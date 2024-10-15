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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f909130-5e1f-3b8f-9558-b1e8bccdc8fb | -6.56756 | -48.23728 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f5465c16-db45-38b8-9179-b2990846793c | -6.56695 | -48.24106 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f1c29375-05b3-3b9e-8108-69ccbce07e03 | -6.56634 | -48.24484 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3b02f49d-18c5-3a8d-ae09-0a573772c165 | -6.56573 | -48.24863 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 127ecf59-16ef-32a3-b28b-8dc4c1247029 | -6.56512 | -48.25242 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6d59906d-704c-3f0d-8fad-520522f02e60 | -6.5635 | -48.2405 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 91276d25-4f5c-3d74-976a-28644595a8ff | -6.56289 | -48.24428 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62d56951-4375-33ec-8e80-a840a7a9967f | -6.56228 | -48.24807 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2a59591-379c-336f-8680-d77a487cc106 | -6.56167 | -48.25185 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d13e4b64-f51e-3dcf-bf30-ac76cafcbe80 | -6.56066 | -48.23615 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 0d2be6ec-910d-3172-8321-ceb76ea4b60d | -6.56005 | -48.23993 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 84.8 |
| c5378478-be8a-3ab0-9c68-24816baeab65 | -6.55944 | -48.24371 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92bd89fb-8730-3fa9-8616-d0ef742f3996 | -6.55883 | -48.2475 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8c3efd9-71f8-356b-bf6e-f72f50fc7fb8 | -6.55821 | -48.25129 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 34b3257c-3c30-398e-8dc6-4f3b3ca5f241 | -6.55721 | -48.23557 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c3f4056-f953-3134-8811-8ec8a9c227ed | -6.5566 | -48.23935 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97bc436f-86af-38c0-8dd0-9279ae0775bc | -6.55598 | -48.24314 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1abd1639-87a5-3cc4-bcfc-9024232cdcd6 | -6.55537 | -48.24693 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e15d03c-b2f2-3dd5-8ab2-6fef42748205 | -6.55476 | -48.25072 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 021ff39e-b3b3-3f12-9b32-20ff0a883c59 | -6.55415 | -48.25451 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79be01d4-a401-3b81-8323-a4e65e96aa49 | -6.55354 | -48.2583 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f1474a3-6420-346f-b6b4-8ad7b52faeb0 | -6.55314 | -48.23879 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3d7ffb3-5071-38aa-909f-dd180c4b6fcf | -6.55253 | -48.24258 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6482c7b7-5a7a-373f-ab53-26e742417ca3 | -6.55192 | -48.24636 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68296f86-5dd6-3a76-87c2-320a3a01339f | -6.55131 | -48.25016 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e1fb5cd-d4df-3dcf-9eaf-fbf74499082a | -6.55069 | -48.25395 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f8b2980-1c17-3f6d-83b5-3772ddb4d1d2 | -6.54685 | -48.23387 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a9e08b8-3e85-3c7b-b1fd-a524e8d4ad51 | -6.54624 | -48.23766 | 2024-10-15 04:25:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1c50097-117d-3926-a6d0-0a7accc7fb8e | -6.41779 | -49.59624 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40d0b657-5f9b-3d8c-a87a-01f42661dc8f | -6.41707 | -49.60061 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9c1a7eb-aff2-36eb-b5c1-2efbfe975b20 | -6.41634 | -49.60502 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c6bf326-f6cc-3bd5-8f7f-634545ca9f81 | -6.41485 | -49.59118 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb2dd733-1b15-3177-b8db-31aa55a6d2f4 | -6.41416 | -49.59539 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c1ed67e-7912-3e7b-b4dc-9967bd246f4f | -6.41342 | -49.59983 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 421e3a06-f573-337f-9617-8a6634887c8e | -6.41267 | -49.60436 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a92a03dd-4589-32cb-a40e-2da609999fb4 | -6.4112 | -49.59042 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7499eaef-2276-3ec2-be08-4014208f6a55 | -6.40974 | -49.59922 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68976d93-3417-3215-8145-1f5e30de3d8b | -6.40754 | -49.58971 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e8d6663f-7790-3642-8513-3bd7ffe57af5 | -6.40681 | -49.59414 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d566f04-0392-3415-95c7-f1af427ba111 | -6.40388 | -49.58902 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db967797-9419-3ad0-8dd5-28f3770d03dc | -6.40313 | -49.59356 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1e6c1be-bb27-37e2-8d84-8ccf55599bf4 | -7.65434 | -49.36615 | 2024-10-15 04:25:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17138876-1b12-354c-a917-f0dd0b1c58e0 | -7.65076 | -49.36556 | 2024-10-15 04:25:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b230f95-e412-3af8-9a55-097403fa9c31 | -7.59648 | -49.44252 | 2024-10-15 04:25:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e2eb787-d6d9-30fd-991a-aa7ce9aa7df3 | -7.51855 | -49.48891 | 2024-10-15 04:25:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ab83a8f-364a-3d81-901c-288167a5d4ce | -7.51494 | -49.48828 | 2024-10-15 04:25:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22cc82c6-9974-30dc-a1fa-ab3d825dd444 | -7.39506 | -49.5345 | 2024-10-15 04:25:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 698ad4b6-e40c-35c9-8168-ca7beb69cec2 | -7.35743 | -49.58189 | 2024-10-15 04:25:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f12c74c7-dd1c-3780-adf4-d151255a915a | -7.34518 | -49.29411 | 2024-10-15 04:25:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 003d9f61-594d-3d10-97db-eb5afa80e246 | -7.3056 | -48.60614 | 2024-10-15 04:25:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4d174b2-24cc-38a6-88de-86237ac6c1d6 | -6.99943 | -48.54202 | 2024-10-15 04:25:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b681197-7e3c-38a4-bfb4-1327e18b9ba3 | -6.99802 | -48.54189 | 2024-10-15 04:25:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 353dbbc5-273e-309d-b64e-aba468baba7e | -7.11826 | -49.14265 | 2024-10-15 04:25:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a5e91d8-e821-3af9-8ac1-8c82c83cccd4 | -7.01531 | -49.32327 | 2024-10-15 04:25:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc5e5a96-15a6-3416-85af-ee16bafcfc93 | -6.77406 | -49.10624 | 2024-10-15 04:25:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa7c9fb8-4f80-3d3a-aa68-54a2ef07e760 | -6.77049 | -49.10566 | 2024-10-15 04:25:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29e64209-9222-3fb1-84f7-65e38fe41940 | -6.66767 | -49.46323 | 2024-10-15 04:25:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| c3c457ce-8e31-3eb3-837e-f9d9d9b09b4e | -6.66333 | -49.46684 | 2024-10-15 04:25:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 447f179f-057e-355a-8240-60216b8094fc | -6.42214 | -49.59277 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b520b32e-6f78-348e-ae9c-f2c429b8c86e | -6.42143 | -49.59705 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8af14961-5b26-397b-8fe8-1109fe143702 | -6.42072 | -49.60135 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4353a19-d48c-32b5-88ca-efdc21cc4f4e | -6.41849 | -49.59199 | 2024-10-15 04:25:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1a5a77d-5f13-3186-a932-4737a187591c | -9.27239 | -49.23383 | 2024-10-15 04:25:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21989de4-8d3a-330b-a834-ff94a3fabec1 | -9.18497 | -48.85997 | 2024-10-15 04:25:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffa20528-d883-3860-ac57-fd203cc22ef9 | -9.18152 | -48.8594 | 2024-10-15 04:25:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 706191dd-2157-3da7-a8d4-4ce2d3af66ea | -9.16422 | -49.82912 | 2024-10-15 04:25:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99dd93de-ada1-34db-a4ac-2e8025df367b | -9.16062 | -49.8285 | 2024-10-15 04:25:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1720334-48d1-3f80-86a4-f78e60771829 | -8.60128 | -49.57999 | 2024-10-15 04:25:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 565f5a17-c412-3038-bac1-8508db919db9 | -8.55989 | -50.10183 | 2024-10-15 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29cde5e3-a841-3429-993d-85a7848a13f7 | -8.3378 | -49.66172 | 2024-10-15 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7103ee91-151c-3d0e-bc8f-9eee5e65a7df | -8.25313 | -48.97622 | 2024-10-15 04:25:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9598fe73-153a-3535-a8c4-981073e8d1b3 | -8.20786 | -49.33901 | 2024-10-15 04:25:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce0990df-f7c8-3040-9904-95e20b9096b1 | -8.16884 | -49.18156 | 2024-10-15 04:25:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7702169a-0f68-3edd-b776-f2d1b65f9c33 | -8.16531 | -49.18097 | 2024-10-15 04:25:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a095c318-130b-39fe-979b-fc59ff5d830b | -8.11522 | -49.35389 | 2024-10-15 04:25:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aaf68cda-e924-31ca-bc4b-639aac68e5c7 | -8.09583 | -49.07714 | 2024-10-15 04:25:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9afa61d4-0ff8-3397-896f-47b11824373a | -8.05358 | -49.31602 | 2024-10-15 04:25:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac0fa804-d723-381e-b801-3feaa5a56de2 | -7.99217 | -49.85061 | 2024-10-15 04:25:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 356e8095-f6f4-3ec7-8540-6bd1fb439dc3 | -9.65811 | -48.97421 | 2024-10-15 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 560d5931-532d-3950-8e31-59d79708eef9 | -9.65465 | -48.97364 | 2024-10-15 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bcb70e5-a2c8-3c83-bf33-626126c46e62 | -9.62337 | -48.98111 | 2024-10-15 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef4639c4-8128-32b5-bd03-dedf2ab1b183 | -9.62275 | -48.98495 | 2024-10-15 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59ca3d49-a03f-380e-8903-bdd1f7e90e62 | -9.53257 | -48.99326 | 2024-10-15 04:25:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6579f4b0-daad-3dce-afce-32f58729ff32 | -10.82467 | -49.23745 | 2024-10-15 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c8e7fe9-1ce7-335b-81ee-8660dbabffd8 | -10.82122 | -49.23688 | 2024-10-15 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80bc81fe-4d1c-310b-ae2a-42804987affe | -10.52062 | -49.78712 | 2024-10-15 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7db5514f-9526-3056-b65f-3682410349bc | -10.4537 | -49.36275 | 2024-10-15 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e625918d-98cf-35c6-9582-2fb730cf6561 | -10.35024 | -49.61668 | 2024-10-15 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9613a7e0-1402-3b1a-9801-e270c3bbd4a7 | -10.34959 | -49.62065 | 2024-10-15 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fecdd260-b6b6-3975-a448-2c2199f43fd5 | -10.34672 | -49.61609 | 2024-10-15 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a83d113-9f59-3161-990e-a50a4b760c9c | -10.34606 | -49.62006 | 2024-10-15 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 334fa8e8-6c61-31b3-babe-4a36f8fa9358 | -10.34541 | -49.62403 | 2024-10-15 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87df83d6-d9d8-3cb5-8134-f2c41b75f29f | -10.1504 | -49.36186 | 2024-10-15 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad42f226-5abb-3eec-bce9-2d914ea76f45 | -10.13832 | -50.44347 | 2024-10-15 04:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bb2c9c1-e088-32e6-a5a3-bce9e7ebd3b0 | -12.10908 | -50.24716 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 270ee1be-ab4c-3e05-8cbe-51e64c360b3a | -12.10553 | -50.24654 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5d446af-0ece-3379-bf9a-26681cb18c35 | -12.10485 | -50.25062 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c73ebfd-cea8-3bad-90a0-0b6caedef982 | -12.10349 | -50.25878 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9de78243-8c4b-3a2b-9e82-62dac85fc3f6 | -12.1013 | -50.25 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4469822-859a-34df-ab2c-546f82e4fc98 | -12.10062 | -50.25408 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README44.md)
