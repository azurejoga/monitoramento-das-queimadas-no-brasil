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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b4a93f0-e274-365f-a3cf-813492daf146 | -14.50338 | -45.96314 | 2025-08-20 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e0507d4-6472-37d9-83d8-f0c40718e06f | -15.05935 | -54.83356 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb186cd2-90ae-324c-83fa-292b98243429 | -13.33493 | -54.42926 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3f0d0fc-7052-37a0-a667-d8a4a4f174b5 | -14.5379 | -53.16929 | 2025-08-20 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b540001c-6aca-372e-82be-89cc71ed2ba3 | -14.89276 | -48.08379 | 2025-08-20 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9595f2a0-9665-37a9-830e-8ea07007e261 | -15.54071 | -48.56433 | 2025-08-20 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b7cf09b-4440-3c3e-a414-03dcd0100c54 | -15.06443 | -54.84575 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 314044e0-2d58-31d2-9dba-ac45533d4331 | -14.74328 | -46.30068 | 2025-08-20 04:59:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ce4a916-a766-3ba1-88ca-484a9433bb1f | -15.00116 | -54.82014 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 80c4bcf5-7974-3f2f-b35f-cef007f5e15c | -15.54006 | -48.56962 | 2025-08-20 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37d10295-721f-3ac8-becb-3334cb80c364 | -13.14949 | -54.93201 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e32f3295-328c-31c0-9a02-eee85d57c771 | -13.15228 | -54.93612 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1353dffd-93de-33b5-8a86-2e087e151e08 | -15.01801 | -54.82291 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f1fc788-73ac-3ac2-a28d-91cf2cc92261 | -12.97941 | -56.87054 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70e7690c-98b6-3139-91b4-e80415734607 | -13.1506 | -54.92485 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ec4b3480-5432-35c1-94e8-969706260859 | -14.62396 | -54.8897 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb713760-03b6-38a3-a22b-780bf93d2dc9 | -14.50383 | -45.95933 | 2025-08-20 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cba9c31-0c15-3c11-a22f-e6130b3fea6d | -15.42859 | -46.71491 | 2025-08-20 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c0f6ccb-6177-373b-a87a-e6bb1737065b | -13.16117 | -54.94489 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87bfa828-7eee-3297-8978-609b1c657b81 | -19.85609 | -49.83809 | 2025-08-20 04:59:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 120a367a-9a02-3e5c-9c68-3d41cdef1a67 | -15.35065 | -49.61264 | 2025-08-20 04:59:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4e4f862-0c07-315a-8c46-398c662119fe | -16.75109 | -49.04767 | 2025-08-20 04:59:00 | NOAA-20 | CALDAZINHA | GOIÁS | Brasil | 5204557 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dc0a8ca-75af-3e38-a549-27c3dc7564f7 | -19.87548 | -49.83505 | 2025-08-20 04:59:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d40809fe-d5df-35c4-bf0d-87cf95dccdeb | -13.34221 | -54.4041 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 522f60a1-c13d-3bc5-a7ef-b458002712ab | -15.74715 | -46.6204 | 2025-08-20 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e918c8f-7177-3fb5-93b9-96da2d00f6d7 | -14.55037 | -53.94985 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1977e91b-0f29-34e8-a246-51441325993c | -17.66226 | -54.06002 | 2025-08-20 04:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75ca72b8-6179-3eff-8cc7-a9b0a82d83ba | -14.54579 | -53.18109 | 2025-08-20 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed9d4c58-356c-3797-a978-987ebb7b48b6 | -12.97708 | -56.88499 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c542ec50-5daf-3626-99fe-169b039a4f02 | -13.32648 | -54.41666 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75e7ab6c-92da-3554-bbd3-ede2fc111b60 | -13.33211 | -54.42507 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5fb57ae-ea45-3b95-9839-c7b036438ef9 | -12.97824 | -56.87777 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c5ec257-f9e0-384c-b2ca-5da6b0d68a48 | -12.96996 | -56.86523 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae37dac0-4083-3d24-8da4-3049b53281d2 | -16.18049 | -48.8616 | 2025-08-20 04:59:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5748ee33-85dc-3e90-a843-d0ff9789c926 | -14.89415 | -48.07195 | 2025-08-20 04:59:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12f309f2-5b8a-34de-bf5f-0a502ff8d7ff | -19.45492 | -47.1923 | 2025-08-20 04:59:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89e0eb60-0216-3642-9116-f0aa4cd9099b | -12.97606 | -56.86997 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b41344ab-1838-3893-b92d-aa8f6cc2eb6e | -14.64188 | -54.88499 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f08d98c8-bc4d-32d1-94f6-34eedd3f1005 | -13.18618 | -54.95993 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3aa16501-e976-3ba4-8a2c-4e567318464e | -16.34362 | -50.1786 | 2025-08-20 04:59:00 | NOAA-20 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee8bce7f-0d94-3207-9990-6712de925432 | -15.00172 | -54.81645 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68f055c0-573c-30e7-931d-e6bd0994dbf0 | -13.15393 | -54.92538 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cf2e2eff-4dad-3bd3-b0de-2d989a7089f7 | -12.97781 | -56.85914 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 657f7a96-eb3e-38f5-9069-dcab7e844cdd | -14.98685 | -49.56372 | 2025-08-20 04:59:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56de4a2c-89f6-3ddb-ad53-8c59ce7fc15b | -13.0265 | -56.84897 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aeb442fb-b78d-3023-8b50-5a2b0422ab4b | -14.62732 | -54.89022 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a15aa4b7-0aeb-36a8-a16f-d1c2b059781b | -15.05391 | -54.8366 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c1b0d67-8e6f-32cb-bee9-dfa080c0f25c | -17.66247 | -54.06219 | 2025-08-20 04:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9aa0e60-12ca-3467-bc41-7eb2a860bf63 | -14.49775 | -45.96227 | 2025-08-20 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ab9b53b-ffa9-34d0-81f0-3ac67abefe93 | -12.98667 | -56.86808 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd4461c1-26e9-3e6e-86d4-a46c88d84033 | -14.65532 | -54.88711 | 2025-08-20 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10c5e7c2-8283-3f38-b092-b1d1fc5beaec | -12.98057 | -56.86332 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b19a00bd-3242-382d-b77f-9a1491bd08ca | -12.98275 | -56.87112 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 126a5ee1-20d8-33a9-abb3-476762da4cbc | -12.98042 | -56.88556 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f445aa79-fb7c-35f2-a8b6-2c5b279ec5c6 | -15.02361 | -54.8315 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb752e2b-a208-3999-9f7b-dd0cdb37405b | -13.03043 | -56.84594 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b34d1a4c-bb86-31e4-a1ac-428095e80e9b | -15.64801 | -52.68834 | 2025-08-20 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d24387e-1bfa-32bb-b695-133ecce5473c | -13.14671 | -54.92789 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 08ba8644-ada2-361b-8477-1a4d6504fbc6 | -12.9733 | -56.8658 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3809cb1a-f960-3fac-bdc2-b7fbe2a31b39 | -16.32935 | -50.18579 | 2025-08-20 04:59:00 | NOAA-20 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78baf949-658d-3824-91b4-bcc8b9fc85df | -18.17845 | -47.90068 | 2025-08-20 04:59:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caa99ca5-a098-3e65-b167-2fa0a12d5597 | -12.96501 | -56.85331 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6269cf3e-47e2-3bd4-86ce-8e4887561875 | -18.67965 | -46.97704 | 2025-08-20 04:59:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b76312a3-f40f-3df5-b2d4-cf881b0f8a4d | -15.42818 | -46.71849 | 2025-08-20 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe1370f4-960e-33f7-8015-e44cb5ed2a4e | -13.02984 | -56.84954 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee4f74dd-e0be-38cc-a3e2-cf835dd72146 | -13.33434 | -54.41039 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 51a6aca5-ec36-3caf-9f6e-2ebe04384627 | -13.15338 | -54.92897 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cfb69ffc-6ae5-3934-91f1-a1d4e12988b1 | -15.02138 | -54.82347 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b39e4dc5-f37c-3f51-b901-30f98b68eec9 | -12.97664 | -56.86637 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5240ffdb-6470-3bfa-a2e0-2a7f45615312 | -17.66581 | -54.06051 | 2025-08-20 04:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54bdcf5f-5dab-36fb-8b21-aeb629a5685e | -12.98725 | -56.86446 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 695f74d6-552c-3b41-b957-3e8855a1400d | -14.74996 | -48.3858 | 2025-08-20 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38ad67b1-0788-3630-879f-61d59753d05f | -15.00453 | -54.82068 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 565f7621-d048-3c0a-befb-e285cd98558e | -13.34671 | -54.39725 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf41cb27-06ed-387f-8f8a-2a3c928c2145 | -13.15671 | -54.9295 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3fba5f1-581e-3293-83a0-12041afda065 | -15.00004 | -54.82752 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a33b167-5bb9-35a2-96fb-6cb465076db9 | -12.97054 | -56.86163 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c96947fd-3518-36e0-930d-126f6987999d | -12.96894 | -56.85026 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be9aa821-419e-345a-9beb-699413117622 | -13.15448 | -54.9218 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c1321c6a-293b-31cf-bc18-f42c4998bb98 | -14.8828 | -48.06868 | 2025-08-20 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b8bae86-f336-313b-a03b-21b30056f5ff | -13.34449 | -54.43454 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 207bf41d-6d5f-3305-bf21-f4d68bc15dcd | -19.88428 | -49.84138 | 2025-08-20 04:59:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bd6b8f33-5ff5-3b98-9d4f-609237342479 | -15.05167 | -54.82867 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca031a49-1e76-30a0-a1ef-03a8da67d5cc | -14.89053 | -48.0871 | 2025-08-20 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fe5825e-851e-3996-a5a9-cb0f24576dfb | -16.18012 | -48.86146 | 2025-08-20 04:59:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a17a4792-3c25-384a-941c-0145e70198fa | -15.01745 | -54.82663 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32b53887-84eb-39de-864a-aab0c9b8dc99 | -15.05542 | -54.83671 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9dab5801-7202-3bd8-bc78-1ee0c3d95568 | -13.14726 | -54.92431 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b5756e72-73b5-3303-9050-c492a1b93338 | -15.06161 | -54.8415 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba0b9678-232a-36dc-a764-2fa3ffa9aff2 | -13.16451 | -54.94543 | 2025-08-20 04:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49ba5ebe-218d-31c3-b946-27a2fd6e3879 | -13.0326 | -56.85371 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 187df9d1-c50e-3bc9-89f5-92d01fe668a8 | -13.34615 | -54.40095 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdd59cec-e8ba-3287-b646-d66887f4adb3 | -14.35125 | -51.97694 | 2025-08-20 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eddee16a-340c-3674-aae2-617dc42f79d3 | -18.67928 | -46.98061 | 2025-08-20 04:59:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50f8e604-b8c4-3d99-b566-44bde28d322c | -13.32929 | -54.42087 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 243c0ad3-accd-3486-80ec-76e25b535de1 | -13.13392 | -57.15369 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56668651-b396-36e1-bb35-b589c86d00c0 | -14.99612 | -54.83066 | 2025-08-20 04:59:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9081d38b-e341-3186-a85b-3451c9bb7484 | -12.97214 | -56.87302 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed0dd0d1-32b2-379b-97cb-6a42f47dbc80 | -13.33549 | -54.4256 | 2025-08-20 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f9a255f-8372-328c-91e7-401ec1854355 | -12.9672 | -56.86107 | 2025-08-20 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README51.md)
