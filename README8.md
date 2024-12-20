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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e2cacce-94c0-3c62-b163-012122389558 | -2.70058 | -46.13859 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5587fb70-340d-3a04-8cd9-241b4222d2c9 | -5.98177 | -41.60229 | 2024-12-20 04:10:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 795aeb32-34c9-3f6b-a60e-a6b8046da873 | -2.7013 | -46.13402 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5451d0e2-16fc-3694-a5f2-df9327e1a301 | -3.81151 | -45.13021 | 2024-12-20 04:10:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7126ba5a-71b6-3f5a-a22e-d62d1740073d | -2.76193 | -45.55988 | 2024-12-20 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfc57aba-dd46-34b1-8e4d-74979fd20514 | -4.38603 | -42.14745 | 2024-12-20 04:10:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 37f5f46b-14d1-3409-be34-e6585418eae1 | -6.03994 | -44.0413 | 2024-12-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7c3ca367-58c9-385e-bd52-30626a85ecc5 | -7.25105 | -44.71174 | 2024-12-20 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85939568-8da1-3ebb-ac40-97cf90bd7c3b | -6.6782 | -41.03518 | 2024-12-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d6387661-a3f0-3591-a46d-cc01c3445197 | -11.44584 | -44.6722 | 2024-12-20 04:12:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33d1fc6f-a9e7-3c5b-8279-332893f429fc | -6.68164 | -41.03571 | 2024-12-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cd264d68-a4c5-34c7-a407-e99865b59c84 | -6.1046 | -44.75555 | 2024-12-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12296cd6-a8f7-39cf-8a2b-a92ccf09aada | -6.11488 | -43.95177 | 2024-12-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31a1c4c0-8f2c-3e19-9da5-726e064228ee | -7.45438 | -52.87672 | 2024-12-20 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 5b1620b1-ec67-3a8c-bf35-1fd6fd639c45 | -6.39078 | -43.50096 | 2024-12-20 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a68fa99b-6c7d-3da1-9d6c-915a30d4ad85 | -6.11544 | -43.94825 | 2024-12-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1757b2a-7d85-35f4-bd90-ada1ae355e7b | -10.45746 | -37.12441 | 2024-12-20 04:12:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c557f33a-8888-3b19-87c9-9d0ccda1b830 | -6.23914 | -46.17572 | 2024-12-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8e0884c-c316-3911-a06e-cb55a8bf154a | -7.22159 | -45.30671 | 2024-12-20 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95ef614b-236f-39b7-81ac-2abe9f4b5a2a | -7.38302 | -45.56257 | 2024-12-20 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6673a6bf-efc5-3a7d-9837-b75ef4c189bb | -10.45294 | -37.12371 | 2024-12-20 04:12:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4c1cc780-2277-3aa5-be24-9ad36ae006c2 | -6.27911 | -46.13522 | 2024-12-20 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d5af57f-f04f-3dfa-957a-e10725b75be4 | -6.16226 | -44.42006 | 2024-12-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30fc6195-6330-3d86-a3aa-bbfa0aff5ae3 | -7.98726 | -43.13243 | 2024-12-20 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ac250e35-5360-346e-9bbd-3b5930735f86 | -8.12198 | -43.13982 | 2024-12-20 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e9398ed7-2717-3723-b49a-fcdd972ee185 | -7.22793 | -40.3581 | 2024-12-20 04:12:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bc5e04e1-9aed-31d7-a424-e2f1a900f4c0 | -11.44252 | -44.67166 | 2024-12-20 04:12:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 566a1e32-a53c-39a2-bbb0-2ac8e7efa2f0 | -6.22775 | -44.83925 | 2024-12-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cb96d01-6721-3fdd-b71d-75df9fff3fbd | -5.89663 | -45.56431 | 2024-12-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc0df944-a5cb-333c-89f1-11549a7d2c45 | -6.10802 | -44.75608 | 2024-12-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbf33649-8a88-3d22-9744-f2f4fbbc3955 | -6.39133 | -43.4975 | 2024-12-20 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac341a8a-ce96-3ea3-a45f-b690e4c22aac | -5.8931 | -45.56376 | 2024-12-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cc95a40-2145-3944-a136-b4d78e171b8a | -6.16168 | -44.42366 | 2024-12-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f6d04cd-8326-32ff-afcd-f953bb55ccb5 | -6.04329 | -44.04182 | 2024-12-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c917d27b-b984-3cf1-ae8a-88979753ae38 | -9.15868 | -43.13203 | 2024-12-20 04:12:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00f098ae-d085-331e-9c48-a9a7d0aad6f2 | -6.12433 | -43.9569 | 2024-12-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53ad66c8-0e6c-37cb-9a68-afefe4f74b06 | -10.15289 | -42.16556 | 2024-12-20 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| cf8e1000-2993-31ae-ae57-1cfcf54b511d | -6.68044 | -46.38614 | 2024-12-20 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63b96e28-bc55-3535-bb1d-8b0463f6dddb | -9.04246 | -40.03144 | 2024-12-20 04:12:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eba92686-d2f3-3802-a1ca-da5f3ba87072 | -6.6822 | -41.03197 | 2024-12-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c5bf1359-c1a5-382d-863a-004724783b99 | -10.22333 | -42.18769 | 2024-12-20 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee502acf-d2a7-34ee-93f0-e56b5a754ccf | -6.4934 | -41.60331 | 2024-12-20 04:12:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| c29e69e1-eb5e-3c45-92c2-b20063cff9ec | -6.116 | -43.94474 | 2024-12-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01572b4a-ab57-3613-ae7e-bbfc42f44937 | -6.22434 | -44.83871 | 2024-12-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76373758-6c6e-3aeb-95be-b8d16dfab2da | -10.14949 | -42.16503 | 2024-12-20 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| eef553b1-8551-33b6-8151-980220675edb | -9.76087 | -42.00459 | 2024-12-20 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 01287179-848a-366c-bb25-e7507231fe8a | -6.98646 | -47.0819 | 2024-12-20 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92608757-40b2-3480-91cf-e2feb6e7f625 | -6.12602 | -43.94634 | 2024-12-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a5c77d0-637b-328c-abfc-86f43e2d7d79 | -10.15233 | -42.16925 | 2024-12-20 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1faf4036-16e2-3682-b1ec-cd875820e9bb | -10.14157 | -42.17136 | 2024-12-20 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3868d423-afa8-3ac4-be38-1b67ee53b9ae | -7.25163 | -44.70812 | 2024-12-20 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d454cfd-2a0a-30de-a52a-6da68423280f | -6.06588 | -46.13358 | 2024-12-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d49eca52-f210-3d72-bce0-a2f5e5d97d69 | -6.11266 | -43.9442 | 2024-12-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a23955c-3049-3a38-a244-d1c08352b8a0 | -10.14893 | -42.16872 | 2024-12-20 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 70e70fd6-c73e-3be2-9f73-98e9ed8d5b15 | -6.12767 | -43.95742 | 2024-12-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5df9bb5-cd16-36d3-ad38-29da2c26db10 | -12.41445 | -43.80406 | 2024-12-20 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a4a93a56-075a-346c-8b61-93e80b13811e | -17.75297 | -42.89526 | 2024-12-20 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1165c99c-68df-3033-865f-894b6c8b7806 | -12.67109 | -43.43892 | 2024-12-20 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6434137-6c32-30c8-96c6-4e9358d75f96 | -12.86545 | -43.74108 | 2024-12-20 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1da3de21-eae0-3c95-b7db-3c6a6d759acf | -15.30719 | -43.13162 | 2024-12-20 04:14:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 629bab69-6b3d-38f4-bb50-b17d271848b0 | -12.41168 | -43.79999 | 2024-12-20 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c0935fe-a8fb-3b58-b1d7-0f7220d5031a | -12.41113 | -43.80353 | 2024-12-20 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b2ac17c-46cc-32fd-bf4e-d63fd5233fe6 | -19.83748 | -40.08275 | 2024-12-20 04:14:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 53cdb70d-f3a3-316c-9cb7-29e03212b35f | -12.8649 | -43.74465 | 2024-12-20 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ec0170b-42b2-3880-aad8-dfad11ea55ce | -16.14739 | -40.368 | 2024-12-20 04:14:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 47a4f79f-ae07-3f1c-a498-2313f6e328c3 | -11.99037 | -57.20545 | 2024-12-20 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83221af5-aaaf-34fa-872b-b41905ca57ce | -20.34787 | -40.36295 | 2024-12-20 04:14:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7d44dc59-72f0-3e50-94fc-8f6c81a44f8f | -12.33216 | -43.67806 | 2024-12-20 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9943e35e-45c4-39ff-82ee-88a717bc7d93 | -12.32244 | -43.43193 | 2024-12-20 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8011817-ac54-392c-8c30-7ede2e0a6071 | -12.15395 | -43.49293 | 2024-12-20 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dd0ac4a-f47d-31ee-9d36-0ace4c3229cb | -12.67164 | -43.43533 | 2024-12-20 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ebdb1b4-e617-3699-9011-0f3f6eb1b85a | -12.33548 | -43.6786 | 2024-12-20 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6a4e8cc-6167-3268-a39a-25dcf833f952 | -13.88158 | -43.07682 | 2024-12-20 04:14:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a5632c91-43a9-3f3a-9d13-612f97a22af6 | -14.72921 | -42.42604 | 2024-12-20 04:14:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9a4bee61-d9af-380d-843a-d012db433bfd | -19.84925 | -43.84538 | 2024-12-20 04:14:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27dbba92-87b9-3886-b88c-965a3a277d80 | -15.19256 | -43.73425 | 2024-12-20 04:14:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 516d4c62-f7e7-30f6-b814-d9b76c7ec9ec | -14.23507 | -42.22388 | 2024-12-20 04:14:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 68b2172e-468c-3b2a-8943-d68c01a48087 | -12.33603 | -43.67504 | 2024-12-20 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8940cf5-bb85-304c-b144-251e6a6cd349 | -12.86822 | -43.74518 | 2024-12-20 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 465424a0-60ea-3aa3-bff4-f49f4cc2efdb | -20.53 | -43.97261 | 2024-12-20 04:16:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 0733f56e-7102-3092-aeb8-e58dfa68cfad | -19.11893 | -53.45763 | 2024-12-20 04:16:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ec191ca-6a40-3f8c-ae75-c19c2dd69f9f | -20.89989 | -47.38255 | 2024-12-20 04:16:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3b08fa9-e287-3942-8207-bc9eae3e0816 | -19.12069 | -53.45547 | 2024-12-20 04:16:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fef8d711-2a3c-3565-897c-979dc21c99f6 | -19.05114 | -52.26979 | 2024-12-20 04:16:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30a63f32-7fce-3a36-8071-03193ae6868d | -21.2982 | -49.0199 | 2024-12-20 04:16:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1dac808a-8c9e-37dd-86dd-07b9862cfe59 | -23.40536 | -46.55811 | 2024-12-20 04:16:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6e5e6b81-009f-3232-a4de-46e06d751a11 | -22.85523 | -42.98035 | 2024-12-20 04:16:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1938618e-9914-31fa-8a6e-6be60e14dabe | -19.45698 | -51.60418 | 2024-12-20 04:16:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7295c431-954b-306b-9bf9-e67b30d4c295 | -20.99225 | -49.02317 | 2024-12-20 04:16:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.7 |
| e007d0fc-83dd-38b2-8417-27e840bbea85 | -19.37894 | -54.17461 | 2024-12-20 04:16:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 019bb8dc-2784-398f-89e1-aad2feb643ed | -23.7057 | -46.47908 | 2024-12-20 04:16:00 | NOAA-20 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f64c1c7a-e38a-3623-9934-0cb2bc57329f | -20.97239 | -49.76057 | 2024-12-20 04:16:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bd51b2f4-6e74-3b5f-a193-84d5bee1d6db | -20.97599 | -49.76129 | 2024-12-20 04:16:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| df3b8780-abff-3840-9e54-5ebf5f9f9f74 | -19.12528 | -53.45649 | 2024-12-20 04:16:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bdf8680-4b4e-3777-a243-527bd8c82268 | -19.1197 | -53.46049 | 2024-12-20 04:16:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc776698-df14-3a79-8112-6830013d4d61 | -23.58696 | -46.3217 | 2024-12-20 04:16:00 | NOAA-20 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a855a7f4-2564-37e8-88ad-3efee62c80ad | -20.77828 | -49.8586 | 2024-12-20 04:16:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 96be9c57-1177-3d13-a965-e9a3d0e9823a | -23.58638 | -46.3255 | 2024-12-20 04:16:00 | NOAA-20 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| bace0f93-9603-3682-9b1a-2de490062ee7 | -21.3375 | -49.39798 | 2024-12-20 04:16:00 | NOAA-20 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f7a4cae8-6ba1-37ce-b885-ecfc1dff43ed | -20.99487 | -51.79279 | 2024-12-20 04:16:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README9.md)
