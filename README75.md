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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd0d6c6b-f8d3-3e5a-8444-445244b83d01 | -8.10693 | -61.48507 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b41b2130-0ee8-3194-90ed-ab3b1a2f334d | -8.9117 | -60.71747 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de4df0db-bc57-3211-ba1c-43b93643b4cd | -7.25433 | -57.67117 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb7331e5-69d1-3bd4-bb05-ed204e59ea14 | -5.52949 | -60.21103 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b47a8b3-52e6-310f-8472-a8e507f509f2 | -8.59366 | -63.86687 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f70caa45-e00e-3faf-9625-cb4cc6a03bd1 | -6.94631 | -59.56021 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14738d4d-e4ea-396e-9759-5c92a70dfda1 | -6.84585 | -58.96391 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ec3df131-0ccf-3fe9-ab47-f3b60675c9ec | -9.23918 | -60.91288 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23d8ddfd-cbaa-31f1-b3b6-8f43eaf4986a | -9.16622 | -59.55914 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9ea23494-1087-32e3-aa5f-4aa74636e44a | -4.09517 | -55.81015 | 2025-08-27 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05020ce5-53eb-3749-9a82-cf619167b79f | -7.38334 | -64.36248 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 959fd72a-cda9-3e64-b813-7cf56d0a0f42 | -6.81874 | -58.96423 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42e4afbd-5718-39a9-8f10-b8afafa70022 | -9.17369 | -60.76614 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db4a6d2a-1fa7-3658-9e0f-bf7593f0f71a | -8.61715 | -64.0288 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d049d66f-fff8-35d9-a253-e4263c7bf3f5 | -8.89597 | -60.76939 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56399c49-b9e1-3184-b5e2-c0b8ab7a4919 | -9.41547 | -60.5254 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2f08b994-9d20-3e94-a891-ee3ee361d342 | -8.12297 | -62.86846 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9be674ad-8bba-3946-81c9-56e6291be8d7 | -7.1732 | -59.74343 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9dd29d4-733f-3df5-a1f1-84bf79f0f2be | -8.88479 | -62.47314 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c71d36ea-8fb1-3737-ae6e-87a29021ffa5 | -6.35629 | -55.80176 | 2025-08-27 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96c9efd0-ae7e-3bd5-8bef-2cf5cd47be61 | -9.42097 | -60.53306 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47b184b5-6c5b-3b2b-a84d-1217ca4fc5f7 | -7.35873 | -57.62296 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9e9e9e2-1eee-39b2-9d38-b5cf48c277c3 | -7.47847 | -61.36266 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9cc6f93-99b6-34ce-8fcc-b40b4603915e | -8.90102 | -60.76294 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ceeac1c5-8b11-382f-a561-a2b13273040b | -7.16834 | -59.74939 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 194548e4-b0fb-34a9-a409-0b967785f334 | -6.70999 | -58.56306 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80570dbc-0af6-3975-a47e-48a933420457 | -9.16682 | -59.55482 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30a36a64-1b36-3333-9620-8362edae4396 | -7.2592 | -57.67178 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8754a8a-df5e-3686-8b7f-5b946d94c86f | -6.24213 | -60.01403 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8daf4ab-a3de-3048-b028-fc3f6c710ba8 | -8.07775 | -61.53498 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de44c1f6-6fc5-3e98-be46-30d43597077a | -8.85272 | -62.43778 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a17894fb-849a-3d45-aec4-175a4358ffb2 | -9.16042 | -59.53637 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49133a38-af82-31f1-a58e-6f85e505a225 | -7.53984 | -63.48442 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1970d7e4-1ae4-33de-8318-444df57a8a78 | -6.69242 | -58.549 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a8b6e03-ada2-3d05-a452-b71f2bdcf8e0 | -9.26484 | -59.77753 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6abd18e5-e85c-3572-9df8-fd0aaced6e80 | -9.41927 | -60.49934 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ee80ab7-bf9c-3c26-b660-bf4ce2191222 | -7.4711 | -61.33282 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a07b5646-b126-3f03-896c-ccf955878cae | -9.16905 | -60.76834 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7f58d23-18ab-37bd-b4f5-064d7f7ed037 | -9.27287 | -56.91299 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea317cfd-2ef0-303f-aefe-12b8e2d2648f | -9.15077 | -60.78028 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ef97424-99c7-3ffd-9b0c-33af7422a444 | -6.24373 | -60.00334 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2eafe93-aeab-3058-b446-1ab763817806 | -5.74051 | -59.88237 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d26b27aa-9faf-3057-ab31-73416229554d | -5.4507 | -60.15572 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63ad87b3-abb5-3fda-b5ee-c5700c1af9ea | -7.35205 | -59.66691 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ff658ff-bc20-3364-95ae-e2af127239b2 | -6.7937 | -59.63448 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db170887-463b-3499-8a11-f3ffb152d521 | -9.25855 | -56.90421 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebe16df1-693c-352a-8812-3bdb5e111881 | -7.53811 | -61.38115 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac26fa16-3ae6-32ce-b701-916759c49b22 | -7.56385 | -63.84762 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afa904ff-0a92-3b66-a3ec-16c83eda837c | -9.41581 | -60.5399 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11eb940f-e6cd-3029-96d7-8ed9b5325310 | -6.31299 | -59.86713 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00243b6a-d9b5-35cc-8820-0ad2e3aedf9a | -5.80652 | -59.21402 | 2025-08-27 05:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8798150d-b040-3a83-b77e-8f6565894e00 | -7.37773 | -64.35432 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5870c5b-95ec-3fa5-9efc-6a2275832d71 | -8.58221 | -63.9183 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58162731-488f-3845-8488-d24a8cdf3d61 | -9.41788 | -60.525 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ca15e62-55ad-3171-b441-6e2bb4d84b69 | -8.34083 | -62.92842 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b37c5975-dc15-3970-9157-6d8b8dab7451 | -6.95243 | -60.08008 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d879a3bd-73e4-3706-9d0e-27b7fbf992c3 | -6.81937 | -58.95991 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a07e95b1-8a1a-38da-8d9b-61f437a14da4 | -4.11266 | -56.33977 | 2025-08-27 05:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a726bfc-a6a6-3dcc-8698-2868ba8807f8 | -8.89749 | -60.75882 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5790a3b4-6033-3603-960c-bd7e7c898ebd | -7.05016 | -59.82324 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2264ca47-c5c2-3024-ac23-85428c2f44de | -9.59047 | -55.37679 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 453b8a86-5ac0-3c36-8216-2805fdbc406b | -7.47983 | -61.35336 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05a251cb-52f9-33ae-84a0-6ce787a42ac9 | -9.41188 | -60.5211 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1e4281d-f1fc-3dab-b4bf-a5db4e125685 | -8.97289 | -65.42298 | 2025-08-27 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbdc890f-a221-3650-a027-9f48beb583fb | -9.41217 | -62.47946 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d10ee8e-e227-3263-a2a0-44c377d3ab7e | -7.47492 | -61.3334 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79729857-6ba5-3f65-b2c6-1a44dd57b93c | -8.91221 | -60.71391 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ffc1979-37f6-3eb3-94f3-fe4efcc2aee0 | -9.1462 | -60.78324 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d02398b2-63e6-3b6d-9dcb-9f604b1d210b | -3.98213 | -51.0578 | 2025-08-27 05:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec91e347-19a5-305d-942a-65ee2a1f4bb2 | -9.40786 | -62.48322 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7858f77-6c62-346d-920f-7d88188b074e | -8.89295 | -60.76175 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fbfcea9-96b8-3086-9c7c-746a387b511a | -7.16942 | -59.74174 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03d1e221-5634-3485-ba8b-64a0e5530784 | -7.17363 | -59.74242 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04b23797-314a-3bf8-8aac-3552055b62ce | -6.84522 | -58.9682 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 55dd83ed-2bde-3819-8a3a-bb0f6876c945 | -8.57635 | -62.598 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48a11eab-4fe6-33b6-9399-aee380aa437b | -9.17496 | -59.4638 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcb9c774-b96e-375d-9b4b-77cb8ecdb4bd | -7.17896 | -59.73513 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54402a3d-49b5-3a47-bd15-12abef4f74ab | -7.41967 | -60.61864 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f736d3d-6a75-35e1-853f-bbc31af2ba6e | -9.16853 | -60.77192 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39aaa1d4-4bc3-3739-a76b-6761254a285f | -6.68856 | -58.54371 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42d80c77-23d3-3f01-848b-808641b64aaa | -9.40864 | -60.54342 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d59466c2-bd74-3ddb-b462-aa3308ff5556 | -8.96813 | -62.14392 | 2025-08-27 05:44:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4dc451f-e802-3ec8-9e04-0e3e3ced567c | -9.2102 | -59.43774 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b98ea6d3-d08a-3a3e-9c66-4d60ec1f5e54 | -8.89699 | -60.76234 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac0ca260-c2cd-3854-8c5c-a8fceb99196d | -7.62588 | -61.03259 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 131c7440-bea7-30b6-9288-c95e618423d2 | -7.37828 | -64.35076 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0866ec9-52ac-3013-95ec-f336147dde22 | -8.25178 | -63.18613 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f7f4a39-638e-312d-8b94-27559079c792 | -9.40991 | -60.5056 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f361d966-8a00-3743-9206-40717977d617 | -9.57909 | -55.38639 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 662d69de-dca4-35db-b387-74568b2f8f89 | -7.75065 | -61.0805 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4791b588-dfc2-398f-b665-de2e8d583bd5 | -8.95148 | -63.36705 | 2025-08-27 05:44:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b05210a-c3ac-344e-9f6d-9a2f92627ed2 | -7.40626 | -64.34784 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45811596-9d1d-3ad0-a85a-58183f3223d3 | -5.45548 | -60.15115 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82e09904-1b9d-3f52-9422-d0b7ac511aae | -7.62603 | -61.03444 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 82ae4628-4673-3a14-98bc-9d78cb81bc64 | -7.4029 | -64.34731 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0995799-efe8-31e4-9746-d430f702839a | -9.63729 | -59.64174 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2a24d79-34db-3af0-a482-da1cbcfbd3e9 | -7.37718 | -64.35787 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56a4c811-a373-3175-9710-02f9c06379c9 | -9.41797 | -60.53717 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a9d2972-54fd-382b-933c-4da8c3c5335c | -8.86241 | -62.44797 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed81e29d-f06c-3533-9a2d-ce9664a6cd05 | -7.39899 | -64.35035 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README76.md)
