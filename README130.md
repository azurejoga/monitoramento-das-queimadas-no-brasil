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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74b04e13-292b-3b23-9903-6bce9b68f0e7 | -7.02869 | -45.86017 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7bf12ac0-c802-3b31-88ab-52b4094b2ccc | -7.62367 | -55.29364 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 020a7cce-e6ff-34ff-9d9b-220ac69a18d5 | -6.25693 | -53.67444 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bef98b2c-b0aa-3ddb-98d5-e31235718e1f | -7.82313 | -44.47305 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e7be3e7-662b-3cbf-931d-fae1d10764a2 | -7.1119 | -42.76052 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| bd84b954-d7f3-3caf-9d91-944d8e5130ec | -5.76277 | -44.11752 | 2026-08-31 16:33:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b0c98962-50be-396d-9301-f2b9ea746885 | -5.53539 | -46.59941 | 2026-08-31 16:33:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc738e2f-6265-38bf-a09f-19c556d8c9a6 | -3.40718 | -43.37478 | 2026-08-31 16:33:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 79320fc3-bad0-35b0-8cc1-fd6aec991762 | -5.31664 | -55.85738 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ceb35b1f-df63-32ed-a7e8-5cccf35dbe9e | -6.62676 | -53.17804 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7c5d4ca7-48ed-308e-853b-25e2820c461d | -7.60016 | -44.93263 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1141e89c-9413-3284-8445-43c20abd3912 | -7.7859 | -44.06194 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b5e62a2c-51bf-3cd2-a327-6a4ba1eca8aa | -1.75933 | -48.22963 | 2026-08-31 16:33:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 342eb8d8-57de-309a-941d-b3580967c914 | -5.62775 | -45.57636 | 2026-08-31 16:33:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38475070-c263-32e2-82c3-fd8f1dd86a50 | -6.25 | -53.67365 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6fb757c4-1082-3905-81aa-430c6b93ab9c | -7.00665 | -52.8902 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 87d40860-2e50-33da-a2f7-561395964561 | -6.95288 | -56.51574 | 2026-08-31 16:33:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c342b8e-91ba-3fb6-953b-d3af9506f309 | -7.11137 | -42.75704 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 4aa5fcc0-7d2a-326e-bcc1-cc6915b7925f | -5.851 | -52.39212 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ce94226-0906-358b-875c-d3b80e37e005 | -4.96528 | -55.85905 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9044a21b-5895-3429-9877-a5accc641e26 | -2.83976 | -43.6133 | 2026-08-31 16:33:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 0bc56e09-2f0f-3103-be8e-09b69e6fe42b | -6.86438 | -41.69502 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5d8c8fb7-68d4-3c05-b9d2-208bfddf224d | -5.90038 | -46.12802 | 2026-08-31 16:33:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 46892c6f-c923-36cc-abed-5186ce4e1234 | -2.62252 | -43.45617 | 2026-08-31 16:33:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70df5eb5-ada2-3823-91b1-b6ea061d8846 | -7.77118 | -44.05632 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ec25bbf6-030f-308e-8640-c4a0be2fcd05 | -5.39042 | -47.71908 | 2026-08-31 16:33:00 | NPP-375 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| f09b8bdc-f256-332e-a5db-680af452f94c | -8.12669 | -45.56836 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 74086e7a-78ad-3333-b384-44d83e21cabb | -7.99278 | -44.2818 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 1f4ca2cc-0c76-3d8f-b1ce-04ccd327c756 | -7.61788 | -44.88168 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 820e6742-d7bb-3d5f-90e9-a45e8ac03bc5 | -7.42455 | -45.27113 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 18ce46c9-1245-38ee-857a-01e5773050ec | -7.63477 | -46.73763 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92907a78-37f3-3382-95fa-cf12124d1527 | -5.58279 | -42.334 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 90a057e2-248b-36bc-b3e7-89bd97a1dc91 | -7.56185 | -44.33476 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 510aac99-2d7d-3131-b563-14474a77f0fc | -2.51907 | -44.15286 | 2026-08-31 16:33:00 | NPP-375 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 922d09e6-e6ac-3a88-8d63-1e63c9c96344 | -7.05452 | -52.7204 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a924bf22-05b9-39a1-9dc5-d432bbdc7a3a | -7.41865 | -44.26124 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 34d03b73-67ff-332c-bf05-0b0d3db7fc86 | -1.58511 | -48.63849 | 2026-08-31 16:33:00 | NPP-375 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9823e61d-7f7d-3f7f-9cd3-e0ec2ddb10df | -4.14352 | -38.57755 | 2026-08-31 16:33:00 | NPP-375 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| c5f1c27a-e6f1-327a-8eef-02f116ab82d2 | -7.78808 | -44.07671 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| bcdfb8b6-5dc8-3993-b054-109dc51c0199 | -7.95501 | -44.26453 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| deed7bf5-baf5-3b7d-867d-627061210c4e | -7.13091 | -42.81821 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9f64288a-2ee8-3c93-b34b-82d62a8dd637 | -7.00752 | -52.89028 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0584b227-e22d-30ee-ad3d-3865f9dfdd9c | -3.54105 | -49.47275 | 2026-08-31 16:33:00 | NPP-375 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 053e0e70-587d-3f78-bdbd-17c7539d722b | -4.73611 | -56.26571 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b649ca85-3ec1-34e7-b32e-4b643076b003 | -7.09621 | -45.79074 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a0c204ea-1d5f-3362-8b39-c8e4dc7c7a3c | -7.0568 | -45.41939 | 2026-08-31 16:33:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e4451eb2-ea68-35fc-aacb-db96ccbfd626 | -6.86968 | -47.99778 | 2026-08-31 16:33:00 | NPP-375 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fe13d1ae-7b55-36ff-abbd-aedf4f265fa9 | -3.05936 | -48.74751 | 2026-08-31 16:33:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a70e4895-7ae7-3bd4-a658-235423378efe | -7.79095 | -44.0725 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| db0878db-554d-3a5d-afb7-a4f45ec85551 | -5.63656 | -45.56793 | 2026-08-31 16:33:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 922fc5fd-d628-360b-acbe-4cdc41a2b130 | -6.67423 | -52.86796 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f54b85da-cc59-3baa-93a8-bfb149221269 | -2.6192 | -43.45667 | 2026-08-31 16:33:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea321ab0-8b58-32f9-b3b3-b6f50c29e2fe | -7.98703 | -46.52391 | 2026-08-31 16:33:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 37a607c3-91b4-37c5-920b-efbacbfb4e2c | -1.75541 | -48.23022 | 2026-08-31 16:33:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 951e64af-4564-3dc8-adde-438c02a53cbb | -7.48535 | -45.37476 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9c50fa8b-8a7a-3363-8bca-1a58aeedcda3 | -5.87917 | -52.15617 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6e745bca-7c6a-31ca-8fef-0fcd3f772c05 | -7.63802 | -46.72929 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b18477e7-ea8d-3cfe-9c49-3bf63e92ffc0 | -8.38917 | -46.46386 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 24943d11-8fc4-3478-be86-c3e2baba3dcd | -8.08172 | -45.46131 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a5fac5f6-f3df-3e98-96a1-ca535e9a8ea6 | -6.75619 | -52.9074 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d3c03952-9440-3752-bb31-bbc9b1250e97 | -7.92687 | -45.00317 | 2026-08-31 16:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1f1d4b84-17aa-3642-a1a0-31c521ea2c69 | -7.93737 | -44.24035 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a9319589-4c7d-3c58-8463-e2ceff9f1457 | -7.11084 | -42.75356 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 36c96a97-9894-3d25-b37f-e6f625d7b4ce | -7.1398 | -44.30713 | 2026-08-31 16:33:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ab6d933-c1b6-3599-b037-ab6b3cd8604c | -7.52227 | -44.44835 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7abbfe3d-c09f-3fdb-a645-c7feea8981f6 | -7.44113 | -44.9512 | 2026-08-31 16:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| da3019f5-2456-38ed-ba1b-636adc6d0920 | -7.91232 | -44.25209 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aedea94c-ca51-3fd4-891a-840d430b98cd | -7.63666 | -46.71964 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d3f9f362-7ccf-3928-a764-1da94fe7ad19 | -4.59562 | -42.92451 | 2026-08-31 16:33:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f35c59d7-67b3-3327-8043-94374c41fef9 | -8.12723 | -45.49432 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 234ef65e-df2a-378c-a2fe-23a88622dc7e | -7.16477 | -44.68766 | 2026-08-31 16:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 556547a4-82d4-34f4-afe2-bc820dcbc620 | -7.99025 | -44.33587 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| cfff9673-a3ef-38fb-935c-c3b432c24a1c | -5.63598 | -45.56396 | 2026-08-31 16:33:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| eb28532b-e1d4-3f8f-acff-7bb96a4e4c86 | -4.67163 | -43.22124 | 2026-08-31 16:33:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8d292424-fa99-3d57-ac4b-f6100d3f9b97 | -8.22186 | -50.77899 | 2026-08-31 16:33:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea11e82a-589c-333a-84c2-d0f8db0493ac | -4.91459 | -40.66954 | 2026-08-31 16:33:00 | NPP-375 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 63fa4880-ea73-351b-a358-95d66ccb2b02 | -2.79983 | -49.57778 | 2026-08-31 16:33:00 | NPP-375 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 7c5110a3-e766-3dc3-bff7-4dbd16a62d94 | -7.61437 | -44.88221 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| c799f2a0-145c-32f2-b0e3-1312718430fd | -6.87216 | -41.70105 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 9c9923b2-d3e8-3f73-9ce5-3738e5d961a8 | -6.15322 | -52.64083 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| de3529a1-68ad-363f-86d0-f634ccb726b3 | -5.53913 | -46.59886 | 2026-08-31 16:33:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e6229929-3964-3a2e-9ce4-38e80fb0356d | -7.222 | -42.77209 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 28207945-f104-3cd1-8e27-8a20b1fdbc78 | -5.58333 | -42.33749 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 024443e7-0fec-31ea-a49b-b1d1fe779513 | -6.13225 | -53.52972 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| b1c4b145-3acf-3dff-bc01-1bd1885ababf | -7.95157 | -44.26509 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d1e69686-fed7-3e0f-9d13-1829c182b892 | -8.61067 | -54.825 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b4d90b52-a564-36f9-914f-c6b3019be787 | -7.36071 | -55.90421 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 2a7ef715-1d6b-3d65-8baa-c803332cda5c | -2.43182 | -48.43311 | 2026-08-31 16:33:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8f27ac5a-4ba1-312b-a2ee-45e65e96ff8d | -4.29885 | -49.09052 | 2026-08-31 16:33:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| aa227001-1086-3b8d-ac78-2caf8bbe72c1 | -7.64577 | -46.72818 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 230c11a8-e017-3105-adf5-08e73af6cab5 | -5.84042 | -52.39708 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c8fd3642-3bf0-3e2a-a9d4-d37a809d9d2b | -7.09438 | -45.77815 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e820ba62-9368-3492-a6f4-279ad81cb53d | -5.28108 | -42.78473 | 2026-08-31 16:33:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7181c75f-8757-3742-b01e-d57851e5bfea | -5.58892 | -42.32951 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f6df1a11-f019-350f-8cc4-ddba55a1a56e | -3.65412 | -54.85251 | 2026-08-31 16:33:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d9b5271-5457-3b14-b0b8-7755199ec84b | -2.881 | -43.59917 | 2026-08-31 16:33:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 5f06f7f6-aa31-35a6-be18-8435550fcf0d | -8.20967 | -54.94989 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8e60bc5b-fc48-336a-b5bf-4c104db76ed2 | -3.0423 | -57.40652 | 2026-08-31 16:33:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c0a0bb77-5416-351e-899c-7d7bd29ce584 | -7.36036 | -45.08404 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e270e34a-973b-30c1-9e89-78e1a613e81f | -6.40698 | -45.42778 | 2026-08-31 16:33:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README131.md)
