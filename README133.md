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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bdfcd38-cd51-3167-a0bc-147375fd09db | -9.831 | -48.4292 | 2026-09-21 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 1338d023-22a5-39dc-8c24-098cda866f87 | -2.9525 | -57.72 | 2026-09-21 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1e22ef2e-653f-34db-b5c3-0c8a4f5a175e | -8.3167 | -45.9934 | 2026-09-21 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 63ccc584-8363-3bb5-ab0a-9ba44c1285e5 | -2.4636 | -49.2301 | 2026-09-21 14:50:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5550c8d8-9289-3b5f-9be3-0c37388f5a5f | -3.2817 | -57.8685 | 2026-09-21 14:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e6740bb5-9c00-3606-be03-4b4deb4c682d | -6.9849 | -59.663 | 2026-09-21 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 6ac4eeaa-040d-3f22-8fe4-26b802d6a71b | -9.6665 | -54.3332 | 2026-09-21 14:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 05780dae-d338-3e4a-b78e-996288f49ce9 | -11.8715 | -48.9792 | 2026-09-21 14:50:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 37d2071b-7b5b-3f95-b1bc-6db03f04d422 | -3.3453 | -42.7832 | 2026-09-21 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| bc3f1e85-dd94-357d-9377-9694351d3727 | -3.6631 | -58.8835 | 2026-09-21 14:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1c0fde7c-68a2-3b9a-b3e0-9fc9043ce7c9 | -3.6449 | -58.8647 | 2026-09-21 14:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 920686f1-fb32-349a-b40f-a10740f23dad | -10.3914 | -48.9133 | 2026-09-21 14:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 25bbe0e9-a5bb-37db-af21-eb85e1924870 | -8.7267 | -44.8836 | 2026-09-21 14:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| cd06a1e9-60ae-3ee0-88d2-6dc450c2566e | -16.9964 | -56.4525 | 2026-09-21 14:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 2584a39d-cff3-371a-a6b3-bfa6d86022f5 | -12.026 | -50.0663 | 2026-09-21 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 9a7ad2d9-af19-3947-98ad-4b6ca4953c29 | -11.8362 | -50.0244 | 2026-09-21 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| ebb68a86-e47e-3866-9fa5-d7e23b1c0c1d | -8.0466 | -61.3237 | 2026-09-21 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 91393e66-e50a-3a94-8158-74111f276501 | -11.8495 | -46.833 | 2026-09-21 14:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 0fa0b5e5-d2ac-396f-8138-1aaf6580d189 | -10.7463 | -50.6172 | 2026-09-21 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| f519049e-3814-3dd4-b269-be2dc2101ca5 | -10.9358 | -50.5972 | 2026-09-21 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 6cb7be6e-19c5-3a06-840e-2823dc04bfc2 | -6.8448 | -55.5411 | 2026-09-21 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| e50d4ff5-32e3-3a05-a4b7-5454ca9b8b04 | -6.4107 | -45.1934 | 2026-09-21 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f409df81-eae4-32b1-864d-1d18f8a69d39 | -3.4975 | -59.1752 | 2026-09-21 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ea4f2650-7e88-3d26-a528-70d3affd7fb1 | -10.5108 | -51.2771 | 2026-09-21 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 0e85e30e-a251-3ea3-8536-abb3a79ddf63 | -10.8924 | -53.9652 | 2026-09-21 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| ba5ee12e-3dc8-3000-9a69-845f22594bd1 | -10.4108 | -50.2683 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2fca6726-2679-32c6-8aaf-872e8c0c4431 | -6.5571 | -45.5434 | 2026-09-21 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 56d417f2-6f71-3c14-ae35-83c9c1b834a1 | -8.3764 | -47.2802 | 2026-09-21 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 6b92dc05-0006-3bab-b267-763d3fb4dceb | -10.0898 | -50.2795 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e0b2960c-874e-3f15-a97e-0b881a442c96 | -12.8708 | -50.9719 | 2026-09-21 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 69fa8707-b8a2-3879-864a-9dd98a1e3c92 | -10.7115 | -60.7312 | 2026-09-21 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 0675e3a0-04ee-38ca-b91d-2b122976b221 | -9.8325 | -48.3198 | 2026-09-21 14:50:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 2d599480-b40b-3615-8e02-bad3bdca004d | -11.7823 | -49.8152 | 2026-09-21 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c01e71a7-56f9-3b03-9ffc-7dcf2ce0b95c | -12.3025 | -50.6774 | 2026-09-21 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 7c08e03d-54c6-3ef8-a6b0-b6f7bbd63890 | -10.8276 | -50.203 | 2026-09-21 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 5162b06a-2fe3-3f6b-9764-eb65d22b106a | -9.1711 | -49.9835 | 2026-09-21 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 35b13337-8f25-369f-90e6-d557142cd93b | -3.3824 | -50.4276 | 2026-09-21 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f3bc558a-e25d-3fb9-a5d5-bc62bbaed152 | -4.4112 | -55.2466 | 2026-09-21 14:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 675fb9a0-b7e6-3d79-ae53-acd6c697e4db | -8.7706 | -45.8567 | 2026-09-21 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 3c292a97-5b10-3c59-b6a8-468bab2b3533 | -4.0943 | -52.1458 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cb431d51-759d-376c-9ba3-3f37951b4a73 | -3.3823 | -50.4486 | 2026-09-21 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ae35ed8c-fc09-364b-aa9e-250ecb3f5e59 | -4.8683 | -55.8457 | 2026-09-21 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 82f5f50d-ed5e-38c2-b1b7-d8e966046ee3 | -3.2086 | -57.8119 | 2026-09-21 14:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 54ac88dd-9263-3916-9d79-e889b3616864 | -4.0944 | -52.1252 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 45f0d8ce-978f-3d55-9388-e00473b84455 | -10.9547 | -50.5952 | 2026-09-21 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 80187d3a-9db7-3e39-9c54-851df35e756f | -4.2239 | -48.6127 | 2026-09-21 14:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 6d02482d-3502-3ac8-b0d7-9cded04ade36 | -5.7506 | -43.6859 | 2026-09-21 14:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| f370ef59-f862-3178-a401-5dd09adae626 | -4.9535 | -45.1374 | 2026-09-21 14:50:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 05cd3adf-3f62-3c7f-8a58-8db176e2e0c4 | -2.9157 | -57.8177 | 2026-09-21 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 2b96c57e-9eb8-3fbc-8208-bfb835cee016 | -5.6411 | -43.3687 | 2026-09-21 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 8e13bc78-55ca-3710-8550-68a84679e569 | -8.1872 | -54.7622 | 2026-09-21 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 4efb23a5-6e16-3f56-aa87-80e489f5082d | -10.43 | -50.2449 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| a2c61375-82e0-38c7-9408-8e2da73557d4 | -7.3289 | -55.2155 | 2026-09-21 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e7ed07ab-3d2c-3507-a797-37403585bfe1 | -10.7437 | -50.8089 | 2026-09-21 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 14fa2fc4-9643-3088-a4dc-434e25656dba | -7.4126 | -49.8317 | 2026-09-21 14:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 1cba8bf3-6723-3948-a6ac-9cdfa8e1320d | -10.473 | -51.2808 | 2026-09-21 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 628e8da9-efbb-3735-a646-f11251aa3060 | -10.5906 | -53.9918 | 2026-09-21 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f2b101a1-8a9f-3a0b-a51f-3107938a71aa | -13.241 | -51.7571 | 2026-09-21 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 748d1eee-a33f-386c-a712-1fee18e3b287 | -10.9098 | -54.0866 | 2026-09-21 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5163de03-0bff-343e-afaa-e7c9799ed525 | -6.4554 | -48.4423 | 2026-09-21 14:50:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1fe3eb7d-62f2-3203-8261-1c2656a5e8de | -10.8002 | -50.8243 | 2026-09-21 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 7acdb146-8df3-359d-8f06-dac9ec86dd8b | -10.3919 | -50.2702 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 9949fdac-482b-3553-aa12-d7c79855d006 | -11.0804 | -49.7456 | 2026-09-21 14:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| f018f549-e250-3679-8f58-2e754e86678c | -7.5661 | -61.3239 | 2026-09-21 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9250d2df-cfe7-3354-9343-32645dd2d09a | -11.4353 | -45.3459 | 2026-09-21 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| d24b9c5c-2fef-373f-a81a-88ada3fb23d5 | -13.0678 | -50.6256 | 2026-09-21 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 387489c8-bdee-3664-81bd-124bd999d329 | -10.4919 | -51.279 | 2026-09-21 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 139.7 |
| e647e63c-aefd-3c0e-a458-1b0687f8c97d | -2.9997 | -60.8047 | 2026-09-21 14:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d94bb78a-0a41-3b80-9269-d08d1e57d587 | -3.6947 | -60.5645 | 2026-09-21 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 54391d44-a34b-37c4-b96b-ecd195bf1d52 | -3.4599 | -59.54 | 2026-09-21 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| af49b318-c2dd-3e29-8881-e135bce7110a | -6.392 | -45.1948 | 2026-09-21 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 9327fdc6-f51a-38c3-a106-086939665c99 | -6.5759 | -45.5419 | 2026-09-21 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 250262ee-f9b8-36d5-83d9-739db4ca5b1a | -11.4545 | -45.3432 | 2026-09-21 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 1d5843e6-1e7c-3c3c-9ca7-d396797b15ed | -3.2189 | -60.8011 | 2026-09-21 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e8582bb2-fda2-36b2-b880-a238e4372ea6 | -6.5444 | -44.9327 | 2026-09-21 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 251.4 |
| 7b0140fc-c644-3eba-b131-f9648292d70d | -13.2596 | -51.7973 | 2026-09-21 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 6fcf9ee8-9d36-34b3-8369-cc63d76b8309 | -6.9223 | -42.9323 | 2026-09-21 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 5a91f1a4-7b12-3b61-bcb4-574ff586ab24 | -9.5595 | -66.0172 | 2026-09-21 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| f83185a1-091e-341a-a194-8afcb35968fd | -10.7999 | -50.8455 | 2026-09-21 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.8 |
| a07fc674-4134-3beb-869c-41eeae38b4dc | -10.7466 | -50.5959 | 2026-09-21 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d922c8d4-fcda-3e24-856c-e91aba4dfe43 | -9.247 | -57.1488 | 2026-09-21 14:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0125bff6-51ff-35d9-9056-2f626a656ad3 | -3.2162 | -42.4833 | 2026-09-21 14:50:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| f78edcc8-d244-3b69-a27e-718d39bb5c4f | -10.3917 | -48.8915 | 2026-09-21 14:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 30cb660d-ef57-3b87-b92e-55ccf5eef589 | -3.5356 | -58.6939 | 2026-09-21 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 12f2b425-1542-3ab1-b532-fd2301f5213f | -3.4963 | -59.5775 | 2026-09-21 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2ecc4860-67e3-3a25-9047-bcc3f111beb8 | -7.3376 | -44.4744 | 2026-09-21 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 20cba7c5-5b42-3103-995a-32c4419360e0 | -5.6406 | -43.4153 | 2026-09-21 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a96e6ce1-7689-3e5b-b241-d045f679dbf9 | -9.3986 | -48.3213 | 2026-09-21 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 580d5b20-37de-38e2-a8cb-4f98a11d8a84 | -11.3232 | -51.3414 | 2026-09-21 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| c826f70f-3e0b-3037-933f-647e17612de4 | -9.0239 | -48.1622 | 2026-09-21 14:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 5f8164b8-ac33-364d-8196-2fa1933e39df | -7.5713 | -45.4106 | 2026-09-21 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 42bdae57-6793-34da-afba-e1d6171b98f4 | -3.0507 | -50.2702 | 2026-09-21 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 31a47659-cfd9-3a01-a660-965964fa0dad | -12.0451 | -50.064 | 2026-09-21 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 60174356-1fad-357a-bb65-6a8cc70bb9f4 | -12.9091 | -50.9672 | 2026-09-21 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| cb00b820-10d0-347d-b52d-2904dc263b03 | -2.4451 | -49.2306 | 2026-09-21 14:50:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| b50e7f6b-691f-37a0-b6e4-c60be60c3f22 | -7.252 | -55.5794 | 2026-09-21 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7bd0c1fc-ccb6-37c5-b0fd-10d185265037 | -6.0197 | -51.7686 | 2026-09-21 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e8ce0a08-e3f6-3835-be1c-00735be648bb | -6.1832 | -47.5915 | 2026-09-21 14:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| fb9b9a59-47f0-3809-a5cd-b6cf4d4b07e3 | -10.2982 | -50.2158 | 2026-09-21 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e8d62da9-b0fe-3516-b40b-f596afe7a995 | -7.5477 | -61.3247 | 2026-09-21 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |


[Clique aqui para ver as próximas entradas](README134.md)
