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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8361237-725a-349b-a325-c7569ce94d46 | -5.7758 | -45.0599 | 2026-06-26 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a076e3d8-2e2e-3c1c-bda8-ea4f4a092820 | -11.7798 | -46.4367 | 2026-06-26 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| ca20d6af-deed-329f-9efc-cf8d06764cb0 | -10.3916 | -56.7533 | 2026-06-26 03:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| bda84f9a-69bb-3bbf-9057-71bbf6240aca | -10.3916 | -56.7533 | 2026-06-26 03:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| c1ad55e0-e4b3-3108-9da3-fe979775952c | -11.7798 | -46.4367 | 2026-06-26 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 517231df-e854-33a8-92e2-69e535d1e291 | -5.7758 | -45.0599 | 2026-06-26 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d9bf0b1d-46d6-3308-b3b1-2df6e60219e0 | -11.7794 | -46.4594 | 2026-06-26 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a6cee8de-aadd-3066-8f54-234710041bde | -5.7945 | -45.0586 | 2026-06-26 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3d8e508a-565b-3164-bb6a-dfc7a6fdfd72 | -13.742 | -54.0475 | 2026-06-26 03:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 695a3f88-c1c6-3036-b5b6-32235df026d2 | -5.79268 | -43.89012 | 2026-06-26 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3bec6afe-26a0-30be-b174-8e116498f40e | -4.85592 | -42.94733 | 2026-06-26 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bbcfdd1-eeff-3b09-b009-299140ae3b2c | -2.95315 | -39.92266 | 2026-06-26 03:53:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b2bff1ef-e57a-31d8-b2c0-a1de2f564b66 | -4.35458 | -47.76199 | 2026-06-26 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a95d32c-7811-3b04-8785-0d629ed59b4d | -5.32939 | -44.69425 | 2026-06-26 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2a7cb283-7e74-3b86-9c5f-6b61b252abcf | -4.40833 | -40.69236 | 2026-06-26 03:53:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 144fd416-df20-32fb-8092-33d447304005 | -2.9514 | -39.92294 | 2026-06-26 03:53:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 32ac163c-f85e-394a-95fe-22de6494a8fe | -4.14578 | -43.65897 | 2026-06-26 03:53:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e9fc7955-99bb-3c1b-b8b0-65818c96917b | -5.94384 | -43.47186 | 2026-06-26 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66aef72e-668f-3878-a8ab-d2183a9e62cc | -3.04044 | -40.12386 | 2026-06-26 03:53:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9067db28-6365-3db0-9377-e77e5ba8494a | -4.14151 | -43.65828 | 2026-06-26 03:53:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 918b4000-db8e-383b-98b1-f15f8f771519 | -5.78769 | -45.047 | 2026-06-26 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9a2ed66e-4111-37d2-a5ee-2aaa01ba8972 | -5.78155 | -45.05563 | 2026-06-26 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f2e2c81b-68c8-3921-874a-e0afa1ff4b63 | -4.94778 | -48.24557 | 2026-06-26 03:53:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fcd2a8c-18cd-3f64-b959-8632c4538f33 | -4.94199 | -48.24479 | 2026-06-26 03:53:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1ab930d-3120-38a3-9764-01b5dab6b26e | -5.32809 | -44.69004 | 2026-06-26 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| cdeaa705-5af5-3345-b9fa-3de454030ba0 | -4.98439 | -37.23069 | 2026-06-26 03:53:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3459d877-f05a-3396-b4cd-2a72ca93bc41 | -4.94223 | -48.24871 | 2026-06-26 03:53:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60829995-bc44-334b-8903-9c20dcaed9b7 | -3.39155 | -40.42507 | 2026-06-26 03:53:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 683c3311-112d-381d-8181-eca2ce597aa4 | -4.85533 | -42.95087 | 2026-06-26 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5640189c-82fb-3066-ae30-d90188410315 | -5.93973 | -43.47116 | 2026-06-26 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa7aea86-a7f8-3952-963f-89453db799c9 | -5.77616 | -45.05966 | 2026-06-26 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b74ebc2a-a855-3e05-a56f-9754cc5c8d33 | -4.98108 | -37.23018 | 2026-06-26 03:53:00 | NOAA-21 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 304f8dec-1501-3fa2-877a-fe47dd65a04e | -5.78076 | -45.06035 | 2026-06-26 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 304de39b-2702-3c57-b9fa-e031a4195943 | -5.78535 | -45.06105 | 2026-06-26 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| eaa89993-612b-32eb-af32-1b45b2eec2ab | -5.79072 | -45.05712 | 2026-06-26 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| e2444200-16c2-3ad7-bd2c-0df5dbd32789 | -5.79336 | -43.88621 | 2026-06-26 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5253639a-2a70-3024-acd4-46be3faf44e5 | -3.04107 | -40.1199 | 2026-06-26 03:53:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 28508398-1dfb-3e44-9a62-ced552cfda6a | -4.63349 | -43.05136 | 2026-06-26 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaec69e4-ecd0-38b2-97db-d924154f2959 | -4.34892 | -47.76118 | 2026-06-26 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21b84d2c-64bf-3326-9e71-f3526051d047 | -5.94034 | -43.46745 | 2026-06-26 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92d142ca-e084-3a4b-98f6-8b05c3cb066b | -4.94129 | -48.2489 | 2026-06-26 03:53:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcb52beb-ed6a-3bfd-b935-1e679ef9142f | -5.94444 | -43.46815 | 2026-06-26 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6036c9d-0605-32d3-8f67-07f7c9690ebd | -4.85426 | -42.9506 | 2026-06-26 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a24a6fd7-4b44-32f3-a612-fc9d9039871c | -4.66425 | -43.22192 | 2026-06-26 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fbc22b0-789d-3329-9828-bc4e3287752b | -5.78614 | -45.05634 | 2026-06-26 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 2b29b19b-19a3-3d89-97bc-3645d59284ce | -5.79333 | -43.88612 | 2026-06-26 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1deb41ab-3674-3566-952b-3fc15c016671 | -4.85482 | -42.94706 | 2026-06-26 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b52c9b1-b517-3100-a784-2cd09e8cf454 | -5.79268 | -43.8902 | 2026-06-26 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 231d0a20-f9ce-35d3-bb2a-66d2c14edd65 | -5.79613 | -43.63203 | 2026-06-26 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e04a2281-cb3d-3bf2-b3e6-2eaf0fe0bb3a | -5.32566 | -44.68905 | 2026-06-26 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7c8e788-8c3f-3bbf-8f10-97b4085779ea | -5.04551 | -43.26424 | 2026-06-26 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f7c0d92-e9c2-383c-999e-dfc7d2dcf8cf | -5.78692 | -45.05167 | 2026-06-26 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f067d1d9-f8fd-3288-a0ae-56956ac275b5 | -2.94966 | -39.92212 | 2026-06-26 03:53:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ebc99c8a-d68c-327c-8293-e3377368678c | -5.78233 | -45.05094 | 2026-06-26 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 617eac49-24a4-30e4-83de-9571b95e40be | -5.32735 | -44.69457 | 2026-06-26 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 916c834e-b228-3152-8205-12b506f62ced | -4.94297 | -48.24457 | 2026-06-26 03:53:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f4442a8-0a5e-3fa6-b2d4-ef7f67b50df3 | -5.33017 | -44.68972 | 2026-06-26 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0f795df0-c90b-397e-a09f-f57c1ab058b7 | -4.98385 | -37.23416 | 2026-06-26 03:53:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dec3ba67-6880-3e36-a679-8f10ea51f4b3 | -4.94704 | -48.24997 | 2026-06-26 03:53:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72388434-377d-30ba-b03a-9d8f5ccd3772 | -13.37269 | -44.21321 | 2026-06-26 03:55:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44909518-0d23-3021-930f-3dbdd26bb061 | -8.1346 | -47.88359 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7535cb30-edf4-3f64-931f-61e65c3963e8 | -6.98885 | -42.89362 | 2026-06-26 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7b15cb60-e0c4-3e0b-abd1-e36e03d9b689 | -12.76123 | -44.50003 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b48d937-4bba-3af6-8a6d-c48cf063386b | -9.18634 | -45.32221 | 2026-06-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15e74630-e27a-36be-8f53-91383f0d76b1 | -7.75074 | -44.61913 | 2026-06-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6f210e35-a2f0-3d2e-929a-55b309b1fc21 | -7.62969 | -47.29626 | 2026-06-26 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ea1fae4-d3bd-3b32-bdcd-53b33c2a6f7d | -8.13593 | -47.88684 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e36f08d3-7f69-333a-b15a-c613e3864b37 | -8.49398 | -44.74829 | 2026-06-26 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d21600a-dd77-36e1-ae37-c9cbc647480b | -9.00702 | -47.99903 | 2026-06-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ed351eb-057e-3cbf-9feb-426acd7018a2 | -8.22788 | -47.12448 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| feb1e0e0-0a1b-3e79-a93c-96f42ea2af5d | -12.76212 | -44.49486 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af420f39-faad-3f32-972d-a12df714c160 | -11.77532 | -46.44929 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a39fa041-02b9-3bb2-ac52-8c7b2b2b6253 | -12.87103 | -44.35339 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3aa1b4e5-262f-35ad-9316-8695fe0f99da | -11.91555 | -43.4076 | 2026-06-26 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a171c93-f0f9-348f-9260-0da3a3162823 | -6.97554 | -42.90152 | 2026-06-26 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f91f4d25-c2fa-394f-b2e3-bddbc88b9a04 | -9.37106 | -50.54363 | 2026-06-26 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d95be737-b7d4-3f9d-b1d2-614d4a82f424 | -11.87613 | -51.73003 | 2026-06-26 03:55:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f554752-a9b1-3cc4-ac5a-af7387311e1c | -9.13023 | -47.64771 | 2026-06-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e503bb1-8eef-3090-a6dc-847b05877311 | -6.94347 | -43.66788 | 2026-06-26 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1883db7e-caec-3a45-a7ef-420bbcf3586e | -9.37012 | -50.54849 | 2026-06-26 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 81bba9fb-032a-3a78-a239-58866a4f1eb5 | -9.41021 | -50.6736 | 2026-06-26 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e16d0f7-b576-3b5e-9c02-e059001afd10 | -6.93877 | -43.67079 | 2026-06-26 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63a97224-4864-3150-9d6d-f63b2cbaea9c | -11.7771 | -46.43961 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 7026da7f-8c81-3298-85ac-fff32054c050 | -10.10078 | -49.59454 | 2026-06-26 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e57e47c9-05dd-3b9a-89c0-96d52e3bd73d | -8.25893 | -46.22205 | 2026-06-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d2066ed-4e35-32af-87e3-6643948b7f4f | -7.00362 | -42.78048 | 2026-06-26 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 09238484-dc04-391f-961e-1980a8d128fd | -11.90886 | -43.40171 | 2026-06-26 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b138056f-50bf-3253-bc5a-a6ccfdf84eef | -6.30054 | -44.65417 | 2026-06-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d4baf10-45fd-34df-983f-c81d4499e6b2 | -7.6503 | -37.12081 | 2026-06-26 03:55:00 | NOAA-21 | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 195ccf05-8873-38dd-9d14-4049bed8ecb4 | -10.38869 | -50.13347 | 2026-06-26 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1441b71-fb6a-3240-a1cf-eb3911585f59 | -10.54211 | -47.71496 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18fb98f4-c130-373e-97ab-8150002a8c05 | -8.01479 | -49.64906 | 2026-06-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeb4e28a-9c58-38ee-b551-65d6f413f72c | -6.50426 | -42.22797 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8bed7ab1-9eb2-3fdb-aeb5-c946d4279f66 | -12.51469 | -48.27183 | 2026-06-26 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e572470-8ece-327b-87f5-3542f067cec1 | -12.87189 | -44.34838 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| faf3fe18-19f0-3268-8546-fc4a4ff356c6 | -11.5438 | -48.26345 | 2026-06-26 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab847149-36a4-356c-a866-388d3c43222c | -11.91259 | -43.40237 | 2026-06-26 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6df943b7-8df4-3bef-8361-e47945bb6805 | -8.4947 | -44.74417 | 2026-06-26 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7be5d11-9609-310e-b915-7732ceebf493 | -12.763 | -44.48969 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14dc8588-bd7c-362a-adcc-30df51d4507c | -6.50127 | -42.22272 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |


[Clique aqui para ver as próximas entradas](README4.md)
