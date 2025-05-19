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
| 5b1fb310-e04b-3a23-9af0-b931f9bfabfe | -12.4608 | -57.2079 | 2025-05-19 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 139.9 |
| fe1befb9-82fc-366c-8480-467378be032d | -12.461 | -57.1879 | 2025-05-19 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 499.5 |
| b3f07698-dee2-3893-b3a9-831143b082fe | -12.48 | -57.1863 | 2025-05-19 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 229.4 |
| 64ecdac2-bc13-33ae-8801-5226c8b702c6 | -12.461 | -57.1879 | 2025-05-19 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 440.3 |
| b483c606-9520-37cb-9e01-642012f9cd40 | -12.4613 | -57.1679 | 2025-05-19 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 4809aaf2-2f76-3e15-ac24-2604487f91a9 | -12.4608 | -57.2079 | 2025-05-19 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 190.8 |
| a5401be3-8d5f-3a02-8a32-f2346f3c9cc5 | -12.461 | -57.1879 | 2025-05-19 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 544.3 |
| f1f58d88-fd95-3d03-a7e3-4f5d109f6b97 | -12.4613 | -57.1679 | 2025-05-19 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 215f257c-90ce-30ae-91a5-c0aee6d1483a | -12.4608 | -57.2079 | 2025-05-19 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 209.1 |
| 9d9f27d2-e143-3a33-afad-77203cd576ea | -12.48 | -57.1863 | 2025-05-19 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 215.5 |
| d3b2a811-c5be-3f78-8baf-925412a03529 | -12.4608 | -57.2079 | 2025-05-19 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 283cd138-7f7a-3b83-9b65-567307ebd14a | -12.48 | -57.1863 | 2025-05-19 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 257.2 |
| ba95c4e5-477b-3fc4-8353-2c7746e9ebef | -12.461 | -57.1879 | 2025-05-19 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 569.9 |
| aa2cdbb8-c07c-3493-995a-1c23cc3fd34f | -12.4613 | -57.1679 | 2025-05-19 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 7553a08b-7d15-3445-8510-8eef7a393501 | -12.4608 | -57.2079 | 2025-05-19 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| b19bd72f-53f5-3435-8f0d-60b7c2484491 | -12.48 | -57.1863 | 2025-05-19 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 239.9 |
| 5da506df-8e6d-38e5-a437-9464813deb95 | -11.4273 | -44.7011 | 2025-05-19 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 8259532d-ff86-33b9-9419-23b30bbb83cf | -12.461 | -57.1879 | 2025-05-19 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 557.1 |
| 16def448-c3ac-38b3-accb-82705097ccbb | -12.4608 | -57.2079 | 2025-05-19 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 1f5558bc-d9e6-3cd4-99f6-93da209bf677 | -12.4613 | -57.1679 | 2025-05-19 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 946e9479-d62e-38ed-b76a-b11a9f1eaa6b | -12.48 | -57.1863 | 2025-05-19 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 294.4 |
| 3f96cc34-e756-312a-af9f-c6249d9b7ddc | -11.4082 | -44.7039 | 2025-05-19 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 07581b19-37b6-3119-adb2-e6ed489ccfb9 | -11.4273 | -44.7011 | 2025-05-19 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c5e0111a-e3db-36ee-a74a-293e72b516a6 | -12.461 | -57.1879 | 2025-05-19 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 374.9 |
| 46f26e48-11ce-3fc7-b9ee-df03629b4bfc | -14.4075 | -46.0491 | 2025-05-19 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 5294b174-5af8-3c4a-a145-5d2424c6fee9 | -11.4273 | -44.7011 | 2025-05-19 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 83a2706d-6b97-3bc3-809d-e50dd680774f | -12.461 | -57.1879 | 2025-05-19 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 435.5 |
| 8749b9e8-fecb-33f1-bd05-bb23f3fbf302 | -12.4608 | -57.2079 | 2025-05-19 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| df946554-b359-3273-b468-155f1a213f12 | -11.4082 | -44.7039 | 2025-05-19 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 7eb6097f-0761-37fe-9dba-19fa7bbf05b5 | -12.48 | -57.1863 | 2025-05-19 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 367.0 |
| 5344b3b7-814d-34d9-90c0-5c18a7404110 | -11.4082 | -44.7039 | 2025-05-19 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 255.8 |
| 6b9687c3-014a-376b-8ba9-bff7fa66167d | -12.48 | -57.1863 | 2025-05-19 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 346.1 |
| 4a62bab5-68b0-3993-b1aa-de6f95948d78 | -12.4613 | -57.1679 | 2025-05-19 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 9136b89f-9a28-3fca-b45d-35326b4fa5e2 | -12.4608 | -57.2079 | 2025-05-19 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| a671aa8f-7ebc-30a0-ac06-3dd11c0f9c0a | -11.4273 | -44.7011 | 2025-05-19 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 4b456f3a-0c8a-34c0-9a1e-3fb14f03888d | -12.461 | -57.1879 | 2025-05-19 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 358.4 |
| 7ce01104-4b28-31f5-b8d8-9a7549012bbc | -11.4269 | -44.7243 | 2025-05-19 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c918574d-6df0-3627-92c4-5f15228595e7 | -12.4608 | -57.2079 | 2025-05-19 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 10aeea83-bd13-3e13-ada3-c54d23f729c5 | -12.48 | -57.1863 | 2025-05-19 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 391.2 |
| d1fbf574-4374-3a2a-b3b6-00a6607455bf | -11.4273 | -44.7011 | 2025-05-19 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 216.0 |
| 212a141f-b600-374a-b4e7-b390e6d8a1ce | -11.4082 | -44.7039 | 2025-05-19 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 278.5 |
| 9342a110-adc7-3036-ae8e-0198a116a4a7 | -12.461 | -57.1879 | 2025-05-19 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 373.9 |
| 713213a9-1571-3fa7-982d-f5e5513dc2c1 | -11.4273 | -44.7011 | 2025-05-19 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 353.0 |
| f12633ab-791c-35f7-ac13-61a694b11be6 | -12.461 | -57.1879 | 2025-05-19 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 356.9 |
| 44713f46-00ea-388c-bf16-ad86eda1ad9c | -12.4608 | -57.2079 | 2025-05-19 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |
| d5e2b639-f45f-3aea-89f3-1e6ea9a6286a | -12.48 | -57.1863 | 2025-05-19 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 364.3 |
| ef99cb68-b42d-31bb-b60c-bbc4f3840b26 | -11.4269 | -44.7243 | 2025-05-19 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 31dd3a74-7eba-3364-aa83-534293578829 | -12.4613 | -57.1679 | 2025-05-19 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 57512eb7-6fe3-333e-b9c6-2aac5575bcc7 | -11.4082 | -44.7039 | 2025-05-19 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 49700adc-8bc2-375f-b3cc-0ce86859011b | -11.4269 | -44.7243 | 2025-05-19 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a65f8ea7-8dd5-3f9c-8c00-86c4f47da58d | -7.1575 | -47.2771 | 2025-05-19 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 488afb5c-4e5c-3793-930a-74670c358b9e | -12.461 | -57.1879 | 2025-05-19 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 304.4 |
| ee3b18f4-4726-3185-83de-f5c7213ca6b6 | -11.4082 | -44.7039 | 2025-05-19 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 342.9 |
| aa33a922-cb6f-331f-abe6-63f0ac32af62 | -12.4608 | -57.2079 | 2025-05-19 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| bda7c193-034c-3a16-ae94-9444da36766c | -11.4273 | -44.7011 | 2025-05-19 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 8a75416d-e124-3ebe-8642-25bf81dee68b | -12.48 | -57.1863 | 2025-05-19 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 369.6 |
| 81ff4071-4de6-3e07-976a-3bed9f098f0b | -11.4273 | -44.7011 | 2025-05-19 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| d0656be9-8388-3159-86cb-6891fab18d4f | -12.4608 | -57.2079 | 2025-05-19 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| cbb0764b-8db3-357c-bbb0-ba72f12ea228 | -13.2126 | -53.6085 | 2025-05-19 14:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 39204b7c-2d19-38e9-9730-9b89e419ed1b | -14.4075 | -46.0491 | 2025-05-19 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4d189264-1d78-3d45-9da4-e488e76e8f3c | -12.48 | -57.1863 | 2025-05-19 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 425.1 |
| a0fe1237-083a-3d18-998e-edef07718815 | -12.461 | -57.1879 | 2025-05-19 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 319.7 |
| e2b3f847-0554-39fa-a54e-db90ee877f56 | -17.0616 | -45.0191 | 2025-05-19 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| dded4733-403a-328f-ae97-d0b64a3e8fcf | -12.3515 | -49.9833 | 2025-05-19 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 40170da9-57e0-39f5-b63d-196013c0cdeb | -11.4273 | -44.7011 | 2025-05-19 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 325.8 |
| 669841e7-2795-3b9a-b922-1996f26e7c4d | -12.48 | -57.1863 | 2025-05-19 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 394.1 |
| 9253cda0-0f21-3b15-a367-0f77819cd3af | -14.4075 | -46.0491 | 2025-05-19 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6202d395-044c-3f30-b036-2a08aaf66072 | -7.1575 | -47.2771 | 2025-05-19 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 42631436-0102-32e2-b70c-f9c961d6ed55 | -11.4082 | -44.7039 | 2025-05-19 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 243.9 |
| cd837bfd-9eab-3f3b-8cf6-5f4d55ccfd38 | -12.4608 | -57.2079 | 2025-05-19 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| dcb3e844-569d-3cd7-a114-6c6241613d58 | -12.461 | -57.1879 | 2025-05-19 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 287.2 |
| c76e9f1d-4d71-3bf1-95ba-70a2dd2ad54b | -17.0616 | -45.0191 | 2025-05-19 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 116.9 |
| dad45408-f989-390f-8e9b-bf7467d6c1a0 | -11.4269 | -44.7243 | 2025-05-19 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 79da2dc0-b9e5-3862-a007-9a521fe6dc6b | -12.4613 | -57.1679 | 2025-05-19 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 427990fc-bbab-3ca2-9728-ceae8ed1aa48 | -10.4917 | -49.8744 | 2025-05-19 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c0e33ff8-939b-375e-9edf-a7436f2605ed | -12.3515 | -49.9833 | 2025-05-19 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d3610add-e83f-3538-9357-037162d542f8 | -13.2126 | -53.6085 | 2025-05-19 14:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7e2d4441-900f-38e5-976e-ee5dc1055a9a | -11.4269 | -44.7243 | 2025-05-19 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 83a2532b-8908-3749-a04d-2b2a68486d1c | -17.0616 | -45.0191 | 2025-05-19 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 39d87cdd-ae9c-39a6-b83b-49f4c19a6226 | -7.1575 | -47.2771 | 2025-05-19 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7388eab0-e795-3da5-940f-b3dd448520a7 | -12.461 | -57.1879 | 2025-05-19 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 243.9 |
| 2e9d284e-a857-3442-90ac-21e9082d8294 | -14.0136 | -55.1321 | 2025-05-19 14:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| febed0ec-e111-3154-a548-36cab6a6a22d | -14.0328 | -55.13 | 2025-05-19 14:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 140.7 |
| a6b22965-0eb2-3de3-8ae2-cecd997abcee | -12.48 | -57.1863 | 2025-05-19 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 312.3 |
| f521fdf4-6ea6-39e6-8468-40bb419f7729 | -12.4608 | -57.2079 | 2025-05-19 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| a176eeb6-0809-33f9-b43d-6578be61d459 | -12.48 | -57.1863 | 2025-05-19 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 348.9 |
| b62b60c6-97e2-3537-9d77-8a31f1ebaee0 | -7.1575 | -47.2771 | 2025-05-19 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 84b61c54-0401-3a11-a4cb-f1d16ebb2023 | -12.461 | -57.1879 | 2025-05-19 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 255.9 |
| aa664aaa-7259-39c6-8c7c-f11f5edcbf47 | -14.0328 | -55.13 | 2025-05-19 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 328.7 |
| 5cfb20ff-cb3d-3dd5-8bbb-bcae6b70fdc8 | -14.0139 | -55.1115 | 2025-05-19 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 95005976-621f-3be4-afe1-227facea2e1d | -12.4608 | -57.2079 | 2025-05-19 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| bb5fe577-5409-3d19-8ecc-32b83c32cf86 | -11.4273 | -44.7011 | 2025-05-19 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 350.4 |
| a66b04b9-9c86-332e-9fd6-9482e71efd04 | -14.0136 | -55.1321 | 2025-05-19 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 6760ee1d-aa6d-3dc3-b03f-7a451d37bc6b | -13.2126 | -53.6085 | 2025-05-19 14:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ba6e27ea-37e0-3a60-9cbd-75e25f6e8dd6 | -12.3515 | -49.9833 | 2025-05-19 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 08966195-9fd4-39ab-a32c-62dc5e5f5591 | -12.461 | -57.1879 | 2025-05-19 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 196.7 |
| 027b8afd-9bd0-3472-a376-a2bc7e24a070 | -11.4082 | -44.7039 | 2025-05-19 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 401.7 |
| 2d1ae259-e9c4-38c4-ae9c-f860c98730d4 | -14.0139 | -55.1115 | 2025-05-19 14:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c0065a18-74c9-31a3-a166-1733a45842c6 | -13.2126 | -53.6085 | 2025-05-19 14:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7a799d46-e346-31c1-aaac-bbf0fa294c3c | -7.1575 | -47.2771 | 2025-05-19 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |


[Clique aqui para ver as próximas entradas](README6.md)
