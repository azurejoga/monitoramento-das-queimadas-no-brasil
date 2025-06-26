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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53c7997b-6258-3f30-b2d9-2dcd8d653af8 | -22.67583 | -42.85163 | 2025-06-26 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d5b1a56a-e785-31c1-b9fe-d23141a7c7ff | -22.67546 | -42.85567 | 2025-06-26 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e3b24b5f-e95d-34db-9984-2435a03923f2 | -23.79335 | -53.36454 | 2025-06-26 04:44:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9415a913-37aa-32bf-af32-9fb393f5d99d | -23.40766 | -46.55688 | 2025-06-26 04:44:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d7f2589-98d9-33e7-88f3-07f0b7d5c7f6 | -21.02788 | -54.56114 | 2025-06-26 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a88f8697-b0e3-3dca-879c-4264494d0a4b | -23.63196 | -46.42793 | 2025-06-26 04:44:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bcbab5f3-82e1-3b21-a73f-9c3f245a7e6b | -25.19334 | -49.32623 | 2025-06-26 04:44:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 05c19f23-95e2-3f57-a027-4501a3a499e0 | -20.25567 | -46.73505 | 2025-06-26 04:44:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adedbb94-69eb-317a-b206-8b7fea2aaff8 | -20.50057 | -45.58489 | 2025-06-26 04:44:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3caacffe-f8ec-3855-9409-6fdfd1275b1a | -20.50538 | -45.5864 | 2025-06-26 04:44:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ffe427b-7002-3e59-a828-ac21083a2217 | -20.50515 | -45.58548 | 2025-06-26 04:44:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cbd8533-c86a-3ac2-8fc3-dfb3afc75d1f | -21.19135 | -48.69296 | 2025-06-26 04:44:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5cef2435-7bd4-3da7-9c89-4c7547d3c6a5 | -23.40599 | -46.55797 | 2025-06-26 04:44:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0118eff3-33a1-3959-b469-288695f80756 | -22.14518 | -43.04432 | 2025-06-26 04:44:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fd60ce09-4076-3029-a07d-2e57603d8cc2 | -20.15585 | -52.96365 | 2025-06-26 04:44:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ae4d702-1a33-3d12-a337-fd50a7ab6005 | -22.1455 | -43.04098 | 2025-06-26 04:44:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0f5b20c8-7022-3197-98c5-ee37523a79e5 | -21.19201 | -48.68797 | 2025-06-26 04:44:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 159e25e9-0e98-3219-9173-ceea7b55d1b8 | -23.79004 | -53.36394 | 2025-06-26 04:44:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aa869b0c-ce56-3a93-b8ef-178375a04f26 | -23.33831 | -46.77174 | 2025-06-26 04:44:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d8ac8dc0-ef0e-3178-8fd3-30a9a8c2d053 | -21.02452 | -54.5605 | 2025-06-26 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee6db6f6-51aa-3f27-b464-439260868a94 | -20.47833 | -53.67543 | 2025-06-26 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| babb82e5-20c3-3a8c-9319-a523d5dc5df6 | -20.95188 | -56.59101 | 2025-06-26 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2aef5481-90cc-3138-8c62-952b4045bc91 | -20.25616 | -46.73107 | 2025-06-26 04:44:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c802dfa-ad6a-3b9f-a0d4-c8104969bd7e | -9.121 | -49.4528 | 2025-06-26 04:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 4af3fc47-0b5c-3c8c-851f-5b3d77317d90 | -9.1213 | -49.4313 | 2025-06-26 04:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 0a30f234-5175-3da8-8745-b379780deb68 | -9.1213 | -49.4313 | 2025-06-26 05:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| d6ac7f3c-657e-3858-bf5c-47212c280de4 | -9.121 | -49.4528 | 2025-06-26 05:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 603e00e9-373f-3822-8f8c-f1a7beac72cf | -4.12921 | -43.06484 | 2025-06-26 05:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b86ce3a9-abf1-33e0-9fb8-9a826a31d0f8 | -4.12845 | -43.0703 | 2025-06-26 05:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a6ce519-0562-3644-aff8-5ba84c56964e | -3.98381 | -48.416 | 2025-06-26 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fa96932-54c2-3e48-b9e6-fe543a647947 | -2.75087 | -54.59307 | 2025-06-26 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d694528-c11b-396e-a73b-98f9d05cabd9 | -2.44634 | -47.49887 | 2025-06-26 05:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0421c38a-32fc-3ed3-b981-926bd9051c93 | -2.74526 | -58.1853 | 2025-06-26 05:04:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83a8d4f1-deef-3883-a17a-3f1cf97eb359 | -3.72033 | -53.75294 | 2025-06-26 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c220b42-8158-33f4-a9b2-84ebfed33508 | -4.52881 | -48.04613 | 2025-06-26 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13017cdd-49ce-309e-bfaa-5cc55df8ccf4 | -2.55224 | -47.70199 | 2025-06-26 05:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c7bc64b-1a9a-34fa-964b-969bbc98fecb | -4.1869 | -48.15231 | 2025-06-26 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3440e46-a374-3884-96a5-36d97a4b7ce0 | -3.59112 | -49.43449 | 2025-06-26 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7a28454-e9df-3f63-b566-c4be6c1b8f59 | -4.1876 | -48.14766 | 2025-06-26 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bd3d8f0-fabb-32d9-ab38-970fd85a4e8f | -2.53278 | -53.956 | 2025-06-26 05:04:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7154b7c6-ffce-3266-b268-b457b6115ab0 | -4.53484 | -48.00526 | 2025-06-26 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fd4e235-65f6-3a4f-99c9-c811668292c7 | -4.52333 | -48.05035 | 2025-06-26 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ceb2270-93a5-32d4-b913-ecde3fd34196 | -4.53012 | -48.00433 | 2025-06-26 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48c6392b-aa07-3b23-afe8-8c332d221a79 | -2.28921 | -48.56539 | 2025-06-26 05:04:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3b8d66d-6a6b-3312-8d66-66ac3c925ad7 | -3.98018 | -48.41401 | 2025-06-26 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db0bcec9-c9c4-3695-8f0b-09121e2f85fc | -3.97922 | -48.41534 | 2025-06-26 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1db163d2-87ef-3fba-88f9-198acef04c43 | -4.52406 | -48.04541 | 2025-06-26 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bce851e6-b738-3c7c-9450-762a5dd32284 | -4.27033 | -48.18172 | 2025-06-26 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7af64abc-62ce-35dd-a357-b2c70fab2c06 | -4.27501 | -48.1824 | 2025-06-26 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2ac23556-d4ae-3004-9025-976c550cfe99 | -2.44711 | -47.4938 | 2025-06-26 05:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ce31776-2011-3429-87e2-6de33aef2723 | -4.52808 | -48.05105 | 2025-06-26 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f01c189e-0d42-345c-ad77-b0c9d60212c3 | -8.84644 | -49.858 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc0a663b-6ad7-3690-9ff5-b75ffd0e0236 | -8.26045 | -47.02333 | 2025-06-26 05:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bc348bb-d784-3863-afd8-b3795cb61718 | -8.34195 | -49.23254 | 2025-06-26 05:06:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6cc9039-82c5-309e-bba1-1e5345b95f9e | -9.50409 | -56.09593 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e90121c-a1fc-3d72-ba1a-3cfc81da6233 | -8.05919 | -43.1068 | 2025-06-26 05:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9dc9e791-5023-313c-a32c-327738c522f1 | -9.78961 | -48.56376 | 2025-06-26 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40944e94-ce68-39bc-9ccd-c5b628c5144a | -9.78886 | -48.56936 | 2025-06-26 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01d09f7e-11ab-325f-9562-e34791214442 | -5.49195 | -42.1468 | 2025-06-26 05:06:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6d93ab4f-f08b-3f44-b456-ec7cf14ee6ca | -9.87615 | -48.44923 | 2025-06-26 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3a7b9cc-a150-3c3a-8d17-0b0055a508a0 | -6.37663 | -43.75073 | 2025-06-26 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 580105ee-33b4-3629-97d0-2b842492b507 | -5.87231 | -50.14912 | 2025-06-26 05:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 34932bfd-24a8-39ea-abe8-67c5bee66c5a | -9.33285 | -47.8303 | 2025-06-26 05:06:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27e4eeab-130a-39a9-b50b-ee3d4aa039de | -6.17585 | -48.07922 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1363582-6a44-3010-92d4-70f336fc37af | -10.51035 | -47.20096 | 2025-06-26 05:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa76a6b8-e363-381c-8cda-7546a10758e5 | -6.18144 | -48.07488 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9abfcfa8-52dd-300d-ab0a-353e9daba0dc | -8.84198 | -49.85731 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42534128-f63b-3aa6-9f5b-4707e6f51802 | -8.11162 | -54.86899 | 2025-06-26 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09150886-d78e-3e3a-b89b-20f6627705ee | -9.23775 | -49.30794 | 2025-06-26 05:06:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb208fe8-d66e-348a-b2d6-e2bf508d6c1d | -7.0932 | -49.16636 | 2025-06-26 05:06:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3027520-ca16-3c24-b270-753af0362c85 | -6.17824 | -48.08047 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 398dcdf8-f61e-3d4c-9423-f5533e43b196 | -9.12286 | -49.43814 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ba25e59-4b0b-3557-b083-ac5b8c60d1ab | -9.32808 | -47.82652 | 2025-06-26 05:06:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23b0ae5e-2d91-303c-a00c-c2972bd33e1f | -7.74886 | -47.60065 | 2025-06-26 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4b6fcb3c-13da-30ea-91a2-ce6ba75b3e8d | -9.50464 | -56.09242 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2842d116-58f7-3eee-80c2-400916178188 | -7.11061 | -47.84971 | 2025-06-26 05:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3e280d5-6008-331e-b01d-f9ae0eaf0778 | -7.10098 | -49.17683 | 2025-06-26 05:06:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 939b4ebd-d294-3242-bb30-d7299fc448e9 | -9.11428 | -49.43193 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4a78390c-8c83-3fa7-9bf8-dccf73f99df9 | -8.33666 | -49.23655 | 2025-06-26 05:06:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6572312-0812-3357-8a58-09cbbfb81496 | -7.74269 | -47.59633 | 2025-06-26 05:06:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adb88ce0-5a9d-329d-89da-b22eacac7f04 | -9.50687 | -56.09996 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb2c9acb-a832-38c0-bbcc-678ae5a7b0f7 | -11.06334 | -46.64378 | 2025-06-26 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7feaa31a-7323-3011-b4a6-ca3e61b27459 | -8.72543 | -48.01666 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a98e3767-eba7-33e1-82ae-b180db26da91 | -8.86311 | -50.15695 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc335282-9783-3bf9-a9a9-8d852d9c4acd | -5.00807 | -56.17503 | 2025-06-26 05:06:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a84f2fc6-bd9e-3cc7-ab21-10f165cec274 | -6.57005 | -55.39371 | 2025-06-26 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aea27a65-4264-3815-ae30-b621dcd7e264 | -10.41358 | -47.50732 | 2025-06-26 05:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b89e39f7-255a-38a6-a03f-413f3f9cf84c | -9.67035 | -48.77073 | 2025-06-26 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbd9bfac-7eac-3490-884e-0a116eb47541 | -8.70915 | -47.98461 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df6445a4-7452-3e97-bd79-23f5e49b3e66 | -8.67357 | -49.94988 | 2025-06-26 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddcdb820-0510-304d-9c97-7bad6b6151b0 | -9.11889 | -49.43267 | 2025-06-26 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 20158cde-9a7d-305d-be63-6bafb0047fa7 | -6.17992 | -48.08525 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c6eebf2e-3724-3157-9611-9ed7434ae8b4 | -8.26137 | -47.01676 | 2025-06-26 05:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41bf0451-28c9-3e39-b470-f7dcbbd9b59e | -7.36715 | -46.23109 | 2025-06-26 05:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbf78e2e-80fc-3fb8-af5c-13157d1850c0 | -9.49799 | -56.09136 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d2ff30bc-a669-3778-a7a0-c615458107da | -7.20672 | -43.09587 | 2025-06-26 05:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 18b87434-227f-3e2d-acde-7823c7f88708 | -9.50742 | -56.09645 | 2025-06-26 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8304001-2412-3380-9dbe-a98c223a008a | -10.23754 | -47.458 | 2025-06-26 05:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| efea34e7-b64a-32ee-95c4-62b3d4531436 | -10.41895 | -47.50801 | 2025-06-26 05:06:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ed69350-32f6-37db-9b47-641476075a54 | -6.17751 | -48.08572 | 2025-06-26 05:06:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README15.md)
