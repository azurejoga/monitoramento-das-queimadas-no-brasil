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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19c120e9-bbbd-34d9-9373-911c3f1c0972 | -6.87748 | -45.86343 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 645dffea-886f-3737-9d0b-3565a4b7359d | -9.83033 | -48.61398 | 2025-09-02 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a7ca295-9b32-3221-864a-dada3738ed60 | -9.6688 | -47.84018 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 032bcb94-6023-3dad-884f-d842a35430ad | -11.1032 | -44.62071 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 752dc9fd-5fb3-33a3-80f7-c70b3e90e23c | -7.55296 | -45.69775 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4575658-297d-3bd6-b37b-bb91be5d747a | -8.17999 | -46.79549 | 2025-09-02 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f1c8553-40e5-37d8-bfd8-92974ec10bf9 | -9.7271 | -48.98496 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| debaae1d-1565-3f0f-857e-83d8620f908b | -8.05302 | -48.41823 | 2025-09-02 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1aff4dd2-2f65-3df4-9291-09299e9ee430 | -6.86128 | -52.81979 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c59788f5-bee5-33c6-989d-0e086e9bfa8e | -11.66393 | -52.22901 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 13f94c3b-2f76-3f6a-915d-f201f9dafc72 | -6.99707 | -43.2226 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d921617e-6129-3dda-a921-2b91194d9889 | -9.96925 | -46.41185 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45fde48f-400d-3b52-baae-b434c6cf76ce | -11.91724 | -46.67625 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99fa758b-182b-3cf5-b9cf-e4f0d0ec8b5a | -6.17706 | -47.27756 | 2025-09-02 04:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b130a7f-21a4-3a55-b209-8befa0f20c99 | -7.40409 | -42.05561 | 2025-09-02 04:14:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0c2c0b8-fe1d-3743-bc56-3106f55423ee | -12.78007 | -47.65129 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5358bd55-3cfe-3b42-ad20-2cef00a042d5 | -6.88831 | -45.8411 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4982662-9daa-30c2-8a3d-7b6006e0d650 | -11.97873 | -45.87534 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8ff29a2e-c771-3b36-b22c-a15eb0b627c8 | -9.61171 | -47.83292 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68ef90b5-5221-3c5d-9f9e-2732f0be59ca | -12.06826 | -43.2916 | 2025-09-02 04:14:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37fe662f-9bf3-31be-b4dc-bd1cdfb60177 | -11.92055 | -50.62862 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ed0dc38-65e4-3f62-8280-20ddd9286609 | -7.3125 | -44.27557 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3930de1f-c429-3df4-8b2a-c40e22614952 | -10.05567 | -48.1453 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b644435-53c1-38c3-9cf0-eb75751303d5 | -10.05107 | -48.14935 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b18a24c-0dbe-32c2-83c7-c040081f9b52 | -10.45423 | -49.05917 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ae07b2d-1a5c-381f-a51b-6ee75a4bd6d1 | -12.09229 | -43.33601 | 2025-09-02 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c72b00d-3ce6-339f-8fad-b260bb811004 | -7.98407 | -46.45453 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 176d4daf-0caf-3038-bc63-4c2c4aad932a | -9.73113 | -48.98566 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 15d8f55c-7400-38f0-8d78-25f520f13aca | -7.70613 | -45.01328 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5e1906c-da39-38f8-9b5b-8f81169f8794 | -11.67471 | -52.19727 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 008dd673-3531-360f-819e-2e08d83e52cf | -6.8177 | -52.84037 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad86fb91-b8b1-33d9-9408-89560e665bca | -7.49731 | -45.34747 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82f6653a-3e06-3b3e-8048-8e8f06f0f821 | -6.42862 | -55.61472 | 2025-09-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8139607c-4df4-3564-b5d5-e89b0f492687 | -9.8382 | -48.61526 | 2025-09-02 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9738df0b-d2e6-3b48-8bbf-21a6bd58c501 | -6.77234 | -52.8096 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06cbb2eb-42ea-3e1b-b752-860f870f6668 | -11.86595 | -50.60967 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ea7d094-6da9-3c22-b18e-7f39dd556cf0 | -13.72111 | -46.93045 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daebcf54-3bd8-342a-bcc9-008b8a85a8f1 | -6.8484 | -52.82881 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72def494-8ecf-3781-9a69-c81f3af78470 | -11.83558 | -51.53951 | 2025-09-02 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aadfe418-53bb-3730-bea6-14306853d088 | -13.75821 | -43.77452 | 2025-09-02 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f1ee121-2629-3756-b8d3-1ff0c22aebd3 | -13.68727 | -46.92692 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 890f33cd-b21b-3c79-ad96-76ea43c9cadb | -11.66798 | -52.22562 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 97ed7dd5-2040-308a-bd83-19e24481e1d9 | -11.4332 | -46.81765 | 2025-09-02 04:14:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3ad52cc-b592-3baa-b551-81161e980bd1 | -11.44151 | -46.81098 | 2025-09-02 04:14:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49f62ecb-b3c6-3b8d-9940-4e1c51e86a5f | -13.69837 | -46.88076 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51b9042a-b286-3a3f-9a60-581f8bf1b2b4 | -6.88353 | -43.83359 | 2025-09-02 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5faa324-598f-3fbe-8051-0ad050982e98 | -9.55013 | -49.16393 | 2025-09-02 04:14:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c97d0b2-e03b-364b-8655-ca009825804e | -9.75093 | -46.92595 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 793fbf56-f0b6-3c01-abe9-e09f76469b67 | -11.66039 | -52.16661 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 07317a54-aff9-3cf0-b6ce-8084b87e5bc9 | -6.81699 | -52.81541 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1673f435-7809-3a32-a38f-e15ada565965 | -11.37978 | -43.59637 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efd862f3-31b8-3deb-8b88-06809646617c | -8.15026 | -42.46972 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 16014983-e6ac-3c1e-a6ea-9539684f01f1 | -13.5492 | -46.97518 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b896a218-9a21-3434-a5fb-5e9347194c36 | -7.60986 | -46.03824 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| baebaaee-904e-3039-87ce-ecb161a63e05 | -8.85547 | -47.50644 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55c9d885-7ac8-34dd-81e2-328541558588 | -7.46572 | -44.80458 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 802a741b-c1d2-37bb-9c17-d3fc66405446 | -11.09988 | -44.62017 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f937c079-fbda-3dbb-9bf6-2dceb1cf9e17 | -11.79371 | -46.40736 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68f52935-d594-33a8-8816-63991799d6c6 | -11.86062 | -46.72655 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1edef71-9696-396d-9776-71c2d692b78b | -10.73509 | -44.7995 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7aa3167c-efea-3d2c-a235-8f0f41ff6e82 | -7.70791 | -50.25838 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 623b9545-287f-334a-b4b7-b3527d75db99 | -12.61792 | -48.18436 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9db209ed-e62d-3060-9509-87e51bbe7f5d | -12.86683 | -48.04827 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c223a518-5cf3-3a0a-a1d2-9e1025c3803e | -6.82046 | -52.82737 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6954fae8-5d4f-3e10-81d4-0039c7432771 | -12.58049 | -44.79323 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16875006-6cf4-3996-8e18-8ebb82141f18 | -7.69448 | -50.27697 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bf61bf15-c820-3399-8167-10bbe0939c12 | -11.66225 | -52.18361 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0c3b944e-5b1d-3683-aa68-aaa231c4f553 | -11.09601 | -44.62314 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0d430f38-02da-3d43-bf93-78043e4458f6 | -5.82484 | -51.38023 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae4d15df-9e53-3e8f-8c2c-50bbaed737a4 | -11.9002 | -44.88486 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee77b1ac-bbd6-32ab-9cfb-edb5b0c2c5e9 | -7.96294 | -46.3382 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32544f59-ec58-3b0b-a8be-da20ec630268 | -7.56866 | -45.23267 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d997cbc-6a65-37d3-aef9-569bb0c8e0e6 | -7.3086 | -44.27856 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5334f65a-f8f1-377a-8457-3272216357b8 | -12.5683 | -48.26064 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e2fcb04-4d82-30c8-b2b3-79b012dcfa85 | -8.26034 | -45.61469 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bb070c1-12ab-3b46-b85e-8b0a965650e2 | -8.1264 | -45.03282 | 2025-09-02 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ac62bcd-8554-3824-b8e5-e886fc6597f8 | -7.93136 | -46.46272 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 888fb3c2-52ee-3349-825e-1b62e0e95e80 | -11.66315 | -52.22474 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 0f17926c-20c5-3c88-a9c0-28575e34584a | -6.87587 | -45.85111 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c7e60f52-223c-33f2-9dd4-762b83383a13 | -8.01437 | -44.05034 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a64c97d3-a2f6-3e26-b9b0-248d16b728f5 | -7.18056 | -45.76172 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a4e0572-65f0-3336-8262-09e5af220b18 | -13.69495 | -46.93871 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ce02af4a-4bbe-3118-8895-ace755d05155 | -8.84372 | -45.80495 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c440d1ba-f217-3c2b-9650-f2ef4bf192d9 | -11.09876 | -44.6272 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 8d0f9ccc-199d-3954-8d6c-ac69ba45ac6c | -6.79353 | -44.62687 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df26046e-1fb1-3a72-a38b-30c0bdb05795 | -12.33064 | -45.7175 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47cf8b5e-49e4-3c41-8198-7d4caf78e06f | -13.50823 | -47.00791 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9bc47b3-b286-32aa-8127-e546824ee294 | -6.42761 | -55.62036 | 2025-09-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f8162fe-7c8f-32b5-833d-119b5832b680 | -13.3199 | -46.83209 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06077352-d779-3aaa-9f9d-a37a4eb00ccb | -11.81214 | -46.4024 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be35fc98-0ec6-3ab5-9486-9367c527bdcf | -11.41911 | -46.89761 | 2025-09-02 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17468a28-4bc0-3c94-b28e-2dd0d51c1b1b | -11.78684 | -46.40625 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62e369a9-2439-3319-846a-69b44eabbd1d | -7.62724 | -42.6486 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6e4b832c-0d6c-325a-82f4-4010074318c5 | -11.31262 | -55.21939 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42c8bac4-ae1a-3811-9386-fddd07995d7e | -11.67384 | -52.22107 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 6f839214-05be-34c4-9f94-b8200b6c7da5 | -8.18433 | -46.79182 | 2025-09-02 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| daac536a-f116-3d4a-8c27-eb0026c18091 | -12.98574 | -48.09937 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bde60a3c-ec8a-36ba-911c-16ba85715624 | -9.66958 | -47.83559 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42370ca1-0622-3486-a6ba-68378e79d165 | -13.4972 | -46.92541 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79933183-85b7-3f16-8618-1a4feea30121 | -13.54101 | -46.98175 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README40.md)
