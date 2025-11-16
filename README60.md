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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77f48141-21e3-3622-95c5-ae8d7e280f62 | -8.31733 | -45.4057 | 2025-11-16 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bfb4e293-fa51-3042-8c23-ddc201a485ff | -9.33068 | -46.57347 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06f90f96-418c-310d-9669-5bd44df0e11b | -6.81278 | -48.78833 | 2025-11-16 04:57:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a36c98c0-357d-3665-9e0e-b8e981f725b3 | -8.58346 | -46.05308 | 2025-11-16 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 391d28cb-f1c9-35fe-bb05-80ab5d275066 | -8.54529 | -46.06625 | 2025-11-16 04:57:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dac6767d-d5a5-3218-8f74-9271157446d7 | -7.01562 | -45.16786 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b9d85d4-f29f-3d52-945d-e8f3b6d24392 | -10.80644 | -47.99093 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5cf7d780-36e6-3aea-a46c-876991d89cfe | -12.67163 | -47.18251 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa315e2b-9b04-3004-bff4-dd18d35b6e69 | -10.66602 | -44.80008 | 2025-11-16 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8a909a2c-c1f6-3b67-8994-8f8a8dcbb12a | -8.90122 | -44.43078 | 2025-11-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e97caba6-28e0-3bd6-9fc5-df376d27d1d8 | -11.96063 | -44.94868 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b11b5938-daa3-3226-a165-b631d4c75d74 | -9.44504 | -59.20851 | 2025-11-16 04:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b69756e6-99d3-3600-b8e6-6d3b6569684a | -9.84454 | -44.1781 | 2025-11-16 04:57:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9670754c-3171-33fc-bfd5-a09f5887be2c | -12.41984 | -48.12864 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f61dd7b-cbfe-3670-a8e0-4f269c8610ce | -7.26217 | -48.02497 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74f93742-b3c9-3c06-882a-800bc76b825e | -10.00738 | -44.76866 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4431039c-034d-35ed-bf41-9725404ad7a7 | -7.03633 | -55.50303 | 2025-11-16 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f2795f2-a6b7-3039-a7ce-8c277f06b04e | -6.31204 | -43.79738 | 2025-11-16 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 61453340-8bec-3859-bfc1-d3cb0fd57e75 | -9.71383 | -48.90644 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 13ae0e3a-f7c6-3583-8de7-83da09546697 | -6.71301 | -42.12521 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 32814aba-eabb-3fcf-b872-79d5602f2863 | -9.72876 | -48.88603 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd06ba62-493e-3a26-a98f-8c97d1d9aa0f | -9.85005 | -44.71327 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fbcd39c-17a9-316d-b1f4-f272619517ee | -6.8764 | -51.8088 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63d00db6-6216-3afe-b2b1-bd2e41e1fbda | -10.66938 | -49.36169 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0edb42fe-a201-3e0c-8fa0-114ea5059cc3 | -7.71826 | -47.30119 | 2025-11-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffd3bd96-d5b8-3e3c-bf11-6c5a00280901 | -12.86416 | -46.78215 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa61aa17-5b8f-3985-829b-a117b074c56e | -9.74704 | -43.95904 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0d787423-1ab0-3d7b-ad93-ff7b71775139 | -11.66134 | -54.58235 | 2025-11-16 04:57:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d4fab41-c359-384f-bf6a-33193b7b44db | -4.38478 | -56.02763 | 2025-11-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a115acce-6216-36b0-bd22-9aa2e1b7375f | -16.56539 | -47.60495 | 2025-11-16 04:59:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5206c4f7-d095-3d0f-91fb-2b5368ae86cc | -13.06212 | -53.94851 | 2025-11-16 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55b1c10c-ba2e-3abe-8459-27d4c562b1e7 | -14.65292 | -46.5929 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4540af0e-5964-3acf-b975-58e4bb35de74 | -13.98016 | -48.77242 | 2025-11-16 04:59:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa2302b2-1685-3038-8536-915fb209148b | -14.89452 | -47.37111 | 2025-11-16 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cd34f3d-41fe-3d7c-ac91-38af41bdb8bf | -12.44451 | -54.21397 | 2025-11-16 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7ac623c-fb41-30d8-9d9d-8b924624bc57 | -14.64655 | -46.57391 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c334222-eb4b-336a-83ca-729e3d52cf1d | -17.58259 | -46.6823 | 2025-11-16 04:59:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 724928fc-deea-3719-bbdc-1b3977947901 | -14.48995 | -46.62718 | 2025-11-16 04:59:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0e97468-4873-31f0-bc85-5aa3eb9a5fee | -14.64927 | -46.57698 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a0a370e-c2ba-3528-8ee5-a770d7069e65 | -14.49076 | -46.62031 | 2025-11-16 04:59:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd47beba-3563-3e3f-9746-f87905c9c344 | -14.6424 | -46.58979 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| acaa844d-8b62-33ef-8368-9e13865906e2 | -14.68032 | -46.54342 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbd3c257-a92b-3469-86fb-03629daf5dba | -13.2735 | -47.30293 | 2025-11-16 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3087b38-3ea4-3f13-96a4-f33d5c5b874e | -14.64732 | -46.56753 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43b5410d-e2bb-32bf-bb00-a491b44f0b3c | -14.49036 | -46.62374 | 2025-11-16 04:59:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4ad444b-aad0-36a6-8519-0b5d7dbb00e3 | -13.75871 | -48.52438 | 2025-11-16 04:59:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2dfa7eb-3254-3220-9254-c6daa201e80b | -14.71165 | -48.09578 | 2025-11-16 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92a015f5-bacb-3f61-b4cd-f780a3ce4357 | -14.95334 | -47.52614 | 2025-11-16 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| deed265b-17cd-3f0f-a3c6-52d1c8573058 | -13.81997 | -42.54351 | 2025-11-16 04:59:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1bfa406e-8211-34d5-9270-e2ff1d858c49 | -16.56574 | -47.60178 | 2025-11-16 04:59:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 534f5695-8df0-3272-8dfe-74c9987ec18a | -12.12839 | -55.45056 | 2025-11-16 04:59:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b1d9008-3813-3867-beef-246e7cc6fe6d | -16.56504 | -47.60807 | 2025-11-16 04:59:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fc517fa-aedb-31d5-b2a4-b77cb96ea5b5 | -14.64695 | -46.57057 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eaad0d03-1c31-3a24-8740-b826d1917e83 | -14.64767 | -46.59126 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9534fcee-a1f0-381b-a3af-57d3c23220f7 | -13.97948 | -48.77782 | 2025-11-16 04:59:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79abbaf4-f15b-3d7a-bf4c-1caee50cc3a9 | -13.05873 | -53.94798 | 2025-11-16 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc0ced2-ee93-390a-bb6c-2aa8690d7df7 | -14.95221 | -47.52736 | 2025-11-16 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 63c821fc-8b98-371b-9731-779e9b8e7191 | -14.67833 | -46.56078 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7236b35-c14a-39ca-b457-e73c2be89bd4 | -14.6457 | -46.58103 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1428c376-7392-3b59-ad6a-3d083e09c8a7 | -14.66502 | -46.5822 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 32a5885b-7364-3721-b90b-5726cc227afd | -14.67992 | -46.54689 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e6c2e8b7-d584-3d47-bf3c-f90b3356ac79 | -14.65 | -46.57052 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f5bec2af-f2be-3f20-966a-9f17357dde1f | -14.90479 | -47.37181 | 2025-11-16 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b32782d9-205d-38da-bac6-f44a7d8b66e9 | -14.94778 | -47.52967 | 2025-11-16 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22e0b33d-0822-3c4a-a67a-b1dedf9c5ec0 | -16.57051 | -47.60573 | 2025-11-16 04:59:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1dd6da9a-eabe-326f-9a3b-86fe2ce953d8 | -14.64437 | -46.5722 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98a6aade-0a25-36ad-8a49-3ef374737c46 | -14.65972 | -46.58096 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0781971f-3de2-39dd-b2dc-e0e6a9f8d38c | -14.58633 | -45.21983 | 2025-11-16 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28877983-ecb4-3e61-9070-b81b5bc9903c | -13.71526 | -48.54279 | 2025-11-16 04:59:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eeaad4a2-9563-3248-baa5-849514ca2681 | -14.58524 | -45.22311 | 2025-11-16 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 282905a2-a785-354a-9ccd-b99c0598f869 | -14.65359 | -46.58702 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 708079b9-07bf-3284-8d6d-7a1f00d4eb6d | -13.81812 | -42.5479 | 2025-11-16 04:59:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0ef87739-0a87-3887-9dbf-9fb385ce3c21 | -14.58584 | -45.22413 | 2025-11-16 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dd3edba-fbda-3467-ab16-5dd470c574a9 | -14.64886 | -46.58066 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 541ae44f-3a74-3ef3-b08c-d751f4b8699e | -14.64358 | -46.57924 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8c2605c7-e5df-394b-a770-be41443a27bc | -14.64524 | -46.58486 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8db37b50-a981-37ba-a246-82ed6bb1a31d | -14.64474 | -46.56887 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb61d856-aa64-32cb-93c8-8b21821c0b5f | -13.05479 | -53.95115 | 2025-11-16 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 922143c8-ad4b-32f3-85fb-eb7c1a7d9558 | -14.67873 | -46.5573 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b1878d3-d4fd-36de-9000-bad27c15fa4a | -13.71079 | -48.19675 | 2025-11-16 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbeddfbc-da41-38c2-a7ea-d252e846de4a | -16.56981 | -47.61199 | 2025-11-16 04:59:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca438a7b-d658-3145-ad7a-428938d90ef9 | -13.81915 | -44.45312 | 2025-11-16 04:59:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edf7875f-9b59-3c9e-9517-a781b2bd1f81 | -13.07397 | -53.93897 | 2025-11-16 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 314cb73c-5bed-3062-a558-acca021e0e8d | -14.6646 | -46.5859 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ad2185e-7f17-3320-b27d-0a774e508d98 | -13.81251 | -42.54903 | 2025-11-16 04:59:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0ef51a73-42d6-3ba2-9925-07bf473dcd44 | -13.05534 | -53.94745 | 2025-11-16 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3d38955-45ae-3c30-b23d-eeba458e5b81 | -14.6451 | -46.5657 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75ceacde-c8eb-3cea-b1fe-a14332c64907 | -14.67912 | -46.55386 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5684fcb6-2d6c-3b99-8fa8-05886f57752a | -14.64483 | -46.58831 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cc96596c-8a4e-3495-a871-47e9e61b091a | -14.64447 | -46.59131 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5fd1097b-7c6d-30da-bee4-7d94932a3dd4 | -13.81971 | -44.44824 | 2025-11-16 04:59:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78ac09d6-f031-33c3-b174-4b97b2caa9c5 | -13.87241 | -46.84348 | 2025-11-16 04:59:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a94e257-1727-3628-9ba4-5f7a70160dfe | -14.95294 | -47.52945 | 2025-11-16 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d85df4a-41f2-3022-adc3-f589de4d8726 | -14.95181 | -47.53086 | 2025-11-16 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b9da128-a5dd-37cb-bcf7-3af25590f599 | -14.6484 | -46.58475 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ae6a447-f74c-3362-a1b7-1cc9c57a86f8 | -13.27313 | -47.30602 | 2025-11-16 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d202afc6-21b8-33ac-b553-d6fea47842bf | -14.64614 | -46.57735 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4e218141-32de-3703-910f-ae4d5558beb5 | -13.87203 | -46.8467 | 2025-11-16 04:59:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76722b64-fcb3-388c-921a-c9ce9e90ba4e | -14.50132 | -58.42582 | 2025-11-16 04:59:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c26f58a-436b-394f-9a34-74a207c02ad7 | -13.79023 | -46.90337 | 2025-11-16 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README61.md)
