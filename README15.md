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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c407a60-7a77-379a-81fe-5d62b36f94db | -3.91021 | -46.90304 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 538580b3-666c-34b1-a2f6-628811869a0e | -5.91102 | -43.49201 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cc46ce21-4d3c-3993-9956-244a180447d3 | -5.90937 | -43.48121 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a09ecca7-045e-3b7f-900f-1bba9af855e3 | -3.90325 | -46.98305 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93474159-1843-32ef-91cb-70618cca3b5e | -5.64471 | -43.71381 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ef1e9580-d08c-3ed6-929f-84ca06bc822d | -5.65169 | -43.70635 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0afd040-220d-3a56-a37b-a0eeb0850e5c | -4.56545 | -44.12753 | 2024-12-27 04:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e935f313-df6b-3f3e-b664-5c6632cbae62 | -2.52321 | -51.85419 | 2024-12-27 04:57:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00b78087-8702-33f8-91a5-a74b48aafead | -3.92615 | -46.986 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 27cf5965-8132-3d53-bbf5-094c21f506c1 | -5.90567 | -43.48664 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 67f94f32-276a-3963-bd56-95ba4256adad | -5.64 | -43.70446 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b9ebe0c-0be6-37ea-bc28-e8e9c01ded88 | -5.64645 | -43.70758 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0a91825-c9fe-3f19-8ce8-b5cd8bf6fe51 | -5.90625 | -43.48237 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b41e0493-846e-37eb-839a-4240d617ec54 | -4.03616 | -47.06047 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d0437a2-cb4f-33d5-a5cb-c3602cbe9e36 | -5.31554 | -46.05824 | 2024-12-27 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bbf1612-53be-37e0-b6d8-5bf09aaad396 | -5.65111 | -43.71061 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dcac0a0-6cb3-3c49-b360-a331cb07f6ad | -3.7379 | -47.18004 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8b6032c-0454-3a75-8cb7-046905a7f5dc | -2.91326 | -54.01024 | 2024-12-27 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d476394c-39f8-3546-981c-3b5cc839c6ee | -2.40106 | -54.18671 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ed62f22-e3b1-3496-8708-f5b728b7c231 | -2.40162 | -54.18322 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20fcf7b7-ed82-3af5-822b-a11c87d6e916 | -4.52672 | -42.06238 | 2024-12-27 04:57:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 86b51478-1ffc-3b2c-83d2-3c01ba6b8974 | -5.63888 | -43.71275 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe438731-290c-32be-8455-df3af7c628bb | -2.52661 | -51.85472 | 2024-12-27 04:57:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c759228-624a-36e0-a7a2-10a093d0f12b | -3.91015 | -46.90567 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc048134-3c5b-3cb5-8308-a590466fa5c3 | -3.91088 | -46.89842 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bef0759-f620-3d4b-a7b8-e483a16ea952 | -3.75936 | -47.21972 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6529bd5c-bc0e-309f-a1b6-f898fa1d8a07 | -5.13404 | -43.24162 | 2024-12-27 04:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aee7b686-b829-3ab4-9c80-cc8835047cd8 | -3.91116 | -46.9297 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 419012f8-47b9-3244-8a79-5d9abeba4dd6 | -3.49956 | -45.75567 | 2024-12-27 04:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e539c84-e990-3500-96a6-ad3bee0977a4 | -5.65168 | -43.71274 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b17d393-26f1-34db-999f-cfb8795ce10c | -3.9066 | -46.92888 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db1703f5-70ba-3f6c-9b8c-18608a512a50 | -3.93985 | -46.98809 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ab57bb95-97a8-317f-864e-9f8dd47741cf | -2.49317 | -54.13644 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a554935-986e-30a3-bd03-496e31ed6ae9 | -5.63883 | -43.71906 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d8b7ffdb-60da-37c6-90fb-8512ee5127d6 | -2.80023 | -52.89801 | 2024-12-27 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36f477f3-be07-3927-ab6e-64e708fb541c | -3.03795 | -53.24035 | 2024-12-27 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14ab2f81-34a7-305e-a69e-0f6bcfb8dec2 | -5.94847 | -44.44933 | 2024-12-27 04:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfc06114-40ff-3be2-8698-74250f9041ca | -5.90222 | -43.48872 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e6fb8dd-d459-36d0-8e6a-e520195dd6e7 | -2.64988 | -54.66534 | 2024-12-27 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59ea3724-35fd-3ce2-8181-104b716621b6 | -4.50495 | -44.23255 | 2024-12-27 04:57:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d67f50a-8bed-31cd-a7dd-8d616d15f595 | -4.51659 | -42.08118 | 2024-12-27 04:57:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2a16445e-f697-3832-bff4-9a42bb192993 | -3.93529 | -46.98734 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b4cbf98b-4c12-3a66-9594-d70da7426dc6 | -2.64932 | -54.66888 | 2024-12-27 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba608b9-cfd9-36d5-80ca-702b2211cb82 | -4.52599 | -42.06758 | 2024-12-27 04:57:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 023af840-d4ea-3581-b915-a2ede05ffc28 | -3.91345 | -46.91305 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c58f4834-e70e-3c0a-bc16-9818cf0adac1 | -3.74866 | -47.1998 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a023ddc-4092-3a11-97b3-02dae40cabbf | -5.90876 | -43.48549 | 2024-12-27 04:57:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1f5f28d3-c6c9-34a9-b0e5-680dcadecc9c | -3.73274 | -47.18376 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97889251-9596-3dc0-9709-0f6b95e09bbf | -3.82386 | -46.05394 | 2024-12-27 04:57:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bf467d3-6ae7-31b1-8c50-785bd0fe86f2 | -5.63831 | -43.71694 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82cdbd38-03fb-33df-af7b-0ed194f861c5 | -2.75538 | -54.04234 | 2024-12-27 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24298d3d-bd3b-3b92-9b56-b7cf709ad9f0 | -3.68919 | -47.16788 | 2024-12-27 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f7cb8ed-aa86-33ef-af0d-5e515d0e5450 | -5.63721 | -43.72509 | 2024-12-27 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b021937-14da-3185-bdd8-1ca0a3d1f6c4 | -2.5164 | -51.85314 | 2024-12-27 04:57:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3bd646f7-932c-3b48-992a-23fb6aee0c52 | -3.93917 | -46.99264 | 2024-12-27 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4125a9fb-c35b-3af2-aa52-9f10aa451f68 | -3.91412 | -46.90844 | 2024-12-27 04:57:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dea98c6b-78ab-3280-b418-144702068907 | -12.35312 | -64.17418 | 2024-12-27 04:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33f0166e-f9ed-30b7-a1d6-f48694b3c057 | -14.5274 | -59.74737 | 2024-12-27 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d297d2-ccf4-382a-b7f3-ea95a8f077f8 | -12.34809 | -64.17315 | 2024-12-27 04:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38e46975-ca5b-3ebe-9a59-0fb80bf5bb15 | -15.42109 | -59.05578 | 2024-12-27 04:59:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 326fdac0-7a4d-328b-941b-30b79593d3fe | -12.33726 | -43.67422 | 2024-12-27 04:59:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e2cc9de-c4c5-3fb4-9ec4-277310066de7 | -12.33662 | -43.67961 | 2024-12-27 04:59:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dedb0fb-f3c3-3cb2-adff-2a69d5d681f2 | -12.33839 | -43.67279 | 2024-12-27 04:59:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d64cc806-2737-3c6d-a627-c36a3c575c61 | -21.51626 | -57.17742 | 2024-12-27 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 74468fd3-0776-33f4-a2eb-140f10bf7963 | -20.02512 | -55.32778 | 2024-12-27 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46ee813a-b0c4-3779-ad50-c3acf804b49d | -23.09761 | -52.0978 | 2024-12-27 05:01:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac0019e4-8122-36d0-b743-85062d25d1e7 | -20.47875 | -53.67408 | 2024-12-27 05:01:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85a40af8-d42c-3349-b3e5-9f7857978b14 | -19.02238 | -57.62263 | 2024-12-27 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4ed27ee8-8d74-3296-8c00-6a66406d13a4 | -16.19237 | -58.95996 | 2024-12-27 05:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 24cb159b-3436-303d-9040-14ba40203324 | -22.0034 | -57.30209 | 2024-12-27 05:01:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fbf263c-0e4b-35d0-93c7-fabc700969e8 | -23.10186 | -52.09853 | 2024-12-27 05:01:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9114ed89-1577-3f46-ad04-28d6f0ac9728 | -22.00675 | -57.30268 | 2024-12-27 05:01:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 939e0157-fbf8-3803-be94-5266ab6e66f2 | -28.03897 | -55.20322 | 2024-12-27 05:03:00 | NPP-375D | PIRAPÓ | RIO GRANDE DO SUL | Brasil | 4314555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0272c003-c48e-32f5-b9b2-12d33c6889b6 | 4.07204 | -61.05261 | 2024-12-27 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f9a19f7-a520-3742-8b77-2eabadeccb25 | 3.31752 | -60.08408 | 2024-12-27 05:18:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85e0bef7-a778-3df1-a479-2e7cbd33e2b7 | 3.60186 | -60.04078 | 2024-12-27 05:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 225143a6-8c52-3265-93b1-7aceadadab81 | 2.93418 | -60.29987 | 2024-12-27 05:18:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06b5d285-793a-3243-a045-45eccac4dfd7 | 2.66621 | -60.46995 | 2024-12-27 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7979448-6c61-3a5a-88f5-6c7daf92c7c4 | 2.9336 | -60.29618 | 2024-12-27 05:18:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9f956f0-83b8-3bf4-b75e-6bc2ca1530f0 | 2.93076 | -60.3004 | 2024-12-27 05:18:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5fabc51-273c-327a-af90-c2cfd893bd40 | -3.94126 | -46.99908 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fb104132-c083-39b0-a7f6-54ab5a489410 | -1.60583 | -53.37053 | 2024-12-27 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6f93d61-ed57-324c-99f5-9adcf19cbf12 | -3.93143 | -46.97976 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a2f68250-59ad-35ab-8016-c9dd3dbc722f | -3.20653 | -52.44324 | 2024-12-27 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2672e4dc-cf26-3f71-80a5-1421b386a904 | -1.5832 | -53.38885 | 2024-12-27 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71bfa724-0b60-3e4e-b04b-a5033d74a0f9 | -1.58383 | -53.38482 | 2024-12-27 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b06c0e85-1505-346a-9805-1fd6fb6b39d3 | -3.07073 | -47.77394 | 2024-12-27 05:20:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7ef2fb8-b01c-33cd-ab9b-3d402675d1e4 | -3.93622 | -46.98601 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a1db74cf-6570-3faf-a6a1-fe8883209cd4 | -1.88774 | -53.28696 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89b90730-a264-3311-8107-a8f1c0e92139 | -3.00262 | -48.05742 | 2024-12-27 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aedf0d9f-f6ed-39ba-9437-d5d12ee5353d | -3.93576 | -46.99857 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3eff34d1-6d75-3306-9ce0-4994397203fd | -1.35238 | -53.67708 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6020ac9-e74f-3e54-a19e-1ca35b4a5ec7 | -1.55262 | -53.50032 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e38269b-cacd-313e-b387-dea14fa8babd | -1.16992 | -53.73724 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c925aec2-e421-375d-8e37-6a1b4609a7c1 | -3.92941 | -46.98505 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c314c6c-070b-3659-87c1-83e9b57e1a0b | -2.15718 | -53.72835 | 2024-12-27 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4c9173c-533d-3e3e-9dbd-73bb7f819cc6 | -1.1884 | -53.58984 | 2024-12-27 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feaa9ebf-a1ab-36a4-9b87-ea2bdf2b46c0 | -1.12531 | -54.13277 | 2024-12-27 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81d054d4-33c6-3ee6-a858-751315753dec | -3.14158 | -46.34608 | 2024-12-27 05:20:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28a16df9-80b4-336c-98d1-183352175182 | -3.93743 | -46.98658 | 2024-12-27 05:20:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README16.md)
