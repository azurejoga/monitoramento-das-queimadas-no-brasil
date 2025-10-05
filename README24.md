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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 094d2a84-77e1-328d-b903-5c5d2c708ac6 | -6.14981 | -44.67521 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6e9be456-19c3-329d-80b2-15fe7b6535c7 | -7.02599 | -42.78977 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 58fd5458-e647-3959-86b8-0e42e458f715 | -6.14435 | -44.64878 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a11f8534-1859-3e79-9376-24c4cfbcf558 | -7.0603 | -39.37783 | 2025-10-05 03:32:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8e8da96-29cf-3473-90a6-41bf33b96f16 | -5.79052 | -42.9724 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b2a7114-2197-3b7e-86c0-8a3bffe6e8c9 | -6.14186 | -44.64393 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 8f816724-a261-343a-a41a-3890980ac1f5 | -5.88807 | -42.91467 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| f5d15e40-32bc-39b7-83c6-877accc9f7d1 | -5.26329 | -39.27076 | 2025-10-05 03:32:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 751284d6-38a9-307a-aee0-df8ad2f3d209 | -4.50806 | -40.73721 | 2025-10-05 03:32:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18bfa5e9-93d8-312e-a669-d24a699c58fe | -3.84901 | -41.58862 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 716bd5b8-ff55-3f30-a3aa-25711c578d09 | -5.78677 | -42.92476 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 1d0578d4-c441-33e0-8125-336467a3e4cf | -6.02341 | -44.02679 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd419791-450a-3452-80c5-9782d197328d | -5.2523 | -42.64019 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e99e287e-a0d9-3ce3-b4a3-8870c8e52841 | -6.61303 | -43.72732 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bcb7dc73-29e0-3d6a-b705-ab33d5b90708 | -5.48772 | -42.80402 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| ed4a10c6-c895-36f5-b33b-30b2a9bf73eb | -6.2517 | -45.34555 | 2025-10-05 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a962e07e-94dc-3183-a7f7-ee6860783a85 | -6.40392 | -43.05131 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e4f42478-6e70-36a3-9a7d-aeaafcd8f8ac | -5.49292 | -42.80323 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 48f83331-4d26-3049-90b2-786aff69f0be | -6.40314 | -43.05571 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 73ff7c71-6f78-32d3-a1ca-641cca7a6d2c | -4.87693 | -45.85531 | 2025-10-05 03:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 99ff4b33-eff7-3768-a13c-93bf2c63dd7c | -5.83791 | -44.44866 | 2025-10-05 03:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| a8e8249c-17cf-3993-b958-d1fcb507bee8 | -6.63718 | -42.80597 | 2025-10-05 03:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5356aad6-293b-390c-9fec-7b4298f7c3f0 | -5.98299 | -44.36214 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e200dbf-70c6-3048-9923-afe0039f36ac | -5.87641 | -42.54599 | 2025-10-05 03:32:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 4eca63cb-7023-3caf-ba43-0d8073d0e533 | -5.91283 | -42.53425 | 2025-10-05 03:32:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d128aaeb-2448-311b-bbcd-5e5a8c5501c7 | -7.03651 | -42.76545 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 163238f1-ef34-3513-8d4d-42975a84f365 | -6.70349 | -42.17552 | 2025-10-05 03:32:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 242c4585-cd13-3c34-9837-533a3d0e9f9b | -5.84495 | -42.80956 | 2025-10-05 03:32:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fd898243-5129-3e36-8c3d-bec1976b0f8d | -6.14871 | -44.68114 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5661a300-fd1a-360a-90d4-9503855d878d | -6.25401 | -45.37151 | 2025-10-05 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4adab60a-b8a2-30ee-b4f8-07693cf895bd | -5.76956 | -42.98007 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea89eef1-20e5-3289-a228-8254e67cbbf0 | -6.12465 | -42.86513 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8307cdb0-f8fe-3780-93bd-0dd8502d75fd | -7.02874 | -42.80778 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d3634bac-a38b-3416-a072-cdc2ab9ed0e5 | -6.15311 | -44.65746 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| c9bf98d2-37c3-3844-afec-1e8dce8140cf | -6.14579 | -44.67912 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 47806226-920f-3efc-a650-e4c021d9e760 | -6.33196 | -43.45422 | 2025-10-05 03:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16cadc5f-7fc6-3307-aeaa-f36a93dd2667 | -6.16081 | -44.65304 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2638d96e-554a-3582-831a-6a8f8f2e4086 | -6.12378 | -42.86991 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8b5e183f-9238-37ae-931b-d618e656e3bd | -4.64626 | -43.1913 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d3a5d3b9-e42d-3925-bdff-83b5d3b46457 | -7.14725 | -38.5176 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cbe3d65-f7ad-373b-ae26-184e0c050bc7 | -5.85337 | -42.79711 | 2025-10-05 03:32:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 54d1bc48-7ae6-3ebf-904f-0b32281c3dee | -4.44718 | -43.24139 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 29ec0659-12e5-32d6-9e6a-121530515c2c | -6.13519 | -44.64279 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8f8d7f4-946f-39ff-bc4a-187d8d289f33 | -3.4433 | -43.33993 | 2025-10-05 03:32:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae5662d3-5c48-3749-ae45-3d8957a18faf | -5.79011 | -42.96975 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 29b1539b-1ef0-362b-9d62-e33d67ad2983 | -5.24711 | -42.63473 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 928558cf-5568-3476-a021-a1ef3ea9c9c8 | -5.84225 | -42.89314 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 27934c52-9cb2-3087-a8ac-7e553c6010b3 | -5.24038 | -42.63791 | 2025-10-05 03:32:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e07505cd-ee41-3702-bf68-a8a6d1879f2d | -6.55854 | -44.1593 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b66208f-2341-391e-920d-578fe38586f5 | -5.8431 | -42.88845 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a289e934-eb5f-38b8-a151-6a6e0a56c9ce | -6.11869 | -42.86399 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 776a87e0-c59c-3e9f-8cd2-612b68da775e | -6.46183 | -44.58393 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ea6a516f-654c-3131-99f0-cfa295eebfed | -4.6525 | -43.19244 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 90bd2568-8d11-3637-8d10-23c68707740b | -5.93919 | -42.87787 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9ebd4c7c-fa75-3bba-a2e5-d0a128ac6437 | -5.66636 | -42.75139 | 2025-10-05 03:32:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6a6f0b1e-a9c7-3762-a238-7bb331dcfc94 | -6.62848 | -42.42398 | 2025-10-05 03:32:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f837e5aa-83c7-34fc-b9bd-7f4be9009fff | -6.36663 | -42.88095 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cfeed059-0011-30e4-9e33-1949ebd248b8 | -6.71032 | -42.82687 | 2025-10-05 03:32:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c72be8be-850c-3bed-b808-ce4fe0231abb | -5.77654 | -42.94655 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 9b4dedcc-7ab8-3db5-b839-a0611ad8a151 | -7.02015 | -42.7886 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1eb5f7da-6f8f-36aa-90d1-04dcdb99ae75 | -5.89409 | -42.91575 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 9f046066-2c2b-3925-9b43-41c20441272c | -6.14546 | -44.66153 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e71e1847-9788-3408-9861-f15a1ae0a06e | -6.01695 | -44.0258 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0caac454-b421-3569-ae18-d29c1308ab0a | -5.88888 | -42.91007 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 9b69a0ad-0188-3b54-9cc6-2031b4a903f5 | -5.77117 | -42.97099 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea082c62-9077-3a75-9b20-a5349e20c8fb | -7.0299 | -42.76851 | 2025-10-05 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7237bb13-ab7a-3eaf-b132-c7f6c0c823b5 | -5.09296 | -37.6058 | 2025-10-05 03:32:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 595be067-b086-3380-b9f4-b4236f887cd9 | -3.84601 | -41.57172 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| fe2017e9-8962-37e5-a79b-9e957f257d11 | -7.01188 | -40.32088 | 2025-10-05 03:32:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 34aab5c4-c8f2-3407-aa72-aa96516d6759 | -6.2136 | -42.93147 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7614a42-1a7f-3f52-8676-9d2667bcc7ba | -6.60253 | -44.31933 | 2025-10-05 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db058287-1bce-3ee0-98fe-686f3557a4a7 | -6.60855 | -43.71669 | 2025-10-05 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c284980a-d146-3cca-9320-a93235431134 | -4.63291 | -43.19402 | 2025-10-05 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 080d4c02-f932-34c2-b9e1-3fb34d7d625c | -3.8411 | -44.55708 | 2025-10-05 03:32:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcfc3558-6342-3ba6-a631-6e6bc54eb9e2 | -7.29352 | -39.26723 | 2025-10-05 03:32:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bd72dc78-d93a-393a-bfa9-3c0dd98ce9a1 | -6.12546 | -42.86074 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6e5ff5b0-8e65-398b-80b4-0dcd956c256a | -4.43808 | -43.23778 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0053c37f-dcd8-30ad-a2d4-5238cb4cd918 | -6.37176 | -42.88655 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e220d400-d46d-34fc-b817-00b28e561f50 | -5.9707 | -43.50597 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67ba126e-dd4e-3bca-b753-8edd9f9249e7 | -6.1475 | -44.6506 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 9d59f44b-0db6-392c-90d3-f491195d8ef5 | -5.96986 | -43.51061 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 737ccaa8-1a0a-3335-bfee-280fa73d174b | -4.43723 | -43.24271 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 38f97a02-7940-3eb9-bda2-4805ecc7e522 | -5.74337 | -42.04511 | 2025-10-05 03:32:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ef188e96-1248-318a-93cb-229563c6391e | -6.9212 | -37.43863 | 2025-10-05 03:32:00 | NPP-375D | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a5775b6a-1851-3cfe-ac62-6e0d9e7f2480 | -6.20684 | -44.08049 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7dfd812e-de7d-39d8-8c0f-63b04d363112 | -5.97644 | -44.36087 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e8fed47-e518-3d2d-af4c-f5c421a7a110 | -6.40756 | -42.68967 | 2025-10-05 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fdff00b6-ade3-3566-b9ee-489f5b47d5ae | -6.14037 | -44.67092 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1e963de2-c8bc-3a76-81b5-e175817a08a1 | -6.45836 | -44.58645 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8b2f59f4-d49c-3518-a23a-f0c63cac6440 | -3.67214 | -41.7567 | 2025-10-05 03:32:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18c54dee-a568-30dc-a276-cb156aef28e5 | -5.79659 | -42.97334 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf79a051-2532-30ae-a61a-34db2f138686 | -4.4515 | -43.23506 | 2025-10-05 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95c3de09-9892-3ba8-901c-50aeea3d995e | -5.74406 | -42.04115 | 2025-10-05 03:32:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 150a6016-8bb3-3bae-a371-7a77485f317a | -5.96189 | -43.51907 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9492d61e-d3cb-336e-afee-78cc98801a03 | -6.69368 | -41.95754 | 2025-10-05 03:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 890ae7b0-3554-3547-b0e4-45fa05a24578 | -5.9877 | -44.36405 | 2025-10-05 03:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a820bc7-ff8c-3c31-8d7f-74e466bc60d7 | -5.77679 | -42.93913 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 72bf0c26-05ee-397b-81ba-d4a3ed4ff6d2 | -6.40497 | -43.05419 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 6260dea0-cd84-3f17-a147-df2b8564dd7f | -5.79537 | -42.9753 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6112fa3b-2fe7-3583-814f-c275b825a33b | -5.92313 | -42.89801 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README25.md)
