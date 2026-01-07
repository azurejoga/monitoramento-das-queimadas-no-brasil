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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 501749b1-1cc3-3fb2-ba23-921fde8c7368 | -16.16068 | -59.32323 | 2026-01-07 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2028794-4c0d-388d-a7d1-4a825b0c84a9 | -11.91644 | -58.08123 | 2026-01-07 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d78c068-6b0a-3afc-8424-d45e53b5c51c | -16.31701 | -57.56145 | 2026-01-07 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 68731ba7-bfd8-3009-80d9-7f2d61463006 | -15.2934 | -59.38299 | 2026-01-07 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09527abf-9f10-3f27-8248-d7dbea5c55ca | -11.92258 | -58.09148 | 2026-01-07 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efbbada9-b828-3076-8ec4-75ef41802cdf | -20.54099 | -57.98123 | 2026-01-07 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 8a6af0c0-f068-30fe-8efa-1b51b7e27c8c | -20.54049 | -57.98535 | 2026-01-07 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 7e2a11a3-2103-3e02-8a03-66bba0cc0845 | -20.53256 | -57.98004 | 2026-01-07 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9b1c403e-b2f4-3385-981e-bddf83231bcc | -19.17618 | -57.53862 | 2026-01-07 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a25f23b7-e709-3c9c-ab4b-c4958154f8bd | -21.53867 | -57.53318 | 2026-01-07 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1137b610-a79a-36aa-afdd-030b4261b6dc | -20.52834 | -57.97944 | 2026-01-07 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b96f8d0f-a98a-3b80-9f4f-6bc213f1bf07 | -20.53627 | -57.98475 | 2026-01-07 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| b69f85ad-e5b7-3aed-9166-74d9afbf7003 | -20.54521 | -57.98182 | 2026-01-07 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f6efbd1f-e27a-3f2b-b055-de9260d8fbcb | -21.53811 | -57.53809 | 2026-01-07 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a06d0680-c65c-3bea-8bf2-459b81bc2d09 | -20.53678 | -57.98064 | 2026-01-07 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| f40a8317-0fcf-3ef5-bb42-2f34c1a375a6 | -22.04379 | -56.30686 | 2026-01-07 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75e58a4b-2245-381c-a474-86f55040d20f | 4.26759 | -60.65684 | 2026-01-07 05:50:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5aaabd3-4f33-3cbd-b4af-3f35249d796b | 4.51514 | -60.61026 | 2026-01-07 05:50:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25961e9e-b957-3f11-b850-64b790df9b5b | 4.5159 | -60.6149 | 2026-01-07 05:50:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cc95710-244e-353b-b6e4-616b7672b480 | -3.69451 | -43.4323 | 2026-01-07 05:52:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f2c86431-464a-3c9b-895a-3c4f7d5fd6fd | -5.8156 | -44.13452 | 2026-01-07 05:52:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ee1cedad-2c8b-3660-af81-f4cb16d60f92 | -2.8788 | -40.39342 | 2026-01-07 05:52:00 | AQUA_M-M | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 16e847fb-b892-3755-bcf1-15470c511bd0 | -2.16804 | -53.67181 | 2026-01-07 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c244d79-0ad8-359e-a808-90ca71578617 | -1.59744 | -53.98602 | 2026-01-07 05:52:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 839c7352-82d7-3cc9-8826-c52676692baa | -1.59663 | -53.99125 | 2026-01-07 05:52:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43d3b2df-5c81-3c59-9697-e76618c41f8f | -2.16243 | -51.97939 | 2026-01-07 05:52:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf251013-db4e-3845-bfb7-393938feb29d | -2.1689 | -53.66617 | 2026-01-07 05:52:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9f922b5-677b-3deb-9954-b03a70555ff6 | -2.16013 | -51.99421 | 2026-01-07 05:52:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f51bf7e-5ea0-3e7c-9a00-edbfb055298b | -2.16055 | -51.99165 | 2026-01-07 05:52:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 213cae70-d70a-3e09-a58a-061b42d804fc | -2.16166 | -51.98422 | 2026-01-07 05:52:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d82a4e8-5ea4-35ea-ba44-479079be1d34 | -2.16128 | -51.98682 | 2026-01-07 05:52:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3aec024e-de83-33cf-9a72-e13815044b4b | -20.80934 | -49.81748 | 2026-01-07 05:57:00 | AQUA_M-M | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 45087991-a0fd-39ba-9f24-31fc794b2864 | -20.80328 | -49.81059 | 2026-01-07 05:57:00 | AQUA_M-M | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 7d6b8a90-ef57-36fa-976b-97c506ea4288 | -16.6016 | -58.21344 | 2026-01-07 05:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 19bd704a-8f75-3702-a735-ad694dacf5a5 | -16.59558 | -58.21278 | 2026-01-07 05:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2db66ff5-eb57-389c-810a-36c299afbd61 | -16.05264 | -59.20468 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f907b4f-838b-3b06-aa81-e7c55549a268 | -16.16226 | -59.32313 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57e2081f-1267-3e64-8a41-e7f6ed02f92c | -16.16618 | -59.32167 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cad2a154-afe8-3db1-b97f-1af1b97782a3 | -16.31753 | -57.56705 | 2026-01-07 05:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 748ae3dd-b60b-37af-b113-15164b67f027 | -16.04686 | -59.20552 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a659397-ef10-35af-a32c-a476d5e1753f | -16.1606 | -59.32101 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60a0128f-15e1-3ffd-8ea4-6b6b38d30d92 | -16.05216 | -59.20891 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da5075d3-1aa3-384a-9785-eaebe0992525 | -16.16183 | -59.32693 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89370faa-0ff2-312b-91e5-52eb05e53323 | -16.16019 | -59.32484 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a61c4dcd-ae81-3fe8-858d-72d5d54e0cf6 | -16.16784 | -59.32375 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bc13272-bb8a-35a3-a598-a2246e2d9179 | -16.04637 | -59.20989 | 2026-01-07 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19a6d000-44a8-32d3-8b0e-1db567721d9b | -16.31802 | -57.56232 | 2026-01-07 05:57:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 278bfae7-0c37-36e4-b9ba-fc9ad478f669 | -20.54215 | -57.97908 | 2026-01-07 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 934a52f3-6a84-3b7c-9e44-9eefd3c3e026 | -20.54806 | -57.98512 | 2026-01-07 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 8e30bc63-0807-38dd-9286-a6ff2ae66d9c | -20.52895 | -57.98315 | 2026-01-07 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 8c9d94b1-f860-3b84-805c-f20fa5ab29da | -20.53532 | -57.98381 | 2026-01-07 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e94aba1a-612d-3150-b71d-ed4735c473bb | -20.53578 | -57.97842 | 2026-01-07 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| bd864939-e670-3331-b695-1d0bda29d8a9 | -20.53457 | -57.97818 | 2026-01-07 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f9a41a39-1232-3798-ae07-49fa56f3f597 | -20.53408 | -57.98355 | 2026-01-07 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c2189b91-de4b-30cb-934c-09c25186c2de | -20.54169 | -57.98446 | 2026-01-07 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| bc597add-239b-30d4-93c6-a9ebf60202c2 | -20.52772 | -57.98292 | 2026-01-07 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 394b8b8d-fc54-3822-8891-cb4c2a1aa911 | -2.4799 | -47.20402 | 2026-01-07 12:14:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 306e8e1d-b63b-3edd-b704-ac0071c52684 | -1.67078 | -45.77792 | 2026-01-07 12:14:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 47019886-af52-3f1e-9cb4-c468cc2c4550 | -4.0295 | -45.63681 | 2026-01-07 12:14:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 36.7 |
| a4a9e9f6-6619-3cba-9e51-eea4a4ae085a | -3.42013 | -41.64844 | 2026-01-07 12:14:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| ebc501b1-4ca7-373d-b9c5-d91b1bfbbef0 | -4.03093 | -45.62654 | 2026-01-07 12:14:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 4f0d7b5d-f19e-39e6-907d-0226117f5c3b | -2.25398 | -47.42972 | 2026-01-07 12:14:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f8ed4c3d-bf4c-301d-8a39-fccc3f6d9526 | -3.02761 | -42.04774 | 2026-01-07 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| da230799-9f10-393f-8964-22113b41cf32 | -1.24561 | -46.29881 | 2026-01-07 12:14:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f8645770-d18e-331f-956b-d98ac05a6806 | -10.68328 | -40.41323 | 2026-01-07 12:16:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 147.0 |
| bc1e8fa1-ecf0-3bfd-a1d8-dbf73c85b39b | -10.68683 | -40.3805 | 2026-01-07 12:16:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 42.7 |
| dfbcb0cd-798d-3849-82a7-f62f218c7cac | -10.21105 | -44.22051 | 2026-01-07 12:16:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 301f86dc-87d9-32e8-8cd7-36dc4eea4e53 | -10.68906 | -40.40805 | 2026-01-07 12:16:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 168.2 |
| 16fbcfb5-0e84-3a49-9045-419f402218af | -10.67335 | -40.40602 | 2026-01-07 12:16:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 70aebe7c-5b11-3244-8703-e04e706298e5 | -12.2704 | -45.22511 | 2026-01-07 12:16:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 69a0ab99-ca8c-310a-a379-a89948532584 | -21.89559 | -52.58818 | 2026-01-07 12:18:00 | TERRA_M-T | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 416b3ff9-d347-3932-9dba-dd5e9d4f2019 | -27.27578 | -51.77891 | 2026-01-07 12:21:00 | TERRA_M-T | PRESIDENTE CASTELLO BRANCO | SANTA CATARINA | Brasil | 4213906 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 7c43dc1e-7d16-3d7f-bf56-23a358555c19 | -26.8821 | -50.93058 | 2026-01-07 12:21:00 | TERRA_M-T | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| d3615c23-a939-3a64-a8e4-1175921e795f | -26.62125 | -51.16475 | 2026-01-07 12:21:00 | TERRA_M-T | CALMON | SANTA CATARINA | Brasil | 4203154 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| a21e79fc-cbd6-3318-adf4-df36e74f397a | -29.55771 | -50.95178 | 2026-01-07 12:23:00 | TERRA_M-T | SAPIRANGA | RIO GRANDE DO SUL | Brasil | 4319901 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 98520977-ed5b-3126-ab84-8c7a98838379 | -30.54146 | -52.7168 | 2026-01-07 12:23:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 8.4 |
| eb9424da-f2e2-3db8-9c63-01f2bcbc7b7f | -28.35551 | -49.96074 | 2026-01-07 12:23:00 | TERRA_M-T | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 579de1b9-7d45-3b34-9047-74d18a31b115 | -29.03181 | -51.18503 | 2026-01-07 12:23:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ef6a22ba-efc4-3f21-b7d8-96305e5550f0 | -29.21709 | -50.74161 | 2026-01-07 12:23:00 | TERRA_M-T | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 239.6 |
| 90e13abd-4c67-3088-aa5b-ffbbd4d25d46 | -29.21563 | -50.75355 | 2026-01-07 12:23:00 | TERRA_M-T | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 5aaf51c6-e1f2-3c6c-a0d6-ddd4a1fc9de2 | -20.5486 | -57.9802 | 2026-01-07 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| ecf7e999-c575-32e5-b944-8b8c75ae733f | -20.5283 | -57.983 | 2026-01-07 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 14dee9f0-0c48-3add-b311-38398b35ad45 | -20.5486 | -57.9802 | 2026-01-07 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 6c2604c8-32fc-325a-a858-06bac3786e96 | -20.5283 | -57.983 | 2026-01-07 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| eb7d9579-1042-3386-90f4-7931c222069f | -20.5283 | -57.983 | 2026-01-07 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.7 |
| e6dc4a6a-73e5-33e1-b378-1695a266596b | -20.5486 | -57.9802 | 2026-01-07 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.4 |
| edf81f45-502f-3586-b582-cdac1f9229ae | -20.5486 | -57.9802 | 2026-01-07 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 331.3 |
| ec7b41f5-3177-3046-8d88-57d28ba3a8b4 | -20.5283 | -57.983 | 2026-01-07 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.9 |
| 3e149ba9-6c9e-31b8-bd30-db3efd746fce | -20.5283 | -57.983 | 2026-01-07 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.8 |
| 1609edf7-1ef5-38bc-a34c-51c34ef0832d | -20.5486 | -57.9802 | 2026-01-07 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 329.7 |
| dd00007b-f302-3342-9ab3-802a3a4d15d3 | -20.5486 | -57.9802 | 2026-01-07 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 279.7 |
| 5d44fdfe-bf3d-3fb4-8619-cecfc339b8a8 | -20.5283 | -57.983 | 2026-01-07 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.1 |
| 393bb6aa-25a9-3597-86d7-7edee87ee7dc | -20.5486 | -57.9802 | 2026-01-07 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 271.4 |
| 9d9a78c5-1507-3263-8ed3-846791936060 | -20.5283 | -57.983 | 2026-01-07 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 226dde3f-4623-3bd6-b7e8-bc0b64d9b49e | -20.5482 | -58.0011 | 2026-01-07 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 0f08e6cd-5c5a-3953-a015-14bc03be76b3 | -20.5486 | -57.9802 | 2026-01-07 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 185.0 |
| cb3ef31e-f415-3510-8b61-3711429bbdd3 | -25.0418 | -49.398 | 2026-01-07 14:10:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 121.4 |
| ab5d6c52-f3ff-3f4b-bc34-a4104ae75aa5 | -20.5283 | -57.983 | 2026-01-07 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.2 |
| 725ff066-9c59-3ef4-8d68-0499c1bc37b0 | -25.0418 | -49.398 | 2026-01-07 14:20:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 149.8 |
| 82c7394e-8f7b-3581-9da8-9941e6e4176f | -20.5283 | -57.983 | 2026-01-07 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.4 |


[Clique aqui para ver as próximas entradas](README7.md)
