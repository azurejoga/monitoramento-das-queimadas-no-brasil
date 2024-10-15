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
| d2b6d86a-7723-3b0d-a37e-1e25f0508474 | -5.83916 | -44.70992 | 2024-10-15 12:44:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3f376614-50cd-3ad5-9833-2a91e9ad8ea6 | -6.29556 | -53.56082 | 2024-10-15 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 550a27ec-3999-3d59-aed4-73238647af8b | -6.45145 | -45.85663 | 2024-10-15 12:44:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a013b6e7-1f3a-3da0-9942-3f9b3fbd5270 | -6.46599 | -45.17461 | 2024-10-15 12:44:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 1dfd60c9-938c-3214-aa44-cdcc64512c42 | -6.49668 | -46.12107 | 2024-10-15 12:44:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88640e17-f0e4-3265-ac02-da6dbb6857d2 | -6.69766 | -46.77282 | 2024-10-15 12:44:00 | TERRA_M-T | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 49a5f15a-783c-3cb4-87f1-13ec0ccdae7a | -6.80419 | -46.48399 | 2024-10-15 12:44:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f2ea9b81-2fa3-3c48-8ff0-d6ab731719eb | -6.80548 | -46.47501 | 2024-10-15 12:44:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 8ba2625a-1eec-3663-ba45-f770bd6509b8 | -7.0957 | -46.76876 | 2024-10-15 12:44:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1d5b7f30-5e03-3b45-a80e-b8b5e0738acd | -7.16198 | -46.62304 | 2024-10-15 12:44:00 | TERRA_M-T | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5dab16af-ee83-3cd8-89ea-1c1cc9d9a982 | -10.02561 | -47.28105 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 27e51632-c011-35cd-a94b-6a416dda1ee2 | -7.2466 | -46.35613 | 2024-10-15 12:44:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 445425e8-102f-3a14-ab4c-985e08988f77 | -7.24788 | -46.34708 | 2024-10-15 12:44:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 954ba7a8-d2c8-330f-b8cf-7c4aabdf5435 | -7.60657 | -46.79895 | 2024-10-15 12:44:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 24317b5c-8ff5-34d3-b360-dc564fae9e58 | -7.85954 | -46.25498 | 2024-10-15 12:44:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ea06616e-5ddb-38a0-8cc7-cd6f8d217708 | -8.25526 | -45.72943 | 2024-10-15 12:44:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| aac06e7e-57f8-3550-b8b1-60350fb3ff13 | -8.26313 | -45.74044 | 2024-10-15 12:44:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1ce7feb8-2341-3edc-8841-6ad8a4720252 | -8.26448 | -45.73073 | 2024-10-15 12:44:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| afa0a4a5-ac7a-3004-b6ad-279718fcbd1f | -8.316 | -46.86625 | 2024-10-15 12:44:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cd084645-d1db-31d2-841d-3b0a258aca3d | -8.47535 | -46.45947 | 2024-10-15 12:44:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 7c195daf-28e9-3e11-8c3f-a07c3112b9c1 | -8.5921 | -47.19527 | 2024-10-15 12:44:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c5e4cb0a-e3c4-3fe5-98ca-9276f2e2025d | -8.60098 | -47.19652 | 2024-10-15 12:44:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bd95bf6a-eb07-3ec9-804b-c5df36a91df7 | -8.67628 | -46.98775 | 2024-10-15 12:44:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2588dfa6-dfc5-3d36-94d6-ea09b8291729 | -8.68952 | -46.63901 | 2024-10-15 12:44:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2b038f25-dc5b-33bc-9730-df6672adf8de | -8.68992 | -47.53362 | 2024-10-15 12:44:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 86b02c8c-b04b-36a4-abc4-4a9827971733 | -8.69492 | -47.5616 | 2024-10-15 12:44:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4eabe949-2f5a-348c-8b70-ce8bcadc5797 | -8.69848 | -46.64029 | 2024-10-15 12:44:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fb1c8121-bc65-301f-96cc-53577c64ab01 | -8.69978 | -46.63115 | 2024-10-15 12:44:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0f9b3997-a4ce-3777-8af2-d7e243710ed7 | -8.76152 | -47.55032 | 2024-10-15 12:44:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a150416c-beda-3a12-9e41-6adffeb81a7f | -8.86166 | -48.69522 | 2024-10-15 12:44:00 | TERRA_M-T | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 5926b31e-8647-34d9-83cb-5a0ead381cc3 | -8.86333 | -50.71856 | 2024-10-15 12:44:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f7b9f34f-f722-36fb-85df-5f983f776f7e | -6.48728 | -39.97071 | 2024-10-15 12:44:00 | TERRA_M-T | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 637a1d8e-be92-3757-820b-b30d614b34ef | -8.92667 | -47.1698 | 2024-10-15 12:44:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 091eff81-bd43-36d3-91fb-a22ce4147b29 | -8.93428 | -47.18001 | 2024-10-15 12:44:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| b9331de1-b606-3477-b301-91e6fb780e04 | -8.93557 | -47.17105 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| d9bee729-62e7-30de-b75d-57b2ec62f1fc | -9.00676 | -54.50687 | 2024-10-15 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 8d75e1ca-566a-366f-9022-abb89b285bd6 | -9.08714 | -47.78553 | 2024-10-15 12:44:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fd9ff49d-8520-3c39-88cc-10aa6aa097a2 | -9.10578 | -47.07938 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c0fa1b28-06f2-34a2-aacf-af07c5e545c2 | -9.1134 | -47.08963 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9c987e3e-d7ac-3236-b514-940558f72418 | -9.11469 | -47.08064 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 412e97a3-c63d-37eb-ab38-d4f2c5c612ce | -9.12113 | -47.03559 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8fe125b7-c43f-3144-ad22-c68a3c4d1b49 | -9.20261 | -47.56231 | 2024-10-15 12:44:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 05ac37e6-9edc-333c-9242-4b3dc3ed0b21 | -9.20987 | -48.64926 | 2024-10-15 12:44:00 | TERRA_M-T | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 31b601c6-45a8-319e-9f12-9cad17eb52a7 | -9.21042 | -47.94605 | 2024-10-15 12:44:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8d9d1b7a-b289-33a2-ba88-c8167445f5c0 | -9.44054 | -46.01297 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c365a9d2-e0c7-3dca-835e-e5fd20aa10a0 | -9.44749 | -45.89521 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 34ba8a42-97e3-3182-ae9b-a615f21b7731 | -9.44885 | -45.88546 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 275f99ee-759f-362d-ae3a-5a511b7aeb38 | -9.4502 | -45.87571 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c47c18b8-0cd6-3f15-970a-2ddc3a9ac483 | -9.45675 | -45.89653 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b1f65f1b-a16b-3059-9bda-d55ef97b4958 | -9.45811 | -45.88676 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 8caf89f1-3a8a-3386-9bb2-02be5d34f268 | -9.45946 | -45.877 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 04ad7285-2357-3b6a-bd66-b135913c58c6 | -9.48762 | -49.57204 | 2024-10-15 12:44:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1c5906fa-9594-33e9-a7d7-4b4109677c96 | -9.4969 | -47.81469 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| da50b935-eddc-3296-ba24-170cd69b4dea | -9.51138 | -45.84386 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 040e64f8-0b89-35f2-b48d-cf77bca27cc3 | -9.51276 | -45.83408 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 1c24b310-2400-30b9-804e-f3ab8cdba152 | -9.51934 | -47.79657 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| d4d99394-51e9-3456-a5f3-b91c5d6b16ce | -9.57677 | -50.20533 | 2024-10-15 12:44:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5d59bfe6-faeb-3ac9-882b-51e6b431aa01 | -9.59191 | -46.6403 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cbb3a17c-2181-3710-9a08-5f35e93f6e06 | -9.60063 | -47.7353 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 130692a0-1dc0-330f-8c84-60259a86e062 | -9.60321 | -47.71744 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ce7aab10-d759-311c-9cb3-2e41d6e1e954 | -9.60549 | -48.59245 | 2024-10-15 12:44:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| db9401e4-475f-363a-814e-5078e8966bb7 | -9.62077 | -46.04049 | 2024-10-15 12:44:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 16eb6ada-bac0-3902-a8df-6f5aff6917c2 | -9.67219 | -46.91948 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 190f1a83-30fa-3033-8555-6e75b1664645 | -9.67348 | -46.91037 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ff0bcea1-7e78-378a-87f6-7d9bec7826a9 | -9.68114 | -46.92074 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 2b1d468e-6e42-3410-952c-b3bbfc6a2cea | -9.71438 | -46.94395 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 556f9d44-9042-365b-b168-7bed4bfac578 | -9.8082 | -46.67351 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 006b6762-8786-3a72-9cc5-fbb32e3506f1 | -9.80951 | -46.66422 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9bc3ba19-486c-319c-b2f2-ecb04f235413 | -9.88805 | -47.01814 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c5fcef16-e438-38af-8b4f-2eb8adb0b860 | -9.89699 | -47.01941 | 2024-10-15 12:44:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d0a19778-a1e9-3ca3-977e-c1b1b20f9d51 | -9.9658 | -47.25417 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 235dda46-d986-3598-9576-6aed63da6d19 | -9.9668 | -47.43805 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4e0b9dd7-e09f-3c15-a82a-7a680e93c743 | -9.96809 | -47.42905 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d49ee012-02c2-3e2f-9dfa-08986113614f | -9.97472 | -47.25543 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 58f81527-65e2-3199-8a55-95de50d3104b | -9.97967 | -47.34811 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6202b6f1-1ac6-3d59-86b3-0b63df59490b | -9.98857 | -47.34937 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e809f875-e833-3133-8ee3-e386b3255117 | -10.04493 | -44.19584 | 2024-10-15 12:44:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 54f21681-68e8-3585-a8d6-9b16c6945500 | -10.04657 | -44.18343 | 2024-10-15 12:44:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b7737c8f-5460-3c93-8dbb-fc785fd389d2 | -10.05739 | -44.26005 | 2024-10-15 12:44:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| e2693438-a2b6-327b-9372-c4ea5dfd944d | -11.06454 | -42.23704 | 2024-10-15 12:44:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| c288e307-bfe3-37e2-bc2f-f7786d857de9 | -11.07203 | -45.73242 | 2024-10-15 12:44:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 641add92-8842-3ab7-a9cc-0b7526b978c0 | -11.1402 | -45.9049 | 2024-10-15 12:44:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 7baeb82f-8dd9-3d1d-ba93-7537e80c5755 | -11.1416 | -45.89477 | 2024-10-15 12:44:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| dff37cad-56d5-3d16-b533-ae12b2cac958 | -11.54353 | -42.18634 | 2024-10-15 12:44:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 36.9 |
| 5e4f2bf8-9339-3114-b779-aff929da4b94 | -11.91319 | -45.77583 | 2024-10-15 12:44:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 85287255-ab26-3261-a942-b7950c62fe7f | -11.91793 | -45.77205 | 2024-10-15 12:44:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8e9d56fa-823d-3642-8d0b-f387101e948d | -3.30747 | -42.49188 | 2024-10-15 12:44:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e1f624d9-d0ed-3838-be14-d7c3b16ed245 | -3.34774 | -41.37188 | 2024-10-15 12:44:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 20.0 |
| e910efac-3cad-374d-9a60-80d87e3e3566 | -3.35928 | -41.37352 | 2024-10-15 12:44:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 57d5da54-f1c8-3d4c-b837-d6bbbb4e77bc | -3.39854 | -43.00655 | 2024-10-15 12:44:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3846a8db-c52d-3af8-81d3-8bcf1755efd6 | -3.71211 | -42.30402 | 2024-10-15 12:44:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 0cce8bf5-f442-3243-9cb1-9dc97b6a265b | -3.82762 | -42.79231 | 2024-10-15 12:44:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4b93eee4-ac08-3ac5-be52-9f96b98c3720 | -3.82936 | -42.77987 | 2024-10-15 12:44:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 402d2875-1e2d-3496-930b-c22385020135 | -3.91887 | -42.40538 | 2024-10-15 12:44:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| e2fb8be2-128f-3d66-91a8-52f3f4da32f6 | -3.9244 | -42.41317 | 2024-10-15 12:44:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 4080d7e6-fb4a-3df2-85bd-399b099ab20d | -4.09158 | -42.29732 | 2024-10-15 12:44:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| ef841221-afa3-3b35-b69f-1987b3e1ed38 | -5.01051 | -43.23885 | 2024-10-15 12:44:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b650c856-3c6b-39b1-a651-41865c7996f6 | -5.01215 | -43.22677 | 2024-10-15 12:44:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| baa3ca96-38cf-3608-a4c4-ec66080a74e0 | -5.3762 | -43.25149 | 2024-10-15 12:44:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 77c991b6-37eb-36e6-8e47-81a3a3aeae8e | -6.39883 | -41.62111 | 2024-10-15 12:44:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |


[Clique aqui para ver as próximas entradas](README80.md)
