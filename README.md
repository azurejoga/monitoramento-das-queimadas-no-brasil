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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ead147c-e226-3273-aac5-a32ffa208de2 | -3.9671 | -48.1283 | 2026-07-31 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 3ba2dbef-fe59-3308-8bc4-7fb6103a311b | -3.9672 | -48.1067 | 2026-07-31 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9a9c0b3e-fbf2-35db-93f6-1797d4bda5cd | -18.0419 | -51.3097 | 2026-07-31 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 6175b099-4d0b-3878-af9f-c2ce5ffd2f63 | -22.1578 | -56.0217 | 2026-07-31 00:00:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e03d9c7e-8400-3ee3-b71a-771394c8fe08 | -3.9671 | -48.1283 | 2026-07-31 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 166.2 |
| f2bc5553-8626-3455-a81b-88405a12740e | -4.1675 | -48.7655 | 2026-07-31 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5d884267-ffc4-3559-8755-65287d5fe82f | -3.9672 | -48.1067 | 2026-07-31 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ff5a9d1e-b6aa-3eb1-930b-c3fe7a9ee95d | -11.3178 | -50.3847 | 2026-07-31 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| bf132593-cb99-3c9c-89a9-628986261ed8 | -11.2988 | -50.3868 | 2026-07-31 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d9d39a1a-0006-3bd4-9b0c-e4b4f0e66311 | -18.0419 | -51.3097 | 2026-07-31 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 49ed0907-b744-333d-bff1-721eb44933fa | -4.1674 | -48.7869 | 2026-07-31 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b3d725b5-6109-3ee5-b364-ee40e912b27c | -4.1675 | -48.7655 | 2026-07-31 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 88eb64b6-5913-34a7-b132-9fd20420f41d | -3.9671 | -48.1283 | 2026-07-31 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 1e31deef-506c-3ee0-aadd-cb1d88927653 | -22.1578 | -56.0217 | 2026-07-31 00:20:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 058926ea-ee43-3175-8491-61e6bf895896 | -3.9671 | -48.1283 | 2026-07-31 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 99d6d792-cac9-3a4d-b254-522331f2fa77 | -18.0419 | -51.3097 | 2026-07-31 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 1174b648-b877-3c2d-bc58-6288fe24e41f | -11.2988 | -50.3868 | 2026-07-31 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| fee0af1c-eea9-3cd6-9d84-9e2e94c11daf | -11.9104 | -43.4319 | 2026-07-31 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0642519a-e63f-3b54-ae5e-13ce96ab5f5a | -11.3178 | -50.3847 | 2026-07-31 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 67ed5556-48ea-38a7-8974-5bbc7af6486f | -3.9486 | -48.1291 | 2026-07-31 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| bdb08c68-ac29-3795-bfd1-dc31486ec5dd | -18.0419 | -51.3097 | 2026-07-31 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 18139d45-aecb-352d-8381-9b725d8420df | -11.3178 | -50.3847 | 2026-07-31 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8a596749-1367-39e8-8b6e-4d3e809663d0 | -3.9671 | -48.1283 | 2026-07-31 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 168.2 |
| c6fcd2ba-e734-3310-bf60-6dac932bc5da | -12.8543 | -44.386 | 2026-07-31 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7dea1fbd-0ede-3264-a8db-f0e475a7e90f | -12.8543 | -44.386 | 2026-07-31 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 25a33884-9cdd-3810-b724-5fd7fd2137cc | -3.7113 | -51.1885 | 2026-07-31 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| c134c9d7-d7b7-31a6-b024-6ce24ed48631 | -3.9671 | -48.1283 | 2026-07-31 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 1a1359fb-8173-3d4e-aeb4-f5c89f8f2b87 | -18.0419 | -51.3097 | 2026-07-31 00:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| d784792c-2e2b-3f4d-9a2c-fc3a03416f67 | -11.3178 | -50.3847 | 2026-07-31 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 27f6f744-a3a5-3087-9d55-93f92dcfead3 | -22.1616 | -56.02639 | 2026-07-31 00:50:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 0b3758d8-c749-3417-a498-afec591c81ca | -22.15997 | -56.01572 | 2026-07-31 00:50:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 56.7 |
| e60020b8-3502-3642-ade2-150af05148d7 | -11.8456 | -50.160099 | 2026-07-31 00:51:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fed9a43-1994-3bb1-b80c-eb8a24667a21 | -17.6015 | -46.6371 | 2026-07-31 00:51:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0e5d1021-1d5c-3c64-a50c-eaa68d038aa1 | -6.1801 | -55.512501 | 2026-07-31 00:51:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a306c8bc-6e39-3212-9bd5-a5be03f65dc4 | -22.1563 | -56.020199 | 2026-07-31 00:51:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4a8381a7-075d-387e-8ccb-928406ddbfaa | -3.9633 | -48.1292 | 2026-07-31 00:51:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e78868fa-1bac-368e-b92a-3625723b9ccd | -9.2797 | -60.634201 | 2026-07-31 00:51:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36d23dea-7ec1-3e1a-a8dc-2ed70dd2a854 | -3.9548 | -48.0951 | 2026-07-31 00:51:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b112ef5e-dd3f-37fa-9c1c-48b5d8cb792c | -11.8553 | -50.157501 | 2026-07-31 00:51:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed17c284-5f49-376d-b043-5f08af309cbd | -22.153099 | -56.005402 | 2026-07-31 00:51:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 00865322-393e-3f47-8deb-f07693013191 | -22.164499 | -56.010399 | 2026-07-31 00:51:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f4c8c0fb-ff0c-3b78-bb68-c550183660e9 | -18.0394 | -51.305698 | 2026-07-31 00:51:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae675c8a-3289-3e2e-8644-f0f531ea4fef | -9.9446 | -63.033798 | 2026-07-31 00:51:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a58fa817-3daa-3c80-8788-c7310e1710da | -19.0294 | -57.492901 | 2026-07-31 00:51:00 | METOP-B | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 05301b90-7b1d-3bf5-bc03-736b5ab341f0 | -14.373 | -48.0369 | 2026-07-31 00:51:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a9a81fc3-24fb-34af-8ad3-1e4d11bfbc10 | -19.031 | -57.500198 | 2026-07-31 00:51:00 | METOP-B | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7ad230e0-37e4-35fe-a173-54b12c634e42 | 1.1084 | -60.507301 | 2026-07-31 00:51:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac0e136-c223-366b-b18a-8f959b6259af | -18.033199 | -51.281101 | 2026-07-31 00:51:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f786c92-d193-3542-b6bb-8826d1fdb388 | -11.3041 | -50.3815 | 2026-07-31 00:51:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97022aba-ef48-38d2-b05c-806a848d251b | -18.046 | -51.290699 | 2026-07-31 00:51:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 930467d8-1557-38bc-96bb-0e23bfbf3c85 | 1.097 | -60.5121 | 2026-07-31 00:51:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb8b46b-766a-35a4-875d-c6c096e27eb7 | -22.154699 | -56.012798 | 2026-07-31 00:51:00 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 190e72b2-ff5a-3420-a618-aa6eba94f666 | -6.5573 | -55.145699 | 2026-07-31 00:51:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be40dfce-7619-3aac-8553-a47148cd5ada | -3.9452 | -48.097401 | 2026-07-31 00:51:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccd2e61a-0d29-388e-910d-2447fc269794 | -3.9537 | -48.1315 | 2026-07-31 00:51:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e18b455b-cfd9-39a7-9b4f-738307222c43 | -9.2813 | -60.6413 | 2026-07-31 00:51:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c64bea00-92b5-3c50-97e3-2a10747813f4 | -6.5597 | -55.155998 | 2026-07-31 00:51:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 225887e9-586a-35e0-8a5f-710786de43bb | 1.1018 | -60.491001 | 2026-07-31 00:51:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ffbdef30-06f3-3e17-afd4-4cb7faf6dd1c | -19.0179 | -56.411301 | 2026-07-31 00:51:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 141884cf-4997-3c12-9a49-3c36ddc293f0 | -3.7082 | -51.175701 | 2026-07-31 00:51:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edab1ad4-49e6-3b32-9c40-f6f6e3415e04 | -11.3138 | -50.378899 | 2026-07-31 00:51:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5b9b327-e365-3dfa-9bbb-aa8abebae4fe | -18.036301 | -51.2934 | 2026-07-31 00:51:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c6aefdb2-5633-33b5-bb71-5de99e8bd422 | -19.0326 | -57.507401 | 2026-07-31 00:51:00 | METOP-B | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 25dbbc88-c7d5-3769-ae52-3beb8e80b346 | -11.3185 | -50.3969 | 2026-07-31 00:51:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a64601de-a8d4-33b8-a417-191038907e24 | -20.610399 | -57.290901 | 2026-07-31 00:51:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e8ad4f44-62ce-3beb-8e58-c86252e1ae35 | -21.382601 | -56.817699 | 2026-07-31 00:51:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1072b4e9-d5ca-31bf-b697-14ec17aa1640 | -11.3088 | -50.399502 | 2026-07-31 00:51:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 210b3449-2412-3bd4-8679-621b243341d8 | -11.3092 | -50.360802 | 2026-07-31 00:51:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2843e5e-9a53-305d-b3c1-34bd67b2ee48 | 1.1002 | -60.498001 | 2026-07-31 00:51:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2391f07d-a006-3a69-b9a3-fb9872980180 | 1.0986 | -60.5051 | 2026-07-31 00:51:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 69786c2a-dce7-3a4f-b1f8-0993a62a008c | -6.1824 | -55.5224 | 2026-07-31 00:51:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 127927ec-c3f6-3c9e-8746-5c3f28239d46 | -21.384199 | -56.825001 | 2026-07-31 00:51:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3d41cdf0-8a0f-363d-bd88-da0107ae044b | -9.9465 | -63.042702 | 2026-07-31 00:51:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 26fac543-1a28-3a2f-9f6e-9b167c01555e | -3.7031 | -51.154499 | 2026-07-31 00:51:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d8865a2-f540-3d33-b176-73064037c827 | -18.05015 | -51.30558 | 2026-07-31 00:52:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| e69c4e40-c4bd-34e7-bbfd-2134a9f9682e | -20.61832 | -57.30354 | 2026-07-31 00:52:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 701b4a6e-bfed-33ec-b9f4-1433f58083ea | -18.03622 | -51.30858 | 2026-07-31 00:52:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 96db5c64-1ef7-35a5-b7b6-b4e6d60ed6d5 | -21.37924 | -56.83327 | 2026-07-31 00:52:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 637bb864-880d-3b6e-8a66-b126c5d9e042 | -19.02161 | -56.42762 | 2026-07-31 00:52:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 38e053c2-189a-34a6-84ca-15a734ff5bd7 | -19.01996 | -56.41669 | 2026-07-31 00:52:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 52df6cd6-1bc8-3dcb-83b4-256f1f7a146f | -9.9422 | -63.04575 | 2026-07-31 00:54:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 37b0ba68-568d-32dc-a34d-ba3d94a85216 | -9.27846 | -60.65161 | 2026-07-31 00:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fefc86c1-5b38-3a60-87cb-18c0a8aa8e41 | -6.56082 | -55.16764 | 2026-07-31 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8234ad24-cd8b-3675-9176-dbea91e6a9d9 | -6.18046 | -55.52246 | 2026-07-31 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 09f5877d-68b1-39cf-b223-908de6928e6e | -9.4686 | -63.27945 | 2026-07-31 00:54:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fc13abab-4402-36ae-9703-8253cce3810a | -11.31873 | -50.40325 | 2026-07-31 00:54:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| eb59cde9-6780-3f29-ae6f-6cb6c7784e2f | -9.94351 | -63.05585 | 2026-07-31 00:54:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 54137935-5c1d-3d14-8a06-627c34ba7d18 | -6.18337 | -55.54207 | 2026-07-31 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 16ee5cfb-76da-365d-8ac4-acf10b4d3684 | -9.96281 | -64.96319 | 2026-07-31 00:54:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a9543f55-7410-30cc-b0dd-18758333f11d | -10.07887 | -60.50783 | 2026-07-31 00:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 39863cc3-a5f9-3ddd-8381-f0e10f633b80 | -6.18402 | -55.53537 | 2026-07-31 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 7e0adcab-c4dc-3e76-89b6-76637b95efa7 | -11.32139 | -50.39768 | 2026-07-31 00:54:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 7af3208b-3dee-35ba-88db-64dc8e64eacd | -11.30437 | -50.40087 | 2026-07-31 00:54:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| e2816df1-a233-353c-9669-650946ad421c | -10.07762 | -60.49887 | 2026-07-31 00:54:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e2de3477-7109-35c1-8843-b090ca8825e0 | 1.09467 | -60.49856 | 2026-07-31 00:56:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7fac19b5-c6df-30fd-9076-49a6f0f41dbb | 1.10497 | -60.51692 | 2026-07-31 00:56:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 531d7915-8bd7-315d-a03f-d0d415d08d3c | 1.09672 | -60.50476 | 2026-07-31 00:56:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 340f26b1-7bd2-3c72-b918-7fabbe9a987e | -18.0419 | -51.3097 | 2026-07-31 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| d81ddbed-2499-36bc-a061-8965fe8f9188 | -3.7114 | -51.1677 | 2026-07-31 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| dee9a6de-ac9f-3890-984f-0f3d3fb7314b | -3.7113 | -51.1885 | 2026-07-31 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |


[Clique aqui para ver as próximas entradas](README2.md)
