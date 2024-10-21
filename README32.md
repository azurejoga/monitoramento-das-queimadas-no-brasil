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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b23fb676-8b95-33af-a612-2449f39acc88 | -6.92237 | -46.83916 | 2024-10-21 04:14:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 892326c0-cdc1-3858-8d3c-b1fb9a2350a6 | -6.8337 | -49.14004 | 2024-10-21 04:14:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6185e914-9179-3f18-a58d-a117d37f9d18 | -6.83108 | -49.13726 | 2024-10-21 04:14:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 650dd744-e71a-3aa9-a259-f2564ec6e778 | -6.82937 | -49.13934 | 2024-10-21 04:14:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04acb68f-750f-32ad-b9be-61ae4130d6e9 | -6.49065 | -49.81585 | 2024-10-21 04:14:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d07bebe6-d0ca-31dc-ace7-584cbe5ebb18 | -11.87226 | -56.88215 | 2024-10-21 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29a299e9-4085-351a-ae48-2dd483ece606 | -11.87001 | -56.88168 | 2024-10-21 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01c3d975-bce2-39dd-bed1-5356f22b2943 | -11.8669 | -56.87494 | 2024-10-21 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 027332d8-6b23-3b19-8315-d1f71ba6440a | -11.86578 | -56.88052 | 2024-10-21 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27765e84-cc90-3957-9837-bafae2350076 | -11.86469 | -56.87454 | 2024-10-21 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c06ae11e-9fde-3b2d-9777-bfc0feaac8e5 | -11.86353 | -56.88008 | 2024-10-21 04:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99e647ab-b526-3066-aead-e63af725e759 | -1.2018 | -53.6366 | 2024-10-21 04:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 3f7ec617-b49a-36e3-ae96-4fa89e246811 | -1.1835 | -53.6166 | 2024-10-21 04:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| a01e0bfd-592d-3ea5-bee6-5ac7d1f8105c | -1.1834 | -53.6368 | 2024-10-21 04:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 5c56b770-20b6-3365-8de0-acf31bcb8060 | -2.905 | -45.2143 | 2024-10-21 04:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b03c9d74-a3c0-3231-8a61-25c24d6bd3c7 | -2.8069 | -51.3613 | 2024-10-21 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 22ac8bdb-02e6-365f-84a6-4c09b887ab4f | -2.7773 | -49.3067 | 2024-10-21 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 680696a9-7c44-3621-8e80-f5c5450fbb2e | -3.0037 | -53.038 | 2024-10-21 04:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 0102cddc-932f-3e9b-803d-866904351827 | -3.2147 | -50.7884 | 2024-10-21 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 5c489907-2552-3461-8f9f-58d7bf7c31ad | -3.2146 | -50.8093 | 2024-10-21 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1e3d391e-c558-374e-9c2e-8d2725e2f654 | -3.1138 | -53.1163 | 2024-10-21 04:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 12b5ffd2-344f-3324-89f9-a91da56ed4ca | -5.6894 | -46.435 | 2024-10-21 04:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d4c46aa6-723d-3c40-af8d-8c0a4b0ceaa6 | -12.5357 | -63.0319 | 2024-10-21 04:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |
| e553c68d-450e-30e1-90f0-6b331c37b858 | -12.5336 | -63.3003 | 2024-10-21 04:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 28.5 |
| db6ad1cf-746a-3dda-aa43-0fc6a4e7e61e | -12.5147 | -63.3014 | 2024-10-21 04:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 2f3098d6-9068-3bc5-b025-14974a9087eb | -18.2828 | -56.0994 | 2024-10-21 04:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 01d31c0d-07f8-330c-91b7-c9c54678f2f6 | -19.56059 | -56.62226 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 12039c64-36e7-35c2-9e09-e48b5b28c2ce | -19.55831 | -56.62039 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c23d4e86-02f9-3cb7-822f-f41ebd57f815 | -19.55743 | -56.62434 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e425e999-3611-3c34-8acf-610b05121da5 | -19.55503 | -56.62087 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 09f65d18-7cab-3cc6-8584-5c5ce96f2024 | -19.55479 | -56.63619 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 07d00e88-16ae-3c70-92db-41db9b0262ad | -19.5539 | -56.64015 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c6bbf510-d763-3cb1-95b7-02c1ba4e5a78 | -19.55274 | -56.61902 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 508d8886-1729-3e47-ba2e-68463774a632 | -19.55161 | -56.6367 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3d08a215-f4c5-3300-ba27-1a89d6c69576 | -19.55075 | -56.64067 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3e9b6d54-1a5a-3be3-bc12-ab33cb2133c1 | -19.54989 | -56.64464 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6bcbd460-98a3-37a6-8b63-26717fd06a95 | -19.54946 | -56.61948 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9cf4fe82-061d-35c2-9faf-b1ee9c6d1069 | -19.54904 | -56.64861 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3cd3a9c4-4c5c-3005-adbf-303c4b8ac071 | -19.54818 | -56.65258 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e2bb9689-37cd-3aea-a096-2fe19c6fcf04 | -19.54745 | -56.64273 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9f1d4d0d-51da-3fd8-8a46-db0d11749d88 | -19.54656 | -56.64669 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7467152a-5f28-38a7-b507-2130a6f587d5 | -19.54568 | -56.65066 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 54824f4e-d480-33db-ad43-df27ee3751fa | -19.54432 | -56.64324 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e1e180bc-68ae-3fee-af51-2aac79b3077c | -19.54389 | -56.61808 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c8807fbc-d7cb-3c9a-9029-c693af1d7fe6 | -19.54346 | -56.64721 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fbdd8ae5-8e0f-3c47-960a-734079223526 | -19.54218 | -56.626 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 97dc695a-1308-3e0b-87a8-d52fad1695d3 | -19.54132 | -56.62996 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fc3c94a9-e584-3a20-b7d7-9f83e8be43b2 | -19.54046 | -56.63391 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e657ef60-f142-3335-bdf5-5609a4c41cab | -19.53875 | -56.64185 | 2024-10-21 04:17:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fc5a6773-61a2-3e02-a9ce-ad3b93452a51 | -18.29875 | -56.17125 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f89ea1fe-bff0-396a-94b4-874efd6cd503 | -18.29791 | -56.17516 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 231e677f-e9d8-3637-b480-438d8dbad8cd | -18.29708 | -56.17906 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| f1de9b3c-b5cd-34b8-bd82-e1b2204e1332 | -18.29571 | -56.15826 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9fc351e1-f94d-37bf-b538-fcaddabe6deb | -18.29487 | -56.16216 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 82033a32-3d60-310d-b171-4d089592132a | -18.29403 | -56.16605 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5ab3d5d7-6204-3938-882d-723bf368ca67 | -18.2932 | -56.16994 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f9af05c0-2c3f-3d53-9c5a-31ab5715d436 | -18.29235 | -56.17384 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a0beb07b-7b52-3599-a6b4-3a9b8ef66c7a | -18.291 | -56.15303 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 93b11bc7-2ff3-3187-9d6a-f0014533a5de | -18.29016 | -56.15693 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 70a532e6-c6fc-3b94-8b1d-657e6793ba6b | -18.28932 | -56.16082 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| da335c08-41be-32ab-a73e-d96840f4787f | -18.28848 | -56.16472 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 26336641-3de1-389f-8fe9-37b83309a510 | -18.28256 | -56.09587 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f5e6b28f-e4db-3d42-9ef6-beaf7fbf34d8 | -18.28175 | -56.09972 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| ee4ef3e6-08ee-389f-a680-f7087b977362 | -18.28057 | -56.09357 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| ff206844-e777-3d91-90e2-9e9590e43f42 | -18.27973 | -56.09743 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 40a6de88-8b33-3a02-92d9-0f5e31e34867 | -18.27889 | -56.10128 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 046b87bd-b760-3d56-86e7-3f4cb92e9005 | -18.27805 | -56.10514 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 9a0803bf-8f11-3d44-88aa-177efd120f9f | -18.27784 | -56.09068 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ce6e0331-d8a5-38b8-87fe-c5bebfd58f49 | -18.27703 | -56.09453 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f8927cdd-c236-36ef-9ee1-cae099a860ed | -18.27622 | -56.09839 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| e8487bbd-1c6e-3dad-8801-5578a568df9d | -18.27587 | -56.08844 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b75c4c19-386b-3ae0-9002-1f4412da6605 | -18.27541 | -56.10225 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 294e713b-561b-3859-a3d8-1b7554a5ef6d | -18.27503 | -56.09228 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 20afc758-c084-32ec-821e-c14374ba4390 | -18.2746 | -56.10613 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 507e2db3-5e40-39c4-a3f6-da00f2397293 | -18.27419 | -56.09613 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 5a46ad49-049e-30f5-aac0-37a6e8c0ba7f | -18.27335 | -56.09999 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 6aae35cf-d919-361a-831a-5d1ef4ac8943 | -18.27251 | -56.10386 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 28b7b284-133d-31d4-a5f1-5a0cc587bf61 | -18.2723 | -56.08938 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 06cf6dbf-1605-34f3-86b1-8ad0a5197f61 | -18.27149 | -56.09323 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 13ed3737-6b30-3273-bc28-3021e5581a22 | -18.27117 | -56.08327 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 24d51c61-68a8-3350-b9a0-003c7ac89b47 | -18.27068 | -56.0971 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8bf901a1-b0be-3521-89e4-3016723c9016 | -18.26949 | -56.09098 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8fb89c57-978e-30b3-8298-26aea35acca1 | -18.26865 | -56.09484 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 13a585c0-cdca-3396-9842-f099a3bd451e | -18.26759 | -56.08418 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 703772ce-5f9a-327e-be67-af951c830b4c | -18.26677 | -56.08804 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cffd2bfe-081f-338e-948d-d35a9e808f44 | -18.2648 | -56.08581 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 04efad16-e658-3d01-a291-8bc7bfcea823 | -18.26397 | -56.08966 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5ef592af-4ff5-3ac0-af24-90c23dbfd163 | -18.26125 | -56.0867 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 81ecbe07-d0d3-3897-a630-ade088720495 | -18.05068 | -57.33614 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6c327f72-4b3d-33ed-a58a-190eef7d87d5 | -18.04965 | -57.34081 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c36772c9-bbb2-3c70-96ef-b2b50c6f7446 | -18.02003 | -57.30396 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 14795e00-421e-3047-a934-df59454690d9 | -18.01956 | -57.3027 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ca95425b-2cc2-369c-a334-ffa3dd99725a | -18.019 | -57.30859 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b11a3329-e3fd-3587-9d00-780bf9b7d545 | -18.01855 | -57.30735 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e430bf41-45a5-37bd-8750-44edd3160f59 | -18.01754 | -57.312 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4e181fa6-263b-310d-befd-1d605e823103 | -18.01406 | -57.30249 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c323b440-97b2-3af1-97e4-6c13060859e5 | -18.01359 | -57.3012 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3a311130-391c-3583-91f5-8fe058b243fa | -18.01302 | -57.30714 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6b0e5ed3-7665-38a4-8e52-a95cd81421c3 | -18.01258 | -57.30586 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 308f0abc-f5ba-3b5e-9c15-68ab8917cf3f | -18.01157 | -57.31052 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README33.md)
