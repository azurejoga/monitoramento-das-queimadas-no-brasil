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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8f77e11-e5aa-3827-a1dd-f0681604c101 | -11.09788 | -48.28102 | 2026-09-22 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84f1474f-534a-3ad9-879a-af7c5ba2cafb | -5.12274 | -46.18512 | 2026-09-22 04:02:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbd7c147-afd8-3266-a1a0-b13f31d581cc | -11.43766 | -47.33438 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39cf794e-36a8-3fc9-96c4-64cf37f592fa | -12.84486 | -44.33593 | 2026-09-22 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e87d38cf-36f5-3f77-8f78-1ec2f0ff5334 | -6.66837 | -47.37211 | 2026-09-22 04:02:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f92d87b7-8d5f-3d9f-8cb8-6c71fa0db391 | -12.84104 | -44.33524 | 2026-09-22 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56ac25e5-993f-3537-a46a-ea6008beace8 | -5.77853 | -43.76824 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f1a450a-afdd-3c55-a6c2-ff8e020ba9bf | -11.87061 | -46.84165 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1ee46bd-5d3a-3538-9b36-004168da8741 | -11.1629 | -51.12418 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55bfe324-011a-39cf-8364-28ca9bf98b37 | -9.89853 | -48.41345 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ca118bf-7392-3cd1-a854-70e32973e94c | -10.58299 | -46.52717 | 2026-09-22 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a2213ebc-aced-31c5-8453-bd16e29b7311 | -10.51825 | -36.97108 | 2026-09-22 04:02:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8e459968-4e2b-3f47-b2ce-80ccf41fd344 | -5.75571 | -45.08018 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 14221218-7182-3848-aac9-2bf5545dc57a | -7.40329 | -44.81392 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e783a178-1cd5-3427-874e-38797cd8cca2 | -5.62768 | -43.37201 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0183609f-1147-3751-8264-ccfd43f3dd76 | -7.16716 | -37.72333 | 2026-09-22 04:02:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 06511a65-e237-3409-b21b-66ee887081e2 | -10.90632 | -47.38472 | 2026-09-22 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c31a82b-fb35-390a-b3ea-fb1b820c940c | -11.14436 | -42.84055 | 2026-09-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 27d788c6-f6ac-37a9-8a0b-914abe09244b | -11.31889 | -51.36226 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c673435f-e961-30ac-b230-21bfcf11566c | -11.41348 | -45.37551 | 2026-09-22 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 723d8979-17ec-30d5-a5ac-bd5116e6f434 | -7.39898 | -44.81322 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b2a3c88-af21-3b4c-976a-ace3f714d343 | -7.38958 | -44.79073 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee76ed4c-d08c-3933-a14e-d4cd2965e0f0 | -12.01454 | -47.80548 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7929d0c7-4586-346d-861e-070bc47acf17 | -8.82891 | -50.49373 | 2026-09-22 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1a79fae3-e242-3027-b8ad-c78448c9a7cc | -12.55752 | -45.95639 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b7fd7b3-c6c4-39f2-9301-c996d965cb4c | -11.32504 | -51.36357 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aee93100-59cf-33f0-b5f6-703310343faf | -5.85349 | -49.78008 | 2026-09-22 04:02:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58d7b5c2-5aee-3c83-996f-4f6eef121d25 | -6.78326 | -48.67286 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a052353-e466-3ab1-84b9-82aef34da1ab | -11.87971 | -46.84347 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 27ddbfc0-fe83-3fba-bbeb-04478101e731 | -6.57057 | -44.90265 | 2026-09-22 04:02:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fd183c1-84f4-30b5-a9f6-13865b1f42cf | -8.78994 | -44.27263 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f4ce8d7b-fa0e-3933-acce-4034eda1f4c7 | -10.86333 | -50.16127 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c4a74ec-f609-3a26-a281-93f47f79ca09 | -5.73598 | -43.71901 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3bc911c-b2ef-3bdf-93c3-1194857151ab | -11.47163 | -47.74089 | 2026-09-22 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b7fbd4f-f164-32e4-8b7a-0d0f45fb75a2 | -8.02543 | -44.8278 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84fa6733-354b-3936-b0a8-a861e7efe5fb | -8.0297 | -44.82848 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1bbf690-40b2-3c79-a312-368714e055fc | -9.61932 | -43.94193 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1dbaafc4-225c-3754-a57f-0a97e0efb161 | -8.82801 | -50.49841 | 2026-09-22 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d29f2d15-2650-385e-b129-1ab645f18bfa | -7.3997 | -44.80902 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adf041b5-ec17-3649-b82c-605b2a673496 | -11.40911 | -46.78516 | 2026-09-22 04:02:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7106e6b2-9f5f-3ad2-99f5-d9416b26d5fa | -7.16126 | -43.44088 | 2026-09-22 04:02:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 60fb3ab6-1dc6-3fb1-ab2a-50effc7bdfb4 | -9.58817 | -47.778 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 895f5671-c304-3537-80ca-0ad0d98fd063 | -6.21571 | -45.36805 | 2026-09-22 04:02:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e16086f-20b9-3b00-ac36-38206af816fe | -5.74969 | -45.08847 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 64068748-d93c-3cf4-9fda-5cc88174092e | -10.38181 | -48.91123 | 2026-09-22 04:02:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6697865e-a7fa-391e-abcb-1435cf79209a | -7.54704 | -47.32628 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a635e3d-f119-3b5f-9bb9-cce84105ccf1 | -6.44401 | -48.45365 | 2026-09-22 04:02:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4702aff-0df4-31ad-9934-ee8ec809f5f0 | -6.71491 | -43.98127 | 2026-09-22 04:02:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 855f1652-da10-3d5b-b162-87191d821f97 | -8.79398 | -44.27343 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 32fdd26a-413d-3e3d-9e95-c7cb89214ec1 | -5.75946 | -45.08538 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a8e9b849-16e5-3392-bef1-22f71fa6da91 | -11.86972 | -46.84641 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4f56a90-3473-3e20-9d87-6d3e86e9228c | -9.71932 | -47.76712 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84fa55b9-f27b-3917-b12b-96578e884f3a | -7.34735 | -39.88636 | 2026-09-22 04:02:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3f2e1b80-565b-3ea0-ab59-7066eed80fce | -11.15259 | -51.11213 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a6afb765-4c74-317c-a4b9-ce7e5e316671 | -7.3519 | -45.34311 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 24efe7b4-1c42-3035-9af9-6cb52b819d25 | -11.33924 | -43.3754 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2ca4d03-8966-3225-8554-97a4f5970dca | -9.29028 | -44.37529 | 2026-09-22 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 727ed7a4-eb38-37e6-bace-9b3266444078 | -6.97415 | -47.50275 | 2026-09-22 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 865c7a23-9426-3942-8e39-cd8319b13b8d | -6.71903 | -43.98195 | 2026-09-22 04:02:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f431770-8a58-305b-94bf-1d40da039c46 | -11.02839 | -48.32744 | 2026-09-22 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c76141bd-b2b4-3e96-894c-6d97ce4db6a4 | -8.10884 | -44.44506 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d339e9b-0b60-3349-a41f-2d615a08056f | -10.5611 | -46.72903 | 2026-09-22 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 700cd0ad-aba7-3e0e-8a75-cab7ddfb2968 | -11.14128 | -42.79226 | 2026-09-22 04:02:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b35f02e9-2cf3-3986-9e02-9baa9b3478c3 | -10.01815 | -45.20392 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ede6a6d-6434-3530-bb94-0517b1d55659 | -11.84152 | -46.82034 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bba18ca0-4fd8-30c8-ac73-3f7978d018ae | -10.90725 | -47.37951 | 2026-09-22 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1978634-e78e-336a-b829-1d30e45d3fcc | -5.82725 | -44.132 | 2026-09-22 04:02:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b0e2dc7-efb2-3e82-95e6-b5853090b922 | -9.61846 | -43.94696 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ff2897c6-160c-31a2-af07-1b75a4c49395 | -13.08439 | -41.07896 | 2026-09-22 04:02:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5539ad23-6358-31ff-9532-eb78053fb2d1 | -11.14577 | -42.83211 | 2026-09-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb90fdba-75a6-31fb-b795-4455f07a71e1 | -10.54945 | -43.96706 | 2026-09-22 04:02:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8cc3955-96df-3f9b-b579-e1d7b470251a | -7.13369 | -42.07099 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a966fbdb-d6ff-3489-ba4c-c0486db38a12 | -12.56105 | -45.96129 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e007adc6-5384-3a48-82a0-c14f7c3bbaff | -8.09762 | -44.43582 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc335a77-e6f6-3290-8cee-86d6f323e1ae | -6.54863 | -45.56818 | 2026-09-22 04:02:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a97b3273-fa4e-3967-aa6d-3df7853e2d34 | -6.88354 | -41.69656 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1bf90654-d934-35f0-baa1-208aed24dac2 | -8.30519 | -40.60282 | 2026-09-22 04:02:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4c671171-2b61-3c76-84ac-5fb303364f06 | -11.15867 | -51.11343 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 390bf550-31ab-3f8f-908c-624d56519b92 | -6.57996 | -44.14923 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ecfeb3be-447b-38f7-9a57-c70d18994617 | -6.28906 | -47.65616 | 2026-09-22 04:02:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d36816cb-c93e-3b73-a895-e2c9e3121d2d | -12.2431 | -43.70248 | 2026-09-22 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0a1d43d-1bc3-37e2-a97f-0232457ff828 | -5.39299 | -42.95378 | 2026-09-22 04:02:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8db6e42b-d5e4-3eac-ac5a-68eb98f749d5 | -10.02162 | -45.20887 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6458f55a-953e-3d7c-bfe9-40ffc3606aef | -6.5793 | -44.15305 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e419cd6f-858a-399d-836c-947681bc7a57 | -8.111 | -49.58652 | 2026-09-22 04:02:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e8772f1-0d14-3657-8a84-2331c0ba336c | -6.84589 | -43.71947 | 2026-09-22 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fac7b84-93cc-3579-a8f7-d3f2301045cc | -8.83421 | -49.24054 | 2026-09-22 04:02:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad4cf0ae-0077-3943-9a46-3550417e8fc0 | -7.13595 | -42.08011 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3feb3d77-c8f2-3e5c-a8f4-eaa8158909f3 | -10.21081 | -44.15334 | 2026-09-22 04:02:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be5b2055-e200-37fd-bc82-c88a51706e28 | -7.06659 | -43.67273 | 2026-09-22 04:02:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4ea11be-1743-37a8-8b59-05699a0cf9c8 | -11.67833 | -43.45665 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44f55c09-2c73-3828-ba24-48e56eda4e40 | -6.78022 | -48.67343 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7c0ff85-2fd7-3b0f-938b-8c57523ccc70 | -12.10194 | -45.65877 | 2026-09-22 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5b92882-5418-3fa5-b79c-50ac5398b709 | -5.83118 | -43.84951 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8628ff09-b33e-3a39-a83b-1fec4b020b11 | -8.91953 | -50.90367 | 2026-09-22 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9493559e-f2a9-31c1-a218-fc8084b552c4 | -8.41369 | -46.86684 | 2026-09-22 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcd13b17-816e-3602-9b2b-1aa5761c185c | -6.86702 | -42.86831 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e1666966-da59-3540-a8be-f13f90bc6b99 | -9.23772 | -46.16489 | 2026-09-22 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c5ddf2f-d226-38cd-99a6-bb70b2542722 | -6.58062 | -44.14542 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ac61ef99-959d-3f1a-9c7a-c05d53599bd4 | -11.4397 | -47.34963 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README38.md)
