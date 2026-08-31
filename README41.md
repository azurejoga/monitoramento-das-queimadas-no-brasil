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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a6f9eab-5a76-310f-9099-6e1368535f60 | -5.88717 | -57.75364 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee60534a-b290-384a-848c-349677a91430 | -7.49975 | -55.32238 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfcf5612-902e-3051-bc52-4ff48b5d0826 | -7.52798 | -55.33764 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b6597a1d-29a0-3ec1-b960-a768c2bb2ea7 | -1.59276 | -54.4066 | 2026-08-31 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5218cd9e-5df2-3b91-80f1-c714a97a556a | -3.86877 | -49.10703 | 2026-08-31 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83d865aa-0050-3701-8e8c-bb912c91d6c1 | -7.29185 | -52.36504 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00c22d30-9ca3-37c0-9cab-942e5a656663 | -4.15774 | -60.69036 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35a4e415-521b-3beb-9943-4b6703c47ebd | -6.78311 | -55.67857 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 922d0ba9-3b7b-32b6-90ba-3f27c854c0bc | -7.9797 | -44.28016 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8773a159-dbe0-3974-b81e-5d8a9a5cad17 | -7.34038 | -55.14684 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c19bb1c-9bf9-3e09-aaeb-0b0cb4e59906 | -6.60521 | -58.60027 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 04ea9622-0549-318f-8701-0f48ed2b3126 | -7.14407 | -46.17165 | 2026-08-31 04:57:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b42879b-eb71-30a2-a2f1-6caa59e2ad0c | -6.77259 | -59.47117 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72b7368a-b5cf-36d5-a8fc-c01190ab669a | -6.42664 | -55.52723 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88e60225-f6be-3a22-83c2-d31d1d120c13 | -6.15579 | -57.7841 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eadf7493-1984-340a-8cf3-09a97ea16ba8 | -6.86447 | -59.47207 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b647a479-bbc9-311a-b00a-2665d91436e5 | -3.93511 | -59.32727 | 2026-08-31 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dbb99be-9861-30d0-8445-9b6adc22a49a | -6.41994 | -55.52618 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3a27faf-0a18-3d23-bac7-6374b8ca6c41 | -3.65243 | -54.84748 | 2026-08-31 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 143393f4-b339-3421-b0dd-0af5b44d9d75 | -3.90312 | -55.87897 | 2026-08-31 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f48c88ce-6d72-3137-b792-b0aad5107e82 | -7.3487 | -55.18034 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34cc0a13-5107-327e-9bd0-cc9b300f4d59 | -7.52743 | -55.34114 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f69f3b15-c0be-3a78-a30c-7c12b3aa5d6b | -4.96774 | -55.84934 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca9bfa5e-72aa-315f-8cca-8c929c4fe133 | -7.35148 | -55.18431 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3590266-0a3f-3283-afe5-cd0abf93bb43 | -5.95953 | -57.67615 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fc6555e-95fe-3291-8b41-c68bbe34a89e | -5.94507 | -57.69582 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e560104f-9fbf-31d9-baeb-d4c27ab19242 | -7.25499 | -60.63207 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 611cf9d3-0e25-3abf-af2b-df1dade8a87a | -6.91944 | -55.72247 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b07c2611-b014-34c3-a0be-84dcfd450d15 | -3.96845 | -60.02888 | 2026-08-31 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa84c133-74af-3e84-9c2d-db57fad2d58e | -6.42329 | -55.5267 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaeb0b1e-ddd6-3b4d-b94f-93d5fdf53870 | -5.24422 | -55.90014 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b3b423f6-e6aa-3113-bc9c-159286a6bc96 | -6.87082 | -56.57468 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25696bc0-db99-3b28-9fc0-2d5d98b70467 | -4.27065 | -56.12915 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2b7e5b3-59b6-3b57-9cb9-80acb41acf6c | -6.25814 | -53.64831 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 379e17f1-4c91-3a6d-a3eb-ded7fe61bc8b | -3.48774 | -54.66288 | 2026-08-31 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f8b62a7-c8fd-300c-8eb6-1f7e9c697738 | -6.26602 | -55.42174 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9937f80f-b9eb-3435-b11b-cc76b936785e | -6.93748 | -55.63044 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6f6230c1-2a7f-3381-b8ac-50edbefcb98e | -6.09796 | -57.70115 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87c53b8c-2d9f-3207-b84f-d86028746d32 | -8.3839 | -44.99171 | 2026-08-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74cf15bd-0746-3d47-b9b0-d25564d9630c | -8.22022 | -54.93776 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99d45e69-a955-3be5-bf3c-cff7ed48812d | -6.25955 | -55.42392 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4749078-1cb3-3ed4-acb1-32dd3018d75c | -4.96434 | -55.8488 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15bb6d61-55b7-31fa-baf6-c7e3540ed68a | -6.22624 | -55.93039 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b14c3759-ffc7-3101-ba9c-8bf59c718024 | -8.21198 | -54.94712 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 895922fc-f3af-38fb-bb97-b44d41058f64 | -5.40431 | -45.88766 | 2026-08-31 04:57:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e2f1492-e592-3875-95c0-ca0f56f59c7f | -7.97871 | -44.28803 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a72fd21f-3bf7-3984-a69d-ed582479238e | 0.14099 | -60.40171 | 2026-08-31 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a26a760-75e2-3905-939e-5f62159cd36c | -6.22165 | -55.42524 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e52db2fc-777d-3f99-8451-65ce16a69c73 | -3.93927 | -59.32794 | 2026-08-31 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ac3fd27-3f0c-3577-ba2b-90b94b323932 | -5.25162 | -55.89753 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f1c06c2-f2d5-3bf1-80a6-4b664a07fe50 | -7.31087 | -60.59051 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2fc4b07-2f2a-349c-ab25-65cf789db8ed | -5.94281 | -57.68664 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dd0503a2-d6e5-3927-929f-34232238041e | -3.62512 | -60.5512 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1249131-f5d6-3d5f-ac77-d43aacd52a77 | -6.8679 | -59.47626 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d689fa52-660d-367c-9e4b-cdbc61532b5f | -7.52964 | -55.32714 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62884496-0a8a-3117-b78a-39a66d582e47 | -4.85068 | -55.83466 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0140dcbf-6827-32f2-9c26-46ea8e5599de | -5.31762 | -55.85538 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9fe915b-9aa3-3db1-b372-9004dffb6d60 | -7.34647 | -55.15135 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09e8ac85-303b-3e6c-9a8c-8260549bcc52 | -7.2924 | -52.36133 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97713116-93df-360c-b94f-2f4124e7d5bb | -7.09646 | -45.77505 | 2026-08-31 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c51331d0-3fef-399c-ba3b-b0159228fc64 | -8.75175 | -46.44904 | 2026-08-31 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 062e2560-e63c-3345-928d-ac4ba777688c | -6.91157 | -59.48701 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3adb49d7-6ce0-3a8f-81e6-e2c8dc38a4a1 | -3.62892 | -60.55653 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e3edee7c-f748-324a-8eff-f68e84defa88 | -3.86408 | -49.11137 | 2026-08-31 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 07584108-e2d6-3216-9b45-2863d4bc69f4 | -6.60674 | -58.59082 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c34fb7ab-fa8e-38e3-9245-5c2556219986 | -7.94777 | -52.45384 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e081d325-cb13-315f-bcc1-062453c6d200 | -6.92615 | -55.72353 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ce5b98c-1b2a-369c-8fe6-2f5aaa813893 | -4.75967 | -50.66533 | 2026-08-31 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a99541a-4798-32c2-9aea-c63d9f48b8dc | -7.97705 | -44.30117 | 2026-08-31 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc9af71e-c6b9-3de5-81a0-bc3f476576d2 | -4.96035 | -55.85193 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddfe5720-a73f-3395-9da1-e4d05aa22cf9 | -6.93636 | -55.63755 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0a4bf3de-d838-3dcf-84c8-b3cbb62a198e | -3.41121 | -50.12718 | 2026-08-31 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 95a271fc-145f-33a7-a2b3-a972131514b1 | -5.87561 | -57.77876 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c1398b9e-a8d9-338c-ad45-9b656af011e7 | -8.01018 | -51.79266 | 2026-08-31 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1f411e7-ad1b-3d60-b101-8d4f7a9b8848 | -6.00128 | -57.8321 | 2026-08-31 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3b475b1-ded2-3bdb-97df-fa1e8ea752ac | -3.62588 | -60.54659 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d40973d-91cb-3219-804d-939ecd60002d | -4.43013 | -55.22705 | 2026-08-31 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6e69f55-5d7b-3ded-8248-53d9b4df881e | -7.52355 | -55.32257 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e262499-c977-33d9-a183-02d9198538e2 | -5.48357 | -57.14107 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25ab04a8-1a01-354b-83e6-dfd10e289ce9 | -8.39545 | -44.99001 | 2026-08-31 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 255b3df5-afe5-3e94-a8c5-f85eb908db6d | -3.63346 | -60.5573 | 2026-08-31 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0dfe0faf-ad44-3e5c-a572-28305e4a4582 | -5.31024 | -55.85795 | 2026-08-31 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e8f5b4c-5685-3add-9d0f-8c8893f1f362 | -6.60751 | -58.61031 | 2026-08-31 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec553913-df79-34f9-a057-5eb664cbbe2a | -6.26289 | -55.42442 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3dcf3387-b0be-3e00-aa62-49a70f054d3b | -5.58724 | -42.32496 | 2026-08-31 04:57:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 88687016-8bed-373c-9186-6a2eae14c419 | -4.09262 | -54.10423 | 2026-08-31 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 742f5e5e-a0df-3cc3-a95e-e1fbf240af57 | -8.14396 | -45.51845 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aeffbcfa-dbd4-3b8d-b4b8-39405ae7da1f | -7.33594 | -60.59906 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b84b1521-4d6a-3507-8c46-b51f04fdcde2 | -5.48224 | -57.14927 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ea25ae8-7435-3274-849f-a6e7b9bc3781 | -7.06303 | -52.72082 | 2026-08-31 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c19669ba-3481-369a-8319-9d70d1a5abc7 | -8.21637 | -54.9407 | 2026-08-31 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b9e8815-e774-35e2-bfb1-705eba14d5ac | -7.52632 | -55.32661 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a6d59c2-ce63-3dee-b546-d96a4d81e0c7 | -6.1279 | -55.6259 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c353ffb-d679-34b8-a6b9-14eb7214087d | -5.62024 | -60.21135 | 2026-08-31 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb4bcf3a-2258-313c-83f9-81254212ef8a | -6.72191 | -56.34362 | 2026-08-31 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7d274fb-9bb3-3a73-a148-81787c2a0bfe | -4.15165 | -60.69892 | 2026-08-31 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eddc259b-d1cd-3d5d-bf70-422a0279aa20 | -7.51747 | -55.33953 | 2026-08-31 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91c06670-2568-379b-8dfa-13f0e74b1857 | -8.15057 | -45.47008 | 2026-08-31 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 912de18d-7787-3c5c-88e4-7af262da4639 | -7.30802 | -60.58133 | 2026-08-31 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 69c899ef-c08c-371a-8e3c-e8f6d6975156 | -3.86802 | -49.10938 | 2026-08-31 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |


[Clique aqui para ver as próximas entradas](README42.md)
