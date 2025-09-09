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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66729ada-a12e-33fe-a1e4-296be267b930 | -10.0737 | -48.09454 | 2025-09-09 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba62a614-3826-3610-9b33-37f275f793d3 | -9.10256 | -49.51736 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26fcc223-3f39-3aef-b374-f52f25901cd8 | -9.46996 | -60.48123 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9d64e07-b00f-3f23-8a2e-6d30418ebe0d | -8.06539 | -48.652 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20c6ee6b-bd22-340f-99c9-6f497b12b1f5 | -9.70872 | -46.8146 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f9013ff-4b86-34c5-bb27-769d3d1cfc61 | -7.70793 | -44.74975 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aad1583d-b58d-394f-9f43-8fd560f87c36 | -8.08715 | -54.75667 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e117c1a-cb70-3af9-a3c4-9fcf7c28a3ab | -8.85982 | -47.23275 | 2025-09-09 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f6c5c59-e28c-3a31-aa94-79a5fe823095 | -19.89669 | -48.20784 | 2025-09-09 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 93f00385-3cc7-3c6f-a053-59c59f1e1c8e | -14.53711 | -48.75544 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 03568eba-1cee-31c0-9926-7ebae696487b | -17.28112 | -46.74317 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f96a7fd4-10cc-38d7-b604-c620f1b306ad | -19.89787 | -48.19934 | 2025-09-09 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1f297bb-51f2-36c4-a3f2-4f56dd76e30e | -15.75987 | -53.53075 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9e4031f-541e-364d-a24f-a4d15347efa3 | -15.7485 | -53.52596 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 995c635e-184c-3704-be08-b8d8a9904092 | -20.03191 | -48.53331 | 2025-09-09 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5ba4dadf-5d2c-3a15-9e3b-54179bc81bf3 | -15.53122 | -48.39699 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 55972753-43f1-3d8c-ba8e-a21a12686333 | -15.53749 | -51.70738 | 2025-09-09 04:36:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aadc543c-e968-3cd5-ab44-b235e4056985 | -15.83008 | -52.25613 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 436c81ac-0457-3601-a14e-a4232acf2ca8 | -15.2617 | -53.80319 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf78405b-38af-3d8f-92c8-93389efa20c2 | -19.89728 | -48.20359 | 2025-09-09 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75aa47a6-2cb9-32b0-8771-72a2fae626a9 | -16.43064 | -49.28459 | 2025-09-09 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4da4bfc4-6d48-367b-b4b8-a277b57d9d1f | -17.26512 | -46.6939 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 517c7019-963e-33fa-8df6-fe99919360d3 | -16.06779 | -50.48743 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 888b835b-264d-3f5d-bf70-ec4dbfdc2c5a | -17.28678 | -46.70174 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 830938d0-306c-3f4d-8fa2-9cef3c8e6329 | -16.96148 | -49.6793 | 2025-09-09 04:36:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffaafbcc-2699-3040-b4b0-ad7d80c9681c | -16.32663 | -52.92187 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 845ca020-6f37-3bad-a876-fbc05430b4a4 | -15.52555 | -48.3884 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a92df1d7-cd82-3a1a-929c-22af2d345af5 | -16.69366 | -48.06494 | 2025-09-09 04:36:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e462db72-52e3-3e66-8eb2-fddcbffcc235 | -14.55515 | -49.17094 | 2025-09-09 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca979a9d-be47-3c19-b764-15f763d0ef1a | -17.26756 | -46.73182 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44d78297-a6a3-3e38-b9e1-062c3f66070a | -14.54155 | -48.74874 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbc40680-823f-3ca2-a2e7-e1c1b4e0e06b | -15.24481 | -53.7907 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c5914ad-d7ca-3159-899d-31640f13b411 | -18.34484 | -49.3817 | 2025-09-09 04:36:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1e2a0a9a-1d91-33f6-9ef2-81911bf09d30 | -15.21751 | -44.03884 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 712a8d5c-7b43-3085-b6e9-f468b245c3a0 | -18.76869 | -48.19413 | 2025-09-09 04:36:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ddf11e69-5a6c-3fc8-855a-5e07699853ee | -18.82567 | -49.68401 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d5a7b090-1372-3bf4-96a5-7c3f9054ba77 | -15.25908 | -53.81084 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07b58f12-9269-3549-8842-b40634163cc6 | -20.74716 | -43.22976 | 2025-09-09 04:36:00 | NOAA-21 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fcef88a4-c487-3a61-96ce-c51850291578 | -17.15851 | -44.44905 | 2025-09-09 04:36:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abda78a9-1524-3067-b378-4f8c063ebd80 | -18.01381 | -47.11297 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a2417ce8-4843-3d54-9c51-4b63d70aa632 | -18.47384 | -49.55849 | 2025-09-09 04:36:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2c1eabd-4926-3d9a-b451-c8161c3c88dd | -15.2677 | -53.79029 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef547718-3ee4-36ca-98d8-0cf6cb86d1a0 | -12.87869 | -62.10369 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dbd52936-ac64-346b-acb8-a5d019e9687a | -18.82177 | -49.68716 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fcc10c10-7118-362d-89ca-8140b87684f7 | -14.99634 | -48.31821 | 2025-09-09 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa9d9bc9-7d43-3fa7-9d77-04f406a36ec9 | -19.48498 | -46.13802 | 2025-09-09 04:36:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77f839fc-2222-3eeb-9763-a8f1ab2ca0dd | -19.83007 | -48.16868 | 2025-09-09 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f2dea11-fa23-31af-9aba-17b629491dce | -20.17149 | -44.79587 | 2025-09-09 04:36:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6700bf65-408a-3859-9f3f-f5a21c93213a | -18.02717 | -47.12444 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fb04df8-d7cb-3813-936d-4224adf10907 | -12.88099 | -62.0926 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 543941e3-bb40-3355-8800-4b5c27916fae | -15.81785 | -52.26617 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87e8ef94-e876-360e-be68-5af4c744bca9 | -17.67365 | -52.27 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5681e544-7080-309f-bf96-6da6a9b71733 | -15.13395 | -43.98111 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8c5d40a-5e02-32b1-95a2-b8be6c11f8df | -14.52485 | -48.74602 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfd7ff58-7cfe-308a-9d5a-471ba8ddd27a | -15.53288 | -48.38582 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f18e6c60-96a2-322c-a668-238cd150a97c | -14.36019 | -60.30778 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb46602d-9c47-3c72-b0ec-7534ad0e2af5 | -17.4127 | -49.12318 | 2025-09-09 04:36:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddf5a077-4270-39b8-ab2a-be3ea71059ea | -15.53799 | -48.39807 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5e1ebd34-c300-31e5-bcbe-fbe4fa57e9ea | -15.82061 | -52.27079 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77c866d8-238f-3e61-a374-72a1b7a9131c | -18.82902 | -49.68459 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c8ff02ca-a2a7-3004-aff8-23f8ae5f1f02 | -15.24101 | -52.37164 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 263ff9fb-8671-389d-bd4b-d5b188529975 | -14.71678 | -60.24485 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6d955a0-c792-3a9c-b3b5-c004cdde0416 | -18.03182 | -44.34435 | 2025-09-09 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5eac26e-7187-3134-92b8-948f64b23cbf | -20.03134 | -48.53743 | 2025-09-09 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 00ebe164-a3a6-3629-9249-119dee0e681d | -15.87084 | -52.34778 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceaec14f-e5ee-30c7-9d8a-35b9fecdb8e2 | -15.29418 | -43.37736 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 396f5d9d-0f51-3a23-b8cc-bd03138a2b16 | -15.503 | -52.76086 | 2025-09-09 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c6865c01-fce5-3854-99fa-1dd000df8df4 | -15.87012 | -52.20462 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2e42bb2b-5540-3ca3-86ae-3cbae7c31857 | -15.27174 | -53.80386 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6fb3009-7bfc-3d04-926b-93fa2350584f | -17.67552 | -52.25861 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8580d826-99c7-34d3-bef6-808e8e3c7da7 | -15.04577 | -48.10241 | 2025-09-09 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cce89afc-dc71-33f4-a9dc-cc9f3f3a45bd | -15.37573 | -46.43746 | 2025-09-09 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6d50700-3298-356c-8c4e-3dfd3656a9ff | -19.78847 | -47.99649 | 2025-09-09 04:36:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edf4d49d-1b14-38e5-a0e9-78fcd9591aa8 | -16.90099 | -45.81806 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5aec9db7-a113-3b94-b950-41e363cd271c | -18.02294 | -47.12798 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c20cc62f-2470-3252-b92d-fa8ff7e78e82 | -17.29357 | -46.70751 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 325012f7-6781-37d4-ab3e-1fcf0a794bbf | -17.30216 | -46.72763 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4daca3bb-1e6a-3abd-aca6-645fdd371812 | -15.2477 | -52.35282 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d323f85-b85b-395c-a021-ba0e901bf9d9 | -19.61053 | -46.09203 | 2025-09-09 04:36:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72639640-5707-34dd-966e-7c8b545ac653 | -15.26539 | -53.80389 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c986727b-911a-3d07-87d3-8cc551abaec4 | -14.99579 | -48.32193 | 2025-09-09 04:36:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48000592-b19b-37c4-934b-e46ac06528cb | -17.28986 | -46.7069 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21bc7a08-5b87-36ea-95bc-bc72b419821c | -15.82661 | -48.94471 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 583d0502-b52e-324b-8f41-5074eb0f21bb | -16.53751 | -51.76041 | 2025-09-09 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d33be839-cf64-3e99-9779-54501e8d241c | -14.70172 | -60.2613 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfebd0d8-c98b-3a49-bc40-92d61b519e46 | -16.28661 | -45.68541 | 2025-09-09 04:36:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 561836aa-b1b6-30cf-b9fb-213623712473 | -14.99836 | -48.0213 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5cf0f38-96d7-3376-9c26-305049390b17 | -20.458 | -48.06265 | 2025-09-09 04:36:00 | NOAA-21 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ab2c6cd-d306-34eb-be22-0f8aea16359d | -12.90363 | -62.08188 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1ac18b48-70f9-3485-9bac-8b334a6dc2d0 | -15.77679 | -56.41537 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe5ab491-b2e4-3df9-9887-619811da3e68 | -15.53568 | -48.36691 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3ea7d9f-2c00-3c92-ac8e-18fe0da4b592 | -18.34148 | -49.38115 | 2025-09-09 04:36:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8fa3f3d3-fa9f-3b45-92e2-387321f5d4eb | -12.87109 | -62.10785 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c739e7d7-cfce-3d6c-a16d-0b01d175b7ef | -15.7356 | -53.58418 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2225c3e6-26dc-3f13-b17e-6c112bc11957 | -15.25879 | -53.79796 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c93543fd-5b44-36c2-b504-621c3a198d19 | -15.55206 | -48.37354 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 808bdfe8-3ec8-3799-8b39-d9a3c0f9f632 | -16.88903 | -45.75942 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64a44f37-9ba4-338d-8b3c-923d7f97392d | -16.07061 | -50.46956 | 2025-09-09 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b6a4e4d-1d4f-323f-a5e3-770a650927d0 | -14.37682 | -60.3007 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8562383e-e623-3a20-86c3-b96489a5160a | -15.53907 | -48.36747 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README48.md)
