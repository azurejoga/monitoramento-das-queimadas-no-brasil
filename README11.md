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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a17d2fb-055b-3033-9d39-ba00279ddc20 | -18.59886 | -51.72503 | 2025-10-22 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ddcf788-faba-3a2c-9db2-caa06f89d46c | -19.0565 | -57.49181 | 2025-10-22 04:29:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1ed4a796-e530-3ade-84be-695c0e9b5f14 | -18.1479 | -52.98359 | 2025-10-22 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b8238e09-2646-31f4-9dad-72d5768ec77c | -18.94757 | -55.07784 | 2025-10-22 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| eb26d1da-05bc-3995-8631-3c44cf24f0d9 | -17.40017 | -55.08491 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bd2db5e2-d53f-30fb-b99a-c00f1686628b | -18.16993 | -52.96827 | 2025-10-22 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fede4596-a9c3-37c1-a97e-73c8fd29b39f | -18.16536 | -52.9723 | 2025-10-22 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29277466-aba0-3a55-92e3-5dedadb87be8 | -20.56619 | -45.89196 | 2025-10-22 04:29:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36b2b1c1-ad34-3d9d-9800-33f74822b82b | -22.12557 | -47.02672 | 2025-10-22 04:29:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfd7e585-3e04-3c9a-9dc3-df7cfb3ad716 | -19.09065 | -57.52309 | 2025-10-22 04:29:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cbd8e338-1cdc-3138-a86d-d7631672f34b | -18.62538 | -51.65434 | 2025-10-22 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21967fb9-ac7b-3aaf-a03b-7ee32c9aff33 | -19.48985 | -54.93085 | 2025-10-22 04:29:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03314c1d-1508-32cc-885d-194af39a83d1 | -19.94218 | -46.08906 | 2025-10-22 04:29:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be883ba6-1a54-3f8e-9427-c92e938bb894 | -22.1158 | -53.04034 | 2025-10-22 04:29:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 333f4857-f5ce-3cf9-a681-e2098f5b0a08 | -19.0625 | -57.48717 | 2025-10-22 04:29:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| cf891e97-673a-37ec-a9ad-875aee4906d3 | -19.96277 | -44.68905 | 2025-10-22 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b53b3ae4-0d69-3986-84a4-dbd754e9d053 | -17.41888 | -55.07988 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f39ba2ff-6a06-3309-aebf-1f8f3d20ef91 | -18.2051 | -52.96548 | 2025-10-22 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8a4714ef-095d-3679-aebd-26a6a5c7edff | -22.3829 | -46.91319 | 2025-10-22 04:29:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a8ef64a-9160-3891-aa0b-4a7298f44c4d | -20.97597 | -47.21307 | 2025-10-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6c68177-bd31-39c1-ac62-5bd3b00c29d1 | -17.6732 | -54.21732 | 2025-10-22 04:29:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ca4e886-6d85-3440-83e4-c2e62cb27f8a | -18.6498 | -49.09342 | 2025-10-22 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 201d17ae-1d1d-3a12-8ece-eaafb98234a6 | -18.11643 | -54.52278 | 2025-10-22 04:29:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| feb26aa4-0c02-32e4-b226-a7d018794730 | -17.41693 | -55.07948 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0a409bc2-fe33-3918-99ed-ea27c69d6e50 | -17.40445 | -55.08578 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f020bd40-7a1c-3010-9487-139ed32d3cde | -17.40873 | -55.08665 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 88a09d2c-11cd-39e2-930e-109ed36cfb86 | -19.15523 | -49.12426 | 2025-10-22 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 417490d8-12b5-3715-a9be-5ed83d52920a | -20.95323 | -46.63197 | 2025-10-22 04:29:00 | NOAA-21 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f7d535e5-f51f-390e-b863-9484c108929b | -21.90137 | -50.67148 | 2025-10-22 04:29:00 | NOAA-21 | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ce20fe7e-f0ce-3b40-86ef-16f0972e7925 | -18.11563 | -48.52745 | 2025-10-22 04:29:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 05f036a8-7c31-3694-9ace-8f5c4c6bf93c | -20.98058 | -47.20556 | 2025-10-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 094fb798-eb2b-31ba-a62d-e57dd3bc3efc | -21.24659 | -45.14059 | 2025-10-22 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 22b93942-49a9-3bb2-a148-432319d3201a | -19.08794 | -44.34481 | 2025-10-22 04:29:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e49b18ee-e0bd-35b3-869d-db5f14fff427 | -22.12135 | -51.18205 | 2025-10-22 04:29:00 | NOAA-21 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fd0effc0-c513-359e-84c4-6b0b1187e799 | -19.08581 | -57.522 | 2025-10-22 04:29:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 044d8f11-03f7-390b-9595-6e1b34a745d6 | -20.27878 | -45.14264 | 2025-10-22 04:29:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c0786430-cfed-3131-87d7-24dba930de28 | -22.37876 | -46.91693 | 2025-10-22 04:29:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38b873cb-3270-3061-934d-ab30a08c98e7 | -18.34103 | -49.4975 | 2025-10-22 04:29:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 53b234f2-0283-3f0c-afe6-2aa457f224be | -21.96307 | -42.93368 | 2025-10-22 04:29:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 19d6640d-5c95-33d6-8da6-f95fc019bb30 | -20.44375 | -44.85672 | 2025-10-22 04:29:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3da3f77f-dd14-3c96-ac88-efb3c38d1a51 | -17.40755 | -55.082 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a661a086-11b1-3233-af96-ce96903dc4fd | -19.29461 | -45.75298 | 2025-10-22 04:29:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2800930-9d81-34a3-9a66-ad5c36ad0eca | -18.94731 | -55.07421 | 2025-10-22 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| a848df9d-2f15-32cd-8225-616303d17f3b | -19.75137 | -47.90884 | 2025-10-22 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 939d5f9e-c882-3c25-b768-6b5e1ba72ceb | -18.67655 | -49.09768 | 2025-10-22 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3e7c635-e3c6-3286-bab3-946f7fa739b8 | -20.45393 | -54.68097 | 2025-10-22 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb72b338-2b38-3c5c-8c1a-0a432e8a7817 | -21.41014 | -44.27426 | 2025-10-22 04:29:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1510bb03-bc6d-31fa-b740-e1f0c950c4b0 | -18.15332 | -52.97488 | 2025-10-22 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a3f1638-6b39-3688-a08f-eb6c7c331464 | -19.90979 | -46.11088 | 2025-10-22 04:29:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| af211077-963c-33fa-a64e-415eb110c232 | -18.14875 | -52.97888 | 2025-10-22 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 446a1d5f-b6b2-3d86-9a00-846097ff305f | -18.94655 | -55.0783 | 2025-10-22 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 2e8c0a27-4d6f-374b-ba2a-72079ff2f332 | -20.42488 | -55.74012 | 2025-10-22 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54c6c211-6a9c-3389-b723-3dbc0b154851 | -17.14788 | -54.60938 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37e77f6f-18be-3514-a500-2d135997f76f | -19.86106 | -48.69344 | 2025-10-22 04:29:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5de06e1-aa6b-3279-a5f8-489614aa838b | -18.62886 | -51.65501 | 2025-10-22 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f1eb98d-a7a6-395d-8afb-755fde948f76 | -20.14445 | -52.83725 | 2025-10-22 04:29:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f046b70-9c77-3f48-b5e8-3d1ed9f64fa2 | -20.56985 | -45.89248 | 2025-10-22 04:29:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 808c2e92-206a-3705-a241-0f20ed256ec2 | -4.4632 | -43.2386 | 2025-10-22 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 80ef1141-5476-36c6-8ce1-0991a1eba000 | -9.0036 | -65.9226 | 2025-10-22 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ee9f6e60-ed9a-3f8c-89e1-32749904e734 | -4.4445 | -43.2397 | 2025-10-22 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 72019fe8-d20e-3045-b3d4-e99cb3a00420 | -4.4446 | -43.2164 | 2025-10-22 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f6962d1b-03c0-30c1-8242-2379be8cffbc | -29.65333 | -53.92533 | 2025-10-22 04:32:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 9e010225-57fe-3398-8896-e3750c4813ee | -25.04213 | -51.02054 | 2025-10-22 04:32:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9490e30c-1f2b-3933-a0a8-6af1339eb61e | -24.98433 | -51.52816 | 2025-10-22 04:32:00 | NOAA-21 | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b0009029-823c-36ad-83f1-05242a3d5612 | -29.65331 | -53.92469 | 2025-10-22 04:32:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| 0f0473eb-c6c0-3deb-9650-c9e5d0b36fef | -24.35471 | -51.93536 | 2025-10-22 04:32:00 | NOAA-21 | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1d43b7ae-2ff4-3be2-897d-d6c9b6848c2c | -24.98765 | -51.5288 | 2025-10-22 04:32:00 | NOAA-21 | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ae03cf26-dbbd-3fb7-9b5b-b7ac3644b3ed | -29.72168 | -50.00307 | 2025-10-22 04:32:00 | NOAA-21 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d0712ced-0f5e-3b23-9d21-f3e568187f43 | -25.00927 | -50.86262 | 2025-10-22 04:32:00 | NOAA-21 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 34da0595-0f1a-335b-a8d2-adb0a898b421 | -32.02385 | -52.28226 | 2025-10-22 04:34:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 4050674f-dfd4-3dd2-92c7-29f974abef87 | -4.4632 | -43.2386 | 2025-10-22 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 1dfde81f-9ca1-390d-8626-1e3deaf69ee3 | -4.4445 | -43.2397 | 2025-10-22 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 2f3d106d-bba7-36f3-9f24-4e68c15cedd5 | -9.0036 | -65.9226 | 2025-10-22 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b67e9ea5-199e-3d11-8527-34cb9cdcb60a | -4.4446 | -43.2164 | 2025-10-22 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 335b7fa5-3372-3ed4-a1d4-dbba7193c710 | -4.4446 | -43.2164 | 2025-10-22 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e7926e3d-2d1a-3d93-88fe-22bc45731d3a | -4.4632 | -43.2386 | 2025-10-22 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 192f834e-78d3-366e-bf46-7911febc9122 | -9.0036 | -65.9226 | 2025-10-22 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| bef40abc-d522-3b75-aede-1fd30eae3ba3 | -4.4445 | -43.2397 | 2025-10-22 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| c9011ce1-0441-3c6b-ace5-2160a8342fee | 1.67528 | -55.72752 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fc02abe-0ef3-3272-acf4-57ef71f393ac | 2.284 | -51.62963 | 2025-10-22 04:51:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bc58966-c8e0-3aa3-b1cd-de49250fb191 | 1.67874 | -55.72341 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4244ea57-6fff-3e3f-a38d-e947a4f1ce0b | 1.35051 | -50.89919 | 2025-10-22 04:51:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce9195cd-6bb4-3b05-a86d-c397ee6e6082 | 1.67636 | -55.73444 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a856fe62-1d90-38fe-bb79-f591d6c47d0f | 1.5328 | -56.06086 | 2025-10-22 04:51:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58366983-8874-3287-a89a-249a4af58624 | 4.29052 | -60.72923 | 2025-10-22 04:51:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87125c25-7818-32b6-abc5-75f6093c83b6 | 1.52871 | -56.06149 | 2025-10-22 04:51:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd5f0be2-0fff-359b-ad21-f878c7c2b9d2 | 1.67343 | -55.742 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d61d56e8-1535-3db5-841a-0ac44b502b42 | 1.67289 | -55.73853 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4424144-8ec9-381a-8a7f-8ddd95d48181 | 1.67398 | -55.74549 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a650cf42-f1c8-3e61-808b-a4e7692c335c | 0.59727 | -51.57165 | 2025-10-22 04:51:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 784d6f15-bb57-39ae-84e1-206eb3783144 | 1.69661 | -55.70642 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44b21f09-e4b2-3d11-b4a0-a87b6f0322f1 | 1.67929 | -55.72688 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb0733ad-b6a5-3251-92f7-02f6b1af36d0 | 1.69369 | -55.71393 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cb179a5-b044-3917-b357-13d1085f40c9 | 1.35383 | -50.89867 | 2025-10-22 04:51:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fa3f167-fe1d-3890-bdb0-daa261f430a2 | 1.67582 | -55.73098 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07074b7f-1964-3eed-8afb-3932bc408349 | 1.69314 | -55.71048 | 2025-10-22 04:51:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adac6d25-8864-37a1-ab17-64fbd9ad8996 | -3.02809 | -49.45594 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d15e890-4673-3e57-9a39-6036a2383c3b | -3.5648 | -49.4823 | 2025-10-22 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46bf0513-5775-3b58-9ab9-16ecd1fd9349 | -4.3166 | -48.08831 | 2025-10-22 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e13b34f-2e80-34fc-a2a4-32766037ef19 | -4.11008 | -48.02752 | 2025-10-22 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README12.md)
