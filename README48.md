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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92aeab10-a0d5-3922-b81c-4f0309fc9bec | -17.01842 | -57.52106 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4fe349fc-d219-3ae1-baf1-991a17ce142c | -17.01773 | -57.52505 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 79bc33e3-1954-3b59-a8d7-bd093ab90766 | -17.01753 | -57.46337 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8b64cf81-5c55-3d4a-bd66-49929ce46ec8 | -17.01699 | -57.50845 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ddce1104-cc3d-34ba-8d42-57d002623bad | -17.01631 | -57.51244 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e4eb199b-9cbb-3fc7-b81a-c775c18a5e21 | -17.01562 | -57.51643 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| af8a0001-5093-3b5e-aeef-f78c183cf757 | -17.01525 | -57.33673 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 953bc60e-7a48-3e36-ab9c-69babe639003 | -17.01494 | -57.52043 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2c51acd1-af13-3abf-bb90-69f63887c576 | -17.0146 | -57.34068 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bf4d5c5a-ae68-3e5e-a40b-dfda4cb15828 | -17.01426 | -57.52443 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 715680ab-33b1-3c73-a857-47b8789a6e0f | -17.01283 | -57.51181 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 12c89410-6387-3f48-abe0-1d02e808cd9d | -17.01215 | -57.51581 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 274fc939-c24e-3ed2-a32e-91b42c5fa84b | -17.01197 | -57.35645 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b48665a3-3bf3-352b-a200-128fd2034a29 | -17.01147 | -57.5198 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ed6b3dec-fc66-385a-92ec-9f18b227dfeb | -17.01131 | -57.3604 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2a9315e9-2792-3843-8722-19d97116d5e9 | -17.01065 | -57.36436 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9d565ef1-d7f2-3172-87b0-fed90d8ff609 | -17.00999 | -57.3683 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e252a968-76ac-3bf1-b40f-d0e87b8e3e3c | -17.00983 | -57.34794 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d1e212fd-d537-3d41-a2b1-61ea35c0365b | -17.00936 | -57.51118 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9d14467a-7d96-39ce-aad8-d48343bfb1ba | -17.00851 | -57.35584 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4b43e11d-884c-3358-8fec-c163cd0b3d1a | -17.00836 | -57.33548 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 682e7302-8d39-3b63-8db3-b00c5dc09634 | -17.00786 | -57.35979 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a78067a6-f7d3-3612-8640-c892af378925 | -17.0077 | -57.33943 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 74dc581d-9334-34da-bfe8-92d773647da9 | -17.0072 | -57.36373 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 05f27601-8236-3c0f-acb0-e0b6f16ab2ce | -17.00704 | -57.34337 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f2b1440d-32c5-3fb4-b6d3-dc1f87d292e4 | -17.0044 | -57.35916 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 329f0ac2-3402-3e2c-a830-1b19d5fbc40a | -17.00425 | -57.3388 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1a15a82f-05b4-3a65-a20a-e294939b8898 | -17.00359 | -57.34275 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cadd4064-9eb7-3dc4-be13-884b303ccfc9 | -16.97377 | -56.824 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ec84925a-710f-3b02-a377-3b14bdb2b0d4 | -16.97038 | -56.82339 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2bcc6387-3605-3d1f-8a68-4de71b06c174 | -16.96121 | -56.7944 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 94e58c90-8c4f-3bc9-b0ec-742c8f6dd92f | -16.9602 | -56.82158 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 5444d1e3-7079-33e0-b856-9f6ce7f5577f | -16.95782 | -56.7938 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0ab15a36-d876-3176-8ecf-73e2d4c86002 | -16.95425 | -57.53032 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fae7ec14-bdfa-3795-904e-0d66364f8a66 | -16.95357 | -57.53432 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c96581c1-8b81-31dc-a1cc-03bc7fb9c446 | -16.95145 | -57.52568 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8f7ba508-0a45-3755-80fb-91b2a7a3da4d | -16.95077 | -57.52968 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cf7dca4f-d32c-36b5-aa1e-da64a432176f | -16.9501 | -57.53369 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c61c1e03-aa31-3dc1-b919-3a02a57f5138 | -16.94942 | -57.53769 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 30a7f3c6-1689-3947-8118-c41d3584df28 | -16.94662 | -57.53305 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6fb87827-f6f5-37c9-86b0-b59a8968719c | -16.94594 | -57.53706 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 8d7ce851-897e-3622-95d1-b3bf5328da97 | -16.94585 | -57.51641 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b5adc524-9d5e-398a-a5ec-e6ec984778c3 | -16.94518 | -57.52041 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7c6f8e5c-3e44-3226-8c5e-1d75afeb0838 | -16.9417 | -57.51978 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 67ca21b7-6fd3-3423-991a-e087a82f6203 | -16.93619 | -57.53116 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 99f3f47a-d497-3ee2-a519-ac528518b8ab | -17.81985 | -57.59255 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 80d6ce7e-5b6e-3735-95e9-79532f1b7f7f | -17.78437 | -57.52887 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c03f0451-63ad-30f2-9c93-6252b832404b | -17.78041 | -57.57305 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ab91a4b8-1834-3943-983f-a8eeaf19fa55 | -17.78033 | -57.55259 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 36677335-9ef1-3762-9114-449665196bae | -17.77966 | -57.55656 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a34ae183-2ea5-3eab-a918-3f715156d924 | -17.77764 | -57.56845 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1a234369-3447-358b-8212-981a5b9fb59d | -17.77688 | -57.55197 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 57f042e8-056c-31ac-b69f-f0cbda3d6eb6 | -17.77545 | -57.53947 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 97a813bb-f9ab-3086-a482-3837e2dd3bf2 | -17.77267 | -57.53487 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| ca89288d-ac19-3698-b316-47e88dc485e8 | -17.772 | -57.53884 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 4bce2766-531c-338a-9ea1-17d2e693d5ef | -17.76998 | -57.55071 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 774f1e30-df2d-33da-912f-c7873f16eb1b | -17.76788 | -57.54216 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| f65923f0-9137-38d2-8cc1-0e55b738caab | -17.7672 | -57.54611 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 16e8ef3c-26ef-3cf0-a7a3-d8cbe2f00ab1 | -17.76652 | -57.55008 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2d7f98fd-567a-353f-8816-9bf51a54e003 | -17.76375 | -57.54548 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0c09b04c-d7b1-37c8-ad3e-27e9f13f3618 | -17.76314 | -57.5699 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| aff0fb98-a734-3c1c-8263-c4a484c9c2ee | -17.76246 | -57.57386 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0a565642-3f1b-3113-80e0-aae14dff5b4c | -17.76105 | -57.56133 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 70572b49-25b4-30ff-8186-321da935b572 | -17.76037 | -57.5653 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| f823985a-1caf-3175-9a68-227adca0a685 | -17.75969 | -57.56927 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 60c58698-744e-3900-b1d2-ce2182232042 | -17.75901 | -57.57323 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5217a635-0140-3b7d-b74f-bf031be98e55 | -17.75833 | -57.57721 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| ba4d37e4-478d-3121-8efd-9883dd1616df | -17.75827 | -57.55674 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a93832ec-686c-38d8-b679-ba8127f993d1 | -17.75759 | -57.56071 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 011bc108-4ece-3a88-8532-3f07137cfd45 | -17.75624 | -57.56863 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ea2bbef7-55de-3b35-8981-382e1d982feb | -17.75555 | -57.5726 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 045910b9-3fb1-3855-a7ee-c5261d1acce6 | -17.75488 | -57.57657 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| e25ade89-d0f5-3d03-8bcc-a9f60096b8d7 | -17.75482 | -57.55611 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4547d2f5-8f22-39dc-b0a2-3f0bbc3ddef2 | -17.7542 | -57.58054 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 8d5c1906-1539-36ba-835f-13951436b8bf | -17.75414 | -57.56008 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| b6a5abf7-635b-3270-876f-022e31e18495 | -17.75346 | -57.56404 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a68ea958-0f87-3f54-9deb-97fdff4dd201 | -17.75142 | -57.57594 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.9 |
| 7758b5a7-41ed-3c3b-856c-c2079e55cc1a | -17.75074 | -57.57991 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.9 |
| b748567d-237b-3a8a-a1b3-e7b92e63149d | -17.74922 | -57.57627 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| d8dd730c-b20a-35b4-9d29-51059761db74 | -17.74856 | -57.58025 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 566cd5bc-6384-323a-8a82-67bedf8ba808 | -17.27129 | -57.29627 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b82d5340-a779-3645-852b-479518eac5e4 | -17.26852 | -57.29174 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 066e8091-ae6e-3431-9a43-4db19d7bc283 | -17.26785 | -57.29565 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bb1790e0-0b37-3303-989c-b440e06e8887 | -17.26719 | -57.29956 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 737c79a9-27a2-314c-8664-33fd842ec1b3 | -17.25821 | -57.28988 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a4e5fc4d-91fa-3f5f-948d-dcc4e893e7fe | -17.25755 | -57.29379 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3462a727-93f1-38cb-82fa-5008e78cd45f | -17.25688 | -57.2977 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bd67e3be-bbb2-3e89-a66c-0d673f8a98ea | -17.25544 | -57.28535 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9060c5c0-08fa-3515-a5d0-6c64afaa99d7 | -17.23998 | -57.27536 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7722124d-0ac8-39a2-9367-98b3d9e6f74b | -17.23033 | -57.26959 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 28d7b451-7fa8-3dbd-844f-1aeadcdcf40e | -17.22968 | -57.2735 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bb7f459a-b100-3ce6-a056-3e1c9a826f95 | -17.22755 | -57.26506 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c937a826-18c5-393d-a6a7-ca219c88fa53 | -17.22641 | -57.29307 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 34d90942-9abc-31ad-a2da-89daad519720 | -17.22232 | -57.29636 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ae1bc061-4021-3f57-b913-47e35a474104 | -17.22166 | -57.30028 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 685b3033-bb07-34a3-9f82-e65ad2863e76 | -17.21659 | -57.26711 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0bf2f6fb-7433-340c-84e9-cd232ee7e4e0 | -17.21363 | -57.50948 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9027d6bc-5b09-37f5-90bb-f7649edd9cec | -17.2125 | -57.27039 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 56fc69c7-b407-3c37-8249-44f4d95afbe7 | -17.21185 | -57.27431 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 25fa1162-1b5a-3c49-8549-292d0d4a89b4 | -17.21149 | -57.51011 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README49.md)
