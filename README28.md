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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef9b3c52-fe93-3216-bcdb-f1e21546b9fa | -10.8512 | -46.67146 | 2025-07-27 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e8039907-1402-36eb-8cb0-90a098437eb9 | -10.84793 | -46.69879 | 2025-07-27 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| d2e921c0-1fae-3955-9ad6-1eb22e30131b | -13.5049 | -45.50948 | 2025-07-27 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 66682ee9-57c2-3dda-9bec-f8fffd5d19ba | -14.97551 | -46.97654 | 2025-07-27 12:51:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 87cca110-7daa-3e55-930f-d63234a6940e | -10.13591 | -46.70825 | 2025-07-27 12:51:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| e69d794e-de6d-382c-9d48-9321978ea95a | -12.00641 | -45.82928 | 2025-07-27 12:51:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 58cb973c-d4db-3820-8c52-f9d5d9f54ed9 | -12.01526 | -45.83533 | 2025-07-27 12:51:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ea5823b7-b63c-30d4-8799-69ff84484ea2 | -14.97809 | -46.97257 | 2025-07-27 12:51:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| fc8346c0-7ee6-392a-9b7c-acf79d8930bb | -11.98344 | -46.70651 | 2025-07-27 12:51:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 29c35f34-6a01-3189-8980-61cf7479bdda | -9.85783 | -53.23399 | 2025-07-27 12:51:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 353c52de-b950-3af7-8330-6dfb7f5844f7 | -13.11076 | -47.31388 | 2025-07-27 12:51:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 5a912ce6-0aaf-37ac-af84-9c663cbb1900 | -8.01978 | -48.15856 | 2025-07-27 12:51:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b46e0cfd-929c-3b3c-8815-4d8182f6f6df | -12.67615 | -47.00744 | 2025-07-27 12:51:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| d5134b08-0a47-3ec1-be48-f65dcf2f8a03 | -12.6611 | -46.99871 | 2025-07-27 12:51:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 47c926dc-8eb8-3618-a5bd-46a777f1efb0 | -9.03297 | -45.38963 | 2025-07-27 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| ace3dc86-ff64-3de3-8d1c-6a938874b883 | -10.85181 | -46.67669 | 2025-07-27 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 6178aa73-c47f-3c23-bed2-e1d1f91f1e49 | -14.96269 | -46.97171 | 2025-07-27 12:51:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f10cc3a3-2469-38dd-acde-fe28f38834b0 | -11.87628 | -55.44877 | 2025-07-27 12:51:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9b3bf512-83d4-3541-a0cf-1252bd5bbba2 | -13.50092 | -45.54704 | 2025-07-27 12:51:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 2fe1f166-94f2-361b-8f22-4c850b1f4290 | -10.84874 | -46.70404 | 2025-07-27 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 831135cc-8b80-33de-b8c2-72353de2a59a | -8.01576 | -48.17068 | 2025-07-27 12:51:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f623cbca-5c07-3383-abc0-e245ad70b6ad | -19.00404 | -51.40219 | 2025-07-27 12:53:00 | TERRA_M-T | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 12e88343-98a4-311b-97d8-36f03f3da44f | -21.60597 | -57.578 | 2025-07-27 12:55:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 0eed7bc6-b740-313f-8cf5-a3677cba3e6c | -21.60736 | -57.56852 | 2025-07-27 12:55:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bfec0069-c6d8-3900-899e-c343dc0825fd | -21.61481 | -57.57944 | 2025-07-27 12:55:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 981abb1b-aca3-3a5c-8021-abb02e0da620 | -4.9643 | -43.7182 | 2025-07-27 13:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 49d8bfa5-a09f-3e42-822e-5aa82bb46e15 | -4.9454 | -43.7425 | 2025-07-27 13:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 2de307bd-d651-3b54-8ff6-698278a5ad9f | -4.9641 | -43.7413 | 2025-07-27 13:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 219.5 |
| cfdeed5a-e86c-350d-9db4-2b8c4dd545f0 | -6.6759 | -58.846 | 2025-07-27 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5ac8c4a8-5315-3ba8-9e89-a0af294373a9 | -4.9454 | -43.7425 | 2025-07-27 13:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| a51e2a61-3477-3b82-a7ac-362f4a1e5ecb | -6.639 | -58.8475 | 2025-07-27 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| e2dab166-50e7-353d-9041-6a4434d577f9 | -6.6575 | -58.8468 | 2025-07-27 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 6c1c0fe5-2e5b-3730-a1a3-7304e2e1ad21 | -4.9643 | -43.7182 | 2025-07-27 13:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 2721867b-54eb-3ed9-8194-e55fe9740b2b | -13.5077 | -45.5105 | 2025-07-27 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| db77c991-1f47-3111-88a4-40654145c692 | -4.9641 | -43.7413 | 2025-07-27 13:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 5e27af1c-42b0-31c6-9556-330787324d39 | -6.6575 | -58.8468 | 2025-07-27 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| d77109f4-d19a-3f7f-b67f-0369395b67cf | -6.6759 | -58.846 | 2025-07-27 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| baf908a0-d724-30b9-bfcb-2f9e8e772097 | -4.9643 | -43.7182 | 2025-07-27 13:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 0bc958e7-fefe-3b76-bb39-e41fff2c90a3 | -13.5077 | -45.5105 | 2025-07-27 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 587fb540-9e8a-371c-bfc5-c525ff1d8694 | -5.7483 | -43.9406 | 2025-07-27 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1bf89490-6cd0-380d-b2af-2cc5bf4807dc | -4.9641 | -43.7413 | 2025-07-27 13:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| d6174435-df6e-3794-8911-c52a27867ba1 | -6.0095 | -44.0591 | 2025-07-27 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4ae146ef-9542-34df-818b-e2cf6d5d3fd7 | -6.639 | -58.8475 | 2025-07-27 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| d78ee419-899b-3d1a-a5fa-21349a3c6ede | -4.9454 | -43.7425 | 2025-07-27 13:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| e9bd0a7e-a423-3c96-88ef-7e64befce109 | -4.9454 | -43.7425 | 2025-07-27 13:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 3c0bd86d-eb1b-3d6c-b791-4a124f3e3322 | -6.639 | -58.8475 | 2025-07-27 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c9f67799-4878-3542-b83b-b5a0b6cf23de | -13.5077 | -45.5105 | 2025-07-27 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 64434297-ba92-3c39-8333-5b513dae494d | -7.0886 | -44.909 | 2025-07-27 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| aea97883-700c-3c8c-8105-03ec1984ff7e | -4.9641 | -43.7413 | 2025-07-27 13:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 153ce418-af6c-37bb-9446-811c0b3b791f | -6.6759 | -58.846 | 2025-07-27 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b2c84658-4498-3818-ae2f-01460397f3f4 | -6.6575 | -58.8468 | 2025-07-27 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 3e657f53-c054-3990-be03-3b0efe6fa5c2 | -6.6576 | -58.8274 | 2025-07-27 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 89434a75-64e3-3688-9e5c-cc6cc501d576 | -4.9643 | -43.7182 | 2025-07-27 13:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c469c391-6f07-32d4-9f73-8143e596cbff | -6.639 | -58.8475 | 2025-07-27 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| a7d41c5c-c6f2-3d93-8a78-32c7c898c38f | -7.0041 | -42.3567 | 2025-07-27 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 3a56d002-5f55-3348-ae28-442784dfb007 | -12.67 | -47.0092 | 2025-07-27 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4de8b3fa-4925-37a8-8b4d-167d50c9ed6c | -6.6575 | -58.8468 | 2025-07-27 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 75b8c37c-7d58-3c18-bbbb-31931874a6f1 | -6.6576 | -58.8274 | 2025-07-27 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 7ee4f8eb-61f7-37fe-bb41-689e72f8e019 | -8.5055 | -47.4885 | 2025-07-27 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4fe84e67-6187-3116-91ed-726c15c6a669 | -7.0886 | -44.909 | 2025-07-27 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 9c92fa70-db55-38a5-96c4-7d6071645bec | -4.9641 | -43.7413 | 2025-07-27 13:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 79e4e2d2-4da5-33a9-b295-9f3e6a53eddf | -6.6759 | -58.846 | 2025-07-27 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| bd80808d-6c67-36e0-8bfb-242e79398f04 | -4.9454 | -43.7425 | 2025-07-27 13:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 4ef1cf85-4fdf-3abd-9761-80ac2eb482dd | -13.5077 | -45.5105 | 2025-07-27 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6309a21c-af32-3f9c-b9b4-987a5ef305c4 | -3.4 | -43.0148 | 2025-07-27 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| dc043416-619c-3ba4-a222-55e1f693b85e | -4.9643 | -43.7182 | 2025-07-27 13:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| a56a9b06-9ea8-31ac-9892-1d068b7119f7 | -12.67 | -47.0092 | 2025-07-27 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 25fbf557-8fb6-3fee-980f-7abdb5e5283e | -5.944 | -45.0704 | 2025-07-27 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 013d027d-06bd-3259-88db-4b3e6f77d919 | -5.9627 | -45.069 | 2025-07-27 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 49240242-8ee9-3d07-b9e0-0edf2cc4a03c | -8.5055 | -47.4885 | 2025-07-27 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 754c12ae-253f-3fcf-b221-0c5ec669b7c6 | -6.6575 | -58.8468 | 2025-07-27 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 8630567f-a9d3-3271-8e74-fed6a3f87032 | -7.0886 | -44.909 | 2025-07-27 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| ca60889f-ecc8-3918-a0fd-c5af0f96ec37 | -6.6391 | -58.8282 | 2025-07-27 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 74971276-907f-3597-a280-be06c30b06fe | -6.639 | -58.8475 | 2025-07-27 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 4f5d4785-38be-3230-a07d-357cb1f84146 | -4.9454 | -43.7425 | 2025-07-27 13:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 5c7329ae-3bfb-37df-b56d-17ee003ac2b7 | -13.5077 | -45.5105 | 2025-07-27 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| a7601679-43ef-39f7-89d8-2376ebad96c2 | -4.9641 | -43.7413 | 2025-07-27 13:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| af719a7b-55a6-36f0-ac16-d97bbe4542a3 | -4.9643 | -43.7182 | 2025-07-27 13:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1ac4596f-4bc0-35ab-82c6-fb9f858ff433 | -6.6576 | -58.8274 | 2025-07-27 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7c8d9445-5150-3aff-a246-e2d3715e4032 | -6.6759 | -58.846 | 2025-07-27 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b292ca97-b82f-3ad6-818c-c72971b86d30 | -7.1074 | -44.9074 | 2025-07-27 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 834307d3-13c7-3446-a3de-308e268ee760 | -7.0886 | -44.909 | 2025-07-27 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| b635b2dc-79aa-3593-992a-93bab6aecd6e | -4.9454 | -43.7425 | 2025-07-27 14:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| e05115ab-c25f-30b7-92df-2c5d1345c092 | -4.9641 | -43.7413 | 2025-07-27 14:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| d21217e5-4bae-31c2-927c-6eae8e96afdd | -4.9643 | -43.7182 | 2025-07-27 14:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| fd7f12da-43e0-3e13-b6f0-6854296ae7ce | -7.0886 | -44.909 | 2025-07-27 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 6dc7560f-6800-3a2d-842f-529291578b2b | -7.0041 | -42.3567 | 2025-07-27 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 2c4d7f71-0bff-3f03-be14-bd3466af2e47 | -12.67 | -47.0092 | 2025-07-27 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 3509c928-23f2-3643-8abd-6ba140efbd1d | -5.9627 | -45.069 | 2025-07-27 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 55a24948-c4e4-3534-814c-332d065df1e6 | -4.9641 | -43.7413 | 2025-07-27 14:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 49294b76-5294-3ab8-a574-771a47229b75 | -4.9454 | -43.7425 | 2025-07-27 14:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| a8e1f899-cdd0-3720-927c-e76ac1f14903 | -4.9643 | -43.7182 | 2025-07-27 14:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 380f7b32-534a-3ed7-8241-c8dab8f6c001 | -7.1074 | -44.9074 | 2025-07-27 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 3ed92b3a-f3d5-3791-843a-9aa597c5941b | -14.9714 | -46.9811 | 2025-07-27 14:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 57ba9d93-05e6-3a95-a441-2f29afb70159 | -7.0886 | -44.909 | 2025-07-27 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| bb291453-1d3d-321b-8d8b-dd7b56d605f7 | -7.0041 | -42.3567 | 2025-07-27 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| bbffa64e-85e6-3545-a92c-6f82a47a8ccd | -5.9627 | -45.069 | 2025-07-27 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 8195358f-9a2a-34a4-aa1d-ff095d76bc67 | -12.0203 | -45.8115 | 2025-07-27 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fd148ae5-c861-39a5-8ea5-6f18c2ec520f | -4.9641 | -43.7413 | 2025-07-27 14:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| c384927e-44fa-3ffc-b83d-c1dc16061c4b | -5.944 | -45.0704 | 2025-07-27 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |


[Clique aqui para ver as próximas entradas](README29.md)
