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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac28ba36-e648-3144-b4c6-a55d1f9c712f | -6.8412 | -58.9746 | 2025-08-27 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 031d3c17-b734-3e56-84f0-0f084977fa2d | -8.948 | -65.9429 | 2025-08-27 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| ac2b201c-831d-3ae7-b77d-0ff593210274 | -12.8036 | -48.1294 | 2025-08-27 07:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b3398515-3bb5-3b0c-8c9e-e140f83da3a1 | -6.4355 | -44.5764 | 2025-08-27 07:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 4dc4f02d-e070-3cf3-a1e7-612fd8d6f85b | -8.9664 | -65.961 | 2025-08-27 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2a4c756b-aced-3b1c-986b-ca027abc94f3 | -9.4062 | -60.5326 | 2025-08-27 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| c0c0dd17-b164-3c76-942a-a77fd05d4cde | -8.948 | -65.9429 | 2025-08-27 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 985bc0ac-ed74-3646-a096-a2a478957ce1 | -14.4109 | -51.9269 | 2025-08-27 07:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 85521939-3eab-35fc-9657-5cde589941d9 | -6.8412 | -58.9746 | 2025-08-27 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 55370811-71bb-3f1e-b012-1fad904ed434 | -8.9295 | -65.9435 | 2025-08-27 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 053a340a-bf93-3ef7-be8f-1673435ac3eb | -14.3904 | -51.9935 | 2025-08-27 07:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 229bc254-5478-3beb-8c1a-455b3d56fad5 | -9.4064 | -60.5133 | 2025-08-27 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 90bf48e4-6099-3f90-8240-f9a65cc2d812 | -9.6574 | -64.9845 | 2025-08-27 07:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 1bc5682d-56ae-3dd2-b532-00cf1cf477ce | -14.3915 | -51.9294 | 2025-08-27 07:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e16033f4-6ee8-3bec-a5c2-1ade3003968b | -8.9296 | -65.9248 | 2025-08-27 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 819754af-acf6-329a-bb56-d7b16312def1 | -8.9479 | -65.9616 | 2025-08-27 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| b133c3c9-6cdc-37ac-92ec-57e8b5cdb8f9 | -8.9294 | -65.9621 | 2025-08-27 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 0f2c807d-1ad0-328e-ba90-2ecb6953ea9d | -6.8413 | -58.9552 | 2025-08-27 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b1effae1-0378-30ba-9325-5145c81957e5 | -8.9296 | -65.9248 | 2025-08-27 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 94106b36-375a-3cbc-af2d-50fa61360c6a | -8.9664 | -65.961 | 2025-08-27 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5da6c360-e921-37cd-8821-c421e375a28f | -8.948 | -65.9429 | 2025-08-27 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 681b46cd-7b33-38a7-afce-cd9f068c8c0b | -14.3915 | -51.9294 | 2025-08-27 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| d43f9a6e-92d2-387e-ba6f-e284fe814dda | -8.9295 | -65.9435 | 2025-08-27 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4e0bed93-2f11-3351-8010-c031d31f5f39 | -9.6574 | -64.9845 | 2025-08-27 07:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 66d60bcd-db3d-3340-ade1-c3f59af27a62 | -8.9479 | -65.9616 | 2025-08-27 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| e904532b-38df-3eb7-953b-70fc550fe3f8 | -14.3904 | -51.9935 | 2025-08-27 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| a4a8073b-308a-34e4-a129-39f68bef0f91 | -6.8412 | -58.9746 | 2025-08-27 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c19de3f6-2679-33d7-a44f-fd2fbda02447 | -6.8413 | -58.9552 | 2025-08-27 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| c08f5e84-6ab7-3808-8502-b11925d20d62 | -9.4062 | -60.5326 | 2025-08-27 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 91372fd6-a69c-39a0-91e1-39f35f90f737 | -9.4064 | -60.5133 | 2025-08-27 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0eda2592-20e6-3dd5-b34c-88676937bfb0 | -9.6574 | -64.9845 | 2025-08-27 08:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c34cd8c0-6008-3cfa-8ae5-31288bb4ea84 | -8.9664 | -65.961 | 2025-08-27 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ee347e15-b2c2-3545-a266-21fbd8f89ad7 | -8.948 | -65.9429 | 2025-08-27 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 0cfdc799-ea8e-3d1d-a979-fb14bb905f2a | -9.4062 | -60.5326 | 2025-08-27 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 0d2d494f-c492-302d-998c-f82120809cd3 | -6.8412 | -58.9746 | 2025-08-27 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 440e01f0-6b73-30c5-9668-4526181580ce | -9.4064 | -60.5133 | 2025-08-27 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 32eb2c8e-f48e-3050-8c45-e3df01840497 | -6.8413 | -58.9552 | 2025-08-27 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 89efbac2-aa09-31b6-b7e4-bef4e82ab35c | -14.3915 | -51.9294 | 2025-08-27 08:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ed2ed8b7-aaee-349a-95dd-6cd715f6d460 | -8.9295 | -65.9435 | 2025-08-27 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d528cef7-bb10-3a4b-af97-c64baff359d4 | -8.9479 | -65.9616 | 2025-08-27 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 602756e6-4dbd-3b18-b2e9-4173f2e425cb | -9.4062 | -60.5326 | 2025-08-27 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2d9e3954-6c2c-3bb0-9f28-2ab711878a51 | -8.9479 | -65.9616 | 2025-08-27 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.6 |
| c73d274d-724b-34de-953d-a74116404091 | -6.8412 | -58.9746 | 2025-08-27 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e3d23540-ce07-3236-bfbd-12f73a3a9c0e | -9.4064 | -60.5133 | 2025-08-27 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 3f6a0914-5cc3-3c4c-8771-b0d813014fc1 | -8.948 | -65.9429 | 2025-08-27 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 2b72a8a3-e4fc-3227-ab3c-93842c46186b | -6.8413 | -58.9552 | 2025-08-27 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 11fd8390-a27a-32f1-a46b-bd48bd07e15b | -8.9295 | -65.9435 | 2025-08-27 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3676e975-e843-3beb-9cf0-0d25154f7af6 | -14.3915 | -51.9294 | 2025-08-27 08:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 52d01963-f9de-3bdd-866b-e6e53d6e451e | -8.9664 | -65.961 | 2025-08-27 08:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7044dbe1-a935-3bb7-b41e-984c3b7bea1b | -8.9295 | -65.9435 | 2025-08-27 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 90b4b19d-e7d8-3247-9472-7b25beae5957 | -8.948 | -65.9429 | 2025-08-27 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c27c1f73-b9ec-306d-983c-89bc9f31b773 | -6.8413 | -58.9552 | 2025-08-27 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 75004347-80de-33db-8b81-6cee76420d63 | -9.4064 | -60.5133 | 2025-08-27 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| dcbfb076-d43a-339e-b3b2-013e091cc393 | -8.9664 | -65.961 | 2025-08-27 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 6bae4db7-b907-3803-b6d2-d3fb9a385ee7 | -6.8412 | -58.9746 | 2025-08-27 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 116ea49c-1adf-3fc5-a9a4-bdc42f3f14c4 | -9.4062 | -60.5326 | 2025-08-27 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 60fc76b6-c652-3367-86ef-61efcd3a9d7f | -8.9479 | -65.9616 | 2025-08-27 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 720f146c-75dc-395e-83a0-9f0b572e7267 | -12.7843 | -48.1321 | 2025-08-27 08:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 06bcb9c1-e1af-3e12-a29a-0891761f2661 | -8.9479 | -65.9616 | 2025-08-27 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 9eec0b9d-59ba-32d9-b8b9-5a568bffa89f | -12.8036 | -48.1294 | 2025-08-27 08:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 692380f5-c949-3789-bb81-31514d022225 | -9.4062 | -60.5326 | 2025-08-27 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| b1664404-062e-31fd-bf1d-0016fd9a994e | -6.8413 | -58.9552 | 2025-08-27 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ce2fce11-116a-3d28-bdbe-d86ed551bca6 | -6.8412 | -58.9746 | 2025-08-27 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 2b52d08b-70cf-3d41-bfbe-2a56b3b6be0e | -10.2743 | -64.4907 | 2025-08-27 08:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 6aecca31-6630-317e-86ce-dc3b020fb79f | -8.9664 | -65.961 | 2025-08-27 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| bb329c3e-0239-3dfd-8f41-8a64f2c7dadd | -9.4064 | -60.5133 | 2025-08-27 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 672cb912-84a7-3965-8176-09f44991c91c | -8.9295 | -65.9435 | 2025-08-27 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 90111067-4b1f-3afb-8341-1af0f83c2c8a | -8.948 | -65.9429 | 2025-08-27 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4a29dd21-88cd-3972-8348-5e68a7e51749 | -8.948 | -65.9429 | 2025-08-27 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 293def8f-d4b5-379d-8f35-746e4b0ce1aa | -9.4062 | -60.5326 | 2025-08-27 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 08f52583-03a1-3359-9f35-9bffb23dc929 | -8.9479 | -65.9616 | 2025-08-27 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 64b71da7-b4ab-3cc9-81b9-0d443b294442 | -8.9295 | -65.9435 | 2025-08-27 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 18e56b04-43de-3a3a-a270-27a73eac308e | -9.4064 | -60.5133 | 2025-08-27 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 8415fe63-775a-3aff-8f8c-b63dbc377b77 | -8.9664 | -65.961 | 2025-08-27 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| dc11b4cd-353c-3e77-a89c-1bbb8ee78617 | -8.9479 | -65.9616 | 2025-08-27 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b0fd3595-4a49-3d7e-95a4-d0d6082e1c31 | -9.4064 | -60.5133 | 2025-08-27 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c63999cd-1d93-324d-b142-6d276b6a2038 | -8.948 | -65.9429 | 2025-08-27 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8d7b4b71-447a-3aef-9fdc-a685dd05f137 | -9.4062 | -60.5326 | 2025-08-27 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 11cc68ee-8db7-3671-8785-48858fb7b414 | -8.9295 | -65.9435 | 2025-08-27 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4d61fb20-c812-3703-8451-f40d22067b4c | -8.9664 | -65.961 | 2025-08-27 08:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b5133beb-1d59-3303-ae4e-f225748cd4c2 | -8.9664 | -65.961 | 2025-08-27 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 72cc146c-9f24-3084-866d-d2958ccb814d | -8.9479 | -65.9616 | 2025-08-27 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| c9b8a820-bac4-3faf-b608-1dfe95619ba3 | -8.9295 | -65.9435 | 2025-08-27 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 422657e4-bf60-3090-b33c-8037a9e8ffe9 | -8.948 | -65.9429 | 2025-08-27 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ea15665b-54e3-3692-8e37-3dbba07f4273 | -9.4062 | -60.5326 | 2025-08-27 09:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6691d3f8-41d9-3d22-8616-b26575fb1133 | -9.4064 | -60.5133 | 2025-08-27 09:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 87ff44fd-bb40-3f4b-aa18-a7b7d2367f8e | -6.8412 | -58.9746 | 2025-08-27 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6465361f-5840-347a-9a86-2d720e9b5b3d | -9.4062 | -60.5326 | 2025-08-27 09:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b1d4f8ec-e56e-3c1a-80a7-4cb80ae2de7d | -8.9664 | -65.961 | 2025-08-27 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5fb6c1bd-7e89-30a0-b51a-d458c1b8689e | -8.948 | -65.9429 | 2025-08-27 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 69dda28f-c0b5-347a-86f3-08fc6c2c2421 | -6.8413 | -58.9552 | 2025-08-27 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c04bb8a6-b771-3b04-8787-31c0e9ddbf6c | -8.9295 | -65.9435 | 2025-08-27 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 25cedbc0-e4c8-391f-8a28-6bfd719e94c7 | -9.4064 | -60.5133 | 2025-08-27 09:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 39b7d330-780c-35f5-841f-6639670ade0d | -8.9479 | -65.9616 | 2025-08-27 09:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 13de4381-3e84-3201-bb6a-a69333fef65b | -6.8413 | -58.9552 | 2025-08-27 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 86df3cab-1e8c-3b7d-9451-a50b65f081ad | -6.8412 | -58.9746 | 2025-08-27 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c6ae55cd-b5be-37c1-bbf0-cbeeae63418a | -6.4355 | -44.5764 | 2025-08-27 09:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 4648345c-78cf-3432-8d98-b8b04c408691 | -8.9479 | -65.9616 | 2025-08-27 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| d047a138-cdda-336d-8b98-f53d53e6258c | -8.9295 | -65.9435 | 2025-08-27 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ffcc1b8c-89ef-3f91-8bcd-bbd178f21742 | -8.9664 | -65.961 | 2025-08-27 09:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |


[Clique aqui para ver as próximas entradas](README89.md)
