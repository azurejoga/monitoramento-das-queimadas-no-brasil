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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 736679f1-c1f8-3d37-b095-3cd1828da89c | -5.35159 | -43.13928 | 2026-07-27 03:28:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67f32aee-8780-38b5-b96b-a0bc2194a672 | -7.61933 | -38.79513 | 2026-07-27 03:28:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ed5bced4-9d99-395d-a266-9466e8e9712a | -5.9351 | -43.65454 | 2026-07-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9465311e-026a-3fa8-95a9-f671302fc18d | -10.9397 | -43.0593 | 2026-07-27 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 285.4 |
| 764c9ff6-da2a-3ab2-b84a-e66f93bc73b3 | -10.9401 | -43.0355 | 2026-07-27 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| bc7194b5-de1c-3e08-8dd8-991388c3909e | -10.9588 | -43.0565 | 2026-07-27 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ac738653-d604-34b9-bd79-cc0eb7b3437f | -10.9205 | -43.0622 | 2026-07-27 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f532739d-4334-3059-a1f8-5ff4e58c8332 | -10.93953 | -43.05848 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 214c42a3-8c0b-373d-b206-6d338eabbfc8 | -10.94476 | -43.06258 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fd7d99d6-0957-331e-aa46-f290f8b2cb55 | -10.93765 | -43.06787 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| f6c771b6-4cae-3380-9b8e-e837721e65c5 | -10.93899 | -43.09262 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5aec83a7-8201-39bc-8994-e3bf2ecd2bce | -10.93387 | -43.08663 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 098babab-51c8-3efd-a150-528ad0fc82ce | -10.93859 | -43.06317 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 3eb744a0-b9c9-3110-9c0d-5b793d666be9 | -10.93355 | -43.05529 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 38ef633c-a4d7-33e4-891b-6066960c0989 | -10.92685 | -43.09005 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 484692d1-1c50-37dc-8984-23015d4921b6 | -10.93778 | -43.06598 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 0e376425-b7d5-371d-8d1f-cc28228f4ace | -10.93263 | -43.05999 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 737fa33e-88af-3efc-9ee1-34ee02f33be3 | -11.98445 | -45.5618 | 2026-07-27 03:30:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d1fdf731-014b-335d-93f9-44c04ea3bb60 | -10.9387 | -43.06127 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 8b29d46e-6fe2-3e36-a1ce-bfeafc313aa6 | -10.93292 | -43.09134 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ecefbb66-58df-39e0-a28f-54e84533977d | -10.94048 | -43.05379 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 04f51f09-e8c0-3614-9f04-3ce18d317d87 | -10.93347 | -43.05721 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 60332794-d684-3f3b-be72-0e1ea227cf7b | -10.93576 | -43.07724 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fc5709f-6a86-3af8-bd87-baab423c18d3 | -10.93961 | -43.05658 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| a1e06ef7-bf31-34bf-b62b-de915b5d4b16 | -10.93482 | -43.08193 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6df19672-1174-3abd-8fc6-80ee065d19b5 | -10.93994 | -43.08792 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9688c8d7-1e50-35ef-851a-3930946be71a | -13.08918 | -43.56847 | 2026-07-27 03:30:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f5addcf-3d4d-3dc8-9363-0d38ce089e0d | -10.9278 | -43.08534 | 2026-07-27 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1267e2ed-ade9-3619-abe5-3f23d018d255 | -11.88672 | -43.8308 | 2026-07-27 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 79f760a4-65cc-3e50-886b-0359bee2d526 | -19.11065 | -44.33979 | 2026-07-27 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 016a3359-54ba-3afa-9fe6-67a7a3cf4423 | -19.10855 | -44.34059 | 2026-07-27 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6325913-9822-3c31-a014-2606bde47ce2 | -20.06013 | -43.70385 | 2026-07-27 03:32:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 640b20a2-7d75-3175-ad59-326c0bb84e6a | -19.10214 | -44.34279 | 2026-07-27 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f584167-ec7b-3a04-9f2a-d9a1a56a7893 | -18.13066 | -40.16985 | 2026-07-27 03:32:00 | NOAA-20 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6333cd80-597d-321d-b1a6-9c5c4ef16f78 | -19.10428 | -44.34171 | 2026-07-27 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94391ffe-7c06-3f18-8a74-6b35ae9be744 | -19.10779 | -44.34412 | 2026-07-27 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37bbbcbe-82c7-381b-b3c9-72c270106431 | -21.57328 | -41.33532 | 2026-07-27 03:32:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 89e044c8-9a19-3e11-bf13-8b4d086b4d02 | -20.06127 | -43.69859 | 2026-07-27 03:32:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 128459e4-c04f-36c1-aa16-5858cf2a0661 | -19.10128 | -44.34678 | 2026-07-27 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7647a175-6519-3178-9bc9-17fcde08b83b | -19.10345 | -44.34543 | 2026-07-27 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eac6480-e393-38c1-9294-7a5945b1d61b | -23.45144 | -46.27066 | 2026-07-27 03:34:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a165f929-1149-31e5-a3b2-a413807d0f5f | -23.37065 | -46.9367 | 2026-07-27 03:34:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3d3c3308-556d-345e-8631-9dcf591fffa6 | -23.37185 | -46.93172 | 2026-07-27 03:34:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 718ae3c8-423a-3e7a-9913-b463e46c0300 | -23.37781 | -46.93356 | 2026-07-27 03:34:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9144471e-cf0d-3e45-ae91-a4b72fc124de | -10.9401 | -43.0355 | 2026-07-27 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 81455505-620d-3ad8-882a-b78c3d28d1c8 | -10.9397 | -43.0593 | 2026-07-27 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 5056d53e-3ec4-3a29-b13f-78d7dd1226e0 | -10.9588 | -43.0565 | 2026-07-27 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 47d84a61-270f-3873-b6e3-335bff7c7c08 | -10.9401 | -43.0355 | 2026-07-27 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| c8a240f0-6a51-3475-827a-9ffd5fe368b8 | -10.9397 | -43.0593 | 2026-07-27 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 281.1 |
| a36727ab-2366-324b-960c-52e6f14db81e | -10.9205 | -43.0622 | 2026-07-27 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 800784fd-6b3a-33ff-a24d-c43cd3465ad2 | -10.9588 | -43.0565 | 2026-07-27 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| dc1df269-644d-3e69-a1d9-5a83dbbd5f2f | -10.9588 | -43.0565 | 2026-07-27 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ed7ec102-2894-3059-b7bd-44eee90e934a | -10.9397 | -43.0593 | 2026-07-27 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 350.6 |
| 4ed94c94-4e76-353f-a799-03818de2df99 | -10.9401 | -43.0355 | 2026-07-27 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 5aae9cce-eeea-3e99-8b75-d4a92f1dd5c1 | -10.9397 | -43.0593 | 2026-07-27 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 321.4 |
| 665fd41f-12e7-3527-b237-82794d89b64e | -10.9401 | -43.0355 | 2026-07-27 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 64282852-e8c6-3110-bc50-2b85b6655ab5 | -10.9205 | -43.0622 | 2026-07-27 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9405e32c-a564-3eb5-908b-befbd405da17 | -0.99582 | -48.08622 | 2026-07-27 04:12:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e6cce79-dc34-33a5-aad0-5cce1acff53c | -8.38688 | -42.2755 | 2026-07-27 04:14:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88ed7c98-d24c-3bb6-95d0-447bd8376de6 | -3.99889 | -43.29087 | 2026-07-27 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdb9fc64-245a-3659-8998-962956fe1add | -7.62682 | -50.03458 | 2026-07-27 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 37cd73ee-6768-39dc-997b-5c21f7e9c6d7 | -7.69746 | -46.49247 | 2026-07-27 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca486cc2-2e69-33cc-8369-e88dbb2017ce | -2.95045 | -50.32995 | 2026-07-27 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c9f3055-7d2f-3ec1-a4c8-a9b922661449 | -6.92716 | -42.81475 | 2026-07-27 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 91cb5235-851c-3723-8465-45d2707890e6 | -2.80801 | -48.66899 | 2026-07-27 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1a4a5823-224d-306b-aa25-0e26a30a3c3e | -6.98073 | -42.07011 | 2026-07-27 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1b5c0862-2dbe-3059-a1e0-7f88ca8286c2 | -6.95363 | -42.11316 | 2026-07-27 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eaab394f-2bcd-3d43-af7f-20b05ca46ad4 | -7.90108 | -48.04947 | 2026-07-27 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd764918-50bf-38a2-aabc-55134d493410 | -4.9131 | -43.47069 | 2026-07-27 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bf50739f-e84a-35fb-b6eb-0a7df0da48d9 | -3.92174 | -47.82092 | 2026-07-27 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 126e639c-c4b0-342e-9b88-1822a0988f66 | -8.82936 | -47.0723 | 2026-07-27 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce93dff6-2ef0-31a1-8f64-9e5f3addba62 | -2.95137 | -50.32443 | 2026-07-27 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c2b71f1-3bad-38ae-b872-12a6ffd5e923 | -8.82651 | -47.08953 | 2026-07-27 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b7ee3c5-7291-3dad-90fb-e52cb6ac3b6e | -6.3024 | -43.63684 | 2026-07-27 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1780bc92-1cc6-3503-ac39-c1c5a09ed9d1 | -5.93609 | -43.65012 | 2026-07-27 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 90ae5096-bccb-34ce-8515-3967a3d71494 | -2.80731 | -48.6733 | 2026-07-27 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d953a76-66aa-38d7-8abf-fdd953c8b0f0 | -1.54553 | -53.69927 | 2026-07-27 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d95f9050-8812-316b-a46e-48d8dc44591c | -3.72802 | -48.87146 | 2026-07-27 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41fcbac1-89da-3ba9-8ae7-3a577f836f42 | -1.5463 | -53.6946 | 2026-07-27 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 61c3bae7-6ebe-35ed-a4ac-3726f46331d1 | -6.92331 | -42.8177 | 2026-07-27 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc2f4d82-b169-3c2f-9b07-eb144948ba1f | -7.62829 | -50.03687 | 2026-07-27 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8eb4667e-4344-364d-b5be-7716a0feb9d1 | -3.96589 | -43.112 | 2026-07-27 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe70f1f4-6378-313f-a70b-d7c47a7d822b | -8.83088 | -47.08579 | 2026-07-27 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fffc4897-7f59-3968-95a4-7c79f067517a | -4.00498 | -43.29538 | 2026-07-27 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 521f563b-29db-37ea-b62d-b00eb11e4144 | -2.76923 | -48.57539 | 2026-07-27 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87aefd1e-d304-3b55-b842-de3fcfd271bf | -5.35653 | -43.13652 | 2026-07-27 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00cafbc7-b59a-3ff5-9efe-6620000f93b6 | -6.92662 | -42.8182 | 2026-07-27 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ebb97a39-53b6-399c-a7f0-8cd15dd46866 | -5.93831 | -43.65759 | 2026-07-27 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 217764b1-d73b-32e7-a769-408fa30bc8d5 | -3.21841 | -53.1362 | 2026-07-27 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8fc7f27-130e-3da4-9cd6-de45db1654ff | -8.83016 | -47.09012 | 2026-07-27 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a1615da-b34b-359f-98d8-e2a36559a801 | -8.82723 | -47.08521 | 2026-07-27 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1530bfdc-e659-3823-9972-ab37e9bb7c96 | -5.48385 | -45.11838 | 2026-07-27 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42bdb5ac-6ec3-30a0-a992-38980cd3318e | -6.95028 | -42.11265 | 2026-07-27 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0028d333-3423-3d42-9bc6-1d2f4446c2fa | -6.29963 | -43.63286 | 2026-07-27 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b4e0764-61ed-313a-b1ca-fbae33444286 | -6.30185 | -43.64031 | 2026-07-27 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51ddc6ce-d8e0-3b02-95fd-37afeb20fdd1 | -3.26265 | -49.5268 | 2026-07-27 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7345f6e3-3114-35b5-8779-7efe0e9aa1bf | -7.70105 | -46.49305 | 2026-07-27 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5455f6bf-a7da-3900-8384-ee7c9d0906b7 | -5.4873 | -45.11894 | 2026-07-27 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3396c0fe-aecf-39a2-b108-af6c5c7c77de | -7.20491 | -44.87548 | 2026-07-27 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b7084078-53ef-353a-8591-bdb53ca5c28f | -8.12712 | -46.79876 | 2026-07-27 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
