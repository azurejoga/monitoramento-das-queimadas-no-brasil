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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0af0515-7a82-3216-b056-52a004c7a56b | -9.91932 | -59.90702 | 2025-04-18 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 996d3d69-36be-3628-8c11-007a35745023 | -7.90819 | -61.51217 | 2025-04-18 04:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 670fd1ef-83fb-38ec-82fc-ed4a0daafc56 | -15.07619 | -48.94643 | 2025-04-18 04:59:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd95a8e3-c7d4-308b-a284-374b8b57f93b | -9.92823 | -59.90316 | 2025-04-18 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bedff23d-4e16-3216-9688-4724ec32b498 | -11.39985 | -52.94244 | 2025-04-18 04:59:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eaeeb96d-6de0-337c-be7f-800816c75933 | -9.92423 | -59.90245 | 2025-04-18 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6a77f98-d032-366a-9b16-2b12e2619b2d | -7.90358 | -61.51143 | 2025-04-18 04:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4432138a-2e52-38fa-b0d9-b84c8119eb3c | -19.49183 | -57.42965 | 2025-04-18 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 637e6a50-4c4c-3820-bfae-9d05db6d1294 | -29.40721 | -54.03866 | 2025-04-18 05:04:00 | NPP-375D | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 323689c3-5d23-3836-bc41-e2cb35f6ea81 | -29.40314 | -54.03794 | 2025-04-18 05:04:00 | NPP-375D | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 03ebe1e1-ccd0-358f-a023-63a534a76d25 | 1.99566 | -60.87229 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db374dc3-be3e-3df4-87dc-1299cfe45065 | 1.99218 | -60.87284 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57d9adde-4a88-3efe-96a4-26d8cde1dec3 | 1.99854 | -60.86792 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d95708b-ad1b-35da-86fe-c28a858efb57 | 2.39348 | -61.29448 | 2025-04-18 05:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a13e90c-aede-34ae-a6af-e2a60e3543bc | 1.99913 | -60.87175 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b5d9839-87e7-3e4d-8eb8-550bce64d871 | 0.69276 | -51.44619 | 2025-04-18 05:18:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c2f26c6-6e2a-3270-bacd-1536abc69ef7 | 1.98812 | -60.86957 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4db0d8ab-137f-3f30-8bcb-908481ca08c0 | 1.99514 | -60.892 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a714d305-3e9e-31ca-8513-2e68c7bb35a1 | 0.6945 | -51.44855 | 2025-04-18 05:18:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec7e6c93-8aac-3cbf-a1d7-6bae5eca8111 | 1.98871 | -60.8734 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 774e4475-1188-34cc-aaa9-91414bdf153a | 1.99159 | -60.86902 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0e1efb1-c8e7-3686-b7d3-d0b8b270f494 | 1.991 | -60.86519 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 808fc7ae-4518-3984-ad6e-d0b52e8efc23 | 1.99448 | -60.86464 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76623932-9195-3d61-a7eb-9544e226fb8b | 1.99277 | -60.87666 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1160aad5-5964-3de3-8887-61f3d3194b0b | 1.99507 | -60.86847 | 2025-04-18 05:18:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3269e233-2730-3d32-aff7-7790dc1d2a7d | -5.00928 | -56.17452 | 2025-04-18 05:21:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd49a063-2743-3e87-8eb8-2f9a9ad65adf | 0.76654 | -60.60608 | 2025-04-18 05:21:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3a437cdf-4676-3898-82b6-3626484fed69 | -9.92486 | -59.90437 | 2025-04-18 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| edd35ce8-3168-3dfe-a77f-4bbdcdccd6c1 | -9.92663 | -59.93786 | 2025-04-18 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e3fbfa3-4903-3e52-89f0-d8bd6a2170c2 | -7.90485 | -61.51071 | 2025-04-18 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cea38ce-02e5-3f29-9db3-be7b6289f775 | -19.49188 | -57.42753 | 2025-04-18 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 14522148-e1b0-383d-b855-3961f3cd02d6 | -12.36214 | -60.80592 | 2025-04-18 05:23:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8775796-3a63-3648-89fb-49c5087aaecf | -5.7898 | -43.61024 | 2025-04-18 05:55:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 89a97dda-d854-3f3b-ab71-aff25b91baa8 | -6.95272 | -43.03838 | 2025-04-18 12:34:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 7e05d8ac-548b-3990-a3b7-8e9f63dbfdc9 | -7.32423 | -46.31542 | 2025-04-18 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 89a06e88-b3e2-3f2e-8a23-3d69d53be127 | -12.21767 | -44.15723 | 2025-04-18 12:34:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7650a656-a3a1-3215-a618-281fc5719432 | -7.07942 | -44.37784 | 2025-04-18 12:34:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 42b8aee0-f388-3ab7-ba74-8b9a4666ec9a | -7.76103 | -46.74881 | 2025-04-18 12:34:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2e13c492-03b8-36c3-b6ca-5f71c9c0a857 | -12.21954 | -44.14236 | 2025-04-18 12:34:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 69b9dc09-3fd5-3f32-b482-c384afe565e7 | -6.7167 | -47.60182 | 2025-04-18 12:34:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2bf0f788-7ae0-3060-a148-d2e2d701dac0 | -7.69947 | -47.57404 | 2025-04-18 12:34:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a8ce50b8-85d5-3f3a-9f98-c3fad3d4a561 | -5.48756 | -43.3317 | 2025-04-18 12:34:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 357bada3-48c6-3cbe-9600-79e69fefc2a3 | -5.7951 | -43.61027 | 2025-04-18 12:34:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 03f2096d-6adb-37b2-b38d-56f56275d6f5 | -6.51224 | -44.03115 | 2025-04-18 12:34:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |


