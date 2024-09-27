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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 113d6343-8d39-331e-90b7-fd2cd81bc470 | -10.624 | -46.0023 | 2024-09-27 10:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 7c2c7e7e-a3ea-3f98-8a98-5c8789f73bdd | -10.6244 | -45.9796 | 2024-09-27 10:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 39e30968-3cd7-3a09-b1a6-70f9f7e717f0 | -11.0577 | -51.3694 | 2024-09-27 10:36:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 157afc97-71c6-3ca8-826a-5bb7abded4da | -14.7305 | -45.5061 | 2024-09-27 10:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 229.1 |
| b2b7b600-a333-39fa-8306-8da81e9eb6bd | -14.731 | -45.4827 | 2024-09-27 10:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 48c9fefe-bbe5-3d6d-a780-1eb6342ace39 | -14.75 | -45.5025 | 2024-09-27 10:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| ea0eb1fd-47bc-3909-85dd-63905aeb083d | -14.903 | -51.4319 | 2024-09-27 10:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 232dbb2e-95e0-3ac1-8e12-ca96f1878586 | -10.0141 | -53.4258 | 2024-09-27 10:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 232.8 |
| e3a15a07-8913-316a-af87-9b0f444f8ed0 | -10.0139 | -53.4464 | 2024-09-27 10:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 596.3 |
| da8ce718-0186-3789-ae28-599f5223be0a | -10.0517 | -53.4226 | 2024-09-27 10:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 8ea8cab5-c23f-3aca-abc3-aa585ff31004 | -10.0515 | -53.4432 | 2024-09-27 10:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 190.6 |
| 3fd2c783-3ee2-373e-856a-2510fadde493 | -10.0327 | -53.4448 | 2024-09-27 10:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1361.6 |
| d5c7f8d5-8a8d-30f7-b994-01166319fda2 | -10.605 | -46.0047 | 2024-09-27 10:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 717836f9-af1f-37b3-b1a1-32afbb15ee4a | -10.624 | -46.0023 | 2024-09-27 10:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 702d28c2-96f8-3a90-9f17-f59fa1684866 | -10.6244 | -45.9796 | 2024-09-27 10:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a5acb3f8-313a-346b-b64c-7d4905d75ac8 | -11.0577 | -51.3694 | 2024-09-27 10:46:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 0358a314-8ae7-3e41-b148-b32384be1bb3 | -14.731 | -45.4827 | 2024-09-27 10:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| c6ef0884-8813-349c-9331-8925dad04eb8 | -14.7114 | -45.4863 | 2024-09-27 10:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 186968b5-c2de-3233-b147-a240138c4e6d | -14.7305 | -45.5061 | 2024-09-27 10:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| d104ae1b-eb8d-3a5d-92a3-98669c9576a1 | -14.9026 | -51.4534 | 2024-09-27 10:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 272.4 |
| 3a2d3b6e-96cc-39f8-83ad-cfd5e64cd7db | -14.922 | -51.4507 | 2024-09-27 10:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 0e0d7506-a669-399f-b192-230952fb83cf | -14.9224 | -51.4292 | 2024-09-27 10:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 9e819495-9905-33af-a051-164c81dfb839 | -14.8443 | -51.4616 | 2024-09-27 10:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 2c4bfef8-7829-3553-ab73-6f0ed4b73c0b | -14.8835 | -51.4346 | 2024-09-27 10:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e70147f8-8849-31be-99a9-87d4a5e8e90b | -14.903 | -51.4319 | 2024-09-27 10:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 281.4 |
| e225c2b0-c509-375f-9528-9d13bf7818b4 | -16.0793 | -51.9709 | 2024-09-27 10:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 11ee5005-305f-3b90-b4e9-58912ff2845d | -10.0139 | -53.4464 | 2024-09-27 10:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 525.8 |
| f9cc24dd-4929-346a-a903-b9d836bf2384 | -10.0136 | -53.467 | 2024-09-27 10:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 123cd705-5612-3875-9b89-2494aff45fc9 | -10.0141 | -53.4258 | 2024-09-27 10:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 234.1 |
| 7f113fbe-e82f-3e6c-97c4-16522b24ff1e | -10.0327 | -53.4448 | 2024-09-27 10:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1415.0 |
| 1c364276-469e-37ff-a362-1816b7ac7531 | -10.0322 | -53.4859 | 2024-09-27 10:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 8b5fb76b-65ad-3197-a607-86e7c5085790 | -10.0324 | -53.4654 | 2024-09-27 10:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 478.8 |
| 958f08c2-f94f-3ab3-a63d-1ece07027be3 | -10.624 | -46.0023 | 2024-09-27 10:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d289cd66-a957-3e8a-a7aa-8a425b7fcc31 | -12.7351 | -45.566 | 2024-09-27 10:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| d26b9b4c-547b-33b2-98e4-922902b81a47 | -14.75 | -45.5025 | 2024-09-27 10:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| f6809f31-30e8-3d1e-9ea7-f8ce73caf674 | -14.731 | -45.4827 | 2024-09-27 10:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 4d360fc5-2573-37d6-a505-6561b1180c5d | -14.7305 | -45.5061 | 2024-09-27 10:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 256.7 |
| 6d3d0462-aec1-3d06-8d05-59f5e5cf2a61 | -14.7114 | -45.4863 | 2024-09-27 10:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| f8c976de-c246-3bc8-926e-3b096b82ee42 | -14.903 | -51.4319 | 2024-09-27 10:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 231.4 |
| f3414c17-5cf6-3bf9-9e3f-ccac92e34aac | -14.9026 | -51.4534 | 2024-09-27 10:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 230.3 |
| bed8a790-d93a-3eb7-b129-46f3ded3c5bc | -16.0993 | -51.9465 | 2024-09-27 10:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 6a6cd4dd-9b67-3b0b-8c96-203b98d031cb | -16.0989 | -51.968 | 2024-09-27 10:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| b2d79f60-70d5-3562-8541-fd6d80d206b3 | -16.0793 | -51.9709 | 2024-09-27 10:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 596bf14f-ad7e-3196-bdad-f2327b916c3d | -14.72 | -45.5 | 2024-09-27 11:04:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f98d54e-ac03-3771-a76c-8e9cdc4fd62e | -10.04 | -53.48 | 2024-09-27 11:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07fc94d4-d877-33a6-803d-f5bef50dd54d | -10.01 | -53.41 | 2024-09-27 11:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 781be289-c1bd-3741-b31f-174f71ecd742 | -10.01 | -53.48 | 2024-09-27 11:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31bda6c6-97bb-32ef-b340-07d887676caa | -10.04 | -53.42 | 2024-09-27 11:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af6b759e-714b-3a4f-999f-5b12eb1b0c1a | -10.624 | -46.0023 | 2024-09-27 11:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 214.3 |
| 1fbeeed5-eb3e-3013-97f0-c74d43ae8699 | -10.6244 | -45.9796 | 2024-09-27 11:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 1509531e-786f-3d19-9d82-87ff67ef2434 | -12.2371 | -45.4815 | 2024-09-27 11:06:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a4170bff-073c-35b0-aafd-f8ad3adb6d95 | -12.7351 | -45.566 | 2024-09-27 11:06:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 291.9 |
| f8429c9b-3c93-302e-b040-0c1e69ed2198 | -14.7305 | -45.5061 | 2024-09-27 11:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 607.0 |
| 0ab3b9a2-e650-38a5-84b7-e93ab16a5f60 | -14.7114 | -45.4863 | 2024-09-27 11:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| cb7af08b-5c6d-3f14-81fe-8f84d583b6d6 | -14.73 | -45.5294 | 2024-09-27 11:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 02ecacfb-50ca-3636-a2a8-ee5928e5d248 | -10.624 | -46.0023 | 2024-09-27 11:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 90ba24e2-c450-3342-a89a-a15c20146300 | -11.0972 | -46.1673 | 2024-09-27 11:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 0dfcda35-fccd-3ceb-8c92-7e38537f81f4 | -12.7351 | -45.566 | 2024-09-27 11:16:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 65bcb6f5-18d3-366d-81c8-0719d3d6f9d2 | -14.73 | -45.5294 | 2024-09-27 11:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 6e27d081-98b3-3286-8f69-c749d7738908 | -14.7114 | -45.4863 | 2024-09-27 11:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 75570362-2064-3f61-8c76-75f8931e725e | -14.7305 | -45.5061 | 2024-09-27 11:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 817.0 |
| 1bcfb707-98e2-3718-a343-c53d57ba5939 | -14.8443 | -51.4616 | 2024-09-27 11:16:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 32406a08-53b1-3e11-b98b-a18cbad8ad66 | -10.0134 | -53.4875 | 2024-09-27 11:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 99a20b77-be7e-3813-a587-efaa2dcc3ba6 | -10.0136 | -53.467 | 2024-09-27 11:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 219.7 |
| 7a0ecfb3-40c2-335f-ab92-b0eeee10d996 | -10.0139 | -53.4464 | 2024-09-27 11:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 467.5 |
| 9cd80159-147c-3d19-88b2-79fef8d2dc6b | -10.0322 | -53.4859 | 2024-09-27 11:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 262.3 |
| 42cf88d9-e0ad-3f74-8e6f-64f7ebb7639d | -10.0517 | -53.4226 | 2024-09-27 11:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 1ae8091f-137e-3137-88f5-8257232fb0d3 | -10.0324 | -53.4654 | 2024-09-27 11:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 603.8 |
| 047befbc-233a-3151-8b0e-af013a0c91dc | -10.0515 | -53.4432 | 2024-09-27 11:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 246.1 |
| 71536b3f-81f3-30ee-8617-dc5534461e4e | -10.0329 | -53.4242 | 2024-09-27 11:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 768.3 |
| 72be9c8f-a3e1-3fe0-829c-1ac642006c5c | -10.624 | -46.0023 | 2024-09-27 11:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6b80d23c-e147-324e-b477-b40fa722a75b | -10.8334 | -45.998 | 2024-09-27 11:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0ccdd15c-76df-3759-9cbe-660288b53d36 | -10.8143 | -46.0005 | 2024-09-27 11:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1c748395-1a0f-3ba1-9e8a-81fcb4c93219 | -11.2025 | -45.5616 | 2024-09-27 11:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| be4b9486-d954-3a35-98c9-91e19155fda4 | -11.0972 | -46.1673 | 2024-09-27 11:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| d0e7831c-a61f-37c5-b5f7-5e702fc8e87c | -11.0969 | -46.19 | 2024-09-27 11:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 396006d0-1c1e-34b1-b4fd-f91a0a3dc7c1 | -13.3376 | -46.2957 | 2024-09-27 11:26:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 533fa0c4-9d7f-3211-ad08-d02c98cd47b9 | -9.417 | -51.4426 | 2024-09-27 11:36:01 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 5ca675ad-d741-3080-b3f5-ae4444177b80 | -10.0324 | -53.4654 | 2024-09-27 11:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 824.7 |
| 90c38198-ea39-3da6-8f1f-9504330ad8fb | -10.0515 | -53.4432 | 2024-09-27 11:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 201.6 |
| 3eedadc8-4e59-3058-b68c-6759f18bf04a | -10.0136 | -53.467 | 2024-09-27 11:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 197.0 |
| f29a8430-86aa-3861-aaf6-9914cb1c0735 | -10.0139 | -53.4464 | 2024-09-27 11:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 394.4 |
| 5734f565-24ad-3144-b407-474b28bf1f6e | -10.0329 | -53.4242 | 2024-09-27 11:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 615.6 |
| 2c187bca-54dc-3acb-bfab-fb90bc4b5a05 | -10.0322 | -53.4859 | 2024-09-27 11:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 241.4 |
| f159bb61-b093-320b-b293-9f45c9eac3ef | -10.0517 | -53.4226 | 2024-09-27 11:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| f2151b35-016f-3fed-9ba8-cb529aa484fd | -10.6643 | -45.861 | 2024-09-27 11:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8762b764-e640-312f-b4be-47ebc11b2a5c | -10.8337 | -45.9753 | 2024-09-27 11:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 032bdeab-815f-311c-b092-06bc144a3fda | -10.8146 | -45.9778 | 2024-09-27 11:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0e28425e-cd64-3c5b-a45f-9bbb9b81e8a5 | -10.8143 | -46.0005 | 2024-09-27 11:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 56362e9d-9b46-3508-8757-70ce7ddf43da | -10.8334 | -45.998 | 2024-09-27 11:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| fc660365-9064-318e-8daa-fa454496fd7e | -11.0972 | -46.1673 | 2024-09-27 11:36:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| e5c8fab5-6e91-3e0d-8376-b97adff3e240 | -11.2025 | -45.5616 | 2024-09-27 11:36:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 3ba5f955-da04-3e33-bafb-f6bd13275b68 | -11.6605 | -44.5041 | 2024-09-27 11:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 4691efa9-a480-3647-9d82-897c88ce3302 | -11.6409 | -44.5303 | 2024-09-27 11:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| ffa0171d-a2b3-3b77-bf61-413543d9f741 | -13.2796 | -46.3049 | 2024-09-27 11:36:22 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 167.7 |
| e84db328-178d-3d73-8bab-f60327d9280b | -14.7114 | -45.4863 | 2024-09-27 11:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 70395fbd-72c5-3961-82bb-46038a0f1bff | -14.7305 | -45.5061 | 2024-09-27 11:36:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 376.0 |
| 374cdf45-9d0c-38bd-94d9-0585500e34b5 | -14.9026 | -51.4534 | 2024-09-27 11:36:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 550f96c2-09db-32b7-8b12-25aae95b42ca | -19.7933 | -47.0209 | 2024-09-27 11:36:57 | GOES-16 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 622bf00c-09fa-3dbf-83ef-afe1d5c9f1e8 | -8.839 | -44.9628 | 2024-09-27 11:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |


[Clique aqui para ver as próximas entradas](README133.md)
