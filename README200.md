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

## Dados Diários - Página 200

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24a3c310-e1a3-3de0-9f8a-776a88d9d15c | -7.00189 | -44.05434 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| ecde622c-2dfc-3e3e-a21b-7f95c8496926 | -16.14822 | -43.74517 | 2026-10-07 16:37:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 828570ac-0960-3b2d-8b4f-0934a433f342 | -10.37039 | -45.02686 | 2026-10-07 16:37:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 02407d0c-1dd3-33af-a711-c8ed59b5b2cb | -4.77157 | -50.81032 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4a2250fa-295e-3b82-b42f-2a1c9ac4d9b6 | -15.40236 | -46.07222 | 2026-10-07 16:37:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4488a9d7-3b15-375b-8a8c-c46f0efc26e2 | -5.28205 | -45.72942 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11a8a810-6206-35a1-b780-35cb309a8d43 | -4.30294 | -50.79045 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 81b8ddc9-4d96-3041-a9b8-8466bbe77bd6 | -5.10361 | -42.92545 | 2026-10-07 16:37:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6ca5e606-8a0b-3ac2-b632-c8eb5defb0c3 | -3.39679 | -42.83638 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c6c136b4-e2e7-3a4c-bed9-3a22c8be9d5f | -5.82 | -53.83333 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 13575e8f-7be6-3268-8dff-506a61c359e0 | -6.15097 | -39.41907 | 2026-10-07 16:37:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 9938b0d7-0ac0-3a34-9fa2-75f4d51c75b7 | -3.78112 | -41.64014 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d7a12bf1-2bf7-3a41-9b5c-ac22315c6cab | -9.44175 | -45.83631 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| cbb71c5a-d8ad-30fd-98af-d23acdc29a95 | -7.1878 | -52.62407 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63aa0dd3-22d0-39e1-8b8a-f9c651951397 | -5.9924 | -44.1294 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 885496e3-c4dd-3414-ab5f-53c0bc66ddbd | -11.13805 | -46.16389 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3e3228c-a74d-3d08-961d-68007b94d7a1 | -6.92568 | -43.66805 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 4ab87125-ada6-3b67-b81f-a8e92aee6741 | -5.72932 | -45.15459 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f20e2c52-1102-3be3-9416-9e32f3e65dd3 | -7.4674 | -42.99377 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 02f14df6-ed51-3620-9cc0-b863407a3acb | -6.70476 | -44.00983 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1f5ae2d6-32cc-304a-a4c1-3fa3f091e005 | -15.97212 | -44.88224 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d97d538-7057-3b30-867b-709d5808857a | -3.91587 | -42.5179 | 2026-10-07 16:37:00 | NPP-375 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c0cd82d5-7d7d-3868-8cfe-269ecd014c3d | -7.59743 | -55.73082 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 209b3e25-575d-3251-8c8f-1443bf736890 | -9.032 | -41.46453 | 2026-10-07 16:37:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 66786d1c-352e-363d-8823-c093e658f382 | -8.39081 | -48.07618 | 2026-10-07 16:37:00 | NPP-375 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 77bfa4b3-0a3a-318c-85fa-a83e12315291 | -6.05143 | -47.31997 | 2026-10-07 16:37:00 | NPP-375 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5994fc9a-9094-31e9-aab3-1cf8bb1065b1 | -8.76926 | -45.76516 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b2815ab7-1c98-300a-9b52-702195899c37 | -15.70525 | -40.59806 | 2026-10-07 16:37:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 81f0a512-b8d3-399f-8b97-5b13fed06872 | -6.48013 | -52.82749 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f982be74-fb51-3a36-a48a-47cb7d3c68d8 | -6.68398 | -44.96593 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f7b7ea1a-6c63-32b0-a74e-c94589a48a11 | -6.07528 | -44.38261 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ac56c303-f9fa-3086-9a51-6d9c3aed5238 | -7.81073 | -44.59514 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efd687ee-d9c5-31a9-8901-8fdf58790ac6 | -17.28076 | -43.89832 | 2026-10-07 16:37:00 | NPP-375 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5538f679-3114-35d9-9f77-60739c03c4c5 | -4.3247 | -41.23088 | 2026-10-07 16:37:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| e0d66569-29e7-3a4d-9a96-a8c40fbd7188 | -4.74032 | -49.75168 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 713d3e84-dd82-35c8-841e-99cf209916a5 | -15.40172 | -46.06756 | 2026-10-07 16:37:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 33.6 |
| aa911d26-5cd5-3860-8d41-ac116fa0f6c8 | -4.5804 | -40.76888 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 49d911c8-862c-37c5-bb24-152a45ac2d44 | -6.67987 | -45.33452 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| bfaa3aec-934d-39d2-9289-81eae098367c | -5.34188 | -45.69105 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c293d24-d8ea-38cc-aad0-2b34cdd31858 | -4.21677 | -44.43589 | 2026-10-07 16:37:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8a88713-deaa-3c12-9a59-7e29caea1596 | -4.78801 | -43.33775 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| afa3cb9c-6227-343e-b824-b98aa4c3f88a | -5.9815 | -40.93268 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 3ba5ed4f-3a46-3d64-9a2e-9f280737b7c3 | -7.47398 | -42.81525 | 2026-10-07 16:37:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| f857155c-de4c-3580-b41c-1236822b03ec | -6.37517 | -55.15032 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71943940-0c14-364f-8606-ae8c9de0e7d2 | -5.99885 | -53.50668 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 58d5a79c-1ffd-36eb-907a-5f2afdb4e342 | -9.95655 | -43.54726 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 8f30861f-328e-3231-8345-fbd13a7cad84 | -7.48423 | -49.47673 | 2026-10-07 16:37:00 | NPP-375 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3bc27b73-33a5-3d20-ae1a-321cf8f1e5f3 | -8.99329 | -45.94202 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0d6d7a0c-688e-3d75-9aaf-8a0fee84cdcf | -7.57325 | -46.68658 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e708fa22-1a97-37a6-9849-f29f12ba0ed8 | -6.04593 | -42.58695 | 2026-10-07 16:37:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 97b55f98-5e55-3dfd-af1b-d8289e81e592 | -6.13654 | -44.65046 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a6efb92f-8893-39c3-909c-88a32e4d7cdc | -17.03035 | -45.92959 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd6a8871-89d1-3f04-a203-4f5da1108ae7 | -7.22357 | -44.28974 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6b03748c-db21-3d24-aca1-5e48b33406ca | -6.06679 | -44.90444 | 2026-10-07 16:37:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1993cef-bffc-36f0-b729-10adfd43178d | -7.46071 | -42.99479 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ed98e67e-6c6d-30d9-939c-fb9a5366557a | -3.78177 | -41.64427 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1820b444-14d2-3871-8117-e108d93929fa | -3.8373 | -42.63803 | 2026-10-07 16:37:00 | NPP-375 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 09601cdd-513a-37f0-b3c6-2cbc1810523e | -6.46169 | -53.69214 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 63bd356d-24a5-3aa9-8236-3a829b75922f | -14.34896 | -39.35772 | 2026-10-07 16:37:00 | NPP-375 | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| bfa8e071-6131-375c-86a2-5a420c79c1e3 | -3.5042 | -41.93988 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 876c403f-d347-33ae-a8c7-e95f581e1bfe | -6.94902 | -45.26754 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 779ff2a8-1454-3155-821a-89da21ab5a84 | -3.29637 | -39.5135 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bf7dc1bb-64dc-3cf6-bb20-fd1398df9a7c | -16.00369 | -38.92663 | 2026-10-07 16:37:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e161d657-5b56-3fba-979b-c43bba7a5ffb | -7.87051 | -54.97623 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9f52be9c-70b8-3805-8409-05bfc0a80f37 | -8.29451 | -45.47719 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b9f28662-aa9a-38ed-a114-2057f3ecb263 | -11.05526 | -45.82398 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5e2c5b04-b570-3510-adca-ca103d390bb0 | -7.76133 | -54.94608 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 8429bf0b-a1a0-3f74-8a7e-46efef015e6b | -6.02679 | -44.10997 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5c24a1ce-19b9-3fbd-80a1-75d1d21aa960 | -6.55945 | -46.03868 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3d6b748a-154c-3eac-9b1d-e61d4db1c8ee | -9.9438 | -43.55283 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 139cd7d2-b470-39b1-b212-b64a7dfb6420 | -5.75897 | -42.04082 | 2026-10-07 16:37:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 47.2 |
| 8d02342f-ba00-3ef1-bd40-70c56a5b4f02 | -5.98474 | -53.56508 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 16e3e1c4-8d44-38c4-a054-e8a0ea0f8c7b | -9.93412 | -46.8094 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d5ea7496-6a34-3280-b042-d0ecba57fa57 | -9.58081 | -54.63861 | 2026-10-07 16:37:00 | NPP-375 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 0efa9f3c-6311-340c-8462-6a60cece08be | -11.09084 | -45.6509 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 251e65a1-8c59-38df-b5d4-d949f806b683 | -5.37428 | -38.28292 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| b003aecd-a063-3c42-9e61-13a1fe7fdb39 | -8.5379 | -54.59615 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 015570d4-f393-32e2-890f-d2980b4ba296 | -5.96465 | -40.94393 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 68ccf9b5-8173-3a9d-b3bf-69a94905bb25 | -5.72768 | -41.7463 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 984062bf-a2a4-390b-8267-582dcb0cdc83 | -5.17076 | -45.32116 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a0d395a6-1b54-3f03-b235-a595df4823ff | -10.952 | -45.3846 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6dea6f82-c614-32c6-9c24-4f4bc638966b | -17.01233 | -45.91211 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fb3bea44-a5f2-38ee-859b-b7a353eebb7c | -9.97091 | -43.55221 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c6a2cd0-a5bd-3f60-a18e-512f2ae935d4 | -7.0276 | -45.42197 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e18b7dd6-872e-3050-88c6-061b099d2c4d | -6.05349 | -53.48979 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 194406d2-f2ab-3c46-8ee2-199f87a05767 | -6.22595 | -52.8388 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b341a885-af2a-3936-9abd-139463bfacab | -8.75407 | -44.15165 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 274164b1-2153-3215-ba33-a058c57c3abc | -3.74396 | -44.70191 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b71589e8-46e4-33ae-9eb4-83715bba91c9 | -4.99166 | -45.37416 | 2026-10-07 16:37:00 | NPP-375 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e220f535-e45c-3dbf-bf83-4bd50dcaa867 | -9.86756 | -45.7468 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ea7330e9-0ab7-391d-bae6-5e54bd66f00b | -7.02815 | -45.4256 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a455a3b3-88bc-3a3e-bdca-22dae60f8071 | -5.74168 | -45.05564 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a9de17c5-e704-3b21-a6c5-9b76199e0ebe | -3.73049 | -39.53099 | 2026-10-07 16:37:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4b807455-b974-3c53-abd1-2ed888a1ace7 | -7.35464 | -37.37306 | 2026-10-07 16:37:00 | NPP-375 | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| bc057e82-a17d-38ca-b2a9-81fe68fba9d0 | -5.68802 | -53.48938 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 848baf47-f1d6-310c-a161-e554e0687a5f | -15.64036 | -43.29582 | 2026-10-07 16:37:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6be8ed32-03df-3ece-b706-65599b9a54dd | -7.72043 | -45.43558 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fc3df7f4-7dda-3832-af28-5385d3924b15 | -6.97904 | -45.12418 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5773516e-23c3-3cc9-b2e1-21f8a507e848 | -7.43937 | -44.46613 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7881514c-228f-3e20-85d3-015cd3c6df29 | -11.17118 | -49.47736 | 2026-10-07 16:37:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README201.md)
