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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07752a42-2ff8-3965-900d-72a9bd236536 | -13.64862 | -47.30122 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9444d82-cb13-3711-9290-51dc7cae2c17 | -14.68817 | -45.18084 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46e632fd-daca-3822-a52b-ef54d3c15baf | -13.16779 | -47.86895 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 155d6caa-9558-3a3f-981c-7a9f159acaf1 | -13.75471 | -48.71271 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32bce4af-e5ed-3897-83fb-8f2c3d5dc14e | -15.5016 | -44.18913 | 2025-10-03 04:34:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46f6a6b7-8254-3234-a09d-13c9016a6798 | -13.96624 | -48.16854 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8c188762-60e1-393d-b1ca-d2ab13aac108 | -16.58212 | -44.0119 | 2025-10-03 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a31c0249-9a5f-326b-84d9-b67f33db129e | -12.20281 | -47.81612 | 2025-10-03 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04452579-4f7c-3bf0-99a0-95eef3a8a600 | -13.58379 | -47.59144 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5569664f-1500-35fe-800d-482fad7f28cd | -14.76849 | -49.28639 | 2025-10-03 04:34:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7089b9c6-a0dc-33bd-9cf1-373ccbb3d6ca | -12.94135 | -48.44339 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea4763ca-7c34-3ffb-8a52-c8ac065b46a6 | -14.93046 | -46.89129 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f2e7c1ec-ec8b-3d67-a11e-acf95ad4595e | -18.24492 | -53.32309 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c61bd746-299b-3aa8-b6f7-0e26c068649e | -12.61176 | -46.963 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9d974698-7c63-3654-be02-74293f743617 | -13.04764 | -47.01922 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b1ed671-78ef-3493-9cb8-aa8cbcc6b145 | -15.49034 | -45.92975 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d93c66ec-f35b-3fc2-b71e-6aa437ceda5b | -13.7531 | -47.97411 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 273f5745-8beb-31ad-b326-6d05bd00b04c | -12.91728 | -46.37023 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82981ec4-19b0-30cc-9112-850c961cbf12 | -12.9358 | -48.43521 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4f1229a-2cb4-3c31-a1a8-cd0276269324 | -14.95003 | -47.52624 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e440572-8e46-3e31-b28f-06b7af7d76a2 | -15.25123 | -47.92535 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b8dff48d-7ab3-3210-95c1-082145264fd3 | -14.91091 | -48.34394 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca49803e-af76-3c1c-a378-149a18a80e84 | -14.68359 | -45.18543 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64bca119-6ef2-3113-9b7e-545778306748 | -13.26331 | -47.25529 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 820fb54b-1292-3d2d-8f48-5056adc8df89 | -12.71306 | -48.57877 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0639d4e3-4dc8-3eaa-a1be-40027e7c4e5c | -17.84559 | -44.31447 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e619ea6e-8c1d-33e9-a6c5-0238de07430d | -13.3309 | -47.2035 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19e09b0c-e43f-329f-a410-a2a4ac35ce68 | -14.41975 | -47.14741 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6441a18f-2745-3008-b542-beb271500119 | -14.6294 | -48.13205 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38fdc414-23ea-3576-9ed2-17bd1988ae91 | -15.23314 | -48.06938 | 2025-10-03 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d42a3af6-1607-3869-a7a5-27b75bea72eb | -13.21494 | -47.83126 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6a019c0-e21e-3280-bea4-7eca9d97f695 | -14.80609 | -51.42135 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe32916e-6905-389d-b48e-8e9dce7b9203 | -17.91244 | -43.93761 | 2025-10-03 04:34:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97b5059b-6d3f-3782-9bf5-2e0ea9c42d02 | -15.23708 | -50.10539 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca82f439-cf82-3a97-a389-d8be39a8165d | -14.13793 | -47.05681 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98db4620-55ae-3f69-8ece-953dcad735ea | -15.59629 | -46.92727 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fb2e056-dfe3-3ec7-a621-981939fda75c | -18.45941 | -49.44076 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2fc079c-1e83-359c-9305-100f16702764 | -13.78656 | -51.3037 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc7f5914-13ce-34cc-962a-5c5369b2239c | -20.12783 | -44.01277 | 2025-10-03 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1f1fb6b9-4624-3e17-a024-b988fbe38771 | -12.84088 | -46.85785 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dbe64cd-3e7f-3e84-b432-4a017aeac3b0 | -12.20226 | -47.81974 | 2025-10-03 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96449186-4e28-3ece-b8a1-4a6e63e59056 | -14.74938 | -48.12505 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1b70bcd-5feb-362e-829c-5bcc2953a100 | -14.57652 | -52.46549 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a9211188-c73c-3a2a-b95a-838fd1c6b716 | -12.6228 | -46.97535 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| de14662e-c491-39c7-88f4-2c741568a4f7 | -15.34168 | -47.83363 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 547a92d5-739f-30ac-b19b-cb0810837500 | -13.78425 | -50.78698 | 2025-10-03 04:34:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb6c2496-f918-3434-be51-b1a200af4c65 | -13.30855 | -47.81609 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 759ebbda-1be3-3fe5-b27f-03c1636199b4 | -15.59571 | -46.93129 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f345303b-1ebb-3c2a-831e-932eef88172c | -15.24432 | -47.16522 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9f3a6e1-41f6-34fe-8bb4-03db149b6b7b | -14.41514 | -46.16171 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44a095fb-383a-3b6e-812a-db3838097589 | -14.37656 | -45.93686 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83bcfe17-49cb-3aea-a1a0-836858dd2b15 | -15.34823 | -47.07171 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fda6fba-c624-3449-bd6b-da688682438d | -14.15724 | -49.20112 | 2025-10-03 04:34:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 272b4653-bec5-3278-9bfc-08fd6c9974d0 | -13.33433 | -47.20413 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09d1d2f7-10a0-3f39-96fe-7e00112cc876 | -16.01205 | -48.33619 | 2025-10-03 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0aae8630-b055-3be9-94a2-8904bc5f8b78 | -13.68151 | -48.63492 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8778e8e4-9e54-3721-9739-2755588f8452 | -14.90165 | -46.96624 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 360b0e57-7972-39b8-99d4-78dcea78e0f0 | -13.13263 | -47.88618 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fa4a929-6faa-35e8-ab42-84e7caef3200 | -15.98743 | -50.87136 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76c2766e-9cb3-3bb9-a472-c2a16d791fc7 | -13.36278 | -48.08188 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff43990b-585e-39c4-977b-238ef70a6300 | -14.40937 | -47.87054 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3688ea51-7afa-3287-88f7-5a92aa7d8f9f | -18.2322 | -53.35629 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f2bd5bd-0270-39a4-9d24-894a8bfaab98 | -13.16391 | -47.89458 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 535b3c65-11bf-3262-9099-15bd167587a2 | -13.35241 | -47.33836 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73baf6aa-0188-348c-a93f-efec5714df9a | -12.76404 | -44.90248 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e07a6d8d-fd2a-349a-bc83-daf50e7e613b | -16.04432 | -50.89594 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22c7f691-2ae7-3932-a747-5df5eb7732d0 | -14.57079 | -48.32718 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 076e177b-1d14-32cd-8b7b-bd1018807abe | -14.94773 | -47.51781 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2c41441-1763-3720-b1fa-5a13d98583a3 | -18.23202 | -53.35516 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5536508-60e9-3f8a-b168-211d34994c60 | -15.65686 | -44.49697 | 2025-10-03 04:34:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 989fe53a-eb54-386c-8abd-f0163836dff9 | -15.25354 | -50.13025 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab97f123-c0c7-3fab-9263-2cff4b8a06cf | -13.75085 | -48.71571 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d55b34f-ad86-302a-9f85-2a0a60bb15ff | -13.80001 | -47.57304 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 755bb4c8-b403-3613-9142-e973b7481aef | -13.22831 | -46.43902 | 2025-10-03 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6e1c95e-0f40-37b1-8dc8-4aa3ed63b65a | -13.52703 | -47.29455 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6ddfa8d-a637-37f5-bc5e-cfeb507c1ace | -15.30177 | -46.29845 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ee02f5e-1588-316f-b565-4c0fb2163416 | -12.89644 | -46.90169 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16d8d056-33b9-38a1-9c67-a07e77488584 | -13.27143 | -47.27154 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 872d4ee1-d5ed-3fc6-8e8b-af88e9412896 | -13.35642 | -47.33506 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| adf2c206-0272-32ba-a41e-fddfee0e7dd7 | -13.33492 | -47.59559 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d039573-57f7-3c1d-919e-b02240d250c2 | -13.20769 | -47.87886 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7de5d24-a391-3770-b6f8-f77450053479 | -16.06831 | -51.00149 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ecf22031-6ba6-335b-b6a5-59ff2985d961 | -12.89184 | -46.88479 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85126a4e-8fae-35f5-b4cb-3f24bd5f37d7 | -13.69147 | -48.6146 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 422e970c-a182-3dff-bb40-d42a34bf253b | -15.3549 | -46.2899 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9452c40c-e669-36b6-9216-c4b34c7ad15a | -12.62038 | -46.9995 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45586d72-bae0-32e9-8ef1-419ccd856384 | -12.679 | -48.58031 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd53ef0b-c4d1-36f8-806c-3900d77de0de | -14.01393 | -44.97385 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 179add86-bf61-381f-be37-dd6364d3a33d | -16.04706 | -50.90015 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62f7f276-ae3e-3c87-aea0-24b5e37f552c | -14.9375 | -46.89268 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e8af689-c280-32a2-967f-f722f9e204f5 | -12.60716 | -46.99352 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00d52384-6f27-3c12-99b4-ae6dd807fa68 | -11.31816 | -53.9612 | 2025-10-03 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f085ae14-f5d5-3c0b-a4d5-ac596723a62c | -17.31659 | -49.37613 | 2025-10-03 04:34:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6a49a39-9d2a-318e-aecb-b7541e10c434 | -14.93221 | -46.90434 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4d1f87c5-20b8-3518-b3c2-d7ed22d5cde7 | -12.62291 | -46.99847 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4dfcc0e-c4ad-30f0-9114-b171737b05bd | -18.23292 | -53.3521 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a002819a-d947-39b0-ba38-718328454434 | -20.11284 | -44.39401 | 2025-10-03 04:34:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 94c50d54-733d-347c-985e-a8abccde8723 | -13.24629 | -47.29882 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abf5bac7-4854-355f-adef-c91f5ae579f5 | -19.59769 | -45.90097 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08f48b68-1652-3073-81d3-b83dcdf5422e | -13.73796 | -48.00551 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README115.md)
