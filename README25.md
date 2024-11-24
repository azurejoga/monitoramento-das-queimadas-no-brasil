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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98506b45-ba43-3669-b4d0-6e0966f4b4d8 | -4.55184 | -44.01827 | 2024-11-24 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 20910597-944e-303e-9b14-ea790c85ef69 | -8.07453 | -34.97743 | 2024-11-24 03:34:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ef5f53dd-63a6-3bf0-a383-3ff8b32c8514 | -1.42127 | -46.06427 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9e74a5c-5b1e-32b2-a246-d5535300dcac | -7.14062 | -38.70634 | 2024-11-24 03:34:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9fa8ffc8-6fc2-3857-81e2-f298f0b400ce | -5.11024 | -43.15198 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75c72ba7-96c8-35a2-8b89-125a0bb7de5b | -4.52938 | -46.42773 | 2024-11-24 03:34:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fe4e6765-1922-3f00-8644-e8298b49dae1 | -4.53734 | -42.91406 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6763726-46d0-33ee-a4c5-684826bc3043 | -4.55339 | -44.01511 | 2024-11-24 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c804a39-092e-38bf-a971-c755bcd3c186 | -4.69718 | -45.70051 | 2024-11-24 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dc2a3a0-b0c5-3ab0-8669-d68ec7bc1eeb | -4.86762 | -38.38301 | 2024-11-24 03:34:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93c38a42-4fb4-3973-b9cf-3cd8984772cc | -1.47167 | -46.04203 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b320bb4c-311f-3e9c-8122-495e874559ad | -4.54062 | -42.91123 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c01a7d8e-cb36-3ef7-b6e6-735298bd35a8 | -4.53858 | -42.90664 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 123c5bfc-5df6-3733-a998-1a1c19fc5bc5 | -2.86821 | -45.83835 | 2024-11-24 03:34:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 29c87e1d-84f9-3e53-9b6e-806aae92c4c0 | -2.22061 | -46.38865 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| cf44425f-c22d-3fa8-9c3d-3c779ae3ce57 | -3.8499 | -44.05048 | 2024-11-24 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ba52025-183b-368a-a143-a7affd55f0c1 | -6.05857 | -44.04454 | 2024-11-24 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37f4c8ab-0536-3b82-bf2f-0ef8c9b9349d | -6.91954 | -39.47841 | 2024-11-24 03:34:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d71ba5f7-78b9-30e7-8127-6becb1504ca9 | -4.53565 | -42.90662 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ba2b492-2e94-348c-8a3d-3d1920bd897e | -1.42955 | -46.05844 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 989856a2-e92e-323c-ae27-d2f0ffa20552 | -3.84912 | -44.05504 | 2024-11-24 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3193d97-4472-36ae-98da-2f40e022023e | -4.53921 | -42.90293 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5b4a5f4-7c0f-30cb-a3ff-1e14fe4313f3 | -2.10422 | -46.26527 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 879e1e99-fdc8-38e7-b490-c263d3b1bb3c | -5.10523 | -43.14726 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 62a33855-2d23-37c6-8513-282f758f3b6a | -7.39689 | -34.82902 | 2024-11-24 03:34:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 52e905e5-158e-3c01-859b-b55b90cab010 | -3.16986 | -45.30491 | 2024-11-24 03:34:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 04654950-bb63-33e3-affa-d33d76d4480f | -7.90178 | -36.02462 | 2024-11-24 03:34:00 | NPP-375D | TAQUARITINGA DO NORTE | PERNAMBUCO | Brasil | 2615003 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fdc1ba45-68e2-3ca0-81d6-d46e87abaacd | -5.93136 | -39.47182 | 2024-11-24 03:34:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bab65a1d-4a28-3f2d-a488-aaae16fde3ce | -3.17471 | -45.29739 | 2024-11-24 03:34:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 656b38a7-1e49-3e3a-8980-64eb933d7a32 | -1.42839 | -46.0655 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f38b779-f22e-3642-9c70-ac1685713524 | -3.13045 | -45.37568 | 2024-11-24 03:34:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad2bcbf5-2434-301f-b325-c3e31c4ccfbf | -3.07423 | -40.06637 | 2024-11-24 03:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 872028c8-bbac-30a5-92db-c9d0108736d1 | -4.86982 | -38.38366 | 2024-11-24 03:34:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5d9231ad-8f8c-3758-a867-ba79244463c7 | -2.86926 | -45.83207 | 2024-11-24 03:34:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 5368de6a-34a3-3635-95da-800e24e37c7e | -3.77456 | -44.0496 | 2024-11-24 03:34:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 320d368d-def2-3f45-9c6b-77e023f41017 | -2.86907 | -45.83248 | 2024-11-24 03:34:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 18bd354d-20e9-3e8e-a3ad-f1762dfd788f | -4.35594 | -45.27714 | 2024-11-24 03:34:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 09d09602-3f17-31da-b67d-a8bb38ec78de | -4.53236 | -42.90929 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21cc8255-a097-305a-bf03-0e74940fce2f | -6.0437 | -44.04049 | 2024-11-24 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d977eaca-2ede-35db-925f-e4cf11c249ba | -6.05701 | -44.05316 | 2024-11-24 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81679145-848f-399c-8c0f-2b07dd5e3694 | -4.52739 | -42.90451 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38f6ec30-9e53-3c04-b8c7-7c1dd4672d9f | -5.06818 | -43.69815 | 2024-11-24 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac8fc636-5055-37fa-a441-738c21cb484b | -3.57647 | -41.95449 | 2024-11-24 03:34:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7ba50aee-63c5-362b-9af9-ff31cb0b5447 | -3.79267 | -40.99947 | 2024-11-24 03:34:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 089dbf8f-f3d3-3130-837e-5454c37eb619 | -3.10377 | -45.78201 | 2024-11-24 03:34:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a70edd6b-1728-33a2-bb36-2dd55c564577 | -5.93066 | -39.47598 | 2024-11-24 03:34:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c709bb9e-c0ae-3f40-af03-88ce40939bf4 | -4.53435 | -42.914 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47bbb255-1e89-3018-90c3-e6a1c3a4772c | -1.42415 | -46.06306 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab5f3b04-8c93-3e52-9632-7941bc93a6e8 | -4.23006 | -44.63155 | 2024-11-24 03:34:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4f5a934-c9fa-3d1e-97ea-5a71e434df96 | -1.95494 | -46.43835 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d95b7a3-b68a-3a54-9539-36da70059538 | -3.47002 | -43.88718 | 2024-11-24 03:34:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| df373aab-ecc8-3aaf-b8f0-197d2596f3c4 | -5.85329 | -40.80016 | 2024-11-24 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 939f7a90-daa3-372f-a81d-cecc9e01fd4b | -2.09708 | -46.26402 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0be08863-02d4-34ce-a52f-42c83d404fd3 | -5.06233 | -43.69709 | 2024-11-24 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2a15407-5193-3c1f-9c05-61788d67b18d | -4.52677 | -42.9082 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c63365e2-03d2-3d91-8f05-0030f39b38b7 | -6.83565 | -39.18229 | 2024-11-24 03:34:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 32fbf4d2-315a-3a37-bfb7-ba1cd5d6687d | -4.53629 | -42.90295 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99cc93af-6d30-3b88-ba03-474d5e91094b | -7.90526 | -36.02513 | 2024-11-24 03:34:00 | NPP-375D | TAQUARITINGA DO NORTE | PERNAMBUCO | Brasil | 2615003 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1bd86565-3a51-38ab-aad8-dc37dd2ae9e7 | -5.61019 | -46.28943 | 2024-11-24 03:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7f5b148d-2024-33e9-bdcb-4b8251a430f3 | -5.10459 | -43.151 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d48fd8dd-e087-3c9d-9fe0-abce0f2b1267 | -7.32635 | -35.32919 | 2024-11-24 03:34:00 | NPP-375D | ITABAIANA | PARAÍBA | Brasil | 2506905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1d602072-8a72-3955-b8d4-c474864f56e8 | -4.53139 | -46.42944 | 2024-11-24 03:34:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2857f924-1d04-314f-8560-4bd23eb0d664 | -4.19891 | -45.36363 | 2024-11-24 03:34:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c073c9c9-eeeb-3593-bbee-b9e2646a4ff3 | -5.69063 | -38.04197 | 2024-11-24 03:34:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7c21bf6a-4f33-367b-81d1-fc69475a254a | -4.53671 | -42.91779 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e57162c-c9c9-3a6a-a84a-792fa2c65cdb | -7.14465 | -38.70714 | 2024-11-24 03:34:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 689880d5-451f-37b2-825b-15053aefc4b9 | -4.5142 | -45.80562 | 2024-11-24 03:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0278c094-bce8-3301-bcbf-7c0e8c3d3859 | -4.51475 | -45.72465 | 2024-11-24 03:34:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 57bbb47b-08b1-3571-828b-efb48c50d7e1 | -7.34725 | -38.91289 | 2024-11-24 03:34:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15ae607e-a720-3f6a-aedf-ba9c0aefe854 | -7.3956 | -34.82922 | 2024-11-24 03:34:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 335d206b-93dc-3fe4-be6a-46877543ea07 | -4.93259 | -44.07281 | 2024-11-24 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b23970f2-8774-34b6-8a90-098adf8e0c2f | -4.9386 | -44.07383 | 2024-11-24 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ff26ccd-363a-313e-944e-1cc38f89e900 | -3.95712 | -45.99712 | 2024-11-24 03:34:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 08212545-d6a4-3e71-a1e0-1ca23fdbd507 | -1.79459 | -45.71394 | 2024-11-24 03:34:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6876c17e-1938-3693-acdf-2133de59b12d | -3.58235 | -41.95223 | 2024-11-24 03:34:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 62d797a9-6d86-320d-988a-4c741931b5f1 | -3.76767 | -44.05311 | 2024-11-24 03:34:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63062b2b-221f-3757-8cc2-b15c7b15bd1d | -2.21343 | -46.38743 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4e317ea-a241-3441-9930-a6486fffb295 | -4.49522 | -37.86097 | 2024-11-24 03:34:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 13f1fb15-3a13-321e-9517-bb34ce83bffc | -5.1033 | -43.15846 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d968c63a-6db6-354e-93b9-38042a0ad88e | -6.31547 | -35.20671 | 2024-11-24 03:34:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ba056f87-37c3-32ad-a16d-d96c1c4a642d | -4.49922 | -37.86162 | 2024-11-24 03:34:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 19846c70-c05c-3085-a9fb-8c5cc1247cab | -3.17083 | -45.29914 | 2024-11-24 03:34:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9c43271f-5acf-3490-8697-0d7418c20919 | -4.54127 | -42.90752 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 484deec2-6f34-3a7f-8793-058538049118 | -3.16706 | -45.30189 | 2024-11-24 03:34:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1345d78c-ba32-3864-8315-b77cba497af9 | -3.89747 | -38.53733 | 2024-11-24 03:34:00 | NPP-375D | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| df0528a7-3b40-34ab-863d-185d231d60ff | -5.11088 | -43.14826 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a03c5771-43dd-34c0-8bae-47d779c99acf | -3.84375 | -44.0497 | 2024-11-24 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e063610-183a-3de6-9fb2-95f608dc9958 | -4.20102 | -45.36274 | 2024-11-24 03:34:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d42d6909-8840-3ca5-b202-6beff1d3b46a | -5.85279 | -40.80185 | 2024-11-24 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 90b30353-3abf-3d29-a5a0-02219752cf05 | -5.60913 | -46.29525 | 2024-11-24 03:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 243e3df9-015f-3536-aaa2-c73fca17ce49 | -4.19168 | -42.96979 | 2024-11-24 03:34:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4956fa7-e435-3a24-a67f-6ff3b83f38b5 | -4.54626 | -42.91203 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35a1f5fa-307c-3524-a7e9-70dc55cc7a2b | -3.79308 | -40.99426 | 2024-11-24 03:34:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4c81e99-8cf5-3e01-9d4e-9f297a6a7492 | -1.46152 | -46.04195 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a40186b3-4bcf-30b4-83a9-d904251eddc9 | -3.95141 | -45.98943 | 2024-11-24 03:34:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 45ae3e24-2f21-3f53-952c-e4a8ce09bc3a | -4.53996 | -42.91497 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cb64ea8-99eb-34f9-b55e-09d339118ad3 | -4.53796 | -42.91034 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43b20c7c-9949-3d0e-b011-846b0e8bb264 | -7.64344 | -37.99432 | 2024-11-24 03:34:00 | NPP-375D | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6e90b422-431d-3039-aadb-c5552a5d05cd | -7.39617 | -34.82563 | 2024-11-24 03:34:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f0f1f5d3-ccd2-3b5a-a685-6300de1a2f79 | -5.84795 | -40.80151 | 2024-11-24 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README26.md)
