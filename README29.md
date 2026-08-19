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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0549b6a-31f3-3c7b-a3d2-cb10243d8b69 | -8.5598 | -54.7579 | 2026-08-19 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| bbd48a36-6d12-3cce-8c92-2fe9151d7c13 | -17.60142 | -52.62831 | 2026-08-19 04:21:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cbee72d-d437-3b4e-976f-0a8713951851 | -18.87683 | -44.20623 | 2026-08-19 04:21:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c868918f-f6fa-3048-9cc0-1879d6c1e313 | -20.57318 | -45.93579 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec4969d7-fad5-357c-a406-4896e4bba9a8 | -15.60966 | -49.31465 | 2026-08-19 04:21:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 314ec9ea-7dac-3c7d-b62c-ceecdaa4e65b | -21.04488 | -48.47481 | 2026-08-19 04:21:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5afee1a6-58c3-3d6d-af22-b3bd771621a5 | -17.59263 | -44.59897 | 2026-08-19 04:21:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c93930fe-dd72-3537-8020-8aa6f235bfd2 | -21.74784 | -45.00217 | 2026-08-19 04:21:00 | NPP-375D | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| be18a152-79ca-3dd0-8335-77abfef68a1a | -18.8631 | -48.8781 | 2026-08-19 04:21:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0202ed2-c638-3430-baeb-819103a6db30 | -19.66971 | -45.90476 | 2026-08-19 04:21:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d0fbe0d-18a4-3603-8a4b-6c053e21fc9e | -20.58629 | -45.91883 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b37b62b7-a3ec-3d51-8d82-3cc334360928 | -17.3573 | -39.74205 | 2026-08-19 04:21:00 | NPP-375D | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5d245618-7e38-3a81-8534-c35ef6aa7056 | -17.99318 | -48.54419 | 2026-08-19 04:21:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f5d3901b-405d-34f7-9b54-b218be434a9a | -20.29729 | -46.482 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72737a8a-f29d-326f-9e59-6bb867bd9591 | -15.4428 | -41.38423 | 2026-08-19 04:21:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c07080f9-2f13-3b23-917e-e0519c9a739d | -19.67184 | -45.91283 | 2026-08-19 04:21:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ac12e818-7ae4-386f-809b-33ce544b115e | -14.46172 | -45.62862 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e73c514-9693-3421-8333-9badf718834d | -16.57878 | -51.62201 | 2026-08-19 04:21:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 465d3d0d-7eef-300d-9ca3-3c64812023bf | -19.57006 | -49.43512 | 2026-08-19 04:21:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3379aa7-c5a9-3737-a1ce-557e4d720a16 | -19.06958 | -57.36047 | 2026-08-19 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 746d9e01-3477-3a2a-8ee4-36ade17c6a82 | -18.58511 | -41.33031 | 2026-08-19 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bea83bfe-9c26-3d55-bfd3-5d02ea037b2b | -20.48892 | -45.24509 | 2026-08-19 04:21:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3dacd0da-86cf-38ff-b239-35b267128630 | -17.45528 | -47.85818 | 2026-08-19 04:21:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 239eabc8-d867-3453-929a-db5a3336504e | -17.98778 | -48.54489 | 2026-08-19 04:21:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4248f3bf-dfcc-3426-a937-160cda8df70a | -15.32057 | -56.4602 | 2026-08-19 04:21:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2641672-7614-33e2-907a-8c677c7ad2e6 | -21.11343 | -45.60683 | 2026-08-19 04:21:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 68a302a1-e7ef-3455-a13b-5ea2ef50a674 | -15.07179 | -45.32498 | 2026-08-19 04:21:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73fb3b36-b236-375e-85d9-5fbe9b4eb490 | -15.39824 | -47.56813 | 2026-08-19 04:21:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf49f55-b537-34e4-9e51-1d406c59daed | -18.58626 | -41.3222 | 2026-08-19 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5479ca1b-744e-369d-9132-eec436b4aa1c | -18.84497 | -47.1407 | 2026-08-19 04:21:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 472a1b82-97bd-3a07-b466-6b45331fe53b | -19.87795 | -44.05019 | 2026-08-19 04:21:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c528f46f-4f27-3239-87a5-e1005808a509 | -17.98856 | -48.54814 | 2026-08-19 04:21:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 558a20f1-5017-36d8-847c-fb8e35e8353c | -15.06777 | -45.32814 | 2026-08-19 04:21:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f04a8672-e3ec-3a9b-90f9-59e76f581a21 | -20.5738 | -45.93197 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 474054a0-fe4d-358b-aec5-e98fde8e0479 | -17.47639 | -48.87364 | 2026-08-19 04:21:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52e2c4c8-a628-35a8-bdab-ed910dffc5db | -15.06437 | -45.32755 | 2026-08-19 04:21:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2310930-c982-3719-b352-03efb8ec0370 | -13.46719 | -51.78838 | 2026-08-19 04:21:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8b87fdf-ca84-339d-a147-3dda538d99e2 | -14.49255 | -45.66908 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 882ffc0a-d8c0-3a22-b76f-d454db9c5977 | -15.44222 | -41.38815 | 2026-08-19 04:21:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2df0bcb1-f85c-3fdc-9d50-5069e0456b10 | -19.48204 | -45.97923 | 2026-08-19 04:21:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47067899-ccb6-3dcf-8900-13fc02a611d5 | -16.50601 | -48.83774 | 2026-08-19 04:21:00 | NPP-375D | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af9af632-8afa-31b1-9f6c-eab28bfd0dc4 | -15.23087 | -48.26205 | 2026-08-19 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68b2bf90-fabc-3b54-b625-4c25d6755438 | -14.48909 | -45.66846 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9504971f-8f6b-3ee6-beb4-6646a53856c9 | -20.1337 | -41.48961 | 2026-08-19 04:21:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 57764544-ff7f-3b7c-8bc3-51e02c33ee6f | -14.4863 | -45.66398 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a87d09-343c-31de-b951-c411963f45e5 | -15.3141 | -56.45876 | 2026-08-19 04:21:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b33ae74-aecf-3a1f-9a13-7196ed40b7f2 | -16.60926 | -43.37332 | 2026-08-19 04:21:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b0e1f3f-968a-335d-9a4d-a4a6d71138a5 | -18.59291 | -41.32729 | 2026-08-19 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 38e3eef1-597a-3f48-8cf2-d1fb65338ad5 | -15.19998 | -48.23322 | 2026-08-19 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3eaf0b12-e8f7-376c-9a2b-ff4717dc7360 | -20.57986 | -45.93707 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88714ff7-1a70-34f6-b61a-35fc77019b3b | -17.98941 | -48.54334 | 2026-08-19 04:21:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2452e280-ea65-34e3-a051-45264fce4378 | -19.05063 | -57.35542 | 2026-08-19 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| edb65554-9461-3344-bcac-81c4410d3034 | -19.67246 | -45.90908 | 2026-08-19 04:21:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c9faf7b-3baf-3f10-a283-9bda91edb19f | -18.58267 | -41.32153 | 2026-08-19 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 46e1f187-04fc-337c-a3a6-ef618cf21528 | -20.29306 | -46.46549 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9ba53a1-2917-3140-a6bd-1d2f3c651767 | -14.46862 | -45.62985 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b00fbd7e-67a1-3d15-80d5-d85a886568ca | -19.14771 | -44.69817 | 2026-08-19 04:21:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7b2dbbf-e470-33f9-8e8f-0e56ad1faf4d | -20.30067 | -46.48267 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 797100bd-f101-3987-8e47-58797d4cb045 | -14.96671 | -41.77291 | 2026-08-19 04:21:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf477571-01d8-3dc8-a810-66085b5b109b | -14.48009 | -45.66775 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a768968-1f6d-3322-b1b8-73d9da22d7a2 | -14.46517 | -45.62924 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9bb4dc58-a516-3027-974a-a0eed7b309ae | -14.45763 | -45.63187 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5fe1634-de1f-369c-8edf-9873c79f8580 | -17.94242 | -44.42442 | 2026-08-19 04:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98770f18-b83a-3f39-bc94-974a67ca10e0 | -19.95124 | -44.70506 | 2026-08-19 04:21:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6efaa15-5de3-3e30-92c1-f5d750a9dbe4 | -15.90575 | -42.65772 | 2026-08-19 04:21:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| abb67261-87ca-3667-9b97-4ba1e70176a8 | -20.28168 | -46.47087 | 2026-08-19 04:21:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d85b008c-b431-34c5-8491-e39e4186b579 | -15.70933 | -47.8054 | 2026-08-19 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b462daa0-64e7-36db-acfa-51e641c7da06 | -14.48499 | -45.67173 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5ac7ca3-bc45-3021-a291-1fb06a4eeff8 | -18.00365 | -44.46857 | 2026-08-19 04:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec80fa26-3b19-3618-acd9-01bbcc3b4bf1 | -19.46659 | -44.17791 | 2026-08-19 04:21:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01c7ba38-e770-318b-bcb1-865597137f4b | -21.39997 | -45.95033 | 2026-08-19 04:21:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f2957616-b60b-3520-84c4-0ae7a17efbd0 | -16.2534 | -57.66133 | 2026-08-19 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0e5749d0-7ee6-3ff7-bdd7-4d88e33be929 | -18.84848 | -47.14133 | 2026-08-19 04:21:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7fb46e4-e2b4-3ba2-ae19-1dc7b732ea77 | -20.48559 | -45.24448 | 2026-08-19 04:21:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c556273a-4b42-326c-83a0-a0bf554d0248 | -15.40197 | -47.56881 | 2026-08-19 04:21:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acac843c-15be-303a-8704-ae9730d18dcd | -14.46108 | -45.63249 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ca4bce5-f2b3-351b-b4dd-0dc7eb035aaf | -20.58654 | -45.93839 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b573593-9ce5-38ef-9ea3-fd3c3fd63c5c | -20.4131 | -44.0865 | 2026-08-19 04:21:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 188fa21d-3569-3b14-afb5-41b147055609 | -19.39491 | -46.41815 | 2026-08-19 04:21:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b798d7e7-85e7-347c-b221-719646d0d8ce | -19.48141 | -45.98304 | 2026-08-19 04:21:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b003025b-52a9-31c2-b1c7-50b8b4450d3b | -18.58569 | -41.32622 | 2026-08-19 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9dfd3100-3488-3ba5-87fb-311606899024 | -18.58208 | -41.32565 | 2026-08-19 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 762ed50a-b04d-3e47-b3d6-2b4fe576c935 | -16.0738 | -54.81081 | 2026-08-19 04:21:00 | NPP-375D | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99fdae13-7411-399b-b687-5d2949972196 | -19.10429 | -39.73091 | 2026-08-19 04:21:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3f4adab6-bb81-3606-8bb0-a543873b0286 | -16.96031 | -43.55346 | 2026-08-19 04:21:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba02fd4f-cb41-332d-9f85-b896daeeca57 | -17.60255 | -52.62271 | 2026-08-19 04:21:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76dfe1f7-8ee7-3fd1-8fcb-02bf291b3e4a | -20.41252 | -44.09023 | 2026-08-19 04:21:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26fdde8d-3d11-3ea1-8b14-249239595452 | -20.6049 | -42.94757 | 2026-08-19 04:21:00 | NPP-375D | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc1e1cc8-36ff-3968-bfe3-968ce43189cd | -14.46453 | -45.6331 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b0492056-80ec-3624-b0e4-f70ddb923c84 | -14.19743 | -51.8168 | 2026-08-19 04:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acc17af0-f43b-3f11-9dd7-b3723960ce37 | -19.46934 | -44.18217 | 2026-08-19 04:21:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c107bd71-16ab-3d7b-aa8e-d80ab79096a8 | -14.45418 | -45.63126 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29b4cd79-726f-32e9-8fa5-36f032b56700 | -14.48564 | -45.66785 | 2026-08-19 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b3a3fc4-3c7e-3f2a-9aeb-bc25a5f376b8 | -19.56944 | -49.43667 | 2026-08-19 04:21:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43bcbfa0-09a6-37af-beea-e3d803213a54 | -19.05694 | -57.35712 | 2026-08-19 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| af083ee3-38ec-32dd-9da1-1fefa85314b2 | -18.67646 | -52.65294 | 2026-08-19 04:21:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03299b2a-fcb9-3d30-8e0c-9c425e3f8eaa | -15.23141 | -48.25971 | 2026-08-19 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d4c3191-01a1-3d1b-95c0-c625fdb4d14b | -20.57046 | -45.93134 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9dcd7dcc-0f0f-3ec5-a27d-59af7f2ec8ed | -18.63066 | -47.2939 | 2026-08-19 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1fc7082-0504-3e47-8668-a85ae35004d5 | -20.57652 | -45.93643 | 2026-08-19 04:21:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README30.md)
