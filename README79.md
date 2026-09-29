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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5a2def7-d489-30e8-88e0-9f9e436b5652 | -10.7913 | -48.7596 | 2026-09-29 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5654f533-073e-3ebd-a6e0-4970240c49d1 | -12.1557 | -50.3089 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| c234a770-6592-3c91-bc00-044d6a86cf3b | -10.2843 | -44.6274 | 2026-09-29 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 5e056437-f2b0-348c-9be3-24de5511d5c0 | -12.7421 | -47.2684 | 2026-09-29 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 276.9 |
| 55b962fd-7770-3973-a962-33659f041e26 | -4.7166 | -44.3552 | 2026-09-29 14:00:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 69e018cc-2759-3587-8a46-52a78a06daac | -10.9861 | -49.7131 | 2026-09-29 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1bc50901-c623-3073-8c6f-7b0ef73170f5 | -11.3739 | -43.3972 | 2026-09-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 810e71d6-8114-37d8-a74c-3648e6a6a389 | -11.4601 | -49.7452 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f382aaab-5c0b-33e7-8012-667c14e1baa3 | -11.1907 | -45.1274 | 2026-09-29 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 728a9555-86c3-3bf1-ad0b-24aa32b89e11 | -11.905 | -50.5103 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f6302d62-9405-33c5-89ff-bb1b6391350a | -11.0241 | -49.7088 | 2026-09-29 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d5cda859-2083-3996-bcf0-f270b220332e | -11.1771 | -44.8064 | 2026-09-29 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 285.7 |
| 7d9275bb-afec-3c5d-9d0c-83ebc7023616 | -7.3967 | -42.6261 | 2026-09-29 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 128.4 |
| 1541fe2e-dcee-363c-a022-4e4a4714595f | -12.0559 | -50.5996 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b483d381-6e7c-3728-ac9a-6f711fcb9a99 | 1.822 | -55.6247 | 2026-09-29 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 29505e1c-746c-348a-88e0-5dd85c63568c | -20.9155 | -57.8456 | 2026-09-29 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 138.7 |
| 6136a533-02ac-3e79-af09-91fe08226b14 | -15.3802 | -47.9294 | 2026-09-29 14:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 901acf06-7d13-3b4b-a64d-89b36decff42 | -10.7916 | -48.7377 | 2026-09-29 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 5c17c19a-3fb2-3aff-ac98-207031851b93 | -9.8064 | -44.8265 | 2026-09-29 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 43c84874-305d-3904-8d51-4ef99b669751 | -11.4791 | -49.743 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 0be9d3bb-cf3d-31f4-ba31-113aeeebf18f | -9.2051 | -45.8322 | 2026-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 8bfe6eb1-01f7-3b01-9d7d-1e39ef4c9a54 | -13.6762 | -45.7822 | 2026-09-29 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 8a01b09e-c62c-3096-8fa3-a44f07f4117b | -12.2304 | -50.4073 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 836d014f-e329-3906-9d57-a3382a200529 | -6.2401 | -41.6153 | 2026-09-29 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 89e974d3-36a5-3206-9616-12b912dfdd3b | -11.8678 | -50.4504 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 775449dc-790b-3e17-989c-3dba346d0ef6 | -12.1734 | -50.3927 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 7143d127-087b-337d-8ef4-4d4e3d2981d3 | -11.924 | -50.5081 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f8d5040b-f190-3a82-9226-b4fe25dcf58d | -12.7598 | -47.3555 | 2026-09-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 7142b4a2-958d-33c8-affa-f6a2affc3b90 | -12.1366 | -50.3112 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| f373192d-c9f3-32f7-98dc-d0bb8ff6dfd0 | -11.3743 | -43.3734 | 2026-09-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 526989c4-802a-3fb4-9018-18b05f3d0dfc | -11.8672 | -50.4933 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 40b9f417-aa10-37e9-a9d2-8c0f48386a8e | -7.0679 | -41.7288 | 2026-09-29 14:00:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| b6c87248-548b-3e97-90b7-4e3e6bd7914a | -10.3895 | -61.231 | 2026-09-29 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 5af4afe3-810f-3bf3-8955-95a2512b54b7 | -11.9047 | -50.5317 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a1bcd081-1d2a-3cc0-aeac-2b6a288f96f2 | -20.9159 | -57.8246 | 2026-09-29 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 150.6 |
| 510313aa-b66b-346a-8a97-31bb66b41e6b | -12.7417 | -47.2909 | 2026-09-29 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 88c62a76-980e-332b-b9ad-9009c4252a8f | -11.3931 | -43.3942 | 2026-09-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 5a762c04-a4ad-3498-9171-bdde8abc5c5c | -15.4003 | -47.9035 | 2026-09-29 14:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 5c73966c-76eb-3779-ac7f-e5152435b60d | -5.4405 | -47.2676 | 2026-09-29 14:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2aceef19-d5cf-345f-9001-511633a64e41 | -11.678 | -43.5396 | 2026-09-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| cd99b015-5373-3393-bfb4-3e5476c56ae2 | 2.1082 | -50.8583 | 2026-09-29 14:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 34b1a9ef-41b4-3f38-bd77-611156034ea1 | -11.1907 | -45.1274 | 2026-09-29 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| bcd47ae4-ebef-3952-a80b-43722c207ed5 | -15.516 | -41.3264 | 2026-09-29 14:10:00 | GOES-19 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| bb281235-e4bc-3ec2-8756-3fa11600c3a7 | -10.3895 | -61.231 | 2026-09-29 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 454d7f8f-ea13-3ad5-b8c4-7e146805afd2 | -10.3894 | -61.2502 | 2026-09-29 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 5ced83a0-020d-36db-90a7-bc139d8a60c0 | -13.6762 | -45.7822 | 2026-09-29 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 56b0a405-e2ce-3bb7-bab8-41a4555fc3a7 | -15.3998 | -47.9261 | 2026-09-29 14:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| d9a0ee1f-964c-392f-a2c3-43761e29fcf5 | -8.2293 | -45.4375 | 2026-09-29 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b7dad960-20a7-3a19-bab8-4770a10f52ef | -10.2843 | -44.6274 | 2026-09-29 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| e3a26ab0-2cd8-33bd-b9a7-a90bd40a7176 | -15.4003 | -47.9035 | 2026-09-29 14:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 438972ea-aafa-3bc5-8718-80a2293678cb | -11.3927 | -43.418 | 2026-09-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 68d2ad54-3ddc-3778-9f7a-d83edd4e4d0f | -8.6451 | -45.3489 | 2026-09-29 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| e03af583-69ad-3231-886f-357f524b3d8a | -14.1309 | -46.2801 | 2026-09-29 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 192.7 |
| b4ae4085-9376-3a59-8846-2636569f6778 | -8.2102 | -45.4621 | 2026-09-29 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 6da4a453-27c4-3eb4-8352-8f13666b7d88 | -8.0355 | -42.866 | 2026-09-29 14:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 147.7 |
| 9a3caf7b-6745-31fb-ae78-06eba3a35669 | -9.0739 | -47.189 | 2026-09-29 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 5f1b07d8-0c16-3546-9482-702a2f191092 | 1.6932 | -55.942 | 2026-09-29 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 36917658-8011-3a1f-9112-3bb00de96463 | -11.9609 | -50.5894 | 2026-09-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d94e86ac-7092-3a83-8cfe-80fd1172003b | -13.3469 | -46.8169 | 2026-09-29 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 5a94bbe5-1ed9-3007-9f6e-5e9d1edf908c | -13.3835 | -44.0132 | 2026-09-29 14:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| fd7c2081-301f-3d3c-a4c6-8a755ef6b845 | -15.5154 | -41.3515 | 2026-09-29 14:10:00 | GOES-19 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 250.9 |
| 93e3255e-c160-3d59-9003-9c4b6e76da1e | -9.0463 | -45.0083 | 2026-09-29 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 172fad56-90e2-3c53-be3b-b807d64b805d | -12.2723 | -50.1657 | 2026-09-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1703247c-1387-3ac3-b335-fd5431d84117 | 1.8403 | -55.6244 | 2026-09-29 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 70573f0b-f01e-3ba6-ba1d-8e3bfc1f61ba | -11.9845 | -50.2864 | 2026-09-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 23dd2fe8-d44d-3c6b-9daa-205d5f2b94b7 | -8.9823 | -44.1633 | 2026-09-29 14:10:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c504837c-1c5a-333c-b597-91abe0489673 | -8.0169 | -42.8444 | 2026-09-29 14:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| f1272a00-e552-3f14-be8e-dc0689d20f7e | -9.1337 | -49.9656 | 2026-09-29 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| b499d178-7913-3040-91df-7949f28fcc1f | -9.8064 | -44.8265 | 2026-09-29 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 71255591-a139-3441-8601-80d620015a68 | -20.9159 | -57.8246 | 2026-09-29 14:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 126.2 |
| ece43e3e-95dc-3b3a-946a-fc481238233e | -12.7421 | -47.2684 | 2026-09-29 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 73419cf9-7899-35c5-991c-5ab71d7faa71 | -8.0358 | -42.8423 | 2026-09-29 14:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 31d0e646-08a4-3b9c-a6e0-56c25f0c9c3a | -14.1115 | -46.2834 | 2026-09-29 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 8e3d2d3d-e349-3886-953f-77f80a97165c | -14.639 | -52.1307 | 2026-09-29 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| c3c9f1e5-b9c6-3924-ad3a-ce0755f9170e | -11.3739 | -43.3972 | 2026-09-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 39a61455-ff92-3544-b509-af5b36138c33 | -12.7798 | -50.6834 | 2026-09-29 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ce24cc0e-bf52-3571-955d-3fe77da77bb9 | -8.9397 | -45.9064 | 2026-09-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| fed53782-9ceb-3e29-a3f2-74116fdae1d6 | -14.5168 | -48.2958 | 2026-09-29 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 68882bdf-d54e-32da-9dd8-e9d22deed333 | -12.6271 | -47.2626 | 2026-09-29 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 0e01edac-dabb-3adf-85a7-d9d2cf9f6751 | -13.1803 | -48.5409 | 2026-09-29 14:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 31d37ad5-447a-3f3b-84db-85809b7a37f0 | -20.6905 | -57.9607 | 2026-09-29 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.1 |
| 52cfc84a-361e-33b6-b66f-4efb555618cf | -9.7877 | -44.8058 | 2026-09-29 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 27fad8b8-3f82-3a0d-8680-e1e18a1c1dee | -12.4966 | -44.9567 | 2026-09-29 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 71c74fc0-c704-3cce-a7ff-c91c61c5bfc5 | -12.7801 | -50.6619 | 2026-09-29 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| aab265bd-e03e-3d23-961f-172e90743dff | -11.1771 | -44.8064 | 2026-09-29 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 476.9 |
| f5da9f33-17a3-3162-9a5a-30791f80f1c5 | -11.1178 | -51.1304 | 2026-09-29 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 89b25b1d-690c-39e6-83b2-8fea3cb3e586 | -10.8944 | -50.8569 | 2026-09-29 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| f0f5c8a8-0a9d-3e6b-929b-4bdd17e6f0ce | -10.7255 | -44.4291 | 2026-09-29 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ffed73db-f186-3ac1-90e3-f2768822b0ac | -12.374 | -46.3972 | 2026-09-29 14:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d22c2090-1118-38f0-9c83-16ce72e788a8 | -15.3807 | -47.9068 | 2026-09-29 14:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e17fe710-4bf7-3bbf-9853-710f9c982b86 | -15.3802 | -47.9294 | 2026-09-29 14:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c0f45d2b-6105-3e06-ab49-a7d8bbb905be | -9.7874 | -44.8289 | 2026-09-29 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| d0e04227-b108-3b1b-929a-402cb5a32882 | -18.0956 | -44.355 | 2026-09-29 14:10:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 9e591408-e428-355b-a2c5-2abd148a20ef | -12.6078 | -47.2653 | 2026-09-29 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| a48eb64a-a893-34ae-8ff5-a37732b3b02f | -11.4791 | -49.743 | 2026-09-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 5b8f416a-b0eb-3892-abe9-9595acf0ac94 | -12.8847 | -44.8015 | 2026-09-29 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| fd5bb3c9-e881-3682-8ac8-151df345c0d9 | -7.4156 | -42.6241 | 2026-09-29 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 496b68d2-94e5-3299-9924-312dc93c7bbf | -12.0365 | -50.6233 | 2026-09-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a9246f13-b4ae-380a-85b7-35e97f96f930 | -10.7913 | -48.7596 | 2026-09-29 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 80965f17-2408-3caa-9c18-b15bcaecfc42 | -11.3743 | -43.3734 | 2026-09-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 250.9 |


[Clique aqui para ver as próximas entradas](README80.md)
