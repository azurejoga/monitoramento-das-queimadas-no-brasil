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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bdd7b05-d743-33a3-9e77-207009c5dc7a | -4.79555 | -42.58747 | 2026-10-05 18:19:00 | AQUA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 285.9 |
| 0e010f95-4c12-3e53-bc2b-431307c16f02 | -4.79365 | -42.5742 | 2026-10-05 18:19:00 | AQUA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 8876fe18-ccde-3632-86b2-7dca0e9d76b4 | -5.12379 | -43.99483 | 2026-10-05 18:19:00 | AQUA_M-T | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 7193781e-50e3-3a04-9872-22bce0f580d8 | -5.97221 | -41.36391 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1617.6 |
| 75a9a208-e080-3d0c-aaf4-d59383dc7c7b | -11.81056 | -41.60093 | 2026-10-05 18:19:00 | AQUA_M-T | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| a9daf2f0-e90d-3a35-a084-efc3a228ac55 | -6.32723 | -43.34406 | 2026-10-05 18:19:00 | AQUA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| ab44c869-2c80-3b19-a5bb-ea8f96bb8086 | -4.90954 | -41.74253 | 2026-10-05 18:19:00 | AQUA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 285038c9-d4c4-31ff-bb65-73ef67e41f69 | -3.82136 | -41.79766 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| dc86b355-0c17-3263-be10-e64de1524511 | -11.65021 | -43.62371 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 68c9aff9-282e-38a6-924a-40f59a337320 | -3.54661 | -39.88959 | 2026-10-05 18:19:00 | AQUA_M-T | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 11c8d514-9846-3c80-ae44-83fe03bda4a6 | -6.55007 | -39.51857 | 2026-10-05 18:19:00 | AQUA_M-T | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 6819694a-3a2a-3aaa-b4a7-62900d99ed96 | -3.48744 | -43.25824 | 2026-10-05 18:19:00 | AQUA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| bec74010-b7e9-3303-98bf-db372e7eb94a | -3.82299 | -41.80908 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| fc086aa3-bb10-37ed-b08c-bb111023caae | -7.0829 | -40.08782 | 2026-10-05 18:19:00 | AQUA_M-T | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 0f4a397a-b8a4-3372-8805-9617c87ec228 | -3.47445 | -43.24568 | 2026-10-05 18:19:00 | AQUA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 117fe7ea-14c6-34c2-ae6e-2d5cab626adf | -6.62869 | -41.80507 | 2026-10-05 18:19:00 | AQUA_M-T | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 7daa3960-2f89-3636-aa65-b504ba23c37f | -8.09267 | -40.36366 | 2026-10-05 18:19:00 | AQUA_M-T | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 8b2b9840-9b38-3e26-92b5-ead1743fc221 | -9.22108 | -40.35378 | 2026-10-05 18:19:00 | AQUA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 14.8 |
| dc953b0f-f729-3dd3-a08a-669fdd9e07cf | -4.84886 | -41.81662 | 2026-10-05 18:19:00 | AQUA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| f119fe53-afea-3f25-adf8-b3301c47a486 | -9.81834 | -44.79246 | 2026-10-05 18:19:00 | AQUA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 53b1688c-76eb-387b-929b-eed86145096d | -8.36867 | -36.30823 | 2026-10-05 18:19:00 | AQUA_M-T | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0ce156c4-52ed-3b97-8c3a-521d7c75fa79 | -3.45376 | -43.02225 | 2026-10-05 18:19:00 | AQUA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 3e43d43e-b417-350d-8bea-d9f3aad63518 | -8.70913 | -35.7485 | 2026-10-05 18:19:00 | AQUA_M-T | JAQUEIRA | PERNAMBUCO | Brasil | 2607950 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| b702bcb9-04a9-3e2b-a995-320ab5400517 | -6.88035 | -43.68261 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ee557f86-90c5-349d-b09e-ed2a3e4cddb5 | -6.82235 | -39.29964 | 2026-10-05 18:19:00 | AQUA_M-T | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 8bfedcb6-5aca-31de-8420-1ee0d155a23a | -7.36935 | -35.21697 | 2026-10-05 18:19:00 | AQUA_M-T | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 6bacef2e-1d26-3ef0-9401-2197714379c5 | -3.77028 | -39.84433 | 2026-10-05 18:19:00 | AQUA_M-T | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 7ff611c5-a571-340a-8ae7-7de64bfd298e | -8.00738 | -42.93638 | 2026-10-05 18:19:00 | AQUA_M-T | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 7b8ecf4f-03b2-3459-95b2-fab22ee04551 | -11.68169 | -43.66205 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 6614b104-2998-33d6-a8d0-2e23e9be9fe3 | -6.81206 | -39.29181 | 2026-10-05 18:19:00 | AQUA_M-T | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 52880467-e4a2-347d-99ac-f60a3d5ded61 | -5.48449 | -39.55961 | 2026-10-05 18:19:00 | AQUA_M-T | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 2ea48cb2-1da4-3887-98cb-e5f12b094b71 | -11.66163 | -43.61484 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 923c8024-36fd-3b94-ab8c-895eeab56dcc | -3.10899 | -41.83519 | 2026-10-05 18:19:00 | AQUA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 85f64997-e74d-3ec0-8859-8c86bb804a36 | -3.79486 | -41.76085 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 34f5ce5d-aec9-3119-ab35-2c5400d5601b | -6.85267 | -41.80518 | 2026-10-05 18:19:00 | AQUA_M-T | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 501886d9-8a9b-3526-ab8a-48504b7e2bc2 | -5.11672 | -42.64083 | 2026-10-05 18:19:00 | AQUA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 0e991399-c20f-3a82-8c0a-c86313cb14fb | -6.89241 | -43.68085 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 282.8 |
| d9259868-d64a-3ac4-910b-f63d905655cd | -4.95082 | -42.72493 | 2026-10-05 18:19:00 | AQUA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e586a01f-52e2-3b41-8cb2-cbd23d5d5bbe | -4.26172 | -42.30225 | 2026-10-05 18:19:00 | AQUA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 25681ff4-2394-34db-a2d2-e0f16550bb1a | -5.5219 | -41.01797 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 22b705d0-0fd7-3cce-8b20-8bfb91ce0fdd | -3.91738 | -43.94742 | 2026-10-05 18:19:00 | AQUA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| e3e919bf-d48a-304f-a1f7-fbd6dc426f0b | -6.15621 | -39.412 | 2026-10-05 18:19:00 | AQUA_M-T | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7d4d208a-d684-33ba-8b14-6f3dfc5f817b | -3.29427 | -42.25982 | 2026-10-05 18:19:00 | AQUA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 35fa60f9-e116-3946-86d1-b18527499344 | -7.86406 | -44.1699 | 2026-10-05 18:19:00 | AQUA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.7 |
| d9c392e7-612f-3f73-a8fe-d14dcbdf6d3b | -3.1188 | -41.83376 | 2026-10-05 18:19:00 | AQUA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| f573fd7a-1ff1-3189-958f-5d26f864b5e5 | -4.50625 | -42.07309 | 2026-10-05 18:19:00 | AQUA_M-T | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 3dec6586-d9e4-3e8a-b8b5-343ccb1b37bd | -3.74305 | -39.53593 | 2026-10-05 18:19:00 | AQUA_M-T | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| e3cf8504-391c-364e-9a0d-d6dc5031769e | -3.90525 | -41.5962 | 2026-10-05 18:19:00 | AQUA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 6bcbd7ad-3c95-3551-ae12-a7374ec798eb | -5.95255 | -41.37232 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| d63744b6-435b-3615-96df-b663a39d95f8 | -6.93382 | -43.66823 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 8aebb399-c548-3b91-b361-4e7a88e8ff7b | -8.00517 | -42.9206 | 2026-10-05 18:19:00 | AQUA_M-T | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| c4d1f9b6-7fa1-354d-91b8-9c937664f1a7 | -6.69908 | -45.23973 | 2026-10-05 18:19:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 13818fab-95ec-3492-9dd0-b6105cf1ae97 | -5.98376 | -41.37403 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 98abd842-dea5-31ac-97e6-91ab934baa0a | -5.9607 | -41.35391 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| bc3dad0b-6cb2-3bbb-93de-995218cbb6fe | -6.08209 | -43.88152 | 2026-10-05 18:19:00 | AQUA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f633e6b5-f9b7-3556-8462-02ce73aa9f33 | -10.52955 | -46.0822 | 2026-10-05 18:19:00 | AQUA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 242.9 |
| f08c2687-fef6-3071-844c-2d3c5faa4645 | -3.12043 | -41.84491 | 2026-10-05 18:19:00 | AQUA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| a735de6f-2228-322e-b95e-a045ba792701 | -11.69477 | -43.66045 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 6004e7a9-9575-3356-8542-f0d071cacf30 | -11.12497 | -45.97398 | 2026-10-05 18:19:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 331.9 |
| d18620ce-3144-3bf6-9394-4c198337f171 | -8.33719 | -37.27081 | 2026-10-05 18:19:00 | AQUA_M-T | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| edd1fb9f-b57e-3f15-9cf8-a2761ecfea62 | -6.10003 | -43.52728 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| cc2bd0a7-122b-33e8-8cd7-b1acc7c81029 | -4.24863 | -40.01486 | 2026-10-05 18:19:00 | AQUA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 2fe48963-16a4-3a27-a41d-a8f2515afd16 | -6.69243 | -45.24532 | 2026-10-05 18:19:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 460f285d-d128-365e-8263-7fdb988ff4cb | -5.47187 | -41.24332 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 9d344f55-da96-3d11-b075-2038d6561f1a | -5.99237 | -43.81258 | 2026-10-05 18:19:00 | AQUA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ba3d6a4e-4e4a-3f51-b1d6-1cc3406f32d9 | -5.48583 | -39.56877 | 2026-10-05 18:19:00 | AQUA_M-T | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 7b8ecb2a-8038-32e0-81c7-95d062baca88 | -6.86309 | -38.68179 | 2026-10-05 18:19:00 | AQUA_M-T | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 945ea6a5-31a7-3dad-9937-30ddfa5e1c82 | -7.16044 | -38.44671 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 9b34ff6f-1d1d-3dac-a752-883754b80136 | -7.54154 | -40.13397 | 2026-10-05 18:19:00 | AQUA_M-T | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 16.9 |
| b738ffd0-9b68-3e7c-be29-bf49bbd6a8a9 | -8.53013 | -36.5199 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e28f847a-7717-37ef-a1ed-b459aa9cde24 | -6.90447 | -43.67913 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 2e739d91-6e98-3401-b9f5-2786dfa59a7b | -3.91184 | -41.57285 | 2026-10-05 18:19:00 | AQUA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 51552d39-d799-3686-bb24-6f789f10daa6 | -6.77634 | -40.12663 | 2026-10-05 18:19:00 | AQUA_M-T | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 7f02ecaf-3888-31f9-8061-a48bf096c4ac | -3.92218 | -43.95192 | 2026-10-05 18:19:00 | AQUA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b445d0ac-66c3-3318-a485-7ff0e1cf3801 | -6.49766 | -43.23335 | 2026-10-05 18:19:00 | AQUA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 2953919d-1f0a-321b-9cdf-da92f0bd7773 | -5.13598 | -48.12573 | 2026-10-05 18:19:00 | AQUA_M-T | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 4dd35c24-d467-378b-bf4f-23940ec0f048 | -6.18508 | -40.50107 | 2026-10-05 18:19:00 | AQUA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| cead7804-ae74-3548-be4c-569ce7d571e6 | -4.56661 | -43.72972 | 2026-10-05 18:19:00 | AQUA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 0a41ca12-1613-3f0c-b083-73666608ffd0 | -5.7347 | -43.37286 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 48c43367-3ddb-3882-a8bf-999948e51b33 | -5.52347 | -41.02877 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| e280de15-3670-3ec2-9fd2-9839b8ca86a2 | -6.43375 | -43.45658 | 2026-10-05 18:19:00 | AQUA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 847e069b-b235-3baf-98c2-99f591772bb9 | -7.482 | -42.80178 | 2026-10-05 18:19:00 | AQUA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 51cd9af5-573d-37ca-a832-47084856b4a2 | -7.83347 | -45.30813 | 2026-10-05 18:19:00 | AQUA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| b2038227-a887-3284-a69c-58e0c42380d7 | -11.85886 | -43.20701 | 2026-10-05 18:19:00 | AQUA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 21.4 |
| b807aa4e-cb12-3231-84db-d01b122051fb | -4.94352 | -42.71912 | 2026-10-05 18:19:00 | AQUA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 432919fd-6774-32fc-9dc7-7d4fbca3c2be | -4.85014 | -40.40413 | 2026-10-05 18:19:00 | AQUA_M-T | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 41b73a9e-019d-36c2-87fb-668b63e40e59 | -4.8537 | -42.20605 | 2026-10-05 18:19:00 | AQUA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 62772c13-7f28-33cd-8074-5790e7712622 | -6.71592 | -45.26134 | 2026-10-05 18:19:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 526.8 |
| 3453b266-0d7a-3d74-827b-8ee6c942bf25 | -10.95104 | -40.29573 | 2026-10-05 18:19:00 | AQUA_M-T | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 2b29d0bc-ffb1-37a1-ab05-92d8d96546a0 | -11.65284 | -43.64426 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 23fdcc27-14d0-304e-b851-6476f853b9e3 | -5.47559 | -41.2477 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 315db28e-a098-3994-8695-e4d7144ff45b | -5.12169 | -42.63292 | 2026-10-05 18:19:00 | AQUA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cad6d046-61a3-3d8e-94cd-1f30e0838dc2 | -3.91343 | -41.58377 | 2026-10-05 18:19:00 | AQUA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 5798f1f5-1a0a-334e-86e3-a4a141712f18 | -7.64235 | -40.43627 | 2026-10-05 18:19:00 | AQUA_M-T | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| fe28b8fc-8d67-3281-bfa0-87af787ad18b | -3.29602 | -42.27172 | 2026-10-05 18:19:00 | AQUA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8e71d44f-3479-323f-bff9-698dad238b29 | -5.98982 | -43.70823 | 2026-10-05 18:19:00 | AQUA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7262ba98-769d-3e38-849e-6e4771ccf4a2 | -4.92122 | -41.75282 | 2026-10-05 18:19:00 | AQUA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 8b9424a3-5f68-31ea-b413-abb3154a34d2 | -3.75486 | -39.53683 | 2026-10-05 18:19:00 | AQUA_M-T | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 24bbff56-969a-381e-9de8-68355831ac4f | -6.14768 | -38.41366 | 2026-10-05 18:19:00 | AQUA_M-T | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 8ead956a-4f7e-303a-bc74-4f0377890406 | -6.47935 | -43.88753 | 2026-10-05 18:19:00 | AQUA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |


[Clique aqui para ver as próximas entradas](README161.md)
