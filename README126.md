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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58af7a9d-d612-37db-9f9f-384ce8e112d7 | -6.3198 | -59.9572 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1908ca23-d134-3c35-a773-f5f7978fd291 | -6.5569 | -45.566 | 2026-09-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c2bde1e9-3767-31fe-86cc-a5dd07856f1d | -10.7466 | -50.5959 | 2026-09-21 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 06973823-6769-368e-880a-4cd9bb1c4688 | -10.0714 | -50.2387 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 95a884b4-86da-3163-b710-81f482d44c22 | -10.336 | -50.2119 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 65162591-4a39-3c08-88d0-bfb166135b1d | -9.457 | -45.395 | 2026-09-21 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| f8b394c2-cb9a-3894-a67b-5b1a9b7e4e0f | -10.8909 | -54.0882 | 2026-09-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 8e883d3f-96a7-3fd3-a828-85264eec9c3f | -9.4567 | -45.4178 | 2026-09-21 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| de868776-3641-3270-9af9-102505317633 | -7.3291 | -55.1955 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f57d3680-ac15-337b-87da-2a6258e3cd00 | -3.7856 | -60.7335 | 2026-09-21 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| cb08a881-f122-3cac-9cc3-bbf2fb64519a | -10.4486 | -50.2644 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a45f982f-b66f-3ce7-9a86-15ec53254fd5 | -10.9544 | -50.6165 | 2026-09-21 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d264117d-bc1e-377b-9216-1b167f33b157 | -10.7999 | -50.8455 | 2026-09-21 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 1525ca76-5688-3da1-aff5-6d8ec0d168b1 | -11.4353 | -45.3459 | 2026-09-21 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6c3bbbee-b39e-30ea-a644-eafdfab06d1b | -6.5571 | -45.5434 | 2026-09-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 6d84c3b5-5ac2-3a4a-9596-d5974d2494d4 | -8.7911 | -48.7502 | 2026-09-21 14:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 9101a0f0-7ca6-3e68-bfba-b1ee1891c4f2 | -15.4471 | -48.4566 | 2026-09-21 14:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| b4cfe52f-4133-346b-a4c5-383210b578a3 | -14.1819 | -51.7866 | 2026-09-21 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e07268ed-1f41-3dc4-924f-3cf999320257 | -10.9112 | -53.9635 | 2026-09-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3e97657a-5b50-3d16-9444-b095a3d7acba | -11.7823 | -49.8152 | 2026-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 3be1bb94-42d1-3477-bb92-5454a462d047 | -5.7615 | -57.5807 | 2026-09-21 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9532def7-3815-3b20-8392-cfb476a39eca | -11.8491 | -46.8556 | 2026-09-21 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| ee071268-82a0-3fef-aaf8-4e2329af66c2 | -5.9151 | -59.9522 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a146aeb9-4c1a-340c-80c5-3a4881175260 | -6.1359 | -59.9446 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e54eef92-8e73-3d6d-98be-b23bc6ed6484 | -3.7713 | -59.4185 | 2026-09-21 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 049e0f41-038c-331e-ab4e-b447b8d7e44b | -11.2307 | -54.078 | 2026-09-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ca26a6fd-661a-357c-aeeb-5fca8021f97b | -11.6802 | -43.4209 | 2026-09-21 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 8b23bb65-37b1-3499-abba-8be58951c5b9 | -6.1174 | -59.9644 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a01b92da-79c8-33c9-b725-9d375347480d | -6.7184 | -55.0884 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 8c3f7361-1e4e-3974-96fc-a9135c6eda64 | -13.2787 | -51.795 | 2026-09-21 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 50f91c47-75aa-38b2-b798-d28e239cfdfa | -2.8608 | -57.8188 | 2026-09-21 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| cb39ee6f-71f8-3d80-8787-9bc77110a309 | -10.4675 | -50.2624 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7fab76d2-8576-3ae4-8028-97a095e5ed48 | -15.8856 | -49.9145 | 2026-09-21 14:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 58315c71-a1f0-3202-bb61-a974f630ee63 | -3.3183 | -57.8677 | 2026-09-21 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e00d0291-5261-3ff4-983b-ed6350721335 | -3.7129 | -60.5832 | 2026-09-21 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 353f8d91-9a81-34c0-a870-fa470d31bc11 | -6.7484 | -59.075 | 2026-09-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 35ee1b64-4ba1-3ee6-a158-c3113f386955 | -6.7463 | -59.4416 | 2026-09-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7c672b96-3718-396b-846f-9a204e48c05d | -12.8246 | -54.0442 | 2026-09-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 269.6 |
| c75dd241-4967-3e06-937d-81603fa7bb0e | -13.2602 | -51.7548 | 2026-09-21 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 71b9cc39-197f-3243-8652-a9abf28a4863 | -13.2791 | -51.7737 | 2026-09-21 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4b2fffa1-f901-34bd-9f7d-e39a5a4aa090 | -6.1651 | -47.5271 | 2026-09-21 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 589c2f85-21d8-38e9-9842-ecd0597c030f | -2.8608 | -57.7994 | 2026-09-21 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| df20d888-85ad-3ce9-bdd3-07fdba2a402e | -3.3823 | -50.4486 | 2026-09-21 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| ff79f1f8-4afd-33be-a46b-979927794626 | -9.977 | -50.248 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f518af67-e08d-3df8-971c-31afe492664e | -11.8014 | -49.8129 | 2026-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 4bbfdbd6-496c-371d-b1ae-b5b0de7ed49b | -11.1183 | -54.0062 | 2026-09-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d6179fcb-bd3c-31b9-a7ad-257ec36bd3ca | -3.3454 | -42.7597 | 2026-09-21 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 9a7658c3-22a2-35c9-b426-9adeb9dbbff9 | -3.7128 | -60.6211 | 2026-09-21 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 17f3bb84-4514-3b02-96e1-dcf62cda85a6 | -5.6223 | -43.3701 | 2026-09-21 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| e2f99a60-c041-3d62-b08f-775e25a5f9d7 | -9.8307 | -48.451 | 2026-09-21 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 0f55a619-bf8a-3177-a41e-b17f2dc75936 | -8.1686 | -54.7634 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 29a73d5c-1327-3c14-9fb2-ef1a44eb4822 | -5.6411 | -43.3687 | 2026-09-21 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 85a54b3d-f70e-33f6-893c-b05e8e1bf75e | -10.8014 | -50.7391 | 2026-09-21 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| bd9c7636-18df-3e06-94ff-bcf3e3527cb2 | -5.841 | -53.5205 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 98f6fce6-ec75-3e1f-a730-71af3e1dd04e | -11.662 | -47.7737 | 2026-09-21 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 519d4f80-f096-394c-b4d4-0864f0e12496 | -7.5247 | -46.2252 | 2026-09-21 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 698dbace-3bdd-3f33-b9a2-47cb182e4691 | -7.4092 | -44.7885 | 2026-09-21 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 159.4 |
| c5a6ff2b-92f1-3209-89c6-001949e915ab | -10.43 | -50.2449 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 19177e9d-f50e-3f96-a03b-9bfe3dcdb4b8 | -10.9547 | -50.5952 | 2026-09-21 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 3596c2d4-dcb5-371e-955a-d5eb0e656a00 | -13.2037 | -51.698 | 2026-09-21 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 7b12a2db-5b5f-3054-833e-11742c89207a | -10.279 | -50.2391 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| cf86dcb9-a6af-35f3-b8ae-aadb5e437820 | -6.9034 | -42.9341 | 2026-09-21 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 19440b63-baf1-3f71-ae49-a08d63952d81 | -8.0279 | -61.3626 | 2026-09-21 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0251517e-d959-3fd2-87ff-0f43480e9734 | -3.2162 | -42.4833 | 2026-09-21 14:10:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 6214a7b9-bd5f-30dd-ab00-0f0b8aec6657 | -6.8448 | -55.5411 | 2026-09-21 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 6d679629-5348-3c06-8559-20bcc8eacbbf | -6.184 | -57.7981 | 2026-09-21 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8ff8cead-106b-34f7-bf86-5cf52e859445 | -16.04 | -52.52 | 2026-09-21 14:15:00 | MSG-03 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eeec06c2-c56b-3c61-8e1c-f258ff9d0b62 | -9.89 | -48.41 | 2026-09-21 14:15:00 | MSG-03 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50649a19-5860-3082-ac25-7ed6d06c2243 | -6.4485 | -59.9909 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 6355983d-1894-3f96-9774-ace9bd77c6b9 | -12.8899 | -50.9695 | 2026-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |
| cf661024-e73d-35c1-8e33-169bb244eec8 | -6.4671 | -59.9711 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e7d36144-af25-346b-9504-88843afc268f | -13.3443 | -51.2973 | 2026-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 239.3 |
| 41ad1f3c-f14b-3aa9-a27c-22dd580eb0ed | -10.8853 | -51.5347 | 2026-09-21 14:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 21ee2a3c-7ce5-3333-9266-37a988dd5199 | -4.2239 | -48.6127 | 2026-09-21 14:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b4eb7f33-9a36-307f-ae85-a2e9e06b9294 | -7.4283 | -44.7639 | 2026-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ba376e66-6977-395c-af85-96dc4c4eec2f | -11.8491 | -46.8556 | 2026-09-21 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 255febc2-abde-3282-a33f-798b32d33296 | -10.8909 | -54.0882 | 2026-09-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e96f6bf2-d430-354f-8329-9dbf49cc30c5 | -12.026 | -50.0663 | 2026-09-21 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 946e66e3-eefc-3650-acfa-36ed2fe3087f | -14.1815 | -51.808 | 2026-09-21 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 6135ebdf-6060-3577-bb75-3b0044968a9f | -13.2787 | -51.795 | 2026-09-21 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 9f1bd610-6cee-3a21-a672-795333d77dd2 | -9.457 | -45.395 | 2026-09-21 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 35176339-8028-3d2e-8b9f-b725597e588f | -8.1872 | -54.7622 | 2026-09-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 9b208a5f-0ae6-35af-85f1-f5d23cc3fb1d | -9.3986 | -48.3213 | 2026-09-21 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 19572848-cee2-36ac-a33e-d84d24c3db51 | -10.7466 | -50.5959 | 2026-09-21 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| a331c8b5-143c-3ad1-9614-9edfaa9767f3 | -6.1651 | -47.5271 | 2026-09-21 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 56fc0396-c74f-36ff-93f3-10f9d34fab87 | -6.1175 | -59.9452 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 220344d5-2a15-3982-8633-e3db57416196 | -10.4919 | -51.279 | 2026-09-21 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 92192a8d-d889-3e76-b702-05c4ca1c8b82 | -11.0804 | -49.7456 | 2026-09-21 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 4c7682ae-416c-3f90-803a-fbaf8861b6fb | -9.2756 | -46.2077 | 2026-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| a7a08032-2a0a-30f6-80e6-60eda353e85a | -6.467 | -59.9902 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 6877a73b-abb0-3a11-a2fc-c2e4548c2f31 | -9.5593 | -66.0545 | 2026-09-21 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| dd22162a-54d7-3bec-911e-da7ef03aec0b | -7.428 | -44.7867 | 2026-09-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 3a994345-67f4-31ab-bb1d-1ac6235125eb | -2.8608 | -57.7994 | 2026-09-21 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3403d4a5-bce0-35ec-882f-201e68a6031a | -3.1698 | -58.5859 | 2026-09-21 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 474104ef-6552-3ea6-8373-ab19b6cc0663 | -11.0412 | -54.1362 | 2026-09-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 32efeb78-0148-3cfc-bafe-9680c9a9e0da | -6.8264 | -55.5222 | 2026-09-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 766e0afc-98c0-3e04-bbb8-c20d12bafb61 | -12.3216 | -50.6751 | 2026-09-21 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 381077ec-7d8e-3cdb-8859-022cdacadae7 | -5.6599 | -45.4976 | 2026-09-21 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 95b6b75d-8e49-3d8f-9b0e-c5b659488a5a | -8.1876 | -54.7219 | 2026-09-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| d5f2ee44-a768-3a96-af85-a297e8fc83e9 | -10.473 | -51.2808 | 2026-09-21 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |


[Clique aqui para ver as próximas entradas](README127.md)
