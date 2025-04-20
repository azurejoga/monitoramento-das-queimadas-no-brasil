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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c463b7ed-45d8-388a-9f4d-7b340589a09b | -10.65017 | -44.40572 | 2025-04-20 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b3179bc-f5da-37bf-89d9-c8ea3539191a | -13.34007 | -43.3798 | 2025-04-20 04:21:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 466afec8-7082-3ad8-8c16-158a85e51c9d | -10.6468 | -44.40519 | 2025-04-20 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d7b90df-d8c4-34c6-bf15-0a9760fa561f | -10.64343 | -44.40466 | 2025-04-20 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16790aad-80a7-3eb8-ae04-f921958403fe | -11.47267 | -41.94555 | 2025-04-20 04:21:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 058a334c-cb83-3cbe-956d-fc0caf3ea4c0 | -15.0794 | -48.94353 | 2025-04-20 04:21:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0390a500-f9de-38a8-9616-22e9669cdcaa | -19.72844 | -49.79367 | 2025-04-20 04:23:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0d51dd71-9c4b-30e3-9784-31eb3d51bf90 | -19.97103 | -44.21716 | 2025-04-20 04:23:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e7503ce4-3331-3df1-9e54-1156dfb45985 | -20.326 | -47.73467 | 2025-04-20 04:23:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e815ad29-8410-34b7-b513-595b47c23f9e | -18.38296 | -47.60553 | 2025-04-20 04:23:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ad362c8-8f2b-3948-8a0f-ba3a392c9651 | -18.38507 | -47.60533 | 2025-04-20 04:23:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 367d8dab-002f-3f83-bf90-c9da5b69f534 | -18.38353 | -47.60189 | 2025-04-20 04:23:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e86fcd55-075d-3f01-ab81-0859e6077da1 | -15.57034 | -47.85464 | 2025-04-20 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 624092bb-edcc-3427-8a29-103d9f5ce686 | -19.36889 | -48.60667 | 2025-04-20 04:23:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9dca3df6-4714-33d1-bae5-8b64599d8929 | -18.00836 | -51.38283 | 2025-04-20 04:23:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de6ab70b-178e-33b6-992a-2a3e7af88921 | -16.68241 | -43.88512 | 2025-04-20 04:23:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d1eedf8-59a8-3fdd-bff8-a86efdfd3ebb | -16.34884 | -43.69508 | 2025-04-20 04:23:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb6266db-e775-3cdc-9d88-5de1076331a3 | -17.77918 | -42.8094 | 2025-04-20 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f98a76d1-a935-3f29-b365-0273649caf93 | -22.69669 | -43.3458 | 2025-04-20 04:25:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 614ba6d5-9b96-3811-8634-5737c3525df8 | -22.70069 | -43.34648 | 2025-04-20 04:25:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4de166ae-cd58-3db7-9ee8-7121d39e246e | -22.78429 | -43.75868 | 2025-04-20 04:25:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 057db3bf-d502-38ad-adcf-a863aba6cc82 | -24.24295 | -50.73922 | 2025-04-20 04:25:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5735d2e7-a00b-380b-ac6a-f87541d1b6ab | -29.62865 | -51.97136 | 2025-04-20 04:27:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf48cae8-59db-36a0-ab73-9d3aa599b2ea | -5.4839 | -43.33719 | 2025-04-20 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fdfdcce6-e9a7-30b9-be47-daa85ed902c8 | -5.41194 | -49.08117 | 2025-04-20 04:42:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc09cb97-0944-3b3c-9403-809ad16a3832 | -5.36641 | -49.19637 | 2025-04-20 04:42:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83e127a6-68dd-31aa-b65f-a400636f6b26 | -5.79457 | -43.62125 | 2025-04-20 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c222518-7b68-3ef3-b396-6396d930a4df | -2.9888 | -52.74995 | 2025-04-20 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54de55ea-71ec-3a49-b7c5-138cb609c6b3 | -6.305 | -46.05532 | 2025-04-20 04:42:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a98acef5-529e-3124-943e-b723a67aea4a | -3.06705 | -52.23623 | 2025-04-20 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fc2d96a-c2bb-3984-beaa-a85de296ea8c | -3.08894 | -51.19886 | 2025-04-20 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d32af261-fc3e-3e4a-9486-665b2c143803 | -5.48463 | -43.33214 | 2025-04-20 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 507881c1-ba65-333b-a5ca-1514e8307e1c | -6.60654 | -47.32935 | 2025-04-20 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d5f4cc8-7140-39de-b378-be1afbafa019 | -11.47241 | -41.94614 | 2025-04-20 04:44:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34823fa0-b1c7-3333-a45f-719610cedfab | -7.0673 | -44.37149 | 2025-04-20 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4dde6a04-6b0b-3a38-914b-5bd412f069f0 | -7.07114 | -44.37689 | 2025-04-20 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3256674-80e2-3422-895d-71b1551206c4 | -7.07631 | -44.37284 | 2025-04-20 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79ccf3af-0bd8-37ec-94e2-43089dd246ff | -7.08402 | -44.38334 | 2025-04-20 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 898dc31b-c20c-326d-b56f-b4b1fc20a403 | -6.61025 | -47.32988 | 2025-04-20 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea332412-4f8b-3cc9-a5db-59c316cdaed4 | -7.07565 | -44.37753 | 2025-04-20 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e8518bc-27d1-3fdc-a4bd-93025c4019ac | -7.07181 | -44.37218 | 2025-04-20 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0041bf5a-8fa5-37f4-b3f3-338d1fd8ffa1 | -7.06663 | -44.3762 | 2025-04-20 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5003658a-4f80-312d-9258-41840bbbf1d6 | -7.07499 | -44.38218 | 2025-04-20 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eec07817-200f-3d86-80e7-cb8723a3a3e5 | -18.94735 | -49.47842 | 2025-04-20 04:46:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2ad4596-80fe-37b4-a565-a43591b07c00 | -15.0782 | -48.94508 | 2025-04-20 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46489405-25b6-319f-a30f-fe005b80f787 | -16.68018 | -43.88311 | 2025-04-20 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acfd792f-e408-3123-9196-8596ec9d989e | -18.38067 | -47.60394 | 2025-04-20 04:46:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa9b06f9-472e-3014-8a3c-6209c9108f51 | -15.56809 | -47.85486 | 2025-04-20 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25cf18e1-bc76-30f0-8b33-48aba5fee55a | -16.34912 | -43.69761 | 2025-04-20 04:46:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a8b47a8-c096-30c5-98cb-9a75a40abe5c | -20.32673 | -47.73451 | 2025-04-20 04:46:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5759acca-797b-320b-b54c-5d6aef3785e5 | -18.38495 | -47.60445 | 2025-04-20 04:46:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2c38574-e9f6-31c2-83d8-d141e7bf83c3 | -24.24304 | -50.7392 | 2025-04-20 04:49:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bb22f9c3-9705-38ed-a326-50808028dd18 | -29.62893 | -51.9684 | 2025-04-20 04:51:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 038fdf2c-e4e0-33c1-9666-500ad9c783d0 | -7.06341 | -44.37524 | 2025-04-20 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 612869a5-c598-3746-9168-de4c30906b80 | -7.07234 | -44.37655 | 2025-04-20 05:33:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 871affc2-cef3-3af2-ad3b-fbb6748cdbe0 | -2.98985 | -52.75006 | 2025-04-20 05:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f028ac1c-691d-3273-b81c-3e1d9df1348d | -2.98797 | -52.74752 | 2025-04-20 05:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20c86fc8-31c1-3175-bfef-584349048bb5 | -9.53602 | -63.33162 | 2025-04-20 05:36:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19b76d8b-5386-3fd3-a09e-9f04837f84fc | -7.52409 | -63.26188 | 2025-04-20 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 384d187c-075b-35b0-a06a-db3bf93e2cf7 | -10.37994 | -63.16502 | 2025-04-20 05:36:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a2f3bcc-4839-32a2-9c46-5f195d013cfb | -18.38403 | -47.60005 | 2025-04-20 05:38:00 | AQUA_M-M | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 57e53517-46e1-3282-a366-bcd2c3083c5e | -9.07823 | -40.38472 | 2025-04-20 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| ab547107-a0cc-353e-8fff-ef4fd055ecc7 | -11.99986 | -40.92065 | 2025-04-20 12:14:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| ef0eebfe-e45a-3948-95f4-a5fc44719807 | -9.31099 | -44.65051 | 2025-04-20 12:14:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d5d332a9-e28d-338a-8030-5ff202b078d5 | -9.08008 | -40.37987 | 2025-04-20 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 66105b4c-6a4b-3b2f-ac56-983e742ea0a3 | -7.07103 | -44.37682 | 2025-04-20 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b072d142-0a33-3bdc-8ba3-6251d6ecf037 | -10.64856 | -44.40525 | 2025-04-20 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 29d960ef-9914-3d5c-b2a7-0e1f29296ddb | -8.52327 | -36.91984 | 2025-04-20 12:14:00 | TERRA_M-T | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 523d47b8-1ad0-3ab5-8b75-2653d2acc2d0 | -10.31865 | -39.12245 | 2025-04-20 12:14:00 | TERRA_M-T | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 1a17e109-9c89-3d60-be83-f8473e49cd0d | -4.11007 | -41.49424 | 2025-04-20 12:14:00 | TERRA_M-T | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6da66d2e-5100-34fe-b9d9-f3f0262d0197 | -15.30374 | -45.32024 | 2025-04-20 12:17:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 78911b78-5eec-30e4-a989-26f8181e244c | -18.3831 | -47.60494 | 2025-04-20 12:17:00 | TERRA_M-T | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6042243f-b7ae-3a35-bca6-693d8a4d5379 | -16.0645 | -43.65646 | 2025-04-20 12:17:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |


