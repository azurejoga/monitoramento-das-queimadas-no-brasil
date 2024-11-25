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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2850a003-5bc1-322a-9d01-bb185af64272 | -0.57294 | -51.73852 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17b2a520-0f1d-313d-a3c7-ead0f7fd4e39 | -1.38178 | -52.32187 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6fe04d2f-739e-317d-a613-f95cb3705e59 | -2.85435 | -53.96281 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01e3df08-fd5f-35a5-a3d0-6551d321851f | -1.22957 | -51.7397 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7ff9b16-5715-30ab-8cc9-673829abaf38 | -3.25399 | -54.21194 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d4401e2-1c3e-3a9c-afe6-fcf4c8d1e9b2 | -2.62527 | -51.77187 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d912b79-bb4f-323a-afab-4d3cfba58f2c | -3.25288 | -54.21949 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1f22a0f-0845-3e2d-b3d1-c7e42a7964b7 | -0.62624 | -51.71003 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d3b8cd6-4ede-346a-a174-9cd39f671296 | -1.74006 | -52.73547 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87bfbacf-a5f7-337e-8aa8-6bf83300e605 | -3.32803 | -53.19193 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1f8529e-4c11-3840-a930-6a33d3d12aed | -2.90184 | -51.57261 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fad9cb0-0465-30b9-8d7c-74248605ae77 | -0.68916 | -51.8798 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 807c182e-4566-3fdf-a44f-e7ebf264ac6f | -3.61178 | -54.74354 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb105e55-342f-3114-a4e5-2740c8f3fcc7 | -3.24414 | -53.27662 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c39d17ed-9481-3c10-b229-28319c4d9024 | -2.64486 | -51.77481 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c566a433-c530-394a-87a9-1f5746df1c43 | -1.36449 | -53.84007 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d80bd82f-a246-372f-968e-29d03356613b | -2.89635 | -51.5735 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df19146d-fbd4-3afa-a6ef-c795f46b20dd | -4.23123 | -53.49354 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ea1e8a7-f2dd-3d7c-8727-9abbdc91abbb | -3.32283 | -54.09604 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe0489ac-20e0-3016-945d-c482cd52eadc | -1.76484 | -52.70485 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb9301b5-0129-356a-b7dd-59cbf129ef10 | -4.54068 | -47.6628 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30e60a53-c4f6-3400-9caa-e91e745f0541 | -3.61572 | -54.21727 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a86958e-912e-3173-9b37-e87ffbef6b34 | -1.34965 | -54.63174 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c569716e-da70-3b49-bf0f-7723adbbc6cb | -2.90276 | -51.7719 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02732d21-5092-3722-ae00-4af05229cbd2 | -1.57028 | -52.00901 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08aa9cb6-d318-3847-b052-96340fcbc954 | -3.63344 | -52.2546 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02ffee7e-be83-3d24-b5fd-29b37f1ba3cb | -2.32844 | -53.86728 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e06a9077-3550-320e-a9f7-d125093fb17f | -4.25458 | -48.675 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d43d6f65-9b95-3f4f-8b7c-a6ea4baf4dea | -2.90177 | -51.57146 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| babfcdc9-44fe-32b1-88d0-110dc011cfeb | -2.74987 | -60.23536 | 2024-11-25 05:20:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1fc3631-15d2-36c2-8fab-901581671556 | -0.68805 | -51.87769 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0090c078-d58a-3de8-9a20-104ef6350eef | -2.3124 | -53.6048 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ebcd309-3c05-37d0-b176-9011407044a6 | -3.63905 | -52.25007 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0302c210-8098-3dab-b1dd-8ba852124d75 | -1.99044 | -53.2972 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc5288bd-501b-3322-880b-7c4fdf3c1a00 | -2.9233 | -51.7692 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f339b3c9-5524-341d-aad1-4fc3d8dafc88 | -3.05965 | -53.22024 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61b85256-32e1-3214-8d76-007ede0a7ea0 | -0.27679 | -51.50289 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07be9e87-4dc1-3cb5-9968-ccae1e68145a | -1.60506 | -52.58126 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b3ff43ae-7efe-3dd5-9f55-2d23d7ca9b7d | -2.85472 | -53.96151 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d4d20a7-0536-30d7-b49a-50c5d7bbb19e | -2.61628 | -54.25448 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87663b08-bcea-3a91-8198-33b9229015eb | -4.55216 | -48.95541 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e7ef72e-453b-3c70-a7c1-037029ea5586 | -3.94196 | -47.99061 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7481b1d1-e7c5-30b3-963a-00e6b9239144 | -9.69092 | -64.7187 | 2024-11-25 05:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40ed1830-4a3f-3276-ad0b-119d56ddb625 | -9.61008 | -63.49499 | 2024-11-25 05:22:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 026e34ec-d8c9-3543-a87a-2ee617616f9b | -17.75502 | -52.43933 | 2024-11-25 05:22:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 032fa72c-026c-364a-86e5-0dcd4fa8b2e5 | -11.55469 | -61.92001 | 2024-11-25 05:22:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d6a47ed-4fbc-3fbe-872d-8c59b94277d0 | -11.86905 | -63.83778 | 2024-11-25 05:22:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e73f6a2-da74-371d-a984-836f28a15302 | -9.77492 | -64.68681 | 2024-11-25 05:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1429c93-accb-3ffd-b1e9-5149e1a37d4d | -14.2956 | -57.63145 | 2024-11-25 05:25:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d2a8f84-6e80-3762-9ed9-b8a6b1430365 | -21.31992 | -55.95119 | 2024-11-25 05:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ad79340-b855-3ef4-b92b-e7f5b2fa9a68 | -23.11705 | -55.06859 | 2024-11-25 05:25:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2609722c-977a-3c9a-bfec-e90a139748cf | -20.56073 | -54.65929 | 2024-11-25 05:25:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20ce6bf2-9743-3fd4-b89d-a1b673884475 | -23.11185 | -55.06788 | 2024-11-25 05:25:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0267bac5-7599-35d6-a267-b9e999e92829 | -14.29879 | -57.63722 | 2024-11-25 05:25:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fc1e5c7-5762-354d-843c-950ed62ac656 | -14.29951 | -57.63205 | 2024-11-25 05:25:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec4c3599-0534-355a-877f-175b6531942c | -20.22063 | -55.97169 | 2024-11-25 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7947f69b-3788-3b12-8bcb-15cb3beb913e | -3.1653 | -45.2046 | 2024-11-25 06:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 5babd9e1-4449-323b-814d-6b135fe2679b | -3.1839 | -45.2038 | 2024-11-25 06:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 1a8b6670-5fd0-361d-88a4-1a181234b91a | -3.1838 | -45.2264 | 2024-11-25 06:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 634a1507-b7b2-3af7-99b8-a1315e030a44 | -1.77562 | -52.71383 | 2024-11-25 06:20:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c44d28bc-f3d5-3e52-a65f-06c42f1fd0d6 | -0.5706 | -51.70851 | 2024-11-25 06:20:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c9f92de2-4479-3b3d-8a9a-8f678f90fd36 | -1.77256 | -52.73552 | 2024-11-25 06:20:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 216db472-7d53-31d7-873c-6a3be2fc8f92 | -2.33355 | -53.86818 | 2024-11-25 06:20:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 8e6e4468-0d51-3d1b-a4ba-6109ccff0cff | -2.33124 | -53.86065 | 2024-11-25 06:20:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 7053f15e-6480-3142-94c4-e74ed771917e | -1.73775 | -52.72353 | 2024-11-25 06:20:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 6e62f652-ff8a-36d1-a6dd-667ee610ba84 | -1.77786 | -52.72919 | 2024-11-25 06:20:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 303abcf5-d442-3efc-ab1b-a2b0b5ce0c6c | -3.05352 | -53.21946 | 2024-11-25 06:20:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e9f3fcd7-7135-35e4-8b9b-a5c8d71a92ad | -3.165 | -45.2722 | 2024-11-25 07:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9a737466-cb51-3ecf-b7b8-db07aa3b5393 | -3.165 | -45.2722 | 2024-11-25 07:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| eef88d80-d660-3eb3-b25f-3427cb3b52aa | -3.2757 | -45.4477 | 2024-11-25 07:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8ae6280e-61a5-3a27-99ce-73f77db48096 | -3.1285 | -45.1158 | 2024-11-25 08:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6c558690-5320-35bc-a667-7766f65daf40 | -17.43 | -44.89 | 2024-11-25 10:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d6b8cbcb-dc26-3558-88ce-58011ed33675 | -17.4 | -44.88 | 2024-11-25 10:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 696c1602-859e-3896-a091-5e47a7399765 | -3.6878 | -44.9111 | 2024-11-25 10:20:00 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 115.9 |
| abb5abd9-c660-363e-8571-ed9e3361ce8c | -2.0255 | -47.3893 | 2024-11-25 11:10:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 344dc048-a78f-3390-a3c4-93464fa2f0fa | -3.50005 | -42.49568 | 2024-11-25 12:12:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 36.3 |
| a897c35f-1856-34e2-9986-1f606a8779c1 | -3.94812 | -42.79234 | 2024-11-25 12:12:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 0d10fc93-de83-3ae9-905f-c07f6dfbb67a | -5.17927 | -35.52119 | 2024-11-25 12:12:00 | TERRA_M-T | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| abc5ace5-e681-326e-b907-9d40094d1ebc | -6.05754 | -37.05754 | 2024-11-25 12:12:00 | TERRA_M-T | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c2f45231-6248-3c75-9d54-d97ff7bbb729 | -3.55389 | -40.17602 | 2024-11-25 12:12:00 | TERRA_M-T | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bfa7defb-45ee-334b-be11-6a5e464b35aa | -5.1851 | -35.51425 | 2024-11-25 12:12:00 | TERRA_M-T | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| b89bcc40-fc27-3554-acc6-742218c98292 | -4.20886 | -38.64961 | 2024-11-25 12:12:00 | TERRA_M-T | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 8d05709f-d9f6-3756-b4bc-c3debf6cfd27 | -4.18459 | -38.36463 | 2024-11-25 12:12:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| a659a5b9-aaf0-31b1-a0c1-3f068c437f83 | -5.18332 | -35.52753 | 2024-11-25 12:12:00 | TERRA_M-T | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| 0567fdf0-1665-3326-a6ad-9500dad9edc5 | -8.51116 | -47.05698 | 2024-11-25 12:14:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 32a3a6b9-a66c-3475-bf00-c8e3dbb3b9e9 | -23.12538 | -45.30015 | 2024-11-25 12:16:00 | TERRA_M-T | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 72438853-2a5a-3062-a21f-942fc021294b | -18.66338 | -40.06093 | 2024-11-25 12:16:00 | TERRA_M-T | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 361aff1e-76dd-38a4-89c0-2a46922f38ea | -17.3021 | -58.1791 | 2024-11-25 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| fc8a4fc5-bde5-32e8-9db6-7878ea5e426a | -1.3471 | -54.6377 | 2024-11-25 13:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d73c5ff4-15d0-3e68-b526-09bfa784fc84 | -17.3021 | -58.1791 | 2024-11-25 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| b7ab4eaa-47dc-3a53-a6d7-792e72a60818 | -1.3471 | -54.6377 | 2024-11-25 13:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| c4f8046c-1fef-31bf-b779-44f7f54f82ff | -1.3471 | -54.6377 | 2024-11-25 13:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 34055155-0152-3464-9be7-fcd1bfcedbbb | -3.0393 | -48.5082 | 2024-11-25 13:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 03aa0144-8b4e-3a25-bb65-0f3b615b2eee | -17.5865 | -57.5739 | 2024-11-25 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 981feead-d8e4-35ee-8c62-4d36eca8a16e | 1.335 | -50.621 | 2024-11-25 14:00:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 93.3 |
| b715eda6-47c6-3d6f-9e55-5a5076d541a3 | 1.2428 | -50.7264 | 2024-11-25 14:00:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9b1f1b54-a812-3ad0-8004-3c204ceefad4 | -1.3471 | -54.6377 | 2024-11-25 14:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| cd2fff82-0da7-3cec-bdab-262c7e3a3e26 | -25.1073 | -49.3567 | 2024-11-25 14:10:00 | GOES-16 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| 2adee5b4-34bf-32b7-b600-40d3bcb95963 | -17.3626 | -58.0703 | 2024-11-25 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| b5c5d1bf-2e6c-3ea0-b978-5c1fc65de77d | -17.5865 | -57.5739 | 2024-11-25 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |


[Clique aqui para ver as próximas entradas](README58.md)
