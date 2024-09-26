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
| 5e375f89-b188-32d7-a291-e5dc6e5dc71d | -13.2786 | -51.320301 | 2024-09-26 00:55:10 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f355c2ec-25d0-3738-a871-8a5ae93abd9f | -13.199 | -51.241501 | 2024-09-26 00:55:11 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b48cb17-44b9-397c-9d00-875119a03a44 | -13.2006 | -51.248699 | 2024-09-26 00:55:11 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98d140d1-de4b-3b1e-8e19-0c62bca2d170 | -13.2022 | -51.255798 | 2024-09-26 00:55:11 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f640b720-5159-3f53-b7a2-0492fc7c8c89 | -1.0369 | -53.3555 | 2024-09-26 00:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a329d5bb-9756-38e3-96f3-091d7ab07978 | -1.0553 | -53.3553 | 2024-09-26 00:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5d82e152-f6a2-3f27-8ebd-10a2c1990f44 | -11.9484 | -47.273998 | 2024-09-26 00:55:16 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ae73df7-d500-3bd4-9721-3ba003cdaac7 | -11.6771 | -46.3339 | 2024-09-26 00:55:17 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af94cf3d-e450-3225-95fa-4043012e59d2 | -11.6643 | -46.323799 | 2024-09-26 00:55:17 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7935062a-c042-3979-a39c-399dcd0a8d95 | -11.6673 | -46.3363 | 2024-09-26 00:55:17 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c02ede32-684c-3f04-a6ac-cf48d95519fa | -12.8417 | -51.3027 | 2024-09-26 00:55:17 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6877d738-b574-355a-ae23-396cd088aa1e | -12.8092 | -51.250198 | 2024-09-26 00:55:17 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3eb6ba94-d9fd-331a-ae22-ea80b5c5d065 | -12.7945 | -51.231098 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a1b48fa-8f0c-350f-96f6-ab63e4a601ba | -12.7962 | -51.238201 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da2eb8fb-f214-315b-9fa6-fab7352b4959 | -12.7978 | -51.245399 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c2d9a2bc-ded9-3cf9-a47f-ed59e10bfa56 | -12.7994 | -51.252499 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd744fb-8106-3763-8f73-8774c55633ca | -12.801 | -51.259602 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd08c94f-c6b2-3fe8-a124-1473c65a1059 | -12.8042 | -51.273899 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55263613-26ba-3f81-9fc3-1a148cdba352 | -12.8058 | -51.280998 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 15ddfda4-b4fa-3270-9865-64acb3be3c99 | -12.8075 | -51.2882 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0210b815-60a9-3993-86ff-ffe5b7a3a586 | -12.7831 | -51.2262 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b64ba71-e9f5-3aaf-8a14-88233a98fe60 | -12.7847 | -51.233398 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb20eb3b-78fd-3ee6-b33b-060d15cb9d5a | -12.7864 | -51.240501 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a0dcf04-a3aa-38d6-812a-9b7933817bf5 | -12.7912 | -51.261902 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| caf10f9a-cd20-3394-89c2-775011baa879 | -12.7944 | -51.276199 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d92eb2e-28b5-3bbf-ad9f-8ea427e798a2 | -12.796 | -51.283298 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a83f122-f82a-3740-b75d-7026a6474470 | -12.7977 | -51.290501 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64d7be0c-3e5d-3200-bd7f-425074489c59 | -12.7993 | -51.2976 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f81ffd4-fd33-3a0b-aee2-e0f787bafe32 | -12.8009 | -51.304699 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 996d2ea4-7fa8-3e5f-a59b-02c422aa6830 | -12.7846 | -51.2785 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59869157-4c8f-3514-86d1-ede0d670e050 | -12.7862 | -51.285599 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec044cd8-6cc4-32ec-beb2-e1e0f0070a23 | -12.7879 | -51.292801 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d79b4d30-7d18-3bae-9039-318a85a17d1f | -12.7895 | -51.2999 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed042280-37fe-32f6-9bd5-e9896c84a015 | -12.7911 | -51.306999 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c28c770-3733-3421-8349-2b4aa21c4388 | -12.7991 | -51.342602 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d60b46da-0a21-32d0-a865-b0d149283810 | -12.8007 | -51.349701 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 75d846f0-b4c4-3671-819d-6c0261e39684 | -12.7797 | -51.3022 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a10ed80a-9310-332f-9c8b-a7a70cf1ab4b | -12.7813 | -51.309299 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 759a23f4-7272-372e-8d89-9897e831bbd3 | -12.7829 | -51.316399 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 629d9f0c-9079-318d-9660-80a0bdbe4bdd | -12.7909 | -51.352001 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 76bbb239-c16a-3620-b2f6-0f372bab4c1a | -12.7925 | -51.3591 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7760f8ae-6951-37f8-9a59-79d58a71f69b | -12.7683 | -51.297401 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ebb8e83d-e42b-3805-9d53-9dd86a5b8673 | -12.7699 | -51.304501 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0048787d-7dab-309a-b96a-a7789611a5b4 | -12.7715 | -51.3116 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e7fd9d9-eb38-31bc-adb4-941dece80586 | -12.7731 | -51.318699 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69dc6033-a55a-3e53-b1da-20d1bbedd014 | -12.7747 | -51.325901 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54ffa1bd-82ca-31ed-a8f1-c793ea175712 | -12.7552 | -51.2854 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab4109a1-5a7f-3956-ba99-922b4fcc7e34 | -12.7568 | -51.2925 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ed23b05-0c7e-3f5d-affa-b7ee13da9868 | -12.7585 | -51.299702 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cbc4a53-c92e-3167-8319-e021787e61bd | -12.7601 | -51.306801 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 476f6e54-7249-3128-a055-d4d3312dea5e | -12.7617 | -51.3139 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ecbbdbc5-132e-3eb3-a722-1ab5301a9452 | -12.7633 | -51.320999 | 2024-09-26 00:55:18 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf8f2574-8317-39f5-add3-fc03089ed945 | -12.6672 | -50.942799 | 2024-09-26 00:55:19 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edafbf42-10e0-38e8-b724-78cc07004ba6 | -12.7406 | -51.266201 | 2024-09-26 00:55:19 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c59f788-a040-3f42-ad8f-5577f536ac84 | -12.7423 | -51.273399 | 2024-09-26 00:55:19 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5390c638-1df5-3518-bdac-f25a3bc5019f | -12.7439 | -51.280499 | 2024-09-26 00:55:19 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 099936ed-3b9a-3b05-a27d-9a20476407a8 | -12.752 | -51.316101 | 2024-09-26 00:55:19 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa26e389-3154-3d64-aeb5-35f835ca5a9c | -12.6214 | -50.923 | 2024-09-26 00:55:19 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ecb2189-2b42-36b5-80b2-d3cee4eca6a5 | -12.4918 | -50.401901 | 2024-09-26 00:55:19 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e416d1c-887e-3220-9395-751229070c0c | -12.4935 | -50.409401 | 2024-09-26 00:55:19 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1ba2b6-59e0-3b4b-8362-3f283408694a | -12.4952 | -50.416901 | 2024-09-26 00:55:19 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19f187ee-b862-33eb-b57c-418751a4c6ee | -12.4969 | -50.4244 | 2024-09-26 00:55:19 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cae0a56-06c5-3b28-9065-77688220344e | -10.9874 | -44.403099 | 2024-09-26 00:55:20 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e806b90-4377-3580-81cf-42e37dab2dfd | -10.9918 | -44.4202 | 2024-09-26 00:55:20 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7feb61af-f48b-379c-afba-2267a8b7f7ce | -10.9778 | -44.405602 | 2024-09-26 00:55:20 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4b71426-2779-3e52-a43b-93e4d941cb4a | -10.9821 | -44.422699 | 2024-09-26 00:55:20 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01ae227f-1237-3e3d-b816-2c1158c106b4 | -2.6601 | -57.5507 | 2024-09-26 00:55:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ca6727bf-fcab-366e-ab88-8c60450ee30e | -2.6602 | -57.5313 | 2024-09-26 00:55:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 7371ffa4-6f03-363a-9156-91881e46462e | -2.6785 | -57.531 | 2024-09-26 00:55:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| efe62598-d813-39b9-91b6-5444507bb3f1 | -11.2119 | -45.499298 | 2024-09-26 00:55:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1994d02f-727e-3271-97d7-20d1cfdaba59 | -2.6968 | -57.5307 | 2024-09-26 00:55:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9e7fe444-bc1f-35da-a21c-f1765bb2e335 | -12.7011 | -51.914799 | 2024-09-26 00:55:22 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d49ef44a-27a7-3fa2-ae60-bd5a96ec658f | -11.2801 | -46.2738 | 2024-09-26 00:55:23 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a0504b94-5be3-37fe-8a78-8045820dd501 | -12.2903 | -50.512901 | 2024-09-26 00:55:23 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 784d8924-37c8-32a8-9a38-ed1a369138f9 | -11.5179 | -47.415901 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c8e3b5f-f007-3ede-b21a-7a497e2e47db | -11.4741 | -47.277401 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9587578f-9aa7-34c5-955c-4fecd292687a | -11.4767 | -47.288399 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6e17f55-2382-3625-a533-19f0fb5cefb0 | -11.5056 | -47.407501 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03613711-40a1-3439-b066-c43f58365602 | -11.5082 | -47.418301 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| caa0324e-a5e9-3e10-9e76-5a29b2abd991 | -11.4643 | -47.2799 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71d8685b-e17b-32b1-8680-f47391c62249 | -11.4669 | -47.290798 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa32018c-f471-319d-aaa9-13c3a45e3cb1 | -11.4696 | -47.301701 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13593630-d05e-3e22-8d76-0a3494f14468 | -11.4599 | -47.304199 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0c3238d-8115-39d3-bf06-d28f61fda346 | -11.4625 | -47.315102 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd7f6e92-ccd6-354a-99d9-7fe6fb12cc66 | -11.4651 | -47.326 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5a0f0c9-c417-3963-848c-2fd2433d18a1 | -11.4501 | -47.306599 | 2024-09-26 00:55:24 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72716c0f-d8a9-3ed2-b8cc-993ee5ce2419 | -3.3157 | -53.2325 | 2024-09-26 00:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 458e6648-9c02-326f-8f38-cfe3f1e7d81d | -3.3158 | -53.2122 | 2024-09-26 00:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 1453913e-4f26-384b-8fde-3c11160bacd0 | -3.3341 | -53.232 | 2024-09-26 00:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4f25bc7a-204a-32ee-b6df-292e857053d9 | -3.3342 | -53.2117 | 2024-09-26 00:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| b661308a-6376-387f-b8d3-f63a8886c2e9 | -11.1253 | -46.148399 | 2024-09-26 00:55:25 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3daa36d7-3b7f-39ce-a59a-cf39bc9461f5 | -11.1285 | -46.161499 | 2024-09-26 00:55:25 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39e769e3-1049-3bd7-ac7f-5788a060d0b2 | -11.4351 | -47.287201 | 2024-09-26 00:55:25 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3628280f-10c6-3576-96a4-91f12b2be352 | -11.4377 | -47.2981 | 2024-09-26 00:55:25 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d043cf06-43cf-3035-8b02-3e822191c68a | -11.4404 | -47.308998 | 2024-09-26 00:55:25 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d6c8692-7a91-3f9d-9b12-b0c14d6c33a3 | -11.4226 | -47.278702 | 2024-09-26 00:55:25 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53931e2b-807d-3894-ad2e-81610378f752 | -3.5673 | -50.3794 | 2024-09-26 00:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 9a2b7427-29e0-3f5f-98c9-f781f001da51 | -3.7821 | -41.5999 | 2024-09-26 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 8ceae234-ecaf-3285-bacb-64ce8b926229 | -11.8519 | -49.601101 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7f3e213-df6b-34c5-b670-5e168dc482fc | -11.8538 | -49.6092 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README21.md)
