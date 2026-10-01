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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d7d9d86-aa29-3d4b-82c2-0b4399c37920 | -11.6395 | -43.5455 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 73b38f1b-acfd-3688-a752-5dbca7d201e3 | -11.7182 | -43.4386 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 378.8 |
| 34c62c44-578c-3893-b69c-293da617ad39 | -11.4294 | -43.507 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| efd1893e-f8b3-339d-a5f2-6f2861f048d8 | -7.0609 | -42.3274 | 2026-10-01 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 74ae858b-7fd6-3618-9e26-bf0d529ec16e | -8.6268 | -45.3054 | 2026-10-01 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 4a9d88bb-f03b-3610-95fc-1a8a1419ef32 | -9.9029 | -50.1487 | 2026-10-01 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 366210d9-d0b3-389d-b8dd-0c15cecb4e73 | -11.0481 | -50.6917 | 2026-10-01 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 2089f04c-741b-3688-853b-49d9bdb19869 | -9.806 | -44.8496 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 153.6 |
| fe0554e6-0460-3054-86ef-1b047cbfa8fd | -9.0247 | -49.6549 | 2026-10-01 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 20b332d0-a717-357d-ba65-1679aad20a48 | -10.9262 | -43.8406 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| aac62a9b-7748-3842-be01-0ba8326ba572 | -11.7187 | -43.4148 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| a9e2a909-d59d-351f-b09c-d9b3c1617ec0 | -8.3208 | -44.1679 | 2026-10-01 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 0062704a-ec08-3164-8887-a5993573f1c9 | -9.8064 | -44.8265 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 5b6ccb5b-d16f-38ac-a555-5aaa7564d54b | -7.4977 | -54.9854 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1fca789b-d746-3097-9e77-c308d71acfba | -9.8617 | -44.9347 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 33fc3614-7f41-3ef0-8bf6-436c78b55c0b | -12.1857 | -48.4345 | 2026-10-01 13:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 200.2 |
| d52de1bd-e8ce-3e70-9c60-ed848e23f51a | -9.8613 | -44.9577 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| d841cc80-e222-386a-8123-6f6daf1000f0 | -9.8807 | -44.9323 | 2026-10-01 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 230.4 |
| e64e26a1-fec8-3dbf-978f-a550a6b224f7 | -6.7002 | -55.0493 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2ef7bde5-1809-3151-8963-44be0e21fb3d | -7.7221 | -54.7913 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 7c23c4cf-4db2-3f32-9f3e-4a2bbd57d02d | -10.9337 | -50.7465 | 2026-10-01 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 57f83bd2-0bee-33e8-8ce5-01eaf1adf171 | -10.5388 | -45.3759 | 2026-10-01 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a46d3401-dde6-3420-a121-2e5effbadf18 | -12.571 | -47.1809 | 2026-10-01 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 1e042687-04a5-3eb2-8fc8-2cc190e0e7c7 | -7.3779 | -42.628 | 2026-10-01 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| bbd10c8b-2664-3dd9-8961-e3983aa97db5 | -5.9152 | -53.4762 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 001a8fae-eda7-3f85-b109-4515db20babc | -7.7407 | -54.7901 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 4939be14-0eaa-362b-a82d-90ad5243eb67 | -10.7879 | -47.7057 | 2026-10-01 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| c18f8912-6c30-338a-83b6-0fe70aa58635 | -11.2438 | -44.2626 | 2026-10-01 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 7529340d-fda1-3258-893b-469ae8a8da98 | -15.6481 | -44.7217 | 2026-10-01 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 3d09c7fc-6818-39d0-8f8c-98be45d90173 | -13.3292 | -43.8335 | 2026-10-01 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 8df259de-1dcc-3870-ba93-c1552da93933 | -8.1496 | -54.8049 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0fc25126-f29f-3237-80c2-ce4d9b60ab03 | -11.6588 | -43.5425 | 2026-10-01 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 585.9 |
| df74f9ad-7353-3487-a16a-01a18e3c08e4 | -5.8411 | -53.5002 | 2026-10-01 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 9d485c56-a840-3f98-ac47-e6571100578e | -6.9231 | -42.8616 | 2026-10-01 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 77f27ad7-911e-3804-acd8-3ccdaeae00e5 | -14.377 | -44.7534 | 2026-10-01 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 5197fbea-e121-3244-ac62-491e8fa549f1 | -9.8064 | -44.8265 | 2026-10-01 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 588.6 |
| 2e4e2f18-74fd-3ce9-9dd4-40f8268d8fdd | -10.776 | -47.2411 | 2026-10-01 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| cb0a7bcb-c499-3d5e-ac35-10e99c4a1479 | -7.0738 | -42.8472 | 2026-10-01 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 784d8215-c3f1-34fa-aff2-178a7be22e3b | -10.1878 | -49.9918 | 2026-10-01 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 76245a78-3455-376f-ab4e-05dd03691f3c | -8.2806 | -54.736 | 2026-10-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a96b7d0a-5520-3d6e-a1e1-2bac6574f8b7 | -7.0451 | -42.0666 | 2026-10-01 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 723e2305-de72-3aee-8f79-21048ce3a264 | -11.2438 | -44.2626 | 2026-10-01 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| fcdf6a36-7ad5-316b-ae9e-c9bf68b361bb | -10.9725 | -50.6785 | 2026-10-01 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 6e986a74-4d39-3431-b746-0bfcdde5336c | -11.699 | -43.4416 | 2026-10-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 0ec13147-94e8-3df0-8a07-3d1e6e8c801d | -8.3397 | -44.1658 | 2026-10-01 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 964d12e1-0cc7-3bac-a876-6927d08be7ca | -16.9909 | -45.4594 | 2026-10-01 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 870e7e28-5e6c-3df6-b90f-ce129d31ecfe | -11.2087 | -45.1939 | 2026-10-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 478b1563-6ee6-3c9e-803f-db1aa60faaff | -9.7877 | -44.8058 | 2026-10-01 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 89ca2ffa-cd3f-33b6-94f0-c04321964aec | -11.1232 | -44.6056 | 2026-10-01 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 17fdd965-f43a-3c08-9b38-32c333c7ca91 | -11.0764 | -51.3885 | 2026-10-01 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 456d4f76-4ae0-3772-9b6b-0efe61408c31 | -9.8807 | -44.9323 | 2026-10-01 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 286.6 |
| 76470c17-3027-394b-b6cd-7acad8c44cac | -11.1236 | -44.5823 | 2026-10-01 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| d16d46ca-6583-3cdc-9d4e-2bb7bc8f7d6a | -11.2278 | -45.1913 | 2026-10-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 78c57d3b-8987-3ce9-ac14-2d043eb6cdad | -10.9463 | -47.2869 | 2026-10-01 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| ef2b4e39-6c58-395d-a474-2dd48c64e7bf | -7.0612 | -42.3035 | 2026-10-01 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 3cf465c9-dcb6-30b5-a871-c2e7bb9a1732 | -11.4495 | -43.4566 | 2026-10-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 2de365b5-c806-3681-8b78-35f508913254 | -7.0364 | -42.8272 | 2026-10-01 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 09a82d68-3da5-36a2-9d7e-32d2b1b370e6 | -8.6265 | -45.3282 | 2026-10-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 295.3 |
| 63c6e34e-8666-366d-8b03-8ab70cbef237 | -12.4732 | -44.167 | 2026-10-01 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 57690b36-947e-3f0e-9ca9-cec22183ffef | -8.1683 | -54.8037 | 2026-10-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4544ca44-b337-34fe-8f2a-932a7a1b1fb3 | -8.6268 | -45.3054 | 2026-10-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 6f229d13-a54c-3abe-b361-61f4404242e4 | -12.4544 | -44.1466 | 2026-10-01 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 5836a077-2bb1-35c4-866f-c2d03f0e33fa | -9.8613 | -44.9577 | 2026-10-01 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| abee8eae-7c98-31eb-83bc-b5f4cd1c7904 | -7.7221 | -54.7913 | 2026-10-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| f0ba68ab-3aec-31a2-a9d8-2eaa0d10d447 | -10.1881 | -49.9703 | 2026-10-01 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 996826c7-0b7e-3d1e-b344-661219c510d4 | -7.7405 | -54.8103 | 2026-10-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d15142cd-b5c2-3c2f-adf2-e50034369fd7 | -12.4539 | -44.1702 | 2026-10-01 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 262.3 |
| 857051c5-2ebe-3f85-9b8f-d4b90fd57886 | -10.8777 | -50.6886 | 2026-10-01 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 8745e3c6-f32e-326c-b9df-10665b36c563 | -8.6457 | -45.3034 | 2026-10-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| e4b46c74-25e9-3f94-ba9d-5bf0a92fd303 | -10.2067 | -49.9898 | 2026-10-01 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| a43bab16-e6f3-34d9-8c94-07211203c9c0 | -11.6837 | -43.2305 | 2026-10-01 14:00:00 | GOES-19 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 407.3 |
| 33ccc075-b4cd-3f19-9a7a-721d89bde951 | -5.8597 | -53.479 | 2026-10-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 57ca6ee9-e5d2-36a1-b4cb-0af1c361e9fd | -11.7178 | -43.4623 | 2026-10-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| b32c82d7-745f-3bb7-b854-df2866f95544 | -7.7407 | -54.7901 | 2026-10-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| fe6137d3-4aca-3639-a134-738f87641927 | -7.0801 | -42.3017 | 2026-10-01 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| c3050508-d13a-3790-a237-401c5ae3de75 | -11.0962 | -51.3231 | 2026-10-01 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 1cfd1553-ebf8-3593-a4bb-c7ccd3012685 | -10.9337 | -50.7465 | 2026-10-01 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e0ccaf93-ad78-348b-ab88-b51d55247e84 | -8.8365 | -49.6934 | 2026-10-01 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c0d4faeb-c2ad-3f53-ae07-7a57b0b78bce | -11.0288 | -50.7151 | 2026-10-01 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 43939d46-9057-3100-ba03-a4be1e60ebde | -12.6463 | -47.2598 | 2026-10-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 9fc02e11-42d7-345b-b6e9-55e5ce2bff83 | -5.9152 | -53.4762 | 2026-10-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| d3ce4177-07f9-3dd3-907c-37627c146e0b | -7.055 | -42.849 | 2026-10-01 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 5c7511c5-a69b-33dc-9a33-414994d28bcf | -10.5388 | -45.3759 | 2026-10-01 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 0c82d2cc-e193-3760-a413-17ea24a262c0 | -9.0247 | -49.6549 | 2026-10-01 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a5dfbfe4-3740-393d-9381-949a639ae72e | -12.6459 | -47.2823 | 2026-10-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 2514e52b-c449-384a-9628-f8bce6fc9035 | -9.8617 | -44.9347 | 2026-10-01 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| edf4556e-c4ef-398d-ba8d-3c7951e081e4 | -11.4298 | -43.4833 | 2026-10-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| b2003ce2-f022-3a39-be82-fa1a46065f4d | -14.659 | -41.0175 | 2026-10-01 14:00:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 135.7 |
| d589477d-80c1-386d-827e-dfdb35717af5 | -7.0448 | -42.0906 | 2026-10-01 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| a92f6354-c29d-3141-b7d8-8a078e5ba0e2 | -15.6481 | -44.7217 | 2026-10-01 14:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 6c0c7cce-5925-37e0-8cc3-8a13a0b7fb5f | -14.3574 | -44.7569 | 2026-10-01 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 219.8 |
| ea08321f-3d98-3209-9545-c05007bafb89 | -11.2282 | -45.1682 | 2026-10-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| ce6dfb3e-54f4-309d-87d1-99b76123cc2c | -12.4535 | -44.1937 | 2026-10-01 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 4155e0dd-efb8-32b9-ad34-64f88203a843 | -5.8412 | -53.4799 | 2026-10-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| e8d9a6cf-7c68-3f96-b24f-246304a60bf2 | -11.4499 | -43.4329 | 2026-10-01 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 515.8 |
| ae56f89f-ad03-3104-bac7-079061271620 | -9.8067 | -44.8035 | 2026-10-01 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 4b7075ca-f6ba-3e3c-92c0-9c5100b9eb72 | -5.8411 | -53.5002 | 2026-10-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 7438db06-ec64-31d0-89cf-05360193cd0a | -11.2275 | -45.2143 | 2026-10-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a7038bde-b77d-3a28-a66d-2a8208a38b95 | -13.3462 | -43.9489 | 2026-10-01 14:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| bb6b106a-ff5d-3b5f-918c-8de8e79e409a | -14.3379 | -44.7605 | 2026-10-01 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |


[Clique aqui para ver as próximas entradas](README101.md)
