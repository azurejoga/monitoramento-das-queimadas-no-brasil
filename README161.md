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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 183c1c38-cde2-3fff-a398-9fe54be7b352 | -23.37938 | -51.47023 | 2026-08-28 18:45:00 | AQUA_M-T | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 3d2bf780-eac6-30f8-9e23-ddd1824fcf39 | -21.06637 | -40.97712 | 2026-08-28 18:45:00 | AQUA_M-T | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| f43b49c3-6c1a-3713-b747-68da23c9be6f | -24.46145 | -48.96195 | 2026-08-28 18:45:00 | AQUA_M-T | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 3fd4f91a-9d29-30a7-817f-848053eda3c9 | -24.90259 | -48.49126 | 2026-08-28 18:45:00 | AQUA_M-T | BARRA DO TURVO | SÃO PAULO | Brasil | 3505401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 4a842100-379a-3a17-83ab-ca20afbc83cd | -25.03081 | -51.20607 | 2026-08-28 18:45:00 | AQUA_M-T | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| c7bea3ca-2444-3e93-8eb3-e65e7299e23f | -17.58417 | -51.6512 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| f883b985-7321-3525-9468-1f6cb15bd583 | -18.11144 | -51.60014 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 820ec70f-5bbe-3fff-bf4b-d4c9890570bf | -17.29669 | -46.57814 | 2026-08-28 18:47:00 | AQUA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cefb1de6-16d7-388d-a46c-b56ea2b0ee80 | -14.9268 | -41.25663 | 2026-08-28 18:47:00 | AQUA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 8c7c3d2e-58e1-3919-8a29-af5be929bdb5 | -18.62491 | -44.29924 | 2026-08-28 18:47:00 | AQUA_M-T | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65afd845-dbcb-3260-a1b0-e6c1b0650702 | -20.64162 | -52.65951 | 2026-08-28 18:47:00 | AQUA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ba52bfa2-5b62-345e-aae2-bb13c7ed4e17 | -14.03661 | -47.80135 | 2026-08-28 18:47:00 | AQUA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5068ea7b-658b-39f3-a939-c9535b01a369 | -13.85942 | -40.13778 | 2026-08-28 18:47:00 | AQUA_M-T | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| b4ed05a5-463c-3568-85f5-b5d0094c0f4c | -14.17599 | -48.77447 | 2026-08-28 18:47:00 | AQUA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| d6c08075-34aa-3489-8695-5d1496404cc6 | -14.20635 | -52.86672 | 2026-08-28 18:47:00 | AQUA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b7e14212-a19b-3578-80ca-1a4644a76998 | -14.19587 | -41.24932 | 2026-08-28 18:47:00 | AQUA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 564e2c32-61f2-36d0-b7cd-13d8c2d84062 | -14.23776 | -44.43752 | 2026-08-28 18:47:00 | AQUA_M-T | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 04d611a2-ed5b-3902-9b59-f3062bc2fe60 | -14.44209 | -52.60753 | 2026-08-28 18:47:00 | AQUA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 505fc8ef-dc4a-3f23-b7ea-6660fcacf2db | -14.19706 | -52.84908 | 2026-08-28 18:47:00 | AQUA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 0c0e00a3-73be-3a10-b270-3d8c49d614cb | -14.60209 | -53.15151 | 2026-08-28 18:47:00 | AQUA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 21a220f4-8d10-3d65-a16e-a9b7049c9c58 | -20.46882 | -48.78255 | 2026-08-28 18:47:00 | AQUA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.0 |
| 289f9689-e279-3835-b559-e0334a471663 | -14.20002 | -52.87377 | 2026-08-28 18:47:00 | AQUA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 37e22a5b-aaf9-3a16-a057-d6491741697c | -13.66161 | -47.7515 | 2026-08-28 18:47:00 | AQUA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2852e891-821d-3581-9f7b-1574d88d5a39 | -17.62143 | -51.62409 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 273.7 |
| b6b7239c-7609-3506-86a3-95a60981512c | -14.90155 | -52.64301 | 2026-08-28 18:47:00 | AQUA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| be8f896e-2fe5-3977-84c4-f58a71c2e1e2 | -16.21006 | -42.19165 | 2026-08-28 18:47:00 | AQUA_M-T | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 60c443a8-cc8a-31cb-b8cf-e62515b3cf4f | -17.9252 | -42.8025 | 2026-08-28 18:47:00 | AQUA_M-T | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2569d814-acf8-321f-a051-eda8e076c87e | -17.30727 | -46.58681 | 2026-08-28 18:47:00 | AQUA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 6876b434-f1e6-3119-a019-3c8293352e6c | -20.50961 | -45.42345 | 2026-08-28 18:47:00 | AQUA_M-T | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| fdc850a5-5df5-3147-bd9e-22ad37f0ac8d | -14.43563 | -42.20871 | 2026-08-28 18:47:00 | AQUA_M-T | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 860d82a4-29ea-3640-8b38-a68de875cc93 | -17.61742 | -51.61992 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 197.9 |
| cbf4d557-8650-36bf-920e-9f7a8da17fff | -14.33962 | -47.25259 | 2026-08-28 18:47:00 | AQUA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 08540c97-4aa0-3fad-bb8f-b1ea4b1f07f6 | -18.11387 | -51.62217 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7eabff3c-e618-39cf-968d-faf4cebac729 | -14.20349 | -52.8414 | 2026-08-28 18:47:00 | AQUA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2ad47992-c456-3ced-a5a9-613e0c9d4c50 | -13.59647 | -45.78482 | 2026-08-28 18:47:00 | AQUA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 1156c57d-553f-33c1-8d7f-10ebab5e79cb | -20.69535 | -50.49903 | 2026-08-28 18:47:00 | AQUA_M-T | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| 92bbfa82-bffd-3dd5-8da2-cd881cf32e39 | -20.6937 | -50.47134 | 2026-08-28 18:47:00 | AQUA_M-T | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| a526a63f-db47-3063-a33b-0ac47588cd26 | -17.17732 | -41.42901 | 2026-08-28 18:47:00 | AQUA_M-T | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 0e58e470-7671-3395-b704-c1bd693c87e7 | -14.55412 | -53.3032 | 2026-08-28 18:47:00 | AQUA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c3f1ec6a-9587-3862-961f-0189c93cfd5b | -17.59492 | -51.62745 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| ad9a74df-26b2-3637-8a64-0395b9592129 | -15.74088 | -51.16858 | 2026-08-28 18:47:00 | AQUA_M-T | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 15bb38e5-3bb8-3a62-8b0d-74992c5bc4c1 | -17.17899 | -41.6353 | 2026-08-28 18:47:00 | AQUA_M-T | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| d5a25195-f3a4-36e8-9ccf-86d2d9cbbb1a | -14.88778 | -52.6448 | 2026-08-28 18:47:00 | AQUA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 537.4 |
| 39649338-c7ab-3f29-93ac-213947ed61b1 | -14.33825 | -47.24265 | 2026-08-28 18:47:00 | AQUA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3f8bdcb7-2ec7-3035-8c47-49826ee1d644 | -17.93889 | -44.41394 | 2026-08-28 18:47:00 | AQUA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 78cf8791-d89e-324c-8f04-35c8c35edf2d | -15.78718 | -41.98675 | 2026-08-28 18:47:00 | AQUA_M-T | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 93baef5c-94ae-3bcc-a614-54d91b9a6f65 | -15.74327 | -51.1879 | 2026-08-28 18:47:00 | AQUA_M-T | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 16131956-c3d0-3cd5-ab07-6611f5f2dab5 | -12.80822 | -42.71773 | 2026-08-28 18:47:00 | AQUA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 25.1 |
| edcbe983-bb25-3f0a-b97d-7a016cd928c4 | -16.98673 | -42.29969 | 2026-08-28 18:47:00 | AQUA_M-T | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 81f8bdd7-f787-34cb-9280-4fb7db3e818e | -13.60524 | -45.78345 | 2026-08-28 18:47:00 | AQUA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 7d0261c3-8625-3c36-af99-a8893b20d92d | -16.30511 | -40.51291 | 2026-08-28 18:47:00 | AQUA_M-T | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 30bd14de-30e7-3cff-8950-f7bc8fb60b14 | -18.9838 | -43.74268 | 2026-08-28 18:47:00 | AQUA_M-T | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 582782f2-8d1e-380a-bcc1-a5f9d7f8ebec | -14.03769 | -42.16169 | 2026-08-28 18:47:00 | AQUA_M-T | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| c21fca8e-50bd-3f5d-a255-4845d799cc52 | -18.64031 | -48.25419 | 2026-08-28 18:47:00 | AQUA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 6d7402de-d2c5-389e-b977-e4193ee81ebf | -16.17806 | -45.64042 | 2026-08-28 18:47:00 | AQUA_M-T | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| b67933ab-1022-365f-b362-b5f377850e5d | -14.80576 | -43.55537 | 2026-08-28 18:47:00 | AQUA_M-T | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 45f71412-bb47-3c8f-9b09-3e50e7c53cb8 | -20.69592 | -50.49213 | 2026-08-28 18:47:00 | AQUA_M-T | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.9 |
| ced16f51-f9c6-350e-ba91-40a9443f5bf2 | -20.693 | -50.47845 | 2026-08-28 18:47:00 | AQUA_M-T | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| 381c2c7a-e165-37f0-b70d-aae4025df5a5 | -19.18445 | -44.91806 | 2026-08-28 18:47:00 | AQUA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4df535e1-030c-367f-b336-1b776742dc20 | -14.40826 | -50.0576 | 2026-08-28 18:47:00 | AQUA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 984897b5-90e2-32cf-97c5-2253da1718ac | -14.89863 | -52.61849 | 2026-08-28 18:47:00 | AQUA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 55a57aa7-f164-3bdd-92d7-ef85c7cf6fbe | -14.05994 | -40.6371 | 2026-08-28 18:47:00 | AQUA_M-T | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| c05d343c-36a1-37be-880a-bf8a89d15a0c | -15.60159 | -41.79795 | 2026-08-28 18:47:00 | AQUA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| af205bd0-645e-3a6c-b70c-86c7e67a0f59 | -16.20838 | -42.18112 | 2026-08-28 18:47:00 | AQUA_M-T | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 96f16e65-703b-3aa0-bee1-764e8e2f81c8 | -13.59517 | -45.77584 | 2026-08-28 18:47:00 | AQUA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4b04eaad-3b93-3a7a-bef3-a53746f3773b | -14.41022 | -50.07256 | 2026-08-28 18:47:00 | AQUA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2c3514f2-a18a-3c70-8e59-8d320d930e02 | -15.6478 | -53.85862 | 2026-08-28 18:47:00 | AQUA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| d75c2db7-91f9-3bcd-a373-b6ee0c65134c | -16.47852 | -42.31171 | 2026-08-28 18:47:00 | AQUA_M-T | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 2964226b-7000-34c4-9af0-1a88a1d11cf5 | -13.66021 | -47.74119 | 2026-08-28 18:47:00 | AQUA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 90a79618-dd38-3e77-b6f4-462f49c7a121 | -19.47569 | -45.61354 | 2026-08-28 18:47:00 | AQUA_M-T | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9aec6c52-a073-3d1e-8349-7ec9802fbf22 | -17.29807 | -46.58821 | 2026-08-28 18:47:00 | AQUA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 27b22750-040c-3e98-b3cf-fd99b644a94d | -19.26245 | -40.17554 | 2026-08-28 18:47:00 | AQUA_M-T | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 3cbc2178-e344-361b-ab6a-26927fdfb236 | -17.5974 | -51.64911 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 209.5 |
| aa268f9a-e115-3bdc-90e1-f3cc7069e9d0 | -16.17673 | -45.63119 | 2026-08-28 18:47:00 | AQUA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4b0364e8-8df1-3347-a73e-bcf435d4e6e7 | -18.83589 | -47.40428 | 2026-08-28 18:47:00 | AQUA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 77a3c635-3daf-3c71-9bb5-b6235521fd46 | -17.60814 | -51.62547 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 5b3b37bb-3b8b-3c08-b8b1-faf58a7fb513 | -18.12473 | -51.5981 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 4a48cf00-1cd5-3fd3-905d-5fedebbbec24 | -14.92891 | -41.26935 | 2026-08-28 18:47:00 | AQUA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 2958a7af-ba11-3c87-ae7e-34cdd8b19ed8 | -20.57848 | -46.98063 | 2026-08-28 18:47:00 | AQUA_M-T | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2f5a5b30-4be2-3550-a421-8a63a13f1d3f | -20.58828 | -46.97924 | 2026-08-28 18:47:00 | AQUA_M-T | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 575850d0-76c8-3c1c-8c08-e5817ddeade4 | -18.43179 | -39.94859 | 2026-08-28 18:47:00 | AQUA_M-T | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| d66e890e-89b0-3e4f-8add-1f88bf09172f | -17.99877 | -43.95651 | 2026-08-28 18:47:00 | AQUA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b003bbcb-3ae8-3c7b-9ecd-b415acc5b6ad | -14.18444 | -48.76085 | 2026-08-28 18:47:00 | AQUA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| f2962fa7-f362-3a89-9a08-99bf1c2b8ffc | -20.6282 | -52.66535 | 2026-08-28 18:47:00 | AQUA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 82b5fdc4-0a43-38af-9ec0-3af3a294f012 | -17.99739 | -43.94726 | 2026-08-28 18:47:00 | AQUA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2498375d-6b63-3cbe-95d1-8745bd36e54d | -12.7274 | -40.28434 | 2026-08-28 18:47:00 | AQUA_M-T | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| fb6ad702-e3aa-3c86-8db6-ce5a504cce0a | -20.35261 | -46.583 | 2026-08-28 18:47:00 | AQUA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b2f2e894-ca40-32a2-ae11-45f0f3c9a494 | -19.87201 | -40.18018 | 2026-08-28 18:47:00 | AQUA_M-T | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 7a68cf7d-9aaa-3d7d-9d56-eb51a3565ab2 | -14.17442 | -48.76247 | 2026-08-28 18:47:00 | AQUA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| abb2f8fd-23cf-3277-98bd-0bd5203c39bf | -14.3012 | -41.5135 | 2026-08-28 18:47:00 | AQUA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 7ce7e245-e313-3626-8d65-b487808d14ae | -17.94765 | -44.4125 | 2026-08-28 18:47:00 | AQUA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 93e105ab-5ad5-3786-b548-c97d7ad27947 | -14.18318 | -52.85062 | 2026-08-28 18:47:00 | AQUA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 0a5c51fc-be4c-3017-a121-4e524051cc1d | -17.30589 | -46.57676 | 2026-08-28 18:47:00 | AQUA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| fd1bbb83-9550-3989-bed4-5b6d6a7a6083 | -15.73086 | -51.18962 | 2026-08-28 18:47:00 | AQUA_M-T | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| f0d325eb-17b5-33f5-a352-41e90dea9a12 | -14.59964 | -47.9811 | 2026-08-28 18:47:00 | AQUA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 52d77db2-ad38-3d5e-82f6-7516b8c83e08 | -17.949 | -44.42166 | 2026-08-28 18:47:00 | AQUA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 49.0 |
| a2524a3b-a323-304e-90c5-6a13f451e7f0 | -13.60394 | -45.77448 | 2026-08-28 18:47:00 | AQUA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3f7ce405-c4a0-328b-901d-8401a5811f08 | -14.18603 | -48.77291 | 2026-08-28 18:47:00 | AQUA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c2c1d5c3-2418-360d-96e2-e590209dfb4e | -14.59597 | -50.89185 | 2026-08-28 18:47:00 | AQUA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f0cf83e9-2c89-3aba-ad27-7a5577110551 | -13.58639 | -45.77721 | 2026-08-28 18:47:00 | AQUA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |


[Clique aqui para ver as próximas entradas](README162.md)
