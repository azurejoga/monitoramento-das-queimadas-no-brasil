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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d1696df-5fb9-32e2-bfee-99414a98b557 | -20.39837 | -46.27462 | 2025-09-11 04:25:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a06a322-74f3-39e2-9e55-64b472cc123f | -17.72067 | -48.19611 | 2025-09-11 04:25:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1608e04c-6fe1-3106-ab3e-d05ee899b355 | -18.0108 | -47.99712 | 2025-09-11 04:25:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b07af519-6206-320c-aecd-9b3166617c9f | -19.13586 | -43.05473 | 2025-09-11 04:25:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 651f7825-b392-3c29-9666-6c36183fa692 | -14.5074 | -53.93515 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49c316ad-bf51-375c-96d3-a4e9d0fb3a7d | -19.2541 | -48.00502 | 2025-09-11 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09c1be3d-8c0d-3106-8676-318402e6dfd7 | -20.0745 | -47.53859 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea50c561-455e-3a72-8757-66dc16d5a273 | -20.0768 | -47.52384 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35286292-eb3f-3400-b4e0-533e30bddb5c | -15.11651 | -48.02608 | 2025-09-11 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec13f627-5dae-31c0-8f29-332f83c09b6d | -17.68613 | -44.20172 | 2025-09-11 04:25:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 317fee63-4193-3782-b70c-4876fb62f230 | -15.87595 | -54.9306 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| abfd779e-7db3-3451-adc7-64a1528e5933 | -20.54852 | -47.62362 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f29bd3c-fb4d-3f76-b4ec-b365f3ebc56f | -17.79667 | -44.41192 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12b0c055-5d2e-359c-b1d7-f87c2f91d017 | -20.51679 | -47.62946 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bd88ca7-328a-3e75-a045-45dbeb8f0752 | -21.12608 | -47.73027 | 2025-09-11 04:25:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c3b24a4-2f50-346c-ba45-d9bb3251bb58 | -19.15928 | -43.05772 | 2025-09-11 04:25:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 65c31d88-aea3-327b-831b-e3c8ce1dddf3 | -17.27136 | -46.08479 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 88c15771-6a72-3765-b8a2-67d990ceff1b | -15.13578 | -52.42285 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbbfee3b-dd61-35e3-a154-e9e602635e8c | -16.60896 | -49.78167 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67eef19b-d72e-3c54-bf6c-e707190159da | -15.08532 | -50.07495 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c14ead5e-56bf-39fb-8695-d5d7ee23597f | -16.57648 | -49.31455 | 2025-09-11 04:25:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75d1b4df-08d3-30b7-8b63-20d7890e3769 | -15.72317 | -44.44096 | 2025-09-11 04:25:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec2c96d2-0f6b-3bca-aadd-e6b5ba0291f6 | -15.80569 | -52.24003 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa245cb2-8bad-376f-a5b5-2c647ae847fb | -15.97627 | -49.63443 | 2025-09-11 04:25:00 | NPP-375D | ITAGUARI | GOIÁS | Brasil | 5210562 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd3a2b9d-61be-3731-8ad5-3f2c39475fe8 | -21.29019 | -47.0859 | 2025-09-11 04:25:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0c4728ce-4b16-3d05-96a5-1fca933baa5a | -15.55853 | -54.75067 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 355490de-3e62-3f82-b03b-61b41107c8e9 | -15.61417 | -52.76628 | 2025-09-11 04:25:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3fabff9-faeb-3431-a516-6d767cf20b83 | -15.10089 | -50.06594 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c41ce118-7954-3c53-86bd-bd93f669a521 | -15.80843 | -52.28368 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1f73cff-b325-3402-bc79-c73e587e1ea0 | -15.14204 | -52.43579 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7babd35f-e455-3c7d-ab00-83b4c4750978 | -21.34478 | -45.79457 | 2025-09-11 04:25:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0c7edd1-c59b-3eba-be89-441c8bb3d04c | -19.98046 | -47.62512 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d8daa6c1-a800-3946-9243-ada33bf4042c | -17.94315 | -44.48694 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d42f6abe-f84d-3d21-92cc-87769f68880d | -16.2895 | -45.68562 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e154aed1-f259-3881-8b52-c371ec98fe06 | -18.71235 | -47.18025 | 2025-09-11 04:25:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 030beb28-17ab-3c25-a370-7b81611be073 | -15.80166 | -52.27441 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e005ac5b-3cd2-32b3-b583-83c091a9ac30 | -20.00333 | -47.6102 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a925abbe-e1c0-3bcd-8b5f-87a49b218536 | -17.70722 | -44.4383 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f80d2a08-5f9a-3a51-ab4d-b4b9d79e0382 | -16.62595 | -49.7677 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23734872-2030-3b79-816d-b4bb44d782f5 | -16.62732 | -49.75971 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a76cfabc-2bd6-30cc-85af-044c6ec8fb17 | -17.32842 | -46.6876 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 070be329-52c3-3a5e-bccd-804a3f591843 | -20.17305 | -44.62033 | 2025-09-11 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f7fc437-a035-30a0-9f66-459f2d54039e | -20.15727 | -41.03747 | 2025-09-11 04:25:00 | NPP-375D | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ba65dc26-07f0-3929-8aa4-bcb60113c03e | -15.13702 | -52.43945 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99901492-a4b2-3b47-9509-68f95db52a15 | -16.53338 | -55.17463 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ef2ab8b5-8ea1-33cf-af51-ca50a8e65cdf | -20.04299 | -42.7338 | 2025-09-11 04:25:00 | NPP-375D | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 789f6c5f-9d26-3dd2-9932-4cb8dcea69eb | -15.79752 | -52.26197 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b01d808-57b7-332d-aef6-538bd246802c | -20.3944 | -46.27792 | 2025-09-11 04:25:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63dfdad1-92f7-3a11-a220-a7fde7e35246 | -16.56212 | -49.74072 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b59a452-f268-3871-838c-30651051c481 | -14.88552 | -55.85217 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd861442-2f00-3e3c-b8f5-733df29ed904 | -17.95854 | -44.48108 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 756ffef4-b8c5-30db-9a81-8fca6328a31c | -21.28188 | -48.3331 | 2025-09-11 04:25:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 670dc2ad-796a-3f6d-9954-778007037cbc | -18.50478 | -47.42229 | 2025-09-11 04:25:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00c3c787-67b0-37aa-a791-6197928fa74b | -14.884 | -55.84002 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b96cda33-bf74-332a-904a-4e6619aafced | -15.54765 | -54.76789 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46a8792a-7d11-3e72-a756-a385142bbefa | -20.00653 | -47.63349 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57de5299-0abf-31c2-80d3-499d13150c50 | -16.29837 | -50.06081 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fe054508-e21a-3b30-a21e-bfb344c98988 | -20.06631 | -45.29068 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4791161-96da-3ed0-8089-7884cc0234e6 | -15.13498 | -48.60946 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 791fa789-689c-3b38-a900-82f70eeb72a0 | -18.01554 | -47.13433 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| caa756b9-1787-3513-a19d-3c3d842015e4 | -15.80405 | -52.23891 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2bc28bc-5fe6-3b71-a637-3773bd491849 | -16.29911 | -50.05651 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63eb98ef-aebb-32c6-9fac-aade807669fe | -15.80319 | -52.26624 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42b5d442-ab10-3190-9975-3ffda543a579 | -15.1384 | -48.61013 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bb3ee16-7b04-3685-8257-8638fade436e | -18.7258 | -48.13604 | 2025-09-11 04:25:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 272a3fa4-73b0-37aa-8d78-6be67aa5dffd | -16.61607 | -49.78278 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6bdb05e-2670-3a84-a6dd-9fcff92c9be2 | -20.91292 | -46.99652 | 2025-09-11 04:25:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fc9813c-8ffc-3514-87d3-22a8ebad9686 | -22.56256 | -46.0457 | 2025-09-11 04:25:00 | NPP-375D | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1c4a3ef-49d9-3c3e-824a-165d584acdc8 | -15.54708 | -54.74546 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42fed28b-abb9-3a58-9987-b0aecdf61770 | -20.17246 | -44.62453 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fce26564-1022-3a60-a76c-69cd518ff1a1 | -15.48064 | -49.36076 | 2025-09-11 04:25:00 | NPP-375D | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ce74c56-3c60-3d48-9170-402e4b3061ba | -18.55723 | -46.56285 | 2025-09-11 04:25:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45933c46-3395-3119-b068-827907d1243f | -15.68037 | -47.02075 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d6aa7d9-b2b5-3d02-83a9-c2ca194077be | -15.67257 | -47.02679 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4830bd37-dd9d-3462-b800-d278644a7ba0 | -15.89442 | -48.18473 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 060ee914-72cd-3b62-b12b-4f41c0b646c0 | -15.12195 | -52.4041 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45fec05f-1a5c-34f4-8805-a6f56dea83c0 | -17.7114 | -44.43459 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d2c519e-e9e8-3396-8124-d55f12a5ac78 | -18.40773 | -43.48069 | 2025-09-11 04:25:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db3404e2-4fe0-3f75-ab46-0bda20b862f2 | -17.24965 | -46.08549 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e70d4c2f-3dd8-3093-a3aa-116c491b428a | -15.10149 | -50.06845 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6437c593-4dcf-3ada-8506-558926292459 | -15.88276 | -44.82178 | 2025-09-11 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecbe04db-9f17-39c8-b52b-de051c7b1843 | -18.62329 | -44.2664 | 2025-09-11 04:25:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbba3a1f-2459-3255-bdd4-54bbf3b0da5f | -19.02951 | -42.15112 | 2025-09-11 04:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4bd1caa3-4ee9-375b-a438-c07aa627afd9 | -20.24215 | -44.81654 | 2025-09-11 04:25:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25b71b07-76e9-3580-84be-e21efb53a3c0 | -19.45848 | -43.71449 | 2025-09-11 04:25:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90ac4f51-8dc7-31f8-8739-1f3f97fda118 | -14.90252 | -55.87626 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afeb0abe-3676-3ffc-a8b6-6aa47b2f5b64 | -17.4943 | -43.74602 | 2025-09-11 04:25:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66664264-98ee-3a0e-b1b5-348ad7e45302 | -15.13851 | -52.43145 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50c3ed90-d8f1-3650-80e1-ce6cd87988e0 | -16.55789 | -49.74418 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dfaea01-539e-3c12-b5f8-1a7c10d37c98 | -20.24717 | -43.57656 | 2025-09-11 04:25:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9db09581-7f3c-3576-be76-a95a414c6520 | -19.52456 | -44.68935 | 2025-09-11 04:25:00 | NPP-375D | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c93ae39-77df-3f45-97a0-039d55a2c890 | -17.25974 | -46.08717 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e18173cc-cf3b-3d7e-b8d1-c786471f33d1 | -20.70255 | -46.0787 | 2025-09-11 04:25:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c094773-9d5c-327b-8de3-5e272052470c | -15.16877 | -52.43185 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a01aa01c-ac5a-38c8-bcdf-c0f5fddcc14e | -15.01118 | -50.08915 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b03c64d-2a65-37f6-a9b8-1f6bf4548620 | -19.13977 | -43.0552 | 2025-09-11 04:25:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9ad98c25-254b-3730-9c46-edfe353a4e62 | -14.28827 | -54.74498 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5c03fe2-a663-3b14-9e6b-16a296e5f03d | -21.35421 | -44.22168 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b6a85f21-38bb-3d2c-89ec-14e5444e1f78 | -20.89153 | -48.30257 | 2025-09-11 04:25:00 | NPP-375D | VIRADOURO | SÃO PAULO | Brasil | 3556800 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a738b99-8442-31f0-a820-f4608ab9b191 | -17.24367 | -46.75579 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README81.md)
