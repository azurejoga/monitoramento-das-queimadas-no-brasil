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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 172bdf83-ec13-352a-a147-82f5637accfd | -10.30579 | -47.79848 | 2024-10-26 04:44:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a208909c-e231-37be-aba8-0e20538172c4 | -10.19821 | -47.63057 | 2024-10-26 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00727020-a67c-3205-8a91-22216c42785f | -10.19506 | -47.62522 | 2024-10-26 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b1f9137-646c-332b-8f92-73934e9d6f6c | -10.19054 | -47.62944 | 2024-10-26 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5d8bc94-c5f4-3b73-b52c-9a23ffc82974 | -10.18987 | -47.6342 | 2024-10-26 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5aebda5a-d775-316f-a405-30d1f56f0f36 | -10.05559 | -48.05901 | 2024-10-26 04:44:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d05631e-bad2-34e1-bdd6-6a591e5ea035 | -9.8186 | -47.85245 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 93baa2cd-d1ce-34fb-afcb-2b9b49f84fef | -9.78954 | -47.86688 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fef37924-d454-3a36-b576-9905f101e0b8 | -9.78535 | -48.29855 | 2024-10-26 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13a432d2-a4f5-3179-99d1-98d9a3c45055 | -9.78472 | -48.30289 | 2024-10-26 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7b0bb5d-96ee-3e15-bc86-b198a9389e34 | -9.77575 | -48.23518 | 2024-10-26 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e02c0049-8a94-3f55-af0c-c7eb609677bd | -9.7392 | -48.25826 | 2024-10-26 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a61f636-d23a-3d69-b934-8f0f2d70335a | -9.73856 | -48.26261 | 2024-10-26 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52112ebd-9bb0-3266-b737-0c23e3e11c47 | -9.73553 | -48.25769 | 2024-10-26 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e7bc6cf-d96b-3576-8088-6efb9f99b0cc | -9.73487 | -48.2621 | 2024-10-26 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2ceecf3-bfce-3632-be94-0c76a1bb44da | -9.7312 | -48.26153 | 2024-10-26 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 824977ae-e223-3158-a402-1ccdf2dd4e31 | -9.73054 | -48.26602 | 2024-10-26 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac5eb7a0-ab45-3706-b65d-8ed9d704830b | -9.63563 | -47.59503 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65dfc4e8-16e3-3a71-a598-1da0f038641d | -9.50442 | -47.81107 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36132452-ca74-3551-b967-ca9db3d4aa90 | -9.50046 | -47.80812 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 045abb5b-3bc3-3fb7-8a39-e3d4e77b7214 | -9.49978 | -47.81271 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bef2067-5b92-352a-9742-88158d5873df | -9.4991 | -47.81727 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fa5d178-2e9d-356c-a787-dc75cafd2f3c | -9.49689 | -47.81001 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01c4f317-5a49-3073-b8d6-2d5fd5e7c48a | -9.49602 | -47.81218 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 718ed224-43ef-3b90-8868-4933d697746d | -9.49533 | -47.81678 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e49986c-0c09-31fd-96da-ed954ba22e7a | -9.49248 | -47.81406 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad8e9b22-b216-334b-9c2c-d9d6c0b793ab | -10.88569 | -47.82304 | 2024-10-26 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2061d8a8-6df0-35b9-a654-c56279c039bf | -10.88255 | -47.81776 | 2024-10-26 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5c9bfd3-17e4-36ea-a02b-3e18a5a4d753 | -10.88188 | -47.8224 | 2024-10-26 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53115569-a183-3aa9-b3d7-6df0545c636f | -10.87873 | -47.81719 | 2024-10-26 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b373fd2-e8a3-39c4-a66a-d98fe5aa4d7a | -10.31027 | -47.79435 | 2024-10-26 04:44:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7acf6bbe-9c45-3bac-bbb3-6629e6d6ab46 | -10.19438 | -47.63004 | 2024-10-26 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a587b155-5a5d-327d-9057-4441347b9e1a | -10.1937 | -47.63477 | 2024-10-26 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c915161-0230-309c-9b75-52cf020a9511 | -10.19122 | -47.62465 | 2024-10-26 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e1c4173-2800-34cd-a537-0bc5af6492f7 | -9.99322 | -48.8087 | 2024-10-26 04:44:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 979e2c23-3b6b-388f-93fd-fba01d5e952a | -9.7213 | -48.88423 | 2024-10-26 04:44:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e47c76d-832e-3a33-b216-b7542a65303c | -10.29123 | -48.89142 | 2024-10-26 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f429192-da65-349e-80c6-41391371ceca | -10.29062 | -48.89555 | 2024-10-26 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8b89923-dc02-3fa2-b034-b7816c9d0c94 | -11.7578 | -48.36326 | 2024-10-26 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f911249e-d2d2-3fb4-a6b1-24889ad769f6 | -11.59531 | -48.47557 | 2024-10-26 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55e051c6-8552-395b-b31a-cbb97ac05d0e | -11.59159 | -48.47501 | 2024-10-26 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a644a79b-5be1-3472-9da9-16cfa3df7d39 | -11.59095 | -48.47952 | 2024-10-26 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2eece285-6fe8-3c31-9082-175fc5f4d586 | -11.43844 | -48.48358 | 2024-10-26 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5237057d-780d-3c2d-81f7-266c174efcad | -11.43473 | -48.48302 | 2024-10-26 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50efbf50-a351-3c36-a0b7-c05c44220157 | -10.95226 | -48.05626 | 2024-10-26 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 878b76a2-1de8-3c7c-9309-6c4c8d3138aa | -10.94848 | -48.05574 | 2024-10-26 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9699fb61-b467-3514-b9b3-f8421cd55db8 | -10.9447 | -48.05522 | 2024-10-26 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3feb981-8c83-357a-8d70-94f001c892e2 | -11.60391 | -48.60004 | 2024-10-26 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c61bf7d-8efe-3c5f-8d07-323a13a86316 | -11.60327 | -48.60446 | 2024-10-26 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d74c4cb-ecf1-3235-8190-8417cbaff94c | -11.2855 | -48.63527 | 2024-10-26 04:44:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 607b504d-a643-3f75-a8cc-828b29050e82 | -11.28249 | -48.63021 | 2024-10-26 04:44:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1b6d7d5-dc27-3729-a66f-b6ab26dec8ff | -11.04288 | -48.53085 | 2024-10-26 04:44:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75bdc192-003d-34ab-9a12-d219b5d9cf45 | -10.87245 | -48.80733 | 2024-10-26 04:44:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d9f51ad-a85a-3cd8-befb-eac687286b0c | -4.89218 | -48.64939 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4701b30-cd5b-3a78-ba5d-e25797048ebc | -4.88358 | -48.65956 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcb05374-a567-358c-892d-cffc8d785049 | -4.84754 | -48.64262 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eba68e78-c038-354e-949a-f62ca6886650 | -4.75198 | -49.24155 | 2024-10-26 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 152fdc96-c34d-322c-99ad-773e625e937e | -4.75077 | -49.20465 | 2024-10-26 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 746af34c-f404-38df-97d7-b572cc852148 | -4.30375 | -48.64916 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57a565ab-58bf-35f2-9be0-cf5fdbfac041 | -4.30033 | -48.64865 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5960955a-6a79-3284-bb7d-4707a200249f | -4.29976 | -48.65234 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 36d82703-8a45-3274-bfca-1c59d0a7658e | -4.29406 | -48.64393 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de48e928-28d9-3530-a4ac-70443fa87097 | -4.2692 | -48.64457 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 101c60d0-4cdc-3074-abf3-d741a06bfea1 | -4.89377 | -48.72961 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21c05955-96a8-356e-80a8-1ae477ef8311 | -4.88817 | -48.65262 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9e9c6cf-b362-3a4b-ab3f-27020705bba1 | -4.88644 | -48.66381 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41dc4010-560f-3a9a-9c53-a0d830cfe554 | -4.88301 | -48.66328 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b3da482-667c-3da5-a16f-a52f275cebdd | -4.87337 | -48.56598 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9079806d-42e8-305a-9fd5-c63faf4aabd7 | -4.8378 | -48.61438 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d401d531-a0ea-3173-b09f-1d0f319f52e7 | -4.75133 | -49.20105 | 2024-10-26 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3660dda4-099e-3cb0-a851-a4b3c9d401a3 | -4.71875 | -49.08987 | 2024-10-26 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bf61a86-8666-32d3-bbd8-07642fb58e98 | -4.71818 | -49.09349 | 2024-10-26 04:44:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3858a656-4d85-33b2-ab5f-ce78faf5854e | -4.36424 | -48.59771 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bd6d2b8-ea4c-33cf-a848-c42c9286d754 | -4.33908 | -48.62434 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a2738d3-1c87-367f-9918-c5bcdd11bcee | -4.33621 | -48.64286 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f09ad27-6d61-3d7b-8ad4-48803d0a14b7 | -4.33394 | -48.63493 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1439e4ce-61d7-324f-97d6-b691a6002bbb | -4.33052 | -48.63439 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 974b65ec-e743-3acb-9b40-c5518e8b6327 | -4.30089 | -48.64497 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5070888b-9364-3bf1-91c5-03306db0c33b | -4.2992 | -48.65603 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c5d650ae-dc11-3da2-b237-e79ffc96e2c1 | -4.29691 | -48.64815 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 029c5fe9-f5a1-3097-9e1c-750859ad7757 | -4.29634 | -48.65182 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3f384ec-e10a-34da-9d8a-f8e903b8f412 | -4.29064 | -48.64338 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 934cfafb-d6d2-3084-9a98-a4a83ccac915 | -4.29008 | -48.64707 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 240963f5-c9dd-3bcd-8e2e-28fb86f98f52 | -4.28895 | -48.65443 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc6ba4a2-c7ee-3db7-b5c4-76a7a26eaa1b | -4.28838 | -48.65814 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1439981-1b34-3fcb-8e18-38647668b344 | -4.27261 | -48.6451 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a50f026a-3df3-368a-bc8d-ce1f50b8074a | -4.24883 | -48.55037 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bfd4b848-6af7-3119-b037-799b30b0d869 | -4.23855 | -48.54877 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c56180a4-eada-3050-b616-e5cd00289364 | -4.23682 | -48.55998 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95e673e6-006e-3d77-8f2c-322be8a9d560 | -4.23397 | -48.55574 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 564530d3-36fb-353c-bda0-8faf4d92b3f1 | -4.17066 | -48.60293 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd9cddf2-0bc1-3462-b0ea-35cbb524a599 | -4.17059 | -48.60335 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a30f3dae-b892-391b-8b0b-66c3fc0e2958 | -4.16775 | -48.59914 | 2024-10-26 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6a1d4da-30fd-3bb2-abc3-0cfc28091268 | -4.1389 | -48.96857 | 2024-10-26 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17a5a36d-0b2e-3375-a8df-af195eae6224 | -3.99194 | -49.02715 | 2024-10-26 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2f3e33f-d430-3b1d-a38a-2aa588652652 | -3.9011 | -49.07923 | 2024-10-26 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0db449a2-876b-33a2-b9d2-fc4a4147ed30 | -4.13834 | -48.97217 | 2024-10-26 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ba5a6b9-62f2-374e-bd74-a5ef9dbd713d | -3.90166 | -49.07567 | 2024-10-26 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 53b8c164-9b92-3959-bd31-e3a07d865a57 | -5.13006 | -48.09521 | 2024-10-26 04:44:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dc3c675-0be5-326e-8456-6a0bede23a80 | -5.12654 | -48.09469 | 2024-10-26 04:44:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README79.md)
