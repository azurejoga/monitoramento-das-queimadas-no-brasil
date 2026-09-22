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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cae6b7de-d193-38a9-ae7b-39ef65b40f25 | -3.68811 | -42.96066 | 2026-09-22 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1da9bf7b-b333-33fd-be7c-728b00675931 | -4.65702 | -42.08702 | 2026-09-22 04:00:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 70f1c166-04d3-340d-bbde-aca63502f4a9 | -3.37625 | -50.41446 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28bf97a7-b64b-37be-8287-a3d1f764afe1 | -1.3801 | -49.32874 | 2026-09-22 04:00:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ee9a435-846f-31f6-9e58-7101bbc43f96 | -3.38924 | -50.44358 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cd6eeae-4538-3a2e-a01c-b44a2c30a9ba | -5.01053 | -38.02669 | 2026-09-22 04:00:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 36a6c51a-5e6b-3bb8-8171-bff2d672f35a | -3.68465 | -42.95649 | 2026-09-22 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 07ed8e54-7608-3954-9b80-65e38d7ee6d0 | -3.44311 | -50.60932 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c97065d7-a6f6-3e74-9082-cb22d4262da6 | -3.8681 | -51.19409 | 2026-09-22 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 252f8fd5-2282-3c0a-830e-9f43b92c1b1f | -4.65332 | -42.08483 | 2026-09-22 04:00:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5ba2e860-be92-3703-b39a-2baeeb730212 | -1.78402 | -47.10979 | 2026-09-22 04:00:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2e10ad3-85cc-39df-81e9-c8122e2de66a | -3.44877 | -50.6166 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc4c2fdd-f791-3a9a-869b-08852a810d3d | -3.68926 | -42.95362 | 2026-09-22 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| cadb2b24-3d82-376d-b3d0-718e061b111a | -5.63314 | -40.87464 | 2026-09-22 04:00:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d8ec1c1f-8782-3471-adbd-5d6ab0ef6d5c | -2.54386 | -48.16236 | 2026-09-22 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f4454ad-9791-3036-adf0-11364aeb9ec9 | -3.86922 | -51.18757 | 2026-09-22 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e14674f-0ef4-35a6-8ce4-2825c73e0717 | -2.16625 | -47.88737 | 2026-09-22 04:00:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d2a7664-4cf9-3583-b896-3051fab294fa | -4.95342 | -45.15265 | 2026-09-22 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92687365-1e5f-3239-90df-54423df00d34 | -3.8691 | -51.1895 | 2026-09-22 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b57c8a3e-2d8a-33e3-9446-4fd7d8b55e2c | -3.43821 | -50.61514 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ae47983-76a0-3885-a26d-7cedd8b4c613 | -4.66003 | -42.09221 | 2026-09-22 04:00:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c170e6c3-6ce1-374c-99e7-8a4a9b23642b | -4.22058 | -40.62283 | 2026-09-22 04:00:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 01be3700-50a4-3e24-b5bc-d0f392a9402f | -4.95262 | -45.15742 | 2026-09-22 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 152f6658-0745-346b-8ba9-54abbe958b03 | -3.68753 | -42.96419 | 2026-09-22 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 17166996-6b95-37d0-9e23-43a87a6f6585 | -3.34174 | -42.77825 | 2026-09-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3059211-939c-34d9-b2ae-afba0ac16139 | -4.83163 | -45.99086 | 2026-09-22 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7375d7e8-003c-30f9-a9cd-7d77703588dd | -3.45267 | -50.61134 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f588f18c-e3ad-3109-95bf-db5b931e395c | -3.3811 | -50.41198 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a8b9f7a3-677b-3b13-bb4c-0dedc136ce71 | -3.34324 | -42.77896 | 2026-09-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a010f93-6b60-3506-ba77-4c6620b65b09 | -3.45077 | -50.60474 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ad50166-d2a5-3cd9-a004-f516e3aadecd | -3.12769 | -51.6056 | 2026-09-22 04:00:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7e1064d-c9f0-3e7f-b016-326765d3df09 | -3.34063 | -42.78522 | 2026-09-22 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 15834426-85ec-3a14-914a-1f490d56bcbd | -3.4498 | -50.61049 | 2026-09-22 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cd5e425-4006-352c-9eb9-467cfdfcd494 | -3.12644 | -51.61258 | 2026-09-22 04:00:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f57b5e1e-7f2b-3cda-810f-afbcc4ef3766 | -4.29781 | -49.12601 | 2026-09-22 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 636d8136-419b-3502-8c67-512310b74159 | -4.21733 | -48.61893 | 2026-09-22 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3605606e-9cfc-379b-aebb-ac5580704744 | -9.8953 | -48.46014 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81c3f559-e605-366c-8466-033c55aee868 | -5.99568 | -44.72509 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a31457e0-2455-3c9c-9669-1e03f226c669 | -7.16437 | -37.71928 | 2026-09-22 04:02:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7982f401-9651-3d13-949d-262653a437f8 | -12.56036 | -45.9594 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b9239cd4-e793-3ab7-9cbb-3c0101358026 | -9.97002 | -50.25665 | 2026-09-22 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76d7e6fd-66b4-35ba-9ab1-6e9d2e49cf1f | -11.85086 | -41.74887 | 2026-09-22 04:02:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1e057fc3-3a6c-38f5-b811-f0941747ead9 | -10.05326 | -44.88482 | 2026-09-22 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a791395-7e82-388e-8388-88e283f76d63 | -5.78144 | -43.77627 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d919281c-37d1-3fe6-b036-cebb45381f67 | -9.38104 | -47.75602 | 2026-09-22 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0592f71-c6a7-3523-9358-d494f27750fd | -12.56386 | -45.96426 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 49fef85c-57dd-3b59-9f23-97c495b7af38 | -7.41574 | -49.84126 | 2026-09-22 04:02:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 650345eb-2d63-331e-b599-5887696cc0da | -7.08419 | -42.07587 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97bc9166-e1c1-3927-a926-1c0612f2d43f | -10.12826 | -45.54637 | 2026-09-22 04:02:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c422a62b-7691-37fd-a66e-c73f99067ef2 | -10.01393 | -45.20312 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d73a3df-1951-39f4-aa5a-37855b670624 | -11.43578 | -47.34431 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac3c3eb3-21e8-3e82-a6b1-b3d8ecfdcf0c | -8.91303 | -50.90376 | 2026-09-22 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63d9aa6a-8785-324f-85ed-7fd19b2de2ba | -5.77998 | -43.77596 | 2026-09-22 04:02:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 621a892f-bd2e-3cf0-81c7-4fed5ced3ac5 | -7.83211 | -45.26204 | 2026-09-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5a0540cc-6e90-3422-a038-02368fc61b98 | -8.09348 | -44.4351 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84a2184f-eef6-397e-9dfe-18d3bc6dce19 | -12.19824 | -47.03672 | 2026-09-22 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5069b5a4-7a6f-3a3b-adbd-36a61e1f860e | -6.78187 | -48.68046 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4f83bfb-de15-37d6-9145-ce5e1e9e1b4c | -7.52713 | -45.4087 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5201af8c-db84-35d2-a235-8911c72faeb2 | -6.44259 | -48.46164 | 2026-09-22 04:02:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc7045b5-fa48-31bc-86a8-dd8cdeb60830 | -8.42081 | -45.85226 | 2026-09-22 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f2bc3a5b-4ea4-3a82-8d7a-1cd16b8c90d6 | -5.38821 | -42.95815 | 2026-09-22 04:02:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 24507e2c-8907-3c6b-af9d-5d50ace85a0b | -8.81146 | -45.37492 | 2026-09-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5068c055-e9ab-3b01-bc2c-dd9b216a7d8a | -11.16434 | -51.11806 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8fa4b15a-75e8-3fda-83fd-9d1beeadfc22 | -12.84603 | -44.34295 | 2026-09-22 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ef00412-5b8c-3894-9863-9f560687567d | -11.1055 | -48.32471 | 2026-09-22 04:02:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a75cb3e-60b8-35be-8560-2d1c76fe4f10 | -6.29436 | -47.65714 | 2026-09-22 04:02:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8ed462e-b68c-307a-bf5a-c5252d411343 | -7.13357 | -48.43418 | 2026-09-22 04:02:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49418988-d8ed-3991-8f31-ca664a885665 | -10.26164 | -49.98681 | 2026-09-22 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 809a148b-b4ed-37e2-94b8-53397e083c3d | -6.90621 | -45.51564 | 2026-09-22 04:02:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c518cfe-efff-36ac-b20a-300723d9d5ab | -12.8432 | -44.34562 | 2026-09-22 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4d27a123-47eb-3724-9c3c-eb01e23ff6d8 | -7.39707 | -44.67078 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3675f090-06de-32d1-bb10-63b4f2d7536e | -11.09337 | -48.27698 | 2026-09-22 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8306384d-9876-330e-84dc-4d2739853714 | -5.60982 | -44.84228 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41242ea3-4868-33cd-8dc4-ea704e6f0734 | -11.38557 | -44.23138 | 2026-09-22 04:02:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3509032-d85b-357e-8f96-b75a603b0474 | -10.38114 | -48.91467 | 2026-09-22 04:02:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23dec29a-9dd4-3436-9183-78d8b1785012 | -11.10258 | -48.31215 | 2026-09-22 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8826a0b3-a028-3c10-8749-79161718f28a | -11.43583 | -47.34213 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d723c31-f9df-38f7-9cad-b4e0931ff335 | -5.85177 | -49.78953 | 2026-09-22 04:02:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a26816f-eb2f-3f56-ace2-f8a04277b669 | -7.88867 | -44.83784 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d2d1b87-aa8e-3cce-a437-2cf72711ea3d | -10.47645 | -51.30278 | 2026-09-22 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6d68e8d4-1316-3874-9813-18ebe55bc31d | -6.00756 | -47.90804 | 2026-09-22 04:02:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef647b62-f8d6-318c-968f-91eb09a06f0c | -10.6955 | -48.72009 | 2026-09-22 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40e7be18-069d-34fd-8c8e-2425ca7fd09c | -8.30571 | -50.38532 | 2026-09-22 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4ef464a-2280-347f-8b9b-d41785d45106 | -7.34449 | -45.34397 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4ba365c-7e60-3315-977e-217d71044a07 | -9.23941 | -46.15532 | 2026-09-22 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 53ed8bae-4f91-33da-880d-142a5a3d511e | -6.92089 | -42.88954 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ec2fdea-a3a5-3cbb-aef1-b042c68899cf | -9.28964 | -44.37896 | 2026-09-22 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3aeef70-2454-3686-a827-92ed90ffda09 | -5.33441 | -43.30171 | 2026-09-22 04:02:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35465eb9-96c1-3c3b-9d9e-732889566b82 | -6.77526 | -48.66858 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8223c11b-9b28-3994-bb23-60421a425bf2 | -11.67311 | -43.46494 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 767f71c0-2b42-3985-abe7-2e25077e34ff | -10.84188 | -50.14836 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a907707c-3aea-3c25-8daf-3a16e20e9c75 | -5.99496 | -44.72931 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af5561ab-6f5c-3d71-ba07-9b7c6e5412e5 | -11.94079 | -46.5143 | 2026-09-22 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a3766e5-a04f-3dc0-99b0-8e8718482159 | -6.88274 | -41.71213 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 484d51d7-9450-3ee7-8c6c-d04270edb421 | -7.10714 | -43.07282 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09a4693a-2abf-36e7-856f-8ea88c4f7e44 | -6.57089 | -44.90086 | 2026-09-22 04:02:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 889abf6a-5cd8-3e04-bccc-96af74248ffe | -5.69682 | -50.01668 | 2026-09-22 04:02:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e25e127c-fe5b-373f-9d92-cb7a7fde7b97 | -10.47558 | -51.30724 | 2026-09-22 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c45ce74d-f25e-3db2-9f32-a096eaa0c130 | -7.82409 | -45.25614 | 2026-09-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 584f270d-0735-3441-99e3-e5645fd32ccc | -5.38905 | -42.95316 | 2026-09-22 04:02:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README33.md)
