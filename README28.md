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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b433338-6432-3942-a33e-fe29b8ebf5a5 | -15.83667 | -47.69088 | 2026-09-01 03:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7dff6d05-13f4-38bb-a3d7-ac848e723420 | -15.65559 | -48.702 | 2026-09-01 03:57:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2aae61fa-df9a-3892-8692-51dfdf8c3f0d | -15.04018 | -48.17161 | 2026-09-01 03:57:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aadcac42-5733-3b6c-9363-e0d324e38a37 | -14.25835 | -52.86462 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 712c74a2-bc1b-366c-b9d7-6e4ba5f4efe5 | -14.26465 | -52.90286 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f91ca0b3-e652-37b0-9d83-67841a45d634 | -17.79089 | -39.70592 | 2026-09-01 03:57:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a149fd93-8911-305b-b9a2-554e09d2f005 | -20.54034 | -47.8033 | 2026-09-01 03:57:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba260b7f-d3ac-3323-86ec-44a923271eae | -14.46755 | -52.52912 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4d9cefec-d1b7-3094-af6f-860cd064fbd4 | -17.18388 | -48.71757 | 2026-09-01 03:57:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e533c414-50a4-3c2b-9178-2566834382d3 | -15.01668 | -52.77289 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7207832e-410d-3f13-9f5a-8fc619260264 | -17.31928 | -42.70423 | 2026-09-01 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb7a46f7-6fb9-30b7-ad51-08a46813ec77 | -14.26533 | -52.86614 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 80acd0a9-16c9-33ce-af00-d6a50db1be87 | -15.67156 | -48.70546 | 2026-09-01 03:57:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68abddc1-8d6f-37c4-a535-c8478524cf19 | -15.01019 | -52.77013 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7bc8896-8c7a-31e8-9764-e8f1036b3183 | -15.03279 | -48.18121 | 2026-09-01 03:57:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a99c6efd-f675-3908-a10d-a8ab477c86af | -16.47282 | -47.95485 | 2026-09-01 03:57:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 81e32620-b40e-3b64-810c-b4c61a671a7d | -14.45752 | -52.51132 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e029f0e1-a001-3700-afcd-df235753f1ed | -21.87169 | -42.03166 | 2026-09-01 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d215ac54-2c6d-3784-b529-876116da2ebc | -14.43583 | -52.51218 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce9a8a35-32c4-3694-a12b-bc3a7862d5d9 | -14.4289 | -52.51119 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4878b47f-99c0-38ef-a45a-fb3630491602 | -16.47828 | -47.95359 | 2026-09-01 03:57:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 23a044e9-de4b-322f-af9c-03a8510169e8 | -14.46888 | -52.52295 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c21ae21f-8466-369b-9214-018d08ab1584 | -20.54175 | -47.80185 | 2026-09-01 03:57:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99a559f7-4050-3c3d-83ac-b1b2f67cc87b | -17.17784 | -48.74726 | 2026-09-01 03:57:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 180d2f9e-08fc-313a-865f-58a72c3b5566 | -15.66209 | -45.90823 | 2026-09-01 03:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db286289-4a00-3807-b32b-f57931183310 | -15.59051 | -46.46368 | 2026-09-01 03:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7063f7f8-6649-3622-944c-3fd64d5e5cf2 | -14.45012 | -52.5105 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b677f315-23ca-3692-ad04-e82b295e2737 | -15.66103 | -48.70256 | 2026-09-01 03:57:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1351fdcb-70ff-3ef1-a475-aa9ff83f1a51 | -15.02504 | -52.76781 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35c9aba3-c477-37fe-aeb6-ffaeb7583b74 | -14.42823 | -52.51242 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e983a3e-0db4-3477-9153-e10481974a53 | -14.46817 | -52.52778 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f921ba15-99f9-398b-9280-e3aa6cda4018 | -14.2622 | -52.90176 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2373179-cfc1-3c88-ac90-c54787edcbbc | -15.41986 | -47.54804 | 2026-09-01 03:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18570a47-a910-39dc-8c5d-51e3da9782de | -14.47022 | -52.51676 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 36db3b13-615b-3f68-b029-5330bba18bd3 | -17.36993 | -44.87611 | 2026-09-01 03:57:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 363c982b-f27f-3b54-9357-14f184d2a04a | -14.50873 | -52.23975 | 2026-09-01 03:57:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17060337-3837-3270-9a07-6f8d17001a92 | -17.1401 | -46.8356 | 2026-09-01 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2dc5b74a-d998-385b-a1c4-2e2124edac28 | -15.60048 | -46.57676 | 2026-09-01 03:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d136be2f-4546-3ea6-a173-95553935b7c7 | -14.44402 | -52.50764 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b9b50f0-0e46-31a0-9bbb-a0470dc3590a | -15.84665 | -47.69281 | 2026-09-01 03:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66ef55fe-893c-362e-b381-f9674d635dbe | -16.3681 | -46.88055 | 2026-09-01 03:57:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f152f00-d50e-3e96-bce0-9bf7566b551c | -16.00303 | -43.55417 | 2026-09-01 03:57:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca27a050-7eca-3097-a0d6-89648233ad64 | -17.18906 | -54.30945 | 2026-09-01 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2b8fc36-84ea-3181-9658-80c2c2c03cbd | -18.45206 | -39.75569 | 2026-09-01 03:57:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 61e0080a-04df-3393-bb9d-2dac15a1b65e | -15.66604 | -47.27475 | 2026-09-01 03:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67f61ecf-0428-32e5-9068-c6fd66605e63 | -20.89913 | -43.29453 | 2026-09-01 03:57:00 | NOAA-20 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b13fb4d-9f45-3d51-bda9-b60c01500149 | -18.53068 | -42.16093 | 2026-09-01 03:57:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2af64c4f-db51-3a2f-91f6-cd1b08a8b3fe | -15.05979 | -47.99575 | 2026-09-01 03:57:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 668b0fb2-770e-3d7c-8f39-c417a8db4e1e | -16.70651 | -47.64069 | 2026-09-01 03:57:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3d8ef2f-1d4f-3627-8598-08a44333b670 | -17.7942 | -39.70649 | 2026-09-01 03:57:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 859ca3df-aacb-3bcd-a214-af194959dbcb | -14.50202 | -52.23822 | 2026-09-01 03:57:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 07c9db72-2314-3e85-8650-9d3a4bc117d4 | -14.27229 | -52.88948 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 607da284-43af-302f-b7de-e3649e79af84 | -15.65685 | -45.91151 | 2026-09-01 03:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65aafbae-1d13-32d1-afc0-88b5d10ba9c7 | -17.18458 | -48.7141 | 2026-09-01 03:57:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c1330e6d-ec2b-312c-9505-6bc3b3843b03 | -15.8376 | -47.6862 | 2026-09-01 03:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ab21b88-ea84-3164-bd75-65f7a8fc6479 | -14.27465 | -52.89058 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0e0a62e-a7d9-342d-9923-f5bc8a3d429a | -15.66168 | -48.69935 | 2026-09-01 03:57:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36f9dd93-e8b6-3578-afce-4b6795a45b66 | -14.25223 | -52.89255 | 2026-09-01 03:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ffd578a-7ad9-3990-b56e-c8d43209dca8 | -18.3037 | -45.08444 | 2026-09-01 03:57:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50409d04-ac9e-3632-95e0-ca3684961b43 | -15.84759 | -47.68809 | 2026-09-01 03:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 325942b1-abf6-3c02-9a2d-6e9f7242ff39 | -15.64959 | -50.10715 | 2026-09-01 03:57:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 887d6317-b9aa-3ed2-9c98-0585d0420aaf | -17.18741 | -54.31655 | 2026-09-01 03:57:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0c60f44-a9dc-3d68-9ba1-2e95df440f41 | -20.38212 | -41.60883 | 2026-09-01 03:57:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9068de79-ec80-31de-a69f-618b70f48e09 | -18.56699 | -41.27203 | 2026-09-01 03:57:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| da8336e5-3d10-3dc1-9b73-e39c641ad1fa | -18.94169 | -47.09876 | 2026-09-01 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 527cbe46-fc43-334f-97d2-96d4f73e2933 | -16.61109 | -43.37041 | 2026-09-01 03:57:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c294c63-5abe-35c0-9db9-b9b950ffcfa7 | -18.56761 | -41.26828 | 2026-09-01 03:57:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bbee5874-3569-3e54-91ff-e60df7329c1b | -16.47771 | -47.9565 | 2026-09-01 03:57:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5c16b7ab-84b1-3c80-965a-d5094c63628a | -20.38355 | -41.60841 | 2026-09-01 03:57:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| db101802-e52b-3343-8211-b68c07ed4b1a | -19.57309 | -45.71489 | 2026-09-01 03:57:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 560f37cc-a3dc-3b71-841c-06f9fb555781 | -15.01119 | -52.76541 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df7a17ca-84e5-3ebe-9f73-e2143d30c6ef | -15.8426 | -47.68711 | 2026-09-01 03:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 10051659-4320-3a69-9f94-fb0f80a53374 | -15.65763 | -45.90737 | 2026-09-01 03:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2380e14-b4aa-37f3-ab30-4dbe07e185a4 | -15.66223 | -45.95671 | 2026-09-01 03:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 116318cf-39ff-3a81-bef9-e5be0af9f4d3 | -16.08635 | -48.04771 | 2026-09-01 03:57:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4c3e0e8-4eb4-358f-9ba2-6479d189890c | -17.13157 | -46.85426 | 2026-09-01 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fd5f27a-15e0-3200-a15d-c6fdfb7fdade | -15.85163 | -47.69385 | 2026-09-01 03:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a3b6707-4a61-3cf2-a9b1-b6e7ae898774 | -17.37281 | -42.37386 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3eb34b65-e8ed-3aed-b648-382466f3f5c5 | -17.37634 | -42.37456 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c955af58-5828-393f-879c-c18ec83f85da | -16.59662 | -50.24338 | 2026-09-01 03:57:00 | NOAA-20 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efef7aad-2663-3d55-b996-ce2056546d35 | -17.13318 | -46.85203 | 2026-09-01 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6049c5fc-b452-3c17-b7fe-d4a685d15a32 | -18.94054 | -47.10155 | 2026-09-01 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d47161c-2ed6-34cf-8abb-3b038da55070 | -17.90275 | -50.64871 | 2026-09-01 03:57:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03422bce-e44a-3a64-baec-51ce00b69218 | -16.47458 | -47.94598 | 2026-09-01 03:57:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 21737c67-2b32-349d-bd6e-b056d4b235f3 | -15.59952 | -46.58172 | 2026-09-01 03:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d794192-560b-38bb-b323-0a501cea553a | -16.36341 | -46.87964 | 2026-09-01 03:57:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6c5fef6-6688-3f45-84a2-9852511bec79 | -15.64383 | -50.10563 | 2026-09-01 03:57:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 886b2b80-8627-39c9-925d-a5fe17106ae9 | -15.0097 | -52.77192 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4873272-184b-3a96-8ef0-f22859b7c418 | -15.06303 | -48.38353 | 2026-09-01 03:57:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb8a6f25-c132-3ac9-ba80-5f969046ea13 | -15.67442 | -45.91631 | 2026-09-01 03:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ab19f81-947d-3c35-aaed-647dba06ee1d | -14.38563 | -52.54321 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1f3e175-fdd7-38dc-babb-ed178d12aee8 | -15.65628 | -48.69857 | 2026-09-01 03:57:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 543a3d61-ad6b-364b-ade6-95373dc80391 | -14.46222 | -52.52067 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2a911464-ec73-3010-8bca-328e051ba226 | -21.87105 | -42.03548 | 2026-09-01 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0324edcb-1779-3848-8eef-f9f6171782be | -21.53007 | -48.62745 | 2026-09-01 03:57:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6e51306b-1476-3259-adff-171092a19a90 | -14.40943 | -52.50022 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fdf6381e-b2c6-3103-9754-057ab26f3e95 | -18.53414 | -42.16161 | 2026-09-01 03:57:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1551d791-bf06-34c9-bc76-d6cfecc20210 | -21.13321 | -42.34755 | 2026-09-01 03:57:00 | NOAA-20 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a50db433-d6d5-3758-bd33-1817392887f7 | -17.39054 | -42.35552 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a8e6dd99-88be-30c6-91e7-09d56393ad6f | -21.52536 | -48.62625 | 2026-09-01 03:57:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README29.md)
