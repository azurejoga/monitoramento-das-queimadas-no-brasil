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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9769856b-a11e-3be7-a33b-69057e4f7ffe | -7.883 | -45.52257 | 2025-08-03 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 530d1f8a-d339-336e-afd1-4b76800b5e41 | -9.81591 | -53.28873 | 2025-08-03 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fec7072e-4fd9-3076-9414-eedcd6991c31 | -12.64369 | -44.49197 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 930d1c57-163b-3b2b-a7e7-0fedb32e1952 | -7.25436 | -44.55968 | 2025-08-03 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e02ea27e-59e2-33ad-a9fa-393932faa5b1 | -7.96364 | -45.10541 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20995ceb-6295-3a4f-8456-5457c30c992a | -8.00974 | -43.15064 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 2624ff42-b49e-3637-8467-db290fff10c5 | -12.65074 | -44.49209 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6e6984c-2888-3e4f-bdd2-367917a1f2f4 | -6.73353 | -59.17095 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e64b786-e033-35f1-ba39-a61b53325a01 | -12.64958 | -44.48914 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf744e0a-b832-3ba9-ab3a-56ef260d9f40 | -12.65825 | -44.52156 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44bf8767-1553-3abb-92f5-1672cca9cefe | -7.11728 | -43.48378 | 2025-08-03 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba5da37e-27ed-3428-8fd6-31f6ee6a2141 | -6.62302 | -59.96537 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c38e025d-cc86-3bed-ad66-d8e1e56186d1 | -12.6725 | -44.49486 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42c0110c-4251-3699-83db-33ea8283b238 | -12.61961 | -44.66093 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73ff3a4d-cb96-3567-927c-1cde69650e9d | -12.41304 | -47.06878 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb4642e8-5827-3678-8b60-efcf4750b662 | -7.96437 | -45.09995 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4af8c419-649c-39a0-9874-ea8d74727385 | -9.39295 | -45.50671 | 2025-08-03 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 317445d6-d14c-31c3-9a99-34d7cc37b943 | -11.15423 | -49.69987 | 2025-08-03 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e8c8af-194e-36f9-9d38-07a4fdd527b5 | -7.75908 | -45.11189 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5605c12c-9203-30a1-b651-2627e0fcf68a | -8.41749 | -47.46247 | 2025-08-03 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4621a637-699b-39aa-b3af-55c1692fbc2c | -8.88107 | -44.79361 | 2025-08-03 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1792683-aed6-3041-9494-3b6c9d8cb3fe | -7.78137 | -45.20207 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c9cdb36-61e7-3dff-8763-940d4de61e3c | -12.63986 | -44.49066 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df70f06b-2d4b-3a82-accd-b893f4eef1aa | -10.46617 | -47.22953 | 2025-08-03 04:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 690bed1e-2b74-35f8-b5fb-6e9ef2fb7f74 | -12.4257 | -44.86576 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfcf51da-fb1a-3c20-bc53-063d56265cf2 | -8.01785 | -43.15963 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 87ba2eec-9c08-3cfe-822b-f34be23abaea | -7.43646 | -43.8255 | 2025-08-03 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1db3a420-3cea-36fe-86e0-f91354033bff | -7.59743 | -44.98541 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af19dfaf-79f4-3e21-9a7e-8f9a6a4bcb5d | -7.88704 | -45.52815 | 2025-08-03 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efe5bf9e-e76b-390a-958d-14b12910558f | -10.47984 | -46.97183 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40421b6d-eaca-32e6-9fb9-d0f0f23907f1 | -8.00574 | -43.17991 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| e26c517a-3838-3b4a-aedc-eb26797c8a01 | -6.82545 | -59.26683 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4456298e-9b01-3800-8886-1ff8e7d085e1 | -12.63018 | -44.51152 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49161332-d891-3fb2-9496-2ed4d9dbc3dd | -12.65783 | -44.52505 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 585f99a4-9497-3e4d-9f1d-3a425e2b14bc | -8.02039 | -43.15585 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1df3c635-3d75-3dfa-ab9c-721f1f32ac26 | -7.3652 | -44.19369 | 2025-08-03 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1629129-d0ae-36c7-9935-66577a6eee3a | -12.66035 | -44.50404 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 816d8711-ebd8-33a1-b796-9c782b510f7d | -6.62624 | -59.95229 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c762e166-677c-32b3-aaeb-3faeef27f2d4 | -6.62473 | -59.95524 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2bb06f38-bd1e-3727-8f39-8fc0feaaf803 | -10.47724 | -46.9579 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf55a6da-0df2-3e5e-8325-90691cdcab02 | -5.96578 | -52.16867 | 2025-08-03 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d410d005-5028-3898-9633-215cc51a4685 | -8.01832 | -43.15601 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 735e8d73-1bbf-3f52-ba39-50a12c57c606 | -10.33918 | -44.90493 | 2025-08-03 04:53:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98efca8a-a1c1-39e9-8084-97671e76d46f | -7.52067 | -61.33087 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dc393ec-ae0e-379e-89aa-ae367c6a47d3 | -7.52311 | -61.34687 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e27c065e-6941-36ad-9536-4131b94ff610 | -11.05328 | -49.54495 | 2025-08-03 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf92b360-bc33-381d-97f2-c458f0372c82 | -6.81417 | -48.63942 | 2025-08-03 04:53:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf8b5696-3e43-35a6-89f0-3b18a0f73e97 | -7.11821 | -43.47717 | 2025-08-03 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 064218d6-88a5-300f-a89b-cdd40da46fb0 | -12.64779 | -44.50321 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14266abe-3bab-3795-99c9-de7f45565dfa | -8.01927 | -43.14866 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 607e6359-2778-3d51-a5bc-320ac9f39039 | -6.62217 | -59.97041 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 385409f0-8e3e-3ed2-8285-b1d4a028f08e | -12.62816 | -44.49625 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 749f5c8a-013f-36fe-a872-63282e213b1b | -12.41408 | -47.0613 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 328283e4-38ae-3539-8f84-a93c5d7c92f3 | -8.03108 | -43.11955 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 237bbc59-88b1-3036-86b0-1a600e5c104e | -7.52013 | -61.3339 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4875557c-71e3-31b8-b04b-dd621d1ed337 | -10.47802 | -46.98495 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ea3f480-e5c8-31c3-b8b4-8d430faba676 | -12.63401 | -44.49346 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1a2e594-e1c0-3811-bcc6-f263f845433c | -7.59667 | -44.99097 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 27858bb1-f179-3b7c-b3c7-87fa4e7e5c0f | -6.62445 | -59.96241 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f4a5cb05-294a-3b57-929b-6ed4be435680 | -6.61589 | -59.95569 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a4cf4d4d-591f-3525-bec3-7503c3dfc0df | -9.39368 | -45.50142 | 2025-08-03 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 442b3604-cd8f-3d8b-94d8-e1d2839c9d15 | -7.12257 | -44.08708 | 2025-08-03 04:53:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 118f87ce-ccee-3970-a955-56e1608cd217 | -12.25882 | -47.00331 | 2025-08-03 04:53:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 827f0359-f8c1-3244-a5d5-a6271b269934 | -6.67395 | -59.16925 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9179a350-7c50-391e-abac-3767c77acc95 | -12.61564 | -44.49539 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 877515a9-4c5b-361c-bd1a-c6fc095ebc22 | -12.63737 | -44.49827 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ba87600-6520-35fb-9af9-7da7732a5b99 | -6.67545 | -59.16061 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3497e98f-f967-3782-be83-f7e4fb0ceb3b | -8.01332 | -43.16596 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 726a3119-eaa0-3f68-bb5e-e2c74b778b5f | -12.62733 | -44.50327 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 95617051-57e6-3614-a7e5-e5986822281a | -12.43174 | -44.86041 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54a8c26e-8a93-38a7-a9dd-9fdf46970802 | -8.03718 | -43.11662 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7f54411f-7916-3348-9cf7-6a6442c7cc6e | -7.88631 | -45.53327 | 2025-08-03 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e76bed0-991b-3eda-89c6-195913fa0aa2 | -8.42638 | -47.45993 | 2025-08-03 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2022e8a-e22d-3097-80e2-2e3b35465e88 | -12.62692 | -44.50675 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a608be19-ad54-308c-b192-be9c96e97121 | -6.61973 | -59.96154 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8a033a47-65c6-3e2b-bef3-d699280d209b | -6.63655 | -59.94903 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6342c63-0d63-3ab6-98ca-cc2940e8a66c | -6.61829 | -59.96455 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac909cdd-9299-3e4b-ad8f-8db1e26987bc | -12.61521 | -44.49889 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b5319e5-9bee-33a2-a859-91f6d749eb2f | -8.00366 | -43.15352 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 7f7d04dc-23fe-3e3e-8b3d-793e0fce044c | -8.00675 | -43.1725 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9aa6238e-5f6a-311e-a650-40cb7b26ede3 | -8.04329 | -43.11369 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| daeca4da-8e3b-3d88-8d8e-cdf62f6fa26b | -8.94159 | -46.75063 | 2025-08-03 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b54e0548-be20-301a-8043-ad36e07c8c95 | -8.11441 | -49.76067 | 2025-08-03 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98b38418-fbdc-3c6b-84d9-fb1b5d878cb8 | -8.01182 | -43.1769 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4cfd4818-7502-3bef-a4be-f1a81728e444 | -9.10812 | -48.90155 | 2025-08-03 04:53:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10473c7a-abe4-3470-86be-4d0ff248d4f6 | -12.64016 | -44.51991 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4213393e-fab8-39bb-9324-f3faa8c6a822 | -8.04432 | -43.10619 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2f309238-d102-38f4-9701-8ba5ca34ac9f | -10.47601 | -46.96671 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d5632ba-f356-3457-90ac-5524ab1e4f31 | -12.64824 | -44.4997 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4441d26-559a-3791-873d-184561e018bf | -12.65282 | -44.52085 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 779a66fa-ef53-3e47-8a28-02ee340b5079 | -7.54198 | -43.83059 | 2025-08-03 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03caa332-256d-3ff0-b300-42f9a3598452 | -7.9992 | -43.18626 | 2025-08-03 04:53:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| a1c4e801-b67c-3081-b1db-c387d6bf0701 | -6.61884 | -59.96659 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e59bd2d3-6e91-3fe6-b1ac-8011c4bcde96 | -7.09373 | -44.36518 | 2025-08-03 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0c1157fa-ac1a-3f0d-825c-3468642cdb50 | -8.028 | -43.14189 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 69e1b79f-ea06-3deb-96bd-3cf501c8ba4a | -11.93578 | -46.67385 | 2025-08-03 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64fe5489-59ec-32e2-95a6-44bd164784f2 | -12.43135 | -44.8636 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38ac9554-b41f-3a38-9d0a-b02c4f345e99 | -10.78951 | -48.80459 | 2025-08-03 04:53:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b524e87-8a3b-3cd9-b5b5-c01e62092d06 | -11.40856 | -54.7167 | 2025-08-03 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bb8c4df-9060-3ec2-9bfe-1268e08c5a71 | -12.66995 | -44.51598 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
