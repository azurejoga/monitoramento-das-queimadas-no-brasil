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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53d300c1-3627-3d83-b4cd-5882f07a9d30 | -10.41813 | -50.70846 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 041a6eee-0f07-31ee-8d84-bc8145ee7bbc | -10.41796 | -50.72683 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a03c99d2-67af-3db4-b8c3-a418c8b40a4c | -10.41751 | -50.71212 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 256533db-edbf-3367-a14f-5679fdf854b6 | -10.41712 | -50.70781 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e1baf60-01ce-3a7f-8674-06e858a409a8 | -10.41689 | -50.71579 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09d42f6e-9fda-3e7f-a6ab-a1699a77eac7 | -10.41647 | -50.71147 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70d36c87-efaa-378c-8aa7-7edae2e789d4 | -10.41626 | -50.71947 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f97b2631-40c9-312f-8099-71979acc6fca | -10.41582 | -50.71513 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25466774-3dd8-36f2-9c8e-21fe77834616 | -10.41564 | -50.72314 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 914f7199-6b77-38a3-a6cc-cd45bbea4f8f | -10.41517 | -50.7188 | 2024-10-10 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1721eb66-1c6e-3e64-97d8-1cd7df594f38 | -11.48161 | -51.85934 | 2024-10-10 04:19:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| babf80b8-f669-3060-b110-fc95e7596fb3 | -11.48088 | -51.86347 | 2024-10-10 04:19:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2dd2625-5a42-3d5b-9259-4170335594bf | -11.32454 | -51.42339 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d21bd91-b728-3303-8597-fe1076e066f9 | -11.29958 | -51.04766 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f8ef3e9b-45d0-3210-a31d-59da2bb775fd | -11.29547 | -51.04692 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 56fba130-cffc-3590-adc8-d00cab1c0e0a | -11.29482 | -51.05064 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e445de40-f04e-38c6-9c73-7647fb725967 | -11.29371 | -51.08141 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81fdb83a-9ca6-3d72-85e1-0d1055bfaa0d | -11.29221 | -51.06559 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49718742-25a7-34af-8dd5-eb0d5ef58eaf | -11.20838 | -51.34666 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e8e8720-913c-32f4-b630-feaf190c5cb2 | -10.99851 | -51.26109 | 2024-10-10 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65a12844-d1d0-317c-875c-7abdb43c197a | -11.99426 | -51.91919 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 847ac3c4-512b-3cea-9421-819dad28007c | -11.99352 | -51.9233 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fccd34f4-33b8-3dae-9aae-68ad1a32c79a | -11.98922 | -51.92247 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6f8d064-42a4-3dc9-b1ca-352ec3c6f4f9 | -11.98493 | -51.92162 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bbf86512-2318-3923-92e5-8383b9a373f2 | -13.18801 | -51.71024 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc42b319-e42f-349a-954b-33a8ff595d5f | -13.18246 | -51.71711 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be04aec3-fc9d-334c-9453-423ec478b1c3 | -13.17973 | -51.68481 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3abae061-f62b-3af4-b01b-42fb04f17bf3 | -13.17904 | -51.68863 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f266a854-63fa-356a-998e-e6dee9cfc670 | -13.17902 | -51.71232 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae845bc2-c2fd-3524-bbc3-cefc6f49b2b1 | -13.17831 | -51.71625 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47bb361b-dd1c-363e-bf61-4a9f8d8e36aa | -13.17767 | -51.67258 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| addaed96-c5b8-31a8-ac55-20a3415dc1b9 | -13.17561 | -51.68388 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2cbbe6c-ef16-30b9-9b0c-a72e0c209138 | -13.17491 | -51.68768 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f67145d1-0b78-3a87-9fb0-0a0e6f784a50 | -13.17486 | -51.71155 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ada17a3-4ee0-3407-aa23-91e828237de9 | -13.17421 | -51.69152 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93c7099a-c540-3c35-b2b5-570231d95e0c | -13.17421 | -51.66798 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e29dbf0-deb8-3314-8dbf-6ab7b2b0492d | -13.17415 | -51.71544 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 574e0ff2-635a-380d-aa0a-d433ebb9c64a | -13.17323 | -51.66899 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa990029-25f6-35ff-a3f9-98e283883a02 | -13.1728 | -51.69926 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83459539-d0af-38d2-acc7-1ff271622b7e | -13.17148 | -51.68295 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc06bd37-efc4-34d8-9e07-49e5db1f8e4b | -13.17126 | -51.68022 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60b2bed6-d085-34aa-bc44-b2b4c0339fbb | -13.17079 | -51.68674 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8206a9e-8675-3cf9-b85b-d202f5757873 | -13.17008 | -51.69062 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b65763f-0e71-30b5-92c4-75c92a1a62dc | -13.16999 | -51.71465 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f4aecc0-cb4b-3699-b4c7-ae7fd7301cd2 | -13.16993 | -51.68781 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93458c32-62e4-374a-b796-d83611fb0ce2 | -13.16936 | -51.69452 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52e30fcd-67e5-3299-a433-fe8ead9644b9 | -13.16924 | -51.69172 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af1f2636-336d-3c15-973b-78ddfdec008f | -13.16865 | -51.69842 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc2ab837-47f7-31da-b188-befa5e64d380 | -13.16856 | -51.69563 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a6bb28e-230e-3d3e-9596-e740541eb090 | -13.16733 | -51.68214 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4de7b21-a502-3da4-a5b2-ba8a651542c4 | -13.16645 | -51.6832 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4594aaae-300e-389b-aaaa-400847847139 | -13.13388 | -51.67313 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e83c70e2-0326-3933-a169-17ad24acd565 | -13.12971 | -51.67239 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75aad70a-96dc-372d-822f-89be493786cd | -13.12624 | -51.66777 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35c3af58-0202-310e-839b-403fd1a7562f | -13.12412 | -51.65562 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a976671a-d565-3b09-a36f-e1831a7d5e3c | -13.12345 | -51.65938 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32b07559-9b8e-3672-b936-2146abafc95f | -13.12278 | -51.66316 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d010ea64-2d2a-3380-924b-75ea4e98ddd6 | -12.51616 | -51.70988 | 2024-10-10 04:19:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4d130a5-d7fc-3eac-a13d-d4459aadde05 | -12.40863 | -51.03865 | 2024-10-10 04:19:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd85123d-5e2a-3321-b984-9a1d4eb36c32 | -5.76106 | -51.44136 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85ef5ba2-83cd-3e3a-aab4-18b28167688d | -5.75478 | -51.45006 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4114b63-0645-37de-bdc1-a063657756ca | -6.45685 | -51.71436 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fe5a904-6d05-3411-9642-024659c36670 | -6.4538 | -51.71516 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10a7dc6b-fc2a-3075-bc80-ac034f0d8c24 | -6.40383 | -51.7153 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b0c563d-9a57-306b-9352-24de9dcaa656 | -6.39354 | -52.72575 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0e9b51c3-a13e-3aed-97bc-fd5dc67c99eb | -6.13613 | -52.70161 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 960884f0-75a1-3103-8022-6115a1186241 | -6.11758 | -51.69459 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc2274f0-59f5-3f1e-9723-390dda50c345 | -6.11676 | -51.69944 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c984261-9562-3a46-bc4f-7d1124ee203f | -6.05499 | -51.52814 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9274bb7-8123-3784-858c-5d4d4672bd0d | -5.94231 | -51.59856 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f400b87-834a-3613-a269-5fe5aa68e64f | -5.93957 | -51.59988 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9d6d6d2-035b-319a-b3f4-dcb949a883b9 | -5.76024 | -51.4461 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0b63ef8-49fd-3454-90ef-3fedf106c0a6 | -5.75942 | -51.45084 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcd831ea-c1e5-350f-80aa-553b3225ef2c | -5.7586 | -51.45558 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 42bc689b-9a81-358d-adc3-2cdd6e09cba1 | -5.75561 | -51.4453 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a81ad419-5102-32be-abb5-8149c3a76937 | -5.75396 | -51.45482 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da374ecd-895d-35d2-a38b-f3e91cc0f4ef | -6.45466 | -51.71024 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7560051e-e4a8-3343-a595-2bbdeb77afe2 | -6.44818 | -51.65203 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d35370b1-e88d-395e-bfdc-2709300994a8 | -6.44349 | -51.65147 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17d9fb87-c3a4-386c-883a-aa5875045115 | -6.40851 | -51.71605 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5cff449-56e3-3e35-b5dd-368f5acaebf6 | -6.40468 | -51.71033 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71396acc-1d6b-3985-b993-9ab02cf86cb9 | -6.39396 | -52.72095 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 58eb2eb0-0ba6-32c9-9d71-8b698a4acd32 | -6.39295 | -52.72663 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6542c4ba-04ce-3682-9a2f-eddde271e915 | -6.38854 | -52.72484 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ebc2659-874a-309a-abfc-64b7c2afd31f | -6.38795 | -52.72573 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b86bc842-ffc6-30b6-a4cc-b43f13e3209b | -6.20406 | -51.51174 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12859738-d53e-3710-b136-724693647bf6 | -6.20489 | -51.50695 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1456283-a21f-316f-adf4-ea8e9ce8c4ed | -9.33733 | -52.54927 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2a375b3-f355-35c0-b279-9cfaac67534a | -8.86526 | -52.99035 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 008a9083-050b-3588-8535-38d36e8fd81a | -8.86038 | -52.98942 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41cd7cd8-964b-3f7b-aaf6-9839c39b2a82 | -8.8595 | -52.9943 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cb6f84a-386e-3207-b71e-60709d665907 | -8.85849 | -52.9999 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 920e7ede-fda1-3a56-9272-688ff2feca79 | -8.54641 | -51.80462 | 2024-10-10 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a223b98e-bd88-3625-a429-c84c4b4fa0c0 | -9.71696 | -52.83741 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8d54141-df0c-3f49-89e9-90ead80b1092 | -10.90137 | -52.45286 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15060d41-3373-3e95-9974-8bcf6d6b49e0 | -10.70215 | -53.03531 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60cfd7a8-1f08-30a2-baf8-a909fe47b207 | -10.70026 | -53.04568 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8efcc815-3f4b-3de5-95df-88f9aaf1e035 | -10.69743 | -53.03429 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e99b864-1c1b-3724-b801-3710a42fb2d6 | -10.69553 | -53.04469 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d40fc1d-222c-3fb1-9db0-efdd2c060aca | -10.6927 | -53.03334 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README80.md)
