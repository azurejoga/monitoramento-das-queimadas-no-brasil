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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 999c7093-32ec-3014-bbc3-bda675824acc | -7.5583 | -49.4127 | 2024-09-28 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba7f2724-7796-3e0c-aa49-66ac1ecc015e | -7.55747 | -49.41757 | 2024-09-28 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8002a8dd-d0fa-3745-825c-9959ba0e43b8 | -6.65157 | -49.76626 | 2024-09-28 04:19:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b672f3c-2408-3a36-9d6c-7f53ecc54f19 | -6.65097 | -49.76979 | 2024-09-28 04:19:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d13749ca-65fd-38f0-b5c1-469c8c822a33 | -6.64695 | -49.76912 | 2024-09-28 04:19:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dafcb32b-8407-3fb7-854d-c0d11f4c9505 | -8.24076 | -49.38253 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d0c1b50-2db4-37c7-95ca-132f6213577a | -8.23992 | -49.38745 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c1f4a180-80d5-38f9-9964-f28ce441589f | -8.2361 | -49.38676 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| df730530-9eed-344c-b246-db7308bcd1e5 | -8.23228 | -49.38605 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f9150571-97ba-370c-979f-9eba0cc925eb | -8.1221 | -49.53426 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c0a99990-6ebf-38a5-b5ab-77c270448793 | -8.10965 | -49.53718 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05aab1b9-b716-353e-a1e2-17902dd3eef4 | -8.1044 | -49.52119 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 29923474-39ae-3fd8-b286-f3ba70f5a57a | -8.10357 | -49.52609 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f782c4fe-87eb-3137-83e4-b8f5d2f737a5 | -8.10053 | -49.52055 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 232c6cc4-7202-3b69-a580-1656e87cbdaa | -8.09969 | -49.52545 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 87f36e47-a388-37c8-b232-cac5fd1b2d71 | -8.0972 | -49.54004 | 2024-09-28 04:19:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75c7a7b9-e232-3a41-9e03-8814a64aad79 | -1.42549 | -48.89099 | 2024-09-28 04:19:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63e3cf43-22d6-3e31-ae2d-bc7a77af7036 | -3.34978 | -49.77779 | 2024-09-28 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71983d7c-eded-3557-a1ab-41a59766ff8a | -3.32837 | -50.30494 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4ad433e0-dd51-3432-b421-750968f0ff92 | -3.32766 | -50.30925 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4bf6286f-a6cb-3b20-b8cd-46563f8594d7 | -3.32325 | -50.30862 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f20c345-48ed-3c7b-a2a7-91daf710108c | -3.32254 | -50.31294 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95596de6-bf7f-325d-8a29-5168a83169fb | -3.31884 | -50.30798 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 020a3ceb-ef1c-383e-a0c3-151e53a4b359 | -3.23699 | -50.01176 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb3acc0f-da98-3c53-a3a6-8df74849abf3 | -3.22639 | -50.32082 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e14a15c-b048-30ba-9392-2c0b45357e13 | -3.19828 | -50.43697 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 36867889-0dea-3ee2-b7a0-903b062caef1 | -3.19753 | -50.44153 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| a29ba42c-82f3-3bc8-b207-c547bc5f3a24 | -3.19678 | -50.44608 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a017646f-d48a-3e55-9ec3-43b229db8d38 | -3.19382 | -50.43634 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ae18aede-3857-3770-8358-cb160243888e | -3.19307 | -50.44091 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| fbeeb1eb-ffdf-3044-a5ca-e1696931479a | -3.19232 | -50.44545 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| c0405dc9-e583-38dd-8018-7ffef71ab007 | -2.52172 | -49.02971 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f1bdc1e-ccd2-3940-a8f7-0fb1dc789067 | -2.48573 | -49.90709 | 2024-09-28 04:19:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95341dc6-da57-35f9-af54-24c4efc1d5c4 | -2.48413 | -49.90686 | 2024-09-28 04:19:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca8613c8-853b-37ef-9d05-b96482ddbb5e | -2.47649 | -49.15834 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3dbf857-a4c9-3048-a391-814fed38dcb4 | -3.14667 | -50.28321 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bef4796-e95c-37e7-9593-5c155a9360a0 | -3.14226 | -50.2825 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac9b3777-36a5-37d8-a66f-b8a8d38187c5 | -3.13856 | -50.27749 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6cd381e-4545-30e7-9da5-539df8d9be58 | -3.13786 | -50.28178 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca7110ae-f2bf-357f-a94a-975d5570efc3 | -3.13346 | -50.28107 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6127ae42-2d77-3410-8698-116e31cb00de | -3.11044 | -50.47903 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0558c399-3840-31b0-bcb6-009433b2061d | -3.10972 | -50.48345 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b19e6999-86ff-3aac-b27d-f185a6074dc5 | -3.10597 | -50.47834 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dece9763-7ba9-383f-a76b-6195b523e109 | -3.10525 | -50.48277 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7bf87c9-4f96-314a-90a0-d750915804af | -3.08667 | -50.48426 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| e535d49f-8dcc-3cd1-9599-0c6901075a06 | -3.08293 | -50.47912 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| eb566df0-8986-3c18-b246-b2d234f95e1b | -3.0822 | -50.48354 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 73695075-be0c-3e4f-8061-e81b4b4005aa | -3.07918 | -50.47401 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a6eae522-0640-396c-894e-77549a8c4c25 | -3.07846 | -50.47839 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8e9d9ec6-6b20-3329-b2b9-54a59d850183 | -3.07774 | -50.48281 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1a4bcc06-09c6-3262-8bb4-9a5f5d032e44 | -3.074 | -50.47769 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3cbeca1f-cb66-339d-a9a5-22cf46f0e2e0 | -3.07327 | -50.48212 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6e11cf7a-8b84-32c7-8eda-54b83b75e409 | -3.07253 | -50.48656 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 08af7307-b3d2-3933-9ca4-4659441ea01e | -3.06879 | -50.48143 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54b41ec7-afe4-3b7f-8f5d-f095340d441d | -3.05915 | -49.56021 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f3b4e760-042e-3ab0-b949-6c4e00324f65 | -3.05853 | -49.56411 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 17b0692a-6527-36f8-a2bb-245f0ad776ca | -3.05557 | -49.55569 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7e7ae56-88ed-3191-b0a6-d6cd1a2d4aa6 | -3.05494 | -49.5596 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0e19d2a0-8880-3e9d-a4bf-a4d58df0ed37 | -3.05432 | -49.5635 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 061ba86e-5417-3b92-9503-fc4c2a152211 | -3.0487 | -49.49153 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab2bd94b-e94f-3818-86a6-fad167255bd1 | -3.04514 | -49.48704 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1865341-c2e2-38a2-9872-55fed07354b4 | -3.04452 | -49.49086 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4053aaef-2022-3891-a75d-f75650e6d7c9 | -2.95352 | -49.35626 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d819150-dcdf-39fe-ae8a-cd79dfa535c9 | -2.95291 | -49.36004 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 256f3ef0-d144-3223-9285-f36ef6c51d03 | -2.9523 | -49.36382 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ff32982-2a66-3d7a-885f-d39f67b353bb | -2.94944 | -50.30263 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5f60953-a436-3a3c-8632-f730296355f9 | -2.94938 | -49.35559 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c68652c-0522-30ad-8cf1-3142ee4e5fc3 | -2.94877 | -49.35937 | 2024-09-28 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cd0ceab-e9af-3d75-b266-9f21270703bf | -2.94857 | -50.30528 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60f007b7-6c5c-3ee2-9159-cbf34c0eda94 | -2.89516 | -50.47013 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0be87ae5-c64d-379c-a1b8-8d9749d78dbc | -2.89443 | -50.47466 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8b210dd1-0e30-3abf-a8f7-7ce832e2f3b4 | -2.80451 | -50.2765 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed8abfe8-063f-3abb-8453-a325cf2c1024 | -2.80009 | -50.27579 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fac50cc0-b5db-3fc0-9387-98d4990fa995 | -5.16363 | -49.48513 | 2024-09-28 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20668591-e153-3bfb-b784-0fa01d18e907 | -5.02836 | -49.76888 | 2024-09-28 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6855f171-c99e-3a20-96cf-e00d624eff5c | -5.01599 | -49.76686 | 2024-09-28 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 240e2ce9-9b74-354e-b623-8584074b2ffe | -4.06516 | -49.94193 | 2024-09-28 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66d2e15a-1fcd-3307-93e2-4d79b9800e9d | -4.06321 | -49.95392 | 2024-09-28 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 674bdc90-c64f-3abd-b0a4-982f7c34b898 | -4.06256 | -49.95787 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4004e9ca-0a81-34c2-b770-451c9f530bba | -4.05898 | -49.95315 | 2024-09-28 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af56aa01-dd41-333b-a1c7-06f09cadef2e | -4.40774 | -50.69484 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abb8339e-ef4a-39d9-9b68-3ab0902a27e5 | -4.40703 | -50.69918 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89fa580a-5f6e-36c6-8999-83285bb6a1a0 | -4.40648 | -50.69742 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ce43f70-abff-30cd-a010-60ee11815e4d | -4.4026 | -50.69845 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e8defd5-83b1-3513-abd7-90013abe1ae8 | -4.40205 | -50.69669 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d19d2b7-c751-38c7-8e0a-783838fe4080 | -4.36075 | -50.78658 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df855dd7-5a88-3022-b58c-8c988ea29513 | -4.3205 | -50.75288 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d88879c0-c3c5-3546-892d-2398517399e7 | -4.31603 | -50.7522 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7cae02e-3c15-38f8-9b82-3a3939e27d6f | -4.1258 | -50.26293 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28e3b169-894c-3060-849d-dcaf7f7ada8d | -3.68604 | -50.19048 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66512c67-eea4-32f7-b94c-c9f12211f4d7 | -3.6817 | -50.18982 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d33dc756-3034-3ce9-8bdd-5e2289ed53da | -3.58045 | -50.55594 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa63ff47-4e4b-301f-a128-f61c82fefefd | -3.57973 | -50.56023 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eae2ba83-609f-3484-8d9a-32ef748f4a2b | -3.57639 | -50.39096 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8db0900c-3fb8-31bd-bdf4-903327ac4227 | -3.57601 | -50.55516 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 892ddb04-389b-39bb-9bba-b39a7e492c6e | -3.57569 | -50.39534 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fee8949-04bb-306c-a1e3-4dd7155fd9b5 | -3.57528 | -50.55949 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b785466-8aab-3c0d-b871-20eb5657edb0 | -3.57382 | -50.56821 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1621538d-8e4e-3bf6-a5a4-ae2422e56ace | -3.57309 | -50.57258 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf4bb9f2-7814-3951-848f-b4ad806dfd2d | -3.57255 | -50.55634 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README46.md)
