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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 354c1acc-e60e-3ffb-9754-a6bd060c1b80 | -10.45347 | -47.85734 | 2024-10-15 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6d7f07b-94d6-3f6d-9c30-faa9b1d87083 | -11.58316 | -48.43313 | 2024-10-15 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 336f1c2a-b1e5-3ce4-8a30-346af2902227 | -10.94492 | -47.77544 | 2024-10-15 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c938047f-5e29-3262-8d18-6d7af1b97635 | -10.15267 | -49.36324 | 2024-10-15 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff5760e9-71a7-350f-bf1c-f1d19b01c5fa | -10.51798 | -49.78652 | 2024-10-15 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 081875a3-7ba2-3076-9633-b62ce92c6b68 | -10.51738 | -49.7897 | 2024-10-15 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df73cabc-c169-39e0-b027-b029f2aa2141 | -10.45227 | -49.36258 | 2024-10-15 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 917f1cf5-974a-388c-98b4-dfe166bffb77 | -10.45171 | -49.36554 | 2024-10-15 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b558538c-d2fd-3f60-b2af-1296d10e6d49 | -10.35347 | -49.62016 | 2024-10-15 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89615175-76d0-3ad9-97a2-87aaa653c61f | -10.34833 | -49.61922 | 2024-10-15 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cce25e3c-02f7-358b-bec8-45a78ee237ab | -12.11109 | -50.25114 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8540e439-bbe8-30b5-aa32-c62a01610dfe | -12.11048 | -50.25435 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a1643b8d-5b34-352a-923c-2434967e6dc7 | -12.10988 | -50.25757 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9488e61c-aff0-3c3e-abd2-9936a242eedf | -12.1059 | -50.25013 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 5f0ed813-ce13-37e0-9aec-2655a3f18262 | -12.1053 | -50.25334 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 7ec9b974-433a-39f8-a576-9c6efc3ee721 | -12.10469 | -50.25655 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 01931d4c-9daf-326d-b8a0-a28b0902baa6 | -12.10408 | -50.25976 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 501533ae-97e6-3db3-b2b6-4a4fa54e267b | -12.09889 | -50.25875 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae3322a3-2ba3-380a-885d-35342b7a2686 | -12.09828 | -50.26197 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c41cec1a-4217-3093-a46c-68163a89cc8e | -12.09767 | -50.26518 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 649e7e14-3935-37da-8ecb-c24b9f0c2436 | -12.09308 | -50.31792 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fcd0f95-8cf3-3dcf-8c49-c90303b6b589 | -12.09246 | -50.32117 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c3be111-8e52-3e43-a868-1556b8a29925 | -12.09184 | -50.32442 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10b9c773-916b-393b-9d4c-21412ef50054 | -12.08663 | -50.3234 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86193396-5578-3e32-9deb-899e5a55d3ec | -12.08142 | -50.32238 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb94f74f-725b-320f-b2a1-77ee7d6a2949 | -12.08026 | -50.2718 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 6791431c-ee4a-361c-b288-faea1013f2c7 | -12.07964 | -50.27502 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 951f36da-bbf4-385c-9237-1b3eca3f9b66 | -12.07903 | -50.27826 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 067f86ca-f634-3f7c-88c8-bdf57e2fdaf5 | -12.07683 | -50.31812 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28c6496a-46cb-3a66-af84-668ac4dc15b2 | -12.07621 | -50.32137 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ea51367-4902-3ddf-995e-a5d54814b842 | -12.07506 | -50.27078 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| a87e201d-053c-35cd-a2a0-62145e7b4af7 | -12.07444 | -50.27401 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 16ce36f2-e890-37d2-9705-6cfe8243a08b | -12.07383 | -50.27724 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8b0ab1db-1a4a-3cb6-8230-97f2638e2a0d | -12.07321 | -50.28047 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19475e62-5b55-3427-9d54-595012b39ee5 | -12.07285 | -50.31062 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e30b62db-dba4-3686-9731-1e33b4f6a174 | -12.07223 | -50.31387 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e97477f-6ba5-3543-8128-a83363b0218c | -12.07161 | -50.31711 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 848f9f2e-d456-3318-a3d4-2fa4c5e80bac | -12.06826 | -50.30636 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21378cf4-e39d-393f-a234-7c2a978b1435 | -12.05814 | -49.48331 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc03ea8b-d7c1-3ff3-a53c-923ae5a1e29e | -11.60334 | -49.86933 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b38b59b6-3cd1-3519-8b49-944c7237683f | -11.58878 | -49.83467 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c04227c0-9ffa-3182-93b1-e2c24a41b2c2 | -11.58368 | -49.8337 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97528de5-d045-3cb7-9a24-5c54b8da9bd2 | -10.66819 | -51.82368 | 2024-10-15 04:04:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bae7383-9059-3bf7-af15-e839bef209ec | -10.66733 | -51.82806 | 2024-10-15 04:04:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db57d7ce-52eb-3bb1-9da7-bf0113514601 | -12.08315 | -51.05989 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4449009-1870-31b8-8d12-f742c2684cd1 | -12.08276 | -51.05961 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91ac56a4-6d1f-3acf-b5b6-6ac423a2e64a | -12.08243 | -51.06353 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c8abfb2-6067-3921-ae8c-fb1117d06c89 | -12.08206 | -51.06326 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cdc7a9d-159b-36f5-838c-092373a75fd7 | -12.08171 | -51.06716 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b4dc505-e444-35de-96df-9fbf1013c8b7 | -12.08137 | -51.0669 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94a7c60f-b0e1-31a6-a961-383827ddcb48 | -12.07928 | -51.07784 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e1cd05e-ca7a-3540-a1cc-6a0bacd6b90d | -12.07624 | -51.06608 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b740eca-ab70-390d-b9d1-8c8d98264a3b | -12.07552 | -51.06972 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6d24d45-4023-3ad9-9898-1e70a630f0b5 | -12.0752 | -51.06945 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c967d049-a574-35e0-b406-beb465bf1b1e | -12.0748 | -51.07335 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8ebcd05-9899-314d-9a1b-46853a3122a8 | -12.07451 | -51.07309 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 285d4712-c785-3f2c-b527-b886d0e93108 | -12.05105 | -51.10644 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7dfd9c86-b8b1-3ad9-82b3-0aa4943ce434 | -12.04556 | -51.10535 | 2024-10-15 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96781537-20b9-31da-aa35-f5725a2f5ba9 | -11.23869 | -51.5211 | 2024-10-15 04:04:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67f159b9-5af7-3f6d-8708-191e9726fb02 | -11.23789 | -51.52512 | 2024-10-15 04:04:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91b8f431-baca-3a8e-b8be-a642666a44a4 | -10.20252 | -52.31852 | 2024-10-15 04:04:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 164724f6-a2f1-39c3-87f8-fec0d8b6da51 | -10.2019 | -52.3212 | 2024-10-15 04:04:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4010db4-2c97-36a0-a4ef-edb6df4b5a1a | -10.20158 | -52.32322 | 2024-10-15 04:04:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5da2643d-9eef-3ea6-bb52-8e62dc67c435 | 1.0199 | -52.2162 | 2024-10-15 04:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9f26092b-6bba-3df0-b707-398571671ac5 | -3.1099 | -54.2263 | 2024-10-15 04:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 4d2263a7-fe78-3b68-992f-115901a49f67 | -3.1283 | -54.2259 | 2024-10-15 04:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| cfe3df72-ac1a-3b46-856b-240a4e734457 | -3.9265 | -42.4246 | 2024-10-15 04:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 162.9 |
| e0f27c3c-f954-36ea-b5bb-5efb013ceb22 | -3.9267 | -42.401 | 2024-10-15 04:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 189.2 |
| 07a6976d-4450-3b71-93e3-aa74928609b7 | -6.5691 | -48.2395 | 2024-10-15 04:05:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 81b84fa1-c15c-32c3-9282-de4c6dbadcae | -6.5878 | -48.2381 | 2024-10-15 04:05:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 99.3 |
| b54722b5-869c-3494-946d-4eea2c01aabe | -6.6701 | -49.4586 | 2024-10-15 04:05:44 | GOES-16 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b9cab74a-a4fc-3287-b168-2f405a25a1c2 | -9.4556 | -44.1763 | 2024-10-15 04:05:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 523ba8d2-17bf-3984-abb1-f6d70e69eddf | -19.64871 | -40.47822 | 2024-10-15 04:06:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ee4f40a7-8713-3377-81a2-bd5b2c14316f | -19.64583 | -40.47341 | 2024-10-15 04:06:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ee1a9c5d-235b-39ff-b341-e261c0f108b4 | -19.64523 | -40.47762 | 2024-10-15 04:06:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6f677049-52f1-33c0-9cca-b3a946a946a5 | -19.64465 | -40.4817 | 2024-10-15 04:06:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| da0c1c13-d140-3430-9002-efc24e47daed | -19.64235 | -40.47285 | 2024-10-15 04:06:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 40aa4114-25b5-3b12-bfb6-4537fb7201fe | -19.64175 | -40.47704 | 2024-10-15 04:06:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 128bef7b-46b3-3cb7-b2ec-fa061a20c307 | -22.30515 | -41.87951 | 2024-10-15 04:06:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8ccbcb3e-7b6e-3844-b7bd-5056d3fd54bb | -22.59922 | -42.21516 | 2024-10-15 04:06:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9652923f-efe8-331b-9b5a-69ba413ac856 | -20.35867 | -43.55599 | 2024-10-15 04:06:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7330d08b-adeb-3774-bd69-6085567e5db7 | -22.72904 | -42.89523 | 2024-10-15 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d95745f1-52aa-3fd8-9de8-15fdffd21230 | -22.72847 | -42.89901 | 2024-10-15 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6801d19-3469-3dde-87d6-b5445c06e8b8 | -19.43778 | -44.34047 | 2024-10-15 04:06:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6385b11a-5e08-3fbf-8c92-7bcc34e1c9da | -19.34497 | -44.51499 | 2024-10-15 04:06:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3ccd55a-93cb-3c37-83b6-159f07ad8710 | -20.57816 | -44.57318 | 2024-10-15 04:06:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cbe9d2b2-83c6-3817-9b20-41138b605af4 | -20.30041 | -44.44109 | 2024-10-15 04:06:00 | NOAA-21 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4183ccee-d08f-3aa8-ae73-848a3da89e39 | -20.02022 | -44.59722 | 2024-10-15 04:06:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49080fe4-8c02-3963-b35a-918bf51bef6d | -19.98098 | -44.68809 | 2024-10-15 04:06:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9078e23b-68e2-3c22-8814-8c8d86178179 | -19.86704 | -44.95261 | 2024-10-15 04:06:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bfd2487-c50b-318b-938f-3b0fdc0afcc9 | -19.76574 | -44.25234 | 2024-10-15 04:06:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6b9c5bc-1518-34a8-82b8-ad7225d702a3 | -19.71235 | -44.05915 | 2024-10-15 04:06:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c1326e6-8bb8-328b-8cc0-25b5be65733f | -19.70962 | -44.05483 | 2024-10-15 04:06:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25320591-8ae7-3c14-9ff9-a056b6735d88 | -19.70901 | -44.05856 | 2024-10-15 04:06:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e09c5673-68e4-3e1d-995a-4c225e130382 | -19.51379 | -44.27679 | 2024-10-15 04:06:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75decbd6-c1e6-38ba-ac30-ed4d425b705c | -19.84959 | -43.84348 | 2024-10-15 04:06:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8771e3f4-0dac-352f-ba02-58b97de7acf6 | -20.31198 | -45.58428 | 2024-10-15 04:06:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66e9d903-80d0-3d58-91a7-2d4815da3d28 | -20.05612 | -45.73875 | 2024-10-15 04:06:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e46e397-d86e-363e-aeab-458a7ed253c7 | -19.95779 | -46.0735 | 2024-10-15 04:06:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea5f7228-8f5d-3629-bacf-11e229b77c46 | -19.73746 | -45.32262 | 2024-10-15 04:06:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README34.md)
