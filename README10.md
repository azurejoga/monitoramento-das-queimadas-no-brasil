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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e05f1180-8098-32fe-90f7-b2eb02166eda | -3.32806 | -45.64055 | 2025-12-01 04:04:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cf40a810-1ff8-33a4-8046-2fe5a5a24d20 | -3.71206 | -45.9041 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 7bff4902-78ca-32db-8364-1747c96180e0 | -3.21709 | -41.56416 | 2025-12-01 04:04:00 | NPP-375D | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4252ecb-b784-3de3-a105-d8cf60929596 | -3.21304 | -50.1333 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f752fb17-f55c-3c4d-a4e2-0a50e54380d9 | -5.33864 | -43.57068 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a466fe98-1aa2-3974-bde0-4453fbbd82c7 | -3.39257 | -50.24848 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1f72331-32ad-3641-be79-c575fbbe5b3d | -3.25444 | -50.68881 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dff1f2ed-95c3-3cb4-8bf1-da51105386e3 | -2.44228 | -47.08368 | 2025-12-01 04:04:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecb6da8e-fb46-33e7-a681-00891fec58b5 | -4.37803 | -43.15383 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| abe2cd6c-1a08-3b61-8c8a-074c1daa1279 | -3.26197 | -48.57149 | 2025-12-01 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da932be3-dd51-373c-93b8-1a096ed281c0 | -4.3803 | -43.33545 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35c9c820-4102-37b2-9c6b-6148197d6d17 | -3.5991 | -47.27037 | 2025-12-01 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 9e1e2e56-3968-3bdc-acce-81b204e93f54 | -2.3435 | -45.74099 | 2025-12-01 04:04:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3df44add-d22d-3c71-9562-d21e5a866390 | -2.84509 | -45.62299 | 2025-12-01 04:04:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 645702a7-c4a3-3fa9-9943-b8257cd9f2de | -3.19796 | -45.22908 | 2025-12-01 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34972532-a3ca-3bc3-8e76-dce536479904 | -4.38332 | -43.3405 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f8a7e1a-973c-3d17-b290-fb5757666ed6 | -4.60431 | -45.21245 | 2025-12-01 04:04:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 291caf4f-c770-37bb-b54b-db00e80d173a | -3.87944 | -40.77965 | 2025-12-01 04:04:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 73e5bdde-355e-3539-8f49-78e8df4b7691 | -5.33938 | -43.56617 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49b0935b-fdd2-3e6d-b65d-e610909a0b61 | -4.37918 | -43.15669 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a2b962ba-655d-3c9d-b0fb-d607e9f8771f | -5.3274 | -43.56867 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6288c67d-5b5e-30a9-8c5b-b5b525395e43 | -2.25198 | -45.61643 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6322cc2-8244-388a-a1aa-6327729f4bca | -3.1442 | -40.181 | 2025-12-01 04:04:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1876a825-953c-38d8-b2b1-8002b0d542bc | -4.36688 | -43.15203 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 96a86e01-0cfa-3385-a40d-bdf06830f630 | -2.92604 | -48.22768 | 2025-12-01 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23fda6dd-8a86-3a9f-946e-c9c3fc36e91e | -3.26316 | -48.5737 | 2025-12-01 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b67156e4-f614-3b67-b196-c16671cd8d0c | -3.21075 | -50.13487 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 970e860a-eedd-3e6a-8950-01a76f7687a2 | -4.13164 | -43.72349 | 2025-12-01 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e08f885-9272-3063-9529-1d22121f3f4a | -2.24848 | -45.62711 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c8ea123-c568-3bb3-80bb-4d8aa5cbcc39 | -3.70687 | -45.90773 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 643d2a08-7355-3ff6-b72b-ac40ae940f0e | -3.63726 | -42.3489 | 2025-12-01 04:04:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7e34c4e-31ab-3b93-86b1-4deec7bcac8a | -4.37502 | -43.14883 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b3256adb-9f30-38c5-bc2e-93bf64fffad9 | -5.49217 | -42.166 | 2025-12-01 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 99f2f6d7-f617-36c9-84b2-981da69da846 | -2.65149 | -48.55156 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5e693b3-0ba9-32c5-a9b4-d8f4043a7b8d | -4.14321 | -43.72536 | 2025-12-01 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77e1d395-23ba-38ae-88dd-32b33be4dc59 | -4.38782 | -43.33658 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f619c2be-5d3f-376f-88ea-3423a49e7c27 | -5.49155 | -42.16988 | 2025-12-01 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 66541b8e-db10-3acc-85c6-019268d2b7c0 | -4.37991 | -43.15227 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1a52e791-a568-3a24-aee1-71eded21ccd1 | -3.70903 | -45.90741 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b172c2c4-2e2a-3ca7-ab93-d3e79a520ffb | -2.64045 | -48.54617 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb5cff3e-1fd3-3bc8-9bc8-e169de2cc60f | -4.37732 | -43.15826 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 807d4099-7419-3498-92ab-58c52ee61d6e | -3.70533 | -45.90211 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a86a7926-9f1b-3fce-8d94-107cf5a67695 | -4.3758 | -43.33935 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3cba5af-0674-3177-a060-029a62c1d3da | -2.44665 | -47.08331 | 2025-12-01 04:04:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28fc7003-3e07-3cee-bc86-020c5e52cde5 | -2.2499 | -45.61816 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9f269572-bc45-3d9f-93be-9e5c6ce50e5d | -3.71138 | -50.65978 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f910ea44-de94-3b6e-9251-07279109d18d | -5.87986 | -40.83964 | 2025-12-01 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b37f2715-3c9d-3273-89b6-c3f1c7301a0c | -3.57912 | -50.29628 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11fa1f89-d722-38bc-8ac8-e5ef9057995f | -3.21827 | -50.13877 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b13453a3-a376-3998-9b01-37a93907cda5 | -5.23936 | -41.23664 | 2025-12-01 04:04:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce35b6cb-b00c-3b42-ae8c-79cf332e1ba2 | -2.97271 | -49.6343 | 2025-12-01 04:04:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0464ba9e-56f0-34c4-9814-d221e50d72a4 | -2.59638 | -49.2617 | 2025-12-01 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f8e21fc-2a30-3e40-b836-60513f5fab9a | -3.3932 | -50.2534 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc25187e-efee-3bf0-8d1a-a99fb0b6e249 | -4.1903 | -44.76358 | 2025-12-01 04:04:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| accd57a5-2de5-3bf3-9854-825d2b9128ea | -5.16839 | -40.65173 | 2025-12-01 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 38468662-00c4-30a4-87c5-f927cea58d71 | -3.75265 | -42.95919 | 2025-12-01 04:04:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4166f354-9c2b-3043-acdb-8ea2c6b25435 | -4.3713 | -43.14824 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7c563092-c00a-3255-8246-ad886c79451c | -6.51429 | -39.16372 | 2025-12-01 04:04:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c2cfe99b-471d-3b38-8aae-b5e4ed7af9bd | -5.33263 | -43.56034 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1f92738d-d7f1-3b5a-8e7b-c7627816f89d | -4.38175 | -43.15445 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 70459ec8-ac43-3166-a51d-244955d37678 | -3.70759 | -45.90326 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 643d21c6-c629-3d40-b324-f082177a688c | -3.21002 | -50.13925 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 29534b74-0414-311c-8bc6-561d1ae8f703 | -3.26375 | -48.57029 | 2025-12-01 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcd1c8d0-79ba-350c-97e8-b6d906dded03 | -2.74624 | -49.32685 | 2025-12-01 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a58ed1b2-fbd8-3298-8535-3f9103a70635 | -5.33415 | -43.57454 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c4faa621-9d7f-305c-8f38-2f1a5da5fcfb | -4.38554 | -43.327 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c73fc267-6230-346f-b33e-1d34023a1376 | -4.6309 | -43.2671 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09e977ac-9685-3551-bc33-74512d9c4ef2 | -2.60212 | -49.26259 | 2025-12-01 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a78f1a5-edbf-3d4d-9fff-b465728d9d48 | -3.41115 | -52.8317 | 2025-12-01 04:04:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c9a0391-7035-39c3-858e-392a5c8f7166 | -3.9403 | -45.85281 | 2025-12-01 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83d66100-a46b-3dfa-9bdc-81a607f2bea0 | -4.59947 | -45.21546 | 2025-12-01 04:04:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a3664e8-d43c-3e3e-a2d8-e1a52e4fb72b | -2.44725 | -47.08448 | 2025-12-01 04:04:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29fdb283-2d72-34e1-9081-497aab50b682 | -2.97853 | -49.63537 | 2025-12-01 04:04:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2224d678-20b3-3722-a13d-403a9b7d9e2d | -3.70313 | -45.90243 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a06b7472-7d03-362d-a2b3-94bd42d2d852 | -2.73542 | -45.21866 | 2025-12-01 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1722cf23-8785-34c4-ac97-a0f9cb59e249 | -4.08166 | -40.10293 | 2025-12-01 04:04:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7ca0c9e4-ecb0-3209-9271-6eafc5f2c95d | -2.34268 | -45.74244 | 2025-12-01 04:04:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d9bd688-2022-303d-aa6b-1eb0dc1e7e43 | -2.63556 | -48.54169 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8f7a05a-4d3f-3313-9d84-a4ae3aa7e4a3 | -5.33189 | -43.56482 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c6f36a1d-d37e-3b70-a102-c8e298329189 | -2.8414 | -48.83072 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a0e8f6b-cd92-323d-bdb0-9733088aaca1 | -4.25304 | -44.32878 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a59d8646-d0df-318d-bdcf-d2b5975c2ea4 | -3.20927 | -50.14371 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 627b8ff7-6b3e-320c-a941-a9214a60dc7c | -3.70604 | -50.65403 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54a80970-5f77-31c7-bc48-3371611810a4 | -4.39607 | -43.33329 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| baa2f81f-9475-3cfe-a4e5-4f06f0591cd1 | -2.34802 | -45.74171 | 2025-12-01 04:04:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a27dee4c-2604-38ae-875a-bb4934f20abc | -5.52604 | -42.60408 | 2025-12-01 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9ab1f880-daf8-3f4c-bc16-e926642968ef | -4.31412 | -45.37857 | 2025-12-01 04:04:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6adb5c62-d09c-346d-8cd2-b66514aa3544 | -2.75601 | -45.26302 | 2025-12-01 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57719fed-effd-327a-9039-8c2adf913144 | -2.64545 | -48.55407 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8b38123-2084-319b-a2a8-387977b3c5e9 | -3.21601 | -50.14038 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c9371c8f-0016-3a55-9fb2-56429581b802 | -5.73264 | -40.81328 | 2025-12-01 04:04:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 91d741eb-e238-3d87-bc6e-f8e87efa3f8a | -4.38363 | -43.15289 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 78cb1c3a-4bb7-32c5-a48e-2cd9224dee6b | -4.37361 | -43.15765 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2040bc80-a946-3a03-b9c7-72a8a7726b85 | -5.32814 | -43.56415 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b60ddd8b-d873-3fc2-a4fc-c8ab8e2354bc | -4.70144 | -44.40469 | 2025-12-01 04:04:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac8d216e-b503-3464-a23b-e1d1bdaf90f4 | -2.83587 | -48.82966 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| babcd23a-9163-335f-909f-f27a1602b89c | -5.49916 | -42.16715 | 2025-12-01 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5091b908-211f-3a36-92a5-629ac8fa0daf | -4.70061 | -44.40984 | 2025-12-01 04:04:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cdaf613e-9434-399e-a58f-c7364d947831 | -3.21229 | -50.13764 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ef53419-0daa-3d1e-bf49-7645ecaed315 | -2.99394 | -41.47095 | 2025-12-01 04:04:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
