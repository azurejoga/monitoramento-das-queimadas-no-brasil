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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ef97469-4943-322e-b582-c27af7a7e7d7 | -9.96348 | -51.20018 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04bd8613-20db-3130-80bd-3c9c63d300ec | -6.35601 | -42.58653 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 24a55c6a-e5c8-318e-93ef-1a3847b311b3 | -6.17421 | -44.24642 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53d17ea6-d6c3-3375-8704-99960a9b2e99 | -10.81354 | -47.25581 | 2025-09-08 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa7cabf9-c827-3c63-b6a5-cba816863065 | -6.88073 | -45.53588 | 2025-09-08 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f0d3cb37-cf5f-3ac9-8e82-23de4bf9d416 | -9.88993 | -46.49054 | 2025-09-08 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c51a3196-32c0-38e5-8f63-074855beae2e | -11.32709 | -46.5538 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f8f4204-357b-3589-a279-2ace377abd87 | -9.80684 | -46.23759 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c455196-b3fb-3716-9dab-f488fe25c319 | -6.62643 | -53.36095 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77707232-5064-3bd4-8282-fa3144dd8370 | -9.7187 | -45.94785 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed6dc1fa-9ce9-36a5-843c-04fd47e5ed16 | -9.16861 | -59.36802 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ec37d84-2508-3124-a306-ba5ee57cf22c | -10.4728 | -53.61057 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa1e96eb-2a24-3584-be3b-23260890c44b | -4.30538 | -48.09429 | 2025-09-08 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed795031-62c0-3c98-8a3a-4d5f4719f043 | -7.40316 | -61.62874 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 83fb9d4a-2cfc-391c-ac9d-f9de7c642888 | -9.23727 | -57.06743 | 2025-09-08 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c9fff3c-d89c-322a-a9b6-af2f1f3586c9 | -6.22651 | -49.41999 | 2025-09-08 04:51:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e3dfea4e-53fd-3833-a6d6-c9403ca35fde | -9.81684 | -47.77727 | 2025-09-08 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adc7c8f7-3a5f-3e98-917f-e0be9d32156e | -6.63083 | -53.35453 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7344712-481e-3106-b79e-3c34b6bb7b2b | -7.24848 | -44.83505 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ab96df6-c8f9-3b6a-8001-75804bc3acb7 | -7.68594 | -50.28257 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3cb95e4-f84f-3b42-b015-cc00793ee2b1 | -10.00558 | -51.62275 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fc7ec04-1e9b-3009-8d21-a7fa5a2de55c | -9.17493 | -46.06714 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f923a23e-1952-3c98-b592-5162c2f8fb2d | -7.74614 | -50.75166 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ff7f409-d0f3-32ef-bf0f-e911ecd88dbe | -9.50591 | -57.78344 | 2025-09-08 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37abdcd7-c5e0-365e-8234-c8b49d2d4fbe | -7.59208 | -49.28706 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcf3e4f7-3f08-3f92-b665-d63ea8647b72 | -6.63028 | -53.358 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 592617d5-e8b1-3830-82a7-88444e8d73e0 | -7.74246 | -50.31534 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8aa6d788-a205-32e2-b7ae-d0bf34448e74 | -5.44307 | -42.5877 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3dc5158-257f-3e1d-a670-f8c47f40bc49 | -11.41656 | -43.59081 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c73979e-8c65-3668-8b7a-e8a929e4c671 | -9.15477 | -46.07483 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac0bc570-b432-3ad4-aa36-e3179b01f58d | -9.80217 | -46.23679 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78c051da-18c2-3b26-9881-5f2a04286691 | -6.66857 | -43.84406 | 2025-09-08 04:51:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1664ac1b-f083-3b99-b28b-d448862ef473 | -5.64788 | -45.11642 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a323cb2b-0640-3598-9407-1f32cffe04ff | -6.09087 | -43.12074 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93c605ad-239e-3d47-8395-bf95eeedd0f8 | -9.2736 | -60.91099 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0356b330-d013-3aba-be0d-3f81f926416c | -6.30689 | -43.82397 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 245d47a2-73c1-31de-b861-f2462ed71bf3 | -9.96637 | -51.20458 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50dd70a1-04e4-360e-9e72-c556189dd0db | -8.69999 | -45.30435 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75eda1ba-5234-3e0a-a999-531d847804f2 | -9.97026 | -55.04624 | 2025-09-08 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a78ca3c-d78b-38d3-b9b7-5d010c189a69 | -7.36617 | -44.31273 | 2025-09-08 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41fdb52b-13c4-3977-af85-c2ffdec807e8 | -5.49581 | -42.66213 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 68833b3e-dbb1-3295-9658-60a5de8afb99 | -9.39597 | -46.78699 | 2025-09-08 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9b02351-b581-3017-8d71-f9f73c3f21fc | -6.62257 | -53.36391 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0b095a2-19f1-324b-b455-431a3312002b | -6.4667 | -43.94789 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55157f29-f02e-3cef-b053-2e731c82075c | -8.88028 | -51.03848 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e2d8939-3578-3008-a0eb-5c311c0d0fa3 | -8.88617 | -52.0414 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9ffae8c-debc-3e3a-a4a6-56183cc4b193 | -9.11519 | -61.48891 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9779ff19-e87f-3251-935c-a1b55c752044 | -11.42794 | -43.64098 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 749e8a45-3579-3538-a179-8b24644302ef | -6.81995 | -52.8 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b5ec6930-524e-3fe7-871a-e77632439c52 | -7.43134 | -49.26727 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3db2cd36-8f3e-3078-af53-27989208bc5c | -6.30164 | -43.82319 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a950556-f3d8-385f-b855-403d725a7cf8 | -11.32623 | -46.54403 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53492033-f417-3302-b41a-32cb1db35613 | -7.68784 | -44.80494 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ee7b5b9-d2ba-3721-b2ee-995a2bd074fe | -7.83043 | -45.42407 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5241dbdb-6cf1-355e-b62d-9f017b3650f6 | -6.40148 | -44.45423 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e654f54a-2ae5-345e-ae14-5d9d2622f71c | -10.15626 | -46.21665 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20bab9ec-b36c-3fa5-9bbf-fdbd79cfe9b2 | -6.17589 | -42.63653 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ca4d64c2-cd95-33f3-b58e-13fa72e41218 | -7.74306 | -50.31138 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8843e59-006b-3303-beea-e7c8a396667f | -6.17505 | -51.51862 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ab2a7d-b5d0-3f75-9b0a-1f1191c1c209 | -5.54047 | -43.0624 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94cb9e37-d15b-3eaf-91d2-8ffa34b88df5 | -7.88075 | -46.25558 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89614dc5-a0a9-332a-aa0a-0ae3889d665c | -9.2842 | -56.89993 | 2025-09-08 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ef464fa-d060-3da5-b7d4-d6efae8031af | -9.58274 | -48.29449 | 2025-09-08 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dd3914d-cfd3-32b7-b196-699ad6710288 | -8.87774 | -47.90303 | 2025-09-08 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd67b964-1dfd-3cc0-8648-264a2e7beca9 | -7.61735 | -43.87595 | 2025-09-08 04:51:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ea17b73-502b-3ab9-8c68-633a24557492 | -7.83168 | -52.15458 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cf1cfa0-e4b6-3c79-bd11-f39ab153832e | -8.37862 | -48.27367 | 2025-09-08 04:51:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e81995ef-ecd4-3bd8-aa63-52d65a619ae1 | -9.45701 | -56.051 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ae419d0-8aa9-3b79-9fa8-8652a5623f4d | -10.14086 | -46.18814 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0238c40b-4ed4-32d2-b0f0-bd432c155242 | -6.20258 | -53.2651 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5db64110-a421-324a-baea-4e0fa8d196e4 | -9.56358 | -53.59636 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07acc123-7fb2-39d0-a078-084048549b6c | -9.73284 | -51.07482 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca2e4504-92e7-3c92-b3be-04bcc7de700c | -10.45077 | -53.59991 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 390f54ad-73ce-3202-9031-d549e40de791 | -6.64449 | -44.80656 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f2651d7-d400-3735-b9b1-4d48b9dc3943 | -6.63468 | -53.35158 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 874287f7-bc82-3fd4-b581-707f8bc7460d | -6.95151 | -62.92494 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9296fc9-15d5-3437-817e-0c11c4ca8d34 | -6.85636 | -44.82845 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 831e8d99-1008-3df1-bf16-18f476ba5b64 | -11.57101 | -44.65731 | 2025-09-08 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f8417e7-a6ce-3273-9c54-2816d07198a6 | -7.22653 | -46.2103 | 2025-09-08 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 808ff79e-d8bc-324f-b933-ec417bcf48cb | -5.99864 | -47.60934 | 2025-09-08 04:51:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd483590-c8fc-3b6b-ba6c-9504739a6485 | -9.95712 | -51.19512 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 040536f0-f125-3643-835e-8a6c46765a4f | -7.68788 | -44.80356 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ce6a6f0-6217-380b-9cc9-9e903589e652 | -9.20583 | -46.05117 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8a9d6512-d28b-34b0-be33-02348745cf75 | -9.46051 | -56.05158 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd170e88-5ee7-3525-9f3b-471478de0223 | -6.62476 | -53.35002 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58e011bf-605b-3e05-9f85-03e15f99bb29 | -6.83591 | -52.80603 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aadd6f9-4be0-3ef7-b7ac-6a86c1fefde4 | -7.75136 | -50.74049 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80d82569-c053-3024-ad83-c4c2d24fb8f2 | -6.81173 | -52.80932 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f84a33c9-ee2b-3aee-a2ed-1029b23ea220 | -5.24809 | -57.12577 | 2025-09-08 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0f026370-2f4f-3d1d-bd82-c1f98bae72e2 | -9.16931 | -59.36405 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 000c7006-87cf-3c30-a481-eea78e3826a9 | -3.20991 | -54.96142 | 2025-09-08 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ef8e2cb-679d-31a6-bac5-2d29da13b73f | -6.967 | -62.93557 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b09bcec9-c5a3-3b9f-b776-cddefe109442 | -4.2696 | -48.18162 | 2025-09-08 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ec791657-6783-3cf8-a764-a97c4b2e6db5 | -8.21716 | -49.51397 | 2025-09-08 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 934300d8-8184-30d2-abb5-4d25ca8c4fd2 | -3.73497 | -49.68883 | 2025-09-08 04:51:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 724a8a97-bfe6-3392-8dc4-46f7a54e07dd | -6.09063 | -43.11851 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51d6debc-a04e-3d33-b325-8047145af463 | -9.86339 | -46.5832 | 2025-09-08 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e03a6ab-b9fb-3f45-a5c5-2e8d61daf01c | -9.99936 | -51.64097 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca669b70-7c5c-36b1-8ef5-4473401e1c3b | -6.27101 | -53.43614 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 405144fe-2da6-3ea7-a522-51fa182af136 | -8.88833 | -51.05579 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README52.md)
