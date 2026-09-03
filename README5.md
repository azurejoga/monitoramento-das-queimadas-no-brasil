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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b508d971-ab80-3c04-9a66-3d51fdbd2c04 | -6.4208 | -58.3137 | 2026-09-03 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 21b0a604-f1fb-37c2-8bc7-637a715fbb17 | -10.9815 | -45.0874 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| f87d1bb1-4ded-32cd-bbeb-92df678141fa | -11.0006 | -45.0847 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 457.5 |
| 3c43a386-ed87-3cc5-8aa8-0766fa39e449 | -13.4162 | -42.4755 | 2026-09-03 00:10:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 105.6 |
| c9602d18-a5f9-31db-bbd0-70cdccf3ede5 | -9.0415 | -65.7349 | 2026-09-03 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| abb5c7a5-a76f-3c63-95a0-8005efb3f18b | -8.0924 | -50.9642 | 2026-09-03 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 230734b0-9498-3577-bbdc-249ea97d3d8a | -10.9811 | -45.1104 | 2026-09-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 216e94e2-5e2b-3184-a92f-96f729086d83 | -18.776 | -48.9226 | 2026-09-03 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 145.8 |
| f95b5d20-2227-3ec9-bf36-2b8af3bbbffb | -9.0231 | -65.7169 | 2026-09-03 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3c6046e2-ad84-3081-9647-36c7a4a0840f | -18.1699 | -51.8122 | 2026-09-03 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| bfe381cd-c5a3-36f5-aa92-13fdac8d8156 | -18.7565 | -48.9039 | 2026-09-03 00:10:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4d9a8d0f-c423-3929-9df7-8991ecd72bec | -8.6853 | -62.9307 | 2026-09-03 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 22288584-ee7a-3181-b672-7d7e5ec1d917 | -6.6883 | -59.9436 | 2026-09-03 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 9064fb3c-3d50-3b56-aa93-42c15b1328fd | -8.6133 | -62.555 | 2026-09-03 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 1c6f0022-c644-365b-8087-3db4645e38fe | -6.6541 | -59.4452 | 2026-09-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 08295611-befc-3be6-9843-74e259987c66 | -9.023 | -65.7355 | 2026-09-03 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e3558a0c-3f99-3dc5-aeb1-a8b627fbfc15 | -6.6764 | -58.7686 | 2026-09-03 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 49c61f6f-b3f1-353a-8dc5-3ce0b8252571 | -10.87 | -45.34 | 2026-09-03 00:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06739a16-2acb-377a-bb31-31003930b6a1 | -10.99 | -45.08 | 2026-09-03 00:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d51f49b2-9a20-3777-9b5f-25f12e671526 | -11.02 | -45.09 | 2026-09-03 00:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a721862-09c1-3d92-8ada-96fbfe46c841 | -10.99 | -45.13 | 2026-09-03 00:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b5becd4-8451-352e-b5c6-8b64839d4401 | -8.4296 | -54.7262 | 2026-09-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| d8e00ab8-2a97-3579-ab37-e814e5775d7a | -10.8826 | -45.3075 | 2026-09-03 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 300893d9-ce0e-34a8-9f02-c1207843d755 | -9.7316 | -65.0194 | 2026-09-03 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 2d1cbab1-bc0b-3dd6-98eb-80fb177ef5d2 | -8.0737 | -50.9656 | 2026-09-03 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| cd97c19a-3e86-32ac-87a4-1b8ef116a0dc | -18.15 | -51.8156 | 2026-09-03 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b633b95b-e2d9-3fd2-b040-c64f10ec658e | -9.7071 | -57.8887 | 2026-09-03 00:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 583b77fc-1a8c-3f46-93d6-8d28acabe1c8 | -6.6764 | -58.7686 | 2026-09-03 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| d082540b-58b0-3c19-afe0-502a1d5f2a51 | -18.7559 | -48.9267 | 2026-09-03 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 23218b5e-2ce6-31ab-a136-1de63572b784 | -7.0428 | -59.2173 | 2026-09-03 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 2aba51cb-6eb6-39e9-828f-240e7aab1c7a | -6.6248 | -55.2331 | 2026-09-03 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 99712a63-759e-3df2-aca6-7b4687822202 | -13.4157 | -42.4999 | 2026-09-03 00:20:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 116.3 |
| 4b5b42da-fcde-301f-b512-85f947d494dc | -9.0414 | -65.7536 | 2026-09-03 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e81f19e2-4365-38dd-9695-dd1c79c0f190 | -12.4033 | -44.8089 | 2026-09-03 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| bbfd8dae-f710-3225-9f96-94578d9c1779 | -6.6884 | -59.9244 | 2026-09-03 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 742722e6-5efb-37fb-b563-6753a183726b | -8.4675 | -54.6631 | 2026-09-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 3d738fc0-282c-3340-a2da-20961c137b58 | -6.3237 | -56.0434 | 2026-09-03 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d157dfb3-8067-30ee-91b5-d6a93affd4f3 | -6.6247 | -55.2531 | 2026-09-03 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 511e8328-6ff1-32bc-81d5-819f08300288 | -6.7648 | -59.4408 | 2026-09-03 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| c313ced4-a244-3568-a01b-ed8310f4a7ab | -18.776 | -48.9226 | 2026-09-03 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 2363d767-c9d8-399b-9b12-45ad0263c4cf | -8.6132 | -62.5739 | 2026-09-03 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| b80df62e-736c-315c-8ae9-1a0b812a85cb | -18.7565 | -48.9039 | 2026-09-03 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4c829571-f136-3cb0-b419-1b49fb672710 | -11.7722 | -50.4829 | 2026-09-03 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5792b985-a192-3ed3-a6ee-a2729e64aad5 | -11.7535 | -50.4636 | 2026-09-03 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 3b90753f-28ee-31c3-8dcd-6393c112a45f | -6.6882 | -59.9628 | 2026-09-03 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 9260a71d-9955-358a-8740-fb6f6b2e21a6 | -6.4208 | -58.3137 | 2026-09-03 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| e9ac01ad-eaee-314f-8a9a-4c0dc0d465d3 | -8.1298 | -54.9471 | 2026-09-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| ca4d30a6-4ec0-3abd-a52a-ff5412b383e6 | -11.7725 | -50.4614 | 2026-09-03 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2917616c-9e68-3ae5-a54e-6654c969225b | -6.4209 | -58.2943 | 2026-09-03 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 1a28ebcb-c8d2-3624-922a-fc9ee4fb5dc4 | -8.0926 | -50.9431 | 2026-09-03 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9bd45a3f-d2e0-3f9d-a5ac-7a9ea91b5580 | -11.7532 | -50.4851 | 2026-09-03 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 668f50d6-a3e6-3252-8c62-d93544dd49a6 | -6.1474 | -57.7605 | 2026-09-03 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 769bc4a2-06b2-3cf8-9102-24ee138d117a | -10.9017 | -45.3049 | 2026-09-03 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d01f687b-6c61-3440-b072-96a6c89cd584 | -18.1699 | -51.8122 | 2026-09-03 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 639c9a29-2c3d-352f-b9ca-1dab146b7a9b | -6.6698 | -59.9443 | 2026-09-03 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c83b40ee-2be0-3b75-90d1-193ce936467e | -8.4295 | -54.7464 | 2026-09-03 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 932d4716-2619-3b03-a874-fa79579b9149 | -8.5916 | -67.1788 | 2026-09-03 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| ed58be2d-cc34-3cb6-9431-86b170d60aa3 | -8.6317 | -62.5732 | 2026-09-03 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| d9063171-6cb7-34f8-ad9e-b922bd64aecc | -10.9013 | -45.3279 | 2026-09-03 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 99116e6e-141e-3e7c-be95-64dfaab3f281 | -9.0415 | -65.7349 | 2026-09-03 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 359aed8d-fe6c-3a4d-908b-96d28d20972f | -9.713 | -65.02 | 2026-09-03 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0ee577ff-8dc4-3f61-b83c-6794a51ba1cc | -8.7612 | -62.6058 | 2026-09-03 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6fd01cd0-f6c4-326b-b255-73710b8594f2 | -18.8407 | -46.4417 | 2026-09-03 00:20:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 401c334a-de0b-33ce-853d-fcd3e02df406 | -13.4162 | -42.4755 | 2026-09-03 00:20:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 109.7 |
| bbaa4a61-bc31-320f-a859-6026ecaafb20 | -6.7463 | -59.4416 | 2026-09-03 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| c80009da-1ad7-36ba-8b88-bd63f53bfdf4 | -6.436 | -48.5301 | 2026-09-03 00:20:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 260122d6-ac09-3999-ad11-0a4f3b3738b2 | -9.7317 | -65.0006 | 2026-09-03 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3feb2caa-cdda-30f3-b819-a982d86d86a0 | -6.6883 | -59.9436 | 2026-09-03 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 169.5 |
| 69bcd034-8e4c-3baa-8c74-c517a5724bfe | -18.7766 | -48.8999 | 2026-09-03 00:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e810978a-b613-3aa3-b5c1-2a82f04fe6c5 | -6.6725 | -43.4239 | 2026-09-03 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 579d6c6f-e087-3697-8b4b-26486207e3a1 | -6.3052 | -56.0442 | 2026-09-03 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| d5664b64-0bee-39f7-a07a-ba4b24d7ab7e | -18.1704 | -51.7904 | 2026-09-03 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 015b8fce-7aa4-3f1e-bbc9-fc746a9721fb | -12.4037 | -44.7856 | 2026-09-03 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b654251a-3683-3987-8d72-48f01513b6ef | -6.6727 | -43.4006 | 2026-09-03 00:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 100d9b19-028e-3c5e-a4de-1e670917dae8 | -9.7131 | -65.0013 | 2026-09-03 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 04b99869-c9db-3292-9c7c-9a2e4354a429 | -5.8537 | -57.5576 | 2026-09-03 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f83c1b1e-b0ba-3f49-80fd-d69dff145d58 | -10.8822 | -45.3305 | 2026-09-03 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0d12caa9-e9e1-3411-a9f4-570b4094ad8d | -8.0924 | -50.9642 | 2026-09-03 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 868c2dea-a712-3f4d-a16d-1b96ac72c254 | -8.7613 | -62.5869 | 2026-09-03 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b0bf0c1b-94be-30c2-9937-fe15f766677d | -13.4162 | -42.4755 | 2026-09-03 00:30:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 91.2 |
| a63f0bee-cd1e-363b-9898-9f9005d4f056 | -13.4157 | -42.4999 | 2026-09-03 00:30:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 105c503e-39c8-34e9-8a80-f1a0c0efad26 | -11.001 | -45.0617 | 2026-09-03 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| ab4d6cdc-9f2e-3d32-9c23-afcb8f9d68b5 | -6.6884 | -59.9244 | 2026-09-03 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 3e3fb959-dfce-3575-b570-760975f29c89 | -18.1704 | -51.7904 | 2026-09-03 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2c06050b-f137-3f11-8c47-de8cd358457d | -8.6317 | -62.5732 | 2026-09-03 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a228a3ac-063b-3eac-8926-3712abd4636f | -10.9811 | -45.1104 | 2026-09-03 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3bc173c3-5da1-3d81-a0f0-009faac9bf37 | -6.7648 | -59.4408 | 2026-09-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a0293e8f-0b71-3a1d-bcf4-2db78589d402 | -6.3237 | -56.0434 | 2026-09-03 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| e24c37e2-e348-38a9-bf6d-944bdc805c31 | -18.776 | -48.9226 | 2026-09-03 00:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 7188604c-991b-373c-9089-1619c407813f | -18.7766 | -48.8999 | 2026-09-03 00:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ab182502-ae4d-3e8d-b0df-09ae059026f2 | -6.6247 | -55.2531 | 2026-09-03 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b0130df5-8d49-3098-b5ba-f88434f83685 | -6.7463 | -59.4416 | 2026-09-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| e2d090d5-b1ec-30cb-8dd2-c6f5d8abcc07 | -11.7535 | -50.4636 | 2026-09-03 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7a68b753-e336-303d-80de-02111e09ec52 | -6.6248 | -55.2331 | 2026-09-03 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| baa75f3e-7c23-342a-90f0-2a32ac3d24ac | -18.7565 | -48.9039 | 2026-09-03 00:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 108.1 |
| ac86733e-2967-3f97-badb-a8c936febe64 | -6.6725 | -43.4239 | 2026-09-03 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 2ce64fca-ebae-3176-84c9-d944b73dfc45 | -18.15 | -51.8156 | 2026-09-03 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 0598b1c2-7580-3c9c-a564-38ae2e4c2e12 | -5.8537 | -57.5576 | 2026-09-03 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 4d43a16f-48c4-3c2f-bdc2-22baaa1bcd43 | -9.7131 | -65.0013 | 2026-09-03 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 011d905b-50dd-3440-ba19-8d7717e5ccab | -8.5916 | -67.1788 | 2026-09-03 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |


[Clique aqui para ver as próximas entradas](README6.md)
