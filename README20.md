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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0b7755a-f697-374a-a4b0-12f2f26b7341 | -12.17161 | -59.7556 | 2026-06-27 05:53:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f83d515-14a7-33da-b827-a6ecdb35bf3f | -13.66631 | -53.94318 | 2026-06-27 05:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0ba03da0-dfaa-320a-9065-0ea516112ab5 | -12.46417 | -58.48995 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef28a91d-0bd2-3a7e-9c50-efa8d57c6eec | -13.65958 | -53.94293 | 2026-06-27 05:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d79d1a04-5379-3e7b-a868-b616ed5de579 | -12.45872 | -58.49217 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 3bc89fe8-9da2-3710-bb30-b4afec562d23 | -12.46341 | -58.49579 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 1f5eac5b-2d6c-3eb0-8ddf-e55f06096fba | -13.64743 | -55.29432 | 2026-06-27 05:53:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab409c66-7d89-35e7-8f52-49eb355be8cc | -12.77311 | -59.00993 | 2026-06-27 05:53:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f6861c8-dd4e-30f5-84d2-038197041d17 | -13.66714 | -53.93737 | 2026-06-27 05:53:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 709990a2-a01a-37ae-93dd-1135c33eeaef | -12.45948 | -58.48629 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4eea1c3c-f858-3a5e-99ae-8e61f6c5cbdb | -12.94197 | -56.64994 | 2026-06-27 05:53:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ba8a834-ba2d-33d1-bd3b-f00e999ce8fb | -11.9084 | -57.4174 | 2026-06-27 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6175fc8e-16cf-384b-8f11-8a4bc5b1a92e | -12.62566 | -57.88715 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1124e3fb-a1de-3efd-9a29-98fb0da0abe6 | -12.62444 | -57.89685 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3305772c-af1d-3fd4-b70c-03a2d1810c62 | -12.60978 | -57.88493 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3d71991b-46fe-3a0b-9b91-15d39d4a9ebe | -12.4529 | -58.49728 | 2026-06-27 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64fd6ee7-2e58-3b32-b5d4-1f7c5f75e4b1 | -12.62404 | -57.90005 | 2026-06-27 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 78026192-a63e-3b50-9c1f-3aee124de325 | -10.01804 | -59.35074 | 2026-06-27 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c3e191c-dd74-3a78-a94c-923da521770d | -9.02817 | -59.54235 | 2026-06-27 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db4c4064-84ec-37c7-8302-427c43d70ae9 | -10.30369 | -57.14526 | 2026-06-27 05:55:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a54068ec-ed52-3d1b-81aa-79312c2bc967 | -10.54197 | -53.71836 | 2026-06-27 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 218f14e6-b8f2-363c-b450-7712b608c830 | -10.39143 | -56.72467 | 2026-06-27 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3efe6efc-8cb4-3b3b-a2a4-9c294b1d361d | -11.66427 | -57.26117 | 2026-06-27 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f69c82db-97ac-3254-a5b2-7a0f1495d246 | -10.7888 | -56.75911 | 2026-06-27 05:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d281e13-5073-3baa-b059-7685c00a4192 | -11.32294 | -54.47339 | 2026-06-27 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4673acf8-76cb-30fe-adf8-2b19c10a9176 | -10.38627 | -56.72082 | 2026-06-27 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50fd3feb-cbaa-3c1a-9873-1dd51cd6f526 | -10.7837 | -56.75453 | 2026-06-27 05:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c66086-ee4d-3863-ab53-ceb92adb521c | -9.03057 | -61.33677 | 2026-06-27 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13164257-ab4f-30e4-8757-3c54c51b3904 | -9.59492 | -56.9296 | 2026-06-27 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea334972-0db9-3538-8db4-91c6372cc074 | -21.75352 | -56.26395 | 2026-06-27 05:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05e8d3cf-6ec8-3252-8ea2-f3d6fbb16b0d | -10.90013 | -56.85632 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30cb6a58-c35f-3b69-9d37-4ab9c8f9c9a9 | -10.78561 | -56.75448 | 2026-06-27 05:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36cd6bfa-0780-3820-a7f1-f6ccfa6322e1 | -10.79019 | -56.76276 | 2026-06-27 05:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0fc5b3d-fdab-3b4d-92c0-f0f3e5d1b918 | -10.53749 | -53.71751 | 2026-06-27 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81c0aacd-54d8-3d34-a119-88abea155efd | -11.65884 | -57.26035 | 2026-06-27 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b89e7a1b-b65d-3e25-845b-f56ad9e68346 | -10.89968 | -56.85996 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2630e529-65d2-3796-af29-e0cc8c92beb0 | -9.59385 | -56.92325 | 2026-06-27 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e990cbe-88f5-35d9-98e0-9d35b7c5ddbd | -10.9339 | -56.8566 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fff5d030-0bdf-31c6-b157-256237c567f9 | -11.64693 | -54.89752 | 2026-06-27 05:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1caf450e-dace-3666-aebe-ab7949f71026 | -10.78463 | -56.76197 | 2026-06-27 05:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25fef147-3113-35c7-a0f7-9501b570177f | -10.93993 | -56.85355 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 717e9eb2-5f9d-3076-9e2f-e783f12ed961 | -11.66473 | -57.25763 | 2026-06-27 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef807606-ac62-3604-acab-9a2ae2f754ea | -9.02594 | -59.54325 | 2026-06-27 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bf3da37-f565-3cb8-a341-f3751c3ded3e | -10.78926 | -56.75534 | 2026-06-27 05:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a91a052c-db59-3125-954c-40f3a4248894 | -21.75957 | -56.27033 | 2026-06-27 05:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 003131a9-8377-3181-b764-b3565c465230 | -9.03131 | -61.33162 | 2026-06-27 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f176a9df-e2de-370f-bb6f-336628556834 | -11.32359 | -54.46784 | 2026-06-27 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b4dcca4-c5ff-31ea-8466-6e07c8d386ac | -10.93948 | -56.85708 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 353826f0-ac8c-3df7-8f6c-68a8d80c45e6 | -21.75306 | -56.26957 | 2026-06-27 05:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| de6bb517-56e7-3248-9555-c2c90b542659 | -9.03205 | -61.32645 | 2026-06-27 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9daf16a6-61a3-3b6e-9cee-a1da07b5b0a0 | -10.54422 | -53.71834 | 2026-06-27 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f954251-e9fb-3038-9d3b-6f2b929698fb | -10.93903 | -56.86062 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09864226-b017-368f-926e-1df7cf82d959 | -10.05474 | -59.1228 | 2026-06-27 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5388ff01-b97f-3621-832b-c3a2604bde48 | -10.93435 | -56.85305 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdba8389-55b3-39b7-b4ff-23ede78fb085 | -10.30415 | -57.14178 | 2026-06-27 05:55:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51e7ceec-d8fe-35ca-be0c-93d9272ad913 | -11.65928 | -57.25684 | 2026-06-27 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62d02783-5a98-31e7-ba93-1ea153ea2773 | -10.02266 | -59.35136 | 2026-06-27 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 774815c6-2aaa-30fc-9184-f1e44369e827 | -10.90059 | -56.85267 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e7b2ea7-c52a-3af7-8734-61da9a3cf037 | -10.90103 | -56.85377 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 933330e4-b506-35a5-b07b-ace7d1d1a59e | -10.38583 | -56.72433 | 2026-06-27 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ebccbcf-a24a-3030-926b-1407df2bc072 | -9.59535 | -56.9262 | 2026-06-27 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c46068c2-8cbd-3867-814a-e59c13bd504f | -10.02068 | -59.3541 | 2026-06-27 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 799a11e7-442e-3d67-a537-4dfe1110a1f8 | -9.5875 | -56.92947 | 2026-06-27 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f691fd59-e308-36e4-b539-f6d5ae5d89d5 | -10.38746 | -56.72363 | 2026-06-27 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28b6a64e-1fe9-3a1a-a1c7-88e1b60ff9c0 | -11.64869 | -54.8986 | 2026-06-27 05:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a481c8f2-c83e-31a6-a731-2d9b410af9b6 | -9.58797 | -56.92599 | 2026-06-27 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a1b699c-7a98-3fd3-bac6-ced87b552a8d | -10.93345 | -56.86021 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8da1b694-8ac3-3a04-862d-44e8d9195a55 | -9.59339 | -56.92666 | 2026-06-27 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6efcbc65-5c03-330d-bfec-b0422c0d8bbb | -9.03603 | -61.32707 | 2026-06-27 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a7b4262-0ead-3b4b-95c2-dea33edca3d9 | -10.79068 | -56.75903 | 2026-06-27 05:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d36651-6075-3de3-919e-1a15b3a8cffd | -10.30909 | -57.14587 | 2026-06-27 05:55:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8fc2891-9b72-3500-9a89-51f3fc804dc8 | -10.90523 | -56.86061 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94e29a6e-ffd4-3b7a-a20b-d92f5ed22d85 | -10.78834 | -56.76286 | 2026-06-27 05:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de063bd1-a1c5-3b82-9214-388db3d17211 | -10.30955 | -57.14241 | 2026-06-27 05:55:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32375815-7f56-3897-8db0-172f35b84777 | -21.77121 | -56.28868 | 2026-06-27 05:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0057f67-2080-3caa-a7c4-e3c415ace9a8 | -9.59293 | -56.93008 | 2026-06-27 05:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 33e7bc6b-d46d-316b-b6b9-c8cd94a716e5 | -10.90055 | -56.85741 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2dac467-ce93-3b28-989a-68387772b81b | -21.77774 | -56.28912 | 2026-06-27 05:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bad16aba-a312-35eb-bfbd-39a27b84e763 | -21.76003 | -56.26481 | 2026-06-27 05:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8077372d-a889-3692-ab8b-a1da591c2818 | -10.90007 | -56.86104 | 2026-06-27 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b15fe7d-43dc-3057-ab09-2e3ae2a5c1ae | -11.64927 | -54.89351 | 2026-06-27 05:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19f3bd1b-f93a-367d-97b2-e8c219f8a54e | -9.03455 | -61.33736 | 2026-06-27 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8400fc0d-144d-32de-881d-29d1596a4951 | -10.38234 | -56.71964 | 2026-06-27 05:55:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d87e819-0622-3a10-8722-38fa71bf7c39 | -11.64754 | -54.89241 | 2026-06-27 05:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11ae5b81-064e-3533-ace6-89ffe509b509 | -9.03529 | -61.33223 | 2026-06-27 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61b69d68-d188-3ea9-b5a0-1a7a1efb03ca | -10.05635 | -59.12086 | 2026-06-27 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca2a235e-f946-3e56-92fe-56fa68959f84 | -12.6236 | -57.8926 | 2026-06-27 06:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4588db29-5aa5-372a-be92-c79ece62f95d | -12.4654 | -58.481 | 2026-06-27 06:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 27331525-5dd3-31a3-8246-2e9fa0644b18 | -12.4651 | -58.5009 | 2026-06-27 06:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 46e8365e-75da-3c02-a291-1ef2dd585bba | -12.4654 | -58.481 | 2026-06-27 06:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5619516c-f96d-3795-83cd-3fccd90e2900 | -12.4651 | -58.5009 | 2026-06-27 06:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d681aacd-4d85-3168-8893-b9b2613231da | -12.6236 | -57.8926 | 2026-06-27 06:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 52c8db98-648e-3a2b-9ec7-8f3c5bfffe7e | -9.03108 | -61.33504 | 2026-06-27 06:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efa23824-e7a6-3ece-b8bf-cacd674c8462 | -9.0322 | -61.32605 | 2026-06-27 06:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49252d34-5d50-3f4e-877f-bbe5a684ec06 | -9.03597 | -61.32897 | 2026-06-27 06:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 664cf2ee-048c-3834-835f-56b1366c2e5b | -9.03164 | -61.33055 | 2026-06-27 06:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bbd7f4e-ff7d-3596-91c6-52fe460f6104 | -9.03538 | -61.33343 | 2026-06-27 06:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a75b5fc-8316-30fd-a7cf-420618505eed | -9.03765 | -61.33145 | 2026-06-27 06:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e15dcc-7cd8-34fd-81e9-eaf49275fbdb | -9.02997 | -61.32808 | 2026-06-27 06:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3806bf13-d0b1-3da3-94a6-616eb29ed3c1 | -9.02938 | -61.33257 | 2026-06-27 06:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README21.md)
