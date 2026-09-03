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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a03addb2-6bad-352a-8169-fc8397457f9c | -3.6311 | -60.548599 | 2026-09-03 01:12:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f99bf650-ae7f-3717-898b-82b080278bfa | -6.3234 | -56.0355 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 032065c1-677c-3bde-9d16-a371fad0e858 | -10.1975 | -50.277802 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5af64060-9039-3857-af28-78ffcdd56fa7 | -10.5469 | -49.9786 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 802e2b9a-cb18-3b11-a4d5-bddcd504e1d8 | -6.4535 | -48.5298 | 2026-09-03 01:12:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| fc47407c-05d7-3210-99ba-8106caaa0dc5 | -14.0669 | -48.392899 | 2026-09-03 01:12:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d53f7d42-684a-3948-b9b2-0129e570575e | -8.1071 | -50.973202 | 2026-09-03 01:12:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d6a7209-62c0-399f-b280-df8996b5327e | -1.4805 | -54.811298 | 2026-09-03 01:12:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f26bd690-29fb-3d3e-81eb-b280aa45a0c5 | -0.0051 | -60.5952 | 2026-09-03 01:12:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 36617bd0-45b5-3816-a006-fe66b2133ffc | -18.7817 | -48.898998 | 2026-09-03 01:12:00 | METOP-C | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0542a6c0-48c0-3f65-a3c9-081768431ce5 | 4.3269 | -60.776699 | 2026-09-03 01:12:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6edbf8f3-52e4-31df-88b4-9e4775a6e0d1 | -5.526 | -60.190399 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 349949e1-ec57-30bb-87a9-250a0a7fdba4 | -8.1013 | -50.949501 | 2026-09-03 01:12:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b794233d-2b09-3f07-8f32-673045a12fb3 | -6.1224 | -59.960201 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c38b383-10ad-37c8-a328-0d8d96b5569b | -6.6957 | -58.753899 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63e70685-3d85-3305-a5ae-09181695b1b1 | -10.291 | -50.0298 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5369fb2-48db-331c-a002-b1ef4bee586d | -6.6536 | -52.951199 | 2026-09-03 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c68e834-7f81-39e8-be62-1cad59927ea4 | -3.2109 | -61.1936 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c557783f-6093-389a-a8fa-1b1002726708 | -10.22 | -50.285198 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25ffd587-8f8c-36f3-a966-2f7adcfd24a7 | -7.58 | -57.696899 | 2026-09-03 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 357ac55a-6e03-36dd-a04c-2c07a6b58e7d | -6.6374 | -55.252701 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53a1af15-69f9-39f4-81eb-d0be703d9019 | -3.395 | -59.417 | 2026-09-03 01:12:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57492cea-8334-3a06-bebc-586aac9e6103 | -10.1945 | -50.265598 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba34f561-3198-3178-a09f-f3433c14be61 | -5.575 | -60.179699 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d99ccc03-f7f6-3e7a-b247-dde8dcb43fb6 | -4.1629 | -51.067402 | 2026-09-03 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8b47617-0396-3b29-9967-31e9b22ab606 | -6.6941 | -58.7467 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd5b917-297c-3daa-bfe1-03b4a4a9956d | -6.6127 | -59.1171 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e10df045-7fd3-3d71-a75f-28e0fd0247ce | -6.5089 | -53.6031 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2ca6834-5303-39c0-b141-6ccedace4720 | -3.0937 | -61.175598 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db052ec0-c41d-34db-9709-6f5d5b2079ad | -10.885 | -45.2953 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b573ec1-8e38-3068-8c05-a6d8930d52af | -10.9015 | -45.318401 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2b6d71e3-408f-3dde-895b-c1145a0e60fd | -8.472 | -54.6647 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b8447f1-f8b0-33fc-967e-3084366b0275 | -3.3083 | -61.260201 | 2026-09-03 01:12:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c31a385-2aa0-3ee5-95ea-ca33cb8549b7 | -18.185699 | -51.799702 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1fe191b9-d950-372c-bf5a-13ebb6126007 | -6.2676 | -55.437901 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68a1b9bb-da92-3ceb-b988-73e88d865ce4 | -1.0414 | -53.715698 | 2026-09-03 01:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2f76319-6419-3779-8e9d-6fca3cbe83b2 | -6.6618 | -59.428398 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 427ac827-eb1c-3ab1-a3e8-62e2abb50cc7 | -8.0915 | -50.9519 | 2026-09-03 01:12:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9949ea3-c8e3-3389-8ffc-287eeeb0ff22 | -22.4422 | -49.757198 | 2026-09-03 01:12:00 | METOP-C | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b933f2c-5477-3286-a709-d7b65a2c663e | -3.6267 | -60.574402 | 2026-09-03 01:12:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09d7a6be-9543-3e31-9492-744aea9279e6 | -6.6633 | -52.948898 | 2026-09-03 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 345e4834-0b5c-308f-b232-d0eed39a24c1 | -6.3842 | -58.285999 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 920bce34-ab29-3f62-b25c-0a0eeff3ab79 | -18.7719 | -48.901699 | 2026-09-03 01:12:00 | METOP-C | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c18af07d-a024-3935-b8ac-b96bdb2c1da4 | -6.5802 | -58.561298 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e44dd7bf-b1a4-3b1f-8f10-0bd8e662e69e | -3.0391 | -61.480099 | 2026-09-03 01:12:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7b502a6-8c56-3ac9-9bbb-c88a7b1172f8 | -10.8946 | -45.292702 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5e1eb0a-3ea2-332e-9a69-2148c7f088b4 | -12.0199 | -60.528099 | 2026-09-03 01:12:00 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a56dc40c-fea8-31e3-a302-c3f9c4dbb8db | -8.4853 | -54.677399 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb790fb-f6c3-3e97-a730-c1a0d05d5839 | -4.9812 | -55.853401 | 2026-09-03 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faa9b024-8dde-3b8e-9f6c-59b1264d278a | -8.7918 | -54.574501 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3350a8fc-4b54-3b38-b4f8-1726bb2459e7 | -6.6876 | -58.763302 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebbf1cd7-2a57-3afd-8ab6-5cbbe64beb0b | -6.9673 | -59.783199 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b15ece7-9392-3652-a0ad-2d5f2b883089 | -6.652 | -59.4305 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c11a0e2b-172c-3019-ae6e-db80f4ab03ba | -16.783701 | -49.6199 | 2026-09-03 01:12:00 | METOP-C | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 59b1068f-23cc-304a-96c3-0577cb72ae90 | -5.2667 | -60.180801 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fbb54ec-a779-389d-b0e8-e6370a23435a | -6.6455 | -55.243099 | 2026-09-03 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d81959c8-84f1-384d-b68d-95427d199a2d | -10.2134 | -50.2999 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd81069-9cfa-3d69-9e48-57a1f76c48b7 | -8.4451 | -54.726002 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee52e90-82d0-3cab-978d-d714ded3df37 | -18.177799 | -51.810299 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c092a2da-9427-3da4-af81-d012f49d626a | -6.3799 | -55.2108 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00d9411-8d47-38a7-aa17-c54db79660a0 | -8.0973 | -50.975601 | 2026-09-03 01:12:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb7383e2-f7f4-3459-bc80-7bdc18255f02 | -3.7674 | -61.746201 | 2026-09-03 01:12:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e17213f7-477c-3971-92e9-c18de208be9e | -5.1846 | -60.273499 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2e2ab69-a2c0-3309-ae58-0eb425d9acfd | -5.5661 | -60.231701 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76471384-852c-3780-b837-66cfa564b359 | -4.1661 | -51.080799 | 2026-09-03 01:12:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6f4cc3c-9e76-36c5-bfc0-295ef1ba6e94 | -5.5242 | -60.1824 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a82164ca-b205-34de-a77c-2fb7928271a7 | -6.6421 | -55.228401 | 2026-09-03 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d1f0505-3d91-3b3f-92bf-2e03e6296d94 | -7.095 | -56.519001 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7084031-6e3d-31d1-a34e-005cfe05503f | -4.1575 | -60.692402 | 2026-09-03 01:12:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 171c6c5c-11d0-3236-93e7-c9526a154c55 | -18.144699 | -51.801601 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5aba8c8-6943-3a07-b67a-da965c2829c9 | -6.6353 | -55.688202 | 2026-09-03 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8f66925-4403-3262-bde6-09363d918b5a | -10.9111 | -45.3158 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c1178dd-6b90-3da4-9b52-1d07ce376573 | -8.4685 | -54.6497 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac271b3f-7508-342b-a90a-3a0b559ba5df | -8.1042 | -50.961399 | 2026-09-03 01:12:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1462f6a7-8e4c-373a-b74a-15cda5b7cdd8 | -6.6357 | -55.245399 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37f4979c-6050-3979-a530-7fd8b1ac7df3 | 4.4092 | -59.7897 | 2026-09-03 01:12:00 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4bec3470-c072-330e-b518-9672dad343dc | -3.1344 | -61.219101 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d583234-1337-3cc4-b1c2-2fe6b132282e | -8.456 | -54.6842 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56c44a8a-bf4a-3926-accd-c6ba41b2e435 | -5.2253 | -60.042099 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0e7efaa-3c18-377e-b1a9-8f229d652bea | -18.7845 | -48.910099 | 2026-09-03 01:12:00 | METOP-C | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a8f45bb6-19da-3895-b648-e3801154966e | -3.6231 | -60.558701 | 2026-09-03 01:12:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 639c013b-8152-3b5c-ab23-730fd5e94c41 | -9.0481 | -65.740501 | 2026-09-03 01:12:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d5d30c3-f2bb-3f31-8f24-80c6a2a2353b | -10.9988 | -45.067299 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25728924-9c2c-3a5a-a271-4caac2902a1b | -8.4703 | -54.6572 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af607e0-d9aa-3280-b9e2-dad44907ba93 | -6.2659 | -55.430599 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 598a685b-37e0-346b-b1b7-c5a248059f52 | -6.6635 | -59.436001 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 087d34d1-079a-3fa2-a650-25aa1342f2f7 | -10.3821 | -49.939201 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 903b9b91-df48-327f-8773-1b05344ca3e8 | -4.7089 | -56.058899 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c346f2b-22f7-3664-9460-3f8a0662275f | -6.7649 | -59.4296 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4904319-ac76-3592-88a5-7d7f41a24733 | -5.5732 | -60.1717 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b53559a2-9731-3e0a-ad05-df6558c80e11 | -5.583 | -60.169601 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17c1739f-d4e1-3ef4-9300-c9226b002501 | -4.2488 | -62.245098 | 2026-09-03 01:12:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c1d6285-2d23-33dc-bf0f-3277d4e0ff9f | -6.611 | -59.109699 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d353d2c-20ae-3739-a760-7f9bfb098271 | -9.7149 | -57.894501 | 2026-09-03 01:12:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9ac22a7-0d95-3485-a01d-4b751f2fbb3e | -16.4981 | -46.590599 | 2026-09-03 01:12:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fedd38ba-a0e6-3a64-a79d-a4f6f726ceb6 | -3.7744 | -59.318001 | 2026-09-03 01:12:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53750422-8c6b-36b7-aa53-ec75eccc364e | -6.2757 | -55.428299 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5325100b-d962-3b43-8a13-d77d997d4306 | -6.7683 | -59.444801 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da8fdcf2-728a-3eee-84ab-ef18f66d54e0 | -7.0547 | -59.207199 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b8dc699-be28-3801-9f46-20b148e40615 | -6.3816 | -55.218201 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
