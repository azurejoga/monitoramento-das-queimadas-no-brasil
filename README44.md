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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c49f7d1-31b6-3f1b-8d2f-428395660e01 | -4.31386 | -47.51403 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 42543ec8-43e3-3d35-b038-eb50e81a6a1a | -3.07494 | -49.49997 | 2024-11-26 05:22:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 79b7fea8-cd8c-3a1b-b681-d77d1ba6db2e | -3.96742 | -48.09224 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d6ca61c2-fa88-34b9-be67-616a75c3a430 | -3.46641 | -47.68122 | 2024-11-26 05:22:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f3d2c7bf-1acb-3c33-8e38-3f111a3a963e | -4.31536 | -47.50421 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d9537e59-1d19-313f-859f-86777559ae2f | -6.17834 | -43.41514 | 2024-11-26 05:22:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a52bcb6-00a6-3b35-b835-dc4fe9fa168a | -5.75555 | -47.80979 | 2024-11-26 05:22:00 | AQUA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 77a58b00-b89a-38ac-908d-391164ff699e | -3.96098 | -48.06971 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 2787150a-2d2d-3521-b256-068af461b233 | -3.97387 | -48.04983 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 583fbdf2-c0a4-35d2-9cfe-20a4dde372b6 | -3.96423 | -48.04843 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8ed7d9b3-f60e-3b30-bc1c-80651285832d | -3.98348 | -48.05144 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 17108666-8bb2-3f68-87f4-ab3a21040955 | -3.18773 | -48.43294 | 2024-11-26 05:22:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d88808db-97b7-3a8d-8f98-d0f30caac7e6 | -2.71687 | -46.29097 | 2024-11-26 05:22:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fc42ce3c-bf93-3ef7-8c0f-ae8e6dd4da94 | -3.176 | -48.44289 | 2024-11-26 05:22:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| de9fdcc8-7f85-3c56-9985-3c6c29248837 | -2.70128 | -51.97821 | 2024-11-26 05:22:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 83ab16a4-2b37-3ae3-8c7e-66caf0910214 | -3.97065 | -48.07095 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 589.0 |
| cb37d058-ec50-37e4-82f2-d0ca5fe54f4a | -3.14218 | -45.25328 | 2024-11-26 05:22:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 213f7269-43a9-3cb6-beeb-41fae8085e06 | -8.04723 | -47.0782 | 2024-11-26 05:25:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e6a2b4ca-6ed7-324b-8cd8-3e07ee576451 | -6.08058 | -48.03625 | 2024-11-26 05:25:00 | AQUA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ee84ac18-aeee-30ef-a9dc-16efa09d7416 | -6.0712 | -48.03481 | 2024-11-26 05:25:00 | AQUA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f0291f6f-89f7-36be-acef-999610027b46 | -6.08213 | -48.02619 | 2024-11-26 05:25:00 | AQUA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4d75e0b1-b258-36d9-bd7d-8a0f506d995c | -6.63874 | -47.34419 | 2024-11-26 05:25:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7aaad7b2-e80e-3089-8a83-7d88b2fc9c51 | -6.37042 | -47.35168 | 2024-11-26 05:25:00 | AQUA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 90950177-c6d1-3d73-b813-dda96cc85248 | -6.07275 | -48.02479 | 2024-11-26 05:25:00 | AQUA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d387bb4c-85cf-3573-819c-3fb52ba6802a | -3.1877 | -48.4172 | 2024-11-26 05:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a8048ae0-80f3-3336-8108-9f3a8afd22b7 | -3.1691 | -48.4394 | 2024-11-26 05:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 874b6629-4d77-3cb7-ba5e-5ac1e51b3c41 | -3.1876 | -48.4387 | 2024-11-26 05:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 522df6a1-f4ef-3414-a72f-284b877367ce | -3.1876 | -48.4387 | 2024-11-26 05:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 9706d4a5-a96d-3a3a-97a0-88e583b727dc | -3.1691 | -48.4394 | 2024-11-26 05:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7a026c60-01c2-3ddf-bf0a-5860b12bd370 | -3.1877 | -48.4172 | 2024-11-26 05:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0439ef6e-0774-3370-9d63-d9baf39a61de | -3.1691 | -48.4394 | 2024-11-26 05:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| c32bae5f-1e26-3b64-945d-ab6a12fabab4 | -3.1876 | -48.4387 | 2024-11-26 05:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| aeeaf005-d1bf-3a84-868c-8d82b8d1b439 | -2.8198 | -53.0222 | 2024-11-26 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 73b10022-9f3d-3298-ba0b-282b20fdd619 | -2.8014 | -53.0227 | 2024-11-26 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 87a9f481-2763-3367-8e9d-779dfaf84b73 | 2.68257 | -60.42496 | 2024-11-26 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5973ce64-6fab-3d9a-abfb-08708311c7b9 | -1.63168 | -53.86908 | 2024-11-26 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 400677ef-caf0-3574-8c10-a117c571e570 | 3.82155 | -59.59485 | 2024-11-26 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8adc1ad1-7645-3a16-83ac-1e8b841b574b | 2.68126 | -60.42286 | 2024-11-26 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| be399ec7-6a17-3b29-bfdd-62fe793ca394 | 3.82229 | -59.59946 | 2024-11-26 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 570af219-e6ba-3a72-aeec-dbb04e5e3b45 | -1.63057 | -53.87646 | 2024-11-26 05:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43fb4928-0c65-3935-a2d7-5951d19f7845 | 4.07775 | -60.25156 | 2024-11-26 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ac3a094-e5d0-364c-9562-d4e96bd8dce9 | 2.68188 | -60.42074 | 2024-11-26 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 08f16ef8-95a1-3d73-bfd4-40ed9f955e3c | 1.94649 | -60.85341 | 2024-11-26 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d4988130-955b-341a-9272-0e50ac6af85a | 1.94714 | -60.85749 | 2024-11-26 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91a4c8d0-d4d0-3bf5-8d59-c3dc6d6ef863 | 2.67821 | -60.42567 | 2024-11-26 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ab80cc7-0553-39a9-add5-eb613789ff67 | 4.22895 | -60.07666 | 2024-11-26 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 020de359-a9da-34b8-ae8b-1b09062bbb68 | 4.07402 | -60.25585 | 2024-11-26 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e035c286-3ee0-3379-97ab-527eaae5cdc6 | 4.23252 | -60.07101 | 2024-11-26 05:54:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a919a38-802b-3fe0-b6a8-a50ae02dd2d1 | 2.68629 | -60.42638 | 2024-11-26 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 894fd34e-5be0-3135-8316-c8e81ca8da88 | 2.68326 | -60.42916 | 2024-11-26 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f1a136c-b9e5-3ac8-a674-8077429296ac | 2.68193 | -60.42709 | 2024-11-26 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf3d8902-46ca-30da-8c14-1ddde442ac4b | -9.55754 | -61.94948 | 2024-11-26 05:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3184bc5b-31da-33f0-8b2f-00697fb30dcf | -9.93314 | -59.92939 | 2024-11-26 05:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a154527b-7c39-320a-ae3e-7b7f64ceef60 | -9.36912 | -64.37587 | 2024-11-26 05:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d323fe5d-ac3e-3724-bcb8-b74d1a9c3eda | -9.99237 | -62.30397 | 2024-11-26 05:59:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f33e915-f381-397f-810d-efba1f435300 | -9.92767 | -59.92854 | 2024-11-26 05:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dbc7918-c75c-347b-8bb4-8f6f8489b236 | -10.04262 | -68.15663 | 2024-11-26 05:59:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fab93820-2915-3e3e-b7cd-37e065b1a1c9 | -9.99528 | -62.30537 | 2024-11-26 05:59:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc360149-05cf-37f0-a925-8f45717a8bd6 | -8.58071 | -63.42098 | 2024-11-26 05:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04b7548e-d23f-3e9a-ba8b-23d2d35e2c88 | -3.1876 | -48.4387 | 2024-11-26 06:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b63c0e77-1da4-3c58-ace8-596ca60b6e68 | -3.1877 | -48.4172 | 2024-11-26 06:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c1298577-ac2e-303f-8c36-c852bf0d2ec9 | -3.1691 | -48.4394 | 2024-11-26 06:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5ee6eb69-f875-3d5a-ac5c-a081191111cc | -3.97 | -48.04 | 2024-11-26 06:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 562a3868-0212-3649-90e6-8f6609116bd3 | -4.0 | -48.04 | 2024-11-26 06:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66688d08-48e5-3323-adbc-79e7b9f96e39 | -4.0 | -48.09 | 2024-11-26 06:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aab43cc3-59d7-34be-9ccb-fd59d27a9202 | -3.97 | -48.09 | 2024-11-26 06:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b472ac63-14c0-3b9a-aeb5-d596531312e8 | -17.63569 | -57.58836 | 2024-11-26 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a652f973-b252-3a2a-824e-777fa51327e7 | -17.63542 | -57.58604 | 2024-11-26 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bdd4f2c4-608a-3c7e-829b-6a1be9371d0b | -17.64954 | -57.58984 | 2024-11-26 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a49e8089-d489-3827-b3db-24f9400c524f | -17.63628 | -57.5817 | 2024-11-26 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| dfc5590f-c383-3189-b8ec-8e870c2e5db3 | -17.64261 | -57.58911 | 2024-11-26 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2bb339b4-c66c-39b0-9e4b-36bcebe2d8e8 | -17.64928 | -57.58758 | 2024-11-26 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| b2c86e5c-8e4f-30d5-b541-28f76c903de2 | -17.64235 | -57.58681 | 2024-11-26 06:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fc27b40b-6d1d-3af9-95f2-d791115d06ce | -3.1876 | -48.4387 | 2024-11-26 06:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| e68b5cd8-e785-34b9-971c-0b9addeaf700 | -4.5375 | -43.304 | 2024-11-26 06:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 0bf5d90d-3fa2-3fe3-8ab7-e14503706cec | -3.1877 | -48.4172 | 2024-11-26 06:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 4072c827-46ce-3781-a7f6-5685f99ddfc0 | -4.5376 | -43.2807 | 2024-11-26 06:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| e631d92f-c053-31f7-be58-6d3069541aa4 | 2.68388 | -60.4279 | 2024-11-26 06:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1056a1e1-c30b-3dd1-b862-16b38f6002c4 | 1.95118 | -60.85342 | 2024-11-26 06:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 118a2b5b-0885-39d8-a7b2-d708ce7bd914 | 1.94474 | -60.85442 | 2024-11-26 06:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fc893ff-eb14-39f3-a9ee-85659d1fc041 | 2.68308 | -60.42754 | 2024-11-26 06:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cfb060f-36a2-3187-8ffa-7a5492eb1675 | 3.82683 | -59.59607 | 2024-11-26 06:16:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63c424f1-11ae-3ba5-9d67-549d5f7a178a | 3.82443 | -59.59613 | 2024-11-26 06:16:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 08670802-cccf-30cd-bf4e-7d73c32dd758 | 2.68297 | -60.42239 | 2024-11-26 06:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b82f4763-dfec-3ec8-bf43-c838a54f2e74 | 3.8177 | -59.59734 | 2024-11-26 06:16:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69ef3455-8d1b-3c95-8f2c-1c4de3a0c48f | 3.8201 | -59.59728 | 2024-11-26 06:16:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8dd3fd9-6e09-3b0e-8fd5-fe5420fd128b | 2.68214 | -60.42204 | 2024-11-26 06:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a02650f-af32-318a-8b19-108a020f55b0 | -3.1877 | -48.4172 | 2024-11-26 06:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 228190fc-39c2-3ba3-96e4-2675bce13b3f | -3.1876 | -48.4387 | 2024-11-26 06:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| c45111d6-b851-3467-a64a-8b5269f97373 | -3.1876 | -48.4387 | 2024-11-26 06:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 163923b2-88df-3b6b-893c-9971ec90d332 | -3.1877 | -48.4172 | 2024-11-26 06:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8db80e50-5d12-36ef-b0cf-f38a68299515 | -2.8014 | -53.0227 | 2024-11-26 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b0e02ca4-13e3-3f3f-8769-edf5e1f92b13 | -3.1877 | -48.4172 | 2024-11-26 06:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 427effa6-2881-36dd-b412-9333f1254aa5 | -3.9674 | -48.0851 | 2024-11-26 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 261.4 |
| 35c1c2e0-2738-30b2-b80d-07f624eb3bb4 | -3.986 | -48.0626 | 2024-11-26 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 312.9 |
| 782f83c6-6832-3d79-9999-78bbbef1c715 | -3.9675 | -48.0634 | 2024-11-26 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 537.1 |
| f6514f56-fc93-39d1-90da-f6b7420099f9 | -3.9859 | -48.0843 | 2024-11-26 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 227.8 |
| cc852a97-12a6-3779-85c5-ad3392520b15 | -3.9676 | -48.0418 | 2024-11-26 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| e0a37ee6-527e-3c95-ab3e-b655391541b4 | -3.9861 | -48.041 | 2024-11-26 06:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ee15d51f-425e-39ea-8593-53f05546bd4f | -3.1876 | -48.4387 | 2024-11-26 06:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |


[Clique aqui para ver as próximas entradas](README45.md)
