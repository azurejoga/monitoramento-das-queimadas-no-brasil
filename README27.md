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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7fd30f5-0d72-3105-bc6e-d5426254be0c | -4.21498 | -50.08724 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab667ef6-7037-389d-9b24-35ee85aed6d5 | -4.84859 | -43.43651 | 2025-10-29 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96487a94-65a1-3d27-831b-5b6888e1e914 | -3.78709 | -45.59694 | 2025-10-29 04:21:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f44f5ba8-663d-3015-a53b-54eb63abc52a | -3.73861 | -49.70401 | 2025-10-29 04:21:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 456e29f1-0ef9-34e2-8591-abcd203533ef | -4.91981 | -44.70102 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57aced1b-f1c4-3de0-9c03-672c2a0db170 | -3.40731 | -52.72597 | 2025-10-29 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38d91984-66db-336e-b663-1f9cc08bbb1e | -4.52006 | -47.83884 | 2025-10-29 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8c35707-4cc5-35e3-9187-73a649049ffb | -3.04003 | -50.26869 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bbc9742-ee13-3115-b973-5b3276a186e2 | -1.50643 | -53.16104 | 2025-10-29 04:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9c23532-1908-3f81-95fc-4ed52ffe7025 | -4.3531 | -43.63898 | 2025-10-29 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a2a64b8-b5a8-3ae6-a312-cc7890e05338 | -4.51223 | -46.00045 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4b2cc63-14db-3d7d-a6e5-e643b9ae8af9 | -3.91348 | -43.32016 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ab73cb-4be3-361a-98b0-0b492e3adc91 | -2.4253 | -49.31049 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6680b2e3-b6ac-353f-adda-0ca4144b5f80 | -4.48234 | -43.44064 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2afbcb0f-f50d-35ed-8fd6-e2a762ca4fae | -4.0019 | -49.03672 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12df7478-e7b1-3d64-a8cc-1fea94691581 | -5.11165 | -44.70972 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 746875ca-3940-3370-83d0-f3c04b42eacc | -4.0099 | -49.03804 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6cd307b-855a-3509-b568-6a7a690c7713 | -4.01077 | -49.03284 | 2025-10-29 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32dfabc0-f185-3983-937d-ad49268f9399 | -3.89423 | -40.79822 | 2025-10-29 04:21:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9c4b541a-3d80-39e5-8dab-a3195d68aa23 | -4.48624 | -43.43766 | 2025-10-29 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d093b59-19b6-3886-aeaa-460169b52dd5 | -4.21203 | -50.07849 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04d1bd13-ca88-366f-851c-d9856fc5cc47 | -5.0086 | -42.50078 | 2025-10-29 04:21:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 98c4166f-79b3-3238-81f1-21afb3e45f90 | -4.29412 | -44.48821 | 2025-10-29 04:21:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a09bc31f-e170-3406-8cd7-f2607df4a614 | -4.43515 | -48.01066 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96013e7a-371c-3f85-8c5b-dd9251e3fa42 | -4.80356 | -42.96723 | 2025-10-29 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d10dc50-caec-3523-8725-ebd638139bd9 | -3.7837 | -45.59641 | 2025-10-29 04:21:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7b4d7f7f-cb76-37ed-a084-c2d0601cbfd3 | -2.42234 | -49.30224 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| db490c55-6b7c-305a-9b23-1b43b0f157f0 | -5.65412 | -41.14466 | 2025-10-29 04:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cc51ce57-50bd-3654-a99d-102d9e1bef0c | -3.42462 | -50.11439 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bf224d8-266f-35b0-93ed-dc37c6f2fba4 | -4.20642 | -50.08587 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5f3f8278-de5d-3bb1-abd0-04bc884b7099 | 1.83706 | -50.50567 | 2025-10-29 04:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cea48a34-658e-37b0-ac7e-bc4aa324e637 | -4.65399 | -42.5153 | 2025-10-29 04:21:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 61bb47ec-8c1d-35b4-8a94-1569b41261e5 | -1.49584 | -47.80778 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 026bf5a0-96de-30b0-922c-a201ff6c49c4 | -2.77073 | -45.40124 | 2025-10-29 04:21:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac6979d1-927e-30f3-b256-27d317b73399 | -3.12641 | -49.10033 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b526592a-74ba-3075-b432-0cb8a8dd41aa | -3.73903 | -51.34334 | 2025-10-29 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e27c5219-65cf-3057-acd2-ef5cc794a76f | -3.0479 | -49.51655 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc98d9ea-dc89-300b-bec8-a39f61c68d03 | -3.94629 | -43.26418 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb4e9c6f-7dfe-3761-b19e-429708802ebf | -2.82996 | -49.39715 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce058f54-1d3a-3112-ba62-e72b2255dfea | -3.78981 | -43.32975 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b49d7cf2-6f88-3f4b-b0c7-3b482a3a128f | -3.11781 | -40.99236 | 2025-10-29 04:21:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab2f948b-2889-3aee-a737-b1efd56be4a9 | -4.74493 | -46.45917 | 2025-10-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d2d8f75-14d4-301e-ac87-2a17960cfdc4 | -2.22615 | -48.37523 | 2025-10-29 04:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf12618c-9620-3039-8587-ef9357b2380b | -4.726 | -46.81738 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33fe253d-0aae-3fa8-b074-e2eb478059e3 | -3.47958 | -52.86725 | 2025-10-29 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2eaee90f-fd16-3c64-9897-6a42e136b885 | -4.66067 | -46.39995 | 2025-10-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2c8878e-ac51-399b-b299-97f5988c588f | -5.48968 | -42.16507 | 2025-10-29 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2b0c0358-de31-3b81-8032-30b1b7dc4bf9 | -3.32684 | -52.62866 | 2025-10-29 04:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f267b85d-4eab-301a-b292-40c857170155 | -3.79036 | -43.32626 | 2025-10-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db85e197-7ac8-3dba-bd09-fbf0154b7909 | -3.58041 | -41.04453 | 2025-10-29 04:21:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61842520-9af1-3b33-9432-fd95168d7a3c | -4.03 | -50.4474 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9498932-f48a-3d7b-a77a-e145c641bab4 | -5.02412 | -41.89159 | 2025-10-29 04:21:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2fe0753-c4d6-33f1-beb5-7b8b37d5d742 | -4.30192 | -48.06841 | 2025-10-29 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 259c0983-e281-344a-a000-a59a48319c04 | -3.04429 | -50.2639 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3f42f9a-656c-3901-a03f-7eda1bd783fb | -4.52682 | -46.04028 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b678700-de9a-30a1-8f31-cabea7068bea | -4.21431 | -50.09125 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f22c40ab-1fff-3cb0-a2ed-d938e383d677 | -4.35256 | -43.64245 | 2025-10-29 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39aeabae-7191-3bca-bb94-b6e8edc12af0 | -3.04445 | -50.26937 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a882a240-4f49-3e08-ba45-d02be96d3201 | -3.12926 | -50.1864 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95bd045c-c2ee-38e6-a9da-b4ce61cee813 | -4.75769 | -46.97962 | 2025-10-29 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a6c95dd-dda7-3d18-b408-39761b3d5fd7 | -4.66412 | -46.40051 | 2025-10-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b696728b-7ebe-3da1-ade5-d522a678ce2d | -4.71032 | -46.13687 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7acc6e9e-a679-3ddd-8f97-1473f07f0b4a | -4.20775 | -50.0778 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5c94928-07af-3cdb-823b-e4d28a176bcb | -3.23155 | -50.65489 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90dd5cdb-8e31-3aed-a9c9-277e8d00de5a | -3.431 | -50.10275 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c4f3694-b94d-3fe9-82c2-7f8107d2468c | -3.32232 | -54.0892 | 2025-10-29 04:21:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf86813f-5ba0-3879-8681-b896582b402b | -3.04286 | -50.27244 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afc3e977-d768-39be-9d4a-db496314c9fc | -3.5429 | -53.31934 | 2025-10-29 04:21:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9f9b41d-fd07-310b-a24d-66fb0269080c | -4.08549 | -46.94169 | 2025-10-29 04:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06059f59-8337-374b-b929-4eff640efb96 | -5.02425 | -44.80961 | 2025-10-29 04:21:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c8d4602-d26d-307e-b56c-4acb88a771f7 | -3.12685 | -49.10063 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b12d5f96-f038-38ac-a7bd-352cd9f47120 | -2.42174 | -49.30603 | 2025-10-29 04:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 730986ec-24b9-3c16-82a3-518dafeda94a | -5.64065 | -41.20806 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a807445d-0e02-3669-96d9-22c591fdeb50 | -5.53104 | -41.70763 | 2025-10-29 04:21:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4166867d-7746-3e79-9e7a-0af6ec803620 | -1.49308 | -47.80937 | 2025-10-29 04:21:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 71c4d9ba-aa28-32c3-a451-ed2a35d9dcd9 | -3.38075 | -49.96608 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e532873-54dd-3e1f-bef3-e458af9474d4 | -4.20709 | -50.08183 | 2025-10-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b841e765-a7c7-332e-a7a1-0b313b1700ee | -3.12628 | -49.10423 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9202099-e989-36a3-88f4-bc6f01371cbd | -4.08484 | -46.94569 | 2025-10-29 04:21:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49e2d720-5ad4-38f0-b771-fe7cbbe3ccf5 | -4.35644 | -43.63949 | 2025-10-29 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac7d14fc-7aff-39df-9ea0-425a9b297d08 | -4.75832 | -46.97569 | 2025-10-29 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62b6d9aa-14ba-3ad9-bfeb-d13424f6b716 | -3.38459 | -48.94729 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9b44041-a1fb-34f3-9c64-a7b6dcee4f30 | -4.66669 | -46.87331 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9db0f31-bef0-37b3-9e5c-9bcf2c4a6b02 | -2.82936 | -49.40088 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f89eba-0ba2-30c2-8090-6a4bd24c7f8e | -3.38057 | -48.94665 | 2025-10-29 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c94987b0-be61-3024-aaee-c92825050e04 | -3.11422 | -40.99183 | 2025-10-29 04:21:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0d1e64e7-8af9-3e04-9ad5-2757320cbe5a | -3.04513 | -50.26509 | 2025-10-29 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4160a1b6-15ac-3656-b331-a821d6adec79 | -3.66396 | -49.81506 | 2025-10-29 04:21:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84724487-e211-3062-9170-436960f88ab3 | 1.83222 | -50.50644 | 2025-10-29 04:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8611dda5-9a41-3aaf-83b8-6707228ece51 | -2.77015 | -45.40486 | 2025-10-29 04:21:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1555d91c-7e29-3d49-a048-6fbf8487022a | -3.37822 | -50.14649 | 2025-10-29 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| deadaa8e-e8ae-3ca1-b15e-50fcdea42a88 | -4.08057 | -42.92222 | 2025-10-29 04:21:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12ed56aa-f3fa-37ed-90f2-0f1d1281250b | -3.78766 | -45.59334 | 2025-10-29 04:21:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9dccffae-14f9-3851-b5b5-5a8dba63ad44 | -4.72312 | -46.81296 | 2025-10-29 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4531f71d-0cd9-3f6d-b0ae-60f4bc184074 | -4.25328 | -48.58258 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 659e8549-575a-3b8e-8d74-60c18e52fed8 | -4.07664 | -42.92526 | 2025-10-29 04:21:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f59231fc-8d1e-3d2b-a683-a51872619d06 | -4.51283 | -45.99675 | 2025-10-29 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13187d25-cc10-38fc-9cb0-5f1f499860f4 | -4.92831 | -45.66923 | 2025-10-29 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebebf03f-3792-3619-acf6-6e6a2c796832 | -3.92305 | -47.6925 | 2025-10-29 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f55c93c-f039-3304-824a-c587900b1395 | -4.06359 | -49.36231 | 2025-10-29 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README28.md)
