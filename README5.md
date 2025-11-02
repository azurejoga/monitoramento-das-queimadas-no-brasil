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
| 201f581d-d146-3cfb-b9e5-eafa8d43b4cf | -6.12347 | -39.72243 | 2025-11-02 03:27:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 36cfc983-da3c-3125-b1cb-0c0237e95041 | -7.17944 | -41.93844 | 2025-11-02 03:27:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f876e08-b84f-31dd-a0ec-0d1d05de5d6a | -4.63961 | -38.56542 | 2025-11-02 03:27:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 17.4 |
| f33b848c-1529-3b53-a336-0132d20b8687 | -5.30694 | -44.42321 | 2025-11-02 03:27:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3dc8869-3fc8-3f6a-814a-43bf3abef670 | -3.28129 | -42.63216 | 2025-11-02 03:27:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4537ffd-4d1e-34af-b392-155fc7569e79 | -5.81287 | -35.5724 | 2025-11-02 03:27:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9c18884-54a4-3e54-9124-c7b91ea1a996 | -5.12895 | -43.37754 | 2025-11-02 03:27:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edacfa4c-b68e-3f05-86ce-e3cfe7f4dd82 | -5.03688 | -43.62567 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 67c7d1f0-f9cb-3e95-a789-35932c80d7ab | -7.40034 | -40.07456 | 2025-11-02 03:27:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 74c226c9-efc9-36b7-b379-f0f708c53611 | -5.03855 | -43.62605 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df329c2e-0640-3060-9856-34c5713671b4 | -5.0395 | -43.62082 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 504f19d0-4a09-3401-bad8-c3f7667f88e8 | -5.07022 | -43.66986 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70277e7f-cfab-3f1f-9757-d4a7aa59c2a5 | -5.03214 | -43.62506 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9aaaac1e-05b0-3528-8034-a8ec2089410a | -6.09505 | -35.36176 | 2025-11-02 03:27:00 | NOAA-20 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f15ac2ef-cbeb-3ebc-8f07-c66905c3fec0 | -5.08915 | -37.60763 | 2025-11-02 03:27:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 12.0 |
| b2c75250-35f0-3bba-9b3c-143ff3321fda | -5.07469 | -43.68184 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4621aa2-9008-307c-8f28-f12e8e433676 | -5.06834 | -43.68039 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d86ea12f-a35b-3f2a-9a9c-763a79ec7d63 | -7.40841 | -40.07248 | 2025-11-02 03:27:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 84e378f4-ddee-31c1-8266-1a766aa67f45 | -7.37384 | -35.09121 | 2025-11-02 03:27:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c39111a-14f3-35e4-9597-ccfd23ceb2b6 | -8.17187 | -34.98079 | 2025-11-02 03:27:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 237df73a-6fae-33f4-96ad-87c418549968 | -7.40354 | -40.07159 | 2025-11-02 03:27:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 75ff713f-1a8e-3555-9ccb-b06ab268a480 | -3.28267 | -42.6291 | 2025-11-02 03:27:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81e30a44-6baa-32cd-b355-27d8de998ccb | -4.64341 | -38.57097 | 2025-11-02 03:27:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 01a1d91c-adc0-32b3-bd09-916e7f2bad8e | -6.09434 | -35.36614 | 2025-11-02 03:27:00 | NOAA-20 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 681ee68b-b450-301f-96f5-3e4dbf4c935c | -4.67919 | -44.62016 | 2025-11-02 03:27:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 494c7f8e-cd13-37df-a567-b7677a5a47ac | -7.033 | -41.46576 | 2025-11-02 03:27:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e151407a-9f17-3c07-881b-bf574217cfb7 | -6.48141 | -39.41208 | 2025-11-02 03:27:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 16c53405-5171-3fd7-a1ff-c21d16a8cfc5 | -5.03118 | -43.63034 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9dd4497e-0a07-3e84-9a1e-ac66c1af59ff | -6.39328 | -38.90927 | 2025-11-02 03:27:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 627e8d28-12f3-3409-a93a-d4f66f9aa0fa | -7.17388 | -41.93751 | 2025-11-02 03:27:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9483cdfc-4a0d-3d41-94c5-d5a6ac779772 | -4.6426 | -38.57575 | 2025-11-02 03:27:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8e41537a-64bf-3af5-9936-e785641a9b50 | -6.78971 | -38.42931 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cd727418-c87e-32b5-8121-e70720188242 | -4.67237 | -44.619 | 2025-11-02 03:27:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed82e526-1376-3da0-937f-45d9b8a40bdc | -7.17486 | -41.93845 | 2025-11-02 03:27:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4c29faab-4eaf-359d-a507-6e5f529534a3 | -5.31362 | -44.42434 | 2025-11-02 03:27:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2efeddd8-e634-321c-b80a-5f4267ce3bac | -7.40128 | -40.06905 | 2025-11-02 03:27:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5cfd8c3-cdbb-38f9-885d-78464e257a2d | -3.69351 | -40.44033 | 2025-11-02 03:27:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 149615d2-7dab-394d-97ab-44aeb0bdbaec | -5.34209 | -45.38065 | 2025-11-02 03:27:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c271bb1-bb77-333a-8a33-601e4cb85f66 | -5.0314 | -43.61938 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| da3accb7-51f5-3f50-933e-4232c4aea4b6 | -6.09872 | -35.36235 | 2025-11-02 03:27:00 | NOAA-20 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| abb16052-f0d9-3d2b-902e-794e45b3a796 | -4.33328 | -40.19133 | 2025-11-02 03:27:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d8ea796e-2d95-37d1-9928-2f50408b18de | -6.12833 | -39.72334 | 2025-11-02 03:27:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cffbbf53-9e73-33e8-8798-1adf55bfd856 | -5.03048 | -43.62466 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 35f57560-e63e-3c02-afee-d193e5e9d323 | -5.81659 | -35.57304 | 2025-11-02 03:27:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02fe9216-14ae-39dd-a623-eb366214b7d7 | -7.40743 | -40.07799 | 2025-11-02 03:27:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 664f32cf-a27b-380b-b14c-3b57c71de374 | -5.06928 | -43.67512 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 620d9784-194f-3d09-b6c9-bb39157f1331 | -9.10958 | -40.61363 | 2025-11-02 03:29:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31367de7-290e-35ed-9fd6-105e4f71d7d4 | -8.12773 | -42.21794 | 2025-11-02 03:29:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0bbc07fe-7fed-384e-8225-c5f56efa470a | -7.29613 | -41.57418 | 2025-11-02 03:29:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7db29c7e-89f2-32f6-9ea9-1c1a91a78fd6 | -12.30457 | -38.94822 | 2025-11-02 03:29:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f7c90869-671f-3d9e-8304-8faa01c85dc7 | -12.64183 | -41.28345 | 2025-11-02 03:29:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78831b16-5dcb-3279-97f4-23a7dfca53d3 | -7.30153 | -41.57518 | 2025-11-02 03:29:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 44ccdf15-b7f6-38d7-a6bf-c498f1505aad | -10.736 | -46.23053 | 2025-11-02 03:29:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80d356a7-c1f4-3ab1-be96-d4d747905361 | -8.12842 | -42.21419 | 2025-11-02 03:29:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f9ddb939-7e16-3092-b855-c275c472df21 | -12.20889 | -37.77775 | 2025-11-02 03:29:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5260ffaf-26b5-3264-94b1-4263f897c9a1 | -9.31016 | -41.07305 | 2025-11-02 03:29:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2c5fe95-8032-316d-a0ec-d673c1753400 | -9.44813 | -43.19971 | 2025-11-02 03:29:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f956a13c-c22b-3e81-aaa0-4a639f25f24e | -12.64287 | -41.27793 | 2025-11-02 03:29:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 658d0e69-9e68-315f-87c4-a79a8300f369 | -9.31071 | -41.07007 | 2025-11-02 03:29:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 53a3e4d8-2c9a-361c-987e-75670636f980 | -9.44731 | -43.20401 | 2025-11-02 03:29:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3346f339-5ba8-3fb0-b07d-c185c9f4eec9 | -10.08962 | -39.28362 | 2025-11-02 03:29:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fcd5473a-a0cd-3900-8d33-2874663868d4 | -9.20068 | -36.7877 | 2025-11-02 03:29:00 | NOAA-20 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 205318a4-a700-39d7-8cbc-6f261966b60f | -7.88249 | -39.10073 | 2025-11-02 03:29:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e0bd7b8f-4128-3cd2-9ad9-6554cc9e061e | -7.30093 | -41.57854 | 2025-11-02 03:29:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7d594829-2266-380e-b6d4-961b52c38d3c | -7.29553 | -41.57754 | 2025-11-02 03:29:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1e7f99bc-3729-3f53-83be-e6f8455ed344 | -7.88622 | -39.10044 | 2025-11-02 03:29:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3a7bc87d-a238-377c-ad07-5c0e70039c1e | -9.11057 | -40.60809 | 2025-11-02 03:29:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1d81d9c-1707-3dd5-853c-4ba1eef66840 | -10.73469 | -46.2368 | 2025-11-02 03:29:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1b6a4c5-1fd8-36d7-b540-a4ebe386c534 | -14.0356 | -43.4666 | 2025-11-02 03:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| c31ed7f3-b8df-3a57-b15f-7ce79529eda7 | -14.0155 | -43.4943 | 2025-11-02 03:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3f472d81-5446-30e3-bd92-b6ad3bb7a1de | -14.0161 | -43.4703 | 2025-11-02 03:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 80cc3ec7-6adc-33cc-a7b6-1ccc2af2dbe8 | -14.0351 | -43.4906 | 2025-11-02 03:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 5bc3f105-03c6-3fbc-9c94-2504664acfb2 | -15.86201 | -42.05773 | 2025-11-02 03:32:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fedc8af7-c2c1-3635-9a9c-aa9464dc4938 | -15.2968 | -42.96309 | 2025-11-02 03:32:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 250940a1-056a-38d9-8c89-2d3494c70f4c | -14.65928 | -46.61602 | 2025-11-02 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bf5d465c-a909-301c-9e2b-59c88f7be157 | -14.02097 | -43.47934 | 2025-11-02 03:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 72a7636d-6a9c-344b-8957-21fdde390972 | -13.312 | -43.45832 | 2025-11-02 03:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff135abe-3243-35c6-a130-313b37f4841c | -13.31675 | -43.46318 | 2025-11-02 03:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d2a608b3-e060-31a7-a580-7c917acf38a0 | -14.20726 | -47.81336 | 2025-11-02 03:32:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05b70796-749e-3b1a-b352-2c011aafb932 | -15.78297 | -41.46587 | 2025-11-02 03:32:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 450f8292-b96b-3390-bd2c-8b9577bec0f5 | -13.72069 | -43.63956 | 2025-11-02 03:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| be194f85-4e6b-306a-a23e-43d6ac4b2bc3 | -15.3249 | -43.89308 | 2025-11-02 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c678810e-47df-33e4-9e60-efe6409aabbf | -14.01951 | -43.48652 | 2025-11-02 03:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| dfd07acf-4aed-39d8-940b-62b35598ffbb | -14.65873 | -46.6224 | 2025-11-02 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19769dd5-036c-3583-a349-0d87de281489 | -14.02639 | -43.4805 | 2025-11-02 03:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 23e683c5-be7f-311f-800e-d9031021d228 | -14.20549 | -47.82132 | 2025-11-02 03:32:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8b04f89-7b95-36b4-86f8-2fdf6e25d850 | -15.82778 | -43.27301 | 2025-11-02 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2d81424-ce40-3328-b88a-410b6a240c06 | -15.32492 | -43.88866 | 2025-11-02 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 129d0c47-3e40-3205-82fe-18455b0df894 | -16.85429 | -40.69817 | 2025-11-02 03:32:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ec997106-7b22-3961-bc95-cd3f06712d85 | -13.31603 | -43.46685 | 2025-11-02 03:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2c95eaa7-0dd8-316d-85b9-9ccf09a5f007 | -15.46666 | -43.20347 | 2025-11-02 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c8d2494-436a-3978-b8b4-c30b1332826c | -15.8135 | -42.00124 | 2025-11-02 03:32:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| eba55288-0723-323a-addc-46793ff1e7f7 | -15.46695 | -43.20474 | 2025-11-02 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 87e092b9-94fd-3685-bc61-74002d6b6897 | -15.32568 | -43.88937 | 2025-11-02 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df857103-2c02-353e-826f-ac4922a9f412 | -13.31748 | -43.45949 | 2025-11-02 03:32:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6fe15979-3af9-3add-8ac8-870ea906134c | -16.85004 | -40.69705 | 2025-11-02 03:32:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3edef5f8-e267-3652-9fd7-28514a1f6bfc | -15.46601 | -43.20673 | 2025-11-02 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2cb23ea8-1845-38f5-b077-a74d1ac5806f | -14.02493 | -43.48771 | 2025-11-02 03:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| f091cbb5-13b4-3bee-bba3-93d4fbd8c9ab | -13.31054 | -43.46568 | 2025-11-02 03:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e79f55f-8da1-3804-a46a-cfac86bf5674 | -14.0217 | -43.47573 | 2025-11-02 03:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |


[Clique aqui para ver as próximas entradas](README6.md)
