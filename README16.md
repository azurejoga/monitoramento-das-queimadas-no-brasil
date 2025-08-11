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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c5ff286-4757-37e0-8549-18da6e65b8d5 | -8.5663 | -54.70914 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56ea663f-0ce1-3c5f-8cd7-113530112e07 | -6.58996 | -44.55351 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3b570c08-d873-3114-9117-e988c7156fa4 | -7.06173 | -59.19876 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24219629-8058-3ca6-b509-7756a1a94c8f | -10.37124 | -50.8219 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31c9f931-e2dc-336f-9962-579c0e0f48ca | -4.29471 | -48.05904 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c48bfc41-918e-3664-8797-fee564d163e4 | -8.5663 | -54.67289 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e14f489-7acd-3a4c-8def-5c5f4fd510e2 | -8.55943 | -54.69131 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 826312cc-b903-37ae-bb3c-f11e3661bf68 | -7.06062 | -59.20472 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ec3f961-a082-325e-ba5f-8afbd221ba74 | -6.58598 | -44.5567 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 14985795-e7f5-3f9c-8b30-4fcfd7943eb7 | -8.3015 | -44.99125 | 2025-08-11 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02ba5e9f-e5d8-3841-a174-958d11ecb92d | -4.11116 | -48.20235 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b7d4e61-6263-37f3-aa68-e81b5bfa8514 | -8.13035 | -47.4315 | 2025-08-11 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8d67e5b-8143-3979-98d1-46289bd8eab7 | -10.62067 | -46.12463 | 2025-08-11 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b3cb077-bb0b-3343-8a47-0718aa51db82 | -7.05621 | -59.19166 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c71d695-5367-361a-9d62-c43a9f1c8daf | -6.57897 | -42.77275 | 2025-08-11 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 93a21341-33e5-3206-925b-affc08ba04f9 | -8.56818 | -54.69839 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a2ac9c2a-fee2-33b4-a4d9-4230772f82b3 | -9.80632 | -45.95016 | 2025-08-11 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62b4c9b6-b323-316b-835e-4d8cd495dc06 | -7.21963 | -46.25093 | 2025-08-11 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 197d0fef-9641-38b0-99df-5dc29cfe2eae | -7.05839 | -59.21669 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 50e48f66-adab-3dda-b3a3-64e8ec5b2c7e | -7.07868 | -59.20517 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 991f1c18-d951-3783-9a09-a40db2315fca | -4.80845 | -48.37607 | 2025-08-11 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f76a209d-ffac-36b3-bd4d-d03872097f5f | -6.65079 | -47.39999 | 2025-08-11 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09ac8796-4d61-3238-9ad8-5e19fee92292 | -10.37345 | -50.80882 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e37c04dd-4150-37f4-8eda-8caa4829bb7b | -9.19866 | -59.67813 | 2025-08-11 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 644d18cf-5e7d-3f4c-a0d2-4ceb7bd297f6 | -5.48285 | -44.39437 | 2025-08-11 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 0564de97-3b2a-3b02-9ffb-4af7a0d66680 | -7.61466 | -45.198 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a563fb1-0d5d-3779-ac42-6edf66bf5f00 | -11.36312 | -41.59423 | 2025-08-11 04:25:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a8f4562-c110-3ad4-a3f6-5e93b1275402 | -7.43301 | -43.76089 | 2025-08-11 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91c4e9e5-5170-3cf5-a0db-bab07212440e | -7.26195 | -45.37072 | 2025-08-11 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02f025a9-ddbe-3961-863d-a72cc52601ba | -8.5634 | -54.68875 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a08abfe3-7672-35f1-abc4-5ca9e94b18c1 | -9.20837 | -44.52644 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de765c48-716a-3835-8bbd-952b9ca140cd | -6.57972 | -44.55194 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b45c5aa-30a0-373b-8d4b-adb3e400fb2c | -7.26251 | -45.36716 | 2025-08-11 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53cee590-6cf0-3cdd-b48d-05c2a17c98b5 | -7.85482 | -47.24054 | 2025-08-11 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f9bf964-8682-3b5b-9dc8-f9ace2002a29 | -6.92579 | -42.92117 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 22881a85-4532-3b9c-a107-89c2c35496a2 | -8.56145 | -54.70826 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 75f3d8ca-286b-3e94-9be8-c8ecc9874182 | -7.35047 | -44.59367 | 2025-08-11 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baae90d1-8ba2-3280-b63e-69fe363494b2 | -11.77623 | -44.94404 | 2025-08-11 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d190aa4a-6a6d-30a8-b1e6-38173d0490e1 | -8.56521 | -54.68682 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d9bb020-f1fa-3e9b-be8f-fa93213d24f2 | -4.29127 | -48.05846 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 456da305-7906-3a18-b7a7-5cccefbefb16 | -6.97525 | -43.09227 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c22fb0d-3ecf-3ac2-8148-2d2b72c9daaa | -7.13269 | -44.21363 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22304e10-2a6a-38c7-86c2-a83792c6870f | -5.48342 | -44.3907 | 2025-08-11 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d59f715c-2a69-374a-93e5-e6412dc7b9de | -8.57111 | -54.70121 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47176ad2-b422-33bf-b025-2c121246780e | -7.21741 | -46.24349 | 2025-08-11 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 877d9c9b-b3fd-35f7-84a6-84b5ffae8464 | -9.21536 | -44.52753 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 992ae610-b97c-3cb0-81a6-6293c896d9c9 | -9.3011 | -40.21983 | 2025-08-11 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| aaecf698-9ac7-3f44-bd9d-3b1c962976d6 | -8.56529 | -54.70569 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28d0d286-65c7-3249-b78a-0c13ace43fc3 | -7.61915 | -45.1913 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c210c681-7b59-3bb2-a02c-5285188cfd56 | -9.86824 | -44.70222 | 2025-08-11 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3027eca-8dca-32f8-afe3-8db371b9780b | -7.16406 | -44.27644 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58f47579-80d0-3f77-ad51-cc5602a0bcf5 | -4.77782 | -42.7219 | 2025-08-11 04:25:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2ce75ee-b979-32d6-8fb9-0328ea26bbe9 | -7.12654 | -43.49829 | 2025-08-11 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 225d2236-e54a-3e4c-a2d7-2a48acd31517 | -6.58542 | -44.56039 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6198821a-19eb-35ac-b03f-74c1b517ed17 | -6.92515 | -42.92555 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1168d77e-777a-3999-a54e-b30d2c703efe | -10.3705 | -50.82625 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c5bba6d-9e29-3298-a7fc-2a8f8125a397 | -3.42989 | -49.0475 | 2025-08-11 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7b50702a-cc20-329e-8cfe-3de2e43ec5a6 | -8.56823 | -54.68964 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 98470f6b-9dd1-3b36-a98c-5bed7b423d2a | -8.57207 | -54.70468 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e410c7b-9fa6-39fb-8c21-cafa178a6a47 | -7.0683 | -59.20024 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e39510eb-a7ac-35df-8fe9-141dc9b5dd75 | -10.37198 | -50.81754 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4b6794d-aebb-3ec3-9fb9-2c6f509d52b2 | -4.06106 | -46.93177 | 2025-08-11 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ae19fef-db1c-348f-843a-36c76e6f8c5d | -8.57014 | -54.70655 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 618e9507-2aeb-399f-a609-8a4927f90f72 | -9.21069 | -44.53478 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5992e56e-7f0f-31ea-a85c-4b0b84b283c4 | -7.06696 | -59.17076 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe9546a9-44de-3eb5-a2b2-6901e6de2e7d | -4.2941 | -48.06282 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3072908a-aa2b-3b8c-b95d-bbba18731fe6 | -10.3587 | -46.63257 | 2025-08-11 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d8a3857-b4de-3054-8c58-d0e1f889b643 | -7.07359 | -59.17182 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f77eeafa-5e1d-39fa-a902-202dbb54c9ea | -6.96403 | -44.21155 | 2025-08-11 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9f1ee1e-3445-3031-89c3-0b469335d417 | -8.57402 | -54.68525 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f63dc8f-41d7-338a-b4cc-9fdd24dc5110 | -7.12629 | -44.23215 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e70170b-fc79-3dda-94d0-ca6f97c506d9 | -6.58314 | -44.55247 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 321967ec-db42-3e3d-b4c2-2cff07000056 | -8.08107 | -46.86329 | 2025-08-11 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4590e510-ef62-3ae3-b7a2-19c37db34ddd | -4.07039 | -47.97015 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 564eab21-ac54-3cc6-a31f-8c7ee85c6903 | -7.07149 | -59.18309 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f58fdf0-c42a-3edb-a303-382008fdd91c | -5.08847 | -46.17236 | 2025-08-11 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4dc55df-186f-327e-a5d6-a04d5c6a90bd | -10.30523 | -48.11106 | 2025-08-11 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bc2c383-fb0b-3845-800a-009ba760b802 | -7.08359 | -59.19161 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37e19722-3cc6-3f54-ab64-f4fcd01a5b10 | -7.07044 | -59.18875 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f98bc661-d390-319f-a9d6-2e3c31fda0fa | -10.62765 | -44.74665 | 2025-08-11 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f56b6116-6890-39ed-882a-25a79d5d6164 | -8.56628 | -54.70033 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31d3bafc-24d7-3b97-91db-d284efa1e831 | -7.17155 | -44.27381 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 885d7758-c2fd-3b5c-a38f-95bdfff669a4 | -7.25351 | -59.99847 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5563593e-7ef9-3607-8d8f-c67dca69545e | -10.36905 | -50.81253 | 2025-08-11 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 46ee460e-3423-3296-b826-ac9abfdec050 | -10.42081 | -46.251 | 2025-08-11 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fdd9910-2e83-322d-9244-1bb0f7b72f69 | -8.78713 | -48.35302 | 2025-08-11 04:25:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 323905f1-d214-3534-a6ec-2bc15fbcb03c | -8.56223 | -54.67536 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7093c332-eb07-39c9-b149-1558d24b3585 | -8.57487 | -54.68863 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c310b8e-cb3b-38b7-a046-3352059e31ba | -10.41823 | -46.25045 | 2025-08-11 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c615cc4-31d4-314a-80e5-b754d057d723 | -7.13035 | -44.22884 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0e0d1b7-3a05-3da7-8643-d0e61eb200f2 | -10.30912 | -48.10811 | 2025-08-11 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b0d933c-58a5-3d2b-a929-897c8f0cee75 | -7.05828 | -59.18061 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3d5a6a6-abff-32b4-ad41-184fee51a431 | -4.0644 | -46.9323 | 2025-08-11 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| bed01127-31f0-3182-ad2f-612d868c98b7 | -9.21595 | -44.52359 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ccf004c0-bfa3-36a2-b607-68af2bcf12be | -6.58485 | -44.56408 | 2025-08-11 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09dc2cb5-a28f-39e7-8ebc-5f7d925ec508 | -7.07485 | -59.20181 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 44a51886-4ba7-3793-a2fe-37e791239b10 | -6.9716 | -43.09169 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57e73c8c-cad8-37ad-9a11-fc517b1c6b10 | -7.06939 | -59.19437 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c642efb-734c-30d7-b704-67a2e7fb9f73 | -4.11403 | -48.20676 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e1b6b37-e344-33fc-839a-bd993e7dcf87 | -7.61074 | -45.20107 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
