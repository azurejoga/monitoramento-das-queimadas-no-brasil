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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 464c9f30-3e14-3298-81cc-b76b9f16bdcc | -9.21702 | -47.93114 | 2026-06-19 05:01:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59c87baf-ba06-3f15-89ed-c53af84915ec | -8.78754 | -46.62817 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34266b4c-138f-3e1b-b93e-21d67689dfe4 | -10.69478 | -49.6078 | 2026-06-19 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff2567f3-6788-361e-b66a-dc58f1c86d09 | -9.74864 | -47.87846 | 2026-06-19 05:01:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c376363-b88a-331b-b5b9-1dc517da58e1 | -6.75081 | -47.12815 | 2026-06-19 05:01:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecab5b93-3b69-35c4-90a6-5c46590f1e08 | -9.7492 | -47.87453 | 2026-06-19 05:01:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44761ef8-c03f-30ad-9f32-e907a013c471 | -7.79657 | -46.45643 | 2026-06-19 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc07e2d3-84c8-313a-921c-86e71cba4caf | -10.98718 | -47.74733 | 2026-06-19 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd88f014-7314-3997-a403-909cc80223aa | -4.35466 | -47.76094 | 2026-06-19 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffc8a621-89de-362f-aa62-67485edec510 | -9.80606 | -48.92019 | 2026-06-19 05:01:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff8439ab-245e-3d6f-b710-a8250bc868f2 | -8.90952 | -46.95446 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17f3d33e-c8ad-30de-ae22-1ba7f348a274 | -10.54025 | -47.71585 | 2026-06-19 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b90a8abe-874f-323a-8d0c-76552e8846c5 | -8.89352 | -47.99905 | 2026-06-19 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27abcaf4-9c45-3806-bdb8-eab7f3055635 | -8.91076 | -46.94566 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c54c6ad8-c87e-3984-9529-1ac7887dad0b | -7.47718 | -38.96286 | 2026-06-19 05:01:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6344d0ec-4b02-3cb7-9d75-4fdc9d62cd7c | -10.5567 | -46.33965 | 2026-06-19 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0b81f68-89ed-3e94-acd8-f66cb2d9c825 | -10.25344 | -47.34241 | 2026-06-19 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1bc788f-f642-38d0-a197-8cfa28b0f09b | -8.68689 | -48.30595 | 2026-06-19 05:01:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e9b3f52-1130-37d9-8318-ded92bccab36 | -11.06059 | -52.46185 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c92bda72-9b60-3aac-b2bf-305362ee71c7 | -10.9835 | -47.74916 | 2026-06-19 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 745ee62e-8c5d-3105-bec1-08847b80e3d3 | -11.06454 | -52.45871 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3b96be4-cbf7-30a5-afd6-fdd3a074c506 | -4.34996 | -47.76534 | 2026-06-19 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bd7a8f8-0750-3e26-8294-260e20452990 | -9.74497 | -47.87384 | 2026-06-19 05:01:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15b164f1-b3b0-3357-99dd-cb5dfb91bf54 | -10.05265 | -48.09575 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68983bab-fdb2-32c2-8fac-945717318c34 | -8.90444 | -46.95827 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11de71cd-ab9a-3f26-ac0d-aaff5d8dd545 | -7.8297 | -55.40403 | 2026-06-19 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddb0e257-7e81-3f35-9d7c-317b097e5630 | -11.05832 | -52.45396 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e282d9-8fb6-31be-8690-7eed18257b27 | -10.90463 | -54.13568 | 2026-06-19 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68069324-da8b-37e1-8cef-7c75eca99ac0 | -11.33595 | -48.00566 | 2026-06-19 05:01:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9b9bc40-101f-3443-a951-b64c3980bb71 | -11.05664 | -52.46498 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a72603e0-b8d0-397e-934e-e0e6f67659b2 | -10.77107 | -54.10723 | 2026-06-19 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ec95ec3-cfef-33b0-828a-dca8568e1330 | -10.05322 | -48.09182 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84269833-459b-3edd-8325-7886632bdb07 | -7.35917 | -49.8606 | 2026-06-19 05:01:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81144f50-2d06-38c4-831b-b1460e2ef831 | -10.24901 | -47.34176 | 2026-06-19 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a7a50e2-17eb-30a6-bb81-c7914b42ce6b | -10.99219 | -47.7505 | 2026-06-19 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e8b50ec-4358-305b-bcdc-baeab11d9844 | -7.4782 | -38.95513 | 2026-06-19 05:01:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dc6fb02a-db29-3e86-897c-67fe0ff7124b | -8.9089 | -46.95885 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 112a4fb8-2e75-364b-8759-1d3e8a104c7b | -10.69862 | -49.60841 | 2026-06-19 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09db279d-d495-3191-a988-0f79195d2523 | -8.89766 | -47.99971 | 2026-06-19 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b24b2a8-22ca-35b4-be85-4e49e55cbd74 | -7.80173 | -46.45273 | 2026-06-19 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4129db18-26a3-3580-b63e-1c8f9e9035a2 | -8.89297 | -48.00279 | 2026-06-19 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e01ff34-0898-3064-a15e-2fbd1fdf905b | -10.98784 | -47.74987 | 2026-06-19 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a23efcd2-c4b6-3151-920c-f8aa760879ee | -10.99093 | -47.75218 | 2026-06-19 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6032fe5f-ead3-3fce-beb5-b29637f2167f | -4.35391 | -47.76597 | 2026-06-19 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e7495602-abbf-3f3b-a6db-032fe01b0583 | -12.41201 | -43.82304 | 2026-06-19 05:01:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dc04c62-f8d0-352c-9017-87d3634e5a2e | -10.06273 | -48.08519 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e9e3c65-819e-3451-9e10-2ffced8bb02c | -8.56827 | -45.98993 | 2026-06-19 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 123662ed-ab08-32e8-b294-1d06b350e888 | -10.54085 | -47.71161 | 2026-06-19 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dbc32577-04e4-374c-93f1-1b9680890b9e | -10.04214 | -48.10948 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97d94522-3904-3014-94d0-e2fc950ced50 | -6.90322 | -42.84288 | 2026-06-19 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3fdc168e-6dae-3a72-8c14-f563f4157f04 | -10.79427 | -48.22959 | 2026-06-19 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a9e72e4-d2e8-3c32-8023-d2d2b446130b | -10.05741 | -48.09239 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7c2275e-d9fd-3611-af99-8c21476b27a3 | -9.68441 | -47.04002 | 2026-06-19 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af49965a-c91b-30ee-86cd-2f5983ed3d75 | -11.06003 | -52.46552 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f167c031-4fc6-3ada-a86c-fe6f4550614d | -7.83255 | -55.40845 | 2026-06-19 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b80c3e22-438d-3b7a-867f-809c25ae160e | -6.90894 | -42.84371 | 2026-06-19 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5442f7f8-3c1f-323e-9297-a5c94678feda | -6.90841 | -42.84751 | 2026-06-19 05:01:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ffcc8b7e-f7aa-3328-a94c-4b59f0a30fce | -10.06162 | -48.09285 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 223f4f88-3861-3357-9ca5-b54469b20140 | -7.80109 | -46.45719 | 2026-06-19 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a305259a-6ad6-3777-90d4-138fbc46ea62 | -10.12364 | -52.17986 | 2026-06-19 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eabed368-d044-34f6-a001-47d30e290ebf | -10.90646 | -46.33561 | 2026-06-19 05:01:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df62d50b-9d47-371e-ab51-0a7c135c387a | -10.98407 | -47.74495 | 2026-06-19 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 571c8940-be3d-3233-a281-19aa6fcd31d1 | -8.78688 | -46.63271 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a462d0a4-8c61-3372-af34-4a540c11b224 | -4.23553 | -49.18018 | 2026-06-19 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb72cfff-4616-335c-8c3a-baa732bd94dd | -8.90382 | -46.96266 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3aea3c57-f133-345b-84ce-087b9adb4088 | -10.04847 | -48.09507 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6d7e839-0b89-3918-80cc-248f42b0d0b0 | -10.76774 | -54.10669 | 2026-06-19 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceb04083-bd1c-3471-83fc-98754eec61bf | -7.79721 | -46.45195 | 2026-06-19 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa0f6108-c8c2-3c32-a86e-741b5bc690f8 | -10.04268 | -48.10569 | 2026-06-19 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27985050-3118-3718-a08e-03d1b3147349 | -11.33166 | -48.00499 | 2026-06-19 05:01:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4259705a-cd23-3b8b-89e1-ddd5778da9d0 | -10.69791 | -49.6132 | 2026-06-19 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6164fd0-6dfe-32cd-8c6a-ded7713a77dc | -7.83318 | -55.40461 | 2026-06-19 05:01:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b04fbd39-fad1-3b4b-ae42-e783c2979939 | -8.91139 | -46.94123 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a743e7b2-d087-3616-8437-2614203d40e1 | -3.81999 | -50.63284 | 2026-06-19 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51bee64f-92b4-3b27-a106-9969afb97630 | -8.91014 | -46.95007 | 2026-06-19 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77cba1e0-5b4f-34f0-b35f-300cac7f3d80 | -3.85052 | -54.22183 | 2026-06-19 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2984eff4-75ea-32e9-982b-98971d550899 | -10.7178 | -56.04498 | 2026-06-19 05:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f420be2-04b1-3e65-8d50-1949959cbb13 | -10.82963 | -50.20825 | 2026-06-19 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a904c00-5881-3c2f-8035-4ebaa51f5e3a | -11.06115 | -52.45818 | 2026-06-19 05:01:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53bbc52b-f0d3-3c72-97e2-81e54f4327d1 | -10.16026 | -56.62126 | 2026-06-19 05:01:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e69bde3-cbba-3708-81a3-b910a3626aec | -8.56898 | -45.98475 | 2026-06-19 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5605cc45-91ac-323e-bbda-03395c879830 | -8.5683 | -45.98719 | 2026-06-19 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41f9e28d-7962-362f-b0d4-fc2e70e09cf4 | -13.3358 | -45.20361 | 2026-06-19 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9548e32e-b848-3942-b2eb-b567e429a4dd | -12.79138 | -44.51049 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb3b1435-4069-346e-b3ce-54c3f2e144b8 | -13.4887 | -47.50639 | 2026-06-19 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31ce05d6-9b16-306d-bf97-dddbaa5f776a | -11.61541 | -55.32924 | 2026-06-19 05:04:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90be8947-76f3-378a-89a8-548d34a0b991 | -17.11149 | -49.75177 | 2026-06-19 05:04:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22ffbe2f-c7d3-3174-8b9d-f4a288d985d8 | -11.72312 | -54.49419 | 2026-06-19 05:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23a3d097-37b4-30e0-957e-2de2c556b1ea | -10.9138 | -56.85514 | 2026-06-19 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ed84b77-bb32-3c15-8660-69f55a253cb5 | -14.75664 | -52.6968 | 2026-06-19 05:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 721ed89d-de27-380a-aba6-cd14029c1ec8 | -17.34407 | -53.81328 | 2026-06-19 05:04:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86f307c7-a19b-3bbb-b041-c24d94e696f8 | -14.94925 | -52.87547 | 2026-06-19 05:04:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 501efcf1-baa8-315f-901e-365cac5d4e0e | -17.32109 | -43.64737 | 2026-06-19 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6d45a01-ecb5-3adc-845d-2db897ad0a4c | -12.54819 | -54.58608 | 2026-06-19 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ecda6def-6793-31bb-9901-0a06d2a43691 | -12.8626 | -44.37387 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 649d879e-8042-3237-a9be-9a32cdfd346f | -11.78608 | -56.99702 | 2026-06-19 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85302b1d-66a5-3dec-8ee2-a13cb009764b | -13.32722 | -45.18524 | 2026-06-19 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acace52b-1bf3-372b-9bd0-b148405a1c99 | -11.26097 | -53.95552 | 2026-06-19 05:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20072d55-ad41-36bc-9d49-19ba87aae5ea | -17.31705 | -43.64596 | 2026-06-19 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ca31f59-27b5-3027-b30a-0cb01b4119b5 | -13.31946 | -45.15997 | 2026-06-19 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
