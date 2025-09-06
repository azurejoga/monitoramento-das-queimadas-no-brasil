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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8499afc-556f-379e-aa40-bac7ef481b29 | -7.68375 | -50.29588 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2f28cf4d-a7a3-396c-86a7-b574217d90a2 | -12.49784 | -53.85719 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2d4b191-cab6-3513-b99e-8e807d35526d | -4.37496 | -48.06737 | 2025-09-06 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81b8fa37-82e8-3c90-aee7-44d9be309247 | -4.57051 | -40.34549 | 2025-09-06 04:17:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 67a2d58b-bf2b-346f-9e46-a13fdcd36809 | -7.29988 | -43.72855 | 2025-09-06 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bfeac5b-517c-36ff-b284-c063d82fdb49 | -6.19484 | -53.24457 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2572ce37-b6de-3a60-948c-741299034ff0 | -16.29176 | -45.6855 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c13006a-0418-3ae5-80ec-b341c04ac760 | -3.37987 | -50.84952 | 2025-09-06 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fe9b53f-c9ae-311c-a4ba-d9a4d1d90a48 | -5.75554 | -45.53456 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c309e0a4-1ef2-3db2-8a22-d075379032b4 | -5.79154 | -45.62638 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d01bf115-39ca-3e5c-8bd7-8a2af534e1fc | -5.72859 | -43.90715 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5568daf9-caf0-3391-ae02-5b18ac4ffcfb | -16.09835 | -45.17309 | 2025-09-06 04:17:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a579931b-e67c-32ca-94e5-4b269518f119 | -15.54456 | -48.3984 | 2025-09-06 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15f2092c-7ab3-34e3-873a-67c9b957fafb | -13.04957 | -47.09856 | 2025-09-06 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10e447a2-89b2-30f3-8279-31d2f9aceca0 | -3.24683 | -50.80576 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8d2837d2-3cd1-3df3-9a57-c1e0481ca5ce | -6.08906 | -43.29705 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b594c548-f529-3d02-8447-d7aa703f522f | -5.99285 | -42.98977 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b05e59d3-a40f-341a-839d-3617d6486ef9 | -9.7921 | -48.33995 | 2025-09-06 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 537f6d2d-eb98-3ed8-9cf7-008adaa4cc3e | -7.30321 | -43.72908 | 2025-09-06 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7915827f-417e-3e59-8666-4ff72b5c83f4 | -6.55555 | -42.961 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 573b4281-8427-3cb0-9e75-b3445d2a80fb | -6.19407 | -44.77204 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c677f62-fdc4-3178-8b05-9b0dafd8ee07 | -6.22132 | -43.57473 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 210a401c-7bbd-39e9-8c8e-df33e21fb387 | -9.74002 | -51.06602 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 52b2393e-9d8c-3eb9-aeca-bf91522d712c | -7.32767 | -48.50019 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 835191f4-af7c-3fc9-83c5-3408274866f0 | -8.02251 | -44.76694 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5c04b3d-f30c-3814-bc85-b5619f621dd7 | -5.18219 | -43.04245 | 2025-09-06 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc63a365-d0f1-3076-9f6e-49494864ae94 | -6.20142 | -44.18581 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20219447-5025-37b6-a0f7-e9defc30532f | -5.83313 | -43.97456 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 216283ca-389d-31cb-8fc2-45a62ce5188c | -5.98444 | -44.72831 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e13bab1b-602d-3531-ba21-6f31392b5d15 | -14.59154 | -48.09039 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4da1f3f-91a2-3c9f-a848-a1c24c8095a0 | -14.583 | -48.00986 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e0affee-181f-348c-ba4b-a99abea90f8f | -12.9936 | -54.8205 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c0521a3-3763-32fc-ae75-c30bfd4e86b0 | -12.99835 | -48.05095 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f88ca4f9-47d9-314b-8b5c-c31d50026904 | -13.35868 | -46.83401 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb8cdf73-cffe-3120-9002-7c8ead37ae91 | -14.83735 | -48.18546 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc3a3606-45c2-339b-a810-3c4691afeebb | -5.73135 | -43.93304 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b47f23d-9250-3be0-8f5e-ab900a32baac | -13.00972 | -54.82799 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 73d720d7-0521-3032-998c-8c0c6ca50212 | -6.22723 | -45.12575 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7c90b07-dc46-375e-80e2-d3d68637eec4 | -7.69528 | -50.28404 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6a3c3fd8-ac8f-35c5-ae01-24ae62e04c41 | -10.3086 | -46.34159 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6617dd4c-12d2-3f9a-8972-8444512446d8 | -7.96521 | -44.94431 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49774a78-681f-3837-814e-421c8d990488 | -5.65304 | -43.61734 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a10df335-9f63-3be7-8f77-83488bb196e5 | -10.06711 | -48.06242 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42f591b6-4e7b-3cda-84e9-fbd6ff1f8143 | -6.84589 | -43.04995 | 2025-09-06 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e876b050-7fb0-323c-ad96-7ba0d8b042da | -4.88948 | -41.78666 | 2025-09-06 04:17:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1164a256-b0d4-3887-a340-1e6cb8a3c95a | -3.80463 | -50.03475 | 2025-09-06 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ae3a87f-4a16-326a-b805-bc1b1da51391 | -6.21076 | -43.57663 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba95f922-f3d1-3d59-a5be-c92929a3fad2 | -9.08454 | -47.00885 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a657c16-1d71-3b72-a465-0b4ca0923735 | -7.41581 | -44.95109 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d3c0924-448a-3386-ab4f-242c76e8e2fb | -5.98485 | -53.5952 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f44ef2b-6d4f-3b34-b7a2-18ffa7c4288d | -6.24607 | -43.28964 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ff9fa7b-fe87-3b1c-b988-1ec38e4ecc75 | -7.65217 | -46.73347 | 2025-09-06 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 436788e2-f2e2-3172-89f3-2ecd407e7470 | -15.07687 | -48.11862 | 2025-09-06 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93c8abac-7abf-3b37-8cc5-6faf45f4ddba | -5.93031 | -43.019 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5161fde5-f463-3034-9daa-19c9f3c37597 | -9.02063 | -49.80318 | 2025-09-06 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4be83df7-5264-3dfb-95c7-b3f5e686517f | -7.57542 | -44.67366 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83a18047-cc1e-3634-abe3-7bd5d95dc9a1 | -6.55441 | -42.94659 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8b74985-1757-381b-85c6-8658b5d75c32 | -5.68322 | -46.34217 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79d0cf51-0e6a-3b7a-ae9f-a365425e00c3 | -8.4922 | -45.10012 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63755928-234d-3466-876c-f1e0473144d2 | -6.76176 | -45.93377 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48d9393a-d0c8-3092-a8e4-8663a040c3d9 | -14.57515 | -49.12526 | 2025-09-06 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8e7bfe8-e60a-3e43-8c09-2af8adeba16a | -5.7411 | -43.69951 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00e6d659-deba-3252-8f8a-87a2d3fa8e18 | -6.22076 | -43.57821 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d53ad82b-c374-34c6-95a2-82e6d9ed35ed | -19.62692 | -46.01744 | 2025-09-06 04:19:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8194e9f4-9ce2-3319-a07a-3af6f22f775c | -11.01329 | -45.92206 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2a330fd-70c9-38fe-9a36-ea1598ade9a0 | -11.22001 | -46.17684 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c4df1a81-5290-386a-b698-831f0f3a562c | -18.00763 | -49.26363 | 2025-09-06 04:19:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20eaacf2-f6cc-3d66-921b-037cf90ea41f | -10.97033 | -45.96896 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 576f23bd-acfc-36b7-b0bb-ee5049458f16 | -22.15595 | -46.40026 | 2025-09-06 04:19:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 692f1c4f-924f-3dcf-84d2-47378e6b58bd | -18.00842 | -49.25919 | 2025-09-06 04:19:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb00d112-f684-3588-9a24-031b9ea1550a | -23.10312 | -49.85074 | 2025-09-06 04:19:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d71560df-15b3-3e53-ab47-bd16126afcb3 | -17.96461 | -46.90408 | 2025-09-06 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df18a4c6-427a-32c1-9a7d-448185a56711 | -12.29733 | -49.99253 | 2025-09-06 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5831fb92-a124-3d6a-9fd7-2bc0197658e1 | -16.32543 | -52.94959 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fe25136-b315-32a7-b54c-e83d8badbad0 | -21.13868 | -46.27399 | 2025-09-06 04:19:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2d8365e8-c1cb-3425-9147-03e58372d341 | -11.93316 | -46.64741 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65da9c5c-5f94-3435-bd5b-bc011927a146 | -11.64623 | -47.1509 | 2025-09-06 04:19:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79d68c13-af33-3132-9593-72c85b593ca2 | -16.33109 | -52.94571 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b261d69-5a36-38d1-a450-f310532de953 | -11.75146 | -47.74522 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| acc5bfef-9a4e-30cc-a55e-c2f0385c1d75 | -10.95016 | -44.8293 | 2025-09-06 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5250469-b1c2-3c4b-9708-ae8b9cabcea3 | -10.47362 | -53.64005 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c3a39d4-0be4-3f1c-897c-09bf0d2e9e51 | -19.81362 | -57.97092 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a54b424f-90b1-37f7-b53d-b06d5ed280e5 | -16.33014 | -52.95049 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 762f3916-b058-300e-8a96-ede56cc74c85 | -9.23528 | -57.07431 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01650421-671f-3b37-93ac-d4e8a7e12027 | -23.09863 | -49.8477 | 2025-09-06 04:19:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7087d7ea-4631-3e0d-bbc5-a74380c47cf6 | -16.32269 | -52.93882 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c60a8d06-74f6-3cf4-9fb4-59aad6c7d072 | -11.93281 | -46.67145 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68e97966-b497-3b78-b58f-2311e4be6e73 | -10.46623 | -53.62118 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be33cf6b-8e98-3e09-9e41-65a49b0a96b3 | -10.47292 | -53.64366 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d35d52fc-07a1-33a9-afad-6eb3b06ca93c | -12.08855 | -45.69262 | 2025-09-06 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e3778033-3533-3b7e-bf67-fbf7597f5d4d | -9.23398 | -57.08092 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ff26370-4b7a-39bc-8bae-c2a754ee7138 | -12.08796 | -45.69628 | 2025-09-06 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3a6863a-75ac-3afc-820c-17e5cd655444 | -21.99903 | -49.91552 | 2025-09-06 04:19:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 67a520f0-16ac-3922-8f2e-89c66a427ab3 | -20.18501 | -44.24184 | 2025-09-06 04:19:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 71fbae90-c5e4-3809-94db-5f722f51c769 | -11.00707 | -47.15061 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fea978f2-8500-33cb-8f33-9ae865beae5b | -18.44003 | -45.9384 | 2025-09-06 04:19:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5653b42-5e3a-364c-bbff-fc7087cb09d7 | -23.28905 | -50.95143 | 2025-09-06 04:19:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 211dbb27-a71d-3965-a78b-4f5b5025dce9 | -11.5996 | -52.18834 | 2025-09-06 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0f3f1d9-ca2b-3b43-8f0e-84fcc70c3eb9 | -22.25301 | -47.30557 | 2025-09-06 04:19:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 52b29672-0d18-31af-9e46-8b920ffaa9c4 | -21.83617 | -46.4596 | 2025-09-06 04:19:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |


[Clique aqui para ver as próximas entradas](README47.md)
