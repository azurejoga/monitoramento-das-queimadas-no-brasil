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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a515e2d-9ed6-3a86-babb-cd817210c24a | -7.42855 | -43.08743 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 183d2676-5fd9-30e4-b9c0-59d86ac374a2 | -6.41163 | -51.70801 | 2026-08-25 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0dd51d0e-41d2-384c-bc6c-3d391898fb91 | -7.30274 | -43.0044 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 95f66c59-f774-3cac-aa31-dbb29c244992 | -7.26577 | -45.85147 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4bc072f0-85a3-3e51-8b8d-eafd61b99755 | -6.0871 | -40.41829 | 2026-08-25 04:06:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7d710d85-7ab8-3621-8167-e47e28bc2731 | -6.77125 | -44.89788 | 2026-08-25 04:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eef6885a-4c7c-3457-a603-09ff6cbd9d82 | -7.15086 | -42.73994 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5c236c15-42bd-3e9b-937c-b42dce0d4d06 | -5.39364 | -43.60459 | 2026-08-25 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f099d697-2b23-3c61-a9c1-c729f5e98a5e | -7.30757 | -42.96822 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b53315ac-6ccd-3c46-bdd1-83f32e8bde52 | -7.15599 | -42.77931 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a192734-51ed-37d3-a46b-6ad0c50ce5cd | -7.4383 | -43.12428 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8f562e6b-4fba-3f5e-bbe5-c83ddb10f40b | -7.28093 | -44.07737 | 2026-08-25 04:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4cc31e18-1bd3-3cf3-9c69-d16c990b3499 | -6.97243 | -43.76242 | 2026-08-25 04:06:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fab5f56-8241-3237-b36e-28e91bd87726 | -7.44161 | -43.10463 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 24aefc3f-91e7-306b-908b-c67ddd950fa1 | -3.97114 | -41.51978 | 2026-08-25 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ae96de26-cd10-3355-8fa7-1abc882885b1 | -7.2649 | -45.8564 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dea7df00-27e1-3bde-957b-babd385b95a4 | -7.28572 | -45.36193 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 94e7fafa-fbf5-3777-9b5b-3cf5765d8164 | -2.89305 | -48.80899 | 2026-08-25 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 64cbb63e-f9cc-3e0c-a45e-f78fee0a6220 | -5.68223 | -43.27339 | 2026-08-25 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b159ec82-2391-3e67-b6db-e5477f7b2116 | -6.41077 | -51.71378 | 2026-08-25 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c761685-a5d1-39f7-b667-cd94958112a6 | -4.05302 | -48.96164 | 2026-08-25 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0f0849a-ed37-3973-a8e7-88734baab2d4 | -3.01543 | -51.05385 | 2026-08-25 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b54be6d4-8d1e-334c-9833-63cac97e37bf | -7.14769 | -42.75863 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11b72f84-b4f5-39fa-8c46-0e1c5731b60d | -7.29023 | -45.36275 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3fddf4a7-6cc5-3177-817a-d32e1cc83c7d | -6.29585 | -43.79832 | 2026-08-25 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91574eba-00ec-3fe0-b5b8-ae207769f197 | -7.19284 | -42.74681 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b8303bbd-4eb8-3dd3-9896-9d12bac2d52f | -7.64843 | -42.7281 | 2026-08-25 04:06:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1c5b552-f5ed-3c50-9084-3b4db0ce2a2b | -6.40463 | -51.70737 | 2026-08-25 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 390ccdad-661f-365d-af97-28ea6ced2c93 | -7.48282 | -44.4679 | 2026-08-25 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78704f57-edcc-38a2-80dd-02ec6bb0900d | -5.79818 | -43.64443 | 2026-08-25 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9838123e-e6a4-3928-8e9d-c0cff8d22eba | -7.30201 | -43.00209 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1b3e2f08-572b-35f7-afc5-86b26cedf166 | -4.12603 | -49.44936 | 2026-08-25 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3f4f0d5-ec8d-3b11-a806-b4b961ca931f | -3.53442 | -48.18549 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0f0f1f71-0797-3761-8869-9868124c2b04 | -3.54095 | -48.1823 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 8011ae09-2092-38fc-9759-e53dd9d867dc | -7.18599 | -42.7409 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 25c386fa-5001-3003-ba62-2b8083e6cf34 | -7.16127 | -42.79468 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 971d41a3-a16f-3e7b-a484-95fb02020930 | -7.06231 | -42.9269 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9ba7d50-aa29-3cc5-8fa7-7043947a135e | -7.26665 | -45.84654 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 09f80ae5-9ce1-36bc-a434-b028c403a66a | -6.78712 | -44.69974 | 2026-08-25 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0c743d3-1dcc-32c4-9b0a-b47af9707be7 | -6.16994 | -43.76704 | 2026-08-25 04:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b2be8cc-3f98-3e33-bdb5-1bbd61a7f1ec | -7.2669 | -45.3632 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 529b08ce-e479-3224-bdc9-10f28ac5b22d | -7.26983 | -45.3731 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 985c0fbf-cbee-309e-8547-65913d62ca42 | -7.29249 | -43.01775 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c21fc448-0a3c-3fad-9839-8d557ae0dade | -7.2608 | -45.37153 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0e06ffa7-607e-38d9-ad97-f0d1848b6e57 | -7.26 | -45.37613 | 2026-08-25 04:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12b18f9f-96cd-3659-9bc0-80ea01def694 | -7.25093 | -45.85376 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 02cc8fae-0111-35a6-a228-6b042ac0dba7 | -7.14848 | -42.75398 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 69f13efd-f19a-3db9-8979-9f168c4ae387 | -4.79999 | -43.07981 | 2026-08-25 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e432d44b-506f-38c1-9f89-e61019e70281 | -7.1898 | -42.74152 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 69fead78-034e-35d4-8bb8-918bfc43eb13 | -3.5286 | -48.18457 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9ab5ffb3-9cde-3a7a-a10d-3043665f5ea9 | -4.03362 | -38.20559 | 2026-08-25 04:06:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42cc485e-e616-3cba-8b6c-47d721b2d41a | -4.12316 | -49.44957 | 2026-08-25 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16a10229-991c-3eef-9a3c-1d5af3d7e69b | -3.04514 | -48.98602 | 2026-08-25 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01a74ebd-5076-358c-ada9-1dd0db8d233c | -6.45235 | -41.56037 | 2026-08-25 04:06:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d5635295-cfce-3d8b-a7be-404d0d83a375 | -7.15153 | -43.44362 | 2026-08-25 04:06:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 264c4ce6-a1df-30a9-9994-a9a6afae0722 | -7.13148 | -42.78468 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d1bd58f-a4c4-3fb2-9ae2-08a5fd955efe | -6.72218 | -38.23803 | 2026-08-25 04:06:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 82a96ee1-d104-3a02-9423-8282946fb2e7 | -4.05224 | -48.96614 | 2026-08-25 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3476af3c-de03-3df3-a8c1-b98969a339d7 | -7.43136 | -43.11803 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a4f6a8e7-c3ea-3598-974e-380c32813e8d | -5.98318 | -43.74402 | 2026-08-25 04:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72e96557-7450-381f-be9b-f533215b309b | -7.44243 | -43.09979 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2c8c44a3-1003-39b2-8426-d7a29597dc9e | -7.4508 | -43.12127 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aaa4568c-7279-3df6-995a-89955f423727 | -7.48656 | -44.46751 | 2026-08-25 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbcefb2f-e86e-3a05-8c83-a81a41401962 | -7.26611 | -45.36774 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98abbeb4-77e1-30e5-8873-abf4390c4650 | -3.53368 | -48.18976 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7bc4e5ed-1c60-3e60-8598-97bb3234562f | -5.7564 | -48.67423 | 2026-08-25 04:06:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f979b1af-5a62-3d31-8af8-0e2a4a847a93 | -7.43607 | -43.11378 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 36c920c1-6bd7-3e4a-b75a-c17ca6aad0c5 | -4.43332 | -43.40631 | 2026-08-25 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 217adc8e-02af-38ea-b8a6-117e001bfa86 | -1.87076 | -47.98331 | 2026-08-25 04:06:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbac59a0-fc0c-3453-9af5-81a40bae0476 | -7.18217 | -42.74026 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7aaab11a-4b0b-33d7-8532-ce2fb6edf6de | -5.98474 | -43.74439 | 2026-08-25 04:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8c7fbed-fdc0-3348-8332-c891baaf7522 | -6.95108 | -42.68655 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a123e6b5-fcde-3c5f-800b-b917996bd7fd | -7.30041 | -43.01184 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 62ee8e51-9adb-3f0e-adbb-cf194bbae378 | -3.53653 | -48.1733 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f17838bc-deff-3828-a801-b267cba193ae | -7.43441 | -43.12362 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fcf4a46f-8b01-30c8-9765-3e8364e1b196 | -7.43384 | -43.10332 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8f2c43e5-0ae0-3e2c-811f-841c0fd900cb | -6.32496 | -44.85452 | 2026-08-25 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4759dedb-ec8a-35ff-8092-15ab18473ec3 | -7.28157 | -44.07365 | 2026-08-25 04:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4fcd4b53-e9ed-34bf-89cb-c3af49084cdf | -7.43053 | -43.12294 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0374458a-63be-3a36-9750-4e77a652dac4 | -7.1951 | -42.75682 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| def9a76c-2021-3c05-a2ed-9c02b136de8b | -7.30853 | -42.9706 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3de52ff9-0497-3efa-a0c1-a56a949262c2 | -7.47859 | -44.46712 | 2026-08-25 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65826602-ad9e-397d-bad5-8d35d8539261 | -1.59376 | -47.35829 | 2026-08-25 04:06:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 238374a9-367c-31ce-abf5-a687acad3aa4 | -1.86488 | -47.98234 | 2026-08-25 04:06:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec173d48-f253-37bf-b452-17912ddd0bc7 | -6.64385 | -45.16594 | 2026-08-25 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 877b5c8c-e3c0-311d-9865-34a76692e3ce | -5.98257 | -43.74771 | 2026-08-25 04:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edc494f2-f1e1-39f7-9951-b6ce1a6cd136 | -7.30371 | -42.9676 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 206948b6-834f-3edd-8bc8-a9c69b6e46ec | -7.30121 | -43.00695 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c3fec174-c695-3c6d-af91-42ee645dd0eb | -5.68627 | -43.274 | 2026-08-25 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a34fe729-d651-3982-b2d8-a42384deae80 | -7.43524 | -43.11869 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f9fcd6e9-401b-38b5-9b54-f08cad46fb3c | -7.30191 | -43.00927 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0cca6e5c-4750-3292-ae15-d11599c1fd73 | -7.18903 | -42.74616 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e6fc4688-c9be-331c-863f-a2d81c7510c9 | -6.8084 | -42.66778 | 2026-08-25 04:06:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4f01e1be-1e9b-34da-8786-e4229d7ae557 | -2.95401 | -40.35534 | 2026-08-25 04:06:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f6144ac6-fb06-3cf1-8308-af623c616d0a | -3.04593 | -48.98133 | 2026-08-25 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f109407-af4b-3191-8b49-82253aa7397c | -4.71697 | -42.77205 | 2026-08-25 04:06:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 187806b3-1a64-3977-92f9-772606f44a67 | -7.16047 | -42.79941 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c318174e-3fc8-3817-b9b9-be2b24d7cf6d | -7.44711 | -43.09565 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| faf274a5-d37d-3efe-9687-0d6f85fb1613 | -7.43773 | -43.10397 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6846dd1a-24e0-365a-9f64-9a4b1774af26 | -7.48705 | -44.46866 | 2026-08-25 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
