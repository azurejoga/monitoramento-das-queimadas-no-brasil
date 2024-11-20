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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 529b22a9-6d57-3e63-a837-535f743c224e | -3.59019 | -43.63175 | 2024-11-20 03:34:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8ddacb7-7d3a-3820-9288-c1d5d1654659 | -9.01459 | -35.60785 | 2024-11-20 03:34:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 617fa84e-7f92-3263-ace8-0d0c772820d9 | -4.13157 | -42.83834 | 2024-11-20 03:34:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8eba7535-e158-3baf-837a-c26c655b42cc | -5.87374 | -39.62893 | 2024-11-20 03:34:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d88e6ab-1415-3372-a105-a8f34e3854f4 | -6.90454 | -39.55344 | 2024-11-20 03:34:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dd2eca3c-b93a-3207-b835-feb406143e35 | -9.18627 | -44.73715 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7111311-3dfe-330c-8c35-abf3aff928e7 | -5.38882 | -45.13487 | 2024-11-20 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ceb9396d-154f-306f-8f75-0a49f4e6a149 | -9.19205 | -44.73822 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04ab0260-1adc-35df-a921-0b0564b6fd5b | -3.7775 | -44.07188 | 2024-11-20 03:34:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41d1038d-659a-30c7-b8bb-7e8ecb9e2bb3 | -2.82026 | -45.13556 | 2024-11-20 03:34:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beeadb1d-c552-38db-a91f-16147ced9464 | -3.38036 | -44.43655 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9721f1bd-7810-3cbd-b721-83637c7a6322 | -3.84047 | -41.56807 | 2024-11-20 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 522353df-812d-3f38-b7fe-05c7712082e5 | -2.51531 | -45.00098 | 2024-11-20 03:34:00 | NOAA-20 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9179460-9e58-3f6c-9745-0e40146b885d | -2.21771 | -46.49208 | 2024-11-20 03:34:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8aca5028-0410-3dde-be33-b8d2767a7754 | -4.69932 | -37.78056 | 2024-11-20 03:34:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3845b03a-0356-3352-abf5-db7afcdb9491 | -9.25386 | -45.00797 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ca5e274-4f75-371f-8899-8747ecc61011 | -3.00283 | -45.44171 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a5cdf4fb-ae9c-3fc3-916a-257f48c21cee | -6.80459 | -43.3003 | 2024-11-20 03:34:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 232232d7-b9c2-38a8-92dd-3957ac51782e | -5.87247 | -40.17345 | 2024-11-20 03:34:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fd506839-c1dc-3f39-9292-e58a9885a774 | -9.79507 | -36.54626 | 2024-11-20 03:34:00 | NOAA-20 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| de4b2cf6-c17f-3778-a689-80b05c45cb94 | -7.81289 | -42.73701 | 2024-11-20 03:34:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3a6921c1-6104-351c-8b4b-06dde3a39e98 | -2.84356 | -46.68209 | 2024-11-20 03:34:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4469312f-313c-3891-af2d-852f1cd8387f | -9.49767 | -43.19017 | 2024-11-20 03:34:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07597ee3-47a7-3017-90ed-646029ab3eb5 | -5.59161 | -46.17609 | 2024-11-20 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9272030-291e-3291-ab3e-789fc1b0fe79 | -6.93741 | -41.1974 | 2024-11-20 03:34:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b18d9ce6-6699-3e94-bf3d-a6cd2a065db6 | -2.21175 | -46.48378 | 2024-11-20 03:34:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a9301385-9cd5-337b-b9f7-d4cf17de6b9e | -9.18856 | -44.72483 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee5e1a97-9309-3bed-b26e-ea1dceaf4a95 | -6.30759 | -41.5177 | 2024-11-20 03:34:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7d08cd74-eec0-328f-b78f-76de775aaec3 | -3.83993 | -41.57115 | 2024-11-20 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 371a7e88-fa8a-372b-88b2-fd5ef5acc146 | -5.01302 | -41.9608 | 2024-11-20 03:34:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c3f7ccd-672f-32cd-a4bc-4a1458af69f0 | -7.26956 | -42.11345 | 2024-11-20 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 766e03e8-339c-3698-a3fe-5059639e658a | -5.3909 | -45.13916 | 2024-11-20 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6b2094a-ab76-3471-a23f-58b33c91a7a2 | -7.11675 | -39.14785 | 2024-11-20 03:34:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07b52071-8649-3fe9-8e6a-f1af7d57f0be | -7.99396 | -44.39198 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1cdba48-5482-386a-9fa5-0aa09384009b | -3.35655 | -45.11337 | 2024-11-20 03:34:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4808b762-9f3e-3526-b9a1-bbf4a90929cc | -5.97247 | -45.36737 | 2024-11-20 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 624b9c55-5ce9-34ca-80f0-16062743836f | -2.99619 | -45.44044 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e709a4e2-6acd-352c-88af-1131d9bd1434 | -2.99522 | -45.4463 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d8cce9c1-ec41-32d6-bc74-48806878459a | -5.24546 | -42.6489 | 2024-11-20 03:34:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eda7bee9-9e8f-31fa-a84a-ea903d28c9c1 | -9.4971 | -43.19333 | 2024-11-20 03:34:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 658681e6-6f2b-3d17-b40d-238f250c4686 | -6.93274 | -41.19846 | 2024-11-20 03:34:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3c6b9909-5f5a-39a4-a160-63f82f14fc74 | -3.59094 | -43.62749 | 2024-11-20 03:34:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b816a0a4-1d6e-3450-a996-0ff44a911a6b | -6.93265 | -41.19666 | 2024-11-20 03:34:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d8be58b-17ab-3f93-a482-5f2695ac1cfb | -5.24904 | -43.83961 | 2024-11-20 03:34:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43d293b3-b301-32d9-89da-8adbffebbb43 | -5.10747 | -40.33073 | 2024-11-20 03:34:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65cbcf3a-cd56-32e8-a1d5-271a2eb63f4e | -10.49032 | -42.50942 | 2024-11-20 03:34:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 679aaa26-544e-344f-becc-ff65cf7e7edf | -7.80774 | -42.73581 | 2024-11-20 03:34:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 879cf4f1-06ae-3063-82ff-43d084735ed7 | -4.14658 | -43.9752 | 2024-11-20 03:34:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0065c4c6-86dc-307e-b8dd-17462ef83ba8 | -3.5869 | -43.62719 | 2024-11-20 03:34:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afaa81b6-2615-319d-8ca7-1d05b4ea3eb2 | -2.51557 | -45.00414 | 2024-11-20 03:34:00 | NOAA-20 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fef29010-2f26-31c5-9a6d-cdc1b3d7e137 | -4.52999 | -38.57605 | 2024-11-20 03:34:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cac0c6b-21f6-3555-8299-24ed0535ae52 | -3.78355 | -44.07294 | 2024-11-20 03:34:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9a0b28f-159f-3546-b053-03ba797fd77a | -2.97446 | -45.12573 | 2024-11-20 03:34:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da99a9e6-9441-34fc-8b52-c7b4cca592d1 | -8.90761 | -36.6486 | 2024-11-20 03:34:00 | NOAA-20 | PARANATAMA | PERNAMBUCO | Brasil | 2610301 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 567da7e2-46de-33e6-9972-a27cb25c7582 | -7.99549 | -44.38378 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 518e0119-8c86-319c-bb98-2e349cf6d273 | -6.53538 | -44.1927 | 2024-11-20 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11d7ba22-3b69-3b59-b07f-a841f89aec58 | -9.01738 | -35.61202 | 2024-11-20 03:34:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a96e5844-c55b-396e-81f8-2f7bd506b4b2 | -3.37615 | -44.43668 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 116c350e-c830-3b1f-ab5c-17eaed2237d1 | -3.05286 | -45.13953 | 2024-11-20 03:34:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d289376e-83bc-377b-8d2d-a027733c3918 | -2.51648 | -44.99865 | 2024-11-20 03:34:00 | NOAA-20 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d84567f-15cd-3ff0-a2ee-e2b90ef2ff39 | -6.66902 | -40.31278 | 2024-11-20 03:34:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 76838293-376a-3e5d-9bfe-c97e402bc5b9 | -2.22009 | -46.47801 | 2024-11-20 03:34:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 215a1f03-be04-3f70-a772-a4b13766bafb | -7.17301 | -39.11545 | 2024-11-20 03:34:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ac2d7bf-1eee-3cef-b499-d570560d044b | -3.22177 | -45.28323 | 2024-11-20 03:34:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a4ece95-b730-3068-93cb-448b54dab857 | -3.78381 | -41.60976 | 2024-11-20 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eff12f6b-5b02-3338-b334-22fd7f3289a5 | -7.99857 | -44.39734 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fd64138-5916-3e24-96ad-4e8fe52f0834 | -9.19359 | -44.72995 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 46ceb6a2-88bf-37f5-9d90-56a5257589ae | -3.2331 | -45.56255 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| ee9c8729-b08e-3450-9352-e3a02118f116 | -2.99859 | -45.4473 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 97dc57cc-edb4-3bbb-a261-2cf5c35cb77a | -4.2012 | -42.19912 | 2024-11-20 03:34:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 51e4eacc-595a-395c-b203-8d1d65e4e3e5 | -3.83772 | -41.57169 | 2024-11-20 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2fed420d-f95a-372e-8fd5-5b9eb453525d | -3.05166 | -45.14 | 2024-11-20 03:34:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 919078d0-61fe-379d-9fe2-8af364c31ef7 | -5.01354 | -41.95778 | 2024-11-20 03:34:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 61344f90-872b-3ee8-9751-5db428389d55 | -2.6146 | -45.90465 | 2024-11-20 03:34:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb3c2511-2b42-3b56-8241-8fe29bfd0709 | -3.37413 | -44.43544 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f2ccd6d-907e-301f-81b4-01c25f89fbf1 | -5.59334 | -46.18323 | 2024-11-20 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5df8be8-0089-3c11-b4b6-e3e817b6597c | -3.59278 | -43.62836 | 2024-11-20 03:34:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d022dc5d-1af8-3b7d-ac3b-73907c629bf6 | -3.77813 | -41.61201 | 2024-11-20 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f0ae961-d81a-3867-81bd-191a12f31d4c | -3.23108 | -45.57437 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| c6a080f0-2f3b-34d8-80ba-9a1dadd91cfd | -9.177 | -44.72272 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 994a6456-bed9-323f-a32d-ac00235f8356 | -3.83823 | -41.56859 | 2024-11-20 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e3232285-301d-352c-90c2-e036181b5c05 | -7.99703 | -44.37559 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c066f79-0f1b-33a0-817a-1c1e0329fa5a | -3.23209 | -45.56847 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0026c303-ae1d-3c17-9965-126de4857bed | -6.52948 | -44.19201 | 2024-11-20 03:34:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6a37107-3053-3661-b37e-a2093e0973dd | -7.19572 | -39.1232 | 2024-11-20 03:34:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12f18246-0d2d-39c8-9bc4-c56baac818f4 | -2.99294 | -45.4403 | 2024-11-20 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b2569970-a927-32dd-baf5-5916bef76897 | -7.11738 | -39.14413 | 2024-11-20 03:34:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b11aad86-7aea-37f6-8cad-3f131322ff4e | -3.58758 | -43.62315 | 2024-11-20 03:34:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bf529e5-8856-349b-8da5-30becf072537 | -5.24606 | -42.64543 | 2024-11-20 03:34:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c74d9689-7131-32a6-a34a-acec12fb7342 | -3.88877 | -43.15359 | 2024-11-20 03:34:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ed351df-5fb5-32b1-a89b-592c92fb95f9 | -5.25488 | -43.8406 | 2024-11-20 03:34:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6adc4c13-dfd6-3096-a4de-d9d3796029b0 | -8.00005 | -44.38907 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 569fd770-629c-3180-991c-1d9f0916bb5c | -7.10547 | -34.84283 | 2024-11-20 03:34:00 | NOAA-20 | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9b5248cb-1df5-36a9-b029-df048b2591f2 | -7.19511 | -39.12674 | 2024-11-20 03:34:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68d9fc94-671c-323d-9a94-d889c9d8423b | -5.39181 | -45.13417 | 2024-11-20 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70c8d951-4601-36e1-a44d-5b1b91c93e96 | -8.30256 | -35.21636 | 2024-11-20 03:34:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4150b440-844d-3519-883d-404adc12d9a1 | -4.43745 | -46.59351 | 2024-11-20 03:34:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed4915aa-28bf-3284-92c7-2688d3a12856 | -7.99896 | -44.39714 | 2024-11-20 03:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5110dc25-53e7-35e8-93e4-da426823f955 | -3.37697 | -44.43172 | 2024-11-20 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 19e23d51-7ab8-3b87-91b8-b8e4d62db98a | -5.59834 | -46.17706 | 2024-11-20 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README19.md)
