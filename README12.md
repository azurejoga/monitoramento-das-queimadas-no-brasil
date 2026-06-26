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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc4e1275-97f4-3b3c-8fac-63075ff743f6 | -9.47798 | -57.31793 | 2026-06-26 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9069ca09-65d9-3e24-bec8-2cc622266eb2 | -6.50139 | -42.22548 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f72ffcfa-0dfb-3851-8c58-a3fc1cc47f7a | -12.74151 | -44.48473 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16a92aad-8389-392c-b811-d226b66b6897 | -11.19589 | -43.35135 | 2026-06-26 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0a9e20ac-3417-3dc9-9c3d-d7fc3e2cbb70 | -6.507 | -42.22396 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a48a0aaa-ef89-3d9c-8f60-e3988313b12c | -11.42195 | -54.43789 | 2026-06-26 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 899cfbf0-0e35-3466-8c48-d90b8c7c1a8a | -11.21107 | -54.33309 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a973c1fd-890a-393c-96b5-5e810c70dd72 | -11.3891 | -47.81414 | 2026-06-26 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d48fb576-3985-30e4-9aa4-b69ab373644b | -8.69052 | -49.09158 | 2026-06-26 04:51:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b4e90b1-406e-3fcd-986a-11f18826747a | -8.01516 | -49.64207 | 2026-06-26 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0886a31-bf48-3bb3-a75e-c776efd13850 | -10.10199 | -49.5872 | 2026-06-26 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac3e41ab-fb97-3e72-8e84-de4b8d514738 | -6.98614 | -42.89705 | 2026-06-26 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 53833f32-acf7-3c47-a74e-462b06b67348 | -10.39841 | -56.7626 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c78c1508-022c-351f-ad0e-dd8eddf67fb4 | -6.50214 | -42.2203 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 735da273-eaeb-3fcb-b1df-d94ecc5d0c74 | -8.85532 | -46.92605 | 2026-06-26 04:51:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dcd5edb-a4d9-34b3-8569-cc2b2a719399 | -10.93847 | -56.85307 | 2026-06-26 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744cdf71-8a5e-3dcd-95cb-fe75b42982ce | -6.50258 | -42.21712 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7147e926-4e89-3f14-a2ef-d66a7ddd4166 | -10.16235 | -56.61317 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ead0f8d7-f8c2-3413-8c20-0b6837af8ab9 | -10.15971 | -56.62827 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2df61a2f-cc80-370b-bcee-b3726a7e7245 | -12.43684 | -49.5801 | 2026-06-26 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1072d2c7-e1b4-38fe-8030-de838543b0b7 | -9.66096 | -50.70852 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2178931b-fd9c-381b-9241-8348e6332102 | -6.98107 | -42.89642 | 2026-06-26 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3f1ce118-252f-3f36-8946-949d5fcdad09 | -8.22984 | -47.12548 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79fe3b64-b679-3aa6-859d-2973937dd6cd | -11.41162 | -54.43613 | 2026-06-26 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24dd4526-5f84-38bf-8b63-5830de423b00 | -10.75434 | -49.11391 | 2026-06-26 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85cdaeca-72d6-314c-8deb-7afa5d85c73d | -11.48099 | -47.34367 | 2026-06-26 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19fb6bbc-d993-3025-9498-95f3e30178de | -10.09851 | -49.58667 | 2026-06-26 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e2dce68-b890-3625-b77b-a75358b4327b | -8.68992 | -49.0955 | 2026-06-26 04:51:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a161fbc7-5b04-3518-9e45-32a6e833e232 | -12.74643 | -44.48538 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce155ccb-f083-3615-8625-4e7bd4152682 | -12.35889 | -47.42561 | 2026-06-26 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 371ab715-ecb9-36e4-92b6-ab0a2acf3fa7 | -6.30193 | -44.65064 | 2026-06-26 04:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 885cb23a-06ae-3331-ad3d-c0ac49a6b2b6 | -9.49038 | -57.32011 | 2026-06-26 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbd9993d-88d3-38ed-b80f-16f0a8b25b3b | -11.21325 | -54.34128 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1064265a-738b-3ab4-b0db-db0e6aa62bbf | -10.36031 | -47.34312 | 2026-06-26 04:51:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecb4cf33-02c5-38a5-990f-0a761a981d7f | -11.77357 | -46.4387 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec848d88-f457-31fd-8f38-10f4fac41a01 | -12.75655 | -44.49794 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f172a83-e268-38ef-9e5b-75217a571898 | -8.23513 | -47.11647 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5fe802a-f6ff-31fa-b10f-908c31f54a93 | -10.38676 | -56.7129 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f22fd27f-904d-3009-a3e9-96e371757ad0 | -9.18636 | -45.32277 | 2026-06-26 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e2046f8-eef0-3c1e-94db-5da5acd403d9 | -11.51225 | -56.13071 | 2026-06-26 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b62d5cc0-48ec-3107-b9ab-3590840f354c | -10.10604 | -49.58386 | 2026-06-26 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2faf24d-793f-34d9-ab5b-f28e8e3d5b01 | -10.76743 | -54.10843 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7054e4bd-719c-3908-9ad4-0be68b24f949 | -10.35959 | -47.34816 | 2026-06-26 04:51:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0c543b4-e5cf-3e16-9391-36a5d0535a64 | -11.21451 | -54.33367 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7635895d-3645-347f-9c09-26421068294a | -9.80447 | -48.91812 | 2026-06-26 04:51:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 565a4ca7-c57b-3f20-8a1b-bef8b1607b01 | -12.7481 | -44.48539 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f04539a8-273c-3a51-a96e-1f9fb07fd821 | -10.93456 | -56.8523 | 2026-06-26 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6666039e-7a1b-3f89-8c5c-c35ae20888f9 | -7.75304 | -44.61823 | 2026-06-26 04:51:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 05b3fb7c-2c47-3733-ae86-9d817e3288b8 | -11.36478 | -52.95645 | 2026-06-26 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e313fe80-54b9-38db-b2d7-c61030813878 | -9.76482 | -48.25333 | 2026-06-26 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b7bad788-86ee-3515-a2c7-084a9bff2023 | -12.4473 | -44.75365 | 2026-06-26 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19e6461b-1936-384c-8143-816b36738fe2 | -8.01801 | -49.64633 | 2026-06-26 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a32af39-ec25-3ff1-b221-c4bd7254915d | -6.50301 | -42.21393 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0601bec7-fee7-314d-be1e-d79814a271df | -9.39758 | -50.67449 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53c50afd-8bbd-3261-b534-4da367900bbf | -9.8009 | -48.91758 | 2026-06-26 04:51:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9bb09a8-d821-3933-99a4-f57306f84d0b | -11.87101 | -51.73351 | 2026-06-26 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d6c75b0-e9ce-3610-b925-1758edf1a416 | -11.77249 | -46.44657 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf143388-624d-3bc2-9f35-b041e0e2c4a2 | -9.13083 | -47.64462 | 2026-06-26 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8ccffbc-1a6a-3ca1-b25b-e129cb54df60 | -10.38498 | -56.72318 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea77a396-2f1d-3879-8bfe-28504e5db914 | -12.86768 | -44.3386 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2db8a127-db5e-3a81-a847-945832d41f7f | -10.38285 | -56.71216 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a8d2a88-5c2b-34b3-9301-358de2ee511b | -10.12703 | -52.11004 | 2026-06-26 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53685446-5d35-3428-8d27-9eaced7968c3 | -12.35487 | -47.42505 | 2026-06-26 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5db2d85-f394-3f4c-841c-a06dfc2b36c4 | -8.13161 | -47.88902 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f4c8639-ff15-37e6-b21e-427903898734 | -6.307 | -44.64689 | 2026-06-26 04:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f85d48a5-1c38-3f13-a6dc-9b3352ab0905 | -6.99204 | -42.89177 | 2026-06-26 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b92785bd-3afd-32c1-8e09-b4ad8bb574b1 | -8.89593 | -47.9994 | 2026-06-26 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af4cd5d4-fd32-3bf2-bd0b-6d5f1b6ae23f | -8.23123 | -47.11606 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c72d6d4-40eb-37d9-aefd-7f632f3fded1 | -9.8922 | -57.39825 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1eb89ca-f5ee-3078-ae44-bc0fc1b8ebc3 | -9.12703 | -47.64405 | 2026-06-26 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f0fe4eb-6da2-33d7-b898-cbcaef87c22f | -9.66151 | -50.70493 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d4b35bf-c3d4-342d-8e02-b32bfda716e8 | -9.36725 | -50.54508 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 81f36164-3f5b-35af-bbc3-c9898e16df36 | -8.22734 | -47.11558 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1e73114-a2c2-339f-a40f-5e6c033143c1 | -8.2582 | -46.22046 | 2026-06-26 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e8f339ef-9eca-3aea-a030-d0cb011181a0 | -8.43821 | -51.5534 | 2026-06-26 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 497ddedf-ae1d-3e62-be98-e2de0387a1ba | -10.38196 | -56.71726 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35008f09-be62-373c-bf8f-c513b89c465b | -11.87156 | -51.72997 | 2026-06-26 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 036bce9c-f509-3cb4-b4c1-fcb90d29e19c | -7.91455 | -48.24083 | 2026-06-26 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1bb91e3-0579-33a8-a64f-fc4f0488982c | -13.23187 | -47.64862 | 2026-06-26 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a93b2453-d2a3-3522-8915-f317ad3d2794 | -6.30131 | -44.65493 | 2026-06-26 04:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c6c54c5-0a12-3ebe-a685-9b5dd744d02c | -7.73754 | -44.1761 | 2026-06-26 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91cf8261-a16d-357b-be81-ce6c921e0b5f | -12.51793 | -48.28532 | 2026-06-26 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fbdc633-b82a-34b7-aa16-e9b34ac9ec4a | -12.76147 | -44.4986 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c5c51c9-5437-3397-a2c4-a4537257b42e | -12.51618 | -48.27037 | 2026-06-26 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e09146a-9448-3a86-83ab-ae7950e56726 | -12.441 | -49.57655 | 2026-06-26 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c0f547c-b3ac-3e0c-85b6-5078e2b753bd | -8.44428 | -51.55793 | 2026-06-26 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d7d943-8a9f-365f-95e9-8a5d48d8128f | -11.51379 | -56.12163 | 2026-06-26 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fadb9e8c-61fd-342e-a28f-c2eafb90ccec | -8.49286 | -44.74596 | 2026-06-26 04:51:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbc05caf-5957-3280-83cd-b693dbd5dcf8 | -10.36352 | -47.3487 | 2026-06-26 04:51:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d023a306-7618-3d39-9011-6a7a529c39f7 | -10.01776 | -59.35153 | 2026-06-26 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5522d8fd-71db-373e-8c05-7072c9625fa6 | -9.7356 | -47.89471 | 2026-06-26 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 319ad499-9bd8-3d1d-a529-5dd39cd5ff2f | -12.44395 | -49.58122 | 2026-06-26 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d8e4adf-132c-34a7-9410-7b93a4f6235c | -9.19077 | -45.32339 | 2026-06-26 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb821acb-c8c3-323f-897d-e38e429b1779 | -11.77194 | -46.45055 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a1b6e73-34a7-383d-9b9e-2eaff8c4af7a | -7.57334 | -45.87964 | 2026-06-26 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eda698b-5fb4-3d2e-8cf1-77e79315cd6c | -7.73682 | -44.18106 | 2026-06-26 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2af9b71-5cf2-309f-bb67-23c2169b9368 | -10.12428 | -52.10602 | 2026-06-26 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 630244cd-c408-31e8-bb01-fbc691ac3ef7 | -9.60536 | -56.92551 | 2026-06-26 04:51:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50c132cf-144f-3172-967f-f2782eeadd4c | -9.8938 | -57.40166 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f73f4325-0e83-320a-acd2-d97191c42a2a | -6.50803 | -42.21669 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
