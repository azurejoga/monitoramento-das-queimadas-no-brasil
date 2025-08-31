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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a4c3b7a-8d51-34f1-80c8-701db18b1d81 | -15.22926 | -56.07204 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d52b55c4-66d5-3c9b-8a3e-f128efb5a07d | -15.67766 | -52.72625 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb7bf2c2-5f55-3c43-b759-7e696f5e9d98 | -18.05502 | -45.95145 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1efbd5e-57cd-3b12-9a25-238080c5fa1f | -15.70931 | -48.93188 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55a1e436-cb21-319f-9812-2aa355c0fca2 | -15.2115 | -56.05373 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d258cc47-c5a4-395e-943d-d2892def0fd0 | -16.40723 | -45.64992 | 2025-08-31 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b588c2a-1498-3ced-a1ed-5b417c7eb120 | -15.21979 | -56.06651 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af3d67c7-f5bd-3abd-bf01-069ea8b2e962 | -16.22174 | -52.68857 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3c4857ce-aba5-341c-aec0-58765bc84819 | -19.05964 | -49.35192 | 2025-08-31 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55e2c7fe-4e63-3081-bd0e-3ad28bb32847 | -17.61225 | -52.68515 | 2025-08-31 04:53:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98015afe-3b56-3c5e-9f0d-1ac11402cdc9 | -15.71883 | -48.92483 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74a0fe2f-7479-3d15-9d55-bbf8bb53547a | -15.71527 | -48.95237 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fd7ba5f-9d40-30c9-b157-51517cb3d87a | -14.80051 | -59.71865 | 2025-08-31 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12edd6db-2f2b-38e6-8440-d1052d3ff51d | -16.21943 | -52.68019 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64127f8d-edb4-35a4-bd81-720915904327 | -14.58009 | -54.52847 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3550dede-25b5-30c2-943e-76d3830810a2 | -18.05925 | -45.94889 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ede2891-75e1-3559-84fc-17138ca9107d | -15.71203 | -48.94414 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6b4c067-cdcf-33e8-b8f3-750f6cfa9e2a | -14.60767 | -54.54763 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bef62b49-7734-34c8-90df-1838f69697e2 | -14.96005 | -54.81019 | 2025-08-31 04:53:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 825b5181-97b1-3a58-90c8-54595e514aae | -16.99027 | -49.3331 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15f96236-b3b3-34d7-8307-70812ea84bee | -17.14726 | -46.0757 | 2025-08-31 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f199717-ee82-3a40-a212-5dcfa62da655 | -14.95568 | -54.79484 | 2025-08-31 04:53:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fcab1c6-fb34-3042-9716-02d5573fa26c | -16.53761 | -55.05512 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8165632e-254d-3d2b-8184-f04fd3fad3c2 | -16.22524 | -52.6649 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08a44a0c-8d4a-39cd-85f5-656d91ba96e1 | -20.47862 | -53.6746 | 2025-08-31 04:53:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34c27f4d-3d93-3793-8aaf-48ab6a0af063 | -16.2212 | -52.6683 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24102411-757c-3a91-9511-8e94de557249 | -16.22061 | -52.67226 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7033a679-e733-3e65-b1f7-b3063212b913 | -16.40686 | -45.65325 | 2025-08-31 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 676f10e0-1b84-3457-a8e3-da2eda91be32 | -16.21545 | -52.65926 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a8d483c6-a323-3b45-b099-a82dcd3dcc51 | -18.05462 | -45.95498 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f52fad9d-b436-3630-96ce-58a58bc711dc | -16.97284 | -49.30285 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b4c8ffc-03c7-3795-bb31-1e6fcc782dd4 | -15.7078 | -48.94362 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da0160aa-7230-3ba5-85fe-150a7c56407b | -18.0585 | -45.95609 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a536e91-abd6-3a4f-a1ce-956251c13361 | -14.60823 | -54.54408 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 403b13e9-4101-3e88-b2dd-b704a71f9229 | -14.60557 | -54.49621 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf11dbaf-12d0-3253-a510-19fd453abfbd | -16.23446 | -52.67444 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f2b97bb-1d3a-3a26-8b39-f4b89a4295b3 | -16.53874 | -55.04794 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e11cf871-4d14-38f6-a289-4b0bccb46562 | -18.05887 | -45.95254 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e42de75d-d992-3c83-b15c-98fa17eed001 | -15.21643 | -56.06588 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39981446-727a-3aac-8cb8-3c3b980f9646 | -17.47833 | -46.99937 | 2025-08-31 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77635071-e878-30d7-b093-6d4689965303 | -16.53543 | -55.04738 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c115deda-6b20-367c-910b-9aa214dc1ecd | -16.22519 | -52.68912 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 015e268f-90f0-3653-ab6c-4f82c765d9de | -17.14795 | -46.06951 | 2025-08-31 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d75a820c-4f68-3827-9569-722f043612ed | -14.80441 | -59.72001 | 2025-08-31 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13c30e6a-d996-3d75-a70e-7b2324b963aa | -14.59549 | -54.5602 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5ad59f6-f03d-3414-9dfe-151ce59dac38 | -15.79572 | -55.9119 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 50957c5b-029c-358b-8e2f-aabf1f2a2b5b | -18.04972 | -45.95057 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c414ab76-3f0c-3245-94ff-59ded8cbdf9c | -14.60655 | -54.55474 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24b1a194-94e9-3507-ab39-9c946e7e22d9 | -16.98291 | -49.32406 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64d0de92-0b58-3f58-b0da-a00efa92241f | -14.60832 | -54.50032 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5a3da15-f22a-3120-accc-2269308eaf2e | -15.71778 | -48.93291 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23bcb271-49c6-3662-8215-b2654b9bb938 | -15.71677 | -48.94074 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecb3f19d-481c-3ff1-904b-1976e0123bb5 | -14.7952 | -59.72511 | 2025-08-31 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 272f8181-9a2e-3353-81b9-ad4f6447f425 | -17.566 | -52.53149 | 2025-08-31 04:53:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 600724ba-27bb-3dd5-9df9-f0fa2507f426 | -15.68856 | -52.7434 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04924b14-7216-3757-9231-5a97596e0a7e | -16.58361 | -56.20509 | 2025-08-31 04:53:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 77105308-3528-3562-9f35-9edc325f76c4 | -18.06495 | -45.94599 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 597a9447-f866-3c90-92f7-acfb0cb04da0 | -14.79448 | -59.7291 | 2025-08-31 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77a1f89f-19f7-38ce-a009-ec996384125c | -16.22008 | -52.65189 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bbba445-8b72-39f5-9b66-effc2b1d2158 | -16.53212 | -55.04682 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a2b09bf5-cf54-3531-ad1f-c0d3917a0214 | -16.97924 | -49.31945 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21c5ace5-a668-3720-9667-616ceb8d6551 | -14.60935 | -54.53697 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0b67c39-fbe8-3aaa-b62d-cdbadd2e35ea | -15.79036 | -56.39724 | 2025-08-31 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eef18eb7-11a7-3bb8-9e58-53e926b9ecf7 | -15.22986 | -56.06839 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fec4847-84b4-37ca-8ec2-6071c18ec0ea | -18.65432 | -48.22342 | 2025-08-31 04:53:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15a0150b-d568-36e3-9cb0-4d854894f7d4 | -15.22866 | -56.07573 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d160f1cb-4136-34db-9782-4bf3989ca6bc | -14.60221 | -54.51754 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed6e4eab-17d1-3881-b1aa-815fcff1cabf | -16.74417 | -49.30981 | 2025-08-31 04:53:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7013abb-0f18-3ea9-954f-a6481f0fbbb8 | -15.2253 | -56.0751 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee14a579-f3f9-3796-8ecd-35eca088f504 | -15.21703 | -56.06223 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bb2763f-e07c-3740-8bf8-fe2e5d6bdeb5 | -16.22116 | -52.69245 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 99e2a721-df2a-37e5-860b-a7239e2fa080 | -14.95512 | -54.7984 | 2025-08-31 04:53:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f97b334-d1f0-3ea9-92d8-fde3812c5b3c | -15.72205 | -48.93317 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d78169b-6d47-3830-8ac2-876f2973be90 | -15.16458 | -52.34297 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c185d29-fb15-3277-a2f9-2eed12754bbc | -15.70984 | -48.92781 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e12bafa8-d1c4-3973-935c-e8fecf135997 | -15.23202 | -56.07635 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5567c78a-7be3-30e5-b7dd-6b71e2471322 | -14.79912 | -59.72634 | 2025-08-31 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1860ccd4-8a5a-3d9b-81c1-19f5cf249d64 | -17.14205 | -46.07496 | 2025-08-31 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 751a0fd4-865a-396c-8f56-629338b84d87 | -15.6891 | -52.74392 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 341f3702-5b8b-35cb-a273-87dea7bc10db | -16.53818 | -55.05153 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 124f8c0e-b772-3e8d-a07c-8028cb0bd720 | -14.6038 | -54.55064 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e507b9d-1f45-3b94-8f9b-cf60dfaf34a5 | -15.68744 | -52.75112 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fe90f95-f41b-3465-be28-e343cd18e16f | -14.60664 | -54.51098 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46406213-7d29-33cf-8bd2-495f95bbdf2f | -18.05581 | -45.94434 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b0ed7ab-4da9-32aa-96d7-bc6168b74855 | -15.68566 | -52.7434 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5e2668f-3a8c-3c38-9f52-90502d02b0cf | -18.66346 | -49.0962 | 2025-08-31 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c0cae6df-9ea1-3ca7-a423-8cf4138e429f | -15.79374 | -56.39784 | 2025-08-31 04:53:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fea380ee-36d8-3f82-9aa7-3b79493495b2 | -17.14627 | -46.08444 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2e0eae3-12ec-3f8d-bb32-99703dc5df92 | -17.56247 | -52.53097 | 2025-08-31 04:53:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b749c925-3c83-3828-9951-c6897c61208c | -16.97875 | -49.32326 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e6387c2-73b9-3085-9b3f-5b028ccc57a5 | -14.60552 | -54.51809 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7059484e-a90d-3879-98b7-fd5fa26adcd1 | -15.22195 | -56.07446 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba9dc86d-e44f-3184-87fe-2e04a96ba3a8 | -14.58998 | -54.55199 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 981cc30b-c664-3ef5-bfad-d1eed6ff9766 | -17.14659 | -46.08161 | 2025-08-31 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 82fc238a-2e6a-31cb-9195-af68441e30e6 | -16.96445 | -49.75179 | 2025-08-31 04:53:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d91d99f-44d2-31b5-8ca8-9410e40728c3 | -16.76616 | -50.30243 | 2025-08-31 04:53:00 | NOAA-20 | SÃO JOÃO DA PARAÚNA | GOIÁS | Brasil | 5220058 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cded0a3-db29-3e79-bec1-0dec77dd4b0c | -16.97652 | -49.3074 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8804575-58aa-3242-be1f-7a3b23082136 | -15.71406 | -48.92841 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cebb263-42ad-35ee-bcff-e40fa78be267 | -18.06606 | -45.9492 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3991b22-2013-3a5e-b789-22ccc1dab352 | -15.71154 | -48.94799 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README71.md)
