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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e483bd48-4215-3278-89aa-a4ea4daf27a4 | -11.8497 | -51.6859 | 2026-08-23 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 221.3 |
| dd76ed50-a5b5-30b7-8b0c-70bd28f85771 | -12.8554 | -48.4541 | 2026-08-23 14:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 96c8c7bc-ff76-3d2b-8393-c4f90c4f9546 | -14.3737 | -51.8466 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 8764d913-d6bd-36b8-9d00-c771da193f39 | -10.6925 | -47.7393 | 2026-08-23 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 2ebefc5a-3fc7-395e-b705-d5994599a385 | -13.4904 | -51.7475 | 2026-08-23 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| dab02e14-7bc4-3aa2-8832-5dd8142d0eb7 | -16.0509 | -50.4363 | 2026-08-23 14:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 14c7a571-e871-3ccd-bbb6-cdaa7060725d | -19.6483 | -45.7083 | 2026-08-23 14:10:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 9bcaf459-a8ff-3822-bbd6-aaa0bd0c2b09 | -13.227 | -51.44 | 2026-08-23 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 969230f3-7fce-3ff7-a70c-d76a40f2bef6 | -10.6738 | -47.7194 | 2026-08-23 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 17486801-0b48-387e-ad6c-0194592b7d0d | -10.3292 | -45.4028 | 2026-08-23 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f8b9fab9-1727-39c7-bb5d-2b5c7852c9bb | -19.6476 | -45.7323 | 2026-08-23 14:10:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b13d3dc5-fb02-3da1-b514-dabe59febed3 | -14.374 | -51.8252 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| a81c39d4-8c40-3972-993e-c21ed272fe5b | -13.6806 | -51.8511 | 2026-08-23 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| bde67974-08c4-358f-a26a-df32085c61ae | -10.3899 | -50.4198 | 2026-08-23 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a2ab72a4-3118-3d78-a35d-e7b57c427c67 | -14.3365 | -51.7662 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 87eeff35-b5b2-333b-ba27-bda1679f623f | -14.3748 | -51.7824 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 8d5f6d4e-b15d-3087-965b-d6cce08be917 | -9.7141 | -45.955 | 2026-08-23 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 3f039add-3423-325d-8fde-7c7c48d6a387 | -12.2999 | -43.1781 | 2026-08-23 14:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 193.3 |
| 87ed11d2-ac22-3388-93e5-d911d2b62295 | -12.3004 | -43.1541 | 2026-08-23 14:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 137.0 |
| c84fd6ff-d060-38a1-bf05-9b776448908e | -12.281 | -43.1574 | 2026-08-23 14:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 124.7 |
| 7e8ec660-fce9-3ddd-910a-430a87a6e892 | -13.17 | -51.45 | 2026-08-23 14:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74f7dbf7-3caa-31c4-8101-cc4ad29826fc | -13.2 | -51.46 | 2026-08-23 14:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 989b2ad4-735a-3a52-9b57-b83e6135e85b | -14.23 | -45.24 | 2026-08-23 14:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3dcd7397-9dd6-3bc7-bb78-eb9ad59e489e | -11.7852 | -47.2453 | 2026-08-23 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 08740105-bd53-309a-9538-6d9454556f9c | -10.6925 | -47.7393 | 2026-08-23 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| d8c2cfce-c5f3-3ac3-9bf8-e1561710429c | -10.3899 | -50.4198 | 2026-08-23 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ba4d611f-09a8-35be-a564-7948f9535519 | -16.0706 | -50.4332 | 2026-08-23 14:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f61756cd-cc2d-39ca-ad17-6af69cfe38b0 | -9.1332 | -65.9559 | 2026-08-23 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 190.4 |
| 70d9caf5-9234-3ab7-8efd-e3fe2aca7b59 | -11.5804 | -46.9369 | 2026-08-23 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e54e447b-11f1-3f98-8cee-d54b9e07d8ba | -16.0509 | -50.4363 | 2026-08-23 14:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0a364a12-e0df-3adb-894a-d7654ab05951 | -11.638 | -50.5625 | 2026-08-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 4379455c-0bdf-39f9-b3c7-8d891eb0ac5b | -11.9872 | -45.5187 | 2026-08-23 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 79bafd18-d1f9-32f7-8acd-16cbc901ce27 | -9.5181 | -60.5075 | 2026-08-23 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| dfae05d2-8384-3d67-af74-24e05e863457 | -10.8547 | -50.9884 | 2026-08-23 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 1f4d581b-e326-3cda-923f-19a25ea40334 | -10.6928 | -47.7171 | 2026-08-23 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 198c3d74-f43c-3789-b229-94562e080d96 | -8.579 | -54.696 | 2026-08-23 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| bd368e06-cae4-306c-8ae9-3933d4e33593 | -12.281 | -43.1574 | 2026-08-23 14:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 212.3 |
| 6f85b7a8-dc3d-3a9f-aa0e-b4f7933a0339 | -12.0559 | -50.5996 | 2026-08-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| bc4e4728-594a-300c-8694-c58cf6d106e8 | -6.5232 | -51.4488 | 2026-08-23 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8e2c7497-7c76-3345-ad40-5448be8ac369 | -10.3902 | -50.3984 | 2026-08-23 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 247.8 |
| 648228f8-8711-3146-b35d-ea6844d9fd71 | -9.0529 | -45.9167 | 2026-08-23 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 2be05b80-822e-3a72-980e-47a7dda1fbae | -9.4996 | -60.4892 | 2026-08-23 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5bb97fd8-9028-358f-a017-eef664d90adc | -12.2999 | -43.1781 | 2026-08-23 14:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 188.2 |
| 8e5a40dd-6f00-3542-b5ce-ebd13c0e2e5f | -14.5659 | -53.0292 | 2026-08-23 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 9ad28ecc-b0de-3ea4-b0ba-ba4f99e43d84 | -13.6806 | -51.8511 | 2026-08-23 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 451d8c57-769c-3d79-bf1e-0aa9178f901a | -13.6614 | -51.8535 | 2026-08-23 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 026cb141-aeee-32b3-bc16-19ed364898ed | -10.4716 | -49.9624 | 2026-08-23 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e979f1ee-2302-34b1-a0ee-37784b163b9d | -11.85 | -51.6648 | 2026-08-23 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 5bec6fc7-72e9-3565-9906-4f1fb978bd11 | -13.1505 | -51.4281 | 2026-08-23 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2252f3f7-b4e8-3693-98ca-28ab5fcc35bc | -13.6999 | -51.8487 | 2026-08-23 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| f5c1d252-378d-373f-88be-b162fbcf96e4 | -10.7985 | -50.9518 | 2026-08-23 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ec31b394-678b-3e26-b97e-640e08396e0d | -6.1925 | -53.5231 | 2026-08-23 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2d6bd018-76dd-3bca-9640-12f5914219b2 | -5.9628 | -51.9579 | 2026-08-23 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4851e814-6ce6-3973-8464-5c6ef9ae157c | -13.1694 | -51.4471 | 2026-08-23 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| a58f8e85-1946-334c-99af-b732fff2b789 | -13.896 | -54.0092 | 2026-08-23 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 30fce5a2-2e0c-3e98-89f8-fffcf712041d | -14.3275 | -53.4577 | 2026-08-23 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e672fe8f-364c-3f57-a9ab-25689819dab3 | -10.9174 | -50.5565 | 2026-08-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 76242568-187b-35cc-8e5f-c9702ce451a4 | -12.075 | -50.5974 | 2026-08-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d95ba3f5-a47c-3bb7-9446-388fbbdb47b9 | -14.3543 | -51.8491 | 2026-08-23 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 143dd728-6da7-3619-a86c-2e1d9cd40246 | -11.8497 | -51.6859 | 2026-08-23 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 244.0 |
| fbd24134-e2f8-30c6-8c79-736cb74d75d3 | -14.3737 | -51.8466 | 2026-08-23 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| c0c3b8ee-d636-38a1-a3f8-bcf315820592 | -10.8361 | -50.9691 | 2026-08-23 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 776f66ed-319e-3244-9b17-e1e471b768dc | -9.1331 | -65.9746 | 2026-08-23 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 4db18e94-3d8a-306d-a9c2-b8956a0b4ca0 | -10.6738 | -47.7194 | 2026-08-23 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 90ef2cd2-5dea-3988-bc36-e2d696222d0c | -10.4526 | -49.9643 | 2026-08-23 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 84c2aded-55bf-384b-b8e8-7a878a7115b1 | -10.4905 | -49.9604 | 2026-08-23 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 718431e1-98a7-34c7-9eef-d02657cc6909 | -9.4995 | -60.5085 | 2026-08-23 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7d053cb7-6e3d-3eff-bf12-d1a5c5780549 | -10.8174 | -50.9498 | 2026-08-23 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 758136e3-0ad1-355d-a4df-9a7c4da4b17d | -10.3292 | -45.4028 | 2026-08-23 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 3030ffa9-2c49-321f-9efc-6e86091eb6f5 | -11.85 | -51.6648 | 2026-08-23 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 6d4fae1d-e0d0-33e4-9595-509ab206f40f | -6.8992 | -55.6977 | 2026-08-23 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| de22c125-6aba-35a3-a831-98e8e6dfccbc | -10.6925 | -47.7393 | 2026-08-23 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 9b8bb514-cd77-3c66-9ab0-738b51c02eab | -14.5659 | -53.0292 | 2026-08-23 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 36e9212d-0a87-3db5-bf2f-042b73f1c02e | -10.8547 | -50.9884 | 2026-08-23 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f4cc94e8-8625-32ea-af26-6bf958199481 | -9.1517 | -65.9554 | 2026-08-23 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1c8316d1-5318-307a-b005-89b525156ccd | -9.4995 | -60.5085 | 2026-08-23 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 2173046a-bb5f-3b0f-94a6-eee06362f1f7 | -13.5096 | -51.7451 | 2026-08-23 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| b2c15b0b-363b-35c6-9bb7-b451fca3a907 | -12.855 | -48.4762 | 2026-08-23 14:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fa437641-d672-39d8-8155-30983e518e74 | -10.7702 | -50.2519 | 2026-08-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| de87816d-2be3-372d-92d8-08a0e787bc57 | -13.6806 | -51.8511 | 2026-08-23 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 283.0 |
| 052de2b9-2728-3317-8012-01d38f500b4b | -14.3558 | -51.7636 | 2026-08-23 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| b5a2c72c-7239-3576-b7b6-a639e4e22273 | -9.1722 | -59.4629 | 2026-08-23 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| cdae14b8-6598-3e74-8dcc-af97999305fa | -14.9967 | -52.6988 | 2026-08-23 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 654ba3f7-23cf-3034-a795-f57693ef5268 | -10.7985 | -50.9518 | 2026-08-23 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| b3a02989-6bb6-3f2f-bd53-97d92600a28f | -16.0509 | -50.4363 | 2026-08-23 14:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 58bd392b-a644-33de-86ac-75c494317cdd | -11.5804 | -46.9369 | 2026-08-23 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9d8065ac-f6f9-3eb7-9eae-c0c17225886a | -15.6955 | -53.7878 | 2026-08-23 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 44140e3f-7a33-37fd-a814-cdb647a242ce | -12.075 | -50.5974 | 2026-08-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c5899518-518a-3e8b-b93c-2dd7f25f439e | -9.0309 | -50.7394 | 2026-08-23 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| b4510ab4-322a-3a56-b408-5b7f26a79166 | -10.9174 | -50.5565 | 2026-08-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 992e78a2-5fc4-3349-bd6f-34c0fe0a20d8 | -6.5232 | -51.4488 | 2026-08-23 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| eb0a31c7-80d6-33be-bbe1-330ca52bd7ef | -14.3164 | -51.8115 | 2026-08-23 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| d452255a-c9ee-3a46-8574-231022af7d0f | -12.281 | -43.1574 | 2026-08-23 14:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 155.5 |
| 0baa01a5-6a5c-32fd-9241-b980676e2eb8 | -16.0514 | -50.4144 | 2026-08-23 14:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f7b7f8db-1c23-319d-ae97-32bfb3f9884c | -9.1332 | -65.9559 | 2026-08-23 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 260.0 |
| 42543214-0f63-3d18-9337-7199e6851adb | -10.8364 | -50.9479 | 2026-08-23 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 352e4d64-84db-3a6c-9b65-fcb90c3412f3 | -10.4716 | -49.9624 | 2026-08-23 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 645b25b0-f45e-3fc0-b76c-d247834fe94c | -10.8174 | -50.9498 | 2026-08-23 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| df9d61ff-b5c8-3446-9251-b15d193dcb90 | -10.8361 | -50.9691 | 2026-08-23 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 488857cf-6fd4-3d6d-b8ee-3fc450f0481e | -9.5183 | -60.4882 | 2026-08-23 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |


[Clique aqui para ver as próximas entradas](README77.md)
