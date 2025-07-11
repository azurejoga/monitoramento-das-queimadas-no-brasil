# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f9eb63c-38f6-3d66-abd8-cac180f4efba | -10.5776 | -49.1316 | 2025-07-11 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| f8d99ce1-81c7-3500-b8a0-1fe2088337ac | -5.5614 | -43.9082 | 2025-07-11 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 9e407da1-a585-3d24-ae8b-3e0187bcc9f4 | -5.5427 | -43.9096 | 2025-07-11 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 6b0b00f7-0cc2-37ab-bd02-b42aad38895e | -9.9148 | -47.8282 | 2025-07-11 00:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 565a99ed-dcb8-3a84-97d8-142b51e8f656 | -23.3066 | -47.392 | 2025-07-11 00:00:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| 83c1d2a6-d7d8-387b-9274-42e41238a3d2 | -7.2025 | -43.1171 | 2025-07-11 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.0 |
| 00fa11ef-d6d0-3811-9185-73a4d2e68134 | -10.8429 | -49.1236 | 2025-07-11 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 756bdd41-5403-3c7d-bcd7-5542e8e96c46 | -5.5616 | -43.8851 | 2025-07-11 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| af91a4e9-176f-3fd0-a467-e1c291a4303d | -9.8958 | -47.8303 | 2025-07-11 00:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 47f7d6b3-f4c8-3296-9b13-250334654690 | -9.9145 | -47.8503 | 2025-07-11 00:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 44778f51-a7df-354c-be75-40934ccb8614 | -9.9151 | -47.8062 | 2025-07-11 00:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f83c2ccc-f616-37fa-a999-ae4ca0887384 | -7.1837 | -43.1189 | 2025-07-11 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| f71918b3-7e5d-36cf-ab26-7b2ef0dd9a51 | -7.9562 | -49.6615 | 2025-07-11 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ffd8ab10-aacf-363e-8941-145e93b5c09e | -10.6672 | -49.4895 | 2025-07-11 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 203.7 |
| ab6ae084-89d2-34f3-9064-9965e9944926 | -10.8619 | -49.1214 | 2025-07-11 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 6d535937-b251-3dab-8553-c9b56de2c444 | -23.3058 | -47.4162 | 2025-07-11 00:00:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| 90a7aff4-ba8a-3b48-8ac0-248d23c9e788 | -10.6862 | -49.4874 | 2025-07-11 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 155.8 |
| e5b6f92b-24f1-3ef4-875b-c8c3e5a4c3b9 | -5.5429 | -43.8864 | 2025-07-11 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 6ed88410-a0cb-32df-8a80-c6e3f486f447 | -10.6862 | -49.4874 | 2025-07-11 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 275.6 |
| bc980d44-4d9a-378c-bd8f-fcf6bc8b6755 | -9.9151 | -47.8062 | 2025-07-11 00:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fc6df911-8ac9-35e8-8267-1208dbd03a41 | -9.9551 | -64.9548 | 2025-07-11 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f2c147ad-6f17-3205-9126-fef2707c9aa1 | -5.5429 | -43.8864 | 2025-07-11 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 3efc4992-4e07-3321-b17d-df5d8aac8cf6 | -5.5614 | -43.9082 | 2025-07-11 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 32e113cc-1332-33e2-8cc3-c8c5f02380a8 | -10.6859 | -49.509 | 2025-07-11 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 30d5334c-adbf-39f8-9b2b-b44983a038ac | -10.6672 | -49.4895 | 2025-07-11 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 740f5858-5b16-3cae-8daa-3f43f757d7da | -5.5427 | -43.9096 | 2025-07-11 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 81662ce4-ec5a-3a7b-8461-3bf8899c30dc | -9.9148 | -47.8282 | 2025-07-11 00:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 205.5 |
| 30b263a5-fa08-384c-87b9-07b388178f61 | -10.5776 | -49.1316 | 2025-07-11 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 89197a19-6213-3886-8d24-e1b8c595605a | -5.5616 | -43.8851 | 2025-07-11 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| ca27c025-7e3a-3510-b8a5-49b3dc90d2f1 | -10.8429 | -49.1236 | 2025-07-11 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 0d7ce520-be5e-3870-9a9e-fca971981705 | -7.2025 | -43.1171 | 2025-07-11 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 157.8 |
| f268f9cb-05ef-3e9e-9c9e-3ccaaeb1c3d7 | -9.8958 | -47.8303 | 2025-07-11 00:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| fe17fdfa-9234-3d80-8a6f-ba5a93a9d273 | -7.1837 | -43.1189 | 2025-07-11 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 0e4d42c2-8476-3296-b22e-4a8a48908233 | -9.9145 | -47.8503 | 2025-07-11 00:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| d4bcede8-0a8e-3114-9ca2-3af9816820b3 | -10.8432 | -49.1018 | 2025-07-11 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c97ea349-a17b-30c9-b1f1-a88b0108837c | -5.5427 | -43.9096 | 2025-07-11 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 03907071-5f62-3614-a339-8337969fd2a5 | -7.2025 | -43.1171 | 2025-07-11 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 156.8 |
| 56584f56-6d09-3afd-925e-1a643bfdb87c | -9.9551 | -64.9548 | 2025-07-11 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| fd382896-18c5-3b0d-842a-9c9a8be48ed6 | -7.1837 | -43.1189 | 2025-07-11 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| d09f45c4-7a94-3022-9242-614c3bab9a5c | -10.6859 | -49.509 | 2025-07-11 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| bea2a103-c19c-3c7c-9fd9-ce6d785ee5e6 | -9.9148 | -47.8282 | 2025-07-11 00:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 268.2 |
| da67907a-fdbd-3e76-9542-e722962fcbc5 | -9.9145 | -47.8503 | 2025-07-11 00:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8033e9eb-f8a1-3752-85e3-d536062d84fe | -22.2852 | -54.9409 | 2025-07-11 00:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 854be974-2817-3279-8b94-3d5e2b4c30b3 | -10.6669 | -49.5111 | 2025-07-11 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| fd66f301-70b4-36e9-8661-ca55f464d959 | -10.8429 | -49.1236 | 2025-07-11 00:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 93785485-ac21-3950-a2aa-4a2fb6860266 | -5.5616 | -43.8851 | 2025-07-11 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| ae15e727-6738-339c-b486-daec1e6aeb54 | -10.6862 | -49.4874 | 2025-07-11 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 227.5 |
| 65d02afe-7274-3e32-ad8b-e64ab974093a | -5.5429 | -43.8864 | 2025-07-11 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 173b11ce-854b-3cbe-abe5-2ea4dc1c5f1d | -10.6672 | -49.4895 | 2025-07-11 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 9705dd08-9cc3-3a47-bdcb-bce2cbbb292c | -10.5776 | -49.1316 | 2025-07-11 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 700f6f03-eaf0-3a73-b9d8-76edeb49b720 | -22.2645 | -54.9446 | 2025-07-11 00:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7c393a97-9d79-3563-be31-6a0ba32c81ea | -9.8958 | -47.8303 | 2025-07-11 00:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| b7b979c0-c99b-3635-9d54-3c7ba609792e | -10.6865 | -49.4658 | 2025-07-11 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 6ad8fdff-abd3-3303-b6d5-1bad4c8f3400 | -5.5614 | -43.9082 | 2025-07-11 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| a8805227-ede4-3798-8ed4-aa0510310b42 | -9.9145 | -47.8503 | 2025-07-11 00:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 706dc3ff-04e4-35fa-b37a-a012f7e270da | -10.6672 | -49.4895 | 2025-07-11 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| d106478c-c21b-3812-bece-7edbe66b4019 | -9.9148 | -47.8282 | 2025-07-11 00:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 319.4 |
| c596defe-bd29-3cfa-b96f-a4645200c4e2 | -10.5776 | -49.1316 | 2025-07-11 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 25176634-5b0b-37eb-8ab1-a74ae6ecdc25 | -22.2847 | -54.9627 | 2025-07-11 00:30:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 7cfa4632-b06c-3cef-b87a-51d0c206c86d | -7.2025 | -43.1171 | 2025-07-11 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| ffaf9018-e1a3-3a24-9b03-7974622ac0de | -22.2645 | -54.9446 | 2025-07-11 00:30:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 0f4969a9-3977-341d-8ca2-056edb674b89 | -22.264 | -54.9664 | 2025-07-11 00:30:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 91ea9bf6-e92a-34c2-bfae-9b671fd3d467 | -9.8958 | -47.8303 | 2025-07-11 00:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 43e25d80-32ab-382d-a17d-a885df46ff0f | -10.8429 | -49.1236 | 2025-07-11 00:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| f7bd651b-efcd-3329-9f43-11c8be5b3a7a | -10.6669 | -49.5111 | 2025-07-11 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 59ca7ec3-1783-38e8-88a1-283165444dd3 | -5.5614 | -43.9082 | 2025-07-11 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 8bc5ddb6-2fab-3623-b801-3c9832608058 | -22.2852 | -54.9409 | 2025-07-11 00:30:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 150.6 |
| ac71aa66-d8d8-3ea1-8d21-6ae96dfd17a6 | -10.6862 | -49.4874 | 2025-07-11 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 212.7 |
| c3f25913-d50c-32f4-87bd-fbfac5b6ac30 | -9.9151 | -47.8062 | 2025-07-11 00:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| ade2640f-e22f-3516-8018-b526f987733e | -10.6859 | -49.509 | 2025-07-11 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e76d3f00-6802-3736-b9de-44cff61812e3 | -10.5965 | -49.1295 | 2025-07-11 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 928eb1ec-092e-38ab-961c-feedb270984b | -5.5427 | -43.9096 | 2025-07-11 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 6cc3f5d2-b27e-3a7e-a754-6690a36c720b | -7.1837 | -43.1189 | 2025-07-11 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 486a283b-43a5-3d3b-a849-01fc02c60b74 | -5.5616 | -43.8851 | 2025-07-11 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| c86240d1-7f99-366f-9a1e-bbbf4a5866ed | -5.5429 | -43.8864 | 2025-07-11 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| cbc6803a-795c-3a37-85b4-39df9fe2bde3 | -10.8429 | -49.1236 | 2025-07-11 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 64aed2f2-f705-3b13-8c9f-786dd93fc8cb | -22.2645 | -54.9446 | 2025-07-11 00:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d0d46ae8-50a1-364e-8c52-442dc1cf84a0 | -7.1837 | -43.1189 | 2025-07-11 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 35cda2f0-d7bb-3f73-9ff1-b524901506c8 | -5.5429 | -43.8864 | 2025-07-11 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 61c2bee6-e9a7-3cc0-bd5f-acf37b7b9e8e | -10.5965 | -49.1295 | 2025-07-11 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5f1c89aa-88e9-3970-a66f-1bb9605152f9 | -9.9148 | -47.8282 | 2025-07-11 00:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 303.5 |
| d047a5d2-2fe7-3452-8534-57a4eb729f9c | -7.2025 | -43.1171 | 2025-07-11 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| d7c0e615-3b21-34d0-aef6-5fbc475bf1db | -10.5776 | -49.1316 | 2025-07-11 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| f95fd5cf-a6f2-3696-9635-c0fa8ee53817 | -10.6859 | -49.509 | 2025-07-11 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 362a8888-261e-333e-a730-b7bf22db47f9 | -5.5427 | -43.9096 | 2025-07-11 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 9b0633fb-3ec9-3837-bca4-1132260254fb | -10.6672 | -49.4895 | 2025-07-11 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 164.9 |
| ec239252-4c98-330d-9325-ff2f0f7dba91 | -9.9145 | -47.8503 | 2025-07-11 00:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| bf5cb532-a9ef-3542-bd7b-f47a90b6f081 | -9.9151 | -47.8062 | 2025-07-11 00:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 26f3ec11-f9de-3753-98fa-28f8a32e27e9 | -5.5616 | -43.8851 | 2025-07-11 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 6e87af23-fc60-344c-8143-15d5729edcda | -9.9551 | -64.9548 | 2025-07-11 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2705c5c1-93c3-3844-9dc3-e086ad184959 | -9.8958 | -47.8303 | 2025-07-11 00:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2161ba57-431c-3d8d-a8fc-1a1c42ee0597 | -22.2852 | -54.9409 | 2025-07-11 00:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 4b2d85c1-22c9-3cc3-8e46-53184cf90e92 | -5.5614 | -43.9082 | 2025-07-11 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| dd044b53-0c30-386a-b779-0cde4f2828ef | -10.6862 | -49.4874 | 2025-07-11 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 218.1 |
| c5ba0c74-c0af-33e5-ac08-7e0edea6a127 | -12.0181 | -49.525501 | 2025-07-11 00:41:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2eedf66a-39f1-356c-ae41-94355d1645c6 | -10.8591 | -49.1278 | 2025-07-11 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac1b154-f8fc-3c25-b07d-9ace35ed1539 | -7.9485 | -49.6516 | 2025-07-11 00:41:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1f23fc7-8f99-33d8-addf-5f026f44e05c | -11.3399 | -45.222198 | 2025-07-11 00:41:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5282d5b2-7dd3-3963-b750-971293009674 | -4.5968 | -47.725601 | 2025-07-11 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d1a8702-11b1-347f-b09b-694270a2a7af | -7.2039 | -43.360699 | 2025-07-11 00:41:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
