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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5186d3f9-0c57-3323-8427-a1a717b0f497 | -6.2053 | -45.1414 | 2025-09-17 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c7919bf9-5c4f-324a-a2b1-373a053db997 | -15.8417 | -59.4799 | 2025-09-17 14:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 59ab90d5-99f3-3c5c-9d70-037ca25d5167 | -6.8734 | -43.9636 | 2025-09-17 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 0d2fc95b-b160-305c-b9ed-74bbe108677c | -8.4315 | -47.3853 | 2025-09-17 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e2bb03c7-a5ec-3e7e-a770-5f7c9e965710 | -8.9728 | -46.263 | 2025-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 41924f69-3f33-3fc1-9dab-98886a2e3fc6 | -9.7445 | -47.8468 | 2025-09-17 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 7e2cf6d5-b9cd-3663-8cf1-ec4b31a3b046 | -8.9539 | -46.265 | 2025-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c0b9797c-94f6-3726-a877-b2395805c9af | -6.1253 | -47.8137 | 2025-09-17 14:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ca9a4995-4e57-37e3-9bf9-cdad7c4ba8f2 | -9.0289 | -44.8958 | 2025-09-17 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 428ed215-f162-399f-a4e4-727e122a7c9f | -9.0478 | -44.8936 | 2025-09-17 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 163.6 |
| f5a56706-918b-3276-856c-cfa4083548ce | -5.7869 | -45.9379 | 2025-09-17 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 0686e4c7-72fa-3277-87b4-fa9551fcea65 | -5.943 | -45.1838 | 2025-09-17 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f36d8f8c-7ffd-3810-9b57-757d4cf29102 | -8.9449 | -45.521 | 2025-09-17 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 4fd3d85f-6de9-3fc2-bc80-8005b6e5be1b | -8.6696 | -46.3842 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e997f12b-cad1-39a1-9904-0f103a7854aa | -10.6734 | -46.4928 | 2025-09-17 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| dda397b1-f32b-303d-beed-a47f69ff44f8 | -11.211 | -47.3872 | 2025-09-17 14:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8bbc9225-6268-3b9f-b832-e3ec5d35bc12 | -9.5714 | -48.0847 | 2025-09-17 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| fddab639-7be9-3cca-a2ec-d070b4ede525 | -7.8264 | -46.1081 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f3354fe9-b5cb-36c9-ae07-6eb49c47c9ad | -7.5227 | -44.7321 | 2025-09-17 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 053ad37d-d916-374b-b572-cc2e3edfb292 | -8.899 | -46.136 | 2025-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| f45ed269-d844-3c54-9f7e-d665cd5864cb | -3.8228 | -44.1063 | 2025-09-17 14:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| f5b1f307-ce3c-3fbd-bfbb-d974785ca117 | -3.8004 | -41.6708 | 2025-09-17 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 266.1 |
| 7ee12139-18ff-3608-909b-be9f3c669245 | -5.8056 | -45.9366 | 2025-09-17 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| f3d728d9-166f-321a-8819-5bbd27a10a5c | -9.1053 | -44.8412 | 2025-09-17 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 093b577d-6179-3c0d-afbf-1fb4daa6684a | -9.0475 | -44.9166 | 2025-09-17 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f701ebb8-ffef-3057-a7ca-8e45325d394e | -9.1526 | -46.9366 | 2025-09-17 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 140a0941-c1b1-34b1-b62f-b738c02f9dbb | -12.124 | -47.5566 | 2025-09-17 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 068faa05-c167-3e06-9f6a-bcb36ce35de6 | -14.7911 | -60.2289 | 2025-09-17 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5743478a-0c4a-3995-8fe8-495216d472cf | -8.0005 | -45.6864 | 2025-09-17 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0717ad93-be9b-3e7e-ab7d-6fa6f3e2244f | -8.9399 | -44.492 | 2025-09-17 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 2b9c44a0-3b48-371c-baed-11f4650a9eba | -9.9418 | -45.9281 | 2025-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| b81d3e84-77b7-33e6-98a8-36e92710e644 | -8.6699 | -46.3618 | 2025-09-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.5 |
| ac1966d7-b51c-3f1c-b5c6-d8200f4193f9 | -8.9607 | -45.7459 | 2025-09-17 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 254a6076-6130-3563-8bc9-1ed6cbc8a552 | -8.9359 | -46.1995 | 2025-09-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |


