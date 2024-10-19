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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3adf2645-4cd8-3aa7-81e7-a7767bd22e36 | -3.05272 | -49.41565 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21900624-5e83-3f43-98e8-5a084277fdb8 | -3.04798 | -49.4116 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98f0b44a-029e-3426-805b-8a1e00209dfe | -2.84098 | -49.53865 | 2024-10-19 05:14:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c89bb66-335d-3d40-bcb9-8bfed2dba5b9 | -2.83537 | -49.5409 | 2024-10-19 05:14:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 625d50d6-7c49-38a8-82aa-0202ea3d9598 | -2.77546 | -49.32909 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1e966dd-66fe-37ea-9c19-7be2f240ef56 | -2.77499 | -49.33225 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8de88476-5c1e-389f-957a-0a09db1083de | -2.76458 | -49.36608 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ae957d51-9ace-33d6-b6cb-705dd7ce143e | -2.71403 | -49.16833 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9ca1b55-a9d2-3e68-b397-e2aea048c962 | -2.70925 | -49.16422 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 22fa576a-342c-30aa-830e-2decfe1be99e | -2.70875 | -49.16752 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b02f8675-ad31-3254-9736-450598bda018 | -2.62658 | -49.07213 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04cca955-cefa-3a2e-9964-b9adeab72a22 | -2.62127 | -49.07133 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcba72a9-48c5-3eae-85f7-4aab2f5a1b8e | -2.57114 | -48.9481 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b7f2aa9-922b-3674-8612-2ef85b30bf2b | -2.56941 | -48.94464 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e82b2a17-2262-3be8-89c9-2f2465a0f15c | -2.56892 | -48.94799 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af53d60a-57ca-3cdd-990f-729f9208e1e0 | -2.56632 | -48.94393 | 2024-10-19 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35c92257-5d47-3833-8ef6-4e5ad5522de1 | -2.35757 | -49.35717 | 2024-10-19 05:14:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c931440-da88-3914-99ce-d708e4154601 | -2.35709 | -49.36027 | 2024-10-19 05:14:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 448c11af-20d3-36f4-af6e-1648c7f18662 | -2.34764 | -49.6601 | 2024-10-19 05:14:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f39741a1-72f9-3cf1-bdd2-d92e75f42cfc | -2.34718 | -49.66306 | 2024-10-19 05:14:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d662ce72-b93a-3c3b-b23a-69e5e1ff2c93 | -2.34603 | -49.66161 | 2024-10-19 05:14:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 136d1cf4-e7df-314c-ae67-9cacd8a1e722 | -4.59819 | -49.51988 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acdd129d-f513-31ea-8a64-df04fda93ff5 | -4.55616 | -49.65976 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f25ffe71-39cc-3994-867c-b730a898219e | -4.55138 | -49.65578 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa4d415-5669-3908-908e-e05ed14aac9d | -4.5509 | -49.65906 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b25c5c4-74e2-313f-a09e-86c673907eb9 | -4.44768 | -50.15427 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d431d7e-7734-3975-b49b-bab29567a72b | -4.44725 | -50.15723 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 388bd8ef-0f8f-3957-b14d-c61910f5d3ed | -4.39847 | -49.74935 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 970fbddd-e832-32dd-b4f7-8120efc71964 | -4.32382 | -50.81281 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a5bf707-52ab-3d7d-8622-423a3f7b2573 | -4.32338 | -50.80962 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 056f93f2-b2e0-3a45-a341-0b8fa1b462a2 | -4.32262 | -50.81495 | 2024-10-19 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7aadb87b-faaf-3652-aa98-46b8a694167d | -3.70367 | -49.83195 | 2024-10-19 05:14:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c9722e7-73f8-37a5-a04e-2e8497451028 | -3.70322 | -49.83495 | 2024-10-19 05:14:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3f21251-880d-3c1e-840f-0975056f799e | -3.69855 | -49.83115 | 2024-10-19 05:14:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f3287a9-b7a9-3bf7-b8c7-5b11fd2bd30b | -3.87454 | -50.26265 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23570d32-084a-34b7-a5d3-bbad751c16e0 | -3.87434 | -50.26149 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71d1b5d8-50e6-3442-ba4a-04593c602598 | -3.87413 | -50.26549 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90ecec6d-ae16-3277-b438-895054562db3 | -3.87391 | -50.26432 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a6741cf-6014-3a88-b8fe-ac66bb90fb18 | -3.60459 | -50.58612 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a35b8356-53b0-38f2-9f69-2520490833e5 | -3.60271 | -50.58741 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c1728144-51b3-3252-9586-be6e38b1ecd0 | -3.59971 | -50.58554 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5117d52e-ea57-3aff-92d5-136e9b2df8c3 | -3.59889 | -50.59093 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 062aae41-ba8c-37f1-b4ff-f45c866df6d8 | -3.59783 | -50.58684 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a4047f4-a984-3cb4-b829-ba665474a035 | -3.5976 | -50.1623 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 647fd232-7364-3554-acc9-97c9ff450796 | -3.59718 | -50.16516 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec8d066c-2e02-35be-ad89-5e7a5703a83e | -3.5868 | -50.5725 | 2024-10-19 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b4ad4a67-3387-3c39-8369-f28f0a2300d9 | -5.5098 | -50.58989 | 2024-10-19 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f47fc8b0-9d6b-3705-afef-4a19f7e78cad | -5.50522 | -50.58629 | 2024-10-19 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4257471c-b543-3e19-9c2e-0bae73d70670 | -5.5048 | -50.58915 | 2024-10-19 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c7a9023-d963-3b85-add4-6ed0a6cfa940 | -5.50439 | -50.592 | 2024-10-19 05:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df8780ff-ee9a-3a24-a79d-1de785905b5d | -5.0332 | -50.45563 | 2024-10-19 05:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a4f7b4f-1040-3ccf-961d-626d604b8bfd | -5.02829 | -50.45297 | 2024-10-19 05:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 321d3dcc-7d34-3e4f-9a2e-453194ca9699 | -5.02819 | -50.45492 | 2024-10-19 05:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4adef91e-c0f9-35a1-884e-810f32b6aa1d | -5.02786 | -50.45584 | 2024-10-19 05:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c71bbfb7-39bd-3164-9c94-bdc9964685ec | -5.57876 | -51.04934 | 2024-10-19 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4157bde0-d77c-3a75-b50e-ac32393ffb83 | 0.00369 | -51.22165 | 2024-10-19 05:14:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01acab4e-78a9-318c-baf6-878d96caef85 | -2.16158 | -50.69971 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41929e58-f6fa-37ef-a7a3-c1291c7f17bb | -2.09616 | -51.43753 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89435191-9232-3fb6-820c-702b007d9040 | -1.58741 | -51.7027 | 2024-10-19 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf831780-a351-32d2-afbe-3dda49865770 | -2.89183 | -51.68348 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec700a09-45a0-3429-9d64-5042a92c0fae | -2.89115 | -51.68787 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7813623a-87eb-3a49-8cc7-edbb0445c386 | -2.8781 | -51.65433 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9437d44a-21c6-342e-8808-046c98f9055b | -2.87457 | -51.61767 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68102944-8718-37eb-bfbc-566946e0dec6 | -2.87389 | -51.62211 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe92a83-1253-3619-8749-b98e94d4541b | -2.87027 | -51.67573 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe731815-a417-357d-bf43-aa2df96729ef | -2.87012 | -51.61693 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ffbbbb6-a745-3644-b023-dd836df35d9e | -2.8604 | -51.28083 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04b98fec-762f-3072-a3d8-15b65da682d1 | -2.85971 | -51.28549 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f516377-d2e9-337a-9f8d-2225801c100d | -2.85966 | -51.28447 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94bb841f-c8ea-3685-bfb5-b1e5392ed989 | -2.85894 | -51.28912 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1e77679-1b0f-3b12-8fb5-40b43343fe0c | -2.8378 | -51.30495 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6ee09a04-8c19-3979-80c2-20b14bb6ad67 | -2.83709 | -51.30958 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ceb89d51-20c3-383a-99c1-131968aa75b2 | -2.83324 | -51.30423 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9ca0fc4c-0f49-3c2c-997d-c9fab2d3e021 | -2.82158 | -51.3498 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12e73fdc-c167-35ae-9e83-020966c46042 | -2.81845 | -51.3399 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc3d607d-d4f5-383b-b6ee-87edf5b9ea0b | -2.81774 | -51.34453 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f947c21-6c7d-32ab-8630-fdadf6148ee9 | -2.81703 | -51.34912 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 367c18f8-e77a-3db2-9516-da34eba43daf | -2.81319 | -51.34384 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22a239b9-3c6c-3776-92e2-1832e8325593 | -2.81249 | -51.34844 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83b87574-2091-3b26-ba2a-dc36114de9b7 | -2.80794 | -51.34774 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5efae0ae-8019-38b5-92c2-d94ce955d541 | -2.80581 | -51.60123 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a582c13-c980-34bc-abe6-042db2820cbf | -2.80378 | -51.60228 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f052a49-0fd9-3ed4-9692-35b5f7c2b361 | -2.80312 | -51.60675 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b54826d0-60fd-3be1-aca5-0c74d8372a34 | -2.80134 | -51.60057 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f06b31d-187e-3676-b0a3-2e6c9fe1655b | -2.80064 | -51.60506 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7849d7ce-d3cf-3a3d-b408-48100d658265 | -2.79931 | -51.60162 | 2024-10-19 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3989a13d-2756-30bd-b393-44d5ff03f82b | -2.79676 | -51.36015 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0ec181bd-a643-3d5b-8994-2fc3fb9b6be6 | -2.79606 | -51.36475 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7002c262-4c2a-3429-b978-bce3296edc35 | -2.79221 | -51.35947 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b311b0aa-9b50-3f8b-b578-cdf516449078 | -2.79152 | -51.36405 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b3a8a710-f908-3df6-8442-d15fdfb9f40b | -2.74239 | -51.62789 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78ab58a7-4f28-3ac9-aed0-ed04ffd75234 | -2.74173 | -51.63229 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cdf423d0-c91a-3927-ad7f-7a669858cfff | -2.73794 | -51.62721 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c400812-98fb-31f1-9509-6c82b6dbde09 | -2.73727 | -51.63163 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc0fc746-fa6a-32f0-a069-4085ccfa4a8a | -2.70521 | -51.34335 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b27fe581-1a77-38d4-9847-c611bc738c91 | -2.65514 | -51.84545 | 2024-10-19 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f2b1513-61ae-3c9d-90ca-afb6e0ef830e | -2.62298 | -51.76229 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 758c8f09-594f-3e55-9bca-386801bfe5fd | -2.62233 | -51.76656 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cbb83f83-83fd-3441-8e04-1f430977d10c | -2.55215 | -51.24258 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9813156-c085-313c-b531-ea33bad8ed8f | -2.55145 | -51.24728 | 2024-10-19 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README40.md)
