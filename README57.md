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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e029f43-c8ba-3430-921d-092c1d9a0d11 | -6.07155 | -44.70431 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed2caca3-2ba3-3cec-9069-53dd66b44420 | -6.06931 | -44.69637 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 542af267-c9e0-3819-8960-37f2278d1113 | -6.06872 | -44.70007 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 923813ce-c9e5-308d-99d9-792368063488 | -6.06813 | -44.70378 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cdc59ab-ee51-31a7-a137-e3ffed9c4c4b | -6.06754 | -44.70749 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af8fa173-17c6-31bb-bf4d-4f6cea5ecec4 | -6.06504 | -44.63517 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ae44400-d260-34c6-88f2-6be2e1ae920d | -6.06402 | -44.8783 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34e95e89-4a49-3850-852b-2bec0c9a7fd9 | -6.06057 | -44.87775 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb92fdc1-e2b6-38b1-88a5-52f4f8bb8f62 | -6.01083 | -44.55882 | 2024-10-05 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2fd5bbd-0e26-37f3-8cfa-9b8dc5934500 | -5.99812 | -47.45587 | 2024-10-05 04:12:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd9e5036-8e3f-39d1-a946-6886a850cf93 | -5.9942 | -47.45524 | 2024-10-05 04:12:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5426ad3-2ad7-3218-af2f-2585f9f1d845 | -5.99335 | -46.01454 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f562ba6f-0aa9-32d2-8168-b8047c3adc3b | -5.98465 | -46.65268 | 2024-10-05 04:12:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c6ec1cd-7406-328f-b0fb-efd559835771 | -5.9839 | -46.65717 | 2024-10-05 04:12:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb3e6d8c-4b9d-34c6-8588-c65d4d9c2753 | -5.98355 | -46.65442 | 2024-10-05 04:12:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 179d5835-161e-3497-94e7-d7271d38f5c2 | -5.98017 | -46.65653 | 2024-10-05 04:12:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0246d04-706d-31a0-8400-6d3e4ec7fdc2 | -5.97981 | -46.65377 | 2024-10-05 04:12:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 290d260d-39cc-3f8d-a3ba-fe814492aba5 | -5.9768 | -45.36916 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0173b4c6-b082-3178-b6b9-83fb2ff09028 | -5.97616 | -45.37305 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 677c408c-7316-3798-86c7-7e409f731d73 | -5.97329 | -45.36862 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97abfd2e-b8ae-3e8a-92e7-fc8784b0b406 | -5.97265 | -45.37252 | 2024-10-05 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbdd548c-ed56-3cc9-ac50-a5739cc07523 | -5.95887 | -44.64522 | 2024-10-05 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f828a74-aa77-3b8c-926b-3e006377caf2 | -5.91515 | -44.12929 | 2024-10-05 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 857d0951-92e3-3221-a3c2-3cfd30fb4de4 | -5.89702 | -46.28659 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a47651d-6f4d-3176-83b0-fd01f4626903 | -5.89632 | -46.29091 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1eee9e2c-aea6-3417-84e7-3f08e6c8ee9f | -5.89404 | -46.2817 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d1599df-1e9d-3d26-ab5c-4250d7447199 | -5.89334 | -46.28602 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 417b8f59-3d31-3cca-a465-ac0c6505d9a3 | -5.89037 | -46.28114 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa011a65-2f61-3852-8164-8fa192f22a45 | -5.82481 | -44.1263 | 2024-10-05 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| d5cd4a35-94ae-3f3f-8040-263d58159de6 | -5.82424 | -44.12988 | 2024-10-05 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 8fc0af41-1edb-37fd-b4cb-4388a419571d | -5.82367 | -44.13345 | 2024-10-05 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d633625d-03df-35e9-8a44-a599907497c6 | -5.82143 | -44.12577 | 2024-10-05 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 54154f55-219c-3293-bd95-fcef94f352d2 | -5.82087 | -44.12934 | 2024-10-05 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 095a2dda-ce3d-37ed-8ad3-f00decc49641 | -5.8203 | -44.13292 | 2024-10-05 04:12:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| ebe4bec5-5ad0-3331-8e73-ded5370e73ae | -5.81806 | -44.12524 | 2024-10-05 04:12:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 90067731-cfb8-30c0-a9a0-09e1799373cf | -5.81749 | -44.1288 | 2024-10-05 04:12:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b722b525-4668-3652-971b-182eb495db23 | -5.81693 | -44.13238 | 2024-10-05 04:12:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0689c8d0-1ec0-3962-b31d-572024dae761 | -5.80517 | -47.007 | 2024-10-05 04:12:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70b77c34-2c41-3b02-85e2-e72712a7c578 | -5.79807 | -44.01231 | 2024-10-05 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e69716c1-6723-32ec-8a4f-3684a161b433 | -5.7831 | -46.43856 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e311a684-07e2-3ccd-bcff-2eb45d05bdd0 | -5.76569 | -45.06436 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00177816-d6db-3115-8063-e5ab584c242a | -5.76507 | -45.06819 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96355603-9dae-3c51-8df7-d881462e6d86 | -5.71553 | -44.8131 | 2024-10-05 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18d9573f-d910-369f-bcb0-06250f4b3846 | -5.71209 | -44.81254 | 2024-10-05 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afd3537b-d11b-38a6-86bc-45a820774f7b | -5.71149 | -44.81629 | 2024-10-05 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66f3b2b9-83a6-3829-bd85-3408315e8843 | -5.68692 | -44.37735 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfb8e4db-ad7e-3f21-b749-74b7ba30a386 | -5.65545 | -49.71823 | 2024-10-05 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fe09ca7-3c4d-3b0b-9fe2-8b6dd584b879 | -5.65087 | -49.71741 | 2024-10-05 04:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b176626-cbf1-3090-9326-f0ff66697ec2 | -5.64714 | -45.8236 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7cc2459-adb8-374c-8bc8-6bfcf3c4ba91 | -5.58999 | -46.37764 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9216b66e-f79c-371b-a6ec-365f1f0fd74e | -5.55603 | -46.20106 | 2024-10-05 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 014a2c94-3d6f-3a1d-960e-89ac2eb1376f | -5.53632 | -44.3167 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5785d6ff-c151-34df-95f2-1dbadbafa204 | -5.53409 | -44.30891 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e8b29fb-f916-3059-9413-979c64dbe66e | -5.53351 | -44.31253 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71e7197f-52e8-391b-8ba5-56ee674ee547 | -5.53293 | -44.31617 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8643206-d179-371e-ae0b-b9f794677851 | -5.53069 | -44.30838 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dc795d9-8ab8-34c2-b940-2eac13bdeb74 | -5.53011 | -44.312 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40aef174-ad01-3e0b-92e0-ba41b0009725 | -5.52975 | -44.1197 | 2024-10-05 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93f2f2c0-3444-3819-b910-5064e8737d5e | -5.52953 | -44.31563 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7eba2578-6c01-326f-b1e9-5ed035fa6546 | -5.51983 | -44.20292 | 2024-10-05 04:12:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d0aa6f0-66da-3bec-8d5e-9b0834bd2401 | -5.50279 | -44.97632 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 763459c0-5ec9-3ef3-ac0a-dcc1a3d4167f | -5.49196 | -45.3755 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bdd9451-62e0-3133-bb8e-3ad7489acaf7 | -5.47923 | -45.00458 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 627f07b2-f00e-3365-b8a4-18666393bc4d | -5.44718 | -44.04441 | 2024-10-05 04:12:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10fe4339-0241-3830-9534-2a5adce5ddfd | -5.44008 | -47.61342 | 2024-10-05 04:12:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 203e6fe5-5de6-3768-95a0-07a9aaf804f5 | -5.43694 | -47.60759 | 2024-10-05 04:12:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71a7d2f2-20c0-39d6-a499-aa34bdf8a4e5 | -5.43609 | -47.61275 | 2024-10-05 04:12:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9da98f70-7383-3ac1-b422-7f42251690c2 | -5.39782 | -46.57806 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10de6e7e-d0d3-35ca-a434-28a0d7cd4769 | -5.39658 | -45.03057 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 067fe639-2d50-3456-bc88-a738266ddb3f | -5.38764 | -46.42977 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fdd522fe-a7fd-3fe6-8c90-a529e459fe4c | -4.87237 | -47.60209 | 2024-10-05 04:12:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0feb0b8e-9f15-3af8-b966-625312b31313 | -5.38467 | -46.42461 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0bcdbc23-a768-34e6-93f4-f697d1d053f6 | -5.38393 | -46.42909 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ad9c17a-376b-3317-aa2b-215d55575cde | -5.38169 | -45.69432 | 2024-10-05 04:12:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfb9b841-92fc-3674-aa6a-fc2b2c3cc845 | -5.38022 | -46.42842 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| db3f8095-ee96-31ef-810b-fc3e8d854176 | -5.36357 | -45.89446 | 2024-10-05 04:12:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6ae1283-8222-36e8-932a-0f54de006fd7 | -5.31838 | -46.56621 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89f6606f-8b11-35d2-b95b-f790d0c6fe26 | -5.2879 | -47.32281 | 2024-10-05 04:12:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9270976e-3f15-30d5-8c23-aaaf458b8e2e | -5.28709 | -47.32775 | 2024-10-05 04:12:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfaecdc1-a72b-394b-ac38-132f3f4e28a6 | -5.20598 | -45.48993 | 2024-10-05 04:12:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0d8d944-80c2-367e-8598-eb65251cd1a7 | -5.1569 | -45.23952 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a4c6448-0e16-371d-86fc-8ac08a1f260e | -5.15626 | -45.24346 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b791175-7cd2-36c1-897f-42f125dce88c | -5.15338 | -45.23898 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30a50c9f-739a-306d-9759-b2676ec4aee5 | -5.15273 | -45.24294 | 2024-10-05 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 915a77d0-3d7a-3935-84ef-240f8eed0a83 | -5.141 | -45.76932 | 2024-10-05 04:12:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93df56d2-cdd9-3f0f-a0e5-0dff4739da3a | -5.13188 | -46.12442 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09a4d191-029e-3e67-b6ea-da6b81c72d3e | -5.12822 | -46.1238 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 651f4706-7a3a-3f55-986e-583e6b04325b | -5.09253 | -46.11997 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96b62804-5bb5-32bd-9915-db9213a3907c | -5.09148 | -46.11792 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd7ad6d5-2bc8-3ec7-8be1-4d2d9425251d | -5.09075 | -46.1223 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc121329-5c00-3738-b977-024b462f79d9 | -5.08954 | -46.11511 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56507f34-5278-3f5d-85fc-a14d7d996424 | -5.08885 | -46.11946 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b556fdf5-8c05-3b21-9d9c-31b6a35d024f | -5.08779 | -46.1174 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cc9f930-2ed2-3f29-819b-d7c867c1bafa | -5.0393 | -46.57196 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f95d9766-0179-369c-8fc0-a1f94ff72d4b | -5.03553 | -46.57131 | 2024-10-05 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4dd2553-55bb-3bb2-8fe5-d306ebac16a8 | -5.02439 | -47.71389 | 2024-10-05 04:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c12468bc-9cc7-3dcb-a64d-636beea0d6e7 | -4.93852 | -47.1319 | 2024-10-05 04:12:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a974968-b76b-3fa9-b730-58444644cec2 | -4.92477 | -45.67716 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f8ff142-b745-32e6-b39a-3df27342752a | -4.92413 | -45.6812 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60a943e9-40a2-3416-9eae-7a1e7fbd7856 | -4.86354 | -45.85004 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README58.md)
