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
| e85753d8-7dcc-3088-b9ad-a0b4c5bee1e4 | -18.23653 | -43.3491 | 2026-07-13 03:40:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d390014-083d-373a-964e-b228c3c7917a | -18.23205 | -43.34816 | 2026-07-13 03:40:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 021789ff-7d10-3023-82a2-5be733545826 | -17.41945 | -39.6475 | 2026-07-13 03:40:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0d380798-c905-3511-a27b-3260aeee70cb | -9.3629 | -46.7359 | 2026-07-13 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| dc7968b7-75ff-34cf-8dd9-ba3ceb8125b1 | -9.3629 | -46.7359 | 2026-07-13 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 8fd0d6e5-44c4-3d5c-9718-dfa0c3d757e6 | -9.3629 | -46.7359 | 2026-07-13 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 39010207-649c-3b56-b1bf-988534f77a07 | -6.92496 | -43.69418 | 2026-07-13 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d06ea57-69da-375c-a43a-e5a7af96e088 | -3.98815 | -47.9319 | 2026-07-13 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ec5be25-7565-3c2b-8464-dd7a1b0e59fe | -6.48982 | -42.22044 | 2026-07-13 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 669c5e10-06ef-301f-a622-8c7d7011c343 | -6.9246 | -43.69299 | 2026-07-13 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a762fe9-cfe0-35ad-aaac-68414725385f | -6.94701 | -43.71287 | 2026-07-13 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1eff145-e032-376b-a961-762cede0299d | -6.92815 | -43.6935 | 2026-07-13 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e21c1ca5-ed6d-3a92-9ddd-6456d5ff9177 | -4.94366 | -48.24966 | 2026-07-13 04:29:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34a9135c-4440-3f7f-bd88-7eff07eccae1 | -6.48825 | -42.22242 | 2026-07-13 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 1ecc5f5c-3b29-30c0-b046-2c9560f53db9 | -3.17555 | -48.01677 | 2026-07-13 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0595d4b-f983-3a86-86c2-cc327cab246f | -4.40128 | -37.79804 | 2026-07-13 04:29:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3ddd95c0-30c5-357a-9ac0-c1aaf62063f5 | -3.27143 | -48.82553 | 2026-07-13 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd7b0e54-3a05-3f96-9275-9ed5574db974 | -6.48894 | -42.21769 | 2026-07-13 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4c4997cf-7ca1-3d7b-b38f-355e23bd9806 | -4.92489 | -41.97514 | 2026-07-13 04:29:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 397cf761-8c71-3be8-a402-6eb222a78101 | -5.42112 | -45.29658 | 2026-07-13 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d0bfb4e-4780-3a2b-b372-04a4f782165e | -6.9458 | -43.72094 | 2026-07-13 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a58f6db-9959-3b48-82f8-6c4a9cfc9d5a | -6.49294 | -42.22564 | 2026-07-13 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 37570811-0896-3ce0-aba2-c523e6611b92 | -5.41834 | -45.29257 | 2026-07-13 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5c45a42-cf1e-35e7-aafc-89b30d15ac93 | -3.49461 | -48.03788 | 2026-07-13 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a54b420-b6a4-380d-a217-7ec92fbea11f | -5.18539 | -49.34448 | 2026-07-13 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19f01441-0072-3c45-819f-99c725f0c91c | -6.08328 | -43.663 | 2026-07-13 04:29:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d90713f-4185-3669-b8cd-adb182503c40 | -4.80622 | -45.77228 | 2026-07-13 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5d3b9cc-d5bf-3d93-8efa-34c6842d1de5 | -7.09139 | -41.68937 | 2026-07-13 04:29:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 205aacf9-7077-34c8-a02b-ad7dcc219faa | -7.09088 | -41.69275 | 2026-07-13 04:29:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df21c31a-0c85-301a-b7b2-37cd2a17299e | -4.80677 | -45.76883 | 2026-07-13 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2290cfb3-cad6-31d8-b211-76a9f477395d | -5.7969 | -45.1105 | 2026-07-13 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75821651-2521-3522-88db-621e2b4c3599 | -6.49364 | -42.22102 | 2026-07-13 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 331cdc28-e2ab-3262-a942-2000ebd83535 | -5.55714 | -49.06842 | 2026-07-13 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74615a5b-7094-36ea-86a5-21bcf8589170 | -4.00435 | -48.95075 | 2026-07-13 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7943ec2-759d-3d28-b2de-9ef9ec648c82 | -4.18414 | -47.84808 | 2026-07-13 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35ecf7f4-2d18-31ab-a773-b9d5c4ac73b8 | -4.64019 | -43.04632 | 2026-07-13 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b1d9de2-edcf-331c-ab0e-8ff91673fe54 | -3.49808 | -48.03841 | 2026-07-13 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76a6f42e-08e7-3316-a2e3-45ec416fe6ed | -6.94995 | -43.71743 | 2026-07-13 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e09a8bd-05fd-3d93-8817-b2a645e0430a | -5.74979 | -43.26648 | 2026-07-13 04:29:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72f918c9-bb05-3660-b7b9-88c709ade5ef | -4.40086 | -37.80087 | 2026-07-13 04:29:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b270e25-97f9-345f-89af-03d5b77537fa | -6.94225 | -43.7204 | 2026-07-13 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa3d4f0b-2307-3340-a8e2-1c0e0104db05 | -5.97791 | -43.61948 | 2026-07-13 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f6466c9-5c33-31ce-aea9-aca407540183 | -6.94934 | -43.72146 | 2026-07-13 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22b8784d-c696-3293-91e7-2eb2d0683d32 | -4.18473 | -47.84438 | 2026-07-13 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71140758-54d2-3786-b250-070d861e52ae | -6.34755 | -44.31961 | 2026-07-13 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d22aed9d-c07c-3733-b656-bcaf961a2489 | -4.30204 | -47.57307 | 2026-07-13 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05498197-b45f-3790-8456-59c60c11ab75 | -5.79634 | -45.11403 | 2026-07-13 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 38a8cb3e-76c2-3612-9ca8-7b5f69d75d5b | -4.94428 | -48.24585 | 2026-07-13 04:29:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4567cf24-af59-3bf6-84aa-209171107810 | -6.48912 | -42.22506 | 2026-07-13 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b6ef3391-487f-393a-83d7-1fd1a944391c | -6.9464 | -43.71691 | 2026-07-13 04:29:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d171096-8001-30d1-831c-b655e796d9e4 | -6.49207 | -42.22299 | 2026-07-13 04:29:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 24f70172-b187-32b3-9350-4acb1686b894 | -4.00795 | -48.95131 | 2026-07-13 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3b9049a-9198-3129-82e7-bf07aeeb7c11 | -9.3629 | -46.7359 | 2026-07-13 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| a61e9b63-5ba0-35c0-b8b0-a1d0e14eed11 | -10.47733 | -42.42479 | 2026-07-13 04:32:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9c1d8c6a-b35d-3c09-a3b6-297686d5837e | -9.63713 | -40.60053 | 2026-07-13 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| fe30c8f0-76c7-3954-822d-6e343e625be9 | -9.3821 | -46.72209 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3b0a86b-d672-3ec8-af40-0ab291f69fb2 | -10.56288 | -45.69573 | 2026-07-13 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6505281b-7424-3b45-8b1e-c769764f84d0 | -13.96054 | -38.94402 | 2026-07-13 04:32:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 794d42c9-86e4-3dce-857b-18aedec4154a | -10.26395 | -50.05475 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7992b9c5-713a-3680-aaa2-a74257d7f54e | -13.75893 | -46.24712 | 2026-07-13 04:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66c7a350-56e0-3246-be4a-3d31a7d309b2 | -13.62267 | -43.7147 | 2026-07-13 04:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4923112c-e7fd-3b1b-98c0-a4e77b6d67f2 | -9.38265 | -46.71861 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38768063-c1b5-3bf0-a0a9-1210d10116ea | -10.56683 | -45.69258 | 2026-07-13 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95950239-f292-3748-901b-1c104132f025 | -8.09592 | -47.09991 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 480e174c-a884-3a5f-acf4-24c3c41acc7f | -10.25622 | -50.05757 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bbefd5e-bce4-3b3c-9cd7-27480cda5e11 | -9.34904 | -46.73826 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99fd8e65-bfe7-3e40-b595-4bbe474a479e | -9.37878 | -46.70014 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbc943ae-5468-355c-9938-8544274a3532 | -13.76292 | -46.24381 | 2026-07-13 04:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b91f2685-f867-32f2-8a87-8232b5daab7d | -9.34736 | -46.70586 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eef1e401-5e18-3880-8c1f-e8cb66d15df3 | -10.67725 | -38.28134 | 2026-07-13 04:32:00 | NOAA-20 | HELIÓPOLIS | BAHIA | Brasil | 2911857 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 245be1f5-a2d5-38cb-9bef-c58c496a68ba | -10.25269 | -50.05696 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f67ffa3-6399-39c0-8aba-dde301efad00 | -8.09261 | -47.09939 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f276c5b5-62a0-3d1d-bf27-51a17bc6ed0c | -10.26389 | -50.05359 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0641f518-1cfa-35fc-95e3-46d205cfe66b | -8.8814 | -48.50039 | 2026-07-13 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab1a6ed6-b27d-3d34-b0dd-5649b4ef6e8f | -10.25401 | -50.0489 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11fda8ea-2403-3985-aeff-4e6906b6395a | -11.98915 | -45.15239 | 2026-07-13 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc3a3e05-22f0-32dc-9963-934419498b1e | -10.81735 | -45.12962 | 2026-07-13 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0c874549-558c-3170-a7a7-c40fa3392d7d | -10.56627 | -45.69626 | 2026-07-13 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9095ba30-2f13-3b30-95b0-376d669822e4 | -9.36392 | -46.72991 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81226f41-4484-3edc-8c6f-a6372d0182fc | -9.38596 | -46.71913 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b51d79e-a520-3ea8-bb25-2734f9595ddb | -13.75836 | -46.25089 | 2026-07-13 04:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 992eb121-ad25-3fd7-aacc-e2f538883e1d | -11.99034 | -45.14448 | 2026-07-13 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bdae44b-f5ca-3eb7-bfd3-5c0ffc58f3f3 | -10.25335 | -50.05293 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5e96772-3879-3aeb-82bd-089348bef8ef | -9.37879 | -46.72157 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 564feb51-7aab-3ce4-b2d1-4d3a69a3ec00 | -14.12317 | -46.47861 | 2026-07-13 04:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b725708e-630a-3cb1-aa1d-91989a280823 | -11.7844 | -41.19552 | 2026-07-13 04:32:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c98c514c-2207-34f8-8fed-bb4a0c277c9d | -9.36337 | -46.7334 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c02b4962-b044-3a8a-b266-dded86a1b7a8 | -10.81676 | -45.13346 | 2026-07-13 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3eb96b8b-ae43-3c58-b80e-85af06bc3742 | -8.62805 | -49.86074 | 2026-07-13 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca6d8747-52e8-3f87-872a-03ff9459d488 | -9.37108 | -46.72747 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e454906-a767-3a05-9bed-6f20e77419f0 | -9.86203 | -57.80323 | 2026-07-13 04:32:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79897e95-2d6a-3f16-bdcc-b207272ad515 | -13.75779 | -46.25467 | 2026-07-13 04:32:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69947d71-898b-3807-9faf-fedc3033484a | -9.37494 | -46.72452 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34606a19-d7e3-32cf-a4c9-6fc7547a8a10 | -10.25754 | -50.04951 | 2026-07-13 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bea78f95-6534-3859-83fe-afcc8f5479c3 | -9.37548 | -46.72104 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 763e315e-114e-35ab-a15a-87a6cc6e303a | -8.086 | -47.09833 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09a32588-c2b1-3a03-8b5a-86b66a760a99 | -8.09041 | -47.09192 | 2026-07-13 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51702783-3ec5-31d2-8fce-a90d0b28584b | -9.35896 | -46.73983 | 2026-07-13 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a210ef10-89d2-377c-a4a5-5e6fe6798464 | -9.86204 | -57.80363 | 2026-07-13 04:32:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4f988d9-0fe7-3604-8ea5-b46ed60a776e | -8.87861 | -48.4962 | 2026-07-13 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |


[Clique aqui para ver as próximas entradas](README5.md)
