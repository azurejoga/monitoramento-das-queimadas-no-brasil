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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de3cde42-ebc7-3264-a249-cdb7bdc04e18 | -10.25634 | -45.81871 | 2026-08-09 05:12:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04ccb35e-b8ba-3c7d-8031-0a0dd475198b | -8.64067 | -66.53037 | 2026-08-09 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1fd2a87-c5fc-3ceb-b783-c640095e229c | -11.09946 | -62.36116 | 2026-08-09 05:12:00 | NOAA-21 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd02e187-da8f-3f47-9dcf-734de7dc8b4b | -8.69018 | -62.87199 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75253bbb-38fe-38b0-ba44-4766c0e8ba6d | -11.17163 | -54.81361 | 2026-08-09 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e6004b6-7077-3694-b00e-92adbb5f675a | -8.78736 | -64.21278 | 2026-08-09 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a33af310-551f-3a9e-b75e-9ac07e0dfe9e | -12.35361 | -53.16136 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1aedfcbc-ef5c-3fd4-bc00-5352cbf7fa83 | -12.33254 | -53.14817 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8999a231-e22a-3731-ae05-90ee0b436982 | -10.92576 | -57.11977 | 2026-08-09 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eab53ab6-3816-3bbb-8de4-dd75174520c2 | -11.24924 | -54.03282 | 2026-08-09 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91efe69a-7fde-3dc6-8c99-ae3f7f79b573 | -8.63503 | -66.53252 | 2026-08-09 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7562201d-cccd-3acc-a032-0d15ac764a33 | -8.63557 | -66.52948 | 2026-08-09 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d00907a-5c38-33d4-978a-2477cc0c4f09 | -10.25052 | -45.81152 | 2026-08-09 05:12:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31bd6c94-16f6-32de-8a5c-f83111d8f3e2 | -10.08018 | -60.50169 | 2026-08-09 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31412585-563f-33ed-bad7-af2cf23d5a70 | -11.62575 | -51.09644 | 2026-08-09 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 922a6c51-066e-306d-a0c9-9dc7daf6e071 | -8.6862 | -62.87132 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1817490-649e-3051-8146-495865344087 | -10.05944 | -60.49831 | 2026-08-09 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 409aaf75-439f-3ced-814e-7e42ec2c3f83 | -10.24994 | -45.81636 | 2026-08-09 05:12:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80e3f8d5-8f10-3121-8371-de926821f926 | -12.34628 | -53.1524 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6986f27a-9408-3892-889a-780279e2ea32 | -10.91849 | -57.12236 | 2026-08-09 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c83a6057-7022-33f3-884e-9cf9878d3fbe | -8.6762 | -62.86858 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b5e046c-16ed-3d24-94e3-f381610841f0 | -10.12717 | -59.47691 | 2026-08-09 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75979b93-360a-354a-8cdf-f2085db14607 | -8.67961 | -62.8727 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7087d60b-dd4e-3288-9a2a-df2ad8da1577 | -8.68161 | -62.87413 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4d2b4783-acb9-3762-8c35-a36c33ef0ad8 | -9.14644 | -59.65263 | 2026-08-09 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 389149c0-f546-3269-b6e7-9770d0c37a96 | -6.13943 | -57.71791 | 2026-08-09 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f5a408c7-eaf7-3fa1-9124-0dfac99f528a | -6.84209 | -58.9758 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c08ecd2f-e24e-33e0-a0bb-d13d0a5c7947 | -6.64541 | -56.43186 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| beb28fe2-30cc-33b0-af93-2dfcaef80980 | -6.84989 | -56.40558 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| db98d0b2-d0c0-3f39-bdae-f89541a67f8b | -7.39201 | -59.97161 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0dba2c5-72b9-31d9-8026-7cd5bdd35f43 | -6.8902 | -59.89708 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c95e776-17f1-3ae6-bd5a-f24990401966 | -6.61393 | -56.34739 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 839bc847-b8b8-3ec2-be70-5a0c40533955 | -6.87032 | -58.92862 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f9f34f9-2c8d-3ed6-bd4c-aa4f2e68a757 | -6.64821 | -56.43588 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f020c06a-8243-3a13-a68c-6ded29bc6ec1 | -6.87648 | -58.93328 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 684eea4c-138d-3972-ba35-5ad4709bc2de | -6.64875 | -56.43235 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23032546-ffc0-3a02-9a96-6d4118a5d3d4 | -6.60345 | -56.37114 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 864b811a-384d-3d95-93d4-f779f2d39565 | -6.82322 | -56.42321 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff743eee-fe3b-352d-b56c-043c108d409c | -6.83216 | -56.43185 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f772ab8-f1d6-36c7-ac68-998cc8f7e3dc | -6.60734 | -56.36809 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c015cf47-2c9a-3420-89f3-8d2dd3b0494e | -6.85379 | -56.40254 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94624512-f05b-3a5d-a891-976431ae29e5 | -6.88321 | -58.93436 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75d5ecf7-46e5-35e1-8c9d-da8cf749fc31 | -7.38631 | -59.96284 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ae64bd0-6a0d-3043-84b3-905e453b2e18 | -8.15642 | -55.39523 | 2026-08-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10a1ed13-a8d9-369b-8889-bf8d5b4282ca | -6.70896 | -58.95492 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 790bbf52-9115-3dd1-ab2d-80bc73d6f0f9 | -6.65203 | -56.41116 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd0114e4-684a-3742-8978-4670e33ee23d | -6.84328 | -56.42633 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4a36db87-6f5a-309d-8c19-20b3cc217eef | -6.84935 | -56.40911 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87a85182-1bdd-3737-9a25-5c8a61bf16da | -6.85044 | -56.40203 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 46bb1345-eabe-325e-9159-cd9d3b7c04b3 | -6.83774 | -58.93824 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10a426c9-007b-348e-83be-37eeec0e8782 | -6.8787 | -58.94101 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 703bcd1a-5b7d-3766-9fd8-58d7ef123a3e | -6.85823 | -56.39591 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a286c106-4d27-39f5-8311-19c3ff0748ac | -6.60399 | -56.36761 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 222d384f-f895-35b3-ba02-f65a3a1466b1 | -7.55255 | -61.16536 | 2026-08-09 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc85a50a-c3af-317a-8d42-58fb3fc8b9b9 | -6.81988 | -56.42269 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6fc0f89-ba0c-3b36-98a5-ffa80551779d | -6.84484 | -56.39389 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 502156c6-be6d-3253-a9db-e36bf1eafafd | -6.82439 | -56.43789 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9ca1929-4d4d-3372-b487-8cecfb12a7a8 | -6.82105 | -56.43738 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4e58936-02fd-362a-98e0-11b75765013b | -6.58522 | -56.53439 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a93e176-768f-34ee-bd15-cb9bbae8a18d | -6.64595 | -56.42833 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e240834-63bf-3197-b553-1e650202cc33 | -6.84655 | -56.40506 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 16d86aa1-1893-3410-8c19-7e00db29ddd7 | -7.55253 | -61.16389 | 2026-08-09 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71d63457-5c8c-3c8b-9dd0-636522e9318a | -6.14295 | -57.71916 | 2026-08-09 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4e1ef22b-85af-3fe0-adc8-c3ca7e67c6b7 | -6.88958 | -59.90094 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d41cb9f5-23c6-3072-b73f-5eb71c26d860 | -8.15526 | -55.40303 | 2026-08-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e948bcf-40e9-3309-97da-bae9b784bd6c | -6.82159 | -56.43384 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a94d4f91-cdfc-3e10-b838-0125931a39fe | -6.82765 | -56.41664 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76bf90ba-f9d1-3e73-b348-03ead219b729 | -6.88715 | -58.93131 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5acb9328-461a-39f0-8ce8-666c8f6aca6b | -6.70783 | -58.9506 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4c1001f-ffac-3d8f-8ae7-35299b000e68 | -7.84714 | -56.5913 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8e37d53-5feb-36ac-969c-b1a841098960 | -6.82719 | -56.44196 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3e16b6c-204c-388d-b6c5-b413f5e3dff6 | -6.82773 | -56.43842 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53200adb-e378-3b23-81a4-b9889c615b6a | -6.84048 | -56.42228 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4908d95-1f2d-3bfe-864e-7a4e071c5e43 | -7.3914 | -59.97545 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30900981-cd5e-36ca-8b46-d3f8d1d821ab | -6.13775 | -57.70702 | 2026-08-09 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 208954f6-8509-3dbb-93d8-19d80372d9d6 | -6.83939 | -56.42935 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df68f9fc-d6ba-3dc2-abbd-fedd712c92b2 | -7.08118 | -56.95561 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 293cbab8-e514-3e8c-9941-751aff5cb937 | -6.84709 | -56.40152 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9d24f3e-b24b-3b89-a416-d02b1449ecb0 | -6.82493 | -56.43436 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21a55ebd-fbd2-3bee-995c-c8ab0bc363fd | -6.88658 | -58.93489 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3a625da-f162-374c-9fd6-95417700e9e9 | -6.72032 | -58.92719 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72f635a9-730a-3ad6-a776-b9b5077dd458 | -6.70669 | -58.95781 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c91f741-99b9-3607-bbe1-29a5a8257d58 | -6.81879 | -56.42978 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9822ecfc-ea65-3b15-bd30-b942159dca99 | -6.85488 | -56.39541 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b705f090-e8e8-3556-aaab-6b427acfde8a | -6.14241 | -57.72262 | 2026-08-09 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 323185ca-f230-3701-8741-f86d7c74a027 | -6.84539 | -56.39032 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98b86f00-aaab-3473-ad94-c3fc26cd5e04 | -6.83768 | -56.41821 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8509d4f3-55b3-3256-a1bc-5036b4f74458 | -6.8415 | -56.39336 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee64e3be-4248-352a-bbe6-2dfe6bdde07c | -6.83434 | -56.41769 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 44be8be7-12e3-327c-9e5d-b6451f557e7d | -6.85636 | -57.65799 | 2026-08-09 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92774616-6e4e-3ebc-bc9c-faf1e52aa0e8 | -6.85269 | -56.40963 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad9eb559-73f5-39e0-a7df-48a0676b9a95 | -6.8355 | -56.43237 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10437d3c-d284-35d8-928d-64bff93cca15 | -6.88994 | -58.93544 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 085bc7a5-3c8c-309f-a95e-fff39430c1f0 | -6.13721 | -57.71048 | 2026-08-09 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42043fff-a193-354b-85d0-b2a4ab366d4a | -6.14572 | -57.72314 | 2026-08-09 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59c90ad4-83a2-3a74-99ab-9df152406f81 | -6.85768 | -56.39948 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2b75b1c-cd43-372e-8d16-5fdfcf32a29e | -6.82936 | -56.42778 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 384f4949-1244-35ac-8082-c025c38e707e | -6.83823 | -56.41466 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 50d66f12-03a0-33eb-9e20-725f49c6c1dc | -6.8443 | -56.39744 | 2026-08-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f95a2efe-65ca-336c-920c-3d296eede653 | -6.83273 | -58.9264 | 2026-08-09 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README18.md)
