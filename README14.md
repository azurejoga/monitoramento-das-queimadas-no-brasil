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
| 38ca4c31-b81f-37fd-96d0-927025d6679f | -1.5237 | -47.290699 | 2024-11-23 00:45:00 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28640382-9029-3b85-a15f-fcc99ce87ffc | -1.4656 | -51.1166 | 2024-11-23 00:45:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 076bcc79-1ec2-3092-a171-487b79f7e08d | -4.7186 | -45.488602 | 2024-11-23 00:45:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb9987b0-9029-34c3-8673-8947e5d15fa3 | -2.7642 | -54.071201 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0f4617d-9441-3ae9-8b67-80a460324df7 | -4.1104 | -43.226398 | 2024-11-23 00:45:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbca301a-1317-37ac-8e6f-d3521129c900 | -2.5335 | -54.0079 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea472153-fa06-3e89-9a85-fc5fcf0ac074 | -3.835 | -52.245998 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2afce3ad-a1a8-3df1-ab5d-71a2f24ac5b8 | -1.6364 | -52.684502 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adf6eddd-a06e-3ac7-9a9f-68d057e4ea91 | -0.9247 | -51.636002 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc2fcb61-ad71-37db-85bf-0b6ce65826d3 | -2.1852 | -45.689098 | 2024-11-23 00:45:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f796e6f-53f6-3d69-9177-9d6e9f0c4159 | 0.4823 | -51.011101 | 2024-11-23 00:45:00 | METOP-B | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f5de7649-bb82-34c3-a453-30ece521e988 | -2.8252 | -54.0219 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b686f34d-697f-3a43-93e0-5264024577c8 | -3.2415 | -54.222801 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bdfa2a5-fd6d-3e02-a158-5afb24118efd | -3.0593 | -53.279099 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae19b46-99e1-32aa-b805-ddb127d8314a | -1.6379 | -52.1007 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e836963-64ae-3344-bb45-553c877e6ca1 | -3.1046 | -53.9814 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52c4cda7-46bf-3c62-ade9-90c265d9267d | -2.6031 | -54.042599 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b40a71-25e7-3877-895e-131ae892a4a7 | -4.635 | -49.536499 | 2024-11-23 00:45:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1ba5971-9f8a-38ca-937e-aaf911597ec9 | -2.5933 | -54.0448 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19bf20c5-8c2b-3dfd-8514-fab4bbd614c9 | -3.2332 | -54.2318 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db511d8d-0f01-3c21-8e0b-73cead39fdd8 | -3.0772 | -54.545799 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c650ea3e-67c2-3e84-8c05-296081e77154 | -1.7765 | -53.622501 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff47ab48-674e-38cb-a92a-d3af3a14faa6 | -2.7807 | -54.053299 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a831fe9-736b-3b7c-8f29-cdd5ec7f78e3 | -3.7585 | -49.933102 | 2024-11-23 00:45:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f5f32af-d770-3265-aaf0-5be71e41832a | -1.629 | -52.424999 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a568af0-2631-315a-ac56-b8786774be62 | -3.5065 | -53.799099 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65183feb-0a55-3097-af4b-00919bf6f026 | -3.8482 | -52.349098 | 2024-11-23 00:45:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b392c781-7e47-36a0-9f23-adb6e64c2d11 | -2.8024 | -54.0126 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c207f937-8fc4-3c22-a21e-3cad7d706109 | -2.8318 | -45.1777 | 2024-11-23 00:45:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e67df4b0-88a7-3e8a-b19c-bdd6dbbd863a | -3.0664 | -53.219501 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c94b2a-0225-3b7d-b1d7-01db5321ba43 | -3.2535 | -53.272202 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6df2f7-d5b1-3575-8242-b76b142da4f9 | -3.084 | -53.2519 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac0dfacc-fa45-3090-9b1e-2fa336b7e077 | -4.1124 | -42.482498 | 2024-11-23 00:45:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99ec84c6-2e1f-3fa2-87c8-0317fe5397b7 | -2.6993 | -46.091702 | 2024-11-23 00:45:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82c250de-15c3-3bfe-b132-9390b48262a1 | -2.5798 | -54.076401 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 656f3ea7-2d29-3c6f-8b70-fc99e6cd5b52 | -2.7694 | -54.048599 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 709a95b6-2467-3a3d-919c-9edb79090eed | -3.8422 | -43.931 | 2024-11-23 00:45:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcfcf598-4136-3a7d-b162-d8e06a2994a9 | -1.8937 | -53.32 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1be8e7-7eaf-3e9c-afd6-de8d396b5460 | -1.9446 | -49.5201 | 2024-11-23 00:45:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb58bd8d-fbb3-3bfa-9100-90646bbb88dc | -3.2218 | -54.2272 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28317bac-4445-3a92-9269-09f0e723c6ec | -2.7421 | -54.018902 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4348819a-615d-33a3-9777-a7d77e7a1a15 | -4.5221 | -42.906399 | 2024-11-23 00:45:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5234aec-4781-3e20-8124-9b0271dc029b | -1.2488 | -51.748199 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3c494f7-4118-3e77-bd0e-056bdc097383 | -3.9391 | -47.964001 | 2024-11-23 00:45:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 596a7040-70f4-325b-8986-b1af48f32ce6 | -1.6068 | -52.599499 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 668995cd-349d-307f-9d2e-75c49dbf5ed4 | -3.1904 | -51.362499 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13fea8a2-d7d1-3f22-914c-b0bd5ef597fd | -3.2876 | -53.833302 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c5a1e5b-1177-3304-aab9-d75952f50692 | -2.3113 | -45.442101 | 2024-11-23 00:45:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41f6e54c-2cc3-3afa-b523-56e190672118 | -2.7865 | -53.987598 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4da566cc-7de5-366f-aa47-4e7607b1d48d | -3.8089 | -52.357899 | 2024-11-23 00:45:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 634ea01f-6836-3f96-ad99-4b935bfec8df | -0.9839 | -51.715401 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9915e1b3-3806-37e3-a952-dce43239d0e4 | -3.1077 | -53.994999 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd7730a0-70be-3a3e-8889-0932dc3fb02c | -3.468 | -48.236401 | 2024-11-23 00:45:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88e2525f-ef7b-3f2d-b601-c4c19b2782a2 | -4.6887 | -45.834702 | 2024-11-23 00:45:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6898cfe-1af9-39b3-9972-d1c5f566f034 | -1.1486 | -53.397598 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5950e76-f10e-38b8-98ca-e154723a544b | -3.2461 | -54.243301 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08d28bd4-eeab-3831-ace9-7a44adf102f2 | -3.6298 | -54.437801 | 2024-11-23 00:45:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40774335-c190-3909-b9c4-abb966b65102 | -2.8619 | -53.956501 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec2d4901-a8c2-3b48-822a-c2dc1d5bb7e4 | -1.3076 | -51.7351 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8565c8de-cc5f-3213-8bc3-83f66a70b234 | -1.7718 | -53.601799 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2e854f9-5e64-3c32-b065-c7747a9d5811 | -4.1647 | -54.571602 | 2024-11-23 00:45:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0fd49c4-534b-35bf-87d0-d87065614584 | -3.0302 | -45.151699 | 2024-11-23 00:45:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f781a19e-c994-3eaf-aee5-ffefbcb92ab2 | -2.8485 | -53.988098 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d842fa-597d-34f3-8d75-070380e0057f | -3.252 | -53.265301 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b768363-4531-3166-9c4f-9878df375fb4 | -3.8984 | -47.922199 | 2024-11-23 00:45:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a02615f-0752-38d5-850e-9a2f6a8ae58f | -3.2716 | -53.808201 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 383fbc3b-2501-359d-b7e0-c25d15c9d5f4 | -2.1955 | -53.652199 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e063479-e07d-3cb8-a148-1a89ba8caa58 | -3.2158 | -53.834999 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69358e0a-f5b9-377a-b662-159ec2a4fe23 | -3.8178 | -51.989101 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f8b6c4d-7745-3275-a760-b04992bba45a | -3.2675 | -50.439899 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d929457f-3bc3-3890-9ed3-fb2e78df927d | -4.681 | -44.3974 | 2024-11-23 00:45:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa9e5c3f-1010-33b4-8f0d-2e4ada96f357 | -1.2096 | -51.938099 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 855f26c8-a1e8-3b4a-a3ce-17d806df9eb9 | -2.4481 | -53.6754 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 667fddc8-7cd2-3644-88b1-747d49a0c0c4 | -1.6273 | -52.417599 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 522da838-3ea7-3773-9e86-162823c9d587 | -1.19 | -51.942501 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e050ca5-a394-3b8e-a4f8-8ce765fa6f31 | -1.2158 | -51.738899 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5ec6b90-0561-3f14-8508-850bf406316e | -3.1092 | -54.001801 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91be2def-95af-3c81-9d64-bb700e9e5658 | -4.7456 | -49.081902 | 2024-11-23 00:45:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcec5775-9dec-373e-afe4-1e6b879dab64 | -1.8442 | -53.694199 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dff0183c-5a47-3c10-a2be-1185f98da070 | -2.6198 | -54.253399 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2e93788-0897-3a91-8abe-d1b61c14ac16 | -1.0683 | -53.179298 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d2d1ff2-04a0-31a9-ad0b-d8c64c189336 | -3.9013 | -47.934399 | 2024-11-23 00:45:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e093f31-2102-350e-ba8f-e555753357cd | -1.7378 | -52.722698 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91fd196c-7135-304a-b8d0-7a3790799039 | -2.616 | -54.054001 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5278cedf-7898-3b56-a275-595552e58877 | -4.1632 | -54.564701 | 2024-11-23 00:45:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f46d0e8-2936-3514-96f1-a58cc126112e | -3.3394 | -53.332699 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3255988f-f578-318e-a6bd-939015dab8b5 | -0.8441 | -52.5532 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec14ae6a-2136-388d-891a-4bb35a1fb016 | -4.1013 | -51.064999 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1a8f6c5-4f3e-3e54-a6a2-c0fca0861c03 | -1.3741 | -51.9827 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3045ad17-8323-3717-b468-a3dd53b58f94 | -1.6228 | -53.306999 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0591570-7ba9-3e29-98db-cbabd1feb53d | -2.9581 | -54.795101 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28adf5e8-3b73-3316-8c18-c53c691d4ca4 | -3.0998 | -53.731701 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fde4fa68-3497-3b5f-93d0-621dad670c90 | -1.3954 | -55.176498 | 2024-11-23 00:45:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fce5db76-8cc3-34d1-a6ce-0c30e5414444 | -2.8268 | -54.028702 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3864a4d4-92f3-3ebe-a56d-68803b019d19 | -1.1408 | -51.680401 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dca476a9-89b2-3e0c-bdd4-7c83795d1396 | -2.5614 | -53.994598 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8745124-a600-3faa-aa90-6ced51599473 | -3.7332 | -46.043598 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5782c67a-013f-3da8-8415-eb19d39f4c94 | -1.2243 | -53.687099 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe4ec063-6fbe-3cb3-a0d9-4c67f0e410c7 | -2.194 | -53.645302 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd719ccd-2385-3a7d-b77b-64d42ee1b839 | -4.7502 | -49.101799 | 2024-11-23 00:45:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
