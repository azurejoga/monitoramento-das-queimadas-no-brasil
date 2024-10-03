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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c431afa5-31da-3bc6-959c-f5da9c3dc3d7 | -12.39013 | -38.00209 | 2024-10-03 00:28:00 | TERRA_M-M | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 1a31cda7-5f13-3a23-9989-cbdb242eb7fb | -12.3468 | -38.06852 | 2024-10-03 00:28:00 | TERRA_M-M | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 56d413cd-f7b7-3685-b5b6-5784904d0c6a | -12.27083 | -45.97043 | 2024-10-03 00:28:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| ef2dd0c6-b2bc-3dde-b922-59a357620dd4 | -12.26428 | -45.97768 | 2024-10-03 00:28:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| d0d2f729-c659-3bf1-b593-1fd2bb12a4d5 | -12.26218 | -45.96098 | 2024-10-03 00:28:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 342eedd3-dbe0-3f49-aac2-9f39faaf913c | -11.84486 | -43.83018 | 2024-10-03 00:28:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| b00dc1d4-4dc7-3c64-b774-b63c761b80e3 | -11.83488 | -43.83154 | 2024-10-03 00:28:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cab21e80-0c04-3fd7-8064-f0b675cf6648 | -11.5637 | -42.17869 | 2024-10-03 00:28:00 | TERRA_M-M | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 78f9cb8b-dacf-321d-a17a-b8f05274572e | -11.27716 | -43.39866 | 2024-10-03 00:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 637dcc42-043e-3ec1-a01a-f7ee87ea7f63 | -11.2095 | -41.06887 | 2024-10-03 00:28:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b6597b08-0771-39b6-8b24-87388d0dfe7b | -10.73101 | -46.18531 | 2024-10-03 00:28:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cb912640-feb5-36be-8398-c1ce9b8f18dd | -10.71727 | -46.1699 | 2024-10-03 00:28:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 24044dee-4a21-36ee-91cf-9ebbcc3a1b75 | -10.66812 | -44.50884 | 2024-10-03 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f412a6d3-8505-3fb7-929f-832e6ebefccd | -10.66652 | -44.49655 | 2024-10-03 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 26cab8a5-1b35-3aee-ae1c-e7cbac3c3024 | -10.65783 | -44.51019 | 2024-10-03 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 57d26823-53fc-3a1d-8b3f-3a1334ddd01a | -10.65624 | -44.4979 | 2024-10-03 00:28:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 797b1da2-9297-33fd-af27-ce817f3373bc | -10.14241 | -36.15229 | 2024-10-03 00:28:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 1ed4e93b-ae40-3876-8164-328e8d078ced | -7.80543 | -47.47382 | 2024-10-03 00:30:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bec89d37-dbe6-3943-b02d-0c85cb6fd0b7 | -7.74063 | -49.89855 | 2024-10-03 00:30:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| ed5916b9-1484-3cf8-bd43-23e2a12623af | -7.7391 | -49.89327 | 2024-10-03 00:30:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| d9cc0989-d330-3641-8f2b-564725a53a60 | -7.23208 | -45.52634 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a707034d-f3e2-321c-b280-6264ec2cafa5 | -7.11219 | -47.87821 | 2024-10-03 00:30:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 73ea1aee-8632-3635-8b58-eb3e81da128d | -7.11188 | -47.88383 | 2024-10-03 00:30:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 2cca97ea-40bc-3811-9cb3-cd497244014a | -7.09877 | -44.46397 | 2024-10-03 00:30:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4896951b-1e1a-3d1b-8385-545203c0987d | -7.06853 | -48.04946 | 2024-10-03 00:30:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0bd69547-46e2-3338-8298-344f49d02fe0 | -7.066 | -48.02959 | 2024-10-03 00:30:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| e7de82a1-dc1f-3520-bd4a-e1b1bbccb3b9 | -7.01239 | -45.66002 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 77332027-b6cc-37fc-9d31-af1625c06f9b | -7.0028 | -45.50437 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| cbca8626-2cf8-32e8-ba28-705eb35f00e9 | -7.00114 | -45.49172 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| ca86f224-7687-3599-adc9-de7af0ffe601 | -6.99232 | -45.50576 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4ada2711-938e-3e55-830e-a0a66698ec3d | -6.99067 | -45.49306 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f54299ac-b54e-3908-bf3e-069ee038f706 | -6.89049 | -44.28599 | 2024-10-03 00:30:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fc89b344-8b01-39a3-9645-18ba13c132dc | -6.88087 | -44.28734 | 2024-10-03 00:30:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 154fd65f-33f8-363a-95f2-30e47b8cdd0c | -6.68084 | -44.53452 | 2024-10-03 00:30:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c20622ce-ce43-3e88-9274-7a20c5ced9cb | -6.57743 | -44.22858 | 2024-10-03 00:30:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| fabd7706-7135-3e03-9195-6a1f22cc4091 | -8.92381 | -45.63313 | 2024-10-03 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 776e9ccc-f855-3312-8753-4368e382d203 | -8.85101 | -45.52267 | 2024-10-03 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| a316b212-5a81-3393-aec9-ac0fac1c47c3 | -8.8618 | -45.52125 | 2024-10-03 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1b3d8ec1-0fd1-3620-86b4-147d4eedfe22 | -9.25776 | -43.49789 | 2024-10-03 00:30:00 | TERRA_M-M | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 03123603-fe5a-3627-9381-49fd8f4d819a | -9.01406 | -40.26573 | 2024-10-03 00:30:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 37f38dd1-26f1-37a4-a803-4dd41f459d9c | -7.70586 | -42.98185 | 2024-10-03 00:30:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 74106dd3-79d8-3fda-aaea-660fc0939ab2 | -7.70714 | -42.99125 | 2024-10-03 00:30:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 41.5 |
| 7adf715c-5845-373c-bfe2-833b0af61537 | -7.71598 | -45.42456 | 2024-10-03 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dd411289-bba7-37e7-a903-8f6f881eec25 | -8.84926 | -45.50909 | 2024-10-03 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 517300e2-9a18-32c6-b98d-839688893f7f | -7.69805 | -42.99253 | 2024-10-03 00:30:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 1465f627-4abf-3c7c-8a8e-11d0b64c9514 | -7.69676 | -42.98308 | 2024-10-03 00:30:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 588379b3-39ac-3cb0-b91e-b7b2950a6d3b | -8.93645 | -45.64545 | 2024-10-03 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 79bcad03-c1b4-3433-aa56-c2cffd3698f1 | -7.65913 | -45.20675 | 2024-10-03 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| be92966c-514a-3173-81e5-7e8c69e919f7 | -7.64879 | -45.20815 | 2024-10-03 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| be06a25a-0e40-3f34-9f52-47aacaec3e3c | -8.93469 | -45.63157 | 2024-10-03 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c6d4a2b2-a0cd-3334-b3e4-915cd05674e9 | -8.92556 | -45.64708 | 2024-10-03 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d290cb15-08ba-3a9c-97d9-df8037a28b6c | -9.49884 | -43.16902 | 2024-10-03 00:30:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 6ae42f5c-9c4a-3cf4-8e62-67650abfc42d | -9.47539 | -40.39902 | 2024-10-03 00:30:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 718aaeba-b800-3878-bce0-8be9437bf475 | -9.46267 | -40.37323 | 2024-10-03 00:30:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9d853e74-703b-3042-b95a-8f1f7073b604 | -9.45505 | -40.38358 | 2024-10-03 00:30:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 8cf2cafc-5e14-32bf-b3a8-085f265760e0 | -9.45377 | -40.37453 | 2024-10-03 00:30:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.8 |
| bf2e335a-9987-32d2-92d1-f0313aefebbe | -8.43837 | -41.9399 | 2024-10-03 00:30:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 530b3fe0-c273-3f9c-ba69-88ea35eba14b | -8.43713 | -41.93091 | 2024-10-03 00:30:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d0346d0f-bd11-36c0-bb5a-22ab01a62079 | -8.42948 | -41.94111 | 2024-10-03 00:30:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 642a9763-629c-333a-bb1d-a21904698e22 | -8.33793 | -45.35071 | 2024-10-03 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 363ac287-1a5e-3f76-a24d-1d35ab33067c | -8.33304 | -45.35775 | 2024-10-03 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 460123c8-be32-375b-98c7-da8c4e188d9e | -8.33131 | -45.34487 | 2024-10-03 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fa976cbe-8b63-362d-9ee3-6d2b12fad25d | -8.32741 | -45.35252 | 2024-10-03 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ec716836-f070-3512-985a-d673c0d8bf0b | -8.31048 | -42.82622 | 2024-10-03 00:30:00 | TERRA_M-M | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6ade84c3-6053-3a1f-bd8c-b9710c1ac684 | -8.21582 | -41.40262 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cffc36b2-33c8-3d0a-9318-ac8c1d4f01e8 | -8.19048 | -44.37632 | 2024-10-03 00:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7e544b92-ce05-3ea2-8687-0bb7050747e9 | -8.18897 | -44.36515 | 2024-10-03 00:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 4ebe508e-9916-3562-a6f5-1f8169666303 | -8.18368 | -44.40026 | 2024-10-03 00:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5c06607c-f41c-36a8-98b9-7e3d5fdfecff | -8.18215 | -44.38888 | 2024-10-03 00:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ce79eea4-66e5-3a6f-a4f9-a6a8e96b5cbe | -8.18109 | -43.69938 | 2024-10-03 00:30:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| e54e595c-2551-3ee7-b51f-53030f76c632 | -8.17971 | -43.68916 | 2024-10-03 00:30:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 967d5b70-b881-3f6e-a65e-f4f4822d2963 | -8.16357 | -43.71222 | 2024-10-03 00:30:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 299a87fa-a8bf-3a52-b36c-ec1048eb4381 | -8.1622 | -43.70204 | 2024-10-03 00:30:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 900c089d-176a-3895-8678-3de9aa7ebff6 | -8.15276 | -43.7034 | 2024-10-03 00:30:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 982c9c46-5e80-3ee8-99a9-ec8ad5d8c72c | -8.07955 | -42.88608 | 2024-10-03 00:30:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f4018c89-06f6-3428-a7c9-0b6a78ab97a7 | -7.86776 | -43.09209 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1c670ee4-2041-3dd5-b548-4154168edf8d | -7.86555 | -45.32708 | 2024-10-03 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5fe74228-4b78-3b58-9818-086c80e80338 | -7.8599 | -43.10292 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| cc489f3b-0de8-33f1-b3b4-5b3c9944c338 | -7.8586 | -43.09331 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| fec58ed7-0299-3fdf-b649-bc6d13c11020 | -7.85731 | -43.08368 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 3f3e750b-58f5-3b6b-93c0-e4a35450f418 | -7.84688 | -43.07537 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7c7e1e8f-83e9-3ad8-bb2f-13f703ad3da6 | -7.81215 | -43.0865 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 9a6ea73c-07bb-3005-967d-a8381e712b93 | -7.7626 | -43.0643 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d44192ee-1514-30b7-8cd0-e92828111200 | -7.76131 | -43.05477 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2521b4fc-a84f-35ae-a30d-77ada61ef2d2 | -7.75767 | -44.04161 | 2024-10-03 00:30:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ae7de7b9-bd1c-3453-a3fa-b1e473e12df0 | -7.75347 | -43.06558 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c9bf052a-1705-3395-b995-4736e9ed6ace | -7.75219 | -43.05605 | 2024-10-03 00:30:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 553dd124-e6e4-313d-a6e7-227014df294e | -7.63489 | -42.4645 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 7e1e7d12-8d1d-3719-9d6a-90e65327fb08 | -7.63364 | -42.45543 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 115f6dfc-6e87-3d7e-959b-854b9065b57a | -7.58035 | -45.007 | 2024-10-03 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 75c0adad-a82e-3094-8f3f-faf389c33fff | -7.49655 | -43.93624 | 2024-10-03 00:30:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8f0d583b-8a66-3566-bd3e-52354f1e00e1 | -7.48703 | -43.93738 | 2024-10-03 00:30:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bdee15a0-be71-318a-bf71-28831d7b21f7 | -7.29461 | -42.26416 | 2024-10-03 00:30:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 32485030-87ee-3d4b-97fb-c8d3455941f3 | -7.29337 | -42.25518 | 2024-10-03 00:30:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1bfbe9e8-2ed6-32e6-891c-f8082a6a22c9 | -7.20289 | -44.16471 | 2024-10-03 00:30:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e58f3b92-33bb-3d9f-b888-412c9a84fd95 | -7.20146 | -44.15408 | 2024-10-03 00:30:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f258a140-8241-3598-b0ad-35d70d6f4bc9 | -7.14938 | -44.23204 | 2024-10-03 00:30:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 955d84ab-b865-3a6c-ac5f-76bf53d6bb95 | -7.00567 | -42.5776 | 2024-10-03 00:30:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a22dc64e-2360-3c6e-b5ce-30af5e25b232 | -6.88157 | -43.61789 | 2024-10-03 00:30:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 302a9007-f622-3c7f-b2eb-cacc29097999 | -6.88023 | -43.60807 | 2024-10-03 00:30:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |


[Clique aqui para ver as próximas entradas](README17.md)
