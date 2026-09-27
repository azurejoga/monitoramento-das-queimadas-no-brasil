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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 801f0d44-8c3e-39b1-9a47-f648d0fd02b6 | -12.2495 | -50.405 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 95c8c348-d85b-3974-9e96-df0a35c1ff8d | -6.84 | -43.572 | 2026-09-27 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7caa1bc3-13d9-3922-a99c-d10c77f3019d | -17.0533 | -56.5693 | 2026-09-27 13:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 7dfee33b-eb6e-39dd-b431-a3fe31331afd | -12.7028 | -47.3189 | 2026-09-27 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 85760261-e46c-3cae-bc9a-c0b2aa910902 | -12.4351 | -44.1497 | 2026-09-27 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| a9a4cb03-51ab-3d00-bfe6-664af7dcf017 | -9.9318 | -49.3733 | 2026-09-27 13:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| dd09d5e5-b7b5-3cec-bca2-0de2d8a2bef3 | -11.0393 | -51.329 | 2026-09-27 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| debfdf39-b125-3ace-8f1a-90803363cdfe | -9.8494 | -48.4709 | 2026-09-27 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fb507ffe-f8c0-3f2d-864b-d61a7efaa8b0 | -11.9415 | -50.6131 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 402f8c96-dcff-3e8d-981d-a8d66eb5c982 | -12.2699 | -50.3166 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c1cd61be-c916-3a25-b57e-fd78edcd247f | -8.3397 | -44.1658 | 2026-09-27 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| b91f2403-29aa-3e21-a02a-09dbdbc84d7b | -12.8059 | -54.0255 | 2026-09-27 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 842f8049-9dac-34ca-86be-70cb6831fe65 | -8.3583 | -44.187 | 2026-09-27 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| af93aaa2-d2eb-3aa2-92ee-dcb76ccadfa9 | -12.4157 | -44.1529 | 2026-09-27 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 9cebbb14-fb1c-3ae4-a012-a47f89581b26 | -12.2723 | -50.1657 | 2026-09-27 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| dbe3d9a5-f140-31cc-8027-eedfdd01acfd | -8.34 | -44.1427 | 2026-09-27 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| ae7d6c43-b362-38b2-af57-feb9c90bc050 | -12.7225 | -47.2937 | 2026-09-27 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 8cf8e909-0bb3-3501-bd3a-412866e1284a | -12.6651 | -47.2795 | 2026-09-27 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| cd08a727-4169-3c2e-ba7e-0088ad159a11 | -12.7225 | -47.2937 | 2026-09-27 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 340.2 |
| f08ea8d1-088d-3630-b237-04259cf42459 | -6.8596 | -43.5003 | 2026-09-27 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 8fe32831-5947-3ba8-8801-d76b8b1ad524 | -8.5984 | -54.6139 | 2026-09-27 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 1f6c3e65-02c9-3c66-824b-453ec4107589 | -7.055 | -42.849 | 2026-09-27 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 132.6 |
| 1f90b30c-6b01-38b1-939b-8135dcbab2b4 | -12.6655 | -47.257 | 2026-09-27 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 4bae576e-abf3-3a26-88ff-343339ed9b2a | -10.8052 | -60.7257 | 2026-09-27 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7b151580-091f-3d5e-8910-309f79339657 | -10.147 | -50.2311 | 2026-09-27 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 93355912-5066-398d-bee0-063dd506097c | -12.7221 | -47.3161 | 2026-09-27 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 312.8 |
| bc98850f-cffb-31c1-a90b-29d6033e8890 | -6.8405 | -43.5254 | 2026-09-27 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 03dc13fc-674d-3b71-9728-615f4330e258 | -10.4234 | -53.8014 | 2026-09-27 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 61ab5ec7-290a-35bd-bfcc-22697b7bc346 | -11.0238 | -54.0148 | 2026-09-27 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 62cbddc0-c0d7-3203-a271-4d33be713217 | -12.6463 | -47.2598 | 2026-09-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| a0be5e8c-e1ff-3b1f-bd40-25f4847ef5a6 | -11.0991 | -54.0285 | 2026-09-27 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 2388a4ef-feff-3d62-84a5-190613600526 | -13.3824 | -51.3138 | 2026-09-27 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 9952261b-2ed9-3560-9768-41169bbb4d27 | -6.8408 | -43.5021 | 2026-09-27 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 723196c5-5aec-3f3c-b37c-d52420751028 | -17.0533 | -56.5693 | 2026-09-27 14:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 7bc3216e-1789-353e-8ceb-4242a485a964 | -12.6647 | -47.302 | 2026-09-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| fa791ac5-b042-3fed-a47d-5734b1786f3a | -12.4157 | -44.1529 | 2026-09-27 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 6f5c5e63-53e0-3662-8e3c-97b931c00e6d | -11.8014 | -49.8129 | 2026-09-27 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8ef514b7-5a69-39bd-adc4-bb1aece3c7b0 | -12.8059 | -54.0255 | 2026-09-27 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a1ad39fd-399b-32c7-be25-c9c305c570fc | -12.4351 | -44.1497 | 2026-09-27 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| bfc2a3a7-5025-39a0-96ad-25e71cf12411 | -7.3842 | -42.1039 | 2026-09-27 14:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| d5adfab6-0875-3fcc-a216-939e748807a8 | -7.3653 | -42.1058 | 2026-09-27 14:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| 2ba9d2fc-6b3f-3b80-b479-806a1666959b | -11.0991 | -49.765 | 2026-09-27 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| efef2133-0e19-375b-a48d-538e9acf56e6 | -12.3068 | -50.3981 | 2026-09-27 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 86847346-fb18-370b-bca9-647dddcc1cf0 | -17.5697 | -46.9019 | 2026-09-27 14:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| edd3a30d-41cf-35ef-b0ca-e2fddf71d0fd | -13.8151 | -51.8553 | 2026-09-27 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 4da2760b-6dbe-37cc-a24d-d795685433bb | -12.6651 | -47.2795 | 2026-09-27 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 8e00ebe6-eec3-346e-a48f-7961b5153fe9 | -8.3589 | -44.1406 | 2026-09-27 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 356.0 |
| 488469b1-3577-39cc-a522-9783bbe4c84b | -12.288 | -50.3789 | 2026-09-27 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 62c845b0-0b5b-36f9-9bcd-c22f56b73013 | -17.0529 | -56.59 | 2026-09-27 14:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 82b3afca-e6b4-3252-a2dd-47d599fb1f75 | -9.9318 | -49.3733 | 2026-09-27 14:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 65d1b64a-d9ca-37eb-8cb5-3706a046ecc2 | -11.3221 | -51.4261 | 2026-09-27 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 1e04d19f-0d81-3126-89dc-e076b850935a | -10.8238 | -60.744 | 2026-09-27 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1990597a-9dc0-3cf0-a4de-f7569c7db9ad | -8.4483 | -54.725 | 2026-09-27 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 43eee5ea-efc3-3c16-9ede-5567e52d38f2 | -10.4046 | -53.803 | 2026-09-27 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ff6c21d8-57f1-3cd0-b514-1752a7703780 | -9.0247 | -49.6549 | 2026-09-27 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7082c762-02e1-376e-914b-631e7cd5f835 | -8.6171 | -54.6126 | 2026-09-27 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8500f3c1-147f-333a-aa68-089c245142ae | -12.7028 | -47.3189 | 2026-09-27 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| c5f1dad7-9688-3e60-817a-28561d58fdba | -10.8532 | -54.0916 | 2026-09-27 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 86c46230-fb40-3f6e-9ad2-8a46a1f2b74b | -6.8594 | -43.5237 | 2026-09-27 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e228d40b-b858-3d9a-8e14-8783e54dc70b | -7.2755 | -43.321 | 2026-09-27 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 71a014a7-34d4-317e-acfb-ebc1b6d9a8a9 | -12.8061 | -54.0048 | 2026-09-27 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| eb91e929-e0dd-37d2-b99d-1e82b9adb9b5 | -9.7874 | -44.8289 | 2026-09-27 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 44e1b12e-e471-305d-9dd0-83defed11e29 | -6.2026 | -47.5026 | 2026-09-27 14:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c56ea194-973a-3774-9890-a445dfcca034 | -7.365 | -42.1298 | 2026-09-27 14:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| 87d1d594-5927-35c2-9753-fc604b6b7dd7 | -12.7032 | -47.2964 | 2026-09-27 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 640e2d85-fe78-36f5-a05a-0b03fbe7fc9b | -10.0162 | -50.1374 | 2026-09-27 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 5a0db2b1-1351-3115-bf4a-0ecb46fee394 | -10.8052 | -60.7257 | 2026-09-27 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| bff2b86c-1d3e-3c92-b705-a13510454be0 | -12.6655 | -47.257 | 2026-09-27 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 46ba4002-504f-381e-8268-821bb23ca876 | -11.1714 | -50.0151 | 2026-09-27 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 88d496f1-7318-3909-9846-7e3352af47e3 | -9.9318 | -49.3733 | 2026-09-27 14:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| cb512b12-1288-33e7-9fb8-53204bb932c1 | -9.0249 | -49.6334 | 2026-09-27 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| cb3c115a-4eb0-308a-a7c3-159362c839e0 | -11.6186 | -50.5861 | 2026-09-27 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6e5f168c-71d3-33eb-9860-54d09c07977b | -12.6463 | -47.2598 | 2026-09-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 36ea9eba-7db0-3632-ac64-22225893012c | -11.8014 | -49.8129 | 2026-09-27 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| aa79deff-d242-3905-afce-0edc03d180da | -10.4046 | -53.803 | 2026-09-27 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c7c8e4c6-9a96-3459-b0a5-097eebdfa2e2 | -7.365 | -42.1298 | 2026-09-27 14:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| e4733c12-29b9-3bca-ae9e-c89714e38f7e | -11.0991 | -54.0285 | 2026-09-27 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6473a444-ec51-31b9-957a-1a995d1dd236 | -11.6567 | -50.5817 | 2026-09-27 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 690d64a9-11a4-3817-a78f-c0c5b1646e46 | -10.6094 | -53.9902 | 2026-09-27 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c5a22a2b-919f-3529-9599-5142a33ac967 | -15.9869 | -54.9419 | 2026-09-27 14:10:00 | GOES-19 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 97f06a78-bebc-3430-a499-0b028bfdba70 | -13.8151 | -51.8553 | 2026-09-27 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b3c559b7-88d6-3c5e-b002-598de89467fb | -10.8944 | -50.8569 | 2026-09-27 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 866752c3-40dd-3c52-9fc6-b60af05c4a25 | -17.0529 | -56.59 | 2026-09-27 14:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| d7e0f77a-6203-35ab-9825-4bb1c82526e2 | -9.7874 | -44.8289 | 2026-09-27 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 135e8f79-be2e-3354-ba97-66805960fd22 | -17.5697 | -46.9019 | 2026-09-27 14:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 83.8 |
| cbf45a4f-21bc-3036-8443-eff7ed5ba088 | -7.3842 | -42.1039 | 2026-09-27 14:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 47d6f839-8a06-3aba-871b-5e3e78734019 | -11.5818 | -50.5047 | 2026-09-27 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 580731ae-80a5-393f-ad00-46a5b062380f | -7.055 | -42.849 | 2026-09-27 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 123.7 |
| e2549eb0-5b83-3ded-8e67-3d7bac6ace42 | -6.8405 | -43.5254 | 2026-09-27 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 93a97aef-7dae-3cae-95ce-fd8b7d0ad240 | -11.1524 | -50.0172 | 2026-09-27 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e7f50241-9133-31cf-814a-e892540f9e95 | -9.8427 | -44.937 | 2026-09-27 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a0c16a49-fae4-376c-977a-5d4e0197d560 | -12.7868 | -54.0275 | 2026-09-27 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 616efd6c-01d9-37e8-9c48-fb964d4b1d92 | -6.8408 | -43.5021 | 2026-09-27 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 33a9641f-ecf6-3e2f-aced-a312eefcfeac | -6.2026 | -47.5026 | 2026-09-27 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 83f092fd-2f7c-3714-82c5-c658c177e6d0 | -6.8596 | -43.5003 | 2026-09-27 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| aa3c6330-f6bf-3aff-b8d0-d75b6433a04f | -8.6171 | -54.6126 | 2026-09-27 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b4590f3c-6ce1-364c-82a6-69e48b4738ab | -8.5984 | -54.6139 | 2026-09-27 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 4e6c81fa-cae1-336d-87e2-668d35cc6134 | -11.6377 | -50.5839 | 2026-09-27 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| cdcc03f5-ec7f-3a05-a38e-9581ab8d65f2 | -12.6647 | -47.302 | 2026-09-27 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 96875bde-c971-34fe-9438-8d0b20c80417 | -6.84 | -43.572 | 2026-09-27 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |


[Clique aqui para ver as próximas entradas](README59.md)
