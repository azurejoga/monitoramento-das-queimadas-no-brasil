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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 295a668d-9f60-3478-a0c1-e83030c66b2f | -4.2388 | -46.1197 | 2024-11-21 02:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 25b41f40-0da2-320a-a3c9-4058111d56ba | -2.5325 | -45.4517 | 2024-11-21 02:20:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 604f124e-ef0d-37ea-823c-86245cfd9fa4 | -3.295 | -53.8597 | 2024-11-21 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 7f0b246f-a6ce-3c0b-b488-0d8cc47f0249 | -2.5326 | -45.4292 | 2024-11-21 02:20:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a6ca4751-cefb-37b4-a4c2-9e29b5317c9e | -4.2575 | -46.1188 | 2024-11-21 02:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 1223a953-7861-3aa3-b4e5-91120a4c14f0 | -2.0075 | -54.5292 | 2024-11-21 02:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 4f9cc5a2-d094-323b-9b30-50c04ee91f8e | -4.16 | -43.8818 | 2024-11-21 02:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 23acbbd8-187f-35e5-8a0f-12f635b5e91f | -4.7717 | -44.4891 | 2024-11-21 02:20:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 0717de56-0022-33a8-8847-325f1c1c2579 | -4.5799 | -48.0349 | 2024-11-21 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| b3ac1006-74b2-3eba-98a4-2e9cd80048fc | -4.5986 | -48.0123 | 2024-11-21 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b1393449-28b5-34ed-8b34-a5b0cb0db395 | -4.58 | -48.0132 | 2024-11-21 02:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 143.3 |
| a7880391-ef9a-36fc-a302-540a853d740b | -3.2767 | -53.84 | 2024-11-21 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 14edce06-96eb-3575-afed-7cb80e870443 | -6.8258 | -46.7737 | 2024-11-21 02:20:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 216beed1-f458-3262-b2fc-a5db4aa3d57f | -2.0075 | -54.5292 | 2024-11-21 02:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| d23cb846-1da3-3532-ba7a-1366a739c94f | -4.2575 | -46.1188 | 2024-11-21 02:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 099ac7a7-f245-34bf-b676-9b50de3b7e6b | -4.7717 | -44.4891 | 2024-11-21 02:30:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 08908092-eaf9-33c7-914d-18336bdd93fa | -4.5799 | -48.0349 | 2024-11-21 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 7ccf385d-3564-323d-846e-23e678cb6874 | -3.295 | -53.8597 | 2024-11-21 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 04e70c76-e7f1-3b83-97da-633ae4a84d06 | -3.374 | -52.4568 | 2024-11-21 02:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 37523be3-61d3-3258-b0cc-dbe736dfa5e2 | -4.2388 | -46.1197 | 2024-11-21 02:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 4d6cc300-861a-3310-b7fc-ff0cf226a34d | -2.5326 | -45.4292 | 2024-11-21 02:30:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8d212024-d683-3125-b5b8-da68daf9f81d | -3.2767 | -53.84 | 2024-11-21 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| da2a2d92-90f9-3157-b5f3-1269b828da73 | -4.58 | -48.0132 | 2024-11-21 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| c286b281-7c91-3902-bc8c-42b480542447 | -2.0259 | -54.5289 | 2024-11-21 02:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| f4deec85-00ed-3e4b-89ae-da275797b524 | -3.2952 | -53.8194 | 2024-11-21 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f009d1eb-a974-3305-be1e-9f7e0bea008f | -4.2576 | -46.0965 | 2024-11-21 02:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 51271071-dce8-3b97-90a3-5d7bdb8adc7c | -3.2951 | -53.8395 | 2024-11-21 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 7c722784-9b04-3c59-bc61-29ceb56707ac | -2.5325 | -45.4517 | 2024-11-21 02:30:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a20d2b17-dd40-3865-bf2b-95f8ed9964a0 | -3.2768 | -53.8199 | 2024-11-21 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0c8ada26-1c9c-3400-992e-263113413e2b | -4.5799 | -48.0349 | 2024-11-21 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| dcc2c9f0-79ec-339c-9e9c-ab39145c158f | -5.1183 | -43.1731 | 2024-11-21 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 85de43ea-9708-3c2f-961a-63ef629945a7 | -3.374 | -52.4568 | 2024-11-21 02:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| abf674d0-9dcc-3a7a-a20f-ecaf97458a5a | -4.7717 | -44.4891 | 2024-11-21 02:40:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 87c460fd-2d3b-3cf3-84b3-717e75dff435 | -2.0075 | -54.5292 | 2024-11-21 02:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 243800d5-b9e0-3fd7-a747-c9cb89bae840 | -4.58 | -48.0132 | 2024-11-21 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 150.6 |
| c1459956-90fb-3289-97f8-014c47a07e25 | -2.7676 | -52.1045 | 2024-11-21 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 47afaa41-10cf-3f89-a062-1ea11ec0a927 | -3.2767 | -53.84 | 2024-11-21 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| ab5a1368-6513-37a8-9a02-8cb58713eac0 | -3.2951 | -53.8395 | 2024-11-21 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| d87e7d9e-9cd1-3848-86c1-a6d95d2c1bda | -6.8258 | -46.7737 | 2024-11-21 02:40:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 9398f6be-b37b-3557-b904-7a55855a0f4d | -4.2388 | -46.1197 | 2024-11-21 02:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 38a5ac65-a4de-3e99-9bbb-b5cf17efc758 | -3.2768 | -53.8199 | 2024-11-21 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0135ba14-ead6-3147-bcd7-f6fac53fbd2e | -3.295 | -53.8597 | 2024-11-21 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 82e3df0e-272b-380c-a00d-756cc8be9a74 | -2.5325 | -45.4517 | 2024-11-21 02:40:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 348b075e-2292-3fd7-a245-6a95734e0317 | -4.2575 | -46.1188 | 2024-11-21 02:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| b8458ae5-2a76-3bd1-a0a7-d55d62e8d2d6 | -2.0259 | -54.5289 | 2024-11-21 02:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 120a932b-19ef-3dc0-86cd-8d8ea1ba92dc | -4.1413 | -43.8828 | 2024-11-21 02:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9c58699f-6c2d-31c4-b11b-279f7dc04a09 | -2.5326 | -45.4292 | 2024-11-21 02:40:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 598492dc-f704-37e9-aba6-35bde4342c55 | -6.63554 | -35.04711 | 2024-11-21 02:49:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3d60b2f9-1d42-3670-82fd-625caf670c27 | -7.10947 | -35.24749 | 2024-11-21 02:49:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 91b792a6-f9bc-3251-a34c-23b8a546e26e | -6.6378 | -35.05244 | 2024-11-21 02:49:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 977c5c52-a3c0-34d0-b9d7-21bf9004bd7a | -7.10587 | -35.25314 | 2024-11-21 02:49:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1a5f385-8afe-30b9-9cb5-8fa1b7ccbc09 | -7.10697 | -35.24717 | 2024-11-21 02:49:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1392750b-dad6-3d50-86c6-e070e7a7b800 | -6.63443 | -35.05304 | 2024-11-21 02:49:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| bbae787a-54ad-31b5-8dac-73d0bd249217 | -7.10833 | -35.25345 | 2024-11-21 02:49:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e1ee3fe8-dc1a-385a-a0c0-ee2df93e8491 | -6.63221 | -35.04538 | 2024-11-21 02:49:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a3e6f7ee-1e43-3a5c-b06e-ab1164ddab4d | -6.63004 | -35.05733 | 2024-11-21 02:49:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c9afca7b-a3c3-3e29-ab31-b1fa77e47784 | -6.63888 | -35.04649 | 2024-11-21 02:49:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bb569e62-b6f5-33e9-9388-75f0eeb29d3f | -7.11363 | -35.24852 | 2024-11-21 02:49:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6d382979-1598-3ed0-a5de-a03bd270d4f7 | -6.63115 | -35.05123 | 2024-11-21 02:49:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 18ccdc17-bf62-3e05-8173-6aa2e218cf98 | -4.5614 | -48.0141 | 2024-11-21 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d9c09810-5566-3065-935e-f1cf68b4c9ff | -3.295 | -53.8597 | 2024-11-21 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2c165b30-c77a-3008-af0e-3192df21cb57 | -4.2388 | -46.1197 | 2024-11-21 02:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| aaaf3541-b894-3bd1-bebc-aaa500b4cbb6 | -4.58 | -48.0132 | 2024-11-21 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| efea26b9-1e1b-331a-b1ee-a2d0a5fe1ccf | -4.5986 | -48.0123 | 2024-11-21 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f4ff0a57-46a3-3189-8662-b66354d92c66 | -3.2951 | -53.8395 | 2024-11-21 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| bc62d1cd-8913-321f-b798-f75f83423ce3 | -6.8258 | -46.7737 | 2024-11-21 02:50:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 138273c1-94cf-378f-8a89-87f4ee9eba67 | -4.7717 | -44.4891 | 2024-11-21 02:50:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 06671902-b25e-3d2c-92a6-6c155f18040d | -4.2576 | -46.0965 | 2024-11-21 02:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5fd2cb82-ad7a-335b-9164-dd1368bde4c6 | -4.5799 | -48.0349 | 2024-11-21 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9fdc7238-baff-34f6-bda2-247336bb5c84 | -2.0075 | -54.5292 | 2024-11-21 02:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| ad6265df-075e-3109-b8ba-3badb3a2e2de | -3.2767 | -53.84 | 2024-11-21 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 2688db44-637a-3967-ad17-d091a2fff5b4 | -2.0259 | -54.5289 | 2024-11-21 02:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 5bb5e080-3c4d-3279-ad90-cae5a94a818c | -4.2575 | -46.1188 | 2024-11-21 02:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 2b15bf93-58ff-349b-8a85-b9522bc6ed18 | -2.5326 | -45.4292 | 2024-11-21 02:50:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| cc72373e-a0b3-30a0-a737-266c53f72b4d | -3.7611 | -52.4037 | 2024-11-21 02:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 976d4471-6970-3753-8ada-abd29d452bfd | -2.5325 | -45.4517 | 2024-11-21 02:50:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 529199c1-7b8c-32af-8d78-9487ad91bc62 | -4.2575 | -46.1188 | 2024-11-21 03:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 5378689a-8be3-3c5b-8e2f-3b7fff92e11f | -3.2767 | -53.84 | 2024-11-21 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| a6908f2a-691f-3896-b900-5e43e80a7650 | -8.2305 | -41.0182 | 2024-11-21 03:00:00 | GOES-16 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 8b23caee-3078-3039-b69d-12bf2e4026af | -3.2768 | -53.8199 | 2024-11-21 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| fa18f4bd-81fd-36ff-85f2-430d454f4790 | -4.239 | -46.0975 | 2024-11-21 03:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3fa243fe-47c7-3f52-87b4-cac5ae215ede | -4.58 | -48.0132 | 2024-11-21 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 9001e59a-1ba9-3d01-807e-fa213481882e | -8.2309 | -40.9938 | 2024-11-21 03:00:00 | GOES-16 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 39d5660e-a901-332f-93e8-1afb750132be | -4.5799 | -48.0349 | 2024-11-21 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 94e8e1e7-d923-3e1b-981f-fb85067ca885 | -3.7611 | -52.4037 | 2024-11-21 03:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| b2c48827-5451-3a15-b0d9-ea68b2639bb5 | -2.0075 | -54.5292 | 2024-11-21 03:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 1a5916d3-1ce4-39ef-84d2-250179aece6b | -3.295 | -53.8597 | 2024-11-21 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| d5fc7c18-4822-3a55-86e0-003766fdb50e | -2.0259 | -54.5289 | 2024-11-21 03:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| ee9afcef-2cdd-3337-a54e-cb56369af35d | -2.0258 | -54.5489 | 2024-11-21 03:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e52e52a8-9757-3487-b09c-418c0ed9899b | -4.7717 | -44.4891 | 2024-11-21 03:00:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 35d111f3-bfda-3a69-a513-d9678c01b545 | -4.7715 | -44.512 | 2024-11-21 03:00:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 7b82cc38-c0d3-3e36-9853-16c2f6c33605 | -4.2388 | -46.1197 | 2024-11-21 03:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 147.8 |
| f0116f91-65e1-3440-81c9-044b56310eb1 | -3.2951 | -53.8395 | 2024-11-21 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 567f5c1c-9070-35da-8d29-a2d31a669c2d | -8.2305 | -41.0182 | 2024-11-21 03:10:00 | GOES-16 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| f09e4e05-7a83-34b9-acc6-5783724e10a7 | -3.2014 | -54.3243 | 2024-11-21 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 0400f909-d584-360e-863a-e66f5cd67156 | -4.239 | -46.0975 | 2024-11-21 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cc17461e-2ae3-36fc-ba59-cbacf28e8926 | -3.2768 | -53.8199 | 2024-11-21 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 72141e9c-fca3-3241-af19-28a46d9c5dd7 | -3.2767 | -53.84 | 2024-11-21 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d807b190-efee-3e2f-9b7d-45dd23c5f380 | -2.0075 | -54.5292 | 2024-11-21 03:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8af2163b-90aa-3df2-84a7-195330a23a29 | -4.2575 | -46.1188 | 2024-11-21 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 112.6 |


[Clique aqui para ver as próximas entradas](README10.md)
