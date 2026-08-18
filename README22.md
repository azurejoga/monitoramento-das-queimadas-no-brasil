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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25526977-3ed5-34de-8644-566a1cc35ffa | -7.53889 | -55.58576 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3946133-3b02-346a-8831-13ef97767894 | -8.33609 | -46.47089 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0a2c760-9da0-36d6-a8cb-21d853605ebb | -9.08267 | -50.81416 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ca43051-a0b6-37a1-9b42-b6c85003b82a | -6.84173 | -58.9938 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f48984b-ee53-3465-b1c5-84db64dae469 | -8.59666 | -50.34542 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ca258d68-ef29-3711-ad98-3060dbb09df3 | -8.56381 | -54.69524 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5d37f0c1-046d-3f6c-a347-ce206e8ee4b4 | -4.84723 | -42.05843 | 2026-08-18 04:38:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6fd5a4af-2d2b-3cac-9d6a-bfb60a6a3617 | -9.47865 | -51.60252 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9263d688-3a62-3a7b-bb27-185aaa805f95 | -8.74279 | -45.31297 | 2026-08-18 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b134770-4141-3481-ad0f-f85d1a576692 | -8.55631 | -55.30703 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb0b2f35-1342-32bf-bf83-283428d8b413 | -7.62924 | -55.62305 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| facb0db2-bbda-385d-a27e-cbd9d776b74b | -9.47487 | -51.64814 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f467a357-5662-3cc1-ba6d-a52cae4b9122 | -7.28552 | -44.07396 | 2026-08-18 04:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf6b15b6-9394-3fa0-837c-468e6d2b38a0 | -8.49317 | -48.81779 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9aa9f330-a60e-372f-94ce-1e40b9b260de | -7.13091 | -47.51637 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29d97794-ecc2-35c3-b1ff-aa85782e7fdb | -6.75332 | -59.17129 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a18976c0-db23-33c4-94e3-70a7aa28104d | -7.17511 | -43.12241 | 2026-08-18 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 632429c6-4f57-36ac-a17f-653b59d549f8 | -3.42992 | -51.51595 | 2026-08-18 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 626ef099-bb9b-3836-81f7-bc7ff50770ac | -6.99036 | -59.04785 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b516f29-b373-3886-a9c2-b9c7cbbbc8f1 | -5.73345 | -44.51131 | 2026-08-18 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d25a526-982a-36f4-adec-b4e094e4d78d | -8.18644 | -55.01614 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 223d2f1e-a5ed-3aad-8d1e-4e822a5a4773 | -10.85575 | -44.96803 | 2026-08-18 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 929b2806-3bac-3404-8b71-c115a1034c0c | -8.21924 | -55.03421 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e433b406-367e-3dee-9157-a5337c01a9cf | -9.77308 | -46.71743 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 413ec290-566e-35d4-8057-381ab2441166 | -8.58121 | -54.68212 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 73636db2-e6a1-315b-a5da-457c5821a7e7 | -7.38438 | -55.48678 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9de7d61a-3a2e-3528-988d-6b83ae62a9bd | -6.95565 | -59.02889 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0067c1e7-b19b-3cb0-b078-9b61373c1f1e | -7.45288 | -46.15234 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ce043e4-1f6e-3db4-afd5-8ea1896f35e9 | -7.55706 | -55.57291 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc4ed392-fc5c-3e34-bd2f-91d67a3bc8ab | -7.56342 | -55.56764 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3d0bf56-546a-3d13-9359-247219e37e95 | -9.0691 | -50.84905 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c016958f-1e26-362f-9122-4bcd1a5884e1 | -7.12303 | -47.54408 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98eb9a67-3bcc-37fc-bf04-950199c3a064 | -2.87569 | -48.85433 | 2026-08-18 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bf6fb9d-61b5-3cbd-813d-cac697a087af | -8.32671 | -46.48726 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 641a4e39-5288-3610-a3db-ae5acd7657ee | -8.57154 | -54.73549 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4ffb63b9-170d-3d04-8c8c-e5d860e4605c | -5.73696 | -43.27218 | 2026-08-18 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b5f7810-82c5-3fdd-81c6-178f860d0a70 | -8.58318 | -54.72663 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 2d303f40-b00a-39f5-bce1-ffb6c0e22b2b | -8.52987 | -54.909 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1145e60d-ef3c-3d68-97d0-85fb2ab10a45 | -9.42316 | -48.25515 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d978aa7a-faac-3888-b996-643fb3db8194 | -3.51365 | -48.03605 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31bf2bbb-136f-374f-973c-cb705bf22232 | -8.33887 | -46.4749 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ced93fab-3080-316f-9002-534b3dc11cbc | -9.46359 | -51.62016 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 818cd057-e0df-316d-a13d-a6b8c5d5da72 | -7.17121 | -43.4204 | 2026-08-18 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 41df3972-c502-3f68-8fe6-8a072210d119 | -7.16881 | -43.13908 | 2026-08-18 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af9c4a01-6530-31db-8045-6cebfca842c4 | -8.36199 | -46.37119 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04feaf63-a38c-3703-9429-af1b84e4df4e | -7.77663 | -45.71035 | 2026-08-18 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b691fcc9-4794-317c-85b2-f1459c6267b6 | -8.53198 | -54.89745 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ce43f3db-38e6-3ec8-a5aa-00f7f23945e7 | -4.41475 | -42.13667 | 2026-08-18 04:38:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34e47723-f414-3eb9-91fa-b619991ecac3 | -9.76422 | -46.73039 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94eb89f4-5717-33e2-b568-6ef66f6ec019 | -6.5552 | -44.77113 | 2026-08-18 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27e56e5f-d69c-3867-9759-ee4a74c84a9d | -7.55764 | -55.56971 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ac26e0a-c8e9-3165-bf09-2cf81ef4585e | -7.564 | -55.56448 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 788b5e13-7054-304f-b49c-b14bc0cf9f3c | -9.77031 | -46.71339 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5392511c-2432-3a58-b481-563d6115376b | -9.28093 | -50.32005 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04b194a2-d2e2-3944-bb59-d2d4240d0271 | -6.84069 | -58.99933 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2bc14dde-79f7-35df-9036-8639a031c713 | -8.55476 | -55.31578 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e33acee-f909-3b8b-80e0-adabbdfdf2d8 | -9.28457 | -50.32067 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f12c1ca0-2480-319f-9456-9d83c14cbf2f | -8.51457 | -45.32279 | 2026-08-18 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf429359-7f40-3a25-a68b-29ffd4fcaea1 | -9.79778 | -47.30941 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ec32054-014f-31cb-8f78-f39cec341dc0 | -7.81717 | -44.59782 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00e29f7d-2896-386c-a13f-12e1da47b0a1 | -8.60326 | -50.35104 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6c004328-803f-36e2-bad2-2b69144ae37e | -7.63351 | -55.62395 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a755a7a-445e-3c98-b52d-d872624433f9 | -7.1482 | -47.51553 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30be0ae9-7567-3783-9ab3-9d68f94244ad | -6.74314 | -59.15261 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d0a629c-50e9-3df1-b45a-0828c20e04be | -8.55683 | -55.3041 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75309669-2100-3721-9d8a-8622885ac95b | -8.57832 | -54.69804 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 65bab41d-ed4c-3d70-8ffd-3b9553d424fb | -6.83858 | -59.01057 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b264b440-1e14-389c-8aeb-73e26ca11f17 | -8.59153 | -50.35349 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93c6f3f8-843b-3c60-bdf6-d0b56e8d87b1 | -6.95669 | -59.02337 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0dbdb2d0-b92c-3ea9-90e0-db425b691d50 | -7.61183 | -60.95895 | 2026-08-18 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a9d4871-bb55-3186-9fd0-62b488749758 | -7.7278 | -49.31663 | 2026-08-18 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40740795-8b88-34f5-b690-f691b0b547ec | -9.06538 | -50.84821 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 16913d4e-8e0e-3deb-89f1-8a1348212970 | -9.47015 | -51.65224 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f5184f2-afd2-3b16-9e99-0081a6bdf2d7 | -3.20464 | -49.05867 | 2026-08-18 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5ab8b50-5014-36c0-9843-301c543615d9 | -10.29234 | -48.23901 | 2026-08-18 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d175e34-425c-3628-8914-8064a92374e1 | -8.56671 | -54.70681 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| fca55f0d-7d93-32bc-9a3f-9c3f028825c0 | -8.19142 | -55.01706 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ac93c802-bc2d-34f5-bc5e-51a6e8a819a6 | -4.53026 | -42.93288 | 2026-08-18 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 391e2542-87e5-358c-b802-e47dfc7ea7ed | -7.24593 | -49.8908 | 2026-08-18 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| fe1aa5a3-b5f8-389f-96a7-97897eb4efde | -7.6358 | -55.64102 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ae121a1-f55b-3950-a270-a3605c6089cb | -3.87872 | -50.31835 | 2026-08-18 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 488addf5-14e7-3c25-a4a6-6fcad2ca5b22 | -8.56159 | -54.7197 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d8d493c-be79-3df7-be59-234a9c3a348b | -5.57742 | -43.78985 | 2026-08-18 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc576bba-669b-33ca-84b2-5a60497b1896 | -6.74086 | -59.18549 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| edeebf74-38bb-30f8-ba3b-a12a46738a81 | -8.5822 | -54.70427 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 71987a54-684e-3aa6-8d9f-494009d583ef | -6.62497 | -53.38645 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a42c61-09d4-3735-9a8e-b0d4e62348d3 | -9.15229 | -40.11303 | 2026-08-18 04:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5622b7eb-3f0d-311e-90e2-d5ed32a30fb5 | -9.76034 | -46.73337 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1043b20-54cb-31c3-ba58-a3194ddb7551 | -9.45777 | -50.31276 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 085cba8d-294a-3961-afd6-30cfde985b3b | -7.53843 | -55.58604 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 729594aa-3105-3beb-8a55-e7f1d70b0780 | -6.74985 | -59.15351 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc973a39-5c00-32fd-9997-50ad1f6376f7 | -8.73767 | -45.30095 | 2026-08-18 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea6d6b2e-a48b-3965-b0b2-fce43ca5fc67 | -8.49474 | -48.82963 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ab33e7d5-5478-3147-ab1e-6593c59f0c92 | -7.12417 | -47.53698 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c3e88ab-a50e-3b73-839f-2ad77d3ec6e9 | -7.45178 | -46.15932 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ee4a776-6904-3d63-95a4-63ccdefb49bb | -6.75193 | -59.1628 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7e1785e7-a4a3-3ddf-9053-3965318669ca | -7.45233 | -46.15583 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2d38ef7-cfe3-3c50-90b2-25d8c20b3448 | -8.74051 | -45.30513 | 2026-08-18 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67bb49fa-4414-31a7-8242-e02cdd3114af | -7.60456 | -60.95757 | 2026-08-18 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae4bd169-6399-327e-a313-309f94d48812 | -6.27221 | -43.27953 | 2026-08-18 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README23.md)
