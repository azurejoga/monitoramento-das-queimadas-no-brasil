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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2db434f-f4ba-310a-ad08-8cc7e2106ec3 | -16.7532 | -55.7797 | 2024-10-01 04:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| d31b5709-ba34-3d07-891d-900d5d44c7d6 | -16.7724 | -55.798 | 2024-10-01 04:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| c4cafff1-8570-388f-bdf9-acf2eeeac236 | -16.7728 | -55.7773 | 2024-10-01 04:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 940b67e8-803f-3ba9-809e-840ee319b14e | -16.8787 | -57.6971 | 2024-10-01 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| a9e32fd1-cc0b-337f-9530-7b678d64b817 | -16.8983 | -57.6949 | 2024-10-01 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 3d8178a5-e883-3ae0-9a59-6cf7a1bf2b62 | -17.705 | -53.2046 | 2024-10-01 04:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 1a6ba08f-b8e8-3303-880d-e284aeb56737 | -18.6973 | -57.333 | 2024-10-01 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| cf8fe89f-2702-3d07-ac74-7c9ceb2ecfe8 | -18.6977 | -57.3123 | 2024-10-01 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 03c95911-6af6-33ab-a0ea-411b805e70cd | -18.7176 | -57.3097 | 2024-10-01 04:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 7cf31282-c0d7-3195-b70a-598c76d8f84a | -19.1129 | -57.4655 | 2024-10-01 04:26:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 648aadea-bfa7-3271-9410-5cf402398718 | -22.3498 | -49.3293 | 2024-10-01 04:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.7 |
| 1f0c9a3c-99f3-35e4-804a-0054b01ab509 | -22.37 | -49.3477 | 2024-10-01 04:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.8 |
| ba5213c6-5a75-3fe8-857c-394faa86ddfc | -22.3707 | -49.3244 | 2024-10-01 04:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 279.0 |
| 033ecfdd-8f2e-3a47-8a63-0ef4f91f3857 | -22.3713 | -49.3011 | 2024-10-01 04:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 150.1 |
| 832a9b99-f1c6-300d-bcf9-ef82b0b5de45 | -11.5695 | -63.8084 | 2024-10-01 04:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 48c86b2a-92d8-3af7-973a-c9c347ac4dde | -12.7826 | -62.9025 | 2024-10-01 04:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| cf27a052-f53b-3c9d-aeee-d24c545f5122 | -16.4536 | -57.4188 | 2024-10-01 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 119304fa-84ac-3fad-aa12-082d0c9aee64 | -16.474 | -57.3553 | 2024-10-01 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.8 |
| b7386c24-9317-33bf-89e3-c6f1c858e785 | -16.4743 | -57.3349 | 2024-10-01 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 52377e0c-91b5-300a-a588-004dcb2c5530 | -16.4935 | -57.3531 | 2024-10-01 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 41839b6f-5ff2-3d3c-a64f-79454811f71d | -16.4939 | -57.3327 | 2024-10-01 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| bb041c22-31dd-3853-9912-b316cbe4473b | -16.5131 | -57.3509 | 2024-10-01 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 38f9ad92-9012-3b96-8e90-3f08044d8fa6 | -16.5134 | -57.3305 | 2024-10-01 04:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| b4251512-6c31-3c7b-93e4-44d3ba3fa0f1 | -16.6316 | -57.2557 | 2024-10-01 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 40cd123d-9d57-392a-83e5-a6264ffa1cee | -16.6508 | -57.2739 | 2024-10-01 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| 52284a11-5ea5-3ef4-b800-d951b5f16457 | -16.6512 | -57.2535 | 2024-10-01 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 285b47f7-b902-36c8-a0cb-e50a4e834364 | -16.6515 | -57.233 | 2024-10-01 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| fd03dbf0-61a7-3579-af9a-8371448c9513 | -16.7079 | -57.3696 | 2024-10-01 04:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 0bcc360c-6145-3f8f-b2ff-9f0733cec8c9 | -16.7724 | -55.798 | 2024-10-01 04:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| 937d545a-4ebe-38df-afb8-d66b49b36ff4 | -16.7728 | -55.7773 | 2024-10-01 04:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.2 |
| 6b0370ee-ee7e-33e1-9a32-df19b95d69ed | -16.8784 | -57.7175 | 2024-10-01 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| f7e4d4e0-276e-328a-929e-0556ba431ec9 | -16.8787 | -57.6971 | 2024-10-01 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| c88e26bc-756a-3ea4-8e5e-3081954d073e | -16.8983 | -57.6949 | 2024-10-01 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 65b4bb22-bc61-3177-896a-921ce209dd13 | -18.6973 | -57.333 | 2024-10-01 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 0a32d340-bf34-3970-af38-95c504dac97c | -18.6977 | -57.3123 | 2024-10-01 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 896055b0-e682-3181-b4a7-3f6f5c38ee16 | -18.7176 | -57.3097 | 2024-10-01 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.0 |
| 508821dd-cf55-3043-b253-b1c57602c49b | -19.1129 | -57.4655 | 2024-10-01 04:36:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| ccb016cb-bc72-360c-80c4-606a134f2078 | -19.1329 | -57.4628 | 2024-10-01 04:36:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 58e7f04d-ea8b-38ab-b745-5f2e50a903a2 | -11.6555 | -64.9991 | 2024-10-01 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| bdb4e6b9-cceb-3abe-9d96-b2d9649f3562 | -1.16911 | -47.73412 | 2024-10-01 05:01:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4c111002-0306-3752-8bfe-2d39d901bc2b | 2.18006 | -50.79069 | 2024-10-01 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a85d97d-67a1-360a-8d21-e1953ccac1b1 | 2.11884 | -50.90781 | 2024-10-01 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15ab2ddb-e1e7-38e2-84ee-d1b892e1193b | 2.11872 | -50.68248 | 2024-10-01 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62134e7b-1dba-3990-9d35-6089b53ab747 | 2.11806 | -50.67835 | 2024-10-01 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f8520a3-61b4-3961-9b8b-2874da5f8246 | 2.11512 | -50.68305 | 2024-10-01 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a6ac027-95b3-39f1-8212-2b2c6addbb8d | 2.11446 | -50.67892 | 2024-10-01 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cdffae1-4dac-3002-9ca9-2bac7670c20f | -0.16631 | -51.55482 | 2024-10-01 05:01:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 926c719c-32cd-39fc-9d47-1213a162399a | -22.34 | -49.32 | 2024-10-01 05:03:18 | MSG-03 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c5fe6b5-7b55-3e1b-8cb9-d14d57e7adcf | -21.56 | -47.83 | 2024-10-01 05:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fd227831-55a7-3979-a863-7d0f4747e2dd | -2.14549 | -53.64443 | 2024-10-01 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6a9f472-7cda-3cf3-b06c-8bae0f431d9b | -1.43279 | -54.47901 | 2024-10-01 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a2b7996-531e-34c8-aceb-b542662582a5 | -1.34832 | -54.65163 | 2024-10-01 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f406e51b-3577-3355-836a-22008d402800 | -1.31898 | -53.49088 | 2024-10-01 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a29d2fe2-bac8-3525-8929-5699c711fea3 | -2.79886 | -54.58132 | 2024-10-01 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02f88651-7ae4-3666-92a0-dcc630a2b3d1 | -3.46891 | -53.79845 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e3232d1-331a-3b7e-9d03-61e30614532e | -3.46611 | -53.7944 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 052e5b1f-4354-339b-91be-de2b9ca39c26 | -3.46556 | -53.79793 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d87490f-3641-37ff-9127-00b48aab7f37 | -3.46501 | -53.80146 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee7a3b10-8b65-3070-b7e5-8e8bf29a4907 | -3.46166 | -53.80094 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45ed31b2-25f2-3d4c-bf66-b3478bbe34f2 | -3.12939 | -53.7279 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d0d5065-775b-351e-a85a-74f6379fd393 | -3.12884 | -53.73145 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b40e9f3-b5e4-36d0-b17d-0a1d375aa2b1 | -3.12719 | -53.74208 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bff7692d-3a1b-3a77-9c90-4ce38481a4fe | -3.12664 | -53.74561 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 213cb093-9336-3ab8-b7ad-c8ea618e3450 | -3.12604 | -53.72738 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 140541c5-1ea1-3a82-afb8-214d3aebb1d3 | -3.12549 | -53.73093 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 801cfbb3-a881-373f-9c93-91b000197b10 | -3.12329 | -53.7451 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2912cb56-3b16-38c6-9a35-5e8b2a17e095 | -3.12324 | -53.72332 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6978d33e-647b-3c1f-897e-0e87754d7cf1 | -3.12269 | -53.72686 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad23f1e1-a832-3bf5-812e-006570a0ec76 | -3.12214 | -53.73041 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f5ab9dd-0e2a-34e6-9121-06bd7d6cc9ba | -3.11934 | -53.72635 | 2024-10-01 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6e4c06d-9191-315c-ab3e-b788576cd0fa | -3.07141 | -54.7756 | 2024-10-01 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e763d5a9-3104-3c28-853f-fe2badb7f86d | -3.06811 | -54.77509 | 2024-10-01 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04230f7e-916c-39f4-b291-a3221f6a7849 | -2.98284 | -54.62461 | 2024-10-01 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c0c0c08-86c0-3f5f-adea-5310d25c3027 | -2.94025 | -53.69847 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3b90faa-bb1d-3a04-9523-b21a8732e0b9 | -2.9369 | -53.69795 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64df5f6b-a438-35ba-8200-f2a9e03e1d94 | -2.93635 | -53.7015 | 2024-10-01 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89ba3292-1fe8-3519-862c-38e4c0153c9a | -6.22332 | -55.63977 | 2024-10-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 403808d1-2be1-3cc3-b929-e230cd9feaec | -2.33538 | -60.06905 | 2024-10-01 05:04:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99077184-ad58-3cf5-a1db-8d79970d7263 | -3.95341 | -41.52048 | 2024-10-01 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 971f037b-5498-3a3c-b4de-8454033b8fb2 | -3.95104 | -41.51493 | 2024-10-01 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8626568c-2615-3d8a-9af1-79189cd8c554 | -3.95009 | -41.52172 | 2024-10-01 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bec119de-1e58-3ba8-9047-c3e493694dc3 | -3.94634 | -41.51929 | 2024-10-01 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b9b4b666-a25f-36a8-b238-9c265f7f0a68 | -4.8423 | -42.76889 | 2024-10-01 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 517d11be-0770-3159-9587-20bb95cf05a4 | -4.83849 | -42.76898 | 2024-10-01 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 29385ea3-34dc-398b-bdd7-72775eed3c81 | -4.83763 | -42.77499 | 2024-10-01 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8634fb7a-d9f9-3c96-aedb-e82efbfe2bff | -4.83479 | -42.77404 | 2024-10-01 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 563a54fc-156c-30dc-9e12-de31d4ed19f0 | -4.83094 | -42.7742 | 2024-10-01 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f652e54-b4d6-3af0-a5b0-78ef2056566b | -7.85433 | -43.08627 | 2024-10-01 05:04:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 368c9169-039c-3916-afe9-e2d0ca948f93 | -7.85288 | -43.08206 | 2024-10-01 05:04:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ffaaab7b-92b3-38f1-b9f9-8487b23252a5 | -7.8521 | -43.088 | 2024-10-01 05:04:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 52ee30c2-919e-3309-892b-0233722de08e | -7.84751 | -43.0855 | 2024-10-01 05:04:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| de974552-89ff-35ef-809a-0cb4e755c11e | -7.28426 | -43.38157 | 2024-10-01 05:04:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 484b0d8c-fba7-3b63-a6f1-de21f1441d99 | -7.2817 | -43.38358 | 2024-10-01 05:04:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ac6f076-27ec-325b-990f-5b59c3d5aa59 | -7.27682 | -43.38669 | 2024-10-01 05:04:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30627849-8ba6-313b-b557-3d01989f139e | -7.27433 | -43.38852 | 2024-10-01 05:04:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a814d0e2-3de0-39aa-b49e-e1a61974cddd | -6.70096 | -43.04562 | 2024-10-01 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f3d0cb73-fdcf-3f5b-b65c-bd5574f6d372 | -6.70016 | -43.05151 | 2024-10-01 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0d96b2e6-7c57-381e-b134-559977e8aab3 | -6.69692 | -43.04749 | 2024-10-01 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ccc2e31d-da9c-3995-8c4e-d2dcb64256d0 | -6.69344 | -43.0506 | 2024-10-01 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94f7c414-1a7e-38f2-ae9f-c7453bd3a016 | -6.68564 | -43.54466 | 2024-10-01 05:04:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README99.md)
