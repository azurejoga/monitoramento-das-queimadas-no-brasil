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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63d4bb8c-f864-3c33-9342-46ab1e58f02d | -2.83656 | -46.73649 | 2025-12-14 03:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dab7cfe9-661a-3063-ac07-96f9a761e58e | -7.24228 | -39.17781 | 2025-12-14 03:42:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ecccdf9c-d766-3902-9a78-717539680d94 | -3.3642 | -39.53773 | 2025-12-14 03:42:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e4bceb9f-db99-3c3b-a834-efb71b0cef01 | -3.31525 | -39.34677 | 2025-12-14 03:42:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2627051f-5de8-3edc-972c-a4e1182f2fda | -3.36491 | -39.8149 | 2025-12-14 03:42:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0f714e3a-7052-3a26-954a-29982a462cf4 | -5.39265 | -44.6833 | 2025-12-14 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3054a3ea-ce1a-34b1-b751-fc4d0595e240 | -5.34803 | -40.6883 | 2025-12-14 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5a0b8ac-b82b-3f38-b454-8276c8b51b4a | -2.21307 | -45.69242 | 2025-12-14 03:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c5f8f7b-aabf-3dff-a528-f159cb39983c | -3.43749 | -41.65184 | 2025-12-14 03:42:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1c5331d8-7374-392b-ae33-eee1f4382963 | -2.88287 | -44.96816 | 2025-12-14 03:42:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7637ba05-4317-3f16-bf12-d340a89bcf2e | -5.32684 | -36.80466 | 2025-12-14 03:42:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d711697-796b-3824-82fb-d39885657bc4 | -7.91608 | -35.28709 | 2025-12-14 03:42:00 | NOAA-20 | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c4749fb1-1ef8-38c8-b880-c56ae70f6c66 | -7.67254 | -34.95632 | 2025-12-14 03:42:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 65c1d657-eb0c-3953-ae6f-9ee98534931e | -7.66211 | -35.32549 | 2025-12-14 03:42:00 | NOAA-20 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9160858-1f27-34b8-86d2-9264ab694e0f | -5.93984 | -44.46334 | 2025-12-14 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fd9c37f7-f66a-3b38-8996-fca3b40476b8 | -3.43288 | -41.65108 | 2025-12-14 03:42:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 59099416-3aa0-3ffb-86ee-39f91510a19c | -1.52383 | -45.68281 | 2025-12-14 03:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8f4bfb2-2f5e-3938-836e-672fe4256cf9 | -6.53041 | -39.28469 | 2025-12-14 03:42:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 503c6789-2afa-3a47-b377-997d377d0137 | -6.19597 | -37.86469 | 2025-12-14 03:42:00 | NOAA-20 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43a6f456-2eed-3dca-bd43-510d3fb2f1b5 | -5.01048 | -41.279 | 2025-12-14 03:42:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62ae0de8-552f-3aec-9fed-4bed4826e1fd | -6.40412 | -41.08941 | 2025-12-14 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2e5e63f7-cb95-3790-a894-d54f3ec0d6e1 | -3.72129 | -43.75876 | 2025-12-14 03:42:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a006b4a-4165-3c5d-8530-cc7d3bd47662 | -4.94785 | -37.45186 | 2025-12-14 03:42:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 247e2a59-d16a-36ae-939a-f0ee2f918da5 | -5.39327 | -44.67978 | 2025-12-14 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a72e6f96-61c8-3c28-8ce7-71b124e31e8b | -2.47569 | -45.44099 | 2025-12-14 03:42:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b3ab054-611b-3bde-b096-f8e6fe0f337c | -1.52304 | -45.68768 | 2025-12-14 03:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 61d26646-b1c6-34e5-90ce-e92e4526d393 | -1.97216 | -46.48814 | 2025-12-14 03:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b60db50-4d7d-3b3d-907a-be509f080902 | -5.93714 | -44.46272 | 2025-12-14 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30eee280-4109-3469-bb5c-eaf30cd251c4 | -8.03052 | -43.0983 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 499e3f88-19c9-3cde-8186-33f376aed191 | -8.84562 | -35.16227 | 2025-12-14 03:44:00 | NOAA-20 | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c18b5200-93ed-3608-a9f3-c50b44b6835e | -7.21554 | -43.11354 | 2025-12-14 03:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4011d35b-3984-3e3a-b294-5a02c80056dc | -8.26859 | -35.48607 | 2025-12-14 03:44:00 | NOAA-20 | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5c516319-6e4b-383b-aa3f-fcc5188459e9 | -11.59202 | -40.15191 | 2025-12-14 03:44:00 | NOAA-20 | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 590b3961-b0a1-3ce6-a538-507ca78683e7 | -8.02961 | -43.10337 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 811a502c-4279-3384-b5c4-862ea5fe1fdf | -9.5423 | -35.95993 | 2025-12-14 03:44:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 031bd414-adb4-39f8-9f51-294d2ec019b2 | -10.14001 | -39.84678 | 2025-12-14 03:44:00 | NOAA-20 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5d6d4f26-dd4d-3c50-b384-129f14195791 | -11.71276 | -37.6438 | 2025-12-14 03:44:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 63d87d11-976a-3a85-a5a3-c41272c73696 | -8.67565 | -35.22891 | 2025-12-14 03:44:00 | NOAA-20 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 01fa05df-bbde-39b8-ac42-7897523a9100 | -13.33131 | -40.34026 | 2025-12-14 03:44:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ede9a7a0-258e-382f-b1ef-9b3765d7ca00 | -8.03613 | -43.0941 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| eddb726b-7d46-39ff-9274-74830678d875 | -11.71553 | -37.64795 | 2025-12-14 03:44:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 306fe60d-e999-352e-8458-d4fc0ce6d249 | -8.07433 | -43.15358 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0fea638b-5362-338f-aba3-239d6f51cf66 | -10.14406 | -36.27863 | 2025-12-14 03:44:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8000fb7b-b1bc-391b-a800-6c888e934b1d | -8.17104 | -34.98062 | 2025-12-14 03:44:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b7df7d1d-d35b-3b8c-bf61-be4fc869062b | -8.06868 | -43.15796 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0139b6c4-6810-3193-b8e3-0c5439a58f02 | -8.03993 | -43.10006 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ed5ea1b4-a3f7-3c4f-a206-9d2ee5de0930 | -11.08663 | -48.25807 | 2025-12-14 03:44:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc08d84e-342d-38db-a3ae-2ea63234f19e | -8.03142 | -43.09324 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5ac745ee-7938-3b67-be67-8594cecdd08f | -9.11268 | -40.46501 | 2025-12-14 03:44:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8d71f9bb-9fc5-39fb-9dfd-e5302d9edae6 | -11.09286 | -48.25937 | 2025-12-14 03:44:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f5b0035-6fe8-31ef-8a5b-dd535cd2209a | -12.31678 | -37.92208 | 2025-12-14 03:44:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f491f253-165e-32aa-b7c3-8bc07cc92db5 | -8.84894 | -35.1628 | 2025-12-14 03:44:00 | NOAA-20 | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ec104152-553f-3a94-9d16-5837e050ead0 | -8.06959 | -43.15279 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 48c4f6ff-39e5-3c3a-a1ab-3b5021ca87b2 | -8.03523 | -43.09916 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f64add4a-9e6d-329c-8e12-2e99112213bb | -8.06484 | -43.15205 | 2025-12-14 03:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3be8b728-5506-3b4c-a15e-ec9fe8be38ee | -11.71218 | -37.64738 | 2025-12-14 03:44:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 035c597a-6989-3142-b5ee-e2193ee82e8c | -9.11242 | -40.46332 | 2025-12-14 03:44:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 90fe7485-a7df-3e0c-b529-293874cb54ef | -17.00532 | -39.77727 | 2025-12-14 03:46:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 25cdd06b-2045-3bd9-b0b9-943bec1ab24d | -17.8983 | -40.1151 | 2025-12-14 04:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 138.5 |
| eeaa5a87-515c-34d0-a57b-1e0a45d9e037 | -17.9186 | -40.1095 | 2025-12-14 04:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| 2c869d7a-8829-3725-8e36-d0f269792bb8 | -17.8991 | -40.089 | 2025-12-14 04:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 72.1 |
| 337f50a8-4d87-3d3d-8951-7b784c1f0bb1 | -3.51341 | -52.18568 | 2025-12-14 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0524e0e-1da1-330c-815d-0bb45bf52d79 | -2.13793 | -45.4561 | 2025-12-14 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8504b5d5-c738-3dc3-bf21-99f8bccfb5c7 | -2.88797 | -44.96368 | 2025-12-14 04:31:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e58f2fb-a6c0-3491-8eb5-a25a4ab61d56 | -2.97212 | -54.32745 | 2025-12-14 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1209768-5a51-3a30-9289-f867c4647fb4 | -3.44127 | -41.64587 | 2025-12-14 04:31:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f38e251c-5251-3f6a-a843-c33987ead03e | -4.93081 | -43.95965 | 2025-12-14 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa9a5f3e-38dc-33ae-9590-efadc966cc7b | -3.22429 | -46.86454 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a66118b2-9d8c-3693-aedb-56a747f9281a | -4.69588 | -43.24397 | 2025-12-14 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c676f40e-f9d3-3935-9230-d60b1c4602d5 | -5.67443 | -39.26785 | 2025-12-14 04:31:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f51984f2-e5f9-3ab2-9c88-10fcc5511def | -4.69058 | -43.25295 | 2025-12-14 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ff07e02-1e44-3a3a-8619-2024515f1d5e | -2.8883 | -45.3699 | 2025-12-14 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c897aa14-f28a-3234-a824-6bfd7255fd63 | -5.99077 | -44.59354 | 2025-12-14 04:31:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a82a68c-8c21-3375-82c1-0eead847db9c | -5.67358 | -39.27388 | 2025-12-14 04:31:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90146632-e51b-32cc-8cea-654e64a2a080 | -3.30568 | -42.53609 | 2025-12-14 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a140266-6aad-33d8-935d-64107428709c | -5.90617 | -44.36071 | 2025-12-14 04:31:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 905fdd11-79f3-3138-86f0-42d1326bf0ab | -3.31316 | -42.19991 | 2025-12-14 04:31:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 09a3efe2-7549-379a-a042-3ce446c9ac75 | -4.69973 | -43.24454 | 2025-12-14 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89ec13c4-b6a3-3e92-a93c-3af23f0bd098 | -4.3462 | -43.63532 | 2025-12-14 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 369518bd-b0a5-385d-8aaf-7e8307d926d6 | -5.67401 | -39.27082 | 2025-12-14 04:31:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e2910b7d-720a-3e99-988b-9f4e4446606b | -1.29105 | -52.88001 | 2025-12-14 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13e81a87-c02a-3156-a41d-cddd240bbc6d | -3.37566 | -44.88814 | 2025-12-14 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e3b8c14-f9ab-3211-a8cb-da294dc2b9d9 | -2.46585 | -44.18007 | 2025-12-14 04:31:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac377916-8f0a-3173-a7f6-02b882569b70 | -1.50443 | -53.99287 | 2025-12-14 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a07200bf-fb41-3658-a7d7-f7615177d59c | -3.15166 | -54.6069 | 2025-12-14 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b98da96-e713-3220-8be3-79a7f03c8093 | -3.42635 | -52.8986 | 2025-12-14 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 564c87a5-8b40-34f4-bf28-fa281cfa47c7 | -3.43653 | -41.64903 | 2025-12-14 04:31:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| df98261d-c73b-3342-9bff-a6f4a04ef82e | -5.98352 | -44.59248 | 2025-12-14 04:31:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 225a243f-6a69-342b-b5fd-88c70d756f67 | -2.96897 | -54.32957 | 2025-12-14 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9469b07f-8a1b-3a2a-a8bb-c5375f3c808f | -2.66476 | -46.89695 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e77b847c-ab8c-302a-a5ae-8e608c3543a3 | -3.43541 | -41.64913 | 2025-12-14 04:31:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| cbfe9234-1381-3b9f-9cdc-edee06fbb77d | -1.14536 | -46.75985 | 2025-12-14 04:31:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44f2f701-a328-3816-962c-4e7e06c46916 | -4.17225 | -44.02231 | 2025-12-14 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79f39413-0820-3f37-9553-c18cf3911a4c | -2.48151 | -45.43415 | 2025-12-14 04:31:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17bffe7e-7f1a-348a-9e20-7768466322fb | -2.83709 | -46.72985 | 2025-12-14 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8abc4526-a104-3b38-a43e-e140a1b5fc1c | -1.5278 | -45.68227 | 2025-12-14 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8641e87f-9e0c-394a-8baa-aa56d881af7b | -4.40387 | -45.77487 | 2025-12-14 04:31:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4008b22e-64eb-3810-ab27-a3a4c9b7ad3d | -5.83851 | -44.92852 | 2025-12-14 04:31:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 453d5196-91cc-3d2b-9d98-576722bb6a2e | -6.59312 | -39.56883 | 2025-12-14 04:31:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46647c54-188d-32c5-b151-6561600ab3ad | -2.58731 | -44.95738 | 2025-12-14 04:31:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
