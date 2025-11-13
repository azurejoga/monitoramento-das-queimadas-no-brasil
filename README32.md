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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f806907b-10af-3434-acd5-d32b01d16fbf | -11.73671 | -48.53364 | 2025-11-13 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1ac8b8f-a89a-3656-a935-75e428700969 | -10.37052 | -45.05359 | 2025-11-13 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d55ceb3-e7dc-3a03-8eb2-60ba9242e7c4 | -8.72566 | -49.59683 | 2025-11-13 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e82a3e4d-d690-3139-9a89-76ee667e57ff | -10.62048 | -45.24548 | 2025-11-13 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19803c66-9e5d-3e55-9f00-8acba2176a0c | -12.04179 | -43.51387 | 2025-11-13 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31668c16-0397-3886-93d5-4e5787824d9d | -8.94384 | -49.82446 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e468845-8a30-309a-aa0f-168fdf051a5a | -8.20899 | -47.88259 | 2025-11-13 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22aab0bf-ec1a-38ac-b065-4b284dfba559 | -9.06147 | -48.83059 | 2025-11-13 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 043d31b0-ee05-3207-9a4b-6857a40894e0 | -10.35375 | -47.70155 | 2025-11-13 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec8bf4cf-83a0-3c85-bc3a-97faec4bd8b5 | -8.8688 | -50.19147 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 579460a2-f5b7-36ad-8e7c-5c5673137d3a | -11.81266 | -44.25521 | 2025-11-13 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bd5e463-0d9b-37bb-8a56-c52d64ea9e3b | -9.66847 | -43.89853 | 2025-11-13 04:44:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f19a341f-3a47-30fe-b502-ec0fdb9c9574 | -11.59498 | -45.11202 | 2025-11-13 04:44:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b042280c-2f38-3c8b-9e36-43383feb3276 | -8.25373 | -44.3685 | 2025-11-13 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d51b42b-13fc-3943-99ef-7bf30f1a9f0a | -10.16159 | -46.56654 | 2025-11-13 04:44:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eee273f6-a9c7-39a4-86a6-92c2e701c557 | -15.62697 | -46.50928 | 2025-11-13 04:46:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a06e61dd-b84b-3e52-bef4-971eca399f98 | -22.46453 | -44.20618 | 2025-11-13 04:46:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a5da7328-0560-387c-88a3-e4c6ebac3a56 | -21.03814 | -48.52104 | 2025-11-13 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| ab1a8823-4aca-3988-a3d1-315c6ac0985a | -17.55882 | -54.01893 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fad88fdf-d3c0-305a-9bbd-93bde5e5324b | -17.31865 | -46.49818 | 2025-11-13 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc4e3040-6811-353f-aaa9-17ece6ffda0d | -15.22419 | -51.12396 | 2025-11-13 04:46:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15e90888-109f-3d59-9734-5b5ab4989ba6 | -16.53049 | -52.7736 | 2025-11-13 04:46:00 | NPP-375D | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d34bcf5-e372-3f44-8f82-94047ce308f1 | -22.21619 | -46.75095 | 2025-11-13 04:46:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5bbccddf-8810-3d41-8bdc-e546518019d5 | -17.53261 | -53.714 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5627e4de-f103-38b0-be04-aee6907e68ef | -20.73993 | -55.70071 | 2025-11-13 04:46:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67e4b00a-a43f-3c38-ad14-0e1fcf0b444e | -17.03384 | -46.75772 | 2025-11-13 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1eba414-40b1-37d1-9b43-29cae148fc26 | -17.56159 | -54.02348 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4923845-d50b-3ba4-96bf-a803192f28c3 | -17.56224 | -54.01958 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3eb92cf5-170b-3edc-b1ec-d510a01e316e | -15.49342 | -52.80436 | 2025-11-13 04:46:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91803b4b-e1e3-3c06-9559-c29e99df4df6 | -22.02094 | -44.2479 | 2025-11-13 04:46:00 | NPP-375D | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4fcb3c0-99ee-3b41-8e52-de4b91af2a46 | -22.73645 | -44.84478 | 2025-11-13 04:46:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 03f3104b-9823-30e2-8101-2dee073b6933 | -22.64795 | -44.92223 | 2025-11-13 04:46:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 274ff740-b7b6-3795-bedc-b8cee78e1d70 | -22.46518 | -44.19997 | 2025-11-13 04:46:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 01fcc266-e97f-38f0-88bf-7bf7d77c2da9 | -17.96256 | -47.25003 | 2025-11-13 04:46:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 215f77c4-4838-31fe-8648-356599874db7 | -17.02979 | -46.75718 | 2025-11-13 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 12fb19f7-c091-3a71-8ff5-717a182fb91a | -17.53941 | -53.71523 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20792fa0-e219-342d-ac2c-f043ee597383 | -17.53665 | -53.71078 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4322632-3ee2-3e22-b961-43aaac6bcd54 | -22.02602 | -44.24858 | 2025-11-13 04:46:00 | NPP-375D | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9c10a07e-edd6-3981-8f8d-25f6c7a7bcfe | -21.03231 | -48.52382 | 2025-11-13 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4c978653-1324-3735-9e62-49eec2a8a439 | -15.49679 | -52.80495 | 2025-11-13 04:46:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 637e57f0-3568-3e1e-85b6-aec076a6bdda | -16.4477 | -45.00367 | 2025-11-13 04:46:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8967523-ccdb-304f-a4a0-908cfc66622c | -14.67645 | -51.89128 | 2025-11-13 04:46:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44e37e39-1008-3db2-a1da-b018a07a6d12 | -17.28514 | -54.88169 | 2025-11-13 04:46:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82955109-2d02-3c5f-b47a-435e58e59319 | -22.02127 | -44.24472 | 2025-11-13 04:46:00 | NPP-375D | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 54e9c50d-2c69-3b4f-96a2-f8357729e177 | -16.44989 | -45.00677 | 2025-11-13 04:46:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69a89f8f-d26f-388a-8b4f-222257ceccbb | -17.21165 | -47.65477 | 2025-11-13 04:46:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8483212e-e6a7-3d72-a164-012af4955c58 | -19.59115 | -45.39902 | 2025-11-13 04:46:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bf466e3-b6a3-3ec7-9681-581020dfbe89 | -17.55474 | -54.02219 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 059c1d3c-76e5-3ae5-bb1e-e9a46167a274 | -16.90026 | -51.56628 | 2025-11-13 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af9405d5-f10f-3648-9b75-029af58e87e8 | -21.03749 | -48.52603 | 2025-11-13 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f60d9c98-0376-3d6f-8013-0b30c293357b | -17.76427 | -44.57175 | 2025-11-13 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2f0b827-a2c9-3d17-b0d5-7e54ba4d5bac | -15.4299 | -52.19078 | 2025-11-13 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1543e28-ca88-3b11-a8e5-e2cc3683b1ee | -17.32278 | -46.49877 | 2025-11-13 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2054a679-f5d1-3428-9a30-185218a9735f | -22.46485 | -44.20309 | 2025-11-13 04:46:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 60eca508-ce7c-39da-8ed4-b5f7112423c7 | -18.02289 | -51.0346 | 2025-11-13 04:46:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ed32acf-2c26-33fc-ad12-e511bc302706 | -17.96655 | -47.2505 | 2025-11-13 04:46:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5234883e-49ac-3154-8528-61854ed64e70 | -17.76297 | -44.57021 | 2025-11-13 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c01ddf71-a5f8-3c1a-b239-b3d25756881d | -16.4454 | -45.00608 | 2025-11-13 04:46:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c385978a-e744-3724-87b6-3f144ca62eaa | -22.21672 | -46.74657 | 2025-11-13 04:46:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0b52e599-2951-3ba7-b766-4969101cb63c | -16.84046 | -46.07539 | 2025-11-13 04:46:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc7745d8-4b68-3ad0-9104-add189897640 | -21.0343 | -48.5205 | 2025-11-13 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| b8a3188f-49f4-3ca6-919b-87c6718adc36 | -17.32037 | -46.49845 | 2025-11-13 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15359c50-9d8c-3355-9923-3e68e034b0db | -14.86799 | -52.86509 | 2025-11-13 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c300e273-a9c5-3e81-a24c-f7b1279f113e | -17.96417 | -47.2514 | 2025-11-13 04:46:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05981fba-337d-3bbe-b8b3-cce8b276aac2 | -16.8861 | -51.65651 | 2025-11-13 04:46:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c8b01b33-13d4-3bc8-9142-eb323086c660 | -17.55539 | -54.01829 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59bbd6ee-dca3-3162-9ece-0993b90037ff | -16.89637 | -51.56934 | 2025-11-13 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 226f67a1-0462-3b10-90c6-8684e9ff352b | -17.53601 | -53.71461 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 558a67c3-f5b8-37c4-9f84-232eaea5bb9f | -22.73102 | -44.84902 | 2025-11-13 04:46:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e28a3bc4-9e99-32c3-bf9c-debac75b3218 | -17.62634 | -49.33598 | 2025-11-13 04:46:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76c19c6f-d84c-3784-9dd2-ce964ba9d55c | -16.84078 | -46.07613 | 2025-11-13 04:46:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50afa2e6-85a9-3351-aeb5-77c8278e18ef | -17.53538 | -53.71844 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d22b611d-31eb-3ef0-8bc9-38bf96e70086 | -18.16813 | -41.30306 | 2025-11-13 04:46:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 204dead2-8f8d-3f85-b1db-8aa300e0d2d8 | -18.16763 | -41.30805 | 2025-11-13 04:46:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 56ed4fbc-6b0e-3bed-95dd-60281d4f28d4 | -22.46968 | -44.20668 | 2025-11-13 04:46:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9a059477-d5cc-3b13-a289-5f1557948ee7 | -22.73602 | -44.84455 | 2025-11-13 04:46:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 30e8beb3-3d01-3568-8c8d-3dee2297e801 | -22.73541 | -44.8502 | 2025-11-13 04:46:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 1633eb11-c0db-30b2-a753-2d032fc9d863 | -14.86868 | -52.86528 | 2025-11-13 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bafed37-17e5-34f7-bf17-0dc39ebb9c35 | -21.03299 | -48.51884 | 2025-11-13 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d650657a-5346-3417-ab74-f1ceb94c0258 | -16.54111 | -52.60295 | 2025-11-13 04:46:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22e201dc-5be7-304f-b38c-fc79eef06b6f | -22.21332 | -46.74835 | 2025-11-13 04:46:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8bb5909b-bcef-37fb-9981-b7027a7c5662 | -22.47001 | -44.20359 | 2025-11-13 04:46:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6026916e-e3d6-36de-afaa-4a3661571fea | -16.44715 | -45.00822 | 2025-11-13 04:46:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d80009f-2e12-36f8-b7a0-3444af4977fb | -17.55817 | -54.02283 | 2025-11-13 04:46:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cda450d-264a-33fe-ad5c-08b86fe2e28c | -22.21768 | -46.7488 | 2025-11-13 04:46:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0ef12540-3b04-355a-8ed2-5da52e89a90c | -14.67978 | -51.89185 | 2025-11-13 04:46:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a6b0dc7-3635-3240-a19e-736759f80844 | -14.67255 | -51.89431 | 2025-11-13 04:46:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f72b81c-5bba-3182-b9fb-765f699fa226 | -18.24745 | -51.27238 | 2025-11-13 04:46:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6f787c21-95b1-301c-9a2b-20a66f665466 | -22.73588 | -44.85045 | 2025-11-13 04:46:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 3606fd86-1c34-349e-b29e-a95f5292b08c | -4.7204 | -46.4497 | 2025-11-13 04:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d78acc56-fdf8-3dab-ad41-2971e8bb4759 | -3.0916 | -49.2759 | 2025-11-13 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 0ddf2dcd-f33d-3baf-99d5-3d5515d2fada | -12.6557 | -46.7407 | 2025-11-13 04:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 857f10e0-d25b-30eb-a311-0f404532d5d2 | -4.7206 | -46.4276 | 2025-11-13 04:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| a557ff3f-5aa0-3f8c-901c-ef282e2519e1 | -4.2056 | -48.5706 | 2025-11-13 04:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 4a61c678-885e-3dc8-a2d9-0d882ca12c28 | -4.7204 | -46.4497 | 2025-11-13 05:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 60bea064-d759-3c05-a9ce-550a21c30e6a | -4.2056 | -48.5706 | 2025-11-13 05:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 27ed47c9-1790-3ef9-b214-4a70e2cc088d | -12.6557 | -46.7407 | 2025-11-13 05:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 00801ff1-f34e-302e-8ad5-743ff9a339d2 | -3.0916 | -49.2759 | 2025-11-13 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 2ea3ee98-aee9-3e21-9cff-156500ec8584 | -5.8403 | -38.358 | 2025-11-13 05:00:00 | GOES-19 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 64.6 |
| efe3f93a-a25c-38f6-9c74-aa34b46b56cb | -4.7018 | -46.4508 | 2025-11-13 05:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |


[Clique aqui para ver as próximas entradas](README33.md)
