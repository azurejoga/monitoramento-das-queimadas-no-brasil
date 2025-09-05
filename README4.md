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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 485fd362-b17c-3efb-b6e8-89d45a432544 | -12.97661 | -48.07144 | 2025-09-05 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f270662c-7a25-3f64-9281-48bc8fb133ff | -10.03937 | -48.14095 | 2025-09-05 00:30:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ad7e889f-db0d-3c2a-a8bf-5a64804db64c | -9.42722 | -46.77722 | 2025-09-05 00:30:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b94ca6fe-682e-35ed-853e-6cbe9d8b2b7c | -12.32273 | -47.0519 | 2025-09-05 00:30:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| cdf40647-591a-3fa3-be71-bcb5923fe918 | -12.29589 | -50.02282 | 2025-09-05 00:30:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 499e3d78-1284-3324-ac24-74551de01f2d | -13.29802 | -46.84122 | 2025-09-05 00:30:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c64c28f8-60ea-353e-a475-84cdb12be066 | -9.71292 | -48.99025 | 2025-09-05 00:30:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db750243-6f55-3550-8093-d0dfb58fa59d | -12.02236 | -43.78798 | 2025-09-05 00:30:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 9e4e855f-ef21-371b-8d49-0c07158c1748 | -12.09157 | -44.72816 | 2025-09-05 00:30:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| ad92f281-e7d8-3499-8d7a-5461559ef8c8 | -12.44462 | -48.08277 | 2025-09-05 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7eabf65e-bad3-3e49-94a0-d0fc68ff1d0e | -12.98504 | -54.84191 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 77ff4f8f-cc87-3258-9d25-d4cbfb684bf7 | -10.10498 | -48.07992 | 2025-09-05 00:30:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9f3bda91-a9b8-3621-8489-f9ddbf733ba0 | -8.08935 | -45.34026 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 4f2d24d0-f293-3c8a-8a97-0392847abc5e | -8.94085 | -48.65592 | 2025-09-05 00:33:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 85164ae1-703d-3493-94cd-26c90ed8c094 | -8.34993 | -48.30822 | 2025-09-05 00:33:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6f8343cb-a566-37ad-bb38-c72a9c8d8588 | -9.08078 | -46.99955 | 2025-09-05 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 97204b34-e2b8-33b6-ac5f-46ac71ad3c12 | -4.23766 | -48.56149 | 2025-09-05 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7c80bdc7-48ca-3a8d-8465-9a6699b9dcba | -5.16988 | -45.45739 | 2025-09-05 00:33:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5a2f92e7-943d-37a9-a246-a2f7a5b5f9fe | -4.80574 | -47.21958 | 2025-09-05 00:33:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8d4c49d5-5bc5-320b-8dc1-3a71d325d47e | -5.59978 | -45.0374 | 2025-09-05 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 87c59e5a-2412-3164-887b-baa00cde401c | -5.02932 | -45.34116 | 2025-09-05 00:33:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| dd76d11e-23c2-3da0-a24d-48599e756f76 | -7.89207 | -45.31781 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| fda6ed3b-2db6-3d3b-9472-72b68a919fa6 | -4.49233 | -47.67896 | 2025-09-05 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c17339e-05e2-346d-85e9-f744e462d812 | -8.0945 | -45.34347 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 28fcf8f2-bb6f-3cf8-921f-4e96102a5871 | -8.77874 | -49.63352 | 2025-09-05 00:33:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3f79ef87-e5af-3e8c-a087-dc4020c3f164 | -2.5527 | -47.72067 | 2025-09-05 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f2891746-8719-3519-a62c-722fe82b5b33 | -7.68415 | -50.27316 | 2025-09-05 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d15ff27f-4a94-3ad6-a455-abba2be615a5 | -3.68187 | -49.01315 | 2025-09-05 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a762b96f-1277-30ad-9bf6-2b57d5b273ad | -8.01038 | -45.43235 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4db1988b-531e-3c59-a870-0f94f9cb7b24 | -4.16777 | -46.81871 | 2025-09-05 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bdfb6f4a-51a4-3a49-8971-df09c2c9f196 | -6.26158 | -43.28048 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b9a76006-e141-341d-95ae-c12f4be5960c | -7.61542 | -43.85459 | 2025-09-05 00:33:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 01fe8083-76ed-316a-9ebb-635a36069002 | -2.38384 | -47.63465 | 2025-09-05 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a2ddd6b0-117e-3c00-9e70-93b58e786dce | -6.32463 | -43.95124 | 2025-09-05 00:33:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7a047332-afe3-387e-a2ef-54be4b097cea | -6.00225 | -46.68483 | 2025-09-05 00:33:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 637d9f67-ff29-3dca-814c-5c2d61816c25 | -6.81685 | -45.66891 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d9960980-6139-3ca2-809b-3dba6f650a8a | -6.42728 | -49.74897 | 2025-09-05 00:33:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1da89da5-bf1f-3050-a215-587051be18bf | -8.01183 | -45.44258 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| cf12dca7-6a35-39af-93e2-b9ff11853e2e | -7.3436 | -46.26081 | 2025-09-05 00:33:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3e14a26e-07b5-3553-a286-e2476b01e735 | -6.89223 | -45.18828 | 2025-09-05 00:33:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3a127590-d729-31f7-a031-bcaede5dea43 | -5.60984 | -45.0359 | 2025-09-05 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0af4c1f9-8148-314f-9fd0-f9638bf0e68e | -5.94737 | -43.02593 | 2025-09-05 00:33:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 62816c65-730d-3025-9d19-a04b9d237593 | -9.07952 | -46.99057 | 2025-09-05 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 69e914b7-488f-3b89-a806-a5313ebc8334 | -4.30773 | -48.07821 | 2025-09-05 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 63db47a4-c9e9-3fbb-a8f1-ddf3d7ddb3c5 | -6.35727 | -47.10732 | 2025-09-05 00:33:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ebd23b51-e620-330c-8358-4bb3bfb8bb6b | -6.26023 | -53.44496 | 2025-09-05 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 3a572bd9-30ee-328f-9b22-b304b6cc5e5b | -3.6843 | -49.03072 | 2025-09-05 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 54bb7770-df60-3627-8713-1c1f3da7feed | -5.60648 | -45.01268 | 2025-09-05 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 9a861cec-d3a9-3b9f-8089-279675655b73 | -8.8828 | -47.23831 | 2025-09-05 00:33:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fca13773-8939-304f-8919-76e57a8941ce | -7.894 | -45.23536 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0dce548a-6615-31e6-9c27-332818a263a4 | -3.68309 | -49.02193 | 2025-09-05 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 02af1a75-563c-3661-9f6e-a2c2de3d5de5 | -6.2502 | -43.28206 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 3b6ded26-0348-3943-86e2-0300fa8d1320 | -4.48343 | -47.68024 | 2025-09-05 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f1742f97-e267-3c72-b72f-cd2930d8a288 | -4.59728 | -46.59711 | 2025-09-05 00:33:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1c3303ac-12df-378b-8981-547ce6569766 | -9.07194 | -47.00094 | 2025-09-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 06d8fe09-e9fc-3ca4-9af1-174c0d4ebc7a | -4.21072 | -50.44979 | 2025-09-05 00:33:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3dc9654e-18da-3e41-a48f-142b11a6d304 | -7.16143 | -43.90004 | 2025-09-05 00:33:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 10fc7d25-b999-3083-9f0a-b0644e17d06c | -8.897 | -45.78242 | 2025-09-05 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e71005f6-2048-3ea3-9f90-1ce98b5850b3 | -5.67441 | -45.12642 | 2025-09-05 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5b8d8d93-2d95-34b4-b9ee-5a8b1ee6f4f8 | -6.25246 | -43.29706 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4e831f6d-1005-3eda-b5df-1cfd72773c2a | -7.6878 | -47.32633 | 2025-09-05 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fa6e73d0-e194-3683-9755-385b37509933 | -5.62908 | -45.74111 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6b8bd912-cc45-3cdb-89d6-7cd112687470 | -9.98046 | -51.62697 | 2025-09-05 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e91b58f4-4159-3224-a4b5-435498faf250 | -8.90833 | -45.86014 | 2025-09-05 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f5e5ca9-cfbf-3183-86dc-c1c5fe0a40f4 | -5.5981 | -45.02581 | 2025-09-05 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 763ecb25-507a-323b-974d-c5dd37e424e1 | -5.55275 | -46.18871 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4c0aeb11-d39f-3588-9eee-b4b7224c756e | -3.18977 | -43.90233 | 2025-09-05 00:33:00 | TERRA_M-M | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f71f6579-da77-3541-8a67-31b83a6c91d3 | -8.02234 | -45.41426 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d4bbe7a1-ec29-344a-8211-a55875569c64 | -8.09603 | -45.35383 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8419e280-3e57-34d6-9ba7-c56cc10cf4c6 | -5.59642 | -45.01425 | 2025-09-05 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e31df4b1-ec90-3938-a4dc-23faf75c65a7 | -3.67428 | -49.02317 | 2025-09-05 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9137f419-ce76-363d-8553-38aed1cdb53a | -2.51195 | -51.82189 | 2025-09-05 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 67774e6f-81de-3ce6-9cc7-7fb1ed3883ae | -6.21257 | -43.56789 | 2025-09-05 00:33:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6576be3e-f24d-31ce-82c8-e649cf748cf8 | -7.98279 | -44.52641 | 2025-09-05 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 0b6bf7a8-2f10-33d4-a7d8-f702eaed9b1f | -7.69626 | -50.2921 | 2025-09-05 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 349387ed-067a-37dd-9901-3b2385cf3751 | -3.11204 | -47.50141 | 2025-09-05 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 957c197a-1325-369e-9dc0-13e1cb710aa7 | -3.49264 | -49.04298 | 2025-09-05 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 46b7a2e3-4043-3bf5-8420-da7d16644440 | -6.87029 | -52.77603 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 97a29985-7764-3a0c-9e36-22d111dacf0a | -3.60537 | -52.64383 | 2025-09-05 00:33:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 78362e94-bb73-31d9-a1ea-a7b6eda2eb73 | -2.34887 | -47.58278 | 2025-09-05 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 50fedfae-a397-37a6-986b-dad275ca6393 | -6.25351 | -50.83684 | 2025-09-05 00:33:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b1265f13-fffd-34af-b45a-651b36f08bb6 | -7.79554 | -52.13408 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c515597b-afd3-305b-b557-99eca7a97b26 | -6.92668 | -51.20106 | 2025-09-05 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8743b7a1-39fe-3998-9cd6-b9aa3bf8be53 | -9.06213 | -47.00859 | 2025-09-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 352e6066-b4c3-377b-922d-2589cfde9519 | -6.42046 | -44.02079 | 2025-09-05 00:33:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2c341510-48c4-30aa-aee8-106e22e54553 | -9.70652 | -51.06182 | 2025-09-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| bb6b5a79-bb89-334b-a035-6be0c9544aec | -8.09082 | -45.35056 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 83ed2668-4fcb-3612-90aa-e8d18b2496de | -6.9036 | -45.1978 | 2025-09-05 00:33:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cec7ff0c-7381-33d2-955d-73810c04ff43 | -2.33981 | -47.58405 | 2025-09-05 00:33:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6c06fa99-c9f1-3a8f-b72d-ca865f943482 | -7.88905 | -45.29667 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| e18534c0-d781-316a-a968-c69ed357f5ed | -8.97599 | -44.45609 | 2025-09-05 00:33:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a16f9c73-d211-3594-8728-f84f66064992 | -7.59321 | -49.71829 | 2025-09-05 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c9295af1-975e-3f68-8cda-274fd209a83f | -3.23496 | -50.04744 | 2025-09-05 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 16a6c0d4-f24a-3974-b1f3-bb7b171e60c4 | -7.44509 | -48.97001 | 2025-09-05 00:33:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 166607ad-11b3-3ad6-b8fb-a2d1a4099b49 | -7.67137 | -48.73565 | 2025-09-05 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6b91ed1e-c2b6-3bc5-b32d-5bd073a6ba34 | -6.87221 | -52.79054 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| f0c01d39-6d2f-3581-a708-be2b83735fe4 | -7.61343 | -43.84145 | 2025-09-05 00:33:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b93a3931-2c6b-3960-9922-aa9bc6551bcb | -3.78656 | -44.12542 | 2025-09-05 00:33:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| a06c6967-1815-3b7d-bdc1-024fe713720c | -6.62026 | -43.97828 | 2025-09-05 00:33:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 795c2685-e966-3faf-8e7e-c3879613ab8d | -8.08788 | -45.32996 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |


[Clique aqui para ver as próximas entradas](README5.md)
