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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95033b15-d3bf-3e7d-99b6-62d145325bc2 | -2.66811 | -48.79766 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7cb0a9a-7449-3917-be08-e9b1a1bff86d | -1.07351 | -53.62984 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7798a28e-ce75-3089-b4df-ba8a39ab88c4 | -1.96064 | -46.45399 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be9d51c8-1f54-3942-9a3f-4dbc804a2790 | -1.58504 | -52.24995 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2dc5bd4-3ce2-31fc-9fa8-0f48cef15145 | -3.26538 | -53.62795 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 128c55c2-09fc-33cc-9adb-15af47048710 | -3.72607 | -49.9378 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 515170ab-0f01-3e2b-898f-040caf5c71da | -2.56406 | -54.34329 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c3b1082-f00a-3adb-8a92-22574b10357d | -3.61166 | -54.74466 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 460c3d3f-4723-31de-92e5-c42904922b4f | -2.35872 | -53.86034 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49292323-bd15-3bb2-9d3b-b4b85c9708e4 | -3.74585 | -52.26992 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27107fea-339e-362b-a0aa-c783079af44e | -4.06974 | -47.08777 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4701c677-238d-30fe-aa34-75ff4f326d6c | -4.18912 | -50.67754 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4e9c3e4-6332-3159-baef-fb29fee60ae5 | -4.04168 | -46.83211 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9056b353-8722-3cd9-a7ca-8cccdb2316fb | -3.28391 | -50.43353 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f28387e-2bb6-3ccb-b8a0-dc804e4f9401 | -3.59323 | -54.74586 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dd54bd8-991b-3bce-b2bf-2c6cd53496f1 | -2.84698 | -53.35041 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37375660-80ca-376f-a60b-f48560910a0b | -2.8337 | -54.08851 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65b1ab63-81a6-32d2-9cc1-f79e7e82a88d | -2.72014 | -45.07449 | 2024-12-02 04:48:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53455171-28b8-33b9-81af-74134b845abc | 2.42599 | -60.65564 | 2024-12-02 04:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e23bec9-e04d-31ad-a3d8-35b311321bd6 | -3.5366 | -54.08265 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdee32a4-4dbc-3541-be1b-bac653e0bc9e | -3.94344 | -49.98189 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff3157ea-8182-30bb-9c21-482abc51cc1a | -1.99834 | -53.28324 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5006c2b4-3f71-34e7-a680-5f539a389976 | -2.8106 | -54.06559 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8d521e6-e721-3c70-94ea-07a65e8f4acb | -3.08261 | -53.76339 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd62d273-634b-31ab-924f-1c60a83c9d14 | -4.26193 | -47.61739 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a1e5be2-d3dc-3295-96af-8b43d1d3514e | -2.83717 | -54.08907 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d74f162e-f9b6-3f1e-9ed5-80c0e8bd08a7 | -3.29586 | -53.6781 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf427297-fc4a-3e3b-bddd-7d57c533389b | -3.93737 | -46.50057 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a78db8bb-f019-3ecd-b7b1-7d0429f8784c | -2.43698 | -54.02918 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59235e09-df6d-3a6f-904f-2537e66b3a51 | -1.00256 | -51.71922 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1496044-c67c-3271-bd78-13c348b600f0 | -1.35064 | -51.38672 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 788dcb4e-ebb6-3691-89e7-16389ab6f392 | -3.6222 | -52.49483 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a791694-c28c-336f-9bf2-c6d7b444a823 | -1.73553 | -52.77743 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 25674b2d-4416-375a-bf62-ade1d3d6b6da | -2.86418 | -53.98761 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cef9a709-af3d-31a1-bf1c-e5d9d8b1c468 | -4.05211 | -50.90386 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c95f79ba-c9c8-3c90-9cb1-e3ddc607cc8b | 1.00094 | -59.47012 | 2024-12-02 04:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf76709d-01c6-3344-98c1-bd128e351c0b | -1.17084 | -53.41707 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2aecfe2a-634d-3fd9-be26-a4ae7a503fd4 | -2.37677 | -53.65866 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17716a96-ab1d-3b85-9cd3-ee3b54ed2421 | -3.06634 | -53.68865 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 14a63883-4f51-3c0b-a50a-ce18c62231a0 | -1.31573 | -51.67314 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9621438-d3e3-3514-9ae1-f5de72560b4c | -2.264 | -53.61853 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| daead74f-7725-300c-89e5-56b8ab4e3710 | -3.71365 | -51.0699 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfd2692d-fff2-30d4-84a3-1e3f0c157f88 | -2.04526 | -51.20356 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59750703-b0c7-3e68-b1cf-4b97af510ddf | -3.75713 | -52.67273 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee41c456-a007-3e07-b286-31736243b26c | -4.18127 | -50.66164 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60ab9696-08fb-3523-ba12-bd230e6d451d | -2.6762 | -46.61564 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d9013af-9dff-3c60-b76e-2cb83e637bf7 | -3.05622 | -51.06029 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15fc3418-af0b-3e34-a3cc-c2970a8cde83 | -5.36784 | -44.90245 | 2024-12-02 04:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9868e032-cd92-3dae-b96d-bb09e8df31fb | -1.08892 | -53.1358 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5cc838a-40bb-30d5-a2d8-a9bf64bde2f1 | -2.88145 | -54.21481 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8f18bdb-88b8-38a8-94b5-5e675f654114 | -2.57715 | -53.6773 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cb7557d5-2f84-30e1-8f9e-03014f31fe4e | -3.24529 | -53.86406 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e54f8bb6-3461-3dc3-bfa5-cebc841b35aa | -2.67969 | -46.61977 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42fd1af7-b30f-3dfe-9f94-e7c65d5f6f19 | -3.11366 | -53.98656 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8165145c-9122-31a4-8576-6c3ecd52faed | -1.68577 | -53.94652 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 126022a1-970f-393f-a0e9-7b8d72cd5250 | -3.40631 | -50.23501 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fd8314a-cdc8-3c5f-83ee-a216dafdaf8a | -3.93621 | -46.9213 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 767b460e-ec99-3563-9240-1773786b9a56 | -1.82867 | -46.22795 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b56496eb-3734-34f2-a0f2-6ce8efe7871e | -2.43776 | -50.49615 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79d5b91f-e459-3521-8c1a-35e49589f6cf | -3.40298 | -51.25324 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72983c9b-b855-39b9-b58a-78845503e9dd | -3.0874 | -53.71072 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e0e963c-7d34-340a-ba43-7415344b19e5 | -3.05032 | -54.49715 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5aa27a33-5956-3fdb-b074-f7c4e6997d91 | -2.88253 | -54.00609 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e39d776-711c-3d18-8b2d-26543a2c6bfa | -3.09704 | -54.04626 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 476ef664-1b5e-3cd5-a7c5-691797f8f4a2 | -2.5908 | -45.99931 | 2024-12-02 04:48:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f80e3b5-16f4-3b35-aebb-147b560e2798 | -3.03659 | -53.43244 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86b77da4-f02e-3213-a003-85332c5647c8 | -3.11429 | -53.80581 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68c7e089-cc3d-3a40-8bcd-926ff77f0845 | -1.64367 | -53.86576 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81909126-9490-3b1b-92c0-797f2cdad4e9 | -3.13584 | -48.53645 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cd5fb7b-a219-36f4-8bef-d2d2cf197bd2 | -1.57482 | -51.21464 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f270705-45ab-30ba-8bf1-3a632997e8a9 | -3.0955 | -51.2653 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db41a508-902c-33ad-aead-9753ba4d8e53 | -3.48702 | -53.82142 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1586923b-e7f3-3efd-874b-0163e3cb3200 | -1.7316 | -52.78046 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94a83238-b691-352b-b9b2-931acbfb9ec0 | -2.26578 | -53.60741 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bee8d4aa-5218-3a7f-87bd-5aacbdbaf39b | -1.3209 | -51.74791 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00c50146-b45c-3f2a-a991-c0ec66ce43c0 | -3.96226 | -46.50436 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92e1feaf-4cda-30a9-9451-ce08c3b548db | -2.95135 | -51.79227 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcdfef19-84ad-33c3-a29b-6fdb5dab8e9c | -2.88393 | -53.97513 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a03602bc-021e-35b9-abd9-57525f8326da | -4.32043 | -45.92485 | 2024-12-02 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10e102ec-b732-343a-8657-aa1ee887d727 | -3.36131 | -51.1296 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c6fcdce-888f-3830-83a6-2016644963f8 | -3.77615 | -50.04395 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e9b0142-071e-32b6-a7a1-cd71653bc770 | -3.70422 | -51.06487 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98233f4f-d30b-340d-b7bf-5128a3d9843c | -3.7596 | -50.06031 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25f42169-fcc8-39ba-a8b0-ffbe2ad53695 | -3.02528 | -51.5402 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bac28be-e1ea-3dea-aadd-50f5f1ab36aa | -3.23635 | -53.63467 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b384a55-421d-3421-84e5-7b2dd9434c96 | -2.37486 | -52.19584 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dec8d30-40ac-35d9-aa83-c138a835ae44 | -2.89898 | -53.96974 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e16ebe80-f4fa-3b83-985c-968d2059650b | -3.52629 | -52.80064 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b74a30ba-2ead-3e81-93d7-7c22ba278c8a | -4.26422 | -50.84944 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4877cdb8-07fe-333b-bab6-8b56aa0869f0 | -4.07263 | -46.6846 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b60d5a27-90d7-344e-aa36-a46eee99eb6a | -2.86867 | -54.00391 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d1e7321-fc8e-3d28-9c1f-ad0a23beada4 | -2.8289 | -51.83707 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de6b8258-021c-34fe-9a99-0ccc476b9d3f | -3.25486 | -50.57471 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77ac0cfd-c644-38a9-b7bb-15dcbb43cdda | -2.35899 | -53.65973 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c4bd3d3-c638-3e43-8679-63fc293f5af3 | -4.47486 | -48.11957 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2cb4ec3-4aa9-31fd-aac1-944c9269337c | -2.50467 | -46.10783 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01442a81-03da-31fa-9a4a-1d387eb8033b | -1.36961 | -53.64818 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75cd93f1-adae-3260-91c9-72fde14a800d | -3.50219 | -53.44123 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 47716494-ad4c-39e1-8bf0-ae2d34042eed | -1.24078 | -51.62999 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27d1ae7a-26a3-341a-a128-872b69a26b38 | -1.94999 | -53.34361 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README50.md)
