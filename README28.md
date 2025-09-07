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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c9595ca-57e1-3b19-b549-e6b0df47060b | -11.34681 | -43.51323 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daa3af23-7e16-3757-8f01-6c51752bfd52 | -8.93833 | -48.65129 | 2025-09-07 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a13d80d-b01b-31d3-a00b-1e7e6fd29d3f | -7.60536 | -44.6681 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01ead6eb-4a12-3ba7-a070-01b8c35f5b46 | -10.60693 | -44.33236 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d43b4e51-f648-350b-acf0-e156b43b5411 | -7.73465 | -50.31325 | 2025-09-07 03:57:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7feba0f2-b2b0-343e-af00-93af364ad926 | -8.04297 | -44.06892 | 2025-09-07 03:57:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a6a56cb-d9e0-3246-bda8-0124b5474109 | -6.87221 | -45.55843 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2789e412-6c6f-38ad-9f0c-1ad7f8508ea0 | -12.79346 | -48.02262 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3c0bdf9b-2005-3f2a-9044-8ed1877717f8 | -10.58817 | -48.47329 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 274b2d17-8b7c-39f8-835b-24c9adfbb46a | -8.50104 | -45.10352 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fecd90b-3295-3837-9f8b-ef8dad056d9d | -6.21242 | -44.39054 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cdf6f1b-fa48-30b6-ba69-75072a8f8761 | -12.82048 | -48.01576 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad003af3-4137-3611-ba4f-bb43bb8a5ae4 | -11.15745 | -48.37267 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf991349-902c-3bf0-a15c-81190d1a89bf | -12.79955 | -48.01762 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 466a8ac0-6bc9-3cc3-9c76-42ec8bf760e8 | -11.40608 | -43.63765 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 844b38d4-115d-3dc3-a33d-4f3e2b30d3fe | -9.98005 | -51.66593 | 2025-09-07 03:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 033fc0b3-c82d-3dd6-af0a-9766d8d0d09e | -13.04452 | -48.08048 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5355ed61-6321-32a9-9cca-968ef7aa69e3 | -6.22416 | -43.29886 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce68cbdd-6799-3eee-8f32-4c8cef6bd4fa | -6.32141 | -43.28928 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc6c85a3-46df-3d25-8bd1-eed50ceaeb23 | -11.40882 | -43.59886 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0a533fb-44b5-3648-8f5a-9e13be80c101 | -8.42848 | -47.30664 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28fa7674-cebe-3b9d-88df-646b6206f9e0 | -12.79842 | -48.02358 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0f9f15db-2be2-3beb-8b98-d6b78a19703d | -10.74541 | -48.18583 | 2025-09-07 03:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 155022fb-437a-3162-808d-cc383040e13f | -8.68465 | -45.31218 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40fe15de-e53e-3ca9-a87e-4d039c6b998c | -8.48056 | -45.17634 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 976d260e-4f7e-3cfe-8ea1-54581eabad8f | -12.54625 | -48.07832 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3b37c19f-3803-3b6a-98c7-9a02f2d54784 | -13.68898 | -41.36968 | 2025-09-07 03:57:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a4ca2a1b-7e94-3f55-b00e-4f5748e5079d | -6.60516 | -48.06008 | 2025-09-07 03:57:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f74c3bbb-f9f2-3b31-a3ed-fddcbfd097de | -10.58346 | -48.46912 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5642c6a-f158-3ab4-aba2-639fbefd0317 | -6.26616 | -43.4977 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d5dd4eb-533d-3417-953c-bdd64a578a88 | -13.0347 | -48.07798 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd8bdb3a-2857-3c43-88a0-50f128876013 | -11.4069 | -43.63287 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fcafad3-cbce-31ec-a644-16bf35f38425 | -13.04014 | -48.04885 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b27c87b-1f79-3945-a861-7f117fb361d7 | -8.4336 | -47.30753 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7c24102-cc74-3ce6-92e4-9d4308c91962 | -12.5761 | -44.62855 | 2025-09-07 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6aa1e9f3-7c50-3763-802c-482b3f0088c4 | -6.1949 | -43.59475 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4d633cb-35d0-3385-88d3-6cfbf4a9fcc5 | -9.83109 | -46.54667 | 2025-09-07 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dcceabe-3232-32fc-8d34-8d9891f6b066 | -6.34255 | -43.7931 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 776049af-1ddb-3407-888a-8554e7312380 | -6.8034 | -47.07302 | 2025-09-07 03:57:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd1672af-d9d3-349b-9c16-8709a8f3b5c9 | -13.02989 | -48.0762 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b1fbd3c-4117-31e5-a48f-cddedb751cc1 | -7.5966 | -44.69249 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 799b47f2-5d0e-3cea-8da0-b92c5e75335e | -6.13093 | -44.25818 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7b247a8d-50d2-388b-af3b-74d880344b55 | -10.73625 | -44.35632 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 291d15ba-2e8a-3e28-8868-7ebbdccd0535 | -6.30041 | -51.41725 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 44460af3-7bbc-302c-a04b-8e4403be4ac9 | -6.18798 | -43.36963 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5fa3561a-db4c-38de-a0d0-39e2d43b61e3 | -7.75572 | -48.81345 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 273f0626-243b-3fde-9e9c-0f489000782f | -7.74216 | -48.82289 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4d22346-0209-30c8-b97a-338196eab2b4 | -13.03051 | -48.04827 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a0d3a5b-5d47-389e-99dc-e3f38a289996 | -7.00574 | -44.93946 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91f9cd14-a60e-3ba7-a550-c29ff27f168a | -8.91273 | -45.82181 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff1ae9a4-59b0-350c-9cb2-26574dc693bd | -7.32517 | -43.94088 | 2025-09-07 03:57:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 181e6a7d-f568-3de1-b265-2960d67130a8 | -11.34301 | -43.51255 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3aa8488-e42e-3386-aab1-c2f22a3b183d | -6.2127 | -43.58993 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9398928-e081-31c4-bc39-2a2b05e0afa6 | -8.91816 | -45.81794 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 748352e9-a40e-32a7-9c6f-7e3eb9b3efb3 | -10.78443 | -47.7461 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccdc3a2b-f04b-3965-bbd7-0a2476026902 | -7.01542 | -44.96384 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a1d5d7d-0c27-36ee-8a9f-7eec234165ce | -6.38786 | -42.99764 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d24d52fa-afb4-3b4c-8519-7c3a691b6a1f | -10.6063 | -44.33595 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bec5ebc6-f3a9-30be-ae78-19619584f102 | -9.35118 | -46.51354 | 2025-09-07 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 431e1c3d-0f31-30d5-961a-36d77ebccabf | -8.3415 | -48.27359 | 2025-09-07 03:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd486ed9-6c96-3b07-b7f4-e0bfaf029923 | -6.96286 | -46.51596 | 2025-09-07 03:57:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eba99d10-901d-3213-8563-809e14a79d33 | -8.50351 | -45.06425 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e75ce9f-39b4-3fc3-9418-e526d7340555 | -10.61097 | -44.3331 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6766d30-eb70-3349-8934-6a2b9772ada6 | -6.20423 | -43.53971 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80582a1a-af6f-35d3-9546-b2b229b3c720 | -11.58854 | -47.73192 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a16d109f-047f-36e0-a786-527a1c903928 | -8.91449 | -45.81211 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71c12c01-881d-3ada-95ac-9b90997dc498 | -11.5855 | -47.17786 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c353aef-f11e-3b64-8837-8eb12c38cb58 | -11.40092 | -43.62185 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 722e522c-ad84-371b-ae2f-af4a068b8bd7 | -7.43658 | -44.9433 | 2025-09-07 03:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32029001-40f7-35bb-8fa8-a896f558ca3e | -8.03987 | -44.03784 | 2025-09-07 03:57:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2ae2c6b-c121-3526-94e4-63a701fe3be6 | -6.55345 | -42.94508 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90ff2f50-73b7-3895-bf90-b3b687c85138 | -9.08918 | -46.99088 | 2025-09-07 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad74d92a-0f28-3ea0-a7f8-9b02abc0b7be | -8.68717 | -45.31062 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96d98623-f182-3f6f-a9a3-6215cdccacf2 | -8.44695 | -40.60403 | 2025-09-07 03:57:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2ee85c7-8c22-32c0-a8b2-4ee1cb85bd32 | -6.27558 | -43.4917 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ac27555-06c8-36b5-80ff-46b78824ac0a | -5.69384 | -49.19649 | 2025-09-07 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4604756d-7ec9-32c1-a86b-3573dd980a54 | -9.83485 | -46.55308 | 2025-09-07 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b93e4522-b649-31d9-a29f-51c867b334eb | -6.16456 | -44.24285 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83a45155-9dc9-3084-b58e-d5fbccad56b7 | -7.34222 | -44.31641 | 2025-09-07 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2a97535-dfce-3084-85e0-e9de31480c95 | -7.28836 | -42.5216 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7f662f13-d248-3bd0-a364-d7db1703861c | -7.01971 | -44.97613 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8905e415-1cab-3987-8a05-34ffb0f23683 | -13.02934 | -48.0517 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68fd4c00-879b-3ab9-bdc0-13a451e720bb | -5.69305 | -49.20095 | 2025-09-07 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf8fa861-cd32-3ca1-a49d-1b95673ef5dd | -8.03822 | -44.03829 | 2025-09-07 03:57:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6a701afd-a1eb-39e4-a774-4c06aaf83a3c | -12.22466 | -43.87023 | 2025-09-07 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f366ef9-bf09-321f-bde9-b81e6b66b95a | -6.60583 | -48.05637 | 2025-09-07 03:57:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5d1a83e7-e09c-3f24-be8a-41747b9c4ff3 | -7.97505 | -44.94837 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e9eb88f-9652-37b3-9ad2-1f797fc79d3c | -7.59148 | -44.69615 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d077495c-91dd-3939-babc-1619fcbc0b16 | -8.6828 | -45.28262 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce355062-461d-38c2-b8c7-c20b12207396 | -13.03614 | -48.07215 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aff76951-7078-3fab-9103-64ddfc5cca2f | -6.24398 | -43.28018 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8414534e-a143-3045-bdb7-648e4a3d8796 | -6.19427 | -43.5985 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38b03cb1-0e14-37cd-8814-b305f5fbae8f | -12.92958 | -48.03651 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b25dd309-d02d-3944-aa90-62c7abb71acc | -10.78497 | -47.74319 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40fd4b9b-3f34-317a-a503-c97072f07af5 | -7.60968 | -44.66893 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c691936c-4ff7-33a5-8d57-212f65acb6c8 | -10.35321 | -46.45729 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| f8f2ea21-a197-3f0f-87b9-edcfac1cbdb3 | -10.10332 | -48.1595 | 2025-09-07 03:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11fe3e56-8ffe-31f4-8cba-5177226634f7 | -7.28991 | -39.21729 | 2025-09-07 03:57:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| eb314cd8-9903-3fa8-8b61-8b78e03c5377 | -6.47114 | -43.98057 | 2025-09-07 03:57:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 39f11cca-8e37-3179-a5ba-45b14dc5f31d | -8.35306 | -48.27203 | 2025-09-07 03:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
