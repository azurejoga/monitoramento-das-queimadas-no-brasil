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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f210f93-ec75-3838-80a7-252afcb6ebe6 | -10.91784 | -44.69921 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b92109f-8ba7-3233-b4e4-ea1ddc1113b5 | -10.91376 | -44.6908 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1475e364-2bf3-31f5-8ee3-ab2979c93920 | -10.91296 | -44.6977 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdd82654-9856-343f-94a3-8ba23fd2101c | -10.91215 | -44.70459 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a7d8efe-4379-331f-b665-c56ac27a9508 | -10.91135 | -44.71144 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0925d09f-6073-3842-877d-095a937408d3 | -10.91076 | -44.6986 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8166d18-d717-33c4-8de9-82f181351995 | -10.91 | -44.70551 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5af590bf-2551-39c6-9776-89b7388495ce | -10.90924 | -44.71236 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45933cbc-5aae-379b-afe7-9761d85bdba8 | -10.90507 | -44.70402 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee410053-74d4-3df8-a6a2-e6e732a74ea3 | -10.87257 | -44.79993 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce503884-616a-35bd-8260-beef86b7e92e | -10.86557 | -44.79908 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e903f048-c059-3155-80c3-48cbd686887b | -10.86479 | -44.80583 | 2024-10-14 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 325b0963-5ca1-3ee3-9e95-23d4653f9f3a | -10.81989 | -44.95092 | 2024-10-14 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 410d9f3e-b043-3849-ba11-f5a094faac97 | -10.81913 | -44.95758 | 2024-10-14 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9f5a1d3-b5ef-306f-8a76-cecce31ffa46 | -10.44184 | -44.9493 | 2024-10-14 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc2e20e1-c64b-3405-9554-abb514b81b82 | -10.44179 | -44.95078 | 2024-10-14 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f0e7f085-585f-3495-b7a6-357bd42d05bd | -10.44106 | -44.95583 | 2024-10-14 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c5aaba6a-12dd-31f5-ace9-e5abca48090c | -10.43645 | -44.93549 | 2024-10-14 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 334ad9e5-26af-3bf4-8f72-75b91f67e481 | -10.43567 | -44.9421 | 2024-10-14 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e320fd5b-b1b8-3f6b-b97c-fa3cd7d6f79c | -10.43491 | -44.9486 | 2024-10-14 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5526d76-f3b2-36bb-8dda-22f0b524380a | -11.92394 | -45.77782 | 2024-10-14 05:10:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de6eb954-5065-3599-bc51-86bd6c2aaa26 | -11.92325 | -45.78381 | 2024-10-14 05:10:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebc46da4-2880-331c-8f7b-32cacb1b80a7 | -11.91656 | -45.78306 | 2024-10-14 05:10:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81349d77-5b93-36da-adc2-498d73b29815 | -15.08509 | -46.50634 | 2024-10-14 05:10:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b90fba36-d1a1-3cf0-b915-409e9e91b8e6 | -9.49069 | -45.83498 | 2024-10-14 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9c844535-a81d-3c8f-8d48-dbc27955b58f | -9.48419 | -45.8343 | 2024-10-14 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 48b1601d-d6e7-38cc-af11-6978bf8cdccd | -8.71521 | -46.64085 | 2024-10-14 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0aac3504-cd48-3ead-9513-74c4a63b4ed1 | -8.70961 | -46.63602 | 2024-10-14 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb2d991c-55f1-3b92-88b2-66107ca390e0 | -8.70903 | -46.64061 | 2024-10-14 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7789abee-3b56-3acf-a62f-798168770991 | -9.99438 | -47.29818 | 2024-10-14 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b845ffbe-007f-3e37-8c8a-f90879a4ba46 | -9.99086 | -47.29873 | 2024-10-14 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d5344a1b-eb82-3057-a11f-75a463064ff9 | -9.98318 | -47.31131 | 2024-10-14 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 816f07f9-73a4-30c5-88d9-054468d26c25 | -12.44207 | -47.92103 | 2024-10-14 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e16bdd78-3891-365f-b65d-6e29b00ea749 | -12.44255 | -47.91685 | 2024-10-14 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aecf89da-3a12-3124-8ace-e897278eb0cf | -9.10057 | -47.78452 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eff9f85f-09e8-3f53-b34f-86080f378fc8 | -9.09805 | -47.9378 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a94c8118-7e5c-30dd-af5f-a88034890989 | -9.09706 | -47.94542 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61fd426f-b3b6-3c2c-aa7d-b3e154ce7dcd | -9.09656 | -47.94926 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9121bbac-2df4-3ba8-a84e-e64b356f5c19 | -9.09487 | -47.7837 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3fbbe95-d7dd-3380-a341-6539993c2ac3 | -9.09142 | -47.94464 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78d9b05d-7192-323d-8f3e-19b49071fadf | -9.08867 | -47.78685 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e34d0f46-fe1e-3743-954d-591b52046b09 | -9.08295 | -47.78615 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f87d98dd-e81a-3522-b243-05e1d87b834d | -8.98632 | -47.7532 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ff2d845-3e03-332f-a6af-cef8b2420198 | -8.98114 | -47.74827 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6acc6c1e-4673-3860-a3a7-5cf5517d8990 | -8.98064 | -47.75223 | 2024-10-14 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d4664b4-22c1-31d1-9008-ad3be9584880 | -8.91709 | -47.91096 | 2024-10-14 05:10:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48879b16-2793-3638-a6a9-d7e4f09c2c00 | -8.91659 | -47.91478 | 2024-10-14 05:10:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fe1b5e0-0456-3055-8e83-e80f2bc67fb4 | -8.91096 | -47.9139 | 2024-10-14 05:10:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb4add93-a06e-3c78-8df4-b9751dac4a75 | -8.90533 | -47.91308 | 2024-10-14 05:10:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af446bff-d0a0-3f86-ac0c-52a51a27d318 | -8.60314 | -48.61878 | 2024-10-14 05:10:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc52817b-148d-3f9f-9ad2-486711f5dfff | -8.60264 | -48.62249 | 2024-10-14 05:10:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fa7c556-60b2-33bb-ad6d-421d18e09a86 | -8.6021 | -48.62643 | 2024-10-14 05:10:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1cd2dde-4df9-3c35-81c0-f60998f53832 | -8.48387 | -48.62854 | 2024-10-14 05:10:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31424449-a067-3b7c-a66b-bb9a428e547d | -8.47899 | -48.62429 | 2024-10-14 05:10:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8257772e-f3c7-380d-864f-df03fed68cd3 | -8.47851 | -48.62785 | 2024-10-14 05:10:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c44d046d-c27f-3374-8a1e-cd5412dc7373 | -9.99777 | -48.86311 | 2024-10-14 05:10:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5953dc04-c16c-311d-b18d-c1cda2a92fac | -9.99288 | -48.85875 | 2024-10-14 05:10:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c227764d-6034-3887-91a8-7ba3b8d586f7 | -9.99078 | -48.8555 | 2024-10-14 05:10:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b9054a6-22b5-3e55-8260-547f2061977e | -9.99033 | -48.85913 | 2024-10-14 05:10:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5143f408-e82d-3f92-99d7-f9bd33fa1638 | -9.53564 | -47.61831 | 2024-10-14 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1eb1e78c-7fc9-33e5-bea9-4dc76123ae07 | -9.53511 | -47.62252 | 2024-10-14 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ce79d29-e2e8-3eb0-a0d0-0f0642b52b04 | -9.50216 | -48.67403 | 2024-10-14 05:10:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3036b0fb-12a4-336a-b140-745a92695e6a | -12.92917 | -49.25883 | 2024-10-14 05:10:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4558fd9a-3dee-31ea-b9f8-3e966bea9259 | -12.92372 | -49.25816 | 2024-10-14 05:10:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e92ed60f-8c5d-3a94-8712-0fd05ce17c55 | -7.96477 | -49.06688 | 2024-10-14 05:10:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abbd38b6-f125-3f3d-b54d-25560d35c81c | -7.96047 | -49.05982 | 2024-10-14 05:10:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dd8f923-f353-305a-972c-21f2a2fc1647 | -7.96004 | -49.06295 | 2024-10-14 05:10:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16e70a5b-eb96-31ca-9df9-892dbd0e0b2e | -7.95962 | -49.0661 | 2024-10-14 05:10:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62f52df8-835a-3ed8-88c0-4bb603a074af | -7.9592 | -49.06924 | 2024-10-14 05:10:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e10db2c3-41fb-3ada-8241-7dbbbc96d9c6 | -7.95531 | -49.05909 | 2024-10-14 05:10:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3537279-be92-330a-9774-4793364c7e32 | -7.95489 | -49.06221 | 2024-10-14 05:10:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acde1896-36b2-3190-a2df-8c7ae258ad35 | -7.95448 | -49.06532 | 2024-10-14 05:10:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3acf70b-276f-3730-8b81-c8e638cb57fa | -9.16289 | -49.82965 | 2024-10-14 05:10:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b814b522-4b3e-3a8a-9860-da8bd1055204 | -8.65889 | -49.92569 | 2024-10-14 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4b8af65-9cd7-3051-b2cc-e5e04752970e | -8.65661 | -49.92111 | 2024-10-14 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e0a7194a-2f3a-3359-9190-a6bed9eaeb3a | -8.6559 | -49.92657 | 2024-10-14 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90141bff-b7ad-3929-b513-04762e110585 | -8.65398 | -49.92501 | 2024-10-14 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 665a0922-774c-37e2-9ce1-be1b387a6c87 | -8.65323 | -49.93046 | 2024-10-14 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d476cc-37b0-3d15-b6f0-a90105fcedc1 | -8.33521 | -49.97155 | 2024-10-14 05:10:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 571b17e1-cc29-3d52-9fcc-f39432432a8f | -8.18231 | -49.94332 | 2024-10-14 05:10:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55c528f4-f94a-361e-8d9e-d067f8584142 | -8.0631 | -49.39856 | 2024-10-14 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 738614dd-b48e-3b07-afc2-47216e43fcb3 | -8.06269 | -49.40152 | 2024-10-14 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0c2a954-5ed9-3116-beb9-e7c780e8c139 | -8.02569 | -49.63226 | 2024-10-14 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3698af08-48a5-3ee0-bb00-cc844ac7922e | -8.02491 | -49.63787 | 2024-10-14 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c11fc80a-6e0a-30f9-8abb-6721bef91644 | -9.62273 | -48.98734 | 2024-10-14 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c5cf75a-c550-3d04-8bc8-f35e7296cb7f | -9.61785 | -48.98336 | 2024-10-14 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02c55b0c-39ce-3277-9c67-c834c246a418 | -12.31049 | -50.23905 | 2024-10-14 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3de37471-ea5e-3362-87cb-3aec25c17c83 | -12.31012 | -50.24204 | 2024-10-14 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfdee102-a993-3815-b495-33cdab7ae608 | -9.16891 | -51.49069 | 2024-10-14 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9befbfc-1e8c-360b-a1c3-4acbc71b4634 | -9.16835 | -51.49467 | 2024-10-14 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dd88263-4442-3537-a25f-7bc010e24f66 | -10.54808 | -50.84241 | 2024-10-14 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 303d2d11-d38b-3c25-a574-c7a146ba4dfb | -10.54335 | -52.0965 | 2024-10-14 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce2ac6c3-48ea-39ad-b4d6-6213873518a4 | -10.43261 | -50.83213 | 2024-10-14 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 429e34cf-356d-3c80-b305-f51230d509e0 | -11.40426 | -51.23855 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b89e9310-79fc-3421-9245-b3e84e702bae | -11.40167 | -51.23558 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26dd3bc1-fa9c-3a68-9ec6-1eb52c747b7e | -11.27189 | -51.33068 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48a9225f-b2a6-3ba4-8a35-dba493ad7900 | -11.27122 | -51.33553 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1749ce62-f9e8-338c-beee-a5f7ded6ac36 | -11.2633 | -51.32453 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7305721-919a-3f34-82d1-1507fe0c54da | -11.26191 | -51.32633 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4270e054-e827-3bc9-8cd3-e9ad6a2c711f | -11.25867 | -51.3239 | 2024-10-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README114.md)
