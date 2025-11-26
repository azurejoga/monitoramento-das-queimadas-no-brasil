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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3849300a-3273-3688-8c38-0a4b6d3afa20 | -3.36604 | -49.25726 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da7c869d-0c50-3e3e-81a2-e9becc35492b | -4.45592 | -44.29892 | 2025-11-26 05:10:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64572a9b-1f17-3af8-af37-78ee80f7df21 | -3.42948 | -50.54416 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c2b8800-9d4f-31e9-b70c-8e723433a68f | -3.38827 | -47.18453 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 342c243c-23c9-3485-9401-30125aa90fec | -2.50492 | -47.82624 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0d8f949b-aac8-379f-9f35-47b6bfbd9057 | -2.93477 | -48.23521 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3e3e25e-9013-30b4-a72b-5ad6206ce60a | -2.93563 | -48.22941 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f91ec45-4063-32c7-89da-96ee0be385e8 | -4.82269 | -43.81855 | 2025-11-26 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2eac41a0-27f5-3189-8ee3-5068b308f5f2 | -2.74622 | -51.90846 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f50a188e-cbf8-35f0-a1e8-91fef5fd72e1 | -2.94089 | -49.35987 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 279f23b0-3bc3-3191-92d9-26fe9c22833b | -2.88616 | -51.80938 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cf95b4e-08e3-396e-95ff-e350ece1653e | -4.18159 | -43.7086 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 312b2095-fa62-3808-99c6-207a4cc8ada7 | -5.28411 | -43.64183 | 2025-11-26 05:10:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e51ab062-9392-34d1-82a6-423f2b9934b9 | -2.93735 | -48.21769 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2089ee3f-19b5-37bd-8276-939a8c16da40 | -2.43475 | -50.26337 | 2025-11-26 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b9052b5-0a94-3adc-8039-84251a9dfa16 | -6.57366 | -47.89363 | 2025-11-26 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13255133-d4d5-34b2-b8a7-159ec02a1045 | -2.75014 | -51.90906 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d837bf8c-c79c-37f8-9d7e-79e3d3dfe275 | -3.17656 | -50.24287 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d571a244-0a3f-3926-b663-3cd89daa1327 | -2.92973 | -48.23441 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3ec7cef-1f06-31b3-b44b-63be24940772 | -2.8957 | -50.49921 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32fb2129-8ff6-3006-a1e7-873618dfa730 | -3.48096 | -43.42931 | 2025-11-26 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8afd8b66-1003-3eb3-8c51-4f537587819e | -3.82705 | -48.99182 | 2025-11-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c968421-d9c5-352a-a0b3-2293cfd58899 | -4.17709 | -43.74002 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ab326e50-466c-35d4-b9dc-ea512f4b8c78 | -4.65817 | -43.9831 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5165f42f-6df9-3931-8ea0-197936031606 | -2.92728 | -48.2159 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ce25b85-2b5c-3beb-9b21-36e3c007620c | -2.93232 | -48.21679 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a59508-33f5-34e5-9e26-b50677f7114e | -7.75058 | -44.19062 | 2025-11-26 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 30f1c804-370d-31fe-81a2-80766b715bbd | -1.38386 | -55.33991 | 2025-11-26 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e2ff33a-4993-3eb0-adb6-dede9b96f64d | -2.74545 | -47.13139 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2cb4acd2-ae66-38d5-b76b-32c5b2d74b0d | -2.99254 | -51.06445 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b1dc940-ca4f-39a7-8af0-c1b98d41e0bb | -3.46045 | -50.54459 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f10df766-1888-3d21-8068-093cf18a304e | -6.76656 | -46.51691 | 2025-11-26 05:10:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5fe83175-f9ec-3545-affd-2c2b41e45fbb | -4.17233 | -43.73108 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 7fd15c63-2a1b-3e8e-9ef2-f8614992b85b | -3.26264 | -51.17269 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 32397576-83f2-3cee-b97e-1add00ee3143 | -1.36303 | -55.42924 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 277fdb03-b48c-3836-be20-03d2d65f42af | -3.44118 | -50.19114 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddba82bd-7e9c-3be1-9e80-29f5846f70fb | -5.28289 | -43.64256 | 2025-11-26 05:10:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 956fc7cc-e21d-34f2-b179-234299d675fe | -3.04093 | -49.51079 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9789978d-dec8-3823-8099-490cda4bd7d5 | -4.93291 | -49.15446 | 2025-11-26 05:10:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1dc3fc16-1843-37e3-bbfe-721a2f6adac0 | -3.43741 | -50.18605 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b947b9a-978a-3246-82cc-57397921d239 | -4.1652 | -43.72525 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 10643ae4-8ab3-3a11-ae4f-a1875052dff1 | -3.39606 | -49.2265 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47959b73-7f83-3242-8500-aad08a80a113 | -4.17957 | -49.87084 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e71e542b-bc81-3b17-a07b-e1b6cec10995 | -4.24821 | -48.56761 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b036b33-5619-3d5e-a7f5-dbf463380fc6 | -4.48353 | -50.35406 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dada4435-0aa5-3003-88f3-e5f07343db15 | -4.15835 | -43.72414 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| acc868ac-9aa2-3cb1-b5cb-0d70f6d7dce2 | -2.47685 | -47.83753 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a7c2ef5-ae27-3beb-99fa-617ffbfc652d | -3.00739 | -49.58209 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d1bda1f-fcaf-34f1-9307-adee12ba8cf7 | -3.13802 | -49.40181 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 70427efc-7cb4-3255-96e5-80890755485b | -2.99312 | -51.06067 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6acad05-3978-367a-b4bc-0e9bd84b1f7d | -3.90172 | -52.12725 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f74cf77-26e3-3169-a74e-fed3efef189e | -2.92095 | -48.22384 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 257dc1bf-2efa-3398-b420-ebdd05fa8666 | -6.87802 | -47.2395 | 2025-11-26 05:10:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a89bcfa1-cca8-378b-bb71-9af6a72f3461 | -3.40628 | -54.57959 | 2025-11-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 263baa10-a023-32ae-aa3a-9decda1d07af | -2.94363 | -49.35428 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ce72bdcb-90bd-380f-9004-19e30e93e67b | -3.88171 | -54.19979 | 2025-11-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11e553da-7411-32af-90e6-7c369c18a6e5 | -2.75091 | -51.90409 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3220e38d-ced5-3186-9daf-2dcc4859b8ea | -3.3455 | -51.17275 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29f09a0a-e409-3b6a-af4b-8822d4da2cce | -6.58306 | -47.90597 | 2025-11-26 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90fb8e4c-8d18-370e-838c-47086c438718 | -3.00278 | -49.58141 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fcc250c-27a3-38b4-b3cf-d6b2393eaf57 | -3.43297 | -50.18534 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa05597e-5e47-3e1d-b440-62f1d18d3e26 | -3.36117 | -50.48483 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffa516d1-d323-3d40-b696-d9b2805a69f9 | -3.3621 | -49.50457 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d4ef464-09ca-39f0-80c1-1dd964ea7f70 | -6.58403 | -47.89905 | 2025-11-26 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7a61eb1-23a5-3e7f-bfbe-10c6ee95b977 | -8.05918 | -43.10488 | 2025-11-26 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 9552efd1-5451-34ab-bcbb-dc0e3dbbcd61 | -8.05346 | -43.13782 | 2025-11-26 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| b2054cd3-89eb-3965-a372-1878b40c8e21 | -8.16013 | -43.20339 | 2025-11-26 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 25d5ee2b-8988-3e57-8b98-445f8fafd018 | -6.30027 | -43.76657 | 2025-11-26 05:12:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 166e2d2c-13e8-31f7-8db6-2d7a2f8dc7ec | -8.03763 | -43.13491 | 2025-11-26 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 45a0fc25-7dc8-3ac4-a61e-06c1bda8c2c7 | -8.04335 | -43.10223 | 2025-11-26 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.7 |
| ad9c0675-c291-3c98-bb2b-882d865c4ac4 | -11.11182 | -54.42734 | 2025-11-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4760a98c-1ed2-318c-9d17-7f5887b6ecc2 | -11.25922 | -49.467 | 2025-11-26 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c163b6e5-ad93-37c2-b287-891b21766623 | -15.51447 | -50.40382 | 2025-11-26 05:12:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39e5fa6a-5629-3070-be45-fcf08d027395 | -11.25799 | -49.4767 | 2025-11-26 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 780c6f1c-536c-3257-88ea-df782ed4ff9a | -12.53369 | -48.34603 | 2025-11-26 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df7c91fa-b82a-3ba2-a246-1ea0e158ec93 | -7.06337 | -68.13612 | 2025-11-26 05:12:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 39ddc2f5-7841-30e4-a257-99b331ca0c57 | -11.26323 | -49.47746 | 2025-11-26 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5535811d-5573-3072-9065-783c4a4534e0 | -11.2584 | -49.47348 | 2025-11-26 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be2f81e6-a18a-3489-aac5-bc695cc8291c | -11.26404 | -49.471 | 2025-11-26 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 007f2875-ab2f-3efa-b1a8-e97d5b1b6680 | -11.25881 | -49.47024 | 2025-11-26 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c565a45-a054-31f2-b7c0-60163f48a907 | -12.062 | -48.2326 | 2025-11-26 05:12:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48ee8d27-f1f8-37b6-b692-5040631968ef | -15.50928 | -50.40288 | 2025-11-26 05:12:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 999bd234-dbfb-333c-a811-b1e42f541d78 | -16.54826 | -54.2471 | 2025-11-26 05:14:00 | NOAA-21 | SÃO JOSÉ DO POVO | MATO GROSSO | Brasil | 5107297 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 370a0f75-5281-3a24-9196-4da68dabdce8 | -20.39497 | -57.95949 | 2025-11-26 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5b1659f5-d9cd-31a6-bdf5-5ae7320c85a9 | -17.01964 | -56.57914 | 2025-11-26 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f2bd008e-8cca-3920-b040-90fd585f270f | -16.22528 | -59.51912 | 2025-11-26 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a634d1fe-c168-34f6-99d7-28b41d05fe50 | -22.47627 | -49.13129 | 2025-11-26 05:14:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5f2563a-efbc-3241-baa9-73b8e8c9ce8a | -22.08425 | -56.58153 | 2025-11-26 05:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a44f0983-2303-33b9-b93d-4b0e26654985 | -20.39848 | -57.96005 | 2025-11-26 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| da071aef-7703-3fa2-9148-24f1368ea176 | -16.0951 | -59.97833 | 2025-11-26 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5286759-c9f8-3e5c-935b-49282d6596e2 | -20.40199 | -57.9606 | 2025-11-26 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f62e4825-ac3e-34fd-a5ae-a37c2df1a477 | -18.9416 | -49.30169 | 2025-11-26 05:14:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8271f012-260d-35a4-8301-9df48b8251bc | -18.94745 | -49.30232 | 2025-11-26 05:14:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3f8f44b-83e8-3f66-a29b-a023890fc8e3 | -21.70609 | -57.6624 | 2025-11-26 05:14:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d398a985-f3c3-35b9-91f5-fcd3af9bd6f2 | -23.55956 | -51.44897 | 2025-11-26 05:16:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ba55e888-4184-386c-8641-dbae85e0d16c | -27.91116 | -53.77723 | 2025-11-26 05:16:00 | NOAA-21 | SANTO AUGUSTO | RIO GRANDE DO SUL | Brasil | 4317806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 54ead9d9-08cb-3775-878e-2b45d1a5fe7a | -25.19213 | -52.97421 | 2025-11-26 05:16:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 87037d50-0afa-37a0-81ed-c504cfa5e67b | -27.91363 | -53.77688 | 2025-11-26 05:16:00 | NOAA-21 | SANTO AUGUSTO | RIO GRANDE DO SUL | Brasil | 4317806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 399ce208-ec12-3869-88d9-9129367bf853 | 3.10272 | -60.76685 | 2025-11-26 05:37:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9d16448e-0803-345b-8018-00126a5f4aed | -4.17146 | -49.87151 | 2025-11-26 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README29.md)
