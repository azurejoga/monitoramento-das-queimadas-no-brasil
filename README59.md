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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98cd9408-5982-34ff-9afa-bd0b5e2579c1 | -7.10542 | -49.15016 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4327a4a7-1415-32c4-bbbe-d0b4423868d7 | -7.10493 | -49.17503 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bd88111-bca4-357f-ad29-23fc128affba | -7.10264 | -49.14616 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aed6e10-83ae-3257-a8c9-5bc09cb69510 | -7.10215 | -49.17103 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1c1292d-d6aa-3932-8a8f-795369e1bc36 | -7.10161 | -49.17451 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2f943fd-1419-306c-84ee-984533e6323b | -7.09544 | -49.1486 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e9cda14-3914-3dae-a00b-7dfa63acb114 | -7.08762 | -49.13673 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7301b4a7-1dde-3940-9d0e-f2fed77f9375 | -7.08708 | -49.14021 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd8602bf-3ea3-3f04-a975-d04178ecd85d | -7.08375 | -49.13969 | 2024-10-25 04:38:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a92bb450-e458-3933-b0f4-1fa088345bb8 | -7.82151 | -49.82643 | 2024-10-25 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97f2ccc7-14a7-3946-8172-d98dd268e8cf | -7.82096 | -49.82991 | 2024-10-25 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 019cb478-dc38-3111-81c8-cf3ca21bd6d4 | -7.79203 | -49.5219 | 2024-10-25 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c3952f8-c00a-3921-a43c-4f16bf760c89 | -7.78871 | -49.52137 | 2024-10-25 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7cdb897-9b87-3053-a88a-28294aeca0fa | -7.59448 | -49.61188 | 2024-10-25 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c504c31-0575-30c3-bd5a-4c3b58d2d7d1 | -7.59393 | -49.61536 | 2024-10-25 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fe292b1-9bd5-3a40-ac90-b2f8a4a09967 | -7.46833 | -49.85565 | 2024-10-25 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 333c7db2-8a07-3688-a8d0-f981995d742a | -7.46501 | -49.85513 | 2024-10-25 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 793f08b6-d23a-3f58-89bd-dba4f399c31f | -7.3392 | -49.58197 | 2024-10-25 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cac1629-edd9-37c6-8ea6-204d46d09816 | -7.31982 | -49.57534 | 2024-10-25 04:38:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1e3d75a-bc06-37c2-9062-73c9ced01e32 | -7.2682 | -49.83782 | 2024-10-25 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00e67695-dcf8-3d68-86f7-afacbb251cd2 | -7.16474 | -49.56871 | 2024-10-25 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0190067b-a4a9-3689-9354-0c98648bd433 | -7.03424 | -49.28155 | 2024-10-25 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00d576b4-7a23-3b4c-90eb-1f06be616425 | -7.0337 | -49.28501 | 2024-10-25 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4c01fc6-d6b0-3ab3-aea2-6110bbe4358a | -7.03092 | -49.28103 | 2024-10-25 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cde8678-1cba-392c-ab10-e3ffd356c65a | -7.02983 | -49.28796 | 2024-10-25 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4865970-3d37-3f88-900c-398c309e6cc3 | -7.0276 | -49.28051 | 2024-10-25 04:38:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a590f663-71ee-3248-86f5-e49af438a35b | -8.97088 | -50.17725 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 652a6f75-cf0a-36a2-b819-3868510b129f | -8.91384 | -50.17169 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c06b2ee-3c65-331f-bf30-81e7ce78505e | -8.81601 | -49.63429 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b80ec300-451c-3972-8743-6dff63d65487 | -8.71978 | -49.40362 | 2024-10-25 04:38:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91e81d60-6290-329d-acc8-8ff0b6c5e56e | -8.6815 | -50.03776 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a7f78301-8fee-374d-906f-1a6d40c61a6c | -8.68095 | -50.04125 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a64cf02-987b-30b4-969f-290a9710c24b | -8.67873 | -50.03374 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24c129c8-512f-3dc7-ad76-5130128e3deb | -8.54771 | -49.57363 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 894844f0-048a-3b45-b1ec-7dd9ecd183d5 | -8.54489 | -49.55182 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e6a0f69-cc34-3870-a83d-aefff983f531 | -8.54211 | -49.54781 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30c66db5-fb28-35fb-a6ae-68875dcbddac | -8.54157 | -49.5513 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ab4e996-b16a-3995-b28b-2f4416bd1aa7 | -8.54047 | -49.55827 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8c463ce-7885-3810-87f3-0155897fec4c | -8.53879 | -49.54728 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f8f25e3f-cf03-3dde-96a9-b574d512ba64 | -8.46101 | -49.43481 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89897341-c475-3127-9f42-9d95e24b5d1f | -8.46047 | -49.4383 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f3b9f49-c934-37a5-813c-7526b51fa920 | -8.41609 | -50.08864 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe4ef713-f121-3b73-baf4-4f87dfc8a3d7 | -8.41553 | -50.09213 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6c49660-e56f-3b84-9057-eeef2e4714d3 | -8.35272 | -49.63245 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 710cd196-cfbf-3236-bfa8-030c28d54a61 | -8.23614 | -49.7705 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf54dec3-f28e-3e4b-b19b-8f792af155db | -8.09727 | -49.38469 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e235028-accd-38a3-bb57-c8acb57a5372 | -8.06457 | -49.37595 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10b9d593-dbc5-340a-8c92-96750e4866f0 | -8.06402 | -49.37944 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf707e92-6ea2-314a-b398-59125552a189 | -8.02693 | -49.63766 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34bb1b81-94ec-3b9a-b224-b1fe6eaa433a | -8.02415 | -49.63365 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c0f87b82-2f7e-396b-ae11-22be18cf638e | -8.02028 | -49.63661 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 938a093f-6ee1-3fbe-822f-141c1a8db813 | -8.01696 | -49.63609 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e923a8ef-5553-3925-af69-30bd6325f17d | -9.43884 | -48.88585 | 2024-10-25 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1242e4a-6c16-377d-a55a-af93361c02e7 | -8.98084 | -48.81902 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 91552b72-fe57-34fe-b684-27ee619a89a2 | -8.98029 | -48.82259 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d1c032d-6ae5-39af-bcd9-5c9929e4b904 | -8.97638 | -48.82562 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a527806d-5d23-3fec-bfc4-641b678aa953 | -8.67417 | -49.09078 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be87d99d-89a8-38f0-9443-a7b10c8198f3 | -8.67362 | -49.09431 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22aea361-4aa2-3777-bffb-3da73e2d4738 | -8.67307 | -49.09783 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 048d00f0-2a9d-3772-87e4-894d2908b1d9 | -8.58479 | -49.23192 | 2024-10-25 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ac80140-92d0-30fb-9750-64293a61184b | -8.57812 | -49.23087 | 2024-10-25 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0ec1adf-65f4-3bf4-a907-15d0d0b09f46 | -8.34624 | -48.93471 | 2024-10-25 04:38:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4913292a-4af7-3ea7-b72a-7a88585be8fe | -9.43829 | -48.88942 | 2024-10-25 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec50fdea-6a66-3765-b04a-acafa1c4acdb | -9.43548 | -48.8853 | 2024-10-25 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85eb7817-4d6b-375b-92d9-276f7e2cd645 | -9.43212 | -48.88476 | 2024-10-25 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e07628af-271b-3420-a92a-10678cb8dace | -8.97749 | -48.81849 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a3cfefb-348a-366d-a725-92d007fd6995 | -8.97693 | -48.82206 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71162d2a-c984-3c44-bb92-fab915c5fd04 | -8.97032 | -50.18074 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b81baf39-8042-3d62-ac09-3a9cb07a4906 | -8.967 | -50.18021 | 2024-10-25 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a1d1a6f-b28d-3e71-963c-757ce4393d9b | -8.91051 | -50.17116 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2185d31-03d4-3d49-a32d-1ec412b52ca5 | -8.89021 | -48.82674 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65c1b0b3-1552-3273-bad7-ed26f76147ae | -8.88966 | -48.83033 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbfcf3e7-708c-3e35-bf5f-cefc5a1552b9 | -8.8863 | -48.8298 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9263b461-3d4a-3c91-87da-60e364d3a370 | -8.75846 | -49.65379 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 350a62db-3881-3b6f-9f8d-92f781cb307f | -8.75427 | -49.78897 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e90eceab-6fde-3674-ba95-d87efbc3212c | -8.75095 | -49.78844 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2b4bdc33-2761-3d3a-ac67-e9425bd88d7c | -8.68205 | -50.03427 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 80a27e12-63de-3f07-8e64-1a442f4334b5 | -8.67751 | -49.09131 | 2024-10-25 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7d22247-fa05-3583-bf98-aac71ba5597b | -8.582 | -49.22788 | 2024-10-25 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2bade2f1-a2aa-31a6-b5f4-25f6b1967379 | -8.58145 | -49.23139 | 2024-10-25 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d2dc8b6-60a6-3cbc-b7d1-9d5ab3d23bc1 | -8.57867 | -49.22736 | 2024-10-25 04:38:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c29bb9f8-945b-308b-853a-2d8b3f5fe63f | -8.55154 | -49.54921 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63b340a9-f7d6-3a0e-9b9d-1afadeba4d02 | -8.53824 | -49.55077 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4622432b-f31a-31ae-8985-848f84fd3bf9 | -8.5377 | -49.55426 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b04ebc06-9a1d-388f-8c15-774a5ccacdcd | -8.52402 | -50.02717 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f418a1a-cc98-3767-a2b3-cb1ac1221c9f | -8.5207 | -50.02664 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b53202bd-e9f7-3c05-bd87-9bba6d3685b3 | -8.46379 | -49.43882 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f62d0298-ba20-34cf-9f39-b68167ca7707 | -8.35993 | -50.04065 | 2024-10-25 04:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ebe3b7b-7262-3613-b7ca-e0e9599425de | -8.13185 | -49.78981 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e73fd269-cab3-3262-81eb-d1f65da36522 | -8.1313 | -49.7933 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27b2757f-5cfd-3895-a6d0-e061905b424e | -8.12798 | -49.79277 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe5bf221-4106-351a-8e6e-a81058c27aec | -8.0607 | -49.37892 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 855b894b-cf8f-35ea-b028-59502b54cf78 | -8.02361 | -49.63713 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afc227aa-43eb-3772-a9d3-d9f356095fe1 | -8.01364 | -49.63556 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92eb4c72-a5fa-3ffd-93bd-d7f92d77fca5 | -8.01032 | -49.63503 | 2024-10-25 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f32126f-19ed-3d56-9503-070ba9d3bf05 | -9.94451 | -49.81247 | 2024-10-25 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 357bde4d-a9ad-3a79-92f8-c2e263e729ef | -9.94119 | -49.81194 | 2024-10-25 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 243c8f1c-0042-3ab3-8c8b-7adf8d4e2ac1 | -9.63362 | -49.63751 | 2024-10-25 04:38:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6022b8d-8280-38ea-a014-9be0798bf7cb | -9.58162 | -49.64737 | 2024-10-25 04:38:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ec7d9e8-fcd8-3bfe-b33d-d2b7649375f7 | -9.82571 | -48.98188 | 2024-10-25 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README60.md)
