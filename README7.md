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
| 4bd03458-e41d-3ad6-996b-edc9af1e7123 | -6.4212 | -44.66663 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccc53fbd-976c-3741-8bc1-f4ea8bee8553 | -6.94251 | -44.56096 | 2025-08-22 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56d3a9e2-2be0-388b-811f-dbc58321ea6b | -6.42065 | -44.23266 | 2025-08-22 03:30:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae1bc631-a076-361d-b3b2-cc817dae0983 | -6.29527 | -43.88886 | 2025-08-22 03:30:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69fcdfa6-8df4-3db8-9f57-a53601982c1e | -4.39787 | -44.08605 | 2025-08-22 03:30:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c9087d95-17b5-3fc7-aa58-627c569e4946 | -3.82 | -41.56328 | 2025-08-22 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5ed25add-fa27-39f0-b9d1-074e4e984d76 | -9.06736 | -43.00143 | 2025-08-22 03:30:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0be388f2-fc8c-3768-812f-abbd65d45090 | -4.39746 | -44.09277 | 2025-08-22 03:30:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b42c4805-c893-3f15-8064-3e9a5f9f2a86 | -6.57601 | -44.73212 | 2025-08-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f419da40-ac04-3ee4-a988-ee276bd84070 | -5.79322 | -45.07803 | 2025-08-22 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3292dab1-d96f-3e49-a818-292c04a49eaf | -5.13963 | -45.17901 | 2025-08-22 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c945ebae-c42e-3def-9e6a-17b8b72cd990 | -5.70137 | -43.54098 | 2025-08-22 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f7a7dd5-49da-38d5-8f9d-0a99bc3335f4 | -5.13992 | -45.17913 | 2025-08-22 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7f2476a-da14-352d-984f-528f969f3be3 | -7.14999 | -43.22913 | 2025-08-22 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a009cd3-0232-3265-ab10-6b37804d6894 | -6.27324 | -39.69453 | 2025-08-22 03:30:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7be0995c-363e-3f76-8b6a-2d7e70903cf6 | -7.14425 | -44.17358 | 2025-08-22 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1193120c-56ac-321b-82b0-0a7ab8922856 | -5.79237 | -45.071 | 2025-08-22 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b41ef8b2-b376-337a-98fd-71c7affa488e | -7.02456 | -44.62497 | 2025-08-22 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ef6cfe1-eb79-35da-88b6-6f209c5c7d96 | -5.73035 | -38.98609 | 2025-08-22 03:30:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| f07ee4f8-e0a4-3a42-ad50-1f32b2589b43 | -4.64037 | -41.40596 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 19d98de4-05c1-3bcb-9c3d-ce2c8717ce07 | -4.65659 | -41.41014 | 2025-08-22 03:30:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4805b72a-7b09-3329-a027-aad81bc2e93d | -12.95637 | -46.27562 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e390830-8c51-3318-bfad-0bb94b12238a | -15.44708 | -39.29599 | 2025-08-22 03:32:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4bf65184-03b4-3985-ae7e-7c09e66aa238 | -12.99827 | -45.23635 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fe1b1935-dd34-3b04-beda-485cb5230a8d | -14.76499 | -45.40548 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 09ab838d-f869-33c1-ab1a-6e563c6203e0 | -10.96904 | -45.6176 | 2025-08-22 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2931af82-95f3-3d51-a85c-54cb929e3372 | -13.64534 | -45.70597 | 2025-08-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47093df2-3191-3c7a-88ad-31a7d4e82050 | -12.09296 | -43.34475 | 2025-08-22 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b90f9f77-f477-3460-88dc-83211f7ed26f | -12.92526 | -46.16772 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b516e218-7fba-3c8d-af57-23c8d7e75386 | -13.03054 | -46.33963 | 2025-08-22 03:32:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 64fa755f-a4d4-3c3a-80e3-5d9eda6aaf0e | -12.99922 | -45.23163 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 174f7472-a297-3de9-b724-f6e8647091e6 | -15.89338 | -43.46251 | 2025-08-22 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 9a864263-3667-3a7f-adfc-260f7e72a6f1 | -11.81698 | -44.25346 | 2025-08-22 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e5e8f3b-e69d-3873-a533-907c00752688 | -11.31756 | -44.94168 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49bf94ad-1462-3b49-b2a2-bb7d4e914bcb | -13.37222 | -47.50148 | 2025-08-22 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e57db52-5ecb-30d4-82ef-1218ec10c120 | -13.00016 | -45.2269 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a4f811f-5581-3bcc-b77b-0d6edcb181fd | -12.09367 | -43.34114 | 2025-08-22 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30ce7b4b-586f-34f6-a494-0bba12c24c7c | -12.57461 | -41.27747 | 2025-08-22 03:32:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 05369dd9-be5a-36a9-8dc7-621845487c70 | -14.7662 | -45.42957 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b2cfb98-0418-34bb-9847-806862fb84b7 | -12.94929 | -46.27729 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4dd921c1-ba0c-3d44-bf92-248d8223716f | -13.90904 | -43.88758 | 2025-08-22 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d548409-d4a9-386f-97e8-31463e4cee82 | -14.76527 | -45.43405 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe2e3eb4-3119-3ce9-a1d7-75945bdaf788 | -13.65257 | -45.70782 | 2025-08-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1bfeeb02-fd1c-3ec1-a94a-8a5b6585afc3 | -10.96995 | -45.61668 | 2025-08-22 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 549d93b1-a15f-3255-8883-2e696feb7fcd | -10.97214 | -45.60597 | 2025-08-22 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ef02e15e-15fa-3f32-b269-18d8ef0486ed | -13.00541 | -45.23558 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ee5ab50e-e016-33f7-9cc0-24f73cf732c1 | -12.99695 | -45.21148 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31ba48dc-546d-3ec0-a37b-8149d773686b | -11.31567 | -44.95134 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18194616-1a71-3dfa-94c4-d9c7fb16f05b | -10.97114 | -45.60693 | 2025-08-22 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6bf574b1-d4b1-3eca-847c-adade2b123b3 | -12.93548 | -46.1828 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5cb8cdb3-b846-3d62-a92a-dcd9df4e86fe | -14.76309 | -45.41464 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8a1f5086-6f64-31d6-8f53-28165e47bd50 | -13.64428 | -45.71099 | 2025-08-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c480dc66-a59e-39ab-ae33-5752e45aa785 | -12.00803 | -44.67105 | 2025-08-22 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ac10c81-480f-3214-a343-549971d2a2bc | -12.10772 | -41.07717 | 2025-08-22 03:32:00 | NOAA-21 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3ad7300b-68d2-38a8-b151-e03b91a06538 | -11.85751 | -44.84196 | 2025-08-22 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ddedec53-829f-3ead-ab49-c2e83ade1168 | -13.00131 | -45.22491 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 383b1041-4d85-366e-b914-79c099b191ef | -13.38055 | -47.49685 | 2025-08-22 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 93b0a362-572e-37d5-98b8-36db062691c9 | -13.50028 | -47.0635 | 2025-08-22 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9a6f53b-4bc1-31ab-80b4-8f14222c6462 | -14.76214 | -45.41924 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54ba9b10-6697-3e13-9292-35281ca224cd | -13.64323 | -45.71594 | 2025-08-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 423f02cb-94fc-32ae-8003-52f5935508f4 | -11.31548 | -44.94879 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6028ed9c-e031-33bd-8ea6-2841ee832e05 | -13.02888 | -46.31543 | 2025-08-22 03:32:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7693ea19-715d-3d4d-8a1e-44e415a8f685 | -13.64293 | -46.88378 | 2025-08-22 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b037ac9-8071-3c14-b8ba-41ee199eefe2 | -14.88235 | -48.0499 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 94a5cce7-596c-3cff-9343-0bdd29f6df2e | -13.03035 | -45.20652 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71a619fc-084c-3a17-a11b-bde20d6d28de | -15.13587 | -48.10716 | 2025-08-22 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4bc00657-0fb7-352a-a36f-ae14ea233021 | -11.27691 | -44.95364 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed0bb2c4-8fc2-30f6-ba05-30be7b1db8d0 | -9.58901 | -43.32806 | 2025-08-22 03:32:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e421bd1a-085f-3528-a1ac-35b0591d3d96 | -13.01802 | -45.17467 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bdf9267-1644-385b-84e8-eee406e0b439 | -13.36502 | -46.25757 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bf87774-376c-3de7-90ae-cbb2fbaad8e2 | -12.98613 | -45.23391 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97161a06-77ee-3fb7-b34a-e1bb4a14c71a | -13.00205 | -45.21748 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1eb8e95-6014-30f7-8dbc-40b02e3ead06 | -16.61457 | -43.3605 | 2025-08-22 03:32:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ddeb40a-9f44-36ff-acab-69c6e10f8bdd | -12.98622 | -45.23664 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 97641faa-b247-3a4f-8629-848174bd36c3 | -12.91903 | -46.16549 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ede1104-fc98-39dc-86fa-15d4467bba2d | -14.88152 | -47.95796 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 25aadaa6-be44-340b-bcfa-c9cffb02e126 | -13.65155 | -45.70708 | 2025-08-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| daa0e99d-5363-3118-a1ca-10ebee6c6b53 | -10.97871 | -45.60242 | 2025-08-22 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fc6fdba-1e21-371b-b47c-8158ab099ff8 | -12.95748 | -46.27029 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 96924e31-3472-3077-af71-31cd57291217 | -13.02258 | -45.17776 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83b76ba4-a9c5-384f-8133-fbfd2f543227 | -11.30838 | -44.95232 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b280549-5088-354f-b8fb-92474c922def | -12.57374 | -41.27931 | 2025-08-22 03:32:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 84e4a0d5-0d05-3729-b442-091d1af73c29 | -15.44644 | -39.29951 | 2025-08-22 03:32:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e340b78a-cb9a-3751-8eee-63b779bb09ef | -12.92746 | -46.18557 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5cdd85b0-9b2d-34de-9f18-17fcc19bf093 | -11.44143 | -47.31593 | 2025-08-22 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0953c56c-627c-354e-88dc-52f889edeaaa | -13.65048 | -45.7121 | 2025-08-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a8c0aad0-815a-3804-9144-f882a57b943a | -12.95533 | -46.2806 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31a705e0-b3d2-38a4-8269-15dd1d51d882 | -13.02911 | -45.18196 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d094e1a-16a1-3244-9f31-b9aeba133799 | -12.92842 | -46.18452 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6db18fd9-067c-30d2-b713-7a7105458328 | -12.9525 | -46.29422 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ebc09420-106d-3f86-834c-9a3f97a24b3a | -12.92423 | -46.16856 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1e1156fb-6b39-3f54-99ee-c354e9a7bb38 | -11.81114 | -44.25231 | 2025-08-22 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1efe6265-fab3-3d8e-9433-c4922eb573f2 | -12.99131 | -45.24258 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 94117bb9-f30e-36a8-a540-c9f8f68f4324 | -14.83842 | -47.9253 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46f1f5ce-d1f5-3ffa-9640-b266eb8721f3 | -14.97039 | -47.14197 | 2025-08-22 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03d1c26a-f4d7-3071-a09a-6215fd8cd21a | -10.97768 | -45.60764 | 2025-08-22 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 75e366db-afdc-3829-bb25-9c636bcc0c6c | -14.76593 | -45.40093 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cd77bf9c-f9e1-389f-be7a-3e2ea8bc9337 | -12.98709 | -45.22914 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55cb7edf-4f1d-3397-a0b5-03c2702b66b2 | -14.75811 | -45.40879 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b17381e-2117-3bc0-8826-54d78344afe8 | -12.94746 | -46.28607 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README8.md)
