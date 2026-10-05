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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e5781bb-8f6d-3017-b2f4-0a354d556407 | -5.496 | -42.8178 | 2026-10-05 19:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| d4bcf9d3-a8ad-3a06-9784-1fac10cd658e | -8.6293 | -66.9926 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| b818f50b-1abf-3559-9fa2-08db4cedf7a9 | -8.6214 | -69.5026 | 2026-10-05 19:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 626be202-def2-3035-a65c-d969ff739020 | -10.534 | -68.7055 | 2026-10-05 19:10:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 56.8 |
| cd99049c-894e-38df-8110-854e67bd91eb | -5.9417 | -41.3524 | 2026-10-05 19:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 3cb3e507-c84d-37a4-9000-300b88c03224 | -9.7126 | -65.0951 | 2026-10-05 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 160.0 |
| cb42c145-3a2e-3489-a2d0-b441f2270390 | -9.7127 | -65.0763 | 2026-10-05 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 10b95e93-00b9-3c3c-92d3-9a7c67d12d24 | -5.9606 | -41.3507 | 2026-10-05 19:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 185.4 |
| 7ef9ad15-6c74-325e-8b13-2ed280792588 | -8.5368 | -67.0135 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 70a90214-608e-3a6a-a675-4347c2bc3938 | -9.2199 | -67.3852 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4ba8111c-eae9-3a75-8f3b-cafdaec34ab1 | -10.4781 | -68.7255 | 2026-10-05 19:10:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 46805759-cdc5-30a8-bfdf-22dc7123089f | -8.5367 | -67.032 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| d8d2c662-a99f-3845-8be0-4cb93b85513c | -9.077 | -66.0881 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 98a94822-5317-32bc-b7f1-eed5384ed058 | -8.5929 | -66.8266 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| ec59d986-a519-3074-b410-bd8ba75eb278 | -9.1072 | -67.8326 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| cc2da967-1f55-3ce3-9ed4-a4cf5aa0bb8e | -9.1334 | -65.9 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 8a62b869-a9dc-3125-af63-99fc0de6cd66 | -8.8519 | -66.8012 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 68f0e383-aceb-3e05-8d6d-c1f17ef26880 | -9.7312 | -65.0944 | 2026-10-05 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 143.2 |
| db8e580a-7ad3-3e2c-82b8-be3350b1e189 | -9.0244 | -65.4367 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 48202932-bd28-3cc9-a210-586b7e313251 | -8.537 | -66.9764 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 635e212b-d87f-37ad-8490-986adc6326c6 | -10.6463 | -68.5914 | 2026-10-05 19:10:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 458cdf36-6d3b-3936-84b6-9e5e9f663fbf | -9.2366 | -67.885 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b0966ed6-695c-3eb6-8eee-731a16f50296 | -2.5353 | -65.8819 | 2026-10-05 19:10:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 2bdbe79a-33db-328a-a149-ed66b91311eb | -9.9728 | -65.1232 | 2026-10-05 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 731cfe17-88fc-364b-98bd-db65af6b5e84 | -4.8081 | -42.1577 | 2026-10-05 19:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 177.9 |
| 8ea6b8c6-b8ce-32ee-adfc-61c845b331c3 | -9.3014 | -65.652 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 77d6fbd0-0e9c-391d-a40d-8aad8d3d37ec | -7.4889 | -42.8059 | 2026-10-05 19:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| d9a75443-29ac-33fb-80d9-0a4f9deff8b4 | -7.47 | -42.8078 | 2026-10-05 19:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 8eb77e0c-8e78-3fd0-ad00-fa4afe5fd1a6 | -6.8952 | -43.6833 | 2026-10-05 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 167.9 |
| ccad6a1d-b691-3e95-83d4-f4eca79f4bf1 | -9.1535 | -65.5634 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| cf18faf7-0bf6-3b4b-87b1-733643a1f6f1 | -9.4751 | -64.3336 | 2026-10-05 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 3cb3642e-c0e9-391f-a8f1-9cd61541bef0 | -5.3985 | -39.1078 | 2026-10-05 19:10:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 1b42bba8-3161-3c1b-b727-e65d58ca1fc7 | -9.3443 | -68.9177 | 2026-10-05 19:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 18016169-a6e2-3626-97d3-53c114028872 | -4.5091 | -42.0584 | 2026-10-05 19:10:00 | GOES-19 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 164.8 |
| 82926046-b39c-3f68-96ee-e3f9d8b6e9ec | -9.4565 | -64.3344 | 2026-10-05 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 3bdb8661-3404-3b4b-96b9-65bec5ebe535 | 3.5254 | -51.5057 | 2026-10-05 19:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c643f440-a75b-31f1-a7c3-f0c15d531cfb | -9.363 | -68.8619 | 2026-10-05 19:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f76bba13-91a7-3d66-8ccb-da501d08f367 | -5.809 | -43.4491 | 2026-10-05 19:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 3217512a-e005-3a2a-af6e-05157afa551a | -9.0429 | -65.4361 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 76fb7676-c7b3-3f2a-b2b3-9690b484ce71 | -8.5183 | -67.0139 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| cf46f239-3b80-3936-9e71-8624b6f95cf2 | -9.7313 | -65.0757 | 2026-10-05 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 9bac9506-97b8-3d53-9fd1-05a849fa7c57 | -5.97 | -41.35 | 2026-10-05 19:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6e0f6cdc-3e10-3a0d-969a-4b5db95a8874 | -11.13 | -45.98 | 2026-10-05 19:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cdb68800-3979-3f0f-a805-f8b1961ed8aa | -11.69 | -43.68 | 2026-10-05 19:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21ec26ad-df54-377f-937b-df70207daf5a | -5.97 | -41.39 | 2026-10-05 19:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 186f4ecb-36b3-38cf-817f-033147647feb | -2.79 | -57.66 | 2026-10-05 19:15:00 | MSG-03 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 054d99f2-786f-38b3-a5fc-f6832deb0e8c | -4.509 | -42.0822 | 2026-10-05 19:20:00 | GOES-19 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| a8fffd13-2e39-37ad-abdc-881e5cae055e | -9.1442 | -67.8317 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 391801ba-4635-3a27-bc04-1ffbe0dbdbf5 | -9.7126 | -65.0951 | 2026-10-05 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 184.8 |
| e1530bc2-2383-345d-8d7e-305e4a9b6304 | -6.4279 | -43.4686 | 2026-10-05 19:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 7246a12d-ed61-34db-8ff0-1cfead3849e2 | -9.2367 | -67.8665 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 83dd8824-95c9-3573-892a-a9318c25e482 | -9.1426 | -68.2941 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 5920bcd6-1764-3d81-b8c2-70866c003e9b | -8.6214 | -69.5026 | 2026-10-05 19:20:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1c27447c-0239-34fe-a050-c44bf3f88a98 | -9.1535 | -65.5634 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| bc314190-f41b-3e47-9839-fed1a5905765 | -9.1613 | -68.2568 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 6b313250-1f93-3fb0-a200-e179db5033b8 | -9.1072 | -67.8326 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 245d35f4-31fe-384d-a5a5-9670ab909ea1 | -8.5929 | -66.8266 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 92bb97f1-5166-3e31-92eb-96a98fe00314 | -9.6672 | -66.834 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 65b40410-a7bc-31b4-8e13-1ed688e29f5d | -9.077 | -66.0881 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 9d1febf3-f7c9-32f9-98d3-d4a19f350739 | -9.1076 | -67.703 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 309fe06a-7c3c-36ba-988f-646a3aacb59c | -9.1257 | -67.8322 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 14e9962c-da1c-35e3-9f3c-d48aebe32510 | -8.593 | -66.8081 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 73f0ae84-76ab-3f8d-a10f-ef0d67864d9d | -9.1429 | -68.2202 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 2d829a5a-ca2d-3622-a9f1-01dc09782ffe | -9.4565 | -64.3344 | 2026-10-05 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.5 |
| f5e88b36-eef7-3590-b9bd-03aca3e37b4b | -5.9606 | -41.3507 | 2026-10-05 19:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| 87abf9c0-bf89-3edd-8143-e3df1c1e583b | -9.0429 | -65.4361 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 846f4b75-c11d-3155-a39c-04b45d096fbe | -9.4958 | -63.9562 | 2026-10-05 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.8 |
| db958826-7b1a-319f-b515-cef8b475398d | -9.4783 | -67.6752 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fba76c39-ffe7-337e-9224-5c8b85c30c57 | -9.0982 | -65.4904 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| db3c37d9-d3ce-387d-a4eb-1e403ea39c47 | -2.5353 | -65.8819 | 2026-10-05 19:20:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 4ec24f60-140a-35f3-bc12-4f2b23edba5f | -9.7127 | -65.0763 | 2026-10-05 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.2 |
| e20d62e8-3a55-30f2-814a-519a89643fa0 | -5.1303 | -44.0074 | 2026-10-05 19:20:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| dc57d1f7-9a0a-3751-b81d-d7abf98513f3 | -9.1257 | -67.8137 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| f67db215-db3d-3b02-9c25-8e3ca275f494 | -4.8083 | -42.134 | 2026-10-05 19:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 166.8 |
| d0c8fd1e-2689-3066-b50f-f4e6b29b2059 | 3.5254 | -51.5057 | 2026-10-05 19:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 34998050-f5ee-3cfb-9bed-840c806e3a65 | -9.4751 | -64.3336 | 2026-10-05 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 13324ffb-c785-32b7-8ee9-842fc2b94272 | -9.7312 | -65.0944 | 2026-10-05 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 189.6 |
| 263b7998-60a9-3994-86e7-5e168744abd9 | -8.5183 | -67.0139 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| f17bef5d-bb87-3a8c-ae04-770e2d4aef2c | -9.1072 | -67.8141 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.9 |
| cb288be5-48af-34c3-bef4-38b77e734835 | -9.2199 | -67.3852 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0f1ea831-0400-31ae-8a5b-95f57cdc8614 | -9.7313 | -65.0757 | 2026-10-05 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 112.8 |
| ad4fab15-43a5-36c5-b134-5366a58add72 | -10.5541 | -68.3338 | 2026-10-05 19:20:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e749d1c9-8e86-3792-a5c9-99c7d8d1ccb9 | -4.5091 | -42.0584 | 2026-10-05 19:20:00 | GOES-19 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 9bddb5f3-5383-3b2b-8658-06d66e25fadb | -9.0614 | -65.4355 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| d5cfb5de-29ba-3f52-9fd7-981e683ef345 | -10.3503 | -68.0234 | 2026-10-05 19:20:00 | GOES-19 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 93b23cae-a23d-3be0-be20-c8c85a367f35 | -4.8081 | -42.1577 | 2026-10-05 19:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 267.4 |
| 01e68f40-046d-3681-95b8-3727baf7d473 | -8.3526 | -62.8302 | 2026-10-05 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 39d6b30f-20bd-3a4b-a54c-7bd8688fbf6f | -9.1613 | -68.2383 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 950be408-da79-32b3-9d09-06b4cccfde54 | -9.1243 | -68.2206 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| d917ca36-d69d-331a-bb88-5f400bcd10e7 | -9.1428 | -68.2387 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 2699659c-6779-3f21-a875-ff83f879d573 | -7.47 | -42.8078 | 2026-10-05 19:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 4e9f445d-19e6-3b58-9ced-591bd4823238 | -8.8519 | -66.8012 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 43789956-a184-32f1-8b4f-07ef068b1cb2 | -9.1075 | -67.7401 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 43fd6969-aacb-39eb-ae90-62a35c0150b9 | -5.1305 | -43.9844 | 2026-10-05 19:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 85a51830-ec82-3d29-98d7-0bde410f0cb2 | -6.914 | -43.6816 | 2026-10-05 19:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b20ae484-df4f-3c37-a429-e7fc51627034 | -9.1241 | -68.2946 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 2f0f1641-3da7-3bdf-bc90-b91ab202357e | -2.5535 | -65.8634 | 2026-10-05 19:20:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| b5c0c1cc-2fa6-3ddc-bb0d-7d7a03d9f103 | -9.2366 | -67.885 | 2026-10-05 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 7362b8c5-71c7-3921-a0ea-e19b87ac8bb0 | -9.0045 | -65.7174 | 2026-10-05 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 01f60834-0493-3735-8281-3d1433865e51 | -6.8408 | -41.7994 | 2026-10-05 19:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |


[Clique aqui para ver as próximas entradas](README167.md)
