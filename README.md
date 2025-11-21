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
| 055303ef-cc37-39f2-85e0-b510791dfdd8 | -22.92743 | -48.66664 | 2025-11-21 00:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 2352638d-b29a-326e-baf7-80000462caa2 | -21.15661 | -48.59456 | 2025-11-21 00:09:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| 8a05f0a9-291a-32e6-9449-e807dd4ded63 | -17.64558 | -43.89474 | 2025-11-21 00:09:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7bb8fc50-0848-3aac-b133-a18062391829 | -21.2989 | -49.67648 | 2025-11-21 00:09:00 | TERRA_M-M | ADOLFO | SÃO PAULO | Brasil | 3500204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 41.6 |
| e8d68eba-192a-3616-871d-c53b5b5295e6 | -18.24128 | -44.16066 | 2025-11-21 00:09:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b770b6b5-74a8-3354-97ff-f45479f657c9 | -20.89215 | -52.35086 | 2025-11-21 00:09:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 7bb1a186-7efa-3cde-8287-77b3b4e7b500 | -21.04887 | -48.55376 | 2025-11-21 00:09:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.9 |
| 1768c217-b1c2-3fdd-a354-317baa7765c4 | -17.64433 | -43.88529 | 2025-11-21 00:09:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 9ffdb61c-ef11-3496-8a88-8c605353b33b | -23.60524 | -51.73899 | 2025-11-21 00:09:00 | TERRA_M-M | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 35.8 |
| bd57d034-1192-3ab4-8d54-d7adde13673f | -22.91794 | -48.69604 | 2025-11-21 00:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| efce2bef-b08e-3059-8f5a-e47c614e6329 | -19.58506 | -42.73722 | 2025-11-21 00:09:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 63db1f64-23e7-301c-995c-eb1bf9af4e7a | -17.24727 | -42.21252 | 2025-11-21 00:09:00 | TERRA_M-M | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| e3f69b88-8eab-322d-961e-1c50cf3dee4f | -22.9309 | -48.69478 | 2025-11-21 00:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e3005b58-9f01-35e5-a5d2-91e4b3902de1 | -17.65327 | -43.88395 | 2025-11-21 00:09:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d51bfc88-e687-314a-9c22-c2416dbb36bc | -18.27439 | -42.3747 | 2025-11-21 00:09:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| cd86fd31-ab83-3031-84ab-7b11628793d7 | -23.89218 | -53.00213 | 2025-11-21 00:09:00 | TERRA_M-M | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 219.9 |
| e94a99fa-eedb-36c3-9db0-9d42a5a7202b | -23.89142 | -52.99731 | 2025-11-21 00:09:00 | TERRA_M-M | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 201.0 |
| d955aa72-c207-3395-82e2-2c7050e66a9b | -21.06897 | -48.75314 | 2025-11-21 00:09:00 | TERRA_M-M | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| 52b6e6dc-71e4-389d-836c-e00177c48e65 | -22.03402 | -47.19314 | 2025-11-21 00:09:00 | TERRA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| af98db39-907b-3753-ba3a-f86d81b123ca | -22.52163 | -44.32238 | 2025-11-21 00:09:00 | TERRA_M-M | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 8be0417a-0928-36ac-9640-dab62962989a | -21.28922 | -49.65857 | 2025-11-21 00:09:00 | TERRA_M-M | ADOLFO | SÃO PAULO | Brasil | 3500204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 7aae612c-be44-3545-afe2-8ef2873aa042 | -22.9158 | -48.67436 | 2025-11-21 00:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 45ff924c-c507-31b6-8e2e-03e075a59cf1 | -22.92874 | -48.67309 | 2025-11-21 00:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 35.8 |
| aacfa297-05c9-3be0-8b16-ae8bce00806a | -21.0364 | -48.55505 | 2025-11-21 00:09:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.2 |
| 2e31f3ae-b585-3f97-bbba-f9ae1399daa1 | -18.91714 | -47.17376 | 2025-11-21 00:09:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 84fc19f5-4d9a-3070-a67d-e6a612288425 | -21.37678 | -48.59773 | 2025-11-21 00:09:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| bf702a6b-5cc2-3877-ab5f-ce1ee3cc9e48 | -21.19966 | -48.62388 | 2025-11-21 00:09:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| dae9f6c1-9e7f-3c3b-91fa-44b9dc82dc3c | -18.0539 | -39.59706 | 2025-11-21 00:09:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| ccda62e8-cde9-3b1d-9f2f-9ea8f6077569 | -19.8529 | -46.30655 | 2025-11-21 00:09:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5b4a2f3d-4c31-305d-8c26-c622ad9a4a13 | -17.81095 | -44.31244 | 2025-11-21 00:09:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 921a0ae0-d50d-34ae-a0d1-c1c04570d4e2 | -22.92942 | -48.68818 | 2025-11-21 00:09:00 | TERRA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 1add3a9e-89f1-332c-b968-cae9e9db4270 | -16.41742 | -43.12824 | 2025-11-21 00:11:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 99d35f7f-d967-31cd-bcc9-0aac79cfd00a | -16.52209 | -43.54677 | 2025-11-21 00:11:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 19763a56-6ceb-3b52-b06a-5369792b68ac | -17.71989 | -48.0833 | 2025-11-21 00:11:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e5fd7e04-389e-3a16-8f32-c230a1551d42 | -13.78512 | -49.59001 | 2025-11-21 00:11:00 | TERRA_M-M | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| eff33f2f-72a4-3c5a-83b3-cfb0fd8dcb4b | -14.9431 | -47.5131 | 2025-11-21 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a96af584-ce47-352d-bea5-21efdb414188 | -14.52307 | -49.34088 | 2025-11-21 00:11:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 9f706268-b850-38f4-833a-9aaa1ff14cd7 | -13.78308 | -49.57233 | 2025-11-21 00:11:00 | TERRA_M-M | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| c79959da-35c3-3ec5-a932-12acc0ff28c5 | -14.95362 | -47.51204 | 2025-11-21 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 39.7 |
| f077102c-b584-337e-8dcb-d7d4ae9b5630 | -16.63165 | -43.47732 | 2025-11-21 00:11:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 05ed2c8e-da44-3f09-85f9-66475d6ea445 | -13.70613 | -48.42554 | 2025-11-21 00:11:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7c2054bd-7c65-3916-8545-43b0f372f711 | -15.44841 | -43.83672 | 2025-11-21 00:11:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea8338e7-001e-3dd6-ba2d-d3f1dda7ea04 | -13.70486 | -48.43136 | 2025-11-21 00:11:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 818ed830-76ce-39e7-bea4-99c1bc8fbd4a | -12.49926 | -47.44021 | 2025-11-21 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4a9eb08e-97ff-32dc-80f4-e4019c771bf8 | -17.57725 | -46.67366 | 2025-11-21 00:11:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fcea74d4-b3ff-324a-8af8-602f95e7d71a | -13.80251 | -50.64475 | 2025-11-21 00:11:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| fe5942e5-2252-33a2-8e39-5e910ec408e9 | -17.58904 | -46.68489 | 2025-11-21 00:11:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b120dd33-ab0f-32bb-8546-6f0e10eacc9f | -13.74275 | -48.4511 | 2025-11-21 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0162d7e5-17d8-3868-a24b-59a25d6ec32e | -12.23287 | -49.38865 | 2025-11-21 00:11:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 9c0c11c8-25a3-30a2-811f-635cd3da47ef | -16.38953 | -44.06033 | 2025-11-21 00:11:00 | TERRA_M-M | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f39d3940-775a-367c-9c89-4fb96b5a169d | -3.7086 | -43.34356 | 2025-11-21 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f23aa114-abd5-3806-8b5b-b141c0ce120d | -3.14027 | -40.1771 | 2025-11-21 00:13:00 | TERRA_M-M | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 671e783d-481d-3cd9-9361-3682372b41f6 | -3.26361 | -45.75871 | 2025-11-21 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 069da976-9071-391f-b9b4-b4bda5badab5 | -4.00489 | -42.47598 | 2025-11-21 00:13:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 16eddffe-c055-35b4-947f-8efd50f57c9a | -2.98026 | -44.58728 | 2025-11-21 00:13:00 | TERRA_M-M | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9ef1d20-bfe8-32ce-81f8-b283eac5fbdd | -5.71667 | -46.24686 | 2025-11-21 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d659fe6-5715-38c4-b1e0-187b4ef94289 | -5.5012 | -46.35901 | 2025-11-21 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9c3442c2-7c81-3021-8325-82fc2971cab4 | -3.18049 | -44.3086 | 2025-11-21 00:13:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5b254c00-e74b-3231-9c85-1988bea4a625 | -3.46105 | -43.40777 | 2025-11-21 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7eb191f8-bfc0-3937-8cf7-e03ec74ebdd4 | -3.16043 | -44.88903 | 2025-11-21 00:13:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8e5d5f4-f87c-3020-bd05-87381d361477 | -6.80158 | -39.5536 | 2025-11-21 00:13:00 | TERRA_M-M | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 06c165c7-f0b6-3a59-bd23-20894e162688 | -3.35214 | -45.00725 | 2025-11-21 00:13:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 35b8a3b4-3150-3fdf-91f7-401cd35772e3 | -3.66079 | -42.20482 | 2025-11-21 00:13:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 1378e7ad-2958-35e8-8d86-f5e7cb3bf507 | -5.03508 | -43.60715 | 2025-11-21 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 78091e1e-4a16-3c0d-996e-52e92b2df3a5 | -3.53781 | -42.50221 | 2025-11-21 00:13:00 | TERRA_M-M | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 3710b011-5540-3515-92d2-dc4294c55fce | -5.03369 | -43.59727 | 2025-11-21 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 74b0ed63-d069-309a-9d45-4a1ef215072a | -3.80524 | -39.52901 | 2025-11-21 00:13:00 | TERRA_M-M | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 6ad9700b-02b8-334e-803a-dc6c9a825bbf | -2.90358 | -45.364 | 2025-11-21 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2730f319-569f-3f03-b9ae-f83b5be15b85 | -3.72569 | -42.16414 | 2025-11-21 00:13:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 47abbae3-cad6-3bb4-b998-848a6dacc3cc | -2.82793 | -45.41705 | 2025-11-21 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 7d339e6d-5e70-3922-99ef-78343f7276e0 | -3.1416 | -45.34837 | 2025-11-21 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6feebc23-8ece-396f-9803-f5ff352d296c | -3.2045 | -45.47556 | 2025-11-21 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c6da6f4a-4ec7-3a53-b62e-2724892c99c0 | -4.0066 | -42.48778 | 2025-11-21 00:13:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 5f72bb3c-61f8-3dd1-b633-4686269fc76e | -3.21414 | -45.46823 | 2025-11-21 00:13:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bd953e36-510f-3cb3-8b5a-6ed3e485aa09 | -2.74977 | -45.18119 | 2025-11-21 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 35.8 |
| cebc020b-5721-37f3-8493-0953b9bbfc8e | -6.16711 | -46.10733 | 2025-11-21 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b82e1d37-4baf-36e7-b623-1f0210cb92ea | -3.32101 | -45.5734 | 2025-11-21 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 051098b1-086b-3d09-bfd7-01511c9bc909 | -5.02436 | -43.59866 | 2025-11-21 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0d3a5eb4-230e-33ff-acc2-0ee4bd704377 | -4.04849 | -46.03928 | 2025-11-21 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4f9138e5-a350-3fc6-beaf-3585d60c8805 | -5.72822 | -39.39769 | 2025-11-21 00:13:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 90b63bfe-497e-3d24-82d1-7ca74eedaa45 | -2.75103 | -45.19021 | 2025-11-21 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 29.8 |
| bfbf80a6-1adc-3382-a2eb-a8d3a03d0396 | -6.75151 | -44.21545 | 2025-11-21 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 166068f7-6ba4-341a-9c3b-5b4bd37fed47 | -3.30342 | -43.52811 | 2025-11-21 00:13:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7098399e-aeb5-3e10-8cc3-aec1e9f9deed | -3.04654 | -45.06582 | 2025-11-21 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dee880d1-c67a-3d92-8c44-d0d015d7c0c9 | -3.34191 | -44.99947 | 2025-11-21 00:13:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b61d08e5-bcf8-381d-9f70-06645f1ed786 | -3.80246 | -39.51004 | 2025-11-21 00:13:00 | TERRA_M-M | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 22.4 |
| bdb9318f-c4f9-3220-94f8-645c0c3de7ac | -2.89592 | -45.37418 | 2025-11-21 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 373acc7a-3a7e-36e7-a605-bf6bc8cf29e1 | -6.16589 | -46.09837 | 2025-11-21 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 036220d2-3311-31e1-af7b-7af0876053fb | -5.50243 | -46.36798 | 2025-11-21 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d1c811b9-886b-3fac-aa20-e63d97d2b8c2 | -5.20806 | -42.16006 | 2025-11-21 00:13:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 5fe1a542-9aa2-38ea-9106-600ae702e074 | -4.05124 | -45.99402 | 2025-11-21 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c37f3f1e-cf07-3155-85c4-a8206d1de704 | -5.73929 | -39.40252 | 2025-11-21 00:13:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 0e71e892-df68-32ae-ba3d-f88fb22432a0 | -6.31689 | -39.66692 | 2025-11-21 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 988e685f-8a18-3fb1-906c-00cc56de016b | -3.48234 | -45.8773 | 2025-11-21 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9d1f6471-1e0a-3464-9e8c-b165ccfe96e8 | -6.28307 | -39.68907 | 2025-11-21 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 6a932b00-7dbd-31d7-89db-890c746d20cd | -3.08359 | -45.72439 | 2025-11-21 00:13:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a8be3de8-48b0-3df6-aa59-44a834208be1 | -3.46253 | -43.41835 | 2025-11-21 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 83bb4b72-3b8f-3cd7-89a9-200ada8d7720 | -3.31978 | -45.56456 | 2025-11-21 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 0dd2182a-172f-3e0e-b2fb-d88dade22833 | -2.89468 | -45.36525 | 2025-11-21 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9220c539-6628-3f42-9eba-0f28a9971945 | -3.30831 | -43.53201 | 2025-11-21 00:13:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |


[Clique aqui para ver as próximas entradas](README2.md)
