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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21376036-8565-38c9-86a8-18227f6bb2f6 | -6.91342 | -43.52775 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8bac827-fcc8-3589-947b-a615ca9e4107 | -4.795 | -46.39917 | 2024-12-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 02d8bf0a-c373-3e70-b177-24fa57efd5a0 | -4.65615 | -44.32642 | 2024-12-17 05:08:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 76bb1f16-039d-3854-affa-a25e94ead01f | -3.52963 | -54.69072 | 2024-12-17 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bea7a939-effa-35ef-8c85-852e14dc9f8f | -5.2062 | -44.56488 | 2024-12-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 49192353-e4b2-30af-98e8-64ed3641227a | -3.33575 | -54.08204 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e019c1c-0b98-3588-9316-2a265fa22b0f | -6.9884 | -43.56634 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79e447b1-4c73-3774-94b9-b02551ae287a | -5.20587 | -43.29837 | 2024-12-17 05:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6ede915-3a34-3c39-b616-9e1287378b92 | -4.57258 | -46.58334 | 2024-12-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 173987a6-0cce-32ae-80e0-0332d4db261f | -5.62522 | -44.83895 | 2024-12-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dae27b70-66de-3f5a-9081-123634eaf85b | -3.96503 | -47.032 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8dd8239-a7f3-33d3-8796-3b35323c13cb | -2.93976 | -54.18155 | 2024-12-17 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 310e0363-26fb-3eaf-ae10-f9b41726d49a | -2.55388 | -54.70151 | 2024-12-17 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c426ed1-eee9-30a9-b5cc-7a2a523da229 | -3.08412 | -47.78191 | 2024-12-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 82236a3e-a87b-3d4c-abeb-01958848678d | -4.09736 | -46.72763 | 2024-12-17 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 146bc6cd-7ec8-385b-883f-f7891b514046 | -6.98441 | -43.56502 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 868ec9bf-4d96-3171-90c4-05c44fbdd824 | -3.78287 | -47.11908 | 2024-12-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e87cdf9-d42b-3c0d-b14a-254c58fe0a04 | -2.57638 | -49.41171 | 2024-12-17 05:08:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d9ea73e-faf8-39f0-b31c-ac905c66e574 | -5.20698 | -44.55933 | 2024-12-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ba412ee4-796b-3864-9243-e838076022be | -3.87325 | -47.04102 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2410048-ca7b-3d7d-b571-b4042cf6ffe2 | -2.68835 | -51.91331 | 2024-12-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cfb5dcc-c985-393e-b3a7-ff0f6b4466b3 | -3.30482 | -53.3693 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 451136d4-e3dd-39ac-96bd-507ed08e8431 | -3.23846 | -46.80341 | 2024-12-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 855a1e9d-741a-387c-bc9c-66a9b3828cd5 | -3.19227 | -52.89266 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32be7659-7724-34c6-ae96-842eea45c83f | -5.20978 | -43.30051 | 2024-12-17 05:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d0c4ee27-b35b-3561-befb-f3cc908652af | -2.77184 | -48.58072 | 2024-12-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db24495-ab9b-39cb-9ce4-0e7e7452950e | -2.62366 | -54.00563 | 2024-12-17 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d067a467-6f68-37b8-9dd4-690646a7041e | -6.9305 | -43.5083 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 13d64d3b-4ca4-3573-a0be-e6f18c2bf6c3 | -4.79547 | -46.3997 | 2024-12-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ae0e6494-9947-3f6a-a2c5-d786b2011852 | -4.88806 | -44.17657 | 2024-12-17 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4438ca7-2f1a-3eaf-a31f-912eda123199 | -3.29759 | -53.36822 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 27579cdc-47cf-3eaa-b346-b8b0b2107bf1 | -4.78954 | -46.39941 | 2024-12-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 305a5930-89d0-33b6-8b08-b08c3bee0b51 | -5.08526 | -43.91087 | 2024-12-17 05:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 60af4523-9f39-3a13-876d-14ddaf564790 | -3.11905 | -52.70037 | 2024-12-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d85d2fe-8183-3e9a-849d-8bd5b7a9ff4d | -3.02906 | -47.83056 | 2024-12-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bbade5a-4cc1-3af6-a966-b1c062fd6371 | -5.70438 | -46.79762 | 2024-12-17 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1cf63eb4-c934-375c-b760-cb2a67e038d9 | -2.75699 | -54.02927 | 2024-12-17 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2960fc1e-5b1f-3a04-85a5-1396f3947130 | -2.95294 | -52.3135 | 2024-12-17 05:08:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ce42427-4e6d-3835-b190-7a8523fb8783 | -4.79558 | -46.39503 | 2024-12-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cc69667f-221c-3bc3-bde5-00a1b26c2f73 | -3.76405 | -47.17117 | 2024-12-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e422d0b-f95d-36bd-9b15-f53d4bb89801 | -3.02491 | -52.52799 | 2024-12-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85417b0c-6ed4-3949-9013-00981d37cca4 | -2.68342 | -51.91512 | 2024-12-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 358a3f5e-9322-3fea-b325-e3aabbcf456b | -3.12246 | -53.2422 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a316f82-24cb-3f43-ba65-c4778e655a62 | -3.7834 | -47.11549 | 2024-12-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c2345e5-db71-3f05-86e9-593e249a7b7a | -4.65131 | -44.32893 | 2024-12-17 05:08:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 68ee7b86-b305-3cd8-970a-e3eb62d75492 | -3.10225 | -53.76458 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ec016d9-ebd8-3041-b446-53cd4170df2a | -3.43685 | -54.0538 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac16edfb-211f-3f51-927c-d2b9993aad93 | -4.81012 | -48.37475 | 2024-12-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c155494-4294-3b95-8bdf-12fa71e4ff32 | -3.30057 | -53.37288 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fddca015-93d9-3a00-9c2a-c1417cbc105d | -5.14146 | -43.23967 | 2024-12-17 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4854681d-4025-31ce-9e02-3cc235479f55 | -3.24304 | -54.09635 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ecb7cd6-9fc5-3cd3-9a09-8efc03124e23 | -3.95895 | -47.03478 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee24ec44-bc48-3f69-abf8-219fc305c66d | -5.07841 | -43.90994 | 2024-12-17 05:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b515222b-a907-3ad0-86e8-2912ee396ab2 | -4.06143 | -46.91162 | 2024-12-17 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb858864-4545-37ab-9c8e-717c721eed06 | -2.08382 | -54.23487 | 2024-12-17 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1def6297-c478-3901-97aa-c081fd0fcb71 | -2.46013 | -53.65952 | 2024-12-17 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66f50f03-ceb4-3baa-8da3-2e27476625a2 | -4.09685 | -46.73124 | 2024-12-17 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03ec9d47-7700-3f58-9e3c-d2636fb90f89 | -2.58583 | -51.92322 | 2024-12-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc230546-fa7c-3eec-adde-f9a9b58e4388 | -2.89409 | -54.17843 | 2024-12-17 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41891222-6fc2-30a8-93c5-ce0c4102655a | -2.77897 | -48.58396 | 2024-12-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c38bc3b3-441f-3bb6-bdf1-fb5baa0f8e28 | -3.44021 | -53.98647 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d3bfe3f-35a9-352d-8498-bc345ee25101 | -3.33224 | -54.08159 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f221e151-a8fc-3201-913f-8a56c1eac524 | -4.78966 | -46.39471 | 2024-12-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4e8b9110-06a6-38fa-913c-3d2cba19e473 | -3.18083 | -46.69255 | 2024-12-17 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 353ff199-c661-3651-9839-e0993d5b8f6a | -3.42421 | -53.22776 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| decbce35-a418-317b-8345-dd817c3c0994 | -5.13429 | -43.239 | 2024-12-17 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf3b97c4-8d62-350c-a072-65e2b8aac2d6 | -3.77005 | -47.16835 | 2024-12-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f376fe4-0c1a-3caf-81b8-baa854592040 | -2.93424 | -52.71673 | 2024-12-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2de7ed2-98b8-3395-a74c-0714583b1fe6 | -6.92333 | -43.50737 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e98411b9-7104-3897-bf2e-8e736ee4295b | -3.02418 | -52.5326 | 2024-12-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d38f524e-567a-3a1a-8ff5-47487a3f999c | -4.67151 | -44.04407 | 2024-12-17 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c7dcba2-6d03-35dd-8871-2932ba3d0489 | -3.43746 | -54.04989 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 835d8397-511e-330d-9c3b-a1159ab01e74 | -4.76123 | -46.71296 | 2024-12-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 013bacfb-e453-3db0-aa68-f86abc146ea8 | -3.30121 | -53.36876 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 41e3e1db-b762-3e02-948a-36fb8aae2ce1 | -5.0999 | -43.90594 | 2024-12-17 05:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7cbe5cef-0e01-3465-95d8-fb1bfd3d2467 | -4.96448 | -44.96626 | 2024-12-17 05:08:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b11e7c9-c8fc-3715-8a36-ff4211c7449b | -2.83353 | -54.05244 | 2024-12-17 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dada45b-ca19-3b6a-a399-cd90b63b2f3c | -3.48575 | -54.65742 | 2024-12-17 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bef80e9-88e2-38af-b50c-ccc6f1b2bedc | -2.77407 | -48.58321 | 2024-12-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50a41a9f-cbdd-3080-b0da-8b55b3482165 | -4.04303 | -46.9203 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb18b83e-5768-345a-b374-c96656f799f5 | -5.0913 | -43.91764 | 2024-12-17 05:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4cfebad2-575a-306c-9180-ccf7336c5003 | -6.9853 | -43.55801 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4be2380d-6a35-362f-8628-56fbcee1396f | -3.23754 | -46.80367 | 2024-12-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 04e74adc-3a85-39b6-97e2-c6fdc68e14c5 | -3.43378 | -53.98156 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88c3a574-e3ed-3481-9f6a-2db6e2db6585 | -3.08931 | -47.78271 | 2024-12-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76ff02dc-97d0-3510-b207-993b96405bfa | -3.66855 | -47.13149 | 2024-12-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e400ab7-56c7-33c1-91ce-22f2d2a1ed8c | -2.58691 | -51.92052 | 2024-12-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00c655b4-ebd8-323e-b5fb-54094c50fdbf | -4.79015 | -46.39526 | 2024-12-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 59ba5b21-94ce-361f-bfa3-a73bace11a4e | -4.88523 | -44.17424 | 2024-12-17 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62392ab4-8e78-3298-9e63-966b1e6d4676 | -5.36259 | -44.04808 | 2024-12-17 05:08:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc155f79-8211-39cb-b4c6-265aa9cfc844 | -2.07753 | -54.2301 | 2024-12-17 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a0e0fac-755a-378e-a62d-3486167fb7d7 | -3.15351 | -53.18967 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b389f214-0eec-3066-a57e-a76064124675 | -2.89351 | -54.18224 | 2024-12-17 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd5f9878-e652-3068-a653-4c89f1868369 | -3.19112 | -52.89101 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 707f9257-702f-39d4-89ce-abed2f70a9f4 | -3.18644 | -46.69338 | 2024-12-17 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 843d701c-60aa-3af4-8221-c1463eec1cfc | -2.51817 | -51.79224 | 2024-12-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 997a3f08-1d12-3053-993f-10e2f81c6550 | -3.86933 | -47.02899 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 25c8ed02-49b9-38d9-ba91-ca2a299bc033 | -4.0673 | -46.59579 | 2024-12-17 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8671193-4a5d-36c8-a566-d42fd2e02012 | -4.70202 | -44.38566 | 2024-12-17 05:08:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 245553a5-7843-31ff-a67d-8b53754dc5ad | -2.77836 | -54.49904 | 2024-12-17 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
