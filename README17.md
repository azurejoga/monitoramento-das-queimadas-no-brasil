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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f221849b-9333-3952-872c-f5b8493432a4 | -3.07089 | -49.41196 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25721459-05b9-3195-8d1c-8619fb012df9 | -4.66538 | -45.69823 | 2025-10-13 04:21:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab33fb21-cb92-3b86-93ba-c81a32afd73e | -6.48526 | -42.05736 | 2025-10-13 04:21:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| eb903993-c0bc-3a19-8287-04ee863d0a69 | -5.57984 | -41.10807 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 32388837-610b-30a6-9c4f-411834ffa430 | -2.46088 | -48.66146 | 2025-10-13 04:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3b72198-abb7-3d39-868c-b62fd885e03b | -6.16709 | -42.53982 | 2025-10-13 04:21:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e2f7b0d5-b51c-302c-a35a-48495768a993 | -5.10223 | -43.20244 | 2025-10-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 87dc7664-b8cd-3d4d-9549-603096d5409b | -3.40709 | -46.90013 | 2025-10-13 04:21:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51629ff3-9f18-3bea-b8b1-11749dd629f2 | -5.73299 | -45.27602 | 2025-10-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47923381-de29-3e5f-b0b6-e9675de9f8bb | -5.3531 | -43.42299 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 659fe217-f634-3d26-8b8c-09cd1a6f411c | -2.44414 | -48.99646 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5622063-177f-313e-9e31-c0a818cd6d65 | -5.93787 | -43.93621 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ec68257-2047-3472-bf07-d5ebc61607b5 | -5.91736 | -45.43425 | 2025-10-13 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60a21c1c-9d28-3d43-9c2e-33e39c9ae031 | -5.73954 | -40.76786 | 2025-10-13 04:21:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42c5d6b6-a00c-324a-b27c-dd1c2f8924f6 | -3.81719 | -45.76242 | 2025-10-13 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 42ff9ac3-36f2-3747-874d-a2ad950ee799 | -2.88023 | -50.73462 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89bf9137-bd63-3650-a763-baa3e0c2b292 | -5.46683 | -43.38962 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81076b29-3bd8-354f-93be-93d7d1eb6f38 | -5.58049 | -41.10379 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 52c95d3e-b39f-3fc3-9765-598460a24620 | -4.28948 | -48.579 | 2025-10-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83e9d795-d03c-34e1-9646-d54a5c223132 | -3.06733 | -49.40757 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 23da2589-bbc9-3478-bf8e-2f11b4b5a679 | -2.53548 | -47.79852 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c28fdd88-15e1-3735-8150-4792369c0d93 | -5.22212 | -43.79893 | 2025-10-13 04:21:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed220604-5de8-30e5-8e90-42f4777ba29e | -2.88377 | -50.74116 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0670295f-7eeb-3ac0-bf9e-32559263df63 | -5.93402 | -40.88274 | 2025-10-13 04:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec918b0c-2469-3db4-ab58-70c8511464b8 | -3.07149 | -49.40822 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac773b83-69cc-3d80-900f-cefcf03b5c27 | -5.38768 | -47.20726 | 2025-10-13 04:21:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb625353-951d-3e58-aec7-0a3fe82018b6 | -4.53351 | -42.88714 | 2025-10-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d8729eb9-2ec7-3d5b-9980-218f15041fee | -5.45898 | -44.12565 | 2025-10-13 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ded6f23c-1fc4-3609-8f11-b2dd36b9d09e | -5.41195 | -40.9788 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a14a25c9-e91a-30c7-9f3f-448f45230d99 | -2.99114 | -50.29158 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce39a556-61ad-37ff-89d7-7a283b0bdc1c | -5.45506 | -43.39872 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c34ad9d3-6d45-3a00-9e14-79a1f224578b | -6.23817 | -43.00851 | 2025-10-13 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b4e4ef7-1427-3c09-89da-ad9f10de3a58 | -3.8404 | -50.01298 | 2025-10-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2196f07-00f4-3c96-b900-5e9046607182 | -3.0203 | -50.44793 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7045d85d-b66a-371c-86c7-25705ad81061 | -5.47825 | -44.6475 | 2025-10-13 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 176d33fd-43eb-3410-8e65-8a69a095db41 | -6.2146 | -42.48489 | 2025-10-13 04:21:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca5a7405-40b3-3287-897a-2c92592a2898 | -2.54304 | -47.79981 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ff2c2a80-c696-3cc1-a199-c9f233d36000 | -5.56483 | -41.32735 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2df99990-f30a-3107-aa30-268b6c804cb3 | -4.48053 | -44.93807 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1fdb7104-9106-35d3-b3d7-6658bb3a6c4a | -3.84903 | -44.46435 | 2025-10-13 04:21:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67f99a60-8e2f-3635-bf07-44aef0945cbb | -4.48386 | -44.9386 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65dd8085-8443-32e9-b93f-d75ec624084f | -5.83806 | -42.30817 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 03f63669-c851-330c-bb7e-d47493e59c90 | -5.62806 | -42.69036 | 2025-10-13 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7427dffc-098c-3575-b655-16fa892796b7 | -1.89868 | -51.0072 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af4c831d-90db-35c0-a7e9-9623d75ea1a7 | -3.89543 | -44.12794 | 2025-10-13 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a0d942a-e920-319b-90ad-ce7120f24ce0 | 1.90594 | -55.68923 | 2025-10-13 04:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94bb89f8-f9fe-33d3-a575-b48a98373535 | -6.22019 | -41.57071 | 2025-10-13 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f45c48cc-ac11-3b94-b28f-56f112a7c238 | -4.88923 | -37.49764 | 2025-10-13 04:21:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| b163d86e-2308-3a87-95c3-c09de098c3d2 | -5.73702 | -43.83645 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c0cf5d6-f475-3813-8cff-045a1f92533e | -5.45954 | -43.39213 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 141939f7-7b12-380a-83bb-b4b1273fd37e | -2.53852 | -47.80371 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 28dc669a-0e7e-36c1-ac9d-c4c1a0ed31e1 | -2.60294 | -51.91769 | 2025-10-13 04:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98916c7f-ac14-309f-8284-cb817d844596 | -6.2251 | -41.56271 | 2025-10-13 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0cb914bf-4f52-3771-87ec-14f3b402117e | -2.91585 | -48.75434 | 2025-10-13 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 762a3015-a2ef-38af-83a1-f31313031049 | -5.22546 | -43.79946 | 2025-10-13 04:21:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 063898a2-c3de-3666-acdc-e187455fb306 | -3.17028 | -40.15762 | 2025-10-13 04:21:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07ee8cf3-7298-3c57-b80d-c1898b2bfecc | -3.72237 | -44.4093 | 2025-10-13 04:21:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9416dda9-3fbd-3f4c-a500-577118629625 | -3.09429 | -47.01936 | 2025-10-13 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03978750-f945-3048-a9d7-78937b9442e9 | -2.88451 | -50.73655 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cef14226-2159-31d3-b061-42a4c2c11dde | -2.92617 | -48.29945 | 2025-10-13 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f7afa7b9-72ba-3eaa-a4a2-c5d51b19aab2 | -3.27111 | -53.27413 | 2025-10-13 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b61e2343-c2fd-3115-9810-3fd98219ff96 | -5.47938 | -44.66189 | 2025-10-13 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f267812-c9ff-30c9-84d9-c756b9914d42 | -6.24158 | -43.00906 | 2025-10-13 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 47d21fd4-595d-3367-baf8-1ff3a1b42d5d | -5.29717 | -47.86221 | 2025-10-13 04:21:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e9acb7a-d216-34ff-b407-0946c3774453 | -5.4406 | -44.09072 | 2025-10-13 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f55960d-66cf-3ba5-8048-46b05f9a2209 | -3.09817 | -50.37782 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f8c01398-1732-35f3-a215-616703186d55 | -5.62347 | -42.72009 | 2025-10-13 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f5c4fbe5-d850-35b9-86b6-6c565c5475c8 | -5.65529 | -43.6115 | 2025-10-13 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0424e459-0f7c-3659-ac59-c7483228912d | -5.8849 | -44.21398 | 2025-10-13 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5354819f-d421-3b6a-846a-7c650583d094 | -5.83108 | -42.30715 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 16a46916-0cf1-385d-9b1a-ca6a5b85600b | -5.83976 | -42.32023 | 2025-10-13 04:21:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d9cb6d19-85cd-3e2f-bddc-408f6df7134b | -5.06841 | -40.47243 | 2025-10-13 04:21:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7793a7e6-1f2e-3eaf-86fc-a8432534da43 | -2.87945 | -50.73922 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0c8cf5a-a331-33bc-942c-2777a1d5c07f | -3.91787 | -50.01231 | 2025-10-13 04:21:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5017852e-a5f9-3e4b-bd55-69c0d09c114d | -3.73294 | -45.41274 | 2025-10-13 04:21:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cbf81b9-28d1-3a3a-9d79-67fe08681a6b | -3.06378 | -49.40318 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 82130840-f6fc-3891-b9bf-bb90caa78335 | -5.81456 | -44.03155 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9ef7a40-227a-3b00-a1c1-f78ae20197df | -5.33227 | -44.84119 | 2025-10-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc33f8eb-bb35-301c-a4f8-5d941f3a0795 | -4.91187 | -41.53373 | 2025-10-13 04:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c28c457e-0961-3dac-a9c6-bdde067660ac | -5.56551 | -41.32301 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 21492624-4fe5-3082-bf2a-a65230622639 | -5.48212 | -44.64455 | 2025-10-13 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ecb24f6-c43f-32e2-b4b8-0f0ca98b50d2 | -4.86904 | -45.91126 | 2025-10-13 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3811c08c-4ee5-38bc-8f2e-31a5c469b59b | -5.83632 | -44.06713 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46bff1aa-5ef1-3d66-8596-c5239852e9d4 | -3.06317 | -49.40691 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4df317bd-cb5c-3413-8d8d-7dcaaa9d1353 | -1.25309 | -49.05161 | 2025-10-13 04:21:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88f31119-974e-3343-a937-a3ae073e82ce | -3.60625 | -42.74593 | 2025-10-13 04:21:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d56aa655-0914-3a99-b582-392285e36fa9 | -4.01434 | -47.35056 | 2025-10-13 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e527a12-af1e-32bd-98ed-910a3a11a203 | -5.28904 | -41.03809 | 2025-10-13 04:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 84eeba46-78f4-322f-a2d7-470cf6ba1c65 | -5.486 | -44.64161 | 2025-10-13 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 174a46fe-0122-33d7-a1d3-f15ff194efca | -3.3662 | -40.63323 | 2025-10-13 04:21:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 872d67ff-8ba8-3760-8791-0125ab566bb0 | -5.4545 | -43.40228 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e98a0715-ae16-337b-8f7a-2177b245278c | -3.92215 | -50.01301 | 2025-10-13 04:21:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f609945-55fe-37de-b59c-75c06349a135 | -4.47432 | -44.94076 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 167ede57-73f3-382d-9f15-531a8fea7362 | -3.68391 | -45.43798 | 2025-10-13 04:21:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82ef1ab8-a568-36a2-9535-dd9da691c4ee | -6.5555 | -39.98584 | 2025-10-13 04:21:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 72786142-47ca-3ee4-8d5b-df99efa50bfd | -3.58884 | -47.28319 | 2025-10-13 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f2e0e4ff-90e6-3ed1-a083-38845cda35b8 | -4.30413 | -48.10673 | 2025-10-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd37e10f-33cb-3ebc-b6e9-5530778e901c | -3.06256 | -49.41065 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e06481d1-5780-3d12-a346-0f7dcc3f0fbe | -5.35366 | -43.41945 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa840e3f-345e-3f39-b35f-aee42853e048 | -2.45872 | -49.03582 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
