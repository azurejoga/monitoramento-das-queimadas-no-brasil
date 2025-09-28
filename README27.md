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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77cde56d-ad3b-3373-98e3-c4ea49b142bf | -6.05922 | -44.86515 | 2025-09-28 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbb404a2-b959-3981-8809-dadada28b10e | -7.30858 | -42.95127 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dfde8310-fcbd-3c66-817b-95943028fe6c | -3.80367 | -41.56499 | 2025-09-28 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 127d2e2a-cfc3-324b-a8b9-e2c34bbf2b5f | -5.70158 | -42.62536 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 80b80a23-387b-3de1-a9f6-4910926278c7 | -3.3344 | -50.25409 | 2025-09-28 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b834e44d-aabf-3ec7-a300-12336f2ee9ff | -2.58165 | -48.403 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fe427770-1e3a-3544-a0b7-d10991bfb8f9 | -6.25448 | -42.46931 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68fe8533-b26f-3fc9-8a14-c6bf5d6d3a11 | -7.03698 | -44.75811 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1086ff8e-8700-3e50-8825-e13c4b13caff | -6.53824 | -43.82597 | 2025-09-28 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8125326-a772-3807-afe0-32f107ec7856 | -6.54603 | -44.14756 | 2025-09-28 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cc2be25-4e5f-3855-83d2-cb00a9544e92 | -7.86739 | -44.56271 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68769e4f-05b5-3671-9c34-5beb0b2afacf | -3.54414 | -39.8091 | 2025-09-28 04:04:00 | NPP-375D | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7050fa3e-f756-3b91-af2b-8eea98ba75c6 | -7.75079 | -47.01185 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8eb15762-6a1a-32e6-9a62-a120526a5688 | -8.28299 | -45.43609 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 063f8a40-4ec4-321a-a4e8-1ee5516d8d28 | -6.31002 | -43.47003 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fba94868-73dc-3d9f-8d6b-1bfcffac28a2 | -6.41248 | -42.86729 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bd9f7606-fb40-34d3-8271-ff4b9706e7c7 | -3.86657 | -40.45222 | 2025-09-28 04:04:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ebea070b-a798-374c-a14b-a5b5be32025e | -5.89466 | -42.81274 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12525b2e-9b8f-3ffe-a3ec-e6c24ad8f7d7 | -5.69312 | -42.63221 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1c43ff6f-6823-38b4-84d2-fbf5cdc27372 | -8.47974 | -47.79026 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bd6c1b9-5888-354f-93d2-b199915a54b7 | -7.5885 | -42.32574 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 081a00f6-440c-3259-a517-f4514c82022e | -5.74992 | -42.82564 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 397450fa-765c-327c-808d-3c667923f144 | -4.97549 | -43.20514 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d99b58c7-09be-30ca-af4b-a94d54069c53 | -9.2121 | -46.77403 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d267df54-bb73-3378-95d7-bc2a0c7a9f28 | -6.71815 | -47.20822 | 2025-09-28 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00fea306-36ac-3da7-b5c8-5434dce0c44e | -6.12822 | -41.79523 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bdf2946-002a-30f8-b172-031126e612e0 | -5.73285 | -42.83975 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 36c80822-12ed-37e1-9218-25e7c9fd0bf9 | -7.30567 | -42.94667 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31c6c87a-a7a9-383b-bb90-f704134a3603 | -7.04401 | -44.76472 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3900b42-5277-3848-93d2-82374f0426d8 | -7.03135 | -44.76759 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64e69d23-e647-3393-8739-7e386a2eff7b | -4.9046 | -47.13868 | 2025-09-28 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3bc27b4-214e-3875-b166-8f7814c563bd | -6.7594 | -44.59326 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69cedf3c-7ff2-3876-aadd-26f143824d54 | -5.82667 | -44.43147 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69f35283-720b-3504-8849-1abb77431f77 | -8.49592 | -44.73176 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ba0f822f-374a-3996-9f4a-97936cbcd790 | -6.09593 | -49.3937 | 2025-09-28 04:04:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1fc0b6df-8984-3c28-b97f-3407915ed4c1 | -5.54008 | -42.73911 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 887542ec-496d-3c3e-942f-8013de095bcd | -4.86599 | -45.75506 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 329f31cc-8915-3423-956e-bc6220b8adf2 | -5.72845 | -42.66272 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3929b81-f923-3ba7-9a8f-ae7c45fb722f | -5.98146 | -44.12555 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d50d7956-17ae-3843-a750-e768c2750860 | -5.82505 | -44.44146 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fcda0024-3fba-39cf-b72e-884d45cc5194 | -5.82022 | -42.8104 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 81330795-5b4b-3529-a0c9-f7e00fe8fd35 | -5.80972 | -47.81517 | 2025-09-28 04:04:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89d1d03f-5e25-3c55-aac8-79e226931092 | -6.40711 | -42.89967 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0023af98-6917-3891-9110-8da5889b5866 | -3.80613 | -47.584 | 2025-09-28 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 633aa5de-37a8-3cad-93a3-8cc2438f8c26 | -7.74627 | -47.01101 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 022adde6-cb3b-3703-97f1-e98ad2593e59 | -5.90122 | -43.29184 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd7ae6e0-f725-3ad1-ad19-b23615d83840 | -5.46483 | -41.07561 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6e36307a-ca2b-3158-a9fa-0831cecb972d | -6.1306 | -43.44238 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 474ee900-6e13-35c6-aa0e-0b71a55755fc | -4.77807 | -41.04897 | 2025-09-28 04:04:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5212b1b2-210d-38f6-9731-590a1205dc47 | -6.62486 | -45.90637 | 2025-09-28 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a7e3025-0d51-3a6a-887d-f5c96eedad1f | -4.92008 | -48.16541 | 2025-09-28 04:04:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59e72194-f88c-3531-8b3a-13f7c32bb2fe | -6.15626 | -42.80718 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 38e23028-5aca-35e0-a201-c0f45610c559 | -6.44493 | -45.90324 | 2025-09-28 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e02681d0-2d8f-32a8-a271-b6084a44ce8d | -6.70934 | -44.5824 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ad83de5-9cae-3f13-9be4-3c866ad7494c | -8.65211 | -43.99147 | 2025-09-28 04:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f30c4b45-cd12-355b-bf53-f7a7f33e7777 | -3.87218 | -48.04652 | 2025-09-28 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c67a9c1c-8d35-3874-a7e2-00005e196635 | -6.11143 | -41.81194 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 694fd1e7-bcf9-3dc5-81d1-e6490e9ed7ee | -5.29791 | -43.1501 | 2025-09-28 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 885ffce2-deaf-3034-8f3f-1a6e1d177e72 | -5.76008 | -42.83902 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| b4889644-5ac2-3c4e-9b6b-f18505bf61cf | -7.79078 | -47.02566 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 92c54de7-eb90-3f21-af25-4bada5cf9f9e | -6.35012 | -44.31182 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 25d46c74-6344-3633-a050-380686262ca7 | -7.16378 | -45.50774 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85b73885-7ff8-36f0-a36a-13d0adb6098c | -9.29266 | -45.70976 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad6c5248-71be-3431-9bcf-83289132601f | -7.86499 | -44.57678 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b485a26a-0cdd-3753-92bb-cdae7eb1637c | -5.1869 | -39.30796 | 2025-09-28 04:04:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc90b859-e062-3250-85fa-783b173669f0 | -5.73981 | -43.37206 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16260fe4-9bbd-3cd5-a2d6-8129786fe8c9 | -5.75444 | -42.84356 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 45d554a1-541b-3d07-959b-e82139d8bbae | -5.72948 | -42.86063 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 75904bad-3a42-3cf7-8872-823b0054a60d | -5.75579 | -42.84261 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 63a81169-ab56-3cad-be79-2cbe7b07f429 | -9.06789 | -45.54163 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5119f9c-ca56-3b86-88d1-ce80827b4052 | -8.28925 | -45.44809 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb0488e7-91fe-3235-a5a7-7a8da2180c40 | -6.40577 | -42.90778 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1b73f090-913a-3ac9-b1a4-e9f3b825b793 | -6.05847 | -43.78391 | 2025-09-28 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b492730-3e46-3889-9541-63fad70ad7fa | -7.86295 | -45.29 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceaccc00-4838-3520-8830-5b49eba4508d | -3.64943 | -48.32244 | 2025-09-28 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 258a191d-820a-3520-a004-22b23b8a578a | -5.78074 | -42.89333 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 23d4d013-d51e-365c-916d-1ddc3d4e6ae1 | -5.37582 | -42.30272 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 03c83fa4-9812-39c3-8074-90aeda62a851 | -4.88037 | -37.91953 | 2025-09-28 04:04:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 63435f5b-d8c9-3a7f-b915-c2655c9253ff | -4.44609 | -43.98857 | 2025-09-28 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e85dbe73-c556-3024-8d2c-bcf7e292a6e8 | -4.86163 | -45.75434 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d937fcbd-8561-32b6-8dfa-074fd9739f09 | -9.75321 | -46.13367 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f40d49c3-da3c-3a41-aca9-de05c66b27bb | -9.95155 | -43.6274 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02dfe292-667c-3ad0-85eb-ca49a7af73cc | -7.37331 | -47.02411 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e64dc2b-33a2-31c1-8ab5-bb25afcfb0af | -7.62443 | -43.80003 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 531d7b6c-5e24-3e50-8d44-d0ad7ad5df3b | -2.65687 | -48.80125 | 2025-09-28 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 929b296b-436d-3c64-bc41-6990acbb24f7 | -5.3202 | -42.76143 | 2025-09-28 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8e272710-a794-3a55-b7ea-ad3225a49eea | -6.46091 | -44.22393 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 062281d5-4e8a-339e-b1fb-a592a51d3f2d | -6.2702 | -44.07034 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eff0fb4c-3d31-3d87-9fb2-e4a9469546b1 | -10.53895 | -43.62838 | 2025-09-28 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b44ef142-6879-33e7-bf91-13d23193a663 | -7.53634 | -46.10669 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8af768f4-0d26-3c86-b72c-00575b15f181 | -7.78253 | -47.01951 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba5945ce-ce78-358b-a4c8-64a6304b7677 | -3.80243 | -41.57259 | 2025-09-28 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 5e6b85d0-0a87-3fc6-8074-6ed6697f94fb | -6.27593 | -42.4929 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e571557c-a649-3ce2-8582-3f57119ddd5b | -5.61256 | -43.37067 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70ff635d-151b-3a1d-bf65-ee19713e2dc5 | -6.90406 | -44.75945 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90d55af8-5498-3685-8ec9-03047f1790db | -5.78436 | -42.89388 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 88eda0b5-7282-386c-9f4e-880bce543c11 | -2.58762 | -48.4067 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d6dfd76-964a-3354-a288-3ea48aced5ea | -6.11428 | -41.81618 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| efc59be3-c256-33ec-b402-94c1d93f8393 | -2.58708 | -48.40392 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d3fb0bd0-cbd7-3bc8-93a8-39db37fd0993 | -5.81593 | -42.81407 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |


[Clique aqui para ver as próximas entradas](README28.md)
