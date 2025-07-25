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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e93d7c2-ea74-3115-a052-1f0f276b3a6b | -8.09001 | -43.15179 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| d107c026-5f16-33cb-93ef-9f9649debf21 | -7.89048 | -43.54589 | 2025-07-25 03:55:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccffcd8b-064c-3ced-99a0-c5d8c6837601 | -7.8604 | -48.21917 | 2025-07-25 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 189259fd-c53e-31f6-80f9-ea462f79e7e1 | -6.16466 | -44.5842 | 2025-07-25 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48d7e937-602d-3e90-afed-687c8e9a9884 | -8.1299 | -49.58915 | 2025-07-25 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ad73460-199c-38aa-bd4a-464505975df7 | -9.03639 | -42.68227 | 2025-07-25 03:55:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4b35b003-3ef9-3f83-9dd1-2ee23d0701d0 | -6.06423 | -44.5886 | 2025-07-25 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a512cf7-8db4-3fbb-bc91-17a9cd006c29 | -12.4358 | -45.38001 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 621e16b2-060f-3022-8a75-277f9fce8dea | -7.36815 | -48.13689 | 2025-07-25 03:55:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aabcf7ac-d71a-3e32-b375-e5656b62d0c0 | -11.78016 | -47.32786 | 2025-07-25 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0095748-edb0-3d69-a65b-1ecc414766af | -6.9145 | -44.23178 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b28a7e48-b0ab-3d14-9055-31e6b7c95591 | -6.94894 | -44.56702 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 651faad6-2cec-3605-944a-132008fd0a43 | -11.44619 | -45.12365 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3a57e2f-9c97-3a8b-a33d-610d04faa5b6 | -8.33457 | -44.94765 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62ff9a14-bdff-3af5-adbb-070c5ae20a81 | -6.67242 | -43.96342 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2818f394-4ddc-3fdc-8cf6-d1d99ba3b56e | -6.34056 | -43.74855 | 2025-07-25 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d1e40436-2406-3c20-a29e-817bba6c5b5d | -6.93535 | -42.80495 | 2025-07-25 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b0bbb214-3583-3d5d-b9a4-00d00091df12 | -7.91329 | -44.09201 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7149ccd1-8fb3-3661-ab30-f3b82400cade | -8.06928 | -49.72202 | 2025-07-25 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9736d333-cb4d-3c94-9802-b623b8a2ad53 | -7.14289 | -46.0933 | 2025-07-25 03:55:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99e6debb-8a81-31ac-86a1-e32de97290ee | -7.25042 | -43.06091 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 738e12dd-183c-37aa-a337-5d10418fda0e | -10.50456 | -44.88264 | 2025-07-25 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db8bff72-058c-38d3-83da-9c66082725d4 | -5.73735 | -43.96489 | 2025-07-25 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d263a3a1-bb75-3f53-8a54-2f185307b326 | -7.90641 | -44.0834 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac7273d6-5519-331a-9012-10925f07abdd | -7.91612 | -44.0999 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6e32752-7f14-3a61-a09c-a84842419864 | -8.08155 | -43.15532 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7d7d29ac-316a-364c-987f-31544cc1a25e | -9.00085 | -45.33646 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29d0b7fe-3af2-37c0-8de7-8e1a5c21f6b0 | -7.99728 | -45.03865 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9beea829-8587-3a9f-8d5a-4bddb0ca62a3 | -7.85439 | -48.22172 | 2025-07-25 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d27f3176-6e1b-324e-8735-78e07edc9d4e | -8.89645 | -45.59375 | 2025-07-25 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5379ae2a-9a15-3c06-bcf8-f2f33828573c | -8.89126 | -45.59736 | 2025-07-25 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f7d435d-cc6d-3799-8223-895980af0fc3 | -7.91391 | -44.08841 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d2e719f-8cf7-30eb-a837-0acab874a3fb | -7.24657 | -43.06027 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df3a894f-d967-3750-be06-dee2408c7090 | -8.20997 | -44.93816 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7be6e0f3-4ced-3ca2-88c8-209ba027297a | -8.09766 | -43.15305 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ace011f-089b-31ab-a2d5-14b827dca08d | -6.63763 | -43.96901 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e37a574c-3af9-3020-8be4-b3576c6c96bf | -6.02524 | -44.03837 | 2025-07-25 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2e6609f-1bec-3a7f-abc4-36e242322fab | -8.08618 | -43.15116 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5b353acc-4459-342c-a0f5-572fc74e0100 | -7.92143 | -44.09338 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3f7b2038-3fed-30fe-83cc-2e160c4f1347 | -8.93216 | -47.34475 | 2025-07-25 03:55:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 317223ea-6c8b-3c87-8dbf-db3e8af048eb | -7.11363 | -47.83866 | 2025-07-25 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 304e5558-124b-3e62-98d6-565180fd6486 | -11.45782 | -45.1297 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 730050b8-9c1b-3a3b-a0d0-39c227636a86 | -6.95318 | -44.56265 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3f3a5d56-5777-3289-af69-91e566c48dcf | -12.23174 | -44.63129 | 2025-07-25 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 360415c3-048a-3b81-8b22-cf1997953dcc | -8.92719 | -47.34383 | 2025-07-25 03:55:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9112db34-79c4-3e02-853a-f8c79f6dd519 | -7.21819 | -45.3328 | 2025-07-25 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa1f75f7-14f9-3c7a-a782-07d786e413f8 | -7.91267 | -44.09561 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b151256a-7b98-3797-a9b5-8aa62cb78aa0 | -10.61028 | -45.24247 | 2025-07-25 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 88d6545b-6a7c-3c8f-901e-432b1765ee11 | -12.4276 | -45.37846 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f203813c-675b-327d-8522-6aae6c8f73fa | -7.92487 | -44.09767 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6936c05d-af6d-389a-854f-a3e6d4e72073 | -6.64739 | -43.05054 | 2025-07-25 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e3611c7-a397-35af-8e53-a691c5c1a0a8 | -7.91051 | -44.08331 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 880d3ce8-6d91-36f9-8fbe-cb20880d74ec | -7.16087 | -43.47409 | 2025-07-25 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b967cce5-549f-3572-bd9c-8bf3e32623e5 | -12.25627 | -44.58302 | 2025-07-25 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22aca565-dcc6-3c47-9ef9-f1c695b3de05 | -9.00446 | -45.33297 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3161aee-8e4e-3c0a-9612-ed517dc3cb16 | -8.82313 | -44.51616 | 2025-07-25 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51eddb31-6974-3d94-894e-8e90168c2ced | -11.45439 | -45.12515 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7dd7a849-b6d2-38ab-9517-95947b60d3c3 | -9.00594 | -45.33298 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb42e575-0efb-332d-ae7d-d64e9a93969a | -10.44933 | -49.05277 | 2025-07-25 03:55:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb7a1bc9-3ba0-3476-88c0-66fdb908de88 | -7.24962 | -43.06569 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| c51d1067-81fc-3cc7-bddf-b8bd9422aa8f | -7.92955 | -44.09478 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0df89c9b-330d-387e-ba90-b48856237f43 | -7.91515 | -44.08123 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 829cc233-6add-358a-ae40-20c40ee5b821 | -7.88658 | -45.5425 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 90452a70-102c-3348-b039-41cdca882f0f | -7.94238 | -44.09315 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3df4c43d-0911-359d-9e50-c9825ea213d3 | -10.63859 | -44.76435 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2954a8bb-3dc1-334f-9d8b-20527db95daf | -8.36927 | -51.07948 | 2025-07-25 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 662a1881-776b-3aa1-a5eb-3d6b8883c32c | -8.37026 | -51.07442 | 2025-07-25 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c4b7f589-532a-31d5-9ca3-30596fc4ffad | -10.61586 | -45.23524 | 2025-07-25 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 01e34c0b-a728-3cf8-aa55-b1e4d46e2cb4 | -6.95452 | -44.55978 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 46d8b080-b7a9-3a0c-ae2f-9d034640779d | -6.95456 | -44.55472 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| c7cb434a-7bb5-31e4-88b8-41a1babd739a | -9.02331 | -45.33581 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a1ed94ae-cd93-305b-a6ea-d74e8ea7d59e | -6.6718 | -43.96712 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21ab09b0-fc02-3571-85c6-ef23ce3a3682 | -7.93016 | -44.09121 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2a5ac185-91c2-31af-ba8b-1024a2480907 | -8.33814 | -44.95245 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e422111b-740e-35cc-93d7-812df6b87c20 | -6.95092 | -44.5551 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9da63e8c-b3d8-31f9-8252-aa573fda54b0 | -6.95385 | -44.56379 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f0c1eed4-3254-3146-b9e3-f49593b72de5 | -11.78644 | -47.32607 | 2025-07-25 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfdc5f30-36c5-3bd1-a9e3-387e1b7e79f0 | -8.3303 | -44.94689 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| becf7172-d1e3-3e12-907d-59d4538a873d | -8.28783 | -44.97242 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1b622a1-871f-31bd-ac9b-641572b58cc6 | -9.66067 | -40.59171 | 2025-07-25 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c39e158-5253-3661-8146-38a70662b35d | -12.42627 | -45.38598 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eae14646-3c61-39b8-86e4-34a4378b4314 | -7.90872 | -44.09412 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 137e7c44-13ec-357f-82e3-57b3452d4a5a | -6.99323 | -43.32205 | 2025-07-25 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0652c7e4-808f-3447-a071-8da514128d64 | -8.13494 | -49.58913 | 2025-07-25 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d306c782-5ec1-3ad4-9f0c-cff7b9fec380 | -6.98453 | -43.32579 | 2025-07-25 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| dd4be9bc-e3b3-3ed2-90d2-0ed210aa96ef | -10.50046 | -44.88187 | 2025-07-25 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33fe3291-a99e-39ed-a852-fd40a696c11f | -7.26198 | -43.06281 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 818c131d-8db6-35a2-a344-79b60a43e545 | -6.88835 | -44.20047 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f8443f1-d05c-3b85-a285-d45f03979f30 | -7.88466 | -45.53949 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b974940a-636c-3bf6-88a4-96daa4230fdd | -7.90923 | -44.0913 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 595b4d11-0c50-3fb5-ae3e-a5e49e26371b | -7.8903 | -45.54765 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f1fad8d1-e58c-3ffd-9792-66bfcd3cefe3 | -6.91649 | -44.29547 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4706bda4-9358-3065-a833-bbedb1b6c26a | -7.55361 | -42.16047 | 2025-07-25 03:55:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2311c2d9-b8f4-3efa-a6e3-db81e4049e7d | -7.88287 | -45.53737 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e103d8a-06d0-3cae-b1d5-7ab9dda6fbfb | -9.59643 | -43.87049 | 2025-07-25 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 605ee9fe-2084-3ce7-b45d-2ea73799fba9 | -9.85391 | -44.70701 | 2025-07-25 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb3ac7f2-0979-3c8a-a8e5-bf5a7f64f389 | -12.42826 | -45.37472 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 462a45e9-360c-3c75-b87c-55e9ca091ac4 | -12.42216 | -45.38523 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b561d732-6830-343c-b91b-2b7ccc8c4c09 | -11.46324 | -45.12299 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 9e12d9a1-4c03-357b-bd18-f35ad781220a | -7.99657 | -45.04273 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README8.md)
