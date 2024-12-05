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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9597b21e-cafd-3e93-bb25-b5fefd538143 | -6.93124 | -43.53855 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e86a392a-2a33-3a03-8bee-00e1ad270a36 | -6.92349 | -43.53932 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 041286a0-a622-3fa7-a9f7-b5d4853ee57e | -8.18423 | -35.26899 | 2024-12-05 03:29:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a58ea027-d422-359a-8f4f-8b2cfdbf2397 | -6.93209 | -43.53385 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| caec2fd8-9861-369f-9ea6-1f1a6a838579 | -8.97941 | -35.99021 | 2024-12-05 03:29:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 17965fbe-b527-3762-8016-ea58ecca8038 | -9.89959 | -44.34908 | 2024-12-05 03:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dbd7bcf-f2cd-3c49-8088-b2ead1119bd8 | -6.13088 | -43.95193 | 2024-12-05 03:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a240ace1-31f9-3737-94cb-1713bb87cbda | -6.13821 | -43.94809 | 2024-12-05 03:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 965bf6cf-ada0-3f77-ab89-57f08f375091 | -6.93738 | -43.53984 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4d61896b-ceb4-3328-af8b-fbe2280a8b53 | -12.71536 | -40.20898 | 2024-12-05 03:29:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b663f9c-5b80-3483-a3b7-dfda9daa9851 | -7.42745 | -39.89143 | 2024-12-05 03:29:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| dc441d39-ae99-39af-b711-a29671ecf37c | -10.49764 | -36.98822 | 2024-12-05 03:29:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| db6befac-4e6e-37f2-b4aa-71852c16817d | -10.67776 | -37.20052 | 2024-12-05 03:29:00 | NPP-375D | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9aec14ed-f2f2-3270-8ae2-1db69edc69d9 | -7.94204 | -34.85462 | 2024-12-05 03:29:00 | NPP-375D | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ae29d2f3-16d3-3e9b-8707-c02eeb18c04e | -9.89466 | -44.35198 | 2024-12-05 03:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5afb56e2-d7a4-37cd-8b5a-096ec8a39019 | -6.92952 | -43.54807 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 34d1031e-8ce2-3159-9f78-19ddcbcde2c3 | -6.92965 | -43.54047 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1abfac2c-0ef1-3b90-a055-0fbdfd0bbcab | -11.23378 | -37.74211 | 2024-12-05 03:29:00 | NPP-375D | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f64df794-1c3f-3c05-8857-c6cd1cdd7c54 | -9.9865 | -35.99781 | 2024-12-05 03:29:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3c44d6eb-1d7f-32ee-8642-99c38683352f | -10.46791 | -36.98523 | 2024-12-05 03:29:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bf2d5786-c2d6-33b2-98e7-91523ae7d567 | -6.13732 | -43.95295 | 2024-12-05 03:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91f48e3d-abb7-3d21-a4a3-f8321cad190b | -10.4711 | -36.98333 | 2024-12-05 03:29:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 78c865fd-2e04-3a05-8bc5-06956e7d268f | -6.92422 | -43.5421 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9a9c08d4-8b8c-3ab6-a577-36f2f313e295 | -11.29154 | -40.9781 | 2024-12-05 03:29:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a818dd3-b29c-3e9b-a0bf-10f25bcbab74 | -6.13099 | -43.94926 | 2024-12-05 03:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e8248db-db66-361a-9192-205970223677 | -9.31393 | -43.06304 | 2024-12-05 03:29:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5c3d399-8ac2-3bc7-99a0-38cffabac892 | -6.93142 | -43.53107 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 952d6125-1534-351b-9a96-2f6727c4d345 | -10.6105 | -36.93816 | 2024-12-05 03:29:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| afd50fef-c92f-335a-9ca0-b3382eb3e25c | -10.47028 | -36.98809 | 2024-12-05 03:29:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 808a23b3-cac1-35df-b972-160ce780061a | -11.29394 | -40.97686 | 2024-12-05 03:29:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b262211b-4173-3780-9aaa-daae1bd57c63 | -11.87174 | -38.35217 | 2024-12-05 03:29:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3bcdcf9d-dac6-3597-acee-3e93e9064117 | -6.93823 | -43.53513 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d21dc373-44bb-3547-b136-b69862be36c4 | -6.13653 | -43.9553 | 2024-12-05 03:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 107ae238-c3d1-39da-905a-7550316e7a90 | -8.18356 | -35.27307 | 2024-12-05 03:29:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2b860cf7-143d-3482-8529-3a655d357fb4 | -8.17999 | -35.27246 | 2024-12-05 03:29:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7f2987af-490e-3aa4-b3c6-19e366fd4168 | -10.50362 | -36.7021 | 2024-12-05 03:29:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5e0706b4-061c-3afc-a222-2604ae3879a3 | -6.92508 | -43.53734 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fd020eee-b551-325d-8a27-a30742395717 | -8.67412 | -37.00087 | 2024-12-05 03:29:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edc50ea3-b180-36f8-a9ab-5eced48e8f20 | -6.93294 | -43.52912 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ac826eed-3187-3faf-978b-6fc48f380a01 | -9.31322 | -43.06684 | 2024-12-05 03:29:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ed9b644a-dcf1-3e1c-baf8-55cd5a3dd6b4 | -10.49989 | -36.70141 | 2024-12-05 03:29:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 237a09ca-8340-3abb-b17f-096143d18ff1 | -7.43227 | -39.89227 | 2024-12-05 03:29:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 644e0d3b-9bdb-32a0-b4f7-2698c498589b | -9.34149 | -41.27042 | 2024-12-05 03:29:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fcb1e895-fa32-3eb2-8f0c-de18e46ef5fb | -10.65874 | -37.09116 | 2024-12-05 03:29:00 | NPP-375D | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4ca4cd8f-ba41-367d-9b92-477a98d5fe6e | -11.76857 | -38.68159 | 2024-12-05 03:29:00 | NPP-375D | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c193f1ae-070e-3af6-9d6e-f67b7ac50769 | -9.9822 | -35.99857 | 2024-12-05 03:29:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 43bed3ad-e1a0-3922-92e7-d95b275fc420 | -8.9791 | -35.63389 | 2024-12-05 03:29:00 | NPP-375D | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8c7135dc-63be-3e9b-ba0b-dcfdccd4c37f | -6.93054 | -43.53576 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 731d8b30-7db9-32fb-8012-06aca9e679c6 | -9.89346 | -44.34763 | 2024-12-05 03:29:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efb1b49b-1e8b-35fb-97b6-9aba67b3a099 | -6.93403 | -43.5512 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3d163ad8-12ee-34e7-a723-d1f8cb0bf04a | -11.11249 | -37.33084 | 2024-12-05 03:29:00 | NPP-375D | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0da58085-21e5-31a5-8cc5-41066180c3e6 | -10.81753 | -44.36694 | 2024-12-05 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62522091-1ebb-31fe-8923-79a053016f4c | -9.98582 | -35.99921 | 2024-12-05 03:29:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2cbeeee3-c5bc-36c5-98f3-8a4b37fad127 | -6.13562 | -43.96046 | 2024-12-05 03:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49191089-f12e-38e4-ba64-99986e46e8e3 | -10.67695 | -37.20517 | 2024-12-05 03:29:00 | NPP-375D | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 20af2331-99cd-37a0-a055-001a932836e4 | -8.18066 | -35.26841 | 2024-12-05 03:29:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a4ba4ca1-081e-3fde-a44d-2c5a3f2ba8f1 | -6.93756 | -43.53233 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a46f6cec-3700-3cf3-99d3-bd9da3e41d11 | -12.71877 | -40.20717 | 2024-12-05 03:29:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f65ad305-211c-3b87-bef7-1e1bb327d534 | -6.13639 | -43.95801 | 2024-12-05 03:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9901a017-6443-31d9-ab11-65bfef65ff60 | -6.92438 | -43.53456 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1d1eff2-3fd5-3c8c-92b8-f25c10cc5144 | -10.82359 | -44.36824 | 2024-12-05 03:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73362d87-2d32-3151-9a6d-e7d25aae708b | -9.98945 | -35.99986 | 2024-12-05 03:29:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d49b2d56-dd2b-3d72-b7bd-21491ad995d0 | -10.65796 | -37.09583 | 2024-12-05 03:29:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 16ce703f-9b21-3b06-9c89-ae3c53728d01 | -6.93569 | -43.54925 | 2024-12-05 03:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e82d179b-a297-37e5-800a-a1f8d335ac43 | -6.9344 | -43.5401 | 2024-12-05 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 127.5 |
| f63d09c4-1bf1-3b37-866c-8bf3ba892243 | -6.9346 | -43.5168 | 2024-12-05 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| fffefe1f-a96a-33d3-8d75-b7848d8b27d1 | -6.9156 | -43.5418 | 2024-12-05 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fc4688d7-d482-3d35-940e-820be982c1fc | -17.61712 | -40.30798 | 2024-12-05 03:32:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 3dc2dd0c-a4e7-383a-8226-b507d27c8a6f | -13.41352 | -41.11581 | 2024-12-05 03:32:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d14e11b3-0593-3c3a-ab42-39526afd73b1 | -17.61785 | -40.3041 | 2024-12-05 03:32:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 9dd32462-5570-3366-a883-c583a322fcb3 | -13.36174 | -41.33852 | 2024-12-05 03:32:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bbab00f4-753f-38f8-9fd2-4f37a0cfc918 | -13.41512 | -41.11279 | 2024-12-05 03:32:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8a5be053-6f7a-399c-9cec-8d2f451b50cb | -16.85336 | -40.66328 | 2024-12-05 03:32:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 23a2a9da-54b8-372d-b00f-5efb6f30eaeb | -19.1654 | -40.13806 | 2024-12-05 03:32:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ac9e58a7-6608-3575-a263-6ab9afa5ecd5 | -17.622 | -40.30495 | 2024-12-05 03:32:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 339557c1-d33b-3e34-a019-a76b5ff20486 | -19.16941 | -40.13885 | 2024-12-05 03:32:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fdb65c90-4054-3ecd-8135-9aa008cafed7 | -13.35691 | -41.34153 | 2024-12-05 03:32:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 43d05e3d-b705-3ceb-a438-b61b1fb526d7 | -13.3627 | -41.33704 | 2024-12-05 03:32:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7965289a-1c9a-31d5-8fce-fc9f30986bc3 | -18.50813 | -39.92466 | 2024-12-05 03:32:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b5656dba-6bd2-3580-bcc0-f1994c9a5054 | -18.50774 | -39.92337 | 2024-12-05 03:32:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 886406e4-92d6-328b-93f2-8f4eae26c998 | -16.84904 | -40.66254 | 2024-12-05 03:32:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e689b1a8-bede-36eb-bffe-0dd3c13a2452 | -13.36168 | -41.34253 | 2024-12-05 03:32:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6714bbf6-e6b0-3e18-a8e4-bc6af1701a9e | -17.62127 | -40.30885 | 2024-12-05 03:32:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 369b22e6-27c4-31f8-9382-45ec059b4c46 | -28.70509 | -49.30411 | 2024-12-05 03:36:00 | NPP-375D | IÇARA | SANTA CATARINA | Brasil | 4207007 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c7ffe822-d37b-3f7c-86de-956c80935a24 | -30.52872 | -50.45821 | 2024-12-05 03:36:00 | NPP-375D | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| e0816ec4-f10b-36b6-9377-a5efec67e15f | -28.70619 | -49.29967 | 2024-12-05 03:36:00 | NPP-375D | IÇARA | SANTA CATARINA | Brasil | 4207007 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d05837d1-f7ee-3960-8611-a949102f6219 | -30.52746 | -50.46302 | 2024-12-05 03:36:00 | NPP-375D | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 67f75b82-52c1-341f-82d1-ffe8bb9c3c74 | -28.70525 | -49.3011 | 2024-12-05 03:36:00 | NPP-375D | IÇARA | SANTA CATARINA | Brasil | 4207007 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 19e42549-e94d-3201-bc00-fa9682469832 | -30.53446 | -50.46024 | 2024-12-05 03:36:00 | NPP-375D | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 132f578d-3a6c-3a2f-8437-ad12c90cde1d | -6.9346 | -43.5168 | 2024-12-05 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d4fc3e5b-7eaf-3e42-8386-c3c0d834eed5 | -6.9156 | -43.5418 | 2024-12-05 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 379c29d7-2418-3451-987b-eb0552ab089f | -6.9532 | -43.5384 | 2024-12-05 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 0bc1c025-8c77-383c-9ac6-61d7665fee25 | -6.9344 | -43.5401 | 2024-12-05 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 0079f34b-1fd8-339a-947f-2af70fdec445 | -6.9346 | -43.5168 | 2024-12-05 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7fdacacd-8245-366c-a75e-6d42dd3bce96 | -6.9344 | -43.5401 | 2024-12-05 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 82e7b964-3678-3434-99d7-3a79a38d40e0 | -6.9532 | -43.5384 | 2024-12-05 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 7585ea99-65f6-3c2b-944e-f084e8a3cebe | -6.9156 | -43.5418 | 2024-12-05 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| fb9b3ed1-64f5-3ede-8809-401a7e59836d | -6.92391 | -43.53371 | 2024-12-05 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c16563e-75e2-3dbe-8bd4-a07ec150faa2 | -8.97562 | -35.63227 | 2024-12-05 03:53:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 32eedf69-edc1-3a5a-a6b4-c9b4eaeab539 | -5.58033 | -45.21388 | 2024-12-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README6.md)
