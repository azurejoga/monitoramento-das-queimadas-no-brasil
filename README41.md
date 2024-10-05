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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cad90c2-a7c5-383b-b5e6-054885c3fba3 | -13.10789 | -46.34535 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76cb8fad-12b3-3a20-a798-43c8f4728174 | -13.10628 | -46.31727 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 08948cbf-b297-3d62-9b95-dcf09dedc779 | -13.10583 | -46.37179 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a463dc63-193f-30ab-9b87-815470ca1369 | -13.10573 | -46.35704 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 35fc2410-f2d9-3c86-85e8-07a75d4af47c | -13.10537 | -46.34805 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5c166ddf-c183-37cc-96e0-14841bc7078c | -13.10514 | -46.32319 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| efdc9912-4696-36eb-8c8d-366d6d60c89f | -13.10477 | -46.37732 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8801eca2-644b-3699-81ac-39ab766d2047 | -13.1047 | -46.36266 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 526e04c7-add1-3426-bf07-d8e645f0abee | -13.1042 | -46.35409 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d2390ebb-b07d-3a95-8cec-4c74f8784430 | -13.10367 | -46.36821 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1bf3fd0f-b643-356d-9fbf-3a06705ccabf | -13.10313 | -46.34391 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 86d3dc81-b2e8-3ddc-9b31-f792b1a6b9d2 | -13.10311 | -46.35978 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7a97a6d5-c564-3ab5-a12d-2102c76ff4ed | -13.10264 | -46.37377 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2619af52-5e46-31cb-a07a-7b044dd25db5 | -13.10203 | -46.36536 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| fd75cbeb-d3e0-3004-b3c2-845aec88bbb9 | -13.09983 | -46.36178 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 53e99600-a07b-3aaf-94f8-86b3a60981ba | -13.09879 | -46.36737 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e6f63fd4-f686-3992-8e31-7e3c1ea089ae | -13.09715 | -46.36453 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d608c0e8-eb83-3318-a885-a5a16ac7ce8a | -13.09495 | -46.3609 | 2024-10-05 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62903818-74cb-36a3-b574-ac3ecc5a94cc | -6.34585 | -45.69764 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e976317-ac1d-3758-b61f-083a8e75c796 | -6.34522 | -45.70122 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bdcf77d-e15f-34f2-829d-fe23a77c11a4 | -6.34053 | -45.69717 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a62a2e48-ab04-3cce-b294-798971955505 | -6.33989 | -45.70089 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89ebb1e4-f9c4-3b7c-a2e4-6569dbb32129 | -6.33455 | -45.70052 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f952b859-5c4f-3174-961f-20a2b6079452 | -6.33101 | -45.68992 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 84ad5eab-73b4-3d8e-9f11-2669936b8b54 | -6.1274 | -46.42777 | 2024-10-05 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaea3210-a6ea-38f6-a2b0-819492f76ada | -5.89669 | -46.28662 | 2024-10-05 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bffeed1a-423c-39f0-b883-5b01e5aad02c | -5.89605 | -46.29028 | 2024-10-05 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2575f4a1-6e3c-3e37-8908-a20b7b1b8395 | -5.89246 | -46.27855 | 2024-10-05 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e5c5ca6-0ea9-38fb-9082-cb9da162e239 | -5.89182 | -46.28217 | 2024-10-05 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30a9188c-8596-3f12-ba78-d9844d3e3282 | -5.89118 | -46.2858 | 2024-10-05 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| caead8ea-cd41-37aa-90c5-11182c5faf41 | -6.18088 | -45.43336 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 96be8704-7b40-37e0-9cec-f44e7361b889 | -6.18036 | -45.43639 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fba13e88-1d6e-328f-8805-9f0348dd5eb2 | -6.17517 | -45.43563 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 008ef83f-ba45-356d-b6bb-18038dbbe95d | -6.17464 | -45.43873 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4e5a4a6f-0002-3b6b-9c2f-776cff3a3b95 | -6.17408 | -45.44191 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| dcfe50b6-5c21-379c-afa7-8c93385c8c86 | -5.97568 | -45.36942 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a779d29f-42f9-374f-959d-7a4f1400426a | -5.97514 | -45.37253 | 2024-10-05 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4d75dd8-7dc1-34c8-8317-cebcbbd37886 | -5.76978 | -45.06648 | 2024-10-05 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e35b4fae-96e8-3379-80dc-0053e3e2461d | -5.76472 | -45.06556 | 2024-10-05 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10fcca2e-7ee7-390b-acad-1b610daf6e51 | -7.27614 | -45.78947 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2453fdf-2680-3bea-8626-e2b490f3d6d6 | -7.27558 | -45.79262 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81bf7636-3293-3399-8414-30e81e9f51af | -7.25718 | -46.25231 | 2024-10-05 03:49:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e49adaed-1763-3f17-b0a0-c2057a59f5d8 | -6.99844 | -45.73581 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f6fb99c2-9278-3c9a-827a-865ae13d7c00 | -6.99789 | -45.73895 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9669a002-85ed-36f7-9a11-c372264d54f8 | -6.99733 | -45.74215 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dd84a84f-1d7c-33a1-9a77-5152addb0782 | -6.98909 | -45.7281 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1474c7aa-a4d4-379e-89f8-990eb571bfbb | -6.98854 | -45.73123 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7b7bc131-9414-372c-b85f-0695a084a5b0 | -6.98799 | -45.73439 | 2024-10-05 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c3e939d2-65ad-34aa-b678-de2e9c802053 | -6.88369 | -46.13896 | 2024-10-05 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0c83d83-8282-30aa-b7f4-e1fb6fe97cdc | -6.88308 | -46.14239 | 2024-10-05 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b3c9a8f-08a3-365e-82d2-fc4f2464c5a3 | -6.75857 | -46.29706 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a9a543c-bb84-3c31-bde1-63b5e53cba4f | -6.75795 | -46.30057 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5b931a6-095d-36c5-8bc5-faf3f9bbb7f1 | -6.75314 | -46.29621 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f56cc63-1f3d-321a-a8af-6f6407e8b479 | -6.75251 | -46.29974 | 2024-10-05 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fb47e2c-9108-3844-ae65-9384befff6a0 | -6.71378 | -46.06474 | 2024-10-05 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 639774c9-5db0-3a2c-b134-f7b7fe084df9 | -6.71319 | -46.06811 | 2024-10-05 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 24431e64-c1ff-3d1c-ba02-3f33af5b0f05 | -8.76721 | -46.80543 | 2024-10-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f808eb36-9c7d-3f57-8837-0e4ce0c1b84f | -8.76515 | -46.80519 | 2024-10-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fc95624-cd6c-32f4-9d83-57cf8c51046d | -8.5984 | -46.49991 | 2024-10-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2139c121-668c-3e4b-9136-77c7f661f555 | -8.59249 | -46.50223 | 2024-10-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1772772b-d5d4-310c-b218-ea2a7d3bfd1a | -8.58718 | -46.50128 | 2024-10-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5c5200f-f71d-3148-b098-6e4640cbe5d4 | -8.58658 | -46.50456 | 2024-10-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12af817b-7b86-3b4d-b880-f6018d17e209 | -8.39448 | -46.3096 | 2024-10-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef3932f1-1a42-3111-9a15-ec86d5a877fb | -8.39389 | -46.31289 | 2024-10-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b95c8ae-e0b5-36a5-8103-8a5c59da885b | -9.96845 | -46.35515 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f2b89cc-8bc9-3737-8687-8a2c6972131d | -9.83989 | -46.72447 | 2024-10-05 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 466dd035-772e-3d53-b7c4-2e74cf7ea441 | -9.78143 | -46.06041 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 017f8d03-1b29-3042-89bd-a9281cec6070 | -9.78088 | -46.06348 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a00703e2-702a-3c93-8c46-0b9cf87a3753 | -10.15551 | -46.34512 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60c684ab-34e1-3c4c-b0e7-74ae613251d9 | -10.15492 | -46.34826 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb89e024-a4aa-3227-8542-02709362ccf8 | -10.15372 | -46.35455 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47e120e7-1c80-3aff-a0a1-d4fe26723eba | -10.14089 | -46.35284 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7764912f-6648-3c4d-ad7b-b5cf05d18847 | -10.13632 | -46.34887 | 2024-10-05 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d69344c-497e-3490-b7da-97901d0da09b | -11.2628 | -46.99713 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6c13aaf-96f9-3dd3-8f12-cebd923af72c | -11.25758 | -46.99607 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4387b443-24ca-3957-a78b-edd0c775134d | -11.24773 | -46.99081 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 615549c9-e303-338d-a824-74497b2c8daa | -11.2471 | -46.9941 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d25ba444-bab4-3373-a814-54ae35054bb0 | -11.24335 | -46.98594 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7a9026e0-4e11-3986-b5c5-c5938ee075db | -11.24312 | -46.98656 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f7d56388-ac11-3b82-a3c0-e472889a6e98 | -11.24275 | -46.98917 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9cccd7a5-fc0c-3128-904a-c4d12a2cb606 | -11.2425 | -46.98979 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 98e2af4d-9213-3bcb-93a8-df12f0439bb0 | -11.24215 | -46.99243 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7fadae84-fd83-3924-947b-a65493bb4f6b | -11.2385 | -46.98239 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3450fc89-4c99-32bb-a77a-03270952f850 | -11.23811 | -46.98495 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3e0280bd-7eeb-3a72-a2bd-8246d4fb35a3 | -11.23788 | -46.98558 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1eb1e9f9-034a-3c26-9caa-9fe508eb02d5 | -11.23325 | -46.98148 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 916e13ee-e00e-3609-a397-bf0c2689ad73 | -11.23286 | -46.98403 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8cd6eb5-c825-3ff4-a41a-e085c6ca3ac6 | -11.23263 | -46.98468 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34433e61-ede2-3cdb-ab31-dae64921add7 | -11.23216 | -46.61617 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab45f3cd-bf1c-35d5-bc8b-44e9d45a2c6c | -11.23158 | -46.61927 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 49a6d6d1-c3c9-318b-85f5-08bcdc43d907 | -11.22703 | -46.6153 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5001e074-d454-3c81-b63a-6b5900bd027d | -11.21978 | -46.59777 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 613a787a-515f-3c02-ae18-bce40e1d6250 | -11.21918 | -46.60092 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23fc4011-9acd-3c08-967a-13fae370f7e2 | -11.1946 | -46.89948 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ef7f847-3e28-3854-b0a4-08006794266c | -11.19397 | -46.9028 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91bc652d-97c9-3ca2-8867-f25927dab06d | -11.17925 | -46.92344 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67e88645-25c1-387f-9ac8-14c3a58a1a11 | -11.17865 | -46.92658 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3db411f0-1181-3056-9969-06bcfda63c88 | -11.17338 | -46.92585 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5d22078-d475-322d-960b-12169efc984f | -11.17277 | -46.92906 | 2024-10-05 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d16a9334-efa6-31a2-ad47-16569f7f4c4b | -11.16438 | -46.51124 | 2024-10-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
