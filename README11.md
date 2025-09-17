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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01297dda-522c-3e1e-8f04-b3ce3803ffc0 | -7.26617 | -46.58101 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 443ecb74-4290-3433-a963-9d58ecafa7a4 | -6.39832 | -43.34481 | 2025-09-17 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96e312a4-24f9-3845-ab9a-0e33ed4688b5 | -6.16093 | -43.67848 | 2025-09-17 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c22a9952-2f93-34d9-929f-93123cdd29e5 | -5.62915 | -44.83303 | 2025-09-17 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9c49976c-a921-3e41-9617-8b3746a0fe3d | -6.76935 | -43.39937 | 2025-09-17 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d69e82c3-644a-344a-8dac-2d5bdceb51d9 | -5.7943 | -43.50075 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba2813f7-aa6c-3feb-b239-99f8d313add4 | -6.18185 | -41.21814 | 2025-09-17 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc23f8d5-0e1e-3e2b-81dc-016bd16efce1 | -6.12055 | -43.33883 | 2025-09-17 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad1f2f94-300d-3e5e-b293-a23dec43f304 | -7.27206 | -46.58272 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8b18e8ec-3863-3646-a444-39fa66ffe295 | -4.51842 | -38.54979 | 2025-09-17 03:42:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c1f7270c-7fad-3850-8ff3-844cbe59a9a1 | -6.68212 | -46.30666 | 2025-09-17 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6e54fc57-b8bb-3f27-a308-ec3e52781fe6 | -6.03945 | -43.14705 | 2025-09-17 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f9992231-7a4e-374a-9b94-2c3ed19b4369 | -6.962 | -44.54988 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0f6a783-7538-3661-86cd-42d94da2ee41 | -2.37655 | -47.6347 | 2025-09-17 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 47b80229-597e-3d2e-a67d-1eb6e7e1795a | -4.92445 | -47.86778 | 2025-09-17 03:42:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fb1cf831-9e5a-34fa-bd16-5c9512b246d2 | -6.61288 | -45.58678 | 2025-09-17 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c2c8a7ac-51a6-3f14-83e6-178b210530d0 | -6.59119 | -44.32169 | 2025-09-17 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d14e5d0-97c1-3ae1-9838-41bc0bc85785 | -3.81492 | -41.6838 | 2025-09-17 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cb8e17f5-80a6-372e-aa34-5971ce64c151 | -4.66528 | -46.31754 | 2025-09-17 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 832fc0e7-27e1-3511-bc42-d71ea82ed842 | -6.68133 | -46.31116 | 2025-09-17 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| be247457-ce7b-38f5-9288-d5366c18ba46 | -6.16143 | -43.67558 | 2025-09-17 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 489aa1f5-406a-3671-9a21-692e4701b09b | -7.0676 | -44.34868 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0625b37f-017b-3831-93ac-e958d945b605 | -6.60877 | -45.57701 | 2025-09-17 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6428d89a-769b-3d8e-bc69-22cd17f77f7f | -5.76662 | -45.90556 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b57cafb0-349f-3bd7-893b-8a027b87ccd8 | -6.8678 | -43.97016 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae0806b9-9578-3f47-a50c-d39c31155dbb | -6.04531 | -43.14207 | 2025-09-17 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8c440a21-47b4-3804-8c87-3741cbeb3d1f | -5.79636 | -43.48891 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 286fa26d-30c5-3db8-8c4e-2377b44acb62 | -6.52771 | -41.81775 | 2025-09-17 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f114eb01-d26f-3bc9-9064-8c421cee064d | -6.98335 | -44.61557 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 837837d0-350a-30c7-b29c-328d016a4323 | -6.28897 | -42.38394 | 2025-09-17 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 26ccfc8c-5da6-3972-98e2-1074894f1ea8 | -6.2904 | -42.38091 | 2025-09-17 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 210159d8-44da-3101-8614-e5762886cdb8 | -7.78426 | -35.62555 | 2025-09-17 03:42:00 | NOAA-21 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b66069a9-1637-3fae-aeeb-7071127d30b9 | -5.53088 | -42.18646 | 2025-09-17 03:42:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3e91d34e-6083-3de0-9259-98b63b9e9e80 | -6.87051 | -43.9721 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 903d0b40-1eea-3f93-a34c-217374410a1b | -6.60797 | -45.58146 | 2025-09-17 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23b754dd-b6e1-3422-9275-30bedaa724b0 | -8.63686 | -46.41143 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80980467-bb7a-3077-8460-8983b544e27e | -12.72354 | -48.01568 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a8feb976-e500-3998-a9eb-c56b208acaac | -15.32467 | -42.05088 | 2025-09-17 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0c833cf9-51a3-3eb8-acd2-be15506586c2 | -7.76729 | -44.73244 | 2025-09-17 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b1bdc88c-9c94-3292-80c3-0040fcb10ff2 | -7.82605 | -46.16183 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7911e29a-9271-34d9-9339-3d58ad2cf4c2 | -8.54041 | -48.97385 | 2025-09-17 03:45:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05031586-0f9d-3501-91db-9c5b7c21cb62 | -12.10524 | -44.8337 | 2025-09-17 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47a487a5-8e52-375e-b028-7330347e2387 | -7.49183 | -46.12289 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a12e725-582d-3928-841e-078ed760faef | -13.86431 | -44.88448 | 2025-09-17 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f8ae0fd-f7a3-3e85-9450-3deff1f54943 | -8.68096 | -46.36747 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5121ae9-ec57-318b-b314-cf296a7a98b4 | -9.59521 | -45.6632 | 2025-09-17 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d106e34-b29b-3732-b121-f6b0d617006e | -13.35903 | -39.78932 | 2025-09-17 03:45:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1c23737d-9eaf-3108-81f1-ecf71d7a1d76 | -9.17901 | -46.93683 | 2025-09-17 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 76cc3d1d-55f8-3d9b-a3d9-d25fe6293c42 | -9.06577 | -44.94218 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27405a38-a3ed-3494-a76a-6bc227ae1604 | -8.57129 | -46.34509 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b71a917-2d37-376c-966a-d7a3054c9735 | -15.76716 | -41.61861 | 2025-09-17 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 76a05ad9-65c6-3105-b49d-fda1c0007170 | -12.72234 | -48.0082 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 97e84e0e-0951-317e-87c8-548f91929ccb | -9.09224 | -44.94552 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b93002e0-aed4-3927-bb1f-64e1846a22bc | -12.35964 | -47.06739 | 2025-09-17 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5614072b-ce73-3983-b009-e0aab103780c | -8.63302 | -46.43195 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c4d362c4-fc03-3af1-a9e0-b58ad119cace | -9.55154 | -46.29834 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59085458-407c-3729-b06d-f974551b09a0 | -12.09527 | -44.83247 | 2025-09-17 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e590543f-829c-38fc-a2db-0d2a5f012ba4 | -8.96926 | -46.33475 | 2025-09-17 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07c7e49c-1ddb-339e-8cae-da2e2da0c425 | -12.71723 | -47.98594 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e99f8fb3-7b96-31ba-921e-1f9e7186fe52 | -9.09453 | -44.93319 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 108fd549-16f2-30c2-8a0e-9fb467ffc6d6 | -12.72416 | -47.99901 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 12829ae7-4455-30fd-ae70-f1fdad9abfc0 | -11.50825 | -43.62898 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7942dc4-2ea8-3c7f-ac5a-7abb1a190ef0 | -7.76848 | -44.72585 | 2025-09-17 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 703ccc59-9fb9-3f8d-9f9d-c6d82cc66060 | -12.84637 | -47.19595 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36612a2a-25b6-39df-b18e-6e7e987818d6 | -8.1598 | -46.75482 | 2025-09-17 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50b331b0-f66f-3a55-861f-d72d2c08346c | -12.96461 | -47.95616 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad63d755-2bc1-3502-93f9-a62f82818b2e | -12.97318 | -47.94436 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0380af61-34c8-39bd-90dc-8bb0d300692d | -11.46825 | -43.56406 | 2025-09-17 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47ed1a75-ee0c-38ad-862f-89ec7207f574 | -7.61 | -47.46716 | 2025-09-17 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8ac1b4a-5398-308a-84a9-d8418eb82cc5 | -12.36041 | -47.0634 | 2025-09-17 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5353d28-be3f-3c70-b043-95c79c2c5986 | -7.8253 | -46.16593 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2fce96e1-3da3-3f65-a4dd-ceebf2561a18 | -13.21586 | -47.28071 | 2025-09-17 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed693f99-42f2-364f-af71-56c0d75f583c | -12.97232 | -47.94854 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50bae625-a350-34ac-9e43-84deee0748bb | -12.72324 | -48.00364 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e4245bdf-aef0-3c28-a239-b417e0c162cb | -9.05332 | -44.83218 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d438502-4a81-3f4e-9893-07d05ee0f4b1 | -8.78942 | -47.81136 | 2025-09-17 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87f9134f-0ab6-3b8a-9dd9-6f455c62ac7f | -8.56551 | -46.34399 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02dcf54c-55e7-3033-a9fc-0b3cc905ab65 | -14.61381 | -46.40158 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1bd7c4c-597b-3a9f-987c-9f444412654d | -9.10992 | -44.85019 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6422f509-e371-348e-9799-bed9658887c8 | -12.69739 | -47.76286 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 715b25f2-96b7-3441-a69d-8c3964d279a5 | -8.13018 | -43.6405 | 2025-09-17 03:45:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f5ee84e-eba9-3a47-8987-840bbc1652a6 | -9.5899 | -45.66813 | 2025-09-17 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 131bd60f-8971-3424-b5db-fc8f37086c11 | -8.15381 | -46.75377 | 2025-09-17 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a04b172a-50f7-3edd-8022-dec21cfef8c7 | -7.47817 | -46.09945 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3fbb346-080b-38ac-a915-12305839025d | -14.61314 | -46.37757 | 2025-09-17 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39cd65f7-9546-31c4-92fd-0783ecc60cc0 | -7.8268 | -46.15776 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5c2cfffb-8145-395b-8d9a-7f6034d588a1 | -9.59058 | -45.66456 | 2025-09-17 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7180cf91-df0d-36c2-b772-9d0853eb587d | -12.70239 | -47.76842 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d863fd5-180f-3ca8-99ac-aa33c6fb3af9 | -7.67703 | -46.63482 | 2025-09-17 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18946fbc-7cfd-32c3-b23b-93736a079777 | -9.09632 | -44.92353 | 2025-09-17 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2574261-c104-3d03-84b8-f42dedec7f0a | -13.8635 | -44.88642 | 2025-09-17 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cf4f48e-c713-3a7c-aa76-32bd64eafa3b | -9.59672 | -45.66187 | 2025-09-17 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df2e1c33-581a-3fa6-9e43-31218e1c954a | -12.70502 | -47.95491 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b126122e-6ef4-3eb3-96e7-d44d7c5ebcce | -8.67664 | -46.3585 | 2025-09-17 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1011de3a-b910-38a0-8291-3b70927c4bf3 | -11.93867 | -38.33242 | 2025-09-17 03:45:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7aad09bf-1944-371f-8246-3ffb18ffa9bd | -13.17806 | -44.48095 | 2025-09-17 03:45:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46edc9a2-4219-3305-806c-eca8ec3f7350 | -12.70716 | -47.97454 | 2025-09-17 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02b78aa3-35c9-3ed3-b3df-da3ba3aa18eb | -8.13757 | -43.64334 | 2025-09-17 03:45:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fe4d9c7-0a70-33c0-8c78-31083afd56ab | -11.60096 | -49.81528 | 2025-09-17 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 519b1825-da58-3c83-be03-81ee7db2fb21 | -15.88024 | -41.94975 | 2025-09-17 03:45:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
