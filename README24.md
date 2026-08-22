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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39205e1f-1dd2-37a6-b4b1-e8ff4a55fa49 | -10.27496 | -50.38081 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c15643b1-5e7c-38be-8ce3-83894e93022c | -9.3138 | -47.63144 | 2026-08-22 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39fc35ea-d14d-3ef6-8eae-d6d31197cf8d | -10.38694 | -50.42846 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2ee599c-d161-303e-8e2d-885b88221a9f | -6.82173 | -59.66224 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0340748e-987f-3d9f-8588-8cdfdb14b2de | -6.88351 | -59.44366 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 90870b49-a97e-340c-9422-4e822c9dc89c | -12.83847 | -48.46507 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee4a6648-2b77-3d51-b18c-4a9ec265360d | -6.76881 | -58.68855 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f2d4e2d6-f2d0-3448-bf41-743c778be890 | -10.89609 | -50.27319 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70f1b55f-a398-3d1e-9d3e-4aa250d6b208 | -13.95608 | -47.82093 | 2026-08-22 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0d89f73-26ae-3c52-8356-540979b02dd8 | -11.82123 | -56.59423 | 2026-08-22 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e47aadbf-e140-34f2-8cc4-c38ba000da64 | -12.73953 | -48.46665 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a10b3fdd-756d-35e8-9dff-2f3200604633 | -7.74116 | -46.16168 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00267d49-df03-3363-83c4-6080bda57cff | -8.09367 | -51.66078 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6d99ef8-5036-3902-9587-b0ac240f4574 | -8.03394 | -54.0037 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dab4b6c6-e01e-3839-b68c-60c086239e6c | -6.81408 | -59.40643 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ea57c6b1-d997-3699-b667-31aad49dd82e | -8.63341 | -54.74145 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb71ec6a-aa4e-377e-9d51-53bfb6a1bfc8 | -10.81291 | -50.98115 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7ae94001-fb18-370e-b82b-da437223d98f | -7.35132 | -55.67484 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47e4e37f-4257-3c17-9e8f-0e20a2414389 | -6.76784 | -58.6535 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c247e98b-b3f4-3157-8b64-2cc7d56bc054 | -6.79946 | -59.41023 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| f7acc36d-4b78-3a11-ae2c-563df4a5697c | -6.88295 | -56.63728 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6f9452e-fe17-324e-aa4e-0634e0e1ce6d | -9.16811 | -57.01162 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8442184b-a8cb-3802-aa4a-4161c3bb638c | -6.79944 | -59.59388 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d0f770d-f3c2-3f00-9a05-e8582ffe2066 | -6.89952 | -58.99878 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c5a04e7e-ab10-39c3-9bc3-25f04e563719 | -6.8175 | -59.38845 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b5e9f79c-e4a4-30f9-a071-ea575acb7513 | -10.79378 | -50.98242 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 93fc5673-1731-3f95-bd6a-291e6f038353 | -15.44547 | -41.38377 | 2026-08-22 04:27:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8ef279fc-51e7-3b1d-9313-a6b644a453fe | -6.87788 | -59.43653 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 769f402e-79d4-3629-9744-909f1ee82935 | -6.87008 | -59.44113 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d20ec867-f405-3ae8-8505-a058fbefad42 | -9.17566 | -59.43857 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9cc08b38-797d-323e-af92-5cd0c2f4db35 | -11.58529 | -46.57694 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1abb515-2f5c-3b8a-a290-09afa151db60 | -10.51699 | -50.77294 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e00d03b-e513-370a-af8d-8f9574b646c2 | -6.90182 | -55.71227 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d53c583b-8c05-3b0b-9529-519e00fdba3c | -6.8965 | -55.71126 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d86a24ca-27ca-3fcb-ac97-53e6c270575e | -6.60467 | -56.36662 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10d0a0e0-c4db-3608-9560-478b5e6c6a08 | -14.13966 | -48.06177 | 2026-08-22 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68d6eec2-095f-3bf7-9b85-527223ad951c | -8.53828 | -54.82548 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ae1b08f8-dc0e-3634-98c1-0ffe4c63b486 | -13.4463 | -43.8398 | 2026-08-22 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6425414e-95e1-346d-9fae-554c828e518f | -8.54217 | -54.83185 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf29e630-9b4d-3b58-b856-a731e5018ae3 | -10.94668 | -51.41803 | 2026-08-22 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 179dea88-7f9b-3cf8-bd0b-40cf49451d1a | -6.43725 | -52.75756 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ac57870-21df-3b38-a5e0-e72d789ddfc2 | -11.95426 | -55.5177 | 2026-08-22 04:27:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ed66ea3-7a66-3d6a-8280-3071885aad9e | -7.26351 | -49.88019 | 2026-08-22 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fddbb629-6b40-3d93-b2e2-37fe590cf4fb | -11.38522 | -46.35102 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b62235d9-b5a5-30d9-b6a0-19e18c7ee13c | -6.00373 | -57.80402 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 733f3d1f-2f6f-33bb-97d8-570d6dee0ecb | -12.78809 | -48.46069 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6672a8c8-cbb5-38a7-a5f1-63a6835f04fe | -6.76407 | -58.67456 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f14f640d-eb58-3836-be13-ace7c2aec3b2 | -6.12957 | -59.8999 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9b0746e-5fe2-3246-8d83-df8319a5bd80 | -6.66426 | -56.34693 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4aa60d8b-57c0-3b7c-8ba5-bda9cae86846 | -8.53044 | -54.841 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e6242814-0997-3f46-af7b-c0c7544024a4 | -6.86336 | -59.43987 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9c1aa3c-8f35-3ccb-a0a1-4ccdccae23bc | -9.17783 | -59.46089 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1370bf42-6450-3c57-a8d2-04ebeaba35c3 | -6.80169 | -59.43499 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d40233a3-f238-3118-8cbb-9e1930ee5207 | -6.85886 | -59.46393 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| faec6cdc-a33a-3e84-a088-ecd55d7cbf2c | -8.58687 | -54.72202 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 045daa8f-06a0-3237-8082-3b75a0dd802e | -6.53843 | -58.52461 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a451a53c-a249-3509-98a4-246f9563b30f | -14.29091 | -44.96082 | 2026-08-22 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 816911f1-91e1-3284-acd0-053bb3b9201f | -8.08907 | -51.66369 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e14bd8f4-3e97-3c1d-8466-5c8e62d522ab | -11.45182 | -44.53818 | 2026-08-22 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57c6abcf-299c-3918-94c8-d74303657aa6 | -6.11441 | -53.07159 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b1a453c-7dfa-3522-89c7-dd284a25bfd2 | -10.12212 | -48.81338 | 2026-08-22 04:27:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80e9adcf-d1fb-3ee3-ac6a-d2dad62e0f54 | -8.52173 | -55.32109 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83631a9b-7411-3cbc-9e95-f16262db6296 | -11.34855 | -46.03433 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6bd849c-d098-34ce-809a-eb4e82fa0b7b | -8.53143 | -54.8355 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f08d2327-016b-3984-b91b-529de43de3d6 | -8.53241 | -54.83008 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3b08d21f-978e-38ce-b2a5-de1d08b2c888 | -9.18448 | -59.46291 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 27f485e0-7a2b-36f2-b87e-7cdf871e9a01 | -6.13778 | -59.8945 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69f699ef-5228-36dd-b6bc-b4759d2e2ccf | -6.00454 | -57.79949 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5a7355e-3ec7-38ef-a786-e6e19db7497b | -12.55292 | -54.76801 | 2026-08-22 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73651c8e-9217-3e7c-9c45-584ae2375136 | -10.29941 | -50.38921 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bad70848-b5ba-3803-b8dd-27d45736c32f | -6.41965 | -52.72821 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e1e3d41-ab05-3d60-9913-679659731539 | -8.59182 | -54.75051 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d7f6f7c-12dc-3abd-a416-3cb7f463d1ab | -7.25878 | -49.90937 | 2026-08-22 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7f62480c-4076-379b-beb5-13becfeb7478 | -6.86585 | -59.02656 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 94c4aa0a-413b-3267-be3d-4a85957ea948 | -6.79826 | -59.60011 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4bf57472-be43-392e-a95a-e62fdd0375bd | -11.13244 | -49.04205 | 2026-08-22 04:27:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f8a4945-d980-3318-8ec4-27d5aeb8b806 | -11.94807 | -45.49403 | 2026-08-22 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63bda2ca-55fa-3a12-83d4-5566ff25a237 | -8.52657 | -54.80667 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 80382347-5728-3ef8-b42b-07e4a9feef09 | -9.19298 | -59.45226 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 307df8c8-b19d-3504-84ad-dac1ec8eeba8 | -12.83182 | -48.4641 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa3fbc9a-5ce1-3c7d-8409-00ac4d38cb85 | -10.68743 | -50.30692 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c02b884-6983-3323-a38f-df6a3eb114f5 | -7.47567 | -45.15037 | 2026-08-22 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8f57bd33-8481-32d5-a715-36efd87615f2 | -11.16428 | -54.01583 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23f2dd02-c66d-3e1f-bbe8-9c01a6c7e836 | -6.43736 | -54.94954 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ff3c0af-d482-3062-bcf6-ed06806c0474 | -10.8912 | -50.28074 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 072b9282-dc94-3135-b021-44f9c4fc9aba | -10.96326 | -51.41138 | 2026-08-22 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15a5be07-a10c-37ff-9117-b8523d555d6e | -6.43813 | -54.95789 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71c152b2-4b98-340b-84cf-3145d863d881 | -13.3856 | -54.36934 | 2026-08-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce03dbeb-c314-30ba-8c53-3ad8949bf930 | -10.68232 | -50.29342 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc9941db-32ac-3225-be59-fc3c91c5c422 | -10.51278 | -50.82148 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff6025a8-067d-3bd2-818e-5f89e29a1f70 | -6.8002 | -58.98666 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97b970b9-62f5-3313-b175-7b665d4dfdee | -8.53456 | -55.3305 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 515b8359-6b21-39cc-bf3b-f66a41c1df18 | -6.97389 | -59.05891 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 730cb6c1-f470-3141-bb6d-68dee8b0ae76 | -8.11014 | -51.66019 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 225a4d50-8705-3efd-959c-b6c074207dae | -8.15449 | -46.71819 | 2026-08-22 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10149d8d-0a62-32b6-a2c1-1bd642f2e73d | -6.86002 | -59.42059 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4f5ed78-b213-3330-ac43-3176b21b510e | -6.12708 | -59.91327 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 591e9964-4477-3b76-9a92-5d80f31d796e | -8.52629 | -55.32479 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa263c4d-ccae-39dc-938a-86c40de0f8b9 | -7.63214 | -50.03637 | 2026-08-22 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da52b1f8-1ca7-328a-aad6-ad9b509c5197 | -8.52655 | -54.83464 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |


[Clique aqui para ver as próximas entradas](README25.md)
