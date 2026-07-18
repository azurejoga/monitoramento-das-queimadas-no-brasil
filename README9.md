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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dde06bbc-b065-3f82-9792-a893ca6193a0 | -19.78484 | -48.26261 | 2026-07-18 04:21:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b09543cc-50d3-3afb-b345-603fde786567 | -22.25097 | -52.86884 | 2026-07-18 04:21:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b71bd5cf-6f7a-3a58-99d3-da947d2cb26f | -20.52758 | -42.35904 | 2026-07-18 04:21:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9ed6fdf6-d6ba-303f-85b6-174b2672fa85 | -20.63118 | -41.39899 | 2026-07-18 04:21:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0783b593-dc43-316f-bf90-08efc907cab7 | -22.81589 | -43.56276 | 2026-07-18 04:21:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d5a585f1-30e3-3f36-9d24-430a423144ff | -22.46872 | -43.0873 | 2026-07-18 04:21:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2923e96b-26a6-37ab-b067-06e7db7957a1 | -21.858 | -48.75906 | 2026-07-18 04:21:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 238de03c-2a8f-3e0b-a3f0-d6532486ae72 | -18.72503 | -54.20514 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3526a376-9b55-32c4-8473-a00d6592e7b5 | -18.67569 | -48.18142 | 2026-07-18 04:21:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 55852e61-d106-36bb-8a7b-64a313dae569 | -17.34198 | -42.37928 | 2026-07-18 04:21:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b599e8fe-59f5-3855-869b-1aed1a6e612f | -20.63544 | -41.39542 | 2026-07-18 04:21:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 821f9085-5af5-3cb5-8c04-2eadecbd0de7 | -22.46647 | -43.10313 | 2026-07-18 04:21:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 70e10b64-8240-3245-8cbf-d1d83125069d | -18.73714 | -54.2001 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d116b6a6-a61f-356a-b69a-d305d56a5c91 | -18.73032 | -54.20631 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d0a954cc-b8dc-39ce-a000-f6138e5a8897 | -19.35282 | -44.71018 | 2026-07-18 04:21:00 | NPP-375D | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 255c9c50-fa06-382f-a3a4-8b40f69e4570 | -19.82712 | -57.99852 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4f35af9c-ce7e-31e6-a96d-c2ad13f5d01d | -20.35178 | -48.31874 | 2026-07-18 04:21:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc4c5130-c36e-3380-88b7-818169c29a99 | -20.32162 | -41.51378 | 2026-07-18 04:21:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 27630ada-5f44-3811-85ff-bbdaec2d8607 | -18.73178 | -54.19929 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 57d3ee4c-8a05-3ac1-b534-7daf54c4f213 | -23.76141 | -47.33111 | 2026-07-18 04:21:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a90186b2-a152-3199-8e73-26ea65d03a82 | -22.92128 | -49.20116 | 2026-07-18 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff47a920-8556-378b-a5e0-1f10f8b39539 | -18.73529 | -54.1997 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b4a93af6-f9ec-3ee0-a987-52ef12bca1f8 | -22.9567 | -42.83418 | 2026-07-18 04:21:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ae31cfde-1545-3f51-ade3-0c943e275710 | -20.78344 | -57.93482 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9232acd0-f709-3562-92b9-89ae1309bdd7 | -22.25901 | -52.87599 | 2026-07-18 04:21:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 777c5f7d-92ef-37a0-874b-3adaf3443d4c | -22.79879 | -49.33984 | 2026-07-18 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2baad0b4-a45a-3fe4-a322-2fbc5635bee6 | -20.32586 | -41.51006 | 2026-07-18 04:21:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7d90a5a6-3eaf-37b5-b3c9-4ec3190a112f | -22.24645 | -52.86771 | 2026-07-18 04:21:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6fbf398e-5190-38e5-9f48-20bb6fcdf220 | -20.56627 | -41.96737 | 2026-07-18 04:21:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4c7f6133-eacd-3389-9786-bba8df294721 | -21.25753 | -49.12106 | 2026-07-18 04:21:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0afaf4a7-2bc7-3565-9730-66d1ad49c68c | -19.44522 | -46.20913 | 2026-07-18 04:21:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fec47be-961c-3262-acbb-07a31ad2bd16 | -19.83355 | -58.00027 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9798b426-0c2e-3fe4-a823-5ebe30560a8b | -16.47796 | -47.96055 | 2026-07-18 04:21:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33c7eca3-76ed-3517-aa66-5efa166f43ed | -21.76715 | -56.30592 | 2026-07-18 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e928209-1d45-3999-9b62-eef053efe029 | -19.81357 | -57.94012 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1f805630-cc45-3baa-b858-0799a938cba2 | -18.4148 | -43.72186 | 2026-07-18 04:21:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c8b8537-5c33-3d1d-a3e8-e7669b0e95e6 | -20.07365 | -43.70559 | 2026-07-18 04:21:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66b71d3c-6c03-3c16-8e77-7e580d44359d | -19.80921 | -57.98753 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 16e628c3-9726-3706-b4c2-d2383e3cc328 | -20.35539 | -48.31945 | 2026-07-18 04:21:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e2e6dc7-1388-3aad-ad95-f99d4ece2eda | -22.46702 | -43.09174 | 2026-07-18 04:21:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a27c6b5-ea1c-3470-8d84-231a7431bd10 | -19.83255 | -58.00105 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d0719db1-aae3-3b95-8e03-7854a4003896 | -19.92991 | -44.07181 | 2026-07-18 04:21:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4a4654f8-16db-3d11-b707-77de97d4bd0a | -23.40765 | -46.42203 | 2026-07-18 04:21:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| de837020-f234-354c-828e-79bf49d7a644 | -22.77005 | -43.73111 | 2026-07-18 04:21:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd7e6b84-ea3c-3e27-94f2-e6cb70346088 | -20.61755 | -41.73595 | 2026-07-18 04:21:00 | NPP-375D | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9d7669ad-2fc6-37e6-918c-a5a96fb10690 | -22.79513 | -49.33902 | 2026-07-18 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e24adf03-d84e-345e-948e-40491b3877b7 | -19.81563 | -57.98928 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b205aef7-d10c-3a04-ab91-62a7c03ba4fc | -22.81245 | -43.56213 | 2026-07-18 04:21:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f9bb6ac8-2768-3a8b-a4a1-8fb17dc289ec | -18.00901 | -49.39952 | 2026-07-18 04:21:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0ad5e0f-8b74-3052-998e-24ceafde7caf | -28.75387 | -50.00498 | 2026-07-18 04:23:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 92c7da70-9db2-34d3-a93f-5bd6f6e4a24b | -29.03771 | -50.15856 | 2026-07-18 04:23:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 333422f3-4925-3b37-9523-eb4f3e1cccd7 | -29.04121 | -50.15939 | 2026-07-18 04:23:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d2470109-8a9c-35c3-b997-2a1334e2ea31 | -24.54439 | -50.72195 | 2026-07-18 04:23:00 | NPP-375D | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 94cdb6de-b245-328c-abe9-14c6c5c26295 | -26.0149 | -49.01211 | 2026-07-18 04:23:00 | NPP-375D | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8370108-d3ed-3211-9d89-c707fcf1e90c | -23.81759 | -48.71584 | 2026-07-18 04:23:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22c48de6-52a1-32ac-9b92-b6ebdbdd0912 | -28.99578 | -50.5891 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e517af2d-5871-331b-b430-208a5fdf4b57 | -24.00309 | -48.50526 | 2026-07-18 04:23:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8d837a7c-8254-39cb-a27a-414feb39f0e7 | -29.03954 | -50.88066 | 2026-07-18 04:23:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cd853291-c941-32cf-97ae-50cd585d2370 | -29.27433 | -50.33633 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 39cd91df-ad68-3aa7-8131-4d282ee025d9 | -28.89342 | -50.73787 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cfa21aac-91a8-3f69-a43b-982b86cf3b38 | -29.07559 | -50.72717 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 418ef310-91bd-3f35-a2ce-b96499115258 | -29.27271 | -50.34527 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f83a50e0-474f-3feb-9554-10724c8158bf | -28.09205 | -50.59831 | 2026-07-18 04:23:00 | NPP-375D | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 88661890-d6ef-34a7-a679-e52bf4dc0091 | -28.75737 | -50.00578 | 2026-07-18 04:23:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8dce5d85-582f-3ab2-8223-2f16575f07bd | -28.93933 | -50.67222 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed6e9c23-c1bf-3f65-b725-b22babaf6091 | -28.88626 | -50.73605 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5c06c5bd-1633-308b-bb12-d34d1ae84cc7 | -29.27623 | -50.34609 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b4da4ce3-28e7-382d-8825-8cb00ff109f7 | -28.08846 | -50.59737 | 2026-07-18 04:23:00 | NPP-375D | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 68122ad9-4f12-31ee-b5f5-f45b082c1a73 | -29.27894 | -50.35137 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41ad4a59-79fb-3cf6-bec8-e0b3df0bd0d3 | -28.99934 | -50.58996 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 49df5e64-15dc-372c-beb6-ab9027a3e730 | -24.63457 | -51.01126 | 2026-07-18 04:23:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 631fe493-9e89-364a-92dd-a920fe096ffa | -29.07646 | -50.72245 | 2026-07-18 04:23:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 49b49a4d-75d1-3e9b-a63f-eb6931b9406f | -31.12277 | -54.40429 | 2026-07-18 04:25:00 | NPP-375D | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 6.2 |
| 7e8df4a1-695d-33a1-b2cb-5dc9648efc4b | -29.92558 | -53.91204 | 2026-07-18 04:25:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 29a41b33-08fa-3843-ab20-e607aab572d2 | -31.13106 | -54.40666 | 2026-07-18 04:25:00 | NPP-375D | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 04b24494-9f4d-3d1d-963f-c2a51c77833c | -29.63136 | -51.60016 | 2026-07-18 04:25:00 | NPP-375D | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 0703d499-a077-3e04-9097-f5918dc3ac18 | -29.93064 | -53.90885 | 2026-07-18 04:25:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| a54c0b08-3950-300a-9d80-e83aea368e39 | -29.92592 | -53.90919 | 2026-07-18 04:25:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| e2139fe5-d9b4-3fee-91cd-964831c1ecfa | -30.09891 | -56.65367 | 2026-07-18 04:25:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 11854809-c7b3-36c0-9bd4-64bf54066cac | -30.10012 | -56.65543 | 2026-07-18 04:25:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| d600bce3-711f-368f-87ee-2396a173a5a6 | -31.12692 | -54.40547 | 2026-07-18 04:25:00 | NPP-375D | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 6.2 |
| 70e907f7-7c39-3f5b-9e7e-e541aa55c2c0 | -29.93005 | -53.91037 | 2026-07-18 04:25:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 9f763f56-5d00-33ae-8cd5-5077b0358405 | -29.63133 | -51.60267 | 2026-07-18 04:25:00 | NPP-375D | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| db2a719b-4cca-36e9-b26f-8ef5b8f0da9d | -13.3023 | -45.1511 | 2026-07-18 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 24ec11c9-d7f9-352e-8e3b-e33afacb9a51 | -13.3217 | -45.1479 | 2026-07-18 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 7bb8a033-64b9-32f8-95ac-507483de3fd1 | -13.3221 | -45.1246 | 2026-07-18 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 01b3ca37-2e9d-3806-ae95-e11bb63bad3b | -18.7364 | -54.1988 | 2026-07-18 04:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b4f17bdd-8140-3f1b-80b3-7c24e5e4c92a | -13.3028 | -45.1278 | 2026-07-18 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| e310cda4-cdfd-3e19-a45f-46a8feb178f9 | -2.79656 | -48.57652 | 2026-07-18 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f2c7246-88a2-350f-849d-0d2e08cfee35 | -1.54365 | -51.64932 | 2026-07-18 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d88f985-c79c-3536-8174-f805e2c18436 | -3.4953 | -43.31301 | 2026-07-18 04:36:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e62cab0-f458-39df-8b46-a2be15caef4e | -4.10088 | -49.35315 | 2026-07-18 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbc76dea-b130-36db-8ff9-017e8866deeb | -2.43332 | -47.03057 | 2026-07-18 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae544d12-690d-348f-bb87-10773d8ac7c7 | -4.2557 | -48.65006 | 2026-07-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1588a7a8-6598-3f0d-ab17-e4bc9fca0b44 | -2.79274 | -49.52395 | 2026-07-18 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a51d8308-884c-3057-945a-0e3701ab1609 | -4.8292 | -44.06474 | 2026-07-18 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2f83126-fbb2-3243-9f76-fd12c18a10a2 | -3.71408 | -48.83113 | 2026-07-18 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63c78327-9b56-36ac-90ae-c659183cfd7e | -2.48184 | -47.08738 | 2026-07-18 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 209e8f26-f296-32c2-b0a2-49ded5607043 | -3.47724 | -51.18817 | 2026-07-18 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5e4e3e9-09ef-324f-883c-d2033f75d91d | -0.08815 | -51.28156 | 2026-07-18 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README10.md)
