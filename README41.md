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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09d2ac6c-0312-3e2b-aeb7-c3a450e88717 | -2.78425 | -49.24979 | 2024-10-11 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed7e00cb-ff48-316b-a75e-e6c0679623f4 | -2.78357 | -49.25387 | 2024-10-11 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5ccb6a0-c18d-3175-b973-9c5dafae7cb3 | -2.77914 | -49.24474 | 2024-10-11 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 614b7644-a77b-3466-9370-cca1e377546c | -2.77846 | -49.24884 | 2024-10-11 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc31bc02-2082-35be-8845-b2c1096f73ac | -2.77778 | -49.25293 | 2024-10-11 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dedc62d1-0ca7-39f5-a068-ed9669e0db0c | -2.77471 | -49.23569 | 2024-10-11 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 060d8fdc-e8a3-3a9e-8e50-71013b0c75a5 | -2.74215 | -49.53979 | 2024-10-11 04:00:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca859f88-2f7f-3f46-a7a6-c3b84faf795a | -2.74145 | -49.54403 | 2024-10-11 04:00:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46fb5943-44bc-35f3-88df-e273271b2a20 | -2.73626 | -49.53876 | 2024-10-11 04:00:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35e0aa63-1fe8-346d-b188-9db2d8ddd0a5 | -2.73555 | -49.54303 | 2024-10-11 04:00:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b2227f3-fa0e-36c6-99ca-c8a7f266b06c | -3.6334 | -49.56909 | 2024-10-11 04:00:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 883d4f36-2d0d-3a0f-95f4-3553a2609847 | -3.63258 | -49.56661 | 2024-10-11 04:00:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7aa06f15-0698-34a3-9082-09f548a0802f | -3.31342 | -50.17648 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ab6b1266-64bf-3fc0-912b-46309a6f710d | -3.31305 | -50.1776 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 15866fee-7cd2-3119-8429-7b73e7a7540f | -3.31266 | -50.18107 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 34625f00-0190-32ee-8261-c3e9c4411dbf | -3.30734 | -50.17541 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1f4ebf64-492e-3c22-813e-072cb7286f76 | -3.30697 | -50.17656 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78a38848-c926-3fbe-9bd5-e7c5a8efb17b | -3.30658 | -50.18 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b32c9aed-0010-346c-84fe-7f054bcadeaf | -3.17015 | -50.43496 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10eaaf31-df9a-3c63-9d34-46296e6fa6a3 | -3.16939 | -50.43958 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 872b0dd5-2e47-30e8-859e-1d37493ff08f | -3.16835 | -50.43652 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c1380cd-4e5a-3d25-87ba-0db224231a2a | -3.16757 | -50.44107 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8dadee8d-22f7-3865-939f-c66cee5a6d7e | -3.1632 | -50.43847 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9170a484-3c35-3606-b7a2-82fa7986699f | -3.16248 | -50.44281 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 256d3b1d-7a59-335e-babb-dc0e040c7f74 | -3.16217 | -50.43539 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 05cea0ef-9b11-3771-8b3e-3b1c5af81f2c | -3.16138 | -50.43995 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1f45d918-2488-3c15-953d-deddce024272 | -3.16063 | -50.4443 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5a8144d6-129c-31f0-95f6-756c7f920598 | -3.15702 | -50.43728 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0e7fbad1-0aa0-34a1-a8f5-3586400e12ae | -3.15629 | -50.44168 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 51252f7d-0452-306f-a32e-e3c5fdb9f1c4 | -3.15553 | -50.44625 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| df7801ad-57b9-3ccc-ac2d-93969f1dcc4e | -3.15521 | -50.43871 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ec2b2653-0499-33ae-89bd-05e129a96455 | -3.15473 | -50.45105 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 6e804dce-1ede-30c2-a197-88e4b16116ea | -3.15443 | -50.44322 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 58eaeb12-d109-3e3d-8006-9fb672939bb7 | -3.15362 | -50.44786 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 2d71b2a0-d32b-3f87-ba5f-3b500fdc3bb1 | -3.15085 | -50.43603 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0f7ea6a-1c4e-39a9-bd07-d6c33263bb5c | -3.1501 | -50.44057 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8d8787ff-acd6-3e41-99ed-866a96fab5e4 | -3.14932 | -50.44524 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4a669a7a-de7b-34b4-bf60-b194bfbd0f64 | -3.14904 | -50.43755 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 17b64d84-2ea1-3987-b9ca-82912f121d8d | -3.14852 | -50.45 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 3a755993-3a54-3d07-960a-32509444b5f2 | -3.14823 | -50.44217 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a4229f24-7a45-3e31-8ff1-ee77c920ed3e | -3.14741 | -50.44691 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| e99fd049-00ef-3c49-9ce9-191fd3534259 | -3.14391 | -50.4394 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dffb5f04-850c-3d5d-b99f-dd45f90f1ba1 | -3.14312 | -50.44418 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 088cc404-2012-3012-975a-10f0cd3aabb5 | -3.14204 | -50.44105 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66b51653-8642-38ad-8317-f8f0109f7795 | -3.14121 | -50.44584 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47021bc4-a168-3eb5-977b-0772d010e3ee | -3.14004 | -50.42445 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13ba6695-664d-31a2-b2f9-17fccb390940 | -3.13929 | -50.42894 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f96aa29a-6014-3252-b5a8-94ac55b4a579 | -3.13312 | -50.42771 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05a635c5-9439-3e51-b892-7912101ff18b | -3.09736 | -50.2279 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bfa1cef-7cc3-32e6-a8f1-ae3e691d8cb3 | -3.09203 | -50.22575 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64326af6-d042-30fd-9033-f2ccec706809 | -3.09127 | -50.23035 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42fb7dd9-a740-3e6b-856a-7dea300d12a0 | -3.09123 | -50.22693 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 902beed9-cd38-3976-9dc2-5a054fad8a8a | -4.94767 | -49.76274 | 2024-10-11 04:00:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0ac62b4-2ead-360c-8037-ba80ce250c39 | -4.94697 | -49.76677 | 2024-10-11 04:00:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89fda76c-29f0-3ade-88b3-91730bf67bf6 | -4.84316 | -49.88888 | 2024-10-11 04:00:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d4707fb-916c-3474-8c4f-b3a4074b0f5c | -4.84229 | -49.88637 | 2024-10-11 04:00:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 119ad7a1-acc5-3133-abda-f4c1cad3c576 | -4.84154 | -49.89058 | 2024-10-11 04:00:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81afefc5-5db4-3677-b051-7b4cb29c5f91 | -4.83176 | -50.79201 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89c758d4-eafb-31da-a526-a52db221f692 | -4.83094 | -50.79666 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e3e5e3ab-ef2c-344b-aba7-7f900102267f | -4.83007 | -50.80159 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a5196b2e-de5d-302f-8367-44cb46dd8ba0 | -4.82475 | -50.79569 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13324943-1b36-30e3-8b75-445ca17879e2 | -4.58837 | -50.42499 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eee7a9dc-dcf2-3fc7-9880-8b595d66dc60 | -4.58759 | -50.42949 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d90baad-278d-3e7d-bb6a-4469273d1018 | -4.43604 | -50.54295 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de8daf35-4b8a-3d71-a40e-cb318206d31a | -4.43521 | -50.54767 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e178b12-7a94-39c4-afce-ea91732b2ea1 | -4.38477 | -49.82343 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f749814e-6dc0-3968-9968-713d0360144d | -4.38405 | -49.82761 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97ffdc3d-0838-3e41-9337-5eaa656b3e11 | -4.34717 | -50.51104 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4359e3a3-8d66-372a-926a-bdcb4a95d321 | -4.34107 | -50.50991 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4d886ae-4177-341f-8883-fcdc773d2072 | -3.92481 | -49.66302 | 2024-10-11 04:00:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 443ff6df-8f5c-3bb6-8770-a1335195384d | -3.92416 | -49.66674 | 2024-10-11 04:00:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af5948b0-9f31-3a53-86c2-58abebf20f97 | -3.9235 | -49.67051 | 2024-10-11 04:00:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d50481bc-2d50-3213-9630-0f0556c9e3e0 | -3.68781 | -50.11573 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5990d33c-0954-37db-be97-d8b37c47840d | -3.68706 | -50.12008 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c2cfd1ce-434c-3d25-93fb-e05570e25b1d | -3.68629 | -50.12458 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 70fe88d8-9590-371e-b5b4-c911c2a28adc | -3.68099 | -50.11934 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 28eeda79-5c1d-36d9-8ead-d13718602e72 | -6.20168 | -50.89686 | 2024-10-11 04:00:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27e23fef-91a2-3e2f-adf0-0b2468120185 | -5.55768 | -49.58047 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48241b75-5252-3d9b-ad18-b2ba2014a8ee | -5.55701 | -49.58424 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3f3d2aa-b663-3fcb-8c7d-7d1525eff4e2 | -5.55535 | -49.58187 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5869042-3b32-3ec9-a993-fb4f2d405505 | -5.5547 | -49.58569 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e170e141-2630-30ab-83aa-edd9142cea90 | -5.55135 | -49.5833 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7048510d-ce26-33bd-a66d-677f98f51a05 | -5.55067 | -50.42392 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6a435da-dae9-3c16-8288-83945a140114 | -5.54905 | -49.58466 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79745942-a77b-35c2-960a-10526cccac73 | -5.54471 | -50.42285 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95c4171e-d2ba-314b-8494-60c76e589193 | -5.5367 | -50.99251 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 835c7ea8-6703-3dd1-8c66-aa7d9bfd608e | -5.44443 | -49.56845 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaf3351a-cdc2-3782-9975-9e49e9032d5b | -5.44377 | -49.57232 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0f31536-078b-3a6c-912d-7fc2f0dd5e39 | -5.34135 | -50.99855 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c3604c8-8c8d-3284-bb0a-2b9ff3023dfb | -5.33514 | -50.99749 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 275e4504-a05d-3557-8baf-48d4a1e527c1 | -5.28785 | -50.98854 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5683616-b5b4-3b7e-a163-c9591d3ee521 | -5.28699 | -50.9935 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de4f5b29-f35d-31cd-be62-3e1bef4731af | -5.28674 | -50.95833 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bee5241-cab7-32cf-a37e-5925943aca7c | -5.2855 | -50.98888 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5f2e290-b869-3f34-882b-3c31469fd7bb | -5.28459 | -50.99383 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8988a5f2-f89c-3ff3-a139-ed55d2e36dd9 | -5.28166 | -50.98735 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc4df3a2-f7f0-3e30-bf0b-9756f21c3368 | -5.28079 | -50.99232 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62834a36-467b-32b5-b896-6f33086dae2a | -5.28059 | -50.957 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 698d6d8c-7542-3ee6-b24b-572547c2f43b | -5.27974 | -50.96185 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 259a2d53-8945-3b22-bd00-e8af0d13f4e8 | -7.67723 | -50.25027 | 2024-10-11 04:00:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README42.md)
