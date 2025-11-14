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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 197477fe-8283-3ddb-8787-a85209118031 | -15.54987 | -43.17369 | 2025-11-14 03:55:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 35901e39-d65d-3413-9f52-b2e34af530bc | -14.9866 | -42.41503 | 2025-11-14 03:55:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e21f642-6cbb-3a0a-acc4-fc17004f7f04 | -4.45628 | -45.82302 | 2025-11-14 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6149e8fd-ba73-3852-af43-a219458c3b8a | -11.85441 | -49.22 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 0be43cda-977c-312b-b580-b69e158a96b3 | -11.55993 | -44.94522 | 2025-11-14 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 697eb2bf-0f68-3cbf-82fd-0f7f7725cb88 | -11.93706 | -43.94724 | 2025-11-14 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f7087727-15fb-3168-91f4-3e0f1a3c9f89 | -11.74555 | -48.52868 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3cccc14-3fb2-325a-aa95-1ac1c8273ea2 | -11.85576 | -49.21285 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8a2b4ece-580d-391d-a996-fb263c8885bd | -11.84965 | -49.21535 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 9d70db37-d446-3897-9fd2-81599795caa0 | -10.75861 | -44.91494 | 2025-11-14 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f3d08e3-86d2-3cf3-9cf8-0aae61380b46 | -4.60444 | -41.7408 | 2025-11-14 03:55:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 75d6be6b-8bec-36e7-b831-001a4b2eca00 | -10.05701 | -44.76841 | 2025-11-14 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| debcf34f-90db-3337-a28c-5ae5926cb097 | -12.71147 | -45.42091 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dee22958-0b30-3282-9cda-32bb77e3b91f | -4.01401 | -41.6912 | 2025-11-14 03:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7e2b01d6-4879-3a6a-b655-8c69740e2c07 | -13.59963 | -47.06233 | 2025-11-14 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4386fd70-6bf9-37d1-9d09-319253d262c7 | -2.63317 | -47.29769 | 2025-11-14 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ec0dc549-3b05-3f62-a9cb-3a3e20c98dd6 | -9.66634 | -43.90063 | 2025-11-14 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5ffd2557-b9ac-3242-ad7d-9eb26ff7fea1 | -12.71982 | -45.42247 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 34976bd7-b460-35ea-87ab-1da39c51148b | -10.75255 | -44.5618 | 2025-11-14 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00fb1f0b-2a88-371a-8a90-091289f6ad10 | -4.24113 | -42.33295 | 2025-11-14 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2663126a-128c-3c65-85b7-7ae8e1f09630 | -13.60469 | -43.56628 | 2025-11-14 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8013661f-b33b-3cf3-89c1-e8f8eb6f06ab | -4.07175 | -44.13317 | 2025-11-14 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee4f240-2401-3729-8df9-38aba8abba55 | -12.06303 | -48.20565 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84e93a81-abcd-30a1-9bd8-00d168730826 | -10.05871 | -44.76509 | 2025-11-14 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 044209a0-8cf3-3cb5-a2a1-eba4cb83a139 | -5.02542 | -40.60515 | 2025-11-14 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df5f6213-9ce6-33ef-95fd-ccc0635117e7 | -2.44937 | -48.81924 | 2025-11-14 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fcccb47-a252-33aa-8999-e386480d31ff | -3.53127 | -44.84735 | 2025-11-14 03:55:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39fed949-756e-3d22-bd6a-98f629c34d7f | -15.64845 | -46.1704 | 2025-11-14 03:55:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fed2077d-d09d-3ae2-9fa7-76855ee2cb11 | -2.23733 | -46.07788 | 2025-11-14 03:55:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad240cc6-a239-3533-98a3-e2920d1b6357 | -3.05534 | -40.8136 | 2025-11-14 03:55:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8b80b9b6-3863-3e45-af41-411ce98ba6d9 | -13.28655 | -43.85737 | 2025-11-14 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a6a6aaf-e01e-3b39-94c2-420f32696330 | -11.85038 | -49.21729 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 3e2a3adb-60af-315b-98c3-17d46dc0a8d7 | -14.69924 | -46.61705 | 2025-11-14 03:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0aaa23aa-c695-3501-aafe-5854cecb5aa0 | -10.75443 | -44.91426 | 2025-11-14 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 540d6403-3856-3a77-9efc-764f017bd143 | -13.32868 | -43.17798 | 2025-11-14 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75a78d27-7fc8-382f-b9fe-2d3535e70e17 | -3.7723 | -46.00649 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5be8613-c52f-354c-a370-5ec44e15e56d | -4.06458 | -43.06233 | 2025-11-14 03:55:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60914aac-5f70-3c8a-9c0c-9d4feeb2af01 | -3.4418 | -42.55098 | 2025-11-14 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48ce7c93-f22d-3e37-8e5e-5f37257e5453 | -14.98724 | -42.41116 | 2025-11-14 03:55:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 49c30a5f-9176-36b0-b36a-14956152403b | -10.75775 | -45.01953 | 2025-11-14 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f8fe9ec2-38eb-365c-9f03-150a77202e1e | -2.94298 | -49.36047 | 2025-11-14 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51966313-a9d9-338b-872e-608cba7b3069 | -12.99705 | -43.8649 | 2025-11-14 03:55:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5187e722-ab5c-3d27-b42c-2367e48122e8 | -8.90454 | -44.4401 | 2025-11-14 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd1b1968-0f47-347b-8554-5d6d1d3b2ac4 | -12.45227 | -44.63448 | 2025-11-14 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf10d3d9-386e-32ce-8f05-eb3db6266004 | -12.62596 | -48.40402 | 2025-11-14 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f1bdaa6-aea9-39f3-94e0-96d1f2def728 | -3.3991 | -44.71427 | 2025-11-14 03:55:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 070d8aa6-6bff-32a1-9f05-846dfd87676b | -13.27564 | -44.259 | 2025-11-14 03:55:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bcbcbc63-2ae8-35a3-9341-b6b85d77c2f1 | -3.38696 | -41.15374 | 2025-11-14 03:55:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fe0c6c16-9a40-368d-88d3-3a4dd80c6611 | -14.28382 | -42.83707 | 2025-11-14 03:55:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94cd56a5-e376-31b1-9642-fc4cd5b10bca | -13.688 | -43.00953 | 2025-11-14 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2b02eb1-7d2a-34d5-aa75-06432e47311d | -13.92032 | -42.88157 | 2025-11-14 03:55:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9081d3dc-8a05-38da-b7b5-23521137e542 | -12.06245 | -48.20866 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0818ef8-72bc-32b3-90e9-a8e4db781262 | -2.11418 | -45.36546 | 2025-11-14 03:55:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ca1eff8-d163-3384-bb54-c2c0b0ead5ce | -14.67678 | -46.56779 | 2025-11-14 03:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 24777bce-0eb2-3bc1-9aac-3678f9b7eac0 | -11.93321 | -43.94656 | 2025-11-14 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1fbb0c64-0ef5-3919-9eff-be0de4a5e711 | -3.80828 | -45.03627 | 2025-11-14 03:55:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a30aab06-5642-38d3-b67b-e24b5aa2d651 | -12.01688 | -46.7703 | 2025-11-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7512f4e-0204-3420-a1e7-4468424f21bb | -4.60638 | -43.35285 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0ff6ffcf-52c9-3837-8183-3ccc0c48891e | -4.71566 | -42.94234 | 2025-11-14 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 53dc021d-f0c7-3365-a742-2414fe21332f | -3.20295 | -43.47353 | 2025-11-14 03:55:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c56c059-48e7-3c75-ace1-352ece66a2c3 | -14.67259 | -46.56612 | 2025-11-14 03:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7b03437-188b-353f-9cb9-47213746eabe | -4.37298 | -41.73088 | 2025-11-14 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ed295145-3f9a-3f0b-aaf9-785fdf5d36f2 | -12.44512 | -43.7478 | 2025-11-14 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bda4abf3-3c87-3f85-8186-72022691d19c | -10.88249 | -44.39088 | 2025-11-14 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 951068e9-7b05-30b0-8270-559726152e62 | -3.76724 | -46.00567 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ee2a677-5654-37f0-ae47-d134debff39a | -11.80679 | -44.26052 | 2025-11-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f7b1d7f-78d3-31e9-b350-dbe3a54e2389 | -14.28113 | -45.36092 | 2025-11-14 03:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21851a2d-2e75-3e56-8f45-f4df634c365e | -4.64564 | -42.95916 | 2025-11-14 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8869bae7-d1d4-39b6-8777-7a1c7c341179 | -11.85983 | -49.22672 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d394d198-b112-3fb6-8cdb-51e8942a0cc1 | -13.72893 | -49.13404 | 2025-11-14 03:55:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f34910d-b2af-3c6e-aabe-3e723530abf6 | -3.9538 | -47.49827 | 2025-11-14 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d372a447-fe6e-33b9-b044-8de41c0fd0b0 | -4.7203 | -42.93944 | 2025-11-14 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eafed766-b0c6-392a-9d8d-84eec1ecb0c9 | -12.58794 | -43.36139 | 2025-11-14 03:55:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee2409b0-dce0-3744-bc6f-8211e28ee973 | -14.98608 | -47.86709 | 2025-11-14 03:55:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 097cfe92-3890-304f-ad7d-936320f6edbf | -11.74033 | -48.5277 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a447ad9a-7381-3915-86eb-87b2db518f02 | -2.83578 | -45.483 | 2025-11-14 03:55:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b928c82a-6d60-35eb-84c4-7ebb1d2cc2f0 | -14.05312 | -44.48129 | 2025-11-14 03:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69e04871-1a4b-3844-a5f3-7f5faee9288a | -3.80396 | -44.39592 | 2025-11-14 03:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56249b8d-1d67-3c86-8402-cb11931f5468 | -9.95343 | -44.94076 | 2025-11-14 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8be762d-7dab-3feb-81c5-e292020d5307 | -14.35287 | -47.89133 | 2025-11-14 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5909abd9-85b0-3a34-8013-9e9e294e02b0 | -4.45002 | -44.00742 | 2025-11-14 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e47d9b05-39c2-3f04-a533-7e53e3d57b2f | -11.72653 | -48.51487 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 692de33c-062c-33bd-83e8-b955cf08e6a4 | -4.63111 | -43.27942 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cccd4f61-c3c5-3b53-bbb2-947cae59b53f | -10.51894 | -40.32994 | 2025-11-14 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 531297f8-5e31-31fb-b820-3363589fce27 | -4.60975 | -43.38461 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8b030e62-43c7-3a98-8641-a9d2024977fe | -13.46947 | -46.49333 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a518919-8f76-38db-bd18-357caf009029 | -16.47499 | -42.17258 | 2025-11-14 03:55:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2a6777b0-0075-3665-a44b-2f396175434a | -5.39998 | -37.86163 | 2025-11-14 03:55:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 82fdfe32-7b14-31e9-8cfb-d7b6dd175250 | -5.3269 | -35.55407 | 2025-11-14 03:55:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 60bcc442-9db2-3411-b8ec-22e366701b04 | -11.84896 | -49.21897 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 231e1cf2-f0ee-3e47-8f07-f310788204d7 | -3.06284 | -40.08171 | 2025-11-14 03:55:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50dd95a7-1171-33ce-aa9d-d2d9addc4b71 | -10.63533 | -44.82538 | 2025-11-14 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa6f4cd0-875b-3a15-b205-578530a8224c | -4.04165 | -46.12331 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d93f2a41-88bf-3d25-baf5-f1ebb9805384 | -12.68848 | -45.42886 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b3f6c69e-a427-3009-89b2-1fe2862acf3a | -3.35703 | -48.39693 | 2025-11-14 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46522c0a-e648-3b1d-9120-b514debccd2c | -14.69832 | -46.62207 | 2025-11-14 03:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 92e3a9ee-c2a1-375d-a1cf-5bf6bbb0015b | -2.23786 | -46.07473 | 2025-11-14 03:55:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3efe9896-fa65-3c40-a1cb-5f4a07a66df2 | -10.05801 | -44.76898 | 2025-11-14 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32a3d34d-be4e-3b1c-a80f-58bfc46126d0 | -11.24957 | -47.5003 | 2025-11-14 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28d402c4-84dc-35a2-b151-e0a87866aba1 | -9.00347 | -44.17315 | 2025-11-14 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README20.md)
