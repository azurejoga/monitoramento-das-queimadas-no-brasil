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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6192cdb-7bdd-398a-aeb9-9541909088e1 | -8.64275 | -66.53661 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| da09561c-ddb8-3e76-ad7b-7cda6a39ed50 | -8.27282 | -70.45229 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd38a590-3ce5-350c-9a85-571102242020 | -6.82484 | -55.60966 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7c32a113-d0de-322f-8092-ca822e5b36f8 | -7.97793 | -71.4417 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b1a5ecbf-da6a-3e03-a05b-347776ce28e6 | -8.44359 | -70.70262 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 15.8 |
| bde808de-9ef6-3aa6-a3a0-020943fde0f8 | -6.01237 | -57.77892 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 95870d1e-676b-3eb1-b4ca-0af9ba6ca80d | -7.347 | -72.94173 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 5c492908-b6b6-37e7-bbe1-242877978f93 | -6.84703 | -59.94406 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| c49a5a79-ad28-3117-a6bb-23b06171fb4c | -7.60196 | -61.19738 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b2368724-6fd7-32a6-96f9-670b7af9b04f | -4.31746 | -59.47171 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7996fb70-79cc-324e-bff7-fcaeb67e4fe2 | -8.3391 | -71.01625 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ea7cefdf-a24d-32d7-ad32-34e71b8a1758 | -7.91801 | -71.48593 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6e67656-f8d3-3679-828d-41d39f59729a | -5.8022 | -57.63462 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 523c15c9-fa29-3de8-9b53-149545f62970 | -8.20391 | -62.94307 | 2026-08-28 17:47:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 4453ad9f-6fe7-3c52-b808-bcf9af605152 | -8.60063 | -70.01672 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 64e35741-8061-3f5f-a7f1-72078ab570c3 | -8.68521 | -70.75475 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d622bfec-1bbe-32af-b5c6-00aa25fcd9be | -6.01304 | -57.78294 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e4002537-17de-3a60-8126-9fd325b403f4 | -6.87083 | -59.03202 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 20775503-9a4b-3133-887f-310040b56fcb | -6.72417 | -59.43967 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e1ae4ad6-3290-31c9-8b4a-cdc98fb59154 | -8.50238 | -71.2077 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b2f40c4-5dca-36ab-88d6-ea68ad391d8d | -4.91212 | -56.268 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| eff91dcf-1993-38e3-a800-457a59866192 | -7.09635 | -55.47763 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a5205474-b8d9-30b8-bfb7-08b36fdc5276 | -7.48683 | -61.40231 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 915e184c-f3ca-350e-b945-50ba6c62567f | -9.16715 | -65.79948 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2ddd5dfc-6cf2-33e0-856c-86a63fa388ad | -4.31825 | -59.47655 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cbd67f53-9877-3b73-989d-5e4d6b02aae1 | -9.4517 | -72.12091 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4d034be6-e7e7-3794-95cc-46207dd01702 | -6.80855 | -59.583 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0bd13d6c-3546-31dd-a382-8ad645cf0ad0 | -7.74381 | -70.72543 | 2026-08-28 17:47:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ec931437-0e14-3c21-a1ef-e19371990a5d | -4.76389 | -62.16385 | 2026-08-28 17:47:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 95c07475-7e7c-3f69-9ab1-ae4f3d87f77b | -7.22317 | -60.62527 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c14e9b9f-88b1-36ff-88d1-fe694bf485b0 | -6.86777 | -59.03739 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6c939e7a-ad6e-3e13-8b8a-580c7870558d | -4.19977 | -55.23767 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| eda9c5be-787f-3d11-ac1c-e4045dc8b3fa | -7.76272 | -61.08356 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57817c29-591f-3da4-84e3-e4609198679a | -6.32614 | -54.74628 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 88e7725d-7d31-3ae4-b039-212239d18097 | -8.65591 | -70.94453 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9905db48-e800-3ea8-9ac7-048b83df0959 | -6.43833 | -68.2431 | 2026-08-28 17:47:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a8ae482d-ee32-364f-9fc8-fda6002d876b | -6.27133 | -53.13849 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf2ad29d-c620-32c6-a0e6-167a7801f0da | -3.29491 | -61.56841 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 560a0f82-744a-306d-b10d-2433c4e8518c | -8.79847 | -70.83347 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 69.7 |
| eca400d6-61a9-3806-a76a-bc1ea5e12207 | -8.64033 | -66.53555 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d0031a65-0e88-3b46-baef-81456fc0a0ac | -6.21341 | -55.41662 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6452cfdb-e1cc-3ce6-86e9-31766cf6027c | -9.28796 | -72.68609 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 88289869-e9db-35d5-9594-934114e1aed3 | -8.67226 | -62.8535 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c1b0c02-6d1c-3adf-a553-dddfa71402cc | -8.95093 | -70.70732 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 46.4 |
| cd9a6873-5d4f-346a-b989-056746caafe8 | -9.23316 | -65.73585 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 926b1ac2-ef95-31f9-8666-3bdedc947606 | -6.33182 | -57.74331 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d5ef5e31-2775-33bf-8c1e-30c0b83a6fb4 | -6.2645 | -55.41062 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3c89c68d-4c97-3010-92a7-1cd5b6930f13 | -3.28655 | -61.32697 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 67197c9a-0406-3576-aa32-4648598742d2 | -7.74272 | -61.09056 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2f4666c8-c8ad-3f17-8f72-83f6f65293f0 | -6.07232 | -57.95932 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| b51c42ba-e454-370b-975d-6679dfdbf0f3 | -6.94371 | -58.95858 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bf558e40-ce53-3c8b-8ebb-18d595694d90 | -7.92901 | -72.2831 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f90bbad-4ed2-39f8-ac9d-6a5418513951 | -8.25639 | -73.31941 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bdabd33a-59e9-323f-a454-310b12de0bdb | -6.07891 | -59.9629 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 790d3e28-d019-38e1-ba70-1b4bc9917eff | -8.53195 | -70.85552 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 22.6 |
| a6b18421-00ac-34a8-bad4-eefaae82bd62 | -8.63905 | -66.53716 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0b73c5a8-6ef6-35a6-905d-675091bff341 | -5.15289 | -56.26938 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| de5ea7ed-249e-3a67-87f6-6e9b790933f4 | -4.30662 | -59.47835 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ee04f040-3414-3e8e-baee-d20e8395d8fe | -8.35176 | -70.85064 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 37.3 |
| d934ae83-99d6-3df8-875c-43e012944e6e | -7.57981 | -61.39081 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 81c451d6-a9af-33da-936f-da47f5448746 | -7.61259 | -61.33278 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc9e6820-8ad6-308e-ab4b-f50a175529dc | -9.09156 | -70.12032 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 9d3f8e5c-9aac-3401-acdc-a1481b9daa54 | -6.76154 | -55.69798 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6a7915f1-938a-3374-9d84-ff416c69c91f | -6.12087 | -53.74433 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 074acf83-73bf-34b2-a4cf-4467bcda3291 | -7.92364 | -72.28378 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 2ce7678b-6fcb-392e-ad7b-cb664092015a | -8.91386 | -70.6902 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1f7eb8ba-8f69-310b-91ba-86ac183147c9 | -8.22145 | -70.50772 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b41682fb-98fb-30ef-80cd-1572652d5b8b | -6.73489 | -55.45578 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eb40459a-ef14-37db-af32-8529701997fd | -6.02383 | -58.05201 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2a14e1fa-5a84-32e0-ba3d-e31e26bd4eea | -6.20862 | -57.75897 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b5935502-0881-37f4-935d-5ec62cc4d558 | -8.26034 | -71.99255 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cead01ad-3cd6-3e90-b26f-b96f8ae243ff | -9.37578 | -72.71861 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 87ad56ed-9d93-3ab6-b42e-0108889915f6 | -6.58466 | -55.4443 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fbf1bbd4-f1b5-3434-8850-9e142f198d76 | -5.81009 | -57.62931 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 09cc08f6-94d9-32d1-94d3-b05e3738e7f2 | -8.34478 | -70.76358 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84b9487b-ba2b-385e-87cb-9acb4e20447a | -9.20506 | -65.79457 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 28ec56f1-e841-31bb-ae71-583436b24ac5 | -6.54893 | -58.59327 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c2e4aca7-af28-3b52-9225-581f0fc1d26b | -8.63968 | -66.53114 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c38e930d-9744-3304-9dd1-71a8a1fdfde1 | -6.92195 | -59.48524 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| c1a89ddb-f943-30e9-bf0b-c1005f24489e | -9.58327 | -68.58642 | 2026-08-28 17:47:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 828603e7-ab52-3f65-80d3-e1772d5bd130 | -7.36763 | -55.18806 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a088bbcb-5ed6-3a1f-ac98-a161aaf10181 | -8.334 | -70.72106 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 215a7600-46cd-31e7-8aa9-d72f24e71dac | -7.01622 | -59.64344 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 662af168-3167-332c-be9b-7171970b8b26 | -7.22253 | -60.6213 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b8d36de6-6b26-36d3-8b7b-8223b9b57103 | -9.07641 | -71.94549 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bfeaf771-e8c9-332f-9102-c67b011273fb | -6.25661 | -55.42359 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8bd8740a-2097-3dc2-961f-cd51b9a46880 | -8.40555 | -70.3455 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9e407286-e646-3c54-a1eb-2d4a880355d6 | -4.47943 | -55.40097 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 192896bf-156d-3b15-91ef-f9672f2b8705 | -9.27042 | -71.9086 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d4059b6a-59fe-3b2a-be9d-6c00829f3055 | -7.58183 | -61.31483 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0093872b-2d48-39bf-b24e-7dfe5a4b3da0 | -3.3394 | -57.99445 | 2026-08-28 17:47:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bc0a06e9-2769-386a-9d00-57f32da70f7e | -8.68327 | -62.94787 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8860d384-0fd0-30d8-899c-b855b1068b01 | -7.35576 | -55.17788 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 1fe06f90-c88c-3b02-957e-ebb15e102c7e | -7.09859 | -55.48172 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| eda4131e-2c1c-3baf-9a49-34f70f5896b6 | -7.60525 | -61.35282 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 1ba8f3b2-6e45-30df-b4a8-4bcc7d564606 | -6.65425 | -58.50002 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1adfcf48-a275-3177-9acb-d31e1d80785b | -8.63357 | -66.54104 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4c6f5197-7a16-3bd2-b246-a091be8b81a4 | -7.44305 | -73.20536 | 2026-08-28 17:47:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 37a2f36b-1996-3f33-bd4f-8bbee09696c2 | -4.97091 | -56.29305 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c83f6428-1d78-3307-94a6-0d4c26815d14 | -6.79497 | -59.71243 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |


[Clique aqui para ver as próximas entradas](README147.md)
