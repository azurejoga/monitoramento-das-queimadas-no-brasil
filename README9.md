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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1a2e441-0ce8-3ec2-9b0a-c487a5ab4dd8 | -5.51277 | -42.70555 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 97b93cc4-f5d3-3fb0-9db9-690d8baec58b | -9.84685 | -43.15892 | 2025-09-16 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 195b9a9b-1062-3177-8ce9-3f41e5b2c607 | -8.90981 | -46.15592 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b1f36b4-a8a9-3f9d-9289-c500f06dc440 | -11.70745 | -46.89125 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f433345b-7623-3d0e-a29f-e9f5433ff9c8 | -6.5989 | -42.56216 | 2025-09-16 04:02:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a91d55e8-81f3-370e-a52a-139b916c5d3f | -4.17748 | -48.57629 | 2025-09-16 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5f0d343-ad75-3d4d-b5fd-f48589d7855a | -7.03543 | -44.15052 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15811306-f163-3ffa-81c7-eeb83e75f317 | -5.80408 | -45.70143 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06b3db71-84a6-31c9-aea8-c576ef92636d | -7.42701 | -40.07878 | 2025-09-16 04:02:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5247ee0b-647e-313a-9de7-aa205af37f90 | -7.45916 | -46.14417 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3e9befa-a83e-353c-877b-46722b3f3060 | -6.34736 | -44.31237 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef59e5da-75bb-36ff-a7c9-e82e6e92186f | -8.58404 | -46.35495 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 805682af-4c1a-30d7-b8f8-cff3f77cf058 | -5.51631 | -42.70612 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 004df0ca-675e-3758-84b0-b97041d35150 | -8.136 | -43.65026 | 2025-09-16 04:02:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17001c4f-43d5-35d0-9ffc-9300d68049df | -8.12146 | -50.17056 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f17ceb3-14e2-330b-8ac8-b39320f082f3 | -8.09004 | -50.15626 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edd56b9a-e88c-3a7b-a3f2-fcaa1d3f699c | -8.41931 | -45.74432 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8d0d3e0-e1d6-396a-bedc-064335425875 | -8.96898 | -45.76075 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1314ccb-c213-3b23-b53f-a9aeada1d3d1 | -6.17236 | -46.81105 | 2025-09-16 04:02:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0cfb7e5-ef27-3e06-8f0a-729dc06b4a68 | -7.72919 | -45.29956 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2f0816d-e7e5-381f-9545-ed25e3a36b14 | -6.05689 | -43.55336 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9e5f4ad-708b-3686-b667-fde6dcf0189c | -8.87642 | -46.17658 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4925431a-b31e-39fa-8310-f8269cf18fc2 | -8.60583 | -46.40614 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 067157f1-4cd8-3731-ad7f-4bc21191a56b | -11.12557 | -45.33911 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ad1c1f5-0978-3188-ad80-6bbed04103e2 | -10.71879 | -44.76178 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2f5d4704-c865-3439-ba01-edb85efac08e | -5.81832 | -43.4963 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1bc6228-fafd-3f01-95f8-04583f7bda32 | -8.11381 | -48.26612 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24b8e600-9748-3359-9f59-f9bac935b2c1 | -8.97255 | -46.22469 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ffcd528-8bd9-32dc-bf0f-00074d5f63fc | -8.12207 | -50.16713 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 794b6702-68dd-322c-a8df-3ef0ea021f2b | -11.4466 | -46.93992 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 196d7ed0-59e5-31b7-847b-8ead84eacc4e | -8.12818 | -50.16782 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1590cd25-6974-3504-b441-8beb80db58e5 | -7.57201 | -49.84846 | 2025-09-16 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a86fcb6d-2c14-3851-b185-7d1ecd1d7fcc | -11.13235 | -45.34524 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3281780d-c75d-3385-8283-38ce9fd4262b | -9.1449 | -46.9514 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 981908fb-a310-3d11-a2fe-68da0e3b0444 | -12.05907 | -46.53914 | 2025-09-16 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6e5cc74-cb59-3bd1-a3bb-f799bc1a869a | -10.72858 | -44.74911 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e64715e-caaa-380f-8183-01ec91c8ab9a | -12.12002 | -44.81247 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fbb72e6-42c4-3ef3-9483-f34198de1372 | -7.42323 | -44.86493 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85172de7-1c83-3fda-b094-1e685d0055cf | -6.27493 | -44.00092 | 2025-09-16 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b089ca0a-d58b-30f1-8584-6033d4226949 | -8.12533 | -48.2572 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e0320e8-70d0-3dda-ab73-f6297450231b | -11.1182 | -45.31351 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8508b79-0fd5-32c1-9739-1ea777bb2069 | -7.16562 | -44.34958 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1742243b-efdc-3a47-85e8-f48ab6cac62d | -5.47631 | -45.34399 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73eaa032-af61-359e-9176-5e1e18039e0c | -8.41916 | -47.21655 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aff2b105-3c45-3125-8b11-016c4ac02eea | -8.91278 | -45.52319 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36fbe697-ae3a-3063-8eca-e10b5e00ef6d | -7.04896 | -44.16194 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb988cd3-bf13-3e55-839b-9a6d3c90ffff | -5.78629 | -43.94584 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5ff55e8f-42ca-3251-acbb-99045ea21fe2 | -8.97604 | -46.2292 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf1feefd-31af-3a18-9004-b23c91491568 | -7.04905 | -44.11502 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8bb2135-874f-3d53-bab4-d652d7ae69a0 | -11.46342 | -43.56415 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0c7dd7c-b193-3e0a-96c6-f9dfd14736eb | -5.80907 | -43.48688 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c66c7b62-8498-37ad-8923-a75046f45024 | -10.6457 | -46.47198 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5127c2ab-2443-31f5-806f-1ef9e52475c8 | -7.67913 | -46.30768 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f077a41-63f2-3f89-b49e-0a85ddf510b1 | -7.71244 | -49.55841 | 2025-09-16 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82d7a01f-ff55-3fca-8045-fe92a9c4f9fb | -5.78142 | -45.94 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82745f88-3030-331a-8acd-8d1c4a0f0885 | -8.59992 | -46.34069 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac61c6cc-c69a-3e9c-9378-8d287245b813 | -7.2096 | -44.38816 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33085c56-a02f-3653-8676-8780bc16aa42 | -11.11496 | -45.33249 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d1bf9af-a66d-32ba-8ed8-8365c6c9cffd | -5.19355 | -45.13303 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fa60630-0d97-35b0-b594-f81ad068ae39 | -10.20905 | -42.54763 | 2025-09-16 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b51acbf0-b942-3de8-a558-a956efc518e3 | -7.05952 | -44.16812 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1321396e-04e4-3843-9c2b-689116def49e | -10.73072 | -44.75884 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4501b39f-c642-3053-b5fc-32d9fefdfe0d | -5.66729 | -43.31894 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 114c434b-60d9-369c-ba74-669ca8614089 | -11.9085 | -46.74791 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdfa63b2-175a-31df-ad5a-ebcef396b43b | -8.4205 | -44.97958 | 2025-09-16 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0ed8e00-f498-3d74-9c5c-96a0000b44be | -11.27826 | -50.79838 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6060f695-0ed1-31e0-aa49-0d371552e203 | -6.66429 | -45.54033 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0538ace-63db-35d2-88d6-4001a2d87543 | -5.8577 | -43.71988 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2843000-67a5-32f0-b063-993fcdd862e7 | -6.4657 | -46.00698 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf9032b4-4771-32fd-b169-9a2b2e3714fc | -5.79345 | -45.92085 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efc6576f-7675-389d-966d-2758a3c24099 | -8.10145 | -50.15581 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4bc3c02-d4f7-3bbf-879f-b94e50999202 | -6.96659 | -44.45168 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49e552d2-7b82-3397-9511-bdf3d8fca8a1 | -7.26002 | -39.31484 | 2025-09-16 04:02:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ada0af5-81e7-3dc1-ab77-9b0c4136ddde | -11.43714 | -46.93856 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d871bafa-35e5-38e2-8ae9-4e87401706f9 | -10.73151 | -44.7542 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 487f6a67-4eb3-3bde-b48f-6ff951edca62 | -7.59632 | -42.2562 | 2025-09-16 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a08843d-3e35-30a0-8d1c-c33822e90b86 | -10.76864 | -44.71454 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21cffec9-6aae-32be-b73d-f582587695c1 | -10.71482 | -46.48798 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b7ba5550-b21c-3558-91c5-37e1cf8627f4 | -6.61947 | -44.07959 | 2025-09-16 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fa19860-4b0a-3b6b-a665-14daf26228ac | -12.10325 | -44.82317 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4f1bc4d-d9ca-30ed-9c82-68e6564c2847 | -7.27842 | -46.61336 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05ca025e-dada-3ed2-9dd0-14131441893e | -5.81205 | -43.49185 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 541df233-a70c-3b53-8da7-cc42a961ba05 | -10.72621 | -44.76294 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dd367394-56fb-3bc0-bf37-8007678556fe | -12.17693 | -44.09735 | 2025-09-16 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 518dfa22-792f-3b82-8a91-166e1a136ae6 | -12.10763 | -44.81938 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 945d0575-126b-338f-a36e-a49432d36d5e | -9.73271 | -46.04118 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46a065bb-d185-3450-a861-09ad1b3e6562 | -12.12438 | -44.80875 | 2025-09-16 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32fb5e01-1168-3bcf-845a-711e80e10785 | -7.66194 | -45.14933 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4933ad39-00de-3cfb-9551-c876972b118e | -5.80874 | -43.48579 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ae34b981-e1f7-30b8-87dc-8bb8cdf3fcfd | -7.08615 | -44.5453 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2304e171-00c1-3e21-953f-c4198c35f04b | -5.77902 | -45.90194 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7334d5da-886c-360f-844a-530f29861a49 | -8.11958 | -48.26163 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03a9b33c-ac57-3c59-aa0f-bea95d44be27 | -11.05406 | -43.29994 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d7fd25a3-4425-3025-ace3-6541750423f9 | -5.778 | -43.92555 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c53662d-b2f6-32db-a715-fadf26161781 | -6.22508 | -43.90119 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fd81919-2a1d-3205-a030-39df257a6d06 | -7.67123 | -46.30257 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c838fa92-206c-3f00-be27-46118186e2b5 | -5.14111 | -42.85443 | 2025-09-16 04:02:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e78ba600-df46-3fd5-b7df-db56a66d6ba4 | -12.1776 | -44.09333 | 2025-09-16 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5798353-5116-3c6b-8e7b-2c111b97b594 | -11.1174 | -45.31821 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 304babb6-40c0-3fa0-aaf7-a6e5680aaeca | -8.92148 | -38.62833 | 2025-09-16 04:02:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README10.md)
