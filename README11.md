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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f183897b-85b6-31a4-abbe-1ab17f7f37b0 | -14.8288 | -49.2008 | 2025-08-23 02:20:00 | GOES-19 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| ff345b83-3044-3f34-ab46-461fab190551 | -7.813 | -63.5656 | 2025-08-23 02:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 65e0feff-6f49-39b3-bf98-5775b7ad159c | -9.9493 | -60.1947 | 2025-08-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 359.1 |
| 0c327319-d377-3d59-bf47-070316513d6a | -5.7429 | -57.6009 | 2025-08-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 11ddf4d9-ddc6-311f-99b8-e47bb57d05b2 | -8.5943 | -62.6315 | 2025-08-23 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| f5c2628d-7a18-30f4-9cce-5bd36dcfdd6a | -14.8089 | -49.2259 | 2025-08-23 02:20:00 | GOES-19 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 5565a232-bd47-3069-a471-4fe85ad6efc4 | -5.7615 | -57.5807 | 2025-08-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 93e64a30-79d2-3efa-9e9d-45b83c6332d8 | -9.9492 | -60.2141 | 2025-08-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f94564fb-6271-395f-a456-24b11ef73e0f | -9.968 | -60.1937 | 2025-08-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 202.1 |
| 909c42eb-3d8e-3e26-a11a-7f11a5098d34 | -5.7431 | -57.5814 | 2025-08-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| d71ac6cf-2192-3288-9b10-204cfcebd28e | -14.8093 | -49.2038 | 2025-08-23 02:20:00 | GOES-19 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| ab098ea6-fd43-383b-974e-dca10a49c068 | -9.968 | -60.1937 | 2025-08-23 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 161.5 |
| f8b429d0-e33c-38f4-a140-1ea4a8404e32 | -14.3126 | -58.5431 | 2025-08-23 02:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d23658e2-454a-354f-9009-2a0403b15d39 | -9.1897 | -59.6171 | 2025-08-23 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 4dee4c4a-a6a1-3118-b6a0-9629fcb4a9ca | -9.9493 | -60.1947 | 2025-08-23 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 332.9 |
| dd2a26aa-dca9-3604-9163-022c1d7e169f | -9.9495 | -60.1754 | 2025-08-23 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 2b6db678-b362-3a01-912e-20fda4bd7ed7 | -8.5944 | -62.6126 | 2025-08-23 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 77f55b87-117b-37d2-a961-e75fe617acdb | -9.5181 | -60.5075 | 2025-08-23 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| efbf33e1-1c8a-3784-b725-2b3418c3cd77 | -7.813 | -63.5656 | 2025-08-23 02:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f33d3bad-a22d-3cfd-b121-f6bbe8d874e4 | -9.9681 | -60.1743 | 2025-08-23 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 0c13e335-5123-3723-8976-e9be05884b70 | -7.0164 | -44.6413 | 2025-08-23 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 71beed6d-87f2-3289-afd8-3c718cbb4914 | -7.0352 | -44.6396 | 2025-08-23 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| aeeb323f-270c-304d-bdb3-344ad712b34d | -17.5985 | -46.5481 | 2025-08-23 02:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 711840fe-dfa8-3500-9211-855069f0d3f4 | -5.7615 | -57.5807 | 2025-08-23 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| f6812055-ada8-3ada-8dec-70be7b10295c | -8.5943 | -62.6315 | 2025-08-23 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| e9dd4175-61d3-3d95-b84a-1908c662aa76 | -9.5177 | -60.5653 | 2025-08-23 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| f57c31f6-c3a2-3a3c-a935-b4f546eb6a3b | -6.6044 | -44.5624 | 2025-08-23 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| de104072-0eb2-31f5-b360-edb0fc2f011c | -9.5179 | -60.5461 | 2025-08-23 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| d82e4f79-b58d-3bfe-aaa6-509e0275599d | -17.5979 | -46.5715 | 2025-08-23 02:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 3bbc9623-0191-3367-a656-59180c7cead4 | -14.3317 | -58.5414 | 2025-08-23 02:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| e08623f9-82b9-3596-93fa-4d39341b63ef | -12.9921 | -45.2252 | 2025-08-23 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ca1ca37d-7491-3a8c-af9e-70082336427e | -17.5785 | -46.5523 | 2025-08-23 02:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e436018a-121a-3bc2-895a-97d743e3bbf9 | -9.518 | -60.5268 | 2025-08-23 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 0883f175-b228-3a6e-a645-d25295870c1e | -14.3123 | -58.5631 | 2025-08-23 02:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ea3dfe53-0379-337e-8623-bfa4caab45f9 | -5.7429 | -57.6009 | 2025-08-23 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| c07e3f57-d841-3c7e-a26e-25187021b5eb | -17.5779 | -46.5756 | 2025-08-23 02:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 945f994b-e603-3699-974f-0587ea543e4d | -8.8921 | -62.4297 | 2025-08-23 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f4a7d479-999a-342b-92d9-41d7554676ef | -5.7431 | -57.5814 | 2025-08-23 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 1a41a3f0-8c11-3be6-bbd4-c20d1835a74a | -9.5179 | -60.5461 | 2025-08-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 13e01e20-cde0-3271-ae66-db09cc2eebfb | -12.9921 | -45.2252 | 2025-08-23 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 10c7a5e1-69f6-3658-baea-16cc773976f9 | -9.5181 | -60.5075 | 2025-08-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1f4f3e0c-752a-3268-b42b-9bd63a2ed44d | -9.968 | -60.1937 | 2025-08-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 142.9 |
| e58a0967-26b7-3658-9642-98abf438f227 | -9.5177 | -60.5653 | 2025-08-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| bd831e2e-62a1-311a-a7f6-6a13e8645bc6 | -9.518 | -60.5268 | 2025-08-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 1099edd7-3eb4-32b9-812f-0174e0e68985 | -9.9495 | -60.1754 | 2025-08-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 54cd5c37-3083-382c-a7ba-fedcbf361409 | -17.5985 | -46.5481 | 2025-08-23 02:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7249d59b-e668-3c11-a86a-db437014bd46 | -6.6044 | -44.5624 | 2025-08-23 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| f9a72604-9938-3667-b204-d6c71d5cca4f | -17.5785 | -46.5523 | 2025-08-23 02:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 53f7c2c9-26ba-35a7-8e02-4ad2dfb95a8f | -7.0352 | -44.6396 | 2025-08-23 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0b928ac1-18ae-3fcb-8d03-c44069583144 | -7.813 | -63.5656 | 2025-08-23 02:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 31ac7c7d-a01d-3d53-a251-aff1f1b87f51 | -8.8921 | -62.4297 | 2025-08-23 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 316ef8c6-a615-3d6d-9b43-3d83414ea1c9 | -9.1897 | -59.6171 | 2025-08-23 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 826aa893-5a10-3e72-adde-36d473332cc8 | -5.7614 | -57.6002 | 2025-08-23 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 96eeb20e-49dd-33dd-8ef2-e1e509be3b53 | -9.9492 | -60.2141 | 2025-08-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2b8227a3-0b1f-3618-bb6f-7edf637f82aa | -9.9493 | -60.1947 | 2025-08-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 310.2 |
| 4887a48b-f792-3137-84c0-d5dd24ff1253 | -17.5979 | -46.5715 | 2025-08-23 02:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b2df1ec0-c8bc-314d-b842-270a6373ef0f | -5.7429 | -57.6009 | 2025-08-23 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| ee0c3322-8a6d-3266-b34b-b38882b4bacb | -5.7615 | -57.5807 | 2025-08-23 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b0fb2135-8fa9-3015-ba67-37e4b2caa0c9 | -5.7431 | -57.5814 | 2025-08-23 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 93ec0766-32c3-3b09-8947-52e17014e0b1 | -9.9681 | -60.1743 | 2025-08-23 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 168c17e4-cd2e-301e-acb6-373acb6e7508 | -7.0164 | -44.6413 | 2025-08-23 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 78433ee8-7960-3856-b42d-9aa421651fc6 | -14.37 | -52.06 | 2025-08-23 02:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| c3eb2245-d5f3-3d12-8d7b-c0b2e12f146b | -7.0164 | -44.6413 | 2025-08-23 02:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 3f015f90-9bbe-3c93-87ac-43aaf14c6564 | -9.5177 | -60.5653 | 2025-08-23 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a0668105-9778-397b-b0cc-a0130a93b95f | -5.7614 | -57.6002 | 2025-08-23 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| f1dfb09a-2c75-309b-89cc-6f582180fe62 | -9.1897 | -59.6171 | 2025-08-23 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| efa1788c-2b1c-332b-b3d8-7c4dc5e602f8 | -9.968 | -60.1937 | 2025-08-23 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 00dcc91e-9581-3639-b349-c4fc9250f841 | -6.6044 | -44.5624 | 2025-08-23 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 0d9ae982-837c-39db-b994-982b0667e27e | -9.1895 | -59.6364 | 2025-08-23 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| eb337796-96c3-3240-aeb6-fb2acb547c02 | -17.5985 | -46.5481 | 2025-08-23 02:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 54.5 |
| a9c2913b-d1ba-33fe-8635-0eda6ac269e0 | -20.097 | -47.7676 | 2025-08-23 02:50:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 46.8 |
| e9762fc6-5e16-3d00-ab6c-fecdcf9a374b | -9.9495 | -60.1754 | 2025-08-23 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 174.7 |
| c446a53d-d01a-34fd-8c2b-0eaaef9a15f2 | -9.5181 | -60.5075 | 2025-08-23 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6ba40ccc-0312-32e5-92c2-e73fd51671b5 | -5.7429 | -57.6009 | 2025-08-23 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ff55a4e1-42f7-33f0-8fc7-2f4a5d55c95a | -12.9921 | -45.2252 | 2025-08-23 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 93e19658-96c2-332b-84c4-7e2abc36232d | -17.5979 | -46.5715 | 2025-08-23 02:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 4c33191d-6d23-326c-85e6-8bd0dbd1f021 | -15.2083 | -48.6969 | 2025-08-23 02:50:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 37.9 |
| fa7ac16a-2d4e-342a-8544-ea2dc479e8a0 | -9.9681 | -60.1743 | 2025-08-23 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 2b9fc0cc-6656-353c-b17e-a98ef6145ea1 | -17.5785 | -46.5523 | 2025-08-23 02:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 4cd2db61-42b4-384a-a33e-675c0b814daa | -9.9493 | -60.1947 | 2025-08-23 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 278.5 |
| 5da1e751-f079-3d89-9499-abb53a0884d8 | -7.813 | -63.5656 | 2025-08-23 02:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 29a0b9f8-1212-32de-aa92-045a38ade25a | -17.5779 | -46.5756 | 2025-08-23 02:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 57e5fe05-71ae-3063-be11-044cb4f77b96 | -9.518 | -60.5268 | 2025-08-23 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 71773acd-adf5-3253-b5cb-c4305301f7e0 | -9.5179 | -60.5461 | 2025-08-23 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| db167115-faf9-3907-8583-cd99af5d2106 | -7.0352 | -44.6396 | 2025-08-23 02:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 500d2b34-5ca2-3d49-93fb-8274c988ac1d | -6.6044 | -44.5624 | 2025-08-23 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 4c28e340-57cf-3c1f-bc59-3607adf5b4b0 | -13.3971 | -46.2177 | 2025-08-23 03:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d42637af-64ef-3fa4-ad1a-e580819926d7 | -17.5779 | -46.5756 | 2025-08-23 03:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 1b7eff5f-028c-3e94-89de-cdaddac0eb94 | -12.9921 | -45.2252 | 2025-08-23 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6edbbef4-d8ce-3129-b897-ea95c2e9348a | -9.9495 | -60.1754 | 2025-08-23 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 175.7 |
| 710cb274-77d7-3097-89ed-21f2c801fe49 | -8.5943 | -62.6315 | 2025-08-23 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 373d6634-fbd7-3854-a0f2-5af538db85ff | -9.968 | -60.1937 | 2025-08-23 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 3015e3d8-878f-3721-bc30-fd397023a231 | -9.5181 | -60.5075 | 2025-08-23 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 572cf83d-2868-38c1-b318-f8c59eafa18f | -9.9493 | -60.1947 | 2025-08-23 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 281.1 |
| fad55533-10f0-3160-9c3d-94b162cd3d95 | -9.518 | -60.5268 | 2025-08-23 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a90eb0f5-78cd-3b12-99cb-ed41a056088a | -9.1897 | -59.6171 | 2025-08-23 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 326a1d08-29b1-30cc-86f7-d450fcbbc4da | -9.5177 | -60.5653 | 2025-08-23 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a05904b9-4758-3df9-a007-6e8ae5d1b7f3 | -7.0164 | -44.6413 | 2025-08-23 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 7f97becf-95d9-35a4-a226-ffe4a139549a | -14.2936 | -58.5249 | 2025-08-23 03:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| afef67a2-889d-3b02-a193-b74ba85b25a8 | -13.3583 | -46.2239 | 2025-08-23 03:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |


[Clique aqui para ver as próximas entradas](README12.md)
