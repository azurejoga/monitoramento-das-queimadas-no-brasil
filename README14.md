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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 321bc11a-ae39-3e9c-a112-b09e7ac194dc | -5.71611 | -44.81189 | 2024-11-19 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7f99c0a-0ac0-3d3e-a379-11a622dc3946 | -5.86999 | -40.177 | 2024-11-19 03:27:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5caeabb7-c644-311a-b4e7-18450099151e | -6.70008 | -43.95215 | 2024-11-19 03:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3eeab48-2daa-314b-884f-cf4cb78d3402 | -7.99625 | -44.37171 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 74e13fae-5237-3e61-8813-38667cb6e77d | -4.99496 | -44.33087 | 2024-11-19 03:27:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 779ed9d4-3a33-3040-b5f7-043fe09c06dd | -4.11642 | -43.58872 | 2024-11-19 03:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e074321a-292a-3132-b15f-68a758e7dbf8 | -5.97535 | -45.36785 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 4b09be8f-48c0-37c1-95f8-8755902cca9a | -4.10992 | -43.58745 | 2024-11-19 03:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cfb46364-dbd4-3ad3-85a9-e8ac0a1385b5 | -8.00613 | -44.39025 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66353462-8da2-3d74-99a8-8c85bfd1a8c2 | -8.00675 | -44.38914 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1720db52-eb5b-3c85-8b3a-4b21f146e7ce | -4.11433 | -43.59523 | 2024-11-19 03:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 062bb3fc-afed-3bad-b1bc-121c39484f24 | -5.98364 | -45.36225 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7408d638-57c9-34c2-a67e-f1a27de7aebb | -5.86948 | -40.18001 | 2024-11-19 03:27:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f5af04b-7aa7-3274-91ab-13d9c28a50b6 | -7.76063 | -35.25817 | 2024-11-19 03:27:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 48749842-c3c0-342d-b485-74a48ec4563b | -7.89749 | -44.22373 | 2024-11-19 03:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6616ae66-4332-3ef1-b969-d238e441997b | -5.58303 | -44.88279 | 2024-11-19 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5022119-4510-3c3a-b014-05f2c19948d1 | -5.8235 | -35.38819 | 2024-11-19 03:27:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4c0cb602-2244-36e7-aa58-1d5e60935aac | -5.44936 | -43.24477 | 2024-11-19 03:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e7cafafe-7516-3a2c-b2f4-0fc81a175b14 | -5.59718 | -44.8826 | 2024-11-19 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c498f13e-fc07-3bfe-a2e3-a89760fe8268 | -6.39432 | -44.74467 | 2024-11-19 03:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c57dd107-a336-3247-8be4-d5e851e62d91 | -7.38317 | -35.10531 | 2024-11-19 03:27:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c7f3dbc5-5cb1-362c-b4d2-1b52f93fb1ef | -5.81978 | -35.38761 | 2024-11-19 03:27:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 59451753-5138-30b2-a06b-3a41283a9ec0 | -5.53358 | -39.17741 | 2024-11-19 03:27:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ca37797f-0820-328d-9c82-be3598dcbe89 | -4.99566 | -44.33971 | 2024-11-19 03:27:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d662895-d69f-368c-9bbe-788a098ac1ba | -7.75517 | -34.95448 | 2024-11-19 03:27:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 5b946724-b1ca-3671-a97b-9ba9400bb22c | -3.23176 | -42.69822 | 2024-11-19 03:27:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71b645cb-47f2-3822-af50-c876f101d9c9 | -6.93116 | -42.81027 | 2024-11-19 03:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4490c0d7-2922-3c7e-8094-944a8a51448b | -7.89919 | -44.21907 | 2024-11-19 03:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a8b212f-4d21-310b-a1a6-32108541ad63 | -5.82424 | -35.38374 | 2024-11-19 03:27:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| fb6f0251-efbf-33fd-b4fe-beb0b3f8c7f8 | -5.58355 | -44.87944 | 2024-11-19 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d167325-51de-36db-8f00-afbe923e65bb | -7.9949 | -44.38145 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 845005ea-3db0-3663-b4e7-8c74e2e0dcc6 | -7.50006 | -34.98874 | 2024-11-19 03:27:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7afebb8b-3391-3283-8701-dafb5fbfb5e3 | -7.99594 | -44.37607 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c68235f-8a72-305a-a01d-47e1fdc68c2f | -4.12184 | -43.59076 | 2024-11-19 03:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99440261-f90f-3f77-8f34-7236b98e6f66 | -7.25344 | -38.53226 | 2024-11-19 03:27:00 | NPP-375D | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2a65e77-7de6-3708-9378-b76510fabd23 | -5.87253 | -40.17627 | 2024-11-19 03:27:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2adf32e7-ec7a-34d6-aac3-9eae744f3a20 | -7.89818 | -44.22432 | 2024-11-19 03:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a121c0a3-dbc5-3268-b803-bb99224207f9 | -7.39122 | -42.77131 | 2024-11-19 03:27:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc8a9c9e-d94e-39e7-84ea-b02f68c546b2 | -6.40337 | -44.73338 | 2024-11-19 03:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca9d7986-08ea-347b-9b75-795bccb37a29 | -7.99525 | -44.37712 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa812357-2284-3a00-86b1-5affd609b734 | -5.38986 | -40.66059 | 2024-11-19 03:27:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4aaacef6-5fa8-3105-ae82-ebd487b5a725 | -4.10894 | -43.59319 | 2024-11-19 03:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 95c4f4f3-4551-383e-9f03-3e6d79312b62 | -4.11633 | -43.58391 | 2024-11-19 03:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 655cb091-bc2f-3941-8562-c903b62c1fa4 | -5.72289 | -44.81341 | 2024-11-19 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3bd518b-bef4-3134-b4f3-f76064ef190b | -3.92032 | -42.41428 | 2024-11-19 03:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ec0309dd-7e46-38ac-a2e4-110a3d94b962 | -7.51378 | -37.21384 | 2024-11-19 03:27:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f32c6b5-9181-39e2-85cc-02c5e1446dd2 | -5.95531 | -38.63033 | 2024-11-19 03:27:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 798bbf8b-bf70-3cb3-912d-09c5af4b06f3 | -7.75095 | -34.95787 | 2024-11-19 03:27:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 10f8e65e-9366-32e6-bb8f-96f141386a0a | -5.60398 | -44.88432 | 2024-11-19 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d729e771-6162-3568-bdbb-09624884b912 | -4.99383 | -44.33725 | 2024-11-19 03:27:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2a13040a-9027-3828-ada5-138ea0f8f3be | -8.51104 | -35.44444 | 2024-11-19 03:27:00 | NPP-375D | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d8475de9-ab94-3a98-891b-5bf1129bba1a | -5.87674 | -39.6268 | 2024-11-19 03:27:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 465bce60-3f4d-3af5-ab05-e9eb6652950b | -5.95136 | -39.67035 | 2024-11-19 03:27:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2c8cf136-c56e-360b-bdc4-5010bc28aa51 | -8.00571 | -44.39455 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f633c376-9adf-375b-9526-82e28ebbe1ae | -8.52142 | -37.06137 | 2024-11-19 03:27:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d9e0455d-0b0b-3a2b-befd-e151579b098c | -6.05777 | -44.04549 | 2024-11-19 03:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c676746-3b84-3942-b5b5-9c27218283e1 | -6.567 | -39.43475 | 2024-11-19 03:27:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3b443dc6-f173-338d-b1ff-0702fd85d727 | -5.86506 | -39.66481 | 2024-11-19 03:27:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 984fd29d-ede3-3959-be4b-39a46ad7564b | -8.00069 | -44.38366 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffd7fc60-d159-3632-a84d-9a3a04a0059d | -4.11548 | -43.59427 | 2024-11-19 03:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6a3527e4-bca8-3e6a-9673-49998e18ab15 | -7.40451 | -42.76513 | 2024-11-19 03:27:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7d15bbb7-d3e8-3e39-a6d1-716d614799ec | -5.86015 | -39.66394 | 2024-11-19 03:27:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 818c9463-fb51-3a47-9968-207214c6f86e | -4.11532 | -43.58963 | 2024-11-19 03:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8691bf94-1c18-3179-8d06-83cb12daf517 | -4.99681 | -44.33348 | 2024-11-19 03:27:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74768764-f214-3c69-840d-252eb758876a | -3.41665 | -42.38633 | 2024-11-19 03:27:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 05fba67b-33a7-39fd-994b-62b7d8478b99 | -8.00031 | -44.38796 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 968a090b-2927-3d7a-8f3e-e09f60a0ba8a | -6.42939 | -35.25071 | 2024-11-19 03:27:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a3e8c1c6-97b3-3dfa-8d93-5a854883f81a | -3.5905 | -43.62605 | 2024-11-19 03:27:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a07e7dd-112e-3f21-9f11-c839dc9a2495 | -6.39546 | -44.73846 | 2024-11-19 03:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c15ba1ba-a69a-3b7b-b993-e1b91bd8d88e | -7.99425 | -44.3825 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4b089c8-9691-31e9-9f9e-e5991d1168ed | -5.22649 | -37.73145 | 2024-11-19 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 67c1b2a1-0afb-3dd3-9dd0-47960dfffca6 | -5.9506 | -39.6678 | 2024-11-19 03:27:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b855e739-fcbc-3e3b-815e-2350a06272fa | -6.70003 | -43.95506 | 2024-11-19 03:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bf69552-f730-3fa4-979b-8e51a480618f | -7.39938 | -42.75993 | 2024-11-19 03:27:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 60a72b9d-6213-3cd3-b239-3b857272e694 | -5.98484 | -45.35573 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a8ee8e69-03ea-33be-acf4-1f6b023c6a97 | -6.05122 | -44.04451 | 2024-11-19 03:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f14b38e-802c-367d-a646-a64365f9d09b | -5.98242 | -45.36891 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 656cadea-058b-317e-adb4-42bf47a111e9 | -6.70097 | -43.95002 | 2024-11-19 03:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc9526b2-e6fe-393b-9778-456ddcf98dd5 | -5.872 | -40.17926 | 2024-11-19 03:27:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e38b0c2-12a0-3da6-ab85-c2c49bf0ebfb | -7.89112 | -44.22246 | 2024-11-19 03:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d47bbdf2-a688-3a77-a6f3-91869581e426 | -8.26267 | -44.01733 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ff01439-1768-3b52-8eaa-d871c604cd85 | -10.13673 | -38.5201 | 2024-11-19 03:29:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 4d9ccd1a-acaa-3086-bff8-d85ec8d765f3 | -9.7712 | -35.88343 | 2024-11-19 03:29:00 | NPP-375D | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ea327564-e586-395f-849b-7414a3d1cf76 | -10.9718 | -44.53154 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93443095-4c6e-3070-b253-d04f456e6e7e | -11.24488 | -44.65736 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac379806-f29b-3494-995c-76ce69fcf37e | -10.13968 | -38.52374 | 2024-11-19 03:29:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f5391d37-6d30-3d6e-8753-2265ea14efa8 | -9.24931 | -45.00214 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 76b8a8bd-8c65-3873-bbb9-7a58203a17e1 | -8.27801 | -44.02299 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9871385-8faa-3cb0-bb28-ace49e242e63 | -10.97276 | -44.53483 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e6548b55-11cf-3983-afba-3de9c218e2b3 | -8.26613 | -44.03355 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a94a7a6d-0d4f-3348-bba6-7e837989f343 | -8.26174 | -44.02229 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 316e57b7-b54d-321b-abad-3a848e063f07 | -8.26563 | -44.01984 | 2024-11-19 03:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 254fe6fd-fe60-38d6-8a8e-d34d4e6f6a17 | -9.25721 | -45.0065 | 2024-11-19 03:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c1ee988-7345-3bf9-b476-e662232766d0 | -10.14093 | -38.52103 | 2024-11-19 03:29:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 4ffbf8af-62e8-391e-b52c-6cde51900efa | -10.41254 | -36.64304 | 2024-11-19 03:29:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 08e23e92-3609-39b2-ae14-09a574171e5b | -10.97082 | -44.53643 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 17790ccd-276b-36d6-b8e4-bd1f5eec76cc | -12.27854 | -43.5278 | 2024-11-19 03:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dea19a6c-277b-349b-8514-88a0f9b3abb5 | -10.40322 | -44.47822 | 2024-11-19 03:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0acdfb67-e524-36bc-9d0e-572f652a528d | -10.97693 | -44.44257 | 2024-11-19 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ea2c057-87a1-33f0-b4c1-4e9576cc3422 | -8.86928 | -40.77921 | 2024-11-19 03:29:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
