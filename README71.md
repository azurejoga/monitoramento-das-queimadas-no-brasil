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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47d1b568-34fb-3214-aa68-4d0c704b27db | -3.55492 | -43.57719 | 2024-11-09 04:55:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3fed2a39-b71f-31fe-bcac-280f86557279 | -2.51646 | -47.57837 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 743e4efa-28db-3896-a05e-1e2207e32e5c | -2.87608 | -51.467 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3647d00-490a-3632-96ab-54ea56952e8f | -2.91843 | -51.04007 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2800ffca-8803-3f56-a2fe-f2282f3611be | -2.92759 | -48.67014 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28b3f538-a4d5-3f4c-b5c4-d7c04d9c8a44 | -4.81407 | -50.60083 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba15de52-a496-3a02-95a3-f72638f6f448 | -1.88075 | -52.17702 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eba9d2f0-739b-39f0-9441-dfd049349207 | -3.83461 | -50.04289 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 44a274d7-a33d-370c-870d-a6cd41c53459 | -2.88776 | -49.38067 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4fbb3b1f-85b8-3c14-bf5f-943f612e3a10 | -6.18426 | -45.44488 | 2024-11-09 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9533d366-8cf2-360f-bd33-93fc8b05f3eb | -1.44555 | -52.68496 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1af07e3-769c-389e-a210-274909d04f7e | -2.50864 | -47.46589 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8783ccbd-b4e1-3cd5-85d6-9bb245b89065 | -2.28155 | -53.82333 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6120b065-1e8d-32ed-b45d-765943083e95 | -3.53682 | -49.99344 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c662e74c-21b1-389a-84a6-63941aa3ad12 | -3.18617 | -54.31194 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5aa8dbc-435c-3a0a-9804-b55af879a528 | -2.56734 | -48.25984 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dbc81f8-b7f5-313d-8a3f-ea487576b969 | -5.44227 | -43.26886 | 2024-11-09 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b73292c7-d41a-3ad7-8c92-5daf1e0c1155 | -3.18135 | -50.38889 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 528ba50c-ae06-3f78-8852-9fa40a5a0285 | -4.77855 | -48.68213 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aa456f4-5f0d-34f5-8891-930de8a436fd | -2.27914 | -48.73065 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e3c9956-6b26-3628-b91b-f813d30cfea7 | -3.35672 | -50.1208 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44218b5a-5eb3-33ce-91ae-b9c1c37da36a | -2.0858 | -46.5163 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 578164ea-5ece-3654-9db6-41a7b63760f8 | -2.07466 | -53.5668 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1165c181-5be9-3ed8-a370-8c3a62798b39 | -3.96911 | -48.16897 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dec9a88-cf71-35f5-be17-8ae2631a0dbf | -3.39097 | -50.80816 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 235f84df-cc49-3ad9-9838-f3672ea271c1 | -3.95172 | -48.14344 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe55f380-995b-3a05-b40d-e0bfabbcf3c5 | -3.02024 | -51.19553 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72a31dac-8a8b-30af-8ab4-502c4795ba25 | -6.5522 | -44.49432 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf3b343b-d780-32b3-9b82-4d5d498a928b | -2.94063 | -54.10507 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1549779-8019-31cd-b272-7bcd03d2e882 | -2.09133 | -46.48037 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff593a31-693c-3b1e-a40c-932aca79bfd1 | -3.21557 | -50.38157 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b92f2f95-7e5e-3b70-bed7-ebfdb5ffc4e5 | -2.93751 | -51.05473 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5d28110-1189-3e04-95dd-9043d2d1b8a1 | -2.58512 | -53.98156 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ad751ab-e7e8-33e0-8162-1b6980ce815f | -3.15922 | -51.12209 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb9fe520-c159-382d-af3a-7718b3e0dfae | -2.15809 | -46.68822 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3366cfee-73a4-3be1-91c5-3714bec90b80 | -2.51469 | -46.30852 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efd7a7f9-ea54-3ba3-84c7-53359b0f5e8c | -2.93905 | -51.05493 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61810ca9-10fd-315a-9490-4c70173e6f94 | -1.18596 | -53.66597 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0933809d-ef8d-35fb-a469-58f290ada88c | -2.43089 | -50.51588 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2636f923-a7bc-3d54-9ae6-b0bb7563d75f | -4.26852 | -46.91469 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dea2ae40-2a00-3144-8de9-433181d92ce4 | -3.19036 | -54.31929 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eea7e1c5-8862-3cf2-bbaf-8bd4a5f9b873 | -1.36362 | -51.40257 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d34b1b21-2823-3f0e-8d09-05aca4e792a4 | -3.24363 | -50.27202 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac979555-e949-3dfb-be47-1e7ad1043f62 | -1.77831 | -52.35053 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e45c3eb-34de-330a-81f7-d08b619f7b31 | -2.25805 | -48.8414 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60561a2f-7dba-3113-87f5-7e13c4c4ab10 | -3.83627 | -49.95891 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91bc7489-30ac-3f11-b52b-544802771f4a | -2.36412 | -54.74621 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f08146e-8f5f-3e80-aa22-1e2a513cb222 | -1.35906 | -47.31681 | 2024-11-09 04:55:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ec81c79-856c-3e23-a404-ce279b22e3a5 | -1.48825 | -51.74454 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 88c126ad-025b-3355-a681-71f6535d8aab | -4.08799 | -48.5098 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9421a4e7-9a39-36d1-bff4-6f51dfd60db7 | -0.39068 | -51.94582 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 696ed1f8-63c5-31f8-a13e-3ad3d4e5f5fc | -3.03041 | -51.52808 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a0e09ba-6c5d-309b-b65b-337bad72c671 | -1.94764 | -52.89033 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d64e3bb5-2eba-343d-bf0a-7544355d9651 | -2.94036 | -54.4544 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d636ea9a-9492-3377-804a-1094ad85eb02 | -1.14651 | -53.65631 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2faceb6f-d664-37ca-baf7-52327598d3ca | -4.53459 | -50.35706 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ec1e853-c64a-31c4-8b9a-0431cda0f948 | -1.67903 | -48.73033 | 2024-11-09 04:55:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 766d09aa-e6fc-318b-83c9-c63b0a0ca596 | -2.71298 | -47.73184 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9cd29b4-cc54-307f-9429-db1008f6a172 | -2.6935 | -51.6974 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86de6ea0-b127-364c-a100-c033937f5e98 | -1.83175 | -55.19699 | 2024-11-09 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c6f26b7c-8024-3e3a-aca7-d8d164113680 | -3.01018 | -53.42775 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d085b5fa-cfd4-384b-bc9e-91abe5161a7c | -3.54785 | -43.56978 | 2024-11-09 04:55:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a626d827-1a12-37b2-97bf-050870bb46d4 | -4.61575 | -45.98138 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63590ae8-374d-35aa-8bea-5f0e0d84a5e7 | -3.89081 | -52.38972 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8534a184-196a-32bb-9ebb-1eeaa41d20a4 | -4.438 | -43.64064 | 2024-11-09 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b00624cd-f247-35bd-91bb-747ac7bbded0 | -2.18445 | -51.74114 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06785434-7e44-3090-8f86-08e5c696f5bb | -3.90137 | -51.92131 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff3069c7-c068-3833-964b-63c0f546d0aa | -2.58459 | -49.12613 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50c088cb-48de-3c7b-a5aa-c47547fb731b | -4.06634 | -50.01625 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b8b89c8-c4e4-396b-a886-a7c03dc29d2d | -1.24327 | -51.77198 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f342e96a-02c7-3040-b684-1ec2398fa801 | -2.92131 | -51.04443 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05207c64-abbe-3ccf-9003-fcdd4da624ef | -2.8527 | -54.10509 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0149675-3181-37df-8551-6564470ee517 | -2.36898 | -46.86394 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65a0ee04-bf03-3c73-ac31-b496c4bb5f40 | -3.03128 | -53.27216 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcfcd862-8afd-3147-be82-2ef52e66783e | -2.43108 | -48.60015 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a52b473a-425f-3ff5-97ba-a2b612b26baa | -3.8246 | -52.16451 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5593515f-86e0-31a1-993b-c46504b0ad1a | -3.30453 | -52.50115 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 876e7aad-2e0f-3dcd-b11d-d28b98f3726e | -3.95277 | -48.99335 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff00ee60-14cf-3f64-9c12-19596efd5edb | -1.23264 | -51.77395 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2a235b6-fd35-334a-8a9d-bf04220fdfd2 | -3.04732 | -53.27818 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f01cbe2b-1119-3a79-becf-217771d3be5e | -2.18116 | -48.33852 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e8fa252-cb4d-394b-8757-5c01c8d53b65 | -2.31027 | -48.31639 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e971e65-6030-3aaa-9527-e05a603dafca | -3.58635 | -50.2737 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b5919ed-2fe5-3b48-ba0e-dc52494bc41d | -2.61517 | -51.74852 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb39ec0e-d886-3c23-b2a5-7d03ad6f0504 | -4.60776 | -49.57553 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a818085d-a6c1-32e6-a4e5-32285cd232bd | -2.87167 | -50.31997 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6fee0f0-0536-31ad-9ccd-68973b2b2163 | -4.13887 | -46.90734 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50e1d9cd-4f10-3bb2-92d9-e31beed44607 | -5.44287 | -43.2646 | 2024-11-09 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7cd28c1b-3fcb-3d31-abc1-c9513a332761 | -0.04408 | -50.8028 | 2024-11-09 04:55:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30dc0da3-5cf3-34d4-8051-16158fa124f2 | -2.61612 | -51.74833 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de669a1f-d39a-38f5-9659-fe266f497507 | -2.69237 | -51.70463 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae53f8ab-f503-31b7-b34f-7998f8a3952d | -4.03851 | -48.28489 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b90f6420-0a18-375d-a198-c01f64ff94a4 | -2.06559 | -53.27907 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55ef9323-4fe3-38b2-a65c-1b05302f96b9 | -3.91083 | -47.95626 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb864dce-2580-3c28-bc48-dedb5e9a79c6 | -2.7365 | -51.89153 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 018620f0-f18c-35ad-b9a7-e83a57dd4ba0 | -1.48585 | -51.5834 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50e3bc7a-1aae-336e-96db-f07e0d760db6 | -3.17882 | -50.59531 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3567da01-6118-3d3d-a711-17d236951cae | -1.36895 | -49.35505 | 2024-11-09 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b78f3ac-7de2-3005-99eb-3825df21bfc6 | -2.43443 | -50.51643 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5559cb35-bbbf-3413-b751-f198e37ffa13 | -3.08886 | -51.22065 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README72.md)
