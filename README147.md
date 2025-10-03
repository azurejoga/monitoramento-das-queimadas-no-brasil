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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b525342-8a11-3813-be84-65c4a418b425 | -11.1271 | -47.8856 | 2025-10-03 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 1fae5181-2dad-39be-950a-a16dcb5b0131 | -13.1727 | -47.8987 | 2025-10-03 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 04e1a464-0086-31c2-a7c4-6ecb6c832b61 | -8.8343 | -46.7694 | 2025-10-03 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a1f09c57-9e97-3978-8eff-1ae2b5d9357b | -17.6331 | -44.4626 | 2025-10-03 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 221.0 |
| a6e7a1ad-57c7-3fbf-8dbb-c90d90a40506 | -8.5959 | -44.7833 | 2025-10-03 13:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 63674fe0-acb2-3455-a5ed-0c375cf34584 | -12.6131 | -46.9725 | 2025-10-03 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 30c99a83-7745-3628-a7e6-684d72d0f3e7 | -12.9314 | -46.3818 | 2025-10-03 13:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| e4346af4-240e-30df-aa86-3a7a5935999c | -13.3418 | -48.1188 | 2025-10-03 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 271.8 |
| f7f3d6c5-e497-3928-b66a-d7705a799465 | -16.7717 | -43.9601 | 2025-10-03 13:10:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 15f7c50f-c682-39e8-9826-803d3d164232 | -11.8818 | -44.9815 | 2025-10-03 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 7cdcb365-2686-32b4-854a-bf2642de22b4 | -10.345 | -48.176 | 2025-10-03 13:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 83029e9a-19a3-3744-a4ae-d09b63c46d86 | -10.0278 | -44.0108 | 2025-10-03 13:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| f7484dc1-24a3-3d9b-a6ca-5088b11989e5 | -7.3101 | -45.2531 | 2025-10-03 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 7c7dad24-ff94-3f0d-afc0-1462ddf4aa92 | -9.3547 | -45.951 | 2025-10-03 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| bfd4b34b-2eee-3a76-8785-98c76b92eb73 | -10.1759 | -45.4906 | 2025-10-03 13:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| e07fe8fa-394d-3ba2-a9e7-8c11a988c214 | -8.6908 | -47.7126 | 2025-10-03 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e2d3c1f8-d087-33cf-a53a-e18aa08d6d71 | -9.3354 | -45.9758 | 2025-10-03 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 94683a4e-bce6-3f2e-bd25-3d2fe0f41d26 | -14.3904 | -45.9369 | 2025-10-03 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 06687f03-4646-344c-9534-ff10446ffe32 | -10.948 | -51.0846 | 2025-10-03 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cc7c099d-207e-3018-9ccd-f977abeb5f5e | -12.7627 | -50.5567 | 2025-10-03 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| fdb90fab-aeda-3fcf-bdc1-3fcb19aa7d4e | -10.1763 | -45.4678 | 2025-10-03 13:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| eae6d37a-d211-3eef-889b-81ff3d51cdad | -8.9118 | -46.6052 | 2025-10-03 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 90fa81ea-ea62-310f-8d14-7d6ab2b5cdb9 | -12.5305 | -47.2988 | 2025-10-03 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 22773195-ba67-3ede-b89d-86f45be48e15 | -11.9159 | -46.3044 | 2025-10-03 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 232.3 |
| e79e536a-7bf4-3de6-a3d3-0c81c9a11a61 | -10.1273 | -50.2971 | 2025-10-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 3aa11501-3a6e-324f-a6dc-29eccdb521e2 | -17.6338 | -44.4385 | 2025-10-03 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 2c785894-f4b5-3913-9734-71f279644816 | -10.9554 | -46.7044 | 2025-10-03 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 3dd3d616-586c-3bd5-943a-1babf94dab71 | -8.1728 | -47.0119 | 2025-10-03 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0dce6ea1-8146-3256-b8af-dce026a12a2d | -9.8769 | -47.8324 | 2025-10-03 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 1514871f-0f49-39a6-b47d-8ab69a279ccc | -10.2781 | -50.3032 | 2025-10-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 5ea9f784-f68f-39a8-bc15-9d69d9209d23 | -11.1275 | -47.8634 | 2025-10-03 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 52779df3-e179-3e26-b21d-900de75ad694 | -10.1095 | -50.2135 | 2025-10-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 1bbaa62e-4f9e-3352-82f9-5f372801e189 | -9.8772 | -47.8103 | 2025-10-03 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 205.2 |
| c81d3c1c-c636-3510-8c02-887118ad6c51 | -14.9055 | -48.2779 | 2025-10-03 13:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 64e337f2-7e9c-314d-9edd-440a10b7af18 | -10.019 | -48.4964 | 2025-10-03 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ba5a2b54-d489-30f3-9748-20b5d0488153 | -13.7858 | -51.3047 | 2025-10-03 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 8654a781-3a2a-381b-977a-e74f4972b2b8 | -10.127 | -50.3184 | 2025-10-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1b8fd47b-ff61-32a6-8903-c5e3627f195c | -8.5389 | -47.8368 | 2025-10-03 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e4356c6c-5e46-3125-8bb0-f2c8aec55435 | -9.9182 | -43.7212 | 2025-10-03 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 157.6 |
| 5ee80e6f-10f5-3eb6-bdfa-c2f9e8289c7c | 1.48586 | -55.84024 | 2025-10-03 13:14:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 50c47cea-adb7-386a-a1de-7e73d88e7261 | 4.55263 | -60.70618 | 2025-10-03 13:14:00 | TERRA_M-T | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88293a1c-e711-3060-a709-7938819499ce | 1.38364 | -56.47292 | 2025-10-03 13:14:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2bd7cd9a-069a-39fb-97a1-be0a2056dd3f | 0.68462 | -55.95209 | 2025-10-03 13:14:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 31480e84-81bd-3b6d-b65b-25a805272825 | 1.36898 | -50.71809 | 2025-10-03 13:14:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 87992182-48f8-347d-a023-b6b9719ddd8d | 1.78116 | -55.82127 | 2025-10-03 13:14:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| be0f6324-799b-3a77-b361-f44c37eeaa6f | 1.52612 | -55.88975 | 2025-10-03 13:14:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6a56858a-e2e8-3a58-b69c-51fda4ca339f | 1.51341 | -55.87794 | 2025-10-03 13:14:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 18bbe2f0-0c83-35e3-8283-e2b9f1d5ea51 | 3.91517 | -59.66705 | 2025-10-03 13:14:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d22cbd31-3307-319a-b492-ea59b453da6e | 1.51537 | -55.89147 | 2025-10-03 13:14:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 49667cfa-aedb-3941-9f9a-381c795ae1e1 | 4.16368 | -59.72084 | 2025-10-03 13:14:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5c6a85b6-9dff-37e3-868c-6b7065f199d9 | -7.7746 | -47.3792 | 2025-10-03 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0c5a69af-8a44-36d7-b52c-9670d43bcb5b | -14.3904 | -45.9369 | 2025-10-03 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 7cfd1f6b-92fa-3899-a264-acfb17d63b72 | -9.3547 | -45.951 | 2025-10-03 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2f5a599c-716d-3237-bb81-32d0335f8c06 | -9.9186 | -43.6978 | 2025-10-03 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 80e4b72f-cdcb-3df2-a19b-2eba6d7f3a32 | -9.8769 | -47.8324 | 2025-10-03 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 939a63f8-a477-3b68-bb30-a5866322139a | -13.3418 | -48.1188 | 2025-10-03 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 255.3 |
| ca153d9a-dfb6-31ca-a27b-6a3faf7efd74 | -8.1728 | -47.0119 | 2025-10-03 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 34371ddc-0b0d-3081-8938-3007074846d7 | -10.2781 | -50.3032 | 2025-10-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d4509c33-c77b-3b3c-8b29-794942491b8c | -10.1095 | -50.2135 | 2025-10-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6261f11d-0034-3cdf-b548-de3736882040 | -17.6331 | -44.4626 | 2025-10-03 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 276.5 |
| b7f6284b-8025-34b6-a541-6eed72560193 | -10.345 | -48.176 | 2025-10-03 13:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 52ea7d20-3026-38a6-91f8-9b096ccb754c | -10.0903 | -50.2368 | 2025-10-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 1dd96b0c-c145-3137-9f64-373d5105b468 | -10.0717 | -50.2173 | 2025-10-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 038fb716-2eb8-3d79-a853-d1fd99b19463 | -9.8772 | -47.8103 | 2025-10-03 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| b38b6fbe-c884-314c-abce-6b4dee92ee9c | -10.9483 | -51.0634 | 2025-10-03 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e0831151-a3e3-31f7-a16d-1d1b672ed8bf | -11.1271 | -47.8856 | 2025-10-03 13:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 5796b1d3-972d-3f2b-81c8-f2218cf6a5ea | -12.9314 | -46.3818 | 2025-10-03 13:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 4566be2c-a66a-3757-be58-974507bc02c3 | -11.8814 | -45.0047 | 2025-10-03 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 2554f269-8d1c-3ce8-baba-bd77396ea0dd | -9.3386 | -45.7493 | 2025-10-03 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ca0519ea-af06-3a65-bb70-12d639be35d7 | -7.3101 | -45.2531 | 2025-10-03 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1af9f2cf-34c9-372a-8370-cd396fd90057 | -8.9118 | -46.6052 | 2025-10-03 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 354c89eb-79b4-3ba7-875e-6cfec0866f25 | -8.5959 | -44.7833 | 2025-10-03 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| d4d1e13b-1618-383e-a78e-31f56dcbd057 | -13.2168 | -50.8856 | 2025-10-03 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 229d03d3-2dbb-35e5-b013-3159a0e2467a | -10.0278 | -44.0108 | 2025-10-03 13:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 14d06975-ae2e-3778-94f1-adbd4543e0d4 | -14.0037 | -44.9376 | 2025-10-03 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 227.6 |
| c4cb2d84-51b7-3970-a8b3-b080ef4e57d3 | -12.6131 | -46.9725 | 2025-10-03 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 6e105a98-8778-3678-bfc8-dc94809b60a6 | -11.8818 | -44.9815 | 2025-10-03 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 1a06fccd-3e59-34eb-a8e0-fca367593635 | -8.1702 | -44.1377 | 2025-10-03 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2fe74792-28ec-3b3a-8ca7-cff37ab8f4a3 | -12.6323 | -46.9697 | 2025-10-03 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4d036fe5-134a-3f0f-876e-1b0b4ed159b3 | -8.8729 | -46.6985 | 2025-10-03 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 51a9bfe0-2a4d-34af-b7bb-ff5d3c502d7b | -14.0227 | -44.9576 | 2025-10-03 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c080854c-6095-3238-adf7-8b50c2e97ea8 | -7.8165 | -46.9781 | 2025-10-03 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| c1f72432-dc87-333b-b8c4-14f82305c9ac | -7.7682 | -46.2703 | 2025-10-03 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ce8f4802-6049-3a13-ba15-8dce95365c4d | -11.1275 | -47.8634 | 2025-10-03 13:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7fd4bfac-ad36-39ac-96b2-45970a5d55aa | -18.9667 | -48.5198 | 2025-10-03 13:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 4985020e-e069-3b41-aaa5-743e9e7c6f2b | -13.1973 | -50.9095 | 2025-10-03 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 7994e366-303a-3193-83da-8ae3801fda8e | -13.3611 | -48.1159 | 2025-10-03 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 9b700028-fb8d-33e0-b4e2-9f131a6b01cb | -8.1917 | -47.0101 | 2025-10-03 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 392f00c4-5da9-35d3-bfcd-94ca2ae38a98 | -11.9155 | -46.3272 | 2025-10-03 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 414.4 |
| 2d85bf23-5788-3573-8b45-8c0519003bea | -15.7905 | -43.7155 | 2025-10-03 13:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 126.3 |
| c5866e2a-395e-3d4f-9acf-7446dbe90a9e | -13.6711 | -48.0253 | 2025-10-03 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 8ddb42f8-0582-390d-82e0-82dcf1d6c8d9 | -7.7947 | -42.4894 | 2025-10-03 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 6f312e32-1d5d-32a4-ac95-3c596f6feb52 | -9.8991 | -43.7237 | 2025-10-03 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 29c0980b-a125-3bf5-8ce4-091b60a27d5a | -11.9159 | -46.3044 | 2025-10-03 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 232.3 |
| c197d4d1-7106-34c2-8fe8-6e5a1f0e2e13 | -12.6127 | -46.9951 | 2025-10-03 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 76b03924-a4cd-398d-8055-547b67346041 | -18.9673 | -48.4968 | 2025-10-03 13:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 625.8 |
| 849d4d84-2181-34d7-8681-88032b9d18ec | -13.3422 | -48.0965 | 2025-10-03 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 56a82bb6-51bc-30a9-be7e-0d2bd079c88e | -6.5551 | -43.8758 | 2025-10-03 13:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a885e397-64f9-3cbb-9df4-f508a3d98d14 | -9.062 | -46.6565 | 2025-10-03 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| acb7cdd8-1617-30f0-b433-2f4085a09729 | -7.2911 | -45.2775 | 2025-10-03 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 181.9 |


[Clique aqui para ver as próximas entradas](README148.md)
