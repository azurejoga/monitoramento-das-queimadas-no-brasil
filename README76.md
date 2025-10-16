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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0252d1b0-a09a-3b13-b098-cca723129946 | -6.94816 | -47.7393 | 2025-10-16 05:08:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 216db67e-70a2-3742-86a7-89b9973913d4 | -7.94947 | -44.13776 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c5c634b8-cd94-316e-b9ff-17894cefcf9d | -7.47524 | -42.15075 | 2025-10-16 05:08:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 39c948b8-2213-3749-97cd-04823c788400 | -5.85448 | -43.87986 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1eef9750-4d6c-396f-8073-a5a7afa85ca1 | -7.95525 | -44.14405 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1965d11a-6c86-3383-b029-d2156bcd4b16 | -7.18433 | -42.36301 | 2025-10-16 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ab4ec6ff-9b60-3ff4-8c7e-2395ccd37b2f | -7.47601 | -42.75705 | 2025-10-16 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ee8abc86-1a29-3d2b-9da4-0191a7459350 | -6.17816 | -44.30553 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ac3f396-4869-3590-9282-c8e1a9e84e5a | -9.15771 | -46.86477 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 861cb5c6-a573-311e-9a5d-08e2255c8e93 | -11.57187 | -48.55829 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c5f8326-dcee-390f-b71f-0ed472243544 | -7.92461 | -44.12893 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b35b3144-d5dc-3a4f-91a4-b58e939beefd | -6.45761 | -44.57716 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e8b00c4-17da-349f-b258-ea33f254dc80 | -6.53568 | -44.69116 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91b8bc2e-b0a3-3fc9-b513-3097cd8674a2 | -6.06561 | -44.30543 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27d8bb51-9fbb-383f-8b81-f8fc49cfd615 | -5.50391 | -47.3038 | 2025-10-16 05:08:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22340f9d-a467-38fe-8592-5c4023611d23 | -8.55713 | -44.58498 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 397f79d8-4850-386c-b973-b0713d36cdba | -5.83524 | -42.34351 | 2025-10-16 05:08:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3156e0a2-3447-3f83-81e0-4bf7870c8dc4 | -10.67233 | -45.33048 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89e4dbb2-af34-3ae7-9b82-b793ac5ee4b8 | -5.87901 | -42.80999 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98e2a911-7ae7-33c6-b728-318c71d37dff | -4.97734 | -47.10307 | 2025-10-16 05:08:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc550aca-fbc8-3c88-b85f-b0b607e456d1 | -4.29877 | -50.40483 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 94fd4689-f3cf-3457-b932-44abe72c9c5e | -8.4632 | -44.18963 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 96189d2f-561c-38e0-8fd6-fddfea6f41fb | -11.43069 | -44.13805 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb3759df-4142-316d-9178-c98026189384 | -8.27509 | -48.00318 | 2025-10-16 05:08:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6cbc238-fe62-360a-8a32-ea470315e66f | -12.67141 | -43.44051 | 2025-10-16 05:08:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5ad6b7fb-7c87-3a80-a315-fa34666406f0 | -8.25445 | -44.07276 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35446ce0-5ea8-31eb-9a1c-17e9b5848555 | -8.39518 | -46.26223 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 751951c2-faf8-36f7-87ac-fda8214c65b9 | -10.87027 | -47.93505 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9efba830-869e-3823-820f-ae865d237c45 | -11.54237 | -49.92463 | 2025-10-16 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c942ca66-b067-3e6c-b56b-20fc0522c03f | -5.87746 | -42.82174 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 30b40c69-3cbb-3b4a-98d4-007d00176b2e | -5.31861 | -44.83946 | 2025-10-16 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90bb5954-5436-364c-80e2-56399618e226 | -9.7205 | -44.50426 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3a01343-a776-3901-a006-bef0ea22bb12 | -6.79927 | -45.47652 | 2025-10-16 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 506c4337-8a24-363e-8d73-22283a24a9a5 | -9.69006 | -44.53123 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 70fa525a-01b4-3b07-b1e8-7e3ce299fd42 | -7.0722 | -44.9534 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 843d97c2-8a10-3a7f-9058-2b0e642af7a9 | -8.06911 | -45.43167 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3874fd5f-a5b1-324c-bf03-f86ea32f6f18 | -7.63964 | -44.08697 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdf504a6-96d8-35d6-abb2-dd7e10564c48 | -11.58458 | -44.08289 | 2025-10-16 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b901ec95-12e1-373f-a43b-9b06718239e0 | -8.07073 | -45.41901 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04237363-6bfe-3242-aef9-facccfd4b5fb | -7.53459 | -44.28572 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdf4dc78-9b2d-35dc-9573-52e70e4a2f2f | -6.02566 | -44.31842 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1879eb14-b2d0-390d-a7f5-3250f5c6ccb5 | -8.47526 | -46.24424 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eab75fde-47eb-3efb-b918-643e11775c55 | -7.10991 | -44.72155 | 2025-10-16 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70703d6b-875c-3d5c-a7c9-d01b325279e9 | -8.40611 | -46.2409 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c3b3571-9eb5-3415-99bb-fcb916c734d0 | -6.45077 | -43.38154 | 2025-10-16 05:08:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1af52e54-b2b4-38d1-96dd-8a53479715be | -6.24613 | -44.01033 | 2025-10-16 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3d4b489-f801-37fb-b470-dfe14d543cb8 | -5.91968 | -44.72988 | 2025-10-16 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1daca378-dc8d-350a-b940-bdcce3296499 | -7.11053 | -44.71677 | 2025-10-16 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9aca7a23-f19b-3a44-86fe-732d5853ffb7 | -8.55082 | -44.58392 | 2025-10-16 05:08:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95c7c5c6-9880-34ee-b5e4-992d3c9ed86b | -8.39326 | -46.25066 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32722b41-ef5f-31c5-85d6-ccc1f55fa38c | -7.93722 | -44.13066 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 69876811-14ce-3605-b238-db0eabb66ebe | -8.06698 | -45.42514 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b5b9507-8ad0-3610-9d57-6be17105faba | -6.17937 | -44.29679 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba2dab44-83e5-377b-bd19-5f46a811a79c | -7.1679 | -42.52429 | 2025-10-16 05:08:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4dde68a0-e608-310f-9d7d-f31ac397f7f0 | -10.13259 | -44.57457 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03fa6f7b-f9ae-3900-96a5-a06e9723ac26 | -11.50749 | -44.06751 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b5d5463-3a80-368c-8c33-9222a2bff092 | -5.85926 | -43.88554 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 167edf85-521f-306e-822f-e0de60fb3680 | -7.85141 | -45.40811 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b487054c-cb27-3606-a176-8ed37fcf9f8d | -8.47086 | -44.18309 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6ff5edfc-41da-38d9-a52d-56c7ceab93d4 | -8.45734 | -44.18403 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4928950d-7374-3866-b30c-ec2dc27df0b6 | -5.51365 | -47.30831 | 2025-10-16 05:08:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e66e543f-1457-37f6-8433-a2380d37f511 | -6.33246 | -44.32024 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e41d8368-ded2-361f-9b35-b41857f0cd14 | -7.11064 | -44.72044 | 2025-10-16 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bfe8be1-2970-3e1e-aafd-1997f1ecd2cb | -10.05322 | -43.83572 | 2025-10-16 05:08:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb214314-43e4-37f9-bc43-e55fa6dca17d | -4.34971 | -50.53957 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72fbee6e-a362-347c-abc7-df6090d8d8d2 | -9.15723 | -46.86831 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de52ba2a-11cf-324a-ac2e-934f42cc2807 | -5.85515 | -43.87486 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37f7b5b8-c5b0-3bf4-bde5-567ba751d9b5 | -7.0499 | -46.68534 | 2025-10-16 05:08:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07b2253d-04c6-38d1-b567-b8a748b1fac7 | -5.72469 | -44.52113 | 2025-10-16 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0af8ab8-6f55-34ff-a00d-4bdb1737e5e6 | -8.45846 | -44.17673 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0229dea0-ab96-3792-b50f-8a968578bdee | -8.46337 | -46.24644 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92d4eacc-d7fa-3cf3-8e88-6d31c422ed80 | -5.35556 | -43.7533 | 2025-10-16 05:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60c8bcaf-4be1-395b-885b-3b1203d2520d | -5.91351 | -45.4371 | 2025-10-16 05:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f04c9366-c2ec-30fa-a4ac-218768211354 | -10.61947 | -45.2431 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 639a6e14-836d-36a7-828f-190fd004a02c | -8.45667 | -44.18915 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ed966b09-f9a8-3199-9dfc-1055d19a5fdd | -6.33014 | -44.32093 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94727409-20a1-33c6-9bb9-be07c2ac4931 | -10.13386 | -44.56412 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c76065d9-1a4e-3888-b60b-91583dadf171 | -10.13079 | -44.58931 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 48d860d0-8115-3133-9265-e42c7735f887 | -7.24572 | -49.51701 | 2025-10-16 05:08:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2545601a-1fd8-3f12-bdb0-b19d3b0f4ce6 | -5.46806 | -42.9435 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 04188d04-e9d6-307d-bb60-3c9a2228bdf2 | -9.68627 | -44.51562 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c409d605-8cf5-308d-affd-e3292d9606d5 | -10.6639 | -45.29576 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07f912e1-9178-3c82-b509-260ce31645c5 | -7.00594 | -43.75174 | 2025-10-16 05:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9234ebb0-9153-3ef7-8ee0-c617355a2147 | -9.36489 | -46.94652 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e1aaf94-1404-39df-a1b0-32c45e676a47 | -10.83706 | -43.95097 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a25cbcc3-d61a-3b1a-812d-3346a2a3d869 | -9.69208 | -44.5218 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 75a7063e-3a89-3193-83fd-2592738d3572 | -5.86722 | -43.88204 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8b411e0-1290-339b-9289-0830bbad638c | -7.35257 | -43.86579 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ea8661d4-cc26-303d-93e7-e56bc4e7efd4 | -6.51917 | -42.19785 | 2025-10-16 05:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 31236e5b-a8b4-33b9-8d44-1d6cc3f925e7 | -10.33014 | -45.17453 | 2025-10-16 05:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5753c6f1-90d5-3d0e-9817-7827b55e4232 | -4.30386 | -50.39847 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9529df34-e061-3959-b01b-f39431416115 | -9.7185 | -44.52039 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 30e04147-d301-3713-8414-b26ca14abc44 | -5.83154 | -42.33751 | 2025-10-16 05:08:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 664a90c1-b6d4-332a-a3d4-b8f0d2be5aa2 | -6.22053 | -44.15479 | 2025-10-16 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68ce8fad-0b9e-3f11-bb11-2770bce9f24b | -10.05472 | -43.83548 | 2025-10-16 05:08:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb04b86e-21bb-3033-ac4c-e0e7809f6f91 | -10.81554 | -43.9404 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13fe1fa1-a771-3f8f-97d2-e9718217cce5 | -5.88796 | -43.87331 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2873068-c485-31c0-99f4-d0dd1dab64c2 | -8.38997 | -46.258 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb44d620-e67a-32a4-81b2-bce306e61f57 | -11.29228 | -49.8886 | 2025-10-16 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a51351bc-8228-3d60-a417-e87a00052d24 | -7.16463 | -42.51241 | 2025-10-16 05:08:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README77.md)
