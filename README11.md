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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2678dc91-f6a1-30dc-9d88-c8238e303196 | -2.49366 | -47.82158 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3cc80ce-13e7-3637-86c0-a060032046d5 | -4.16997 | -41.61379 | 2025-11-25 04:38:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a1eb18f9-a9da-3672-9e91-e1b7513cb8eb | -5.03634 | -43.26141 | 2025-11-25 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64433b9b-7deb-3740-90b7-42ab399be59c | -5.5688 | -44.97509 | 2025-11-25 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 270726f0-082d-3abc-8891-d35fc36ef99a | -2.99212 | -51.05983 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a078ed03-f4db-3282-a8b5-c3326a499e33 | -5.89669 | -44.5249 | 2025-11-25 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c579f5e4-f83e-36c1-afe7-122914375b79 | -5.03207 | -43.26066 | 2025-11-25 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e46ad4eb-8072-3ba9-b604-d75e866e5cde | -3.65681 | -42.77959 | 2025-11-25 04:38:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00982ca9-4402-3688-a151-a1dddefe92f4 | -2.94217 | -48.23202 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f74d990-2ba5-3c43-b95a-bb61030c1a8c | -5.41337 | -43.65913 | 2025-11-25 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1cf734c-90b3-39bd-a7f7-db2532bb22c5 | -2.88292 | -51.80623 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4613878-91e9-3e97-a06b-ba3866d965d5 | -4.30858 | -50.74398 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8188fef-ca15-3860-9c8d-6a2e256fdf12 | -1.20975 | -53.38519 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fba21b81-271d-39f9-b8e1-a69b247caf21 | -6.89186 | -42.84606 | 2025-11-25 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 19095ac8-618c-35e3-b6b5-26f1e7df635d | -2.55838 | -47.06446 | 2025-11-25 04:38:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf0e7157-0303-3536-aae4-6cd28e0f9e5b | -2.93995 | -48.2246 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83fe318d-d41b-326e-9806-a13c6de072b1 | -4.32876 | -45.76418 | 2025-11-25 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14621733-e8ea-36d1-b7bf-d78c06a3e99b | -2.49203 | -47.83202 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53781c9a-e344-36fc-8be1-b8e5276ef6f5 | -3.23242 | -50.58751 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cc88e043-cdef-3213-9c09-91835055afc3 | -4.46609 | -40.76021 | 2025-11-25 04:38:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ba2a04f-5cba-3456-8447-630f95180c72 | -3.02068 | -51.03697 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8c4d3df-ba88-363d-9e55-136985c08f32 | -4.74624 | -44.44265 | 2025-11-25 04:38:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f49c24a-5ab3-3e1e-bc54-927173c15588 | -4.48194 | -50.358 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06cc1945-6868-3916-9186-94292c8da072 | -3.69124 | -49.57804 | 2025-11-25 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37508df7-57fe-3e2b-8c73-79a0837dd067 | -2.93778 | -48.2384 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a4c14cc-b575-3cf5-ba45-273d81c1a1f4 | -3.56526 | -41.60682 | 2025-11-25 04:38:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f41769d-ebba-3ba8-8191-cdf787fc7099 | -4.66347 | -44.14815 | 2025-11-25 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51b2d04a-8f0f-3a02-b08d-bd90a677adcc | -5.31392 | -47.48645 | 2025-11-25 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a59272d-985c-35af-a660-892ec2873631 | -5.5848 | -45.18123 | 2025-11-25 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 554be785-65f7-383d-ae5d-ded2d15136ec | -5.90177 | -44.01328 | 2025-11-25 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4a28520-0611-3631-8317-0e9cf82e6722 | 0.65869 | -51.5407 | 2025-11-25 04:38:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bae8ff1-5c0d-35dd-9b96-250deeca2904 | -6.26103 | -47.04588 | 2025-11-25 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5de83f11-baf7-32e9-b0b1-0f4dd6583551 | -4.82065 | -43.82765 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 027fae45-0872-3a6f-90d8-ebfdc3a296f1 | -4.73041 | -44.73801 | 2025-11-25 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60a1b934-a7e7-3ad5-9c3d-1ad71fd5cc98 | -3.3601 | -45.56905 | 2025-11-25 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6885bcf0-7a39-3cce-8273-d09a3bc936eb | -2.9317 | -48.23392 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 22f6f165-2d82-3055-93ae-0c07d5c2bf91 | -2.37499 | -50.51114 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d435a1eb-a463-3b42-b6ad-971a2eb6b6c1 | -2.4363 | -50.26195 | 2025-11-25 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf923b25-4f52-3a12-a538-905b27277f38 | -4.35076 | -44.32773 | 2025-11-25 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e197a68-28a0-326e-b30c-3897bcb3e381 | -3.6035 | -40.98605 | 2025-11-25 04:38:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| daa13097-6d00-303b-b7c5-ef943d964976 | -3.83762 | -45.67781 | 2025-11-25 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4b29539-a0ef-3881-998e-9f899f2cfcc1 | -3.80545 | -49.50019 | 2025-11-25 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93c8a59c-3172-3ff8-b3ca-5c397db64b31 | -1.61531 | -48.6958 | 2025-11-25 04:38:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c579aa6b-1257-35da-be02-2df6dfe21cc6 | -3.27225 | -46.01551 | 2025-11-25 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84214e2c-8f1d-3a4e-b0ec-37322943cb84 | -3.94662 | -50.61988 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28d73523-b5fe-3867-8c81-a3a9121656cf | -2.93664 | -48.22409 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1142278e-37ff-3eff-8d5f-26b51acbcd2b | -2.43456 | -50.27283 | 2025-11-25 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9004547b-c82b-32e4-8eef-5343111b7c15 | -3.35595 | -51.54558 | 2025-11-25 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8828c414-24b3-3f35-be9c-71ee0d1ea338 | -2.49644 | -47.82558 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d007703a-323f-319a-ad0f-14c99ffba27b | -1.15008 | -54.21936 | 2025-11-25 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbd4f607-5bc9-31f3-a9b3-4375584dedc8 | -3.64865 | -43.932 | 2025-11-25 04:38:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4a39793-7aa9-397a-bbb2-4c0a18ce40ce | -3.21245 | -46.82677 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 558f4905-8494-35e3-b644-a30cbe6f2ca3 | -4.75232 | -45.10837 | 2025-11-25 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57f07182-5221-3089-a35f-06963477edaa | -5.04183 | -44.80119 | 2025-11-25 04:38:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abef9a60-b055-35e7-b8d2-69eb03e6c408 | -2.89333 | -50.23296 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba87de0d-f6b8-3791-ac86-2eb88fda6361 | -1.22223 | -47.71868 | 2025-11-25 04:38:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61347ec2-951b-3722-b4f6-38a1444d0db8 | -2.87903 | -51.78457 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abe634de-4115-3ab2-b482-b37ce47001ac | -2.43124 | -50.26481 | 2025-11-25 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a188c77-9b4d-3c98-add3-3a8236eac530 | -2.93279 | -48.22702 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9084ef46-4364-307d-83c9-2a4669b5f36a | -3.4516 | -48.81634 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b6d5dbe-e988-3124-98e0-b72d38a1e3c9 | -5.41644 | -41.08427 | 2025-11-25 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 661389b4-4a0e-3042-a63b-d086a94efd65 | -4.82942 | -43.82525 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c30f6526-252c-3f1a-8bc9-776374883948 | -3.39062 | -47.19086 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b617044b-c5aa-3b65-ad79-e0ca2284c1cc | -3.02822 | -51.03428 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ceb944e9-0cd8-3a12-b3b7-40be93a1e728 | -4.04372 | -42.51153 | 2025-11-25 04:38:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a032e11d-e84d-3e90-9e9b-22df67b0d139 | -3.45786 | -45.42247 | 2025-11-25 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 906879cc-4c6b-3798-956b-325c2f262ae8 | -3.83274 | -49.28516 | 2025-11-25 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92d04693-22ba-3833-a4ad-57226e43ced7 | -2.69712 | -51.86398 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de68e0cd-897e-3994-ad56-65f795d1bca0 | -5.63692 | -43.9266 | 2025-11-25 04:38:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa9fbc8d-5b02-330a-a971-4d364c46e106 | -3.82976 | -43.99117 | 2025-11-25 04:38:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bde5a759-3fa8-352b-872c-d29f39f86cbd | -4.81654 | -43.82703 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c0eb57d2-3ec0-34b7-b218-8f156a1cbba6 | 0.716 | -50.80368 | 2025-11-25 04:38:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75fb6194-1507-3a5c-9677-36b68a2101ae | -5.03471 | -43.2635 | 2025-11-25 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84fc5bc5-c48f-33cc-b316-d109b176173b | -3.58169 | -50.28934 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a2e6d6b-67f7-3375-b303-d2a44a82d50d | -2.48288 | -47.827 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9925df5-8e6f-39ef-af89-538e30ab6fd4 | -2.87866 | -51.80978 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdd4d1d4-c785-33ba-ab33-7f1f99d62d6b | -4.46564 | -40.7633 | 2025-11-25 04:38:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed0714c9-9fa2-3d85-b51a-e41de0e66354 | -3.4164 | -44.22559 | 2025-11-25 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3afca11-e417-3086-89b8-2666119b8b34 | -6.27613 | -39.68432 | 2025-11-25 04:38:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9f392516-d5b0-3a00-94eb-0e05e94380e6 | -5.99898 | -44.72052 | 2025-11-25 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 188d3b7d-5388-3fa4-a4e1-d06e25fc317e | -2.87932 | -51.80565 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 024566e0-1155-3151-9fa6-3f3cd784ca00 | -3.80737 | -49.97955 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d6344ac-d058-3a34-8f04-29b8ad98fcfa | -4.61022 | -38.68088 | 2025-11-25 04:38:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 035c83cd-2367-3594-af14-266dc3f0dd9c | -3.20503 | -46.82941 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| cef1e230-c2e0-330b-9160-f7da945498bd | -4.75277 | -45.1057 | 2025-11-25 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db161146-d833-35f4-8d02-5b8fde708576 | 1.3622 | -50.67645 | 2025-11-25 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ed2c5a6-ff47-3bcc-acc5-70db140c65de | -4.06583 | -44.59219 | 2025-11-25 04:38:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0974ccd7-5626-39d1-92a6-14755fc91382 | -2.93886 | -48.2315 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87a60618-9e4a-317c-9df0-34b22ba035d2 | -4.33392 | -45.63526 | 2025-11-25 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81862d7f-e471-39bf-8f11-a1af5b7d2058 | -6.6882 | -43.94766 | 2025-11-25 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f8a1244f-dab8-3e7b-aa64-0e5d4ea75687 | -2.49589 | -47.82906 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3cfcdbc-bf5e-3135-a40d-5750f50b5caa | -2.48123 | -47.83743 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c6b08e1-f3a5-389c-8430-1d9f9bc742d0 | -6.1179 | -42.94864 | 2025-11-25 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 60da2500-a4d1-34e8-9255-f7cc427d2c14 | -4.04306 | -42.51588 | 2025-11-25 04:38:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7e37644-67e7-3ea7-a439-e82d41de43f5 | -6.68344 | -43.95098 | 2025-11-25 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0a5eb468-ddcf-3d7c-b362-45a7123fa076 | -3.65547 | -50.20562 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ece11089-1b43-365a-bb0c-e729db81b782 | -2.48565 | -47.83099 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d672df7e-de28-3ee6-815e-4e665c86fc8a | -2.47956 | -47.82649 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2dd487f-503e-316d-9cf8-980b33b4d866 | -4.4825 | -50.35445 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e084a340-4323-35ac-8993-46fc68529eaa | -4.33667 | -44.34105 | 2025-11-25 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README12.md)
