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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7384da9d-3a55-3303-bd95-27b085fa19f9 | -2.35495 | -46.57456 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec37b1fa-877c-3233-9a68-55986cf4a887 | -1.23256 | -51.75223 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b1c7e3c-1e33-3b4e-b6fb-f6ace3a504a8 | -1.8403 | -52.40504 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b7d8233-0a1a-37c3-baa1-1da1788ed5a2 | -4.58446 | -47.07216 | 2024-11-11 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15b0842e-b97a-3ef1-a7a9-bc2585c3f6db | -3.56546 | -52.29824 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 321cfa2e-e5fe-3aaf-831c-25f06aeb7317 | -1.29383 | -48.01178 | 2024-11-11 04:18:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45bbc051-d4cc-3ff4-8888-bc48f48b8296 | -2.39137 | -49.85302 | 2024-11-11 04:18:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ee25c72-5ae7-3216-a2b9-546c6a9e50f7 | -4.75798 | -44.37207 | 2024-11-11 04:18:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf2b5e47-9c9c-37d4-ab94-bc260071f5dd | -3.78715 | -47.46095 | 2024-11-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 301a1f0a-46a5-36fb-9f55-1b6cf74a4c3a | -2.3074 | -46.4689 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 290d4ef2-0eee-3c28-94bc-f73982a46c4a | -2.38464 | -50.32872 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26952eb3-f14c-38f1-8667-1cc56f76998d | -2.34618 | -46.56072 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ea1358b-4a18-36be-8eb2-866551318089 | -2.97879 | -45.82924 | 2024-11-11 04:18:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad462401-5f50-3ad9-90f3-2794a4e566b9 | -1.11465 | -48.37874 | 2024-11-11 04:18:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d625040c-d5ef-36c1-9a61-bfcdd5697713 | -3.09048 | -49.59092 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b98ebf3-8172-37b2-b4a9-438cdb488f6b | -2.72602 | -46.69679 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e69689de-83e7-39b9-b28c-7d251509a67e | -2.88032 | -45.36868 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5a6fbc25-749e-3209-9f99-ebb4d69b48f8 | -3.74056 | -45.91506 | 2024-11-11 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e320201-855a-303b-b86e-e7a84ecd4e89 | -2.54338 | -46.30023 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f1ed9c-30bc-37aa-88eb-6165e7edc122 | -2.55695 | -45.53598 | 2024-11-11 04:18:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1376d9c0-7cbc-3589-a0b2-6f6a324d7077 | -1.60601 | -54.4081 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d2853ec-9342-3e3e-8745-4b84fcf0ac31 | -3.23807 | -46.53759 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5be7c0f-497b-3e3c-83c7-b16047d5e46b | -3.20506 | -46.49625 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffcd0e65-5260-3c37-aabb-ba31ab6c0386 | -2.53381 | -46.31486 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 606120ac-0363-3786-8b67-6d0bb45dbcfd | -3.44982 | -51.5772 | 2024-11-11 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95b27cbf-5e9b-346c-80e1-ae751567b48f | -2.41533 | -46.51779 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b31644ca-f63f-37e8-84cb-b7b234a80708 | -2.39978 | -48.93164 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b9b9e7a-733a-3e9e-a3cb-12e41007df4f | -4.71009 | -46.38008 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3755963-2a45-385a-89c4-98f89727025e | -2.5996 | -46.17298 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 837a88d8-e080-3290-a938-40dbdf0f6dbf | -1.56387 | -53.4183 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df756025-45d5-3043-aa58-00b13525fd13 | -2.25411 | -53.73559 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 715a391e-0f97-3216-b919-4899e11d7230 | -4.69805 | -46.4331 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e049542-a30c-3211-a60e-9c4ff9f8c5f4 | -2.62967 | -46.16891 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 389f7794-2025-38a1-8a83-45a2fab15ca2 | -3.82881 | -46.52179 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4846f348-b75c-3354-a8db-2abf8bd74842 | -2.34033 | -46.55152 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8fd2c0e-aed2-37a2-8d0f-7119f9e810ad | -0.90646 | -51.6521 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43633520-79fa-34a5-b7e1-c38a9a9fc3e9 | -2.87751 | -45.36451 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfb41ac3-7d47-3be7-a93c-f1b6394323c3 | -4.68763 | -46.4314 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb9f68b3-d9b6-3bb2-aabb-18afb65b7096 | -3.05941 | -53.88494 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20ae25e3-b700-3a8b-95e3-6a74111773c2 | -3.02944 | -50.97523 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 12480f2c-418f-3471-aaa6-2a7f399f1d7d | -3.24182 | -45.37999 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f682ab8e-fcad-3446-a59a-5132c098595d | -2.4083 | -46.7721 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 530a272c-63b5-3161-9049-9312b9f318d5 | -2.25327 | -46.50989 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82a2e047-6452-3442-ab7c-05c06db3b3aa | -2.97735 | -46.99501 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d74a1743-9693-3967-a35d-82b95e58d5d0 | -2.69936 | -46.81843 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9adebd0b-24a2-3f5f-abb2-5ccdb1d23d55 | -2.30898 | -48.9024 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dda53d4-96e8-317b-b2cf-7dc80ff73b42 | -2.35722 | -46.58323 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59b5157c-3c3b-38f9-8a29-e1b87b8ef059 | -2.84353 | -48.67961 | 2024-11-11 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 4b90101d-5fed-3b08-96c9-bc0c78f275c3 | -3.11573 | -45.97279 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b700b6e-436a-3d3a-a941-5896f710125c | -1.5542 | -51.85124 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19f2c1fb-394f-34ba-8249-f36482a20689 | -3.28033 | -53.66905 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 630f3506-8db6-36b8-9e1b-d6ded9a372fd | -3.6872 | -45.23945 | 2024-11-11 04:18:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a7f6a87-7a68-3413-b8aa-1fa241799a82 | -2.6524 | -46.81119 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90e7235a-1b9e-317b-89b4-652e1b978657 | -3.01948 | -53.24365 | 2024-11-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1de5512-126b-3c22-aab2-322e6499a780 | -2.6989 | -49.3431 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 768cfa50-ac20-34d5-b58b-46e56fbf6b72 | -5.37431 | -42.76842 | 2024-11-11 04:18:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 652c06ed-2ad3-379f-aebc-1fdbac073a55 | -4.7054 | -46.38721 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b33ecf92-c64c-39e7-87d2-a77698083ddf | -2.92095 | -49.49317 | 2024-11-11 04:18:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 174e481b-24d1-3ce0-b084-18d34993665a | -1.34341 | -54.62772 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 848346d6-df97-30a5-bf38-812cd1ba0e7e | -3.57462 | -52.30584 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f495db2f-bd0a-3c09-b3e7-fc38a8444e7b | -2.40765 | -46.77624 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0a892dc-125a-31de-aeaf-5fe6bc52bc53 | -2.25331 | -48.31672 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9112bfa1-6472-3a55-a0b5-30278bd05988 | -4.61195 | -45.98868 | 2024-11-11 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| dfe9d266-0b85-3604-b6dc-3f3fe66c8ad9 | -3.12611 | -45.97444 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f9adf65-641f-3084-b876-8d4e710f212d | -3.12732 | -45.9669 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d2afb3c-d973-3a45-91da-bc729c202858 | -2.3426 | -46.56016 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bfaa90b-eb8c-3f12-9f61-629cc3584ed9 | -2.87974 | -45.3723 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f761351a-350a-37a9-b16b-c043d8a63823 | -3.2086 | -46.49681 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abb7fc25-ab41-39cc-8f68-68969879f943 | -3.38332 | -46.37444 | 2024-11-11 04:18:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5535b981-e924-3e8a-9266-3fe62a6fde9b | -2.54177 | -47.32302 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efa031ef-cdfb-3fff-af29-5fd15959c7b4 | -3.96135 | -46.70615 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0be03035-d818-338d-9244-1dac8330fa54 | -3.83518 | -52.31355 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4a8acb5-fb8f-35c2-95f9-64b2df2ecaaa | -2.93151 | -46.71847 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e51538c4-1d8f-3eff-a287-bdcd2f9d38df | -3.58985 | -44.55071 | 2024-11-11 04:18:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 166fb975-2059-3fbf-b92e-9a4215c3da13 | -2.24905 | -46.51337 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7469aaac-6fca-36f9-8dbb-4e4577fc8ab8 | -2.36755 | -48.51842 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aca4b7b2-b694-3d19-bd2e-d4dc3226a053 | -1.5196 | -54.99875 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3050178c-78dc-34d9-9e64-bab92da29a06 | -2.30427 | -48.90538 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93826ecb-8ccf-3d9f-bb48-92bb03863985 | -4.90483 | -45.86187 | 2024-11-11 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33144f86-3d3b-3116-89e3-ac0fce685833 | -2.77049 | -49.38244 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4058fa11-6bbd-35c4-88fe-184b38e33e40 | -2.24678 | -46.50471 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0c0e6bd-10fa-3562-af89-de77cd10a6d0 | -2.98165 | -46.99142 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90261d10-0502-3ec5-ba4f-9aa6b62eb12e | -4.12675 | -43.58989 | 2024-11-11 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a4b5607-a583-3d76-b013-a74a6ad04414 | -3.32482 | -52.54255 | 2024-11-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 950dcd2c-9994-394a-8aa0-f8f7e96c8884 | -1.92871 | -46.35963 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8324ebec-8e2b-3587-a41c-0958ebad311a | -1.56955 | -53.41904 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f979ded-99ad-35d6-8b83-548f47b45dde | -2.54327 | -47.32189 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f388808-120e-37bd-9f87-7d88c013a3d7 | -2.2484 | -46.51739 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a58612af-1d14-30cd-9dee-8d8a5acead97 | -4.90317 | -44.65731 | 2024-11-11 04:18:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76cd7d7a-3a92-3d7e-acfe-f260c0bd8897 | -2.69764 | -46.66726 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f2c76c3-af0f-373e-95ca-cb914905cd32 | -4.69049 | -46.43582 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca2ac7ff-a6d8-3f56-8e9e-1ca4248d4695 | -2.28539 | -46.86508 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db00a7f4-1c0d-3b23-88ea-8c281d413d70 | -2.54628 | -46.3047 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d86d8d1-192c-3b04-8dca-5be29b6e513b | -2.40044 | -50.31736 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51584f6b-50f0-35d5-89c7-58e9a737de5f | -2.54087 | -46.31594 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 74b47dff-e596-33b7-9b5f-8555aca3318d | -2.59776 | -48.1894 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8e14d84-5853-3fea-9e22-fcd0c9cbc4ed | -2.22384 | -46.40705 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8f0191f-0874-33b0-8973-34c281538abd | -2.95645 | -48.01993 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b647c40f-199b-3e35-9d37-e29514fcd90a | -1.6307 | -52.53652 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfe28164-2891-3b24-9550-521b2a1fd690 | -2.92192 | -45.63361 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README34.md)
