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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f90bd751-f579-3e4b-8441-5fe25ea31452 | -16.98334 | -49.26889 | 2026-08-15 04:17:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba6b537c-1e67-34a5-bb6e-821876ed9a46 | -14.98234 | -46.61056 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d664508-d35e-31cd-8219-1d5f47da42d6 | -13.46973 | -51.81352 | 2026-08-15 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 897ce2e3-e8b4-3ca6-8089-477896051c2e | -15.03832 | -52.69347 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dcd6c9f-3ab9-3c80-8f89-14b94de13549 | -14.91908 | -46.64307 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| facdd8fc-8f84-36ce-a02d-1d74ce3e1f2e | -14.92129 | -46.62999 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dff184f-0aa3-30e7-be48-ebee5a9b652a | -18.57427 | -48.34129 | 2026-08-15 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c4e03e0b-0bb0-3569-bd14-ee4fc600a467 | -13.2686 | -54.1913 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da84611f-1252-3da3-b3e5-0ecbbc3c28de | -21.57047 | -45.57785 | 2026-08-15 04:17:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 989c1a39-64f2-32ea-a52d-90f749845067 | -14.98511 | -46.61575 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7752883c-8db2-397f-8958-cb57080bc2a5 | -13.81554 | -53.78537 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 933deeb5-c124-3727-8877-d46b77d93304 | -14.40271 | -48.95422 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 020d80cf-b4bb-3352-aaed-30c125f329cb | -14.48673 | -52.08726 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 440b63bc-6a22-3ad5-9061-c5d44fea8c93 | -12.90161 | -52.83081 | 2026-08-15 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34b468a2-cebe-3ab5-81f7-23e32ad5d32d | -15.29097 | -53.19007 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59cd618c-2d2e-394c-bd65-e3749f8383dc | -14.45642 | -51.9265 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fece11cd-dcb5-3f04-8539-93d12e05a2fd | -15.14482 | -48.63063 | 2026-08-15 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9df74980-2b60-3c6d-aa0b-68a0136d407a | -14.91909 | -46.6214 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a217b52-6e47-375a-97ec-25b4319d923a | -14.94254 | -46.63436 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1737e885-d63e-3075-bfcb-2c9d08bd3af2 | -21.82989 | -44.19618 | 2026-08-15 04:17:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ccea5898-f0e7-3bf4-a5ee-840959eabbde | -19.49568 | -44.8053 | 2026-08-15 04:17:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3118692-d541-3fee-b255-e71f5e3d89f4 | -14.43551 | -51.85036 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 186bc89b-4017-3088-aa8e-3028847decf8 | -14.44692 | -45.6937 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40146480-b070-3f20-836c-8daa665afc81 | -14.07591 | -53.60327 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09e90efa-3408-3dd7-82c6-f2422f2e371d | -17.89943 | -44.4417 | 2026-08-15 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6acfd11f-b97e-3c06-b4ac-bf39f690f640 | -18.17875 | -45.221 | 2026-08-15 04:17:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edd227a9-ad8e-328a-9f2a-17be09caec5c | -14.44881 | -51.91289 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f9ed4ea1-bd8e-3408-8401-446294faf69e | -16.80027 | -42.49146 | 2026-08-15 04:17:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72d0fff1-de03-3b9c-9c97-9dd887bd2de4 | -14.08344 | -53.70766 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3a47477-bb19-32c4-9103-3153fdcda916 | -14.07163 | -53.60197 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57ee7ade-dd7b-325d-92ec-83dbc2526256 | -23.50237 | -51.72948 | 2026-08-15 04:17:00 | NOAA-20 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c0c1d81e-dfe4-3032-9559-cb3e0ef983ba | -14.39865 | -48.95333 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fdc9b12-77ee-31ce-9b06-4ab326fddbaa | -16.11004 | -49.86041 | 2026-08-15 04:17:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| acd3a035-7a54-3f28-af0d-16fb4594157e | -14.07889 | -53.68198 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e23fb88-98fd-39d2-9c6e-6cb7bdb66d6e | -14.91983 | -46.63862 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 90faf122-b95e-308b-b14f-0c4cd0217070 | -16.95496 | -51.74693 | 2026-08-15 04:17:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 297d8965-bbcf-3bf4-9dfe-eda2fbdc8777 | -14.9305 | -46.6189 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eafe53c-402b-3f0d-af43-fe267e58ecdc | -14.44085 | -51.95341 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd384c09-f239-302a-9e19-99867702d5ab | -15.10562 | -48.69813 | 2026-08-15 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3fec20e-e299-3c54-93b8-799d9da36431 | -14.44412 | -45.68923 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3c166f0-0d02-3037-a4af-fd535b2b76ee | -13.80552 | -53.79221 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 079b8f84-1743-3e05-949e-ef44bbaaece2 | -15.03652 | -47.03376 | 2026-08-15 04:17:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3ab256b-0660-3c23-9884-c93ed3e759e0 | -14.45035 | -51.93124 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86d0c7c8-5578-3746-81ee-769c823365ef | -14.46667 | -45.67696 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 017c58df-a786-3137-868b-08d468e1f725 | -14.4926 | -52.03197 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f20ec8e-d0c1-31bb-923a-2f07a0935cdb | -14.44044 | -51.85132 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f480dcdf-7b3e-3455-86d5-165957e1ca1c | -17.9049 | -44.45007 | 2026-08-15 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 037a5dcf-ece1-347d-8835-5fb68214e579 | -14.30857 | -53.06495 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61aa34a6-63d0-3d60-bc6b-fc996628fbe4 | -16.88915 | -54.14676 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af8718e9-3bf5-30bb-bde5-f2b90b57c26c | -14.73471 | -52.68967 | 2026-08-15 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21b4cdaa-db12-3fff-a05a-3009291d072d | -15.65325 | -48.21188 | 2026-08-15 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9eb8bf29-ca85-3541-ba2d-d3060f08ee40 | -16.90039 | -54.17275 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1277961e-c44f-3c92-b655-cbdfb22b2477 | -14.30108 | -53.07488 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7902201a-64e2-3182-a779-4725ce8c5138 | -17.57745 | -45.38363 | 2026-08-15 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75ab562b-8c4b-359e-9e76-2ff5f6eb75f2 | -15.15689 | -50.06676 | 2026-08-15 04:17:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a3c9221-32bd-3f56-8b66-bb7a0be8cb80 | -14.59808 | -46.74152 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e7f373d-8fb8-3a7e-948c-5d6e1116d66c | -18.10286 | -44.72153 | 2026-08-15 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fe4200bd-cf43-33e2-9b92-91a9b9fb365e | -14.60597 | -46.73859 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49244a4b-11ee-3596-8b7e-bcf73f7501cd | -21.56716 | -45.57724 | 2026-08-15 04:17:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c56c880a-cb9f-3414-92d0-33fed9e3eafd | -14.98865 | -46.61646 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f45cc2d2-88de-33ab-8ef8-4c9bcff061d4 | -20.01375 | -43.89739 | 2026-08-15 04:17:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c1751170-dc37-35e1-870b-3416968c6c85 | -14.966 | -46.62041 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12a560bf-d4a3-3470-8aba-4c85e7f76595 | -14.75504 | -48.24265 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9d514aa-efc9-34cc-85be-254dc761741a | -14.93831 | -46.61599 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65bd7463-bd25-3b9d-b78e-382afaca08d7 | -14.442 | -51.94759 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29140580-149d-350b-a6fd-a206f8bcbca1 | -14.24704 | -45.41631 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3defd2f5-edad-3db4-9033-99d3a70f2a22 | -14.69621 | -42.91442 | 2026-08-15 04:17:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 25816363-ef48-31d0-b2ee-9965f44565b5 | -14.5988 | -46.73729 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0c132d9-be94-33f9-a2d5-1f3e090b59ab | -16.88983 | -54.14111 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecb4e61b-e881-34aa-974d-c82cbd569c64 | -13.82834 | -53.78025 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a02fe05-ca27-35cc-9dad-36a8fb5434b7 | -18.00312 | -49.40356 | 2026-08-15 04:17:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5554a84c-2b7d-3970-a724-375ed4ea25a1 | -18.58479 | -41.28165 | 2026-08-15 04:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| cdd03b3b-e07b-3be3-b16e-0b25307d563f | -14.93474 | -46.6155 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d7a4384-c3df-3fbd-a993-c32cf89b8c0e | -20.33118 | -46.74824 | 2026-08-15 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb9c596a-f304-3843-beff-22cfd05ab525 | -14.44501 | -51.9061 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8d707d5f-fa54-32ca-ad92-3a5fe9b85e3b | -16.89532 | -54.14451 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4ac5dac-1312-326b-9974-9f4d17246715 | -14.96173 | -46.62394 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a68af227-c549-39d3-aac4-0246b08c2c2a | -20.01822 | -43.89054 | 2026-08-15 04:17:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5a57063a-de4a-348d-a3db-58eeffcccea3 | -14.71646 | -52.88948 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3f90c68-e3de-30d2-92a1-69cc415f79e5 | -20.33459 | -46.74882 | 2026-08-15 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7557d966-726d-3eaa-b5e2-1f57bdc9f49e | -14.72229 | -52.88755 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ddb54ad-7799-3e40-9656-7eb00f245784 | -14.10093 | -53.70741 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7e80450-ca91-3766-bb05-62597a328a26 | -14.05823 | -53.6692 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efde4823-ebd6-304c-87c2-b60802532c72 | -17.89554 | -44.44474 | 2026-08-15 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9c86a0a-c81f-3e73-9e31-01e24bb8cccb | -14.44284 | -45.69695 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b7d0c9a-dea1-38a9-8f8a-f72abf816abe | -14.22379 | -45.40835 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2aba95d-f1bf-3f29-84da-418a4d269282 | -20.32908 | -46.73994 | 2026-08-15 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3375e487-d18d-319d-93cf-1d21d2a4457d | -14.11567 | -53.66341 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e36b885-ce89-3b32-b5ae-e3dfbaf3c34f | -18.08449 | -47.95042 | 2026-08-15 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 758f04d8-dc3b-35b3-a88a-7195655c1948 | -16.19924 | -45.26644 | 2026-08-15 04:17:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45c9d44b-419c-3da7-a71a-03f9d665a667 | -19.69562 | -43.38333 | 2026-08-15 04:17:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 044ea365-0433-303b-8b76-1e8e3c1b3a07 | -15.52811 | -53.01166 | 2026-08-15 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62a61e94-465f-3d6d-904c-3249f1eee079 | -15.15252 | -50.06617 | 2026-08-15 04:17:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c043a085-9157-3e0f-a9df-359d5862890a | -14.69289 | -42.91388 | 2026-08-15 04:17:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a127124b-d401-3562-881b-3ef1c0bd388a | -15.16636 | -52.83812 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e436bd2b-322c-3c34-bcd0-f2f17d0bdb65 | -14.45354 | -45.67504 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10e44f0a-aa5c-381e-8381-2e0244d58b6f | -14.30602 | -53.06411 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f4449ab-78d8-39ae-9d2c-6afa226c2112 | -13.22956 | -54.17415 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f13762b-1f70-31ce-b0fd-5fff20c37270 | -16.89069 | -54.13691 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5934b813-0a51-3632-9ac1-fb6b410e3195 | -23.50317 | -51.72532 | 2026-08-15 04:17:00 | NOAA-20 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
