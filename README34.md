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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 331c16f1-f848-3bf2-932e-a4fffb8029e5 | -6.18042 | -45.43785 | 2024-10-27 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7bfbe69-e345-3153-819c-1c9f63d09133 | -6.17978 | -45.44175 | 2024-10-27 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2efaba23-00b8-37e8-bef9-9daa9f8f50d7 | -6.17913 | -45.44567 | 2024-10-27 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7330726-cd03-34cc-86d0-32c81bc32491 | -6.17555 | -45.44109 | 2024-10-27 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a4bc702-62be-375a-a439-5abf8c781ed2 | -6.17491 | -45.44502 | 2024-10-27 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4dcc2d1-9a21-3de8-a124-55aaf1501ffa | -5.99303 | -45.97253 | 2024-10-27 04:00:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9630df0f-0137-3b90-ba0a-010765e4c344 | -5.98937 | -45.9676 | 2024-10-27 04:00:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54be7fcf-e230-3740-9d83-03cc07a20d73 | -5.98709 | -45.95574 | 2024-10-27 04:00:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 325e71fe-affe-33d8-9d64-6f402ee6519d | -5.98637 | -45.96011 | 2024-10-27 04:00:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90d7a8dc-fb79-3cf6-9e9f-208aaac32ec5 | -5.64723 | -46.28713 | 2024-10-27 04:00:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9df61c7e-6689-3cab-9f59-44a8b79a1d18 | -5.42716 | -45.34528 | 2024-10-27 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c7f04b8-faa0-3db9-8d8f-a2ac17ae2473 | -5.40889 | -45.40314 | 2024-10-27 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff2ce9af-68f0-391b-ae3a-d41ac5571ad5 | -5.40465 | -45.40232 | 2024-10-27 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86c0d4c3-5db6-3770-b2b5-8ea46f1e42f3 | -5.35686 | -46.25295 | 2024-10-27 04:00:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2ed6b10-8e1b-3af5-a278-e5da25bc8670 | -5.35611 | -46.25739 | 2024-10-27 04:00:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fdddf2a-3d62-32d1-ad6c-814858239d30 | -5.20581 | -45.5403 | 2024-10-27 04:00:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e47db30-3006-3806-8f96-d9d29b625e95 | -5.2032 | -45.53825 | 2024-10-27 04:00:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79ce5338-c8af-352f-8f22-ec28ef6712bc | -5.2025 | -45.54237 | 2024-10-27 04:00:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 442e214e-b723-3bed-993a-25e306b54ae8 | -5.2015 | -45.53965 | 2024-10-27 04:00:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e95994d-d626-3ff3-b979-e8c0729700cf | -5.20083 | -45.54374 | 2024-10-27 04:00:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39800299-b5e2-3166-bf62-f57f8ee2ac47 | -5.19888 | -45.53765 | 2024-10-27 04:00:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6bca5ca-5544-3759-bdd9-795db6435bdb | -5.19819 | -45.54168 | 2024-10-27 04:00:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5991beea-7eef-31fb-b30a-9f43600a150c | -5.19718 | -45.53902 | 2024-10-27 04:00:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66209407-b940-326c-a303-12c2c3e3e7c7 | -5.14388 | -46.04553 | 2024-10-27 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 066bff88-46e8-3a01-87b1-19a797db3f07 | -5.14315 | -46.04982 | 2024-10-27 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ab5e0cc-5724-3c2a-9d7d-7b2cd897dba2 | -5.09046 | -46.16922 | 2024-10-27 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1869efdb-ebee-3337-9fd8-dd4d96e00a7e | -5.08899 | -46.17152 | 2024-10-27 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbad8a66-0270-3cdf-87a1-b07d2e2ad951 | -5.06789 | -46.10364 | 2024-10-27 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05b3d0bf-b5e6-33cc-ac09-66b3fa2596a6 | -7.86195 | -45.41465 | 2024-10-27 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d38cdcd7-23de-33c1-92fe-14e608ef433c | -7.94541 | -45.6855 | 2024-10-27 04:00:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9a1591c-870f-31a9-8eed-d5037e1951bd | -7.94057 | -45.68875 | 2024-10-27 04:00:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e96e454a-6708-34e1-84c0-aada1b648cb0 | -7.71653 | -45.70968 | 2024-10-27 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7feb53a5-33b2-39bb-8f8b-25a8faa4fda5 | -7.7137 | -45.70105 | 2024-10-27 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86d5fe06-2204-31db-aef9-8b082cdc7ddd | -7.71303 | -45.70498 | 2024-10-27 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 943ed69b-8343-305d-8a4c-acb6f5044148 | -7.59571 | -46.87893 | 2024-10-27 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88dac22a-e956-3834-aa75-fa3e29840e69 | -7.58253 | -46.81702 | 2024-10-27 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a04d179e-999d-3464-ac39-1b2b5c33e399 | -7.53232 | -46.78444 | 2024-10-27 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4eb17b41-fba2-36f9-a871-367274b8388d | -7.52745 | -46.83968 | 2024-10-27 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0175febf-5884-31b5-a926-48c6dbda7f2d | -7.42336 | -46.65534 | 2024-10-27 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ba43afc-d981-3b10-ba81-0a2ffa46a489 | -7.38351 | -46.75095 | 2024-10-27 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 149f7e34-50e1-3f0e-b899-4c42f0e825e8 | -7.38302 | -46.74876 | 2024-10-27 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0bbdc26-1716-3d0d-bac3-14c71c650b6b | -7.25758 | -46.07572 | 2024-10-27 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8547baa9-c66f-3a4a-98d9-3ed523fcb295 | -7.23946 | -46.05157 | 2024-10-27 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5219282d-0523-38aa-b992-1c4b41919f85 | -7.23514 | -46.05084 | 2024-10-27 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 642c9554-5144-3ed9-955b-57d377d54f69 | -7.20395 | -45.57013 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e8dfefa-3a19-3de3-9096-bc12fb2ab0f2 | -7.20099 | -46.38506 | 2024-10-27 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9f33bcb-e233-3bdf-984d-c3cdeae4e66b | -7.07347 | -45.75593 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11d66cbc-3c0f-3338-a1d6-a16219239f57 | -6.92816 | -46.31969 | 2024-10-27 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f715730e-8213-3022-9e16-1456e007a7dd | -6.89646 | -45.57537 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 826b7671-a54d-3852-9fed-c749c52349ff | -6.88113 | -45.88826 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53e9c155-1fcc-376f-b805-ec762c68d47a | -6.87685 | -45.88752 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89f95c5e-00cf-3e14-b2e9-1800e78c880a | -6.87548 | -45.88471 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ff5f39cb-126d-3041-813d-94a06045de75 | -6.87325 | -45.88279 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8aa1a877-2043-30e8-b504-4192bbd1555c | -6.87255 | -45.88681 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b8243bb-b9f3-343d-a99a-1f1b4cc8e5a7 | -6.8712 | -45.88397 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf9cb08c-e8a0-3ec8-bc61-f7182bac756e | -6.86225 | -45.91121 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab2762b2-f73b-3f06-ae72-a5e14bfd2ed1 | -6.85972 | -45.87339 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b626e0f4-7f79-3639-95ce-13bf6cf47269 | -6.85907 | -45.8773 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3660bcd7-0b21-32bb-a1fa-707f08b978f8 | -6.85053 | -45.8756 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5c00de9-8886-344d-9b66-31d9e21a41b7 | -6.84689 | -45.871 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80850595-ca4a-356c-afbb-d4e1bb9fc70b | -6.84625 | -45.87485 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cc18654-82df-3fce-addf-be82b1f1413f | -6.8456 | -45.87868 | 2024-10-27 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7615fae-48ca-348a-a1d2-5287fbd5833e | -6.8186 | -46.14617 | 2024-10-27 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1088788c-7837-3691-8a9f-83f1141c8ae0 | -3.18967 | -46.18365 | 2024-10-27 04:00:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efe77d86-85af-3fa5-abac-2c574bbd85e2 | -2.65323 | -46.00027 | 2024-10-27 04:00:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7607e12-1e6d-38d0-99ff-d6851e233862 | -2.55365 | -47.33002 | 2024-10-27 04:00:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13ae0f28-7a2d-3cca-b3cf-d97dc8c46da3 | -2.47357 | -45.84116 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 544314ff-54ec-30e4-978e-33b0521c5ff1 | -2.47279 | -45.84585 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed11930d-510b-3283-9ce4-e41215525863 | -2.46938 | -45.84175 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 43e70c69-641b-38e2-bdbe-35b87407cb0a | -2.46898 | -45.84041 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46efdb2a-52c3-3a9a-9d5e-d013b46d2fee | -2.46864 | -45.84645 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1154181-6f9b-361f-bba4-64c47133fb06 | -2.4682 | -45.8451 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e352db8e-a345-311a-8d5a-10e092e40cbc | -2.46789 | -45.85116 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68463567-cea2-31d5-b247-1d01c3282387 | -2.46742 | -45.84978 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5186fe30-d709-3eef-a0cf-474a36033b30 | -2.36503 | -46.9891 | 2024-10-27 04:00:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf726536-ceaa-3ecf-800c-88b0186c147a | -2.36466 | -46.98978 | 2024-10-27 04:00:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aa3af52-bd70-318b-82a8-59de1c279d1c | -4.93408 | -47.39219 | 2024-10-27 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba86539e-f0ae-307f-ac4e-506b366a5935 | -4.81726 | -46.87012 | 2024-10-27 04:00:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f7bebe3-cc38-35ee-bbbb-5e7596b5c4d1 | -4.81252 | -46.86927 | 2024-10-27 04:00:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 213a93eb-d97f-3507-9413-e6e35e56d27c | -4.81164 | -46.87448 | 2024-10-27 04:00:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad0dd343-57b2-3e24-8f03-368de33ac8b4 | -4.65539 | -46.32684 | 2024-10-27 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b786a8dd-2844-3566-a414-cd50d4e9356b | -4.60825 | -47.53284 | 2024-10-27 04:00:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 531d0c83-4b50-3c97-8701-8cf96d9057c5 | -4.53337 | -46.41166 | 2024-10-27 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bc32cf8-e4de-3d68-9219-0e9e332b2cdc | -4.36934 | -47.09199 | 2024-10-27 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 12637f37-267c-3d7b-88f1-b09f6007be85 | -4.3654 | -47.08565 | 2024-10-27 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e62d38c9-92db-3121-bd14-57f735dd348a | -4.36451 | -47.091 | 2024-10-27 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5ea8bd71-0b98-3557-87fa-9ca704ce38b9 | -4.3636 | -47.09645 | 2024-10-27 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 470c470c-36ca-3961-a965-13699b9a3020 | -4.35969 | -47.08994 | 2024-10-27 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cb2bfd0-a9d3-3699-96cf-a95e7b76ddfe | -4.09957 | -46.48368 | 2024-10-27 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 86fc9703-3698-39d8-bb56-a22b60b3f6bf | -4.00827 | -46.44165 | 2024-10-27 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c674305-6894-3401-a834-c95c26c4e5fe | -4.00365 | -46.4406 | 2024-10-27 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9808a44-3605-3269-b1c4-ad7e37b43c5d | -3.90948 | -46.44699 | 2024-10-27 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00347024-5d70-35df-afd8-be7847da35f1 | -7.70975 | -47.00663 | 2024-10-27 04:00:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e38524d9-1b0f-3ee6-abd4-04c3eaa560b2 | -7.49491 | -47.33509 | 2024-10-27 04:00:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee6da1f7-b3ca-3dfc-9645-7a271a591e28 | -2.09629 | -48.55357 | 2024-10-27 04:00:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a561b551-216d-3a34-b664-9b0a085eede0 | -1.96745 | -48.68713 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e61855f-6dcc-3c11-adb4-b3fae2737c36 | -1.96683 | -48.69094 | 2024-10-27 04:00:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c690e69-0087-36b2-8a6d-66b37dd55f3f | -2.17228 | -47.94989 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f351dd5f-8eba-3f80-b07d-9299e8ddc8aa | -2.17174 | -47.95322 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2568729a-a162-351f-abae-2facc2604b5a | -3.26624 | -48.80098 | 2024-10-27 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README35.md)
