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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c58015f1-bc76-3d7d-a1e5-965446751548 | -12.30599 | -57.18 | 2026-04-23 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb7e3ed3-ce25-3f7c-8f6e-674c2f2c9144 | -12.86748 | -58.62827 | 2026-04-23 05:38:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdb1495b-d04c-359f-9335-62ec7c450c6c | -11.91287 | -58.07833 | 2026-04-23 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2eb85fd-d0e7-3fc6-8e09-a589cc4066ee | -19.44075 | -56.58733 | 2026-04-23 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 450c5901-5a67-329b-b666-8fc54bc88272 | -18.51038 | -55.49966 | 2026-04-23 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d7bd8d06-d63a-3d2e-bf9f-b5c70e25c6c6 | -18.28589 | -52.88468 | 2026-04-23 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bdadc8e-1be2-315d-9efe-4a470b665814 | -18.41488 | -54.54512 | 2026-04-23 05:40:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ef7c408-3059-3619-9f1b-8c32d4c06274 | -14.83023 | -59.83902 | 2026-04-23 05:40:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f21fe76f-76fb-3930-8b4a-9cd2b1c9e28e | -18.2718 | -52.88914 | 2026-04-23 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e63e4076-ae8b-321c-a52d-d0179d0b8b07 | -18.28419 | -52.88607 | 2026-04-23 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f5d5d69-3cda-327d-9ae3-ecc5ab1f3785 | -19.44403 | -56.61058 | 2026-04-23 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c29e36c1-0250-31e8-8033-7df92d648108 | -19.44953 | -56.61124 | 2026-04-23 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 506c58c4-a5c7-3c1c-97d8-a5722fefd9c2 | -16.43384 | -54.91673 | 2026-04-23 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec46801f-ef4b-3826-b78e-3b946ddc3164 | -16.4275 | -54.92022 | 2026-04-23 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 74b7d146-c134-3e68-83de-d32ea9ec3aff | -18.41442 | -54.54987 | 2026-04-23 05:40:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cebf57b8-e135-3426-b473-af1cdacc45f6 | -18.27741 | -52.8851 | 2026-04-23 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4895e70-ffbe-30ac-802c-c92c0190a38b | -18.50455 | -55.49896 | 2026-04-23 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ebc981e6-70c0-3b9a-98e8-32b849dfbe26 | -18.27911 | -52.8837 | 2026-04-23 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d293242f-142c-306e-8568-2717a349b658 | -16.42792 | -54.91608 | 2026-04-23 05:40:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 514ee689-e487-3b78-88ff-8f9cbcbd2d3f | -19.44626 | -56.58797 | 2026-04-23 05:40:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3b151f5e-1a13-3e85-809c-39e24e899dea | -11.78626 | -43.62503 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f665e25b-1634-348f-9586-95545abced5b | -11.78776 | -43.61438 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| f5a09a08-8b9b-3507-89d3-fd69f9e206fe | -11.78024 | -43.66766 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be8ec845-5e46-37e2-9afd-40adbd072b43 | -11.78174 | -43.65702 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9242a6ff-a172-3bd0-a8f6-bc09ae2ea53c | -12.28156 | -44.6171 | 2026-04-23 06:18:00 | AQUA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fa4df6b2-3323-3898-8dcd-c56b0f15be2b | -11.7642 | -43.64359 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d412560d-8fb5-3c87-9a36-55b6eba44437 | -11.77223 | -43.65561 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a77b45b7-2110-3f99-bc03-2ab27f4e8d7b | -13.37965 | -45.31698 | 2026-04-23 06:18:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26e9d27d-ea84-3f9a-a6e1-781ef2125849 | -11.77372 | -43.64498 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fc39a938-5462-3a72-bb04-4697fddcab2c | -11.77372 | -43.64497 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c70cb44e-622d-382a-aa5e-2a20b5ec61df | -11.78024 | -43.66764 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| badebdc4-638b-35b2-8188-d7b15d3d9b9f | -11.78626 | -43.62502 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e52df673-e384-3acb-95fc-245c7ec3cf81 | -11.78776 | -43.61436 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 5185b97c-1213-37fb-99b4-d2377a21c943 | -11.77223 | -43.65559 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a3b50e91-5b3e-3ea2-bdf7-258c5a06f3ee | -11.78174 | -43.65701 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f5d25898-aa69-379a-9d39-fd3be1402492 | -13.37965 | -45.31697 | 2026-04-23 06:18:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 958f9245-27d4-3d60-8d22-59ec11e44314 | -12.28156 | -44.61709 | 2026-04-23 06:18:00 | AQUA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 404633ac-05d2-34f9-8648-da4a052e3f8b | -11.7642 | -43.64357 | 2026-04-23 06:18:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 4a0782b8-d74c-3faf-8163-71fffff3ac82 | -20.23349 | -46.79768 | 2026-04-23 06:20:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3a6cdaa3-272e-3beb-a65f-367956e404d3 | -20.20019 | -46.90143 | 2026-04-23 06:20:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6c1d6d7d-c05e-3f5d-9c3e-1408b8c365b8 | -20.18365 | -46.8891 | 2026-04-23 06:20:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f0cbba66-796e-3b27-9ef9-f0890d111ea6 | -20.2002 | -46.90141 | 2026-04-23 06:20:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| de2450dd-f282-3aca-af73-71d25b64da60 | -20.18365 | -46.88909 | 2026-04-23 06:20:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 957c2477-3883-3c3a-b0aa-835a8616f584 | -20.2335 | -46.79766 | 2026-04-23 06:20:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4352f1db-bfde-3f84-987a-3ad476f61808 | -15.62456 | -39.0092 | 2026-04-23 11:04:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 813cef3b-95cd-32f5-bd17-a9d50f168cc6 | -15.62455 | -39.00922 | 2026-04-23 11:04:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| f543248e-6627-3751-b835-68b65cfa8b09 | -13.3761 | -45.3243 | 2026-04-23 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| cd61b620-e58c-3145-8ea4-a28f078fa458 | -13.3761 | -45.3243 | 2026-04-23 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| b77cb32a-8393-3bdb-81f1-df3fc573a241 | -13.3761 | -45.3243 | 2026-04-23 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 7acbd4ce-b360-3da6-bdee-3e8aa8107350 | -13.3761 | -45.3243 | 2026-04-23 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 05588f9a-c5b7-359d-894b-188e9fce3c34 | -13.3761 | -45.3243 | 2026-04-23 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 50bc45f0-5684-3f70-8998-cb15cb3b4b21 | -13.3761 | -45.3243 | 2026-04-23 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f798ad65-6d86-3627-abcf-d5dcd6ccb054 | -13.3761 | -45.3243 | 2026-04-23 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a5647598-8cae-3f83-8486-c463a814689d | -13.3761 | -45.3243 | 2026-04-23 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e73beee0-9c6c-35ff-a5ce-13ce3c3f164a | -11.772 | -43.643 | 2026-04-23 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b5fbce54-35a2-310e-9eb8-1585269dbe1c | -13.17317 | -53.6605 | 2026-04-23 12:42:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 214e55c0-e1db-3916-a2a3-b0395eaca237 | -14.20436 | -57.43226 | 2026-04-23 12:42:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 57b6dbdc-a295-3f64-ad08-3c65b2282c57 | -14.20568 | -57.42244 | 2026-04-23 12:42:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 7396abbb-1f6c-3df6-911f-b4760b37c1ca | -14.20436 | -57.43228 | 2026-04-23 12:42:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 960bdd5d-1b79-3a66-99db-3a58a054e23c | -13.17317 | -53.66052 | 2026-04-23 12:42:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 25a5828f-ab95-32ca-bfff-e45326ebf4d9 | -14.20568 | -57.42246 | 2026-04-23 12:42:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| e756bd2a-f790-3216-9378-264633881582 | -18.27912 | -52.8856 | 2026-04-23 12:44:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 58549ab1-ecc2-3839-ac53-085bf3d46d3e | -18.29246 | -52.88728 | 2026-04-23 12:44:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 21cdddd1-b1f2-30e6-991d-779caded483e | -16.42618 | -54.91717 | 2026-04-23 12:44:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 66471d14-92ec-3388-b7f1-cb22f5188762 | -16.43989 | -54.90962 | 2026-04-23 12:44:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 040b47a0-a6bc-33f1-a5e1-cc98304e5ee5 | -19.68541 | -51.35028 | 2026-04-23 12:44:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 24.2 |
| fe136bc2-97d4-367d-a78b-e8ca8d682258 | -18.28827 | -52.89229 | 2026-04-23 12:44:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 031bb938-353c-30bf-bde6-11df92f63b3b | -19.68853 | -51.34496 | 2026-04-23 12:44:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 30.8 |
| bc256917-153d-30f2-b848-4374cbd5968b | -16.42618 | -54.91715 | 2026-04-23 12:44:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 97414b80-9c19-39cd-86ea-63074ead4983 | -18.28827 | -52.89231 | 2026-04-23 12:44:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 2f92e06e-b078-38c6-83b0-69413ce5c26d | -18.29246 | -52.88729 | 2026-04-23 12:44:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| d3de28c5-f820-35a9-879c-9d646cc475cc | -16.42709 | -54.92292 | 2026-04-23 12:44:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3fda4cc2-e49a-313a-8428-383bf33966cf | -16.43989 | -54.90963 | 2026-04-23 12:44:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1b2f332b-be54-3607-8077-56fa40694532 | -18.27911 | -52.88562 | 2026-04-23 12:44:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 41.3 |
| f029eea1-a711-32ee-8ad0-7a5054ceb944 | -16.42709 | -54.92293 | 2026-04-23 12:44:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 00b49fc2-af52-38eb-ae3e-d0486ef9ba98 | -19.68853 | -51.34497 | 2026-04-23 12:44:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 1015b1ab-c5ae-30e6-8bc4-efa6600bbca3 | -19.68541 | -51.35027 | 2026-04-23 12:44:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 40143b10-38ed-3af6-b9ca-7fa18522b286 | -11.772 | -43.643 | 2026-04-23 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9521702d-8627-33f9-9a2e-f1ff4881d5e8 | -13.3761 | -45.3243 | 2026-04-23 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 406ef035-40e0-348a-94d5-87202e21cde6 | -13.3761 | -45.3243 | 2026-04-23 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2a1b0a88-9360-3308-bbec-7ff916128d4a | -11.772 | -43.643 | 2026-04-23 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e9e92a9f-1fa5-3de0-8f90-8a0f9072e5be | -11.772 | -43.643 | 2026-04-23 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 4a2ee1c4-a7c6-3d1a-9e61-28248c6de8f2 | -13.3761 | -45.3243 | 2026-04-23 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5fb286f0-c036-312e-896c-bac22126a92e | -12.2421 | -44.1807 | 2026-04-23 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 6b54586e-ef2f-3514-a675-1b73f9f8b9b3 | -13.3761 | -45.3243 | 2026-04-23 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 18fb9e47-bec4-3aa5-aeb0-5c80050c3b10 | -11.772 | -43.643 | 2026-04-23 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 4c955db4-b2ba-3392-ba0a-fec5967739bf | -13.3761 | -45.3243 | 2026-04-23 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| af6db2a3-ba0a-3d1b-942c-f3c2f58ab132 | -11.772 | -43.643 | 2026-04-23 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 2f0aec46-2057-3e1c-a29a-2eba17ec9bac | -12.0502 | -45.2103 | 2026-04-23 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 48a3ddca-4252-37c7-a73d-d2aa7a9c37fb | -12.2421 | -44.1807 | 2026-04-23 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| d435a9a8-bbab-3b9e-bd41-13f0f8f2c47e | -12.0502 | -45.2103 | 2026-04-23 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 37bc7efd-0aa2-3f09-bdbe-507c41e82967 | -11.772 | -43.643 | 2026-04-23 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 3926c951-b7f0-37bb-923d-751e97e466d8 | -13.3761 | -45.3243 | 2026-04-23 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| fdbec9ce-ef74-327e-b66d-f02a22fcac18 | -11.7528 | -43.646 | 2026-04-23 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e5be2c77-2191-3799-a8ff-613de7f5838f | -12.0502 | -45.2103 | 2026-04-23 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ae0dc015-5033-3e02-9bdd-804059eed9df | -13.3761 | -45.3243 | 2026-04-23 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| a863155d-a4c5-30d2-b965-ced8822626c3 | -11.772 | -43.643 | 2026-04-23 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 9011b2fb-b43a-31d3-b9b2-68f55cf925d4 | -13.3761 | -45.3243 | 2026-04-23 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| dbba7374-428d-3793-b530-0fe26025f0ec | -11.772 | -43.643 | 2026-04-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 0ddd2fd7-29fb-3d65-b66a-959c7c5ef70a | -11.772 | -43.643 | 2026-04-23 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |


[Clique aqui para ver as próximas entradas](README9.md)
