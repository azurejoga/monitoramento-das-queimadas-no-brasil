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

## Dados Diários - Página 214

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34172c76-d442-3fe8-a7f0-9672d16c56f6 | -8.1115 | -50.9206 | 2026-10-08 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 812c86f7-e34d-379f-a747-6f6b9866e18c | -8.1876 | -54.7219 | 2026-10-08 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 79ba1a7f-db9e-369c-b6c3-9634a3a7bcf8 | -6.8764 | -43.685 | 2026-10-08 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 0f71240c-8044-3062-a992-db755d9c87ab | -9.4749 | -64.3713 | 2026-10-08 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a8c159e8-e018-32da-8f90-590daf3c9fba | -8.0895 | -55.311 | 2026-10-08 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e3ec2ed7-e350-3160-a2da-996d920bad86 | -6.895 | -43.7066 | 2026-10-08 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| c9ded85a-0128-30dd-a02e-2fda6dc728a8 | -6.9881 | -59.1037 | 2026-10-08 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1812e29a-5b5c-3fab-a91c-1c75b39b0c54 | -9.8253 | -47.4629 | 2026-10-08 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| dfcff0a0-641d-300b-85d6-36ee23be7118 | -3.7818 | -41.6479 | 2026-10-08 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 150.7 |
| 5908ef51-5688-3d16-8137-ff71ff40a296 | -9.9014 | -44.8147 | 2026-10-08 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 8b8ac1d3-fc62-36c5-8119-47c6c783a2dc | -7.2185 | -55.1016 | 2026-10-08 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 693d037f-be8a-3ae4-8f83-70f161719766 | -7.0066 | -59.1029 | 2026-10-08 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 0febab85-2917-3a75-be25-94769078f9d3 | -11.9643 | -57.5882 | 2026-10-08 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b5fee9b2-ae16-3a7b-8176-eef57ebf010d | 1.6937 | -55.6263 | 2026-10-08 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f073c467-8683-3277-bbfc-e0779cf09f66 | 1.7304 | -55.6061 | 2026-10-08 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 64bb1f3a-fc3a-342f-86e0-5059285ec191 | -8.0207 | -47.1808 | 2026-10-08 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 3cc54445-fc62-3645-8694-54fba7528723 | 1.7121 | -55.6063 | 2026-10-08 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| dd8af0e3-034b-31a8-9ac6-ba242c209ef2 | -6.988 | -59.123 | 2026-10-08 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c517a275-98ae-36de-94aa-29bee6ee707f | 3.0732 | -60.5949 | 2026-10-08 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 2c7e3307-2575-3606-ba5f-f0876eb03cca | -11.619 | -43.6196 | 2026-10-08 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 05f9519b-66c4-3eed-9eb0-f8f626fef0c3 | -11.3986 | -47.5635 | 2026-10-08 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 6481c8a6-3465-3824-8a89-1c03c88f0ab6 | -11.8595 | -47.3694 | 2026-10-08 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 598c052c-512a-3837-a44e-66864ef8542e | -11.3103 | -44.8337 | 2026-10-08 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 5b21a81e-0763-3d46-9d7c-365499eb713e | -7.4694 | -42.8551 | 2026-10-08 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 125.7 |
| 4981123a-5ab4-3df3-be4b-3b2e21667be3 | -10.4724 | -47.2333 | 2026-10-08 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 8c2fdc4a-8fea-3b88-a15b-b46ab5bed921 | -3.195 | -42.9772 | 2026-10-08 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 10b88c92-ea20-3fb9-83fb-4bc496135562 | -8.969 | -45.1313 | 2026-10-08 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 914a686a-55f3-33c7-a2e4-edc0014bea6c | -17.1012 | -41.3472 | 2026-10-08 14:10:00 | GOES-19 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.3 |
| 726a8235-284c-3aec-b06e-27a70963ed47 | -9.4306 | -44.5959 | 2026-10-08 14:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 65b29a29-6fb5-3345-a7a9-f0bf2ed11ce1 | -8.1807 | -46.3433 | 2026-10-08 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 0f47cb9b-eda6-39d2-9a1d-c455009eb072 | -7.2082 | -44.2794 | 2026-10-08 14:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5b79fa29-948e-3539-ac85-2f1ce9617c81 | -3.2919 | -42.291 | 2026-10-08 14:10:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 2600b08f-000d-32fc-be46-ce5f8c5372f3 | -9.9589 | -43.5516 | 2026-10-08 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 4b7883e7-9c94-3f82-870e-cbbc588c9724 | -11.2661 | -45.1859 | 2026-10-08 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 39813da7-edf9-3e9c-80e0-c6faaed81122 | 1.7304 | -55.5863 | 2026-10-08 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 1a04b8ad-23bb-34ff-b998-f5b395b23c44 | 1.6568 | -55.8045 | 2026-10-08 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c19dffe2-8757-3b66-a8d8-cf98154c1c93 | 1.7672 | -55.5463 | 2026-10-08 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f38d18ba-868a-3708-ab82-6552106cb668 | -11.8404 | -47.372 | 2026-10-08 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a07034f8-16d5-3636-a6ee-e70407f48984 | -7.8876 | -55.0023 | 2026-10-08 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8192e2c2-a719-35dd-8ee7-9f31b374dc57 | 1.7855 | -55.5461 | 2026-10-08 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3ac386a0-37d6-3933-b271-7aab9ff9d80d | -6.7368 | -55.1074 | 2026-10-08 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ed0d53a1-bc84-3aa0-b83e-267262a3c3ff | -6.15 | -47.91 | 2026-10-08 14:15:00 | MSG-03 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3cb46ea-640f-360e-a5eb-ccdc2a4cd0ab | -11.84 | -47.3943 | 2026-10-08 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c2c3e4e2-e0d5-3b85-b465-be2f5cba6ec5 | -7.8878 | -54.9822 | 2026-10-08 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| cd90b277-4a78-36fb-840a-86c5d1894dcb | -11.6382 | -43.6166 | 2026-10-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 5e1015d8-38d2-3e9f-a1cb-00a404f42b3f | -9.9398 | -43.5542 | 2026-10-08 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 0c62a54c-087e-35a4-a977-dc73653cb1cc | -9.1483 | -45.8385 | 2026-10-08 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| c52007c2-5f0d-3648-a5b9-124d1f5cff8f | -9.9014 | -44.8147 | 2026-10-08 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| b060aa85-edee-36d1-a76f-d0b35ec9acc3 | -6.4568 | -55.4609 | 2026-10-08 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 49714307-8719-361b-be45-36bb2ff84d5e | -8.1876 | -54.7219 | 2026-10-08 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 178117fb-4d54-3156-bcaf-237c4a9a6d32 | -9.7688 | -65.018 | 2026-10-08 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 58f8992c-903d-3029-afdd-2253ccc7acc5 | -13.1641 | -54.3178 | 2026-10-08 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 49527707-1f9a-3cb2-86c6-bbf5da3dcefd | -3.195 | -42.9772 | 2026-10-08 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 50cc52a2-f1e5-34c0-b4ad-2f93b4f3403f | -10.4527 | -47.2801 | 2026-10-08 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 7634fb56-4ead-327b-b02b-9e0ad383bbfd | -8.5922 | -67.0306 | 2026-10-08 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c2854a42-4da6-34ea-89ae-9b6175075f47 | -7.3286 | -50.8314 | 2026-10-08 14:20:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 86259e80-6eda-33af-95ea-dd243d197933 | -11.2486 | -46.2377 | 2026-10-08 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| c98b59f2-fcbf-31f7-8435-edd59896cbbc | 1.6937 | -55.6461 | 2026-10-08 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 52ff811c-b1dc-3fdc-87d5-d8a020f9b0ff | -10.4724 | -47.2333 | 2026-10-08 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 6b259c71-3841-332f-b946-e744883b3904 | -10.4337 | -47.2824 | 2026-10-08 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 8adc8fb1-481a-3759-a9ee-c2f113f5e56d | -7.2185 | -55.1016 | 2026-10-08 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| fb0d124a-8416-38f7-b514-fe8f91f16234 | 2.1083 | -50.8375 | 2026-10-08 14:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7cc8bcb9-7136-3b20-8cfb-0602c6340644 | -8.9054 | -63.3378 | 2026-10-08 14:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| fc4136d7-b09a-3000-9ed4-53fc6362dc32 | 4.4436 | -60.9278 | 2026-10-08 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 284.2 |
| 8893bd28-6963-3f8b-aa90-5de1d3cd8ac1 | -6.9881 | -59.1037 | 2026-10-08 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ae91030b-ec39-3c9b-affc-f3eb8874185a | -6.7096 | -45.2824 | 2026-10-08 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| bc2d6248-48a9-3881-82e8-039ec44842c9 | -15.5216 | -42.6588 | 2026-10-08 14:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 281.7 |
| 404273ed-c4f1-3161-82c2-36b3f39744a0 | -9.0592 | -65.9209 | 2026-10-08 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c87a4ca5-9078-363e-b778-6cdefb7f6693 | -7.8876 | -55.0023 | 2026-10-08 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| aa9e1bf2-b37a-3565-a2c2-740cf33064cd | -7.2369 | -55.1206 | 2026-10-08 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| fea9aef4-3caf-3e74-8952-caa441779ff2 | -6.8762 | -43.7083 | 2026-10-08 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 0f0f60e9-4854-36d4-85e7-ed171b541d10 | 1.6568 | -55.8045 | 2026-10-08 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0c83f9a5-3ea9-3da8-8f2e-e5877fe4371a | -7.0066 | -59.1029 | 2026-10-08 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 3918addc-98b2-34ea-91ee-37d0d90ca405 | -6.6716 | -45.3308 | 2026-10-08 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 158.6 |
| f19751a1-6251-3d41-8878-3e379a98bcd8 | 1.7304 | -55.6061 | 2026-10-08 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 72259c10-553e-3002-98a9-edd0c8ef3166 | -6.8602 | -41.7494 | 2026-10-08 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| 01cf6a9d-b8fd-3a29-ac41-4d2f5411fb01 | -6.6901 | -45.3519 | 2026-10-08 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 259e427d-3b1a-3fbe-b5b7-f5922b4ca253 | -9.4751 | -64.3336 | 2026-10-08 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 40446cca-224d-30e0-a4dd-b52e715ccf87 | -11.2083 | -45.217 | 2026-10-08 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| f554aeb6-4d88-32d1-a601-7a933645f309 | -6.988 | -59.123 | 2026-10-08 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 842da91c-f179-3135-8228-38431c6ff1e0 | -9.4749 | -64.3713 | 2026-10-08 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0142b101-71fd-37b2-b093-2c74517f3729 | -9.9787 | -43.502 | 2026-10-08 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| c53755b7-37fe-358a-a1a4-6968ca7d43cb | -7.5284 | -45.8885 | 2026-10-08 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 4165431d-006a-30e7-a753-0facd08bcc8d | -11.7935 | -43.5215 | 2026-10-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 32b3c269-c1fd-35ad-aa25-1b096a60e193 | -10.4727 | -47.211 | 2026-10-08 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 174a1b0d-f1ed-33b6-947c-082c2b750727 | -8.2826 | -45.7038 | 2026-10-08 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 2227301f-36e0-3955-bd89-e7b4e2ce33cc | -7.4694 | -42.8551 | 2026-10-08 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 149.4 |
| fe5dd5ca-6de3-3335-af7a-070983533811 | -8.969 | -45.1313 | 2026-10-08 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 8f966abc-c73e-3008-8482-c1f731f83303 | -6.3283 | -55.3276 | 2026-10-08 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d79561e9-f6fb-3030-90a8-35936140d424 | -6.7368 | -55.1074 | 2026-10-08 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 04726167-1c43-3529-a28b-238fb41e914b | -3.2919 | -42.291 | 2026-10-08 14:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1f8a45e7-69da-35fa-9deb-235af44328d5 | -11.8404 | -47.372 | 2026-10-08 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| b5268f48-0ca9-3fc3-ab8c-197e7ef12ecd | -7.2184 | -55.1216 | 2026-10-08 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 94a5274c-6143-3679-9e03-09c250502963 | 1.6937 | -55.6263 | 2026-10-08 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 84f9ac6b-37f9-378e-841e-67ea6256e74e | -6.7366 | -55.1274 | 2026-10-08 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 26ad3d37-5354-3f83-9c53-9e471046f926 | -9.1486 | -45.8158 | 2026-10-08 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| be1c2b3e-6463-33b6-b9ef-aa3a677962b7 | -8.1115 | -50.9206 | 2026-10-08 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 29c46835-210d-39fe-818c-5028512467af | -12.1545 | -44.7547 | 2026-10-08 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 361.4 |
| 1edd4f30-4080-3570-8f65-1c237f263f91 | -6.8764 | -43.685 | 2026-10-08 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 8d6fd997-f83a-3311-9cd7-4b2bddcd0ca6 | -11.8408 | -47.3496 | 2026-10-08 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |


[Clique aqui para ver as próximas entradas](README215.md)
