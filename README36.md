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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8418e01b-6b82-3641-8fa2-d2a0b07ff9c3 | -4.44411 | -49.83965 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4af9dc2-e24e-3482-9f5c-5874e08bcd87 | -3.2296 | -54.23368 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa6d3aaa-1cb3-387d-a09a-d2f5c066500b | -5.6293 | -45.3148 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87b7e61f-ebb5-3926-aa2c-7d4e41d0c425 | -3.12502 | -53.10527 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9eadcb5a-afbf-3235-87ea-728a35de97c0 | -3.79637 | -46.66477 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8c18e1e-4df7-31f2-83a5-97b66473c2f3 | -5.03316 | -45.81631 | 2024-11-23 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b00e74ac-7468-30fa-b48e-41496bc3c483 | -4.60171 | -46.4991 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 4d591d92-13c8-3157-a279-dd020cdcf01f | -3.85271 | -51.14984 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34589176-511c-330a-8f50-da68b742d054 | -5.4316 | -45.3407 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c25cb1a-a51f-325f-927c-7a9c0a52706b | -2.20256 | -53.67496 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 559c17a6-59fe-39a4-9272-00f1ef6767b2 | -4.52504 | -42.91681 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43766735-ef85-3454-8880-bfe514c3d5f8 | -4.10318 | -50.71696 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea6fbf2e-8725-31a6-97c2-7cec740b28ed | -4.15232 | -48.39837 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfbee11d-21a3-3515-8f09-75349570b113 | -3.12024 | -53.10102 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6cecc8c5-20c2-3d8d-92d9-7193219f8544 | -4.41962 | -48.30698 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8c00d76-6ae1-31a1-a5ec-d71774141793 | -4.36246 | -47.22209 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8963a94e-c132-3aae-8e6f-9beac9216fb2 | -4.47785 | -45.65177 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08e3fefa-0fdb-35e5-a4ee-8b9b06472e4f | -4.41273 | -43.96032 | 2024-11-23 04:18:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5075ebca-2863-3505-ba59-32c100baaa12 | -5.65425 | -45.20063 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b825406a-cad9-3453-b2b4-13317c95e4f1 | -5.58389 | -46.49625 | 2024-11-23 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b508785d-4925-3ee7-b496-ae221818c7fd | -4.95091 | -47.80031 | 2024-11-23 04:18:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a298ccaa-3bce-3589-afd5-235d6b92ed57 | -4.43981 | -46.45395 | 2024-11-23 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5af055a8-6c54-30aa-94dc-9dada46d67a3 | -4.12653 | -43.22733 | 2024-11-23 04:18:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88537037-9db2-327f-94ef-66c87990d1b0 | -5.94922 | -39.67338 | 2024-11-23 04:18:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c7ead08-6386-3075-b6bb-03204bb393b9 | -3.24552 | -54.24479 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 36ad572c-ee3f-3187-ba34-c0a85e276ee1 | -5.56367 | -46.2947 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9fd144e-3a72-3f50-9b82-2adf03358ccb | -3.70395 | -47.6157 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 560b4197-f546-34db-99a1-dd7968e7a036 | -6.50509 | -41.48446 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e34ab2b-e403-3444-8a3e-cb93642d27ab | -6.13646 | -44.73016 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c76b86b0-1454-3118-a56b-834b77342390 | -6.29462 | -43.4358 | 2024-11-23 04:18:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a565680a-e075-388f-832a-250a4e0e681e | -4.65859 | -45.67601 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db9ddadd-08c3-3bfc-8056-67bb819e5702 | -4.42644 | -45.76945 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 413ce5a2-b9c3-39f5-81f3-270406243ef8 | -7.07517 | -49.20845 | 2024-11-23 04:18:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e2d8462a-7d46-3f2f-82ff-f9880faa2e88 | -4.95021 | -47.80464 | 2024-11-23 04:18:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adce022f-8c47-3c13-b382-52e7a046f05a | -4.95449 | -44.31723 | 2024-11-23 04:18:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52518492-8076-3a1e-9e88-92d52b2cc6dc | -3.2456 | -54.24891 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6f71ccc-14c1-3816-9a0f-ab20273b079d | -4.07206 | -46.8436 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa21ed12-a3eb-351a-98e9-7de2c01cb9c9 | -4.53512 | -42.91834 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c999de9-3656-3b98-b7d0-3b3370184040 | -4.09257 | -51.06313 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ba7cc95-5e3b-35b6-b8b4-959ed3befca2 | -2.20192 | -53.67881 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f79d71d-68a7-3b25-ad6c-a782729650e6 | -2.82135 | -54.03708 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c8df684-b9d0-393c-8c27-a6a0db2fd3a4 | -4.10246 | -44.0108 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24f1b547-ed37-3547-8b75-6a3cac129445 | -3.17771 | -54.33034 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ff4828f5-2a68-3290-85d3-23caa150011d | -4.90744 | -48.62178 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99be4373-1b56-39c6-b26a-a2be961a21d0 | -3.21319 | -51.42745 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f05f7185-cc80-30a4-8307-8b0933f48a43 | -6.14613 | -46.68373 | 2024-11-23 04:18:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3d549ac-d71f-3ca2-84bb-9db77db01ca7 | -5.49328 | -42.84391 | 2024-11-23 04:18:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 56d836a2-b518-33df-bf4a-4e84ed4c38ea | -3.18352 | -54.33122 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd84ccd3-118c-324c-b814-31f4095643ae | -5.74334 | -46.2668 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 410e6b07-0bcc-394a-a922-b792eb70c252 | -3.22246 | -54.241 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc435e1f-78d4-37e8-8d50-e68022810319 | -6.38973 | -46.00075 | 2024-11-23 04:18:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2845f512-087c-3c04-b4d7-f898eb4405fa | -4.0293 | -46.198 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db75becc-3a65-3245-bec9-3665b5f15916 | -5.22672 | -45.11107 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36f49ed0-a620-3007-a74c-8034d7bc6f47 | -3.05887 | -53.28778 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64885894-035d-3841-932f-2995badb92e7 | -5.0789 | -44.21678 | 2024-11-23 04:18:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d39e2cd4-c434-378d-bda8-f1f5aec524b5 | -6.69961 | -43.95264 | 2024-11-23 04:18:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 242f478a-0e63-3499-8175-9af24e40e686 | -6.16346 | -44.42644 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb4193bc-4406-37d2-b270-e6e148b246c8 | -3.24993 | -54.25394 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d32b13ae-5af7-3d9b-b874-cde4aef3cf00 | -3.66525 | -51.57366 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1d8b9a2-dbc7-3272-b5a7-905914ee6c14 | -3.96079 | -46.72508 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d71a506e-5a56-3eeb-9a3c-71f7dd260b5a | -6.27063 | -44.54618 | 2024-11-23 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8583d25-377a-312c-9820-f0981f875ea2 | -3.82215 | -51.21962 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 633ea9ce-3edc-3658-8427-2ab3cdf5b5ee | -4.10452 | -42.47027 | 2024-11-23 04:18:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8dac0b19-7340-32c1-b7d9-77cc68bb8498 | -8.71407 | -44.01215 | 2024-11-23 04:18:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4320d411-b364-35d2-bf8f-00246fb1dec8 | -4.15863 | -43.82561 | 2024-11-23 04:18:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0337704-2799-37dd-b459-329ea1f29289 | -5.29334 | -44.86193 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| c3b1780b-81df-34db-8f84-8ca92f6a0199 | -4.47727 | -45.65538 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e399264-e025-3f87-a085-e566c48ad8c2 | -3.22104 | -54.24946 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0f15b2a-98c8-33ba-959f-80312e88859a | -5.56254 | -43.31946 | 2024-11-23 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1fe3537-1726-3b58-b1bc-ca715dd1a38b | -10.58232 | -36.98794 | 2024-11-23 04:18:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 15d7a226-5417-3ce4-a8f4-f316ac64807f | -3.80146 | -44.92942 | 2024-11-23 04:18:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d35cd975-c072-3ea8-b63c-bc5669fad7b6 | -4.44516 | -48.19694 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 78a6bf3c-d348-3b37-811c-a4a02c165bb6 | -3.80654 | -51.34315 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21bbb16d-7039-3a1a-b4e0-091b5a7cda63 | -2.92864 | -54.28702 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c42d3346-3a65-3eb1-94ec-b7e3f19e615b | -3.84927 | -52.35619 | 2024-11-23 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec1a1f25-183f-3178-b73a-f06ee8ca2953 | -4.03521 | -48.93769 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caa782b0-0d9b-3d13-a2bd-bcf9a7324d50 | -4.53523 | -46.43397 | 2024-11-23 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd6d3dad-71c5-3585-965d-37713ac3498f | -4.68918 | -44.40632 | 2024-11-23 04:18:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 842f59a0-4f8f-3678-81fb-fa3276efa085 | -3.99586 | -46.93476 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 525c3114-02ed-3724-b569-1cc44caef8d2 | -5.13018 | -41.5578 | 2024-11-23 04:18:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6643991f-9507-359c-a008-56b79079de34 | -4.66253 | -45.67292 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16d18646-82a8-3831-ba60-4b25fc4a1eb6 | -6.05651 | -44.04836 | 2024-11-23 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb8ac639-4843-338c-a5df-68fd1d448333 | -3.91175 | -46.53431 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e695f1fc-3af6-31dc-891c-86120a6d24e6 | -4.6358 | -49.54285 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c6ff6b3-d5a8-3310-94a1-3e41d2ed5390 | -4.2359 | -48.67327 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f9b86b2-5b7b-3c7d-87ce-b02573c30a04 | -5.75415 | -44.48249 | 2024-11-23 04:18:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bc08e5e-b409-3baa-9850-2fee1d966dfa | -3.84423 | -52.35541 | 2024-11-23 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35c53ef2-1756-3d6c-be68-dc1dc16bd144 | -6.64012 | -41.43774 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9ee9dab3-3c38-35ed-8fdb-0bcb4106e905 | -4.25692 | -48.69178 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 34864bca-9bc2-3b32-b1de-cc99d41bbed5 | -4.26622 | -46.29187 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d27dbbb-4492-341f-9edb-6f8663f48cb2 | -3.22822 | -54.24198 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cfcc058-fca9-38a8-b231-ba46f96f49c5 | -4.48064 | -45.65591 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86d03e06-2367-38aa-821f-cdbad573eef0 | -9.12962 | -43.10644 | 2024-11-23 04:18:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d7d1313-874d-367c-8fd9-3616e11d5e15 | -4.56852 | -38.48352 | 2024-11-23 04:18:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a9f81ba-2f09-3041-b50e-9f19773b5476 | -3.80288 | -46.60178 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 073e8537-cd2b-3d73-9510-b54769ff692c | -5.65747 | -43.363 | 2024-11-23 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa4b3c17-7c54-339d-9386-cb1a1a53efa8 | -6.08823 | -43.54132 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1e884f9-51a9-3d70-a1bb-f643251b65ca | -4.07687 | -46.83625 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd89888b-d1e0-3d27-a029-b351aed29d30 | -3.22545 | -54.25856 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a70a00c-86cc-35c9-b017-c27946dd65dd | -5.32575 | -44.78552 | 2024-11-23 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README37.md)
