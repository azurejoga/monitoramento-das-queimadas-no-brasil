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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccf7a0c1-6fcf-3f5a-96a8-fc01242b6cbf | -7.4051 | -60.00328 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10427923-1481-31e0-8757-33c14f6b4119 | -8.57049 | -54.68591 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a479505c-c30b-3a9f-8087-f856a629447a | -9.37176 | -61.53994 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eda0f84-c3ac-3066-839a-5cced927e7ab | -7.25844 | -59.99812 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0168cf8-470b-3950-8b51-832c9d35b6a0 | -7.08805 | -59.18305 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd428e60-32db-3a1d-81a9-c48a85e7ba3c | -7.06597 | -59.21158 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2c8a8913-dcb0-3328-8a63-5e983a8aed47 | -8.56756 | -54.70876 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebf83b05-1fa1-39bf-a3f3-3501f996a9b2 | -8.93437 | -60.73451 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34ecc789-ebae-354d-9429-caee2002dc79 | -7.06821 | -59.19743 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eb59babe-bdce-31c8-962b-866d95aad504 | -7.06186 | -59.17916 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7b2e43c-d020-3024-8318-da59c8389a71 | -7.06622 | -59.17984 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65617996-3762-30f7-bea8-6631148bf6d7 | -8.9952 | -68.45941 | 2025-08-11 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41dcbb52-7467-39f7-8edc-3361631d1300 | -7.06158 | -59.18108 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b63fdf9a-596e-392a-8502-006bf61efec6 | -6.10449 | -59.92941 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ad3ebad-6539-3bc8-813b-1d360342dccf | -8.57654 | -54.68671 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4921073-a2df-3f5e-9fa0-e8f9b8ef305b | -7.40565 | -59.99948 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf60acdb-80f2-39a6-bead-52717cdefff9 | -9.38233 | -61.52168 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12c7739f-79e1-33b5-b957-d4470a1da1b6 | -8.76931 | -71.11015 | 2025-08-11 05:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05d757a2-849d-3bb7-851f-43ceed04bc1d | -7.07495 | -59.18117 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4d17eee-52d8-3b21-bfaa-36aca7d92e3e | -8.56504 | -54.68046 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f84ad9c0-a64c-3331-9382-321ba4cec180 | -7.05595 | -59.18901 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4038d3cb-991f-31f8-a420-bb40bc8c90f5 | -7.06783 | -59.16896 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40e8284d-e57e-30c0-92a3-c894a4e87bf8 | -9.37704 | -61.5308 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eda43807-590d-3258-b52f-ebacc327963d | -7.06283 | -59.20276 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e65f31e-b867-37d9-840a-3954a4d9a2a4 | -7.07614 | -59.17271 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8373a66-fe73-3156-93c1-ebe61c14d4b3 | -9.37001 | -61.52481 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e07553ca-c920-32f4-8b1a-3aae9c374836 | -7.08687 | -59.1914 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83650852-09ff-3b51-be5a-77548aaf022c | -15.42364 | -53.92131 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f733592-bb53-3c96-b77e-8dda7a7c6a62 | -16.29984 | -52.91856 | 2025-08-11 05:46:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8a59e472-8605-3b76-a5d4-8baab81124ae | -15.43176 | -53.91535 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9378393f-01a5-3469-89b2-a33d1001bb05 | -15.44359 | -53.93024 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 964ddf47-c8c9-3d21-a0a8-8fcd63bdaa8f | -16.30018 | -52.92041 | 2025-08-11 05:46:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c165d76d-fae3-3b28-a44a-fd1e4a294cdb | -15.43056 | -53.92824 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6aa6247e-3893-3b7a-8222-aa099a7475bd | -10.06638 | -67.92496 | 2025-08-11 05:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78d36cef-56b4-312c-9055-1a45a22735a1 | -15.44428 | -53.92996 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 659d292f-0fb5-37fc-a77b-86989d809ad9 | -15.42428 | -53.91487 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bdcbe81d-c834-3447-80f5-9fef75436e4e | -13.06777 | -56.84874 | 2025-08-11 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 049cd87e-cf34-32bf-b1fe-c6f1d1dd0d7b | -10.16504 | -69.00751 | 2025-08-11 05:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee19c62b-a2b5-3c72-9709-9447a5315854 | -10.16862 | -69.00812 | 2025-08-11 05:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50a0f718-d956-3df5-94ba-e0c440b8a049 | -15.43116 | -53.92179 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 794f5b3d-d234-3bbd-bb8d-d61e81cfe5d8 | -16.30749 | -52.92149 | 2025-08-11 05:46:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d615644c-0508-339d-b92c-09f05c9efa7b | -15.43802 | -53.92265 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7ac153e5-7f05-3b4c-aa28-f8fe823ad5da | -10.96572 | -68.49312 | 2025-08-11 05:46:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4cb7125-f77c-3b15-9e62-29fa8986c124 | -15.45114 | -53.93086 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 71a7b5d1-c1a1-32fb-a8d0-87e037667e33 | -13.06218 | -56.84816 | 2025-08-11 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2839f9f6-df7b-34cb-ac7f-599e478382cb | -15.42986 | -53.92859 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1f9102c-d5b9-37ea-abeb-b672253f7119 | -15.45053 | -53.93729 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a2bb49f5-db86-3d82-8c67-93cc2019224a | -10.067 | -67.92121 | 2025-08-11 05:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c0bd4c3-5c58-3070-a606-89e5a0e5498a | -15.45666 | -53.93829 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b3e4821-2e09-3c61-b0f7-2e8c0e7a92f5 | -15.44293 | -53.93671 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 702321c7-7bb6-3250-b66a-f330cb03fd72 | -15.43051 | -53.92215 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe7d977d-c550-39b9-a9c0-7c4aaa668f65 | -15.44423 | -53.92383 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5c32e015-8c18-3f93-8b10-4dc9fb968d63 | -15.43115 | -53.91571 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a68c7f31-5532-3f33-a95c-fe9ba3061ef2 | -16.29928 | -52.92495 | 2025-08-11 05:46:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 11988767-9614-384d-a8b4-d79328e8fc02 | -15.44367 | -53.93643 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 22c002e4-5a14-3cc3-8501-80255bd415a2 | -15.43737 | -53.92297 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6fef8127-7a0e-3050-92c8-d017b1c103b4 | -15.45044 | -53.93111 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8226f335-d2fb-35a4-844f-e0bf4f4acfdc | -15.4574 | -53.93807 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2821534e-0377-35eb-9d38-b2db527df704 | -15.44979 | -53.93754 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 43545905-97b8-3249-8a1f-6ded6e95185d | -16.3066 | -52.92592 | 2025-08-11 05:46:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 303ee348-fbb1-36b5-ad0d-ad10aee4aa2a | -15.41806 | -53.90757 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9891a2d3-9c2d-3a21-93ea-0a0b0cd1a49f | -15.41742 | -53.91401 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a528aad-5fc9-3c7f-a750-72c5bffe009e | -16.30716 | -52.91961 | 2025-08-11 05:46:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9555d47e-9101-357f-a3ba-ab0e03104054 | -15.41055 | -53.91317 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c7224f0-b3f5-34e9-9d71-0dbd4e3d6bfa | -15.43673 | -53.92939 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9a0b284e-0eba-35e8-820b-94356ca16915 | -9.32133 | -68.32142 | 2025-08-11 05:46:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3be187f7-0533-3678-9eed-45a6be585765 | -15.43742 | -53.92907 | 2025-08-11 05:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a6f70548-f7c3-36e7-9676-6912f9f01a2b | -15.4407 | -53.9258 | 2025-08-11 05:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 2f29240b-42a3-3817-83c8-bee02aaf76ac | -7.4752 | -43.9536 | 2025-08-11 05:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 611ec18f-4d72-38ef-842d-2dc47aae9b76 | -7.0799 | -59.1964 | 2025-08-11 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 524baf13-e17f-38f0-b31b-ffc7dcb31905 | -6.5856 | -44.564 | 2025-08-11 05:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| db2d8e1c-4683-3ba2-b759-2a1e511f3bb7 | -18.6085 | -46.8673 | 2025-08-11 05:50:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0a0a4d53-3c85-3242-9e67-96a06cbbee3f | -7.0614 | -59.1972 | 2025-08-11 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6ddf3e76-a3ab-32ef-b176-e809d05cda1f | -18.6091 | -46.8438 | 2025-08-11 05:50:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 6ec30f9a-6e66-35e4-9863-da853c807ff8 | -7.0799 | -59.1964 | 2025-08-11 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 3c2ab668-5e0f-31b1-a8e2-c65e8fc3aac9 | -6.5856 | -44.564 | 2025-08-11 06:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| cbbb64ef-5796-3748-ae56-22d9ed4d292a | -8.9401 | -60.7288 | 2025-08-11 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 1d85a7af-737e-30d8-9158-4d1c853c3f19 | -7.4752 | -43.9536 | 2025-08-11 06:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 5e0caf11-9d75-3136-8e21-d8c0ea6a575a | -8.9399 | -60.7481 | 2025-08-11 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b73a71f0-09b1-3295-a7bf-e3bfef440390 | -18.6287 | -46.8629 | 2025-08-11 06:00:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 5c30d08e-b6bd-34fd-bd35-e97c1620b0bf | -15.4407 | -53.9258 | 2025-08-11 06:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| f488953c-0269-3c8a-b334-7a7a4994b6a3 | -18.6293 | -46.8394 | 2025-08-11 06:00:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| d4dd6cb8-891a-3747-89c9-22394c307285 | -7.072 | -59.21039 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a5f15032-8888-3dc4-a092-9272e256d638 | -7.06557 | -59.18022 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90489c57-4831-378e-a8e2-ef1e9b281267 | -7.05578 | -59.20316 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1743fe02-b448-321d-8dec-9d51df28b15f | -7.05805 | -59.18563 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ca4c658-8880-3198-bdfe-b5e5e7dba6d3 | -7.06099 | -59.21559 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4e55da3a-a1b0-336a-adcd-5c98cc781130 | -7.06684 | -59.19824 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| de8fbac7-cec2-318f-9105-819cfa473760 | -7.05935 | -59.20316 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e88f7737-99a8-3732-8877-2e5d9a3ff513 | -7.07438 | -59.193 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77597021-6c51-3a83-8cad-6a2f3e070403 | -7.07896 | -59.18216 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a9badb0-bd71-3d5e-9911-43278c06e86e | -7.05727 | -59.19167 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 362c1593-6ccf-38d9-a5ab-ba2f25927d58 | -6.10109 | -59.92716 | 2025-08-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 386ee26d-168b-3532-8c2f-5dfd7c6e7477 | -7.06475 | -59.18654 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dede62b-cb0f-3d31-83a7-bc5455afdb72 | -7.06246 | -59.20421 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bcbc6a4e-9473-3347-ae6c-b14cb343fb61 | -7.07743 | -59.19393 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56523955-35c1-3e90-b9f2-4d2bd1e04f33 | -7.06765 | -59.19234 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03e9bf07-abe4-35c4-b9f3-111fec6d57ff | -7.25492 | -60.00145 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40afd5d9-8192-315e-8b0e-3c9c071364ba | -7.07519 | -59.18708 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55c2d0f7-b995-3060-9346-e64b2fdb7ea6 | -7.08415 | -59.19466 | 2025-08-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README28.md)
