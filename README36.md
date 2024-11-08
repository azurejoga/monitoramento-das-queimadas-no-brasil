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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e753b5a3-b480-3950-9d1f-d4d0f42f4ff7 | -1.14894 | -52.00201 | 2024-11-08 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 316bf326-a5fd-37ae-9778-c160e555868c | -1.45796 | -53.42239 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28fdaaf3-dfc3-3932-a87c-ade320b46547 | -1.14366 | -53.71886 | 2024-11-08 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35fb398f-e6ab-33a7-ae20-109c6007e425 | -1.15468 | -52.00718 | 2024-11-08 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7762013-6dda-37fc-adb2-436aee3113d0 | 2.52056 | -50.94335 | 2024-11-08 05:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f9a2bd3-cb1e-37fe-b1eb-9f63f4edb43d | -1.50392 | -52.07152 | 2024-11-08 05:37:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c66e7983-01ce-3da1-9aab-5b133396c9df | -1.25854 | -53.35128 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 878095de-ca19-3614-b809-9353b5421aee | 1.00798 | -60.58368 | 2024-11-08 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f15f4dd0-faaf-3d93-9196-b3b0a86592c4 | -1.22907 | -55.81302 | 2024-11-08 05:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bedbb9e-62e3-3b8c-aeab-07c6f9579e65 | -1.11474 | -53.17541 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 939b5b5d-a0d7-3d4c-987c-1e0ab43b9fbb | -1.0979 | -54.20148 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fae94a12-3da7-372b-bedc-7a3e6b2172c4 | -1.16572 | -54.15808 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f990908-69c3-3a40-8d33-8caab65672e9 | -1.32887 | -54.60309 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 580e8629-d1c4-396b-8b71-4fb6df7aebde | -1.43316 | -55.6957 | 2024-11-08 05:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c2ee76e-7b1f-3c92-af00-f53816a69846 | 4.3354 | -59.82718 | 2024-11-08 05:37:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 106bdee0-2c73-3cef-8b25-3569d619c853 | -0.64106 | -52.39192 | 2024-11-08 05:37:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5a7af1b-7265-36b2-a110-7e156e0932dd | -1.16515 | -54.16182 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a244727e-d226-373f-9ff8-19989f1e057a | 2.52198 | -50.94449 | 2024-11-08 05:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26276d1d-c00a-3843-af29-175378431ea4 | -1.46208 | -53.41764 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a221ddb-0ab9-3d2d-bb21-d955fa3b8ef5 | -0.51879 | -58.10147 | 2024-11-08 05:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d6eaf72-c46c-3f79-83f6-93874e834ea8 | -1.45544 | -53.42126 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aea7a2f-8908-3c15-936d-bdcb6b94f197 | -1.43268 | -55.69872 | 2024-11-08 05:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d532c54-4931-3581-b0a8-7d2b35e81106 | -1.46142 | -53.422 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7aa8e661-68d5-37e0-8daf-5ce036374b91 | -0.64535 | -52.38687 | 2024-11-08 05:37:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7da36091-6614-320b-b782-85510cb92405 | 2.51959 | -50.93772 | 2024-11-08 05:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 23c1ebb3-1f39-3e53-b933-330ff682afa5 | -1.24968 | -53.38701 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ced5d33a-8c34-3b42-bd23-48e7f3fd6b5a | -1.2295 | -55.81017 | 2024-11-08 05:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a68d85cd-dfa1-3e93-aa67-a039063eafcb | 0.74462 | -59.77638 | 2024-11-08 05:37:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fec3d132-a585-39af-a4a1-4f45df3d7a3d | -1.45267 | -53.41724 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 629afc0f-4782-3323-8dc5-caab7ea55a93 | -0.89944 | -51.76765 | 2024-11-08 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42f1f4af-e9aa-3919-8a42-6bd5004b51a4 | -1.34199 | -54.62738 | 2024-11-08 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab5b72f3-9ac8-3ba7-b059-19b3cf9bcf7b | -1.45865 | -53.41798 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 831dcf12-6bba-3074-b1d1-071d04da77ab | 2.5271 | -50.94223 | 2024-11-08 05:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3708f6d-a601-3eca-9e42-913b87066a8c | -1.13776 | -53.71855 | 2024-11-08 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fedc3134-4b1d-32bf-82db-289acf8fcff0 | -1.32604 | -54.18714 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abe1c2f1-1c45-33de-977c-d3b60a0e2123 | -1.24726 | -53.38576 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f8440a4-8304-3733-9e80-b03d082679c1 | 1.52458 | -56.06779 | 2024-11-08 05:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fbaf1042-b219-3bb0-92fe-dc20215b1610 | -1.10355 | -54.20223 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecf9cb45-2e61-3fe9-95ab-bc68dcbb4a3a | -1.33379 | -54.60768 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81484f1d-592a-3fc3-81a4-986934ba4719 | -1.25458 | -53.35594 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddf6dde9-c255-36f7-aef4-2c2497f67304 | -1.51039 | -52.07259 | 2024-11-08 05:37:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81d8b1af-2eaa-38ca-b7c7-f52782a4c287 | -0.64735 | -52.3928 | 2024-11-08 05:37:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61eaaaa1-4803-3fa1-9b5d-48a22646a26e | -1.25194 | -53.3546 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57f92072-190b-3a70-a43f-9752147966fc | -1.14813 | -52.00735 | 2024-11-08 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 985b1663-1df8-3a6b-b06a-f4642488911f | -1.17091 | -54.16196 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c591808f-b3b0-3540-9fc6-bfdfd5620b28 | -1.14906 | -52.0008 | 2024-11-08 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fc35d7f-4060-3164-95ab-f0d79a2f0456 | -1.33491 | -54.60041 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b42202b-ca0c-3c4c-93cc-d1f7c8594cbc | -1.14822 | -52.00613 | 2024-11-08 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4bba095-64e8-3f8c-bff2-595090427790 | -1.11404 | -53.17995 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c24c7eef-33e5-3042-b9fa-b72cffedcca4 | -1.33648 | -54.62671 | 2024-11-08 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f6c2973-9fa6-3d24-a296-79bc1944e1fe | -2.82 | -52.9409 | 2024-11-08 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 5fea4c3d-d230-3502-8926-f97c8628245b | -2.82 | -52.9613 | 2024-11-08 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4ed63e18-5343-3696-a3f1-13d7cb6eeac2 | -3.068 | -50.5631 | 2024-11-08 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| d0be60be-ff68-329b-9038-2384e0fc2ee2 | -4.6835 | -46.4074 | 2024-11-08 05:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 66106e74-644e-3941-a72f-1d6f1949b626 | -3.5446 | -47.3855 | 2024-11-08 05:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| aec9d7bb-fc10-37d8-81ae-2b3f66c825d9 | -2.8016 | -52.9414 | 2024-11-08 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| d0808c13-4d01-3aea-b54b-2a5f6f301c50 | -4.5209 | -45.6804 | 2024-11-08 05:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 64f35660-b0be-3972-a2f5-c4deadf2a4e0 | -2.8016 | -52.9617 | 2024-11-08 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 5ac309d8-3834-332c-9fc5-07657104253a | -3.5631 | -47.3847 | 2024-11-08 05:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f5d24a78-ed6a-34e0-8572-4905e1049919 | -3.9669 | -48.1716 | 2024-11-08 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 11f7c351-131d-35a2-96b9-8cc2a4349230 | -2.80877 | -52.96994 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 692698b4-f2d6-3c4e-aee0-280403ceeef8 | -2.82126 | -52.97185 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20638427-203a-3d0f-951c-fa7c69214799 | -3.02015 | -53.86887 | 2024-11-08 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5101ccd5-30c6-31cc-bcaf-336e21784d80 | -2.82472 | -52.90735 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 261af441-6abb-3ee1-871a-fa982535645e | -3.0087 | -53.43231 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bad6580a-ee7d-3cfe-9480-02c0175f678b | -2.76387 | -53.22265 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25205cb3-92f2-3c44-a8c9-76d17b20704c | -3.15614 | -54.47856 | 2024-11-08 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1384b7f-00a0-3d28-a707-44a98d4e48aa | -2.81716 | -52.95685 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a79b0ba-cfa5-3c51-baf4-1047ba006580 | -0.7826 | -62.90865 | 2024-11-08 05:40:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6759776b-ea36-36e7-b4a7-028830c5c82d | -2.81789 | -52.95209 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aedafd50-bcb6-3713-9e09-e4c29d597c62 | -2.60988 | -51.30532 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2777ad98-5594-3030-b156-7df33f56759b | -2.79998 | -52.94366 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2d018669-911f-3d2e-adbc-f83b5fdbdbea | -2.81396 | -52.93589 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be67762b-05f6-3bc4-9b9d-4e54be7c6fcc | -3.03428 | -51.52992 | 2024-11-08 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e03a870f-dcf3-392a-8265-e0fda378cbdb | -2.79375 | -52.9426 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 673500f6-b31e-3111-a5ac-f2a181157d81 | -2.62147 | -51.74755 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c36642b-a242-304c-b27c-3f001552e244 | -2.82173 | -52.95542 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0d8b841-709c-310f-a598-0e064c671964 | -2.81544 | -52.95469 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f34113b-7ad2-3f29-bb7c-24b950d50858 | -2.82418 | -52.9528 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c17dcc39-772c-34b4-a8a8-c4357d2c76d1 | -2.61475 | -51.74656 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8d1123a9-db27-3de8-8d86-d4557956a085 | -2.62057 | -51.75354 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f0adb638-ec7b-3fb0-a298-7a5a0e833dff | -3.28074 | -61.50801 | 2024-11-08 05:40:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3f949f9-0634-3db9-a0bd-37bb751fa3a6 | -2.81689 | -52.94472 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 906e2342-47d7-3791-aaa6-64403f73437e | -3.03527 | -51.5317 | 2024-11-08 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 99c3243d-984b-304d-9868-abbe8f2481f2 | -3.08815 | -51.11629 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8766b90-0334-335c-9bfc-5115366bb6c0 | -3.00739 | -53.44114 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c63853b-a11b-3b3e-96ae-575fe1e5d03b | -3.01951 | -53.87324 | 2024-11-08 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04de92da-9fd9-3bd5-b063-c46652156201 | -2.82052 | -52.91972 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d996c09-881d-34dd-8c0b-ae947b6370cc | -2.6177 | -51.29997 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60878a8a-3f4c-3454-962d-92c64c2d5414 | -3.74832 | -52.10476 | 2024-11-08 05:40:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee6eaf0f-82f1-3d58-b9d8-c8fa47908772 | -2.81574 | -52.96618 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f3eb113a-e34c-32e8-9f15-9743396173f5 | -3.03244 | -51.54207 | 2024-11-08 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 93e284fb-9d32-3139-8cb7-6358d2ace44a | -3.08889 | -51.12173 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed4306c1-8abb-3442-a20f-191e6afa2e44 | -2.79675 | -52.95135 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f069818c-93ca-379f-b618-087437c91ec7 | -2.80543 | -52.94994 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| abab2e31-8a86-36d5-a8a7-16eb6f25edae | -6.48146 | -60.07132 | 2024-11-08 05:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35246f2d-3c95-3c79-852d-ed37d2e3d737 | -2.81018 | -52.96071 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00bb6ae8-1aa6-3b3d-a063-4b3f14aa3156 | -2.80994 | -52.94854 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bd3d410e-7fa7-3e77-a094-dd151124d6ee | -3.08988 | -51.11516 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27eb316d-2a63-3574-ab10-05539c85ad58 | -2.81645 | -52.96148 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README37.md)
