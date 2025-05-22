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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55a4d66a-35af-3d90-8123-61a2752fc66b | -10.54952 | -42.43026 | 2025-05-22 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b5a731a4-cc71-3465-9058-e2de2e3c453b | -9.04576 | -47.02242 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d6fc0f1-6ed6-32a9-a519-1e420b9c7b1f | -7.58002 | -45.86481 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57685e41-ecbb-3ac4-975f-126b523108c6 | -13.69892 | -45.27056 | 2025-05-22 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8664245-1b0d-3ebf-a41b-3de0757bfe5c | -12.08341 | -47.33902 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8dd247a-aaae-35c6-bd35-b93bc1bbfd24 | -10.54884 | -42.43441 | 2025-05-22 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 76c2a917-bb30-3755-b3c1-bddd7af3b7a8 | -7.97008 | -49.69672 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5040cfe4-87dd-391b-b9a4-6a4e2a8ad64b | -13.5338 | -43.68341 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fb04317-8690-3420-8695-f9462a2103c0 | -11.79854 | -49.34003 | 2025-05-22 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bb8e5fc-636c-38d8-9205-0118e0d3f78d | -8.78486 | -49.07627 | 2025-05-22 03:55:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bd516fd-11ec-3837-ac8d-ad3049440ea0 | -13.89551 | -41.30085 | 2025-05-22 03:55:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e0849d25-c8cc-3aa8-b666-c5ceb30fd979 | -12.30366 | -52.49249 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d311ba34-148b-3203-813e-07f64761ff89 | -12.36396 | -49.97968 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 007c351d-dc5d-3956-b7cc-8d65c4bfe36f | -12.34229 | -49.97144 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 236a6e91-4dd1-3a52-b2c3-fe9df1c6025f | -9.67332 | -50.9579 | 2025-05-22 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ad4c9c7-68a4-3efa-936b-f2cbfd019893 | -8.79193 | -49.06954 | 2025-05-22 03:55:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17b542fa-8765-3d66-9a47-686ecbd4a736 | -10.65653 | -49.44207 | 2025-05-22 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8cab453-a268-3c74-93d9-e38d27eeee9e | -12.34562 | -49.98394 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fdd9103-3889-35c3-80ad-ada5253b2bfe | -9.04476 | -47.02796 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a059c87b-a9c5-30bd-8a31-9efd2035056c | -7.46579 | -47.05892 | 2025-05-22 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3244e745-2a1b-326e-adf1-17e02276f9ed | -10.65579 | -49.44595 | 2025-05-22 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e17de62-4c56-38be-90a9-c390e6b5dcf0 | -12.84455 | -47.39524 | 2025-05-22 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eebd15e2-788e-3db4-8793-7b912c233a19 | -14.03679 | -45.51519 | 2025-05-22 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b94d1b1-3440-36fa-9643-46e074a2b91f | -11.56823 | -47.4507 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| df235e0c-2963-3720-b530-eab695f3cc32 | -12.34638 | -49.98013 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc918d87-7111-3ad7-b394-2c4362d14f40 | -10.71289 | -48.80861 | 2025-05-22 03:55:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b1b4a39-222e-3947-a6fc-a94d4aebc6c0 | -10.30284 | -47.02692 | 2025-05-22 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e4f42d5-fc05-32d4-b471-a7a877de7ef2 | -8.48206 | -49.60962 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1483ae8a-c537-3941-843b-8df72d057f48 | -9.02248 | -47.75134 | 2025-05-22 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0363ace5-f9fd-3b4f-a936-53532b4e8106 | -11.57842 | -47.86945 | 2025-05-22 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df8fb74f-ae89-3e45-a235-f20cbbe56a19 | -10.09769 | -47.09613 | 2025-05-22 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31f4f187-6833-333c-bcf0-76af4495c62a | -10.65726 | -49.43823 | 2025-05-22 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62036cc5-a2e0-3a8b-860b-d83caa89689c | -7.47033 | -47.06279 | 2025-05-22 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ebac08a-4999-3dac-bdef-8ff6090174a8 | -11.60071 | -47.61676 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82a6b33c-6367-38e8-85a3-de99cc8bc8e4 | -11.24425 | -49.49909 | 2025-05-22 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c6099b1-14ef-3bc3-8b05-af15d0e42977 | -8.74886 | -49.75048 | 2025-05-22 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| a218321c-dc3f-384a-b71c-3e7228ac8eaa | -12.08209 | -47.34226 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84bef987-2599-3f92-a422-222a4a609058 | -9.95987 | -49.81832 | 2025-05-22 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb8c0dd7-d679-3c6e-9876-a1c49f244daf | -11.89328 | -49.2058 | 2025-05-22 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04b66a50-a265-39e7-86e4-67086fc3c722 | -11.648 | -48.10324 | 2025-05-22 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 25b686da-ed97-3139-bb4d-c71867d5b1f3 | -9.96147 | -49.8099 | 2025-05-22 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2183c7d4-329f-3be2-8828-1845b02a4983 | -10.55117 | -42.43352 | 2025-05-22 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 09c57550-8f53-38f5-8783-a857fdfe716d | -11.79925 | -49.33629 | 2025-05-22 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72bfbb3a-c3f5-3121-9cf2-306bc45355e6 | -10.46137 | -49.15064 | 2025-05-22 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 375a220e-d556-3c32-90d0-f705e2948990 | -7.96495 | -49.69112 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1af2911-52d0-3cb8-ad7b-efb9cf68e5fb | -11.86377 | -52.27372 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f063f97f-96e9-3d84-a6c7-1f4a769567b3 | -11.92867 | -45.76477 | 2025-05-22 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41e2dfe3-c37f-3ba7-8aa0-402130a1a7a1 | -8.9067 | -50.02424 | 2025-05-22 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c96a7939-916c-3e5a-b97e-ab3b5abcd053 | -11.57207 | -47.45687 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4d155212-8231-30eb-8186-50466019d250 | -10.36381 | -47.97725 | 2025-05-22 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68c2b2d9-d71d-3507-8db8-4dca09cecdf3 | -12.3476 | -49.98677 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 288b147c-1038-36a1-a9e7-188357e88c03 | -12.34306 | -49.96755 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e185627-08d8-3228-a3fa-73cd78e6b4e6 | -10.32882 | -47.02037 | 2025-05-22 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50f31469-3a06-3237-9572-c785a850342a | -10.71225 | -48.81207 | 2025-05-22 03:55:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117b598a-652d-300e-9f6a-cd0191e834a0 | -11.64297 | -48.10231 | 2025-05-22 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c3460e22-9ef7-35ef-b8f1-6628926f8513 | -13.52044 | -43.69483 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab372828-505b-3e3f-b026-1ed788d5e5a7 | -12.08589 | -47.3484 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 967a8c19-5a96-316d-81aa-bc5d69e38419 | -11.57304 | -47.45168 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0194ee3a-d661-3f19-a988-aa19b5e8523c | -9.96067 | -49.81411 | 2025-05-22 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5af0d8fe-7626-3d22-a6cd-7d502ee68e58 | -11.60556 | -47.61777 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bcdf558d-5b67-3081-a8ec-07ebdd7ac167 | -11.57403 | -47.44631 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 04363942-7d24-3d48-b67a-5111fd95e872 | -12.86235 | -38.36608 | 2025-05-22 03:55:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| affdaa31-07ac-3d5e-9c18-429c087e7e2d | -9.01956 | -47.73815 | 2025-05-22 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd0cd58a-f727-37f7-be8c-f6a34de50b80 | -11.64354 | -48.0993 | 2025-05-22 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 04002d43-38a7-349c-88cf-ae1bcd896d80 | -11.55759 | -47.45416 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 65c30576-b49e-39a3-91a8-2156085139e8 | -13.38536 | -46.78822 | 2025-05-22 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b46067da-6ee0-3b65-b121-aa80976ff1ce | -13.51599 | -43.69864 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6a3b542-0817-324c-bbd2-e368056599eb | -12.29355 | -52.50829 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 53300b55-a387-3dbd-b86e-dfd6b2c5fcd4 | -8.47622 | -49.60841 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97f83cef-196d-3743-b7dd-cc8b4e4df81f | -10.35305 | -47.81781 | 2025-05-22 03:55:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f7ccc70-efbd-3529-bbd4-c3252f1c134a | -11.57113 | -47.46196 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 518e398c-12ad-3ce3-8456-4e5d94bdd04b | -12.29832 | -52.48545 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22e7fc2e-154a-3b78-b0b8-944564d4d018 | -11.58506 | -47.61941 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53402e75-b0f8-36a6-8e9a-1b6c081683a8 | -12.35395 | -49.98404 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f96f7191-9e6a-3371-abf9-badd070be502 | -10.3525 | -47.82082 | 2025-05-22 03:55:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77a99fc2-36f1-3a34-80be-0d8a60f47fe9 | -12.3547 | -49.98012 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9f7f20e2-38ac-3f94-9ab9-17bf39e3984c | -12.29061 | -52.48977 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8a608185-2091-3091-85fe-bc10682d7d85 | -10.46756 | -49.1481 | 2025-05-22 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c57f73c3-e212-3a13-961e-4b2c29cae382 | -12.28877 | -52.50544 | 2025-05-22 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 56a3a205-a27f-32e9-bf04-1b4a3ee7ffd2 | -13.38732 | -48.45322 | 2025-05-22 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22ea189f-4fa0-32fc-b693-6440c75f3b02 | -12.35838 | -49.97844 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28d0690c-b5e6-3963-9f0b-645b90c66af1 | -9.02303 | -47.74828 | 2025-05-22 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11cd28d5-fe4b-3d76-a286-960bcdcb0b5d | -7.58213 | -45.86164 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0818ad0d-acb9-3c56-8b56-a772f3547b9e | -13.53825 | -43.67961 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 0abcbbab-a0e9-3afb-87bc-5b278c3e5865 | -7.8046 | -46.20767 | 2025-05-22 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08442a32-e00e-31f8-877f-093cf83744c9 | -10.30296 | -47.029 | 2025-05-22 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c92961b-cc03-338b-98a1-37810f8a5794 | -7.96772 | -49.69425 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 78ea9ab7-bbf7-3d88-9e6d-8a7906d24b99 | -13.53089 | -43.67831 | 2025-05-22 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 49aadd18-3372-38e2-a99d-7fe3c95b6dd6 | -12.84357 | -47.39146 | 2025-05-22 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc3de92e-bbb1-305f-a202-16bf7f47b0ca | -10.98908 | -42.18478 | 2025-05-22 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0b2b28b1-801d-3b3a-b8bf-9929d2ed3dfa | -11.24337 | -49.49847 | 2025-05-22 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 496c6d8b-d263-322f-9754-4ca5e072192a | -12.83986 | -47.39432 | 2025-05-22 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7f8577a-682f-34b1-8db6-fc1968d98dc6 | -12.34419 | -49.9742 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75288c5d-a3fa-3dc4-bf36-cd252666b73c | -8.74967 | -49.74618 | 2025-05-22 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 27392929-cde2-3072-aa13-334958b4ed8b | -12.08114 | -47.3475 | 2025-05-22 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6756ebb4-6354-3274-aafc-bca784033963 | -9.60331 | -49.01762 | 2025-05-22 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e09c6b3e-974a-3f74-afae-66803114da52 | -10.02804 | -48.6987 | 2025-05-22 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 520ddbd7-9662-303f-b6b9-e4c1104274ec | -12.35123 | -49.98504 | 2025-05-22 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8d321f73-2b23-345e-a16e-58cdf5f42edc | -11.55859 | -47.44879 | 2025-05-22 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 8c72324b-e8dd-3ba8-8233-1e5f0b6199c2 | -10.37462 | -47.97593 | 2025-05-22 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README8.md)
