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
| 68d20e7c-d4a6-3495-bb34-2826a3a5ed6e | -7.00528 | -43.86496 | 2026-07-06 04:44:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ee011ce-e947-3022-8eab-cec944470966 | -8.72818 | -54.55648 | 2026-07-06 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 258b8867-75e3-33ea-ae9d-033c604af4dd | -8.21737 | -47.21408 | 2026-07-06 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3444970-084c-3a60-8726-2871077b5eab | -8.73246 | -54.55723 | 2026-07-06 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19f8a07f-9c08-38c5-a220-93f1cddae78a | -10.77274 | -54.11213 | 2026-07-06 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8367b18-b9e2-3b1d-af0e-8fd69d041926 | -8.11647 | -47.12462 | 2026-07-06 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c362904f-5c5d-3dd0-8d51-403d7fe130bb | -11.91685 | -43.37885 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31077d0b-17b1-3b07-9e85-b1323df23652 | -6.93617 | -43.71478 | 2026-07-06 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6de53e91-7726-3b14-94b1-a279630f87fa | -11.4331 | -46.59963 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 560ef881-524c-337e-9170-3a5904d7d2f8 | -7.0014 | -43.8644 | 2026-07-06 04:44:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37879e71-475c-34ea-8e09-0096954e6ae0 | -8.34284 | -46.49178 | 2026-07-06 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 963ceb08-032f-3dae-b963-48e1e589554e | -11.43779 | -46.6164 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e799f973-e09a-3c0e-90d3-b0e7dbdd01d6 | -11.45802 | -46.62225 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef10030b-ac7e-3c99-aee4-cc4263382efa | -6.90097 | -43.71264 | 2026-07-06 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf3cf5bb-a822-3999-a981-14cf56936072 | -10.77633 | -54.11198 | 2026-07-06 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20392f26-3a4a-3ca1-a28e-1c78e90f21c8 | -10.18304 | -48.50333 | 2026-07-06 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c33252a7-38cb-3adb-976e-35157d0949a2 | -8.91026 | -47.77062 | 2026-07-06 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f8eca35-57fa-367c-a20a-e77b9989a12b | -5.87957 | -49.7739 | 2026-07-06 04:44:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fa9c77d-ec17-3a15-8f8b-2d25bcf6044a | -8.3742 | -46.88132 | 2026-07-06 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f599962-4fd8-3d2b-b030-972cfd15b034 | -11.91894 | -43.38086 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1076ce50-1d99-3739-b3cd-cf28a778391b | -6.89242 | -43.71633 | 2026-07-06 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b24e1559-3b13-3efc-8ab7-2e60f4f51c80 | -10.01667 | -42.37337 | 2026-07-06 04:44:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ed916e10-3d61-33c6-a73b-3c2a53d8c364 | -9.74882 | -48.18545 | 2026-07-06 04:44:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f4bd53c-d4d3-3735-8fa4-c1f55d72c29e | -6.94254 | -43.72582 | 2026-07-06 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b6b7219-0d0b-300e-8299-5b663fd7c9d5 | -8.11364 | -47.12053 | 2026-07-06 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61254a40-ad4f-3dd8-9611-5fef57c5ac0f | -9.74827 | -48.18897 | 2026-07-06 04:44:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c352b6f5-b0b6-35b1-bfea-7dd866baef03 | -6.93935 | -43.72031 | 2026-07-06 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25004cbd-9937-30a8-8fd9-80f83f5cdae3 | -11.88604 | -43.82929 | 2026-07-06 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55222243-232e-301f-9131-a073aa4bf4e1 | -12.44071 | -47.00719 | 2026-07-06 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5121897-9e10-3c85-9724-57e30b9ab0bb | -10.39492 | -56.77261 | 2026-07-06 04:44:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 21aadfbe-4918-3bf1-9c66-8b9cb9eea2a3 | -10.45241 | -49.97712 | 2026-07-06 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b8222b45-33bd-3f92-bd8f-3f5d4a1a4c67 | -10.14682 | -48.29895 | 2026-07-06 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| caafe665-c0bc-3e85-aade-73bd5bc94d93 | -10.92342 | -43.05888 | 2026-07-06 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d3fe4523-59da-37ba-9278-c99cd3f9af6f | -8.73606 | -54.56197 | 2026-07-06 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 865a3253-a92c-3f2f-bfe0-a59aad41b715 | -11.45508 | -46.61771 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf072e23-d337-38ad-afd4-955b0ac0575c | -12.3392 | -48.22297 | 2026-07-06 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a7170ae-3a60-34b4-96a1-4b6ea1eb2d38 | -8.73037 | -54.56938 | 2026-07-06 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bc01dbe-8ad6-3baf-b3f1-706104d97b0b | -11.91463 | -43.38037 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8f620c9-338b-36a9-8f62-d93af4413283 | -11.91254 | -43.3784 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4779b75-e6aa-3e2f-aa4e-875354471475 | -10.39007 | -56.77179 | 2026-07-06 04:44:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b401895-3486-32e0-9f00-e1d95ebfbd95 | -11.44133 | -46.61692 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28661600-3604-367a-8427-fd243eb7de86 | -7.00208 | -43.86648 | 2026-07-06 04:44:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 076cb4d4-fe91-3f50-b462-fe553d328df0 | -10.93259 | -54.10065 | 2026-07-06 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab3f2539-2bf1-3d77-93d5-010aa6b79494 | -8.1204 | -47.12157 | 2026-07-06 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ba74c771-95a7-355d-b703-4f36a08c339d | -11.45332 | -46.6297 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f162708-b693-394e-856e-757a28acc190 | -11.9217 | -43.37531 | 2026-07-06 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3acae374-236c-3fe5-8436-025c0ddeee55 | -8.08221 | -46.69356 | 2026-07-06 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35471128-e34f-3dac-af1c-57c6691e0d79 | -8.73537 | -54.56602 | 2026-07-06 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 89522117-9463-3c78-ad28-3b78437a345d | -11.44073 | -46.62086 | 2026-07-06 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31e7fc39-b513-34cd-9cb3-b59a24c2350d | -8.73467 | -54.57008 | 2026-07-06 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59e0b613-5783-3b86-a01c-3f6104578c18 | -5.40235 | -49.00704 | 2026-07-06 04:44:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baa21f3b-0aef-3fc4-a8a8-9f34a616e647 | -9.50349 | -42.99234 | 2026-07-06 04:44:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3984d15f-828f-36c6-af99-589ade639476 | -13.29147 | -54.35844 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b60ba88c-d852-3acc-948f-e5a8b82e55b4 | -14.16604 | -43.64684 | 2026-07-06 04:46:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74406e54-0372-3866-a517-2707f7ecbb41 | -13.2507 | -54.31432 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9822b06-de74-3d96-813c-731f4bd175c4 | -15.42766 | -49.16585 | 2026-07-06 04:46:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a96eb734-0cc3-3e64-ad7b-7b6717f979ec | -13.24498 | -54.32367 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76243c21-fbb4-31be-a6f3-8efa05a894d7 | -13.20584 | -54.29943 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7e2829e-3e20-3c52-9d80-460b58b1b7b6 | -14.02242 | -53.94369 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0e6b192-a0c4-3302-8412-c0d8bb400e82 | -13.24106 | -54.32297 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 601d6c16-7504-3e5b-87cb-f7be086d9379 | -13.25372 | -54.32005 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eabb07ab-7d47-313c-b6bc-56dd4311d1d1 | -13.21969 | -54.35936 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 135fa3a3-7fa8-39cb-a514-ce66054a9599 | -18.938 | -47.44691 | 2026-07-06 04:46:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53921ddc-70c7-33e0-8410-776a95f822fe | -13.20496 | -54.30446 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea5ec29c-1ac5-3038-879c-d36e666182b9 | -13.29057 | -54.36353 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d1421cf-8641-3c60-ab80-c9fd7111fc6b | -17.99722 | -50.34415 | 2026-07-06 04:46:00 | NPP-375D | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93e1dfd5-7172-3167-8dd5-342958925420 | -13.29663 | -54.37522 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a30acbbf-24bb-3745-8d2d-8641ef578746 | -21.05888 | -47.25961 | 2026-07-06 04:46:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb0bcd60-1170-305d-b527-4db646c8bb2c | -13.30146 | -54.3708 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b2544f2-fc6c-36c2-9fa7-7c08547f2de0 | -13.2498 | -54.31933 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9143b438-2639-32a7-b704-79571cd1ed46 | -13.29753 | -54.3701 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b8ff510c-93a0-314e-9a11-fb57f8477de3 | -21.59444 | -41.89833 | 2026-07-06 04:46:00 | NPP-375D | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ab8d175-6cbb-380b-aa9a-283e9806900c | -21.0627 | -47.26011 | 2026-07-06 04:46:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2873ab9f-aa4a-34ca-89d8-081d47d4e606 | -13.24196 | -54.31792 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d90b3aa2-00bd-3335-818c-4da6cacbe6e1 | -13.29573 | -54.38034 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4477a41a-379b-38e1-8406-6ae33216809c | -13.24588 | -54.31863 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 021dd791-96e9-3361-a11f-b89e26f243fb | -13.2954 | -54.35913 | 2026-07-06 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82fdcf2b-ba62-36eb-a114-e115ec746278 | -21.59479 | -41.89481 | 2026-07-06 04:46:00 | NPP-375D | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4ad573cf-e7b8-3739-8ab5-8ca60eb531ec | -21.58908 | -41.89732 | 2026-07-06 04:46:00 | NPP-375D | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1f6ebfe4-3a74-35bb-b979-9b0e6fd5d3e1 | -17.00687 | -48.28584 | 2026-07-06 04:46:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dbdbd23-451c-38d8-ae91-7e72c13fb031 | -17.01035 | -48.28639 | 2026-07-06 04:46:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8807f384-789e-3409-a9c8-62472ea45cb6 | -22.91106 | -43.19725 | 2026-07-06 04:49:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d3b426b8-678b-346f-b08f-9d2d0f85d526 | -22.04101 | -52.90042 | 2026-07-06 04:49:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ca058de9-4ce4-313f-b1a3-ef142732cc5f | -22.91488 | -43.19952 | 2026-07-06 04:49:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 71a12995-fff3-3396-8ce9-523023142f4f | -20.83592 | -49.62831 | 2026-07-06 04:49:00 | NPP-375D | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 01cf84f0-6bb6-3d7e-92a1-4c737d9edc02 | -6.9077 | -43.71473 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 585d709a-079c-34f3-94c1-8463579be125 | -8.71966 | -54.5409 | 2026-07-06 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa5215fd-3442-3c33-926e-bb8f098cb47f | -6.93732 | -43.71874 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2de20e88-949d-3be4-8f4d-60aa5660bb9c | -6.94028 | -43.72701 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63714399-6ff7-38a9-b7fa-bbccc9bea80d | -4.34927 | -47.76692 | 2026-07-06 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d7ef2d8-d979-31da-a1ca-317ba38dd2c0 | -8.11528 | -47.11943 | 2026-07-06 05:01:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 639f43df-dc9b-3179-8b55-fde543f45a19 | -6.89589 | -43.71285 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c697d7c8-7188-3231-b354-c25a01374b71 | -6.42631 | -55.79722 | 2026-07-06 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11b63eb9-428b-3abe-b029-9536ba1333e9 | -8.7369 | -54.56149 | 2026-07-06 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76dbdedc-741b-33c6-8412-ee78dc6741f0 | -8.73138 | -54.55348 | 2026-07-06 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc528304-ea1c-35f3-9fc8-a32024ce01c7 | -8.34373 | -46.49336 | 2026-07-06 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0389e0ba-597c-3e6e-b61d-433b17e94e3c | -6.93792 | -43.71438 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c7cc154-b863-36f8-82ed-4b1f725f9b77 | -6.94085 | -43.72271 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0243cf5f-34e6-3d54-aba2-5e4c9302da92 | -8.34412 | -46.49053 | 2026-07-06 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ebc4c09-01ea-38c1-a210-11b4bb52e9be | -6.90238 | -43.70955 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README5.md)
