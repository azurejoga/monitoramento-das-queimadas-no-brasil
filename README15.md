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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7130fd9-a698-3065-8e9c-b5aed0fe21ab | -15.10731 | -52.69112 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39954e89-01a4-33b7-b32d-1a3c0fe1202b | -12.61144 | -52.46304 | 2026-08-09 04:27:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56261c33-8413-399b-ba75-d7cc8351a78a | -14.04367 | -53.83825 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc1e5115-4a85-3368-8158-09a2a757c384 | -10.91796 | -57.12391 | 2026-08-09 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6695f38b-66c3-3a94-a025-d8d9b34c6c11 | -19.15256 | -43.49994 | 2026-08-09 04:27:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ca4cbe7-c431-3851-9a31-89745ab41c19 | -18.98481 | -48.41274 | 2026-08-09 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b27e4db0-c363-37e7-b363-cbecb851bac5 | -14.84518 | -60.07176 | 2026-08-09 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27a1b04d-f382-3893-8997-b474c9903b1a | -14.04459 | -53.83331 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58e12dcc-0779-361c-8f6b-d9f832f57d73 | -18.63744 | -49.87286 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| da3540e5-1017-3a04-a4d3-4167b399ebcc | -13.86594 | -53.67651 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 74823155-e9b7-37b1-9479-c834bf30bdb8 | -12.35209 | -53.15427 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23d082f5-53c0-3d2a-9ebf-5decb29b1703 | -14.15202 | -54.01075 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6335eebd-80e8-3324-8d52-160e7f5c3a5d | -18.63945 | -49.86105 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f66ac497-8bee-31ac-a4fa-fbd0c5929c39 | -13.85485 | -53.73412 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab7129f2-fa5b-3ec8-acf8-b2b42f1d36e8 | -17.76034 | -42.79996 | 2026-08-09 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41226f7c-f75e-3332-9299-7f5d28383079 | -14.31688 | -54.94414 | 2026-08-09 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e7e7929-7e2d-3cda-ab84-01add73f3176 | -10.91665 | -57.12004 | 2026-08-09 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f5ce46e-f013-3bd1-a69a-56e13fdafbdc | -16.18935 | -46.48459 | 2026-08-09 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7595cf27-43b9-3069-8d89-a07e484986e0 | -19.9356 | -44.37477 | 2026-08-09 04:27:00 | NOAA-20 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 72c7ffd5-562a-394e-8ce6-bd36520cad61 | -18.66096 | -40.78798 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d9fd4935-9493-382e-a0ee-099af4760b08 | -15.75535 | -48.41358 | 2026-08-09 04:27:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c972d019-15bc-3bc1-ba54-e32d06f871b2 | -15.87568 | -43.32948 | 2026-08-09 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4bad801-49a6-32a1-9701-6511d2ff71bd | -20.54423 | -42.39818 | 2026-08-09 04:27:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 22d092ad-d740-3972-b9df-4a37da19f4ae | -18.63124 | -49.86766 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f956a9cd-42ef-3a35-a292-a27501ca1ba6 | -15.64985 | -43.29089 | 2026-08-09 04:27:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9070f3ed-3583-3f38-a378-6ad51bc41492 | -14.90798 | -48.23106 | 2026-08-09 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cf87eee-0931-3ecd-a432-9f3419f176bf | -13.85097 | -53.7313 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0b9f005-f65b-31d7-a514-ab3ba89ec5f5 | -20.78905 | -57.70136 | 2026-08-09 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a31afa19-7887-3c3a-aceb-d68afaae77b8 | -21.3183 | -43.77696 | 2026-08-09 04:29:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 832ca341-25ec-3334-b2f6-dba83b7168e1 | -22.23238 | -43.03626 | 2026-08-09 04:29:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 38cccb7f-95de-3ab9-8c3c-7fe0291598e1 | -21.31898 | -43.77178 | 2026-08-09 04:29:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 54e81622-7e5e-3fdd-9f50-b5c08ff80287 | -21.67134 | -43.6082 | 2026-08-09 04:29:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 00a85147-ffd5-3490-8ca3-344d19c80e2c | -22.94059 | -43.4253 | 2026-08-09 04:29:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| abce15bd-602b-3f54-964b-1fa90d1cd047 | -21.27783 | -42.93578 | 2026-08-09 04:29:00 | NOAA-20 | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 524da12f-c33e-3f95-ba6e-7b99ae7ed271 | -22.2283 | -43.03559 | 2026-08-09 04:29:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e6f7a8ca-f656-3171-94d4-66703b47a485 | -20.80136 | -57.72301 | 2026-08-09 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 564babe8-be69-3b54-b3e2-d5d7dc6ef9f5 | -20.80097 | -57.72193 | 2026-08-09 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d6097fba-dd53-3fc5-b331-1ea74e558729 | -21.32215 | -43.7776 | 2026-08-09 04:29:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ca74b3ee-06c3-39bd-8f62-7231dc4e55d2 | -22.30109 | -42.60878 | 2026-08-09 04:29:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 02d7975c-738e-3540-b9ae-9a511e67be77 | -22.23192 | -43.04 | 2026-08-09 04:29:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| aab4a49d-1996-337f-bd3d-64bdd4104ff0 | -20.78835 | -57.7047 | 2026-08-09 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5c7d2fc0-5502-3892-b430-7e7c6da2622a | -21.43523 | -43.8849 | 2026-08-09 04:29:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7f3665c0-bb6e-38a1-b473-832e5defa62a | -21.76567 | -48.76537 | 2026-08-09 04:29:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a659d46e-95c2-3623-8006-863551233bed | -21.71377 | -46.23053 | 2026-08-09 04:29:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1965a021-331c-3284-95f9-93b06745c267 | -22.2964 | -42.61221 | 2026-08-09 04:29:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 12747ebe-6690-3a7e-80c6-a823eabec156 | -22.22881 | -43.03141 | 2026-08-09 04:29:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1be1577a-1d1b-3f1f-9da0-b2d0f1465b15 | -21.74511 | -43.56108 | 2026-08-09 04:29:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e7cbee85-5b16-3a2b-ab3f-3382f4680d1a | -21.66741 | -43.60766 | 2026-08-09 04:29:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 44cb9dab-cab4-380c-8137-69efab641981 | -22.18776 | -42.47892 | 2026-08-09 04:29:00 | NOAA-20 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ed7fe822-b532-3865-a973-0aa91b0f11d4 | -22.1872 | -42.48367 | 2026-08-09 04:29:00 | NOAA-20 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be5973f6-0f5b-3aa1-844e-b0174c3507e3 | -20.60769 | -45.11042 | 2026-08-09 04:29:00 | NOAA-20 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 12144997-286e-36bd-92fa-ddc10f72ac45 | -21.66002 | -43.63379 | 2026-08-09 04:29:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1f94417-c92e-3938-aa10-524b23d231dc | -20.97135 | -43.925 | 2026-08-09 04:29:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e9f8bf66-5188-3ec2-a263-632026b297b0 | -22.23149 | -43.04356 | 2026-08-09 04:29:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0df101a-f1bc-34e1-858c-9d5a1aec5fc2 | -21.36501 | -45.48791 | 2026-08-09 04:29:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 79cb8a69-999a-3bd3-8418-f730e664f3b8 | -21.66071 | -43.62851 | 2026-08-09 04:29:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c8c458b0-28d2-32bc-9f07-1dc5f6d329f5 | -21.08158 | -45.60687 | 2026-08-09 04:29:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d293dbc8-79fe-3b52-981e-073ae0d6db6b | -21.28143 | -42.94012 | 2026-08-09 04:29:00 | NOAA-20 | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de637aaa-215e-32be-9981-764c6372a330 | -21.34667 | -48.2389 | 2026-08-09 04:29:00 | NOAA-20 | GUARIBA | SÃO PAULO | Brasil | 3518602 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21c56bca-81cb-3fee-bdb1-861d30fae1ee | -21.43762 | -43.8814 | 2026-08-09 04:29:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74b54ddb-29a4-3c15-a291-8389343e59ab | -21.04567 | -45.68217 | 2026-08-09 04:29:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80929e5d-f708-3f44-af0b-ba954e6b809e | -22.88916 | -43.5018 | 2026-08-09 04:29:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8627084a-bd4e-35df-8c02-48a947634373 | -20.61127 | -45.11094 | 2026-08-09 04:29:00 | NOAA-20 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e34ba00a-7b92-3f04-a372-23998641c074 | -21.26776 | -49.58709 | 2026-08-09 04:29:00 | NOAA-20 | MENDONÇA | SÃO PAULO | Brasil | 3529500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 99d81956-af62-357f-88c6-dc32a5189aa8 | -21.67064 | -43.61354 | 2026-08-09 04:29:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cc2225c1-a4e9-3bde-bb51-bea38f51d1fc | -22.29694 | -42.60775 | 2026-08-09 04:29:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 005d0ccc-55c5-3285-a877-d3cd91ddefc0 | -20.7942 | -57.70265 | 2026-08-09 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 61e9c004-ebeb-3c94-ac25-b884d626217e | -22.22783 | -43.03941 | 2026-08-09 04:29:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7795e2cc-b6d9-3258-b0c1-055db5d4d79b | -20.78956 | -57.70254 | 2026-08-09 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8287121c-946f-33b9-827e-2e2793efd7e4 | -20.80026 | -57.72528 | 2026-08-09 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5b43fce5-ae04-395e-b951-e8552726d965 | -21.27377 | -42.93517 | 2026-08-09 04:29:00 | NOAA-20 | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7bf52a0d-1c4e-3c75-bb6c-e9ab38bf9f6e | -22.8899 | -43.50511 | 2026-08-09 04:29:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4e2a7df6-03a7-314b-ac22-8daffd1bbb0f | -22.30054 | -42.61335 | 2026-08-09 04:29:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e3170cc4-0008-300d-bf37-632b509c1ca2 | -21.9061 | -46.47054 | 2026-08-09 04:29:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2331a748-6594-3d0f-88e4-92ce5374ff42 | -21.90951 | -46.47123 | 2026-08-09 04:29:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f61ad01b-fdc6-3c52-bbcb-f3ffc56a700e | -9.4773 | -40.3116 | 2026-08-09 04:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.0 |
| a17e08b7-9b47-3062-a2e0-64b5ad0cff5c | -6.8388 | -56.4146 | 2026-08-09 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fd96f222-940a-3a1b-9aca-7641aaa1165b | -30.14653 | -51.17859 | 2026-08-09 04:32:00 | NOAA-20 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 78bc6944-b397-38fc-9b27-22fa9e9f3499 | -22.2978 | -42.6039 | 2026-08-09 04:40:00 | GOES-19 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| b7cc016f-89b1-37af-9278-9dba9af42eed | -6.8388 | -56.4146 | 2026-08-09 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2f28587e-39a3-35c9-a18f-da527fc2a7ce | -6.8388 | -56.4146 | 2026-08-09 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6c28ee2e-68c3-369c-9fa5-92d4f7f1e094 | -6.8388 | -56.4146 | 2026-08-09 05:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b2eb40a7-5f92-38ca-b44a-674949b781cb | -22.2978 | -42.6039 | 2026-08-09 05:00:00 | GOES-19 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| ac8f600f-f24f-36d1-9820-25d049137351 | 2.1543 | -50.70293 | 2026-08-09 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 699bae81-42b9-3878-bcb6-4868bce24929 | 2.15376 | -50.69952 | 2026-08-09 05:08:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8efb5dfe-11fc-3e83-af17-aa9f16af320f | -6.8388 | -56.4146 | 2026-08-09 05:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a89d5c43-baf0-32e0-b272-2dd64501f0ef | -13.935 | -58.1179 | 2026-08-09 05:10:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 16edd11b-2e16-33b4-bbe9-3efb1e85e914 | -2.37858 | -48.2305 | 2026-08-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71e452fe-8670-33bc-853e-3d7ea99fd3ac | -6.86841 | -44.43061 | 2026-08-09 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e37986b-ed08-3f29-b889-ad86fabfde0d | -7.58792 | -45.21415 | 2026-08-09 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 49b3aca2-0b4c-37aa-a3eb-c2b22c9d014c | -2.55989 | -48.42738 | 2026-08-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e399d4ca-4f03-3198-9c91-e233b9223110 | -6.86752 | -44.43761 | 2026-08-09 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0851603-3c25-31db-8f79-8584cc88a239 | -5.03048 | -56.12485 | 2026-08-09 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61d8ea67-938f-3f5f-a26b-dd9e9bcc8096 | -5.72927 | -49.13837 | 2026-08-09 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cefb2326-be1c-30c5-83f1-33a39450a98f | -7.58959 | -45.21301 | 2026-08-09 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3b9c0d1b-f1b0-35a5-9025-07d23b09b690 | -4.30003 | -55.72358 | 2026-08-09 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c87e5caf-311f-3a61-9941-b026ae3e0304 | -5.03103 | -56.12133 | 2026-08-09 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be131b61-6899-325e-9546-9f67438d98d4 | -1.46557 | -53.5975 | 2026-08-09 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f594d660-d141-3aed-8236-76da15f9b3a9 | -5.88499 | -57.64984 | 2026-08-09 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a99ba9b-69bc-393e-b4ef-b1afcffae232 | -2.65878 | -54.62284 | 2026-08-09 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README16.md)
