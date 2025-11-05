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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10fe501f-5b0a-3853-a38c-ce40d6da7a5f | -5.3474 | -45.17469 | 2025-11-05 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c82f37ed-63c9-320f-b9f4-3d4d4a454ad6 | -4.66432 | -44.52802 | 2025-11-05 03:51:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddcd9d8c-4bb1-31c9-9a84-65ba43bd2ee1 | -6.63677 | -44.53579 | 2025-11-05 03:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06dccbc2-8980-3859-adaf-7488a13dbd54 | -4.45682 | -46.63602 | 2025-11-05 03:51:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c57a0473-14b2-385f-b4d0-f6274a833191 | -5.54961 | -40.75782 | 2025-11-05 03:51:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e15e13a5-78e2-3b00-a862-deef6b32e1a1 | -5.5115 | -41.15834 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f9d5e47a-5971-3edb-b672-af559e3500e0 | -5.47012 | -43.57961 | 2025-11-05 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 34585b57-56bb-3b67-8082-e0ad20bd3a13 | -3.82456 | -48.66774 | 2025-11-05 03:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3915a669-a417-3e11-bfeb-f94040d8210e | -6.13354 | -41.6272 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e89ce2a1-2995-36bd-b31e-6a4d075f6926 | -5.781 | -40.80973 | 2025-11-05 03:51:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c84d6b83-89e5-36cf-94b8-5eff8fd205d4 | -5.23716 | -48.50137 | 2025-11-05 03:51:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 54d95214-6f5e-3258-81ce-6e8e0087cdec | -7.28942 | -45.45498 | 2025-11-05 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c940b410-01b1-3b8c-9c3e-3bb50d94bc66 | -7.9408 | -49.73348 | 2025-11-05 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdb04c30-90e0-3798-a846-c3a09b15c7e8 | -4.09928 | -47.28718 | 2025-11-05 03:51:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bceb74d4-919c-3468-9206-8d7e08c99bbf | -6.12978 | -41.69822 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2246184b-9d1a-3678-a922-5cb3b734ea2f | -7.66764 | -47.41986 | 2025-11-05 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4e7ae7f-246b-3f1a-8a7c-7306de276e21 | -2.62583 | -49.23094 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e7de521-1e47-3504-a2e6-a720a021c5c9 | -3.64623 | -44.43446 | 2025-11-05 03:51:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ad8f2f1-6c86-3aa3-a163-dd247e8756e1 | -7.31072 | -46.29514 | 2025-11-05 03:51:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd985996-9add-3a9b-a44e-6648da7aa8da | -5.89091 | -42.91613 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dd552050-7ada-36d3-97fc-782bd27fde7a | -6.10605 | -41.71601 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5206031d-90e1-34ab-8492-88c0b28bf622 | -4.46728 | -43.22081 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 289d5ec4-248b-3fda-940e-b362883d4dff | -3.41394 | -44.4448 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbffd5a6-582b-3240-aa7e-e34c4c7ca11a | -4.76112 | -42.65394 | 2025-11-05 03:51:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 0a450cd5-5053-3792-9144-a71291696f44 | -2.8321 | -49.41886 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1bd91d1-fcd6-32a6-9523-58f97ca94455 | -7.03818 | -46.98588 | 2025-11-05 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6650e1ec-0580-3a9b-b313-bad0156dedc7 | -4.4077 | -48.97938 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c2bfcf5-5c63-3528-ac72-7f73399eba7d | -6.45495 | -39.11277 | 2025-11-05 03:51:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 134573d1-7a02-3789-92cf-d7b7ae98d6d7 | -8.04764 | -49.63647 | 2025-11-05 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ccdf326c-3fbd-3aee-a319-54f668192252 | -9.74448 | -44.00155 | 2025-11-05 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9891e73-43b9-3f46-a754-08a9dfb72789 | -6.22016 | -46.13511 | 2025-11-05 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5b729243-3df2-3fca-859d-7ef1aee10fc4 | -2.42302 | -49.30408 | 2025-11-05 03:51:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62100ba7-b373-311b-8ada-e37f203a032b | -6.97149 | -38.08181 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03f321b3-a183-3843-a9dc-f18548932136 | -6.5892 | -44.62337 | 2025-11-05 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70274e13-b924-3808-b438-c2b1d9e13e83 | -5.24392 | -45.74009 | 2025-11-05 03:51:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ccb83d5-9599-39a6-ba97-798ed9f825da | -4.65936 | -44.53077 | 2025-11-05 03:51:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb13dd7c-297d-3abb-a004-1d6b34f1cfdd | -9.84776 | -40.26311 | 2025-11-05 03:51:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f40af86-8299-3bfa-b053-14e9d47662a5 | -4.38371 | -46.2696 | 2025-11-05 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46cb581d-47ac-34d1-956c-ad517cccefe3 | -4.76551 | -42.65464 | 2025-11-05 03:51:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d5065655-c8b7-3ae5-9f6d-7bbf918ea5b3 | -4.86012 | -44.6157 | 2025-11-05 03:51:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9d04de97-9268-3281-b6ee-4eac723954ae | -4.45733 | -43.22393 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 7c0e7c22-0703-3429-b45a-488ab6550d6f | -7.54713 | -45.84499 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8118a6c9-098d-3873-b001-ee31d4bb7e0b | -6.43389 | -45.66069 | 2025-11-05 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0ffeefb-1be6-304f-889a-5ac9c996ba7f | -6.33565 | -42.3695 | 2025-11-05 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d3a12cb1-7374-3127-bdbf-ab279a6ebbc4 | -6.04768 | -40.11169 | 2025-11-05 03:51:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7900c6e8-0714-3d00-99be-088883317056 | -5.2703 | -44.13968 | 2025-11-05 03:51:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20e89048-aaf3-3e13-9804-c455c0f1cf56 | -8.95745 | -42.66095 | 2025-11-05 03:51:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 510cb52d-5695-3cb7-983c-8d803f2ffe7b | -3.70611 | -45.88573 | 2025-11-05 03:51:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee0c1d0e-fb73-37d9-a71c-dbd302e0964e | -3.66043 | -44.8005 | 2025-11-05 03:51:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dadb99ed-47b0-304c-b595-f944d8afb866 | -6.0718 | -43.25072 | 2025-11-05 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a2a5fa1a-a3b2-3b08-8ce3-9a6f24345124 | -6.77254 | -44.84625 | 2025-11-05 03:51:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0a71ee6-1eac-3d4f-874c-240be2a900b5 | -4.50344 | -45.43663 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6f53621-dcb3-30fc-a753-d097cf78c4ed | -5.0309 | -43.62457 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 30543b94-1b7d-3956-9284-9e3ae8c6c63f | -2.7269 | -47.38433 | 2025-11-05 03:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 197cf2ba-f6ca-306b-86ed-c73686b78078 | -2.42413 | -49.29745 | 2025-11-05 03:51:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 693aa36f-f4cf-3901-ab53-eb078fd64dac | -5.13083 | -40.62603 | 2025-11-05 03:51:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94d81055-9135-32f9-a21c-1cfd7118a7ed | -7.03985 | -41.45859 | 2025-11-05 03:51:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0e78884a-334b-38d7-8a2b-2b7ec1057522 | -8.13978 | -42.20789 | 2025-11-05 03:51:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e97d605-6835-3536-9d9d-771d3efa38a1 | -5.45259 | -45.40438 | 2025-11-05 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 27a1b851-f099-3b02-8202-c25b92b447af | -7.23404 | -37.15573 | 2025-11-05 03:51:00 | NPP-375D | CACIMBAS | PARAÍBA | Brasil | 2503555 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4e29b0ce-fc68-3b4a-aedd-d688b83b9d40 | -3.40887 | -44.44394 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e21a218-0ec6-3ce2-8a25-e2155fd2b760 | -7.90262 | -45.56567 | 2025-11-05 03:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5cad05a-0655-3a63-9f6d-7f1b28814f80 | -7.54512 | -45.85384 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b9a563e-85f2-3ad9-8a5f-39972123e918 | -2.84031 | -49.41325 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7c32498-d818-3d51-aa1a-8529d6eac240 | -4.40978 | -48.96747 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d1ea541-16ee-3da2-946a-297cdaa40fbe | -5.46665 | -43.58226 | 2025-11-05 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14064f8f-34d1-3c5d-9807-af0a47e365bf | -3.49197 | -43.63371 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| abe22ced-d2bb-303d-8a6b-5505ce91ff4c | -2.8347 | -49.41564 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de57a463-8023-3752-9b03-79ea83744dc4 | -6.06372 | -47.30421 | 2025-11-05 03:51:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 66b55c2f-e3df-3de9-83bc-33bc8416fb2a | -6.07119 | -37.50723 | 2025-11-05 03:51:00 | NPP-375D | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7bde7dbb-a8c8-31f0-b70a-af35196cf277 | -7.42132 | -46.65417 | 2025-11-05 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20db7874-bc17-3278-a3a8-8b4d933defa5 | -6.46771 | -39.16627 | 2025-11-05 03:51:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| daf642fb-4af4-3b30-942b-aa5323fb4daa | -3.22956 | -43.4413 | 2025-11-05 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e571d4d4-7c63-38b2-9d9c-9b6902ba1f8a | -4.55683 | -45.59151 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1570c20-6bbd-33fd-854b-fff50c41b90e | -4.50821 | -45.44091 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa527c9b-b4a8-3a2c-9f3f-66d57f97b185 | -3.87157 | -44.43397 | 2025-11-05 03:51:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37b3c7d1-e697-33e5-82f1-910541cece19 | -6.63584 | -44.54111 | 2025-11-05 03:51:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b889bbe-1859-30c0-a7da-a840eeff257e | -4.89466 | -46.85462 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1af68b2-2f7a-3191-a520-c1de1d1d1369 | -3.70487 | -45.89298 | 2025-11-05 03:51:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3992ef5c-4f59-3141-a9b5-b2977f7ff58c | -4.30275 | -45.37237 | 2025-11-05 03:51:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22c9952d-d54d-3219-b4eb-41bdfd63b32f | -4.60657 | -43.89986 | 2025-11-05 03:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc1c0615-3524-3edd-a158-f6a99c3e4acf | -4.55631 | -45.59461 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1d8b4de-9ff1-3089-bdfc-3a5c4bfc490d | -5.61565 | -41.08586 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bbd8ab19-c9f8-387b-826d-fe488fe03c96 | -5.10808 | -46.22358 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aae1a4e-ea78-3c51-88ec-200de603ce7b | -6.51203 | -38.74086 | 2025-11-05 03:51:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4654b25d-e04b-3953-a3ca-9cc7eec6c621 | -6.14338 | -41.61775 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 286f90bd-7c20-3a9f-ae31-d4ce87b5e6a4 | -6.27243 | -42.56904 | 2025-11-05 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2a6ec70e-ec8b-34cd-8788-c70be9c5c484 | -9.62617 | -45.23119 | 2025-11-05 03:51:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e43df344-3b5b-384f-990e-17856443fcc2 | -4.57894 | -43.33887 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 50acad50-8480-3350-b9ab-168f1345e654 | -3.82294 | -48.66375 | 2025-11-05 03:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| daf54814-1af4-312d-9b2c-e117afdb8f75 | -7.2925 | -45.45348 | 2025-11-05 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdc0f936-1534-3c89-acd8-7e82398dff8e | -4.45354 | -43.21852 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f5ba745d-9a6c-39e1-9a0b-700d95924fd7 | -2.98483 | -48.71133 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a1d4787-59b6-3c22-aa80-ca1828617a64 | -4.95438 | -45.0833 | 2025-11-05 03:51:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c97566e-39f7-3a6f-bd6d-a7a8189068de | -5.45368 | -45.39802 | 2025-11-05 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5f3cbff-ffcd-33f7-8004-be6c93461c68 | -2.82091 | -45.15365 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 506249bf-0a4e-37e1-8f03-2454f9ecbba9 | -8.93639 | -40.86977 | 2025-11-05 03:51:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7f292ac8-e22d-352c-a9f9-879554469a6e | -5.78485 | -40.81022 | 2025-11-05 03:51:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 30c49f76-57ff-31e1-9ce9-bccf41bfc9bb | -6.20795 | -43.27244 | 2025-11-05 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bd68b03-4c8e-364e-80ca-9909c8ba3f03 | -6.13037 | -41.69472 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README13.md)
