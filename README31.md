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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1803ed31-8128-3e98-a956-c45f5d620016 | -5.48404 | -45.10896 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7addfba0-207a-36bf-b4ac-d932557839d0 | -5.4304 | -43.86124 | 2025-09-27 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8b611c1-191f-3fde-b82e-ae5a5d07dac3 | -7.05541 | -46.41586 | 2025-09-27 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a4f480f-4a0a-3b09-ae87-d7bc1b124714 | -5.78629 | -41.75247 | 2025-09-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0136c147-4249-3ff8-a26f-7b07aba3aa85 | -6.31278 | -43.3894 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3917c7a-73f9-3026-b602-3977df479d45 | -4.38258 | -48.069 | 2025-09-27 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2cedce50-51ec-3618-a594-f405d38e7217 | -6.9869 | -44.85102 | 2025-09-27 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 937eb844-0d78-3212-929b-585babe06056 | -4.57167 | -44.07944 | 2025-09-27 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90b3426d-3dca-3ce1-a408-55d5eb0d701f | -6.89598 | -44.76171 | 2025-09-27 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35b2d4c5-c9eb-3b67-ba61-fd5765abfad8 | -5.49236 | -43.0798 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87e184ad-ed2b-3c15-96fa-c701920ad8c3 | -4.59073 | -50.66023 | 2025-09-27 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 68e2593b-a595-3897-90a9-ab33fbccfab6 | -6.06272 | -44.0779 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3db8da60-6427-3379-b3a4-cdbf377cbe88 | -4.4472 | -40.96923 | 2025-09-27 04:21:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 482c2577-6d3a-3fa3-93bb-d69f2ce207f0 | -6.69776 | -44.58112 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 474f6a1e-c923-35bd-ad29-a691758133ac | -5.73738 | -44.96305 | 2025-09-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92185f15-b89c-3d12-ac2b-bef40fbccb58 | -6.2429 | -44.09954 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c362cd4-674c-3ae1-81d6-4a8153f8001b | -5.4285 | -43.86112 | 2025-09-27 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6abdb07a-fddf-3104-bfbf-a146f7b0da8c | -5.47485 | -43.0808 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 017aa0f4-367a-3e22-9c05-3afc3b991abb | -6.80113 | -45.54731 | 2025-09-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f71c2260-82d6-3524-b02f-e18ee9539cce | -3.81345 | -40.37202 | 2025-09-27 04:21:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18430423-0eee-343e-97a8-835ea602c4a0 | -5.03706 | -38.00749 | 2025-09-27 04:21:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 9438646b-8935-32f5-97ac-3e783ded0a8f | -6.99704 | -42.38423 | 2025-09-27 04:21:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a9b4c4dd-d052-30cb-94d0-b8dee9ee0269 | -5.39343 | -45.84894 | 2025-09-27 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfbbd358-f1e4-315a-8902-e15ea576a463 | -6.70522 | -42.74112 | 2025-09-27 04:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d48e070b-0c92-3b89-ac2d-b112b575686a | -6.22808 | -44.19375 | 2025-09-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d43812ac-4404-3981-95d5-5d7f88134f85 | -2.54926 | -48.40529 | 2025-09-27 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f8d2e663-facf-31e3-aa54-fc0645916c27 | -5.08798 | -43.05515 | 2025-09-27 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77088fc3-d58d-3c9e-9fdc-8ea4777484d9 | -6.26487 | -43.9163 | 2025-09-27 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a3078cf-6352-3d50-b5ea-c4afa763d67c | -6.06715 | -44.07148 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a171cd5e-f44b-3a20-a3fe-5738ac88dce3 | -6.49478 | -44.23498 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3333c234-11e8-3489-9860-1e18a325efb7 | -7.62913 | -43.80813 | 2025-09-27 04:21:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7683b7d6-6e37-3791-8bbb-9c1f1c5ba5c3 | -5.49009 | -43.07206 | 2025-09-27 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08f248bf-5ccc-39e6-ba26-2f0d4f7556a4 | -6.31623 | -43.45615 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f4912ad-092f-3d47-943b-e29737cc09e4 | -5.979 | -44.93343 | 2025-09-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30f3ec25-03c7-3ea7-9645-d19d1628e69d | -6.11953 | -45.62738 | 2025-09-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2195751d-6675-3b82-b1d3-6d50191d489a | -5.80935 | -42.81412 | 2025-09-27 04:21:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 52a304df-eeaf-379c-9e82-a848cad79cd6 | -6.07436 | -44.06905 | 2025-09-27 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12f2352a-7cca-3cab-a911-a4449543d4ea | -6.70108 | -44.58165 | 2025-09-27 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78bdb545-87dc-3e29-8dd7-da836fbda22f | -5.7806 | -43.82991 | 2025-09-27 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6389de9-f043-3b7b-90af-82efe64ad9fd | -4.64673 | -50.97064 | 2025-09-27 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47ea9148-0cbb-35b4-9137-d28967cb509a | -8.72276 | -46.69025 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0b7261a-e0f9-3e7c-8765-0cc0181ee0f2 | -9.17922 | -46.65202 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e83962d-11b4-30fa-b4fe-770a6afceee1 | -12.88001 | -47.09845 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98b93d7d-4f2f-3bbd-a0da-bda8a4e293b5 | -10.31166 | -45.22916 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d692bd40-4080-3913-a6f8-9055d104dab0 | -11.67714 | -44.308 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d19d9c5-d679-3e0f-a3df-c13c3ca25865 | -7.67303 | -47.4208 | 2025-09-27 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59c7f9c0-902a-3b6e-a7ca-e7681a742e6e | -11.71632 | -44.41636 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9227d953-52fb-3166-89bf-0e5f2b574b05 | -11.67333 | -44.4699 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03255b04-20b8-391a-9a63-ea77f40d7ea3 | -11.42999 | -45.01434 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3abf331e-5f44-3ad4-affc-229c75f1d5d1 | -11.36384 | -45.00774 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3ea8d77-62ab-361d-81e2-70ba7ede6817 | -11.77722 | -43.76258 | 2025-09-27 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e5586952-5273-343e-8b23-e13910aeaa9f | -11.70217 | -44.46314 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90cd0ebe-d8f5-3e55-b0ac-cb077a94656e | -11.43888 | -44.97897 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5702cd5f-6422-333a-bb15-f5b8f455ef46 | -13.17912 | -47.42691 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f765f81-dbbf-31ad-906c-34a99b798849 | -12.30427 | -44.35454 | 2025-09-27 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| beea4017-a4a4-3325-a874-5fc40c5ae0cb | -9.05308 | -45.51647 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abc1b318-4bbd-3915-8f2b-72769a523e37 | -13.33687 | -47.30001 | 2025-09-27 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27e6bb86-0115-3383-b7d0-7381004abc01 | -11.38395 | -45.03288 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27f3876c-b677-35c9-8744-3bb8eebfabe6 | -11.61998 | -48.50486 | 2025-09-27 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbaf97d2-914b-3555-b626-9a9815df629a | -8.91239 | -46.09938 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5299118-3c11-3223-8aab-58fa3eec0c5c | -11.37496 | -44.95813 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a525c663-d8a3-3c4d-b7ce-104765f16e60 | -10.17897 | -44.86793 | 2025-09-27 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b397e794-c685-3af8-9004-5991d7d7d0b0 | -10.7916 | -49.15866 | 2025-09-27 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3faf6150-4044-3d78-9dd1-4e23eab35822 | -9.03922 | -45.51784 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf91c79d-7c29-369e-bee6-c680e8cb7b69 | -11.35938 | -45.01434 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de625110-9538-344e-9cc1-ad38741f358b | -9.97114 | -43.61207 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6262958-41e9-3b3a-afb5-8aeceabceba8 | -8.32499 | -48.00461 | 2025-09-27 04:23:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 705d7cd4-a3b6-353f-99c8-0686e83557b8 | -8.81858 | -46.26626 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2e71c18-395b-3cef-b539-bb06a05df6e1 | -7.77491 | -46.9322 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cf5c494-fbcf-3076-9e43-06e437791a6d | -11.71689 | -44.41267 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0101e381-b03e-3de8-92c2-3752725c19c9 | -8.81079 | -46.25037 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf01824a-0a85-3421-a49d-ea98072c5076 | -11.43776 | -43.51062 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1163091-fa22-3807-8fbb-77468cb5f159 | -11.49835 | -43.53592 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51e0fb59-55ad-3517-9b51-a3b84dfc9ab2 | -12.44745 | -43.5392 | 2025-09-27 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b051926a-4e9f-3a30-976e-60db463bc777 | -7.67653 | -47.42137 | 2025-09-27 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4fe1847-3274-3757-b632-3999e04f144e | -8.20587 | -44.40646 | 2025-09-27 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5cf5f11-ec91-3046-8191-eabbd5c1268a | -11.38501 | -44.93762 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d23bee6-cb4a-3f01-a5ac-244b3914325d | -11.42984 | -44.92613 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b445d23-f5ab-3f9f-83b9-92357d8b78c6 | -9.16175 | -46.65281 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 135aba24-6505-3346-8143-d90f22f63dc1 | -7.65704 | -48.2108 | 2025-09-27 04:23:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 617416ef-513b-382d-b11c-8a8689dfd88d | -11.24374 | -45.55852 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ded93800-d1fc-331b-8805-80e97ba70d93 | -7.67273 | -47.42179 | 2025-09-27 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 674ba7b5-be87-311e-9e6a-0582ab538d69 | -9.0503 | -45.51244 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c2980f7-fdf3-3801-9b03-58c4628e4562 | -11.97047 | -47.8961 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 552757e0-3189-3729-bf18-eed939851ffe | -12.64846 | -51.67895 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c414a2f-f236-3f41-bdee-1fa12488806e | -9.03977 | -45.53587 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71c6570e-3616-3c1d-8808-79c7c2e9f84c | -11.69253 | -44.41262 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea26b397-56fa-35af-a9c8-d6fce88bcf56 | -8.67563 | -43.99072 | 2025-09-27 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9943bcfc-721d-3372-8ca7-05beeba49194 | -7.94246 | -45.19958 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42f1ad8a-40fc-394d-85c5-c43b8642874b | -10.12292 | -46.48075 | 2025-09-27 04:23:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddf596e3-0d21-3396-8dee-b24ca87ea412 | -10.30014 | -48.79452 | 2025-09-27 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b983ba1-1398-333f-b387-a5f966fa19ba | -11.35883 | -45.01791 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66e7bb35-a82f-3b1b-9a43-95db6e2454f1 | -12.64427 | -48.15199 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bf164f5-bae9-39f8-97f6-4e268fab2730 | -10.79775 | -45.36816 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b15647f-0db5-3828-9d8c-4d4fd27cb9a5 | -11.436 | -44.93071 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd4c7320-8f2f-322f-8b91-cc40601a037a | -7.77148 | -46.93164 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 942b3bbd-5912-308c-9757-18ddf1efe84a | -11.44344 | -48.52569 | 2025-09-27 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a8ed085-9485-388a-aa58-c0a291821dfd | -7.55611 | -46.40998 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b50fa70-8e94-35a3-b456-d362e74a6283 | -11.6948 | -44.42052 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28064be5-bb16-3a40-ad3d-e9d22c7b7fdb | -9.76348 | -48.58922 | 2025-09-27 04:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README32.md)
