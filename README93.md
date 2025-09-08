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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c553799-4823-3aef-9bd1-279ff66b56ed | -12.35643 | -63.63746 | 2025-09-08 05:44:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72d32526-0355-3d14-a16b-4b3bba3f03b6 | -12.8757 | -62.11289 | 2025-09-08 05:44:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 028a9ac3-e475-38ed-b6cf-6ecfdab06cd2 | -12.63591 | -56.98248 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 669ab0d1-8011-3d56-8e24-29dbb2994ec6 | -15.74546 | -53.59993 | 2025-09-08 05:44:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7682314c-789f-332b-b7ed-6b550359907f | -12.94537 | -54.80629 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c5e5e7d-1a72-3287-ae75-d67e1210bb0a | -12.87177 | -62.11232 | 2025-09-08 05:44:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f4d752b-1877-30f8-918f-8110165d6948 | -12.63569 | -56.98412 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3be90976-bfd5-30a1-a63b-c8fba6101baf | -12.86784 | -62.11175 | 2025-09-08 05:44:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31512ef6-d16a-3bae-a888-11b34d490b60 | -12.939 | -54.80552 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9660fa8d-c700-3105-81d4-8464e00497a6 | -12.94072 | -54.7901 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2363b3c8-3465-37d7-a797-89b6d7a791a9 | -12.93958 | -54.80039 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d25e171-d33a-3c2c-b55f-e432fdbea202 | -12.92856 | -54.78334 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2c78860-4e1c-3a92-be83-6586ea4cc9b1 | -11.79618 | -62.73907 | 2025-09-08 05:44:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b34a5148-e350-316d-a9d8-75ae3c68a237 | -12.93436 | -54.78928 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce0ba2d3-8e7f-3aba-8550-504174ed806d | -12.63082 | -56.97807 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 342d535c-d13b-3349-a488-953a7790a55d | -14.70801 | -60.25236 | 2025-09-08 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8af2ea20-da10-3f65-9468-ccd9348c6fe3 | -12.92914 | -54.77813 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0114564e-a48c-3dfc-92cc-70a9756cbc7a | -14.35385 | -60.31629 | 2025-09-08 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47080f5a-cdd5-3f6d-a0c6-94e67b8d3881 | -12.95584 | -54.7705 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7822096-9002-3422-b499-707ce3008b43 | -12.42033 | -63.89034 | 2025-09-08 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fec14bd-2cc3-338c-b459-a7fcb2fe86af | -11.8965 | -64.98494 | 2025-09-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e39ee98-09fd-3ca7-be74-c824f82f19c9 | -14.34946 | -60.31472 | 2025-09-08 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 403a1c09-b02f-38a5-a3a4-08632dd3444e | -12.94015 | -54.79525 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3dbc3e1-5353-3977-ad8f-aeb0cb0d68a1 | -14.87684 | -55.82294 | 2025-09-08 05:44:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 550ff404-81e1-370e-9164-32f1172909d9 | -10.92602 | -69.19601 | 2025-09-08 05:44:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5e2a308-2a28-3f67-a1ac-d28143f746ce | -14.53327 | -53.98901 | 2025-09-08 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50c75343-3852-3000-9a1f-5348b4249673 | -12.95524 | -54.77587 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91ecbb56-2f1b-3cde-8843-67607d4ebda4 | -12.94766 | -54.78579 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87ca1888-aab0-3f3d-907e-29aeb8f3e172 | -12.41499 | -63.90201 | 2025-09-08 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 565a2404-761a-3af8-850e-392fdfb37013 | -12.63063 | -56.97973 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2d980e15-e567-3d3f-9a38-700602696fe7 | -15.73845 | -53.59884 | 2025-09-08 05:44:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b89f4111-5653-3a32-89c7-0adc13f088e1 | -12.62557 | -56.9753 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 38296422-f87b-36ad-8a00-0fee14f6960a | -11.90328 | -64.98596 | 2025-09-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 960eae9c-c144-3d09-94f1-8568e37d880d | -12.6311 | -56.97597 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f27d182d-c696-3603-8f72-bb987382eb89 | -11.81418 | -61.53588 | 2025-09-08 05:44:00 | NOAA-20 | SÃO FELIPE D'OESTE | RONDÔNIA | Brasil | 1101484 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92e6d030-9e97-3327-a251-36dd6ab85dac | -12.94304 | -54.76933 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1b280df-4394-35d5-b0a8-7ae39de6b3a0 | -12.94594 | -54.80116 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c2ce0243-a9a7-3b4e-9362-e437793e221f | -14.71253 | -60.25326 | 2025-09-08 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22501a60-285b-36bc-ba1c-45b54c2ec478 | -12.61868 | -56.98563 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f14f5a3f-df5a-3188-a6f2-f759a19a6432 | -12.42268 | -63.89901 | 2025-09-08 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e066365-d4bd-3515-ba2a-19976c145397 | -12.94944 | -54.76996 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df1da7b4-dbc8-3ae3-9365-5e1079b81a22 | -12.6297 | -56.98719 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0703e5b6-0a4e-35df-ae7a-ef0b8db73d20 | -12.95114 | -54.81229 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ac42279-54c9-364c-a41b-2f9427ebd437 | -14.87643 | -55.82231 | 2025-09-08 05:44:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 805084b3-a335-3f95-89e7-f26d7aa551b4 | -15.76298 | -53.56657 | 2025-09-08 05:44:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db802faa-c359-3970-82dd-4609e89d164f | -12.95003 | -54.76469 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de87443b-7791-3fa8-af14-8e22a41959ab | -12.6205 | -56.97091 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b48a4ddb-b1d6-3040-99fc-9eb9d0feb1f0 | -12.94651 | -54.79605 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 60c4eb27-ba34-3177-9eff-5bfa26f7a4a3 | -12.63017 | -56.98347 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9bce866-ad85-392a-a027-ae1c799f6e34 | -12.94884 | -54.77528 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4119f247-30c5-3aac-9e18-123e3d2e945c | -15.7684 | -53.56062 | 2025-09-08 05:44:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 366cdf2c-2af7-3110-917d-b874da1cf53e | -12.93667 | -54.76853 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3966f04-c503-317c-a1d7-f5e348980337 | -12.62925 | -56.99088 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0815cc8-e476-3a8b-8cf3-c783a872fef8 | -22.56784 | -54.91686 | 2025-09-08 05:46:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8ce8e106-f1fd-38bb-9796-cc7aad8d72d6 | -22.56738 | -54.92357 | 2025-09-08 05:46:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9a4fadda-9872-30da-ba2e-7a7c51fd05af | -11.4125 | -50.3955 | 2025-09-08 05:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5401b574-e280-3bfc-a3c1-c53e6dd22e2f | -7.3983 | -61.6346 | 2025-09-08 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0f57c0ba-3a04-3e39-9405-548d38b2a2e8 | -11.4318 | -50.3719 | 2025-09-08 05:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b8ef3fe6-ffbe-3e23-abec-390280686db4 | -11.4128 | -50.374 | 2025-09-08 05:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| be55d38b-5612-3628-8667-08ef6927c797 | -7.3983 | -61.6346 | 2025-09-08 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8518b2d0-2f85-3efa-9149-ae129d0edeac | -7.3983 | -61.6346 | 2025-09-08 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 4fc3ad87-206b-300f-805f-2b750d1357b4 | -11.2007 | -54.9992 | 2025-09-08 06:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 88ab2729-c3e2-34a0-8c4b-c578ddeccc5a | -7.3983 | -61.6346 | 2025-09-08 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0cba49b2-4169-3aff-b9c9-755ad5fbc9e8 | -18.1426 | -43.3964 | 2025-09-08 06:30:00 | GOES-19 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 19daa05d-c3c5-301b-9b4e-ebd1f1feb007 | -9.51704 | -70.43208 | 2025-09-08 06:33:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bd6c089-918a-3f6d-91dc-d418b873056a | -9.1342 | -65.95064 | 2025-09-08 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0091451-c3a5-30fc-8f47-6f54758cc348 | -8.36228 | -70.06158 | 2025-09-08 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67beb2ba-657e-3d99-ab0e-428822f979bf | -9.12353 | -65.95618 | 2025-09-08 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fa2da9e-4dee-3bb9-95f3-acc34bbe64e2 | -8.35627 | -70.29107 | 2025-09-08 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8481e90-f800-34a6-8374-4d7b25385652 | -9.13022 | -65.95722 | 2025-09-08 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b79b3ad3-9c61-35cb-946e-64d7a2be9bae | -8.36187 | -70.06463 | 2025-09-08 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41e54001-b110-3ed1-99f5-71bd97797fa1 | -9.13348 | -65.95673 | 2025-09-08 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dff86d10-1d33-334b-b2b9-6b7b36f1f7cc | -9.13099 | -65.95108 | 2025-09-08 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08d4401d-b22d-31eb-bc02-b86f6a40df3c | -8.88202 | -69.34342 | 2025-09-08 06:33:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 075cbee5-5bdc-33d1-ae01-8ffbc920e280 | -8.88156 | -69.34692 | 2025-09-08 06:33:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e38505d-3d2e-32f7-a0eb-9c441c24c364 | -9.13694 | -65.95798 | 2025-09-08 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3c02e46-255e-33fe-bfd8-67ce9723fbe7 | -9.12678 | -65.95578 | 2025-09-08 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1566e4ce-4575-3f4b-b4f0-d8e9b21371ef | -11.8589 | -51.0492 | 2025-09-08 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 00f95b97-3211-3075-ba9e-cc623f33382f | -19.0563 | -49.7472 | 2025-09-08 06:40:00 | GOES-19 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| e75c6806-f6bc-3abb-9bbd-84d5df33f4b8 | -12.9021 | -47.9823 | 2025-09-08 06:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| d622bdae-8ab2-3b7e-a7c8-2040b4358ba9 | -19.0765 | -49.7432 | 2025-09-08 06:40:00 | GOES-19 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| de36c0e2-d3c7-30f3-a2f8-feb5bf1ab28b | -18.1426 | -43.3964 | 2025-09-08 06:40:00 | GOES-19 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7bbfaede-5465-3cf1-a826-2704f2de6d6f | -11.8586 | -51.0705 | 2025-09-08 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 6f3a2fec-5c3f-3827-b466-a53ce48089ea | -18.1434 | -43.3717 | 2025-09-08 06:40:00 | GOES-19 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 93966784-4511-3a7e-a6cc-547348f33922 | -12.9017 | -48.0045 | 2025-09-08 06:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 9351f8d5-f7ff-3986-8a66-722e80eed4d1 | -7.40477 | -61.63503 | 2025-09-08 06:48:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 92f81637-145d-3ddc-806d-86af8c54112e | -7.39721 | -61.62444 | 2025-09-08 06:48:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 627e3137-80eb-39d1-a226-dea7e9aa46da | -6.63073 | -53.35461 | 2025-09-08 06:48:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 226a479d-1b8c-3aa8-ae3f-a488e4aeefeb | -9.16751 | -59.37759 | 2025-09-08 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fb7940d8-44db-3fce-a9cb-ac8850b0131d | -8.88258 | -64.21786 | 2025-09-08 06:48:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a93b423c-2115-312f-b36b-f9a3f713722a | -9.47555 | -60.4867 | 2025-09-08 06:48:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9eceea63-3e3b-3959-9b05-ec0d205a9fbf | -7.39579 | -61.63368 | 2025-09-08 06:48:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 27003998-927e-316b-ace2-de27aa304f3f | -9.44113 | -59.2098 | 2025-09-08 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5d599b11-09d3-3d4a-a03e-324a2b70ea32 | -9.16886 | -59.36827 | 2025-09-08 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| edcc66da-2917-36e7-8818-90c6f66a1ee0 | -8.88311 | -64.21113 | 2025-09-08 06:48:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5aaaea55-fc54-3bd7-b419-0db4c8e6bfdd | -9.44251 | -59.20037 | 2025-09-08 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 70084c6a-5d31-3cef-9c0a-fecef3e50d3e | -9.18246 | -60.76848 | 2025-09-08 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 380ea848-ff80-309d-a2b4-4f6b138d1735 | -7.40618 | -61.62581 | 2025-09-08 06:48:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 2fbca981-61db-3eb2-a69d-47aef5b2ce14 | -7.90116 | -61.77611 | 2025-09-08 06:48:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3518e6f5-8a45-39ca-b9c1-01228016e554 | -11.917 | -50.9787 | 2025-09-08 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |


[Clique aqui para ver as próximas entradas](README94.md)
