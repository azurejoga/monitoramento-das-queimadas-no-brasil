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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffca0c70-e6ed-37e9-a81d-4b8f5a93b40a | -14.4197 | -52.5413 | 2026-08-30 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 250.7 |
| bc4a3f81-0ead-3bc7-8d5a-d0215cda5b2c | -12.9216 | -45.8812 | 2026-08-30 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f0210e06-9081-3596-91f2-0569f394a61a | -11.3619 | -45.1724 | 2026-08-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 4e5d00f2-0ea0-3845-a647-e59ced7befb9 | -5.871 | -57.7715 | 2026-08-30 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4e838035-3328-3593-af79-6655175520c4 | -13.8381 | -54.0365 | 2026-08-30 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 8b0c5ab2-e4d3-3f5b-88d3-322f99e5b478 | -13.3991 | -51.461 | 2026-08-30 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 4d8a18fd-9252-3112-beea-5d6fc2745596 | -12.3811 | -48.1877 | 2026-08-30 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4c7df834-9254-3c45-bdd6-e7e1132a1a84 | -12.2281 | -50.5578 | 2026-08-30 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 151e4962-3dfe-3ee8-80fc-5981bf18a6d4 | -15.2283 | -57.6517 | 2026-08-30 14:40:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a658b79c-9d1c-3df5-84bf-6b10bdaff192 | -11.1726 | -51.2728 | 2026-08-30 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 4c5a7963-806d-39e0-a4f3-3d5325c0af5d | -12.2086 | -50.5815 | 2026-08-30 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 8fe21f8f-0320-3fa2-a2f4-9732137901de | -10.7407 | -54.0401 | 2026-08-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 24454b72-3838-3d1d-8e02-2674ffc1edab | -14.5631 | -52.0557 | 2026-08-30 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 93d65640-5457-381a-9bd6-136c4621293d | -8.5925 | -66.9564 | 2026-08-30 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e70706f1-d546-35e9-84ae-88366147b9c5 | -7.3117 | -60.6089 | 2026-08-30 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 215.5 |
| eba804f6-b660-330a-b730-5e0d72e54c07 | -11.1534 | -51.296 | 2026-08-30 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| b5a6e5f8-aa5a-335d-b20e-2cf50b763ce9 | -7.5272 | -44.3413 | 2026-08-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| c8f15ed4-3e5c-37f1-a69c-8ee42decd270 | -14.4477 | -58.4709 | 2026-08-30 14:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| cb8a433e-e70f-359c-a9d2-1d867cd6d456 | -4.9605 | -55.8226 | 2026-08-30 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| a4ee8f9b-bd9f-3a99-8ce0-44fbc3550139 | -14.2027 | -52.8432 | 2026-08-30 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 135.5 |
| bb155e4d-adb5-376d-8f54-0ebf2a83a3a5 | -10.7647 | -50.6579 | 2026-08-30 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 30e17a8a-9384-30f9-8458-4adbb17390f4 | -7.5644 | -49.5857 | 2026-08-30 14:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9aefec6c-12da-3039-a6ed-fac8ca5469cc | -9.1532 | -59.5221 | 2026-08-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| db42b589-9f8f-3445-b226-2112492c4398 | -12.0921 | -47.1812 | 2026-08-30 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 61ce72b0-4f02-3e7a-9e78-7025142ebf94 | -8.574 | -66.9569 | 2026-08-30 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 6838147e-162f-3e7d-b47a-3e172aa391bf | -7.2931 | -60.6287 | 2026-08-30 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 83b199cb-0192-3512-a4a7-7c3476eef5b1 | -7.2932 | -60.6096 | 2026-08-30 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| ff4aab0e-3b5e-3a57-bec0-3182e61d89b7 | -11.2294 | -45.099 | 2026-08-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 577be3e7-195d-39f9-af2c-008d99150d56 | -3.6216 | -60.547 | 2026-08-30 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 62da9efb-1e40-36dc-a275-936dd9ad6700 | -12.2277 | -50.5792 | 2026-08-30 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 31c5435c-6a1e-389a-890f-7197e16df2dd | -7.1001 | -42.2044 | 2026-08-30 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 117.4 |
| aeb43616-2c78-39e2-8781-7de5a4ec87bd | -4.1515 | -60.7068 | 2026-08-30 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 450c3a2e-63d4-3cdf-9dd1-11fc8a9b87b4 | -11.0057 | -49.6677 | 2026-08-30 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 24272b80-dc8b-3184-92d0-4141d514d466 | -3.6215 | -60.566 | 2026-08-30 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 38bc5a07-eeb4-36a4-a301-d2f82885ed7c | -9.1533 | -59.5027 | 2026-08-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 9015ca93-42d3-3c77-8c48-4f9946f2688a | -10.8058 | -45.3407 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7e3d7b6b-18c5-3a16-a2dc-29bdfca0ce00 | -7.991 | -46.4954 | 2026-08-30 14:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 7895a1e4-3350-3796-a666-4c3475b6fb08 | -15.4044 | -52.665 | 2026-08-30 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 4ee92588-7710-3d19-b356-19caf36b1aec | -11.2314 | -54.0164 | 2026-08-30 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 220.5 |
| 7a68cac2-e84a-33da-8225-167685ac852e | -11.2317 | -53.9958 | 2026-08-30 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.0 |
| c060a28b-9dd5-356e-8c27-421e1593c86f | -9.8925 | -60.2945 | 2026-08-30 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d2e18e99-5861-3d7d-a99e-e14dc0e43a6b | -15.228 | -57.6719 | 2026-08-30 14:50:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 252d2b3e-f1c9-3dd6-9bd0-fa9bd15f7f28 | -4.1515 | -60.7068 | 2026-08-30 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 5ece8404-9428-362c-9491-854251759f86 | -10.7867 | -45.3433 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| f817b881-9ab9-38c7-b0fc-31039ddf435d | -14.2027 | -52.8432 | 2026-08-30 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 5ba59421-397c-3649-993b-44db0ba260fb | -11.6586 | -50.4532 | 2026-08-30 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| aa08985c-672b-3c32-bf1a-9ae399519b3e | -12.2086 | -50.5815 | 2026-08-30 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 6a635187-1511-3bda-b905-d0fbc3b621b6 | -16.2735 | -42.5653 | 2026-08-30 14:50:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 219.9 |
| bc71acd8-6e3d-3449-8fa7-427c4208d187 | -9.1755 | -59.0355 | 2026-08-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d55fd016-d83c-3e9b-9b43-b9e28e2693f7 | -15.4048 | -52.6437 | 2026-08-30 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 8d87c197-da9a-3e0e-8488-f12163241552 | -14.2092 | -45.3207 | 2026-08-30 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a1717151-1ab0-3d2d-8f43-daf25af080ff | -13.856 | -54.1175 | 2026-08-30 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 137.2 |
| f56ccf61-6280-384d-9fab-12e05b04d6bf | -3.6399 | -60.5466 | 2026-08-30 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| a2a29ea0-1107-3f8d-9bfc-ce869b27f750 | -14.4842 | -52.1512 | 2026-08-30 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 35500ddf-a46c-3cdc-a9a2-829a65869921 | -13.3038 | -51.4304 | 2026-08-30 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d397f5b0-02c4-3d86-86ef-8d00c70fa243 | -9.1719 | -59.5017 | 2026-08-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 2b5f1633-61df-376e-81eb-7883104ea2bb | -13.8752 | -54.1153 | 2026-08-30 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 84ab0363-1700-37b7-a85e-a84d03c08eb1 | -11.2107 | -45.0786 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fa99cf0b-68f0-3665-9c84-29f7cd625e04 | -14.4193 | -52.5625 | 2026-08-30 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 896c1f10-161e-383d-b04d-0b25bca2c421 | -9.1662 | -60.2752 | 2026-08-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 76f78d55-e2c0-3411-84bf-35846b02e642 | -12.3811 | -48.1877 | 2026-08-30 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 3b1b7c51-c34f-3487-b3c7-d13173fcb5e3 | -8.0098 | -46.4936 | 2026-08-30 14:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9c1aaedd-4c53-3c7c-a076-b05ceb35ca53 | -10.7457 | -50.6599 | 2026-08-30 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| eceaf716-2abf-32e2-8270-d6a95fc544e7 | -7.1309 | -42.7945 | 2026-08-30 14:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| fe83b37e-7e8b-3bc3-a00e-52fb1c31aa20 | -10.7434 | -50.8302 | 2026-08-30 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 23579970-9e46-3b58-89e0-e76715c59e22 | -10.3394 | -49.9547 | 2026-08-30 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| a4ab8389-74c8-3402-a290-e9b21881e2e7 | -10.1538 | -45.6982 | 2026-08-30 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 9d0b3488-2de3-352a-9848-31c1612a0be2 | -7.3302 | -60.589 | 2026-08-30 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b5ef9097-9c49-3e50-a010-2650cf0d75e6 | -14.4004 | -52.5438 | 2026-08-30 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 689e3ea8-7df2-3e01-aa50-b9fdf07138ac | -5.8708 | -57.791 | 2026-08-30 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 88ee39bd-6b49-354e-90e7-ffc49261d034 | -5.8894 | -57.7708 | 2026-08-30 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| dd557c72-b061-3130-a43d-5880ee3c97ee | -10.8249 | -45.3382 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 15bb008d-e0b7-3e14-b044-d7cdffe16d5e | -14.4197 | -52.5413 | 2026-08-30 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 4e0a5f38-0fe2-3552-bc8e-3962e1ca2216 | -12.2083 | -50.603 | 2026-08-30 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 990249f3-b312-37c7-9a5e-2ba13cf36f1b | -14.4 | -52.565 | 2026-08-30 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 9745d29c-aaac-367a-8b2e-d07839280921 | -10.7056 | -50.8341 | 2026-08-30 14:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 9921d418-009a-3e88-b052-68f557f56e2a | -9.0536 | -60.435 | 2026-08-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 589a0a3d-f0db-3528-892f-a970679c5e46 | -10.844 | -45.3356 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a3f7b88d-1b11-36b5-b8c2-3895b91afbc9 | -3.1998 | -61.161 | 2026-08-30 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ac33e6e3-dd9c-33f3-b7e6-e17a440b3a83 | -13.8381 | -54.0365 | 2026-08-30 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 536196c1-474d-315c-871b-3fb2c064c5af | -12.3807 | -48.2099 | 2026-08-30 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 52deba5f-5f9d-3df9-a69a-dfa8589b1e73 | -9.4535 | -45.6455 | 2026-08-30 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 8aa94b5b-7f0d-3d48-8727-f10f9633ecb8 | -9.8928 | -60.2558 | 2026-08-30 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9a0c5992-96b9-3632-a37d-91c201782237 | -8.1531 | -45.5131 | 2026-08-30 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2fa0a92f-2380-3ad2-abf4-e502fac9a0e9 | -11.6205 | -50.4575 | 2026-08-30 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 859ed369-007c-3606-8f66-0294a5a2141c | -7.5272 | -44.3413 | 2026-08-30 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 54118c4e-c6aa-3be8-9a43-a4a8fa09ee79 | -13.323 | -51.428 | 2026-08-30 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 17c719c0-8fd7-35fa-aa53-10cdec465507 | -13.3991 | -51.461 | 2026-08-30 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 504b1297-a568-3814-80db-47e866f1126f | -8.1345 | -45.4923 | 2026-08-30 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e4bc609d-3e3a-31bd-9ecd-cc2c7fd07831 | -6.0 | -45.0889 | 2026-08-30 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 06c1ee1e-842d-34f3-a388-4ff118227d85 | -9.8927 | -60.2752 | 2026-08-30 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 12505817-2954-35c6-9d4a-fcc26d37aef2 | -5.4875 | -57.1611 | 2026-08-30 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 297f00c2-f172-3fb7-96e2-2c58d44b0d79 | -14.5634 | -52.0344 | 2026-08-30 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 2bbbd943-eecb-3a69-afbe-993a2bd4ac4c | -13.3995 | -51.4397 | 2026-08-30 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c342512a-28e3-3b96-9469-2074cfad6da9 | -10.8253 | -45.3152 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| c67765cd-7465-3279-b0a2-e60714af4268 | -14.4846 | -52.1299 | 2026-08-30 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| defc819a-f0ee-3f3f-b62f-1d780c2c8d11 | -8.2229 | -54.9412 | 2026-08-30 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 82575913-bfe5-365a-a1b3-4b8c4ed7a4b0 | -9.0722 | -60.434 | 2026-08-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| bf1781a7-d908-398b-ae7f-9f4c1d5a5fb1 | -9.1718 | -59.5211 | 2026-08-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 21af3f96-26b1-3669-8777-7072d2468ad8 | -11.2446 | -45.3267 | 2026-08-30 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |


[Clique aqui para ver as próximas entradas](README88.md)
