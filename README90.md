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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58c6d544-c70a-3172-8b88-08db5076d01f | -4.84268 | -48.57217 | 2024-11-02 05:27:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b80ec7ce-807c-3df6-9624-cf3ef352f11e | -4.84175 | -48.57883 | 2024-11-02 05:27:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f14b9c7-73b3-3171-88b9-10f3fbb640af | -4.35773 | -48.62852 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1d83e12-388b-3a99-9b76-fc264cb624b1 | -4.35374 | -48.60808 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24a0c380-953c-360c-9248-a28d7cffe38e | -4.35367 | -48.60837 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d002d5d3-c0b3-3e45-9c65-ebf82acac7f3 | -4.35285 | -48.61454 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e166843e-439d-3497-b387-05409a498f57 | -4.35274 | -48.61481 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c381e76a-6435-3a1b-9c4a-513d38ad5d48 | -4.34776 | -48.60081 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f111930-7b36-355b-9adf-6239e59c0b8f | -4.34772 | -48.60114 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4eee5558-9fb6-3729-88c6-2552817fe85e | -4.34685 | -48.60738 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a3d34b43-9917-365d-821a-a5e960f914e5 | -4.34678 | -48.60771 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bd70fad2-5ec0-3a3b-82cd-4ff5c3f094fe | -4.32093 | -48.64184 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5be440e4-25ce-3b1f-9644-b3e47abd7b83 | -4.32003 | -48.64807 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64686016-1220-3185-9098-f8ec61d8bd90 | -4.29624 | -48.61931 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83b361a6-2577-32c2-9867-ba5693fe644d | -4.29538 | -48.62542 | 2024-11-02 05:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 547af8fc-badf-371c-90cc-88261e68860e | -3.9479 | -48.35496 | 2024-11-02 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ddaf98da-2ec5-3e35-b874-7901aad17cbc | -3.94702 | -48.36105 | 2024-11-02 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ee64ed1-4e4a-3717-86d0-8a0de6bf7ba2 | -3.94693 | -48.35382 | 2024-11-02 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e0aa814f-beef-3580-804a-bed7b47c9f88 | -3.94608 | -48.35994 | 2024-11-02 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2fd8b30c-d06b-3780-8820-137fc3cc6cce | -3.94192 | -48.34755 | 2024-11-02 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57cfc86c-86bd-3f03-a580-2cb4a05e2398 | -3.94099 | -48.35395 | 2024-11-02 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c36974df-c248-3381-b5f5-63230c2861b4 | -3.94012 | -48.35999 | 2024-11-02 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ccc0f42-437d-3e31-a0be-7d534028f6d0 | -3.82327 | -48.97823 | 2024-11-02 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9c1fe6c-24ca-3fad-a616-f78b9fdea706 | -3.81661 | -48.97733 | 2024-11-02 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 783c9a9c-ea6c-39a4-97e6-29eb22a98320 | -2.07631 | -48.81966 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40fe9aba-172b-3c01-8a85-8f840a2c3c69 | -3.50431 | -49.93912 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca0d1aa2-745e-30fa-bbec-356fa8a1833d | -3.50359 | -49.944 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a466614-1304-3d6e-a817-d0e04fbdf101 | -3.47152 | -50.37255 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a316148-ef14-3bf4-8714-a742b7530ad2 | -3.47135 | -50.37122 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0218b87b-04ad-3778-b2e7-2fc71d3731f7 | -3.47088 | -50.37706 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2c17df10-0576-3d59-8cf1-851a21a9e389 | -3.47067 | -50.37572 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6aed43ba-bd24-3ebb-b672-46daf35e7c08 | -3.46528 | -50.37031 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 966c5be2-795a-3e65-b20f-90afa4207fb2 | -3.45933 | -50.28511 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68e58fc9-1391-36e6-a815-240ab23c667c | -3.45879 | -50.16179 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2e55584-b3c0-39a9-a075-d93a41d7e9d7 | -3.45864 | -50.28977 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3292b1a6-c05d-3528-8e5d-092589a75520 | -3.45813 | -50.16632 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b02016d9-f6c0-3236-8927-8ac882a60bc0 | -3.45747 | -50.17078 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80b9066c-2938-328d-a825-0fbc7c067774 | -3.45338 | -50.15585 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4aafe98-de5a-39a6-b024-ffa072708f71 | -3.45267 | -50.1607 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91bb7f48-3200-3d36-aa05-7328e9e8f500 | -3.45199 | -50.1653 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dffc69da-20c9-3010-957f-1477681ef4cb | -3.4499 | -50.17958 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6b60a9c-1a8f-3466-baf1-48ecce9b606a | -3.44725 | -50.15477 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d174794a-5e4b-3f02-8375-264db25f1588 | -3.44375 | -50.17871 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2366c9d8-b062-3e2b-9e6f-3372e6c52753 | -3.41594 | -50.28336 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f117abdd-1c59-3fcd-870f-5b208867b1c0 | -3.41526 | -50.28804 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2de12b8a-4c83-3e24-85ef-046ad1f7288a | -3.39512 | -50.34102 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0da27fe-42cd-3bf6-819b-65b9a2e9d6cc | -3.38904 | -50.34015 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae01fdf8-b0ab-3f28-8b10-5374cf83adb6 | -3.3752 | -50.26327 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04b6a595-f67c-3a57-affc-c913ac283f7c | -3.37458 | -50.26763 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 405935b7-e5ac-38ea-9f5b-f19e03497298 | -3.37458 | -50.26397 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdf0093f-f29c-3646-b60b-1a573e27020b | -3.37393 | -50.26832 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1beedfe0-f3a7-36ca-bff2-fd5070751670 | -3.36908 | -50.26245 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da963726-596f-319e-bf8d-776f1081cf2b | -3.36847 | -50.26314 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b67b9267-a22d-3fd0-8d25-22f70e4c0008 | -3.36846 | -50.26682 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8db91762-d0d2-32f7-8cce-651235fb1bae | -3.36781 | -50.26752 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2248602-b89d-347f-baf1-a87b43c57ceb | -3.36465 | -50.16282 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 907efa08-96af-3010-90b9-a7f2b2c527e7 | -3.35852 | -50.16179 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec0611d4-b6cd-3915-ac10-3b8d1837a342 | -3.34477 | -50.25465 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a38d7b13-3eaa-3a5b-bf5a-838bbe14e9ba | -3.33867 | -50.25374 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30363e5a-acb7-339e-b263-6466178b0b52 | -2.97886 | -49.51217 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f6447b0-3a59-392c-8ef6-77d0f679666f | -2.93783 | -49.34124 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb86fd65-1ef4-3cf4-9320-046e0eb0af93 | -2.93702 | -49.34671 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a8597d3-be42-35b8-a2f5-d5bd77968427 | -2.93184 | -49.4256 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ea7a74f-20cd-323e-8f52-34b2658ab62e | -2.93107 | -49.43081 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05842b3b-dc7c-3ef6-a72a-2f9b7d67dabc | -2.86529 | -49.38894 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcff0128-4c7f-38cd-82fa-b8f0d9055baa | -2.86385 | -49.38784 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 352aaf09-7c86-34fa-bcac-de2583119620 | -2.85889 | -49.38799 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce9a62d6-d3de-3aae-ba94-1918f43756cb | -2.85744 | -49.38693 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e754aab8-809b-302b-bcda-c3e1a36d3813 | -2.85248 | -49.38707 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3f9ac4a-7b22-36ae-afae-b14cfce7e05f | -2.85104 | -49.38599 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68b37686-84b9-3e5a-808a-83ca82eb5365 | -2.84542 | -49.37984 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1800cf0a-0bde-3034-93e5-c38c1508b157 | -2.84465 | -49.38496 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1eed2a1f-f05b-357b-9262-6976e4229d90 | -2.81922 | -49.76694 | 2024-11-02 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98a7ec40-ff58-3c9e-a1ee-5ad8b775e270 | -2.81296 | -49.7661 | 2024-11-02 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c6b88dd-8763-3045-acc2-2e82171e23c9 | -2.77777 | -49.83016 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27456e98-9a4f-3cf4-8473-d33090fbfdf7 | -2.77155 | -49.82922 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3756a39d-f0e2-3a0c-98e4-b491dcb04e14 | -2.74114 | -49.55741 | 2024-11-02 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e460b5a9-a56c-31eb-b44a-21bb47b8ff61 | -2.73929 | -49.55606 | 2024-11-02 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9b76358-08f3-34ea-b6dc-e441162b7e13 | -2.73853 | -49.56108 | 2024-11-02 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef8c45d6-9621-3015-9f17-da923ea9a366 | -2.70767 | -49.28852 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d350468-1aae-3562-8ea3-b50a93ab4eb1 | -2.60835 | -49.1551 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4197a3b4-372f-3eeb-9ecd-091520ecb2e2 | -2.60753 | -49.16047 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73aef146-c2b9-3087-bafd-864ab68f64b4 | -2.60751 | -49.15805 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4a963c4-90d0-31ef-9aeb-618e03b24cab | -2.60515 | -49.82083 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 007cf749-72d0-3e4e-bc6e-2126a5f79327 | -2.60413 | -49.8176 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f59c0f9f-3820-321b-af3b-492e758b6945 | -2.60343 | -49.82234 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6cc22927-a7ff-3662-9ec5-754f7919405d | -2.59966 | -49.81519 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 479e6ccc-2c98-3557-87f4-ecf426680a66 | -2.59892 | -49.82003 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7373bb1-1d03-3ef7-a7d8-239f5d4b6469 | -2.5982 | -49.82468 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb32f73a-a21f-3649-958b-582d39aae081 | -2.59792 | -49.81665 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c6d15e4-e3cd-357e-882a-bce353cd3593 | -2.59721 | -49.8215 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41b8b253-2195-3131-a440-b5f6a6893022 | -2.5927 | -49.81915 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 535bf3e0-3a49-36ed-acb6-619fb848a8a0 | -2.591 | -49.82058 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e7aedaf-bedb-3e9e-bafc-31d984a0849d | -2.5512 | -49.62811 | 2024-11-02 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 838fa947-3dd5-30c7-8198-8ea63098574c | -2.55047 | -49.63305 | 2024-11-02 05:27:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31f8fa2a-11ca-3e78-84ec-b12fdc8058e5 | -2.49409 | -49.07735 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d22c4953-4492-3678-bf3d-b32342626850 | -2.49404 | -49.07763 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c992e89e-c35a-3f51-8322-9fbc0be91da4 | -2.48758 | -49.07646 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd8e974b-af72-3e04-9b3b-66409533aafd | -2.48754 | -49.07671 | 2024-11-02 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37c77a73-3bfe-38ef-9a59-a2c24601b2ca | -2.46029 | -49.78556 | 2024-11-02 05:27:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README91.md)
