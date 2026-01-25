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
| 3943bf78-4fa0-30dc-8a73-3ec680f34c99 | -9.96876 | -36.78216 | 2026-01-25 03:36:00 | NPP-375D | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6273a31b-584c-377d-ab03-48772a239833 | -7.89575 | -35.31742 | 2026-01-25 03:36:00 | NPP-375D | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1fe2f368-411e-375e-9bb9-5e02d9ebdb66 | -9.965 | -36.78151 | 2026-01-25 03:36:00 | NPP-375D | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2273fb76-bd25-31a1-b8be-02dfd797191b | -7.50062 | -38.8255 | 2026-01-25 03:36:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 04790fc1-7d8b-378c-a91a-271f1dd3c41d | -8.33911 | -36.72231 | 2026-01-25 03:36:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b3e640a-53ec-341b-af02-6e3a71a49326 | -10.1174 | -36.99751 | 2026-01-25 03:36:00 | NPP-375D | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d32f18d-fc54-3d79-976e-ddd294dc13fa | -9.60857 | -35.9031 | 2026-01-25 03:36:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 66c31a4a-b1a7-3a16-8f92-4169debf79c0 | -11.08034 | -38.13573 | 2026-01-25 03:36:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c4189914-53e7-3e5e-9063-8e13f8653b23 | -9.60787 | -35.90733 | 2026-01-25 03:36:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 481a9a4b-8776-3ae2-ba61-7d359ceb96ee | -9.37631 | -40.71351 | 2026-01-25 03:36:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b6c5795e-0bb3-37f9-907b-28f9dcf7788d | -15.69962 | -39.25187 | 2026-01-25 03:38:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 91cf0ad1-f7d1-3a32-ab93-e418ae118990 | -3.0603 | -40.1072 | 2026-01-25 03:40:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 753a6930-2fc3-33ac-82af-9b0fa087b817 | -21.94677 | -47.42077 | 2026-01-25 03:40:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 890fcb24-6d75-309b-9c75-9f179cd3f27c | -21.06862 | -49.53195 | 2026-01-25 03:40:00 | NPP-375D | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d8103a0d-03d1-3825-b0f8-6bdf9e9cf321 | -21.07522 | -49.53406 | 2026-01-25 03:40:00 | NPP-375D | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 26393c2d-8ab8-38d2-958e-2e7914dd9ddb | -21.069 | -49.53489 | 2026-01-25 03:40:00 | NPP-375D | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b372741c-1985-34db-9d09-c45f4739623c | -23.46798 | -48.89868 | 2026-01-25 03:40:00 | NPP-375D | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bf6877f-7e79-3c57-b5d8-bcb673530e9a | -23.46667 | -48.90402 | 2026-01-25 03:40:00 | NPP-375D | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae52aa74-b981-3ef7-9232-2fa9b18d3b77 | -10.11394 | -36.99643 | 2026-01-25 03:55:00 | NOAA-20 | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ecfa23a4-ff34-3537-b89b-1ebc69095411 | -4.65773 | -37.93012 | 2026-01-25 03:55:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a28a020-e7a8-384c-ac16-f6fafaa80896 | -5.54177 | -37.68687 | 2026-01-25 03:55:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8a6c519a-6e0b-37bd-b982-43380ff677cf | -5.89764 | -39.72069 | 2026-01-25 03:55:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 695b2d75-2c92-31ed-a598-f633caeea0f3 | -3.38246 | -42.11528 | 2026-01-25 03:55:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd424810-9911-3005-8758-9975040921ca | -3.06449 | -40.11026 | 2026-01-25 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| dad96d58-9efa-3d99-ae60-12a6aa503295 | -9.60892 | -35.90485 | 2026-01-25 03:55:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3fae3e90-14d3-377b-9b59-b91bb2c93bf4 | -7.86358 | -39.09518 | 2026-01-25 03:55:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c0ce6f7d-8276-3a59-b6a2-b63f56373746 | -7.58344 | -37.63544 | 2026-01-25 03:55:00 | NOAA-20 | SOLIDÃO | PERNAMBUCO | Brasil | 2614402 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c70ab4b-ff21-3bef-9704-1ca619a28fff | -3.06736 | -40.11469 | 2026-01-25 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 3d315ab2-5570-3081-a3fb-804a36274ffa | -5.48035 | -37.66658 | 2026-01-25 03:55:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a07a3d2b-8ba6-3271-bd5f-90347f6e04fa | -3.06859 | -40.10697 | 2026-01-25 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 7732a77b-78f3-3cac-92ad-b406e63d7e27 | -5.99587 | -39.43014 | 2026-01-25 03:55:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63e8b014-de7e-3a44-9be2-8a1338ae788b | -5.56932 | -39.12118 | 2026-01-25 03:55:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 489e5252-f419-38c6-b5c7-1077b4265dc3 | -6.20263 | -39.28313 | 2026-01-25 03:55:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 05885e88-82f6-3eb3-9bd5-0736f7e9c122 | -8.20949 | -39.48275 | 2026-01-25 03:55:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5a5477ac-0519-31bf-a395-330059fc3976 | -3.0651 | -40.10641 | 2026-01-25 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e3137781-1126-3f44-8c0b-c56c9b3dad03 | -6.22594 | -35.52486 | 2026-01-25 03:55:00 | NOAA-20 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dbae5f05-b987-34d6-9ec2-762c4d040cc2 | -5.56655 | -39.11716 | 2026-01-25 03:55:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ed225c10-9ab7-311a-b36c-46cf199da57f | -7.1246 | -39.70113 | 2026-01-25 03:55:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b806d27-6353-3da2-a0ff-c9370e7f9498 | -5.49149 | -41.32507 | 2026-01-25 03:55:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c71703e-fe84-3364-88e7-affe8276236f | -5.56599 | -39.12065 | 2026-01-25 03:55:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f5e15f38-7be7-36c5-8a52-5fa1f88fb879 | -5.55624 | -39.546 | 2026-01-25 03:55:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3659b7b-1420-327f-b402-347cd2a3c3e3 | -7.89584 | -38.45999 | 2026-01-25 03:55:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 434f1d0f-090c-364e-a4c2-0b31657070eb | -5.92437 | -36.22517 | 2026-01-25 03:55:00 | NOAA-20 | SÃO TOMÉ | RIO GRANDE DO NORTE | Brasil | 2412906 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c032b552-b334-3998-98f0-6c34e85ce892 | -8.97082 | -40.56167 | 2026-01-25 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 43541a26-fc2c-3e8e-a4f8-df540e2c1081 | -3.06387 | -40.11412 | 2026-01-25 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| cecc1a06-8347-3b04-8a1e-c570b22dd173 | -7.87856 | -41.59224 | 2026-01-25 03:55:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ec6284e-5606-3828-83d2-5178a07475bc | -10.11544 | -36.99778 | 2026-01-25 03:55:00 | NOAA-20 | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a0c16dad-e2a4-3ff1-8311-dbc16169e268 | -4.54172 | -40.16544 | 2026-01-25 03:55:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d4ed202c-b28e-370e-90c4-e4e4064ccd4a | -5.35481 | -40.60294 | 2026-01-25 03:55:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7e74151c-cef1-3fda-ae32-7a23bb1bfc3a | -3.07207 | -40.10753 | 2026-01-25 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 5e0fc0c2-306d-3fb6-9d9a-9a6fe74a6818 | -9.96506 | -36.78022 | 2026-01-25 03:55:00 | NOAA-20 | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8541752c-3e0a-383c-96c8-c5ad55373013 | -9.37777 | -40.71339 | 2026-01-25 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 74fa3caa-da08-3620-b911-1d0b176fa37d | -4.64173 | -38.75973 | 2026-01-25 03:55:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6f1c5d7-be41-32e0-8130-12981e9f299c | -5.66472 | -37.85517 | 2026-01-25 03:55:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 372d8fa6-a3ed-3e05-990f-456edf695d71 | -7.89915 | -38.46052 | 2026-01-25 03:55:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e2ef6e6e-c6e0-3d9e-b045-19ada026eb82 | -6.82348 | -41.2188 | 2026-01-25 03:55:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9b4d86d7-4fb7-3230-96a0-7da289b012e8 | -9.96856 | -36.78076 | 2026-01-25 03:55:00 | NOAA-20 | CAMPO GRANDE | ALAGOAS | Brasil | 2701506 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 14d41c03-76cb-3860-ac57-eeb7970f6754 | -3.06797 | -40.11082 | 2026-01-25 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 4a30d61e-7a42-342c-ad69-1e56ce7e68d5 | -8.96744 | -40.56111 | 2026-01-25 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c70696f9-c832-37a8-9208-df9f6fe43d72 | -6.1993 | -39.28259 | 2026-01-25 03:55:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0b8bfb28-5827-3b08-b045-72f23eb1aab3 | -7.12209 | -41.38892 | 2026-01-25 03:55:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6eaec2c1-b933-3e58-a43c-255ee160a771 | -5.56988 | -39.11768 | 2026-01-25 03:55:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 659d9422-c07e-3997-8c59-f02bdff7b54a | -10.11742 | -36.99694 | 2026-01-25 03:55:00 | NOAA-20 | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51e2b0b8-1e1c-38f8-ada6-e51ab16a6119 | -4.64014 | -40.27338 | 2026-01-25 03:55:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7284463-2417-363d-a5ae-4faf6f560a06 | -7.16419 | -39.95905 | 2026-01-25 03:55:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac859e9d-accf-382a-aa11-5e4826b8b102 | -3.07146 | -40.11138 | 2026-01-25 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 612bedf0-72ba-3db7-ace7-8907bed77a77 | -12.43058 | -43.79396 | 2026-01-25 03:57:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0f2253c-2a69-3e82-9147-f81b15a0d920 | -15.70073 | -39.25072 | 2026-01-25 03:57:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9c5a5223-e35e-3581-a4c0-696a401bbc68 | -11.07922 | -38.13433 | 2026-01-25 03:57:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bad5d4e3-42ae-340d-9a23-235bef55e4db | -11.1478 | -43.31825 | 2026-01-25 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 89b07f67-eb8e-351b-a640-9c5e4e36bff0 | -11.14704 | -43.32275 | 2026-01-25 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2b4ef39c-5fcd-37fd-9f0e-5627e047a660 | -11.19162 | -41.03469 | 2026-01-25 03:57:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5e59fe59-c5c4-359e-bbb9-a3431a068b9f | -11.55461 | -37.97759 | 2026-01-25 03:57:00 | NOAA-20 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8bd15db8-b0cf-3286-8ce5-74740874a95a | -15.46795 | -43.48162 | 2026-01-25 03:57:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99f53b26-022a-355a-b109-261619b4586d | -15.69736 | -39.25018 | 2026-01-25 03:57:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9b885ab7-c3de-3f7b-ad6a-9c69f8fc01b3 | -17.70622 | -53.2849 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 032b8a9a-f788-3cb7-9005-229bb9206655 | -17.70402 | -53.28606 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 716dab42-90f5-3e8d-979a-eef6820f42b3 | -17.70345 | -53.26805 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 421d963f-fa1c-305d-aced-fc6dd54d570c | -17.69401 | -53.27302 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d726b0f-b9cd-3420-9734-8287762f14f2 | -17.70733 | -53.27987 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffa5458b-0ff5-3818-adb6-24af186d23d9 | -17.70118 | -53.27836 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7b727cf-8fd6-3686-8243-c94159ebb297 | -17.71025 | -53.2872 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0855863b-af76-3e2a-bfb5-c4d622806b4f | -17.69616 | -53.27173 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8ec40e0-a2b5-3349-9558-f1db6f5437bc | -17.70138 | -53.26915 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efd3f4ba-c2aa-3f3e-b6e3-ca429350ece4 | -17.69499 | -53.27703 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e4fcf5d-86e9-3559-865f-05c69cde4282 | -17.70634 | -53.27585 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84ec2a59-99fb-3f9c-a7cc-ca68b5449337 | -17.71243 | -53.28613 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d772cf7e-590d-36fb-ba8b-4131a18b8bd9 | -17.71136 | -53.28234 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9a6e412-7285-3485-abe9-11d4e1eb656d | -19.29437 | -53.1785 | 2026-01-25 03:59:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f78bdf7-ed17-316e-87cf-b6dcc31166ea | -19.30024 | -53.18028 | 2026-01-25 03:59:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| effc60af-3057-3404-8f05-1b9e4fbfdc97 | -17.70233 | -53.27314 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6498f94a-9f1a-368a-9852-28f24b8331ea | -17.70519 | -53.28091 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6e106a9-df96-3d5d-8e40-8988b17a37ca | -17.70021 | -53.2743 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c66dce0f-0cca-3b9e-b5ac-8d445e477fe7 | -21.071 | -49.53232 | 2026-01-25 03:59:00 | NOAA-20 | NOVA ALIANÇA | SÃO PAULO | Brasil | 3532801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| efb8a9a3-3425-35c4-a411-ee462d4df76a | -17.69901 | -53.27956 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4882b284-47d9-3fd2-b498-1ed9d2506f6a | -21.94875 | -47.42208 | 2026-01-25 03:59:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1853a180-7925-34c1-8c8f-7d5e25238c25 | -17.70001 | -53.28368 | 2026-01-25 03:59:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f6f50ea-e841-32c7-bedb-66983ac44108 | -3.0791 | -40.1063 | 2026-01-25 04:00:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 6e9aa116-61fb-3d70-84ed-b2c9997df91e | -3.0603 | -40.1072 | 2026-01-25 04:00:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 06cda552-8edb-3ba3-9931-a674f785c425 | -26.03023 | -52.69662 | 2026-01-25 04:01:00 | NOAA-20 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README4.md)
