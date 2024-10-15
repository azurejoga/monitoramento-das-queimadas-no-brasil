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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6f8490b-3a4d-35bc-9f42-525798b4e447 | -7.43502 | -42.98671 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78b4c6a9-4b27-3272-a54c-2663961fa8f9 | -9.41715 | -44.15051 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5725e9a0-3621-3ffa-b68e-5abb34632dff | -9.41479 | -44.16655 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34dce855-e1ae-39ac-8da2-6bb101f9b913 | -9.41391 | -44.15109 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b91fe82c-65d2-32c3-9b78-2773d47bb16b | -6.39696 | -39.90792 | 2024-10-15 04:25:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a5056ac3-d2bb-33d9-af21-7a50e9b2bbad | -6.39635 | -39.91224 | 2024-10-15 04:25:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42f8e813-dc02-318d-a596-312a85373f85 | -6.39574 | -39.91648 | 2024-10-15 04:25:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1141cd5e-db96-3ecf-9480-818fb1d792f4 | -7.51785 | -40.51212 | 2024-10-15 04:25:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d86e7de-1db2-32a2-bfa7-ffd2b25a4bcd | -7.24937 | -39.85238 | 2024-10-15 04:25:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 35f0fcd6-b182-32c2-bc09-29a5d492c464 | -8.24304 | -40.28886 | 2024-10-15 04:25:00 | NPP-375D | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da3902d3-99b0-3a67-a455-8f629d44dc0d | -6.39801 | -41.61134 | 2024-10-15 04:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d772e00-eb67-3022-9844-ccb9a5c25937 | -6.39729 | -41.61618 | 2024-10-15 04:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25da0be8-f626-3cbb-a918-1a567263c5ec | -6.39657 | -41.62104 | 2024-10-15 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea334718-b2f9-395d-af13-78e89754882a | -6.39584 | -41.62595 | 2024-10-15 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c3f9327e-d6dc-3812-8011-e4724bdb682e | -6.39087 | -41.60543 | 2024-10-15 04:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 99e0a728-a6a4-3bf0-982a-1d0f11239e46 | -6.39015 | -41.61032 | 2024-10-15 04:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| cf39c14e-04b8-37ce-bd41-33a328c7b734 | -6.38621 | -41.60981 | 2024-10-15 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6ec7d706-f2e9-3e70-9a87-383d6c9e5aa0 | -6.37344 | -41.58765 | 2024-10-15 04:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2676afd7-bbe1-389c-9a3d-d8a1882470fa | -6.36952 | -41.58702 | 2024-10-15 04:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 353ae540-103c-337e-9e0f-db7859859894 | -6.36879 | -41.59201 | 2024-10-15 04:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e3005660-52aa-3db5-af05-6e546bcbb41f | -7.55126 | -42.23783 | 2024-10-15 04:25:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f238b350-5e56-351a-84cc-d812dd3abb57 | -7.55058 | -42.24257 | 2024-10-15 04:25:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aef238e7-641a-3d24-8882-a519c872afba | -8.13742 | -42.34033 | 2024-10-15 04:25:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7ff8d764-d11e-3721-8712-1bb8749f9b97 | -8.13288 | -42.34452 | 2024-10-15 04:25:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 13ea9976-b622-39db-bfae-145b1fea2bea | -8.13218 | -42.34921 | 2024-10-15 04:25:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e4b0c848-9f0a-352e-a43b-44146d197a44 | -6.5723 | -42.0984 | 2024-10-15 04:25:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 14469cb6-c689-3880-9fe2-0513be0220f1 | -6.33599 | -42.6702 | 2024-10-15 04:25:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3178a6d5-4680-3917-998c-f2ff5916389d | -6.29385 | -42.62402 | 2024-10-15 04:25:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8f82ea42-fbe2-3a62-82a2-0ad9fea0ad73 | -6.2922 | -42.62152 | 2024-10-15 04:25:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf2b9503-e225-32d4-a4a5-6a8d61d6fade | -6.28746 | -42.60314 | 2024-10-15 04:25:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 20f50a8f-4079-39fb-bffd-4c0a9779c442 | -6.06358 | -42.25219 | 2024-10-15 04:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da0cfa0a-6b15-3ff2-9a70-f6dfac438dfc | -6.45154 | -43.11688 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f4af16f-aa2d-31f8-bb0a-0ae31cb4658b | -6.44793 | -43.11634 | 2024-10-15 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1d2b36eb-5e8a-3e80-a4a8-18f042bb640f | -6.33113 | -42.97373 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0e124d4-6749-35f8-afee-3c847ba1d002 | -6.31238 | -43.37566 | 2024-10-15 04:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b82356a2-22b9-3473-a128-45fe6df13113 | -6.31178 | -43.37966 | 2024-10-15 04:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63f05eaa-242a-36b2-9ff7-ddf491ace825 | -6.28947 | -42.955 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c79a90f1-4c30-3802-a51c-46378e6abd1f | -7.95327 | -42.67536 | 2024-10-15 04:25:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 63f0abef-a7f7-3042-8687-cb8aba10e8f7 | -7.94952 | -42.67475 | 2024-10-15 04:25:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5be8335-5dbc-384b-b1b9-1a51dbd52437 | -7.76558 | -43.31124 | 2024-10-15 04:25:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| abede815-2794-3d65-a287-03ff98473879 | -7.76259 | -43.30649 | 2024-10-15 04:25:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd1fe31f-50c0-32e2-ad01-a079eafd18b2 | -7.76197 | -43.31067 | 2024-10-15 04:25:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 170b896c-4b00-3dca-970c-f2f31df3b1f5 | -7.7596 | -43.30177 | 2024-10-15 04:25:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 79d029c8-a1c1-3e77-98a4-676583580458 | -7.72972 | -43.20288 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ebe0d21a-107f-37c0-a38b-8272443cd443 | -7.7291 | -43.20712 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0cf6b7f5-8acd-3dbb-a779-fae168ac2f4b | -7.72848 | -43.21132 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dba07a90-7d2e-3da7-8c1f-dd84939188cd | -7.72786 | -43.21554 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f9f5979-38ae-3d75-ab47-48cfc32d0599 | -7.7274 | -43.19573 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 24dcd48a-2e6a-30c4-97a0-f3780695b9fe | -7.72734 | -43.19376 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25f5df1d-5e5b-3438-bc79-6747276fe9a9 | -7.72724 | -43.21977 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e1260087-45b7-3ce5-bb5e-eabfc36ef90e | -7.72675 | -43.19999 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 10015ded-7459-3df8-9362-c785a5988827 | -7.72671 | -43.19805 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d54a2788-723a-329e-b22b-38a8ae90bdb6 | -7.72662 | -43.22398 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ec19c1ec-c69f-3265-b5c2-e447e974701e | -9.44901 | -44.15537 | 2024-10-15 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fda5ec5-1c9b-328b-9a43-ad0a4b57b877 | -7.7261 | -43.20425 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bd9b7727-6600-3178-9d1f-6ce863729e0a | -7.72608 | -43.20232 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4bfa080b-8eb3-35b0-b23a-81db8df73450 | -7.72442 | -43.19089 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db0c8082-569c-3622-982a-023a8f958c00 | -7.72377 | -43.19516 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b7049a83-b41f-329a-b8e6-50f92d2789ca | -7.7237 | -43.1932 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| efb5f055-6aa3-3494-9658-3ee2a6667b5f | -7.71161 | -43.27485 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab1e607e-e9d8-39ca-a5f1-64092e4afa17 | -7.70926 | -43.26595 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6e77e93b-8c40-373f-8ba0-477afc198566 | -7.70896 | -43.26834 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 74d4d77f-c4e3-3376-bbb5-d3c4123351f6 | -7.70799 | -43.27428 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| abc79f11-e9f8-3e30-b7d4-3be12725730d | -7.70773 | -43.27668 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 69cf16b2-d5f3-3bf2-a598-c82ccb5e0c3a | -7.70735 | -43.27844 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 673ae5fa-c511-3735-acdb-e6897112b285 | -7.69722 | -43.17374 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ed2bda80-dd81-3a20-8c8b-3aca3cdc7c64 | -7.69476 | -43.26368 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c47b1bad-fc08-3a17-9f3d-6f26268601d4 | -7.69413 | -43.26785 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3cb3e2cf-c7cf-3c5b-a8f1-0612016d9e3c | -7.69293 | -43.17744 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e94e8cab-d4cc-3612-830b-213828fb1c9c | -7.69229 | -43.18169 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 42183856-7d29-389d-be5b-efaae39ee8a8 | -7.69177 | -43.25893 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40da1f1a-334e-396c-9807-647a0949cbcb | -7.68866 | -43.1811 | 2024-10-15 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb50d503-bf6d-3a66-927e-73945dbf7af5 | -7.44083 | -42.99446 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0390a65b-9f05-37b2-ae54-b59e42e4bf1e | -7.43894 | -43.00727 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 072bfb07-9876-36d3-a7c6-81afc2414378 | -7.43832 | -43.01151 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 82cab180-419b-3ad5-8405-2077f5074294 | -7.43778 | -42.98969 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ec956bb0-3eac-336c-b8a7-ef35de4abfc2 | -7.43769 | -43.01577 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ebd345a-05aa-3dca-87c4-d65b4910cd6e | -7.43568 | -42.98241 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2f1879a4-afea-39bf-8ae5-e8144503b3ef | -7.43537 | -42.98056 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aaa52db3-b941-368d-90a7-41b26ff5e714 | -7.43474 | -42.98487 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fc2daaf4-12bb-3728-ad10-564d6e0ffd6c | -7.43201 | -42.9819 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd8dc3e5-243c-3649-9532-5913a6939b8f | -7.42251 | -43.01958 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c2c0ead8-7832-3c50-8be8-ad9e5422bce3 | -7.41841 | -42.99729 | 2024-10-15 04:25:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee8c017e-4e5b-34cb-95be-105c89c7960e | -7.182 | -42.62985 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a86fb1bc-fea6-3db4-bab2-b84e767a7f1e | -7.18134 | -42.6343 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 905f1cd1-e67b-3c45-92ff-3841e47af674 | -7.17892 | -42.62485 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ae4ecf36-56d5-3430-944a-266449020025 | -7.17781 | -42.60645 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4b129569-bb0c-3faa-a3c1-8bee3808bd63 | -7.17696 | -42.63818 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d06f46f3-d3ee-33f2-883c-89d7ba160208 | -7.17565 | -42.6471 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a799953f-5157-3187-83f2-bbea613b5309 | -7.175 | -42.65149 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3072036d-8a48-3c42-80dd-c994a91fbfed | -7.17473 | -42.60139 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 537949c7-4038-3f6c-a04c-4f80aa030c78 | -7.17063 | -42.65531 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 91133f85-9090-30bc-a54b-0d69f69b9964 | -7.15946 | -42.65361 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 444745fd-f58c-35e6-af90-37ac8062ae3d | -7.15877 | -42.65127 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d0ba7d51-f82a-38a4-b3ec-c9b130843adb | -7.15639 | -42.64859 | 2024-10-15 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95e54267-9077-300a-a89d-1c075a456527 | -7.14484 | -42.56692 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f466c130-050d-39fd-abcc-60307a45c5eb | -7.08597 | -43.03014 | 2024-10-15 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fdd881cd-e498-32c5-8574-b8b333d1771f | -7.08533 | -43.03435 | 2024-10-15 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 82a3f9c6-3053-3fe8-9062-634985d18026 | -7.08122 | -42.63522 | 2024-10-15 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7fe5b944-5a22-3aeb-adfe-81c29b603dd2 | -7.08063 | -43.01623 | 2024-10-15 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README47.md)
