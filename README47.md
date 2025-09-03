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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8cd0f06-dbdf-3b6b-b95e-85ad6759a578 | -22.18513 | -47.49477 | 2025-09-03 03:57:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9efcf5e0-2129-3f8b-b653-da80e8694912 | -23.39532 | -45.96427 | 2025-09-03 03:57:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d8855cfb-8290-3cd3-ad67-4cdcde616d40 | -17.18901 | -46.06201 | 2025-09-03 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27691c6b-54db-3818-a092-af6559c4d794 | -22.7584 | -47.26522 | 2025-09-03 03:57:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce921b93-41e1-33b9-b9f1-12d63575b7af | -23.35403 | -47.17435 | 2025-09-03 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0f67eb6a-11df-3c98-a918-fbb8a41395ab | -17.29261 | -47.7023 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 563141dc-2eb5-3219-8d4d-fd7066400c90 | -17.52869 | -47.5797 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5af48d8-ba41-3a91-b83e-15bed52196d1 | -22.48741 | -43.72351 | 2025-09-03 03:57:00 | NOAA-20 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f0800db6-902a-39e1-bc5a-673400ad209f | -18.66413 | -49.09153 | 2025-09-03 03:57:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f9bca8d-48d3-36eb-b413-e745d6efe2c9 | -17.52807 | -47.58282 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e4e75ae-2ecf-3808-92a4-963dd1e29faa | -22.18097 | -48.82194 | 2025-09-03 03:57:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| dff12a70-ecdc-36b8-9b5c-4a9c980f247d | -23.3579 | -47.17511 | 2025-09-03 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 38ceafd0-898b-3668-ba18-180d56409be6 | -20.68855 | -46.31171 | 2025-09-03 03:57:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fca2754-96b9-3684-bee9-637559f4396f | -18.03278 | -51.58829 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 220e9aaf-1885-359d-9013-915b63e0d267 | -18.19793 | -48.12867 | 2025-09-03 03:57:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e225bcb-8420-3fec-ae1e-ddf6f01b4a16 | -22.7045 | -47.03725 | 2025-09-03 03:57:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de1ab0ef-eaa6-3ff1-bae5-50cee66df1b5 | -19.14536 | -47.59805 | 2025-09-03 03:57:00 | NOAA-20 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b48092d-3b47-3d08-82b4-46754afccebe | -17.53759 | -47.58064 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f45931c3-32fd-33f0-8420-2ed9bbe6324a | -18.07055 | -45.98902 | 2025-09-03 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2096a7c1-e37d-3ec8-a66e-a4ea2a30acaa | -16.85874 | -49.60328 | 2025-09-03 03:57:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03942756-e388-3196-b186-41f492204bab | -22.86502 | -47.38704 | 2025-09-03 03:57:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 047a32f7-0c87-38f5-9798-3c116f570137 | -22.75449 | -47.26434 | 2025-09-03 03:57:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b483902c-0392-386e-b904-c53cb4d6ac7a | -19.75297 | -43.29394 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 704b4291-0117-3a15-ad99-40d28da12cbf | -17.5324 | -47.58396 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9fce4cce-d005-37a0-afb4-0055dd37a5ce | -15.73725 | -53.69041 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff54d073-be2a-3cd5-a13d-35b1cb498291 | -19.75167 | -43.30166 | 2025-09-03 03:57:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 95171814-c42f-311e-ada5-adb5baf105d9 | -17.92679 | -47.22078 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 338eef0c-ea83-36ba-a696-a8ba218f6440 | -17.93946 | -47.21695 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1216a011-8146-3670-a6b0-3c8ccec08310 | -23.71839 | -47.36682 | 2025-09-03 03:57:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 63bbdf32-3138-3b7d-b22a-08f9b680a6d2 | -16.29942 | -52.96626 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67d4588a-6b3f-3759-8f2c-ab237f9f0531 | -17.92336 | -47.209 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efc2252d-09d0-32bd-bfca-1f79ecffc9a9 | -19.12212 | -46.44195 | 2025-09-03 03:57:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57e33ec4-aed0-3080-a223-9c271dcca192 | -16.28951 | -52.96558 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2cf49ec-bfed-34bc-8e37-a8697af116c2 | -19.74892 | -43.29714 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 76e72793-c8ea-3de3-b509-b2769e78067d | -17.54054 | -46.60649 | 2025-09-03 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c311bff4-5eec-3ac0-af05-60cc5fecba88 | -21.0867 | -45.45808 | 2025-09-03 03:57:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0776a56b-cb00-3328-8941-996319fbb982 | -22.39927 | -44.4687 | 2025-09-03 03:57:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f7770130-6613-3fcd-a55c-99448645f98a | -20.70411 | -46.30073 | 2025-09-03 03:57:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97dff0f0-4a1c-3f82-8af3-563ab3460ca1 | -15.71854 | -53.63832 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf4285f5-1ca1-3f45-b739-dd1f4215e5af | -16.94909 | -53.52227 | 2025-09-03 03:57:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10f4c2ee-9c92-3447-a4dc-7c84b03ebcdf | -22.18351 | -48.83203 | 2025-09-03 03:57:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 08346489-2d23-3abe-8fdc-bfb3591eaa7c | -17.94131 | -47.23026 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 981c8ef5-2fb2-30a6-b255-398774fb03de | -16.59455 | -48.97679 | 2025-09-03 03:57:00 | NOAA-20 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c7c9bc5-e44a-3191-b851-161b675a5119 | -16.29828 | -52.97149 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 271d442f-8441-3bd0-9c1c-7bef21ffc4d7 | -17.24665 | -44.86476 | 2025-09-03 03:57:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cb9d6d6-3eed-3197-b501-de1432d7a96b | -17.43649 | -47.20581 | 2025-09-03 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e9c298f4-ff5a-33c8-a3a1-441f3d9f1df6 | -15.74508 | -53.68616 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cf62bd0c-7b36-34f8-ade1-a61d562bef50 | -22.1843 | -48.82991 | 2025-09-03 03:57:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 8e83c60c-894a-39a4-8f47-fd94e783fad7 | -22.1777 | -48.8368 | 2025-09-03 04:00:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| 591fdf41-098f-325f-b4aa-7862239ba4f7 | -22.1784 | -48.8134 | 2025-09-03 04:00:00 | GOES-19 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.5 |
| 8a540431-7acd-3797-9da4-3fcd0d32ac6d | -12.9573 | -56.9839 | 2025-09-03 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 156870cc-65b7-32b6-bbb5-df8dea103b10 | -12.9382 | -56.9856 | 2025-09-03 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 609defbc-63d6-3c38-a375-32d91837fcf2 | -3.2305 | -47.135 | 2025-09-03 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 11b93902-2e21-3cfd-9c18-9db305e2e7fb | -12.9385 | -56.9655 | 2025-09-03 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| ec5fdcc5-d2d5-3dd5-a2b8-6cf6d5bfc589 | -3.2306 | -47.1131 | 2025-09-03 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 5b9ac2c5-d79d-320e-b5e8-57da5fbbd9da | -3.212 | -47.1357 | 2025-09-03 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| e414830b-fd7c-3e81-ad7d-8797e22953cc | -23.76634 | -51.62937 | 2025-09-03 04:00:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 872dd839-935f-38c4-bf81-54aa7a1ed6f5 | -23.76568 | -51.63243 | 2025-09-03 04:00:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 3f16fddb-511a-3048-903a-dec52a357b0a | -25.04141 | -49.27364 | 2025-09-03 04:00:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b40700a7-5938-3e1e-ac33-2f28ebf64566 | -23.76702 | -51.62627 | 2025-09-03 04:00:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| ca6f2d32-cd7a-3577-b5d9-699853cfbf6e | -27.22688 | -52.90928 | 2025-09-03 04:00:00 | NOAA-20 | RIO DOS ÍNDIOS | RIO GRANDE DO SUL | Brasil | 4315552 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1ed5f169-520e-38a6-a454-af5d9cf9efeb | -27.23189 | -52.91059 | 2025-09-03 04:00:00 | NOAA-20 | RIO DOS ÍNDIOS | RIO GRANDE DO SUL | Brasil | 4315552 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aae5ccdd-7f75-33b9-8537-4cff3784e401 | -3.2305 | -47.135 | 2025-09-03 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 52960293-4206-3959-8d06-8e3b9c3b166d | -3.2306 | -47.1131 | 2025-09-03 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| de70d7c6-d47b-3263-ac12-80f06f325192 | -3.2306 | -47.1131 | 2025-09-03 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 76873f4b-e74e-3a55-bc94-0e8f07c61ef9 | -3.2305 | -47.135 | 2025-09-03 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 5a2def44-cbca-337c-bcab-6fa4a5d8f13a | -3.212 | -47.1357 | 2025-09-03 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8d01b839-e606-320d-b044-fb179707a8ef | -3.2305 | -47.135 | 2025-09-03 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| d72737cb-967e-3a89-ad38-a1b1854cdba3 | -3.2306 | -47.1131 | 2025-09-03 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 12fb4971-5866-3424-976e-2ab4f7151606 | -3.2305 | -47.135 | 2025-09-03 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| fcb24f23-95df-3c7a-8331-d37236709af3 | -3.2306 | -47.1131 | 2025-09-03 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| fc8286fc-c1c8-3fe7-825e-197e24c5c4fa | -3.2121 | -47.1138 | 2025-09-03 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ef75b8f7-81d1-3242-be41-752069d17bd2 | 3.84342 | -51.81536 | 2025-09-03 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7b77a2d-fc78-37cf-97dc-47a75f8b6a33 | -1.32994 | -50.68383 | 2025-09-03 04:44:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 545e68da-0691-30de-beec-611d858534fc | -3.60153 | -51.53531 | 2025-09-03 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37af4493-023a-3627-9a13-65b440f0dadd | -4.89588 | -43.21766 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 093d5dbf-4eb0-307e-a656-c7b594fbab4c | -3.48604 | -51.18866 | 2025-09-03 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7145d71-b339-304f-a47e-758bc70ecd03 | -4.74087 | -43.57726 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 193ba36f-6d85-3939-bd45-da33eff1c8ae | -3.22077 | -47.12391 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ede9106-6a8a-3236-85c3-2d8b02523618 | -4.03034 | -46.94748 | 2025-09-03 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58fcafac-0dee-3c88-a9ac-60e537ff3bac | -2.19999 | -47.99623 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7a526b-b21e-3123-a73c-386c79653f67 | -4.78528 | -43.66406 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c38f399-bbce-3fff-98f3-22b1eec493db | -4.67977 | -42.92889 | 2025-09-03 04:44:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59c35049-e1b4-37fd-b536-25c7d5597564 | -2.56208 | -47.7147 | 2025-09-03 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac4d1082-ee78-35a0-a0bf-662c666e796c | -3.81186 | -52.26855 | 2025-09-03 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfdbdfc9-adcf-3856-af48-37a36f42af5a | -4.85196 | -42.74188 | 2025-09-03 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6da60b9-995b-39a5-801c-192e6e12b22d | -2.77761 | -48.59634 | 2025-09-03 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89b595b0-17f1-342b-88af-0694f8c53d47 | -2.88796 | -48.29158 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb859da3-329e-33d1-9407-5933762a4e5e | -4.82953 | -41.80673 | 2025-09-03 04:44:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ccc8ea7-bd20-38e3-a626-86dd532a3a67 | -4.10654 | -48.20675 | 2025-09-03 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae43d9f5-500b-3e9c-a75c-510e22f5edc6 | -4.16392 | -46.78222 | 2025-09-03 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 884ae622-74b1-3d44-9315-d7349df10e51 | -2.89811 | -48.29241 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6c6fb61-a666-31db-9b92-bf68f791394d | -3.22804 | -47.12507 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8099aea3-9c73-38e5-91d3-06f29bbd8f71 | -3.35818 | -43.38011 | 2025-09-03 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0de238d4-25a7-3a9d-afef-7433f3ae8732 | -3.41359 | -51.56292 | 2025-09-03 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2739d3d-2aae-3031-902c-148dc5042845 | -2.94239 | -54.80165 | 2025-09-03 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2109ad2d-4d44-37e6-b546-6dc786c38995 | -3.9802 | -44.46424 | 2025-09-03 04:44:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0402dc10-1536-3372-927f-fb8c6e323043 | -4.16325 | -46.78664 | 2025-09-03 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 76e0de4e-d1a2-350d-a51a-f1a9bbb94159 | -3.2244 | -47.12449 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 63363f14-3d30-3bc0-b9af-32ad1396eb49 | -3.16181 | -48.60575 | 2025-09-03 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README48.md)
