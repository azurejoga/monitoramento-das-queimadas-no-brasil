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
| 135b4292-b5e2-3379-8379-195e3a7498f1 | -11.90583 | -57.40557 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c8ef4cd3-7432-3ae4-8184-918dd471d7e6 | -10.84937 | -54.02913 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5278d3a4-944c-3626-b5a9-afeb126e897b | -10.47969 | -47.08097 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 54684a99-6bb3-38c6-8c7d-fc5e8ea3c37e | -10.56829 | -46.23226 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e442389a-03ca-3cca-a8ab-b2dd1664607f | -10.788 | -56.75965 | 2026-06-27 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17bc5b6f-d9a4-3cd1-a6a6-9e5a536fd46d | -9.47271 | -48.06818 | 2026-06-27 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f409068-e0be-369d-97a1-b01a2bcde24e | -9.07822 | -44.76346 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7afc6f39-335e-3e20-ab85-6dc248572b6c | -13.86987 | -50.40258 | 2026-06-27 04:32:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| feb7d53f-7c65-3939-8265-3acdd1dfb498 | -12.46498 | -58.48589 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0cdd9a3-f833-35d4-b1ec-53122a1fd6b4 | -15.58958 | -46.80835 | 2026-06-27 04:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 819efb4d-73a7-3674-add4-a9f35f7b958e | -10.48246 | -47.12795 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 038e82e8-7c6d-32e3-986a-caa7d845048a | -13.44923 | -47.87258 | 2026-06-27 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dac3c79a-d2ae-3bb7-b127-2aa4bdc7ae09 | -10.56773 | -46.23583 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f89e8efd-e620-377e-93ed-6c8d74d790dc | -10.49513 | -47.13358 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 444174c2-7570-3fca-b298-ce7b6f69d93c | -9.47214 | -48.07173 | 2026-06-27 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6180990a-1e79-326a-8006-cd5e8293a19e | -12.17061 | -59.75901 | 2026-06-27 04:32:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05aaa171-b51b-39e9-8ee7-f2c5292dfaa1 | -10.48135 | -47.11347 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a45264c-4e6d-3509-adbe-c19cf3054e60 | -9.06013 | -44.74938 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d47f46ba-b7ca-361b-844f-2282dd970e6b | -10.78395 | -56.75185 | 2026-06-27 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c3cb2bf5-75cd-3f36-9616-e85464f2eb3a | -12.45211 | -58.48779 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 61d8a5d3-27b6-3847-ad5d-c2aa30419fa5 | -12.61345 | -57.89029 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 45a850cd-334a-3168-b4a9-2a4a9beef7c0 | -10.68058 | -50.20934 | 2026-06-27 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00055f52-f557-3505-8a29-aef805d0efad | -10.93345 | -56.85575 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49517a3f-b3ee-3f68-a870-5154cb3b3647 | -13.24698 | -54.41434 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c6c1d67-5c1e-3ffc-8c20-c4189093a73e | -10.93876 | -56.85708 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80a77e5c-e921-3a32-8c14-5a091b2c69da | -12.45122 | -49.58224 | 2026-06-27 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3354c074-a00f-3a2f-91e6-ee4608423ae7 | -16.45137 | -45.01601 | 2026-06-27 04:32:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56551a2d-fa74-3869-84e7-0e46a5c1156c | -11.04386 | -52.4638 | 2026-06-27 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d338e6f4-d027-3443-9d07-77ccd6be87ec | -9.58021 | -48.72548 | 2026-06-27 04:32:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55dbc74f-e17d-387d-8852-d5e455cc8de2 | -13.25217 | -54.4108 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5ba8a19-38fd-3d31-bfb2-24f2c28e40f2 | -12.45837 | -58.4889 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 6a2dfe6b-9998-3170-a532-3832263367ce | -14.87532 | -54.53474 | 2026-06-27 04:32:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9ff93b59-5123-39a5-b043-85b46e55f527 | -10.47914 | -47.08447 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6ff820de-e7bf-3abe-acb7-dfee08afe582 | -10.49182 | -47.13305 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 935d9606-2b83-3e61-b0b2-2bd684c7399c | -11.79043 | -57.35233 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a10de2d0-71d7-3eae-bb46-84ca518fd0fb | -9.59068 | -56.92486 | 2026-06-27 04:32:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 01ebf63a-3b68-32c8-8883-a9b125b2775b | -13.08971 | -48.16832 | 2026-06-27 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4e5a28f8-0c49-3772-a9e9-9de482cd9d54 | -10.30007 | -57.1427 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c96d3a6-6d14-32ec-b630-7fdcadd796d2 | -12.44052 | -49.58131 | 2026-06-27 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a0f9fc13-df14-336e-8ef7-f40e6238a698 | -10.48025 | -47.12044 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53a64370-c75b-3cc8-837b-963cf9c352f6 | -12.93265 | -56.62536 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c123c4af-5086-36c4-8bb9-9b115242312b | -10.49568 | -47.13009 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 678baf77-7d96-3f20-99f0-73b7c6fcd0fe | -11.52013 | -54.25525 | 2026-06-27 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fca79d58-9eb7-300b-9280-846b0e7f5642 | -12.45122 | -58.49213 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b13b40e-7d6c-32f7-b55a-acfa68af0a52 | -11.89963 | -57.4082 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e55d3891-df5f-3062-9488-057ebd431bee | -13.66644 | -53.93804 | 2026-06-27 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 903520b8-6118-3f2a-83ee-5e3fced9cbbd | -11.87036 | -57.81847 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0f5186d-abb6-3d97-bcc1-4c95e3535ff0 | -10.48356 | -47.12097 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d4fd73c-b9f3-3580-81b9-769aaba8a76d | -9.06359 | -44.74991 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb4ad580-9001-3104-9138-b01f2b063b6d | -11.66083 | -57.25746 | 2026-06-27 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1696de1d-1d2c-3552-8358-d02a195a1b39 | -12.79759 | -54.86766 | 2026-06-27 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 317135ca-1b85-3508-adc0-c75eef9a4111 | -12.93143 | -56.63157 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57fc43a0-fbf4-3a5c-b6c6-038efe9f7dc9 | -10.57163 | -46.23277 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4811f9d2-8d44-34ed-8126-df4e6897059f | -13.87813 | -47.17004 | 2026-06-27 04:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e85a8771-a867-36bc-9c3c-3b0500ad60cd | -10.90009 | -56.85574 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b80f1170-0770-34a2-9620-341ae7e0b7f2 | -14.69916 | -46.14685 | 2026-06-27 04:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0136c978-5654-3d62-a8ce-3d753af2fb08 | -11.32126 | -54.47197 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93024e7f-58f6-3cd3-9f94-df8acc3a3252 | -15.79404 | -47.99152 | 2026-06-27 04:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d61f7e21-6506-3d0b-8f05-b804777b0c29 | -10.48521 | -47.1105 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4468728-c3c0-3a27-98f3-f6a835e6d611 | -12.4495 | -44.75359 | 2026-06-27 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aeb6e79-cc80-3183-8feb-6e74331e0041 | -12.46452 | -58.486 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d1f0c274-a512-33b3-9354-ffc775682770 | -10.11949 | -48.25312 | 2026-06-27 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 909b2b00-b22c-36f7-a754-5a426f819fb8 | -12.457 | -58.49335 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| f3c9a1ee-a15d-396a-bbca-629df3393c71 | -12.93532 | -56.6388 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 981d40c8-b475-36d0-bf3b-e6d0fd51a43f | -10.49017 | -47.12204 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5a786f0-fc2d-3fc3-b3ce-d6fab119a3f9 | -15.58901 | -46.81213 | 2026-06-27 04:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39826562-ae58-3295-a061-af9d7628d6a2 | -12.93409 | -56.64508 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9e04502-a7fa-397e-8bb3-73a502f53a14 | -10.55217 | -46.24794 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64ef40d1-d550-3748-9393-087ac38a072a | -8.78029 | -47.5324 | 2026-06-27 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caea1238-8bec-3052-a58a-33fdf36b571e | -12.45174 | -58.492 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7e32f113-878c-3ec8-88f6-c859c0e62f67 | -12.62455 | -57.89262 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6b39cfc-277d-3495-8eff-8b8ba48e9f54 | -9.08167 | -44.76398 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 187e5c0b-6b12-3a2e-b5a3-be58ab842b10 | -14.84326 | -48.14235 | 2026-06-27 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b018c67a-f0e9-36fd-8483-eb5c81d27ea1 | -14.87103 | -54.53394 | 2026-06-27 04:32:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ad05be18-899e-3b05-b90e-95243a5efe77 | -10.56495 | -46.23174 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4284c4c8-21ec-3539-8db8-9ab42369549d | -12.93859 | -56.64913 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5c8c076-c3c3-3afa-a051-3715984317b4 | -10.5605 | -46.23835 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c72385c4-3721-338e-b58e-4e090712d646 | -10.93411 | -56.85218 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02f1fb92-7989-3f49-b2b3-1c86718ae308 | -10.48355 | -47.07801 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab61e9d4-aa09-3aec-8875-6515b3fc33fd | -15.58562 | -46.81157 | 2026-06-27 04:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c553057d-fe6c-333f-9ebd-878cd8bf3751 | -12.45788 | -58.48902 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8676dfeb-4f35-3624-9294-2e759bdaaadf | -13.88534 | -47.16756 | 2026-06-27 04:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6910dcf0-76a9-3f21-bc30-2fbd3340f38c | -14.84113 | -48.11284 | 2026-06-27 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ffdefd0-aea4-31a2-a786-dbd63a584c1d | -10.47584 | -47.12689 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0041b8a2-0dfd-3d7a-9106-989d3f130b60 | -10.30626 | -57.14022 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 20296b36-5a86-3876-a62f-4b1cf1e09e02 | -14.83782 | -48.11228 | 2026-06-27 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71f719b5-e914-3f89-9d76-e43c777465ea | -12.61421 | -57.88646 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c7ac369c-56e9-3022-b23f-f09f1e9feeb0 | -9.58999 | -56.92854 | 2026-06-27 04:32:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ab3cf8ea-0944-3eca-9074-3eeceb0e379d | -11.91059 | -57.41019 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b372922-42ef-357d-8a12-7c837f4365e3 | -12.4506 | -49.58598 | 2026-06-27 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15f13c04-5896-3ced-a52a-8e982bbf9520 | -13.26091 | -54.41252 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 904e4337-307b-38b3-b655-890ac32559f2 | -12.60788 | -57.88919 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 893a8002-57a8-348a-b56a-cbcca72e21d7 | -12.44379 | -49.58484 | 2026-06-27 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8df3e806-5bda-35c3-b8fb-d09c7f3d21d6 | -12.16755 | -59.75975 | 2026-06-27 04:32:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e57499b-9440-3932-bff5-356424f94eda | -11.87668 | -57.81598 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfc366b2-038e-373e-a2c7-048307b82109 | -8.56969 | -46.89209 | 2026-06-27 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7eb1d99-3c08-36bd-ae36-64f6b2c81961 | -11.9033 | -57.41591 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 09ef414a-7653-3237-b3a2-bbfcf4a1f256 | -14.85017 | -48.14304 | 2026-06-27 04:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 022f4be4-6d80-3569-9f3c-9eaf239f54b2 | -17.00941 | -49.02913 | 2026-06-27 04:34:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 857f1dce-4a47-3890-8b63-ed6124b6cefa | -16.58187 | -49.53437 | 2026-06-27 04:34:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README16.md)
