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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96944be3-d390-34ab-80fd-66cc5d3f7167 | -6.178 | -44.0688 | 2025-08-28 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d6881cf9-fbd2-3a06-ae3e-0c41fefb31c6 | -13.0859 | -46.358 | 2025-08-28 13:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9a716035-d282-3d72-a916-776f4aa064a5 | -6.8769 | -43.6385 | 2025-08-28 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1e8a7057-feb2-30c0-a4b0-b7db0bb8a371 | -7.3357 | -59.6484 | 2025-08-28 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 17121606-9689-3577-a316-8ce808742cad | -13.4212 | -46.9637 | 2025-08-28 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 812c9da8-caba-332f-8e20-4edcf6efb178 | -13.0863 | -46.3352 | 2025-08-28 13:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b1c9f597-4648-3476-9708-e3edd978a1fe | -12.3993 | -45.0183 | 2025-08-28 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5dbbc83f-8a5a-3d38-9674-228e11a3182a | -12.8224 | -48.1489 | 2025-08-28 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| a8254b71-2d14-375d-b90c-77177bef4ac6 | -13.5193 | -46.8805 | 2025-08-28 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d7975f7a-236d-3394-8184-37cbb95684ee | -7.233 | -45.4413 | 2025-08-28 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 700c9a83-159e-391a-9f44-a1fbd3e29099 | -12.8032 | -48.1516 | 2025-08-28 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 3669d2cc-a122-339c-b69d-9bea5505f500 | -6.1595 | -44.0472 | 2025-08-28 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| a671b7fc-463e-3aae-922e-ad1be77cf4a2 | -9.2632 | -65.8959 | 2025-08-28 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| caa0a69a-e529-3ac0-9551-a512e7f60f73 | -13.5576 | -46.8972 | 2025-08-28 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 4f674868-cc4d-3b1b-bcba-7759a38ac7bb | -7.1917 | -44.0732 | 2025-08-28 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 31f03407-c578-3a76-9b49-cba9598d403e | -12.6878 | -48.1677 | 2025-08-28 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1f4ada2c-b694-35df-8b6a-bc782b0c15fc | -13.4208 | -46.9864 | 2025-08-28 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 82014610-f680-3cf7-8722-91841e933a1c | -10.8421 | -60.8009 | 2025-08-28 13:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| adc0dcca-ec0a-3f4a-b50f-239aa203a136 | -6.4355 | -44.5764 | 2025-08-28 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 9bc803c9-38ec-3214-8ec4-6fed525e46e9 | -11.3521 | -43.5423 | 2025-08-28 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 251.8 |
| 2004cb72-8442-36f8-b8e0-48448429f00f | -11.5707 | -46.3751 | 2025-08-28 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 53941c78-9732-3cef-a855-467cfaffffe5 | -11.1523 | -54.3104 | 2025-08-28 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 8449ddc8-49c1-3d3e-ab44-3b3eac03f1cc | -6.8583 | -43.6169 | 2025-08-28 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d0b889bf-ba7f-3682-aeba-5ec8310e3c31 | -11.3526 | -43.5187 | 2025-08-28 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e9454b29-043b-321e-9128-7fdb65835136 | -10.8419 | -60.8202 | 2025-08-28 13:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 9018f3e6-6df7-3d8a-bc97-c7a65dbf9816 | -6.1593 | -44.0703 | 2025-08-28 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 66bcaec7-00b6-3f7b-a4af-a70a23a76b9b | -7.3196 | -46.109 | 2025-08-28 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 6743f766-941f-314b-abf3-6230d992dd98 | -6.2755 | -43.6907 | 2025-08-28 13:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 1b368416-7c68-3168-a099-f46b98eb3d74 | -12.8028 | -48.1739 | 2025-08-28 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0b8cd228-2e1f-3fc5-a634-478e27f4423f | -11.3329 | -43.5452 | 2025-08-28 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 62952e2a-b472-3c0d-a207-f99483cb007b | -6.4543 | -44.5749 | 2025-08-28 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 08656c9a-6148-36d2-bac1-71ab05e6c55f | -11.2378 | -55.0569 | 2025-08-28 13:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| c81ed299-6372-37b4-8dbb-d1feb1126744 | -6.8772 | -43.6152 | 2025-08-28 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 15b18619-b8ab-350f-a426-f0565da20f0a | -11.3521 | -43.5423 | 2025-08-28 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 355.4 |
| ca8d1766-9b69-3a1b-b9b8-5c4d2e125a7a | -10.308 | -46.8068 | 2025-08-28 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a267fb91-81aa-3911-9941-4763eb3b453e | -13.5378 | -46.9229 | 2025-08-28 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 14d88534-6359-3efd-9e78-c1bc5e8f721b | -6.1595 | -44.0472 | 2025-08-28 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 184.6 |
| b6ea4328-3cca-3515-8d39-9f8892802627 | -11.3526 | -43.5187 | 2025-08-28 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| f7788149-c0f5-32d3-8c3f-52aacd7358f0 | -6.4543 | -44.5749 | 2025-08-28 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 9ea0beb6-ee60-3985-ae59-e353a3f67cf4 | -6.8583 | -43.6169 | 2025-08-28 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 965c3648-586e-3a7e-be51-a32c3d0c45e3 | -7.3357 | -59.6484 | 2025-08-28 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 95b1bac2-2ebe-3157-821e-cc9cb2c4b5e8 | -10.8049 | -60.7644 | 2025-08-28 13:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9f23db6c-3c71-3eac-a255-34bc4bf4a6df | -6.1593 | -44.0703 | 2025-08-28 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 05b3e576-0800-3e53-9485-9feb3235e45d | -13.5184 | -46.9259 | 2025-08-28 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| dd835709-ad7f-3818-9d22-763fa5160610 | -9.406 | -60.5711 | 2025-08-28 13:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3ee04fb0-3237-30e4-af31-193231579f68 | -6.4355 | -44.5764 | 2025-08-28 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4ffb47b8-da24-3cc8-b10d-da844aaa6b00 | -13.0863 | -46.3352 | 2025-08-28 13:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b3a7112b-e4a0-3ed2-a02c-e7d27cdffa35 | -10.8421 | -60.8009 | 2025-08-28 13:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 23d51b4a-e1c4-3024-9964-45e78cef42c9 | -6.8772 | -43.6152 | 2025-08-28 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 173.6 |
| aaa3f89e-e686-37b3-aabe-17b814c1a863 | -6.3881 | -45.6018 | 2025-08-28 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 547dd670-84a1-3584-bf50-fc5cd497faf5 | -6.2755 | -43.6907 | 2025-08-28 13:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ecac0616-6687-3ca7-af91-cbf0b58cd70b | -6.1783 | -44.0457 | 2025-08-28 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 32cb9161-aa5d-3539-8478-a66a4af1a049 | -12.8224 | -48.1489 | 2025-08-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| a9bdd966-1968-3e7c-a5a9-02769f23e182 | -7.6414 | -42.6718 | 2025-08-28 13:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| c7fb6eb2-355c-3fd0-9c8a-c07f90c0444b | -11.2378 | -55.0569 | 2025-08-28 13:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| e4c91f1d-cc82-3122-ae3c-38ac8081bc06 | -13.5193 | -46.8805 | 2025-08-28 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 4221d3ca-6229-383f-9c2c-edbbea957cf8 | -11.5707 | -46.3751 | 2025-08-28 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 22ddbcad-df9f-33e9-9f30-a11280c05260 | -12.8028 | -48.1739 | 2025-08-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 64ffa285-e637-3097-9515-53e2e41ca283 | -11.1523 | -54.3104 | 2025-08-28 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 6eb32c36-b48f-38be-8fd4-6a6ab9bff8ce | -10.8419 | -60.8202 | 2025-08-28 13:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 30c999c2-9e65-3304-a964-40e08b8413d5 | -9.4246 | -60.5701 | 2025-08-28 13:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f05a274b-c1b1-31a4-a948-6f317fb6553a | -9.2632 | -65.8959 | 2025-08-28 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 929aa882-ab92-3839-a318-dd0fc89ea453 | -13.4208 | -46.9864 | 2025-08-28 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d0d9fc84-a1cd-314c-b6be-2ca131cf5bf3 | -12.6878 | -48.1677 | 2025-08-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 18cec53b-b7e0-30c2-a8e2-7caf21c96456 | -9.6816 | -48.3139 | 2025-08-28 13:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5b8c49f0-00af-3a0b-8251-ce944e6427c9 | -13.0859 | -46.358 | 2025-08-28 13:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ee898b87-58ef-3396-870f-c6869654a31b | -11.3329 | -43.5452 | 2025-08-28 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 35b1c0bd-ede5-3174-a828-4f8fff235275 | -6.8769 | -43.6385 | 2025-08-28 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2969e419-3c99-3af5-b987-2428ec293190 | -7.3196 | -46.109 | 2025-08-28 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 9f5813b2-c149-3b35-92a6-3509ca5b1d81 | -14.3696 | -52.0813 | 2025-08-28 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 66503c34-af11-338c-a725-0e446e27303a | -6.178 | -44.0688 | 2025-08-28 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 3b348e29-497b-30a9-8950-6da1ab134512 | -12.8032 | -48.1516 | 2025-08-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f4773034-1c94-37d7-a3f5-f3195e6da6a1 | -12.3993 | -45.0183 | 2025-08-28 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 4c936710-3291-3a10-a249-ec52bda22e4f | -16.3606 | -43.7858 | 2025-08-28 13:20:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 119.3 |
| a7718e07-5f54-3c4c-9b67-b0ddd45232f7 | -6.4355 | -44.5764 | 2025-08-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| f102ad9d-c71b-3d51-ac2e-fd8677373f5b | -12.8224 | -48.1489 | 2025-08-28 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 5df0c5d2-d1c6-3ba4-b022-ac3b229f8ccf | -9.6572 | -65.022 | 2025-08-28 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a75710ae-93d2-3deb-8bff-23e376ba6690 | -6.1372 | -44.417 | 2025-08-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 7735fd83-6e1c-3a75-afd1-520bf2072b7e | -12.6878 | -48.1677 | 2025-08-28 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 43a17ae6-68a5-3b4a-a20e-06ed02077c2d | -8.8842 | -60.7507 | 2025-08-28 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 345f2603-51ea-3ed5-afb7-14fba04472a8 | -14.3696 | -52.0813 | 2025-08-28 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5ac5629b-9656-3a2b-90b0-1b370f734671 | -7.3357 | -59.6484 | 2025-08-28 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 53b4f2b6-115c-3e50-a42a-2c58eff1a4e8 | -13.5193 | -46.8805 | 2025-08-28 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ff0c1932-6f7e-35a0-b56a-8ceb522dc7bf | -9.2632 | -65.8959 | 2025-08-28 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 78cb61c5-3762-393d-8a7c-923048421c24 | -6.4357 | -44.5535 | 2025-08-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5082cae8-b6da-3fba-95e5-a04feb5a76f0 | -9.1153 | -65.8073 | 2025-08-28 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 293.7 |
| ade4716b-0f61-3739-9f45-b2f7cb544f94 | -12.8228 | -48.1267 | 2025-08-28 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 85a4c121-9636-35ae-9e0e-91f70d4bf4df | -6.8769 | -43.6385 | 2025-08-28 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 36c9e0b8-e39c-33bd-baa9-3d428c6f70d0 | -12.8805 | -48.1186 | 2025-08-28 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2e2c1c68-ca03-3ce9-92f8-75ebd2e64b20 | -14.3339 | -51.9157 | 2025-08-28 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 49146e82-ba84-3dac-b14e-62b101e67149 | -9.6816 | -48.3139 | 2025-08-28 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 138.5 |
| a8a9ed4e-a378-3e27-9916-aaae0f6dbb19 | -7.6414 | -42.6718 | 2025-08-28 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| baae2501-e28f-34a7-abc1-40e44e11a866 | -6.2755 | -43.6907 | 2025-08-28 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 5727da5d-e36f-3bab-845a-18739488c712 | -6.9486 | -45.7366 | 2025-08-28 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9b9d99e3-edb1-34b2-8135-eed108a94779 | -6.1564 | -44.3696 | 2025-08-28 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b9f5c6d6-f72d-39a7-a7a8-7fa9ba58d640 | -9.134 | -65.7694 | 2025-08-28 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 219.0 |
| 5465101a-695e-3ad1-bcb9-5d82172d0608 | -14.3113 | -53.2711 | 2025-08-28 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a7354531-78de-36bc-ad3b-49c190d7f980 | -10.8419 | -60.8202 | 2025-08-28 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 5c1b2ec9-bea6-38f9-a478-4245be0326bf | -6.178 | -44.0688 | 2025-08-28 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 0140c2bb-dde3-3912-8c16-3d125c2aa8fb | -11.5703 | -46.3978 | 2025-08-28 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |


[Clique aqui para ver as próximas entradas](README96.md)
