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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b6542e6-be85-37e0-b146-2e1a9eeac5c9 | -2.73841 | -46.7928 | 2024-10-06 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 66b2ebc2-13b7-3b26-aeb7-a79624688416 | -2.73665 | -48.68825 | 2024-10-06 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 80d2acc6-6381-30c0-b8f5-7fef22901f00 | -2.73156 | -46.80906 | 2024-10-06 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3b1af2df-a4f2-3852-8583-f1c5114b4573 | -2.72253 | -46.81039 | 2024-10-06 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f956b0ef-8d50-3246-8ea6-703ca28d9609 | -2.69763 | -49.07325 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 263.0 |
| cd4a64a0-753f-3aad-98ac-b199a14a5e48 | -2.69639 | -49.06424 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 312.6 |
| 7b4f7ad2-5b57-3234-98b4-7b0c997fce1d | -2.6887 | -49.07451 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 236.4 |
| 1087a29f-d7a4-39b2-9137-3d1eaf072b91 | -2.68746 | -49.0655 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 300.4 |
| 834cd639-b010-3453-88a9-d962c8dd47ee | -2.56832 | -49.076 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 623fccc5-f6da-30d1-a32d-ac6baf325228 | -2.53408 | -49.02592 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 48d606e5-0209-3ad7-9a81-b742d7e9a8e7 | -2.53283 | -49.01696 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 66debccc-5eeb-3aa4-9c60-7b7218cbef50 | -2.40964 | -48.85814 | 2024-10-06 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9daa3970-9280-32bf-ac1a-9ba6ce93666e | -2.37892 | -48.63678 | 2024-10-06 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f89fa290-ef49-3b47-ab22-50f4051a1d1e | -2.37007 | -48.63802 | 2024-10-06 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c8984eb-a093-3993-81dd-c8b76c39fea0 | -2.23475 | -46.74986 | 2024-10-06 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 382866e7-a1e1-3d7d-9f80-2a3d5833d031 | -2.23344 | -46.74053 | 2024-10-06 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 74bb9fd2-5899-373f-b9c3-ea7ee3c015cb | -2.23214 | -46.73118 | 2024-10-06 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0f6b6851-8a95-3a3d-8564-8a43f3ff881b | -2.20316 | -48.16592 | 2024-10-06 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0a59bc8a-33f3-3c03-990f-50839e86587d | -2.20193 | -48.15714 | 2024-10-06 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c2ea6b38-2c18-30ab-bbd9-d9465a49b325 | -2.05796 | -48.512 | 2024-10-06 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 71b58b00-2e94-34d9-b1f8-3756e11f1126 | -1.84126 | -47.09987 | 2024-10-06 00:54:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7610a039-5fae-346b-8fa7-eb99bde97526 | -1.82954 | -50.97343 | 2024-10-06 00:54:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cdae83e5-ece1-350a-88c2-28b76e720444 | -1.77084 | -47.19062 | 2024-10-06 00:54:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5757ec3b-71c8-342d-9dbd-e8ad64fc542f | -1.76313 | -47.20099 | 2024-10-06 00:54:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b73f1568-64d9-3cff-933a-147afba1666f | -1.76186 | -47.19189 | 2024-10-06 00:54:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4ebb2f0a-7c5f-378d-90df-12050f37147c | -1.74891 | -54.00583 | 2024-10-06 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| d94b6142-61ae-3837-b094-4d9d8ed13435 | -1.55546 | -54.78657 | 2024-10-06 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bdf027b7-f2fd-3b37-adb3-f6d287befe24 | -1.55339 | -54.77304 | 2024-10-06 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 1d3cc10d-a83b-39b4-93a3-57c37a0fa955 | -1.55277 | -54.76678 | 2024-10-06 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| f37d1872-9838-3f5d-b87c-c29df92a27b4 | -1.4643 | -54.97509 | 2024-10-06 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 31bbc543-6d4a-32d7-ae14-509a7e5cabf1 | -1.46203 | -54.97004 | 2024-10-06 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 0433a8f6-7cbd-31ff-a113-86a47242b50e | -1.14399 | -48.84194 | 2024-10-06 00:54:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57802e18-410a-3d4c-a24a-49161a065138 | -1.04116 | -48.70142 | 2024-10-06 00:54:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c2aac035-9106-3e15-90af-400d5d0a010a | -4.43548 | -42.88861 | 2024-10-06 00:54:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| aca7b174-3055-32c8-843d-482cfc783089 | -4.13262 | -43.81771 | 2024-10-06 00:54:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 825daf1a-ccf4-3c0a-949b-8d2f2aaea97b | -4.13077 | -43.80482 | 2024-10-06 00:54:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 8cfcd6d2-10d2-3965-8cff-baf483a010a5 | -4.05055 | -43.2463 | 2024-10-06 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 6556e402-835a-32fe-9025-3dea13c32744 | -4.01734 | -43.25134 | 2024-10-06 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 611082c1-63d3-3167-a420-f220786e7bd7 | -4.01523 | -43.23698 | 2024-10-06 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 269e321a-1b12-3abf-a626-f642a0cd9cb4 | -4.00626 | -43.25298 | 2024-10-06 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 788acc20-eecc-33db-8edc-70236c173fdd | -3.9973 | -43.26883 | 2024-10-06 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d60a0a1e-19f4-3103-983b-df29ac35bbc8 | -3.99519 | -43.25462 | 2024-10-06 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 895514d8-fbda-3c8c-bf3d-bad93bf58d17 | -3.80025 | -41.60889 | 2024-10-06 00:54:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 160.4 |
| 6cfe6945-f2c5-3a5b-b578-241f04529201 | -3.79741 | -41.5896 | 2024-10-06 00:54:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 263.1 |
| d731c9f9-0bb2-3cd4-b628-f74289a75055 | -3.71974 | -41.68637 | 2024-10-06 00:54:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 13271442-fe0d-3e0b-90f7-acc3160a80e9 | -3.71692 | -41.66716 | 2024-10-06 00:54:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 58c2e353-7401-3dcf-9664-4a01ebd9a670 | -3.7071 | -41.68828 | 2024-10-06 00:54:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 50.7 |
| ccac1651-40f8-30fc-b67e-8acf4cfc367c | -5.82501 | -44.13408 | 2024-10-06 00:54:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 16231c6b-a37c-3943-a1ff-f86687ec6441 | -5.82331 | -44.12234 | 2024-10-06 00:54:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ddfad5fb-9865-3a1d-89c7-fc5c7da957c5 | -5.81663 | -44.14716 | 2024-10-06 00:54:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 62234daa-7981-3210-8b2c-068ccf58389a | -5.81494 | -44.13556 | 2024-10-06 00:54:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 189.3 |
| c45fe972-21c3-3cff-995e-81ccf81cf441 | -5.71024 | -47.1513 | 2024-10-06 00:54:00 | TERRA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c42cb35b-fc3e-3099-9767-298c8928170f | -5.58458 | -44.88618 | 2024-10-06 00:54:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8fd6722d-f8dc-3bcf-af82-f38a2f8dd3db | -5.58308 | -44.87567 | 2024-10-06 00:54:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| af76aa1a-b577-3c7e-b14b-11664198fcb7 | -5.57496 | -44.88763 | 2024-10-06 00:54:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5a0de430-f3bc-3397-8664-ec2ed4bdc82c | -5.57345 | -44.87709 | 2024-10-06 00:54:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 242.0 |
| 722a7399-04c9-3157-acc9-bfc8d5260e28 | -5.44164 | -46.28739 | 2024-10-06 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 340364b0-719c-3a13-819d-c55b1f84fc6e | -5.34964 | -47.59614 | 2024-10-06 00:54:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e370943-cfa3-31e9-a9d2-fc966366c294 | -5.26436 | -50.88748 | 2024-10-06 00:54:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f241f433-bf30-38a7-a7a2-7fbabe4683cf | -5.18539 | -45.25208 | 2024-10-06 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dcdb5b96-e2e2-31bf-b920-46485372f9e0 | -5.04639 | -45.19421 | 2024-10-06 00:54:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4f2fc58a-4518-31ff-be82-8fb44984b626 | -4.95218 | -45.51486 | 2024-10-06 00:54:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 315910da-ce73-366c-b40b-cbfc85ca9035 | -4.87054 | -50.76799 | 2024-10-06 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b6a3d683-7a12-3e90-a1f1-22ff20aa1dee | -4.86924 | -45.95727 | 2024-10-06 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c8b6d6d9-07f6-32c7-b8a9-4f66e8d018d4 | -4.83028 | -45.81605 | 2024-10-06 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 534c285a-e8c1-3824-81fb-b562a83ef2bd | -4.82326 | -46.80629 | 2024-10-06 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 424737e8-5b45-3c2a-be68-23bade9a4364 | -4.82199 | -46.79729 | 2024-10-06 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cae356d1-1461-33f5-b99e-a0ad974be093 | -4.81411 | -46.99941 | 2024-10-06 00:54:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 54a98c9e-f6df-3029-b68c-6ea22bae32b7 | -4.76841 | -46.6758 | 2024-10-06 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e3cb225e-b9f1-3c01-b4aa-03ed486d6d7a | -4.73751 | -48.83736 | 2024-10-06 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22194bfb-bfb0-3f68-ba15-1daaebd38522 | -4.66501 | -50.98851 | 2024-10-06 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| df351571-25e0-3893-9c17-093988c6fbb6 | -4.58158 | -46.07547 | 2024-10-06 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 03af1ee8-2eee-323d-b4c3-4331a40b3288 | -4.58018 | -46.06578 | 2024-10-06 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 44ab71ce-1393-3d21-a79b-1e828a377244 | -4.45536 | -47.4698 | 2024-10-06 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d103e6ad-9e5b-37c2-bbce-0244f7972bce | -4.45412 | -47.46096 | 2024-10-06 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| f85459fa-5b84-324d-8bd7-c2aac0bd0d07 | -4.43082 | -46.44054 | 2024-10-06 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ffb59718-46e6-3828-9caa-6db901241b46 | -4.38897 | -48.71031 | 2024-10-06 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f0260496-be61-3756-8641-6d5a8ea5e5a9 | -4.37546 | -50.81544 | 2024-10-06 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 5d462978-2388-36b9-8ac9-6c337290fd98 | -4.34871 | -47.30204 | 2024-10-06 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b8f5d4ec-708a-30af-b521-04f6f721e2a8 | -4.34747 | -47.29315 | 2024-10-06 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9d66f69b-a8ca-3022-b809-a2f8621b3b86 | -4.31337 | -47.70876 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| d8af674e-6bbf-3eb6-8351-a1915a192ec4 | -4.31214 | -47.69995 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8a2a1c3d-f936-330c-8b78-e2f6b13613f8 | -4.27771 | -48.64647 | 2024-10-06 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cd3c667b-0941-3d14-a3e9-d5bf4f36dc5e | -4.20807 | -48.87418 | 2024-10-06 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51fee51b-9639-3e78-b95f-7d19bb9938ac | -4.19828 | -48.14117 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 835adafa-3976-3bfb-b5f5-df7f771f52df | -4.19016 | -48.87674 | 2024-10-06 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 09b31b42-baaa-354f-ab33-61e8382885bd | -4.1889 | -48.86765 | 2024-10-06 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 20c62994-1e4e-399c-83cd-ee9b03411b54 | -4.18528 | -46.85738 | 2024-10-06 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 22d5f227-e925-3633-8186-ef43b678d3c3 | -4.18401 | -46.84834 | 2024-10-06 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4929ef6a-99ba-3eb5-b930-cbec5233b3ab | -4.16159 | -48.60523 | 2024-10-06 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4e29385-e80a-3931-8a0f-9b2fd7fbe7a6 | -4.09814 | -48.27871 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aaf90e42-dd56-338d-97e9-1e207e77864e | -4.09691 | -48.26986 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fb8e64ff-ac1f-32eb-8829-cbbad035f329 | -4.09568 | -48.26101 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0a601384-38ed-39fb-9254-0ec1c2f82fc4 | -4.08929 | -48.27995 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f5fea10a-35a3-3bf2-8d15-c4821d9ba8e8 | -4.07044 | -47.95007 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ea2cd0d-5f5e-3cd8-a8c4-7eaadf735cdb | -4.06921 | -47.94127 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bc742fab-e051-3eba-825b-8c29a28f8e85 | -3.93521 | -52.1866 | 2024-10-06 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 39771580-a464-3d7c-997c-2a61b72f83a8 | -3.92331 | -49.67914 | 2024-10-06 00:54:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 50db08d3-8d7f-3ba2-9bd5-9df5d90e4a7d | -3.90695 | -46.45164 | 2024-10-06 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 648cb40e-4066-3a74-be67-f77a7430ea30 | -3.90625 | -48.35415 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |


[Clique aqui para ver as próximas entradas](README21.md)
