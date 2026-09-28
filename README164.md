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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fda4d246-8a2a-34b3-8167-4c6b337b4add | -8.50524 | -46.89508 | 2026-09-28 17:09:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e344cd69-f245-3e25-9de8-e2f242a0b6d1 | -9.32111 | -46.55651 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 086aea7a-39ac-3ba1-966b-eece9b843e7a | -11.29373 | -47.64103 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2f18b04-3721-3137-abee-b6dbc5f20861 | -6.89625 | -52.47868 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4624ba18-adaa-35cf-a91d-941d32959f61 | -11.00216 | -50.69557 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| df4537e2-4cf9-3596-978d-d58789a83034 | -10.45325 | -61.29767 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 75e45a49-8b81-35af-abbf-6fb405f666a7 | -10.8211 | -57.19355 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 22b348b0-f60c-3d38-98be-b1e47f8141ae | -6.14957 | -51.57021 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 53a97ec4-a2c9-3e25-9052-538ac3ed72ad | -10.93633 | -61.52167 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 772ec35d-7312-3010-a11f-c42a8c733de4 | -8.87129 | -49.73569 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| d610a703-324e-3344-a168-0d3f2b23441a | -8.30332 | -45.42162 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d4bdcaad-2457-3d89-8b96-2e2dcc32969d | -11.84869 | -50.84714 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3875df0-60f4-3a94-a852-ff05cc882149 | -12.16706 | -50.41722 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| adcfb3c5-a7e5-3ad4-979d-8aefe38acb58 | -11.46592 | -49.74259 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 90c6d969-81c8-3bad-8976-6f205ec18794 | -7.69583 | -46.9604 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0464f4a1-af31-36c6-ad41-3cffbe38bfd2 | -5.84796 | -53.82792 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dc123f78-2b43-3fd8-941e-580fe0283e27 | -8.64771 | -45.34673 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 37.4 |
| b51d6034-9a8b-3dd5-acbd-39f54154f11a | -12.17861 | -58.39574 | 2026-09-28 17:09:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c990904f-b513-3870-afb7-4db7f6a04cbc | -8.2241 | -45.45596 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 85a51ae3-a5f0-366b-b156-9445e8a1f333 | -7.81977 | -55.13469 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4fb18fe8-9d91-3da0-aaac-53916a5a5013 | -7.69237 | -46.96989 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d11c8f94-56a6-392b-a45c-0d896cd286c7 | -6.13085 | -53.05221 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2965db44-a085-360a-9319-68f3911bfa11 | -6.14882 | -51.56561 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9fdf7a3d-c42d-3aea-8ed8-01532d604047 | -11.46685 | -46.73717 | 2026-09-28 17:09:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8daf4d40-be5b-3d45-9d48-2e0687cf8669 | -10.80538 | -48.72147 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cfb57c79-155b-330b-92c2-4641cf678817 | -11.51431 | -47.39736 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d2bfdcfa-767b-31b7-9743-f259f31bc350 | -7.66636 | -49.53732 | 2026-09-28 17:09:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0bf8feb1-7de8-35f8-b687-b82d24e16d32 | -9.0984 | -49.89398 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9a129169-9a59-3e37-a68c-782a35b8999a | -11.17633 | -44.80244 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 97cab40f-14ab-35bb-b9c4-8f300f48fa75 | -8.23229 | -45.40696 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a862a3eb-0177-3084-a53d-6c6cc2a24b47 | -10.83313 | -60.7472 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ed023694-1ce8-3b33-a48e-02e8bf7bc18e | -10.69261 | -60.73516 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e6975c4f-06a9-3ff2-8d7c-3bdcdd51f310 | -11.08209 | -48.88871 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 80df406e-7cd2-3f45-ae05-a72d02c649a4 | -7.50026 | -44.56099 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 47d07c8e-ee2d-302c-8b7d-4aca38478470 | -8.88179 | -66.82173 | 2026-09-28 17:09:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0cdd9e31-de90-3cf6-8571-3ad462a1d80b | -6.06281 | -53.60468 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f223657e-fceb-3396-8a49-e1f44e82e059 | -7.99455 | -43.25834 | 2026-09-28 17:09:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 5b0df13c-4820-3867-8abb-531f8d4142b9 | -9.79935 | -44.8322 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a9fe0817-6223-343e-8f62-193c0f2ec4ce | -7.67907 | -44.7889 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| deab5708-580a-365f-8508-7d04f0d34975 | -9.32601 | -45.35901 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 03653a40-f020-35a8-80f7-80a932f8dda7 | -12.158 | -50.38634 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3dcc8640-10c1-30e9-b77e-7f76a5aa52cd | -12.155 | -50.352 | 2026-09-28 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 527f6a54-6b9c-3894-8fd2-6743c2d9a473 | -12.0158 | -50.7327 | 2026-09-28 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 175a80b4-5b4a-3266-97ea-349d46f6acdd | -11.5628 | -50.5069 | 2026-09-28 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 7679e582-0dbf-3e4a-8006-78ed9dee0502 | -10.824 | -60.7246 | 2026-09-28 17:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 821db069-61b0-3fe1-a2ac-2f8cd7027f65 | -12.1547 | -50.3735 | 2026-09-28 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c928e2a7-2223-3d61-817b-2b852ec861f8 | -12.2442 | -50.7485 | 2026-09-28 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9654e4cd-e396-3f87-872a-f1987c5148a7 | -11.9047 | -50.5317 | 2026-09-28 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ba736859-8944-3808-af55-6d33109d4166 | -12.0609 | -50.2773 | 2026-09-28 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| c4762200-4811-38d5-8f81-ad0b4d658ae7 | -12.206 | -50.7531 | 2026-09-28 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b415d974-becf-3250-b206-d19c4c5f1a0a | -11.0991 | -51.1111 | 2026-09-28 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0950e0c4-df76-3e7c-8f6b-9b49ef12e6cd | -10.7677 | -60.7279 | 2026-09-28 17:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 4951e56e-e907-36bf-b0bf-a9c43dd40ecb | -10.9156 | -50.6845 | 2026-09-28 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| ae2fe236-be2a-3653-9cd2-187d3bc7ee18 | -10.2565 | -50.5185 | 2026-09-28 17:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 11ed4e2c-eedd-311f-a76f-dfdadba0fc3e | -12.2445 | -50.7271 | 2026-09-28 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 713568c3-79a8-3d49-a9eb-008cf702584b | 2.1266 | -50.8788 | 2026-09-28 17:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 83.1 |
| fa4073ba-096d-3356-826a-7483ad88d9ad | -12.0612 | -50.2558 | 2026-09-28 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 4431e0ca-6a06-3e99-ac4b-5ef15d533562 | -11.9586 | -50.7393 | 2026-09-28 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0c91c3dc-9632-3d22-a178-1c82b0e3626d | -12.1362 | -50.3328 | 2026-09-28 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 31543a01-b497-38e0-a482-61dd394f8365 | -12.2248 | -50.7722 | 2026-09-28 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 13cfa90c-68d7-3bee-a91c-bf202733cc1d | -12.2251 | -50.7508 | 2026-09-28 17:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| b2c4d61f-f948-34a4-9fd6-d6b51b59060b | -3.72095 | -54.2085 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ba78310a-0b9c-3620-a464-06593f7f8222 | -2.11791 | -48.03754 | 2026-09-28 17:11:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 305ed338-dff4-3b17-a8e7-c9f1f0c0e048 | -3.80136 | -56.80773 | 2026-09-28 17:11:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1ce4709d-d1d6-3124-a9b1-9f65e3a031d3 | 0.88967 | -50.78358 | 2026-09-28 17:11:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7ff21f54-4b0b-3fa2-a868-65de2392bfa9 | -2.9068 | -54.09291 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f3136e6e-4f99-32f4-b727-185068932682 | -1.85397 | -55.44725 | 2026-09-28 17:11:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 08249a81-7824-3fbf-8ae6-0d9e8ad9ad66 | -2.89491 | -54.17557 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2ca992cd-4d63-3caa-9303-df5952380fcc | -2.09425 | -49.56633 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| de401b2d-87d8-3827-a7df-42362a025e60 | -1.43483 | -51.55266 | 2026-09-28 17:11:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ec3852ae-99aa-3710-b522-bbf91d2ae6bb | -1.8573 | -48.26752 | 2026-09-28 17:11:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f5239c92-ccd4-359b-b1aa-62f946bbb2b5 | -3.15385 | -54.0784 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 1857aaeb-ab4a-3514-aca6-84b225f1ce1e | -2.73052 | -54.20012 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cffba701-860b-317e-a013-7e1089e7fdcf | -1.22964 | -54.09592 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b3167358-315d-3677-a984-754b4e5e1dce | -3.76523 | -59.40016 | 2026-09-28 17:11:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0893ac8e-7d5f-30a5-913f-8c22a8abe454 | -1.29204 | -49.05722 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| eed408e2-206e-384d-94e8-f822bcaa1934 | -1.43736 | -48.8902 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d5561e1c-11d4-39ca-a0a3-9fafee092762 | -1.88521 | -48.68884 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 0f1c41ec-917d-35f5-b66b-ca14d68c4a04 | -0.4472 | -52.02269 | 2026-09-28 17:11:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8bbc11d-e7a8-392c-914c-b3d671891dfb | -3.01214 | -54.23017 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 04b8437f-519e-3d26-a265-016d6b367f3f | -1.04557 | -53.56498 | 2026-09-28 17:11:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4076a844-5015-35ca-a34c-4b2fa846ff54 | -1.21541 | -49.22229 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0da8fd3b-c9e9-3fb7-95c0-1aa951fb1fb6 | -1.2101 | -49.22612 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 67704923-7314-3e6a-8517-7783e97344df | -3.79983 | -52.00181 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c39d1329-4d28-3df6-9da1-703b1318258a | -4.25592 | -48.54229 | 2026-09-28 17:11:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 9b7f6e95-b507-3904-9ba7-c77770fd89d7 | -2.965 | -55.84552 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 625f9846-9a3b-330e-93e4-34042c539caa | -3.75614 | -51.33999 | 2026-09-28 17:11:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f55ff318-22f6-3ca1-9508-482371e52395 | -2.72707 | -54.20061 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0a2bcbbe-c85f-3a85-9e82-d36ffadedb95 | -2.57786 | -50.78695 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 10499533-844e-3398-b96d-eb649e16bb40 | -1.85321 | -48.27407 | 2026-09-28 17:11:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8667fe74-2dc2-3fdf-af94-d43eda68dbc0 | -2.51041 | -49.75081 | 2026-09-28 17:11:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 3536ee98-b2d4-37df-b45f-edb50dda8426 | -4.31898 | -48.63021 | 2026-09-28 17:11:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b0966d3a-3c7d-3f19-88b5-f921ad2afee3 | -1.31677 | -53.14166 | 2026-09-28 17:11:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1e323307-52a8-3109-a7df-0918a3ff0b1b | -1.21067 | -49.22303 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 740665fc-1ba2-3d17-83bb-d15c7283db15 | -3.57738 | -45.05597 | 2026-09-28 17:11:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 91c105c2-a590-31a1-a23e-2c24ff678583 | -4.31515 | -50.3965 | 2026-09-28 17:11:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4140885a-a1a5-38be-b6d5-1b5f35045088 | -3.00019 | -50.4713 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 66c0903d-1765-30e0-bb3d-679d1ca97016 | -4.44579 | -50.85093 | 2026-09-28 17:11:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5a71880f-36f4-3aa2-9ac8-3ad8bb9955a4 | -3.2253 | -53.95112 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9dae0144-334c-3c77-a5f4-7917da8363ce | -3.19884 | -42.44873 | 2026-09-28 17:11:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |


[Clique aqui para ver as próximas entradas](README165.md)
