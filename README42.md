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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 228624f4-7643-342f-b602-53f6c5420eb3 | -4.75748 | -48.00575 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 367f327f-2727-3bae-8ad6-e01165adfa09 | -4.59833 | -48.07217 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65650595-d10d-353a-8277-5f9f8984ba38 | -4.59482 | -48.07166 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e3fc2c08-7850-366f-9b40-eb1fa1fafcff | -4.59131 | -48.07117 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a7ed27f4-2692-3f7d-973e-7bc272a9ed7f | -4.51533 | -48.21822 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1abffda-1ca0-3df7-8e97-6cf5bd119ad7 | -4.44519 | -48.17595 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e83ce2fb-f80c-3a90-9a85-5288ed48c007 | -4.44229 | -48.17159 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77eb340c-d5bb-3905-82a4-97391ebc964a | -4.44171 | -48.17542 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32e7708f-b00e-38bf-98c7-0a7ec3b1282a | -4.43823 | -48.17489 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7e766d1-ea6c-3a3c-be14-263027fd15e3 | -4.35033 | -48.15482 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47bd644c-8377-33f3-9603-b3900dc94578 | -4.34975 | -48.1586 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be8ee40b-33c6-3c7e-9e61-4698a8394a29 | -4.28591 | -48.22755 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b43703-791c-35da-b90a-f90a3b2e174c | -4.28302 | -48.2232 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85a5f8a8-9657-33ac-abdb-4ecdfa36ba98 | -4.24193 | -48.03637 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5db1d343-d215-3315-9484-c8f32647b1a9 | -4.24074 | -48.04419 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 265db87f-6d07-311e-8ab5-dc1dc81c6de8 | -4.24014 | -48.04809 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8643f7b-ab06-31af-a675-2a25803821aa | -4.23844 | -48.0358 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4dc3c67-ef0e-3e20-b7df-1bc2d255be4d | -4.23784 | -48.03972 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 898ec475-307c-3908-b434-ab8ff93018ff | -4.23555 | -48.03128 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0eccb4a-c4a0-338f-a9a1-03688037bdd3 | -4.23495 | -48.03521 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed9304ed-c7ef-3e45-a43f-6e352712fac4 | -4.19003 | -48.14324 | 2024-11-03 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6354dad3-5cad-3428-9507-38d49a06a7be | -4.80289 | -49.38788 | 2024-11-03 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73fdc136-eb6d-343a-abae-f7034793e3c2 | -5.70597 | -48.99075 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d953227-2611-3b1c-a099-88efa1f333fe | -5.70256 | -48.99022 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73e563bd-2e52-33b7-80cb-03df67d6c906 | -5.70199 | -48.99393 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e0c353b-0913-3b6e-9c81-011960e172e8 | -5.69914 | -48.98969 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb532a4b-cffb-3181-8d09-6a185e2ca3bc | -5.69858 | -48.9934 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52063442-ff5e-380d-b25f-e02a4ecd9ca0 | -5.64537 | -49.13186 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 043643b2-d45f-327e-ab1f-f0f2cefe2d80 | -5.48261 | -48.96094 | 2024-11-03 04:46:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c8b5712-e4a7-3d5c-9cfe-bf477641aea6 | -5.30691 | -48.84743 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf02ffe-ca2e-348f-a30a-243ec14facb8 | -6.40715 | -49.56651 | 2024-11-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65c385f6-6549-375c-af16-163c519ab43d | -6.40433 | -49.56237 | 2024-11-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d2ef325-ae87-398d-a92b-8e46bd4e7e9e | -6.3982 | -49.57996 | 2024-11-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5dd28498-dc29-3662-a89f-dcb4c1fe1447 | -5.22451 | -48.07702 | 2024-11-03 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa85bc4b-69a7-30c3-856c-715d3cab7221 | -5.70596 | -49.30898 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb73fa90-e70d-34d6-b353-82722e4773b0 | -5.7054 | -49.3126 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bca892c-1099-3c45-bea1-e4d7ca0902ed | -5.70202 | -49.31208 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e214654a-f23f-3376-a898-92a9a200980a | -5.51784 | -49.48962 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ab4b4ab-00c1-3d3e-bfc2-46412bbcfe72 | -5.51448 | -49.48912 | 2024-11-03 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e509782-b8d1-35a7-8723-23b731897b3b | -5.24753 | -49.41547 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47efa262-0f1e-3644-8d2c-3feec04c507d | -5.1998 | -49.36783 | 2024-11-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57545119-3f6b-3148-898f-04f1165a44f3 | -7.03462 | -49.15405 | 2024-11-03 04:46:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 768fbf09-8b6b-3113-8002-e09904a17b9a | -7.03119 | -49.15352 | 2024-11-03 04:46:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7084992c-ec54-34ef-88fd-b9655695ebbe | -6.8923 | -48.63713 | 2024-11-03 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95801d46-76c7-3ff5-a5cd-24710cd514b0 | -8.0087 | -49.84999 | 2024-11-03 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04791543-c4f1-3373-96eb-3883260cc1b0 | -2.13319 | -49.51949 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f39c05-5d5f-342c-a40c-5c13b551852d | -2.23633 | -48.85307 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc6f3692-5d9b-3ee7-8e16-b45cf7d0b2ad | -2.22283 | -49.13895 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2212e7fa-3e6a-3cd4-a6ab-ee06af1b850f | -2.2195 | -49.13844 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c49134b-8ba2-302b-81b4-693903411473 | -2.21618 | -49.13793 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8030a00e-a985-32e7-bc8b-e5e5cc934628 | -2.21347 | -49.1554 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e467b43-a19e-35cb-8709-2ac423be907f | -2.2096 | -49.15838 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e5745f6-bb26-32f7-9782-6245bc60ca3e | -2.2034 | -49.13239 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aa5b3e3-b40d-3409-b04d-73931a35339f | -2.20302 | -49.1788 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb5e2675-ec64-3f38-83fd-cd613cb4c232 | -2.20024 | -49.1748 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6a3d500-e7eb-39ab-a285-b36f0e6f23c2 | -2.19063 | -49.12685 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0ad6eee-be82-374b-a791-0f7893d53fb1 | -2.17714 | -49.21407 | 2024-11-03 04:46:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c409df5b-c94c-3839-9dd7-e096ca7bdefb | -3.51049 | -49.49907 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a6f1e70-769a-34d8-be94-19c410bd0c52 | -3.45733 | -50.1707 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e7d13a0-a104-3374-85be-ae4f03b5e382 | -3.45403 | -50.17019 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3460df6-4c4c-38f2-99a3-dfe965a3d778 | -3.45234 | -50.15937 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d279709-5d94-3485-8c05-a257d288a9e7 | -3.45054 | -49.73168 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c971ecf-ed16-3ac7-a941-25cc8be4a0f3 | -3.44957 | -50.15543 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69ecdd37-5b60-3aa5-a8ad-4fb4a7d1e204 | -3.44515 | -50.03157 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5eb8c9c-fe17-3722-a80d-8c0d273eaa18 | -3.40601 | -50.01789 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4105661e-9d60-3de5-a69e-86c25d77a2c2 | -3.35448 | -49.23116 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 288c2f34-e46d-315a-a25a-e295852d38b5 | -3.35394 | -49.23468 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de09bd30-b4d4-383f-9145-0233a88953f5 | -3.35222 | -49.2236 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d5f0f31-d906-303c-a83d-f3b2a13e4977 | -3.32616 | -50.11822 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 774b4c8d-b0fa-34d2-aa29-99b4114b47bd | -3.29987 | -50.02254 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48358672-a1e6-30e6-be15-940190a6f7dd | -3.2988 | -50.02942 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bac1d135-8f5c-3ebb-97ee-eb4d5501179f | -3.29826 | -50.03286 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e16d345-e9c3-328b-a7f1-b19e8933451c | -3.29656 | -50.02203 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67cbf5c0-977c-340f-bc27-778f03b3cf83 | -3.2963 | -50.08885 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d487b5bb-121a-33bc-bb9d-c7a0dbf3cc8f | -3.29549 | -50.02891 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5230f46e-8c22-3eb8-b7f2-266030596037 | -3.29496 | -50.03235 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e4df6a8-0c23-34a7-b67c-6e481975253e | -3.29326 | -50.02153 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 827f2116-9390-3ef3-8688-32be3825282c | -3.29165 | -50.03184 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12a879d8-ae49-368e-8622-f427c714ff4f | -3.26601 | -49.09847 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fca999c5-4ba9-39d8-99e6-80579c79a238 | -3.25649 | -50.04051 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e339d161-31b5-37cc-8c31-028da359a162 | -3.25595 | -50.04395 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c7b505-85f5-3c4d-9f76-772350520dd4 | -3.25542 | -50.04739 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f541a3e3-d21f-3fae-9200-c6034e89e58a | -3.25489 | -50.05082 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79d3c2f8-a3ee-3cf5-b181-9ace837ff3e3 | -3.25438 | -50.18435 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52ba3943-4c52-37bb-b4ad-b396bf512dee | -3.25384 | -50.18779 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76a6d842-d8cf-3ff5-b33b-1619e0d7a462 | -3.25331 | -50.19122 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7073435-22ac-3326-a1d9-ddf519392aaf | -3.25319 | -50.04 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07c24e98-23b7-33c7-9629-285ee39f899c | -3.25265 | -50.04344 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a965d44-9a82-3cac-a737-1cab5a54f908 | -3.25212 | -50.04688 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80b75d44-64a3-3826-b36f-6acb8e3f3617 | -3.25158 | -50.05031 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af1ac981-61cb-33fb-8634-3ec876385115 | -3.24988 | -50.03949 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fcc8ae3-ca6f-304e-bcc2-b77c01f6934c | -3.24935 | -50.04293 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c945f33-53ba-3267-a6da-28e1615e89a6 | -3.24882 | -50.04637 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1bf0d78-82f5-3c3d-93b2-4001000c23ce | -3.24828 | -50.0498 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88283507-862b-3899-8dc3-7fcf0837fa6c | -3.24775 | -50.05324 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95037a04-567f-3479-9a25-80519daa9a5f | -3.22817 | -49.47709 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f0d1a7a-2c3c-3daf-a981-00befb5e710d | -2.58034 | -50.05772 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 121c1791-adff-3c4e-8ab0-c0598e4b0a4a | -2.57758 | -50.05378 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3882f261-e1ec-3db2-9048-40af26e44f6b | -2.57704 | -50.05721 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afd13fc3-17a4-3566-997f-575f2106b20a | -2.57651 | -50.06063 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README43.md)
