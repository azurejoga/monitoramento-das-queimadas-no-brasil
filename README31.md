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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 110bc134-3cb3-3902-a13b-6f6c8f958125 | -11.71778 | -50.11757 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 912a94a8-884a-320b-881f-5e312d77f564 | -3.82997 | -47.74924 | 2025-08-12 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 72f57416-06d6-3043-b61d-84b4f8d9bcf4 | -9.3829 | -61.52443 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 583c63d7-05ce-3255-83df-a49a4deec425 | -8.93401 | -60.72556 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 1a41b883-7cd0-3b40-889c-d69b0d5b3a44 | -11.72968 | -50.10238 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e8a245b-5b12-39cc-87c3-015a12523411 | -13.33616 | -50.25146 | 2025-08-12 05:25:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e16f8f2b-21c8-36c7-ad06-38d27590ba89 | -12.95137 | -56.22779 | 2025-08-12 05:25:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74ff5397-97c5-3a39-a3fe-537984db0ede | -7.06875 | -59.21089 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8966bc59-ecbf-34d2-9bce-31f4d461a70f | -10.34474 | -50.82325 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e55e5d5-cce5-306c-8a1c-50dfe41ffb95 | -9.01038 | -59.53648 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58848977-95e2-3749-9d07-e4ac7b2f43ff | -6.96801 | -59.27671 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1cce6122-9459-37d2-b7c1-1f1da7de3c6e | -9.18944 | -59.66494 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce2ddbfd-147e-3813-a8b8-2a576a8c653f | -9.7092 | -49.47668 | 2025-08-12 05:25:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 80ef8ea3-198f-340a-a2db-8a58d7ce1ae1 | -6.97138 | -59.27723 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 679ff2ae-368a-3927-ba66-82611a41c1f6 | -9.17591 | -59.66282 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c89cab88-d6b8-3d79-a9a7-fb68b85b4092 | -8.56658 | -54.67883 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c865b2b-b92a-3d03-b36f-dce1c80dceac | -9.17984 | -59.65971 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28e4bdc4-d5eb-36b8-b707-6ffc2626319a | -8.57921 | -54.71543 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5eaca3af-03cd-3709-b2f4-613f0211be38 | -11.66517 | -50.13577 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3013013b-14cc-3938-ac3d-8d8bcdd4ff83 | -7.06239 | -59.20306 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d846e91-e056-30f5-9d30-11b84fa3c659 | -7.06986 | -59.20369 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a319a083-b27f-315c-a8db-440ce08a8c3e | -10.35109 | -50.82 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c98662c-acda-369f-8715-cae8c4a599f7 | -10.96793 | -49.56708 | 2025-08-12 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88e1c87f-4d12-3bd2-a5e0-42436c704801 | -8.57729 | -54.69774 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26596ed9-794f-322d-b965-58c69f03bbc3 | -9.37513 | -61.53037 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58b9004e-cdb9-3c8f-9097-8d4af13c9744 | -7.08505 | -59.19495 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6afebaa6-accb-350b-9531-e20f27fc15ef | -11.73535 | -50.10808 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e8dd0bd-770c-3edc-b6df-ebcbf0a45106 | -9.37735 | -61.53791 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a3f3066-b253-3029-b390-84087d300fb8 | -8.92575 | -60.75647 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6018a845-ecaa-3793-9ff7-189d4fc0e7f9 | -11.7081 | -51.59989 | 2025-08-12 05:25:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64d48abc-30bd-3eec-bf87-1fa17cbf10e7 | -10.96648 | -49.56881 | 2025-08-12 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bea91da-f744-35f3-8b28-3222e7fecfb2 | -8.93346 | -60.72906 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 59bf32dd-bc09-3c42-98f8-80cfc75babe0 | -7.06577 | -59.20356 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71d9f791-8526-31ae-be07-64748a131b4e | -7.13034 | -60.12907 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7de5dfed-5026-3577-8502-2f0953f99ad0 | -11.68777 | -51.60192 | 2025-08-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5754f61f-5da0-3ce6-8afd-0d3459bd8d0f | -6.9669 | -59.28388 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1644a9b3-960a-3a48-a26f-428636fb8d9c | -11.38966 | -56.21282 | 2025-08-12 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b37722d-0aa7-340b-80ea-2daf30ab3a6e | -8.57045 | -54.71425 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bb9bf888-2b6a-327c-9131-5384040e1ca5 | -10.75901 | -48.79067 | 2025-08-12 05:25:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5b4b81d7-6fc9-3bab-a8f2-41bd5323c3dc | -13.06856 | -56.84864 | 2025-08-12 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef7f547c-7da3-305b-b6da-6959b9734694 | -9.38844 | -61.53251 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| df6131af-ae85-302c-9a90-ae2bf3ef3693 | -9.82888 | -60.75926 | 2025-08-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec42c1b2-57e9-386f-b605-04e1d1f0e374 | -8.92079 | -60.76637 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 555fea6b-cfad-362a-a98f-eaf62489d710 | -8.56414 | -54.69593 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a41ea033-45fa-3014-a98c-2c55ca915521 | -9.47451 | -57.84026 | 2025-08-12 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1b017259-57cb-3a9e-ac3d-9894b85ecd00 | -8.93459 | -60.74356 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58b12dd9-537c-3b40-9efc-f59b6997cc9b | -9.71245 | -49.48209 | 2025-08-12 05:25:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 057de73d-2e3e-37da-8e64-f2a59bb8a461 | -10.47355 | -61.32586 | 2025-08-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1374d9f6-394a-30b0-961e-f4339a0fba94 | -7.20069 | -59.84656 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9523eee-4ba5-3c1d-a939-da5b4711a5da | -9.18999 | -59.6613 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3e34d4a-51e4-3e17-a6ff-f5f49b295c31 | -11.68263 | -51.59719 | 2025-08-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d76987d5-2322-36a2-a131-c7ef3f7cd5d7 | -8.57422 | -54.71911 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f013abf4-e42a-32e6-ab62-c8186477a3d9 | -11.66574 | -50.13088 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac002f36-07de-38af-b81d-37835719875c | -13.35561 | -50.24867 | 2025-08-12 05:25:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff4a017f-baf7-36de-a694-6a03506d0068 | -7.12647 | -60.13203 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44f44eb9-32ff-3570-b31b-4ec200b7546c | -6.69231 | -59.13862 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96fe95b8-767e-3039-b22d-07b347794950 | -10.32088 | -54.15633 | 2025-08-12 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3d7cbca-200a-3ab8-8dec-086bc5df7dd2 | -13.065 | -56.84444 | 2025-08-12 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76951828-c953-3832-a59b-633824425b42 | -9.71488 | -49.48268 | 2025-08-12 05:25:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 559f0126-730a-327e-bc63-f00f70b5a711 | -6.97083 | -59.28082 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1561ce02-c456-302e-9e81-72d06e856c70 | -9.71549 | -49.47769 | 2025-08-12 05:25:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 303cbb60-eb72-3331-be1c-904c781886c1 | -11.67748 | -51.59246 | 2025-08-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 660e3635-c6b9-3f39-a8c8-ed4d5d77dd77 | -9.63841 | -67.51659 | 2025-08-12 05:25:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f3bb48b-7505-345f-aa10-245b51f45df2 | -3.4296 | -49.04418 | 2025-08-12 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ccb9a76-980d-3651-b338-30ff34ac0c4e | -7.13822 | -59.64159 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82c6ad6a-624c-39b6-b4bf-a9da3c5f3555 | -11.3902 | -56.20909 | 2025-08-12 05:25:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 954d2760-2ba6-3fde-9788-f25cd56be52e | -7.06521 | -59.20716 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a34adde8-119c-3f9e-b244-8e39db5159f9 | -8.92908 | -60.75699 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5430a5d8-1bb9-35da-876f-351f6e336b1d | -9.38622 | -61.52497 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08e9fc41-f3ea-310c-ac91-c504dea2c29d | -8.93627 | -60.75455 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d97ae16b-6b28-3c79-a53d-4aa36ed0e907 | -9.71939 | -49.47797 | 2025-08-12 05:25:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40af7d08-13e9-3f36-9f42-9b340f02cdd1 | -9.19393 | -59.65821 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6616d8b-240c-3f55-b02e-725ac40129a4 | -8.56171 | -54.71292 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 663635e0-89c8-3b4f-bb28-b097f966c552 | -7.13199 | -60.11861 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8068923a-b21e-3ed9-89d7-b4e2a23855ee | -9.18323 | -59.66026 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c1d39a1-6191-3929-9b12-20dec970e150 | -7.07379 | -59.2006 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27b86349-07f0-390d-939a-7dd7eaa1bc57 | -6.97027 | -59.28441 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c83c79e8-597f-32a0-b320-77f4021b8b9a | -7.09411 | -60.03403 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85dbe729-d73e-3548-9015-da9b24ffccca | -8.93679 | -60.72958 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 39607ec6-2624-3089-996d-7af6ab9976a8 | -9.92201 | -60.48199 | 2025-08-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e469505-9f09-3c95-b609-fb16fe715fca | -10.04479 | -64.8998 | 2025-08-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54abd7d2-1022-3f17-8883-c6bad88598e7 | -8.57606 | -54.70628 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9cc5309-3ced-3b56-a796-a46069647923 | -9.53366 | -66.14356 | 2025-08-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 403f7773-fe37-3333-a7ac-ae163efc9d4f | -10.21302 | -55.33152 | 2025-08-12 05:25:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8ac1bf3-225e-3bd5-9a02-2e467978ac9e | -9.3779 | -61.53442 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85581eec-bbbe-3a0b-825c-5b137789dbd0 | -7.14426 | -60.12087 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e32aa4a9-e500-3288-bf2f-66b0056fc81f | -8.56984 | -54.71849 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e618b0df-f2d4-3da4-99d7-f53c39db7668 | -7.06593 | -59.20678 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 541d4552-3622-3eb8-8679-9199bd3fb038 | -7.14039 | -60.12383 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 669d09f9-bfaf-3afa-8356-671e5715c8f6 | -9.03477 | -59.75931 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 034d5b43-7064-35be-8803-45b53ba326f2 | -13.34353 | -50.24247 | 2025-08-12 05:25:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 73db72b2-70e9-3947-81f1-9f8176149869 | -7.07435 | -59.197 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66fe2487-cf79-3c93-81cb-3b7bd2880728 | -9.37181 | -61.52983 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2ce3d47-2849-38f1-a5cf-7d4687c0950a | -8.57483 | -54.71484 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f33afeaa-ff82-3ea0-960a-0827df8b1fa5 | -9.19055 | -59.65769 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d86f8153-9126-3775-9858-82c741e1ebb2 | -8.56547 | -54.71784 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3030a75f-b0af-35af-bb24-e823d636c4c4 | -9.17253 | -59.66227 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91b81bdf-84e9-3bce-925b-787f06e87bcc | -7.13809 | -60.12315 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9fbcbbeb-e3ae-33d3-87d4-fcf373fffb67 | -13.04475 | -56.84144 | 2025-08-12 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b54ecb5-8177-3afd-a073-8d98995762d0 | -10.31557 | -54.16051 | 2025-08-12 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README32.md)
