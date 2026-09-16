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
| e295ce04-9559-36da-bd2c-006e21ea5068 | -6.15829 | -36.48019 | 2026-09-16 03:53:00 | NPP-375D | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d0fbbb81-15ce-3cf9-929b-74f72dd5109a | -5.14055 | -47.60306 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05bfa196-4233-35ec-896f-c439909a77a2 | -7.13606 | -42.09016 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f3465d4-3f93-3ff0-a509-706b62d38da3 | -5.62805 | -40.85876 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1636bc97-265a-30a0-a172-54f80655be66 | -5.64088 | -40.86074 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 053ba668-9616-31e5-84e1-aac0c284551f | -8.38104 | -42.218 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ee6b0a26-c565-35c2-9b82-ef0853fb606c | -7.0993 | -41.82121 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a62ecfd-0105-31d6-ab8c-cb09fe6997dc | -6.10863 | -46.10471 | 2026-09-16 03:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa236603-a55e-3f5a-9c83-d9976e1301fc | -5.10293 | -47.62001 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cf76ecc3-68a3-3687-9479-3348a42a3ffd | -6.39571 | -44.05762 | 2026-09-16 03:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95a8993f-36c2-3549-9bed-de10d9685ed2 | -5.75598 | -37.8862 | 2026-09-16 03:53:00 | NPP-375D | ITAÚ | RIO GRANDE DO NORTE | Brasil | 2404903 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a83dc49-c1a3-32f2-ad64-dea14902b1b9 | -7.14598 | -39.53098 | 2026-09-16 03:53:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 70b8cdee-1ade-32a3-8d88-42d45773de38 | -7.26436 | -46.17657 | 2026-09-16 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14ccadcd-670f-374e-9dc3-5b7c76afff01 | -5.99831 | -46.63229 | 2026-09-16 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 86f491f2-da6f-39b6-9428-ab7409e37499 | -5.17242 | -39.74331 | 2026-09-16 03:53:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 68899291-8f51-3f49-b6e1-72fa9f5297fa | -6.66257 | -43.65055 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6ef735f-5633-34f1-83f8-749872604c4e | -7.17452 | -43.5136 | 2026-09-16 03:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3a00671f-b039-355d-83bc-e667aa7e7eb2 | -8.05127 | -43.74697 | 2026-09-16 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8278a904-37ea-373b-9562-e10ec20fb814 | -6.11466 | -46.10568 | 2026-09-16 03:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ada110a8-e310-33ed-a136-4d375c2dcc7a | -7.26285 | -46.1849 | 2026-09-16 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f335133-160a-31bf-9628-087c26e6ae72 | -8.48125 | -38.12628 | 2026-09-16 03:53:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 76d0cfee-39ad-3729-9fba-72e18760b87f | -6.11369 | -46.10397 | 2026-09-16 03:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ded32e9c-1124-3eac-9224-32882032b03e | -5.10514 | -47.60797 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1982d6ef-ca00-3752-b427-06c3c9318239 | -4.90685 | -45.67457 | 2026-09-16 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a13e9198-d403-3067-b3e4-66f9ae9eca96 | -6.00386 | -47.39146 | 2026-09-16 03:53:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e6a3ce3-309c-3e02-bdfa-930bafb0e91a | -6.78763 | -48.65399 | 2026-09-16 03:53:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34f3c65a-9968-30a7-a66f-df59233434f5 | -7.26361 | -46.18074 | 2026-09-16 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e51410bb-a659-391e-9d27-0c8de4472b46 | -7.34209 | -44.47997 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e23dae7-ff41-347b-a163-9cf8df06da8d | -4.67822 | -42.0951 | 2026-09-16 03:53:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8943e04d-7e22-349a-aa6c-2e4e9edb9efa | -7.33397 | -44.49489 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c5da837-8a60-3f76-b03b-71ef29fefed5 | -6.7778 | -42.97756 | 2026-09-16 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f43b65c6-447c-3686-ae16-0c51b7e94777 | -8.05038 | -43.74868 | 2026-09-16 03:53:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 18bda0f6-3860-3d02-9cc0-36d0f06ed5e7 | -6.94539 | -42.57943 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3f655c01-4bc6-3fe0-960f-99d8cc614e79 | -6.77506 | -42.97408 | 2026-09-16 03:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 11b48bb7-4abe-3da5-bd6f-a0c98b0f82bc | -7.0941 | -41.82478 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a32e896c-9c51-3190-afdb-9686e1488753 | -7.8231 | -41.24099 | 2026-09-16 03:53:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85035fbf-3e47-3e79-b622-de72dc98c982 | -6.95566 | -42.57581 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5dea5ae1-dac4-325e-9e79-49e012c2b186 | -5.60596 | -44.84104 | 2026-09-16 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e86c7342-e898-356a-aea9-61af6c2f383f | -4.34576 | -46.61611 | 2026-09-16 03:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7446536-f41b-3ee2-bea7-d0ad49a926e0 | -5.12512 | -47.61197 | 2026-09-16 03:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a06665c9-6ba8-34c5-941f-c533cbbb723f | -7.33928 | -44.49578 | 2026-09-16 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9632eb35-f230-3fea-9bb0-7a98639bc727 | -4.90615 | -45.67863 | 2026-09-16 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66d09fbc-b3bb-31c7-b5a3-6937a1d8889d | -6.26737 | -43.27801 | 2026-09-16 03:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 986d1c0a-eff3-3574-836c-682ef6fcc1e2 | -7.09521 | -41.76644 | 2026-09-16 03:53:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3954fba2-4592-3633-bad1-3bcf1118b249 | -4.35802 | -47.77821 | 2026-09-16 03:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d5e1b400-52d5-3f19-9143-a34f9f54838b | -7.08315 | -42.0996 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b1fbfedf-e7fb-30c9-b1a9-1051d9f671c7 | -6.78738 | -48.66021 | 2026-09-16 03:53:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acdd80c2-afc4-3ce4-b35f-3b80e5d3d6f5 | -5.63116 | -40.8488 | 2026-09-16 03:53:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f3a2de89-236d-3112-bea9-b73d1c54314e | -6.77947 | -48.65907 | 2026-09-16 03:53:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10ed97b7-5081-39bf-bcf5-5616d1c36a9f | -6.72742 | -48.11497 | 2026-09-16 03:53:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8b2f2bfd-8bbb-32da-b778-1174dd98ae85 | -5.76936 | -45.09406 | 2026-09-16 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f7898ea6-67b0-3590-919f-e7221d137829 | -8.05141 | -43.74299 | 2026-09-16 03:53:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 07e58576-a9d8-3c0c-895b-c77558a9696d | -5.60465 | -44.84837 | 2026-09-16 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cf170d6-1aa6-3395-a693-394df03853c9 | -7.03679 | -42.04498 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 12c24524-cdcb-3c39-99ea-c32cab6cf454 | -7.15861 | -44.24118 | 2026-09-16 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bc6a621-2efa-348d-870b-d03a3ea6b4c9 | -7.18703 | -41.8079 | 2026-09-16 03:53:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c78dbb53-bfb7-363f-aa10-c2f3596e85fa | -3.31656 | -47.14543 | 2026-09-16 03:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b79688c3-6a62-3387-9a22-3dfb4b45c941 | -6.78823 | -41.46203 | 2026-09-16 03:53:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 30a96667-bd09-3ff3-8e2b-feace6666329 | -8.03276 | -45.54675 | 2026-09-16 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15dbcaeb-c479-38a5-9b41-68f49a2222b7 | -6.9501 | -42.58011 | 2026-09-16 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3e5d778a-7028-3e21-8817-2b746aa0036d | -7.22926 | -46.13429 | 2026-09-16 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65c3fd62-7c75-3cb4-9644-dbb4932ef47c | -7.07772 | -45.23309 | 2026-09-16 03:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ec3d290-2f82-3d28-b127-619b2adb4f72 | -9.53129 | -42.96333 | 2026-09-16 03:55:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a03f0654-8b0a-3d73-afc8-68119956bc17 | -10.81985 | -46.1754 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71687280-2ea8-34af-b273-51a848e5be6b | -11.16812 | -42.80042 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd21f802-83c5-3337-a2ea-14a4875eb4f0 | -11.13834 | -40.47744 | 2026-09-16 03:55:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 157d2e57-1467-36dd-bf1c-466d52f51e65 | -12.55139 | -47.09816 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e4d152b-7e17-3526-ba21-0747f3a60931 | -10.10144 | -45.61094 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fded943-22fe-3b9c-8979-804f8bccb6bb | -9.78614 | -46.54494 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d468fac9-e7ee-3bf1-81d8-08a736021600 | -11.17299 | -42.82414 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b63959a-456e-3f7a-ab09-005aa9f21968 | -9.48212 | -45.44096 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6d1382c-df80-3c1c-be83-bf4ee3cd860e | -9.77897 | -46.48711 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7864a543-a1b9-3ffb-9ff5-4a56350ab08c | -9.84332 | -48.35199 | 2026-09-16 03:55:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a7e868c-354a-3cfc-bcc7-2a04d0f75ea6 | -12.15268 | -47.99008 | 2026-09-16 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 595d8ae6-4c7e-31a3-9f5e-33be68fa289d | -12.32365 | -47.95717 | 2026-09-16 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3cad51c8-6353-31cc-93d3-7314718a11af | -9.76125 | -46.57611 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2a0409b5-8fd6-35b2-af83-666c32d5e1b3 | -9.79123 | -46.48569 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a33c1c79-b591-3f9e-ae4b-66cdfd6df761 | -13.34787 | -46.30537 | 2026-09-16 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0befdc09-6b32-3999-bf3e-56b8526ed711 | -15.29103 | -42.78637 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9fc62f9-10c9-3e4a-bdbf-6a2a1af3e921 | -10.10866 | -45.57291 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54f1b5a2-6612-34cf-8627-778eedce0177 | -12.85028 | -44.39214 | 2026-09-16 03:55:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0dfc9bbf-3773-322f-b1f5-1cec550c767c | -16.78329 | -39.45745 | 2026-09-16 03:55:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d5999cba-efde-3b7a-9970-a69e0c3b093f | -9.54938 | -45.41825 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 907f17b7-c9da-3f21-a3b4-33f464b6d1ef | -9.35232 | -50.18525 | 2026-09-16 03:55:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea5fc4e5-4adf-3215-8284-b1102139879f | -10.78859 | -46.20094 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1eb52833-7e43-309e-b6d2-e685d4d88145 | -15.27108 | -42.80198 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7752d840-a8b9-385f-a443-8f94c66679b2 | -12.46434 | -41.40342 | 2026-09-16 03:55:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e8f6c5b8-b248-332d-83c5-a6cb1d405852 | -15.8933 | -40.23597 | 2026-09-16 03:55:00 | NPP-375D | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e286dc2d-c0d4-3d84-b5a0-95222830d2b4 | -15.88153 | -39.94243 | 2026-09-16 03:55:00 | NPP-375D | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 54bebf78-53ad-3073-8169-587795046809 | -12.17216 | -38.59937 | 2026-09-16 03:55:00 | NPP-375D | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| daca0834-ab06-3439-a778-220f14931c05 | -9.78387 | -46.49123 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 49a629b5-0be7-3c6b-9062-25ec23f96e94 | -11.20402 | -42.82999 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7675f7bf-4a53-3262-94ef-3708af614443 | -11.53913 | -46.86495 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d327a240-ba1d-3fba-ab72-a854893bd125 | -12.5195 | -47.1087 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9958d51-a9f8-3deb-8677-250a9c8fa6ff | -9.78471 | -46.48848 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8ddad500-8222-3af4-a9e8-72f1e9ee15fc | -10.37149 | -45.12789 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 850af1c7-3f2f-3f48-9f20-2053bbdc05d5 | -13.65176 | -45.96524 | 2026-09-16 03:55:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1a58d88-c1f7-3bbc-a972-0be22d7bfdf0 | -10.30693 | -45.27008 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eb71f02-6608-308f-b6df-d066a1065be4 | -10.09507 | -45.61476 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94dd7db9-7ad3-306f-a2f4-f1a678851045 | -9.55299 | -45.42278 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README16.md)
