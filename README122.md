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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fb95070-73e5-3283-a8a8-c9ebc359a35a | -8.3689 | -44.8305 | 2025-09-12 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 9fb575bc-c7c5-3d88-a381-7d937deb5213 | -8.9566 | -46.0623 | 2025-09-12 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| f34fdeff-a0ab-3bcf-9d6c-5a66ad90599e | -7.5641 | -44.4068 | 2025-09-12 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1b4d2edc-95e2-3ba8-9c8d-5705603a6a2a | -16.9621 | -45.8176 | 2025-09-12 12:30:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ab0c9d78-bbd8-38c1-b81f-fb7a6d14824c | -9.0379 | -47.0597 | 2025-09-12 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 7a99fa12-c332-3fa6-9349-e36207d6c312 | -6.1703 | -41.0901 | 2025-09-12 12:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 401.8 |
| aaaea4eb-7622-3253-b7b4-f0b2e78a2257 | -9.0759 | -47.0335 | 2025-09-12 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1ef84a6c-7e71-337d-8fac-142336d74295 | -9.673 | -47.5459 | 2025-09-12 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 78fb4c29-1859-3b7c-b87b-08de7d90f5a9 | -11.4402 | -48.5513 | 2025-09-12 12:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 4484f736-45ec-3e0c-9f2f-30826c6dde68 | -6.83012 | -45.65769 | 2025-09-12 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 760b22b2-058b-328c-9aad-56474f6d994a | -7.44893 | -44.42723 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 8f12bb2c-fb62-3fc9-857d-354a7bf856b6 | -7.57047 | -44.40485 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 48d70d0e-4d74-3d4d-b3eb-9c3ef6c65dc9 | -7.62783 | -44.7658 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| a0a45c94-a658-39ca-9f5f-cfe6e9fd0b2b | -6.55211 | -43.97959 | 2025-09-12 12:34:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 1a1cd947-2812-3ce3-b131-e22628df5281 | -6.80835 | -45.63725 | 2025-09-12 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| efbaf4b4-7c7a-3577-a10f-32a676be9d4a | -6.28038 | -44.46822 | 2025-09-12 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| d44ad3be-b24e-32c0-9397-8067fd533281 | -7.55698 | -44.40322 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 01cb5ff6-3e49-3398-bcb3-12ac3472f350 | -6.30776 | -42.21494 | 2025-09-12 12:34:00 | TERRA_M-T | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| c90d8dc5-cf63-3414-92b1-624c6529832e | -7.55453 | -44.38591 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| fbb1119b-c46f-31a7-b9a2-9d2f537dcfbe | -7.62768 | -44.75086 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 3efa1948-2964-381c-9ebe-822c306a8270 | -6.16807 | -41.09216 | 2025-09-12 12:34:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 254.8 |
| b1818854-fa29-3470-afae-c8fe04248b6a | -7.57336 | -44.38284 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 68256e5f-948c-36a8-bd6d-880175a14bb1 | -7.53369 | -44.68459 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| e8b684b5-d03d-3397-ac6e-2b41b6945698 | -5.94366 | -42.78862 | 2025-09-12 12:34:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| b0cbf895-3b79-3d2c-a9cb-624bfd27fbb7 | -7.55183 | -44.40805 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 3f81f11a-3822-34ac-b1fb-486a8b277713 | -7.55985 | -44.3811 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 03eca867-23ce-3926-befe-e79b3206a9eb | -7.64081 | -44.75246 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7a262809-ce96-3a95-90f1-bb5748c81350 | -6.18516 | -41.09418 | 2025-09-12 12:34:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 81aff6ae-6a4a-37e4-9b59-2fcfbf79bde6 | -5.76196 | -52.36978 | 2025-09-12 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d204317f-c69d-3ec5-bb26-6f7f7b3ca448 | -6.1634 | -41.13058 | 2025-09-12 12:34:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| c073961a-13b1-37f5-b872-a78fcebb696b | -7.63069 | -44.74427 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| bccc1dd4-9036-38b5-8b75-a5cf99cc8e5b | -6.96059 | -42.90053 | 2025-09-12 12:34:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 14fc88ee-77bb-3d15-93d2-d07ebaa1c310 | -6.15975 | -41.12506 | 2025-09-12 12:34:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 131.8 |
| f6d9de22-e50b-3205-95f6-8c76741383cd | -6.14984 | -53.68309 | 2025-09-12 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3333a719-2185-38e3-b6c8-d18e24669688 | -7.56532 | -44.40973 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| bbba6294-5139-31df-9245-10f37691f111 | -6.18174 | -41.08881 | 2025-09-12 12:34:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 756855d1-2098-3da0-a209-0177f00fb587 | -6.17829 | -42.62477 | 2025-09-12 12:34:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 9631acba-fe3f-39a2-9079-7939fd73d3b5 | -6.32901 | -53.45824 | 2025-09-12 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 25c86aae-8a0f-3c54-8415-501d7fd01e5a | -6.68582 | -44.14672 | 2025-09-12 12:34:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 271513c8-13e3-3261-bd89-c0e946276e46 | -6.68871 | -44.12353 | 2025-09-12 12:34:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| a92cdfd6-459f-3b42-a92c-f2c99285e6c1 | -2.8567 | -47.74281 | 2025-09-12 12:34:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 6fbaba64-6c01-3255-9164-e7c1e13e1314 | -5.8229 | -52.33136 | 2025-09-12 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f18e639b-184b-3b2d-8abf-3b1f07889f42 | -6.82779 | -45.67525 | 2025-09-12 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| d452cfe1-e4ac-3e25-8b7f-bff028db240b | -6.80606 | -45.65475 | 2025-09-12 12:34:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 56b82427-eb99-3862-860e-fcc1fee80f3e | -7.71888 | -43.85756 | 2025-09-12 12:34:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| e6362d6a-a9b8-3063-8ed0-06b14cd1dc8a | -6.17596 | -42.63035 | 2025-09-12 12:34:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 46c7ff3e-157b-3e5a-b703-febe70dce152 | -6.08161 | -44.69828 | 2025-09-12 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| d024a57b-0ba3-3405-8f37-81d1907faea6 | -7.4517 | -44.40575 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 8aad5a7a-0254-3078-8fe3-773da0d8b649 | -6.67806 | -44.14073 | 2025-09-12 12:34:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a359cf6f-8821-3d18-8375-87de4c5ea916 | -7.38992 | -44.3525 | 2025-09-12 12:34:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 7eee647b-adfc-3b29-889c-e96265e21788 | -7.43828 | -44.40379 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 5f91f1bc-b46d-3250-ac89-13ab0e4c79ff | -6.54542 | -43.97249 | 2025-09-12 12:34:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 633fd6de-9cd5-3e16-a54d-1cf1bb33bb37 | -7.42023 | -45.86097 | 2025-09-12 12:34:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| fb6c94be-27f5-3c66-a627-16db6c1a82e2 | -3.65004 | -48.9676 | 2025-09-12 12:34:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fa1886db-c133-30c9-afb1-1e5e1c8adace | -6.08417 | -44.67832 | 2025-09-12 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| bd392b63-8e93-3b3d-8be4-fe9835dcf831 | -6.30195 | -42.22055 | 2025-09-12 12:34:00 | TERRA_M-T | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 0f35a52a-ae91-3551-813c-9db853fc85e1 | -7.56803 | -44.38767 | 2025-09-12 12:34:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 24279d77-99ae-34fb-9c14-0249711a2195 | -7.18215 | -44.87187 | 2025-09-12 12:34:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0c30c8b6-9965-3815-99f2-b70dda649c2e | -6.1647 | -41.08647 | 2025-09-12 12:34:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 192.2 |
| 98041a9e-cd01-36bc-8a71-2365a2a609cd | -6.10373 | -45.93819 | 2025-09-12 12:34:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7a23f124-57d4-3255-a141-fb0877afce99 | -6.08225 | -44.69278 | 2025-09-12 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 52e65c09-42f6-3bf3-9fad-28406522a47a | -2.76906 | -49.2014 | 2025-09-12 12:34:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d61853e9-5cad-3d72-8c45-2e8b7c42f83d | -10.1292 | -47.91245 | 2025-09-12 12:36:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| b7d1291d-988c-3f1f-89d8-060b7f5f6df8 | -11.08871 | -48.42424 | 2025-09-12 12:36:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ad66d710-8a89-30d4-9abf-3635dd656cd2 | -9.67451 | -47.55071 | 2025-09-12 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| ed5040ea-75b3-3071-9717-7c20082b3cd9 | -11.54833 | -50.57885 | 2025-09-12 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 1c975505-b67d-3c26-94ac-2ae2bb009d40 | -9.87254 | -46.4761 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| f09e4fd6-4956-3bfa-9504-e184d4b537ad | -14.39364 | -52.94156 | 2025-09-12 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4364c982-18dc-3fa7-a65e-24a70ed6f3c8 | -11.73808 | -46.63174 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| a0a2e440-49c3-327a-b481-a637cca10696 | -10.90673 | -47.23315 | 2025-09-12 12:36:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| b9b37167-d80e-3090-af10-f20ea635e745 | -11.09027 | -48.41209 | 2025-09-12 12:36:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4b021f2c-0a23-3cb6-8743-10ebd122fe06 | -8.43011 | -47.2473 | 2025-09-12 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8a9d3e81-f67a-3391-82d7-d75618c85062 | -9.72444 | -46.89455 | 2025-09-12 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| aae775ff-f659-32db-b44e-69861cf6559b | -9.71397 | -48.34467 | 2025-09-12 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 55d38175-a6bb-3b53-8b6a-800959ca40cc | -11.49992 | -49.25638 | 2025-09-12 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 3630a340-45c2-31b6-815e-77d744447336 | -8.04635 | -52.3247 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f041450a-7cc8-3c37-83c2-9a7d315c527b | -9.83416 | -54.52954 | 2025-09-12 12:36:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5979cec2-5e02-3473-b836-ecb9afe364dd | -11.46744 | -49.27468 | 2025-09-12 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c322e8d3-71a4-3162-914f-7fac8b6df333 | -7.73096 | -49.82632 | 2025-09-12 12:36:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| aabb7ba1-7784-3ba8-9a3a-c0cf6b75c7b5 | -11.11884 | -51.99488 | 2025-09-12 12:36:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1d1c80cd-1d9d-3ec6-b26a-0fad0e887782 | -9.56627 | -48.29501 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b5740237-d677-3514-ab5c-86be3e162be4 | -9.75404 | -46.01686 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 032e8e8b-5eca-3999-a343-a37416c38b2e | -11.18858 | -55.07044 | 2025-09-12 12:36:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 80ad1cd3-9d26-3e1a-99af-46af8fbd7c5a | -8.47446 | -47.27291 | 2025-09-12 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 39039ef3-fa9b-320d-a267-e7f99ffd0118 | -11.70611 | -46.59338 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 4175bd23-f58a-331c-ae93-c9f3b1fb28f0 | -11.81678 | -50.56535 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fcd47058-5e5b-3254-8864-e380422e304c | -11.79179 | -50.55561 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| aa1abf23-6461-3026-8ab5-12e6bc41cea2 | -6.82465 | -52.79736 | 2025-09-12 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6d234535-400d-3908-973c-8cc45f9995e1 | -14.18917 | -46.20651 | 2025-09-12 12:36:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| eaed53a4-279a-3547-b796-506b17dfeff6 | -10.74649 | -48.18131 | 2025-09-12 12:36:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f86ac323-1ac0-326c-af80-4d4b30a801fd | -8.9583 | -46.09349 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| c5a3a343-7cfc-3ac4-a9e6-6e1e22a1daf0 | -11.70822 | -46.576 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 705.6 |
| fdfd54ae-6025-3608-85ae-46b627f774cc | -10.09111 | -47.16485 | 2025-09-12 12:36:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| ba5a30e6-898e-322f-b6de-6c305c9f17c4 | -14.33 | -54.13319 | 2025-09-12 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c16a358d-bf06-305d-b91f-056ff7489bfc | -9.07297 | -50.50312 | 2025-09-12 12:36:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4ac9865c-9429-39ca-bc61-91f5d4b4b880 | -15.13092 | -48.5992 | 2025-09-12 12:36:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 64206e99-9bf1-3fb0-929b-d28a347f0b5d | -9.0534 | -47.03525 | 2025-09-12 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| aea5105a-8dd8-3726-a595-afc42f8e4a99 | -11.13991 | -45.22714 | 2025-09-12 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 20260755-f656-38fa-a3b4-934915eb90af | -9.91472 | -45.99366 | 2025-09-12 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| db109b48-0cf0-3139-b349-a50e7d274d5e | -9.6508 | -48.05501 | 2025-09-12 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |


[Clique aqui para ver as próximas entradas](README123.md)
