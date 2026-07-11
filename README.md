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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc3ea62a-8577-311d-b0a1-12747d133d56 | -14.123 | -58.3806 | 2026-07-11 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 95685261-65b5-311e-b4ed-6a21dfd5a3af | -13.3737 | -54.3572 | 2026-07-11 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| efa419ea-fe39-39f6-9a5b-8ec8c3ad88f8 | -10.3822 | -49.5849 | 2026-07-11 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 7529802a-bb14-3e91-97fd-861d9ac027c0 | -11.893 | -47.6545 | 2026-07-11 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 58d9a411-32a6-39a6-941d-395526745c04 | -12.8359 | -44.3422 | 2026-07-11 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 03b91a51-2c2e-3ea2-9245-c80c3893d68f | -13.3929 | -54.3551 | 2026-07-11 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 9cd3b122-9c93-3728-bda5-296ec1e9107a | -14.1233 | -58.3606 | 2026-07-11 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 7d14c39f-873b-3522-b3a6-210bd22deca4 | -4.3402 | -47.7645 | 2026-07-11 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 180.0 |
| ccec27f4-d916-35eb-99ee-62a8e829c43f | -6.4973 | -42.2142 | 2026-07-11 00:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| da74aafb-6cdf-3030-bc13-41cd7ce3bb59 | -12.8548 | -44.3625 | 2026-07-11 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 81a35749-e920-311d-952a-d4f33e8661ef | -14.1041 | -58.3623 | 2026-07-11 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 7e7a5b2e-23c0-34a6-99ce-a5d43ab934d4 | -12.8354 | -44.3657 | 2026-07-11 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 609482a5-be75-329a-8693-7a47dea3fb38 | -12.8548 | -44.3625 | 2026-07-11 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 9935b698-6f37-322d-9786-75ee8f16f66e | -4.3588 | -47.7636 | 2026-07-11 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 2806af45-1d54-354e-9a9c-1a8bac0c6dc4 | -12.8552 | -44.3389 | 2026-07-11 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 7f4567fe-24f7-3efe-a47f-7e488c47cfaa | -12.8359 | -44.3422 | 2026-07-11 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c8c412fc-1859-3965-9431-c0883c62a5bb | -6.4973 | -42.2142 | 2026-07-11 00:10:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| bbcde351-c34e-39e1-acce-ae61782dcd90 | -13.3929 | -54.3551 | 2026-07-11 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 8559e466-aa68-3f6c-9762-1ab1dfb91ce6 | -12.8363 | -44.3186 | 2026-07-11 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b04573c9-3f08-3875-891f-93da11198fc8 | -12.8165 | -44.3454 | 2026-07-11 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 605897d5-b761-3ad4-8373-4e1b2e299ec8 | -10.3822 | -49.5849 | 2026-07-11 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 30c4d658-7068-354f-b1ff-7c0dfe1e87cd | -4.3402 | -47.7645 | 2026-07-11 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| e8042c8b-732d-37f4-b476-8ce508c153e4 | -14.1039 | -58.3823 | 2026-07-11 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c957d8f3-2abc-3cca-9afd-e42d13c14809 | -11.8739 | -47.657 | 2026-07-11 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d5606554-f052-3c59-968e-cdfd448a6295 | -12.8165 | -44.3454 | 2026-07-11 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 1396f59d-fbd8-342a-be71-296ff89866d5 | -12.8363 | -44.3186 | 2026-07-11 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| fed4d2f1-ec3d-38bc-b62d-9654eafbd913 | -13.3929 | -54.3551 | 2026-07-11 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5306c3c2-5830-328b-82c5-ddad3d04d800 | -11.8739 | -47.657 | 2026-07-11 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a68050e6-604d-3bab-a68a-81166393d4eb | -4.3402 | -47.7645 | 2026-07-11 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 7085a791-a4f9-32c6-a048-8d5e30e2c642 | -4.3588 | -47.7636 | 2026-07-11 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 21f3eab0-ad4f-328d-ba41-2021d3841be4 | -12.8548 | -44.3625 | 2026-07-11 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 83998f36-6965-38b3-ad63-d52e04ab6037 | -10.3822 | -49.5849 | 2026-07-11 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 9d41fcd5-4efa-36a4-a6f4-b8bf8daddf53 | -12.817 | -44.3218 | 2026-07-11 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 312b8cad-605b-3a1f-b655-f1e7904dc5b5 | -12.8359 | -44.3422 | 2026-07-11 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f0bf404d-1f11-33dd-9cad-a91950168077 | -14.0847 | -58.3841 | 2026-07-11 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| cd1bdf7a-2bb0-307d-a2c0-0ad139e8df05 | -12.8548 | -44.3625 | 2026-07-11 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 953ffef7-07d5-376b-bec6-5b322070845d | -4.3588 | -47.7636 | 2026-07-11 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 62e2f224-ac2a-3f8e-9b48-3c4f23bf1aae | -10.3822 | -49.5849 | 2026-07-11 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a77836c7-6668-3108-b827-e07200003ea3 | -12.8359 | -44.3422 | 2026-07-11 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 51a6613f-5909-3ef8-bc78-98c8d38a5362 | -12.8363 | -44.3186 | 2026-07-11 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8fb95386-5cc5-34c9-a858-23266d16528e | -12.817 | -44.3218 | 2026-07-11 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 9ca6c3b6-f2c1-31d7-b71e-43d3fa50ae63 | -12.8165 | -44.3454 | 2026-07-11 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| c4978746-547c-35e5-8b53-fa3c8ceb43ba | -4.3402 | -47.7645 | 2026-07-11 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 1b5f8cd9-bcca-3c1c-a8eb-62ec6ad9d611 | -12.8363 | -44.3186 | 2026-07-11 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 60230878-f716-386e-9004-759bc77d70ef | -14.1041 | -58.3623 | 2026-07-11 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9ee06501-db22-3351-8536-090c5784f6fc | -14.0847 | -58.3841 | 2026-07-11 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 3e48cf93-f43a-3513-b770-ab0b7ec0cc1b | -10.3822 | -49.5849 | 2026-07-11 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| d4328f64-3070-3416-9373-deed9a271cf1 | -12.8548 | -44.3625 | 2026-07-11 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c8ab2760-cb2a-3d71-9bbe-bf7d72095800 | -4.3588 | -47.7636 | 2026-07-11 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b925104e-f6f6-3ab6-a5ee-24455a942ca5 | -4.3402 | -47.7645 | 2026-07-11 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 22ebb920-c38d-339b-8d6e-292ac8346ce5 | -12.8359 | -44.3422 | 2026-07-11 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 118154d4-cfaf-3950-b103-aca62fd3be33 | -14.085 | -58.3641 | 2026-07-11 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 2525f1a0-2c43-3c3f-8e09-2c52a3688529 | -14.0847 | -58.3841 | 2026-07-11 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| f26db772-af9b-3554-8d53-44dd286d2f07 | -12.8359 | -44.3422 | 2026-07-11 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| a8e8bae6-d8e2-3f9b-9109-5f24a2a65870 | -12.8363 | -44.3186 | 2026-07-11 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 6f8cf178-d125-3c46-9b2a-00f66c7f389e | -4.3402 | -47.7645 | 2026-07-11 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| f7af7a4b-e560-3724-bbe9-5fac771d85dc | -14.0658 | -58.3658 | 2026-07-11 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 3cdc18bb-53d1-3148-bd45-a82180a7951a | -12.8548 | -44.3625 | 2026-07-11 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 73e05b2e-c6ac-3bf6-a02b-1d3c69c7d2f7 | -10.3822 | -49.5849 | 2026-07-11 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 45311082-8a52-3444-9bad-2ebf55e91926 | -14.085 | -58.3641 | 2026-07-11 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8924762c-3aaa-3bd1-ad9e-424a871dfd3f | -14.09236 | -58.3688 | 2026-07-11 00:56:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8fd02198-8454-3672-bc96-7f71ba3f30a9 | -13.37892 | -54.34771 | 2026-07-11 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 6f926661-ba53-30d3-a62a-e00346d475bf | -13.36605 | -54.35007 | 2026-07-11 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d2bd1ceb-ee6d-3ae9-9d35-1c719badb9f0 | -20.27035 | -57.69114 | 2026-07-11 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| e2872af5-48cb-393b-b336-c53101c501f4 | -18.03262 | -54.36853 | 2026-07-11 00:56:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8f105aed-ca28-30d1-a442-f629cce7e0d1 | -14.07337 | -58.37191 | 2026-07-11 00:56:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 8d0aab6e-b421-357e-96d0-04bf457c66bc | -14.08286 | -58.37036 | 2026-07-11 00:56:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bd1f56b1-f8da-33d0-99bd-2c246d983340 | -13.38072 | -54.36258 | 2026-07-11 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 8a5d69f5-72d3-3bf1-b94d-0116cda54145 | -13.38221 | -54.36799 | 2026-07-11 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| e19a3a21-6bca-3ced-8b08-f94f1c7fecee | -14.07494 | -58.38254 | 2026-07-11 00:56:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| cd1cc427-1726-307b-9c3f-cbb0186a8b4c | -13.37728 | -54.34237 | 2026-07-11 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 762915cc-2d82-3702-8ab7-4fcd296a60fc | -21.10251 | -57.46588 | 2026-07-11 00:56:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4c3d7d3c-b7cc-39a9-8d01-edd19432de05 | -13.39178 | -54.34536 | 2026-07-11 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ccf19d2d-e98a-3085-bf72-7b9bb6dd3210 | -13.39508 | -54.36581 | 2026-07-11 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f5fc10e7-504d-3cd1-aaa8-c16c0a731f64 | -13.39359 | -54.36036 | 2026-07-11 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 38e7681f-62b9-3ec4-92e2-ac9f59c52a6b | -13.39015 | -54.34007 | 2026-07-11 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| fdddbcf8-07b3-34f7-b2c6-c76946149153 | -10.97517 | -58.68148 | 2026-07-11 00:58:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6831b3f4-d1ae-3710-911f-7c89fabcf5f6 | -12.85645 | -58.31323 | 2026-07-11 00:58:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 001838eb-f608-3910-bf33-991975f518f9 | -12.08119 | -57.13116 | 2026-07-11 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cf783db1-7303-3eae-ba29-8c070185ae05 | -20.8725 | -43.0863 | 2026-07-11 01:00:00 | GOES-19 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.0 |
| 75fc3ac8-d5b9-3b15-80e2-8d51d2c98088 | -10.3822 | -49.5849 | 2026-07-11 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7eb785b0-6cfc-3fdf-813f-5438f4cf42be | -13.3929 | -54.3551 | 2026-07-11 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e34d95e0-f7b5-336d-b136-44fa0f20c386 | -12.8363 | -44.3186 | 2026-07-11 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 483c26aa-22a2-371f-8e8c-ce1662b1ad62 | -12.8165 | -44.3454 | 2026-07-11 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 6161dfdb-7869-31ab-bda4-752a8d8920da | -4.3402 | -47.7645 | 2026-07-11 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c06d337b-3152-3e91-8aa9-5d877945d696 | -12.8548 | -44.3625 | 2026-07-11 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 18fed28d-9daf-37df-91c0-25aa235e8774 | -20.8717 | -43.1116 | 2026-07-11 01:00:00 | GOES-19 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.4 |
| 1defdf1d-c236-3b1e-bc82-6ed7c7118474 | -4.3588 | -47.7636 | 2026-07-11 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e29d22d6-6c49-3cce-9dfe-acad1cdd1694 | -12.8359 | -44.3422 | 2026-07-11 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 9a768c2c-777a-37c8-a76c-38b465166171 | -1.88118 | -54.6756 | 2026-07-11 01:02:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| cb1e6297-573d-3d3a-9ac0-6350bcca2254 | -1.87041 | -54.68268 | 2026-07-11 01:02:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 01208379-0c0b-3d00-a708-758dc9222a02 | -13.3785 | -54.3312 | 2026-07-11 01:04:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45ecca82-8219-39a1-8ced-2605b3ea7878 | -22.924801 | -49.182598 | 2026-07-11 01:04:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 09b50e7a-1f06-305e-a601-c8e5a4091bf5 | -12.0857 | -57.1245 | 2026-07-11 01:04:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ccd1a1d-d21a-3814-a93f-168129dd881d | -22.2355 | -56.675301 | 2026-07-11 01:04:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f70be969-68ea-304c-9715-80dae996fe9f | -22.915199 | -49.185799 | 2026-07-11 01:04:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3b9b9971-37a4-313b-85fc-6482d18999e7 | -13.3823 | -54.345901 | 2026-07-11 01:04:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7692bcd8-d81b-390b-b61f-01a08beb384e | -4.2061 | -56.0341 | 2026-07-11 01:04:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef5af994-f4d5-35b7-ab8e-d86ac3057ff5 | -13.3688 | -54.333801 | 2026-07-11 01:04:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcacd11f-c5b2-3798-b850-c4f6207bbc14 | -4.2023 | -56.0182 | 2026-07-11 01:04:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
