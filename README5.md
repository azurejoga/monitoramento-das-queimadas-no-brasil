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
| b950d852-2c51-33f7-b680-32dbe73907be | -9.6069 | -56.923901 | 2026-07-01 01:37:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| befb7740-80f2-3230-8069-d8c2c3290b1a | -11.6385 | -59.006401 | 2026-07-01 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c8424dd-a6b9-300d-8a7c-408286606eb0 | -10.6774 | -54.5121 | 2026-07-01 01:37:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a86be07e-b8b7-3899-be48-6e066aec7b99 | -10.6814 | -54.528099 | 2026-07-01 01:37:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f5c88d4-3719-32b6-9d95-7bac0621f8ff | -11.4195 | -56.064999 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee60e72-4e2d-3d63-8021-834d8cc096c0 | -9.0266 | -59.534302 | 2026-07-01 01:37:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc6b1547-7638-3416-b95a-cb3e5990e5bc | -9.6194 | -56.933102 | 2026-07-01 01:37:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2712dc02-30ef-3288-8956-daf03366c2f0 | -9.7019 | -56.094601 | 2026-07-01 01:37:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33634a01-65ca-3413-875c-526b826bba6c | -11.0529 | -56.923401 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 412a9610-4833-335e-9cfc-8586f6f8d822 | -10.6758 | -54.546501 | 2026-07-01 01:37:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be1277f0-a6c6-3693-bff5-7a0628c1714d | -12.4143 | -58.402802 | 2026-07-01 01:37:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c6f455d-1502-3a35-8710-f90fa73028be | -12.4199 | -58.3829 | 2026-07-01 01:37:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b46cc12d-b896-3653-92fd-89d8cef0b8b1 | -9.6922 | -56.097 | 2026-07-01 01:37:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a65fea3-1415-3a3e-9a0e-7529540e14d0 | -10.13 | -52.0802 | 2026-07-01 01:37:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f278dde-6d04-35eb-9dc3-65788d9efc17 | -10.6952 | -54.5415 | 2026-07-01 01:37:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ccd2e67-4b43-3085-82a0-b233adb359b6 | -11.6425 | -59.022999 | 2026-07-01 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e52dd2a8-3747-3257-94dc-f85faf124199 | -9.183 | -58.0695 | 2026-07-01 01:37:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06190be9-3ec2-3d6c-9927-69c5b9bc82d2 | -12.8035 | -54.867599 | 2026-07-01 01:37:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05989779-75fb-3b22-9df4-50bab96e30a1 | -11.439 | -56.060001 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d8a9c0e-4c84-3821-95d3-8219e4e4fd00 | -9.0891 | -59.493099 | 2026-07-01 01:37:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59005b5e-6d36-326c-881b-2f8e0999e229 | -11.442 | -56.0723 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45c174e0-cf0c-3f42-8e6a-ead79aab659a | -10.1362 | -52.104099 | 2026-07-01 01:37:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a8593c0-0772-3197-a118-c0a352a332e7 | -11.0502 | -56.912399 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fde131c2-91b6-3686-ac51-6e1c316f26ba | -11.8436 | -56.944199 | 2026-07-01 01:37:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66b37f5f-c022-3f30-926f-3e591408c156 | -11.9086 | -57.379101 | 2026-07-01 01:37:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0c9051-7316-3f55-803e-2fad05f84fa1 | -11.4359 | -56.047699 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0e1435e-1270-3237-8423-f035dd096780 | -16.371401 | -56.671001 | 2026-07-01 01:37:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 572ce8a4-e660-3442-a8db-b9069a88ba27 | -9.6097 | -56.935501 | 2026-07-01 01:37:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f595dc5-f3e4-3759-90de-bb5da6a8126e | -11.4323 | -56.074799 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 156f5ef2-4c63-3831-a3b6-3b70a552698d | -16.359301 | -56.663799 | 2026-07-01 01:37:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 30792d37-be3a-3c35-b180-ab257b7aebaa | -12.2241 | -56.558102 | 2026-07-01 01:37:00 | METOP-C | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80265d52-5c96-3ff4-ac24-9a798f2b9bb9 | -25.289301 | -53.869202 | 2026-07-01 01:37:00 | METOP-C | CÉU AZUL | PARANÁ | Brasil | 4105300 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 301ad916-06ee-36e7-aa98-efaf38f7ab7e | -9.0286 | -59.542599 | 2026-07-01 01:37:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77100a0d-ea2c-3584-9717-e2c841f0c630 | -16.3666 | -56.651501 | 2026-07-01 01:37:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 256d4d8a-c051-33bc-8a41-3e1d17687a98 | -11.6287 | -59.008801 | 2026-07-01 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c3542c15-7105-3b0d-bb67-2b09160e3b35 | -10.6717 | -54.530602 | 2026-07-01 01:37:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32d4c82d-84f6-346d-8014-fa7b18af8ea3 | -10.6855 | -54.543999 | 2026-07-01 01:37:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12623979-5867-318d-9055-6b83afa9f4e9 | -12.2269 | -56.569199 | 2026-07-01 01:37:00 | METOP-C | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b85d8a8b-1b74-3d32-bf8b-7d9d78433c17 | -9.6166 | -56.921501 | 2026-07-01 01:37:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2c8e00d-267e-3f1b-a0f9-e79b49e321b0 | -9.6041 | -56.912399 | 2026-07-01 01:37:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2c9b966-46e6-3ec3-b129-f3f4b8574a1d | -11.6307 | -59.017101 | 2026-07-01 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00c54793-2ac0-3283-8d19-6b939a5f2d0f | -9.1807 | -58.059601 | 2026-07-01 01:37:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91b4a0cc-d582-3cf2-9dc7-923aca69e32c | -12.2214 | -56.546902 | 2026-07-01 01:37:00 | METOP-C | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce5b0929-a52d-3217-beae-b85d9a902dd8 | -12.4317 | -58.389301 | 2026-07-01 01:37:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c37a28a7-e9ab-34c3-ae07-a57a34b4dc8f | -11.4293 | -56.0625 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4ea8f6e-b7fe-3bea-aa10-2cd1b0c96af3 | -12.422 | -58.391701 | 2026-07-01 01:37:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0de6672d-92e9-392c-9c21-0224f7f43c21 | -21.0986 | -57.4702 | 2026-07-01 01:37:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4b59bf7a-9692-3924-ad1c-2e5d63bb618c | -11.8462 | -56.954899 | 2026-07-01 01:37:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77c46a50-f489-3f84-9d0e-1ce3b9f43cff | -10.0785 | -60.497398 | 2026-07-01 01:37:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2581aba-aee5-31dc-a2a6-ce912c60b14e | -12.4241 | -58.400398 | 2026-07-01 01:37:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6dcb33e0-e6b0-399e-ac43-e7f07f7e3632 | -12.4122 | -58.3941 | 2026-07-01 01:37:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9692344a-c146-3e73-8afd-e57d8ce8e185 | -11.4262 | -56.050201 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d0333ec-bda7-3052-9c87-18746e5e2e4d | -11.4437 | -55.913101 | 2026-07-01 01:37:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 131f93e8-01d8-3326-8a24-1a7ab4518818 | -16.368999 | -56.661201 | 2026-07-01 01:37:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0c6ca59-6065-3280-8bd9-55d291907f9e | -12.7999 | -54.8535 | 2026-07-01 01:37:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07490aff-2569-3253-b680-744bbfc8ee8c | -10.6911 | -54.5256 | 2026-07-01 01:37:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4f6f42d-b655-339f-9902-9bc18d62e1f5 | -16.356899 | -56.654099 | 2026-07-01 01:37:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c8a74b3-3a79-31a2-9cb4-3af8012e7b8f | -21.096701 | -57.462101 | 2026-07-01 01:37:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 304e9e69-8449-3ee5-aabe-2c596bbaf7e8 | -11.8533 | -56.941799 | 2026-07-01 01:37:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee16c48-6c79-35f1-b573-0120c6ec0165 | -11.6327 | -59.025398 | 2026-07-01 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2dad850d-f993-32cd-b173-9c81bc59d52d | -11.6405 | -59.014702 | 2026-07-01 01:37:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0412e872-d358-334a-958f-99f44de1c675 | -11.9111 | -57.389198 | 2026-07-01 01:37:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea85c36f-1219-3ba0-b6c4-00fdae22bdff | -10.6596 | -54.5372 | 2026-07-01 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 9b975779-1b26-33c8-a36a-b496093a157f | -12.7746 | -44.5162 | 2026-07-01 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| b7c23fd4-afa0-3fc9-b84b-1f9c264876d4 | -12.7562 | -44.4724 | 2026-07-01 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 64e7f18d-6fb8-346d-9911-28d2f3b8c120 | -10.6787 | -54.5153 | 2026-07-01 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 1105fb34-6b53-3e48-91da-4024f3b2ad5e | -12.4096 | -58.3865 | 2026-07-01 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0904b7b9-48eb-386f-99c4-8e0a8fe378d8 | -16.368 | -56.6514 | 2026-07-01 01:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 2ae192d4-3e1a-38b1-af9d-537af6606da1 | -12.7553 | -44.5194 | 2026-07-01 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 7ba27d53-b4f1-352c-bcdd-55755a5e17de | -11.5337 | -47.4571 | 2026-07-01 01:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f87624ba-2851-3c7e-aa48-9a35448eff3d | -12.7755 | -44.4693 | 2026-07-01 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 491.6 |
| 89cb65e9-6a80-35f6-8a72-80f5f57fb3b7 | -11.5528 | -47.4546 | 2026-07-01 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| b952fc1c-60f5-341d-a789-1014150cc2d5 | -11.4336 | -56.0711 | 2026-07-01 01:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 643.1 |
| 96049d05-4262-3262-8594-d1a2868fb7e1 | -11.4149 | -56.0525 | 2026-07-01 01:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 08a51b0b-0939-3731-96d1-b1a8efcdb8db | -12.7751 | -44.4927 | 2026-07-01 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1121.6 |
| 7963d876-5c06-3bdc-a935-b6afd326c3be | -11.4338 | -56.0509 | 2026-07-01 01:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 433.3 |
| 44f8d464-cb44-3b44-b76a-f87b2b7683c2 | -10.6784 | -54.5356 | 2026-07-01 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 2deca08e-b0ca-3f76-b9ef-9830020bc47f | -9.6037 | -56.9276 | 2026-07-01 01:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ab9f3ed0-c50f-3139-9539-f5e8befec34b | -12.4285 | -58.385 | 2026-07-01 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 5c865714-8ce0-30cc-9433-dabc73f6580d | -12.7557 | -44.4959 | 2026-07-01 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 443.4 |
| dbd62122-e4d1-37c8-8255-1024a74d4007 | -10.9205 | -43.0622 | 2026-07-01 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 05456b1a-89cf-30a2-ab0b-c2a975947a8c | -11.4147 | -56.0726 | 2026-07-01 01:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 215.1 |
| 91716a17-c765-39b2-b14a-32be250ad74f | -11.6286 | -59.0169 | 2026-07-01 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 0b0730db-be30-3f5d-8e79-19d5887d5391 | -10.1237 | -52.0905 | 2026-07-01 01:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0b7b6fa1-9751-3d2a-84bf-e2ae331d038e | -10.6596 | -54.5372 | 2026-07-01 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b136fd39-493b-35ff-8316-dc8f49c6f19d | -11.5337 | -47.4571 | 2026-07-01 01:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f6301764-3250-39bf-99ec-f13768e63569 | -11.5528 | -47.4546 | 2026-07-01 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a735c579-c3c9-3846-8f13-c1c37c12f7f9 | -11.4147 | -56.0726 | 2026-07-01 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 227.6 |
| a9390415-19ba-3b5b-bf15-ca7dc3a14754 | -12.4285 | -58.385 | 2026-07-01 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| f3b1f3e3-25c9-36b7-bad5-53e13721e0da | -11.6286 | -59.0169 | 2026-07-01 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| a4b7f6b5-3073-36d8-aa66-2a9052b4b436 | -10.1237 | -52.0905 | 2026-07-01 01:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f2981961-02f4-38ee-8403-504b8ba3b8ff | -12.4096 | -58.3865 | 2026-07-01 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| b01d9141-bfdf-3b78-bd83-876afd081621 | -10.6784 | -54.5356 | 2026-07-01 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 527e7f97-4a63-3a36-9fde-5d1dafb8817a | -11.4527 | -56.0493 | 2026-07-01 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 59766f0f-5b22-329d-8ae1-6568263b50af | -11.4525 | -56.0695 | 2026-07-01 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1bc79771-748b-3e3e-b447-282d907b7411 | -11.4336 | -56.0711 | 2026-07-01 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 436.9 |
| f9a0221b-9b71-31c4-9e2c-bc9e7449afa5 | -11.4149 | -56.0525 | 2026-07-01 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 3954019b-8373-3418-a981-eada2d3c3439 | -11.4338 | -56.0509 | 2026-07-01 01:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 392.1 |
| 8f59e490-8329-36b1-ad62-b6851f7865ab | -10.6787 | -54.5153 | 2026-07-01 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 7e02b415-f729-3eb8-b514-44532934bd51 | -11.6286 | -59.0169 | 2026-07-01 02:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |


[Clique aqui para ver as próximas entradas](README6.md)
