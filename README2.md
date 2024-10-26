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
| 2163147d-905a-30f2-ae82-dd97e0224f86 | -3.613 | -44.9598 | 2024-10-26 00:15:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 404.6 |
| 04d8be3e-1ce0-3d59-8909-4e63672b4121 | -3.8982 | -41.0154 | 2024-10-26 00:15:27 | GOES-16 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 59.4 |
| de627375-a00f-33a6-9864-2b3b280d98cf | -4.4842 | -42.91 | 2024-10-26 00:15:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 0210c34a-1ce8-3b14-82e1-d503567cd8bb | -4.5613 | -48.0358 | 2024-10-26 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 35796965-7cd7-323a-ab13-382144ad2fe2 | -4.5614 | -48.0141 | 2024-10-26 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e6a54faf-3221-3ab6-8b7b-21ed070f9dc1 | -4.5799 | -48.0349 | 2024-10-26 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 229.7 |
| 8d197a3b-f4f8-3b22-8617-2b596261a319 | -4.58 | -48.0132 | 2024-10-26 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 283.3 |
| 3633920d-4975-305f-aa64-16e08b401de2 | -4.9108 | -45.8598 | 2024-10-26 00:15:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 5043a4fb-bd9e-317e-a20a-83a1a2b972e3 | -5.7014 | -45.0199 | 2024-10-26 00:15:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 73bbd01a-46ba-3d89-b2f3-96dc207198a7 | -7.6474 | -63.4584 | 2024-10-26 00:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 05597b03-a585-3e86-bbb6-b515391c5aba | -7.6475 | -63.4396 | 2024-10-26 00:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 2a9de826-f628-3aa9-98d0-480c2becd1cc | -7.9046 | -63.7129 | 2024-10-26 00:15:51 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ffa46d61-d3fe-3649-acd1-fc38f9baa563 | -7.923 | -63.7123 | 2024-10-26 00:15:51 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| dda15e96-110d-3a2f-97b9-c2e4bfc2cf00 | -8.8177 | -49.695 | 2024-10-26 00:15:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 621e0dfd-b833-3736-a379-e208f2d5d723 | -9.6075 | -42.9134 | 2024-10-26 00:15:59 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 51.4 |
| 300d25e3-b66f-36db-8b7a-ed36b1e0602d | -9.4996 | -47.8068 | 2024-10-26 00:15:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| ab56b4e5-5a21-3513-9b99-c4249c5b9259 | -9.6156 | -47.5962 | 2024-10-26 00:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 903c7103-c9ad-3da4-943b-e3bbfff19a33 | -9.6343 | -47.6163 | 2024-10-26 00:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| efbb8358-c414-3bd6-8897-2a6757218b64 | -9.6346 | -47.5942 | 2024-10-26 00:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 233.4 |
| c81e34ab-b2e4-3307-a9e3-a7a8326ceaf5 | -9.6349 | -47.5721 | 2024-10-26 00:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 11240b6a-7d94-31b6-9f71-2b3a5c260ef2 | -9.6535 | -47.5922 | 2024-10-26 00:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| c38f310c-26f7-358c-9b68-1112569ed77d | -11.5225 | -45.8369 | 2024-10-26 00:16:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 5ca08a86-d240-31b9-bfe5-41496b6131e1 | -11.5228 | -45.814 | 2024-10-26 00:16:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a021dded-9e1f-390d-afb0-ece4c7a2c376 | -12.0083 | -44.3579 | 2024-10-26 00:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ec30c0ec-70a7-35af-a340-c1749ee3e8cc | -12.0012 | -63.9013 | 2024-10-26 00:16:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c97b2f7d-21de-39a0-8022-d9efe67d9eac | -12.4591 | -63.1704 | 2024-10-26 00:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 95c29946-efbe-304e-8e3e-a2a9f25c0729 | -12.4593 | -63.1512 | 2024-10-26 00:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b2708305-fbb3-3fb1-9212-4dee79380c52 | -15.78 | -55.7129 | 2024-10-26 00:16:34 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 8344ac8c-e4c5-315c-ac54-acf3fdf6ee12 | -16.9012 | -57.5108 | 2024-10-26 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| de7c68df-141e-34d7-ad28-f3c75037ece6 | -16.9204 | -57.5291 | 2024-10-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.2 |
| 190fe1c5-7048-3eb2-9e51-d236cde9dc66 | -16.9207 | -57.5086 | 2024-10-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| 62820e26-6ffa-3916-a3df-214f80cc2964 | -17.0499 | -53.452 | 2024-10-26 00:16:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a8b3006f-3d8e-38fa-ac4a-63e6b3d02fcb | -17.0583 | -57.4722 | 2024-10-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| e38ba06b-bb76-3c5a-a7c0-ff5eaaa3fca3 | -17.0789 | -57.4085 | 2024-10-26 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 193eca82-e79f-3651-a8d0-f9f066be50e6 | -17.254 | -57.4903 | 2024-10-26 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.2 |
| 4a29c0fa-72f1-38ed-a787-50c9d0683448 | -17.2576 | -57.2644 | 2024-10-26 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 449d5801-5ece-36ea-878b-06cd8d57adcb | -17.6667 | -57.4822 | 2024-10-26 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| ede3c946-a3db-300d-af60-5b7e44a58163 | -17.6865 | -57.4798 | 2024-10-26 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.9 |
| 48c7c41d-5567-3a58-bf57-ae995d0129ea | -17.7062 | -57.4774 | 2024-10-26 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 9683dd33-2844-3ceb-abe9-40e8e921eca2 | -17.7671 | -57.3673 | 2024-10-26 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 1b0b6b2e-f42b-3494-8110-fa7ecdf93b63 | -17.7674 | -57.3467 | 2024-10-26 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| b3eb23c9-1594-3bb2-a47e-f846809679d3 | -17.7868 | -57.3649 | 2024-10-26 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 186.9 |
| 1385022e-5181-3c3f-82da-b29de13e5fb0 | -17.7872 | -57.3443 | 2024-10-26 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.1 |
| 90f407a9-12b4-3833-8dfd-6b4dfe89faf3 | -17.8066 | -57.3625 | 2024-10-26 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 0e10fe8d-4801-3f94-94c6-f2099f8913e3 | -17.8069 | -57.3419 | 2024-10-26 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 85fa6d68-9302-3fcb-b8bc-d7994e1107f7 | -18.1417 | -57.3829 | 2024-10-26 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| ace115f2-cde9-349c-a026-1bf8df74382b | -18.1421 | -57.3622 | 2024-10-26 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| d485cfb1-5285-328a-96e7-23bd2ae6f55b | -19.6233 | -56.8758 | 2024-10-26 00:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 77587fc8-1d43-3961-83e0-7408d6a6aeb7 | -19.6434 | -56.873 | 2024-10-26 00:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| ed20fe0f-f81a-3822-b40c-997933035d48 | -2.1929 | -53.7436 | 2024-10-26 00:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 7d07451c-4f4a-3eb2-b97b-e2149727ab55 | -2.1929 | -53.7234 | 2024-10-26 00:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| decd9805-654c-38da-a8f1-00d6b2f48cc5 | -2.3709 | -66.4527 | 2024-10-26 00:25:19 | GOES-16 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 234489df-a205-3057-a348-927d1e21f243 | -2.6949 | -51.7979 | 2024-10-26 00:25:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ff3dcd32-4ffe-3349-9c47-5668e6be33bc | -2.8739 | -53.3252 | 2024-10-26 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8a5be821-0cd7-30a9-b571-94b844504d8a | -2.874 | -53.3049 | 2024-10-26 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| fc4158c8-43ac-37b5-99c6-fe1c9114c0c7 | -2.8923 | -53.3247 | 2024-10-26 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 4645952b-9b37-3816-9d54-3a9b1c12a8bf | -2.8924 | -53.3045 | 2024-10-26 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 3202203c-c34c-3f28-8535-5b66e1e10fbf | -2.9501 | -52.5708 | 2024-10-26 00:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 6d7ea9c9-9d10-3abb-992c-25cb0597763c | -2.9944 | -50.5025 | 2024-10-26 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 64536b8c-c1a5-3f76-be41-0b0eb4f7bb86 | -2.9945 | -50.4816 | 2024-10-26 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 285.4 |
| 5f26ac63-2715-3515-a907-3ce4984b202a | -3.0129 | -50.502 | 2024-10-26 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| f77ea0e5-dced-3441-a202-45f61a130bc5 | -3.013 | -50.481 | 2024-10-26 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 312.6 |
| 456f8a5a-36f7-3f5b-b11c-d51d8a843089 | -3.013 | -50.4601 | 2024-10-26 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1319ac86-f30c-37c4-86f7-c462bc4f6e65 | -3.0314 | -50.4805 | 2024-10-26 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ee325ead-33af-3423-af73-bf046dc5a00f | -3.0932 | -53.7239 | 2024-10-26 00:25:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| abbe99ea-5c01-3362-adaf-451b0d44ae30 | -3.1116 | -53.7234 | 2024-10-26 00:25:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 3bf32f65-d6d6-3e6f-aa7c-66e1da9269c8 | -3.2368 | -45.8077 | 2024-10-26 00:25:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| d54dc4a7-65f5-3043-97bf-8ce7c87626fe | -3.2553 | -45.807 | 2024-10-26 00:25:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 95.0 |
| d7b20300-e939-3721-bd5f-314ebd145bef | -3.4729 | -43.3377 | 2024-10-26 00:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 23189dfe-ed8b-3820-b9d1-fb9baf02142d | -3.473 | -43.3144 | 2024-10-26 00:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| b8e6f43d-96be-3c1f-b8a4-567936dabe7c | -3.4915 | -43.3368 | 2024-10-26 00:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| aea36dd3-887b-3725-b4c9-152e8a1c772e | -3.4917 | -43.3136 | 2024-10-26 00:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 5a56f885-c8ef-3a2c-9528-ec7cb2beba3c | -3.5943 | -44.9833 | 2024-10-26 00:25:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 217.6 |
| af5d8fbe-c8a0-3427-8e12-e5d489263a91 | -3.5944 | -44.9606 | 2024-10-26 00:25:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 288.0 |
| 442cc394-0b70-374f-9f0b-2e7a1e92aa01 | -3.6129 | -44.9824 | 2024-10-26 00:25:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 192.6 |
| 0d4b86b2-4c6d-3c1a-9653-40c2f682da2a | -3.613 | -44.9598 | 2024-10-26 00:25:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 256.0 |
| d8069253-ab36-3cd4-87e2-043783cd4be0 | -4.4842 | -42.91 | 2024-10-26 00:25:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2c01b8d2-7b7c-3308-bfc4-c0a1a79da51e | -4.5613 | -48.0358 | 2024-10-26 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| fbb41c53-d606-3c12-ab4f-8a4828a9790a | -4.5614 | -48.0141 | 2024-10-26 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| c05946f3-19ff-3ee6-91fc-c44d1b9c58aa | -4.5799 | -48.0349 | 2024-10-26 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 673e1a18-bec8-342a-a92c-631a65dddfcb | -4.58 | -48.0132 | 2024-10-26 00:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 201.4 |
| b8f4b9ff-7d8a-384a-b617-05d9b246ce95 | -7.6474 | -63.4584 | 2024-10-26 00:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1fa7fdf5-d976-3497-9906-deb618d67772 | -9.4996 | -47.8068 | 2024-10-26 00:25:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 8592709b-0ae8-3956-a341-f90b3a3ada05 | -9.6346 | -47.5942 | 2024-10-26 00:26:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 73d0ee39-fa2f-35a7-b9d9-a984295b2732 | -11.1671 | -56.2939 | 2024-10-26 00:26:09 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6746faf3-40bf-3793-8b04-9b4816434433 | -11.5037 | -45.8167 | 2024-10-26 00:26:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a25eaa2c-25cf-3c22-b4bd-16737d56d32a | -11.5225 | -45.8369 | 2024-10-26 00:26:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 482bec79-509c-330c-9509-ddcf234845fa | -11.5228 | -45.814 | 2024-10-26 00:26:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 3788ffc8-a0f3-3db8-89a4-926f98b8c19f | -12.0012 | -63.9013 | 2024-10-26 00:26:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4817afab-2c1e-3299-b639-de599311034c | -12.4591 | -63.1704 | 2024-10-26 00:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a86fff56-c185-37c0-a2dc-e916a7fdfb32 | -16.9012 | -57.5108 | 2024-10-26 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 047780af-eb24-3c7e-b643-4cf5b8def1da | -17.4214 | -39.9614 | 2024-10-26 00:26:41 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 82.5 |
| 8ed57134-557d-3364-9deb-9281c543c02f | -16.9789 | -57.5428 | 2024-10-26 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.0 |
| 0ac6a8fb-366d-31ee-bc99-df508d20d01c | -17.0499 | -53.452 | 2024-10-26 00:26:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c780604f-0a47-38c9-85f1-39ac3aecbc89 | -17.0593 | -57.4107 | 2024-10-26 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| e0789cc9-cc77-3220-86f3-70f3e8a04051 | -17.0789 | -57.4085 | 2024-10-26 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 7e25a2f5-671c-3251-baa3-87be22dfb6b7 | -17.2344 | -57.4926 | 2024-10-26 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 4cfdf2b4-480d-3636-a9c0-cbf419ba2c7a | -17.2537 | -57.5108 | 2024-10-26 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 7ba05522-d8cb-3bc8-b419-66a0bf6cf807 | -17.254 | -57.4903 | 2024-10-26 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| ecba7835-e55d-38ce-ba81-f709266da976 | -17.2576 | -57.2644 | 2024-10-26 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |


[Clique aqui para ver as próximas entradas](README3.md)
