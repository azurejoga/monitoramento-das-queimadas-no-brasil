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
| 4eb41ef9-ffe5-3a06-abef-a0f5b803eb3b | -5.54412 | -44.87912 | 2026-09-29 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cae2dbf0-9f2a-3317-9331-1232650c21bc | 1.67482 | -55.90167 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b9c87d5-01b8-320d-af2d-2b58a739c966 | -3.01571 | -53.87389 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db417817-ca67-3a5f-89e4-9349749c5c9e | 1.68817 | -55.92082 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c94af86d-8c7a-3143-b32c-5af516ea2aea | -3.88457 | -49.50673 | 2026-09-29 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e34ad1e-ecb0-307c-99ed-2cb3ee94c82e | -3.69288 | -39.57947 | 2026-09-29 04:49:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 136d6335-3660-36c6-a1b6-8b0893817873 | -4.4953 | -49.64341 | 2026-09-29 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10fc6f85-4fe4-3bd4-87fe-a9583702791b | -4.36257 | -47.76933 | 2026-09-29 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23756b59-882a-329f-879e-23440a1f3fa8 | -3.23056 | -52.22853 | 2026-09-29 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c7ed78-c770-3a31-a4a2-87d33fa06851 | -3.85928 | -52.00477 | 2026-09-29 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e90d43ca-6dc4-3db2-a723-f9993021f6b1 | -5.43898 | -47.27095 | 2026-09-29 04:49:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f80f2e29-980e-3357-b64c-dcd95bec7df9 | -2.86727 | -49.05375 | 2026-09-29 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31769fda-3f74-3c13-bd61-6bfabdeba9c1 | -2.29255 | -48.58066 | 2026-09-29 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb3268c1-b794-3d90-810a-3e3c806993c7 | -0.48651 | -49.13449 | 2026-09-29 04:49:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1e2b91c-a1a2-3c0c-bf92-fe1f25cfded2 | -4.12824 | -51.05981 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff7cc51-8dbc-3143-87d4-b896fdc6f24f | -3.67978 | -47.49213 | 2026-09-29 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e9bbdfc-01c1-314f-931a-25c76584ede8 | -5.12752 | -50.71286 | 2026-09-29 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4edcc1c-340a-390c-88f4-6cbf5dc5bd5e | 1.26055 | -50.69704 | 2026-09-29 04:49:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40e28460-1eae-310f-a9d2-41b8bd4e8896 | -3.41769 | -43.16427 | 2026-09-29 04:49:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3a1baf4-a9b0-34cd-8387-0e1ec5afa02f | 1.69227 | -55.94759 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba1b8cd7-53ac-3a90-81be-2c7f71773897 | -0.50686 | -49.12285 | 2026-09-29 04:49:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c56d2a8-976e-34bb-bb4e-2df67846f21b | -3.04695 | -46.92515 | 2026-09-29 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 627640ba-4bc5-3303-8c0c-f416af4ebb74 | -5.18992 | -46.07692 | 2026-09-29 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4422eb6a-a5de-36fc-abec-e883f7e50706 | -5.86718 | -43.58851 | 2026-09-29 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10aaff6e-8405-3922-8e46-5620939edd32 | -3.53702 | -48.17675 | 2026-09-29 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32fd72a3-e40d-3822-a251-d233c21a45f3 | -4.81941 | -45.63363 | 2026-09-29 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c228daa-3b00-3163-96c3-181970592c49 | -1.43108 | -48.90934 | 2026-09-29 04:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79377c83-a30e-3e0b-9f79-b8d169b4e7cc | -7.05792 | -42.30313 | 2026-09-29 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a9922f6a-d504-3cac-99b0-a38864dfe460 | -5.36855 | -46.22284 | 2026-09-29 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b472888-8ba9-3d61-9321-41600219cc45 | 1.86876 | -55.56745 | 2026-09-29 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d41699e6-b779-3e52-80e1-48715948b8e6 | -3.42907 | -50.43621 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8370883e-dbd6-382b-8150-b918e61102c1 | -5.42289 | -43.45058 | 2026-09-29 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f0c18e6-b22f-3bf7-b715-9aa3dc7bbd3b | -0.48707 | -49.13097 | 2026-09-29 04:49:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d55d7f0-8cda-3e8b-97b1-310ae89dcab6 | -2.66085 | -51.73426 | 2026-09-29 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c721eed8-ec3e-3f20-96ff-5f53090a3539 | -3.88513 | -49.50324 | 2026-09-29 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0ce3c16-7aea-38b2-ba54-ebe743165722 | -3.50579 | -50.48232 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6c1fbd8-539e-388d-b9c9-8d21a60bae5e | -1.99618 | -47.63268 | 2026-09-29 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecae9b72-08e5-398f-a1c9-dee80d075463 | -2.57392 | -50.78674 | 2026-09-29 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f3298ee-cb4b-333d-8bdf-99dd0ab526bb | -3.1596 | -54.09836 | 2026-09-29 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d16642e-028f-3478-b745-2b30cfb5648c | -5.73435 | -43.28376 | 2026-09-29 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33a25463-2e87-3afe-bea5-4b250676a2d1 | -7.0573 | -42.06382 | 2026-09-29 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3703d8c0-5309-3cb2-a31d-fce00344a663 | -5.73612 | -45.03545 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb6c4812-d282-372b-b04f-c63867409138 | -6.12938 | -43.73152 | 2026-09-29 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb4823f3-bc53-3a0b-ba13-0aa35ffe70a6 | -3.96072 | -49.04893 | 2026-09-29 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8088c4d-f2fe-35f3-be01-99dea16b9cbc | -4.13171 | -51.06038 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf6e648e-1947-3ab7-8496-6a8f09b9d90f | -5.73444 | -45.0205 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f2eb351-485b-3fe2-b1db-282fe65caf42 | 1.8267 | -55.62302 | 2026-09-29 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52b7a64b-93bc-36e0-81e1-baef48d36b53 | -4.30182 | -48.06742 | 2026-09-29 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 595e1355-26f5-34f5-aa52-d6cc62cbb38e | -4.37561 | -40.61857 | 2026-09-29 04:49:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97015a00-dd57-39aa-aa64-b247b4871a08 | 1.67392 | -55.89578 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1af40827-e900-3936-8c32-20a0e295a45d | -3.09331 | -49.34984 | 2026-09-29 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0f54e7c-cae4-32bf-91f8-01db95ea0ba0 | -1.79639 | -47.95045 | 2026-09-29 04:49:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b06470b8-0844-330e-9046-6f8f8c3d13b6 | -5.73709 | -45.05509 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4e0d072a-0dfb-3884-9232-77bc2f5f315e | -3.41742 | -48.33599 | 2026-09-29 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 645e4df8-bd63-30ca-9432-cd32264ac13d | -6.12517 | -43.73093 | 2026-09-29 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6385bfe4-8b88-357f-be99-a89f982e4d3e | -5.0266 | -43.56792 | 2026-09-29 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f8d4572-8ac2-3633-861c-296bd39b9941 | -3.16019 | -54.09465 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 996f0091-7d06-3382-b9ed-a65d9d365acd | 1.69692 | -55.94384 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8f6eaf0-8f1f-3ff5-99a1-5e44bd6381c1 | -3.70957 | -54.22461 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3daae1ec-2e03-3e81-8a5c-58e37d702953 | -5.87141 | -43.58913 | 2026-09-29 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 494deb3b-1cd4-3670-93fe-4d687aa16af2 | -4.32091 | -48.63075 | 2026-09-29 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb58dd93-f7ae-3975-896a-30754d4f023c | -5.48388 | -45.12207 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cff1ae4b-4786-31ab-8ed0-4b34b2b4155d | -4.36201 | -47.77289 | 2026-09-29 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5f69bc3d-e44b-3227-b7d7-2a4c4b422ebd | -4.25327 | -51.04522 | 2026-09-29 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 146241d1-7c2c-3fa3-bbba-06ec38e790c0 | -5.73227 | -45.0349 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc7c5ce9-11d6-32bc-8b7d-f7f3c8771689 | -6.14098 | -44.13629 | 2026-09-29 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad73b6a1-1101-3c1e-9081-257a6d7330b5 | -5.33283 | -46.19209 | 2026-09-29 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb971377-cdcd-35f0-b61f-7cb77cc37d49 | -4.81507 | -45.63737 | 2026-09-29 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca033a2b-2edf-3944-8ed5-0a60fe03882d | -7.05654 | -42.06907 | 2026-09-29 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b600eb51-af7a-3d29-8739-47dce3dd2a5b | -5.03078 | -43.56856 | 2026-09-29 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 6d54e863-e550-34c2-b980-47791be2e265 | -4.67493 | -44.58139 | 2026-09-29 04:49:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63ed9a5f-a660-3798-952b-24d6ec17165b | -6.38167 | -45.80954 | 2026-09-29 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37a57940-2ea8-395f-849c-c57173613592 | -3.51217 | -50.311 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f90e84cf-c2ef-3d9a-9ced-f48f2c0bf26e | -3.59267 | -50.68114 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a0fe2234-b95c-3ce5-80a0-9ce07a2a9082 | -4.00194 | -38.98475 | 2026-09-29 04:49:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 85352056-d52b-3436-8fb5-a9b5170627d7 | -5.73986 | -43.27619 | 2026-09-29 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a93a0fab-c793-39bf-9c3d-3ba5daba03b9 | -3.96438 | -48.89705 | 2026-09-29 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3955f9a7-7b85-3b31-bd27-d3a963b4c29e | -6.16956 | -46.74762 | 2026-09-29 04:49:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d24c1fef-c92b-36d2-8315-a67b4999c7a8 | -4.1311 | -51.06415 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8a12955-b791-3603-9318-2caefcb34630 | -3.15426 | -54.0784 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbff93f0-fa50-3a90-88f3-246ee6e66875 | -3.51441 | -50.31881 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f1e31f5-c000-3b65-868b-7886501bbdc1 | -5.7384 | -45.17529 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6969742e-07ed-3427-b656-cb010bbe3e33 | -2.86595 | -49.63366 | 2026-09-29 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddd7ab4c-1c3c-3db6-b48f-c2589765c888 | -3.7025 | -54.21576 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ce8536b-847e-3bfa-9244-e66b3b2d7af3 | -3.72744 | -49.68296 | 2026-09-29 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6687c674-84d3-3cf7-a6dd-de3183dda918 | -1.79028 | -47.94595 | 2026-09-29 04:49:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73985a28-d6ac-3f63-a796-5a1fd4236bca | 1.82172 | -55.62388 | 2026-09-29 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fca24d85-aefa-3b0b-be4b-52f9d713858d | -2.78363 | -57.685 | 2026-09-29 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fed0c35-858c-3e9e-a451-2aef40c8f737 | -0.5035 | -49.12233 | 2026-09-29 04:49:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 659861c8-cfe3-315f-bb94-6c70f13ceaa2 | -3.0163 | -53.87028 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 578bef7a-3d5b-3fc6-9a82-5516c5ddd80e | -5.36496 | -46.22228 | 2026-09-29 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9679cb11-d95e-340f-805f-c9932b72b5c8 | -3.97638 | -47.96241 | 2026-09-29 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc4f9bb7-b62e-3459-bc0c-d099d28dc042 | -3.99117 | -49.04344 | 2026-09-29 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 581cfc3a-c1dc-334a-9533-918490794c98 | -0.48876 | -49.14208 | 2026-09-29 04:49:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1608f6e6-dc75-3988-b739-1b6be37505fc | 0.70259 | -51.43201 | 2026-09-29 04:49:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 109275c3-7403-323b-98be-8d638ecea1e1 | -2.29748 | -48.5496 | 2026-09-29 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b4d6d03-0c50-3ed7-882f-ac5fbead576d | -3.15603 | -54.09396 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f583a1c-7617-37b6-9e0f-52b029883dff | -5.19353 | -46.07747 | 2026-09-29 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2ec52f0-ddc9-3625-9e09-a4e968a3bb59 | -4.49864 | -49.64393 | 2026-09-29 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 436f3456-b269-311a-bd76-67a769ceef48 | 1.67303 | -55.88992 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)
