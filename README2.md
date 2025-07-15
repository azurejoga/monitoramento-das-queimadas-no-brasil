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
| 6a606c74-a704-3369-b26c-99af6488b7e2 | -10.55202 | -54.25021 | 2025-07-15 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 5b1854fb-516a-3ddb-a88d-584aebce51ac | -9.42728 | -48.39054 | 2025-07-15 00:43:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3780413b-c56a-3e6a-b655-c9ba66c2a939 | -9.94818 | -48.16905 | 2025-07-15 00:43:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fee6a6bf-d0fd-3701-ae63-8a0d26708713 | -15.08902 | -49.48988 | 2025-07-15 00:43:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 08e67741-3db6-375a-bb74-605d6abcaf58 | -11.90024 | -46.76115 | 2025-07-15 00:43:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0bf0f95b-9992-3033-9fb3-0dd3fd692497 | -11.46424 | -45.10034 | 2025-07-15 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| e4a1b858-dd5d-385e-bec0-4e2703a1dbea | -13.66038 | -45.72868 | 2025-07-15 00:43:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| bbaf8302-8e36-37a1-9e76-3657c029fead | -10.54107 | -54.2518 | 2025-07-15 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ec889a3a-3161-3144-8573-eba21145ef37 | -15.47742 | -50.05087 | 2025-07-15 00:43:00 | TERRA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 6eb63f6c-f1ea-3376-b9e1-9fdc8e7d63e5 | -10.56702 | -49.14511 | 2025-07-15 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 66e6c42e-e2cf-39aa-af23-6620028d1324 | -14.58596 | -48.11819 | 2025-07-15 00:43:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c52a153f-bce8-37bb-a689-8193cfbb128a | -11.43605 | -45.13358 | 2025-07-15 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| f66d7ed9-d2c0-3fac-b7d7-1e676e6c8fbf | -10.3704 | -47.14744 | 2025-07-15 00:43:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9745291b-7068-3d6f-ada2-84682905cd16 | -9.16043 | -44.41853 | 2025-07-15 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 71617419-5dbd-3a24-8a8a-00059319e747 | -10.28281 | -47.60886 | 2025-07-15 00:43:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9b1d1106-2e07-3e01-be56-9248dd73c060 | -13.04036 | -47.8134 | 2025-07-15 00:43:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9693f41c-3726-330d-b0b5-ca9b97cb23d3 | -9.98144 | -48.07449 | 2025-07-15 00:43:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2bdb1fa9-73e8-3d55-bea7-02db105a5cf9 | -11.57529 | -47.31842 | 2025-07-15 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 43e2a513-1bfa-355f-98d9-0bbe31544c70 | -9.80333 | -47.74311 | 2025-07-15 00:43:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 484e8b2f-472e-3cb3-811e-24a3355d4e82 | -10.89864 | -49.21621 | 2025-07-15 00:43:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ce85b6b5-c1d5-32b5-bf02-64377c2edbe8 | -12.68031 | -47.87328 | 2025-07-15 00:43:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cb0688ab-c9e5-354c-b4c3-2ee807ca2110 | -9.98284 | -48.08422 | 2025-07-15 00:43:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| e6e3a085-ebf0-3e8a-8bcc-7429d3be5f76 | -10.55383 | -54.26432 | 2025-07-15 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7a76f620-e714-396f-960a-d90185fc3478 | -10.9602 | -49.25591 | 2025-07-15 00:43:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d60be5be-61fd-39f1-8375-92bf47f2182e | -8.83917 | -46.6293 | 2025-07-15 00:43:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 40149063-244a-3bb9-aa3c-22047da5538e | -9.36892 | -48.56017 | 2025-07-15 00:43:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| aa0f7c10-1868-363a-bb6d-3fbdbaf6df49 | -11.72641 | -47.0292 | 2025-07-15 00:43:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 01410b26-416d-37cb-866d-91a878a9d2bd | -9.36757 | -48.55076 | 2025-07-15 00:43:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 1b172649-d855-362e-adcc-676ad507eb96 | -14.57704 | -48.11946 | 2025-07-15 00:43:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 55be8cd9-9425-39e5-8dee-ce2dc8482054 | -12.08138 | -43.49244 | 2025-07-15 00:43:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 158395a0-cda1-3875-aed4-4c0c02fb48fa | -11.46205 | -45.08619 | 2025-07-15 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 719f1aff-1e5a-390c-99e6-55bbce33361a | -11.46735 | -47.31575 | 2025-07-15 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d9becfb3-1513-3e0f-9f8b-bb12fa39e425 | -11.47204 | -47.30922 | 2025-07-15 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e8e4fe9b-a84e-363c-b645-2aa35c7636c2 | -12.40761 | -45.38008 | 2025-07-15 00:43:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 837a7bc2-075b-32ad-bbeb-daff3ab3a758 | -9.61914 | -49.02158 | 2025-07-15 00:43:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| c130b432-921b-350f-954c-c09ce1a0a217 | -10.881 | -54.04203 | 2025-07-15 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d1cf3bd7-e226-3d44-bc83-d3b8faf7bb5e | -12.07816 | -43.47306 | 2025-07-15 00:43:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| b3995264-8597-36b2-9c69-7c022e5c1c82 | -8.76511 | -46.60981 | 2025-07-15 00:43:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cbbb4ce3-9885-3ded-8312-5a70d22602d7 | -8.8374 | -46.61736 | 2025-07-15 00:43:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 229831cb-b297-31e6-8d03-239e5b972a5f | -14.58467 | -48.10909 | 2025-07-15 00:43:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 670a6266-f463-3f75-b8dc-ef3b576ccff4 | -9.62044 | -49.03069 | 2025-07-15 00:43:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3811f66c-3480-36f3-b6af-f8ddb25061d9 | -11.86011 | -46.75658 | 2025-07-15 00:43:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 080eecac-0173-3eb3-b191-2595936dad22 | -11.44689 | -45.13181 | 2025-07-15 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| aa7facc9-1e88-3ca0-8d52-cf9f49efc53c | -11.5278 | -48.9638 | 2025-07-15 00:43:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a514eb29-d3a3-376f-b2fa-530ce659fefa | -9.378 | -48.55885 | 2025-07-15 00:43:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6b190bd4-dc96-378a-a636-141948ced2d7 | -10.96906 | -49.2546 | 2025-07-15 00:43:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5770dc1f-5e07-3be7-a8fc-7b43b7766b6b | -10.86101 | -54.05856 | 2025-07-15 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8c604bf9-8ed1-3d9c-bee7-ccd598206fdb | -11.36511 | -48.73085 | 2025-07-15 00:43:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 89df0d1b-4c17-38b3-ba7b-d25422745672 | -10.89738 | -49.20718 | 2025-07-15 00:43:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 7fb99ee1-3a86-37ef-ab63-2677f261f2d5 | -10.87188 | -54.05718 | 2025-07-15 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| fd22a892-725f-355c-b3ee-3bf0a2944285 | -12.06913 | -47.98024 | 2025-07-15 00:43:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1f51e348-962e-3013-be2e-1441a04804f8 | -9.81417 | -47.75181 | 2025-07-15 00:43:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8a0e5d11-1d65-3757-aeef-8568dc7af6ee | -11.4534 | -45.10222 | 2025-07-15 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 209.6 |
| e574ef21-c1bf-3c0a-a3d7-827b3a186e0a | -10.57464 | -49.13477 | 2025-07-15 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 58cb6a1c-8c1b-3983-a46b-308acadb3544 | -9.62185 | -49.10486 | 2025-07-15 00:43:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 98155c0d-2665-3269-97a2-58cef9ffdbc9 | -5.53574 | -43.87471 | 2025-07-15 00:45:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 67fd24ce-5828-30a9-b1fc-4883ab65f5ac | -7.43393 | -48.09797 | 2025-07-15 00:45:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ada6e534-6a99-3693-9b8c-7683c47ec047 | -7.29902 | -46.25427 | 2025-07-15 00:45:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 22311bfc-c6e9-393d-84cf-2edcd33dc87a | -6.37637 | -43.72921 | 2025-07-15 00:45:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 0ac0bdd8-7b99-3882-90b3-3835dd521850 | -7.20516 | -45.33251 | 2025-07-15 00:45:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 68137f82-ab57-3832-8391-652d9b05a222 | -6.38638 | -43.70553 | 2025-07-15 00:45:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 40143029-eff9-3d39-92d4-451323d66e5e | -6.70744 | -47.79938 | 2025-07-15 00:45:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 89300bc4-b154-339e-a430-e9f7a0c5dd3e | -5.78448 | -45.11369 | 2025-07-15 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| b04eba85-3bcb-3eba-8efc-2dbe64d5fcec | -7.5893 | -44.72747 | 2025-07-15 00:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 731e3ebf-5a81-3a86-a8e2-cc23461e50fa | -8.6539 | -47.74602 | 2025-07-15 00:45:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 30f5eb69-dcde-340e-9b9e-e5cb13cfb2f9 | -5.78923 | -45.10736 | 2025-07-15 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 641f437b-3d87-323b-8760-3286b65f9354 | -7.88492 | -44.49678 | 2025-07-15 00:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8f822df8-26d4-3c5b-847a-f8badb2052d8 | -7.81668 | -46.56585 | 2025-07-15 00:45:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9999e9fa-eb37-3b24-8980-e0667e95d151 | -5.33569 | -43.75991 | 2025-07-15 00:45:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 42885bd4-2f48-34a1-aded-8ae0e975d3b5 | -8.64441 | -47.74744 | 2025-07-15 00:45:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a0dcaeae-92c4-31c3-a4f6-b26af82fbf84 | -7.20822 | -45.33848 | 2025-07-15 00:45:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 42837b71-670a-37c4-8e90-62877355f3ad | -7.43247 | -48.0877 | 2025-07-15 00:45:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6589ef04-9b8c-3737-a624-ae020b4613d0 | -5.53091 | -43.86884 | 2025-07-15 00:45:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 364fd601-2426-3e90-a496-fd735104b674 | -7.19916 | -43.1188 | 2025-07-15 00:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| bbe3a68f-dd8b-3e71-85c5-614ed30fb147 | -7.82476 | -49.82561 | 2025-07-15 00:45:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b6053557-9b68-319e-bbfb-1acdb926dcef | -5.78197 | -45.09665 | 2025-07-15 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 1f57fdfa-b9c5-31b6-83ee-3ef17bc49b29 | -5.53429 | -43.89056 | 2025-07-15 00:45:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 220.4 |
| 870f0899-291b-3486-a2d0-b6035c0afd13 | -4.7818 | -45.33399 | 2025-07-15 00:45:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 1510f07f-d712-3f75-95fa-bf96f2bfb262 | -8.38439 | -51.07723 | 2025-07-15 00:45:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| c7df4e57-d5e5-38ce-9895-5f84cbf78ef3 | -7.30419 | -45.36507 | 2025-07-15 00:45:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d369f750-7460-3637-9a92-ebf1fae04811 | -5.37025 | -43.92843 | 2025-07-15 00:45:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 4d1093f3-80dd-3254-aa4a-2bd5bdf06cd7 | -6.12214 | -42.9603 | 2025-07-15 00:45:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| b46d6974-7367-3728-a7d8-cbc92fcb55ab | -5.47806 | -44.29159 | 2025-07-15 00:45:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c583b5be-b011-37e9-a235-dafadea8c079 | -5.32953 | -43.7543 | 2025-07-15 00:45:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| ed3a935e-01b9-3172-b536-a8224d673340 | -7.08884 | -49.17813 | 2025-07-15 00:45:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 14.2 |
| fef01140-5539-3048-ab8f-c217eed48fa8 | -6.63573 | -44.57549 | 2025-07-15 00:45:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0ceba881-bf0f-364b-8ae0-6ee051fc1a41 | -8.64591 | -47.75777 | 2025-07-15 00:45:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 903ee162-bf92-37e4-bddc-bcdd60ff7cd6 | -4.78429 | -45.35082 | 2025-07-15 00:45:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| a1a69cf3-7f8d-3969-9af4-26db2badd2bc | -4.68749 | -43.25864 | 2025-07-15 00:45:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 162cc7ae-3fca-3fc9-bd1a-3080588d9380 | -5.53892 | -43.8963 | 2025-07-15 00:45:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 33487222-4914-3a6c-9cf0-4f0a6b322b47 | -6.63266 | -45.72224 | 2025-07-15 00:45:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f6a28d18-b192-3b25-a76f-7dabbd2be272 | -7.08753 | -49.16886 | 2025-07-15 00:45:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f63c53a6-8ac5-371d-918a-2b24d5c16bf6 | -7.8971 | -44.49498 | 2025-07-15 00:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4ae66a72-50e7-337c-b308-8a40b597d50e | -7.30145 | -45.3598 | 2025-07-15 00:45:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e2f797dc-76cd-3f2c-93b7-79b49eb1358e | -5.53766 | -43.91221 | 2025-07-15 00:45:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| e0cf6b7c-1d25-3b95-b0cb-931250df188f | -7.301 | -46.26751 | 2025-07-15 00:45:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e1caf3bb-3652-37da-81df-5f1819aab2a5 | -6.91284 | -52.86037 | 2025-07-15 00:45:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| c5a845ee-8fe8-3dde-ad28-14542bba153b | -6.17493 | -44.38284 | 2025-07-15 00:45:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0cd474f2-41a6-3e2c-9073-d6f3ece094d7 | -6.70899 | -47.81014 | 2025-07-15 00:45:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 3bdbd09c-e3d5-364a-a5d5-2619b57cda73 | -7.09788 | -49.17682 | 2025-07-15 00:45:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 49.2 |


[Clique aqui para ver as próximas entradas](README3.md)
