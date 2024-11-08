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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8920df9f-d54b-3142-84e0-c8d581fa64e1 | -2.08653 | -46.17649 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c66d88-d61d-30b9-bd77-b97fcd6078a7 | -3.04925 | -51.33925 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35dccb34-b32f-343e-88e7-2d0a47847f52 | -2.81864 | -52.9459 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a32fdfd-dfaa-3a7c-8794-57f377453d55 | -2.61887 | -51.74448 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad83cd06-1f5c-3b07-ac42-50f684e26dd5 | -2.6096 | -51.76061 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83f0c886-9156-348c-abf3-4732dfe309c8 | -2.18335 | -46.46527 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c366f96a-6116-386e-b0b8-373bff22cb0b | -3.50441 | -51.14642 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2242df5-5f4c-3a09-b305-acee4be0398f | -2.18451 | -46.46269 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f0ee214-0d36-30de-ab05-7d9a7d9b2d7c | -2.72558 | -51.71529 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1af27b6c-929f-3f4d-ae4a-7f51db9dd27b | -1.16623 | -54.15942 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a97aab0e-8f11-3fde-865b-45d3007a299a | -2.17714 | -50.97641 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81eb3db3-9546-38b9-b36d-b81af9fb1ba0 | -1.3479 | -54.62263 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5da32cbe-719b-31bf-b272-8e542e8e0017 | -1.51645 | -51.3082 | 2024-11-08 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e325bc6f-3d73-35ca-bba4-95ee5bf8ac24 | -3.95478 | -48.14663 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8966483-b887-33ad-a11a-27846eea3ac3 | -1.21973 | -51.77122 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51a1b34e-f6a0-3eb4-8a83-7326bc387340 | -2.17206 | -46.43449 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f56862a-8ddd-3725-a00a-12fc8b7c6e6f | -1.56692 | -51.29203 | 2024-11-08 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5745843-eb51-3884-ae59-c3d9fb59484f | -1.67691 | -54.34841 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52ec4f11-3433-3489-9485-2db1e0da2b2d | -4.39659 | -49.40583 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db4f64ea-8ee3-3b3d-8568-d097b9507d66 | -2.5687 | -54.03354 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f3b7caa-140a-3ad0-980c-cd6b05c5d854 | -3.23387 | -50.45173 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b87af9f8-2fee-3208-b951-edd008ed5f46 | -3.02018 | -53.8661 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae2cec12-89dc-325c-8a31-a32468bccb34 | -3.41964 | -52.04249 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 465de835-c2e2-3383-a170-1fb34506a905 | -3.27561 | -53.41967 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9ae13d7-71ce-3e96-8790-4d21d2ef5078 | -3.96404 | -48.16209 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16821a76-9620-3214-b838-5ba35c5f46c1 | -1.28233 | -54.13605 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d00c26e7-3249-3ad5-9ed9-34f6b1d66f7e | -4.78032 | -48.67885 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 749b41d4-1fb6-37c3-9b9e-749e3b865e67 | -3.97312 | -46.41476 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71aaaa2e-8652-3fce-b492-cfdd33837f97 | -1.50709 | -52.06598 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d4113c5-0b93-3b19-b0cf-66b77fc72498 | -2.79852 | -52.94643 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e6590a63-c87f-328c-8afa-82b323b3049d | -3.22465 | -50.37632 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdbb890a-4df4-3cd0-a887-144d6497270a | -2.72279 | -54.14981 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86b96105-0c49-380e-a6ab-4bc989eeb722 | -1.23954 | -51.77427 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 285d25f1-bc9a-315b-a4cb-8d6bbf7f3235 | -1.15079 | -51.99619 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 95858025-debf-3b82-b710-b9262b4958a7 | -2.22004 | -53.72863 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b7c028e-985f-3560-a498-e22b25b36235 | -2.80519 | -52.94744 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0c14d2da-d8b2-34b2-8b57-2b33abb296a5 | -3.52357 | -51.52674 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 869a8ca3-f35e-34dc-be41-955ce075a7f6 | -3.40363 | -50.28099 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| befdac86-12fe-32a1-bb78-de524f7fe26f | -10.72991 | -49.53484 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b348d146-ce8d-3098-ba22-bff62b737e40 | -0.03984 | -50.78583 | 2024-11-08 04:53:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15d6ff29-0149-3aae-9b97-2f39755f6833 | -3.97467 | -48.16845 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9eba7ae7-7847-370b-a26a-5c843256d27d | -2.8041 | -52.95443 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 995e9f89-56ca-3c6f-9e5d-2a49caf8cb1e | -2.16225 | -53.64775 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9e100a3a-93aa-3382-adc5-8ef12ceed3bc | -1.24007 | -51.77084 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cfa3e65-d0e8-38e3-a447-b9bf99a73079 | -1.71027 | -55.1605 | 2024-11-08 04:53:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90cf2507-2e8d-3d90-880d-12e2e2522680 | -2.10825 | -51.09017 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8cc03dc9-56f7-308e-bd77-2d1b2b4ffad1 | -2.85594 | -48.45223 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f29bb5b0-fbc3-34b3-b54c-9eddcaf29d2a | -3.07758 | -50.5681 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b79048aa-fc39-318f-93f2-7e48de02eade | -4.23849 | -48.54728 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00f701a6-701f-3151-b8c4-30b5487640a8 | -2.8753 | -46.76872 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0369db08-45b2-3c85-a963-21ca54f7a906 | -2.84018 | -51.34896 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58e04431-7aba-311b-aecf-994afc2bf763 | -3.17704 | -53.84943 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ac008e4-1ab1-3016-bbea-6a80a8c5bf33 | -1.47166 | -51.13943 | 2024-11-08 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae198319-3522-36ed-bc40-cb8ea3e664b3 | -3.7183 | -51.63103 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5e89a63-f074-3028-8deb-f146360c5298 | 0.03318 | -49.4251 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1529e8e6-72d8-33a7-9d91-eed7a0da8d7a | -1.52858 | -52.62633 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59e78df5-98f1-316f-8cac-e2f3566d7254 | -3.29378 | -50.08338 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ec7777f-63ea-382b-8622-136294ebba08 | -3.58966 | -43.0323 | 2024-11-08 04:53:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 196450f6-5142-3111-826e-f1f60dbcb989 | -1.61802 | -47.35132 | 2024-11-08 04:53:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 417fe47e-1989-3d79-ab15-aaa1e3a59547 | -2.96609 | -49.28668 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13fe3d84-8ad8-36dc-a61e-35432d54d718 | -2.60843 | -51.74638 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a83b85d9-656f-3b8b-8146-daa82c21b526 | -6.08074 | -44.72154 | 2024-11-08 04:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74287e8b-66e0-336d-a101-271b746e4ab8 | -4.87592 | -45.72701 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e3cc67b-5dd5-3f1d-8f7d-1a2890bf10ea | -1.45504 | -53.41532 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 814b5357-7e6d-3007-9678-5b1f810443d6 | -3.11029 | -53.71478 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b291a2f-4208-3781-a8a5-de3196724eec | -3.0171 | -53.43798 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6e83076-1a9b-307b-a9a3-1506c4e1a012 | -0.89991 | -51.77033 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47244cbf-2deb-3fed-a46b-2a43ca5b826a | -4.88652 | -42.75521 | 2024-11-08 04:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 899ca893-6b24-37ac-9466-8bcbdfac51de | -12.32947 | -48.00964 | 2024-11-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 125f49e9-55ea-34ec-8b36-0938d18cc899 | -3.24118 | -50.44917 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ffb05bd-f7d2-3be1-95af-2b704d081fc9 | -2.21037 | -53.72337 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd3839a1-2772-3627-83a1-16a4a6e99285 | -2.21036 | -48.82747 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31f5da10-8cc5-36b4-b50a-6272e8976376 | -1.6265 | -53.43826 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea8b4e33-c334-3015-b705-bfb81783649f | -2.84192 | -52.9065 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbe2039e-eb1f-3f4e-a304-c19c6eefc112 | -1.25783 | -53.35148 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f501ef0b-5d57-3b36-8ef2-f74e5f3f54bc | -2.86653 | -50.32608 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7e89944-8bee-30dd-9225-45c4a7600298 | -6.17076 | -47.23322 | 2024-11-08 04:53:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f402d103-313e-358a-bb27-652010da552d | -3.10067 | -53.70957 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0843ce9b-030a-3d53-8266-5d6540fc7926 | -2.13682 | -48.74258 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70e047a6-ac80-32f0-b169-9efe528f52c5 | -2.84895 | -51.77367 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d863aa4-f285-33e9-bb8d-4133e947a1f5 | -2.9219 | -48.95752 | 2024-11-08 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 026a2c1f-9b76-3fb6-befc-7edd7c648cee | -1.62265 | -52.24277 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 742e0d3b-d47b-3d3a-a974-4618f04e329d | -3.2532 | -53.4089 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34fe35e1-7391-3f2c-b865-71f3e2512bdc | -2.80907 | -52.94445 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 80134556-e648-35fd-8c8c-dfb8a7f0545e | -3.25319 | -53.36506 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79fbe266-32d8-3dcf-8905-ef5b876315c7 | -4.20491 | -45.97449 | 2024-11-08 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26defb63-c9a8-3e76-8ab4-dae1f2c11b5b | -1.61523 | -47.35411 | 2024-11-08 04:53:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70656c9c-a7cb-3e2b-a347-209f01a84df7 | -0.64758 | -52.38511 | 2024-11-08 04:53:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec479b48-f570-380e-81b1-fc77c8d7fb9a | -1.45803 | -54.31108 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af949ef7-b6e7-35d7-bc7f-7ded7f47d1a3 | -1.24528 | -53.38692 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64a40715-1167-33c8-ac95-6b317ec6effb | -2.81017 | -52.93745 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e50b385f-fbc8-39a9-9ba7-c20aaae3800a | -4.56298 | -48.01261 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fc55ce2b-572b-3259-8032-6b68789efce7 | -1.52227 | -52.14233 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f78a1d33-b4dc-33e0-9d6e-1df848327220 | -2.17968 | -53.69602 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af3cf378-6170-395a-a0b7-87b0725cf89c | -4.1345 | -46.89948 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f18702dd-1326-32e6-a765-aa62ca2912c7 | -3.22463 | -53.39352 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee4f2e3f-c1bc-304d-bb83-7b619a843664 | -3.08992 | -53.71164 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a73e442-66ab-3a42-b2b4-a2dd57ef02e4 | -2.76697 | -54.04476 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8655f13f-6cbb-3490-adfe-f533a275a0be | -3.96095 | -48.15697 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c04e5b44-b5df-32ad-b4e2-72530a3af4f1 | -2.23615 | -48.36756 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
