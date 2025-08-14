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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f4a1e90-1312-3c4f-8486-0a02b84b7598 | -5.74999 | -59.87786 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aab205d-4cf6-308c-8c56-0f3757b341f1 | -6.9149 | -59.13649 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b614ced9-0ca9-33e8-8941-76bdc9bd1b85 | -5.74263 | -59.87291 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fffa64a-b3ca-300b-a5f8-87aefbaeb248 | -6.90495 | -59.13477 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ff73a137-76ac-3295-a5cf-2603a58c5bfe | -7.52617 | -61.38536 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fa2d2ba-d8d6-311a-9953-d478ed2bcd7a | -8.74175 | -44.00933 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce08ce84-b85d-3b08-9007-834b88b56172 | -5.7466 | -59.89782 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c59c6b3-0081-31ce-8ce5-35dddd3a77fa | -6.08461 | -59.94936 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1c85dad9-52ff-3b1d-ae68-7164dd920940 | -7.12379 | -59.63617 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d38a2d37-97aa-3ee7-9ff4-b2a23eda1180 | -6.48479 | -55.89974 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8e9e2fb-cf53-3a23-b0a8-1d452ad5cc35 | -7.24195 | -57.64797 | 2025-08-14 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6281a67c-6305-34ce-bc2f-a3af8856d7fe | -7.25938 | -59.99319 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f1fa715-0f47-3ce7-9a9c-443610023c0d | -7.12486 | -59.63013 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af1a1e88-2353-30f6-b9fa-91f197e4a3ca | -8.53067 | -43.32492 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c6c3e5b8-edea-3de2-8c24-fffd2f45fd4d | -6.87512 | -59.15856 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 719ae734-5e3f-3dff-b1a8-aac4b12d4294 | -5.75038 | -59.89116 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0300637b-66db-3da4-b419-804cb986cfbc | -6.92388 | -59.14383 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93570bad-7d44-3890-b8cb-49b766f2fe3f | -7.3259 | -60.62932 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f496d40-5110-30a2-a189-3b20318253da | -7.25358 | -59.99543 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b6ec4e7-a855-3182-9bb6-5db3a0e978a9 | -7.31634 | -60.62008 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 641a4976-a8b1-3011-bf91-50a1e670056d | -7.23378 | -57.64204 | 2025-08-14 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9514568d-f4f0-37ea-af63-dcc9a0b23237 | -8.7268 | -44.01222 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c6f4b00-6894-3d43-9dd0-a35e4b692a65 | -7.33202 | -60.62669 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e0fd2e2-1422-3cf9-92b8-e92c3f947d42 | -6.09111 | -59.94365 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f46aaf72-185b-3b24-bf89-03fdd1350602 | -7.07656 | -59.20789 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e4d31d3-7370-3223-82ff-506bc8214bb2 | -6.88804 | -59.14346 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b88dc7f4-14a0-3546-b5b3-7068c9b554ae | -8.7458 | -44.01514 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4440922d-e60b-365a-935d-2783bb5b0712 | -7.26276 | -60.63487 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97c2cb96-640b-3b0e-9562-9ba121c35aad | -7.25732 | -60.63373 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb3272c8-95f4-32ac-8b53-7cb7e2ffa800 | -6.93604 | -59.63121 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edd8fd2a-ec59-3807-969e-3b9041563b31 | -7.14206 | -59.65249 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bd0707a-9410-39b1-bcec-3ea40f7b44e0 | -6.11236 | -59.91627 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 998519d1-27e8-3229-951e-31a18dec7855 | -6.64798 | -59.07824 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58c7e058-f023-3ddd-90fb-76bd1f16f615 | -7.12612 | -59.41691 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcf13f19-2bbb-3cba-bc02-2a01f27ab88a | -6.94119 | -59.63209 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdff6d96-80b5-3ab4-afb9-9584f1538c29 | -7.25299 | -59.99868 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0674bb6-a0b0-3219-842f-2870069a05a6 | -7.26887 | -60.63226 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30df3fa0-be24-36d7-bfd3-b5942c40dda6 | -7.10372 | -56.77198 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b779f17c-d45f-3de9-bd2b-387f9a37c00e | -6.88136 | -59.88197 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54fd631c-4ac8-3f70-8178-d2ee3024d284 | -6.11121 | -59.92285 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13874481-3b4d-315c-a3d6-0b8d57b0a825 | -7.25823 | -59.99961 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d87bc2-5a14-3def-9c90-3c06bae1da6f | -6.90595 | -59.12902 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3681f7b-3ff0-3928-b47b-e36d4db0d69c | -8.73492 | -44.02369 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30588d68-b5bf-3ccd-922f-cb76a32cf27a | -7.12734 | -60.1305 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8f4e49b-ca33-3e20-a3de-be87d7d10844 | -7.26405 | -59.9973 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70d5c628-239b-3c83-8976-ebee67794b56 | -6.90395 | -59.14049 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| db1c48b0-ba17-3a7e-8363-7ddc13e2303d | -6.87115 | -59.15192 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 42c73c69-51c0-31f9-a096-1b71b12aa652 | -7.33747 | -60.6277 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afbcb85b-340b-3b96-b842-0119c84ddfcf | -7.52688 | -61.3815 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcd4c00a-22b6-3d49-b49a-179df13c70e0 | -5.74886 | -59.88451 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e613335-aeb2-3c81-8945-3a152aed1912 | -8.7451 | -44.02018 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9ce7f86-1022-3d83-b663-6af3a96bddbc | -7.12432 | -59.63315 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b05557c-766c-330e-8029-010d8904c3c6 | -7.08793 | -60.02167 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 937fe08c-b2c6-3127-af95-d0f138ea006c | -8.25508 | -45.06128 | 2025-08-14 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d049a438-2503-3932-a7d0-9aba59006dad | -5.74739 | -59.87703 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dbe19d7-033c-38fd-b90e-ea0a1ed5b4fd | -7.23301 | -57.64648 | 2025-08-14 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67abaf29-0687-36d7-b5d2-f91b0b8edb72 | -7.53115 | -61.39034 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14d46474-8e6c-33b6-9c11-976f419a8c81 | -6.90098 | -59.12811 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7a7f00b-42df-32df-96f5-a832d9de79bc | -7.13323 | -60.12814 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07804842-7d64-3722-9bcf-90e85d33b455 | -10.53615 | -42.5523 | 2025-08-14 04:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 09471e0a-bb16-3a89-b970-1a3e7a5e66d6 | -8.80684 | -52.06362 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2332b2a1-f005-32e6-baff-96278016e124 | -7.11773 | -59.4165 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8ac091d-bcf0-30e1-a8d1-f0f9af850e29 | -6.52991 | -56.20219 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef202565-2122-3940-a663-f036e2a25d60 | -6.88608 | -59.15464 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0eed20eb-8db3-3050-ae2f-02af6bcf52c3 | -6.8801 | -59.15946 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0ecfb3fd-6254-3974-8fc5-710ba93102d5 | -6.89401 | -59.13871 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c418e35c-ed92-3460-bf9f-0a5eb221367c | -8.5181 | -43.30571 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ede8184b-0669-354a-b43a-5ec5f5ea0193 | -7.11551 | -59.41797 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c09b0161-ea30-369b-b85f-d68725657e13 | -6.09587 | -59.94777 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3578023e-0ba3-3802-8954-d1e79014ba52 | -7.31633 | -60.61887 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a095305-9a9d-36ea-b83c-6a8ef439cea4 | -8.80022 | -52.04094 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c3a4912-4913-3cac-8a2e-e916378fee3c | -8.73561 | -44.01866 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68f0c19c-89ff-3e4d-bd1a-91f6dc714914 | -5.75274 | -59.87786 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8db11c90-6f13-37ba-9d43-88dc00683473 | -6.09227 | -59.93703 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69f28e74-2ebb-3c8e-8363-276103bbcb0e | -7.13695 | -59.65146 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acb636f5-bcaf-3d9d-b1a1-2ce288e1b301 | -6.87713 | -59.14716 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c3f3967-dd3f-3c9d-947d-7bf6706b04bb | -7.53188 | -61.38641 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4202ccaa-3160-3a5a-b64c-b2ddc4b3c6f2 | -6.88508 | -59.16033 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| dd4693b3-0bc7-3b0c-a9a9-6b4c65290a1a | -7.11974 | -59.6292 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cf4ddc7-5cdf-355f-bdbf-270e85a2bbd5 | -7.12852 | -60.12395 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9acdf311-0fc8-3c80-a401-ab87750e276e | -6.07461 | -59.94379 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ee9023e-20f9-308b-be85-d60392ff20cb | -6.10471 | -59.9287 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35de20b6-a529-30e1-b12d-0aabad9b97c3 | -5.7452 | -59.87374 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 257a7666-395c-38e0-9f70-84067fa02316 | -6.87414 | -59.13501 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fee2b79f-e929-3679-bb30-a66c5e5dd9cc | -7.25414 | -59.99229 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b71969b-33c0-3b22-8728-5309364135d4 | -7.23552 | -60.00556 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bc493cf-f5b5-32b0-9850-c9bc8633011d | -7.09208 | -60.02895 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87f513db-3823-36c3-8f4e-9d6a84896548 | -5.74562 | -59.88699 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fffde2c0-7e2b-38da-bd2a-913b84d2654f | -7.46023 | -59.89263 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 985adc19-b469-33b6-8948-4bee93dce5ab | -5.75514 | -59.89532 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14c4f44a-de36-35a8-8c1a-0b4e23da5a9a | -6.90198 | -59.15178 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| cf926067-b206-3693-9b0e-1f62993768cc | -7.25882 | -59.99633 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cb752a0-86e0-3cde-9fae-2d8add519b4e | -7.23666 | -59.99929 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b5a81a0-9687-34d1-b715-dd42ab0f7cd1 | -7.3266 | -60.62451 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa7701f9-0d20-3167-8bc6-463460e0b05d | -8.51888 | -43.3 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 02b7f00c-72b7-304d-881e-58e6f61e1223 | -5.74444 | -59.89362 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b39c849-eaa9-337d-8f8f-fb4a39f6c127 | -7.07261 | -59.20116 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1525c5a9-c813-3b06-82c5-90c48f2659e8 | -7.33268 | -60.62193 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7341089-a3bb-3cbc-a899-59e96f941662 | -6.92844 | -59.14555 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46229140-643a-3d0d-a3ac-df38353e748e | -8.74035 | -44.01941 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README20.md)
