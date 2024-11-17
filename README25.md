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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2ac1351-d8dd-3879-b11a-eb7bf94ca3be | -11.12686 | -44.56882 | 2024-11-17 03:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b661e8f4-3f61-3725-9ee8-582bce212255 | -12.44084 | -43.79734 | 2024-11-17 03:46:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cfb75dbd-44f2-304d-8e55-11f6fb484ca5 | -11.8532 | -46.93941 | 2024-11-17 03:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5efade1-4208-34c9-a7da-17a63055c22e | -14.1958 | -43.25934 | 2024-11-17 03:46:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4efdced2-f957-3532-b5b6-54d9604d6d28 | -10.54046 | -44.67384 | 2024-11-17 03:46:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64102163-9527-3398-971a-57f8798db8d3 | -15.89362 | -43.45782 | 2024-11-17 03:46:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8785d96-49eb-3f20-b97a-edf4a4675a08 | -10.54545 | -44.67476 | 2024-11-17 03:46:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20fa9410-88bd-3bd9-b02e-f056f8748b5a | -10.66603 | -44.49426 | 2024-11-17 03:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 419a233e-66e7-30c0-99f6-a6c386c34bda | -10.69323 | -44.91083 | 2024-11-17 03:46:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e845412c-5e80-320c-ad2c-dd822e4be781 | -12.96703 | -40.63186 | 2024-11-17 03:46:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5180c598-4482-35d9-b88c-1182010a3707 | -10.66501 | -44.49983 | 2024-11-17 03:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31bc8207-4372-3863-8635-24b421f183bc | -10.6601 | -44.49892 | 2024-11-17 03:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1eaf73b-b0e2-3488-83a4-4f8b4c95bd1b | -12.27564 | -44.98919 | 2024-11-17 03:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de3b22d8-6ca5-3550-ad0b-d5f9ee540745 | -12.26704 | -44.98066 | 2024-11-17 03:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 350b9d29-cdf1-30a8-a0fa-161792a0a695 | -11.18534 | -44.62152 | 2024-11-17 03:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0beaa56-d4ea-3de1-9bcb-8f62e585eecb | -14.19507 | -43.25809 | 2024-11-17 03:46:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 908d51c9-1212-3795-a342-802924b3ab02 | -15.89289 | -43.46185 | 2024-11-17 03:46:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3547b28f-db14-374d-96bd-ad6a045a87be | -11.85041 | -46.9393 | 2024-11-17 03:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54ae905f-c8ff-3883-9b6e-c0cb59b2380d | -12.17771 | -38.81342 | 2024-11-17 03:46:00 | NOAA-21 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ae628b67-1fb5-3cb0-b4cf-43d2b1046b1a | -11.85607 | -46.9403 | 2024-11-17 03:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f1d3360-579f-313f-bdb1-8018454af94f | -9.8653 | -47.52593 | 2024-11-17 03:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c109325-ca25-3f7c-880d-e973279ebec7 | -11.16277 | -45.10513 | 2024-11-17 03:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cbcb273-ec71-3f5c-b526-f005e0d0d33a | -15.89434 | -43.45821 | 2024-11-17 03:46:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40e7199e-2900-3bef-9798-70fcb41188c4 | -13.01051 | -40.02676 | 2024-11-17 03:46:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3923052d-9896-3eeb-86a4-aebe938f7fed | -10.38415 | -44.8798 | 2024-11-17 03:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5cb8a09-a2a1-3236-9bc1-80f8fdef18dd | -15.89359 | -43.46222 | 2024-11-17 03:46:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b30971-fd6e-3109-b7b8-6ea246415aba | -10.81906 | -44.92927 | 2024-11-17 03:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dba8450-3cad-35a0-9e79-5ef81724ebef | -12.26969 | -44.99362 | 2024-11-17 03:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f093ace-0ad2-3740-8d0e-5742d1eb7885 | -22.41796 | -54.17632 | 2024-11-17 03:49:00 | NOAA-21 | GLÓRIA DE DOURADOS | MATO GROSSO DO SUL | Brasil | 5004007 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 19279b37-49b4-3a8e-94be-cce008f19252 | -2.6137 | -48.5639 | 2024-11-17 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| e5455b26-0cbd-350b-a0f5-5c517208a4e3 | 0.6159 | -51.7676 | 2024-11-17 03:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1164cf32-715c-31af-992d-39288238b3f5 | -3.5308 | -50.2757 | 2024-11-17 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3bc72512-c300-3447-9419-c0d331f8caff | -3.5494 | -50.254 | 2024-11-17 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3dcece32-a83c-379e-8ae2-ef864f00fba2 | -2.5802 | -47.571 | 2024-11-17 03:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| cb83d395-aa9c-3c19-8444-fdc5bb5b9c69 | -4.5616 | -47.9925 | 2024-11-17 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c08977ed-caf3-3955-bfb6-fdcf14437487 | -3.531 | -50.2337 | 2024-11-17 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 91115106-d42a-3f9b-b83d-6f8b7bd2dd4a | -3.5124 | -50.2553 | 2024-11-17 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| a6f5fe80-539b-38bd-b7db-c7176e17f75e | -2.6322 | -48.5634 | 2024-11-17 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a51afd74-69a4-3e22-9b36-116ac0f2821f | -4.5614 | -48.0141 | 2024-11-17 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 80a1656f-34fc-3bf2-bac5-1c506ab27797 | -8.4336 | -44.2019 | 2024-11-17 03:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 90af2940-6161-3d64-ad09-719e9e206522 | -17.6063 | -57.5715 | 2024-11-17 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 9dddac07-8f6f-3c9e-99c8-3ba95087eb42 | -17.6059 | -57.5921 | 2024-11-17 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 9a33e0fe-35b1-3a9b-a8cd-a4c0aeba34c7 | -3.5078 | -43.7761 | 2024-11-17 03:50:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| fa6a3947-99c3-346a-a201-77ce76f4aa0e | -17.5862 | -57.5944 | 2024-11-17 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 4c0f8ad6-3b5e-3dab-97b3-4f83808c9480 | -3.5309 | -50.2547 | 2024-11-17 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 186.9 |
| d208d5aa-09b1-3239-8aff-7fa45ba8eba8 | -28.57929 | -50.14503 | 2024-11-17 03:51:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e65acffb-dc83-3452-8e30-4a238e67da19 | -28.95985 | -49.41597 | 2024-11-17 03:51:00 | NOAA-21 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| cb2780c5-319c-3705-9128-ed74197529c1 | -28.95772 | -49.40332 | 2024-11-17 03:51:00 | NOAA-21 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f65e1d80-cea0-369c-9c5f-3844be6f685d | -27.05508 | -52.62356 | 2024-11-17 03:51:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4220e3d8-538b-31da-ac1e-9fd66771d745 | -27.05932 | -52.62214 | 2024-11-17 03:51:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 11a25072-1894-3e48-bd7a-b3cddd7a0350 | -27.06086 | -52.62547 | 2024-11-17 03:51:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 735aaa10-2a1e-35f8-b041-7edc09dcea74 | -27.06202 | -52.62075 | 2024-11-17 03:51:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| deab05fc-0c98-3d5f-a9c9-3ba7fbdc0ae2 | -28.96112 | -49.41029 | 2024-11-17 03:51:00 | NOAA-21 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 052261c9-fc8c-30ae-aa3c-c0760cb124a0 | -3.531 | -50.2337 | 2024-11-17 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| be026bfa-eeac-3f90-9239-27136b1329e1 | -2.8615 | -46.7086 | 2024-11-17 04:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 558e89fd-3685-36d6-8e0f-6b918124d90b | -2.8614 | -46.7306 | 2024-11-17 04:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5d7d0c66-702d-322a-86de-6ae27ad339da | -4.5614 | -48.0141 | 2024-11-17 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| f4a0470a-4228-369f-938c-1339b960f406 | 0.6159 | -51.7676 | 2024-11-17 04:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 3ab756c5-5eab-3267-acb8-44d08b606491 | -2.6321 | -48.5849 | 2024-11-17 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 4a737cb2-486e-37b1-8be5-36df204aa212 | -17.5865 | -57.5739 | 2024-11-17 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 68507352-3dce-3329-9048-04a1de4bb59a | -2.6322 | -48.5634 | 2024-11-17 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f40203c4-ee19-3b41-8c33-5fc6865be810 | -3.5494 | -50.254 | 2024-11-17 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 1be18a1b-753f-3beb-b721-987db485bf26 | -3.5309 | -50.2547 | 2024-11-17 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 240.9 |
| 57c7a6ee-ddcd-35ce-839a-602930664a07 | -4.5616 | -47.9925 | 2024-11-17 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 98601ec5-0673-39ab-929d-a82287828981 | -17.6063 | -57.5715 | 2024-11-17 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 4d050887-0380-3110-9791-f2eb03f5f218 | -17.6059 | -57.5921 | 2024-11-17 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.6 |
| b974c3b5-fcc9-38c4-a6dc-5e9630e857b8 | -17.5862 | -57.5944 | 2024-11-17 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| c829ee3c-b56b-3df9-8ce4-806b44c5602e | -3.5124 | -50.2553 | 2024-11-17 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ec91c40a-3452-3fca-ad5c-4326efee948a | -3.5308 | -50.2757 | 2024-11-17 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9caac957-48cc-3154-a69a-f83539d7af77 | -1.51917 | -47.46871 | 2024-11-17 04:04:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb79a258-000f-3a61-9c1c-d2a91a563b11 | -0.32037 | -48.70034 | 2024-11-17 04:04:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9102c773-5d8a-307d-a620-cbe86d1198da | -0.40559 | -51.62941 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1c0e1ec-d3ab-318c-881c-45b5af9c1de6 | -1.70663 | -46.23568 | 2024-11-17 04:04:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff8e4c63-4bba-3775-8e47-adac4d950dc5 | -0.10691 | -51.60865 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8962142-5f66-39bf-aa33-a13a0d50f508 | 0.61436 | -51.77805 | 2024-11-17 04:04:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7fae6310-dbbf-3ea3-bccc-f55568ddbe30 | -1.2288 | -47.35983 | 2024-11-17 04:04:00 | NPP-375D | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 82aa89eb-2947-3f5f-a4c3-ca4ea97a697d | 0.62003 | -51.77206 | 2024-11-17 04:04:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2113726-f57d-3196-8f9c-55837de7cfc9 | -0.04836 | -53.25612 | 2024-11-17 04:04:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7994875c-73e2-34a1-a775-f3f24cee1c8a | -0.32704 | -48.69179 | 2024-11-17 04:04:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7a9d4ae-0460-3b90-81c9-a84a80b9d570 | -0.04237 | -53.2585 | 2024-11-17 04:04:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86b4d895-1a4d-3738-b40f-70dfbd5aa5c3 | -0.32134 | -48.69408 | 2024-11-17 04:04:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44579fec-047f-386d-8f03-54600592aef0 | -0.40309 | -51.62793 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 542bbe9b-f699-3622-b44d-b866ab5cb19b | -1.07464 | -48.18866 | 2024-11-17 04:04:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e481128-a03b-3bee-97ec-b0e6e74a2628 | -1.4961 | -47.39311 | 2024-11-17 04:04:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c8aa293-a105-3fdf-8b81-4b3a6c94cd8a | -1.22958 | -47.35498 | 2024-11-17 04:04:00 | NPP-375D | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fe3112ee-0a44-3c32-87fc-bf5a67f203e2 | -0.31299 | -51.50671 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43f384fe-b15b-3c07-9b0e-297badc0871b | -0.4064 | -51.62447 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33e752ca-5c03-3396-bbc9-582e02ff18ec | -0.30999 | -51.50161 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12671c9c-4e0a-307d-8ecb-b0825cad6ea2 | -1.07341 | -48.19294 | 2024-11-17 04:04:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 646687b4-de0d-34e9-8a72-a87f8bf896c1 | -1.49767 | -47.39485 | 2024-11-17 04:04:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f2abc26-a227-33d4-8dab-983d8e7cc021 | -1.37203 | -47.25544 | 2024-11-17 04:04:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f100640d-b3db-31c5-88ff-57eb55bcba81 | -0.83878 | -47.47372 | 2024-11-17 04:04:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2c29835-41e2-34ce-a03e-44a5ca6f0dd2 | -0.12044 | -51.62317 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2e758e5-4dbd-3412-84e5-1d6e9bf1a99d | -1.49534 | -47.39795 | 2024-11-17 04:04:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16875ca0-7ffd-3b84-b5e1-b0ceb4a033d7 | -0.31516 | -48.6995 | 2024-11-17 04:04:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26f29121-56cc-3bf4-a59a-c20172778992 | -0.10845 | -51.59866 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55267460-0dcb-375c-8532-9cf475cc9fef | -1.49687 | -47.39967 | 2024-11-17 04:04:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62d9459d-242f-39d6-9ca4-2834212ed935 | -0.12679 | -51.62404 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df2946cc-cfed-3a04-b44a-640f48214058 | 0.61357 | -51.77298 | 2024-11-17 04:04:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 9ec9ed05-dce8-35d6-9a98-45bca77b45a5 | -0.05044 | -53.2526 | 2024-11-17 04:04:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README26.md)
