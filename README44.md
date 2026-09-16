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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5801648f-6b44-39e0-b1e4-8a11dcc4cec2 | -11.88993 | -43.82816 | 2026-09-16 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 40ee563f-52cc-3dcc-814e-02c6a5d4bb4c | -9.22119 | -60.29518 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e5d6c48-5980-326b-a68f-e4dd1a1957bb | -15.03615 | -48.56103 | 2026-09-16 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25b6604f-ae72-3d51-8137-6514356b05ca | -8.64394 | -66.57366 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 771ea171-f9df-3f4b-a497-682dd8664aff | -13.3015 | -51.75319 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab0aa04e-7fb0-32d1-96d9-08fda3ca1b19 | -11.28653 | -47.67972 | 2026-09-16 04:59:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2874531-ae6b-33c0-887a-d522de13fb44 | -11.8119 | -60.46277 | 2026-09-16 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 30c297a5-7963-3c4e-b482-65e3bada7340 | -11.25835 | -46.57242 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6c3261f-ae04-37d7-9ad1-9b908a18234e | -10.10344 | -45.61128 | 2026-09-16 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 523dfcf6-1d10-3765-92b6-43344cf63d5f | -11.2715 | -54.1323 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79730d43-19da-3f56-8f98-9bad252b146e | -11.8905 | -43.82312 | 2026-09-16 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1352ff62-d4d7-3107-83fe-7f75700e8750 | -9.79991 | -46.5048 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 2f3dd87b-43ed-3b5e-866e-a163dda5c9a9 | -10.80432 | -46.181 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11e54aef-f8bf-32fd-9e95-a4d796172489 | -14.85969 | -49.97062 | 2026-09-16 04:59:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 58f5af3b-a05a-3a98-a090-aa6f9f1730e9 | -9.14733 | -51.56823 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5413bace-8fe7-392f-996c-588505fbbb8b | -9.78141 | -46.48645 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddc949ec-db4b-3263-9b86-0ba54e0081a2 | -9.25277 | -60.28164 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 901c0f5d-9337-302a-be2c-5252142f66de | -10.4807 | -50.95829 | 2026-09-16 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54745750-94a6-3c9c-a942-cb88ac7fd3b4 | -11.28167 | -47.6792 | 2026-09-16 04:59:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4200236-bcb2-383d-8d20-ebb46acd1d36 | -10.84724 | -46.18427 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85ae41cb-624e-3735-9846-684997790b22 | -11.19458 | -55.03473 | 2026-09-16 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61748485-b560-3e3a-a106-3b20878e6ca5 | -12.22704 | -47.13052 | 2026-09-16 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f37bd8b9-32c7-3237-badb-bc4a207b8401 | -11.97847 | -49.71114 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e172141c-a467-349f-b001-ec6d1d34e24b | -10.67864 | -54.14811 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83746ba7-e3d8-3404-bf2d-b55eae0568e4 | -7.76384 | -61.35308 | 2026-09-16 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c83b08e-ff4d-3a91-890a-145f320847b6 | -9.80336 | -46.49815 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 85201b79-749e-3e88-a9d9-bc40ddfee3b8 | -11.54761 | -46.8658 | 2026-09-16 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 05fbcff5-7a10-3983-94e3-0f4f7e0dca65 | -9.38951 | -60.31332 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 653a6818-579b-3418-a534-019a29c5c0b5 | -8.54484 | -54.69255 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a756747-ef85-3ecf-9bd7-10a1cf57b4e6 | -10.77441 | -46.21568 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0821543e-4bd1-36f4-b040-52832dce123a | -14.8583 | -48.12655 | 2026-09-16 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e24303b1-9105-3744-8a0a-a34012ca2b1d | -11.79157 | -46.58532 | 2026-09-16 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c7e894f-0293-39ca-b7bf-e760ab9534b7 | -9.22181 | -60.29147 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 574f87c0-83d3-3b8e-bded-b97047926421 | -11.98445 | -52.46759 | 2026-09-16 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58a794be-87d0-3ecb-9721-7257874bb96d | -11.41141 | -51.42319 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ce761a18-ec2d-33ee-87b5-69eb9c67aea0 | -10.10301 | -45.6146 | 2026-09-16 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8e939db9-1343-3ba4-848a-5fa94d1b7460 | -9.10018 | -65.93253 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d818a39-9eff-3a18-a4c5-440897927b71 | -12.11288 | -57.19091 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f49fc3de-5c36-3e57-a427-22bb83bd3bac | -12.64645 | -54.70093 | 2026-09-16 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a42d8e72-d3de-31ff-bb38-f3f96a5942c1 | -9.83317 | -57.70273 | 2026-09-16 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34395763-54dc-33d7-aeea-6c65787abe30 | -14.00144 | -53.86608 | 2026-09-16 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd9692ea-b329-36a4-9711-60bb3e8c7666 | -10.82605 | -46.18044 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b23bd048-f135-3f2b-9ca5-041969425294 | -9.16008 | -49.9907 | 2026-09-16 04:59:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99e28788-19b7-3c51-8ab4-7f5997bbe63a | -8.36952 | -54.72477 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb1fce4b-97a5-31f4-bc01-0946bcd5147b | -9.23822 | -49.58275 | 2026-09-16 04:59:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b03f735c-915d-3a09-b68d-83dcb255b9ee | -11.44506 | -49.76754 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 591e7fe7-2a14-3ddf-b713-e7f3ee06e999 | -9.34128 | -50.15292 | 2026-09-16 04:59:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6144a28a-c05b-3521-81be-b6a89e533eb0 | -9.06461 | -65.9261 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9f108f5-35ac-3a6c-a937-87856ef2c161 | -12.77064 | -51.2307 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5713eb43-914c-3a08-9eb7-c73b2d4c831a | -12.12181 | -57.19994 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e03f438-40f3-3043-b5eb-750a55eb77df | -12.32382 | -47.95784 | 2026-09-16 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ea69b9ea-64a4-3fa7-b858-e70bd6738066 | -9.7264 | -64.90703 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 90d8a989-0200-31fa-943f-1ee9526dc041 | -10.76784 | -46.22484 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c0710fc-d4bd-36dc-8b0d-41f701f5e1df | -9.07221 | -61.01554 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c69aa672-8d89-3238-8abf-4bd431174444 | -9.37762 | -58.00115 | 2026-09-16 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84e48a83-bc33-30aa-a3a2-707a3eed51c2 | -12.13547 | -57.1796 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa4aaa43-c33b-338f-b577-d4e29fc5e719 | -13.39317 | -57.03775 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07e19228-cc4c-3969-8b0b-3d0261902c5e | -11.98085 | -52.46704 | 2026-09-16 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4359e892-ebbd-39bf-8c47-763e49da7cce | -10.69399 | -54.17651 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df387f27-7021-37f7-80a2-047d9db1ff60 | -10.89113 | -51.49498 | 2026-09-16 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6fce81-e1e2-3cc4-a277-7a3a35d4b1aa | -11.31563 | -47.24292 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0d4589f-2225-3496-b670-95d997fb7ccf | -9.71025 | -52.01914 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2a3f724-338e-3a05-a03e-34cc084e8f3d | -9.71372 | -64.91571 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b489554-dc95-362c-b75e-ce7d447dc22c | -11.88879 | -43.83815 | 2026-09-16 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ead637a3-76e0-323a-9b33-25a443053cd3 | -7.6197 | -67.25381 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66f0248f-fb56-38c1-96b3-3d8672da437a | -8.37282 | -54.72528 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b3e87d4-1eff-3465-a531-13317e30c9f3 | -8.70853 | -62.84417 | 2026-09-16 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b87ec1-0d57-3677-a9c7-ee06eba63038 | -10.42161 | -48.65702 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3274936f-1590-3d35-a758-fb9f1203bc6e | -10.84764 | -46.18105 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c87a8872-5167-33f8-8bdc-31c15a7cc4da | -10.87336 | -50.82269 | 2026-09-16 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd258543-6b2b-37b9-899a-975b7348afc9 | -10.82562 | -46.18389 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 64f2ba79-80b0-319c-b62d-c23cb1dbc2ea | -14.40046 | -44.70637 | 2026-09-16 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8996a60d-527c-351e-8e65-c1362831e2a2 | -8.37559 | -54.72927 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34492428-fbe8-33a7-9eea-acdbc12113cd | -14.22863 | -48.51262 | 2026-09-16 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c14e3bb5-986b-35b7-9c96-3605a413939c | -10.90409 | -54.00576 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d58243b2-35b2-30df-ac01-308e9f3e1ef5 | -10.32094 | -59.14378 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6432c8f4-ee8e-397a-a6ce-31933db36ffd | -7.57389 | -63.28743 | 2026-09-16 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b28adf07-a855-3e3c-b613-5b88089ad8e5 | -9.12122 | -65.85169 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c73416f-5faa-3928-ab13-3656f2e2fee5 | -10.89907 | -54.01609 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22f71496-dce5-3320-b7d9-409a458ceefd | -9.70007 | -52.01334 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1b7d31d-cf40-34ef-9830-c5f61d1febd3 | -10.10221 | -45.62084 | 2026-09-16 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f91b6452-c254-3cb7-b9e3-c3cac96179fe | -13.76481 | -48.82621 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56bfbd28-ad48-39ac-b784-4e944febef2a | -7.76565 | -61.35418 | 2026-09-16 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcf284d7-1fa7-3afe-980a-dbd8e0c25f3f | -9.57327 | -46.59615 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02f6a287-22c2-3791-bff1-cbbae74db295 | -9.80505 | -46.50546 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| e3ab99c6-400d-39bc-9d97-df3c9f78987b | -9.80297 | -46.50132 | 2026-09-16 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| d1d6711a-2c98-37eb-bad7-5c09e1d7fa57 | -10.66019 | -58.76192 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 240e0f40-5b58-3b38-b483-cba09230c983 | -6.93119 | -63.13135 | 2026-09-16 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43e683ff-12fb-3e96-9efb-a0ab5ed98adc | -9.60302 | -55.10289 | 2026-09-16 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44c2f24a-954d-36f5-9c78-bf457ea42c61 | -12.1214 | -57.18103 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7a2fb64-7020-34be-bed1-e648a3a0bbe5 | -11.32123 | -47.23899 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c13c0e8-045a-325e-afb8-e273acc73276 | -13.55996 | -43.52621 | 2026-09-16 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d08312c-3923-3281-a954-d1f663455571 | -12.67017 | -50.83131 | 2026-09-16 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f2ae8085-c598-3be3-ad56-4b092f9ae504 | -11.20264 | -42.8347 | 2026-09-16 04:59:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5a73b635-d9d0-375e-a209-5d4c345fbbf1 | -9.70306 | -52.01809 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdab7f97-6da5-340e-8b6e-976393b77a92 | -10.46081 | -44.9435 | 2026-09-16 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26b2af04-ce17-3de0-b028-f3c0e5e64e21 | -8.70681 | -62.54069 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d98e70a-4197-394d-bf78-0875aa496199 | -9.49545 | -56.7527 | 2026-09-16 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51640c29-7cdf-38c6-b7ac-6a25d99496c2 | -13.40608 | -57.02144 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a606cb6-d239-3991-b57a-f114f8a67385 | -12.76192 | -51.26525 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README45.md)
