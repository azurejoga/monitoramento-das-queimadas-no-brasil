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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e339b5-bc19-3136-81ab-472b508312b1 | -11.56432 | -47.75152 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4577d052-2a4d-3f7b-a3f2-cf30f730c372 | -6.55428 | -42.94009 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 285a5082-f186-38ab-8efd-d87d0ef7c746 | -10.80399 | -47.72501 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c9176e3-6c3c-3349-a2b2-abd3ef41ce04 | -11.90907 | -46.64075 | 2025-09-07 03:57:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f48823eb-ff1b-3d81-8d29-925e60c585eb | -10.31531 | -46.46858 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b1de848-027f-3855-a0a6-10c4b424e625 | -7.74785 | -48.82404 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d8a66ac-cc0f-3bf3-b607-cc96e1dbb8d1 | -13.05878 | -48.06139 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e6a9cf58-a4c0-315b-a158-2bc9f85a2654 | -13.03607 | -48.07062 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bdbe5c9-e03b-3c6b-99fd-005d355a7283 | -10.73261 | -48.59829 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 104e9c8e-c25a-3ffa-b219-f33af6fec967 | -8.68545 | -45.30766 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba1d5a73-4f45-3cb9-a18f-41f6fe725c37 | -7.71394 | -44.7154 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3a67531-4bd4-3835-adad-b4284fc46e35 | -8.50186 | -45.10473 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc7fc9c8-44d3-3a1d-9730-731793025ff8 | -11.80823 | -48.23841 | 2025-09-07 03:57:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 036567de-e20b-332f-b814-abd0486c67d1 | -7.0205 | -44.97163 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 551fc9fc-435c-3702-b623-67f6be6a4936 | -13.04412 | -48.05499 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f00333dc-9a11-349b-821a-930250cfafea | -9.1786 | -45.59809 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b7ca36a-df24-32b2-9109-505ddb1eae59 | -11.32134 | -46.55972 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1790e238-23f4-390a-942e-ceed98183fa0 | -10.38283 | -44.9629 | 2025-09-07 03:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1b65e775-7944-3722-8bd4-d71e20b7bbf2 | -10.1558 | -46.22178 | 2025-09-07 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb182f8d-3915-39e9-8105-cf845b87c17a | -9.97803 | -51.66743 | 2025-09-07 03:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1ca536f-e013-3bd6-9e43-e6275dce3713 | -6.7112 | -51.41879 | 2025-09-07 03:57:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9788d97-9bda-3256-9557-e66b7f34aab6 | -6.58791 | -43.9787 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39dddbe6-43bf-3c87-8c85-92f545cc34be | -7.71757 | -44.72021 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 450aa278-8446-3222-9713-8426eef5a138 | -8.2876 | -47.4363 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a11fd86-0ced-3bbd-a081-bf16788d5e3b | -8.91561 | -45.80865 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dc03f6c-4604-3343-88b3-c17d118e766f | -7.74857 | -48.82017 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 338cb1d0-d1f3-356a-9616-ad272c816019 | -6.52483 | -42.41892 | 2025-09-07 03:57:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35f4b6f6-7bd6-32d5-b7fa-bf4be295bc58 | -6.53233 | -42.92612 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fb48aa2-27ce-3838-9476-6bd32bd224bb | -6.55656 | -42.95074 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0265b166-43d9-396f-95c3-7e008445d3b6 | -7.40335 | -44.97754 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cbbb11a-a940-31fc-8b6b-394eb0cb05c0 | -8.67836 | -47.44886 | 2025-09-07 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4adf2f4-c7f1-39e8-a946-ba2ac0384a01 | -6.23284 | -43.29679 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90ba39a9-14d6-3f82-8564-32b1820ddcc3 | -6.7996 | -50.84875 | 2025-09-07 03:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2586825d-8017-313a-a847-d0410e6e75f3 | -7.00809 | -44.93756 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbaa308e-c3df-3750-ad54-bfd1b17ac5bd | -6.24331 | -43.50829 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc62ca67-9911-3db7-bb7b-6e96a4762722 | -5.97504 | -44.73874 | 2025-09-07 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a668eaac-13e6-35b6-b565-74067ce1e59e | -11.58698 | -47.17702 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a80ff1d-e42f-3910-abd5-bd8eef2fd9d4 | -5.95009 | -46.17867 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3de36e63-adf8-38e5-99eb-39d9bd6b84f9 | -11.85329 | -50.53067 | 2025-09-07 03:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50164d21-b814-340f-b03a-5d6f44b3e96a | -7.81193 | -45.43756 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dc1b52b-3eb9-37ba-92b9-233f8050bdb7 | -7.67169 | -47.33112 | 2025-09-07 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae4d0229-db9d-3ad8-8e2f-da45c77c6e2e | -7.84011 | -44.9227 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fad46dc-7d21-3c1c-a3a1-deef334feff6 | -11.59372 | -47.16713 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a62c9916-58d8-322d-8ed5-b06792cb3941 | -6.26967 | -43.50199 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0f7050c-157e-3ca6-9a4b-e73bd8a044be | -6.87844 | -45.55009 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2983989b-da73-38a7-8de6-cb5f7160adcc | -13.78874 | -43.16498 | 2025-09-07 03:57:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8ce67331-8403-3b2c-ba89-1c01d41d9707 | -11.39247 | -43.55706 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cfb9533-52a2-32d8-8734-70e32772bd8f | -6.19147 | -43.37388 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c07ea88-3ef5-35b2-9979-bff52301378a | -8.15132 | -44.86482 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f59a72cb-d8c1-3cc9-a4db-ce2785ee1a62 | -6.89615 | -45.59668 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22e50b0b-016b-32e7-9164-fc1d49d6acda | -7.72835 | -44.60777 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 526141bb-89a8-3773-a284-ebd2398fa2b9 | -11.40719 | -43.60831 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08ef32a2-ee7d-3ecb-a754-2e2426f8bc94 | -6.38389 | -42.99701 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 088c3742-5f66-3088-8e77-fe8bb9d925e5 | -11.31474 | -46.54361 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4274642d-728b-3cbb-af52-fcdabd6efec7 | -5.87075 | -46.05015 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c65a07b-2df0-3074-b55a-12fa8c5d8f1a | -5.86978 | -46.05571 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9d16e27-e953-3029-8b14-e943376c6dc4 | -8.68273 | -45.30984 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17a60ca8-13b6-36c1-a3dc-bf93e8b22e92 | -7.72925 | -50.30742 | 2025-09-07 03:57:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13d7118d-5746-3f7f-a8b5-0898a4b04bc3 | -6.20683 | -43.37599 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee62530a-12f1-3d4a-a9ee-2e578b5119be | -10.80286 | -47.73113 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7662ad08-eace-30c8-9808-66cda4de0e0d | -7.59057 | -44.69635 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d72f193-ee82-3660-af2c-e2a62a153288 | -6.19617 | -43.5873 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0b2bdfc-f47c-3b70-b726-1640f212ec55 | -11.01512 | -45.91279 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e928be10-b85f-36c8-815e-6d1bb5e6e49f | -13.00575 | -45.21124 | 2025-09-07 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b625b8b2-2dae-3979-97d2-0ea0a7ef0f53 | -6.19677 | -43.58376 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dba122f6-d203-3c0c-9ac8-58b14c4da444 | -6.30036 | -51.41842 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cf90afbe-d1e2-3c31-ac80-2a9fc4fee9a7 | -8.08486 | -44.80722 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67aa83d5-1022-3ba0-bf77-f433baa2cf17 | -7.81359 | -45.42817 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 86da907e-c9af-3d67-a1f9-b1dcfd462a37 | -6.7177 | -45.14721 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ce7fb4b-123e-36a7-aa4c-5d434cc06b85 | -7.53872 | -42.52362 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2582e2cd-e401-32ff-a523-47f9e082cefc | -6.23587 | -43.27895 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 261fb5af-a666-3c00-9024-96d580ee4e6f | -6.86513 | -44.25656 | 2025-09-07 03:57:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64d1abef-5cb9-3aa3-8a2b-59d6c45b6993 | -11.31673 | -46.55882 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41ac50b3-33e7-3d41-acb4-5351877a6e25 | -12.4668 | -48.03853 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71a185a4-6be1-3260-a0e1-bbf5e9c2f5a1 | -7.24486 | -39.17767 | 2025-09-07 03:57:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e7983f1b-9de8-32b6-a772-5b20ed34b351 | -11.00342 | -52.05677 | 2025-09-07 03:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 027c78a2-d69e-3cf8-bbad-8598caf02450 | -6.48891 | -44.00393 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0859e7bb-3a53-3c1e-a1d5-b4db21f455ca | -7.01912 | -44.9692 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 028176f3-1255-31da-95ff-70b12b35cf0c | -10.58446 | -48.47548 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4df1659-0fda-3275-a76b-dbe8cfba3281 | -10.34854 | -46.45649 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6cba33e6-14ba-3db5-9492-60af5db9a462 | -10.7415 | -46.33887 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f0fcce3-5a9f-3034-ab47-4d92a0fb50a3 | -7.61331 | -44.6737 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42018496-e054-3264-857e-2c2b42af4747 | -6.40231 | -42.98446 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8ae0e00-ff6f-38b2-a078-280d8f8f2dd6 | -11.5186 | -43.25083 | 2025-09-07 03:57:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 48f6fb77-85b1-37df-87d0-c1c4a3770f95 | -8.0892 | -44.80798 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 006ed428-445a-3a6c-808c-aa0850297536 | -10.35231 | -46.46227 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c0ca56df-b70d-3fb5-ba31-08c2c4d88cbd | -6.72656 | -50.46075 | 2025-09-07 03:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c90d0111-0af4-3eee-9685-b14a9fbaedd7 | -5.95027 | -46.18092 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8efdd059-bf6a-3984-a587-9c495b02118f | -13.04581 | -47.12268 | 2025-09-07 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 43b05aad-12f7-3df4-944e-c0ba6c7ec32f | -6.43357 | -43.61266 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cdcc49f-486a-30e5-9b0b-51812da8362a | -8.31194 | -44.97622 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c158d5d-3000-35c7-b244-bc6c699d2c6b | -7.00946 | -44.94461 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed042725-fc58-36d2-b076-a98aff0c11b0 | -8.48942 | -45.17783 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5612cf86-87b3-3413-b401-39dcefc7ebf5 | -11.31761 | -46.55399 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf4f9d0b-ff26-3485-809d-5d809c849727 | -11.14195 | -48.36874 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c88a200-c0e5-3fc7-8574-8fc82a1fba09 | -7.84224 | -44.93668 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e3da577-c2ea-3274-b61c-841e933fb734 | -10.15118 | -46.22097 | 2025-09-07 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bee18bea-3a6a-3117-ba14-7bfb7e1a699c | -6.19554 | -43.59101 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efd16609-b81f-3a8e-b3d3-b27c3989cca5 | -11.60042 | -47.15742 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e1ec9f6b-9a0c-31f7-adeb-da61731629b9 | -13.03433 | -48.05242 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README33.md)
