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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44809838-fc40-3f04-979e-2d52dc9eb6e4 | -11.37276 | -47.48358 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 79b08aca-7477-341d-9ff4-dbf7db923d42 | -10.6251 | -46.59682 | 2026-07-22 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5724817f-bd05-376c-aa99-5cf6afbb2ee9 | -9.95794 | -50.55199 | 2026-07-22 04:44:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a0de7a1-065f-3257-ade7-3158c18a3ae6 | -7.90475 | -48.27663 | 2026-07-22 04:44:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c7dee51-662a-3d1e-8959-2c80ad238e6c | -8.74975 | -49.07327 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0053ad33-c2a4-36b9-880b-65124f96c81c | -9.18433 | -58.06966 | 2026-07-22 04:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6918f9ef-9199-3753-a18b-0a5752facf7a | -11.6377 | -48.54802 | 2026-07-22 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a701854a-d86a-3311-9277-5aef0760ce82 | -7.00537 | -45.43238 | 2026-07-22 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a3e56d5f-1b22-3f7d-931d-eccfdfc7c574 | -8.74586 | -49.07623 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4596a2e4-4a55-3035-a241-c18a1bb82552 | -11.37617 | -47.48412 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 774b24c3-e14c-3a9e-ac23-2793a296a727 | -8.75805 | -49.08537 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77fc4b19-4d8a-32a0-a564-9736e73b5dd3 | -8.73973 | -49.44708 | 2026-07-22 04:44:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01555149-1568-309d-9396-513af6cbc85e | -5.71232 | -45.66426 | 2026-07-22 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d0a5811-d675-3cb9-8b44-e42b36c1fd76 | -6.67317 | -47.52213 | 2026-07-22 04:44:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 878c3610-a719-357a-b493-dd6c8ec60356 | -9.90577 | -47.87743 | 2026-07-22 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f3849d6-63e9-3708-88c1-9b90717df99c | -11.4171 | -47.51305 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a56afd89-d981-3d7b-978a-48d55cf6724b | -8.7453 | -49.07973 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa3e5248-e8ef-3cef-86ab-0f080d2c60ae | -9.18495 | -58.06623 | 2026-07-22 04:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46f472d7-7b4b-3dda-8013-0cd2f691f7ea | -7.1765 | -41.40406 | 2026-07-22 04:44:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 23d6c498-54ec-3811-b8c3-6ced5de39dfa | -8.75861 | -49.08187 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcf379e2-b130-3a49-b0b2-58574c3e6528 | -10.66496 | -49.56065 | 2026-07-22 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 485eb93d-e832-32cc-bf50-16e141a6fc40 | -11.40176 | -47.49933 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09130c86-d5e6-382c-9b9e-affbfac63d0a | -10.83177 | -50.4426 | 2026-07-22 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85698443-4f70-3780-ac4f-d1b83486256f | -8.49063 | -54.7758 | 2026-07-22 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f658af16-a7e8-3915-8a75-206095f55dc2 | -11.8891 | -43.83009 | 2026-07-22 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3126a1a5-63f9-37a6-8216-5314da8188ad | -9.3822 | -47.08951 | 2026-07-22 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5d37d13-01d1-323b-9a8f-a7c144a54c90 | -8.49076 | -54.77423 | 2026-07-22 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 443af8a1-abae-37bf-b4aa-91ba6df41719 | -11.3995 | -47.49133 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7dab3d9-9299-34e7-89ab-d200d6720b5c | -5.67343 | -43.57309 | 2026-07-22 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67aae88c-0a33-3a47-ad21-2aa8a368868c | -11.4203 | -47.51328 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 753d615f-ca0e-3295-85a2-33fd4cd44a85 | -10.63269 | -47.48745 | 2026-07-22 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0673af9e-38b2-35f9-ac0e-3fc5633bee69 | -11.33507 | -47.99807 | 2026-07-22 04:44:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94d62053-bb59-31c5-9634-9ca808014e4b | -9.09833 | -59.40481 | 2026-07-22 04:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ac7ebbf-f78e-3497-82f7-db54e103bbab | -7.80429 | -47.11937 | 2026-07-22 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6881844e-6c38-3390-973d-d497891f6af8 | -7.00242 | -45.42783 | 2026-07-22 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f026a423-2c7e-3768-a38f-27bec875597f | -11.33114 | -48.00114 | 2026-07-22 04:44:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d4c3e77-5156-37be-b7f5-6abf850f5379 | -5.55234 | -45.18306 | 2026-07-22 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2332a2f9-e994-38bf-96a4-96b2fd7f1e17 | -9.22721 | -48.55949 | 2026-07-22 04:44:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ea4a21d-729f-3c2b-a3fc-62e2424744f1 | -8.4899 | -54.78005 | 2026-07-22 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c60cc88d-0c83-3628-9124-1a09431d591a | -5.63778 | -47.09856 | 2026-07-22 04:44:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 054ca63f-ba88-3368-adb6-2cb0f6825d92 | -11.41688 | -47.51284 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5fa7832-faf5-317f-b707-af08d954f765 | -11.40118 | -47.50308 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f0109d4-1791-3f40-9ad3-4467c45fd646 | -4.28036 | -48.24849 | 2026-07-22 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f932557-e95b-3459-82ef-26f263caee5e | -9.20495 | -49.82554 | 2026-07-22 04:44:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80ca0419-947a-349e-9d0b-9a97a28d5a8f | -6.60812 | -47.99977 | 2026-07-22 04:44:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ee571eb-ea4f-32a4-86ad-c2b6d341eab7 | -9.22776 | -48.55599 | 2026-07-22 04:44:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f19d9556-8f40-3f5a-a927-e2320187933d | -9.22972 | -50.15163 | 2026-07-22 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a9715cb-1de8-3d5d-8cc4-5abc99fee38a | -11.55516 | -47.6135 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e659852-5550-38e5-a65a-4b7ccd978a03 | -10.35293 | -44.75166 | 2026-07-22 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72ff2b12-e31e-33c7-96ad-8c94c6f88e8b | -11.63437 | -48.54748 | 2026-07-22 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 666e30ae-b2d7-310c-9e55-4c619435eaa7 | -10.16742 | -56.80238 | 2026-07-22 04:44:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1896dd5b-2fac-3179-8997-8a51d0500a6b | -10.5418 | -50.27192 | 2026-07-22 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bfff4e3-b96f-3681-a553-10bb678fd5b8 | -5.74645 | -43.27256 | 2026-07-22 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 142d8ab8-c09c-3bff-b8f5-09e711c549f3 | -10.30664 | -49.64709 | 2026-07-22 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebe28a33-48da-318b-b1e4-ab116b453245 | -11.81376 | -47.33437 | 2026-07-22 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 10800d80-8187-39ce-b94c-3f8dafa988f2 | -3.98796 | -48.38488 | 2026-07-22 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42e32732-345f-3a05-9e61-d91ef6ee5bc1 | -11.37958 | -47.48465 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9f9702c2-9173-35f7-afd2-b0caa2f84fd9 | -8.74919 | -49.07677 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b9544edc-e7fe-3ed6-a0fe-8f1a19bca2ae | -7.01309 | -45.85196 | 2026-07-22 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7dc491f-2465-3da4-8f3a-dba070d918d3 | -11.91242 | -43.8451 | 2026-07-22 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8914e6d5-90b1-3b84-b628-448d78178733 | -9.69982 | -47.69937 | 2026-07-22 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9a62228-0a91-35cb-a382-5e91e06826be | -8.82999 | -47.07353 | 2026-07-22 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8d25fff-1055-3107-aca7-a23a599bfe3c | -11.42315 | -47.51751 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fcab79f-39b9-3c69-a9b9-513dfa8e65f0 | -9.46683 | -45.6527 | 2026-07-22 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a92e32c2-9aeb-34d1-8ddc-b2fd7ad33498 | -10.3235 | -46.84458 | 2026-07-22 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d788b5b-d206-3221-ad32-c455cb46ffed | -7.00658 | -45.42435 | 2026-07-22 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8f79460-aba9-31c8-a5c4-6f80c1ff0b1c | -11.63492 | -48.54393 | 2026-07-22 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba645150-21dd-3b4c-a4c3-99db325f6482 | -10.63326 | -47.48376 | 2026-07-22 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c105586-083f-3b27-baef-485148106f91 | -7.18106 | -41.40473 | 2026-07-22 04:44:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7832375a-1f3f-37bf-8d89-3e7a9eef7470 | -8.75196 | -49.0808 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6355e381-d73e-3a3a-a5da-5e5cf0643350 | -8.49001 | -54.77845 | 2026-07-22 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10ee4d99-5bca-30a5-998f-183fd44a414b | -7.00597 | -45.42837 | 2026-07-22 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c382ffe5-00eb-3484-bf77-3ebab1d1db98 | -7.83684 | -47.10971 | 2026-07-22 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46a38f94-5227-3679-92d4-8c5231b93bc5 | -10.66829 | -49.56119 | 2026-07-22 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91da6b6f-2a17-31a9-bf88-a575c306a1b5 | -11.88495 | -43.82947 | 2026-07-22 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4e30d87c-e33d-3031-bca4-6a6db9a82c10 | -11.80975 | -47.33761 | 2026-07-22 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1169f7c1-f1a8-3c94-8075-6fc821a8f159 | -7.19788 | -45.49194 | 2026-07-22 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81efe5a4-b640-371d-9b76-fb96056be0c5 | -8.75472 | -49.08484 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1638695b-bc83-3cde-a240-b3a554ffcc5b | -11.3345 | -48.00169 | 2026-07-22 04:44:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7de74e5e-3d3f-345c-94d2-ef8eb979379a | -5.63722 | -47.10208 | 2026-07-22 04:44:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fef24a97-f27a-34c7-aeb2-2de84f16b19a | -10.54516 | -50.27249 | 2026-07-22 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0be02ac5-4a03-3f70-ac8a-f95ea825cd01 | -10.95314 | -49.81064 | 2026-07-22 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5377d9bb-ed06-3dae-abed-75edbde443ed | -9.63984 | -47.81071 | 2026-07-22 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77d775bf-9623-3de1-ac83-1bdafb7fe9bd | -9.01439 | -40.99134 | 2026-07-22 04:44:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7c176626-dce0-39cd-8978-64e7d491dc94 | -11.40517 | -47.49984 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c69cec23-b35b-33eb-8092-447d1b287a67 | -9.23311 | -50.15219 | 2026-07-22 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ec6c4e7-e76c-37b7-9238-04b44800e785 | -10.50913 | -50.28136 | 2026-07-22 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f783e30-94b4-3fcf-ae9b-fa0251bd5e56 | -10.6293 | -47.48694 | 2026-07-22 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 239db37c-920b-32a8-9de6-137d2e70c0f5 | -5.70944 | -45.6599 | 2026-07-22 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08fbe1e8-8303-3b59-9496-88b4b7b4c10b | -11.81319 | -47.33816 | 2026-07-22 04:44:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b97c86c-3d11-38a1-8be7-05df92646fd2 | -7.90752 | -48.28063 | 2026-07-22 04:44:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af35abd7-8fc4-332e-a3fb-b489ddb66d26 | -11.41143 | -47.50454 | 2026-07-22 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de44818b-f5ed-3179-a631-6e5e099ce6d5 | -9.09758 | -50.18999 | 2026-07-22 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a23c2ba-5a13-3d8b-a43b-4918bec4a22d | -5.7425 | -43.272 | 2026-07-22 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fa3f4bff-c476-3032-92e9-6bcebcabab7f | -9.22389 | -48.55895 | 2026-07-22 04:44:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd3de599-5133-3227-b86b-6b9a33671843 | -11.09808 | -46.9476 | 2026-07-22 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 549572ed-bbc0-3934-97c5-20a5c3a4fd8b | -8.75528 | -49.08133 | 2026-07-22 04:44:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 829ff4a3-f4b8-3054-b02d-b18cfc8d80b3 | -10.42734 | -50.20127 | 2026-07-22 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92605563-eb7f-39da-b281-e7403feb8ef9 | -10.16479 | -56.80346 | 2026-07-22 04:44:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f00a0f44-ac16-3965-b27e-6567d0cc0a28 | -11.63826 | -48.54447 | 2026-07-22 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
