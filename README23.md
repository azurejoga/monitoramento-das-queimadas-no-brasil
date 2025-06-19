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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d63e3beb-44a3-38e0-903f-8219e1e83473 | -17.70463 | -46.30144 | 2025-06-19 05:14:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3e935f8-5dac-3947-bcf7-09667d65a1ee | -16.31016 | -58.25378 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| da9418c0-84e9-3747-bc08-d7c1b69ce9d5 | -16.3227 | -53.79416 | 2025-06-19 05:14:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8dee36e-0c0e-3838-9afd-1eba9c6eaec0 | -13.98902 | -58.10895 | 2025-06-19 05:14:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8d5c9e1-116d-3bc2-adcc-565380cbc253 | -16.31071 | -58.25005 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a86afa01-be08-3ea3-a535-797eeb3aa71d | -18.65945 | -55.74986 | 2025-06-19 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e9c539cd-9f5c-36e6-a157-241f761a9408 | -20.20758 | -56.61404 | 2025-06-19 05:14:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 884694a4-796a-3824-8c30-dfa436598b69 | -20.47695 | -53.67708 | 2025-06-19 05:14:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c207a69c-87e0-311b-99e7-5ec78cb9f7f1 | -21.78662 | -52.76017 | 2025-06-19 05:14:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 339dfc80-8512-3516-a2a9-d2b2700758e4 | -15.51307 | -56.04041 | 2025-06-19 05:14:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93dc4947-8e71-3f29-888c-91c45d11c8c6 | -16.65025 | -49.36992 | 2025-06-19 05:14:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebbb3523-b57e-3dd6-8893-1e8870d5c52b | -13.72401 | -58.68519 | 2025-06-19 05:14:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00db2ac4-80aa-3b7e-8dee-38ccd2c5f4ff | -15.10534 | -54.66045 | 2025-06-19 05:14:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9558d5e-1141-379f-8a1b-cc5f7fe4912f | -18.66265 | -55.7555 | 2025-06-19 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| afe21410-ab7d-3fc7-b5ac-1e658fc4bf89 | -16.2995 | -58.25586 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| db35babd-530e-31e3-8a56-e3e804aa8a5b | -16.30569 | -58.26067 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 828f4051-7a29-33e1-9ec3-a9be725b5bda | -18.99638 | -52.08702 | 2025-06-19 05:14:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ffb7636-4cac-33f4-8166-28484d3403a0 | -14.90524 | -54.32767 | 2025-06-19 05:14:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 872ec193-247c-3b39-b5c3-e64dfe5ed44a | -18.30008 | -54.26047 | 2025-06-19 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 108c67a6-f1f8-3caa-9c46-08b0aca7cf87 | -16.64828 | -49.37023 | 2025-06-19 05:14:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5efd9eae-e0ff-3cd4-8d18-cb1e942568c3 | -16.30679 | -58.25322 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1e2c151a-5b94-3f3a-92ad-e2df7357b3d3 | -20.4542 | -50.01049 | 2025-06-19 05:14:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b103f80-61ca-3b7b-a485-5aaf2baf0c99 | -16.29894 | -58.2596 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 2218331f-cd96-3bb4-9c55-1e06936eb0c4 | -19.58742 | -53.50395 | 2025-06-19 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e437c02f-007c-3506-b096-0d5383084d5d | -15.51321 | -56.03881 | 2025-06-19 05:14:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6302d19-1866-3e02-94e2-c7010ad5df6c | -23.58688 | -54.42043 | 2025-06-19 05:16:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e2208f09-2fc6-322f-a88d-5d1ec962c0ff | -22.0849 | -54.42714 | 2025-06-19 05:16:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d873a04e-b20a-3045-98c4-ee1404d7f84c | -22.08458 | -54.42879 | 2025-06-19 05:16:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3899b186-d79b-35aa-904b-566018fd644c | -23.58922 | -54.41847 | 2025-06-19 05:16:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aff8c3bb-ff10-394e-b075-58eba703f8b0 | -24.24456 | -50.73998 | 2025-06-19 05:16:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 09d337e0-99a5-328a-ab20-3077b0b56ad2 | -23.58474 | -54.41775 | 2025-06-19 05:16:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41b0f0c8-09ea-37c8-955e-e3a4b145193f | -23.58742 | -54.4156 | 2025-06-19 05:16:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b1738d5f-3ea9-327c-aca8-6436300d296e | -11.952 | -58.7376 | 2025-06-19 05:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 136.2 |
| ac9152ff-721e-3349-8811-01e90f1fccbe | -8.0892 | -43.096 | 2025-06-19 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 3f834bee-4e90-3746-ab82-5d15c69e78d7 | -11.9518 | -58.7574 | 2025-06-19 05:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 8268e95c-1491-31db-a650-6606bba8ac14 | -11.9709 | -58.7362 | 2025-06-19 05:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 16fbf6af-5adb-36a6-b563-55b1f5b47e1c | -8.0703 | -43.0981 | 2025-06-19 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| d3204159-8518-3179-8f64-febf87984a10 | -8.0703 | -43.0981 | 2025-06-19 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 39b21004-b995-3a1d-a463-9e028df974a7 | -11.952 | -58.7376 | 2025-06-19 05:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 136.8 |
| b95d5254-74a6-3a3b-8abd-054708736579 | -8.07 | -43.1216 | 2025-06-19 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.3 |
| 910ff4b2-de17-3ba7-8882-c4d95d247b7b | -11.9518 | -58.7574 | 2025-06-19 05:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| c573a91e-5096-3755-8726-fceede3076dd | -11.9707 | -58.756 | 2025-06-19 05:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| a6766d95-dc44-3418-b93f-abf3fb078a5d | -11.13546 | -53.94378 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c931514-a790-32ee-b772-79fb708ee13a | -9.39653 | -65.51488 | 2025-06-19 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc2a7d5d-9517-3092-95c1-098e331739b5 | -11.9573 | -58.73021 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74f5fe6a-7899-3276-be4c-6cc4947880c6 | -10.09652 | -52.73591 | 2025-06-19 05:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8aa8320-34a4-3ab6-831d-8913228aae36 | -10.50948 | -53.58467 | 2025-06-19 05:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 25abcef0-1a4c-3c6d-ac27-239a0bdcf91d | -11.94443 | -58.7591 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36c03bee-8b79-3832-9f33-c864051c12d9 | -12.13256 | -54.66616 | 2025-06-19 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f1c0e98-81a4-3df0-8733-5a1d6c021d8a | -9.49881 | -56.08804 | 2025-06-19 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57f11fee-fb38-3169-8002-43d7b47218f3 | -11.95611 | -58.73891 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 47d2681f-e433-329c-a148-e5d2f0a780f0 | -9.3936 | -63.26711 | 2025-06-19 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62a22f35-f7b2-3095-b7b3-0b9fa454ea24 | -9.39416 | -63.26351 | 2025-06-19 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e7670d1-d552-36e2-8eb8-2b20317d2486 | -11.12948 | -53.94296 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 978dae3a-1317-3f5b-8306-a804a33dce9e | -11.76895 | -54.36954 | 2025-06-19 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc92201e-c6b1-3997-8ab8-14e7967d27b7 | -11.95816 | -58.75663 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 68606e90-b27e-39b9-87c4-66516d2111b3 | -10.85219 | -53.7848 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01e11bbd-69f3-3dfa-b65c-a9b481766a78 | -12.13206 | -54.67031 | 2025-06-19 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edae59b8-41c8-3d21-99f8-c07c8ab9bd1c | -12.02788 | -57.09912 | 2025-06-19 05:38:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8841beb3-3e3f-3ecc-aef4-a6500314e46e | -10.85326 | -53.77602 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd848c64-3869-3beb-a587-4a1099265fd8 | -10.09014 | -52.73515 | 2025-06-19 05:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3daf8547-cf95-3f47-8fe6-b64dc59d3e15 | -11.07518 | -55.05077 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a70fb484-25b0-393b-bd30-ac0b5f05d24d | -11.95991 | -58.74384 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0c2c5efc-951c-3d88-9f98-59bca457edf4 | -10.84828 | -53.76651 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdbca810-dc38-3b1e-bae6-67a2e8834d99 | -9.71521 | -64.53969 | 2025-06-19 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfc76717-04df-34f3-bad4-81cf777097ce | -7.92827 | -61.55579 | 2025-06-19 05:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c6214a7-291a-328f-befb-04d50d0f3a4e | -11.94677 | -58.7419 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57262c92-8185-3c4b-a350-d02fe71f1e87 | -9.46061 | -57.85267 | 2025-06-19 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3704a1b3-6162-3058-9823-5a04cd7b65c8 | -9.65558 | -65.75186 | 2025-06-19 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ec0fa6f-822b-3519-aaf7-c1300077387c | -11.61779 | -58.29224 | 2025-06-19 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0358e2db-55bb-38d2-b838-7d170b26c298 | -11.5275 | -56.99759 | 2025-06-19 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 390fadf9-5d3d-3de3-bd1b-6b97b9a86d88 | -12.02297 | -57.09835 | 2025-06-19 05:38:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc9f9689-93d3-3287-87cf-13ee4b46afb1 | -10.08491 | -60.4969 | 2025-06-19 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b872c7cd-8341-3f21-b45a-bd2b08668a7d | -10.86091 | -53.76342 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96150602-afcd-3792-a07b-c01e1fd4044f | -9.49295 | -56.0932 | 2025-06-19 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7648cd87-a3ee-350a-9077-4be372d4254b | -11.08195 | -55.05681 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f3e0b26-8942-3ca1-b205-cbe8283f05c0 | -9.49334 | -56.09026 | 2025-06-19 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 460ad47d-84b2-33d5-953a-60026006b5f3 | -9.48904 | -56.08365 | 2025-06-19 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 32d08d06-1ce9-3a5a-a724-3925edbf4c43 | -11.81673 | -54.50307 | 2025-06-19 05:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bee9b2ef-dc62-3fec-ae3c-dea219cccc22 | -11.9567 | -58.73455 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 97748f74-edea-32f1-a974-39cf12ef8b32 | -12.49769 | -55.7403 | 2025-06-19 05:38:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f380d2f-50ad-3f0a-9513-0fe08391c47f | -11.12698 | -53.93563 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8202ea59-de8c-398a-a6a8-9409823b4efd | -9.33307 | -65.64494 | 2025-06-19 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a745aae3-3cd6-3a9b-9e10-64162ab3dab0 | -10.50397 | -53.5794 | 2025-06-19 05:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 715b5cda-fd54-3bc0-93bd-1e2448179f39 | -11.13004 | -53.93857 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5ad563f-a8b9-304f-9946-da88719fb837 | -10.08954 | -52.7402 | 2025-06-19 05:38:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8ffcd2a-aa81-3d4f-be5d-b7a07331bdc8 | -11.07223 | -55.04433 | 2025-06-19 05:38:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb103e7d-9d73-3471-b334-b8a32d4df5ae | -11.14544 | -53.93388 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f560340-e8c2-3753-b709-c9578eed8558 | -11.6252 | -58.29137 | 2025-06-19 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8714a305-b644-379f-974a-f954615ccdf2 | -9.49412 | -56.08438 | 2025-06-19 05:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 73917bc0-e912-3ad2-9c56-4c00d53ebd1e | -10.50342 | -53.58384 | 2025-06-19 05:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d0b3bf8e-faae-3e0a-bf27-d4b3bdb36a89 | -11.96228 | -58.72647 | 2025-06-19 05:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bc22a53-3485-3073-932c-62e6e9ca883c | -9.57174 | -64.43779 | 2025-06-19 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f7f05a0-1919-3368-b7dc-7987bafde4f5 | -11.62229 | -58.2929 | 2025-06-19 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71ac09c3-9168-3ca9-a2e6-0d93ce51f00a | -11.5233 | -56.99145 | 2025-06-19 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 669027ba-1b55-37c6-bcc6-0bb2b5c80ab4 | -11.13945 | -53.93307 | 2025-06-19 05:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 614cec2a-cb40-3877-819f-c45cba300e5d | -11.62009 | -58.29521 | 2025-06-19 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60234fbf-c88c-329d-88c5-a663ae7f342e | -11.61559 | -58.29457 | 2025-06-19 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c46410d0-1829-3e72-bd5d-6d2704f8eb15 | -9.92361 | -63.11514 | 2025-06-19 05:38:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 606101e9-d141-3fd1-84a7-594f5bb87e2b | -12.42533 | -54.86796 | 2025-06-19 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
