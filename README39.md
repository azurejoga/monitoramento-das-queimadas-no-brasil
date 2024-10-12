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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1570e2b-7499-3f45-b181-e96a6b9bf5de | -17.627 | -56.3318 | 2024-10-12 03:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 772eab1c-b67f-3918-ad00-03a9ac2c9e2f | -17.6467 | -56.3292 | 2024-10-12 03:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 9c68d278-e920-3388-a03c-5fe89943fe62 | -17.6679 | -56.2435 | 2024-10-12 03:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 4e1291fe-b47e-3682-85da-9e2d14bb8bb2 | -2.8254 | -51.3401 | 2024-10-12 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 7e1a8aab-68e7-378a-adee-c76e78616e6e | -2.7885 | -51.3618 | 2024-10-12 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 034ad082-3015-32d4-b000-90350004fa9e | -2.7884 | -51.3825 | 2024-10-12 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b406403d-8cd8-3d64-a48a-8e0217879395 | -2.7701 | -51.3622 | 2024-10-12 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9aa641a5-a2ce-30d5-8e38-06fdeb712f0e | -2.77 | -51.3829 | 2024-10-12 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 63cdbab0-ed2e-3c3d-8ee3-cda6a9b924f3 | -3.6978 | -50.1225 | 2024-10-12 03:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 8e0a266c-49dd-3107-84c5-db9f57e9a6e3 | -3.958 | -46.4442 | 2024-10-12 03:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 37.9 |
| a8ba18eb-4793-31a1-aa32-bc67df2d6113 | -3.9396 | -46.4229 | 2024-10-12 03:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 384891c7-ccc5-3688-8432-c513779745e3 | -3.9394 | -46.445 | 2024-10-12 03:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 95bb26ae-cde3-38d0-8adc-b1a3d61df57d | -4.4538 | -44.5763 | 2024-10-12 03:55:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| c21ec2da-1b83-37f9-985a-594ff651c79f | -4.5859 | -47.0968 | 2024-10-12 03:55:32 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 436bb012-1497-39f5-b3b3-669ec160488f | -5.2486 | -48.0424 | 2024-10-12 03:55:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 98188cda-306c-3b7a-8fc6-e6f979a28e62 | -5.3997 | -45.3574 | 2024-10-12 03:55:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 9d1d046c-4e98-3a86-accc-35070c31ac21 | -5.381 | -45.3586 | 2024-10-12 03:55:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 480911f6-518a-3cb6-8574-958d0248d459 | -6.747 | -59.3259 | 2024-10-12 03:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 6f90e7a5-381a-303c-abcf-c288c8009214 | -6.7469 | -59.3452 | 2024-10-12 03:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| beab3ee1-c6a3-32bd-988b-0042675c494e | -7.8901 | -54.7004 | 2024-10-12 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d8da0dc1-fef7-3b5d-99fb-ee3389d3cb0d | -7.89 | -54.7206 | 2024-10-12 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 44cda160-0bb2-3183-9a50-f2d3d2f1178b | -7.8717 | -54.6814 | 2024-10-12 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 82314e91-d5d5-3851-bd30-b63e5c01eb1f | -7.8715 | -54.7016 | 2024-10-12 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 42fde4c2-c426-3a1e-a4eb-6ad82e82820d | -7.8713 | -54.7217 | 2024-10-12 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 4b1e5b71-e4c2-32d2-92d5-fa1074cdbd4e | -7.8529 | -54.7027 | 2024-10-12 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e7d94277-7125-334d-998b-7e2f05d97df5 | -8.4231 | -55.4704 | 2024-10-12 03:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 70c300a4-7014-3ddd-8b14-b7d5921f3cd5 | -10.9697 | -44.6504 | 2024-10-12 03:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 90bb3f3d-3349-30c3-8be6-3a4adc04783c | -10.9506 | -44.653 | 2024-10-12 03:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 7a4c2a8b-2c66-3788-9e91-52ca04ec40e3 | -11.8377 | -58.8445 | 2024-10-12 03:56:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 1bbce604-6dc9-3482-8cd2-a78030929f83 | -12.456 | -54.5554 | 2024-10-12 03:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 44e4657c-08f1-3b11-b7ef-994242f542f8 | -12.4558 | -54.576 | 2024-10-12 03:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 0d11d9c2-4a8a-3c3a-b279-1aeeb1f57ce8 | -12.437 | -54.5573 | 2024-10-12 03:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ee2b7a99-9fab-377c-9403-0a637094f209 | -12.4367 | -54.5778 | 2024-10-12 03:56:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 3b8c3abf-9ab7-323c-9187-afa7eeef291c | -12.8893 | -53.5194 | 2024-10-12 03:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f79246fc-6c45-3836-ab97-5dc8f4219971 | -12.8135 | -53.4861 | 2024-10-12 03:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 31c0f7d0-e651-3a63-9d40-055a9e2c4aaf | -12.8132 | -53.5069 | 2024-10-12 03:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 23125751-ad07-35b6-9124-eb3a90ee84b4 | -12.8129 | -53.5277 | 2024-10-12 03:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 87090f72-1132-3992-894b-bae13b88419c | -12.7941 | -53.509 | 2024-10-12 03:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 37165ab2-1bf7-304b-888b-c0edb57d3e0e | -12.9658 | -53.511 | 2024-10-12 03:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 7553a987-63d9-3990-b38e-1ce90239eb17 | -12.9655 | -53.5319 | 2024-10-12 03:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 219.9 |
| 25060f16-10ce-3ad3-9510-5d14e632ef3d | -12.9652 | -53.5527 | 2024-10-12 03:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f73632f9-72d9-3b99-a52f-c1df8bac28e1 | -12.9467 | -53.5131 | 2024-10-12 03:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 9f307e7d-03d9-3b0f-b610-9034dc2f1bd3 | -12.9464 | -53.5339 | 2024-10-12 03:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 175.4 |
| c9380c4f-d27f-3206-9171-0962369acaff | -12.9461 | -53.5548 | 2024-10-12 03:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3819d6e2-76c0-34b9-a57e-daa1fa0f00ce | -14.3246 | -57.6002 | 2024-10-12 03:56:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 366a43b7-9b25-33db-9f8e-9cee6b685cb0 | -16.9805 | -57.4404 | 2024-10-12 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 6783d05d-5731-31ac-b737-863341bb5b94 | -17.1761 | -57.4585 | 2024-10-12 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 601761da-c6e4-3ead-86f4-5beb90d4d5f0 | -17.1758 | -57.479 | 2024-10-12 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 708aaf8e-b068-3a6a-aff1-1154a208a59b | -17.6471 | -56.3084 | 2024-10-12 03:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| a25da0ea-80cb-355a-81b9-ca7f661c6bbc | -17.6467 | -56.3292 | 2024-10-12 03:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.4 |
| bcdbf458-c2d7-32ca-9881-9fb7ef40eea8 | -17.6679 | -56.2435 | 2024-10-12 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 46bb1989-8e20-39bd-8065-43bdef4e66dc | -17.9841 | -57.3612 | 2024-10-12 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| b103a161-51cc-3d0b-b9a2-4d5752885bbc | -17.9837 | -57.3819 | 2024-10-12 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 94c15be0-054e-33ae-8f7d-e88caf6491b3 | -17.9643 | -57.3637 | 2024-10-12 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 0ad9601b-f63b-3925-b535-94349d10942a | -17.964 | -57.3843 | 2024-10-12 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.2 |
| 79658a41-6446-3f83-a91a-f7ae0282b2d5 | -4.82732 | -37.83688 | 2024-10-12 04:04:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47dce65f-adc4-33da-a5e4-d4ceb31d8005 | -4.72498 | -37.8449 | 2024-10-12 04:04:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2a5859f-9b30-37dd-bb32-2a7e589e6605 | -4.12148 | -38.42853 | 2024-10-12 04:04:00 | NOAA-20 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b89d4e3-d4d2-38e7-b8e0-5c294b22306f | -5.3704 | -37.78049 | 2024-10-12 04:04:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dda60a6f-35cd-31cd-a929-5f1b208a5254 | -5.27772 | -38.14959 | 2024-10-12 04:04:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a1a8c9ff-738e-3970-ad3d-7c35ba454b57 | -1.63456 | -46.2535 | 2024-10-12 04:04:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ced1454e-08c4-3ee0-9c3f-4339b3ecf6d0 | -3.69126 | -50.12556 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4757f51f-45e3-3bbe-a173-a4218d652fbf | -1.87936 | -54.43423 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9c90d138-914c-33fb-93b8-c5191d0bb2de | -5.21264 | -37.88587 | 2024-10-12 04:04:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3e5dd223-7617-3cdc-8015-340a5840c11d | -5.209 | -37.88532 | 2024-10-12 04:04:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c5405ac-a58c-3658-89dd-d30573f30a62 | -5.17877 | -37.98843 | 2024-10-12 04:04:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46585e3d-617c-31ae-9d53-4d6569ac2aa2 | -5.17744 | -37.98926 | 2024-10-12 04:04:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c238425-7bca-305e-b4eb-259c2f2694c0 | -3.46163 | -39.58459 | 2024-10-12 04:04:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de82ecc6-0bf9-3c64-b8c6-ae6422b8b736 | -4.78039 | -39.77628 | 2024-10-12 04:04:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a265253b-5f3b-3e1b-948f-e7ba23f66cf7 | -3.71751 | -39.13439 | 2024-10-12 04:04:00 | NOAA-20 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d47a8a54-62e4-3126-8383-51167aa5785a | -2.90301 | -40.44199 | 2024-10-12 04:04:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6fc5aed9-cd9a-3642-bba9-5cfc3cee50ab | -4.01917 | -40.40813 | 2024-10-12 04:04:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d73bb1e-70b8-377f-8db7-db490d2f6523 | -4.01694 | -40.4007 | 2024-10-12 04:04:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c75fb59c-07ac-35f2-8320-6b86d4966e1e | -4.0164 | -40.40416 | 2024-10-12 04:04:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8d0b239-d8b1-3d18-b746-f4d0ac37246b | -3.76955 | -41.00339 | 2024-10-12 04:04:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9402dd62-e4cd-3b33-8d61-c0669b38e1ca | -3.76127 | -40.99154 | 2024-10-12 04:04:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 725582e9-a9ed-3b8e-9bc1-f11688e3e6e7 | -3.75797 | -40.99103 | 2024-10-12 04:04:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d994bba-f4ec-3640-88d1-028b12deca52 | -3.93227 | -42.40765 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5046b0f4-4878-3dfc-8eaf-a2b43097b10d | -3.9317 | -42.41125 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46029a8b-acfb-396c-a38d-876a876390a8 | -3.93113 | -42.41484 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb6bfa2c-61ce-3396-ac57-2d8c761916f2 | -3.93057 | -42.41844 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e2586cda-621e-388f-bf17-706de4acc525 | -3.92947 | -42.40352 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dae017e3-a1da-32e9-b072-d9f6bd13b13b | -3.9289 | -42.40712 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7625f83e-1728-3f28-8bc3-0749b81d2f97 | -3.92833 | -42.41071 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 921b4c9b-6cbc-3f4c-9713-b030681e57e0 | -3.92776 | -42.41431 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5039d119-25ae-3d44-9102-adb17cbcf1ef | -3.92719 | -42.41791 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65f85040-77f0-36a0-9b0b-f8541cf9732e | -3.92609 | -42.40298 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 53cc27c2-6144-389a-9608-d9374ec96e34 | -3.92553 | -42.40658 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| d20ebf99-2155-3ad0-8774-c6d4d378f69e | -3.92496 | -42.41018 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 1cafe2b2-3877-33c6-930f-36fa248c8e2a | -3.92439 | -42.41377 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| aaee19f0-d36c-38db-9a61-f0e94cd83a21 | -3.92382 | -42.41737 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 99bd544b-87ef-36c7-86ee-fffe040d316d | -3.92325 | -42.42097 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 94383d80-fea2-37e0-bc6a-2d73f55e4384 | -3.92272 | -42.40245 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 498935c8-33ac-325c-b566-c772cef76a5a | -3.92215 | -42.40604 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 68b874f4-360d-3a00-9615-1f6ff97bd2b8 | -3.92159 | -42.40964 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 7c43d4a7-7702-3ddf-95be-c5f476c93195 | -3.92102 | -42.41324 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| d96fbbae-ae2b-3249-9d7d-52073c2a9a36 | -3.92045 | -42.41684 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 47294073-4de0-3681-9c82-33affe1f28a4 | -3.91988 | -42.42044 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e8be2889-29ff-3c33-8de7-af782b129891 | -3.91878 | -42.40552 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 857884ef-e02a-3a64-a565-b79258705922 | -3.91821 | -42.40911 | 2024-10-12 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README40.md)
