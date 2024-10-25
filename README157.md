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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23f7a604-af4e-388a-943a-d24233b3512e | -2.29787 | -51.28288 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 0b5c67e7-2ffc-3479-9f22-b994f6ca226b | -2.28952 | -51.14003 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c80c47f0-40da-3cb7-8b33-b315fd735d1e | -2.23443 | -51.06746 | 2024-10-25 16:52:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 32578d63-f6da-3012-934f-b5a951981fdd | -4.67057 | -50.97155 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 323d17fb-4308-36b9-83fc-1053694f4299 | -4.66952 | -50.96467 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fd0bc734-f771-396c-945c-6cbcd9ae1b8e | -4.66727 | -50.97205 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c9cb5fdf-9fb6-3791-8be8-767acc2a58a9 | -4.66674 | -50.96861 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 69992926-f505-3a3d-8148-0c1cdb61957b | -4.66621 | -50.96517 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 05971d51-4345-3981-b7bc-e7ee71681c3e | -4.66052 | -50.99421 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d6b5aa8-0bf2-3b7a-9e0e-09e5e708e1b2 | -4.65999 | -50.99077 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1719ed26-bf1d-3beb-bd00-e1936eb56199 | -4.65616 | -50.98783 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 480818bf-9d7c-34c6-bbde-4c1e504423be | -4.64734 | -50.90817 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2829b43-e3e2-3d2e-8d71-34c7804f832d | -4.64404 | -50.90867 | 2024-10-25 16:52:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd5639d6-e9a9-32ed-bd0f-ef43825c4688 | -4.54095 | -50.96738 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5158fb93-5ccd-365d-ad0d-47551db2648d | -4.53817 | -50.97132 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7dba4fe3-322d-33a3-926b-e9ae4e966c49 | -4.53765 | -50.96788 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| af105475-c72d-3d07-95a7-f6b8b774135f | -3.9522 | -52.25443 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e37106ae-a7bf-30ca-ae20-89b865712864 | -3.94885 | -52.25492 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 6993d31a-98b1-3b09-8f06-e83310fdc6b4 | -3.94604 | -52.25897 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 76e618c5-779f-36fe-a6e4-81a131d312eb | -3.9455 | -52.25542 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| e0e98d42-c05b-3d00-8b3e-8b8e35638328 | -3.91324 | -52.24582 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fa96c551-e785-3728-9787-ed4b7075c794 | -3.88731 | -51.96223 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 786dae4b-69c5-3c17-b530-6516bb5370ec | -3.86948 | -52.13347 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e7f6800d-3de5-33eb-8be8-d5af206173c6 | -3.86667 | -52.13748 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1846aef0-3fdb-384e-9235-ebf3e1ef4aff | -3.86333 | -52.13796 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e5b39382-5750-3ccc-ac00-b62d60e82be9 | -3.86279 | -52.13444 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d8e4fb55-10f0-3afe-8f5f-3839a3669729 | -3.79288 | -51.34254 | 2024-10-25 16:52:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a258a6b3-9ebf-32de-9ce8-9f5dcbf942cc | -3.77773 | -51.97888 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffe1b072-61c1-3bba-9359-ccb74007e604 | -3.7772 | -51.9754 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c77a852f-6f46-398a-9b2b-fc0b9fc42f89 | -3.77715 | -52.26353 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c4294451-414f-36b7-befa-6a81e66578b7 | -3.69457 | -51.63268 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a1b53520-e63b-34da-9730-c07f09f308bf | -3.68304 | -52.09418 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9a6acb42-3342-3c39-8cf9-8adc5f68bbb7 | -3.68249 | -51.08874 | 2024-10-25 16:52:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ba9af5f8-2364-3996-af7e-b67fa06d0639 | -3.61323 | -51.7911 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 8af8e75b-d68f-31fa-ba06-fa151ff6b075 | -3.60991 | -51.7916 | 2024-10-25 16:52:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 90020e26-ded9-3e41-9223-473b0ec8404e | -5.89454 | -51.39512 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d9f7e24-000f-3fe9-bd45-1188a3e6ffdf | -5.67284 | -51.56917 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8320d1b9-c14e-3a6b-b615-912711663205 | -5.67231 | -51.56566 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a983e98a-e63c-3e33-8885-c49f01ad9d39 | -5.63662 | -51.28569 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 304f9ef3-f06e-351d-a558-24cbfca17957 | -5.43202 | -51.39281 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f40fd617-648c-36a0-9052-a1f48643397c | -6.56067 | -51.57561 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 65f758ab-a617-351f-b072-d3e2b811aebe | -6.5049 | -51.94994 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 40c7b4fd-3c75-3471-8cea-7a1f383efff7 | -6.47921 | -51.44079 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69b8fc3e-5705-3ea4-a148-d0ec04cda38b | -6.22159 | -52.11869 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9a3b4ae7-456a-316b-b1ab-40cbfb21d91f | -6.21876 | -52.1228 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a460d841-f406-3f2a-868b-58645fac1c53 | -6.81377 | -51.56239 | 2024-10-25 16:52:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 2ffef123-806f-32f8-bbcb-4916de1cac78 | -6.69115 | -51.49397 | 2024-10-25 16:52:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ac57dbe7-ae57-3b31-828e-cadc602236d3 | -6.69061 | -51.49044 | 2024-10-25 16:52:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2ca843e2-b5d4-34b1-9c3f-e34873f71b28 | -9.3433 | -52.06957 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8bcdc286-b608-3be6-8e18-aac0c680cf2e | -3.63825 | -52.56131 | 2024-10-25 16:52:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0d7f9ce0-d0b2-3b62-a704-fdd891f375d9 | -3.51528 | -53.55647 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 476d320f-c091-37d1-9207-16c2cddb7d8d | -3.27766 | -53.68139 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 42d4e0b1-ad77-3a3b-92b5-dedde5f71e06 | -3.21907 | -53.36281 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 387e9bf5-55a6-3dbf-9fe3-14cd83e58d3d | -2.99957 | -53.44224 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2b66af35-583e-39a4-a434-7e9e0437de9b | -2.999 | -53.43843 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 899d7937-5cd3-3dc5-a288-bd8733692c79 | -2.61885 | -52.44977 | 2024-10-25 16:52:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8845af23-8233-3636-9f4a-833090aa6ffb | -3.10625 | -53.03496 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f70729e-7945-3b02-9a7a-8066ec402cee | -3.08067 | -53.23479 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9e6ef007-49d2-3c7c-8ffd-f61963197f74 | -3.07896 | -53.06152 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8e72e822-080e-3cfa-b277-8ad29ec72d0a | -3.07206 | -53.24741 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 11533529-c6a9-3ae7-8ab6-49f8f45c2b2d | -3.06642 | -53.23317 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6c70b6de-c5af-3efc-9674-3aa9b91b6288 | -3.0641 | -53.24106 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 86589ad3-2be0-3dd6-a022-0da7b21ce4e0 | -2.97372 | -53.27012 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6c9b545a-ff87-3013-8767-aafcd04db5a3 | -2.97316 | -53.26638 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| ee53c7bd-f78c-3ae4-99b1-c7d416279c68 | -2.96743 | -53.27488 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 320ed543-7509-343e-b0b1-860404af4345 | -2.89423 | -53.32354 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 675ba774-743d-3728-8ffc-0bd0fbac6799 | -2.78992 | -52.07647 | 2024-10-25 16:52:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cbf498e5-b05c-34cf-b751-ee54eb172751 | -2.78591 | -52.09481 | 2024-10-25 16:52:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 84872be0-9a7e-3c07-9ba8-5f83ab3b9d5e | -2.74222 | -53.19896 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 714bcc97-367f-3dcd-9d25-b81e2bff44d4 | -2.73881 | -53.19951 | 2024-10-25 16:52:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 392860c5-811a-3f65-b110-d97896c7897e | -3.90561 | -52.39195 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a13f06b5-4420-3b01-a04a-07a69131bf4c | -3.87801 | -52.32355 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 951d4a09-3b46-39a2-828b-18571859f255 | -3.84032 | -52.76689 | 2024-10-25 16:52:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0e6b0b35-fb26-3c81-a62b-dc654a418132 | -4.21199 | -53.66131 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b37517da-f0ba-3fd8-8be9-e24279e48ee7 | -4.16744 | -53.70013 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| ae924b3e-68ee-3d23-a5fd-e9bc07ed5b6d | -4.16685 | -53.69619 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| b75d914c-0e7f-3c1f-91df-41b61042dd12 | -4.16392 | -53.70067 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 397af6cf-4e4b-390a-a44f-5f4296174d07 | -4.16333 | -53.69672 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| ef1a8bca-abf7-3221-a674-6373837d0dca | -4.16297 | -53.48092 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f978d5f7-4cf8-36be-9c14-432800a7779a | -3.57168 | -53.54005 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2bdcf0be-1c08-32ff-88b8-ae9b7df5d16f | -3.5711 | -53.53622 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0e5009c6-1f00-3251-a238-764dbc1829a9 | -3.56705 | -53.53292 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4bfc2369-d675-3925-99e8-abd2f069590d | -6.23977 | -53.94128 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e828e539-5433-3d66-90aa-f0be065033d7 | -6.23915 | -53.93702 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 92560375-0173-3499-8c92-b805f34aa26a | -6.23542 | -53.91154 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 96d04b00-cf15-338e-ba45-02e0e4d7919e | -6.2348 | -53.9073 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6034f0a8-b284-3982-9411-363e5ab3d045 | -6.23177 | -53.91208 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 03f5e7e3-2032-30bc-bc9b-de83b090cfc0 | -6.23115 | -53.90783 | 2024-10-25 16:52:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b74e30db-fe05-3b2c-b353-7bc5ca51864b | -6.74107 | -52.94679 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 25d9f2ce-a216-36c0-8acf-f92911355c21 | -10.25539 | -55.02554 | 2024-10-25 16:52:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0fd3dcb-df6c-3979-9027-f7708b7ebcc3 | -10.25226 | -55.02553 | 2024-10-25 16:52:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4ed5ef2f-167b-3293-826e-25d61f694f84 | -10.13657 | -53.78442 | 2024-10-25 16:52:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 32c1043d-f2ef-386a-8188-3e543e9e0d9c | -10.10428 | -55.0997 | 2024-10-25 16:52:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 538a7310-7172-3c45-bb83-b52e7954df79 | -10.09345 | -54.1062 | 2024-10-25 16:52:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8d6f47e8-2c6a-3ac4-aca7-6ceb87e29a69 | -9.83271 | -55.06107 | 2024-10-25 16:52:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 63aba2f6-1fb3-3d0c-96b8-6d7b57f0ae1d | -10.01922 | -54.20496 | 2024-10-25 16:52:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8d62799f-c954-3177-b3dc-48a57ddbfb11 | -3.63564 | -53.96728 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c4be61f5-73e4-3b00-9ca1-052ab6dafb33 | -3.6321 | -53.96785 | 2024-10-25 16:52:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e6da46c2-d7c2-30b5-a13c-ca49afd656ca | -3.59107 | -54.6703 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| be89e5f2-2e5e-39b1-8259-09c8ef654cc8 | -3.58304 | -54.66702 | 2024-10-25 16:52:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |


[Clique aqui para ver as próximas entradas](README158.md)
