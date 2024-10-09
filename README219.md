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

## Dados Diários - Página 219

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 842cecec-97fd-3616-aa96-aa4eafe9fb91 | -12.9998 | -62.74231 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 43675763-ae5a-3e96-9492-61d280fa84d5 | -12.99516 | -62.74167 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b3a7cd6-3761-32a7-b99b-8668ad1f611d | -12.99453 | -62.74659 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a38874a4-788d-37ef-bbe0-65c46e9a5f20 | -12.9924 | -62.72621 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56a26787-a6f8-32b6-a090-59916a2441b2 | -12.97289 | -62.69318 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b620627-d055-354c-b474-3ee8cf76567d | -12.97017 | -62.69033 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08dac159-abbf-3b66-b4a9-2c535461f2de | -12.96885 | -62.68758 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3febf530-5ff2-3fb0-8bd9-61462231c9d3 | -12.92185 | -62.73395 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99863a05-bf45-34f9-a5e5-12a3a70a5037 | -12.91722 | -62.73329 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7437d3bf-c4f6-36d3-bf29-bd637229a759 | -12.91385 | -62.72279 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b0babcbc-7a58-3a0b-8e0a-5b2d347235ab | -12.90921 | -62.72212 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dd40d62-fc78-3357-809a-6401a37deea8 | -12.90858 | -62.72704 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ac4766a-646b-30d8-86de-f6f488dd4619 | -12.88711 | -62.78407 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 026693b6-78de-3935-9638-bac2f5546c82 | -12.88186 | -62.78828 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a897dd8b-e13f-3b87-b32e-a5485a6d12af | -12.88124 | -62.79317 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a746b544-0f88-35f9-a7b7-c771f9a9cab3 | -12.88061 | -62.79805 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3cef0132-2fcd-3f94-9426-405a8b661d47 | -12.87725 | -62.78762 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d03f75bf-cdf1-3863-85a8-7097697fe80d | -12.87662 | -62.7925 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e08c5cde-55b8-30e9-bc55-294c49e6e024 | -12.876 | -62.79739 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a3d3cf9a-5297-3873-bee1-7fe52b256518 | -12.87538 | -62.80228 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bd0e064b-9155-3a9d-96e9-e72cab660313 | -12.87475 | -62.80715 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33d9d830-216f-3e6f-87e9-9031a6166ff1 | -12.87076 | -62.80162 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7acf1945-cbb3-3bc9-8e64-d1488877b841 | -12.87014 | -62.80649 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b46730e-82b7-3737-882d-11cd150512ec | -12.86553 | -62.80585 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 051fd22d-1528-3d64-8f2c-39e4bed0632f | -12.86215 | -62.79543 | 2024-10-09 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 600d5433-7c8a-30fe-8a50-a4154c7cab11 | -12.86092 | -62.8052 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cc46df9-e7f3-3af9-84c7-cc72747ae16e | -12.8563 | -62.80452 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e425f98-7fe6-39f7-84bc-26f325780081 | -12.84706 | -62.80698 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0322c145-5a7f-3233-96cb-1947911a23b4 | -12.84647 | -62.80807 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1b5f58a1-a1b2-31a9-8426-25289c09df10 | -12.84245 | -62.80634 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f532684a-0d99-387f-8bc7-c3f592ca07fc | -12.84186 | -62.80742 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c311c3fb-db8f-3ec2-998d-d4c57285afb6 | -12.45065 | -63.01192 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71546c4e-7107-3e95-aaad-060606063646 | -12.43465 | -63.0286 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bec0472-1058-3cdd-8589-ed07c8211985 | -12.42171 | -63.02203 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b4d9687-fd13-3b71-9953-3d32a9587c43 | -12.42111 | -63.02671 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccb273f0-f970-32e4-a5af-01ea6e973d11 | -12.4172 | -63.0214 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18c66c70-3948-38be-baa6-6cdc66d5a6c9 | -12.41659 | -63.02608 | 2024-10-09 05:57:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b7d73f5-a78a-39ea-8230-9872a2120208 | -3.57977 | -54.33816 | 2024-10-09 06:10:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 57611967-5336-3383-b2ad-582911e795cf | -3.27096 | -54.18136 | 2024-10-09 06:10:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 53ea9d02-dc91-3535-a30f-7dc83771f098 | -3.26654 | -54.18771 | 2024-10-09 06:10:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| aefaa491-424d-3aa0-9155-57fd1698fcab | -3.13834 | -53.73219 | 2024-10-09 06:10:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c3e8df43-b92b-3615-9286-028cd6184d5f | -3.02385 | -59.10442 | 2024-10-09 06:10:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b33f48c2-9ccb-3d61-90eb-564183b65223 | -2.99084 | -53.72006 | 2024-10-09 06:10:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 77bba651-29af-3658-ae18-81f17c3e682f | -2.88788 | -53.95737 | 2024-10-09 06:10:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 491e4082-9947-38cc-9871-682351b90ad5 | -2.61415 | -49.78474 | 2024-10-09 06:10:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| b7fcfbd4-b72f-3194-8bbd-827f36eccbda | -2.61078 | -49.79189 | 2024-10-09 06:10:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| b347281c-8b8e-3a6f-8167-f94da413c50a | -2.2426 | -53.65161 | 2024-10-09 06:10:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 030d9522-4097-3164-bc83-18ae311ee9e2 | -1.13112 | -53.61255 | 2024-10-09 06:10:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 6d36299b-b317-3078-ad70-c4f9c10a5e9e | -1.12908 | -53.62616 | 2024-10-09 06:10:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4bac3a98-532f-3b81-ba33-cb34516c346b | -1.12024 | -53.61111 | 2024-10-09 06:10:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| fb64f2ef-727a-3f09-ab1e-1b91706a9cfe | -1.11814 | -53.62523 | 2024-10-09 06:10:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 93b170dc-4361-36ce-baa0-0a7635be478d | -9.95948 | -60.13126 | 2024-10-09 06:12:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e87d43a5-cd22-3b9a-8faa-72600b2c2054 | -9.95813 | -60.1402 | 2024-10-09 06:12:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ee8265d-188c-3880-b649-68a62f49f543 | -9.94057 | -58.1322 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6bd3f92c-7b63-3068-b0c3-dbac81927f66 | -9.93449 | -59.93587 | 2024-10-09 06:12:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e67b016-205a-3a63-953a-2e75972db9ab | -9.93138 | -58.13086 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 48c05de4-9b7b-337d-b566-b5b1ca6878ce | -9.90174 | -60.21399 | 2024-10-09 06:12:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f8e94a47-cf0d-3714-951c-e3ba1bb04dc6 | -9.88247 | -60.10143 | 2024-10-09 06:12:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 983f8e3b-5da2-372a-b8fa-3686bdbe6129 | -9.82091 | -60.43467 | 2024-10-09 06:12:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 44af1515-af44-3d76-b159-b26cbd7620dc | -9.74626 | -56.98199 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4beb0ae0-c575-3a74-a691-4936a285e813 | -9.7436 | -64.22967 | 2024-10-09 06:12:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f3db2ae1-a41f-3961-9267-0694e7bd23a8 | -9.48966 | -57.93676 | 2024-10-09 06:12:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f4ebb321-93e1-317c-b302-133b60e6ad43 | -9.37302 | -63.80603 | 2024-10-09 06:12:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 18acd1a3-0e83-388e-8378-185e85722cfb | -9.34204 | -60.31229 | 2024-10-09 06:12:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f54dc43-62d4-3d95-9e1a-eb5e4eb6522e | -9.1942 | -62.28189 | 2024-10-09 06:12:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bdb6e246-1327-3852-8e86-2b0e50402144 | -9.17779 | -61.57186 | 2024-10-09 06:12:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 970426a3-35ba-3313-a0f0-aa60615d8c26 | -9.16855 | -61.57041 | 2024-10-09 06:12:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 12fd6888-d4f5-3308-84d5-a67a7dd23ea2 | -9.10539 | -61.13311 | 2024-10-09 06:12:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3488b685-fc96-311e-8eac-db51aff79333 | -9.07782 | -61.37218 | 2024-10-09 06:12:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b6367882-85b3-3e7d-a527-2106af95a880 | -9.06368 | -63.22968 | 2024-10-09 06:12:00 | AQUA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 99f46c80-7a76-36c1-9ff4-17ad65432fb4 | -9.06175 | -63.24178 | 2024-10-09 06:12:00 | AQUA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c71e73ff-3e90-3a95-a762-2ffcb25efb1e | -9.06108 | -60.4544 | 2024-10-09 06:12:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 304090d9-b117-3dbe-8882-ab8866a3bc78 | -8.31047 | -55.1001 | 2024-10-09 06:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 72fb2bc0-a0e1-3ef0-9b34-556cc6634b25 | -8.30859 | -55.11399 | 2024-10-09 06:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 45573c61-6aa0-3129-a744-59b33b1a758b | -7.36756 | -64.66826 | 2024-10-09 06:12:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 7d94dec3-4b2c-3768-8310-9498870709c2 | -7.31342 | -59.73801 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01bef2e6-b767-3317-a023-f40d5ca4e52a | -7.30456 | -59.73671 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b20daf40-25bc-31e4-a533-e89fff499c66 | -7.25572 | -59.63208 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8ffe1344-679a-3b43-b363-acb24755fe0b | -7.2064 | -59.77928 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 88b36eed-dc27-3e01-beb9-2fcba50eb966 | -7.19753 | -59.77795 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fa3a9f34-7149-3ae8-9fcc-83596258b03d | -7.17771 | -59.35194 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 142528cb-08b2-3e9a-8cdb-e3fd94a327e2 | -7.17638 | -59.36079 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e54e3b69-7629-3a12-ab36-9f17ed866e6e | -7.04029 | -59.41552 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 85ff6257-35dc-3b17-a191-43b4b6ba9759 | -7.03896 | -59.42437 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e3ffbba4-75ec-31fa-8fdb-fc861f14782d | -7.03144 | -59.41422 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ae5fd69-9327-340e-9003-68d331939db9 | -6.80807 | -59.354 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93f9c3e3-4c7d-3667-9807-e71d8d2bef91 | -6.78847 | -60.04045 | 2024-10-09 06:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b9910765-1965-3a7f-93dc-dc8a31152dd7 | -6.7871 | -60.04949 | 2024-10-09 06:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 38656243-7e88-3e35-b192-dec3b4f59505 | -6.78573 | -60.05853 | 2024-10-09 06:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 9ac41c85-2784-38a8-ade3-78ad274dbf5b | -6.77818 | -60.04812 | 2024-10-09 06:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| e2a60bf9-f998-356f-ad00-3136b91eeaac | -6.7768 | -60.05718 | 2024-10-09 06:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 87d65652-d7af-35b6-b487-a7ec9bff774b | -6.69052 | -59.46561 | 2024-10-09 06:12:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df5b6184-da86-35c9-8e11-e403047e3041 | -6.67029 | -59.78077 | 2024-10-09 06:12:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 81d31496-f7c0-32ab-8fbb-26d96247d0f0 | -6.54176 | -58.41983 | 2024-10-09 06:12:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 308262c1-cc04-31f8-a87e-6f45d1e38589 | -5.45372 | -49.56078 | 2024-10-09 06:12:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 5fe7aff6-b7d6-3114-818a-850dd2e1d14f | -5.10803 | -60.22076 | 2024-10-09 06:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c221555f-9bf4-3ccf-8944-93e2b2917b93 | -5.09896 | -60.21941 | 2024-10-09 06:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9cbb79d4-ea5c-3d86-b0ce-24582d8ce46c | -4.73087 | -60.812 | 2024-10-09 06:12:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5eeec2d0-3baa-3fcd-bb5c-067dad1588b7 | -4.30711 | -60.01779 | 2024-10-09 06:12:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 29daeb60-75b2-35e4-9e6d-c758a99fc508 | -4.29805 | -60.01645 | 2024-10-09 06:12:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README220.md)
