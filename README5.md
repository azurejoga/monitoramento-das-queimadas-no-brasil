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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79c2b228-2b97-38ce-a7ef-953771b8f04d | -10.32162 | -53.58062 | 2026-05-21 04:06:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 971ce62c-0737-31ed-95a8-b9ce66b7b300 | -10.4888 | -49.35859 | 2026-05-21 04:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5362766a-7840-38c1-8066-6b2df59f181a | -11.99763 | -45.14018 | 2026-05-21 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c035eff3-b100-30c4-8d56-2016aef19261 | -13.0289 | -49.94199 | 2026-05-21 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 023b7602-e35e-3174-b2ac-cea1b79bfd1d | -19.76652 | -54.06624 | 2026-05-21 04:08:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbd072a9-941d-3646-b3ad-b799d65560bf | -19.78304 | -45.39606 | 2026-05-21 04:08:00 | NPP-375D | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e942f1ee-1d2f-3fd7-a804-dd070624768a | -19.76406 | -54.07682 | 2026-05-21 04:08:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 219c2e99-749a-3196-9c1b-33f900a813e5 | -19.96708 | -44.71796 | 2026-05-21 04:08:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8042d3b6-477d-35d8-9953-0613a79618b2 | -19.7726 | -54.06827 | 2026-05-21 04:08:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 738a4afb-4866-318e-9221-8bbac9ba6273 | -20.76536 | -48.56672 | 2026-05-21 04:08:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c97c1f3-6265-3237-8dc6-782e2d5911de | -19.76531 | -54.07146 | 2026-05-21 04:08:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ddd429b-b739-3ac8-b143-d000c8d90544 | -19.78388 | -45.39146 | 2026-05-21 04:08:00 | NPP-375D | MOEMA | MINAS GERAIS | Brasil | 3142403 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1a69da3-c4cb-3896-9fcc-4e5b4c014e8b | -20.76969 | -48.56778 | 2026-05-21 04:08:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf1504cf-1925-34bf-9aaf-ddefa24a9e9d | -16.89698 | -46.78522 | 2026-05-21 04:08:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62820917-5a8d-3aa5-a800-0f993ced43aa | -20.90255 | -42.65248 | 2026-05-21 04:08:00 | NPP-375D | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 08859666-abc7-3a2d-80fc-32fffdfeb113 | -19.77138 | -54.07355 | 2026-05-21 04:08:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa503c79-99b9-35b9-8b75-4c36e1e2b43a | -18.49696 | -40.01345 | 2026-05-21 04:08:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a02b4692-04a3-3b04-8a4f-445592293f80 | -19.77014 | -54.07891 | 2026-05-21 04:08:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a211a97-d48b-3055-bf75-603a2c3aacfb | -9.3045 | -45.4809 | 2026-05-21 04:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| bda82125-b36f-3dde-af8d-6e36384eb0de | -27.6109 | -49.94293 | 2026-05-21 04:10:00 | NPP-375D | OTACÍLIO COSTA | SANTA CATARINA | Brasil | 4211751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e6a5f81d-117f-33b1-bb5d-721f0deb6db4 | -28.51121 | -55.22779 | 2026-05-21 04:10:00 | NPP-375D | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| b7b00767-a8da-3dca-83ba-6b15e7d6794e | -31.85354 | -51.76639 | 2026-05-21 04:12:00 | NPP-375D | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 04ab1de5-ed4f-3f64-8374-a21e85f3c2d0 | -9.3045 | -45.4809 | 2026-05-21 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b310e2ca-69db-3be5-a357-74fbc1039e6b | -5.3455 | -42.68966 | 2026-05-21 04:21:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a1cf862e-0e5f-3d32-841c-8681443e4c62 | -8.1113 | -44.14938 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17c321e7-277a-3b95-9cfd-19469c0f7bbf | -4.47684 | -37.81499 | 2026-05-21 04:21:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 431d328f-2481-3ddc-851d-8da0e0a557f2 | -3.61408 | -41.81903 | 2026-05-21 04:21:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 73d92b4a-c35a-3bc1-90ca-e10621955658 | -6.7527 | -45.01313 | 2026-05-21 04:21:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ec08b6c-ada8-37ab-91ca-3ed69efd6dbb | -8.10907 | -44.14181 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e61e629-022a-3da3-9cfd-4083521c4958 | -7.01839 | -45.4157 | 2026-05-21 04:21:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46a0259f-fbe2-3f0f-8a91-13e6ace4917f | -7.05428 | -45.06135 | 2026-05-21 04:21:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8634dde5-8a31-3e65-8768-60df1d0312a5 | -7.73133 | -47.2409 | 2026-05-21 04:21:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc2979ef-5183-3b70-a8f8-bfcf2f3efc21 | -8.11021 | -44.15642 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 036c2d90-7077-3395-94a1-e7234b7f9781 | -4.47619 | -37.81931 | 2026-05-21 04:21:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ee59a47f-d5a2-3ced-bb51-a7a88f3469b3 | -7.92869 | -48.28621 | 2026-05-21 04:21:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 810b7e5f-4b0a-3365-986a-24bdb6eadeac | -8.118 | -44.17207 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0527315e-4a30-3556-8b51-727598813921 | -7.01067 | -44.99399 | 2026-05-21 04:21:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9ee501e-384c-3c4a-8f8f-248c615aae82 | -6.29769 | -43.63511 | 2026-05-21 04:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0507ecb1-a93a-301d-97dc-7f4b6c4e23fb | -5.75282 | -43.40577 | 2026-05-21 04:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f764147e-f2ce-381d-8d8c-7870c18c133e | -1.50331 | -47.46833 | 2026-05-21 04:21:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fb388c3-390f-33af-89bb-4a639d02eb1d | -6.38986 | -44.17189 | 2026-05-21 04:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a84f942-d80d-34ba-97ae-736cc6dd8ed7 | -5.30537 | -43.05673 | 2026-05-21 04:21:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| deb0a055-91d8-3369-8048-c252d82d6f79 | -6.30103 | -43.63563 | 2026-05-21 04:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| beb0e27b-2f02-3630-932f-b461a64042a8 | -4.65865 | -42.42145 | 2026-05-21 04:21:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eaa45d0c-799b-3b84-aa7e-aaf4faafbe1c | -5.94996 | -43.49088 | 2026-05-21 04:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2acd9400-9700-3402-8bc8-9f3efff732b9 | -6.39041 | -44.16842 | 2026-05-21 04:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6c3f5333-2df9-3703-a2ed-856ac87ab67b | -7.82634 | -42.06003 | 2026-05-21 04:21:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60a4183a-3c86-3ddb-a619-1e8525726218 | -7.92505 | -48.28563 | 2026-05-21 04:21:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa77cbe6-04ca-3028-8bd7-bf7940b256e1 | -5.9533 | -43.49141 | 2026-05-21 04:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f071e5de-725b-38e5-8d52-522381e106cf | -7.05042 | -45.06429 | 2026-05-21 04:21:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0891d938-16db-3129-b8a4-9d2b196abba3 | -7.01894 | -45.4122 | 2026-05-21 04:21:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fd9dee7-009d-3400-847e-73e0e42ac0f7 | -7.95016 | -46.08891 | 2026-05-21 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 212eb6a1-c432-3301-b54d-aeb49b6e42af | -6.39372 | -44.16894 | 2026-05-21 04:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 056b5162-2eb6-31a3-9bfb-9b2358f34486 | -3.61466 | -41.81527 | 2026-05-21 04:21:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4d25a2c8-bfc4-336f-81ab-8747d4c35e98 | -8.11467 | -44.17154 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 205f8b8c-5e25-3d4f-b7b4-f518fe0d2c10 | -4.4775 | -37.81068 | 2026-05-21 04:21:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3d528495-5460-3044-a5e5-16c522bda384 | -8.10405 | -44.13019 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45b66072-b831-3544-bfe5-a3aa4d4ed1f9 | -6.39426 | -44.16547 | 2026-05-21 04:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 15729926-3ef4-3c5d-bbb2-3a9635cc6248 | -7.05097 | -45.06082 | 2026-05-21 04:21:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf2f04ad-8db5-329a-bc74-0db26975eec0 | -8.11075 | -44.1529 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72b18be5-494c-3e3b-b2fd-ea11df1df106 | -6.75889 | -45.01802 | 2026-05-21 04:21:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39fa2e75-b281-3511-bcdc-7f5e94648918 | -8.10574 | -44.14129 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3709eca1-7699-381f-a368-90ad19e03598 | -8.11522 | -44.16802 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c275c211-051b-3370-900c-1daa40fb4c1d | -6.10929 | -44.74371 | 2026-05-21 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19efd611-86f2-37a1-a0ad-14bf2a51a000 | -8.10628 | -44.13777 | 2026-05-21 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73bdab34-bc41-3130-8d6a-24095576446a | -6.99563 | -50.46596 | 2026-05-21 04:21:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4596e264-1046-3e51-8e06-65c671fb4a0f | -6.29714 | -43.63863 | 2026-05-21 04:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa7adac0-07d2-3167-8243-7ef6f9a7d979 | -7.73417 | -47.24532 | 2026-05-21 04:21:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e80ce19c-9bf2-3c5c-be45-8b85170d6f7e | -4.36538 | -37.89642 | 2026-05-21 04:21:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9474184d-0b81-36c7-97b9-8dae6b34edbe | -7.94959 | -46.09244 | 2026-05-21 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62aa2c1e-6a1c-36b3-b3b2-988924daf72f | -6.11314 | -44.74078 | 2026-05-21 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5e59dd1-de42-31d8-a2a9-d372a07fb6ab | -7.82278 | -42.05949 | 2026-05-21 04:21:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4964be24-73ce-3ca6-8d43-ab68100c27e3 | -11.33503 | -48.00814 | 2026-05-21 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63911a28-eafe-3d43-aa51-8edde3cb07e5 | -10.63588 | -48.33147 | 2026-05-21 04:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e1f6bf9-bf70-3b58-aa33-4befc4e1f720 | -10.49283 | -49.36671 | 2026-05-21 04:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3675c8bb-a7a6-36b1-87a1-48cc196be7b6 | -8.60082 | -45.95083 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0083e32-353f-3a3c-8138-d20061170d71 | -8.60025 | -45.95436 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 219b47ce-0c57-379d-b43f-fb7f6f041beb | -15.06798 | -42.37656 | 2026-05-21 04:23:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f9cec542-7667-3755-ae5b-20333e0a875d | -13.41872 | -46.71504 | 2026-05-21 04:23:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd02ab5c-3cdd-3a0e-93da-1b2dc14b6cd6 | -10.44235 | -47.94913 | 2026-05-21 04:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b497fc96-b99b-3c52-b622-330a2559b5f8 | -10.39807 | -49.44861 | 2026-05-21 04:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bf01949-7f22-34d6-9f84-30ef498eba70 | -10.39432 | -49.44795 | 2026-05-21 04:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38227dbd-043d-3073-a31d-d8a748b116ce | -11.30465 | -54.71653 | 2026-05-21 04:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e0bf343-46f8-387a-80b9-3becb89adef9 | -10.65243 | -42.30231 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 92b560cf-f369-3116-adfa-9aeabeda8398 | -10.66479 | -49.70279 | 2026-05-21 04:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf83bd2a-bc6f-31fd-81d8-f95c01019027 | -10.66579 | -49.70074 | 2026-05-21 04:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 634493c0-8328-397c-99ab-38d8afeb1bc4 | -8.60415 | -45.95137 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a363a3-ac29-3769-95bb-e46852028c5f | -11.18626 | -55.91616 | 2026-05-21 04:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeddc4dd-6145-3226-8a8c-a0532a169c2e | -8.5513 | -45.98594 | 2026-05-21 04:23:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f9fd956c-0bd8-3877-b16b-caf09e36f9d2 | -9.30908 | -45.4948 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4e681907-64bd-3309-a2ae-626b39cdd194 | -9.2913 | -45.47732 | 2026-05-21 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c3478be-87ae-3734-9134-b183e35fbd33 | -11.67681 | -54.58219 | 2026-05-21 04:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38680ada-e4bf-3798-8ac3-3a9edaa99e9c | -12.6003 | -44.51631 | 2026-05-21 04:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fb6e2bc-ac39-3bcc-b0ef-67b2395f2b11 | -9.94897 | -52.45515 | 2026-05-21 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aabfed63-048a-3db6-851f-493b1afcc96f | -9.25081 | -47.73862 | 2026-05-21 04:23:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 616a83f2-568f-335e-bb4b-9843f06f5d57 | -12.39811 | -45.86967 | 2026-05-21 04:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf30622d-7171-33a9-8700-0270db44ff0a | -9.7151 | -50.41346 | 2026-05-21 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16743d22-fa7d-338e-abdc-04a4b60c23b8 | -12.81155 | -44.87115 | 2026-05-21 04:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b20e317d-f404-340a-bb52-49c93399f85a | -11.02189 | -42.86306 | 2026-05-21 04:23:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2457ee1a-c397-3fb2-af68-5f3d0c415930 | -10.64517 | -42.30122 | 2026-05-21 04:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
