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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 490af0cd-493d-3ae4-a416-0374058f3a6c | -21.93638 | -46.56869 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d780015a-3183-322f-ac18-abbf94fc2e28 | -22.08608 | -46.65599 | 2025-09-16 04:53:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b22d9bb7-281e-3369-ad5b-7518dd8f9b07 | -23.19876 | -49.6331 | 2025-09-16 04:55:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b16dd02d-3be5-39ff-b9b5-81e097315dc8 | -23.16071 | -47.63744 | 2025-09-16 04:55:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 28237af6-16d8-3ced-8f15-d6039014773a | -22.24025 | -49.37402 | 2025-09-16 04:55:00 | NOAA-20 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d02b8242-ace5-3bda-94e6-a773cb4a1da6 | -23.44518 | -47.67463 | 2025-09-16 04:55:00 | NOAA-20 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8f6d4cbb-1b86-399d-8e89-2892ae70d384 | -22.98461 | -49.94799 | 2025-09-16 04:55:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d5385c39-2db1-30dd-9e8c-1a0015959d2b | -22.71747 | -43.22887 | 2025-09-16 04:55:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f0c3a079-c538-3d83-8004-3d9265faefb9 | -22.60194 | -47.65312 | 2025-09-16 04:55:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 32f18412-290e-3cf5-9397-9a11695ef748 | -22.71044 | -43.23427 | 2025-09-16 04:55:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0ef05029-d084-369a-8025-cb06b2acb98f | -22.51572 | -47.60507 | 2025-09-16 04:55:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 64785e8a-0202-3df4-9050-8f4c41da8abd | -23.12848 | -49.706 | 2025-09-16 04:55:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 489b0972-1875-30f1-b957-9ce0d5895115 | -23.25563 | -48.28896 | 2025-09-16 04:55:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5bbf6d5e-6310-3be0-af08-1a9f71e912e5 | -22.4674 | -45.2106 | 2025-09-16 04:55:00 | NOAA-20 | MARMELÓPOLIS | MINAS GERAIS | Brasil | 3140407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0494e137-96f8-32bc-bcf6-641a742e7628 | -22.97976 | -49.95173 | 2025-09-16 04:55:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4dafa78c-3e47-3097-88ac-fa06c3387cad | -23.39514 | -49.50141 | 2025-09-16 04:55:00 | NOAA-20 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 1540fd69-fbf3-3903-9557-98fdce45f7b3 | -23.25624 | -48.28307 | 2025-09-16 04:55:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75eb3043-d039-3973-9810-09efb4ab63d4 | -22.68805 | -48.29771 | 2025-09-16 04:55:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fedac36-6841-3770-8357-b32fc0364cdd | -22.34659 | -47.33684 | 2025-09-16 04:55:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aa7a4bc1-d3b8-33e6-989e-c545f4273e36 | -22.98946 | -49.9443 | 2025-09-16 04:55:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c28d4128-209a-31cf-9d27-04cc8f3bc9bd | -22.33179 | -46.5262 | 2025-09-16 04:55:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 60e2eaea-5ba8-316e-923c-66d62323fd2f | -22.71159 | -43.23856 | 2025-09-16 04:55:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 409717a5-5c97-303b-9754-27ecc73331eb | -22.71 | -43.24034 | 2025-09-16 04:55:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e8ba8f17-51eb-3a70-8de2-0dc21db56374 | -23.252 | -48.27648 | 2025-09-16 04:55:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 12ae5bc9-a2cd-33c0-aab6-715ed18f1faf | -22.32896 | -46.52986 | 2025-09-16 04:55:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9e836d2-db9d-3c3b-b6ce-884ca1eabfce | -23.23345 | -51.00346 | 2025-09-16 04:55:00 | NOAA-20 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7d36dfb9-5fe7-31bb-9765-4fb4c1d9c27e | -23.2032 | -49.63385 | 2025-09-16 04:55:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| be21b1bb-bce6-3cd6-aa31-51e8c648aa18 | -23.16481 | -47.63578 | 2025-09-16 04:55:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 744d6a8e-d715-39a8-bd1e-823ccc432e15 | -22.71206 | -43.23253 | 2025-09-16 04:55:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a67a3808-64d2-3fc0-828b-a1be10103660 | -23.12793 | -49.71076 | 2025-09-16 04:55:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1e5c7c68-6991-3812-927a-e168e925347a | -22.34463 | -47.33444 | 2025-09-16 04:55:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0a6a0cdc-06af-31b5-b545-2283c612080b | -22.32932 | -46.52631 | 2025-09-16 04:55:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 63c36c1c-6ae3-3028-b840-1f30b879ed2b | -22.33146 | -46.52978 | 2025-09-16 04:55:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0c20c833-2084-3d55-816c-fb4edfce6d54 | -23.16451 | -47.63894 | 2025-09-16 04:55:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 66619e2c-7b3d-3888-8bc3-5880b2359685 | -22.46705 | -45.21466 | 2025-09-16 04:55:00 | NOAA-20 | MARMELÓPOLIS | MINAS GERAIS | Brasil | 3140407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ecd7d85-3b82-3c50-9a8b-ee9a7d9ea276 | -22.71704 | -43.23487 | 2025-09-16 04:55:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9694236b-945e-3a06-9def-dd9bd5687a6a | -23.16578 | -47.63803 | 2025-09-16 04:55:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 91084be0-397c-3c57-84c2-cb76d37f65a2 | -23.34148 | -51.06601 | 2025-09-16 04:55:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5e272141-84d6-3ea2-9898-4538294290c5 | -23.39785 | -49.50053 | 2025-09-16 04:55:00 | NOAA-20 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 6608f08d-d0ac-3476-a6d1-3f9787daa531 | -7.26434 | -46.58848 | 2025-09-16 05:25:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 9012e085-baae-3de7-99e3-8d219b4e7731 | -6.68264 | -46.30378 | 2025-09-16 05:25:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| a0518777-b5b2-37f0-bae3-5b7f828723e5 | -3.83599 | -44.10026 | 2025-09-16 05:25:00 | AQUA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| cc4e9a3c-2e83-3ba0-83ff-2162a84c61e5 | -6.17679 | -45.11909 | 2025-09-16 05:25:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a29c2d62-4148-328c-aff1-32b13161cc26 | -3.80399 | -41.56019 | 2025-09-16 05:25:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 4d40f326-93f5-331a-bf40-1b3c681bafad | -5.55897 | -44.96467 | 2025-09-16 05:25:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b2341496-012f-3854-b19e-228a5d663eab | -3.82967 | -44.10455 | 2025-09-16 05:25:00 | AQUA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0431f2bb-1533-3a4f-bf86-c219b3d918ab | -5.22335 | -43.69427 | 2025-09-16 05:25:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1a7dd213-a5ad-37d6-a70e-c43664405681 | -5.90721 | -42.7456 | 2025-09-16 05:25:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 0b55e632-5beb-3814-a5f8-95272140fd3c | -3.83248 | -44.08724 | 2025-09-16 05:25:00 | AQUA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4c8281b3-5a55-334c-92b0-64c129277f71 | -5.5351 | -42.64506 | 2025-09-16 05:25:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 470cdf04-368c-3f8c-b4c8-d97013be7fa9 | -7.1363 | -47.96926 | 2025-09-16 05:25:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 4b97d6e9-7221-3b9e-8cc4-1a06ff223fdb | -5.77473 | -43.92865 | 2025-09-16 05:25:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f90fbe8b-5061-3863-8092-bc864fd55221 | -3.8139 | -41.56164 | 2025-09-16 05:25:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 6f6bd34e-c7b5-3ed3-bc2f-6ebe64952d02 | -5.53318 | -42.65754 | 2025-09-16 05:25:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 4eca8552-b7eb-34b7-a8fb-3e325fb97bfa | -5.5566 | -44.95908 | 2025-09-16 05:25:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 75663e69-2cbc-3fd1-b53a-036c216d0703 | -6.17995 | -45.10696 | 2025-09-16 05:25:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| fadac6f0-7875-37fb-a731-87f81a9feac7 | -3.81215 | -41.57296 | 2025-09-16 05:25:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a0b275ef-10f5-3579-8a5f-c646691e41b3 | -3.82393 | -44.09849 | 2025-09-16 05:25:00 | AQUA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9aaeff71-c63b-3667-9ec0-0135d17d79e9 | -6.1822 | -41.19318 | 2025-09-16 05:25:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 491c51cb-7b13-3fb6-81d5-285a98c8dbbe | -6.17676 | -45.12629 | 2025-09-16 05:25:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9cd21bcf-bc5d-313f-a51f-497d61b42dfa | -5.90922 | -42.73306 | 2025-09-16 05:25:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| ac097e80-3039-3f5f-aed1-784755457793 | -7.09025 | -39.66618 | 2025-09-16 05:25:00 | AQUA_M-M | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 636ea636-a93c-355e-a622-14a8806270d1 | -5.53988 | -42.66427 | 2025-09-16 05:25:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 8d83d830-8fe2-3575-b06b-718c3d81950d | -5.54189 | -42.65176 | 2025-09-16 05:25:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 90662b63-f86d-3793-89a0-72cc5caf38f4 | -3.81563 | -41.5504 | 2025-09-16 05:25:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 8661e100-7746-34f8-a832-59e8910a16bc | -6.18936 | -45.12791 | 2025-09-16 05:25:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 9fe11d6e-56e2-3eeb-8674-aa63aaed3869 | -6.18064 | -41.20327 | 2025-09-16 05:25:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d99ceca9-500e-32f7-a73a-038514f6541d | -10.70159 | -46.50924 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| a204274c-ebba-3c33-8858-a60ae8b69537 | -10.71439 | -46.5117 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 417.3 |
| bbad4a66-e875-38e1-8d9a-c9e4b0abec81 | -12.30126 | -46.39957 | 2025-09-16 05:27:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a1dafecc-1992-3702-b6f9-a01c123cb8d4 | -12.69076 | -47.99422 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 78e93fbb-cc2d-31fb-9bd2-af26ff564770 | -10.71795 | -46.49065 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 295.4 |
| 3e9dd300-86e5-37cc-aaa9-94049d482d70 | -9.05382 | -44.83547 | 2025-09-16 05:27:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2928a538-8b02-39dd-888f-891b8058ba73 | -10.71798 | -44.75198 | 2025-09-16 05:27:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 77cc7fc3-be6e-3dc3-b3c1-88df5e821395 | -12.75501 | -47.95527 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| fc1bc4db-469f-39be-abc1-425c379c3fd4 | -12.76167 | -47.9614 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 0710ec3a-cd85-3e34-a380-749d640c6849 | -10.70511 | -46.48856 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 446a907f-5606-377c-abdc-58b94a7f4ecc | -9.0944 | -44.86597 | 2025-09-16 05:27:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 372be7a8-e196-347a-9cfe-9d1652814ebc | -10.71548 | -44.76714 | 2025-09-16 05:27:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 491b4dc1-8600-3d5e-9d58-5037f9513994 | -10.72171 | -46.46838 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 236713e7-90a8-30f1-bcf5-58d26d11e61b | -12.65412 | -47.93008 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 6d4a0aa0-872a-315a-b50a-df6b67b92a9e | -10.64455 | -46.45725 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 661efc6e-38c2-3ee0-9a25-043fa5e1858b | -14.51528 | -47.32954 | 2025-09-16 05:27:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e7d005a9-443b-3025-b9eb-0278ae8ba95a | -12.61715 | -45.75245 | 2025-09-16 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 330.5 |
| 7d38994c-ca9a-3cbe-8532-e0c131a73cb7 | -12.62327 | -45.73093 | 2025-09-16 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 346.1 |
| 914fa571-c4f5-34d3-9186-2e35370ab74e | -12.53962 | -45.86966 | 2025-09-16 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 803bf683-f438-34ec-9e2a-b049841c2718 | -12.78839 | -47.25033 | 2025-09-16 05:27:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4cbfc0a1-49d5-3e1b-864f-37296d1336e5 | -12.05416 | -46.53885 | 2025-09-16 05:27:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7bfa02b0-442f-3fea-b112-3626810a575f | -11.70726 | -46.86824 | 2025-09-16 05:27:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| e20265b5-a84e-3684-84ba-294296dedf02 | -7.99699 | -45.67491 | 2025-09-16 05:27:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 2349f333-8c74-3549-86f9-8e6ae93b9f98 | -10.72044 | -44.73701 | 2025-09-16 05:27:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fa2cd594-efa2-3efa-bf6b-2bdd0db2af12 | -11.43131 | -46.93235 | 2025-09-16 05:27:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| f7ef2306-4be8-3b86-b9bc-227057ebb3f0 | -10.71948 | -46.47575 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1bc37f6e-76be-3a2c-b1b6-1a7646284b6f | -9.09168 | -44.88225 | 2025-09-16 05:27:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 401c35cb-2830-39f7-8237-1d28207732e1 | -12.75717 | -47.98569 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 425f39f6-eb3c-37fc-b50c-99e6d9d495cc | -12.62004 | -45.7359 | 2025-09-16 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 657.2 |
| 67b2de4a-b543-305d-b8f3-8570aec3be82 | -12.68708 | -47.98608 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| c126a4f9-fb5b-3834-b407-32e92b866a61 | -8.00031 | -45.65553 | 2025-09-16 05:27:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| b76b2f1a-f98a-322c-80f4-399106bc531b | -9.05393 | -47.02499 | 2025-09-16 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 2daca751-c991-3674-98ff-b8ad8c864910 | -13.21434 | -47.29482 | 2025-09-16 05:27:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |


[Clique aqui para ver as próximas entradas](README82.md)
