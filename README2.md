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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d18d8344-a022-33d4-850c-4e6310270849 | -9.4344 | -61.8347 | 2025-09-08 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 10883a65-63d0-3924-b84c-52eefc4f2844 | -9.173 | -59.3659 | 2025-09-08 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 41b10364-2ce2-3c2a-b1d0-ddc821343438 | -15.7576 | -53.5691 | 2025-09-08 00:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c122d2d3-a5a0-3da1-bfc4-8d6e7028f41e | -11.2831 | -46.4591 | 2025-09-08 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5c38c01e-cc8b-316f-a259-509cd8d2d8d4 | -6.4605 | -43.9532 | 2025-09-08 00:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 5e59641b-914d-3617-a7ad-939b9a3190db | -7.3984 | -61.6156 | 2025-09-08 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 00d504ef-90b6-3501-9237-583dcbc1aac6 | -7.4168 | -61.6339 | 2025-09-08 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| bb703f5d-87ba-396c-aa2e-a51699e65f2e | -11.2834 | -46.4365 | 2025-09-08 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 14f008b5-06b9-37fd-bdce-48b571f09099 | -6.6382 | -53.377 | 2025-09-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| c4357f98-2119-3769-9540-ccd4a2f3c407 | -6.6384 | -53.3566 | 2025-09-08 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| df0a403e-6e1c-37c3-b117-9c2cf9900374 | -9.481 | -60.4902 | 2025-09-08 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 0b60ce18-e745-3d71-854d-641223c1b27a | -7.3983 | -61.6346 | 2025-09-08 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 268.9 |
| 39fc3f36-d8a2-3710-b7f7-ea2c552aed19 | -11.3745 | -50.3997 | 2025-09-08 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d5ffe9a0-dec0-3e4e-b912-5b9bfe6807a3 | -12.9477 | -54.793 | 2025-09-08 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 89ddbb34-cb8d-3cb2-9c83-70a5185f1a4f | -7.3799 | -61.6353 | 2025-09-08 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8a6ccef8-0520-36d8-9104-f0a2258fc319 | -10.0495 | -59.3547 | 2025-09-08 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 68d48608-7c77-3b02-9df9-8c5230ce7f61 | -9.4345 | -61.8156 | 2025-09-08 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 3d8b7d45-3423-3964-8dc0-5cefdaeaf9a6 | -7.3982 | -61.6536 | 2025-09-08 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7788fc48-6452-3b3d-af1f-c8667bdaf207 | -6.3392 | -42.5919 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 43b50312-c73b-350a-a3a9-192311a7c28f | -11.3521 | -50.398998 | 2025-09-08 00:25:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4835ff25-636a-3a95-b82a-83c15c792cfa | -17.149 | -44.4436 | 2025-09-08 00:25:00 | METOP-C | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c635c189-fa02-3e40-a293-0a79270ce9f4 | -6.6494 | -43.848801 | 2025-09-08 00:25:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a33899fe-945b-3981-8bfe-4f78aa0942c9 | -8.157 | -43.181301 | 2025-09-08 00:25:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b34a2a1-6d4c-38ec-af09-534c614506e3 | -3.6966 | -39.635502 | 2025-09-08 00:25:00 | METOP-C | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 93c9533d-af7e-3e82-88f9-619f88c233df | -7.5628 | -44.010399 | 2025-09-08 00:25:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f07fca2b-492f-3a82-bc2a-5fe12e7e1912 | -6.8599 | -45.546799 | 2025-09-08 00:25:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72d2c4e2-31a8-3203-b003-a191d2b33919 | -6.456 | -43.9501 | 2025-09-08 00:25:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae3b506b-c6e9-3457-84f8-e1b35ed51efe | -11.6077 | -47.155998 | 2025-09-08 00:25:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5c1c949-a343-31aa-bc71-c0a76c697c1c | -17.2414 | -46.704601 | 2025-09-08 00:25:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4bec2110-2b72-38d5-a221-7b759bbb9b4a | -5.533 | -45.691101 | 2025-09-08 00:25:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cb896b5-3d6c-3cb3-9ba8-ce8a8f9dccc7 | -5.7732 | -45.660198 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7879d78c-7e4c-305a-9c4d-8ce37d86dc8c | -6.3005 | -42.2029 | 2025-09-08 00:25:00 | METOP-C | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d8f7076a-c65c-3d11-91c5-95dbc4de2cac | -9.1946 | -46.052299 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa5e1db9-646a-36e7-8da2-8a2e1dfa8ed9 | -9.1929 | -46.044498 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1835a33-c69f-3ed7-9681-0a32f8cc585a | -6.8425 | -44.831699 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5e54266-e116-311c-96cf-4c45587384ef | -6.4494 | -43.966 | 2025-09-08 00:25:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 646f5f46-c63c-31d7-9ea0-4df0570d2f30 | -17.827299 | -44.258301 | 2025-09-08 00:25:00 | METOP-C | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9e29f7-7cbf-31ac-b05b-e25dcc345230 | -7.5992 | -44.6698 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ce15fc57-703f-3c9b-9877-f3a72fac0002 | -8.0272 | -44.057499 | 2025-09-08 00:25:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9b79ea5f-a579-3740-a09d-fb4913ccaaf7 | -20.4515 | -43.982101 | 2025-09-08 00:25:00 | METOP-C | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 19bb97e5-767c-3440-9a25-9c2b095ed1ab | -12.9852 | -45.211201 | 2025-09-08 00:25:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38ec10e5-5c04-3068-92bf-cad63777b8b9 | -5.5325 | -43.790699 | 2025-09-08 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3441d797-7a51-3c1b-958c-a4b041426b4e | -3.6317 | -43.644699 | 2025-09-08 00:25:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84c69029-1f66-3d16-900f-1771a51f87d2 | -14.4866 | -48.816101 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b2a7e160-f91e-39cb-8d1d-c956808d3a5f | -5.8677 | -46.0327 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7967bfb-bf6c-3dec-bfff-ec81844123ba | -15.1445 | -47.982601 | 2025-09-08 00:25:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 890c8246-9361-3b4a-b822-4ab243ff8ea5 | -12.7953 | -47.999001 | 2025-09-08 00:25:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de2d6c7e-1c66-3830-ac74-6c972ae42776 | -19.1833 | -42.0886 | 2025-09-08 00:25:00 | METOP-C | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7cfc80d1-13a2-3882-9a57-c840ec3ab2d7 | -5.7435 | -45.3922 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 815b087f-aac2-30ef-b868-9906089004ea | -5.9282 | -45.753399 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6acfc46-537d-3b5e-84a7-394d096be7fc | -5.7929 | -45.6558 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 604b64b3-61c4-3894-bf81-88d27e3befb5 | -7.6324 | -47.9599 | 2025-09-08 00:25:00 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c431cd6e-6787-3256-9997-dd95d8a2e69f | -6.8554 | -47.9254 | 2025-09-08 00:25:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6da3f1d-3643-3eb2-8f52-586576b56d02 | -6.2012 | -43.6035 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c034a30f-94b3-3c86-a8ca-a00a7418dd25 | -6.6132 | -53.370201 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b01a58a2-3726-306a-8511-0678b9a760db | -9.1964 | -46.060101 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09741fb3-66d9-35b3-8fb6-611d44b7d60e | -11.1692 | -54.961201 | 2025-09-08 00:25:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b0c652a-2899-3dbd-bcbe-d83b980d80d1 | -5.7913 | -45.648701 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da4e6aba-7170-3053-a247-93fe13eeb53b | -6.3725 | -43.810398 | 2025-09-08 00:25:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f5be8a9-d789-34a7-ac39-1facf062421d | -5.8621 | -43.9687 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c6ea262-2c81-3328-ba33-9224ff533275 | -5.7029 | -43.903801 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe7b07e3-6169-377a-a284-459253ee4b2c | -11.5861 | -47.1507 | 2025-09-08 00:25:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68e4ced9-f4ef-39fb-ae35-cd0b67aa2ae0 | -6.2907 | -42.2052 | 2025-09-08 00:25:00 | METOP-C | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bba8f6ec-6bd0-3d7d-8f87-3b29c367b99e | -7.073 | -43.897301 | 2025-09-08 00:25:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f8718d23-009b-3854-bdd8-4b4ab9bad534 | -6.7957 | -52.795898 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec3bb0b8-985a-354a-b894-f9874b561241 | -14.9784 | -48.0168 | 2025-09-08 00:25:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff832260-bd08-39c7-9dad-799d767c48d4 | -17.567101 | -44.533699 | 2025-09-08 00:25:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7278744d-b571-33b4-8f18-b73a251b5f5c | -14.4592 | -48.780102 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 581ff248-c366-3d8f-ae9e-93bd5965346f | -13.0233 | -47.128799 | 2025-09-08 00:25:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1009afef-8d91-38b3-809e-8adce851b988 | -6.5992 | -53.351601 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88288a3e-44a7-39d2-90b2-2911165799f5 | -16.0641 | -43.634701 | 2025-09-08 00:25:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 996c35c5-9545-3163-8061-0d17a0155f4a | -7.0762 | -43.910999 | 2025-09-08 00:25:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 215f1465-898a-369f-932b-cc2942e16ecd | -6.3885 | -42.9837 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 696f50bb-6df9-31f6-b0d8-6efedd8e8eb4 | -7.811 | -45.4268 | 2025-09-08 00:25:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1fc850e7-67f7-3df0-bc7c-8684ac5838db | -9.167 | -46.066601 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ceb75865-6fd4-3126-a0e6-7af4e0d2a369 | -16.3204 | -43.062801 | 2025-09-08 00:25:00 | METOP-C | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 22dd0c65-f21f-3d7e-8ceb-8097fe19c59e | -7.0776 | -49.9277 | 2025-09-08 00:25:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db16ae95-f56a-3fc6-a53d-c8462965eca8 | -13.6278 | -43.8218 | 2025-09-08 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 878bc457-72c6-340a-8440-a2759e1321dd | -6.1798 | -43.3759 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f20f032b-f396-3241-afe1-4282f36d9d48 | -6.1847 | -41.002399 | 2025-09-08 00:25:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f1eeac8-2030-3e58-a457-1a7c57ad2633 | -6.4768 | -43.9958 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d44cbd90-1d85-35fe-ab89-979a4cf65fda | -5.4522 | -42.8167 | 2025-09-08 00:25:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 967ce768-cc70-3be6-a75c-efd48113ded5 | -6.6222 | -42.967499 | 2025-09-08 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 669a452f-6c0f-3c62-a836-98ac6fcdb39d | -5.4407 | -42.811798 | 2025-09-08 00:25:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 46de1060-f59c-3a3b-af93-560041203b22 | -5.7175 | -45.368401 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74b74f02-9034-394d-ad31-9f2ddafdd531 | -13.8103 | -43.857101 | 2025-09-08 00:25:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53cb2f89-14d6-3dff-8ec6-d3f0acaf3fb3 | -19.9559 | -44.311001 | 2025-09-08 00:25:00 | METOP-C | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8317a958-8dbb-399e-aaa5-b7bb64277f17 | -8.181 | -44.782398 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ead8a553-dae9-341c-868c-e7a997f4c547 | -6.5843 | -44.014801 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a3c0502-57be-3650-b627-00e6585c1aa1 | -6.2063 | -43.3116 | 2025-09-08 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d05a977a-075b-3a48-a4d3-f23d40130ff3 | -9.8285 | -48.8438 | 2025-09-08 00:25:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f239eab-bc19-3ee4-b723-ef63577ef129 | -19.385 | -44.52 | 2025-09-08 00:25:00 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dbd1589c-67ac-3aa1-ab0c-2a1ff7199926 | -7.5976 | -44.662899 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cdae3544-4fab-3052-b2f2-1d77a655f642 | -2.7666 | -49.613899 | 2025-09-08 00:25:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0dca74d-1d4f-3637-814d-cdfd07cd9a43 | -17.1507 | -44.451801 | 2025-09-08 00:25:00 | METOP-C | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 21c235be-a752-3bfd-aa45-57bcdd49c777 | -5.783 | -45.658001 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f7130e2-35eb-3e3b-8a08-f11a52e59838 | -9.5801 | -39.687901 | 2025-09-08 00:25:00 | METOP-C | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 19a27f2d-ea62-3f10-b43f-0852e71fa63d | -15.1421 | -47.9706 | 2025-09-08 00:25:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| abba5638-d789-36c1-9bd8-9224688c4d39 | -5.2019 | -43.698799 | 2025-09-08 00:25:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f360cd2b-7031-341d-b85f-e3c2ca946fe1 | -9.578 | -39.6791 | 2025-09-08 00:25:00 | METOP-C | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README3.md)
