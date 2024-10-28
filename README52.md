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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fbf6262-a1ad-3194-83b3-04865f022183 | -4.15049 | -48.76449 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41dc4d47-05c2-3380-968e-ccb9419d02c8 | -4.14969 | -48.75771 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f653f453-1493-3c6a-bd84-59cb779f04d3 | -4.14918 | -48.76119 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8c71bfe-1aaf-31b5-ab22-4ab4caf2b8d7 | -4.14867 | -48.76465 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23b374b7-3cfd-37b1-8839-15db264eea3a | -4.1481 | -48.75348 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9616aa5-2dd4-324b-a365-ed6657f8070c | -4.14757 | -48.75694 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0420752d-99b8-3ffc-827e-121c70aa2262 | -4.14704 | -48.7604 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58aa273e-67c2-3f6e-a57a-064675ff375a | -4.14651 | -48.76384 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6eec6d1-ad23-3338-a773-c8fb2f456691 | -4.14411 | -48.75287 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87c341a1-a6bd-338d-9800-69196195f23a | -4.14358 | -48.75634 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7ca6111-c64d-3522-bc2d-f3619f1d21ab | -4.14305 | -48.75977 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff1b9c8a-8012-315c-9b37-3a2f43f3f5e6 | -4.1112 | -48.2804 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23a1ec1a-06e1-397f-bebe-7c2a0f2b3ab8 | -4.10313 | -48.50612 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3861c40-f6ea-33fe-8adf-482b4b087040 | -4.10261 | -48.50965 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9130898-6ce9-360d-be52-841f0ac9f052 | -4.09908 | -48.50548 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 920b9f20-c7fd-37a6-98db-7e43c15a8535 | -4.09856 | -48.50904 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e9b36c2-c515-3cd7-8a4d-57445223be6e | -4.09825 | -48.2341 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a4d10d26-34d0-387d-9392-9e79cca25bd6 | -4.09767 | -48.23793 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 31095f08-4b31-39fe-b1d5-3d54643f24bd | -4.08757 | -48.3044 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4afb2b45-c43f-3b11-a783-be9077e41e97 | -4.08701 | -48.30808 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fee1ca87-8930-30df-8fb3-ac9209dd1678 | -4.07169 | -48.2983 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb65ff97-3189-3ca1-9a16-6a04d0aee25f | -4.07115 | -48.30188 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b2786b7a-3663-3ea5-b11e-b655c8debf1d | -4.06814 | -48.29397 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29054a48-d8dc-3b06-8cbe-3769b64eb508 | -4.0676 | -48.29759 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6db6419-6b77-3014-96b2-7bca92c5bfe1 | -4.06405 | -48.29321 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 074d3c4a-2fef-3dda-b126-7332b33a1db8 | -4.0635 | -48.29686 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8a4acd8-1897-359d-be07-e041781bc08a | -4.02904 | -48.30273 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b71c9bbe-7511-3fc1-80b9-0466f5ad41d1 | -4.02851 | -48.30634 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8629d3f6-fced-33ae-bc80-569ce4174b48 | -4.02604 | -48.81503 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f63d4de4-ce4d-3bfd-99c8-d671dc1ee328 | -4.02526 | -48.82013 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad57b351-b9ad-3d04-b0eb-e178ec9d19c3 | -4.02492 | -48.30225 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e05c064-8baf-330c-bcb9-ee618b6897c4 | -4.02474 | -48.81615 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0aa066cc-8800-3752-b1e2-2c1696e6c1ed | -4.02399 | -48.82126 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f9395c8-aab4-3420-b11a-b15c7b04fdde | -4.02208 | -48.81442 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3451cd2d-5310-3ba3-85ef-1b47c29597be | -4.02129 | -48.81951 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b72a7d17-9576-3afd-80de-b7f4dafbbd30 | -4.0208 | -48.30177 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f498ab98-e608-39a6-96a1-8496d46e67cd | -4.92226 | -49.01888 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0035ec39-99a6-3e39-833b-9e5c59ee3443 | -4.92138 | -48.63166 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9caf27b4-af12-37e0-ad52-b18052daf7ef | -4.92083 | -48.6353 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fb80acd-1fd4-38b4-8317-9e92c31560b0 | -4.91829 | -49.01832 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f7344f22-abf2-32f7-a451-5cafd19ba5dc | -4.91676 | -48.6347 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88748eb6-db7b-3b6d-9915-e3c0e88c63ad | -4.91269 | -48.63409 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9df2ac0b-a9f6-32a4-a67d-18f94bfd26cb | -4.90954 | -48.9952 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c82e379d-dc6a-3da7-8897-5ecf8013ef39 | -4.90558 | -48.99456 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8afdaff-ecc4-33dc-b435-a1687f05aa8c | -4.89725 | -48.65384 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e274a20-afe7-30c5-9de0-f197072ec960 | -4.89481 | -48.64241 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef468427-a29b-312a-856d-8490f6e712af | -4.89318 | -48.65325 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 497a162e-4a23-3d01-91d2-87b0e3a5ae48 | -4.89264 | -48.65683 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ad93d15-c902-3223-8b82-94ded372d3cc | -4.89074 | -48.64183 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d438995b-a34c-3ce2-8db0-26664613360a | -4.8902 | -48.64544 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9108d6a5-16d9-3d3f-80e4-6a33dd45639f | -4.88422 | -48.62984 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0c5a558-d897-3dcf-a9fd-4ae4398e27c3 | -4.88345 | -48.66277 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47bcc3a6-1c73-3c80-8460-715d48eb57f5 | -4.87492 | -48.58041 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96e1c688-8e63-32dd-b494-2bc4cf8dd55a | -4.4873 | -48.21742 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70c9f588-5785-381f-a89a-6c29f4776339 | -4.48517 | -48.11599 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 747c04bc-3f04-3ee1-8825-d27806fe4d27 | -4.48461 | -48.1198 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5b1a8aff-b7d3-3264-bf3b-514a3b4ab0cb | -4.40391 | -48.61284 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 355772b7-9fa6-3775-91cc-3cbd6b8c6878 | -4.36727 | -48.49406 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b524bd74-135f-3ebf-a670-691314456e7a | -4.34894 | -48.61581 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a6d9719-3d8a-367c-b81b-ff42c431b64f | -4.34625 | -48.63369 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6572e769-e412-332c-8dd8-56151ce424f3 | -4.34543 | -48.6117 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d0bc00b-b804-363a-85a2-53a5cd4b3295 | -4.34221 | -48.63307 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a1cf06f-739e-32a1-9278-af46ce33070a | -4.34116 | -48.6401 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e0b4c11-24c0-31e3-9192-2448fc36c378 | -4.34086 | -48.6146 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0a12a29-1866-304b-8108-687678b04ce5 | -4.33713 | -48.63948 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36fa1958-7b2b-3882-b893-78044e475b49 | -4.3366 | -48.64297 | 2024-10-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30f6ce84-ff71-3cc2-8991-0acceaa1c00e | -3.69296 | -49.052 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c7e8a77-639d-3ce1-826d-638036de1f12 | -3.93745 | -48.3602 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32acc620-9273-3ff4-ae9a-d68b680b07cc | -3.93552 | -48.34521 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12fd12bd-76c6-3811-bcdc-4d3a9e3aa107 | -3.93497 | -48.34883 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 738b5501-40ab-3621-9329-61a93a596303 | -3.93196 | -48.34101 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6828c787-a756-3597-b25a-d380e4250c08 | -3.93142 | -48.34466 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afd0cd18-c64e-33cc-bef8-0d1bda1c78b4 | -3.93088 | -48.34827 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| de83f628-babc-35f4-9442-31ba2619cb9b | -3.92574 | -48.00026 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32680300-ea04-3e12-a6ee-96f3e09f1099 | -3.91082 | -48.37086 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acbd623e-a7e7-3e7e-a32e-a6b8450f0ab2 | -3.90727 | -48.36667 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88881f01-6db2-3a65-9d6e-5f7df8424606 | -3.90674 | -48.37025 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2deaf989-9ddd-35db-a267-7f46b4a47054 | -3.90266 | -48.36964 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd3d3304-43cc-371e-8f68-4d5cb7209217 | -3.8706 | -48.36119 | 2024-10-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da911879-5fec-3690-836d-01ef302bc3d2 | -3.82531 | -48.89164 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f292c660-8ca4-305d-a772-0eefd9678581 | -3.82285 | -48.88105 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6e386b2-80ce-34ed-9340-c569dca2a214 | -3.81891 | -48.88045 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| be67118d-2179-3080-a551-ce4194a9713c | -3.81497 | -48.87984 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7ec3c8d-7a8c-3416-9885-6d0f10099682 | -3.81483 | -48.88274 | 2024-10-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 341d31d3-e98e-3018-9975-58ef0ef00e78 | -5.41917 | -49.23851 | 2024-10-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 99791b1e-de56-356c-a40a-e33f5648fd9e | -5.38459 | -48.34892 | 2024-10-28 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db3434e0-7c92-311a-a44d-e414265a0c30 | -5.2321 | -47.9509 | 2024-10-28 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f38ff1c-06d2-3779-929d-010d0170fcdf | -5.2315 | -47.95489 | 2024-10-28 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af360fb3-b39a-3225-8c45-1ece680d3a8b | -5.22781 | -47.95035 | 2024-10-28 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d9ca89a-8592-337d-ab0e-74c0f504020b | -5.22721 | -47.95433 | 2024-10-28 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3a7acf9-0aab-3b41-bfa8-c3fbebf24ca2 | -5.20643 | -48.12199 | 2024-10-28 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a05c8758-76eb-33b1-8fe0-d941383cbfdb | -7.95994 | -49.05537 | 2024-10-28 04:57:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c9d49db-803a-343a-8c66-4aa9a93160fe | -8.13961 | -49.48061 | 2024-10-28 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66cd3953-2329-30a2-9e97-7e301d402fba | -8.13908 | -49.4842 | 2024-10-28 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 571db587-c3a4-340b-997d-f3bd0df8a97b | -8.13856 | -49.48778 | 2024-10-28 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 940183c2-815c-3135-adde-75376793d521 | -2.18767 | -49.09396 | 2024-10-28 04:57:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9366586d-603b-30d2-99fb-913cb51c0c35 | -2.1547 | -49.30945 | 2024-10-28 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a2b46d3-349d-35c3-acf3-d2a578dcbe88 | -2.10141 | -49.27508 | 2024-10-28 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19a622c6-afad-3cdd-a473-2b16eacdc7e4 | -2.05307 | -49.48718 | 2024-10-28 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c811e456-dba9-36cf-a965-3c9cbda2128f | -1.42286 | -49.02504 | 2024-10-28 04:57:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README53.md)
