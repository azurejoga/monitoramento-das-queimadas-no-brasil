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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70fa4a21-0f47-34da-b698-db9d2605ae22 | -12.9552 | -45.1385 | 2025-09-28 09:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 78b396a0-684c-393d-8726-fc819695828d | -12.9156 | -45.1912 | 2025-09-28 09:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 185.9 |
| c340b48c-96d3-317e-9fdd-b53da43ac2cd | -12.9547 | -45.1618 | 2025-09-28 09:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| efb674f2-6555-3e44-845c-5ba7541545ee | -12.935 | -45.1881 | 2025-09-28 09:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 256.2 |
| 3cac9f41-352c-3e5e-8278-4393ef49a030 | -12.9354 | -45.1649 | 2025-09-28 09:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 244.1 |
| 075904d1-b3ad-3a56-b24e-08200e6cf5cb | -12.9156 | -45.1912 | 2025-09-28 09:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 51368558-061b-3b57-9337-4ba5eeffa6d9 | -12.0019 | -47.995 | 2025-09-28 09:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 85fe0674-6208-3c77-b8a0-8461cc6c1c06 | -12.9156 | -45.1912 | 2025-09-28 09:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 352c6e29-e06b-3c30-bc68-086d133b9a01 | -12.9354 | -45.1649 | 2025-09-28 09:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 297.6 |
| bd5a6497-3691-36bb-a134-35903ba428f8 | -12.935 | -45.1881 | 2025-09-28 09:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 495.5 |
| 86ad94da-5351-3491-a60c-b28a35944fc5 | -12.0214 | -47.9703 | 2025-09-28 09:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 387dd485-102a-3496-b4a4-16d814bb4645 | -12.0023 | -47.9728 | 2025-09-28 09:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 6247d945-fd57-36da-b113-d2b13f98efd5 | -12.935 | -45.1881 | 2025-09-28 10:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 7e7f08f6-ed4d-3150-8e83-90004f4cf682 | -12.9354 | -45.1649 | 2025-09-28 10:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 4c1cb4d6-64ea-399e-8676-7c839f4a7220 | -18.1977 | -53.3208 | 2025-09-28 10:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 4a563c2d-1e09-3daa-8b47-cf8c7a7518d3 | -12.9156 | -45.1912 | 2025-09-28 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| ace070dc-be84-3f5b-9a1b-ec2f161b5af8 | -18.1977 | -53.3208 | 2025-09-28 10:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 221.3 |
| bc176826-af6c-3502-9d4b-184fdd6bbaa8 | -12.9345 | -45.2113 | 2025-09-28 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 24a82dc2-703e-3c74-9509-04d2eb9b40a8 | -12.9547 | -45.1618 | 2025-09-28 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| d507ff92-f33b-37fc-897b-db135df63f90 | -12.9354 | -45.1649 | 2025-09-28 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 491.2 |
| 0bff3d0b-7aa5-3a1f-88e1-df4467c5d825 | -12.9161 | -45.168 | 2025-09-28 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 843a1825-8451-390c-bd58-6a0e652fcd1a | -12.935 | -45.1881 | 2025-09-28 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 647.8 |
| 339791d0-909a-32ee-8f6c-621a9a7ec462 | -12.9345 | -45.2113 | 2025-09-28 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 8060c4e0-f010-3181-90f1-143c93aeef9c | -12.935 | -45.1881 | 2025-09-28 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 480.2 |
| 5038c73c-1c4f-3eec-a84a-3c345771a2e3 | -18.1977 | -53.3208 | 2025-09-28 10:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 220.6 |
| fdf064cb-9a4a-3844-b2ab-a0035a137347 | -12.9547 | -45.1618 | 2025-09-28 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| c3f6b2cc-d174-3c58-82d7-ead1350c8ac8 | -12.9156 | -45.1912 | 2025-09-28 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 086aa807-5bef-3a7d-89d8-d4f615175d6a | -12.9354 | -45.1649 | 2025-09-28 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 282.8 |
| 37e8b6fd-befd-3184-8003-da22755ed30d | -12.935 | -45.1881 | 2025-09-28 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 651f7ce6-d74f-3a33-8b7f-a48617cbfb02 | -18.1977 | -53.3208 | 2025-09-28 10:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 132.3 |
| d9b73c02-6cb7-3baa-aa79-7058836c5f97 | -8.8393 | -44.9399 | 2025-09-28 10:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 3df83c93-ed13-3868-96fb-958221c70903 | -9.0916 | -45.8447 | 2025-09-28 10:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 360a2c5f-6797-324c-a43f-bcd8721abd31 | -12.9547 | -45.1618 | 2025-09-28 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 4f66957a-18b7-363f-abb8-c1331b72b309 | -12.9354 | -45.1649 | 2025-09-28 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 381.2 |
| 95024fea-2ed6-32b3-b748-585c66ff0f77 | -7.3849 | -47.0157 | 2025-09-28 11:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 24c33096-65c0-373b-a650-080aba5d8078 | -9.058 | -45.5313 | 2025-09-28 11:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 957620da-dfd1-3280-acd1-9b46865f2cee | -7.3659 | -47.0394 | 2025-09-28 11:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 2fb80902-df49-3f3b-87aa-de71d3162e06 | -7.3847 | -47.0378 | 2025-09-28 11:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 99b0c2a8-1e4c-335c-b2d0-7fb584c9eaeb | -12.9354 | -45.1649 | 2025-09-28 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c3f5f5c9-e117-3609-a24b-1786d0fd8e3c | -12.9547 | -45.1618 | 2025-09-28 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 4404af00-670a-343a-9c4d-ea0231d80b16 | -7.3659 | -47.0394 | 2025-09-28 11:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9b16a46f-02ca-38cf-b16b-ca0a63618e73 | -18.1977 | -53.3208 | 2025-09-28 11:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 9ad3f263-43d6-3429-8c67-75dee2b9a42d | -9.0577 | -45.554 | 2025-09-28 11:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7567577c-9888-3512-bfaa-cce524ec8166 | -12.9354 | -45.1649 | 2025-09-28 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 223.0 |
| f23266d8-9fb7-32ba-a3b7-7396485bd973 | -9.058 | -45.5313 | 2025-09-28 11:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 8390de3d-71bd-3fdf-bf54-63f2decdffbb | -12.9547 | -45.1618 | 2025-09-28 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 235.4 |
| e0614092-ba2b-3c0f-860b-6089cfad708a | -11.979 | -47.0847 | 2025-09-28 11:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5d5e1d41-c3ba-3809-8454-b00c5f166340 | -7.3847 | -47.0378 | 2025-09-28 11:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 6b0077a6-28bd-3bc4-b1bb-07e4567c1e17 | -7.3849 | -47.0157 | 2025-09-28 11:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 351d66d7-3e10-3940-bf7a-10acf10c0cea | -7.3847 | -47.0378 | 2025-09-28 11:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 202.4 |
| c9d4ec48-1011-3a21-bcdf-d61be241ca94 | -9.058 | -45.5313 | 2025-09-28 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 5280c950-a35f-3db7-a40b-530bfcc8e1ac | -13.6073 | -47.3183 | 2025-09-28 11:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 3771da98-5ad7-3c08-b700-2cc889e17d33 | -7.3849 | -47.0157 | 2025-09-28 11:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 06fd0ee5-6b18-373f-9f8d-f7bfe00feabe | -9.0577 | -45.554 | 2025-09-28 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 23df0c64-661d-326e-8f2e-e139810904eb | -12.9547 | -45.1618 | 2025-09-28 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 97c10827-0c5a-34c0-9c42-85bf9eac51dc | -12.2825 | -44.0804 | 2025-09-28 11:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 0ec2d9c0-56fb-3b71-a1b0-bd1106efb74c | -7.3659 | -47.0394 | 2025-09-28 11:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| e540bdbb-58fb-390c-a436-a19b974103c6 | -11.9824 | -48.0197 | 2025-09-28 11:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 447d59ff-73e7-33ed-a9cf-08fa070127b4 | -11.4083 | -46.9597 | 2025-09-28 11:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| a3dc7671-2dab-3635-b63f-555703b21b98 | -14.9046 | -45.5672 | 2025-09-28 11:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d0338a25-d18a-3394-b8ce-3f9d5371e4bb | -11.979 | -47.0847 | 2025-09-28 11:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 939f9ba0-3646-30c3-8b78-248aae2bf575 | -14.885 | -45.5708 | 2025-09-28 11:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| fc7187b1-4fb7-3c01-adb8-bf66c03f2535 | -5.29867 | -43.14463 | 2025-09-28 11:36:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| b019dce5-59ad-3b18-aa2d-1a963a2a44d2 | -6.07474 | -42.45046 | 2025-09-28 11:36:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 46.9 |
| fc13795f-d22e-35d8-80d0-a86294eabf25 | -2.97278 | -42.64922 | 2025-09-28 11:36:00 | TERRA_M-M | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| cb6f487d-f7da-3f8e-98b7-e78857287a6f | -5.37485 | -42.29494 | 2025-09-28 11:36:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| ef83c996-7150-3373-b53d-60ec57d146ca | -5.64341 | -44.93569 | 2025-09-28 11:36:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 03b78d00-56eb-3860-a0ce-dd10894972bf | -5.64331 | -44.92838 | 2025-09-28 11:36:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 32296ef1-dde9-3c1f-9b63-41601d222571 | -6.70743 | -42.76615 | 2025-09-28 11:36:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 1042d7f0-3c23-3880-b6f8-4fa919903952 | -5.2956 | -43.16434 | 2025-09-28 11:36:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| bc87584b-6244-3514-af66-578e69c0adc4 | -2.9722 | -42.65508 | 2025-09-28 11:36:00 | TERRA_M-M | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| dfe30ec6-0631-3356-8825-3f26916aa728 | -5.76569 | -42.83248 | 2025-09-28 11:36:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 35.4 |
| 40d09278-b94f-35f5-96af-502974f7ab63 | -4.94588 | -37.71718 | 2025-09-28 11:36:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| d38fa69d-a02f-3018-8558-ae7b970922b6 | -5.61822 | -36.83232 | 2025-09-28 11:36:00 | TERRA_M-M | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 9.9 |
| be1dbdad-c3ac-3776-8332-a7e076b92207 | -5.75607 | -42.8126 | 2025-09-28 11:36:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 72aa69af-2cd0-3f8b-a703-66ca3bee8321 | -7.5951 | -43.05643 | 2025-09-28 11:38:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 27.7 |
| dade38f4-23f8-3aa3-9b07-c7cb3d3125b4 | -8.83287 | -44.95803 | 2025-09-28 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| ecde8994-d0d7-31e9-b867-3f9c20e94174 | -11.98298 | -47.08118 | 2025-09-28 11:38:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 77b18549-e69b-3ebe-9c81-424c25423bfe | -9.04719 | -46.71415 | 2025-09-28 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 62a7ac44-cda2-3f30-b019-814aca5249ea | -9.06491 | -44.96508 | 2025-09-28 11:38:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 2fddbee0-d5b5-354e-99a2-64c73ea2dac1 | -7.87183 | -44.56437 | 2025-09-28 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c9aeb4c6-3fe7-3d8c-9aaa-7dd8d25a8e58 | -12.29109 | -44.08474 | 2025-09-28 11:38:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| a3078fa4-1212-39d8-875a-92ca78a5acd5 | -8.50172 | -44.73289 | 2025-09-28 11:38:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7a62dcb3-428b-36f9-a61e-0fcc1058f2dc | -8.87192 | -45.02029 | 2025-09-28 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 9576a613-f013-3f46-bdc6-acf73433b5a2 | -11.97874 | -47.08637 | 2025-09-28 11:38:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 181.0 |
| e88aee8a-7add-3879-90c4-4fe8203c449c | -13.47217 | -40.02289 | 2025-09-28 11:38:00 | TERRA_M-M | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 97701af9-3c17-3aaa-8381-de10ee498675 | -12.93084 | -45.20112 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| c74e064f-65c7-3649-82dc-6ed8b91c539f | -12.83349 | -42.55805 | 2025-09-28 11:38:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 843ba6a4-5e7b-3726-a4b0-1e0f22ce3fed | -12.28981 | -44.0602 | 2025-09-28 11:38:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 6aea2831-7897-36f4-86dc-b55813c82146 | -12.9611 | -45.16996 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 061ba7bd-a703-329d-b10a-f1f0f94f435e | -11.72101 | -44.40915 | 2025-09-28 11:38:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 80fc902d-fa64-36e7-b17a-ed0eccbcad77 | -11.68878 | -44.43742 | 2025-09-28 11:38:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8a9e310f-1fde-3126-95e5-aff73c5c6f99 | -11.94967 | -47.89926 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4d77451a-5d13-3840-9be9-89e852f91da9 | -11.36514 | -45.04251 | 2025-09-28 11:38:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| fd19ed0e-b841-386b-b70c-1df271e1d2a0 | -11.94348 | -47.93489 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 9108fb87-e05a-3043-b18b-ca0b26985eac | -12.93437 | -45.18001 | 2025-09-28 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e365f746-f17f-351e-955a-2e1e68b869da | -8.27861 | -45.45845 | 2025-09-28 11:38:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| caeacd81-4059-3375-ad11-435ac4006457 | -8.84205 | -44.94273 | 2025-09-28 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 41adb013-70b7-399a-8ed9-ed09e38b977d | -12.28694 | -44.07786 | 2025-09-28 11:38:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 348.3 |
| 093a9f35-751f-3b2b-8549-d14727c474d5 | -12.92807 | -42.23726 | 2025-09-28 11:38:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |


[Clique aqui para ver as próximas entradas](README95.md)
