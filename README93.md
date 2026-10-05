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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e61b0f6-84f9-3d00-b179-6dc2ee29ff7d | -3.37421 | -58.18957 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 52c5cba8-df98-3a5a-a86e-89b6da635970 | -2.92992 | -54.13134 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 5b997f14-3ed1-3d8b-8263-d6fbe603c59d | -2.76364 | -57.64786 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 57b1a2ee-3fad-3478-a312-c24761b881b2 | -2.99156 | -57.89794 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3fd4fbf0-561d-38f9-923d-772ce7c2604d | -3.1088 | -57.65609 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0b0fa1b9-1ea9-388b-8506-0c9716c68385 | -3.32378 | -59.48048 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0a5d0584-ca37-3888-838d-82754c5c5e98 | -1.86603 | -50.60145 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 15b90d39-9e98-34dc-9dd1-a675f154dfbc | -2.56969 | -57.98084 | 2026-10-05 16:39:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41666b3e-3e2a-351a-8d18-f2c09032703d | -1.42971 | -52.72933 | 2026-10-05 16:39:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5993868b-f4fd-3590-b941-c5cfc99836f1 | -3.74533 | -39.53651 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 57d66bbd-e1f5-34d8-aad6-a13ce1a71810 | -3.43527 | -44.44415 | 2026-10-05 16:39:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c20f98ad-16dd-36e4-b79f-1bad6c2ef952 | -1.82466 | -47.1437 | 2026-10-05 16:39:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a91bd1f6-0a36-3579-97f4-f1429279f49c | -4.99467 | -42.72948 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4dc8845-0912-35cd-9be3-e67cfdeb9f1a | -5.99984 | -53.62845 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 10841890-d267-3db7-b239-7f2883f8bdc5 | -1.19246 | -49.25642 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a69f4b37-18ea-3884-90a6-de429d2d0669 | -5.84244 | -45.0121 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| fcab6515-ac2c-33d6-bdaf-c41c123d4318 | -3.28905 | -59.41431 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2d9ddd17-f1fa-3039-887a-b4b42a3e88d3 | -5.55279 | -45.26527 | 2026-10-05 16:39:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8e7eaac6-0464-3948-a7a8-4c85317688ed | -1.26302 | -54.5585 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 69651403-9ffe-341a-95aa-ad7aee634ff1 | -3.0775 | -49.543 | 2026-10-05 16:39:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a3f9e5af-861d-3703-be50-7e19d004b458 | -3.88438 | -55.80073 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6b5ae096-7f27-3796-a20f-068b3e3d156c | -4.0701 | -55.76586 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 549a50b6-d63f-3c8c-aa7d-2ec8c7423f9c | -3.18261 | -60.05103 | 2026-10-05 16:39:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a0f1d316-e846-39d6-bbf6-11b20efd612a | -2.85263 | -51.30288 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1396ad51-a296-32d3-a416-1998448e0cd0 | -7.22927 | -55.18558 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| f5e29464-bb28-396c-b879-c81a98530d50 | -2.95413 | -54.14817 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 31e57c9e-3cd7-3e69-aa8c-59ee1c09d762 | -1.72704 | -54.97129 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ad55706e-ef55-3450-8c18-51a5bbafb69f | -3.08679 | -54.17023 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9d8e2f06-ea6e-3020-8d9d-9ca70e1e34cd | -1.18479 | -49.25051 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 81b33f16-5454-341f-a429-390de44195f1 | -2.95838 | -54.14763 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3aac8807-4445-3e19-ac27-bdf811e82d96 | -3.03623 | -57.42059 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9b1aa9fd-4c3a-30f9-bf7f-542f87a252af | -6.08417 | -47.65442 | 2026-10-05 16:39:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 042db1c9-c1db-30dd-bbad-f9ec4ca77d41 | -3.0999 | -53.73555 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 4c8eed71-3c76-310c-86d1-267df31bb6a1 | -1.63194 | -55.53029 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2fc392be-cc6b-3c17-93c8-ac469bb965bd | -5.48088 | -39.55946 | 2026-10-05 16:39:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 39.9 |
| 5acafeb0-6016-30ba-bced-6050af73c784 | -0.17643 | -51.32322 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9146096-0012-3c03-add9-4e824f020347 | -2.01993 | -56.43236 | 2026-10-05 16:39:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4857cbb5-fd12-355e-b06d-c2939153d3de | -5.40555 | -39.10456 | 2026-10-05 16:39:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 50a243ba-0a3d-3f6d-9395-7b5e49a78ef6 | -3.16895 | -43.05779 | 2026-10-05 16:39:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b62a63a8-5ee5-34e4-883d-5e314b43c307 | -7.22441 | -55.18633 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| e769c066-5ce5-3a85-a6d6-9bbb88ed3e3c | -3.11341 | -44.29396 | 2026-10-05 16:39:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 520c68f3-99aa-33f2-913f-0e5f600065fe | -3.09282 | -51.09653 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3309158-663d-34c5-94f2-cf2c9fef7a8c | -3.37645 | -42.51132 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0ffb0c8e-7c4a-3bf5-9524-9ac51c7a7a97 | -1.63727 | -55.53456 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7e2bce8e-6738-3200-b4ee-e87c79dca340 | -5.26657 | -47.91033 | 2026-10-05 16:39:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09f8cd9d-aad6-33f5-8655-e574d10454a5 | -1.31159 | -54.22203 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2e3380e-9e3f-373e-a6a8-12d310e85ede | -6.18695 | -55.35008 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 402d4350-c445-3518-9083-6cf7724da35d | -1.8756 | -50.04045 | 2026-10-05 16:39:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 22832ef6-567f-31d0-a318-8a5ad8f0978c | -2.90273 | -54.12311 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 03de696b-188b-3398-a9d4-e44450e4b808 | -1.18915 | -49.25691 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e84a9cb3-8bd8-3ff2-afcd-39f7174b012a | -3.40946 | -58.462 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4acbd7dc-478b-3e05-8909-ad3fca9f0818 | -3.61803 | -44.41912 | 2026-10-05 16:39:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a6325862-c863-3722-9753-90b29a05c480 | -4.57039 | -39.59081 | 2026-10-05 16:39:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 4ec8f1ed-6557-316f-bc47-0d5c96919b3a | -2.0435 | -48.34953 | 2026-10-05 16:39:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c91409f-6218-321d-a195-26443a4382cc | -2.96107 | -42.90269 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 7af1f3a4-36cf-3708-b94c-4d1ccd630f74 | -5.87622 | -42.42465 | 2026-10-05 16:39:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d145fff3-d527-3b7e-a8ca-49f5f35c4c19 | -2.87427 | -40.12349 | 2026-10-05 16:39:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 540ed4e0-edb0-34b7-a27d-24bdbf525a2b | -3.34167 | -44.58954 | 2026-10-05 16:39:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f18e10c4-1f59-331f-97fb-cf3fe7460cbc | -3.75246 | -61.01852 | 2026-10-05 16:39:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 24f540d1-61a3-37eb-b8e7-d64d769872d9 | -3.25443 | -57.88138 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0fe7fbe8-b288-325f-ad40-285036c9e2be | -4.05948 | -44.74692 | 2026-10-05 16:39:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| add91b93-3d3b-3048-ba37-53cd4cf57b40 | -6.07861 | -47.66233 | 2026-10-05 16:39:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bd933c8-6756-3ce7-a0d4-b95d80ded1f6 | -3.05145 | -54.22004 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 14d8e090-a197-3cd5-821c-700ef1d87264 | -3.9378 | -40.7222 | 2026-10-05 16:39:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 20.9 |
| a78faccf-5fd6-399a-813b-6e662b6f112d | -3.11251 | -53.70713 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 93bc1380-2908-37fe-90ac-7aa4a8a99052 | -3.37812 | -58.19141 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1bb9d353-cb64-3c50-ad5d-90a318bb9c29 | -2.46 | -49.39014 | 2026-10-05 16:39:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 21366c27-280e-3253-b834-0be232b5dcf9 | -3.37592 | -58.20084 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 178.6 |
| 05ed8f41-35be-3787-a4c9-e8a22173124a | -4.94245 | -42.71587 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 31.7 |
| db0accca-b104-3825-ae81-5b29faa04a2e | -6.33506 | -55.32275 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 56c2b717-0cad-309c-903d-612ff2b39be2 | -2.90599 | -54.08675 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b50b7bb4-20bc-3df0-a221-4b774c344d39 | -3.30219 | -43.94355 | 2026-10-05 16:39:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 253a96d0-5a93-3062-8068-af70c229d7ca | -2.04458 | -54.48536 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3efb790e-48cd-3b76-a468-a2122561f8af | -3.87987 | -45.77497 | 2026-10-05 16:39:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7f671167-80a1-3c2b-a739-956e3c246a00 | -3.31596 | -44.2254 | 2026-10-05 16:39:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e339c06-03f3-36ec-80ed-7ce7baf5ccb0 | -4.86304 | -38.98682 | 2026-10-05 16:39:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| e8efd7af-64ee-384a-b7c9-0547d8798786 | -3.10046 | -53.73928 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 520751a1-8025-3999-9b23-63defbf9da68 | -2.99831 | -57.78703 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 49342f4d-bdbb-3222-b408-291fcf56bc92 | -1.09539 | -54.11407 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 451.1 |
| 70015416-2229-3fd6-ae60-ff948980917b | -1.21696 | -54.54119 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 25051188-958a-3691-8028-f11541c6c9ec | -3.15684 | -50.44333 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 121f60bb-2b72-31a7-9552-0a6681b57dd3 | -3.38141 | -42.59446 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a978d2ce-91b8-3339-a87d-d3177f219a6e | -3.3176 | -43.94114 | 2026-10-05 16:39:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6624ff69-dd9d-34ca-b6b6-ac6706e62297 | -3.12973 | -53.71911 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f3f0f621-0894-3a41-8e97-7ccf0d158cd9 | -1.27981 | -48.84929 | 2026-10-05 16:39:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9304792-a6ce-3a61-a00b-d0f95548f4b9 | -2.95633 | -42.89959 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 71accf1e-d548-36cb-ab0b-972e950f6fb3 | -2.90697 | -54.1225 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1aa9415f-4e50-30e3-b98c-8e1639b3d2b4 | -3.35876 | -43.387 | 2026-10-05 16:39:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a2ff4960-5ce1-3161-8001-360a4846dfc6 | -3.208 | -42.87831 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| aa6aa006-fb39-3371-b6b7-c3cce0ae6559 | -3.19668 | -57.08729 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 515bf113-3754-36c8-a6a5-356ec5cb9afa | -1.62985 | -53.65306 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fc5e2d79-a834-3424-859d-e646827e5e75 | -4.79985 | -42.13935 | 2026-10-05 16:39:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 9f4c238a-a4ae-3df2-b83f-3ff3eada855a | -2.34292 | -57.11826 | 2026-10-05 16:39:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 026f39ae-c511-344a-862e-3b55ef7f99f1 | -5.83123 | -45.00977 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6fbaedb1-a13a-3176-941f-5e5b4cfeaae8 | -4.14322 | -44.99512 | 2026-10-05 16:39:00 | NOAA-21 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c539c8ab-625e-300e-8c5e-b8558a13aaa2 | -6.40683 | -44.48335 | 2026-10-05 16:39:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f111bc07-3c7d-3206-b1c3-e716ee856607 | -2.07012 | -56.85882 | 2026-10-05 16:39:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c1b76c7-534f-30ee-a9a3-20f77f89ca6c | -2.96204 | -54.14314 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| ffbdce9a-b9c4-3b88-bfda-420f50b05b82 | -1.93195 | -56.75976 | 2026-10-05 16:39:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ac3b808c-af1e-3f59-bc76-3e27f1a5cd00 | -5.60888 | -42.92891 | 2026-10-05 16:39:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |


[Clique aqui para ver as próximas entradas](README94.md)
