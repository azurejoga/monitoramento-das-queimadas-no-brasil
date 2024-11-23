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
| 4b452e94-ffb2-3a07-b97d-d04a2f8db8d1 | -0.26417 | -51.552 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 156d838d-96a6-3278-99a6-76768e0edf4d | -3.93058 | -42.28006 | 2024-11-23 04:16:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fa806f13-90a0-3fa4-878d-73178c7859f1 | -3.23964 | -45.42923 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d78bfaf3-9150-308b-8228-4677e30edac5 | -2.08614 | -46.28319 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b949fc58-ed87-3aad-811b-1b4c790c761e | -3.2655 | -45.44067 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83f403e5-efd1-3a7c-a252-a001246b7064 | -2.6302 | -46.21372 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b37f90bd-81ea-3c89-8f6a-9e4d67a9f82d | -2.10172 | -50.35814 | 2024-11-23 04:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61f6f54d-fb85-330d-9558-771f3288ae5b | -2.69377 | -46.26348 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bda363f-bcfe-31f4-aff6-75e7f4f9650e | -2.70851 | -46.23806 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0d56219-059b-331d-a8d5-83937c3d3603 | -1.10982 | -52.34577 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07f11159-27f9-3a91-92cf-dbe041b7989b | -1.11802 | -48.7967 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f571340-5132-3e06-a31d-c26a289d506c | -2.69605 | -46.27174 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 355cd3ef-a00c-34d5-a639-9ab7ae4c3fee | -1.96344 | -48.38613 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6c0a8a7-756b-3c90-9bc9-fec8c71799c6 | -2.7032 | -46.24911 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08082cb7-552b-37fa-8f52-95e03d882e69 | -2.74299 | -47.54145 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28e2ae9c-3faa-32a8-8747-e76ace9da63f | -1.07255 | -53.36705 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9052e02a-5aa3-3d31-9fa5-eb5391dd4de1 | -1.21855 | -51.74239 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aba2c83-0c49-3d85-90c8-daeddce93c84 | -2.1343 | -46.48125 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69e6d875-23cb-31eb-b592-3b2e708bc49c | -2.56277 | -46.15615 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0a73741-af70-3002-942e-6cbb57edb358 | -0.98164 | -51.72124 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b71a9fea-a089-3477-990e-01a6ab4d4139 | -2.94308 | -45.62049 | 2024-11-23 04:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb8edf05-0757-3173-b3d8-05df0ec2c1df | -2.01238 | -51.17659 | 2024-11-23 04:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 161df6d1-e755-30af-b609-d9f2fc995239 | -2.65298 | -46.13865 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f956a5de-f10c-3df5-bcfe-30182bf27b17 | -1.62366 | -53.31388 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d26fe49-d670-3f35-937d-a438612e2d36 | -2.61575 | -46.25893 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 885daa95-969c-33e2-9b6b-db6d30e30863 | -1.7196 | -52.72845 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73841c6a-905e-39c7-a292-a7b58d5a0dfe | -1.72766 | -52.71264 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e69255ab-b8ae-3900-9a12-fa9b34792a8b | -1.71905 | -52.7318 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 184e4a94-496b-37c5-ac67-62216811e60a | -2.20686 | -48.91514 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1a79be6-6d0d-3e92-a24b-5433a16b0ce7 | -2.18262 | -45.68098 | 2024-11-23 04:16:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 369fff02-5b97-3bb8-8822-9ca684595936 | -0.04442 | -50.8157 | 2024-11-23 04:16:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf9966f9-8f7c-33e4-9720-55b8570ebf2a | -2.01019 | -48.76564 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b37a3fd5-5401-3f97-be24-815298b46819 | -0.27176 | -51.60142 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47ee8164-9557-39be-ab28-c9b2261d5cf0 | -2.71934 | -45.70295 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 946c0947-b00e-39a8-b5ff-13d608a097fb | -2.25591 | -49.00146 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2fcc6a7-b797-3e3c-a58a-e5ca1d89e6a4 | -1.2827 | -54.54098 | 2024-11-23 04:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc0a531a-dcbc-3808-bc0b-4740ac787f6b | -1.13306 | -53.40507 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1451b851-db74-32e3-82d2-60a8546e88fd | -2.63182 | -46.22582 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18e3daae-5d8c-30fe-aff1-112287f72d69 | -1.45203 | -55.45578 | 2024-11-23 04:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcf831c5-f1d5-3c94-8671-5b196aa8b7c0 | -1.62595 | -52.61059 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df4d1206-835c-34c9-87e2-68737ed3ce30 | -1.23411 | -51.74194 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1608bd1-95eb-3af0-9d63-249a9170b88c | -1.73136 | -52.72353 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 06cad8e2-349e-3b5b-a4a9-a2f8c7d36397 | -0.2637 | -51.55495 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7f61b04-8125-361c-918d-e1aabbf95532 | -1.25834 | -53.36749 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37e34e5c-2ed3-35a2-b780-40f1123017e7 | -3.00059 | -45.71975 | 2024-11-23 04:16:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 96765b82-fb06-37ed-bf6f-c792353c1b94 | -1.81903 | -46.61576 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 341f3c65-9926-3212-ad39-82157e568aa8 | -2.69153 | -46.09783 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f418970f-d19e-3b50-ad83-72111b83db35 | -2.57455 | -46.55844 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ca2579e-89ed-3417-8f7c-814eaec79871 | -1.60799 | -52.58736 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f59a4a5a-130c-309c-9bd5-9c9efa1048d6 | -4.56826 | -37.98376 | 2024-11-23 04:16:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6ce45128-885a-37e9-b8d9-fb9cf02cfa39 | -1.11835 | -53.4057 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a9b9922-41eb-31f4-b4aa-e340a3a42eb9 | -2.93849 | -48.02013 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0d6491a-345e-3ef3-9e75-73c7b041a924 | -2.67772 | -46.16217 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a226ce4-c2dc-34e0-bbd0-2c6ea96c4347 | -2.70133 | -46.10324 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7031e75d-e0b1-3e77-ae1a-a05f01f38d82 | -1.60745 | -52.59064 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b10cb5d-b4ad-31eb-86fd-596921bf0091 | -1.9674 | -48.38678 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3b8d695-aa89-3d4c-952b-f186eeeb38b6 | -3.70281 | -42.7911 | 2024-11-23 04:16:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ab60080-ce31-3ede-8879-47604f547780 | -1.43116 | -53.38885 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff044d9f-67c8-3a85-906d-c4bedf7ed86a | -2.44155 | -49.09047 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b4c5a7c-9f3b-35cf-9ab1-85f086e1e18a | -1.73778 | -52.71775 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 61b842b2-8b39-30f2-be8e-105d277e9829 | -1.73191 | -52.72019 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 54e386f0-4ccd-3f0c-bc57-bbf90ada5562 | -3.43945 | -44.07905 | 2024-11-23 04:16:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2bb16fb-b3ec-3f06-acf8-03d6e1fff017 | -1.2057 | -51.94997 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da693253-275e-3ec1-9d4f-41999adaad35 | -2.06606 | -53.237 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f21d4e9-3046-3e6e-9024-66c0cc7dc2d8 | -1.63232 | -52.60489 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a39170c4-ed3f-3038-a4db-827d000f9c31 | -1.19411 | -51.76533 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69c8b00b-0f02-3278-a157-334109af97eb | -2.68345 | -46.17097 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbee91cf-7aab-32a7-adb5-ad604053f923 | -3.24302 | -45.42976 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1912c2f0-90c5-3dad-94dd-519c0165824f | -1.73027 | -52.73023 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1778735d-5776-34cb-a320-eb8c1b471b4c | 1.36749 | -55.95134 | 2024-11-23 04:16:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a105327b-212e-32f5-9006-4b71bb32df49 | -2.53363 | -46.22654 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86144ffb-0424-37f1-bae0-25a2d8492475 | -1.13639 | -51.68044 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 535de7ea-cdbb-3a3d-af93-51160fad32f2 | -3.22963 | -45.38347 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c088332-6393-3a9e-85fd-bcda1be16c37 | -3.26617 | -45.37082 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb1b612e-744d-3ab6-b553-65d647e42d88 | -0.26118 | -51.57699 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75c2f990-28e5-3024-873c-dcaeea218ebe | -2.6904 | -46.17207 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9336c79d-1222-37a1-8b7b-b3c46f867e92 | -3.18744 | -46.55328 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c96e661d-59b0-326d-879c-4f9975871159 | -0.25629 | -51.56878 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95648e5a-e17f-3640-addd-7b6993db5283 | -2.70137 | -46.26071 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20630c1b-8564-3829-b170-2fcc56b74ff4 | -2.3567 | -47.61001 | 2024-11-23 04:16:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbd45de8-78e4-354f-8f99-413a8561024e | -3.32959 | -45.35125 | 2024-11-23 04:16:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 414ef575-bddc-3f84-913e-c1f498a65246 | -2.20219 | -48.91809 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44c863ae-5fed-390a-a37e-545896a7309c | -1.63017 | -52.61808 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dece1de7-88ec-353f-b599-8fdcf4fe1f4a | -1.85319 | -48.75605 | 2024-11-23 04:16:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4edb48b8-31bd-319d-bcde-b57ef3387426 | -2.6662 | -46.55256 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0867626f-9c05-33a5-b698-ece03917a225 | -0.25659 | -51.57318 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6514b3bb-d9ca-311c-8c8a-146051b3381c | -1.19268 | -51.77407 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd10eaae-1b5e-335f-9a9e-fd0f303e27c5 | -2.1314 | -46.40745 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70d07257-de9e-3d02-a076-97a83ebed401 | -2.73927 | -47.54084 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7102f1c-6db4-3829-bea0-6dd98119b3ff | -2.64256 | -46.13703 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7b216bc-8647-3f5e-9b06-c554c9190d11 | -1.4529 | -53.39679 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1a51b351-9213-3413-bbdd-b3a69af185b6 | -3.37956 | -45.31882 | 2024-11-23 04:16:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aea1420a-07c5-3675-a33d-e2ea38dc9708 | -0.90988 | -51.65278 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e31c6ba-4473-3be7-8dd8-e3201e39e5ff | -1.63686 | -52.41271 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51f8298b-7127-38cd-9620-c97ded929381 | -2.44836 | -46.55659 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7046352-1af1-3523-9bca-d42d1f12333a | -2.8013 | -42.30236 | 2024-11-23 04:16:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf2f4abd-ebfb-3b71-a5e8-892cb397d389 | -1.7367 | -52.72441 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b85a1f3a-e7dd-39d8-9f37-2488c9ff658c | -2.70259 | -46.25298 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d7bf8bb-f46e-3471-add6-12f8006c62c6 | -1.18726 | -51.93451 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff60244e-d568-31a4-96f8-cab41a14af3e | -2.7262 | -46.10331 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
