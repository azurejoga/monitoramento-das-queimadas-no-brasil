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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e26b122c-beca-3dff-ac0f-5ae826c971c2 | -3.93391 | -52.13412 | 2025-09-10 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6fe5830-ec7f-3b99-b945-178a48faa29a | -5.39884 | -48.85013 | 2025-09-10 05:01:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b663cc19-7872-38c2-9651-211a6fc5ee58 | -6.1882 | -43.50195 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b329393-4983-3749-bab3-f8c474e9a2dc | -5.67969 | -43.35212 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0151b83-e123-39b6-ad13-c1abcf67152a | -1.83781 | -54.73178 | 2025-09-10 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f19d6e04-1c27-395b-94f4-9039d63ec5c3 | -5.67864 | -43.35312 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5038e089-47d3-361e-9991-a1fc2e3fab80 | -5.22082 | -43.69553 | 2025-09-10 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3069bbf8-05d6-33f4-90f4-642639835d19 | -5.67236 | -43.35672 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e043709-87af-3c58-bacd-c5baf7ea9498 | -6.29116 | -44.21645 | 2025-09-10 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e16fcaf-081d-3399-87ee-57e839d29409 | -5.79185 | -43.88867 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f677a945-0185-3766-b444-2a4417999d56 | -5.66487 | -43.35642 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9d09a83-69fb-396a-a70b-ed913ef89ba5 | -3.32164 | -54.90833 | 2025-09-10 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7595225f-574b-389e-83cd-c4c4523bb6c3 | -3.85673 | -52.00412 | 2025-09-10 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 636c620a-ed45-3ba4-a0fa-1943f0ac4eb6 | -4.86737 | -42.77526 | 2025-09-10 05:01:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84793ac6-466b-3446-a74c-350bc6183c67 | -6.20071 | -43.50602 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b8f3434a-432f-3b9e-a6d6-519c5548c2d9 | -5.74136 | -47.47499 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68bd725d-b432-394f-b17c-94942961a0a4 | -2.51144 | -51.90235 | 2025-09-10 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9584e408-2195-3628-bc5d-6ec147a303db | -3.6789 | -49.01962 | 2025-09-10 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3418a8e-b1ba-3d34-a61f-a03342a4627f | -5.64399 | -42.62464 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 96e28533-d5eb-3f59-b708-ec314e068ab9 | -5.66587 | -43.35552 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54fe23ef-56eb-39a6-b78e-3a0d79819042 | -6.1694 | -45.81558 | 2025-09-10 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e241992-6ba6-331d-9037-5fc0b0a897a1 | -5.7476 | -47.46701 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22a9a950-e520-3e4c-ad1d-8d68e5102f9a | -3.81383 | -51.29107 | 2025-09-10 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94640c8e-4269-3164-9f4f-4145764cc3f5 | -5.67116 | -43.90319 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eac4790d-8c96-311b-b1b5-1719ce695088 | -4.2002 | -55.13075 | 2025-09-10 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ed7717f-3e26-3c83-adc5-6b4695f779c4 | -5.53308 | -42.66344 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b3daba64-ba26-3b3e-897c-69df9fd5d01c | -6.05873 | -43.14083 | 2025-09-10 05:01:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 89cbf2c0-47c5-3ff7-9e54-6c8eead0cc8e | -4.19911 | -55.13765 | 2025-09-10 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f549692-7a37-3bda-94d2-1dfc731395db | -3.24288 | -52.85278 | 2025-09-10 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5333889b-2d01-39b8-82f1-962c9fc67b89 | -3.89919 | -52.12031 | 2025-09-10 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7719ed6-1c21-3117-928a-0fed9118cad4 | -4.48181 | -48.11663 | 2025-09-10 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1b484bc1-f17a-30fb-8f9c-111d55687e81 | -6.24479 | -43.42674 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9c904145-a460-3bce-bb35-fbd7270ee33d | -5.646 | -43.92227 | 2025-09-10 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e3bcf31-befc-388a-94df-813a1f3252d6 | -5.45061 | -43.47034 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6d98ea83-40d4-3bac-bdc1-6a9fc2d87c34 | -2.51439 | -51.90701 | 2025-09-10 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afae91f4-95e0-393f-9654-6390513b217c | -5.42044 | -43.45042 | 2025-09-10 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b853b197-cd00-3ccc-98d5-9c5b37c556a2 | -6.34807 | -44.85539 | 2025-09-10 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d31780c5-8fc3-3112-b8b0-652217fca118 | -5.41248 | -43.46 | 2025-09-10 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d7162535-ea8c-369e-9902-48ba832c4b25 | -6.39966 | -43.50541 | 2025-09-10 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7abba63-7f00-3a9a-aa26-f2cd07a11cdd | -6.25213 | -43.42193 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 17fd1776-2c0c-3b21-911b-dc320bf6c4e7 | -3.63731 | -49.21117 | 2025-09-10 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 785223b9-545a-30c8-887b-1b6df7856501 | -3.63521 | -49.20734 | 2025-09-10 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5329ed65-2bce-3556-837a-d6b064bd5b54 | -4.49489 | -47.82669 | 2025-09-10 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf8ecac5-202a-35f5-a0c1-0ec79749d92f | -5.67397 | -43.34546 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5b51efe-729f-3783-981b-0e0c3f6d3a05 | -5.67289 | -43.34638 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13761e66-2e1b-3b9d-a1b3-dcd727fe663e | -6.39309 | -43.50476 | 2025-09-10 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 068261e9-0353-3bd3-9813-b969947ffbdc | -3.80237 | -52.25727 | 2025-09-10 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bde24bf9-3148-39fc-8922-e277913c29e3 | -2.93196 | -53.69466 | 2025-09-10 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83663f5c-5389-31e0-beaf-b7a2fcaee52a | -5.68667 | -43.34313 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d48fd5a8-f3b7-3e20-8c21-5e523516c971 | -6.21746 | -45.63305 | 2025-09-10 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76a2998b-6184-3b6a-8dd7-6ffe962dc496 | -5.74678 | -47.47275 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99c5afed-1bb2-30a3-8d8e-a8a018689f3b | -5.88466 | -46.09051 | 2025-09-10 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ca44a02-f865-31e0-adbc-dba65982a2b1 | -4.53076 | -54.84366 | 2025-09-10 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ff83a0d-5105-35b8-a660-4628307c8dfd | -6.25953 | -43.41674 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4dbe9226-7c77-3b63-abf9-59cd39df7ea3 | -5.74176 | -47.47216 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e41c6e09-f5d9-3d35-b5cd-e367dc340c83 | -4.09218 | -41.5788 | 2025-09-10 05:01:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 73aab984-92fb-3d26-8b65-8c0d2166fa92 | -6.25806 | -43.41767 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 1d605975-f1f9-36f1-b0e5-c5d5c6547b49 | -5.22647 | -43.70155 | 2025-09-10 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0120a41e-6832-3c09-836e-016cc734164c | -5.53049 | -46.49818 | 2025-09-10 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 828c22c0-8f14-3f9e-915b-1d9aba45a226 | -5.6789 | -43.35764 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31ae8651-419a-3e7a-9902-7aa8c3301625 | 0.83084 | -51.18171 | 2025-09-10 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| defea093-4ef2-3a6a-aa2d-7b2f9a901870 | -6.1689 | -45.81929 | 2025-09-10 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6ae7428-365e-3bb0-92aa-62a8ffa93d6d | -6.24793 | -43.40378 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 310425cc-e312-3441-8284-5f33c00ed51c | -5.52639 | -46.4999 | 2025-09-10 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e7dd531-3608-35a4-ae83-86eda0074595 | -3.20813 | -54.96105 | 2025-09-10 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82e318dc-b7b3-3374-8c86-1b5f2503c80e | -4.86916 | -42.7627 | 2025-09-10 05:01:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15bf5c78-e6f7-3e02-95f4-ed8eed36c5d5 | -5.93967 | -42.78034 | 2025-09-10 05:01:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66d27135-ce32-3714-a3c2-5a89f07b2906 | -5.85835 | -48.16419 | 2025-09-10 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9489a31-9a45-37aa-a24b-30aedff280ce | -5.53849 | -42.66388 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3c7f7642-5814-371f-a9b6-0a1c07944d29 | -4.28665 | -55.01406 | 2025-09-10 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3513116d-9b69-3c77-bdd3-99877c21a9da | -5.66009 | -43.91361 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dce1a5e-749c-3de7-849a-d7bb37cb7fec | -4.36433 | -54.75712 | 2025-09-10 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08d8ce3d-7ee6-367d-854d-d2955fa1423a | -5.44487 | -43.46579 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 520cdbac-fbcb-3b94-9052-b7d982d4c2cf | -5.4132 | -43.456 | 2025-09-10 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a259d37-6a1f-345f-b2fe-47d893a68cbb | -4.86404 | -42.77232 | 2025-09-10 05:01:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4517d070-3fea-36f3-89d1-e1bf25aaa480 | -5.45136 | -43.46516 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7870d680-c1c7-3112-8e1c-1c79ff19f855 | -5.53094 | -46.4949 | 2025-09-10 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ec8e4a4-7c66-35b0-9729-658ab9318ba1 | -3.37131 | -52.79443 | 2025-09-10 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3aab1db-84ae-3e85-9e9d-8c741a688637 | -4.8386 | -45.35144 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a1624e6-0693-3538-b9fd-5c9bb99e0ccb | -6.25952 | -43.40645 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7b6c3980-0685-3b96-85a9-98a8b79b2d17 | -5.68013 | -43.34214 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb9abe56-98ed-3c33-871d-20023d9ebac8 | -6.20764 | -45.61983 | 2025-09-10 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6b7d4dc-709c-3692-94b0-6b1100929360 | -5.74719 | -47.46989 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aba78f6c-12ad-3ef9-8463-4129381d8097 | -5.67316 | -43.3511 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7049e8e-4e29-37eb-97ef-2ef79321573e | -3.12494 | -52.00172 | 2025-09-10 05:01:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c60d9498-579e-38cd-a577-643635ae55ee | -6.21281 | -45.62459 | 2025-09-10 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ad7f7c6-0a4f-3850-a61c-dc0dfa20f42d | -4.47242 | -48.11523 | 2025-09-10 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5acd577e-a8e2-3c9c-902d-6ae52b5cb4c0 | -5.66639 | -43.34515 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7467139c-2ed7-3864-a8fc-0b42380e71bb | -5.67606 | -45.46869 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebf54e96-4f2a-320b-9abd-e3c093bb81db | -5.64201 | -42.62845 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b58a85cf-be84-3493-9efe-4cc2ace4269f | -5.66419 | -43.90718 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f02e4166-230d-3bad-9763-5a55861eff16 | -5.57811 | -45.0344 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 57f7ac12-913a-3245-8e0f-d0ff6c0c8422 | -1.96778 | -48.43697 | 2025-09-10 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 215ef8ef-1df2-3836-81f7-5d44a2c56aaa | -4.08126 | -48.04302 | 2025-09-10 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbd4d6e4-9e01-34fe-9f24-144ae90c10b8 | -6.29184 | -44.21135 | 2025-09-10 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac5ff3a5-f332-3d44-9c1f-55f852a3bbce | -5.74297 | -47.46358 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6182f05d-ce04-3034-a462-47db94557769 | -5.44486 | -43.46447 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f63f55cf-cf5c-337d-b400-fc024a653f78 | -4.86825 | -42.76907 | 2025-09-10 05:01:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62cf7174-dc8f-3707-beba-8c09d5448b84 | -4.83412 | -45.35831 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8872088f-b56d-3cf7-a534-032b76a6a2de | -3.20537 | -54.9571 | 2025-09-10 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README85.md)
