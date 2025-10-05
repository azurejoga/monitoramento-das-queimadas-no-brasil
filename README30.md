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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15d89811-e531-3dc9-81dd-e7e31dba4bc2 | -8.11664 | -44.10194 | 2025-10-05 03:34:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77f5b4f4-dd5a-37d5-9bfe-577214705faf | -9.57674 | -46.1277 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1cb1a36e-4492-365c-8b2d-17f5f9a74cff | -8.89914 | -46.68156 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29a97160-69f4-3c54-9419-acdab51b1e5a | -7.78793 | -42.59636 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dac3e0c4-2c22-3cd4-be10-3a202ba80266 | -11.43287 | -43.48812 | 2025-10-05 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15e2a9f8-84fc-3cb0-92a7-46efbd39ef80 | -12.46822 | -45.52843 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8f0879b5-3f1c-3899-b945-9a2af1de03ad | -10.93586 | -47.09539 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 648873ee-aad3-3b6a-a9c0-d1d58fabb7ce | -13.27446 | -47.1829 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7de439de-dcd9-3a3d-800e-927ce1f7dd83 | -11.81669 | -45.08551 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77a68677-42bb-36db-9490-2ef0c41943eb | -8.58765 | -46.32656 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| fd74c545-1cce-39ab-8d28-90fd0a775f81 | -11.89984 | -44.99401 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5813f68f-8ae8-3226-836f-60f75312f9a1 | -13.59659 | -48.16792 | 2025-10-05 03:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfb482b3-72ef-3860-acea-931dd76009a4 | -10.94242 | -47.08135 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 170.0 |
| a46cdeed-dabe-3e00-a567-e296b757b4b5 | -11.81096 | -46.85462 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f7db7b0-c6b5-3a3e-908e-275b0a5b4e2c | -13.85919 | -43.99474 | 2025-10-05 03:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d5c80c5-243a-3866-be52-bf26ba49bb6f | -11.81816 | -45.05841 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9caa32ac-f3e4-3339-ad46-63c77c340d3d | -7.6885 | -42.58776 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 33557094-1f75-3686-9d41-d812dff5cebc | -10.9439 | -47.07438 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 052b96f9-75b4-318b-807d-2895342c7bd7 | -12.98347 | -46.8433 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f1ebaf4-a46f-3c9d-85e1-91d6f4f13cbd | -13.30642 | -48.12775 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d74f661-da14-37af-85fa-96220369dc4f | -13.10308 | -47.87466 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 38bf6a02-9fc3-3795-9040-2f8f0bf4229e | -11.02024 | -46.68636 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 03bacc82-9c47-3bbe-9c48-b4dcb7ea6c69 | -11.82578 | -45.07277 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57c7d531-605e-3181-b272-0c75913e8ada | -7.74159 | -42.52691 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd82b373-2dbf-3f78-83e0-6ea33839c642 | -8.55456 | -46.36567 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a9cb679-e0f9-3ce3-b217-7f7a2e533075 | -11.49146 | -46.78642 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fd5a445-2f7b-33ef-bb98-17a1c8c94651 | -13.10497 | -47.83189 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61683dbb-2cf9-3de2-9da1-d8404dd89716 | -7.79863 | -42.5696 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f177e74d-c75c-3d1e-b8b4-59de79ca1726 | -8.57352 | -46.32393 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 0292a51a-9121-377e-b1a8-7e8ddd28272a | -11.00838 | -45.59412 | 2025-10-05 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 629f635f-60aa-37b5-90d3-37d58fdb03da | -7.15852 | -46.0854 | 2025-10-05 03:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2bfa8eaf-f3dc-3831-93a4-c24429b3e4bc | -8.63261 | -44.90581 | 2025-10-05 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0988bede-1530-30f1-a0eb-a4188ac7d9ee | -7.48316 | -43.03122 | 2025-10-05 03:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 88fc8497-a322-35e4-bd22-c3d4965a5dbe | -13.15341 | -47.9529 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa4a62b9-a50b-3d6d-8ded-27ebd37f6c8e | -8.58095 | -46.30734 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 48558890-aa49-32fe-be47-794ff424684f | -13.27386 | -47.61606 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69862066-71b8-35ea-be6a-e2066ec4d664 | -8.16872 | -43.34848 | 2025-10-05 03:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e921522d-52e1-3c22-a956-9a98e41ee3fb | -9.30047 | -45.98052 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 845a4d81-a830-32fe-a892-ced7541ce133 | -10.4016 | -45.41937 | 2025-10-05 03:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d5c0d524-1a89-32fd-b56c-3f704f7f09e2 | -7.68939 | -42.58587 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d847edde-71b6-383c-b9e7-51c52549d0cd | -7.31853 | -45.99459 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d6f0d40-95b9-3554-9084-e76f6a60b6f1 | -13.30405 | -47.78363 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f93f802-5f0a-3c95-bf94-d3cd9dc75d8f | -7.24897 | -44.89792 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afb4733f-82b0-3150-a90d-e169fa24e810 | -8.57215 | -46.33097 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 567d1c82-9d68-3539-a401-9dc0d631125d | -10.99645 | -46.52752 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 409d62c0-d3b5-3743-b688-7a7ec8edd801 | -12.46091 | -45.532 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2c994ecc-e56c-3272-9b3b-b7d9e55fa488 | -8.54496 | -46.28288 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a9c70bb9-f05d-37f9-b343-af8ffbcb40fd | -8.56437 | -46.35342 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66623cca-6391-3866-9b9c-0dbf2fc0959b | -7.51711 | -41.27541 | 2025-10-05 03:34:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e1c22d8d-dc49-3023-a60d-760321d68d40 | -12.8213 | -46.86486 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9df41cdc-00cc-3a2b-bdf3-fa69b2256b6b | -11.50237 | -44.9828 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdf00177-058f-34d3-b9e4-b2d06ad7da51 | -7.72898 | -46.27588 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 119093b1-b85a-31b7-84d5-022bce39f434 | -13.28966 | -47.57693 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 17fc5b1a-4d4b-3813-867b-37fd4a77595f | -13.72774 | -48.08442 | 2025-10-05 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8071f9c9-a61a-335c-9033-8e1467f0cd22 | -11.75573 | -44.73677 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 405f35fd-36f1-3a49-bfee-f0c02af10867 | -12.45773 | -45.52351 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 40ae7b23-414e-3f0d-a6e3-9724bdb3fa52 | -13.43885 | -47.27995 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8a793e9-e6b1-3bb0-a491-5bf396409b47 | -13.33822 | -48.05957 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dca89da9-0372-3e1f-9012-9154d796b2dc | -8.16283 | -43.34703 | 2025-10-05 03:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1cd3a636-971b-3f33-8b17-60c1dbf53f8c | -12.45755 | -44.64197 | 2025-10-05 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca7868e2-ed36-3abd-8992-0b2157784894 | -7.25002 | -44.89226 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e8cca09-afa3-307c-9fbc-7c6c27981937 | -13.7393 | -48.07875 | 2025-10-05 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d33c5a35-a01d-3875-b37c-595de3c71ac8 | -13.32802 | -47.56858 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6460acd6-b19c-30cb-8963-4a2983c73022 | -11.8172 | -45.05156 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07079b69-7add-38f0-95f0-e05937ea9815 | -8.55984 | -46.26687 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3cfffef9-6f2a-3285-a486-d3c8ccde1bc0 | -11.83196 | -45.05405 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a517f3c-6fd3-35c1-a416-bab1d12736b9 | -8.59922 | -46.28905 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8d9bab16-b9e4-3fee-823e-12ebea7354fe | -13.31206 | -47.1743 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b42360a-509c-3a21-8abe-98b4a332988f | -11.76183 | -44.73803 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 62907bad-7994-3ad6-a53b-2bf9c103ef72 | -13.38115 | -47.5455 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e3aa5e9-c67d-3642-bb4e-c6f206624b62 | -12.45465 | -45.5304 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 30679b14-b5f1-3b3e-a65a-9a1dbef36284 | -11.01756 | -46.69939 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b8926b3e-3697-34c9-846a-abbec9d6bdae | -7.48052 | -43.03337 | 2025-10-05 03:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c720b0c9-85f3-3ae7-9782-02e02525fa89 | -8.57963 | -46.3139 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| be1a19f8-a657-3a43-9faf-e313d2dd403c | -11.67557 | -43.89811 | 2025-10-05 03:34:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0d66add-e773-366c-81f0-b899f784e13a | -7.78089 | -42.60822 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f8cfeb5e-137c-3502-92e6-98d0a6313dfe | -11.90613 | -46.23453 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6b815ad-9e43-338a-a9b3-fc2ee10d478a | -13.29154 | -47.58711 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5cb910f2-c365-3090-b385-695f0158b1e3 | -13.30654 | -48.10034 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8fad6e7e-570b-3bc6-bbad-08a4e1fd43ef | -8.18387 | -44.14271 | 2025-10-05 03:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a5d7d5a-6be3-349e-801c-29efc7a7798d | -7.78629 | -44.54716 | 2025-10-05 03:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 147d8a31-ebaf-39ce-a377-e08246d9e5e0 | -13.35293 | -47.58875 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74580b4b-3fe3-3636-a9c4-776a434cd994 | -10.19119 | -45.53893 | 2025-10-05 03:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3aed05c6-f93e-3b8e-9983-e2a9d557fad2 | -7.43764 | -46.51751 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0f75a87-2b32-3e79-810d-0112c8947f74 | -12.47027 | -45.52652 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e24e37e8-551c-33db-b94e-35e176c847fd | -11.91526 | -46.24387 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f58c926-2270-355a-a361-40d61050e795 | -13.74191 | -48.06718 | 2025-10-05 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84f351cc-e49b-3249-afc7-cd7223cb9d3f | -13.34775 | -47.57869 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18bbae1f-2cd0-350b-bc84-d5e59c0aaa0c | -9.25318 | -46.77673 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ee922a5-3d53-358d-8959-9a888a9cfcaa | -13.51455 | -47.2937 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74098440-7dcf-3fc5-9812-353c6276db7b | -7.79793 | -42.57351 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e27dcf5b-4f33-39ea-a82c-a411781b3c53 | -12.4566 | -44.64074 | 2025-10-05 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81f9f4fe-d177-3df4-bb5e-e6fdbb74b9e6 | -12.81572 | -46.85776 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 12cb11eb-f897-3a0e-9733-a568a8343ae9 | -7.72344 | -42.39217 | 2025-10-05 03:34:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0330abfb-8b16-315f-89b7-bd110891e258 | -8.63729 | -44.9122 | 2025-10-05 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c96fbf56-95d8-37ec-8e67-c12837f000de | -8.55717 | -46.37036 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4829c02f-abc4-3291-842d-0003a646f759 | -8.59782 | -46.29608 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 74dc2fec-959f-3c19-bb94-bd2830cbf1f2 | -8.85724 | -46.10575 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5fb3762-b7d7-3aae-9715-6597c0ca7aa3 | -11.82762 | -45.07594 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 00d598ee-a20b-391a-94c3-14a528482924 | -10.64259 | -46.34106 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README31.md)
