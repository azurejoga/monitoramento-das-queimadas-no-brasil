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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82333b28-f904-35d4-ba77-8ea237ed8b90 | -7.19875 | -72.68004 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9419f0cd-4512-3177-a503-ddce6783d6ba | -11.88663 | -64.93061 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 15ed8634-2c68-3f98-921b-8a7bd2897962 | -9.12061 | -67.73272 | 2025-09-22 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1e44be4-b6e6-32d2-8b24-667dd01b3fcf | -7.6555 | -72.26263 | 2025-09-22 06:20:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e816370-be40-3b75-9e22-a06e3a89b2f1 | -7.24583 | -72.50967 | 2025-09-22 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7542289c-4c3a-3602-bd20-2c80986c44b4 | -8.73963 | -69.10713 | 2025-09-22 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dff022c1-4794-3f69-8f13-f03e90c08ad4 | -8.21145 | -70.47759 | 2025-09-22 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e09397d7-9ce5-3137-8efd-384a10e3e442 | -9.9139 | -65.04499 | 2025-09-22 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 644d2189-e91a-3123-a80e-d90df6b34ceb | -20.274 | -55.4927 | 2025-09-22 06:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a3ab1e75-2fd2-3ef7-818d-7f8e42481350 | -20.274 | -55.4927 | 2025-09-22 06:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 3d9b4026-8646-3fee-a9ab-17c94a59538d | -20.274 | -55.4927 | 2025-09-22 06:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 51e195e8-8492-3f71-9917-167559005922 | -20.274 | -55.4927 | 2025-09-22 07:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fdd018b8-bf87-39c2-b759-3a3a88e2b8e6 | -16.0163 | -59.4633 | 2025-09-22 07:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f03f0be5-a420-3a90-b85a-2e081e88b156 | -20.2537 | -55.4959 | 2025-09-22 07:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 03610d0c-a984-37ec-8776-e50528253a26 | -16.0163 | -59.4633 | 2025-09-22 07:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 70db8408-341f-3b13-8110-001e7fc415bd | -16.0163 | -59.4633 | 2025-09-22 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 65652b50-dbf0-352e-83b2-9468cd408877 | -15.8412 | -59.5199 | 2025-09-22 08:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 5e31c3ab-4cd6-3d5a-baaa-5e6df4c5ade0 | -16.0163 | -59.4633 | 2025-09-22 08:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 99ae4f72-e0b4-3ced-a754-13226e62290d | -22.9073 | -50.9001 | 2025-09-22 08:30:00 | GOES-19 | SERTANEJA | PARANÁ | Brasil | 4126405 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| 1e31cfb3-74c3-3e3a-8f06-60db57160f36 | -16.0163 | -59.4633 | 2025-09-22 08:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 9894afd5-a291-3ee5-9f5c-90782fbbe2dd | -15.8412 | -59.5199 | 2025-09-22 09:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 5e7cb92d-18b1-34cc-8f96-cb1c3e5f82fe | -13.3094 | -51.088 | 2025-09-22 10:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d0fbe29f-234e-373d-ac50-f63df55c8677 | -13.309 | -51.1095 | 2025-09-22 10:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 139.1 |
| d4042b59-dfc6-36c5-9daf-65c8a2b4d778 | -8.2803 | -44.3801 | 2025-09-22 10:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 28205c66-8688-30aa-b043-dfe61e1b19f8 | -8.28 | -44.4032 | 2025-09-22 10:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| f1f2ab21-4502-3de4-9b2c-843ee2a456c1 | -8.2614 | -44.3821 | 2025-09-22 10:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| eda49229-d5bc-3fb1-a292-1e170668e013 | -8.28 | -44.4032 | 2025-09-22 10:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 42ac6cbd-121f-3367-9f4e-b9e18c72bdae | -8.2803 | -44.3801 | 2025-09-22 10:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 261.0 |
| f6347bb1-0fcb-3cd4-9b49-5358a466f56e | -8.5185 | -44.9291 | 2025-09-22 11:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 161.8 |
| ea238c9f-465f-3545-ad8d-dcd9245610fa | -8.5185 | -44.9291 | 2025-09-22 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 4d96e28f-a6d8-3b48-b5f2-6e41d6721651 | -8.2803 | -44.3801 | 2025-09-22 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| cb0b9d69-4c2a-330a-8097-96d9d5ae70b1 | -8.2614 | -44.3821 | 2025-09-22 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 8f5265dc-e59c-3545-8e57-049ea363d2dd | -8.5185 | -44.9291 | 2025-09-22 11:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8fb73920-0532-388f-84f1-61d4c1263b38 | -8.2803 | -44.3801 | 2025-09-22 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 242.6 |
| d721a34c-9a30-31aa-a5e8-27fa99f616ea | -8.5185 | -44.9291 | 2025-09-22 11:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| a662d325-8ac5-37de-a7ac-c19ee36d375a | -8.2803 | -44.3801 | 2025-09-22 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 68d8a060-0c2f-33a5-a89d-9a79d7abd726 | -8.2803 | -44.3801 | 2025-09-22 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 629df430-bfce-30ce-8f84-4fde28b2e2a0 | -7.6195 | -44.4934 | 2025-09-22 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f2b53906-80a4-3978-9778-bcd27c6a7e0d | -8.5185 | -44.9291 | 2025-09-22 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 0b9eee7b-ef87-3050-8d15-d67fa2dd3a09 | -7.6195 | -44.4934 | 2025-09-22 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a2890bd6-92ea-3fa7-a06e-d2aefed11cdd | -8.2803 | -44.3801 | 2025-09-22 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 0655b49c-b519-31ae-b550-10a4e038ba2a | -8.5185 | -44.9291 | 2025-09-22 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| f793c445-2e8a-3a5c-a045-f178c8de4e3a | -8.2803 | -44.3801 | 2025-09-22 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 391680cf-6b92-33c9-807e-07fc37b1db7b | -14.9895 | -44.4022 | 2025-09-22 12:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| aad0db6d-71c9-3607-9793-4ef3aae3d919 | -8.5185 | -44.9291 | 2025-09-22 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 500fedb6-3efc-3fd0-8c61-f3183111eb54 | -12.4353 | -45.1515 | 2025-09-22 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 56bba459-b538-3a1f-a57d-08e794e8cbd7 | -12.9889 | -46.3957 | 2025-09-22 12:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 195b3b27-2315-3d20-a851-8a791430c90a | -12.455 | -45.1254 | 2025-09-22 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4e083424-3d20-3894-b858-b7e985b1b7d4 | -12.4545 | -45.1486 | 2025-09-22 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| deae0bb2-a503-3687-a5cf-a17c8be4598f | -12.4554 | -45.1022 | 2025-09-22 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3f0330dd-d235-31e6-9cf0-4d5c25e389ff | -14.9895 | -44.4022 | 2025-09-22 12:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| ed3eb623-e7f7-34af-b433-269d7a8c9b88 | -12.9893 | -46.3729 | 2025-09-22 12:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 3f78b636-7555-3d4e-b285-48504d475d31 | -12.4357 | -45.1284 | 2025-09-22 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ea859bb7-081c-303e-ac38-b8e0a2756ea7 | -8.5185 | -44.9291 | 2025-09-22 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 03d1f904-9a5e-3157-906b-2bfc1b824b43 | -8.2803 | -44.3801 | 2025-09-22 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 34c2896e-e871-37e7-87f3-9fa40a8349c7 | -0.95075 | -47.35727 | 2025-09-22 12:34:00 | TERRA_M-T | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 26320aef-86a2-3475-9f61-bfe664021245 | 1.4334 | -50.76023 | 2025-09-22 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 97cf0e7a-0532-312b-bdb3-64297d5a49c0 | -3.29616 | -43.52382 | 2025-09-22 12:34:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 58586808-011a-39d2-9e71-510ae6a60400 | -0.95032 | -47.35125 | 2025-09-22 12:34:00 | TERRA_M-T | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 59800127-8d71-3400-ba59-38665b4fc5fe | 1.42321 | -50.75253 | 2025-09-22 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2f96532f-8734-3ec9-9634-854e6e879d69 | 0.95563 | -51.22272 | 2025-09-22 12:34:00 | TERRA_M-T | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3be9f441-b279-31ea-a8ec-922af6fd2c4f | 1.42449 | -50.76146 | 2025-09-22 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 9eccfdf7-3147-3d78-a37a-64982d6d574e | -0.9523 | -47.3461 | 2025-09-22 12:34:00 | TERRA_M-T | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4c8161c1-8f0d-3ed8-a7dc-c723b2c9db28 | -3.40507 | -47.50298 | 2025-09-22 12:34:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 095db61d-ed5b-3e9d-a1ee-1e9c6a48d7dc | 1.42578 | -50.7704 | 2025-09-22 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 35.2 |
| f4ff7dde-116a-334f-963c-dce791965906 | -5.09489 | -42.7075 | 2025-09-22 12:34:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 4f61d744-ac6f-383e-aad2-71f3acbc1958 | -5.10741 | -42.7141 | 2025-09-22 12:34:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 3e9f350d-9cb1-320e-961d-c668d33a72b2 | -3.08792 | -52.92288 | 2025-09-22 12:34:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f243d82d-3e28-3ef6-9bb0-4a6e76663fb4 | -4.42034 | -48.78049 | 2025-09-22 12:34:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f9c9ab73-8a13-3543-b665-8e251e230dbb | -4.31381 | -48.09192 | 2025-09-22 12:34:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0463071c-6389-39d0-9714-9a44b6b4fb2f | -11.23009 | -49.60288 | 2025-09-22 12:36:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 19b29aef-202f-342c-b5ca-3bfacf00cd08 | -10.45894 | -53.59891 | 2025-09-22 12:36:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c0bec727-fe85-30ae-9791-004674590290 | -8.53631 | -44.91314 | 2025-09-22 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.1 |
| c6b312cc-c1ef-3f1c-92d5-b0c775658749 | -11.73884 | -54.23943 | 2025-09-22 12:36:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 71186768-cb37-3be7-a8d2-183611bf470b | -7.82498 | -46.18261 | 2025-09-22 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 615ff6bf-8afd-3a28-8141-7205a4e2b555 | -11.64665 | -52.85533 | 2025-09-22 12:36:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1599fa78-2836-32a2-b86d-ebe421f4152b | -12.08266 | -44.77905 | 2025-09-22 12:36:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1c40e153-cb0f-3ce9-85ca-c04b73fd12bd | -6.47046 | -45.6651 | 2025-09-22 12:36:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c71f45c4-3757-333a-b2c5-79c66727b376 | -8.59067 | -44.31087 | 2025-09-22 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| cbb32705-7e80-399a-8c29-70bc0f0edd1e | -7.81738 | -46.18862 | 2025-09-22 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 9fccc2a8-4921-3af1-adc4-eb1d8e7bc99e | -6.45809 | -45.66382 | 2025-09-22 12:36:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 991571cc-933d-351f-89a5-db1342ccbfbd | -8.27654 | -44.40559 | 2025-09-22 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| df15502f-bdaa-3baf-a76c-28ddf4161391 | -8.46418 | -44.75859 | 2025-09-22 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| cb65f6d0-8312-3467-b1a1-94d6634c2e08 | -11.07712 | -50.74818 | 2025-09-22 12:36:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| bc28109d-40a9-3223-a689-26742e4f32dc | -11.44347 | -48.53262 | 2025-09-22 12:36:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 67fbe5a8-e319-3e98-8548-11346a5959e0 | -8.59387 | -44.31792 | 2025-09-22 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 3d24be73-da97-3842-b452-82023066d180 | -11.6391 | -52.84507 | 2025-09-22 12:36:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| c53a1f50-7bc5-3c6a-8b33-d4dab9c701d9 | -8.51993 | -44.93467 | 2025-09-22 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a9acd4e6-57c3-3f6f-98b7-c6e69a4e73d9 | -6.45573 | -45.68187 | 2025-09-22 12:36:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 1f7ca781-8567-3ba4-928f-e33991d5ac27 | -11.13742 | -53.94038 | 2025-09-22 12:36:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f27dcc6f-eeba-3449-bacb-818dba829c4f | -6.62246 | -44.60839 | 2025-09-22 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0c8697d8-cad1-34ac-83a1-62a3c8141ec5 | -5.80603 | -49.33512 | 2025-09-22 12:36:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 83216de6-401a-308a-8d0b-e6ed9977021f | -11.4653 | -51.47316 | 2025-09-22 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b1ccb3ea-ab6c-38a5-84ea-76946cebb09b | -9.89834 | -52.44173 | 2025-09-22 12:36:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fe604847-0727-3f31-b2d2-42972c4486b3 | -11.12762 | -54.13283 | 2025-09-22 12:36:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 41fa3d75-1b39-3c2d-b0e5-5899da96cc5b | -3.95277 | -53.38379 | 2025-09-22 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c6c00310-913f-37c2-921d-bcb1c067fbdd | -10.03651 | -49.35722 | 2025-09-22 12:36:00 | TERRA_M-T | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 30f6693e-c80e-35e7-9bfe-1ea6ccf4a58e | -8.526 | -44.92822 | 2025-09-22 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 4b3afb84-4dd7-3823-aa08-90b502c1498f | -7.6078 | -44.42514 | 2025-09-22 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f684a125-9a51-3f59-a06e-0c16f7bf4ad0 | -11.64535 | -52.8643 | 2025-09-22 12:36:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |


[Clique aqui para ver as próximas entradas](README44.md)
