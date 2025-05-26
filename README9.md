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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a9e633c-1f0e-3937-92ce-9e49f3916912 | -12.14876 | -64.15821 | 2025-05-26 06:01:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee90682e-dc57-3501-918a-6c708b7e6d3e | -9.858 | -65.25938 | 2025-05-26 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e93773c6-df80-3c99-9c39-a93a4035e71e | -14.04023 | -55.1277 | 2025-05-26 06:03:00 | AQUA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3cf342ad-0496-3144-a03a-c28322309aeb | -13.78187 | -54.31615 | 2025-05-26 06:03:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ae48ddc2-5f62-3c45-b50f-221f4b67e08a | -19.87473 | -54.36134 | 2025-05-26 06:05:00 | AQUA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 78544a8d-499d-34a7-953b-472d37cfb9e4 | -8.07 | -43.1216 | 2025-05-26 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| 31949587-faf6-3adb-93e1-7b1ce7c700dd | -8.07 | -43.1216 | 2025-05-26 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| fe901684-c2e9-3e3e-8430-2af1a9435d19 | -8.0696 | -43.1452 | 2025-05-26 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 1ae0792d-6257-3d5e-8aba-463b8b0847b3 | -8.07 | -43.1216 | 2025-05-26 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| cdc18eba-e088-3922-b2f8-e2cf2b9fba2a | -8.07 | -43.1216 | 2025-05-26 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 133bb58e-b73a-39fc-8cb4-636659f5e8bb | -8.0696 | -43.1452 | 2025-05-26 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 7ddf820f-378b-3374-a132-7eb29de0bda9 | -8.07 | -43.1216 | 2025-05-26 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 913099ce-a729-3f19-8769-d605fe1c5d45 | -8.0696 | -43.1452 | 2025-05-26 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 29c5ee34-e1cb-3bb2-9bda-0acec0af6208 | -8.07 | -43.1216 | 2025-05-26 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| b75462a1-4011-3564-a349-220dde1d7b5f | -8.0696 | -43.1452 | 2025-05-26 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 47a4008b-f877-32b9-8daf-7f685cfa97ed | -8.07 | -43.1216 | 2025-05-26 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 86f036e7-1614-3058-8d3c-fdc8df74c10c | -8.0696 | -43.1452 | 2025-05-26 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| b2c18bda-3a62-33ee-8af5-5d980acf355a | -8.07 | -43.1216 | 2025-05-26 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 822b7b8a-25dd-3834-a03c-a8105f2e0ad4 | -8.0696 | -43.1452 | 2025-05-26 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 07a380b7-53e4-3ac7-ac02-634c639f0548 | -8.07 | -43.1216 | 2025-05-26 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| bfc8b87b-b651-39eb-89cd-44deb7a9aae8 | -8.0696 | -43.1452 | 2025-05-26 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 337e016f-9e27-3a20-b341-319ff5df40a3 | -8.07 | -43.1216 | 2025-05-26 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 4fad67c8-6724-3ce3-ae3a-6b8e1762e6db | -8.0696 | -43.1452 | 2025-05-26 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| f7f14f43-150b-3e0e-8271-47d5c123cc84 | -8.07 | -43.1216 | 2025-05-26 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 3b5eae78-f994-3247-af3f-8f0b39c45472 | -8.0696 | -43.1452 | 2025-05-26 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 7277c90c-f398-379e-aa97-e900fc167c46 | -8.07 | -43.1216 | 2025-05-26 09:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| ed043a5f-d004-3617-8eff-0393d3659b5c | -8.07 | -43.1216 | 2025-05-26 09:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| a8cda3b2-00c3-3cfc-a550-410d91634445 | -8.0696 | -43.1452 | 2025-05-26 09:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 559e26a5-17c3-3873-836c-b7ff3c69acf7 | -8.07 | -43.1216 | 2025-05-26 10:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| 74d69583-d4c5-30dc-9275-a38d9b864a38 | -8.07 | -43.1216 | 2025-05-26 10:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 153.7 |
| 77e8217c-41f1-3faa-b4f7-26b1a297736a | -8.0696 | -43.1452 | 2025-05-26 10:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 85d69ee5-8411-3246-9b1b-c5b3a08ce602 | -8.07 | -43.1216 | 2025-05-26 10:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.4 |
| ced0205d-8719-35bc-a9ba-189200b6b721 | -8.0696 | -43.1452 | 2025-05-26 10:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.0 |
| d996ee91-94b1-3807-878f-721798e3fa67 | -8.07 | -43.1216 | 2025-05-26 10:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.0 |
| 4c23ef54-7f14-33a6-8f9b-46bd785d0886 | -8.0696 | -43.1452 | 2025-05-26 10:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| 29313c13-bfe6-3c4b-8290-f3018139b692 | -8.0696 | -43.1452 | 2025-05-26 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 922ecd45-c177-332b-8a17-b581b18e0f5f | -8.07 | -43.1216 | 2025-05-26 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 147.7 |
| 2119a9b0-1e95-338c-a740-5e8f55d013ec | -8.07 | -43.1216 | 2025-05-26 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 4eb88cf5-7dbb-3a4b-9a4e-6fa4af12a5fa | -8.0696 | -43.1452 | 2025-05-26 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| dbd1a41d-d5d6-34b8-9fe6-4d5ac0f50e05 | -8.07 | -43.1216 | 2025-05-26 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.6 |
| 63d56c49-e947-3487-872d-a175c7917d60 | -8.0696 | -43.1452 | 2025-05-26 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 74ff63ac-b90a-30fa-8270-3e4ec61782c2 | -8.07 | -43.1216 | 2025-05-26 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.8 |
| f535129f-2b4c-30f6-81aa-08a664accdd5 | -8.0696 | -43.1452 | 2025-05-26 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 167.1 |
| 70c78f0d-aeff-3d88-b6d0-f5477dbc3622 | -8.07 | -43.1216 | 2025-05-26 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 185.9 |
| b81c4ef4-223a-39cc-a7b9-ec4fd435a3bc | -8.0696 | -43.1452 | 2025-05-26 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 176.6 |
| 430c1f7d-d52c-3910-9f47-7710d2f0e652 | -13.6402 | -41.69604 | 2025-05-26 11:23:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 7bca2050-91e1-32d4-8a3a-520da1c8a9bf | -12.4089 | -49.9762 | 2025-05-26 11:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c84a56e3-af0b-3f49-9c00-c00151e40afe | -7.595 | -43.3828 | 2025-05-26 11:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 7124a565-a95a-312f-a9cf-0845d859a13f | -8.0696 | -43.1452 | 2025-05-26 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| b7e17f81-b14f-3d97-8a51-31c2c957bb75 | -8.07 | -43.1216 | 2025-05-26 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.9 |
| 246242e9-8498-3b5d-a928-2f92790158bd | -8.07 | -43.1216 | 2025-05-26 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| de344c5d-8b0c-3934-b3e6-c449a26ead4c | -8.0696 | -43.1452 | 2025-05-26 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 852b36db-8e68-3efd-8b48-0a7f3266b315 | -8.0312 | -43.1964 | 2025-05-26 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 1cf9955c-9873-3fd4-90c5-92828487aa72 | -7.595 | -43.3828 | 2025-05-26 11:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| cd637ee5-a180-38eb-97dd-dae2bf9931cf | -12.4089 | -49.9762 | 2025-05-26 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| b533975d-a849-3a0c-98ad-4cb2dba59324 | -8.07 | -43.1216 | 2025-05-26 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 2fa316eb-5cb1-35ad-8eea-4b24deecdd98 | -12.3526 | -49.9184 | 2025-05-26 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| b3dd1ea8-ebe0-3bb6-80df-5f63733b28b2 | -8.0312 | -43.1964 | 2025-05-26 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 193.8 |
| 7a5a3eaa-3edc-355a-8d37-b1a2eabae85d | -12.4089 | -49.9762 | 2025-05-26 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 6ea48dc8-549f-3b0f-bf77-deca9305f518 | -12.3898 | -49.9786 | 2025-05-26 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f5edc41b-406b-3b46-882f-045d24c80d2d | -12.4089 | -49.9762 | 2025-05-26 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 209.4 |
| cd4a505a-6187-3f9d-91e9-c3a00c9c031d | -12.3717 | -49.916 | 2025-05-26 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 03496d12-95d8-32f0-b87e-b8a3108e1065 | -8.0312 | -43.1964 | 2025-05-26 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.6 |
| 9d3f829c-9d2d-3182-a8c6-6b0ebc0ecce0 | -12.3526 | -49.9184 | 2025-05-26 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 42a08c68-609a-3f9a-b85f-c697d1b19d37 | -12.3526 | -49.9184 | 2025-05-26 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 36034f79-c05c-39bb-84b0-f0838e629094 | -12.3522 | -49.94 | 2025-05-26 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f4dd42e5-600d-3aaf-9690-9c38cd1186a5 | -8.0312 | -43.1964 | 2025-05-26 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 292.7 |
| 4e928f10-7623-3a34-a67d-3a7ff933b77a | -12.3898 | -49.9786 | 2025-05-26 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| cef1fad1-04c2-3fbf-a499-fdc817bc399c | -12.4089 | -49.9762 | 2025-05-26 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 276.2 |
| 784360d5-8c73-3507-ac81-a978c76736eb | -7.9827 | -50.7201 | 2025-05-26 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8077e2e3-2e63-3748-ab92-eb6dacb7e438 | -12.4086 | -49.9978 | 2025-05-26 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| c4116c92-4be3-398d-bfa1-4205256b9049 | -12.3717 | -49.916 | 2025-05-26 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 16c18bd9-d448-3f54-9d8e-827ddefeba66 | -12.3898 | -49.9786 | 2025-05-26 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 01f5f040-8e22-3856-a31f-24243652f541 | -12.3522 | -49.94 | 2025-05-26 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 10a7c12a-e3eb-3212-88b3-2ae56d386e81 | -8.0312 | -43.1964 | 2025-05-26 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 191.9 |
| 41d077d9-aa0a-325d-b2dc-ca790696f3e1 | -12.0703 | -47.3408 | 2025-05-26 12:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| da7754ba-fbb3-3352-b668-f4931d2a1322 | -12.3526 | -49.9184 | 2025-05-26 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 66b7ebc6-88d4-3ab2-80f4-883e1ba474d9 | -12.4086 | -49.9978 | 2025-05-26 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 38d00287-c350-38c7-8ca6-610b59caa4fb | -12.0699 | -47.3632 | 2025-05-26 12:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 8908b86a-6050-3138-af05-f95ffbc4c20e | -12.4089 | -49.9762 | 2025-05-26 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 297.5 |
| 4f029f14-5943-3315-99c9-8bdc78c7cf16 | -12.3526 | -49.9184 | 2025-05-26 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 207.0 |
| fcffb8e6-73b8-3cfa-a19d-0cb83e0a54a3 | -12.0703 | -47.3408 | 2025-05-26 12:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 831111fa-0c8b-3699-a44d-7d4e3967b54c | -8.0312 | -43.1964 | 2025-05-26 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 220.1 |
| 11c0fdbc-02d9-38b5-907d-0898d7921e49 | -12.0699 | -47.3632 | 2025-05-26 12:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a14f6671-bb21-347e-96b5-adb59cbd7c93 | -8.0123 | -43.1984 | 2025-05-26 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| ae220f4c-2d73-3d4c-b141-69663c350cb8 | -12.4089 | -49.9762 | 2025-05-26 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 297.2 |
| e62aa930-b6f9-3603-9c7c-bdd98f82f914 | -12.3898 | -49.9786 | 2025-05-26 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 90b76272-cb41-3274-b35d-203b31d782aa | -12.4086 | -49.9978 | 2025-05-26 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 9a92be25-fdca-367a-b6bc-d62fc36dc3ca | -12.3522 | -49.94 | 2025-05-26 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 1342fce8-e020-3ad6-877e-af72e2ebf358 | -12.4086 | -49.9978 | 2025-05-26 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| f823363f-68e5-3fd1-ab83-b6be561f9245 | -8.0123 | -43.1984 | 2025-05-26 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 581f1e18-7346-3a2e-8543-280249502fd6 | -12.3522 | -49.94 | 2025-05-26 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 404ad914-3b17-3122-a197-10b5817d0a7f | -12.3526 | -49.9184 | 2025-05-26 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 249.0 |
| cd54a37c-d861-38a1-83eb-43bb97233994 | -12.0703 | -47.3408 | 2025-05-26 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| faa12709-37a3-3725-b28d-c20c7adacaa9 | -12.4089 | -49.9762 | 2025-05-26 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 330.5 |
| e816d05c-d220-3386-87a4-e12f35d4f0d4 | -12.3717 | -49.916 | 2025-05-26 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 22bab7c4-eaa8-36dc-9299-2cd6fe8bfcdf | -12.0699 | -47.3632 | 2025-05-26 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 24267af9-2322-33f7-9f14-f39734c252db | -7.541 | -43.1774 | 2025-05-26 12:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| c45b53d3-9935-3932-b2ef-ad8ad202a7ce | -8.0312 | -43.1964 | 2025-05-26 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 283.1 |
| 9a7b52a6-9b67-3a10-bd09-7b4a19fafef7 | -12.3898 | -49.9786 | 2025-05-26 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |


[Clique aqui para ver as próximas entradas](README10.md)
