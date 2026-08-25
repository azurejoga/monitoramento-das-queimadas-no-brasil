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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f199434c-bb28-3ab3-a8b4-5ab545cf099e | -6.86737 | -59.40869 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b00c6443-ac6f-325f-b84f-1a109bf7cb91 | -6.09441 | -53.4095 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12cfd343-a8a4-3844-921a-2256a7a600d8 | -6.15175 | -57.94258 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 14d6f3c7-856c-32f8-b240-33e3950ec4a5 | -6.61358 | -58.39029 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1233d0bf-3284-3b82-bac6-403acbf85bf6 | -7.0085 | -59.24143 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 167c9fd4-7c7f-369e-9360-1e7d84aaa11e | -6.43625 | -54.96697 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eab5b31e-6352-379c-9418-7772c98185d6 | -6.12082 | -57.82677 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 545651e4-8665-3962-82c1-808b23e01b13 | -8.5714 | -54.85619 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fe2ad74-403a-3d98-b207-498c8999bf4e | -6.80397 | -59.40419 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4069d40c-df26-365f-a58e-9490840799bc | -8.2092 | -54.97303 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5771424e-0f49-3afe-8ba0-fdfec7fcb913 | -6.99114 | -59.24911 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| f5596afa-e18b-358f-bdff-bc6b1669faad | -6.12511 | -57.82748 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0771d9b-379f-35aa-8435-ecbf43f9fa14 | -9.67681 | -55.09048 | 2026-08-25 05:48:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5cee9fe-bdb1-3253-a182-2853203abca9 | -8.80999 | -62.31492 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73c9b05e-b1a4-3c44-a44f-0343339b5e3e | -5.9049 | -57.7134 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9870a2e1-566e-33dc-93ca-abdac0a0a087 | -6.26536 | -55.41946 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05693139-7f3b-3434-83c6-d72905d519cf | -6.3529 | -54.76711 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d94add28-69e2-34b2-bbc3-52dc5a707ccf | -6.35384 | -54.76051 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 505b42c7-b3d6-301e-b727-f9ddbfebf512 | -10.77163 | -50.92151 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 70f91554-f1aa-352f-93d5-ad4b1c360a85 | -6.63418 | -58.49272 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6f7ec770-903b-3f79-ad97-8235b8b4bada | -8.66256 | -62.84302 | 2026-08-25 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b983ae4-2b1c-3317-87ee-b4f4bac58375 | -6.18162 | -55.43641 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae7ce4a5-c508-35ab-be35-fdcbe7457b59 | -6.34412 | -54.75221 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3f75b60-5026-379b-9047-7e91505979b7 | -8.22798 | -54.99685 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 604c705d-a8f6-3440-8b72-484fa788bb78 | -5.9419 | -57.73191 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43f2b10d-9861-3351-90bd-1aa27f21605a | -8.57779 | -55.28107 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d01983c-8f6d-312b-bbd3-8f93042cc37f | -7.01323 | -59.23693 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 973f2b54-8c5a-3c4f-a15e-e0148da1a1df | -6.7746 | -59.44352 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 009d33a3-d73f-3922-8fdf-29cbdb452875 | -5.78061 | -57.55049 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2915c459-8512-30b3-8976-679ffa54fbba | -8.57378 | -55.28111 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b47d8377-e9b3-3968-b710-6568ec0d655d | -6.17484 | -55.44741 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fd67c55-e22d-3d70-aff5-6f6c2136275d | -6.24844 | -55.42887 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1157db3-cd39-32f7-8383-6c9ae7cb65b1 | -6.12776 | -57.71929 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8468561f-725c-3e03-a2b4-48cfa1a77a60 | -6.80858 | -58.65797 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90a0eb76-b29b-3529-bec6-f45e7e6e4438 | -6.35682 | -54.77783 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bdd3e3e-7de2-36d5-b4a2-bf0216374df6 | -5.79011 | -57.6097 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 276e023d-4091-39f7-8929-334104d3f40b | -5.78742 | -57.56678 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90f70f7f-2bcf-3668-9293-e46acf46240a | -7.5467 | -61.36827 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6cf29d49-68f0-379c-b523-5ff3198b80d0 | -6.44245 | -54.9612 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6346b7f-b865-3aa8-a468-e123d5219024 | -6.01016 | -57.66525 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71116f50-dd70-3f9b-985c-6dcbd5736080 | -6.80467 | -58.66453 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 050609b5-2ccf-37b9-8d41-508279319a9d | -6.60946 | -53.34646 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9767e0ff-5455-3822-88f9-59d48df72003 | -8.82088 | -62.336 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1bd2551-720f-3cde-ab9c-01d7ee2981f6 | -6.63724 | -58.5008 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a17c4bc3-40f3-3a25-bff2-6508f574f6b1 | -6.79525 | -59.81159 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f78122e4-8f38-307d-8479-ff0a445c5f12 | -7.53848 | -61.35073 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 801ad641-fdb0-36e0-91f1-b136a7c3c5cc | -6.81178 | -59.59499 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c4baf82-b813-3bf2-a9b0-24906a756dfd | -6.22948 | -55.48948 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1fc403b-8382-3ae2-9be2-4e3f620b5d13 | -11.15856 | -54.00207 | 2026-08-25 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58322d1c-fa9d-3fc9-b1a3-4e482a637e64 | -6.63167 | -58.48083 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5dae53c-4f3a-3e24-a456-247cc23fa602 | -8.57775 | -54.85039 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 9988b70a-9a0d-3fb0-ab67-124bf3c5b115 | -6.60942 | -58.38961 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2cf5236-94de-3c9a-9f43-bc38d0e3ca38 | -8.20969 | -54.96935 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1d37682-9316-320a-956c-d2e2ff5af551 | -7.58499 | -61.2132 | 2026-08-25 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc9967fa-6e2b-3c58-bf54-0498a0c8a485 | -6.35431 | -54.75716 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f7373da-2a31-3a3f-9b3c-98d3464fcce9 | -6.1718 | -53.6988 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c9d185e-5189-38c5-b0c8-66ced3b90875 | -6.1269 | -57.81531 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b9b09d8b-3fe4-3895-a78a-b05388418277 | -8.8134 | -62.33871 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 832c918c-c0dc-3fbb-b4ba-80b5a6907943 | -6.54803 | -55.08437 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d159265-c6ac-39db-bce9-a0174d48361b | -6.17904 | -53.47704 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c75787fd-1ff8-3f6d-bfbb-736eab667c55 | -5.77563 | -57.55399 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81be3869-9cf1-3092-8d6c-95cb2c364bae | -6.94068 | -52.78061 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a638080a-34e7-3230-9da8-a1e84f1a8f36 | -6.81269 | -58.65862 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfdceaa7-e4a7-370e-babf-b4a8bad5320b | -6.33252 | -54.75731 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82ef6c0f-f03e-34ee-afdb-7f02b4202e01 | -6.99983 | -59.2452 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d40d3d16-a3e3-3178-968a-396021363221 | -6.17269 | -53.48027 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de7b2df-e271-301d-9127-0c66cfcf6916 | -6.17527 | -55.4445 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5209ae8c-7728-3c69-a825-75b9ed3966e6 | -7.56773 | -61.20642 | 2026-08-25 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f07a48b-919a-31e7-b7e5-edc72f12823b | -10.78197 | -50.92089 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 403b1e5e-dee0-3e54-a38a-efa4d3e2c3a7 | -7.00454 | -59.2408 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4741b645-7a24-3a91-99b2-2bdbabd6ac71 | -7.3538 | -55.66229 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e3075fb-671a-3701-bb79-d64c17730323 | -7.35851 | -55.66578 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aeed31d1-f3f0-3bf5-ab6f-ad6cb9dd8e65 | -8.54356 | -55.30391 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38d7024f-79d9-3142-b640-76d042e14492 | -6.76995 | -59.4479 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69a011e8-e1ad-37df-8071-24e399800ce3 | -6.61822 | -53.19155 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 471328e3-cf6e-3a25-af7b-8fa0a354cc01 | -11.17054 | -54.00366 | 2026-08-25 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7de3e96-6285-302b-91fd-5641d3452e0f | -9.20363 | -59.57644 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1873d895-74da-3425-b345-6cb82ca55b27 | -6.79596 | -59.80684 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aafc149e-f09c-3439-96fd-5a24bb5410ea | -6.96675 | -59.08201 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db486d46-df64-3e84-a181-726b4c0a9ab8 | -6.33549 | -54.77496 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c07f4f78-6f85-3d15-93bc-77bc8d43dc0d | -6.96738 | -59.07769 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84a7f1b8-fec7-36da-8252-151f0ed95c8a | -6.83594 | -52.50653 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06a1ccb0-95e7-30ec-82e8-e979c0cf731f | -8.57404 | -54.87804 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70fbd2e4-4190-36c9-95a8-44e128395478 | -6.13501 | -57.84962 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67116c9d-ae0d-31bb-8ca9-f160a526b8a6 | -6.35778 | -54.77108 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef81554c-b8fd-3769-9589-8491db1371cb | -6.34507 | -54.74551 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bae2684-fd2b-3912-8dce-7ab02a040e55 | -7.38362 | -55.17467 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07f8bbab-4b09-3f86-a3cf-1a52153f66e4 | -8.17728 | -54.96483 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fbd68d6-803f-3ea8-9cf1-efbccadfcc82 | -10.7708 | -50.92865 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 0d0d6239-fb3b-38ec-a762-ced9492132aa | -6.13749 | -57.86251 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85f33ef5-a5a6-3676-8d70-48c3e7ca5d31 | -7.50046 | -55.37126 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c423e689-a5e3-3021-8c08-08134dd3ade2 | -6.01078 | -57.661 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 781631c1-7ebb-3d84-93a9-a8bb21d57038 | -6.33393 | -54.74729 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9386e7e-c404-3604-bc65-9ad3a22d6563 | -7.00926 | -59.23633 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d05ac7a3-c8bb-3913-9866-18e1234a965c | -6.60999 | -58.38582 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ae28c46-d8d1-3998-ba55-1a0926fa5cb1 | -6.81322 | -58.6549 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dabe7a42-ae9e-3732-88c0-7c4ee45821c3 | -6.80477 | -59.58891 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 398ce811-b024-3cb3-a232-de796b0e9a29 | -8.22292 | -54.99367 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efd2d0f0-d63c-3a89-81a2-39e9139e3008 | -6.18484 | -53.47779 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a045c65a-3ee5-3468-bb20-c2f5f5ea4a33 | -8.81398 | -62.33492 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README62.md)
