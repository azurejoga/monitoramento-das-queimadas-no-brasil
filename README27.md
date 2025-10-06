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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c424e208-0692-347f-bd34-24391df1ffba | -8.51904 | -46.33878 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c347be26-f176-3639-b7c4-84fb98c06146 | -8.57882 | -48.70009 | 2025-10-06 04:25:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 617f4279-a94b-36bb-9126-670c4db9889d | -8.17423 | -47.66915 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c611b22-5316-3162-b8c9-03d659357610 | -8.55964 | -47.2546 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7695e98c-9cf8-3aac-94a5-5d573827b6af | -8.76293 | -48.80184 | 2025-10-06 04:25:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cbab3e5-732d-31c3-8e94-46f7ca2d7d75 | -8.91585 | -46.58709 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b051853-dfdd-3811-9b46-4149e9c139dc | -7.81863 | -47.37852 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 719613cf-6cd3-31b4-8999-b3ac94f5aec0 | -4.77151 | -46.60356 | 2025-10-06 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 13267d6a-6e38-30ab-a6d9-a102a7d2cf1d | -8.19067 | -44.21083 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c68d4bb9-5456-3e53-93f9-59ba80aeba28 | -5.99737 | -45.46888 | 2025-10-06 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7097481e-4a28-3297-bf80-9a3ea5f554ae | -6.78149 | -41.58313 | 2025-10-06 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a82183da-f518-3a3a-a4db-0a3e3557b044 | -6.9564 | -42.05896 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b81c3254-2194-3122-a80e-e4f083bf0fe5 | -4.70691 | -45.60355 | 2025-10-06 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6839fff-6404-380d-a5b8-ccbe9c7b53f5 | -5.33612 | -43.37735 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75f41f53-0738-3984-a8b2-2a59697d6b3b | -6.228 | -45.78213 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 153ac0e2-fa51-3c17-b732-860c774899dc | -4.2524 | -48.56902 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7404a4c-908c-31ce-93ce-f6de2728ed60 | -5.76391 | -45.80846 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b64f52a-e2ea-3a3f-bbee-51bddbb711b2 | -4.31438 | -50.5456 | 2025-10-06 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d190874-a661-3c74-b24c-c3b66b43a934 | -6.6486 | -41.96843 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d976b8da-dd1b-3548-a95e-d8783bca6703 | -8.61853 | -46.29077 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6d007438-b42f-385e-b278-52c4f51a3c95 | -5.80103 | -45.81418 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55975426-d4f0-38ef-a3e0-682682e266a3 | -8.19988 | -44.15955 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 768f8034-afa2-366c-8731-cf25e0387fd5 | -8.18163 | -44.12905 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00e7ad03-4a6e-3513-ab4d-2a50af5cde16 | -7.32234 | -47.30939 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f043c3f-ebee-37f7-9bad-3f3a534e76b6 | -6.25031 | -44.2605 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8af0f801-c212-3d5b-9965-2b3963eb277d | -6.69339 | -41.38828 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e229d81b-7c0c-37ff-94e1-960cca8c9f78 | -7.20786 | -45.89017 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8280004-134d-36b2-91e1-6ab981fb8d36 | -7.44668 | -47.42661 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7858f748-fefd-3910-a9a8-b05401cb7684 | -7.34684 | -46.26696 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3c72fc3-c8cf-3cf9-85d7-c979959a003f | -8.26178 | -47.05012 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13afbc84-f434-33ac-a4f4-4f7f0987ebc8 | -8.87275 | -46.71169 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 772600b0-6df7-3724-8b74-9a152c00cf5f | -6.2942 | -42.93597 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bef9b5b9-97c4-3e63-b203-41cf5b1e8f75 | -6.22247 | -45.7742 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c84fc40-53d4-3073-af08-c5644b1d95ac | -7.91802 | -48.96189 | 2025-10-06 04:25:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51d1d83b-ac54-353f-877c-f1c9a63824f9 | -5.69932 | -44.84701 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd624e46-dce7-3ecf-a1e7-5e7cfbf86bb6 | -8.95822 | -44.6024 | 2025-10-06 04:25:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3afa90c2-eee6-37ca-bd9c-35e5fc7a7fd5 | -6.66536 | -40.91909 | 2025-10-06 04:25:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2795158b-063f-35c3-afbd-b5eebb98563f | -6.67038 | -42.77598 | 2025-10-06 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 93b5db53-f786-3969-964a-b4597f20e0fb | -6.22577 | -45.77471 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2fa834a-8b65-3bec-bced-9c3a33ff0165 | -8.57132 | -46.33321 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9fbb74e-3a41-3f09-9ec6-a37bc5009e43 | -8.53358 | -46.40205 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56de255e-dd1d-34af-8cd8-892030d5a270 | -8.37361 | -48.64736 | 2025-10-06 04:25:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88301caa-95d5-3137-bedc-3e062f378998 | -5.40338 | -45.9173 | 2025-10-06 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2094cb29-1d16-3000-82d9-cb6da299d5e9 | -7.42046 | -41.13766 | 2025-10-06 04:25:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f5f871de-ea89-37f2-87c9-b817fdd3cc18 | -7.02017 | -42.78468 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c7f33385-b61b-3273-bc33-6913c37b1272 | -8.53929 | -46.2997 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c57218c-3331-3f05-b897-e4d392e45fe8 | -8.63126 | -46.31769 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 70668fb2-b59a-3ff0-ac68-1de16ef0c143 | -7.27312 | -44.12833 | 2025-10-06 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2cf2c5a-e59c-3e04-bcde-f325eacd7b9a | -7.09944 | -45.09097 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22899fc1-4448-3e7a-862d-307bb0b0d205 | -8.52938 | -46.29815 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cab9cbfd-7353-34dd-9d51-f56eb93a00a3 | -6.06273 | -42.55404 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c1981861-43e7-3b88-a2b7-aa61ba30efbf | -6.69607 | -42.16806 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5ec9838e-9698-34ff-9fb5-0e84db161d6d | -7.7204 | -46.24813 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1676def-3d9d-305b-a171-9af000b9e1b2 | -7.54179 | -49.5301 | 2025-10-06 04:25:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fa228a2-2559-3880-9361-0e286558af3d | -5.70844 | -42.62479 | 2025-10-06 04:25:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eb8bfc9d-d331-39d4-9137-1fee5f0c0637 | -7.02535 | -42.29998 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a6a3ddec-a050-3641-9724-340355e09987 | -5.02529 | -45.02446 | 2025-10-06 04:25:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7670dfd-046a-3b7a-a282-9fe6992215ab | -4.93289 | -48.10048 | 2025-10-06 04:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c100e78-d9c3-3c5f-a5a9-23a4244bb510 | -6.7512 | -46.41616 | 2025-10-06 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50458baf-2333-3395-bbff-c93d517671dc | -7.73222 | -42.38725 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a0547d1d-df32-35be-a012-fac5365fbe58 | -7.79855 | -44.12891 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e049cfb-c02a-3ce9-9c6e-96b28fd650fd | -7.61304 | -45.46883 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7736c4f7-e3e3-36c5-b000-d0812d2605c5 | -6.37147 | -42.87101 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ae8b1d84-34a3-36ec-8991-fa29f451653a | -8.60862 | -46.28919 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54191155-71f9-31eb-a9bf-054b0ea0abd5 | -8.16003 | -47.19767 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7db6d276-66bb-37d4-a5f4-7e6584c3d56d | -5.442 | -42.94609 | 2025-10-06 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 06486915-7ab8-315c-9213-7960ef05d4fc | -7.02155 | -42.29937 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90c35d46-dd41-3e0b-b6f7-a4854a31842b | -7.78628 | -42.60336 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c6fab0e8-e88f-38ab-9f7e-adc5e25f62b3 | -8.16903 | -44.25938 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 47665276-7ef1-3dad-8dcb-d9745407273e | -8.15673 | -47.19715 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2df73af-9298-3f94-b4f3-78cf46cc47d4 | -5.70097 | -44.83637 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f3d917c-04bf-3813-a64e-a37c3a510491 | -8.3915 | -47.99146 | 2025-10-06 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec81041e-6d9f-3180-90dd-4edd9a0d484b | -4.79114 | -45.71869 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5f3ec41-f10b-3017-855c-5e163dddcf91 | -7.71175 | -42.39397 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ce08220f-a7f7-3284-902e-4d1b588036cb | -4.76766 | -46.60649 | 2025-10-06 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41fa6ed4-16a0-30f0-a5e3-ed8b305eb1c8 | -8.1708 | -44.2477 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3027448e-cc37-30e3-92db-db4d955b1719 | -7.01149 | -42.79233 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 768f6c0b-2aa3-3a86-8e89-e72d530d0dea | -8.19295 | -44.20659 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed21f93d-7983-38b5-83d0-2ca7210c305e | -8.87689 | -46.83653 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 160f0b31-d781-396b-836f-828d0ea3b954 | -5.26392 | -46.48374 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f51198b-127a-3c3c-82b6-87dd182e0fa2 | -8.19841 | -44.15996 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 953f995e-f435-3260-8a1f-2f788e8c91ff | -8.8597 | -46.09589 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae51cf3f-56b3-3cb3-ab9e-aee950209ff8 | -5.76592 | -45.75228 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82c29292-9b80-30f1-be00-f729a5c1c36d | -8.87424 | -47.61289 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd1b8836-bea1-3d8b-aa7f-c41ce0622ffc | -8.71513 | -49.48371 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13ba020c-0f69-3128-a77f-00e423f622cc | -5.02862 | -45.02498 | 2025-10-06 04:25:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa1fc126-af4b-3587-ad73-8d912dd513de | -5.49692 | -44.92125 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34dcfcc4-8a3e-3db0-9fe6-cf9f121c992a | -6.05838 | -42.5579 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f1543957-f415-3625-ab35-5bc2ed65338c | -5.69593 | -44.82467 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 618acffd-10fb-3e1f-a4ed-86e4913a119e | -8.66195 | -41.67369 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cacbc5f0-c033-3566-8af1-e211784f31e1 | -7.2511 | -44.13319 | 2025-10-06 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e4d7ce33-11fd-3993-b62a-fe8e27b8de24 | -8.54201 | -47.2162 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b7e610b3-f400-3302-891f-3d565dc3301e | -8.55728 | -46.24908 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dcbf43f9-fa8c-36db-b29d-48f4c5ae7527 | -7.79138 | -42.5947 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f6de38c-734e-3378-9ea2-8d35c89662b4 | -7.46147 | -43.04095 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f5ec2009-86e2-3bed-882e-da9c189d2746 | -7.62971 | -45.4714 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d875309e-c217-35b7-b829-129e95ce40fc | -6.62401 | -41.97466 | 2025-10-06 04:25:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6e8a4bbd-a0a7-3b1e-88d1-9e6e2c853637 | -6.8031 | -46.14898 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8ca8da3-e27d-3ee7-8e33-fc94c80540a7 | -9.20301 | -46.90994 | 2025-10-06 04:25:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1224d34e-a078-3ece-bdb7-ae94264499c9 | -6.31823 | -44.25157 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README28.md)
