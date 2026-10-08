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

## Dados Diários - Página 313

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bec120d3-36f5-322d-a734-cecb78fa1c2e | -7.57572 | -45.19751 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d4d7f784-8e8c-33f7-976b-406c23b67a5b | -7.86089 | -44.14742 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 51a1d593-1775-335d-92ce-84dea542db62 | -9.80355 | -47.81558 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f4646015-5654-3bfa-acdc-46d2b4c636da | -7.63514 | -44.37933 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 41dccfe6-1540-3ab1-8971-9168d7dddd15 | -9.82841 | -45.77504 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| fc9bc42b-2f78-3a71-9fd0-b732583ec267 | -8.04016 | -49.40652 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0126c16c-9c62-3c7a-8288-c93e158b539c | -5.49937 | -40.53983 | 2026-10-08 16:37:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b3a95a38-c593-322e-bf63-b9ce68a94ed6 | -6.52997 | -45.39395 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| e6842bac-74e7-3a65-855e-ee989acb2413 | -13.017 | -47.201 | 2026-10-08 16:37:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| ebbe4a79-f41d-395c-b91e-25796949cbbd | -11.86282 | -43.55727 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 231f122d-cec6-337b-97e3-1a4ed040f1a6 | -9.54062 | -45.6207 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a8ed91e-d28a-3011-b367-72bbb6be2476 | -5.74744 | -42.05543 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| b0569b29-d2b3-3c81-940a-09980bcb43cc | -7.51639 | -47.3338 | 2026-10-08 16:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| f608540a-b17c-35e8-bbbc-0450aa42e622 | -7.19423 | -44.33966 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c02f89bd-c1d5-334d-b3dc-ec59cef5048f | -10.86979 | -45.55169 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| c8942d77-d96a-333d-9dac-67badcaeede6 | -10.93039 | -45.39088 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 90bba6f9-ca9f-3d54-bcc8-3740c72c75e6 | -10.45577 | -47.29277 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| bca2068c-f866-3e66-a0f9-70d99077ad12 | -5.98245 | -41.35755 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 9c06ca0b-30ea-3dc8-a8ea-d7ccc6a5cf35 | -6.99984 | -43.44051 | 2026-10-08 16:37:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bb5d310d-cae7-3f35-9cac-4366c5fcdb90 | -11.07695 | -44.02374 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b2054fec-7ed9-3b50-8ff7-be19129f457d | -11.40996 | -47.5696 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 425139b5-adb2-3965-b284-659e27c358b5 | -7.12328 | -43.91294 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f4565fc0-48df-35ef-b3a0-db0d0e4cef97 | -5.51073 | -37.48675 | 2026-10-08 16:37:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| be86626b-0e79-3b33-b18e-962988bb329d | -11.20387 | -45.22505 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c112d7a1-ed17-3635-b995-7815142b21cb | -8.02061 | -46.96347 | 2026-10-08 16:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 258652a2-8650-3e38-9069-b0937e14355e | -11.20798 | -41.5778 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6dfdacf7-6d8f-3952-a3a0-75ba7e6cce94 | -7.31326 | -44.00755 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 81461cb5-53aa-3ccd-8c2d-a5a94bbdf0b9 | -10.91136 | -45.53446 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21283f6b-134b-35f0-a62d-2fdbfdf177bd | -10.43904 | -47.27546 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 536904af-e6af-3aec-bd64-b442d47837c1 | -7.06513 | -40.94588 | 2026-10-08 16:37:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 52bc2378-afa6-33c9-b5cf-b437e78b91b0 | -11.09082 | -44.02518 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 0a2eb7bd-345a-3983-90ba-69a9d9b71428 | -7.22453 | -44.26855 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d21886fd-2321-3e5f-98c1-19e0dfc9dfef | -9.37102 | -45.93433 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 861b414d-8f8e-311f-b3ba-e2e07a67e19d | -11.94175 | -40.35697 | 2026-10-08 16:37:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 43e7d02f-9e7e-3e82-b668-ffe6c6e43baf | -8.3323 | -45.04074 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 32c52848-0171-33e7-a25a-08a7b4c5bfec | -6.66817 | -45.3652 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 0a41b85c-628d-380f-ad9a-f07b97b890ce | -6.16485 | -39.44054 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fbea9a10-8919-3e66-a768-0a6c570ecda2 | -9.8988 | -44.85482 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| b124dd0d-13c3-316b-aa84-a47ce1682751 | -11.276 | -45.20901 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 8ea8b2e8-bf1d-3120-bcc0-aa6d69120862 | -9.23519 | -45.66542 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 45d9aa94-0e7b-3e31-8f62-6fbe983f893a | -7.18919 | -42.00171 | 2026-10-08 16:37:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 11174a4d-b3a2-399d-84a1-d26c6155b8cf | -13.20216 | -47.87424 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4bfb9397-ba58-324e-9c46-dfd05914eb9e | -7.32173 | -43.9949 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 52d1f8a9-4766-31d7-b7f8-c7ba00cc270a | -11.11544 | -45.69747 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 27a8e503-dce9-3302-bfb0-1b76f452b272 | -13.37408 | -43.88446 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d4e64465-93e6-3ce8-9460-5fe0339e805f | -6.55357 | -42.12383 | 2026-10-08 16:37:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b08dadff-e251-3fe6-a310-abffbdd1d468 | -6.79684 | -45.05493 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 06860ecd-644f-3cf6-a65d-32ab1b122054 | -7.30987 | -44.0081 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 147.3 |
| f6aa8f4a-8233-31fd-94da-c7d302c473f2 | -11.63609 | -43.709 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f0c144cf-db4b-379b-853f-5847dbf1f732 | -11.30962 | -46.68294 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4bd2107d-e7b6-3e5f-959f-1b1d23a77095 | -7.19024 | -44.31438 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af4a30ef-d83f-35c7-9c77-726b334c07c4 | -6.33368 | -43.34913 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 2cd25e4a-2a90-3787-ae9e-10bb5ebdfe11 | -6.33079 | -43.35362 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6b5dafcc-5c8d-3341-b470-64d11e6f41c5 | -9.79828 | -44.77458 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 210fb6ca-4b40-3acf-9cbc-b09bac8b4804 | -19.27929 | -42.00317 | 2026-10-08 16:37:00 | NOAA-20 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0e04c417-9585-35da-9b24-12977616d5eb | -6.79351 | -45.05544 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 68e62c0c-af64-305d-a62e-4acfda0e394e | -6.38264 | -45.78337 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f605c1e5-bcaa-3c6f-8916-8056a6cff063 | -10.15937 | -40.52826 | 2026-10-08 16:37:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 34d7c7ab-6240-3754-87bf-a1f5062aa4d0 | -11.48984 | -54.60961 | 2026-10-08 16:37:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 814e1bd7-fee2-3aa9-a4f2-8d8be096be71 | -6.22362 | -44.86137 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 996c48b7-145e-3339-bf07-cf38b636cde4 | -8.29341 | -45.74051 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 46824dff-98bc-399c-ab3e-569f401d2a6c | -9.83652 | -47.46654 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 46d11f03-c634-3d99-8212-5eaa59495fa8 | -9.13666 | -45.84264 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7af2f86f-e9b3-39b9-ad17-c0fb2063c837 | -6.97423 | -45.12643 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3370538c-a536-3c62-a22d-dcea8b3cb3e3 | -7.19028 | -44.33653 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95bf2d5d-825e-3c82-bf71-411bb62d192e | -11.95351 | -47.7673 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a321637f-3de8-321e-96dc-e98e4bf80375 | -9.27553 | -47.44719 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 91a25e51-de2c-3596-843e-2e1c2f146c8c | -9.89987 | -44.86181 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f6cd33af-4a00-31c7-8679-a00f3e9634e7 | -7.71453 | -44.73423 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| c89960de-9821-3a78-a54c-a197a0a32e5e | -7.02805 | -44.7253 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e4881c4a-36e9-357a-8edd-707d9bed77c3 | -6.52397 | -43.53986 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a3d8f1ab-e971-3257-b278-5877a3d82dd3 | -7.8187 | -44.57302 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| fe78c2ab-ed82-328b-8758-43f36847755f | -10.44677 | -46.87826 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b1ae902-03f8-34ad-b7c3-1bb747ab97a3 | -10.44132 | -47.29089 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 94a21a8a-fde5-390d-b765-f4a65e1b81bd | -17.06808 | -40.02299 | 2026-10-08 16:37:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.0 |
| f2f6cc5f-d808-3820-93d2-4b4f4bb442b3 | -8.10096 | -39.88411 | 2026-10-08 16:37:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 02fa15d5-d8e6-3ad1-9934-19ab6d116367 | -9.84756 | -47.84603 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4afb219d-c2eb-36e9-862e-7a493620dbe6 | -11.82147 | -39.19007 | 2026-10-08 16:37:00 | NOAA-20 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 786d77af-c70e-3665-b166-a0502e367648 | -17.73493 | -42.24864 | 2026-10-08 16:37:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5ac52c71-7f7b-3807-b125-ebfdbc8ee453 | -5.70179 | -41.72932 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fa8d4dc0-39be-3fb5-827a-1bdd6770a537 | -10.45594 | -47.28041 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 299328d2-3fa0-3119-bc71-9033d54dabf7 | -7.65022 | -37.6704 | 2026-10-08 16:37:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f5bfe15b-fcbf-3961-bfed-aff2fd29560f | -7.21723 | -44.33229 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90b2cea0-9f3d-3f98-bfb3-3aa8569e2373 | -5.71854 | -41.63723 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 5acf3dad-abfa-3a78-aee6-5c061a73dd6d | -6.36674 | -45.59107 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 252a3e28-3c9f-3aae-9356-ca50e5fdf673 | -7.13253 | -44.08559 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 152c2ce7-d0ab-343c-9871-2f499df30382 | -6.04105 | -44.38634 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8d4965d6-8506-394d-8151-b245465ada8d | -6.93377 | -43.66619 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7959e684-70a8-304b-9938-232de8cc4a57 | -6.93051 | -45.26182 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 48f3ae24-4208-3696-957a-aa9fa52238e8 | -11.83278 | -43.53287 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 956a3523-8750-3d3d-b633-775dc9435f50 | -11.09767 | -41.32176 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d4ccc4c8-9bce-3190-8d2d-4d7c0a2bff51 | -12.61372 | -44.54605 | 2026-10-08 16:37:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7f7c0944-25f7-379f-816e-bcd02aa866c5 | -11.08527 | -44.03334 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 9104929f-702b-340d-a90a-8aa8c7b7f69e | -12.15539 | -44.72165 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 35ff788a-aaba-378d-866d-3db84426257f | -8.84679 | -45.45318 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a98bdfc1-65c5-3980-9cf0-cb9bc794ace5 | -6.32655 | -37.75499 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 24.3 |
| a9a7f78e-d236-3679-9e11-85d0282006b4 | -8.53377 | -46.90655 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00bf4456-949f-3557-861f-f18c675863ba | -8.27858 | -45.73214 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e4d2eb85-40c1-3e6c-ab15-6e8c18920106 | -6.85394 | -39.46342 | 2026-10-08 16:37:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 1494aa7a-75b0-36c0-9471-5749ee0d652d | -6.22674 | -44.96957 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README314.md)
