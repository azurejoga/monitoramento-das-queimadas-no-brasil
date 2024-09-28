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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ce7fa8e-0613-37f4-b6dc-4e900e721a80 | -11.66802 | -60.39128 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb6e280b-7c69-3572-ad6e-834ec9297e97 | -11.6614 | -60.28199 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3360db33-8b26-3773-9dbf-5ecedfbe3f10 | -11.65799 | -60.28142 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ba1941c-9f1e-38bf-9ddb-b14217d08e1e | -11.65396 | -60.28459 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5f73d61-75d9-3826-bbf2-207c07daf49d | -11.64994 | -60.28775 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf7434ab-5b79-3851-961b-819520459c06 | -11.64251 | -60.29031 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6512e1df-eaf8-3c3a-a714-2de816365359 | -11.64222 | -60.31333 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00712e98-2f2e-3087-9906-499547319256 | -11.6416 | -60.31708 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13dde141-2a2d-3a75-84f9-16453625ad5e | -11.63943 | -60.30897 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83c8ac8e-2a79-3908-95e7-8c047fafdf1b | -11.63881 | -60.31271 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 298b4282-9ef2-33df-a603-d11d7a883924 | -11.63508 | -60.29285 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d65d16a1-d924-3a5f-8a4a-9d858bee8cf1 | -11.63168 | -60.29225 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efe76c19-47e0-3d5a-a146-53de79f10779 | -11.63153 | -60.29276 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4e7e486-4aea-3510-9a3f-e17d5dee01be | -11.62751 | -60.29593 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ada64ce5-6cf0-3aac-81ec-93cb3faaa5af | -11.61849 | -60.28673 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bd7aefb-0234-39de-ac3e-a4745054c6e5 | -11.61435 | -60.35556 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2c9b832-8f79-36cc-bf0d-eb969cbfa311 | -11.61094 | -60.35491 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f348739-2e03-3648-805f-b507a18c504c | -11.60972 | -60.36249 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03c2550d-d71b-3554-a87f-7698e75dafeb | -11.6091 | -60.36633 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf5290cf-2e8b-38ce-a179-b87fbf571593 | -11.6063 | -60.36188 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0b03aa1-5cb6-33e1-b0f3-de35fcdd4bf8 | -11.60568 | -60.36573 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76d2703d-e823-3e35-9e0c-684de710dca8 | -11.60226 | -60.36514 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7f6efa2-1754-3201-8d2c-680539045659 | -11.5948 | -60.36781 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59db23e3-c755-3a7a-ac42-7e43891eaccb | -11.59418 | -60.37162 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b256e5-05aa-3ea3-a574-38c68ce12bde | -11.57388 | -60.30238 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed3a7208-5ce4-3a4e-8aaa-d2b0f1cf82ea | -11.57181 | -60.37945 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c01824b-84b4-3a27-8aa6-7956397e3065 | -11.5562 | -60.30327 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4485d0bf-73d2-34b7-905e-51bcfd2311c5 | -11.4681 | -60.45586 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f846831c-e4c8-37ac-a58b-7c96dfd7391a | -12.64726 | -60.39074 | 2024-09-28 05:10:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ede1585d-b7e6-3f91-98e3-506811e4c033 | -13.69829 | -60.70114 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 96a2b509-a755-343c-8770-9091a3cfde8e | -13.69767 | -60.7049 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4a9f4134-e2ab-334e-b47f-936f726cfe7c | -13.68097 | -60.72135 | 2024-09-28 05:10:00 | NOAA-20 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74aba0ed-c518-331b-8630-2266d83de004 | -13.65315 | -60.67788 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5734e552-39b9-379a-9b79-d35b5094c6e8 | -13.65253 | -60.68163 | 2024-09-28 05:10:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24707d6a-9a9c-37be-8678-0b2823a98c15 | -9.28468 | -62.31423 | 2024-09-28 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52529f9e-ea10-3f27-90ec-ec00035c38eb | -9.28385 | -62.31914 | 2024-09-28 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa92fc40-a779-321d-bed0-f61f9e05e447 | -9.09253 | -61.13241 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d437b44-703e-3154-a7c9-4a7ea5983cf9 | -9.0889 | -61.13182 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bf56b90-aff4-31fa-9d52-3e07465e7f4e | -9.08821 | -61.13607 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a8374b8-f22e-3f60-a7e5-759088acbdf0 | -9.08528 | -61.13121 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d13056bf-f71b-3c69-aeb5-12d575f31d0f | -9.08458 | -61.13547 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 357ab484-5a7f-334d-acb0-d5f55284f3ae | -9.08165 | -61.1306 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d77022a-13cd-390f-be53-2ee82a300e30 | -9.08095 | -61.13486 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4797d66c-8d62-33d7-abc0-275251af182a | -9.07733 | -61.13425 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0921cc22-19e7-304e-a519-1d56cbbdc0e4 | -9.04627 | -62.34428 | 2024-09-28 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7dece2ce-87d7-3d71-adbc-4353d8733bb9 | -9.04239 | -62.34361 | 2024-09-28 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a395fd41-3ecc-3d75-852a-a6125a7da0a0 | -9.03031 | -61.63658 | 2024-09-28 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c42b7011-f9f5-3cd8-ade5-13602b99d6dc | -8.86177 | -61.82891 | 2024-09-28 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72ee7b5f-91c7-3dd5-bcd4-0d3d1703c444 | -8.84229 | -62.14875 | 2024-09-28 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b09d5dda-52df-3d4e-9406-eb8604c6869d | -8.84146 | -62.1536 | 2024-09-28 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53a15e93-e737-3ac0-b098-ae7d5e164818 | -8.83927 | -62.14326 | 2024-09-28 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eebd0063-152e-3ba9-b2ef-80bdb1e00572 | -8.6113 | -61.279 | 2024-09-28 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 9a5c8888-e1e7-34ca-913d-d61c26593325 | -8.61059 | -61.28337 | 2024-09-28 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 6b2f1020-5ecf-3fc8-9dd3-eae562e9c9e3 | -8.60763 | -61.27839 | 2024-09-28 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1797dc29-7a2b-3b6b-aca1-b2ef2ad7f357 | -8.60691 | -61.28275 | 2024-09-28 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d777a8e-80f3-3582-b67d-7ee9d47b804b | -8.59984 | -61.1436 | 2024-09-28 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22bdd060-922c-3a28-bccf-b19c72c4d47b | -8.51328 | -62.01434 | 2024-09-28 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78cb2964-14d5-3e65-b1fe-a8ec4cfcebab | -8.51184 | -62.01135 | 2024-09-28 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a35e4245-b016-308e-bc19-a1daddf64017 | -8.51102 | -62.01614 | 2024-09-28 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93fb261c-8f83-3454-981e-390ed6c088ff | -8.50991 | -62.04562 | 2024-09-28 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08ce944e-479a-38ed-b40f-83d6c5832621 | -8.50944 | -62.01367 | 2024-09-28 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2379b28-5ac7-35fe-9b63-84b8aa725a5f | -8.50908 | -62.05043 | 2024-09-28 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b29372d-f21c-3245-96b4-55cf7b93406a | -8.50773 | -62.04802 | 2024-09-28 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d29af5c-a087-34b3-b001-1debff208cc5 | -8.50524 | -62.04977 | 2024-09-28 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97e9d218-1f28-3a8f-af28-ab6ba5b17cb3 | -10.20817 | -61.41425 | 2024-09-28 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fbcc390-deb2-3908-8164-4d3902725d51 | -9.37068 | -62.33031 | 2024-09-28 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f992c07e-d2f5-36cd-a19c-f935baaaa0a3 | -9.36985 | -62.33517 | 2024-09-28 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3f23b22-284b-3778-baf9-d56b3dbd072b | -12.27678 | -62.32067 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 644edc29-7195-3603-b589-9c39ae1b2f5a | -11.73946 | -62.5607 | 2024-09-28 05:10:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 886254c5-7e0d-38ff-ae97-483812e0f580 | -11.50757 | -62.41796 | 2024-09-28 05:10:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bb62be2-25e6-386f-b2f0-094be5d9f46e | -11.50381 | -62.41732 | 2024-09-28 05:10:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0cc1e6f-47e5-30cc-8d99-7b88c465b768 | -12.27753 | -62.31617 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07a82a14-21a6-304b-9341-fca998aeadfc | -12.2753 | -62.31873 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19d61402-e035-3ec9-bff8-ed385020cc63 | -12.27307 | -62.32 | 2024-09-28 05:10:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bc499c5-bd54-32a7-9f8b-10202695482b | -12.86669 | -62.71789 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40fea613-08bb-305c-b6ca-e8116b0de604 | -12.85936 | -62.75977 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 68b2c90d-f0c6-3b79-963d-53c68d755461 | -12.85854 | -62.76442 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bf5db5f7-6393-373b-b986-82f17901459b | -12.85805 | -62.7451 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dbdf2860-9d33-391c-98a5-48cb350d7ccf | -12.85745 | -62.74701 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 904ef5e0-82c6-382b-8b14-0efedb79e8e3 | -12.85723 | -62.74976 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9881777-010b-3a16-b3f6-d00a540265a0 | -12.85666 | -62.75169 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 53d2cefa-acec-3570-bf90-3c910bdd6958 | -12.85641 | -62.75443 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 54439db1-791f-36ec-b571-a0c30cabfd0d | -12.85605 | -62.73234 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c6e7300-39fc-3e25-b52e-f82ed256150c | -12.85587 | -62.75636 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 43af5b9f-9588-3237-85ae-ed0540dcfc42 | -12.85508 | -62.76102 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8713d4fc-cd2a-3ddd-889c-a8102512e26c | -12.85347 | -62.74908 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8b74a7f1-43b3-3647-a2f6-ef2ea7073620 | -12.85229 | -62.73166 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7744ea4d-0834-3574-a71f-bf9c5dd2867a | -12.8484 | -62.73376 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3528154-2a99-35dc-ab7c-fd440ad624d2 | -12.84695 | -62.7403 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d93e705-14ab-3ccd-a859-3e4233e2e008 | -12.84477 | -62.73029 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1f8c927-cdf2-3eb5-ac4c-50bd28d944dc | -12.84398 | -62.73495 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9136292e-71c2-3a09-af33-873e97d73ef4 | -12.82153 | -62.79841 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9737c065-af2d-36bf-a225-8d3a362227f1 | -12.79429 | -62.79832 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2cdbbb0-17ec-3cc5-ba29-135b16df5024 | -12.79348 | -62.80302 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7595085-05c5-3c93-9c4b-e9fdc7e2178b | -12.79321 | -62.75945 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e5f7f01-aed1-39ce-8a40-43dc4ca749dc | -12.78836 | -62.78756 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6de245c4-e9b8-31c0-8785-061801d5f44f | -12.78701 | -62.7728 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5da26e4-5afb-3fbe-a057-1db5fae1c687 | -12.78458 | -62.78687 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb6ce183-5e9e-323a-b4ba-1030d97da902 | -12.78324 | -62.77212 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84609536-6b47-302b-aeea-66340b245009 | -12.78243 | -62.77681 | 2024-09-28 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README91.md)
