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
| 24c66d6f-3605-3604-92df-bf381ce3240a | -8.62242 | -47.4557 | 2026-08-12 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 343a5c96-8202-3360-9c96-c15d6f23a2f4 | -7.37053 | -42.83893 | 2026-08-12 04:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 940d563c-7735-35c8-9307-eba973e1e998 | -8.49003 | -45.41746 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 151aeb02-efac-37a7-a59c-85b6cb022d62 | -6.55019 | -43.12282 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46b61c01-750b-30fc-8340-cd87dffd437f | -2.76796 | -49.46628 | 2026-08-12 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4af954e6-38d7-3f8d-a188-3eb8680b5ebf | -7.19634 | -44.36535 | 2026-08-12 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c258c8b-f662-398e-8752-938a2b011464 | -9.03931 | -47.46708 | 2026-08-12 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc22e432-5c30-3a68-89e8-44aaab50fa09 | -7.31729 | -47.43977 | 2026-08-12 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d467df4-8e33-3c05-b3be-9b69651ebeaa | -6.89271 | -41.94456 | 2026-08-12 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5ff0386e-f0e5-3d6b-9e83-d89a8f8c507c | -8.07329 | -46.52233 | 2026-08-12 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fc4164a-2d0c-338b-8093-98276e42e9b5 | -8.59869 | -45.40903 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 218c6b68-3b0d-34bb-be6a-669215c8a21f | -8.35449 | -45.98193 | 2026-08-12 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 577ddf74-6174-345f-be54-67a30c0ad409 | -2.6904 | -48.20171 | 2026-08-12 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1599d31a-d39e-3857-84ca-7e0889867981 | -8.07696 | -46.52289 | 2026-08-12 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7524189-b37a-3025-b8cb-a4ca4b2ef723 | -6.0433 | -43.8683 | 2026-08-12 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78fd76c9-78e5-3ddb-a2e2-c61bfbf24557 | -3.15251 | -54.60347 | 2026-08-12 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b8aaa33-156a-3920-b02a-2bd0d318788a | -6.99922 | -42.63413 | 2026-08-12 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0608d70b-059e-3801-bb31-a5639264747c | -7.36986 | -42.84373 | 2026-08-12 04:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db28a558-afaf-3d30-bd49-ddbf2e920b69 | -3.84439 | -49.03792 | 2026-08-12 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97dace0a-d351-322a-9f59-5b618465a5e8 | -7.6066 | -42.75021 | 2026-08-12 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 70262979-f1b3-3779-bc62-15f8bb65a773 | -8.64059 | -45.85032 | 2026-08-12 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37b5bb72-a2ed-393c-9599-b164b9117561 | -7.38698 | -42.85583 | 2026-08-12 04:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a859fa97-016a-327a-a8e8-cfd25e6e0681 | -3.49015 | -50.05081 | 2026-08-12 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82a2b003-0f89-3217-86c7-dc9dd61e6a6d | -6.04386 | -43.86444 | 2026-08-12 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 925d027e-c372-39eb-aab8-7c84268dae37 | -7.62852 | -42.76337 | 2026-08-12 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0f081ce9-edb7-35ac-a155-fd5bb2c87e0b | -8.07027 | -46.51741 | 2026-08-12 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 494d066f-9dfc-37a7-93d4-8ef3ea99ac60 | -6.04808 | -43.86506 | 2026-08-12 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47faf479-594c-30e9-8c4e-62b0d1652287 | -3.45956 | -48.81808 | 2026-08-12 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83cad480-e87d-3018-8df9-7a9a5de4b757 | -3.96282 | -43.10527 | 2026-08-12 04:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42556dea-aad3-34d0-bef7-62e7cfc2524f | -6.54062 | -43.12583 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1cef3f6d-34c4-30f6-a554-05c8cb33f951 | -9.13301 | -46.39489 | 2026-08-12 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f754e840-0225-35c6-8324-f5be722e5b98 | -7.74543 | -45.02302 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4407c5b9-03c1-3ac7-a43c-05a3e36fbb04 | -7.00439 | -44.82743 | 2026-08-12 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cd06ba4-f265-3a2f-a07e-e8aab12bd205 | -6.59977 | -59.00614 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b081375-fcc6-327c-b2fe-03a3bab0894b | -7.92748 | -45.11145 | 2026-08-12 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7192023c-f532-3696-89a8-e39d21d3f113 | -7.33047 | -49.59705 | 2026-08-12 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18d0d408-e167-3973-8481-a719833b2765 | -2.41878 | -51.83894 | 2026-08-12 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d66c15d5-ab26-38cc-a2e7-ac8dfb7db969 | -8.48437 | -45.41847 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d4896ed-939c-3023-8333-b55c1fb01039 | -5.73525 | -43.27508 | 2026-08-12 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8feeb5e6-f69e-3c58-9500-a5ebe97f7291 | -8.48606 | -45.41703 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa030ead-797e-38ff-a43c-145ea9b063db | -8.48364 | -45.42356 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac772592-e033-3267-8f49-38146341eb26 | -6.5368 | -43.12076 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79a7aa88-43b7-3a02-a813-41f1200a5c1a | -8.07395 | -46.51797 | 2026-08-12 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2433027-48e7-38b9-b4f0-56978fd2257f | -6.12778 | -49.32838 | 2026-08-12 04:49:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5247256a-b0b8-37fe-880b-eeccedad6f78 | -9.04309 | -47.48289 | 2026-08-12 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3c01506-afe7-3486-9318-9a64f54d3baa | -8.62183 | -47.45966 | 2026-08-12 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2017880b-7e4a-3268-ae6f-cc438018c3c5 | -7.01403 | -44.62035 | 2026-08-12 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75497893-9e81-3257-b2d1-1e368a792985 | -6.54702 | -43.11337 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44e9741a-7f38-3140-81c0-69cdce326250 | -7.02528 | -42.13802 | 2026-08-12 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 09737230-43e9-3dda-a878-624ca826406c | -7.72531 | -46.21804 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38accd0e-e116-3756-a5e8-3436089c18ae | -5.64805 | -44.30601 | 2026-08-12 04:49:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7664fc93-2826-3be7-8100-6c66d00ddbb0 | -8.83323 | -45.95125 | 2026-08-12 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8778040-41e1-306e-9af3-0f4da32d8186 | -2.96243 | -49.26275 | 2026-08-12 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78f86b24-9756-3647-81b4-2c2b7e607e56 | -6.54255 | -43.11271 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 438b0e5e-a7ab-395c-bf51-2f21d44d8d60 | -6.54127 | -43.12144 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6171de83-6651-3fb2-836d-0f2e2920a5f3 | -8.64005 | -45.87994 | 2026-08-12 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65bdc654-6bac-3efe-bf88-e3876617dea2 | -3.05163 | -46.92661 | 2026-08-12 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6c20320-0c39-304d-b724-fc94a6838667 | -7.02757 | -42.13222 | 2026-08-12 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 8f63bad6-a7f7-339c-a0e7-30aef0d09061 | -6.85583 | -46.00659 | 2026-08-12 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4ff48c8-b987-3168-8004-e7e3396989e5 | -9.56948 | -44.5795 | 2026-08-12 04:49:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2fe6d25-a3f8-305a-872d-d8e242986bb8 | -7.72157 | -46.21758 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 756d64e1-8faf-3664-b344-c30dfb53a59b | -9.13743 | -46.39089 | 2026-08-12 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5927b10b-8596-39b4-89dc-f157466ae2f9 | -2.48536 | -48.02056 | 2026-08-12 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 440d16a2-f747-38dc-9e79-4016e1e092ea | -9.04394 | -47.48418 | 2026-08-12 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bb6c164-051c-338c-bc39-f06aebe62b38 | -8.0746 | -46.51361 | 2026-08-12 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4ca70bb-ab0b-3b16-8785-76cd8ac2e407 | -2.68543 | -48.21158 | 2026-08-12 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb6c8fb5-7fb0-396f-8c79-925c922453f0 | -8.36519 | -47.75459 | 2026-08-12 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 9d4aaa8f-02ab-3137-8dfe-b47039383f2b | -3.15185 | -54.60743 | 2026-08-12 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2d12e9c-c42b-395a-8823-fc08611b1a50 | -3.03014 | -48.41118 | 2026-08-12 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7828f28-4fe8-3465-b8bd-e2b43b9b24b2 | -5.64223 | -47.10514 | 2026-08-12 04:49:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5abe3881-c9cc-37dd-b2ce-bb89408539e4 | -2.74411 | -54.59317 | 2026-08-12 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e641860-edc5-3537-b15a-ce1b11ec9049 | -1.8268 | -54.50819 | 2026-08-12 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a8fb57e-cfd5-3dc1-ba85-596eeb0912db | -8.41714 | -49.48648 | 2026-08-12 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07d473bd-9e72-3ee3-b77f-ead5045f735a | -7.00387 | -44.83092 | 2026-08-12 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5b81196-1d53-3ed4-b7af-3288757e2a66 | -2.6893 | -48.20864 | 2026-08-12 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f229b83f-213c-3dd9-bbf0-9b0129acf30a | -5.72755 | -49.14085 | 2026-08-12 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d7d8ac1-8ae3-349e-80d8-7f74169cf3da | -2.77074 | -49.47029 | 2026-08-12 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36c194d0-8081-3294-9058-ace4ba316749 | -6.53744 | -43.1164 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77873080-0e3c-315d-ab94-284a35138a97 | -8.36395 | -46.38582 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4671665d-4f29-353e-9af3-bcc7acb8d8ec | -2.96188 | -49.26621 | 2026-08-12 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fd73ef9-1a67-3b90-b303-cdf7059336f5 | -6.59916 | -59.00964 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6c1182-00d2-3910-970c-ccabc469ddbe | -8.35828 | -45.98256 | 2026-08-12 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 90cd1545-cfd8-371f-b344-238b0583971f | -4.77135 | -41.80033 | 2026-08-12 04:49:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 029229b9-19df-3102-9ac7-530f13506a67 | -5.63874 | -47.10464 | 2026-08-12 04:49:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5962617f-dd75-32c3-9da7-f00525940411 | -6.89199 | -41.94967 | 2026-08-12 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c7bb59d1-013f-30af-b378-a1e080eeb46a | -9.03087 | -47.49854 | 2026-08-12 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01c1588c-f909-3f50-aa90-2b497b473227 | -3.48329 | -47.68596 | 2026-08-12 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bced6b0-ccd1-3ef0-934b-1b260c8875d7 | -7.45602 | -46.14362 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb953076-f6ba-390c-b38e-44bb48e45d70 | -8.07093 | -46.51305 | 2026-08-12 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 547d87dd-cc76-3bd1-84c3-f5420f8b626b | -8.63674 | -45.84974 | 2026-08-12 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01ed2ad3-7922-301c-919b-7bbd204ac477 | -6.54507 | -43.12657 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ba510998-e258-3660-8e93-3af1c072d6f6 | -8.62595 | -47.45622 | 2026-08-12 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d82ab20-2abc-3bee-a861-b769b3c3993b | -6.8942 | -41.93408 | 2026-08-12 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e494930-c217-3ccf-94dd-9c5b5ca84662 | -4.46629 | -45.89874 | 2026-08-12 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 177abbe7-6051-3df2-a9fa-c1f5420b6f79 | -2.48591 | -48.01709 | 2026-08-12 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d0ce8a4-cb5b-300a-84bb-8b5902ace84b | -8.37378 | -46.39647 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 190e7318-88e3-365a-9cd7-6c06795ade7c | -8.49475 | -45.4129 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 036b54b7-e9ba-3884-be95-4acffd008380 | -7.01351 | -44.62394 | 2026-08-12 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff388d6d-72b1-3911-97fd-0eb8d26e63e6 | -7.60128 | -42.75434 | 2026-08-12 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 855e750e-0c61-3f48-a500-948751a7439c | -7.45669 | -46.13914 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README17.md)
