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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4254f76b-dd3c-3d20-b180-70cce013ce38 | -10.35845 | -49.92482 | 2025-06-26 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af386025-ea00-3910-ad97-557438b73ca6 | -11.0639 | -46.64741 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b51b10c-bbe3-370b-b287-fffba6a117ab | -9.12373 | -49.44271 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f4085e19-6871-3219-aef3-866859de651b | -11.82638 | -51.26258 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27f079d2-679c-36ae-a7d3-e428e6e767b9 | -10.72177 | -47.51309 | 2025-06-26 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1978198-41ab-3611-bcd9-941b4de87389 | -9.50735 | -56.09467 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 70edcd10-c178-3bbd-9d50-d01c98bf9643 | -8.67743 | -49.95366 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 185a88d5-654e-3b79-aff9-a3228af9a3b5 | -9.79193 | -48.56005 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a329335-b8a2-3f1f-99ba-cec3535ab62a | -11.06898 | -46.63874 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d889568c-774c-3f07-8483-0bad9ba9a41e | -10.24875 | -47.67963 | 2025-06-26 04:40:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0509c59-dfa4-3722-b609-973f40316448 | -12.4947 | -45.90501 | 2025-06-26 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b34e7c2-9bdc-301d-b3b7-c299a45f6e21 | -7.02386 | -44.57162 | 2025-06-26 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4f9073f-b142-37aa-a745-5faff7cce554 | -11.12963 | -46.89202 | 2025-06-26 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 831e14f2-3aeb-3807-894f-0c662cd691a2 | -10.86968 | -53.77694 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0716d4ac-a94e-3b06-82d3-0339a5d1a486 | -11.07022 | -55.37868 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9625f3ab-5ed5-3c2e-a52c-def9a3325320 | -10.65588 | -44.48748 | 2025-06-26 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 528d5155-db2e-32ab-a6bd-247b7bfb1c3a | -9.88204 | -48.05294 | 2025-06-26 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8bc2861-8722-3b0a-8dbb-06cb46fe73ec | -11.80225 | -47.54125 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0a747e9-367b-3388-bcf4-49dcd8f9435f | -6.82818 | -44.81982 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32516fa5-83e8-32e3-9765-50f5f5c30065 | -10.86458 | -53.76303 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54934ae4-1fcc-3dc0-a22a-b4682deb0a75 | -9.17027 | -61.40648 | 2025-06-26 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 430669fa-a301-3c2b-a76c-1ffd98acb7fb | -8.13951 | -46.82756 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef0234f8-97ac-330a-b0c6-e3b246d8e42e | -10.82564 | -53.73058 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7ff5e13-b658-3b01-bee2-14245ad448a3 | -7.87585 | -47.87442 | 2025-06-26 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34054303-5d0d-352e-a252-19a91bab9798 | -6.95615 | -42.80977 | 2025-06-26 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 27eeaa2d-2c84-3032-ba90-17f687609b86 | -10.82785 | -53.73951 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cfee3af-23b7-3c28-98f8-131627d4e46b | -11.82694 | -51.25906 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9611b3df-32ea-3104-8d3a-1a74023357b9 | -9.51822 | -56.10812 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1f2dbaac-e16b-33a1-9b6c-1f750c66eb2a | -13.10076 | -52.29855 | 2025-06-26 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6008da92-8112-33ed-a1fd-38b8436d871a | -12.48315 | -45.89976 | 2025-06-26 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df9a402b-fd05-3b79-a653-0ccdfed8a1aa | -8.70743 | -47.98619 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fecbddbe-1471-3bfc-8c81-155c18994b35 | -10.50754 | -53.59006 | 2025-06-26 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8871e48d-440a-3a13-9514-506e7f52eb25 | -11.79505 | -47.53996 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14bf6b60-0e23-3d1f-9481-9ce132d4341d | -7.20378 | -43.08634 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 07eabf8c-053c-30b2-9777-cca0aab22b98 | -10.82854 | -53.73534 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b7ce0b6-e833-3687-a25e-a00b92ccd5c3 | -7.20828 | -43.08699 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fa9dc91d-8eef-39f7-9874-5c342375aab7 | -9.8741 | -48.36279 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40f002c9-f28c-3f7b-81be-c769d8c2bf37 | -11.80751 | -57.35418 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf0d4b8c-1ea1-32e8-ad4e-5c74d58ca664 | -10.86866 | -54.30453 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95f79ddc-9f92-3ee0-bf81-971b22b9e342 | -9.50313 | -56.09399 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c9f51c6d-e4bc-392b-8bde-625dd432bc71 | -8.07614 | -48.47234 | 2025-06-26 04:40:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ac68026-ae10-3949-b113-f97fe16a1bd7 | -11.77781 | -47.40133 | 2025-06-26 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d75b0122-65e1-3c22-a848-0642a2dc13b9 | -10.52347 | -53.62698 | 2025-06-26 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 539af244-35b7-3696-a35b-d833af89c85e | -6.17944 | -48.07274 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 41f6a4f1-203c-3402-9807-8d647c240b16 | -10.5133 | -47.20147 | 2025-06-26 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6f1c74d6-30de-3224-9f7f-08ed9bffba3e | -9.12319 | -49.44622 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c0716b2d-d58d-3b75-b880-30760411ac38 | -11.60938 | -46.50893 | 2025-06-26 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3e2608fe-a42d-3561-b366-c100f54565e0 | -11.09287 | -46.63304 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f05c92e3-ad41-3ab8-8abb-fce8956ec42f | -9.4947 | -56.09256 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7857a04f-c577-372d-93e7-82b73b615c57 | -11.13027 | -46.88757 | 2025-06-26 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a596364c-8dce-3093-a774-4e82a3f9facb | -10.05964 | -49.65819 | 2025-06-26 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 204a2bbb-47c8-3ebc-b3e4-75b1bee88d73 | -11.95396 | -47.02806 | 2025-06-26 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c19ee0bc-acfc-3d49-8bfd-aae30b3c866c | -10.30068 | -57.13501 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bba6d52-d628-3e9e-bb76-966bc6deace2 | -11.13962 | -53.91925 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bbd69d7-81e9-3b9c-9305-ee33b5882a6e | -11.0663 | -55.37798 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9a3fcc82-a8f1-38e4-9067-e289b50de2c0 | -11.44007 | -54.476 | 2025-06-26 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df838270-7f03-386d-8cf6-db0f6308c683 | -12.65637 | -54.1041 | 2025-06-26 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e28c77a-660c-3ac6-a51a-753f75d4a411 | -9.11154 | -49.43361 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f0815dd-aee5-371a-aeb1-6707f5884d12 | -13.04315 | -48.82323 | 2025-06-26 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89c972e6-c9e2-3bb4-87ff-d36e59d59bed | -12.04957 | -48.07809 | 2025-06-26 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3cec1ef8-c049-3b73-acd6-119bd6083c72 | -11.09664 | -46.63359 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fa60c8d-6e71-3c61-8539-742052e3f70c | -11.06934 | -55.38375 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 46af6aa4-58ef-3b90-a626-f45a4a1debb7 | -9.97262 | -48.24366 | 2025-06-26 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6722810e-2ced-3b57-bdd0-3ff5780d0d11 | -12.02723 | -57.08709 | 2025-06-26 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e11b0ce6-b656-3a83-a8ff-d7f5b8008830 | -10.89054 | -51.62798 | 2025-06-26 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 795f35cf-5738-36ba-a597-36d35587aaa8 | -11.74158 | -54.71439 | 2025-06-26 04:40:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64b897ae-cd6b-3074-9325-9a98907456a4 | -11.13671 | -53.91444 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37a26882-f20a-3ca1-9f2f-e36f3e650b94 | -9.67532 | -48.77193 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ef7693e-b3b9-3b13-81a0-79b9a7f47b35 | -10.3546 | -49.92781 | 2025-06-26 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 852901d9-1f12-36e0-9cc1-207c5e87da69 | -11.23858 | -49.50387 | 2025-06-26 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f92b522-fac1-3a14-8f8e-4abbc777f7af | -10.51208 | -47.2099 | 2025-06-26 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43d59f62-683f-382a-81ca-ffc4a55883cd | -11.43931 | -54.48046 | 2025-06-26 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6187d7d-790d-3957-b3e7-936e3f67e206 | -9.49853 | -56.09663 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7902dad6-e1df-37a4-91ed-48221f6d5504 | -11.05845 | -55.37662 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2ddfff02-db5a-304c-b727-3880f94af7f2 | -10.31853 | -52.56462 | 2025-06-26 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea98b7ca-9849-3119-a07d-aabb968884e4 | -11.10965 | -46.64986 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 898f914b-f5e5-3fcc-94ce-0d8d5318d78d | -11.06326 | -55.37222 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4274a2af-b444-3a7b-ac28-cb887c959102 | -10.55884 | -52.01687 | 2025-06-26 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26bdb9a9-3d23-3657-bed0-0606e69b6c5f | -9.49824 | -56.09726 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 49855384-33d5-36c6-8105-bac88c7435e5 | -6.18116 | -48.08397 | 2025-06-26 04:40:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0b08252b-88dd-3d71-bc24-72b09aebc717 | -12.02861 | -47.77863 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 838cdb2b-44d6-309b-b2fa-adc60c85e76c | -9.24426 | -50.04719 | 2025-06-26 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d37c479-b252-36e3-9e80-0dbee1bdf688 | -11.06686 | -55.06696 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29519081-219b-3a80-b3af-5dbb40a98761 | -11.86924 | -52.25457 | 2025-06-26 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47d34a0e-d6cb-3eb4-b281-4a3635de6373 | -7.10824 | -47.8483 | 2025-06-26 04:40:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc199203-c186-3910-84cf-e6ae0bd9083d | -10.82495 | -53.73474 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09011177-0159-34a8-b346-9993534a6160 | -6.96137 | -42.80581 | 2025-06-26 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0dfc3ded-96e3-3feb-a7d8-52b4079d8a58 | -9.79137 | -48.56376 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76e5b5b8-3e1e-38e4-982b-6e2abb7befee | -9.78686 | -48.57064 | 2025-06-26 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10c46a90-35bf-3287-8ab5-aa274bdf048d | -7.08523 | -49.60511 | 2025-06-26 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 892947f1-93b9-3292-a785-4ec8bad2525e | -10.27359 | -47.6092 | 2025-06-26 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f40f45ed-602c-344e-a728-da70b5562361 | -8.86007 | -50.15657 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0daf5bd9-ca70-39ec-be69-c07e967dc09e | -11.36057 | -48.71068 | 2025-06-26 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| f0ca23db-066b-3f3e-b053-ab4c687c63a3 | -11.93019 | -47.85264 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b8b0e89-ff24-324c-b82d-52d18b89106a | -9.11987 | -49.4457 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 64df84e8-c67c-321e-8e71-51452b49c435 | -11.06238 | -55.37729 | 2025-06-26 04:40:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 70563df2-b007-3769-b89e-cdd3bf6aef24 | -10.47228 | -55.58868 | 2025-06-26 04:40:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52a7cb9e-9981-32d1-898d-f8be6fe427d8 | -9.11486 | -49.43413 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 970de77b-a9c8-372b-8a01-9193d06abc79 | -7.20765 | -43.09151 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a6181459-6148-3621-b7c9-7c6fc5ea32c1 | -11.93494 | -47.84496 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
