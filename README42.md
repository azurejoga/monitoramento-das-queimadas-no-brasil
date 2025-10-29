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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a44eba6-1518-30bb-80e9-cf5bea3090c1 | -8.25708 | -46.34905 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb0d5389-fdef-3621-8ef3-55da9853a27c | -6.16826 | -43.75313 | 2025-10-29 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 00e3c467-7355-3f61-8cb9-7df2f69989f1 | -5.94489 | -49.10939 | 2025-10-29 04:23:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3aabacc4-b94e-3f72-8665-35b28b0826bd | -6.09322 | -41.77991 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a9720443-3702-3eef-b38b-f7f0a19771eb | -10.76334 | -47.89303 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b38ca5b3-6dc2-3224-bd91-f4a2da4e4ec6 | -4.91912 | -47.32409 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b74cf05-ca3d-3903-b93d-d7aafed1e1da | -7.66774 | -45.94871 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e309fa05-f3a5-3706-9718-b81388922562 | -7.14235 | -47.36309 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d13995e-6952-342d-ba33-169e7a3c876c | -10.98608 | -47.72613 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15cbaf8b-b72d-3eb4-b543-a945e8b860a4 | -7.26912 | -46.90015 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2c29ebc-c72f-3ade-9c1d-0aaffb1c7010 | -6.19047 | -41.58297 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6abd6c41-37fb-3542-a071-72cb3e1bff24 | -9.33291 | -46.24792 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3af9efd3-d112-3737-8562-56442ec7fbcb | -6.53109 | -43.57261 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81d121a7-477c-3d2b-823e-d3a629bf4176 | -10.5194 | -47.7353 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 029a4bd7-f151-334d-b28f-c09830a4ccab | -7.34811 | -43.90661 | 2025-10-29 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a50866b4-e315-3034-b230-ed64067c661d | -6.96101 | -49.40534 | 2025-10-29 04:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 356be4ea-ea4a-3c79-a0d4-3f350f82159c | -7.16991 | -47.26004 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42eca7bc-17e2-3b38-b444-381a389bd466 | -6.96131 | -47.73927 | 2025-10-29 04:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea5424f6-1f3c-3f9c-a43f-4b15e163fb84 | -6.11341 | -39.98856 | 2025-10-29 04:23:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| deea4b79-d4e8-3d11-bd05-b09c3fe12900 | -7.62932 | -46.9238 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06a3639b-6b76-3a52-a34f-fb7886a83b59 | -6.4989 | -42.23216 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b953c409-bdeb-3e95-bb4e-77a5e5fe6a06 | -6.12662 | -41.70591 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| aa9ecacb-986b-341e-ad27-c20053deacf2 | -6.14245 | -41.68169 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fb27cd3a-25f6-3f8d-8baf-9686c505438c | -10.98624 | -44.6839 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb2a7bac-3dc3-3de6-82db-5798f98fe44e | -8.00292 | -46.20942 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7149bb1-05d2-39f6-9251-72dcd70e4749 | -6.16293 | -41.66779 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a79a576a-320c-3c67-9bb7-b01df8701fe2 | -10.50751 | -47.72147 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41decfa4-2531-3cf6-be64-21bca6adfd60 | -6.49365 | -42.24306 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b82c6c59-3c1c-3551-b621-3e6a67404253 | -9.50654 | -46.96296 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c21cbe2a-716d-3dfb-9881-afd7aba8933a | -8.65135 | -47.21628 | 2025-10-29 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a01a0225-6e9e-3f93-b28a-2c6a29c01491 | -9.09385 | -47.81493 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91e254b9-4d85-3a83-a295-8829d49db092 | -10.90624 | -47.81004 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c952c98-8042-3327-8708-ac8715b3f661 | -5.80251 | -42.57341 | 2025-10-29 04:23:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aac0417c-cad6-39ee-b41b-7e4a3e3b53c2 | -5.66596 | -42.87468 | 2025-10-29 04:23:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4133a9fe-a28c-3ea8-9916-664f81c1d062 | -9.44484 | -46.89279 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c48578b6-b618-3137-9b97-919b66ec9f47 | -7.15398 | -46.62336 | 2025-10-29 04:23:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be51eb7d-e52d-35fb-882b-a16f2408a0bd | -10.87014 | -48.6253 | 2025-10-29 04:23:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a6874fb-4027-356b-9925-834964e59e11 | -6.15872 | -41.67132 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 621a5d37-97ef-393a-9de5-c8fa42937625 | -7.45292 | -49.40921 | 2025-10-29 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c66d6099-71a1-3b48-b43b-2669c98fafc6 | -5.61246 | -47.09335 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a01f466-4adb-3f20-8705-bf51faaedbf7 | -7.98729 | -47.23208 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d469daa6-5d40-3ce7-a722-730d5dc920c8 | -10.35537 | -47.56545 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f120d5f2-a049-3aab-a377-7f8b500fc7ef | -9.88426 | -44.88294 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f52680cf-9409-3165-b5e7-3f14c1bedb2e | -7.92257 | -49.73897 | 2025-10-29 04:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3202efe-606e-32e4-bc80-e5df05c8d930 | -10.94034 | -47.62218 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3566f34-2fed-36a3-bfbb-3df98e2d2df0 | -7.8614 | -44.23734 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51f0a71e-b2fc-3102-927b-0d9ecde88aa8 | -6.36502 | -44.18574 | 2025-10-29 04:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab42b9c3-0237-3676-83be-22ea58141356 | -10.6569 | -47.90236 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dd70939-91b4-3fbc-a2c2-76d219d1b596 | -8.25651 | -46.35263 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91022a2c-c908-3444-af49-8bce45db6edd | -9.94667 | -47.0944 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efcca015-934a-3966-a809-6c090d2e8a4a | -6.21951 | -41.8261 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 14d50561-488f-3147-918d-2663ad290f36 | -10.3718 | -47.14144 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1aa63d0b-11bc-3cd3-b75f-8fc4fa3d0ae3 | -5.97013 | -46.31887 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27c45f77-9aa4-347e-ab60-9cf0aa49d399 | -7.79811 | -46.44183 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 834cd248-351c-3f71-a3fa-1b29e1553891 | -10.61621 | -47.86832 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42669753-ed57-37dd-9dab-d632eec70d10 | -8.30869 | -46.82997 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b052f46-6611-3d75-9ced-9c3702b9e82b | -6.95351 | -47.74202 | 2025-10-29 04:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2f6a64e-90b5-31de-8d37-fc4d99251430 | -6.24411 | -42.55773 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 37796b15-68c3-3068-8477-43bc928f58f3 | -11.01195 | -47.56833 | 2025-10-29 04:23:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f34c19d5-dc77-3d5a-8cc8-08a1d12a7350 | -6.22675 | -42.53204 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b376b90d-0bd4-3ca3-94f9-f2697dbed340 | -8.32282 | -46.15463 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0d1ad09b-f6d8-3dce-a582-048607dbe7f3 | -6.14119 | -41.71465 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 92e0e4d8-cce6-3f2d-b7e6-62f718da31ed | -9.92878 | -47.67566 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64bfcb81-08bf-3b7d-bbbf-521f80474427 | -5.90522 | -42.50383 | 2025-10-29 04:23:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 57f6a34f-862d-3ed3-b78b-64696d4e80ac | -5.06943 | -47.10795 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75970819-95d6-3952-a6aa-033cb385d27d | -9.96162 | -47.13091 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb79eca7-4197-31db-8c44-6dffc000a8c7 | -7.28545 | -44.97639 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecbdef84-3372-32d0-bffd-ed2a88938196 | -6.93118 | -47.00238 | 2025-10-29 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 763641d4-d42a-3472-b591-fac517b1c686 | -7.37385 | -47.0297 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0929781b-0187-3d90-bd6a-e549f8b970a3 | -6.27596 | -43.75529 | 2025-10-29 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dea329b2-d588-3c8b-bf42-1498a14ec3b1 | -6.88033 | -45.03654 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a40e518b-e321-3eed-b940-d2a24dc7ff95 | -7.27781 | -46.89021 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ceeff1b2-7ffc-39bf-91b1-949756a0def2 | -8.89029 | -47.53626 | 2025-10-29 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d63ba6ec-fd50-3c4c-9acf-9f5a77140531 | -5.1768 | -44.91911 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 299f69e3-8775-3882-a5d7-a8554b238970 | -7.09933 | -44.09265 | 2025-10-29 04:23:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2835a9bb-1bed-3907-96ee-9964a87f296a | -6.30075 | -41.8828 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 1f618b4a-42c3-3563-86da-59f27965987c | -8.04027 | -42.5145 | 2025-10-29 04:23:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de220fcd-3745-3a12-b6a9-591c0dff1a11 | -6.6016 | -44.63627 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71337ef8-ee05-339e-ab7a-4aeb42bfc6ae | -10.65177 | -47.76044 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d220be6d-5895-370c-aa03-bcf8190207fb | -10.76705 | -47.82712 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2d3c92a-f7bc-3e5d-b7c1-6752b21c0cfd | -8.01021 | -46.20691 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56c37535-7d6b-3749-aa3b-8881c24acdca | -11.61356 | -43.35808 | 2025-10-29 04:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 536f3a53-a730-3bc7-93d0-e3b1f4e18b85 | -6.48662 | -42.242 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 52eb123e-211a-3672-aece-0114a3d16e8c | -6.14182 | -41.67892 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c9696e5d-c66b-379d-b06e-3d6d5a62fe38 | -6.11225 | -42.44863 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8cc529e-134d-3acf-ad65-28d007758506 | -11.17745 | -45.22222 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e28211e6-7a5b-3d92-a759-19bc67e54a74 | -8.14301 | -49.47895 | 2025-10-29 04:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97abe91c-39ae-3e1c-bb1d-fb65c8e4bce9 | -7.74522 | -44.7178 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 351513fc-0b2c-31c1-aa12-af41cae52a64 | -6.07663 | -49.35393 | 2025-10-29 04:23:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d8ffde0-f52b-3ec9-a70b-ce0a6949fdf0 | -10.81817 | -48.43363 | 2025-10-29 04:23:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f7fff4b-a8aa-343c-b705-0a47b1ce3279 | -7.30606 | -45.67674 | 2025-10-29 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11714b74-d95e-3a49-8408-b4e08c77ed6d | -6.10913 | -41.72404 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 763daf34-61e6-3608-8c82-bb949ae85bdc | -9.0875 | -47.80982 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1229087-3e8c-3718-82e6-9c63ff2cc75d | -10.20553 | -48.07787 | 2025-10-29 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f189fe31-5c1b-3e39-8da2-3cf692ea6d56 | -9.94924 | -47.12125 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04033f22-c543-3816-9ff3-3593b1d01612 | -6.1047 | -42.4514 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5be2897f-fe82-3ed2-b852-f8fadc69238b | -7.07211 | -44.95646 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3d36390-0f32-3e8f-9312-91d1dee3e5f6 | -8.25554 | -46.91968 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b68f5e0-9e01-3cc0-bcd9-4a0335dcf4b4 | -7.81748 | -46.40791 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 911dc557-e558-3969-bf48-300c4f6b984d | -9.33987 | -43.0899 | 2025-10-29 04:23:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
