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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca4b226d-b860-35c2-9f3b-d754eeb618e6 | -15.23353 | -43.27918 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c31e2788-c503-3867-b377-1944d9dcfe4b | -14.83045 | -43.30827 | 2026-09-26 03:32:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 947e6724-c7ad-3a2d-9899-145a231076e8 | -15.23606 | -43.26651 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 3ce36986-bed8-3263-9c26-2c6271f87de6 | -13.47474 | -42.48047 | 2026-09-26 03:32:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8ab8ce17-5dea-3804-ab5b-0f0f97ab1efa | -15.2451 | -43.27489 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 654b11e1-0396-33c9-ae35-c32a5b35a5e6 | -15.23868 | -43.28025 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 83a9b78d-6697-347e-acde-5120080d6280 | -9.46645 | -40.3383 | 2026-09-26 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5b5819c8-e336-37f4-9bab-12e5199253fd | -9.85838 | -36.01613 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a1c41763-2763-3b11-9f5a-9323ce21f544 | -9.85587 | -36.02312 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fe0d7280-1f5d-3cc0-9198-5456982c3463 | -14.61222 | -41.03141 | 2026-09-26 03:32:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3028b4a2-da0b-3140-8c25-39ca59ca1a1d | -12.58358 | -44.13344 | 2026-09-26 03:32:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aff9cda4-3f4c-3a06-9e1f-c0afe39a95db | -11.94799 | -38.29004 | 2026-09-26 03:32:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ae70f73a-2500-36a2-ae6b-c044475d8e73 | -15.23417 | -43.27597 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 16b177b5-0ac5-38ab-b8eb-84ff7460c84f | -9.85413 | -36.01967 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 66737b56-779f-3cb8-b12d-4dec1850ab2a | -11.93045 | -38.29744 | 2026-09-26 03:32:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 83cd1173-2bb0-3b78-bef8-6a5ca453712a | -11.93529 | -38.29298 | 2026-09-26 03:32:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 1dbecf49-2745-3f43-a3b0-9efdb66f84c4 | -11.13777 | -42.8241 | 2026-09-26 03:32:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f817ab08-b12e-3807-a5c3-4a99efb81434 | -12.69817 | -47.29523 | 2026-09-26 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| def1b40f-219f-373a-b21f-ff32b51180b1 | -15.24574 | -43.27169 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 0b17af9f-2df6-37e3-8a82-1f603941196d | -16.56562 | -43.98734 | 2026-09-26 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b11bf075-4720-3de6-a7c2-e0297527dd7d | -16.76377 | -47.25734 | 2026-09-26 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dea7d187-f3a7-3785-8897-44f2df3897fc | -16.57017 | -43.98862 | 2026-09-26 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d75e345-aa74-3c3b-81cf-0c2103d3c87d | -15.42658 | -47.89698 | 2026-09-26 03:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8b07979-fe43-3c1b-abdc-648a67dfffae | -16.57159 | -43.9849 | 2026-09-26 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 104e597a-80dd-3859-a15a-a07caf0894a7 | -19.90946 | -48.259 | 2026-09-26 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de8dc4ff-bea9-33ab-98c9-3cbd42a2aa3b | -15.42786 | -47.8978 | 2026-09-26 03:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ae91476-f664-396e-8e4f-badba95c928f | -16.3596 | -42.56831 | 2026-09-26 03:34:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db325c8f-35e9-33eb-9a8d-e5c8a7d65ed1 | -19.90862 | -48.25668 | 2026-09-26 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d7b786cd-fff5-3981-80bc-842f24133b25 | -16.57017 | -43.99196 | 2026-09-26 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| af1a2139-19ef-33b0-ba59-4aa9def88f39 | -18.2606 | -45.62048 | 2026-09-26 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87875bee-59b0-36a4-ba46-533e38f7d589 | -19.90319 | -48.25712 | 2026-09-26 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 795baa46-198d-35a4-8c44-a656c9c2d766 | -16.67389 | -41.85461 | 2026-09-26 03:34:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.7 |
| ce01052c-c506-3da5-b77a-bbedb886d5ce | -16.76314 | -47.25277 | 2026-09-26 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d901660c-c303-34f1-b412-99f7f4671290 | -20.4237 | -47.45917 | 2026-09-26 03:34:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e060f689-8ee8-36a5-84cb-b11218f37824 | -18.55632 | -42.71278 | 2026-09-26 03:34:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fd5ad8a7-cff4-35ee-af42-8847efbf82c9 | -16.5709 | -43.98833 | 2026-09-26 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 08d288fa-0db2-319b-8b17-74812755ea72 | -19.89441 | -48.26586 | 2026-09-26 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2142760-a0d4-3067-9d67-03a07cdfcfbb | -21.86936 | -42.12157 | 2026-09-26 03:34:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 087e41f0-6f07-3d10-98ce-a7b9384c4370 | -15.42911 | -47.89225 | 2026-09-26 03:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98931259-49c9-3a1f-be30-7f39667e73a3 | -16.76196 | -47.25821 | 2026-09-26 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7ef6cbe-262f-35c7-bc2f-0919cbcd90b5 | -15.43215 | -47.9039 | 2026-09-26 03:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52f4d188-84df-3c14-8b80-df7e6e8498b2 | -16.56561 | -43.9842 | 2026-09-26 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 947463e8-2ddc-3a78-a176-217f2f64c3e0 | -16.67364 | -41.85748 | 2026-09-26 03:34:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| e209b816-a46f-3c6a-8f9e-2458b43a00af | -16.56489 | -43.98766 | 2026-09-26 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 450260a2-6e92-3715-ac24-5b9f7b9eeb89 | -16.56631 | -43.98389 | 2026-09-26 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d83078d-7c6a-3d1a-9cc5-e0524ce5b2e7 | -15.42108 | -47.89639 | 2026-09-26 03:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60e201c0-f904-3452-b53d-31b59d4875f0 | -21.10277 | -46.26912 | 2026-09-26 03:34:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7d8f2298-9aa9-3805-b7be-305b8318c8e0 | -21.23933 | -48.33578 | 2026-09-26 03:34:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7defd899-60ca-3862-a12f-71e74363ac91 | -16.57089 | -43.98518 | 2026-09-26 03:34:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9a3dcde5-f504-3302-b046-c4442ca047f7 | -19.91074 | -48.25357 | 2026-09-26 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3b1eac8e-be03-3cf1-8504-5e1fff87f482 | -21.10384 | -46.27018 | 2026-09-26 03:34:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fcfa5d39-6db8-3eae-95ba-7356faa7c610 | -21.11084 | -45.65801 | 2026-09-26 03:34:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 31c0bfa6-c192-3a6e-a262-364705741f6d | -15.4198 | -47.89557 | 2026-09-26 03:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c4ab7fc-0d52-3753-b9ec-67856dbce736 | -16.75748 | -47.25554 | 2026-09-26 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ee0f861-fe47-3634-9f8e-4157cb20e1a3 | -15.42534 | -47.90263 | 2026-09-26 03:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3ba778a-9ed4-33e9-b0b2-cc9de8163710 | -15.43338 | -47.90482 | 2026-09-26 03:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c253628-c18d-38f5-8ee3-803485b0c8dc | -16.67461 | -41.85233 | 2026-09-26 03:34:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| ca7d53ba-3aeb-3458-9b97-a10be82a567c | -15.4278 | -47.89141 | 2026-09-26 03:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39bb11ad-4dd8-34d8-b720-fe674dd152ac | -21.10558 | -45.65641 | 2026-09-26 03:34:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3595cb8a-9656-321b-83ce-9678612ac0e9 | -18.84142 | -46.83272 | 2026-09-26 03:34:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cdefe88e-e557-3cc5-b1d1-67c425de5d70 | -16.76699 | -47.26578 | 2026-09-26 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e2a32fb-fa46-321c-90b4-e4387a3aebfd | -15.2511 | -43.2743 | 2026-09-26 03:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 129.8 |
| 494c9a6c-2957-38ed-b660-6d9565cfc92e | -5.7384 | -45.0626 | 2026-09-26 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0168c1b3-8be1-31c0-aff9-ed1d05e5744d | -15.2517 | -43.2501 | 2026-09-26 03:40:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 74.7 |
| ffc641c4-640c-3841-ac3a-5dbec62ae8b5 | -12.9457 | -51.0695 | 2026-09-26 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4abedde9-8206-346f-935e-b852762fc6b3 | -9.4582 | -40.3143 | 2026-09-26 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 139.2 |
| 68deb4d3-2795-3ebe-b75c-7084643f51d7 | -11.8475 | -50.5384 | 2026-09-26 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d518b9fd-3e50-3bca-9e83-578e028b8e32 | -11.8662 | -50.5576 | 2026-09-26 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 147edbef-1989-3f1e-a9a2-f0dda2fc616c | -9.4769 | -40.3365 | 2026-09-26 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 316.1 |
| e720dd75-8113-3e96-9b13-6185451ce815 | -11.9228 | -50.5938 | 2026-09-26 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8a8011c6-0c8b-31b9-8d7b-956c1222b237 | -11.8665 | -50.5362 | 2026-09-26 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 9f2db67e-a0e8-3785-b0e4-1df93807198a | -9.4773 | -40.3116 | 2026-09-26 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 190.8 |
| 8abcd7fe-b00c-37fe-831e-a04e8f92154a | -15.2314 | -43.2784 | 2026-09-26 03:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 7853b611-e2a0-310b-b367-41a85a2f13a9 | -11.8472 | -50.5598 | 2026-09-26 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b1e076ae-490a-38ec-857b-262a2a7417bd | -9.4578 | -40.3392 | 2026-09-26 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 226.4 |
| c1849567-4b82-311a-b0e9-916035addb21 | -15.2511 | -43.2743 | 2026-09-26 03:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 158.8 |
| 02cfb441-25f6-33bd-8097-37a563bbb093 | -15.2517 | -43.2501 | 2026-09-26 03:50:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 100.9 |
| 193c6818-735b-3c92-ae96-637d810c94b9 | -9.4578 | -40.3392 | 2026-09-26 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 330.9 |
| ba395408-276a-349d-ab30-91df164e515e | -11.8662 | -50.5576 | 2026-09-26 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| db685b7a-0afb-3a4d-b231-3eb52bc71bb1 | -12.9457 | -51.0695 | 2026-09-26 03:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 283a34b3-4a36-3155-8008-02186429ecfa | -14.8903 | -47.1315 | 2026-09-26 03:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 7c8f1544-418d-3c82-a1ce-54f5f9503847 | -9.4765 | -40.3613 | 2026-09-26 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.4 |
| c95fbff1-c4e3-3be9-88ef-e04900ebadd5 | -9.4773 | -40.3116 | 2026-09-26 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 323.0 |
| 2cf5ea7e-c648-3c5b-9d38-3b8dfe802842 | -11.8472 | -50.5598 | 2026-09-26 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 662578a3-eb48-34fd-9591-fdf8e4d22654 | -9.4769 | -40.3365 | 2026-09-26 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 537.5 |
| 0ec4d4a9-c93b-39d3-be0c-4a6cae4aa907 | -9.4582 | -40.3143 | 2026-09-26 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 186.9 |
| aba51a1c-f4fd-3056-8f60-d32fbd064b5b | -14.8708 | -47.1349 | 2026-09-26 03:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 368b3bf6-0e32-3476-958c-760a2600dbbe | -3.2728 | -50.1372 | 2026-09-26 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 382b8588-0f44-3188-bc0a-f7830605d9e0 | -15.2314 | -43.2784 | 2026-09-26 03:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 95.7 |
| fa99e9bd-6c73-3a7a-8a7b-0edea688e3a2 | -15.232 | -43.2541 | 2026-09-26 03:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 6cf1608b-c4b6-3326-9590-ba83c624ffa7 | -15.2511 | -43.2743 | 2026-09-26 04:00:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 68.4 |
| ed1de070-d30b-3e08-bca1-d80541712d28 | -15.2517 | -43.2501 | 2026-09-26 04:00:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 57.5 |
| 808b5fdf-7de4-3865-8a7d-62c424bbfcd5 | -12.9457 | -51.0695 | 2026-09-26 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 485aaca9-3cd9-31d0-860f-12e6e8b87318 | -5.51992 | -39.86869 | 2026-09-26 04:06:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3c3a90fd-df6b-3b21-9c38-c8c29f5ca9bf | -3.80291 | -51.01943 | 2026-09-26 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bb4cd66-0cfe-31ee-b350-54cc688cb4ec | -4.65898 | -42.43297 | 2026-09-26 04:06:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e9ef1926-d35c-3abc-a9b9-337d8f1b807e | -3.23777 | -43.22388 | 2026-09-26 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad907e8f-7e02-3fd5-a369-7da6d2ed1c8b | -4.29044 | -48.61557 | 2026-09-26 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 171ca664-80ba-3d4b-9f60-85a83918efb2 | -5.52392 | -39.86562 | 2026-09-26 04:06:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 54cb9bc9-cb41-3d24-909a-4e26108f3bc9 | -3.45092 | -50.07732 | 2026-09-26 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
