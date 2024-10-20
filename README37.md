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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ae7f778-4077-3b4a-85ef-c0b2d24a50f2 | -3.67704 | -49.79468 | 2024-10-20 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fb23dd0-c896-3b9c-b7bb-0c9906c1b4b7 | -3.6735 | -49.79411 | 2024-10-20 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f567f15-412e-3c3f-a99e-119073a2fca7 | -3.63808 | -49.83364 | 2024-10-20 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 302aafba-a9e6-3614-a8a8-aad43e0176ac | -3.60927 | -50.58762 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8cd5b1a-1231-3360-bd46-00b99e3335a0 | -3.60629 | -50.58274 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1dcf21bd-f7ad-31c0-99df-21d8f0db1c58 | -3.60559 | -50.58701 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1945f74-97a6-3fc4-a5e3-a37b2e41a8a4 | -3.60261 | -50.58212 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e57a3f6a-a487-3092-a65b-78c3ae1fe09a | -3.60191 | -50.58639 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea94e4d9-28e6-32b1-8ff7-5757564725c2 | -3.59852 | -50.59195 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e99e73dc-4308-3268-8bb7-e7cab97eb0a6 | -3.59753 | -50.59006 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 403d775c-dc63-3b70-8905-5d119c2cfc4e | -3.59682 | -50.59438 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91198974-9e30-3511-850c-572a39d14a16 | -4.48191 | -50.45131 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93859e0f-22bf-3df2-822b-5da979e16026 | -4.47901 | -50.4502 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c294be0a-28de-3ae4-93d5-b66ee856b298 | -4.47833 | -50.45434 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 434638b1-deb6-3566-b4c2-4db97918b774 | -4.47829 | -50.45073 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfad8250-d285-3091-8992-60a70dbd2c59 | -4.47039 | -50.4537 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24831ecf-1244-3214-9896-8eb16bdaa51f | -4.46756 | -50.3554 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59ebb463-05cb-3b87-a16f-bb584e822f3f | -4.46677 | -50.45311 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7347387c-1c89-3bca-bcca-2c5880ce17ad | -4.46433 | -50.53856 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f1aa5c4-efce-30eb-b933-a5f171c63338 | -4.45889 | -49.62185 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7edc22d-373b-391d-ae13-04112da28018 | -4.45712 | -50.07881 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fbd81d3-928d-3270-9e5c-1dfe277934c6 | -4.44071 | -50.68719 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 595a4bfe-c842-3949-8a94-03c1de5fcfb6 | -4.43713 | -50.45259 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f6aff27-1cce-302c-b564-7c4273149570 | -4.40908 | -50.53396 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e04adbdd-6d37-38cd-b6ca-bb7cefcd5835 | -4.39863 | -49.75091 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16191a11-d9b3-3437-bb09-bfadb94db69e | -3.96049 | -49.89411 | 2024-10-20 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e526d26-b0ff-316c-a7c1-f872faad2a96 | -3.94141 | -49.47211 | 2024-10-20 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18ded57a-7994-3193-b534-b87d9e694e65 | -3.89906 | -49.98772 | 2024-10-20 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| faa7df67-2e16-3dfc-b5aa-ba0b777e6c87 | -3.89842 | -49.99174 | 2024-10-20 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6003d6ff-03d2-3104-a647-5572069a2834 | -3.87968 | -50.01768 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15cbe12d-5a7a-3987-9665-6a46272e82dd | -3.85571 | -50.07607 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dfd73aa-d98d-3a69-9251-66168dcc44bd | -3.8551 | -50.68574 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4145b33-1a3c-3c02-abaf-fe1af23f00a0 | -3.85213 | -50.0755 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a7a6982-84c9-3466-8057-72e4234c8790 | -3.85141 | -50.68513 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53c19d5a-99e5-3aa9-bd2d-4b450bbb72e5 | -3.82104 | -49.95042 | 2024-10-20 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6255aeae-aec4-369c-8f7a-3923e0dafb63 | -3.81504 | -50.65257 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b50c3836-8426-3530-bfea-5c55e5190604 | -3.76547 | -49.98825 | 2024-10-20 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efc4761b-8e57-3873-8b86-13114c186097 | -5.01665 | -50.8372 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f995fb51-4f54-3911-897d-0c96a2616fb2 | -5.01595 | -50.84148 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30dee1d9-5d49-304d-a7db-4f975b5fc0f4 | -5.01298 | -50.83662 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0ada831-c662-3695-a0b4-7eae9559237c | -5.01228 | -50.8409 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4206bf7c-752b-359a-a487-031dfcc34ded | -6.5113 | -50.2552 | 2024-10-20 04:32:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8825a62-0862-331f-b369-090d6e52440a | -6.21792 | -50.88542 | 2024-10-20 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b83f83cf-de80-3dd8-a6d9-5916b9c0ccc4 | -6.21724 | -50.88964 | 2024-10-20 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7d15b08-f708-3532-85fd-9f5ae8ba6718 | -6.21361 | -50.88908 | 2024-10-20 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e68ecac3-4187-35e1-88db-eb1b288c9d9b | -6.20998 | -50.88848 | 2024-10-20 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0766cfde-bfaa-32d7-b013-84c9981d69db | -6.1939 | -50.87297 | 2024-10-20 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04527336-7114-3324-8872-fd49c4fabdaf | -6.19027 | -50.87241 | 2024-10-20 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dcbc6ee-ca56-3462-af25-d6368df09407 | -6.18664 | -50.87186 | 2024-10-20 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 892bb0a2-c0a6-3a01-8e12-37c4bac1ca88 | -6.18233 | -50.87542 | 2024-10-20 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d89434f-3b3a-3b47-95ce-c64226d609a6 | -5.86214 | -51.07596 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 065d7fc5-67da-3e75-a2bb-41f88df22187 | -5.86144 | -51.08027 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d258830e-8196-3b02-a5b5-22e1b801ee81 | -5.86074 | -51.0846 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d73b036-0f42-348a-b236-dd922d777907 | -5.85846 | -51.07535 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f06cb97f-4eca-325c-b027-8cc544e493ac | -5.85706 | -51.08399 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cb88af9-c2ef-3c4f-9b2e-2b05f166b560 | -5.85478 | -51.07475 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f26fd707-6d36-38d5-9a67-8d18e8292ce7 | -5.70166 | -49.86023 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dddcdb9d-db55-3c91-afe9-a223d0e825d6 | -5.5787 | -51.09143 | 2024-10-20 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 313c9502-bf91-3e75-939c-bc27e68fce23 | -5.54627 | -50.97674 | 2024-10-20 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f21d55d-520c-3f40-b704-5cb4fc22e8f8 | -5.54422 | -50.16266 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe539aff-9d1f-3ede-9377-bdb088c79453 | -5.51199 | -50.58802 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b660e327-2d36-3f8e-a344-57b6491036cb | -5.50906 | -50.58331 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef72ae42-d22f-31ef-b5d2-00a8c14b7742 | -5.50839 | -50.58743 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d221990-989f-35a0-b741-1f800e7ece4a | -5.50772 | -50.59157 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd7cd269-c84d-309e-959f-bbec1cfe4a44 | -5.50479 | -50.58685 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dced4b4-f28e-3fc0-b8a9-c5fa67dddd71 | -5.50412 | -50.59098 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f1c1f24-f711-3b1c-abc5-6a3e3d3208df | -5.50118 | -50.58629 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c08c47b-3781-3b60-87e9-37e8fa2e8fbe | -5.50051 | -50.59041 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c3055ba-adb0-373f-b912-19d017ded054 | -5.49985 | -50.59454 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df4a1f3-3d5d-3315-85ad-d3a8448f4761 | -5.49758 | -50.58572 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45bcb988-0f28-3546-a2ef-aa2f67315c59 | -5.49691 | -50.58984 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7279e7cf-88c6-3cfd-b984-36b1396583e4 | -5.49331 | -50.58926 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d06f5e5-7024-32fb-a50d-7b62e985d1f4 | -5.47773 | -50.54871 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4d9aa56-66cb-3f26-b4a6-c5b9a7389ad8 | -5.47616 | -50.53576 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b4a4a94-a01e-3cb0-85f1-b4ec0fc60dbe | -5.47548 | -50.53989 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b409c318-1032-3ee8-b79c-760083714f1d | -5.47413 | -50.54814 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5e1ef49-5c93-3707-8ef8-4e6676dc1720 | -5.47256 | -50.53519 | 2024-10-20 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d912cc55-b033-37ed-8148-e2a6903c204f | -5.36937 | -50.91997 | 2024-10-20 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f05e0df9-8931-333f-bd6d-b39e3e524ca3 | -5.34354 | -50.98669 | 2024-10-20 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1876f07f-722a-3616-a16d-17bfd9994ee3 | -5.26514 | -49.51728 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 231d4da0-fe80-3c0b-9e5a-387df064738a | -5.21252 | -50.00706 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8361f4e8-4ea5-3418-b626-ceef7cec625e | -5.209 | -50.00649 | 2024-10-20 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aa1dd36-ae0d-3648-bd0d-7c6bbfe78d09 | -5.1636 | -50.71482 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6060df40-d0ae-30a5-a71b-ebd5d09b8bcb | -5.16291 | -50.71914 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 68f81ad8-4828-34b2-bee6-48737b7aef28 | -5.15994 | -50.71434 | 2024-10-20 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 07188453-b652-358e-9f36-215bfe533c36 | -3.42378 | -50.65459 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90cbffda-83ba-3172-ab39-61bdc4f48a23 | -3.39657 | -50.79985 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ce7a9fc-cb34-3742-86c1-5e020cba51a0 | -3.39585 | -50.80428 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cc646ba-6f5a-3212-8c6e-eae070a11e51 | -3.39283 | -50.79925 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56a1d86b-2ea8-32ae-98cf-4a5e25f10716 | -3.39212 | -50.80368 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 239851ad-92c7-33e6-ba95-729bf0390d3a | -3.39199 | -50.66296 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 494a464d-98fd-346c-984e-7b8afa550f19 | -3.39127 | -50.66738 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9569a880-e9c9-3a6a-b959-c07cf3fa57eb | -3.39055 | -50.6718 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 31f4ff6b-9a22-3f3a-9cc2-7a1c64a0135d | -3.38827 | -50.66238 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 0a351e93-7abf-3711-a4cd-3707a53046c7 | -3.38755 | -50.6668 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 25470b8f-e323-3fc1-90a8-ae3be8a30961 | -3.38683 | -50.67125 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 013c4186-e330-3dcd-9fe7-2a7a1b8bd572 | -3.38612 | -50.67562 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ba539532-cb4c-38fd-bdf0-3935bee277cc | -3.38384 | -50.66624 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| cb78f706-2529-3dce-9f92-6c6563631a6c | -3.38311 | -50.67068 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d1188e0b-64ed-34ce-8a13-bf93f4f8f869 | -3.2795 | -50.66479 | 2024-10-20 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README38.md)
