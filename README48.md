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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73f6bc01-85bf-3594-8327-0c6df6b258f6 | -3.22908 | -52.91617 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8528976a-6efa-31ea-9859-7f05a586ba04 | -2.32948 | -48.58798 | 2025-10-26 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aff797dd-6070-347f-bf23-c1a78480a986 | -5.50605 | -49.5835 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af1a5a01-8959-33ce-9871-7a2dd7bd7d85 | -1.80077 | -54.18015 | 2025-10-26 05:21:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d17ac97c-2a7a-3dd2-8e4c-9365256e5748 | -2.98986 | -52.62598 | 2025-10-26 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83ab77f5-6053-36f3-9430-5fef8f055fc9 | -3.79545 | -51.35038 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd2cfe07-cdf6-3d5a-a19f-50c48245c852 | -4.87146 | -48.65117 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b24f893f-1bf1-3d6d-8d53-2bf7de90593f | -4.58052 | -46.50767 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da0840f4-21db-3e43-a3ee-9b9e807e050e | -4.25134 | -48.64372 | 2025-10-26 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 774636d2-ff03-3cd9-b087-0174c34579d1 | -5.88974 | -49.65166 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4eedcd0-11c5-368f-93c7-e9cb4c82980f | -6.80251 | -45.4075 | 2025-10-26 05:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35b2bee9-681b-3d72-88cf-49709cbf8b39 | -3.94407 | -52.12286 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 828bec7a-8a0a-33f0-bd02-47d1015d088b | -3.79813 | -51.34726 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7715e5e9-cf07-393d-bf97-efe75fd02ed1 | -3.10493 | -49.46709 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79687c95-caed-38ee-9836-6b4468028932 | -4.70824 | -46.43915 | 2025-10-26 05:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7b323cd-2b56-3c91-953b-54cc0868804e | -3.10717 | -49.451 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2934803-1396-3f29-a432-70e5f27f188e | -3.27453 | -50.05082 | 2025-10-26 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63421cbc-8c95-3207-98dc-309bb3ad4aa2 | -3.92925 | -52.25112 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 347a68fc-b8ff-3f0d-b70e-e00bcb843258 | -7.80528 | -45.3971 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a92b1acf-08b9-3adc-88d9-d1002cb87512 | -3.09589 | -49.456 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f630b037-41b5-3f19-bb90-adb3d103eaea | -8.73187 | -48.57036 | 2025-10-26 05:21:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 562d0798-3524-37a7-8536-6797bf1bc753 | -1.51982 | -55.86029 | 2025-10-26 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c06d5ae3-3f37-3405-96dc-1c4bc2563d97 | -3.79474 | -52.01973 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be10fc8f-817a-367a-a2ac-353c87978e95 | -2.81217 | -49.14558 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 797071e5-f641-38ec-a814-36cc18c41f9c | -9.43125 | -46.32795 | 2025-10-26 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a473dae-070f-319a-8a18-b0ad3fc6d240 | -3.12254 | -49.10128 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8646a8f4-227a-3ae8-b8d6-a9b2212331a7 | -6.39099 | -45.77189 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffcd1148-7ed8-34aa-8e83-acd0402b1606 | -3.46527 | -47.6886 | 2025-10-26 05:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d7de73d-3cb1-3188-a4a8-2c35b3568ce7 | -7.79999 | -45.39148 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b91f59b1-e613-38a1-86bb-148f3456a6de | -4.03074 | -46.06649 | 2025-10-26 05:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92fa21eb-2b04-31ab-9db3-46f12012acff | -4.60425 | -48.78971 | 2025-10-26 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91c5d141-a183-38de-8eb2-3583f9046d88 | -4.02992 | -46.0721 | 2025-10-26 05:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 590594f2-cc67-39fb-b67c-947280f2f78e | -3.10145 | -49.45342 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60546db5-55d2-30ca-8f2d-b49754ce5245 | -3.78478 | -52.04741 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 551e8438-e69d-3df0-bf2d-20d5159e4a20 | -4.59787 | -49.58682 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 391e37aa-d1a9-30cc-bdd4-570c7343175c | -3.79738 | -51.35242 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6e23d0db-c9fb-3945-8347-2b6ef339f172 | -6.54017 | -54.96728 | 2025-10-26 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bf1749b-1377-396c-864c-ceeafafadfa4 | -3.76222 | -52.25933 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3e65b7d-a806-3743-9264-346971029168 | -2.319 | -48.58281 | 2025-10-26 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6ff0f67-bd68-3347-b849-36da91856f0c | -4.58063 | -46.50689 | 2025-10-26 05:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a5da88-7258-3246-b271-933afc4491c4 | -4.71139 | -46.42856 | 2025-10-26 05:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5611b94-9eee-31cb-b15b-7d22c53ece1d | -3.10006 | -49.46298 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 181889cf-54cf-3b69-93de-3344e20afb40 | -4.2673 | -50.50579 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d8f534d-2aac-3ba3-8621-83c48bb0b193 | -3.1067 | -49.45424 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 633dea43-8269-32b8-a0a4-5dfc479325d8 | -2.78926 | -54.42176 | 2025-10-26 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cf4cec6-321c-362b-9572-8ddf56b1ecf9 | -2.90394 | -53.13678 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ddf34d6-b618-33cb-bb9c-727ae5a1dc9a | -5.70697 | -49.31492 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e06a957-ffec-3011-90b9-f722ec3b75c9 | -3.80013 | -51.35098 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de4a4e7b-b2fc-3eeb-8bdc-756b8cd5c830 | -3.79624 | -51.34531 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf633531-7173-344f-9cf4-bf039c9b38c8 | -1.88813 | -54.61942 | 2025-10-26 05:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e52f4b98-818a-3d7e-94c3-ed49ab7dbefc | -1.75365 | -55.74837 | 2025-10-26 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2319e4ad-ab49-35ed-9742-a5adf5212cec | -2.66813 | -49.49527 | 2025-10-26 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5bc5436-74b6-3c17-8470-94c203b80fa4 | -3.09638 | -49.45279 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99609c62-990f-33c7-b979-906a6dc2287c | -3.31712 | -50.11065 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 827925f9-9750-397a-aa4a-adb59b108b3f | -4.59697 | -49.59311 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00d45ab2-1532-358c-b5e2-ddf9b9835ae3 | -3.10396 | -49.47339 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aad3f94d-1925-339b-9358-78dd1399b67d | -2.89988 | -53.13615 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92f4a406-6f82-3371-bc60-275ad5fca852 | -6.39586 | -45.78438 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc7ff75f-c177-3390-bbe4-0b028bfe9a9d | -7.42163 | -48.77176 | 2025-10-26 05:21:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2ed1013-b9e7-38a2-ad42-5a266b0b8747 | -8.3334 | -49.31162 | 2025-10-26 05:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2abfa710-0484-375a-bf07-07ac01ec115b | -5.71153 | -49.2821 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be63e66a-e13f-3dd3-a930-9ebd18d94ea8 | -5.71299 | -49.31204 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6875ccca-369b-385f-b223-99c736d1b3fd | -3.76157 | -52.26353 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 736cf2a4-2f45-3850-a8ae-4b84939e8bb7 | -2.06597 | -56.86958 | 2025-10-26 05:21:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 385cb6be-0b10-39e3-8c85-f6f2b041107c | -5.71255 | -49.27479 | 2025-10-26 05:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 491c644f-242a-31bc-ac20-71a99e4ed198 | -2.98033 | -49.12011 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bc30f46-761d-3f51-8655-bda0fc6d698a | -3.47922 | -50.07845 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a44012db-462c-31a8-a1d5-d0943535d561 | -2.6674 | -49.49496 | 2025-10-26 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f862bbf2-d3ae-39b3-ae39-7a39226b5a12 | -2.66692 | -49.49808 | 2025-10-26 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a1a258a-42a4-34af-b553-313c12e0dbdf | -3.09687 | -49.44956 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| feca3cba-b6ed-391d-891b-c09a83c0b74a | -4.15154 | -47.66017 | 2025-10-26 05:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b07d557-fdfd-37d6-af0c-e20325201f3a | -3.83835 | -50.20265 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40fcf21a-4809-32e2-97b4-e93c3cebc7dd | -3.10531 | -49.46377 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc34f652-82d2-347d-b8fd-36eae6759fa5 | -2.66767 | -49.49839 | 2025-10-26 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efd686c1-6782-3378-a99c-d08a8e77a472 | -3.41034 | -45.46142 | 2025-10-26 05:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9fe5e75c-497a-3ba5-91ff-e7a14befc9c7 | -3.41083 | -45.46196 | 2025-10-26 05:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 283b1406-cdf4-3d52-a948-058d76466ee3 | -2.22715 | -48.37391 | 2025-10-26 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 960b0173-f71a-327c-a200-670dcae1a9c3 | -3.13171 | -52.99969 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3099d44d-4943-3dd4-a74c-24b04122a7aa | -8.3133 | -46.81612 | 2025-10-26 05:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88f930dc-3935-3af8-b031-bc0caa4e4f81 | -3.81525 | -54.72234 | 2025-10-26 05:21:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a84a079a-5f55-3f64-86dd-d18485431d00 | -3.61075 | -48.91867 | 2025-10-26 05:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cc93e0f-fe3c-3ea4-bfeb-af4b39b23a0d | -3.11485 | -51.21295 | 2025-10-26 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8ba192d-4d3a-39ca-ad6e-e655e1a64cbe | -6.3905 | -45.77132 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 444fe431-3445-3ada-9030-03620b64dc77 | -3.0954 | -49.45919 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 604dc924-bd60-332a-b3e6-afc7ae57868b | -7.78462 | -45.38645 | 2025-10-26 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51a8e827-e296-3b9e-8609-5e4cca90b127 | -3.10286 | -49.44373 | 2025-10-26 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08a607e8-eecf-3791-ad1b-ee1ee26e949e | -3.23107 | -52.9159 | 2025-10-26 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7314823c-eb2e-3d2b-92b5-1db206c0832f | -3.76174 | -52.26614 | 2025-10-26 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 442c9233-b9d7-3a60-84f3-591e462eef7b | -3.54357 | -53.3194 | 2025-10-26 05:21:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45efbd89-2429-3da2-9c19-ba3f6f6635f2 | -6.38836 | -45.79105 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f67290a5-fdc1-321b-a92c-02dbd1ee07bd | -2.78994 | -54.41726 | 2025-10-26 05:21:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4afe1019-0131-3dde-ace5-056561586506 | -4.25697 | -48.64464 | 2025-10-26 05:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5f184b03-a028-3c3e-8f66-ec44b5bd8bd0 | -4.2615 | -50.51073 | 2025-10-26 05:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d405cfc-aee4-349a-a29a-6cb5cccf4912 | -9.43661 | -46.34198 | 2025-10-26 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66e07dc9-c2f1-33b4-84e3-d7ffe7ed06fe | -8.32 | -46.81696 | 2025-10-26 05:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d09c365-27bb-3348-bbc3-15b9948de8fa | -6.38923 | -45.78471 | 2025-10-26 05:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 20d9b005-43e8-3611-a501-1c5f4ce799f7 | -8.54021 | -47.20083 | 2025-10-26 05:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 829e27ae-9b41-3298-a1ad-44c2eeadc2c5 | -3.83375 | -50.19895 | 2025-10-26 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13c9abb4-30ba-38cb-9df6-463d093d31ea | -6.66359 | -47.74346 | 2025-10-26 05:21:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49a37ed7-c3c1-3383-8532-b4a6c1df7887 | -3.96522 | -45.41756 | 2025-10-26 05:21:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README49.md)
