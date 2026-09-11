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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 503f78d7-6b51-3ade-8b8a-a9baf6a3a1b6 | -3.16244 | -58.65244 | 2026-09-11 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f46ff41d-d76b-3fb7-b359-b0b1431de761 | -2.71692 | -57.61671 | 2026-09-11 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2b1f0df1-85ce-3617-8670-84a8faa31028 | -7.82599 | -55.41663 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d85f77e-63fa-33ae-9e74-c250e26992d8 | -4.35401 | -47.7779 | 2026-09-11 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 8facc357-841a-30a3-829d-1ffd5f1ca5aa | -9.18322 | -59.45911 | 2026-09-11 00:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| a683a522-dc26-32d3-b3d7-f7cab539c314 | -9.18176 | -59.45352 | 2026-09-11 00:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b20df6e2-cfc2-352e-836f-1f2b45a211a1 | -8.21251 | -55.26788 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| af42c5de-74b9-3be6-acef-8d50f72c92b2 | -8.7331 | -50.60017 | 2026-09-11 00:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| db428587-6e1f-31ed-b6c0-5ba01ed0a823 | -5.34836 | -55.89116 | 2026-09-11 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 82b76ad8-8c71-35bc-9a91-d68880ce1f3f | -5.36653 | -56.02442 | 2026-09-11 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ea35e059-ef6f-3ada-b0dc-44e918ef3fbf | -3.70668 | -58.51963 | 2026-09-11 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| bdcca348-886a-3136-8831-6f892122acdd | -8.07229 | -55.32717 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a3143dd1-8a71-320b-af53-2f3a6ac02207 | -6.83768 | -51.49297 | 2026-09-11 00:24:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2260de96-e620-3749-a499-56dbc8462ee0 | -5.76625 | -45.08625 | 2026-09-11 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 30eb831d-06df-3e07-afe4-79de055f59a1 | -4.35712 | -54.78444 | 2026-09-11 00:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a7e23997-71bc-35f8-b77f-91b6924c0afb | -2.73782 | -57.63327 | 2026-09-11 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e5f01dae-31e1-37ed-addd-2e5021739887 | -9.17671 | -49.95404 | 2026-09-11 00:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 67ab434b-7cc8-3f21-ba0e-a2ebb6b74e60 | -2.72607 | -57.61545 | 2026-09-11 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c96864b9-c88a-3a65-b910-00b715600d2d | -9.17309 | -49.9458 | 2026-09-11 00:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 51e056d1-0c0c-3582-99cb-35025e64a3f3 | -4.86592 | -56.01274 | 2026-09-11 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 155b0c1e-7a3f-3509-be6e-052f92f328ab | -2.86397 | -49.53219 | 2026-09-11 00:24:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8621c110-85fc-3c48-b090-6b7af4a516a8 | -3.97355 | -53.43484 | 2026-09-11 00:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4e44b533-295d-32ca-aeb5-50cea1f34364 | -5.78048 | -45.09116 | 2026-09-11 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6bde9bc5-e0b5-361b-88b7-24a9bebe025a | -6.02663 | -51.33146 | 2026-09-11 00:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d7bac75c-f88b-3da4-92b5-a1ce41bae64d | -5.63396 | -51.65934 | 2026-09-11 00:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 13e8ab5c-e38c-366b-aaaa-30a1567a2b4d | -2.11945 | -47.50322 | 2026-09-11 00:24:00 | TERRA_M-M | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| f72400b2-ae1a-3573-a62b-14d961467903 | -6.63285 | -55.30513 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d4788993-9faf-3e6c-9f5c-e1bb22e02431 | -6.31995 | -56.05899 | 2026-09-11 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 78d1647d-53b3-3236-81f2-f466cf45bc94 | -6.01622 | -51.33289 | 2026-09-11 00:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 8c03f638-ca29-3339-b249-0cb784190559 | -5.82477 | -53.8059 | 2026-09-11 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 40d97ded-5376-3f8b-8702-20b7dbd193f8 | -6.19141 | -57.76102 | 2026-09-11 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a805fb55-298d-3871-8146-e63bc30107d7 | -5.78338 | -45.08393 | 2026-09-11 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 42493eab-b115-32e0-a819-1f9ca4c4d002 | -9.67434 | -55.11041 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d3efda8-39ea-33f3-b882-58472ee858f7 | -8.20368 | -55.26915 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 674a4c2a-1444-3305-81a4-bd64be2bc5cd | -2.73652 | -57.62372 | 2026-09-11 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 11c23b68-3d05-300b-b665-946ce84ddeca | -3.07083 | -51.33995 | 2026-09-11 00:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 62df3ff4-32fe-366c-8bd3-885204cbf46b | -6.19429 | -55.27147 | 2026-09-11 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 651517b0-b428-35a1-9acb-d9490905fea5 | -8.08114 | -54.85033 | 2026-09-11 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 69b42cc2-002e-3a74-9d1a-95e3d8999063 | -4.53677 | -54.9606 | 2026-09-11 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| d494102d-4bbf-3910-9fc2-2f68bda69f4b | -4.29878 | -49.1208 | 2026-09-11 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5633fc3b-ca19-351d-8ea7-79ef22fec76d | -8.20247 | -55.26023 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e39572f2-784f-3879-af5c-30757a5a626d | -1.32045 | -49.02129 | 2026-09-11 00:24:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1599cff7-fbc1-377a-929a-c377f422b324 | -8.07993 | -54.8415 | 2026-09-11 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 5df6371a-0842-3382-b0b2-b61ef08d572b | -8.51391 | -50.15044 | 2026-09-11 00:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 3577d343-3048-3bce-b00a-84c62ecd26b5 | -8.50301 | -50.15217 | 2026-09-11 00:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 0574689e-f2a5-32d1-8602-8908650093b0 | -5.97923 | -57.76952 | 2026-09-11 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| afe0608c-119a-3a94-9284-368234d4d17f | -4.52795 | -54.96184 | 2026-09-11 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1fb37abb-beb2-33e9-94cf-95fba2a314b7 | -2.71563 | -57.60718 | 2026-09-11 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0b86c146-ae06-3e47-a830-1e7056bd0bff | -5.98061 | -57.77993 | 2026-09-11 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c766da7d-983f-3311-bd51-b2a069c92675 | -9.38835 | -49.38615 | 2026-09-11 00:24:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4c2f4cb8-f951-3ddd-9d23-99a0b896f21b | -5.20444 | -45.57119 | 2026-09-11 00:24:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 416b33ba-f41c-3c4e-9e7c-4d2da9025b2f | -4.74233 | -45.68252 | 2026-09-11 00:24:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8692f125-792b-336c-81b6-cd3e9b22d23f | -9.67556 | -55.11941 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff2a9f06-146d-3f17-9a58-767fee977e55 | -4.35588 | -54.77552 | 2026-09-11 00:24:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| be5bec28-9842-33e9-a2b0-20574641afaa | -5.63568 | -51.67142 | 2026-09-11 00:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f34c6aa9-0191-37a5-926d-4f4d59b40bad | -3.37753 | -50.7514 | 2026-09-11 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| f822d71d-5c16-36e3-b869-0bb7ef3b24df | -4.89932 | -55.91226 | 2026-09-11 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| eedb8807-3b93-3bae-a58b-a06fb2b671c8 | -4.36106 | -47.79596 | 2026-09-11 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| e53516cd-e493-3e40-8684-0bd03966d15c | -4.0875 | -56.30569 | 2026-09-11 00:24:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6d0d955d-dcbb-35de-a853-4d7a2ba8e3f4 | -8.62735 | -47.39507 | 2026-09-11 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c1f827d7-0aa7-3eaf-9ab6-89296e4d3ec2 | -2.25138 | -47.99376 | 2026-09-11 00:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 59fd798f-11c7-3701-ace9-752a030ab388 | -8.71055 | -49.62152 | 2026-09-11 00:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 188742ed-e5c4-3871-a36d-25eb309c4384 | -6.19308 | -55.26268 | 2026-09-11 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e0bfd127-272d-377c-9a5f-2fc5cc56bff5 | -2.86418 | -49.53787 | 2026-09-11 00:24:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d924ada1-2c2a-3f67-adf7-0593598351d6 | -3.40115 | -54.07824 | 2026-09-11 00:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 59c76c58-6a8a-3417-a606-af92845af3c8 | -6.20428 | -55.27902 | 2026-09-11 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 246c1fff-b9d3-30a9-98ca-1399c20086bb | -5.19377 | -45.53968 | 2026-09-11 00:24:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| e17edb5d-94d1-33dd-8933-cd741a37310f | -9.37537 | -55.96878 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 43e9d477-5b7e-3764-a1a7-e71bf1b019f0 | -8.07107 | -55.31825 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b0cbc7b-5d52-30ee-8409-beb5c5775b85 | -6.3196 | -55.85789 | 2026-09-11 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3346edbb-dd5f-3029-8693-b28950e5a660 | -2.72737 | -57.62498 | 2026-09-11 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| b5ad8e44-966a-399a-a317-92d1aed81416 | -5.19944 | -45.57691 | 2026-09-11 00:24:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| b1f8ed89-2c10-33e4-9de0-5e1beaa0c8e8 | -6.18999 | -57.75048 | 2026-09-11 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ee8713b-af55-34f1-b150-b8bdc75b74fd | -3.37968 | -50.76655 | 2026-09-11 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| d89b496e-c258-3cfa-92a0-48338a741534 | -2.72866 | -57.63453 | 2026-09-11 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| c10d69a8-2e7b-3c56-955e-8957b065b9f2 | -3.36615 | -50.75301 | 2026-09-11 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| e3f1ad6c-0cbf-3b43-a149-fe3ccd81e365 | -4.29584 | -49.10099 | 2026-09-11 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 3b8565e2-9127-399a-88b4-7002b4cacc2f | -4.53798 | -54.96945 | 2026-09-11 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| edfe988f-6b65-3a6f-bab9-22201f82a589 | -6.33069 | -55.85955 | 2026-09-11 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80ed7a0e-ebd6-3e30-8824-c49b16e3cefa | 0.21032 | -51.38357 | 2026-09-11 00:24:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2aa5f97d-c5cc-368a-b3c4-530526169254 | -3.16096 | -58.64154 | 2026-09-11 00:24:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9aa46d0e-e781-3075-afb1-59f0d461f31a | -6.50841 | -58.2928 | 2026-09-11 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 10eb9803-2bc6-3f8d-b50b-cbf44c3064c5 | -8.63098 | -47.41781 | 2026-09-11 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 999abce7-9fc6-3a4b-b763-9818ae931aa5 | -8.06985 | -55.30933 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 470f85ca-6d0b-3f5a-8aee-778ef131ac96 | -4.35722 | -47.77075 | 2026-09-11 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4690a5c9-f23a-3ea1-9e47-933faaf5d575 | -6.62285 | -55.29756 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| d7a177f9-3bdc-39a2-87cf-877c0f4ef280 | -6.19549 | -55.28026 | 2026-09-11 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5fefadeb-e663-3872-bc62-9bbad154ec1c | -1.03142 | -53.73526 | 2026-09-11 00:24:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f0a6207e-fd3a-379e-8310-68356fe5dbc0 | -3.24941 | -50.82286 | 2026-09-11 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| b7bd7764-5962-31c0-806b-54b08c2a6d64 | -8.06863 | -55.30041 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 155d0e9e-e041-3b60-819d-231fe60aed6d | -8.2113 | -55.25898 | 2026-09-11 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2fe9287d-3f51-3f30-b971-aa557af0e43c | -2.73523 | -57.61419 | 2026-09-11 00:24:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f82ca14e-075a-3ab0-9a2d-5400a3bd118d | -3.36832 | -50.76822 | 2026-09-11 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 7c7042e7-0409-30a7-8bf2-ac2b658b422d | -7.84623 | -56.58393 | 2026-09-11 00:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3d37e2d1-ef87-30c3-983d-f155036bf8f0 | -4.52674 | -54.95304 | 2026-09-11 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 971801df-ea6c-3e48-915f-eb892dd323a5 | -5.28571 | -56.04183 | 2026-09-11 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6130485d-c7f8-3c26-9d9f-9db776bd1fbe | -4.52917 | -54.97069 | 2026-09-11 00:24:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f44772cc-cb92-3880-9297-0b362678db67 | -5.64348 | -51.66402 | 2026-09-11 00:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 310c9c71-cf94-31c1-b4b6-d57e61990695 | -4.86472 | -56.00396 | 2026-09-11 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 93a58d94-938c-3573-8583-40cbbe91d63e | -2.25272 | -47.98785 | 2026-09-11 00:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |


[Clique aqui para ver as próximas entradas](README3.md)
