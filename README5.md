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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 842616c5-2c92-38e1-8ed9-5128adb33096 | -13.9084 | -43.8857 | 2025-08-29 00:31:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ae22c71-23f7-3bb1-b996-cff201790705 | -17.549299 | -46.603199 | 2025-08-29 00:31:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a8d460bc-b8db-3ad0-8e95-a29f8e7756b2 | -5.6993 | -45.966599 | 2025-08-29 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2015f49-1de7-3842-b9e3-1258e01851dc | -6.4405 | -44.5695 | 2025-08-29 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26afc198-c5f4-3e6c-a61b-62796ce4bc9f | -7.0333 | -44.6786 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3604c2d2-0732-3184-8f8e-c324f30b8423 | -11.3382 | -43.5658 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69ae806b-c8ee-3e20-9398-a724626ca7d3 | -6.552 | -43.937901 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a08d0ab-4e9e-3047-a864-0153ceac8b7f | -3.9903 | -47.875401 | 2025-08-29 00:31:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5374847-45ab-3bce-8e7b-61a69eebd4aa | -13.4254 | -46.9674 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45180eef-ba64-3108-ab90-27aa148aaad0 | -6.816 | -44.319199 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89b7a907-2633-34f4-a37b-349ea5765a95 | -7.6262 | -42.704899 | 2025-08-29 00:31:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dddb1a48-2286-3d93-bd1a-2c398d1768a1 | -11.33 | -43.575199 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1e6a80c-112b-39ad-8039-af9ecde0ab3b | -7.6336 | -46.539101 | 2025-08-29 00:31:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a311d1f-3d33-3a73-931c-ddb63d7fc132 | -13.5028 | -46.849701 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2431a13d-f9e3-393d-bf01-ec58ae20471b | -12.0466 | -50.6306 | 2025-08-29 00:31:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c809d8e2-2594-3157-9092-6f1e50444b27 | -11.3284 | -43.5681 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 35bd2ab8-f324-3008-822a-447d646b22f9 | -12.7065 | -48.161598 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74ed0d74-3a07-33ba-8acc-3b82807df772 | -7.236 | -45.425701 | 2025-08-29 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22c05792-5706-388c-bd71-a3f0a0d4662d | -8.704 | -50.366501 | 2025-08-29 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28faa0d9-7304-3b0a-8fc6-78bdb1ef66c9 | -5.7855 | -42.603901 | 2025-08-29 00:31:00 | METOP-C | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c142499f-4ef3-3a52-9496-e20bea438f7b | -7.4337 | -42.065102 | 2025-08-29 00:31:00 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 75ea84a2-639a-31fe-8155-14e542cfb6a9 | -12.8297 | -48.1632 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0393fd3c-e484-3f58-827a-5ea9a3e1212f | -13.6358 | -48.200401 | 2025-08-29 00:31:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cd78f0ac-22d9-3da9-ac0d-44389f9eee97 | -12.8237 | -48.183399 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d5bb492-4ab7-3bd4-b82b-3f65c4f44ffe | -20.702999 | -43.937099 | 2025-08-29 00:31:00 | METOP-C | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc0337c7-bc7d-3350-9f40-561186e84f2f | -15.1295 | -48.107899 | 2025-08-29 00:31:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0e713663-efe9-32ed-941f-4856f05c6093 | -13.6715 | -46.871201 | 2025-08-29 00:31:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 29ce8ca2-b88e-3a6c-a258-e22a295e297d | -7.219 | -45.306702 | 2025-08-29 00:31:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6283991-2784-346c-b9bc-5618695f0f6d | -10.8611 | -47.4972 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f13187c-1156-3eaf-be3c-8c111cf9ef70 | -17.049999 | -45.878799 | 2025-08-29 00:31:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2384a00d-39e4-3ebd-bbe1-c68e23a70cf8 | -13.2036 | -45.292301 | 2025-08-29 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4cd2891-8404-3099-9ebd-361e962976de | -8.4935 | -43.6749 | 2025-08-29 00:31:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa72c879-2887-3ca0-9e8d-7bd4e0fc72f0 | -11.348 | -43.563599 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce16407c-d67d-32d6-a02a-211feb104ccd | -7.058 | -44.383701 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7db57614-1e47-3100-8c1f-b47ef530726a | -3.9271 | -47.688499 | 2025-08-29 00:31:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c8d2b47-1aa9-36a9-85bc-30b773b1e90d | -11.1262 | -45.122299 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e72b2294-1d62-36ef-ba0c-3b9b6cc0cd59 | -10.0221 | -51.0895 | 2025-08-29 00:31:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b1e741a-972c-36f2-9ed7-55e5485e308b | -12.4084 | -46.491501 | 2025-08-29 00:31:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39cda70d-9c9c-3e61-9f64-f6554f5154b6 | -11.3332 | -43.544399 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da1c9272-9b1a-3296-9a16-0936fbf8067f | -12.0964 | -44.7174 | 2025-08-29 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93a23a4d-8605-3da6-8279-838a13ba19df | -6.5433 | -42.665798 | 2025-08-29 00:31:00 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b3b9be5c-550b-32e0-9b58-52ff5e55a145 | -18.7349 | -49.145699 | 2025-08-29 00:31:00 | METOP-C | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 47bb928d-6a53-3c4e-ace1-541fbb7f18d5 | -13.4318 | -46.9492 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ccb50b84-cd7a-3473-832a-2b37680246f0 | -7.4239 | -42.067402 | 2025-08-29 00:31:00 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 825fc6b9-d9fd-3162-ac5e-ed1b770ed401 | -13.5241 | -46.853401 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df2e7090-6e89-345e-9fe3-8d51557e8863 | -12.0394 | -50.644901 | 2025-08-29 00:31:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b3ba3f8-c659-35ec-a3c2-b45e865db7c9 | -15.6072 | -48.046299 | 2025-08-29 00:31:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| dc97490d-4b61-326d-8768-58946782e46d | -20.2866 | -41.299801 | 2025-08-29 00:31:00 | METOP-C | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ab6d873-d1ff-3213-9559-e74adbe79c6a | -13.5552 | -46.8549 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9b297657-7362-3724-a1d7-ad9444e2194c | -3.7355 | -48.931599 | 2025-08-29 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bc2f6fe-97ba-3fa9-b8fb-00322ef45c76 | -11.0951 | -44.757198 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4c6c94f-6a05-3735-879c-5b2f2ad80769 | -7.6281 | -42.712898 | 2025-08-29 00:31:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ee1c495-6d02-3246-bbdd-a5eb2fcaea32 | -11.4664 | -47.306099 | 2025-08-29 00:31:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 122d12f1-9fdb-333f-83b2-8557d3cdf55e | -12.6967 | -48.1637 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1b44229-6da8-3dfc-ba7b-76b83855bc78 | -10.8593 | -47.489201 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef5b4dee-3bbf-3516-966f-7643b1bc555f | -8.4377 | -43.657001 | 2025-08-29 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b87d718-c1c0-3a08-a30f-5dcc794cc067 | -8.754 | -47.4034 | 2025-08-29 00:31:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 064ca97c-c869-394e-990a-2f98a33fa5b5 | -10.0345 | -51.099899 | 2025-08-29 00:31:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa9ab866-6d95-3c54-b259-2c43ac7833b1 | -4.4072 | -40.488098 | 2025-08-29 00:31:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 457a8bdc-a53b-32be-bb19-b110d0f678f3 | -14.2603 | -48.056702 | 2025-08-29 00:31:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e2d8c26-8413-35c1-8128-30e6b3e9888f | -2.9904 | -48.598801 | 2025-08-29 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1a51549-08cc-3426-95b0-eb6ba1fea19a | -17.5529 | -46.620602 | 2025-08-29 00:31:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d57e69d3-693a-38fa-bf6b-88b23751785e | -12.6948 | -48.154701 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46d6fcb4-213d-3179-8570-104efa7c11d0 | -4.1048 | -48.1982 | 2025-08-29 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b9cdbda-7621-39c7-97f7-609ccd9be05c | -24.179399 | -49.568501 | 2025-08-29 00:31:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 0cef6731-a528-3f61-8dff-7ce76459867c | -7.4027 | -43.3806 | 2025-08-29 00:31:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78c5db23-0d14-35b7-a9bb-70d8613abda5 | -11.0837 | -44.752499 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4283b64a-14c7-34cd-b23e-b7b424d7c05a | -11.0919 | -44.743301 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c56cb4cf-c493-3697-87f6-150c44e8589f | -13.4139 | -46.961498 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 28513c3e-4ba7-39d8-849b-75a12f840862 | -5.6247 | -45.013599 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb4f0a2c-d8f8-3037-8620-1f24be0a0779 | -6.2739 | -43.807098 | 2025-08-29 00:31:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d6c99e4-a1dc-398e-9cd5-de7450afe61b | -8.4675 | -43.696201 | 2025-08-29 00:31:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8adc391c-1ffe-3a75-bd09-30d9f08351d8 | -11.312 | -43.541901 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 538e8b33-d48c-3084-bef4-0c2923f4de6f | -13.5672 | -46.910999 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1f4f6aa9-6611-3987-8bc2-b2a494c35d9c | -22.1441 | -46.668499 | 2025-08-29 00:31:00 | METOP-C | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b8ac9ba-78a9-3166-a6b8-6d29fd7af359 | -11.5868 | -46.262402 | 2025-08-29 00:31:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27fe0325-c730-315c-a1ea-dbb3cb95d6fc | -11.5803 | -46.279202 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62c2a9d2-4077-36e4-99a5-d1edf621d18d | -5.7973 | -42.6101 | 2025-08-29 00:31:00 | METOP-C | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d8b07054-ed1b-3e29-93c3-9a11c77a8c45 | -9.3992 | -48.231499 | 2025-08-29 00:31:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6861d35d-e9cb-35b9-a969-3cf08c477c77 | -6.7196 | -49.446098 | 2025-08-29 00:31:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 639baaec-b50c-3cb3-9577-ed03a0bda996 | -7.0563 | -44.376598 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d358e3d0-d1a4-38e7-9908-0aa51be39bb2 | -12.3231 | -47.043301 | 2025-08-29 00:31:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a37d448-ac75-3ae5-b6eb-5f643a2aac64 | -15.0623 | -48.377399 | 2025-08-29 00:31:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f3a452b-8c1e-3cb1-b269-66f05e3c82b6 | -12.0687 | -46.630402 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1340cd5e-8e5e-3d2b-bbf3-8b73f45a4b9e | -6.2091 | -43.000801 | 2025-08-29 00:31:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d24e3d8-3076-315c-bbdc-faf4c2e40920 | -3.7453 | -48.929501 | 2025-08-29 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64cf7d71-fdda-3219-8b7a-37e36a62b221 | -13.4514 | -46.944801 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 883d1ca2-7e7c-37af-8418-8eb3e1f75d9b | -8.461 | -43.7131 | 2025-08-29 00:31:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c18ed74-cdab-3071-9271-39fbe3819392 | -6.8887 | -43.6105 | 2025-08-29 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c521ba25-0806-3a7b-ad8c-35c7540b09d2 | -11.787 | -44.671398 | 2025-08-29 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6028848a-31ea-3128-baec-48a3d5b92f07 | -13.1922 | -45.287399 | 2025-08-29 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fc51460-1bd0-327d-a327-0520edc98a5c | -11.2446 | -45.007702 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6438aeb2-0675-3052-a0c6-165a959dcbab | -7.6461 | -42.657799 | 2025-08-29 00:31:00 | METOP-C | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 09c0af3f-e878-31ab-8036-d45f77d3064a | -13.445 | -46.9631 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec5bcd2-bdc1-3fca-8411-23e3deba50ff | -7.0758 | -44.282299 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b26fe84e-25a4-30d9-8064-87805ce137af | -11.5573 | -46.361198 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4bc5b7d-4139-37f5-a28d-aa0bf0793843 | -13.411 | -46.995899 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5855a6f-0460-370c-a011-79d76328f5a5 | -11.3545 | -43.547001 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1422e656-704a-30a5-b622-8fb5efb5fb33 | -14.3717 | -53.129101 | 2025-08-29 00:31:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 696997ba-2e34-33bf-8163-b0fce693c949 | -6.4942 | -44.400299 | 2025-08-29 00:31:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
