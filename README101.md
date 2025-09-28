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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78f48159-d64f-385b-a5b2-12f488d51932 | -18.1778 | -53.3239 | 2025-09-28 13:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 6fee6a44-e5a3-347a-9e12-f8dcecfb6621 | -6.3 | -45.0205 | 2025-09-28 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| c5e6e446-24c7-3e71-9a8f-8d4259f19479 | -13.6127 | -48.0564 | 2025-09-28 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a2474d6b-cc84-3d80-999a-2e5e3b16e100 | -12.6495 | -51.6797 | 2025-09-28 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c3ac94cf-d2b2-39a4-8548-262c56906e9d | -13.6122 | -48.0787 | 2025-09-28 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| a3e1b82d-8b0e-3f38-8aea-47959b3d7625 | -7.1386 | -45.4948 | 2025-09-28 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b06d5ffe-f2a7-3411-8a0b-c0438a717b5e | -12.9156 | -45.1912 | 2025-09-28 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 433.5 |
| c6c4b4b2-02bf-39cf-aa85-8d3ce2c940d0 | -6.6005 | -44.9509 | 2025-09-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 87b38142-4347-3237-b68c-6b639f3cb23e | -11.4409 | -45.0229 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e3b6d437-8c91-35a0-951e-5512def76de0 | -6.3107 | -45.8775 | 2025-09-28 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ec43f7ea-f008-3a7e-b358-027a20a76730 | -14.7846 | -45.7051 | 2025-09-28 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 280.3 |
| e1e3b572-4cd8-3fc9-9563-77b53576a9e3 | -5.1885 | -43.7495 | 2025-09-28 13:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 66c08379-4dc0-38fd-a551-d5052d21b1f7 | -4.676 | -37.6366 | 2025-09-28 13:40:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 193.2 |
| 2e599803-4f52-3831-8bd1-63c44382c72d | -8.1611 | -46.4122 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9ac22fce-0e09-3182-ad3f-37299a91a240 | -12.9552 | -45.1385 | 2025-09-28 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 1f9fb533-a686-39a3-8275-b004ed7f6ec9 | -7.7555 | -45.7324 | 2025-09-28 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 81028a26-3773-3905-a6e5-f273ef1a92bd | -4.6757 | -37.6624 | 2025-09-28 13:40:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1649.2 |
| cc08eba0-42bb-3b12-89cc-610135dc1efc | -9.4194 | -54.697 | 2025-09-28 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| db882d1b-bced-3617-98a8-f15136b5c236 | -8.8393 | -44.9399 | 2025-09-28 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| cfbd11a9-93d0-3841-94b9-bc7a7cb43654 | -10.8242 | -45.3841 | 2025-09-28 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0c145f34-6eeb-308c-9783-d9fa9734a6ba | -13.77 | -47.8987 | 2025-09-28 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b6044149-1f7c-3557-bca4-c4bf815ad113 | -6.5065 | -44.9813 | 2025-09-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 1ed29f6a-1942-3ba5-ab8a-9fead441ad4a | -8.2668 | -45.4564 | 2025-09-28 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 5e781d4b-b29f-36fd-91e1-6b0681d174d2 | -4.6948 | -37.6351 | 2025-09-28 13:40:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 105.0 |
| ea135fa0-1656-3370-b592-695e18daa747 | -8.1608 | -46.4346 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 4fd39989-54e5-3480-9011-e51ff8e0ac67 | -8.2859 | -45.4317 | 2025-09-28 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b0cd31d3-c34c-3427-9dd2-5e01345f3e11 | -6.6178 | -45.0859 | 2025-09-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 512a9d89-8dbd-394b-a810-cbce08b555d6 | -11.4217 | -45.0257 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4d060c4f-f556-3a8b-b073-49039a5ec17c | -14.7655 | -45.6854 | 2025-09-28 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ace3cb9e-64a6-33ac-8800-044d4dc637fb | -13.7893 | -47.8957 | 2025-09-28 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 652e6f8c-3203-355a-ae1f-3b759dff1f47 | -6.619 | -44.9721 | 2025-09-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 184936f3-1ddd-3961-89d2-d75ad96f8d05 | -5.6223 | -43.3701 | 2025-09-28 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 23eb6591-1f85-3d84-8b0f-46e56462bf19 | -12.1072 | -44.2021 | 2025-09-28 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 94a318d5-f365-3a63-82c8-9ca6ae38ca9d | -12.935 | -45.1881 | 2025-09-28 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7986743b-91f5-3756-858b-b3df593b558a | -12.791 | -47.7533 | 2025-09-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 265.3 |
| 70710ee7-0116-36c3-86f9-936446b3c612 | -9.0913 | -45.8673 | 2025-09-28 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e0bb84f6-477a-36d5-86d9-da104682a53e | -11.3846 | -44.9618 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 632cbba1-bb9b-3a05-adbe-89d7fb82ff45 | -12.9547 | -45.1618 | 2025-09-28 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 11615f6e-aa4b-31c8-be4c-82c5703139a2 | -7.3849 | -47.0157 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 5373a32a-f557-3c84-b59f-3f908343fc48 | -13.5929 | -48.0816 | 2025-09-28 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8d22a2b8-bd40-36e8-b1c2-0532fce3e33f | -14.7851 | -45.6818 | 2025-09-28 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 11c9a06b-e21d-3ff1-a5ef-aaac6802f259 | -5.7396 | -42.8461 | 2025-09-28 13:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| f0da2c87-6bd9-3445-a2b9-5fb6b4b8495d | -9.2824 | -45.7104 | 2025-09-28 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 3c6dbd9a-6b79-3f11-8290-e60db67e3b92 | -12.0218 | -47.9481 | 2025-09-28 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0383cd62-7430-373d-a47a-e1251420c965 | -14.5336 | -48.4268 | 2025-09-28 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| f3883ae7-097f-383f-aab1-0ad4e4890e9d | -6.6192 | -44.9493 | 2025-09-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| eff895cf-eab4-3a90-a9bc-4f4cdb70e2cb | -14.885 | -45.5708 | 2025-09-28 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 2348580e-e63f-3c3a-8a91-efcda33c4f80 | -11.979 | -47.0847 | 2025-09-28 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 91b33566-3254-3665-990c-0fe15ca5c4ae | -12.0023 | -47.9728 | 2025-09-28 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 610ce088-ad3f-3b31-a2fb-f61c5319e76a | -6.3105 | -45.8999 | 2025-09-28 13:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| aeecbdfd-965e-3c4e-92a6-673325cd6ee3 | -8.2856 | -45.4545 | 2025-09-28 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| e4f46f77-7745-33ad-b745-e9357b6d998c | -7.3661 | -47.0173 | 2025-09-28 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 63b13124-aa31-3ff9-a2f3-2412ae3f2eda | -9.3013 | -45.7082 | 2025-09-28 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| bce40edd-2c1d-35f0-98b5-f284f1ccd95a | -12.9363 | -45.1184 | 2025-09-28 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 28802dba-0c5e-3356-a46b-ba33e86cc258 | -9.9578 | -43.6222 | 2025-09-28 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1e775168-3520-38aa-9ce0-d0ac586ff543 | -14.5535 | -48.4014 | 2025-09-28 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6d3ae215-3112-3e76-b812-0effb463fd64 | -5.7583 | -42.8447 | 2025-09-28 13:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 825a3dcc-fd9a-3e4d-aade-4b20a3b44fa2 | -11.365 | -44.9876 | 2025-09-28 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 1e17fe66-5988-338b-ba8d-2c09cbb4499d | -12.2636 | -44.0599 | 2025-09-28 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| bee775fb-2790-348f-9cf7-6cbe628de1e5 | -6.2759 | -43.6442 | 2025-09-28 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ce7b8572-cf31-3641-af0a-c198f0946ff6 | -8.8759 | -45.0274 | 2025-09-28 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 9426d9c2-559a-3389-801f-45d081c18528 | -7.1571 | -45.5158 | 2025-09-28 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1d6be437-9972-3ab7-bb9d-3123192eb8bf | -5.9076 | -42.9268 | 2025-09-28 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| bafafc03-b67e-398e-8437-dc6d773e39db | -12.1072 | -44.2021 | 2025-09-28 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0adec7dd-5782-3f18-ae1f-3412ee47d632 | -8.2854 | -45.4772 | 2025-09-28 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 087f5fbb-ca00-3902-b4c2-83c4dad61cf0 | -5.1712 | -48.4792 | 2025-09-28 13:50:00 | GOES-19 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 16b5e045-5eab-32d5-9292-9b8f71a5224e | -14.7851 | -45.6818 | 2025-09-28 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 55ec3609-bff3-32ab-b839-0850a53d27f2 | -11.3658 | -44.9413 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 955438fb-13f8-3a78-a30d-ed71ccd02495 | -6.2762 | -43.621 | 2025-09-28 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 5ccd796d-fcf5-3430-972b-1e0cd0cc4645 | -11.3842 | -44.9849 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 058ba5b8-c491-3788-9e98-3d53b43efe6c | -14.8845 | -45.5941 | 2025-09-28 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| f1d5a46f-c56a-3c01-9204-7c94fb962672 | -4.6946 | -37.661 | 2025-09-28 13:50:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 244.7 |
| 7c4c9ce3-8795-3497-a51e-747d687b8ec4 | -4.6944 | -37.6868 | 2025-09-28 13:50:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 171.1 |
| 504b9a6c-8e45-30c2-bb81-3fe84e0e86f6 | -12.791 | -47.7533 | 2025-09-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 263.8 |
| 67931011-6b89-3178-886e-267384f97b17 | -7.3661 | -47.0173 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 182c8e04-2976-361e-b5f2-74ac8639e3c3 | -13.7893 | -47.8957 | 2025-09-28 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 94d05852-1588-3b36-a81e-4251d726a0fa | -8.1614 | -46.3899 | 2025-09-28 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ada110cc-0d31-3f49-9fea-c096c5a35155 | -7.1571 | -45.5158 | 2025-09-28 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 7697be63-8899-350c-8719-c484da5a76c1 | -4.676 | -37.6366 | 2025-09-28 13:50:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 251.2 |
| 975b6eca-2d59-31e3-b573-7bdd282f5c69 | -9.0874 | -47.6074 | 2025-09-28 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 0a591858-46d7-30cd-81ec-18905c2208ab | -5.7583 | -42.8447 | 2025-09-28 13:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 19346c16-3e15-3800-86d6-6db8ea41fef2 | -11.4413 | -44.9998 | 2025-09-28 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 6451e9a0-14b4-3c58-ab44-1766acce6584 | -7.7555 | -45.7324 | 2025-09-28 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a3bb8664-6fba-3e6c-b5bd-fdb9c86ab692 | -9.2824 | -45.7104 | 2025-09-28 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 28160044-4e0b-3958-b530-9d3d0ba1c619 | -11.7194 | -44.4254 | 2025-09-28 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a4d368f4-4212-3d29-a168-a3599385ad64 | -19.7518 | -50.1034 | 2025-09-28 13:50:00 | GOES-19 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 142.3 |
| d265e031-64e2-350b-9585-04399fc1b960 | -13.7704 | -47.8763 | 2025-09-28 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| ef513b70-ebbb-332a-b93a-ad943195e1f7 | -18.1977 | -53.3208 | 2025-09-28 13:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 1d7974db-027b-315b-a4ea-92d608821359 | -11.9986 | -47.0596 | 2025-09-28 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 1c916d27-89d7-3777-b414-d09829c855d6 | -14.7655 | -45.6854 | 2025-09-28 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 8ef819a7-c3ec-3333-a444-20ce164f8dbe | -5.3057 | -43.1599 | 2025-09-28 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 1c863737-795d-3abf-86fb-32dec4ba3f74 | -11.4083 | -46.9597 | 2025-09-28 13:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 906a16fe-3093-364c-a5a3-70d1f8c365a8 | -14.765 | -45.7086 | 2025-09-28 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| fa42ac50-d894-3ff7-90a1-30ed07ea0757 | -11.9982 | -47.0821 | 2025-09-28 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 47152be3-13bc-3cb2-836a-8f48c518539e | -8.8226 | -46.2115 | 2025-09-28 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 7fe75e7d-db4d-32a1-94e2-b061708ad669 | -9.0422 | -46.7255 | 2025-09-28 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 4097711b-98e8-3332-b5ee-bd67c2956c83 | -9.4455 | -47.6144 | 2025-09-28 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 6ed07680-d463-3089-a89e-f2a8ae447e05 | -9.9581 | -43.5987 | 2025-09-28 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 293.0 |
| ce15b2f9-f0a9-324f-809b-1f6c663d0df0 | -4.6757 | -37.6624 | 2025-09-28 13:50:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1215.9 |
| 0d06c669-d0c3-39b2-b4f5-8ef093810d1b | -8.6442 | -43.9931 | 2025-09-28 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |


[Clique aqui para ver as próximas entradas](README102.md)
