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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e999125a-6a5d-332b-bffe-b1d7bc4b9dc9 | -2.59594 | -49.82055 | 2024-11-02 03:47:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b288b1d-9ef1-33aa-8b90-2afbbbf4d554 | -2.55603 | -49.13234 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b735ddc-a5da-35e9-9631-4888e52871d3 | -2.52532 | -49.24397 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba191004-7da4-36f9-925b-a259f9a19296 | -2.5228 | -49.24197 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1e4f98cd-b507-3145-8a67-93107b3d4b7d | -2.51942 | -49.23607 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ebb4c06-71b6-3688-83aa-6e10fc9693f5 | -2.51831 | -49.24273 | 2024-11-02 03:47:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b8a7a7e-1654-3c93-a969-6405f2f1a27e | -2.49595 | -49.0759 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3f28133-0f39-3c06-9e9a-39362678869b | -2.49486 | -49.08239 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80dda79f-fd4d-33f2-bb7a-f5deca2f8d33 | -2.48902 | -49.07461 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a75f35d-998a-3e9b-bcac-92b3fbc58bcb | -2.48794 | -49.08102 | 2024-11-02 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1bd7db9-6989-3376-82ce-4c70e79be584 | -2.46539 | -49.79045 | 2024-11-02 03:47:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c73a953-0e66-3ddf-8e1d-f612bb37a05a | -2.45814 | -49.78927 | 2024-11-02 03:47:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42760657-a03e-3ec1-8cf6-207e3203102f | -6.00713 | -41.83598 | 2024-11-02 03:49:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 432af60e-4ed8-3b51-af35-6f023268a005 | -6.00302 | -41.83533 | 2024-11-02 03:49:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d077d075-ed5b-3ebb-b7b9-e5cb86974a94 | -6.33683 | -41.91952 | 2024-11-02 03:49:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f21ef507-6f32-3148-bbb0-9f9113417266 | -5.99891 | -41.83466 | 2024-11-02 03:49:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 862cceab-0df7-32cc-ac96-93171202cf3e | -6.937 | -42.80914 | 2024-11-02 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2e7c5439-29a5-3531-bfae-b99bbe73f47a | -5.92998 | -38.34883 | 2024-11-02 03:49:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 35944448-64fb-3fb0-ade1-2e3ce57bb061 | -5.48042 | -40.39522 | 2024-11-02 03:49:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 76859855-cc65-3718-a61f-2721b009fdba | -11.56787 | -42.18462 | 2024-11-02 03:49:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 16351852-2660-3c4f-8d55-bccb3c4a22ce | -14.03353 | -43.5634 | 2024-11-02 03:49:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 14f934e0-578b-3c12-8771-952eac53e81a | -14.03289 | -43.56702 | 2024-11-02 03:49:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c062d45f-7e25-3674-b4c3-591820932f7a | -14.0295 | -43.56263 | 2024-11-02 03:49:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43f9921c-2ebb-333a-8f73-7abbfb416591 | -13.87607 | -43.44102 | 2024-11-02 03:49:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 776fc342-e4e3-3376-aa34-6e2df9d6a40b | -13.70743 | -44.15709 | 2024-11-02 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2c0ab7e-5f4b-3ba1-8f61-9d643e90f624 | -13.65287 | -44.12217 | 2024-11-02 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5236e6e9-8861-30c3-8da8-b73a87b5496f | -13.65083 | -44.10957 | 2024-11-02 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2668679b-43e9-3420-9246-37eb54a8fe62 | -13.65011 | -44.11351 | 2024-11-02 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 467f7fb6-75c3-3864-b06d-09180edb70b7 | -13.64939 | -44.11746 | 2024-11-02 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9d8f832-a74c-3719-b3bc-cf56330276fd | -13.56545 | -43.98156 | 2024-11-02 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0abc99f6-cb43-37ee-a9a9-3a7eaa87b17c | -13.36313 | -43.92592 | 2024-11-02 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 725d67f1-792c-3316-bdb5-7ad542105072 | -12.78955 | -43.86216 | 2024-11-02 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a3d73b6-4edd-3e87-9d85-b9b31b36ca4a | -5.44143 | -43.25775 | 2024-11-02 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb3bca75-7026-37ea-87e5-d72c04b9538a | -5.43687 | -43.257 | 2024-11-02 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35056a29-38f2-394e-9f50-8665b122a904 | -5.31814 | -43.06979 | 2024-11-02 03:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e97dbfd-2e6c-3c13-9041-7147b34e86c8 | -11.96987 | -44.24194 | 2024-11-02 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6cf6da0-e3b5-3707-a215-e626b0bc82ff | -11.96551 | -44.2411 | 2024-11-02 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d585f4b-66bd-3052-8acb-e32ef048599c | -11.96499 | -44.24334 | 2024-11-02 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77072708-dcea-307b-bb08-a9af41b09aff | -11.96476 | -44.24534 | 2024-11-02 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b0950d9-a18a-31f2-995b-75fcbf3316a7 | -11.91297 | -44.18287 | 2024-11-02 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36c44c40-5a2f-3f0e-bc84-e9c027bea6f9 | -4.65869 | -43.81846 | 2024-11-02 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c0f4a42-07ea-37b0-8fe4-18ef0354c944 | -5.1465 | -43.8285 | 2024-11-02 03:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9049bf73-e81b-31b3-a1f0-4a66e8f895ad | -5.29229 | -43.33576 | 2024-11-02 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8ec4004-9f5a-307b-a37b-7df164c8f5f8 | -5.25693 | -43.34931 | 2024-11-02 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed0ff309-1837-35af-901c-21863fe67999 | -5.25314 | -43.34374 | 2024-11-02 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5de85a38-8935-3883-90fb-53aa9196597f | -5.25234 | -43.34845 | 2024-11-02 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dda925b-9704-3500-a57e-7f49d56bc5f6 | -5.11487 | -43.96072 | 2024-11-02 03:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfea13f0-742d-3146-8263-c5cf42a4126b | -5.31289 | -43.07347 | 2024-11-02 03:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ca324e39-4028-31f2-962d-22d9fc9f7d0a | -5.46873 | -43.17699 | 2024-11-02 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac5ab328-55ec-36f8-b0a1-f52a1bdfda1e | -5.31739 | -43.07424 | 2024-11-02 03:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47ae16a0-5222-3e94-8ddd-e80569a1878b | -6.47494 | -35.49324 | 2024-11-02 03:49:00 | NPP-375D | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7e9cae1-76c4-38e2-b19f-1901475185f7 | -7.67067 | -35.1392 | 2024-11-02 03:49:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 937a33c3-43e6-397a-9005-85f7ae53635b | -7.6701 | -35.14292 | 2024-11-02 03:49:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b77c0cc6-fc1f-3cb5-a6c9-09dce36f2866 | -7.66953 | -35.14664 | 2024-11-02 03:49:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a39139bb-8485-399a-9f7c-a5fc8b18aa44 | -5.31364 | -43.06899 | 2024-11-02 03:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e759160-b3b1-3581-9c45-73f0862b6f4c | -13.13871 | -42.15996 | 2024-11-02 03:49:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 97c24e38-e3d7-352b-9d6b-9d4a5dc7f610 | -13.87319 | -42.91886 | 2024-11-02 03:49:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bb179840-b384-3f8f-980f-ad54dc46f9bc | -13.86931 | -42.91813 | 2024-11-02 03:49:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 388e4a32-a0c9-3384-839a-f91e873d2f9d | -5.56329 | -43.88127 | 2024-11-02 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 568c9476-d784-3691-a155-8271f9894346 | -5.44801 | -43.57823 | 2024-11-02 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed356030-e416-3e4e-bc77-07fbf1632f8c | -5.29307 | -43.3311 | 2024-11-02 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 596cf52f-d723-3d92-ad48-9e1ff5eb1c37 | -7.66724 | -35.13867 | 2024-11-02 03:49:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 296a4a4f-4d5e-39db-a70d-f51b964ffd52 | -7.66667 | -35.1424 | 2024-11-02 03:49:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| aa4cef61-579d-3c32-920c-407b5bc5e5e5 | -7.66611 | -35.14611 | 2024-11-02 03:49:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3977ff14-f664-3123-962f-54c63d586ae2 | -6.23576 | -36.1978 | 2024-11-02 03:49:00 | NPP-375D | CAMPO REDONDO | RIO GRANDE DO NORTE | Brasil | 2402105 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b085f97-48cc-3987-b33e-4a661d2e3701 | -12.844 | -38.45123 | 2024-11-02 03:49:00 | NPP-375D | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 56c66513-fce8-3220-9e65-865830a7d62a | -19.27976 | -39.8959 | 2024-11-02 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ba944c06-0c99-378c-9e8b-98bf7e46f9d6 | -19.27701 | -39.89166 | 2024-11-02 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bf1e01c5-ac2e-3f51-9135-7f35bd2ba199 | -19.27643 | -39.89532 | 2024-11-02 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 721ff400-d7ed-3d8e-8ca8-589985382ccc | -19.27368 | -39.89108 | 2024-11-02 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fccb2d96-40c9-3487-b120-c9813eaa1436 | -19.2731 | -39.89473 | 2024-11-02 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a568079f-92b0-3b89-8922-f3a6e946bc09 | -19.26978 | -39.89415 | 2024-11-02 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c8f42a5d-b965-3963-9a57-ede941cc7e92 | -19.26703 | -39.8899 | 2024-11-02 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bb76b154-be19-392a-8acc-c87e09dc3ae7 | -19.26645 | -39.89356 | 2024-11-02 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0232a1d2-2510-3cae-92ef-3bbf9add6ef0 | -19.26312 | -39.89297 | 2024-11-02 03:49:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0b6f5e8b-af60-3f54-8288-7a7a850e7489 | -5.93058 | -38.34513 | 2024-11-02 03:49:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f7669907-9e7a-37dc-ac31-5c331027e86e | -5.93066 | -38.34557 | 2024-11-02 03:49:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3abb1cbb-6f46-3f39-9cd2-2bb36ac671bd | -5.93007 | -38.34927 | 2024-11-02 03:49:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8350e4ec-915e-33ab-9aa9-8207719c7cf1 | -7.44439 | -38.14115 | 2024-11-02 03:49:00 | NPP-375D | BOA VENTURA | PARAÍBA | Brasil | 2502102 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77d29cca-9473-3e50-b3db-9b7dff5a6ed3 | -6.86507 | -38.35708 | 2024-11-02 03:49:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ced668f8-6a1a-386a-a71e-0cf506cc2861 | -6.7787 | -37.54126 | 2024-11-02 03:49:00 | NPP-375D | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c307c0bd-d92b-32b1-9f31-11d1bf915f5a | -6.77758 | -37.54827 | 2024-11-02 03:49:00 | NPP-375D | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bee2d503-f299-3c18-9cc9-5c1babda85f7 | -6.77536 | -37.54072 | 2024-11-02 03:49:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9af2738b-46cd-34eb-a590-9b774943fa6b | -6.77202 | -37.54019 | 2024-11-02 03:49:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8bafb7a-dbff-3e01-8007-cda9527c1553 | -6.70346 | -37.48259 | 2024-11-02 03:49:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 328e5bd0-ada5-3f8d-8778-88e75d265e8a | -7.44496 | -38.13757 | 2024-11-02 03:49:00 | NPP-375D | BOA VENTURA | PARAÍBA | Brasil | 2502102 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af5d570f-92f5-3052-9a89-77db37619950 | -6.86846 | -38.35765 | 2024-11-02 03:49:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74e6e697-7d31-3644-9105-7de933941cf8 | -6.77814 | -37.54474 | 2024-11-02 03:49:00 | NPP-375D | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 97ce3cba-9671-3b32-bcf4-a65b0053eb33 | -6.70623 | -37.48666 | 2024-11-02 03:49:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d08adbb1-fb70-3ced-aa0f-69c2829028d6 | -6.68288 | -37.46143 | 2024-11-02 03:49:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9f8ed03a-89e6-3680-9c5b-f48ca837fa5b | -7.56036 | -38.76871 | 2024-11-02 03:49:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6350678-37f2-3694-b14b-c76ee028ffcf | -6.97608 | -38.40425 | 2024-11-02 03:49:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 01976944-05f8-38ab-9a5f-cbe554bb17d2 | -6.77148 | -37.54364 | 2024-11-02 03:49:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de5ab8fa-0843-3f1a-8705-f57b156f5ecc | -6.76869 | -37.53965 | 2024-11-02 03:49:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d394c3bc-6a9e-388d-8ba4-8da64b0df9f3 | -6.7029 | -37.4861 | 2024-11-02 03:49:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0bf4bd19-30f2-386d-b556-b63358ae7aec | -6.70012 | -37.48204 | 2024-11-02 03:49:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2d49b4d9-bc29-35c1-aacc-667cef838fbc | -6.69401 | -37.47743 | 2024-11-02 03:49:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6cc4689f-73df-30c1-8299-f6d4c8cbd469 | -6.69011 | -37.48048 | 2024-11-02 03:49:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 60b14090-46b7-3613-a47d-5b17e235c5bf | -6.68233 | -37.4649 | 2024-11-02 03:49:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9f43b493-27db-3cb4-a4a2-3f9aa0b5714d | -6.67955 | -37.4609 | 2024-11-02 03:49:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README26.md)
