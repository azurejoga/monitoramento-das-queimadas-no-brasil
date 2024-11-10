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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97de4c5b-f16b-3825-b319-6a3a3be12990 | -2.23547 | -53.73514 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 18587a01-4dc9-32d1-bd75-d1dd4f767567 | -3.94811 | -48.1366 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 9b832c95-1f7d-3c97-b277-f37e350fe9c2 | -3.05015 | -49.55589 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c95b3cf9-703a-3031-8ccc-be8cf161e076 | -2.36145 | -50.61763 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d5f92053-08c1-3cae-8c69-6257d8fd0608 | -3.18167 | -51.2191 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 448789d6-0073-3bff-94f6-7dd47d016786 | -1.50745 | -52.18103 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0de34d8a-51b5-3c2c-8c81-dc69535efe80 | -3.55807 | -53.3111 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| be67f934-e06a-38b9-b16d-b7bcaf10c087 | -1.75404 | -55.03802 | 2024-11-10 01:19:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| e1656ed0-1d00-38fa-a28a-7f57cffeacfa | -3.9546 | -48.19351 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 8d653fc1-22f9-39fa-a301-7b1ab862cc1f | -2.9342 | -51.78512 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 246ce942-bc95-3db2-96f1-835a7b29b79a | -2.08152 | -50.34432 | 2024-11-10 01:19:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f579742c-98dd-3bce-b49f-a034f7fb4e13 | -3.44443 | -50.3069 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| a2233cfe-b4ea-31d9-9802-8ec2427280f2 | -2.83755 | -49.05947 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| d1bbfaa6-59b3-3395-92b0-f79f7b952928 | -2.21713 | -47.7545 | 2024-11-10 01:19:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 5bd6bb91-7556-3762-8196-c866a7565916 | -2.7304 | -51.7205 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d07f1ee5-f05a-3564-a776-dc179c8fe9da | -3.96455 | -48.17108 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 438d67a7-ee88-3e27-a316-347780b8dcac | -3.26155 | -51.01501 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c7fb529b-01cc-358b-b0e2-3ac94fb8428d | -4.28252 | -48.1885 | 2024-11-10 01:19:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| be5bec42-b065-38b9-acc6-5d1e7aca4599 | -3.95144 | -48.17278 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 9a85392a-a274-373d-a5f8-a12d986edae6 | -2.91922 | -51.68113 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e65e7a5e-bfa0-3882-b9bc-8cffedc1de55 | -5.32657 | -45.04583 | 2024-11-10 01:19:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 0408d583-968c-3f41-969b-b62d18daa813 | -1.53216 | -52.21204 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 433.4 |
| 5f3a51c4-2b56-3d49-898c-287ebeae8339 | -2.75373 | -49.36881 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 0df4c690-fd4e-3328-a008-87e161c79071 | -2.19946 | -48.36349 | 2024-11-10 01:19:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| dc3c593f-b239-3642-9784-ab2a43f64a78 | -3.57269 | -45.82155 | 2024-11-10 01:19:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9ba80239-4e65-3b2e-a66d-eaf91ac04fe2 | -3.23098 | -50.26199 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 3ee542eb-ab62-344f-8517-9d0cc8709d7c | -4.63585 | -49.08848 | 2024-11-10 01:19:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 28f09e29-a3ed-315f-96a4-d8f096d62aa8 | -2.96436 | -53.87406 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 55b872e5-3b03-3f83-ab0b-87bd22edb85a | -2.40986 | -50.30817 | 2024-11-10 01:19:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 69f5c33c-15cc-3ed6-944f-bfd32ab204f9 | -2.63242 | -54.66411 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 88ed61a3-df80-38cd-9d19-decb5cb6fe20 | -1.45094 | -55.50835 | 2024-11-10 01:19:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 91afcc8b-9023-310c-95d4-4c4156c9abe2 | -2.62529 | -46.78465 | 2024-11-10 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| fd664174-2788-355b-9927-89b32c59c8db | -2.2083 | -47.75049 | 2024-11-10 01:19:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 0cd16ed0-d005-35a7-b8f6-96cb4411f57d | -1.51418 | -52.15693 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 534d7c9f-0d97-3831-8c02-8c6a30b0c30f | -3.22902 | -50.25389 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a7fbebf4-8d9a-3143-8c4b-303faa5b8d47 | -1.467 | -54.30174 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| f6a03096-5656-3419-a83c-493fe3d34665 | -2.09859 | -48.84336 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6fc44470-d80b-3b7e-8c32-40ef86fa55f1 | 1.62479 | -56.05059 | 2024-11-10 01:19:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4b8e241-a8c2-3b0c-abc9-a5a9c7df5594 | -1.23172 | -51.96829 | 2024-11-10 01:19:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 06e9f5f8-7ef2-368c-991a-f453a36184db | -1.46225 | -51.49423 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f51bb243-e460-3111-b00f-3fca70de3eae | -2.42627 | -51.95337 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4ea19382-a285-3a96-b885-82ea82def7d0 | -3.25352 | -53.7023 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9e7545e2-8e7d-3bc0-8795-061b24b77142 | -2.23159 | -53.77361 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 3272f431-d47f-32a0-a5f4-329ca73a5e0e | -4.11057 | -51.07958 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e1e1790c-c5cf-34bc-b12a-3a28c76c6db4 | -2.62118 | -46.75648 | 2024-11-10 01:19:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| f0b0aa9b-8535-387d-b67f-9c87ad5f722d | -3.28624 | -53.67291 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 41600298-780c-3037-a439-a1954b78f21c | -3.21993 | -50.27017 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| b8fcc9a3-5b28-34ad-b692-e01869f682cf | -3.69218 | -51.29578 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 3e078cb5-69fc-36de-af36-9386c5cc867a | -2.47108 | -48.4337 | 2024-11-10 01:19:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 092bb619-22aa-3a8e-b624-55abf481a2a8 | -2.73378 | -51.74383 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 83194c11-ab1d-367c-9950-e4287cc30302 | -3.90562 | -51.92641 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1d08c05b-c8bf-312f-94ca-7cd6da187977 | -3.6251 | -54.11467 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2fe11043-b8b7-3f83-a1c0-2cae183d1cb8 | -2.25363 | -53.73254 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ce7edf7-d61a-34f2-93be-0f216bd84c79 | -2.9311 | -51.47363 | 2024-11-10 01:19:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 8e8f9534-100b-3da2-80a4-f8d1271eca69 | -2.60491 | -54.19893 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 84c0ab92-13fc-314a-8939-f3d2b47ac11f | -2.62196 | -49.471 | 2024-11-10 01:19:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a7642cb5-d3ab-31d4-a26c-89a8c06a1c01 | -2.04698 | -52.09022 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 27c46c05-87fe-32e5-91fc-b1e55497fa15 | -1.666 | -53.81483 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e92dbba7-c830-3230-971a-35133f11d0a2 | -3.2548 | -53.71149 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c461aaca-693c-3e90-948e-754ab176f900 | -1.17915 | -53.69425 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1c0196bd-ae3c-367d-8862-20d4aa059e06 | -2.20316 | -47.75648 | 2024-11-10 01:19:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 98c27413-a332-3084-83ba-1d9d7af06f9c | -3.0564 | -54.00294 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 98394640-4d2c-364d-984c-9140488f7b1c | -1.52062 | -52.20219 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e78802c7-fc10-3100-b0f7-e56193ca7138 | -1.53375 | -52.2233 | 2024-11-10 01:19:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 97010bfa-9af8-368f-86fb-4ad12489d547 | -3.48936 | -54.58976 | 2024-11-10 01:19:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5306152e-54c1-3b6d-af87-76c47d22a4c4 | -2.36389 | -46.87171 | 2024-11-10 01:19:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 29bd3761-f60f-30d7-bfca-3900c76b4cc5 | -2.43277 | -46.30859 | 2024-11-10 01:19:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c8e06d52-07bc-36a5-94a6-f54cc4e5ef59 | -3.62209 | -55.47958 | 2024-11-10 01:19:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| be5aeed4-bf4d-3682-a1fd-f4e3566641db | -3.5115 | -54.02736 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8ea3872d-222a-3706-81ae-6f236dc5717d | -2.87581 | -51.30714 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6421b0d1-7462-3dd0-8c21-c6da7438e2c2 | -4.06376 | -49.27995 | 2024-11-10 01:19:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e388baac-fc70-3824-941a-a197b0bbc1fe | -2.83488 | -49.04115 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 703de5c2-200f-38f8-b13b-d5926c48234f | -4.06722 | -50.00887 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| abb027ec-7115-3b08-adef-d53f0c23599e | -2.2137 | -47.73066 | 2024-11-10 01:19:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 92b26b5c-85d2-3b9b-95b9-9df0e9e59e5f | -2.58009 | -51.88415 | 2024-11-10 01:19:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 64edb717-b144-3ee1-ae65-6fcda4a2326f | -4.18395 | -50.42669 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 97a5c6d2-dfee-33ad-861b-559c34d4e336 | -1.83891 | -52.0692 | 2024-11-10 01:19:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 70018a05-1ba7-3c82-a176-aa037956adbe | -4.20567 | -50.62315 | 2024-11-10 01:19:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2bc214fb-f9cc-3799-ba4a-0a7ec160a63d | -3.5263 | -50.00398 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b6831cf7-828b-33bc-9bea-33d9638a8962 | -3.21896 | -53.0661 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| f13c07a0-b328-3c94-b591-b58d2a948294 | -4.20764 | -48.12294 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 82da28d5-fe56-356d-a910-adcbd61ef703 | -3.29207 | -53.25199 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 5542f717-81d7-3146-af2c-2f5e99772b01 | -3.71781 | -53.40066 | 2024-11-10 01:19:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 128f0379-d147-36aa-9639-0290e2b3c7cc | -1.2279 | -54.172 | 2024-11-10 01:19:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9acd3f28-85b0-3462-b9da-c4a4ae26ec29 | -3.30145 | -45.68643 | 2024-11-10 01:19:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 9058b3d5-5b00-3597-98a4-439392189f50 | -1.20779 | -53.63124 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c8a89417-2dfc-3e68-914f-0df9983e3acd | -2.73209 | -51.73218 | 2024-11-10 01:19:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 79d7a8b0-07cf-33e1-8f30-8cda7f4f5fea | -2.95708 | -54.34938 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 210fb75d-9fde-3e66-883e-68cd4df561af | -3.19255 | -54.31605 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c390d6a1-bd06-30d4-bcd6-5bd89a305b29 | -0.88687 | -51.7781 | 2024-11-10 01:19:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ad82a5c9-9c1b-3f24-89f8-d97a80b55c82 | -3.21479 | -54.94036 | 2024-11-10 01:19:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f617fc8f-bad7-3e39-8e79-5586af573f00 | -3.96767 | -48.1917 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 6b6682d4-64df-3a69-91ee-3995ff16b299 | -2.9179 | -49.35679 | 2024-11-10 01:19:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 0b0a4881-8328-3919-9dd8-1de94f41e1ef | -3.95825 | -48.12943 | 2024-11-10 01:19:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0906b3ad-1f51-38c9-99de-3540bfc290b9 | -3.24512 | -51.24148 | 2024-11-10 01:19:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 59586190-4493-365a-bd89-1b5b5584151f | -2.45312 | -57.94081 | 2024-11-10 01:19:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5f9f9ab2-452a-3993-97df-13f8253b04f9 | -3.15968 | -54.48056 | 2024-11-10 01:19:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bb4d3e53-0cf8-3a9f-b01f-083275b8673a | -2.42852 | -49.87383 | 2024-11-10 01:19:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1faff4c7-9cb2-37ce-a50a-a5ca8406d765 | -3.22821 | -53.06472 | 2024-11-10 01:19:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 267.7 |
| 17015810-74a1-3211-ac41-d1d6e3e3987c | -2.84924 | -53.97065 | 2024-11-10 01:19:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README10.md)
