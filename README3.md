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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9c6f8dc-8d15-3cf9-8dc1-536324963ca8 | -10.63242 | -46.10395 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3ce3a5f0-a1b3-3973-a3a1-77927d198b87 | -10.69488 | -54.17626 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| bb750236-2532-35b5-8245-b80c48ae52c4 | -13.55528 | -49.48401 | 2026-09-13 00:03:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 4dd270ec-38ca-3376-a9e1-05bd76a19ffb | -12.17778 | -44.00905 | 2026-09-13 00:03:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 062747d8-86be-3082-9654-745ab263aaca | -15.63457 | -43.32937 | 2026-09-13 00:03:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 27.2 |
| b1c24fa8-1d6c-3f0a-b5fe-6d3b686b210a | -11.19288 | -42.79217 | 2026-09-13 00:03:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 32.2 |
| c588889a-606b-37e0-963d-bb93b63bea8f | -12.76481 | -48.80953 | 2026-09-13 00:03:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6e54c666-a29d-37f1-9ef2-4e1d99845d42 | -10.98069 | -49.71616 | 2026-09-13 00:03:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed8e5ad1-4f0a-36d8-82f3-3d5ec0e70ecb | -8.80458 | -45.86929 | 2026-09-13 00:03:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e0694402-9cec-3e11-8cec-9df08ce46aea | -10.93318 | -47.91214 | 2026-09-13 00:03:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4e713696-d16f-3e9b-8040-d74d246cd02c | -10.48858 | -48.09398 | 2026-09-13 00:03:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e849c660-3611-3a9f-a54a-196449409b85 | -13.14707 | -48.58252 | 2026-09-13 00:03:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 231ab6ae-f5eb-35a6-b8e7-cac426749dd7 | -10.47286 | -48.63895 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b9a23c02-b255-397c-adeb-82ec86d4dd4c | -11.32625 | -48.55074 | 2026-09-13 00:03:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 93044446-b77b-3d00-aa7e-7b32e6e43e9c | -9.38688 | -50.12484 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 3e3fec71-2a40-3031-9924-ab2312bae6aa | -11.84055 | -46.38871 | 2026-09-13 00:03:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e6d64a23-35b4-324d-9a10-6b166ec52ae4 | -13.3068 | -51.72003 | 2026-09-13 00:03:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f6ab0e5c-13c6-3a14-b5e4-a8d50978637c | -10.96829 | -48.35497 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca1a04b3-69c4-356d-b8a3-ab2d281a253b | -10.95065 | -57.20841 | 2026-09-13 00:03:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| e733120a-0492-3e5f-9473-f8f4a30f98e3 | -10.68349 | -54.17765 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 306.1 |
| 18c60e61-6114-3b37-9ce8-2170a852302c | -10.93786 | -48.33163 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d26d2065-c4b3-3a7b-a4d2-2b6c9879b1cd | -9.53921 | -45.44338 | 2026-09-13 00:03:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6ab3fbf8-6fff-3460-9555-8fbdbbebc2dc | -10.29466 | -45.27725 | 2026-09-13 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 105932fb-0253-3463-966f-a67797219ddd | -12.66616 | -54.73668 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| eab06fe4-0e30-39fc-93e5-02f08f77a3c3 | -13.74617 | -42.59687 | 2026-09-13 00:03:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| a97a1488-13a4-35e7-955f-9665d8832010 | -11.34771 | -48.17245 | 2026-09-13 00:03:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f144fcd7-134f-376f-98aa-985ed87b7dd4 | -10.61882 | -50.7271 | 2026-09-13 00:03:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1062245e-9cb4-381b-90bf-3622de49dc01 | -10.51723 | -47.90346 | 2026-09-13 00:03:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a20f8b33-ec7a-3cf1-b438-05bd4b83edfb | -10.30699 | -45.28831 | 2026-09-13 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4bbbfb84-246c-38cc-9be4-6186e3bdd3e9 | -10.69504 | -54.18606 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 4414f64f-3edf-3d94-8125-79f2a722bd05 | -10.3001 | -45.26969 | 2026-09-13 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9fff180f-3b1c-3287-a7fc-fcb31165f276 | -10.21532 | -45.249 | 2026-09-13 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d9b7141d-5042-3f0e-987f-3e0ac8bc9ec6 | -10.53841 | -51.37706 | 2026-09-13 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| d07185e0-693b-396a-945a-4ec9cb20c1e3 | -11.25249 | -54.15877 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| daa11391-9b6a-3dc6-83bc-be186ac7f902 | -14.96403 | -47.53424 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 1f813d2a-81ed-322c-8cd3-085d3e697952 | -9.84644 | -48.51582 | 2026-09-13 00:03:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 61305790-a3b6-3c2f-8386-be003726ad08 | -10.30505 | -45.27507 | 2026-09-13 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d81f9cc3-1d53-367d-b6cc-5bf973ddce9c | -10.63411 | -46.11519 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 4118dbc9-26c3-3d21-a594-7ada8612c11a | -13.54501 | -44.04508 | 2026-09-13 00:03:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 422b8804-00c8-34fc-9016-e95f3ca645d3 | -13.4498 | -48.49525 | 2026-09-13 00:03:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2c9ea165-418f-3904-b292-e7678922963f | -13.31667 | -51.71876 | 2026-09-13 00:03:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 40c60b19-38a2-3b07-8b3b-eb11b194e58e | -13.45859 | -48.49396 | 2026-09-13 00:03:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| e726d64f-722c-31b3-8cdc-d67252eb5488 | -10.34017 | -48.09046 | 2026-09-13 00:03:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 20a2d88e-294a-3b76-afb6-19217552c089 | -14.12441 | -42.11941 | 2026-09-13 00:03:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 914f9775-c08d-3553-a54a-05ed89c7a894 | -10.81199 | -48.55567 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 665f2b95-c6b0-3bcf-814f-5f7d54f695d8 | -9.75457 | -48.18489 | 2026-09-13 00:03:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 125685bb-2089-370c-b2da-5e7b3b1b85d9 | -9.65897 | -46.03926 | 2026-09-13 00:03:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 77b897b6-6328-3c9d-9e1d-0ce74ccac582 | -9.41588 | -50.13906 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0acdbbe2-a1fa-3449-8134-7a2945750053 | -10.47411 | -48.64799 | 2026-09-13 00:03:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c2408025-f45e-38a4-8c3e-f13de9f65349 | -15.55358 | -53.79201 | 2026-09-13 00:03:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 754878a0-64f8-3ac8-8e95-2627ac704cb6 | -12.49569 | -47.16163 | 2026-09-13 00:03:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a2402704-c95e-34f3-95c1-f706d4d6f0ec | -13.01856 | -48.64398 | 2026-09-13 00:03:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b7742e42-47cf-3377-aab6-729e01be0466 | -11.325 | -48.54176 | 2026-09-13 00:03:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a74dea72-ee20-3797-a19d-54477ea7aa89 | -16.9839 | -49.73828 | 2026-09-13 00:03:00 | TERRA_M-M | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 9d64fe3e-0ed6-359c-8b78-52d0f1090534 | -14.95518 | -47.5357 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6cd422cc-aa71-3026-84af-ab01b136b1e5 | -11.72116 | -46.72955 | 2026-09-13 00:03:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a29fec18-c520-3847-a9e7-380c8a8d453a | -10.6501 | -48.91095 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 59c44b75-50f1-35ad-8d10-be76284112db | -9.8819 | -47.5864 | 2026-09-13 00:03:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 447d1fbb-6c05-3fcd-95b9-b411c36698dd | -16.31964 | -46.55899 | 2026-09-13 00:03:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb49cd8c-1cf8-3b49-b277-5595cd655f47 | -10.69319 | -54.17059 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 261.6 |
| 64215398-1a2b-3c28-a483-0e82c8584d5e | -12.85098 | -44.39533 | 2026-09-13 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 81be6728-ac5b-314a-bb8c-cec2969e3038 | -13.30825 | -51.73133 | 2026-09-13 00:03:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d0781336-4399-3288-b21c-1807a83ffd82 | -11.1941 | -42.78564 | 2026-09-13 00:03:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 44.8 |
| 510a3d78-a15a-33e6-a82e-f85575f06154 | 0.14513 | -51.45951 | 2026-09-13 00:05:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1836a7fe-a563-3aca-933b-74254cd187bb | -6.10563 | -57.67916 | 2026-09-13 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9232352f-c84c-38e9-a32e-3eec3b35a5ce | -6.10376 | -55.66392 | 2026-09-13 00:05:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 310b508e-29b9-33f3-befa-9db8e4b80040 | -8.55101 | -54.70566 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| db6f52cf-a360-3bcb-b2e3-5adc453227da | -7.60099 | -46.96976 | 2026-09-13 00:05:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fa108d62-1d9c-3e90-9070-fdcddfd0efee | -6.72705 | -50.82626 | 2026-09-13 00:05:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1ef3dcb-31a3-3337-afdc-e2eda81f7ee3 | -8.21611 | -47.87418 | 2026-09-13 00:05:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a3bd8f93-75b3-3d29-b9e4-104a5af05be3 | -3.19675 | -51.01777 | 2026-09-13 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 18ae757b-34ae-30de-8b36-938851f56bb5 | -6.78728 | -48.65802 | 2026-09-13 00:05:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 19808a78-32a2-3745-9570-36329b4c83b3 | -2.94588 | -50.40465 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| fbe6c5c4-8e70-3878-8b0f-af48a3337cc9 | -4.34872 | -54.78319 | 2026-09-13 00:05:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 37ddfb92-9b13-3af9-9640-bf462d90980c | -5.01842 | -49.99141 | 2026-09-13 00:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 88638cb5-eece-3723-bcce-bc4901922a64 | -6.00205 | -44.25439 | 2026-09-13 00:05:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 11d497de-ee53-3ee3-8d99-70fc7e14c17e | -6.51684 | -47.6036 | 2026-09-13 00:05:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2a2749ce-349b-3757-a88a-d28615082a57 | -8.54154 | -54.72274 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 51d437cd-3602-3563-a6ba-712b49bf2ac6 | -5.29543 | -49.20009 | 2026-09-13 00:05:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d6ef5be7-1d94-3d32-bad4-cc3bb42ab8d9 | -3.33548 | -42.31096 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 9f82ea97-9354-3a0c-9a17-39f6607d55cb | -6.72583 | -50.8173 | 2026-09-13 00:05:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cea9721d-bbd4-3461-bd21-6be36c9d10ca | -6.30748 | -52.93394 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 68b82179-28d1-3408-bb74-bed6557e39d3 | -5.80925 | -53.81381 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 752141c2-3035-304a-b063-7215fb67b3e3 | -4.92081 | -45.83827 | 2026-09-13 00:05:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2fa8d276-ffeb-3524-abb6-6659b47b391c | -3.40796 | -48.88831 | 2026-09-13 00:05:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| a8e5f6d5-a29f-3a5b-b21e-1acccc106ffc | -6.22784 | -51.69503 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fe1a5f83-c557-3eaa-8f1e-32f4eaa465af | -7.76715 | -46.68891 | 2026-09-13 00:05:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f13b1768-d585-3aa9-9476-1573823d7545 | -7.53128 | -47.33332 | 2026-09-13 00:05:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 41dc5466-6bb7-3ea9-8b60-c0fb726e6795 | -4.45123 | -50.16756 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8f29825e-65bf-357b-8248-49e7ebe86f5a | -2.9483 | -50.42222 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e5e0273e-7bc4-3b1e-a9d4-ded6a5297870 | -1.46202 | -52.96513 | 2026-09-13 00:05:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4eccc38f-ad24-3a5a-bf3d-819c3acd07e8 | -1.22202 | -54.12761 | 2026-09-13 00:05:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 357884db-fce5-3e58-a6c4-16d717f5c004 | -1.21914 | -54.12318 | 2026-09-13 00:05:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 186a045e-e95c-3475-9974-d4277b19cd6f | -3.15605 | -48.60845 | 2026-09-13 00:05:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6a579ff0-fa90-3158-a6ee-9cca427d878a | -2.61428 | -54.75455 | 2026-09-13 00:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| dc637b73-b45f-3ab4-a127-58b99f3e52f6 | -9.13437 | -51.60473 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6bffb333-4cf0-372d-a341-a5bd4793b935 | -8.54871 | -54.70031 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9c996659-8390-3c0e-b9ae-30c07f73f079 | -5.79899 | -53.81511 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f591a28d-835c-35e7-9a3f-0d941d9d6d33 | -6.66495 | -50.91438 | 2026-09-13 00:05:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 910555a9-e896-3300-b4c2-6f098cd3d838 | -4.46162 | -50.16018 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |


[Clique aqui para ver as próximas entradas](README4.md)
