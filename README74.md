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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48709d00-85c4-3175-b554-3b1fcc8a133d | -11.487 | -43.4981 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 929dd1cc-62ef-3b07-a52c-95f2bb4e7428 | -10.3034 | -44.6249 | 2026-10-04 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 8a5c6624-bbf3-3ce7-9017-3d25277cd12a | -9.9175 | -65.0313 | 2026-10-04 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5b280ebd-a36f-3980-85e3-800bb0aca56a | -11.3927 | -43.418 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 4ce76fa9-c0e7-30c1-b8c8-60eb28c32c68 | -11.3555 | -43.3526 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 20b9e2fc-0ba8-3491-874b-2696a7993d00 | 4.1526 | -60.3836 | 2026-10-04 14:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 64a48f2b-27c9-3857-9fe1-b02dd2f898ba | -11.2058 | -44.2448 | 2026-10-04 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| b5c0ac72-dd26-3b76-8a03-5567e1bbae07 | -8.3397 | -44.1658 | 2026-10-04 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c7611b39-e77c-3514-82c8-403e3d7889e0 | 4.2065 | -60.6865 | 2026-10-04 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| ecc73cb4-ee0e-3940-8327-5e3ef2d400e4 | 4.1883 | -60.668 | 2026-10-04 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 84.2 |
| a5de9f1c-6a1d-373b-8bd5-2277fcc6ef64 | -11.4674 | -43.5248 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3addad0a-86c1-33ad-a490-e3f322f6cb63 | -11.4102 | -43.5099 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| ace0c0a5-837b-331a-a6b6-14f09ced36c5 | -11.1775 | -44.7832 | 2026-10-04 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| dc7eeaec-af83-3054-8beb-ead14c9ae778 | -11.8315 | -43.5391 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 3b390888-630f-3cbd-ab5e-2a925284cc14 | -11.3204 | -44.2514 | 2026-10-04 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 1c1146cd-5202-3b18-8d9d-fc6e0c18ded7 | -11.2758 | -43.5303 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 7ad32ce2-ee62-3e99-8e78-ac823007fd8b | -11.3551 | -43.3764 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 473dd7ed-5586-36ff-92b3-89d9e0d5693c | 3.8215 | -60.9792 | 2026-10-04 14:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5a05b2c0-25f8-3843-bce3-64413cb0d54d | -11.4691 | -43.4299 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| c8792880-5662-3b60-8750-4e47d7fc2ffb | -11.2242 | -44.2888 | 2026-10-04 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| ae47e561-71ec-3081-a103-3e00d1ba1682 | 4.1697 | -60.7443 | 2026-10-04 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 09c3a3cf-8fe6-36a0-86b2-cfe6e44daa30 | -11.3918 | -43.4654 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f604550a-d170-3e0b-9f01-5a738aeba743 | -11.411 | -43.4625 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 4718c6ee-ef22-3dc8-b242-de75ab76d761 | 4.1702 | -60.5924 | 2026-10-04 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 72502e62-7f3f-30da-9f52-946bfd9bc41a | -11.2246 | -44.2654 | 2026-10-04 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 59bfbacc-a92f-3a9f-8fd8-b74c63ba607b | -11.8127 | -43.5184 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ac24a502-7d85-31ef-8097-9ccd3cd4d06c | -11.3935 | -43.3705 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 7298e4d7-d345-3bde-9934-e5f6a08834c1 | -11.4106 | -43.4862 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| e0dcf7e6-94ef-3765-8c9e-6bee2adf6133 | -11.3931 | -43.3942 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 2d533063-2666-3782-b03c-69c711b8ab13 | -11.4495 | -43.4566 | 2026-10-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 548b5636-44dd-35ca-ae70-f12d161a494b | -6.6129 | -43.7317 | 2026-10-04 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d81a7e65-86d9-31ef-afde-48b5bfd6e794 | -12.1967 | -57.1103 | 2026-10-04 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6ba5032d-1f5a-3e51-9a01-abeaf9170c3f | 3.8215 | -60.9792 | 2026-10-04 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 439f578f-96b5-3864-9471-bc0072a92065 | -11.4674 | -43.5248 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d84e1f2d-24a1-3a55-b5ce-fade711e967f | -11.3918 | -43.4654 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fcbe843a-bdc7-3aab-9921-d9934d87c394 | -11.3204 | -44.2514 | 2026-10-04 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| b7b47b6b-cab9-357e-8741-23492b66a480 | -11.7935 | -43.5215 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| efd272fe-e449-3208-9078-9b35a9c5ec4c | 3.678 | -60.013 | 2026-10-04 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| bafe4f3c-9bb1-3f98-8dfd-6fecc8d900e0 | -11.7375 | -43.4356 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 2d336cf7-f358-3a6d-a9c3-97728fc5de10 | -9.0844 | -44.9811 | 2026-10-04 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 134fc2d2-a903-3173-af0f-566b3a968453 | 3.6573 | -60.8499 | 2026-10-04 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| f9db062a-47db-3df1-a1b6-37b92c9bd223 | -10.303 | -44.648 | 2026-10-04 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c1fb325a-1487-3fc3-ae78-7ecc5ba26cc4 | -11.7733 | -43.5719 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| f3ea2752-1eb1-3f19-af1e-ae7b168fcad5 | -11.7174 | -43.4861 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| db735a7a-a62e-3797-b06d-746bb922649c | -11.8118 | -43.5659 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| d79038db-39e1-35be-9bd4-b9701f820b62 | 3.6966 | -59.9173 | 2026-10-04 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5becb9da-0e0c-3bb4-9370-fc2a43820cea | -10.5318 | -57.7549 | 2026-10-04 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 38ab913a-cca8-3c5c-9703-14ed1148ead1 | -11.2442 | -44.2392 | 2026-10-04 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 08c1ccfa-e55c-35cd-be0e-f9cd826e82c8 | 3.676 | -60.7168 | 2026-10-04 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e7bd2662-cd1e-3ffe-8be9-fcc49640e5e5 | -11.4678 | -43.5011 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 845b4235-d4cf-3c54-9a96-df63f18374fa | -11.8123 | -43.5422 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| f3449c4d-ed0d-38d0-9ece-ed4efa7a8930 | 3.9686 | -60.6918 | 2026-10-04 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 83a27a2b-38e2-3201-8c7f-afc846d62f6c | -9.4751 | -64.3336 | 2026-10-04 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 3e966e56-25ff-3deb-981c-385a0eedaa3f | -11.2621 | -44.3066 | 2026-10-04 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 37163749-8a5f-33af-9755-ba585a9e69f9 | -11.2438 | -44.2626 | 2026-10-04 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 35b739c7-749c-3490-adea-adb3adbc8523 | 3.7483 | -60.9807 | 2026-10-04 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 80141497-d9da-346a-acab-7914987c43a9 | 3.8215 | -60.9603 | 2026-10-04 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 114530a0-605c-3352-bcb5-671e409f3ecf | 3.6753 | -60.9632 | 2026-10-04 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 7f06bce7-0b4b-3903-b008-60e1338fa485 | -11.2566 | -43.5331 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 1f0274ad-4065-3f79-9b19-c959e4165cc6 | -11.2758 | -43.5303 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| e775e0ce-e23d-3186-8e13-02863c50a215 | -11.4687 | -43.4537 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| be015bc0-8d69-333d-be55-91b23e1b2f40 | -12.1967 | -57.1103 | 2026-10-04 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 67fdd98d-1aa1-3615-b0de-2ec6c8ffd150 | -11.2629 | -44.2598 | 2026-10-04 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 80f0085a-a128-33c3-a954-14d6a388ec84 | -9.1613 | -68.2568 | 2026-10-04 14:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| bcfb80b4-9782-34b1-b55e-59a166632bf6 | -9.9175 | -65.0313 | 2026-10-04 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| aa97806d-40dc-341b-80ba-48b11a1247de | 4.1697 | -60.7443 | 2026-10-04 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| eae399f1-cad1-3cbf-b339-bc2920b41458 | 3.8214 | -60.9982 | 2026-10-04 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 4601be1c-777b-316d-bdc1-9cc041031642 | 3.6393 | -60.7554 | 2026-10-04 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f0575dca-1842-3eec-9e4f-d6e44d1d15d2 | -6.2162 | -52.7876 | 2026-10-04 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 033b0b00-7aea-3e54-bbe1-59cd62d43840 | -10.8189 | -57.1993 | 2026-10-04 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| b48d9028-a9e3-3255-a5a0-27dff4e5079a | -11.487 | -43.4981 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 6e781cd4-a93f-3da4-b355-9fe91b536cf0 | 3.843 | -59.895 | 2026-10-04 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3c1dd7fc-1c3a-325c-8c69-efe6e1a41544 | -11.8315 | -43.5391 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| b188cb1f-619c-3068-b13f-018c62100dc7 | -11.793 | -43.5452 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 0dbaaeba-3d3a-3186-96a4-abce785d8723 | -11.4866 | -43.5219 | 2026-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| e2e1bdd2-baef-39d3-9081-c6466b6eec38 | -0.4319 | -52.0151 | 2026-10-04 14:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 7907c7e4-64ce-3e6c-af9c-7ce4685f0e94 | -11.3013 | -44.2542 | 2026-10-04 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 7ad4af0b-5ee3-3db2-bcdd-4692d96079d0 | 3.678 | -60.013 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 24aa92ff-5b28-3db4-8ae3-7a84fcf410cf | 3.9136 | -60.7309 | 2026-10-04 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 8d31644e-6da4-3c77-92d1-a2f5d86ce20a | -12.1967 | -57.1103 | 2026-10-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 051db3ad-c396-3aab-a5d4-50294803424e | -10.8187 | -57.2192 | 2026-10-04 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fcbc6287-d865-3ce8-92ed-c9643c7aa811 | 3.9686 | -60.6918 | 2026-10-04 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 732230ae-560e-326d-b3d2-986c00764362 | 3.4155 | -51.3021 | 2026-10-04 14:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 45ce870e-f3fe-3737-87d0-fb1dfcea3be4 | -9.1613 | -68.2568 | 2026-10-04 14:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d7092d35-acac-309a-a03a-33c74bcd7c78 | 2.8909 | -60.465 | 2026-10-04 14:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 5a17a5fd-00a4-35cb-9557-35b34e61a8a8 | 3.6393 | -60.7554 | 2026-10-04 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f381c2f4-b01e-3a52-9ad2-d0ca7a676611 | -11.2561 | -43.5568 | 2026-10-04 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c01141f5-1418-3c11-8b2a-226efd903ade | -11.4682 | -43.4774 | 2026-10-04 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| d5f49e00-8fcf-3964-88c0-4bf1da33036e | 3.8965 | -60.3322 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c2720ac7-b01f-34c6-b879-5865403c74f1 | -11.2246 | -44.2654 | 2026-10-04 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 3aab67b1-f7b4-3f2a-bca4-f37051361ab4 | 3.7148 | -59.936 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 3abaea69-5bb4-3a99-a973-cae121afddae | -11.2629 | -44.2598 | 2026-10-04 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| bc501198-c339-3b88-a926-d714f02f75eb | 3.6211 | -60.7368 | 2026-10-04 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ba9700e4-c4fe-3dcb-8b2d-38642d44914c | 3.8953 | -60.7313 | 2026-10-04 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 938a11e2-b3f9-3163-a974-ab62f3f2d255 | -11.3013 | -44.2542 | 2026-10-04 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 5c978335-4ef2-3aad-a17a-0bfee1923918 | 3.8215 | -60.9603 | 2026-10-04 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 1b64b7b3-32b9-3ee6-aa7f-801d74e677ab | -10.8189 | -57.1993 | 2026-10-04 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ae28c2b2-c845-3e00-aa25-bd184d181591 | -13.5197 | -61.1319 | 2026-10-04 14:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 68df5065-7867-3a13-a87b-89ebde056b45 | 3.7504 | -60.2592 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 78afca41-7748-3be4-991e-656d664efa0d | 3.843 | -59.895 | 2026-10-04 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |


[Clique aqui para ver as próximas entradas](README75.md)
