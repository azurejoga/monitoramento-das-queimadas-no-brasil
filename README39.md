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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0862e3ce-a9bf-3ab7-a8c5-574a72969d7f | -22.62348 | -43.70999 | 2025-09-11 04:00:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c3f22a51-cdb9-311b-935c-7a24ddba18d4 | -22.8702 | -46.40475 | 2025-09-11 04:00:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f001c74-0856-33b6-8247-fc83e9ec0106 | -23.35222 | -47.21657 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b9f87e58-7738-3a45-903e-a5278d11c755 | -22.66971 | -53.12477 | 2025-09-11 04:00:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f979bd72-9c44-31a2-9e69-86fa0282f1e8 | -22.90703 | -47.0767 | 2025-09-11 04:00:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 93fd161f-f39d-3d35-830b-9ca6762b9553 | -23.16398 | -47.33027 | 2025-09-11 04:00:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8e3e859e-f291-34f7-bba7-ab41eaf0036c | -22.66327 | -53.12731 | 2025-09-11 04:00:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ac6b9838-8b03-3be6-94e2-d133d635a542 | -22.82178 | -47.04268 | 2025-09-11 04:00:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 473ed02d-268e-3851-a2a9-13598ddfeaf9 | -20.91892 | -49.46178 | 2025-09-11 04:00:00 | NOAA-21 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 77c7c52d-d96b-3d3e-afcb-c771aa51fd0a | -23.42036 | -46.1384 | 2025-09-11 04:00:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cf3df02b-67ee-3538-b27c-e38e063e5e67 | -23.33722 | -47.31675 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 104c263d-a573-371a-8510-c1808dd12360 | -22.59171 | -51.89154 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| aa3a0ad0-5d0a-3324-928e-d3dd999061fd | -23.63864 | -51.67655 | 2025-09-11 04:00:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c5e52a01-d76c-31e5-bfe6-5f55ed0159e5 | -22.82621 | -46.43487 | 2025-09-11 04:00:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e56f1605-31f7-3346-a8f5-41f467e7f589 | -22.59231 | -51.89256 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| d4d3ce3e-9202-3e67-9fdc-35952b2645ae | -21.28654 | -45.20527 | 2025-09-11 04:00:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14dd04a4-1d5f-392f-aa47-8f94641601b6 | -22.83923 | -47.46026 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c7181d8f-694c-3048-afca-448594fe7a24 | -22.56579 | -46.04556 | 2025-09-11 04:00:00 | NOAA-21 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3f53beed-a2d4-3a75-bcdb-a761c2abeec4 | -20.91756 | -49.46392 | 2025-09-11 04:00:00 | NOAA-21 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| e707d82e-5371-3263-9ac5-bfe3692187dd | -22.59818 | -51.8906 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| d8086e96-abd6-3d50-88e6-02d27c31a375 | -22.59097 | -51.895 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| f9f92933-58bd-3477-ab12-d4a0c812935d | -23.63347 | -51.67428 | 2025-09-11 04:00:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0e7ab890-d0a6-3c2c-85cb-3e1f88ccfaf7 | -23.14723 | -48.2562 | 2025-09-11 04:00:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 651e21d7-8ac9-36c9-82c7-b5102f330e4c | -22.93295 | -48.38413 | 2025-09-11 04:00:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| dd789027-9cf0-384a-b082-da83642e7624 | -22.5193 | -49.08747 | 2025-09-11 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f992f25-defe-3a79-8f02-115d20730afc | -21.12797 | -47.73097 | 2025-09-11 04:00:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a27b73bd-c8b9-397b-8e5f-9dd69d78e516 | -21.52931 | -43.8836 | 2025-09-11 04:00:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1a49400e-361a-3231-8332-1a15c0340b17 | -20.91789 | -49.46698 | 2025-09-11 04:00:00 | NOAA-21 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 6558c54a-0c39-3d96-b713-563536ebafae | -23.63369 | -51.6752 | 2025-09-11 04:00:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 487fec0b-0046-35b1-aad5-f6199f92af7a | -21.06183 | -46.14951 | 2025-09-11 04:00:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29e5dabd-cbc9-3fca-8c9a-38ff3c0442b7 | -21.35534 | -44.22272 | 2025-09-11 04:00:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c5929586-cf80-3932-882f-8b362bef27c6 | -23.74917 | -51.78908 | 2025-09-11 04:00:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| d4184084-b35c-37b6-a0e8-dbf0a33945f5 | -21.81205 | -47.23379 | 2025-09-11 04:00:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 370f7581-850f-3b7d-b045-75d8b6a5faec | -22.92802 | -48.38728 | 2025-09-11 04:00:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1f1bae86-8c88-365c-84b0-13e92a4f5f8f | -22.8422 | -47.47023 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b0e58d21-e31e-3389-b9c0-3c54e511a0f8 | -22.59384 | -51.88572 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| ad57c56f-4e1e-3e94-959e-f20af10ce12e | -22.59755 | -51.88962 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 09e5d704-c6e3-3703-9fe6-22220943a9e2 | -5.84526 | -46.15508 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d80b330-5639-3df7-943e-b95b96199108 | -6.24395 | -44.79946 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23740c64-934a-3523-adff-685e44da10b1 | -7.54603 | -42.53135 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 21139be7-78e2-37d6-b374-cff67785358f | -5.54331 | -45.52535 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 499b3b04-ed8f-344d-ae93-16b8c00ce9ba | -8.43685 | -49.11229 | 2025-09-11 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc6374b8-dfe4-38cf-9d15-ada8fe1ac1d2 | -9.52169 | -43.06017 | 2025-09-11 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b19a1e38-2dcf-3eac-9116-1a030eb8e487 | -7.86318 | -44.88678 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bfd3bf3-bc59-363a-bdd9-9259ee361729 | -6.8326 | -47.90726 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a702a47d-8f07-3aa4-ae5b-559232e1e8c6 | -6.24117 | -42.84794 | 2025-09-11 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 31d04dac-d269-3510-9ac0-6fa6d54e7e96 | -6.31459 | -43.81535 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddfdddcb-8e9d-3973-808a-66f4fe645de0 | -8.11421 | -49.25782 | 2025-09-11 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3077fa7-c4f4-3d1b-a0e7-2468d0a68ff2 | -2.22073 | -48.22914 | 2025-09-11 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4bb4035c-074c-3936-ad79-cf64c9aeba7f | -6.0865 | -44.81398 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49ef2909-3788-38b5-aaf2-f79e08cf3466 | -6.38948 | -43.51171 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1676e8ff-532b-3bbc-82e3-55c5baa87b4e | -6.08262 | -44.81693 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bf0a4fb-134e-3de2-82ae-f7b7bc47fd32 | -6.85538 | -47.85939 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c90a1b48-d00e-3277-b061-ea68a82c5ca9 | -6.67939 | -44.57346 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37f026f3-c956-30c8-9882-6289aa47d0d7 | -7.56249 | -48.21334 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57d8c0a2-663f-3faa-9ef0-2723068c9876 | -5.97242 | -44.72164 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4e56d5d-d9c0-3917-b9b5-876a03a87d2a | -7.20887 | -40.23894 | 2025-09-11 04:21:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| dab8c151-4b67-3775-a32e-cb00c2049fe3 | -5.72848 | -53.599 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab2561f8-e173-39a8-9510-298dc4118eb0 | -5.36477 | -45.96833 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c9b9e38-6a31-3117-9e21-495304eb7341 | -8.32225 | -44.89521 | 2025-09-11 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e32f4788-fc72-3603-9f19-5943eedcf5ac | -5.73744 | -45.60339 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17e6f986-7582-33f7-a7cd-9788757e509a | -6.40359 | -42.60903 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 06f3deea-7b15-32f6-936b-37acbac928d0 | -7.29599 | -45.17861 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2173ec47-2df2-3bb0-ad14-e9dc16fb5d20 | -6.24544 | -43.49687 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4cc0443-6d3b-3689-b2dc-541bde015b6c | -6.5934 | -43.95261 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d32c183-8fd1-39d3-a832-977081736a93 | -6.25144 | -43.4138 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1845cb9-5208-36b5-ae04-dde3072ae497 | -7.26672 | -39.38117 | 2025-09-11 04:21:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 886a8b3b-d51b-321e-9a60-3d3ced5fc2df | -6.20035 | -43.53412 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 628ca430-c767-3e1f-bb17-865402572d98 | -6.29106 | -42.40685 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dcde1cf6-2131-3639-a658-566fb1aa71da | -6.55765 | -42.92124 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2243afc6-e7d2-314d-8f33-770a07a863c7 | -6.53164 | -44.60707 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 426e3516-f15d-312d-9dd6-4f3e004edc05 | -7.08416 | -44.84848 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a0b840b-b0c7-3519-9684-2291a5a4cf6d | -6.68762 | -44.54276 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bca87bc2-72f5-3804-b207-8bc31694622c | -8.43363 | -47.26556 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b412539c-5dd9-3e8e-8bcb-d4d6ea7334b5 | -6.25033 | -43.42094 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de8de4e6-0c4e-3d80-a716-37cf0eb69428 | -6.44147 | -43.06582 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5a527ad-5c08-3e6e-8faa-6d03767376a1 | -7.53852 | -44.67485 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa9898fc-bbdc-3e60-b356-5a2b0d3b4540 | -5.77487 | -44.85772 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac8047de-fc06-343e-b8ee-f8ccdd91ab12 | -8.35875 | -44.83662 | 2025-09-11 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41c09a95-1ffa-3cfe-98be-6d2fcb14c7de | -6.08207 | -44.8204 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 848900c3-8710-38f6-98de-05bb7dc86fd5 | -5.02486 | -43.12724 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 452ec669-eb4c-363c-8afa-139978c04106 | -5.43324 | -43.45933 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43ae0d67-6b81-355c-83d5-f94358e598e2 | -5.23292 | -45.45787 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78b2f65b-2d46-3817-ae9d-04dcbb6fbc8e | -7.54192 | -44.66803 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10825cec-18b9-36a0-b774-a0ba4c3239da | -8.72786 | -47.09522 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8fa3f039-1408-3fe7-aa87-cdbc16d090fc | -6.68271 | -44.57399 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77f85236-ce11-3c5c-9a96-e560deae7e01 | -7.23943 | -55.05134 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1378dd1-a929-301e-afbf-1efb0a4dac1b | -8.43797 | -49.10949 | 2025-09-11 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3dd8b49a-23aa-36ce-b0ea-e07dfa9a1ed4 | -6.59285 | -43.95612 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff3d4d2e-1d08-3d80-a7dc-f641fb063357 | -6.96991 | -44.78418 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f33009b-7758-30d5-9a39-110dc6eb404b | -5.43379 | -43.4558 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1053e158-270e-304a-b99d-5d3d709b0411 | -5.909 | -45.75761 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 253cd07f-1c19-31d5-b0c2-65046d847e1a | -6.69847 | -44.93979 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b94c7b3-dcc6-3266-96ba-fdcfff9bda55 | -8.64447 | -45.72388 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 066f9a38-1cc7-381a-b002-c80cec3749ea | -5.47645 | -43.43683 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5c9985a-da50-3514-8bd6-5bdd043805b0 | -5.28638 | -44.19811 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4132cdb-e3d9-3259-a4b1-e34fb16d4d2a | -6.79811 | -43.44262 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 47c3fa52-8b22-310e-a5e0-ff40e9e992bf | -5.52634 | -43.20431 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46257568-ed23-3f4c-ad37-bc3a2fad0977 | -6.63597 | -44.07404 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 256e348e-fc99-3b1d-9046-1b552bbed508 | -5.53381 | -44.34749 | 2025-09-11 04:21:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README40.md)
