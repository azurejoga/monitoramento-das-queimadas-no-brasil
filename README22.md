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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87fcbce5-c55a-3983-8e13-9f11408b0983 | -6.1173 | -44.14132 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19c7ebfe-8a45-346c-b663-77644f8b2a43 | -6.2973 | -43.49623 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a808b92-b402-3747-bee8-5531ff4af846 | -5.73148 | -49.29195 | 2025-09-05 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 75a628c0-7a48-3ac7-b984-d70efd9e348f | -6.68346 | -44.80351 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60068dff-17c4-3ade-8bbb-bb351d0d229f | -6.25234 | -43.28806 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6506ebcd-7f61-3d91-8319-4468ed8af4f7 | -4.85866 | -42.54486 | 2025-09-05 04:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d1d8a0b4-e3ca-3960-943f-5a6225ce53dc | -4.15358 | -41.66436 | 2025-09-05 04:34:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50357617-1c1d-3679-9415-303610276526 | -5.72866 | -49.28774 | 2025-09-05 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5fc8939a-c057-3859-a4bb-e392c99da04c | -5.75353 | -45.53806 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96b91165-e770-3d1d-bef5-0140ce38a998 | -5.62902 | -45.73427 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4fde8183-48c1-36cb-8765-1a9603f6716b | -4.17483 | -42.02888 | 2025-09-05 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ccd0179d-2bd1-3d5e-886b-10141d3620ea | -6.21729 | -42.45289 | 2025-09-05 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24e2660d-7edc-314b-b765-7f3189ce7235 | -6.31884 | -44.42806 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2774226-21d0-323b-8faa-131d1f36eedc | -4.56799 | -40.34621 | 2025-09-05 04:34:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf951456-b4dc-351e-923b-64e99f259a28 | -6.88981 | -45.55272 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b8ce49a-7f92-3d36-b733-47b026c23ee5 | -6.05186 | -46.00131 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a64220f-6ea8-3a25-9e71-3258b58483d0 | -4.90091 | -41.75757 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0e867474-2555-340e-b981-98296375ab07 | -2.94449 | -48.59442 | 2025-09-05 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| df1a70bc-e688-3882-8b9d-bc12f7817e77 | -6.11595 | -44.15007 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f2d61c9-5643-364a-b905-6f627ca098e5 | -7.66074 | -46.26818 | 2025-09-05 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21d96f35-454b-310a-a7da-080762fb2fb0 | -5.89794 | -44.17723 | 2025-09-05 04:34:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faf7b898-66bf-3bc0-9a83-9f5aae0fba73 | -7.71147 | -45.16943 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca1ca22e-ce83-3bbe-bbe1-1f3d6265e751 | -6.15485 | -44.23427 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89f1ca2e-4494-32f5-a1de-6b4d17a8b3b3 | -7.95448 | -44.93974 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d945c60a-a3b3-3c09-b062-2244d0c6e24f | -6.26944 | -53.54493 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b922ce4d-4f70-3eec-bebb-9f0419093cf7 | -8.00174 | -44.77203 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d554e5b-48e3-3f8d-98fc-b8e55bc620f1 | -7.98829 | -44.51736 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da0356e9-90df-3835-a6fe-e798d37f6152 | -6.16247 | -44.20889 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c0933b2-91fc-3bdb-9a1d-912e47d85df1 | -6.15998 | -43.18745 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb5f4786-efb1-3fc5-a57f-614b6b43fabc | -5.09881 | -56.12413 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1001679-a17a-3c76-959e-dde4f36b648d | -5.7987 | -45.62474 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35ea72ac-6b9f-3e0c-943b-747e41c39fa0 | -5.98419 | -42.99427 | 2025-09-05 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6dae0534-5b77-3a6c-a3af-79048b05cc0e | -6.01893 | -43.70051 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e2fb15c-04a3-37cd-94ef-2d7326cc9ba9 | -6.2734 | -43.49759 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daa4973e-571f-3b01-bcdb-3d72dac4b38f | -6.00069 | -46.69035 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a1bf3ed-a7cb-3c34-a356-0ef8764a2da6 | -6.54703 | -42.9418 | 2025-09-05 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b58cd4b5-3f95-3324-96df-0dc67edd4393 | -5.64928 | -43.13232 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 892fc475-7577-3908-91ea-934146196f4c | -7.71567 | -45.16587 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f757ce13-9dc9-3b40-8f04-60b45eb37a50 | -5.54689 | -43.06902 | 2025-09-05 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2654baf7-323d-3a9a-a667-cc5b8fb4632f | -7.99807 | -44.77146 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b568441-5d8a-39dc-86e7-3e841b133ffd | -5.72807 | -49.2914 | 2025-09-05 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e9d9f8cf-d499-39f1-b839-e993b9617efd | -6.38261 | -43.01192 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 770ff4d5-c847-32dd-9ad9-92d0db0353ea | -6.2351 | -42.64126 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d856886b-ba6e-3b59-8662-739b1c0ea6ff | -6.47187 | -53.40121 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9248915a-f1ab-3d8c-8d96-f0830a22bc09 | -5.11112 | -56.14549 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40b12052-3cb9-37d8-91ab-36c8ad60a332 | -6.37941 | -43.00611 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e7acfc5-82c8-31fc-8a5b-6bb4280a1ea4 | -3.33331 | -43.52399 | 2025-09-05 04:34:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 865f7438-d39d-3875-94fe-625d67da889f | -7.30377 | -44.06924 | 2025-09-05 04:34:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9864f8f4-953a-34f2-bed8-fb3157f92697 | -7.9795 | -44.5252 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8864d972-d95d-3db9-9a2f-2c805201b969 | -4.79249 | -43.81446 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ca2d8165-4334-3d4a-b726-a3b437dc61ad | -6.21272 | -43.56157 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 438e7903-be25-3475-a15e-6d2aa2bb4b29 | -5.92556 | -43.0203 | 2025-09-05 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3a99bd68-5ca3-3c0e-a895-acd975c75c99 | -5.21113 | -43.69585 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3b99444-e303-3498-a6ea-2dab4833e94f | -6.00456 | -46.66556 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eac8abb-6b72-3ebb-be6b-ee264107e17d | -3.67588 | -49.02359 | 2025-09-05 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d28ff336-a4ae-3b14-812c-5b13b0e06f9e | -5.65404 | -46.42271 | 2025-09-05 04:34:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a61ec28-86c4-328c-ad4f-25a10571f590 | -6.30133 | -43.58231 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9e338cb-e5b9-3c07-a520-f9339ae75a30 | -6.20633 | -43.40697 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3e0ef8d-59ee-3b1a-b305-104ae20cc9e7 | -5.69402 | -45.17616 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a8a6deb-7529-34ef-8c26-4bd28b86927b | -4.30822 | -48.09716 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fbff784-332e-3319-9f92-63291eff05b2 | -6.0513 | -46.00497 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1eb9cfa-a369-3b44-be1d-a097364c7697 | -5.90133 | -43.36491 | 2025-09-05 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| beefdde1-515e-39f0-ba36-e1f0e15e93b0 | -7.36099 | -44.32473 | 2025-09-05 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20fa19bc-3d3d-3656-be4a-a08ac45d9e2f | -4.31098 | -48.07967 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dacd2c8-018b-3176-94ef-b79897f14840 | -5.5508 | -43.0697 | 2025-09-05 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa97e9b9-c61b-3e3b-a814-ad6f57ca6163 | -5.77166 | -44.86026 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54b6b81e-d1f3-358c-aa27-a899bf4cab97 | -6.26574 | -53.43916 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67fa0332-506f-3526-a92f-cfdfd7994486 | -6.25381 | -43.27847 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 64845411-35f8-3c0b-bc1f-10e8ebe04685 | -3.49224 | -48.94952 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aadc9d33-9f5c-33e0-8f8d-c6429e239df4 | -5.94142 | -43.02251 | 2025-09-05 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f78f1d5d-30c6-3fb5-9edf-56732648f0ae | -6.29268 | -43.50065 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b544046-9245-366f-9e2a-6bc9f502ce1c | -6.59818 | -44.55361 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6851ccad-d86b-3e5e-9138-3c94d38b9456 | -6.78545 | -44.44767 | 2025-09-05 04:34:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02bec13e-96f7-3959-82c9-feaa32c919ad | -5.94538 | -43.0231 | 2025-09-05 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 17bdc506-e7e8-33f1-9056-c9da6ddfe6e8 | -6.0763 | -43.29081 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0e4e8287-fc6b-31de-8e38-ede0d3ec8400 | -7.58355 | -44.67411 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d2f736b2-e1b5-32c9-817e-0666f457c12b | -6.67228 | -48.40846 | 2025-09-05 04:34:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88316f07-b0b8-3950-822f-f715df3408ad | -5.96861 | -44.74642 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5ca3d58-efbc-33ad-aefa-4160d2e8a334 | -3.22086 | -50.91471 | 2025-09-05 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 656a4719-a959-3b8c-b7fc-c4447907565e | -6.24844 | -43.28745 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b93cfe1f-b60b-3673-8217-0f79a6ddd584 | -3.67991 | -49.02043 | 2025-09-05 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d14ac00-6c7e-3d3c-bdba-d5f23f3e2559 | -6.24886 | -43.31485 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec80cbda-8b00-3793-b2f4-0d7ef5ea1ef2 | -7.95689 | -44.94857 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15328ba2-7a10-36d1-a03f-f43f13269674 | -3.97047 | -48.1337 | 2025-09-05 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a6f8a1f-8c2e-315e-8bda-ed742e254642 | -4.8959 | -41.73289 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 210b1983-1e66-3d26-8219-2b3d4f081ec5 | -6.20304 | -45.05193 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcaf77b6-9a96-3b4d-9ddc-6fe4439dcdab | -5.81922 | -47.78025 | 2025-09-05 04:34:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e95ea9e0-de21-3e45-9293-295700b43562 | -2.90031 | -51.47917 | 2025-09-05 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 725c9b38-4548-3daa-9b91-6c4781b3f1a8 | -2.37856 | -47.62955 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10ff3457-9a9f-33a5-835f-bcc00bf9fb4a | -6.2693 | -53.44373 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b05c62f3-243d-3be6-a1f6-efbae70b62f4 | -6.6877 | -49.76855 | 2025-09-05 04:34:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef456938-acac-3d62-a871-f7f6e73060ab | -6.31328 | -43.28461 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf72a873-568a-3af9-a455-74c602028b59 | -6.60921 | -43.98075 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f471be7-34dc-371a-bc95-e946dbe0a054 | -6.59365 | -44.556 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| b1730480-8b75-30a3-81e3-e9517f373baa | -6.80814 | -45.3605 | 2025-09-05 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e6ec837-f167-35cd-bce9-84d1ee827f6f | -6.12892 | -44.15469 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47e00f73-f229-3f64-8541-e42ef429e96a | -6.59062 | -44.55125 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bf19a8be-233a-3dfd-a907-25df2cfbe4d3 | -5.93746 | -43.02193 | 2025-09-05 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9af079a9-8ef5-3c66-b310-cf1865ed3e3c | -6.27125 | -42.64558 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7bb751c9-ef5b-35c3-bdd2-81ea936088c9 | -6.25171 | -45.16054 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README23.md)
