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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b4ea672-a145-3c6e-8200-59ac19faaa28 | -6.124 | -45.8466 | 2025-07-16 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 9d6b7fc2-f569-302b-ae8c-656c8692d3dc | -12.0825 | -43.4753 | 2025-07-16 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 46400974-7b76-3929-8cea-7f4ff264cc2d | -10.5824 | -46.2338 | 2025-07-16 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 30bc6cff-df3d-3239-8585-89d42d32ddc0 | -10.6015 | -46.2314 | 2025-07-16 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 51a17927-dd92-3a7e-8169-86f3357e6507 | -12.4801 | -46.9017 | 2025-07-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ce751b2a-c33d-3992-b6b1-65e48c8c8dba | -12.4989 | -46.9215 | 2025-07-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| bed5e191-97b9-3ab6-9be6-e3a93bdc4c50 | -6.7194 | -44.3231 | 2025-07-16 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| a1ed3bb2-574f-34fb-9395-802d1289c08e | -4.4626 | -49.009 | 2025-07-16 14:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cd967f39-f93a-3d13-ac77-d11751ef0c0f | -12.4121 | -45.3628 | 2025-07-16 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 21591794-9b65-35ab-b88e-8f91f76d9c17 | -8.7611 | -46.5985 | 2025-07-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 4428d494-c4f8-396b-acdc-081dbb637f80 | -12.0825 | -43.4753 | 2025-07-16 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 4e5d6d88-811b-3cad-90c7-eb4b9423e222 | -12.4797 | -46.9243 | 2025-07-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| f808b5c1-29d9-35f2-a118-cec2cba100b7 | -6.668 | -45.6922 | 2025-07-16 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| e6592c42-2320-3192-9000-094dbc744974 | -12.4121 | -45.3628 | 2025-07-16 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 9d79763a-a1fb-3abc-8439-07e752d5196b | -6.6678 | -45.7147 | 2025-07-16 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6dd2601a-1241-3bec-b4c0-fcfe394cb3a0 | -12.0632 | -43.4784 | 2025-07-16 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 1c4a704b-7299-30c9-a812-e748d43fe95e | -10.6015 | -46.2314 | 2025-07-16 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 582ab7dc-545b-32ee-9014-77c86a185af6 | -6.7194 | -44.3231 | 2025-07-16 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 149.2 |
| bdd87596-d87e-301b-a488-8afa01c280ab | -8.7608 | -46.6208 | 2025-07-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 2381d27b-ce2b-3b51-836b-bcc844455e43 | -12.4989 | -46.9215 | 2025-07-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| ce909080-2c29-346c-8832-8e24ec62bbbf | -10.5824 | -46.2338 | 2025-07-16 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 4014b004-8439-3942-a3e4-aafdb363b7bf | -12.4989 | -46.9215 | 2025-07-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 81455dba-09ff-327d-9014-687aeeb0c796 | -10.6015 | -46.2314 | 2025-07-16 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 76813c99-3db8-3f0f-a2e5-494346686033 | -12.4797 | -46.9243 | 2025-07-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| e595ddab-ab97-3233-8611-8db9fb40cca4 | -6.7194 | -44.3231 | 2025-07-16 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| f25819ee-0dc9-3528-9c60-9cbbb80229de | -8.7611 | -46.5985 | 2025-07-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| dcc505f9-61b7-3327-86f8-7146ed331433 | -12.4121 | -45.3628 | 2025-07-16 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 6100e4a0-19e1-3cbf-875d-f32606171adb | -10.5824 | -46.2338 | 2025-07-16 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4128c73a-0289-3930-bcb4-78da8289ac34 | -4.444 | -49.0099 | 2025-07-16 14:30:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ba973fa0-a65a-34dc-955e-a9a4536290fd | -4.4626 | -49.009 | 2025-07-16 14:30:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b8232e63-4bab-3100-8aed-c0b8a56bb86e | -8.7608 | -46.6208 | 2025-07-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 9a479417-ec68-31c0-ae6a-985be21428b5 | -6.6488 | -45.7388 | 2025-07-16 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| e4091e08-3924-365e-8b67-33c6d92d39e7 | -12.427 | -50.0387 | 2025-07-16 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 517.4 |
| 4f4354b3-57c1-3fc1-9617-0d24222bc50a | -10.6015 | -46.2314 | 2025-07-16 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2dc06410-3a68-319b-8bd0-51ae70a7eaa9 | -12.4079 | -50.0411 | 2025-07-16 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 460.8 |
| 0dbcf4dd-64b3-3fd1-a176-0890e268ac0f | -12.4121 | -45.3628 | 2025-07-16 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 08e0797a-7e13-3a1a-8d03-c3cec9a68416 | -12.4989 | -46.9215 | 2025-07-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 174ad6a8-0c66-31bb-8a6e-e93b7a3b365a | -12.4797 | -46.9243 | 2025-07-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| c80cbb1d-9126-372a-b05f-5576181a0135 | -6.5807 | -41.4634 | 2025-07-16 14:40:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 146.3 |
| 3935e138-2e30-3241-844c-6d06a8910790 | -12.4274 | -50.0171 | 2025-07-16 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 9c10fcc7-99cc-396e-af7b-b666edbd445f | -4.4626 | -49.009 | 2025-07-16 14:40:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| b42f85aa-4a6e-34d2-8209-bed9c6406720 | -12.4267 | -50.0603 | 2025-07-16 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a8b21218-a2de-31c8-b8aa-7c77cbb1e8c7 | -8.7611 | -46.5985 | 2025-07-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| df4ac48f-f824-3d41-abe0-8e43310394d1 | -6.5996 | -41.4616 | 2025-07-16 14:40:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 852af96e-3eaa-3002-85e0-ac72fcb6dc52 | -10.5824 | -46.2338 | 2025-07-16 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8c658186-b763-39a4-88ca-30837c7262ab | -7.0478 | -43.4829 | 2025-07-16 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 40c1e622-204f-35d1-a460-ade6256e42b5 | -4.444 | -49.0099 | 2025-07-16 14:40:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |


