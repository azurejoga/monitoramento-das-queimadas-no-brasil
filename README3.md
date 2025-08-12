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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c1e42bc-5c4f-39c8-8b46-4be3cddc5190 | -16.2957 | -52.923 | 2025-08-12 01:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 61e69988-39f5-37a1-96d9-0672957cdc5c | -23.1491 | -47.0754 | 2025-08-12 01:00:00 | GOES-19 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.8 |
| fd82f460-8f1c-3038-a8ab-353717c384e0 | -8.9401 | -60.7288 | 2025-08-12 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 239f8636-3260-3ed1-b1ab-296d9c9e5040 | -22.62594 | -54.99573 | 2025-08-12 01:05:00 | TERRA_M-M | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 162.1 |
| 22c6a218-bb20-307c-b43d-1000ad292d42 | -21.21127 | -49.62045 | 2025-08-12 01:05:00 | TERRA_M-M | ADOLFO | SÃO PAULO | Brasil | 3500204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| ee35f374-f2f5-3415-8d98-82cdd7a1c34c | -19.71371 | -46.22182 | 2025-08-12 01:05:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 0ff8889a-f853-318f-a367-dc0669a6e3a1 | -19.3042 | -48.42611 | 2025-08-12 01:05:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 079d0481-6fac-38fb-ac62-7ba439fad166 | -19.29815 | -48.42084 | 2025-08-12 01:05:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 3bd5606a-0d3b-3829-9cea-e29cc79ad6e1 | -21.77635 | -48.31396 | 2025-08-12 01:05:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 9a5ae884-b847-3fd1-93c7-d98d526024e4 | -22.97413 | -49.04041 | 2025-08-12 01:05:00 | TERRA_M-M | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7a570d25-3498-3e2f-b4a9-9cdcbee2701d | -21.77588 | -48.30279 | 2025-08-12 01:05:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 2812e391-b11d-3446-85ec-1d7b5e68bdcd | -19.29532 | -48.44573 | 2025-08-12 01:05:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c1c16354-93a1-399a-93d8-e4cbb6a5b708 | -23.13594 | -47.0826 | 2025-08-12 01:05:00 | TERRA_M-M | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 162b83b3-5e98-3e00-b1bb-610c54b1d2f0 | -23.13277 | -47.06464 | 2025-08-12 01:05:00 | TERRA_M-M | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| 353dbe14-c363-3409-bf5e-24206670c2b5 | -23.13635 | -47.05732 | 2025-08-12 01:05:00 | TERRA_M-M | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| 2c61a6df-163a-3743-b656-f8b29619c663 | -22.98697 | -49.05235 | 2025-08-12 01:05:00 | TERRA_M-M | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 52be5175-b847-37ca-9842-4e6e1677fb59 | -22.98466 | -49.03838 | 2025-08-12 01:05:00 | TERRA_M-M | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 67.3 |
| cac518ae-d276-35a8-aa5f-d558ec597cf0 | -23.04139 | -47.06944 | 2025-08-12 01:05:00 | TERRA_M-M | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| f5a7403a-d4e6-35f5-897f-dedcaea7ad82 | -19.29241 | -48.42847 | 2025-08-12 01:05:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 4650c83e-a8ba-3da0-9d57-c6bcce0d7c75 | -16.98733 | -49.20507 | 2025-08-12 01:05:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| eb1b1f31-c5be-301a-9881-188c979dfc7b | -19.72258 | -46.22528 | 2025-08-12 01:05:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 32a3953e-8bfa-3e29-9431-2ec5be5e5ac7 | -21.7786 | -48.31895 | 2025-08-12 01:05:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 27d6826c-9634-3758-8724-933f3eef9edf | -23.13965 | -47.07537 | 2025-08-12 01:05:00 | TERRA_M-M | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| e5527ea4-5f0a-3f4f-9cc9-e8fc05c425d8 | -19.30116 | -48.43798 | 2025-08-12 01:05:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 127.5 |
| b994d120-7af0-3973-b0cc-67e556c97505 | -22.62724 | -55.00581 | 2025-08-12 01:05:00 | TERRA_M-M | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 251.9 |
| 550395d2-6343-3ea3-ae64-87c8fe94b1b9 | -14.03939 | -47.42149 | 2025-08-12 01:07:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e356c7b0-c6de-34fb-9e36-f90a2fdcc274 | -14.70071 | -53.71817 | 2025-08-12 01:07:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 12d1c699-e11b-3e34-9df1-82c7e030ae81 | -11.7704 | -49.10738 | 2025-08-12 01:07:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c8d47de9-75c2-30f2-bf7d-76e3f076239f | -13.03731 | -56.8455 | 2025-08-12 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2e8b5602-03c8-33bc-834a-f0b212f64b9e | -10.74824 | -58.01857 | 2025-08-12 01:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c98dbaa4-3337-3544-8d58-eef02fe2dcce | -9.71713 | -49.49129 | 2025-08-12 01:07:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 9155bd71-5429-3f89-a999-8e5865a72c26 | -14.68423 | -53.72653 | 2025-08-12 01:07:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c57d863a-04d9-3eb5-8874-b7c50a2bebc1 | -11.72055 | -48.35172 | 2025-08-12 01:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| c72b4fb5-402b-353e-a473-376207887283 | -9.71717 | -49.47624 | 2025-08-12 01:07:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 3c35951a-ddba-307d-a515-3b78e72d7693 | -11.69293 | -51.60608 | 2025-08-12 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bc024a50-3de4-3db5-9c14-ff88587ff7d2 | -10.31528 | -54.16627 | 2025-08-12 01:07:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f9980fa5-acbe-333e-80e7-7d20d852c429 | -13.90363 | -51.8373 | 2025-08-12 01:07:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |
| fd069c72-91a2-3c3c-bd57-f72063a83843 | -16.30825 | -52.91706 | 2025-08-12 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 41cf6d03-6787-3256-aa06-dd01049bbbba | -16.30678 | -52.90703 | 2025-08-12 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bd828b1f-faaa-37fc-a782-4341117c46d2 | -10.35239 | -57.60863 | 2025-08-12 01:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8ddfe85e-bf66-3517-a9eb-4d828dbdc7f3 | -12.57592 | -47.01476 | 2025-08-12 01:07:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 7fb9b14f-fe12-34fe-84cb-f7d3348524ca | -15.30094 | -59.24279 | 2025-08-12 01:07:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 82c4f53f-c330-37b3-97a2-2867ead54a20 | -11.46036 | -50.16787 | 2025-08-12 01:07:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| cbbb7e4c-ae38-311d-81f3-cdb3d3dcac26 | -12.56101 | -47.01835 | 2025-08-12 01:07:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 8ed5c32b-591d-3147-907a-890975e91954 | -11.45572 | -50.17522 | 2025-08-12 01:07:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 36085f99-aa37-318e-8e99-9e7d42217fea | -16.3097 | -52.92692 | 2025-08-12 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dce5479c-68e9-3dc9-b19f-111629ef7f88 | -11.46323 | -50.18527 | 2025-08-12 01:07:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5b62ee28-f300-3ce8-afa6-2a2b49bfbce3 | -9.47287 | -57.84085 | 2025-08-12 01:07:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 6e96327c-6b2f-3047-b9cb-d31dcf3a1aa7 | -14.69161 | -53.71954 | 2025-08-12 01:07:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| bfbd372b-451b-3129-9029-29744a89474f | -14.0284 | -47.41871 | 2025-08-12 01:07:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 63fb76b1-edd4-3f9b-8695-7f58c1e894aa | -16.29898 | -52.91846 | 2025-08-12 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 659ceecf-2521-3257-8ef9-fe921ed56312 | -13.06567 | -56.85103 | 2025-08-12 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6815c311-c525-31ee-8156-873a40912013 | -11.465 | -50.15569 | 2025-08-12 01:07:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b691dd3e-8896-3664-9ce3-61406a2891f4 | -12.76615 | -45.46244 | 2025-08-12 01:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 149b1721-9591-3b1d-a544-4443eed27e9a | -11.72893 | -48.35681 | 2025-08-12 01:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 86a9bf80-1765-3334-83b3-d67b894cd505 | -14.6902 | -53.70992 | 2025-08-12 01:07:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 474ff441-40db-3c70-9f96-95092f9deafc | -14.68284 | -53.71692 | 2025-08-12 01:07:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2548a923-dde2-3bd0-aa0e-19b298e13bb9 | -12.57087 | -46.98545 | 2025-08-12 01:07:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 19a92043-7b55-3bc7-95e7-6970e5e635a2 | -10.31386 | -54.15635 | 2025-08-12 01:07:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 67bd9298-0bba-3f9e-b661-0145b5c1d99c | -15.40604 | -53.8767 | 2025-08-12 01:07:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c6d4d5df-80c3-3d0e-8e63-065cc223a03c | -13.04634 | -56.84419 | 2025-08-12 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 88383669-dcaf-3dce-937d-c65ea26e7722 | -13.06441 | -56.84162 | 2025-08-12 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 699e664d-87da-3433-b7b0-9c18dba2d029 | -16.28974 | -52.91999 | 2025-08-12 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| b01156b7-c2d9-39bb-850b-22049969c308 | -16.28826 | -52.91002 | 2025-08-12 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 8d4095f9-4d07-3940-87e7-187196c277be | -11.64669 | -48.32748 | 2025-08-12 01:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| f4d341f0-ed9c-3e80-b4ad-81eb12f6eca7 | -10.36208 | -50.83434 | 2025-08-12 01:07:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 800b8297-7dc7-3fef-bba4-8085666a5184 | -10.73896 | -58.01988 | 2025-08-12 01:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 13f20c12-4d43-3548-966a-f33a8bd01c42 | -11.68538 | -51.58572 | 2025-08-12 01:07:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 64447248-feb5-3406-9109-3a19bc8958c2 | -10.35959 | -50.81818 | 2025-08-12 01:07:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b4a12f5b-4f76-313a-bf3d-a690c4b31577 | -13.90175 | -51.82508 | 2025-08-12 01:07:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7a6da9f0-af61-3e97-b66e-38b85b5be32f | -12.57363 | -47.00894 | 2025-08-12 01:07:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| d1abe08b-19b3-3e88-a53e-4002b28faf1f | -9.72046 | -49.49732 | 2025-08-12 01:07:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 8ba29fcb-4da6-39d4-ab0f-67b6e8cd561b | -13.07345 | -56.84037 | 2025-08-12 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 08879021-727e-3b29-b849-569f7e2240e7 | -12.77938 | -45.46527 | 2025-08-12 01:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c154b976-b585-3b85-bee0-f75a6c59a223 | -11.69078 | -51.59251 | 2025-08-12 01:07:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 51043a55-ca87-359d-a76b-d4450d273fdc | -9.71367 | -49.47017 | 2025-08-12 01:07:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 0344dc8f-e12a-32e7-acd6-4eca7fc3c483 | -12.78294 | -45.45933 | 2025-08-12 01:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 53c99050-6c6c-3419-b2fc-76e50798cbde | -15.57852 | -47.32392 | 2025-08-12 01:07:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 87232bdc-c981-3dec-9ccb-46eb0b2190a6 | -16.29753 | -52.90857 | 2025-08-12 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| cd644bab-e3d2-3d3b-bccb-9f0dc5908d7a | -13.07472 | -56.84978 | 2025-08-12 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b3bf2fd-e2f6-3905-9890-edaeafd2e99f | -10.35044 | -50.83625 | 2025-08-12 01:07:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 746691b7-69cb-3366-8edf-a96a41e1b566 | -15.4164 | -53.88477 | 2025-08-12 01:07:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c1a8862f-7cd6-3ccb-a2da-8ba6b760a6b9 | -14.69302 | -53.72916 | 2025-08-12 01:07:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5befbe5c-904e-3617-8545-bbbf33ef541f | -10.34793 | -50.82013 | 2025-08-12 01:07:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 1b47cf68-7f5f-357e-8b26-3fcd6f17fd64 | -16.30044 | -52.92835 | 2025-08-12 01:07:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 699cbb2e-485f-362d-a481-e939c5bd2c89 | -10.96685 | -49.57751 | 2025-08-12 01:07:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7b30e86c-39bc-38f2-b255-e1a440d2d826 | -11.68744 | -51.59935 | 2025-08-12 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| d29223a2-e873-35f0-a003-47bca4bd3f8a | -9.38296 | -61.52331 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 8902e4ba-9293-3641-b348-af3d2986e065 | -9.18939 | -59.65773 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 4e6e344b-0a0f-3e1f-a9d1-fa8b9be6a1b3 | -8.57704 | -54.71395 | 2025-08-12 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d8357302-e7ee-361b-86f5-1dfddf5191f1 | -9.39317 | -61.53164 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 53208355-3326-3834-ae2c-6e7fe509b34a | -5.88912 | -57.74867 | 2025-08-12 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9139a6c3-f0ef-3a1e-9371-eac859be2a46 | -8.56144 | -54.72223 | 2025-08-12 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1de35099-5e74-3bae-acbf-22a1f8ab3222 | -8.56783 | -54.71533 | 2025-08-12 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e68cc716-98ea-3fcc-9702-b60b77f961e6 | -8.57845 | -54.72364 | 2025-08-12 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 17e64f65-da29-3e71-b447-6cacde0b0024 | -7.13783 | -60.12049 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 243.3 |
| d4112aa1-9ad2-3681-94bd-ba31bfce1457 | -8.56924 | -54.72504 | 2025-08-12 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 0cbdf1b3-2da9-3bb6-8ec2-c03a24348282 | -7.07888 | -59.20255 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d031b777-02db-39ae-b741-613447537ad8 | -8.57562 | -54.7042 | 2025-08-12 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 03fbdc89-9d60-3f6d-9bb6-083dd94fab19 | -8.93765 | -60.72106 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |


[Clique aqui para ver as próximas entradas](README4.md)
