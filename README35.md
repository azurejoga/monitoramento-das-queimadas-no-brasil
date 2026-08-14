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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a9efcdd-0ee7-387d-959f-0a154504a5c2 | -6.60057 | -56.33266 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11de3cc3-709f-3341-937d-8c21b9fad642 | -6.62308 | -58.99718 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c544126-bfce-35dc-8caf-2b1e1f93e7b5 | -13.27804 | -54.22555 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e728ab51-10f5-3ba8-9cb7-f4e7490df8f3 | -14.07484 | -53.61246 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f03a6702-c8ad-31a1-af1e-f4e0e39e8ae9 | -11.62109 | -55.18501 | 2026-08-14 05:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1f94036-af34-376d-9d79-b3209d30b5c2 | -6.79307 | -58.76174 | 2026-08-14 05:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0556f3da-f04a-3c7e-be47-d06a7c87920a | -6.60491 | -56.34055 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f36e3ecb-f16e-3115-a72e-885c6d92f011 | -6.60542 | -56.33698 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04d7346f-d37d-3a12-8886-f5dd9591c615 | -6.60074 | -56.35316 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b38adb10-cac5-3ce2-bdef-b79afb4cbf59 | -6.62906 | -56.26608 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c8d832b-5f7a-348d-8662-d9a6e6277f00 | -14.05107 | -53.59173 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6dbbe1f5-f23a-3d0e-845b-2f4c953be57f | -13.81988 | -53.79397 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39faf12e-47cd-3ef5-bd2c-14279ef59601 | -6.59763 | -56.35317 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d4911a4-6bc8-3c0b-bdd6-613d1f705e65 | -6.78465 | -58.75574 | 2026-08-14 05:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 633cb208-980f-3a34-98e3-c1f444f81c4d | -10.06547 | -67.55714 | 2026-08-14 05:55:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6ae11b1-012f-3c36-81dc-d4319b192d4a | -6.71107 | -58.94401 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2c9780d-1e57-3fad-83e8-1e914eb7757a | -10.06884 | -67.55769 | 2026-08-14 05:55:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03bd1af4-e54d-3f54-af74-75e0f054faaf | -6.59661 | -56.36026 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5916869-2308-3f5c-83e2-c8c6786bb8b5 | -6.63248 | -56.26355 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70d7794c-1f4d-35d8-802f-e9001f4cb890 | -14.0678 | -53.61208 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a271101c-6db1-39db-8cb1-774245612535 | -16.91286 | -54.15306 | 2026-08-14 05:55:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47dbe3ac-b8f4-332c-991f-50fc80fa122f | -6.62373 | -58.99275 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c78cfe4-fae9-324e-9ae1-b11a6a679c7e | -6.59712 | -56.35669 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58dc321d-e39b-3fa4-a9b3-3e8dd752c7ed | -11.65674 | -60.11887 | 2026-08-14 05:55:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d651409-2395-387d-b226-0836858878ae | -6.62556 | -59.0424 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d436be3-78ac-3740-adc3-737badf04fe5 | -6.60119 | -56.34985 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4709893f-5cbe-312c-9f43-c90e7f314af2 | -6.58929 | -59.01008 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cc919c8-a0ee-311c-9294-ebee1889d699 | -14.30923 | -53.06954 | 2026-08-14 05:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 661ed134-eef9-3148-8ee3-69cdee51bcea | -14.08742 | -53.62763 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2ba033ad-c7b4-3f5d-9009-00899b09a6b1 | -6.61537 | -59.04985 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a81595a4-c6ee-3e9b-8ec3-d7de62d4a54e | -6.59859 | -56.34645 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3ed0cf1-a945-34dc-9304-cf1b18ecaef5 | -6.96452 | -59.29312 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7faf4d40-60c2-3bde-847b-a1ccc0390d93 | -13.81855 | -53.79912 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 100d92ba-249a-3135-8b86-7c65b2ca7a59 | -6.58482 | -59.00944 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 655e02af-514e-36c4-ab92-cb4f9950df3c | -13.42295 | -57.04666 | 2026-08-14 05:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d6f10a4-7545-3f01-a831-718a036a0542 | -6.95693 | -59.28324 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ebb90f7-30a0-3943-bc88-93bdc03eaa84 | -14.07551 | -53.60596 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e9b4f83-fa60-328e-a5f9-3e50402edad7 | -6.60594 | -56.33341 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ebc00eb-a07c-3d03-a778-b59228d1ec9d | -6.60257 | -56.33965 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5538d8e4-b225-3669-9670-5f604c0c71c7 | -6.61474 | -59.05416 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 929574d0-f410-3470-9a79-c463a9f7c5e5 | -7.44988 | -55.30274 | 2026-08-14 05:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56fbc9fd-d5dd-3f5e-8f0c-cfe7d6ca8e0b | -6.96513 | -59.28883 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f3b1072-076c-3165-ae38-5476479e392b | -13.27737 | -54.23166 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 921cdedf-1584-3a32-b1f8-ae89ab1d795d | -15.51056 | -53.00277 | 2026-08-14 05:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 911845d4-3655-3828-ad66-6a72a37d220c | -13.28472 | -54.22645 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28a0dc79-27bb-3e1a-96f9-1d5a902ccab4 | -6.70463 | -58.95692 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4128365-a2d8-31c5-b994-c9f41ec62f6c | -6.63198 | -56.267 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a86e7a3a-d046-3378-af7d-36713084ed48 | -6.61349 | -59.00034 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52668551-1af8-3993-b328-035b4ca8f8fa | -16.90578 | -54.15328 | 2026-08-14 05:55:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5198e8f9-812e-30e5-a3b1-412141a9d931 | -14.04474 | -53.58464 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c6fe3457-f839-3231-b659-f5e0e800cf93 | -14.03477 | -53.58858 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa0a823d-84d4-3be5-b7e3-f775c4e4f21d | -6.616 | -59.04553 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 520f12ab-5793-30a2-9f6a-a4abe109c196 | -14.06851 | -53.60518 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46706f42-6854-37c8-bca9-a0f14b6ecc4b | -6.62046 | -59.04613 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef539f4c-2605-3617-8821-bcf4eed2f07e | -6.59131 | -56.35913 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62cf8e2b-48f8-3e01-b889-e592e9c4763d | -6.62492 | -59.04675 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56381d30-8622-35c5-b04c-f5d491009c38 | -16.91996 | -54.15259 | 2026-08-14 05:55:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8617855-507d-3007-b89b-30b91cd5e72c | -6.59437 | -59.00641 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce978819-ef2a-33b5-896a-10c3c68e65a6 | -6.6089 | -56.33336 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26b4b1bc-9cc3-3140-8ab2-d36850a91306 | -12.51887 | -55.79055 | 2026-08-14 05:55:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2fe77f2-d3ac-30cf-b4b6-5a32732d0e82 | -6.85726 | -58.95851 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d99b1f97-2c5a-3927-9985-38db2f060b5a | -14.07968 | -53.63402 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e2431fd0-64bb-377e-adb5-8d4af4b473f4 | -13.82607 | -53.79399 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 023ec507-e3f4-3021-ad89-c08edad64718 | -6.60107 | -56.32916 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8048e2fe-026e-3a9b-b059-a0b983440c4b | -12.51336 | -55.78524 | 2026-08-14 05:55:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b455a0b-3f8d-38a7-9519-6177c84d42cb | -14.05179 | -53.58506 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91e248cb-f1e1-30de-b0e1-e550de462890 | -16.92047 | -54.14695 | 2026-08-14 05:55:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b00ebff-240e-3a77-b40b-51cac34a613e | -6.61983 | -59.05046 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d1782769-75cf-3db9-81da-aa3c8a574f7c | -15.5116 | -52.99772 | 2026-08-14 05:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3d286993-ab2a-342d-8480-0fbc7721be92 | -6.78145 | -58.74578 | 2026-08-14 05:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c72606b2-bc88-3c99-ba38-c422be381fd5 | -16.90815 | -54.15128 | 2026-08-14 05:55:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 658a6229-ec43-3a81-a6cd-008e0a707651 | -16.90117 | -54.1504 | 2026-08-14 05:55:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1af4e816-365b-3a58-ae28-86a73c490f49 | -6.60305 | -56.33612 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3d634fb-bc70-3bd7-98d8-a7d07a91fdc0 | -6.60353 | -56.33257 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74060e0a-a53f-33f8-8087-046897751954 | -6.61155 | -59.04488 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9c6eabf4-1a75-357d-bb08-7f0dff849d5d | -13.28604 | -54.21446 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d1f28b0-f5a2-38b3-b37c-7f01cef56772 | -13.28539 | -54.22041 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b05e9c48-74ee-3472-85b5-74aaacfe750a | -6.24779 | -55.62083 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5650138-5aee-3c15-9b73-6fd65fd0bd60 | -6.70591 | -58.94801 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d363b9ae-9642-33ac-801e-1cb066024a37 | -16.91341 | -54.147 | 2026-08-14 05:55:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a68c4832-a982-352c-bfa2-0b80c5a4a026 | -6.60742 | -56.34425 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3deab7a-fc6e-3b61-8736-987d9e2d9ca9 | -14.04249 | -53.58237 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 701b6897-d1f6-3e66-80df-d76dea858a54 | -14.04951 | -53.58302 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6b77897d-ad29-3f9b-9adf-a1a4ae8a0754 | -6.58992 | -59.0057 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e96835d-53a9-361b-91eb-360f10e2449e | -10.47733 | -67.81835 | 2026-08-14 05:55:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b8b70c2-2564-3451-a777-b234b9ad4103 | -6.61181 | -56.33063 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4714464-f2b7-31cc-9bb0-9f1e5d2b3e8a | -6.6044 | -56.34408 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f413c2c-85d0-34f6-b5a8-15c3b79ff982 | -14.31645 | -53.0705 | 2026-08-14 05:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df9f6849-ac92-3422-84d7-721a21f94572 | -6.61665 | -59.04114 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58f8bf38-097e-3112-9ee0-ae5c39b16b4f | -6.61861 | -58.99658 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 871ad20d-cac1-3006-b73b-474dcdd5474f | -16.91524 | -54.15095 | 2026-08-14 05:55:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0dba3368-5957-3379-acf1-3a16fc1e99aa | -6.79342 | -58.75909 | 2026-08-14 05:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a4c6448-1edd-3c77-8858-987b744aaad0 | -14.04548 | -53.57777 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cb4a6a3d-4971-38bf-ba99-e082de1ae234 | -6.96574 | -59.28454 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f475a61-740d-3d96-be07-26a2e7df3fea | -12.5181 | -55.78719 | 2026-08-14 05:55:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c389e701-f053-377f-a033-7fad170baee1 | -6.78601 | -58.74645 | 2026-08-14 05:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cab7fce-d4d9-3b69-b4e8-4397d7b87112 | -13.90477 | -53.77774 | 2026-08-14 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5f74f55-6ee1-3dd9-8c26-3471fcb2fdaa | -6.61092 | -59.04922 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6e2b67d0-f449-3e9c-905e-154e7fa63336 | -6.832 | -56.42019 | 2026-08-14 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa42bb37-ce0e-3404-86c9-e78d255262cd | -6.95511 | -59.29604 | 2026-08-14 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
