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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5190715b-1ca6-3a38-b99b-3919eb2e5800 | -13.66549 | -43.67331 | 2024-10-10 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f946013e-bbf1-38da-93c1-739acf700231 | -13.66026 | -43.67266 | 2024-10-10 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5c8a25bf-f58e-382c-87a9-950c4f31cf3d | -14.1377 | -44.97008 | 2024-10-10 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faeb77b1-4c1b-3fcf-858d-1cb862a52960 | -14.05649 | -43.70379 | 2024-10-10 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 346f018d-41bb-3830-bcaa-79ed09aea7c5 | -13.89974 | -43.80586 | 2024-10-10 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55bbd239-be2e-3bd8-835b-5c1023b1c2a5 | -13.89455 | -43.80521 | 2024-10-10 04:46:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4449ba1c-d24d-3472-a5e0-626a5bb5f24f | -13.85249 | -44.51629 | 2024-10-10 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fa7f52ef-9358-3dbd-81f3-8f76879f8f48 | -13.00315 | -46.25373 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9916f09-d68c-3249-ad66-62f3c52ac526 | -12.99885 | -46.2528 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45d172ed-2340-3345-b989-00bd884735b8 | -12.99131 | -46.2428 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a321454-fdfd-32cf-a2ca-be56ae6f9fbe | -12.98702 | -46.24178 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29605022-0e73-3dad-99e9-e4779de7948a | -12.98326 | -46.23664 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ae2e688-4526-3bdb-9951-435d9d22016d | -12.98274 | -46.24067 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 312a291c-5510-3642-aded-dadbb711d1d4 | -12.98221 | -46.24474 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ab2c12de-b853-315f-b2ec-c19369dd3893 | -12.98168 | -46.24876 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0d8c9365-75c6-3577-8b70-624f063541aa | -12.98115 | -46.2528 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| beec69db-2e7d-346d-a675-0db5b8dc913a | -12.97947 | -46.23177 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 21b58c14-ebb6-31ea-a705-dac6e7147c1b | -12.97896 | -46.23565 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 40316746-65bf-31d2-b357-9998dcbf60a4 | -12.97844 | -46.23964 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7fa698e6-3779-3368-8930-ca05c4d59f78 | -12.97791 | -46.24377 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 6e1c6d99-5f6e-3a95-97b3-bdcc3d7bbc9f | -12.97791 | -46.20966 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 837b44e8-6a8a-30b2-9ba1-8dd13d4ce890 | -12.97738 | -46.21375 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c835f83-5e9e-306b-a3af-725c725aa2f4 | -12.97684 | -46.21792 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e29a62b1-1bdb-3c82-b9a6-cb8e5d3ce770 | -12.97571 | -46.22662 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3acbf932-ce7d-3485-93cd-743a2afc84b9 | -12.97516 | -46.23086 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cff55cfa-093b-39f2-87eb-3f7f5a8422f1 | -12.97464 | -46.23484 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6267538f-9cad-39c6-be07-70a59e86032f | -12.97413 | -46.2046 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b185e40-ca80-32f2-b537-9adab9911bd2 | -12.97359 | -46.20871 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a4ad354-e40c-36fb-83a1-949cf9defbdb | -12.97299 | -46.20601 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f81a4c3-6f54-3b84-9605-d832f6022633 | -12.97251 | -46.21708 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad056a0c-590c-36ae-8e33-13cde50f120c | -12.97243 | -46.21014 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5fd162c-38a7-38da-acc5-c475adfae7ea | -12.97185 | -46.21432 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a2f0fc3-e9c9-3849-b565-65215dcf4e30 | -12.97141 | -46.22562 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e80f88c-f897-3f7c-9d4f-9574e14919d3 | -12.97127 | -46.21857 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44690a1c-fd40-3a95-a042-f9c046aa1e98 | -12.97069 | -46.22284 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ca9034a-6a6d-3fcd-a202-68ac5cc81311 | -12.97011 | -46.22709 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 209776fc-1dba-3236-9adb-92d7139082e9 | -12.96818 | -46.21633 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c6a38dd-7d93-3e9f-86aa-19f00db02710 | -12.96752 | -46.21359 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfaed38d-3a10-30ac-b116-4d34cbabef03 | -12.96694 | -46.21786 | 2024-10-10 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bbd8a51-0fe4-384b-b5aa-c710832b8f48 | -12.70885 | -45.46719 | 2024-10-10 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6b76eead-609b-318e-9968-b4e98c88db24 | -12.70823 | -45.4719 | 2024-10-10 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef561b13-c566-3579-907d-613169181978 | -12.70429 | -45.46651 | 2024-10-10 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eec2084a-bc39-3942-bb02-10ff3fed0be6 | -12.70367 | -45.47124 | 2024-10-10 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22edf6d2-a94b-3a28-be69-938771997414 | -14.81778 | -50.80658 | 2024-10-10 04:46:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 19ff620e-7179-3934-8309-af91125940d6 | -14.2091 | -49.74456 | 2024-10-10 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d74e006a-0fa7-3e94-95b6-f0f2907c8adf | -13.40117 | -46.91394 | 2024-10-10 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a76caec9-56fd-3099-8e4e-bd93bb1d8301 | -13.38714 | -46.70097 | 2024-10-10 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a41808b5-e630-3dfa-bc56-13e86c907190 | -13.50408 | -47.98552 | 2024-10-10 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b4ba82b-f345-3493-b371-307e7aa0a12d | -13.50015 | -47.98508 | 2024-10-10 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba6f40da-43e8-3b88-bc1e-567cc243a7fc | -13.20816 | -47.98479 | 2024-10-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d05f5a3e-85d5-3ac8-9abc-9e9ebb32977c | -13.20496 | -47.97929 | 2024-10-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8705de7b-5580-3b32-bb0e-b34d481996f3 | -12.4836 | -47.50006 | 2024-10-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd75f448-e82a-3dbc-ba0f-bff87b54b5a3 | -12.47892 | -47.50466 | 2024-10-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 593621c1-221f-3df2-9385-4f84bc079df4 | -12.45479 | -47.30975 | 2024-10-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67b69079-e790-3383-9fb1-d7d9047ee458 | -12.45429 | -47.31332 | 2024-10-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd066fdf-b998-38c9-a742-8358b7d4628b | -14.8149 | -50.80219 | 2024-10-10 04:46:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4a56ef86-7ec5-316c-9902-06142f8a92ba | -16.50399 | -50.84755 | 2024-10-10 04:46:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20e6849b-3188-3d4b-99cc-ce45548ac42b | -14.20851 | -49.74873 | 2024-10-10 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 099e489c-cc3c-37f6-877b-af6f89a637ef | -12.7176 | -48.42978 | 2024-10-10 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cfe150a3-791f-32dc-967d-4242f3961eef | -13.61772 | -48.47934 | 2024-10-10 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4178dff7-bba5-3de1-921a-a3a5f97b0123 | -13.52665 | -49.47687 | 2024-10-10 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bef7346c-73a3-3921-83c8-9b2ab81f733c | -13.50318 | -49.2477 | 2024-10-10 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 502649be-92a4-343b-92d0-3ed440e2d157 | -12.50064 | -49.48808 | 2024-10-10 04:46:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08c5d841-b2d6-3236-b2fc-57405baf0331 | -13.0337 | -48.67587 | 2024-10-10 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 587dd086-890d-3365-b4e5-f5a9615c57f6 | -14.2067 | -49.74633 | 2024-10-10 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0a4752c7-271d-377e-81e5-ae2f9b3edd37 | -14.20609 | -49.75049 | 2024-10-10 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d78d5a58-688e-3217-8427-738d9bc51fd1 | -14.20552 | -49.74405 | 2024-10-10 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39a75496-5b41-3082-b211-397769ffde8c | -14.20493 | -49.74821 | 2024-10-10 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0a26064d-e95f-3b73-91d6-bb6b8a0a2555 | -14.20312 | -49.74582 | 2024-10-10 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4d6c2a75-14fb-37f6-8f2e-cfc12f83c028 | -14.20251 | -49.74997 | 2024-10-10 04:46:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77c533cb-7a38-392a-98c7-4a7f30efefa1 | -16.48395 | -50.00515 | 2024-10-10 04:46:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 046ca33e-61ed-3da2-80ea-a50ef7ea186c | -12.22157 | -50.43863 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1182802-240c-3d60-ac13-4fa015e130fe | -12.20751 | -50.6237 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f1a2761-67df-3e49-a625-7692a978e472 | -12.20412 | -50.62318 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcee81ec-8b76-32ca-9aad-48038413b529 | -12.20129 | -50.61893 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2aeed37b-0589-3954-8674-ef02cb43d643 | -12.19562 | -50.61045 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b21f097-8574-3cbf-8db0-e8b061801796 | -12.19279 | -50.60621 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5889fa0-c89b-356a-9ee2-9956b9705539 | -12.19223 | -50.60992 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c6cc1ff-38c5-33a7-ba62-86a6986d110d | -12.18995 | -50.60197 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c90a799-ef75-39fe-912a-2decbdea141a | -12.18939 | -50.60569 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 759de174-1486-36a3-beb6-d2fa5dc47a0a | -12.16798 | -49.68758 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a1a7736-12e2-3b96-9680-fde8b3885592 | -12.16505 | -49.68306 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eba11a0e-dfa3-3d32-8961-120bb96cec9f | -12.16447 | -49.68706 | 2024-10-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f6c5de1-26e2-3916-94c6-5877b8448d4f | -12.07632 | -50.81865 | 2024-10-10 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d17291c-5b13-3c0c-a940-326d038bbb12 | -12.07577 | -50.8223 | 2024-10-10 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62020acf-4ebe-3088-b8eb-4f9027954903 | -12.07239 | -50.82177 | 2024-10-10 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b788f9b5-0f88-366d-b067-ca9005a45b84 | -11.95 | -50.82138 | 2024-10-10 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50a61384-3bb0-36db-beb8-79ef8852b624 | -11.94438 | -50.81303 | 2024-10-10 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbd918cb-dc0b-3483-8231-d2c0eae30dae | -13.70294 | -49.85579 | 2024-10-10 04:46:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14c2408f-fbc8-316a-a261-40436416c3ce | -13.26181 | -50.28408 | 2024-10-10 04:46:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ccb31fc-b627-39bf-bf48-ab9884aaa2ec | -13.25966 | -50.2846 | 2024-10-10 04:46:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5fa12ca-6d46-3262-9b78-af207623fb50 | -13.25834 | -50.28355 | 2024-10-10 04:46:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba6ddd1b-2e74-3b7b-8ff0-c37fed4a66e4 | -13.2562 | -50.28407 | 2024-10-10 04:46:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53f3ac48-6d91-37b1-b4b2-7e0fc01e2748 | -12.94342 | -51.1312 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 130ec5ff-d141-36f7-bd08-ee93e91b7c62 | -12.93559 | -51.13744 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f407d60a-7265-3476-b1b5-be41853c9ac7 | -14.82178 | -50.80327 | 2024-10-10 04:46:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 772efbf0-6571-392b-8cf7-1f2ec2682405 | -14.82122 | -50.80711 | 2024-10-10 04:46:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc529837-73b1-3f26-bdc8-611ed97d0742 | -14.81891 | -50.79888 | 2024-10-10 04:46:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a0dd8e5-fb05-3c21-843a-18f01fbd8cc6 | -14.81834 | -50.80273 | 2024-10-10 04:46:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 239ed8ab-a98a-3644-ba40-6e7c426f222d | -12.01501 | -51.0621 | 2024-10-10 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README120.md)
