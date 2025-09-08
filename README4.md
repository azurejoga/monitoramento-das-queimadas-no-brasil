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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5edd1e1c-171f-3ad9-baa4-d769aa454637 | -13.7982 | -46.286999 | 2025-09-08 00:25:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 99a8472b-54cb-3a6c-af82-c28c256b42cf | -16.065701 | -43.6422 | 2025-09-08 00:25:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f96ab4a6-004b-3923-9e9e-558dfb2e25e5 | -11.5493 | -44.657001 | 2025-09-08 00:25:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba4e2668-7ed2-3d62-916a-35faf7c424d7 | -16.319 | -52.938599 | 2025-09-08 00:25:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ad9e7af-f84d-384d-ae5f-0abdfe55a710 | -11.3936 | -43.5877 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 266b9150-4389-3c58-bdfc-f10d9c6682e2 | -9.8069 | -47.7826 | 2025-09-08 00:25:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a86a7c7e-5e23-3f26-8601-2cbed909411c | -11.8391 | -51.0588 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 353aad53-160a-3488-9ceb-7e8d0df900a9 | -7.0746 | -43.904099 | 2025-09-08 00:25:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5c57c96c-5b76-35d8-84fc-739e4bf1421f | -6.2363 | -43.711201 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa5dbc91-b727-3a24-8a77-31a2dbd746ab | -6.1992 | -49.416901 | 2025-09-08 00:25:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c52d0190-98ef-380f-9e3a-818e59e000ca | -15.1469 | -47.994701 | 2025-09-08 00:25:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63a8ada6-e089-3340-a1e0-b1bcfce16c35 | -16.896099 | -45.8465 | 2025-09-08 00:25:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dd135bc1-349b-3156-a66e-11f0bba84d1d | -6.2114 | -49.425701 | 2025-09-08 00:25:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e2515d2-c14a-34fa-8916-32b11562481c | -15.1738 | -47.976601 | 2025-09-08 00:25:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 998dd74c-e9ce-312e-a957-a8f33e0f6720 | -8.1825 | -44.789398 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4235cb25-66ae-31a8-8abf-3800501969cb | -11.1656 | -54.994301 | 2025-09-08 00:25:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 273ddc81-fd08-3803-bc06-668c31d4928c | -12.924 | -54.8008 | 2025-09-08 00:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 878d2f82-2b1a-3de7-bd2e-3d10e71f128d | -11.3588 | -50.381802 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb60f1c9-9ea3-3820-af72-ad1425112317 | -7.3319 | -43.946999 | 2025-09-08 00:25:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bb32420c-adaa-3aeb-9cce-1ed2c52e8cf1 | -7.2035 | -46.206699 | 2025-09-08 00:25:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34847722-adcc-3071-a64d-3a363c59906a | -6.5438 | -42.941002 | 2025-09-08 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acf5c8e2-4353-38b2-802a-79172c04870e | -5.8437 | -43.843201 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8144fbc5-7f65-3c94-9342-1eaabf4f7e64 | -11.3204 | -46.577499 | 2025-09-08 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e782e22-2e9d-31a0-8448-c64a6a8a0d01 | -6.6187 | -53.347599 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35fe9702-1972-322b-8b3f-426d46616834 | -5.3599 | -42.6409 | 2025-09-08 00:25:00 | METOP-C | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08566551-658d-3771-b30f-5f67f51e86e9 | -15.6478 | -48.267502 | 2025-09-08 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 623ef8d8-9382-3f40-9a8a-b48686aa5b1e | -18.179701 | -42.439899 | 2025-09-08 00:25:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a915f08-a64a-34db-b8b8-76c232a2a719 | -11.255 | -46.464001 | 2025-09-08 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1f5581b-75de-3bd1-8864-519bfbbf1890 | -15.6453 | -48.2547 | 2025-09-08 00:25:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8bef442d-b51d-3770-aece-5d55d4d22b63 | -5.2003 | -43.691898 | 2025-09-08 00:25:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 728a5008-6168-33d8-b1e9-45ff08e29af5 | -12.9869 | -45.2192 | 2025-09-08 00:25:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0b49223-d5ca-3da5-9d5f-e1f757b1583c | -6.234 | -44.829399 | 2025-09-08 00:25:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4445a8f7-cbc7-30d9-a991-8ca3213b2edf | -11.349 | -50.383801 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bc1aae6-b43d-3c46-99ee-8437fdd5ddec | -5.4424 | -42.818901 | 2025-09-08 00:25:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ea751ac8-603e-313d-b0c0-c0a5372696f0 | -7.0702 | -45.2005 | 2025-09-08 00:25:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3bdbdc3-8f48-3057-90e0-c8b4243ec228 | -6.5827 | -44.0079 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46017523-2c27-3ca7-a074-2afe800b9b00 | -5.7698 | -44.918701 | 2025-09-08 00:25:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dfdfc91-f7bb-3ab1-838e-6f01149b76e6 | -6.4752 | -43.988899 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4d2c1de-a1f8-39fb-af54-ab87ad620877 | -18.016399 | -47.131599 | 2025-09-08 00:25:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9956eab3-f0e3-359c-aa43-55f440645a15 | -6.1025 | -44.252701 | 2025-09-08 00:25:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b276011-a5af-3c32-b845-d0c7ad97c1ae | -11.3983 | -43.6087 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99c376c3-9b1e-3323-b979-0dd2cceb47e5 | -6.161 | -44.780499 | 2025-09-08 00:25:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1e5cd19-39d4-3545-beb7-02cb68429747 | -5.6229 | -43.9147 | 2025-09-08 00:25:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2998301-fbea-3f55-8340-e12bebcf6712 | -11.4077 | -43.6507 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 769f1b1b-9cf6-3350-a64f-7ab82a3a455d | -5.727 | -45.4105 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31af967d-ced8-3007-b448-2648c2ac7070 | -6.5263 | -45.848701 | 2025-09-08 00:25:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e458ea21-f70c-3ba8-922a-49d3e91b1e8e | -18.0096 | -47.096298 | 2025-09-08 00:25:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b874565-2378-3e44-ade7-423541f60d66 | -14.4547 | -48.808701 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f6ffd8b2-27e4-3fe2-ad27-b780a9a6e7cd | -13.6561 | -44.232601 | 2025-09-08 00:25:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b26331e8-b56e-3446-a02b-f3c1b378c617 | -7.5863 | -44.6581 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d664c3cb-6ce2-3217-8146-f8ea79c61648 | -5.6877 | -45.4193 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a555b2dd-c9a3-3bd1-9c8f-d70fe1783f61 | -5.8452 | -43.849998 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 659324f2-b401-32bd-9131-dd272ed4dbb7 | -16.3431 | -43.6427 | 2025-09-08 00:25:00 | METOP-C | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 430cdf1c-6474-3ebc-aff1-c1bf0b8e51ec | -4.2512 | -48.176399 | 2025-09-08 00:25:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1df93d-4121-366f-831d-85668eec7f20 | -5.837 | -43.8591 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 647b44ce-79ce-3b40-ae08-fe4d2861d180 | -16.3209 | -45.038502 | 2025-09-08 00:25:00 | METOP-C | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 41887911-f4e9-343a-b42c-e4f6ac93b7d7 | -3.6333 | -43.651699 | 2025-09-08 00:25:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 186592e6-b428-3a71-bd27-b1ce9bdd10b1 | -13.5331 | -48.118 | 2025-09-08 00:25:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 41ee4d87-d6c5-3979-b1e0-94a3647c0aab | -12.3945 | -47.4935 | 2025-09-08 00:25:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd32fca-97c2-3279-8a23-16d3eccffd47 | -8.0288 | -44.0644 | 2025-09-08 00:25:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df772923-68a3-379e-97b7-64c425e2b0c4 | -6.3706 | -42.995201 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da921d87-9a92-3bd3-9905-74d7be50eb41 | -6.832 | -45.6059 | 2025-09-08 00:25:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 450571c2-c4d1-3446-bfde-34aecdb82d8a | -20.4596 | -43.971298 | 2025-09-08 00:25:00 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 58cf521d-dd2d-3254-8ff9-6f2a2a561715 | -15.2819 | -43.3927 | 2025-09-08 00:25:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 8ab30f5e-bead-30f6-b25e-8f67776fd137 | -11.6421 | -46.884399 | 2025-09-08 00:25:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2f190c-8820-3df0-ae82-7eda9a71d21a | -8.1554 | -43.1744 | 2025-09-08 00:25:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 451e92ce-c249-3177-86cf-53c8b15da8b2 | -14.9808 | -48.028801 | 2025-09-08 00:25:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 05c9442e-6c97-3ffd-bd39-f2fd26f26fbd | -11.1083 | -48.3755 | 2025-09-08 00:25:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bb80355-7f0d-3a41-b8ae-4137459bb39d | -11.3362 | -50.370499 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93d077f0-75fd-3c4a-b5f7-e7e9d32f45a7 | -13.5308 | -48.1064 | 2025-09-08 00:25:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 90d3b433-56e5-3418-8f12-236fd8e9252e | -11.385 | -50.360699 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c4a2dd3-b870-3d03-b329-f27922456dc4 | -8.1238 | -48.4758 | 2025-09-08 00:25:00 | METOP-C | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b94858c-04fb-3d7a-871f-1ee0c29d6884 | -6.3654 | -42.616001 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd9a5b2a-3d59-3b64-a3d3-6c9884e48db2 | -12.3966 | -47.503799 | 2025-09-08 00:25:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40630c9f-6bfc-3f6c-975e-5bbdff5e0780 | -6.2842 | -43.830299 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2647858-9def-340f-91f7-0bb9a0ebfeb1 | -12.9144 | -54.802601 | 2025-09-08 00:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03bdd45e-be75-37de-9fad-311b954ed7c9 | -10.7804 | -47.7407 | 2025-09-08 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d62c2d54-d89e-3033-bab9-156761d884a4 | -6.1874 | -42.6492 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bba6da2e-78c1-38b2-81b7-bbee11c947c5 | -5.7668 | -45.631699 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f286efc-4051-3870-a990-002fc946a0af | -7.2018 | -46.1991 | 2025-09-08 00:25:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6d94c88-2999-3b85-8cfb-310ad09a2cc8 | -7.081 | -42.944 | 2025-09-08 00:25:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e00ae56-d0c7-3e4e-b645-d5f358b1d693 | -6.18 | -43.601002 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b553116-cb5f-3502-ad88-183c880abf8f | -6.8697 | -45.544601 | 2025-09-08 00:25:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9f10dec-6358-3b13-bd45-dcaa92ae01c0 | -6.1816 | -43.607899 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08ddcaae-d3dd-384b-9384-8791e191d945 | -6.1784 | -45.038399 | 2025-09-08 00:25:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce47f487-78aa-322f-a9cd-181121c1ba74 | -5.8504 | -44.187099 | 2025-09-08 00:25:00 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 424bd7b1-b656-39f5-81ec-2c75bbbfa498 | -15.1199 | -48.0634 | 2025-09-08 00:25:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2d00899c-e050-3231-8617-eb58de5c7151 | -6.0115 | -45.894001 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3946b0c8-2fae-3be7-959f-f5ee378b573b | -15.6551 | -48.252701 | 2025-09-08 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 147364a2-b5f7-314d-a049-a4be01865d79 | -5.7846 | -45.6651 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 442e6ec8-d5c9-3f07-8f25-039d972c681c | -8.2021 | -44.785 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 956bce74-1078-31a5-ba4d-de55cb7a0884 | -5.4505 | -42.809601 | 2025-09-08 00:25:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96048871-91cd-3348-a8c4-785a1e29a10a | -6.201 | -43.378399 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 721fab94-ce9c-3221-9fd8-45bf989eacb5 | -6.1614 | -44.7369 | 2025-09-08 00:25:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9671c9f-a302-3561-a92a-6400b1ce1855 | -13.7094 | -46.890301 | 2025-09-08 00:25:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5672e84-293f-3e46-95c9-dd3c0a162075 | -12.1542 | -43.950298 | 2025-09-08 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 298c50e8-521f-32f6-ab69-2094df6b0f16 | -14.5054 | -48.756901 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 91ce5bf6-7499-3e98-b7f9-ffd791778ddd | -17.1392 | -44.445702 | 2025-09-08 00:25:00 | METOP-C | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5eefdcfe-9b3b-3657-b8ec-9779e3558a21 | -6.8054 | -52.7939 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8124948-294c-346c-8c48-0ffd6a89554e | -6.1629 | -44.743801 | 2025-09-08 00:25:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
