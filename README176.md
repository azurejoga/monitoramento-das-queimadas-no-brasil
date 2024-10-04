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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c8c47a1-2078-3139-89b1-9b36dfe50a58 | -17.19146 | -57.35724 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6c03ec36-b6bf-37a9-844a-e23fbce661a9 | -17.19088 | -57.36089 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| dfd550ff-e0b4-3b9d-b076-f36fced53812 | -17.1903 | -57.36452 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 851e16fc-44ef-3c26-948f-fafc0c9b0357 | -17.18913 | -57.37178 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8e5b283b-d843-3529-8902-bd5da8ad3f15 | -17.18872 | -57.35303 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3478c186-7ea8-3578-b6ff-a36ef38309fb | -18.68518 | -57.30058 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f08ce786-5b8c-302b-993e-43fa111faeb4 | -17.18814 | -57.35666 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 962e6e30-0067-3e82-abd1-e1fb9eada981 | -17.18756 | -57.36031 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1c2a83b6-4836-3e96-8114-7269cd55c9ed | -17.1858 | -57.37121 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 0d109ab5-28d3-3210-b391-88803770cbbb | -17.18481 | -57.35608 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 71f9f253-d8af-3dfa-9467-237cff235ec2 | -17.18464 | -57.37849 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 37b9b7d3-8828-3cd3-b45b-1f5f00f3ee2c | -17.18423 | -57.35972 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 990dda14-d97c-3750-944d-5b4fd185e687 | -17.18248 | -57.37064 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3cdaab25-c7a8-3604-8b60-dfb4d91e1ae0 | -17.18149 | -57.3555 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bc6ff717-a38c-3bfc-afe0-456a4ad2b58c | -17.18091 | -57.35914 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4ed3cedc-527c-3603-9405-4d39428fa20d | -17.18032 | -57.36279 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3e054310-f798-34b0-a80b-df294460f008 | -17.17974 | -57.36642 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1d37f0da-18b6-321a-a394-afa38adba025 | -17.17134 | -57.37616 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 32d111b9-755b-3a2e-8d41-19bdc1d41d47 | -17.16859 | -57.37195 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fa319f9c-24a5-349c-9919-24e5b258109f | -17.16801 | -57.37558 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 981bae94-b1d6-3dbf-8c6b-b7dac4778c7a | -17.16585 | -57.36773 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 048978b8-c71a-31ab-a5e8-fdc4a64b5647 | -17.16527 | -57.37137 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c80b9fc2-5be1-3b12-8362-08ec9436e1ed | -17.16468 | -57.375 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b68f21d1-049c-36bd-b441-d8227320f8b8 | -17.1641 | -57.37864 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9da04365-90b7-3587-8850-160180ed5d4b | -17.16351 | -57.38228 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2632b03f-248a-3ffc-8f52-4605f7ce5e84 | -17.16253 | -57.36715 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 8bcddadb-5ee4-34da-bc89-48187018fd94 | -17.16194 | -57.37079 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 264c1966-521b-381b-8460-31d67d1fb041 | -17.16136 | -57.37442 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 76cf700a-f086-359b-b3e1-cc0d8714ab6a | -17.16077 | -57.37806 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0bc97127-a45d-31fd-8c81-3501ed677d4c | -17.16019 | -57.38169 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7ed3961f-b015-383d-9e29-f7c7883d1513 | -17.15979 | -57.36294 | 2024-10-04 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7f88ffd7-aa1d-360f-923b-cac679b95e11 | -17.1596 | -57.38534 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2353814c-039b-326d-844b-a9f8926bcc51 | -17.1592 | -57.36657 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 1ad06f3a-8cbf-3e6f-840a-16e448fd1e09 | -17.15862 | -57.37021 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 429d2286-9a68-31fa-abdb-2be5b48116ca | -17.15803 | -57.37384 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8b7133cd-d97a-3de6-b0fb-5ff624707dcb | -17.15745 | -57.37748 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 65c2c4b2-160b-310f-922c-1697888fb5a3 | -17.15686 | -57.38111 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b89af1c5-fced-3aa8-b3b1-4721b8a2577a | -17.15587 | -57.36599 | 2024-10-04 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 25b9e832-b621-3921-b854-720d03d0f6ff | -17.15529 | -57.36963 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fac0a665-cc68-3028-a23d-11b4e07add37 | -17.15196 | -57.36905 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 19859959-d427-373b-8983-14ab1898bb98 | -17.15079 | -57.37633 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 1026369e-c561-3dfc-9ef7-b6d6863b049a | -17.18896 | -57.3942 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b3cebc72-c6f5-31fb-80a8-badf1ef047e4 | -17.1823 | -57.39304 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f66152d2-1f4c-3804-9857-6cc752494f12 | -17.17507 | -57.39552 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7193bac2-c5f1-3bf3-baf4-9ade96e77cda | -17.17448 | -57.39916 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e5858d4d-27db-30af-a814-c94fdb4f0f2c | -17.17174 | -57.39494 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 48b7a004-a458-32f4-8c35-3092bcd241c9 | -17.17116 | -57.39858 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 40ea51e2-c36a-3855-b33e-e78c2b4ce01a | -17.17057 | -57.40222 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 21004b6b-1509-3e43-8097-a579fdd3f422 | -17.16841 | -57.39436 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 75c221ec-ecea-3c94-b0df-93528363e2a4 | -17.16724 | -57.40164 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| c33e50fe-e04d-329f-8a79-5858c684db5f | -17.16666 | -57.40528 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| debec40a-46a9-3310-87fe-aa524099e0fe | -17.1645 | -57.39742 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 7406b11c-dac0-3753-9ca8-25de66971e5f | -17.16392 | -57.40106 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| de7b687a-2fee-3fc7-bf8a-604ef47a7f2a | -17.16333 | -57.4047 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b5974218-8960-3236-99fc-a93ca3a84142 | -17.16117 | -57.39684 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| e54ff427-860f-37d2-b726-b2c80b93726c | -17.16059 | -57.40048 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 04b1d5e3-d9d3-38e4-b3cb-a3959492371c | -17.16 | -57.40412 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 625e2d0b-e36c-3d9a-8793-40a87cef0fb3 | -17.15843 | -57.39262 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0a352f06-1c56-3d7b-9bdf-f728a8c0b991 | -17.15785 | -57.39626 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| c62bf43d-753f-323e-81a2-f4e2fc7e555e | -17.15726 | -57.3999 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 50406c7a-5dd8-3e4c-a8a9-661f40e9d28e | -17.15668 | -57.40354 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f1db8303-e2a5-3d2a-9b05-8bda8330cb0c | -17.15511 | -57.39204 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 17e91c41-dac4-37f6-85a5-022a28aaedaf | -17.15452 | -57.39568 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ad542aab-487a-3004-8e7c-241f6aed667e | -17.15393 | -57.39932 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| eb27c26c-b2a3-319c-af87-ed6f7a28b532 | -17.15335 | -57.40296 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0d82e92b-396d-364f-8107-dc32fba0227e | -17.15178 | -57.39146 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b8608d3a-19f8-3e05-b933-bca714cf2d63 | -17.15119 | -57.3951 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| d82573ed-0e64-334c-9dac-d20b463e543c | -17.15061 | -57.39874 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 9b1193d7-0806-364e-a9b5-e5673e22af6b | -17.15002 | -57.40238 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b537b114-7f6c-3bf1-8c4e-cc05645e68c4 | -17.14845 | -57.39088 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f4840b89-23ec-3a06-84bd-1b60dbf6beeb | -17.14787 | -57.39452 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c5146bea-2e2a-3918-856e-fa5af4fe0b12 | -17.14728 | -57.39816 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 6dfbf6f4-9ff0-35ae-b29c-a0e3850f7258 | -17.14669 | -57.4018 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2ff1a6a9-3c8b-38cb-a54b-f3d8b05ef00c | -17.14611 | -57.40544 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2eea1797-f7c6-305c-b633-cf9f5b642721 | -17.14513 | -57.3903 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 03916a4d-ed2d-3a0a-ba91-2077a268f975 | -17.14454 | -57.39394 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e0acab49-21f8-3f61-a283-b53cb484329b | -17.14395 | -57.39758 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2fc2b6bf-73e2-38ef-a976-0b5f58b336c7 | -17.14337 | -57.40122 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| a1fcf074-0626-3c13-9ded-de618d4c6bed | -17.14278 | -57.40486 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| a3664855-4fea-38fe-8aa2-0b7c5b0a37e7 | -17.14121 | -57.39336 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 171a1d77-aa07-3d7c-9ffc-035b4622d852 | -17.14063 | -57.397 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2a5fe9e9-4edf-3bea-8bcc-b954730ffa41 | -17.14004 | -57.40063 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| fa88abe9-71f5-30ed-8e2b-1d267f824818 | -17.13945 | -57.40428 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 912124e7-9325-3a47-9986-45ec183b42a9 | -17.13847 | -57.38913 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bd8b9b6d-c33f-33cc-a33b-68e99a497902 | -17.13789 | -57.39278 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3b0bc9d8-dbdd-30fb-8062-e407d32ea8e8 | -17.1373 | -57.39642 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ce32bdb7-f67c-3523-ba22-da3be45e1ca5 | -17.13671 | -57.40005 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2741c349-1df5-3ddf-95b9-fc7f2574b90b | -17.13613 | -57.4037 | 2024-10-04 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6d7da171-90a7-3a87-a8c4-11e0d8ec9986 | -19.10432 | -57.48497 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 65fed7e2-c6c0-3378-a387-f9bf913d0b36 | -18.89106 | -57.71069 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 00a56e2e-db00-38bd-bb3d-d7a6937e6f7a | -18.71658 | -57.31729 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 124d766d-10b0-3a4a-9143-a2da90a36aff | -18.7219 | -57.34816 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a1d4fcdc-662d-342e-a1f1-fce5646339a7 | -18.71859 | -57.34758 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a795d74e-c562-3c55-8dd2-bc74e67ad3dc | -18.69238 | -57.2981 | 2024-10-04 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e4e9dc9a-1992-3aa4-b45a-aa8f22bd13fd | -28.58689 | -49.44269 | 2024-10-04 05:01:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1f63216a-adde-3387-9917-96bf00abd966 | -23.87048 | -55.42098 | 2024-10-04 05:01:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a625f66f-01d1-3ce2-9f3b-7a0020505ef7 | -23.93654 | -55.25322 | 2024-10-04 05:01:00 | NOAA-20 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| da34bef3-4298-3497-b1fc-f97833ad9814 | -19.51 | -42.93 | 2024-10-04 05:03:31 | MSG-03 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 909fb294-97a0-39b6-8c4d-d3bda8354a1e | -19.51 | -42.89 | 2024-10-04 05:03:31 | MSG-03 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa759d16-cbed-3107-a0bb-4163c9651a9e | -13.07 | -51.12 | 2024-10-04 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README177.md)
