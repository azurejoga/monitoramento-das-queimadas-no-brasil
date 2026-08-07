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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf21f210-86d5-3f35-b3e9-2bcabf8a884a | -11.4681 | -44.5558 | 2026-08-07 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1c067a95-aabb-3dd6-88a6-ae50e3ab3fd6 | -11.1635 | -44.4838 | 2026-08-07 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 018246a3-bb0b-33c5-a4b3-b83ba58dc917 | -22.5342 | -43.55636 | 2026-08-07 00:28:00 | TERRA_M-M | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 33.5 |
| 65c0de80-4174-3fb2-8616-4b4c9448a8df | -20.38973 | -49.3121 | 2026-08-07 00:28:00 | TERRA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| b970adb5-70e9-3203-b5b4-26b5584345aa | -23.02926 | -52.65585 | 2026-08-07 00:28:00 | TERRA_M-M | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| bfed53a6-1107-307d-abbb-6d2db32dc061 | -11.4681 | -44.5558 | 2026-08-07 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2306605a-7bf5-32b2-b58a-99eb020b9dc2 | -7.09 | -46.5526 | 2026-08-07 00:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 49459f4a-a6f5-35dc-a0c9-cdc46c1d6695 | -11.449 | -44.5587 | 2026-08-07 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5e12090a-7874-3084-8a92-08f3aebe1e60 | -16.6984 | -51.3576 | 2026-08-07 00:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e62f17d6-4517-3533-9545-66cb6c36c46f | -15.1169 | -53.5898 | 2026-08-07 00:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 52a2ea89-a9fc-392d-9109-c85c6387a13c | -18.14461 | -47.97276 | 2026-08-07 00:30:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4c78cfe1-ddf8-32df-9258-9c34942d0093 | -16.36743 | -53.76469 | 2026-08-07 00:30:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 7c5316c5-02bd-384e-802c-e83103b21fff | -18.14767 | -47.99066 | 2026-08-07 00:30:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 73468a98-d45d-35a3-b566-28ffb89d75dd | -17.4858 | -53.32985 | 2026-08-07 00:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a220e219-ca1d-3f0c-ad70-f084873b172e | -17.47558 | -53.32198 | 2026-08-07 00:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9a0ab848-c563-3a3f-a4e9-2dfbaa93c8ce | -16.68245 | -51.37384 | 2026-08-07 00:30:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 872bd397-853f-38ec-885e-ac26c9e48b45 | -16.69051 | -51.36112 | 2026-08-07 00:30:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| f6dff165-f948-30f9-8f59-cd55b3ae1641 | -17.48447 | -53.32053 | 2026-08-07 00:30:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7b6aa1a3-578e-3c85-8a7b-93f4fd1794f8 | -16.69221 | -51.37237 | 2026-08-07 00:30:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 058b9918-bd62-3999-b34d-abb0c4bb63ca | -8.5366 | -49.554298 | 2026-08-07 00:32:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 142b44a9-f3cd-3f54-9f55-93ee8c726c9e | -14.4262 | -45.665699 | 2026-08-07 00:32:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1a23ccb-0324-3c35-b3f4-b04f5d8cdd77 | -4.3608 | -47.766602 | 2026-08-07 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0ba58ce-440a-30cf-b0c8-dc1b4c9c8e2d | -11.1578 | -44.4748 | 2026-08-07 00:32:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82e86786-81bd-37ac-9f49-835027465a57 | -12.6213 | -46.906502 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4170a77-5af2-3e9c-9d33-aa74a9c64292 | -11.1611 | -44.488998 | 2026-08-07 00:32:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd3e8548-d66a-3498-8634-7bb46cf6fd27 | -12.5656 | -46.934299 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 379a31a3-a015-3b5d-9772-53f2c6e74ce7 | -11.1765 | -54.845001 | 2026-08-07 00:32:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96509191-3571-3d31-abf3-012544b139fb | -7.0914 | -46.5378 | 2026-08-07 00:32:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47c11932-0328-3a65-a3e0-ecd8163a6997 | -13.7842 | -49.727299 | 2026-08-07 00:32:00 | METOP-C | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 324667b5-8c9e-3ab9-b845-01b041b20ca2 | -12.0066 | -49.292999 | 2026-08-07 00:32:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4239e27-b5db-3832-b679-e7c49a47380d | -6.9937 | -42.912498 | 2026-08-07 00:32:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 09b2ff46-713e-3aeb-ad65-60ddd262ff40 | -12.0047 | -49.283901 | 2026-08-07 00:32:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4170c4c9-c020-3e0a-b52a-fbe2b514b0b9 | -7.0186 | -35.169201 | 2026-08-07 00:32:00 | METOP-C | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2499401-da99-342f-b327-af32fcb90311 | -11.325 | -45.205799 | 2026-08-07 00:32:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b31478ac-2e57-31f1-b474-1286e7dee8cd | -11.3909 | -47.249901 | 2026-08-07 00:32:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1460e89e-d279-321d-b4e8-a05df01ed6f7 | -11.4664 | -44.560101 | 2026-08-07 00:32:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17ef1f11-87f0-3f29-baa7-dda56629af89 | -12.5903 | -46.9058 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4c6bc96-8d39-326b-b13b-db9e660ada49 | -12.3489 | -48.207001 | 2026-08-07 00:32:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eae42f92-a41b-3dd2-8b4e-0e1d58f257b0 | -7.7208 | -46.222801 | 2026-08-07 00:32:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86131cb0-1f25-3ccc-b324-e792087e538e | -12.5574 | -46.943901 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b27c098-f98e-3c15-aa29-95d44ffdf46c | -11.0807 | -47.803398 | 2026-08-07 00:32:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1b8a0c6-8ca6-3e01-8936-d94a5e7cd6d3 | -11.4696 | -44.5742 | 2026-08-07 00:32:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da92c702-73ef-30de-be12-5c8985c16cae | -15.9238 | -43.5214 | 2026-08-07 00:32:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 99944f30-c6df-3896-9c8a-d59353e57eca | -16.692301 | -51.375801 | 2026-08-07 00:32:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 86c42087-3ff5-380a-bd4b-2418df5462d7 | -6.9916 | -42.903702 | 2026-08-07 00:32:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6ae7b0b-730b-344e-988d-9eb67025374b | -12.5591 | -46.951199 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6586ad65-e8c6-378f-b2ce-a5990f0fdf93 | -6.6372 | -56.414001 | 2026-08-07 00:32:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5da026eb-5a85-3fc9-90bb-818a4735cacf | -2.6914 | -47.363998 | 2026-08-07 00:32:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20fb1d51-eddf-3a5e-a5f5-e670432ccbbd | -15.8685 | -43.5956 | 2026-08-07 00:32:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 15f0af1f-fac3-3157-a44d-f13121c4d95a | -12.5558 | -46.936501 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a38d74bd-8e40-3f87-a469-d62106c1034e | -2.8842 | -48.073101 | 2026-08-07 00:32:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4bc0a3d-f64f-3d58-8ba3-71199acbd1c2 | -14.2696 | -45.284901 | 2026-08-07 00:32:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4cccabde-167a-342c-8ce5-b2d8716eb33b | -6.2646 | -46.348999 | 2026-08-07 00:32:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f67ff2e1-9aba-350f-a961-53764542d660 | -3.1232 | -48.579201 | 2026-08-07 00:32:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb447938-9d58-3f5b-b6c4-f6632b9ca391 | -3.0762 | -39.6492 | 2026-08-07 00:32:00 | METOP-C | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2fa0d821-f357-3025-a045-24070a75c5ef | -16.1458 | -43.544201 | 2026-08-07 00:32:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d6df24e9-cb92-32f1-9420-6d949fc5a1b8 | -4.8478 | -45.211899 | 2026-08-07 00:32:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3581f5bf-1032-33b7-8ce5-8983e7083808 | -5.9793 | -52.1605 | 2026-08-07 00:32:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a92db676-47ed-3400-932a-5c2175ab031f | -22.916401 | -43.313301 | 2026-08-07 00:32:00 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c02a3f10-60e5-3a57-8212-b0bebdd4c4ee | -5.426 | -43.441502 | 2026-08-07 00:32:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39b765d0-7392-376d-8014-021b4a3b4453 | -6.2769 | -44.566601 | 2026-08-07 00:32:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71b5665c-839a-3ecc-8855-4c8e44af15cd | -22.9678 | -43.0266 | 2026-08-07 00:32:00 | METOP-C | NITERÓI | RIO DE JANEIRO | Brasil | 3303302 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e1c2cc8a-005e-3db1-a200-acadc6f49a85 | -15.1098 | -53.5966 | 2026-08-07 00:32:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac73562c-ad24-3d8b-af3e-2b2931df57a0 | -2.4787 | -49.325699 | 2026-08-07 00:32:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c67d111-bff0-3907-9c6e-f1f51c1bd18c | -7.0929 | -46.544601 | 2026-08-07 00:32:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da96a1bf-4159-3683-acd7-ef130baa7ed3 | -17.1036 | -47.5826 | 2026-08-07 00:32:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a66f765c-29ad-3b63-a81a-e2f35dcc1193 | -13.8305 | -53.705101 | 2026-08-07 00:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc0ed4d3-493b-3f22-a0d8-d10a4bdd6cde | -6.8549 | -45.998699 | 2026-08-07 00:32:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f93bea77-1f23-3dd5-a722-726b61e1423d | -22.536301 | -43.555401 | 2026-08-07 00:32:00 | METOP-C | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5abc7877-1080-302d-92cc-0a82668f4619 | -6.8565 | -46.0056 | 2026-08-07 00:32:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac64d8f7-c060-35b5-bfba-cb2dd66f69aa | -14.2712 | -45.291901 | 2026-08-07 00:32:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6164b24b-cfe9-3e06-84ac-a1c4981ffd6d | -6.9165 | -41.935299 | 2026-08-07 00:32:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e61d2303-8bb5-3660-9b0d-1ca7c735cee5 | -15.5897 | -43.730598 | 2026-08-07 00:32:00 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| f178a52c-8c66-324d-8737-a8414260a5fc | -10.6311 | -47.487801 | 2026-08-07 00:32:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13d74527-f969-366d-a658-e498e6e9e994 | -11.468 | -44.567101 | 2026-08-07 00:32:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8594b977-6e75-3ce8-95dc-48560b505baf | -11.1595 | -44.481899 | 2026-08-07 00:32:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d19a8830-22d7-3a64-8075-a75cdd9e4fac | -8.4681 | -49.569099 | 2026-08-07 00:32:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81acc089-8012-39b0-bb81-4a915683b277 | -11.1497 | -44.4842 | 2026-08-07 00:32:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 974df40a-3640-3f52-acad-14e65d8de8d0 | -16.6826 | -51.377701 | 2026-08-07 00:32:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b3a57185-7efd-3e5d-be46-892414dfc725 | -2.4771 | -49.318501 | 2026-08-07 00:32:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cabf0c3-abed-3f8c-9bd3-cfd86ef01e95 | -11.1668 | -54.846901 | 2026-08-07 00:32:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3acadbf5-14b7-3800-9307-7d139b383539 | -14.2727 | -45.299 | 2026-08-07 00:32:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf4fabc8-01bb-3b3e-8e1d-12b2ac24fbfd | -15.9253 | -43.982101 | 2026-08-07 00:32:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6debda1c-8e21-375f-9f37-f8ddebcc3561 | -4.2623 | -48.194901 | 2026-08-07 00:32:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55462372-1139-343c-890e-71c8677bd99a | -6.6326 | -56.391899 | 2026-08-07 00:32:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c403c678-8f00-3908-965f-76150fea6ab9 | -12.6197 | -46.8992 | 2026-08-07 00:32:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f5c4257-2519-336c-9928-5895ce57a593 | -15.1063 | -53.577499 | 2026-08-07 00:32:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77f36583-bdea-3aee-a8b0-8f31bc92b341 | -6.4824 | -42.235199 | 2026-08-07 00:32:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8070ac47-23d2-37c7-867c-87c5e4b5ecfe | -16.1474 | -43.551399 | 2026-08-07 00:32:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e9821fac-480e-310e-948e-83c7872fec6e | -13.7821 | -49.717098 | 2026-08-07 00:32:00 | METOP-C | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f1ace313-a824-35b9-a968-3b582d4bdaf1 | -4.2737 | -48.199799 | 2026-08-07 00:32:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a64be85d-44bd-3aa3-a7c0-474ecdc282d9 | -4.2607 | -48.188 | 2026-08-07 00:32:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6570ab8-6a22-38b0-96c5-2567f402e512 | -3.2665 | -49.529202 | 2026-08-07 00:32:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 573793e5-5586-360b-baa3-45a49b6bea97 | -7.0945 | -46.551498 | 2026-08-07 00:32:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8f1bc0c-e323-3b4a-a611-8e29caba9c4a | -4.3624 | -47.773499 | 2026-08-07 00:32:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd7b746-26a6-39d1-aeda-36d79a805468 | -11.079 | -47.795799 | 2026-08-07 00:32:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aac1fcb5-a396-3804-966c-6cbc735fb391 | -13.8207 | -53.707001 | 2026-08-07 00:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62e0c10a-ce27-3b00-b238-32b26c321a1c | -3.8328 | -49.1642 | 2026-08-07 00:32:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f92de382-d332-3bac-88a4-b16404f43cbe | -12.0028 | -49.274899 | 2026-08-07 00:32:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cc38de6-82e8-3382-9712-a4c2ed917147 | -22.537901 | -43.562901 | 2026-08-07 00:32:00 | METOP-C | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README4.md)
