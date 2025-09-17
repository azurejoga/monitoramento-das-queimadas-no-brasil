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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f36b9be-f193-33c5-ada1-7c4956d27821 | -8.91002 | -46.28307 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 423d730a-7614-33b8-b7ab-c1871665b38f | -6.2417 | -43.45752 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1ed251f-6351-32ba-a3bd-ada87faba932 | -7.98143 | -43.93671 | 2025-09-17 04:10:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13f6f597-7973-33e9-a9a0-3a09c5ff2855 | -9.06359 | -46.58051 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a32bf4e1-ee6f-3bcf-9d24-903e43d4d551 | -6.25892 | -43.46039 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42c15004-7ab1-3397-8db1-e85da9f36ba4 | -4.99863 | -44.87589 | 2025-09-17 04:10:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50718b95-555c-33fe-ae1d-a4127c31e795 | -8.56572 | -47.56495 | 2025-09-17 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c98fb9a9-c552-3e24-960c-367093c0e948 | -5.3502 | -44.82388 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11fc9a04-21a0-3559-a6a0-a8da96091bc7 | -5.52051 | -42.1852 | 2025-09-17 04:10:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7d60ce32-7414-375e-95fb-f464ef24fb80 | -6.15895 | -44.52557 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f40eb870-5261-3f1b-a88f-633fceec1baa | -6.31053 | -44.55975 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d258d4de-4055-3d9b-8ea0-3585bc821885 | -7.00063 | -44.58175 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3b0b25d-bca5-3a8c-93e3-8f7ae12c6200 | -3.85223 | -40.34859 | 2025-09-17 04:10:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a4f2b8b0-3ff2-3652-9128-40339c2851b4 | -4.32845 | -48.38746 | 2025-09-17 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a07056e-5f78-3313-bc82-806bd527a4f6 | -7.33908 | -39.71701 | 2025-09-17 04:10:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a6cda996-5851-3e36-86b4-65f9a061ffd4 | -8.16008 | -46.76389 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e41c06ef-8024-35a9-be7f-f9a2647f401f | -9.09405 | -44.92765 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8928cc77-9429-3ec1-b472-6d11cc7dc7e5 | -5.54625 | -45.37868 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9be53938-5805-38e6-950e-63ddfc842586 | -5.33071 | -44.993 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cef9ee5f-709e-3b48-ab4d-15960d5a2bf7 | -7.76534 | -44.72772 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 480f460f-e1f0-319b-b17d-b8d689bf428e | -8.92311 | -46.27576 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e28e915f-12bf-3b61-9719-fb10df35090b | -6.22373 | -43.74265 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a96ccf6a-0e3f-3347-a4b0-7e6a3d058b60 | -5.34793 | -44.82621 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bb78125-1b5e-364b-ae2e-0782e247f2cb | -6.15763 | -44.53372 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49e8a077-3b74-3c9c-ae56-0c9b5c4a2735 | -6.45915 | -46.00967 | 2025-09-17 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c76adac6-f30b-36c2-be77-535d67ac804f | -7.37595 | -47.04595 | 2025-09-17 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a289053-503f-31e8-b391-0eca533d9914 | -5.80089 | -45.70465 | 2025-09-17 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25a9acd1-1085-3fac-b602-75013760c3f5 | -2.25716 | -47.84373 | 2025-09-17 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59f401a4-fcab-3953-a6a4-a526801cbafd | -6.92304 | -44.80722 | 2025-09-17 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04af3346-cbc4-394d-9c14-1783d421895c | -3.69169 | -49.01968 | 2025-09-17 04:10:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecf92487-49c2-3975-a190-a846bcd37618 | -7.48943 | -46.12334 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c47d0cbb-9099-3949-9b08-d28cb5693ecb | -6.04523 | -43.14148 | 2025-09-17 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 21164300-c1fd-3189-8bcd-bb16992d529e | -8.2271 | -49.48615 | 2025-09-17 04:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43ab2947-fd7e-3042-a61a-9a142cc778c9 | -7.39777 | -50.00844 | 2025-09-17 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90769391-823d-37c1-9571-6464b8e27848 | -8.58371 | -46.339 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36ba0ad0-505d-35fb-a432-498673d6b73e | -5.7749 | -45.52843 | 2025-09-17 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b91d7f1-490c-33d8-94bf-bfa9c932fb26 | -9.10664 | -44.85103 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3622d248-2cbc-3ced-93b7-e73fbf7bd910 | -6.42075 | -43.60094 | 2025-09-17 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5bbe5d30-9c3c-346c-8139-040dd70b8199 | -8.56603 | -46.34378 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b411ea21-db17-35bf-9e41-63679dbcaab2 | -7.85907 | -48.1777 | 2025-09-17 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7c747b8-0665-37ca-8c8c-ba74a0080aca | -8.13513 | -43.63102 | 2025-09-17 04:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 245008f2-3d09-36f6-9f5e-54ebb53e2e0c | -5.62855 | -44.82853 | 2025-09-17 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d5be20f-37bf-3c3e-87ee-874dc53cecff | -5.58962 | -43.80361 | 2025-09-17 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88f3542a-75b7-369e-ad89-97bcf10dd35f | -6.8763 | -43.96739 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0eb2dc79-332d-39c8-b712-8de8342439a8 | -8.13334 | -43.64218 | 2025-09-17 04:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc301317-7979-397e-b2a8-33f70bb8ccf3 | -4.91925 | -47.86579 | 2025-09-17 04:10:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d641ce7-90ac-38dc-ad94-3367c3493b31 | -10.20296 | -42.54173 | 2025-09-17 04:10:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7072b543-2eb3-3755-b1a1-dc029f6217a1 | -7.57947 | -44.58687 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 142fb4a9-42f8-3695-b460-2475ad287c8a | -9.94153 | -45.93139 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 107798db-da31-3c8e-af9a-e9b82e88987a | -6.87281 | -43.96681 | 2025-09-17 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cd219e1-b28b-34b0-82a3-8fe60e5da44b | -7.32347 | -44.0599 | 2025-09-17 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f1dbfb1-6f3d-316f-b549-afae83246ee7 | -7.61017 | -47.46894 | 2025-09-17 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6dca0ca-976b-3a93-a2dc-db2e6b1bff53 | -8.06516 | -45.45518 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 116f73d7-6968-3906-bc7e-f95c3ad0a876 | -8.67283 | -46.35657 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1c9bd94-0e61-31c6-93c8-e7e357b14984 | -8.15782 | -46.75942 | 2025-09-17 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df8b6026-5ef3-3846-9677-6648baa053a3 | -6.40493 | -43.35682 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80fe6b42-bd72-379d-96d4-b2daf294b845 | -8.97138 | -46.01562 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 281063c3-9ebf-3f0c-b38e-ce9dcf0a5b0e | -8.56242 | -46.37022 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9baffdea-546e-312e-96dd-ddc50cbe520d | -6.97701 | -44.45634 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d283365-264f-3be1-9a3c-40e57c7de5ba | -6.22972 | -42.02511 | 2025-09-17 04:10:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d545deb1-10a8-360f-a4aa-8d109e75cf03 | -8.12813 | -43.65276 | 2025-09-17 04:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37fc5890-ca26-35e9-b55d-3af67f695a41 | -6.17972 | -41.22669 | 2025-09-17 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 99f0e5ba-e832-3047-b240-d740f7b098be | -6.17639 | -41.22616 | 2025-09-17 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0b83bf8f-dfc7-3356-8efa-c2f15563a747 | -6.95811 | -44.54907 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6467dcab-d805-3760-b1c3-b53f537a3519 | -3.34387 | -42.17088 | 2025-09-17 04:10:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 126f2f65-044d-3820-bfad-0477fe694be2 | -7.40385 | -50.00344 | 2025-09-17 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 577d2454-abc2-3dc2-828b-1dc5b7ecf539 | -7.26935 | -46.59943 | 2025-09-17 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dfdfcc9-bc96-3d55-8a20-ffd4cee25aff | -6.24514 | -43.45811 | 2025-09-17 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d824a3d-78e1-3198-bc51-45eb7ed38988 | -3.81348 | -41.6824 | 2025-09-17 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 782478f7-4385-339b-9b35-ddf607607567 | -3.17455 | -48.81019 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b233b55c-ae19-3912-93d8-716361f4bdf7 | -8.96798 | -46.3374 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 159221fe-1c2c-3a68-9c68-4289f2d2249d | -7.40437 | -50.00892 | 2025-09-17 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 451ff12a-7b81-34e3-847c-17eb4e7400db | -3.07613 | -48.81573 | 2025-09-17 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd3464e1-1d5e-3ceb-a37f-9e8a2abd0cf8 | -8.89941 | -46.14879 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fc6c45c-2398-3d87-88d0-a9e525033726 | -6.96368 | -44.53754 | 2025-09-17 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 026dc6c8-8866-3d98-8177-c1e687b3bfb3 | -8.6722 | -46.40651 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3a26f1cd-3bab-33e6-9ea6-7392e5774189 | -5.46205 | -44.68477 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0fd7218-edf5-34cc-b564-307634a66583 | -6.16157 | -43.67754 | 2025-09-17 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 945d74c1-7885-33e1-9075-a175e8cdb8bb | -7.0013 | -44.57767 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73c8997a-2ff2-31cb-b910-033215d06733 | -7.17219 | -44.34282 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 934faab1-0b36-3021-ad90-c1fd305e2b10 | -9.15386 | -47.01448 | 2025-09-17 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 337ae6f2-91ef-3fe7-893f-c5c973917979 | -7.82367 | -46.16111 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1418bbfe-5f72-3364-86f2-ff8a21ba623a | -6.19445 | -45.1258 | 2025-09-17 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 434c8781-9b20-38a5-b6ee-61b7ab506ef0 | -5.84498 | -37.49246 | 2025-09-17 04:10:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 051ecb36-0bef-361b-bcec-5c21fe19f12b | -5.52385 | -42.18573 | 2025-09-17 04:10:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ec8b57fb-ac0d-32ff-b696-f9d7359c22f7 | -8.96542 | -44.19459 | 2025-09-17 04:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f7427ad-6e82-32fe-a1e7-c0d929154307 | -6.15832 | -44.53231 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15c5eb04-088b-3b6a-8504-057786de8fd5 | -8.96473 | -45.75599 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4c659e8-a55d-311a-a5a3-83c61ba45d8f | -8.92189 | -46.23689 | 2025-09-17 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c48bd78-9b1c-33cb-bb43-c7f2e03204c6 | -7.7269 | -45.29688 | 2025-09-17 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64544ad1-c241-33ee-b031-edf9b5c06fee | -7.52777 | -44.7342 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e61e8ebd-e4c0-336b-b4d9-436fb7cc2884 | -4.92303 | -47.87104 | 2025-09-17 04:10:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e11702ae-9930-3b2c-b702-ca2a0cb83829 | -7.07614 | -44.55539 | 2025-09-17 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bc49926-3cb4-33a6-9539-a2de7842cf83 | -6.41017 | -43.34613 | 2025-09-17 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe7ecf47-6c29-3619-a255-ff409bc59a5e | -7.58237 | -44.59149 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e2faa679-6540-3ecc-b44b-86b317f8de3b | -8.94457 | -45.53545 | 2025-09-17 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73893d27-0d0b-329d-ad0b-844fad9417cf | -6.61195 | -45.5925 | 2025-09-17 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9f33079-ec89-330c-b7a1-4de4e828b5d8 | -9.09987 | -44.93681 | 2025-09-17 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18437d7a-0251-379c-9b9f-e800f782c8ac | -7.50461 | -44.71786 | 2025-09-17 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2543401c-ae0c-3006-bd79-70ea6fceb072 | -7.48556 | -46.12269 | 2025-09-17 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README24.md)
