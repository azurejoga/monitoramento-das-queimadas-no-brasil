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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1bfdb6c-0328-3d9a-a14a-ab2e725452bf | -11.4665 | -43.5722 | 2025-09-16 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| d25d23bf-1f5c-3d03-a946-4fe1bec205d8 | -7.9822 | -45.643 | 2025-09-16 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| b1b92afe-2c11-36fd-9cf4-6d731684a15b | -5.7873 | -45.8931 | 2025-09-16 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 8482c51d-96a0-38f4-8c7a-475f56e25d8a | -7.9843 | -43.9254 | 2025-09-16 14:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5404e68d-0d26-3557-bc77-a753fcef31f8 | -12.1152 | -44.8072 | 2025-09-16 14:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b01d6c99-cada-3ca3-a52b-f4ed756e1cbc | -7.6738 | -44.6717 | 2025-09-16 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 69cf9855-08d2-3bda-aa50-b7f9881396a7 | -10.1189 | -45.4977 | 2025-09-16 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 182.1 |
| e1099b99-be74-3856-bfad-acecf7146f24 | -3.0448 | -43.1702 | 2025-09-16 14:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c7033bac-ef0b-3e53-8fec-b6a7e92daae3 | -3.4179 | -43.154 | 2025-09-16 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 23fb0fc5-92d3-3be1-8a63-beeac1df7763 | -15.8359 | -42.6879 | 2025-09-16 14:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 184.0 |
| d2d51163-0448-3df9-907e-ec8e6d7d0ff7 | -10.935 | -45.5978 | 2025-09-16 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 9f998bec-b103-3b36-9f63-f3b0000f4d49 | -11.7151 | -46.8739 | 2025-09-16 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b07950cc-04d2-37dd-bb2b-81b8ae6deb03 | -7.6927 | -44.6699 | 2025-09-16 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| a647a20b-7e89-37af-8551-7ad9068b647e | -8.9568 | -46.0398 | 2025-09-16 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 5b353043-388d-3b12-8fdd-2cbe8acb34be | -7.1318 | -47.9801 | 2025-09-16 14:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| b7da2921-a417-3ad5-950f-e3f7e54dd1fa | -5.8809 | -45.8641 | 2025-09-16 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 79bbed4a-bcd4-39b4-a714-1e31f7c94278 | -8.0005 | -45.6864 | 2025-09-16 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 05305066-36fd-3ae4-a8c2-cf3305a14084 | -6.1881 | -41.1855 | 2025-09-16 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 2d4652d5-7f2a-3cb0-a16e-11bd386e41a3 | -9.7322 | -47.3625 | 2025-09-16 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 499bee2c-26c8-320b-8b78-cc21ce5df749 | -8.9571 | -46.0172 | 2025-09-16 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| cca87d65-72a1-3e03-b832-dc2a896aeb07 | -7.6949 | -44.486 | 2025-09-16 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 282.1 |
| 3f34d0ca-3d1c-34c1-a56e-36594f4e86d1 | -14.1727 | -46.1354 | 2025-09-16 14:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 4b32fea4-23e9-36a4-9130-0864867c3962 | -7.6517 | -46.6155 | 2025-09-16 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ef96639d-d38b-3cbf-b983-14ac9b164133 | -7.2581 | -46.6052 | 2025-09-16 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d11ecae3-6ff6-36dc-932a-a430268b13e0 | -5.7858 | -43.9378 | 2025-09-16 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 3b4fb44a-6b14-3212-ba0a-98a75626fd21 | -5.786 | -43.9147 | 2025-09-16 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e365fbca-67c9-3c13-b05e-4965b8f1db65 | -12.1147 | -44.8304 | 2025-09-16 14:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f81b4908-891f-3fad-bcec-b19888f61267 | -6.3558 | -43.1711 | 2025-09-16 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 245.0 |
| b30fdb4e-b722-3372-866e-3b6642d0ec82 | -7.0592 | -44.1547 | 2025-09-16 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e7f4f6cf-44c3-352c-8844-07ba85be906e | -8.7677 | -46.0823 | 2025-09-16 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| d05b1725-4511-3b6c-842a-aa310fb1e9d0 | -8.651 | -46.3637 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4178a978-e12a-3dc4-9d79-5ce611ea15d5 | -10.0728 | -48.7086 | 2025-09-16 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 65d55c39-3298-3752-a4b4-b45c00900a1e | -5.7686 | -45.8944 | 2025-09-16 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2fb1011b-24aa-3525-844f-74e5407d3e50 | -7.4315 | -46.1663 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6840d992-615f-3cc9-8c5c-86b03cd34dcf | -6.6696 | -45.5344 | 2025-09-16 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 168b1b5e-a77f-3d14-9602-8e525cdd22a0 | -8.6507 | -46.3862 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f9d67bd8-ade6-33c1-b937-ae723e28bd5a | -12.0647 | -46.555 | 2025-09-16 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4f0bb187-fd3c-334e-8af2-ad0819ef7d45 | -7.4503 | -46.1647 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| e7602907-5565-3e07-8c9c-48176a8fdfd3 | -8.613 | -46.39 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 149140fe-5fe2-311e-906a-e4833f746329 | -6.356 | -43.1476 | 2025-09-16 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 280.5 |
| 3cc4bc30-18d3-39bb-b877-b2eac05fdbfa | -8.7674 | -46.1049 | 2025-09-16 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 239960eb-2cde-3f83-87ea-1b309950d4fe | -10.08 | -48.1836 | 2025-09-16 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e3629a87-a29f-3e27-a8d4-3f5fdcb6996f | -12.1668 | -44.0988 | 2025-09-16 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 9bfc0c87-cd85-3351-a82d-7b18047bb1f9 | -8.3244 | -46.9088 | 2025-09-16 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 9cc69e6b-facc-3594-8242-f6fc57a0face | -12.1861 | -44.0958 | 2025-09-16 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6aa513ee-c18d-3c3a-a7ae-da91f3edc8b5 | -10.0611 | -48.1856 | 2025-09-16 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d6345f62-765b-31dd-912a-706d23285d9e | -8.001 | -45.6412 | 2025-09-16 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 9fd4be6e-dca4-391d-905f-ca304132d497 | -10.0803 | -48.1616 | 2025-09-16 14:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a46114bf-c6ae-3416-849a-4a5442a963f7 | -13.8889 | -44.8644 | 2025-09-16 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4d20fcf5-d259-3671-b96f-54367af76f8c | -8.5947 | -46.3471 | 2025-09-16 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| fa3ed48d-81e0-339c-8227-588c29e7dd93 | -9.0759 | -47.0335 | 2025-09-16 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4089cb4f-9d28-39d3-ae1b-5438a8d5c3b0 | -7.7229 | -45.3056 | 2025-09-16 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |


