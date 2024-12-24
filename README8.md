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
| 9246440b-4e03-3479-bff5-341b64af391c | -1.73967 | -53.15207 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a968a63d-2563-3684-8a61-99bb1f368a68 | -1.90967 | -52.66527 | 2024-12-24 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbfa8764-ed25-35bc-ab3e-a8a23903ef7f | -2.19528 | -45.6825 | 2024-12-24 04:36:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b08628de-c26a-33ff-b8b8-afcb86b49df7 | -3.21426 | -53.10033 | 2024-12-24 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49323b0f-19b5-3bcd-ac4a-bc38f97cd81e | -3.18498 | -45.9721 | 2024-12-24 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cc01782-1147-3c20-9102-9546326a4f25 | -2.60777 | -46.07556 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e61b95a0-5b0a-3d89-bb0e-bce70b807d14 | -5.20757 | -45.61902 | 2024-12-24 04:36:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d019808d-17eb-3c51-9ab0-5d3c660a5a50 | -2.03799 | -46.4686 | 2024-12-24 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcf6c649-55f6-3666-a2bb-5e27e31e3f23 | -2.9252 | -51.58319 | 2024-12-24 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f23de879-bfae-3187-b153-e2a91f3d67e0 | -1.70352 | -46.43373 | 2024-12-24 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdf6bebe-27bd-3252-8b1c-fff8bfcfe635 | -0.62058 | -49.62137 | 2024-12-24 04:36:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2ed36ca-554b-346e-80a2-44139947edbe | -2.35087 | -45.59106 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 17338be3-fc75-3161-8ded-017dacaa2200 | -3.02353 | -53.89408 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b60b5e14-ac94-3311-a747-64a8edd0ce0d | -5.96477 | -44.29039 | 2024-12-24 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc1ca23c-947c-34d5-a34c-8cc36562138e | -1.51982 | -54.95456 | 2024-12-24 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0acaa24-453f-37ca-873a-2cb4ecda05f5 | -3.0571 | -53.79218 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aca3e14-5a95-3b47-b849-90983460cb02 | -2.21965 | -47.0317 | 2024-12-24 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73964378-b231-34ce-8f8b-b846ac5f0826 | -3.14452 | -53.18481 | 2024-12-24 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78821dcc-57fb-30c5-9ad0-5047f3b6f3dd | -6.95388 | -43.5423 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 880f9fef-63fb-327b-9afb-e41b985ec6d3 | -2.97843 | -54.1336 | 2024-12-24 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34691ab5-b675-3b6c-b26b-3ba8a8846cd3 | -0.72769 | -47.79467 | 2024-12-24 04:36:00 | NOAA-20 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20d43350-8cc0-3bf5-bd7c-1cd9e06e6d2f | -1.58037 | -53.334 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7761cdc7-e8ea-315b-a206-86cfc70122ad | -2.37524 | -54.61993 | 2024-12-24 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f97ee0a4-6b35-3932-b3e5-abe9bea9ec8e | -5.38621 | -42.95395 | 2024-12-24 04:36:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4827b5d1-0ad2-347f-b522-7749d5378ef7 | -5.98388 | -45.39187 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76864591-3ffa-35c6-ac23-6e7d7166a1ec | -5.38996 | -42.95883 | 2024-12-24 04:36:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 33c55bf2-3755-3ecd-b315-9f6ba91a68a7 | -3.15057 | -51.55453 | 2024-12-24 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b19d80a-e934-3e00-b60b-eeeab53dd90b | -2.77253 | -45.0953 | 2024-12-24 04:36:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6307558c-ba56-3056-a91c-e0c2d82edd22 | -2.11937 | -45.49641 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c739a08-c560-3503-8fdc-e54f341d4b7e | -2.01407 | -45.59192 | 2024-12-24 04:36:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd5e78b-d322-39ea-9410-46d10c492a9c | -2.1093 | -45.49071 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f04b1f74-7b77-3f23-87b2-fb1920708640 | -6.1945 | -42.63826 | 2024-12-24 04:36:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 63ac43ef-d97a-3cc9-9fc9-28437124b579 | -7.87963 | -38.55227 | 2024-12-24 04:36:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f283165b-caa9-3e33-af44-2e6a2dac76b3 | -2.72044 | -46.17364 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f58c2b6c-2c59-317a-8c22-7b4b11edca6a | -2.73714 | -45.8744 | 2024-12-24 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0eddf498-d470-3f6a-a8a7-b148c3375be9 | -2.41063 | -54.22054 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b5fad829-ba5f-3486-8571-5cef81a2c2f5 | -2.60717 | -46.07941 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c26df62-287d-3e69-9685-18f07f937f54 | -2.58155 | -51.81381 | 2024-12-24 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef69cc1d-75b3-37d7-8318-bdb196cf9a61 | -5.63834 | -44.30499 | 2024-12-24 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2140608a-99da-3244-9143-978270fc9b6b | -2.35784 | -54.6171 | 2024-12-24 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f5df7ea-a088-39f4-9339-278dc83199ba | -2.09014 | -45.36373 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cedfa79d-6b47-33fd-b393-fea860adb428 | -4.51142 | -42.069 | 2024-12-24 04:36:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 35454193-2544-3520-810a-f1f0b47481c0 | -1.47164 | -45.81795 | 2024-12-24 04:36:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 032d8569-6f65-3b74-b960-6a5a7689e4bc | -1.67902 | -46.83926 | 2024-12-24 04:36:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53a815fc-dc2a-3e05-82a1-9edc6e38c502 | -3.13027 | -52.12831 | 2024-12-24 04:36:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 068310d2-79e8-3624-8441-c4f1ede5dd5a | -4.52621 | -45.82742 | 2024-12-24 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ffe3031-6be1-397e-a8df-f7387a880128 | -2.47224 | -54.16069 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b51f5a72-4a61-3b84-934c-94925786e4cf | -2.53302 | -54.15874 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ed9e76f-2ffc-3f0a-8809-04119a742b97 | -3.08987 | -52.07946 | 2024-12-24 04:36:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42e572c7-1554-3f01-aaa6-d7017de09b3c | -2.08868 | -45.36265 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1d3b21ae-2020-345f-bb44-ccf1c2e68cc4 | -2.99034 | -51.44279 | 2024-12-24 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| feef95dd-278e-3307-8458-2466ea8f9bbc | -2.64299 | -46.11134 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b284e9d-dc33-3715-8fc4-b306e3520e55 | -3.03113 | -53.89909 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5039aa08-b094-3cad-97a0-dc890ef4183a | -2.99616 | -40.3922 | 2024-12-24 04:36:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 93b42150-8d6b-34b1-bce6-acb609694b2e | -2.37959 | -54.62064 | 2024-12-24 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d271d4c9-2284-3ccb-a2ec-40d9f44d40e2 | -3.0565 | -53.79583 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e22026d6-2f94-31bc-b225-895ea9cd5c4d | -2.76745 | -52.65079 | 2024-12-24 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 897535da-8fd1-3796-80cd-16ee173e721d | -6.97413 | -43.55356 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c2473e99-31d1-3522-b3ff-e2f9f7e17b2d | -1.78995 | -47.84422 | 2024-12-24 04:36:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb40d8a8-b739-324c-bc43-91978bf4b6e8 | -2.92585 | -51.5791 | 2024-12-24 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78e3d72e-d7b6-3204-8e7d-4473e6b03951 | -2.59129 | -51.94086 | 2024-12-24 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d0858ea-e65e-3cdc-a4ed-4ca727c80166 | -3.03583 | -53.89613 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b32c558a-6163-31de-8c56-a8f3af40849d | -3.75581 | -52.38316 | 2024-12-24 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c960af8-6118-3d50-9417-9a9f8dfcb098 | -2.99114 | -40.39142 | 2024-12-24 04:36:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 48e05ce5-8044-3123-87ba-93c1f571d138 | -3.08881 | -52.08197 | 2024-12-24 04:36:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c02dc997-9b90-3f60-9979-f9c1ae732209 | -3.02823 | -53.89111 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7438d228-5118-3b4b-8130-8d7479821a6e | -4.30127 | -40.69904 | 2024-12-24 04:36:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4243237b-7c29-34ac-87ea-397d75884317 | -2.86542 | -51.65775 | 2024-12-24 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2857d3d1-756a-3b35-b0ca-d5c3a46fed5b | -1.94308 | -44.7781 | 2024-12-24 04:36:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1f71f32-e627-39da-8926-180ed19e27e9 | -3.03233 | -53.89179 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78d4e7a1-680d-3dad-81d7-3c504014c48d | -6.69168 | -39.12116 | 2024-12-24 04:36:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 45f43768-8f44-31d5-a91f-8a47fcfd3fc7 | -2.60818 | -45.91221 | 2024-12-24 04:36:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a7ce22f-b9f2-35bd-936f-4cede5715117 | -2.34375 | -45.58998 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf4e66a9-d0ad-30d0-b1bf-77b404824e79 | -2.76819 | -52.6461 | 2024-12-24 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9fc1a6b7-a193-39f8-921e-e8aaa6efbff8 | -3.84644 | -52.28437 | 2024-12-24 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f8a3540-c609-336b-9e71-6efb9f327319 | -1.58362 | -53.39301 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8707161-7648-3d66-9e13-19e1f99b9b7e | -0.93078 | -46.89181 | 2024-12-24 04:36:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b76e213-2a88-371d-9d00-ae5f42bf6241 | -2.64647 | -46.11189 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c3e709d-fd37-3f6d-a9b5-94ca41b0a206 | -6.91293 | -43.53301 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dec29a7a-c424-3e19-b286-3243526be575 | -3.74784 | -52.03884 | 2024-12-24 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2f355a3d-6c48-3128-8675-ba516f875a5f | -0.93469 | -46.88878 | 2024-12-24 04:36:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10477fcb-87a8-3b48-a4ec-50c410523a07 | -3.18373 | -45.98002 | 2024-12-24 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd15596a-ec94-3cc3-bc05-9ba1234e4ae6 | -1.57981 | -53.33754 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a68aa3b-ca18-32d6-84d3-dbca0ae2cd42 | -2.92162 | -51.58263 | 2024-12-24 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4093c575-fc23-310d-8f1b-82d72eebdb61 | -2.70976 | -51.66584 | 2024-12-24 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8185d1f-95c1-3dd3-a341-2a6220ed084f | -1.6245 | -46.11303 | 2024-12-24 04:36:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 072fe866-dbae-3571-a664-72b38c99a9d5 | -6.91585 | -43.53271 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb1a017b-ab03-37e5-958f-22b9c7400e04 | -2.96515 | -40.29602 | 2024-12-24 04:36:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7abc9aea-ac25-3312-9a99-ce949f079e5d | -2.34731 | -45.59052 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 7da87c57-d43c-30af-bfe1-abd7bb80b3a6 | -2.34856 | -45.58249 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 78bc48bc-46fa-366c-a320-805da5cb8b7c | -2.35569 | -45.58356 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e0be8e7-3bd4-3f7e-ae2e-d047134cd37e | -2.09078 | -45.35964 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7f51e48b-150c-3c79-8aac-abcb13681d5d | -2.75903 | -45.71086 | 2024-12-24 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 765aa6c3-b9c3-32ea-9098-418c32ea6de9 | -0.96098 | -46.78733 | 2024-12-24 04:36:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c834fe74-84bb-3252-8b1b-5e28b625acdd | -4.51212 | -42.06433 | 2024-12-24 04:36:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 62d6d7aa-5562-3872-b8bb-96dee35589a2 | -3.15462 | -52.14116 | 2024-12-24 04:36:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b44fe385-a847-392a-90b9-1c2d27b54f4f | -5.98764 | -45.39238 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8582b4ff-76fb-39c2-8213-d9b2c0608893 | -5.96828 | -44.29446 | 2024-12-24 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8438b0c7-2bac-3f32-9a78-a403f4263b4a | -2.5824 | -51.92619 | 2024-12-24 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f8d912b-226e-3938-a0bf-3cf080ed61ae | -6.20739 | -42.64479 | 2024-12-24 04:36:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README9.md)
