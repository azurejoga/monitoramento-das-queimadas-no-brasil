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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83a644e5-5d30-3589-aebe-4cd283c4baa5 | -9.45474 | -56.64754 | 2025-10-05 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caf5377f-c000-3996-bdeb-f8e356040c1a | -9.60442 | -58.98385 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97c5cbc7-fedf-337a-b8ca-d810a9c1e7ee | -8.90454 | -46.5926 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 753896e9-9e0f-3386-8194-6609441ddfe7 | -8.55419 | -46.27733 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 825e2d47-0573-3dd6-91a2-2287f76c24be | -9.56079 | -63.20864 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dc39865-8185-3fb1-bb39-419b8a7bac7b | -10.65279 | -46.34396 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fb02979-a20a-3a70-8fc9-27039c184050 | -10.94733 | -47.08579 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14c2cb43-9b80-33a1-b509-0f647525c7d0 | -10.46712 | -57.49373 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79139023-3883-39e4-979b-bcdd257f113d | -6.18031 | -44.62586 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d56e54e6-61d2-32bb-a37b-02be8d453c4e | -11.00121 | -46.51506 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb8d879c-e8c9-33f6-b992-131c2c8c4925 | -6.14662 | -44.60302 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6faf45c9-3a30-31da-99e6-a75a34d0928c | -6.15337 | -44.604 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 629631be-b8f1-3b84-91b4-78c14ed16202 | -11.71084 | -45.35686 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8a62ccf-67f7-3bff-9988-43b8044ebee4 | -3.77969 | -53.93248 | 2025-10-05 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d96de73-e72f-339c-bc83-b07bf9cda0a0 | -9.16106 | -58.30955 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddbb3b43-c59f-3f83-a676-a4e084a27f1d | -5.98303 | -44.36242 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3958870d-d044-3aa4-aeb6-56478f71edd0 | -11.11446 | -47.14172 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2aaec5bf-fd4f-39a6-adb8-d71b25d9158a | -10.46098 | -57.51102 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f2b62ff-8205-3985-95fc-035155974444 | -6.43118 | -46.01926 | 2025-10-05 05:14:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e0824b7-457a-31fb-a5d3-3fd519cf0bbe | -8.8734 | -50.88939 | 2025-10-05 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d014562-6053-37a5-9cf8-3eabbc33316e | -9.91287 | -50.19567 | 2025-10-05 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e34e2dc-d236-3388-9406-81f9150721c8 | -11.09969 | -49.86013 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63d218b1-775a-3de5-9bd8-12c7797984af | -7.31896 | -45.98902 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d86610eb-5544-394e-b4a8-f6142f103e4e | -9.91281 | -50.18885 | 2025-10-05 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b4b4921-c0a8-38b5-9c35-f9787f21a396 | -11.05479 | -47.7715 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79c93911-a572-3dd5-8cb7-08daf283606c | -9.24694 | -63.29193 | 2025-10-05 05:14:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3795758-2a05-360f-9d47-deb96389257f | -5.34522 | -45.30368 | 2025-10-05 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2c7f41a-6b4e-3882-8825-1f235c5b2567 | -11.11357 | -47.76497 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fba75b2-9447-35a5-bfe4-86b6b9be990a | -10.85331 | -47.96988 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbcc57a8-b78e-3bf6-a502-f872455ec514 | -8.60316 | -46.29478 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0780c0df-6b87-38bb-9559-0b412399377e | -11.10548 | -47.87991 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7ccc7da7-4188-3b0a-adb1-1ca774861f9b | -6.1575 | -44.5736 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9269500-b9be-3b37-af27-c80c2ca9e052 | -11.78469 | -47.55641 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0c403a6-7ce8-36f7-97c7-c816a42f2071 | -8.05038 | -54.90059 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c4ff6a-60a2-3f7d-8f65-53d3aa7084d9 | -8.60443 | -46.28513 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d33fddd2-e38c-3673-8472-1b2ba7117406 | -11.52269 | -47.67517 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f6ec3d6-c2d5-33ad-8f6b-b4119a6023b1 | -10.46265 | -57.50032 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81b32192-937d-364c-9c58-5705404a56aa | -5.00508 | -47.21133 | 2025-10-05 05:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde5e666-bc99-3fa2-9f07-69d530c970e2 | -9.80148 | -48.27901 | 2025-10-05 05:14:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa816eac-6492-335b-97a6-841a4cf23d38 | -9.19571 | -58.96165 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a11c4415-6856-391b-a454-5088d0597548 | -11.92994 | -46.43351 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44bfd6ba-83c6-3bd2-b771-609cafe550e3 | -11.11865 | -47.20835 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc07ce5c-d925-3da3-8a58-6d71ed461f2c | -5.21336 | -46.18511 | 2025-10-05 05:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 833b7442-a9b5-3eda-9129-f3445df45b5d | -10.64432 | -46.30529 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 253cbf4d-3e42-37ef-9532-469987afa70f | -5.97619 | -44.36147 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f083e4c-d7b9-3ee3-91b2-3e1a0614c42d | -9.04437 | -47.01313 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc7a3058-8eed-30de-8f6d-ae200e94d885 | -9.9063 | -50.19941 | 2025-10-05 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9f18bf5e-4190-318e-a44a-a1d5b39eafae | -9.44683 | -56.6538 | 2025-10-05 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0652f385-f81e-394c-a7be-f6eacd063b86 | -8.57482 | -46.31586 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 436e4c68-0e1e-3372-9e6b-49bca03f2c03 | -6.16438 | -44.62423 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a7e62f71-df65-39c2-9749-7226f586616b | -7.42462 | -46.50375 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2675f96-75c2-3231-b363-a0c917a10459 | -6.4445 | -44.1532 | 2025-10-05 05:14:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c689d1ea-5e01-3052-a932-042ad386cd7a | -11.35542 | -47.6642 | 2025-10-05 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c553ffd4-2250-3bf6-9f2c-efde1e449e1d | -9.45135 | -56.64703 | 2025-10-05 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a11e5d87-ef5c-30df-8e2a-4370ca78200c | -8.5497 | -46.31236 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e78a41b-0ae7-3e95-852d-98e680cb76d0 | -7.20868 | -46.86313 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99ffd343-6668-34a7-8917-f6c7df666939 | -7.75558 | -46.3119 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0968a78-304c-3771-8ce8-16a7f1135d2c | -10.36512 | -48.28617 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe2d2f53-07ac-3f5f-9537-375a0e1092e9 | -5.64476 | -43.91773 | 2025-10-05 05:14:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6107ebd2-69a0-3b90-a14b-f19937c67760 | -11.54315 | -49.80669 | 2025-10-05 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86dbdfb0-73a9-362c-a067-786528cf5a06 | -9.84589 | -60.26923 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05bd25ba-5ecd-36b9-9da5-f6c475d6c3d8 | -11.07236 | -47.90676 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba3aa3e1-ac10-39ea-88df-f9ffc254b1db | -10.36366 | -48.16344 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a6eaa6ab-74fb-3c53-b893-90b1c5bc89ec | -8.04384 | -54.89543 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fdef22c-2243-3d8d-95ff-6c023c273630 | -5.96518 | -43.50985 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45a13e72-3e40-36c7-8c1c-c0edf9b1d55b | -6.16685 | -44.60617 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ec4c5d4c-be64-3b8f-b556-5027a2c88d3c | -8.6068 | -54.96948 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dae1c71-7b36-3fc7-aeeb-81b94d4deaae | -6.42423 | -44.47248 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a7a35f2-d683-3b2e-9bf5-090b8cb7787e | -11.82758 | -45.07723 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c06fa88-cd21-3394-a0a0-0d96c41cfe2f | -7.54712 | -47.27999 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 176a49fa-af94-3a41-9f84-3b64b1b0f819 | -10.99963 | -46.51448 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0bf0670-a851-3920-8a92-e1a14cd7a533 | -7.20265 | -46.86286 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c00188a-9613-327e-85f1-1a2ff6767a16 | -8.60061 | -46.28553 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6d6a6e80-496b-32ac-be41-e6fba119a276 | -10.57 | -48.68488 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbe6de5f-3b90-38ef-be7d-a637bafd14d2 | -9.07189 | -58.93097 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbb7f08c-044a-3ec6-89f3-eaf28a9951d4 | -9.33602 | -54.5134 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05669e7d-60eb-3214-90bd-95a1d26d40e4 | -9.13258 | -61.87421 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 064fa124-6aca-3745-9b31-1a67defec9a8 | -11.10834 | -47.14052 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85b79a54-d96b-3f1f-a206-2bc7e04dfb80 | -8.86448 | -46.81241 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e10017b0-ae7e-3bbc-8550-e793438751c3 | -9.04336 | -61.64129 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25ab42e2-5809-3dcf-94d1-41a3b757d51b | -9.90904 | -45.962 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 243a0222-bf1f-3328-8e5d-cdde524ff258 | -8.86022 | -46.84172 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 873d6fdd-dc9e-3bee-ba72-2a70fc64b558 | -10.64511 | -46.35358 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2381631d-c6c8-3165-a19a-3645f7290df9 | -11.6194 | -47.74663 | 2025-10-05 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e8d67b8-bec5-30ec-af56-b6b7b810bddf | -4.99879 | -47.21489 | 2025-10-05 05:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30fe8491-eb8d-3675-a529-2a46e4c7767f | -10.39944 | -45.40615 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 534ca4ca-4648-34fc-934f-9b5914b9c502 | -9.03694 | -61.64341 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad9e16a9-2b51-3239-9307-eb10d550a52b | -9.90983 | -45.95536 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e5b7483-8627-3c67-b906-57afc6cabb4e | -11.78209 | -47.92727 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca587632-ed0b-32bf-90aa-4705bd7552e8 | -9.05462 | -47.01766 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5c96f5b-3897-38de-a9a2-e430a4cab12f | -8.90569 | -46.68338 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9d7121b-603e-371a-aa0e-20ecb32ce435 | -6.99642 | -44.21146 | 2025-10-05 05:14:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cacee705-3c58-3c51-811f-779af7ac4615 | -8.54406 | -46.30654 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d62954aa-1a54-372f-82ab-8d9f6ae1b6e1 | -9.25318 | -46.7822 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adc51c4c-d7b7-3df8-9b0e-c6a5416e9336 | -9.85155 | -60.27801 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58bbe883-3bd5-34f0-8882-6ed04c7587af | -7.78981 | -44.5139 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27781ab4-062d-311a-b9cc-aba1fab8479a | -11.1096 | -49.8646 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d96bcf8-284e-391a-b813-380e46aa1e19 | -5.76288 | -43.98122 | 2025-10-05 05:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5edd7f1f-4bc8-39b9-8273-1fb39c61dab8 | -10.94403 | -47.06053 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4bb6896-a7cc-341b-959c-ed0e73f0a289 | -10.84728 | -47.19476 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README122.md)
