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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16e26988-35b7-35fa-bf08-50880b4770a1 | -10.6561 | -50.900799 | 2024-10-09 00:40:30 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cec2a094-d3d1-3de4-8a0b-079343dd49f9 | -9.9267 | -47.722599 | 2024-10-09 00:40:31 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f292b0bd-56d3-3c97-9242-3bb99dc1027d | -10.6611 | -51.800499 | 2024-10-09 00:40:33 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d6d27f9-1b61-3992-9c6a-80ce893a9d70 | -10.6637 | -51.812801 | 2024-10-09 00:40:33 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3baa96-ddd7-3e08-ace7-dd5342da931b | -10.0082 | -48.838299 | 2024-10-09 00:40:34 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bc8b111-0f4f-36ef-998b-5d7aff672fa1 | -10.01 | -48.8465 | 2024-10-09 00:40:34 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c311cb9-76c3-3bdf-a6a8-1620601f38f4 | -8.2264 | -41.5481 | 2024-10-09 00:40:35 | METOP-C | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e767c819-8b4a-3274-841c-0fd882a7c9c0 | -8.1 | -41.068001 | 2024-10-09 00:40:35 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66a55bc9-b50b-374c-81cd-5498b7d25046 | -8.1026 | -41.0788 | 2024-10-09 00:40:35 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71afde66-0248-3c45-a274-4de9bd2c6914 | -8.1052 | -41.089699 | 2024-10-09 00:40:35 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ed5e03d2-8321-3a2c-a776-8221e37c4111 | -8.0929 | -41.0812 | 2024-10-09 00:40:36 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c13c7d52-16f2-3ca3-99cd-fad153fb6c0f | -8.7611 | -44.147099 | 2024-10-09 00:40:37 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3dcc43ed-31c6-3f56-a1a2-0c1296d3908c | -8.7629 | -44.154499 | 2024-10-09 00:40:37 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d31d00b6-504d-3b7a-9f83-2be2bf50be3a | -9.2627 | -46.687801 | 2024-10-09 00:40:38 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5f014fb-3e19-3c49-9999-03d2d47d3510 | -9.2642 | -46.694801 | 2024-10-09 00:40:38 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e457bfd-6357-3b83-9526-32511baca3d8 | -9.2658 | -46.701698 | 2024-10-09 00:40:38 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19bd4831-a48b-3e10-b058-53cad49d3cfa | -9.2674 | -46.708698 | 2024-10-09 00:40:38 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4442609-ce05-39a6-8fe8-7e42601a90b7 | -9.2689 | -46.715698 | 2024-10-09 00:40:38 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1188cf99-4cae-3202-a821-70d2ccfaccf3 | -9.2705 | -46.722599 | 2024-10-09 00:40:38 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 033b300f-b19f-37af-9b73-a52ca98141fa | -9.2544 | -46.696999 | 2024-10-09 00:40:38 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2846480f-2d33-31c9-a70c-4b13261ec405 | -9.256 | -46.703899 | 2024-10-09 00:40:38 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c59e9de-95b7-3cd0-b0f8-d70ae6258a7c | -9.2576 | -46.710899 | 2024-10-09 00:40:38 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cca1914-3085-31cf-81fb-947e9650830a | -9.1512 | -46.3778 | 2024-10-09 00:40:39 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d41d05a6-dfba-3bd4-ba0c-07e49e682679 | -9.1528 | -46.384701 | 2024-10-09 00:40:39 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 590cb643-b3cf-34bd-a4a4-c3cfafe36463 | -8.1495 | -42.952301 | 2024-10-09 00:40:42 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2000d485-7d6a-36a8-8c1a-0a8575d4f91d | -8.1515 | -42.9608 | 2024-10-09 00:40:42 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f3705186-f53c-3a29-94ac-5d2d155ea16a | -9.2049 | -47.944599 | 2024-10-09 00:40:43 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0eeefc4d-9d71-3f4b-b29b-d42ec385f08a | -9.2065 | -47.952 | 2024-10-09 00:40:43 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05bacae0-62a9-3852-a985-54bbe989143f | -8.3398 | -44.110699 | 2024-10-09 00:40:43 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e506c2b-9619-3614-b3ad-e31ce499ed27 | -8.3247 | -44.090302 | 2024-10-09 00:40:43 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 59cb0fb2-c00c-3580-9557-1c081414f0ed | -8.3264 | -44.0979 | 2024-10-09 00:40:43 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1edc4b2-b929-34a0-8f33-03d1e64b33b2 | -8.3415 | -44.118301 | 2024-10-09 00:40:43 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f755797-9827-306f-8e38-b38e39650e38 | -7.9245 | -42.440399 | 2024-10-09 00:40:44 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7113a8ed-27bf-3149-b7e0-da83929184c6 | -7.9266 | -42.449402 | 2024-10-09 00:40:44 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95a9c9db-c9ef-3cc4-b94d-5f333ae544a7 | -7.9168 | -42.451801 | 2024-10-09 00:40:44 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 101e715d-c5e0-3193-a4a1-5e277fb2117a | -8.3174 | -44.147701 | 2024-10-09 00:40:44 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff71f333-c665-3647-868a-f549c0358369 | -8.2925 | -44.129601 | 2024-10-09 00:40:44 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82bc23b3-ff67-3ef9-8ce0-09c6321111a8 | -8.4216 | -44.682999 | 2024-10-09 00:40:44 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c699fb00-f398-35e5-b398-699a2bca7dde | -8.4232 | -44.690201 | 2024-10-09 00:40:44 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 733c5f7b-be11-3804-9899-50b4d4bb4557 | -8.3149 | -44.092602 | 2024-10-09 00:40:44 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd46e7e1-2967-30ef-9b8c-e9aa238a503a | -8.3167 | -44.100201 | 2024-10-09 00:40:44 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ad30a730-7ca3-3f0b-9d8b-474cc7147fef | -8.3051 | -44.094898 | 2024-10-09 00:40:44 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ef871aef-0297-37f0-8dd7-c9dda548abd2 | -8.3192 | -44.155201 | 2024-10-09 00:40:44 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9eb6e670-cb3a-338c-a737-d4926bb2238f | -8.2971 | -44.104801 | 2024-10-09 00:40:44 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c51ac626-aab1-39bf-981d-df99f9e20b41 | -8.3094 | -44.157501 | 2024-10-09 00:40:44 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 801fcd69-8f96-340e-81d6-e5ded4b69be1 | -8.3076 | -44.150002 | 2024-10-09 00:40:44 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b890dcf-6708-3f88-b2a2-5f3f7dbf2efa | -8.9222 | -47.050499 | 2024-10-09 00:40:45 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78a7b2ba-e4f5-3078-9917-ae32c1095580 | -10.6221 | -55.856998 | 2024-10-09 00:40:47 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d38e1c6e-a066-30a5-a53c-a2d93266d7ed | -10.6267 | -55.880402 | 2024-10-09 00:40:47 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85a311e2-3ff7-37bc-8870-ef16f9ddb355 | -10.6124 | -55.858898 | 2024-10-09 00:40:48 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cba62bfb-5fad-3edb-9ae2-c136ccbd14be | -10.617 | -55.882301 | 2024-10-09 00:40:48 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 357c9128-54bf-3e00-9ae6-b3d7839e9be9 | -10.6217 | -55.9058 | 2024-10-09 00:40:48 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7da49a11-9129-324f-93df-86b8031a4406 | -10.6073 | -55.884201 | 2024-10-09 00:40:48 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8f80dd8-4bb9-36cc-9128-267a4855f7d7 | -10.612 | -55.9077 | 2024-10-09 00:40:48 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f4fa158-ed32-31a4-93fe-15690c184aa9 | -10.6166 | -55.931198 | 2024-10-09 00:40:48 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 779a3d0e-ea4d-3228-8028-aa93b78af657 | -10.5976 | -55.886101 | 2024-10-09 00:40:48 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2733e2c2-eccb-3d75-8079-98b277ed4e9d | -10.6023 | -55.909599 | 2024-10-09 00:40:48 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba8ee15-60b2-3a8c-95d7-657190bf22aa | -7.6584 | -42.407101 | 2024-10-09 00:40:48 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 76d32f2a-6eed-3025-b101-70059059444d | -7.6606 | -42.502998 | 2024-10-09 00:40:48 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2be85cba-88cd-3f60-ad3a-97565d838083 | -7.6628 | -42.5121 | 2024-10-09 00:40:48 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 622cbbe0-7ee4-3a55-ae7e-1281908feea2 | -7.6649 | -42.521198 | 2024-10-09 00:40:48 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 579a4383-ca61-3fae-8538-a216b51cd943 | -7.6552 | -42.523499 | 2024-10-09 00:40:48 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 997f6a45-aa9b-3adb-81f4-74b464e9fa8d | -7.6172 | -42.4072 | 2024-10-09 00:40:48 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab0f2d5e-b4d3-3ab0-839c-a6b47c992386 | -7.6194 | -42.416401 | 2024-10-09 00:40:48 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 52b8190d-2068-328d-af29-58c52d111a0e | -7.6215 | -42.425598 | 2024-10-09 00:40:48 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2b90751-d6c9-3860-bd8e-e90bf0e5f074 | -7.788 | -43.082298 | 2024-10-09 00:40:48 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f2bc9166-f768-39b6-93bc-b180fc7bf0ae | -7.79 | -43.090801 | 2024-10-09 00:40:48 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 74314094-908b-391c-af8f-289e08b462f0 | -8.1313 | -44.411098 | 2024-10-09 00:40:48 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b2d3848a-ad81-38d3-99c1-d0c4b8d124ae | -8.133 | -44.418499 | 2024-10-09 00:40:48 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 88ef95fb-cf35-3596-9b5e-699a0ce72dc4 | -8.1215 | -44.413399 | 2024-10-09 00:40:48 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a50d3bd8-5231-34d7-8511-ee357cad814f | -8.1232 | -44.420799 | 2024-10-09 00:40:48 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a91ad080-79e5-3ff2-8a80-c03817a0d4eb | -7.7173 | -43.0453 | 2024-10-09 00:40:49 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bdaaf7d0-d413-3af4-857e-5e9c867fc590 | -7.6117 | -42.427898 | 2024-10-09 00:40:49 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9099e7cd-ff20-361d-abe7-4ee7bc47eb32 | -7.7684 | -43.086899 | 2024-10-09 00:40:49 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bc5e50f4-f3b7-3e6b-9962-c0ce6d8f8cfc | -7.7704 | -43.095402 | 2024-10-09 00:40:49 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 537bee3e-ffa3-33d4-ae69-d7b02a0056ef | -7.7724 | -43.103802 | 2024-10-09 00:40:49 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e94eb9a3-2aa6-323b-af6d-74f8b07be6dc | -7.7348 | -43.0322 | 2024-10-09 00:40:49 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6f3644ab-dfc7-35d6-ab3d-dd73fd2d63c7 | -7.7368 | -43.040699 | 2024-10-09 00:40:49 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aa98a48d-d1a1-3513-9aa2-4cca5d84001d | -7.725 | -43.0345 | 2024-10-09 00:40:49 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c44e771-346e-3769-8b4c-ce8b2f2ca471 | -7.727 | -43.042999 | 2024-10-09 00:40:49 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 414ef8fc-3f5f-3182-b152-a3ae99450172 | -7.729 | -43.051498 | 2024-10-09 00:40:49 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c128c086-9381-3e65-872e-68bd007315ce | -7.6893 | -42.970901 | 2024-10-09 00:40:49 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61958db8-0b70-3814-9235-89d2180bcdc5 | -7.6914 | -42.9795 | 2024-10-09 00:40:49 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 927e513d-e506-3e83-b681-5d3c98dd8a32 | -7.6934 | -42.987999 | 2024-10-09 00:40:49 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bc85ae2b-7e09-3412-b25e-3680d37f0c2c | -7.6836 | -42.990299 | 2024-10-09 00:40:50 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 995729d1-c905-313f-940d-caefd1fdb015 | -6.7526 | -39.226398 | 2024-10-09 00:40:50 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4d6119fa-04e4-3804-8326-72fdeceb6ccf | -7.6816 | -42.9818 | 2024-10-09 00:40:50 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d233455-0d12-3914-a548-939d4b8c643e | -8.0028 | -44.347099 | 2024-10-09 00:40:50 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04daadab-f3a7-3c50-acb2-a50a0bdefdd5 | -8.0045 | -44.354599 | 2024-10-09 00:40:50 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9128d4f4-a6ba-3a15-83b8-1d246d1d8620 | -7.9982 | -44.371601 | 2024-10-09 00:40:50 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8e8f1154-83e8-37f4-9439-085ef84cbc60 | -8.0063 | -44.362 | 2024-10-09 00:40:50 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c8d8cfd-eaa1-3e47-9719-47e74c8e7415 | -8.008 | -44.3694 | 2024-10-09 00:40:50 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b5708fe2-1880-34ca-a957-61f2359d0f78 | -9.6606 | -52.230301 | 2024-10-09 00:40:51 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91c46c36-11bf-3852-9986-1ba147fa6aef | -10.3468 | -55.838699 | 2024-10-09 00:40:52 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf77555c-16c3-371a-b602-1399e7b9309d | -8.2424 | -46.279099 | 2024-10-09 00:40:53 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93775bc8-ae39-35f2-9123-25b5717e029b | -8.244 | -46.285999 | 2024-10-09 00:40:53 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30ddaf57-5f6e-3c7f-ab8e-0ab18aa62e22 | -10.5843 | -57.515301 | 2024-10-09 00:40:53 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91e80808-b6df-3bf7-ad71-2da9d6ac4e3b | -6.4368 | -38.822498 | 2024-10-09 00:40:53 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 189beb72-39bb-35a9-96bb-ef172680402f | -6.4408 | -38.838699 | 2024-10-09 00:40:53 | METOP-C | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7b71c0df-4228-363b-a772-2ea18957be87 | -7.6238 | -43.698898 | 2024-10-09 00:40:53 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README15.md)
