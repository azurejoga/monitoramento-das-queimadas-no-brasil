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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 443d2678-66a3-37dc-93a5-13b0854e48ea | -11.9533 | -58.6192 | 2026-06-29 13:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 45f83d97-31b0-314e-a69b-0066ed97133f | -12.4464 | -58.4825 | 2026-06-29 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 5b7a9190-65b3-34a3-a06e-8268330c3457 | -8.943 | -45.6573 | 2026-06-29 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| ab1e6356-5187-3266-af35-284e6442f96d | -11.9095 | -57.4134 | 2026-06-29 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b91e7cdf-37a4-3cf8-b0d7-6942c2e7c30d | -11.2148 | -53.833 | 2026-06-29 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 3d199d9a-bd8c-3823-a601-99531113c5f0 | -17.712 | -46.7798 | 2026-06-29 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 7d6c40ae-d913-3dee-b769-3482aa41cb62 | -12.4651 | -58.5009 | 2026-06-29 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| d8fac588-5bae-30b8-98c3-bad669a2b9fa | -11.9535 | -58.5995 | 2026-06-29 13:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 308ebdf5-b8e8-3bc1-8a7f-dbe9f6811143 | -12.5135 | -48.2802 | 2026-06-29 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| f0503392-b351-371c-b9ea-ac414702939a | -8.943 | -45.6573 | 2026-06-29 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 6b938baa-b8d7-34f7-b54c-8080dcf5f331 | -8.2907 | -48.1876 | 2026-06-29 13:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8338eab6-7f15-32a6-9939-223e4e166a8c | -17.7126 | -46.7565 | 2026-06-29 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a1ba4e8a-bf6d-3722-a16b-30f2548dd408 | -9.0684 | -44.7765 | 2026-06-29 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| deaebe31-e7c3-37a9-b290-775e94ce7413 | -12.5135 | -48.2802 | 2026-06-29 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 6303f490-d69b-3205-9661-0fbeeb015328 | -11.9535 | -58.5995 | 2026-06-29 13:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 0394939f-0c93-37a5-989e-fdc6dd252f93 | -6.497 | -42.238 | 2026-06-29 13:30:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 59c82a85-fbb9-3961-8610-3974939f6902 | -11.9095 | -57.4134 | 2026-06-29 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 784acb10-2210-3554-a0d3-90ae086e0229 | -12.4462 | -58.5023 | 2026-06-29 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 177.9 |
| c451a464-b1dc-372a-a6fa-90d8aa669d4a | -11.2148 | -53.833 | 2026-06-29 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| afff228f-6b81-333f-85ca-a2d2ccbf1cad | -17.712 | -46.7798 | 2026-06-29 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 172.1 |
| d73e6585-1f76-3eff-840d-d0ad2a543139 | -12.4651 | -58.5009 | 2026-06-29 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 5d2b015d-26bf-3d02-ac8d-99e2a8f8508c | -11.8906 | -57.415 | 2026-06-29 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 52beb036-457d-3a1b-8267-e61e09683e44 | -9.0687 | -44.7535 | 2026-06-29 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 13791e4b-b12b-3b7c-bd40-dd9d4b79cada | -11.9533 | -58.6192 | 2026-06-29 13:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| a090c6b0-c82d-3430-9368-5f5e5d007255 | -11.9097 | -57.3935 | 2026-06-29 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| de860ee0-64ea-32f0-9f4d-0bf566a8a7f7 | -17.712 | -46.7798 | 2026-06-29 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 3b9fb8bb-9c8b-38ef-aee1-127aeace2613 | -11.9097 | -57.3935 | 2026-06-29 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| ee0b07d0-5c0a-34f5-931d-68c6a5b6e1d2 | -9.0684 | -44.7765 | 2026-06-29 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 076e44dc-f7ad-312c-9503-1729ff96d734 | -11.2148 | -53.833 | 2026-06-29 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 2749ed9c-b3c8-3526-91a0-b5b87b5b5d51 | -8.9427 | -45.68 | 2026-06-29 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4ea59a53-2572-32bd-b016-3c003bd28de1 | -11.9095 | -57.4134 | 2026-06-29 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 272.2 |
| f1d7a07a-9d2b-36fd-8925-7a1dd3c30d67 | -12.5135 | -48.2802 | 2026-06-29 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 106809fd-0234-3093-99c7-e4e72f019553 | -8.943 | -45.6573 | 2026-06-29 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| bd335ef6-9daf-327f-9551-7bd906733dd7 | -9.0687 | -44.7535 | 2026-06-29 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a3e7f4bc-f666-3186-ab91-c635ce9acbe9 | -11.8906 | -57.415 | 2026-06-29 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 62bbc0c7-db90-3a70-8224-ef1a570da95d | -12.4462 | -58.5023 | 2026-06-29 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 214.4 |
| 36532e99-a120-32dd-a8cf-218187977b59 | -11.9533 | -58.6192 | 2026-06-29 13:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| b38c2398-f57b-3d64-b6b1-cf0761052757 | -8.943 | -45.6573 | 2026-06-29 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 161.2 |
| b17b1930-2feb-3e1e-80ad-fb35e8ffedd9 | -11.9093 | -57.4334 | 2026-06-29 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| c5e6b8a3-655a-33dc-a829-85e37cea415f | -8.9985 | -45.7418 | 2026-06-29 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 810f139f-efb5-3718-94c6-27f73e8cc37a | -17.7126 | -46.7565 | 2026-06-29 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 539692e3-d48e-3d69-8b4e-f68c54d27ee9 | -11.9535 | -58.5995 | 2026-06-29 13:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| b0ecbeff-48d4-35e9-a8bb-fba34ac73421 | -17.712 | -46.7798 | 2026-06-29 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 42314a88-03d1-3ebe-adb8-7da8a4e3a77f | -9.0684 | -44.7765 | 2026-06-29 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0fd8dcb3-f756-3f0e-9b74-146a1dfb969c | -11.9533 | -58.6192 | 2026-06-29 13:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| c47a3f52-37e2-3933-8dcb-b4512b47aa6d | -8.9799 | -45.7212 | 2026-06-29 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 20fe5ddd-82d4-3259-bd6b-17e8c072a6f4 | -11.8906 | -57.415 | 2026-06-29 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.7 |
| ba46dcc5-e2fc-3ae0-aa68-d8d6670c6723 | -12.5135 | -48.2802 | 2026-06-29 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| ccdc16e3-4fba-3b75-8c64-1919da7c6bd6 | -11.9095 | -57.4134 | 2026-06-29 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 496.6 |
| f5555c72-0ce7-34a3-8bc5-5fb5c9be90a4 | -11.2148 | -53.833 | 2026-06-29 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| b42a460a-af1b-3d0f-972f-8dabc1817068 | -11.9097 | -57.3935 | 2026-06-29 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 86d52152-b5ab-3095-a6b4-a531b74c1e7f | -14.1926 | -57.4318 | 2026-06-29 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e88a463f-3486-3d11-9662-54e88528c0f7 | -8.2907 | -48.1876 | 2026-06-29 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 073447e1-0d73-36ca-aab4-3d9993d23985 | -14.1924 | -57.4519 | 2026-06-29 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 746f1048-78ec-37a6-bbbf-52b6dc6bbdcf | -9.6037 | -56.9276 | 2026-06-29 13:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0793c87f-9508-379c-a938-2228dfc3517b | -11.0414 | -55.7411 | 2026-06-29 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a1497611-0cd2-38b9-8372-b7ff74bd1943 | -8.9799 | -45.7212 | 2026-06-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 257.9 |
| 6eb75e3b-a719-3fb1-9a9d-a82944524a2c | -9.6037 | -56.9276 | 2026-06-29 14:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a89b6879-d1c7-3773-8ede-77153ab459d9 | -12.5138 | -48.2581 | 2026-06-29 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 55650f07-dca4-31f4-b82e-ba608b49d29f | -17.7126 | -46.7565 | 2026-06-29 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| bbf1452c-e073-392e-bab0-868efa9ba18e | -6.497 | -42.238 | 2026-06-29 14:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 2de83d47-d06e-3ca5-a7ef-06fdb6849560 | -8.943 | -45.6573 | 2026-06-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 1568d2f4-c3b5-354d-8064-90d7c053f7d7 | -8.2907 | -48.1876 | 2026-06-29 14:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| fb293ebd-e26f-3966-b0f9-1d597ac6674d | -11.9097 | -57.3935 | 2026-06-29 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 03ec9526-4094-3885-9f74-c20cb88beb8a | -17.712 | -46.7798 | 2026-06-29 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 5e36d0f9-7c87-3aa3-97cc-63567b33b2c2 | -11.9533 | -58.6192 | 2026-06-29 14:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 916f5c67-4602-3aff-9133-cc4c2c45b557 | -11.9093 | -57.4334 | 2026-06-29 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 9e3cd35b-276e-36b3-9cc8-ec37100f8c92 | -11.9284 | -57.4119 | 2026-06-29 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 4d593b4e-64ff-35e0-8db6-6e1335d62a02 | -11.2148 | -53.833 | 2026-06-29 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 5cd2494b-e406-3797-8753-ec10c4add298 | -11.06 | -55.7597 | 2026-06-29 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 9a374823-01b0-3845-8c68-3decba76ddcb | -11.8906 | -57.415 | 2026-06-29 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 212.0 |
| 06844a12-e445-3bb5-ba2a-19945c38542d | -12.5135 | -48.2802 | 2026-06-29 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| fa288168-1590-3dbe-a2e7-3a56595fca6f | -8.2719 | -48.1893 | 2026-06-29 14:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 9b89d82a-9d78-3d5a-9e60-8263858611ce | -9.0684 | -44.7765 | 2026-06-29 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| d620cc6e-500f-3f77-8014-620bb5337bbc | -11.9535 | -58.5995 | 2026-06-29 14:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 5992db8a-5fe6-350c-9444-ac4d34af7a51 | -11.9095 | -57.4134 | 2026-06-29 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 427.6 |
| 8908d5f2-d693-36f8-81f7-42b202943613 | -17.7126 | -46.7565 | 2026-06-29 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ab455955-5f01-3778-8ef1-2089f308dc77 | -12.5135 | -48.2802 | 2026-06-29 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 39ae0b49-b7e5-31f5-934e-970a08059c47 | -8.9427 | -45.68 | 2026-06-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d60f360b-71d6-34e0-bf47-cb43c8038790 | -5.4738 | -45.4201 | 2026-06-29 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 06191487-ad10-3023-8da6-d7933e158676 | -9.6037 | -56.9276 | 2026-06-29 14:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 792f5a0a-fd1a-39de-b871-e850d0effddb | -8.943 | -45.6573 | 2026-06-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 279a7bdf-b585-389b-9d10-50be57c93635 | -11.0414 | -55.7411 | 2026-06-29 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 6db5733c-aa9f-3683-a54f-6bd5aaf7babc | -11.06 | -55.7597 | 2026-06-29 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 08420767-b956-390d-8d6c-ba633c2ccd1f | -12.5138 | -48.2581 | 2026-06-29 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b8b760f3-e53f-3b48-9ce0-e9fa2a7f0e54 | -17.712 | -46.7798 | 2026-06-29 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 13235f79-cd1d-38bc-89d3-5b8e9c0d9df9 | -11.2148 | -53.833 | 2026-06-29 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c3c6072a-64ca-3dc4-90e4-6cb369bf9a1f | -8.9799 | -45.7212 | 2026-06-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 93ed4262-a0a9-38fd-8cac-8ee0041c4e10 | -8.9985 | -45.7418 | 2026-06-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 196.0 |
| ecff0f5f-218a-383a-83a0-bf025328f879 | -11.9533 | -58.6192 | 2026-06-29 14:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 8a12f0cc-0f0c-383e-9532-cd3337c1ae51 | -17.712 | -46.7798 | 2026-06-29 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 222.7 |
| 3ba3913b-cc1b-30ee-911a-92a9418fb0ae | -11.06 | -55.7597 | 2026-06-29 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 211.7 |
| 84ed847c-5423-3d63-9031-cfaebc564615 | -11.0414 | -55.7411 | 2026-06-29 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 1330abdd-8aa3-3069-bb3f-64fba1e7a11e | -8.9985 | -45.7418 | 2026-06-29 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 9b4212b0-822e-3533-b131-427ebe70bcbc | -8.9427 | -45.68 | 2026-06-29 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 35fb8fdf-fc0d-3723-8878-2d16ff402804 | -11.9286 | -57.392 | 2026-06-29 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6c7f9dd1-749b-3cab-b9fe-e7e7703790dc | -11.9097 | -57.3935 | 2026-06-29 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| bf92baa9-7502-39db-9371-c86d89528f9b | -11.9535 | -58.5995 | 2026-06-29 14:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| dd5e75ec-8942-32f0-b6d0-fa25956dd239 | -11.9095 | -57.4134 | 2026-06-29 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 457.0 |
| c7770f21-7bb5-3478-b321-d0220dc65902 | -11.2148 | -53.833 | 2026-06-29 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |


[Clique aqui para ver as próximas entradas](README13.md)
