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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82b1bc4e-d5c5-3f59-8d5f-1dc363b79703 | -10.7902 | -46.3203 | 2026-09-20 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| fd1d551e-1187-3041-9d2e-4ee5ecce6a72 | -11.0802 | -54.0302 | 2026-09-20 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| fe5c6f8f-1492-3e54-a335-897dd09847ba | -9.6964 | -45.8666 | 2026-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 43fb0e43-edff-32b0-b37e-2b257a4cc55e | -6.3382 | -59.9566 | 2026-09-20 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 986de6fc-a68b-350e-b6c7-c354e9ad7d70 | -9.8502 | -48.4053 | 2026-09-20 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 699eb8c1-2d4f-3b9c-aa33-68d330f90491 | -8.0892 | -55.3511 | 2026-09-20 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d8d9e1b0-7065-3d19-9a53-5a1ffaa861eb | -8.4376 | -46.8757 | 2026-09-20 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 42da046f-7451-36fa-b962-01606a494f80 | -3.3492 | -59.867 | 2026-09-20 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| fbf2f9d3-e3f2-3a9d-acfe-c6577922fe08 | -6.9225 | -42.9088 | 2026-09-20 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.8 |
| 31d6d40d-2e4e-31d4-8cf7-76a7270272b3 | -11.155 | -42.7885 | 2026-09-20 13:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 109.0 |
| b37067c8-417e-3c9b-ace3-301c2667535e | -13.2602 | -51.7548 | 2026-09-20 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| dc583e19-868f-3b7b-b24d-9ae366f3e73e | -12.1328 | -47.041 | 2026-09-20 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 04340cf6-5055-3b7e-b95c-b835157438ca | -10.3171 | -50.2138 | 2026-09-20 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 55dbf5a3-cc88-318a-871a-e7123e1dd0f9 | -6.4236 | -43.8869 | 2026-09-20 13:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 969aecea-dade-32f0-bf3c-d449bd98ae42 | -11.379 | -51.42 | 2026-09-20 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 15b87cfe-2ea7-3234-8a1c-cd49eccb5c9e | -11.4714 | -47.776 | 2026-09-20 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| d05a5855-1f74-38f4-9171-b9ae8000ff5f | -12.7616 | -46.2029 | 2026-09-20 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 297078aa-6e78-32e5-b30e-49fff5a1b854 | -7.7631 | -46.7167 | 2026-09-20 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 1a6f6100-92dc-32e2-be7b-94db4d574d2d | -9.2865 | -48.2453 | 2026-09-20 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| a12b2fb5-8b16-330a-9778-23e429e14758 | -8.1376 | -46.8155 | 2026-09-20 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 98fb8362-7de6-3927-b161-df4c8d1c797d | -7.2519 | -55.5994 | 2026-09-20 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 464a25f1-216f-3d57-bc2d-e3ac1ba3f7f0 | -14.1253 | -45.6136 | 2026-09-20 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 165b3e8b-3e54-3a39-871a-83b4822a8e1a | -11.1183 | -54.0062 | 2026-09-20 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 9bad2365-8bec-3604-b585-99674802ff21 | -11.4537 | -45.3892 | 2026-09-20 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 6c67efb9-2bbc-3c35-8202-504a7293ce42 | -14.6661 | -46.6919 | 2026-09-20 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 47101ad4-e333-35bb-9c52-ef7c3e258a69 | -8.1874 | -54.742 | 2026-09-20 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 7ef32263-b4b2-36ea-a9d9-62effe2e76a7 | -8.9752 | -44.6722 | 2026-09-20 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 4846bc27-9745-3df5-a84b-7e5fa6281f05 | -14.1059 | -45.617 | 2026-09-20 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d8e8d8ff-190e-33d8-94b6-1050c66432f1 | -8.8639 | -45.937 | 2026-09-20 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 8213588d-57ce-375c-a04a-b70405c029ce | -10.8367 | -50.9266 | 2026-09-20 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 171.7 |
| fd995be9-d96e-31ca-b132-43555b1ef540 | -13.2606 | -51.7335 | 2026-09-20 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| bf4e1f78-e33d-3968-bc22-4511610ccce8 | -3.3367 | -57.8673 | 2026-09-20 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7c37e626-f76e-3ea3-bba5-4d250dd4e5f6 | -7.0455 | -43.6928 | 2026-09-20 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 5cb0116d-b2a7-372d-80dc-de005ce654de | -10.3917 | -48.8915 | 2026-09-20 13:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7ea5a9e8-25d2-3c41-9d24-a7b7bf5e7897 | -8.1872 | -54.7622 | 2026-09-20 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| aa009d82-1b9f-3db1-bd7e-51aa85563d40 | -10.3168 | -50.2352 | 2026-09-20 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 43ca3898-f9da-3be5-9c4d-c3a6e3a8a7f9 | -12.152 | -47.0383 | 2026-09-20 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| d23a3dc4-0937-3b7a-b9c2-4fbdb655b2b1 | -3.478 | -59.5779 | 2026-09-20 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 79e5cb2c-d589-3940-bc76-bb9247346e5d | -10.7899 | -46.3429 | 2026-09-20 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 180.8 |
| f80f9690-7cf2-3c9c-ad62-b6d2e7e87153 | -9.2756 | -46.2077 | 2026-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 916ef349-2f67-3566-b0f7-3c96ba9e2fa5 | -8.845 | -45.9391 | 2026-09-20 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| f8d994fe-e74e-38a1-80ce-555a719c93f3 | -3.6947 | -60.5645 | 2026-09-20 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 888a5d9d-f7af-35a7-85da-07009c91176a | -9.84 | -46.4136 | 2026-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 11a7a056-99c8-34c4-aebb-65f5d329f2ac | -10.7902 | -46.3203 | 2026-09-20 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 4aa97a12-5d43-3f13-9772-60ce3a59d012 | -9.3609 | -48.3251 | 2026-09-20 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5218cd74-d119-36e1-8c82-08f191701371 | -9.26 | -45.9616 | 2026-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 1373dea5-5167-3008-86dc-24d76fbd452e | -11.1369 | -54.0251 | 2026-09-20 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f9b2270c-8660-3e12-9ba6-dd00fd411041 | -8.7003 | -45.4567 | 2026-09-20 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a061bb2e-370b-36d8-8206-7492eb3f2b34 | -9.0541 | -48.7686 | 2026-09-20 13:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 81.1 |
| bc289fde-7e2a-3e08-ad13-763d6de5f542 | -14.1458 | -45.5638 | 2026-09-20 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| df3e9c0b-f437-3d63-9b7d-bd40d1d307d4 | -11.0994 | -54.008 | 2026-09-20 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 8f40fbad-5f64-3024-bfa7-46e713bcd4b0 | -13.2219 | -51.7595 | 2026-09-20 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| bfcc3887-50bb-39c6-a0c4-e55106b5ed34 | -6.4485 | -59.9909 | 2026-09-20 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 968c3b47-e340-3f45-af62-b2350b535822 | -9.8397 | -46.4361 | 2026-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 196.8 |
| d7631a89-befa-36ed-a9ab-53188f149a09 | -8.3965 | -45.6244 | 2026-09-20 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 55a153fa-5dbb-349d-87c9-9e2e04a71942 | -9.5325 | -45.409 | 2026-09-20 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 2c81c0e5-32b6-36ea-b587-c779673160cf | -9.8313 | -48.4073 | 2026-09-20 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 5dbc79cc-2d3b-36a7-93ff-30300ae11465 | -12.5227 | -50.0267 | 2026-09-20 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 26d9590a-1267-3d91-bcd8-7f65e934e876 | -8.7729 | -44.2568 | 2026-09-20 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 49fd6c04-12c2-387e-b3d5-4a3e31c1ea70 | -9.7154 | -45.8644 | 2026-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 12621bee-b214-36d7-9925-df7f67f7aa44 | -11.4345 | -45.3919 | 2026-09-20 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 959d3fc7-87f9-3f30-870f-de814f5405da | -7.6314 | -46.7507 | 2026-09-20 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 3eb78bea-a5a7-369f-b5d1-8229ec42ea3d | -9.2868 | -48.2234 | 2026-09-20 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 22f7f20f-18b4-3586-ba8e-25070702aa71 | -11.1545 | -42.8124 | 2026-09-20 13:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 5dd97283-524c-3aef-9fe3-ed2805ee6177 | -11.3787 | -51.4412 | 2026-09-20 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| d6f200a6-7d4c-3a89-aae8-b5571fffb622 | -17.5795 | -44.9765 | 2026-09-20 13:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 6198e64d-7e9b-3551-98a3-c04256f45e6f | -11.8744 | -50.0199 | 2026-09-20 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| d1d3d294-9684-3e9b-a444-ba996a5455ca | -11.118 | -54.0268 | 2026-09-20 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 188.0 |
| 3222d9e7-1f6b-3241-9428-01e0fee22518 | -11.3603 | -51.4009 | 2026-09-20 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 310c2b21-2d06-3d6a-bfcb-f58725350814 | -3.3454 | -42.7597 | 2026-09-20 13:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 33344dcd-2206-3880-921d-fd673bc25f06 | -10.7708 | -46.3453 | 2026-09-20 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| cc2650a4-f024-335e-8648-fe0180741ca6 | -3.3675 | -59.8666 | 2026-09-20 13:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 358a9f7c-95f3-3b59-ab49-16e94960548d | -12.2341 | -50.1703 | 2026-09-20 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 8abd6620-28d3-3158-bb68-8cb3b15a34f1 | -12.3209 | -50.718 | 2026-09-20 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 5844f4a6-638f-3b31-af80-9bb15e5d9046 | -3.6946 | -60.5835 | 2026-09-20 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 5fb4c075-3dfa-32ca-aae5-ab35c513eac3 | -8.8825 | -45.9576 | 2026-09-20 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.8 |
| e0039245-78be-3df8-978c-975071cc0edb | -8.754 | -44.2589 | 2026-09-20 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3f9c2db9-3ab9-3aa5-be24-f7fe62381613 | -6.3199 | -59.9381 | 2026-09-20 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 64f66e5b-34db-3a3a-8145-5c3a2af5388f | -6.9414 | -42.907 | 2026-09-20 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 88c46bb0-d602-3caa-a04e-bc4961783a35 | -6.4671 | -59.9711 | 2026-09-20 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7b7adcbf-043b-382f-9013-7b19248c6336 | -8.1688 | -54.7432 | 2026-09-20 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4fdd84a2-66b7-322d-a947-6d0149c1c060 | -10.9665 | -49.7583 | 2026-09-20 13:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 0913eac8-fcbe-34d8-ac99-47bdac5ad846 | -11.0802 | -54.0302 | 2026-09-20 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c83e6018-4f63-3439-84c1-348a98d5a3ca | -14.1258 | -45.5904 | 2026-09-20 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| feb4c324-7f64-35ed-959f-82efb0221f64 | -10.2973 | -50.2799 | 2026-09-20 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9eef987e-f51f-3f11-8741-e235ca67e88a | -11.4924 | -45.3608 | 2026-09-20 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6b492272-e7fa-31f3-9b60-4d3282c8bf0e | -11.0256 | -48.3164 | 2026-09-20 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 9198f635-7d87-304c-9cb1-fc0a91a2509e | -14.6856 | -46.6886 | 2026-09-20 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 161.1 |
| beb95fa5-678e-38df-bf03-e0052df4da66 | -11.0065 | -48.3187 | 2026-09-20 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3c1ee80d-6be9-31dc-8e47-f020894bb72b | -9.2567 | -46.2098 | 2026-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 32e344f6-4f49-3be3-9653-91de46ee09b6 | -11.3793 | -51.3989 | 2026-09-20 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| d861db80-0ddc-3555-ba52-28ff96df2273 | -14.7046 | -46.7081 | 2026-09-20 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 338.3 |
| 09d0967e-50c7-34fe-8336-ff47c33b4d5e | -6.4486 | -59.9717 | 2026-09-20 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 49761d12-b850-35ce-98fd-fca8f817a9c7 | -10.3914 | -48.9133 | 2026-09-20 13:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0040e6c9-851d-34ad-a324-f5bfdce86c98 | -3.355 | -57.8669 | 2026-09-20 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e0f6c922-09f4-3473-bf2f-8d9ccb2de629 | -6.7406 | -44.0909 | 2026-09-20 13:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3eb6eb3f-b46c-399d-b80b-10c004f439ba | -8.8636 | -45.9596 | 2026-09-20 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 67f33501-0937-3fe6-863a-6588d02bbae1 | -10.2787 | -50.2605 | 2026-09-20 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| fd267161-3de2-391e-8394-6f95cfc9606b | -12.7653 | -52.8661 | 2026-09-20 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3bf4787a-5240-38ab-ae7a-11c83ab9b4bd | -11.6609 | -43.4239 | 2026-09-20 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 309.8 |


[Clique aqui para ver as próximas entradas](README119.md)
