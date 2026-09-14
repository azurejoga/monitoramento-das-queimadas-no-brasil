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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14cd9a35-f1dd-3034-bd17-1e9982b02e91 | -13.3055 | -51.3235 | 2026-09-14 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 2b232993-0dec-33a6-8df1-1e90d83ae2a0 | -5.1255 | -55.955 | 2026-09-14 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 2b68f337-27df-3acf-a353-62578cd5b0da | -2.9025 | -50.4004 | 2026-09-14 12:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| bb042de0-3133-3682-bb25-85edbb852190 | -13.4458 | -43.8128 | 2026-09-14 12:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 4302e2dd-3b7b-325f-ad1d-a13e7b559007 | -13.4264 | -43.8163 | 2026-09-14 12:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a5e5a938-29ba-33cf-8703-1f79ccb26913 | -6.1109 | -57.684 | 2026-09-14 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 6ad3f7b3-4d41-388a-b0ed-311c50361044 | -10.6641 | -54.1491 | 2026-09-14 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| fda418ab-7a21-3744-89e8-38c8cfa0c41f | -9.3763 | -50.1139 | 2026-09-14 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 9292565a-33f1-3889-a021-12900f06c579 | -13.2863 | -51.326 | 2026-09-14 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 92526ca8-296a-3dd7-b3ab-3129274322c7 | -3.8042 | -44.1072 | 2026-09-14 12:50:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 010afbd5-742a-3dcf-a471-508249745891 | -2.9208 | -50.4418 | 2026-09-14 12:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a1fc8c0e-cac6-3e2c-a9ea-25a1e919e871 | -6.1111 | -57.6645 | 2026-09-14 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 009a66d8-9d26-33b9-8286-939d6b008465 | -6.6767 | -58.7105 | 2026-09-14 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 4dc68eb7-cfaf-3fb2-86f9-c222e3b34c24 | -9.3758 | -50.1565 | 2026-09-14 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| c5b85e49-dbd4-38ba-a472-e16ac0fba636 | -10.6829 | -54.1475 | 2026-09-14 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 82c17d0f-bc8a-3d28-a811-59c1abae69b5 | -2.9024 | -50.4423 | 2026-09-14 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 87ca28f4-7f22-368b-9b71-e0dae6f246d8 | -5.1255 | -55.955 | 2026-09-14 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| d1f86316-16be-32c4-87dd-fd268fdaf6a8 | -3.4089 | -58.2142 | 2026-09-14 13:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| cc20045b-de84-3c5e-8fc6-2c389bf1acf9 | -2.9208 | -50.4418 | 2026-09-14 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2a877467-3d47-3c93-b8d9-d6e906b81f3b | -8.6194 | -44.4357 | 2026-09-14 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 41064ae8-b338-39d5-aeae-25ce56603811 | -14.205 | -47.4039 | 2026-09-14 13:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 5dd6ea1e-5833-3a41-b1ae-0542f8df8d88 | -9.3755 | -50.1779 | 2026-09-14 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 351c5746-ab7e-345e-9a20-88357830356b | -7.1048 | -41.7971 | 2026-09-14 13:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 7fe532e0-449e-3610-9bbc-13db5531286c | -9.4325 | -50.1299 | 2026-09-14 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 8bec514a-4f74-3e56-b4a3-4108b42095ba | -2.9579 | -50.3988 | 2026-09-14 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ad825034-08be-3497-957a-93ed14742c48 | -10.6641 | -54.1491 | 2026-09-14 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 042e8a6b-7ce8-350d-8906-db1c7126d41c | -13.4264 | -43.8163 | 2026-09-14 13:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| a08e609b-14a3-38b7-b1e8-604e6e493622 | -7.0166 | -44.6184 | 2026-09-14 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| c78cda4f-1c23-3dc9-a8c7-c3faf1216312 | -9.3763 | -50.1139 | 2026-09-14 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 87276bb3-f2a0-34ad-b855-91489bc3e36d | -6.5837 | -58.8498 | 2026-09-14 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| da34c07a-5b62-3940-9925-d647f21d6ce6 | -2.9025 | -50.4214 | 2026-09-14 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 278.6 |
| 7d685c71-231b-3379-9da9-5647b18ae274 | -10.7145 | -47.5374 | 2026-09-14 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| b5871632-eb86-3450-980c-f9f35dc85d15 | -15.5768 | -48.792 | 2026-09-14 13:00:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| eee3e6ec-d26b-3fd0-9cc5-6869199669d1 | -11.2391 | -43.4413 | 2026-09-14 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ca67f87b-0d24-38c6-a129-e57850a3b0e6 | -10.6643 | -54.1286 | 2026-09-14 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 8f113d8d-86d3-3d08-9d87-b3bbfee6f26a | -10.6638 | -54.1696 | 2026-09-14 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 41d5ab0c-3f02-397c-bb98-8c4f69987cc6 | -7.0164 | -44.6413 | 2026-09-14 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c78b70dd-1e49-3525-9c95-ce3d0309824b | -9.376 | -50.1352 | 2026-09-14 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 76e54a79-2c84-3a31-a576-a46ab0156afe | -15.5572 | -48.7953 | 2026-09-14 13:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 908452dc-3a28-3548-9fa7-923a89bf638c | -8.8081 | -45.8753 | 2026-09-14 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 222.3 |
| 972e276e-88c6-3792-be74-2fe74aecee43 | -8.7634 | -46.4194 | 2026-09-14 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 3e331116-1c42-371d-87e7-3bd3f146cf23 | -13.4458 | -43.8128 | 2026-09-14 13:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 158.8 |
| f8c284bc-c368-3b26-98fe-07dfca27d70f | -13.4453 | -43.8366 | 2026-09-14 13:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 4872bd63-1d3d-3ad5-9c77-b18027a611ea | -10.6827 | -54.1679 | 2026-09-14 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| d09072a2-494a-3055-994d-a59a98ea1a73 | -9.4328 | -50.1086 | 2026-09-14 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 69f42cde-0f5d-3c02-82e3-21d2eb02ab4c | -4.1333 | -60.6882 | 2026-09-14 13:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 85a6bc6f-8756-3665-b772-c677bb2749b8 | -2.921 | -50.3999 | 2026-09-14 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 83b27682-53b4-320f-9cf6-e987cb4b2de5 | -3.4272 | -58.2138 | 2026-09-14 13:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 132.6 |
| b5623e63-a5a1-34d1-9ca0-8a14a369156b | -9.3753 | -50.1992 | 2026-09-14 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e7ec7314-3d62-3e47-98e0-c61d3d7042e0 | -2.9025 | -50.4004 | 2026-09-14 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 0d39ffa8-a7ed-3654-82fc-4d13916b1d25 | -14.1856 | -47.407 | 2026-09-14 13:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| f1279d46-1219-3b71-8345-63a365bd1182 | -9.4513 | -50.1282 | 2026-09-14 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| d95df140-8d0b-3554-963c-8057aba898d3 | -6.1109 | -57.684 | 2026-09-14 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 22d00a33-a326-3e2a-8c09-54ccb16eded3 | -13.3059 | -51.3022 | 2026-09-14 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 7b70e568-d99a-3b1a-a990-0abc85e40441 | -13.2863 | -51.326 | 2026-09-14 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| bfcbbb0f-d042-3c1b-b3dc-135b059ef4c6 | -14.1861 | -47.3844 | 2026-09-14 13:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a802acec-4820-32f7-91b5-e2ddcc8dcaad | -15.2859 | -53.9037 | 2026-09-14 13:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 4743b305-c35d-3d4c-968b-31866e97f700 | -13.2867 | -51.3046 | 2026-09-14 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 494741c2-cb64-3d1f-91fd-b6f3cae12015 | -3.8042 | -44.1072 | 2026-09-14 13:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 13610633-f49f-3efa-a0dc-fd99621c60e8 | -10.6958 | -47.5175 | 2026-09-14 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b0cf636e-f204-3cb8-8759-459fcef950e6 | -3.42391 | -58.20204 | 2026-09-14 13:04:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 5b80bd97-53e5-3233-af1a-013a9a3b3bd7 | -6.0184 | -59.94548 | 2026-09-14 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 7c0068e9-c48e-3197-a8ea-df9636e565b6 | -3.42034 | -58.20825 | 2026-09-14 13:04:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 223.1 |
| e0f7ab9e-5fe9-35e8-a8e8-37dbe35b9d89 | -2.7107 | -57.54348 | 2026-09-14 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 77de5ffd-2825-31d8-9491-4bdf5fc8e3ba | -6.02681 | -59.92779 | 2026-09-14 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 94cac217-5bf0-3a50-968b-db191f0615f8 | -2.66724 | -57.50425 | 2026-09-14 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 99c70144-3af3-3b1c-9dec-e4194d052845 | -3.60913 | -59.06266 | 2026-09-14 13:04:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| a773ff3a-1eb9-3dc1-8c00-4386887c5e3c | -6.33248 | -60.00986 | 2026-09-14 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 9bdc303f-b3ad-3611-a59b-8e6282daad99 | -2.66276 | -57.53726 | 2026-09-14 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 869da6b6-655a-3c5e-8fda-0aaf891a2672 | -3.41983 | -58.23192 | 2026-09-14 13:04:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a6e3ead6-5d1e-3a49-89e8-7ea8b93b9ebf | -2.67424 | -57.57215 | 2026-09-14 13:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 8e0ceed8-ccfa-3f16-99b0-37fa37c76ef8 | -3.40855 | -58.20002 | 2026-09-14 13:04:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a0b8d459-f02e-394b-8352-8ddbabd6d36c | -6.68121 | -58.68429 | 2026-09-14 13:04:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 49f4917d-7d95-3662-acf7-0549972e939b | -6.28098 | -59.9229 | 2026-09-14 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c985f0c8-129a-3959-a299-9dc45bfeacb0 | -4.12987 | -60.6809 | 2026-09-14 13:04:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 12502f3b-fd09-39d0-9f75-6e851bb9a4e4 | -3.73575 | -61.74754 | 2026-09-14 13:04:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e99cd3ef-99bd-313f-85cd-6dd2f57ae1af | -6.66645 | -58.70722 | 2026-09-14 13:04:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 7d7beb46-8e07-3d38-a8b9-f042e5d7e2e8 | -3.35659 | -59.82286 | 2026-09-14 13:04:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c14d4aba-b600-326d-8e79-ac605efec0ed | -6.67739 | -58.71516 | 2026-09-14 13:04:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 175.7 |
| 0941effd-91a8-3c44-b9d9-fb7c83b4a3ee | -3.165 | -58.6499 | 2026-09-14 13:04:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 8fce771a-4dd8-344b-a8ba-2fe01905eecf | -3.59736 | -59.06668 | 2026-09-14 13:04:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| e99897b6-6aeb-3e04-91c8-ddb55aa0b580 | -6.02382 | -59.95188 | 2026-09-14 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| deb01f6f-1af4-3824-918e-ca130fda643f | -6.58513 | -58.85215 | 2026-09-14 13:04:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 66ee5a91-f94e-39df-bc20-d41f6e63ada5 | -4.11714 | -60.67923 | 2026-09-14 13:04:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0b2c7dc2-e36d-3cb1-b92e-53c5e7b8d5e1 | -9.26388 | -59.6236 | 2026-09-14 13:06:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| c465458d-4a7c-3b7a-b7bb-346e13a4375c | -9.26224 | -59.6301 | 2026-09-14 13:06:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 8ae6523c-330f-3514-8040-aabbb80a1e79 | -7.0166 | -44.6184 | 2026-09-14 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 84bc8366-b552-3b5e-a7a5-38bf9329b6df | -9.4513 | -50.1282 | 2026-09-14 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| cf06eaab-be36-35c4-8a78-c2964dd4bb7b | -8.6005 | -44.4378 | 2026-09-14 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 8cd443bf-c0f2-32cc-aa02-1efd11400696 | -9.4936 | -45.4818 | 2026-09-14 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ee6f3019-c061-3eb0-a0e9-8fbe23b3c607 | -13.3059 | -51.3022 | 2026-09-14 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 0447f292-c480-39cf-951c-de4c01831dd8 | -10.6955 | -47.5397 | 2026-09-14 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 486288e9-2532-3812-bab9-6589d53d37ff | -9.3763 | -50.1139 | 2026-09-14 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| a1e59a97-95bb-3af5-bd43-ec00fd41a165 | -8.8081 | -45.8753 | 2026-09-14 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 6244f87e-46b2-3cf9-8f46-599ecd674145 | -9.3753 | -50.1992 | 2026-09-14 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 38ecca72-cf57-357b-bc95-c249dba535df | -9.4328 | -50.1086 | 2026-09-14 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9d80f4aa-6f3a-3770-96c8-13cd84c0fe69 | -6.1109 | -57.684 | 2026-09-14 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 3dede9aa-203f-3d8a-b1c8-3d32e611163f | -8.7445 | -46.4213 | 2026-09-14 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| fd86b8cf-ceda-362b-bfc2-c2a5f6afce4a | -10.6638 | -54.1696 | 2026-09-14 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 44e98fc8-ecdd-3f56-8adc-5d024ee5cb90 | -4.1333 | -60.6882 | 2026-09-14 13:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |


[Clique aqui para ver as próximas entradas](README69.md)
