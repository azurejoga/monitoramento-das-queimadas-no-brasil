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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbcda099-7273-392e-affb-bf442c5f27de | -6.64737 | -43.19852 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5fc66173-d982-3f8c-9582-aaa4f0c9fca7 | -3.45233 | -48.88741 | 2025-07-10 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b87dba2c-f1d6-358a-9a7c-7824e72df44a | -6.23848 | -43.36796 | 2025-07-10 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecc13cd2-6fd4-316b-a868-4a84ee5335d1 | -5.76328 | -45.79826 | 2025-07-10 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fd61021-dfcf-30db-b015-3d57c11353c2 | -6.95615 | -42.72202 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c33b54c0-de93-363d-b7a3-65c0f774a5ee | -4.222 | -47.2086 | 2025-07-10 04:02:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d1b89110-0e6f-3895-b8a5-735e16c37251 | -6.69016 | -43.14129 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8386c16b-74fc-3778-bb01-0cad995e1e54 | -3.98691 | -42.59842 | 2025-07-10 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4052a25-84ff-3153-aa83-0654bd8559df | -5.41636 | -46.07251 | 2025-07-10 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f48e812d-bfbf-30ae-b75e-b582fb7655b5 | -6.99804 | -43.51772 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bbfe0bca-0403-3750-9df4-c5b4e093dca3 | -6.9539 | -42.71347 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b3d72a41-933a-3a84-ab54-f853ce43d798 | -6.98988 | -43.49866 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49e96f4f-8a73-3076-a0fd-f5494664fb7f | -6.86645 | -42.78109 | 2025-07-10 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 39aa6066-bd13-38b5-9667-79a80b5908e7 | -6.85354 | -42.80086 | 2025-07-10 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e68e3aa6-47dc-3a58-a636-a74fe79c46c3 | -6.99935 | -43.48709 | 2025-07-10 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d654fe9e-5d20-3695-92ff-d13540732576 | -5.20352 | -37.66669 | 2025-07-10 04:02:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 35d5b3f5-d9d9-39ef-a0c1-e4e3f02ae69a | -6.64873 | -43.19021 | 2025-07-10 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 88ddd272-4377-3f36-9181-5b723658b553 | -5.48955 | -45.34661 | 2025-07-10 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a39c2aa-ff7d-3ba0-be2a-452579c6f16b | -10.65783 | -49.45942 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9f5a0440-4635-3e3d-bf79-4708b5c7312d | -13.89901 | -42.13585 | 2025-07-10 04:04:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5742cc56-2886-3426-a448-ad243afc3b8a | -11.05874 | -45.87368 | 2025-07-10 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 251e2710-b2ba-3d9b-b5b6-8c74ac25a5b6 | -9.32051 | -49.2253 | 2025-07-10 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a06fccaa-673d-3482-b838-5e27f7d8a970 | -11.46198 | -45.10735 | 2025-07-10 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6e1bc48-b2d8-384e-a689-15bdfc9677db | -9.30587 | -44.84343 | 2025-07-10 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b96ee1a-11d5-3106-ac02-a65f4d654d5e | -10.6618 | -49.46645 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5aec36c7-e65e-34fd-a44e-b9f2a1e8d472 | -7.7443 | -43.59032 | 2025-07-10 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8401c9b-7560-337f-ab03-5f70d9ca2803 | -10.65615 | -49.46853 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c4e2975b-d854-364d-bdf1-5d25b935e3b2 | -12.22157 | -44.20776 | 2025-07-10 04:04:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de4285d9-092a-3616-a130-b9124275dc52 | -13.00007 | -46.28514 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e59259f8-6d0c-3b26-97b8-a01a949b69f6 | -12.13514 | -44.99593 | 2025-07-10 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a7eb57cb-1ef0-3f63-b42c-75e8542a4f5d | -7.46712 | -49.40054 | 2025-07-10 04:04:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4452f4c-6e1e-318e-8bf4-225a351643b5 | -12.03781 | -48.75753 | 2025-07-10 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1dee617-4ab1-3272-8769-72ccd7c2ec20 | -7.20181 | -45.35146 | 2025-07-10 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c221b9f-4938-3766-89a5-f88e7585c400 | -13.33598 | -52.91739 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 515f2a70-d64e-3854-b2ef-bd2cf1327966 | -8.50107 | -43.30074 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 7e158510-2994-36a5-b77a-593fdf9f72fe | -9.83382 | -41.4987 | 2025-07-10 04:04:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 210f7e1a-b3b3-3148-8e6d-5eae47f544bd | -8.50423 | -43.32641 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 49170fd8-1eb1-327f-9e97-1e3335f9acfe | -8.50331 | -43.30949 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 54939238-1251-38ee-a5dd-fb5f11de8d1c | -7.71168 | -43.74071 | 2025-07-10 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7cd304e1-41ab-3327-ab6d-29e59c311383 | -11.8282 | -48.21239 | 2025-07-10 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7849443c-3b7b-30d3-80ab-cbe6d29a4bac | -10.57 | -49.1514 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 31b348f5-e4d4-3d03-aeb2-3e1cf1459cee | -13.16284 | -47.27898 | 2025-07-10 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73389dc0-8ae9-3157-980c-785496c168b9 | -9.83105 | -41.49462 | 2025-07-10 04:04:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3e82c7f4-508b-300e-ae1c-572cf18f84ba | -8.50946 | -43.30482 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 5c8e58e7-a8c3-309d-b21b-cb66fdb4a5f2 | -10.89911 | -46.73632 | 2025-07-10 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ab6f401-8fc5-37fe-a8b7-23c8eda828c1 | -8.23335 | -44.92957 | 2025-07-10 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b752001-f67d-3df0-8541-ce491f247cd7 | -10.62343 | -45.23278 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36bc5523-eef9-36bf-a844-ee693557b287 | -13.01432 | -46.31996 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18f0a5cd-2d9a-3f79-9bcc-7ca4e9bda050 | -10.56711 | -49.13914 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 04a2a90e-39d1-3426-94f3-f5e8c25a06cf | -8.28291 | -42.27114 | 2025-07-10 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3ee641b6-a389-30a7-a808-daf697ba7478 | -9.30203 | -44.84276 | 2025-07-10 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e1e7932-abaf-3d13-8ad1-b991c5160af2 | -12.42538 | -43.72066 | 2025-07-10 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7dc739c6-c895-35f5-b29d-860f7c3dbb56 | -9.32106 | -49.22218 | 2025-07-10 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35023553-f651-32e4-8b42-4e2210113887 | -12.43301 | -43.71795 | 2025-07-10 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdec42de-b2bb-3a31-a788-2850af2d8672 | -8.50397 | -43.30542 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 8c502630-e84d-3e46-bf54-d23581025db2 | -10.74587 | -40.82776 | 2025-07-10 04:04:00 | NPP-375D | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e4453d5b-22e9-38a3-ad37-80fdc969a227 | -10.62728 | -45.23349 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c0baa9e-56a8-3f3a-ad6c-34ee3feda927 | -13.04196 | -46.30256 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0dd4ac7-493a-31a6-a848-bff2cc044991 | -11.45769 | -45.10463 | 2025-07-10 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf32c5e5-9286-347d-add8-3f0aae4cc122 | -10.63498 | -45.23489 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff3172ef-fc0a-3b05-8bb1-c34b02830679 | -13.33979 | -52.90336 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cca7ee4-26be-3a3a-9e2c-b42c237f074e | -7.48138 | -43.9369 | 2025-07-10 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48c0c2f9-e656-3834-a21e-79b6bffff8d8 | -8.21816 | -46.96025 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fa6d629-b348-30d1-bdfd-47ccc367287e | -11.36388 | -48.70757 | 2025-07-10 04:04:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67f1e547-639d-361b-8c08-aa5ab784c024 | -13.01035 | -46.31925 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14048a41-cc3d-3ea6-9644-5d50760e32f4 | -10.61958 | -45.23208 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98884a3a-85c0-3267-891d-62adb72c0302 | -13.03794 | -46.30221 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 433efdfb-150b-3dcd-9160-1420c555e457 | -11.75314 | -48.3468 | 2025-07-10 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8762977f-bab0-390f-9f43-2cd46d637aac | -11.95199 | -46.36315 | 2025-07-10 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c41a7311-d3b7-3240-9a70-9d903842c4c3 | -9.29436 | -44.84142 | 2025-07-10 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e49d508-0ad3-31f7-9074-f8c2479a407d | -12.43236 | -43.72189 | 2025-07-10 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2251d8bf-e840-3826-a345-516e4e582902 | -13.67885 | -44.22129 | 2025-07-10 04:04:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a948449-79fa-32a8-af13-c0d45c5fa227 | -7.95392 | -49.65224 | 2025-07-10 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7977087-bda8-3d34-80dd-a83a885d5695 | -8.49883 | -43.29199 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8334a85e-ee03-397b-b68f-1e85b5d1ee76 | -9.21127 | -48.59932 | 2025-07-10 04:04:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ac25148-de2a-309c-956c-dcd3312663bd | -8.50589 | -43.30423 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| e950042c-7923-3afb-a321-380f5ce02ea8 | -7.95454 | -49.64871 | 2025-07-10 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90a42584-9aca-380f-8a0a-f5ff69d9e69f | -8.49659 | -43.28326 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| f8623389-3a0b-3ea9-97f2-c7d5a44956e9 | -11.00653 | -42.77976 | 2025-07-10 04:04:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9551fac6-03ae-3341-aadc-6dcbe4527836 | -10.57424 | -49.12843 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 826a3e2b-b363-3f85-98a5-67ed7296f2fe | -14.85846 | -45.12687 | 2025-07-10 04:04:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38f3d354-e9d6-35a1-80bd-65cdb15a1aa3 | -8.50247 | -43.3246 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 757c000f-4dc8-3305-9024-b1baf2699946 | -11.95263 | -46.3595 | 2025-07-10 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e68c219-c433-3ffc-978b-eb054f456544 | -11.87982 | -40.95298 | 2025-07-10 04:04:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 876656ec-a9ba-3ff3-9071-b00b4d63af91 | -13.037 | -46.3075 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edb1657e-5e8f-3a7f-a80b-b120bb4ef9ba | -7.11484 | -47.83566 | 2025-07-10 04:04:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb4f9ea0-99c4-385b-a4bd-1cc70f127f9d | -13.15793 | -47.28208 | 2025-07-10 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f00b9676-a17d-32a3-88ab-181d14538fea | -13.02094 | -46.28278 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de4030b9-62e9-3f07-815f-d4225df6173b | -13.00943 | -46.32441 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5117158-3cc0-33da-bcc6-9194cdeb4d3e | -13.37032 | -47.89397 | 2025-07-10 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ca94e73-311b-39c8-9e25-68c14fcc4ffe | -9.09179 | -47.9705 | 2025-07-10 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33c3f8c0-4f9d-3baa-b04b-0859fa1f744e | -12.42887 | -43.72128 | 2025-07-10 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9f28180e-c663-3f29-afda-0428a0488e10 | -8.86012 | -47.94983 | 2025-07-10 04:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0e98793f-804a-30ec-9783-dfd173204e68 | -13.00404 | -46.28581 | 2025-07-10 04:04:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17e5bee5-3041-3502-afb9-8cb57c0a7b75 | -13.16208 | -47.28316 | 2025-07-10 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fb9cafb-bc5f-3612-b710-a21e2ed4f2c1 | -11.06271 | -45.87446 | 2025-07-10 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c80f7ae8-7048-3e75-85a8-d76f2070441f | -14.86208 | -45.12753 | 2025-07-10 04:04:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 993537c6-dbda-39d5-8dca-7574c1adc471 | -8.50452 | -43.31237 | 2025-07-10 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 2950e404-ebf9-352c-910c-17dc6d0a0529 | -10.66799 | -49.46136 | 2025-07-10 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da2601eb-05ab-3af6-83d9-88c7d5714cb3 | -13.34268 | -52.88954 | 2025-07-10 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README13.md)
