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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74740b49-6b7a-31b3-b132-f7ecb6ba5890 | -10.88149 | -63.901 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a4a1c6c-1fd9-31e5-95e5-7e3693432ac9 | -10.87871 | -63.89687 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3af8cd65-1893-3e0d-b240-4b98e76ccf91 | -10.87815 | -63.90044 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 86896125-8c02-3ef3-ab64-01504bbd922d | -10.87537 | -63.89634 | 2024-10-06 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7aea6f4-6be3-310c-bf61-e1af5bef5131 | -12.02336 | -63.74118 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 223b5c50-18e3-3a4c-a010-96fdb9c24587 | -12.0228 | -63.74481 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1caa6492-7c82-39c6-8b57-e36bae1521bc | -12.02225 | -63.74843 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13b7ba62-23c9-3840-97d1-921a65cf2e24 | -12.0217 | -63.75204 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d6c8630-67e4-385c-a36a-c7484da0d063 | -12.02115 | -63.75566 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec1393a1-31d4-3fe6-b02c-09c5bb8cefe4 | -12.01999 | -63.74065 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 746973d8-ca79-313e-85c8-e29cf1367bed | -12.01944 | -63.74428 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| becb24c9-20cc-352c-a88e-bc3bec8003f3 | -12.01889 | -63.7479 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc6184bd-2a09-35b2-8a3a-2f6fe3d6998f | -11.98946 | -63.52781 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8303befe-0b45-35a9-b7fc-c400babb6133 | -11.98891 | -63.53146 | 2024-10-06 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8913ef6d-d868-3d8e-bfc9-ee2a96770e1d | -12.43842 | -63.69055 | 2024-10-06 05:36:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dd10fdd-53f7-3878-b93a-0840e31e7d98 | -9.45216 | -64.5378 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0eec19c-6ba2-385c-8146-dcc533ee36d5 | -9.37405 | -64.49673 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38265b7e-517c-3fdd-9096-b45eb493027c | -9.37059 | -64.32409 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa0459d6-f91c-3829-895d-2aa9dba0c84d | -9.37004 | -64.3276 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0943661-02b5-33e5-be2d-58178c2d9327 | -9.36949 | -64.33109 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab09a435-30bb-308b-90c4-cd8f7434cf1a | -9.36894 | -64.33458 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f24ef89-11df-3ac9-a58d-aa05471d04d8 | -9.36781 | -64.32007 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20b1f4b4-c459-3a69-8394-0ee4bfd63d33 | -9.36726 | -64.32356 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12eaffc6-daab-3e98-93b0-60cbd878230f | -9.36671 | -64.32706 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 151d8403-100e-30e7-b34d-a5cb41d7215b | -9.36616 | -64.33056 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9d04d4d-f589-37e8-a8cb-11cdcce433ff | -9.36561 | -64.33406 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25e3098d-b99f-35ee-8756-29655ad4c696 | -9.36449 | -64.31953 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 868b0f55-be60-3996-911b-19a13161b138 | -9.36394 | -64.32304 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e5277e24-1ced-3917-903e-ab878412f6fe | -9.36339 | -64.32653 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3928e7a4-3170-3a7f-9154-3ad8e3aad90e | -9.36284 | -64.33002 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43ef1c3f-a990-3a86-a3ac-aeed450f9431 | -9.36229 | -64.33353 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f1e1853-2b2a-315f-a7e0-7f4ca482843a | -9.32686 | -64.3637 | 2024-10-06 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 795ca38e-b831-3114-be8e-dcc662380ddb | -9.31049 | -65.38432 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 854164be-e13c-377f-8929-b7df43166d18 | -9.30828 | -65.37659 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0509e8e-674c-3bdf-bed2-9d3494a0b924 | -9.30771 | -65.38018 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ddaf7c73-66ef-394d-afa4-435f894263e5 | -9.30713 | -65.38377 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 010fb661-2a32-3081-8134-7b4ed072c9fd | -9.30492 | -65.37605 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41865bf9-79cb-3e2f-afd5-8e933d861915 | -9.30435 | -65.37965 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b38796b6-15ce-3dee-af02-cbec09a6a31c | -9.30377 | -65.38322 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fbad4a0-9bcd-31a3-9a0e-d92f3e7a6422 | -9.29306 | -65.51431 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acba365c-13e6-34e9-8d6c-6e242bc64391 | -8.54902 | -67.12771 | 2024-10-06 05:36:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3796512-2517-34e4-966d-f7f574a571ce | -8.54833 | -67.13185 | 2024-10-06 05:36:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2874337c-5638-39b0-8aac-ffe2c0754a55 | -8.54611 | -67.12298 | 2024-10-06 05:36:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fcda863-6fcf-3b64-a52b-4fd3ceacb8b4 | -8.54542 | -67.12711 | 2024-10-06 05:36:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 660dce4a-b4e0-34ba-a393-313fab451cb4 | -8.05415 | -65.98453 | 2024-10-06 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59e50012-2139-390f-a11d-9d48df20b2c4 | -9.63868 | -51.77845 | 2024-10-06 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fc0f93c-92e0-32c0-af35-7f6f45df2392 | -9.63798 | -51.78419 | 2024-10-06 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0d42a25-f296-34e7-9625-480d82a3e129 | -10.51421 | -50.96034 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88ebbe28-0695-3e43-bcea-6fc9d6a8f52e | -10.50715 | -50.95956 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 069106fe-50f4-37ef-b182-60a0e6791b3d | -10.45091 | -50.73091 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d3aeba3f-4be5-331b-b4c0-849fb05c6bf2 | -10.45012 | -50.70711 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 33d04fff-572b-331a-80da-0b833c4d5a14 | -10.44848 | -50.72152 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fd46ac6a-e908-3697-a790-5cc3426d218b | -10.44766 | -50.72879 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| aa707901-c2f0-337d-b168-f6fccd552f6d | -10.44639 | -50.70824 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 160.7 |
| bf722837-0ccd-3f7b-ba4e-10235dae7c3b | -10.44553 | -50.71537 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5502d199-b74f-3141-9e88-3f39def57a58 | -10.44467 | -50.72252 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a1d96e65-bac0-3c0e-8891-8bd9b2223327 | -10.44381 | -50.7297 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f4b58a26-f36b-3e4e-884e-5f18f5f911bf | -10.44296 | -50.70627 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 3a8a0ce0-5f83-31ef-bb3e-624285b6f79d | -10.44215 | -50.71343 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 2c05a6c6-6688-30e0-98c7-caa41ff37722 | -10.44135 | -50.72054 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d9e5f014-634a-3d02-a3c3-315f5bdbd7a0 | -10.44054 | -50.7277 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f4b2552c-82e0-3c43-bda0-72ca6c8a02f6 | -10.43923 | -50.70744 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 160.7 |
| d8d808d7-c6e0-3880-85e8-1ca1e40cb479 | -10.43837 | -50.71458 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| feece6b3-c393-3393-afe2-87a9c5647e13 | -10.43754 | -50.72161 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 03858f98-2270-3851-a695-a7f85c7872e8 | -10.43669 | -50.72868 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9a0c6051-b4ef-39f2-96ee-d5004a9bf084 | -10.43581 | -50.70538 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 165.0 |
| b9374923-5f93-32c0-92d9-9d1acf67a617 | -10.435 | -50.71259 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 165.0 |
| f181dadd-5766-3777-b4ca-87d3cea67346 | -10.43421 | -50.71965 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 22aba63f-79fd-3eeb-b90c-0d6106a51346 | -10.43341 | -50.72673 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 37.3 |
| baef6c36-d677-34a6-95f0-45e9d54dcb27 | -10.43208 | -50.70655 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 50f5ce53-33eb-3c26-87d2-355c83525bc3 | -10.43123 | -50.71371 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c99679c2-c76d-3211-aa34-02ae73df1073 | -10.43039 | -50.72075 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 0ce65fe3-deac-3590-9d9e-58be5732ff56 | -10.42955 | -50.72781 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 0e51c82c-0a0b-306c-a509-ca5ff8864026 | -10.42867 | -50.70443 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 165.0 |
| d477997e-b78f-30d7-a64b-0dbbe2a98e8a | -10.42787 | -50.71161 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 7f44725f-1b84-3021-8b9a-288833c85d51 | -10.42707 | -50.7187 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 61054660-2859-3068-b9da-4a76935a8f73 | -10.42628 | -50.72576 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 37.3 |
| d6d55010-84f9-343a-a8b3-873a2a8b9f7f | -10.42548 | -50.73281 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5cb3c9a5-910a-376d-9dee-bacd747b2f4f | -10.42495 | -50.70559 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 77d0246e-3477-384f-bf40-8579caf881b3 | -10.4241 | -50.71271 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| dc7c08d7-99d4-35c4-8548-11a21ae16cae | -10.42327 | -50.71974 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 1ae6ef6a-1408-3d33-b4a0-3e893bac3e6e | -10.42243 | -50.72677 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| fdae4ad5-0edd-3e16-b8f5-154db38f7c8a | -10.4216 | -50.7338 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| ecb1b613-ac2d-3ef0-a46b-24d9823d7daf | -10.42153 | -50.70346 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 24d11d15-79b2-3f16-8b56-dfe6485b4d4f | -10.42074 | -50.71055 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 7f93b946-4873-31a6-8045-c39fe1d69d48 | -10.41995 | -50.71763 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6739c5d4-0d9b-3c90-be8c-07642ebea352 | -10.41916 | -50.7247 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f0383375-0ada-3d39-b9ff-1c3e7fe94a72 | -10.41837 | -50.73175 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ae1ba38f-f811-3f27-adc2-6635d2d03285 | -10.4178 | -50.70469 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa5acc1e-0a09-36be-94f7-f07a220c3b3f | -10.41697 | -50.71173 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 09c1ff3b-82e3-34cd-988e-8c095728c849 | -10.41614 | -50.71875 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 38451e44-56d4-377b-9217-0614bd109249 | -10.41531 | -50.72578 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a9b7ef74-c284-38f6-b157-f99e572db8dd | -10.45094 | -50.69989 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| b718d1a7-9b6b-3f7d-ac70-76b7c16600f1 | -10.44895 | -50.68682 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 092aa8f4-0d8d-327d-a21b-62185753b1f1 | -10.4481 | -50.6939 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 962cb5fc-a606-37a5-94b8-34d4140695a0 | -10.44724 | -50.70108 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 1d155d52-7075-38ef-b01c-981836eb0688 | -10.44617 | -50.67792 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d20c643c-e146-3a8f-ad7a-0b4f4948de88 | -10.44538 | -50.6849 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a0fb1763-c904-3fb8-8ffb-8e68c8a16afd | -10.44459 | -50.69191 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 5fc70bb1-0ce9-350e-b8e5-122b175ad657 | -10.44378 | -50.69906 | 2024-10-06 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |


[Clique aqui para ver as próximas entradas](README136.md)
