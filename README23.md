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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9fc3977-b622-3e50-86d9-c87ae735e819 | -5.43894 | -45.23808 | 2026-08-19 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcd1e3e6-0903-3586-af10-74b42e8d2c46 | -3.272 | -49.51886 | 2026-08-19 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0f9b568-de55-389b-bf91-6bd9839dc591 | -5.91578 | -43.62417 | 2026-08-19 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 643db0cd-eb05-30dc-aa77-29873e7370ca | -6.3379 | -44.07792 | 2026-08-19 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0ac002c-2192-3c5f-b677-adc47c3e6ed5 | -4.70665 | -47.15386 | 2026-08-19 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87f5f3a9-2045-352a-bdda-bd6be691d3b0 | -5.92877 | -46.24007 | 2026-08-19 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ed10c34-722e-3790-a7d3-28e840a13956 | -5.82218 | -43.40233 | 2026-08-19 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9123d9e1-f9ab-3507-9d32-6414949e0a98 | -3.01808 | -51.05884 | 2026-08-19 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e4fe7bc-6e91-35dd-90ae-7f5b381edcd4 | -5.43015 | -48.4124 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 452644ea-436b-3dd3-b4e8-c289274f5670 | -5.70946 | -43.2328 | 2026-08-19 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62d5911f-8ce8-33b1-b315-8bab720075ff | -5.42472 | -48.41645 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 4a53a11a-fe7c-37b2-ad49-3ef62c85df05 | -5.44113 | -41.85033 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32ec3e55-a332-321e-8c01-f54925732465 | -2.76488 | -48.57352 | 2026-08-19 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a09d9fed-5e5f-336f-860a-4260e792caf6 | -5.91638 | -43.62039 | 2026-08-19 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| cc858eb5-c997-3a43-a3e3-ba42f2696567 | -5.43094 | -48.4077 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| f4c0f70c-695c-3525-b255-f52560815cad | -5.91232 | -43.6236 | 2026-08-19 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 41ca0f37-3a42-3a7a-9efa-b0e9e386ec67 | -4.00806 | -48.06429 | 2026-08-19 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d0c3fa5-901a-3c05-90be-53b86de91548 | -5.91983 | -43.62096 | 2026-08-19 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7806137-b721-3d6e-9ab8-337888d3c084 | -6.27224 | -43.27686 | 2026-08-19 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8c1a8a3d-f9c2-356e-90de-e8c2e5bb322f | -4.43264 | -46.13781 | 2026-08-19 04:17:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a91d6aa-af07-3892-9a58-de947d6d4b7d | -5.43856 | -48.41877 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 2add92eb-d1c0-3028-ba35-8e6d4cfc856e | -5.43395 | -48.41798 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 2791bc15-5ff0-3308-85a0-b33b02557ba5 | -6.2305 | -43.68882 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a7a30f9b-a1ac-3aee-b16e-8b4e53b0e55c | -3.4264 | -51.51627 | 2026-08-19 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a059374-7fcc-3ab5-a269-a53b28cf3e72 | -6.53511 | -43.12043 | 2026-08-19 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8fccc795-f472-3b6a-9d00-c8984c1f9190 | -3.27148 | -49.52195 | 2026-08-19 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2da0e96-7a6d-3ff9-9d73-76d6b55655f0 | -7.21769 | -43.28565 | 2026-08-19 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f4e28ea5-2dc6-3409-a6bb-bfb737d4eea9 | -7.94739 | -44.63264 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5e83816-ed11-3a73-b3ca-50634010916b | -11.23399 | -55.06157 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5c9fc0b-3bf2-3c65-974a-4a4a7bc47acc | -8.56801 | -54.75004 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59b92efc-72bb-3044-81f9-4a4b6f23cf96 | -8.55919 | -54.72497 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c00fb1a4-119f-3ba7-ba05-d1b6571f5a28 | -7.55762 | -55.57204 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0152bf13-8809-3cc2-ad62-f08a1e900a04 | -8.55376 | -54.75305 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 693e1a13-ea6e-3e69-8848-09ae28e9dc2a | -8.5602 | -54.68458 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97e9aba9-5d7d-395a-90e0-efe8d455ac87 | -12.79678 | -48.43384 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0f6796f-8b88-3382-b582-82a993cd4f0e | -12.83125 | -48.42156 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 998c3529-95df-3fb7-b431-9a9c07b947cc | -11.12262 | -47.28498 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b1f0854-fa19-3a89-9e48-0395ee3d71c7 | -7.27354 | -44.53614 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62408513-1713-35f0-9abe-f022d0a0a99d | -11.71935 | -45.58509 | 2026-08-19 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0b70815-6338-303c-b5a5-b3416288705d | -8.56569 | -54.69143 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 070910e6-3554-3239-9cec-00de1a4ac10d | -6.02019 | -50.19563 | 2026-08-19 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dec43e6-d1bd-3535-af4e-0c34ff77de48 | -12.75848 | -48.4123 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d845d59-279d-3dbb-8df8-acdc4918822e | -10.67334 | -44.41273 | 2026-08-19 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fcb7d0d2-0ea5-39c4-8844-e7df34a8fdb4 | -5.91311 | -49.25943 | 2026-08-19 04:19:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c522380-5e78-3e76-b138-df280783c046 | -6.33767 | -54.90358 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66188a44-f683-3842-b187-6d210cef7df6 | -6.39489 | -51.75016 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39f07d41-ddd2-3a25-be73-e19843945d1f | -9.11073 | -46.04097 | 2026-08-19 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c4ad4cc-2b01-3081-b6fc-efdb3ea45918 | -8.3603 | -46.36228 | 2026-08-19 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 242e73d1-2ae2-3a73-b14d-534cfb623cf6 | -11.22737 | -55.05871 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1385e9a2-4ee4-3520-993a-b36ca410b1b1 | -12.35594 | -51.2156 | 2026-08-19 04:19:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcbda1df-74ad-3f04-9713-3158d2117067 | -11.22956 | -55.08317 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 880717a9-8a71-3f44-9348-4ceb96c9f547 | -11.07973 | -47.6031 | 2026-08-19 04:19:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34441859-27b4-38a6-a014-25cd9edf84b5 | -9.27174 | -45.64853 | 2026-08-19 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd3e8794-f032-3f2a-943c-bc601edb121b | -9.06003 | -50.8372 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba17c2d5-538c-3007-af36-472f12db8896 | -7.54099 | -55.58279 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e48962b6-e4de-3394-83f4-83bb8502e48d | -11.31177 | -45.2155 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a09352fb-a157-38d3-a27d-212b559d75a0 | -8.55697 | -54.73647 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cdaecc42-4068-3313-90ee-ea818fbdfa23 | -8.56467 | -54.73196 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 31e36158-f1d3-3a88-834b-e26d7c1fccd7 | -8.54259 | -54.77533 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2f33c300-d9a9-3f33-9179-4c2efb59c92b | -13.44622 | -43.84358 | 2026-08-19 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f63029a-7c07-3e43-bfc6-2ffec4fa262b | -7.30459 | -44.56513 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7978b953-78ab-3a48-853b-7b8e89896eae | -8.54927 | -54.7409 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6187dfdc-ff90-3463-9b1c-2b02682ac158 | -7.56021 | -55.55857 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26029a27-bc84-3ae1-8a9a-52c282bf123d | -11.21991 | -55.06262 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b106241-6083-3f53-a532-162d8c83a55f | -7.25366 | -44.21771 | 2026-08-19 04:19:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df3b28c4-a877-34ee-a8e7-bc632b4f694f | -8.54598 | -54.75785 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45075328-66c6-36fa-b727-6c82b7d5f4b9 | -7.64909 | -42.77669 | 2026-08-19 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e341ab84-7a62-3419-bcdd-9175f4cbf75a | -8.55691 | -54.77211 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 40f51db6-8bd2-30c9-b876-6eb7a498d2af | -9.06192 | -50.85572 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3da52790-442d-39a5-84c6-d60c30f10b4e | -8.17794 | -44.43623 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 164d2144-5891-3e95-b2e6-2ef90b9840f2 | -9.49316 | -51.67492 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be91da6d-94ce-30c2-b808-4f4512530d11 | -9.08265 | -50.80006 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85bc4e43-2e4f-3875-9096-ffbb6e97ef64 | -8.35162 | -45.97648 | 2026-08-19 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 14dadf74-0bce-314f-b05e-ba021af56111 | -8.53603 | -54.77382 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1c08fb05-08ca-30f4-ac08-adea2290a575 | -8.56579 | -54.76157 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bbfe92af-eb5e-3e97-bf45-c3b3e48e20a5 | -8.54159 | -54.74525 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28299e5a-cf06-33b1-b437-268c1259549b | -8.58767 | -54.75446 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46015077-3da1-3ed6-bdd4-fb878e28852e | -12.83184 | -48.41827 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51078a22-f4b2-35a2-986a-34557888e37b | -10.76689 | -42.08883 | 2026-08-19 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7c32fb0c-f601-32eb-a72a-6ded13941058 | -8.49479 | -54.86053 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7edcb4fc-b86f-32a3-9233-5e8eaafbdfa1 | -11.10878 | -47.27201 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 241f9ac2-6f94-3a52-b787-0fb932a65ece | -8.54819 | -54.74646 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1865b289-dd0f-3ac4-b448-b41d0f02ce94 | -8.35539 | -45.97709 | 2026-08-19 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 06a0894e-98a5-3c12-9c04-2e163fd5ee74 | -8.10441 | -51.65589 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b912d673-11e8-3901-a7af-1c9172ec546a | -8.58113 | -54.75292 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84d0876a-db70-3613-9e6a-b9d9d07be91d | -11.19796 | -54.02221 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b80b728-a450-3cd2-b63f-249a2be0b79a | -8.55142 | -54.7651 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1f868e24-7703-3187-ab75-9f4fc8311b4c | -7.45506 | -45.14054 | 2026-08-19 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81d58622-db81-3928-9d9b-fe2a8bda87d0 | -8.57436 | -54.68181 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28432cfd-b23e-34ac-b7b8-62a6d19b86fa | -8.58151 | -54.77113 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dac57d58-ae18-3e49-a34a-1d5f9fbb8cbb | -9.1182 | -46.04223 | 2026-08-19 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ea5c016-e1fd-3061-8656-b0b8468d673d | -13.41166 | -43.86713 | 2026-08-19 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed334fa1-f2ff-31e3-a374-4d9ccbb02574 | -8.58035 | -54.77694 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a24390c2-28ef-3d06-bdb7-39d870ff26be | -8.55667 | -47.40818 | 2026-08-19 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59fb7756-d1b0-3974-85b9-47955ebd132a | -11.40851 | -47.23554 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94a9b78c-3e46-3f2b-9f2d-ef7500d0dd1f | -8.54051 | -54.75083 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6555273b-7fde-378a-abb3-9b163bc2a90d | -6.33846 | -54.89748 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cb304e4-0768-3b32-b15c-4e434ed32797 | -12.79334 | -48.42945 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8a013f5-8e5e-305a-878d-49d56014deb6 | -8.57117 | -54.69832 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e62a3b9c-0935-3f80-9f9e-9f53b2c68b50 | -11.69642 | -54.56217 | 2026-08-19 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
