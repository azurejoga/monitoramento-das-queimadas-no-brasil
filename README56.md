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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e660504d-83b2-3568-b666-b2ec220fdca4 | -4.09784 | -48.51609 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc2c8a93-ec9f-350a-8255-ddac86bfc826 | -4.08477 | -48.31137 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d1fe2f4-9a14-3370-ae5d-d8a3b8b254a7 | -4.08347 | -48.31116 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d7b8fe-d1e6-38c4-9cf5-39e8f04a4cb7 | -4.07212 | -48.3017 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 185bcfc0-ed72-3e40-8511-d9a7f1e0f64f | -4.06867 | -48.30115 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf25ffff-63f5-33a2-bd65-3ca0b60c43bb | -4.06294 | -48.29252 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd99d7ed-6073-3a41-aef1-dfc7c20778a1 | -4.06235 | -48.29629 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 296aab33-f38e-3dde-9bd5-d6993a31be45 | -4.06176 | -48.30004 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbb90051-3c3a-3967-ae1a-015826f27212 | -4.0266 | -48.29854 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5de70fc-e423-3d36-8ae4-36ed5163d310 | -4.02313 | -48.29806 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59895f46-7e46-322d-9ccb-bfa372721bff | -3.9388 | -48.35106 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15e8ca35-a080-3f0e-8dd0-65d9e032b89a | -3.93764 | -48.35851 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e122ba3-ffdf-377c-87f3-0675a86ec089 | -3.93651 | -48.34306 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fa3159c-0152-3f5d-b587-8662bd0c7101 | -3.93593 | -48.3468 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 940c47f1-dda7-34e5-b9fa-f8cb2d6fd9df | -3.93535 | -48.35054 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9413a03d-73c2-3b14-b508-3e510d20a4e7 | -3.93477 | -48.35427 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db8f76ce-14ee-3704-9433-29779650ee31 | -3.93248 | -48.34629 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52acca7d-292b-3e5f-94ab-710dececf13b | -3.9319 | -48.35003 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 236383fc-d9ed-33df-8cd7-ad8380bc3157 | -3.93132 | -48.35375 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80c54e84-77b1-3cbd-ac5d-0af46fa2f3c7 | -3.92902 | -48.34578 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36fad5cc-07cf-350d-b478-076de283f99c | -3.92558 | -48.34523 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f644b42f-d8c4-32f1-960f-41a4a1468c0e | -3.90775 | -48.36918 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5150df0b-f8f5-37ac-8d6b-e8e5d32f03ad | -3.90431 | -48.36866 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f9228b1-ed95-3f49-a6be-93885c75aa27 | -3.89397 | -48.36707 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3b89746-acd2-3ba9-ac15-56f95b1065ab | -3.81796 | -48.88109 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e901434-f7c5-36ba-9ace-584106c52000 | -3.81457 | -48.88057 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1558a91-d6c8-3c91-a490-07039868c0b0 | -3.81174 | -48.87644 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36a40613-8fbb-34b0-8ed4-08c628d1e5cb | -3.98882 | -48.97367 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5c54e7e-74d9-3fb5-8a25-989545686a68 | -3.96584 | -48.93663 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bac19c43-67e6-3510-912b-c9a5993d306e | -3.96245 | -48.93611 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0b70169-add2-3da5-9fad-71e3e6f3d665 | -3.92259 | -49.08055 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 386ea70b-2fad-3c28-b4e3-d8b06bd29001 | -3.91921 | -49.08003 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77994e06-72aa-3726-940b-a999ebe0f346 | -3.90235 | -49.07744 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a808587-f379-340b-8c48-b6fbafedfe37 | -3.9018 | -49.08101 | 2024-10-30 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86f1a902-a7c2-3628-afee-aec90128dd05 | -4.96671 | -49.36847 | 2024-10-30 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d4bb2c3-304e-3420-a88b-28ddbae76c0d | -4.96616 | -49.37202 | 2024-10-30 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fad6ec2-0ddf-3f78-a03a-4643dc0e0979 | -4.96279 | -49.37151 | 2024-10-30 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d6aecdb-1c17-35d5-8731-1e51ef2b93e1 | -6.4075 | -48.35 | 2024-10-30 04:44:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8518a417-e855-3b62-893e-f26874c8b0f8 | -5.84631 | -48.15627 | 2024-10-30 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bd77292-2645-3ca3-9d45-c3c2edf6fb76 | -5.23347 | -47.94733 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e116acd7-ae1d-3ea2-82b0-7a564ad52883 | -5.22991 | -47.94684 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4d57a005-edf1-3ad0-bc34-192f1b022808 | -5.22932 | -47.95081 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3cf9693c-95bc-3a57-ae22-00828e642442 | -5.22636 | -47.94631 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 89f6f137-ffa7-3e2b-935f-5e776df6cf75 | -5.22577 | -47.95028 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| be6cb430-4b7d-3e8d-869c-99af00bf86bb | -5.22326 | -47.94698 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 75465761-1760-3db1-977a-d1c90806b9ca | -5.22264 | -47.95095 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a2a423da-583a-333b-ac95-27bb41ead1dc | -5.22222 | -47.94975 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f79b889c-a500-3a24-9a3d-3a347b473f1b | -5.21892 | -48.11518 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a57c163e-c34d-3126-82dc-56408725effd | -5.2154 | -48.11465 | 2024-10-30 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d297f03-a407-3061-b7ee-7674652b62a0 | -5.99338 | -49.59133 | 2024-10-30 04:44:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 569424f1-1959-3e10-972f-7d21a0dfcf91 | -5.70878 | -49.31218 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48cd9d79-697d-334b-816b-04cf9eda3c36 | -5.70822 | -49.31579 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32c14ef4-e5e5-32c6-802c-103ed23c56f7 | -5.70483 | -49.31527 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4866418b-bc37-3210-a700-c2c298c01009 | -5.5187 | -49.20956 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 794ec5d2-e653-33c4-b4e3-c9b716a7b78f | -5.51558 | -49.49635 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 075354d8-6e5b-30a5-b1aa-3e8df646039d | -5.5153 | -49.20903 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9d7d6d6-bc8c-3a8b-a0a0-b6779fc361f5 | -5.51474 | -49.21264 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d873b20-656a-349e-b806-e8f28738988b | -5.51247 | -49.20491 | 2024-10-30 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b057eb9-f816-39c3-bf77-a3c6cc9f4a4d | -5.45532 | -48.87338 | 2024-10-30 04:44:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 096598a2-d1ff-322b-a19b-43c8af1af247 | -7.63265 | -48.53301 | 2024-10-30 04:44:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3caf21e-516f-3c56-8b9f-0141c42a4e58 | -8.84495 | -49.85718 | 2024-10-30 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3786aba1-fed1-382c-b77e-7f1c365cdbfb | -8.8444 | -49.86084 | 2024-10-30 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 62eb3e71-4a91-3358-8493-6240a6731d36 | -8.84155 | -49.85664 | 2024-10-30 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5315aefb-7074-39a0-b447-79f833e732bd | -8.84099 | -49.86031 | 2024-10-30 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 153a6391-b9ec-3176-adbc-534ee346dd80 | -8.65728 | -49.14032 | 2024-10-30 04:44:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cec66b35-fdb6-3cb9-93aa-00daf20d7575 | -8.54793 | -49.69906 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22b4785e-073e-3131-9f31-9da8811a5284 | -8.54737 | -49.70275 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78aaa9d0-b49f-33ec-9362-83b5e56040e6 | -8.536 | -49.70858 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5114853-69f9-332b-8b72-207e6bc48488 | -8.53544 | -49.71226 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4348dab8-28b5-3aa9-966c-b38386e0c29a | -8.14997 | -49.29689 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8a229e5-fe2a-386f-ba64-82f5e5f81ee7 | -8.14938 | -49.30066 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b450389-317a-393c-82b4-f62c2cfe8e41 | -8.14799 | -49.29958 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b18872d7-c87f-3ad4-8240-76e47a263b66 | -8.04874 | -49.65836 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c247e8e7-5dd0-396c-bb6b-c3099572a1fc | -8.04533 | -49.65784 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ea0a82c-3f61-356b-b92e-065cebe9f801 | -8.02034 | -49.63886 | 2024-10-30 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64e15f97-a37e-34a7-afed-bf55ad310eaf | -2.17137 | -49.11531 | 2024-10-30 04:44:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40d22a7c-c28c-389b-85d7-5d3036c94c37 | -2.15074 | -49.3121 | 2024-10-30 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244f2973-1eab-3549-87a1-f8a28ebcb632 | -2.1502 | -49.31558 | 2024-10-30 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f96903a5-0c0f-301d-9220-cec36a5b0cec | -2.12725 | -49.06903 | 2024-10-30 04:44:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11fbe324-59ba-3a98-9ceb-c42f8b96566b | -2.09697 | -49.50263 | 2024-10-30 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 570afd1f-482e-3a24-b64f-cfcf178955ae | -2.09555 | -48.86579 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17a63a11-1520-306d-a7a3-d88dd4825463 | -2.09364 | -49.50212 | 2024-10-30 04:44:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8de26194-42bb-3fdf-9453-c1b748d82537 | -2.08121 | -48.9574 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5d974a1-9b8c-3539-ac2b-0c322306da17 | -2.05533 | -48.88125 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a723ffd-086e-3e4f-bb76-59f860d80500 | -1.67886 | -48.80582 | 2024-10-30 04:44:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0916d69-06d7-3dd0-b7fe-37d3be807da7 | -1.67606 | -48.80178 | 2024-10-30 04:44:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d2a5d03-ca16-3190-8eda-b16d7bf48c87 | -1.67551 | -48.80531 | 2024-10-30 04:44:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a49418a4-e8dc-398f-8fbf-7f15024cd383 | -1.43622 | -49.23286 | 2024-10-30 04:44:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f8663b2-b0b7-3e44-99dc-01da1e5bf077 | -1.42733 | -49.22438 | 2024-10-30 04:44:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dc2cf11-7ed6-3601-b904-3c5d840519ca | -1.42564 | -49.21346 | 2024-10-30 04:44:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc761c27-5ea8-3422-a873-59b9f45a03c2 | -1.42509 | -49.21693 | 2024-10-30 04:44:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c792bf85-9735-364b-904b-72357925169e | -1.42454 | -49.2204 | 2024-10-30 04:44:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f01a0596-88d9-3033-a82b-c43a99d8fcf6 | -1.42231 | -49.21295 | 2024-10-30 04:44:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bf35ccd-3071-38d2-b593-ddba99eca930 | -3.07292 | -50.50671 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 359f21a7-96e3-3aca-94a5-e1ab84a014d2 | -3.07014 | -50.50273 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c129def-8fd7-39f7-8fcb-83d9acd46c0d | -3.0696 | -50.50619 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca3d65db-5e50-38fa-b6a9-5db95df44309 | -3.06905 | -50.50964 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f70cb008-280b-36e2-865e-9e551a31f4cf | -3.06682 | -50.50221 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b23702ad-a574-36ca-8f1c-5d3a666760c9 | -3.06627 | -50.50566 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcf059be-5e55-394d-b703-3b1b6f506426 | -3.05331 | -50.41521 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README57.md)
