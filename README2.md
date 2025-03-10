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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c3ff73b-b498-32d2-bb36-22fff5e53cad | -22.9357 | -42.97301 | 2025-03-10 03:53:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 45bf31db-9881-35ab-afdf-aa5bd3f22da2 | -22.48199 | -47.40736 | 2025-03-10 03:53:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dcaa69d0-1d96-3f9f-8f22-937b37736cf5 | -22.80729 | -42.47358 | 2025-03-10 03:53:00 | NPP-375D | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aec3e982-a5ff-3dcc-b183-52d1d0adff36 | -23.26126 | -46.04781 | 2025-03-10 03:53:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c10314ef-0e8b-3b2f-ae9a-8b1de31e3a96 | -22.80112 | -42.46836 | 2025-03-10 03:53:00 | NPP-375D | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9c463ab2-e162-3ea4-91aa-40b2f6e58bfb | -22.93224 | -42.97234 | 2025-03-10 03:53:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1705fefd-16cd-363d-8afb-b294c703220f | -23.46941 | -45.85905 | 2025-03-10 03:53:00 | NPP-375D | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a54a8436-7c7e-3088-a777-3c79e794af0b | -22.80386 | -42.47299 | 2025-03-10 03:53:00 | NPP-375D | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a7e131d6-b453-3cef-ab01-ea148401eca0 | -23.56783 | -45.87221 | 2025-03-10 03:53:00 | NPP-375D | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 72d4637d-6962-38f7-b700-4d5958fe6783 | -23.26221 | -46.04914 | 2025-03-10 03:53:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0003bbc6-ee5a-3093-86a3-b3f4d2ee7cbe | -22.48636 | -47.40839 | 2025-03-10 03:53:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b53ac93a-86d7-3572-9367-4a6634fbb030 | -22.80795 | -42.46962 | 2025-03-10 03:53:00 | NPP-375D | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d2d34ce2-e032-3c88-a6ba-8009bda16433 | -11.64227 | -37.78984 | 2025-03-10 04:12:00 | NOAA-20 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 15adc1f2-113f-3ee6-871a-602b01ce20b7 | -9.47147 | -46.5092 | 2025-03-10 04:12:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7aa80407-074f-34ec-abd0-a0d48f97a6b2 | -14.20215 | -45.76632 | 2025-03-10 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01a62f06-c990-3795-b996-6ea849157fde | -12.26906 | -46.00445 | 2025-03-10 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cfa94fd-fa53-3b79-bfd0-22999785692f | -17.77986 | -42.80682 | 2025-03-10 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bc3270c-38a3-37f1-aeea-8056edd38cf0 | -17.59434 | -43.19718 | 2025-03-10 04:14:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab9d1372-65d2-3fc0-8634-60a6b6a8c9bc | -12.49691 | -45.52684 | 2025-03-10 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdcf2d40-f79d-3126-ac12-35c6fa8577e5 | -16.6788 | -43.88493 | 2025-03-10 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a44b3406-78e1-3666-8bb2-764c368bd40b | -15.72464 | -44.97344 | 2025-03-10 04:14:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 263aee4a-ac41-3e45-87cc-e25d6b1c2ae2 | -14.224 | -41.59936 | 2025-03-10 04:14:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 22efd80f-9f69-3662-ae70-a74497440a0a | -16.68217 | -43.88549 | 2025-03-10 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3c7dbca-36f5-30d2-b7be-8c39cfc9188e | -11.63715 | -41.75586 | 2025-03-10 04:14:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dab38730-2a97-3e67-b730-9747ad26ae30 | -17.12122 | -42.89714 | 2025-03-10 04:14:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 792aaaff-1ee2-33f9-a6f3-32053e622979 | -13.30579 | -40.22126 | 2025-03-10 04:14:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2462238-dbc2-31e3-b0b6-27fa8022be80 | -17.82089 | -43.61474 | 2025-03-10 04:14:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bfd8a72-a0d5-3380-9592-30073c23812f | -16.5554 | -43.20972 | 2025-03-10 04:14:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea934d86-ebab-3725-808b-66d0d2fa6058 | -14.22762 | -41.59985 | 2025-03-10 04:14:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 52c1d954-2144-3158-bb32-a5a1254914c7 | -12.49749 | -45.52325 | 2025-03-10 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74acbe3e-82e9-3971-8e8c-1b44380b2c89 | -16.52168 | -44.09366 | 2025-03-10 04:14:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fbbfada-2574-3307-8193-50917cb4b2b4 | -15.90777 | -46.08823 | 2025-03-10 04:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f038710-87f9-3f89-a01a-2e0390b4b814 | -14.20273 | -45.76273 | 2025-03-10 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea3da189-396f-3062-8b45-bfb162700c5d | -18.02085 | -43.29227 | 2025-03-10 04:14:00 | NOAA-20 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d5db5da-aef5-358e-b1f5-9ecdf4a302b1 | -15.07726 | -48.94519 | 2025-03-10 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7656fbe9-b8d8-357a-b455-dbf849a46393 | -14.20997 | -45.76022 | 2025-03-10 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f86c154a-b2cc-33d9-911c-4ec939916f7a | -17.09365 | -43.80291 | 2025-03-10 04:14:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38cc41f0-d7e2-30d8-9704-fc0411f8bfeb | -14.72641 | -42.88002 | 2025-03-10 04:14:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| edd26513-2b79-319e-ae54-bde6b2334d8d | -23.5382 | -51.44917 | 2025-03-10 04:17:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 92834688-ad90-3a75-a2c2-f4e2862106bb | -22.90313 | -43.75323 | 2025-03-10 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8855e0af-c6c8-3696-a8f7-f6f5039ac47a | -18.48743 | -48.3724 | 2025-03-10 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0480370c-fc35-36f5-8acd-62b30207028b | -21.62162 | -48.7432 | 2025-03-10 04:17:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a95e2313-325a-326c-91b9-151b525fe942 | -22.77096 | -41.93681 | 2025-03-10 04:17:00 | NOAA-20 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3d24ba11-03bc-3f76-ad1a-fa6aad41b463 | -19.4494 | -44.91587 | 2025-03-10 04:17:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcf28be5-09b3-38ea-afbd-e1333afe7dff | -24.0188 | -51.07167 | 2025-03-10 04:17:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1773c450-c569-3d29-bc3c-afcaa0e8c180 | -23.35211 | -52.30647 | 2025-03-10 04:17:00 | NOAA-20 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3d9a744a-70d6-3a6d-992c-f7e7e8100d79 | -21.61752 | -48.74649 | 2025-03-10 04:17:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5418425a-b612-3a49-ac4f-23901bd6c00b | -21.62094 | -48.74715 | 2025-03-10 04:17:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6faa71a7-d830-3bf1-a0d2-cec494f2981c | -22.80639 | -42.47309 | 2025-03-10 04:17:00 | NOAA-20 | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1bdf0c36-2877-3759-920c-ecd59b2b7628 | -24.01927 | -51.07465 | 2025-03-10 04:17:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5098a36c-3cc1-39f4-a915-5fff8d933d3b | -30.14995 | -52.02376 | 2025-03-10 04:17:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 0c746813-9149-3ffe-9aa0-e0fc8208402d | -19.96982 | -44.21525 | 2025-03-10 04:17:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 07058856-05cb-3252-bd47-c08503f57e1b | -21.61819 | -48.74253 | 2025-03-10 04:17:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 133de34b-29eb-3f9c-81cc-32c5a7544194 | -22.89955 | -43.75267 | 2025-03-10 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1fe4027b-24d5-3540-b4f6-a1325cdfd6d5 | -20.76401 | -46.76842 | 2025-03-10 04:17:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eb823d60-6184-3062-b731-7180fb28ec30 | -23.54228 | -53.36794 | 2025-03-10 04:17:00 | NOAA-20 | IVATÉ | PARANÁ | Brasil | 4111555 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0de49f56-a460-3f7e-8511-f3e113afac7a | -22.46966 | -48.27876 | 2025-03-10 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cfee9c4-15f4-337c-b240-b83220259517 | -20.72352 | -49.43419 | 2025-03-10 04:17:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d10cb20-23f6-3bb9-a6d5-f82e831f4cb9 | -19.43751 | -44.33944 | 2025-03-10 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85e594a3-0ae6-3403-9571-bd4fe1b67fd8 | -22.78682 | -43.75888 | 2025-03-10 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0306d193-e750-3d20-bdee-553a93119ac2 | -23.50138 | -46.41548 | 2025-03-10 04:17:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 397eb05a-d367-302a-b4a9-80cb78dbd537 | -20.41495 | -43.55126 | 2025-03-10 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d0706d71-5d85-3cb4-a44b-3f7e1ed7f320 | -24.67019 | -51.90679 | 2025-03-10 04:17:00 | NOAA-20 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c2ba4b5a-0df1-3e6d-b9de-e1c9ba999be6 | -22.48326 | -47.40749 | 2025-03-10 04:17:00 | NOAA-20 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5ec31147-1baf-380a-b1ce-f4e1c29a67fb | -20.07341 | -44.22306 | 2025-03-10 04:17:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3fe30f65-b75b-3a2f-9c38-3d950b437a01 | -20.07684 | -44.22364 | 2025-03-10 04:17:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9ee0905b-902a-373a-abd3-2d2bb5e9d994 | -23.56747 | -45.87152 | 2025-03-10 04:17:00 | NOAA-20 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 233c9632-07b9-3a35-8473-b6a861bccc1b | -22.85554 | -42.97943 | 2025-03-10 04:17:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e3101974-af29-3e6e-905c-e51491475336 | -18.48677 | -48.37626 | 2025-03-10 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a8e880c-434e-3286-a01c-86c397e19f5d | -23.54147 | -53.37209 | 2025-03-10 04:17:00 | NOAA-20 | IVATÉ | PARANÁ | Brasil | 4111555 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d1eb2ff9-d90f-3948-b0e8-f6f5d03b5515 | -22.47031 | -48.27491 | 2025-03-10 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a57584b8-ba37-314a-bbb2-0bdf8ddfb130 | -19.83371 | -40.11407 | 2025-03-10 04:17:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e96cf252-93fc-3cd7-b915-9f3106ba7a2c | -21.61684 | -48.75045 | 2025-03-10 04:17:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b08e5673-1201-3096-84b0-9354920f1c79 | -30.3234 | -53.42199 | 2025-03-10 04:17:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 886e6c8a-7db0-30e2-af1a-7890d8a46c38 | -23.35112 | -52.30244 | 2025-03-10 04:17:00 | NOAA-20 | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 86b1aa65-fdd9-36e1-b62c-e3070b8d6ad6 | -23.46841 | -45.85513 | 2025-03-10 04:17:00 | NOAA-20 | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ab2fcf54-9315-34ac-a4ab-535b96fcb947 | -23.56413 | -45.87091 | 2025-03-10 04:17:00 | NOAA-20 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 69f8594d-ffe0-3368-8efd-ecfe647a7eb6 | -24.01515 | -51.07081 | 2025-03-10 04:17:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 076bf425-fa7d-3f63-bbb8-90a0a54f1dd4 | -22.79942 | -42.46666 | 2025-03-10 04:17:00 | NOAA-20 | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 05450ca3-5f59-3051-aa57-c25bdc18133e | -20.41847 | -43.55178 | 2025-03-10 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aca7fe1a-2689-3dfe-9ddd-0cee30a9212b | -24.01562 | -51.07381 | 2025-03-10 04:17:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2a8bff6f-f4e3-3bf3-abc7-ae3adeb5d1c5 | -22.80705 | -42.46799 | 2025-03-10 04:17:00 | NOAA-20 | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 230193e2-61dc-3ee9-9b05-fed08af8e354 | -22.77028 | -41.94223 | 2025-03-10 04:17:00 | NOAA-20 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f6541fa1-7f2d-3e4d-905b-e3b897606e58 | -25.7928 | -51.09693 | 2025-03-10 04:19:00 | NOAA-20 | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e887d289-b38a-38d8-a73d-a4c0783ff19c | -31.73001 | -53.90405 | 2025-03-10 04:19:00 | NOAA-20 | HULHA NEGRA | RIO GRANDE DO SUL | Brasil | 4309654 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| dda77416-fc6d-300d-8619-5be0ea3a735f | -8.31746 | -55.11617 | 2025-03-10 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d6c2a1a0-12fb-3eb4-ad02-e0db95e97d86 | -9.12787 | -61.46503 | 2025-03-10 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87101783-080a-3f94-8401-cab1bd37452f | -9.92458 | -59.9027 | 2025-03-10 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1777057f-e6ff-37ab-90a2-8a24291bac12 | -9.18714 | -61.38177 | 2025-03-10 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 89ec8831-fe4e-36fd-814a-324bec743dbd | -9.92819 | -59.90331 | 2025-03-10 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60caef91-1c9c-388c-9b8a-b8a542fb5b45 | -9.92096 | -59.90209 | 2025-03-10 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bdd36a0-850f-3a2a-97f9-978a086caa0b | -9.18656 | -61.38528 | 2025-03-10 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ae50750b-d0c9-3ec0-ac71-53437cd2f962 | -11.64462 | -54.37944 | 2025-03-10 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d7d2cb7-0e8c-3894-8aaf-a56608ba7646 | -9.58076 | -57.39734 | 2025-03-10 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eceef748-5853-34ab-a60f-f4b08e8ac5da | -16.68069 | -43.8837 | 2025-03-10 05:06:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6586dc7-4b44-38cf-be17-edd165d7321d | -23.35424 | -52.30556 | 2025-03-10 05:08:00 | NOAA-21 | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9b8f622f-5761-3c83-a2bf-3b2fe9bc5bc8 | -20.72517 | -49.43525 | 2025-03-10 05:08:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4474a29-6a7d-35f3-a5f9-72877de7ae3a | -20.47885 | -53.6753 | 2025-03-10 05:08:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cabd3db-436a-3788-b0d6-0c031d473225 | -20.47859 | -53.67673 | 2025-03-10 05:08:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a374a96a-c7ef-3c8e-9592-3e17d874323b | -24.24519 | -50.74097 | 2025-03-10 05:10:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README3.md)
