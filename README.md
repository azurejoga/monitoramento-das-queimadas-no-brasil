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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b3f30cc-4b79-3cf7-b377-b15d956ea990 | -12.9169 | -49.467701 | 2026-02-08 00:18:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb8c5fb4-7400-366e-8ddc-27bed9711b7a | -18.163401 | -39.7659 | 2026-02-08 00:18:00 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bab5a71f-8044-3161-94ad-940f6efac314 | -12.9185 | -49.474701 | 2026-02-08 00:18:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3fe02c9c-f12d-3a9c-ba21-f547e74c818a | 3.0179 | -60.8423 | 2026-02-08 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 40.3 |
| e21d4a85-c6a5-3d03-b4c5-b056a3ed79c2 | 3.0178 | -60.8612 | 2026-02-08 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 2ae25a4e-2cac-3ed7-880a-a0c16bf9a9ba | 3.0179 | -60.8423 | 2026-02-08 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 37.4 |
| a6a60700-e67d-34f2-ac12-1ff2f5e04c53 | 3.16611 | -60.55037 | 2026-02-08 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b52e168b-4023-3dbc-a637-a1d0c0c1ca20 | 3.01515 | -60.84228 | 2026-02-08 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 96ac9ad9-bf2d-36f2-93dc-bc39e6a3a44b | 3.0493 | -60.86665 | 2026-02-08 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b686fb25-dbe0-3118-99b3-a0596a6a4d91 | 3.01384 | -60.85192 | 2026-02-08 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 6fc0235f-61ba-327b-b2e4-cb0595f737c3 | 3.0179 | -60.8423 | 2026-02-08 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 56fef57d-8c72-3147-8434-8d172fb01f65 | 2.9996 | -60.8426 | 2026-02-08 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 23648cb9-d69f-3543-ac29-5f6d06adf7e1 | 3.0179 | -60.8423 | 2026-02-08 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 1c3d0425-7ecd-398a-8f14-6d0e6034fe60 | -18.15644 | -39.79517 | 2026-02-08 02:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 6d3f02a7-6182-3ba8-837a-cd2ed83016c8 | -18.14952 | -39.79327 | 2026-02-08 02:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c092055d-fc82-302b-ba07-7a5840f3f1fd | -18.15482 | -39.80208 | 2026-02-08 02:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 14d8e0fd-979f-37ef-8135-cea1bd1c1dbb | -18.15257 | -39.80104 | 2026-02-08 02:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| a3b62857-b11a-3ec7-b74f-1901528c6b2a | -18.15423 | -39.79413 | 2026-02-08 02:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 29532add-175b-37bb-8ea6-6838767f3792 | -18.14789 | -39.80022 | 2026-02-08 02:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ea2d84ca-b552-3554-8263-aa9e305c17ee | -12.9145 | -49.477 | 2026-02-08 03:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 7c41af86-f1ac-31f7-bbba-29005b17510c | -12.67877 | -38.80052 | 2026-02-08 03:44:00 | NOAA-21 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5cacf64d-2048-334f-811c-e4539b167a77 | -10.5237 | -43.63829 | 2026-02-08 03:44:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b641c908-428b-3432-ab50-38aff7622a96 | -9.99632 | -36.29165 | 2026-02-08 03:44:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 983c2b8c-2f13-3bcf-8de6-41273825d275 | -12.05412 | -38.32233 | 2026-02-08 03:44:00 | NOAA-21 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c98a72eb-08d3-3497-a561-ae164f23a91c | -10.5246 | -43.63329 | 2026-02-08 03:44:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3644b365-5906-33e0-a272-82f014764293 | -12.0575 | -38.3229 | 2026-02-08 03:44:00 | NOAA-21 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9f11b50-b012-3586-8385-2b852e1cf7a2 | -10.1511 | -37.9181 | 2026-02-08 03:44:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f7017ded-b807-36a3-b24b-8c6bbd46949d | -10.15049 | -37.92179 | 2026-02-08 03:44:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a4d84d2-0947-3d88-94c0-5a9daa08f7d4 | -12.92181 | -49.47903 | 2026-02-08 03:46:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f98068f1-276f-3972-b8c8-384be0c637b9 | -15.5349 | -39.4594 | 2026-02-08 03:46:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a60605ae-57f6-344d-bdb5-456883994c66 | -17.88204 | -39.88036 | 2026-02-08 03:46:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 55cad861-3fd4-36b5-ab3a-aa5748f68f47 | -15.42586 | -41.43018 | 2026-02-08 03:46:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c9742b9f-c758-3186-a6dd-0a9e9b3ede8f | -15.42211 | -41.42954 | 2026-02-08 03:46:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 435dc8d0-0dc3-3cbb-b336-1599d007203c | -15.43858 | -39.12688 | 2026-02-08 03:46:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| baa0de4e-0064-33a7-b581-b0175afcbcb0 | -18.15577 | -39.79919 | 2026-02-08 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2a2d3d19-6ab5-3d6e-afa1-16ece6e0d459 | -18.28234 | -39.67294 | 2026-02-08 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 13dd3478-b7a1-35fe-99be-13008b0298f0 | -16.2891 | -40.77464 | 2026-02-08 03:46:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 08b73366-f07f-3b08-bdf7-53ecd114425d | -15.42538 | -41.42747 | 2026-02-08 03:46:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| e31c07f1-c508-3ed8-a087-18871cda5dc9 | -16.29268 | -40.77526 | 2026-02-08 03:46:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| a828ac32-4da4-3cd1-a8da-83f36c2db836 | -18.45169 | -39.75761 | 2026-02-08 03:46:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 61351197-5ce3-3ca5-aadc-9fe7bbe51cb1 | -12.91414 | -49.48335 | 2026-02-08 03:46:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 50e017ac-e388-3c63-861b-03b1ebf1d94f | -15.70939 | -40.82392 | 2026-02-08 03:46:00 | NOAA-21 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d66c8e6a-6180-3878-8716-984446c252ca | -15.42669 | -41.42548 | 2026-02-08 03:46:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ba053fbd-e923-34da-b372-a35e3c05792f | -17.69028 | -39.46375 | 2026-02-08 03:46:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f474e5e9-b859-36f9-9616-4160a0930b6e | -18.1564 | -39.79539 | 2026-02-08 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 0bc120a9-c9f1-3327-87d4-40db29b010fb | -12.92063 | -49.48461 | 2026-02-08 03:46:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09fecf2a-26a7-3985-b1d0-8a0d42ca9b04 | -18.15703 | -39.79158 | 2026-02-08 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 6821fb77-7ed0-37d7-8a64-895380d0e79a | -15.42456 | -41.43221 | 2026-02-08 03:46:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5fdecc9a-73fa-3d03-a169-4d2ad42b24ae | -18.15301 | -39.79478 | 2026-02-08 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| ede254b0-554d-333f-a51d-cae9ccd70cbe | -18.28572 | -39.67355 | 2026-02-08 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 571b8ee7-455e-3952-a944-8ef69b83a11f | -15.42831 | -41.43285 | 2026-02-08 03:46:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| acab1a71-ca6e-3dcd-b72d-dacac4372321 | -18.15978 | -39.796 | 2026-02-08 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 21b3387b-da25-3e2f-a659-63f10e71da3b | -12.91446 | -49.48249 | 2026-02-08 03:46:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7a5a7b85-c7ff-3306-990d-3f12388f891a | -15.24963 | -39.18337 | 2026-02-08 03:46:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 30b564fc-f76b-316a-9582-213660206af8 | -16.81243 | -39.68851 | 2026-02-08 03:46:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b783fa1-122d-31ad-bc94-0f29a45032ac | -18.15238 | -39.79858 | 2026-02-08 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 929cc6c7-d3b0-3a80-9308-bc394911dcba | -15.4296 | -41.43083 | 2026-02-08 03:46:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1eb6811f-bfe7-39fd-9398-b7c24b8f48d0 | -16.43144 | -40.87247 | 2026-02-08 03:46:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3af929cb-4d37-364f-9d34-05a340de2f02 | -18.15365 | -39.79097 | 2026-02-08 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| a368441c-1968-3583-953d-7e4126161b26 | -15.42295 | -41.4248 | 2026-02-08 03:46:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b4794977-7b50-3c18-b5aa-44da54118256 | -21.88696 | -41.65132 | 2026-02-08 03:49:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3b4c7c01-9c6a-3971-bd1a-db0ec56fd644 | -18.97481 | -52.93309 | 2026-02-08 03:49:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 63949dd3-f79f-3666-b1fe-980db0285434 | -30.29451 | -50.92264 | 2026-02-08 03:51:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| e4d0035c-3aaa-33aa-adda-7fea88067fe3 | -30.29529 | -50.91935 | 2026-02-08 03:51:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 89cf3c1f-570a-3b0f-87aa-e89807c2bbcd | -11.96695 | -37.71322 | 2026-02-08 04:14:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b201c0c-3689-3453-9fe2-e1527a410103 | -11.96736 | -37.71378 | 2026-02-08 04:14:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b7e139a7-3503-3f6b-b4fa-91bad307769f | -18.15446 | -39.79461 | 2026-02-08 04:16:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 4aac0b0a-18ad-36bc-a3e2-16b7117bba15 | -18.45379 | -39.75869 | 2026-02-08 04:16:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c63b9bb6-6bc9-360a-9c30-0672b38ec8d0 | -15.42564 | -41.42829 | 2026-02-08 04:16:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 22cea6f1-af5b-3d85-9094-767751cf8029 | -18.15513 | -39.7895 | 2026-02-08 04:16:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9b7fccc4-6fbf-308a-b8ce-3bb5609ef8d6 | -16.43033 | -40.87004 | 2026-02-08 04:16:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 744e5817-62d0-370e-b03c-1f264799c8ac | -18.15836 | -39.79518 | 2026-02-08 04:16:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f1cddc15-3b24-3045-aeb8-04e8e920f6fb | -15.42216 | -41.42772 | 2026-02-08 04:16:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b2a2d107-43bb-3ea9-84d4-5445a7be65a5 | -16.29212 | -40.7756 | 2026-02-08 04:16:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 509a766f-573f-3ed8-8de4-c8b646213d81 | -15.42507 | -41.43221 | 2026-02-08 04:16:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ef1f8052-950e-39c2-bbd3-c447dbee7318 | -16.28851 | -40.77502 | 2026-02-08 04:16:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 1573ae29-5654-3644-8d9a-c0ac6199fe5d | -16.29573 | -40.77618 | 2026-02-08 04:16:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| aa86f219-0109-3064-9c6d-40480e6d48e1 | -18.44986 | -39.75812 | 2026-02-08 04:16:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 10788bb1-660d-311c-8420-49e1f45e17b6 | -18.15378 | -39.79971 | 2026-02-08 04:16:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 1fa01d31-c263-3b77-9735-986e5584bb28 | -13.65438 | -39.00899 | 2026-02-08 04:16:00 | NPP-375D | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a7b0ff1c-e79c-3abf-8baf-c126cbca30b5 | -17.47321 | -41.10957 | 2026-02-08 04:16:00 | NPP-375D | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b14be7f2-94fe-3e28-acc5-4aea7b6a8de7 | -15.42912 | -41.42885 | 2026-02-08 04:16:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| efddfc01-c110-3a88-9541-5004de1f283c | -22.68495 | -50.47319 | 2026-02-08 04:18:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7f323f5-a293-3039-a7c5-f2efd7bad572 | -22.83409 | -50.2859 | 2026-02-08 04:18:00 | NPP-375D | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 262ba6b7-4d69-30da-a2da-701d2f62c617 | -22.68558 | -50.47654 | 2026-02-08 04:18:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 912bc333-c135-3b99-8e3b-9b3cac299f83 | -25.36157 | -53.57892 | 2026-02-08 04:21:00 | NPP-375D | SANTA LÚCIA | PARANÁ | Brasil | 4123824 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 91ea2317-94e8-3e68-82dc-fab029b2cc85 | -10.52168 | -43.63462 | 2026-02-08 04:33:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ff97cf1-5e7e-304d-aba3-6711e331a7c0 | -10.52525 | -43.63896 | 2026-02-08 04:33:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90824f7c-f026-3e4d-8ba9-5b8d1664889f | -16.29139 | -40.77748 | 2026-02-08 04:36:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 888ef8e6-c9f0-3135-94a9-5175418d7093 | -12.91188 | -49.48182 | 2026-02-08 04:36:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1662f462-cd26-3d4d-8cd1-a56cc90ce6db | -11.28548 | -49.26357 | 2026-02-08 04:36:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf33022b-455b-3e26-af8f-682e1ce608c7 | -12.91575 | -49.47884 | 2026-02-08 04:36:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8427ffe-ca7d-3386-96b2-314a1e6c12d1 | -15.42369 | -41.43135 | 2026-02-08 04:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 868ad11b-8430-3aca-a7af-68cbd369064a | -12.91906 | -49.47939 | 2026-02-08 04:36:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66ff382d-5041-3fe5-833a-cacfd3f53221 | -16.29174 | -40.77428 | 2026-02-08 04:36:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 850e0e3d-9c57-3137-8afb-ec41d3aff61c | -15.42439 | -41.42538 | 2026-02-08 04:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 73d1e09f-e204-3fb2-80de-2e1948957e47 | -10.1598 | -49.18452 | 2026-02-08 04:36:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99f272c1-ec0a-324f-970b-083b33d17249 | -16.29407 | -40.77737 | 2026-02-08 04:36:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f6c69e28-5c73-3021-a24e-da79f80195bb | -10.76836 | -45.0136 | 2026-02-08 04:36:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cce0e253-c41d-300f-919d-de318cb04205 | -12.9185 | -49.48291 | 2026-02-08 04:36:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README2.md)
