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
| 4ec76648-7415-3569-ac94-8793c0302d53 | -1.1362 | -48.0989 | 2024-10-18 00:05:12 | GOES-16 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 7d7195a1-e0a9-3921-b37a-463962f4d521 | -1.619 | -47.0919 | 2024-10-18 00:05:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| d97979d1-9ac4-3a21-b433-2f8e0b8e0e20 | -2.188 | -48.7248 | 2024-10-18 00:05:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c95ba555-595c-325b-b6f4-7bc09cff9754 | -2.6105 | -49.4811 | 2024-10-18 00:05:21 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| bac4f73a-39ed-3b03-b0ff-409a6024159c | -2.8611 | -51.6699 | 2024-10-18 00:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 86d6d3e4-604d-357a-bfcc-0314ca673519 | -2.8795 | -51.6695 | 2024-10-18 00:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| fa380afc-bff2-3c95-b2c6-1c7ba2cd9392 | -3.1382 | -51.497 | 2024-10-18 00:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 5ab5f92a-5c54-31ae-a0f4-846d9a32b3cd | -3.1566 | -51.4965 | 2024-10-18 00:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| eabc0666-fffd-3f7b-a223-8585ba43c360 | -3.1567 | -51.4758 | 2024-10-18 00:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5cf9353a-31cd-3d75-8dfc-3bcd4e9ebf70 | -3.2118 | -51.5155 | 2024-10-18 00:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 33b12817-f737-37c0-8bf8-d71e11e8d32a | -3.2862 | -47.133 | 2024-10-18 00:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 0326df17-cf07-3a8d-9725-7f097b84dcc8 | -3.2863 | -47.1111 | 2024-10-18 00:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 3c50398e-c085-396b-8920-e2513571fb6a | -3.3644 | -50.3023 | 2024-10-18 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c35c487a-5738-3191-bd63-bdfa077b0de4 | -3.7007 | -45.9223 | 2024-10-18 00:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 117.8 |
| b77fc3a0-b937-34a2-80f9-169a80d9a898 | -3.7009 | -45.9 | 2024-10-18 00:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 199.7 |
| dc5b55ea-8fa5-380e-b72a-52571ab14a5c | -3.8732 | -52.092 | 2024-10-18 00:05:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8755e640-9e87-3ffe-b637-873e8fd12248 | -3.8733 | -52.0715 | 2024-10-18 00:05:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 8c02f048-bed4-39a3-8247-0e67886aaba5 | -4.2987 | -45.4903 | 2024-10-18 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e55695f8-8bac-3826-916f-e6b7a94332ec | -4.4072 | -45.9773 | 2024-10-18 00:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 1ad060c2-7d76-3399-a72b-d3bcbda10440 | -4.4257 | -45.9987 | 2024-10-18 00:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| bea4aa5b-a120-3e16-8a90-0096990aaae4 | -4.4258 | -45.9763 | 2024-10-18 00:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 288.3 |
| 804e677d-72b0-33fc-908b-981dc2ea51b8 | -4.426 | -45.954 | 2024-10-18 00:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 157.0 |
| af13c963-2669-3ba5-bce4-0c6f856912e8 | -4.5613 | -48.0358 | 2024-10-18 00:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 94d9b0b5-8778-3b8b-a043-d58a7176f9ac | -4.5614 | -48.0141 | 2024-10-18 00:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 3878d334-9981-3e93-bb83-03325ec96b31 | -4.5799 | -48.0349 | 2024-10-18 00:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 5ba4dd2b-34fc-3771-ae91-9417dae96025 | -4.58 | -48.0132 | 2024-10-18 00:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 209c7fa9-2e14-3a6d-862d-3a318d9b3845 | -4.6653 | -46.3418 | 2024-10-18 00:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 851af8f0-ad01-327b-a9e1-56c431ae572a | -4.9397 | -47.0336 | 2024-10-18 00:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 100.2 |
| f0ab1a72-657a-3c3d-ad78-a17cf2b13d01 | -4.9496 | -45.6559 | 2024-10-18 00:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b44440c0-f79f-3c83-84cb-179ff17496c0 | -4.9583 | -47.0325 | 2024-10-18 00:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 2e013ad7-f47f-35af-a909-ab2456587dbe | -4.9584 | -47.0105 | 2024-10-18 00:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 39ad8fe3-2ddd-3e91-9367-ad9774922d7f | -5.23 | -45.5711 | 2024-10-18 00:05:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 80348565-5fb2-3a3e-a1b9-cd874a73bfe1 | -6.9222 | -35.1716 | 2024-10-18 00:05:44 | GOES-16 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.2 |
| c87a3744-8634-381e-8fee-df254bf65fb7 | -6.6703 | -70.1174 | 2024-10-18 00:05:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e25d3edb-4d21-335d-994e-a1532997fb97 | -6.6886 | -70.1171 | 2024-10-18 00:05:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0c33ce49-6feb-35ac-9d5a-0047027665d5 | -9.9675 | -36.3612 | 2024-10-18 00:06:01 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 129.6 |
| a54e3c9a-835d-3bb0-bb60-bc8a0f02eb39 | -9.9869 | -36.3578 | 2024-10-18 00:06:01 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 90.6 |
| aa3a6d3c-aedf-3378-a276-27fbc1fd4bed | -9.5773 | -66.1846 | 2024-10-18 00:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 339baed1-5ad9-3e3c-96be-70b996164a36 | -11.4859 | -65.1198 | 2024-10-18 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e7c4b7c2-d633-3c2b-aca2-b090e6b7d4ac | -12.4966 | -63.2066 | 2024-10-18 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 7cf743f0-caeb-325e-aaab-672fb1d0419f | -12.5147 | -63.3014 | 2024-10-18 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 6d2b5a59-8c5a-3575-a9be-ee1062b839a9 | -12.5149 | -63.2822 | 2024-10-18 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 32dda01f-9fb6-3c37-84a5-b6de29586b5b | -12.5155 | -63.2055 | 2024-10-18 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c0c87fb7-fd43-3ab6-a950-02cefe6358cf | -12.5336 | -63.3003 | 2024-10-18 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 2ccbb957-b730-3627-a43c-f807b4dbf1f2 | -12.5338 | -63.2812 | 2024-10-18 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2f3f8b1c-8f96-3d60-b9d2-6ae353b942f7 | -12.5339 | -63.262 | 2024-10-18 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 6aa19044-3519-38a3-b59f-0aa68db2ca6b | -17.0191 | -57.4768 | 2024-10-18 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 7e2b35f0-a00f-3566-9a09-11bd78e3f4b8 | -17.2177 | -57.3102 | 2024-10-18 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 240434f8-1eea-3bdd-911c-13e01789c020 | -17.237 | -57.3284 | 2024-10-18 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 90422b7a-bb05-39e2-af5b-ce37c8583c8e | -17.2373 | -57.3079 | 2024-10-18 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 197.0 |
| dab14557-0d39-3dd5-8a9b-42df23ec552c | -17.2376 | -57.2873 | 2024-10-18 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 3dc24f0a-c770-3d34-af22-9aee00aa752a | -17.7851 | -57.4679 | 2024-10-18 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 88571071-301c-3825-a221-35e09f18f872 | -17.7855 | -57.4473 | 2024-10-18 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.2 |
| 439118ef-d2de-38b4-82e6-1672b7f9a9af | -17.8049 | -57.4655 | 2024-10-18 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.7 |
| 929a168b-3033-3a11-a2a0-0981bf54dda3 | -17.8052 | -57.4449 | 2024-10-18 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 2f1424a3-054b-3618-827e-8087920c4e0e | -17.8246 | -57.4631 | 2024-10-18 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| e3607d0b-8342-3fa5-8bef-f404318524cb | -17.9036 | -57.4534 | 2024-10-18 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 7dcbbf49-7c78-3aba-a096-df8692793bdc | -17.9234 | -57.451 | 2024-10-18 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.9 |
| b8a84767-2e17-3072-beb6-07d0506d94ba | -17.9432 | -57.4486 | 2024-10-18 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 460bb1fb-0fbe-3d97-b2d5-3448a79590da | -17.9629 | -57.4462 | 2024-10-18 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 10517537-a39f-3171-b4f9-8c690e03c53d | -18.0632 | -57.3514 | 2024-10-18 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |
| bbd80ff5-ea4f-33ab-8430-9e5152ecbe60 | -18.1989 | -56.3608 | 2024-10-18 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 1c0a81ea-233b-3a5a-90eb-3888d78a8c91 | -18.1993 | -56.3399 | 2024-10-18 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| da8ce92d-d991-3e87-a9f0-e2df04a7ea5a | -18.1997 | -56.319 | 2024-10-18 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| bb09f246-b0e7-3860-97b8-270b6f2eb1bb | -18.5495 | -43.2208 | 2024-10-18 00:06:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 6187d042-b032-3698-abbe-54735511a6f8 | -21.9662 | -49.7186 | 2024-10-18 00:07:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 173.5 |
| a9d5847a-3252-3993-8d42-9c44c00fa5e1 | -1.1362 | -48.0989 | 2024-10-18 00:15:12 | GOES-16 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 12a647d9-65b2-3121-bf9e-b532e739169e | -1.619 | -47.0919 | 2024-10-18 00:15:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| f692132b-a1a2-3482-8986-2dbf04ac9add | -2.188 | -48.7248 | 2024-10-18 00:15:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| cb0daef5-73f7-3721-8426-baacaa140bf2 | -2.6105 | -49.4811 | 2024-10-18 00:15:21 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 697f0fa4-00f3-34ae-917b-4090f7890070 | -2.7229 | -54.6556 | 2024-10-18 00:15:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9d86f62a-4da0-3ab1-81ce-5620e24a8a1f | -2.8611 | -51.6699 | 2024-10-18 00:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 8dd8ed58-8156-3942-9e45-1f1351016ca8 | -2.8795 | -51.6695 | 2024-10-18 00:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| bfd1ed44-8d79-3cf7-a133-1b3482a932d8 | -3.1382 | -51.497 | 2024-10-18 00:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 6253b4cd-35cc-316c-a6d6-5f832b14d5a9 | -3.1566 | -51.4965 | 2024-10-18 00:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 0698036e-0f5d-3439-8928-f84fc9833b3a | -3.2118 | -51.5155 | 2024-10-18 00:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 888af23d-fce1-3653-9c4a-232dbc37edda | -3.2862 | -47.133 | 2024-10-18 00:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| f7ad3f0a-fe06-388d-94b2-249e41124737 | -3.2863 | -47.1111 | 2024-10-18 00:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 2941cc8b-318d-3dad-a4f2-a288a0f2d283 | -3.3644 | -50.3023 | 2024-10-18 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 872a5e1b-0111-3c1d-9558-efbd663bef07 | -3.6823 | -45.9008 | 2024-10-18 00:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 6aad3358-d8d2-33de-8385-e9c2d41adfee | -3.7007 | -45.9223 | 2024-10-18 00:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 2ac47ad3-2f7f-3a3c-a89e-c6b1646922cc | -3.7009 | -45.9 | 2024-10-18 00:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 605f98f8-056c-39b7-9ef5-b27def7227b7 | -3.8733 | -52.0715 | 2024-10-18 00:15:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d08052c7-f398-3130-a267-f47adf3cd35b | -4.4072 | -45.9773 | 2024-10-18 00:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 103.9 |
| f2d44b61-af14-3c05-8691-08d2e82019c8 | -4.4257 | -45.9987 | 2024-10-18 00:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 74c877dc-d2e9-38b9-b794-2589b32bb8fe | -4.4258 | -45.9763 | 2024-10-18 00:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 287.5 |
| f0e72cf8-95ca-3b5f-badf-35c024153636 | -4.426 | -45.954 | 2024-10-18 00:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 92d81896-45f5-31f1-b80c-9d36d46ca4ea | -4.5613 | -48.0358 | 2024-10-18 00:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 17d598c1-af32-34c6-9e68-1145dc7a236d | -4.5614 | -48.0141 | 2024-10-18 00:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 293bc38f-cf38-3289-a33b-da8379e9f3d7 | -4.5799 | -48.0349 | 2024-10-18 00:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| be2bc033-eb84-3f62-9582-764a75ff59d2 | -4.58 | -48.0132 | 2024-10-18 00:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 516d55d5-6c5b-31e7-9554-450b36b2a247 | -4.9397 | -47.0336 | 2024-10-18 00:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| fdb019ff-d85e-3e26-99d3-991100ee4e0e | -4.9583 | -47.0325 | 2024-10-18 00:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 1102f3a7-03b0-32c3-9177-09c4c5913f56 | -4.9584 | -47.0105 | 2024-10-18 00:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7fcd6f60-80d6-3736-9fef-47273f3c007b | -5.23 | -45.5711 | 2024-10-18 00:15:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 9f622103-c306-33dc-8ead-39cd57cada3d | -6.6703 | -70.1174 | 2024-10-18 00:15:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ee089d37-11d3-334a-9f37-89a27323606f | -6.6886 | -70.1171 | 2024-10-18 00:15:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1e72713c-c918-35de-94e7-af5468c4fa27 | -9.736 | -36.4017 | 2024-10-18 00:16:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.0 |
| 54cb5170-0fd3-3db6-b07b-6854ee587016 | -9.7553 | -36.3983 | 2024-10-18 00:16:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 127.5 |
| 19e296ce-8f3d-3779-b629-0c2a5277da80 | -9.876 | -36.1077 | 2024-10-18 00:16:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |


[Clique aqui para ver as próximas entradas](README2.md)
