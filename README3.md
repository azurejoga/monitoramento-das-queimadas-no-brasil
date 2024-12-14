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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 385d63a6-e7d8-3e59-babc-3af8464e08da | -4.4081 | -45.8433 | 2024-12-14 02:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4d2316be-f453-365d-b441-32e5116cdad4 | -4.4082 | -45.8209 | 2024-12-14 02:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 91.3 |
| adbf25a6-7c15-372a-922f-02041a3b8cd6 | -6.0472 | -44.0331 | 2024-12-14 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 30c74b91-9ed5-3bd5-bc6a-381508b3d717 | -12.5499 | -57.6996 | 2024-12-14 02:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 0c3d8007-93aa-3358-86fb-d3c3332de051 | -9.64875 | -66.56394 | 2024-12-14 02:36:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 86520873-d2ab-356b-bd33-e4c4c537fe37 | -9.65778 | -66.56929 | 2024-12-14 02:36:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 05f81a17-6efa-334b-8c09-deb8fe76ccd5 | -12.5497 | -57.7196 | 2024-12-14 02:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ebc54e68-173d-3d30-b499-372e7954157f | -4.4082 | -45.8209 | 2024-12-14 02:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 194fc2d5-75f9-3013-bcee-79d4a8f90cf7 | -14.8449 | -53.6661 | 2024-12-14 02:40:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| ca8a8e74-ec17-315d-823b-27050ef805fe | -12.5499 | -57.6996 | 2024-12-14 02:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 092ea75e-ea59-3110-9671-e18d096d9049 | -12.5687 | -57.718 | 2024-12-14 02:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |
| b4b8870d-0879-34f4-8a0f-49598c7a1347 | -11.8295 | -57.8175 | 2024-12-14 02:40:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 70350382-0c96-3364-aee2-825cc0a7bce2 | -3.2504 | -46.8489 | 2024-12-14 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| afa8ce83-a196-36a0-8c62-d3425d57cacf | -9.03983 | -35.35746 | 2024-12-14 02:45:00 | NOAA-20 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| e6c913d1-bdec-396a-a7f5-9650cf2dc428 | -9.03597 | -35.35795 | 2024-12-14 02:45:00 | NOAA-20 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 05b1d70b-a5ff-3ccf-967f-fbdda3ed7533 | -12.5682 | -57.7579 | 2024-12-14 02:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d15caae9-ecf6-3a4f-bdfe-cd80505005cc | -14.8446 | -53.6871 | 2024-12-14 02:50:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 299b8d0d-4dad-3f51-bc72-8d73ed3d6411 | -3.2504 | -46.8489 | 2024-12-14 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 083184d2-df1a-3fc0-93ae-92d7d67fffcb | -12.5499 | -57.6996 | 2024-12-14 02:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f98b29fd-4506-3efb-8957-7af940184621 | -14.8449 | -53.6661 | 2024-12-14 02:50:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 29db2663-017a-361a-8627-68359708b170 | -12.5497 | -57.7196 | 2024-12-14 02:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 29deb206-d365-3f7d-ab4a-4e4398fe0908 | -4.1057 | -46.6142 | 2024-12-14 02:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8a7e67d6-b121-3d7a-9e30-63f331e88afe | -12.5497 | -57.7196 | 2024-12-14 03:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 296d9d1b-4116-31ba-a79e-905f6e8bf7fe | -3.2504 | -46.8489 | 2024-12-14 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 354bf691-d835-3747-8432-a2c9ceab3096 | -12.5682 | -57.7579 | 2024-12-14 03:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 228bfaa8-2ef5-35c1-aede-04e32432bc1a | -12.5499 | -57.6996 | 2024-12-14 03:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d97b00cf-e471-38f9-8117-754f4527ad68 | -14.8449 | -53.6661 | 2024-12-14 03:00:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9a580b51-792a-3f1a-a81b-3f63589dda40 | -14.8446 | -53.6871 | 2024-12-14 03:00:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f3fcf353-2dee-3c0d-89ea-3b474fabf9ab | -4.1057 | -46.6142 | 2024-12-14 03:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 24697163-f797-34c9-9d42-7793f4a64707 | -14.8449 | -53.6661 | 2024-12-14 03:10:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 157.9 |
| f60bc6f5-9e7b-3f10-88ff-50bcca7ff05c | -14.8643 | -53.6637 | 2024-12-14 03:10:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ceab33f6-c0d1-3654-afd3-aa1e7368050c | -11.8295 | -57.8175 | 2024-12-14 03:10:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 20cde1bf-067c-3899-9491-e80e5f372028 | -3.2504 | -46.8489 | 2024-12-14 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 750981f3-3868-3d32-975e-26fb6b1438b3 | -7.9334 | -35.2518 | 2024-12-14 03:10:00 | GOES-16 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 62.4 |
| 875650cc-5295-38e3-8109-50f3adfc9b2f | -14.8446 | -53.6871 | 2024-12-14 03:10:00 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ee778a35-4287-36dc-be0c-f3d0a2ae3d4e | -12.5497 | -57.7196 | 2024-12-14 03:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2506d3cc-f75b-37e0-b262-a9d8496e433a | -4.1057 | -46.6142 | 2024-12-14 03:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2d05ea3a-23a4-3005-b489-9a61d26d38c9 | -12.5687 | -57.718 | 2024-12-14 03:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7e735ff3-0c39-3255-a63d-481eaaa3cd09 | -3.2504 | -46.8489 | 2024-12-14 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5f43d613-e5af-3716-bf76-842ebf30a143 | -11.8295 | -57.8175 | 2024-12-14 03:20:00 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 559632b0-bb4a-3db8-9b7b-fde5e3ad84e5 | -12.5497 | -57.7196 | 2024-12-14 03:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e86747fe-64a6-3fb1-8ed7-596996d7eaf9 | -12.5499 | -57.6996 | 2024-12-14 03:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2f7a58db-5f55-3230-a76a-8fb44c0f09d4 | -4.1057 | -46.6142 | 2024-12-14 03:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| adcba9be-89a9-3ee3-a0ae-935fee877ed9 | -4.0871 | -46.6151 | 2024-12-14 03:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 5738e656-b0da-361d-a5ae-1bc3d5a54882 | -4.1057 | -46.6142 | 2024-12-14 03:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b521961a-6a26-3365-81ea-07f47a8f37cb | -12.5682 | -57.7579 | 2024-12-14 03:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 02ff2e4f-6ce0-3465-adfe-ebf54be0a852 | -12.5499 | -57.6996 | 2024-12-14 03:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f6ab56db-866b-3058-928a-9db8a3361fe3 | -12.5497 | -57.7196 | 2024-12-14 03:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5d1dca01-5346-32f5-9083-541afe5d4d30 | -4.72372 | -43.19807 | 2024-12-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb436f75-a65e-34e7-bca7-adb8fb50b78d | -4.77258 | -37.8131 | 2024-12-14 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4eb83d14-db03-38ea-a9c1-17cf9eaa967a | -3.25231 | -46.85954 | 2024-12-14 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f97255a4-bbb5-3b52-bb24-bfe61709741f | -3.24918 | -46.85894 | 2024-12-14 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8de8bca6-d8dd-3e75-8f6a-ff835c43f8f7 | -4.76995 | -37.81509 | 2024-12-14 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ef1ed565-3839-3ccf-a98d-6ab653d6fcbe | -4.52633 | -42.0682 | 2024-12-14 03:36:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ec7466dd-e97c-38cd-b644-85d3b36d37c9 | -3.25348 | -46.85266 | 2024-12-14 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 44018cd9-165c-34af-920c-8b3c91dcb82e | -3.69013 | -42.60689 | 2024-12-14 03:36:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76c3a74b-d4dc-3d56-af3e-1a901a2efb5c | -4.16792 | -42.42966 | 2024-12-14 03:36:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3d0b3f9b-ed50-385e-8377-b38618f08117 | -4.9626 | -38.73901 | 2024-12-14 03:36:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42802ccf-52f4-320e-a664-16bbd8de28f6 | -4.72434 | -43.19436 | 2024-12-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2168188-281c-34ba-98f5-fe281cb999af | -4.17268 | -42.43383 | 2024-12-14 03:36:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 94260f98-a39e-311c-b6ec-95feb754a964 | -5.01136 | -39.71484 | 2024-12-14 03:36:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 35b9148c-7e76-3bc8-b19d-a695bae595fd | -5.64688 | -37.25927 | 2024-12-14 03:36:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 924002a5-803a-3a8d-89fa-ec6158d1dd78 | -3.29634 | -42.51818 | 2024-12-14 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df4ddaf4-d308-30c3-a44b-1f25e0f5f2c5 | -3.30671 | -40.55532 | 2024-12-14 03:36:00 | NOAA-21 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 07970d18-de3a-328b-a75c-653c96a16b57 | -4.77568 | -37.81855 | 2024-12-14 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8fc99a57-b8fa-331f-95d1-61316676c26a | -4.71818 | -43.19711 | 2024-12-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eda7423f-cbb5-301d-bb1f-d132b12fdde0 | -5.43217 | -37.85332 | 2024-12-14 03:36:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5dd877c6-f6de-3a73-85b2-a6e1c902015d | -4.77181 | -37.81793 | 2024-12-14 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 26201c7f-842d-35dc-8500-81c17ec3f76e | -3.46013 | -40.81784 | 2024-12-14 03:36:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f02b732-62ae-3285-82b2-5764806dc7d1 | -4.24268 | -41.92429 | 2024-12-14 03:36:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 04be9c28-0cbc-3c32-8284-b9b554733bc5 | -4.16623 | -42.43965 | 2024-12-14 03:36:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 793756f4-35d5-3278-9ba5-b5edd1567843 | -4.4014 | -41.43655 | 2024-12-14 03:36:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| afe2524e-822e-38d8-bb52-a4f8b723546a | -3.29092 | -42.51731 | 2024-12-14 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f6d2a99-1ff4-3e86-be71-d6e1fd739956 | -2.53604 | -45.37861 | 2024-12-14 03:36:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ba352e5-e2aa-36f7-b1b7-e58ed7d9ebdd | -2.92062 | -41.46765 | 2024-12-14 03:36:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3aed4c61-f2fe-358f-b444-6b3b321690ef | -2.54262 | -45.37969 | 2024-12-14 03:36:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3aa2d9b1-74b8-3da0-9ea9-5c59e88c03bb | -4.40291 | -41.43438 | 2024-12-14 03:36:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0e431a77-eb01-3115-9177-c3140883851d | -3.25039 | -46.85209 | 2024-12-14 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 99958b97-df3f-317c-b1af-f057f7624814 | -3.90401 | -44.16072 | 2024-12-14 03:36:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59a64951-25bb-3224-98c7-0c571f84df38 | -4.7188 | -43.19341 | 2024-12-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9809eaca-0c57-354a-ab44-5a8720cc4a57 | -5.24146 | -37.69115 | 2024-12-14 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a1369b0-370b-3aae-8801-45f4d0e7b47f | -4.178 | -42.4347 | 2024-12-14 03:36:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6124e291-610a-3c8c-83bc-6b4ab53e8f05 | -3.69071 | -42.60349 | 2024-12-14 03:36:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a2e26fa-b33c-33e4-bbfe-232c4989fd8a | -4.16736 | -42.43299 | 2024-12-14 03:36:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 56f29172-6bfa-3cd6-adcb-49c4fc4fba80 | -4.5258 | -42.07129 | 2024-12-14 03:36:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8db4ba35-480d-33db-865c-d8f0937244c9 | -4.77644 | -37.81372 | 2024-12-14 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f99921ff-f000-38fa-a75d-07dae042025c | -4.77381 | -37.8157 | 2024-12-14 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 56d38933-1def-3f9b-8274-8ff8f1ee5ec1 | -2.92572 | -41.46841 | 2024-12-14 03:36:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f7e16e48-5897-38d9-99bf-c420c10d48c2 | -4.71756 | -43.20078 | 2024-12-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eaaffb09-d71b-3574-8dde-dc01b2a2aa65 | -4.16679 | -42.43632 | 2024-12-14 03:36:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| be4b0c92-0e95-3fd4-be0a-969a51659b72 | -4.24781 | -41.92513 | 2024-12-14 03:36:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48a5791d-58b1-3a42-9491-ccff2955f16c | -4.10245 | -46.61604 | 2024-12-14 03:36:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ae50fdb-8d73-30bd-8928-cda9daee9677 | -2.96545 | -39.96348 | 2024-12-14 03:36:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3774b66d-4c08-3711-bf02-6901816f5d77 | -2.54119 | -45.38038 | 2024-12-14 03:36:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c3113af8-2bad-3c69-8242-ab0e9df64c4e | -4.52527 | -42.0744 | 2024-12-14 03:36:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ecdb615-d09e-320d-9c0b-9e3ecebef363 | -2.96087 | -39.96274 | 2024-12-14 03:36:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ba50d884-feba-3cbb-8dc9-1603573bdaa3 | -3.72956 | -39.95438 | 2024-12-14 03:36:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6ddb8c8f-62f5-38d6-94fa-e6dfc81521d7 | -4.17212 | -42.43715 | 2024-12-14 03:36:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6d23cbd1-db9e-3911-a2b7-9940b2be52a9 | -3.45533 | -40.81693 | 2024-12-14 03:36:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ba2470f1-211e-31ef-9219-8665a6ddcb59 | -4.9632 | -38.73537 | 2024-12-14 03:36:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README4.md)
