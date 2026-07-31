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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f7fd9c8-d4f7-3fdf-9cd3-6283baa1bbad | -3.96185 | -43.1076 | 2026-07-31 11:38:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 179fe710-6b64-3e0e-9aa3-62c1da73a248 | -3.24253 | -41.79763 | 2026-07-31 11:38:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| c8211196-6734-3cfd-8eaf-889d1020d8b2 | -4.91691 | -43.46284 | 2026-07-31 11:38:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f7994731-5a4c-387b-8af4-1491f7d8436c | -6.27345 | -41.85239 | 2026-07-31 11:38:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f735f915-e9a1-3b07-b178-0cd504977c7f | -12.5989 | -44.6381 | 2026-07-31 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1a4839d3-169b-3007-b867-815129a283ed | -12.6186 | -44.6116 | 2026-07-31 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| d70f1398-a999-3aa1-9f43-6d004f821cde | -10.7464 | -40.26766 | 2026-07-31 11:40:00 | TERRA_M-M | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| e73a8deb-a739-38dc-b3c1-d2acd4f8e853 | -8.66746 | -39.43251 | 2026-07-31 11:40:00 | TERRA_M-M | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 8dbf7b0c-58f3-3e80-b809-aeef21d67420 | -7.73309 | -44.41508 | 2026-07-31 11:40:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 63161350-0828-33b5-8a8b-f3e0cd70e275 | -8.02076 | -44.14563 | 2026-07-31 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8abcfbc7-b208-3549-8419-70986b02a6c2 | -9.3598 | -47.99062 | 2026-07-31 11:40:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 258f0434-6d49-37bb-a821-8a5c79c7bce8 | -8.90087 | -41.233 | 2026-07-31 11:40:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 21d14ed4-8936-3c83-8279-7df84e7a5692 | -8.01949 | -44.15465 | 2026-07-31 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 81866f6b-f485-3e8d-abf1-55fab2e832be | -9.55274 | -40.65132 | 2026-07-31 11:40:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 138e676c-c382-370c-a426-b74a81d73ea7 | -9.21285 | -40.35111 | 2026-07-31 11:40:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 13691718-1926-328d-b2fb-dab5c9500d15 | -9.21352 | -40.34213 | 2026-07-31 11:40:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 7fde084d-7f98-3cf4-b205-2d99a403179c | -8.95842 | -45.66335 | 2026-07-31 11:40:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c4590c7d-a841-387f-a223-e17a83202234 | -8.98417 | -46.62033 | 2026-07-31 11:40:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 14b018a1-83ed-3135-90ee-a8033f114949 | -8.97513 | -46.619 | 2026-07-31 11:40:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| bdb23d46-0d98-3dd6-9d20-ccf901703d93 | -9.55457 | -40.63682 | 2026-07-31 11:40:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 75ce7263-fe02-337c-9c27-5c62c3afc7cb | -8.97376 | -46.6284 | 2026-07-31 11:40:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 67cb0de7-1560-3fcc-8ff0-b94c7518e050 | -9.55233 | -40.64476 | 2026-07-31 11:40:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 7c1ea996-869b-32f1-92b2-e92eae2cf647 | -12.61607 | -44.63146 | 2026-07-31 11:42:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aff961a6-f9ab-3bbd-a506-c51754ce6e9b | -12.61994 | -44.60317 | 2026-07-31 11:42:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a1933092-9ee4-3ca5-bda5-c03e7677fd61 | -15.22877 | -43.80042 | 2026-07-31 11:42:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b5cba02d-3256-3afa-8425-80e4b841691e | -14.07826 | -46.23133 | 2026-07-31 11:42:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a992b9fa-abf2-3b70-946b-eb8367cb8b94 | -12.58836 | -44.63115 | 2026-07-31 11:42:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 441c5269-6922-3543-b506-fc270d0cab69 | -14.40005 | -48.0682 | 2026-07-31 11:42:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d114b8b6-300b-3b6d-801b-1ed894beed1d | -12.58966 | -44.62177 | 2026-07-31 11:42:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1c7c9f8e-85f9-36bc-b67f-58f82829ae5b | -14.19644 | -44.10937 | 2026-07-31 11:42:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 525e84cb-dce0-38c9-973b-387669bc83d2 | -14.07955 | -46.22231 | 2026-07-31 11:42:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a770797-cabd-3da9-90bb-02d7487c462b | -14.20581 | -44.11065 | 2026-07-31 11:42:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 7d9d355a-5ce8-3dc9-a332-c7244eb1f806 | -14.20719 | -44.10038 | 2026-07-31 11:42:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8bdd986d-61f1-3fad-a0e6-77d34be46af8 | -18.63579 | -40.47515 | 2026-07-31 11:42:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 04368cf4-0cb9-35da-962a-02bba885e5b9 | -11.9386 | -43.43856 | 2026-07-31 11:42:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 175f2f2b-a6ea-3214-99ec-caf023baaefe | -16.29648 | -45.65593 | 2026-07-31 11:42:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 895adb7a-5f03-369e-9aa8-73bb8955c502 | -17.05486 | -45.02419 | 2026-07-31 11:42:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 88209fa9-f1ed-306c-9703-7f42a5b1f864 | -12.6109 | -44.60193 | 2026-07-31 11:42:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 7ddf30a2-1e89-3a1b-93d6-20ed01e8c589 | -12.60962 | -44.61135 | 2026-07-31 11:42:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 0465780e-3966-3fe6-8576-d90cf119548b | -17.58526 | -46.51894 | 2026-07-31 11:42:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 22e6156f-6cdb-38ff-91fb-69505dfa6603 | -19.42795 | -41.47231 | 2026-07-31 11:42:00 | TERRA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 4dca27c5-4f95-3e3f-9ae0-d11305cac5f7 | -17.05351 | -45.03421 | 2026-07-31 11:42:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 6241caff-e7b2-3b90-9a21-74e466297843 | -14.35742 | -48.04084 | 2026-07-31 11:42:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 073fda35-bd96-3076-8e0d-703d1012e60f | -12.79737 | -47.17614 | 2026-07-31 11:42:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 79354396-5707-3dec-a06b-8cb7feba26c8 | -14.92422 | -50.39801 | 2026-07-31 11:42:00 | TERRA_M-M | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7f3948c1-d48d-3377-b559-3eeb060a6487 | -12.20539 | -45.26262 | 2026-07-31 11:42:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cbcba1ee-63bf-39cb-bc97-0f37547bc269 | -16.80389 | -49.20426 | 2026-07-31 11:42:00 | TERRA_M-M | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b4df6626-e7ff-3cc6-9c56-114cec45385f | -16.88727 | -45.2374 | 2026-07-31 11:42:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 92dda1d1-acf0-380b-ae14-e1184f71e8af | -19.65354 | -41.17997 | 2026-07-31 11:42:00 | TERRA_M-M | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 5906499c-1655-3bab-a8b0-aa13c6f274b2 | -17.60556 | -44.59905 | 2026-07-31 11:42:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ba5ead53-db98-391b-a07c-c9be4c777c25 | -18.90815 | -46.07906 | 2026-07-31 11:42:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af9d8e86-35a7-3110-a2a9-7d065b25f23f | -13.7466 | -51.87837 | 2026-07-31 11:42:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4e7a6c64-3e90-3eca-a04d-4a484d584208 | -13.94896 | -46.03412 | 2026-07-31 11:42:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 93870c69-aa85-3a85-b617-46a70f9f5b1e | -12.61865 | -44.6126 | 2026-07-31 11:42:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 5ade3349-ab0d-3011-b561-7e06ecaf20f2 | -16.88595 | -45.24724 | 2026-07-31 11:42:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e5ee315b-9327-3354-9f6c-c2bc0093ecec | -13.95024 | -46.02509 | 2026-07-31 11:42:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8b015189-6d78-3c83-9731-268d69d1742f | -18.81545 | -41.57363 | 2026-07-31 11:42:00 | TERRA_M-M | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f939cdd1-12d1-3e4a-893d-0189029e577a | -13.94472 | -46.19017 | 2026-07-31 11:42:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 75f12085-eff3-390a-b638-6943242efc6d | -18.90948 | -46.0693 | 2026-07-31 11:42:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b0e29f59-84de-31c3-829b-a83b529483ca | -12.61736 | -44.62202 | 2026-07-31 11:42:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 044762d2-1a9f-3f18-b694-97b0a9875477 | -12.59869 | -44.62302 | 2026-07-31 11:42:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b1dd229d-a3dc-30df-862c-cdfc56ba95f6 | -14.39859 | -48.07808 | 2026-07-31 11:42:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5021290e-a011-394c-8144-e4811dee8525 | -14.35598 | -48.0504 | 2026-07-31 11:42:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 88148f9c-271f-3e09-84fa-17f80ad501fc | -17.60418 | -44.60968 | 2026-07-31 11:42:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| eb40d257-e9e3-3850-a6b0-d044bd5c7941 | -16.29518 | -45.66537 | 2026-07-31 11:42:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eddf192c-9e60-3777-b2c1-311b4c7ec782 | -17.85433 | -45.36267 | 2026-07-31 11:42:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 45.8 |
| de415026-4338-3501-b884-8c80462a4dde | -17.58657 | -46.50967 | 2026-07-31 11:42:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b33ee632-65ce-3cc3-8758-0b2ee496ed5c | -12.59738 | -44.63242 | 2026-07-31 11:42:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 01755240-9026-3916-9da1-9a743e0838c0 | -14.23787 | -47.48309 | 2026-07-31 11:42:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| babbaa5f-73ee-3493-b5a3-3a55178deffd | -12.2041 | -45.27172 | 2026-07-31 11:42:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 947966ce-322c-355c-93d6-b926297bb05c | -14.19507 | -44.11961 | 2026-07-31 11:42:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| e490c26b-029e-3f48-a65c-2bc46f854484 | -26.92428 | -53.07932 | 2026-07-31 11:45:00 | TERRA_M-M | SAUDADES | SANTA CATARINA | Brasil | 4217303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| d6f3a6e8-a407-3567-b760-be48de0e6113 | -26.92696 | -53.07332 | 2026-07-31 11:45:00 | TERRA_M-M | SAUDADES | SANTA CATARINA | Brasil | 4217303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| e3bfefc6-ba85-3361-a03a-329c2039cd79 | -22.43395 | -47.08298 | 2026-07-31 11:45:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ed0318e-4193-31f9-9a4f-13504947fcbf | -12.6191 | -44.5882 | 2026-07-31 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 0b05c4fc-3aaf-3539-9744-21f153802611 | -14.1966 | -44.1029 | 2026-07-31 11:50:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 554e01e6-64bb-3713-90d8-91f9f1adb2d7 | -12.5989 | -44.6381 | 2026-07-31 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 94e68663-c6dd-3149-a370-eabf7e49020a | -12.6186 | -44.6116 | 2026-07-31 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 183.5 |
| cf46bf8a-b57f-3fcf-b401-0d81e0e803f9 | -14.1966 | -44.1029 | 2026-07-31 12:00:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 58d166c9-15ee-3dc7-8939-7bea811dd625 | -12.6191 | -44.5882 | 2026-07-31 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 22640cb4-bf3e-3600-ab85-afdfbbc41299 | -12.5989 | -44.6381 | 2026-07-31 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| fc5d6e29-3f0b-38e9-becd-1d5578ddac6c | -12.6186 | -44.6116 | 2026-07-31 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| e94ec826-55b0-32a1-bc90-4004c11a637b | -12.5993 | -44.6147 | 2026-07-31 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 667c83f3-908e-3621-be0c-922b369736aa | -14.1966 | -44.1029 | 2026-07-31 12:10:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 82082d2b-039c-3640-9b4d-8f0bbae14c49 | -12.6191 | -44.5882 | 2026-07-31 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 445c2ad5-a468-3eef-975d-67e0888a263f | -12.6186 | -44.6116 | 2026-07-31 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 913a5912-ac5f-36f2-b68c-bc07a21ef966 | -12.5989 | -44.6381 | 2026-07-31 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 3567c3b6-3034-3c24-aa9e-088ea1c52eb3 | -12.5993 | -44.6147 | 2026-07-31 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 1a345c59-93b6-33d1-90fe-3c51d869ed0f | -14.2162 | -44.0993 | 2026-07-31 12:10:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| b1216a23-6259-33b2-870d-738788fe887f | -12.5989 | -44.6381 | 2026-07-31 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.3 |
| cdc14c52-4468-3bb2-b09d-990729e032d4 | -12.5993 | -44.6147 | 2026-07-31 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 307.1 |
| 5fb4ca05-33fc-35e9-b487-fc8025fb6be1 | -12.6191 | -44.5882 | 2026-07-31 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 099f8859-a25c-3751-b9c9-ad3ea785bf97 | -14.2162 | -44.0993 | 2026-07-31 12:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 160.0 |
| fd0911d9-0b27-39da-92e3-ab8167a294c7 | -12.6186 | -44.6116 | 2026-07-31 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 8a6e765c-c916-329d-96c2-7206cbe3b1b8 | -14.1966 | -44.1029 | 2026-07-31 12:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 4a954f52-cbe9-3a70-84e6-75bf5c16ad43 | -12.5993 | -44.6147 | 2026-07-31 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 262.3 |
| 7f00555e-5ea3-3e23-97a7-6ee47df9d2b3 | -12.58 | -44.6178 | 2026-07-31 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ce338c4d-8382-32d5-a933-6ae68232e1eb | -12.6191 | -44.5882 | 2026-07-31 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 2fde4e0e-a4c8-30a0-9035-c04f323ac4f6 | -14.1966 | -44.1029 | 2026-07-31 12:30:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 233.3 |
| bd3f9303-5554-3318-8f7f-79c9df08dc63 | -14.2162 | -44.0993 | 2026-07-31 12:30:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 298.1 |


[Clique aqui para ver as próximas entradas](README16.md)
