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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84f727ce-3cd5-3844-bdb5-01ed648424de | -10.62786 | -53.89859 | 2026-08-16 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13203679-f74e-3fc4-9d5d-b9b70b6052db | -7.583 | -61.23669 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2b0ce90-1c34-3d98-8b6e-3b650fa09cf6 | -6.59675 | -59.1139 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56b23034-ad4d-351b-bfd5-cbfbef30f978 | -10.94096 | -57.11142 | 2026-08-16 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a758b9be-1e14-3607-bb0b-46f955c4c1a0 | -9.29493 | -56.81581 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df74363b-bb88-3b19-acf7-4c65a72acb38 | -6.11609 | -57.71482 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9b8e311-d9c7-3500-a6a9-677d0ee5a5ee | -6.37644 | -58.32243 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 709d8e08-a860-37aa-9ad9-8d4c03335701 | -6.86221 | -58.97316 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f66cca57-0f25-3ba4-acc1-e8fd7784c39f | -11.90488 | -45.97277 | 2026-08-16 05:16:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54133180-8168-33c8-afde-06c2ddf3a7e4 | -8.10534 | -51.65321 | 2026-08-16 05:16:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b52de14-d9a3-3d18-b272-8fdd3e0413dc | -6.10509 | -57.73965 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33e7c960-3e70-3d57-832a-cbb6df0b6aa3 | -8.60944 | -54.69518 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20f20ef0-df2c-3e84-9ab1-7ee22eb47ae5 | -7.41821 | -60.01674 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2b18f2e9-9966-3c21-8006-f6468ef9ea04 | -8.95386 | -60.5438 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1887c37-83d2-3e70-9524-bce38b71a337 | -8.43117 | -62.66727 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3e69aeeb-c37f-3865-bbe7-e4b97a444cb0 | -6.62005 | -59.06224 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7cffc54-f525-3a8b-bc74-1f7012d2c621 | -7.27793 | -44.71806 | 2026-08-16 05:16:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0f04d8a-9048-330a-bf35-7011b0394bf4 | -6.61938 | -59.06639 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69de9c0b-b85c-3644-a4eb-7c623f5ca17e | -6.71725 | -58.92902 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b309be00-c806-3f0e-bb7f-1622ff9cdd46 | -6.63155 | -59.05987 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36d4c267-bd4f-3693-8602-741266c1e7c9 | -8.26701 | -57.33826 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d277ab35-555d-32d6-826a-20ef8586e8e5 | -6.0619 | -57.70224 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cd38acc-507b-38fc-9ab9-a478f848d154 | -8.96849 | -60.50332 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d13f736b-1cb3-33df-92b4-4123fa8013e7 | -11.89937 | -45.96733 | 2026-08-16 05:16:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 491cd251-9065-3631-821e-be7bce962203 | -6.36945 | -58.32129 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f705fa6c-940f-389c-a256-112e79813779 | -8.64355 | -54.70057 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b045d28-37ba-3ea7-a529-8da5fb44d34b | -6.83478 | -56.41045 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed200dd0-c9f2-3316-b24c-50c5ce4c2fae | -6.85693 | -56.42112 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a41f669-2f77-342b-a0e6-1dee94d63b00 | -7.42343 | -60.0318 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 537c2519-bc82-3ee7-9af2-c4241601088e | -12.45932 | -46.64848 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7246754-861c-3524-9cd4-94d7b9d89163 | -6.62659 | -59.06758 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab9e85be-ee1f-3c6f-be6c-f2220b8af37c | -11.30211 | -54.8787 | 2026-08-16 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a6fe495-0552-34bf-862f-719fce7ae890 | -6.72016 | -58.9337 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a5e25389-19d5-3869-9ecc-4d3a9bb30c2d | -6.62366 | -59.06284 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab09b3a1-772e-3777-9438-f910b88d67d0 | -6.85505 | -58.97198 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cadc1db0-b52c-393a-8d2f-0492038e0a2c | -6.53861 | -55.17722 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf603e77-eddb-3470-8ba4-4c76902ab79d | -10.94041 | -57.11492 | 2026-08-16 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dffab7e-5b46-3646-bee6-05e3093c655a | -6.83977 | -56.44333 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63fc3d50-d826-3ef8-8358-e33af0427512 | -6.61157 | -59.0012 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 353f7053-afb6-3169-a32a-f70ceb5813a2 | -8.65397 | -54.72434 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e65d95da-728d-37f9-84cc-6cb9e8239cd6 | -9.5477 | -56.80313 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72a75054-0b2c-3c7a-a378-dbe528ae473a | -8.95277 | -60.59644 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83686977-7633-3164-ba52-6bf87f122fee | -9.54438 | -56.80259 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc470fa8-1c22-33ff-9d44-fc11af7f0321 | -8.60489 | -54.70201 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 379b5e26-6508-308c-9039-f259070dd371 | -6.25495 | -47.69633 | 2026-08-16 05:16:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d31b57a1-061b-31e8-a8ac-76a87813241a | -7.42497 | -60.02258 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5ca17df-284a-378a-99ea-7c443629a5c2 | -11.48706 | -54.61042 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7962ca0e-3571-32c9-8894-0f41d2c1c64f | -11.48239 | -54.61779 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32992530-eb71-3d20-8318-bbdd9cde0c8d | -6.85371 | -58.98018 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb158f9c-6631-3e2b-9f21-8b24b72365e5 | -3.23558 | -61.16929 | 2026-08-16 05:16:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6b98094-fb82-365d-aa80-590efe8a5107 | -8.4627 | -57.68166 | 2026-08-16 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c36bc822-1456-39f9-942d-50a10a7a2ddf | -8.66026 | -54.75172 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1839b82e-3ad4-3b54-8517-0e0f4b996188 | -6.8359 | -56.44627 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d5aa187-6247-324f-a69a-a35927b89c9d | -6.59495 | -58.99005 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fd069ff-5184-36de-9688-cafe79ce297d | -6.82815 | -56.45216 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 039a1c01-a673-3aa5-a38f-2dca74f6e3ba | -8.61057 | -54.71048 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e1bbf6-4427-3a19-b7bd-52ed457fd49e | -6.86025 | -56.42165 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae992ef7-1352-323f-bdce-3d3218357564 | -11.0663 | -47.25512 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70d8d311-c21a-3839-88d9-230191249b28 | -6.71658 | -58.93311 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2e16dc5c-317f-335e-b8d9-50bbcd239eec | -8.65168 | -54.71645 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b67af89-9aa7-3c53-9828-82ef0c9e4fd1 | -12.02504 | -46.44031 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 056346ba-73e3-374a-bae7-8eafdea56fa9 | -6.82427 | -56.45511 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb20d067-b0ef-3123-9a07-2bfcf02375a9 | -6.9682 | -59.30758 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a770bd9-0049-3485-a661-04cfea1a0987 | -6.61918 | -59.04494 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3116741b-7129-30d6-afcd-ddf9a3242ba9 | -11.33388 | -46.21166 | 2026-08-16 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6962e115-3d12-3be5-82a0-fdc47bd86966 | -8.96994 | -60.51782 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dcf614bc-6279-330e-bdf1-870a04415e19 | -6.3758 | -58.32631 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d45d5111-7539-3b9f-96cc-de67394926e0 | -7.46283 | -55.30755 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ed1d547-dd60-3b95-bede-00793466da3a | -8.96459 | -60.52644 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cd65d263-fd97-3ae7-baa3-782c1e8bc15a | -6.96446 | -59.28525 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b310207-3339-3c85-afa8-d2ddfae01c8c | -6.85527 | -56.43153 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b28d1c98-2971-38ff-b174-a5d8015fe3fe | -9.15828 | -60.92102 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b35a6aff-bcc8-3651-a908-aa2e45bee2c0 | -11.21425 | -54.8142 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a654fd98-14f8-3154-9c9f-511e30ab2e8d | -6.84309 | -56.44385 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03d5eba1-a175-3b8f-84de-3a0f7e0629f9 | -6.93257 | -43.63985 | 2026-08-16 05:16:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dce16587-3f31-3335-a5c0-7afac5c20472 | -11.08333 | -47.25435 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7be86d09-3697-309a-9257-4b19e4b9f44e | -6.63415 | -56.39581 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87399ac6-2e71-37c0-af58-8b4b27a9619f | -8.89874 | -60.59194 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c55ffd86-4872-3b79-a8ee-75a709bf0685 | -6.29359 | -47.74897 | 2026-08-16 05:16:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cc5d6b1-5c4a-35f4-9aac-1494d14c6d55 | -9.10956 | -46.38656 | 2026-08-16 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8477dbae-0313-3c07-b510-359804570fc7 | -11.2206 | -54.81913 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d738cc08-5d6f-3056-aec4-6885457eac03 | -6.43368 | -60.07684 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41f9ca64-894c-30a4-881f-132fb6ce015d | -11.48577 | -46.59163 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 17052250-ccb6-3d38-a4d8-e4986b89c879 | -9.10326 | -46.39021 | 2026-08-16 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61f246cf-f945-3914-aebf-47d4bb9cd2bf | -6.96164 | -59.30213 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 121887a4-927b-3ec4-88c5-cb7ed0e1618f | -9.48534 | -51.64648 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3adbedd0-c1b7-3651-ab17-0405c912f3ad | -7.58773 | -61.20833 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2979d958-8d14-3c89-affc-05b91e34ba64 | -8.61626 | -54.69626 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85e04362-ce34-3f5f-a651-8395e02bc1cd | -11.48529 | -46.59547 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f241724e-c915-301d-8b56-b667fa90a4cd | -8.61228 | -54.6994 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c18963b8-8339-3833-973e-d65004e6d2e3 | -6.62346 | -59.0414 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8757b846-caf0-3e6d-8ecb-545acaf57bf8 | -7.41069 | -60.01555 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38095455-2807-367e-84ad-30ab9ac2d2cb | -12.03021 | -46.44762 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 792e2ebe-dcc7-3157-8084-4cf9e138d863 | -9.20465 | -59.67593 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6d131d6-8e50-35c7-b305-cf3e6c0dd667 | -6.10628 | -57.73223 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 87e92d91-4e62-3b2b-b68f-9560ea130a64 | -6.62863 | -59.05509 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d7f2137-1d9b-3eec-8bc8-5f6013d49dad | -12.0307 | -46.4434 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ec8ffc5d-4418-3083-ba98-6f3b29a6c539 | -9.48233 | -51.63878 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f358d32-afb7-3dd5-986d-d57c434d7c3f | -9.35461 | -62.36942 | 2026-08-16 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3596aff6-3a2a-3119-b3d8-e40649cf0378 | -8.60034 | -54.68619 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README39.md)
