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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edab0c5e-d9b2-3479-b628-7662478fec71 | -2.77762 | -48.58118 | 2025-12-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d419674d-2303-37d9-a2e0-197f3fd77f9c | -4.0723 | -46.14822 | 2025-12-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1e02d4f-640b-3b6d-aef1-d801e74e02af | -6.44836 | -39.78981 | 2025-12-16 04:23:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e7827d6b-57ef-34eb-b95e-967aa998c30a | -3.65584 | -47.55658 | 2025-12-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fbc902e0-c383-3cd3-a204-08d4660b3962 | -13.2629 | -41.30713 | 2025-12-16 04:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 75100ff6-3d7b-3e2a-a89e-abb4b6c0787f | -8.07298 | -43.14043 | 2025-12-16 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4734a8bc-b123-38dc-a780-289dc3944d52 | -8.42791 | -44.02784 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e695981c-b69d-35d0-a7f0-33940aee83b8 | -3.08491 | -44.88584 | 2025-12-16 04:25:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d53397bd-7205-3cfe-99ab-638bd5533927 | -1.9232 | -46.49993 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acd51f38-38c6-38b4-ac24-423b471303a5 | -12.51176 | -48.38181 | 2025-12-16 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0828013-e926-3769-82f4-736e54bb2cb5 | -1.33386 | -45.82387 | 2025-12-16 04:25:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3440fa8b-240b-3aac-a57a-481a74275b9c | -10.62082 | -40.51868 | 2025-12-16 04:25:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 063ee9df-a5b4-3c32-ae08-6f3b496ae17c | -1.86889 | -46.3904 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86286792-0e39-371d-8831-98c0c717b27c | -1.91902 | -46.50334 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4843c254-9ad6-3bc1-95a0-5a05742adc3e | -2.50424 | -48.03619 | 2025-12-16 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27eae363-4f38-3869-803f-2199d9efe2f1 | -3.43374 | -41.64859 | 2025-12-16 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 56f05fe4-adac-31be-a298-d4bbb929fdae | -7.8626 | -41.94125 | 2025-12-16 04:25:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e9f391a3-1807-3593-ae7a-605704f85fba | -1.60729 | -45.89999 | 2025-12-16 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d6327f87-db01-3701-8878-259c607d8f46 | -12.17276 | -44.35844 | 2025-12-16 04:25:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ebc00ea-18ed-3cff-b03c-5eda6f30d79d | -7.61314 | -47.0489 | 2025-12-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cff20570-0547-3076-a70e-6ec55ccde8c4 | -8.07241 | -43.1442 | 2025-12-16 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e268dbfc-f03a-32b6-8348-dc3b813483a9 | -1.61076 | -45.90054 | 2025-12-16 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0460e45a-1e7d-33e2-a99d-88629eb31142 | -3.42964 | -41.65192 | 2025-12-16 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 6826d2cb-ca42-3e0d-9416-a87cbb11c30e | -12.51356 | -48.38134 | 2025-12-16 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ac3570b-9745-3fca-a672-c8dcfa37da06 | -8.42398 | -44.03092 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa7d6100-4419-339c-8071-c47be3455644 | -9.56032 | -44.93853 | 2025-12-16 04:25:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d7e3a0d-d3d4-3389-ac10-f821d71b6455 | -2.96377 | -41.58382 | 2025-12-16 04:25:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4fd1fec-ee8e-391d-9649-88e30c4158c5 | -8.06839 | -43.14742 | 2025-12-16 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a10ed87c-98ea-31bf-8e88-cad2d7ce3c17 | -11.08891 | -48.25213 | 2025-12-16 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ca36cd4-4c96-395c-a710-4c8bde977fb8 | -8.98419 | -45.92912 | 2025-12-16 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6396210f-44ab-3b09-8c62-f2245d055af5 | -2.02993 | -45.81028 | 2025-12-16 04:25:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69b711fb-7bea-32c8-9add-5f86cd79fd5c | -10.36948 | -44.88517 | 2025-12-16 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 510bb9e0-8123-3f94-8231-9a445569657d | -10.48067 | -44.61041 | 2025-12-16 04:25:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18eb5936-f1ab-34d8-b604-9b7d0ca65baf | -3.65064 | -40.74261 | 2025-12-16 04:25:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc1fc6f0-104a-3497-be80-5b839b6e6d7b | -3.12957 | -45.48872 | 2025-12-16 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0c77d39-ead1-3ecb-9d3a-1269c663ddb8 | -1.70026 | -45.68703 | 2025-12-16 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a022a0c-1ace-3687-9ea1-f9842aa2d351 | -11.00037 | -44.34175 | 2025-12-16 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 190e30fa-0bd3-3a6c-91ac-bef6e5d0d49f | -8.42511 | -44.02372 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 99ea81d5-286b-3ee5-a0a7-356888c84358 | -13.26239 | -41.31075 | 2025-12-16 04:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c81bf8b-9211-3022-bfd2-de8460c0ef37 | -11.09176 | -48.25665 | 2025-12-16 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac0536c1-6c6b-3231-817e-346128f83609 | -15.33871 | -40.24621 | 2025-12-16 04:25:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4d93a413-4e2c-3da4-ae09-bcb4168c1a6a | -7.61597 | -47.05323 | 2025-12-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfa79b29-b9f4-31c3-8d0e-373b6a2ceafb | -12.34646 | -43.44735 | 2025-12-16 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 075eaffe-1331-3fa8-a032-b09e8a527b3a | -8.98917 | -45.94074 | 2025-12-16 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a992193f-cfb4-3444-8efb-84684c7b0954 | -2.99208 | -46.92651 | 2025-12-16 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2844cc5e-1778-324f-a8e2-7d4ba060c53a | -1.6707 | -45.80497 | 2025-12-16 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 587e89e0-d0a8-3d6c-a03c-1febb27809c4 | -11.75511 | -44.03256 | 2025-12-16 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94bbf552-0ef0-3f20-8bdd-767bb24b180d | -3.33817 | -41.79636 | 2025-12-16 04:25:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7e3fd44d-8c72-3638-a5a9-eac40a0029ca | -1.25872 | -47.17741 | 2025-12-16 04:25:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 711c5c44-392e-3969-b94e-098f0f261c6e | -3.65227 | -40.74041 | 2025-12-16 04:25:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| acae536d-a212-3412-be59-0b32cae4e251 | -1.86536 | -46.38984 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b97c689-8075-347a-ad84-9cc5ddbc6724 | -9.55699 | -44.938 | 2025-12-16 04:25:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52d88a12-34a7-31d4-b0b3-db31fa8f65b6 | -15.46404 | -39.15734 | 2025-12-16 04:25:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1da7245a-a9c4-3a12-97db-75283693fffc | -8.41669 | -44.03348 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c5b0de9-78ba-30e5-8ac6-a0423beeb3b8 | -11.0924 | -48.25274 | 2025-12-16 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20b4e03f-4f69-38b6-bd03-454a5bc54cb6 | -10.03385 | -48.12515 | 2025-12-16 04:25:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68156eea-76da-3f4f-8c0a-dcee6aa21e16 | -11.04991 | -45.4053 | 2025-12-16 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5643471-2de7-3997-a46f-08a6b7ccd9ff | -9.11975 | -44.4278 | 2025-12-16 04:25:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb8097b6-56d7-374f-b55e-ba096a24bd09 | -8.41277 | -44.03654 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbaa580f-91f9-342b-920b-0c838994bc2f | -8.66787 | -44.21872 | 2025-12-16 04:25:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f3fd6cc-47b9-364b-ae06-2d09085ffab1 | -1.84643 | -46.39493 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2242e91b-63ab-3f72-a499-ae62390447ba | -8.42455 | -44.02732 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b3e5c71-a198-3cec-a8e0-4beecc2639fb | -10.7704 | -45.03279 | 2025-12-16 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f28c4237-1516-3438-97d6-231ac87fadf6 | -15.45924 | -39.15668 | 2025-12-16 04:25:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f752b341-a9ac-3a2a-91af-79d60a28d9b3 | -12.57432 | -45.40599 | 2025-12-16 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2239ed7c-83c3-37db-986d-ab93db9a1e4f | -11.89005 | -43.71087 | 2025-12-16 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b70010a2-06c5-345e-abff-f5186fca0ea8 | -1.35942 | -46.99471 | 2025-12-16 04:25:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc7eea46-3484-3500-9d2a-51d1a0419e94 | -2.50116 | -48.04248 | 2025-12-16 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f8c41bb-c016-3014-94a2-31781b8366cc | -12.36693 | -47.66432 | 2025-12-16 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b11b6da-93b9-3f8c-92f6-ec9fdcc9c173 | -2.50192 | -48.03783 | 2025-12-16 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27b40c00-0b95-3d23-9c4b-d37dbd16d94e | -2.85195 | -46.8066 | 2025-12-16 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 632b5a07-7c2f-3931-88ba-1463fdf60773 | -8.42735 | -44.03144 | 2025-12-16 04:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96c5cf53-4bda-35d6-9af6-391552ebe557 | -7.49708 | -47.02979 | 2025-12-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19dc0976-0f04-3fd5-a46e-dc2444ef6da1 | -1.8506 | -46.39155 | 2025-12-16 04:25:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a34e041f-18a8-373d-adce-f0dbcc803831 | -7.61253 | -47.05266 | 2025-12-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1446a165-0d45-355b-8689-0cbd9b3dd12e | -1.36308 | -46.99529 | 2025-12-16 04:25:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4952d4f-468f-3640-8f7f-598351d34408 | -11.14487 | -43.32869 | 2025-12-16 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6095917d-92cd-3707-a17a-0d606d0768f7 | -0.85148 | -47.56967 | 2025-12-16 04:25:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a5f3302-5005-306f-8152-fd6bcc927a57 | -1.60383 | -45.89943 | 2025-12-16 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 68ac93bc-0e5f-3dfc-a01e-3b5f7a517a65 | -2.96438 | -41.57998 | 2025-12-16 04:25:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7429865a-0fbe-32ab-ada1-b1653cb83d48 | -3.43314 | -41.65247 | 2025-12-16 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 1b28adaf-2eb2-340e-8628-d989ed4108b5 | -10.79059 | -45.00291 | 2025-12-16 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 933a442a-2a5b-3ba8-8e77-2039e90ef02b | -8.06954 | -43.1399 | 2025-12-16 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 90b8d962-ad48-3bcc-a216-a5f897b26601 | -1.13287 | -47.16759 | 2025-12-16 04:25:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 426107a2-745a-3b11-abf2-df12d0ca377e | -11.14506 | -43.32575 | 2025-12-16 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3199cf36-40c6-3e83-b33d-b76f547d5487 | -11.89064 | -43.70697 | 2025-12-16 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecfa2ad5-9668-3710-a78e-7c6c2d117536 | -7.86324 | -41.93707 | 2025-12-16 04:25:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| eebcd082-9432-345f-b134-c755553288e4 | -7.86687 | -41.9376 | 2025-12-16 04:25:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5ad2bb7a-e700-357d-82e6-80cf9e4d3753 | -15.14022 | -41.83714 | 2025-12-16 04:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9b0d9936-aef8-3814-8b1e-af26ef6b399a | -7.61192 | -47.05643 | 2025-12-16 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72c65f31-adf4-3a8b-8fc7-7ae7b0513262 | -12.51009 | -48.38075 | 2025-12-16 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d910f35-90c6-3084-b96d-5b2762bc1716 | -1.60443 | -45.89562 | 2025-12-16 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6531d36-fd13-3a69-93ea-cc707d9cf1ff | -12.56929 | -45.39419 | 2025-12-16 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 20b1f60f-0535-3389-9bf9-afc08316a4ce | -1.6079 | -45.89618 | 2025-12-16 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2329018e-d498-3dd9-ac6e-4c1533443e72 | -0.84866 | -47.57194 | 2025-12-16 04:25:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b003c26-0343-399b-8a52-76250546afe5 | -2.16579 | -50.26359 | 2025-12-16 04:25:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c8e46ee-930f-3609-b8c6-8b9bd076ac2a | -3.12899 | -45.49231 | 2025-12-16 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1881346d-7f9b-3868-8dd2-93ae72d2123c | -3.32953 | -44.8601 | 2025-12-16 04:25:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e831d95-c8bf-38f3-9924-e4ff6c6f3d7c | -3.43024 | -41.64805 | 2025-12-16 04:25:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b7d5764d-3fba-3dfa-914e-807da6b97a5e | -12.16593 | -44.35735 | 2025-12-16 04:25:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README9.md)
