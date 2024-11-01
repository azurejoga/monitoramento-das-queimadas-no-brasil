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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01265779-1182-3fdd-9de8-2dfaca44572d | -7.8996 | -72.33406 | 2024-11-01 05:25:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 775ee614-27ae-3185-8d97-6947a2c4abad | -8.28702 | -72.66443 | 2024-11-01 05:25:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2177fffa-df3f-3daf-a82f-741018c23ce1 | -3.0539 | -49.4683 | 2024-11-01 05:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2ef34b60-46ee-3755-b515-030e6c273072 | -3.0538 | -49.4895 | 2024-11-01 05:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 462e4e16-5717-32b8-a1cc-27227ac95966 | -3.0354 | -49.4688 | 2024-11-01 05:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 926c2bd3-c241-3bcb-bdb0-bf8133b56d16 | -3.0353 | -49.4901 | 2024-11-01 05:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a01c9b12-d5da-3c4d-a011-991e2b41c74d | -3.5631 | -47.3847 | 2024-11-01 05:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| be0c2333-3b17-3f62-99ba-8485b76d3fbd | -4.4054 | -43.4746 | 2024-11-01 05:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c28934a0-fca9-3416-a6e9-a77f31bfc0c8 | -18.08584 | -57.37372 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 501521e0-9807-372c-b2bd-5d403f153583 | -17.28123 | -57.50881 | 2024-11-01 05:27:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4e7cd3d4-c04c-3728-bd38-d15867c0f74b | -17.27857 | -57.49671 | 2024-11-01 05:27:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4516339e-de25-3731-a871-1b4da2a1e7ee | -17.27809 | -57.50055 | 2024-11-01 05:27:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 04c16283-9505-3500-aff4-8a6758592a38 | -17.27761 | -57.50438 | 2024-11-01 05:27:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e0b7c54d-0d0a-35ee-9032-f147fe1936c4 | -17.27712 | -57.50822 | 2024-11-01 05:27:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2ede7994-da40-3a32-8341-4452b42d2cdf | -19.63356 | -56.64057 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cf723e33-3894-3da9-bfc6-cb8d9045b263 | -19.63302 | -56.64529 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 78ed17e6-01db-3054-bcf5-001aac46ce82 | -19.63264 | -56.68831 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6a727e78-9584-391d-b7b0-ebf5492a8c40 | -19.62224 | -56.73916 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fcc0d12f-187d-32f2-b1d8-b2faf252adf5 | -19.61831 | -56.7339 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0937da0d-86c0-3806-bbe4-2701ae03dee3 | -19.61778 | -56.73856 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 331910a4-150d-3832-b5a4-95e7c964c7d0 | -19.61384 | -56.7333 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 116e8033-1b8f-38a0-b98e-15d8e4a6d799 | -19.47339 | -56.60553 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 00e5290e-2d08-338b-b19f-9a37188ccf4c | -19.46889 | -56.60492 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 347d7cec-f070-34c9-80ed-4bcbbef4f9f3 | -19.46834 | -56.60963 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f35f028b-1c73-3976-a2fa-f5ea65040467 | -19.48461 | -56.66437 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 219f2804-58fd-3ea4-b550-f727df8ec5d5 | -19.48013 | -56.66378 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c96c0da2-c9f5-3ce8-b7ea-904cb9fc241d | -23.99038 | -54.09006 | 2024-11-01 05:27:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2875d1b1-f9dc-3b6d-a0f8-b0d97412a37e | -23.98479 | -54.08944 | 2024-11-01 05:27:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7f36c94f-289b-34cc-9eb1-e595056ad5e3 | -23.9792 | -54.08881 | 2024-11-01 05:27:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 97d01074-2e2e-383d-93bc-26afd28a0b1e | -18.02301 | -54.68833 | 2024-11-01 05:27:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e223ab34-d544-301d-9293-6c359d33d95d | -17.83937 | -54.31578 | 2024-11-01 05:27:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1ab7463-0ea6-34c6-a457-e42a6099978c | -17.59652 | -53.74232 | 2024-11-01 05:27:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4670a50b-8a9f-371f-8115-1d9d6e765651 | -19.61331 | -56.73795 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b21b5439-7978-3e69-b2cb-5b86d7665486 | -19.60864 | -56.69935 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5d1311f2-a960-3b94-950b-fc340d90b63b | -19.6081 | -56.70403 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d7f6057c-5c03-3459-b275-292597e34838 | -19.60757 | -56.70872 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 334aa14a-493d-3d9d-a805-abcde013f52d | -17.59615 | -53.7459 | 2024-11-01 05:27:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7e224c3d-cb20-329b-92bc-3c24df158970 | -19.60704 | -56.7134 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 16569d53-10d6-3a56-aefe-ff2b52bf168e | -19.60625 | -56.62016 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3474b045-4609-3566-a18b-6d416cf7352a | -19.6056 | -56.70133 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c73e367d-e199-33b0-945b-7de10a80d1af | -19.60447 | -56.71067 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 76801f39-9406-3cc6-8f7b-e7363b0b4b5b | -19.60416 | -56.69874 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e60ffc50-0263-34c9-bb2c-87b2ff3dd6c6 | -19.59944 | -56.71473 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 856c0d32-8633-34a3-a332-7e4155bb89ab | -19.59863 | -56.7075 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e8d4eb0a-f7f6-3453-966a-cec0dd59d84f | -19.59809 | -56.71217 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 49a01234-6312-389f-9b4c-b3b9e7801cea | -19.59756 | -56.71685 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d8b836cd-f656-3428-97c9-385748be9682 | -19.59553 | -56.70946 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c2e17da2-b743-3f1c-b9e0-e5e181797ed0 | -19.59496 | -56.71412 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1ed0d0dd-2755-394c-94cb-a5324ef54ed0 | -19.5944 | -56.71879 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 86d72c33-b02e-3b64-b9c4-3a2d03704095 | -19.59415 | -56.70688 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1e4485fc-ea80-3ddd-9669-00d5c850709f | -19.59362 | -56.71156 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4b9f5482-acd2-3c74-8e26-468a454a15c3 | -19.59309 | -56.71624 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 525021c1-29be-3862-b4ba-fbf9c1c12b31 | -19.59276 | -56.61835 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d861d444-7ec9-34cf-adc6-2af71a29b103 | -19.59257 | -56.72091 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a09e9e6f-4370-3965-8d92-8d10857ec89b | -19.5922 | -56.62308 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2f4e63c6-ec55-3485-925a-e5af6d6c9c12 | -19.5905 | -56.71353 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cd75d50d-8514-316a-9e08-399efa4d2e75 | -19.58994 | -56.71819 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3a3ef3f1-688d-359c-b2c0-01d864190c7d | -19.58862 | -56.71563 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 91e5f25c-d466-3ec8-8ed1-89b51ef1a07b | -19.58826 | -56.61774 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a2c1b684-750b-3961-851d-d0080471888e | -19.5881 | -56.72029 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8f36d83c-a1d9-3e40-981e-e7bdcf16a72a | -19.5877 | -56.62247 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d65e45ac-8670-38af-ab47-8e66dc109104 | -19.58714 | -56.6272 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ab6f7888-1725-385e-a80c-798014aca89f | -19.58377 | -56.61713 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e0e9a092-9c25-3c4b-8831-29c9893c1ab6 | -19.55027 | -56.70809 | 2024-11-01 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 11143e1d-b83e-3379-9de3-23b52a462b1d | -19.54918 | -56.71741 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 5978c9af-075f-34ed-ad25-327d0c688b3e | -19.54526 | -56.71214 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ed3fb4df-ea84-3578-8e77-1bf0c9f35dbc | -19.54471 | -56.71681 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 2ef4b856-dad0-3c27-95ba-08bf795806ea | -19.54416 | -56.72146 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 5a8ac7e3-6a17-349e-82c6-f94d3fed7e89 | -19.54362 | -56.72612 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 214b1f0d-7f07-35df-b718-bf4b88d7446d | -19.54308 | -56.73077 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c48ad34e-b453-3662-b54c-3180d2208d2c | -19.54133 | -56.70686 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| beb03503-0ac6-3e97-8c88-f353730766d7 | -19.54024 | -56.71619 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c2819afa-35bd-3004-8ce5-7ac4b01839ff | -19.5397 | -56.72085 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| fb7a562f-a49b-3103-85be-85d5fade610d | -19.53916 | -56.72551 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 49edcf2f-5653-3627-a0eb-70e20f73ef81 | -19.53578 | -56.71558 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d9b30585-c73c-333c-babc-ec4291183929 | -19.53524 | -56.72025 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 04a78007-08fe-36a7-a641-1d9a63a379a7 | -19.53469 | -56.7249 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1132676e-c5e3-3c29-81b3-d45e28de105b | -19.53415 | -56.72955 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 2a34a3d6-8228-35fa-a3fa-80557252eed2 | -19.5324 | -56.70564 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cd2b14bd-3d2b-3549-b6cc-6d03f9eac988 | -19.53185 | -56.71031 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 77096d69-98b1-3b0b-af5e-10af6138f7d6 | -19.53131 | -56.71497 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 37a555f3-8d83-3d39-b8c5-f33779b6eb54 | -19.53077 | -56.71963 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 496115de-de37-3d83-9e01-0cd424c65640 | -19.52454 | -56.69509 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ccc7e136-b48c-3bff-9f5c-2c0660de4021 | -19.524 | -56.69976 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a9b86fff-8429-370e-a647-7272212c4915 | -19.49937 | -56.5961 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ee62d527-f66d-3b37-a08e-df960156fadb | -19.49724 | -56.61504 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f019c98c-46d7-33c2-98ce-95dd1e729299 | -19.49586 | -56.60859 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4e9523b7-87de-3185-b2b5-4fd62d0a4df8 | -19.49529 | -56.61331 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| db7a8321-91e2-368e-ab05-06446edcc3ca | -19.49473 | -56.61802 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d5b6818a-8d8b-310c-a0da-cadf82e8aa00 | -19.49381 | -56.60497 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 301bd9ea-bb42-33ba-b67b-e374226b1ba5 | -19.49328 | -56.6097 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a78653ad-d805-38a8-86fd-6545940382da | -19.49222 | -56.61915 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d4656dbb-1839-3b94-8b7b-db8291dd36df | -19.49136 | -56.60798 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ed42b540-e7c3-3a55-be37-ee3e74b7791a | -19.48967 | -56.62212 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e29259d4-1066-3831-96b2-76685a85bebe | -19.48965 | -56.66029 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2e3b74bd-b588-3a57-83d6-9506d5ab6407 | -19.48745 | -56.66152 | 2024-11-01 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a4233681-b371-3591-a001-8894e76a6d94 | -29.4782 | -51.96467 | 2024-11-01 05:29:00 | NOAA-21 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ed2f82ab-345b-3c19-8811-684a16709962 | -3.0353 | -49.4901 | 2024-11-01 05:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 34d4ef77-164f-34db-83a6-d959b8650f93 | -3.0354 | -49.4688 | 2024-11-01 05:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0c11e050-283b-3582-88be-a84d7c438068 | -3.0538 | -49.4895 | 2024-11-01 05:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |


[Clique aqui para ver as próximas entradas](README51.md)
