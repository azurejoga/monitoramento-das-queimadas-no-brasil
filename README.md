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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4db4cca-45c9-3251-8ec2-a7cbddfa4895 | -22.05 | -48.7 | 2024-10-03 00:03:17 | MSG-03 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab0f7069-5fc6-355d-af4d-581c3082438e | -22.36 | -47.96 | 2024-10-03 00:03:17 | MSG-03 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 13407a64-e34e-315a-8a02-4491fafa21f8 | -13.53 | -51.3 | 2024-10-03 00:04:07 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aaac77c6-b9ad-38db-bf98-365f2ab73886 | -13.53 | -51.24 | 2024-10-03 00:04:07 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 741a950b-7c56-37f6-a5d8-dd8c3798b3aa | -13.56 | -51.31 | 2024-10-03 00:04:07 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb91d567-0742-3d5e-992d-09067e4f316d | -13.56 | -51.25 | 2024-10-03 00:04:07 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a11b5430-2168-3f9e-bdc3-6339fd8f962a | -5.25 | -43.84 | 2024-10-03 00:04:57 | MSG-03 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd96c6b1-19a1-3b66-8063-866a77d1bfa0 | -5.25 | -43.8 | 2024-10-03 00:04:57 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf3e653a-f7d3-36b5-976f-9047b13d0c87 | -4.47 | -42.92 | 2024-10-03 00:05:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dde2c6b2-e9ab-3218-9690-5d8f04053f34 | -4.49 | -42.92 | 2024-10-03 00:05:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 971a4be0-ee67-310d-9775-20f75153e031 | -3.4 | -42.27 | 2024-10-03 00:05:08 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 322a8e10-d842-3765-861f-d9b68e1f9180 | -3.4 | -42.23 | 2024-10-03 00:05:08 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8988bd1f-4bab-3b1d-a747-f5bed4c33e61 | -1.0368 | -53.5171 | 2024-10-03 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 29ff690b-c5d1-355e-b35d-33a61c82a6cd | -1.7509 | -54.4531 | 2024-10-03 00:05:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 6a3f6dd6-2e42-3aef-bf79-83c1edb21f97 | -2.9489 | -52.9174 | 2024-10-03 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6b189f2d-346e-3555-85a2-c9fa684f9050 | -3.3854 | -42.2866 | 2024-10-03 00:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| f96542df-78f3-3a5a-974f-12663705f740 | -3.3855 | -42.263 | 2024-10-03 00:05:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 1ea717d3-99bd-3243-ab8f-11bfe2d248cc | -3.4039 | -42.3094 | 2024-10-03 00:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 49.9 |
| e5923662-72bd-3111-8814-fe8bd8b8896c | -3.404 | -42.2858 | 2024-10-03 00:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 327.3 |
| 5352afb0-b200-36ec-bc86-6b259680fc8c | -3.4042 | -42.2621 | 2024-10-03 00:05:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 15b01145-9406-359c-b821-1600d71ec1ab | -3.4227 | -42.2849 | 2024-10-03 00:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 05b2944f-2865-3aa0-942b-baccd3820410 | -3.802 | -47.8104 | 2024-10-03 00:05:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a1151e6f-943f-3fc3-ace6-91147c1887be | -3.8021 | -47.7887 | 2024-10-03 00:05:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7d4614e8-1d49-380b-bbd5-2ef3d8a9696d | -4.0949 | -48.4894 | 2024-10-03 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 3bce4c57-cabe-397d-bf35-da2feafc23c8 | -4.095 | -48.4679 | 2024-10-03 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 22642d75-d8cf-30d3-9107-5efa212ffd78 | -4.1134 | -48.4886 | 2024-10-03 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 59357602-f647-316b-a34a-42dc0163e132 | -4.1135 | -48.4671 | 2024-10-03 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 22e5644c-e515-321c-9ed5-998a79976f57 | -4.4655 | -42.9112 | 2024-10-03 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| c1ca167e-1271-3c3b-80cb-fb024b62facd | -4.4657 | -42.8877 | 2024-10-03 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 199.3 |
| fc63c895-690c-38c9-a10f-db2984813ccb | -4.4844 | -42.8866 | 2024-10-03 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| fc0f0ff9-4004-30a2-94b4-d06169837f37 | -4.5373 | -43.3273 | 2024-10-03 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b1b9ff59-23b8-3490-b7dc-848a7dc87cd8 | -4.5375 | -43.304 | 2024-10-03 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| e06acff9-c9b7-3c33-90a9-ff89eb4218f1 | -4.4975 | -46.3953 | 2024-10-03 00:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 1192203d-df37-3e1e-8284-cdb289e49fab | -4.4977 | -46.3731 | 2024-10-03 00:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 868fe9b4-63d0-3bac-9974-a3df7cd54185 | -4.58 | -48.0132 | 2024-10-03 00:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 460f3930-0b86-3525-8a03-3f0622c80aaf | -4.8398 | -42.8875 | 2024-10-03 00:05:33 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 71b0612c-93bf-38f4-aa2b-29c23ccc01da | -4.84 | -42.864 | 2024-10-03 00:05:33 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 62d4b22f-eed4-3002-a7c5-648c328d20dd | -4.8586 | -42.8863 | 2024-10-03 00:05:33 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1fd4f64a-ef5e-3e88-a85a-494f373d65c1 | -4.8588 | -42.8628 | 2024-10-03 00:05:33 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3190bb74-f5fd-3348-be09-e9378494fb23 | -4.9264 | -43.79 | 2024-10-03 00:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 41322bc6-d368-3b9f-8de5-1541e73b565a | -4.9265 | -43.7669 | 2024-10-03 00:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 5c232300-9e67-367b-9d60-91f1432d46ec | -4.9451 | -43.7888 | 2024-10-03 00:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 5f48c448-6b99-33e9-b3ba-1c983dd6953e | -4.9452 | -43.7657 | 2024-10-03 00:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 99a18697-d206-30fe-9ae0-c48409d35119 | -5.2253 | -43.8164 | 2024-10-03 00:05:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 949f0c00-a22f-3942-b060-b81041773554 | -5.2255 | -43.7932 | 2024-10-03 00:05:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 5190b2b1-515a-3326-828d-f76991cb714d | -5.2441 | -43.8151 | 2024-10-03 00:05:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 306.7 |
| 312747e3-56e4-3683-9fdf-996bf33c4078 | -5.2443 | -43.792 | 2024-10-03 00:05:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 289.0 |
| dc898587-2a78-3b3d-9dd7-cfdff334fd55 | -5.8545 | -44.6217 | 2024-10-03 00:05:39 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 3c2e613d-7fcc-3786-95b4-9c8a497dccb6 | -5.8547 | -44.5988 | 2024-10-03 00:05:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| b1aab45f-f852-3274-9fef-a5913a212988 | -6.6453 | -54.952 | 2024-10-03 00:05:44 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| d9944f27-1ef6-3e8b-a09c-71083e2a981f | -6.7112 | -59.1345 | 2024-10-03 00:05:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 77804dbc-5549-3826-985f-39e1a8f16981 | -6.8777 | -59.0504 | 2024-10-03 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f90ac954-cee7-363b-a5a3-53d46416d09a | -6.8778 | -59.031 | 2024-10-03 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fc1d1835-372d-3e63-9e26-8f38a2856dc2 | -7.1871 | -59.7893 | 2024-10-03 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2ff4faf5-dbac-3aa6-b9b2-497b51a371be | -7.2055 | -59.8078 | 2024-10-03 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f76087c0-d627-3e8f-9935-bc26db843fab | -7.2056 | -59.7886 | 2024-10-03 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| fec88f64-9d3f-3e2f-9196-49a3a0742af0 | -7.3726 | -68.0177 | 2024-10-03 00:05:48 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 24bfd00b-6a3b-3c6a-a3d4-25528bb5ded9 | -7.6326 | -67.2013 | 2024-10-03 00:05:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| d93526f9-7336-3970-9715-feeb44ac4619 | -7.8785 | -72.805 | 2024-10-03 00:05:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 05d178bc-aca4-3c7e-976e-2ead93eeb11e | -7.8969 | -72.8049 | 2024-10-03 00:05:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ffb77886-86aa-39ce-a7fb-c09616fe459f | -8.9244 | -45.6367 | 2024-10-03 00:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| d7caa035-3478-31b5-af44-39b698192304 | -8.9433 | -45.6346 | 2024-10-03 00:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 64dd13ba-8e44-3d05-96bc-c0c376488940 | -8.6488 | -66.7139 | 2024-10-03 00:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d6b2957d-e1a0-312e-85cc-e1f9820acd58 | -8.6489 | -66.6953 | 2024-10-03 00:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7f2fa997-a225-3c24-b0d3-2b77cb6ed3ca | -8.649 | -66.6767 | 2024-10-03 00:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 3a06c4ce-fbc1-3423-9d3e-101258892895 | -8.6492 | -66.621 | 2024-10-03 00:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| c8f7e576-f736-356a-aad0-cc8aa00e5833 | -8.6493 | -66.6025 | 2024-10-03 00:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| e80fac6c-7139-3950-ac84-ada998a5c7b1 | -8.6674 | -66.6948 | 2024-10-03 00:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| cc081f06-71aa-3379-bde1-ba582ef56579 | -8.6675 | -66.6762 | 2024-10-03 00:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 255.8 |
| e762aea6-39de-3c7a-bc03-677382a7b873 | -8.6675 | -66.6577 | 2024-10-03 00:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 073e2a09-ab06-3fe9-87dc-6a5f42ff7f44 | -8.6677 | -66.602 | 2024-10-03 00:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| fb15880f-33cc-362b-ab35-82f668beb584 | -8.8926 | -62.3348 | 2024-10-03 00:05:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.6 |
| d6af63ef-9b9f-3db8-a42d-757d13f8b3c6 | -8.9791 | -67.4099 | 2024-10-03 00:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| fc269d1b-a01c-307e-af7c-34d75e57549a | -8.9976 | -67.4094 | 2024-10-03 00:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 38241d3e-a0db-32b6-bf63-bbb47f6e0f57 | -9.0149 | -67.7608 | 2024-10-03 00:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e2ad6d17-eed6-3b75-b2b3-af64be7817cf | -9.0149 | -67.7423 | 2024-10-03 00:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c9c306e8-c594-3859-93db-2eb72387a0ab | -9.0334 | -67.7419 | 2024-10-03 00:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 6120fab2-ff18-364f-a317-b81530f83641 | -9.0896 | -67.5738 | 2024-10-03 00:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| cff02e79-b90d-3528-b48b-8d10a1929595 | -9.1083 | -67.5178 | 2024-10-03 00:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 2ee048bd-c78f-32da-9ce2-f433ba5ae244 | -9.1566 | -61.6758 | 2024-10-03 00:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 6f8137c4-4335-33ce-a8fa-6f2b3c754625 | -9.1568 | -61.6567 | 2024-10-03 00:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| dd3faf3f-0676-3380-ba44-9b52a08a19bf | -9.1752 | -61.6749 | 2024-10-03 00:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 8264afe8-699e-3002-9cae-d19869da2b7d | -9.1754 | -61.6558 | 2024-10-03 00:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 4b12f6b3-c602-3b07-b2c9-839c7e962ad8 | -9.1997 | -67.8489 | 2024-10-03 00:05:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0d42c696-d5bb-3492-9f25-cc3ebf2988a1 | -9.2739 | -67.8286 | 2024-10-03 00:05:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 645da00e-7255-33e0-8f93-2d496af388ad | -9.3839 | -61.0526 | 2024-10-03 00:06:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| e90fae25-4096-39f8-83f5-98675c1b0d8f | -9.3652 | -68.1965 | 2024-10-03 00:06:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 1bdbda38-f0fe-37fc-8fdf-89d2ef5ceb60 | -9.3681 | -67.3998 | 2024-10-03 00:06:00 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 5239ad50-c6c3-3133-ac3e-f2aa755080e7 | -9.4025 | -61.0517 | 2024-10-03 00:06:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| da4c4a07-bae4-39ad-a0e8-cd356abababc | -9.3833 | -68.3256 | 2024-10-03 00:06:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 41.1 |
| c7f9a6f9-765e-3868-b7c1-b7f935ae3304 | -9.4244 | -67.2313 | 2024-10-03 00:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| aa132b43-7beb-3abd-ae45-a402195f95c3 | -9.4367 | -64.5607 | 2024-10-03 00:06:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6417805f-6bb4-3e7a-8100-a253aaee204c | -9.4368 | -64.5419 | 2024-10-03 00:06:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 177.3 |
| dfb264da-3bf1-3a44-be30-c903199527f6 | -9.4554 | -64.5412 | 2024-10-03 00:06:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d9804746-0042-3813-ac75-ea0d3f68bea0 | -9.468 | -62.3857 | 2024-10-03 00:06:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 50b25f2f-6ade-3234-ab29-f7bc4b6e1ae4 | -9.4865 | -62.4039 | 2024-10-03 00:06:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 100.0 |
| c99387cc-edbc-38f0-be18-99ff53325bed | -9.4866 | -62.3849 | 2024-10-03 00:06:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 142.5 |
| b878a8f6-ed9d-3b21-8960-876ceb95e920 | -9.4939 | -68.508 | 2024-10-03 00:06:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bfd25cf5-c01a-3818-b00d-9440c41bf4d8 | -9.494 | -68.4895 | 2024-10-03 00:06:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 78062cd2-ac2a-3a80-8c11-70b5dd337bd8 | -9.5125 | -68.5076 | 2024-10-03 00:06:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 41.5 |


[Clique aqui para ver as próximas entradas](README2.md)
