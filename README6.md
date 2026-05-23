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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bccedb35-078f-3c40-9808-b2734c8e8fb5 | -12.88937 | -58.19294 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a1302ced-5225-3643-bca9-bad8e0a750e9 | -12.87875 | -58.18834 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 144e47fe-6291-3440-8931-88a96b95cdc9 | -12.89285 | -58.19357 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e351c8d2-5d25-3e65-b15e-e59e3bd23ef7 | -12.89004 | -58.18904 | 2026-05-23 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 52b9d91e-ceb1-35f0-aa5f-9d7e01f7763a | -21.29651 | -56.09985 | 2026-05-23 05:12:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eea7c09e-da43-3513-8311-5cbdcb19ca7f | -15.2283 | -57.6517 | 2026-05-23 05:20:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8c1b66bb-6f42-3ca8-80e9-6b51dbcfe180 | -10.65059 | -49.72301 | 2026-05-23 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f01088d1-3e9d-30f0-b0fb-71c078769b3b | -9.11133 | -50.53554 | 2026-05-23 05:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 793e3362-6ed4-388f-b008-07a116a15767 | -9.14064 | -51.28425 | 2026-05-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06f8613f-e954-35d1-aa3b-9afc5a05c188 | -10.64998 | -49.72804 | 2026-05-23 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a07b7b2d-bdbf-3738-b034-465e4d49df97 | -8.52382 | -54.77172 | 2026-05-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b406d94-90df-30a5-b422-07705b2d74e8 | -8.43518 | -51.55288 | 2026-05-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a381e269-a90e-32a4-a284-8b248d18c24d | -10.37463 | -57.76079 | 2026-05-23 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9bd71cf-b46f-3669-b663-b0c2e7407502 | -8.4347 | -51.55638 | 2026-05-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b56bb0a9-adb2-38d6-80b5-2e857ba5dc29 | -9.13937 | -51.28342 | 2026-05-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6eede17a-9051-3e89-b803-1fb18e744cd1 | -9.11187 | -50.53146 | 2026-05-23 05:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56e9ef25-e99c-307a-b4b5-b51b3f8ecd50 | -9.11076 | -50.53468 | 2026-05-23 05:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ca53de3-39ac-38b6-86e9-808e84f92f17 | -9.11127 | -50.53058 | 2026-05-23 05:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73e7a2b8-c1dd-3604-90f7-92f8eecfa9a3 | -15.09752 | -57.62489 | 2026-05-23 05:27:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1704f97-b6c8-3346-9793-e029b4769aaf | -12.44925 | -54.45073 | 2026-05-23 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a15e0717-34ba-340d-a472-77842403f857 | -12.45002 | -54.45859 | 2026-05-23 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0305e42b-de5d-333f-81e3-c9a77c063bbd | -11.18006 | -55.91656 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f07a405b-6ce9-3e7e-851d-4f2477ead8f9 | -11.44763 | -52.92396 | 2026-05-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ff633fb3-2660-302c-8aee-a38fe082bd1c | -11.45238 | -52.92778 | 2026-05-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a98cceba-99a7-3d6c-9460-1b4463de871e | -12.89366 | -58.18833 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d1213c9-2e7f-3f91-8902-76defeed5e2a | -10.71001 | -56.24302 | 2026-05-23 05:27:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f403885-97a1-307e-8772-5abb3380fe22 | -11.1853 | -55.91695 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ca75577d-5b2d-3a07-b5e2-de50a9dd196d | -12.88687 | -58.18269 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faecb966-36f5-3126-bcef-94f5f176e449 | -12.44786 | -54.46112 | 2026-05-23 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ca4e329-e76e-3ca7-b6c1-1ada4743a65b | -12.89805 | -58.18433 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 646e853e-45ac-330f-aad3-8f8f8d4c21df | -11.51436 | -56.12195 | 2026-05-23 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7bf274e-5916-3823-8ba4-d1afec9a0ada | -11.18481 | -55.91323 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f764aa9b-4c03-3200-b975-fe0f16221652 | -11.79645 | -57.3623 | 2026-05-23 05:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e6133a1-9eb5-3777-87cc-6d3539558094 | -12.45067 | -54.45338 | 2026-05-23 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b40a5f2a-196a-37d9-93a3-bd0c61c23653 | -15.0968 | -57.63015 | 2026-05-23 05:27:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf242e78-7d43-3c25-9531-fd89eb95732d | -10.91485 | -54.11787 | 2026-05-23 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d5807ec-6c7d-3a91-8606-63d7663f48b2 | -12.89497 | -58.17928 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 969552b1-edde-3949-968c-861ce9459517 | -12.88621 | -58.18722 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9a626c7-164f-3e35-81b1-3b722ec518c8 | -11.18057 | -55.92031 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 912a4b36-96dd-3cb5-8838-d513859a5ebd | -11.18111 | -55.91634 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0abe200c-36ad-3213-b333-a0718b712ae7 | -11.51021 | -56.12133 | 2026-05-23 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3466f6e-70c4-3f55-be41-20d0491d176b | -11.7926 | -57.36172 | 2026-05-23 05:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 083fde90-4da4-3687-8d72-e57a99d4d000 | -11.1795 | -55.92051 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 18cafae9-b5eb-3e7f-b37d-2befb0af80c4 | -11.189 | -55.91385 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b181fe70-15d7-31a9-8dfa-2e21ed16519b | -12.89059 | -58.18325 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4f69e1f-cb69-3cda-a711-d45922630f79 | -15.2253 | -57.65561 | 2026-05-23 05:27:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 4fa44797-5bdb-33f9-b82c-036abb04a08e | -11.44207 | -52.92641 | 2026-05-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db816ce5-886b-3d4f-af82-511716983bb2 | -12.1701 | -56.45048 | 2026-05-23 05:27:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 489be5e0-970b-3623-8fe8-851e8a6941e0 | -11.18062 | -55.91261 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b212dd34-fa9b-3888-8dc8-ff429292223d | -12.44662 | -54.44747 | 2026-05-23 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e350a351-170d-3e35-a6a9-a5aa997b0108 | -11.79014 | -57.35136 | 2026-05-23 05:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c544b54-bc38-3d02-9e6b-d8e2e2782dd7 | -11.94621 | -57.04108 | 2026-05-23 05:27:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8e3bcc4-ab91-38ba-b087-1921197f4d91 | -12.89125 | -58.17873 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe20e50d-adac-3d8c-a640-5e9b402e5500 | -11.17588 | -55.9159 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 96c08b9d-c2d5-3a9a-91e1-5f4d53193a2d | -11.44247 | -52.92327 | 2026-05-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a2db5d1-4a9c-34a3-b122-c78d87807beb | -12.44855 | -54.45595 | 2026-05-23 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95e4958f-5670-311d-9843-587e542e6592 | -12.893 | -58.19285 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 065f65d1-2b90-3fdc-9ee0-aee602f7c88e | -15.22205 | -57.64982 | 2026-05-23 05:27:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 109a2870-de2b-386d-b44a-09e4bb16935d | -10.91419 | -54.12287 | 2026-05-23 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a14aed4-9986-36b0-b75c-703d52f98000 | -12.88928 | -58.19232 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 912ed961-30c7-3a34-8b4c-432204a1d8cc | -15.10148 | -57.62547 | 2026-05-23 05:27:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1713477b-ea4d-3600-b760-6b5d870d4423 | -12.8919 | -58.17422 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed201c56-9bfc-33a9-b1e2-1f8cb53cbbb5 | -12.89255 | -58.16972 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 077cf979-2aa8-3df5-a37f-e2ab164a78c2 | -12.88752 | -58.17817 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31ef872f-0d67-326c-954c-ceb4e392a375 | -11.79399 | -57.35197 | 2026-05-23 05:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06ccd821-ca8b-3fbd-b322-8d8467d6c5f7 | -11.18164 | -55.91239 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cce018ba-4b15-3354-a031-229dfa90c5f5 | -15.22133 | -57.65505 | 2026-05-23 05:27:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 7baf098c-4df5-3c22-88b3-2e64995f8bfd | -15.09284 | -57.62957 | 2026-05-23 05:27:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8084ae9b-7f5e-3265-8a52-dfc264ba49b1 | -11.79329 | -57.35685 | 2026-05-23 05:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8db0b19-8d96-3292-a036-51ea4cd3fd2f | -10.71004 | -56.24213 | 2026-05-23 05:27:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a44b320-7121-3ed2-b5f2-1d4b0f111f92 | -11.18425 | -55.91716 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9b5fee19-33e2-338d-b147-22645290c591 | -12.88993 | -58.18778 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa21b904-ac35-376f-822d-c2b31b1b60d3 | -11.44722 | -52.9271 | 2026-05-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 75ca9e52-a3d6-3a78-8cf7-7680f47580f3 | -11.45279 | -52.92465 | 2026-05-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1b4fd721-41fc-314e-9fe2-357a0eaa7d60 | -11.55708 | -56.32757 | 2026-05-23 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21d3a7e9-4698-30f7-b1b5-334416fbc577 | -11.95016 | -57.04163 | 2026-05-23 05:27:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a25487d9-c83e-3944-9c72-e2e0b8fe067c | -11.18583 | -55.91302 | 2026-05-23 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0a8968de-fecd-3f7c-a46c-5c2df206a5f7 | -12.89235 | -58.19738 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9db9e6b-c371-3f28-8620-ab0c92176045 | -11.55628 | -56.3274 | 2026-05-23 05:27:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f34d8f80-bfc4-32e9-a073-e185fd6ed51a | -12.89432 | -58.18381 | 2026-05-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae4277e7-cce1-3800-a94a-d7994ab3ba76 | -11.43691 | -52.92572 | 2026-05-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42026fdd-d276-369f-8bfa-0c8be00392ec | -12.8859 | -58.1891 | 2026-05-23 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 1ba88b14-f711-3fcd-b644-f2ca517a7871 | -15.2283 | -57.6517 | 2026-05-23 05:50:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 79cd6fcf-5393-3e63-a431-97e4c81a46fe | -12.8859 | -58.1891 | 2026-05-23 06:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2b2a0e8c-6453-3eea-8cb0-76df8efb671e | -12.8861 | -58.1692 | 2026-05-23 06:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d800a8ab-4208-3c58-a220-60ed1226ebe1 | -15.2283 | -57.6517 | 2026-05-23 06:10:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 808f08fc-cd1a-3223-9f25-d8f6cf2f70a6 | -12.9049 | -58.1875 | 2026-05-23 06:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 55b4baec-3609-3898-8b66-f826194f853e | -12.8859 | -58.1891 | 2026-05-23 06:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 70e411ee-234d-36b1-bd35-ff966dbad58b | -12.8859 | -58.1891 | 2026-05-23 06:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 61b30a14-321b-327a-a233-cf48d7f7076a | -12.8859 | -58.1891 | 2026-05-23 06:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 9223d6e1-56f8-3e48-a4c0-b0deb5c48650 | -12.9049 | -58.1875 | 2026-05-23 06:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| c868b1b6-9f6b-3f13-94bb-16821596fbf2 | -12.9049 | -58.1875 | 2026-05-23 06:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 21ff0ac2-2a9c-3c5f-a0ce-5e5f8ea611c0 | -12.8861 | -58.1692 | 2026-05-23 06:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 416e64ec-5122-342c-a382-9b1ca1902e12 | -12.8859 | -58.1891 | 2026-05-23 06:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 6755702b-d788-3f07-be48-750fe0c2997c | -12.8859 | -58.1891 | 2026-05-23 07:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| b5408c0c-aa2f-388d-bed6-bad108cd288d | -12.8861 | -58.1692 | 2026-05-23 07:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 4b2e60a1-c195-3f6c-a619-7d781ff63d72 | -11.44863 | -52.92805 | 2026-05-23 07:20:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| fab52fe9-ee96-3fa5-8a9a-9b69c092de0a | -11.18035 | -55.9038 | 2026-05-23 07:20:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 498855ba-ebdb-3180-ad88-5798c98f9454 | -12.88424 | -58.18254 | 2026-05-23 07:20:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 36ba9079-a967-3a0e-9fcf-03f021f91f19 | -12.88575 | -58.17162 | 2026-05-23 07:20:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |


[Clique aqui para ver as próximas entradas](README7.md)
