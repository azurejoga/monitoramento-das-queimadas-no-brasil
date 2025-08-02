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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b25dac6c-03f7-38d4-bf9e-3957d261d730 | -23.00187 | -48.63921 | 2025-08-02 05:16:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ea69655-6e7c-35a5-b020-62c6a7c09018 | -22.40184 | -46.78914 | 2025-08-02 05:16:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 28924310-5d31-3b5d-ab17-021736b765b6 | -22.59283 | -54.97323 | 2025-08-02 05:16:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b5aaea97-e8fe-3873-b90d-085ccf99d50b | -21.33128 | -55.63395 | 2025-08-02 05:16:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcec4f95-d16f-3383-a94f-f5bbea17d195 | -22.32776 | -48.71414 | 2025-08-02 05:16:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 003a003a-6bb2-3537-9157-36ad99f7c28e | -23.08814 | -55.19086 | 2025-08-02 05:16:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6080e88b-4f9d-3046-aaa5-36cd2ba63889 | -21.14587 | -48.01503 | 2025-08-02 05:16:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a9aa6ce7-e4cc-365c-b93e-bd1002b440c7 | -18.9277 | -52.48719 | 2025-08-02 05:16:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91f78027-4b4e-3ddd-aca3-8004aff1f606 | -29.77965 | -53.84546 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 6.0 |
| 5e40d395-1775-37e3-8834-334900711889 | -29.77553 | -53.84544 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| 1f8d9d44-311e-3d45-85c5-03de3ab4fa28 | -24.64167 | -51.17233 | 2025-08-02 05:18:00 | NPP-375D | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 850112a6-7f1d-3871-8b46-3ffccb430530 | -24.64199 | -51.16861 | 2025-08-02 05:18:00 | NPP-375D | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 07d00a82-a890-3a1f-bc54-41c48986d345 | -29.78054 | -53.84599 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| c7f5f036-f87e-3889-81cb-8408924349f8 | -29.78495 | -53.85307 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 12.0 |
| 97ba0df4-52d7-3694-9b90-308fec840ed3 | -24.68737 | -49.89499 | 2025-08-02 05:18:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8313afb0-b9e8-3860-b2f5-725fbc8314d7 | -28.91554 | -50.1647 | 2025-08-02 05:18:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e384b487-0a69-3a97-a52c-861583aed77d | -28.91592 | -50.16956 | 2025-08-02 05:18:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 32b81456-5186-3d55-bbb6-e6c19e775060 | -28.74693 | -50.40317 | 2025-08-02 05:18:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c1cb774d-21a9-3312-ad14-b167be1c9305 | -28.79324 | -54.76266 | 2025-08-02 05:18:00 | NPP-375D | BOSSOROCA | RIO GRANDE DO SUL | Brasil | 4302501 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| da099acf-f788-3617-8d86-ae916a46faca | -29.77994 | -53.8526 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 12.0 |
| d10de6f3-60c1-37ad-b2b0-2ed72a8683b3 | -29.77493 | -53.85204 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| fb616c93-9573-3b07-99e6-2817473a7f07 | -28.91522 | -50.16997 | 2025-08-02 05:18:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cebf76c2-b04a-3ba6-baa2-7d1f0c5eb98d | -28.74722 | -50.39895 | 2025-08-02 05:18:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 369e8b83-18af-30a3-8d9a-3be21b665a33 | -29.77464 | -53.84491 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 6.0 |
| ec3427db-1a07-37e8-b717-cc0509c49654 | -29.78411 | -53.85259 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 11.3 |
| 34d9f460-605a-3ecd-9165-5d56d263ef6a | -29.77909 | -53.8521 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 6.0 |
| 3564ad9a-a6cd-3f2e-a0fe-98accb4ca8db | -28.91628 | -50.16429 | 2025-08-02 05:18:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 31ddcd56-0e15-309d-bfad-0440d83085e1 | -28.90934 | -50.16463 | 2025-08-02 05:18:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 57a980a1-5893-3211-b9af-1b2444e6b681 | -28.90315 | -50.16445 | 2025-08-02 05:18:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5f7774aa-b067-3be7-be40-781b8224005c | -29.78465 | -53.84605 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 11.3 |
| 2850a035-cfcf-31ee-97be-63d5ed945f4d | -29.78555 | -53.84658 | 2025-08-02 05:18:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| 368cf413-fc59-325b-a871-69d7fa02df36 | -8.0321 | -43.1257 | 2025-08-02 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| ae3d15c2-d665-394f-b2e3-d49937716205 | -12.6784 | -44.5085 | 2025-08-02 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| f1fea13c-4008-3e85-bdc5-bf8c4d82b47d | -12.6591 | -44.5117 | 2025-08-02 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| a6b54c03-eca8-306a-b6b9-9103bda9a8dd | -12.6595 | -44.4882 | 2025-08-02 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 7daf4389-83b4-3558-89ce-be598889a1cd | -12.6789 | -44.4851 | 2025-08-02 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 7af54f04-da44-3617-8adc-e7d26eb33783 | -30.85222 | -52.58507 | 2025-08-02 05:21:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 1a71713f-0725-30fa-9ee0-e95fb0ec20fd | -12.6591 | -44.5117 | 2025-08-02 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 11f3b698-db02-3fe7-9001-7cc59b005a18 | -8.0321 | -43.1257 | 2025-08-02 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 6f631a87-1c91-3800-bd32-ac28de544306 | -12.6595 | -44.4882 | 2025-08-02 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 90a34a07-2a1a-3df4-92fc-a969d3a538bd | -12.6789 | -44.4851 | 2025-08-02 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 010f85df-e2e7-3534-a56f-e8bd6c65c50d | -12.6784 | -44.5085 | 2025-08-02 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d67412a6-11a5-3ce1-8ec7-030343f45c9b | 2.75221 | -60.36736 | 2025-08-02 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4d12608-c3c1-313b-8f12-e5f7075217a9 | -1.29304 | -55.74796 | 2025-08-02 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90a67e6c-973a-30e7-8a82-63e649ea5e64 | -3.48116 | -51.19176 | 2025-08-02 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a01cabe-0bbe-3873-8136-ff611e1274a1 | -4.66381 | -55.96804 | 2025-08-02 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4c4f4f8-ba49-3a62-97bb-1295c187b8d7 | -11.41191 | -56.86436 | 2025-08-02 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dffb75ee-8112-314e-bdf1-d2485ff07ba7 | -10.1399 | -68.77744 | 2025-08-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0e14366-9df7-32c2-aafd-0113a33cdc30 | -11.41591 | -56.86378 | 2025-08-02 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d2b682a-25b7-3b33-a878-32f1c2099434 | -15.11595 | -55.22073 | 2025-08-02 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d940893-9dcd-33b4-aca2-571b3430288b | -13.99007 | -53.92981 | 2025-08-02 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09f2f6c9-de0a-323e-b3b4-508d4392ed6f | -13.69519 | -51.96138 | 2025-08-02 05:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e02a019f-708a-37a1-a596-a98b75c99b27 | -13.99627 | -53.93065 | 2025-08-02 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fa887a9-49d2-30f5-8188-12f67fcbf93d | -13.98184 | -53.94821 | 2025-08-02 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a148c340-091d-3e4a-b689-95544ae675e5 | -13.98236 | -53.94336 | 2025-08-02 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5a05872-7796-302b-8c5e-24a4776260cf | -13.99118 | -53.92963 | 2025-08-02 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc89e59e-7ed7-3869-b006-3efb3831decc | -13.69585 | -51.95525 | 2025-08-02 05:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ba361f4-b0d5-31f1-87a5-726d3913c884 | -15.11014 | -55.2171 | 2025-08-02 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7351ba23-c76d-3617-828e-65d7aeb7ddfa | -15.11595 | -55.21774 | 2025-08-02 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0795cec5-5b74-38e0-b4ca-53ec4086afa8 | -15.11056 | -55.21342 | 2025-08-02 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6c5a6a8d-69c8-33c2-993a-23cf6e58126e | -13.99737 | -53.93048 | 2025-08-02 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6877d8e-4455-3e6c-ab8f-7e0723865a3f | -14.60326 | -57.48501 | 2025-08-02 05:38:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b21c3eb-3831-3159-b1f5-14e23dfc68b2 | -15.11553 | -55.22141 | 2025-08-02 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcdb7bb6-0bb0-31aa-9004-943416c6c0d6 | -13.69457 | -51.95818 | 2025-08-02 05:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e6828ca-7180-3022-8d92-8ce8fd95ecea | -15.12136 | -55.22189 | 2025-08-02 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fbfe9dd-e6a5-31cc-a621-c186563f16ba | -13.70157 | -51.95855 | 2025-08-02 05:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7ff3022-3c80-3408-ab0f-24e84f1a04f6 | -14.60397 | -57.4792 | 2025-08-02 05:38:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 968ae1bc-97fd-3ac9-a2af-805e4a128edd | -15.11634 | -55.21707 | 2025-08-02 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a70a775-d26e-3532-8260-618b5e18ce9a | -15.10972 | -55.22086 | 2025-08-02 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a16ed508-ddb9-3625-8312-2575e0f50b83 | -15.12178 | -55.22121 | 2025-08-02 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63c8edea-d325-334f-a915-df40a6ec253c | -13.70287 | -51.95546 | 2025-08-02 05:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed222d95-6852-33f7-960e-b5fd163a4d9a | -12.6591 | -44.5117 | 2025-08-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| d461d684-b532-34ca-b320-230c9fc81db5 | -12.6595 | -44.4882 | 2025-08-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| df696512-e002-3c9f-a97c-9e624b31de33 | -12.6784 | -44.5085 | 2025-08-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| fd4beea5-b394-34d2-915b-1d8be177b481 | -8.0321 | -43.1257 | 2025-08-02 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| a8497510-332b-37ad-a8fe-ee59370cbd14 | -12.6789 | -44.4851 | 2025-08-02 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 2c64a8be-08aa-3f60-9f9b-d3dad4ab8eae | -21.33323 | -55.63235 | 2025-08-02 05:40:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94aed6b5-84d5-3827-a515-855761ed165c | -22.594 | -54.97387 | 2025-08-02 05:40:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 80a743bd-4e2a-3312-b662-fe39f867e163 | -20.87579 | -56.37732 | 2025-08-02 05:40:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb7010c7-a4a4-3f9e-af20-1fc13eefec9c | -20.87618 | -56.37309 | 2025-08-02 05:40:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65602590-15c7-3e9c-9247-746eb5eed555 | -3.51676 | -47.21012 | 2025-08-02 05:48:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2e6227d6-6d9b-3d56-8ffa-9f7f5c55c2a0 | -4.77081 | -45.33438 | 2025-08-02 05:48:00 | AQUA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 43b14b50-62b5-3625-8fb9-f752693e8cec | -3.51537 | -47.21938 | 2025-08-02 05:48:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 02f9109e-4e04-3776-b7e3-3b67d92731a3 | -12.6595 | -44.4882 | 2025-08-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6bde4650-2fe1-3ca4-b16e-15b2e124b235 | -12.6784 | -44.5085 | 2025-08-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 14d7637c-236c-377c-a96d-4eb10f0f422a | -12.6591 | -44.5117 | 2025-08-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| bf8cbda7-7ef0-3fab-b425-52eb3ce6df2e | -12.6789 | -44.4851 | 2025-08-02 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 91978622-3c43-39e2-b61d-a07d5c7cc11a | -8.0321 | -43.1257 | 2025-08-02 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| eac1223b-24b6-317e-9204-24c0d1dda5a5 | -6.5631 | -51.1126 | 2025-08-02 05:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ca9d4fba-0191-3cc7-98b9-9ee2f1e4cd01 | -8.05656 | -43.10317 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 34747281-dfd0-3f1d-bf51-71c24b47d580 | -8.04627 | -43.10169 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 37e291b6-8e0e-380d-8685-d25e5c8b6de1 | -8.04453 | -43.11408 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 26d3e841-bc60-3217-98ba-c23f32451a5d | -8.02225 | -43.12349 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 70846d97-754e-33d3-ae18-fd3d90d639b0 | -8.02396 | -43.11117 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 55a6d05f-a573-3823-807c-095335c01c02 | -8.02055 | -43.1358 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 2a9b9d7f-5844-3355-bc84-807cd0c6c60c | -7.56364 | -44.805 | 2025-08-02 05:50:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4222e335-b738-3e26-8494-979b30c61826 | -8.03425 | -43.11264 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 88be12b8-c07a-3a46-817d-010747ac1fce | -7.74624 | -45.13339 | 2025-08-02 05:50:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8c028afa-9890-35b2-844a-170cb16f2097 | -8.03082 | -43.13725 | 2025-08-02 05:50:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 963bb924-31bd-3d9e-8988-dd2fe6bedd0b | -7.8722 | -45.53498 | 2025-08-02 05:50:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README24.md)
