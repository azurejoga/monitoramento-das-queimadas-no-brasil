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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee909a92-9a9e-379f-914a-64f4321851e2 | -0.8918 | -51.7245 | 2024-11-14 00:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 39.9 |
| c26d1623-0003-3a3c-bec1-8a52c8e3e915 | -17.6066 | -57.551 | 2024-11-14 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 21983b0c-0d61-3aae-b877-8c50817c3efe | -1.3895 | -51.099 | 2024-11-14 00:40:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| a919a086-d717-3d29-9838-f3d39b0ee2ca | -17.5869 | -57.5533 | 2024-11-14 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 183.6 |
| 56d70b12-9bca-368d-a456-e57d0e7dd3b4 | -9.3649 | -35.6534 | 2024-11-14 00:40:00 | GOES-16 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 60.9 |
| 877de40e-db01-3273-9de4-9b3ad3fd207b | -3.0504 | -50.3332 | 2024-11-14 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 260b86d9-cd20-3682-84cb-89c7395e68c3 | -3.6402 | -50.5863 | 2024-11-14 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| af94f85f-eac3-338f-af53-0ece880f3f19 | -2.675 | -47.0003 | 2024-11-14 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| b0023006-33d9-32fc-a471-a13964ac2c20 | -17.5872 | -57.5328 | 2024-11-14 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| e2142e51-3f20-3d39-bd3b-6b76e050498c | -2.6564 | -47.0008 | 2024-11-14 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 3e3452d6-ab97-3bff-8f4c-e545209a7add | -2.6751 | -46.9783 | 2024-11-14 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 91b4cbf3-de64-3d23-a1a3-f87c849207fc | -1.3894 | -51.1197 | 2024-11-14 00:40:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e7cec347-3133-382d-ab4d-baa1d05a4dc5 | -4.0867 | -50.0021 | 2024-11-14 00:40:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c0897df0-752a-35df-8a88-cf824d0ca302 | -1.4078 | -51.1195 | 2024-11-14 00:40:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 3fe64e38-df75-3130-9770-62da9d073346 | -2.0268 | -46.9299 | 2024-11-14 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| efd90990-40e6-3942-abbc-0b6f00894fad | -17.2543 | -57.4698 | 2024-11-14 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 2a4ec5e2-b2fc-3983-a9c9-88101b13ee09 | -4.0005 | -45.5503 | 2024-11-14 00:40:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 6cc738b3-afc9-3c22-bf24-1c31b226dfd1 | -3.6587 | -50.5857 | 2024-11-14 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 11cf20e1-1339-3df0-8e90-469427eea24e | -3.1464 | -45.2729 | 2024-11-14 00:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 3a5b85b9-7400-32c2-8f97-6f4a054bb1fb | 1.2852 | -60.4454 | 2024-11-14 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| bd4372e5-d9a0-3dd0-9115-af85a9123892 | -1.3874 | -52.3555 | 2024-11-14 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| c61c822e-3f66-3758-bbc4-1d133958c5c8 | -3.0523 | -45.5237 | 2024-11-14 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 50724f70-0ede-3cc2-9055-06d2df62464b | -3.4014 | -50.3011 | 2024-11-14 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| aa2fe814-ca65-3048-999e-865bf35f3746 | -0.9102 | -51.7243 | 2024-11-14 00:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 7ab8177b-5440-3a5e-9077-8ae15dfa4a57 | -5.1836 | -44.3485 | 2024-11-14 00:40:00 | GOES-16 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 95922997-4c2f-382a-b562-ccfcf1463dbb | -3.4198 | -50.3005 | 2024-11-14 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e26194da-a4f7-39cc-8dee-211d5a1b5ca0 | -3.6401 | -50.6073 | 2024-11-14 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 3c6edf77-6f79-3915-a32a-70cd52f3dca7 | -5.2023 | -44.3473 | 2024-11-14 00:40:00 | GOES-16 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 4223d137-2fa2-3061-b0aa-6e4f63cf85df | 1.2852 | -60.4265 | 2024-11-14 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c6587f69-b766-3767-a33a-54f550a688f2 | -3.714 | -50.6046 | 2024-11-14 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 785723fb-e987-3157-bc4f-38853c1ccb48 | -2.8975 | -51.7927 | 2024-11-14 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| bfae59f8-a874-3f11-a1b7-d88389d4f7ca | 2.6703 | -61.169 | 2024-11-14 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 7535586e-eba9-33ee-9118-bb4c37a43611 | -4.0191 | -45.5494 | 2024-11-14 00:40:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3c738358-d496-39a2-b98b-89d251ec9767 | -3.1278 | -45.2736 | 2024-11-14 00:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 2a191df0-d821-30ea-98cc-330181dcc6b1 | -17.7052 | -57.5392 | 2024-11-14 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 05b48ab3-5b66-330f-b485-2668ef00adba | -3.1244 | -50.31 | 2024-11-14 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3a932146-f553-355a-8030-dd3f4854cbae | -1.3873 | -52.376 | 2024-11-14 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 329a5d86-0d76-379b-baff-113fe3afad72 | -3.7809 | -52.0952 | 2024-11-14 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e29cf703-01af-3b2f-a94a-b6f4635ef035 | -6.0472 | -44.0331 | 2024-11-14 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 06994ef6-ebc7-3233-b489-d65d6e05a77a | 2.6703 | -61.1879 | 2024-11-14 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 42.5 |
| f0acecfc-ee21-342a-b2f7-dfb138385b7e | -2.8791 | -51.7932 | 2024-11-14 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 83f331fc-7aca-3213-b5fe-974e1af07f33 | -4.0189 | -45.5719 | 2024-11-14 00:40:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 2ea0803a-cb44-3863-a13d-8bf7e10880eb | -2.6565 | -46.9789 | 2024-11-14 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 368a70ba-5932-393c-9f62-ed81c596fcec | -4.0003 | -45.5728 | 2024-11-14 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 53d09d83-6da9-3fc6-bf19-8a9d70d92d1c | -3.0522 | -45.5461 | 2024-11-14 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a6e5987f-cab8-3312-be8c-91c151c01e50 | -17.6263 | -57.5486 | 2024-11-14 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| 2937e7ae-96a8-3530-b371-65e380bf6a82 | -10.0641 | -36.3441 | 2024-11-14 00:40:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 0ef4a93c-2ab6-3748-9a47-8613d4b91c7a | -17.5675 | -57.5351 | 2024-11-14 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| 574a1135-809e-3fc4-9e08-7ad819ab4bc5 | -0.34 | -52.0359 | 2024-11-14 00:40:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c7990f8c-c720-316d-8e62-833710525a10 | -17.5672 | -57.5557 | 2024-11-14 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 0d2ece63-f4cd-36e9-b004-90e6eba4892f | -2.0267 | -46.9519 | 2024-11-14 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| ec90ed3f-1475-371c-acea-386526abcd96 | -0.2299 | -51.5011 | 2024-11-14 00:40:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 43.3 |
| f1e3d47b-5eb6-3a26-a2fc-ae4eea0eec1d | -1.85779 | -46.28537 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8a16773d-d634-3997-baa4-871f05c3f71f | -2.78786 | -45.95876 | 2024-11-14 00:41:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24abf1a2-d038-3b9e-b70b-b34c65a9f1fc | -6.87724 | -44.76372 | 2024-11-14 00:41:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 22b7ceb1-d19f-36ed-9952-e1a7185e4dde | -2.71037 | -47.72802 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 76114478-a8a1-3ecc-a5eb-58894b7ad730 | -2.90371 | -46.85735 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| c8648036-f21d-341b-807d-94fe248a6e7f | -4.16614 | -46.25875 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 81f6ec69-e8eb-3c07-9e67-9dd3e82087cd | -3.16775 | -45.44314 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 63086fdc-9271-3c9b-beff-477c3e753ae0 | -3.24294 | -50.40049 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4e63daf7-02e7-3281-8b5e-cf6ba5e31b23 | -6.03139 | -48.04272 | 2024-11-14 00:41:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| fed6ca42-a0e1-38ac-8f89-ee3e9067012f | -3.4397 | -43.89811 | 2024-11-14 00:41:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 908f6e63-ce1f-36c1-82c0-3532f05466e6 | -3.40204 | -50.31483 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 4bcc1214-81fc-323b-a122-3e5bfa10c870 | -4.45552 | -45.36401 | 2024-11-14 00:41:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a7692890-cb96-3e76-a53e-c04ec35c052e | -5.35161 | -45.57178 | 2024-11-14 00:41:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ea24120a-b04f-35d8-8e5f-073e7c2eab59 | -5.48374 | -47.00611 | 2024-11-14 00:41:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8d04e137-2c45-33c7-9b3a-b801df27d8ad | -4.00376 | -45.55767 | 2024-11-14 00:41:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 562da68b-8792-36d7-a3fa-b419559ef61d | -5.11229 | -44.00241 | 2024-11-14 00:41:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b844c4e5-9fa5-3921-bca7-b66ade90f40f | -1.93862 | -46.28295 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9253df33-664f-3ed8-b81d-c5a9fb1de555 | -4.26066 | -47.07858 | 2024-11-14 00:41:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2c4a24d6-ddd8-3209-8964-da6e545a64f8 | -3.1766 | -45.44189 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 8a934d79-2e16-3f93-bd97-92eb821ada4e | -2.52667 | -45.34199 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e836876c-58fa-39f6-a693-0bf8f7c55790 | -2.3661 | -46.49809 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffff5504-623e-307b-a410-e3aecc9b8381 | -3.23332 | -45.38292 | 2024-11-14 00:41:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb4d2db3-539b-30f8-8a40-8bae1ee9911d | -4.51771 | -46.47495 | 2024-11-14 00:41:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e91b8e6c-929f-357c-aa5d-4f0d26f1d8ea | -2.40961 | -45.22814 | 2024-11-14 00:41:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ac930db2-176d-3053-8a6c-cfb1129eac42 | -3.01325 | -45.1273 | 2024-11-14 00:41:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4427a242-f59e-3fe9-b247-c6e66b34308b | -2.02138 | -46.9409 | 2024-11-14 00:41:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 434c3461-5de7-3244-a4fc-ea7e3715065c | -5.34888 | -46.02232 | 2024-11-14 00:41:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 09bdb262-4242-3359-80af-097e58c5c757 | -2.67762 | -46.81837 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 14ea6492-6f0a-3991-a472-3f59cfeb7776 | -4.04477 | -45.72258 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 75624ea6-72c6-3516-9727-6425306087fd | -5.33202 | -46.09765 | 2024-11-14 00:41:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3448ed42-5c06-3fe3-8394-90815de61dda | -5.85589 | -46.42779 | 2024-11-14 00:41:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51bb13c7-4b31-30bc-bc6f-1a273cc02928 | -4.6128 | -46.29911 | 2024-11-14 00:41:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b631d0ef-c137-3c12-ac01-9f7ec50f2e52 | -4.3015 | -48.10263 | 2024-11-14 00:41:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| df08b585-d562-3f67-8c37-43e910d1eefd | -4.61405 | -46.30808 | 2024-11-14 00:41:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| db93cb0e-3fda-37df-a5f4-07a8a5d3624c | -3.08336 | -45.43435 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 48df7495-8121-3a87-8ec3-d0bbdee08158 | -5.19865 | -45.40764 | 2024-11-14 00:41:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 25da4930-75a6-3eab-9bf6-4c51153f779b | -5.95292 | -39.68446 | 2024-11-14 00:41:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 40442643-efdc-3993-8950-c59bba84542d | -6.07334 | -44.87934 | 2024-11-14 00:41:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba10fd69-ece0-3326-bbc0-910720fd672a | -1.44795 | -47.78542 | 2024-11-14 00:41:00 | TERRA_M-M | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 32d47847-7eac-3c35-b6db-25ab16ded9a3 | -2.84827 | -46.65422 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbeb41a1-2594-317a-99e1-bdc3d30ed2b9 | -4.75707 | -46.01184 | 2024-11-14 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6fa25732-033e-317d-976c-968f229daa48 | -2.90497 | -46.86641 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 9dcfa3ea-9aef-3496-b0fc-62a56b557cee | -3.57667 | -45.60365 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b4d34fda-1b79-32d8-91b1-eeabb3df568b | -3.03246 | -45.06985 | 2024-11-14 00:41:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ed42352a-0f06-3732-964d-6e18f364700a | -5.61327 | -46.40562 | 2024-11-14 00:41:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0541fee8-cb08-3791-89f5-0faafc64123d | -2.64216 | -46.17102 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| face111c-357a-319c-9306-9310096e9bdc | -2.88906 | -51.7945 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a50c4545-5591-3d97-911c-82e7fe6c755a | -4.21004 | -50.69579 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README9.md)
