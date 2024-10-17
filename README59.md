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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9064454e-cd66-37f5-8a61-db10d6060780 | -11.70509 | -65.23379 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28fb094d-f0e1-3242-826d-6060b3cc1831 | -11.70438 | -65.2387 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80a22736-612a-386c-ad54-8f8b1a1e8b51 | -11.70367 | -65.24361 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d81956b3-f968-3e19-9c55-5b3b3fc69fbb | -11.69981 | -65.24305 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9a60f04-9fe8-3ab8-963c-d55f21ddbf25 | -11.69594 | -65.24249 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55f9d351-beb2-3aa6-be73-05414056c79f | -11.69208 | -65.24191 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7d7a76d-09f7-3f84-83c5-cb6389d77022 | -11.49683 | -65.12387 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29616bd3-5686-3b96-932d-15e316954fc5 | -11.49295 | -65.12332 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 243cd566-ca08-3c5e-a82c-d123f222f030 | -11.48906 | -65.12276 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0e52375-e075-32bd-91fc-0d27a8ee5fa3 | -11.48518 | -65.1222 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c35539b-1970-3304-b657-d5a6f1ce1269 | -11.48412 | -65.1018 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| baf867e5-b63f-382b-88c2-76d15199ef14 | -11.48341 | -65.10676 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e011a419-dbd5-366b-a536-757a64543d82 | -11.48271 | -65.11172 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38e1664e-ab5c-3493-9924-bdb28d94b9df | -11.482 | -65.11668 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b7a2b5-c1dc-3d24-87b0-d032af44fd2c | -11.48129 | -65.12164 | 2024-10-17 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f46acec6-6549-31a0-b0d6-56da52c86f1e | -7.78852 | -70.06223 | 2024-10-17 05:53:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e98457df-805b-3af9-b710-b18e3ff46492 | -7.75775 | -70.06094 | 2024-10-17 05:53:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c965a8f-8a80-3a70-95c9-6cdfc730df72 | -9.10382 | -69.86929 | 2024-10-17 05:53:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f435b64-424c-361c-ae7e-f44f5c4bd671 | -8.62094 | -69.9763 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f68ab2d-a5d2-33d9-a69c-7f7f27087338 | -8.61761 | -69.97578 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 277385cb-cb30-3f1d-94ef-819ae7dc2c67 | -8.61517 | -70.03355 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22b7db33-f7be-3db9-bb29-fad891f62040 | -8.6146 | -70.0371 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcbc9903-acbe-3496-a1f4-31df3c70f791 | -8.58162 | -69.94796 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6f667c1-ef8c-3a7d-ae47-1f92bae1dad6 | -8.57772 | -69.95097 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d87bd70a-f53f-34bd-a520-4a7ce5d8fd14 | -8.56777 | -69.92758 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23171920-a651-3976-b0ca-c097a63434d1 | -8.55508 | -70.09296 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c77c02a-6e02-33e1-9a2c-77306dafa69d | -8.54148 | -69.98507 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c23d28cb-57dc-3fe1-8bf0-1e79c70ad50d | -8.50664 | -70.07416 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d62ea07d-cf7e-3434-b78c-2a21f46a2bf0 | -8.14076 | -70.19187 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef0bff36-73f7-3e35-bfcf-8157a8cee5ae | -8.1388 | -70.19141 | 2024-10-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c91f2356-5891-3f91-8df7-73c0f160d716 | -9.39766 | -68.93299 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 204ab024-22d2-365a-beff-b43a9cc5ce04 | -9.39609 | -68.98624 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f242d9a9-08cd-32d0-b26a-4c0d04c7fc25 | -9.39555 | -68.98972 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbc1eebd-5bfa-3a6a-9298-d80d175e453d | -9.39333 | -68.98224 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abb544db-87ca-361e-a7b0-b5051bff5fd0 | -9.39279 | -68.98572 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2211827-2873-35d7-82e0-ee19164c8ddb | -9.39224 | -68.9892 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da0c00be-881b-3441-a4f7-f80f545ed059 | -9.20594 | -68.92067 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95dab75d-65fd-317d-bb58-3f076a4f60e2 | -9.04704 | -68.87405 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd06db30-0739-32ed-bf1a-84c8ed0ba7c7 | -9.02054 | -69.21536 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 388ec43c-f0df-3eeb-aaa8-68b9fd329a2b | -9.01433 | -69.08257 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ba86e60-ccd7-363c-912c-46070319bea4 | -8.87658 | -69.43809 | 2024-10-17 05:53:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 119764d5-7349-37c3-8616-cd5e947cdcca | -8.76181 | -69.45546 | 2024-10-17 05:53:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0e5e087-f254-3265-933d-d3165b056e45 | -8.7491 | -69.34276 | 2024-10-17 05:53:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a91e016-ba85-397d-91d0-9626a0fd3d78 | -9.50339 | -70.45566 | 2024-10-17 05:53:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1c336b7-ffb9-386a-8a82-0af6c0d3d5b2 | -9.50004 | -70.45511 | 2024-10-17 05:53:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ccdeb3e-9cae-31bb-8119-6ffc24d5e855 | -9.4077 | -70.45116 | 2024-10-17 05:53:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e14f5c7-fcbd-3913-a212-c5f21edd4d82 | -9.57945 | -68.98711 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e101e8e2-861f-3575-a6b1-1e084e942f4a | -10.73832 | -69.24395 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3472fe5e-ca32-39e5-b9b4-aac1f0520e92 | -10.61734 | -69.19209 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 795f3b2e-9d7c-3f39-b5c5-e54a273b6199 | -10.61403 | -69.19155 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91c57514-9a4f-36d1-85d9-dcf85fbdb8ab | -10.58876 | -69.24474 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 272e6a27-49eb-38eb-9a13-c4f42584ddf0 | -10.58545 | -69.24422 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18e2f4cf-191c-3c19-b2eb-e435e709ec1d | -10.58327 | -69.25819 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db10b43e-4ce1-33b2-b84a-b28822be9d56 | -10.55113 | -69.22444 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d53b63c-73c5-3be3-be7a-921d50a1cf67 | -10.52794 | -69.19933 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 726ce2b7-1b00-3261-a05b-f272c918d766 | -10.52464 | -69.1988 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ca9f23a-a73f-33df-8258-6bc8554f61d1 | -10.48617 | -69.27134 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12659d9f-78fe-3c16-be84-e9646b8cbcd2 | -10.47898 | -69.2523 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c32e7b4-7659-3018-9a6c-fe35360787bc | -10.47068 | -69.21874 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8031ee2a-3140-326a-be2e-af7119ea886c | -10.46707 | -69.19641 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54dfc163-dab3-383c-82ae-8870674c9bf6 | -10.45655 | -69.17691 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34ca1d19-411d-3852-b25f-dbc2c5d82abc | -10.44454 | -69.25366 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9d41a06e-d9b2-3536-9ae5-c2b01c5ecec3 | -10.41079 | -69.14455 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c53ca16-7978-37f0-83cf-543809c628ad | -10.39484 | -69.1599 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99966a50-f551-3e90-bf7e-7bd6b684d041 | -10.39429 | -69.16339 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df87ac2f-1085-383d-865c-3ad1b263e056 | -10.39374 | -69.16688 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 952266a1-1224-3721-8d19-d6cde4995f29 | -10.39098 | -69.16286 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b5064f-4a19-3667-ab9d-49ce4bd4499c | -10.39044 | -69.16635 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 977514e4-aec2-3a65-a6bb-f380efeec482 | -10.37347 | -69.25304 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7eb2a13-85d9-3b9e-8707-27f8eaf3dbca | -10.18982 | -69.10246 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d5b7194-02aa-3c33-b596-e8dfebec8da9 | -10.18705 | -69.09844 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01b9e7c8-5b17-3122-bc57-9fda7dc1ea1b | -10.18651 | -69.10193 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe8649c6-cce2-34da-a0c5-87f67065e4f8 | -10.12089 | -69.17368 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b60db55-24b8-3a08-9bef-eeba1af5976f | -10.11758 | -69.17315 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15a26190-518e-3137-8469-e50d4fbef933 | -9.96515 | -69.10564 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbea8635-2f62-32d5-8aa9-bf47009decb8 | -9.67122 | -69.00917 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90c669e7-46c5-3cf5-a9a6-8b90c14229ba | -10.11482 | -69.16914 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5dddd2f-cb0c-36bd-9782-279b1c3843f8 | -10.11427 | -69.17262 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9b33153-3449-3bf8-9da4-e1a58af5c072 | -10.11151 | -69.16861 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62d51221-cd6b-3d66-bd74-c17307a57601 | -10.00476 | -69.06905 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b5d5d6-1fe0-3d9a-a2b4-757dd99e0730 | -10.00422 | -69.07254 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eed0ec22-9ee5-3796-b5e3-7119d63c2296 | -10.00091 | -69.07201 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b019186c-a966-331e-a729-25f283ba9d2b | -10.91865 | -69.45874 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f20f155c-8206-34d6-b82c-fe25d697c2bf | -10.89279 | -69.55852 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59fac9bd-f4a6-36d3-9801-a541ee2b28e8 | -10.84401 | -69.47874 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b4001a1-a129-3f7e-ba63-b30b267b6d0b | -10.81207 | -69.53093 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebef3ae8-bb58-3ea8-9a65-e10d574a0720 | -10.81153 | -69.53442 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b424807-0203-361f-8a80-18e60bda5611 | -10.79938 | -69.48232 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9926c6c0-3b7a-3b70-aea1-38a3aeabfdd0 | -10.72475 | -69.46022 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 243f89b4-8654-3bbe-8a16-5b0a30024ae7 | -10.71151 | -69.43661 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1831e738-f23e-3ec5-9307-e961303a6960 | -10.70987 | -69.44708 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07c03522-b9e5-3115-abcd-5f26fed137b0 | -10.70932 | -69.45057 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b2cee1d-794a-3ee1-9da3-108861ac07fa | -10.70105 | -69.43851 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6082433c-2cb6-39b4-b65f-757fc9b01f5e | -10.69774 | -69.43797 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e32611cb-0051-30d5-8b08-da57a179c2ce | -10.6785 | -69.51724 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15cd4e4c-2613-30a2-aaec-bde093829bf3 | -10.67519 | -69.51671 | 2024-10-17 05:53:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a67842a-0452-334d-9449-52572576cc31 | -10.6317 | -69.59917 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9ac0e85-4443-3266-82da-595edc0e5c12 | -10.47974 | -69.69983 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dd45188-ed02-396c-af22-f8482020c07d | -10.47091 | -69.73427 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc1b5bea-f0f5-3b1c-99f1-d7ae3e005b8f | -10.45658 | -69.71761 | 2024-10-17 05:53:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README60.md)
