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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42e143b3-4aa9-3056-bc94-94d06ada08a4 | -3.40835 | -46.89742 | 2025-10-18 04:00:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60295f23-e7f6-3969-8c84-1a55f3f30cee | -6.24975 | -47.21814 | 2025-10-18 04:00:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbf926bc-ddb8-3266-a268-b0d7e872c5f8 | -6.36974 | -45.76799 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5add8c53-5489-34c7-a97a-b7d4ba091871 | -2.72702 | -48.8353 | 2025-10-18 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a356ad20-7fc4-394b-9204-4036e3a8a79c | -5.89405 | -43.90241 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bee2406-438f-3c77-88d3-5f6baccb4ac4 | -2.57289 | -49.10978 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7592382-3505-332e-9dec-f9c9e5237f74 | -3.16015 | -49.16216 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67ae59da-4fb9-3a94-bc82-82cbdd81a571 | -4.7122 | -44.36015 | 2025-10-18 04:00:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dc5916e4-b74e-3be8-82b8-58182871031d | -6.29927 | -44.72508 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 695020d1-7b6c-393f-8c93-c2f929541227 | -5.03627 | -45.13825 | 2025-10-18 04:00:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0a10017-8ff4-3c42-ab55-4b50a5af2fa8 | -6.03064 | -43.61324 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 294ad222-ede3-3523-a943-66168ea9bce3 | -6.36294 | -45.75877 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6282b50-656a-3658-98f4-8d5ee499766b | -5.07583 | -49.85244 | 2025-10-18 04:00:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfc4eca7-2530-3222-9e8c-fd2851f2ea39 | -7.54854 | -37.79391 | 2025-10-18 04:00:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0708429b-bd0f-331a-a479-3df5f94dc3ee | -5.42072 | -40.88995 | 2025-10-18 04:00:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ccb3fa4-a74c-389d-8286-cfaccfd3adc2 | -5.86945 | -44.84583 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adbd66b4-7309-37bd-affe-e3ea77a1bf83 | -5.71248 | -43.82456 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dfca89c-1608-3fbb-82a2-8be1c59ef561 | -2.44459 | -49.37159 | 2025-10-18 04:00:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aed4d2a2-0a8e-3a24-aef4-a8c857af1f3f | -5.51406 | -43.87194 | 2025-10-18 04:00:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0ee0792-0ad8-34e9-ad85-2a0a6a3e4438 | -5.06355 | -45.85748 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5d9fe267-2f5d-39d1-af14-2c0061ff12f2 | -2.57354 | -49.10592 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebd8a2e7-1458-36e8-b431-664e8a0ce38e | -4.71276 | -44.35672 | 2025-10-18 04:00:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96c0f25b-f538-3030-8996-7764188563fd | -5.87971 | -44.84126 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eb303b3-96cb-3279-9c2c-43660b23de94 | -2.74715 | -49.38588 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0606e7b0-86ed-31d3-b253-d64c09959573 | -6.10469 | -39.52839 | 2025-10-18 04:00:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff09f4ad-0685-3719-980f-8058d6c1b910 | -4.25197 | -48.3731 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f1eb625-45a0-3b88-9f64-bcfa244661ea | -5.99023 | -39.52053 | 2025-10-18 04:00:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e7a55b6b-cbde-3a8c-8fb4-4352527eb024 | -5.9305 | -46.48852 | 2025-10-18 04:00:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aa63583-cf7c-3ffb-ae15-5c33a02778e8 | -5.86886 | -44.84946 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77cf980b-5b18-3f95-9cf8-2f8796bddf23 | -3.05791 | -43.20745 | 2025-10-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f49f989f-3072-3c18-aca4-f848e0f12914 | -4.69437 | -48.62441 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8978672-33c6-3283-bedd-eca17e540224 | -5.92472 | -45.44328 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 58911b79-73e3-3251-ac2b-4fc491e3b04f | -6.37427 | -44.70807 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6040207-584a-3488-a22b-76278bfcba3b | -7.015 | -41.8268 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| add96aba-9d07-3301-be0e-c22bc153fa33 | -5.64657 | -45.10748 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9215a228-8409-3463-aba7-3a5a0fd91a6d | -4.0061 | -49.01862 | 2025-10-18 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fa2bf1a6-5e57-35ed-a5ed-2f5a7c7c68d3 | -4.97759 | -48.36317 | 2025-10-18 04:00:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fb92d7a-0429-3f1b-a108-3f3d32977215 | -4.53701 | -48.41124 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fabd6f2d-5747-3e44-9d64-97b8be1db0ab | -5.0184 | -46.01766 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 19f77ced-e63e-3edf-a685-230835730983 | -5.15268 | -46.26855 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c65d0f68-2c35-39fe-be16-33cd017b2dc3 | -6.98081 | -39.69101 | 2025-10-18 04:00:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3829eb18-6d44-31c2-b191-74ade8b69559 | -6.6003 | -44.44247 | 2025-10-18 04:00:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94cc9a32-e313-3f02-b66e-57fd7bed4a82 | -3.84875 | -41.56936 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d958bfe9-c9b3-3d98-a42d-20e0109a1f82 | -6.3081 | -45.54404 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8945ad45-5e1a-3712-90ea-ad7d602dcc6d | -3.05643 | -43.21673 | 2025-10-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c499805e-8456-3f17-8d85-bf28c573b9da | -5.72081 | -43.82109 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c6aa6ac-560a-32f9-9264-72c25ff08c62 | -6.518 | -44.90353 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c15f78a7-6018-37ea-b2ad-26e08f9b64fd | -6.374 | -45.76861 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 210186bf-ff36-304a-8ca4-2535ca0d70fe | -5.21444 | -47.50403 | 2025-10-18 04:00:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5732f8c9-ceea-360b-b18f-f8929c4767f0 | -5.71637 | -43.82389 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18e36848-ebb0-3c76-a933-0ad42d6e567e | -6.23731 | -44.15223 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 289c8410-e237-3717-b5a9-55ec93d2eb87 | -4.25249 | -48.36998 | 2025-10-18 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb624295-d9ae-3444-88a7-7195fde3b4f9 | -6.14208 | -44.4557 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 0e1da722-72c9-3b76-a7e7-ecc508bc7105 | -3.44883 | -41.84775 | 2025-10-18 04:00:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e2cb534-1f7d-3d55-8f2c-f1843f081905 | -5.45637 | -45.41228 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91ab1475-7b34-3da5-a4ae-6f71bebc4d4e | -5.01181 | -46.03016 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fc54976f-0c1a-3a01-b93d-0f1d7d1e6692 | -3.59811 | -45.97525 | 2025-10-18 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06891cb0-9951-3dd1-8b26-96dd5195dffd | -6.32015 | -44.30791 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ce1539-0f3e-3a31-a1cd-fa7a32370523 | -4.96431 | -44.60989 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 205ad9f4-10f4-3b4a-8599-42ca4e147a03 | -2.96061 | -48.58931 | 2025-10-18 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e83297a-04a0-309e-a652-a6cdc7cdbbec | -6.84468 | -42.42609 | 2025-10-18 04:00:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1a732e0a-cedb-3628-85af-52f41f518a32 | -5.9089 | -44.76605 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3f74e0f-1899-3d7f-8d92-a95b483eb668 | -6.45704 | -46.28257 | 2025-10-18 04:00:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce082e50-9f60-3b1d-9cb7-5e53312e9cd8 | -6.03745 | -43.40938 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5f07c25-7663-3eb1-a681-42684dc01270 | -5.37285 | -45.95391 | 2025-10-18 04:00:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4472f49-7a23-3569-88f7-f126a83b0274 | -6.14382 | -44.29839 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 80b46d5c-f044-371c-a043-14c7b9d80951 | -6.16907 | -40.89257 | 2025-10-18 04:00:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3763ef94-92ba-3009-a65c-cc6b3cd5a25a | -3.34971 | -40.42283 | 2025-10-18 04:00:00 | NOAA-21 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 019cd8cb-066c-3618-9ef6-ee16ec1e44d0 | -4.68942 | -45.84756 | 2025-10-18 04:00:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e255364f-03b5-3572-8e19-1632aa60a0fd | -5.93142 | -47.31861 | 2025-10-18 04:00:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6a906ff-93cc-3936-810d-3c40dc5bc772 | -4.9774 | -42.79415 | 2025-10-18 04:00:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 77d30fa2-3133-39d6-a812-ac83fabc988c | -5.5789 | -41.32259 | 2025-10-18 04:00:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 649d1ca9-95bb-3781-9583-c266c4b77364 | -6.19918 | -41.72454 | 2025-10-18 04:00:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 620fd3f7-d098-320d-ad31-317d5c862cf1 | -5.23816 | -49.8542 | 2025-10-18 04:00:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a485d983-56f6-30cd-815a-c17b981a1325 | -6.53 | -44.9055 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bc2cb23-e6e6-3b38-b1ee-a11dff6ea32f | -6.31654 | -40.94899 | 2025-10-18 04:00:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9d76722c-f009-31ec-b1ae-aed7ad7cd371 | -2.91407 | -52.72609 | 2025-10-18 04:00:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 86f925e3-fa20-381c-bcef-67e2d5c6c00f | -6.232 | -44.13686 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cd08a53-bf08-3294-a699-6dc73f35990b | -5.06608 | -41.20922 | 2025-10-18 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5380d466-5b4e-3b1f-b86c-8117d174a2ad | -5.71615 | -46.5118 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aa5a0b9-5861-327e-96b9-3e82d87ccb55 | -5.71205 | -46.45498 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4543abf-a781-375b-8419-b6efcb06979c | -5.65579 | -46.81121 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 643b4f85-9895-381a-946e-ef9f63e606cf | -4.1778 | -42.21332 | 2025-10-18 04:00:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f133735-6213-3a78-b0cd-96b61cc9823e | -5.55757 | -44.14581 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 992ac228-c49d-3b9d-a120-cdea658c9002 | -2.95326 | -49.33572 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8e035cdb-b253-3ceb-a405-8217ea5bb048 | -5.2812 | -45.60335 | 2025-10-18 04:00:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8230ed2f-b9ed-30fa-ba24-0b384c7ee5a3 | -3.85324 | -41.58566 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 19251d86-f03e-398a-88e1-9d7587a3b26a | -5.8482 | -44.3357 | 2025-10-18 04:00:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f21708b-28ee-3af7-bec7-04a0ed940ef1 | -4.45242 | -43.23369 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 11538d7c-f3ba-3c1e-b19c-33aaa9edfd2f | -2.56872 | -49.11808 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99a9f55b-0065-3414-8143-1e3b0c49fe69 | -3.99577 | -45.50127 | 2025-10-18 04:00:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87c5110b-c2b3-3bb0-b5ea-e78b45f39aed | -4.93614 | -49.76711 | 2025-10-18 04:00:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12597a5a-bd27-30c4-bb31-23c60271a2cf | -3.8039 | -51.64522 | 2025-10-18 04:00:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02c2fea8-4b99-3a5b-80d1-d7a56d8e460e | -5.72094 | -43.81983 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4587b0b1-8f67-3185-a1d1-d7eb61af0ce8 | -7.09936 | -41.46122 | 2025-10-18 04:00:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2abe9b9-4022-31c7-9a2c-ec6cd24659d3 | -5.00816 | -46.02478 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 356fdc7a-2376-3206-82f1-3461f08d84b9 | -5.45218 | -45.41153 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e38213fd-e437-386b-811e-31b7e72c2c68 | -6.23652 | -44.15698 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0dba2d4a-4fc9-3034-94b2-3dbbc2577002 | -5.16545 | -45.22155 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51a380da-9e05-3723-b92d-b4961a82fd47 | -2.95073 | -49.34011 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README18.md)
