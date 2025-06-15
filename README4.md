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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32236372-f4da-389c-8573-90d781c3d42b | -13.9062 | -54.6084 | 2025-06-15 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 4e8fd75d-d11d-3fb5-a19a-417d0364cfba | -13.9059 | -54.6291 | 2025-06-15 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 597a60cf-095c-3c2a-b0cf-dbc350b338c1 | -11.0113 | -55.0764 | 2025-06-15 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e8f580c3-5436-329d-b185-a121b44a655e | -9.4158 | -48.4504 | 2025-06-15 03:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2e7fa1df-600d-39af-a031-6cc5c9cc6c6f | -18.74968 | -40.07726 | 2025-06-15 03:08:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cd43dd6c-5d6f-3f57-b0fb-509e55eaa50f | -13.9065 | -54.5878 | 2025-06-15 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 7b704a25-cce9-32fa-9d6f-f77d23e28b4a | -13.9257 | -54.5856 | 2025-06-15 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| eb2a7370-f381-31ef-8091-cc1d730a67b0 | -13.9251 | -54.627 | 2025-06-15 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 242e8f2b-5071-3977-8c81-1c2357f19bc5 | -11.0113 | -55.0764 | 2025-06-15 03:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 28f4e2ae-b678-30d9-a818-b41da3cae132 | -13.9254 | -54.6063 | 2025-06-15 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 3a19bb9b-b93a-3c95-b4ee-3bc58ab70014 | -13.9059 | -54.6291 | 2025-06-15 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 67989c39-e7a6-3935-8b29-e7473c8e8cc6 | -13.9062 | -54.6084 | 2025-06-15 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| f860589a-de50-3bf6-abfa-a0921a3c358c | -9.4158 | -48.4504 | 2025-06-15 03:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 64d5236a-8152-37ec-93a4-df9cdc2acf2f | -9.4158 | -48.4504 | 2025-06-15 03:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 9714a9b4-08be-30a5-98c6-2c698ad2a143 | -13.9062 | -54.6084 | 2025-06-15 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 6ae335e5-d432-3759-a329-ceaed127b446 | -13.9251 | -54.627 | 2025-06-15 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 157.4 |
| bc1e6923-7ca7-37b0-b968-60716e53cefe | -13.9254 | -54.6063 | 2025-06-15 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 257.3 |
| 0de35d6c-1cf6-3da2-b1b5-995b385bbaf9 | -13.9257 | -54.5856 | 2025-06-15 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 584f62b6-df9d-39da-93b9-83e98b396e8d | -13.9059 | -54.6291 | 2025-06-15 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 91584b0a-ef62-3a5d-b2aa-571788144a89 | -13.9257 | -54.5856 | 2025-06-15 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 7f185928-94fd-30d6-9440-b7dc14ae4158 | -9.4158 | -48.4504 | 2025-06-15 03:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 23a0dd4f-e5de-3f0a-952d-54c96c7e67b2 | -13.9251 | -54.627 | 2025-06-15 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 5a42e9a0-05ef-3d4e-96c2-53c151a2f426 | -13.9062 | -54.6084 | 2025-06-15 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 636e9bf9-3dfb-3680-813c-07613edf0da8 | -13.9065 | -54.5878 | 2025-06-15 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 72f50f59-542b-3372-bdc5-09ee6f5a1bdc | -13.9059 | -54.6291 | 2025-06-15 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b7aea5a7-1647-3494-a306-fee8ca56b355 | -13.9254 | -54.6063 | 2025-06-15 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 252.5 |
| 37177230-3944-30b4-ad30-491361243b5f | -5.21059 | -35.7577 | 2025-06-15 03:30:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 870ed288-6ff4-38bb-a1de-cfcc7985af55 | -4.49448 | -43.77599 | 2025-06-15 03:30:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c30f24f-cda1-35a2-a955-2cc5e10471c8 | -4.49431 | -43.78171 | 2025-06-15 03:30:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64a41ce8-4905-39d6-b495-9eab11eea256 | -4.49525 | -43.77627 | 2025-06-15 03:30:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af091210-21fa-3b93-8ba6-ed2d7f30246e | -4.4935 | -43.78144 | 2025-06-15 03:30:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 282d0664-3e5c-34d4-ba10-a94f96b0d20a | -7.23146 | -44.15149 | 2025-06-15 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3e1767a-2c9f-3cd2-aa7a-149e2cb905c4 | -7.20414 | -43.10917 | 2025-06-15 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2e51cb84-9273-3379-908c-7d40c9be920b | -8.07868 | -43.11328 | 2025-06-15 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| af9dd0a8-8452-34a4-bc46-9faf45d1057f | -9.03984 | -47.03006 | 2025-06-15 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6702f880-b498-33a5-bc47-ad05776da28a | -9.04067 | -47.02869 | 2025-06-15 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 304ed129-3eae-3022-a555-8589d9484f9f | -11.18445 | -44.49045 | 2025-06-15 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 71200d54-6fe4-3065-bf18-f61cb026beab | -7.20333 | -43.11353 | 2025-06-15 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b1f0774c-6b4b-3b3e-9c5f-2eea4f662c2c | -11.18445 | -44.49165 | 2025-06-15 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8eefb949-f00f-3e66-abd3-dcc426952741 | -11.77674 | -47.39674 | 2025-06-15 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce18df10-4bed-37ef-b546-b2b7eb8cce09 | -11.18623 | -44.48246 | 2025-06-15 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ee9f9f5f-2ba1-38b1-97d4-f3cf2172e66b | -7.20494 | -43.10477 | 2025-06-15 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 71cfb0c2-aff5-313a-bd3c-b49aa2f3b9b0 | -8.31494 | -46.21077 | 2025-06-15 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1823801-17de-31e4-b9e4-6c297bc1898b | -9.04221 | -47.02127 | 2025-06-15 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91fe327f-e636-3af1-8938-ee2a4f9bce7e | -12.42033 | -43.81861 | 2025-06-15 03:32:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77820988-0820-3001-90b4-32580fa5e28c | -11.7728 | -47.39583 | 2025-06-15 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4cc57ba1-22b4-3cdd-aba8-133b716ca9fe | -11.19139 | -44.48833 | 2025-06-15 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6357c4b8-2c21-317c-bec2-c3c8383a124a | -6.68934 | -43.68732 | 2025-06-15 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9886100-c53b-3974-93dc-f18d3d5d5ecc | -5.63864 | -44.1146 | 2025-06-15 03:32:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10defb31-57e6-3a68-800f-bf9bb81b6ecd | -8.3093 | -46.20236 | 2025-06-15 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2829363d-5363-35bf-80d2-21ae6f261e9e | -7.22951 | -44.16192 | 2025-06-15 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e3ad7ce-ffec-3884-85e9-73646f3833cf | -8.31632 | -46.20379 | 2025-06-15 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c084f8b-3225-3de7-a148-0a732796b702 | -7.2093 | -43.11459 | 2025-06-15 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f1828729-6dc6-3f54-8ba0-efd01303b1df | -11.1863 | -44.4813 | 2025-06-15 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 625f972f-095d-338b-8d06-5132770566db | -7.2101 | -43.11023 | 2025-06-15 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| edab296f-b74c-363d-b38b-fea18f931923 | -10.14761 | -46.70187 | 2025-06-15 03:32:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10a0381a-18d9-3d4d-b1be-791ead6787f6 | -5.63962 | -44.10915 | 2025-06-15 03:32:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed91a200-2a70-3dd2-ab8a-d38e3ea5c520 | -6.4475 | -45.73121 | 2025-06-15 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 072a933f-fb8d-329f-9d4d-bc2b6508dc78 | -10.14623 | -46.70868 | 2025-06-15 03:32:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fa5637a-3aaa-3756-b6c5-5ad4df8cad75 | -11.18538 | -44.48587 | 2025-06-15 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e8ee61d4-073a-3710-a081-b2ceab329a6f | -11.18534 | -44.48705 | 2025-06-15 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 22846a16-05af-3ea8-a114-5fb50c49e0b7 | -7.21091 | -43.10583 | 2025-06-15 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 23fc8bce-1056-31c1-a641-6f4eaa4be519 | -6.21329 | -43.33366 | 2025-06-15 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec1cc898-e72c-394a-a1ee-57e5d96f0c05 | -7.23596 | -44.16264 | 2025-06-15 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71cb1043-82fa-37e8-bf2c-460c30e84840 | -9.04135 | -47.02253 | 2025-06-15 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de21bb24-1286-3558-8f88-cdb2fdb9e012 | -7.23693 | -44.15742 | 2025-06-15 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f47154ac-3fab-3466-9c74-7c4394e85529 | -8.30519 | -46.20402 | 2025-06-15 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02cee050-5871-34e4-bc41-3ffc2765f953 | -8.31221 | -46.20549 | 2025-06-15 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73bc30e9-1cbe-3929-ab6c-a76e06278357 | -6.44436 | -45.72791 | 2025-06-15 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4955361e-c897-3654-9620-a599e483f8d4 | -8.07282 | -43.11211 | 2025-06-15 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 57cd164d-ce7a-37fa-ae22-12b1b389885e | -6.44303 | -45.73482 | 2025-06-15 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11036425-8e80-3cf2-9aff-8df0fa5fe043 | -12.4211 | -43.81476 | 2025-06-15 03:32:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ce82a2-c36a-396f-a47e-7335869cc5b5 | -6.68314 | -43.68603 | 2025-06-15 03:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 775177bb-7862-3332-a3aa-d7091b5b3c92 | -6.44054 | -45.72939 | 2025-06-15 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03ea5807-bc98-33e7-9e0d-de1c16fc64f7 | -7.2379 | -44.15217 | 2025-06-15 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1422e0e-1c0d-3a97-8d41-906470e14ef1 | -15.41072 | -47.86587 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb768028-180e-3a23-b083-740e22673cfa | -15.40078 | -47.87794 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25392929-c714-3cb3-8f4d-ba67e120e664 | -14.83452 | -48.43267 | 2025-06-15 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08f2cd50-0a86-39fe-a038-bcf51f0abe1e | -15.39437 | -47.87812 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f83df609-e468-307f-a7e0-4b70e6746fcd | -18.74833 | -40.07441 | 2025-06-15 03:34:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 19269059-545a-3a2c-8d89-8fb20a5f82fb | -15.41421 | -47.88218 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 171774bb-e70b-374e-8e8c-bb7ddf7988c8 | -15.398 | -47.89422 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23c36343-30ce-339d-9699-00941308aa79 | -16.2954 | -40.20224 | 2025-06-15 03:34:00 | NPP-375D | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 43484c7e-b6e4-3ec0-ad12-dcbfa546989d | -15.4121 | -47.85984 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f52cb31-1923-3689-8999-f8fd398260b3 | -14.83275 | -48.4406 | 2025-06-15 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0c0c426-2030-37ff-bd86-d1816db6038e | -15.4092 | -47.87254 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65515e8a-48d9-30f7-a67f-bfb67f092cee | -14.83479 | -48.44019 | 2025-06-15 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4a2baf23-8b2e-31f1-a9bb-310f96e1964f | -15.40763 | -47.87945 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34640cf9-a051-3bb6-8c3e-2f305d055b1e | -18.7474 | -40.07685 | 2025-06-15 03:34:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2dd33a0e-8bbf-38e3-b79d-f234a8bda690 | -18.39264 | -44.19024 | 2025-06-15 03:34:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e4cd119-cfe3-3788-8235-74396758faa1 | -15.40587 | -47.88717 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65772d86-bbe5-35f4-a9e5-de0b2921845b | -14.82736 | -48.43124 | 2025-06-15 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc85e166-4b59-3bb2-b1e0-13bb83b0bf5a | -15.3991 | -47.8568 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e942171-0aef-341f-846a-df8ad27b8bb5 | -15.3997 | -47.88652 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 988d4d8f-3e45-3069-ac99-5e9bf5e4666a | -18.39782 | -44.19152 | 2025-06-15 03:34:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 462a371d-07d0-3884-8567-574a380869d6 | -15.40967 | -47.87399 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25ccb241-0a87-3cf1-ad7c-90f4391ab38f | -15.39915 | -47.88508 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f38f148-fe1c-3630-93e6-c89992fb7ba9 | -15.40544 | -47.85749 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d68e718-3771-388c-adc7-04786ccdb801 | -15.55967 | -42.62772 | 2025-06-15 03:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cb632e6b-6c71-33e2-87da-6c6a0fc172ea | -15.41255 | -47.86096 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
