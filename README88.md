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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04da72bb-0060-36f1-879d-45fb6d897457 | -5.65838 | -39.19976 | 2025-10-28 11:38:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| df4203a1-3305-3a00-b321-cc735a16c853 | -9.53052 | -46.97758 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 90dcb1d5-c770-37fb-a52c-eec824da3d6c | -10.49659 | -38.48074 | 2025-10-28 11:38:00 | TERRA_M-M | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| f7979229-c1da-39a7-9bf2-375c6fcc92d0 | -6.40913 | -38.29441 | 2025-10-28 11:38:00 | TERRA_M-M | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 981dc25f-1155-30c0-94b2-9d3af7292d3e | -9.39334 | -42.6697 | 2025-10-28 11:38:00 | TERRA_M-M | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 4c22d918-bbb3-37fc-9019-a289e00e26de | -6.7009 | -42.04199 | 2025-10-28 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 075c4bce-d844-3d67-8fe7-13772b97f11c | -9.54712 | -46.9742 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b9a3b1aa-6ac4-3aa8-9417-0e4a3eefea29 | -5.9014 | -38.67439 | 2025-10-28 11:38:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 333a6e61-5aa1-3f77-9b65-ef9a573e88ac | -9.53208 | -46.9719 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 255.8 |
| f865e0d5-9fe0-323e-9487-15cd25f500ad | -7.97775 | -46.75199 | 2025-10-28 11:38:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b6e20766-5aa9-328e-99b0-20151b37848c | -8.65162 | -45.27853 | 2025-10-28 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5b3dec32-dae0-38b6-842f-5b2d56072ca9 | -9.53549 | -46.94907 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 1bc4b92f-3d03-3a3d-a5cd-0b9b143690c4 | -9.48184 | -46.90483 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 58dc4746-d628-344c-9909-92fae890e76a | -7.83462 | -46.41228 | 2025-10-28 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 615a4c9a-901f-37f5-a778-c7107aa506a0 | -6.24076 | -42.56488 | 2025-10-28 11:38:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| f4bd5c6b-3925-3550-83eb-a23c869abb47 | -7.9556 | -45.46313 | 2025-10-28 11:38:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 35.4 |
| d4d428b8-5814-3d46-984d-99d2fd4957f0 | -6.69025 | -42.04027 | 2025-10-28 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 689355cd-e28d-3b0e-9324-e25e804e831e | -9.27865 | -40.73932 | 2025-10-28 11:38:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| afaa77c2-de39-3bdf-a3f8-85840bb71bed | -7.92141 | -39.56674 | 2025-10-28 11:38:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8c542931-f950-3c14-863b-a9c7806cf2f6 | -6.59026 | -42.68947 | 2025-10-28 11:38:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| fd222f72-f06a-3359-90bd-0b0c51f250a7 | -9.53681 | -46.94357 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 46ca371f-eccd-362c-b5e2-08d55da66ba6 | -7.81462 | -46.44401 | 2025-10-28 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 2817a41a-98ea-347c-97e9-a2aa0dd31c76 | -9.48344 | -46.89811 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 1f73b96d-8f5c-36a7-87f6-7aaf07bfda39 | -6.42458 | -42.33337 | 2025-10-28 11:38:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| c6a6f722-5a1a-35e8-b472-6aae14faef2e | -6.15474 | -37.74826 | 2025-10-28 11:38:00 | TERRA_M-M | ALMINO AFONSO | RIO GRANDE DO NORTE | Brasil | 2400604 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 593f2456-ac9e-33ba-b39b-04bb90062589 | -7.80981 | -46.47279 | 2025-10-28 11:38:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 4273fc3d-73d1-335b-b910-19015055041c | -5.75611 | -38.97339 | 2025-10-28 11:38:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 35fef981-bea1-351a-9afc-abcfe77b65b8 | -8.03781 | -38.52013 | 2025-10-28 11:38:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| e0a4df82-2cc3-34c9-97e6-8214d5fcad75 | -10.55398 | -43.22311 | 2025-10-28 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| ed8717ca-47f5-3aac-867a-ffea5a12d1e2 | -9.80171 | -47.00696 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| a851b5ca-6bda-3f13-8a59-6a77c0b42b6b | -7.60501 | -43.58445 | 2025-10-28 11:38:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 24c1a922-d255-31e2-a1a4-c16e30990d8e | -6.07031 | -39.47388 | 2025-10-28 11:38:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b65d3004-e815-3f21-b4b2-ea3ef12ea648 | -5.39997 | -39.51091 | 2025-10-28 11:38:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 8add0ecb-8d6c-318b-b192-69be6b15307c | -10.56265 | -43.23904 | 2025-10-28 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 5bcb94b9-2647-35fc-88b0-f07564ad9857 | -7.76096 | -44.69555 | 2025-10-28 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b8faf4fc-b625-36e2-a4ff-fe7c459db41e | -9.96608 | -47.11502 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 096419a5-d926-3a0a-8023-0307a8e02944 | -5.79832 | -38.30021 | 2025-10-28 11:38:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 37686e17-2137-3003-b8f8-c55da852c68d | -5.75747 | -38.96418 | 2025-10-28 11:38:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 4f8c0123-1d31-39ff-9fa0-5a48437b9778 | -9.89762 | -44.89909 | 2025-10-28 11:38:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 688738b7-10ab-323d-ad96-b8fa4cc3da4b | -10.55172 | -43.23721 | 2025-10-28 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 33.2 |
| ec3d9b6b-45ff-37b4-b406-c6b0e8419d29 | -7.74469 | -44.71408 | 2025-10-28 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 7ffb9f67-0658-3304-a116-faf139163eec | -6.76752 | -38.30687 | 2025-10-28 11:38:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ad7ec26d-fc93-3ff1-a5c1-7a5374cc0e58 | -7.74796 | -44.69377 | 2025-10-28 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 43c2af9c-1fbf-34a7-bf4b-668092d0b3aa | -9.04706 | -46.9437 | 2025-10-28 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 777d20fc-56b8-3185-8f73-8302eafac239 | -7.83418 | -46.41809 | 2025-10-28 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e11672b2-2696-39c5-815d-eb52b1f80030 | -6.12039 | -42.44458 | 2025-10-28 11:38:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 1283cfac-2ea7-3ac9-a48a-d273b9f55bfa | -6.4894 | -42.21961 | 2025-10-28 11:38:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 5b131e1d-7346-38ee-85d5-8a39f8e44e78 | -7.8107 | -46.46686 | 2025-10-28 11:38:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 243.4 |
| 8686b7eb-e3ef-30fe-8445-018f19b45770 | -12.8299 | -47.7254 | 2025-10-28 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 12d0548d-6be3-3452-8561-7818fc680a5b | -12.46197 | -42.52008 | 2025-10-28 11:40:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 983fbc4a-7b45-3e8b-876a-99fbc1a903c6 | -12.52225 | -42.46289 | 2025-10-28 11:40:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 11b29deb-5ae1-3cb1-940b-af7a894fe51d | -13.22869 | -44.37494 | 2025-10-28 11:40:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 56df1bb4-9696-31ca-a3c6-48e357e1377c | -11.68861 | -39.80953 | 2025-10-28 11:40:00 | TERRA_M-M | CAPELA DO ALTO ALEGRE | BAHIA | Brasil | 2906857 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 735f43f8-bb24-337e-96ed-3a28d8e00993 | -12.55125 | -44.93232 | 2025-10-28 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 5ef4ea0d-26dc-3f27-b8bf-34ed0b020f17 | -14.22958 | -43.47644 | 2025-10-28 11:40:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| cdf7a76c-94bb-3d58-bdb8-7e80a08047b8 | -12.90712 | -43.3534 | 2025-10-28 11:40:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 19880ff5-b30a-3ede-a0e1-d09e0d0df5a2 | -12.38895 | -40.56981 | 2025-10-28 11:40:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| db1762ed-58e6-3651-b5ca-3879473e6a56 | -14.83671 | -42.62578 | 2025-10-28 11:40:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 62b17e19-873d-38c3-ae33-bea5f4ab243b | -12.08838 | -45.66957 | 2025-10-28 11:40:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 50d1e75a-b24f-3804-b511-bcc897eefd30 | -12.89653 | -43.35167 | 2025-10-28 11:40:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| bb8338b1-2d8c-3c6a-89db-200fe9f1b9f4 | -12.5555 | -44.93994 | 2025-10-28 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 27589706-a6c6-3f85-9fd3-5530cb293ec2 | -12.06474 | -42.56577 | 2025-10-28 11:40:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 63a8db10-e9b1-3a74-9bfb-0a10c09f4544 | -12.6761 | -40.99399 | 2025-10-28 11:40:00 | TERRA_M-M | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 084d4d06-c3a3-3628-a2f5-7bb18a0ae772 | -12.30016 | -42.69854 | 2025-10-28 11:40:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| e8e4d8f3-b2db-38f8-a653-8c71e57875c2 | -12.09395 | -42.76703 | 2025-10-28 11:40:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| c0b5d31f-1240-3516-b357-6248f509c065 | -13.9644 | -43.26857 | 2025-10-28 11:40:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 8f313380-acd4-3acf-9e4e-a5e8ddcf5ea3 | -12.2982 | -42.71085 | 2025-10-28 11:40:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 82d9eb44-17c2-310a-bf32-1d5fa54fa308 | -15.19485 | -47.2149 | 2025-10-28 11:42:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| f420c164-f4e6-323c-97e1-2653b780ab35 | -19.38085 | -43.63263 | 2025-10-28 11:42:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f8e3d5e5-1d05-3399-ae16-2f48415e8e02 | -17.20242 | -44.448 | 2025-10-28 11:42:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 08164cc8-265c-3fb0-bc2b-08e560dc270c | -15.48371 | -43.59008 | 2025-10-28 11:42:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e3a7441f-b772-3195-aeb6-e544a3e8ef40 | -19.79608 | -44.4902 | 2025-10-28 11:42:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 0f8dc723-cdf3-3bf6-9dd6-5ae5fb915934 | -14.53482 | -47.99659 | 2025-10-28 11:42:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 9092df84-5785-391c-ae0c-449139c25fb8 | -19.31955 | -41.82835 | 2025-10-28 11:42:00 | TERRA_M-M | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| b84382ab-0b98-3c0d-9f46-e4485c007667 | -18.619 | -43.31662 | 2025-10-28 11:42:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 941c35cf-5551-3f62-8239-5366e2520cae | -16.26098 | -43.61646 | 2025-10-28 11:42:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| b851fae0-a73c-379b-a4b8-fbeb95cd91f1 | -14.53489 | -47.99038 | 2025-10-28 11:42:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| dcdcd05d-e58b-3f89-9a43-577d4c25a437 | -18.19755 | -42.15819 | 2025-10-28 11:42:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 555c83ba-e9d2-3a2b-82a9-97fdadfec76d | -19.80627 | -44.49206 | 2025-10-28 11:42:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 645805bc-1db9-3315-a33c-853caefef704 | -15.48578 | -43.57736 | 2025-10-28 11:42:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 8bbaf8ab-1d04-350e-903c-ba02222f8b39 | -12.8299 | -47.7254 | 2025-10-28 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 28c671c4-2b6f-3f84-a272-eb512dca33eb | -12.8299 | -47.7254 | 2025-10-28 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2437c5a3-dc9d-3cba-a4a5-133a7d401767 | -14.1206 | -44.0222 | 2025-10-28 12:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e0df0ca7-d222-392e-b6eb-9f4817893360 | -12.8299 | -47.7254 | 2025-10-28 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a1ac979b-3890-388f-95d1-b3799ae56697 | -13.2262 | -47.084 | 2025-10-28 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b0b6cebe-7f26-31e3-b069-f2fa1428330d | -14.1206 | -44.0222 | 2025-10-28 12:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d5e4c951-3bda-3bf7-b05f-f45129b66a20 | -12.7786 | -47.3752 | 2025-10-28 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 3cf12b9e-5f7a-3801-b395-a3d698fecc9a | -12.8299 | -47.7254 | 2025-10-28 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| e31ad14f-6b80-300c-b767-1ba31e5cd2ed | -14.762 | -44.9636 | 2025-10-28 12:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 956d1542-2230-3794-94f5-bfb8d94600cd | -13.9623 | -43.2649 | 2025-10-28 12:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 43a1ff98-c803-30b3-a2bf-5512e7ce7fa4 | -12.8303 | -47.7031 | 2025-10-28 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 0e25936c-4d56-3df9-9f13-67e4b6ae8c53 | -12.8299 | -47.7254 | 2025-10-28 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 3f1444fb-1c82-3bd2-b082-0fb03ea1b689 | -12.7786 | -47.3752 | 2025-10-28 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| dfee6b7d-31e6-3967-b02a-f5e4c2d64c8e | -14.1206 | -44.0222 | 2025-10-28 12:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 817de2cb-0756-33ef-95aa-c7c74b154f12 | -14.762 | -44.9636 | 2025-10-28 12:40:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c363e804-4473-33da-8a69-3388f7878092 | -14.5054 | -47.8951 | 2025-10-28 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 42bb1bd9-e21e-3f81-a360-fd78c18285a6 | -12.8303 | -47.7031 | 2025-10-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| fc052cb8-5275-3069-82e8-cc22cffeec47 | -3.5831 | -43.634 | 2025-10-28 12:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 5d958449-64eb-34f3-88e0-b1ae759ee85d | -3.7074 | -41.58 | 2025-10-28 12:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| ae50e1fa-20ea-3e9c-9d50-7913bc6aa165 | -12.8299 | -47.7254 | 2025-10-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |


[Clique aqui para ver as próximas entradas](README89.md)
