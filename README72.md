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
| 12defe03-6fd0-313c-9d7c-f4c8c4afe992 | -14.17409 | -46.1519 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cd0afafa-e4c7-390d-ac2b-d6f91c735c7b | -18.2734 | -45.39566 | 2025-09-14 05:48:00 | AQUA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 138ecd87-dc33-3509-8746-0e41449e13bb | -12.78267 | -48.02676 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 57091de7-09d4-32cb-9be1-84aa5e653d63 | -12.66119 | -54.66143 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f573f48f-4e9f-3d07-b0df-e1076701c690 | -13.92636 | -44.83816 | 2025-09-14 05:48:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a9d51877-f059-3e47-af91-a3b9fc48320d | -12.79099 | -47.97423 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 20599ab1-867d-3dd8-a847-3f41b680d5f8 | -12.77326 | -48.02523 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9b8480c8-0078-345e-a107-1dafc1a531e9 | -12.80511 | -47.94583 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 84f4ab25-d7ff-3d44-9292-fd9ad85cb953 | -13.93393 | -44.84873 | 2025-09-14 05:48:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| dc9c2a38-9a5a-3cd2-9977-c1f57cc2d0db | -15.94533 | -46.97216 | 2025-09-14 05:48:00 | AQUA_M-M | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d3447a17-7c10-3fc2-944f-8371bf4f594c | -12.67658 | -54.66442 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 520e47b6-e452-3bf6-a1f2-61200d44b88c | -19.71481 | -45.43191 | 2025-09-14 05:48:00 | AQUA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c11b7c6a-f23a-3403-b5d8-c2db47e31613 | -13.53284 | -43.00817 | 2025-09-14 05:48:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 1f645eda-1050-3f28-b852-430d8cb2c063 | -14.19032 | -46.16367 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1cb558d0-227b-3ddf-a518-21760570f776 | -12.70736 | -54.67046 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| cbc542ee-7117-3712-8dc8-0bdd1951630d | -12.75004 | -47.9896 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 188b9e6a-ad71-3fb7-9e81-61e214170587 | -12.69197 | -54.66742 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 367.2 |
| b423f5f2-7f40-34a3-ab0e-6120d1cec759 | -12.78771 | -47.99489 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 17209bfe-2ea0-3427-a902-8f9fbe7841b5 | -12.78432 | -48.01637 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| c0261b1f-75e0-38a1-b80f-2cd8b9f01939 | -14.19911 | -46.16504 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 843b94dc-f2a0-3c86-81a0-167ec2cfdcd3 | -13.94285 | -44.85008 | 2025-09-14 05:48:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| a7b733b1-6900-3c4e-b006-03970125fd5f | -12.92911 | -54.72592 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6c5e405a-0aa1-35cb-a9d5-02ef1de6f499 | -13.53435 | -42.99729 | 2025-09-14 05:48:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 55c6cc10-e496-3dcf-baab-fda257da0db4 | -12.93228 | -47.94756 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6a1fb086-deaf-3353-b7af-c3bea4e3314f | -12.75777 | -48.00153 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 485b50c2-3935-3d0f-81cb-0ff6ebce1d11 | -12.80352 | -47.95581 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| fd10691a-3e8f-3c02-9962-c8e6f2d2501d | -12.65531 | -54.6921 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 631da550-1150-3fa1-950b-a5c347ad55fd | -15.79815 | -52.20205 | 2025-09-14 05:48:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 0e377427-ab72-3d5e-8fda-3433eef31427 | -14.20654 | -46.17543 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 70aed691-afdd-3707-91ab-07b79edc17c4 | -12.99475 | -47.97668 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2c43e5ec-6094-34ef-ac78-5aba1776fbd0 | -12.77491 | -48.01487 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 3b7932e2-949a-3006-abdf-9d0c8325ee5d | -18.04351 | -50.92785 | 2025-09-14 05:48:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 4ad9d2ea-4ae3-3115-8e65-bc16320eaa61 | -12.96439 | -48.04728 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 90bcecee-8cbc-3758-84bc-1f105be0f2df | -12.9414 | -54.7333 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 0fb73499-e08d-30af-891f-ed9cf3f86298 | -14.27967 | -46.12804 | 2025-09-14 05:48:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a6def493-0353-3d50-826d-f315a5a441fd | -14.43699 | -43.19833 | 2025-09-14 05:48:00 | AQUA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 448e2b61-8f3a-31fe-b67a-d45eaae04e33 | -12.68617 | -54.69812 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 223.6 |
| e6ebea4b-cda8-3897-b414-7fc18070019f | -12.70154 | -54.70142 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 0ca69531-b694-3788-ac35-6820466c77f7 | -15.91128 | -49.97441 | 2025-09-14 05:48:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f0ab0288-3574-3ce5-a947-4d488e9a5138 | -19.71341 | -45.44191 | 2025-09-14 05:48:00 | AQUA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5090b4b1-1307-3a4d-beac-9e86980d9b90 | -12.80193 | -47.96587 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 0cd1eb36-b205-36c3-a232-58d095f5bc60 | -12.96604 | -48.0369 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 72177232-7ee8-3863-98a6-d9cc580d0daa | -12.92293 | -47.94604 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f3cb9a19-371b-31c3-83cf-5837b0d396d5 | -14.19775 | -46.17406 | 2025-09-14 05:48:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 16fa1ae5-ca9f-362b-96d7-c8dd09d37ca1 | -13.93528 | -44.83948 | 2025-09-14 05:48:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b09941d6-9d07-3fb1-96ce-e7dea1eed5d1 | -17.27749 | -46.0952 | 2025-09-14 05:48:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6fdd29b1-ca01-3a3e-ac50-70fbb6e9426b | -18.04129 | -50.94086 | 2025-09-14 05:48:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| befd9da7-b8ba-3836-884d-f60c4a96c8cf | -16.65381 | -49.77472 | 2025-09-14 05:48:00 | AQUA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b6025a59-7d13-3e74-86eb-b05bdee9a06c | -12.76716 | -48.00304 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| b39e92b6-60ad-3d45-b4fb-5db8f089f088 | -17.31553 | -46.08245 | 2025-09-14 05:48:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cdae8a4c-5b98-3731-9ac0-280c4c9f0be6 | -13.01158 | -47.97466 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 316c7e08-2258-3484-8b79-26a3bb9abad5 | -12.68266 | -54.65783 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| cefa1d66-e759-3e29-8d30-819493bdefa2 | -13.01126 | -46.74087 | 2025-09-14 05:48:00 | AQUA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8f1d9f45-30db-3453-a3b9-004ada853a7f | -13.0041 | -47.97819 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6be04c39-6a7f-3d06-be64-7d6915a6b493 | -14.28357 | -45.11234 | 2025-09-14 05:48:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3186dc77-52d5-3c06-86f3-2eb5c3102b88 | -12.7655 | -48.01341 | 2025-09-14 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 65898f8a-9818-3ad2-844f-d0317362421c | -12.66163 | -54.68552 | 2025-09-14 05:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| e4a24ab1-af96-39de-b4e3-ca1a00555646 | -15.80398 | -52.20847 | 2025-09-14 05:48:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 01d6f850-30d1-3a22-a856-0c24453bc718 | -18.0502 | -50.935 | 2025-09-14 05:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8937fc86-c90b-3475-b64a-45d128148c93 | -12.9485 | -54.7313 | 2025-09-14 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| bde6141a-76d0-343d-ae58-39d11cee552a | -12.9294 | -54.7333 | 2025-09-14 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a7d14f24-73a9-3190-92bc-528240659e2c | -12.9292 | -54.7538 | 2025-09-14 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8e43d07d-2513-3b8c-b45f-269bcdb5d596 | -22.22699 | -48.61017 | 2025-09-14 05:50:00 | AQUA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 89fb9626-50bd-3415-8a69-395490b84587 | -22.52357 | -52.98996 | 2025-09-14 05:50:00 | AQUA_M-M | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.0 |
| acdff982-c92b-3580-9051-d2225fd497a5 | -20.12561 | -46.87278 | 2025-09-14 05:50:00 | AQUA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ccceb9bb-f12c-34ef-899e-29991fbacc91 | -21.62915 | -46.80931 | 2025-09-14 05:50:00 | AQUA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 58201bf3-9ca8-3f49-aebe-c407fcbba38d | -22.72644 | -49.89275 | 2025-09-14 05:50:00 | AQUA_M-M | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 1a5a0528-e328-3be4-b900-d596ab9a2dc3 | -20.62065 | -50.36168 | 2025-09-14 05:50:00 | AQUA_M-M | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| ab1433c5-c7c8-36de-939e-980a6d5a6203 | -22.20344 | -48.35092 | 2025-09-14 05:50:00 | AQUA_M-M | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f742c408-7a75-3f5a-bd21-8beb35bec8f9 | -21.07688 | -47.10963 | 2025-09-14 05:50:00 | AQUA_M-M | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e4b20d5f-5b35-34ab-99b6-fa2bbb32fd60 | -22.72813 | -49.88242 | 2025-09-14 05:50:00 | AQUA_M-M | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 78a0af3d-a313-3a2e-9c9c-640c4eb3d317 | -20.08435 | -46.89769 | 2025-09-14 05:50:00 | AQUA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9b3e88cf-5412-30c8-99fb-fefa4c5b1144 | -23.47383 | -50.85255 | 2025-09-14 05:53:00 | AQUA_M-M | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 3b6b55a0-deeb-3666-8399-03685d94a6f9 | -23.65545 | -47.59309 | 2025-09-14 05:53:00 | AQUA_M-M | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| a238e10d-2c53-3fa9-bf25-4f5d9c00b671 | -14.7721 | -60.2107 | 2025-09-14 06:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a1e04a57-3d28-3401-bcf6-e7092484f88a | -12.9294 | -54.7333 | 2025-09-14 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 35bcea66-4c65-371b-906a-d6f9f40eeaf7 | -18.0502 | -50.935 | 2025-09-14 06:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 06abef5e-1099-3ed0-88d7-898b0b5d2e71 | -12.9485 | -54.7313 | 2025-09-14 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a594220b-ee97-30e6-876d-efd187efe8af | -22.7282 | -49.8866 | 2025-09-14 06:00:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 60.1 |
| e0558eaf-cf67-3caa-a25b-c4f32a13dc34 | -12.9292 | -54.7538 | 2025-09-14 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 2b4da025-67f5-35c8-89d8-fcdfc1129ea2 | -11.7903 | -50.545 | 2025-09-14 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7e98ccd8-a3af-39e4-bbff-52dbaacc7d8d | -11.7713 | -50.5472 | 2025-09-14 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| fbdf0a20-0b8b-3b82-8091-b97937e712ff | -12.9294 | -54.7333 | 2025-09-14 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| ba5467b9-6338-36d9-9d7a-9cb82e36f127 | -12.9292 | -54.7538 | 2025-09-14 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 48489129-e305-3664-b9e0-7bf28f053107 | -11.7716 | -50.5258 | 2025-09-14 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 1c43d4eb-9725-3f13-8238-1befad4c50b5 | -11.7906 | -50.5236 | 2025-09-14 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 597350ff-be4f-37d7-9250-aa00691f8b0c | -18.0502 | -50.935 | 2025-09-14 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 7ae687f1-8d4d-31b1-83fc-e3ceb84fc9e6 | -11.7522 | -50.5494 | 2025-09-14 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| e086b471-3801-3670-944e-3c028b1af17e | -18.0507 | -50.9129 | 2025-09-14 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| e4ddc141-8ff5-3bc7-9f89-8e048b169941 | -18.0502 | -50.935 | 2025-09-14 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| f41329ca-ac43-3f4e-9230-a75a5342d73e | -12.9292 | -54.7538 | 2025-09-14 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e5473e2f-a74c-3d9e-8ba3-42e17fb34f09 | -12.7486 | -47.9818 | 2025-09-14 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c6e8825f-875d-35f8-bb9d-86e95c422a9d | -12.7482 | -48.0041 | 2025-09-14 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 465cf6a5-229e-37f3-887c-2ac541f9c5fa | -12.9485 | -54.7313 | 2025-09-14 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d1f9d468-951f-36f5-98c5-d167f17a57b9 | -12.7671 | -48.0236 | 2025-09-14 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 298165db-774a-3021-83c7-13fec1be82bd | -12.7867 | -47.9986 | 2025-09-14 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 74a13fa6-285f-3dee-af44-9710318295a4 | -14.2107 | -46.1749 | 2025-09-14 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 09e8dab8-dbd3-3ea5-b647-37719e3f1cdf | -12.7675 | -48.0013 | 2025-09-14 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 255.5 |
| a944c1ed-69b8-3f75-8e9c-f3f45198a6ad | -12.7678 | -47.9791 | 2025-09-14 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 0bdc3a22-ad54-3512-8fec-e631cf47a13c | -12.9294 | -54.7333 | 2025-09-14 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |


[Clique aqui para ver as próximas entradas](README73.md)
