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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88777ba6-993a-3fbc-b93e-7c5ed459aa81 | 0.58707 | -60.36083 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 426838e1-7360-33a8-b756-d83348db0d63 | 0.72322 | -59.83882 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5dc0ba10-9f1e-3e20-af0b-40428e3b9ba4 | 1.48778 | -59.93812 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b2f390f-0a9c-381f-a7d5-eda3be6720bd | 1.20338 | -60.61745 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d962629f-22de-39e3-8185-8ad6bed02e32 | 1.11553 | -59.19315 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e285334e-9e00-3847-a184-0a7d74e7ac3f | 2.52325 | -60.80674 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2778f266-dd79-3729-9c60-008fb5c2583b | 1.73549 | -60.38636 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5857b5e-0d9f-3fa8-afcd-e66e702897b2 | 3.15961 | -59.91315 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 95a540f9-2696-3261-9ae1-31b60fd0b678 | 3.48535 | -60.77995 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ea06061-a179-3ddd-b4d0-18164ea8be13 | 2.8277 | -60.77662 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b96f83c5-eabf-3a37-a988-8349be8b5616 | 0.89648 | -60.09377 | 2026-03-01 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f595a259-5771-3656-b296-5abb7a9d957f | 3.44995 | -60.81379 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24b4c134-f8b3-3e38-a66a-3d35851ce4ec | 1.0677 | -59.25528 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8d9ea3b-7595-3723-a46c-80f25a7d9866 | 4.15178 | -60.70772 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d49305c4-f5df-3ec6-9363-c67b0355c231 | 1.49054 | -59.93417 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20fb21a3-4af5-343f-8d90-c0b8d90c1981 | 3.44979 | -60.28813 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a98228a6-3819-304f-a723-2e33d1bcd60b | 2.73021 | -61.21841 | 2026-03-01 05:29:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf423126-2efa-329f-bc9c-184fa6faf40e | 1.84822 | -60.41082 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c772827-8fe1-399f-ba3c-eea69275ce11 | 3.49197 | -60.77894 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9559a90-7f3b-38f9-9e8b-c54798482ccf | 2.68221 | -60.42966 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3da60a8b-f753-30dc-a10e-057b8159e4fe | 1.4939 | -59.9125 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 51d30538-4295-3239-b7e6-f79364a00a28 | 1.48616 | -59.9278 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8f57528-78ca-3067-80fb-da28ba7c0d3b | 1.50104 | -59.91492 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 5a7b6f24-cfda-327c-89f8-3b99156e9df6 | 0.85307 | -60.40299 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24e014e5-c844-33ae-bded-7cc143efce81 | 4.42149 | -60.75777 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fd8047b-154b-3c54-baed-43beb848a784 | 3.91405 | -59.81797 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b3e3add-41e9-3048-88d2-796d3031dd3b | 1.06715 | -59.25174 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f480f7ce-8fcc-3b3f-a090-97b60d95a8da | 1.0793 | -59.2459 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 428037fe-7f5f-34c4-b9ee-5c06473483c6 | 2.82716 | -60.77317 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7677e4bd-2884-3887-8841-d4e8f2055476 | 2.81779 | -60.77814 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dbd5098-3382-3d66-be7f-67a41f4ca5ac | 4.07412 | -60.34442 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7951e46-5ca2-31f3-b53f-6b5d340164c5 | 0.57378 | -59.90452 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7690c77-7a0c-3826-91bc-44d5f90e743a | 3.44609 | -60.81082 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a286426c-27a2-38a5-ae60-8a90f31563ba | 0.46645 | -60.39369 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e9fdd85-6e81-3b6f-b62b-054c3d593e50 | 3.45218 | -60.80635 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0b5a74a4-d9bf-3bb1-b614-a9e64fbb4894 | 4.09856 | -59.89095 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 239468ab-17c9-3362-b149-3e08f3214581 | 1.37006 | -60.05481 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 204be630-9064-3fcf-ba3b-3eaebadf9425 | 0.6693 | -60.01337 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b89640bb-c9d1-3caf-bec9-dcff395ed1d1 | 4.13237 | -61.06559 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eba78ba-e2b4-39bd-b231-d5ba6ff6e8ba | 1.87863 | -60.91157 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2a9db86-95f0-37db-a426-e2db457399c5 | 1.49384 | -59.93365 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9d8a0a0-27fa-3f20-a2d1-94860b61edb6 | 0.94841 | -59.45046 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c64809d5-5d2c-38ed-a065-d4d51daa07aa | 4.24267 | -60.81151 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 130b8ab3-cc25-3b3e-9def-6b6eb345f6cf | 4.23935 | -60.81202 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cbebd74-5a39-3bb2-92c8-7e73ef58ebb3 | 3.15793 | -59.92393 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 362b9c2a-434a-3702-94a6-d22bc66d4c98 | 3.475 | -60.29828 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ec0b377-223b-3653-beaa-a0564d376f79 | 3.16237 | -59.90922 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a26e9e2d-c1b2-3b9b-b2dd-2e7bade24d36 | 1.48508 | -59.92091 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5816aa1b-3e50-349e-9acf-4ddfa20b760d | 1.48724 | -59.93468 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c9ba1a5-ff51-32dd-b387-d21eebd4edb9 | 1.49108 | -59.93761 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bb17a42-5e99-3822-bc77-2d6c873d1ddd | 2.30165 | -60.58789 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f54b104-0911-331e-9018-d6ec1ccd906b | 3.32175 | -59.88725 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01c0b838-6a12-3f24-9f5a-065118c8d66c | 1.4864 | -59.9308 | 2026-03-01 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 7ae785b8-01dc-34b0-bb3f-c6b633013dfb | 1.4682 | -59.9119 | 2026-03-01 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b4332bb8-07f9-3779-b071-a1a5beb04852 | 1.5046 | -59.9306 | 2026-03-01 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 06e5ecb4-2464-3e18-8069-3773bd1b45a1 | 1.5047 | -59.9116 | 2026-03-01 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 0f9cadee-ed9d-388b-a8a1-a3ec3c22199e | 1.4864 | -59.9117 | 2026-03-01 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 22b7d307-48a0-3e15-b4ac-76301551eb39 | -12.29408 | -61.96371 | 2026-03-01 05:31:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0873967d-20a1-3715-b0e7-bf78c7a2138c | -12.29353 | -61.96739 | 2026-03-01 05:31:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca8c5e0a-eb4b-3087-bf87-3131b1f7fccd | -21.71084 | -56.31609 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e372bdd1-4774-3d3e-a20a-7c331db807d2 | -21.69006 | -56.31025 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fe15a2a-d699-3f84-801e-f7adbbcb2bf4 | -21.696 | -56.30411 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7a7a1b9-f9f9-37a6-b2fa-a2f0eacba44f | -21.68973 | -56.31364 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f7488f1-f27b-3df5-8424-0b2e4946fb35 | -21.71614 | -56.31652 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c097b6ec-610a-3d25-82e6-6ddf7ffb14a5 | -21.71579 | -56.31998 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7639683e-8bfa-3be5-b60a-af8feb6fce5a | -21.69567 | -56.30752 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca13d551-502e-3d50-bebb-a0d76777ec41 | -21.71118 | -56.31269 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71679987-c842-33f1-b8df-9b0d9a7b1b39 | -21.70557 | -56.31539 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeee8f81-9331-3172-9cf1-ae8b6a2c6a1d | -21.7059 | -56.31204 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c54af8b-1778-303c-ab6f-701f630c8a74 | -21.71051 | -56.31948 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43c47a30-234c-3412-a93d-6f10bda38ef1 | -21.71152 | -56.30922 | 2026-03-01 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b34df371-5acf-3854-b9ae-993e11463397 | -18.80862 | -57.63539 | 2026-03-01 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| b01cd398-9e85-39af-b815-2c4dc56891de | -23.28618 | -55.33199 | 2026-03-01 05:35:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a34801ce-caf9-3edd-89c6-2b0305c6b9b5 | -23.28008 | -55.33574 | 2026-03-01 05:35:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cc98f67f-df8b-375c-9e07-95b7075f481e | -23.28581 | -55.33618 | 2026-03-01 05:35:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8cc505a4-5fed-33ce-a664-e81cadde0af6 | 1.4864 | -59.9308 | 2026-03-01 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.0 |
| a0550597-5b12-34a5-8971-1c7a0eb0bbea | 1.5047 | -59.9116 | 2026-03-01 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 3c8e7458-93d0-3257-beff-4cff7765b3e0 | 1.5046 | -59.9306 | 2026-03-01 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 6825d1a9-e684-3204-9096-7c656492ab55 | 1.4864 | -59.9117 | 2026-03-01 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 156.2 |
| f2529d65-9ccb-312e-9d7c-7394cd0f6c57 | 1.4681 | -59.9309 | 2026-03-01 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 980f73d0-f791-3c39-b42c-139a3bb0cd5b | 1.5046 | -59.9306 | 2026-03-01 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.3 |
| cfa3d642-839f-3837-bfcd-7830997aafa1 | 1.4864 | -59.9117 | 2026-03-01 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 5487894c-5efd-363d-9de0-e574f1993d15 | 1.5047 | -59.9116 | 2026-03-01 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 65c577e2-aede-3d87-90bc-047386e6a319 | 1.4864 | -59.9308 | 2026-03-01 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 36806115-f908-32df-87e0-18d4a5c726b4 | 2.62001 | -60.61342 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b724a9e-0f45-32ab-a035-5c5c9f6a4005 | 4.15009 | -60.7108 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46d6f399-bce0-3a1e-80c2-fd2ad8ae9837 | 2.82752 | -60.7784 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 30a8c92d-4068-3ee0-b843-dd55f26ddba5 | 2.90698 | -60.44151 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1cb222c-150e-33fd-bbb6-e95af19009eb | 1.51425 | -59.92846 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fb999931-efb7-346e-89a5-8567fe9f8e59 | 1.21164 | -60.6213 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb8e6273-e68a-3a94-b1c4-6d7d29d0de7e | 3.49206 | -60.77695 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8556c0c6-3ea3-37b7-a318-17f4be1ef066 | 4.15069 | -60.71454 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b928a6e8-6053-3df5-905d-7d239bb5a441 | 3.15905 | -59.92352 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06cce714-7f1b-37f7-8a9b-74463dede3cf | 2.81909 | -60.77976 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf83f6c4-74cd-3c71-8b88-ffc1c20a3ea1 | 1.06985 | -59.25455 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce6f7a2c-d456-3b85-afd8-136a1410f2d6 | 1.50518 | -59.9302 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f088b59-a246-3a14-8e09-b8c828aebaf1 | 1.20819 | -59.97241 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8621f97-453e-3ec5-8ff9-4d7bea8c7b47 | 1.87368 | -60.91245 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4d3240a-33a5-3cad-a82c-e660c5aedcb2 | 0.70789 | -60.27555 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cc1fdc5-411f-37d1-8875-055750087110 | 1.47628 | -59.92522 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README10.md)
