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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b41ed2b9-ef0e-3c1f-9aef-07f3b6b13228 | -10.7591 | -44.7026 | 2025-09-16 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 3ca43e50-2c5e-3953-82c7-1ad79d4d3759 | -7.4503 | -46.1647 | 2025-09-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 3f7be226-7236-381a-afc1-38b6cdbde46b | -7.1318 | -47.9801 | 2025-09-16 14:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b7ea66af-2e87-3316-b79c-a96cd89bfffc | -10.7302 | -46.5082 | 2025-09-16 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 315.3 |
| ee1152fd-a3b2-3387-bb76-217656993600 | -3.8415 | -44.1054 | 2025-09-16 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 158.6 |
| d4db65d1-5a59-34da-919e-7d4514c4ce6a | -7.7229 | -45.3056 | 2025-09-16 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 359ae10e-8422-33a2-9844-74e7b353f26d | -7.2581 | -46.6052 | 2025-09-16 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| fcd6d186-09af-3da2-aa15-9532bfcc71d2 | -10.08 | -48.1836 | 2025-09-16 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 983e94fa-c595-3206-8838-002492b81105 | -5.8086 | -43.4956 | 2025-09-16 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 242f67ad-6835-3a72-8bb9-ea0c910e751a | -6.1881 | -41.1855 | 2025-09-16 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 244.3 |
| 6031c049-24c4-3824-9fbb-10475b417d42 | -5.8809 | -45.8641 | 2025-09-16 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 183.0 |
| a903f709-2594-3fbc-b65f-425dc7e79ec1 | -10.1189 | -45.4977 | 2025-09-16 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| d1801b62-8244-30e6-93ee-1baa146cf3b4 | -8.7674 | -46.1049 | 2025-09-16 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 5c31cd22-682f-310a-ab7b-7710168eff85 | -5.8622 | -45.8654 | 2025-09-16 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 41c532d1-cee0-3c33-bbef-c98559ac24ad | -7.2771 | -46.5814 | 2025-09-16 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 3b55c680-1af0-3183-bfe6-86d27ff1aa9e | -6.169 | -41.2114 | 2025-09-16 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 165.1 |
| 0108ecb6-0b88-3145-a76c-6d3e6ec879ca | -12.6953 | -47.7446 | 2025-09-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 6b96d21e-9ef4-3385-99ac-024c1b0ede4d | -8.976 | -46.0152 | 2025-09-16 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 55b7f952-67e3-3793-8768-904c572e7f9a | -14.1727 | -46.1354 | 2025-09-16 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e3e217eb-f5b7-3ca8-8e9c-1b6482b48fb6 | -12.6352 | -45.7652 | 2025-09-16 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 0dfea934-6efa-3890-8df4-fae1134b3e50 | -12.0647 | -46.555 | 2025-09-16 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8963d2b9-78de-32ca-ab55-42dcac4b9a92 | -13.7862 | -54.9512 | 2025-09-16 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| dc570417-d181-3833-b68f-74735514ad73 | -6.16 | -46.0007 | 2025-09-16 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 0887113b-2c8c-3b75-8054-78b874be94e6 | -12.1152 | -44.8072 | 2025-09-16 14:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 38e5baf9-b97e-3d2d-897e-20d6eb636b05 | -7.45 | -46.1871 | 2025-09-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e407f101-c1f6-3980-baf1-472316ca8a52 | -10.7493 | -46.5058 | 2025-09-16 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 221.9 |
| b192aa54-2b65-3971-9143-5a9689afab28 | -11.4477 | -43.5514 | 2025-09-16 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 10498f9f-7748-3cf1-963d-f6ef84e50f18 | -11.1896 | -51.419 | 2025-09-16 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 357f3efb-c1bf-35ef-ac93-0fcbb993cae1 | -9.0857 | -44.8893 | 2025-09-16 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 185.2 |
| fd2a5148-7f45-37a5-b87c-e54fd17088f7 | -5.7671 | -43.9392 | 2025-09-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 60ff66fa-ac49-3915-8e8d-3fda37022a60 | -8.7866 | -46.0804 | 2025-09-16 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 30ff7a1f-869c-3750-82cb-53733287ffc0 | -3.8416 | -44.0824 | 2025-09-16 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| d84b0127-b36c-3818-93e1-5d75c66b04a1 | -6.8557 | -45.6543 | 2025-09-16 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 07ffdcb0-e42b-325c-a3e9-e93e16d7e247 | -6.1688 | -41.2357 | 2025-09-16 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 3363ccc2-d44e-34dd-aec3-3adda58d83d2 | -5.9006 | -45.7506 | 2025-09-16 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 31e3808a-6bff-3b5c-a0a2-b145021eab7d | -5.9617 | -45.1824 | 2025-09-16 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| ad65c138-abcd-32fd-a4f9-cfdcbad5ff14 | -11.467 | -43.5485 | 2025-09-16 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4fd61b7e-e275-38b4-b2bf-c36297f9dba5 | -14.3498 | -45.1093 | 2025-09-16 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| c10f7d66-eb7e-325e-bb18-faf5d8a54414 | -8.9259 | -45.5231 | 2025-09-16 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 245.3 |
| 6caad1d6-f166-32f8-841e-612d120f1cf3 | -6.8369 | -45.6559 | 2025-09-16 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 5d862885-fda3-3eb5-b5b5-9f5b431e534e | -10.9667 | -47.1952 | 2025-09-16 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 98f3e1a2-f875-3490-bef2-1e6009a69d8c | -10.0803 | -48.1616 | 2025-09-16 14:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1042215a-e9d0-3f11-ab53-6ab3c22fbd7f | -5.786 | -43.9147 | 2025-09-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 04fb5485-f9fa-3678-bba6-f3d180223f37 | -6.4105 | -43.3301 | 2025-09-16 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9200ca1f-1e35-330f-b798-ad301471a06e | -5.7694 | -43.6845 | 2025-09-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 619dbd2c-bb40-366e-9519-9bb13536e7ae | -9.086 | -44.8663 | 2025-09-16 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| d5dd9c51-de79-3a36-81bb-49dbea12e7c8 | -8.7677 | -46.0823 | 2025-09-16 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 91985100-3a4c-3b7e-a8af-4b7785bdcbcd | -6.1693 | -41.1872 | 2025-09-16 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| fac953d9-a6cc-365c-b49f-8f6224806cb1 | -5.9942 | -43.6902 | 2025-09-16 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 6947ce92-b34a-36a0-8187-2c168bef2dea | -9.0671 | -44.8685 | 2025-09-16 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 591747f3-0529-315f-a984-6b523d3618d9 | -7.8261 | -46.1306 | 2025-09-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 178d6f9d-907d-3ceb-b445-fafc4a504715 | -10.7112 | -46.5106 | 2025-09-16 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1f5c93bd-6cc2-3925-8b19-b3e7a563e718 | -6.6698 | -45.5118 | 2025-09-16 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 133cc06d-3967-3729-8c42-9d8e7055f32a | -5.7506 | -43.6859 | 2025-09-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| c32f8645-6a96-3dc4-8272-149395e661c7 | -12.9795 | -47.949 | 2025-09-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 08aba81e-d9d5-3a7c-b73a-8ee6f81a0c41 | -8.5947 | -46.3471 | 2025-09-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b40f6ce0-2479-3bb5-95e0-3ab0967b8491 | -6.3372 | -43.1492 | 2025-09-16 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 220.5 |
| a652953a-361d-33d7-a774-38bad60b3586 | -6.6696 | -45.5344 | 2025-09-16 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| bb1efa82-bded-3dcd-8a88-a435b4ac17ba | -9.1047 | -44.8871 | 2025-09-16 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| f6c3082c-1e26-37e1-a8e5-fb3c7ecc4d9a | -10.7306 | -46.4856 | 2025-09-16 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 8c0fb56f-01a5-345e-a145-7acaeb6a4235 | -6.1878 | -41.2097 | 2025-09-16 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 336.9 |
| f4f7aa4a-3722-386d-b083-aadd7737ea22 | -7.676 | -44.4879 | 2025-09-16 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| a9ecf38c-4d33-33a5-a3d9-080efbd1e567 | -9.1709 | -46.9792 | 2025-09-16 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| b720a24d-2e2d-3440-a6fe-9ca2c560d88f | -7.6949 | -44.486 | 2025-09-16 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.5 |
| a817277a-98c1-3bc4-ac45-fc75e5f0e649 | -7.6517 | -46.6155 | 2025-09-16 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 1a2f4989-b102-3352-9f05-672fc3d87238 | -12.1048 | -47.5592 | 2025-09-16 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| ad92442a-8849-3b7a-91f8-44c9dd66f841 | -11.1299 | -45.3426 | 2025-09-16 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 37d9da0f-1204-3f12-a8c3-4c7ace2be19f | -7.1316 | -48.0019 | 2025-09-16 14:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 96d13c5e-0e37-3fa0-bc30-acc302064770 | -6.337 | -43.1727 | 2025-09-16 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 164.0 |
| a05bfcb8-2fdd-3221-969e-7eb7ba4759d6 | -7.059 | -44.1778 | 2025-09-16 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 15fd284f-5904-30da-8192-0cd40700a5db | -5.8045 | -43.9364 | 2025-09-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 81d926ac-b03e-3ca7-a61a-849daaf7bcff | -6.356 | -43.1476 | 2025-09-16 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 254.8 |
| cd8aaf04-f80e-369c-9a88-6b7a3c003692 | -7.1505 | -47.9786 | 2025-09-16 14:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6ca05eec-70a9-35f0-a54f-fde31ed853d2 | -7.6738 | -44.6717 | 2025-09-16 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| d24b61f8-b3fb-383e-a85d-924f5d305e6b | -11.2737 | -50.8163 | 2025-09-16 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 63972f76-b8e6-3536-9fa5-8c9a43505c32 | -10.9671 | -47.1729 | 2025-09-16 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 180.0 |
| a89dad7e-c004-3965-9cb2-b55db018bf38 | -10.0611 | -48.1856 | 2025-09-16 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 6c45b779-1401-37d6-8eb9-cdd6894dd1ce | -7.0592 | -44.1547 | 2025-09-16 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b5f9ae70-9096-36a2-a023-3991df061f79 | -12.6717 | -47.9926 | 2025-09-16 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| cd69e3d0-3402-3062-adda-d33bbeb055b2 | -11.7342 | -46.8713 | 2025-09-16 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 99742c8d-d392-308a-8ab2-2c63570c3ae7 | -5.9615 | -45.2051 | 2025-09-16 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| cda88984-56f9-382d-9568-67ce1dc58faa | -11.7151 | -46.8739 | 2025-09-16 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 6d98d39e-a1a3-34f6-9aa1-8613205393ac | -7.8449 | -46.1288 | 2025-09-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| b28e0d4a-f9d0-3a26-b660-f08dc95f36e1 | -8.9571 | -46.0172 | 2025-09-16 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| d7bd76f9-8c38-33f7-b259-0a6ec54261c5 | -7.6927 | -44.6699 | 2025-09-16 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ed6aaea8-a30c-3651-9d30-ddf1a37092a3 | -7.676 | -44.4879 | 2025-09-16 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 68f524e0-5ec1-36b1-a0bc-d4349f634cfe | -8.6696 | -46.3842 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7df45ebd-6ed3-3d17-8b5b-8e36c555faae | -8.3244 | -46.9088 | 2025-09-16 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| dce58034-b52f-3c6d-aed8-179b7aaad563 | -7.3245 | -43.9681 | 2025-09-16 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f106a12c-05a4-3c2a-853f-7e038408db34 | -13.2224 | -47.2871 | 2025-09-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 97a1a3c6-13ca-30f5-a633-1a1ecfc812e7 | -10.7115 | -46.488 | 2025-09-16 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 0f6b5109-a328-3cf9-b697-b7c6287da791 | -7.9822 | -45.643 | 2025-09-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 825620fb-f8e1-3f70-8dc5-b8841bbba3c4 | -7.6517 | -46.6155 | 2025-09-16 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 1be66e24-1b41-35d4-b840-ca93196734af | -10.0803 | -48.1616 | 2025-09-16 14:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 5b7f8f88-def5-3ed6-bc05-0af99e1829fe | -8.6699 | -46.3618 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| fd7ff3e8-4f01-3f71-937c-efaaaf0ffd90 | -8.613 | -46.39 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| eeed1b53-d53c-368d-be5e-5e88bb21d6c6 | -8.7674 | -46.1049 | 2025-09-16 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b3be303f-79a3-3efc-9b5a-e9eb086a3561 | -9.7322 | -47.3625 | 2025-09-16 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 59700b66-e06c-3c72-9926-24d4a612789f | -8.6127 | -46.4124 | 2025-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 44df9d6c-0d09-3880-9008-625309cd70dd | -12.1048 | -47.5592 | 2025-09-16 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |


[Clique aqui para ver as próximas entradas](README100.md)
