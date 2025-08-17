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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93c199c4-0b32-38ea-ab4d-16c0d648bd82 | -13.5918 | -47.76618 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1201298-73bb-319b-b943-33da0185a530 | -14.94219 | -47.06142 | 2025-08-17 04:17:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c88f6c93-ce44-357d-b65c-de986b999b4e | -16.63077 | -51.3679 | 2025-08-17 04:17:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad9574b8-89d7-32a9-9a54-995e2bbdd035 | -16.48791 | -45.11285 | 2025-08-17 04:17:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5670bf30-cefd-3ac6-9c28-dc09b02951f3 | -15.85854 | -50.19324 | 2025-08-17 04:17:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 218e5233-4233-38d0-b216-cb2d588d61f2 | -18.20483 | -45.24395 | 2025-08-17 04:17:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec0540c4-87a3-30b1-b21a-d553361085e9 | -14.55036 | -52.03287 | 2025-08-17 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d93e334-49a0-3ed5-9fc0-7ba52ddcc31b | -15.17771 | -48.76536 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 568e962b-ad32-3970-8a69-270e78fd6854 | -13.58824 | -47.78726 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45355cbd-f5c0-3b3c-bdd8-752ff4f4ec02 | -13.42598 | -57.03593 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd61863e-8b09-3ade-9ed0-803a6e487274 | -13.87633 | -45.54342 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c44ae6f6-46d6-310d-95d9-1c89b6f198a4 | -13.60598 | -47.74713 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98e0a8cb-85e4-3b3c-bb81-dae1541f5869 | -13.63927 | -49.45509 | 2025-08-17 04:17:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ec12c55-c592-3440-b1ee-59f85e0e11e4 | -14.63082 | -54.89343 | 2025-08-17 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 321a017f-057c-36f2-81df-9b46f46323a0 | -18.93739 | -48.17668 | 2025-08-17 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db3647d0-1606-3e5c-9b1e-13172ce8db49 | -19.98507 | -45.51687 | 2025-08-17 04:17:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c7b7006-dd5e-3d06-aba6-2721babee7e0 | -13.57813 | -46.98745 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab51cbc1-5135-3223-85be-64ecd8c74e9e | -15.52421 | -42.3369 | 2025-08-17 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3041bfb4-d946-3fa0-8b3e-8f0cdf1abd28 | -15.17847 | -48.76093 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb52cc79-7895-33e7-a693-663f113d267e | -18.96177 | -43.74693 | 2025-08-17 04:17:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 417af7a4-96f2-3a45-8f84-d598cd82e351 | -20.01301 | -47.70975 | 2025-08-17 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6aa4aa82-6c95-3316-8b57-54f7e9c2e9ec | -17.01774 | -49.45498 | 2025-08-17 04:17:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ec1fd4f-0c5a-3b3e-9398-553c6a9a02e8 | -15.18274 | -48.78004 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 461c620c-d79f-3e2f-a5d5-e5d893455abd | -24.16301 | -52.90034 | 2025-08-17 04:17:00 | NOAA-20 | RANCHO ALEGRE D'OESTE | PARANÁ | Brasil | 4121356 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 579ae2e3-7657-3dbf-a662-1b0b4b3a0dd0 | -13.60178 | -47.77209 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c80cc071-41c0-3f82-a7b7-fc48cdbaab24 | -13.00586 | -56.86806 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a3fbba21-d236-30e0-9a4a-62b601e05cfa | -16.63002 | -51.37191 | 2025-08-17 04:17:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9ffbe71-cbb7-354b-8fb0-ea8849a41b17 | -15.76946 | -47.80437 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c2648a6-9b84-3334-8e10-0f505c335e18 | -13.58897 | -47.78294 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5861bee-6fc0-31fa-a952-a363232bb8c4 | -14.18793 | -45.33537 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 888a12a5-b277-3a76-b6a1-b4f588387079 | -14.95171 | -54.7529 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03009a51-2610-32a4-93da-e3afe3379b51 | -14.03712 | -46.3758 | 2025-08-17 04:17:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0a863e9-f2a4-38ba-aa50-0f6a22e31ad8 | -16.83903 | -48.90924 | 2025-08-17 04:17:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ec1fbb7-dff5-34a1-974f-788423039470 | -14.9739 | -54.75328 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4c5db7fa-cb0a-36e1-a01f-a14fc8245520 | -14.59061 | -47.95485 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b76ff2c7-c1b7-3367-8c7f-6c0dbd63437a | -19.91629 | -49.11599 | 2025-08-17 04:17:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6966c084-8563-3fd0-afe7-27d522e28fd5 | -16.83827 | -48.9136 | 2025-08-17 04:17:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1305de9f-916e-35f4-a50d-2825a9e844c7 | -15.62192 | -47.63239 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 387b2a5e-8f71-38b0-be43-29bc2d1fa47a | -19.98748 | -45.51676 | 2025-08-17 04:17:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93089b56-201d-3530-827f-06cea52900f9 | -15.96893 | -43.89699 | 2025-08-17 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a6591e20-d493-3cfb-898a-95fb7e9ad127 | -14.97211 | -54.74765 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fa02880c-b15e-36da-94c8-1754ff14184d | -13.65598 | -53.70793 | 2025-08-17 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3bd7cb8-411d-3a89-88dc-dd79024aa74f | -15.244 | -43.85195 | 2025-08-17 04:17:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9408f410-25cf-3e53-b079-4ec1d23ea528 | -17.83596 | -40.12767 | 2025-08-17 04:17:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cda4882a-c1e3-3ac0-8ecb-25c28b9dd61f | -18.64859 | -52.13281 | 2025-08-17 04:17:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c650e749-539a-399a-b42a-67cfe51aad62 | -22.28528 | -55.95811 | 2025-08-17 04:17:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 364c8f70-eb5a-3cde-9b58-1d8a77de0277 | -22.28109 | -55.95317 | 2025-08-17 04:17:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4a0255c-898c-3efd-9a89-50a0a7e83459 | -20.29031 | -42.21155 | 2025-08-17 04:17:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| af15b16a-1b26-33da-83f0-219aed853bf6 | -20.50503 | -47.42674 | 2025-08-17 04:17:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdcce700-ba1d-322b-8bbf-1a6d4447e30f | -13.60379 | -46.89725 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| dfadf287-d865-300a-b702-68225044d8bd | -20.77904 | -49.56444 | 2025-08-17 04:17:00 | NOAA-20 | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8e5efd18-7909-3d9f-8b73-f5c99fee8c6e | -19.6101 | -47.03498 | 2025-08-17 04:17:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96831718-d59d-3cc7-8372-246c2e0f08ae | -14.95554 | -54.76137 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e18332f7-3b21-3b02-8916-826cddfbd044 | -20.20672 | -49.1385 | 2025-08-17 04:17:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23d8f5c7-d1a0-3444-9143-0bf4de96a327 | -13.60724 | -46.89772 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0743f9be-dcd3-3b97-bd3c-6dc219b3c83a | -15.17984 | -48.77491 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e05488d0-2287-3197-9c9c-0335ca498e70 | -14.95376 | -54.75616 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50556bfc-04dc-35e6-a66b-000bf8bb34e8 | -25.17738 | -50.08028 | 2025-08-17 04:17:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e11ecbf6-7069-31b0-8333-a8345a07493f | -18.27046 | -45.15007 | 2025-08-17 04:17:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5a8b386-c7ad-39f3-89a2-0f44108cab01 | -18.93672 | -48.1806 | 2025-08-17 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b98d27a3-bc18-39c8-b8df-ad8fa33ef4fd | -13.60817 | -47.77759 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a902e038-0c36-3db3-957a-c0de1d79010e | -13.42987 | -57.02932 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad2bba80-1d2d-3a60-b723-1c80c5d9666d | -24.159 | -52.89945 | 2025-08-17 04:17:00 | NOAA-20 | RANCHO ALEGRE D'OESTE | PARANÁ | Brasil | 4121356 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ddd742ff-f1bc-35b5-b237-a349b4b49826 | -18.88715 | -44.77538 | 2025-08-17 04:17:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 592a1d30-9ac3-3afa-a040-e5f14e585272 | -15.64026 | -48.11862 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48fbabab-ad7e-3005-acf1-4094bbd1a8b1 | -14.18688 | -45.32061 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f8ef158-36c0-39dd-8d84-fa3ba2646b91 | -17.8987 | -44.42255 | 2025-08-17 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c741003c-e822-3242-9f9a-3d587363717d | -22.21153 | -56.20132 | 2025-08-17 04:17:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03dc9098-882c-387a-8c23-601ca96dbb64 | -13.61235 | -47.75275 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 232ffb81-b988-3305-8168-52cfc80f9768 | -15.14063 | -48.73986 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74ac27b7-3325-324a-9478-f74410aa1f74 | -13.62941 | -46.91304 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bde96582-cfa1-3f0e-93ce-f4cb80fae055 | -13.65847 | -53.70686 | 2025-08-17 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b15d9f6-6f2b-3334-8b2f-4243b01367b3 | -21.00555 | -46.61432 | 2025-08-17 04:17:00 | NOAA-20 | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9e07615c-8db8-3c12-9120-f02c88ea9748 | -15.76599 | -47.80373 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f7a9e8c-26a6-33a9-a057-a2ed9c5f79ec | -13.59039 | -47.77452 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ccd68a98-3e6e-3213-9c03-8ce2be4ec7d5 | -14.6043 | -47.95592 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98397377-e220-3672-b584-5e4c9527d885 | -15.64731 | -48.11989 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed447ad8-c51b-3a0e-a584-1163ef4d490a | -16.62587 | -51.37103 | 2025-08-17 04:17:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19759aeb-5bff-3120-a6eb-0e04adf4899a | -14.93195 | -47.05961 | 2025-08-17 04:17:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6f3b7c0-024e-30c0-bef9-99008017a837 | -15.18639 | -48.78076 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7d1d6860-868a-350a-be72-fb9149935429 | -18.20816 | -45.24451 | 2025-08-17 04:17:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5b3023f-a191-3adc-ac40-94c380b88142 | -13.61069 | -46.89819 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f8d03fa-6b79-308c-ae7c-423d40dc6ef9 | -19.62742 | -45.27787 | 2025-08-17 04:17:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6388a058-547d-3482-96c0-a77c49a38192 | -22.16955 | -56.11231 | 2025-08-17 04:17:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 724277ac-73f9-3070-97a4-55f3c04c531a | -12.99849 | -56.87183 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| da0ae8ae-af59-310f-860f-678f6a6febe4 | -14.936 | -47.0564 | 2025-08-17 04:17:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa0dca1d-f2e5-33d0-8bcd-1ae659fe53be | -13.60034 | -46.8968 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 50a209e2-1bac-32bd-8e59-380052f553ef | -20.0001 | -44.44234 | 2025-08-17 04:17:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8bb24204-3311-387c-8228-af9052484b5a | -14.60003 | -47.95953 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9637821-b1f1-3567-be9b-57b8edf43852 | -19.50587 | -46.88037 | 2025-08-17 04:17:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a37045a-8fb6-33b3-8ebb-f5ea906e6783 | -14.18849 | -45.33182 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42f9af44-c814-324a-ae00-385dcd5451bb | -18.06445 | -46.3559 | 2025-08-17 04:17:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d0fac34-7dd2-3414-979b-76a0f6f42373 | -15.52064 | -42.33641 | 2025-08-17 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a752a660-e878-326f-87d8-f59496cce8dd | -17.21864 | -49.59529 | 2025-08-17 04:17:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef6bde0b-d87a-377f-bea4-63afe53e2bd6 | -15.18715 | -48.77632 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cebf8909-af62-3cb6-a970-2e3891d63927 | -14.18575 | -45.32771 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da8deb53-fad1-38d3-93c9-045e32493c04 | -13.59302 | -46.96188 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6d2256c-ae70-339b-9f6a-0c0d24b13ac4 | -15.64379 | -48.11924 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b8cb4a8-6134-3d26-8f07-36bd36d6578a | -16.71111 | -49.06015 | 2025-08-17 04:17:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f4f2247-e899-3f23-894d-95600b06928c | -13.59963 | -47.76315 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README23.md)
