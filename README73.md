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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0d933fb-01cf-3a50-aedc-fd9b96cb70ca | -1.60609 | -52.29163 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdff143d-e727-33a9-952e-5dfcc419a8ef | 1.48883 | -55.97997 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f972f8da-c363-3ce5-bb77-85a9b99342af | -1.09227 | -53.36699 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c44455fc-4e63-3e88-a886-e3c6243289b9 | -1.64442 | -52.43652 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71e63206-a473-36eb-a597-3e6fd836aefc | -1.08755 | -53.37143 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 52080612-33a5-3d19-955b-f3be2387124f | 4.26074 | -59.99118 | 2024-11-28 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96cd108f-d77d-3850-b025-a88bc1705685 | -1.74827 | -52.65988 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b8339f0-1a74-33d5-9ff0-7a9932c84b10 | -1.59973 | -55.38931 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20324012-d853-3b1f-aba3-6b90734ac190 | -1.20264 | -51.7574 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c57c1d4d-ca91-3279-abb4-707f90712d0a | 0.93902 | -50.74092 | 2024-11-28 05:16:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2348c4b6-2316-3710-9278-a1391e612387 | -1.32838 | -51.93346 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e34d00e6-3b67-3574-ae7c-252f22e34298 | -1.64448 | -52.46429 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f78f1e4e-a916-3105-9483-c354cba2331e | -1.16075 | -53.57271 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c104a417-259f-376a-b49b-ce007aec5b70 | -1.71602 | -53.25186 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ddbcebe-7eec-37ee-b36e-c423c884a7c7 | -1.29326 | -51.72545 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f619fef9-b59a-31c3-99f9-3cd63a32c7ab | -1.49778 | -54.46146 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 10fd2b76-1963-3b82-909e-5acb04ab1446 | -1.31833 | -51.73819 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 744d1ceb-c429-3814-8376-1e96c1603140 | -1.65933 | -53.80676 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e229441f-c94d-3c69-bff6-c491e002ad2a | -1.59377 | -52.08788 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b510ada-09eb-3103-bd74-7a68b7c84610 | -1.62596 | -53.87045 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b56b5d4-3a03-37ef-8241-cd3337ddfeb7 | -1.69465 | -52.62064 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d037b43-e8c1-331a-b4b3-60295ed4590e | -1.35244 | -51.99027 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81d6e658-4b6b-3fed-88c3-5ae4020dbbc6 | -1.66697 | -52.72014 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 910caacf-f067-3bc9-a67f-bf4a8fcffb21 | -1.73582 | -52.04091 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 067b072f-8ded-313d-ae1c-e60829127d79 | -1.88406 | -52.65913 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e82307d-c11f-39f0-a595-592a2182e198 | -1.35614 | -54.63069 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f91cf782-9a2a-396a-aed2-50f4c6d0acc4 | -0.5844 | -51.70148 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b538768-5ab7-394f-ac59-713023ba6551 | -1.62566 | -52.10983 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 464658ef-f775-3ca0-9a09-e60258436928 | -0.96236 | -51.64908 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8fc2499-8219-3da4-a940-df18d51b3a62 | -1.23178 | -51.8009 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcc80a28-3697-3a62-8e2d-b11f44f70c16 | -1.35679 | -51.96135 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5557a142-14ba-3491-b3f9-996ce2d66b1f | -2.86043 | -46.84599 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 876603f9-ea46-3e78-899a-5322eb8afe77 | -1.19891 | -51.75247 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ee68c73-b0fc-3a28-83a9-dcd8cfab36ce | -1.65926 | -52.71513 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| baf43c59-1482-353f-b793-2e12a30fff46 | 4.25949 | -59.98306 | 2024-11-28 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e7e3996-454a-3452-af5b-9e50969d65da | -1.20329 | -51.75315 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16179056-0f71-3220-97a8-dc7cdb1547ba | -2.01886 | -52.07985 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2db9ad43-f918-3299-9ce7-148493d8505b | 4.26181 | -59.98795 | 2024-11-28 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| effd0cce-9af5-3ad8-8395-851e5f3847ab | -1.71203 | -53.25124 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91eb7bf3-8142-35ec-bbad-af9f136fc0ef | 4.31664 | -60.82828 | 2024-11-28 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec96282-09aa-34e2-b7d5-8d7372d82b12 | -2.84463 | -46.83595 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8db26e06-9629-3854-b212-3e5010fcb33c | -1.45899 | -54.49894 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ff08970-d93b-38f3-8494-fbb141da01ac | -1.64382 | -52.44041 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46705e51-6b2f-3c79-bcc5-d5fab681e038 | -1.62911 | -52.70286 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6dcaf513-31fd-3e8d-a22c-a5cdbb9caf98 | -1.0999 | -53.60722 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e61fbd3-28a3-37ba-bc37-2ea76a630d4c | -1.68351 | -52.46243 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b14b2e7e-4be9-3722-a7b2-67ebeac2943c | -1.38478 | -53.63023 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4917bc0b-6cc8-309d-a44f-a1cff84c2334 | -2.84173 | -46.84278 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fd9b523-b775-31ee-a1fd-b93c9cb9bf6e | -1.10288 | -54.14313 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86a6b1e9-a4a3-3e7b-9c7f-58e962e63281 | -1.66172 | -52.72696 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1d5c607c-0858-3e04-a086-64f77c4627d5 | -1.58795 | -52.23997 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81200853-36b3-369b-9409-74d0dff2f4c6 | -1.14825 | -53.70409 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63ade69d-fb49-3d43-8fb7-52c5db7bddf0 | 0.98188 | -50.126 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2dfe5e2f-207d-33b6-8799-3cef09b33efc | 4.65255 | -60.51673 | 2024-11-28 05:16:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37fdb795-128d-35d6-95b7-7c1ad05382b0 | -1.58001 | -52.2632 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3b9f855f-e147-32a5-92b8-9f8cb7bcc3da | -0.26098 | -51.4915 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9add0b42-95dc-3812-ab45-d10ce1d57dea | 1.46187 | -55.94019 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa01ce56-a576-3d9f-b8a7-b59403170a93 | -1.45265 | -54.51543 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0be47ceb-69a7-3ab8-9bea-09dd98ee4a88 | 0.99162 | -50.25917 | 2024-11-28 05:16:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2de1c273-af35-3014-b203-d00465cdee40 | -1.37622 | -53.63418 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50b54c1b-e214-3d1d-a68c-a88407d01814 | 0.98616 | -50.25497 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b803ceb-c9b8-383f-9bc1-6d0fdc00fe96 | -1.45286 | -53.42441 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e64cad86-6e67-303c-a5a2-940ababf90ee | 1.72051 | -55.80497 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e593ee-5d50-30e3-821e-692908686eda | -2.84389 | -46.84091 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75524f07-6231-3ae4-a869-9ddce3855a38 | 0.98224 | -50.2607 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 898a9872-878b-3bc4-9b6b-9cf622e2e6f2 | -1.74338 | -52.80032 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be6260f5-f675-3249-82ad-4ea8f54ae5e0 | -0.29785 | -51.75289 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d81c488-9c56-38ed-a301-72cedeeb61b8 | -1.33622 | -52.43931 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd9b2937-5b1d-32c2-b6b0-d62e350a05e2 | -2.87152 | -46.85765 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0fa32f1-047f-3e08-8837-1014957fb95e | -1.46316 | -52.29116 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17603b8a-ffca-3fb0-a647-83979521d4a5 | -1.71655 | -52.47516 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81aaa323-6e63-37d1-8420-e163ccba0fc7 | -1.79617 | -52.75041 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2142a469-a1b2-3ae1-8c86-e2042bfc2480 | -1.12315 | -53.73899 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cf8cdb6-d678-383e-8280-20ea28983dcc | -1.19284 | -54.01621 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c608f720-a38d-33c6-a75d-4089e4316d5a | -1.62375 | -52.37341 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2c8851a-9cb4-3cb9-a95a-cb1bdc46f557 | -2.05561 | -47.12247 | 2024-11-28 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18861c64-b7e9-3e1e-af46-66348b72d868 | -1.66943 | -52.73195 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fc1dee38-7995-30ed-a451-31f143887816 | 1.88702 | -60.48459 | 2024-11-28 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74f5e57a-575a-34dc-a483-323de0086db8 | -0.77667 | -52.38969 | 2024-11-28 05:16:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 400097b0-c689-300a-b6a9-ebf65bad44b1 | 1.4456 | -55.91366 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89cf5103-c661-3c76-9a93-1f0bf5e5ce51 | -1.18692 | -51.77231 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6e99cf9-3fba-3fb2-bf95-15c4c4699cab | -1.6823 | -52.49781 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4b6b28e-f8c5-31a9-a74e-a60044984091 | -1.82742 | -53.65756 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6d3c4d3-ee71-36ec-9c6c-86590b93db82 | -1.12755 | -53.71054 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a57a2e10-7c20-38cc-9c0b-b460335a467d | -1.33143 | -51.9424 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50bcb01d-9dcb-33fb-b06d-4ce78ff971ec | -1.6873 | -52.49828 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ed89f86-a4bb-3af9-89f4-4adec39809af | -0.67962 | -52.37125 | 2024-11-28 05:16:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 068640e2-f5b6-33b7-b645-0efe443e1ae4 | -1.6559 | -52.47397 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1acb559-318d-3a45-be0f-55aacbbfb335 | -1.27816 | -52.17129 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36a39aec-bd74-377e-80ca-370742cb154e | -2.85895 | -46.86824 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 843e2538-078e-3f57-ab55-32f4727d83d2 | -1.09181 | -48.21099 | 2024-11-28 05:16:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3104d1c-f788-3f86-870c-da85a712ecb6 | -1.59008 | -52.08314 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c138f21-8f2f-3509-b600-1a440bed77b0 | -1.12346 | -54.16726 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cf486d0-f680-36c8-96e2-37c55c2e6245 | -2.00617 | -51.1725 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b49ad4d-387e-3967-b9ca-e900e72c5ff0 | -1.20963 | -51.74109 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dcb04a95-1ff4-35f9-863e-d385c3605e0c | -1.70308 | -52.5362 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3fde75a-989a-370b-97e2-6fba6b7853ef | -2.84449 | -46.86824 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f52e1a89-4104-38b3-8995-252f1313c856 | -2.65549 | -48.5075 | 2024-11-28 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d38b4f97-3c71-3761-b9ff-7e15869df25b | -1.67991 | -52.45791 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 055cc61f-e6ff-37f3-808e-e6f957581fb5 | -1.72018 | -52.47968 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |


[Clique aqui para ver as próximas entradas](README74.md)
