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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12b0077f-48ef-3fdb-b818-dbb0bad9c493 | -16.9161 | -57.680801 | 2024-10-06 01:40:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9875bf27-75cf-3c85-841f-691ff3163293 | -16.9179 | -57.688702 | 2024-10-06 01:40:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47da4a72-8cf1-3504-bb47-9c466cab4cad | -16.9198 | -57.696602 | 2024-10-06 01:40:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2db72ce-1585-32dc-8eeb-4d24014ac02f | -16.9216 | -57.704399 | 2024-10-06 01:40:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 436d077f-b1e8-3e99-b866-d8786fb2ec0a | -16.851801 | -57.452801 | 2024-10-06 01:40:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5f9ae55f-9788-38ae-a532-149e67dc02fd | -16.9063 | -57.6833 | 2024-10-06 01:40:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0932cc6b-113d-36e2-abbd-a5c53c7b4dba | -16.9081 | -57.6912 | 2024-10-06 01:40:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7b7dac6-955a-3351-a416-f668e57f269e | -14.5471 | -48.793201 | 2024-10-06 01:41:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 84cbfcef-e5df-3b4d-afab-de06f1377a15 | -14.5376 | -48.796101 | 2024-10-06 01:41:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cbe47be0-d10e-3a2a-94a2-24bb69038560 | -16.8402 | -57.447201 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 694be213-9927-3525-bd6b-5a8796e90dfd | -16.8421 | -57.4552 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 081db9bc-3f71-3240-936f-fa964d2a6d82 | -16.828501 | -57.441601 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58c856bb-5857-3285-b8a3-81835da1ae21 | -16.8304 | -57.449699 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24f84da7-393f-3e52-a601-9c96138e1669 | -16.8323 | -57.457699 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52817714-1517-350b-bb7d-d3fa5d7faf1d | -16.8169 | -57.4361 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ef69fe1-6f96-31b6-b580-ecae74e7f850 | -16.8188 | -57.444099 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 574c9644-06b5-3359-97bb-ef1a2d47a3e4 | -16.8207 | -57.452202 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33cdca16-ba76-3f48-be8b-6ea5f71f9a71 | -16.822599 | -57.460201 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74733758-0b31-3eb0-9b0e-0915fc5ccfda | -16.8071 | -57.438499 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33a5d82e-148a-3f87-a63e-ca002de72967 | -16.809 | -57.446499 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bccf55fa-63c1-3a3a-943b-395a117b03e1 | -16.7838 | -57.427299 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8cbc2b7-b646-35fc-9d5a-8f81c69fd686 | -16.7857 | -57.435398 | 2024-10-06 01:41:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99aceda3-d902-3b73-bc43-79956155efc1 | -16.774 | -57.429798 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 284ca5e1-54d9-38c6-950e-e7fbca826f87 | -16.7759 | -57.437901 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aae994d8-b36a-3e0b-a146-951ca07c1964 | -16.7778 | -57.4459 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a7ac45a-bb3e-3a2c-b45e-e81a1d4dfa4d | -16.781601 | -57.462002 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 78aa8aa7-8a77-3a67-8ea0-616028bd6a06 | -16.6982 | -57.154701 | 2024-10-06 01:41:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3fe00a3e-d65e-3208-922e-bac2f99cd82f | -16.764299 | -57.432301 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ac0bb6d-68fb-3f5b-b4d8-66f5178efd36 | -16.766199 | -57.440399 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f270c9e4-b1e2-3da0-8e91-30b9901d892e | -16.768101 | -57.448399 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 162fe6bd-72fc-3cb2-8b9a-6f695126e6dc | -16.77 | -57.456402 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ce2eaff-f245-37c9-a81a-0960a1c59218 | -16.7719 | -57.4645 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be50cad9-7208-3797-b076-b0a6429b0058 | -16.7738 | -57.4725 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4ea57c4-925d-3439-9b7b-bde3dc33b35a | -16.7757 | -57.480499 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f740cf7-c9c4-3e41-bcf0-86e4d278c811 | -16.777599 | -57.488602 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3341d08b-1f59-33eb-9f2d-f7d9a052d4ba | -16.779499 | -57.496601 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ec6cf4e-f242-317b-82c9-d6f21b068af5 | -16.760201 | -57.4589 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bbf8f1ac-cafd-369f-be93-852769842f54 | -16.7621 | -57.4669 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77b9315f-3f20-34f5-8771-75e81dd955b3 | -16.764 | -57.474899 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7cffd827-e844-3a65-9f4c-e14e8966b244 | -16.7659 | -57.483002 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 041bb069-d666-3f96-8ed7-9d3863539d5c | -16.767799 | -57.491001 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 42fba377-7e43-3733-8d0f-4695f860f2fc | -16.7561 | -57.4855 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a8bdc66-0d71-3605-b669-935d4de64849 | -16.757999 | -57.4935 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c78a1fd6-992e-3ca0-8fdc-659b3e2580ac | -16.829 | -57.794102 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 464889da-4c35-3b99-ad8a-6136a51c05ad | -16.830799 | -57.801899 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 822dc0bd-9ccb-3ce0-83ed-f46de1b7dad6 | -16.8326 | -57.8097 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26bc92e0-bd74-3917-9327-618aa110d4d8 | -16.820999 | -57.804298 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89cd3093-9580-33f5-a132-45f72dd36e9a | -16.822901 | -57.812099 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fd034733-b81d-3894-a489-393679d3b716 | -16.729 | -57.458199 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c33b4fa1-1ebc-3431-92bc-213038330c5b | -16.813101 | -57.814602 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb3eccc3-c588-33a3-b8ed-34d48a71b0db | -16.815001 | -57.822399 | 2024-10-06 01:41:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 914d5e83-9d52-3ce1-8ef7-7327357975e4 | -16.805201 | -57.824902 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e028e6e-2c5a-3ac2-92ec-039edb97b7b0 | -16.637699 | -57.161301 | 2024-10-06 01:41:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6a71571-d180-3074-ade2-44fb9971c366 | -16.7038 | -57.438999 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 23d9b3d3-5b73-3b60-985b-86b42c9b532c | -16.7057 | -57.447102 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fbea7103-86d0-315e-8854-2dc59809ee02 | -16.7076 | -57.455101 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a74f1941-5ce8-369a-aa1d-591ac900ad45 | -16.709499 | -57.4632 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef2d4c10-4c21-3f0a-a95e-5fa8ad6864f0 | -16.7955 | -57.827301 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46588d39-6a2d-3e9a-bede-86337228a4b3 | -16.7973 | -57.835098 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 758b3c88-491f-3588-9b1b-273968525a5e | -16.625999 | -57.155399 | 2024-10-06 01:41:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b572292-75d5-3e9f-ba2f-4d7e79b01efb | -16.695999 | -57.449501 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 36cc0999-d09a-33d3-92dc-ea0141b302c8 | -16.697901 | -57.4576 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e04c9766-23fa-3ce5-9f40-300fad362b21 | -16.6998 | -57.465599 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32a83e66-8616-3975-b530-16d0aee94738 | -16.6143 | -57.149601 | 2024-10-06 01:41:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46626630-af33-3f5d-a592-68b4bdf42b2a | -16.616301 | -57.157902 | 2024-10-06 01:41:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce72918c-df05-3fd1-a948-b3796b512990 | -16.6182 | -57.166199 | 2024-10-06 01:41:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8c4d786-4640-3831-b57a-472afa686a45 | -16.6824 | -57.435799 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 27b614ef-6b1a-3574-af9b-314a9a654ea7 | -16.684299 | -57.443901 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 346e722a-63c0-3073-b692-f76031195dc4 | -16.686199 | -57.452 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 320cfd28-fae5-3654-baa6-968c5b5dea06 | -16.688101 | -57.459999 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea417a12-6f48-39d7-a0b3-1a44d864c7ef | -16.774099 | -57.824402 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 342a0d4a-e4f4-369b-bbd1-9c45446fa202 | -16.6745 | -57.4464 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a99388d9-1638-3bf0-a4e5-1a534fc10e61 | -16.676399 | -57.454498 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d08df5a6-61a6-348f-b0d1-c088ef14d1f1 | -16.678301 | -57.462502 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57bf2324-7cec-35fd-a65a-76023841fef3 | -16.602699 | -57.187698 | 2024-10-06 01:41:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1514be0-dfc4-3fef-88e0-586abc01e0ad | -16.6047 | -57.195999 | 2024-10-06 01:41:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c8ae078-1de1-38b9-b2c3-b3ffe6d5c4fb | -16.6066 | -57.2043 | 2024-10-06 01:41:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a54a749-538a-39d5-b36b-cc94258f692a | -16.6667 | -57.457001 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ddbc5c8-962c-35f3-8503-dfca09025dfe | -16.6686 | -57.465 | 2024-10-06 01:41:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96e72148-2ae5-32a6-a298-707eebe91033 | -15.0457 | -51.194599 | 2024-10-06 01:41:03 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b35c26b7-71b4-3027-ade5-f60b13542b95 | -15.051 | -51.214401 | 2024-10-06 01:41:03 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 39f4d832-a558-39b6-8647-81efe910405d | -15.0361 | -51.1973 | 2024-10-06 01:41:03 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0e831d84-feb1-3004-a091-bfaf359286c6 | -15.0414 | -51.217098 | 2024-10-06 01:41:03 | METOP-C | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f900fa2-674d-3ac5-baa5-b6f86580f504 | -16.5949 | -57.198399 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6eea5a57-dd3c-32e9-b52b-67351113437f | -16.5968 | -57.206699 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24271b4d-8393-3b8a-a223-501e2167969b | -16.598801 | -57.214901 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47ee7104-9ffa-3c64-b380-e572dc3c9d53 | -16.5732 | -57.151299 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9158f21d-4547-31eb-a6b0-470f51681daf | -16.575199 | -57.159599 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56d9d4a0-5f79-3151-b5c7-0cae80cc9452 | -16.587 | -57.209202 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 14c5ccf0-d9ae-39b8-b776-66afa3a567e6 | -16.589001 | -57.2174 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fcd919e6-87fb-3fd1-8f5b-881bce5780e8 | -16.563499 | -57.153801 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1cbe5e4-2109-34c8-a2a4-4ce0a0511331 | -16.5655 | -57.162102 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e89ce8d-6b79-3654-991c-18fcc278c97f | -16.563601 | -57.197701 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09cba8bf-b815-3765-b374-078f0c521e6a | -16.565599 | -57.205898 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e90a363-87b8-3005-8884-b059f3cefbe9 | -16.567499 | -57.214199 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac42b977-22db-3cc8-b405-c37bea0d8a73 | -16.5695 | -57.222401 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be36359c-fd31-3451-87b1-1fb345f0a282 | -16.5539 | -57.2001 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f587e25-d641-3e6b-8ddd-9352c9097074 | -16.555901 | -57.208302 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ceedc01d-ea99-39fc-ad06-5bca295b7cce | -16.5578 | -57.216599 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a3183c6e-e192-3102-83c1-9b66776a4aeb | -16.5441 | -57.202599 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README30.md)
