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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8040ded3-07db-3e63-9da6-63b229d8c3c1 | -7.05518 | -59.16803 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 46ec22de-df48-36a4-85c7-f51c741ca6fb | -14.36091 | -51.10441 | 2025-08-08 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc9c2390-9179-3956-86ba-b74c8cd73ca9 | -7.05348 | -59.17904 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54f7c528-1f38-31ee-aeec-5cf22975039a | -7.40828 | -60.0197 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 452a3571-db5e-3b86-bf27-80cd197848bc | -7.04445 | -59.19258 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 31cf7036-c8f7-3551-9642-2f3efdffccae | -7.40658 | -60.00866 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ccb35ca-3f8b-3400-936c-49bbb1912b50 | -7.0501 | -59.17849 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 2272c777-ac2a-3d82-a51f-553bab4cc002 | -13.04959 | -56.85845 | 2025-08-08 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 563a8e72-f5b7-3fc7-a88f-6b69e40ebb89 | -5.88441 | -57.74796 | 2025-08-08 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1f7e5e4-4362-3080-bc64-d8eb8a345830 | -7.0484 | -59.18947 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b21221c4-7766-3129-a03b-da1b07566987 | -7.41269 | -60.01322 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f5807035-3f63-358f-a016-72c6c38717c6 | -7.07325 | -59.1634 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| fb1ca0fc-691d-3241-b79c-a23d8852c1b1 | -7.058 | -59.17222 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 58b79f26-be5f-3538-91f5-deb249771aa0 | -7.04163 | -59.1884 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2bdfca9f-b4e2-30e0-b2c6-5cd523e151dc | -7.07438 | -59.15609 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2e197b16-92f0-3c5c-a2ab-5180b78e4b80 | -7.04276 | -59.18109 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 05fb319d-4436-373e-bbba-0a2057c4749b | -7.04615 | -59.18162 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 43a14c93-eca9-3e23-abf1-e1c599074add | -5.81356 | -59.22657 | 2025-08-08 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9ee37899-04f2-34ad-a3ef-e456d6c1c520 | -7.04558 | -59.18528 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b568a546-3579-32b4-b27e-fca7d9ea1f9c | -7.05122 | -59.19365 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7961ad5b-e2d8-375e-8f39-2b74717965f6 | -6.15652 | -55.80811 | 2025-08-08 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 010eb291-1a77-396d-b848-8ec1c9892ff0 | -7.07382 | -59.15974 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 7ba0192b-df4e-3247-85e6-70bc87226aec | -7.07099 | -59.15555 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b35c338c-af8c-3bef-a199-e10afd361cc6 | -7.04389 | -59.17378 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0fe6ef7-89bb-3314-84d8-3da939af9247 | -7.40047 | -60.00409 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d9dadd33-96cd-3744-b7dc-13948ab3576a | -5.81692 | -59.22709 | 2025-08-08 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46c3f0a8-3c81-3795-86f8-64654b88604e | -5.80965 | -59.22961 | 2025-08-08 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7dc596c0-d771-32f6-9eb6-704991e7bff8 | -7.05744 | -59.17588 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e6ca0e4a-8f60-3da4-bc4f-258433e9a3b6 | -7.05405 | -59.1978 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1903d264-2740-3f4d-815b-bfab2e69effb | -13.04855 | -56.86591 | 2025-08-08 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4f6cd2a-7a0b-34f2-8e78-e07e24f30852 | -7.05066 | -59.19728 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 18ab3123-b937-3b38-89e5-23024816b84c | -7.40379 | -60.00463 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0fb91d6e-5f59-3fce-b02f-3391645522c7 | -10.23201 | -67.31347 | 2025-08-08 05:23:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b9b49ee-8efb-3318-ad2a-3a5beae19314 | -13.03987 | -56.8684 | 2025-08-08 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d42216b1-55de-3339-81d6-466009bdf8ea | -5.00384 | -56.03988 | 2025-08-08 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9db0bf2-be71-3518-b16f-8cfab18c1d37 | -5.82028 | -59.2276 | 2025-08-08 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5192b638-5e03-3d72-95f1-c5f6121be7d1 | -13.04499 | -56.86155 | 2025-08-08 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 505bf989-43a9-3c33-8298-ed27291a0b5e | -7.06328 | -55.41151 | 2025-08-08 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b3952e0-7664-3139-9273-a887c516b9cb | -7.04332 | -59.17743 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cfc5ecb6-0f6a-3f66-a69d-0069c9da5ddc | -7.07043 | -59.15921 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f8e85aa1-224e-30a8-8576-9ec3c887f86f | -7.03599 | -59.18002 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0286b68-466e-3811-9db9-5275166861b2 | -7.0597 | -59.16126 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3acee1cb-edc8-3dd0-8701-8b2130e661c9 | -7.03881 | -59.18421 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b65661d6-4c54-3998-b701-699e56118ebc | -7.04784 | -59.19311 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b82693ee-78e8-377c-b807-5e974c17b64a | -7.41772 | -60.02478 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 516daec6-0edc-3832-aefe-e8231ce8a81f | -6.09148 | -59.92875 | 2025-08-08 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32fdbe51-85dc-370a-bc20-cb75fc1addc1 | -7.59944 | -55.19738 | 2025-08-08 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a40bc2c-5fe5-3048-bc00-591260cae7f6 | -7.04784 | -59.17065 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4be10c05-928d-32de-b219-c1b64184d55b | -7.06534 | -59.16963 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3cdc547b-a882-3a70-a4c3-8e67a5a59d49 | -7.06986 | -59.16286 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6ea0d74d-f2aa-3181-bcc8-c7a0a980b500 | -7.06309 | -59.16178 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95e2023f-31b0-322f-bf79-c7a091ff35eb | -6.15254 | -55.80756 | 2025-08-08 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a449ec9-12ed-3b9f-b971-9442b99ef9ce | -6.0948 | -59.92926 | 2025-08-08 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02203c2e-5c69-3a97-aaab-72589da8f62d | -12.61371 | -48.11098 | 2025-08-08 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ace90cb9-565c-39cd-a87e-2acb8a4ee3aa | -5.81411 | -59.22301 | 2025-08-08 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ee69c91-4e28-33f2-886a-2489a7871049 | -5.88378 | -57.75197 | 2025-08-08 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9bf617d-4ec1-3993-a965-886b3bf161d9 | -5.81747 | -59.22353 | 2025-08-08 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a911c653-39e0-34a3-9f88-2d71a24c00a7 | -13.04907 | -56.86218 | 2025-08-08 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37214949-f886-3998-9afc-e9ccaac6e27e | -7.05179 | -59.16751 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 215de499-875b-3d4d-9aaf-98b0bd418d38 | -7.03825 | -59.18787 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ed67a30b-9d38-3fda-99e6-f097ede1c705 | -6.63965 | -58.81973 | 2025-08-08 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf6a7098-f844-3ef0-8a02-39b387972248 | -7.05857 | -59.16856 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a61b11c4-c99c-346d-b1ec-6830c12b3397 | -7.06591 | -59.16598 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dd6146fc-b0c7-3d89-bcd5-e165f9566295 | -13.04447 | -56.86529 | 2025-08-08 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7d9a56a-a31f-3f5f-b7e3-e3e2fe354afd | -7.06275 | -55.4152 | 2025-08-08 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e34c1ef-b81f-3153-9cc2-d7b06e0ca6fc | -5.88026 | -57.75136 | 2025-08-08 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91f571c5-9496-3288-95c8-56c6699ff55c | -4.99998 | -56.03934 | 2025-08-08 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c43936c-a092-3f6f-b6da-61ba651f6e7d | -7.05123 | -59.17116 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f2ca2417-2863-3cf7-9b1a-6c5b5d893f52 | -7.06365 | -59.15813 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbf42be4-75d2-3701-a507-752e400f9549 | -7.04671 | -59.17796 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 71423b6f-5a7d-3de6-a8be-dc4c212b0661 | -7.05913 | -59.16492 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 73cf8c39-49f3-39ba-af9d-eb1ee97b5818 | -7.05405 | -59.17536 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8123641c-5b03-3df9-b60e-9cf6f693c41a | -13.04551 | -56.85782 | 2025-08-08 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72f6964c-7248-3275-b291-d6ca9a14eaf9 | -9.63995 | -66.99906 | 2025-08-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92e1d3f8-8867-3725-844a-b024437e1723 | -7.04728 | -59.19675 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e8c2c94d-58df-3447-9546-34d0deffe7fc | -7.04896 | -59.18581 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| a9a51883-17c0-31ce-a813-93167ab21753 | -7.40155 | -59.99705 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1fa0f183-bc78-3bad-9aa8-02e59b643d79 | -7.05687 | -59.17956 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6087489b-36c7-3e96-b63c-81dcd5d4ddf6 | -7.06761 | -59.15501 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b39792a8-800a-3653-9e7b-5dc2fdbf26cf | -7.05066 | -59.17483 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d1674b48-7ec0-3e82-a9fd-d5bbd1382706 | -4.99855 | -56.04892 | 2025-08-08 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb9fc914-0854-384b-9a47-085f81e81b0f | -7.06704 | -59.15866 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7b08256-5931-3313-b389-05623b5e6a5b | -7.40549 | -60.01567 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cdecee6-e92f-39fa-be77-5535cf1d1724 | -7.0563 | -59.18324 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e3d84652-4f8b-3482-a9a8-5aea665d49de | -5.45649 | -60.16649 | 2025-08-08 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63f63bf3-1199-3c5d-a4fb-513885f26575 | -7.40936 | -60.01268 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd5f89a7-48ca-35fd-90f2-3a9d3c6f4fe6 | -7.04953 | -59.18216 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 7b3e88a7-ef3f-33ef-be57-059eada774de | -5.88087 | -57.74734 | 2025-08-08 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 448ace4d-56ed-3870-9a1f-6c9d0fface79 | -8.06679 | -49.71827 | 2025-08-08 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f7a6c55-55c3-3a1a-b71b-6d6646afaced | -7.06196 | -59.16909 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 622a59e6-41a7-3e91-90db-6aedda143f06 | -6.63908 | -58.82343 | 2025-08-08 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54f55374-b64f-3103-80c3-27e56d89016c | -7.04502 | -59.18893 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| dd3a8330-b3b1-3923-801f-dc9b33f536c8 | -7.04107 | -59.19207 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18acc204-44d2-397a-8d29-be89a3cdb088 | -7.04727 | -59.17431 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0d3c568a-8f06-3fab-8f42-7e3641d5dba2 | -13.04039 | -56.86466 | 2025-08-08 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41a92126-88d1-35f8-8d98-112a5bf639e3 | -7.04672 | -59.20038 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab7710ee-f047-375b-853b-0169566d4cb5 | -13.05367 | -56.85909 | 2025-08-08 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7d7387d-95ce-3a0b-8cf9-18c6f29cb958 | -7.0501 | -59.2009 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb2b3730-2797-32ee-9b94-92c401b06e32 | -7.40101 | -60.00058 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0433bc92-f705-3337-aa94-d0a4af03679c | -14.367 | -51.10521 | 2025-08-08 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
