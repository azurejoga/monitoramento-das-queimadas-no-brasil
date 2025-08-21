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
| a9776e9f-abaf-30e6-98dd-88a2dec2fff8 | -8.6157 | -62.1374 | 2025-08-21 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| eceb9c84-a57b-36c4-948c-6dd06ae4ba2e | -5.9526 | -44.1326 | 2025-08-21 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 30814f1e-91c9-341c-8596-89f3ab87b2b6 | -12.5932 | -60.3522 | 2025-08-21 00:46:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e9a9851b-4206-3aaa-b673-62f89aff1f87 | -5.8878 | -57.750401 | 2025-08-21 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63b004a2-5d30-32ec-a13e-6503d1ffef71 | -7.2856 | -49.3988 | 2025-08-21 00:46:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e365bd0-4780-371b-ad7f-c7ff0bd31ba4 | -12.9701 | -45.191601 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a4dc407a-6c63-3ff1-8db8-ed38e726960d | -14.3763 | -51.9758 | 2025-08-21 00:46:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d3a586ef-b37a-3b69-bf83-d9a680d8d02c | -6.8052 | -50.0923 | 2025-08-21 00:46:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273f523b-8ece-39a5-ad53-16bebae411ff | -13.329 | -54.4156 | 2025-08-21 00:46:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bbdca9f-6bed-36dc-8da8-411dacd58aaa | -14.626 | -54.869099 | 2025-08-21 00:46:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3600fe-f7f4-3ce7-8115-b6bfb3728e43 | -14.8536 | -47.930801 | 2025-08-21 00:46:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 21ac9efd-fec5-363d-804c-4a7194b75c5f | -8.3676 | -54.994598 | 2025-08-21 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbc9deb-89cb-3e47-a12d-be42a4d93e08 | -7.8586 | -46.734798 | 2025-08-21 00:46:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 879cd3e6-18a6-3c21-8676-cb3306d6edc1 | -8.8931 | -62.394402 | 2025-08-21 00:46:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de4da535-1f8a-3db8-8bf3-2261be243750 | -13.3339 | -54.391701 | 2025-08-21 00:46:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 983c0bef-0172-35e0-9489-618a625bc7df | -8.6838 | -62.076302 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e981b69-812f-3f19-8c35-5b9d86facfdf | -13.3306 | -54.422699 | 2025-08-21 00:46:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28cf9053-c9c3-3b72-8237-cb23be44febe | -8.8401 | -52.055199 | 2025-08-21 00:46:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df2d892-5b8f-3d12-8caa-e20fbfd49277 | -2.7662 | -54.4286 | 2025-08-21 00:46:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44fc1e4b-87da-3212-b31b-9b26d2095eb8 | -13.0308 | -45.148701 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6724357-c1aa-31f3-9736-b9a61408252e | -13.0341 | -45.199299 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54cfe29a-b642-3d8c-a99d-464a59f58845 | -16.052099 | -49.070999 | 2025-08-21 00:46:00 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ce09ca07-02d8-392a-a033-6f8be23ee244 | -8.674 | -62.0783 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 247f2b0d-d48a-3f45-81c3-ded31fa44ec8 | -11.8133 | -55.511799 | 2025-08-21 00:46:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 795979cd-b199-3c22-83be-2bcd819ff15a | -15.0189 | -54.829601 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39cdd173-e3bb-38c3-a8ac-e384b7b38c9f | -7.0215 | -44.612301 | 2025-08-21 00:46:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bd0a426-dedc-3f61-b900-c4f818580e80 | -14.7541 | -56.014599 | 2025-08-21 00:46:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 72058af7-666a-3e32-88ea-b3b0d43a9933 | -11.5657 | -46.995201 | 2025-08-21 00:46:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6996242-f38f-3bd8-8f2f-32d354a420be | -7.0024 | -44.617199 | 2025-08-21 00:46:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5ffd988-d770-34b9-92f4-06953419b37d | -11.4301 | -47.311199 | 2025-08-21 00:46:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86fec403-e05d-3112-a403-68f9afec1be4 | -15.022 | -54.8437 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea95c640-1d51-3806-851e-c1dd87584ba9 | -8.8808 | -62.384602 | 2025-08-21 00:46:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e498dcf4-b314-3bcb-a65c-00a6be418e06 | -13.0181 | -45.178101 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5209d4bc-eca1-3f4b-970c-3033506c01fa | -8.8833 | -62.3965 | 2025-08-21 00:46:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91716a2e-bb8d-3d6a-b770-fad7f6a90af4 | -11.5706 | -47.014301 | 2025-08-21 00:46:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d879504-0eae-30ec-b283-23304c8ca722 | -8.8761 | -62.4104 | 2025-08-21 00:46:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab7ea177-8433-30d7-9439-2ebda97a3020 | -8.8476 | -52.042999 | 2025-08-21 00:46:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8593d8d0-cfec-35b4-aa90-192668ff5f39 | -13.5372 | -47.0341 | 2025-08-21 00:46:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f776c7f-f6a4-3e02-808c-cf65c260d482 | -11.5753 | -46.992599 | 2025-08-21 00:46:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fefe43f9-6933-3e47-9f49-52ffed2ac6e4 | -13.0117 | -45.154099 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aad6db83-d94e-3327-9e2e-56e7b0ee5961 | -6.9409 | -62.8643 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 552fda98-fb1e-3524-9e1b-ba662c63c5f5 | -8.8858 | -62.408401 | 2025-08-21 00:46:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 70874b9a-f188-3674-8a28-9045c897f206 | -15.8893 | -48.999298 | 2025-08-21 00:46:00 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c1628d3f-d298-3ba6-b61a-23694b5152ad | -11.8149 | -55.518799 | 2025-08-21 00:46:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| decc6b02-bd47-3dc3-a041-1c04552e30cf | -2.9115 | -48.302101 | 2025-08-21 00:46:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee2af91a-e7fd-33c0-850e-44565d2067a0 | -8.3659 | -54.987301 | 2025-08-21 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cdee9d8-ed2b-3ceb-a1bd-7d7439b92b59 | -8.6787 | -62.1008 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fef3d948-818f-3979-97d8-b9843420eaab | -13.3355 | -54.398899 | 2025-08-21 00:46:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87649e32-c32a-3caa-8002-05f1a59c2f38 | -8.8906 | -62.382599 | 2025-08-21 00:46:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a676d5ac-dd99-3071-840e-e54078d050c5 | -13.4399 | -57.160999 | 2025-08-21 00:46:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c73f02f-046a-32b2-8edc-184554f10666 | -8.6936 | -62.0742 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da2b922e-8167-319a-a61b-ae13733fbbef | -10.9874 | -55.229099 | 2025-08-21 00:46:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 448b1bd1-5ad1-3d9d-aa21-32ac98cdc71f | -13.0277 | -45.1754 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c7a3a73-4f0e-3c89-aa27-000d9692aba7 | -12.9483 | -46.240601 | 2025-08-21 00:46:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9cf49d1a-45b2-3698-a8c2-3bbeed343921 | -8.8686 | -62.374802 | 2025-08-21 00:46:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7ad2474-0908-3b70-bc67-599c7d8461e0 | -13.0213 | -45.151402 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eed50c69-8c3e-3637-ba10-a5db474f42dd | -14.6244 | -54.862099 | 2025-08-21 00:46:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83396504-fd52-3c46-8e6a-e983eefefc34 | -14.6342 | -54.859798 | 2025-08-21 00:46:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc9e3705-3fa1-3d05-b04a-cde1949033d5 | -12.9387 | -46.243301 | 2025-08-21 00:46:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2ecbe78-36ae-31db-87f8-bbb9c2126f93 | -11.7478 | -58.316898 | 2025-08-21 00:46:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab9359e-7027-3c95-8041-e05629d7ccaa | -11.3235 | -55.211201 | 2025-08-21 00:46:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b88d9805-c853-3ed5-97e7-d3d450f56f72 | -14.4821 | -45.944599 | 2025-08-21 00:46:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e194e53e-d905-37c6-8f4c-983c915c56db | -5.137 | -56.9744 | 2025-08-21 00:46:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6abbc0-a67f-3c12-b8e0-fb16fa60d20e | -13.0245 | -45.202 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47ac7ec7-970f-308d-9cc6-477cbafa4e61 | -8.8304 | -52.057598 | 2025-08-21 00:46:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c8edbab-a7a4-3097-a6b3-9639b86de691 | -11.3251 | -55.218201 | 2025-08-21 00:46:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 948df54e-ad4a-3ab5-8550-5a5c1e62550c | -13.0373 | -45.172699 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3a1b38b-e3ae-3c55-af05-c6976ce7f0ed | -14.7557 | -56.021801 | 2025-08-21 00:46:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d569cc50-3f49-3c93-85df-821e7422009c | -12.9874 | -56.872101 | 2025-08-21 00:46:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbd647b4-b117-3f0d-a639-3cf79d3b5a68 | -12.0283 | -57.093601 | 2025-08-21 00:46:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03ae37e2-c834-35ab-ad03-993069a735fa | -6.4581 | -53.373901 | 2025-08-21 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c3ceb13-b61e-34d2-95b4-4bf0d1f9c3b7 | -6.4484 | -53.376202 | 2025-08-21 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1e86c8f-0aa7-39d5-b19b-aba599854f0c | -15.8826 | -49.014 | 2025-08-21 00:46:00 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 66e5eed1-6a64-3b81-9638-0614f4ddb369 | -6.3508 | -55.553001 | 2025-08-21 00:46:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1e3aa30-6aff-373b-9776-c15ece2c1398 | -15.0122 | -54.846001 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8135232f-e083-304b-9fcc-5b7d6e62b380 | -8.6396 | -62.109001 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73325831-8ee4-3f23-bc38-b91ec843e093 | -5.1355 | -56.967499 | 2025-08-21 00:46:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf8f3fa9-77b5-3de8-bc94-f7c2b0f7c6ad | -13.0085 | -45.180801 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b867d93c-5431-3d4a-8215-c40ef33c6a19 | -7.0033 | -44.5816 | 2025-08-21 00:46:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68fc7217-db6a-322e-9abf-020c2b4a88eb | -14.8573 | -47.945499 | 2025-08-21 00:46:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9511d9ad-c91b-3bbc-ad01-6bcf93f572c9 | -10.989 | -55.236198 | 2025-08-21 00:46:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad7dcba9-400d-3698-bdce-0b0ead5f2e7b | -15.8796 | -49.0019 | 2025-08-21 00:46:00 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f4a6a0dc-ba22-316d-a2d2-ad67b6e0368c | -10.7194 | -48.250702 | 2025-08-21 00:46:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd2ee3a6-5bfb-3851-a943-370d719d696d | -15.0106 | -54.839001 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e7d08fa-8cde-3fcd-ad24-245dcfe3e141 | -7.2759 | -49.401199 | 2025-08-21 00:46:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf4b032-0972-3fff-8af0-a566f1fc3a26 | -4.3002 | -48.084599 | 2025-08-21 00:46:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac2229cd-d6ae-352b-a47c-ae57cb03e31e | -11.4986 | -50.528801 | 2025-08-21 00:46:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f8071ee-1829-36c5-90d8-ad5379ec6e96 | -14.8439 | -47.933399 | 2025-08-21 00:46:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ffe0679-b7b9-313f-8de8-e00aa78eaced | -6.4505 | -53.385101 | 2025-08-21 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61e12966-15ff-3e0d-ad7e-2828b918b68d | -12.2249 | -53.599899 | 2025-08-21 00:46:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0991169d-1c0f-350a-8dd2-4db088e21e95 | -8.6763 | -62.0895 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19fb1bea-d99d-3f26-a640-260989d3ac0d | -14.8402 | -47.9188 | 2025-08-21 00:46:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 32ff1699-0442-3731-aa83-4c6f4468aed6 | -15.0024 | -54.848301 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 986ff15c-c140-35b2-a802-d11cabf0c1bb | -11.7462 | -58.3092 | 2025-08-21 00:46:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3841a54d-d4a2-3c2d-a131-547bae8de54f | -8.8736 | -62.398499 | 2025-08-21 00:46:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c6eaa574-e0bf-3256-b78a-99021514acde | -11.4348 | -47.329399 | 2025-08-21 00:46:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a658209-31b7-3d8e-9d30-f28487d1518d | -9.9172 | -49.295601 | 2025-08-21 00:46:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e488c524-382e-3f1a-8587-7c4d48d39fd8 | -8.8711 | -62.3867 | 2025-08-21 00:46:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e30d29e-72b3-360d-bc01-12ccc58651ee | -8.3757 | -54.985001 | 2025-08-21 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007bc4b9-82f9-3caf-a622-face19592834 | -13.3257 | -54.401199 | 2025-08-21 00:46:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
