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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d601cde-b7f5-34da-a2d6-846a49d70d5c | -9.05846 | -44.84348 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55658f8f-7037-39ba-ba5d-86d7bc0c5c4a | -12.3512 | -38.19305 | 2025-09-16 04:02:00 | NOAA-21 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7814fc6f-fd6e-399d-b932-e2962b0a7682 | -11.11797 | -45.33781 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13a014ab-f8b3-3a20-bd05-9ab955c54282 | -11.2974 | -50.85382 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 995d6d2c-84ce-3df1-943a-63d80a9e1fa0 | -7.56284 | -50.45614 | 2025-09-16 04:02:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca0c10df-f7fb-349c-871e-4c9af3bc9319 | -7.70744 | -45.30682 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 154ba4ed-cec6-36a3-a823-8a7831a27fea | -7.97717 | -45.63826 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 101d4912-464a-3e1b-8d58-9c3b1619bc0f | -8.88624 | -46.19386 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4a67b3a-f383-3189-8161-846194b6f03e | -12.12443 | -44.81147 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faa6b063-aea2-3aa1-b1fd-e3e251234ba7 | -5.79639 | -45.9296 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 116c779b-67c4-3238-8ad7-f44adfe53a85 | -7.53066 | -46.72551 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 862961af-b660-3226-9014-0033dfef9ee5 | -7.42017 | -44.85918 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0679e20-3106-327a-b74c-4481ce8571df | -5.19744 | -45.58757 | 2025-09-16 04:02:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 538e438f-ad79-3ef5-8645-84d45585feeb | -9.36728 | -45.38658 | 2025-09-16 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cef7d4d-028e-32d9-85e1-cf49cf87e328 | -10.71325 | -44.73496 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9ba00a6-5054-3985-a05e-267f254cfeab | -6.16154 | -41.22405 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9f52c6d2-cea8-3172-abaa-52161174ae11 | -10.72173 | -44.76684 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c00137db-4793-3c61-9a0e-6252445e733c | -7.08066 | -44.55447 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec398c18-276e-3fba-b7ca-d56f6ac35552 | -6.6157 | -44.07903 | 2025-09-16 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed2b417c-ab7b-3300-be9f-1a329bce1de8 | -11.02159 | -45.05984 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26098873-7aa8-36e4-bc36-9ba643410ca3 | -6.42562 | -43.319 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 037a0de3-9619-3e73-b3a7-e44d605dbf29 | -11.60151 | -46.97228 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71755672-f270-39a4-8aec-a48d5cd94d16 | -12.05972 | -46.53546 | 2025-09-16 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2680fe9d-edc6-32e8-a3dc-7a1fffb8ecc7 | -6.15985 | -41.23474 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e79b4d8a-9dd6-3e58-a6e8-18bbbdb4712e | -8.09601 | -50.15458 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce107e07-a474-376b-a2c6-814869fbd719 | -5.54966 | -44.97251 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c862b8-0137-3688-81c2-ef9b3ed78881 | -7.66674 | -45.1449 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2f4a6fe-0b9f-334c-8a37-7db27393f4f8 | -5.77644 | -45.94343 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb921f18-7392-3de6-b113-01476f309606 | -6.18903 | -45.12507 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e684d01e-26f3-3353-8812-9304181b8500 | -6.4468 | -44.08817 | 2025-09-16 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc2c6d58-8aa1-3fad-a3d1-bd81756c6889 | -8.59026 | -46.34377 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce36a200-964e-3c15-bedd-7942c0d6ecb9 | -7.6908 | -44.48834 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fcdd846-569c-32e2-a035-ae24f2b9b6e9 | -6.16133 | -43.67229 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8eb4a46a-3852-3a90-a65b-c47a5b5a03a4 | -9.08801 | -44.85102 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 347d0ad9-4ed3-332a-9cf2-eb34652b2d5d | -5.20965 | -45.18182 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae1c2ea7-3935-3872-a9d8-2865f01bd745 | -7.27914 | -46.60915 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94be8b6d-9397-3ab7-9528-817295471923 | -12.10979 | -44.82887 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b27d1e96-608a-32dc-800c-5ac3a40eca4f | -11.71119 | -46.87011 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a83ef356-414b-3257-87ac-011802c1c77f | -5.97257 | -45.861 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc534adc-7475-37f6-973c-8bcfeeeeb93d | -8.97009 | -44.19334 | 2025-09-16 04:02:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90d97f9c-90a9-35f1-b36d-7939b1bc46e8 | -5.34497 | -44.81922 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0566e4a8-5641-3407-bb46-e962cff6bb2f | -6.40059 | -41.75652 | 2025-09-16 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4135f826-8d71-3176-923f-47d2b02c199d | -8.01062 | -45.66262 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fdb532c-cc62-38c9-bb84-523ee89998f4 | -5.97795 | -45.82946 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c6f87f7-552e-3210-9d12-068b7fa9ff0d | -6.37448 | -44.41032 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 167800c8-c010-3b34-bad2-a42b6e84406a | -7.55003 | -44.0193 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6d74aa7-396a-3e64-9001-26ea7a039c39 | -6.92334 | -44.77164 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c56d0eec-ffce-3ae8-8c99-9ad04e5351ac | -11.11877 | -45.33308 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 407e820a-7928-3c16-9519-2181396867f6 | -6.16766 | -41.22865 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| faac32ae-d66f-353d-af90-1345fc282956 | -11.28059 | -50.79537 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2153baee-1e08-376c-81b3-30fa9c49b5e0 | -6.15959 | -45.99557 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b492eba-419d-3e7d-bfa0-3853902db081 | -5.98997 | -43.70547 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dc59688-6ffa-3657-8602-896ec0a08951 | -9.76014 | -41.88235 | 2025-09-16 04:02:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8b01d2de-4cb3-34db-a614-5a4846c60fe5 | -11.13153 | -45.35004 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 050832d0-bee1-3914-bc36-4791ef7b315c | -10.73444 | -44.7593 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 284a3b4d-4824-32d2-988f-a03d791fb4cd | -11.47752 | -43.58639 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6e865936-3ca8-3104-b976-b6951fe2af94 | -7.27265 | -46.59462 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8a04268a-7329-32b9-913d-2968c4e749aa | -8.98974 | -45.76054 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a057a217-a63c-3970-9ef8-2e04104acfea | -6.14822 | -41.17828 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 859d01c0-75f0-3f86-9072-c15593326f45 | -7.43673 | -46.17297 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ecb2f03-74bc-353f-b7d3-2d42c8ed7d70 | -6.18656 | -41.19202 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f2a369b4-ccee-3dee-bd9e-645e9963170b | -6.83151 | -47.84867 | 2025-09-16 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1e77ba9f-5ad7-327e-a3d6-60263202a8f8 | -7.67899 | -46.28291 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dded747-c76b-321f-8d6b-9ecf58cb0316 | -6.96573 | -44.44991 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6fd41490-15c3-3d77-a247-5e5ad653a2dc | -5.81097 | -43.4951 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e526a02f-1fd7-38d3-bfbd-10da9a6b1c7c | -7.81057 | -46.12447 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92d2b05f-fd51-3187-85bb-cf4ef2f6bc81 | -6.2787 | -44.00149 | 2025-09-16 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d3f0793-a9fb-3fec-80b2-b0b2a250bc4d | -5.77404 | -45.90538 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 538e87d1-f94d-3116-a65d-141dc6509a92 | -8.87988 | -46.18121 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7401a552-5357-31fa-a17d-75d814a9eea0 | -10.71821 | -44.74309 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 53043ff3-c52f-3208-ad4d-43964f4bbbaf | -11.27891 | -50.79485 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2188d29-e8f8-3548-b7b9-87f55942eaa3 | -6.18038 | -41.2092 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 00a5db42-7163-3170-9a78-000ab587a8e6 | -5.53833 | -42.66023 | 2025-09-16 04:02:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 2a240fa2-edb9-3228-909b-14374c3708a0 | -10.79847 | -45.97864 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 708e5a29-67bc-386c-8ac2-5c5942d7acf7 | -10.63115 | -44.21476 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec62842a-4002-34ce-a0f4-fcafa648c68c | -10.71509 | -44.76117 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bd8762d4-637b-3555-b9d8-2302e2b4cb24 | -10.71803 | -44.76625 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48147d19-002c-3b41-9b21-49ce195dd79d | -7.99086 | -45.65587 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 772cac14-9939-3a43-ac43-2951c36faada | -5.9974 | -43.70666 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b44c874-e5f6-3670-8f90-a178a2957b33 | -8.11288 | -48.27139 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cbc0935f-a5c0-34ae-a9cb-2c9d731cda96 | -5.7573 | -46.61799 | 2025-09-16 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b3e45f9-0909-34f1-b701-98c5a3310ceb | -11.43791 | -43.532 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac56ce33-8f5d-341b-90e1-e8727d12ed04 | -9.09147 | -44.80786 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67a35544-befa-3c8d-9348-3e7a5cc089ad | -11.33336 | -43.48354 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 405c214b-f282-3bc3-99ac-cdc0f5092865 | -7.69257 | -44.66918 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1affd912-221f-34d6-9bf2-ca07b8e7b01d | -6.3139 | -44.21177 | 2025-09-16 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f028a84-9395-3815-90a8-bedd6ec35da9 | -8.96287 | -46.01828 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2cabcdf-e306-39a4-9b10-c9d697f72585 | -11.4747 | -43.58192 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69514e8e-4aa5-3f78-80cd-28c90bc4f879 | -5.53479 | -42.65968 | 2025-09-16 04:02:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 45.7 |
| b908e3c9-224e-38e3-be3d-f8651e9f178f | -11.72494 | -46.48152 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d61a9093-cc57-313e-a8e5-2e5ef85f5191 | -6.92208 | -44.80286 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c6180869-3665-391d-a7e6-7dc3bc122ac3 | -5.98509 | -45.83878 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54ecdf0f-8fbe-346a-b48b-560471261ee2 | -8.11773 | -48.27218 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6367a52-ba6a-36df-b53e-4ff5565bdb1f | -5.77725 | -43.93014 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 233734e9-1b46-3347-925b-22772ec1e20d | -5.23684 | -43.69015 | 2025-09-16 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55cd12c5-2efd-3d37-bcfa-51bfcffe4c67 | -11.43653 | -46.94212 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1b407c0-89e2-3d50-ba41-8a98fc58f6c6 | -11.43558 | -46.92936 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22b5a93d-697a-3ffb-b51e-0edd1483a2df | -10.64214 | -46.23073 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfe13c56-340b-30c2-8256-afe3d0e975d9 | -5.74927 | -43.9353 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45cd4464-37cb-39c3-ac97-33f509625baa | -11.2776 | -50.80192 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README9.md)
