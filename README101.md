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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 001725ea-b782-3165-b341-525c6d137a28 | -5.9185 | -45.839 | 2025-09-29 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 42cb2eb7-851b-3dff-9946-7d7350c9fcfe | -9.106 | -47.6275 | 2025-09-29 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f20dd252-785b-35f8-9570-c59d6848420d | -7.9628 | -47.3184 | 2025-09-29 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 2f8d3651-80a4-333a-9c8c-f5f800b52dc8 | -9.9581 | -43.5987 | 2025-09-29 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| cbcef8ba-86a2-308a-8048-deca9ae46c39 | -5.9004 | -43.6976 | 2025-09-29 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 22301b15-e2c2-3e6e-a84d-2f4f08247987 | -10.8238 | -45.407 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 63dcd9fb-8423-34cb-9123-eae4c6518100 | -7.6064 | -47.3278 | 2025-09-29 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 86921c6e-57c0-30d7-8451-c39657c1bb41 | -9.7451 | -47.8027 | 2025-09-29 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 6e351ba4-f6d6-338f-a83f-4823f6633500 | -9.7643 | -47.7786 | 2025-09-29 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| da505520-9f12-39b4-8406-c8767cb0d838 | -7.8375 | -46.7766 | 2025-09-29 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 9d4300e6-95ba-34d9-b6b8-e431c0f52a0e | -6.8268 | -44.8178 | 2025-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 4defd0f9-2abf-3342-950e-29efe6300d0b | -8.0034 | -47.0497 | 2025-09-29 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e796b278-24a6-318c-925e-9f87257b023f | -8.88 | -47.6282 | 2025-09-29 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 4a68e473-4185-364c-937a-0add9e76591c | -7.9008 | -44.5805 | 2025-09-29 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| eb13110f-9ac1-3ba3-a871-4fbfdfa30807 | -6.5163 | -54.8784 | 2025-09-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2d4b58d3-24d7-3f78-a7d7-52fb10332eab | -6.8259 | -44.9091 | 2025-09-29 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 1b5929e5-f4f6-3236-94b3-081656966f75 | -8.8988 | -47.6263 | 2025-09-29 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6316b42e-0ea2-367b-a6f4-26c266502b29 | -6.0623 | -42.466 | 2025-09-29 14:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 57dd93d0-c851-31f5-8fcf-171d3be31fae | -9.4194 | -54.697 | 2025-09-29 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 179.6 |
| f1780259-c088-366a-9b81-0b8e362c6246 | -6.4789 | -45.887 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 223.4 |
| a4585c4e-3697-3123-9f00-628019ead139 | -10.6429 | -48.5364 | 2025-09-29 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 7fba3376-6444-3090-89eb-b7c2258ae962 | -5.7679 | -43.8467 | 2025-09-29 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| c95b5e65-ed71-3a27-b489-ccc4e15be8e1 | -8.8061 | -50.7165 | 2025-09-29 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7165e7f4-c3e2-3b6a-9fac-132a4d92a399 | -6.619 | -44.9721 | 2025-09-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1dc7f0dd-8eef-3abe-a735-1112bef11cc9 | -7.4414 | -46.9888 | 2025-09-29 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| bc0ccf5e-b5be-3106-a2be-afca48871b97 | -11.4409 | -45.0229 | 2025-09-29 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ad74ed25-4637-3849-9bfd-56737a0d1661 | -8.7287 | -54.6454 | 2025-09-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 85e57d28-bc44-35f5-be90-cd52bb9c85fd | -6.9108 | -43.9834 | 2025-09-29 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4ea4ea0c-308a-3ff5-8c50-cd19dbab1be5 | -10.7478 | -45.3942 | 2025-09-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 19b21b0b-2d4a-3eb6-9277-5323b32818e3 | -13.2346 | -50.9691 | 2025-09-29 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 201.3 |
| cfc86ed4-8745-3cef-9e93-256df63fa595 | -0.1012 | -51.2945 | 2025-09-29 14:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 5ff4dc08-6dcb-3465-b142-c2cae841ff1a | -5.7294 | -43.9651 | 2025-09-29 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| efb48e98-2e8c-33f4-a6a8-5e4d456e8ad7 | -7.9816 | -47.3168 | 2025-09-29 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| ed900a14-18b5-3424-be73-ead5fc878204 | -8.2665 | -45.4791 | 2025-09-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| c20c2e5c-bc53-361c-9fb1-3ebabe6df088 | -8.1614 | -46.3899 | 2025-09-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d56c611a-54af-3b77-8450-1cbafdf38c52 | -6.5787 | -43.4089 | 2025-09-29 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 1df064c0-0352-36ec-b92b-a5c1df3d7044 | -23.2074 | -49.2138 | 2025-09-29 14:40:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 854c1468-8ad1-3968-9bcc-f548997f744a | -7.0481 | -45.1856 | 2025-09-29 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| df9b9714-ab70-3475-897f-60e2b5f62ec2 | -15.6127 | -46.2465 | 2025-09-29 14:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 96.0 |


