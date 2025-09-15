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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ae02891-de4a-342c-89a7-1ecd622f5783 | -6.97416 | -44.54464 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 58f08ce7-512e-3746-b8fa-ccea7b88b2f6 | -8.64097 | -46.99565 | 2025-09-15 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f69a3ca2-95f3-3014-b175-e1282a63e6e2 | -8.97163 | -46.21169 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cb1ac04-963e-3ecc-8398-2912eab0ab21 | -7.29503 | -46.58128 | 2025-09-15 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12907d63-bdea-36ff-87a0-2abe9456b85e | -6.34393 | -43.16065 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df5c5411-cf94-3513-aad7-9978d15424d9 | -8.23698 | -45.8853 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d7eaf05-79d2-30af-9670-cb5bb195ab12 | -7.39147 | -49.99736 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4e272d3-459b-3049-bdf1-a363c431b67f | -7.86941 | -43.58196 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 62bb02f6-dace-37dc-b78a-99634a1249ba | -9.25263 | -45.65979 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d063d4f1-458d-3074-a5d7-cb2c692c092c | -5.28332 | -45.25705 | 2025-09-15 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13169ad5-2b61-3d21-8b79-cd0994d4dd9d | -7.85909 | -46.12294 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb5c1d60-4f09-38b9-8cbe-4b960a18417a | -2.26117 | -47.84919 | 2025-09-15 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 310ff171-a5c3-36f4-a913-a7b402ec3f5f | -8.96119 | -45.78379 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 461adc26-676f-39ec-80ae-ae6e41eedf84 | -6.17446 | -45.99485 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee3020d1-a7f7-330d-bd23-7756031ca56c | -7.87615 | -43.58301 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| ef0574bb-a74c-3846-bb61-752dbc9ff26e | -5.64145 | -45.94366 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44e88f9f-4c58-3f39-91e2-86982a6923db | -7.51327 | -44.70787 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38f77400-717a-3963-8aea-24f9a18bc111 | -9.05745 | -47.02096 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c52bb3d9-59f3-3373-9a92-fc84f4566199 | -8.42059 | -47.22547 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c6c37bb-d7a7-373e-ba01-f98143e39d32 | -6.68616 | -45.51174 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f5d21af-edd1-31bd-b9f5-53d8326904b8 | -3.47553 | -39.5415 | 2025-09-15 04:19:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b21d488b-4c35-3b0a-b56e-b41fa2f1fcff | -8.12051 | -43.67886 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cff17bae-c266-38ad-bae7-f9e2d7b4bc96 | -8.12608 | -43.66491 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ffa366d-690e-3b03-9573-5eb4afbe92ec | -6.45345 | -44.52309 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9c716b1-44d9-3053-8a06-ab784e82bf6f | -8.41254 | -47.23184 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c87adce-6786-3d3d-832d-4a7cb8c6ca30 | -7.43124 | -44.86155 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f39bd236-882d-35d4-8174-539194edd164 | -6.45015 | -44.52258 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2962c641-c978-3ab8-9290-2e9e90034662 | -6.32638 | -43.34293 | 2025-09-15 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e77156a-76a2-32dd-a9e3-6674599de6e2 | -7.67332 | -44.48754 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b610f1d3-c720-3497-81bd-a9ae867851db | -5.88255 | -44.90899 | 2025-09-15 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46cb45b9-e7b3-3495-ae3d-4de9bb75d3be | -6.76288 | -44.72038 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 201dea1a-7ef4-3291-9fe7-95736bdd5d1f | -8.14854 | -43.65353 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5de61e2-c48f-3576-8d4b-330380f7922e | -7.48953 | -44.68642 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6893ff5d-5023-3552-a8b9-7ab20b9cb065 | -6.45452 | -44.51617 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de4cef15-9ef3-330b-8951-1c0d638a5b49 | -8.91176 | -45.49139 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaf47a46-069c-39ff-873e-8e6641ba1f5a | -6.22679 | -43.74628 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd0f0608-39e2-3014-b635-9d436dd55ceb | -7.01927 | -44.53742 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebb1bcd4-38bb-3eee-8e19-6ced595dc87f | -9.08886 | -44.81102 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d25310a1-3aaa-3923-9806-5ef1bd6f09df | -7.3135 | -43.9325 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea5c9470-186f-3fbe-98c1-df8e1d0c2667 | -7.22194 | -49.59339 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a38eb4e7-840c-3420-9900-60a57ad48dd9 | -6.2539 | -43.46368 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72a38fc5-126c-3902-8ba5-59f020543fe2 | -7.86886 | -43.58559 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 89916f17-1db8-3f5e-945b-f534c13b326e | -7.86395 | -43.58459 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 06ae87a1-4ff8-3939-8a7b-b361d0214a12 | -6.44384 | -44.08085 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d549260-ab4f-3f02-a82e-c3c9dcca096e | -5.87446 | -43.71696 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b8b3612-2a7b-3105-8a74-7e854b185b11 | -8.14914 | -43.67221 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e52d8ffb-c80f-3aea-a041-7d2ebb71ac8a | -8.92213 | -45.46822 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75329de1-a21b-3769-9a47-1878806b1001 | -3.59613 | -47.51846 | 2025-09-15 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d3eec04-211d-3fde-b7f8-d36cd775503f | -5.84573 | -44.16547 | 2025-09-15 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 88a3d9c3-5ba5-3c3f-a05c-e6824a797ca7 | -6.52823 | -51.1918 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3fa62db-25e7-303e-a19a-23021e050981 | -9.06961 | -44.82587 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c898bfeb-1696-37d0-9467-351a5a00bbb3 | -5.9076 | -45.74287 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88400559-3a1b-3cc6-8bf2-0111f486b587 | -7.86844 | -43.57787 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf197d9a-f08d-3797-afa5-063120413a18 | -8.76542 | -46.07379 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 068138f3-9c91-3de4-b79c-5c9f738ddac7 | -6.45045 | -43.59972 | 2025-09-15 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a99a354-bcf2-3961-aa9a-9c87e5523cfc | -5.33021 | -42.70074 | 2025-09-15 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e6297d8-b4b9-30c6-ada2-bd6c3f60d784 | -8.63531 | -45.69231 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cc12b313-8644-3dfc-b579-e4184e3cf807 | -5.7944 | -45.87661 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3e92858-d8bd-3c3d-ac26-c8c06132fc1f | -7.21512 | -44.39434 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcf06b91-4f09-3308-9437-0db5aa475b10 | -5.80375 | -43.93148 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f44c97b6-2883-38ad-9a51-6d9380da437f | -5.08014 | -44.10208 | 2025-09-15 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60ff892d-cbe0-308e-88f8-e8048ac1f384 | -8.424 | -47.22601 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c79b04e-f5e6-3cac-91ce-4e00dbdff863 | -7.06024 | -44.11979 | 2025-09-15 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c80b5ce-da70-3478-967e-8daa5f856d13 | -9.09218 | -44.81153 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d0c6475-a5ba-3197-ab36-424659405422 | -6.05094 | -43.56356 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad7a103f-d7e1-320f-b6e6-e48ac43c0cf5 | -6.351 | -42.53822 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 25f57fae-a3d0-3df5-bd3f-51aa69fc8219 | -1.89126 | -54.61391 | 2025-09-15 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aa6e4a2-8283-3419-b8a4-08f0f7306573 | -6.078 | -43.15001 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 48f9eb49-da3e-3b22-a38a-fd4037a07b4f | -8.95945 | -46.22416 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbc987d8-4fcc-308f-8e76-a38c7f0dab1e | -7.98113 | -45.65125 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2cc4f12-5743-3993-8e7a-048a9fdb2761 | -6.17072 | -41.17485 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36d75614-a8ed-35de-a3a3-6ed947c1db10 | -2.39287 | -44.87635 | 2025-09-15 04:19:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59ec1e1e-54ca-3b70-862d-8ad1ca7ebb75 | -3.65402 | -54.05781 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a31b4c67-c287-392f-90e9-891257e2914a | -5.47739 | -44.69332 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fd02ffd6-e113-3f0e-bc78-703f3bc6e579 | -5.68196 | -43.48867 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 290024df-7656-3868-bbeb-4fdd26690d7f | -8.59841 | -46.35406 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d745ff80-8285-3424-88f8-d19d34432bf6 | -6.41015 | -46.94536 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5f1e7e9-2450-3979-9cad-144dbc4ed4db | -5.77113 | -43.92286 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42c0a339-379b-3149-bcac-87262f685d5a | -4.17993 | -48.57097 | 2025-09-15 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4440d3fc-062f-34f1-b0e2-8d41982f076b | -7.99844 | -44.84477 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c6bff6e-2706-3cab-9ba3-afcb3bdee3ed | -8.18209 | -46.76442 | 2025-09-15 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a61c33d-3bc6-385b-b0ff-5c18e07d9dcd | -7.88008 | -43.57991 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 0de20499-aade-3047-a39d-92e7ec2999e0 | -8.20996 | -45.58089 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de1904b0-cb18-3244-aded-47dceeb43ff2 | -6.40449 | -46.93673 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dc9c93e6-eb6f-3e81-8df6-181d46a9f4bc | -7.19921 | -44.3849 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5302b7eb-5f5a-3078-be67-2cd62fae4b8f | -7.49007 | -44.68297 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0c2db34-b89c-33f4-b625-760ae617a00d | -5.90427 | -45.74234 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df9ff337-dcc3-3100-9a20-2437b202c2f3 | -8.19461 | -47.12402 | 2025-09-15 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 205f6dba-e0b6-3df8-8e26-b37d34f3e8da | -8.14465 | -43.67895 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 010603bb-a2d7-3eab-a0c4-36f2c14da51b | -6.54006 | -39.87538 | 2025-09-15 04:19:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b312d8b2-3f61-324f-b100-ef8ca960720a | -7.84419 | -43.86153 | 2025-09-15 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bf02d24-6d14-33b6-a486-6f9448958a50 | -8.82256 | -40.66778 | 2025-09-15 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9b6fe177-2413-34ca-8428-efc6552d743f | -6.40788 | -42.62406 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c0a52f10-0704-3bc7-ba7e-fbeeb02a978d | -7.8716 | -43.56744 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fed0dd6-01dd-3d68-8014-675a46c1beae | -7.3063 | -46.57574 | 2025-09-15 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42a15242-b508-3656-b5f7-f8d13b07ecbe | -8.54018 | -40.23508 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 505a077b-a342-39b2-b53d-789b41d5b228 | -7.63851 | -49.72956 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8fbc913-eafb-3133-ac3a-e3ebc81aea00 | -8.61724 | -45.73931 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f38da84-53a3-38b7-8aeb-21e5da79f651 | -6.15872 | -41.18345 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9667a816-001c-3ab6-afc2-66d3d9131bf2 | -3.07612 | -48.82354 | 2025-09-15 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README24.md)
