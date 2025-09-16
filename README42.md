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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40c4117c-660f-37d8-bf09-a60bd3bc512f | -8.98232 | -45.75621 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97e949ea-84d2-3bf9-b067-b261a3be6677 | -10.27965 | -46.47988 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3614a440-97a6-393f-90b5-42d7cca2f8fc | -11.12715 | -45.3412 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d6159e8-4fbc-37e6-86be-b95e32e91465 | -13.20306 | -47.30859 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8715f7b5-8bd2-3b2b-9097-db8f798b65a9 | -12.7999 | -47.2511 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4990df5d-2db8-3d6a-b153-3abe4eff78b5 | -8.87998 | -46.18308 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f18f080c-ca94-3341-84e9-868af98914fe | -8.66835 | -46.38364 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 81aaf677-e1dc-3cc9-810a-3035e9b66732 | -10.7161 | -44.74729 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 54126376-13ba-37c2-afac-03f3fc9c834c | -10.47148 | -45.15818 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee7f41bb-7d46-30b0-95ef-3418ec2c2e0b | -9.77784 | -45.93089 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b26a18f-4561-360e-ab1b-7ec158b1ff3c | -7.67788 | -46.29515 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 165028da-5fc9-351f-a240-38922ef5bdb3 | -12.83959 | -47.20606 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ecc0090-c89e-3ab4-9490-8c0d796987bc | -11.44096 | -46.94655 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2aed77fd-dd03-3e64-a6de-ead4a92c1656 | -10.80003 | -45.97779 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f4e022f-cf67-3994-aa63-de5bb562458b | -8.4182 | -47.21787 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77b84f7e-7989-3517-9cc6-382cad3f8dde | -13.51552 | -44.29817 | 2025-09-16 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aa5bf38-bff3-3125-ab16-c0fa0cf38270 | -12.69203 | -48.00053 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f056c721-feda-383b-9b31-84f06d8f4111 | -8.00589 | -45.66693 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ec9a657e-b9ba-3270-9b4d-d7c6932175d0 | -7.40214 | -49.99731 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef52ab89-c695-3c71-8348-b70da24c706c | -8.08426 | -46.83102 | 2025-09-16 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57079cff-a3ea-3565-8cb9-e5d8f95eb4a7 | -10.71693 | -46.49375 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0d6eeec7-92c9-35ce-9064-2de579d71910 | -9.06186 | -47.02291 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4176a1ac-0abd-357d-b86c-3281fbdc1fa8 | -10.72635 | -44.75209 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c603b31c-2570-36c3-a756-8ad269917156 | -11.06874 | -49.73648 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b50a199-458a-3cf9-8b9a-0799870978d5 | -12.95354 | -47.96685 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b36817fe-8640-3cc5-a518-ba3cf80e4233 | -12.24499 | -46.75714 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea70023a-8b43-3264-8e65-c45b3b2def9f | -10.41644 | -50.64417 | 2025-09-16 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f211881f-3347-3428-84a8-79a3abf27592 | -12.96516 | -47.97968 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 880368c2-0ff3-3ecc-a294-b9000455427e | -9.10141 | -44.86202 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| d4cb4c36-251c-3360-a76c-58773eb9a13c | -9.14377 | -46.9536 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d94144d-65a4-3de5-b39f-abbb4515e854 | -7.81641 | -47.50791 | 2025-09-16 04:29:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc4f640a-1dcc-3612-8227-f118a36ed949 | -13.19694 | -47.30392 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7348aa49-5d1e-3321-8ef4-880d18eb8ec1 | -10.79787 | -50.68198 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7505b876-fe0d-32f5-a62f-8e9915fa22ca | -8.13181 | -49.37861 | 2025-09-16 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f784f6db-757e-3aec-8e52-dfa70a13934a | -9.53753 | -46.29395 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a14f612-2665-311c-b72a-fdd7ca274ef2 | -12.7949 | -47.2612 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2f88a78-e6ce-3cc3-8cdc-28c16930cedd | -8.42115 | -44.98196 | 2025-09-16 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e28521ac-3929-3daa-9558-eeedea4ef62e | -12.79656 | -47.25058 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd730212-84d3-34f3-b6a7-320e8bb230fb | -10.36962 | -61.26643 | 2025-09-16 04:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49363357-de17-379b-8372-28063c0fea0e | -9.73464 | -48.1276 | 2025-09-16 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0adb4aa2-bc50-3570-99ce-050e8d6d3a8a | -12.74986 | -47.19915 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca8fbfb2-61bc-36a7-a3c8-e2ff68cb270d | -12.80156 | -47.24046 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 640eb52a-0af4-38fd-a0b8-7eef5f10d684 | -8.95146 | -46.26316 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7d1fba39-410d-3be9-8038-bff4d8af4806 | -10.37379 | -61.25993 | 2025-09-16 04:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a4763c7-be5a-354a-9e06-937f632e7e62 | -12.81991 | -47.23245 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98ee7b0a-9846-30e4-abed-06d5bb35ffba | -7.67686 | -46.28433 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e94c4b9-f6d8-3b1c-a146-e26bd22e1d4d | -9.15099 | -46.97269 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab53e431-3b5b-31da-9f26-8f4716a8b27c | -12.96183 | -47.97913 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c45d0f9f-8907-3b42-8e64-dd32d47fa33e | -11.71875 | -46.87473 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a836d7f-53ae-3c8d-9ca8-241c51c9c9fa | -12.68429 | -47.98468 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b71fc5b-b04c-3158-80c1-0f69409fa575 | -11.43706 | -46.92778 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cda24c35-5ed1-3f05-9c32-d8da4e7d31a9 | -7.98338 | -45.64482 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf5d8e74-9668-38b7-94db-b3120ec53e74 | -10.88748 | -47.79658 | 2025-09-16 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 809cc4b9-0ec9-330e-9bfa-ca5be1e703c5 | -11.28001 | -50.79457 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66f73f7d-1d32-3ede-a9c6-3dcf63098a97 | -11.59479 | -46.97478 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5aa2ffa-d0f9-3cf1-b5eb-5abe1f72b4e4 | -10.1355 | -46.1475 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 009b9da4-00e6-38ad-a4ea-8ac37c5c8d09 | -7.69023 | -45.13404 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d4900ecc-1376-3c1c-9bc0-8fda5cb998cf | -7.48081 | -47.39267 | 2025-09-16 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7f943d4-25c5-3d4d-be7d-57e51b8ef7f2 | -7.94878 | -45.6684 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa90c752-830b-3460-b4d8-c30abf11a6ba | -8.88348 | -46.19482 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d9866d5-ea10-3f76-8500-cbfe16156b23 | -12.67476 | -48.02317 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d417149-325d-3dc0-a942-601745b271d8 | -12.09989 | -44.83045 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9718b297-1272-3068-882d-0536984f4e4b | -11.71207 | -46.87364 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1a1a4639-e92e-3248-845a-e43022ed455a | -12.95077 | -47.96278 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 40c54250-da62-3233-b3dc-adb3430181db | -12.8501 | -47.13831 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2a88409-7f61-3f87-8f2f-e953d3877627 | -12.74264 | -47.20163 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a88bc299-50ea-3b0c-bd94-11c3deae4ad5 | -8.18973 | -47.12698 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 673a3505-951c-32b1-ad71-839687063305 | -11.27562 | -50.79827 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b42423d-4508-3a48-9a1d-0414e90ffbb5 | -8.00199 | -45.66993 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0259df0-e381-3837-891b-c2e0b7987fd7 | -8.59456 | -46.33985 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe237037-b4c7-328c-bfe4-f966f8619a7e | -9.73358 | -48.11276 | 2025-09-16 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f34f4aad-0b30-3ff5-a646-a5869abb5c72 | -7.19726 | -48.60612 | 2025-09-16 04:29:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d56a7ed-7ab3-34bc-a396-c0d8b51fce21 | -10.29743 | -45.36769 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99e2a32c-2d1d-31e2-882d-16e7b49666f2 | -8.34256 | -44.63415 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c790a068-ab9b-346b-90d3-fbdf9baad80a | -12.61611 | -45.75016 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f2d68b76-0e53-343a-823f-6cff4a6dccc6 | -7.69696 | -44.66082 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6316faba-db07-3e84-9b7b-7f3395d3f10a | -7.38227 | -49.99179 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14b5afaf-410a-356f-a5bd-ce63900667ea | -9.4695 | -48.58076 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e226cba-492a-37ba-889c-f2df5f42a113 | -10.64636 | -46.22734 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea52fe94-175d-3377-89f3-f7c5e8bb976b | -12.8238 | -47.22943 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a359203-d9fc-364c-97b8-07bac03dac2a | -11.11911 | -45.34768 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4df2fc33-0ef2-34a7-a0e0-43ffbc413a15 | -8.96857 | -44.19275 | 2025-09-16 04:29:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e90d91a-fcda-3410-99da-a98c1be55b2b | -9.87181 | -46.45176 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 723599ae-4a75-39c2-be08-6e03ed5b765c | -11.24013 | -49.94312 | 2025-09-16 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c776531f-0850-3750-a792-9a159b218999 | -8.70223 | -49.41817 | 2025-09-16 04:29:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1caa6fdd-843a-341d-83e3-4545345081c4 | -12.62127 | -45.73936 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 48a6eeb6-6392-3432-b6f9-538e9e4ff6ca | -9.45794 | -48.60902 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 009e4263-5e65-31b7-97bc-6f49c535947e | -10.18074 | -46.14389 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 870c748e-f70c-33f0-9763-924d78472361 | -13.88179 | -44.85325 | 2025-09-16 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 275fb36d-07e0-3e23-91ca-47b3d9cc04f6 | -7.99693 | -45.65821 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a455e0c-6f35-3c61-b079-d779142eb24a | -8.31813 | -46.91523 | 2025-09-16 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40ce8ebc-21ad-3a27-a949-93c164801c38 | -11.11222 | -45.34658 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 792412e8-4d44-3e76-b6ee-12bd1b50772f | -11.32877 | -43.48386 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ebfb0e8-1dcc-31c3-9e5a-ba27c2615712 | -11.70873 | -46.87312 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f244ea06-7e4a-32b1-a1b7-1a7f326fa52c | -12.97515 | -47.98129 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa73ae8-ae75-3126-b459-d14d50817620 | -13.18749 | -47.29872 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da573287-5d14-3b17-a93f-f8afc7f3ae31 | -12.26434 | -45.29522 | 2025-09-16 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1522577e-9753-3948-9d84-13de7e692d15 | -8.9742 | -46.22712 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76a220a0-c32f-3361-952b-2b25c1fc4f64 | -10.73279 | -44.75718 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b9621d5f-169c-3c53-a8fb-e5aa85160251 | -11.72576 | -46.48464 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README43.md)
