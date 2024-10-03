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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7916e5a-ce41-32db-8131-6773849d66fa | -4.4845 | -42.8631 | 2024-10-03 02:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| e0940c8c-176d-3260-8de0-5b2fc4b08dbb | -4.5375 | -43.304 | 2024-10-03 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 00cf82e6-c430-3a4d-92ea-7fe9859f0949 | -4.58 | -48.0132 | 2024-10-03 02:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 952540ef-287c-3e0f-85f4-b769b212091a | -4.9264 | -43.79 | 2024-10-03 02:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 947657a3-f04e-3eda-ae95-643a9e42cd9f | -4.9265 | -43.7669 | 2024-10-03 02:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 54622caf-8583-3cab-a2af-445997babf74 | -4.9451 | -43.7888 | 2024-10-03 02:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 485fa104-60ad-3870-a173-92add3be8fdf | -4.9452 | -43.7657 | 2024-10-03 02:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| cdf3852e-0511-3ba7-a59a-781434c7de70 | -6.8777 | -59.0504 | 2024-10-03 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 7a89f2b6-7947-3196-bcff-873ea0b70b31 | -6.8778 | -59.031 | 2024-10-03 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| cce41f80-e4a3-36a5-93e8-3398c3786197 | -8.8506 | -45.5086 | 2024-10-03 02:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| b264d1f6-660c-3cac-8075-7824419a52fb | -8.8509 | -45.4859 | 2024-10-03 02:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 103ad90a-f8d6-3119-802c-4a09a8739226 | -8.8695 | -45.5066 | 2024-10-03 02:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 7367bcdc-576e-3dd6-b262-270b39ace512 | -8.8926 | -62.3348 | 2024-10-03 02:25:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f22f4ad1-b521-3c1b-be4c-47dce0f25092 | -8.9976 | -67.4094 | 2024-10-03 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 38603fcf-c00e-3c70-8d37-21ab16f5353a | -8.9791 | -67.4099 | 2024-10-03 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| d2936553-dedb-316e-a987-fc1e3e352142 | -9.0149 | -67.7423 | 2024-10-03 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 3efc1d22-51ab-3842-904e-dcfc20d49413 | -9.0515 | -67.871 | 2024-10-03 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2be94b12-fb05-3de7-a298-6bad731ca401 | -9.0516 | -67.8525 | 2024-10-03 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 5286b42f-ba98-36c1-a27c-2471354aebb7 | -9.1566 | -61.6758 | 2024-10-03 02:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 003518e9-a189-3522-90d9-227ab5d3a500 | -9.1752 | -61.6749 | 2024-10-03 02:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9e3c700c-3566-35d3-8295-affc4f8326d8 | -9.4368 | -64.5419 | 2024-10-03 02:26:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 69dae98c-a8d6-3967-a91f-2f278a24544c | -9.468 | -62.3857 | 2024-10-03 02:26:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c0933944-ac9b-323c-8120-4f7f603ee550 | -9.4865 | -62.4039 | 2024-10-03 02:26:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 605be4f4-116a-3d1f-a6e4-0db6848ff651 | -9.4866 | -62.3849 | 2024-10-03 02:26:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 79ebf814-2b64-3723-9d73-43cc82f7fe16 | -9.494 | -68.4895 | 2024-10-03 02:26:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 009d6848-0680-39c7-8140-e82165620a1d | -10.8942 | -63.8971 | 2024-10-03 02:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 284a227d-45d3-3685-9069-c56dab86bfbe | -11.2565 | -60.6019 | 2024-10-03 02:26:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b0bd1a76-e49f-3c9f-b14b-e15850bfb776 | -11.2566 | -60.5825 | 2024-10-03 02:26:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f74d2354-ed61-3f2b-a17c-22e307e9f452 | -11.6932 | -64.9785 | 2024-10-03 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 34430e5b-1319-3d6f-9f55-590350300a21 | -11.6931 | -64.9974 | 2024-10-03 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| fadfc040-4801-330f-a585-8428dca7f7f5 | -11.693 | -65.0163 | 2024-10-03 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| dba21b90-d213-3cdd-a486-4e7eb18ece2f | -11.6744 | -64.9793 | 2024-10-03 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b3dd4caf-eef6-39b3-a565-8c57d7f9e46c | -11.6743 | -64.9983 | 2024-10-03 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 76135a27-aa04-3485-82d9-650d5c84aff3 | -11.6742 | -65.0172 | 2024-10-03 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2918de0e-b253-3e4f-8bf5-d25d359adffa | -12.404 | -62.9817 | 2024-10-03 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 39ff48d3-3f60-375f-88a4-b47e3a96c0b6 | -12.4038 | -63.0009 | 2024-10-03 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| f77a192f-51fb-3785-8647-432ff65890ba | -12.6486 | -63.1022 | 2024-10-03 02:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 0ac135ed-e863-3893-bcbc-2351a1ce71a1 | -12.6484 | -63.1214 | 2024-10-03 02:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3ab2ad19-37d4-3fc2-bc25-205695342404 | -12.881 | -62.4538 | 2024-10-03 02:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 8902fc08-d5cc-3cd1-8102-172be968a77b | -12.8808 | -62.4731 | 2024-10-03 02:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ce6bb6c7-50c5-3772-ad9b-99b8731179f3 | -12.8802 | -62.5503 | 2024-10-03 02:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4d5675a6-98c9-3d55-b1e5-debadaed50fa | -12.8049 | -62.497 | 2024-10-03 02:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7f3e4830-964a-3d29-9657-f30379e2576b | -12.8999 | -62.4527 | 2024-10-03 02:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| d40561dc-b842-3802-ade3-3447b98ba446 | -12.8998 | -62.472 | 2024-10-03 02:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 48ed35aa-9206-39a8-bebc-15f9a434e17e | -12.8996 | -62.4913 | 2024-10-03 02:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 0861c3db-f3c8-3a33-9f62-df7671172f01 | -12.9741 | -62.6409 | 2024-10-03 02:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3abaf145-19a8-3daf-b3e7-849580907af9 | -12.9187 | -62.4708 | 2024-10-03 02:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5b681a54-ab76-3747-9931-0de310236200 | -12.9167 | -62.7022 | 2024-10-03 02:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ead85399-d359-380f-bbd8-76e682d4abf5 | -13.5195 | -51.1467 | 2024-10-03 02:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| eb31c116-55ef-3fbd-b57a-968d71c98127 | -14.6929 | -45.4432 | 2024-10-03 02:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 63fd6222-3cfd-3c81-8619-07636737a873 | -15.65 | -47.2027 | 2024-10-03 02:26:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c77bd7a7-4a7f-336e-bbaf-361d3cc81643 | -15.6697 | -47.1992 | 2024-10-03 02:26:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6b993175-fd5f-306e-8600-b9c055827454 | -16.4033 | -46.8799 | 2024-10-03 02:26:37 | GOES-16 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ccea5e53-55f8-3d41-964e-bbd4b7bd00dc | -16.7606 | -57.7512 | 2024-10-03 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 7d1e8fe2-bb37-320e-bd26-3391ffbc5342 | -16.7597 | -57.8124 | 2024-10-03 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| eb8bf8d5-14a1-3a37-b120-cdd9ceb399fe | -16.7594 | -57.8328 | 2024-10-03 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 6ab6c41b-0cb7-3ff5-b373-11ced2f29b38 | -16.7805 | -57.7286 | 2024-10-03 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| ef371a20-de9e-3061-80d3-969ed3d7923b | -16.7802 | -57.749 | 2024-10-03 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 9b7d508a-efe3-37ad-b907-466f6e81da7c | -16.7793 | -57.8102 | 2024-10-03 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 23501053-010c-3437-9585-e5e3666eeda3 | -16.761 | -57.7308 | 2024-10-03 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| f4f54eb1-6ecf-3d5f-938d-7e1c9cfff8bb | -16.779 | -57.8306 | 2024-10-03 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.9 |
| 54316aad-44dd-344b-9d46-ea6431a5fb64 | -16.9179 | -57.6926 | 2024-10-03 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 87933f54-ee58-3fec-9d49-176bbc980812 | -16.9176 | -57.7131 | 2024-10-03 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| a52ea080-1459-332b-908d-4fb0f95b7e04 | -16.8986 | -57.6744 | 2024-10-03 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| cc3d7bcf-97e5-33e6-8061-90e11ab3d208 | -16.8983 | -57.6949 | 2024-10-03 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| aaa867b4-9d61-3032-a449-2e6e632c96dc | -16.7985 | -57.8284 | 2024-10-03 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 3a0877b4-df1b-3431-bc72-5c00c60e1ae8 | -17.197 | -57.3741 | 2024-10-03 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 803692ba-73ee-3fdc-a792-7e902947347d | -18.8406 | -42.9235 | 2024-10-03 02:26:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| d2205b17-9a2e-3f22-9fe2-349ea57c7483 | -19.0141 | -43.1998 | 2024-10-03 02:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| 9c71cc26-73fb-3e87-8bd4-48740589630d | -18.6977 | -57.3123 | 2024-10-03 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.9 |
| e4f08d78-c14f-3e00-a4bd-6e14f6d010b0 | -19.0344 | -43.1944 | 2024-10-03 02:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| ee5389cf-4cbb-37e3-a17d-57377f4f6958 | -20.6352 | -46.7497 | 2024-10-03 02:27:00 | GOES-16 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 606d4257-23f4-31be-b8ae-02d65b96a4cc | -21.3675 | -47.6311 | 2024-10-03 02:27:03 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c30d51e8-c020-363e-b0fe-33b4aa666411 | -21.3875 | -47.6497 | 2024-10-03 02:27:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 8c0bbb2a-4c28-372b-ad74-2dd9345a4baa | -21.3882 | -47.6261 | 2024-10-03 02:27:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 586f7658-6cee-3872-a978-7d4474535927 | -21.346 | -55.6626 | 2024-10-03 02:27:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 7d4d667b-2e79-3551-a733-23933417ff3b | -4.0949 | -48.4894 | 2024-10-03 02:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 20459796-5768-37dc-8b53-85b0a58e489f | -4.095 | -48.4679 | 2024-10-03 02:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a089b464-b454-3087-af69-1ded0c43accd | -4.4844 | -42.8866 | 2024-10-03 02:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 565787fc-6107-3770-a966-b0f4c90698cc | -4.4845 | -42.8631 | 2024-10-03 02:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1f48fb98-22cc-3c37-961c-d3bf426f3e9c | -4.5373 | -43.3273 | 2024-10-03 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 73273c1a-866b-3661-ad6c-03f901e8ab11 | -4.5375 | -43.304 | 2024-10-03 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 46b8a1ee-90c4-3d67-b9bf-010d05431e2c | -4.4657 | -42.8877 | 2024-10-03 02:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| dbd80c1a-850a-3436-b6f3-c4cf9322d278 | -4.9264 | -43.79 | 2024-10-03 02:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| fcf913cf-638d-3076-be79-c7f42913a0db | -4.9265 | -43.7669 | 2024-10-03 02:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| c0bc7a2a-c2c4-3a1c-8132-d7bf1e833904 | -4.9451 | -43.7888 | 2024-10-03 02:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 24f76f73-9369-3eef-8a0f-a00baa13a36d | -4.9452 | -43.7657 | 2024-10-03 02:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| da74f111-1c93-3927-a5ed-9783be595130 | -8.8506 | -45.5086 | 2024-10-03 02:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| df7754b7-c4ea-317b-a51c-caf34530f501 | -8.8695 | -45.5066 | 2024-10-03 02:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 0baf40f5-097c-3772-ad5b-3b10c126faa4 | -8.8926 | -62.3348 | 2024-10-03 02:35:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 5e7c524d-7dd2-3e7c-92b5-0a2390a2551f | -8.9791 | -67.4099 | 2024-10-03 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| e3651ce9-04e8-362a-969e-b69413da72cb | -8.9976 | -67.4094 | 2024-10-03 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 9b8ab6d7-f3b0-3014-b5a3-3560835321e4 | -9.0149 | -67.7423 | 2024-10-03 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| be06cb83-4759-39b5-aec2-666c43879461 | -9.0515 | -67.871 | 2024-10-03 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1ae77ccd-69b1-3244-ae2f-11f061bb342d | -9.1566 | -61.6758 | 2024-10-03 02:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 27f92bed-c74f-3d11-83b5-fe9ca32f4178 | -9.468 | -62.3857 | 2024-10-03 02:36:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 86e86f4e-6fb6-39a5-9688-6763b1b79f8f | -9.4865 | -62.4039 | 2024-10-03 02:36:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 2f1d441f-aaaa-3026-80fb-340115047dcc | -9.4866 | -62.3849 | 2024-10-03 02:36:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a8f1b1eb-02e0-3160-b622-a07c1bb4ba10 | -9.9726 | -36.0905 | 2024-10-03 02:36:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| 574cd935-257f-3f40-a5bd-9c0c494b6730 | -9.9731 | -36.0634 | 2024-10-03 02:36:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.0 |


[Clique aqui para ver as próximas entradas](README55.md)
