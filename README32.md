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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a231759d-fe67-3d75-8c69-7e63167e7f82 | -8.56943 | -54.69758 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed190848-aed5-30df-9c94-6ccfa371ca22 | -10.34057 | -50.82104 | 2025-08-13 05:29:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2a91798-ea40-33c5-89bc-32c118d4be27 | -9.19429 | -59.65837 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 50994b1f-828f-3983-a6ee-3e7929a02ec0 | -7.26125 | -60.62923 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1f49c2d-84e7-324a-b7b6-e4d5a040a706 | -9.51214 | -62.37523 | 2025-08-13 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 531525ea-58d4-3943-a47d-4367526988d6 | -8.56528 | -54.69124 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5bbae35-13ef-3567-9bce-f76a3694aced | -10.47367 | -61.32734 | 2025-08-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59dae013-5cce-3fce-8d72-fd593e922368 | -10.47708 | -61.32788 | 2025-08-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95d6d8f9-da78-3439-84d4-e1f567e689d1 | -9.06479 | -60.64776 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dcb6a66b-45ce-3aed-9709-35ce19aa9c77 | -9.18098 | -59.67352 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5fe4b57-5413-3532-9157-6ec35cf66007 | -9.18221 | -59.66516 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d49b2165-f00b-36bc-8e4f-9e205d8babeb | -8.10398 | -55.5766 | 2025-08-13 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41b3a9fd-d22c-3d1b-8d5b-bbd17bcf7da1 | -8.93328 | -60.72958 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05a0c372-9bb6-3a17-9fda-8a19d55a395e | -9.38119 | -61.53349 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb7f7e65-53e2-3d99-b98d-4b001d2bdc2b | -7.26807 | -60.63025 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 869dd8f4-7df8-30e6-803d-df5a761b5c92 | -9.38231 | -61.52626 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab4849a1-1321-384a-a3ff-ecdaba861ba9 | -7.45424 | -60.62744 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d426971-d338-3db7-b8e8-7c75691f8369 | -7.45765 | -60.62796 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78eed01c-c0b7-3d24-9cf3-044993d4a2f7 | -7.46208 | -59.88969 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 075b6ddc-1a94-3b7b-bae9-89756906bdb8 | -7.25341 | -59.99909 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30ffefe8-4ef4-3a9f-a46d-40d60dba761e | -8.92471 | -60.763 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49171a3e-dea6-3715-b9c3-417fb1f06156 | -9.92658 | -65.23522 | 2025-08-13 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1108de6f-3c38-3064-887f-9180d4572ddd | -9.52801 | -62.40286 | 2025-08-13 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f0e9d68-1c47-38e5-aee6-32c3cd4ddc12 | -9.06133 | -60.64723 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a36a6c6c-2744-3e28-88fd-546f168f8206 | -11.7437 | -58.33375 | 2025-08-13 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c7e1bf1-fed4-3e2b-b84e-bfe1cfccb44d | -9.20092 | -59.66359 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bac34e8-7b03-32b7-92b9-323fe450dfc6 | -11.81035 | -62.74656 | 2025-08-13 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e4240a72-2de8-3ed5-b0d3-4001bd3a671e | -10.47763 | -61.32421 | 2025-08-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 083c6653-612f-37d8-80e3-13f7ce2e1e45 | -7.46267 | -59.88575 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a5a4f89-6032-3f97-920c-ca5805efd9cd | -9.92313 | -65.23465 | 2025-08-13 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ec3116b8-01fb-32d8-a09d-93d73ac54e2f | -10.47422 | -61.32368 | 2025-08-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99649eec-88f3-3dfc-ae39-1f87c7c1174d | -9.06076 | -60.65105 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e3a97457-76d6-3ba9-9e31-8143e1e8cae9 | -11.31631 | -55.22608 | 2025-08-13 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cac057f-48eb-3243-899a-efb69417ac51 | -8.57157 | -54.69395 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 993609d4-1123-3026-ad12-caf7baeea276 | -10.3345 | -64.47052 | 2025-08-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89b7ec62-1be0-31b6-bccb-6062fd2fbc98 | -8.93672 | -60.7301 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87753079-198b-3c79-b49f-0f082e7185d3 | -9.19791 | -59.65889 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a32039b3-22c3-3809-81ee-7f50211f671e | -9.20215 | -59.65519 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16bf952f-a05f-3f40-9e80-164f37c0b0bd | -9.18882 | -59.67043 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c0ca0a2-eb67-3918-877c-ae8df2dc5dbc | -11.11343 | -62.66489 | 2025-08-13 05:29:00 | NOAA-20 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b611728f-1517-33e6-b234-3c840e47540a | -7.39182 | -59.99911 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcff93ed-3901-350b-9243-83fd82a506e0 | -9.82761 | -60.76384 | 2025-08-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8064e8e2-2ab1-3aea-9187-2c4f15859fbf | -7.45311 | -60.63481 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adbc1d2e-d79a-3ca9-9cc6-7c82ac175da8 | -8.57352 | -54.71719 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a97b1bd3-8d3d-3198-8880-7ec697205af0 | -10.75446 | -69.08384 | 2025-08-13 05:29:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 665be89c-c86d-3c42-92c9-d9efe07c6b17 | -7.26466 | -60.62974 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 31919e66-5fdc-3a06-b82f-75197103a982 | -9.1816 | -59.66934 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92b5a1d3-5af3-3b95-b2f6-4d71e96f5f2f | -9.21064 | -59.64783 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 747049e2-8ce2-32c5-b080-ae3e0abc57e5 | -9.51269 | -62.37173 | 2025-08-13 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3694796-e841-3656-a398-b544db7b13a2 | -8.56663 | -54.69324 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c87d26b-52b1-3cb6-948c-f2b0ba2fe3de | -10.34752 | -57.60166 | 2025-08-13 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91d0e4ed-572f-3b42-ad81-695e84adc2b9 | -9.06018 | -60.65487 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a45cc94e-30a0-359b-9ef7-368db6368406 | -9.46212 | -63.14648 | 2025-08-13 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89cbca58-b61b-355f-9cc8-2ca3bada8d40 | -9.19668 | -59.66727 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2bfff0d-ac94-3df3-a28b-883206cc9a0d | -11.91208 | -52.54028 | 2025-08-13 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06ae91b6-6047-333e-b6ca-ac18fee5c8fb | -8.57022 | -54.69193 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fe8fc20-62cb-34d5-a479-d4766f3897c3 | -9.18582 | -59.66571 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab322ce1-11d3-3f31-b0c6-6061959a19b2 | -9.1686 | -59.67345 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bca3be9-a9d5-3e2e-ac56-7f277537996e | -9.27407 | -60.76834 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eec66a60-40f4-3cfc-95dd-aa14c11f79a5 | -7.25728 | -60.63237 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f7cb0c6-a401-3249-bbe2-8bf78e79c274 | -8.93615 | -60.73388 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27c7e6d9-5e03-3bc6-89a8-2d9efe79fabc | -7.46148 | -59.89362 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7c85b1c-b7bf-33b1-9abd-3cbba45d872a | -8.9398 | -62.23444 | 2025-08-13 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae5b32bb-b2e1-38d4-84d3-99c0c054a44c | -9.71083 | -49.47754 | 2025-08-13 05:29:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c2228589-a395-3bc7-bde9-c744509cfef9 | -10.34122 | -64.47163 | 2025-08-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9383a76a-b734-39bc-b3c7-8f688174c876 | -11.9061 | -52.53964 | 2025-08-13 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 798c8efe-792a-3039-bde7-d38ccf9d160d | -10.33786 | -64.47108 | 2025-08-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd3982e4-1ae1-3836-811f-eb9793ce2865 | -7.90006 | -63.52722 | 2025-08-13 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27dcf9e1-57be-3de3-978c-4632fd8c3177 | -9.19006 | -59.66205 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a5d8f2a-3732-3bd9-aa2d-bca4e710534e | -9.20702 | -59.6473 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ed768c8-58d6-3917-897b-8e18e8a38449 | -7.44578 | -67.73255 | 2025-08-13 05:29:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98dc741f-bad8-3f0d-b632-eeb4f80ecd3c | -7.26039 | -60.00016 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73abace6-1dc5-3de1-8603-ce19e3fa753d | -9.67827 | -64.70897 | 2025-08-13 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46e3d060-e9f2-3cf2-8aef-22595e0af4a8 | -9.37109 | -61.53192 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93ce8289-fa30-32be-abad-73d446643977 | -9.37391 | -61.53605 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e63a1f08-4f47-3b70-9889-a37e670dcb63 | -7.23947 | -59.99691 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2088d098-c45e-3a78-bc6c-786e3641f814 | -9.18644 | -59.66153 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3af1cc80-6572-3836-bacf-a8c77b43a2c4 | -8.572 | -54.71515 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d46b361c-723a-3771-a4f0-547237e1630e | -9.19306 | -59.66675 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b93b1cf6-f4a1-3550-9c8a-c1c0cdfcd031 | -9.02164 | -63.90817 | 2025-08-13 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6778c315-b90f-33ec-8cee-a569d6b3ba89 | -10.97352 | -49.57366 | 2025-08-13 05:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37a8c92f-f868-36dc-9fad-6f6aab8f2a5c | -7.24296 | -59.99747 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bca965f-baa6-3b94-b3bd-1311c037e1d9 | -9.38286 | -61.52265 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96c9cbf0-5fbb-3441-9a77-437c76f148a2 | -9.38512 | -61.5304 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8154bc02-e3e6-3e9f-b0fe-2416b658d881 | -7.2641 | -60.6334 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 932345da-e82a-34af-8921-85517c68f0e6 | -9.16954 | -59.67604 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53149c6b-13b4-3049-b4f1-e833dfb32db8 | -8.10859 | -55.57731 | 2025-08-13 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 458297ad-1094-367d-b7c6-6c75d7999f49 | -7.45917 | -59.88519 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2e5b500-0ba4-36a2-94ce-abaf68bba8b4 | -8.9207 | -60.76625 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e3fab08-0242-32de-9711-15e51b88dcaf | -7.44517 | -67.7362 | 2025-08-13 05:29:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 396819d1-02f9-37fb-b8c4-803ddab828c3 | -8.56858 | -54.71651 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6128ff-9e03-356d-8878-585b361d0b1c | -11.90663 | -52.53519 | 2025-08-13 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a96fc806-edf9-3854-9013-f21f765eb5dd | -9.37894 | -61.52574 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3871fc0-99b3-36cd-a477-5a85a2827bbc | -12.3662 | -59.84132 | 2025-08-13 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc844a9b-1088-30f6-92a4-85eaae7c08a1 | -7.27262 | -60.62341 | 2025-08-13 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2597fad-49c6-32b6-90ae-0128d70fcb99 | -10.47478 | -61.32 | 2025-08-13 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c101846-a507-3379-b0a8-32d882fbe6cc | -9.38175 | -61.52988 | 2025-08-13 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fde2e725-36b1-3cc4-b414-0572e306a1b1 | -7.81857 | -61.32625 | 2025-08-13 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a7930dd-80d5-33f0-b3cd-a58d6d4746b6 | -8.57427 | -54.71152 | 2025-08-13 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f43ced2a-3092-347a-bf89-0d640fc31855 | -9.56274 | -62.72331 | 2025-08-13 05:29:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README33.md)
