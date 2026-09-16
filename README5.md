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
| f7eac670-a51c-33b8-b09a-12793d404644 | -3.17277 | -61.12426 | 2026-09-16 00:24:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 05a32932-c8b1-3a8e-a02d-316d5a9cb8be | -4.52802 | -54.91885 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e0296d89-bd54-3617-b67d-80a6e14608ec | -3.14042 | -51.10585 | 2026-09-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e0b5e57c-3206-3e24-bbb2-f6b939425b48 | -4.17859 | -49.40928 | 2026-09-16 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d57effce-93f9-3dad-ba70-0394b83690b0 | -4.44364 | -55.5149 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 93c4a6f4-cb9c-36b8-af4c-eaa8e01247f8 | -2.71083 | -57.60794 | 2026-09-16 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 97017185-0fd9-35a4-80b1-b22b5af7e41f | -4.38731 | -55.04031 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2e04d0dd-4ec7-3262-bdd0-6a67770ce9ea | -3.10791 | -57.67891 | 2026-09-16 00:24:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c46a4a94-174e-3c97-a98a-96ce46ed3550 | -4.52652 | -54.97279 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 273d6393-692f-3264-88ea-4606278f8036 | -3.11723 | -57.67763 | 2026-09-16 00:24:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 694b952e-c7e5-3e08-ae4a-eef71e9112df | -1.01813 | -53.737 | 2026-09-16 00:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 9a5ec7ea-4158-34b4-b5c8-1519902ed337 | -2.90532 | -50.41961 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 080f94d5-0fee-3c40-a2fc-7dba24375871 | -1.21322 | -47.90474 | 2026-09-16 00:24:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 5b38710f-4ef6-3843-bb2d-c5db60061a2d | -2.69102 | -57.60076 | 2026-09-16 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0c3c241f-70cc-335f-aab6-3aade640442f | -2.63611 | -54.17994 | 2026-09-16 00:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| affe0458-8bd6-3292-a7d4-25387250dc52 | -3.07645 | -50.57291 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c322ccf5-2f02-3859-92c0-77428f278559 | -4.43431 | -55.79119 | 2026-09-16 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 52b5f8cb-15bf-3cf3-95df-c44d6c7d613c | -2.63741 | -54.18935 | 2026-09-16 00:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f4df65cf-e655-3610-9f7d-b5e0f1415814 | -3.48218 | -54.69111 | 2026-09-16 00:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ed7a5fcc-8951-317f-83cf-5c46ebb2f20a | -4.5149 | -54.97145 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dc9385bf-169f-3b8c-a38d-eb9984e29d58 | -2.10421 | -52.04835 | 2026-09-16 00:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 9f794f3c-6e08-3db9-a053-e84e7fd596bf | -3.16716 | -58.63922 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cc6dda91-3bb4-3e68-a364-0b24f5943b26 | -2.62707 | -54.18128 | 2026-09-16 00:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bfd921b4-7331-3c00-878a-c300527e6779 | -5.13833 | -55.94299 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e2f5b236-7592-3ce9-b727-76d571a58675 | -3.31128 | -47.14315 | 2026-09-16 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| b367566d-9685-3e29-a3b4-8e0b7315947a | -3.31419 | -47.16518 | 2026-09-16 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5cb87469-fa03-3bf1-a28e-296156acbd52 | -3.38057 | -50.84974 | 2026-09-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 4494f394-69fc-3410-b4c1-6e43240d4ab0 | -4.4334 | -55.71927 | 2026-09-16 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08800b28-a985-3625-9de8-5061da09b3a1 | -3.07832 | -50.57917 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ca488769-b25d-3a4d-a8d5-632654a50fdb | -3.46171 | -57.99836 | 2026-09-16 00:24:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 81f38a3a-ebc1-3d5f-9c5f-d0fd4b441eac | -3.3281 | -57.87186 | 2026-09-16 00:24:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4592606b-181a-3595-a774-fdf7257cb040 | -5.12826 | -55.93537 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 36fe84ff-bfe8-3183-ae1f-c4ebf7336e02 | -3.44656 | -50.66367 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0b45bf43-3314-3ed1-8f13-743ef24b40d0 | -3.45642 | -57.9943 | 2026-09-16 00:24:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 6d74441a-5910-3334-b077-8205077d6fab | -4.52986 | -56.07955 | 2026-09-16 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca6bddf7-4c84-3af7-87c3-bb12d759d54a | -3.01734 | -51.35217 | 2026-09-16 00:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 429d1264-6eb5-3ae6-8db8-e5126ee70d1a | -2.98416 | -54.16351 | 2026-09-16 00:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9737e567-91e5-3040-ba03-49a73f526916 | -3.17376 | -53.93406 | 2026-09-16 00:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bdeb5b16-d193-3593-ac80-a5635d3ef19c | -1.02887 | -53.74565 | 2026-09-16 00:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1a539d39-92b3-319d-b0c0-f9546d127c04 | -1.61156 | -55.57278 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 10898fd2-0bcb-3a86-bd7e-1b4e3ee1f633 | -2.88066 | -51.75493 | 2026-09-16 00:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ae7dbcb4-3879-3682-9fb7-fd19b560345e | -2.90405 | -54.85143 | 2026-09-16 00:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 67cfae00-a61e-3c49-ba0f-a745d1e2cffc | -0.92513 | -47.19333 | 2026-09-16 00:24:00 | TERRA_M-M | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| b63c7604-fbb3-32c1-8905-553d7d46e708 | -4.51127 | -54.94511 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 469ded55-7bfb-3484-b222-d9cfa2e8ef3b | -1.21662 | -55.64342 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 72519c6a-1989-3df7-aefb-1881c4ec1c85 | -1.74328 | -55.25567 | 2026-09-16 00:24:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 65060a49-24a4-3777-95f4-fff3a87f0be9 | -3.31061 | -57.88461 | 2026-09-16 00:24:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2518b9ee-2ce5-371b-aee3-615143684b2f | -4.53925 | -54.93519 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 663566f8-6a9d-3e41-8646-04a965095e31 | -3.21276 | -53.95118 | 2026-09-16 00:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 764a368a-6259-3544-a7c7-2048e0aa4719 | -2.89604 | -50.43709 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ca6b2122-3e7a-35de-95b9-1ddbd9f9d975 | -3.48094 | -54.68219 | 2026-09-16 00:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| f97ce2f4-3615-3c43-bd8c-5716bac6fab0 | -3.18249 | -61.10569 | 2026-09-16 00:24:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a0840831-38c2-3a97-ac0e-04bb9cddd9b3 | -2.97384 | -54.15554 | 2026-09-16 00:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e719b69c-7a5c-37d4-bbd1-f6c8e35fd9bb | -4.46145 | -55.25333 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3a8773e0-173f-32e0-9d24-edce6b92fd09 | -3.2641 | -54.51481 | 2026-09-16 00:24:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5e4c9dc3-77ab-3db3-98b0-75293b80a87b | -4.93362 | -55.79316 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6ea7cdd-d4b3-37e9-bb4a-8630da2c23e8 | -2.10596 | -52.06063 | 2026-09-16 00:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| c2017a29-5d7d-38c1-8945-1db389547da9 | -3.43043 | -58.23356 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b84712dc-0608-38c8-9e36-9e8d692128c9 | -4.4952 | -55.49875 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ecd98fc7-1b5a-3913-bfdb-623e56446906 | -2.91464 | -50.40211 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 25a22165-c4fc-3607-baf0-a966d1336cc7 | -3.36629 | -50.74801 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6f028d29-098b-3bbe-b2ee-8d21f639dd23 | -2.57338 | -55.99297 | 2026-09-16 00:24:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ab5bf98c-f069-3354-b971-6d958b41a920 | -2.72821 | -54.97878 | 2026-09-16 00:24:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1fce5af6-4fbf-37f3-a48e-42f97fa9b3e9 | -5.1472 | -55.94176 | 2026-09-16 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 22a888d4-8a87-3f71-a6b8-8ec619c2a6dc | -4.18792 | -49.41438 | 2026-09-16 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 32a8cc75-ec7a-3755-92e4-36b0e81d8fa5 | -3.47208 | -54.68346 | 2026-09-16 00:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7169508b-23e6-36f1-91bf-888a217cc12c | -2.56741 | -54.7441 | 2026-09-16 00:24:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c44b2ea-6a09-395e-a985-92a78cc6397e | -2.65947 | -57.56165 | 2026-09-16 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 69df2907-6be1-3d8b-815d-bc37371e2fc8 | -4.49641 | -55.50753 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8d33a994-3a01-3252-846a-6d515cd4cd6a | -3.15237 | -49.2265 | 2026-09-16 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 67737b64-1359-3638-a7ae-186126d0dd31 | -3.33477 | -58.1343 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d413815a-1996-3540-967b-685428d22a10 | -4.46301 | -55.05029 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ad376dc-24cd-3836-a077-8537465b0209 | -3.54105 | -53.99151 | 2026-09-16 00:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7708a18e-453d-3a70-94fe-ebb595529738 | -2.9169 | -50.41795 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 57357928-e7ff-3485-9354-5ab6c0318887 | -3.07621 | -50.56401 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| dd516935-87a1-3d7d-b0f6-5a728c853362 | -1.19199 | -54.13882 | 2026-09-16 00:24:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 08a826c8-16d3-38ce-8e62-a8e47f4797d1 | -1.21245 | -47.91158 | 2026-09-16 00:24:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 4d862826-c6cf-3d4e-8239-c3373481e2c4 | -3.50816 | -54.48653 | 2026-09-16 00:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 06402449-7d9d-3bea-b814-7bce92d2b811 | -2.69234 | -57.61049 | 2026-09-16 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 00f695f4-7b35-3f3d-9dbe-f0b4d51317bf | -2.10245 | -52.03603 | 2026-09-16 00:24:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a82c9052-86fd-3b07-a035-f31abefe4b2d | -3.43455 | -57.97622 | 2026-09-16 00:24:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| de37bf86-88c2-3e08-9836-3fc7e642c0a1 | -4.52287 | -54.94645 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c890cbd0-04f2-3dac-a435-238c7d0dc2d0 | -3.59365 | -58.53955 | 2026-09-16 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6e65d880-691d-302a-be8e-0988c5688df3 | -2.7791 | -57.02636 | 2026-09-16 00:24:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dd385e83-918d-3de8-b700-4f6206da9dbd | -4.3773 | -55.03276 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d4821148-b06a-3729-a632-dca3f05aca27 | -3.3789 | -50.82966 | 2026-09-16 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 4967f843-fa8b-3a2f-ad66-cad97f27f36a | -4.41094 | -55.08173 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1029c43e-e6a6-3d6c-9057-c253b78e0f8e | -2.58218 | -55.99174 | 2026-09-16 00:24:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0da4287d-79bb-3f76-b6d8-33c869e74ef0 | -1.20867 | -47.88461 | 2026-09-16 00:24:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 1663a5f5-f3a2-365d-8c6c-fb5cc52e4320 | -1.02751 | -53.73568 | 2026-09-16 00:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 0e60efbc-300a-38e3-97e9-a8c83b81c2a9 | -4.5253 | -54.964 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6537fe70-dd7f-3444-b357-2d356df2547c | -4.46422 | -55.05907 | 2026-09-16 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9b9b1ca0-1879-397b-9ae4-d90f1611e75b | -4.18532 | -49.39624 | 2026-09-16 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| e28b11a0-c52c-3bdf-9feb-abffa682fed3 | -3.05363 | -57.14703 | 2026-09-16 00:24:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 08e92bf3-71bf-3129-b213-54da8b75b628 | -3.30986 | -47.13672 | 2026-09-16 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 1651c8af-a023-3ada-9520-fd72422889f2 | -4.54684 | -54.92517 | 2026-09-16 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a77f0a97-b65f-3f55-b568-07ba3cef79f4 | -3.37855 | -50.83532 | 2026-09-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a120aa90-1ad1-3670-8925-a76227f9825a | -3.54234 | -54.00081 | 2026-09-16 00:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fec88d17-8f47-3484-9f96-5e7f0fd7dfed | -3.12382 | -61.25947 | 2026-09-16 00:24:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9c0ba0ab-431c-345e-86f2-1a372294e842 | -4.57081 | -54.90381 | 2026-09-16 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README6.md)
