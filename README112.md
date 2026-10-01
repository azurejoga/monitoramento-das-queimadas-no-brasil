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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e4e549f-0bd4-3962-b9c2-ec3fcd48d929 | -16.43779 | -43.36961 | 2026-10-01 16:11:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c68757f2-dbbc-3d5b-80a5-1da0c79d6b43 | -14.36794 | -44.74517 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b02e2b81-6b3a-38b6-8ee5-4a80456e2230 | -15.96197 | -40.52597 | 2026-10-01 16:11:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7012c3a9-4444-3fa8-8fef-353d045810c0 | -15.00065 | -39.74098 | 2026-10-01 16:11:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c582c2a3-1a8c-3f7c-bd8e-ad15288d2ec3 | -14.40948 | -42.20506 | 2026-10-01 16:11:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| eaaa979e-7ba1-3984-a30c-3a4d5e20f7f8 | -13.65695 | -39.19334 | 2026-10-01 16:11:00 | NOAA-21 | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| ff947878-cfa7-395c-a512-9ddf8b6895b5 | -14.91767 | -39.66285 | 2026-10-01 16:11:00 | NOAA-21 | FLORESTA AZUL | BAHIA | Brasil | 2911006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 20c4fd62-06f8-31ac-bee1-9a9b93274b5d | -15.17924 | -41.3109 | 2026-10-01 16:11:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4378a94c-cf35-332a-b93c-d1a8641dd46d | -15.68785 | -40.59506 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 41a3a21c-3555-31a6-94a5-a91daca92559 | -14.35958 | -44.77697 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 6abd6056-6d11-3551-91ee-e972eb8659b2 | -15.8578 | -40.79521 | 2026-10-01 16:11:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 730b8097-fd62-34db-890d-0150fd91e9ec | -14.24486 | -40.04493 | 2026-10-01 16:11:00 | NOAA-21 | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2190279b-fc35-3b91-b833-162f1d8df3ae | -14.30485 | -40.5178 | 2026-10-01 16:11:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c448a224-9558-31a0-8a0b-de01979660c0 | -15.24794 | -40.91168 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| be002be5-e27a-3dd7-94fb-98acdfa73c00 | -14.12139 | -40.01447 | 2026-10-01 16:11:00 | NOAA-21 | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3cd18726-227c-380f-bcfc-6d03b6ed7f3c | -14.16277 | -39.14598 | 2026-10-01 16:11:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 164e2dd4-46b3-3f7d-bf91-7b3a6eafe69a | -15.24018 | -48.56376 | 2026-10-01 16:11:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a2b54f33-814c-3746-a25d-6e1438a2f0fc | -14.9135 | -39.27718 | 2026-10-01 16:11:00 | NOAA-21 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8cd56240-30fd-3b76-ba1a-2f6304226c20 | -13.54265 | -39.33556 | 2026-10-01 16:11:00 | NOAA-21 | TAPEROÁ | BAHIA | Brasil | 2931202 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6cbea7af-13f9-30ec-a03a-91a7b45ace78 | -14.47549 | -41.55001 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 191.8 |
| 431b885b-b851-3cb0-ab7b-a2f7eeda0e1d | -15.85789 | -41.71671 | 2026-10-01 16:11:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| c245cd0a-16d9-3850-b615-07729efe7731 | -15.96076 | -39.91752 | 2026-10-01 16:11:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 881d5631-7a8f-39a1-9bc1-36328bf17270 | -16.12022 | -42.2251 | 2026-10-01 16:11:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| e5a1c0b5-7515-358c-b8ea-4c01ada0177e | -15.68392 | -40.59176 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 7357042a-15c6-3ac6-8063-8eb5fdfacccb | -16.08566 | -42.62246 | 2026-10-01 16:11:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5f5db79c-aba5-31b5-be3f-8f11f49293e7 | -15.62481 | -49.26656 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 136.2 |
| f57653b0-536f-3212-83ee-52331a0361b7 | -14.35519 | -44.74307 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 66535623-f4e1-3843-8556-db27602b354f | -14.69908 | -41.57243 | 2026-10-01 16:11:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 74aa3c5a-4be9-3a47-930a-f679d49604bc | -14.91681 | -39.27665 | 2026-10-01 16:11:00 | NOAA-21 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d07a2e72-345c-3976-82b9-45bf45f075c3 | -15.0161 | -51.38762 | 2026-10-01 16:11:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4206aa64-6bda-3acd-8719-55c45fdb9b01 | -16.15573 | -42.86935 | 2026-10-01 16:11:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aae476f4-9327-3a0c-96ec-be7796f808d8 | -14.42971 | -44.77149 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 718bf41a-ca7a-3962-acec-a599b18be541 | -14.77337 | -40.33257 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9796a18f-c956-3b98-87ad-89ec96f60283 | -15.09485 | -48.40587 | 2026-10-01 16:11:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 04272750-7ee3-3ac8-9778-34dfd3369329 | -15.65687 | -44.71311 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 632d3c82-4ec8-3dad-9901-6692cf3afa8b | -15.24891 | -41.01488 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| afec2e12-4f2c-3c1b-ac70-50371c41eaf2 | -15.65174 | -44.70592 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d31fb26a-f69d-3da1-9d0c-e0f8fad05c78 | -15.64808 | -44.71034 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 87c6fbd2-e826-3b4d-9d1a-405d7b1a82ea | -16.07763 | -42.61874 | 2026-10-01 16:11:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 86b9a86e-ca4b-32b2-8078-79bd23ec79cf | -14.8218 | -41.45119 | 2026-10-01 16:11:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 94.0 |
| aded236a-fadf-37c5-9b3c-8f54f5d1a009 | -15.95743 | -39.91805 | 2026-10-01 16:11:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| d63b3b7a-12a0-3725-b866-8bd7d2473283 | -16.18058 | -42.88435 | 2026-10-01 16:11:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f9a7f89e-d497-3b1f-8489-15724677d42f | -15.24372 | -40.64536 | 2026-10-01 16:11:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 03c553a1-50f0-37bb-91d2-2d5079d485bb | -16.08628 | -42.62696 | 2026-10-01 16:11:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55a63e9e-fbd8-34ff-a91e-79c48708b71e | -14.4795 | -41.55341 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 191.8 |
| a4ae268b-0ef6-3d00-b4fe-8f25968e8255 | -14.33888 | -44.74549 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 8cf62fa8-c63a-37d7-893e-e641e4ee223e | -14.38166 | -44.7547 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0e80623f-a163-3f5f-ad9a-82e8fcef3f9e | -15.24833 | -46.15129 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| bd41ecca-238b-392b-a1ea-62a8576846ea | -15.89673 | -47.75909 | 2026-10-01 16:11:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fef4746c-9904-3aba-a198-61b21d7a6b27 | -14.35375 | -44.73195 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 65d57369-57a9-3246-957f-20238a961bb0 | -14.7374 | -41.37708 | 2026-10-01 16:11:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 200e7e3d-0060-3500-bf63-b8d3e9e56c56 | -15.79563 | -44.69092 | 2026-10-01 16:11:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 05851518-c1f5-3ad9-a198-a11452152ebb | -14.07137 | -39.61528 | 2026-10-01 16:11:00 | NOAA-21 | IBIRATAIA | BAHIA | Brasil | 2912905 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ecbcf792-d616-3314-8f0a-1465be19aa69 | -14.36416 | -44.78011 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ee5a667a-5ca3-310d-ae7f-9be5a2cd0912 | -15.20377 | -47.96378 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a722a7c4-ecdd-3d42-8b95-e399a097574a | -14.34606 | -44.73673 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 82d97797-fe19-305c-add3-6a8700537cee | -15.67714 | -40.59269 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| dd81b02c-67bf-302c-a64b-19b5c80d98f4 | -15.62096 | -49.26778 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 46d6631f-8e52-3f7d-8668-14d3c90c63af | -14.36922 | -44.78699 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7bc922c2-ebb4-3509-80b6-f6f48b3b3acc | -16.28794 | -48.01954 | 2026-10-01 16:11:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9511b334-e4c6-3dc0-950d-7e2d6cd3fcf0 | -16.29644 | -45.63786 | 2026-10-01 16:11:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f3232779-2185-3b3f-a40d-c451848468ce | -14.91098 | -40.80993 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c5071dff-f686-33b2-8dcc-e6e8b40ea4d6 | -14.64199 | -44.68465 | 2026-10-01 16:11:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e916f884-ae64-308a-b044-510381c13418 | -15.45236 | -42.09639 | 2026-10-01 16:11:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 92a342fd-f195-38f3-9936-aa97a09f7ebe | -15.26835 | -40.90879 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| f2537040-5c48-3ea8-baa8-7a7cf102bbba | -14.9955 | -41.56917 | 2026-10-01 16:11:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 4ecfc93e-7236-3d46-adfc-ae1961c4421f | -15.10024 | -48.40815 | 2026-10-01 16:11:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| fc5bc9d7-07d4-3bb2-bc70-85142588eee2 | -14.40947 | -42.20578 | 2026-10-01 16:11:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 82420315-de31-3ec0-b20a-2429491ac937 | -14.77204 | -41.32515 | 2026-10-01 16:11:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 49b2f0c5-825a-34e7-939f-fbe360373491 | -14.3555 | -44.7776 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6a64d899-8c29-33f3-8dc6-44aa5045d5b7 | -14.37562 | -44.74036 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| b163e794-a67b-3a17-9df5-462493d3da9a | -13.62549 | -39.10066 | 2026-10-01 16:11:00 | NOAA-21 | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 3a105363-13b4-3ef8-9ea0-30add52e7e89 | -16.13462 | -43.7425 | 2026-10-01 16:11:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| aa0c1b69-58da-3bbd-b405-da109ac3b5d6 | -15.171 | -41.25304 | 2026-10-01 16:11:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| e36885be-5262-3873-85b2-61802e2fe6cb | -15.08279 | -39.36163 | 2026-10-01 16:11:00 | NOAA-21 | SÃO JOSÉ DA VITÓRIA | BAHIA | Brasil | 2929354 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 10d46a77-f02f-3255-92d3-5df3e1c4e85e | -15.68433 | -50.56885 | 2026-10-01 16:11:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4fac3b7e-118d-363b-9c15-2b533ac938d3 | -15.79198 | -44.69534 | 2026-10-01 16:11:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7442a5bf-e200-3c0f-8e6d-6d19e517df77 | -14.47894 | -41.54948 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 191.8 |
| 7d0bcb4e-6fbf-3353-a7bb-0423f126b7b8 | -14.65186 | -41.87725 | 2026-10-01 16:11:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e9a71d52-805b-31d4-aeef-59568979ab33 | -14.66599 | -44.67737 | 2026-10-01 16:11:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9db9cab8-f9e4-31e3-8053-56d68ae690a8 | -16.024 | -45.13209 | 2026-10-01 16:11:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1006f0e3-4889-315b-b2c0-fce875c6aeb5 | -14.38668 | -41.37094 | 2026-10-01 16:11:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 079dc592-d975-3247-b42d-e14d4ac374e8 | -15.31124 | -42.77063 | 2026-10-01 16:11:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3c1c2627-1895-3f19-b59a-35ff60248096 | -15.11563 | -40.74815 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 158d88a5-9439-365a-ab2c-5480e0824ab1 | -16.08502 | -42.6179 | 2026-10-01 16:11:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8c85f44c-719e-3072-902a-e39d57e07593 | -15.64688 | -44.73421 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 55603558-49f8-3ca1-aca4-dbad4453c006 | -15.00089 | -40.49432 | 2026-10-01 16:11:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 34df047e-4ea5-3653-8044-0e3b66c16cc7 | -15.07336 | -48.40508 | 2026-10-01 16:11:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 014fd33f-ccf4-30eb-86d5-0c769deeaf93 | -14.77778 | -40.33929 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| ff8ee73e-96cf-3d27-9d35-04caf354501e | -14.72457 | -41.9281 | 2026-10-01 16:11:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 19847a71-958b-3c9a-beff-0243235b823b | -14.36239 | -44.73453 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c7fd581d-7025-3847-bb8c-6aa2935a1993 | -14.37708 | -44.75152 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 88cb836a-2911-368d-91e1-9543c011934b | -15.26689 | -39.59126 | 2026-10-01 16:11:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2e79e7f2-ab9d-342f-b39e-e5ac2a6cebab | -14.71846 | -41.02632 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 793d6d22-599c-3c58-80c3-401eb1de88ea | -15.76209 | -46.04903 | 2026-10-01 16:11:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1ac7e8a1-0652-3ebc-8a4f-eea90f0802c3 | -15.82277 | -42.5841 | 2026-10-01 16:11:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 30522e63-f536-335c-b402-f9a923e4ec4a | -15.51142 | -41.57364 | 2026-10-01 16:11:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 18e9c935-cd8f-324e-802a-b56a716428a7 | -15.62091 | -41.39269 | 2026-10-01 16:11:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 15000356-2e45-3443-b57d-0fd61eabca6e | -14.50205 | -45.21373 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f449df30-9be7-3057-9f59-b811fce3d626 | -16.13854 | -43.74194 | 2026-10-01 16:11:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |


[Clique aqui para ver as próximas entradas](README113.md)
