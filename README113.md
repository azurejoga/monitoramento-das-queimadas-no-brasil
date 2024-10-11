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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 210a91a3-2582-320c-92e0-9221641d2eed | -17.70514 | -56.29747 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 44cb7a59-38f2-3f91-8e71-42856fa3e9b9 | -17.70502 | -56.30129 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5b5a8fec-e8ea-3461-aeea-5e28dfefdf8f | -17.70469 | -56.30223 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9ca259a4-2715-3966-a63b-1fee665fdfe2 | -17.70453 | -56.30604 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c2d2e0ac-0d74-3d67-82d9-90bbdfec5e7a | -17.70423 | -56.30699 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 45149f13-faba-3ecc-a503-6abf11f47a83 | -17.70404 | -56.31078 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| fe3837b1-5277-3ca9-aaff-17dd6700c44d | -17.70378 | -56.31173 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| b9b3a393-0b36-39f0-942f-4968d16824ff | -17.69892 | -56.30061 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 65b5dc18-648c-30ef-810d-81e281bfd9bc | -17.69859 | -56.30153 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3360ba5d-2123-3c65-a840-b8fdbe2b3466 | -17.69843 | -56.30537 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| da641cac-eb64-3853-bcd6-3cdf4590a6ef | -17.69813 | -56.3063 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2d687d5d-3731-31df-afd2-8edb5baaf2f1 | -17.69795 | -56.3101 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e3735df2-c3a4-3d70-a62a-007bf71ee223 | -17.69768 | -56.31104 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 63048c55-6409-3e98-86f3-df7fe2a56be4 | -17.69746 | -56.31485 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| fbfc0222-517a-3bed-9a56-aa490390dc55 | -17.69722 | -56.31579 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5b86bf73-7c6a-3a34-84d9-30a9aeb8c86b | -17.69185 | -56.30943 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d7e8f100-664b-3a76-9316-e4c609be831f | -17.69158 | -56.31035 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fded9ef8-02d8-3d63-854f-cf7dc3d28560 | -17.69136 | -56.31417 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7b443b3b-76a1-3feb-aa88-2760c3d16f61 | -17.69113 | -56.3151 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 0ff40caa-6f85-3f41-915c-7b69452738ae | -17.69088 | -56.31893 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 811af390-9202-3d94-81c0-0e66dfb8a8df | -17.69067 | -56.31986 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 79233b51-fc1c-302b-8785-e2132647798f | -17.6904 | -56.32365 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 1acd7082-a78f-3a28-aed3-318da570db4b | -17.69022 | -56.32459 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 356870c8-437b-3493-aa97-e6e6ac8e47ce | -17.68527 | -56.31349 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 397b4f8f-1d41-34cc-9fc9-4ef5bf24d5a7 | -17.68503 | -56.3144 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 74125e2e-0285-3432-8c2d-a76b3f0d79e7 | -17.68479 | -56.31824 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| dd93f14a-dde9-37b8-ab9b-5bbd79c70cc1 | -17.68458 | -56.31915 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a8113a17-00fa-3c25-8c69-d6c393bdf4d8 | -17.6843 | -56.32298 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 6f995edf-86fd-3cfb-a49c-af9c0df60918 | -17.68413 | -56.32388 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| f88abe5d-8957-3f40-ab4f-92544250c80a | -17.68382 | -56.3277 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e8a81032-c0e7-3cd5-87d1-3fb7bfc778f7 | -17.67918 | -56.3128 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5c2382ba-a124-363c-a45f-09d3e86ec859 | -17.67894 | -56.31368 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 17a2d5bc-8636-3118-96c0-b13f93f70f2a | -17.6787 | -56.31754 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0417ab70-90e2-3826-82c7-1f0733703490 | -17.67849 | -56.31843 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3ba1d6c9-14ec-3f18-915a-15475c343f24 | -17.67822 | -56.32228 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c7922f92-fe92-32fa-af70-727e23d2fa80 | -17.67356 | -56.30739 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 537bd747-68ce-36da-ac3e-1022da5e81fb | -17.67308 | -56.31212 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 924e0541-b0ca-31d5-b5d0-86350ca3387f | -17.6726 | -56.31686 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4c56b316-7c40-39dc-ace4-d7dc3108f83d | -17.67212 | -56.32158 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c2dcb722-2c41-3c56-b901-a80d8cc234c0 | -17.65946 | -56.325 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7a2845f8-cd1e-3673-a1e2-02e7aeb23a1a | -17.65899 | -56.32973 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1a18ddef-2d72-33ac-933d-692583ee5daf | -17.65338 | -56.32433 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| bdf37aa8-0787-379e-90cd-82fe384f6d29 | -17.6529 | -56.32905 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 18f81f19-dc5e-372d-882a-e7fbb366335d | -17.6487 | -56.30943 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4e3565a2-073e-3e30-8158-4c844390ff82 | -17.64823 | -56.31417 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9a3672d8-a95f-3ab7-8b57-18a0363fb854 | -17.64776 | -56.31893 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 45e040d5-98d0-37c5-a64f-702e98c80aa0 | -17.64728 | -56.32366 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4b03c1c7-9266-3003-8c43-e5a403147993 | -17.64681 | -56.32838 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 282cb6c8-e375-3445-b137-db39b8d1dbd0 | -17.64261 | -56.30873 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9c2367b0-1c9e-3764-9aeb-a9fa6b48856b | -17.64214 | -56.31348 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3a15e1d6-6523-37c1-b3ee-ff8d4cff92a0 | -18.20357 | -56.45359 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 30b6d449-1ddb-3876-b6a9-976d172b58ee | -18.20312 | -56.45832 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3376f432-3d66-3d67-badb-85d87795fccd | -18.20268 | -56.46303 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 83a8a0b0-ac61-3cf6-8578-540f3aeb6786 | -18.20238 | -56.45512 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| f6a14b1d-f607-3427-99ad-4b18855c92a0 | -18.20191 | -56.45983 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| c58176a0-9a4d-32fa-8b9e-a22769028361 | -18.20144 | -56.46453 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e85ddf71-cf9e-3413-a1a9-152c4385ba9e | -18.19793 | -56.44819 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6e4e4187-2131-33a5-b76d-3b3f78b69d8c | -18.19749 | -56.45292 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 04f1bc29-e00c-3afc-b239-ffb6fc83960e | -18.19705 | -56.45763 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 934f55cb-7090-3b34-88a6-1edca8d2d1a7 | -18.19661 | -56.46235 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 8c1e04d7-f873-37d7-bea8-ab4a8d11e106 | -18.19631 | -56.45447 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| cc0d2b94-c2ad-39ca-9ce4-ee64ed64eb03 | -18.19584 | -56.45916 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 6f3a4a2e-505f-3939-bebd-bdb5a65fcb8e | -18.19536 | -56.46386 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 77ea6b3b-0ec6-32cc-b960-03649b67a9b7 | -18.19185 | -56.44751 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1203d3ba-f9c3-3bcd-bf64-816d17a841c6 | -18.19141 | -56.45223 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| b883c9bf-73f6-344c-ac80-7afe2b2b54e7 | -18.19097 | -56.45695 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| b090f963-784b-3cbc-8dbf-3e74f8499c17 | -18.1907 | -56.44909 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2b1f256b-d3af-3b58-b115-7b13e92e842f | -18.19053 | -56.46166 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| be981409-013d-3dfb-8d77-9b441e110d39 | -18.19023 | -56.45379 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 93e76d56-abb3-3eb2-a7a9-6b6971fba670 | -18.18976 | -56.45849 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 324bc5c1-7b93-381a-8758-035f484db43f | -18.18929 | -56.4632 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 928ea723-bf86-3e05-8494-13784fbf6bfb | -18.18509 | -56.4437 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 09bbd061-d354-3418-8281-d893c36eb7ce | -18.18462 | -56.44841 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 31169c7e-7fa0-3472-81c4-17ed74a2b1de | -18.18415 | -56.45312 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2019b947-0ba8-3426-b3ac-b89bc9087702 | -18.18369 | -56.45783 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 344995b9-4783-323e-a107-cc1c09bc7dea | -18.17901 | -56.44301 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| cb514d55-7c85-30f4-8585-e78abc5ea650 | -18.17855 | -56.44772 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| e58763c2-8206-30c6-84d8-6635eee6bbb2 | -18.1734 | -56.43763 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| b712b3b2-4ef0-3897-8946-fbf08b6c3e71 | -18.17293 | -56.44234 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 50fa7d83-4970-3920-a095-03e6d3df63f9 | -18.17247 | -56.44706 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 490b296d-5d83-3c7b-a33a-9de5da3ba5b8 | -18.172 | -56.45179 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 405e4b57-9dbd-3f46-a793-920d2e466ecb | -18.16732 | -56.43697 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 76ec4265-afb5-31d1-bb8c-8d19aaa007cf | -18.16685 | -56.44169 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2993cc23-740b-3617-9d30-ed20993c6192 | -18.16639 | -56.44641 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 75be59fc-17dc-3d6f-bd83-98fde0438f12 | -18.16592 | -56.45113 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 69be5df8-738c-31df-8a0c-5bb3e026cf12 | -15.86683 | -57.4696 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3473f2c-3cd7-32eb-a80f-f03471e963fe | -17.16615 | -57.47531 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 78cc141c-4d3c-3167-8964-209bd07f9870 | -17.16381 | -57.47292 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a8f24800-72c9-3ee8-b9cc-986d994184b3 | -17.16338 | -57.47681 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1e089dbd-5a97-3a41-91c8-95b0333310ff | -17.16052 | -57.47464 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a19c2541-934d-3df1-80b6-8b10838dbca4 | -16.99767 | -57.44772 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c85d92cf-9081-3b99-9cfd-5828e4a97e05 | -16.99725 | -57.4516 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6fb063c7-463f-3a71-899c-cce168f344ee | -16.996 | -57.46326 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d5e265e7-7fcb-3c82-b0e5-092934508e6d | -16.99558 | -57.46714 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 12434ab5-b637-390b-8baa-595664a9df27 | -16.98955 | -57.47033 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1fb70880-8818-3f1c-8853-04a0b5f102eb | -16.97556 | -57.44113 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cc27d3ec-52b6-3cd9-be0a-5ca16e2a2d94 | -16.97515 | -57.44501 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 96278534-cbb7-333e-b4d1-8c0bfc5fa134 | -16.96993 | -57.44043 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 24480a58-c4ab-3492-b94a-3706bbaf52d2 | -16.96952 | -57.44432 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2cb89b9d-4e70-39cb-b5f9-eba65d1b51d6 | -16.96512 | -57.43198 | 2024-10-11 05:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README114.md)
