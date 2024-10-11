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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8754f062-fd37-3448-ba08-ebd9d089a212 | -5.49894 | -60.45852 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58727a50-b926-3b57-9919-ecd35692b065 | -5.41545 | -60.61076 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f66a5769-368d-3f07-a6ce-a3152ff6464a | -5.20317 | -60.70721 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5752eff3-e5f3-39a3-b3a0-c68e329f6701 | -5.19974 | -60.70667 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20aec418-d661-376c-a7f2-bb23d768fa7e | -7.79528 | -62.39243 | 2024-10-11 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4f789e3-37ef-394a-937a-21c852608640 | -7.97303 | -61.50681 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f7f1b46-589b-3331-aed8-ae8170b5905d | -7.94587 | -61.26288 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adf3c78c-4dd8-3e0f-9f15-542a2489f64f | -7.94245 | -61.26234 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b944a49-644c-3770-8b2b-21e8a18c2be0 | -7.94185 | -61.26607 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cea0b56-e023-3be7-ba80-ac677aaafe98 | -7.93662 | -61.27672 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25165551-941f-3680-bbb5-2f3f83ac7040 | -7.9338 | -61.27245 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9fe5ef1-d26e-3695-af12-849c502d6c38 | -7.9332 | -61.27618 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdc98343-ff78-34f4-a9ce-a3a24e28a2d4 | -7.9326 | -61.27991 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 969e50a3-ac2d-3ec7-aa62-8d20dea8af04 | -7.9316 | -61.26443 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 855682b2-8e08-3332-a12d-87d2d62be588 | -7.93099 | -61.26817 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 959520bb-d0e8-3a67-9cd5-cc94abbdcb88 | -7.93039 | -61.2719 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 978e650e-218f-38f4-8cf0-9b331045e24b | -7.92818 | -61.26389 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81c01d2b-ddbf-3ccc-8bd5-0bd91d098d48 | -7.92757 | -61.26762 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13eea38e-a30e-3d99-9927-c8ed67bfe821 | -7.92476 | -61.26335 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d381712d-e89f-3e08-a553-8848b029a35f | -7.91677 | -61.66253 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4912047f-5975-3e25-9a93-b16656288682 | -7.90038 | -61.52225 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0d0b98b-55bc-3d9a-a773-ec1192f3c837 | -7.89401 | -61.47439 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 461d524d-1af7-32b4-9752-3f154570bcbc | -7.89339 | -61.47818 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0a1ab7e-540b-3983-a52a-78a963ab1d96 | -7.83308 | -61.22204 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3633dc0e-bdb9-3e06-b634-c18c81cc15d5 | -7.83248 | -61.22575 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dea354eb-4c61-3c8b-9594-32a69d5fe150 | -7.82966 | -61.22149 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4033065-eb53-3c3c-b959-426505e9e389 | -7.82906 | -61.22521 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f465452a-2cfc-3069-887e-38ed6aeb4d83 | -7.82444 | -61.23213 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78519447-5015-3c86-9292-b0abacb8c169 | -7.82163 | -61.16305 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2c276a8-ea3d-3145-8664-8525ad945e11 | -7.82103 | -61.16676 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9cc520cc-e29f-3ee6-83d7-cb4febc1bebc | -7.81823 | -61.16251 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b1d23b4c-539c-3fea-91f2-3488b270e247 | -7.81762 | -61.16621 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 04a60a18-6020-34d1-bbf3-96679adcfc27 | -7.81422 | -61.16567 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fe05ebe-11a3-3e17-9942-aa8b06898a3f | -7.79284 | -61.57978 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beabb06d-7a79-3e15-8b16-4596c786c5a8 | -7.78099 | -61.34807 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b0b6ba6-6198-3d46-8e3e-93346ec9608b | -7.78038 | -61.35183 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8835e2b8-64f0-3462-b359-a18e51be63b7 | -7.77695 | -61.35128 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8f9dd15-e1d2-3e3e-8237-4b99aea36419 | -7.77633 | -61.35504 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37afebfe-6425-3dff-bbc4-5125b996be69 | -7.77352 | -61.35073 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 083c3bd8-e6e9-3265-bd05-74d9b8b06786 | -7.7729 | -61.3545 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b7ba0ac-4888-3260-a162-410e3d3d654a | -7.65023 | -61.20048 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| edd32391-989a-3cac-8275-c64eae80551d | -7.64963 | -61.2042 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7af61d1-b213-364d-8f58-7b4fd712b2ac | -7.64681 | -61.19992 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44cbd537-c56b-3d95-986a-b95c043ad9e0 | -7.64621 | -61.20364 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e844fb05-6de7-3dfe-a0c1-28742479c1d5 | -7.6422 | -61.20683 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd3660b0-97bb-3508-a7fb-451dea4a8cb4 | -7.63938 | -61.20255 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ded3e55e-dda6-34bd-8213-447de4303f90 | -7.63878 | -61.20628 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aba23bf1-c79d-37d5-83fd-4ef9a772788a | -7.51747 | -61.58317 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e3f8921-89bd-3e0c-a302-448ca606c13d | -7.91331 | -61.66196 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d4c7d5f5-3113-33b5-8043-6fffb50a1fc5 | -9.2228 | -62.45174 | 2024-10-11 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86a393c7-d3ff-36d7-96b0-9622f22621b6 | -9.17197 | -62.65361 | 2024-10-11 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06fcb7b5-3b98-34aa-bc97-6288d290fdcd | -9.1713 | -62.65775 | 2024-10-11 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ddc3c20-14c3-38b2-a372-392b673b5cfc | -9.17801 | -61.57592 | 2024-10-11 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90b04adb-068f-39eb-964a-ad19a19d7509 | -9.11834 | -61.27331 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ce6268f-3cec-3b83-be8b-fbd36e1f4bb6 | -9.11774 | -61.27699 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 487ccb4a-da7b-37d0-bb4a-b78245300248 | -8.23573 | -61.16857 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14b84a26-bbf6-37f2-b5b0-7bc0d4c4c670 | -8.22268 | -61.5074 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0fa4949-4b3e-3e13-9656-51c7ee8ba5f1 | -8.22206 | -61.51119 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11aa4b3f-7758-3545-a1a7-e2ebb16d26b7 | -8.16953 | -61.37956 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 983925f9-519b-3387-8e3b-cfade9e668e7 | -8.1661 | -61.379 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5930282-eb3f-3231-9e82-b3e53ca87ab9 | -8.10326 | -61.26913 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 665d3118-2176-3226-911b-90c045c4c195 | -8.10081 | -61.39151 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85b3675f-afe9-3e16-9474-543e8554bbcf | -8.09984 | -61.26861 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2f190b9-c4d2-319f-9bde-ba0c1542def4 | -8.09946 | -61.2688 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ab65f8d-92aa-3020-a501-e370587db9b8 | -8.09605 | -61.26829 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51b22687-cbb5-351a-90e0-b0ba95902086 | -8.09263 | -61.26774 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce112fa7-c7c7-3722-8aa7-8425bf5c7178 | -8.05932 | -61.30063 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6685051a-fd5f-39b5-af00-3b171ebf41c2 | -7.97647 | -61.50738 | 2024-10-11 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0ba968f-ac51-3e2d-9c7a-960d6f2524d3 | -9.59007 | -61.85152 | 2024-10-11 05:18:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cd04f0f-9f10-3477-b5a6-d2c47077aa21 | -9.38733 | -63.41408 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d93198e8-bfed-376b-8cd8-87fb96d17b6c | -9.38655 | -63.41862 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d62c1c5-4e1b-3e4b-896b-73f22f3f4707 | -9.38513 | -63.41492 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c77971bb-af62-3011-b0ff-47c927115053 | -9.38438 | -63.41946 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03aebf8b-4000-369d-a62f-a0d6fc485283 | -9.15334 | -63.3381 | 2024-10-11 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d6f70bb-6b94-3189-9a11-629895a2c8b3 | -9.15259 | -63.34258 | 2024-10-11 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 574d492d-f364-3911-b571-e5793832af4c | -8.81478 | -63.00108 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 501b1c41-98c5-352e-a0ec-6402067dc2bd | -8.77842 | -63.2617 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0119acb4-f124-3c9d-b10d-9b12faaa36f1 | -8.77766 | -63.26616 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76b4a213-9608-3ed4-bb10-9f9576d17a71 | -8.6902 | -63.09321 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7491c8f9-0158-34c2-a813-1919b873d198 | -8.67195 | -63.33746 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c718c5c-647a-3f63-b869-871288d243a7 | -8.66821 | -63.33683 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c251a9e-b24a-3cf7-ab33-caf587b5241e | -8.66448 | -63.33621 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9ff270c-2b46-330e-85be-88ceee018ca7 | -8.66075 | -63.33559 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 862b309b-c30e-3f97-ae81-506f70c32182 | -8.64926 | -63.25676 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fad4161-56d5-3b9e-aab3-c08c3efd1f42 | -8.64763 | -63.25473 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7aed2cd-cf40-3a04-817e-7179ad8196bb | -8.62769 | -63.24855 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c199da9-af74-3675-a3f1-8ee41444e7c3 | -8.62323 | -63.25241 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2df08e26-3170-342d-8364-ca87c45934f3 | -8.61952 | -63.25179 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae53d7da-93f3-31f2-a685-46e333bf6010 | -8.6158 | -63.25116 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d35be771-22f7-3a0d-b838-dd449f093f54 | -8.56999 | -63.4112 | 2024-10-11 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c60c4db3-d1dd-347b-b345-0000aaf40da8 | -8.55737 | -64.03915 | 2024-10-11 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b84cebb8-ed3f-3d8d-a006-8d705381df32 | -8.19341 | -64.02251 | 2024-10-11 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2117762b-15aa-3eb5-8cdd-251c1288dfd3 | -8.15236 | -63.93047 | 2024-10-11 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b43c6305-6f8c-35f7-b34a-5c6acb5f0cff | -9.84522 | -64.05847 | 2024-10-11 05:18:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e4e6752-6e8a-32da-aead-2bd494803bc4 | -9.82691 | -64.05041 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1cb5607-8d7b-3c24-a6b4-4283e60c3a1a | -9.82045 | -63.63359 | 2024-10-11 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64c7daac-155d-3213-8ceb-c5a92666b4dd | -9.5857 | -64.10552 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ee71970-bfcb-33dd-9fd9-c9cfa9ab05ac | -9.58384 | -64.10364 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d3a1979-29da-3ae8-b270-a041e6ee24d8 | -9.58185 | -64.10483 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf9ffff9-d983-36a3-94c1-9a6d92e960b9 | -9.57415 | -64.10343 | 2024-10-11 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README88.md)
