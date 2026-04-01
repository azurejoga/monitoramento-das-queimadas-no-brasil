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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07ee5df2-51cc-3d15-9e16-cb2c5f76a4c8 | -20.04072 | -54.51852 | 2026-04-01 00:37:00 | TERRA_M-M | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f66745e6-9f53-3262-8fc7-f313cfb7dd6a | -20.03939 | -54.50789 | 2026-04-01 00:37:00 | TERRA_M-M | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e1a6ec46-f800-3a93-ba3e-1b1f08710a09 | -21.60345 | -56.62579 | 2026-04-01 00:37:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 4f6a0364-e151-3899-8f9d-cbb3178a89c7 | -22.48731 | -51.67123 | 2026-04-01 00:37:00 | TERRA_M-M | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 020bb3db-ad27-3694-9d9a-6d7885f506af | -14.44741 | -58.44829 | 2026-04-01 00:39:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f02be8bb-920d-3b86-8040-6d7401ed9fce | -16.42804 | -54.91321 | 2026-04-01 00:39:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 73de662d-0b1f-344a-b6ef-81ad217bdbcc | -11.95691 | -58.75452 | 2026-04-01 00:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f74285dc-5e81-345e-95ec-839d2c090724 | -14.44613 | -58.43882 | 2026-04-01 00:39:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0e90d809-a500-3513-9d5f-eb4be8525762 | -12.99475 | -54.67865 | 2026-04-01 00:39:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a74b641f-5692-389c-b733-4a28af5ea603 | -17.47471 | -55.1979 | 2026-04-01 00:39:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d8e30884-e253-396d-b140-b5a4c6faf58c | -14.54415 | -49.1084 | 2026-04-01 00:39:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a644cfe5-afe4-356c-bf50-a0eb30e1c50b | -10.7105 | -56.041 | 2026-04-01 00:47:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c52a9d4-82cb-3ac6-ab37-cecfcc68b6a1 | -10.7088 | -56.033699 | 2026-04-01 00:47:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 849339ec-b96c-3bbf-a19c-9a1111fd53a0 | -21.6082 | -56.617298 | 2026-04-01 01:19:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| acc3388e-1d37-3f2b-8cc4-ec8a8b77f84d | -16.436001 | -54.907799 | 2026-04-01 01:19:00 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 021a09a1-b1b4-3289-afbb-08135ea241be | -20.042101 | -54.5084 | 2026-04-01 01:19:00 | METOP-C | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 432de62e-17aa-3b85-921f-4772e81bc379 | -20.0438 | -54.5158 | 2026-04-01 01:19:00 | METOP-C | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e45e2b08-74f1-3ac1-a179-312b46c49ebf | -11.9549 | -58.752499 | 2026-04-01 01:19:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa32c08c-26d8-3cd6-b709-1016c663ea62 | -17.4744 | -55.2015 | 2026-04-01 01:19:00 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ca82ea54-fcbf-3f0d-a1e3-dc9146cc3938 | -16.4377 | -54.915401 | 2026-04-01 01:19:00 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0344b488-1ddc-33b5-85e7-cfb6e600d04f | -21.6098 | -56.624901 | 2026-04-01 01:19:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7813c4fb-9f53-3aaf-af7b-8503376b1249 | -4.93682 | -37.36977 | 2026-04-01 03:17:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e9187687-8c22-3495-922d-b47950b67fd6 | -4.94201 | -37.37071 | 2026-04-01 03:17:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a508c0f-056f-399c-92ba-69d02beb8daa | -4.93736 | -37.36665 | 2026-04-01 03:17:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4999bec1-718c-3447-8a93-ac3f1052c50e | -11.7245 | -37.62508 | 2026-04-01 03:19:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 56fac140-e76b-3380-816f-0355b51057b0 | -11.72079 | -37.61888 | 2026-04-01 03:19:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8ffe3f08-7978-3762-9438-935529aba824 | -19.59819 | -40.06269 | 2026-04-01 03:21:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e88e9c9f-6579-3ed4-b625-02624d1ff0c7 | -5.34936 | -45.12099 | 2026-04-01 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f790130-76de-3210-a89b-bd34d2ec0e71 | -4.93916 | -37.36818 | 2026-04-01 04:08:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15449c65-9943-34b4-8c52-f68d3cd7c36a | -5.34874 | -45.11816 | 2026-04-01 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9bed2ec-2184-3d67-bd48-024fc4c6e4ea | -5.345 | -45.1175 | 2026-04-01 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4f6357e-d928-38ec-abbf-69ddf36063b8 | -4.93543 | -37.36761 | 2026-04-01 04:08:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e09649f-c0b0-3bb9-adb9-b12a9888e8b1 | -5.34572 | -45.11297 | 2026-04-01 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37b56658-32bb-3358-8d48-c53a15d1bcae | -5.34637 | -45.11582 | 2026-04-01 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6dbf9c6-4c7f-3cfd-9b3b-df3dab3c38a2 | -11.72418 | -37.61985 | 2026-04-01 04:10:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 316266c1-94be-3ac2-bc97-dc2b70a45b02 | -11.72371 | -37.62339 | 2026-04-01 04:10:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4323eb16-04ea-38c0-833c-824e3cb08bfd | -17.47025 | -55.20119 | 2026-04-01 04:12:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4fc4d692-d269-3a40-8b0d-6b5d798b1b1a | -21.71172 | -48.43499 | 2026-04-01 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e13d6042-7a4b-37d3-81ab-4b063f9cd697 | -20.81907 | -48.28405 | 2026-04-01 04:12:00 | NOAA-21 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aee2b4ce-0262-3ba7-9410-81a98dbfd827 | -20.82267 | -48.28477 | 2026-04-01 04:12:00 | NOAA-21 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e65cf517-a4ac-38e9-bc21-2fbfec9f2bec | -20.81984 | -48.27964 | 2026-04-01 04:12:00 | NOAA-21 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44f1580c-ea02-3af7-b019-8258541a1f32 | -19.60207 | -40.06255 | 2026-04-01 04:12:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 21490ba8-abd6-3e3b-b366-6f1dfd3fc9c7 | -21.71251 | -48.43057 | 2026-04-01 04:12:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fb60ec9-9444-364c-9d90-4fa1f861a9b4 | -17.47539 | -55.20084 | 2026-04-01 04:12:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a290ed17-1aac-393f-84e3-863686714eea | -20.82018 | -48.28257 | 2026-04-01 04:12:00 | NOAA-21 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96c14aa0-4f29-391b-9e1d-95a627077434 | -19.989 | -54.74001 | 2026-04-01 04:12:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c42bb69-ddb1-3f33-adde-03b5b5189497 | -18.507 | -43.36427 | 2026-04-01 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 084ca1ce-0517-3ee5-8a85-1ba70e3c5608 | -16.42763 | -54.91121 | 2026-04-01 04:12:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cd59dea-ccc6-3a53-a98c-e03cd012dac4 | -16.43341 | -54.91273 | 2026-04-01 04:12:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b7bf919-411c-31ff-a4f1-6360674756a6 | -16.42666 | -54.91579 | 2026-04-01 04:12:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ae91086-6e6b-31fe-9e21-86565e01efff | -22.48403 | -51.6701 | 2026-04-01 04:14:00 | NOAA-21 | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e46268be-8d77-3311-ab50-1acc64812a37 | -23.58461 | -54.75396 | 2026-04-01 04:14:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3c7e6184-e9f9-3d00-8126-be1da6b2a78b | -21.60682 | -56.62868 | 2026-04-01 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f014b6f4-016e-3592-b64d-63de831cf49b | -21.60781 | -56.62436 | 2026-04-01 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6257f79e-afd2-3ae5-a43c-9996d35f2587 | -23.58529 | -54.75081 | 2026-04-01 04:14:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8949e32d-fab0-36e1-b7e1-3fcd4367d877 | -29.71154 | -50.68193 | 2026-04-01 04:17:00 | NOAA-21 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0b12afaf-07e7-3ed6-b654-a8168600cb1b | -30.05723 | -50.85252 | 2026-04-01 04:17:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 1b6ef8c9-33aa-30c1-ad5e-3865072ecbcc | -10.71109 | -56.0466 | 2026-04-01 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5aa5aca-f52c-3e43-9c07-b9ec89b60fd4 | -10.70765 | -56.04892 | 2026-04-01 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 689aad0c-169d-3b2c-b5ae-015686a55745 | -5.34846 | -45.12097 | 2026-04-01 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c995386-5448-3f78-afe8-b6886407743e | -10.71316 | -56.04485 | 2026-04-01 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e94b45e-8071-3265-a983-8a0b51003c1e | -10.71229 | -56.04973 | 2026-04-01 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb72cfb4-7c0a-3746-bf51-f6200999d886 | -5.1419 | -48.00398 | 2026-04-01 04:40:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d853d6cd-b07c-3125-96bc-aabed29c42e4 | -5.34616 | -45.11263 | 2026-04-01 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7e662f6-25cb-3309-b41a-4d8e33fc4e86 | -5.34555 | -45.11655 | 2026-04-01 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6d05181-9904-313a-bca7-015bf20ab8aa | -13.50494 | -56.85976 | 2026-04-01 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1c11ad7-ea51-3c39-851b-6ad67fff0794 | -16.30665 | -58.46863 | 2026-04-01 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8b2232a9-4ef5-363c-9743-8f494f081b6e | -16.42953 | -54.91026 | 2026-04-01 04:42:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3d1db76-3c45-3c39-9b8f-b3681a32e6ad | -16.99452 | -53.03556 | 2026-04-01 04:42:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52a0be7c-ff56-384d-ba1b-ce4d3a168bf5 | -16.9949 | -53.03719 | 2026-04-01 04:42:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78433266-9091-3c50-8f55-230b07eaf490 | -16.42861 | -54.91545 | 2026-04-01 04:42:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f1904a0-4977-3bfb-8b64-32a17dc8745e | -15.23779 | -50.83101 | 2026-04-01 04:42:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c58503cf-320c-3c37-af2a-27715f407018 | -15.24113 | -50.83159 | 2026-04-01 04:42:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a942e8ce-2d93-3e78-8d38-ff7d68f30310 | -21.60456 | -56.62544 | 2026-04-01 04:44:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ea3ed3c-dd64-3363-b4d1-bc90d80a871e | -20.04027 | -54.51487 | 2026-04-01 04:44:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ba71f64-c66a-3d0e-a66c-9a56da274320 | -17.90328 | -54.12459 | 2026-04-01 04:44:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b7f6711-3e2e-376f-9261-7694f52ff6c1 | -21.7135 | -48.43135 | 2026-04-01 04:44:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a2804cce-5e1d-3b8a-8f89-393d2cdb339b | -20.8168 | -55.67119 | 2026-04-01 04:44:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e97dafe-921a-3803-b5a2-39ecd0e35aea | -20.14209 | -52.83661 | 2026-04-01 04:44:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da305876-5c11-37e5-a210-5e4e409d2e93 | -21.78804 | -57.52397 | 2026-04-01 04:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28b13a19-ee63-35e0-91d6-fcdbabcf5a2c | -17.47349 | -55.2025 | 2026-04-01 04:44:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e58ba62d-7b90-30b1-a6f5-91a83c691738 | -17.45029 | -54.39918 | 2026-04-01 04:44:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e0d08ae-58c3-3cc0-afaa-0baed7b1238a | -21.70991 | -48.43082 | 2026-04-01 04:44:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05b39e59-047e-3288-bd4d-d3a1f7c699ca | -19.60329 | -40.06411 | 2026-04-01 04:44:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 44b42b7f-c8d7-3595-8824-51e4434fcb6d | -21.60852 | -56.62632 | 2026-04-01 04:44:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 726f7a44-dd3a-32bf-a84e-0ab3c3dc1f2f | -22.91797 | -49.20743 | 2026-04-01 04:44:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e0898e2-741d-3f54-ad10-0e2cfb2b6b46 | -20.81805 | -48.28074 | 2026-04-01 04:44:00 | NPP-375D | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f23d5d1-7e53-3740-9b13-28c9dd342303 | -23.58423 | -54.75253 | 2026-04-01 04:44:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5d30e998-46a1-3e00-94d3-52792a3cda91 | -20.91721 | -49.52528 | 2026-04-01 04:44:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb3ab572-eb8f-3b89-bfc1-36684083c532 | -19.60373 | -40.05977 | 2026-04-01 04:44:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fb062d15-92af-312c-bfa5-9451355b4d5d | -19.988 | -54.74319 | 2026-04-01 04:44:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26fcef9e-3f1c-362b-89dd-c2840c975c83 | -17.95968 | -53.67634 | 2026-04-01 04:44:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e0c4287-0c8e-391c-be65-1eb74be0ff34 | -17.47076 | -55.20047 | 2026-04-01 04:44:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e281e850-92eb-3972-9f9a-f95243cd2c2f | -28.56178 | -55.70454 | 2026-04-01 04:46:00 | NPP-375D | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| e9d71c50-3704-32a4-9b89-41ed6e680de8 | -29.71151 | -50.68229 | 2026-04-01 04:46:00 | NPP-375D | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c589824-d131-3bd6-b19d-5a156d65a7a7 | -30.05506 | -50.852 | 2026-04-01 04:46:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 1fa2aeeb-5aef-319d-bdb4-ae96246c3ba8 | -28.55832 | -55.70373 | 2026-04-01 04:46:00 | NPP-375D | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 19022576-2058-3817-8106-b13d6f4e5b8b | -29.86284 | -55.98153 | 2026-04-01 04:46:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 85c9b9b0-1e8e-3e42-ad14-e20d4b5cb99d | -16.43002 | -54.91127 | 2026-04-01 05:01:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31131163-d466-3d03-a5a8-445e73544792 | -12.2994 | -57.40456 | 2026-04-01 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
