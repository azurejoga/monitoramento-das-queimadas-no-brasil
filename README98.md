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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bf7b05f-5686-3b6f-afd4-2100be9b47bd | -8.2582 | -51.2032 | 2026-09-14 18:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 82330c47-8728-3b85-8618-6b3b218fbeed | -6.8651 | -55.2807 | 2026-09-14 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| e1d6f859-3f91-3798-9ea8-d9643b1df442 | -3.4003 | -61.3087 | 2026-09-14 18:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 2fc277d0-e00c-3615-bd3b-943e35d5b437 | -3.1632 | -61.1805 | 2026-09-14 18:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| c3a13058-0b3a-3c4b-8f2d-784b77e79a95 | -3.9707 | -60.0258 | 2026-09-14 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| d4074c87-ebfe-3995-8021-e881dcb03f45 | -12.4702 | -41.4294 | 2026-09-14 18:20:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 165.4 |
| 21c6b98a-4728-3695-9cea-0accfced9b80 | -12.4901 | -41.4012 | 2026-09-14 18:20:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 384.1 |
| f73bf585-06e8-30d4-b965-3ed88ede014e | -8.2645 | -45.6378 | 2026-09-14 18:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 719b40db-8357-345d-9855-46e185ad54e9 | -10.9872 | -48.3429 | 2026-09-14 18:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| ea384ea9-e70e-3e55-ae78-80f771af5a79 | -11.1925 | -42.8305 | 2026-09-14 18:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 5d5bd205-9982-3328-823d-2895a31b0537 | -3.3871 | -59.4075 | 2026-09-14 18:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 0aa5c499-06b8-3ddd-bdf3-514359c7b265 | -7.0476 | -45.2311 | 2026-09-14 18:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 5ddb818f-2f94-3fb4-8d5c-f17386755855 | -13.5719 | -51.4605 | 2026-09-14 18:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 524.2 |
| 05b74913-9530-3ae7-a801-b92639666e67 | -10.433 | -48.6474 | 2026-09-14 18:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 61f0ae47-1660-3aca-b151-1aa5df677e78 | -7.1882 | -46.1203 | 2026-09-14 18:20:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 5d6c21ba-5a8e-36f5-ab9c-c7e196652267 | -11.1738 | -42.8095 | 2026-09-14 18:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 129.3 |
| b0b95da5-4e77-33c2-a730-a61a6ef568d6 | -3.2319 | -43.0457 | 2026-09-14 18:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| bffaa3ae-1da1-3fbb-93d7-9e3908552176 | -14.7565 | -41.8411 | 2026-09-14 18:30:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 87.4 |
| f92a802a-1ef4-3d79-8f7a-b6a7c4c80655 | -9.7036 | -54.371 | 2026-09-14 18:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a3e694c7-7e81-3620-b806-2d3b2bd5bb5a | -7.0823 | -42.1107 | 2026-09-14 18:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 122.5 |
| cb264657-065e-38b5-98df-a8d7946cee7d | -11.8365 | -50.0028 | 2026-09-14 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 5bb41ea2-48f5-3712-a8be-310f2a967104 | -6.6021 | -58.849 | 2026-09-14 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3b0be2d7-7b29-377f-a60b-efe5e6177847 | 1.3634 | -56.1031 | 2026-09-14 18:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 13082f0a-8d72-3821-950e-421720cc7943 | -8.8267 | -45.8959 | 2026-09-14 18:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 498a8efe-2184-361e-8f48-6fbb4eb747ec | -9.3753 | -50.1992 | 2026-09-14 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 62569042-fc93-3e9f-8106-5bd5b5e8595f | -12.0273 | -49.9799 | 2026-09-14 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| f99c290a-3f1e-3bf5-8310-f5888f708975 | -3.3994 | -50.7617 | 2026-09-14 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f0aa8ac7-cba7-34dc-82e5-325378d842bf | -7.6193 | -46.1495 | 2026-09-14 18:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c4716e55-7d4e-3b92-903b-1fe4e8559b58 | -9.6082 | -46.7535 | 2026-09-14 18:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b57193f4-27a9-3052-a966-2f25b1fe6422 | -8.2582 | -51.2032 | 2026-09-14 18:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 19024c53-2998-3c9b-9a7e-9518baef3273 | -10.0293 | -52.12 | 2026-09-14 18:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 155788b0-cffb-31a1-9c3e-6306085bb4c9 | -9.6086 | -46.7311 | 2026-09-14 18:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 98c004bc-fd5f-3a85-8f55-1948dcb90ca0 | -3.1998 | -61.1231 | 2026-09-14 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 68a2ba60-63cb-36b9-8c4e-9b2d6a82612d | -9.1708 | -50.0049 | 2026-09-14 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 06416368-7316-3832-a7ac-de7ead3a1c68 | -3.382 | -61.309 | 2026-09-14 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 8019f41a-495c-3a93-801c-35fbec14d93f | -1.861 | -54.4315 | 2026-09-14 18:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 917a538b-834f-35ee-9761-39ef46aeeaa9 | -11.2391 | -43.4413 | 2026-09-14 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 1234d78a-d6ee-3eda-b350-3be019006c30 | -13.5526 | -51.4629 | 2026-09-14 18:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 85095c66-af2c-3cbc-a655-cdc0e1d17946 | -6.1597 | -55.6938 | 2026-09-14 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 263352f0-0132-34bf-a646-43ad1db17503 | -8.031 | -39.0035 | 2026-09-14 18:30:00 | GOES-19 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 118.8 |
| 29f9b3df-6e4a-31f1-962e-3069fecb75b6 | -7.0862 | -41.775 | 2026-09-14 18:30:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 167.6 |
| 649fd4b7-bb0b-357c-b294-fa8c7c505d80 | -3.4241 | -59.2343 | 2026-09-14 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 82d0ac62-ab3a-31b4-b04c-0ccb7ae2a8c2 | -3.4003 | -61.3087 | 2026-09-14 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 65693e29-80a5-3338-9c36-bc4fe2209180 | -12.4896 | -41.4259 | 2026-09-14 18:30:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 383.4 |
| a43bb51c-0650-368b-8799-4d90e83d28c2 | -3.8552 | -51.9898 | 2026-09-14 18:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 212.5 |
| 21a83e30-d9d0-3e79-b172-eb93e2029c20 | -9.3572 | -50.137 | 2026-09-14 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e9e7522f-c6e3-3c84-bb64-3ab8e14ca059 | -4.5229 | -54.9639 | 2026-09-14 18:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 100ecf0a-74dd-3ade-8da2-81e56b6c86b3 | -10.6641 | -54.1491 | 2026-09-14 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 419.8 |
| eaa85d87-093c-32ab-a4e7-381e5f579e47 | -7.0471 | -45.2765 | 2026-09-14 18:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 7ea07bcf-6ebf-34b4-93dd-104d3b3d13a1 | -3.8958 | -60.5794 | 2026-09-14 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e77138a9-63be-3308-b92f-93a1b136f7d2 | -3.3306 | -54.1805 | 2026-09-14 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 9e0c7406-5049-38c8-9f60-9733a48f37c0 | -3.4186 | -61.3084 | 2026-09-14 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 2bc79d0d-0951-3c16-b591-66a77de09542 | -8.7889 | -45.8999 | 2026-09-14 18:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 5ff9f496-fa0a-36c5-88ac-781c0e528ba2 | -5.9803 | -52.1015 | 2026-09-14 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 5651eafd-649a-3761-b6ae-aa45914da748 | -5.3635 | -50.1742 | 2026-09-14 18:30:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 10549167-2d3a-3303-be45-85088fd4bc47 | -3.5336 | -53.9939 | 2026-09-14 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 477244a5-9207-331d-b66a-fedc383fc583 | -9.4139 | -50.1103 | 2026-09-14 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7bc09fd6-a4fc-3315-b85d-9a0a83130cb1 | -11.193 | -42.8065 | 2026-09-14 18:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 139.8 |
| 6f6f1eb9-a2e9-38fb-b12a-a2b96e88952c | -6.8632 | -55.5601 | 2026-09-14 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 2e31a58e-a90d-3767-a40c-1bb581d1ad65 | -11.1738 | -42.8095 | 2026-09-14 18:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 1e85f7df-0f71-3afc-8d60-636eb995ad04 | -1.7316 | -54.9518 | 2026-09-14 18:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ff5b7d5d-045f-3350-840a-004e6243dd85 | -6.3434 | -55.8442 | 2026-09-14 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d5504fe8-8d2a-3e41-9b89-d02e7f80ad4d | -5.1255 | -55.955 | 2026-09-14 18:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| fde1c9fb-89af-3127-98e8-f295fc32bf61 | -2.921 | -50.3999 | 2026-09-14 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 3d19b3b2-e783-3791-a7e4-1e6f37cadcc1 | -11.8362 | -50.0244 | 2026-09-14 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 53b2e39e-064a-3c04-b445-d922b15f6cec | -3.1266 | -61.2188 | 2026-09-14 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 2456663f-3c93-3b87-af4e-8cdec6c2da35 | -3.3871 | -59.4075 | 2026-09-14 18:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 63a88d9a-10b1-32e1-b5fc-056a43512fe0 | -9.3755 | -50.1779 | 2026-09-14 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 9226bea7-6b86-3de1-a062-0d7a488116fd | -3.1816 | -61.1045 | 2026-09-14 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 9da3824c-be01-3528-80ff-d7840ea858cc | -3.3638 | -61.2904 | 2026-09-14 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2561c004-f5cb-3588-bf4e-e898b18a06e8 | -8.505 | -54.6404 | 2026-09-14 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7108bf1c-43a2-38ad-9dc4-66a9e11d3e55 | -10.6455 | -54.1303 | 2026-09-14 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 7914af1a-c706-3399-83a7-46689e897405 | -12.1093 | -50.8499 | 2026-09-14 18:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 3af47146-256e-3fc2-802f-dd2f48bd44f7 | 4.2788 | -60.9505 | 2026-09-14 18:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d61edf85-900a-37c9-a43b-3677724f5dd6 | -3.7645 | -61.7548 | 2026-09-14 18:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| d9c44f94-536a-38f7-acaf-c10a001fc290 | -6.8067 | -43.1779 | 2026-09-14 18:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| aa30e98b-57fd-39fe-8d48-890cd37f2023 | -12.1265 | -44.199 | 2026-09-14 18:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e4ea6a3b-3e95-374a-a6a5-1f73050d5314 | -5.8021 | -53.8061 | 2026-09-14 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| f92adaac-74f8-3c8d-a864-8aad77cc77bf | -9.6275 | -46.729 | 2026-09-14 18:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 600b0c86-e5e8-3ec8-ba1e-32e0e23cbe2d | -4.4546 | -39.3567 | 2026-09-14 18:30:00 | GOES-19 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 115.4 |
| bf54425e-1f2d-3d78-b9a7-db3ec84c007b | -8.8078 | -45.8979 | 2026-09-14 18:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 43582262-fa8d-3c8b-be36-02d5e0787c5f | -6.1109 | -57.684 | 2026-09-14 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 292.4 |
| 4cd79315-e8d3-3d9b-b7af-46a2abea70ec | -11.1925 | -42.8305 | 2026-09-14 18:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 99.9 |
| dc8a55d0-0b8b-3f3a-809f-2cadd6387eef | -10.6431 | -45.9999 | 2026-09-14 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 6b671dd6-30b2-316b-a8f6-e6ba4f02779e | -8.638 | -44.4567 | 2026-09-14 18:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 2349e258-6b98-3eea-b814-5664fa74b127 | -8.4685 | -50.7658 | 2026-09-14 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 38a55b39-7280-313b-a4c0-5479a0ee60fe | -3.9707 | -60.0258 | 2026-09-14 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 04a24b8d-4e5c-38fd-bde5-eeefeb02e602 | -3.7129 | -60.6022 | 2026-09-14 18:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| b1b038ec-3154-3149-a1cb-48d8aff63c5c | -7.1051 | -41.7731 | 2026-09-14 18:30:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 2fa00b1f-ab51-3226-88d1-1043d1220367 | -13.5719 | -51.4605 | 2026-09-14 18:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.2 |
| c2cf04fa-08c5-3fd0-8c09-70ae40d1f544 | -2.8839 | -50.4428 | 2026-09-14 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 87a6d8f6-e2c4-3d79-b7a9-1b743a439094 | -2.9395 | -50.3994 | 2026-09-14 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 84df6924-404f-3b27-ac09-a4f515f71ebf | -12.0902 | -50.8521 | 2026-09-14 18:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 35f8686c-e057-3ab8-99d5-9082381ef84a | -9.4513 | -50.1282 | 2026-09-14 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| d17a79af-e5ba-3e95-8dee-b5bd1daac84b | -11.383 | -43.9614 | 2026-09-14 18:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7b9d225a-eda6-3cbe-a5ff-607a4670f29d | -6.0925 | -57.6847 | 2026-09-14 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 5ed5abe1-8829-3e8c-9685-22fc4fb8fecf | -6.3436 | -55.8243 | 2026-09-14 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 83f06a90-aa74-3e5f-89e3-021b8ecd5ff8 | -5.6498 | -51.6641 | 2026-09-14 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 7b9bc1f8-1ee5-3716-aa70-a67f1ac29220 | -6.8651 | -55.2807 | 2026-09-14 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 425b70c7-d46d-36df-be9d-a5cb8444f65e | -6.4035 | -44.0273 | 2026-09-14 18:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |


[Clique aqui para ver as próximas entradas](README99.md)
