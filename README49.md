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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f75aa30-86c3-3dc6-893b-9e02ff320928 | -7.78568 | -45.38843 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83565b45-5705-31cc-a4c9-1a37e507f776 | -4.3124 | -50.33762 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0420b7b0-014b-3e61-b1e5-b742b68ed7c8 | -7.79281 | -45.39016 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d17ea9dd-03e5-3c9f-a2a0-e0c7a27f82e5 | -2.06541 | -56.87312 | 2025-10-26 05:21:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85afc8b6-ea67-3b44-854e-7ab444855e7d | -6.39797 | -45.77261 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4b988bc-ef39-3c20-b4b2-8c9c54159ba6 | -7.79177 | -45.38798 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 511e9234-d4d0-36af-9677-1ce6d243fcf8 | -4.838 | -50.92936 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e945d90-63d1-3f52-a2f2-555b02a1d320 | -5.70652 | -49.2776 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74400088-4cf9-3a95-a3bd-c0029e5bd57f | -3.68808 | -51.97245 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a31fd499-71f5-3185-b864-77be28b4a5b5 | -6.17828 | -49.87167 | 2025-10-26 05:21:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1983827d-3a53-3f44-9cca-0e2b754120ca | -3.83879 | -50.19973 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b87b27d8-28cc-3383-888e-c38448d58334 | -3.1031 | -49.44398 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78831972-8dd9-3f34-95d1-0a9dad6e7aa8 | -2.3793 | -55.96514 | 2025-10-26 05:21:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 199da8f8-8cbc-34cc-a004-7b3f47e5ec51 | -3.81358 | -49.29648 | 2025-10-26 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 778e730d-1b0f-30f9-8cd2-b4b974f556f8 | -8.04804 | -46.7475 | 2025-10-26 05:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ce94eb5-fc51-3bd5-a5d8-bfd7dc6f1295 | -2.95186 | -49.34759 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d277a9e-762f-3b46-8bc2-6c3d1585dba8 | -6.10169 | -47.05171 | 2025-10-26 05:21:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13ae524e-f333-3422-be53-7d45b8810ee6 | -7.79915 | -45.39824 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edfbcfdf-0ef8-3574-b5d2-4dbcc9946642 | -3.67093 | -51.9498 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11a43a68-9359-3fd1-af8d-95f583aaffd7 | -6.38799 | -45.79055 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec541d7b-4dc3-3b01-9db0-bb71b3d2ccec | -3.23718 | -50.6509 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be5efb00-fac8-3e4a-9629-4e832955e85f | -3.31098 | -50.11713 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6163a348-c8dc-3d1c-b9e8-04bb5f5f9693 | -3.87145 | -52.19246 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75c0fc49-6de7-355a-8341-64c5c43115d8 | -2.65574 | -48.51141 | 2025-10-26 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 711903ea-50e3-3d57-b148-ca436e7372dc | -7.79892 | -45.38951 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17127190-01f7-33a4-bcd8-a0630da501f3 | -3.10098 | -49.45662 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 380f8861-c227-3827-be6e-a3af8a64689f | -3.23795 | -50.64564 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71a95ced-c523-36f9-ae0c-e45dc9636871 | -3.12022 | -51.20889 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edee1a85-a866-354e-815b-f64468628fe1 | -2.33238 | -60.0633 | 2025-10-26 05:21:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 441ffe8c-2a88-3d13-bcdc-bbebddb4a76c | -9.43623 | -46.33702 | 2025-10-26 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3cef456-350a-3e5e-a627-9e8bd028abfa | -1.56139 | -60.14199 | 2025-10-26 05:21:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e7a26df-7fc9-3117-8614-59798041a022 | -5.70702 | -49.27399 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fae98a3-7fe4-38fa-8bd9-b63bae7a135e | -3.61022 | -48.91925 | 2025-10-26 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47680176-e026-3e31-a10b-1a6ec4c98ea7 | -3.39279 | -52.44669 | 2025-10-26 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72844197-230a-3496-ba3f-31f34eb95516 | -3.41761 | -45.46311 | 2025-10-26 05:21:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e6d4d7a7-f4f4-3ae3-9c19-767b18fc3f8e | -3.75783 | -52.25883 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f798b37a-b26f-3817-b8ed-66297fd4de2e | -8.54076 | -47.20316 | 2025-10-26 05:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 496ad7dc-d1d9-3ed0-8464-8c2976d998de | -1.57431 | -53.45199 | 2025-10-26 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95fdb973-2ff3-3608-bbf7-0b013522b507 | -6.10269 | -47.04949 | 2025-10-26 05:21:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff93026b-acce-344e-bb80-71eeb01bede1 | -3.31164 | -50.11277 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 888a3a9d-07dc-35b5-a065-882dbaf3a1bd | -3.14756 | -53.1438 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3e599ee-83eb-3402-9726-9d14705e77be | -4.02856 | -46.06661 | 2025-10-26 05:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9cdc215-c1cc-3f1f-ad83-32082bacd196 | -6.79541 | -45.40628 | 2025-10-26 05:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a4a0db7-2010-3331-87ba-b4b94ee21f29 | -8.72584 | -48.56953 | 2025-10-26 05:21:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64a81b90-eed9-39fc-bd3d-95128d3decba | -4.48257 | -48.67616 | 2025-10-26 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d13e74b-47d8-3d70-8719-cd2fd935a878 | -4.03512 | -46.06802 | 2025-10-26 05:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fbe25cc-7e6e-32ed-9e21-c875ce0085c2 | -3.10439 | -49.47003 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85ed9ccd-aabf-390b-9e9e-eb0b875cc162 | -3.75858 | -52.25719 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bb9514e-eb62-3f6e-8149-c3326dcee5a8 | -3.10445 | -49.4702 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 825530c5-0c58-39d5-b271-5a4721ab5a0f | -8.05095 | -46.74446 | 2025-10-26 05:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 531b6f87-ca6a-3129-9be0-90f220130d96 | -3.10064 | -49.46002 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 587ce750-6b34-3fa4-b7d2-13ffc5c9e265 | -3.14348 | -53.14322 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29cb477d-dbc0-323a-ae5f-77eed292c87d | -4.09429 | -51.05352 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8714a7b7-466a-3264-9816-bfaaffdba087 | -4.0998 | -51.0493 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ff6dc12-e24e-3e90-b6b1-2b0dd739e48d | -5.79096 | -48.62329 | 2025-10-26 05:21:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c13a866-505d-36c7-847d-f80892c523eb | -3.09736 | -49.44633 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebd7319b-b651-3aac-9592-833775a68234 | -3.87091 | -52.19037 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3215a311-2dec-3a67-a017-4bfd06434785 | -8.0443 | -46.74319 | 2025-10-26 05:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1f0c947-f852-327e-bf5b-7aefc7d928da | -6.54329 | -54.97252 | 2025-10-26 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bc94efb-4224-3205-b479-890787aebe22 | -4.27144 | -50.5122 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb6e248b-dd2f-3e81-bf3d-0bb4032b588a | -2.81699 | -49.14974 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 966a0e96-15a3-3269-b8f7-8148706712a1 | -3.60822 | -49.35186 | 2025-10-26 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46af9c19-deab-3b50-8d84-69e4eee5bb56 | -3.79812 | -52.0183 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e52481b6-c34f-3eca-9f73-74a58bd5a3f5 | -4.57982 | -46.51248 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 360c1c82-1d6b-3792-8f7d-ebf5907cc437 | -7.77846 | -45.38739 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 496effe4-2e7e-3d6e-8ec8-f4ce3f46c16d | -4.29634 | -49.29227 | 2025-10-26 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73bf16b6-6394-3c7d-b432-db48f792a29d | -5.50701 | -49.57684 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d2de0cf-2c97-3140-9366-53cc61c5a831 | -6.39714 | -45.77863 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d13b04b-46b8-3b6a-946e-78d801261c8c | -4.10237 | -50.4493 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c934bcab-0d56-3959-8f44-8ea91019ebd4 | -2.12596 | -56.84584 | 2025-10-26 05:21:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31d578cc-9b7c-3c39-9ca9-721260011a1e | -2.3245 | -48.58365 | 2025-10-26 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 605aed94-1b1f-3dcf-970d-d5caac61518e | -4.72247 | -47.42081 | 2025-10-26 05:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b1422fb-1df4-356c-9206-15c2a0f2f991 | -4.86577 | -48.65034 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e04860f7-e87d-3bb4-b0be-43c7c1f379bc | -6.09554 | -47.05409 | 2025-10-26 05:21:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faa42263-5731-3d0a-bb19-757ce0564235 | -2.65071 | -48.50698 | 2025-10-26 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbe6d477-97f3-3a18-84c8-a462bf537b31 | -3.38251 | -52.3704 | 2025-10-26 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4a33161-06bc-3a18-90f3-2b3520ad562b | -3.83419 | -50.19604 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1336af76-5bf6-3684-8a1c-89c2470bda83 | -5.88929 | -49.65487 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10d161ac-7932-3397-9050-63a85319b829 | -8.69609 | -50.82816 | 2025-10-26 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca5245b7-7ffd-342d-8b6d-d30a55ab67cc | -3.10192 | -49.4502 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa00765b-bd51-3e85-be80-6a21f2b00c49 | -3.60873 | -49.34845 | 2025-10-26 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8470f76a-0e1d-31b9-8bf7-b71e62529004 | -3.72942 | -58.58976 | 2025-10-26 05:21:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5bd2de7e-8a26-350c-bc1c-87bcab11c9ae | -3.12155 | -49.10788 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5917edf-0c28-35bc-a8c0-75e3c2c5dc44 | -4.91073 | -48.62092 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f42ae0e-a2e7-37e3-b085-5ea10209ae63 | -4.61821 | -50.50848 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f5d1e54-5a03-31eb-9fc8-16c73008dc7f | -2.78513 | -54.41866 | 2025-10-26 05:21:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 134cdd61-6733-3ce2-a388-9b90905f0729 | -8.53421 | -47.20227 | 2025-10-26 05:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2cf4435-2f6d-316f-872e-cda69a6b63b8 | -3.37247 | -52.80215 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30c57d41-6782-3bc9-b09c-1760e0667a22 | -2.12933 | -56.84637 | 2025-10-26 05:21:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b89a37b3-a5eb-372b-8a12-cf5c7ac0aafc | -3.10211 | -49.45045 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a43dd215-56ae-3782-8e8c-9264d5dd2754 | -3.76297 | -52.25774 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5e1e469-264c-3b91-bfb4-8f319b87abf6 | -4.79844 | -47.88736 | 2025-10-26 05:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90eb58b2-795f-3015-988b-50a9ccbafa41 | -3.10113 | -49.45684 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc2da5b0-7189-301e-b1a1-38e2b1ab4569 | -8.4614 | -48.02375 | 2025-10-26 05:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f8eaa29-04d0-3fc8-9c1c-49a2a695f0f7 | -5.50653 | -49.5802 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3e50af4-8657-340d-9adf-54fdb44889c5 | -4.93292 | -48.55874 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4386399e-33cd-3a9d-84fd-3e9b49e7e158 | -2.98566 | -52.62528 | 2025-10-26 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e87e72a-3fd0-39ff-966b-1bc42f5f41b2 | -2.33001 | -48.58447 | 2025-10-26 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a520ab00-8022-31d7-b5f7-9c1bd4e7177b | -4.71063 | -46.4338 | 2025-10-26 05:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fa0e8ec-5f02-31b8-933a-51c7bef93bb0 | -9.09237 | -49.64306 | 2025-10-26 05:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
