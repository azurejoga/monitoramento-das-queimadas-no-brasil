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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a9fc435-27ed-322d-b36c-886fe0cb8281 | -3.02346 | -45.37423 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d0c58a81-6934-3455-b44d-91744e7bf40a | -6.69058 | -42.04771 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5b642345-f70e-3870-9381-a0bf7c6c9e15 | -5.30378 | -48.69956 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e88ab16-2e00-3957-a073-e095222fe6c4 | -3.57619 | -43.62715 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ae52772-8c0a-333e-aded-6a8768de1c57 | -3.17308 | -45.65073 | 2025-10-28 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9effaa55-433a-31b3-9d5e-c982fa899b70 | -4.20184 | -48.35977 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c444285-35fa-31f9-a00c-58fc39bed127 | -3.4812 | -55.45516 | 2025-10-28 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10aa3f5a-ad9f-3617-abb9-1f2c3541d3a3 | -3.11927 | -51.21038 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcd62ca6-597f-3dfc-888b-b9f5286b5211 | -5.62857 | -47.61499 | 2025-10-28 05:01:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b25891b-d0e5-3a2f-a73f-117553d00daa | -6.69769 | -42.0486 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 06755a64-5158-3f69-ab99-b126e207f356 | -3.65262 | -49.9244 | 2025-10-28 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 320ed322-d2c8-3bfe-97e4-29071e016549 | -3.57476 | -43.6368 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cbe661d4-6d55-3339-9370-370cc029a194 | -1.32387 | -52.80421 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a26427d9-9659-381a-86c5-0cdbf892b317 | -3.7533 | -54.65564 | 2025-10-28 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca7f5cbd-0a66-391a-af43-427f0478c828 | -5.78868 | -47.71961 | 2025-10-28 05:01:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f915f1f-d826-3d3d-b555-abd6b6d9bb1f | -4.90435 | -47.42231 | 2025-10-28 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19053447-705d-3b3b-a969-5e2196a6909c | -3.57013 | -49.0238 | 2025-10-28 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c30b1ee0-9256-3d6f-a661-dd5e1eeecbb5 | -3.97873 | -55.74607 | 2025-10-28 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 410e8adf-6987-3fed-ad31-6a4c149221fa | -6.13785 | -44.58938 | 2025-10-28 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b32d27cd-31fd-3328-8aa7-442de1742cad | -4.9264 | -48.6281 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16386707-e1b1-3c11-95d3-b5d85c7e278c | -3.73115 | -45.3505 | 2025-10-28 05:01:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e9bf07c-00c5-3162-9dae-8ae82b8deed4 | -2.94615 | -49.34986 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e93eb51-e02d-3394-8a62-196aadb1d0ff | -2.75316 | -45.40703 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f513e084-bdcd-32f1-8451-9afffaed9365 | -3.64857 | -49.92374 | 2025-10-28 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ef13534-36ae-36f7-8b59-80c0c62355c1 | -2.74718 | -45.40966 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1555944d-db11-32a0-8dc9-672560543271 | -6.42159 | -42.33538 | 2025-10-28 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e444ca2c-c7fc-3896-a72b-04ebf6a0b28e | -3.57689 | -43.62239 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8acf8f10-0648-3930-b713-6f83d08da62f | -1.6931 | -55.67278 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f2e680-73d4-3777-b0b4-b56ad30ef06a | -5.2404 | -49.49824 | 2025-10-28 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b9ff5a6-d27c-3223-91f4-404d14bc493f | -1.54961 | -55.42097 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0fa3905-d6df-3b8e-b4bf-c0ad9cbd5996 | -3.48451 | -55.45568 | 2025-10-28 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffbc7b63-7fe3-3194-92f7-443db73bf6b6 | -2.99361 | -51.03915 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6687892b-5493-3575-a6a5-4d8c0f8a7ada | -3.10579 | -50.18038 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 123adee6-3325-39ad-a927-26f8630e6aa9 | 1.6196 | -55.70311 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11a20bb5-f157-3189-8f92-045267ea5a58 | -3.37187 | -50.17543 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b289612-2181-399f-9b86-c21abbdfdc2e | 1.65587 | -55.66745 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0a080a9-5791-3be5-b3c3-53912bec010c | -1.80645 | -55.68631 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52420d0b-edf6-3867-b1f2-7e3871f7c182 | -4.29307 | -44.511 | 2025-10-28 05:01:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52851e67-c1de-35f4-93f7-c272f4dfbd04 | -2.64365 | -48.50962 | 2025-10-28 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c4817be-6de1-35e1-84ce-744e4940c252 | -0.90536 | -47.55104 | 2025-10-28 05:01:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 62c347ea-44fd-382f-8a47-1376da58d5fc | -3.62282 | -51.49535 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 171dec74-c85e-3bbe-addf-6d339dd2cf98 | -5.84046 | -47.56435 | 2025-10-28 05:01:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2f4dfa22-4d91-386d-8afe-fc336ad4bd65 | -4.35991 | -50.66137 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 411abd3f-521a-3c4b-9994-5f37a2a93985 | -6.16304 | -46.09723 | 2025-10-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19d0210f-ed2a-3594-a80f-f9550fe38916 | -3.69089 | -60.55909 | 2025-10-28 05:01:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 796f7047-cb97-35b5-a010-e080062decf8 | -3.57904 | -43.60786 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1db340ac-7afb-3b02-bdac-dc6c14b3a33d | -3.53275 | -53.31486 | 2025-10-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e8d379c-6968-36c5-b4a1-788bf33d93e3 | -1.17731 | -54.20588 | 2025-10-28 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a1aed1a-52c9-3344-823e-0bb04ce93cdc | -5.65905 | -46.4575 | 2025-10-28 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae62df5d-94b2-3cee-beff-f5671d49510e | -5.29925 | -48.69891 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deaa451d-0c74-3953-b63d-ed77e098958c | -3.7103 | -51.82431 | 2025-10-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00f9c42e-e6be-3485-84a7-92d7e353e649 | -4.75206 | -46.42661 | 2025-10-28 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea2d26e5-ed07-38b6-82a7-1a6148f55058 | -2.75966 | -45.40088 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2f9a1dd6-2596-34cc-a32f-7f999bf21cf4 | -3.75384 | -54.65221 | 2025-10-28 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e5ca2b6-155f-3fdf-b539-45156222726b | -4.45608 | -43.65004 | 2025-10-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| bfe2b56e-49f2-3d31-8c45-385f7b52af62 | -6.42246 | -42.32863 | 2025-10-28 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad325aae-512f-3eba-a083-1534fe77e0ab | 1.60767 | -55.71991 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d1fdb58-5c64-332a-96b0-4ca536daf877 | -2.75263 | -45.41055 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 466c197f-beed-3e36-972f-a722aef4d49b | -6.70081 | -42.04728 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 33263abc-6a86-34f8-8c91-e8e22f26e017 | -3.28551 | -52.60955 | 2025-10-28 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b422bc9-e34b-32a5-9927-b0c039889a93 | -3.15023 | -50.33633 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39454763-ff43-358b-bdb5-24f1affceb9e | 1.59521 | -55.7294 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7eed5092-7c08-3e09-a776-0361e54ef7c9 | -4.26947 | -48.69953 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4c61a5b-a318-35d9-8cd4-f81840b988d9 | -3.46725 | -49.96647 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71e9d835-68aa-370a-a13a-cb3588db3abf | -3.1267 | -49.10165 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fc65dce-8938-3210-828a-306f261bc3c9 | 1.61052 | -55.71203 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ae96aae-94de-3bde-8fe0-3e263d634578 | -3.98334 | -48.98837 | 2025-10-28 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be2b03fc-cb9b-3b16-ad7b-fc936d60512b | -3.2352 | -50.64857 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 773b8c3a-99a6-3d17-afcd-02a68177683f | -3.87603 | -47.99678 | 2025-10-28 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80274693-04aa-3782-aed2-2098226f5b2a | -5.61347 | -47.11217 | 2025-10-28 05:01:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c32df0a6-8cb6-35fc-84d4-39fc6c2aa6f6 | -6.68437 | -42.03984 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a583cc0e-65cd-3769-bc24-89dd696621f6 | -5.47135 | -50.16213 | 2025-10-28 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddb4bf56-5e5f-3554-a065-3e18a24a0c37 | -4.29244 | -44.51533 | 2025-10-28 05:01:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4cedf4f-c7e5-3e10-b082-9346d7c489d0 | -3.41812 | -50.36871 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7e32a4c-b407-311f-b735-836350a66673 | -3.04625 | -53.02032 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07143071-4f4c-37c2-a49d-68cfaa898639 | -1.49672 | -53.13008 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82f1fd67-3529-35b0-a82a-b7737195a73b | -1.58537 | -53.16916 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca3d0598-3a7a-3faf-94c1-db6b81dfd43e | 0.23425 | -51.15451 | 2025-10-28 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49a287f1-fb0b-35ac-b71b-e1d277258789 | -3.53456 | -52.85276 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c875ebd9-cce5-31bd-bd7c-aeac32914bb9 | 1.61676 | -55.7073 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd360823-1131-3bd3-9431-f0f06f3c5cfc | -3.11288 | -51.21585 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29e58905-a428-3288-a445-ce8121e7fec1 | -3.27345 | -52.57245 | 2025-10-28 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a02afa7a-4da3-3779-8c6d-bdf45e7c395d | -5.4841 | -47.74558 | 2025-10-28 05:01:00 | NOAA-20 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b6cdd03-47a3-3daf-8a47-9d7f9fdebaee | -6.6937 | -42.04642 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bf247cf6-81ce-3846-b8ea-7d5c82e3de01 | -4.7386 | -48.30666 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bde7fe6a-65fe-34d4-b772-939798674767 | -4.4602 | -43.6475 | 2025-10-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 52e1c481-2a41-31ad-bbdb-e04e64b5bd9e | -4.9272 | -48.55832 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 443a1c2c-1da6-32a6-b460-1c0d8156ab1e | -3.89613 | -52.09963 | 2025-10-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9831974d-0b62-3d0a-821b-62152b619bd7 | -2.43712 | -49.76012 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 281e5343-6dd3-35da-8a89-8d1685b292cb | -2.76019 | -45.39737 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0df2cf08-5cc7-31fc-946a-d16bf4eaad35 | -2.64431 | -48.50535 | 2025-10-28 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58411c53-9d05-3deb-ac77-774590ef732f | -4.03147 | -50.44785 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26b787b6-40eb-3218-9ac5-2ee159994494 | -1.50402 | -53.12751 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7041a982-879a-389c-9a35-9eb832bf2872 | -1.83885 | -45.29364 | 2025-10-28 05:01:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0825d705-1c3b-3487-b8b4-74bbfa0823d3 | -4.44311 | -45.98139 | 2025-10-28 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69893fca-fa04-3946-ae8e-f560ac10554d | -4.20118 | -48.36427 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7208ca27-0131-392f-a86d-0fcb10f56c79 | -4.97504 | -47.81206 | 2025-10-28 05:01:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c27af056-f1a1-3ca9-8e19-ee8c1e31b354 | -2.38104 | -57.08087 | 2025-10-28 05:01:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36a40864-b0d3-3c3c-a0cf-f06ae9634fd3 | 1.09852 | -51.3119 | 2025-10-28 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d41c1a50-8585-3b71-9271-a6c484c902b6 | -3.40036 | -50.27335 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README73.md)
