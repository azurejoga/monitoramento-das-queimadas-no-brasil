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
| 9bcbba8d-375d-3d4b-8c8c-f36eb9baaddf | 1.4681 | -59.9309 | 2026-02-27 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| be9c4bfb-9410-36c0-8607-416585b222db | 1.4864 | -59.9308 | 2026-02-27 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| cc08fa1f-567c-3fc6-900c-9330f9b1c7a9 | -18.9825 | -52.93889 | 2026-02-27 00:24:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2dee9183-1831-3957-8f0b-ef3a667c53e7 | -18.98077 | -52.92371 | 2026-02-27 00:24:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d7f1f383-def7-3b19-94c4-776c67e78251 | -18.9841 | -52.9249 | 2026-02-27 00:26:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e36bfebb-6562-3aca-84a7-bbe3877ca0c6 | -21.808599 | -52.7188 | 2026-02-27 00:26:00 | METOP-B | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 19d6bdbd-6b23-326c-9f31-f92e47afc579 | -21.179701 | -56.478199 | 2026-02-27 00:26:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c2ab0e2f-294b-3cc5-a90b-9b69028f13d6 | -21.6658 | -56.313202 | 2026-02-27 00:26:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0cf269e4-0284-39d4-b1dd-ced0d82fe053 | -18.9825 | -52.916901 | 2026-02-27 00:26:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b5facac4-3f6e-3e57-87f6-511d52e10e4f | 3.14769 | -60.47047 | 2026-02-27 00:28:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6e1f897a-6547-327a-a250-bab4ff2b5ee9 | 1.4681 | -59.9309 | 2026-02-27 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.5 |
| df496375-dd98-3677-af92-d9d23e8c6c12 | 1.4864 | -59.9308 | 2026-02-27 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.2 |
| b286f77e-c711-36e8-a47d-60f9ba027955 | 1.4864 | -59.9308 | 2026-02-27 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 8b86dcf2-4def-37d1-b55f-78f909f8af84 | 1.4864 | -59.9308 | 2026-02-27 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 04d52bea-2694-3fad-90fe-a4817e52bd6d | 1.4681 | -59.9309 | 2026-02-27 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ed4521e1-d061-3973-a21c-f99ee0cf6776 | 1.4681 | -59.95 | 2026-02-27 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.0 |
| eb12c85f-e89f-3bcc-a4ad-879c6ab420cb | 1.4864 | -59.9117 | 2026-02-27 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 7cb5d766-99cd-391c-a8c7-c8fe8062d441 | 1.5046 | -59.9306 | 2026-02-27 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0005f11c-6cdd-3b86-b9c7-867d09c62f6c | 1.4864 | -59.9308 | 2026-02-27 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| cd29060a-426a-3243-ad2e-f76025b235ad | 1.4864 | -59.9308 | 2026-02-27 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 15aced0f-24e2-3d01-8aa7-6d19273bf035 | 1.4864 | -59.9498 | 2026-02-27 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9052030b-f1b5-3d30-bfb0-cdf2d8c6722e | 1.4681 | -59.95 | 2026-02-27 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| a117e643-c4a3-3ef4-bfcb-c350b36d5a10 | 1.4681 | -59.9309 | 2026-02-27 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3a1c9369-9512-3ea3-a14b-59356ad75cde | 1.5047 | -59.9116 | 2026-02-27 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d06c9604-ca2f-3ab9-a37d-2bf2724bf387 | 1.4864 | -59.9117 | 2026-02-27 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 30fd7877-ba85-33b9-810c-d7a987d2d81e | 1.5046 | -59.9306 | 2026-02-27 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e77a56c1-d447-3031-a76a-2659dc4d3b4a | 1.4864 | -59.9308 | 2026-02-27 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 97b74983-52be-34f9-8b82-fa09b6f43070 | 1.5046 | -59.9306 | 2026-02-27 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4de460af-df3d-3c26-8caf-abcfd98033e4 | 1.4864 | -59.9308 | 2026-02-27 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 314d3f8c-8e6e-3a6f-afc2-61e5fb0e5471 | 1.4864 | -59.9117 | 2026-02-27 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c900e12e-9c4b-3485-9f3d-1ab6b5510859 | 1.4681 | -59.95 | 2026-02-27 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 093800dc-c36f-39ee-adea-8bf361cf7f41 | 1.4864 | -59.9498 | 2026-02-27 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6d7b90d0-d074-3449-85ed-f5f529198eac | 1.4681 | -59.9309 | 2026-02-27 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.0 |
| b6f96deb-662d-3fe8-9f95-6b573d145bb6 | 1.5046 | -59.9306 | 2026-02-27 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 2ae868f5-9acf-33a5-96fb-fe3bff13ff36 | 1.4681 | -59.9309 | 2026-02-27 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 98706d53-b1e0-384b-88df-92b6807cd878 | 1.4864 | -59.9308 | 2026-02-27 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5b69c13f-29a0-3d6b-8d5e-de19644dbfe2 | 1.4864 | -59.9498 | 2026-02-27 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| bf7da030-2736-391f-953f-18324e0e2fcc | 1.4681 | -59.9309 | 2026-02-27 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.0 |
| b98dc7d3-de95-3773-b6a0-8cc0cbc6de52 | 1.4864 | -59.9308 | 2026-02-27 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f9223802-bd29-35c8-9760-febeab2a79fa | 1.5046 | -59.9306 | 2026-02-27 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| db3c2567-5001-3be0-8654-a40305cf9cbc | 1.4864 | -59.9498 | 2026-02-27 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 2e8a54e4-01ff-361c-a783-3e166bddf789 | -9.61291 | -35.81149 | 2026-02-27 03:19:00 | NPP-375D | SANTA LUZIA DO NORTE | ALAGOAS | Brasil | 2707909 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d86abe00-e160-3033-a5f0-c81f3a5a150d | -9.8114 | -36.59922 | 2026-02-27 03:38:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5dacdbdc-ffcb-3fd5-bb36-2f07cec0535f | -9.2392 | -35.62365 | 2026-02-27 03:38:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7a2b23e7-994c-3376-af45-e708bf3f7d34 | -9.23862 | -35.62724 | 2026-02-27 03:38:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5948b199-e284-3a1b-90fc-69bfbebf343e | -9.24255 | -35.62421 | 2026-02-27 03:38:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| d164bd05-0f5e-3823-8a4f-0e1aa09aadd0 | -9.61382 | -35.80644 | 2026-02-27 03:38:00 | NOAA-20 | SANTA LUZIA DO NORTE | ALAGOAS | Brasil | 2707909 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 30f01570-c4d7-3dff-8c04-17936f8236cd | -9.24197 | -35.6278 | 2026-02-27 03:38:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| dcd0d7f3-7f91-33c1-bacc-9b298cdc7216 | -9.61324 | -35.81005 | 2026-02-27 03:38:00 | NOAA-20 | SANTA LUZIA DO NORTE | ALAGOAS | Brasil | 2707909 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5f75a9cb-a8d2-3ce6-8531-75d1dad59f5d | 1.4864 | -59.9308 | 2026-02-27 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 215.3 |
| 80e37b54-16ab-354a-b19a-ce164ad10dc1 | 1.5046 | -59.9306 | 2026-02-27 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 155.1 |
| 4a834bc4-07b7-39d8-8c0a-1a4cbbc1ee24 | 1.4681 | -59.95 | 2026-02-27 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.4 |
| a2ead373-2bb4-3cae-b4cf-33b7376ae17f | 1.4681 | -59.9309 | 2026-02-27 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.7 |
| c1e5ad25-dbc7-332e-9e13-dee8a32713b9 | 1.5046 | -59.9497 | 2026-02-27 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 35af06d9-bc63-30a1-89cc-528f365161c6 | 1.4864 | -59.9498 | 2026-02-27 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 7752a855-2506-3dd8-8bd4-47db6eb6ba42 | -10.49691 | -36.71179 | 2026-02-27 04:27:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d59524fb-0df2-3a85-800e-f0f7d07d5618 | -16.91744 | -52.36773 | 2026-02-27 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3867f09-7451-3ae4-a98c-47d9f84dfd36 | -16.91762 | -52.36683 | 2026-02-27 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4d46fb5-2f98-3530-826b-6d42603f1bbb | -23.39188 | -51.12786 | 2026-02-27 04:31:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d0562ed4-5bef-3215-9e35-4c6a8486de04 | -20.69247 | -56.54251 | 2026-02-27 04:31:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 68e9cb00-88b7-3fa7-b2c8-e1309127b819 | -22.17147 | -57.51828 | 2026-02-27 04:31:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e934c864-f1e1-3637-86c2-e7b45d038ab9 | -21.1761 | -56.49683 | 2026-02-27 04:31:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d5711ec-36f2-354f-8d85-0e47bf8664a9 | -23.71541 | -54.95633 | 2026-02-27 04:31:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee3aafd0-7e6b-3259-9a3b-875b85e0a113 | -21.17178 | -56.49588 | 2026-02-27 04:31:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 943a1485-1cfb-3893-9d0b-107c7339f4d0 | -21.8194 | -48.70428 | 2026-02-27 04:31:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2957dd22-4a15-327d-887f-7f9381f390d2 | -21.17066 | -56.49597 | 2026-02-27 04:31:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a430034d-b919-3991-9e24-8cc79f60f991 | -21.77983 | -49.83333 | 2026-02-27 04:31:00 | NOAA-21 | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 31bd1099-328c-340c-bd8b-f3c17bf37706 | -23.72951 | -54.94392 | 2026-02-27 04:31:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b920202f-16ba-39a9-88ac-218bef430705 | -23.20779 | -49.40904 | 2026-02-27 04:31:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73658974-5723-33e5-ab92-4e8cff40ebad | -18.9802 | -52.92671 | 2026-02-27 04:31:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2812cf67-ba8f-3bd7-bc8c-97c5aac21cdf | -21.17498 | -56.49693 | 2026-02-27 04:31:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8a93cac-578f-326b-9878-ecb4ec93463f | -21.66151 | -56.32748 | 2026-02-27 04:31:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a651677a-d88a-38b8-9e48-81ac5465f47f | -21.53207 | -49.5237 | 2026-02-27 04:31:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 046476b6-6683-39b0-b2df-ce7689ca06f7 | -18.97942 | -52.93117 | 2026-02-27 04:31:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad95ce52-f50a-35d1-8bc3-e51ef2c36418 | -21.66236 | -56.32322 | 2026-02-27 04:31:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 329fa723-f706-3758-8948-8484b1bbf834 | -24.10954 | -54.31234 | 2026-02-27 04:31:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7c6d0adf-dc77-3caa-b987-8962d3259c19 | -24.11009 | -54.31 | 2026-02-27 04:31:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6376af13-861d-3311-ad82-e6f321ee2a47 | -18.97578 | -52.93045 | 2026-02-27 04:31:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e38224d-a814-35fd-91ef-b331cf3464a9 | -21.80249 | -52.72972 | 2026-02-27 04:31:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d78aa786-958a-3554-95a6-645113346b07 | -27.6868 | -48.75021 | 2026-02-27 04:33:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 53873a70-85f0-391a-9194-91785b3d8c45 | -29.08354 | -55.14021 | 2026-02-27 04:33:00 | NOAA-21 | UNISTALDA | RIO GRANDE DO SUL | Brasil | 4322376 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 4a02832c-954d-3458-a05b-a4bc545b4b6d | 1.4864 | -59.9308 | 2026-02-27 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 235.1 |
| 7f44dde0-2c56-3e4e-b364-350596956f9c | 1.4681 | -59.9309 | 2026-02-27 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 946120e9-3aeb-35c1-a836-145449f79aa0 | 1.5046 | -59.9306 | 2026-02-27 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 9e2f1c89-763d-3148-b673-9a8bef8cd127 | 1.5047 | -59.9116 | 2026-02-27 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b7394206-6b90-3a36-a51d-af507aef655f | 1.4864 | -59.9498 | 2026-02-27 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 35b4d551-bc03-3559-9c7b-a01f7579a421 | 1.4864 | -59.9117 | 2026-02-27 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9a655fb4-ee48-38db-838a-363c2bcb8175 | 1.4681 | -59.9309 | 2026-02-27 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 28f90f8f-5b17-330d-b075-beeeae453e17 | 1.4864 | -59.9498 | 2026-02-27 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 9953325c-637d-346b-8d4a-a7410feb0af4 | 1.4864 | -59.9308 | 2026-02-27 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 216.2 |
| 1813ef20-e8e2-305c-aba3-860823439bd8 | 1.5046 | -59.9306 | 2026-02-27 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 124.5 |
| f3ba6a1a-22c1-317d-ab29-93e74b40882a | 1.5047 | -59.9116 | 2026-02-27 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ea52a135-c75b-3399-bbb6-77ec083163c0 | 1.4864 | -59.9117 | 2026-02-27 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 444d2220-f45f-33d2-a3ee-b1f0eaafbb06 | 1.51632 | -59.93982 | 2026-02-27 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3958d127-9045-3626-8f7c-66e93ea70d2a | 1.48745 | -59.9302 | 2026-02-27 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e29cb37a-50f2-345c-90fe-7e34d5701ff8 | 1.49435 | -59.93944 | 2026-02-27 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a03c205-098f-349f-864b-ee412b9c886a | 1.48262 | -59.93436 | 2026-02-27 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 56e7be61-286d-3fd3-8fd7-3a3192fb44bc | 3.04741 | -60.02716 | 2026-02-27 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9727248c-8bdc-3392-b105-28b6ba426170 | 1.49332 | -59.93273 | 2026-02-27 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6790cd18-7f33-35ae-9167-6557142dd1ee | 1.49866 | -59.93189 | 2026-02-27 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README2.md)
