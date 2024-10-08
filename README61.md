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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eb34e6c-8e8a-3039-b9be-bf048ae5325e | -19.82988 | -42.38125 | 2024-10-08 04:36:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3b6d466c-7c7e-38da-9a70-737c79e3f97b | -19.82232 | -42.35755 | 2024-10-08 04:36:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c33b2c5f-84ca-3176-96ed-e7512416e37a | -19.82199 | -42.3605 | 2024-10-08 04:36:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9f8b7df1-5ac9-3e41-8e88-f3ac6f2efbec | -19.77461 | -42.00415 | 2024-10-08 04:36:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ae9cd881-7771-3efa-84bd-addfb1862257 | -14.15501 | -45.5559 | 2024-10-08 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b18dc722-18a0-3479-8250-616460ed9ef5 | -14.78756 | -42.84182 | 2024-10-08 04:36:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f01ff8ff-4848-3a96-a66f-34af2cf8da23 | -14.77114 | -43.50046 | 2024-10-08 04:36:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1674ff5a-3ad0-3103-97a4-0c7688dcf457 | -14.53425 | -43.2197 | 2024-10-08 04:36:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 48b32168-890b-3ff4-9ad3-d2a354e59112 | -16.35132 | -43.69557 | 2024-10-08 04:36:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d874ffc4-d63c-3bab-ba40-658e394756c2 | -15.60555 | -42.5652 | 2024-10-08 04:36:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 10832e4e-2362-3427-b3b7-c02882778ec6 | -15.60492 | -42.5704 | 2024-10-08 04:36:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 57de53dc-8723-359d-be69-a7ba97ddc8bc | -17.58693 | -43.7338 | 2024-10-08 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ee7f2bf-939f-39f0-aa8b-88b8f4c6b69a | -17.58041 | -43.71283 | 2024-10-08 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4cd1b94-e29c-353b-9e94-9faa8a51c04a | -17.57706 | -43.70305 | 2024-10-08 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edaa7101-5e8d-38c9-9b23-c3cc9c43c00b | -16.68251 | -43.88424 | 2024-10-08 04:36:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb7d16e2-6d7a-33cb-aa3c-f2a75d814695 | -16.68074 | -43.88648 | 2024-10-08 04:36:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dabe1883-b5ed-3ef0-ba34-d57e3de2c8c7 | -18.32798 | -43.82071 | 2024-10-08 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bcff813c-0404-33cf-8cc2-b3e9b8d1706b | -18.32351 | -43.82019 | 2024-10-08 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5294e97e-4cca-364f-876c-e27cdc019464 | -20.40687 | -43.93825 | 2024-10-08 04:36:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| 9c107f58-6969-3e0a-912e-a74eb45ab9ae | -20.40636 | -43.94258 | 2024-10-08 04:36:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| 82cf9087-a33c-39fb-ad12-c94112073084 | -20.40585 | -43.94696 | 2024-10-08 04:36:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 2bf03d8e-1ad6-3357-beca-0678321d79fd | -20.40276 | -43.93394 | 2024-10-08 04:36:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 1b1b73cd-cb82-3879-b73c-7e4b43271632 | -20.40231 | -43.93773 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| b7eb6d9b-082e-3a8f-83c7-ceb6c5d8c6ea | -20.40181 | -43.94198 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| 9c700771-4d36-32f3-aef4-60288aa89c6c | -20.40131 | -43.94629 | 2024-10-08 04:36:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 0ac82781-9d74-3f46-b4af-f71f3102505c | -20.39776 | -43.93714 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8ed51749-49b9-3ed7-83a8-ebaa3c72112a | -20.39728 | -43.94125 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1ddefba4-ad4b-361e-9530-01f288a39907 | -20.39678 | -43.9455 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| a3c1f0cc-b52c-3ad8-8739-b74320578ecd | -20.39624 | -43.95013 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 31995c90-9599-3650-9b65-48251d22cdc8 | -20.3927 | -43.94091 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 183a8314-ce4e-3d45-bf5e-9832e73ac9ea | -20.39221 | -43.94513 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 25e88019-3e73-33a6-aa01-0ef6f3988bbb | -20.39169 | -43.94961 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| b3720b86-344a-37f7-b6ca-6bf63e04df9b | -20.3881 | -43.94075 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e7bbc819-c7b3-3973-b3f6-105260e20a0f | -20.38762 | -43.94488 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2b360122-8ebc-304c-8344-2f5759f7182a | -20.38712 | -43.94917 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| edb791d1-d3aa-37d7-afcb-40ba3c98bd51 | -20.38661 | -43.95358 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7264302f-6131-3966-8bfc-a88cc33a8e9d | -20.38256 | -43.94867 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 44ab0d86-0693-31a5-ae75-72654e5081fb | -20.38204 | -43.95317 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| efd6ad3d-379b-318c-baca-982d1cec5405 | -20.38151 | -43.9577 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 497b15ea-bbe3-3796-adfc-b056b52409b5 | -20.38099 | -43.96225 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e3bab3a4-cbb8-32b9-bee5-4346a9f3a872 | -20.37801 | -43.94814 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b5565ea3-9f41-3d74-b872-c5a0f453b2f3 | -20.37749 | -43.95264 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4d247b5e-69f0-3949-9164-e1a109bdc07a | -20.37697 | -43.95706 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c7fcc924-8789-3da3-93a3-6655b6c59136 | -20.37647 | -43.96144 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| aacb87fc-1cbe-314b-a57c-b440c83087ff | -20.37392 | -43.94353 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d19d5a5c-8b7a-3714-ba87-bad0c709160f | -20.37295 | -43.95195 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a207c2ee-c030-3f0a-aa7e-ad88c52b92d7 | -20.37244 | -43.95631 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 37ed109a-763a-3bd3-bee9-e82755f7400a | -20.37194 | -43.96067 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 24154426-59ec-3fac-826b-655bfe0038a4 | -20.36839 | -43.95146 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 188d00f2-2996-3aff-a404-293a39762d55 | -20.36476 | -43.94296 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 348f2ffb-17b4-322e-b358-18914964da61 | -20.36431 | -43.94681 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 61545338-9308-34b4-bae0-5d94f50be5af | -20.36382 | -43.95113 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8b0fd4a5-5476-3677-b03f-1f495a442d0f | -20.36331 | -43.95549 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 770b5724-cfef-3a3d-8f3a-095e2839d71d | -20.36116 | -43.93413 | 2024-10-08 04:36:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 651ab620-9657-382d-ab95-490a2b15c214 | -20.36061 | -43.93889 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| aaeacf63-b3a7-3371-8a9c-8f768f5d1207 | -20.36018 | -43.94269 | 2024-10-08 04:36:00 | NOAA-21 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 6496e898-33ad-35ff-9233-a7cb1f8054e8 | -20.35665 | -43.93317 | 2024-10-08 04:36:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 364f629a-8289-332e-ac14-2b220efbe13e | -20.23544 | -44.44205 | 2024-10-08 04:36:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2b27ab61-b1a2-381b-bff3-35ca90685fa3 | -20.23109 | -44.44111 | 2024-10-08 04:36:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 894dafeb-4bef-38f3-8db1-6518d7fe9034 | -20.2305 | -44.44604 | 2024-10-08 04:36:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 739e9192-3a79-3024-b7ea-c675b8386120 | -19.98876 | -44.2576 | 2024-10-08 04:36:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 825c9cba-266c-3f51-a45c-16cb38c70ff2 | -19.8216 | -43.84698 | 2024-10-08 04:36:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6cc083e-b0fd-3e81-9f1a-dde956f15a8e | -19.82107 | -43.8516 | 2024-10-08 04:36:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 767dd9bf-debe-314a-b00c-5f3558a02664 | -20.38642 | -43.87498 | 2024-10-08 04:36:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 04217bd0-9210-3628-b406-7ff9c0c0bb10 | -20.13162 | -43.86485 | 2024-10-08 04:36:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f66cb43c-197d-3575-be52-87d4ab75a0fd | -20.12709 | -43.86394 | 2024-10-08 04:36:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a28d149-305c-3838-a55d-977ef081db7d | -14.48616 | -44.96068 | 2024-10-08 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2a9f09c-b872-3a21-b2e4-65c683ba65d1 | -14.48589 | -44.96275 | 2024-10-08 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93dfe6ef-2092-37cc-8bc8-95f7ea3879e8 | -14.14453 | -44.40166 | 2024-10-08 04:36:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 848f74aa-7dad-3673-9840-2f1aa5a31fed | -15.40101 | -44.21569 | 2024-10-08 04:36:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8e164a81-7a72-3922-ba39-c13868e12c5b | -15.7546 | -45.34577 | 2024-10-08 04:36:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| af8e65d7-d4ed-3d42-a644-3acca5c54f58 | -17.67643 | -45.29913 | 2024-10-08 04:36:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 272843fb-4b6a-3167-888b-664f66e96ea5 | -17.59044 | -44.51222 | 2024-10-08 04:36:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 671a8141-9a5a-3149-9c6b-14f9aa547966 | -17.58625 | -44.51144 | 2024-10-08 04:36:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e965220e-b26e-3ec8-a241-2d72614b21b9 | -18.21895 | -45.05279 | 2024-10-08 04:36:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a5dd4f7-3a29-3c2c-a71c-0497e2eff3d8 | -19.86999 | -45.68713 | 2024-10-08 04:36:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e882f84b-e257-33a1-b46c-931c912153ee | -19.86951 | -45.69086 | 2024-10-08 04:36:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0bfbc0db-0a81-3c9c-96cc-1c0ad32864d3 | -19.86595 | -45.68657 | 2024-10-08 04:36:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74712e73-7ce5-3271-991e-6cbff68573e8 | -19.8624 | -45.68221 | 2024-10-08 04:36:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68242d38-fdc1-332f-afd3-8dd046e0c984 | -19.86192 | -45.68601 | 2024-10-08 04:36:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 770d4be8-87b4-34c4-b59e-884e19efefb3 | -19.79258 | -46.50676 | 2024-10-08 04:36:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4a9b530-9c44-3054-bdf6-d44da3399244 | -19.79057 | -46.50503 | 2024-10-08 04:36:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb0407d5-55fa-3dfb-a70f-60692a7777a5 | -19.66357 | -46.23135 | 2024-10-08 04:36:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b92e0699-e1db-3b17-8895-75f31c3f04f8 | -19.95585 | -45.10976 | 2024-10-08 04:36:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bedde87a-7c4e-3200-82c3-b207d70ef124 | -19.87143 | -45.03172 | 2024-10-08 04:36:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22cabcbe-d1d7-326d-a10e-2d5bd8f20175 | -19.87104 | -45.02964 | 2024-10-08 04:36:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 549de0be-37a3-3598-a307-cd2286bd3153 | -19.86773 | -45.02685 | 2024-10-08 04:36:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e56c590-1abb-301e-a542-19e863bd7309 | -19.86724 | -45.03096 | 2024-10-08 04:36:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b08318a-2370-3f54-9718-d3cdf476b773 | -19.86686 | -45.02885 | 2024-10-08 04:36:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b51236c-a087-3c07-9e70-0af554a29cf7 | -14.12889 | -45.60511 | 2024-10-08 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19c813ca-358b-3220-ae21-08205ec8b009 | -14.21696 | -46.46206 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90cdec4c-b4a7-315c-966b-c0ab6a67dabd | -14.16255 | -45.55704 | 2024-10-08 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1ee0f591-1a61-3044-bb22-8866367dd4ed | -14.15878 | -45.55647 | 2024-10-08 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 79a846fd-87a1-34c3-a95b-8ed1e90ecf06 | -14.12514 | -45.60448 | 2024-10-08 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2e6f9c97-d576-33d6-ae1c-3587f53b278d | -14.22595 | -46.45068 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0c68a72-d53c-3b1f-992d-5866660896b1 | -14.22233 | -46.45024 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8db4be2-aa99-3886-b11a-e4ad4460f4c6 | -14.22174 | -46.45443 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25ff3870-38d7-3570-bf13-4b69bb2ac225 | -14.21874 | -46.44967 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af3058b4-a6d8-3a3a-8c84-8f417fdc4717 | -14.21755 | -46.45797 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5506862-cb67-387c-8f36-346a55449345 | -14.21515 | -46.44901 | 2024-10-08 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README62.md)
