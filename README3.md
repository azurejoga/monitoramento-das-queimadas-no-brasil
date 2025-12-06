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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b72a46ad-4610-3333-bba2-510ccc5f9d64 | -9.33602 | -36.96737 | 2025-12-06 03:44:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a51b3e39-858a-38bd-88b7-b1c579b2d71d | -10.07218 | -36.55454 | 2025-12-06 03:44:00 | NOAA-21 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 690ef35c-5820-3620-bf9c-5151d4350d20 | -10.26257 | -37.86348 | 2025-12-06 03:44:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8536e96-878b-3869-a877-a85419fc1da2 | -22.77942 | -43.04381 | 2025-12-06 03:46:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 40711d38-6d6b-344e-bd33-ddd12bb89eb6 | -22.07951 | -46.82085 | 2025-12-06 03:46:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25bdef14-4b57-3777-8db6-0afcfe87998d | -22.75168 | -42.00491 | 2025-12-06 03:46:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66e20c53-5f91-3895-bb17-05181c65b95e | -22.74815 | -42.00419 | 2025-12-06 03:46:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c7216c1f-12f2-3715-b3c0-bf86b95439b4 | -22.42804 | -48.56054 | 2025-12-06 03:46:00 | NOAA-21 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 10f3dade-3d68-3222-8a32-640bebec5a24 | -22.78149 | -43.04252 | 2025-12-06 03:46:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 923c3fba-e1ee-3cd3-91ee-56a6bb005999 | -19.31939 | -41.59962 | 2025-12-06 03:46:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7aa831df-da8b-3b48-8532-8f6235c7337b | -20.32989 | -50.19204 | 2025-12-06 03:46:00 | NOAA-21 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| da3ecc07-a5ae-347c-9396-7c297d360579 | -22.90067 | -46.2283 | 2025-12-06 03:46:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f4e2dc0-99f1-38d9-b392-94ccd9c62b37 | -22.78312 | -43.04458 | 2025-12-06 03:46:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7abd58fc-b0cc-3b21-9513-137dd2c6d060 | -21.50557 | -44.69688 | 2025-12-06 03:46:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc8e0e50-ced7-3823-b873-6eebc02721fa | -20.32287 | -50.19535 | 2025-12-06 03:46:00 | NOAA-21 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0103070e-85fe-379b-b433-f930a3bc7ee7 | -22.42729 | -48.56401 | 2025-12-06 03:46:00 | NOAA-21 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 622a183b-f4d4-36f2-b71e-b0cba442ecb6 | -19.88083 | -44.05172 | 2025-12-06 03:46:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5d606edb-84f9-3515-a873-952ffb2c0809 | -22.75156 | -42.00328 | 2025-12-06 03:46:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e62bbc90-20f3-3174-b6c6-ffeea7a97b42 | -22.9027 | -47.18927 | 2025-12-06 03:46:00 | NOAA-21 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 33ad0514-bac2-3f7c-b5df-f3d083191c69 | -21.5489 | -44.30121 | 2025-12-06 03:46:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ed198202-8296-3ac1-9acd-d4aba9216637 | -24.16835 | -49.5776 | 2025-12-06 03:49:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b4f4807a-3f77-35db-bbcc-034000130e8d | -25.33731 | -49.88223 | 2025-12-06 03:49:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fbe61348-5ad9-3474-8ef0-bdb47873a0ea | -27.31337 | -50.55787 | 2025-12-06 03:49:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 183839c7-7b40-305f-b121-72d8ff784504 | -22.98924 | -47.13456 | 2025-12-06 03:49:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a936ae4a-3adf-3463-a989-563db09c3711 | -26.41303 | -51.84061 | 2025-12-06 03:49:00 | NOAA-21 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| abdbcca2-1d9b-3323-87da-1f17b4080915 | -25.32941 | -49.87416 | 2025-12-06 03:49:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2daa272e-b7ac-3da2-a771-47096af51814 | -27.31424 | -50.55415 | 2025-12-06 03:49:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 9529c99e-045a-302c-b581-e8895d333aed | -24.16389 | -49.57261 | 2025-12-06 03:49:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac7db777-3aeb-374f-abdf-160b463bb87c | -25.33297 | -49.87696 | 2025-12-06 03:49:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6e729abc-282a-39b6-a732-f3340b2f7196 | -25.33378 | -49.87941 | 2025-12-06 03:49:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 37526871-01e9-3126-85ad-43079d2b10f7 | -26.91351 | -48.77749 | 2025-12-06 03:49:00 | NOAA-21 | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f5746a83-5d05-39fa-9600-831d680e9302 | -24.16753 | -49.58127 | 2025-12-06 03:49:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04b1ef0f-6074-300d-86de-14509ccfa805 | -26.41233 | -51.84279 | 2025-12-06 03:49:00 | NOAA-21 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e63ca680-a210-3e5e-a535-ab0641591ce7 | -26.41196 | -51.84504 | 2025-12-06 03:49:00 | NOAA-21 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c69d3071-0b50-3e1b-9cb0-3611bb6f828e | -27.31251 | -50.56155 | 2025-12-06 03:49:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 9fa15622-a70f-308e-a4f9-aa8ad929d71f | -22.72809 | -49.34945 | 2025-12-06 03:49:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b248b55-af03-35e6-ab16-a1e98cd0aa63 | -25.33461 | -49.87576 | 2025-12-06 03:49:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 583d6c3d-89b2-34e3-8ffd-404e58106e1c | -24.16305 | -49.57633 | 2025-12-06 03:49:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ee1616f6-170c-3587-8f35-087be7efdab8 | -27.31859 | -50.55937 | 2025-12-06 03:49:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 51dd637b-fccc-3d3a-9f71-11b190591dbb | -25.33381 | -49.87332 | 2025-12-06 03:49:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bab8a493-f86b-3f7b-bc2a-bbccc1415f37 | -26.91215 | -48.78359 | 2025-12-06 03:49:00 | NOAA-21 | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e5b85c1a-3c25-3250-9be6-46455222c473 | -23.43917 | -47.05722 | 2025-12-06 03:49:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0e569b34-a774-321a-aa8d-2b3a12374686 | -29.92485 | -51.21424 | 2025-12-06 03:51:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| cfc05769-e7d1-33ab-adfd-bf04623009f1 | -29.56013 | -49.91711 | 2025-12-06 03:51:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 7.7 |
| 22dad88b-4f2b-3278-a383-ccf0e50d5560 | -29.9257 | -51.2107 | 2025-12-06 03:51:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| b1ef5771-4156-3600-b99a-f098fbc01de0 | 3.41947 | -51.2649 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7e04a90-3ea6-3800-a984-9ecc926a7c16 | -4.49971 | -40.50475 | 2025-12-06 04:10:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5c37ca50-a2ef-391d-8fdd-8dd72f36c003 | -3.8761 | -41.57955 | 2025-12-06 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76fcb9da-f658-3ec8-bd94-e7a8b8df4f07 | -3.66205 | -43.55785 | 2025-12-06 04:10:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 712df8ed-318a-31db-8501-97d41036a8f8 | -2.02735 | -46.49408 | 2025-12-06 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 990082a5-2c5f-3f0f-8aa8-bd0bba4b6b86 | 3.511 | -51.25854 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28a0df7d-b8e1-350e-b388-50018f0b9c79 | -3.18009 | -39.5616 | 2025-12-06 04:10:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4da59a75-9bae-384d-8036-a675f932cbe3 | -1.48276 | -45.58172 | 2025-12-06 04:10:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d61fb71-70ad-3f3d-8170-6e57ce60fd0d | -2.77656 | -45.51376 | 2025-12-06 04:10:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 903ea176-4a88-3017-adf0-56d8e685dadf | -2.15983 | -47.86823 | 2025-12-06 04:10:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed0ad5a3-d621-3d3d-a42d-86339ef4ace3 | -2.29707 | -45.78496 | 2025-12-06 04:10:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6a571ad-e499-3e39-a350-63283696df59 | 3.41869 | -51.25967 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6abb828f-5fa1-3aee-b506-62d202628ff4 | -3.2412 | -43.34625 | 2025-12-06 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 921c1238-d489-32e9-ab7a-cbe5ab1724ba | -3.3322 | -45.90742 | 2025-12-06 04:10:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 666955ff-83ec-3e49-9837-dc613d731950 | 1.69591 | -50.84674 | 2025-12-06 04:10:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d25ecab5-1c38-36dd-934d-e20baf6c8958 | 3.49586 | -51.24474 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f03da8c8-67cf-3015-bbe7-c484d4ce608d | -2.85834 | -40.07705 | 2025-12-06 04:10:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5f9efaf7-c424-3e08-8501-6ea5ca8aa9a9 | -4.16135 | -39.25119 | 2025-12-06 04:10:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d14b3469-a993-337a-be58-681a7269ef54 | -2.58888 | -45.54915 | 2025-12-06 04:10:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91cc9b0e-f96f-341e-bad8-3e0fa5059699 | 0.43737 | -50.9273 | 2025-12-06 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab060fc3-af42-3cee-bd71-810c7d3f547e | -1.57799 | -48.6483 | 2025-12-06 04:10:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1079277-5aab-3077-b2dc-58d93977c80c | -2.11092 | -53.57504 | 2025-12-06 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3826539-03d0-3b64-b2eb-6b873dc42b20 | -2.34014 | -47.47599 | 2025-12-06 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0568e71f-394c-397e-b413-a6de2831795a | -3.66203 | -43.60235 | 2025-12-06 04:10:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 421b18eb-c4ad-3167-a900-e7ddf9e05c10 | -2.99352 | -45.58398 | 2025-12-06 04:10:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c498358-c4b0-3de1-8dc1-3c6167a5e8f9 | -3.87555 | -41.58302 | 2025-12-06 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9821a4a3-87d5-3c4a-b3ca-457cf5114756 | -2.0663 | -45.36636 | 2025-12-06 04:10:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dc57a72-3f44-3734-93d6-33a8a6bb51f9 | -2.77176 | -45.51823 | 2025-12-06 04:10:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c5be5111-aeed-3228-a4d3-03b8432551f9 | -3.6961 | -42.13699 | 2025-12-06 04:10:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 27505552-7055-3166-9a33-6c4a8955e6ee | -3.87832 | -41.58702 | 2025-12-06 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aebedcef-9644-399f-b9a2-6edffc1412e2 | -2.16454 | -47.86897 | 2025-12-06 04:10:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a7001f3f-5508-3587-aa5b-48e0cee94509 | 0.43828 | -50.92547 | 2025-12-06 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35b5e0b0-b28b-3211-b9ba-af847a9cd874 | -3.66621 | -43.55451 | 2025-12-06 04:10:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f98f863-7b55-32b1-8429-ae87ebb278dd | -2.1302 | -45.32441 | 2025-12-06 04:10:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4de23da6-42f3-3a22-8d96-dd8e19293576 | 1.70169 | -50.84483 | 2025-12-06 04:10:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c0d8e73-8582-39ba-998e-9b9fe16007c2 | 3.50304 | -51.249 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9281b5ef-7867-325c-810c-38c1bef7d191 | -2.17005 | -47.86477 | 2025-12-06 04:10:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd07c877-a5d7-3989-8930-b688ea2553ea | -2.6084 | -47.00924 | 2025-12-06 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc8313c8-2d90-34f2-bca5-5c3b453d831e | -1.82056 | -45.72367 | 2025-12-06 04:10:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d556a6b-405a-3484-84ee-ad8513b24bb4 | -3.03454 | -44.47865 | 2025-12-06 04:10:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99e5ba04-1305-3fcd-a025-8043326d3b69 | -3.23769 | -43.34566 | 2025-12-06 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83262711-7e1a-3708-af32-27ad09f1ec1f | 3.41382 | -51.27113 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0eb8487-5e7d-3748-85ef-0177e05c1b44 | -2.06852 | -45.36477 | 2025-12-06 04:10:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 791fb9ff-bd83-35e7-9141-93ea8eb8b980 | 0.43664 | -50.9228 | 2025-12-06 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7637927-0da6-3624-ad8b-496c65eefbea | -2.70349 | -45.68662 | 2025-12-06 04:10:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cdce7e8-47ae-3c37-8c48-77d1a1ca5afb | -2.02472 | -46.27071 | 2025-12-06 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2640a8ee-b075-34a1-8119-774d01782e65 | -3.47256 | -43.88751 | 2025-12-06 04:10:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63f709f3-7d20-3772-8c3b-b1ae816e65b4 | 1.69663 | -50.85133 | 2025-12-06 04:10:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9bf7fa2-acf8-381e-8c54-0b956b4d0226 | -2.3447 | -47.4768 | 2025-12-06 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3cdbc892-ac3f-3dac-81ee-e9a7414f7d8f | 1.70202 | -50.84578 | 2025-12-06 04:10:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1c84612-8428-3b18-83a2-8e7c7ab6bf64 | -2.16926 | -47.86972 | 2025-12-06 04:10:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f70dd0b5-62ab-311d-9bfe-7c6e38075f8b | 3.47487 | -51.24052 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd555d4b-c261-30d6-975e-b3ce43359898 | -3.20198 | -43.34395 | 2025-12-06 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5657ad44-96e1-3747-97f6-5199bc0407e6 | -1.72087 | -45.77507 | 2025-12-06 04:10:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec6a4a4d-2814-3744-ab8c-b840046ca5b6 | 0.43758 | -50.92097 | 2025-12-06 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README4.md)
