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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d15edcf2-0222-3294-aba8-921859c192c9 | -12.94922 | -45.279 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| beaadce0-292b-3edc-bc1c-59b85ca983c4 | -12.94627 | -45.30447 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 5e7959d5-8a5f-3c9f-a3d9-daefcaa1f2cd | -12.94339 | -45.29668 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| e737a924-5643-3811-8722-f81321a28f79 | -12.22478 | -45.49157 | 2024-09-26 05:42:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| b527db86-a334-308b-bec1-fa1930bb532a | -12.22187 | -45.51555 | 2024-09-26 05:42:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| cdf3a442-51ce-3d68-93a0-4f31780d67df | -12.11216 | -45.03553 | 2024-09-26 05:42:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 32a26e4c-474e-3eaa-a045-1821924fa171 | -10.80451 | -45.81519 | 2024-09-26 05:42:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 6650c119-1c63-3dd7-b211-b18fe8fd2cd8 | -10.79663 | -45.78787 | 2024-09-26 05:42:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7d46a655-5336-3d7d-9523-4091ea9a2d1e | -10.79389 | -45.79279 | 2024-09-26 05:42:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 70da5125-1df4-3a4a-8520-43a6ab12011d | -10.79386 | -45.80893 | 2024-09-26 05:42:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 364.5 |
| b83eb7db-954e-309b-b6af-f8e9694e6040 | -10.79128 | -45.81388 | 2024-09-26 05:42:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 81a0ca58-ca2f-3bff-adf8-38cbfc35b21e | -10.63157 | -45.84503 | 2024-09-26 05:42:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 7a2f0895-a13d-30e5-81d1-1f8c6114b409 | -9.90798 | -57.05495 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0c120eb1-3bdb-3e99-b8f3-910767dfa56b | -9.89696 | -57.05299 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 634e4297-2add-34ea-886e-697532efdc4f | -9.81658 | -53.5635 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cc8f45a6-e48b-3cd7-9cf2-8b322a569544 | -9.80758 | -53.5621 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 046cf24c-8643-3aa9-804a-abf44804bbf9 | -9.80615 | -53.57136 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6a6f9848-03d9-34e3-819f-6d0cfb56b9a8 | -9.80473 | -53.58064 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3ea52386-4b45-34c9-93e7-21dc7dcb5d0f | -9.8033 | -53.58993 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bbe349cd-aa69-3e73-a66f-2cc9ee5e3fa1 | -9.79858 | -53.56072 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 08521e6a-50e8-39e1-a38e-9b3ffd618cb4 | -9.79715 | -53.56999 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| dfdc9134-416b-3b67-b2ac-9f64811e62c4 | -9.75473 | -57.77994 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 570fac2d-4f47-3658-ae03-adb1475bff0e | -9.68766 | -57.2013 | 2024-09-26 05:42:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e3a79328-dd39-3881-8c55-2562290519b2 | -9.66631 | -53.51864 | 2024-09-26 05:42:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 42a63956-6937-3f8a-ad24-c28e76a552df | -9.60568 | -57.76451 | 2024-09-26 05:42:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 24b3c8d0-adf8-37a2-a253-3eab056626f9 | -9.5939 | -50.14114 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 2ebf0fb5-5cf4-3664-9ccb-8ab75719a186 | -9.59246 | -50.15126 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 1ebd849d-52e1-3308-a23c-b604bf7cde80 | -9.54917 | -50.18633 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8913685c-961a-362d-b05e-bc6e40420706 | -9.54776 | -50.19639 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 688fef98-4d1b-319a-a45c-daad5d424bb7 | -9.47791 | -54.55465 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 94c934a1-7a7b-32ff-ba85-dda1c1d4fa48 | -9.45749 | -54.56197 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0d25e299-4388-390c-8fc0-c585d5b40005 | -9.44022 | -51.51661 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a2142c23-6ca0-3f72-acf8-7b87d2fc2208 | -9.42773 | -51.47777 | 2024-09-26 05:42:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1cdefabd-5605-3e51-a56b-3006ca03c39f | -9.39738 | -56.85981 | 2024-09-26 05:42:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 1e83bf67-56b6-3c3d-8418-8554de0cbcd2 | -9.39545 | -50.03832 | 2024-09-26 05:42:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c1ad39b3-ead1-308c-b3a4-542d8c968fda | -9.37536 | -56.85661 | 2024-09-26 05:42:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7e1f6fa3-ff77-3f75-abc9-f52245912634 | -9.34146 | -51.06501 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dd8e2fa9-85d1-32fc-b249-2bc09cbd19d9 | -9.34011 | -51.07433 | 2024-09-26 05:42:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 0c9a5bd3-f136-3ef5-8b3e-08ce40b8460a | -9.3311 | -51.07298 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 560e6d91-97a9-3a38-9d50-d30b4bf37177 | -9.32489 | -50.73086 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e6d60403-4a0e-335a-9fbb-af88e8c13dfd | -9.32345 | -50.74076 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ae5f0067-830b-367b-af21-86f2f4b3df3e | -9.32205 | -50.75049 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1eeb66e9-89aa-360e-8ba6-101b850f3139 | -9.32073 | -50.75959 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59e1159c-4158-33ac-8f91-ec93bb623b14 | -9.31714 | -50.71997 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 778f5ece-42d3-3b3e-8b58-8461a79075ea | -9.30526 | -50.92995 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e552fd4f-72c0-33f0-8586-4dee026a8d0d | -9.30389 | -50.93931 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e1f5746-df97-3d16-9bcb-fea258b6cd8e | -9.30249 | -50.75699 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a1120ef9-abf5-32be-ae1f-6f258598c226 | -9.30114 | -50.76635 | 2024-09-26 05:42:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 35cdb894-496a-3332-b540-c2e280dc00d1 | -9.17432 | -54.6656 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4d0afc0c-b97c-3012-8960-a618d238b1aa | -9.1727 | -54.67589 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b3aaf9e4-c63f-35a3-97e8-5d4a36a76a8d | -9.13517 | -51.52665 | 2024-09-26 05:42:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 75e12607-aae3-37dd-b9c5-24186d19af38 | -9.11873 | -61.30845 | 2024-09-26 05:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 20ddefd0-f55d-3664-85dc-700ee428908c | -9.11315 | -61.34032 | 2024-09-26 05:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b5735152-234a-3e25-8730-56e64a7cb213 | -9.10991 | -53.29286 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 70db3736-c7e5-314e-b7f8-a90664bb169e | -9.10851 | -53.30205 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7793b294-6c67-3f1b-9a59-0fe34568a6e1 | -9.08971 | -61.11044 | 2024-09-26 05:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 9801e81e-3ffb-3312-845e-b2795f42cccf | -9.04245 | -60.42817 | 2024-09-26 05:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| cf7eb391-8acb-3b0f-b19c-57baecbd3b26 | -8.92278 | -54.74697 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7fcfd73a-69f2-333e-9244-602f01cd6faf | -8.91319 | -54.74565 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41305211-5fc0-3119-9abb-431cdf9afa42 | -8.89247 | -53.02612 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6a7f7275-c727-3497-9292-c35109c04fbf | -8.88354 | -53.02482 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 895c2e09-d0ca-35e5-958b-fa6a2bc03df7 | -8.80693 | -58.20467 | 2024-09-26 05:42:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 42c48a00-3aae-3edd-b72a-cab1f3f5b7cc | -8.80396 | -58.22257 | 2024-09-26 05:42:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 2af50158-ec8c-39aa-8f73-5838806d5f1a | -8.71027 | -54.79902 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c9426243-b883-3190-84f8-83c1d1d126fc | -8.7023 | -54.78709 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 256cd51b-3d6d-3f4f-8bdd-44d1ec984a48 | -8.70064 | -54.79762 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 23483041-bd93-3311-a4e3-38768f3419aa | -8.69429 | -54.77542 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f9d9c8d9-1f35-3384-bafe-5fcd12f0b09f | -8.69262 | -54.78601 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6e049293-cdeb-3db9-a34c-3038a8ad0c87 | -8.66425 | -53.07204 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 03c1241b-abb8-3276-bfe7-ce6bf68e1676 | -8.65645 | -53.18277 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 571e8ee2-84ad-3d0b-8335-ac814df2e0bd | -8.64781 | -53.11055 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7c20c223-359e-3a55-834c-394047b83e78 | -8.57563 | -53.34373 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 884ef5c5-d6d3-31dd-afd7-109547a6646a | -8.53116 | -54.5766 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e6ba283c-29ca-3547-be45-f6840867546e | -8.52952 | -54.58699 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a3f4bb6f-2e5a-3358-a073-a29ff6c0970d | -8.52163 | -54.57516 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f7a967c8-32ba-36f8-b2af-0753df0c19d5 | -8.51868 | -55.17709 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6104c486-d898-37c8-b0f8-6ff16f558f0f | -8.51688 | -55.18832 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| e15998ea-a26f-3a92-9d8a-70a3da1ba052 | -8.51583 | -55.18256 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 758a59bd-6737-39eb-8175-28fb63b41da6 | -8.51409 | -55.19387 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 829f1fca-644f-34fd-b58f-181df0d2358d | -8.4651 | -53.22592 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ec594504-34a0-3498-a7b4-eebcb63be598 | -8.42289 | -54.68159 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a96a5f64-568f-38d8-9d0f-573546938d22 | -8.42122 | -54.6921 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e4b8ed32-4660-3779-b4b0-ad98d3ade4f4 | -8.41955 | -54.70265 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18f8fbd0-19d4-3cde-b09e-e0d6a3a6620b | -8.38204 | -54.93896 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d8998400-33c1-3dbd-8f3c-1c58656d04c8 | -8.3803 | -54.94989 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 16e50941-84c2-3f81-ac24-a4cc5a7ee4a4 | -8.33533 | -56.50989 | 2024-09-26 05:42:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3c7c4277-321f-3ee8-a984-ec1aeabfbe33 | -8.31898 | -55.00232 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 741685a9-79b2-3aed-8111-848850e82d24 | -8.31093 | -54.98975 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e54c4874-34d1-33ae-a9a3-1811e51fdc25 | -8.30918 | -55.00084 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 31e5cc15-83f1-346d-83a3-07a41fdb24fb | -8.11491 | -54.79454 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 23e6b3b2-f20e-34d7-a973-f2ccf7bdc6c9 | -8.03396 | -50.4224 | 2024-09-26 05:42:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 040da4e0-6156-3021-baac-5e79c8280569 | -8.03111 | -50.44173 | 2024-09-26 05:42:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dfc2d825-0a62-3ec2-8b4c-4d1bb45d44b4 | -7.81754 | -54.72954 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ad791332-afba-3000-b8c4-06241c862f76 | -7.80787 | -54.72789 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 3bff047e-f65c-32cf-aa16-21c36fea2409 | -7.79981 | -54.71592 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0b2aecd7-f738-35e8-9584-a584156b8007 | -7.79811 | -54.72679 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d4200b8c-1aaf-33d3-a04b-4101e4982aa7 | -7.79638 | -54.73787 | 2024-09-26 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3c6625be-552c-372a-b010-9ee5e9dd9b86 | -7.72452 | -55.71629 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5458d1d3-9527-32c4-8ae1-dd590a17ab80 | -7.71808 | -55.69018 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fd1bf613-37fb-32a0-a28a-a1a0ffb1a02f | -7.71608 | -55.70264 | 2024-09-26 05:42:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README153.md)
