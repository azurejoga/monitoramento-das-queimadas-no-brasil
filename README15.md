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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 675cfba2-244d-3cd1-8788-7b859a595931 | -3.3098 | -46.0724 | 2024-10-11 00:55:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 30b61f7d-9139-3974-909c-b809b7c06ade | -3.614 | -44.7783 | 2024-10-11 00:55:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 130b8539-80df-3eaa-8885-b30eddec193d | -4.0962 | -48.2523 | 2024-10-11 00:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 31c1f9a8-9673-31d0-be00-c9de693bb4e8 | -4.0963 | -48.2307 | 2024-10-11 00:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 39da2fe0-cc59-3ce3-b30d-83a3f5854a37 | -4.1146 | -48.2731 | 2024-10-11 00:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 94e468e8-1357-373d-bb2a-72439b648477 | -4.1148 | -48.2515 | 2024-10-11 00:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 334.1 |
| 5ceca78d-8b75-3a05-8c41-ced0f61b8b3f | -4.1149 | -48.2299 | 2024-10-11 00:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 62b3ed4c-52d5-3c5b-9b52-a7ef41d66cc0 | -5.1725 | -48.2848 | 2024-10-11 00:55:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7abb488a-c474-3ccc-bdb7-43bca0f2ac0d | -6.1299 | -47.2884 | 2024-10-11 00:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| b8fc8145-980e-3c20-8e2a-084858028eaf | -6.1301 | -47.2664 | 2024-10-11 00:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| cac35b57-5262-3322-bceb-37357e6313eb | -6.5404 | -60.0259 | 2024-10-11 00:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 394b0332-3966-3d81-a0df-49948a44bc2f | -6.5589 | -60.0252 | 2024-10-11 00:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 00725419-135d-3cf2-af28-c171b16379d3 | -6.747 | -59.3259 | 2024-10-11 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a6fdc62e-20c2-3958-8756-ceda100f5e59 | -6.9097 | -47.7572 | 2024-10-11 00:55:45 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 20014c4c-194a-361a-961b-50f2063efe88 | -6.9284 | -47.7558 | 2024-10-11 00:55:45 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 326.2 |
| 11cf5d1b-1e8b-3c41-a858-9d72750b7a54 | -6.9286 | -47.7339 | 2024-10-11 00:55:45 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 7542a6e3-2078-3cd8-a450-26f03ce1c48e | -8.4231 | -55.4704 | 2024-10-11 00:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1f05e256-1505-311d-8102-331e81ee8f7e | -8.4417 | -55.4692 | 2024-10-11 00:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 10038c56-336a-319e-8ae1-dafcc0dcf588 | -9.5303 | -42.9946 | 2024-10-11 00:56:00 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 0668c83a-a82d-3d35-b6b7-e676c70faa77 | -6.4462 | -38.81366 | 2024-10-11 00:56:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 3bff1f05-4788-39b1-95e8-c516fb7d4fb1 | -6.44009 | -38.82209 | 2024-10-11 00:56:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 7679cb3c-04ca-376a-b685-06c2e36c24d6 | -3.70288 | -40.71287 | 2024-10-11 00:56:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 4e05551d-5c3f-3d28-b991-be639880bb78 | -7.46917 | -41.2564 | 2024-10-11 00:56:00 | TERRA_M-M | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 9a79ed0e-d262-3321-9693-da671167453f | -4.4782 | -42.89171 | 2024-10-11 00:56:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 54576c2a-dbbc-3587-8447-5846fae5c618 | -6.69832 | -43.18775 | 2024-10-11 00:56:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 4871f1e0-b981-32ac-86ec-6e6eed632895 | -6.69477 | -43.18259 | 2024-10-11 00:56:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 69424319-a559-33b5-9d67-09b47a3d1bdd | -8.94143 | -42.593 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 45fd172c-b163-30a9-9eeb-335f11dc4163 | -3.37584 | -44.37091 | 2024-10-11 00:56:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 24d4812b-5e44-39b3-99f0-19746256ec55 | -3.36469 | -44.37258 | 2024-10-11 00:56:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 3272e808-81a5-32d8-abd4-b25a93a1dbac | -4.0399 | -44.26795 | 2024-10-11 00:56:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d2dc2ea7-5a55-391d-8e32-f9fe6d6a0582 | -3.8509 | -44.23416 | 2024-10-11 00:56:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0a48c67d-ea47-34ed-a6f5-a10da924caeb | -3.8034 | -44.0658 | 2024-10-11 00:56:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a5001724-025c-33c1-94f7-80ee533a620a | -3.80189 | -44.05941 | 2024-10-11 00:56:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| b9ded7c5-c2f6-3948-a133-b72343418711 | -3.80125 | -44.05064 | 2024-10-11 00:56:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 889dcd8f-feea-33d8-94b3-2dec487cbc4f | -3.79962 | -44.0443 | 2024-10-11 00:56:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 82670955-c33b-34cb-83e7-6c9f47a0a72f | -6.49049 | -43.87997 | 2024-10-11 00:56:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5d50a651-085d-3b91-a360-4e4c0e977551 | -6.47952 | -43.88167 | 2024-10-11 00:56:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 545ac426-f068-37e7-865f-f3bf6a3f3e20 | -6.45236 | -44.38904 | 2024-10-11 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b42c951c-7511-39dd-9f6d-6164f8dd44d7 | -6.45041 | -44.37602 | 2024-10-11 00:56:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 7915b433-ac55-3f5d-a5f2-a442d6c60699 | -6.44552 | -44.27052 | 2024-10-11 00:56:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9b6e5d67-e4d9-3e1d-a99a-501029bf495c | -6.39969 | -44.36358 | 2024-10-11 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 47ea8c1c-4b82-321f-8ffd-a40661612c02 | -6.21544 | -44.11129 | 2024-10-11 00:56:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 514ecc8c-12ad-3f49-a201-e664919f1c4b | -6.19619 | -44.37981 | 2024-10-11 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| f121be47-489b-36ff-949c-ec5f66a1575b | -6.07278 | -44.64731 | 2024-10-11 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ce982736-7ffd-3eda-b1f8-971589c24384 | -6.07096 | -44.63482 | 2024-10-11 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d5997da1-ebc5-39ee-9848-90c3308640fb | -5.88685 | -44.85302 | 2024-10-11 00:56:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0632fb8e-6c2e-3bb3-a874-f1b6b0b6c689 | -5.8135 | -44.13167 | 2024-10-11 00:56:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| edcd87aa-1f83-3a3f-bec3-2313085dea7f | -5.74156 | -44.34372 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 64ebbe44-0f3c-3f09-9c8b-65762994ffdf | -5.73961 | -44.33035 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 89a7f995-1c1b-34c1-9e7a-fabe17e7a2b7 | -5.57233 | -44.12353 | 2024-10-11 00:56:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 98cee4f9-fb3c-32ac-8001-d2a927ce203d | -5.28326 | -44.2056 | 2024-10-11 00:56:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dc4533e6-e9ae-3803-8a83-02701d1e6a1f | -7.82674 | -44.19385 | 2024-10-11 00:56:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| fcdb4bbe-c3bd-3618-86e8-8ad4bb44db8f | -7.58494 | -44.77463 | 2024-10-11 00:56:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 618ea5f3-7a03-3731-b118-f06de8a0eee3 | -6.95955 | -44.8401 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0978d643-2e45-3e56-bca6-ed88428cb137 | -6.94978 | -44.83526 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ce636848-f258-3f99-906d-f3816c064fcd | -6.93537 | -44.60929 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 15b4c4fb-8a57-3934-b545-0e8d517998f1 | -6.58382 | -44.18279 | 2024-10-11 00:56:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4ea91e05-f7e4-346f-9863-7bf75c11d22a | -6.57844 | -44.17665 | 2024-10-11 00:56:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9929e784-322b-3643-8971-73640c428c9e | -6.56665 | -44.24566 | 2024-10-11 00:56:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a99716ff-3d0a-39bb-94c1-54f6d921f4b3 | -8.40304 | -44.022 | 2024-10-11 00:56:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6c8d8b50-5c79-3601-a85f-0930dacb628f | -8.40106 | -44.00906 | 2024-10-11 00:56:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8ffde196-5037-39c6-a30e-930f2e3d4277 | -8.39798 | -44.02923 | 2024-10-11 00:56:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1f36666f-7516-39a5-b5ee-41d39dabbe18 | -8.36171 | -44.07423 | 2024-10-11 00:56:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ed3ee623-1544-382a-9948-fa030a119fe6 | -3.60886 | -44.79387 | 2024-10-11 00:56:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a384ec10-64a0-307d-ab42-5c1d73d5c3c9 | -3.81074 | -45.4921 | 2024-10-11 00:56:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3de511ef-fb5d-357e-97c0-4b20af158f26 | -4.91685 | -45.78297 | 2024-10-11 00:56:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 273709a3-d0ea-3763-a39f-a99f0a7ca79a | -3.81242 | -45.50397 | 2024-10-11 00:56:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 86e1ddb7-659b-371a-8aca-56645efbc316 | -6.33554 | -46.34123 | 2024-10-11 00:56:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 25758043-4618-35dd-bd75-3dd2b1c83e60 | -5.97722 | -45.74171 | 2024-10-11 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d1b659f1-c7f9-35b0-9927-152577e484d2 | -5.97363 | -45.73719 | 2024-10-11 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c728f450-f050-3d41-b9d6-cc72cac5e8b3 | -5.60817 | -46.368 | 2024-10-11 00:56:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ab8517cc-f5a0-3835-bea9-82ff25562d1c | -5.57078 | -45.41942 | 2024-10-11 00:56:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b9b88190-2143-33f9-9f47-c2062911d489 | -5.25733 | -46.22578 | 2024-10-11 00:56:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 268fa367-7611-378a-8abd-374485aeca7d | -5.24782 | -46.2271 | 2024-10-11 00:56:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e5d6a187-b743-35d8-8049-181a7e537565 | -5.22262 | -45.708 | 2024-10-11 00:56:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b711c904-90df-3592-afdd-2204ff5550e2 | -5.19859 | -45.95535 | 2024-10-11 00:56:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 25d75bda-ff0e-32b6-9551-88bce58d0f01 | -5.18892 | -45.95673 | 2024-10-11 00:56:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 37f0b3e6-9031-3473-b80b-99990c54b2a1 | -5.21188 | -44.91439 | 2024-10-11 00:56:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7a878dd0-c6cd-3c58-a1ab-f10d628541f1 | -5.21014 | -44.90214 | 2024-10-11 00:56:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a8df172e-a683-3114-b3bb-b92cb988d39c | -5.20783 | -44.90873 | 2024-10-11 00:56:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e6e872a0-3395-3530-b682-3333edf558bc | -7.82176 | -46.49056 | 2024-10-11 00:56:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7114af7f-69c7-3342-87ea-c7502edb4e52 | -7.82042 | -46.48111 | 2024-10-11 00:56:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 494fd168-b6f1-3477-bbea-5aa0858b27f3 | -7.39403 | -45.83598 | 2024-10-11 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2610b2e9-80a8-3f0f-a7e8-65e2e7f47825 | -7.39252 | -45.82571 | 2024-10-11 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0293bc28-175c-3797-80b0-22fbdbf8c608 | -7.28605 | -45.79539 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b26efc5d-153b-3512-9bae-aeec1368ac47 | -7.27354 | -45.37388 | 2024-10-11 00:56:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f345f073-0e8e-3014-8bb3-e9b6445c7158 | -7.25564 | -45.38768 | 2024-10-11 00:56:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 93ea5df7-f818-3785-90cb-bc41f6d6c287 | -7.23364 | -45.52948 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| c9f2e5d2-d494-3f5c-bf76-aaa1a7f67c24 | -6.95544 | -45.29424 | 2024-10-11 00:56:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f48826a8-9fbb-38d3-b3d2-004e1ae98bf6 | -6.80542 | -46.47215 | 2024-10-11 00:56:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 937a93bb-55ff-35ea-877e-3c2c6e02192e | -6.5008 | -46.16547 | 2024-10-11 00:56:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c93b905f-d519-3188-a005-f59b20b5380c | -9.35194 | -46.36195 | 2024-10-11 00:56:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0b108e7b-52a4-3a62-b202-239b78ee1658 | -9.35059 | -46.35249 | 2024-10-11 00:56:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6362573f-e8fe-32f0-bd62-b1428c3faa8f | -9.28019 | -46.56989 | 2024-10-11 00:56:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cebf2a3f-0c27-35f8-b87a-f6c891956fba | -9.2796 | -46.43656 | 2024-10-11 00:56:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c868dd15-3dd0-3255-9db7-23418c0d6b47 | -9.27886 | -46.56059 | 2024-10-11 00:56:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1f1b173b-ade3-3f13-b3b5-7e7921b8c7ed | -9.14594 | -46.40483 | 2024-10-11 00:56:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dc560e8f-5956-387c-910e-436fc9a3a079 | -9.1446 | -46.39553 | 2024-10-11 00:56:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7d266d96-d74f-32b8-bca1-f146638d108c | -8.70248 | -47.10889 | 2024-10-11 00:56:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a445b8c5-a344-39c1-b756-90a87c1c844e | -8.7012 | -47.09985 | 2024-10-11 00:56:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README16.md)
