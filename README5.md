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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de8a4c58-7d5b-369f-85c0-dc9ca2b542ac | -2.9233 | -49.3409 | 2024-11-05 00:20:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62e6246b-23ae-3359-95a7-033a1beef1f3 | -5.3701 | -46.429401 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e88e7520-6110-363a-a804-7b412ab6aa80 | -5.2987 | -46.2505 | 2024-11-05 00:20:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45215340-b1ec-3abc-80b3-aa7e9e24bb9c | -3.8854 | -46.609501 | 2024-11-05 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46c6ad99-9eed-3720-b3f4-ed3288a81a69 | -3.0112 | -45.8442 | 2024-11-05 00:20:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c2ce614-f09a-37df-b79f-72df44bc0e95 | -10.773 | -45.2533 | 2024-11-05 00:20:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 38f3b53e-9f7b-3a6f-a662-55fa57a49881 | -4.0372 | -48.291401 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3d7ad4c-73a5-39c2-afca-5c0e7274c701 | -4.4056 | -43.113201 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b3c30cc-7490-3793-8a4f-69ce7f75caeb | -0.0381 | -50.748798 | 2024-11-05 00:20:00 | METOP-B | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb262dba-a514-304d-b44f-41b10f8ba34b | -8.3834 | -43.816601 | 2024-11-05 00:20:00 | METOP-B | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83da07d5-9a29-3fa5-ba8c-da06d3be5121 | 3.5048 | -51.252998 | 2024-11-05 00:20:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c5271487-3a41-3143-b6be-0a388ee048e0 | -4.0099 | -43.630901 | 2024-11-05 00:20:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41e09dd6-702f-3e8f-924c-a19e12032391 | -3.1863 | -50.565601 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fafc613-8902-3c77-8d2a-037858298eb7 | -3.2752 | -44.425201 | 2024-11-05 00:20:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 356b3046-f82a-3485-9d64-b33450bdf337 | -4.0827 | -48.310799 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e6b4af-e03f-338c-a54d-8984450acef3 | -4.908 | -44.354198 | 2024-11-05 00:20:00 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a2df100-6a48-3836-8b5d-4bba05a006a1 | -4.0495 | -46.925098 | 2024-11-05 00:20:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b72b3093-819b-3541-8383-3e6999c2f807 | -3.1882 | -50.573898 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf6f214-0d6b-38f4-8b8b-89c0e5f35795 | -10.0179 | -44.8307 | 2024-11-05 00:20:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b392d25-735d-390c-a2c7-6ee1f541e940 | -6.1188 | -43.970501 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3bc4ab0-3beb-3e97-8edc-9203cad8c3fa | -2.0868 | -46.4949 | 2024-11-05 00:20:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fae94dff-7620-3536-8a1d-b103b9ebea91 | -5.3098 | -43.324402 | 2024-11-05 00:20:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 992b2a34-ee1c-3a34-8c49-3fd417cece82 | -3.4823 | -50.370998 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7181131-eea9-344f-ba4b-55e0381dca40 | -5.6338 | -46.959801 | 2024-11-05 00:20:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2d2ad8b-dae8-3849-83fc-facdae2dff01 | -3.4539 | -47.666199 | 2024-11-05 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c23a4efd-89cc-3a42-af35-b052a29d80ef | -5.0664 | -44.235901 | 2024-11-05 00:20:00 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68b6d331-5805-3508-ab33-7c2d63c1534e | -2.0884 | -46.501801 | 2024-11-05 00:20:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e33c31f-bf7f-3c2e-b321-8477f2ec06fd | -2.2403 | -46.672199 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67360632-1c46-384c-81dd-2b431f526085 | -4.3665 | -47.234402 | 2024-11-05 00:20:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb913426-30d7-3904-813a-480df92f70fd | -5.9277 | -43.633701 | 2024-11-05 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02758ed6-8c22-367a-a0e3-35ddf14ab8cb | -2.8448 | -51.340199 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2f6cffa-75b8-3e3d-a2f4-e753cdd55ef9 | -5.8279 | -43.647999 | 2024-11-05 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea48dd01-7644-3c42-9703-0abd808eea75 | -6.2489 | -43.551201 | 2024-11-05 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69e12f79-b498-3866-95b7-9fba80772a2c | -4.2378 | -44.939301 | 2024-11-05 00:20:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c67325f-65c9-356b-83ef-10600a811ff0 | -3.5556 | -47.3857 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fef1437-b34f-3c60-8a8a-ae5f1301a5a8 | -5.0032 | -44.4547 | 2024-11-05 00:20:00 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8472b466-9658-37d5-906d-723d333e2688 | -5.0563 | -44.1469 | 2024-11-05 00:20:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11548821-16d8-34b3-8ef3-0a45f13ed0c8 | -5.6861 | -45.821701 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7740964-3cdb-3440-a09c-fabeab6be8a0 | -2.8145 | -51.4809 | 2024-11-05 00:20:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c93fbd9-c383-3197-b4b7-a7c7d57ceabb | -10.7698 | -45.239399 | 2024-11-05 00:20:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48b939ce-0936-34b2-924f-864ad34828ae | -6.1072 | -43.964901 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4fc84375-93e0-3017-a29c-73a45eb6ef3f | -4.2344 | -44.9244 | 2024-11-05 00:20:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4a736d0-b0f9-3e5e-accb-2dbc886c5fd5 | -10.3704 | -45.067001 | 2024-11-05 00:20:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51de91ef-fd31-3244-a552-d609828ccb63 | -6.0939 | -43.951401 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0a5356a-156d-3d62-a45e-bd985fffe471 | -2.2632 | -46.819199 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d1701e2-0364-3ed1-90c2-c83de8645dc3 | -4.2454 | -48.025799 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ad26679-b2b0-3944-b0a4-a282890fd5f4 | -2.7784 | -51.595798 | 2024-11-05 00:20:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79204501-10cd-3c7d-ad2d-d102740cd96e | -5.4858 | -47.172501 | 2024-11-05 00:20:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56a4e033-5113-3347-a099-142c27f55a0a | -4.5016 | -45.644798 | 2024-11-05 00:20:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81774e78-1833-37f9-8468-2565cebddfba | -4.5 | -45.637699 | 2024-11-05 00:20:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 796b5d29-bb7b-36aa-adb9-d1b2e75359af | -4.1264 | -46.900799 | 2024-11-05 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02e208e9-c99c-3380-8b14-d572166f0fcc | -5.6809 | -46.482399 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62a7dc6b-870a-34f3-9c05-fede39fc31dd | -4.4153 | -43.110901 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a62137d8-051c-3827-abcd-79226a64120c | -8.2599 | -44.853298 | 2024-11-05 00:20:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8cd667be-9a51-3c42-864c-0b1a1447d39e | -4.7601 | -44.428699 | 2024-11-05 00:20:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc4a904-457a-343b-aa3a-5fb3a7f92014 | -4.7555 | -44.5434 | 2024-11-05 00:20:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22f08110-8c0d-3d9a-9037-af92bdc4bd6f | -6.298 | -42.036301 | 2024-11-05 00:20:00 | METOP-B | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8e890eee-1e4b-3717-9636-b06fd3e1b475 | -4.2108 | -44.280602 | 2024-11-05 00:20:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3536e32b-69b5-3129-9fff-7225304ee999 | -6.2957 | -42.026402 | 2024-11-05 00:20:00 | METOP-B | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 90846f09-da46-393e-a9af-ca18b5d81ebd | -3.5541 | -47.378799 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27645e8a-1bb5-34b0-aac7-c40fcefd78a7 | -14.348 | -43.279999 | 2024-11-05 00:20:00 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d298e5b5-730f-3712-a86e-613051ba3e59 | -10.8074 | -44.492401 | 2024-11-05 00:20:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37e592d6-1447-3616-86e9-8ffb6133fa66 | -6.4389 | -42.065701 | 2024-11-05 00:20:00 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 84ecef1a-f8e4-3216-9362-c8e23b24aad7 | -3.5654 | -47.383499 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c15c8e93-230b-3fa5-8b59-f3a4524c7320 | -5.5108 | -41.6675 | 2024-11-05 00:20:00 | METOP-B | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 813a04e5-e7c7-33be-aa3a-7bd5c4e4dcf5 | -12.1655 | -44.617001 | 2024-11-05 00:20:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09cc3a85-5a66-3f61-bcb7-78580841a43b | -3.9662 | -48.3881 | 2024-11-05 00:20:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3110e7d-f2ab-37ad-b4d3-2376d8b6dfab | -7.1951 | -43.139599 | 2024-11-05 00:20:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c620670a-464a-3838-8d2e-1bb3d5cfba1f | -3.778 | -46.044201 | 2024-11-05 00:20:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80d510ed-aaf4-34ad-89df-33bfcab3a531 | -11.1332 | -43.302399 | 2024-11-05 00:20:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ab656cd9-d590-3845-94d5-d2f1ff22b023 | -5.2196 | -46.721901 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e7db1ad1-1a4a-3de5-a9c0-fb78703b4e42 | 3.5065 | -51.2453 | 2024-11-05 00:20:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 96a9098b-4dd1-34c2-923a-49d0b3f06d2e | -2.8047 | -51.483002 | 2024-11-05 00:20:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b5bd101-cf78-3deb-8d8e-5df4db2033f7 | -11.8634 | -43.875801 | 2024-11-05 00:20:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9697d98-c87b-3c7e-9149-92393f2d4a03 | -2.8575 | -45.6213 | 2024-11-05 00:20:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 042518c8-1471-3a1c-a748-a61b5373243b | -2.2419 | -46.6791 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3a139af-4126-3752-ab72-a1f00a7ee0da | -12.1639 | -44.609901 | 2024-11-05 00:20:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c1232df-ac60-3d98-a77a-e9498c0441f0 | -1.6087 | -47.252201 | 2024-11-05 00:20:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffee9896-9c39-390f-a401-d514ea160bec | -4.233 | -48.522202 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc126d3-bcf5-3df7-838e-066a881edec2 | 0.2002 | -51.060699 | 2024-11-05 00:20:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0e7059d4-058a-353e-b5eb-e702398641c1 | -5.5083 | -41.656799 | 2024-11-05 00:20:00 | METOP-B | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88f0b0e0-0eb9-3ab3-9e0e-200da332476a | -5.6354 | -46.966702 | 2024-11-05 00:20:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad3a849c-1007-342e-8674-7bed0cc46275 | -10.6722 | -45.034599 | 2024-11-05 00:20:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa8cc317-579e-3ebf-b649-4b6019736b45 | -5.3763 | -46.456799 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40aa561e-929e-302a-ab91-f67b236adcf6 | -2.273 | -46.817001 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 286b1bf7-6cbc-3ee2-a412-186ec00e7189 | -11.1314 | -43.294701 | 2024-11-05 00:20:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 362dfee4-9d1f-3c91-bb96-e0ad98219417 | -4.6157 | -48.900002 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11728982-bef0-3ec1-9416-c3a1813f5a09 | -2.2941 | -46.499901 | 2024-11-05 00:20:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b839c35-e3dc-3d2c-a1a6-3752b0a389c1 | -11.8617 | -43.8685 | 2024-11-05 00:20:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c87c836c-0a67-325d-9da5-080d73a4b8ca | -4.6595 | -43.811298 | 2024-11-05 00:20:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 828c9901-6845-3202-bd8c-a429dd031db7 | -8.4975 | -42.091801 | 2024-11-05 00:20:00 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c19f547-530d-3748-a18a-a03122b17ffd | -3.5458 | -47.387901 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b181800c-a678-3c42-9d1a-84deb41e39b5 | -4.3748 | -47.225399 | 2024-11-05 00:20:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0e0659f-9f05-3c0d-a45c-24043fb7b2f7 | -2.2434 | -46.686001 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 589d4ddb-8bbe-3d37-b26b-68b010a9636b | -4.3937 | -43.1063 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96913a5b-3550-34aa-a73b-0963c84fbea4 | -5.1137 | -43.9487 | 2024-11-05 00:20:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a26e4a5c-27f0-316c-9e58-f03b945ccce3 | -3.9568 | -48.345901 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e257ad0c-b4c2-3581-ae0b-3c4f91cdb391 | -6.0668 | -47.007301 | 2024-11-05 00:20:00 | METOP-B | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd84fed-473c-39ae-9cea-5eca629c45da | -5.3117 | -43.0658 | 2024-11-05 00:20:00 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d638490-ac2a-3b72-925c-5711415f1f6b | -5.699 | -45.833401 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
