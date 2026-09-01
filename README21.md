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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ace5ca48-f305-320a-a946-32ebf0965259 | -7.5709 | -60.4835 | 2026-09-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 70657170-b920-3f99-80db-8c6618a1aaf2 | -7.571 | -60.4643 | 2026-09-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 097d94af-5a6a-39fe-a654-6ecfb4486f8a | -16.0547 | -54.3908 | 2026-09-01 03:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1ed9bf6e-0207-3bab-82db-5e799e266aa2 | -7.5895 | -60.4636 | 2026-09-01 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 5bb07399-c644-389b-9069-d758a005a764 | -2.49735 | -48.13599 | 2026-09-01 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea6ec622-e6aa-3537-9e28-1a5ddb55c2f0 | -3.85776 | -44.08621 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fda8403e-c1d8-371f-9369-9091d61f2b47 | -3.86671 | -44.08384 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bfc1935-0c12-31c9-9d1d-7f5e1982389e | -3.87696 | -44.05312 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c9709b9-a34b-38a9-9991-b95577f964c3 | -3.86187 | -44.08309 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59fc7f7f-68bb-3e29-a5cd-bc5bb8fb856f | -3.86828 | -44.08265 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d218f1d-c267-3986-8209-68fb6b3811fc | -3.02278 | -39.97754 | 2026-09-01 03:53:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4425cc75-4d8c-3f02-b1d7-e57be3d30aee | -3.86778 | -44.05551 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d41e504-cea1-3433-bf19-968d1189eab5 | -4.09089 | -38.65768 | 2026-09-01 03:53:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fc82e010-4451-315e-bdcf-4263f330acb3 | -3.86277 | -44.07788 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f6cc963-b72e-35ce-af25-b35183cfd2e3 | -3.18332 | -48.02212 | 2026-09-01 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13489ad7-86c5-3df8-9875-7e62ecc5afd7 | -3.04547 | -39.93089 | 2026-09-01 03:53:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30f492bf-3636-3cb2-9cd4-e0fbf1797905 | -4.46546 | -38.50743 | 2026-09-01 03:53:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d4ffc4bf-f5a5-322a-a584-baf6e8c75b7d | -4.24789 | -38.09303 | 2026-09-01 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d430c7e-9c4d-34c5-9683-e45c64f7afa0 | -1.80079 | -47.71799 | 2026-09-01 03:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4e7f8e4-db61-391b-aa2a-e3c73a8c7dc0 | -4.25219 | -38.69742 | 2026-09-01 03:53:00 | NOAA-20 | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 38261cf4-110b-39ba-8200-8bba2b52933f | -3.86822 | -44.04625 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0bc6767-3559-3d22-a699-9bd5769b40b6 | -3.8726 | -44.05635 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a0eef19-ef31-302c-bff0-b86f50f30f98 | -3.87214 | -44.0523 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3694df22-023e-3c24-9b9a-0a18f023079e | -3.87305 | -44.04699 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12cd57fa-e5bb-3276-8a44-c6c0e3ff1767 | -3.86951 | -44.04498 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e3058af-3bbe-32da-bbb2-23b798a79528 | -3.86761 | -44.07864 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c277625-4d57-35b6-87cc-100e6180369c | -3.97208 | -43.10828 | 2026-09-01 03:53:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6085a835-83cc-3f03-8fb4-e5455e64d5ae | -3.8643 | -44.07666 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bf1b633-6539-346f-b3e1-fc7113839dfb | -3.87347 | -44.05102 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd995b73-b10b-33f2-8655-5f094f642035 | -3.97372 | -41.51595 | 2026-09-01 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7ae39bf9-1d5e-3de4-b48c-6fc2ef12f722 | -3.8555 | -44.06984 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fd19a43d-c6c6-3080-ac0e-0ba460e71126 | -3.1847 | -48.02911 | 2026-09-01 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb05efc3-c1b2-3da2-ac2f-9590b140c538 | -3.85947 | -44.07585 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93664e88-75c9-3dde-8b0d-f946bcdd33c0 | -3.87173 | -44.06166 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78b013a8-87d0-35d8-ae7d-83c8a37139ae | -3.05026 | -39.93412 | 2026-09-01 03:53:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 82d24d66-4e3a-399c-afde-8ef7eede2cd3 | -3.18559 | -48.02407 | 2026-09-01 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6623057-b6a6-34b5-9809-3e626d906e28 | -3.97658 | -43.10908 | 2026-09-01 03:53:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15ca61b3-5b8c-3cc7-a5fe-39161d90918a | -3.85638 | -44.06452 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3aa4edef-0f4e-3c25-88fa-de75392997f2 | -1.03491 | -47.55735 | 2026-09-01 03:53:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d1b0c5e-e4dc-3c7c-b26f-0526942961e1 | -3.18246 | -48.02718 | 2026-09-01 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8a0462d4-69fd-3946-b1d7-37fe9115402c | -3.85155 | -44.06369 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d9ce153-f1be-3746-881e-bf94371b309a | -3.86865 | -44.05023 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 031829f2-96bb-3d24-94c9-ebf6f353d5e0 | -3.86468 | -44.04422 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a130e66-e74d-3012-8cc6-c56c111b7215 | -3.85505 | -44.04255 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 897c1e45-7241-32ab-8c9f-69a9894d6024 | -3.87397 | -44.07824 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 972f4456-df2f-38e7-98a8-0a6656f84d2f | -3.86999 | -44.07222 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 24f4869c-6a18-3a24-8245-66eaf95a5729 | -3.87123 | -44.05761 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 803227bd-35c9-3b30-b0a4-0b6f2fd419b0 | -3.85379 | -44.08022 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75529ae9-305d-3804-a0e9-6b88810b340c | -3.96721 | -38.31166 | 2026-09-01 03:53:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65a57356-a4e7-3aaa-abfb-bcf110fd4e40 | -3.86851 | -44.07341 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab2818ce-0c22-36c6-bee8-f9437955c33d | -4.31006 | -38.09549 | 2026-09-01 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 69d30cef-ae7a-3efa-aae4-4664563e2215 | -3.97407 | -41.51625 | 2026-09-01 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0175543-d70a-3a99-9c97-b8eb7dfb9fb7 | -3.85862 | -44.08105 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35dcbd17-9ac2-329b-80c4-8e58f08e71fb | -2.7166 | -48.80854 | 2026-09-01 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 769b1431-7422-3782-92ad-50e0d742fe6d | -3.8498 | -44.0743 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84d842b0-77c5-3d98-8a39-428e15a8aaad | -3.04727 | -39.92909 | 2026-09-01 03:53:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 38c6d112-74a1-365f-9f17-333883cdb25c | -4.46523 | -38.50723 | 2026-09-01 03:53:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f29f993-c5d2-31b8-af49-c854a2663c92 | -3.85987 | -44.04338 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18e1cb61-b29f-3163-8d04-911bed354ae7 | -4.08743 | -38.65714 | 2026-09-01 03:53:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4072caed-ac6d-31fa-838d-bfbc34f3ebfe | -1.03213 | -47.55904 | 2026-09-01 03:53:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e0d7d45-eebb-38f9-9fa7-5326e947ef2d | -3.87742 | -44.05717 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22688fbe-5f6b-344a-8fa7-8a44b2a32aee | -3.87605 | -44.05841 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a90237b5-844c-3cf4-9d8b-217af2cc1f2e | -3.85421 | -44.04766 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee296818-645a-305f-998b-ab80d51bb299 | -3.86732 | -44.05149 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2839770-ed5a-3337-a5b2-7350bca32271 | -3.87244 | -44.07941 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db0a6ad0-78f3-3a2a-978a-cfe25a922777 | -3.86914 | -44.07742 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d434d339-83b3-3d66-8419-6592318cc0d4 | -3.88052 | -44.06854 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00181f96-1e30-3d8f-9650-2886b604cba1 | -2.98542 | -39.97152 | 2026-09-01 03:53:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7fa26875-2d1a-331a-8201-f484289439d0 | -3.86382 | -44.04943 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29999f6e-a46f-3e17-8ca2-6d2840114873 | -1.80167 | -47.71273 | 2026-09-01 03:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5594ac3-3657-3504-bda4-19345f1df54a | -3.02206 | -39.98202 | 2026-09-01 03:53:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6c6f1dae-f824-3a8f-b636-494195b82e8a | -3.05099 | -39.92968 | 2026-09-01 03:53:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 69371e0a-0213-303e-9559-8fb7bd469745 | -3.86344 | -44.08191 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c38ad08a-8e62-3428-85d1-cc24eabd4644 | -3.85902 | -44.04853 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30ca54e9-c784-36f2-80db-e42829de5c6c | -1.03294 | -47.55397 | 2026-09-01 03:53:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5989f81b-a59b-351c-bca0-7737890277b1 | -3.85464 | -44.07503 | 2026-09-01 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c0b95a0-842c-3fab-a0b9-2b01601ee929 | -5.05084 | -39.17953 | 2026-09-01 03:53:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d13be83-ee29-3bcd-b52c-acd45e408d2c | -4.85754 | -42.96659 | 2026-09-01 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e93817a4-2993-3f56-abb6-06eb841d1821 | -6.4022 | -45.42368 | 2026-09-01 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8352d87-dfb4-39a8-b73f-cf0ba76f28ff | -6.6507 | -39.11533 | 2026-09-01 03:53:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d8597a29-4a97-3977-8f6a-f1913e70e8e0 | -5.59537 | -42.32182 | 2026-09-01 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 302d344a-4694-3d47-adce-08a23beabe52 | -5.87844 | -45.57561 | 2026-09-01 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06afbe38-d1ed-3ce2-b039-6efea8f71e6a | -7.76976 | -44.05478 | 2026-09-01 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40556623-333f-3b8e-85a1-240cfeaadc45 | -5.34616 | -45.16695 | 2026-09-01 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf70ac2e-0da2-3d35-b54b-8d9cbf903d9a | -5.34667 | -45.16403 | 2026-09-01 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 32af7cc0-d394-3948-99c6-6499d9a91d36 | -7.21518 | -42.74565 | 2026-09-01 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a10de1b5-7981-3cad-bc3c-fcb50adff736 | -7.04396 | -45.4018 | 2026-09-01 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 532b377a-2296-381f-90e0-72d3c06ec8bc | -7.11843 | -42.75334 | 2026-09-01 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 10c12471-5d9b-3321-ae8c-a0ecb459c6c5 | -6.59739 | -38.29453 | 2026-09-01 03:53:00 | NOAA-20 | VIEIRÓPOLIS | PARAÍBA | Brasil | 2517209 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 12b0b816-1fc5-339e-9abc-d5b069ca3df6 | -8.8474 | -36.53075 | 2026-09-01 03:53:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bafc3542-e21c-3c92-a5b8-91fc8fc74f76 | -5.84055 | -44.89688 | 2026-09-01 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cce000c1-dd41-32af-91c0-58c651074c57 | -9.02945 | -36.93092 | 2026-09-01 03:53:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c48afec4-77ae-3d2b-b0bf-7c691d665a10 | -7.42537 | -45.28046 | 2026-09-01 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91cf9694-5483-3a8f-8d9a-6c402085b705 | -4.85386 | -42.96162 | 2026-09-01 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6c514af-9154-3c7b-870f-0051dcef55ea | -5.02337 | -43.60026 | 2026-09-01 03:53:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b199eec-8b90-34a6-b47f-fcbc80a5b92f | -7.11938 | -45.79404 | 2026-09-01 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d245b2b-66cd-3343-804c-c89b1fad2674 | -4.9463 | -47.65429 | 2026-09-01 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49ebca5e-0599-314f-84a8-27372ae4b00a | -4.76911 | -41.80364 | 2026-09-01 03:53:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| f4ffaa3f-7fe9-32da-aa0b-f045017c3094 | -5.34718 | -45.16109 | 2026-09-01 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cbe97c4b-8887-3ba7-8199-2f9b4caad11e | -4.15799 | -47.83742 | 2026-09-01 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README22.md)
