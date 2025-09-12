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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb8da830-68b6-35ad-92e0-65ade403bb97 | -12.93118 | -47.99707 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08759e7f-b921-33ce-a4ab-22a4719c340c | -12.99123 | -46.74548 | 2025-09-12 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ec3ec41-61ef-361c-9bfc-5286634a3a03 | -12.96503 | -46.73766 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4db09ae6-2455-3f35-9fee-5e65ed116c1b | -15.67035 | -47.06949 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1dc16d4-6eb1-3ad7-9c64-37f6a712fd33 | -13.7808 | -46.27919 | 2025-09-12 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 04ef761f-8d01-32a9-83c6-7954a74e9dba | -13.90011 | -48.24815 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24beca6b-2331-3fb4-8250-940cfdce3ec1 | -15.17947 | -53.81692 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b50eafad-cf56-3c90-92fc-406bd2c5d9d4 | -18.53433 | -48.41572 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3bed8eef-ba66-36b5-9e19-7455fdef86fb | -17.35012 | -46.6787 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f740b5a-74bb-38e4-9b25-909d6ebb8368 | -17.28066 | -46.08094 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 660ec585-41e3-340d-b846-c26ca138da71 | -14.41032 | -47.3096 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 531d8c3e-95cf-3902-b6b2-643f58e41256 | -14.44748 | -47.30829 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f408ae38-c3eb-3547-9c4f-37d8da10d13c | -13.90955 | -48.2315 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9905d3b4-9412-369c-ad64-f1b524f6ed31 | -20.17185 | -44.62471 | 2025-09-12 04:27:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d45c2d1d-0087-3add-b1b0-d67e960ce5ae | -13.14945 | -47.1477 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14270b65-5687-36f0-970e-d93e57117153 | -12.85395 | -52.96952 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bea0fed1-6674-33b7-8da5-338cf59e2950 | -14.40524 | -52.93124 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c64aaac0-4eee-32d0-9149-dde5a843a2c1 | -12.86724 | -47.95113 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f3e427c3-4c86-3b58-b290-6b42ddb6ba82 | -15.57839 | -54.77084 | 2025-09-12 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8a5a9a8-4a55-3386-90ee-a9eed567318a | -14.38338 | -45.18719 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fd8fa17-e1b8-3469-8f01-c7216956c49a | -16.88407 | -45.75363 | 2025-09-12 04:27:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2a2d2dc-6a14-33b2-8e1e-bac8c43e64c2 | -19.20015 | -48.01312 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2318a1b4-9167-3ebf-9eb6-d05cd601e116 | -14.17786 | -46.17408 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 375d2c7e-90c1-386d-acc9-d7c78a452fcb | -18.4456 | -47.16913 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 905af717-9a4f-3d81-a6b9-5e0665b99136 | -18.67218 | -47.66624 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0978e40-7ad2-36c7-b10b-44356b0c5fc3 | -12.85289 | -47.95596 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7175116d-368c-349f-b0b6-e13405b9ee56 | -18.76418 | -48.53228 | 2025-09-12 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 41783195-34a4-3906-aca8-90f099ef1b4d | -13.17515 | -47.26521 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba619052-df58-32c3-8ec8-25cf1bb850cd | -19.23541 | -48.04152 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ad9bf0f0-bec4-3b8a-a16f-bedb1f4d73d6 | -19.19344 | -48.01199 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bb243f9f-3773-307c-884f-b22780f8c5ff | -18.06431 | -50.73225 | 2025-09-12 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 418e0d8d-4da5-377c-9f5b-7e35e52f984d | -16.28458 | -45.68594 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d775bc6c-2312-32e9-b576-8c75ca1c3a8a | -20.12118 | -44.89171 | 2025-09-12 04:27:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a26748bd-8194-3f9a-bd7b-61005af1a66b | -12.89481 | -47.97007 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58ed01cd-4fb9-3598-b9c8-122cbcf1026f | -13.38733 | -51.82641 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53485b97-8bdc-35f6-b8db-82c8a5faf20a | -16.62131 | -49.79446 | 2025-09-12 04:27:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01a44b9d-d489-34cb-88a6-a40aeba7bdd4 | -15.08539 | -52.43142 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6559dba-ae26-36df-8cd2-cb78c504a4d4 | -16.4328 | -49.04586 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3e8eb11-d198-38e4-a3ed-5ad50fe1348b | -14.16512 | -46.1883 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ad094dff-7605-3bc8-8737-94f28f8f7894 | -16.44309 | -49.043 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 575f2142-f53d-3219-a7cd-a349de02eea6 | -16.43236 | -49.02724 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47395eaf-dd6d-3b35-8e63-8598c2de6072 | -12.68512 | -45.05161 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05ff6b24-32af-33bb-9ee9-b11d88dd57bc | -17.5554 | -44.55924 | 2025-09-12 04:27:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5705824-dbc0-373c-ad2c-5fefcbf88e8c | -17.21459 | -48.6973 | 2025-09-12 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b116ff0-8da9-3a89-9245-56263bd85db4 | -15.1047 | -52.45239 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 796ff654-335c-30b5-8994-c5bba1bab61e | -15.10188 | -48.01189 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e749380-41d1-3e30-b7b6-948216946291 | -15.53088 | -48.54401 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c63f9c77-5c48-38ca-8c2e-edcaabe06582 | -14.18185 | -46.17079 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a450f1db-87a8-3ffa-a84c-2b8dfa333935 | -15.10399 | -52.45931 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54f2e528-db6d-3e9f-9566-69a53e01b2c6 | -17.24125 | -46.75463 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 406a91a9-0fba-3d7b-9872-def5bb75d884 | -14.42368 | -46.4002 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a8befa9-4fd6-3be2-83d3-1cb69e3ab52a | -13.89787 | -48.26228 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 102b5045-a91b-30d1-b255-b631ae9d7cc9 | -14.17048 | -46.20039 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48eaadb2-617a-3e28-b67a-67449d642ab0 | -16.10033 | -49.63341 | 2025-09-12 04:27:00 | NOAA-20 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0036aa9-03ca-30f7-8781-c49e57e44f86 | -17.20469 | -48.69555 | 2025-09-12 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ac64211-fc1f-3f76-8dba-a54521b7543f | -13.89792 | -48.24052 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcf1c3ea-7723-388a-8932-6cfd2f773640 | -16.66349 | -47.63 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c5d31b5-571b-30f6-908d-1fd6aa9f8190 | -12.89042 | -47.95492 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e43c801-225b-309b-affe-4891403eefd6 | -14.56678 | -48.75309 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 170a536f-5793-3a68-aef6-3db21b578317 | -19.87749 | -42.05039 | 2025-09-12 04:27:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 40dd93cd-d539-350f-a64f-d65aa5478d3a | -14.11919 | -44.32191 | 2025-09-12 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d3334ea-ec87-3c40-aab4-d195a91150e0 | -14.39643 | -52.93499 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a86f6ca-bde3-3999-bbe6-ac596ff8fe63 | -15.53638 | -48.55229 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc0fe02b-92ed-3cac-a632-4d2504c3191b | -17.8327 | -52.04892 | 2025-09-12 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e810239d-1d23-3005-95c6-7a8627faa355 | -17.37095 | -52.92237 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5efb4daa-6500-3bc5-ad2d-0450f4578154 | -15.80097 | -52.23624 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c9f3e95-d854-39e9-bb1d-ca0f84e0a6b9 | -15.60993 | -52.73774 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd828989-e25e-3eab-93c9-6677123e9b06 | -16.28813 | -45.68649 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3594822-6a34-32a8-b7cb-112fb4281e89 | -18.05319 | -45.44688 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4d63cc3-d5a0-3dfb-a1dc-66713dbd786a | -11.18571 | -55.08583 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ecac0de-0be7-30e9-9e5c-78c099ac7f2c | -12.46053 | -47.49389 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60cc67b3-d899-3c9d-943c-9226625306a7 | -12.24802 | -47.33332 | 2025-09-12 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bef115b6-a20f-3348-803c-789ab5e88aaa | -19.30885 | -47.50095 | 2025-09-12 04:27:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d50d5d27-0be9-3924-b934-fdf75a94e75b | -14.42653 | -46.40441 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15e43ce4-6f7f-3b03-bf58-97244bed954d | -16.41918 | -45.69918 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c7bbcab-ed18-3416-8dab-8e0af29b24ae | -14.27747 | -45.07014 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf695657-02cf-36e7-aeb4-52b6f2f623a7 | -14.18304 | -46.20988 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3afe033-cc07-3f10-8cb9-c88e0882e98f | -20.14539 | -43.6877 | 2025-09-12 04:27:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7afc916d-4b30-30ef-8a80-d24ed9306fda | -19.66438 | -45.85987 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 678e5b8d-9d63-3108-9b06-5e8a5e0b4e68 | -15.64054 | -41.8227 | 2025-09-12 04:27:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| addf757a-8529-3b3a-8c77-f28b4be0a03c | -15.69389 | -47.02757 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 998dba3c-e185-36ce-80d8-0cea66ba1819 | -16.44251 | -49.0466 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cb2e9ad-1523-3d79-ba70-79915efee9de | -18.68061 | -47.67919 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfb61c84-9cdc-39ae-88d9-eb296dff1b70 | -18.76828 | -48.19328 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa73833d-309b-3518-97ee-46d527ede27d | -18.32479 | -52.08465 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d977f97e-bcb8-3927-b766-bdfc03febdb0 | -15.10794 | -48.01656 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2eefb75-01ee-3a26-8670-c3545ed96870 | -13.06245 | -47.13735 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ea49aae-8e34-3d3a-9130-3489938ca892 | -12.97015 | -54.75542 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10f5a00e-563c-35f5-bd3f-65309a82677d | -15.88006 | -48.18096 | 2025-09-12 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af6e6598-bedf-3e72-a1d6-083b438668be | -19.26458 | -51.42716 | 2025-09-12 04:27:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a205ab49-7f82-3413-b1af-57bf3ec82bcd | -12.58288 | -45.68642 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1524fdd9-d57b-3bea-8f2e-f0593cfca976 | -20.15842 | -43.68518 | 2025-09-12 04:27:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 03ec13b7-8a92-35d1-bfc0-69543c18b710 | -13.89899 | -48.25522 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6451c75c-f72c-3f66-bee0-27ef00d6086f | -15.07775 | -48.01543 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a93988a4-ce58-3226-b55c-eaf8e53f948c | -13.90668 | -48.27099 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 98bbb3c6-856e-37c9-bcc1-40bb88076ba0 | -14.26736 | -49.66327 | 2025-09-12 04:27:00 | NOAA-20 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5258e4d2-8e0d-3893-9c61-f51ec78fb728 | -17.1382 | -48.49232 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50d59ef4-6ac1-32a2-8666-8ee5a5a6a4d7 | -12.98083 | -48.00529 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 596eb96d-bb45-3d94-9513-02153374b791 | -12.47959 | -48.92678 | 2025-09-12 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b181b896-4d72-31a8-a24e-f9913d78b921 | -18.38758 | -43.99294 | 2025-09-12 04:27:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README92.md)
