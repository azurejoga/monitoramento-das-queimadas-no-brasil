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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c82d864-3fbc-3edb-8e2c-dad35d522569 | -16.36578 | -46.88383 | 2026-09-01 03:57:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 323f7c70-c3f4-3f2d-9c01-ea43d29d2fd8 | -14.38861 | -52.52972 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e8c86030-53ba-370b-9b51-7f93b853536a | -16.30558 | -42.03556 | 2026-09-01 03:57:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 968be03d-3809-35bd-820c-ab90fdbae8e3 | -14.46154 | -52.52536 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f1c4c5b1-b3ec-3341-948c-2f4da19adb38 | -14.25679 | -52.89318 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56a75e65-1bcb-3267-b2c9-d75ee7e75fd6 | -14.27073 | -52.89646 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed26efc3-6755-329c-bb3f-c808ba289dc0 | -20.16051 | -44.34881 | 2026-09-01 03:57:00 | NOAA-20 | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d28c0e89-c7ca-3fcb-8980-0bc18011700b | -19.95516 | -46.97419 | 2026-09-01 03:57:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 282c6c22-2661-3577-bf39-048d000c2b38 | -15.64284 | -50.11029 | 2026-09-01 03:57:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd043cc1-b1d6-3d56-8dfc-a7ba0fcfa126 | -14.25529 | -52.8786 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a8f239a-c7e6-391d-b2a3-8c44f0b573fa | -14.38713 | -52.53643 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 345bf9f4-aa45-312f-b973-17d4880f11da | -17.39128 | -42.35124 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 954c7f00-3757-32cf-90d4-0706a7af4a23 | -14.46286 | -52.51947 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b1c0bf6-79e8-34fc-a0bf-2db3a55c601e | -14.2631 | -52.86517 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5f27e80-a6c1-3a6a-bda6-8bfc0a13a260 | -17.37706 | -42.37038 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e6e69f3-ffd1-3ed4-bd0a-81839e13b4d2 | -15.67004 | -45.91505 | 2026-09-01 03:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98c75a4c-d86c-3f7e-8d15-6ee23ec03b09 | -15.06048 | -47.99237 | 2026-09-01 03:57:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f5d8b50-288f-309d-b1bf-a0580462a9c3 | -14.99949 | -48.15844 | 2026-09-01 03:57:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25235ca3-e617-3e2e-b9c9-54e210782011 | -14.45627 | -52.51688 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1138fa3-4948-37f4-a6d7-b5d22b80d340 | -15.01718 | -52.77107 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65ab4635-52c3-32d7-9609-d6dcdc05049d | -7.571 | -60.4643 | 2026-09-01 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5232706f-aa73-32b2-b5d3-e6d6c9d0a6f0 | -6.3722 | -51.7693 | 2026-09-01 04:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b7d5db1c-6dee-37d1-8b96-272813762391 | -16.0547 | -54.3908 | 2026-09-01 04:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 49093293-d870-395e-a3d0-e278f0d9ec8e | -7.5709 | -60.4835 | 2026-09-01 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 039558d4-a9aa-39af-bb30-e84f398ac30b | -7.5895 | -60.4636 | 2026-09-01 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| a8a6771f-8de0-33e3-897a-ce2887c5c1c8 | -6.3723 | -51.7486 | 2026-09-01 04:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 525d7d2e-7909-335c-9a9c-e3d6f8dd5048 | -8.279 | -54.9174 | 2026-09-01 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b0d9b975-628e-3315-acb3-9cc36b765c69 | -8.2788 | -54.9376 | 2026-09-01 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 2880d532-c167-34f2-b8ab-a01de906424e | -8.279 | -54.9174 | 2026-09-01 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| d4ea1d83-f676-3846-a48f-4db7024c9cf7 | -6.6036 | -58.5972 | 2026-09-01 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| ae1c3cdc-a652-3238-b31b-0090c001e003 | -8.279 | -54.9174 | 2026-09-01 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 508431b2-4c99-31a4-8492-64b59e749445 | -8.2603 | -54.9186 | 2026-09-01 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 99a84b86-7fad-388c-9a3e-a5485f195d02 | -8.2788 | -54.9376 | 2026-09-01 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| bb1c9e7b-2f62-373d-9682-81c55576773a | 3.80459 | -51.8847 | 2026-09-01 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 14c9ad20-76d1-38a3-8b0e-6516e6a11ed7 | -1.44464 | -54.22796 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a69d01cd-af91-3675-bece-157380aeef2c | -1.96468 | -48.37855 | 2026-09-01 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b6922a2-cde8-36c2-94c7-63154f8aa3d9 | -2.71783 | -47.05767 | 2026-09-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16726b34-2eae-3ab5-aabc-ce15c9f4f2bf | -2.49956 | -48.13377 | 2026-09-01 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9c33ac5-75a5-3cef-82c3-ea133ea69a07 | -1.0355 | -47.55473 | 2026-09-01 04:38:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4827ca0d-c585-36ea-aebb-b64be86be652 | -3.8583 | -44.0437 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23923751-b0e8-3af9-a55c-2fad9da1b449 | -3.85372 | -44.07512 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65afc8ac-48d3-36ea-96c7-f96c0007422d | -3.86573 | -44.077 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f673eb74-0692-3fcb-880a-49ee0db96b13 | -3.85679 | -44.04388 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5522cc5e-55dc-3555-843b-28e0c1f30684 | -1.46882 | -54.21219 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90c64a1c-b92b-3a1f-a0a5-92cccfd519b5 | -3.87333 | -44.0532 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75188218-6af9-3427-8c96-94e6d72be0de | -4.32155 | -45.23271 | 2026-09-01 04:38:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0af33d51-877a-3614-b7d4-47f7bf1bbf18 | -4.36804 | -47.77284 | 2026-09-01 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ffd765bf-faaa-3059-a9e4-db1b24b6ebca | -3.86173 | -44.07637 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f70e3231-b4b2-3e9f-b193-23779d01ea0f | -2.74066 | -49.29203 | 2026-09-01 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52e55045-211e-3411-bb85-9c5bdea791f7 | -4.08806 | -38.65597 | 2026-09-01 04:38:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 948a3fcc-200d-3b33-ad31-ca9ce14afd6f | -3.87785 | -44.05036 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2dbb125-441b-30e7-9028-3d8c012e7658 | -3.53463 | -48.45408 | 2026-09-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e58d241-3b7c-3a56-b717-52e22473ad33 | 0.97699 | -59.39813 | 2026-09-01 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7b7cd039-d7e5-328f-90e5-fa8ab3ed1234 | -3.87025 | -44.07412 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd5493ce-1b7a-3105-9b95-7212e6d71ab9 | -3.86625 | -44.0735 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25a7069e-94cd-3f80-97fc-97a3e87c63ad | -3.86684 | -44.04142 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9ada4b9-499f-33a7-b113-fea491f0ddf9 | -3.86983 | -44.04908 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f63c29ca-ae40-39ec-b18c-de204c46bb7f | 0.91141 | -51.9914 | 2026-09-01 04:38:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edc3a65a-cb32-3455-bf9a-01cbb0b19ff3 | -3.78556 | -52.40758 | 2026-09-01 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 372d116b-1c01-320d-a1fa-0d201b93a6a2 | -3.86122 | -44.07985 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df1618d6-45a5-365f-b432-9c69cb4b2b6c | -4.77226 | -41.79767 | 2026-09-01 04:38:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6399e7f2-20ac-3680-b278-df8792b59180 | -3.05365 | -39.92869 | 2026-09-01 04:38:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b75bc894-a307-380e-83e2-e2037b921975 | -3.87077 | -44.0706 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 04ed8a8a-8d69-36a8-a481-b9774e9b1b8b | -1.47119 | -54.22462 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 964cb36a-1ebf-30d8-b7ed-7df65d43cec3 | -2.55267 | -48.16316 | 2026-09-01 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf266b73-4874-3f73-88b8-1eeb66613236 | -1.46452 | -54.23935 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 51ac5869-fd07-367d-ab8f-4e12b8f615f7 | -3.85412 | -44.06132 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f195304a-bb1b-32ac-a5a0-da6c2c6615e7 | -1.44836 | -54.20468 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4059bcb9-11c6-308c-b7d5-51d8241beb44 | -2.89626 | -48.2732 | 2026-09-01 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c55f08-ca0b-32a8-965d-6889dcfa8125 | -1.47419 | -54.23308 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18124145-ea2f-3a64-9d4c-dc505ffcba7d | -1.7783 | -53.49798 | 2026-09-01 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0747052-4218-34af-b179-4c2a083cf135 | -1.46997 | -54.23233 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f03ef605-4e3f-30b8-95dc-a40ed938c3a5 | -3.856 | -44.07581 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22cfb5f0-0593-3686-8c92-261fbc458385 | -4.77154 | -41.80272 | 2026-09-01 04:38:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4dd5bfc5-97e0-3c83-b086-1c0b200f13ed | -2.80093 | -49.57897 | 2026-09-01 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf45c6d2-24cd-3569-a402-cc5084ad8e78 | -3.85653 | -44.07231 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b78ae77-5174-37e3-ad3c-82e85f047a05 | -1.96138 | -48.37804 | 2026-09-01 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccfbe988-16a7-353f-80a6-a67e95d5435e | 2.51736 | -50.85103 | 2026-09-01 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5834a22c-64b7-35d6-b658-8ec3cd5d3afb | 0.97549 | -59.38845 | 2026-09-01 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea88a806-7b43-38fe-90c6-7f6fa8a411c6 | -3.87281 | -44.05667 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 414b47de-97f8-3a88-8d72-bd333a6ddc5c | -3.18651 | -48.02375 | 2026-09-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 048c11ed-2891-3ef9-942b-46c05fb56608 | -1.85497 | -50.67648 | 2026-09-01 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 265d9dfe-6db3-3dbf-b2ca-87091a3688d8 | -3.85525 | -44.06464 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2af225fd-6818-3cfb-afa8-222766c737a9 | -3.15848 | -48.07285 | 2026-09-01 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6a5e089-40ff-394b-9024-86a83d16c525 | -2.91463 | -54.11778 | 2026-09-01 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92673a9a-bf98-3f87-8ced-5d35d13f836b | 0.01151 | -60.59869 | 2026-09-01 04:38:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9eaa02d3-7b7d-3c04-b8f6-0dd921018858 | -1.5864 | -50.44124 | 2026-09-01 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9113c36-e019-3449-9459-c22d0f65bff2 | -4.28223 | -48.19337 | 2026-09-01 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5965c695-ceab-3fd0-997d-048a37ddcce2 | -3.8607 | -44.08339 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 545b0cee-cc87-31ee-8f78-248e62e02e48 | -1.58982 | -50.44176 | 2026-09-01 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0b3cbea-ac4c-3e02-88d1-4e1428328540 | -2.40173 | -48.17179 | 2026-09-01 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8abd7d08-38bc-3b6b-a09b-a92e3dbc8111 | -2.00273 | -54.31806 | 2026-09-01 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae6466b7-0428-3453-85f5-92bcb0553857 | -3.86922 | -44.08114 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46bf2fbc-0072-3e5a-8591-0d82b9c7de39 | -2.53976 | -48.24597 | 2026-09-01 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfe83fcf-f985-3630-b825-d107ba6df024 | -2.79706 | -49.58194 | 2026-09-01 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecb4649c-4891-34d9-9402-f2ffc7e48163 | -2.26498 | -47.87014 | 2026-09-01 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1d27141-88eb-31f4-97f9-8d66ab93f330 | -3.48615 | -50.59057 | 2026-09-01 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddfca294-f81d-3e37-a01e-995f4782d39f | -3.85625 | -44.04743 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26a87293-e1ce-30c4-85ad-7eedb3700312 | -2.38812 | -47.60281 | 2026-09-01 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42384fc2-fe86-37fd-8a53-32227d897b65 | -3.85474 | -44.06811 | 2026-09-01 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README30.md)
