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
| 76f38b5c-6def-3a00-a90a-1262a03f69dd | -3.48261 | -48.94626 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0097b60c-a47d-3e29-8463-e7194f3d4c18 | -5.65532 | -51.26916 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 162cc28c-939c-3665-9469-5166cbe02cad | -5.9919 | -44.74024 | 2025-09-05 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24354902-67a9-3137-b574-e851e4747dda | -5.73105 | -45.36227 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 37f4309b-88cd-34f1-8f9f-7a5f729f0342 | -5.10671 | -56.14372 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45e51f58-ad49-3c32-b8de-615eaa87a5dd | -2.78333 | -49.62265 | 2025-09-05 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ecd7201-0238-3866-b1ac-e951186078ee | -2.95378 | -51.66455 | 2025-09-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5c92040-ab40-3d1e-a577-cb1ae8b60a19 | -3.02599 | -49.43269 | 2025-09-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c431cc62-023f-37d7-8262-68e86f0b8639 | -5.10447 | -56.13556 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 558d0a3f-5863-3900-b090-918e3b3613ff | -5.55593 | -46.19327 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dbf04424-3cd4-32f4-aafa-351f0edfd452 | -3.32909 | -54.91382 | 2025-09-05 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d6948b5-c88b-344f-90ae-5d42abbc2766 | -5.72738 | -49.28817 | 2025-09-05 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 296eac98-c68c-365b-95ad-c979ba5f2d10 | -5.21033 | -43.70182 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 722ccb0d-ea46-38dc-9875-845812d474f4 | -6.9078 | -45.18468 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f656be-f8c6-3bc0-9b33-fb2f2ccbf290 | -2.38036 | -47.62806 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec085cb6-bbd3-3c97-812f-5a44ff71c41c | -6.02806 | -43.69666 | 2025-09-05 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f758476-e883-34f6-b6a3-e1a021273743 | -5.56082 | -46.19397 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 931daefa-a5cf-3ed2-979a-0774c9578491 | -6.00172 | -46.68731 | 2025-09-05 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17732999-32d7-3030-9604-c4c44fd195a7 | -3.73685 | -53.73378 | 2025-09-05 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fb7d855-b0e0-3223-be66-543a34557356 | -3.81455 | -48.95192 | 2025-09-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f3aee83-6a6f-30fa-84ee-52bcb9a8de51 | -6.59684 | -44.5606 | 2025-09-05 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c03ddd64-6a53-38e8-be6f-9b071f504d51 | -6.59221 | -44.5531 | 2025-09-05 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| bf5a8633-7870-3cf4-b5f8-4f431b91c305 | -4.93471 | -55.81639 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aee0ee84-b0fa-3e64-ab60-196343a932f0 | -6.25209 | -46.11744 | 2025-09-05 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5104069-1deb-3333-b2b6-b2c14610943d | -2.43002 | -49.30612 | 2025-09-05 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de798715-1c1c-3f37-bd9a-ef198acd7a34 | -6.34925 | -47.09579 | 2025-09-05 04:55:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cecdce52-a959-3e7a-a38f-f8eacb02f94d | -7.08069 | -43.87424 | 2025-09-05 04:55:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 579b74f7-bc9a-37d3-b02d-96aafc4118d7 | -7.08123 | -43.87008 | 2025-09-05 04:55:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdfc0644-acb3-3c5d-ad31-5394e154ec37 | -3.67964 | -49.02139 | 2025-09-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3f09be9-6839-3790-8e42-9eeafccdc625 | -4.4955 | -56.2095 | 2025-09-05 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c607690-10cb-3fa3-9b07-44794f741bfe | -5.43383 | -42.85767 | 2025-09-05 04:55:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b56dc6b9-aa51-326c-82c9-3ea20f997028 | -6.04987 | -45.99809 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5969fb18-c78d-3db7-a7f3-f805628dec4d | -5.10792 | -56.13612 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df562249-a98d-34e9-836e-274aefda798c | -2.76743 | -49.19709 | 2025-09-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65bd6981-2078-3d4e-98a6-a7de187cbb22 | -6.17251 | -47.28428 | 2025-09-05 04:55:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28d394a9-997c-33de-b592-21c681564dac | -4.48641 | -47.67893 | 2025-09-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e21cf5d0-d582-3f19-8f9a-f94e9ccf1e39 | -5.62821 | -45.73362 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56f65db1-1739-315c-92ac-98734ca26baa | -4.89439 | -49.96591 | 2025-09-05 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c5fd4e4-0bf9-3935-b6f4-76b3c6932afe | -5.77561 | -47.21488 | 2025-09-05 04:55:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c8abdd9-bce4-3ba6-9b1c-1735e9d5c0a9 | -6.04488 | -45.99733 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7c33d2f-3b84-355a-850d-fd048ba4506a | -5.88176 | -45.57396 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91add213-fcb5-3d54-adff-212c67f80838 | -6.25123 | -43.27975 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 49186a9c-15da-37f9-a87a-d59a2c170bc4 | -6.90634 | -43.80891 | 2025-09-05 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c726a66-1b0e-35fe-93a5-a564594b90b8 | -5.98797 | -49.23764 | 2025-09-05 04:55:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d49626a-2fc7-3d1c-a819-88c0af2a7db6 | -3.21786 | -50.91451 | 2025-09-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a404184b-b24d-33db-b7d4-c81fecb82011 | -6.88774 | -45.55407 | 2025-09-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7380c6a1-76df-3a34-a298-6d7d5a802672 | -5.26924 | -55.9608 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a72a3a2c-f12f-3e0a-af59-beaab7595a5d | -5.98697 | -44.73593 | 2025-09-05 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf1440e1-6daa-33e7-98a1-91c0b13745fb | -6.23015 | -42.44533 | 2025-09-05 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 91a45ed4-c0e1-30cd-bbcc-d63611c59a86 | -6.21217 | -43.56397 | 2025-09-05 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35081420-8389-3c06-9d71-2e8538da9911 | -2.34767 | -47.58818 | 2025-09-05 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5146e710-23e7-3b91-89c8-d9030758d0d6 | -5.20512 | -43.69702 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87ca756d-0323-35f8-a1cd-a53045bf1885 | -4.06906 | -48.0355 | 2025-09-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15a576bc-ac93-38fe-80ce-1ea3f1ab75ce | -3.23698 | -50.04651 | 2025-09-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 960458fd-2bf2-3d02-bd97-c677b4ad4da4 | -4.27446 | -48.19198 | 2025-09-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b271477-acf8-342d-9629-9cf38e9c8768 | -5.59604 | -51.94577 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c1994c-15ba-34ce-a34a-7e4aaa6d4eac | -5.5486 | -43.77969 | 2025-09-05 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 77b58709-8dcc-3d6f-9e48-3252c8cffe10 | -5.53697 | -50.89117 | 2025-09-05 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04f08544-b969-3b62-9225-9f1f7471e774 | 1.12421 | -52.59064 | 2025-09-05 04:55:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 312bc759-17e2-3df6-9806-b987213c1259 | -6.81352 | -45.6584 | 2025-09-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 679f3565-b9fd-314c-bd44-59da932acf39 | -5.99196 | -49.23824 | 2025-09-05 04:55:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1064211b-7ec0-3757-991f-53109444d959 | -5.87846 | -45.57706 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 693c819d-9829-3205-aae7-f1055424cc52 | -2.55142 | -47.72676 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| badbc6a4-0182-386a-b19e-d30f28a457c8 | -4.88838 | -41.76476 | 2025-09-05 04:55:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 67f8e948-7972-3937-91f2-8c28c5a2ae50 | -4.30871 | -48.07918 | 2025-09-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe2b846a-19ee-326c-994c-5953edba9457 | -5.17216 | -45.45189 | 2025-09-05 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3399b43-d301-3061-a620-718cc3c10189 | -6.89463 | -45.18737 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7852d797-cb3c-3a19-8cce-a38375ace15f | -5.05986 | -43.87304 | 2025-09-05 04:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3017fd7-bea1-34cb-a892-d0b745d1637f | -4.16209 | -56.13557 | 2025-09-05 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16ebccd4-729c-3091-9ca1-a8399d74cbef | -3.56226 | -52.70456 | 2025-09-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c33bd8a1-6a7f-3f8e-9f81-e70c2dcedb17 | -6.59123 | -44.56026 | 2025-09-05 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 4ae0bef4-0eb1-3b77-9376-8e2a6bba38ea | -6.21509 | -43.54275 | 2025-09-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1036b2a-a3b8-3f1b-aeed-582862f86a7e | -6.25009 | -43.28802 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d4e344da-2f41-3b16-a382-c9d15b490ff8 | -5.30987 | -55.86052 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1677b1ce-5fb0-35a1-9a36-549cbb503ec2 | -5.60192 | -45.02745 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 507b89fb-42db-3cba-9788-49134b4fc970 | -6.26899 | -43.50187 | 2025-09-05 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b945f6c8-64ac-37a2-8e49-b7308ec87a4c | -6.23285 | -42.44846 | 2025-09-05 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3dcf09bf-59c3-38a6-bebd-0bd2290b590b | -5.54916 | -43.77568 | 2025-09-05 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6594eb34-ae35-3dcf-96ae-9fe0a02b802d | -4.06848 | -48.03937 | 2025-09-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bc3a634-8986-36df-9e66-31ae31fd9edc | -6.16319 | -44.20915 | 2025-09-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a7805b7-72b4-3eba-ac65-fba15a688c2b | -6.22794 | -45.63983 | 2025-09-05 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a4d33f8-3024-363a-b1ac-534622d842c5 | -3.43324 | -52.79163 | 2025-09-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdef09a4-2ccf-3b26-85b6-dd2309d82dcd | -5.02442 | -56.11115 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06dc0a9a-1e99-3935-8ebb-ef4ccb93bd05 | -5.77489 | -45.27817 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24be4644-94b8-34aa-bd00-68518e00ed18 | -5.0945 | -56.15342 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55872b91-d420-331d-816a-ba2eef6c6fc6 | -2.92811 | -54.22964 | 2025-09-05 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 185c510c-3ba6-3a13-a9b5-2133e7ac8ab1 | -6.11406 | -44.14803 | 2025-09-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2773f0be-de03-3f02-bac0-293f1d49362d | -5.11016 | -56.14428 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 885d400f-740b-3997-ba32-c2f21d5d5869 | -2.51177 | -51.82431 | 2025-09-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7818a8c0-624a-3226-a540-0ecc426cdc8d | -6.61691 | -43.97661 | 2025-09-05 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db53e3a2-8e64-3612-84b0-05a40798df22 | -4.93529 | -55.81274 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4df8b76b-66f9-3932-ba87-6c41ab76e6ac | -5.10142 | -56.15455 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 167aeec9-252d-3b83-8dce-dc842f1f4518 | -6.54535 | -43.72641 | 2025-09-05 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 009ca71b-1085-3c72-ae74-d283a2daf360 | -7.16181 | -43.89092 | 2025-09-05 04:55:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5494878-8102-3139-8d45-6740d12a3546 | -6.11356 | -44.15166 | 2025-09-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01c45b79-c1df-33dd-9ff3-8882878a59e0 | -4.61313 | -55.74388 | 2025-09-05 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a92fb8f-61c8-3af8-91e8-47ca6024bfb8 | -6.9044 | -45.1957 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 926f0f56-fc86-3177-96d3-34ca9e9dae73 | -2.89841 | -51.47928 | 2025-09-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4b037a9-1f1f-36d1-826e-e5269f36fbd7 | -6.67075 | -48.39704 | 2025-09-05 04:55:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78b9d370-ecb4-36e0-b3f2-4047a1a7ec72 | -5.88398 | -45.57502 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README43.md)
