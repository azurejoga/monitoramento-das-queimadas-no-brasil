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
| 8fb49b7e-2455-3c09-8aa0-fa4afdbdea07 | -10.6319 | -44.3257 | 2025-01-04 01:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 81b50192-4eda-39c5-b41d-0f85e1cd2281 | -10.6124 | -44.3517 | 2025-01-04 01:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| f73cbf58-079d-36be-92d5-39a1cf90a0c7 | -9.8359 | -36.1958 | 2025-01-04 01:10:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 127.0 |
| 0b767710-29d5-3518-88c5-c00bb64db3f5 | -10.6128 | -44.3284 | 2025-01-04 01:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 787f0a66-243d-35f0-a928-b32cc884498b | 1.3218 | -60.3123 | 2025-01-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 903c5e80-73a9-36b5-be88-95964e00a1a8 | -9.8364 | -36.1687 | 2025-01-04 01:10:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| f3082d47-eae9-360b-b58e-13a11f35ae13 | -10.6319 | -44.3257 | 2025-01-04 01:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 23cbcba8-8ada-3e7e-b940-62b30596eb00 | -9.8552 | -36.1924 | 2025-01-04 01:10:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 87.0 |
| bc230285-a7bd-3ba9-8052-e6795c2c4f51 | -10.6315 | -44.3491 | 2025-01-04 01:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 41a4016a-fa85-3b10-bbe9-03874c938300 | 1.34 | -60.3122 | 2025-01-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.6 |
| de889b99-c554-3b3d-bdb4-20afee639c68 | 1.3401 | -60.2932 | 2025-01-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 242fee16-4524-3fc8-b506-f9fb7d47f541 | 1.3583 | -60.2931 | 2025-01-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c0215c44-4c80-385c-b9ef-c9e95b83fd3a | 1.3583 | -60.3121 | 2025-01-04 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 1622de05-e339-36a7-8799-c72f9fba7b16 | -10.6124 | -44.3517 | 2025-01-04 01:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| c7b75e70-f044-36cf-b225-995472a6e3f0 | 1.3276 | -60.301998 | 2025-01-04 01:16:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c941edc7-3097-3cbd-88c5-ee9e5b8f8ec8 | 1.3356 | -60.312401 | 2025-01-04 01:16:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6f936d56-159a-3cfd-8cf9-b5620f08cb7f | 1.3337 | -60.320702 | 2025-01-04 01:16:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a3d11c72-992a-3c73-80e0-afc40cd0faee | 3.761 | -60.314201 | 2025-01-04 01:16:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ef09c1ef-9fb9-341f-b25d-a504cebf1a56 | 1.3393 | -60.295799 | 2025-01-04 01:16:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f4fc3d3c-66e5-361d-a5f0-af6a71bb9224 | 1.3258 | -60.310299 | 2025-01-04 01:16:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fe6103ea-3aaf-326d-9d33-ffc8e39f1227 | 1.3239 | -60.3186 | 2025-01-04 01:16:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d75c2c80-9bbd-3ba4-8c67-2f4e935d068f | 2.4208 | -60.6558 | 2025-01-04 01:16:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ddc90894-359d-333d-912d-b4c2e5149b56 | 1.3374 | -60.3041 | 2025-01-04 01:16:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8b233c31-c3c6-3af7-a547-f59a1ea3c5f6 | -10.6128 | -44.3284 | 2025-01-04 01:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 179.2 |
| ee4a30e4-316f-35f1-927a-fdabd8a1cddd | 1.3401 | -60.2932 | 2025-01-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.7 |
| ecac17ec-09bb-3f20-b1fe-8febd0616c25 | 1.34 | -60.3122 | 2025-01-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 5713cb87-8e43-367e-a119-7486a1c05b98 | 1.3583 | -60.3121 | 2025-01-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f4b0e24e-4d1b-33d3-8696-5f3de1a2aece | -10.6124 | -44.3517 | 2025-01-04 01:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| f1930896-2957-3d91-9eab-0e4a89a0b68f | -10.6319 | -44.3257 | 2025-01-04 01:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 5ad05dc5-d2c0-3e66-8201-736652bd02b2 | 1.3218 | -60.3123 | 2025-01-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c6f25c77-1bf1-3e6a-9dcf-524a24699d2d | 1.3583 | -60.2931 | 2025-01-04 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 94c1c637-3e12-3432-9810-9890b70fcab0 | -10.6315 | -44.3491 | 2025-01-04 01:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 284b5a06-d71e-3bc0-8089-4df9f4e983f3 | -10.6319 | -44.3257 | 2025-01-04 01:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 7432aef1-8601-3944-8500-f008e6bb4651 | 1.3583 | -60.2931 | 2025-01-04 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4f4e57c6-8151-3e76-9c46-ac79e9258632 | 1.3218 | -60.3123 | 2025-01-04 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 212aaa0a-cc79-3255-96d5-5c1d811daf4f | -10.6315 | -44.3491 | 2025-01-04 01:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e20e2a98-b211-367a-af1b-6df1e3299c93 | -10.6128 | -44.3284 | 2025-01-04 01:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| f89a53b0-4809-3615-9f96-dd49c816d4bf | 1.3401 | -60.2932 | 2025-01-04 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 90ae790e-d01c-36c9-88be-39ba463ab39f | 1.3583 | -60.3121 | 2025-01-04 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 2cca725b-61c9-37f9-ad42-b1b7a9df4a54 | 1.34 | -60.3122 | 2025-01-04 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 3f51a8da-3873-3753-bac7-44fbc289545c | -10.6124 | -44.3517 | 2025-01-04 01:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| f7634bf8-e2a0-356e-a279-7f9f327de8be | 0.58775 | -60.47073 | 2025-01-04 01:51:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9e7c1625-b2e7-3f8f-8023-9986ef6e8649 | 1.35041 | -60.30309 | 2025-01-04 01:51:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ef6c8d71-6588-3ff4-bad2-8b159947cda1 | 1.3466 | -60.31028 | 2025-01-04 01:51:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 172.7 |
| bd095395-3ecc-34e1-9cdb-c5e64eac651a | 0.59361 | -60.46452 | 2025-01-04 01:51:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5600108d-e974-3a19-a4f5-b59f02532c4a | 1.34858 | -60.29636 | 2025-01-04 01:51:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 85a83789-43f7-39f7-8b43-3e086b23ef58 | 1.33946 | -60.30156 | 2025-01-04 01:51:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 64f031c0-e1ec-3ce0-8333-b58df67a335c | 1.3376 | -60.31545 | 2025-01-04 01:51:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| bb612421-b783-384b-bb1b-238b6a1168f0 | 1.33764 | -60.29483 | 2025-01-04 01:51:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 453f82c0-5edf-3f65-b8fc-5359a71921fa | 2.42735 | -60.6527 | 2025-01-04 01:51:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 35f3f4e8-d87c-34ac-aa16-b2564f263bfd | 1.34852 | -60.31702 | 2025-01-04 01:51:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| dfdb2e38-f934-307e-aa83-5870a61aab09 | 1.33567 | -60.30873 | 2025-01-04 01:51:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 2faa458b-967a-3272-80ff-84aabd6af125 | 1.88781 | -60.48544 | 2025-01-04 01:51:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a2315e2e-05ae-3a10-b63a-1ae5d4adb42a | 1.34 | -60.3122 | 2025-01-04 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 193.3 |
| cf7a5edb-7823-3887-bbc0-da5aa036a467 | -10.6319 | -44.3257 | 2025-01-04 02:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 49992186-b3f6-3338-b46f-56227d02b3aa | 1.3401 | -60.2932 | 2025-01-04 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 0044a042-0e4a-3978-8f2b-4376091c75e1 | -10.6315 | -44.3491 | 2025-01-04 02:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 4c4bbe76-38e5-3b8f-acee-5473be5b0e9c | -10.6128 | -44.3284 | 2025-01-04 02:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 6c4d5ed1-3b45-3ad4-a649-26521da30596 | -10.6124 | -44.3517 | 2025-01-04 02:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 7e14cb57-ed00-368d-ba4a-6a262c00c929 | -10.61 | -44.34 | 2025-01-04 02:00:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0879026a-d45d-3e38-a6ed-3239bbb919d3 | 1.34 | -60.3122 | 2025-01-04 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 28a69722-a946-3803-bd6c-a64543731c45 | 1.3583 | -60.2931 | 2025-01-04 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f5123dab-0eb2-327f-aafd-994adbcb707c | -10.6124 | -44.3517 | 2025-01-04 02:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 4f600e8b-d9d1-36ef-8773-112d1107dbc0 | 1.3218 | -60.2933 | 2025-01-04 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3e695c9b-1329-3482-bb3c-159b2cf3e005 | -10.6319 | -44.3257 | 2025-01-04 02:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| dad36970-af2f-33a2-a4fc-b6d9775b7176 | -10.6128 | -44.3284 | 2025-01-04 02:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 7a1b2c45-72c3-33c0-b313-505feffc0848 | 1.3401 | -60.2932 | 2025-01-04 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 8c9f47a5-a82a-38a9-8e12-99114bfa9803 | -10.6315 | -44.3491 | 2025-01-04 02:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 36d0a2ce-854c-31a4-ad9d-012177dc250e | 1.3583 | -60.3121 | 2025-01-04 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 015ebf24-fbc7-3c62-867f-4494f1909336 | 1.3218 | -60.3123 | 2025-01-04 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 35d62d9f-4e80-314a-bcd6-842b2ae15c2c | -10.6319 | -44.3257 | 2025-01-04 02:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| dcc19c4d-a8c4-3b36-9d9c-cad769104179 | 1.34 | -60.3122 | 2025-01-04 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c1884866-3078-35dd-ab37-60608999a661 | -10.6128 | -44.3284 | 2025-01-04 02:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 33a34aa0-d7d6-3aa3-addc-6f61067b1fbb | 1.3401 | -60.2932 | 2025-01-04 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 8db468f0-24eb-3924-811e-f1f2334f89f1 | -10.6124 | -44.3517 | 2025-01-04 02:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 03f90910-fb52-346f-a1eb-fb88faaff528 | -9.84535 | -37.12872 | 2025-01-04 02:49:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ad348d5d-c25a-3e9e-8960-1c33ec3aa4e2 | -9.97729 | -36.39612 | 2025-01-04 02:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 1f6e1d0e-b96a-3cd9-8ff2-e60a5ddfbf9f | -9.84973 | -37.12904 | 2025-01-04 02:49:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 94035090-15a7-3c89-bf17-ea4f2da373ea | -9.97651 | -36.38937 | 2025-01-04 02:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 07f22ea5-66dd-31fb-8c3c-02b42df5718b | -10.01429 | -36.24773 | 2025-01-04 02:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 18d7337a-6c80-3662-bf2b-2c967b6b7f68 | -9.97853 | -36.39 | 2025-01-04 02:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| f7a5467c-823c-36ba-a8ee-461454ea94a7 | -10.02212 | -36.24326 | 2025-01-04 02:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 0a32ac36-9061-3560-b544-40d849537421 | -9.97532 | -36.39547 | 2025-01-04 02:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 3f64c664-0e4b-3270-9f30-7fe41ed097b0 | -9.48347 | -35.99454 | 2025-01-04 02:49:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d8b32d16-3875-3d5c-9f5a-24ab3591550b | -9.85233 | -37.13038 | 2025-01-04 02:49:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f194a852-5ba5-3022-b350-7494086c0c51 | -7.40473 | -35.20557 | 2025-01-04 02:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| eb5308ae-bfb7-3ecc-a8ff-967ee9483bab | -10.01548 | -36.24184 | 2025-01-04 02:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 740b48d0-76cb-3a5b-a0b7-41f414843aa9 | -10.01802 | -36.24819 | 2025-01-04 02:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 7fbe5e37-d227-3fda-93d6-ab6db09cfa27 | -9.982 | -36.39703 | 2025-01-04 02:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 9983b1ef-9303-3ae2-a8a4-a1d8af566a98 | -10.01138 | -36.24672 | 2025-01-04 02:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 363b60ff-0402-38d2-a877-dc7abc95e094 | -9.98399 | -36.39763 | 2025-01-04 02:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3f22de4b-ed86-36c6-8557-060f13cec439 | -10.01917 | -36.24225 | 2025-01-04 02:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 7ab9ce09-d132-3017-bacb-4566d76fcf62 | -9.98522 | -36.3915 | 2025-01-04 02:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4b10bc97-28a8-3bef-b011-ff9b35b6cced | -7.39985 | -35.20367 | 2025-01-04 02:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5731bfad-94a7-37de-ba56-af05aea6ab77 | -9.98321 | -36.39088 | 2025-01-04 02:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 3bae74ae-a417-3881-be8a-cd6abe9512c2 | -7.39879 | -35.2094 | 2025-01-04 02:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7b75964a-ffe2-3a8f-8695-0b12f026ae3a | -7.40636 | -35.20514 | 2025-01-04 02:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 51125bfe-1049-32b7-a7cd-3c0bea26db31 | 1.3401 | -60.2932 | 2025-01-04 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 44a28d42-bc44-396a-b2a3-cb59d76dcf78 | -10.6128 | -44.3284 | 2025-01-04 02:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 9c1ded20-a981-3299-873a-7e2edec84b52 | -10.0275 | -36.2428 | 2025-01-04 02:50:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |


[Clique aqui para ver as próximas entradas](README3.md)
