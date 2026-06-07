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
| 7b50ebee-4af8-3a40-8644-811aa8b3b463 | -12.03986 | -45.27235 | 2026-06-07 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ededfdda-986d-362c-98d2-c265d04c06d2 | -10.39429 | -46.43579 | 2026-06-07 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9f324c5-1c52-39eb-9d09-25dc0dff3799 | -11.03407 | -44.32126 | 2026-06-07 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6145ff95-b4b0-352d-acc4-81d4f9ea7c03 | -11.47583 | -47.33996 | 2026-06-07 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 281e99cc-0970-3e61-bedc-cacbfd2441b3 | -12.06402 | -48.42682 | 2026-06-07 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31b8f13b-c9a5-363a-abd0-bbeb11023782 | -10.53879 | -49.46553 | 2026-06-07 04:06:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 638542a3-36a8-35bf-afd8-2a67ebd8fa10 | -15.66313 | -43.31392 | 2026-06-07 04:06:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c585d44-194f-3975-8fea-343abdd7516c | -12.50294 | -46.25733 | 2026-06-07 04:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a8457d2-ce1e-3eb0-bb72-9f0139f878b7 | -10.39362 | -46.43965 | 2026-06-07 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dbb9605f-f97e-3fd5-9cf3-77ad36edc36b | -22.41463 | -46.79391 | 2026-06-07 04:08:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0db70f46-f3da-3841-a15b-b20536e7af19 | -16.50239 | -43.50394 | 2026-06-07 04:08:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74a79651-9ac2-378d-baa4-262b5d8121b0 | -16.49965 | -43.49968 | 2026-06-07 04:08:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ec17239-6caf-35cc-b0b2-1d500a42dd41 | -17.51419 | -41.9136 | 2026-06-07 04:08:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 64f49e2c-abd6-3fb4-8aec-e2cb4709de63 | -16.04308 | -50.55574 | 2026-06-07 04:08:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5399b81-280f-3b20-b2c2-b44389e91431 | -17.99924 | -54.27906 | 2026-06-07 04:08:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f334502-539b-31ed-9c39-2d233a861bf0 | -16.0419 | -50.56178 | 2026-06-07 04:08:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3bf5f76-9c64-36c7-904e-16c58c34d9dc | -18.45836 | -54.70667 | 2026-06-07 04:08:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b0063dc-143a-3c70-848f-ff25ac69563f | -17.53046 | -46.54012 | 2026-06-07 04:08:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5f03c9f-e3fd-341f-a62d-d6e04dd3c570 | -18.00415 | -54.28513 | 2026-06-07 04:08:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5e5dcd0-4471-3ba9-94a5-40c8ec050a8f | -19.68503 | -46.02895 | 2026-06-07 04:08:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 791a0fc5-b8f3-3f18-b914-822c1a5b5f9a | -19.96499 | -47.20439 | 2026-06-07 04:08:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4b235e3-36b1-3f8b-a7cb-27d9e5d133e3 | -18.21223 | -46.73087 | 2026-06-07 04:08:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc4ec5a7-eb64-30b5-9e4a-7da3ead24964 | -22.8524 | -46.32664 | 2026-06-07 04:08:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 970391fb-5719-321b-8856-3b20473c9e21 | -18.45885 | -54.70522 | 2026-06-07 04:08:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2eb17f68-b947-3732-b680-7c173de65487 | -17.51363 | -41.91724 | 2026-06-07 04:08:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| adc4e7ea-18e9-3c32-a513-fa58f315c6b1 | -19.68858 | -46.02963 | 2026-06-07 04:08:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26e3ef8a-b4d3-39b1-bf8a-9c8c88489665 | -21.38949 | -47.43045 | 2026-06-07 04:08:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a908a721-7fc5-393a-b9d5-22d4acd7ff2b | -19.96124 | -47.20374 | 2026-06-07 04:08:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3880e0a5-be5d-3a55-87de-98d3f3ac57b6 | -16.49904 | -43.50336 | 2026-06-07 04:08:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 33e19ac1-0c44-3728-8c91-27db887a83d7 | -17.69959 | -43.02111 | 2026-06-07 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ca14f49-f50f-3d0a-9e08-5cdd8de4e314 | -17.9359 | -47.01651 | 2026-06-07 04:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b103305-ecc0-3347-8064-4247c80ef130 | -17.99333 | -54.27743 | 2026-06-07 04:08:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08c1747c-0552-3dd4-a298-8bb9d4b541b0 | -22.37858 | -47.01795 | 2026-06-07 04:08:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d10c502c-c830-3477-a3da-a7bb1780c0f5 | -16.6046 | -43.36285 | 2026-06-07 04:08:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51f0c3f4-d934-3aa8-bd4d-7ca4d1934167 | -17.99106 | -54.27957 | 2026-06-07 04:08:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b382cab-608d-3893-b4a1-7e24eb948462 | -16.60794 | -43.36342 | 2026-06-07 04:08:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 065f52e2-4cfb-3b6a-828c-6f668567abde | -20.69009 | -47.52401 | 2026-06-07 04:08:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88e10ac2-f0b1-39e1-a4bf-dafc20b856a0 | -16.79002 | -54.17117 | 2026-06-07 04:08:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b98f84e3-830f-30d4-9012-2f6b5b939828 | -18.0019 | -54.28735 | 2026-06-07 04:08:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe3064f2-9162-34da-89fd-d1ab6bd04514 | -20.69063 | -47.52203 | 2026-06-07 04:08:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8984a93d-d771-3569-9383-9cfd5ad2f1e4 | -18.0029 | -54.28281 | 2026-06-07 04:08:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33417f51-0ba1-3732-9a7f-0ca9950e4a3e | -16.78403 | -54.16943 | 2026-06-07 04:08:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb4e4ee4-45e9-3241-b832-a9be2e1b5b8c | -18.2126 | -46.73236 | 2026-06-07 04:08:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da9d6356-8324-3b07-894d-3ca31d0b69ab | -21.33215 | -49.18216 | 2026-06-07 04:08:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 77ea2b78-6445-3e81-b0ea-130a67e16a69 | -17.99697 | -54.28123 | 2026-06-07 04:08:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2884e95-156f-38b3-a4c4-69d43b31c879 | -17.99821 | -54.28363 | 2026-06-07 04:08:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f60f863-2dd1-31e7-9b4c-17ddf1337e86 | -18.96485 | -41.96949 | 2026-06-07 04:08:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3e8ca1db-9692-3661-833e-04ca45d48eeb | -17.99206 | -54.27498 | 2026-06-07 04:08:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4721c0d8-05ac-3364-8e6b-07286593d271 | -16.43323 | -43.7247 | 2026-06-07 04:08:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 520ee344-aee8-3f50-9460-35c6b99dd80c | -21.98448 | -57.61166 | 2026-06-07 04:10:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2c319be9-ef08-3baf-b46e-14f047bc599f | -23.82307 | -48.71452 | 2026-06-07 04:10:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 128642f0-8504-392a-be7c-5e719efc0362 | -27.13066 | -52.64753 | 2026-06-07 04:10:00 | NOAA-20 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b08a2c29-8964-3c63-a5aa-2f84dff19697 | -23.45094 | -46.70955 | 2026-06-07 04:10:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e0fd955b-5a4c-3d70-b246-df8dc8e7b4c0 | -23.23175 | -46.65371 | 2026-06-07 04:10:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af1179aa-c5a1-3d37-aa11-2d449f989ae1 | -23.81926 | -48.71367 | 2026-06-07 04:10:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f567496-be92-34de-8601-6f3957f6db52 | -23.82404 | -48.70937 | 2026-06-07 04:10:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 983e5e52-60a1-352c-9253-ab55ab49c87f | -21.98586 | -57.60625 | 2026-06-07 04:10:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 05d70b03-f838-31a9-9910-5a8728c2b576 | -25.05676 | -50.87761 | 2026-06-07 04:10:00 | NOAA-20 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7493b19c-5d2c-3361-8953-826738eb0c8d | -23.10319 | -46.53738 | 2026-06-07 04:10:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fab2e475-98a7-3bfb-8d13-cc93bfab7a2e | -23.12985 | -46.73798 | 2026-06-07 04:10:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8e71a1d8-21e9-3934-97a6-5f787202832d | -21.9886 | -57.61287 | 2026-06-07 04:10:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5143ed22-7b90-36f7-b72d-9aba2d37f60c | -21.98994 | -57.60748 | 2026-06-07 04:10:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80ed59f6-f430-38fb-9de3-9058d969253b | -23.76695 | -47.44235 | 2026-06-07 04:10:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e4b4189a-af50-3aae-83bf-f52bfa2fe5d9 | -21.98207 | -57.61065 | 2026-06-07 04:10:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f26c9d2-c9c5-3ca9-94f0-6b9a14c3f351 | -21.98343 | -57.6052 | 2026-06-07 04:10:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72c0c707-461f-3ca2-95f9-8f173ddc0d34 | -2.21327 | -51.38272 | 2026-06-07 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5f2eb43-4198-31e9-b5ed-70946b281a71 | -10.31128 | -48.22622 | 2026-06-07 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20b65565-b639-31a5-9250-d18f22123fee | -10.53985 | -49.46385 | 2026-06-07 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d287f8f4-4c50-3e63-afb3-633e4df56ee7 | -7.87779 | -43.93172 | 2026-06-07 04:51:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d514ebcc-b6c9-36e1-b280-003e5550e20b | -7.18643 | -43.4135 | 2026-06-07 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d1cfd46-19bf-3f54-98ca-b6dbb550ab09 | -5.94193 | -45.50401 | 2026-06-07 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 143e15e7-f911-358d-9c11-3b415a3a862d | -8.46923 | -50.22028 | 2026-06-07 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5680d593-7c0a-3237-a94a-eacfef0d3a53 | -8.16916 | -46.82616 | 2026-06-07 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a40f26d-4b4d-35e2-9321-59448ee763c2 | -5.80448 | -45.12059 | 2026-06-07 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 023ac68d-d12a-3817-9a6d-de34b98233d1 | -9.07596 | -50.59784 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 94d08de7-a207-3c05-b694-ec8ec81702b1 | -5.81388 | -45.1217 | 2026-06-07 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89fddb5d-3696-3d44-9ce6-d23998103cfa | -9.08935 | -50.60385 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f89935a7-a133-3460-8578-660bd732731d | -8.03058 | -46.05001 | 2026-06-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6d16a27-b84b-3dfa-99bb-ee7306fd4ed1 | -5.80988 | -45.11624 | 2026-06-07 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 149dd3bd-e193-38b0-a661-26927a6af9b7 | -7.87823 | -43.9284 | 2026-06-07 04:51:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 997060a0-f4b8-3e80-be1f-389d8da4a10f | -6.439 | -44.58411 | 2026-06-07 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff36ae9b-5e2f-3ed8-8462-873b3e7e7478 | -8.12262 | -47.6169 | 2026-06-07 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de5c1c1e-fe17-3291-9093-43cbbea0cf8b | -7.56045 | -49.41803 | 2026-06-07 04:51:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c3f1477-372d-3123-b56a-0979f502e110 | -9.09633 | -50.60491 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86023ffc-46c8-323b-80b8-2b0cf51cd48b | -8.86742 | -50.1949 | 2026-06-07 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b0017bc-98fb-3090-b89e-fd01d164796d | -9.18322 | -58.05914 | 2026-06-07 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca76d2d-4115-35d5-8cf1-02e0c59f6a1f | -9.07653 | -50.59391 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecb6c714-528a-388b-9cf6-07b5f8de5efe | -9.5256 | -48.68682 | 2026-06-07 04:51:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c58eb54b-bd26-301a-9944-cde82c96e20f | -9.09284 | -50.60438 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbef45ad-9f29-37e5-8cce-22e377354043 | -7.31832 | -47.06861 | 2026-06-07 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d227b2a-528b-3786-afcc-a3da1de83ff4 | -8.86802 | -50.19085 | 2026-06-07 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f12a2973-bfae-3b3c-bf64-253f26b5f454 | -6.987 | -42.88132 | 2026-06-07 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e033a1c5-2cc9-350c-b564-026616ff005f | -10.18829 | -52.64794 | 2026-06-07 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6fb5c6b-5423-32fd-b85a-8763e506df5c | -11.03244 | -44.31835 | 2026-06-07 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5c0af79-5795-3d6e-8012-a4640e73c2ad | -10.31177 | -48.22266 | 2026-06-07 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b43f0ea-19c9-3c9b-b9c9-d16e9c8a795e | -7.11521 | -48.12991 | 2026-06-07 04:51:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7df68abb-0846-30f5-b73e-7ec07d8505c2 | -7.00295 | -43.8637 | 2026-06-07 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 429bc3f8-874a-3132-97a3-7e8879967acb | -7.32197 | -47.07302 | 2026-06-07 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 046244be-ab7b-320a-86b5-12085f349a25 | -9.09225 | -50.60831 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32d0256d-f147-37b2-9ce0-29d08e492092 | -8.93864 | -45.67148 | 2026-06-07 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README5.md)
