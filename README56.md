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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 473f7fc0-7b92-3788-8e64-e14f250af8a3 | -3.98989 | -54.45254 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c9f0712-e55e-3215-80f9-6d0717342a73 | -2.79358 | -51.41041 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8492720e-490b-387f-8003-2b59b0af4142 | -3.22068 | -53.89605 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 280c763d-a4df-32f6-9628-88c32fcc4eec | -5.10443 | -46.22793 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e37e982-ece8-3bb1-b1bc-f8a8f6b23c18 | -2.83377 | -48.43425 | 2026-10-10 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46ff8c22-1b01-35c4-9664-5e5d0d1b55c4 | -3.45854 | -50.58231 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a8e55c8-5369-39fa-aa79-96941174f394 | -5.9256 | -51.81565 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df373167-8864-31fc-a73d-56aaa8ee8aa2 | -3.22398 | -49.43085 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| e57a348b-25d1-3536-bba9-b94157e56a88 | -7.09883 | -41.75169 | 2026-10-10 04:44:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e5ebd618-52be-3fb1-8aa5-1e47be3f89e1 | 0.99842 | -51.09695 | 2026-10-10 04:44:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 34d83f95-7a87-3645-a054-16da1b8995d0 | -2.21906 | -53.69925 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6f42f76-468d-3fd6-8f39-c39fd3046b96 | -7.24029 | -44.1692 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7351c832-4dcc-3470-b359-8fd391d75c0e | -4.28091 | -48.57986 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 237c7e2a-ef65-3320-a53a-f3974ab0ee07 | -2.39226 | -51.29483 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba5e95bd-d272-3a48-a72d-e8045d420846 | -3.01144 | -51.00737 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ec7a169-1e54-322c-8bc3-278c2d82ff52 | -3.32516 | -50.18011 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 648ec507-b69c-3570-82da-1282398469bd | -4.95025 | -49.4165 | 2026-10-10 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeca432e-4152-3ab7-82c6-9705eb54f305 | -3.2084 | -53.85624 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 58e633ae-e66d-3fdb-937c-bd7517c70952 | -2.7903 | -51.40702 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f205647-99d4-397f-b270-7e75fb37065d | -1.08462 | -54.1064 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa88d83e-a7b3-3f9d-a8c0-59639c662dd8 | -2.93168 | -54.08361 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba463d96-43a7-3539-b6a5-93d00581149d | -5.71642 | -53.47848 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbbe0816-95ab-3304-a51a-d1d9256faf50 | -1.51631 | -54.52576 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01557aed-c049-394a-9821-86fd40dff1ca | -3.26324 | -54.06191 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62c3f05d-1301-350c-84bf-1485c373b86a | -3.23251 | -50.17805 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80537fd6-01b1-3669-8ffa-557448d2296e | -5.7525 | -45.1264 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a33f0edf-4337-3f70-9a9d-527c0e2baf8b | -3.02143 | -54.10579 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dacb09bc-e891-332e-b02d-254b0d6808c5 | -2.84076 | -49.87981 | 2026-10-10 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a4854d4-1a72-37ba-b3a1-ed1b2f63497e | -7.2048 | -44.35477 | 2026-10-10 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84e1cd69-8108-33e4-9869-8dc7f000b137 | -4.50336 | -47.14232 | 2026-10-10 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df167d7c-0d94-3fb5-8e1e-a02faffb7817 | -3.30179 | -54.08816 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2558215-37d5-3e3c-8370-ea497ba74035 | -3.03833 | -50.34031 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 62318cc5-cfb0-390d-8a70-8a00ff3bde22 | -5.78955 | -53.81111 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9eb459d8-c5ab-31f0-9ecc-0a567bbc8636 | -3.90273 | -55.81241 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea306b29-4456-3d3b-82a5-c38aa05c546e | -1.11152 | -54.15405 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6de3a2e6-6f19-32ad-942e-7902e0e01559 | 0.48124 | -50.78535 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76ef79fb-72f4-3aa3-b033-b14fff7c37bb | -5.5987 | -47.27599 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77de9b75-34c8-3ea8-a1e3-6e3caac0cd6c | -2.49439 | -56.18885 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f404b98c-d2e6-3f5f-9dd0-022e0af7cec5 | -3.09885 | -49.35571 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 808e0a45-1551-3526-8530-44ccb5356b17 | -1.28199 | -55.74834 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dc3fca0-4347-35ba-8748-4eb47784b3a1 | -4.12484 | -54.03508 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2421c883-faaf-3c9a-a029-47bd5318569b | -4.09534 | -54.01555 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a841e646-af33-3ef2-be84-0bed5aeb4518 | -3.87423 | -55.98475 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 54b90d1c-b191-344e-9c7a-995ed3a82c15 | -3.1072 | -53.96235 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9bc84df-94e4-32b1-bbe4-35c211f4e9fe | -3.0341 | -53.8945 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 01a4d93f-56b4-35c6-ad1d-1abb2d01f613 | -1.28089 | -55.75509 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 602c3f79-f444-3835-bac2-187bbcaced54 | -3.38327 | -44.48907 | 2026-10-10 04:44:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83a01c36-343b-36cd-b208-6ef197bcff42 | -7.23079 | -44.18139 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d1ff958-34fd-319a-a623-88f8e8f7b8a4 | -5.76413 | -41.64054 | 2026-10-10 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 02d68edb-7f13-3a56-91c2-c802c6c0e2c3 | -3.57611 | -54.38129 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a95d8c8d-aae8-32e5-8ab1-94a81f5932cf | -3.57654 | -59.08325 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de8540b4-2ffd-305f-9a4c-c305d1ea3e4f | -3.93426 | -55.72545 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc0ef064-ecb5-37b1-8d60-371259a0436a | -4.29836 | -50.78431 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21a03864-550d-34c1-a873-7094787b08d8 | -3.58915 | -54.59819 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15a97c1e-058b-3cdb-b51c-5c95f24244ee | -3.03829 | -53.89275 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5ef58065-9bf0-349f-814b-fed771c40de9 | -3.22875 | -54.29736 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0838aebc-763e-399b-bf88-d2431ba9ff98 | -2.29929 | -48.54468 | 2026-10-10 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7da1c7ec-9bb5-31c6-ba29-f91cb8fc8688 | -4.63366 | -50.96163 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20ba2f87-dffe-3f1c-a875-469af2771895 | -2.40252 | -57.90126 | 2026-10-10 04:44:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 078aa997-5f4f-33c4-9346-889fcb138a61 | 0.49307 | -50.78349 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3c2ce0a8-2259-3045-affc-f6cccd6f2229 | -2.73596 | -54.11134 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bcb573c-7cbb-3b4c-81fb-667520fc9e36 | -2.461 | -56.05715 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5191a8c3-83ba-3aac-a2af-3af186ec3f74 | -4.40197 | -49.77739 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 394db6b9-0442-3bcd-af78-925dc60598f6 | -1.44902 | -54.4738 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14340df1-d918-301d-b671-27700fd67e60 | -3.42223 | -54.06633 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb3f26f4-239d-37b8-8902-18ae45c1bb2e | -4.58946 | -55.72572 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f47d458e-2017-30b4-93c0-8adf5b915b3a | -5.29569 | -37.32857 | 2026-10-10 04:44:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ddc02ff0-26ff-3765-9d7b-1fc8bc8413d3 | -5.2313 | -50.6852 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e723f434-6392-38ee-867f-5418a6bb865b | -2.79439 | -51.40553 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44859534-a11c-3f8b-b4d9-b4535682b4c6 | -3.46576 | -50.59496 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dc7c657-b0d5-3a62-99fc-5c3929f1f1d5 | -5.74379 | -45.13408 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c91d687c-e287-326d-aced-2525b1ad7181 | -5.79682 | -53.79482 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 513741fc-816a-32f8-b28b-8afc8ea5843a | -7.21359 | -44.3468 | 2026-10-10 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9515832-1193-3276-817e-698a40a6e4ca | -6.06499 | -46.29091 | 2026-10-10 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea61171b-a960-3014-8629-7001e16bdcee | -7.2383 | -44.18243 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 128c87fc-e503-32b0-ae80-42dd21c3660b | -3.17888 | -50.59842 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18cfe9a7-79a1-3d95-95c2-083b2782ef8d | -5.89342 | -43.27459 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f50b961-f674-3ff8-a830-53704cea6266 | -2.50295 | -56.20449 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49a1f85d-a5df-3f9f-a8eb-752011be83bf | -5.74779 | -45.13368 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a072630a-59dc-3b71-a72f-7948073c8d1a | -0.87515 | -48.71597 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bea760c8-0c17-3fa5-810d-7dc1ea3ee0e4 | -4.109 | -54.01786 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a35d601f-e10c-3ffe-8b1f-082cd0f8269d | -6.04247 | -46.41267 | 2026-10-10 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad0415fb-7a4a-3a66-bb50-469e388ba4f9 | -3.54683 | -54.73969 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f17e5e63-c2b2-3652-9a96-7f1f6ed529aa | -2.0457 | -56.38068 | 2026-10-10 04:44:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35e8757b-bb1c-3fd4-8d22-e2e7cc0177cd | -3.34395 | -50.41014 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb1a11d7-020d-36a1-be2d-ee1f2be1966e | -3.06392 | -51.13306 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 638dacb6-44bb-3134-be49-64a7dafd04a9 | -2.92701 | -54.08285 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17b4b022-0ed6-36bb-b140-775f8552931b | -2.826 | -51.28284 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2748d8db-40d7-38cc-867e-c7879dec8e39 | -2.54939 | -58.03251 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d21ccec-79e2-3478-8dd9-a9575deb5b41 | -3.18691 | -58.63861 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d249b3eb-6760-391f-97e7-f9c24baf7329 | -5.84462 | -44.92643 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab341554-3992-38a3-ba60-21560f2b62a4 | -0.91767 | -52.43652 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8893033-2988-3d50-8e03-976aebc0255b | -3.50231 | -49.9416 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b70d3ccf-9515-3dd7-b5d3-012b96f79eda | -3.31186 | -54.68023 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| af76fee0-04ed-342a-94cd-1ae1cec0511c | -2.39895 | -51.30299 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e41c378c-da71-3484-99da-3a7bff8cad52 | -0.97793 | -52.44627 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6daea5a2-999d-38de-bad2-0722d96ad507 | -5.93176 | -51.826 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 752a3f6c-24ee-3807-9d9b-847ede4e8184 | -3.21925 | -49.43804 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f1e5af3-abe7-3f8d-9b18-b77f78857480 | -1.72615 | -56.06362 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ff381b1-4232-3cf0-b002-4df756408ceb | -3.56397 | -53.00762 | 2026-10-10 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README57.md)
