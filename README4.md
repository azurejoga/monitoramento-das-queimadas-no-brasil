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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75f08be2-39f9-32ca-a7b8-0b99b7339d00 | -6.0619 | -57.790298 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8759ac01-9962-370d-bd06-dc3456298336 | -3.5368 | -48.157902 | 2026-09-08 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d26563a-9b22-3c86-9995-8146a28ec434 | -3.888 | -55.818901 | 2026-09-08 00:46:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59a0ecfd-0b27-3ed2-b5fb-f10cefd1b90a | -5.9887 | -57.695 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c66fc73c-3890-3918-b549-d61a9f5bce92 | -5.9919 | -57.709202 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be449897-40b8-3e5d-ab82-8fde1a9828fd | -20.6063 | -58.002201 | 2026-09-08 00:46:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 254fb3ac-d65f-351c-8e63-3bf4402f44bd | -5.9854 | -57.725601 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a88ce3a-da1b-3a72-8600-66eb32dd40c3 | -7.1682 | -59.540901 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e731c5ee-9fb3-332a-b8f4-28c5f36eac61 | -5.9985 | -57.692699 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3321060d-7ca3-361c-a44e-5de67b6fc7c9 | -6.1715 | -57.728199 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2186bf77-722b-3deb-835f-493e55a56e0b | -4.3479 | -47.772301 | 2026-09-08 00:46:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eac4a16-7b79-3552-813c-41b62b95e387 | -6.3805 | -58.284401 | 2026-09-08 00:46:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4521a1b2-d159-3542-8346-42a2fbda7d28 | -3.0586 | -59.267601 | 2026-09-08 00:46:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 733cfcc7-e736-3e5e-828c-4329dd5278ee | -5.1555 | -55.953701 | 2026-09-08 00:46:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 996b4f5b-c439-3121-9c31-eefff2218bfc | -4.0383 | -50.865799 | 2026-09-08 00:46:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d94a104c-e62c-3eb0-89ca-38355aa92cd9 | -20.4963 | -57.417702 | 2026-09-08 00:46:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f6862eae-e440-3eea-8d4f-a9cec8359ab8 | -3.4186 | -58.311699 | 2026-09-08 00:46:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53fbff9b-2850-3d89-80d7-9b781ac6a347 | -13.2263 | -61.7043 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 64e3d147-9f78-3a48-9548-af3cbd8089aa | -13.2577 | -61.707699 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac584618-2fe7-30df-ab68-e058f71995ce | -13.2166 | -61.706402 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 90aa8b90-b2ab-389d-97f3-05fe4449b12b | -10.7805 | -60.781898 | 2026-09-08 00:46:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d65ff903-cd6a-32a9-9e0c-e2a57e6d3f55 | -5.987 | -57.687801 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0586a9f-2fa4-3f61-a57d-db59b5be72be | -20.4979 | -57.4254 | 2026-09-08 00:46:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c62a5540-1c7f-3ac4-bd0f-00c7879b86cb | -6.1079 | -57.630402 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec99c0f2-a4d9-3f70-b262-487ee6e174ec | -6.0181 | -57.688301 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e93dd7-7e09-31a3-97c3-2e780634316b | -5.9837 | -57.718498 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56b0577a-e20d-3b53-ab0b-ef9e3b70280d | -4.0427 | -50.884102 | 2026-09-08 00:46:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1e2bb9e-654e-38dc-a673-4b8f6dc5e1dc | -1.5981 | -60.144299 | 2026-09-08 00:46:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbd2ae45-d303-34e5-9b44-199217fa905e | -20.6145 | -57.992001 | 2026-09-08 00:46:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b5451d2d-cf1e-3968-a27a-e2ef52e03266 | -3.5272 | -48.160301 | 2026-09-08 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 120180ce-b7ac-3974-9857-e732ccc14384 | -13.2851 | -61.691898 | 2026-09-08 00:46:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20bbdec5-e6e9-3c22-9e7e-bc5b10a265cd | -6.0505 | -57.7854 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4371392-4f41-3cb5-9948-514a6d7eb1ad | -6.7693 | -58.956402 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0ae561e-fc4b-3c37-94b2-819bd89c8f53 | -3.6784 | -49.540001 | 2026-09-08 00:46:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c845e461-7b01-37eb-aa4d-dc6bb4dd50b6 | -13.2891 | -61.711201 | 2026-09-08 00:46:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5d5027c2-cdbc-392f-9095-00b1d54bd516 | -13.2459 | -61.700199 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46fa474f-1086-3f6b-8315-3225fb0579e1 | -8.5138 | -63.837002 | 2026-09-08 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 736445d3-2b44-31a9-b546-7ec6e3723cf5 | -6.0197 | -57.6954 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44cbf940-fb2b-3c29-a261-2f98a08050cc | -1.1902 | -55.7243 | 2026-09-08 00:46:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a441dbc-d6ec-3c52-9c41-54bd861a7e2c | -8.5334 | -63.832901 | 2026-09-08 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b01d7bf8-d8e9-3d39-b66d-be0f2649cba3 | -15.6389 | -54.178699 | 2026-09-08 00:46:00 | METOP-B | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 572f8ed6-6e3c-3096-bbba-8e56cba6d077 | -8.5236 | -63.834999 | 2026-09-08 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 59ad661b-bbb6-3cc6-838d-81f7f4afb6eb | 0.3034 | -60.437801 | 2026-09-08 00:46:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c5a1e029-d58f-3f21-8b26-a4871e324eb9 | -3.4226 | -59.236801 | 2026-09-08 00:46:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64c91297-9b6a-3ff0-965d-d459aeab0e09 | -15.637 | -54.170601 | 2026-09-08 00:46:00 | METOP-B | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b12591a8-c4b0-3951-8d85-d1e28e43ce06 | -20.603001 | -57.986099 | 2026-09-08 00:46:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cd815b98-3e3c-387e-8840-42e2efd20634 | -15.9963 | -56.422199 | 2026-09-08 00:46:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 162d731d-bd11-3465-bd82-8dac6358433e | -6.5685 | -58.979698 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 096f9824-2999-3c88-9bee-f0d3c3c58485 | -13.2557 | -61.698101 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23749105-c65b-36b9-8491-05c727705fdd | -3.5399 | -58.936501 | 2026-09-08 00:46:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89b3c6a4-3b4c-3327-b0b8-f9e2196033f8 | -13.2773 | -61.703602 | 2026-09-08 00:46:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbb6a8a7-4790-3fda-a0fc-0db935dc4587 | -5.9935 | -57.716301 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca8250b4-08af-3b94-ba2c-fc6f9df43daf | -3.5438 | -48.1866 | 2026-09-08 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3f9f5c-6164-34a7-ac5a-956ee8f5f1ff | -6.0521 | -57.7925 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a405568f-9c7e-30d0-8d0b-0857dc470b82 | -13.2186 | -61.716 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f69f4d0-c82e-301f-a96b-21b45b217857 | -5.9936 | -57.671299 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b230ead3-e6d2-3e3e-b5de-f1a3e456844c | 2.4635 | -60.774399 | 2026-09-08 00:46:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a650b82a-2fe4-3e35-9ae2-95946fefe0ed | -4.2336 | -59.953999 | 2026-09-08 00:46:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8eeddac-5fe4-38d8-8ad6-31e759655df8 | 3.3233 | -61.301899 | 2026-09-08 00:46:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c76598b8-2cc2-3dc1-99ef-7539e20511a0 | -1.1924 | -55.733898 | 2026-09-08 00:46:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a074e3f2-07bb-3dec-a7ff-9074bfad5d76 | -13.2283 | -61.714001 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c08fddd6-d5d3-370c-bb81-e0c9d1a72925 | -8.526 | -63.8461 | 2026-09-08 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4520c8fd-9ad1-3f10-829f-1ca88ad275fc | -20.6014 | -57.9781 | 2026-09-08 00:46:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ae380254-2027-3176-85c6-a297e049633d | -6.7972 | -58.942902 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f292f46-9115-3119-82a9-103421a1a3eb | -3.5412 | -48.217701 | 2026-09-08 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 688e7ce3-2f90-31bc-abac-a1d64eda37e2 | -13.2361 | -61.702202 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d6eab5d-c030-33a0-80e6-7f6db2306eff | -13.2479 | -61.709801 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1733a16b-8d19-3503-8902-e572d13b3603 | -6.567 | -58.9729 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbb23bf7-cfaa-35c0-8562-95f066f06c40 | -20.426399 | -57.377399 | 2026-09-08 00:46:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fd4b209a-5d48-3cc2-8317-e9be276489e9 | -3.5508 | -48.215302 | 2026-09-08 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8c1159c-23d8-3535-b112-7a153224ed7b | -3.4633 | -59.507801 | 2026-09-08 00:46:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d82e498-47c8-3b5d-9bcd-e0b468e9eb86 | -3.3714 | -59.420601 | 2026-09-08 00:46:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6140e53-abd1-3929-9887-6d30ea8f7581 | -8.8547 | -63.371399 | 2026-09-08 00:46:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 786fc46d-5595-3739-b5ca-a2d6df20d75a | -21.974899 | -56.052502 | 2026-09-08 00:46:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8f9032e9-eea0-3dbe-89be-25031f2a7aa7 | -13.2753 | -61.694 | 2026-09-08 00:46:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 282e449c-7d88-316c-a954-6bd9ad863cff | -3.812 | -55.891701 | 2026-09-08 00:46:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0742443c-55ed-30af-9f4d-d57a78686410 | -3.3812 | -59.4184 | 2026-09-08 00:46:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe32102d-405b-36f3-af36-0f7eb1ac7334 | -1.5965 | -60.137501 | 2026-09-08 00:46:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71f66b8f-cf9c-3bbc-8ad8-94f551c2f922 | -3.0337 | -59.157902 | 2026-09-08 00:46:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14694a94-0e19-32d7-80f1-e7161942cc42 | -1.1946 | -55.743599 | 2026-09-08 00:46:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7fc680f-4156-3449-b394-9a3a0924d62f | -13.2871 | -61.7015 | 2026-09-08 00:46:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 90758e5a-5b8a-3cc2-90a4-4d689b8b9a37 | -5.3665 | -56.019501 | 2026-09-08 00:46:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b09e0e51-b564-3450-a2ae-bb43b4b73431 | -10.769 | -60.776001 | 2026-09-08 00:46:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39668618-15ba-3ae4-808b-37645a289cee | -3.5342 | -48.188999 | 2026-09-08 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc04b258-5918-361d-b0a1-fb17283e1a05 | -3.0602 | -59.274399 | 2026-09-08 00:46:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5544e5d4-6c96-365d-868b-f1cacc208359 | -8.5213 | -63.823898 | 2026-09-08 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be5118d1-3ed1-37db-bdc8-aadc329ec978 | -4.1624 | -59.912102 | 2026-09-08 00:46:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 286e7862-9fcb-3023-b974-0ad803cee218 | -3.7047 | -58.935799 | 2026-09-08 00:46:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0e0aa17-fa6b-34c2-97dd-62285abe6e07 | -13.2381 | -61.711899 | 2026-09-08 00:46:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 243717be-e73e-3a5f-acaf-96f0f4dac492 | 4.1954 | -59.9454 | 2026-09-08 00:46:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3451660f-835e-3491-9321-52110a41b13c | -20.494699 | -57.41 | 2026-09-08 00:46:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d503f14b-912c-3348-9526-f1b3b78fa7ca | -6.6412 | -59.440201 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a985463-f0f2-3c33-b147-23ade8726329 | -6.5044 | -58.285599 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43829511-aa6d-3a18-870f-4eb914fd8d9d | -8.5322 | -63.8604 | 2026-09-08 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 81753174-0283-374c-ba8c-2dda89de694e | -21.9721 | -56.0525 | 2026-09-08 00:50:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 713e57b0-65be-3ffb-9005-3db0cbb5bf99 | -9.7705 | -43.4354 | 2026-09-08 00:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| a78f783c-73bb-39fe-b837-0c5ac69a6554 | -3.5591 | -48.1882 | 2026-09-08 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 177.5 |
| 6decd2d6-7283-3e7e-bf5b-207c88d87894 | -13.2289 | -61.7161 | 2026-09-08 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4d657a22-0972-3d97-9f30-96dbdb54b003 | -3.5406 | -48.1889 | 2026-09-08 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 287.0 |
| 497ebef3-23ad-3e6e-b1ae-a39e23ee2d35 | -13.2479 | -61.7148 | 2026-09-08 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |


[Clique aqui para ver as próximas entradas](README5.md)
