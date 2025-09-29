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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 827045ea-d51c-374d-8cd7-0863d43494cd | -15.28524 | -49.49617 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed98a0cb-9cbb-3785-85ff-54c21c4c7a1c | -9.54957 | -47.77316 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da1e7d6f-4f6a-3d7f-b240-a940dfc26e4c | -11.3581 | -45.06018 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b831f840-c921-3f33-a5d6-182ac9cf0b86 | -13.27164 | -48.45381 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb97a142-7453-3346-8cd1-1b29626a5570 | -12.97184 | -46.85714 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4bb5a75e-87dd-3388-a51a-c14ecbc40e84 | -11.99598 | -47.11035 | 2025-09-29 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4281837-4ffd-371c-b5a4-e0b7aff93cec | -16.40691 | -43.72126 | 2025-09-29 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ec6db01-4615-3eca-8b43-e89a0f43670b | -10.19357 | -46.91655 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f47dee7b-c9e4-31fd-a67d-bad84e26d901 | -11.78829 | -47.61472 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04dad4b1-cabe-35ac-aa8c-e7e034a140e7 | -10.81948 | -47.9423 | 2025-09-29 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71e8fb5f-e704-3133-b061-6caf2ce214e8 | -15.07615 | -48.33951 | 2025-09-29 04:08:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c8a11e5-f27e-383e-95df-d303b0f98992 | -13.63486 | -47.33334 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6450da0a-21bb-3c6a-9019-df337b490a7d | -15.26149 | -47.93958 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e30aa111-883c-31d5-b051-9781978427cd | -8.79069 | -50.79965 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 019a03a4-2af5-36f4-99c9-a95e2421df63 | -8.81904 | -46.1991 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bec51f0-9498-3f4d-8664-1f39a37871d9 | -11.40468 | -44.90739 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 753d7c94-a588-3da6-a04b-4805cc8e6a75 | -14.53217 | -48.42606 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb3357a1-1f1f-356f-acdd-477b7d7b9e0f | -11.36509 | -45.06131 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06a1d4e2-a579-3215-96f4-6c1800bb3816 | -15.29089 | -49.50929 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 792d49c3-32a3-33b5-868a-eef6a46a3ead | -9.46671 | -45.50023 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eddcd4e4-cb60-328a-8df5-6c3faac527e8 | -15.29222 | -49.50606 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 326ce398-e932-384d-8f40-b8adbd6cc84f | -15.61922 | -46.25578 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29b811da-1c02-3070-a8e9-505c9112d474 | -12.91646 | -47.15265 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50b5f20d-7153-341d-9afe-e44c851f7cbd | -11.27052 | -47.18536 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 49db57bf-ac59-38d4-8e7c-7d4d22f886c9 | -12.58101 | -41.29646 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ddbc050f-49bd-3ab6-8ec1-31544dca7526 | -12.42346 | -44.10833 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 350b6dc9-3236-3357-bfad-4aee11ce8f97 | -11.36445 | -45.06523 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ba3f2da-0328-3222-9e88-58cbbc7f5235 | -11.36706 | -44.9408 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b126c72-6fc6-332b-95b3-90e12179cf08 | -14.5931 | -48.27069 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c71d9a45-ac08-312b-9181-26854c3eee74 | -14.82589 | -45.45602 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 217049ac-dce1-3300-be50-1011ebb08596 | -11.62017 | -52.86075 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03db95ee-4466-3e43-96e4-67a80311629b | -14.59002 | -45.01794 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a888e2f-0864-33a8-be1a-dd57e1f1249f | -13.18286 | -47.44915 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c6e9609b-e827-3568-889a-32d20003c2e5 | -10.38982 | -48.15953 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a30fead-2eb7-3037-8d87-5b9785262b5e | -15.70719 | -47.80209 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81faddc3-28ca-33b3-a6c3-a44d953caf6a | -12.02877 | -47.20496 | 2025-09-29 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fea791b-6fb8-3252-8273-f67b6b74077f | -11.693 | -44.47306 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ebf5a84-9387-30f8-a201-7aa5e83d4bf0 | -11.7058 | -44.32971 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5a6f6d0-4890-35b9-829f-6953ea77e44b | -11.71825 | -44.4268 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4efaa71-3246-3d47-8385-0fdfce4fa54b | -15.87337 | -46.83483 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a51168d8-6cc0-34ef-a7a0-b78f2ea5d04b | -15.49336 | -45.87935 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a782f88-2e6b-34d5-85f9-009d2edff176 | -11.44755 | -44.98161 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e25a596-c62b-37a9-8c4f-b3c52d1b59a0 | -15.32316 | -47.90532 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ad47b66-e98a-39d7-a543-a05e994d2d07 | -15.5492 | -47.88059 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93ba59a2-7766-3888-9d83-a760236019d1 | -13.35449 | -47.823 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad5ed8a4-8532-3a5e-8d0d-eec12955dae3 | -11.45825 | -45.00336 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b322837a-658b-363f-8cf5-70d6407a6271 | -12.87912 | -44.68784 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b1a0d40-915c-3dcc-a9a4-f297442f8aee | -12.96582 | -46.39175 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa479e37-727c-3f09-a5cd-735f05305be1 | -11.66895 | -45.35079 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f90d1402-92a6-3e98-ae2b-bab98c14733d | -15.03558 | -46.97116 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07be1096-dc58-330e-9846-4ccfad23556f | -12.96842 | -46.24493 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fcd2553-e2cb-36f7-aadc-053927d6dcb5 | -15.79627 | -45.38651 | 2025-09-29 04:08:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0313d2fa-0c71-3683-a310-8314625d325f | -14.71256 | -45.20974 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d22b0205-84b2-3536-a5a5-45ca61159270 | -15.50217 | -45.88039 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9065beff-d59d-3084-a3c0-e13dfdbd82a3 | -13.59993 | -48.05984 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2a60fcd-9ff8-3891-8e11-ee59e97bf1b0 | -14.7531 | -48.36341 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c50b690-8e21-35b1-89e4-2c2618cbfd00 | -13.24313 | -48.44749 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 774f4c46-7978-3d58-b015-fd3d85ee6f03 | -14.54421 | -48.42816 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78fbb900-b9c4-392e-a62a-ed6dde35bf85 | -11.7068 | -44.43254 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6d34ade-0425-3256-ae93-3d0aec89c53b | -14.2844 | -49.40009 | 2025-09-29 04:08:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb5e5624-09e1-32b0-b66f-991e9998ba8a | -10.39409 | -48.16003 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bfc5e14c-64e4-35ac-9f3e-cd16f51e248e | -11.45478 | -45.0027 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 760c6d42-0df5-3abb-8e6d-7c6c1f345179 | -11.93016 | -48.07185 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9bed7f1f-acff-32e1-b204-d3647b42fbab | -11.65789 | -45.32931 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e04adba-b7c3-3c82-92e1-3e74ccbed3fa | -16.40085 | -43.71656 | 2025-09-29 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc30a672-878d-3b98-a3fa-fcb7d5254540 | -11.93913 | -48.02057 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e505f000-764c-3249-8e5d-e8dfe23844cb | -11.42979 | -43.50882 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd131ea5-6bc2-3fb5-a901-31b7897500e7 | -10.04128 | -50.21235 | 2025-09-29 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26f76883-b012-3933-b4b1-de69783cc311 | -11.90696 | -44.87818 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1809b455-e2ec-32da-af67-363e6015ee4f | -9.79517 | -46.93766 | 2025-09-29 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4e1087a-80cd-3287-9b65-eab2014a7c37 | -14.01455 | -49.63615 | 2025-09-29 04:08:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c3ca68e-38ca-3071-bc9b-3b92c05c3942 | -12.88605 | -46.99283 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99633635-aa92-3556-96ff-8d8de7800545 | -11.8386 | -51.8008 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f53e71a-c5dc-33a2-ad51-86be96e22bd0 | -14.83593 | -45.56509 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2eeac6f-0284-3617-97c6-b92b3df7485d | -15.29148 | -49.51015 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f6fbecef-b126-34bf-8e0b-b1bebb1e7d05 | -11.6181 | -52.85631 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57c58b11-6958-3591-88ba-461799a8c782 | -12.59229 | -41.29067 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ee4a6628-065e-3c44-8c40-2f42653925d0 | -15.79499 | -45.39411 | 2025-09-29 04:08:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae640833-0ab1-32ea-b078-e5145981bd55 | -8.66865 | -49.93475 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9dd834a-6686-36a2-80ce-2d44062a37b7 | -14.58973 | -44.99862 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61bec496-9adb-393c-88ba-22225499d908 | -11.80817 | -48.24501 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cea160b9-a849-33f5-be75-d3edc19dbd0b | -15.5252 | -48.51407 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a6c9f85-c1dc-3324-aaa8-293fe0dbd2c4 | -11.91968 | -44.75839 | 2025-09-29 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8cddba2-f44b-3148-bfc4-503f0bce7577 | -14.67418 | -48.15358 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f93e588-aa7a-3160-b69a-ff2f0e853c3e | -13.83379 | -47.93731 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f89db5b4-f047-3833-8d1a-3e422a39b294 | -15.27869 | -49.50816 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4fc1081-3fdf-3c55-9da1-e1cf4ef73b34 | -12.75733 | -46.86132 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26c8c05d-454a-3d75-a9dc-4274c2861ee7 | -9.86524 | -47.7336 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bae15c50-c2d4-3a42-b5b5-00b1a8d69c2d | -14.58034 | -48.27331 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25f87b9e-734c-3a81-a22d-ce595a00d7eb | -15.70984 | -47.80464 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d71a63d8-b1d2-3c5e-b0c6-23c2cd551f91 | -12.7694 | -46.85863 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daf16dac-f102-3f84-9785-394076ae92e0 | -11.58013 | -45.49064 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4139a10-bf4a-37d6-8ee5-e90f056f55e8 | -14.59126 | -45.01046 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6b5dc3b-a275-3ba2-a8b9-6bf534c06ad0 | -14.76309 | -45.66995 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1ed8396-ca3f-3e63-aa2e-7a0e6a566d32 | -11.45041 | -44.98593 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30187072-3693-3b4b-8153-4abd7b41dc2f | -14.54355 | -48.43184 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d65b14fb-591a-3024-be8e-e6543d8870ff | -11.66993 | -44.29319 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 615b5874-32f1-36a0-ab32-d0a244ef8dc1 | -13.7974 | -47.8945 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d7ccc61-ee57-3a39-88f3-b5ce300babb1 | -13.75337 | -47.91404 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fdc285a-6f44-36d9-9c9b-2ab0ef9bd62b | -13.81137 | -47.93047 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README39.md)
