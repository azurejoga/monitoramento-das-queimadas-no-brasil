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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef1e4adf-9464-3e61-b780-1e0e2a400381 | -7.62016 | -43.8361 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbd39a62-88b8-3459-a6ed-93cebfc96dde | -6.70553 | -42.74852 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 414b25ca-099e-3ab8-b8e0-d3ca549730f4 | -12.36549 | -44.15006 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 340b5f79-160e-3cff-a5d0-eec88c986b7a | -6.6833 | -43.12503 | 2025-09-27 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf7b8bf1-a42e-3182-ac93-8069083a5554 | -12.06712 | -45.04803 | 2025-09-27 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84ca19c5-60c2-3666-9e52-4a7c27abb4f8 | -9.97815 | -43.59462 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e582b8f2-715e-3331-b3fc-ee1322c1ac2e | -7.89864 | -44.02028 | 2025-09-27 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df08db0d-70d2-398f-b305-1266be5b79af | -7.00518 | -46.99951 | 2025-09-27 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5c6acd5-c7b7-3a45-9429-e3c7a8483fc1 | -11.50137 | -43.53415 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1aacb93e-f18b-3933-8c60-916fb876e8c3 | -10.81419 | -45.38152 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ff7d9c0-db62-38ef-ac95-ab2962256571 | -12.61795 | -48.14109 | 2025-09-27 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f07ecb17-3c18-3cec-be07-ba7174b08c09 | -8.72444 | -46.68023 | 2025-09-27 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fda2b73-c758-37e7-bdde-c1bdc45c131e | -12.97455 | -43.22098 | 2025-09-27 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 005baba9-62d8-3097-a66c-cf1546a8fb5a | -6.53346 | -43.8327 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebbac742-911c-3e63-8664-73d8dea164ea | -6.70092 | -42.75267 | 2025-09-27 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8d35db8f-eed4-3e70-8531-9ff630d3a757 | -6.54805 | -43.84637 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8813ed0-af39-3375-9a9b-57a917c7d98d | -12.29686 | -47.21904 | 2025-09-27 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b11324af-26de-3462-98b4-02f8f732ed12 | -11.43067 | -44.92649 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 990e937d-0997-3f3d-96ab-faba07997a00 | -11.3783 | -44.94004 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4aeb1f01-4e18-3888-807e-ed7c34ac1461 | -11.79294 | -44.91546 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ae2f7ca-a103-38f2-a9fe-f6c02b4f30a1 | -6.52869 | -43.836 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5135243-f764-38f4-902a-30b3c182142c | -12.95398 | -48.91248 | 2025-09-27 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b047443-611c-3b03-9990-c882109f3387 | -8.66148 | -43.99014 | 2025-09-27 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 565413da-23ce-3c36-8d49-4b509249fdb3 | -11.49763 | -43.53352 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 264bf182-8c68-327c-8a87-3ffc01a83fd7 | -6.49602 | -44.23774 | 2025-09-27 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 064139d9-1c9f-3b98-b830-d3678e316d69 | -15.45075 | -49.63042 | 2025-09-27 03:57:00 | NOAA-21 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bdfc99b4-b357-34ac-8aed-9c9545255f03 | -15.56089 | -47.91656 | 2025-09-27 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33aaf557-98a6-33fe-ab09-a14714d7fa92 | -15.27622 | -46.42559 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ca9bd61-8613-39e9-be61-d0926156efa3 | -17.1872 | -44.79842 | 2025-09-27 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f74c805-2369-3289-a184-68d5b4f061f1 | -20.0072 | -48.94068 | 2025-09-27 03:57:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fbdf209-765c-3320-8826-0b5b9ca07d4f | -13.75681 | -47.8688 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92d84e06-f8b7-3565-a694-cfae1794a900 | -20.30966 | -46.65206 | 2025-09-27 03:57:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de53be40-d867-3e1e-bc7b-ebee309dfc33 | -15.20211 | -48.4643 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9ba16d37-8492-357c-a7ec-bf2df09b562e | -13.78578 | -46.93289 | 2025-09-27 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3544c7f-9c76-3713-982b-bec8eac5b848 | -20.43962 | -43.36796 | 2025-09-27 03:57:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8c04d8f2-0218-327c-92b6-1fb4de760de2 | -16.4047 | -43.72206 | 2025-09-27 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ce804ad-51ca-396f-a767-c482b3347431 | -15.53247 | -44.33359 | 2025-09-27 03:57:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3e6cea3f-7e26-3423-a078-4ce4963cff36 | -20.3136 | -46.65268 | 2025-09-27 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5de72df-fbe0-339f-9301-e3793321ecd2 | -20.32431 | -47.13646 | 2025-09-27 03:57:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0693033c-c5e7-3777-b004-c3667d762ae2 | -15.19401 | -50.09826 | 2025-09-27 03:57:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b24eb7d8-527e-38c2-b52f-80594c918a51 | -14.88075 | -45.53737 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7f67912-8a43-3cb7-a010-811fd93ec465 | -19.85089 | -42.59866 | 2025-09-27 03:57:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1430952a-cc3a-3bc6-917f-1371616630f9 | -16.76385 | -53.36115 | 2025-09-27 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 37a29153-0aaa-3670-a985-969e68d2b1ef | -15.89147 | -46.19095 | 2025-09-27 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 75ec3ca9-ec58-3168-b181-1c6aba543bab | -20.88471 | -44.00808 | 2025-09-27 03:57:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7194eebe-369f-3db5-a0af-d090658c3c52 | -14.95231 | -47.50249 | 2025-09-27 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0f9f2df-cf0f-3fa1-bb0a-2df67c596be2 | -13.5069 | -47.40953 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 993227e7-2aa3-3af4-b33e-226bfcbc21c4 | -14.0617 | -48.82423 | 2025-09-27 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0324070-5bbb-377e-86a6-9b9743d10d26 | -15.03351 | -46.93925 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 438a4de2-ef7b-3156-87bd-054cd074d54d | -15.0369 | -47.13901 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 36be42e3-6c20-38b7-b108-d581e8cc96ee | -13.67524 | -50.63912 | 2025-09-27 03:57:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d8b5895-183b-3666-adc1-0f0fad40889d | -17.50675 | -46.73836 | 2025-09-27 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 112fdd4a-2060-3d1d-938b-89599d926077 | -19.05324 | -48.1366 | 2025-09-27 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 477cc9f5-58ae-3503-b2c6-4fc5812d97b8 | -21.68598 | -45.01891 | 2025-09-27 03:57:00 | NOAA-21 | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e07a3310-e0d5-3983-847a-94777967b9c2 | -13.62817 | -48.08015 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b626871-fe7a-38bb-9834-50190915d1e9 | -15.10893 | -46.45697 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1346413f-5435-3dfa-8a4e-b851892e6890 | -14.06193 | -48.81919 | 2025-09-27 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 895f0470-dd7b-3c86-a19a-addfdc7f4b37 | -13.70795 | -47.89254 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2a6bfd38-719f-34a0-beee-80611dfdcda0 | -14.84531 | -45.62045 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5cb97d6-a156-376c-beeb-d3c4d638656b | -15.44615 | -43.64435 | 2025-09-27 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8dea85c6-4175-3311-a8b9-634b1d47c389 | -14.83808 | -45.63766 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58ebc7f9-37bd-37ed-a8f6-d24531e4df48 | -20.43561 | -43.37115 | 2025-09-27 03:57:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 49b25b2c-e59a-3657-8e50-7e9d9f17887e | -15.01211 | -49.23334 | 2025-09-27 03:57:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1f7e1c2-45ee-33a2-ba99-ec3fe6be52c5 | -19.45936 | -48.92482 | 2025-09-27 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cd7f71e-de55-34d0-8229-155e9e70d453 | -13.61621 | -47.30529 | 2025-09-27 03:57:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3550e38c-b05b-3981-8a9e-7a8812a0dcce | -15.53509 | -39.88371 | 2025-09-27 03:57:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3c60d2f9-aa5d-32bf-bf3f-c082b7610fd7 | -13.67605 | -50.63505 | 2025-09-27 03:57:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8be0fcc9-0e3f-3c15-b226-91b3950d4c75 | -20.96823 | -45.80896 | 2025-09-27 03:57:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c221015-38c8-3b8f-9019-4dfb9d3dcd48 | -15.2737 | -46.46236 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c01d5ee3-5908-38f7-b8d9-d1df014115b5 | -14.95142 | -47.50729 | 2025-09-27 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75013112-5c58-3da4-bd6b-a469500c6db9 | -17.34031 | -44.45802 | 2025-09-27 03:57:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0978240e-a0db-34dd-8369-acae49a5663c | -20.65711 | -48.78252 | 2025-09-27 03:57:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| baa79448-986e-31c4-8b6f-576cbb1c81c8 | -20.32101 | -47.13179 | 2025-09-27 03:57:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4e330ec-02fd-3e2e-b4fd-2b92b7124ec5 | -14.59541 | -48.24696 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1c51aca-db71-36da-b90e-32e2de113934 | -14.83195 | -45.62542 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 830d0216-c208-35e5-b694-d0145e7602e4 | -13.63414 | -48.07496 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d995e798-5f49-34dd-86c1-b14118e2663d | -17.73099 | -46.70869 | 2025-09-27 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3f7393f-1248-32b3-8bf5-a7dca20e6eee | -15.26664 | -51.46458 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d72f9dc-07ec-30ef-bfbf-875968227d94 | -20.30279 | -46.66718 | 2025-09-27 03:57:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1319471-d475-3fdf-95c6-22ab1ebd7a21 | -15.19934 | -50.09942 | 2025-09-27 03:57:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e5e5052-cb89-3558-8cff-e99348ab7fca | -20.32033 | -47.13541 | 2025-09-27 03:57:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d00296d3-1744-38b1-a085-9318826ffedc | -15.45533 | -49.63438 | 2025-09-27 03:57:00 | NOAA-21 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 766dc00b-9891-3689-ad5c-ee8bb2f3e0a5 | -15.02918 | -46.96268 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78ccb0bc-0d66-3f33-8e13-5af65cf5d4d5 | -16.75758 | -53.35951 | 2025-09-27 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4e591145-1c3e-3d35-bcd8-165f58839a4e | -15.2752 | -46.45433 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05a7e79d-56c1-39f2-a1de-ca810ec9b456 | -14.84385 | -45.60531 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d8b49b0-8026-3285-9722-d7b3f3a65478 | -15.54002 | -44.34185 | 2025-09-27 03:57:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8786aa88-8b0d-3fe0-a8b2-6aeb77a2f982 | -14.47938 | -47.70457 | 2025-09-27 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b464b0d3-ef2f-3d04-b892-61c8d83cbccd | -19.78009 | -41.93515 | 2025-09-27 03:57:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 637c0b76-44d3-37e8-8b9e-228e46facd1b | -15.20104 | -48.46991 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 084b4f94-0166-33d6-a819-e5443ef42675 | -13.76085 | -47.8735 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b49fea54-45cd-3a2b-8fe7-13ac9dc014c5 | -15.27445 | -46.45833 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35354f59-e87a-3a5d-b1b7-8d8fdce58a52 | -14.83259 | -45.6218 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 220a77df-6f22-36a4-9778-9a34254cd5bb | -14.06638 | -48.82311 | 2025-09-27 03:57:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a34719e2-9317-38c0-aea9-43b663b0a966 | -19.05411 | -48.1321 | 2025-09-27 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 86ec1fcb-773a-3942-8bf4-1f61d3a43591 | -12.65082 | -51.68037 | 2025-09-27 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6dc6ab8f-9bd8-3018-94ac-8cdbd6b9541c | -22.13475 | -42.3247 | 2025-09-27 03:57:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6eee5374-6516-30fa-a37e-0c6e2ba6ff47 | -15.32663 | -47.87662 | 2025-09-27 03:57:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe0755c6-879a-39ce-bcb4-3a9cb75df5f1 | -13.61464 | -47.31365 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b871e9d1-0a40-367e-905a-c4a9fc677a10 | -14.5954 | -48.24464 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README22.md)
