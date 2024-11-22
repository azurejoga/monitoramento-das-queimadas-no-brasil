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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb2eab74-e1d7-359b-ad0b-cff8ec5889e2 | -1.71023 | -52.48503 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f40c8f0-b22e-3ef4-ad16-c3def355ca24 | -2.26849 | -49.08462 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34e47b09-3b71-312c-9ac1-161b376c12ee | -0.9239 | -51.74152 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31c94bab-3ae1-3b83-8c6a-d86360b753cf | -4.00373 | -54.34013 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 104179b6-fc30-33b0-8446-8440fb3705a6 | -1.24462 | -51.74709 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 746b9e18-d74d-3e48-bd55-582d19b9175f | -2.14729 | -50.27516 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca17e029-b992-3eea-8bcf-42352846af7b | -4.8712 | -48.21645 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a4c82f1-4114-3ade-9416-3731c065ef98 | -5.82032 | -44.74815 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0163cdf-2a30-3875-a3a4-50108537604a | -1.44359 | -53.39412 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8dbe19c5-3b9f-33bb-bdce-7a8aec2de170 | -2.6313 | -46.56815 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e4b06b9-4cd8-3ffe-b2c4-910db9203241 | -1.64446 | -52.62463 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f26ae05-8587-36ca-b37d-7f87d6da1d30 | -1.1978 | -51.95044 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3a24a043-0de1-31dc-b8c6-f3dee4a2851c | -2.15135 | -50.49194 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f35b6b7d-c843-37a5-a320-4034518e02e6 | -3.28637 | -53.83282 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48ece6fd-c71a-38cc-83a0-72cd3c54bac2 | -3.85362 | -51.40389 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0434a41-4fd3-33e2-b837-e93179119d70 | -2.57952 | -46.54173 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a75c8ab1-da98-38fd-8377-d05e43ee8bae | -2.19763 | -53.6562 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c83f0f36-68e7-39d8-90f6-da081da91b36 | -3.51663 | -54.68981 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cce9075-bcfa-3916-9211-7377e54a859e | -3.79907 | -46.60348 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d163f418-8888-3501-b22b-6189d4b4d53a | -2.70505 | -45.2359 | 2024-11-22 04:36:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c016174f-f523-35fe-955f-872867716cdc | -1.72549 | -52.71122 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e4cd2bb1-8044-3727-bf19-63a5fcd4e4ce | -1.21812 | -51.79613 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8513e603-44c2-305f-9641-2f7f01a20187 | -0.04647 | -50.81707 | 2024-11-22 04:36:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27a47268-efac-35b5-95cc-27bcf206400b | -2.75865 | -52.11254 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba3448ec-37d8-3292-a3ef-319d4a05dc96 | -5.81595 | -44.75505 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3a03cf2-f7a8-3d81-abc5-2fba90c6a3f6 | -1.20079 | -51.76229 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ef4b6f4-374a-3a09-a5e6-2850e052d49f | -1.20818 | -51.96869 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed650165-4e3e-32b4-ba59-6f1bda1edfb6 | -1.65091 | -52.67259 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c168768-7ce7-32dc-a6a7-77a36dcbdec8 | -2.1772 | -46.69532 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 392af74e-b88f-3495-9298-af1acaa0cce2 | -3.05969 | -45.69254 | 2024-11-22 04:36:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d454b171-3293-38d6-8053-8e425f471ded | -4.23544 | -41.92968 | 2024-11-22 04:36:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69804e4f-4af2-3c8b-8b91-cd95368c4f0d | -2.1774 | -49.081 | 2024-11-22 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0371e882-a6c0-394a-b6aa-0c8e5d99dfb5 | -1.30373 | -51.75064 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7587edb-6043-3d4a-aedc-69a9de727082 | -4.81457 | -49.72289 | 2024-11-22 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 231a094c-ad09-3e22-be14-a7c0a749829c | -5.93339 | -43.78293 | 2024-11-22 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffe6ac4f-f818-352d-8b51-ea6dadffb56c | -1.74478 | -52.39058 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 425d7e3b-0266-36a6-8500-db36735a8971 | -2.68886 | -46.19486 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39f795c5-c8be-3cee-bde2-7b6ad35509da | -4.13374 | -54.65562 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 700f9452-1018-37cf-a7dc-093ae182e195 | -3.28929 | -53.84063 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ca26c7d-8daa-38e8-aa4a-7b9a6bdfec4e | -4.75076 | -49.26648 | 2024-11-22 04:36:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcd0aa29-44a9-3342-8884-d67445387b69 | -1.741 | -52.38998 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 271662d5-510b-33d3-bdb3-4f0879536da4 | -2.1955 | -50.30156 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a89129ee-559e-3b9a-aeb8-496445ad10e9 | -3.88568 | -43.99139 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c58ba94-4458-3694-bf66-10aeb95c52b2 | -3.11143 | -53.70621 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfcce637-b4b5-3631-8be3-79e42805b794 | -1.44821 | -53.3912 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d1d0736-6742-3267-a953-e6e752ddf0a0 | -4.06335 | -50.00267 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7abc07c-db38-3af0-b736-d348c817f54e | -2.40107 | -48.61143 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 125597fa-9376-380a-a97f-4e6d60f82df8 | -1.7777 | -53.59795 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afe58eda-8e23-3482-8189-92182ea875bc | -5.81741 | -44.74504 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be62d916-fb4e-3c10-aade-91f3fba80490 | -2.13237 | -50.70111 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98e08569-9198-3d28-97af-ae8fb34b565c | -2.69516 | -46.22323 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6bfe2ca-000b-32e4-9344-1616adf15515 | -2.70381 | -46.2363 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba48906c-f016-3464-82b4-595d7d3f849a | -2.79219 | -45.94443 | 2024-11-22 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8f16cb5-8e9f-3f30-a8fe-183c44af8e62 | -3.23529 | -54.23367 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 103f4600-50d0-3670-ac85-ad461ec0bcb3 | -5.50384 | -44.56293 | 2024-11-22 04:36:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c83ac95a-d3d7-3a83-bc9d-e5f610442d42 | -1.63425 | -52.40389 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b547a38-cc91-3a7f-baf5-b319c6492ed5 | -3.06389 | -53.28656 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a38f66e-25aa-3e6e-bc8e-5c0557f2843e | -2.9504 | -48.33552 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec93aa23-6a3d-37a7-9e03-79a760991bae | -0.93731 | -51.65487 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b38bb995-3885-32a9-8ccd-af17f490507c | -4.88187 | -50.93962 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce12a083-7b8e-330a-aaf8-8fda758ea3dc | -3.23067 | -54.24463 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8a98ea76-11d9-3e60-91d8-7a5f02881f7b | -1.40267 | -50.70887 | 2024-11-22 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d87c8550-6ae1-3172-bb6c-5bf38430c5ad | -2.10155 | -50.36307 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44bd4b35-b970-3439-85d9-4966fa0523e7 | -2.61965 | -48.19168 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6eb1bcc-e2f6-3440-a72c-aa919e9857c8 | -5.81566 | -44.75252 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e262d5d-7293-3b8a-94bf-9dcde7d2122a | -2.3444 | -48.7963 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8b656e87-09fa-3d7a-8abe-a15a863c01d8 | -1.73342 | -52.38878 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5662ce65-f35c-3b73-9bc6-7d071860bb62 | -1.63322 | -52.68455 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2067470-e741-31a4-ae5c-06ca9aa0f019 | -2.63363 | -46.21852 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a04f79c-7283-30de-8013-4ee74a6c38cb | -3.41314 | -53.2171 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 481d9d9e-adaa-3e8d-ab2e-4adb3ddd48ca | -2.9513 | -53.71397 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8628681a-01b6-3c16-8ba9-00b7fb372163 | -4.57957 | -48.01679 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4a6f915-9e25-3146-bfda-f31f6194f4a8 | -3.87199 | -52.35956 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74f5ffee-5c40-3664-9285-8bce8ccc36cf | -2.44529 | -46.54782 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8d13843-dbbd-3148-ac42-479e607b302c | -2.74667 | -54.12566 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05247138-851a-35ec-82a2-e75827b7d983 | -2.65633 | -46.24468 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a73b455-7f95-32ab-88b9-4dcd2ee4f933 | -2.36335 | -46.73861 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9f2c65c-6fe6-3065-b6cc-34447bd74c49 | -3.66563 | -54.65623 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c038eca7-b1fa-3639-b796-17b45fbae100 | -5.81643 | -44.74752 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6fb7598-5c47-353e-b5e2-23f92fa36dcb | -1.45743 | -52.65891 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25e782d8-b7bb-3979-8be8-8e978fd5e830 | -3.10566 | -54.28768 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b55f391-e06e-3239-a717-7a8e1e1a62ab | -3.19001 | -54.32908 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d62e95bf-6093-34b6-854c-7aa5525644f6 | -2.66217 | -46.55012 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5755e8fb-e3af-3fee-a743-f1904ab0201b | -2.40377 | -50.31502 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb94d310-5441-3521-ac10-99cc9aabbab4 | -3.10026 | -53.74503 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b1e4c85-ff9e-3d8f-9fee-180784f424c6 | -1.51741 | -52.08619 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c88c34b0-35f0-3d7c-b058-e0df97875734 | -1.83626 | -52.17671 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ee086d8-a318-3ce0-be2b-94c61913db06 | -0.18903 | -51.55838 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d7be5f7-fb39-36a0-b68e-33dbbffa0bb1 | 0.16709 | -51.22694 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba6d25b1-be0c-3a04-b963-539a7d2e2839 | -3.53675 | -54.08957 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5bdead8-74e9-3b40-a75c-5088b4fd0bc6 | -3.56588 | -54.22474 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 07ff25e6-6a5f-3a09-84f5-bc6091ff5286 | -2.28719 | -51.09612 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45e90a0e-d1b4-3332-a677-a70bff7452fd | -3.47061 | -45.91166 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88d69ae3-6830-32b5-bbbe-d720716b1a71 | -2.27207 | -48.45787 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e48feed-17e6-38d2-8ba0-7644dc75ba9f | -2.16183 | -53.80079 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb335e35-59f7-3e01-a8f4-66493bbc1e56 | -1.72935 | -52.71184 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 77664893-1a4f-383b-90d2-be1436b95651 | -2.61639 | -54.05114 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a1d7f6f-6092-3deb-a9f5-df2c542ada9a | -3.23197 | -54.23686 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| cc469d21-e9fe-3cd0-b44c-4bdf42b385a0 | -3.26662 | -53.82624 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 586a35b7-bdef-332c-999d-e6856c167afd | -3.21551 | -54.25037 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README52.md)
