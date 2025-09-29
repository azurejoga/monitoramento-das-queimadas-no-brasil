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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e035d2d6-faf2-3c5d-a93e-15b17b46ce2d | -7.2214 | -44.783 | 2025-09-29 02:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 156.5 |
| f233f45a-77cd-3e0d-9bdb-ea01d3b400e9 | -4.7159 | -41.9736 | 2025-09-29 02:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 1344bf35-a24d-31cd-82e2-ed25a2ad831d | -15.2893 | -49.5035 | 2025-09-29 02:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 34377775-05a7-3e8f-bb64-96a99ad0adf0 | -8.2851 | -45.4999 | 2025-09-29 02:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 00e4c3c1-6bd6-3603-8c24-d61c2b32ef12 | -14.553 | -48.4237 | 2025-09-29 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 6535eb19-cb6c-3cb0-9ffb-13f6d1fc6f21 | -11.8294 | -51.7725 | 2025-09-29 02:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 0887a20a-c366-36b7-8bc3-3c3c0dc61d68 | -2.5773 | -48.3931 | 2025-09-29 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f3f33419-aa74-3013-b3cf-a4f13e3eefc4 | -3.1013 | -47.0082 | 2025-09-29 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 9f5669a1-441e-36e8-a591-3e50b28fc76f | -3.1012 | -47.0301 | 2025-09-29 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| cefc80b1-56b7-3c7b-a75d-788ce0345368 | -14.5336 | -48.4268 | 2025-09-29 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 1f004c7f-07ef-318b-aab9-1ed246e19eaf | -11.8288 | -51.8148 | 2025-09-29 02:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0e153190-317e-318f-9b18-88f561449d96 | -11.8104 | -51.7746 | 2025-09-29 02:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| df41b0b2-e845-3865-be0a-8bf87ceb5221 | -11.5204 | -44.8497 | 2025-09-29 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 82132111-d143-3aec-8f8c-7cccd81c469d | -0.1012 | -51.2738 | 2025-09-29 02:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 94e8692d-fe94-32b9-b403-752809a3cb34 | -11.8101 | -51.7957 | 2025-09-29 02:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| a51afaed-e02a-3cc7-a599-e6b50b5fd074 | -17.0938 | -48.5699 | 2025-09-29 02:20:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 910ac233-29a3-33e4-8c2e-018c303da8ea | -11.8291 | -51.7937 | 2025-09-29 02:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 200.1 |
| 6a59a56d-a47f-3733-b7cc-5d979ffc0627 | -11.925 | -48.0273 | 2025-09-29 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9ef123f7-4a9d-34cf-997a-2c9d4f48dcf5 | -7.2402 | -44.7812 | 2025-09-29 02:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| e8d6b7e8-85c4-38a2-81de-189d69841cd7 | -11.5012 | -44.8525 | 2025-09-29 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 3ae64c1d-228d-337f-aefd-a59e8ddc361e | -3.1012 | -47.0301 | 2025-09-29 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1ed4c93f-d394-3795-8e24-af2ed173b76b | -2.5773 | -48.3931 | 2025-09-29 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 627933df-fc83-3bda-9754-51cb7960778d | -7.2214 | -44.783 | 2025-09-29 02:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 1c377a14-84c4-3b67-aba9-c492423dba67 | -15.2893 | -49.5035 | 2025-09-29 02:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 53cdefa5-6367-3a0b-af1d-aa3a243d38ec | -7.2402 | -44.7812 | 2025-09-29 02:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| f3eb313e-f351-3b79-ac1e-fee8872c14a1 | -20.0491 | -41.3251 | 2025-09-29 02:30:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| d737b050-a120-324a-b5cd-dfade4294b33 | -11.8101 | -51.7957 | 2025-09-29 02:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 1b89d324-7b5c-37ad-89b3-750dc50b52b4 | -4.7159 | -41.9736 | 2025-09-29 02:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 7d42acaf-7cd9-37de-b739-e56413e25630 | -20.3715 | -51.2111 | 2025-09-29 02:30:00 | GOES-19 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 3eea462b-a1f3-3087-a598-11717c530a41 | -8.2662 | -45.5018 | 2025-09-29 02:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 28aad1ce-503d-3653-a3e7-c051b58f3ac0 | -11.8294 | -51.7725 | 2025-09-29 02:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2d3260e5-c3af-3d2a-a65f-f1c29882ea8d | -14.5526 | -48.4461 | 2025-09-29 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| a6a836dc-e895-30b4-9ad5-5e7e31ae1ebb | -11.3634 | -45.0801 | 2025-09-29 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 52c19d0b-14b2-34de-aae9-952fd530bd35 | -2.5772 | -48.4146 | 2025-09-29 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 32220b8c-e237-324d-a044-d44bc0201dbd | -8.2851 | -45.4999 | 2025-09-29 02:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8ec8d068-efa4-37f9-b955-ed4dd20e526a | -14.5336 | -48.4268 | 2025-09-29 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| a1589a2e-a822-39fe-8338-f74058bb7ec2 | -3.1013 | -47.0082 | 2025-09-29 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 9b6de2ee-6ead-325d-8dbe-f853257a94b1 | -11.8291 | -51.7937 | 2025-09-29 02:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 140.4 |
| b5356e57-474d-3adb-9d87-5e5b81c295e7 | -20.0698 | -41.3189 | 2025-09-29 02:30:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| c71b9be5-5e54-3383-866c-a8bf866c9527 | -4.7157 | -41.9974 | 2025-09-29 02:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 983d2a29-a92b-37d5-845c-cf6e8d875cbb | -14.553 | -48.4237 | 2025-09-29 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d7f17ec0-c16a-3814-aa36-ed3de8906375 | -17.0938 | -48.5699 | 2025-09-29 02:30:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| bf79ba41-f904-3c8d-80cc-28449449a9aa | -0.1012 | -51.2738 | 2025-09-29 02:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 20.6 |
| cb362090-b429-362e-945c-99c55f4875e0 | -11.8104 | -51.7746 | 2025-09-29 02:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 040c1d30-7112-357d-b211-21d1e8e8a9c7 | -11.9442 | -48.0248 | 2025-09-29 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 64117af3-747d-3a2a-9a56-cafab7704fad | -8.2854 | -45.4772 | 2025-09-29 02:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 125c5aab-a835-33df-9e5f-dc658d99f055 | -11.8482 | -51.7916 | 2025-09-29 02:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 9296e557-b0a2-3b19-b234-6b1b50c28c8e | -11.8288 | -51.8148 | 2025-09-29 02:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| be47f351-1321-328e-a918-df37996ae99e | -17.0938 | -48.5699 | 2025-09-29 02:40:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 88d12600-ff65-3d2c-b779-deca175465db | -4.7157 | -41.9974 | 2025-09-29 02:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| a44447dc-a16e-34dc-8a7c-ae1f42d48e09 | -11.8291 | -51.7937 | 2025-09-29 02:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 277.2 |
| 7e82cf68-1afe-3d9c-9f5e-4dbabacf9559 | -11.8294 | -51.7725 | 2025-09-29 02:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 99bffe1b-d852-35b3-aec5-d0168de583f8 | -8.2851 | -45.4999 | 2025-09-29 02:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1b04fbe0-4648-3763-a553-d7d0bbd2c5d8 | -7.2214 | -44.783 | 2025-09-29 02:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 74483c6d-d060-3c6a-bb5d-6bdcdfba5b85 | -3.1013 | -47.0082 | 2025-09-29 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 479a9981-c32c-3a0c-911e-e125f326c80f | -14.5336 | -48.4268 | 2025-09-29 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 7a688d80-56cd-30ad-bfdd-2a59ecce4d64 | -2.5772 | -48.4146 | 2025-09-29 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1bb1fb9e-76a0-3623-95a3-c8a05ce4db3a | -20.0698 | -41.3189 | 2025-09-29 02:40:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 116.6 |
| a050c2d1-60bf-37d9-9e99-d78cc45f630b | -7.2211 | -44.8058 | 2025-09-29 02:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2a405ff1-37aa-3624-b28d-5b8837c97821 | -8.0034 | -47.0497 | 2025-09-29 02:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 4ff0470e-5855-3deb-bb86-815937a35345 | -14.553 | -48.4237 | 2025-09-29 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9b8623ab-cb34-36e8-bd67-fda3a63ad87f | -20.0491 | -41.3251 | 2025-09-29 02:40:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.5 |
| 9fe3bbfd-7cee-3704-9ae0-e83f9ffb7fd6 | -8.2662 | -45.5018 | 2025-09-29 02:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d720fba4-8ec5-3333-8802-aeeee760e019 | -7.2402 | -44.7812 | 2025-09-29 02:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4d62b0b4-097d-3965-a240-22dba046de78 | -20.0689 | -41.3449 | 2025-09-29 02:40:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| 3dff72e2-ca4e-3965-a1e8-c7e933041c25 | -15.2888 | -49.5256 | 2025-09-29 02:40:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 8ae71da3-d503-3a5a-bc8d-741f2eacf108 | -11.8101 | -51.7957 | 2025-09-29 02:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4a433f27-0ad8-3a7a-9910-22cad5040f97 | -8.2854 | -45.4772 | 2025-09-29 02:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 84ae1838-4116-35e2-a21c-00a28b867ba3 | -4.7159 | -41.9736 | 2025-09-29 02:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 26587788-3a98-3ea1-8fe3-19223b567668 | -20.0482 | -41.351 | 2025-09-29 02:40:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.3 |
| 0e795ebf-e2cf-3711-9f09-7cb4453869b7 | -2.5957 | -48.4141 | 2025-09-29 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d7edd79e-519c-3964-92e5-a0ff21cf49e6 | -3.1012 | -47.0301 | 2025-09-29 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c58417d2-c09e-3cc1-9130-466e35bbe13f | -15.2893 | -49.5035 | 2025-09-29 02:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 140.3 |
| ba374c42-fc58-3b25-96c6-ed1010db40eb | -13.3796 | -48.1577 | 2025-09-29 02:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 6e34d834-62aa-30d2-bce2-e1b4e88efb28 | -3.1013 | -47.0082 | 2025-09-29 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| d928046b-f062-3e0a-a19e-846c6bde47b2 | -14.5336 | -48.4268 | 2025-09-29 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| d4bfc45b-dce4-3a10-ac0f-16f888bb2c27 | -8.2854 | -45.4772 | 2025-09-29 02:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 7d9962a4-137e-3715-88da-06145f831a61 | -3.1012 | -47.0301 | 2025-09-29 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 5c8b1f8e-7f88-3721-9eea-7d54d37ab610 | -7.2214 | -44.783 | 2025-09-29 02:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 3f1cf446-a89a-361f-a8b9-39399fd94c13 | -8.2851 | -45.4999 | 2025-09-29 02:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 62f5288b-3146-3454-99e4-7d22fd1adc8e | -12.3013 | -44.1008 | 2025-09-29 02:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0f364dba-5878-354c-b45a-ce44c8fe5cd4 | -12.2825 | -44.0804 | 2025-09-29 02:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| dec7f0b0-379a-3d55-942d-0fbc0e5650ec | -2.5773 | -48.3931 | 2025-09-29 02:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 47a7c9a7-1f35-3ccb-b7ac-45e09234f50d | -20.0482 | -41.351 | 2025-09-29 02:50:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 04fb357c-e78e-309d-8896-9969b48644bf | -15.2893 | -49.5035 | 2025-09-29 02:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 127ce813-4aec-36ec-a513-40c53ef470e1 | -7.2402 | -44.7812 | 2025-09-29 02:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| e2a1630b-662a-3b5f-94df-69403dd42a1f | -2.5772 | -48.4146 | 2025-09-29 02:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| df873229-b2ed-386f-b2de-0e33de189b59 | -20.0698 | -41.3189 | 2025-09-29 02:50:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 120.7 |
| b77cd5cb-7d22-372a-be39-b08c0b2bba86 | -17.0938 | -48.5699 | 2025-09-29 02:50:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 78d300d0-58b2-3dc6-ae8e-e47e1361638e | -12.282 | -44.1039 | 2025-09-29 02:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 0e1b4aec-7fc6-36c4-b1dc-e7175491e227 | -11.925 | -48.0273 | 2025-09-29 02:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7246c3d7-fbe7-3e9a-a5a3-d46021e39fbd | -20.0689 | -41.3449 | 2025-09-29 02:50:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| 8456d870-1dcc-3090-ae39-a60738fe5c22 | -20.0491 | -41.3251 | 2025-09-29 02:50:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 143.2 |
| df7eb7ed-f63f-3fe9-9865-2fafd39d22aa | -3.1013 | -47.0082 | 2025-09-29 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 343faab8-038c-3ab7-bc74-b02ea5043cc0 | -5.1885 | -43.7495 | 2025-09-29 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| e2b6b0a4-50ba-394b-896b-3ca00251b976 | -2.5772 | -48.4146 | 2025-09-29 03:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| aa1861b3-d7cd-3e8f-ba0d-38706428353b | -8.2851 | -45.4999 | 2025-09-29 03:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5707c2c6-a310-35d9-9d19-3f28cef2f748 | -7.2402 | -44.7812 | 2025-09-29 03:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 75b2198a-a73b-30af-b12e-7a6360b77339 | -11.4237 | -44.9099 | 2025-09-29 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 7a507ab8-237c-3525-b068-f5242b672349 | -20.0698 | -41.3189 | 2025-09-29 03:00:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 99.2 |


[Clique aqui para ver as próximas entradas](README6.md)
