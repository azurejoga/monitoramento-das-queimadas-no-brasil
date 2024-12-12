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
| 24579574-f968-3dd2-bf57-43a2c9da854a | -3.04497 | -53.83209 | 2024-12-12 04:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc8c6f9a-27ca-361a-bc33-0f2198a01379 | -2.79062 | -53.23906 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50433575-3f6b-3169-a760-04fdea241265 | -3.78307 | -47.0967 | 2024-12-12 04:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7443dab3-6182-395d-89c7-badcd4bf41a1 | -4.54951 | -43.5737 | 2024-12-12 04:59:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0193ade-5c1a-347f-a8ae-f1188d75b983 | -2.43932 | -51.79121 | 2024-12-12 04:59:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8902ca66-af17-3204-9857-765facad9f2e | -2.56844 | -51.88748 | 2024-12-12 04:59:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 738b5e47-073c-36b4-8655-004eedcb76cb | -2.27441 | -53.48568 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d7c619f-86eb-363c-9664-819c49bb84aa | -2.82327 | -53.07325 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 316ac629-8fb9-38e0-b3db-9fb9d5bbbc0a | -2.71954 | -53.17653 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8461d969-b9f9-3e99-80e9-2602fe7f53fc | -2.08068 | -52.28207 | 2024-12-12 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce401770-dac8-33fb-9739-af69f45efdaf | -2.6471 | -53.35341 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea69797e-840b-3e3b-b5d8-6727b31a35a3 | -2.78622 | -52.86088 | 2024-12-12 04:59:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bcd49a3-bf4e-3baf-be1a-8baeb3b09069 | -4.09577 | -46.67565 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cb92fff-89d2-393b-8188-c6e32ae064d0 | -4.08631 | -46.61167 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 620e44aa-e872-394d-9233-e179892cd866 | -2.82044 | -53.06907 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a06e7ab1-9939-349f-813f-b09a94d27b91 | -2.71078 | -47.55606 | 2024-12-12 04:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 108a00b9-47f2-39bd-88c4-8eb1046b1e46 | -3.04108 | -53.83509 | 2024-12-12 04:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfcf9162-fbb3-32fe-a732-0ecc3c9ab136 | -1.81392 | -52.69172 | 2024-12-12 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ea085d8-fec5-39c1-bd96-26676c60bc1a | -1.815 | -52.72959 | 2024-12-12 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bad5a04a-60f2-3531-acc3-d02b0f4b9083 | -2.81024 | -53.0675 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8329458f-df4a-3f21-94bb-b81abe95a6e3 | -1.63914 | -55.10511 | 2024-12-12 04:59:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e08c2fa0-55fe-37b6-905e-21494af2c97a | -3.10833 | -53.24719 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62e1d691-796d-300c-9b4d-b4875a1b33c9 | -2.64092 | -53.34878 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 894164fe-bb72-39a5-9903-7f26a22fa58b | -3.19536 | -52.86528 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abdbb994-7a30-3cb1-92c9-3651b84ca0b5 | -3.04831 | -53.8326 | 2024-12-12 04:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb933477-3cfa-3abf-981a-806b6f3e259d | -4.07317 | -46.12263 | 2024-12-12 04:59:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31b7b754-4a50-360c-9389-f62eaae992c6 | -2.78678 | -47.6391 | 2024-12-12 04:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d45ba220-82e9-3dfb-bc60-3a96e2e3219b | -1.61474 | -54.67806 | 2024-12-12 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a986280-c547-3ce7-9105-d3b62391a37e | -2.81419 | -53.04191 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d599b877-49f6-30ef-8ab3-0b621df1dee8 | -2.81647 | -53.0722 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0fb70d9-14a6-39af-9635-35f5eedc8732 | -2.56905 | -51.88347 | 2024-12-12 04:59:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff163715-f65d-3a8a-8e3c-735c2913d642 | -2.9602 | -48.61345 | 2024-12-12 04:59:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12c8a632-68d3-3321-8927-8316029a91d8 | -2.81703 | -53.0461 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9fdd24b-fa10-340d-b3a9-7e41eb077765 | -2.64152 | -53.3672 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ca75498-4076-35b5-99cd-a513279598b4 | -3.21225 | -53.00464 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd27bcb1-8500-395a-9675-5461acee0ece | -1.8663 | -47.08578 | 2024-12-12 04:59:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdc7c61f-c361-3573-b503-85dbfc90a67c | -4.01715 | -46.96979 | 2024-12-12 04:59:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16ece54d-9a22-3249-ad0e-abc935b55477 | -2.55949 | -53.41712 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d94d1049-9706-3ef7-b0e8-ff941018264d | -4.07804 | -46.12633 | 2024-12-12 04:59:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4382d090-602d-3366-9c67-a5bb6e105597 | -6.92 | -43.52 | 2024-12-12 05:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11189e72-583c-3544-acc7-e388203746b8 | -3.2503 | -46.8709 | 2024-12-12 05:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 5861e1de-95e1-369d-9a6d-03a2f87ba13b | -11.2148 | -53.833 | 2024-12-12 05:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 1fdd84c0-f4b1-37dd-b82a-718d0596ef6f | -14.7457 | -52.6683 | 2024-12-12 05:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 458403a0-075f-3f40-86c3-fe1ea25d6f05 | -11.1959 | -53.8348 | 2024-12-12 05:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 894aec19-b670-359c-9440-ad20bac70c40 | -14.7655 | -52.6446 | 2024-12-12 05:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8e8071b9-68ac-369c-a890-bd0ae5f05cf5 | -14.7461 | -52.6471 | 2024-12-12 05:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| b08d56e6-fb02-3a46-8aa9-4e12e3dce2dc | -7.47457 | -44.74112 | 2024-12-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6bdf2bc-8820-3977-8b36-564f1d4cdf39 | -3.59892 | -53.71856 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d2a2842-5a80-34fb-95c6-ffce50fcb605 | -10.10071 | -55.43626 | 2024-12-12 05:01:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb1a635f-f2aa-3103-8019-c12471e6c2f6 | -7.94658 | -49.75127 | 2024-12-12 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7df3eb3-ecca-39b6-a581-04b5342f6939 | -4.02261 | -53.9865 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dae8c76f-cc97-38e7-bd21-e881cd8ff68a | -5.92407 | -48.05692 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f4b01a8c-659d-32cb-bcdf-909f0e4b0f55 | -4.07554 | -54.29986 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b3a527e-59f8-355a-beac-dfb7c91a7889 | -5.9258 | -48.04813 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afe31673-083c-3855-b7ad-0b2313779736 | -5.09309 | -45.84145 | 2024-12-12 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1fc96f0-fac4-3368-809a-5a93d32e5060 | -10.29214 | -53.69899 | 2024-12-12 05:01:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b0c9bd8-cae0-3358-ad3e-451921607b20 | -9.19546 | -49.47853 | 2024-12-12 05:01:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0dd2dbe-2d72-316d-b0b2-31595706b71a | -10.53415 | -44.68453 | 2024-12-12 05:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af9cf08c-6504-38b9-9131-53e8d2cc8fdf | -9.20252 | -49.46066 | 2024-12-12 05:01:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 762d4066-ef53-3c2b-85d1-6e4438a9b1e1 | -5.30241 | -43.28694 | 2024-12-12 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 725b67aa-0646-3b13-a9b8-6d1f2c0456fd | -4.83115 | -44.2191 | 2024-12-12 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 183d865d-b746-35ca-9309-aa60a41d5627 | -10.2925 | -53.70029 | 2024-12-12 05:01:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 130ad905-1b3f-304e-a4e4-2dc181a610f9 | -4.41159 | -48.73928 | 2024-12-12 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfce9bc9-0218-3f64-8877-02562cfb04ec | -9.31261 | -58.35078 | 2024-12-12 05:01:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 507967ad-764f-3686-acdd-d51e251e7ea4 | -11.47872 | -48.2169 | 2024-12-12 05:01:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b913f416-a56f-3bda-adab-595bf461a475 | -10.51201 | -53.58524 | 2024-12-12 05:01:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c6a64a-3fb3-3237-a448-4a8e666a73bb | -3.70915 | -53.75307 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3aa9b36-07e7-30b7-af79-2f19997c83fe | -9.37931 | -57.55315 | 2024-12-12 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d45af43-b4a5-365b-acd1-5ca306a1ef00 | -9.63659 | -56.86044 | 2024-12-12 05:01:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d52f73-e6cc-3257-bc5a-be1aab5d660b | -10.85341 | -55.16922 | 2024-12-12 05:01:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3ec2cac-5635-31c7-ad0b-cf18ffac6172 | -9.33912 | -47.83885 | 2024-12-12 05:01:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cb157aa-e1aa-3fc9-9935-0e5777dd3a42 | -10.59245 | -44.97906 | 2024-12-12 05:01:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5c7278b-f1e6-3731-be00-6b9e4f0c2a25 | -3.59451 | -53.74692 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8b2d678-7cdc-3899-977b-d3e3595ed8a4 | -5.9193 | -48.05627 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c5c456af-994e-391f-b6ae-8e39eba94189 | -10.74959 | -55.43089 | 2024-12-12 05:01:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6996bc7-53d6-3065-bc81-2a7b2006ec66 | -6.05442 | -44.05241 | 2024-12-12 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48528d58-209f-3768-aa96-5da297b6f7e5 | -8.33457 | -55.09644 | 2024-12-12 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a923f3e0-8b97-3a53-8b43-29af60e4af7a | -4.80336 | -50.82767 | 2024-12-12 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5bacdc1-74c0-3cde-9662-6092c28184aa | -4.10198 | -54.67266 | 2024-12-12 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad6f4e2c-97a3-3e53-b82e-f9e1f03203a8 | -5.92809 | -48.06262 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d94051c1-3b30-3bb1-8de4-b934149988c4 | -7.46847 | -44.74048 | 2024-12-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c84347b2-c435-302b-bc47-94f2761167c5 | -8.30847 | -55.11046 | 2024-12-12 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e6ffc5a-5117-3468-b375-7bb9fbbb7a17 | -4.37287 | -48.75583 | 2024-12-12 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c047b68-4a3d-3ab0-ac8d-816a58da50c2 | -4.60333 | -48.50021 | 2024-12-12 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2cdf8a1-5bd3-338e-ae5e-9d0fa5329f7a | -11.49123 | -48.19983 | 2024-12-12 05:01:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aad3199-1490-3f3e-94cb-11e268e4e954 | -6.05648 | -44.05083 | 2024-12-12 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| beadd0d9-00f3-3ef1-a66b-c62437ccc78e | -9.47415 | -61.86597 | 2024-12-12 05:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac5f993d-8622-31b0-9936-9da5f250b1ab | -4.3773 | -48.75647 | 2024-12-12 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed6abaf3-2d1e-32bd-8580-6be6e0b1c873 | -10.54433 | -44.68323 | 2024-12-12 05:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14cbd790-9478-3599-a05a-665b14082ca7 | -10.5437 | -44.68827 | 2024-12-12 05:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbb46446-9539-368f-a518-538d40211bad | -3.76172 | -53.84827 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7138052-ee20-3749-a6fe-bbdeca0532a5 | -5.91957 | -48.05799 | 2024-12-12 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d23949f2-8f5a-3b89-90f1-0bccacca9bcf | -11.4886 | -48.19878 | 2024-12-12 05:01:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58062dd9-2ed8-33e1-8e55-cf0d2369191f | -3.59786 | -53.74744 | 2024-12-12 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 806a9456-5151-34a2-a94f-d1c159f6fc70 | -9.32514 | -50.63202 | 2024-12-12 05:01:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bbc50a4-9109-3094-ab8b-03cdec77e04a | -7.42917 | -44.74997 | 2024-12-12 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4366f68a-8ba4-3a65-9bf8-60b1ec9cdc60 | -8.69632 | -50.19693 | 2024-12-12 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 410e116b-edbb-3757-9dec-3fa216763650 | -8.6225 | -50.02073 | 2024-12-12 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c12e6fb5-3ebf-3015-84e9-0c3a4c45e209 | -8.64339 | -46.05416 | 2024-12-12 05:01:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 428afeaf-2b78-3847-8055-31b8942bbd22 | -3.47355 | -53.46107 | 2024-12-12 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
