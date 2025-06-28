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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8bde340-f1bf-346f-ab1e-3ccd84249b03 | -4.54049 | -48.02285 | 2025-06-28 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| d1bcbb40-79d2-3481-809e-7cfb7a8d201e | -4.81567 | -47.3213 | 2025-06-28 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd8bdeb8-cd24-3967-af80-d4e6186eb9e2 | -6.16172 | -47.2738 | 2025-06-28 04:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d77eb7e-bdba-33d7-bee1-67dc6a1959a8 | -8.04323 | -47.64374 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f7b8031-f028-3e8f-b77f-dc27956c36b2 | -6.90262 | -43.98209 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 781371b7-86e0-36a6-9239-544da2b95b9a | -8.0036 | -49.71361 | 2025-06-28 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31dc7c4d-ba2c-37a8-bbac-dc83f128afee | -4.43344 | -47.61538 | 2025-06-28 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec894983-5757-3e74-9f9a-714bf906bf34 | -8.42387 | -47.05149 | 2025-06-28 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcf68aec-bf8f-3b02-9a0f-c109adfcc2ff | -4.12453 | -43.07171 | 2025-06-28 04:49:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9f71b52-2ec2-3dbb-aeb1-cbcf21beabe5 | -6.90967 | -43.9699 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c733c2a-022c-3f1a-8ba8-a78e5a9a5d42 | -7.08257 | -49.60459 | 2025-06-28 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f88ab69-391d-3015-87a7-3dd5493a85a6 | -6.74312 | -47.22336 | 2025-06-28 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f73ad13-0d79-36c2-9ac4-79c2617ebc5d | -8.85161 | -47.50991 | 2025-06-28 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d6c5c9c-0f19-3909-a9b0-2cd213b25d0f | -6.95289 | -42.9076 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a9459855-c96c-3048-a55f-ee5de28e184f | -6.06464 | -48.12336 | 2025-06-28 04:49:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d503a0d-b426-38b2-aefc-0d1322672989 | -6.91243 | -43.99448 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 154d9e5b-6609-3092-ac7d-ff1e7de5efc7 | -8.04217 | -47.65119 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c24bc0fe-95f9-3eeb-8b76-e36bf1843713 | -8.73983 | -47.85123 | 2025-06-28 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4618d947-306e-38ee-b446-9c7f8d0a1a35 | -7.10358 | -52.58413 | 2025-06-28 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8d2a645-78bb-3604-96a0-5a448f2253a1 | -6.45009 | -44.5776 | 2025-06-28 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ba9d3de-9d1e-3a9b-8baf-952e6418f6cc | -7.39291 | -44.55287 | 2025-06-28 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8bc97e3-b1cf-3fef-92c6-db05d09f5002 | -6.45089 | -44.57191 | 2025-06-28 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 245e613a-4bc8-39b4-8738-a6d6d66753b5 | -5.20625 | -46.83189 | 2025-06-28 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87b48714-58b9-362b-a683-f7f162103cbb | -7.08334 | -49.5933 | 2025-06-28 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c50a6ffa-e734-3bfa-aa72-74912f435dd8 | -8.85217 | -47.50602 | 2025-06-28 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f742f58e-405e-3147-b171-09c66289230a | -6.23261 | -44.52587 | 2025-06-28 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8f1190b-70e9-33d2-ae38-12d65cbadaf4 | -6.95236 | -42.91143 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 819b8ff1-3086-3d8b-b617-b058a04fb3a3 | -5.45499 | -43.07872 | 2025-06-28 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a890899-5eed-3685-8c68-997f2a43d2ae | -7.2151 | -43.07936 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| eda5c096-6d6c-3446-b9ed-edb72fe3eb0b | -8.0427 | -47.64748 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb8c44d1-2a90-3f0c-b7cb-e680ef44d29e | -5.22745 | -56.02192 | 2025-06-28 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02217630-3e0d-30f9-a519-13d306d24903 | -6.9133 | -43.98802 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e653de12-7b09-387e-8676-dd55cf0ed883 | -7.21458 | -43.08312 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b277390b-bed6-3f4f-b31a-cb11276f39c2 | -4.37371 | -48.07998 | 2025-06-28 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11ed1373-64ba-350a-a43e-103e5b9bbaaa | -5.4668 | -43.07347 | 2025-06-28 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ac945e1-959a-367b-9ab4-a39d0285ff6e | -5.41481 | -47.5699 | 2025-06-28 04:49:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecd2dd08-d4f4-315c-8733-347bbbbb6dea | -6.91417 | -43.98158 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4f069bf-2246-3ac7-880a-65dbbc9e31f6 | -3.72659 | -53.77492 | 2025-06-28 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b169ba6-9beb-3772-95b4-2a237eb8fc51 | -8.00424 | -49.70937 | 2025-06-28 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a42c4068-92cb-3467-b878-d49689b1cd67 | -7.10222 | -44.36698 | 2025-06-28 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e69fa040-6a49-33c1-9eb5-ce8258f992a7 | -6.90079 | -43.99496 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40b36dc1-86eb-3c27-9a9c-8a2a9613af26 | -8.4282 | -47.05202 | 2025-06-28 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c14f4f9-efdb-30f0-a498-857bfd47c449 | -6.65597 | -55.42294 | 2025-06-28 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d12def33-7287-3c93-9367-27dc3a82652f | -6.89648 | -43.98789 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22da0c35-e76b-3cbd-9896-66a05d4e223b | -8.79751 | -44.99546 | 2025-06-28 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 985467ac-ec8a-35f5-85e1-cd4ace5a54ef | -6.94483 | -42.88338 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 3947ae8f-e34c-3edb-8ca7-1a7e08cabfc3 | -8.85584 | -47.51045 | 2025-06-28 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad1b6d7c-6469-3c88-84aa-6aa3583251a5 | -7.0827 | -49.5975 | 2025-06-28 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90d99c0d-2202-3ba8-b42d-ce5dcb6bbdd5 | -7.10833 | -43.37042 | 2025-06-28 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 001a961f-4934-355e-9a33-92f25908909f | -6.91373 | -43.9848 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c500c14-8023-3903-8fd3-ad11c94d342b | -6.23757 | -44.52669 | 2025-06-28 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c552fa70-1b12-3d51-b39d-56641cf260b2 | -6.89693 | -43.98465 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7bfbfe0-baf7-33ce-9296-2667b6af4dc4 | -8.42597 | -47.05261 | 2025-06-28 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cf9a701-c4dc-3734-891d-c7a1d319b441 | -3.73115 | -53.76822 | 2025-06-28 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbe8b7cb-56b7-3360-a2e6-5bf56f3a4411 | -5.41216 | -49.07947 | 2025-06-28 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46384c8c-ae96-30d2-995c-e9423f31d100 | -6.91352 | -43.98026 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4067a439-ec69-3abb-98b4-c0404edac134 | -6.55643 | -54.98116 | 2025-06-28 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cca60b1-76bb-3c44-81ce-32184408e088 | -4.37657 | -48.08226 | 2025-06-28 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80a4c447-4f77-3ab1-8519-dd9757271ca6 | -6.90125 | -43.99174 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f92e9a0c-8b1b-35bd-9536-cde8372cebab | -4.13034 | -43.06921 | 2025-06-28 04:49:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 018500fb-4e35-32b7-9249-40a8d187a518 | -7.21005 | -43.07479 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 08460a77-e32a-3577-9b15-4b0bd0eb606f | -8.04682 | -47.64808 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31977f1b-3f27-35d8-a4eb-41a1a2cd68f3 | -6.91168 | -43.99313 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25e63fbf-bf8d-3756-8291-f5fd89200e64 | -7.20293 | -43.08536 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d19d454a-3987-3718-bdb2-94382bab9318 | -6.73342 | -47.375 | 2025-06-28 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef8b877d-23eb-3092-a6fa-4c82dd528082 | -6.90647 | -43.99241 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bf7b690-6e0e-3816-a5b3-606a1b5bc470 | -5.46089 | -43.07616 | 2025-06-28 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 78d92dd3-4061-374a-b166-90facfa7fdb0 | -8.04789 | -47.64061 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bbeb5c5-71da-3a09-a99f-c05ff2906e36 | -3.71992 | -53.75153 | 2025-06-28 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6ab5985-c0c4-35ce-b4a5-a7dc0f083082 | -7.54431 | -45.82975 | 2025-06-28 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 30d1d203-9c55-35be-88ce-aa09eba02275 | -8.03086 | -47.64188 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a34de3f-4d40-3377-ace4-5f5c132c472b | -8.04735 | -47.64436 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81ac0221-ad61-329a-b365-c4f7b3174495 | -6.91214 | -43.98991 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28f19e02-2b20-38ed-b7dd-3e7be039b49e | -7.09711 | -44.36634 | 2025-06-28 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e37daf5-d099-3e19-91ed-f13c7c50bc3d | -7.91305 | -49.64553 | 2025-06-28 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 590b469c-3b1f-3c19-b606-dce9ad75592b | -3.38181 | -43.12347 | 2025-06-28 04:49:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbf09f60-5c45-3014-9bc6-1b3598625841 | -4.54503 | -48.01871 | 2025-06-28 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 30af024b-0de5-35f3-a652-bf4c9648bc74 | -5.6219 | -44.01144 | 2025-06-28 04:49:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b19ce86-428a-36d0-b0d1-517560cb5d3d | -7.34223 | -45.31417 | 2025-06-28 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aee2ee5c-6101-3682-a636-713d9acd0f7a | -6.5489 | -54.98383 | 2025-06-28 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b804e89a-94b6-3c36-8b2e-b5af5533470a | -3.31324 | -48.717 | 2025-06-28 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eeb7d83d-0c03-3641-bdd4-b3c2295d3e94 | -7.18912 | -45.32771 | 2025-06-28 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e62dc3df-4b42-3ede-9bdd-82621d356079 | -7.54895 | -45.83043 | 2025-06-28 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1dc823ca-e38c-3786-b6d2-2831b0b0394a | -5.8731 | -50.14805 | 2025-06-28 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e74fc277-af6b-33e2-afdd-46a5500df0b2 | -5.45395 | -43.07509 | 2025-06-28 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b82986f4-4721-3be1-a940-fc42d583181b | -6.90307 | -43.97886 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fdc85f6f-9223-3233-a7cd-2de1f8100bee | -5.44128 | -46.56219 | 2025-06-28 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4797db3-3dfa-3292-8af5-1235b0309364 | -7.11378 | -43.37123 | 2025-06-28 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b48175a0-a503-3e5a-aea6-f6fdfa89b5f9 | -7.39251 | -44.55578 | 2025-06-28 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ec07761-e767-30b1-b788-d5c8f9c593df | -8.03139 | -47.63812 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1731e14-0afd-37e5-bbcd-bdfce1eb8acf | -4.37752 | -48.08055 | 2025-06-28 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbca4fd4-0c59-319b-b48f-f252f027909a | -6.55297 | -54.98058 | 2025-06-28 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6724c7e8-aa53-30ae-b03c-f9b4aeb77b78 | -6.95097 | -42.88046 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 08cdc5e4-7ea1-37a2-ac86-a7efca429eb5 | -7.54964 | -45.82542 | 2025-06-28 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9891a03-6761-33d6-b746-0991db9b5261 | -6.73896 | -47.2227 | 2025-06-28 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea026d4f-68be-3d31-a917-61c947b332e7 | -8.30881 | -46.31123 | 2025-06-28 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e8006d2-541b-321f-9caa-e41325465f08 | -6.90556 | -43.99882 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44b6afb3-0e44-3c20-9a0f-f6d7dc669070 | -5.46039 | -43.07969 | 2025-06-28 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 38b6bd6d-d3d0-325f-b674-65221f9a9aa0 | -5.86305 | -46.48124 | 2025-06-28 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be4d8f2c-866a-3ada-96e3-f0aa735b880c | -4.54815 | -48.024 | 2025-06-28 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README22.md)
