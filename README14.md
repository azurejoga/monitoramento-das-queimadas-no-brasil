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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cad545df-6002-3411-981a-86dca4fe9b28 | -13.68685 | -51.85081 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8d14d40f-d10f-372b-add4-cd8ac104a3a4 | -14.14917 | -48.05915 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0a8f73d-ca1e-3c38-ad47-d93bdd598608 | -15.252 | -52.84444 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4d5ca6e-3133-3f1f-aff2-9898899ca483 | -17.91659 | -44.3791 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19b77a06-594b-3bdd-a62e-2f550608f709 | -14.34396 | -51.7738 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6e54cfb5-a4bd-352c-90d2-6724e455e152 | -14.8482 | -40.866 | 2026-08-23 04:10:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 877b396c-0f06-30b4-a772-67c76c53d806 | -13.56302 | -44.10058 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb241972-543b-314c-adde-03326fb75aa7 | -8.53478 | -54.83678 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65bbd27d-766c-3776-ae95-c53046f5b706 | -10.06575 | -46.45813 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65d94437-376c-3b10-8794-9bd3856fc411 | -13.38031 | -41.32273 | 2026-08-23 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 12c35381-ee3d-33dd-afdd-7594d9f0682b | -12.78671 | -48.38505 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f707fdb-c10d-3a95-a3e7-8311cbca692e | -15.32827 | -46.07906 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b699e96b-e509-3bd9-abef-0653dfb2170c | -13.5597 | -44.10003 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8d2e8d7-5438-3d4f-aeaa-dda8e809fa5f | -13.17316 | -51.42313 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f921ab6f-7025-3335-829a-3c1aef2e4087 | -15.34245 | -52.77493 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c650538-7381-3983-93a7-7b18f9913dcc | -13.09348 | -43.34918 | 2026-08-23 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c3a09b72-2c23-3704-8379-49302ea81dc2 | -10.69609 | -47.72036 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7631dbf3-98cb-3b8a-9ec3-4435540647fa | -12.84713 | -48.47053 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d7278396-03e5-3b86-8cc8-f08f0f102b1a | -8.5193 | -55.34377 | 2026-08-23 04:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9606b2a3-dff5-3882-9aa7-d0760f8732e9 | -13.17209 | -51.42882 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| af3e2fe6-95bd-3775-baec-aaf1ed2d15dd | -13.65982 | -51.85994 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 616e7644-a273-32fc-a9c9-f1b612823fa1 | -11.55769 | -46.94625 | 2026-08-23 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a2844d8d-26b0-33dc-b85e-0b582f7b2903 | -12.75781 | -48.38338 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8224f8c-10cc-38b4-ab55-9683d65d5736 | -16.34924 | -49.48065 | 2026-08-23 04:10:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec86cf63-bc36-3500-8b46-c748f79490dd | -11.27811 | -50.7365 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 789a7841-b1e7-3e87-9b04-77d20ced2052 | -13.20163 | -51.4346 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 893aa8d4-b42c-349d-bb3d-baab6aeaca68 | -12.25571 | -43.18377 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 26ced7b8-8cb7-39d6-82cb-2f088768d850 | -14.96275 | -52.65906 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 487bfeb4-9524-3cb9-a75b-ab8bf97d9ac0 | -12.28879 | -43.16749 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a283e919-dc9c-3411-b6b2-bd20e413e3f7 | -16.20273 | -48.74718 | 2026-08-23 04:10:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06452a09-3fd4-360c-b981-b31e6bae4c1a | -14.14224 | -48.0504 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd5c84f3-65cc-3df6-b255-b0f7618b4a10 | -15.76124 | -49.9718 | 2026-08-23 04:10:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba98e3b5-6d0a-3d48-b44a-6698fb676b45 | -13.38029 | -41.34896 | 2026-08-23 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d9b75c34-1ab9-3484-aa45-212d8f3fd01c | -13.66458 | -51.8582 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f52fbd30-2537-3c6c-8c35-d37db9199f5f | -17.40388 | -48.1195 | 2026-08-23 04:10:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9e2ec5f-2656-37da-b153-1e6ccdd123b8 | -12.78266 | -48.38424 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 061d8cec-217c-3e45-925c-cb7b326a1828 | -15.32415 | -46.08239 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a95a0ff-30f4-3aad-8b20-79ecd36cc7d2 | -17.91546 | -44.38633 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad6053af-a581-30e0-b1b9-3b89dcb01968 | -13.66512 | -51.85543 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6857e9c4-4de2-39b3-95cf-9bfbf8c721c7 | -10.30411 | -48.2121 | 2026-08-23 04:10:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9134d566-be3d-336d-988f-993f38ddf955 | -12.75252 | -47.12466 | 2026-08-23 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c9b4c55-ad61-3129-b8a7-5368858a9497 | -12.79075 | -48.38583 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6456895-6d4b-38c5-96bc-f3743c691795 | -12.77136 | -47.12791 | 2026-08-23 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3a1d865-a60b-3733-a5cf-ae0bd045b48b | -8.53249 | -54.84841 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12bc955d-6fa8-3f88-994b-5d5ff28a6ec6 | -10.68804 | -47.71893 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9379bca-162b-3a5f-aeff-d50eb2705d76 | -9.4396 | -51.5975 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb607cd2-b3b2-3af0-b06e-e95bf6506fbb | -16.0599 | -50.43338 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3567a14c-77af-3aca-bf56-1cdb05d5787a | -12.24192 | -43.18515 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8d743666-1032-3722-90f6-a7bfd53ffc3a | -11.43582 | -44.53014 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c827939-b699-350d-b962-f94871499e63 | -11.43862 | -44.53442 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e755c70-0e45-3fa1-9a92-04b2185e0c63 | -12.26785 | -43.12802 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b7a5fc9e-2007-320d-8673-9cf198c79c0b | -15.5583 | -42.65852 | 2026-08-23 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9fb5600a-b9d6-3127-8aaa-16176d6896aa | -16.18747 | -46.48426 | 2026-08-23 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2eb2ea27-0b7e-3a55-815f-590b1facfdf5 | -9.43903 | -51.6006 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d6c2c0e-18ce-3997-88fb-40dd7871b992 | -13.18095 | -51.44375 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5faec7f-944a-35c2-bdd0-effbc4bd8a84 | -14.13364 | -48.05371 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ec9c58bc-5edf-3d8b-be92-91fa379b1d19 | -13.17808 | -51.4241 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 82c19e5c-5b1a-3921-9356-350c736dcba4 | -13.68627 | -51.85376 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73bfc8bb-3025-3cdd-8bcb-ebe4e75dd924 | -10.6989 | -47.72824 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f26df9d6-6701-3fbf-9a40-e6e78e36026e | -14.34284 | -51.77953 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 427ad81f-ea91-3fe8-bcc9-8c25615b45e5 | -12.26372 | -45.07594 | 2026-08-23 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb263982-56f6-3aa0-adf6-7a68fd4062d8 | -13.18918 | -51.42768 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e0037e9c-aa26-3cff-bdea-7251c35a2d2e | -12.73728 | -46.45825 | 2026-08-23 04:10:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 49be4047-77ee-3007-9d91-bf7487d060f2 | -12.59379 | -47.88551 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7a5504d-8a04-3d97-9f06-4e4ac929aa66 | -10.71778 | -47.74406 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1e9572b-8aa5-307f-b035-38efe7f9504f | -11.8525 | -51.67709 | 2026-08-23 04:10:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adfb4343-4c69-37e8-bc41-f6bb498855f8 | -12.26717 | -45.07644 | 2026-08-23 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61079f77-7651-3863-acad-e10ebe062397 | -12.2631 | -45.07968 | 2026-08-23 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3aa4ce2-6fc3-3ec2-8677-0395c4a96d62 | -14.36367 | -51.77771 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c76af793-2a48-3420-8344-9478ff77dc3a | -11.43802 | -44.53813 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df945791-3990-311b-b1c9-d044d21f0bae | -12.82854 | -48.48053 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa5d373c-a5ae-3fd7-b190-6d145999e9d7 | -12.24247 | -43.18163 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b2b29a1d-aaed-321a-af10-75af91a25f4c | -14.34228 | -51.77633 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f3e9aed5-7e54-3f02-bf42-aa54f7a9f8dd | -14.1512 | -48.07029 | 2026-08-23 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7bb8220d-9494-3598-bd0b-efd3b217b229 | -14.31084 | -53.23244 | 2026-08-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6179e50-42c8-32c2-aae2-9cec008252d4 | -14.95824 | -52.65475 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27bef279-1cf2-36b3-af57-9b3216c225d0 | -12.75747 | -48.40941 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b054590e-b4c1-377f-8219-f9d59745527d | -10.45485 | -49.9688 | 2026-08-23 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9988e365-6072-3725-aaef-bf8c033aeb80 | -17.93208 | -44.49679 | 2026-08-23 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9c55e31-4044-342c-bd4b-7a46e71be882 | -13.20065 | -51.44757 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff1342fd-aaa7-3f04-9c18-3c322ce0afa3 | -15.94164 | -44.04997 | 2026-08-23 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eb8c0314-6cf7-32c2-96ea-ed9e0ae1352c | -14.95957 | -52.64805 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 55a0e69a-77ce-39fa-8287-837dc6737c6f | -17.40307 | -48.11661 | 2026-08-23 04:10:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 895b61c6-a793-3c34-b19f-d64338900b3d | -8.52842 | -54.81023 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a2705245-f19a-3f5a-a37a-8cc95ee183fa | -11.20787 | -55.04665 | 2026-08-23 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70a9713b-412e-3432-9e66-a6775806aab0 | -15.20221 | -52.7925 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a8b6cba-d258-3984-9e36-ac7fe6bab6bb | -12.84637 | -48.47489 | 2026-08-23 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5adf0677-39f9-349d-91cb-247ab352f9c4 | -16.05469 | -50.43697 | 2026-08-23 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 03ed89d5-9c2f-37d6-a246-9feb5298825f | -12.75342 | -48.40858 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a203c62-cf5c-39a0-8d25-e7b19141fd67 | -8.53364 | -54.84258 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e84a58e9-00da-3228-8d24-6b5129b73352 | -13.66404 | -51.86095 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 899311e2-9d35-324e-8572-1c93bb3a811e | -13.43627 | -43.84921 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ae67ffd-5a5c-302c-a90a-ef69a0984610 | -8.52734 | -54.81588 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66c70224-793c-341e-8dd5-92a8678b724d | -12.26399 | -43.13101 | 2026-08-23 04:10:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 25f53055-d746-305f-9f0d-d97487040566 | -9.4456 | -51.59476 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f65abfd5-398e-3285-91f3-1f7ccb0cabe8 | -13.44737 | -43.84369 | 2026-08-23 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa3b905d-6723-3a91-911d-d71bbb0aa7a6 | -13.67068 | -51.85364 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b6237b68-6834-3611-a6eb-e3886eb5bb1e | -11.10138 | -49.89402 | 2026-08-23 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0305655b-1c31-37b0-a121-b9c7346a268e | -13.67512 | -51.85755 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b9afc19-0594-391a-9bff-22d823ba285a | -15.2486 | -52.86142 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
