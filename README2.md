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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7f1ec52-afd4-3616-8407-9ac39794595f | -7.2855 | -45.058498 | 2025-11-11 00:02:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae1e10ef-5bbd-3ed6-ade7-0dea9a29aa55 | -3.9476 | -43.767601 | 2025-11-11 00:02:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f6818a9-662f-396a-a1d6-f4c52fc37827 | -4.709 | -46.425598 | 2025-11-11 00:02:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97e844dc-34da-38da-be08-b49c8fb93a87 | -4.6405 | -45.741501 | 2025-11-11 00:02:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fea8e105-ad74-3850-affd-4c896270dc33 | -9.9768 | -44.455898 | 2025-11-11 00:02:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d3e198d-0749-3a55-99e6-14a5bf622d18 | -7.1258 | -41.258999 | 2025-11-11 00:02:00 | METOP-C | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| efc6a380-c7de-3c4e-b630-fb244336d267 | -5.6539 | -35.6035 | 2025-11-11 00:02:00 | METOP-C | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| f346922d-5a78-3602-9900-ba0caf4cb9a3 | -3.0101 | -39.933998 | 2025-11-11 00:02:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 313c9265-ad8e-38db-84de-5d8f6b87be3f | -3.9598 | -43.776402 | 2025-11-11 00:02:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cd74df2-a3bc-3069-8ff9-0087ecf4d0c3 | -3.9549 | -43.7547 | 2025-11-11 00:02:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8772aa1b-c1d9-366a-9a36-5703b288f574 | -6.3657 | -41.0741 | 2025-11-11 00:02:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 92834273-4101-3bd6-8b4d-74f6fb350e16 | -6.2018 | -41.3535 | 2025-11-11 00:02:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b6368dd-8754-3010-bf53-a1c82fa3d897 | -6.8093 | -38.4683 | 2025-11-11 00:02:00 | METOP-C | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 38ae18d5-70a3-376f-b341-21808a8d5262 | -2.8737 | -45.423199 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba3674b-0b1b-3e22-88db-6ceb766424fb | -5.509 | -39.549702 | 2025-11-11 00:02:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 57930cef-0ec9-3ce0-988a-846dc7481956 | -6.8954 | -35.0 | 2025-11-11 00:02:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35ae8d5d-5195-3361-9bf8-26fb7058d1e3 | -2.8639 | -45.425301 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43cb85e7-278b-33b3-8675-6e7cd98ad2bd | -3.8555 | -41.572399 | 2025-11-11 00:02:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0c532c58-bcca-3524-ac0e-44119d7138ec | -5.4087 | -44.821701 | 2025-11-11 00:02:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd15397e-b370-3e8d-a817-c8b0e55b65b4 | -6.263 | -43.678902 | 2025-11-11 00:02:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf166a46-3528-3ffd-9237-af6a7b3e4cb5 | -4.909 | -44.315601 | 2025-11-11 00:02:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32036c1f-eabd-3d52-9662-f4a88c4fbf5f | -6.0828 | -41.557701 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 483f0c6f-e6e6-3383-be23-98c00317f7c0 | -5.6622 | -39.635399 | 2025-11-11 00:02:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b5e278cd-2c5f-3ecb-bb29-ff8ed796042e | -4.7164 | -46.459301 | 2025-11-11 00:02:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b873fcba-ee68-3d31-b400-0cf745a89b77 | -6.2558 | -43.692501 | 2025-11-11 00:02:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcd10d9a-bba3-375e-be86-62c0b092f5ff | -5.6416 | -41.053799 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9a5d4098-b400-3d4a-ae8b-c9865debfa27 | -6.2533 | -43.680901 | 2025-11-11 00:02:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4fb14b2c-7936-3f5d-8369-9bc342dfb43d | -5.6256 | -41.0742 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef9dd5d4-f372-3042-a0d9-6c9378a018d5 | -5.6557 | -35.611198 | 2025-11-11 00:02:00 | METOP-C | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| f5948b50-4c48-38cf-b191-abc400d0ddef | -6.4003 | -38.256401 | 2025-11-11 00:02:00 | METOP-C | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 33c9d69b-238d-3b2b-a615-a0730bcc27f1 | -4.8189 | -44.741501 | 2025-11-11 00:02:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44772a37-6087-3632-bc31-92d23db6cef9 | -2.9054 | -45.291 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5316b2a-b690-345d-8b37-bffc8c96663d | -7.0367 | -39.749802 | 2025-11-11 00:02:00 | METOP-C | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 77ea0a70-499c-3757-8763-8914428dabfa | -6.7155 | -38.554501 | 2025-11-11 00:02:00 | METOP-C | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 6a50a2e2-aa0d-37cd-91f8-46c8c27ebba3 | -5.3328 | -35.553799 | 2025-11-11 00:02:00 | METOP-C | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| c4cb1b02-a763-3abe-903f-511556ec4808 | -5.4116 | -44.835098 | 2025-11-11 00:02:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f62867ca-f1ca-3e00-87cc-e370da3fb448 | -9.671 | -43.913502 | 2025-11-11 00:02:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1bd148de-2bdc-3285-a301-79ece08b6e06 | -6.2655 | -43.690498 | 2025-11-11 00:02:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 194b6ac3-c182-35c2-8421-7d83e8bd017d | -6.4019 | -38.263302 | 2025-11-11 00:02:00 | METOP-C | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 6b3b64ca-6db7-3c48-ad51-69f1a5c60fe6 | -8.4985 | -40.5919 | 2025-11-11 00:02:00 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 2d25efb1-4139-3602-a317-9a1da71bf7e3 | -5.6514 | -41.051701 | 2025-11-11 00:02:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb0490a7-9418-39fd-ba00-35c2153f12b2 | -3.8475 | -41.5826 | 2025-11-11 00:02:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ff4976fd-0050-397e-9556-a8b0021a7d1f | -6.4269 | -39.601601 | 2025-11-11 00:02:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9c1979a3-4d56-371b-b936-8c3d73ac9f5b | -6.0926 | -41.5555 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c0081ba-ac00-3ab6-ba04-321c51c7132a | -9.6682 | -43.900002 | 2025-11-11 00:02:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 104a995f-252d-3352-b9b9-06ad2ccfe021 | -2.8579 | -45.398602 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b1b0ea18-0266-35cb-ab85-20c792a79e92 | -3.8457 | -41.574501 | 2025-11-11 00:02:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f857c338-fc83-3a1b-96a5-3195ff36d2ac | -5.6372 | -41.080101 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bafd6e56-68c4-3c94-956f-7a9bd99943be | -4.9019 | -44.329899 | 2025-11-11 00:02:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d6f321c-ce52-3bc3-8084-5b969a63596b | -5.6354 | -41.072102 | 2025-11-11 00:02:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0a66bb59-4e08-31f2-a292-615165231c15 | -9.9671 | -44.457901 | 2025-11-11 00:02:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9bbcb0cd-894a-3d36-ac9f-314d90c1dae8 | -5.323 | -35.556 | 2025-11-11 00:02:00 | METOP-C | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 81934c71-0969-3d67-a454-294ac51241f4 | -2.8511 | -45.414101 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b23a520-d789-3d84-ae69-d44d47f63562 | -3.6609 | -40.893398 | 2025-11-11 00:02:00 | METOP-C | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 67a91a2c-e716-3134-8d59-14decc2b9539 | -2.9152 | -45.288898 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0879855-c01a-3dc6-bce9-0a93d3076509 | -6.2 | -41.3451 | 2025-11-11 00:02:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 885e3c9a-1f0e-3db6-a7bb-4dd64a888542 | -3.4196 | -44.066101 | 2025-11-11 00:02:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a66206a7-db4f-3eac-8a46-7545a26909b7 | -6.3339 | -38.916401 | 2025-11-11 00:02:00 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 99c6b968-e69b-3550-b602-470e12889a1d | -7.2952 | -45.056499 | 2025-11-11 00:02:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26f6bd04-755a-3804-aa76-9e2e2acb3ce1 | -7.5923 | -43.681 | 2025-11-11 00:02:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ab42d264-c609-33d6-8a0b-0724392cda16 | -2.8995 | -45.264702 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 197d10a7-c8f0-3fb0-838a-eafa272d4e9b | -7.478 | -35.107399 | 2025-11-11 00:02:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d83102a5-be60-332e-a84a-fc61c7fbc726 | -3.9574 | -43.765499 | 2025-11-11 00:02:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6badcc35-79fb-3448-9d5f-1f9e5d85f8a1 | -6.9369 | -41.8452 | 2025-11-11 00:02:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85bf2e8a-5b7a-366d-91a9-2321b760d1ea | -7.0709 | -39.672901 | 2025-11-11 00:02:00 | METOP-C | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cd7343db-5749-39f6-8371-01fc9f383712 | -7.4798 | -35.1152 | 2025-11-11 00:02:00 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d16728bf-3d1a-33d5-804c-240cc88b13f3 | -6.3639 | -41.065899 | 2025-11-11 00:02:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 802cae16-e543-3725-9edd-a088a889d41b | -6.8973 | -35.007999 | 2025-11-11 00:02:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe588a2f-b6fc-3a41-8362-72af9610f8b5 | -4.6699 | -43.235901 | 2025-11-11 00:02:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d711ce1e-52a1-364f-b7b2-2839d5e8e515 | -3.4194 | -45.347198 | 2025-11-11 00:02:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3da30444-5384-3680-90bc-75002700c513 | -6.8992 | -35.016102 | 2025-11-11 00:02:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8186bc5-9218-3984-8cec-7a0db0d2e333 | -2.9093 | -45.2626 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a5ea207-326a-30a7-9b18-e989f116fc11 | -6.7995 | -38.470501 | 2025-11-11 00:02:00 | METOP-C | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 77e12d26-cac7-35d0-8ab2-e3d737ad81ec | -5.3955 | -45.2286 | 2025-11-11 00:02:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d71dd002-0c23-3451-b2b8-6bfeec45d920 | -3.8666 | -40.9837 | 2025-11-11 00:02:00 | METOP-C | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 65a7dac0-debe-3e14-9a05-810a2bfb9256 | -3.9524 | -43.789299 | 2025-11-11 00:02:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 452db8e1-5a15-3d14-97f0-1066b3369c52 | -2.8609 | -45.4119 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 493d6ea1-11aa-373d-8fed-7cf6846f5212 | -6.3317 | -42.8237 | 2025-11-11 00:02:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ac623cf9-03e8-31be-86c6-8e13ed8d4c41 | -4.6797 | -43.2337 | 2025-11-11 00:02:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7016cd93-05ba-3ad6-8520-08f1d4e407bd | -6.4609 | -43.2262 | 2025-11-11 00:02:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2488425f-a73a-3c10-b61b-8eaed6edb28e | -9.6585 | -43.902 | 2025-11-11 00:02:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ce1f416c-f4ca-32f3-a753-cd258032509f | -6.4707 | -43.224098 | 2025-11-11 00:02:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13517810-d3ae-3cae-983d-b469ad81b286 | -2.8541 | -45.427502 | 2025-11-11 00:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90a7fd69-4a59-312f-92c2-7c03d33648e1 | -20.75036 | -49.76469 | 2025-11-11 00:09:00 | TERRA_M-M | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.7 |
| c76e30bd-958e-3769-9bd2-6211708d7255 | -21.43521 | -48.81213 | 2025-11-11 00:09:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ac8e4c93-9281-3dba-922d-c117ce769c22 | -21.43399 | -48.80586 | 2025-11-11 00:09:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 33a54a6c-18c7-3f94-b0d0-993138abff11 | -20.8764 | -49.0629 | 2025-11-11 00:09:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.6 |
| ca22121e-5baf-3f45-81a9-33315d88be5b | -20.81276 | -49.83232 | 2025-11-11 00:09:00 | TERRA_M-M | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| c7fa3a47-513c-35d7-9715-03c7ff98f8cc | -20.7527 | -49.7891 | 2025-11-11 00:09:00 | TERRA_M-M | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| abd76bc7-c8d9-37c7-8abc-ee276515bbc7 | -20.79092 | -48.35065 | 2025-11-11 00:09:00 | TERRA_M-M | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 0b140dcd-903e-33b9-b534-13217027e6bc | -20.79289 | -48.36961 | 2025-11-11 00:09:00 | TERRA_M-M | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9852f9ea-cc82-305f-8c30-666a75e98cb3 | -2.8855 | -45.4175 | 2025-11-11 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ad20a35c-330f-364f-bbb4-190f132f99c4 | -3.9552 | -43.8004 | 2025-11-11 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 04562e7b-501e-32e7-9f47-5d76d24bdf26 | -5.6436 | -41.0629 | 2025-11-11 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 004e9e71-b3c5-3512-a443-7e7c2cf9bba4 | -4.9036 | -44.3208 | 2025-11-11 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 09d39bf8-844e-34b5-84db-9b4a7bffb3ef | -3.9555 | -43.7542 | 2025-11-11 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| dd14f235-bf7c-3a97-80f4-c4e10f5ae472 | -19.7223 | -58.0491 | 2025-11-11 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| c5e24f94-41d7-3a51-9728-fd45af76fed9 | -2.8669 | -45.4406 | 2025-11-11 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 97.9 |
| b18e80ce-5b2d-3f5f-823e-a66e61ff9b40 | -19.742 | -58.0672 | 2025-11-11 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 5b4cd021-2d4a-387a-beed-1475b3ccaee9 | -3.974 | -43.7763 | 2025-11-11 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |


[Clique aqui para ver as próximas entradas](README3.md)
