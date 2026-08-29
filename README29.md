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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f768a3cd-69a3-3405-9da8-9ae819684c54 | -5.15095 | -43.79588 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4225a2c8-5a66-33bc-9923-b5bfe133e06e | -9.30194 | -56.80333 | 2026-08-29 04:32:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63577242-16c7-3cec-9c3c-cc076c76ed8a | -9.4224 | -50.43315 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5ff8808-e28e-3593-9a05-3dcc8f763baa | -6.87593 | -42.87975 | 2026-08-29 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dede0448-dcfb-3a4b-8bf4-502692752459 | -6.9504 | -45.22967 | 2026-08-29 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a03c0fdb-f97c-38bf-8afd-9187cf42e79f | -9.72063 | -47.7729 | 2026-08-29 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e42a021-a573-3015-9114-1b84addc14a5 | -6.17082 | -57.77893 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d48a03d0-4f12-3f33-bdac-47db6d765d85 | -6.95428 | -45.22673 | 2026-08-29 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b42d39f-43f6-35e1-b990-74dc2746a92c | -6.93721 | -58.95288 | 2026-08-29 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64ac170b-5fd4-3a22-bcf9-0d61a9b3bcb5 | -6.1618 | -57.78954 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0682e314-d65e-30de-b126-90cfed5a94ee | -8.59865 | -54.7747 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0793ea6-0fc7-33b4-9f97-9ebc4980efdd | -7.17559 | -43.17657 | 2026-08-29 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c4c24d9d-b260-3f86-a6ce-f18374d61410 | -4.05846 | -56.29518 | 2026-08-29 04:32:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 950febae-a86f-3d5a-a4f9-cf462977f050 | -7.50083 | -55.30647 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 68ffa0ee-1999-3f71-ae66-083d5aaa8a57 | -7.29147 | -49.9718 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78fb9b0a-0f3f-3bcb-afca-cfee32e3ad1e | -7.07579 | -42.21315 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 991d3245-fea2-3664-9391-699fd8d4aed7 | -7.28343 | -45.85709 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb1b3e37-d481-3ee7-aae8-48b88904e101 | -5.48174 | -45.12403 | 2026-08-29 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca2e8b50-f9fa-3291-a5ae-e72b8a7f8a6d | -4.16769 | -42.43574 | 2026-08-29 04:32:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0310bf7e-6294-3198-aac7-cf75a34f377f | -7.07984 | -42.79828 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ebfe35b7-a5ea-30e3-97e1-23f7180adda3 | -5.98247 | -57.68523 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4651aa28-04ce-36ac-b99c-7ef1eccf3b68 | -7.38039 | -46.5149 | 2026-08-29 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 253e4292-b018-36d3-9fce-454ddf2390ee | -9.6154 | -55.11852 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88a421d3-9cbf-3550-8e25-324066bb39f7 | -6.92894 | -42.67444 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 99c804cf-2d30-35e4-8136-4cb11df6fb04 | -4.36746 | -47.77458 | 2026-08-29 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f2a02b54-3eeb-3d98-8e60-c568ab32b2a9 | -3.15904 | -54.62521 | 2026-08-29 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fedc6a6b-c8b7-3ec3-9d8e-22186069ffc0 | -6.93241 | -42.67498 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a5f4547-c541-3b5d-ad04-d7a900ebe8d2 | -6.93577 | -58.96022 | 2026-08-29 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f622bb1f-d371-38cf-bb93-ad3b931e4f57 | -7.34668 | -55.16843 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41f00175-e066-3ec2-ba29-febd808d49ad | -4.91367 | -43.47116 | 2026-08-29 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| af1ad87b-6045-313a-9beb-cb3189c1eec7 | -7.4973 | -55.29339 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b96cc7b5-a4c2-347f-bc58-e6b55edeec59 | -6.94926 | -58.95587 | 2026-08-29 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26583a47-47ea-33f6-992f-7f520b51de94 | -5.34134 | -45.15559 | 2026-08-29 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dead0082-cde9-32d4-b489-1aceafee3469 | -9.30892 | -56.79989 | 2026-08-29 04:32:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29e02c41-6ebf-34e0-9231-1427a2c06b3c | -5.89966 | -57.7518 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 594d0f37-1213-3f23-96bb-9918c669873c | -4.18504 | -54.57275 | 2026-08-29 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79449557-195d-3c43-9f9b-a9dd12c2b764 | -7.27952 | -45.86008 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f98211f3-a407-35e8-b9fe-ac3d9f10c293 | -8.99103 | -50.79294 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f80f6527-7999-3b96-8b63-708bf03e270d | -7.05944 | -42.15312 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a2ea76fb-28cb-34fd-a8b4-b0514e737720 | -6.62502 | -43.7332 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| b6946e84-9b5a-31da-8d42-39ea86f5d755 | -6.62391 | -43.74031 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 52a04514-ea18-3cc2-b098-d8441cbe4e49 | -6.17483 | -45.9307 | 2026-08-29 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24135a41-afbe-37b1-a692-637d2b1aa4c7 | -5.14123 | -49.93286 | 2026-08-29 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58be0b7e-4219-32b8-ad97-2492da3babcd | -8.59347 | -54.76688 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfd57d54-9357-351d-91c8-36a66bce5b53 | -5.80721 | -43.79781 | 2026-08-29 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbfea727-1c22-3603-8dd7-cab552fd623c | -6.59074 | -51.63685 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c98bda50-8696-3f8e-bc80-ba074c8e1e3b | -11.25655 | -45.05803 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1dd7d95-1cd4-3f1a-bc0e-5f2c7ae24fc5 | -8.28006 | -49.272 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa221538-ba63-3059-ad30-247942581d23 | -11.23652 | -45.07677 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24e6be34-3602-3c3b-87c5-6686e56d6c8d | -7.11405 | -43.16697 | 2026-08-29 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1035fa6-556d-3d9f-bbe6-79ef09ccb880 | -3.15552 | -54.6248 | 2026-08-29 04:32:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d749ded-010a-3c57-89d4-fd6fcb951175 | -7.20151 | -42.73411 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ff75af58-79ce-3399-b3cd-f0a6207557c8 | -3.87514 | -48.04668 | 2026-08-29 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08a48cd1-2aca-30ed-971c-52eab964df62 | -8.58869 | -54.76226 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6907f3ef-1a98-3be9-8918-69aba71ea99e | -8.98839 | -50.79242 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79dd2449-a677-3bf8-b3c7-e9c0f14088ec | -7.60534 | -47.28471 | 2026-08-29 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6e746bb-6ca8-3f8e-af3f-1177998ac961 | -7.0781 | -42.80964 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f96c6cc1-e32d-3b3c-af77-7e92adf5a5fe | -7.2657 | -45.35537 | 2026-08-29 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 415da0b6-08b2-3d5b-b283-dd7e5fd3ac59 | -4.17111 | -42.43628 | 2026-08-29 04:32:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e0810cf-bcb8-3e3c-8806-28f48e1d0fe4 | -8.53495 | -55.26502 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 194b8297-bac9-3f54-b605-15b8695c06c0 | -5.64921 | -44.30167 | 2026-08-29 04:32:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7390c5ba-adc7-34bc-b127-6bfbf513cc45 | -8.58924 | -54.79474 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6730f3b-d66b-3662-9f2f-0bd2c6297ca4 | -4.05936 | -56.29018 | 2026-08-29 04:32:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f33352b2-c4a0-3c84-9d15-38e1b52a6ba6 | -5.28941 | -50.94074 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bff2e481-b0f2-37ad-8f42-18043f4ef6b3 | -6.61945 | -43.74689 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9482d4ff-de3d-3ae1-9a45-4ada2040eec8 | -8.9458 | -50.80836 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3911a463-3717-3778-9540-91862626e391 | -5.41551 | -43.18475 | 2026-08-29 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c17afb2a-df4e-3c4d-baee-ce139ed7f1d6 | -8.9751 | -50.78658 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eedb4f79-f45f-3c23-bbdc-85295ac4dacf | -9.60797 | -55.13026 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 43936d62-080d-3586-87e9-ee2eabf3c14a | -7.26681 | -45.3484 | 2026-08-29 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5311af22-17d4-3e5c-9ace-8c4770469ba0 | -5.88931 | -57.76916 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 21ebd9b0-e950-3ea5-8e8d-c520f99074b0 | -7.50583 | -55.31156 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 6b9c340e-5851-3b29-9dc5-c07aec66e09b | -6.63399 | -43.74187 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5b0561d1-4be7-38ae-addc-92edf7a5d751 | -9.15681 | -49.97257 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d73692e8-b389-3c26-9ec2-157d358976c2 | -6.77122 | -55.67992 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f66038e9-aef1-3b7d-992f-d69b47670596 | -7.28467 | -49.9592 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82afde90-162d-34d9-8801-270d315d5828 | -6.33905 | -44.08968 | 2026-08-29 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8a7e861d-0661-38be-9b96-5342aa6276dc | -8.32933 | -47.6253 | 2026-08-29 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddc76f56-3834-3e39-85b0-20fec3087643 | -4.97221 | -49.61891 | 2026-08-29 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0661e3bf-af24-35c4-967a-043ad2164607 | -3.43767 | -52.76358 | 2026-08-29 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c43f55ed-4047-3faf-a567-c61ad7c6a772 | -5.89176 | -57.75621 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 49101ab8-7d62-3163-8e92-26834665bd80 | -6.90571 | -43.65282 | 2026-08-29 04:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f4c2c5c-211e-3ad4-9dbf-19359c52f4ce | -11.36449 | -45.14883 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f4df2ab-b416-31dd-8e8e-2f4031fbf190 | -4.36448 | -47.76968 | 2026-08-29 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4fa68493-0148-3b5d-8757-76eb50ce6cc2 | -8.99166 | -50.78926 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a25606d-87e4-36e3-ac22-5d84e0dae741 | -4.36816 | -47.77026 | 2026-08-29 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e9ec6c43-aa91-3812-a1fb-fccc4e0698bb | -9.42345 | -51.68798 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c135128-aa9a-3d97-b924-e4ba5ea8e9a8 | -7.12322 | -42.76995 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5f223935-e0fb-32e8-b3a8-0e94dcee2853 | -8.8217 | -49.63329 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7dfaca0-f7f3-3ab3-91f1-c27efe4a6bb1 | -6.40583 | -51.67508 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83e86255-8796-3be2-8649-ecc5f70d01cf | -8.15926 | -46.17567 | 2026-08-29 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b4093c2-395d-3651-8189-24493fee4db4 | -11.25378 | -45.07589 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e092738-e906-33f1-a7b0-ad3df85f89cc | -4.06461 | -56.29438 | 2026-08-29 04:32:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e791182f-d954-3590-8a66-b8545088fc0b | -3.43248 | -52.76276 | 2026-08-29 04:32:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 255233e6-e245-3a2e-8f43-b1265325cf05 | -8.59975 | -54.82868 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9659fcac-238b-3da6-be1d-e3c72ae1952a | -6.53412 | -55.24775 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 875b5240-9937-392d-96e8-06824ec15fd1 | -3.22201 | -48.61347 | 2026-08-29 04:32:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4f043b5-68fd-37de-8fb5-9c580860ecd6 | -7.34169 | -55.17014 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71d9fd52-393b-3e50-b8c7-05f906cded0a | -8.5982 | -54.80281 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ad58262-132d-3ab8-a5ca-abab09b0cd10 | -8.15868 | -46.17923 | 2026-08-29 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README30.md)
