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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1eb4e15-4f92-30a9-872c-3d11870dc369 | -11.75839 | -43.32478 | 2025-12-19 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c90230c-c2f3-32b8-b5d3-374df6a1a15f | -11.07403 | -41.95412 | 2025-12-19 04:40:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 612beaa4-4ed3-31b8-846c-6a016ef9937c | -11.07362 | -41.95721 | 2025-12-19 04:40:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a26d970d-5097-3c4a-941d-020f19d2874a | -10.95799 | -44.88309 | 2025-12-19 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e166495-32fe-3e6f-ab64-686bd7e2211b | -10.4741 | -36.98441 | 2025-12-19 04:40:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ef97abfd-562a-3fc5-8bf1-d501500e1b88 | -10.49513 | -44.92576 | 2025-12-19 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 057099f4-0318-3a60-8d01-a5bfe03eac07 | -4.67521 | -50.71085 | 2025-12-19 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 357f6a0f-11f1-376d-9a5e-cca3a38b7f48 | -13.37733 | -41.34706 | 2025-12-19 04:40:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4fcfe66d-3c6b-361d-b24d-9cd5334cd583 | -11.75679 | -43.32248 | 2025-12-19 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f4253b90-8547-38b6-8426-5e7a2f081b05 | -11.8516 | -43.73176 | 2025-12-19 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f58acc2c-da97-34ce-96e8-af318813bc29 | -13.39317 | -41.87593 | 2025-12-19 04:40:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0a8e1f0a-ea94-3332-9e75-818f10204d4b | -10.48103 | -36.98553 | 2025-12-19 04:40:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 197d1daa-ead0-39a7-9c25-fdf24875f420 | -11.9096 | -43.82211 | 2025-12-19 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5cf98971-2e35-3562-bc60-f28ad2851131 | -10.48034 | -36.99149 | 2025-12-19 04:40:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a96fd962-0882-3c16-a0ef-ed9a60de05fa | -11.75903 | -43.31969 | 2025-12-19 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae7dff45-f490-30df-a1c7-c69a199b5035 | -15.89951 | -43.03565 | 2025-12-19 04:42:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 127eb8d2-d805-3853-bef7-989cdf00c8e7 | -13.94376 | -44.35312 | 2025-12-19 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7be217cd-3eda-3803-b164-ebb88102cdde | -15.89987 | -43.03254 | 2025-12-19 04:42:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77c6d05b-2488-35a1-ac5b-f0dfd0cfb1c7 | -18.98256 | -55.30169 | 2025-12-19 04:44:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 49db398b-1c45-314e-8b11-a93bd5999fc7 | -20.20229 | -54.76268 | 2025-12-19 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc9479fa-939c-3390-af48-2435c282ba7c | -21.00385 | -54.47353 | 2025-12-19 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03c08fd7-c448-3cbd-ac76-d658689c2a50 | -21.53957 | -57.51852 | 2025-12-19 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c577b08e-472c-3fc8-b124-d6e65d0531a3 | -19.56178 | -50.99226 | 2025-12-19 04:44:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| f364ff0c-ec16-37fb-b0ba-6e55297c5688 | -19.81826 | -54.74611 | 2025-12-19 04:44:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc03a44f-12d3-3a4f-b154-68af9ec96270 | -21.53829 | -57.52036 | 2025-12-19 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8c8ee70-48b2-3339-a69c-db6609cec9f4 | -21.29285 | -48.99523 | 2025-12-19 04:44:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4f9951c-3401-31e7-a164-03c8f2e5d328 | -23.06267 | -51.51328 | 2025-12-19 04:44:00 | NOAA-21 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4efdcc7-e9d4-3442-b027-d1474e6bd3de | -20.56182 | -54.65462 | 2025-12-19 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ad9a796-116d-38eb-82d1-513c46185340 | -23.74435 | -55.39473 | 2025-12-19 04:44:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c7d8c1d5-c117-3dfd-a95e-79250c556c57 | -32.34601 | -52.36662 | 2025-12-19 04:46:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 0c2afe87-f540-31eb-877a-cf95f74fe7c2 | -28.88789 | -50.47155 | 2025-12-19 04:46:00 | NOAA-21 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d6ff53c6-1922-37fe-b5b9-7ff6f6c25275 | -26.8471 | -50.7077 | 2025-12-19 04:46:00 | NOAA-21 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5e0856ee-c548-3827-a696-fe64ba37250f | -27.98343 | -49.06167 | 2025-12-19 04:46:00 | NOAA-21 | ANITÁPOLIS | SANTA CATARINA | Brasil | 4201109 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4fe71be4-38bd-3bfd-adc7-c373f676d8df | -31.10617 | -53.43868 | 2025-12-19 04:46:00 | NOAA-21 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 975855b9-dd35-3c8a-9c42-d54755d640a6 | -28.89105 | -50.4773 | 2025-12-19 04:46:00 | NOAA-21 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c2c02313-5c80-3a19-8476-7db1a0eab03c | -28.65911 | -49.29457 | 2025-12-19 04:46:00 | NOAA-21 | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c23e210-e9f0-3c00-a2d5-922dd9ffe6f1 | -29.7289 | -53.87328 | 2025-12-19 04:46:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 8c666ea7-2ce2-3701-868d-6a7b07fbdab8 | 3.80046 | -60.48938 | 2025-12-19 05:05:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7906204-6d77-3cc2-aea1-fe782ac3cea2 | 3.90412 | -60.15571 | 2025-12-19 05:05:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8993d3bd-12b2-3950-ac95-c54868dc6ed3 | 3.22541 | -61.19214 | 2025-12-19 05:05:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcc45f4a-d3b5-3d15-bb0f-7ccaec3d4549 | 3.90869 | -60.15549 | 2025-12-19 05:05:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0031c555-3459-3167-9861-c1cf31db4d8a | 3.18253 | -60.60908 | 2025-12-19 05:05:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ed4986a-7ef9-33d1-aaee-d0e0ecf547e7 | 3.80506 | -60.48868 | 2025-12-19 05:05:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7b12db3-eaf5-3404-acd0-2b5974c7f1db | -2.8271 | -51.27972 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7ba72b5-ce4a-31de-8f5a-a855b0c795f2 | -2.82674 | -51.28131 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd008ec0-67c1-3d64-bff2-2956abde9826 | -2.67357 | -51.70505 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be667818-a441-3591-8e92-211712e2f56c | -0.6469 | -52.38631 | 2025-12-19 05:08:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4a86a69-3455-396d-b6c6-92a2d9a29581 | -2.39854 | -50.31457 | 2025-12-19 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf0aee0b-3e54-3c56-bd47-37232f656212 | -2.70741 | -51.89555 | 2025-12-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f8366c5-5723-3b9c-a2a9-51ab8994a917 | -2.69742 | -51.64755 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9467787f-465f-3023-bcb1-04487b25fc07 | -1.28891 | -53.05313 | 2025-12-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe8709fb-5403-3603-9067-25fedab571e4 | -2.88947 | -50.23205 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e53c2e52-1db2-33e8-85ff-ac4a7c515350 | -2.72713 | -51.62577 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fcb4a021-03e3-3434-88e3-1da962006439 | -2.65128 | -51.72943 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 762cce37-8a36-3d25-9da9-30c4427befac | -2.10891 | -50.91213 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4ac6c7e-5027-3855-a79e-653383b8f2b9 | -2.90177 | -49.79603 | 2025-12-19 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40bfd738-11db-3042-9acd-972d341f9241 | -3.20267 | -51.2701 | 2025-12-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47c5156b-6e1d-3945-b143-d8a568d4bd12 | -1.29174 | -53.05732 | 2025-12-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd2aee87-1f29-3ae3-94e6-960f0ad4060c | -3.27534 | -51.57239 | 2025-12-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1186e33c-3851-3fb4-9e36-1b0690ae5da8 | -2.45116 | -51.98598 | 2025-12-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 999a425b-7f9f-33b7-8e8f-52273ac269e9 | -0.98572 | -52.33927 | 2025-12-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 377b8faa-4128-376a-b1ec-5fa1d017f069 | -2.74471 | -48.38337 | 2025-12-19 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4612b18-3bcd-3ffb-b170-05ee99802e8e | -2.79145 | -51.40812 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36eae3f7-0390-3217-aa3d-9050f60df06a | -2.23189 | -51.93419 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5026023-0184-3021-9cf9-53f299215ca0 | -2.67998 | -51.73645 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db282ebe-32f7-32c1-bfbc-2825a60a6273 | -3.15497 | -51.10521 | 2025-12-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a597c0d-0318-3402-8a00-0d6ebecfc1d0 | -3.02144 | -51.19591 | 2025-12-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3ec126a-32e6-3e6b-b181-3bc14cace2b9 | -2.69374 | -51.647 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3905dc87-48f8-30e0-822c-7ec80362552f | -3.02215 | -51.19137 | 2025-12-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9042a989-3ea6-3b17-b05b-92562817435f | -2.7308 | -51.62634 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d464eb83-d09e-3e00-a46c-64c690d495c0 | -2.79075 | -51.41256 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee2009a6-c95f-321f-8aec-e167cd469087 | -2.86044 | -51.58316 | 2025-12-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ececc43e-7121-30db-8e90-84dcdc430704 | -3.18738 | -50.23152 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59d1ef98-3d74-3913-85c5-f830e8114b52 | -2.44756 | -51.98542 | 2025-12-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2fb1297b-ac39-310c-97cf-2a6e2fa9a336 | -1.28833 | -53.05678 | 2025-12-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e380d0ec-2cc2-3be0-aca2-c78759e967db | -2.10964 | -50.90753 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f31597ea-389c-3e30-8e7f-bb555f0ea492 | -2.82745 | -51.27681 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23163be3-4b7e-33a0-baf3-20f76f267cc1 | -2.97661 | -51.58131 | 2025-12-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5b0fdd2-1ba4-3bcb-a40e-fd182f171c56 | -3.5194 | -50.87244 | 2025-12-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d113bbde-fa73-31af-9d3d-3fdf07359a77 | -2.74926 | -48.384 | 2025-12-19 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a9440ef-25eb-3e9f-aabe-2d512b7d9ef3 | -2.70378 | -51.89501 | 2025-12-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b83a7c41-8a27-3c8d-a4e3-6c9f2dcb188a | -2.4504 | -50.25767 | 2025-12-19 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e82092ab-d5d9-3e2b-a7be-7cefd6a32547 | -1.29231 | -53.05367 | 2025-12-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec55d0ce-1e11-3630-bc52-660040a29ce6 | -2.69808 | -51.64327 | 2025-12-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d159df4c-d8ee-3e8a-8a2e-8abe7127c2fa | -3.15879 | -51.10579 | 2025-12-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5bf38d2-50d5-3503-91d3-7af4963a7065 | -2.90589 | -49.79668 | 2025-12-19 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d889610f-750f-32dc-80ce-0e1e5d089b64 | -10.49883 | -44.93142 | 2025-12-19 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b03ef26-bf9d-330a-b93a-80213eeb41ba | -13.94154 | -44.3511 | 2025-12-19 05:10:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a4eef28-fc3e-3a15-8565-5a57dc9d286e | -10.49945 | -44.92622 | 2025-12-19 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9a4fa3e-e9ea-3bff-819f-0b035f372bf4 | -18.83902 | -51.62921 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8b80e4f0-2176-337d-a93a-cedea0d1bcf1 | -18.83162 | -51.61291 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b123367d-7712-3c0b-b459-57215289be24 | -18.82702 | -51.61233 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b041225-eb5c-3b81-963f-c7730a068fdb | -18.84361 | -51.62986 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 179b2d2f-cf9a-31d2-99db-9e40ba626ff7 | -18.83563 | -51.61852 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 934032fa-1b76-3832-80f0-376429c0a73e | -19.56228 | -50.99116 | 2025-12-19 05:12:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| cbc22d21-f406-37af-a829-861db4e61088 | -18.83503 | -51.62355 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3d332873-9190-35fe-9ed8-732280da8342 | -18.83443 | -51.62856 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bb49d6aa-1b45-3833-971b-28eeb000db13 | -18.83103 | -51.61792 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b66bace7-7b67-3e8f-8a98-bb66a17bf38e | -18.83962 | -51.62417 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2d59eb38-5e23-364e-a542-3ae1274044a4 | -19.55745 | -50.99045 | 2025-12-19 05:12:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |


[Clique aqui para ver as próximas entradas](README6.md)
