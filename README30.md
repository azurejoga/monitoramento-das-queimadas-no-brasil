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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f284bd0-73c4-3509-9be2-8070a111d487 | -4.2542 | -43.7381 | 2024-10-07 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| ff050628-5341-3ded-b98b-a2d7aa306cb4 | -4.2728 | -43.7601 | 2024-10-07 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6e15d045-2ea3-3725-87b9-23ce706b8647 | -4.2729 | -43.737 | 2024-10-07 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 0f54db0d-96ac-371f-b33c-c7617ec4fcaa | -4.2916 | -43.736 | 2024-10-07 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f3ea01b4-87d9-35ed-8696-4c1e6f7dc509 | -6.1304 | -47.2224 | 2024-10-07 01:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 7d5c07c9-f711-3b8c-a75b-53c2d50e8c3c | -9.5343 | -40.3282 | 2024-10-07 01:35:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 1d557fce-3a41-34e2-bd7c-bbbbfe264bed | -10.8337 | -68.3636 | 2024-10-07 01:36:08 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 12947ffe-1b9b-3c14-8239-1de60b647fec | -10.8754 | -63.9169 | 2024-10-07 01:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e8c2d3c3-3d96-397d-862b-df64883087cb | -10.8755 | -63.8979 | 2024-10-07 01:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| fa9e472c-05b9-3842-a354-76f5c0d506b8 | -11.2583 | -60.3885 | 2024-10-07 01:36:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8b71e61b-0b6f-3fee-a9e1-0963c20ac192 | -12.0585 | -63.7841 | 2024-10-07 01:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8ed1a2f7-522b-30d5-8eb2-45c69a618936 | -13.5911 | -50.3197 | 2024-10-07 01:36:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| eb44b3c6-0785-3a94-bae1-c96d3e7d84ea | -13.5915 | -50.298 | 2024-10-07 01:36:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 8af13533-2467-3240-b187-51e2bcc259e3 | -13.8354 | -44.6398 | 2024-10-07 01:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c0d34eeb-2552-39b2-b7a7-4b932cc1202c | -15.0418 | -51.2616 | 2024-10-07 01:36:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 3d917e62-0fb0-3a8d-85ae-a0b174cb7ca5 | -15.0422 | -51.24 | 2024-10-07 01:36:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| f667bbf1-c1bf-366f-995f-18da4ae528f6 | -16.1419 | -48.897 | 2024-10-07 01:36:36 | GOES-16 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3425386b-25b7-31d1-8398-f41ed15aaac9 | -16.4877 | -57.7408 | 2024-10-07 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.3 |
| 521ec187-4e5a-3880-9b69-c39bef6a3ea7 | -16.488 | -57.7205 | 2024-10-07 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.2 |
| 778569a0-5786-3e29-91ce-cfee6d0d050a | -16.5072 | -57.7387 | 2024-10-07 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 207.6 |
| 3f85494c-7b8d-38d1-a5c5-aa150fe59f5d | -16.5075 | -57.7183 | 2024-10-07 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 195.2 |
| 0bb21c4c-21bc-309c-a43f-25dc6e4bf63f | -16.5267 | -57.7365 | 2024-10-07 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 5ebd393e-f344-3916-9471-62ca9d412a4f | -16.527 | -57.7161 | 2024-10-07 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 6c0e0404-c14d-3f7b-8836-1821e7d06fdd | -16.992 | -56.721 | 2024-10-07 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 651c2d45-052f-3d6b-98aa-2094c778b28c | -17.1786 | -53.9213 | 2024-10-07 01:36:42 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 347f17ac-b5cf-318b-97e2-a14cbccf655d | -17.02 | -55.0791 | 2024-10-07 01:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 9550e3b2-5df1-31a9-9e35-43ccec4b227d | -17.0116 | -56.7186 | 2024-10-07 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 7ef1fcc8-1964-3b44-ae84-a6b9977d3aea | -17.012 | -56.698 | 2024-10-07 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| 9f3e644b-874a-33c8-a2a4-2bc88ebbecd0 | -17.1581 | -57.3582 | 2024-10-07 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 417464bf-23e9-37da-beeb-e4b55fa839ae | -17.6279 | -53.1094 | 2024-10-07 01:36:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b6e30bbf-d42d-3bfe-97f0-d37827dcbc0e | -17.6679 | -53.0819 | 2024-10-07 01:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 5af58a40-7911-306c-b71d-93d2ad9180ae | -17.7324 | -57.0833 | 2024-10-07 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 3e183bf9-0119-3902-9cc8-776208d9d9d0 | -18.4518 | -53.5165 | 2024-10-07 01:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 71.1 |
| afe2bff1-5839-3429-9a96-fa8ce6fc4b2a | -18.4718 | -53.5134 | 2024-10-07 01:36:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 60bd267b-53b0-37e4-a17c-f2a1b61c223c | -18.6391 | -57.2578 | 2024-10-07 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 52da8709-2dcb-3521-9530-25887ad594da | -18.659 | -57.2552 | 2024-10-07 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 38cc5060-8d41-3813-b695-775bff6f2e3b | -18.8686 | -54.5617 | 2024-10-07 01:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 90.3 |
| bd3b245d-d9ed-33f2-9a40-065907117506 | -18.8886 | -54.5587 | 2024-10-07 01:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 121.6 |
| e2b824ca-b16c-3bc6-aa07-e12000179939 | -19.8318 | -42.3542 | 2024-10-07 01:36:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 02737af2-ac7c-3618-8403-876db0b2fa96 | -20.1223 | -49.0748 | 2024-10-07 01:36:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 126.4 |
| d3874449-f7b1-3d0c-9b44-1e52ee89ea93 | -20.1229 | -49.0518 | 2024-10-07 01:36:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 274.0 |
| b31487cc-1fd7-3b61-adc0-d2750d938d59 | -20.5848 | -48.5137 | 2024-10-07 01:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 106.4 |
| aef75a99-055b-3b89-befc-be6a7adad16e | -20.5855 | -48.4904 | 2024-10-07 01:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 287.5 |
| 59dabf27-9937-366c-88c5-7a9b9822d47a | -20.6053 | -48.509 | 2024-10-07 01:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 5beb1f37-d2ed-3413-a93e-08974be52741 | -20.606 | -48.4858 | 2024-10-07 01:37:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 618.3 |
| c7973a63-3764-3912-acd6-16554e103c7c | -20.6066 | -48.4626 | 2024-10-07 01:37:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 01ebde7f-d34c-36cd-9aca-38eec71ca362 | -20.6265 | -48.4811 | 2024-10-07 01:37:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 5bcd3624-ad37-3dd5-a9e6-0afdf6f7ed9f | -21.0712 | -47.2331 | 2024-10-07 01:37:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c10ea6a6-cddb-3d10-8984-141292e1b280 | -21.0919 | -47.228 | 2024-10-07 01:37:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 105.7 |
| dc726b24-b2c0-3da8-98a5-92226f5544fd | -21.6121 | -47.7121 | 2024-10-07 01:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 03d162c9-ca47-3af4-ac27-a4558e8fa493 | -21.5691 | -47.7696 | 2024-10-07 01:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 86.2 |
| e7148724-979a-32bf-8f6c-7053c4ac06b8 | -21.5698 | -47.746 | 2024-10-07 01:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 293.9 |
| 7cc44f87-a39a-332d-8a8f-11a56a19fee2 | -21.5705 | -47.7223 | 2024-10-07 01:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 174.8 |
| fda3af5a-dbde-323f-a903-f7b9ce00c2db | -21.5843 | -47.9536 | 2024-10-07 01:37:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 435a8bf8-a296-38af-ac1e-46d2afb7a45e | -21.585 | -47.93 | 2024-10-07 01:37:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3cfc532e-1bf9-36f0-8006-2d945b4b6a50 | -21.5906 | -47.7409 | 2024-10-07 01:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 339.9 |
| 9433434b-0145-3020-9bc5-0461cee80f85 | -21.5913 | -47.7172 | 2024-10-07 01:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 252.6 |
| 7cdbc50b-dea2-3b66-b3f3-160b48af5e85 | -21.605 | -47.9485 | 2024-10-07 01:37:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 99.8 |
| db472ce7-502d-3d4d-803e-a6b581421bf6 | -21.6114 | -47.7357 | 2024-10-07 01:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.4 |
| fd717cea-1c31-3e2d-8812-5418af4ae484 | -22.1974 | -48.1778 | 2024-10-07 01:37:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 66.3 |
| b2379e35-483e-37fa-989c-c19769c12415 | -1.0182 | -53.739 | 2024-10-07 01:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 6cb68f59-ee1d-34b1-a07b-37bca4cca382 | -1.0365 | -53.7389 | 2024-10-07 01:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| a30885fb-8058-378b-9829-5418c4337dc0 | -2.2113 | -53.7029 | 2024-10-07 01:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 3990a45f-4db3-3847-9c58-4acde60f5f13 | -2.8569 | -52.9197 | 2024-10-07 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 2037ead6-7e39-3d8c-8282-9840f3298c6b | -2.857 | -52.8993 | 2024-10-07 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 960bfecb-b066-3868-b3fd-49519cb2e4ea | -2.8753 | -52.9192 | 2024-10-07 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 643d1ec8-ac29-3c9c-b7bd-c444b9c1babc | -2.8754 | -52.8989 | 2024-10-07 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 181.7 |
| 53685dbb-937d-321b-aadf-98fe2069aab7 | -2.8937 | -52.8984 | 2024-10-07 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 8f27bd22-db11-3624-897a-c2a347f7a7b7 | -3.538 | -65.0414 | 2024-10-07 01:45:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e6420a75-160f-3080-bd69-c8025fc83c67 | -3.5381 | -65.0229 | 2024-10-07 01:45:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 35ba1708-5727-36c1-87a0-bbde3b70516c | -3.5563 | -65.0227 | 2024-10-07 01:45:27 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| fc9907cc-a74a-32bd-871d-3d20533abf15 | -4.2542 | -43.7381 | 2024-10-07 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| b30a8632-42a5-3229-a482-78d4ab12f54e | -4.2728 | -43.7601 | 2024-10-07 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ce050b10-1616-3a20-bd30-51ab6be99e2d | -4.2729 | -43.737 | 2024-10-07 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 198.9 |
| f51c6e60-b379-3be3-942d-fcfffefd3930 | -4.2731 | -43.7139 | 2024-10-07 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c55130c8-8011-3a31-98ee-7e3a6afa5d2c | -4.2916 | -43.736 | 2024-10-07 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| e842d5dc-97dd-32f3-889e-4469a6ca5e33 | -6.1116 | -47.2457 | 2024-10-07 01:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| b1594944-165d-391e-8d4c-3f7a9710c783 | -6.1118 | -47.2237 | 2024-10-07 01:45:41 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6b70dd47-4f11-372d-9a94-e83f7f28bd7d | -6.1302 | -47.2444 | 2024-10-07 01:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 461e287c-4522-332f-96ce-4af4d39d40ec | -6.1304 | -47.2224 | 2024-10-07 01:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 7fab72f2-bcbe-32ce-9771-3ab55d64ef36 | -9.5152 | -40.331 | 2024-10-07 01:45:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 127.6 |
| 79f39bb2-f6dd-311e-96c2-74bf3686859a | -9.5343 | -40.3282 | 2024-10-07 01:45:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 221.2 |
| 8ff762f2-168e-377f-b64b-1664f3dcf794 | -11.7373 | -44.4926 | 2024-10-07 01:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 6beee9fc-5fa1-3c9b-bfca-d3b20be1e301 | -12.0585 | -63.7841 | 2024-10-07 01:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4a62d1fa-b77c-3138-a33e-ba86ee91f7d6 | -13.5719 | -50.3223 | 2024-10-07 01:46:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 8d7af0bb-a690-3866-9576-ed6bfb06abfa | -13.5723 | -50.3006 | 2024-10-07 01:46:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 2cbe3c3c-fb79-348d-ada3-265b68620ba6 | -13.5911 | -50.3197 | 2024-10-07 01:46:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 11abdf01-32fc-3524-b457-60c0b9668167 | -13.5915 | -50.298 | 2024-10-07 01:46:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 98c0ccb3-7aca-36be-89b1-1a0ae7dbf522 | -15.0422 | -51.24 | 2024-10-07 01:46:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 9554735e-c4fd-3862-905a-501c35f0abcb | -16.6195 | -55.5892 | 2024-10-07 01:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| ce7dfbf4-c621-3fcc-ace4-ff3930a9276e | -16.6199 | -55.5684 | 2024-10-07 01:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 3f5a8076-86c6-3269-8b31-65883ba83aea | -16.992 | -56.721 | 2024-10-07 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 5072f3a6-7e9a-3a93-badc-650c1b5a2f90 | -17.02 | -55.0791 | 2024-10-07 01:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f89f76f9-b7a8-39f1-9827-36c73676f197 | -17.0116 | -56.7186 | 2024-10-07 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 66ab1f21-a2d9-3f67-9cb2-43cf4e7127b3 | -17.012 | -56.698 | 2024-10-07 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 3b1f5572-caa7-3755-a3c3-9cdd56aef462 | -17.0982 | -57.4267 | 2024-10-07 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 156.0 |
| e5431e43-43b8-3b36-b2c1-c5ed2e133d1e | -17.0985 | -57.4062 | 2024-10-07 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.9 |
| 6f6681cb-55cc-30ad-b5dc-e5aa854c4757 | -17.0989 | -57.3857 | 2024-10-07 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.8 |
| d331239e-919d-31a0-b3c9-5c6eeb934420 | -17.1182 | -57.4039 | 2024-10-07 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 25a5ce32-c4ae-3a9e-978c-552566087b89 | -17.1375 | -57.4221 | 2024-10-07 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.5 |


[Clique aqui para ver as próximas entradas](README31.md)
