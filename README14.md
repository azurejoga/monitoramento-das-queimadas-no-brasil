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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68df461a-2bba-3b31-bae4-f5dee10b8959 | -7.70235 | -63.3327 | 2026-08-31 01:24:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| fb1fe872-4bd5-3ab5-8124-32b2d6e67f00 | -9.83239 | -64.97562 | 2026-08-31 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5494b18d-a0b9-3621-87a1-cbf8da784a88 | -8.60512 | -71.5471 | 2026-08-31 01:24:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 77b62655-d46a-3e7b-a4d0-c5785598b460 | -8.80857 | -62.50346 | 2026-08-31 01:24:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 594abb7c-86a3-32e5-ae0c-d181a9c8162d | -8.00953 | -70.06666 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 485f3ecb-5564-3b63-8fa3-aec9ff9ea4ee | -10.17633 | -69.06978 | 2026-08-31 01:24:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a1a678b6-1a9c-3e39-878d-af0fc7197686 | -8.94327 | -62.37188 | 2026-08-31 01:24:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| d51a5ccc-4f26-368d-bab1-78cf29baafd8 | -8.95709 | -62.36961 | 2026-08-31 01:24:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9b437455-257b-3f1a-bc2d-fd2c8f17694c | -9.93764 | -60.52657 | 2026-08-31 01:24:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| abcaf797-dc03-3651-878c-239e4ed7f98a | -8.67822 | -66.51969 | 2026-08-31 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e7051d3e-22f4-3296-8f53-9cc87ccebc4d | -8.96085 | -62.39333 | 2026-08-31 01:24:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1de7721f-90f9-3a00-93fc-5896c90ad32c | -8.86735 | -66.89672 | 2026-08-31 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| efec1804-1fbc-38ec-9410-09b3c0df24ac | -8.52102 | -67.18455 | 2026-08-31 01:24:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d97afbc7-5dbc-3df0-bfaa-640608bb60f1 | -10.91029 | -61.67652 | 2026-08-31 01:24:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a87fc3d4-33a0-32c5-9a9d-7d32be13d5a6 | -9.72125 | -64.99911 | 2026-08-31 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 72ce30ab-b549-3698-b42b-aa650f2fe569 | -9.48438 | -66.63502 | 2026-08-31 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dcaab467-7495-3d17-a02d-3fc8ef83d403 | -7.33409 | -60.60759 | 2026-08-31 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| c083df79-03e7-3326-b7e0-c400d384e37a | -7.30214 | -60.57062 | 2026-08-31 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 96803cc7-3443-3d9d-b2e0-6c995c61278c | -8.58141 | -66.96999 | 2026-08-31 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f5c882d6-014c-3963-9af7-2a6291881eff | -7.68926 | -63.33482 | 2026-08-31 01:24:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| c5500254-bfcc-3905-b9d7-f35ce18cc8ed | -7.44927 | -60.75866 | 2026-08-31 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 33abe499-bd72-36c9-a163-909c3fffb41f | -9.84654 | -64.98167 | 2026-08-31 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a41e09fc-558f-379e-9581-1bde4231ef8e | -9.05958 | -65.42671 | 2026-08-31 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bb8a414b-fced-399e-b46e-76758f8a24df | -11.49825 | -60.59586 | 2026-08-31 01:24:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 40a85230-0452-3ed1-9d51-ec0b06d4a5a7 | -9.8488 | -64.99609 | 2026-08-31 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 95c20bea-446b-3b1c-8051-1ccfb16b269b | -8.96659 | -62.3866 | 2026-08-31 01:24:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0a495bca-9613-3fd0-aae9-9fdbe42dba6d | -11.49306 | -60.56543 | 2026-08-31 01:24:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| fc3a5332-c13f-327b-ba20-513a0045f23b | -7.32423 | -60.60253 | 2026-08-31 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 56e26660-a267-3b6c-8e0a-4e39d7901c9a | -8.72017 | -70.54784 | 2026-08-31 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 33ec7d38-baac-3509-9d53-58bb9d3960b0 | -7.58752 | -61.35629 | 2026-08-31 01:24:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| e9aee81f-7940-379e-93a1-c3379cf41392 | -3.62611 | -60.56106 | 2026-08-31 01:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e57fe9e0-e010-3dff-b54e-8937e78cfa3a | -7.44553 | -73.07076 | 2026-08-31 01:26:00 | TERRA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ffb92f5f-fa0d-3d62-aeec-f72f18c6339d | -3.62699 | -60.55366 | 2026-08-31 01:26:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0ee6a085-4324-328a-b756-9837e7571ba1 | -4.15432 | -60.69285 | 2026-08-31 01:26:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 0623a350-b326-361f-a013-e945159bf38b | -11.3615 | -45.1955 | 2026-08-31 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 303.5 |
| 89e2e717-e271-3882-ab7a-85324c6d61a0 | -6.6036 | -58.5972 | 2026-08-31 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| dfd3c39a-a002-3e9e-87f8-045e0cb21757 | -5.2548 | -55.8907 | 2026-08-31 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 1364a563-5387-3323-81c5-4d302cf1fa19 | -11.3611 | -45.2185 | 2026-08-31 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 288.1 |
| c61d5356-4bd9-3d12-b123-82516b215395 | -6.1295 | -57.6637 | 2026-08-31 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ffc7fddf-204d-391c-a499-8b8cc8c50f52 | -5.2731 | -55.9098 | 2026-08-31 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9004d1a6-51be-3723-91e3-49348f7c258e | -6.1294 | -57.6833 | 2026-08-31 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b700e2e2-5fc1-30ca-bfd4-6ae79a2a540b | -11.6841 | -47.5932 | 2026-08-31 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 88dd8ba2-ec9b-34be-9d83-02f713175896 | -15.4231 | -52.7049 | 2026-08-31 01:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 09a2c6fc-44fb-3540-b940-bfb9d0db7dfe | -5.2547 | -55.9105 | 2026-08-31 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 269.3 |
| e4e68c31-896f-3e10-a162-9a81d3b6a185 | -19.154 | -57.3978 | 2026-08-31 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| c72dc1f3-d081-3099-a19a-25aeb55562f6 | -5.2362 | -55.9112 | 2026-08-31 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 54fcd807-7837-33a0-8a34-40ab8ae551db | -11.3806 | -45.1928 | 2026-08-31 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| c1301418-19b7-3fa7-a632-9c6b7e835b09 | -19.1536 | -57.4186 | 2026-08-31 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.2 |
| c3130d46-2d5f-38b3-a346-2d438e24af8e | -11.3619 | -45.1724 | 2026-08-31 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 12e0e2c4-c8e5-3fdd-a2f5-f5f6d5012755 | -7.3302 | -60.589 | 2026-08-31 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f2971098-d644-3b9b-9247-e1a811d3ea41 | -18.2904 | -52.6818 | 2026-08-31 01:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 38825b94-63f1-322d-a96d-6ac9bc55e9d9 | -17.513 | -40.2464 | 2026-08-31 01:30:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.2 |
| 356c5487-df36-3414-b59b-fec685fc7383 | -5.2363 | -55.8914 | 2026-08-31 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 6352013a-d148-3db4-8b2f-54df1b2fca84 | -11.3802 | -45.2158 | 2026-08-31 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| e156cd7c-ad73-3b64-b18d-381d104a609d | -11.6837 | -47.6154 | 2026-08-31 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2fe7f2bb-9b8c-3b08-9f7a-063ace665c2f | -9.4342 | -45.6704 | 2026-08-31 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 817272c8-4451-3b9f-ab49-2521988998cc | -7.3301 | -60.6081 | 2026-08-31 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 20205b51-dd52-3781-9988-2dc327018e8b | -1.6042 | -54.415 | 2026-08-31 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 56984555-14f6-3f1a-bb69-29535c7e29b2 | -9.8018 | -46.4405 | 2026-08-31 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0914aaa0-ad8f-3938-81b9-71e9a74c7618 | -11.3615 | -45.1955 | 2026-08-31 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 363.7 |
| ef91ebc7-66c3-3181-959b-0916d6749415 | -20.3703 | -47.4481 | 2026-08-31 01:40:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 4aca750a-1e69-3fde-87e6-059d21e53f5d | -11.3619 | -45.1724 | 2026-08-31 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 587ced8d-8453-338b-a1e6-f2c0b24cc39d | -7.3302 | -60.589 | 2026-08-31 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fbd1c90f-fc1c-389d-9bb7-5aaa3d437aba | -5.2546 | -55.9303 | 2026-08-31 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a551001c-6273-3872-9c73-0d32cb522736 | -11.3806 | -45.1928 | 2026-08-31 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 295.5 |
| 19739f61-5264-34c5-9e71-cef727a3ffc7 | -6.9176 | -55.7166 | 2026-08-31 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 4ca0a5d7-54f7-31f3-b695-c48e6b08d55c | -11.3802 | -45.2158 | 2026-08-31 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 8783e702-fe98-3aae-8f2a-04a8a108af95 | -5.2548 | -55.8907 | 2026-08-31 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 178.7 |
| b19ccdae-0f53-3ee0-a69e-dc8f00207e96 | -5.2547 | -55.9105 | 2026-08-31 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 312.7 |
| b7f484b9-89e4-3c01-87d7-da0b9b7232c8 | -11.3611 | -45.2185 | 2026-08-31 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 79da182a-b145-3f8f-ae1b-df367331da8d | -5.2362 | -55.9112 | 2026-08-31 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 8d314422-f500-3053-8026-cf7fffa3fab9 | -11.5017 | -58.5145 | 2026-08-31 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3f09261a-4721-3d1f-b88c-7e7b36ee5dd5 | -10.8212 | -50.6732 | 2026-08-31 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b53e05b5-1c48-3cdd-8bf9-8108e6e266dc | -18.2904 | -52.6818 | 2026-08-31 01:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 993f960f-98ea-3533-b428-933d6b0d1b5d | -5.2363 | -55.8914 | 2026-08-31 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 10d85d3a-fcf4-3785-9346-87800f81ed51 | -10.8022 | -50.6752 | 2026-08-31 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ed07a372-9844-31ad-a332-c588f05c6fa7 | -11.4828 | -58.5159 | 2026-08-31 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5b04db30-2ffd-3d8a-a39d-18cf3bce47e8 | -6.6036 | -58.5972 | 2026-08-31 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 9f4abd13-69f8-34c7-ba9b-38719d16e7d2 | -7.3302 | -60.589 | 2026-08-31 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 44c66569-ae19-3843-aaf9-d29d028f5cd7 | -5.2362 | -55.9112 | 2026-08-31 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 9bcdf017-7125-3d9f-8a95-df91b4fdd1a1 | -9.8015 | -46.4629 | 2026-08-31 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 28280b86-01a9-3d09-b4aa-63240aea49b1 | -11.3611 | -45.2185 | 2026-08-31 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 272.9 |
| 4fadb319-941d-3c3c-9fd8-7ee8625b9f44 | -5.2547 | -55.9105 | 2026-08-31 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 310.8 |
| ab8eaa9b-ff0e-3a29-af96-34f8a026af6d | -9.8018 | -46.4405 | 2026-08-31 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 3faeedf7-eea8-3dbc-b39a-39e2402ecff5 | -11.3806 | -45.1928 | 2026-08-31 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 254.9 |
| 4e54a91b-4a9f-3fa9-b8c3-9f3ad546ac13 | -10.8022 | -50.6752 | 2026-08-31 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3c268bd5-58b6-3c27-a5f1-f74f55248d33 | -1.6042 | -54.415 | 2026-08-31 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| eaa973c2-ca2f-387b-8915-a633426a3f2d | -5.2548 | -55.8907 | 2026-08-31 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| d5daee33-d5f4-3f6c-b98a-be78f671f6b1 | -6.9367 | -55.636 | 2026-08-31 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 2766a32d-fac8-3141-8803-6cc055a788af | -5.2363 | -55.8914 | 2026-08-31 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 57da376b-60b3-3511-975d-d6909ec565fb | -11.3615 | -45.1955 | 2026-08-31 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 01f471e0-ec68-329a-901e-635b356ee59c | -17.5332 | -40.2409 | 2026-08-31 01:50:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 65.3 |
| db6dc6ec-3a4e-326f-8d58-9442712cc908 | -10.8436 | -45.3586 | 2026-08-31 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d4ccba1b-187b-3ad3-97f5-749fb284aa98 | -10.8025 | -50.6539 | 2026-08-31 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| b3adfbca-978f-32f7-a39c-f5e6c88334c7 | -6.7702 | -55.6246 | 2026-08-31 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 3a6ccc70-f2ab-3a7c-8d63-4bf0200295ee | -13.9474 | -54.4179 | 2026-08-31 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 788172de-76f3-3350-a8d0-7f0230cfa57d | -15.4231 | -52.7049 | 2026-08-31 01:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 559e2af8-5d3b-3526-8dcc-bcadde68b1dc | -10.8212 | -50.6732 | 2026-08-31 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 4f971c30-2c67-33e4-9e8b-fb02a11e8601 | -11.5017 | -58.5145 | 2026-08-31 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 78d4bac0-0cd0-3017-9f8f-517138d29b05 | -6.622 | -58.5965 | 2026-08-31 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |


[Clique aqui para ver as próximas entradas](README15.md)
