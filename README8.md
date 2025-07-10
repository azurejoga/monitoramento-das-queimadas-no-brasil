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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d10e4af5-73c3-3a7c-b25f-5f4e81239f85 | -6.24462 | -43.37139 | 2025-07-10 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acbe41dd-6500-39d5-82b3-f792ebc6e5c2 | -5.25072 | -44.45465 | 2025-07-10 03:36:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 23e9af46-1e75-3a6f-9245-9cae155f9a9c | -7.01204 | -43.49529 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7c16fe6-c9dd-3ea6-b11a-67921336d413 | -6.67284 | -43.77129 | 2025-07-10 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e206b5e-cd76-3fd1-92c6-1e68a4132917 | -8.5056 | -43.29517 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 0db9ba17-020c-37cb-9d98-2f9ebc963b90 | -6.98898 | -43.4982 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e1645b2-f9ca-35cd-b62d-c93d8bfa9d52 | -6.64938 | -43.19684 | 2025-07-10 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e3e08ca6-ccda-3878-b710-9e5a8fce4201 | -6.14562 | -45.87544 | 2025-07-10 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8bf8a1a5-ea64-3a87-b182-262630cb403d | -8.51197 | -43.31987 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 613f2f68-eeed-349c-9f82-59b38a93c8f7 | -8.49856 | -43.304 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 29d96afb-0192-3556-9571-2b9f4e4cca51 | -6.64996 | -43.1935 | 2025-07-10 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0649e616-3041-3eec-8b24-a068680cb3e5 | -5.20353 | -37.66903 | 2025-07-10 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43d25aaa-dd0d-30db-bcf7-14d0c6830c79 | -8.50501 | -43.29842 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 53813353-c691-3922-be29-793ecb506090 | -6.85708 | -42.80775 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 011c7856-f961-3995-a158-8521a219f55c | -8.50491 | -43.32874 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| c02ee967-6c9c-324c-868b-188185f37649 | -6.94217 | -43.02805 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 088850c4-4532-34fe-9225-ac2ee5a65d67 | -8.49975 | -43.29747 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| e52e4f91-d9b5-3364-a528-04c37e4cfd77 | -8.49628 | -43.28676 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 6975e34b-fc47-3842-8072-a6e58d0806c3 | -8.49805 | -43.27709 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 6a7c4712-94cf-3b2e-9f12-893a5e495075 | -5.35105 | -45.26898 | 2025-07-10 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b6cedc8-9fbc-3bd9-9658-62a430cec575 | -8.50389 | -43.27486 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 776af2ca-f645-33df-ac2e-7f2dc0b0d652 | -8.35652 | -43.95267 | 2025-07-10 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2671724-b54f-3cbd-97f4-5ab1d3caceb2 | -6.67911 | -43.76857 | 2025-07-10 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6f0ff29-aa53-3cb5-8bf5-536f4673f0d0 | -5.25403 | -44.45527 | 2025-07-10 03:36:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e98fa846-4098-3c21-bdb5-ac4364a30ecc | -5.25325 | -44.4598 | 2025-07-10 03:36:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5a4f1e8-37f7-3beb-b566-4e1c3a753c8b | -3.6831 | -39.33366 | 2025-07-10 03:36:00 | NOAA-21 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c9114f89-d270-3a18-a8e1-b29c76794020 | -8.50908 | -43.30588 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 067d50df-ee99-3531-9b05-8cbf91a63f42 | -6.99691 | -43.48528 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91a2382b-7f07-31d7-8f47-75cf0c83e46a | -8.50789 | -43.31241 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 045d88ae-d772-3225-b19e-99deb4eac28d | -6.95474 | -42.71576 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50b438f8-584f-377f-b705-06e858e9072b | -7.22964 | -43.08154 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 9b78c5b6-12f9-3b4e-b240-bd585dab1d02 | -8.50144 | -43.31799 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 7207a07c-8e4e-3a04-a0ae-9c3959aef62b | -7.01266 | -43.4918 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2942f047-f3a9-337c-826f-65ac96b13ef7 | -8.50968 | -43.30262 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 9fafbfe2-ae90-3f0c-8a30-64a59ca418b2 | -8.49864 | -43.27391 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 482010dc-d193-349d-9dd2-070b562324b6 | -5.89108 | -45.57465 | 2025-07-10 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 928ac808-1e3f-34bb-9133-74aa7dc1a4c6 | -8.50213 | -43.28447 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| d6593640-ab01-304c-9f7f-86cf7c36b39d | -6.64456 | -43.19257 | 2025-07-10 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b8a2f69-7284-3eea-9da1-3132d07b856f | -7.00225 | -43.5189 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a600b03b-7eb0-3291-b482-0f028c5858df | -7.74961 | -43.59615 | 2025-07-10 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a7c1c46-ab17-303b-bfdb-c59dd4ef99b7 | -8.35671 | -43.95122 | 2025-07-10 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2117e42-9f37-38c8-9229-e146a35bd366 | -7.04315 | -43.28663 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e28de037-5d46-30f9-baa8-edc8b43220db | -8.51078 | -43.32641 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e6a33155-5910-3556-be86-752c522b25ff | -6.95377 | -42.71614 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8e2b4899-a09e-3f74-aade-0981b847baf2 | -6.64621 | -43.19647 | 2025-07-10 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8b01d96f-cbb1-3473-9d6e-590a5140bda1 | -5.89009 | -45.5802 | 2025-07-10 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a9f3a53-47b0-38e0-ab6b-cad23589486e | -8.53424 | -36.29039 | 2025-07-10 03:36:00 | NOAA-21 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7cbb92df-69f2-3e75-bd97-28886d35e049 | -8.49796 | -43.30726 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 9a6967c5-09a4-3d33-90ac-023dabd1448e | -8.50382 | -43.30495 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| b486003b-e9ca-3f23-95b2-09c7b02cedf0 | -6.70256 | -43.12969 | 2025-07-10 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 753a5a8d-0c2c-3a37-9401-b259fa79ae21 | -6.23977 | -43.36681 | 2025-07-10 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6b08d86-b04b-3e60-bd4a-127fe1ef8572 | -7.48439 | -43.9385 | 2025-07-10 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5309e92e-1474-3232-b5b4-580d3314b459 | -3.81026 | -42.54488 | 2025-07-10 03:36:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70467fc0-96b0-35ad-addf-618a364f3e07 | -8.50849 | -43.30914 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| d8a93246-e24c-3e93-a689-f46ce91d9ba7 | -5.24802 | -44.45435 | 2025-07-10 03:36:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01abc380-18f3-3b9c-9ceb-7135bff2c71f | -6.95893 | -42.71724 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d359691-3a3b-3c0e-9968-675cbf7932e3 | -6.64681 | -43.19316 | 2025-07-10 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ef1cf677-6e39-3953-859e-382b82033811 | -6.85242 | -42.8036 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 743f1784-5ce1-30fb-a10a-26a0c5ebb244 | -8.51137 | -43.32314 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| fb1e6589-d930-33a2-9eca-265e9c512ca2 | -5.41261 | -46.07744 | 2025-07-10 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 047f3be8-57a5-37bf-978b-2306ab9a186a | -8.49747 | -43.28029 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 1a698362-1966-3d4b-9f8f-a0d3b54ad2e2 | -6.99629 | -43.48878 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a082d60-d111-334e-886c-880b676d0eed | -6.13418 | -42.95912 | 2025-07-10 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d853709b-83fc-308c-ba55-c28dc5db02d6 | -6.8541 | -42.7942 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d74c2aba-d083-3d04-b61d-3e8452f99b36 | -6.98275 | -41.36529 | 2025-07-10 03:36:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3342d216-357d-3d72-b410-8a848a6c7807 | -8.35606 | -43.95483 | 2025-07-10 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bf4171b-3df9-3019-a088-ed0bbf2aa84c | -8.50154 | -43.28771 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 60560ca5-5cb0-3f83-8cb0-055aee4e05a5 | -7.22494 | -43.07731 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c44e8cc5-e448-3ad5-b6c1-e443bd40099a | -6.95418 | -42.71886 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ff5816c8-a01b-3d81-85cf-daade3de8c9a | -8.49509 | -43.29326 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 5037418d-a356-3e82-b789-144afd0c2d5d | -6.98835 | -43.50175 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 148c546e-224d-37b6-9a10-174661338f8f | -6.57072 | -42.90076 | 2025-07-10 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 68bcaac0-4159-3d39-9cd3-4c540f2e89e7 | -8.50024 | -43.32453 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 1ef3ff2f-5d77-334a-99c8-0f10d57f2cc6 | -8.49915 | -43.30074 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 93d5aca2-9fdc-30c8-89d7-6f0b60670d53 | -7.23024 | -43.07822 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fd27a396-c40e-39af-896e-a8aaca466c8d | -8.51019 | -43.32968 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b0d5f93e-97ed-314d-81c7-3294d41f6376 | -6.82074 | -41.73163 | 2025-07-10 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d47f1e2e-64b6-3636-a307-f433b9966d3d | -6.57601 | -42.9017 | 2025-07-10 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fee4a94-a04a-3de9-95ac-c3b53228256f | -8.36158 | -43.95578 | 2025-07-10 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c14d0d0-50eb-3880-a137-3c619db3e117 | -6.99928 | -43.5037 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2795f80-4bc9-3545-9d65-89c2f7541090 | -6.85876 | -42.79832 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b41e1e1f-2478-32a1-941a-d013e84a9b57 | -6.23915 | -43.37032 | 2025-07-10 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8239b74-d7e7-3b49-a83e-f7f7f35c8aeb | -7.20019 | -45.34981 | 2025-07-10 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f5913ad-4f5c-32d9-81bf-02a78165b488 | -6.84944 | -42.79007 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 432356da-6960-3d06-9f91-b95cb027db5a | -6.85298 | -42.80045 | 2025-07-10 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| adb6dc8b-6d1b-3ebb-91e5-8e1105dd6ce6 | -8.50084 | -43.32126 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| d831f83b-7d69-3a50-8b44-a420dece32a8 | -8.50322 | -43.30821 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 1f42f4c0-404c-3085-96dc-b61344adc153 | -8.51027 | -43.29937 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 99946617-7e32-3f0d-a675-f33076f1ff2b | -8.49688 | -43.28352 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| f5d62544-ebd0-346e-8530-5207adde480c | -6.9599 | -42.71685 | 2025-07-10 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06ad0c86-80eb-3f33-b332-78a6714958d9 | -7.00286 | -43.5154 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f766c454-375a-3da1-9b02-c545f62941cf | -7.4838 | -43.93393 | 2025-07-10 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8cdf49b-dc26-3901-9153-ab378c492064 | -8.36204 | -43.95361 | 2025-07-10 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6a96a00-96d3-3368-9049-367561f4bd24 | -7.02966 | -43.49575 | 2025-07-10 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb55e136-90be-3f7f-8727-642642ef54fd | -7.00981 | -44.42057 | 2025-07-10 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 251b8eac-df81-3b0e-80f2-fe56e3f91819 | -8.50094 | -43.29096 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| b2b86689-7406-36e8-9249-dbaed668a5be | -8.50035 | -43.29422 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| bd183a4c-0262-323d-b8ec-05ad9727623c | -8.50611 | -43.3222 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| f8422d03-cc71-3712-af26-8e91bdea4507 | -5.35012 | -45.27415 | 2025-07-10 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc80ce48-963c-3605-bc97-7c2c7c27854c | -8.5067 | -43.31893 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |


[Clique aqui para ver as próximas entradas](README9.md)
