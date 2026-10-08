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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff65bfbe-ae18-3fcb-aedd-282bd020d2eb | -8.08874 | -55.31363 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed094dd3-3dec-3737-8ab2-447097b8eca2 | -14.93309 | -48.11165 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 642f0b9c-fd63-353b-95b4-14a23d4f9e75 | -14.91599 | -48.11813 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01e9348f-4749-3582-a0d9-bdd969933447 | -6.99867 | -59.11574 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dca410b1-4adb-3d27-ae5f-37640b078006 | -9.43269 | -48.84856 | 2026-10-08 05:25:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b37a192-24c1-373a-9948-57d7d110db00 | -9.59352 | -47.78124 | 2026-10-08 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dce3e9f7-0fe3-3215-88ad-363f7e374823 | -6.73251 | -63.05194 | 2026-10-08 05:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fe64597-4c72-314f-a52c-6bf6fc388882 | -8.08123 | -55.29269 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4407060-dd2d-34c9-b054-7a2387c22096 | -6.99525 | -59.11519 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7df31414-cbfb-3350-82a4-2dc9e4547617 | -7.45337 | -63.56015 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 647c9351-321b-3441-b998-a261df2b0f7b | -8.25061 | -54.7252 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9c14f9a-0743-3b35-a86c-879c8427fd6d | -8.30763 | -54.67302 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec6a7850-9795-31d8-b3b0-608fafc9dc46 | -8.2057 | -54.70567 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e7aa227-f2d3-37ac-83a3-182a7bd526f4 | -6.99405 | -59.12257 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52120e89-d375-3399-ba6c-cf0d7109b75e | -7.00148 | -59.11998 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0594ae60-a21f-340e-91b7-9b52f4e03dd8 | -7.53668 | -55.83455 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cccd148-5ea0-372b-8db6-f312c6bb5524 | -11.30054 | -44.83046 | 2026-10-08 05:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9653bc85-cf73-381e-bd1f-4eb3d99b98f5 | -9.77857 | -55.11072 | 2026-10-08 05:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d08bbd2a-2f43-3df2-a23b-d1b77024a8f0 | -11.23877 | -44.87178 | 2026-10-08 05:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1aa585b5-a490-3e03-99a7-70e338e66fba | -10.7722 | -46.57383 | 2026-10-08 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1887b6f3-a4e5-3bbf-95df-399ab3802c6c | -8.07833 | -55.28829 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b51ea97c-cc43-3ce9-95b1-8f09e7469665 | -7.00832 | -59.12109 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e3bab3ef-5ad9-394f-b9ba-25308dcd893d | -6.99363 | -59.10359 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50457aac-cefd-369d-9084-8951c575ea9e | -19.99315 | -49.08542 | 2026-10-08 05:25:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75426bd5-8058-3719-abfe-895be8cf8007 | -6.99927 | -59.11205 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9e023a2-42c2-3d5a-a382-6ce027c3c1a9 | -8.98851 | -45.91755 | 2026-10-08 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfe844a9-d93c-375f-869b-529bfe939066 | -16.75901 | -53.37852 | 2026-10-08 05:25:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 42a8ffa1-ce1c-356e-8320-e28788588771 | -8.17685 | -54.72651 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 709029c3-610d-3102-8e2d-82639bd42829 | -7.0043 | -59.12423 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 753a7ebb-f817-3f84-bb11-463ba9d814da | -7.89511 | -54.71681 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fe0994d-2709-300d-90cd-b685e1da146e | -8.22369 | -56.08127 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91924b6a-cf92-37cd-82d3-e9eda195c832 | -8.98813 | -45.91686 | 2026-10-08 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c55dba7-01d9-3c9c-97fe-9d41b7e03967 | -9.37393 | -55.97244 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 177253e0-1b6f-3623-acf8-e73f096f7798 | -7.32601 | -59.89567 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85a30850-32cb-3158-91e0-1ec396cf010c | -11.3076 | -44.83116 | 2026-10-08 05:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ca35e96-d73a-3e8c-86ba-f0a16db22559 | -14.92079 | -48.11241 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7bd8b2b-9246-3d47-b3e7-0903d244ee00 | -7.76329 | -54.94542 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6721f320-0e58-39b1-a9bb-6cf590ad045f | -9.58486 | -54.63815 | 2026-10-08 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 196e3ba3-dbd0-3b08-a142-4cc9c3a4cf7a | -9.19473 | -58.95185 | 2026-10-08 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c5cc5b7-c800-3938-88af-8a735552338e | -9.40031 | -49.00741 | 2026-10-08 05:25:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8d9baa8-6865-365f-aab0-d2817742b28f | -7.76036 | -54.94087 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a11f2135-5e4b-310b-b91e-7f23d3c5c9e3 | -14.93006 | -48.10064 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42a306cb-d96b-3462-a06b-7297b341f298 | -8.08533 | -55.28934 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4199d765-bfd6-3547-8363-e2df654e80fe | -8.25452 | -61.39204 | 2026-10-08 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9db534c-1f4c-3e7c-81a9-deb163f8df56 | -7.7639 | -54.94142 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 667d5dff-66c2-314f-9806-b6b30f750a89 | -8.08814 | -55.31749 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3097a6e-d84a-3cb9-b036-a55ba2dbc4fa | -14.9203 | -48.11676 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a4537b7-50a6-3ec0-8215-aa0c159fa941 | -14.67167 | -51.46448 | 2026-10-08 05:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0af86581-1066-35bf-80f8-ef05cb6ec721 | -6.99303 | -59.10727 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f8b78f1-0816-3350-8732-5937720fb350 | -8.22084 | -56.07708 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4461787a-a44c-3171-8f71-f3ccd0c2320b | -8.08234 | -55.30871 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6dc7d59-7ecd-3a76-a456-6e32c68a658e | -6.86572 | -59.35314 | 2026-10-08 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f487776e-e704-37a9-8574-3f0cecc3f971 | -8.07423 | -55.29163 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80914ec6-42ba-3881-a5f0-d39b45b6d5d7 | -10.77608 | -46.57394 | 2026-10-08 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f85a3296-e59f-32c5-9c5e-03239b135c6d | -7.44255 | -63.54558 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a7c6dddc-3cd3-375f-9dad-1d3733726ce9 | -6.48943 | -62.85317 | 2026-10-08 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e372b906-7489-3159-958f-076e06557dbf | -14.92133 | -48.10765 | 2026-10-08 05:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eec36b8f-cc14-3e2b-9e62-90c0abb9fe43 | -8.23077 | -54.73473 | 2026-10-08 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a7587e0-f645-320d-b5f4-816f351d6c40 | -10.76986 | -46.57247 | 2026-10-08 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62e57e9a-9b5b-3b4f-8709-42fa4fcbfdc8 | -6.73229 | -63.05096 | 2026-10-08 05:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3698a50-d220-35ca-b60a-c3fbf073ef0d | -9.59378 | -47.78118 | 2026-10-08 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 23453a2d-9561-337b-bf96-5aa80f3bd699 | -8.08183 | -55.28881 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0599465-331c-3c57-982b-c6155174af69 | -7.44545 | -63.55453 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee63ff34-6b97-3ede-b30d-fd76db48bbad | -8.07653 | -55.29991 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58f7259-70fd-36e9-91df-3724faf7145d | -7.44615 | -63.55043 | 2026-10-08 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a38910b7-cd47-3dc2-b550-ce7c742c4cfe | -8.06254 | -55.29775 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea6c721-e069-3ffd-88ba-c0f4856ba71b | -8.99487 | -45.91888 | 2026-10-08 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1fcc039-3201-3968-af42-8aef44743684 | -9.51574 | -54.75018 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 151f372e-bd7c-324f-b65f-3c9f680b67ff | -8.08353 | -55.30097 | 2026-10-08 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a0eea56-5991-3846-9fbc-fceff532b0c8 | 2.10666 | -60.62468 | 2026-10-08 05:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2496466-a95f-3484-84d5-aed61034941a | -1.33149 | -55.43436 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4a2ff22-7c45-3ad2-b316-56445907f3ea | 4.43986 | -60.93159 | 2026-10-08 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 539f1b3d-f644-3275-a107-dc31084915d5 | -1.45526 | -54.78462 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98c2c4e9-450b-31a5-8b8f-26b72c33f585 | -1.28432 | -54.55999 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6e4114f-f87d-384a-92e7-fc625bd7061a | 2.54629 | -60.61059 | 2026-10-08 05:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b308a7d-d8af-3eca-881f-a312d8df899c | -1.08286 | -54.1116 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c0acaf5-1793-3302-b950-e5090aa2d1ff | -1.60459 | -55.16335 | 2026-10-08 05:40:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7586ff92-e29e-3118-91e6-c983c044dd74 | 1.70391 | -55.60834 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89453782-503a-3eae-846c-a64f3db5c3b6 | -1.45775 | -54.7681 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8510a5d5-010e-3afd-a273-41c7077f2766 | -1.52787 | -54.54188 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1786657-08c0-3181-964e-d85272377d44 | -1.50953 | -54.82619 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5836faa2-2e65-3795-a53b-eb9fdb15e88d | -1.5211 | -54.81675 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07a57c58-8f8f-35b3-b1ca-3ea2250a57d4 | 1.70167 | -55.61577 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb89786-8fd2-367e-89da-7b65d2e28cdc | 1.71205 | -55.60252 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25864d9e-55fe-3c69-b970-47e790f490d7 | -1.72248 | -55.44459 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3ce75da-4bf2-344e-bef3-3e569a1c9fa3 | -1.52877 | -54.53599 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa60dcd3-1404-395d-b8f4-bd2b1d96fbb2 | -1.28846 | -54.56644 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c7ffd92-5078-3418-991a-1ed76b5f1289 | -1.28591 | -55.41701 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf8f3cec-0c16-3d06-8417-5f7e1af7db61 | 2.90516 | -60.94285 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ec75135-f7ac-3326-bfc0-b2bdee20f201 | 1.34661 | -56.1367 | 2026-10-08 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36972c11-8215-3850-b208-93466f1c3bf9 | -1.20139 | -55.68901 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 836a6b4d-6e60-3944-a380-6d6796fab174 | -1.21407 | -55.64431 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d434f72-1c9d-3b09-8c55-974bc6306a5f | 0.88578 | -59.65191 | 2026-10-08 05:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5f8b6cb-3bbb-3a92-bfa2-733095b91274 | -1.10463 | -54.17378 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 112d29d9-8b90-31b5-ae95-34efe31f2948 | -1.52417 | -54.53239 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4614c63c-fa3a-32a2-a097-b1bedeb99ce2 | -1.53157 | -54.55132 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 0a8ab876-082a-3666-bbe5-68cc5c84b334 | -1.46155 | -54.76879 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12d4ad7c-c4dc-3652-8fdf-55e4721db039 | -1.53615 | -54.55497 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 832a3de1-eb57-3f06-8074-fe5455dfcdd2 | -1.32675 | -55.43377 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f8a21f9-d417-30fb-801e-837b1a141c4f | -1.37738 | -56.89498 | 2026-10-08 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README174.md)
