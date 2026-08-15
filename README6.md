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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78be5321-709c-340f-85c2-d9c409e2b02f | -6.1222 | -44.0271 | 2026-08-15 03:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 6891fe1c-20a6-3e29-8211-d87dbbed4ba0 | -6.9145 | -43.6351 | 2026-08-15 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 6ce6037a-d997-3dd8-9d78-3049d5fc1d0d | -14.4499 | -51.9004 | 2026-08-15 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| c1daa4fc-25b8-3e8e-86cd-cc378ae34c4c | -14.4495 | -51.9217 | 2026-08-15 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c770f597-ddef-36f1-babd-3690b9f56bf4 | -6.6013 | -59.0037 | 2026-08-15 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 543f6d3e-30ed-389d-8ad2-508bc3725a8a | -10.7282 | -50.5552 | 2026-08-15 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f8f3cd35-c4fe-3ae4-9df8-5017f215a2c8 | -14.4306 | -51.9029 | 2026-08-15 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2b613fc6-0588-3f13-b31a-0af8f1d035ef | -14.4302 | -51.9243 | 2026-08-15 03:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| c1c9e2e7-0751-3972-b9e0-25ad2a40d22e | -6.9334 | -43.6333 | 2026-08-15 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| f20296d3-799c-3da4-a592-6147aa58314a | -14.4499 | -51.9004 | 2026-08-15 03:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 720d225a-00bf-3927-be5c-23c9560ef743 | -6.6194 | -59.0609 | 2026-08-15 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 895423f0-9742-3207-9670-3182ffeabe85 | -6.6013 | -59.0037 | 2026-08-15 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 53692155-e4cb-389a-af8d-bad6234e0ba6 | -14.4306 | -51.9029 | 2026-08-15 03:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 130c54c6-2f5a-3da4-a8fb-bbf379556260 | -14.4495 | -51.9217 | 2026-08-15 03:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f7d8aef6-658a-3907-99e9-f0bbcf8b6d5f | -6.9145 | -43.6351 | 2026-08-15 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 61d04ef0-f604-372f-b911-13ba494a13be | -6.1222 | -44.0271 | 2026-08-15 03:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d6e41d26-18ae-3324-85f7-85a889d3f84a | -4.52639 | -38.54735 | 2026-08-15 03:15:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f9494629-de1d-3ba7-9590-db4f0a374389 | -4.52574 | -38.5512 | 2026-08-15 03:15:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ba445bbc-9628-332d-9a72-f3636674afd8 | -4.01526 | -38.25259 | 2026-08-15 03:15:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 65cac2b5-ff54-36cb-8a69-7961959d582d | -4.95284 | -37.93698 | 2026-08-15 03:15:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 58ea6751-7e9e-3b31-89f8-86418341e8b9 | -5.19441 | -35.85196 | 2026-08-15 03:15:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c1e36804-195b-35e0-9f1e-2f48bd3cde79 | -5.11615 | -41.10649 | 2026-08-15 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ff5943a1-e5c5-336b-a9aa-a605fd77b488 | -7.01056 | -41.43371 | 2026-08-15 03:17:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 809feab7-5478-34c9-bac6-a026bfb5391a | -5.11721 | -41.10059 | 2026-08-15 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 874093c4-eb89-3c65-94de-985af80a71db | -7.01596 | -41.44085 | 2026-08-15 03:17:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ab947965-1680-3c93-a702-339871ea7efd | -6.41331 | -39.25471 | 2026-08-15 03:17:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7afbe1ba-d15e-3628-a459-80297ad8db8b | -9.28606 | -36.8528 | 2026-08-15 03:17:00 | NOAA-21 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f9916755-c349-32ed-ae71-e6a4f6a6761d | -15.91938 | -43.5241 | 2026-08-15 03:19:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa05a2f7-2650-301a-96e9-c4a8f1177882 | -16.83155 | -42.26271 | 2026-08-15 03:19:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 208033a6-88e8-3728-9880-2d3ab0f156a3 | -16.83727 | -42.26416 | 2026-08-15 03:19:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2202d7aa-6c40-3200-a478-629b8022c736 | -12.08404 | -43.1794 | 2026-08-15 03:19:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 4f1a51c2-6f82-3e02-8e5f-da359878553e | -17.90184 | -44.44621 | 2026-08-15 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c92d9ba8-b6be-33af-868f-7f31d447184d | -14.69325 | -42.91499 | 2026-08-15 03:19:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 205168ee-4f2c-3cc9-bf2c-7fed53958924 | -15.92569 | -43.52551 | 2026-08-15 03:19:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90070a30-a14f-3955-ad86-d3968ae17204 | -17.89557 | -44.44414 | 2026-08-15 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66127f09-1ba3-3808-89d4-bb2116021693 | -12.0869 | -43.17868 | 2026-08-15 03:19:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| fde0f297-3642-387b-a595-716e6d9b2293 | -18.58216 | -41.27688 | 2026-08-15 03:19:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ef8e19f2-4d8f-3af8-81d1-177f6c512875 | -13.47927 | -44.04232 | 2026-08-15 03:19:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e427219f-8810-3b11-bd02-9da2bab53afa | -15.20389 | -41.05128 | 2026-08-15 03:19:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2e21f685-15cc-3067-a88e-0907dd16460f | -18.58662 | -41.28178 | 2026-08-15 03:19:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 134ba2b5-56cd-3bd3-ba3a-5f84e0d1e9d5 | -10.76055 | -42.08818 | 2026-08-15 03:19:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5f0a6b1c-2294-3338-b485-f99ff3acc4ff | -12.08017 | -43.17786 | 2026-08-15 03:19:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67524e3b-93b6-3171-9e77-e26f372d402d | -16.83819 | -42.25989 | 2026-08-15 03:19:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 62d92bad-bf25-3597-9baf-2e0fd56b41ab | -15.15106 | -41.55978 | 2026-08-15 03:19:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8a7439cc-3e0a-3fc4-81f3-0a34c265da6f | -14.69596 | -42.91345 | 2026-08-15 03:19:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0787bebd-3e0c-32db-9936-9f994f8c50b7 | -16.83248 | -42.25838 | 2026-08-15 03:19:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2b47ef2a-9d74-3c58-9e90-5affb51f3e21 | -18.58145 | -41.28027 | 2026-08-15 03:19:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f71bd579-4631-3618-a267-ea5992d32bb5 | -10.75948 | -42.09344 | 2026-08-15 03:19:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fb79f391-80aa-3807-a18c-0f3cf3f844d3 | -18.5808 | -41.28334 | 2026-08-15 03:19:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 0c41cf6d-1ffc-35b1-8002-cbdb9c5c8375 | -18.58733 | -41.27839 | 2026-08-15 03:19:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 21193943-be5e-36f7-af13-cd884fe62b20 | -6.9334 | -43.6333 | 2026-08-15 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| fa259b3f-8f7a-3b6c-bd89-48d1e1d23e77 | -14.4499 | -51.9004 | 2026-08-15 03:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 911f3516-8bb1-399f-820c-eb934c52eb26 | -6.1222 | -44.0271 | 2026-08-15 03:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 72b762e5-0919-3616-9817-6bc597fa5cd6 | -14.407 | -48.9566 | 2026-08-15 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ce3730b2-4c64-3d81-81e3-0dcb022e5d37 | -14.4302 | -51.9243 | 2026-08-15 03:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 389a7a65-ff1a-30f5-9aa8-2d6b1b6c3619 | -14.4495 | -51.9217 | 2026-08-15 03:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d287950f-8664-34e2-b56b-5d9f2e9b66e4 | -6.6194 | -59.0609 | 2026-08-15 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 081e3cfc-7bde-3e61-b443-adc733bb3350 | -14.4306 | -51.9029 | 2026-08-15 03:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 019ad558-dedd-34ff-b44a-d3a410307a7a | -6.6013 | -59.0037 | 2026-08-15 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 8a4fdf93-b992-3727-a7f7-a13b7cd09167 | -20.01684 | -43.89845 | 2026-08-15 03:21:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d67435d9-de30-3919-8879-3fab704d99cd | -18.72435 | -43.01067 | 2026-08-15 03:21:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4c3425e-b778-3576-a7a3-6810c8a903b9 | -20.42949 | -46.46686 | 2026-08-15 03:21:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c70b677-e7be-3ef1-8944-e32cb1a79b0e | -20.698 | -42.57372 | 2026-08-15 03:21:00 | NOAA-21 | CANAÃ | MINAS GERAIS | Brasil | 3111705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 40bd9a6f-0cc2-30a1-ac7f-1eaae1e5a268 | -20.01609 | -43.89277 | 2026-08-15 03:21:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3099517e-d542-3163-9cb1-7b7ea126a51c | -20.01501 | -43.89755 | 2026-08-15 03:21:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 402fe84a-ef88-34e5-af73-5671c0291754 | -20.01796 | -43.89361 | 2026-08-15 03:21:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 85f5b560-3cd9-3332-9171-f412bf716310 | -23.0076 | -45.51245 | 2026-08-15 03:21:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a98e8619-ed4a-36d2-b243-c2e99cf5871a | -20.4299 | -46.46362 | 2026-08-15 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f71c037f-1d31-327e-85f6-3438a1c50081 | -20.3312 | -46.75055 | 2026-08-15 03:21:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c827bf11-56b1-30c6-ae7b-4bc108d01280 | -18.45398 | -43.43792 | 2026-08-15 03:21:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 7fc169fd-4b76-3b42-acae-a54fda8667c8 | -6.1222 | -44.0271 | 2026-08-15 03:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 56dd3b7f-7b19-334e-9890-3c82a6a95d7e | -14.4302 | -51.9243 | 2026-08-15 03:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c7784b84-bfab-3473-8d52-fac5a59c6dc4 | -6.6194 | -59.0609 | 2026-08-15 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 55604aba-3600-3981-833f-1d4d83facdd0 | -6.9145 | -43.6351 | 2026-08-15 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 1a7fa186-9868-33c9-a5a0-000b851d3c07 | -14.4306 | -51.9029 | 2026-08-15 03:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 5800d146-2896-349f-b089-a80e8564ff30 | -6.6013 | -59.0037 | 2026-08-15 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ba80862f-c2d3-35db-b5f5-597394065c96 | -11.4184 | -46.3506 | 2026-08-15 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| b9607a43-374f-3155-9659-e1607342beb7 | -14.4499 | -51.9004 | 2026-08-15 03:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 4122affc-70b2-39cd-abb0-d09f5600fac1 | -14.4495 | -51.9217 | 2026-08-15 03:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 3fe04ab2-57ae-3300-8d10-10293c50eb21 | -10.7282 | -50.5552 | 2026-08-15 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8d909f85-628f-3332-b8e4-20d444fe8d8d | -11.4187 | -46.328 | 2026-08-15 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f19e93ba-a2ec-341b-84d0-bfbab2214efb | -6.9334 | -43.6333 | 2026-08-15 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6cbcfdde-124d-3561-ac37-ceb44dd8e016 | -14.4306 | -51.9029 | 2026-08-15 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| f417c879-7841-3609-9564-70593aeafcc0 | -14.4302 | -51.9243 | 2026-08-15 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 31ea0222-fe26-37b2-9040-6311c03805a2 | -14.4499 | -51.9004 | 2026-08-15 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6b0b58cc-74a8-350b-b446-f05477a39221 | -14.4495 | -51.9217 | 2026-08-15 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 653a49a9-dfb6-3050-a1ef-2ba65af46b99 | -11.3996 | -46.3305 | 2026-08-15 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 9b8a160a-558b-3c3d-8832-18dafb822e4b | -6.6194 | -59.0609 | 2026-08-15 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ce73977a-e909-322b-8dc8-6e23dabda4af | -6.6194 | -59.0609 | 2026-08-15 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8597b2d6-2647-38cc-b4ec-97ab72662ccc | -6.9145 | -43.6351 | 2026-08-15 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 4466a296-136d-31d8-8247-63d314bb8335 | -14.4302 | -51.9243 | 2026-08-15 03:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 424f0f84-909d-3bff-a760-2d0a735550fb | -6.1222 | -44.0271 | 2026-08-15 03:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 2e83a024-12cd-3d08-b724-c51e1e7b949c | -14.4495 | -51.9217 | 2026-08-15 03:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f8d3036c-7e06-31b8-b983-ff7b2ab9a290 | -6.6013 | -59.0037 | 2026-08-15 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1104f895-cd59-3ad2-8efd-70e676f16562 | -14.4499 | -51.9004 | 2026-08-15 03:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| b51e2aa9-8193-3ea6-9fc8-f5cf777ac7b0 | -4.01856 | -38.25296 | 2026-08-15 03:51:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c94ede7b-32f8-31ee-8114-89b713b1744a | -4.09138 | -42.50632 | 2026-08-15 03:51:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 580fc84d-bef3-39ad-82d9-c2b55cccb3f1 | -1.58089 | -47.74979 | 2026-08-15 03:51:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a6bf8da-8563-3249-9561-18ed6ca7dd42 | -5.19442 | -35.85257 | 2026-08-15 03:51:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aec9bfc2-e814-3b59-8420-3cca7952bcee | -4.01488 | -38.25236 | 2026-08-15 03:51:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README7.md)
