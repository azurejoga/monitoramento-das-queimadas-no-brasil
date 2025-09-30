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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34036a41-dfcd-3b89-a5db-1808fd162598 | -20.0491 | -41.3251 | 2025-09-30 00:20:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| ad5177f2-6fbf-3a17-9660-7bd28e391b96 | -11.1735 | -54.1242 | 2025-09-30 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| b7b48e43-d464-34b4-a5e7-efb59095e6f0 | -11.7524 | -44.7228 | 2025-09-30 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f0bb634a-c86e-3314-a4b8-944d496d153a | -21.0564 | -45.6881 | 2025-09-30 00:20:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 25833492-120d-3b28-82db-fe2d02b061b5 | -10.1855 | -44.8709 | 2025-09-30 00:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 439610e5-e18a-3a47-9676-ce4596de29d1 | -13.2339 | -61.191 | 2025-09-30 00:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| cec7c692-7386-34bb-994e-551083125cc7 | -5.5241 | -43.8878 | 2025-09-30 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 13c497c8-5ea8-3a93-8616-32ee996fc1ba | -11.1944 | -47.2334 | 2025-09-30 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5090f667-3a3f-31a4-8eb3-00845d22f57a | -11.7712 | -44.7432 | 2025-09-30 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4f882c31-660a-3dc3-879c-cb831f514c72 | -0.1012 | -51.2738 | 2025-09-30 00:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 739bf98f-d315-304d-a187-bff572e17947 | -3.1013 | -47.0082 | 2025-09-30 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 1dcc1d38-fb10-30d3-a3d4-401335ec40ed | -11.7519 | -44.7461 | 2025-09-30 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 617fa554-453b-3517-b68a-6fe95007a785 | -4.354 | -45.5773 | 2025-09-30 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 5cdaac93-5e4c-3993-91f7-e8f9f9a95762 | -12.8643 | -46.8904 | 2025-09-30 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| def7c08e-1f8b-3ec9-86f8-46be93f6ff86 | -1.2928 | -54.1784 | 2025-09-30 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 92d53aca-1f2e-37dd-9fee-7e153ba9e083 | -9.4192 | -54.7172 | 2025-09-30 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 06e096e2-568a-3025-94cd-9b2580d86b69 | -11.1548 | -54.1054 | 2025-09-30 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| cf11ca89-d4d5-3249-81be-b9094db0292c | -8.2659 | -45.5244 | 2025-09-30 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 69c28a62-ba75-38d7-9b4b-049cc708b6c0 | -11.2329 | -47.2061 | 2025-09-30 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| bc9a70de-0da7-3a7a-8cfe-92c7814c0dfb | -5.2326 | -45.2328 | 2025-09-30 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f74752b5-1fb9-3b31-88af-c5214b8e5f9f | -5.5243 | -43.8647 | 2025-09-30 00:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 873bafdc-3d73-399f-8322-0283b5fd7a9f | -17.4681 | -46.2027 | 2025-09-30 00:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 8d54d5a1-9671-3b10-87e4-5ac474ff5623 | -12.8638 | -46.913 | 2025-09-30 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 06f5feb5-db43-3281-8ea8-8d6efb96271c | -10.2045 | -44.8684 | 2025-09-30 00:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| f8f3030e-8a5b-3786-9e0a-ab7f105c449f | -19.6027 | -45.8861 | 2025-09-30 00:20:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 17a31aea-fad1-308b-b3f0-cafad5460831 | -11.1948 | -47.211 | 2025-09-30 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 60ad5f3a-f51c-3b4c-aa89-f3117cc6feb8 | -8.2471 | -45.5263 | 2025-09-30 00:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 84902ed5-3885-3d85-b3d8-a153f11a7e97 | -13.6285 | -42.5324 | 2025-09-30 00:20:00 | GOES-19 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 2e5d8057-c738-3667-a617-1f0cc4ec943f | -9.4005 | -54.7186 | 2025-09-30 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ac3be1b5-9c4a-3e6c-8da8-87c8c2272ac6 | -11.1546 | -54.126 | 2025-09-30 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 246.5 |
| ba4d6563-459f-30f3-916c-e23ce4bd58e7 | -20.98034 | -45.57005 | 2025-09-30 00:28:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 28f2fa25-7ab1-3310-8903-b4f325bf4b0d | -20.09102 | -43.90632 | 2025-09-30 00:28:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 23571336-0032-3fb4-a67f-d4b0cdc351cc | -21.31891 | -46.75942 | 2025-09-30 00:28:00 | TERRA_M-M | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 089cf2f2-6e5f-34b4-8bcf-c03f1b7f9375 | -23.20372 | -47.40654 | 2025-09-30 00:28:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| d3464ff1-bd33-3a6a-a9eb-1ac708636404 | -21.69047 | -48.06239 | 2025-09-30 00:28:00 | TERRA_M-M | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 704f5db3-1227-3f87-8973-063bb3a3d067 | -22.98055 | -47.59735 | 2025-09-30 00:28:00 | TERRA_M-M | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ea363092-6c99-318c-9c24-286fc9b809b3 | -21.04274 | -45.67904 | 2025-09-30 00:28:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6c445c69-d0c4-31ba-8fe2-55f125ffc0e0 | -20.17804 | -45.69781 | 2025-09-30 00:28:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| aac7fd88-a030-3b6c-9522-aa3bed189cc7 | -19.51291 | -41.70495 | 2025-09-30 00:28:00 | TERRA_M-M | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| abe1e840-64fa-309b-80a4-fd3acc4f4cc7 | -20.74469 | -47.14579 | 2025-09-30 00:28:00 | TERRA_M-M | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 43711a28-5650-37bd-bf1a-4d3aaa156aee | -19.55459 | -44.95229 | 2025-09-30 00:28:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fad87f8f-98d8-33b8-9046-fe5b39ed46ec | -19.60751 | -45.89379 | 2025-09-30 00:28:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a5f83ae9-533a-352f-b0c0-6475b4b9ce5f | -20.24119 | -45.74889 | 2025-09-30 00:28:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a33ab423-e595-34f0-ac8b-b28d746cd73c | -20.39618 | -43.67546 | 2025-09-30 00:28:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| e9f80dc1-2844-3bad-ab67-a2c8c5e9d512 | -20.38743 | -43.17346 | 2025-09-30 00:28:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| b4044510-3713-3c7d-be7d-0c22cdb651e6 | -24.05991 | -49.14014 | 2025-09-30 00:28:00 | TERRA_M-M | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 57ac506d-d40c-3148-93ba-2352313a1fcb | -19.59735 | -45.88584 | 2025-09-30 00:28:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d8f93e21-f577-3bcd-831f-422e53516435 | -21.68243 | -48.07418 | 2025-09-30 00:28:00 | TERRA_M-M | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1636763d-1401-3682-a037-94c0a623aa81 | -23.22805 | -49.40749 | 2025-09-30 00:28:00 | TERRA_M-M | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| d0d451e3-aa24-3b4f-ae57-2c7fa315c85b | -22.31357 | -49.59196 | 2025-09-30 00:28:00 | TERRA_M-M | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| d977cb5d-b8a5-3140-aafd-e1e623f54c29 | -21.61944 | -44.06149 | 2025-09-30 00:28:00 | TERRA_M-M | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 93b22172-50c5-3585-b6f9-91c189ef7c6d | -19.86521 | -43.82605 | 2025-09-30 00:28:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 98547507-9966-30d4-9d7c-c1469e189ec0 | -20.77524 | -44.0964 | 2025-09-30 00:28:00 | TERRA_M-M | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 4f6df18a-f8fa-357e-b6eb-6c680ff4c79f | -22.18692 | -46.7865 | 2025-09-30 00:28:00 | TERRA_M-M | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bddce897-5a7f-3870-ba70-e9733ae3c7ee | -23.21294 | -47.40517 | 2025-09-30 00:28:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| d5beb10b-29fa-3ab7-be88-0042207bc586 | -19.69841 | -43.68993 | 2025-09-30 00:28:00 | TERRA_M-M | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7466ceb9-b267-3c80-9947-9190dbd2b305 | -22.05033 | -47.00443 | 2025-09-30 00:28:00 | TERRA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5097162d-5257-3be3-82d7-240ca93a5306 | -21.30155 | -45.04485 | 2025-09-30 00:28:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 4e509612-f1a5-35f0-bfe7-d34ce6a9cbf1 | -20.34624 | -46.85072 | 2025-09-30 00:28:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f11fdeee-9b04-36dc-8fde-eff3e2a05257 | -20.37096 | -41.37537 | 2025-09-30 00:28:00 | TERRA_M-M | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| cc35cf72-0764-3414-b3fb-18f818877e4a | -19.76614 | -42.1535 | 2025-09-30 00:28:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| eeb40bb8-889a-3b90-808b-48d286c43309 | -21.69178 | -48.07286 | 2025-09-30 00:28:00 | TERRA_M-M | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 1a140f88-d95c-3428-8ec5-5ccf5192bbce | -20.34496 | -46.84122 | 2025-09-30 00:28:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d4c0a23c-9469-37ed-ac47-4216fa894ccc | -20.23634 | -41.6308 | 2025-09-30 00:28:00 | TERRA_M-M | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 16b5e0c0-6851-3a80-92cf-ba688161efe0 | -23.41253 | -47.23496 | 2025-09-30 00:28:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 7daad9f8-13dc-30e1-9cc6-0f9e4081c3db | -20.77371 | -44.0862 | 2025-09-30 00:28:00 | TERRA_M-M | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 870ea4b7-0cf8-35e0-b5d2-430e89b978da | -19.35285 | -43.97341 | 2025-09-30 00:28:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5c3b5c11-e5f3-31c0-958b-5e8831fd2d39 | -20.29156 | -46.23865 | 2025-09-30 00:28:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 333dbaf4-edfa-372a-ba4b-076d140675ab | -20.42156 | -43.37129 | 2025-09-30 00:28:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 943b347b-2f02-3551-8f2c-5380af92961e | -20.06145 | -46.78736 | 2025-09-30 00:28:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8391ce69-e236-39ad-899b-a32b54af197d | -20.42931 | -43.35812 | 2025-09-30 00:28:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2e685a7e-ba33-3bdd-9992-10e56d3a08aa | -21.1961 | -46.11977 | 2025-09-30 00:28:00 | TERRA_M-M | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 75963c29-815e-373d-ae87-bcd900080c86 | -19.86362 | -43.81569 | 2025-09-30 00:28:00 | TERRA_M-M | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| dc0e4243-ade6-38ef-a05e-a52480f349bf | -19.86557 | -42.59192 | 2025-09-30 00:28:00 | TERRA_M-M | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| e16e477a-1390-3afa-bbd5-f5b272d6c897 | -21.6811 | -48.06357 | 2025-09-30 00:28:00 | TERRA_M-M | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1b7fefac-756c-3759-afbd-43b061b9b783 | -20.41977 | -43.35996 | 2025-09-30 00:28:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.9 |
| 55e596a4-dcac-3a65-831f-8fd605c04b30 | -19.60618 | -45.88441 | 2025-09-30 00:28:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 1ca59b1f-2fdb-3859-bfb2-d1064cce31cb | -23.70702 | -49.78948 | 2025-09-30 00:28:00 | TERRA_M-M | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| de9be2c5-9e18-3cfe-b17a-1a6870eeddb8 | -20.9627 | -46.3002 | 2025-09-30 00:28:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 38a86c80-b4de-3180-b9e8-62e30ac562ea | -20.06274 | -46.79684 | 2025-09-30 00:28:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f15ccd7e-5b4e-3cad-a666-fbf399119c6d | -19.59868 | -45.89524 | 2025-09-30 00:28:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 41d2de8b-f021-39c2-9b06-e1aa2f25ab25 | -24.06138 | -49.15335 | 2025-09-30 00:28:00 | TERRA_M-M | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 73f8353d-948a-3be5-a0be-8adc7fc9c429 | -20.08947 | -43.89613 | 2025-09-30 00:28:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d9bef74e-e319-33e0-ad68-9e48e66f997d | -22.5183 | -44.59314 | 2025-09-30 00:28:00 | TERRA_M-M | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 19db9f43-5382-3967-ab30-f6da513e4920 | -21.33286 | -46.72789 | 2025-09-30 00:28:00 | TERRA_M-M | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| dc7747f0-88a8-3f43-9d11-fc2b1d592c18 | -22.98187 | -47.60789 | 2025-09-30 00:28:00 | TERRA_M-M | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| e41aa752-f98b-3893-b516-66c8e63bf893 | -23.1578 | -45.73206 | 2025-09-30 00:28:00 | TERRA_M-M | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| be3fa932-2951-3a7b-be6a-41901dcb8fa7 | -20.41802 | -43.34885 | 2025-09-30 00:28:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e794620e-3b4a-3ba6-b7b5-53f8dad3e798 | -20.61497 | -46.18775 | 2025-09-30 00:28:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 21a0fc4f-bdef-3612-9dab-12c87b595e6c | -20.61367 | -46.17838 | 2025-09-30 00:28:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89503efe-011b-3e7d-b8fe-4f33a190c5ed | -21.99532 | -48.29735 | 2025-09-30 00:28:00 | TERRA_M-M | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f9c211f1-c824-3914-b88c-5ca9ff67c8ef | -24.05255 | -49.14761 | 2025-09-30 00:28:00 | TERRA_M-M | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 67665187-0be4-36e8-a7b9-d8d06770b629 | -20.96141 | -46.29072 | 2025-09-30 00:28:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| f8a11221-ebb6-3216-9ca4-95e475f249ff | -21.09519 | -45.33563 | 2025-09-30 00:28:00 | TERRA_M-M | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 7f3629bc-9448-3c8b-8d51-506704d733ed | -21.22094 | -47.13181 | 2025-09-30 00:28:00 | TERRA_M-M | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 1c9065ae-5f2c-38ec-b51b-6f83d4b84c31 | -21.04407 | -45.68845 | 2025-09-30 00:28:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 0d4c49a7-b7ad-337f-8c84-319f87efd89d | -20.05124 | -41.33885 | 2025-09-30 00:28:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| dfae0994-d92b-362a-9dbd-1a2c72b721ce | -19.60861 | -43.83424 | 2025-09-30 00:28:00 | TERRA_M-M | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4aca02a6-fd03-3d5c-a7e0-e82d629173dc | -20.58754 | -45.5912 | 2025-09-30 00:28:00 | TERRA_M-M | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c6e693e-ce0d-33e1-b062-26131dbc3f39 | -20.6225 | -46.17698 | 2025-09-30 00:28:00 | TERRA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README3.md)
