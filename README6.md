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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc9bf62f-eb7e-36b0-9426-8c147637aa1a | -10.6829 | -54.1475 | 2026-09-13 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| df504b47-860a-3e5d-ba62-1cf103971500 | -12.6818 | -54.7379 | 2026-09-13 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| b5ce8253-fb34-3bd4-a82d-c3afcdee511f | -2.6785 | -57.5115 | 2026-09-13 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a9a6930c-6fc0-3c89-a231-04b309e7b7b3 | -10.9519 | -58.9655 | 2026-09-13 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 95123b43-53d3-3143-83ba-28cf884d0cba | -15.5595 | -53.7845 | 2026-09-13 00:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 3c09a8a8-1cff-3cee-9dbf-b2c62e909668 | -10.7015 | -54.1663 | 2026-09-13 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 197.1 |
| 4a251a24-b200-3a84-b194-e83c1d52fd96 | -15.579 | -53.782 | 2026-09-13 00:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 4a0994e1-73c6-317d-8712-b2023198bdf9 | -2.9579 | -50.3988 | 2026-09-13 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 49325227-afcd-3594-ba89-2c3d1434fb6c | -6.2831 | -59.9394 | 2026-09-13 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| fcf678c4-9d77-30c2-be70-4b7b3b1a7e35 | -10.5284 | -51.3808 | 2026-09-13 00:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 870fc1fe-b594-3f39-b316-7ed74bf3047d | -6.1111 | -57.6645 | 2026-09-13 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| ff6e47a1-66d1-3719-b48e-89d7bac447e9 | -3.7462 | -61.7552 | 2026-09-13 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 6f4f9b64-0853-34e6-8624-4077de67f8f4 | -6.8632 | -55.5601 | 2026-09-13 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 48296f03-7112-35c6-b2f5-148aca7eaad2 | -3.728 | -61.7555 | 2026-09-13 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| fcff0bf7-eeb4-33c8-9f93-2bf861db689e | -6.6021 | -58.849 | 2026-09-13 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 12ec7eee-8acb-341e-9737-f08fd8cf8835 | -10.7018 | -54.1458 | 2026-09-13 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 21780c4d-08c1-38d4-a441-13e413c7da6c | -10.6824 | -54.1884 | 2026-09-13 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 52de53d1-e485-3ddb-8820-0bcd87d0f54e | -10.7013 | -54.1868 | 2026-09-13 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 46977709-6d12-312c-8783-fad540fe08ca | -6.863 | -55.5801 | 2026-09-13 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9300e40e-c71c-33f3-9d8a-df46a249ad99 | -2.6784 | -57.5504 | 2026-09-13 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b48a383f-9dd6-3790-b9aa-1593314311b5 | -12.8543 | -44.386 | 2026-09-13 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 031bad27-08cd-37db-88c0-2628030e1e5d | -2.6602 | -57.5313 | 2026-09-13 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 71b4e5e2-25e9-3cec-93a6-9aedf9cbf3bd | -8.5417 | -54.6985 | 2026-09-13 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7db760c1-bdbb-3279-b66f-608e0daefb64 | -6.0731 | -57.861 | 2026-09-13 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 37a0c43b-dd1d-33d4-a4a6-38fe4c668e97 | -6.2243 | -51.6949 | 2026-09-13 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| a34480f1-a0a1-3348-ae1c-1ce4ef89bd46 | -10.6827 | -54.1679 | 2026-09-13 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 241.9 |
| 46a27aa2-ae39-3fb3-9b23-7eb3ad98378e | -2.6785 | -57.531 | 2026-09-13 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 6f9ba160-a48c-3d97-aadb-e02704142015 | -6.6757 | -58.8847 | 2026-09-13 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b9bdab55-8808-325a-bec1-443d0e6e24d2 | -10.69 | -54.2 | 2026-09-13 00:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1ab7b53-6f82-3edb-92f1-1d9567ac2503 | -5.9631 | -57.7679 | 2026-09-13 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| d8893bab-8c83-31b2-9f95-fe1a082a1595 | -10.6829 | -54.1475 | 2026-09-13 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| b2b28e7d-645c-37f3-a161-9e320744913e | -10.5286 | -51.3597 | 2026-09-13 00:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ee2f7013-f4ef-33da-9de7-444228db4c80 | -6.6757 | -58.8847 | 2026-09-13 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 053edced-3bc6-31b6-9433-d8f1a1b7966c | -6.2831 | -59.9394 | 2026-09-13 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 5a1ac8d7-9da7-347b-9ad3-287cfea71cae | -3.7462 | -61.7552 | 2026-09-13 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 105c715e-43d6-38c2-9d36-a9b8092200d7 | -8.5417 | -54.6985 | 2026-09-13 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 9d909f58-71cf-327d-aa3f-f08c6af1a5b9 | -6.2243 | -51.6949 | 2026-09-13 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 12804345-024b-3d89-bcd6-7074d54705e3 | -5.1651 | -49.3581 | 2026-09-13 00:20:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| d353c6e1-0245-348b-b32d-b3501556f5e9 | -10.7018 | -54.1458 | 2026-09-13 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4ca502fa-4cf5-3b66-87f8-37af552eb833 | -3.3293 | -42.2893 | 2026-09-13 00:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9385f02d-08fe-326a-958c-48a45b1b1d2c | -3.728 | -61.7555 | 2026-09-13 00:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7baacc12-c27a-3431-adc9-21e12d890360 | -2.6602 | -57.5313 | 2026-09-13 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 7d71af32-573a-3239-98ed-1a9f74d3eb41 | -2.6785 | -57.5115 | 2026-09-13 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7d385e23-fa21-3c98-8966-507f849dfee8 | -2.6784 | -57.5504 | 2026-09-13 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 7262da98-bf89-3c7e-8dae-1851d7331a32 | -2.9579 | -50.3988 | 2026-09-13 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8a1629e0-ae67-3c3a-a7b2-a6a4882f8b9f | -10.9707 | -58.9642 | 2026-09-13 00:20:00 | GOES-19 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| fdbbf527-4c83-3f5f-9e4b-f5a919b807fa | -6.6021 | -58.849 | 2026-09-13 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 4232b265-eaf0-3b76-859a-ca0022950612 | -10.6827 | -54.1679 | 2026-09-13 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 317.1 |
| d98563af-dc5d-34d5-aaff-e825bdc2b0f7 | -6.0731 | -57.861 | 2026-09-13 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a2f5dbe5-2621-3287-bc2c-d067a7c3ae2c | -8.5415 | -54.7187 | 2026-09-13 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 4e1ba941-e68e-33a1-81e8-36fd44cc30c7 | -10.6824 | -54.1884 | 2026-09-13 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| b1f1c3be-7641-3a14-a92e-d617c5f88d57 | -2.6785 | -57.531 | 2026-09-13 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| e03faced-fd90-3e5e-9371-76792fe93a3c | -5.8206 | -53.8052 | 2026-09-13 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7d8441c6-90cf-38fb-8735-150cb62b24b2 | -6.8445 | -55.581 | 2026-09-13 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0cfe4c11-f465-39ea-b4d5-0eb4fcd1c11b | -10.7015 | -54.1663 | 2026-09-13 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 5ed66a7e-3eef-3e82-b0d1-4bb55aac5412 | -3.3292 | -42.3129 | 2026-09-13 00:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7a665d13-c6a0-3873-8a0b-f8575be1b153 | -6.863 | -55.5801 | 2026-09-13 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 3d0ce965-341a-35dd-ac4e-639418d342bb | -6.1111 | -57.6645 | 2026-09-13 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2e7dbddb-f051-322f-85d3-fa822b1b0143 | -10.5473 | -51.379 | 2026-09-13 00:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3693daa7-14f6-3bef-bff4-66062927df0f | -3.3292 | -42.3129 | 2026-09-13 00:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 54d19930-e8ab-3482-887d-c293f0ade284 | -10.6829 | -54.1475 | 2026-09-13 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.6 |
| b59d5be5-5f6b-3428-84e0-d901b3a6a487 | -2.6785 | -57.531 | 2026-09-13 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 125.5 |
| f2ab4f34-3174-3b78-87df-64fd9c206f30 | -2.6785 | -57.5115 | 2026-09-13 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 5caad961-83e4-341b-9bc0-42980005dcd4 | -6.6757 | -58.8847 | 2026-09-13 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c76b47e3-9181-38d4-b120-e024b82f41b5 | -2.6602 | -57.5313 | 2026-09-13 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 81bcd927-c798-337f-bb16-da473d0d7453 | -6.8632 | -55.5601 | 2026-09-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| b9e5c201-919e-33b0-b2d7-747ec32f5608 | -6.6758 | -58.8654 | 2026-09-13 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3d4ab57d-8ab5-3c16-863a-9d81abb0417d | -3.7462 | -61.7552 | 2026-09-13 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 4aa1ad11-2433-3ee8-af0b-edb150458b74 | -6.6021 | -58.849 | 2026-09-13 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 832d43d5-1325-3596-b62d-e1ce139b9952 | -10.6827 | -54.1679 | 2026-09-13 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 320.2 |
| a11a8330-355d-3559-a765-ce7c63f3f782 | -3.728 | -61.7555 | 2026-09-13 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3e554c85-93fd-3376-aa6f-135f261f085a | -2.9579 | -50.3988 | 2026-09-13 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a6083309-0b34-31ab-ba76-03223c58ec55 | -8.5415 | -54.7187 | 2026-09-13 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 804d86dd-3d56-30eb-bc96-465fa6be4cb6 | -3.3293 | -42.2893 | 2026-09-13 00:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b581d7d6-daf0-34ee-8544-33a4df628bc8 | -6.8445 | -55.581 | 2026-09-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8c4ab47c-921f-3b59-b720-c21d40f2e7f6 | -5.8206 | -53.8052 | 2026-09-13 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 010d7b4c-305b-375a-9f0a-97aa3f5df565 | -10.7015 | -54.1663 | 2026-09-13 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| b7666bce-c9da-375d-aada-f66e1d2330c9 | -3.728 | -61.7367 | 2026-09-13 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 91be6b4c-cc15-3120-b2c5-4a740216d7c7 | -6.1111 | -57.6645 | 2026-09-13 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 06f15735-6b63-321a-ad3c-aa91c6fe118f | -3.7279 | -61.7744 | 2026-09-13 00:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| cfe31f01-b265-3f1e-8899-8e48861bb224 | -2.6784 | -57.5504 | 2026-09-13 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3b9f4683-399c-36ef-80ee-74268d9d9b20 | -6.863 | -55.5801 | 2026-09-13 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 96ab2c40-3307-3b96-b5c7-0adc44a2df80 | -10.6824 | -54.1884 | 2026-09-13 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 064ef3d1-3f36-301d-86e6-de89a4f8a201 | -8.5417 | -54.6985 | 2026-09-13 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f5f8134b-07bf-3824-a701-cbfd59640764 | -10.6824 | -54.1884 | 2026-09-13 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 6ae35dcc-5031-3534-9d3b-eb82df6351e8 | -15.579 | -53.782 | 2026-09-13 00:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 00bac771-a07d-3197-b237-da89af57c53c | -9.3951 | -50.1121 | 2026-09-13 00:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c371043b-bee9-38e7-b3c8-f3c0b2a4b336 | -6.6757 | -58.8847 | 2026-09-13 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 00a22d85-3e5e-39d9-a28e-c6a747366c61 | -10.5473 | -51.379 | 2026-09-13 00:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| ac37003b-ccec-36ba-9b0a-6d6391dc4985 | -15.5592 | -53.8056 | 2026-09-13 00:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 9fb2f0f5-7ae6-356d-a8e3-10934fb9ed43 | -8.5417 | -54.6985 | 2026-09-13 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d9465135-6a96-3a95-b8e8-b431e700ef91 | -6.8445 | -55.581 | 2026-09-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b5f4240c-7fd1-3a3a-a657-f4094196585a | -6.2243 | -51.6949 | 2026-09-13 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 25898f92-182b-30cd-984a-21d5d26d568c | -2.6785 | -57.5115 | 2026-09-13 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 3f79af5d-ef25-3908-afad-4f2861e0395d | -10.5284 | -51.3808 | 2026-09-13 00:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| aa0e34dc-4719-32a3-8b0d-fde7dc951503 | -6.0731 | -57.861 | 2026-09-13 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 945c858c-e1ba-361c-9e50-f846a1dbe360 | -10.6827 | -54.1679 | 2026-09-13 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 276.0 |
| 87f93e96-a0ef-3ff6-a3da-ade88842ead7 | -2.6785 | -57.531 | 2026-09-13 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 8233bfd7-bdbd-3ada-a9fd-ade663e914ff | -9.1337 | -65.8253 | 2026-09-13 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 91bd0360-cb6b-3f8b-b590-aa2010ab15e3 | -15.5595 | -53.7845 | 2026-09-13 00:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |


[Clique aqui para ver as próximas entradas](README7.md)
