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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88600b2b-c468-324c-bba3-f8f62f5b750f | -12.28828 | -50.37089 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cadbecbe-bb4f-3254-9079-758d5c4ad433 | -12.07294 | -42.21412 | 2026-09-27 04:10:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 98de5630-60f5-31b9-830e-a1847e0a5e83 | -16.56563 | -53.07171 | 2026-09-27 04:10:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee46c227-548a-31ef-8d7d-3e39ff037ece | -11.89093 | -50.5209 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b21879d0-3140-3759-926d-dc3a8267cd5a | -13.3714 | -51.31559 | 2026-09-27 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdf2854d-8d4b-3c89-9af3-29e448a6022c | -15.68435 | -48.22596 | 2026-09-27 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1458e43-a7c5-3d91-9d2c-2425f1e65957 | -11.01347 | -54.05099 | 2026-09-27 04:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee21e0da-6689-32ce-8aad-b259d9985efd | -12.6607 | -47.31381 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f5c24d6-c836-341a-a429-f3859a9df4e9 | -12.26354 | -50.69862 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b75c4280-c540-3b31-91fe-96f35380b377 | -11.96231 | -50.54565 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb50e09c-cc94-37b7-82d3-98a105553c2f | -12.0346 | -50.5922 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 452991c7-d9be-3b48-8f5b-ab4fed406a8d | -12.13725 | -50.33518 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a16b962-85a0-3068-9ee5-89942b4ed489 | -12.29951 | -50.39613 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c9af12c-61fc-3d88-bb74-6b7e29f28e09 | -11.95869 | -50.50753 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 012dc889-fcb4-38fe-baa4-6c43f28e4088 | -11.77247 | -51.00502 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 25921318-e303-3550-bb56-820ebb004596 | -15.60543 | -41.35115 | 2026-09-27 04:10:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 4f903279-6854-3642-b3e8-65e85bb614cb | -11.2765 | -54.44202 | 2026-09-27 04:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9057380e-c5bd-39d9-9563-331b94bdd6e5 | -11.86439 | -50.52043 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e3233015-a7d6-3481-93f5-ccd394399f66 | -12.28101 | -50.29777 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 78e35cec-514b-3cb5-bf2a-8e9c9c6c5862 | -12.66349 | -47.29819 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb6a885e-4194-3921-baa6-91575a2f4f7e | -11.88966 | -50.52744 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68563580-4c1a-3517-a0e6-d529aa8bafe8 | -11.77315 | -51.00147 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ab13409d-58de-3c8b-aa94-c600ac4e79e4 | -11.03915 | -51.32972 | 2026-09-27 04:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b631b3ae-0c25-39e2-aa47-3ae67c3d0f4e | -14.52957 | -48.32629 | 2026-09-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 481d3add-17e4-3d1b-a5f1-cd772b36d327 | -11.85755 | -50.55663 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb0af0fc-f14c-3545-acd3-93f93ed2b827 | -11.05255 | -51.32048 | 2026-09-27 04:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dbdd13d-0b26-3f00-8111-c6c4ac611845 | -17.63043 | -44.84405 | 2026-09-27 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee07f222-813b-3b8b-a861-0a0d93bfd329 | -15.93086 | -42.37282 | 2026-09-27 04:10:00 | NOAA-20 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f73ecbab-1695-32ef-8d2f-c35410a89bbc | -11.88047 | -50.51877 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d183c5b0-0009-3965-977f-21c1b2caff55 | -14.53032 | -48.32222 | 2026-09-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d84bfebe-2be8-372f-a472-333223c6c9e3 | -12.1787 | -47.38251 | 2026-09-27 04:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d69fe9c-8e96-39b8-915b-a7de794682f8 | -12.7261 | -41.80745 | 2026-09-27 04:10:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4cb147b4-39c1-319f-aed7-70faddfc8b5d | -12.66907 | -47.31531 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b54a7db-4b51-3dd6-8d1a-68ed71b1ff52 | -11.98016 | -50.56637 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 020aad9d-fc7e-3b64-a36c-675babe88251 | -11.97954 | -50.56966 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21070654-ae68-335b-86b9-82706443400e | -12.02809 | -50.59772 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d0630217-5503-3a88-9f91-7782a2f73409 | -11.96169 | -50.54893 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac7e5ded-748c-31d4-823f-895414db7db3 | -16.39094 | -46.89902 | 2026-09-27 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2277726e-7d30-3e43-97a0-9083913ff114 | -14.72846 | -45.58095 | 2026-09-27 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c524ffdc-a10e-32a1-a722-9603b729c3f0 | -17.57359 | -46.90277 | 2026-09-27 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17339ff8-d9f4-3d6a-8984-0c50eb6fe2a7 | -10.78682 | -48.73088 | 2026-09-27 04:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3bea613-e259-386d-a691-043ccf779e81 | -12.66489 | -47.31456 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d193c7d-9de5-3345-84f5-90777d7ce2cb | -16.56339 | -53.07248 | 2026-09-27 04:10:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dd36bdf-171b-3c32-9c5d-da154a47f943 | -11.98408 | -50.57171 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c7eae68-3216-3348-9741-02fa64093ab3 | -15.98504 | -54.93725 | 2026-09-27 04:10:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| faa5b1fd-14d1-327c-a1ce-23d54b3e3099 | -11.77339 | -51.00668 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3081ca30-e1ea-397d-9853-dd2ef5d573f5 | -12.02619 | -50.60762 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 773453ab-2ec1-3401-aa8c-3cfc9db2cf8c | -14.11921 | -46.33609 | 2026-09-27 04:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2621b48-76d6-3227-9ed3-c774f51b1f55 | -11.97244 | -50.57849 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 535ddbb4-7b6f-34f2-b65a-03a4f7b06581 | -11.88698 | -50.51329 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9d4040b7-1ac6-3238-9b77-31fc4f03a8fa | -11.98479 | -50.57074 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7ab885d-dc64-3ecc-a046-02439842fefb | -11.11226 | -47.71919 | 2026-09-27 04:10:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba91390f-ac24-3b93-ab23-4742164b99e9 | -12.5705 | -44.14083 | 2026-09-27 04:10:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14b04a9b-9577-3f99-a468-b08b0a60e213 | -17.79129 | -47.16449 | 2026-09-27 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd00f4c1-dc99-34ce-bb7b-a9be056f53a5 | -11.85853 | -50.52265 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6d1745c7-b07e-36c1-8445-0d8eeb7554a0 | -11.942 | -50.5381 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 12e38b29-db83-30b3-a259-5f7407fd39ea | -15.33095 | -42.12953 | 2026-09-27 04:10:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d46e7bd-f724-3583-930a-b807a56810c4 | -14.06463 | -41.93384 | 2026-09-27 04:10:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9153b7d9-59eb-30c5-872e-858bb3224c68 | -11.98536 | -50.56514 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 91343042-4f15-3ff6-9eff-371677af5d0e | -11.57388 | -50.50818 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 286cd1ca-c9ab-396e-8017-81abfec0354f | -11.89221 | -50.51435 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3917de39-c36d-32eb-aeae-1879dff291c2 | -16.50139 | -43.5331 | 2026-09-27 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00f2ef7f-cc13-372f-b28d-e0fa13afdb25 | -15.41375 | -47.89504 | 2026-09-27 04:10:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0e1ecae-f7a7-3963-b692-508ecb6c6f05 | -17.78835 | -47.15888 | 2026-09-27 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57eb2c14-4976-378f-a4c7-a1bc7a1ee8ee | -11.87887 | -50.5302 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d433128a-8608-3805-b41c-2697c5d38bfc | -12.29211 | -50.7426 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b50f733c-6748-3d6b-9815-d41304548cdf | -13.69406 | -43.13781 | 2026-09-27 04:10:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50870b8a-84be-32fe-afb8-f5469188bedc | -11.04146 | -51.75327 | 2026-09-27 04:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64bafa17-9a67-37e1-ba8f-966d75440f98 | -12.71939 | -47.30348 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daa80079-a7ce-397c-a925-fa7fe19c78f2 | -11.94637 | -50.51519 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c348a8d-dcb3-3c84-a02c-ff5495f711c5 | -11.77479 | -50.99961 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 06696695-dee3-332f-9a1f-392f71c3a8e3 | -17.87531 | -42.70429 | 2026-09-27 04:10:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 536cb9f8-1d46-3069-bfd0-563bb044772b | -12.70817 | -47.31765 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 140b4a1c-ce1c-3b62-aba2-b4cbf2a09293 | -10.40997 | -53.81625 | 2026-09-27 04:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74b7dc85-71c1-3e65-8961-6faa046f1030 | -11.92673 | -50.50439 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cccafaaf-10d1-3c2b-a3eb-19f39e7c5926 | -14.50122 | -48.33416 | 2026-09-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9ca5a46-24fe-3158-85e4-860e6dfbe28a | -14.06795 | -41.93439 | 2026-09-27 04:10:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8add6799-bfa3-3e69-8d8b-b026fed59e7d | -11.76976 | -51.01924 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d50817b-a9da-3ff1-90c8-1dd16a0a5975 | -11.77044 | -51.01568 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16b7d28a-fd18-3b0b-abbb-9b6d72804a0f | -16.56975 | -53.07029 | 2026-09-27 04:10:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03eb5850-344c-3452-9681-feb5e855359c | -11.85205 | -50.52815 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c05ca731-c277-3f98-8b19-a5357e9dfd9f | -12.2334 | -50.71321 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8bd33c0-b84f-35e2-a344-35572c6094f9 | -11.85143 | -50.53144 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c2860d-7d00-3fb6-b68d-501b361d432b | -11.02894 | -54.04262 | 2026-09-27 04:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ef0102a-8f0a-377e-a42b-9a5fd6c50579 | -12.28733 | -50.29257 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 39c10a79-8983-3eee-883d-a401bfc7a51c | -11.85392 | -50.5183 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9fe27bd2-a404-3c93-8975-92ee4754f523 | -14.78574 | -45.94709 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec3f7edb-ee65-33e6-8d94-aecf3e6139a8 | -11.23737 | -49.84966 | 2026-09-27 04:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7b634218-ac79-37bd-8de9-fb8d4334ea8d | -12.29637 | -50.30088 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3d14ae31-24c9-3e7f-a811-4b9f056a84ec | -9.6119 | -55.10873 | 2026-09-27 04:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90c0e84d-fe5c-3237-af63-2f61731c71d4 | -13.33817 | -46.80098 | 2026-09-27 04:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a82c002e-6950-3a17-82f6-6337478b99f8 | -12.72012 | -47.2995 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 504286fb-a218-3699-a4eb-e419b3a7bbf4 | -18.02064 | -47.63594 | 2026-09-27 04:10:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 672386ed-8f1e-3430-9600-8e9d3ce8b9c1 | -11.94575 | -50.51846 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a44ed304-6554-32b8-b9d7-ef7d56321d5c | -15.99137 | -54.93888 | 2026-09-27 04:10:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24a50015-c3b1-3e07-8ad3-ff857c6d79ba | -12.29375 | -50.39824 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1349ab6-9008-36bb-92df-b52588be0f30 | -12.67749 | -47.31657 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8421a271-5b3c-3b81-9907-128311062299 | -13.31296 | -43.99819 | 2026-09-27 04:10:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0509f5cb-6a91-31d1-a589-9c9174ccd731 | -12.20568 | -50.37568 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 152496e6-c906-3623-b240-f6c9cf4e6316 | -12.12141 | -50.30578 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README20.md)
