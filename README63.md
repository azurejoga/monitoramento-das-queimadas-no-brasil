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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b444a9ef-229d-3f6b-b548-642247d973b3 | -3.10907 | -53.81882 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2abf42ee-600e-3bcf-b547-ab9babb8b089 | -1.52012 | -52.03414 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fdc9bf1-54f4-3547-803b-ec5fbc0d0f46 | -4.0109 | -53.72823 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 081a74fd-0dad-3c66-8222-55011eb6e57c | -2.26503 | -51.2589 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0538470-cd75-3b84-bc76-7533ece0d409 | -1.22334 | -51.79886 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faf9d579-a705-3599-a572-faddce61dec0 | -2.87711 | -53.32151 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a83c8ab-7963-3ddc-b3f8-62d832ac01fd | -3.06985 | -53.91831 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6acfaa0-dd66-3188-b10e-1cd77d066f56 | -3.49684 | -53.82042 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc7e906b-7ef6-362d-9291-d4f4036cdd29 | -3.49845 | -53.81012 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 291cea20-ab2b-3ec9-b324-e66528bff195 | -4.42805 | -46.57706 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 588682a4-526c-371c-be70-7acc03bcdbb1 | -1.32637 | -55.83486 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57ac82c9-6596-3466-b5b5-0a018a125130 | -2.65095 | -49.46856 | 2024-11-29 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82e7c48c-17cc-3295-8e3b-69e486fd8e08 | 1.86508 | -55.78406 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b399fb8-b109-3bd3-8f08-832ceeacc1ef | -1.89961 | -50.57095 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f9e6bef-5e16-3057-97e1-980065548300 | -1.58166 | -52.27128 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8912cebc-0140-3711-9ae9-e491b32801ef | -1.00118 | -51.71695 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f61f3f7d-7ba8-36e2-997a-f4c0c9311674 | -2.73396 | -54.10867 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8f017b0-ce6f-3b47-aee2-19f102734dc7 | -1.08916 | -53.35823 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dccc84ff-25ff-3281-bb1f-0ebf06beb34c | -1.17034 | -51.94051 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10de50e0-e248-3e06-b332-989627ac05ba | -1.21878 | -51.73935 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 865712fc-7a90-39d3-90bb-81b041da2ca7 | -1.31204 | -52.86563 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6d36231-483f-332c-8601-c9d28659a93e | -2.82614 | -54.08482 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ab31248-3ab8-30e7-bfe7-97bb6a7d6130 | -2.83199 | -54.02578 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2889d4b3-b775-3c83-a580-a0d1586aa9e2 | -1.47068 | -52.67873 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c9e7145-99f5-3a84-8fa0-84187f32ea8e | -2.97348 | -53.88221 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec7485ab-9979-30cb-a4eb-2cea0f1308ba | -1.9994 | -52.09637 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27c6aefa-61fa-399a-b084-c0c33e06a6a0 | -3.31434 | -53.28794 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8cbd9e7-922a-3baa-a860-7e79817589b5 | -2.83691 | -54.01597 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06afd1c4-1c18-3c70-98ee-6beefd0a3d4b | -3.05736 | -48.51643 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96bb21f1-02f4-3c56-85a8-f156dea41fc1 | -3.09341 | -54.02753 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5317b780-345f-362d-bcee-e42ed72dcebc | -1.42446 | -55.27942 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea8f0b23-100f-3fa5-b6bb-ccbd1ce5fccd | -1.28356 | -51.65697 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e0ab176-eb0a-3c00-a4e6-ed800ea960b5 | -1.9121 | -50.56053 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2ce1aa2-5b53-3824-8342-7c9bed15e621 | -2.73329 | -52.58587 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c47bde94-8c9b-35b8-81de-6d0e010a9275 | -1.19026 | -52.12107 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b4b011a-761c-3fb5-ab7e-80eac02eec25 | -1.09197 | -53.64685 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 337be40c-eddf-3edc-8b6f-cb368e897f68 | -2.79982 | -54.12313 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42b9cb6f-dadf-35f4-ac4a-e9d0bbd093ea | -2.85997 | -53.99838 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f18cfbd9-c70c-3482-9389-f00b39359142 | -2.90629 | -54.18202 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccf0a3ee-0e92-332c-b6d0-77debe2c7247 | -0.92696 | -51.62844 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1fadc6e-3c78-3855-9ef6-86b50d57b799 | -1.71323 | -52.49614 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 24040bc4-9806-3c27-9ec1-d9231101ff8d | -1.63532 | -53.86966 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5324bc1-d8cb-3ff0-a2dc-8e5909a88895 | -2.83468 | -49.88849 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f37f641-1a88-3420-9c01-5fff2b55e31f | -1.10532 | -53.40633 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c226b31-648d-3ce1-916d-e6999b22cb94 | -2.5401 | -54.06453 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 511c8c79-8afb-321d-834f-295ee4d7208a | -0.96337 | -51.64849 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 889770bf-beaf-3889-b0c4-620abfa4bd07 | -2.8183 | -54.04834 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ff4fb8e-93d9-38ab-bfd5-b488870483cd | -4.40441 | -47.26732 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9b9e6bb3-f56b-3463-8851-89a2b3d7cfe6 | -2.44605 | -53.66567 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46cefac8-555b-39b3-baf0-546f43b6a753 | -1.06946 | -53.63626 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dff3f4fa-5c65-3d52-b31f-9d7df6c04453 | -1.68398 | -54.23183 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85e7546b-cfc9-3059-8d14-01e7a5ad714a | -0.99725 | -51.72002 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f175744-6596-3164-9f2d-60b114eea31f | -1.10663 | -53.59638 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6787c2ca-e55b-3898-bfdb-943cfc7ffe20 | -0.23705 | -53.76097 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a33bae62-27ab-3113-839d-c6f8c3fef618 | -1.88607 | -53.30725 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dc6adf3-6edb-3c47-8db5-bd46b41a5ae7 | -4.11389 | -50.77709 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 427daa40-f0cf-360f-923e-e68ef179cf3c | -1.59882 | -53.81816 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b7b0342-2b69-33b4-b068-bf4ba2fadb87 | -1.36273 | -55.17953 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cf2572b-72bc-3cc5-8cd6-d9afa03ebaf4 | -2.52616 | -54.02355 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fda086a9-58fa-3fa9-b390-32af85c902d4 | -3.84085 | -52.39249 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 806a895f-5c9c-30a8-901c-0c5ab9c505b4 | -1.19241 | -51.77573 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8e3dd24-ea64-3cac-a2dd-cca5f440ea30 | 1.28237 | -55.92146 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4258c376-0f65-338e-8882-8b27c199e2dc | -1.62506 | -52.27798 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f90a8100-892e-38b1-9aa1-f2207af060ed | -1.70118 | -52.52996 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21a8816c-d72e-3346-9105-237767ebf917 | -1.36672 | -51.96656 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 682e3477-1323-3b69-a25e-aa4a66f419c8 | -3.96705 | -47.24263 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a705833f-2392-389f-83a3-2bddbd55f452 | -4.67243 | -42.38113 | 2024-11-29 04:57:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c4f30e2d-3663-3cfc-a80f-f45b441bff61 | -0.91908 | -51.63461 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56acf9f5-25cf-3e8f-9c8c-b1ff2e454812 | -1.25947 | -52.17833 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21d499af-a9ec-3d5f-a1b1-1870b6728042 | -3.23649 | -54.22327 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81084b4a-92ea-3274-a204-9d25d15a74b5 | -2.80411 | -51.58509 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8bf5268a-3e36-319d-9b95-a613dbe56dfe | -2.59331 | -54.22489 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c08582ff-d243-3c3a-8d5c-3d7a96a891c0 | -1.65439 | -53.81268 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edb2b2ee-5e51-3ed2-b41f-c77fc6cca258 | -1.26676 | -52.19744 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2c61fb78-628b-348f-983c-8bd3d1c4c9f5 | -2.84191 | -54.02731 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e877f81-ffac-3350-9b14-fa9085f5627b | -1.61285 | -52.29046 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 790d7abd-db94-38b2-b4b5-360f60b6e172 | -3.87066 | -48.36301 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4a1fb5cf-0551-3336-81c9-c7ad1df21548 | -2.25706 | -53.74179 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 969df7c4-f9de-3999-a7db-412882dc10de | -3.59348 | -50.36013 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05e678e4-c631-342d-868e-1d0442ec9faa | -3.03176 | -54.0321 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ab2cce1-5718-3dae-a0d4-eee99ef85c4f | -2.61253 | -46.56446 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e58af904-9da1-30d0-811c-1a26eca89c15 | -1.35114 | -54.98672 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f3f4285-51c5-3884-9c16-3b0947e3ec3e | -2.53115 | -47.33252 | 2024-11-29 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fe6f723-0ef2-35b2-9d55-1b7c53022703 | -1.62031 | -52.45986 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d99874e1-3924-3d2e-bbd8-c7d24833747e | -2.45721 | -54.00941 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20d85777-85a7-3cc2-8a0c-d6aef652df8d | -1.40856 | -51.58236 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd6390a8-4555-31db-a65d-d67fde9803c1 | -1.24594 | -53.35855 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49e060b7-370b-3a78-bfe2-0840cd1ab580 | -3.89938 | -50.19855 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b165622d-4e25-3dc4-ba57-13bd29c33bb1 | 1.21788 | -55.94368 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ffdf459-f441-3ad0-92ff-e6e4c6995f3b | -3.14828 | -50.86035 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b7b999a-1609-3ea6-81b7-0d7955a3d52a | -2.59503 | -54.08374 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b39882f-f6de-3d30-a388-c9a85e11f004 | -1.47686 | -51.95826 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9adebb4a-6c1c-388f-b262-507032a29690 | -2.04219 | -54.67979 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72c177b4-4fc7-3694-a97f-bd5e22ef95ee | -1.64953 | -52.731 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e61c83d-191a-3fab-abc9-c6cb510c8890 | -3.74072 | -51.83525 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21cd0322-16d8-32d5-a70c-10adf05767c4 | -2.8256 | -54.08827 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3fc36f5d-b377-3e9e-96c0-1eb19db7ad72 | -2.63555 | -51.76804 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdf24f80-383c-3ebd-9d31-a2a248c9ea1c | -3.52651 | -50.3823 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c86a9ba-6fde-301b-acee-023ca7c6c089 | -3.22329 | -54.06954 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e2ed374-577d-33b4-a11d-6817f9b12ca7 | -3.2944 | -53.67938 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README64.md)
