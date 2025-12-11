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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 749e5930-6c51-340d-9cb2-2da37d43fbb4 | -2.2145 | -51.88778 | 2025-12-11 12:33:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 54f768a4-e00f-3fb2-923e-7daf3e14b267 | -3.03582 | -42.03177 | 2025-12-11 12:33:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 3360e4f2-a36b-388b-9f69-60a75d35d088 | -1.70191 | -47.46072 | 2025-12-11 12:33:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 970152a9-ee63-3e07-bce7-49d9cd771ff9 | -1.76891 | -54.22375 | 2025-12-11 12:33:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0220b014-0864-31ce-839a-67921c82305f | -2.96103 | -45.00164 | 2025-12-11 12:33:00 | TERRA_M-T | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5670e835-2a3c-3a01-80bf-ab5493f7b106 | -2.21323 | -51.89656 | 2025-12-11 12:33:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 84d194a2-8308-387f-bc40-81f9461e2902 | -2.64352 | -47.71492 | 2025-12-11 12:33:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c3c4ca7a-f15e-3748-8242-84cd6225cb07 | -1.69423 | -48.95976 | 2025-12-11 12:33:00 | TERRA_M-T | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| faea713c-0806-3022-9ff1-ff87daaefb80 | -1.72786 | -49.80907 | 2025-12-11 12:33:00 | TERRA_M-T | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d73c5e32-c69f-3163-89d4-9aa20a0dc6e6 | -1.05431 | -53.6717 | 2025-12-11 12:33:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ef8fbf5b-1ae3-3a42-82f0-eeb24d276a61 | -1.4166 | -47.44747 | 2025-12-11 12:33:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 176747bd-3d68-3305-a622-69e6c5004bb8 | -1.41458 | -47.4619 | 2025-12-11 12:33:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 217f3a68-2af6-33fc-9565-b7ec7f80da79 | -1.58659 | -53.75518 | 2025-12-11 12:33:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0a6759ee-4ba1-3eea-82fa-605a245b061e | -2.14933 | -53.75726 | 2025-12-11 12:36:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ca133b6e-1956-36ac-820e-4103475b9ffa | -3.26426 | -46.40685 | 2025-12-11 12:36:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 418635cb-e708-3943-b608-5932a7ac65d5 | -2.65765 | -51.63775 | 2025-12-11 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 07c085cd-5f7c-3b8d-99de-282f7b0d1329 | -3.1746 | -48.0258 | 2025-12-11 12:36:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9d64b216-77a8-3fd9-8abc-2e5b57c71a64 | -2.65638 | -51.64664 | 2025-12-11 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c310f102-f37e-3667-9666-ace6e4a0679f | -6.03199 | -43.70261 | 2025-12-11 12:36:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| a1b4ebd6-ed12-31ca-9b29-38aeb4b6535a | -4.39411 | -43.02112 | 2025-12-11 12:36:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| bd929ea5-44c4-3b61-9d64-165c2e8bc958 | -4.38939 | -43.05751 | 2025-12-11 12:36:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 359d46f5-498c-3baa-900d-fbff16bd2048 | -5.9809 | -44.59451 | 2025-12-11 12:36:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 0ab847f0-b6fa-3613-9492-e28b74cd732a | -9.83389 | -50.66096 | 2025-12-11 12:38:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cdeab324-b7f6-30db-b0da-3462b4a8546e | -10.47764 | -50.65896 | 2025-12-11 12:38:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 3a06e097-9765-3fee-bef6-641ef81444d9 | -9.03781 | -51.10103 | 2025-12-11 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b9846cfe-62cd-3e5c-ab3b-12a18dc56f6b | -21.00845 | -56.15403 | 2025-12-11 12:40:00 | TERRA_M-T | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ae8eefc-b0a8-3342-8ad1-998635111cde | -22.29896 | -55.07438 | 2025-12-11 12:40:00 | TERRA_M-T | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 93ed6056-d21c-3871-aff7-06dfce8a3fea | -24.28485 | -53.83327 | 2025-12-11 12:40:00 | TERRA_M-T | PALOTINA | PARANÁ | Brasil | 4117909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| b47f438f-09c5-31d3-aa36-5931d7666a18 | -22.02331 | -56.33564 | 2025-12-11 12:40:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 85e93ea5-a139-348d-83df-25cb65c4a44d | -20.70448 | -49.14543 | 2025-12-11 12:40:00 | TERRA_M-T | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ff20f28a-3d7f-39b0-bfa3-e4e7e0673e08 | -22.74504 | -50.38561 | 2025-12-11 12:40:00 | TERRA_M-T | CÂNDIDO MOTA | SÃO PAULO | Brasil | 3510005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 5f776239-3da5-3c3d-b943-5a41064535c0 | -22.27546 | -48.55942 | 2025-12-11 12:40:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| 97c01812-e01f-3309-8646-a11c168897bd | -20.62501 | -53.27632 | 2025-12-11 12:40:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e2203c10-9bed-3ed1-bbbe-38d8b89d1c4d | -24.77562 | -53.90297 | 2025-12-11 12:40:00 | TERRA_M-T | OURO VERDE DO OESTE | PARANÁ | Brasil | 4117453 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 04d77973-2769-3a78-9aff-5c3d23c0fbb4 | -18.79312 | -52.62065 | 2025-12-11 12:40:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 707fade5-807b-39c9-a138-189b5d295c02 | -20.40964 | -49.97699 | 2025-12-11 12:40:00 | TERRA_M-T | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c9dc1902-a731-3377-828c-51ae79f35968 | -25.24479 | -53.97541 | 2025-12-11 12:42:00 | TERRA_M-T | MATELÂNDIA | PARANÁ | Brasil | 4115606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| b32b8078-9610-36bc-9c75-e0641cf1a6b4 | -29.18626 | -54.86496 | 2025-12-11 12:42:00 | TERRA_M-T | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 5.5 |
| d2b5b7eb-8d98-3122-b756-d0c66ab3a5ac | -25.05459 | -53.61058 | 2025-12-11 12:42:00 | TERRA_M-T | SANTA TEREZA DO OESTE | PARANÁ | Brasil | 4124020 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 88f2c6a4-41f3-35fa-8740-b87a955f3a39 | -25.45915 | -49.52446 | 2025-12-11 12:42:00 | TERRA_M-T | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| e9d740ea-53a2-3840-9dc2-d554cf27cac6 | -30.96922 | -55.17333 | 2025-12-11 12:42:00 | TERRA_M-T | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| 54c6e123-66c3-34ce-ab2e-10c7e3262ce0 | -31.91602 | -52.584 | 2025-12-11 12:42:00 | TERRA_M-T | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 8.4 |
| 4a6ec62f-a745-353c-aafd-9b5fcefe3726 | -28.39176 | -53.91618 | 2025-12-11 12:42:00 | TERRA_M-T | IJUÍ | RIO GRANDE DO SUL | Brasil | 4310207 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| f6d05e20-554b-30a0-bfe1-2e82bf5213a7 | -28.30035 | -54.26373 | 2025-12-11 12:42:00 | TERRA_M-T | SANTO ÂNGELO | RIO GRANDE DO SUL | Brasil | 4317509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 4bf4249d-afdd-3681-9fa1-de0810a8367c | -25.34571 | -54.22953 | 2025-12-11 12:42:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b19cc500-b63f-32a6-81e8-90b886298513 | -24.98756 | -53.31614 | 2025-12-11 12:42:00 | TERRA_M-T | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| f29d49e8-2cdb-353e-b1fa-c02519ed5ef4 | -6.559 | -41.7303 | 2025-12-11 12:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 150022b5-bb51-3eba-b2d9-e5674a08cf32 | -2.9201 | -41.9276 | 2025-12-11 12:50:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 3b3a43e8-b05e-399b-9e02-cccf0f1f6e8c | -6.935 | -38.627 | 2025-12-11 13:10:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 96.0 |
| fcd5afb5-e093-3a0c-b6c8-96ec7e9d7d8d | -6.3514 | -41.7734 | 2025-12-11 13:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| b4bccc6e-2515-3e27-be48-ecb7f1cb4e90 | -2.9201 | -41.9276 | 2025-12-11 13:20:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 93.0 |
| e0fd8107-a20e-3464-a193-5ac9decb20ad | -2.9949 | -41.9245 | 2025-12-11 13:30:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 71f74a8c-48e5-37cd-9b74-b369a94441a4 | -6.3514 | -41.7734 | 2025-12-11 13:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 5ffadcc2-22c5-3ecc-b70f-e522bbda355b | -2.9201 | -41.9276 | 2025-12-11 13:30:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 8250d596-c657-3826-9644-0239166f4c60 | -6.935 | -38.627 | 2025-12-11 13:30:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 75c00aa7-142c-35df-ab23-a00ac225464c | -3.0317 | -42.0418 | 2025-12-11 13:40:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 6bb0e2a4-490c-36c8-be64-fde245142a8e | -6.954 | -38.6248 | 2025-12-11 13:40:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 21f21c33-9165-348f-94a4-c9b3a2b23a1b | -2.9201 | -41.9276 | 2025-12-11 13:40:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 52541aeb-4ebb-33fd-970e-0a924b54d63b | -6.3514 | -41.7734 | 2025-12-11 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 95224af0-39a6-328e-8381-ad386306544c | -6.954 | -38.6248 | 2025-12-11 13:50:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 49db6299-e366-3125-8481-1e4255fe9d07 | -2.9201 | -41.9276 | 2025-12-11 13:50:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 343.4 |
| 194f8dfb-1a62-3d9d-95c5-c1a7c0a831f0 | -4.3898 | -43.0328 | 2025-12-11 13:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 14da14bf-18e3-363b-8155-0937b884a5de | -6.9543 | -38.5993 | 2025-12-11 13:50:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 97cf7ff7-1860-34f4-a5c1-55072d334c8e | -2.9941 | -42.0909 | 2025-12-11 14:00:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 46fe33aa-e17b-39ab-845b-e63f3cb85ce6 | -2.9387 | -41.9506 | 2025-12-11 14:00:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 4b140556-e1d0-3bb8-b5ab-ab76785f260e | -0.7284 | -49.4496 | 2025-12-11 14:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 8630447e-7ec3-3f05-9996-6413d30a4f80 | -6.954 | -38.6248 | 2025-12-11 14:00:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 91.2 |
| b25b5403-11d2-37a4-a206-80250e6a46b3 | -2.9201 | -41.9276 | 2025-12-11 14:00:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 151.1 |
| 95650880-c36f-3909-88e9-829fde582f95 | -2.9751 | -42.1391 | 2025-12-11 14:10:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c3bb3935-7d7a-3d07-9b3d-f46c4723babe | -6.9543 | -38.5993 | 2025-12-11 14:10:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 5e1ff11b-24fb-3e8a-b8d6-4a5b4b398c81 | -6.954 | -38.6248 | 2025-12-11 14:10:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 95.3 |
| eae55da3-ee64-3369-b44d-4e422016e28e | -2.9753 | -42.1154 | 2025-12-11 14:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 30e1e3b2-c00b-3dab-a543-21da36802abe | -6.9543 | -38.5993 | 2025-12-11 14:20:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 116.3 |
| ca4d1023-a6ac-36cc-bdba-93661783bc72 | -2.9751 | -42.1391 | 2025-12-11 14:20:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 60e2799b-5df7-3d45-8a1e-c63afc1a73a6 | -2.9753 | -42.1154 | 2025-12-11 14:20:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 315c8f6b-c4d0-39f8-b10b-7fbaa0807bc1 | -6.954 | -38.6248 | 2025-12-11 14:20:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 111.0 |
| 233505b8-6a9a-3bba-aad9-86d27f86ec05 | -2.8058 | -42.4061 | 2025-12-11 14:20:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 400bd48b-c5c5-3d58-a5a7-c1ad4fcbf07d | -2.9565 | -42.1399 | 2025-12-11 14:20:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| bc105b83-9984-311e-8b4b-f26b03268adb | -5.0026 | -41.3062 | 2025-12-11 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 335d7d91-7f8f-3c8d-b27c-bcce5f804f8b | -4.9838 | -41.3076 | 2025-12-11 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 4427b9c7-7862-38fb-b31a-f895b0e1ea53 | -2.9753 | -42.1154 | 2025-12-11 14:30:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 00052f3e-58ac-3f7e-998d-6da6284114c3 | -6.3514 | -41.7734 | 2025-12-11 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 330629b1-94ba-3eb1-b0cd-9d3104b8881e | -2.9565 | -42.1399 | 2025-12-11 14:30:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |


