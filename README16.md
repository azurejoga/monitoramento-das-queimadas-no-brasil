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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f08dd7d-73ca-3c87-924d-15e6b6e8b2ab | -7.83425 | -44.2012 | 2025-07-16 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c073104a-9919-3775-9640-c7a6f0e6d740 | -10.31957 | -49.91547 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd5db0df-c526-3df1-95b6-4a4cb4e039ff | -6.67038 | -43.0289 | 2025-07-16 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7bb962a-804b-308a-b94d-edf9c4fcfd2a | -6.88813 | -45.22024 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86db69ee-c034-3cb7-9726-d6ac6e203347 | -7.21089 | -45.32903 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e864d824-1f31-368f-b50d-29facc6c976e | -6.85313 | -42.75249 | 2025-07-16 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e9f04fb-0d66-33b1-9e26-b1e1bf13e065 | -6.93943 | -44.94684 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a8ffada-1d1d-3d4f-9ee3-8829fc3ae9d7 | -6.71011 | -44.32336 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 10354775-949d-31b2-b711-e51609a0c682 | -6.71898 | -44.33201 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e1d0156-e5a8-3e03-b01b-98639f32cab3 | -12.15484 | -44.68139 | 2025-07-16 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bf4c9b2-ae2d-30b5-9fef-65cf9bdcdddb | -6.55065 | -44.68118 | 2025-07-16 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c97f7f55-93c5-3ab1-86b9-79abd5294cbe | -11.18711 | -48.62302 | 2025-07-16 04:14:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e91611e-4b3a-36ef-946b-678b28661bf5 | -8.90727 | -47.34319 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a068a349-e894-3e70-99a5-4b0325eeddf8 | -13.08254 | -43.56474 | 2025-07-16 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fa17ec9-1a76-3ff2-8962-b8cea96b3bbf | -6.94677 | -44.94432 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b298e28-9e28-35ca-8cab-bf0d0d4ba172 | -6.71288 | -44.32742 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 807cb450-ef00-308c-9c8c-5e78a41f04be | -11.58779 | -47.30956 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4347704-d60e-37bd-90d5-a95074c522b1 | -6.41237 | -45.32202 | 2025-07-16 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4223d131-8df5-3224-88d6-851ad4910528 | -12.99701 | -44.8771 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c42c09f-4f42-319e-a5cf-757f4af6b576 | -9.49213 | -40.39185 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0554c5a7-6e36-333c-8d10-233dde2b451f | -7.94579 | -49.65631 | 2025-07-16 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8135c8f6-a88b-3cf0-a50c-a974583da8a3 | -7.25964 | -39.19845 | 2025-07-16 04:14:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 03e8ae39-1678-3451-9bcc-a84b99f4b605 | -6.72175 | -44.33607 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 462f1bc3-bfda-3a1a-b02d-71de725088da | -10.28344 | -47.61509 | 2025-07-16 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 369c5144-a112-36b3-ada8-02d9af0ce83d | -7.35207 | -45.66745 | 2025-07-16 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ffe9b75-23b9-3d86-9156-d2f02748d860 | -12.9904 | -44.87601 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 304cd19e-d1ea-320c-9cce-361fd69bb4f0 | -6.70405 | -43.91383 | 2025-07-16 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d38e65d-5286-3c9a-821e-ea562c433081 | -9.70564 | -56.18803 | 2025-07-16 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1b38b0b-4b0f-36ac-9817-532bbdc8afaa | -12.09953 | -48.19098 | 2025-07-16 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 287444ed-26cd-3fee-9d55-c5e935a5a115 | -10.96391 | -49.2494 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cec91ba3-cd2f-338b-9207-5b884ec48648 | -7.84143 | -44.1988 | 2025-07-16 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95eacce3-efa1-3b41-84cd-5919bbb979fb | -10.56326 | -49.13398 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea12e26-fbda-38d1-bc12-6c4ad156f01d | -7.19366 | -43.11528 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4427c88b-dfb9-3564-84af-b2a716f1837d | -12.47645 | -46.92344 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e428a29-1905-3b31-9b58-89f8d6055c25 | -9.66318 | -49.89277 | 2025-07-16 04:14:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e847ba1-4673-3b91-8f5d-070b5dfed9c5 | -9.70667 | -56.18267 | 2025-07-16 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| daaba580-2219-3920-9390-edae62b803bb | -11.87226 | -55.44941 | 2025-07-16 04:14:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01a65758-0423-31bb-84f2-ba748b3d3f66 | -7.19312 | -43.11874 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| be43c387-e1a0-366d-a8e3-f979045c4524 | -6.73232 | -44.33414 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 38839aaf-75bc-37e5-8ac4-4a39ed0e283e | -9.59826 | -40.60952 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 01bf9f07-e133-321b-a405-48cc9d83cfc6 | -8.33129 | -38.08654 | 2025-07-16 04:14:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 70ca2540-abcf-3b7a-af7b-dd07c2bd6e21 | -6.63332 | -44.5736 | 2025-07-16 04:14:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce945dbb-b9f3-3f3b-88f0-29c086ce4dc1 | -10.31781 | -49.92372 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d194f74-f6e6-3ac1-90dd-189ecaf27144 | -10.89986 | -49.21621 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a2d4e7b-d83a-391a-878d-2458b65d82e4 | -13.12422 | -43.48577 | 2025-07-16 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc70ed02-932d-37ac-ba45-9909cf2b78c4 | -7.9465 | -49.65215 | 2025-07-16 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1390fa0-0156-3bbd-a57b-e993ea19395d | -11.20923 | -49.01513 | 2025-07-16 04:14:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8823e1ce-cf01-3d14-9439-6191346375d5 | -12.41868 | -43.75476 | 2025-07-16 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 239f4def-19f1-3a0b-ad8d-830de17a1186 | -12.29267 | -48.7878 | 2025-07-16 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8468a82-10a2-390b-9d7a-ae57ceb1504d | -7.94453 | -43.86951 | 2025-07-16 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcd8a3aa-c88f-3276-ac6b-550bbbe9ad04 | -7.19918 | -43.12325 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5fc6c4fc-87dd-3930-b20a-57c85a9cca89 | -10.64069 | -49.47641 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5dd3dcd8-fb7d-3540-bf56-084ec923de52 | -11.7428 | -48.52909 | 2025-07-16 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94bef2a1-7579-3ef5-a28d-011776623c2d | -12.73376 | -47.07069 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 539473ce-27bb-3a91-b7f6-ec4723ae67b7 | -11.47206 | -47.30775 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 868b5f7a-655b-3930-80f4-cc55624cbd06 | -6.95556 | -45.49615 | 2025-07-16 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b79e7b8c-caad-3ca5-8fc9-d3a66b9cd513 | -11.99311 | -43.36494 | 2025-07-16 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66669b2d-3b1a-33a6-a140-171fe09bbf4e | -10.56772 | -49.12041 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 81adbb83-6a6f-3d42-ab6b-f59b0e66d255 | -11.95277 | -48.41439 | 2025-07-16 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 36cdfd41-5bea-387d-8035-98765816df25 | -10.22624 | -44.63033 | 2025-07-16 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| caf05f90-472b-3aca-baea-2f66234da608 | -10.89587 | -49.21555 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 566e3581-499b-39dd-a6a8-ba2b428d1232 | -6.70898 | -44.33041 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8c8c10d-8e61-3df0-8900-e808dfa56d1c | -9.05333 | -49.30165 | 2025-07-16 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc0a05c9-7c6d-3c24-a2fd-02c0e95ce624 | -8.88997 | -47.33833 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 215e22dd-973d-3cc2-a19d-3a20036948ad | -8.50244 | -43.3042 | 2025-07-16 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e599305f-11fa-3cc3-8189-7b39792ad962 | -7.50954 | -46.68714 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 461d880b-f796-39d7-8fa6-d960708d9f47 | -8.90653 | -47.34754 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7fbd06b-af69-3224-a04e-ee00ef1f5ce5 | -9.48845 | -40.39132 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ed0adee7-8482-34c7-80db-1f01a409d679 | -8.24534 | -44.92218 | 2025-07-16 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f102dac-b71f-3abe-8ce8-9498c469205e | -10.57033 | -49.11718 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dceb01f1-bea4-365e-8c21-9d1b1cf21226 | -7.83481 | -44.19772 | 2025-07-16 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69b72a0b-0118-34e9-8172-f2bedf7774b9 | -12.02358 | -47.77771 | 2025-07-16 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 943bc3b3-b812-3f2e-85b1-61cb03ea7930 | -7.27268 | -45.29325 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aed5130d-96c1-3ce5-b0f9-6213fcb50b6b | -6.83907 | -42.86419 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28edee91-5677-336d-b11b-19f0197a5a9c | -7.10536 | -43.65417 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c04b0a9-e09f-31d7-8a6c-305c84df07ed | -6.72509 | -44.3366 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 339e3d2b-1473-30d8-98c6-9a5c1607a0e2 | -10.56831 | -49.11692 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 901818aa-7d9f-3881-9d0d-fd769d752a72 | -12.99096 | -44.87249 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65f2e550-cd7b-3925-911f-84d2bc10ef37 | -12.99757 | -44.87358 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1415857-7e29-3427-8bc5-6487077dbb55 | -7.58165 | -46.31971 | 2025-07-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e68b603-44e8-3dac-83a9-e22b766b6462 | -13.54156 | -44.50248 | 2025-07-16 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7359e98a-b4e3-3cf7-85f2-45321dff96e0 | -9.8492 | -47.87712 | 2025-07-16 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d60d86be-4bb5-312c-a42a-e7bd58c72133 | -8.9076 | -47.34584 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6af24b7b-865e-3434-9ead-90b98903399f | -11.45968 | -48.15971 | 2025-07-16 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbf9b94f-8370-3a61-9a2e-876563c4977d | -12.49028 | -46.92582 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 949ae36d-073e-373e-8e21-ad82bc9b7cd3 | -7.04896 | -43.47516 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6804d8f-7026-3558-8206-09fdcdf07ece | -12.42201 | -43.75528 | 2025-07-16 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8037a9b5-a6b6-365a-8251-7ef2349b0474 | -9.42818 | -40.37114 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c1b854b0-1d44-34e3-ab3c-bb80673b8293 | -6.71621 | -44.32795 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2cb18b7-5c23-3a5a-afba-edf576073955 | -6.44423 | -44.9693 | 2025-07-16 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ab38450-b013-3cba-b6be-1078b448bd0d | -7.31576 | -45.76768 | 2025-07-16 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 311972a7-58fe-3cec-911a-8cc77925ee45 | -10.27612 | -47.61385 | 2025-07-16 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c264d072-53bf-3744-be7d-f72494c71f50 | -8.24811 | -44.92632 | 2025-07-16 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94ed59e9-ab98-326f-b9dd-470d85566d66 | -10.56263 | -49.13752 | 2025-07-16 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9fe6855-9302-3bd8-a53e-b71f1f99407f | -14.15752 | -42.8463 | 2025-07-16 04:14:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e7ce7f87-fd79-3a2c-8b03-4469b1599ad4 | -6.87005 | -41.73171 | 2025-07-16 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 09f3e612-b808-308f-ba5f-1399df341fc2 | -9.30178 | -44.84507 | 2025-07-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c393e55-2766-3e8b-bc1c-791548ef06b1 | -8.91168 | -47.33945 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c779a799-940d-374a-a855-1693ebeb20fb | -12.5679 | -48.88565 | 2025-07-16 04:14:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f2152f3-52be-301c-b840-625dc9c64061 | -10.64997 | -44.48709 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
