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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3a5b2e1-5f40-390c-b69a-371a230f0c6a | -6.28696 | -43.63553 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3c177b6-52f8-35d9-babb-c3224f25f6fb | -7.75914 | -49.20424 | 2026-08-20 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5af91df-f31a-3067-8474-93127c770779 | -8.53431 | -54.87161 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| def417b6-5c00-3c8e-ae1a-3d2b412f1dc0 | -6.24629 | -55.40876 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55a34036-8711-3ea7-a3e6-e804e8bac467 | -5.60537 | -44.22158 | 2026-08-20 04:19:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5deb1cdd-8946-3df6-b438-891871e2ee3c | -8.72146 | -49.61779 | 2026-08-20 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 234b4bfd-ac65-39a3-8ded-cede3cfe6737 | -8.58588 | -54.76215 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b440aeb2-16e1-31c6-83de-ba1914bbd069 | -12.38705 | -46.44947 | 2026-08-20 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22bf1d93-8761-3fa5-b340-a2db4526814a | -5.42919 | -48.41387 | 2026-08-20 04:19:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c167616f-bcb1-3ae3-97c9-0728983ccd0e | -6.43989 | -52.76205 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c69559a3-64df-3876-a6ec-3967fb9036c6 | -7.63535 | -42.73235 | 2026-08-20 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9205f05d-9dfb-302c-8992-6639740daeb8 | -8.66099 | -54.58855 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87bfdbe2-af93-30dd-89d3-d33caa2b3de7 | -10.78481 | -50.30939 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d995568c-0f98-3a0d-b2aa-03b4e0a723bd | -10.74609 | -50.35283 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a40301ad-0c3e-33a8-b3a3-74fab1b37d63 | -12.25227 | -43.16508 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fc8da4eb-f90b-3f2a-a406-88641bb3b6fb | -8.71725 | -49.617 | 2026-08-20 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5cb5467-9485-3a72-96e6-24d6cc1788e8 | -10.42137 | -48.33022 | 2026-08-20 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4a73419-fdf3-3686-8559-c74585a77060 | -7.61451 | -45.16375 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56a70243-48c3-3e9b-8175-62bd8849e3ca | -7.71458 | -46.16381 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6cb571d-29b5-3b2f-9fd2-55412beb5553 | -10.74535 | -50.35693 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 13def081-fa04-3969-b8e1-602af7ac8931 | -8.46454 | -46.95969 | 2026-08-20 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5639c95a-fd97-34ea-940b-884ac76275c7 | -8.67155 | -54.65222 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 898b3ccc-e80f-3704-b724-b01f92b50d72 | -8.5867 | -54.75779 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a685f4eb-fe20-3b5c-8427-59379748afff | -11.37785 | -46.37481 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e80d88eb-ed63-3605-9d6f-994476a0c0b1 | -11.39213 | -46.37349 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 66c37073-11b3-3de6-99ef-3d6920169a0e | -11.4252 | -47.24807 | 2026-08-20 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f155b34-d040-36c0-813f-246f5ac1e02c | -5.8057 | -55.72925 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73c7c655-0618-3188-b319-4c4e0792e83e | -7.0191 | -45.8939 | 2026-08-20 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17498179-7ea1-32b3-a60d-e5982e565fcb | -6.83976 | -44.93943 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39e9e398-e7ff-34fb-87f3-5e6c3e958b58 | -6.14287 | -47.22581 | 2026-08-20 04:19:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79ce03c7-ba11-329a-968d-9382e20ee7b6 | -7.63867 | -42.73287 | 2026-08-20 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d1f28b6-b7b8-3e52-a6dd-bcb45f1e2e6d | -6.44008 | -52.72985 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 913d95bd-4916-392e-994f-050f4d706877 | -8.36361 | -46.33845 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f737bd60-0278-3e86-8a6c-95d69d44d458 | -8.58078 | -54.75653 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0cfaf60-32a1-3ee5-beab-8c824d0c7fe3 | -7.00863 | -45.8922 | 2026-08-20 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea16de9f-8c2c-36ad-9306-9f48ea13891f | -10.63012 | -51.61753 | 2026-08-20 04:19:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6f4e1cd-f189-3770-ac55-d2f1d50d40bb | -7.6151 | -45.16011 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1f51d6c-ffd3-3a0b-9b57-d73d399be903 | -6.4299 | -52.7244 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2b44ad2-de59-35da-9d20-ead3b22453ba | -10.7604 | -50.34702 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d2e917b-df48-35be-80aa-913dd782cdad | -7.34481 | -45.82998 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b9284a31-8751-3ffd-9d8b-f3b29d51d022 | -8.54087 | -54.72382 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0ba22d2-785b-3f2f-9c1c-54adcf9e98d3 | -7.63185 | -45.72289 | 2026-08-20 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9ab7fcf-49c3-399a-8988-3778dd800ad6 | -12.22866 | -43.16126 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2db8a8e9-0481-3876-b6e4-e60b352a88b5 | -6.29469 | -43.65095 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b0455ba-278a-3a40-9600-1c789cce9dd4 | -6.95108 | -52.81411 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b6bb3a2-114f-3793-a191-34332160533a | -8.57608 | -54.68386 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e2140a6-9a19-34b7-93be-5dffa70dcbff | -8.6699 | -54.63939 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d05de412-0af6-345a-91e5-fa0d0b47a402 | -8.50945 | -54.87182 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f37b75c7-63d4-355c-8131-64c35f20ac91 | -7.53276 | -55.57505 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6a6cee46-2ad4-3e4d-881b-9238e9bf17e2 | -6.26901 | -43.27852 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb67039f-5da9-32ad-b4d1-43754b81545d | -7.00162 | -48.04179 | 2026-08-20 04:19:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff50d510-798d-32a8-bfa2-5a300f81b9b2 | -11.28299 | -45.79351 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e31ab6a0-1363-31dd-91ad-24ad41b04285 | -7.64868 | -42.75604 | 2026-08-20 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| eaedd18a-9493-3a90-a2f0-08f61c8d95d7 | -6.95307 | -52.81416 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daa2b275-54d0-3d4a-bcd6-33cad00225a3 | -11.58265 | -50.53611 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 772521d9-7ee5-3342-a458-8c1fadd4167f | -8.56555 | -54.772 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11d273bc-2242-3bdf-8cff-3532d424a51b | -10.75967 | -50.35111 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efb7bd88-6efc-342f-bbae-f6a0c3779d12 | -11.42588 | -47.24404 | 2026-08-20 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e216defe-c6ca-3123-926c-b2b6d6bf33fc | -11.81068 | -44.81334 | 2026-08-20 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cbdfccb-c7ea-3466-891a-78fb6267f288 | -8.67074 | -54.65646 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76693854-6727-3f84-b9b6-fc158922f03e | -8.45176 | -51.55171 | 2026-08-20 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6496c1fb-e45f-3328-882c-9c518471ce1b | -5.73936 | -43.27556 | 2026-08-20 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84fd39e0-3ffd-39c4-80dc-6899cfb78c64 | -8.67746 | -54.65324 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4cbb551-9b87-3a8a-8f5f-7f81c99a721f | -8.56508 | -54.67723 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0995dd4-94b4-3b85-ac95-bbf4881aa89d | -7.35015 | -45.81903 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 03fd4663-e6f2-3bfe-ad5b-913b3609020b | -6.42221 | -52.75778 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf207471-6625-3a53-9b57-caf775cb0014 | -5.73528 | -46.07742 | 2026-08-20 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ae7a75c-7925-352f-88ee-049704bc1d06 | -12.24103 | -43.17071 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 629f130c-510c-3f3e-bf65-e383a0df64b2 | -6.42754 | -43.06991 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 697a14d3-cf20-3614-a5b6-4122f35102ef | -10.82819 | -50.28806 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21bbb0b8-5cfe-3fec-b905-434ed3938b1e | -8.6691 | -54.64373 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4e97274-fa96-39b6-8d8c-92427563cf0e | -10.44838 | -54.66388 | 2026-08-20 04:19:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b6df2c4-010e-3921-9cc0-88200f722129 | -11.1417 | -49.04188 | 2026-08-20 04:19:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 015738e2-707b-3dd6-8d61-d96b788b49c2 | -6.78395 | -42.87756 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f65064e-76f1-399c-a010-e2209b6a3d41 | -7.52795 | -55.57536 | 2026-08-20 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da8e5c92-15fe-34f1-af2e-489a69b37123 | -8.47898 | -46.96212 | 2026-08-20 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c7e92ad-64d2-3dee-a30d-859a184245b4 | -8.20372 | -47.39618 | 2026-08-20 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c3faa83-d67a-3755-ba79-9a8844097404 | -6.99131 | -47.44437 | 2026-08-20 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daa81590-3472-31aa-9a6d-22cbcf88c9e7 | -6.4353 | -52.7254 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c28e9da7-8e4d-3175-b7b0-453cba486512 | -6.34205 | -44.07936 | 2026-08-20 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 67cd5f43-f185-3538-b7b3-fb96b87323d3 | -12.36684 | -46.44281 | 2026-08-20 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76c96c76-88e7-3aef-984f-a36c1275c038 | -10.82748 | -50.29212 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 271e2348-bfcf-3876-b4e9-e2c6e429dab1 | -5.80128 | -55.71627 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca7ac60c-c2c2-3b1f-ac99-0ed59ce93e2b | -10.47915 | -50.31924 | 2026-08-20 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 734b029b-13db-354c-9bb8-9c8ffc38dc9f | -11.46261 | -46.56414 | 2026-08-20 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e429b012-d753-3671-b529-42e8a4c6c557 | -6.29524 | -43.64748 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6c3de04-9492-36cd-a93a-f314ce74c0d0 | -6.52323 | -43.62387 | 2026-08-20 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c5547b9-a3da-3374-ae01-ca033fbab728 | -7.46225 | -45.14701 | 2026-08-20 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6958ccd9-cdeb-33c9-9d77-d17bc887c175 | -5.79578 | -55.70917 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7769cacb-d3ee-3259-9fa3-c1d71baf6a52 | -6.34294 | -54.90372 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 934682a9-3421-3db6-9263-2baccea8bceb | -10.45335 | -54.66896 | 2026-08-20 04:19:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7462f79a-b62b-3981-bf87-eee50b89e22c | -6.33872 | -44.07883 | 2026-08-20 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f26657ce-88ad-322c-9691-a41842cb5568 | -11.31618 | -45.2061 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83a99d4e-a6d6-3f05-be04-c2e7c8e348cd | -8.57994 | -54.76101 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e76a3c8-47a1-3786-925c-f98c1ff5a8aa | -12.38665 | -46.44994 | 2026-08-20 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 747140cb-320a-32c7-afcd-788692db55c9 | -12.24671 | -43.13387 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d873e81-156b-3164-80ba-cf399e09d89b | -8.55736 | -54.65347 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f5c9fc7-4b4b-3dc2-bb3f-e6c1bf946222 | -12.19375 | -45.15875 | 2026-08-20 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80736bba-5972-3631-b8d8-9e371513fec2 | -8.11233 | -47.16397 | 2026-08-20 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9de0c30-62d3-3069-8802-0d64ee7f0f70 | -8.55864 | -54.66036 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README35.md)
