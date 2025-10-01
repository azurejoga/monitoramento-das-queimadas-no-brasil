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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83e93d55-7086-36f0-8880-37e347e91ac8 | -10.9182 | -44.3092 | 2025-10-01 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 86ef8bd5-01d2-38fa-8f08-011bfb42bbc7 | -8.672 | -47.7144 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8442c412-ba6b-33c7-aa73-aed7c2135b37 | -13.3804 | -48.1131 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 199.9 |
| e8fbb7c0-d04a-369e-9f4d-0bc41ad750c0 | -8.6908 | -47.7126 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 0711ed2f-2a7b-3c96-b131-f27879ec8f4f | -14.3519 | -45.9206 | 2025-10-01 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 163.7 |
| e9645c00-0860-396b-8561-bc3ea04ce566 | -14.8693 | -47.2032 | 2025-10-01 13:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c569a7a4-0b40-3785-9ecd-1addb7ecbe3d | -9.4644 | -47.6124 | 2025-10-01 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| be2f83ea-21de-31f3-a47d-33ad6e66b3e5 | -5.8927 | -42.5273 | 2025-10-01 13:40:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| e0a10800-0cca-384d-b560-b1426fca993f | -5.8929 | -42.5036 | 2025-10-01 13:40:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 8878109e-67b5-3865-bfdc-026961125998 | -14.3714 | -45.9172 | 2025-10-01 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 108.3 |
| a40a3ec8-a661-3826-a5a4-09d9e6d0feed | -7.646 | -45.4489 | 2025-10-01 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 341aa983-3a2e-3b1f-aaf4-77a845f22939 | -14.3514 | -45.9437 | 2025-10-01 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 148.8 |
| dace4ee2-1005-30fd-a664-d51255a066ac | -15.5379 | -45.2375 | 2025-10-01 13:40:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 103.5 |
| d59e206e-d210-3ef2-bb42-d257339a628d | -6.0809 | -42.4881 | 2025-10-01 13:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 2c8e539d-5616-302d-a614-008febb7b779 | -8.5079 | -47.2897 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b3d18ddc-8425-3434-a118-ee3de0cd9b7b | -8.2105 | -47.0084 | 2025-10-01 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0b6a1ec4-d0e8-3fc1-ac3f-6429645f1f4a | -10.0187 | -48.5183 | 2025-10-01 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3ff29172-8fb5-3ce4-8449-44d6012936b3 | -9.9951 | -46.1703 | 2025-10-01 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 5580a391-5e9f-3a8f-85b7-fd730e4f27d9 | -12.8774 | -45.1742 | 2025-10-01 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 35e0bffd-bc25-31f9-883d-9ec4bf1ecec1 | -9.9376 | -43.6953 | 2025-10-01 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 9f1b1a3a-4a1c-36b2-a649-fba79d149fb2 | -9.9383 | -43.6483 | 2025-10-01 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 999cb93c-3ee7-3e42-9ea9-86b26891909e | -5.8064 | -43.728 | 2025-10-01 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 60196d84-7a88-3681-a64d-6332caf17102 | -14.8688 | -47.226 | 2025-10-01 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 2ea6a41d-2ea6-3bd2-87a1-a59d0b31dc5b | -11.825 | -44.9437 | 2025-10-01 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| bf544052-f4f3-33e7-9b74-1f1322e4fa31 | -5.8062 | -43.7512 | 2025-10-01 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 02bb1ed7-de20-30b3-bad7-dad15bec8988 | -8.4833 | -47.7763 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 9646d077-fae1-310e-96f3-c0bc9b694435 | -9.1248 | -47.6256 | 2025-10-01 13:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6ea79874-7655-3746-8281-605a51bffad3 | -14.9733 | -46.8896 | 2025-10-01 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 454ad850-5651-30f3-8645-bcf9a5e14ba5 | -15.2742 | -49.2852 | 2025-10-01 13:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 310.2 |
| be6a0265-04b5-3f02-abb8-c4aa7b309e0a | -6.079 | -42.6773 | 2025-10-01 13:40:00 | GOES-19 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| f21784e3-d5d7-32c6-b9fd-326a4eff6ccf | -12.4434 | -50.2092 | 2025-10-01 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| d77eb96e-c4c1-349f-b0ba-a7ea4e4213ee | -12.877 | -45.1974 | 2025-10-01 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 45fe1969-729d-32fa-a8cb-619d551e3455 | -9.9391 | -43.6012 | 2025-10-01 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 2898fa95-cce3-3d91-bb13-2a6f1e8a0a74 | -8.5587 | -44.7414 | 2025-10-01 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 394ce2c8-d665-3dbe-b5b3-5afdda2dcbb7 | -7.8882 | -47.281 | 2025-10-01 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 157.7 |
| e1f599b0-0b7f-3008-a80d-1acdd8aba889 | -15.5503 | -48.1926 | 2025-10-01 13:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 9915bcc4-fa61-3b88-a89e-b9005553d2f3 | -13.7691 | -47.9435 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 36f25f78-610d-37eb-9319-033ee930e851 | -11.8482 | -48.0595 | 2025-10-01 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| c0bec2b7-4a8c-3e2a-b06f-47059bebde16 | -13.6896 | -48.0671 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 6a174ca1-927a-30e7-b73a-e19efddeec3c | -12.2153 | -47.8112 | 2025-10-01 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| fe2ad9a7-9964-3517-af15-9b63805438ae | -14.8021 | -45.7946 | 2025-10-01 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| dcc2acbe-d4c5-3f2f-82aa-813c17c40872 | -16.0417 | -50.8959 | 2025-10-01 13:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4fc18367-157f-3b18-a2c6-258c00488104 | -14.9079 | -47.2193 | 2025-10-01 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| a9181f2f-7afd-3dfc-8e98-69cd3a6dd0b2 | -5.9368 | -45.8825 | 2025-10-01 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 9e168259-df3d-3d2b-a9a8-90b8c288d5bd | -7.822 | -48.1851 | 2025-10-01 13:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 97cd5c19-65c3-3a4e-a274-fa9edf31f519 | -5.8418 | -43.9566 | 2025-10-01 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1f5007c2-bbcb-3df6-a2e6-dadab85747ab | -7.1812 | -41.7172 | 2025-10-01 13:50:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 6916d0eb-9584-31b9-969e-ff56fbb5a809 | -7.8549 | -45.2702 | 2025-10-01 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 24bcdd9d-6394-3ff4-8112-061cab7bc9dc | -8.8929 | -46.6072 | 2025-10-01 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d427a390-77de-3d4f-ad5c-31aae9e8d27b | -9.1248 | -47.6256 | 2025-10-01 13:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| abff9a0b-ccbf-3939-8859-95abf543a827 | -11.8246 | -44.9669 | 2025-10-01 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 14b8fa9c-d176-3293-bc2b-ae7388c0a4cd | -8.5587 | -44.7414 | 2025-10-01 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 343941f5-56b0-30a1-bc38-348c672f771b | -11.1178 | -49.7845 | 2025-10-01 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 65db6021-68bb-3957-8b1c-803ccb1e0aaa | -14.9738 | -46.8668 | 2025-10-01 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 86282513-6026-35db-9abe-825cac1ba8e9 | -8.9081 | -51.6743 | 2025-10-01 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| bcc034c1-cbc9-3a7f-973b-370b610dcea0 | -7.4412 | -47.0109 | 2025-10-01 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 6980f810-d7b3-3a96-9568-6a79c4c08217 | -12.122 | -43.4215 | 2025-10-01 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| bd775792-024c-3789-a0a7-435e7507ff9e | -9.9394 | -43.5777 | 2025-10-01 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4a234dd0-9679-31e0-9c58-6c1078b1a709 | -14.3462 | -47.1323 | 2025-10-01 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 419cd234-2d23-3534-a527-8e01f4e4fbc8 | -9.0236 | -46.7052 | 2025-10-01 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 8737d6f0-a316-33e2-b841-04bb89828601 | -6.7168 | -44.5758 | 2025-10-01 13:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 9530478b-5eb4-3393-a3c7-34b5936f17e5 | -13.2969 | -50.6821 | 2025-10-01 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 269e364f-5309-3988-a009-0fd0467a3991 | -15.7509 | -43.7239 | 2025-10-01 13:50:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 1d57ed93-24ce-38bc-b2ce-9e7af9a41549 | -8.9115 | -46.6276 | 2025-10-01 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 301.9 |
| 6b3e6b04-6ae6-3907-8520-fd4ba98598fb | -12.2623 | -44.1306 | 2025-10-01 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| a326f73f-cae6-3740-a780-92e51ea1cf05 | -9.6984 | -49.9336 | 2025-10-01 13:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a4447d4f-a4ae-3172-822e-230cf919c55e | -8.5018 | -47.7965 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 248.5 |
| 4802d094-48dd-3fda-9590-e50673fba2d7 | -8.6908 | -47.7126 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 42edff69-f57a-3157-b042-f318469d7edd | -7.7944 | -42.5132 | 2025-10-01 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| ca1601fc-b28a-3015-8651-93c082a13576 | -6.3393 | -44.8354 | 2025-10-01 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 01012e0d-1462-37a0-9832-5d2347c5899b | -8.4833 | -47.7763 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| bd2f9680-6fc0-31bc-bea8-74fde74c3b66 | -13.3607 | -48.1382 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 208.7 |
| e247668e-3b05-304b-b6af-c42c84d354d0 | -12.2627 | -44.107 | 2025-10-01 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 380d607b-8fdd-34ee-bddb-48672829423e | -11.4596 | -45.0433 | 2025-10-01 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 220.0 |
| c1d89fbf-8588-353d-a758-8935420517ac | -14.3519 | -45.9206 | 2025-10-01 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 8178182c-2274-39b9-a03b-dfcb682b3cb2 | -12.2344 | -47.8086 | 2025-10-01 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 28109be5-61ed-3c48-8a3f-21c63de14816 | -8.8926 | -46.6296 | 2025-10-01 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.9 |
| ed6237bc-fd33-3b55-bd9c-f3c5c4f2c5f8 | -13.3274 | -47.8536 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| c26c4500-f3f5-3ed3-b0e2-b394564fdc9b | -14.9079 | -47.2193 | 2025-10-01 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 139.7 |
| f0458d41-0149-3fe0-ae8f-f906a663f30f | -9.9391 | -43.6012 | 2025-10-01 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| a37b75fc-ffaa-3ef2-a4fc-0b4dc78eda3a | -11.7797 | -47.5806 | 2025-10-01 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 4192f235-6fad-383c-8677-439b435e7dbf | -6.7165 | -44.5987 | 2025-10-01 13:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 0ce759e3-395a-3202-be18-15a1c1f0aa71 | -8.5404 | -44.6975 | 2025-10-01 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 53eaf1bb-3c65-30f0-affe-59a46575b41a | -13.3278 | -47.8313 | 2025-10-01 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 5d64a0a9-87df-36eb-a72e-db35b1d653f9 | -11.3486 | -48.3211 | 2025-10-01 13:50:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 14a82919-2e18-3b6d-8d67-a6d9252f4efb | -9.9585 | -43.5752 | 2025-10-01 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 5fd714b3-bd04-369f-96d0-12b982e8e576 | -6.5546 | -43.9221 | 2025-10-01 13:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| faaf9646-c378-3907-a640-05c7bf52ea46 | -8.8893 | -51.6758 | 2025-10-01 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 5a3117ba-3067-393d-b6c3-86b0660426b5 | -15.9388 | -43.2979 | 2025-10-01 13:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 211.2 |
| fb7d21cd-b9cc-335e-b420-eb9211bf7e13 | -7.6272 | -45.4507 | 2025-10-01 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| b5b70e8f-0322-330d-90fa-ad5ecc6a4faa | -12.7819 | -50.5543 | 2025-10-01 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 247.3 |
| 2509a9b8-b14e-3b9b-8f22-909539ecdc29 | -12.8198 | -50.571 | 2025-10-01 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 8d41e2ea-d997-3d2d-91c0-dee366e5f901 | -10.8433 | -45.3815 | 2025-10-01 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| ede1ae2c-9e62-3912-9282-0db6a5276b2d | -16.0417 | -50.8959 | 2025-10-01 13:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| bc85607e-8bb4-3945-9958-529e6c05ec67 | -13.2973 | -50.6605 | 2025-10-01 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 130c3394-1f54-30d8-861a-315d47123ee4 | -5.8064 | -43.728 | 2025-10-01 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 7ebe7702-5a04-35bb-a877-100c445f8c88 | -7.7313 | -46.2065 | 2025-10-01 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| e6b1a3d9-e258-30db-8015-ca7276339a76 | -11.7793 | -47.6029 | 2025-10-01 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 38e2dea3-d23a-31d3-8f0e-2ec8ddeb0d36 | -8.4827 | -47.8202 | 2025-10-01 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 38dba97b-b5f5-3cfd-9d1a-b75bc8d425d9 | -9.1434 | -47.6457 | 2025-10-01 13:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |


[Clique aqui para ver as próximas entradas](README157.md)
