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
| 54bd5e60-4c59-3642-ba65-7c9cbc695d3e | -5.83332 | -42.33427 | 2025-10-15 04:06:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 62630ef8-5664-3d75-af50-3f9f164fb0f4 | -7.57313 | -42.69921 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 47eed49e-d539-3db6-a002-9d042678cc98 | -5.33722 | -42.57486 | 2025-10-15 04:06:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1593ffa1-05a5-3f0c-bb54-d1e9584e44a9 | -8.28191 | -43.44171 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed979f9c-dad3-32f3-a84d-be606ab9ec5c | -7.26235 | -44.91413 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 695f83c1-995c-319c-8971-2b2e933bd2a8 | -7.56872 | -42.68392 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eeb016cc-1a44-338a-b911-d9052af476f8 | -6.55227 | -43.93008 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 01dc836a-a3a6-3494-ac41-8f489aaa30eb | -8.18445 | -43.97179 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04b50bc7-31ba-363e-ae9b-a64dfcd538a1 | -4.68581 | -45.83619 | 2025-10-15 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35bb3a0f-8881-3b9d-94f5-7e3635aa866f | -5.43542 | -44.30891 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5168088-075b-3d74-b436-b090072c4a57 | -4.90064 | -43.45602 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| adf716ce-024c-35c1-8ed8-6805e74a7a36 | -7.16164 | -42.50991 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f170327c-cc24-3b7c-8372-5c7554fc7d23 | -6.5865 | -41.50974 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 059944a1-b2d1-3d89-99a2-a47d9d0a2620 | -5.27418 | -41.04398 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6319dbfe-3265-35ad-b137-d9fe3b33283c | -5.47507 | -44.66082 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff80cf0e-bda0-398e-ab42-4f9c73a0ded5 | -5.41234 | -44.22397 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dc4c1e9-c53d-3052-ad11-3f0c850f0669 | -4.65105 | -43.13806 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 605b792a-3825-33f5-8058-5d4a15289bc6 | -7.57427 | -42.6921 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2061670-7a20-39cc-b614-753ee31527ed | -5.09997 | -42.63422 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffb82a2e-68bd-3e9b-addb-6c57eba50bcb | -6.91982 | -41.37907 | 2025-10-15 04:06:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84967cc4-7983-3813-bac7-c1e13a95fa05 | -5.73406 | -41.31451 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 96c76567-2425-3df0-bb55-7d1819a78b59 | -5.43904 | -44.30949 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26b264d9-4043-3ae9-859e-39e23018a907 | -6.39783 | -42.52568 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e23fc3bc-935d-37dd-8513-0a1aeed7227b | -5.57232 | -41.11197 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd08e677-01d2-36e9-b62e-6f1e3bfcdb81 | -4.64904 | -44.70026 | 2025-10-15 04:06:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f95842a-eb88-3622-88bd-b67f5117553a | -3.97406 | -43.24708 | 2025-10-15 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dcc882f-e647-39fb-bf82-c01a35b5f521 | -3.43052 | -50.25661 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32ab8caf-f7d9-3dc3-9d8a-b31ce940791e | -5.42645 | -40.98306 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e90fa869-922a-3ead-82c4-48674c65e88b | -4.89872 | -43.46775 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25ee9734-b9ea-3065-95f9-a9f59d765ef0 | -6.17555 | -44.30181 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b1b90ea-75ca-3dbe-acd2-5e299e58e1d6 | -2.92622 | -48.30239 | 2025-10-15 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 4e25336c-6179-3212-b20e-eb9a6019eeb6 | -5.32062 | -42.90133 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f389310-44e3-3dfe-b645-24ce1d0069f0 | -8.19986 | -43.98614 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 881422ff-404b-3a22-96a4-f3952dc1da5a | -5.16243 | -45.16563 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a42c52a-609e-3078-8286-39f416901f92 | -6.25881 | -44.34393 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61122ad6-d353-3d3c-b026-e04881cb84f8 | -9.25392 | -44.36476 | 2025-10-15 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d8124eda-70ad-346a-b0f8-7eb8d5043ae1 | -6.77739 | -42.12792 | 2025-10-15 04:06:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 72268227-7247-3d42-8968-23ea72f71052 | -5.40873 | -44.23832 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bfb3934-3b4c-31b9-bfbc-3439f6996950 | -4.9 | -43.45993 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ef8b60c0-3c9f-3ff7-abe3-2c1fa6a6d7d8 | -5.97463 | -42.91384 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 03aa8359-8dc8-3af0-8ec5-757cc4b94d21 | -5.15861 | -45.16504 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76fbedf0-b5f1-37b9-a3c6-89a241941086 | -4.70064 | -46.46186 | 2025-10-15 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8ef885b-8d3e-30d4-b540-ace1018e336e | -8.26558 | -43.36456 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2934dd9a-96d6-3ca6-bfc3-5ebedf2c0ea2 | -7.67164 | -42.37843 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 97abb361-ca50-3b07-bd44-93634242b46c | -7.43893 | -46.74989 | 2025-10-15 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ca35847e-bc3a-39e3-ad44-5b309a245d65 | -5.15606 | -45.16194 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b65d8c9d-59ff-3176-b54c-646ce9ea39f9 | -6.5774 | -42.957 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 829fb639-db41-3671-846e-83f736f0e442 | -4.25297 | -45.57975 | 2025-10-15 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0483b24-bd35-363c-8843-ce9b99bc3bc0 | -6.37931 | -41.48773 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b908b2a7-2fad-3a46-a2bb-1f40207c23ff | -5.94779 | -42.31963 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02105c7f-8348-3f4c-b5c7-904b8a9da0d6 | -7.55413 | -42.7107 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 569934f9-697f-3e79-9a95-484ba9063403 | -10.16316 | -36.17408 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e4cb8915-30cf-38bb-ae67-e20a2956349e | -5.87554 | -42.7891 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5d248d41-60d0-338a-b948-72c7f283ec81 | -7.75303 | -42.44546 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1c7eff57-bb01-3201-a4c8-89c8513670d9 | -5.69298 | -43.55069 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 651a22d8-125c-3b4a-a2a7-b401cea638c7 | -7.25498 | -44.91461 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a28c154-f635-3797-928b-6ee97fadb7c2 | -4.91108 | -46.71286 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6229887c-38bb-300b-8f26-857483b63a9d | -6.11304 | -46.34264 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5fd4ad8-3d9d-3bc8-8c0d-f7d8718a0a76 | -5.42921 | -40.98703 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 97366a43-3c60-33d7-ae08-f978913368ca | -5.4447 | -44.29755 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d28d942d-dbc4-377b-a05c-e5ab72424341 | -6.5281 | -42.19904 | 2025-10-15 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1c2729f1-458b-310b-a6e7-bac3720e8789 | -7.93629 | -44.135 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e467d1f-7181-3db3-b668-534b28afbee1 | -7.13329 | -42.4945 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83b73bdd-a118-3d10-927a-8832bf4993e7 | -5.61279 | -42.71861 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc78f047-256d-3fc0-bc94-02f21704ef3f | -5.5742 | -43.02508 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9752efa1-d8e0-3051-a7d9-d7d2b3284c6d | -6.38701 | -41.48187 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ff424021-66b4-3db5-8aff-5cb4efd09634 | -6.3374 | -44.02356 | 2025-10-15 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3f48684-51d6-3d31-8350-0548257f6648 | -6.83091 | -42.77444 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be25f488-a656-34f3-a315-fdc02e72a4dc | -3.43055 | -50.25616 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b96a0d10-aad2-37ac-b9cd-c312de1aba2f | -7.81348 | -42.10748 | 2025-10-15 04:06:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05e126e1-1631-37dd-94ba-4492c831b5b2 | -8.18791 | -43.97236 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c27817d4-d03e-3e85-bba9-43ed637a8cda | -5.41709 | -40.97807 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ca815e8-e155-39f8-a16f-547ced79f5d6 | -4.9001 | -45.50782 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d9fd600-7207-3e14-bbcc-a5b2bbf297dc | -6.01167 | -42.87842 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 45a8906d-a7ba-3b8f-89aa-3b0c1ea64d67 | -4.94276 | -41.72122 | 2025-10-15 04:06:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7875539f-5795-308b-91a6-d3c65228008e | -5.5861 | -42.84173 | 2025-10-15 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 64902d2a-ab4d-3e1f-bc4f-414bc0421163 | -5.1863 | -42.90685 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c93e074b-5ade-3c70-b525-42f47f06d675 | -8.19538 | -44.10032 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d11c96b-e9c1-3566-814b-9466ea49e2ae | -5.86787 | -43.85833 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2509bf4-8837-3a7a-8796-da948ff5659e | -5.79421 | -43.88782 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41cc0618-09e1-3645-bef9-2b8ae17c17e6 | -4.89936 | -43.46383 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 9b047ece-5fbe-30bf-a4d8-8bf891863ef7 | -6.16187 | -44.38451 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c44d6e47-11ad-3a46-b769-39053a1cde77 | -5.91823 | -42.82591 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 21926f39-3ea7-3e60-9413-f41bc6241e75 | -7.56929 | -42.68037 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ba771c8b-6b9b-35d6-8e3c-366992238c63 | -5.67269 | -44.25532 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 134b56f3-8108-30c0-8ea4-8549546e3724 | -6.17934 | -41.722 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2cfa5a47-c506-3de4-a4ea-501c4fb5a421 | -5.39768 | -40.88337 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ddcdc34e-084b-3c85-a247-53e173c03e2d | -3.52904 | -50.31089 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6da86816-8317-3bc2-901b-031cef513938 | -5.86596 | -43.87015 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f58c0df9-a16e-37f3-a670-c2f06fa9d750 | -3.9217 | -45.24592 | 2025-10-15 04:06:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 320b104a-d885-364a-8790-1fd3a93176c3 | -6.22721 | -43.36757 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b757468d-2e36-37e0-b517-4e38676799f3 | -7.58301 | -47.20531 | 2025-10-15 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5cdea55-f29f-3015-96b7-f2d8ca3f0222 | -5.92558 | -42.82342 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0ea0f1b3-f348-3eb9-8674-52a7b037a632 | -4.59857 | -47.03279 | 2025-10-15 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3a236e2-27bb-3d53-8fc3-93bfc6a3ffc4 | -5.97262 | -42.79745 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1559483d-eb72-3e77-ac41-a0c942dd6b30 | -5.2525 | -43.47493 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 522b0925-74b8-3730-adaa-4c0815a5029e | -6.04902 | -43.38685 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 163ff182-2241-3b4e-a65b-f3d9628d595d | -6.42907 | -41.83973 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ea1c661-2fc5-3fe1-b8ae-8f66c9530f81 | -5.18289 | -42.9063 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73f0c83f-357f-321c-a2f3-ce497ab8ebac | -8.20656 | -43.32116 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README24.md)
