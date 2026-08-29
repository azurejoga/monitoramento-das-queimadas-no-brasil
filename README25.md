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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a258db0f-9676-3c99-8426-5a84af29b632 | -12.24664 | -50.53793 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfd920fb-65a2-3285-8671-acba7f79174c | -12.78837 | -46.45387 | 2026-08-29 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4f26711-f46e-3cdd-9e1d-4c2e9f2a0699 | -15.57293 | -42.71511 | 2026-08-29 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 437585fb-2e47-3ed0-912d-bb4a1ac7cb35 | -12.19458 | -50.55791 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d184c182-1e5f-3473-a6fa-9da275506d93 | -13.3269 | -48.1894 | 2026-08-29 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8dacf8ed-1038-344f-a73b-a0bd5ec73c50 | -15.12206 | -53.57561 | 2026-08-29 03:57:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 432dcb0e-3540-34a5-a38c-0670d428be30 | -17.05544 | -39.86533 | 2026-08-29 03:57:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e77e9e4d-3d98-3ece-8eee-3e8c5b3e52d3 | -14.76306 | -48.74723 | 2026-08-29 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46fcfee1-e930-327c-a53c-9ad598944302 | -13.65419 | -47.75568 | 2026-08-29 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6dfacbc-2b85-37db-b1bd-1607eba3995f | -17.57718 | -51.63984 | 2026-08-29 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfae57f4-dbb7-30f9-862c-e29dad6ad86d | -15.64676 | -45.91927 | 2026-08-29 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38c08cd1-8d20-32c3-b03a-e0da3815f12e | -17.82162 | -39.69023 | 2026-08-29 03:57:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c737ca05-6531-36ba-8bca-b383696461d4 | -12.42364 | -43.41259 | 2026-08-29 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96b604a3-19f3-30f1-815c-6ce31c8b1ec5 | -18.8525 | -47.40861 | 2026-08-29 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82a344d5-33e9-3a87-8cce-99f58c368101 | -17.28466 | -46.02355 | 2026-08-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 449fdb4a-82b1-3db2-afb5-46b0b5a0571c | -14.90676 | -52.63051 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3724d4d6-c4fa-3bf8-89e5-6240e36bd3ef | -15.15119 | -43.79231 | 2026-08-29 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0db4cba2-2a6b-36c2-83e7-7de37abf8447 | -14.76361 | -48.75028 | 2026-08-29 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e286f71d-cf41-3076-b28e-7147f755b9f9 | -19.91981 | -42.29998 | 2026-08-29 03:57:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 379fa397-7aa1-32ec-b316-c2a9ea016ea9 | -13.6549 | -47.73264 | 2026-08-29 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fdbc231-b870-3b3a-b691-ce83997099cd | -12.19623 | -50.54951 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 090e2495-bc8a-30df-b253-40e777f307f3 | -16.17951 | -45.63491 | 2026-08-29 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 789d1f8c-c914-37c4-985b-6b4a223f19ea | -15.64871 | -45.93148 | 2026-08-29 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d5357c80-7487-353c-b3f3-5cdc7eadca88 | -16.47654 | -49.23521 | 2026-08-29 03:57:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffe6b492-6b22-3387-84f6-6bab0605617a | -14.9244 | -41.26157 | 2026-08-29 03:57:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 16e089d6-e04e-359b-a99d-5d8e664f4554 | -15.12077 | -53.58155 | 2026-08-29 03:57:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| a44e86ef-383c-34bc-8830-d161d3bb512e | -17.82555 | -39.68703 | 2026-08-29 03:57:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c374c7a2-65dc-3493-bc42-eed32c8027c6 | -17.82499 | -39.69078 | 2026-08-29 03:57:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 51954999-fa36-3322-b579-882bd0b8085b | -17.29161 | -46.03042 | 2026-08-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46ca998d-dbe2-33c7-a718-3385ef5396f6 | -14.18725 | -48.75601 | 2026-08-29 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9317b17b-f5ce-3773-a6b3-e0076c12cd38 | -15.17516 | -41.86065 | 2026-08-29 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7fe9f752-f775-3feb-bef7-1c236b919d76 | -15.10735 | -48.15766 | 2026-08-29 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c30a7c68-cc8e-32c7-b822-e5bd9b7d97a6 | -16.48923 | -39.35445 | 2026-08-29 03:57:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8b97d2ad-1edd-340f-8fcf-af146c57715d | -12.1954 | -50.55372 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d1f9e08-44a9-33a0-9a3a-c45bc99836ad | -14.40757 | -52.57326 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 501ff2e6-eba5-356c-b2ca-60f1d1d6b53a | -18.46641 | -42.28026 | 2026-08-29 03:57:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b2f077dc-f505-30d6-8f66-d342121f87f9 | -15.65944 | -48.37256 | 2026-08-29 03:57:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 97d8a89d-e5c7-317d-8fc6-588960919943 | -12.77356 | -46.46051 | 2026-08-29 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af590e99-a672-3237-8c5f-14c127292e10 | -15.82165 | -43.93555 | 2026-08-29 03:57:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f0cd0b87-61ce-3bc6-a412-a4ab3268b52c | -14.90322 | -47.74479 | 2026-08-29 03:57:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2438070f-52d4-3323-946b-70a18ed2d449 | -15.64134 | -45.92603 | 2026-08-29 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f56a8dc4-4558-38b5-b3ba-e4c96974648a | -13.35281 | -43.64842 | 2026-08-29 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63c008ac-ec73-3e94-afed-2a2d13dc611a | -17.28373 | -46.02872 | 2026-08-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2366f25-42c5-3ba7-953e-0df568fad218 | -11.2031 | -51.27005 | 2026-08-29 03:57:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98db7e73-ea41-37c5-898c-8a8ed82cf11d | -14.17553 | -48.76313 | 2026-08-29 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24194ab1-fd97-3cf6-82ef-5c3f52f4d978 | -15.6454 | -45.92672 | 2026-08-29 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 81c32c69-9a72-3fa7-9de2-df914a3fe4fb | -17.79185 | -39.70462 | 2026-08-29 03:57:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fb4d2762-80d7-35c0-b538-9ab14b74011f | -17.79523 | -39.70517 | 2026-08-29 03:57:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 777121d9-d68a-30c7-b67e-32beac59f59b | -13.93952 | -43.99644 | 2026-08-29 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1a4dee7-0c8e-3cd6-b1de-8c3ac9b011dd | -14.41165 | -52.57183 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7d5ebac-56ad-3af9-94a5-778457108b17 | -19.00314 | -47.4425 | 2026-08-29 03:57:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f2d99155-d280-3253-945b-001be8ee6971 | -11.18075 | -51.28594 | 2026-08-29 03:57:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cf08a90-a75c-3d7a-849a-64478147e00a | -14.20596 | -52.84583 | 2026-08-29 03:57:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38c70eff-f299-3444-90b1-a507c1e9890e | -18.02818 | -49.2025 | 2026-08-29 03:57:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eb6c97b-145b-36f7-aca7-ae5928606327 | -14.43134 | -52.58511 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 13c5e832-4bcf-3324-81f7-c221ce505f1c | -16.61406 | -49.40572 | 2026-08-29 03:57:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3097cfeb-3ef8-35b8-be35-1cff69e94804 | -12.43172 | -43.40945 | 2026-08-29 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c8686c02-c7d7-35d6-a21b-6d6a38135de9 | -14.90414 | -52.61208 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96bfc9a4-5251-3ac4-92ca-f6a2b1130d20 | -17.27772 | -46.01669 | 2026-08-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4abacd7-99df-332a-b63c-a3b67205dabf | -14.11995 | -44.21432 | 2026-08-29 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 164c921b-d0dc-3af9-81c4-c0ca833daadf | -14.18167 | -48.75809 | 2026-08-29 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75288944-8cac-3383-9e91-fe27372d8c1f | -16.61343 | -49.40884 | 2026-08-29 03:57:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0930763b-0588-3e9f-b5b7-fea260d17dde | -17.05789 | -39.86523 | 2026-08-29 03:57:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a57a95a2-3c72-388c-9514-66bcac593c8d | -14.20718 | -52.84006 | 2026-08-29 03:57:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d712a5e-da29-37be-a07d-cc1d2622f43d | -12.42731 | -43.41323 | 2026-08-29 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 74439a7a-9681-3602-87a4-c196054d5373 | -14.90414 | -47.73994 | 2026-08-29 03:57:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 458c9960-4dd1-3365-90e2-41ed9104196f | -13.65958 | -47.73368 | 2026-08-29 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7750299e-4272-3a59-8d49-4575c0ef6684 | -15.80146 | -43.23907 | 2026-08-29 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7c6faac-7009-3424-a45c-3c86a37b5def | -17.85871 | -42.77201 | 2026-08-29 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fe7c22ca-ac6f-360e-a727-6a0f2e2c2e13 | -11.68938 | -47.62273 | 2026-08-29 03:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f69f8b0a-d98d-329e-bd1f-9d5f046cdec0 | -14.41687 | -52.57831 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfa235d7-c41e-3d98-bd58-71ac47c3930a | -17.59509 | -51.61098 | 2026-08-29 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c5e5022d-e00d-3d7b-9e60-3c896c2759d6 | -11.68834 | -47.62842 | 2026-08-29 03:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4f1ce82-91bd-3611-a37c-ba41c0463fe6 | -13.31523 | -48.19769 | 2026-08-29 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 218ff41a-f269-3184-80bd-892ce6effe1a | -12.22183 | -50.5407 | 2026-08-29 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4c761be-343e-3592-8bfb-d4f4a27e04bd | -14.11915 | -44.2189 | 2026-08-29 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28c64371-76ff-398d-9465-da3be6c735b8 | -19.00391 | -47.43842 | 2026-08-29 03:57:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fd280b77-1cdd-3240-8dfa-7ace097828b7 | -14.19611 | -52.86057 | 2026-08-29 03:57:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d67fe8eb-5bf4-3b7f-891d-4d73f1bcedd8 | -19.00237 | -47.44658 | 2026-08-29 03:57:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64154ca4-8002-3fc1-ae41-f7b15ab10dec | -18.78513 | -45.59313 | 2026-08-29 03:57:00 | NOAA-21 | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4215e20e-8cf9-3af1-9a0e-48fd04b556f6 | -11.20407 | -51.26516 | 2026-08-29 03:57:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60b7630e-2eee-3f3f-8297-96ac7c4d268b | -19.31483 | -45.24089 | 2026-08-29 03:57:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4758f995-36fb-316f-a63a-aa51757f0453 | -14.90166 | -52.62372 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0537fc26-e34f-314a-96f8-5cc514af7ac7 | -13.59682 | -45.77813 | 2026-08-29 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a4e3a2b-a782-3038-b9d4-e589dff2fd0f | -17.28073 | -46.02263 | 2026-08-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01e17339-562d-34ab-bb2e-199cb6fbf9a8 | -14.75752 | -48.75517 | 2026-08-29 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c0d9055-51c9-3436-a321-67d110cc32bc | -16.48023 | -49.42615 | 2026-08-29 03:57:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac544854-00df-303a-b871-2f61a64dcf62 | -14.43443 | -52.5887 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15f23425-06f7-3bb3-86a2-ea7b4c63ed7f | -14.42921 | -52.58218 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bf29cac-f2f8-31cc-82fe-cd7101743f12 | -12.78318 | -46.45752 | 2026-08-29 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b48a9b7e-0bea-3ca9-acac-fab28584a430 | -15.6447 | -45.93055 | 2026-08-29 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ea4c44a8-4c72-397b-a1dc-30852a685b59 | -15.15045 | -43.79662 | 2026-08-29 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27342278-1426-36df-8270-bb7294925828 | -12.7675 | -44.26897 | 2026-08-29 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4cc86c0-8d4a-3612-8b01-c73e36227fe6 | -14.18669 | -48.75892 | 2026-08-29 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 812c8209-f02e-36cc-813b-6d69b74d4758 | -13.66425 | -47.73479 | 2026-08-29 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa36f633-35d8-34ba-a17e-b3ae4de5d310 | -12.38068 | -48.18932 | 2026-08-29 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a8a2ceb-295b-36dc-bfcf-ae17449edae1 | -11.83878 | -46.77176 | 2026-08-29 03:57:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9a34ab1-9dcc-3be8-a92e-4c38a3c81bee | -14.18047 | -52.83955 | 2026-08-29 03:57:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f65f62db-26d8-3dc4-8438-76ebfc819fea | -14.41278 | -52.57961 | 2026-08-29 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6e2c0af-d5f1-381a-90df-5f1f871a1922 | -12.06244 | -47.15062 | 2026-08-29 03:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
