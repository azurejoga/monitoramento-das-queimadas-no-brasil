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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 873477fd-5b56-3537-a5df-c3f8baa70449 | -15.5945 | -49.8292 | 2026-06-01 00:00:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 59ed7aaf-198e-30f2-9b9f-187e0bac82ff | -11.6286 | -52.5702 | 2026-06-01 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| da13d981-afd1-35b6-92b7-c4da10a8c4cc | -18.5489 | -50.8901 | 2026-06-01 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| b85f00bf-4adf-3a3c-a0a5-4af18628a69e | -11.6286 | -52.5702 | 2026-06-01 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 13504275-376b-3994-82a7-044c2fa54360 | -11.6289 | -52.5493 | 2026-06-01 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 24fc0088-43e8-3dd1-97a0-2d9049dcd804 | -18.5499 | -50.8458 | 2026-06-01 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 8a7aaac8-86c5-3131-a1e0-7430c3964700 | -18.5494 | -50.8679 | 2026-06-01 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 245.1 |
| 9f0009d8-ac95-3d5c-b515-930e311b9806 | -5.099 | -46.949001 | 2026-06-01 00:15:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a4ef83c4-a205-380b-87a7-b8ffd2197536 | -5.0971 | -46.940498 | 2026-06-01 00:15:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb09211d-e73a-30ec-ab72-2344ac3f1c99 | -8.7262 | -48.311699 | 2026-06-01 00:15:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd76e974-a061-3390-990f-ab2495a80919 | -8.7286 | -48.3232 | 2026-06-01 00:15:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0624089c-4b84-3190-a6c3-ce8faa940034 | -6.9927 | -42.880901 | 2026-06-01 00:15:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f0832c25-1126-315b-87f7-5411f7f323e3 | -6.9912 | -42.874001 | 2026-06-01 00:15:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 604fb814-1583-35e9-ae35-d936a133432b | -8.7311 | -48.334702 | 2026-06-01 00:15:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d22a69d-2b55-30fb-88d6-fee67f2dca60 | -6.9943 | -42.887699 | 2026-06-01 00:15:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7447f602-09c4-3984-8363-35045ea1f3ea | -8.7384 | -48.321098 | 2026-06-01 00:15:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 820c9e4b-84ed-3a5a-a4b2-8e6dee415436 | -11.62067 | -52.55984 | 2026-06-01 01:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| fb5230f3-7c66-3098-a199-579aa3610c61 | -6.99122 | -42.88478 | 2026-06-01 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| dc4043f9-0218-34b5-bb80-e1a96c66b95b | -8.14215 | -40.80072 | 2026-06-01 03:23:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d3ff2d0-90b5-3039-b498-b669f6e99124 | -9.4903 | -40.31419 | 2026-06-01 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5c3042b2-6f31-389e-9877-7b1d4df4d8ac | -5.52374 | -37.48839 | 2026-06-01 03:23:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e231dba5-24c5-34f8-b01f-da5bb2449f6c | -6.99019 | -42.8903 | 2026-06-01 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 867b2f9e-a7ac-30ac-bbdb-7eb1ae93955e | -6.99224 | -42.87932 | 2026-06-01 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9d1b7b51-eed2-3a44-a736-4611487978e6 | -5.52267 | -37.48464 | 2026-06-01 03:23:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1e907ed4-e52f-3b7b-ba94-9caa0c125af0 | -5.51903 | -37.4876 | 2026-06-01 03:23:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6891028-ef93-34d1-944a-f72aff8cd3c2 | -15.82953 | -41.42096 | 2026-06-01 03:25:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09ca8d23-6463-3974-977f-69aee616ac6f | -17.62664 | -42.01965 | 2026-06-01 03:25:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 65da7cb0-3d6d-3f02-9efb-236bd940e8d1 | -19.18688 | -40.13678 | 2026-06-01 03:28:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| df5ce554-51fb-3ef0-8fa1-85b903d25dd1 | -21.39157 | -47.01924 | 2026-06-01 03:28:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c226fb4-7783-39ae-b26d-2ddfe012704c | -19.18631 | -40.1348 | 2026-06-01 03:28:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 365ac664-49c1-3520-834c-e68564cd9515 | -19.18721 | -40.13025 | 2026-06-01 03:28:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1f5b8952-c17b-3f60-a4f3-a3054d848789 | -22.68586 | -42.13852 | 2026-06-01 03:28:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c5a2aab1-26f5-3c58-89f8-d10e15d762b8 | -20.64253 | -42.29882 | 2026-06-01 03:28:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 55e07fc1-7837-3cfd-bf94-878927e8c5b7 | -19.18776 | -40.13221 | 2026-06-01 03:28:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 08c4d99f-4257-3864-b8d2-d53eb0155233 | -8.1225 | -49.8613 | 2026-06-01 03:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 164cb49f-4fff-3406-ac98-1ed0b38268f7 | -7.97188 | -34.89475 | 2026-06-01 04:17:00 | NOAA-20 | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2969d540-4076-35ac-b708-dad22c05b8e5 | -6.84378 | -47.93054 | 2026-06-01 04:17:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4fca6fe-255f-35a6-aac3-748a958c307e | -10.72505 | -46.91662 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9eaa122b-5a04-3f3b-9cf0-cfd6e611e35a | -11.63422 | -52.56626 | 2026-06-01 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f9e37b3-f0a9-367c-8cb6-494326d12baa | -6.84772 | -47.93126 | 2026-06-01 04:17:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5340962-430a-3e38-9044-36e3ccea50e3 | -10.72233 | -46.93294 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a782e93d-dbb1-3e63-85d4-c6316302e829 | -6.98904 | -42.88794 | 2026-06-01 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 65fbdfe5-4e39-3259-85b8-1c1e4f2a35b8 | -5.60939 | -37.53014 | 2026-06-01 04:17:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ba379f5a-6098-395a-98eb-b1ad06210eb9 | -10.6952 | -49.61266 | 2026-06-01 04:17:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0583545-0538-39d5-b83c-df06bc540919 | -11.59014 | -47.44264 | 2026-06-01 04:17:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce0221e2-5383-36f4-9674-003b007e555d | -12.06108 | -48.07046 | 2026-06-01 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f54a915-5f87-3a1e-b249-b4120c9e32d3 | -5.10292 | -46.94524 | 2026-06-01 04:17:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 338a2a1a-6d87-340d-83e0-064a442188fa | -10.06289 | -51.66362 | 2026-06-01 04:17:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c97aed9-9678-30fd-9974-25b18438ca88 | -11.74159 | -54.79694 | 2026-06-01 04:17:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03e5d91a-030c-3c35-ac2a-10596b79d179 | -6.75843 | -45.02842 | 2026-06-01 04:17:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ec898b4-661a-3053-8615-faca41e77022 | -11.61548 | -52.55681 | 2026-06-01 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e720845-8f59-3b06-9fcf-941004a98fc2 | -6.99013 | -42.88101 | 2026-06-01 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4c703dc3-96c7-3515-854f-9e7b957189b2 | -10.54915 | -46.64453 | 2026-06-01 04:17:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5ddc771-11a4-3913-949d-a8af41d47fef | -11.74317 | -54.78901 | 2026-06-01 04:17:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c7ce857-9e55-3d30-88e8-611e2d980157 | -11.61163 | -52.55007 | 2026-06-01 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e26b0753-b1fe-3642-9ef9-ea8960a8d543 | -7.16835 | -44.07016 | 2026-06-01 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 144610c6-eae7-37c5-b48c-eef17f324d0c | -12.32195 | -47.90419 | 2026-06-01 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a61e3e0-c5b8-38ea-b763-885ec91a1e1e | -10.86002 | -46.93499 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aac0b9a7-a5c1-3a4b-8549-7dc13d66656e | -12.31756 | -47.90792 | 2026-06-01 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de705084-3818-3ccd-8120-0b58692033b9 | -6.98959 | -42.88447 | 2026-06-01 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 952c9c10-a0ff-3023-9f14-411265caca75 | -12.40849 | -47.49931 | 2026-06-01 04:17:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acb617a3-2309-3948-a649-6648bcc8e0e9 | -5.10342 | -46.94817 | 2026-06-01 04:17:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86fb9cd1-3a27-3ede-a4f5-93ad48777e09 | -10.74415 | -46.9114 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcafb843-1b08-3f45-834d-363d72145157 | -10.72656 | -46.92949 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5251508-9269-3277-9980-6d40cc3f1e2c | -7.31509 | -46.9937 | 2026-06-01 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62d3d2f4-b419-3e67-ae92-32fd01298b78 | -10.06205 | -49.75417 | 2026-06-01 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad85a004-1db9-3efd-9ef6-c01406990e75 | -5.51998 | -37.62189 | 2026-06-01 04:17:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2deaa6f3-5aeb-3f9c-8d93-890a123cf86a | -12.40492 | -47.49868 | 2026-06-01 04:17:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aac3bc65-bca5-31aa-853e-f32b964668ab | -11.61597 | -52.55136 | 2026-06-01 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bbcb34fa-156a-3c73-8e63-3df6b3f32ecd | -10.55266 | -46.64512 | 2026-06-01 04:17:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3523729d-25fa-3417-bbdf-01736b65acb8 | -10.72301 | -46.92888 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7e04cef7-998c-371d-ba54-f8f990e5d3e5 | -10.2715 | -46.22194 | 2026-06-01 04:17:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45f2288e-3356-3e08-b8e4-1044c7153195 | -10.8045 | -49.39358 | 2026-06-01 04:17:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a079bd83-e01d-3ca5-a794-05d4be6abc15 | -12.31391 | -47.90725 | 2026-06-01 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbb7b885-4d4b-3034-999c-0778cae47c92 | -7.17501 | -44.07122 | 2026-06-01 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5d177f3-46f3-32a0-a527-4bc42b9977d4 | -12.31027 | -47.90656 | 2026-06-01 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc61afd2-1311-3661-8592-466af2350004 | -10.0571 | -51.66809 | 2026-06-01 04:17:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5672aed9-5ae6-31fa-befb-76ef86e7beae | -12.40719 | -47.49805 | 2026-06-01 04:17:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 641afd62-1c9f-335b-812b-d322fb2bb6fb | -10.80727 | -49.40168 | 2026-06-01 04:17:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fed1403-6c10-3974-b09f-6bb7051b0b29 | -10.75549 | -46.90889 | 2026-06-01 04:17:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dfef99f-a963-3546-825f-d4ce49ba0aaf | -10.76258 | -46.91008 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7569921-a52b-38ff-8ee4-bc7635ba1f9c | -10.72943 | -46.93413 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17da26ec-4b10-3e3e-b691-e863ed2bf86b | -10.84834 | -53.75166 | 2026-06-01 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fd96cd9-f325-3973-a3d0-426ce1df022a | -10.72014 | -46.92424 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2f5dcd8e-a811-3b94-9179-eb9eb60689b0 | -11.33329 | -47.18279 | 2026-06-01 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd41d9c4-2c7e-36b7-9201-31ca4e388535 | -6.99399 | -42.87806 | 2026-06-01 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 55448b5b-2d9e-33d5-8705-6af2a34dee2b | -10.85379 | -53.75262 | 2026-06-01 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b66c0b5-70c5-3131-b889-4558f5bba412 | -10.84698 | -53.75252 | 2026-06-01 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17554d92-ad17-32fd-80f7-058f8cc38d04 | -10.72791 | -46.92136 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cb7a02a-89b4-365f-9cbd-9c6cda45972e | -10.73011 | -46.93009 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86219256-e35b-3132-93ae-bb92d89c1318 | -10.85243 | -53.7535 | 2026-06-01 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba177778-3176-3d52-949b-efc2e5695a2d | -11.33685 | -47.18343 | 2026-06-01 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24b1446b-7931-3969-9524-ce9bf05b57ef | -11.62925 | -52.56535 | 2026-06-01 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d6fa08a-2100-3ee7-8548-3f68e832683d | -7.97146 | -34.89784 | 2026-06-01 04:17:00 | NOAA-20 | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 08bc98cf-b00b-3ce0-bafa-04f4d906f5ee | -5.09961 | -46.94756 | 2026-06-01 04:17:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b648c37-cc03-3996-86db-61edeec203c6 | -12.3183 | -47.90352 | 2026-06-01 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d30fb58-44af-333d-b042-300058cf2c2b | -5.61191 | -37.52996 | 2026-06-01 04:17:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9cdcdf9b-d098-3557-8558-3b7df025065f | -7.31435 | -46.99813 | 2026-06-01 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b70c02be-a714-3252-8400-46e0bd9b6591 | -10.80663 | -49.40533 | 2026-06-01 04:17:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 007f4169-4528-3604-8bf8-d0734278a59b | -10.96964 | -49.43072 | 2026-06-01 04:17:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README2.md)
