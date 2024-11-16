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
| b58e329d-8ecc-3c01-bcbc-1cfa88f7d53d | -4.37363 | -48.56617 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fba65c49-b8a9-3525-a4c6-1140c30a3030 | -2.55986 | -46.90108 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1a88ce63-a64c-3a9e-8418-ed435f8ca05d | -2.84609 | -46.62057 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d31b56ca-97e3-39cf-b3f8-a537ba01b5ef | -4.36853 | -45.62324 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| effb72cb-395b-36c1-ac47-b1681b3d924d | -4.10475 | -46.87913 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66f63d65-3423-3693-bf75-fc008407c2fd | -2.8567 | -46.66244 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c5f9ef5-dac4-3cae-8b75-39ad9f9a08c6 | -3.56447 | -47.37137 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 036800fe-cb4e-3035-9f8f-eb270a52bccf | -3.04031 | -47.97485 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba1b94df-cde0-3645-bd96-0ff22cbabc0d | -4.13677 | -48.22772 | 2024-11-16 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2908aaa7-0e7c-32ac-b310-2961309b4317 | -3.71512 | -51.84483 | 2024-11-16 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ad3c6cd-5288-3a95-b40d-9fdeeb69e58d | -5.67228 | -35.64196 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 8107b4f6-a936-3f30-9f04-0fc477188765 | -2.81439 | -46.65963 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2df7641e-e09c-3185-a66a-69db0cb6c82c | -3.42077 | -46.0944 | 2024-11-16 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cb4f3048-80fd-350a-bb28-ce5a93fcac20 | -3.79132 | -43.91372 | 2024-11-16 04:23:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 87368ecc-341d-3e2c-bd0b-93ca5023bfe7 | -3.81228 | -46.51029 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a0a2c6b-70ca-323c-8b72-d42d6382f08e | -5.33336 | -40.89857 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89f21887-7a2f-37b1-b386-50ff34ffceb0 | -4.90798 | -43.23381 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 537d0b5d-d133-3fd9-99f8-3b5f44bbc90d | -3.73046 | -45.65393 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33fdc4b1-6a5e-3cd6-a019-d2baa7edc213 | -3.12059 | -45.89424 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23ce60d4-bc18-317f-bc0e-3e7f35a6f652 | -4.18558 | -46.3718 | 2024-11-16 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a04fea39-28d8-397c-823b-7d73add865cb | -4.55642 | -45.76212 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 141b33f3-0079-3a06-bf07-6639ab4a1e5b | -5.66491 | -35.6469 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 037f5109-c154-3793-a7a9-90b800d9d18f | -2.64348 | -46.19463 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6570e361-b3ca-3db9-b239-c2fbc87b6de0 | -3.99329 | -45.85402 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f1801ad-a8c3-39c0-93d2-145e9b3e8f12 | -1.55476 | -54.31157 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 821dec9d-bccb-3572-a999-3efd6eb60789 | -2.50647 | -46.35661 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 025e513e-58c9-33c4-86cc-1ce686a23123 | -1.68775 | -48.46619 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8155be88-d2d1-3485-ba15-ca31f96c3574 | -3.76784 | -50.79041 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de87bae1-7a38-3284-9988-1910ec667076 | -2.22375 | -53.61599 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8769582b-b4f0-38cf-bb3e-0234b2bbc58b | -1.7055 | -46.16014 | 2024-11-16 04:23:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b21ecae6-3eb6-3e7d-9ad8-b06c7396bfbf | -1.17727 | -47.07541 | 2024-11-16 04:23:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b32fa430-8c31-3b50-a7e4-0be71d6fc646 | -3.12446 | -45.8913 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe2255cd-b597-36d2-ab9c-d75817aea47f | -2.15812 | -50.52101 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 315fd0e9-8f32-3b27-9701-ac236f4e4b2f | -2.22423 | -53.613 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 399da13b-3414-3528-afe8-7a8cf0f6e5d1 | -1.58098 | -50.43847 | 2024-11-16 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 373c7c34-5ba6-34e1-9e82-daf6e4d832e2 | -4.00764 | -46.58101 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2779be2c-2d87-3199-b023-d64d26280805 | -4.364 | -45.86292 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42ce6912-95ed-3602-b976-7327f5ddd328 | -2.21321 | -48.39938 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c34a755f-db00-3e0b-a052-9fad2738bb82 | -2.22982 | -53.61077 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| d16f5fc8-fd81-3d2e-971f-42acd0212376 | -2.47235 | -46.35492 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1df90aa-cbe9-31ab-8e0f-bf1e59afa954 | -2.37454 | -50.412 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b216f04a-60a5-3363-9208-c4773037e3aa | -3.3701 | -46.50238 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8247436d-8768-375a-a353-7fc24740de6b | -3.2531 | -46.53497 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfd6f295-9c62-3b5a-8b76-102a3e8960b0 | -4.37298 | -48.57016 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2d94503-20ce-3a3f-867d-14bcecbfd10c | -4.90659 | -44.03691 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38723847-e867-3a7d-b9b1-107a7faa0f20 | -4.90317 | -44.0364 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caf882fe-1c2e-3c55-8423-31cf8629ff86 | -4.83591 | -44.53708 | 2024-11-16 04:23:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d1d900a-1a9f-3e45-9bcc-9a712d35605f | -4.23023 | -50.6744 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7b0110f-fffd-37f1-a854-bfef17a1a231 | -2.96061 | -48.04316 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6e1cbc8-96ae-33e5-9ee8-e6fec0f071c4 | -4.01728 | -38.24892 | 2024-11-16 04:23:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b01cc99b-0cd3-3c51-a7cd-17152500fcf3 | -3.51839 | -44.72014 | 2024-11-16 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| dfb173d7-8bad-3afd-b040-00dec5d18dc4 | -4.30421 | -45.9883 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84299a99-6383-3938-95c8-d339d674cd9c | -3.79592 | -40.9975 | 2024-11-16 04:23:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6740408c-a333-3502-9adb-f8f45593d786 | -5.32932 | -40.89796 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ab7b38f-b8df-37ae-b6eb-0fd50bbcca70 | -3.09802 | -45.97245 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6c48182-9ec4-3d56-8d34-b7f5352f642b | -2.66303 | -46.84643 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 753eb5da-dd8c-3d16-9357-4759ac2e959b | -4.61833 | -45.34684 | 2024-11-16 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82ab14d2-dc50-381d-9ccf-0cefee281bad | -3.58571 | -44.85178 | 2024-11-16 04:23:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 219a1cc7-5431-34c9-87fe-9c588980f5bb | -0.81419 | -49.51861 | 2024-11-16 04:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75deb101-04eb-3922-9118-2c7f46d4175a | -4.03427 | -45.46434 | 2024-11-16 04:23:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb51e830-1aa6-374e-9a70-19b273af06c8 | -2.5106 | -47.47519 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6f8c15a4-aedb-30df-8c07-390d36d88a00 | -4.37463 | -45.62773 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 698586cb-5ea7-3a5e-b5e6-6a25abaf817e | -2.8172 | -46.66373 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5a818a8-797e-3cd4-8b32-eb132acfcea3 | -2.35749 | -47.14386 | 2024-11-16 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3268353e-a56c-3bbb-8ec0-285ef1a56655 | -4.38181 | -45.62531 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e1253ef-a842-3839-9bde-fdd295acbf75 | -2.61344 | -46.25461 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c9b251e-5485-3667-bbbd-8504d6244f22 | -2.61232 | -54.54157 | 2024-11-16 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23b26028-b714-3e46-ace0-7b5d6a5af857 | -3.24974 | -46.53444 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47fe1077-2376-3f35-9b24-a8f17b97825f | -5.67691 | -35.65091 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 16.0 |
| ef401b3a-56c1-3ea2-9ccd-d69f8d01bdfb | -3.24993 | -47.90164 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d52f9a62-4794-3a5f-9d4a-a406bf716343 | -3.16063 | -46.61854 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 687153cb-a689-37cd-9b94-aa4e2994b8f2 | -5.00571 | -44.3206 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98e8581f-24cf-3a11-8297-baf52923c4ee | -2.83366 | -46.65516 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50e70565-41f0-340a-9658-3be02ed8d764 | -2.03194 | -48.96769 | 2024-11-16 04:23:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed7b786d-ef13-3729-81c6-adc008baf091 | -2.6184 | -46.17993 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7030e3b-4ce4-305f-a435-f0071f80060f | -1.40228 | -51.09072 | 2024-11-16 04:23:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cf8aa6b-2f1a-3abc-81be-a7c4cca59caf | -5.12043 | -45.15863 | 2024-11-16 04:23:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ed45a11-b3b8-37c4-9c32-e0752d620541 | -2.6529 | -46.15664 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7649ff5c-5fc8-3dd1-b196-63f779e1b69c | -3.74205 | -45.66272 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2a586a18-950a-3fdb-87d9-c5281ecad9c6 | -3.98524 | -43.72142 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb903483-d2cc-35cb-9ee8-b5247a0201e6 | -2.02559 | -53.94764 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ced6bb9f-955f-32d3-8dfe-c372fea14c80 | -4.10532 | -46.87555 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa29fd68-d403-3b1d-bdbd-bceb288f3bec | -2.35936 | -49.11572 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6ae5532-5510-3e2b-93f7-2a5d9f294a23 | -2.62787 | -46.18499 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 865c37a7-9530-31de-9fbe-dae20d29c8c6 | -4.2498 | -45.90189 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e99489b7-baa0-38cb-bb2f-6414d4030321 | -4.57976 | -46.61667 | 2024-11-16 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ac83fef-cea9-3567-905e-09c743a99bd1 | -3.76725 | -50.79412 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9247056f-c7da-3c41-a8a0-5769058afeba | -2.6445 | -48.47876 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6bac71d-0742-326e-a93c-e883d0f684c6 | -5.32877 | -40.90159 | 2024-11-16 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c20d5a67-d0bd-34af-a130-e6c76f5dbe7e | -5.87156 | -40.17783 | 2024-11-16 04:23:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0243f835-178f-3b6c-bb0c-52d26cfc4dc5 | -1.71375 | -46.16114 | 2024-11-16 04:23:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a866b9af-ca76-3a51-9528-c346b0d49f7e | -2.73939 | -48.56196 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48ef2adf-a384-3c0e-b3cd-0926c69924fb | -2.746 | -48.56728 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1b3e43b-4cfa-32b6-a52a-d34fcb086b13 | -2.62411 | -46.52427 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c75e2d88-59f0-3596-afab-431719850768 | -3.53753 | -51.58684 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2ee44f8-b9a1-325a-ad57-3aec5885046e | -4.13454 | -47.23743 | 2024-11-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 179b5c1b-d507-3e43-9da3-10e807e3e64f | -2.23116 | -53.61408 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84c12e88-1032-3df9-8866-87473cfc14e4 | -2.57543 | -54.41625 | 2024-11-16 04:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2286820-301e-3779-9295-23ab9e77e55c | -4.45342 | -43.85166 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d811ab7-1b9a-345e-bfc4-a678f218d35b | -3.12023 | -45.98303 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
