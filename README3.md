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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a184d502-c4bb-322d-b90c-10434cf7b49f | -7.7005 | -47.2976 | 2025-07-20 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 83b280e0-26f5-398c-8d92-86cfa32ff929 | -10.9624 | -45.09 | 2025-07-20 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4ab4209f-a182-38e5-8e2c-094167949038 | -10.962 | -45.113 | 2025-07-20 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 5db32618-29fa-39cf-984b-14cbc7c814ea | -10.9811 | -45.1104 | 2025-07-20 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 79db0c42-a4c1-310c-8ba4-c725a65244b4 | -10.9624 | -45.09 | 2025-07-20 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4a0fd089-e50d-3cf5-9327-3b3746de4dfb | -10.707 | -46.7805 | 2025-07-20 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 237a1992-644b-3f43-90e3-f107fcd5a4ca | -10.9815 | -45.0874 | 2025-07-20 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6434c61e-e1c3-3d7b-a29b-e9dbb78407b6 | -10.962 | -45.113 | 2025-07-20 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| d5b9d54d-2bc6-332e-9e34-92dec91003a1 | -10.6686 | -46.8077 | 2025-07-20 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ef60ed10-3a6f-3064-9d3b-a5d35542b11e | -10.9811 | -45.1104 | 2025-07-20 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 53a42a57-287a-3daf-8545-18251dc45dd7 | -10.6876 | -46.8053 | 2025-07-20 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| d0be09b4-4f11-37b7-b7e9-ca117216f92a | -3.042 | -47.8607 | 2025-07-20 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 7619d028-2947-3343-b61b-4f7b41e89c42 | -10.688 | -46.7829 | 2025-07-20 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 05ea03d1-5efd-36ed-b23d-7d05e3d19c3a | -14.2779 | -58.2466 | 2025-07-20 02:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 7a0e4bd3-58e3-3b21-a8fd-5ea87b243056 | -10.6876 | -46.8053 | 2025-07-20 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 7de1eb00-a4aa-3c0a-8ceb-12364f5bcbe1 | -3.042 | -47.8607 | 2025-07-20 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 5531cd60-d20d-3d1c-994e-64d502934643 | -14.2588 | -58.2483 | 2025-07-20 02:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| a8025445-11a9-3834-84d1-35cabac1b1b4 | -9.5343 | -40.3282 | 2025-07-20 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 3bf6e441-414d-3c4d-99ca-b2b31b845c4f | -7.7005 | -47.2976 | 2025-07-20 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 89a7f0c6-7e31-30e1-bc2f-ac10dc40a117 | -3.0235 | -47.8613 | 2025-07-20 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 777ff5d5-6bc9-3c46-b14e-20eaba7fd1f5 | -10.707 | -46.7805 | 2025-07-20 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| c5785e85-60f1-3f9c-ac52-474b28b22761 | -10.6686 | -46.8077 | 2025-07-20 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1e2db113-a671-3487-ae62-b132b782980f | -10.688 | -46.7829 | 2025-07-20 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| b212173b-9b3c-3636-a299-7931c0784020 | -10.9815 | -45.0874 | 2025-07-20 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 47da0bda-9da5-396f-81c2-7c8412279d79 | -10.962 | -45.113 | 2025-07-20 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0b3811e8-251b-37c2-8259-7f23a2f29e4d | -10.9624 | -45.09 | 2025-07-20 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c4781da3-27c8-3272-801a-1eeb95a16cc0 | -10.9811 | -45.1104 | 2025-07-20 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 94fb3832-dcbe-325e-85b1-d5f702add006 | -14.2588 | -58.2483 | 2025-07-20 02:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 17c54ee7-11f6-3757-bed3-36ec04a280e4 | -7.7005 | -47.2976 | 2025-07-20 02:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ee05f5b2-0554-3cac-94df-37479af8ce7e | -10.688 | -46.7829 | 2025-07-20 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 178b2941-cf55-3496-b476-e43223333442 | -10.6876 | -46.8053 | 2025-07-20 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ddc26b0a-8423-38c7-ba50-f7fd72a07935 | -9.5343 | -40.3282 | 2025-07-20 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 5b14abfb-f486-38ad-b1b4-062b13fc36ba | -10.962 | -45.113 | 2025-07-20 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| d262a25b-2696-3d93-a75e-44aa14ddb802 | -10.9811 | -45.1104 | 2025-07-20 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| ee9ff2f8-ca38-30e3-a339-ace8b7e29efd | -3.0235 | -47.8613 | 2025-07-20 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1bfaf23f-5c83-382b-9608-9e116d82463f | -3.042 | -47.8607 | 2025-07-20 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 747f4d8e-0ffa-3436-93be-fb885f9c1c88 | -10.9815 | -45.0874 | 2025-07-20 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| d630a4af-ff3a-3cbb-8dec-2e763f15da0a | -10.9624 | -45.09 | 2025-07-20 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3d8de02d-ec37-3d65-8a59-ae9e7b50e1fb | -10.6876 | -46.8053 | 2025-07-20 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 7d34e7d0-bdd6-361c-b45a-a75119fbafcf | -14.2779 | -58.2466 | 2025-07-20 02:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 7d4885c9-3f37-3ca5-a6ee-2e984cdac693 | -3.042 | -47.8607 | 2025-07-20 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4efa390e-e38b-3d8f-9ec3-bd333d1de5e7 | -10.962 | -45.113 | 2025-07-20 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b422a5ca-de38-38ec-b0a8-dad890b3b2a4 | -3.0235 | -47.8613 | 2025-07-20 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 7bde210e-83b6-32b6-9fdd-666f79ca54b0 | -14.2588 | -58.2483 | 2025-07-20 02:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 653cead5-7622-3c7d-a78c-e79b2a3d5466 | -9.5343 | -40.3282 | 2025-07-20 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 5c28c9a7-5d2c-3c0d-820f-693ff938d41d | -10.6686 | -46.8077 | 2025-07-20 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 92128e85-fcfd-3cbb-94ac-49c4c509eb54 | -10.688 | -46.7829 | 2025-07-20 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| a9358c45-530d-376f-8202-f1361d15aad5 | -10.9624 | -45.09 | 2025-07-20 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| fb2c66be-0ad9-320f-b126-d3ee9632390d | -10.6689 | -46.7853 | 2025-07-20 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7fd50002-c335-378d-8c1e-4ea24a8f6d13 | -10.9811 | -45.1104 | 2025-07-20 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 63ebe3b8-f260-331e-8869-d0bdc5a27208 | -10.6876 | -46.8053 | 2025-07-20 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6060eb9e-a645-32b9-af35-b95285f85e1b | -10.9815 | -45.0874 | 2025-07-20 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3a4c1fef-3503-3211-986d-ca4268307663 | -14.2588 | -58.2483 | 2025-07-20 02:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 40dfdef0-498e-38b6-b038-001f7d1da54e | -12.3461 | -50.3288 | 2025-07-20 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| c588bade-176f-3dc1-aca1-3d18821be949 | -10.688 | -46.7829 | 2025-07-20 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 36cb6be0-f5e2-32b6-ae92-d617cd8489c5 | -7.7005 | -47.2976 | 2025-07-20 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9a476ddf-2f6f-336d-84b2-118ba8bfc233 | -3.042 | -47.8607 | 2025-07-20 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 1fbecd89-4c5d-3c62-b898-0447acd91005 | -10.9811 | -45.1104 | 2025-07-20 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 1622cdfb-4f53-3c03-a784-10c72b8f5ce4 | -10.6689 | -46.7853 | 2025-07-20 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 03fd363b-7e5b-3e7c-a14d-6b42b57ca6e7 | -10.962 | -45.113 | 2025-07-20 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ccbe983d-b852-3aef-a434-b3687be45b6f | -10.6686 | -46.8077 | 2025-07-20 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0597069c-d07f-308b-ad24-f388c3e737b8 | -9.5343 | -40.3282 | 2025-07-20 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.7 |
| c645852b-e00e-3e8d-99de-0d9134a2f6b0 | -10.9624 | -45.09 | 2025-07-20 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 21f7b440-d3bd-31cb-9bf4-8991bdba2e86 | -10.6876 | -46.8053 | 2025-07-20 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| a85c7d49-0ee8-3a65-8f4c-3fe622a4997c | -14.2588 | -58.2483 | 2025-07-20 02:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 61dc5fbd-37b0-3ce2-9fdc-7076f7d216f3 | -10.9811 | -45.1104 | 2025-07-20 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 912ae75e-425d-38ad-a429-d631dfc2869c | -6.9145 | -45.4011 | 2025-07-20 02:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 4e90875c-7079-3f08-97f8-5099660a6fa1 | -10.6686 | -46.8077 | 2025-07-20 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 721a0e75-a442-3b3a-a478-e03dc45b6e21 | -10.962 | -45.113 | 2025-07-20 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a664cfff-67b3-3487-9015-a6e599c5d7d4 | -3.042 | -47.8607 | 2025-07-20 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c5c800cf-2a3a-3c1d-8ed5-429ec16dd29f | -9.5343 | -40.3282 | 2025-07-20 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 39749f4c-508f-3ebf-a4a1-15ff3a076fe9 | -10.9815 | -45.0874 | 2025-07-20 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| c6d77542-d0c1-3eee-8ff0-e331587d7ac0 | -10.6689 | -46.7853 | 2025-07-20 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| a82e7d59-10f1-3748-a703-c1ac5b706379 | -10.688 | -46.7829 | 2025-07-20 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| e7d11aa0-2553-3be8-aa75-50fa62390f95 | -10.6876 | -46.8053 | 2025-07-20 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3f41f407-187d-38ca-9427-a40bdcbcdc69 | -10.6686 | -46.8077 | 2025-07-20 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| a2ad2f0d-e3a8-3417-9f40-21965d889fa8 | -10.6689 | -46.7853 | 2025-07-20 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 619cae4a-245c-31c5-ab46-d60ab65e5d46 | -10.9624 | -45.09 | 2025-07-20 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| bc7e870e-b9b4-3db4-a8b2-c3321c37344a | -10.688 | -46.7829 | 2025-07-20 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 9f313745-9039-3f77-9ca5-633ea420e528 | -10.962 | -45.113 | 2025-07-20 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e8bf08c5-d7c5-3029-868f-7a4e664468cc | -10.9811 | -45.1104 | 2025-07-20 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| dc2b814e-7654-3be9-8276-d08a8ef904c7 | -3.042 | -47.8607 | 2025-07-20 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 17a4a310-9707-3e7a-9912-dd9641012120 | -10.9811 | -45.1104 | 2025-07-20 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| b151bc73-1af7-350d-86dc-489114bd78ad | -10.6686 | -46.8077 | 2025-07-20 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| acb43bde-69a7-348a-bc4e-570b3c9f754b | -9.5343 | -40.3282 | 2025-07-20 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 9441541d-f7e9-3e30-abc2-f3036ca046e0 | -10.6689 | -46.7853 | 2025-07-20 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f814dd23-5fe9-32c0-986c-b3b8eced64f0 | -21.0783 | -50.6415 | 2025-07-20 03:00:00 | GOES-19 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| fbbd48da-3dae-3938-9ebd-19560f8f7ac0 | -6.9145 | -45.4011 | 2025-07-20 03:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ac124564-c1dc-34a2-9a30-f05515a7f869 | -14.2588 | -58.2483 | 2025-07-20 03:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 7424529f-a8bd-303d-bbb0-df273c2330b6 | -10.6686 | -46.8077 | 2025-07-20 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d1e30cc2-4510-3efd-8f51-33d913393b4d | -10.6496 | -46.8101 | 2025-07-20 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 00e7a0d7-f530-3e75-a136-ae2e6546bc6a | -14.2585 | -58.2683 | 2025-07-20 03:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 656c7ca5-cea2-3058-9202-4cc408dff6e5 | -3.042 | -47.8607 | 2025-07-20 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b0c6b1de-d10c-3005-85ba-b5122172fe72 | -10.9811 | -45.1104 | 2025-07-20 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 46c48fe1-cdfc-38ce-9b69-7a3b2cc63218 | -6.9145 | -45.4011 | 2025-07-20 03:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 065bb49c-eb18-3cdb-9cae-6b5fd2f916da | -10.962 | -45.113 | 2025-07-20 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 81ab7572-dea3-362f-b049-dd5041a3dad6 | -14.2588 | -58.2483 | 2025-07-20 03:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d79c7976-0456-39ac-8b23-b887c90f66f7 | -9.5343 | -40.3282 | 2025-07-20 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 6edd38ae-ebf8-322d-944f-42b46806f958 | -3.042 | -47.8607 | 2025-07-20 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b2323b2c-8b84-37b7-ad65-00da768b9a31 | -9.5343 | -40.3282 | 2025-07-20 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.4 |


[Clique aqui para ver as próximas entradas](README4.md)
