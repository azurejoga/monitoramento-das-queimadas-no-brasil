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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 072c7583-3329-3d80-8edf-51aad1f14781 | -3.58898 | -47.52399 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 05997ed2-0636-31b1-8672-246d9782507a | -3.23009 | -47.63615 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b33a7db7-d427-3976-8541-aac9efb2fac1 | -8.94426 | -46.04963 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f35edaf9-88e0-3ad9-a31a-d598e0796516 | -9.48879 | -46.40806 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38faba80-339c-3a2a-9060-58bd3b1f4068 | -3.00845 | -47.83865 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bcb3ef3-2597-3e78-b52f-33886e3449c4 | -7.37472 | -44.3501 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4452051-9e49-38e7-a350-b063a4ad7798 | -7.61201 | -46.70938 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 907b831f-3ab6-3344-ab09-55259e352345 | -8.62319 | -40.19392 | 2025-09-14 03:47:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42995e34-551d-326d-8b8a-1f24bb8cc184 | -9.49399 | -46.4091 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c705e167-ad64-33d4-9354-efa0ad4f3d98 | -4.6587 | -37.46343 | 2025-09-14 03:47:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4119053f-df29-3781-b0e4-79211691a52f | -5.247 | -37.35474 | 2025-09-14 03:47:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 58e35d1c-4298-3795-8ead-2346aca6e996 | -5.80362 | -35.54197 | 2025-09-14 03:47:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d01398a6-165b-3f67-9066-0a258ea159c5 | -3.79866 | -47.58642 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf66876b-b640-3be1-8fc8-bf8abbc9df39 | -3.59514 | -47.52515 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4a127d3c-3e3d-3081-a404-944870cc5433 | -8.95 | -46.04725 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00a045a6-9742-3ad2-ad7e-d0d61d056a4b | -5.65956 | -37.2161 | 2025-09-14 03:47:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 27067ea4-5a18-39c9-bac5-ed073e9c94bd | -9.49357 | -46.41355 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77081f39-43ec-3787-8d30-bfec25209ff0 | -3.79392 | -39.53106 | 2025-09-14 03:47:00 | NOAA-20 | TEJUÇUOCA | CEARÁ | Brasil | 2313351 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 607b0d48-bd39-3809-ab25-2cfc75b6f32d | -8.98924 | -45.77622 | 2025-09-14 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae252617-16c4-306d-8bba-71a5babfd89a | -3.2274 | -47.12941 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96f2d5d0-8c80-34f7-8437-6a6fa4be5a95 | -8.47524 | -40.50379 | 2025-09-14 03:47:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f375984b-9733-3cac-a729-d0598e815ac6 | -9.06364 | -47.02874 | 2025-09-14 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc9d9f77-05e5-3ecc-85b2-86e24b7d2bc5 | -7.92945 | -39.84742 | 2025-09-14 03:47:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7df2adc-c8a6-383b-a7d5-397b679ae7b7 | -7.06114 | -43.89661 | 2025-09-14 03:47:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9806af64-3a28-38c4-a516-bd13c7b1b820 | -9.0641 | -47.02819 | 2025-09-14 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bada943-8631-38c5-b7f4-84cb370f6424 | -10.06999 | -47.14983 | 2025-09-14 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4a2bff7-4f76-3310-8e70-31b392fc33d9 | -3.59456 | -47.52184 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6dedee68-109b-3b1b-8bde-b89b097c8ed7 | -8.07841 | -44.52035 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 998cbb2a-398d-3a29-8b40-0bcc155c8551 | -8.179 | -46.77607 | 2025-09-14 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f42961fb-6340-3003-a59f-84ddd2a32f12 | -8.98816 | -45.78208 | 2025-09-14 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bb7490d-89c2-3a21-863a-a960d61d8935 | -8.49538 | -44.72369 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eb812f5-3970-305a-8384-52648e311deb | -9.43025 | -40.30779 | 2025-09-14 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44008fa7-eb0d-380e-acd0-273263d2a6b6 | -7.37202 | -44.34612 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e5eb7d10-2a6d-3111-b2e6-41cbb01cdbc9 | -10.76684 | -46.48417 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 093b450e-4f80-3b59-b5d3-a0aee7cb9c8b | -11.47547 | -50.77909 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb5b6856-5013-3980-81c8-63a653672f7e | -11.60535 | -43.31774 | 2025-09-14 03:49:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82d56c5e-9eab-31b8-813b-86cdee286b77 | -11.78044 | -46.65614 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5961ea36-c4d2-3dc7-966f-9e6fe136a868 | -12.76593 | -48.01927 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2dfb3466-9593-3422-814b-b889585e61a2 | -10.92649 | -47.19364 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3cfe7ec-4fe9-3c1f-ab84-44bf552b2815 | -10.88198 | -48.18541 | 2025-09-14 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3deaeae-113c-3b4b-a1cd-1fb0d0fd1ce0 | -12.5536 | -45.65996 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0320a78d-c405-31f4-8879-f867029ab747 | -16.91547 | -41.28212 | 2025-09-14 03:49:00 | NOAA-20 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 21d0572e-41bf-36ed-99de-a21bcda3844f | -11.14294 | -48.09425 | 2025-09-14 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5951145-66e4-31db-ab6d-5a7e4fbedf5f | -11.24676 | -44.7771 | 2025-09-14 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2df3dce8-faa2-3a95-9e9b-e8efbb68be99 | -11.34442 | -50.82944 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a6c5543a-f46f-324a-af9f-62334da60eba | -17.259 | -47.24555 | 2025-09-14 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a96ab36-8dab-3bd2-acd3-1367b5b2ba08 | -4.48254 | -48.11562 | 2025-09-14 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cf47cef-267d-3d2f-8451-1e80a6e5ec94 | -14.47747 | -47.32088 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3f168d0-809f-3173-81a0-eeacbad586f4 | -11.49158 | -43.63538 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75ca40cb-910c-3071-9117-7011dfe2968c | -14.19776 | -46.16349 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16d3c66a-24c3-34aa-8861-e8287370242b | -14.61603 | -52.07735 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53260fdd-27a5-35a1-aae1-bcb153442324 | -10.32331 | -48.82378 | 2025-09-14 03:49:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c70623d-3880-3409-aada-ae240ba72f2e | -11.23136 | -47.6255 | 2025-09-14 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74493cea-f652-3ada-9cfb-d8f10d58e79f | -18.00738 | -46.9695 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5a8c0556-9d9d-30c6-805c-4574ae7253d9 | -18.09112 | -42.93283 | 2025-09-14 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 043910aa-87ba-3ee9-a3b7-afb9e86275fa | -12.03532 | -46.53715 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e647e066-bcf9-39dc-9e31-0f843690214b | -12.95892 | -48.05192 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1bb1d8b6-65ff-350c-891e-058292e04c02 | -14.61795 | -52.03605 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cf0de34-1be4-3356-a91f-a889b0e31fc5 | -6.56217 | -43.95528 | 2025-09-14 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 117e8ba9-f19d-3650-a16a-6ad684de1358 | -16.18771 | -43.13 | 2025-09-14 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f61a09c-7616-356e-8d9b-3df1490dcdf8 | -12.80362 | -47.14138 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3cb35250-e9f4-3db7-b164-dcace3ae303c | -12.76876 | -48.00455 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 82d8ca5c-1bc2-3360-a716-ee7e172d04da | -13.00746 | -46.74826 | 2025-09-14 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14c07eef-3429-3cd1-b255-50e18339b14c | -17.34748 | -46.66781 | 2025-09-14 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21447a62-4df5-3128-8047-da731a58d559 | -14.62269 | -46.36695 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ed590b3-c6d5-30ec-baba-dbb7126f543e | -12.91077 | -46.54829 | 2025-09-14 03:49:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c501221d-cfe0-33ee-b28a-c827659af95a | -18.47129 | -39.76354 | 2025-09-14 03:49:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 141c0a1e-bf71-31dc-a13d-cebf4522a66c | -15.92632 | -49.97932 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 99953877-92cb-363e-b55d-b8b690884bdc | -14.44087 | -43.19404 | 2025-09-14 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 794a113a-509d-399b-9c8e-73b08c797f25 | -16.65167 | -49.77052 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7e1704a-581b-3741-af6e-aff2a506a5b5 | -14.48086 | -47.33046 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a59de87-5f9f-3a3a-810f-2ed712638021 | -11.14624 | -48.09072 | 2025-09-14 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85a4a18f-7234-371c-ad16-7fc6bbc45e30 | -11.43453 | -43.54453 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9414bda2-8a07-30e6-a43a-c260909109f7 | -12.5697 | -45.65992 | 2025-09-14 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15fe92be-87e6-3908-9323-46a89a8ab063 | -18.06438 | -45.41937 | 2025-09-14 03:49:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 501417cf-e29e-326d-9d5b-cb445f369d4b | -11.82484 | -46.36597 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fb6cdd6-c39e-3583-a06e-cc3e7e2ac1b1 | -15.77294 | -52.22276 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32450129-ab65-36aa-be7e-82b83a384530 | -14.45846 | -47.31062 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9ab2d3a-ae87-35c0-9c45-f2b21c72b779 | -17.13427 | -48.51237 | 2025-09-14 03:49:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50854462-0e25-3f37-81cd-6dc5a58dcbda | -4.41081 | -47.6124 | 2025-09-14 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b04751b9-ed64-3e2d-805d-2ff31f144efd | -14.4789 | -47.34042 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c4a1785-7eb1-30fb-a9a3-93c0b9fdbe14 | -14.102 | -44.30837 | 2025-09-14 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b5cb01e-7e2b-36c3-8da9-efcede5f5474 | -14.20058 | -46.16925 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7cda4aab-43ac-3b75-8a1a-9b057ee6751c | -10.74314 | -46.44059 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7816940a-01a7-3546-af59-0febc6761e08 | -14.56264 | -43.72432 | 2025-09-14 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6771d78f-eb56-37fa-b25a-f1252083e847 | -6.20446 | -42.70613 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ccbdbcc0-181a-37b3-a987-c8b254c4c2b2 | -11.29156 | -50.81752 | 2025-09-14 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bfc8339-783d-3484-8079-d849c7ab8f8d | -12.96638 | -48.04547 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b441bd45-ffab-30cf-beaa-7da014a25584 | -14.61132 | -52.07631 | 2025-09-14 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e0abe9c-0e0a-34f5-baf5-c67f13e0bc91 | -12.78753 | -47.14156 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28a366c6-9ab5-32bc-bb8a-d25498b3d8d4 | -11.23037 | -47.62879 | 2025-09-14 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c0ad8b24-6df2-365f-b0cd-ee1ca03f2992 | -12.25962 | -46.79216 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ae75fc0-6a90-376b-a6fe-4705a08b1dec | -4.48486 | -48.11908 | 2025-09-14 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ebfe243a-dc7c-3d46-a0fb-c67e039fbddb | -12.77687 | -48.02135 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e4ac216-1740-348b-90f1-2d865f0ba87c | -12.96508 | -48.04936 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 279131b6-7de5-356c-9ba5-d061d866773a | -14.33827 | -46.6186 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b29f7584-9188-3dea-a499-c8ef62e4edcc | -14.62739 | -46.36806 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc799924-bf71-3fb6-a92d-1ada92535c4f | -18.39307 | -44.09486 | 2025-09-14 03:49:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce95af62-97c2-3464-b153-b1bbef1195e8 | -12.78168 | -48.02734 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| db85d1f1-db1e-3ee4-8afc-c7126f1bb5c9 | -10.96232 | -49.56912 | 2025-09-14 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README14.md)
