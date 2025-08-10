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
| 8b25d0bf-b9d4-3dae-ad9c-41a0614d2eb0 | -8.3102 | -44.9967 | 2025-08-10 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| ff2e1bef-9e3a-3afc-b394-bf62cfca9190 | -14.2945 | -51.9635 | 2025-08-10 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 193743af-1153-342a-9fcc-c89eab8ab921 | -9.3806 | -61.5315 | 2025-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 222.2 |
| f6064481-a5ae-3f73-ba5c-02847a8fba38 | -6.9422 | -44.5562 | 2025-08-10 01:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 87c77b50-081b-3488-becb-0507adce5619 | -8.9215 | -60.7297 | 2025-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| bf77d4e0-4a34-305d-a7ff-bbded10a3246 | -9.362 | -61.5324 | 2025-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 592e8b58-1788-3468-a387-cb78cca361dd | -9.3808 | -61.5124 | 2025-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 90f66a18-c92a-3e71-9098-80135b5102bb | -8.9213 | -60.7489 | 2025-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 1aa0b9a4-7a70-3669-a023-e1212ea5028e | -8.9399 | -60.7481 | 2025-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 09556a2d-9136-3ba6-a6b8-1b21e759bf8c | -8.9212 | -60.7681 | 2025-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 7c928750-d15a-3e66-8236-642dcdcf03b6 | -9.3622 | -61.5133 | 2025-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| e8a100c4-3d63-39f7-8bca-9ac182140fd3 | -8.3105 | -44.9738 | 2025-08-10 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| ae719c24-c8d0-344e-89c0-30b31bf5d1cf | -7.08 | -59.1771 | 2025-08-10 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 17ee3123-e8f5-348f-9f48-420d31f7ed3f | -7.0799 | -59.1964 | 2025-08-10 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0dbb1288-e4ef-3671-9216-c6d63bcb50ff | -8.9399 | -60.7481 | 2025-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 3bc940cc-f033-3f92-8cbd-e00d184ffdc1 | -8.9213 | -60.7489 | 2025-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| c7eebb12-99cb-34dd-b3ae-4b71352714bb | -8.9398 | -60.7673 | 2025-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 71bc0c7d-47e3-35a2-9dcb-6b76cd84abde | -6.9422 | -44.5562 | 2025-08-10 01:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 0b151cb8-5cd4-387b-8fbf-3818908ae888 | -8.9401 | -60.7288 | 2025-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e136a479-8578-34dd-a928-27cc2f981001 | -8.9215 | -60.7297 | 2025-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 8dc315aa-57e2-36ec-8871-47a45fccc466 | -9.3808 | -61.5124 | 2025-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| b56d361d-7ea2-3bac-bff8-32e964d17786 | -9.3622 | -61.5133 | 2025-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a0175e1d-291e-37c4-9a6a-007e71625e31 | -9.362 | -61.5324 | 2025-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 6734ff34-51ec-3d06-9e2d-36f2b07a037c | -9.3806 | -61.5315 | 2025-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 226.6 |
| a2241423-9a2e-3902-9ced-4bb2364a0dd1 | -16.3731 | -42.5425 | 2025-08-10 01:50:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d13b0602-d785-3fd8-98a1-67d6222b90d2 | -6.9422 | -44.5562 | 2025-08-10 01:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d9924643-8359-305a-afa1-29ead869818f | -7.08 | -59.1771 | 2025-08-10 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0e80a1e8-9e82-3b7e-b648-0ddb8e944868 | -7.0799 | -59.1964 | 2025-08-10 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 17f47f56-46f7-3a58-91a4-15e61cca69ab | -8.9398 | -60.7673 | 2025-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 422c7e78-a26f-3998-b7e5-de0bd690b4c6 | -7.0614 | -59.1972 | 2025-08-10 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c3cdfbaa-c648-396b-9342-5040e4400349 | -14.2945 | -51.9635 | 2025-08-10 01:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e33ea4eb-917f-38c8-9f97-2a5c3a3c1017 | -14.2752 | -51.966 | 2025-08-10 01:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 7b07b991-aead-3fe7-82ba-2bd5c894cd91 | -7.0615 | -59.1779 | 2025-08-10 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 64709fe8-b536-3715-bb82-8a1a7cef42bb | -9.362 | -61.5324 | 2025-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| abd39878-d42c-3843-b50a-b44b39428021 | -8.9215 | -60.7297 | 2025-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 4fd01041-0044-3b48-8f8a-6d16a63897e4 | -9.3808 | -61.5124 | 2025-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 488282eb-bf99-3547-aa19-efab0eab2d28 | -8.9399 | -60.7481 | 2025-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 3a5d4298-5c48-3b81-b6c0-d5bfd634703b | -8.9213 | -60.7489 | 2025-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| e307ba59-608c-3153-9427-3129012dba1a | -9.3622 | -61.5133 | 2025-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 692b2d07-05fa-30b6-a33b-5cf28e9ae2ce | -8.9401 | -60.7288 | 2025-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 2cf8c2ff-913c-3001-b8f1-e8c1fbf90008 | -9.3806 | -61.5315 | 2025-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 1c8146d7-e349-371e-95b0-19e828b3afe0 | -6.9422 | -44.5562 | 2025-08-10 02:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c4270bfb-8c8a-3a1a-849c-065ad111a6b7 | -9.3806 | -61.5315 | 2025-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 198.0 |
| cedac0e9-d708-3107-8692-20a2bfea8a82 | -8.9398 | -60.7673 | 2025-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7b98bd61-c1ff-3700-b340-683c4f5a7416 | -8.9213 | -60.7489 | 2025-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| a41ba3ee-1986-3650-81d2-fc23ebb3b1b8 | -9.3622 | -61.5133 | 2025-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5d3b0d90-8496-387f-bfe4-52662e1cf0b9 | -8.9215 | -60.7297 | 2025-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 25a99119-cd2f-3810-92a1-5e86ec90f2af | -9.3808 | -61.5124 | 2025-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 15635b55-9724-3404-8262-c1ca838b8a65 | -16.3731 | -42.5425 | 2025-08-10 02:00:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a3b0646e-6b1b-3915-916b-e36a2f65786f | -7.0614 | -59.1972 | 2025-08-10 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 77753a6e-68b6-3214-bee4-80acf9632b38 | -14.2945 | -51.9635 | 2025-08-10 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e1ba5920-b0c2-30ad-a635-627db5b0d6cf | -7.0615 | -59.1779 | 2025-08-10 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 673b2298-7d0d-3042-8b32-919f74d88858 | -14.2752 | -51.966 | 2025-08-10 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| c5e566da-aa53-3a74-a372-5e148f573fed | -7.08 | -59.1771 | 2025-08-10 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a70b395e-a63e-32e6-9549-f0e92086ce6d | -7.0799 | -59.1964 | 2025-08-10 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| bcac43e2-8a23-3426-8516-06a28c3ee3ea | -8.9399 | -60.7481 | 2025-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 144.5 |
| ece6ed0c-883b-3035-a591-f37bd8e13526 | -8.9401 | -60.7288 | 2025-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 72cb4639-b8c0-31c2-bdf1-d266650fae0b | -8.5605 | -54.6771 | 2025-08-10 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e201289f-da00-38a2-a01b-991cac4a53f4 | -9.362 | -61.5324 | 2025-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 56f24fa9-f9ee-3404-8270-cd2fa8b75d82 | -7.0403 | -59.200802 | 2025-08-10 02:03:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2936c1a-1415-382e-9da4-81d4dd42072d | -9.3363 | -61.561001 | 2025-08-10 02:03:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78ac353a-0e72-3f56-bc8c-165ad95c71fa | -7.0307 | -59.203201 | 2025-08-10 02:03:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b99d8bb-5b1f-3312-b011-d8e46029c83d | -9.329 | -61.531898 | 2025-08-10 02:03:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4cd9acd0-16b1-32d9-8b45-90a7189670e1 | -9.3326 | -61.546398 | 2025-08-10 02:03:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f6814d1-be0b-37ad-a081-0f6049827f21 | -9.3387 | -61.529499 | 2025-08-10 02:03:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e97cc05c-c8de-38bd-a9a2-8f095c62047f | -8.8936 | -60.745201 | 2025-08-10 02:03:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea0979fd-624c-31a2-8157-a062345880d5 | -9.3423 | -61.543999 | 2025-08-10 02:03:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3168170-e723-3c69-b4eb-e3091cef2a44 | -8.8978 | -60.761902 | 2025-08-10 02:03:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0609e19b-41f5-32ec-8b49-c672795aee48 | -9.6368 | -62.8951 | 2025-08-10 02:03:00 | METOP-C | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a470762-ac23-3705-9cc8-2f5b92dfad98 | -8.8882 | -60.7644 | 2025-08-10 02:03:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5f23ae5-3ec2-3469-b98e-cca591c55bf7 | -7.0614 | -59.1972 | 2025-08-10 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e2a122c4-c63b-39f2-9b72-06b80f9bcae8 | -8.5604 | -54.6973 | 2025-08-10 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 746a3aa0-a1d2-3688-a1a6-6331da35fbee | -8.9215 | -60.7297 | 2025-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| aa25f42c-6a8b-3223-a642-c71406203e19 | -9.362 | -61.5324 | 2025-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 161.1 |
| dd72cbe2-e571-3b69-86f0-30cd691b1cfb | -8.9398 | -60.7673 | 2025-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9c528e91-f770-3c24-826b-128cc0063bb2 | -8.9213 | -60.7489 | 2025-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 4a9e8a07-9020-35d0-8ba1-fa56d7447b88 | -9.3622 | -61.5133 | 2025-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 89aa2f46-78f6-3150-8d84-e1d37dcc0825 | -8.5792 | -54.6758 | 2025-08-10 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d88bbbab-94fd-3f99-bf57-fed8ba564378 | -14.2752 | -51.966 | 2025-08-10 02:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e47c83ac-338b-3d23-b058-a4fffd010ac9 | -8.5605 | -54.6771 | 2025-08-10 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6d328edf-70ad-316c-86ec-6fa58a485fa8 | -16.3731 | -42.5425 | 2025-08-10 02:10:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 67c12c6b-8e97-3b25-888c-dd869e0c80ee | -9.3806 | -61.5315 | 2025-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 50bde18a-d7e7-3b18-9cc2-cb6246443618 | -8.9399 | -60.7481 | 2025-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 180.5 |
| 452a5a9b-0f5e-3844-a719-4f37747d4fd9 | -9.3808 | -61.5124 | 2025-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| f26dab0c-739c-3a6e-bca0-bbaaf8b0f0ea | -8.9401 | -60.7288 | 2025-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| eac458ff-627a-3c73-8517-5b0875a8bbb2 | -14.2945 | -51.9635 | 2025-08-10 02:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| d1ed7d46-23ea-3fa0-89a3-43c2aa3c80e8 | -14.2945 | -51.9635 | 2025-08-10 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 334964a5-4c35-3e65-8083-5ef81d2f3312 | -7.0614 | -59.1972 | 2025-08-10 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3759780a-1ecc-3699-9c6c-d6592f107e57 | -9.3622 | -61.5133 | 2025-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 515cccb5-5085-3630-8692-6b724f896631 | -8.5605 | -54.6771 | 2025-08-10 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7038ea70-b63c-3387-a159-8fc19e3fad6d | -8.9401 | -60.7288 | 2025-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 4667ff0b-91de-3a4d-b4f9-866a72a2be4c | -8.5604 | -54.6973 | 2025-08-10 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| f67bdb0f-2f42-3375-83f2-bfcb6b94529c | -8.9213 | -60.7489 | 2025-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 03740dea-c462-3821-a496-2a09fce9a6b1 | -7.0799 | -59.1964 | 2025-08-10 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5e09004e-935d-3d43-8920-4546f06479ff | -9.3808 | -61.5124 | 2025-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9b419016-787b-32b1-bb38-1d77c37e7f09 | -8.9215 | -60.7297 | 2025-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 394d6867-ef7f-36c5-8622-4e5efdbd1aca | -9.3806 | -61.5315 | 2025-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 59a38e63-5ea1-3477-87c3-63caf8994229 | -9.362 | -61.5324 | 2025-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 96cabe23-1f17-37de-8f53-27b2dd9e49a2 | -8.9399 | -60.7481 | 2025-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 189.8 |
| ac9d8133-671a-3e2b-92f0-ac7050efc74b | -8.9398 | -60.7673 | 2025-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |


[Clique aqui para ver as próximas entradas](README6.md)
