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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d1c813b-dcee-30a0-b29c-259f1aa70e6f | -7.0452 | -44.369598 | 2025-04-20 00:40:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62d6430d-1992-3eb6-96d7-a4f915e5a528 | -7.0474 | -44.378601 | 2025-04-20 00:40:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbcd5160-27e9-376b-be80-dada4817b839 | -10.6288 | -44.412102 | 2025-04-20 00:40:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 19841f4b-a241-34d0-bb24-9051d872f5b5 | -6.5479 | -51.0966 | 2025-04-20 00:40:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a65b32ec-dab6-386f-8a29-903aeb692d7c | -18.360901 | -47.603401 | 2025-04-20 00:40:00 | METOP-C | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 292f7d87-f426-3681-a298-5834120135e8 | -10.6268 | -44.4039 | 2025-04-20 00:40:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e5f3ab3-bf82-374f-bb21-e51b69115e4d | -5.7136 | -49.128502 | 2025-04-20 00:40:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f9f8442-1bd6-3df9-a03d-ab361142c39a | -10.6171 | -44.4062 | 2025-04-20 00:40:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21ad0ee7-1562-32a7-9ec2-2efddd42ba35 | -10.6191 | -44.414398 | 2025-04-20 00:40:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e25a8fc1-c4f8-34d4-a9cd-5d67f6ccbe6e | -6.5805 | -47.327599 | 2025-04-20 00:40:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db8d7c1d-3267-392f-8509-953978dee48c | -6.5821 | -47.334599 | 2025-04-20 00:40:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccb6f28e-f8e1-38e5-854c-23d1a0c34cac | -7.0495 | -44.387699 | 2025-04-20 00:40:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6334b3e1-199b-394d-84cc-326e69e66b52 | -20.306499 | -47.740501 | 2025-04-20 00:40:00 | METOP-C | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd24e3c-ec2c-3f2d-a3b7-2bec655f0767 | -6.5515 | -51.1124 | 2025-04-20 00:40:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e40c643-ed4e-35bd-ae9a-946b30377803 | -7.0571 | -44.3764 | 2025-04-20 00:40:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 335683fa-3ce8-3b6b-b053-6f03841fc9e5 | -6.5497 | -51.1045 | 2025-04-20 00:40:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 544d25d1-d8c0-3a15-93ec-f1464e5bd7dc | -20.3048 | -47.7323 | 2025-04-20 00:40:00 | METOP-C | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 32b1d997-4dc2-3821-98ed-28c3b6f129df | -5.7152 | -49.135399 | 2025-04-20 00:40:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c97f7c9-e617-3b02-865e-a93e8a704ee4 | -9.1876 | -62.873299 | 2025-04-20 01:29:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3cac033f-414c-30e3-8b1a-08db09318154 | -6.03555 | -37.01122 | 2025-04-20 03:02:00 | NOAA-20 | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 00e6065b-c583-31fe-98bd-1bab307ea1d9 | -6.03645 | -37.00631 | 2025-04-20 03:02:00 | NOAA-20 | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 00098dda-e475-3867-a25b-acac195ec7a8 | -6.0372 | -37.01076 | 2025-04-20 03:02:00 | NOAA-20 | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 10f47529-6801-39e7-a788-2487c98d2faa | -6.03807 | -37.00582 | 2025-04-20 03:02:00 | NOAA-20 | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 57393f5b-3a83-3789-9d28-22bd92ae5728 | -15.47463 | -41.6498 | 2025-04-20 03:04:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6af6420f-a49b-3782-bf18-757cea9feef5 | -7.0855 | -44.38358 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e64ccbf-5af3-329c-a5e7-8162e14c9311 | -9.93453 | -37.18833 | 2025-04-20 03:53:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ac34df9f-ca5e-3922-8a66-e97a406a267a | -9.53335 | -36.89894 | 2025-04-20 03:53:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8b549a4f-f2a6-3285-800d-424c4ac894d4 | -7.07043 | -44.36873 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59aa53fb-2a04-35da-9c0e-3d0ccab37c24 | -7.07336 | -44.37732 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b4cb2a80-8bae-3549-893b-42315ecd0e58 | -5.50555 | -35.60131 | 2025-04-20 03:53:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ec2f363f-3a2e-36f0-a3e0-303c82d1cd5e | -6.60709 | -47.33335 | 2025-04-20 03:53:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f437fbff-983e-36e5-be59-bad1abb19cb3 | -5.79765 | -43.62034 | 2025-04-20 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bef470bc-a96b-3f89-be22-1bf9879dce56 | -6.04075 | -37.00773 | 2025-04-20 03:53:00 | NOAA-21 | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 21330fec-57b8-32e6-91d1-6d663256209a | -4.78207 | -38.57946 | 2025-04-20 03:53:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c5a152ee-954b-3be1-a3aa-e24f26c57a8f | -7.07764 | -44.37806 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e77d7544-fe2d-359c-b591-f64439dbe2f4 | -5.48554 | -43.33603 | 2025-04-20 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c12c906f-4c9e-3150-8f9d-f97f56e132a8 | -5.50391 | -35.60196 | 2025-04-20 03:53:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 18c3a9a5-54ca-3f35-922b-4ff69e9afed3 | -5.22384 | -36.14576 | 2025-04-20 03:53:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aef7f826-fe1c-3da1-93b7-f150b7fb58b5 | -7.08123 | -44.38281 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31d0dd7c-b3c8-323e-8b37-015835e3b196 | -7.06908 | -44.37662 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0a9c822a-5b2a-3405-b442-28331edc145e | -6.30486 | -46.05511 | 2025-04-20 03:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f679dac-2dfe-3924-93c3-b768c832a609 | -7.07404 | -44.3734 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| add66238-ed6b-3f25-a242-8928ebe4443c | -7.07831 | -44.37411 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7467095-0c9e-3f14-88f9-8554bd8f575e | -7.07269 | -44.38128 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d9bf19c0-2b54-3640-85c1-b85d76f4d0b1 | -7.06975 | -44.37271 | 2025-04-20 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 912c1b44-1faa-3196-9923-3fcdf993689e | -4.98283 | -38.60068 | 2025-04-20 03:53:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e939e273-fad1-36a4-9a18-e3851f03e181 | -6.60767 | -47.33006 | 2025-04-20 03:53:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 112c463a-15e6-33aa-9c86-bf60b5086b02 | -9.93396 | -37.19207 | 2025-04-20 03:53:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c3682883-7af3-3439-8944-f0a4293381e5 | -12.00234 | -38.16844 | 2025-04-20 03:55:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d4219435-d048-3e64-9bd3-7c03ad349909 | -16.3505 | -43.69852 | 2025-04-20 03:55:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a4f13c6b-4e52-30a9-b592-69572eec176f | -16.6829 | -43.88343 | 2025-04-20 03:55:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a96f01a2-28d5-38fe-8947-e4c701f3b299 | -10.12279 | -37.75293 | 2025-04-20 03:55:00 | NOAA-21 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf9602c7-3ff8-3978-9bef-2ffb0ac49fe5 | -10.64897 | -44.40543 | 2025-04-20 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90f30096-3fdb-381a-b616-4d01b76415b2 | -10.01308 | -38.57831 | 2025-04-20 03:55:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c84ed3bd-3285-31cc-8ea0-e3f83743e210 | -14.12184 | -41.67711 | 2025-04-20 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5c65e074-f514-35a8-9341-eca82a5e8d7d | -10.11943 | -37.7524 | 2025-04-20 03:55:00 | NOAA-21 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0576e06-497d-38e0-a01b-2a38e34ff625 | -10.64429 | -44.40835 | 2025-04-20 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b54c9bf-1d2b-32ca-a12a-b36550c3e0b0 | -10.64493 | -44.40472 | 2025-04-20 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 78dbe89f-bfc7-3a99-b5be-eecceb2b637f | -15.08067 | -48.94584 | 2025-04-20 03:55:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cf52a1a-be13-3669-a1fc-5d320ba38b89 | -12.41603 | -39.15207 | 2025-04-20 03:55:00 | NOAA-21 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb989dd5-76aa-3bf7-a6cd-4b1710fdc418 | -10.64834 | -44.40907 | 2025-04-20 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d352724e-9ca3-3566-b6b6-62eb0bd971da | -10.01254 | -38.58181 | 2025-04-20 03:55:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cedec501-f679-3ef5-be7a-1d114242e850 | -12.24404 | -38.28033 | 2025-04-20 03:55:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f35d9317-26ac-34ff-bae9-296a5c80c33c | -10.69499 | -37.04998 | 2025-04-20 03:55:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ad69c19-71fb-3592-bab7-60e6725d1d73 | -23.5948 | -47.43875 | 2025-04-20 03:57:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b79cba6-a1e5-3336-b095-12875b0e6bd9 | -17.09571 | -43.80434 | 2025-04-20 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7705dc9-1cb0-32fd-afb0-732dd99eb88d | -20.41821 | -43.55175 | 2025-04-20 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 73150f79-cc92-3f0b-9251-9e5218b6b4af | -20.32742 | -47.73324 | 2025-04-20 03:57:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b1e90431-cafa-3199-b270-d0fc1ae99bf1 | -19.97004 | -44.21873 | 2025-04-20 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af2041ac-d181-3a8f-8fbb-6c62b5aeac60 | -17.78174 | -42.80823 | 2025-04-20 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a1bbfc8-e36e-37b7-9af7-491e26d68d93 | -18.3818 | -47.60512 | 2025-04-20 03:57:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 259e2685-0b2c-3994-8d51-8977040f3a78 | -20.90071 | -43.81971 | 2025-04-20 03:57:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 07c8bf7b-c724-3efe-a707-c2f3d68ca5e2 | -17.59613 | -43.19817 | 2025-04-20 03:57:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c89b8d8-b29d-3b73-b573-4c063204f4d2 | -18.38613 | -47.60611 | 2025-04-20 03:57:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94d966c7-58fd-359e-ad36-1f218b4f8e5e | -19.83807 | -40.08336 | 2025-04-20 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9a44c2db-2c99-3233-b823-d4bc4a269602 | -5.48482 | -43.33459 | 2025-04-20 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83b655c5-76f9-3066-885e-d70d83e39124 | -7.06685 | -44.37608 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 241ccc24-b32a-3653-8746-a52702427bba | -6.61034 | -47.33081 | 2025-04-20 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32dca52f-4dbd-3563-8955-6da834a9cd0d | -7.07295 | -44.38062 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12672938-c22b-36d0-a453-9cccb62753ec | -7.0735 | -44.37713 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f868c2c-ceb3-3c53-a5f2-7cff04cf89ef | -7.07405 | -44.37364 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1942ab31-2d7e-36fc-8dcf-a01f1b3cd825 | -6.04089 | -37.00707 | 2025-04-20 04:19:00 | NPP-375D | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 031fefd9-5e08-32ba-8825-2b320fd53c9f | -6.60681 | -47.33023 | 2025-04-20 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a6fbbd2-1446-30e0-9f92-d05bf402eab9 | -7.29539 | -43.92633 | 2025-04-20 04:19:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52a48ad9-cb0c-37b3-8eb9-b7b82124d06b | -7.08294 | -44.38218 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15e9a898-3453-3ae6-96bb-1a522500239f | -6.30598 | -46.0521 | 2025-04-20 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cd2f2ba-7285-3311-b960-b7f5110ce941 | -7.07738 | -44.37416 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6510087d-5efa-3d39-9341-81a8e8c66806 | -5.48145 | -43.33407 | 2025-04-20 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 36a6e4c5-09b3-3d47-b1b3-9fc8ded7c253 | -6.04204 | -37.00582 | 2025-04-20 04:19:00 | NPP-375D | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fd17e7b3-48a9-355b-8efc-391a1994c120 | -6.3026 | -46.05155 | 2025-04-20 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 731258d5-1e9d-38ce-9cd1-700f45746631 | -5.65654 | -44.35381 | 2025-04-20 04:19:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7870ec59-2f93-3112-9bf5-869c013731d8 | -5.73843 | -49.12996 | 2025-04-20 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a3e4806-cf84-386b-868b-58c71d1db1f7 | -7.07072 | -44.37312 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe01e32e-e025-3565-8bfa-f893bb663de2 | -5.36584 | -49.19772 | 2025-04-20 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06029457-415d-31a7-8bcc-c591bd70bc4b | -7.07127 | -44.36962 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e42b1af-ec73-3c91-ab55-a754bc213516 | -7.07683 | -44.37766 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f73be743-7c3c-3312-80d0-a17f7ecab5a3 | -7.07017 | -44.37661 | 2025-04-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 706fb3e5-7760-3e31-9c7c-fb670aaaa991 | -5.79545 | -43.62206 | 2025-04-20 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c322aca-8643-36df-b2a0-49bf97fe1c6b | -10.64624 | -44.4088 | 2025-04-20 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32a31184-20ed-384b-a10a-a0cd2380b47c | -14.53715 | -49.1593 | 2025-04-20 04:21:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README2.md)
