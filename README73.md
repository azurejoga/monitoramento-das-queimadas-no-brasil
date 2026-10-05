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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb991012-92ce-35cc-964c-6897b0a803b7 | -6.69321 | -45.23143 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c1b01407-9fcc-3940-84be-cfc1c9e06d16 | -7.0951 | -42.54618 | 2026-10-05 15:54:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 53a1149f-d889-3a1e-b75a-84037b0c2fe5 | -6.6805 | -45.22511 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 5bbcc724-e279-39a1-b474-147dadac60a6 | -7.09432 | -42.5406 | 2026-10-05 15:54:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 501e947e-c8ef-3864-9e3f-b0114535509c | -6.93038 | -43.67601 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 60a78aa8-32b2-30c4-bf89-d8c88066bd25 | -7.65567 | -44.3748 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 32c4fdd9-f799-3072-95dc-bf46dc553b3f | -9.04038 | -45.14807 | 2026-10-05 15:54:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 3d8884ee-8776-3628-bfe1-1e60efa3e73a | -7.82799 | -45.32601 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a836fb69-c823-3d46-ac38-b90373c727a2 | -6.92556 | -43.68001 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 131bfeb2-75c2-3d36-a6f7-6ecc30f01832 | -8.4333 | -39.54776 | 2026-10-05 15:54:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ab02ca50-c303-39ec-b179-c5d52da270b5 | -6.42052 | -43.46871 | 2026-10-05 15:54:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7791ce36-c1e3-3733-be67-d2f74b82b650 | -6.59887 | -41.57756 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| c9e05611-1627-368b-b69b-56f7fdf8fec7 | -6.33603 | -42.56523 | 2026-10-05 15:54:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 3885a9fa-a9ad-3eb9-97b4-4126e92e265f | -6.68685 | -45.22822 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d71cf59c-4529-3109-aea6-98e0a7564034 | -7.38014 | -34.94413 | 2026-10-05 15:54:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d412dc1c-e547-3741-9e00-75d5bdbb0b83 | -5.98903 | -40.91523 | 2026-10-05 15:54:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| d7b4ee42-0a51-3581-973f-77ed3b885b40 | -7.18617 | -42.00523 | 2026-10-05 15:54:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 0cd545ff-d61b-3918-9a9e-533e2791150d | -6.3312 | -42.56598 | 2026-10-05 15:54:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 4c90c846-28d7-3802-a7b2-a43beeb05b60 | -7.53686 | -45.40098 | 2026-10-05 15:54:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a169b934-24b9-3040-a526-08f2d4af7a12 | -8.37298 | -36.17216 | 2026-10-05 15:54:00 | NOAA-20 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8869baa3-2a23-305b-a6f1-b39e4954d846 | -7.17535 | -41.99635 | 2026-10-05 15:54:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a86df937-4d8e-340c-b9c1-bc6507021153 | -6.42009 | -43.46558 | 2026-10-05 15:54:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d67ac937-6dd6-3956-8f13-4b929a2d627e | -7.52681 | -44.87397 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe01d3cf-5416-3a82-93a2-526c75b3039f | -6.33044 | -42.56055 | 2026-10-05 15:54:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| aab67d82-bc91-34bc-a6aa-8f6785a7b05d | -8.30738 | -39.15211 | 2026-10-05 15:54:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 16.3 |
| d237f8d0-8d92-34bb-bc13-fa546893f08d | -7.17135 | -42.00229 | 2026-10-05 15:54:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 528533dd-dbf3-3850-a946-4c157d675e39 | -6.60865 | -37.89139 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 252d1660-275e-3bb3-8de7-b7371d3bb3fb | -6.90751 | -43.66592 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c04a4e30-543e-3b36-a4fd-5b49910c84d6 | -9.159 | -45.12833 | 2026-10-05 15:54:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1103cc4c-8bbf-394b-a015-6bfab4a5b2e2 | -7.82728 | -45.30195 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb1e154f-6079-395d-8c8c-250b2574bd04 | -7.84422 | -45.31095 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c6d3833e-6a11-3099-9292-180121bc9a8b | -7.90741 | -44.19937 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3032a892-27c4-3637-bb87-7e21ec86598b | -7.2981 | -43.79219 | 2026-10-05 15:54:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 42c804f6-d172-39f9-975c-a8dfba48bdeb | -7.66173 | -44.37761 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c7322786-62f3-3870-b503-ce5610dae712 | -9.97108 | -45.60117 | 2026-10-05 15:54:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ffb96364-0498-359f-b11c-a5507d64dca2 | -6.89695 | -43.66713 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| d43bde97-7ff7-318e-99cf-e5ab54f41a4f | -6.69905 | -45.23072 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| cf852a8d-51e1-3d98-958a-bb876cf8d04e | -7.18147 | -42.00599 | 2026-10-05 15:54:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 02796b4f-54c6-370d-860b-5b03a0272b41 | -6.77297 | -39.02656 | 2026-10-05 15:54:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a4e34971-f2ca-3f3f-9d31-966c9495d86e | -7.9005 | -44.18956 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ae9c1cdf-1c7c-355f-bf88-8cc844fc8d30 | -6.37861 | -43.63377 | 2026-10-05 15:54:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5afa2e42-a04b-3ab4-8ecf-527a6d9c554f | -9.82111 | -44.79284 | 2026-10-05 15:54:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| efffb98e-7199-39fc-96f2-1b733877c0f3 | -9.75921 | -45.29951 | 2026-10-05 15:54:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8757aca6-4792-3c71-9c01-5581956fc594 | -6.80802 | -39.29903 | 2026-10-05 15:54:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 4feeb79a-154b-3518-96c6-bca748382fe2 | -6.90795 | -43.66911 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fdc8c082-93c9-33b5-bd5a-a9aeb93ba495 | -7.90836 | -44.20668 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 52e57574-8c89-31b5-8cc7-55a382aa995e | -10.20638 | -46.67773 | 2026-10-05 15:54:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| de7198e5-fd5d-382e-a038-442d1ea9920c | -6.31749 | -43.34504 | 2026-10-05 15:54:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 514e9baf-3e0f-3193-903a-36dbe79947f9 | -7.78263 | -35.56533 | 2026-10-05 15:54:00 | NOAA-20 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d09796a2-4086-3b0d-aa60-186559a6dad7 | -6.92305 | -38.33131 | 2026-10-05 15:54:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bad1c351-41cc-3b81-802b-92a24f5911fe | -6.61225 | -37.89088 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 75.1 |
| f972ca09-6b73-3b6c-ab84-a5ab808f3dc1 | -9.81041 | -44.80344 | 2026-10-05 15:54:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 9d7008a5-7aef-3f0c-94f0-87434751a268 | -6.3935 | -38.91072 | 2026-10-05 15:54:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| f53b8cc2-a45e-3111-a7bf-4212bcb1c87e | -7.8248 | -45.32841 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| a65644a5-d893-3247-ae46-bed6263b6734 | -8.64923 | -45.84126 | 2026-10-05 15:54:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5a60877b-b667-3fa6-9d14-67f566b62a05 | -7.83076 | -45.32772 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 96043393-e8f8-3654-8f9d-fe7b07d5f862 | -6.61185 | -41.57113 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| 2d415ba8-700d-3ccc-879f-74aa9d99fc1e | -6.69375 | -45.23544 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 8af65234-b566-3010-8c3d-dc84f88dc2ba | -7.90693 | -44.19572 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d9e66800-2394-30f1-8e6b-be3a9fcf0add | -7.82845 | -45.31056 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 388e3e12-5069-3d7a-a8dd-e2fdcd2b2ef7 | -7.82635 | -45.31313 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 7ec90764-6b0e-3536-8b76-6e23f738da02 | -7.8258 | -45.3088 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| b30caa8e-6054-360d-b1a3-480c991d3854 | -6.90882 | -43.67547 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f19ede2f-60b0-3553-8d95-e58baa5a64d8 | -7.50551 | -40.08638 | 2026-10-05 15:54:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3c1b22e8-c9ef-34c2-b6ad-8f787fa37daf | -9.1566 | -45.12984 | 2026-10-05 15:54:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 85da7e2f-4334-37f6-b1ba-7efc248b49f9 | -6.15195 | -39.80089 | 2026-10-05 15:54:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e801dd09-afa4-3df8-84d4-5c8e3ff4c9a6 | -8.78543 | -47.54763 | 2026-10-05 15:54:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 92c427fc-cdd6-313e-b19d-3e0bab9b5e5b | -9.40855 | -47.30641 | 2026-10-05 15:54:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a700af2d-7a62-3c0c-b5c2-343f2e1989e3 | -7.48795 | -42.80107 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 1533617c-271a-3cbd-93df-076628d29b6d | -6.64896 | -43.77336 | 2026-10-05 15:54:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7ab697af-50f4-3a2c-87b5-dc1b09a733e9 | -6.68634 | -45.22442 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 07d41a66-496f-3987-b10d-bf63209cf090 | -7.4787 | -42.80791 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 6e76fd75-de9c-370c-b66c-20f9a0c8098a | -7.78211 | -35.56181 | 2026-10-05 15:54:00 | NOAA-20 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d60c5d4a-11cf-356f-9d0a-9c3539203313 | -7.88103 | -40.20603 | 2026-10-05 15:54:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| cc3409b2-63f8-39e3-8f79-ab062b06de67 | -6.32966 | -42.55502 | 2026-10-05 15:54:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c832bb1a-a3df-3f69-9819-6cf7bce2afbd | -6.61639 | -41.57051 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 87f2204d-2701-3434-8e06-fcd548402b45 | -6.6933 | -41.00047 | 2026-10-05 15:54:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6a616aec-3961-399f-9a3f-74403c1b1226 | -6.69959 | -45.23472 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 625163c3-2289-30f9-bf0f-354f3d00720c | -7.65518 | -44.37114 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b848759-923f-3c97-8da6-699bed3e0fec | -10.40097 | -47.53359 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b7b4483f-6972-3a95-94b6-2ef7217131ee | -10.20962 | -46.6787 | 2026-10-05 15:54:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8c05bf3c-b795-3239-bfdd-2f22e004966c | -9.28803 | -43.32146 | 2026-10-05 15:54:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| db176027-b0f1-3a26-94b4-411044d5d069 | -7.56465 | -34.90779 | 2026-10-05 15:54:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 80d3aa73-ca17-387b-8089-c8876403f662 | -6.61109 | -37.883 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 50a2c4e4-23cc-32da-a6ec-7b417b3e8bc0 | -8.00235 | -35.08789 | 2026-10-05 15:54:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| adbce249-c7bb-3b41-9b6a-f08e46930c81 | -7.90145 | -44.19692 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b654b99e-2785-384d-a02d-9501bbe229bc | -9.04095 | -45.15252 | 2026-10-05 15:54:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 42bd90d2-5687-3d2a-95aa-c70ca77d4d07 | -6.6205 | -41.76634 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 14f89d2e-ec66-3aae-ab44-8d065338adfa | -10.20293 | -46.6794 | 2026-10-05 15:54:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 03bcc769-d311-33d5-b614-f1b61d938511 | -5.98416 | -40.91184 | 2026-10-05 15:54:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| 7384cc07-4d1d-3190-be4c-854cd571d554 | -9.02949 | -45.15808 | 2026-10-05 15:54:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2444be60-0ee6-35a7-a5b7-556ddfbde95a | -6.92512 | -43.6768 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| c3bfc8d0-9113-39d2-acc0-b4fac3b5fab6 | -7.5428 | -45.40002 | 2026-10-05 15:54:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d27f71c-d144-30e2-92ec-47265e7130b5 | -7.47911 | -42.81078 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5150586e-52a9-3513-bb19-4703d9dbd4bf | -7.48301 | -42.80062 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 8d0743b5-487f-3658-b11b-99c79d3a4ddf | -7.47913 | -42.80981 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| b3a0b7ea-45eb-3d0e-b0cc-374d9bc2234b | -6.69745 | -45.21889 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 170f353c-9377-3c65-b9f0-849fd24c2d73 | -7.56652 | -35.45802 | 2026-10-05 15:54:00 | NOAA-20 | SÃO VICENTE FÉRRER | PERNAMBUCO | Brasil | 2613800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| eef574f3-0cfb-3f8a-9a58-d27b0d0e5d39 | -7.47875 | -42.80694 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 0811cd97-8727-3341-bfd4-fd109c2fe164 | -7.47837 | -42.80406 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |


[Clique aqui para ver as próximas entradas](README74.md)
