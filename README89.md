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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21647598-6a16-3428-ad99-c59376f39500 | -21.29581 | -44.48157 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e63a9fa-ee2a-3ecd-a80b-1e5efa8335b4 | -16.99664 | -56.77189 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| a21d0ae0-8eee-30d1-944a-12744436f0d1 | -16.99538 | -56.77747 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| da0d8b88-2d3b-3fbb-910c-6c2a951d8684 | -16.99524 | -56.74819 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 12fe06a2-99f7-3bbe-bdeb-65c762efd141 | -16.99412 | -56.78305 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 085a4ba6-ea2d-35ff-bdf4-a8936e919d19 | -16.99399 | -56.75373 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a6d19509-fc0b-378b-b78d-bf7662e4489d | -16.99149 | -56.76482 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 359e4def-1e54-3892-80be-5a53374ca2cf | -16.99024 | -56.77036 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 1e77cf95-6ade-33b1-bf59-7a77b1cd0de6 | -16.98761 | -56.75221 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2d74b3d6-6717-387b-94a6-6d5e8f64435a | -16.8513 | -57.47386 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 34aa50a2-d3df-3086-938b-09e2e82e9d8d | -16.84604 | -57.4661 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| fdf68d2c-9b91-3afd-91c3-a85f64aad6fd | -16.84464 | -57.47224 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 69ac80d0-ebbc-3758-9b53-70bdc524c34e | -16.83797 | -57.47066 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 421053dc-308b-3a33-b472-08f6c8ab6a45 | -16.83655 | -57.47685 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ba99619a-26b9-3ea2-b75e-916ec1fd8f1e | -16.80179 | -57.38397 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 60159221-e6d5-3493-bed1-d9f92caf7566 | -16.79829 | -57.38515 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 736104d5-ce18-31a4-98aa-f26f8c93628c | -16.79515 | -57.38239 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c673b279-584a-3cf3-bde9-9cdfeb8a0571 | -16.79194 | -57.82991 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 591c15f3-44a9-3b4d-a968-b64c1a485443 | -16.79165 | -57.38355 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fa0d1b1c-f9d6-3210-a7f6-146fb2b11fe9 | -16.79026 | -57.38969 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| df2a7cc7-e90c-3e8c-81c6-e83ca643a9d7 | -16.78708 | -57.38691 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d361ad9d-ceb6-3a4a-9e2f-146911670779 | -16.78501 | -57.38194 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| eee5a4bb-0756-356d-a549-ea17aa04907b | -16.78363 | -57.38808 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 392fd2a2-5e0a-3a1a-9468-40c354b2c455 | -16.78186 | -57.37926 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 56ae0a10-ca98-3502-8ed6-73c33a87db29 | -16.7373 | -57.46832 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a0d8c638-f18b-3133-92dc-691fd2733159 | -16.6988 | -57.47134 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 895158e7-a8d0-3b39-b08d-082c56b6cd2c | -16.69579 | -57.46496 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bf7055b8-aac1-3a48-941a-5001a2e8bccc | -16.69352 | -57.46347 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e82f3a68-e64a-39b2-b9d7-f8b360d805b0 | -16.69211 | -57.46972 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7dcad47b-e8e1-38d3-ad71-92c1fb26c056 | -16.68912 | -57.46334 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a7a79a6b-822e-3e97-aa9b-87ebe9b5ff57 | -16.68767 | -57.46959 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cc4bac44-c1cc-3c85-aa82-a99174f8c038 | -16.68684 | -57.46183 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ce78a539-39c7-3e2a-9c8c-c59875426980 | -16.68543 | -57.46811 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f44a565c-6432-3e2c-b399-27cb11449cd0 | -16.68388 | -57.45551 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7e692ae8-f8ad-340b-b49e-75c0f0cbb125 | -16.68243 | -57.46174 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b5f80d43-a8c8-3cbd-b6cb-a355d0be3b8c | -16.68157 | -57.45397 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7506583a-fc6b-32a6-89f9-a8e9fa8eff20 | -16.68099 | -57.46799 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 506715d8-d4e7-37e6-9f10-cc56a560618b | -16.68017 | -57.4602 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 915653a2-e906-3a22-95dd-95f900e8e90b | -16.67876 | -57.46646 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c9c5df09-dfb2-3965-b9c0-378d0a2d971e | -16.67575 | -57.46014 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 4e54c086-f269-3493-8d48-394902f4919d | -16.6743 | -57.46639 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| d9649824-e1b4-32c1-8437-299179e9f855 | -16.67349 | -57.45858 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a0347f12-20d7-3e8c-81f1-9ef71e5d2294 | -16.67208 | -57.46484 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 15f3d94d-39cc-38dc-a90f-a4127c3c98f9 | -17.18944 | -57.35588 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| f04c1759-c0ab-33c7-96d2-0c2c34486e9a | -17.18806 | -57.3619 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 42c92960-56e0-3715-9142-e7236555e384 | -17.18148 | -57.36032 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e0358f86-fb32-3011-90e9-83f02f492710 | -17.17316 | -57.39656 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d795a959-1d7c-3066-b793-c99e27c82150 | -17.17177 | -57.40259 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| bd54db35-1bec-384b-b723-698e5f8d8580 | -17.17073 | -57.37682 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0f1a7aa7-a676-3882-a237-372f8824422c | -17.16657 | -57.39493 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| cb6af4a9-3296-38d6-b915-f300845133d6 | -17.16555 | -57.36914 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 282adc73-e6aa-3b29-a351-57783f3ad749 | -17.16518 | -57.40096 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 60db72e3-2a2c-3cf0-acf0-85b09dacc871 | -17.16415 | -57.37519 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 66ce048b-c92e-3c7d-aecc-7c8989e28c23 | -17.16379 | -57.40702 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| b4549043-3222-30b9-b756-226f485fdf49 | -17.16276 | -57.38123 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c5857690-7dbf-3507-bf66-6f47ce48f97e | -17.16244 | -57.3643 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| ea3212e4-4111-3de0-a280-a6b4e8eacd8a | -17.16109 | -57.37035 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 344689ec-0bf3-34af-b1be-2d2daeac44c0 | -17.15973 | -57.3764 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| fc677c1b-1b9f-3c10-b7c5-d15eb23ca047 | -17.15895 | -57.36757 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 5e9cff25-b640-3484-ab1f-8ebbf17a8fbd | -17.15858 | -57.39938 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 297fab9d-59c2-3b5f-86cb-455d6e0e1083 | -17.15837 | -57.38245 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e1a0a432-6e48-33bb-8ae1-865fd9997b4b | -17.15718 | -57.40545 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 6c79cc97-839a-323b-aebd-080a0600ac58 | -17.15702 | -57.38851 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| faa19582-f163-380b-b382-f5fbcba75279 | -17.15617 | -57.37965 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 4f633723-f9e0-301f-93eb-060720b60c66 | -17.15566 | -57.39459 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 65ae34ee-7d71-3c63-99f2-5b6f43503fe0 | -17.1543 | -57.40067 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| cdd3f7de-2221-3dc0-9e08-ee90946d733d | -17.15337 | -57.39174 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 79a35275-b642-3840-b7f5-aea023c17267 | -17.15197 | -57.3978 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 63a3aad0-6e23-346a-85f0-9a56aabf0dc0 | -17.15057 | -57.40388 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 1609e396-52ff-33ad-b708-ef4d534c3539 | -17.14906 | -57.39297 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 58743c51-69f1-3bb1-8ec8-96a8361c5872 | -17.1477 | -57.39906 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 35f0954d-23e9-360b-8570-b58f8cfdc0f8 | -17.14633 | -57.40515 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 70a4cb3d-8ae9-3673-861b-a9f26e6545a7 | -17.14537 | -57.3962 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 402e7d09-267c-3d6a-af0d-d35677af4061 | -17.14397 | -57.40229 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 1d1a306f-46bb-3371-be73-e99415d36c23 | -17.14256 | -57.40836 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 9993c44a-82f0-378f-b8ed-c3c88e407314 | -17.14246 | -57.39136 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d2835a39-4b60-37fe-bbd9-a8c8d43486ff | -17.1411 | -57.39741 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 27320ecb-4630-3941-82cc-fd07215c558f | -17.13973 | -57.40353 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 9980a9ea-a9d0-3e7b-a74d-2e172ad7fa05 | -17.13877 | -57.3946 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ef233bf7-4346-3daf-8ae0-455440064c37 | -18.71799 | -57.3476 | 2024-10-04 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 87932fb0-cab5-3008-b6d6-5d598532333b | -18.7117 | -57.31642 | 2024-10-04 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8b088920-ad69-37dd-8465-002efdebb1bf | -18.69584 | -57.29338 | 2024-10-04 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 96c1cf72-2a9d-38e4-9e6c-386e5a582686 | -21.41826 | -54.18947 | 2024-10-04 04:12:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4b80ed1-dd44-377e-917c-cfbf5bcbf78a | -21.40593 | -57.22754 | 2024-10-04 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e3a7726-9c5e-3ae3-be25-4d31675c05a2 | -17.05698 | -56.68886 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| db27cfb9-73ab-3114-a1d7-390513cfb324 | -17.05573 | -56.69431 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b11f1ff7-bdeb-30ca-80df-01f19bda1fc0 | -17.05464 | -56.69275 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2388b755-48fd-3c02-bd25-10f5033154f6 | -17.04812 | -56.69827 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0b63814c-74c7-3444-90bc-9f0bd127e2e5 | -17.04707 | -56.6967 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 79905c02-8b4f-34a1-b780-fd2b55f428a9 | -17.03949 | -56.70062 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 527d85cc-e1ac-36d2-92c4-a97376c3680b | -17.03313 | -56.69908 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f956f6f9-62bc-3321-abf5-6eed0ea00123 | -17.15247 | -56.16168 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 666e544e-d12c-348d-8950-0181167bcbd9 | -17.15135 | -56.16675 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c4697870-e052-37f6-a442-d79740322b5f | -17.15023 | -56.17183 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 02728dd8-8384-328f-a06f-ea0dd99480a4 | -17.06866 | -56.07886 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e83e0500-8808-3c97-a7f2-880c78828f93 | -17.06253 | -56.07738 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 32a77396-47f5-34ef-b427-05d4d14d52e0 | -17.05528 | -56.08095 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 745622fa-3867-393e-83c1-cb17ac6d9f07 | -16.93018 | -55.83642 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2e1a337a-2486-39d7-85d7-f4e834633fa8 | -16.9297 | -55.83861 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d0432aaf-36cf-3f66-a6b2-b19a39355120 | -16.92908 | -55.84132 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |


[Clique aqui para ver as próximas entradas](README90.md)
