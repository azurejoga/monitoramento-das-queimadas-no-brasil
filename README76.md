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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 027da9be-c53e-3ae4-ba87-cc9e4c74b52a | -2.2297 | -53.7026 | 2026-10-04 15:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 7fd76910-24f8-3274-9e63-b8f6925e4adb | 3.5481 | -60.6813 | 2026-10-04 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 21e0bd2d-9379-3046-9f99-14754be63708 | 3.8965 | -60.3322 | 2026-10-04 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 4f489f90-3202-3f18-bc11-208ab9705bb8 | -6.1783 | -52.9124 | 2026-10-04 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6d419c93-b183-3168-97ae-ff117e25a989 | -9.4918 | -64.6902 | 2026-10-04 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 7c1be7b5-1da9-3e86-9f0f-112b9af2d51b | 3.7849 | -60.98 | 2026-10-04 15:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| baa09a78-213a-340f-8275-fc27f1890adc | 3.7483 | -60.9807 | 2026-10-04 15:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 71136054-6eee-3a3b-bb8e-25fc1ae18f95 | -2.2113 | -53.7029 | 2026-10-04 15:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 362964b6-1701-3005-bfe9-cd899473bacf | 3.8061 | -59.9912 | 2026-10-04 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 7fc72248-d754-3b69-be4f-d7741351bc8d | -2.6859 | -49.0325 | 2026-10-04 15:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 133d06a2-60a6-3340-af7d-ff0cb5fed237 | -10.8189 | -57.1993 | 2026-10-04 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| cbeac949-234b-3058-ba8e-0dfbcccf5233 | -1.0911 | -54.1202 | 2026-10-04 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 02c41353-f9ac-37d0-9271-1c1e27d019b1 | -10.8377 | -57.1979 | 2026-10-04 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c2a36951-cb13-3117-8ab0-f4a462513a3c | -12.1967 | -57.1103 | 2026-10-04 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| cfb23b09-ab56-3c09-81db-ae37709455f1 | 4.1134 | -61.2193 | 2026-10-04 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| da899d4b-543a-3906-8e74-b5fc5f84fe1b | -2.6027 | -51.8413 | 2026-10-04 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 6b8517ff-53ab-3f67-a2b7-d3a00bb1bf15 | -1.3927 | -49.2727 | 2026-10-04 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| dec0b5fb-8e57-3f90-9246-718bc2d403d6 | -1.0911 | -54.1001 | 2026-10-04 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| dc5a659e-ab2a-3e46-bb9e-5d0c48c67b64 | -5.8411 | -53.5002 | 2026-10-04 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 17a5c9f8-5ff2-3e3f-b632-ba616b4dea30 | 1.7583 | -50.8232 | 2026-10-04 15:10:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 60.6 |
| a5cc4650-5b87-3898-ac90-266ddf8e87b6 | -2.2113 | -53.7029 | 2026-10-04 15:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 99946c7a-e305-38a0-928f-2fb3e4ae12bc | -12.1967 | -57.1103 | 2026-10-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 9cea60bf-6b93-3bce-8dee-eb214644516c | -1.8693 | -50.6127 | 2026-10-04 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| ea025e35-d194-3ce5-ad40-f5e76bd2c696 | -0.84 | -48.618 | 2026-10-04 15:10:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 7ffff8f9-ce6c-36d4-9217-1b081329a389 | -1.4672 | -48.9097 | 2026-10-04 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 76ae17ff-2b06-3829-b1af-c26cd5ae8009 | -1.4563 | -55.1737 | 2026-10-04 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 34b03325-bcf1-3033-b371-bc6bbbd9446d | -10.8377 | -57.1979 | 2026-10-04 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d75b904a-eef6-3ba5-b11d-b6af9a11e28d | -2.2297 | -53.7026 | 2026-10-04 15:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 473dd70b-a703-3b13-8014-b024959f86cc | -12.1777 | -57.1119 | 2026-10-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 831ae07f-2120-3401-b72f-1cb53a3da013 | -1.1991 | -55.6909 | 2026-10-04 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| f32e2870-20b8-3304-8806-fe96a95586ed | -9.4432 | -67.1751 | 2026-10-04 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0cce96b5-9532-3323-9b41-192dfe4ef3b4 | -12.1969 | -57.0903 | 2026-10-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| cc211745-72ce-3a5f-96c3-67f06752de05 | -1.3927 | -49.2727 | 2026-10-04 15:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 4501829b-5038-34ca-8458-4cf77e301c55 | 3.4155 | -51.3021 | 2026-10-04 15:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 31d5bae0-8993-3947-8726-dd50dbf87dc5 | 3.8965 | -60.3322 | 2026-10-04 15:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4c2081e3-1143-3115-bfde-3f792d3e0aec | -12.1779 | -57.0919 | 2026-10-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1a889af8-433d-3120-80bb-cc36f05af161 | 2.8909 | -60.465 | 2026-10-04 15:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 4d23efbc-6500-36d7-9d95-0915c8a937b7 | 4.1697 | -60.7443 | 2026-10-04 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d3d96a4d-934f-3281-b567-dc2753281619 | 1.547 | -55.7268 | 2026-10-04 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 79beeec0-faf8-3416-b912-3ac2e260cc72 | -2.8899 | -54.0711 | 2026-10-04 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ec9ef30f-6919-3cbd-84b1-64a26375f281 | 3.9157 | -60.0461 | 2026-10-04 15:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8dd3ee06-da77-3719-9b0b-f5573de29de0 | -12.2154 | -57.1287 | 2026-10-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| e4301ff5-ac03-3c5e-a5f7-3b3a14639767 | 3.9351 | -59.7019 | 2026-10-04 15:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 291fc951-7ab6-3425-8c4c-40a53b85bb1c | -12.1964 | -57.1303 | 2026-10-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 2da9aef8-cd6a-3911-b91b-f036389dc45e | -2.6027 | -51.8413 | 2026-10-04 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f6a44aa2-0276-33e9-ad01-2e56f4c79565 | -1.8877 | -50.6123 | 2026-10-04 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 65022f18-c349-3693-a294-17f2e8180469 | -1.0911 | -54.1202 | 2026-10-04 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2f21e1dc-a35b-3240-82f1-75e292d8db4f | 4.2249 | -60.6671 | 2026-10-04 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 93.2 |
| ed36f61f-d2c1-355c-a4a3-c61af416c19c | -2.9265 | -54.1305 | 2026-10-04 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8d2a15ba-666e-3ffd-a2a8-cd68de68a1f7 | -13.5197 | -61.1319 | 2026-10-04 15:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 98.0 |
| bcdc7bbf-72e0-3ee0-a26c-9589cf1b4a6c | 3.7849 | -60.98 | 2026-10-04 15:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f4ae2ebb-47a5-3e77-a01b-b7e7c4d238c2 | -6.217 | -52.6851 | 2026-10-04 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f0262039-c004-3269-9357-2c3feaf1e5d6 | 3.434 | -51.3015 | 2026-10-04 15:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 97.0 |
| d0a81523-ce7c-36a3-9c97-507da20dca05 | -2.5658 | -51.8628 | 2026-10-04 15:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5f99dec9-b324-35ee-acca-990419b01f81 | -11.66 | -43.63 | 2026-10-04 15:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e698a759-f9ab-35d8-9bab-a35d96b8042c | -8.77705 | -37.23881 | 2026-10-04 15:16:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5f2e09fd-963a-3cf0-9924-ff895a651df7 | -7.03218 | -37.3283 | 2026-10-04 15:16:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 50104e67-33db-3019-a6e9-90968d77fa5a | -6.82938 | -38.52743 | 2026-10-04 15:16:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 65be8b8b-b000-3e75-8917-5b7725d165ed | -8.66004 | -35.23882 | 2026-10-04 15:16:00 | NOAA-21 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cae4277c-c718-33e1-a213-e36ff5696b7c | -6.6886 | -38.49074 | 2026-10-04 15:16:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 7c5b72a8-a6c0-35eb-85c8-ccc68aeb5eab | -6.82519 | -38.52441 | 2026-10-04 15:16:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 46738ef2-bae4-38a4-a9e1-042b902772f6 | -6.82657 | -38.53438 | 2026-10-04 15:16:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 390f8106-ad64-3814-87a8-5ded66317ff2 | -8.3232 | -35.28257 | 2026-10-04 15:16:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 87ec3da3-7a22-37b0-b9c2-71cda004452b | -6.76223 | -36.41938 | 2026-10-04 15:16:00 | NOAA-21 | PEDRA LAVRADA | PARAÍBA | Brasil | 2511103 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8903d60c-4b6c-3b72-8449-3c77ff23a96b | -8.77945 | -37.23825 | 2026-10-04 15:16:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd0bafae-955e-3a9d-8d4d-f7cf63cce806 | -8.76538 | -36.63946 | 2026-10-04 15:16:00 | NOAA-21 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 38ee0c41-33ea-39b5-9f65-61a804a98edf | -6.82815 | -38.51802 | 2026-10-04 15:16:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 0d4afdce-75af-3eef-8165-fbe85e8d626f | -6.93196 | -37.42059 | 2026-10-04 15:16:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d5152ff8-14a6-32b6-8b3e-d1b3cf44808d | -7.03104 | -37.31995 | 2026-10-04 15:16:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 815675e3-6d94-3131-ac32-f95ee2cdc1a3 | -7.03161 | -37.32411 | 2026-10-04 15:16:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 11.4 |
| a255d523-ab55-39c3-9c77-e0ad6f670ea0 | -6.82246 | -38.52342 | 2026-10-04 15:16:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 03a4207f-08bf-3203-a7e1-f16bfb251aac | -6.82372 | -38.53302 | 2026-10-04 15:16:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 6ea04c58-0966-3783-8d08-bf5a4ae118c7 | -8.78862 | -37.39967 | 2026-10-04 15:16:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 35c17925-16c6-383e-97cd-ebee0a63d1af | -8.76591 | -36.64348 | 2026-10-04 15:16:00 | NOAA-21 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| bf56aac5-6fd1-359e-bfd8-726953feeb35 | -6.82583 | -38.52905 | 2026-10-04 15:16:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 23.2 |
| bdef2f99-e22d-3ab4-a5c6-bb30d93eb8f9 | -8.19552 | -35.04792 | 2026-10-04 15:16:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9ae6e04a-ad14-3a54-a312-ddaf888f0f34 | -8.20062 | -35.04725 | 2026-10-04 15:16:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 9ddc98a9-1caf-38ad-8802-5a5573eb96c8 | -6.68669 | -38.4913 | 2026-10-04 15:16:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 85be702c-c5ec-36bd-a588-7cf5e86d959d | -10.21926 | -39.38578 | 2026-10-04 15:16:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 462b25f9-24a5-32fd-b03d-81d7ac95dda3 | -7.16262 | -37.33228 | 2026-10-04 15:16:00 | NOAA-21 | SÃO JOSÉ DO BONFIM | PARAÍBA | Brasil | 2514602 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 31f5e202-6f0a-35ab-93d8-24efa0820691 | -10.21968 | -39.38548 | 2026-10-04 15:16:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4f39df9a-dff0-3988-87c3-e3ec0995f6f3 | -9.14101 | -35.43449 | 2026-10-04 15:16:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ddff2b1a-70f6-372c-96f5-4fad20336b95 | -6.82306 | -38.52798 | 2026-10-04 15:16:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 8e06f91e-a193-3267-b9ea-5aa077131438 | -6.82878 | -38.52283 | 2026-10-04 15:16:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 1d7786a2-760d-37f1-aeee-38f5982bc486 | -10.38343 | -36.8918 | 2026-10-04 15:16:00 | NOAA-21 | SÃO FRANCISCO | SERGIPE | Brasil | 2806909 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| cf8788ac-b943-39a1-9890-afbc5ed18d46 | -6.79158 | -38.19253 | 2026-10-04 15:16:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e5ee10bf-49c6-36ce-8da1-2e80c1c27de7 | -5.86835 | -35.95156 | 2026-10-04 15:18:00 | NOAA-21 | RUY BARBOSA | RIO GRANDE DO NORTE | Brasil | 2411106 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2882b691-ce98-3ce9-957c-d9af321f5067 | -5.87359 | -35.95076 | 2026-10-04 15:18:00 | NOAA-21 | RUY BARBOSA | RIO GRANDE DO NORTE | Brasil | 2411106 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d1bce23c-f0b4-3396-83fe-f0e80fda010a | -5.13731 | -37.34313 | 2026-10-04 15:18:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f0021217-8945-3776-a141-b339d4d2e04c | -5.29511 | -36.92722 | 2026-10-04 15:18:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 11.9 |
| ce6e565e-8d1c-3d07-9fb0-84cfbf239d61 | -5.20928 | -36.75832 | 2026-10-04 15:18:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 3ad6fe3a-927f-379d-89cd-c3eea9a2214f | -5.29563 | -36.93089 | 2026-10-04 15:18:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 2bfa1622-bd7b-3069-b392-fcbb0471de07 | -3.94531 | -38.36332 | 2026-10-04 15:18:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5941f8e5-7221-3b52-9be9-11b6322366fc | -5.25629 | -37.05452 | 2026-10-04 15:18:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4f07b313-0cbc-3097-869f-00d537145a00 | -6.08121 | -36.5485 | 2026-10-04 15:18:00 | NOAA-21 | LAGOA NOVA | RIO GRANDE DO NORTE | Brasil | 2406502 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 60139e22-448b-36d8-86c4-fe5875528548 | -5.29454 | -36.92803 | 2026-10-04 15:18:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 8dce341f-5abf-3ff1-b7f3-ca4eb4facd7c | -5.20878 | -36.75476 | 2026-10-04 15:18:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 0eb8092f-8d82-3dd6-8dc3-edbac519e433 | -3.74087 | -38.94973 | 2026-10-04 15:18:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c8eb1e4b-06c0-30b8-afd0-2ae4e7fb008f | -3.71 | -40.34324 | 2026-10-04 15:18:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| f4613704-6a32-36fb-a51b-43363eaf37c8 | -3.75663 | -38.66578 | 2026-10-04 15:18:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |


[Clique aqui para ver as próximas entradas](README77.md)
