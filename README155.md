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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c401b292-e7e7-379f-9647-39e7758a2ed6 | -10.2017 | -50.3749 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 6888545c-7bd5-35b3-beee-63bad1278998 | -13.9189 | -48.1882 | 2025-10-04 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| bd89a6b4-82ad-32e2-8bec-9993f64fa313 | -10.2398 | -50.3497 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 8c7a117e-a57c-338e-963d-dba838177295 | -5.8739 | -42.5289 | 2025-10-04 14:20:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 82c02436-90e1-383c-bfe8-d5540e00ec33 | -13.0968 | -47.8429 | 2025-10-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e9e1231b-fcb4-3b63-9408-b2a71a75c523 | -10.2209 | -50.3517 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 33eff2b9-aa11-3170-a7d5-05f81e7cc491 | -11.6314 | -45.0646 | 2025-10-04 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| acc7a5d4-f458-3a64-865b-9be882112562 | -14.672 | -48.2933 | 2025-10-04 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 80111bb4-a835-3270-8b03-6a64c4d0da05 | -13.3229 | -48.0993 | 2025-10-04 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 6d16508f-2538-356c-b473-c77fc4655d94 | -10.1081 | -50.3203 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| d6292de8-80d0-35e6-b9e7-837db44d3ef8 | -8.1891 | -44.1357 | 2025-10-04 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 3cb737f6-3ab8-3844-84e3-78eb7dac970f | -8.7964 | -49.9106 | 2025-10-04 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 2e65e8ef-070d-3eb7-81ed-b215c39a2155 | -9.2979 | -45.9574 | 2025-10-04 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| dc6cafc9-2b09-3149-954c-62d5aa3b1d1f | -7.793 | -44.1535 | 2025-10-04 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 53b45291-9c04-3f98-adff-507acb508c8d | -13.3233 | -48.077 | 2025-10-04 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9ae17bbc-c125-358f-b3a1-d48ef5438928 | -13.1333 | -47.949 | 2025-10-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| d18224ad-63b7-30ff-804b-4196b52b1ede | -8.2314 | -46.8289 | 2025-10-04 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7c09bc94-4d09-3279-8292-61b3defdd027 | -12.8401 | -50.504 | 2025-10-04 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4fed150e-7b09-3aa7-b8e4-e0953c81ea55 | -10.1267 | -50.3398 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3997c379-7fa8-3b93-902c-37601b1b081a | -7.7741 | -44.1554 | 2025-10-04 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| da56245c-3ba7-3e2b-8600-bf40655f7b99 | -8.4686 | -47.4259 | 2025-10-04 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| afdef50e-3ad1-3aa0-a0d0-9bbbea89a924 | -10.2973 | -50.2799 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| c3a90f0b-4788-30c2-b114-2e9c39802b7f | -8.1888 | -44.1588 | 2025-10-04 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 964755eb-32cc-3308-9092-8a0508b2a68b | -8.6136 | -54.9961 | 2025-10-04 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 6df89222-2c70-3e15-9fc4-3cbdea1a2ce7 | -6.1728 | -44.6203 | 2025-10-04 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 7332389a-3877-328c-89fd-16c559e37589 | -11.5069 | -46.7671 | 2025-10-04 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 289.1 |
| e993adf7-623d-3cce-b8d5-05e667539269 | -8.8523 | -46.8343 | 2025-10-04 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3bc882ea-3e42-3bf3-9ea6-127521a6aac9 | -11.9138 | -49.9289 | 2025-10-04 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0e5e5d55-a044-3e34-93f7-8fd1145b9704 | -14.3904 | -45.9369 | 2025-10-04 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 05398a7f-268a-3966-90ac-f3e3fa3819ce | -12.0895 | -45.1583 | 2025-10-04 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 7c79638d-fb63-3e4f-bdf6-074913abc5f5 | -15.2641 | -52.9172 | 2025-10-04 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 22be0294-5251-3e28-9721-4d3bc7e7531a | -5.7762 | -42.9372 | 2025-10-04 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 55935274-ac67-39aa-ba71-8b6a3a7db233 | -7.7746 | -42.5865 | 2025-10-04 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| faabf069-d513-3876-8294-c0f6cafa7bb0 | -14.9352 | -46.8507 | 2025-10-04 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 91fa4ab8-f499-3200-a665-7c719ef550d9 | -7.6458 | -45.4716 | 2025-10-04 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 1680d3ef-f759-3332-a079-d916d002949e | -14.8268 | -54.7926 | 2025-10-04 14:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 7afcae23-73ae-3139-9fe4-fcbefd2e43ec | -11.863 | -44.9612 | 2025-10-04 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| e3577b28-ab63-3fa2-9c5d-1907d35ede49 | -5.6843 | -42.7328 | 2025-10-04 14:20:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 831f59d9-4bd4-30dd-aad1-1c435589df07 | -5.4556 | -43.1491 | 2025-10-04 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1a39784a-b504-3b44-b7c6-190649ec1b01 | -13.2938 | -47.5905 | 2025-10-04 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5eb6ca62-e343-35ee-a2cb-eac0888cfec6 | -13.6717 | -51.234 | 2025-10-04 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 1c601018-88a3-3abc-9a42-26654b49c40a | -15.5211 | -46.838 | 2025-10-04 14:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| d5a799fc-5b41-3ef0-a6a8-5902d4ac8228 | -11.8442 | -44.9408 | 2025-10-04 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 290.0 |
| 1505bfde-0c29-354a-a2c3-9ede6886f97b | -12.8761 | -47.2937 | 2025-10-04 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 250.8 |
| 23c8fb2a-0a97-3cc3-9535-2c9dc596121b | -13.116 | -47.8401 | 2025-10-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 303.0 |
| 488128a8-eebb-31ff-9583-4fa3a284eb22 | -6.0618 | -42.5133 | 2025-10-04 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 229.1 |
| 136ac154-a7c7-3322-96ca-345857c6e664 | -7.8593 | -48.2037 | 2025-10-04 14:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 5e47575f-a02e-346b-8dba-91f166e7336b | -15.3601 | -47.9554 | 2025-10-04 14:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 65eee3bb-dd7a-397c-8d54-11564ea98c68 | -15.3797 | -47.952 | 2025-10-04 14:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 634cd75b-9566-393f-8b61-187e02bfaae1 | -16.3627 | -51.4752 | 2025-10-04 14:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 253bd789-ed80-3699-b470-e660255cc890 | -5.4554 | -43.1725 | 2025-10-04 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 262.5 |
| 1063ae5d-6a90-3db3-a5b4-685866a45439 | -6.287 | -44.428 | 2025-10-04 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 22939016-4b5c-3252-a75e-7512dc87d8be | -8.8537 | -46.7228 | 2025-10-04 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 5e71d281-727f-3a01-9762-74c5318a825d | -8.8529 | -46.7897 | 2025-10-04 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 713bac53-177d-3427-961b-6a77711c5a5a | -15.3792 | -47.9746 | 2025-10-04 14:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 8b117797-20dd-3fa0-b7f1-cb6622431350 | -13.1164 | -47.8178 | 2025-10-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 863153ec-9d8e-310d-9a0d-5d3ee10a2ff6 | -5.4744 | -43.1477 | 2025-10-04 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 04072a75-9eba-3d0b-860d-6b9079e70793 | -10.5835 | -48.7178 | 2025-10-04 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| d5c14e55-6f3d-3edd-a28b-2e89e433d9fa | -10.5838 | -48.696 | 2025-10-04 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| f02035dc-71ce-30c8-842d-d4774a878569 | -11.8635 | -44.938 | 2025-10-04 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| e5337d27-6e59-3d5b-96ff-b30b4b92e71b | -6.2408 | -45.3424 | 2025-10-04 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 24790673-a3f5-3dba-afe8-d8f7221b241c | -11.1268 | -47.9077 | 2025-10-04 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| cc0fd0c3-f9e5-3074-b9b5-8918c45d09e6 | -13.3032 | -48.1244 | 2025-10-04 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 18e56529-9a82-318b-909c-a19100d0187b | -12.4364 | -44.079 | 2025-10-04 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| d70ff066-839f-339f-8b0c-a38f5fc51d39 | -5.6655 | -42.7342 | 2025-10-04 14:20:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 142.4 |
| edc425d5-1d6e-3f28-940e-782a0f3401bb | -5.2588 | -37.9238 | 2025-10-04 14:20:00 | GOES-19 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 144.3 |
| 2506e642-12f0-32d3-9083-3ed8aa61fa14 | -6.1542 | -44.5989 | 2025-10-04 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| b7492cdc-3bec-399f-8616-f3065b8985e1 | -8.8526 | -46.812 | 2025-10-04 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 76768cf8-b791-3412-95f8-2e4ea2126d7c | -9.6293 | -54.3158 | 2025-10-04 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 8ecaec23-4bbf-3c73-8db7-99301498de07 | -7.7941 | -42.5369 | 2025-10-04 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 132.0 |
| d53f4e29-6ebc-347a-9a78-ca1152e5dcc9 | -13.3127 | -47.61 | 2025-10-04 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 307d2c22-89e6-3bb6-bce9-eb22d1e2d2d9 | -11.5054 | -43.5426 | 2025-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.5 |
| bad5923d-bf64-34cb-b454-a59ff6b4d218 | -7.7687 | -46.2255 | 2025-10-04 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| d6556cfb-8f20-3511-9c37-bf332c965352 | -6.1234 | -45.9139 | 2025-10-04 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7cea2290-5830-32f2-b4b7-aa4d99fc345c | -12.3162 | -45.3545 | 2025-10-04 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 90e19885-ae4b-3667-8fde-4990c7150f90 | -12.9468 | -51.0053 | 2025-10-04 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 0143280f-535b-35db-8e47-1f026af26685 | -6.6069 | -44.3098 | 2025-10-04 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4f6bfea9-a7ff-3a5f-af09-c9fd53cae27e | -6.6416 | -42.7934 | 2025-10-04 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 120.1 |
| 06096017-d2a0-32aa-9188-ced78a5cbdfc | -8.6322 | -54.9949 | 2025-10-04 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| ea29e820-02a2-33da-a56e-a4358597dcd4 | -9.1114 | -44.4029 | 2025-10-04 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6484faa4-aba2-346f-afa4-b131327cdc99 | -7.7933 | -44.1304 | 2025-10-04 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| e500ca94-9eb6-300e-b3dc-eb00b653cfdb | -13.4925 | -47.2685 | 2025-10-04 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e34c9364-3749-3e87-bbe5-6c449d723f8a | -5.4742 | -43.1711 | 2025-10-04 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 352.5 |
| 6d2d1141-d5ec-327b-b41d-7b1a78f5a848 | -9.3193 | -45.7741 | 2025-10-04 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 30277330-8f4e-325e-b8e6-6e51af153d9d | -9.1901 | -49.9604 | 2025-10-04 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 119bf9ee-f9cd-33a3-ae32-78ff0290920d | -11.7924 | -46.8184 | 2025-10-04 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 73e69e40-baa7-3a85-a642-c4f0631cecfb | -11.792 | -46.8409 | 2025-10-04 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8089c7a2-4714-3765-b24b-0b77f2709c16 | -11.4877 | -46.7696 | 2025-10-04 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 92301802-10cc-302b-962c-72a9bd651054 | -6.154 | -44.6217 | 2025-10-04 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 508.5 |
| a3bb10a5-81e8-306a-a110-dfb7352fe9d3 | -15.5402 | -46.8574 | 2025-10-04 14:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 04457e15-09af-323d-a858-b7be8b944e82 | -14.3709 | -45.9403 | 2025-10-04 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9aac02b8-8882-3c52-916e-02f22740fb9d | -9.1713 | -49.9622 | 2025-10-04 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 0a32c4cf-e7a9-3a7e-8af2-0648dce2fac5 | -6.1992 | -45.7961 | 2025-10-04 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1a5d5ee2-0653-3f7a-a835-95265f54c153 | -10.2959 | -50.3867 | 2025-10-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9159451b-da56-3399-ac54-1e7ac913cc55 | -9.2976 | -45.98 | 2025-10-04 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| e73a9657-d5c2-38a0-9899-d83e5942f446 | -11.9011 | -44.9786 | 2025-10-04 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 86a54409-4338-31b7-b2b3-6667ad5ed6a7 | -14.3899 | -45.9601 | 2025-10-04 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 4a2b40ad-aab8-37a3-98d8-626acc789b7f | -11.6318 | -45.0415 | 2025-10-04 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d4b180ea-46eb-3be9-843e-410b5b1e3972 | -15.3179 | -46.3011 | 2025-10-04 14:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 411.7 |
| d36df23c-9967-38de-9d48-5fd9a5535d27 | -11.449 | -43.4803 | 2025-10-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |


[Clique aqui para ver as próximas entradas](README156.md)
