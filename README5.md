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
| 0a750969-d96d-3f74-bee5-d0a6790de751 | -3.19482 | -41.85258 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| e35b3694-0d8e-3fbf-af04-708410ced1dd | -7.54709 | -35.23491 | 2025-12-13 03:40:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5b7cf455-8e0a-3437-ab46-5eb76f07624d | -5.18285 | -40.15318 | 2025-12-13 03:40:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c64cc50a-1456-3cd6-8003-1035df3f44f2 | -3.20427 | -41.86091 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ebf0d525-754f-3f3e-9d80-02856147c1c2 | -3.19955 | -41.85671 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 0e3a141d-a3ac-3ca4-a3a1-13e33c119b4f | -7.79002 | -40.43251 | 2025-12-13 03:40:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f51b8f85-4fef-3eb7-bd48-47464f4a5d18 | -5.07433 | -43.67307 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c39b14c-29b7-3917-baea-34af84f6f42c | -7.06833 | -34.94926 | 2025-12-13 03:40:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ae70806-af22-3fb1-a1c6-5fdd6ef24e32 | -1.90642 | -45.47215 | 2025-12-13 03:40:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e9d9eb69-bab7-3f2c-839c-6b2d66c58cc4 | -5.07484 | -43.67095 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 508be538-2141-3a04-9039-1929ccae842f | -8.59281 | -39.44376 | 2025-12-13 03:40:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eaad0782-f6cf-3812-b6b4-80eaa35af6f8 | -5.06909 | -43.66986 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc3409ca-b397-3d0b-8121-97622021551f | -5.26808 | -37.90829 | 2025-12-13 03:40:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ffa70bef-ec9c-32a9-a370-8f8eb1a9450e | -2.99219 | -40.18968 | 2025-12-13 03:40:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f172e190-35f6-3e12-9ba8-bbf6cbccc884 | -5.40507 | -37.66125 | 2025-12-13 03:40:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4afb9a02-afda-362d-80ca-d4089e4fe912 | -7.14743 | -35.09002 | 2025-12-13 03:40:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 102d88c7-6fc3-3653-b18e-8d6f9680dd2d | -3.19535 | -41.84938 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f87f4251-ba44-3ea2-ace8-36d5ee8a26ff | -3.19845 | -41.8633 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d14b9e9f-a003-3269-8bba-fc6775bf5e88 | -5.0693 | -43.66798 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab9e76b3-3b83-372c-bf99-4f8a961585ef | -7.19722 | -40.10563 | 2025-12-13 03:40:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 52e31080-2b93-3b2b-8042-b4cd20ca7127 | -3.199 | -41.86 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 0c038133-89a1-3a31-ae88-58250b9cf518 | -5.36754 | -35.54954 | 2025-12-13 03:40:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1bc0ab67-8f3f-3894-af60-8867fd191562 | -8.86812 | -36.33409 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 29809d55-768b-3d80-a55e-18b50fbf7202 | -5.01864 | -39.71541 | 2025-12-13 03:40:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c9e6e8e1-7411-3d3b-8c86-f464450b46fb | -3.19372 | -41.85916 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 77919418-3c3c-3a4a-a574-e45e18be9a3f | -3.21003 | -41.85884 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 46eff505-7907-3e5e-a7a1-9f166f971edf | -7.19793 | -40.10335 | 2025-12-13 03:40:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e0c3465-c42f-3019-b6ac-74fb281b5d5d | -7.92898 | -38.19706 | 2025-12-13 03:40:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9ce9528-b68d-3d66-8c63-5060af2825b7 | -3.20115 | -41.8471 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8886781-1791-3940-bbd2-412b4e087300 | -7.63829 | -34.85865 | 2025-12-13 03:40:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3d51b6ea-b555-3938-b3d2-8b128ec9ff6d | -4.33483 | -39.14848 | 2025-12-13 03:40:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9f9a5206-421f-332e-b673-5f96aee5cea7 | -6.78457 | -39.62656 | 2025-12-13 03:40:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fc742f5b-a1b4-3406-bfcc-90d9c0304cf2 | -3.18954 | -41.85176 | 2025-12-13 03:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2849a25c-d0d5-3c98-be9c-3cfa241ec774 | -6.7442 | -39.66726 | 2025-12-13 03:40:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e6d2fb5b-881d-3ce3-9f64-2990140e2610 | -8.75092 | -39.81055 | 2025-12-13 03:40:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65cfbe64-5349-3a5b-a09e-ddaa2ae4b8c5 | -2.79568 | -45.21087 | 2025-12-13 03:40:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e9ce587-e4c1-37c3-85b4-57b0943a3453 | -7.21953 | -43.11369 | 2025-12-13 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d80ac7a6-8569-3008-844d-7ed1a144f633 | -7.63495 | -34.85813 | 2025-12-13 03:40:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 399ad7d7-eb76-3c60-aac8-bc0938e4ea3b | -5.07933 | -43.67837 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfae5d65-9c4f-3fe2-b628-f07538bd221f | -7.23463 | -43.10592 | 2025-12-13 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e691549f-ca95-3aad-a261-234d473ded82 | -7.38618 | -35.21625 | 2025-12-13 03:40:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 121d1d3a-65f1-3db5-bc57-4d6daffa7455 | -6.56571 | -39.51515 | 2025-12-13 03:40:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 430a51dd-e002-36b6-85f6-0e5aca397587 | -5.07917 | -43.68034 | 2025-12-13 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66263c83-3c1c-35b2-9f11-6d9a1a4f8a5b | -2.66556 | -46.8945 | 2025-12-13 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36c67890-9ad9-3d84-9854-eea32b844b65 | -7.9818 | -41.4325 | 2025-12-13 03:40:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 827a3cae-bc31-3ef5-a3c5-2459c12d2827 | -5.54605 | -41.65434 | 2025-12-13 03:40:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 330e2d81-3465-33aa-93db-3257606db97a | -10.37578 | -45.05151 | 2025-12-13 03:42:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab90c31a-b3e1-3ee0-b7c5-3533aec28c9b | -10.15238 | -36.19744 | 2025-12-13 03:42:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 61afdb75-4970-35e3-8eef-65dc0e1609d2 | -14.07433 | -39.47645 | 2025-12-13 03:42:00 | NPP-375D | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c08a2fd7-9b89-385d-a59d-a076c44a75f4 | -10.29373 | -37.80765 | 2025-12-13 03:42:00 | NPP-375D | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eb990ac4-8b9d-3278-818a-c598d6a41fe6 | -10.15298 | -36.19374 | 2025-12-13 03:42:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| ba1155f1-185f-3935-a799-b19dd7503e50 | -10.36928 | -45.05431 | 2025-12-13 03:42:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5f02fb7-0483-3a5d-a41e-fbc1a3b1decf | -12.27192 | -38.41735 | 2025-12-13 03:42:00 | NPP-375D | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ec4c4e64-3c1e-3a4a-a071-32433b0d06fd | -8.40971 | -44.04234 | 2025-12-13 03:42:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ac531ea-e64b-34f9-989a-021b3a2a0772 | -12.27267 | -38.413 | 2025-12-13 03:42:00 | NPP-375D | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 93e53771-dec1-3216-8382-b152f02ffe1c | -10.15578 | -36.19801 | 2025-12-13 03:42:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| eada4002-be44-3951-b2da-f3d7866c2ea2 | -10.15639 | -36.19431 | 2025-12-13 03:42:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c8e8c052-7762-38f1-afbd-ed2b41182cd0 | -12.31463 | -37.92308 | 2025-12-13 03:42:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dd7ab9bc-cced-3af1-bc11-5089fa47458c | -12.8747 | -38.34907 | 2025-12-13 03:42:00 | NPP-375D | LAURO DE FREITAS | BAHIA | Brasil | 2919207 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| faab759f-409f-33bc-a28d-22b09241eb45 | -10.14958 | -36.19319 | 2025-12-13 03:42:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 1565521d-d570-3b4f-8cdb-f9b5d091cf25 | -10.37502 | -45.0555 | 2025-12-13 03:42:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85d171f2-1be2-398d-ad1a-3e956b4c8601 | -3.2007 | -41.8678 | 2025-12-13 03:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 38316490-b519-3233-9991-91c3b9d39bb4 | -3.1822 | -41.8448 | 2025-12-13 03:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| cbb5d496-ef04-3067-91c0-2c41178f64ff | -8.0321 | -43.1257 | 2025-12-13 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 9cf21096-9f38-35bd-b047-80d061ba6c8f | -3.6932 | -43.9517 | 2025-12-13 03:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f4ea575d-8d7c-38fd-bcb4-4be2ac1ef41c | -8.0513 | -43.1001 | 2025-12-13 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 395e3c13-35c4-32a2-bd0c-280523da5f75 | -3.6747 | -43.9296 | 2025-12-13 03:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| eaaddd34-06e0-3809-8304-2c96860184ee | -3.6746 | -43.9526 | 2025-12-13 03:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 9158e2dc-5070-3def-b70b-7e7b52bba146 | -3.2009 | -41.844 | 2025-12-13 03:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 77ad3fbe-0a5d-3eb3-a400-c9b70f49101c | -3.2194 | -41.867 | 2025-12-13 03:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| dc0e58e1-2b32-3aba-bd9d-74a39dca7bca | -3.2196 | -41.8431 | 2025-12-13 03:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 05c63ed1-b238-3ea1-92ee-a3ea4d4ffc5f | -3.6933 | -43.9287 | 2025-12-13 03:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 3ce28f8c-17f7-3f58-9d68-896efe27b10b | -8.0324 | -43.1022 | 2025-12-13 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| 2c930ae0-bb6a-35f4-82ad-7aab0660d05e | -3.182 | -41.8687 | 2025-12-13 03:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 42007207-aabf-3e82-a024-27d963ef1432 | -3.19169 | -41.85094 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8de4315c-6fb0-37c4-b3ae-267ea2ecc7a2 | -2.63916 | -44.87751 | 2025-12-13 03:59:00 | NOAA-20 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d13b9454-50ec-3a7a-b652-1d7a1cb511fb | -3.20857 | -41.85768 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 376bba3b-59b5-36b2-a8ef-740941eaf8de | -2.82361 | -45.25641 | 2025-12-13 03:59:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95e1838c-580f-3277-8daf-56f5320a26e5 | -3.44997 | -44.73459 | 2025-12-13 03:59:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fffad192-405e-3dcb-8b14-bf6024de5631 | -2.51167 | -47.81057 | 2025-12-13 03:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb896b9f-12c0-373f-a5d1-8c376eec1088 | -3.20157 | -41.8565 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 8caaf513-6c61-3ca9-bdc6-73e3a45783bb | -3.43409 | -41.65141 | 2025-12-13 03:59:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b0543a20-2c59-3975-a240-6d32d7721e4f | -1.89298 | -45.42783 | 2025-12-13 03:59:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a44d9f15-5857-3f3f-9639-68821dde3d3f | -2.81863 | -45.25978 | 2025-12-13 03:59:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c021e0a-7456-3dff-9c0e-764e245d2783 | -2.81432 | -45.25911 | 2025-12-13 03:59:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f132af9-19ac-3c32-a875-55c1b2f0dd8d | -3.79991 | -42.79318 | 2025-12-13 03:59:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a820400-6e60-3438-8e0f-853d2f3872fd | -2.4193 | -45.06295 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a06f441-6f6d-323d-9f38-92b7c88a2dc5 | -2.41973 | -46.15632 | 2025-12-13 03:59:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0772a59d-181a-3e57-bb7a-8756307b3f78 | -3.20282 | -41.84872 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| eab2f752-6d52-3589-b66e-5ea64b6418d4 | -2.66863 | -46.89448 | 2025-12-13 03:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a9ebd842-ba97-3cee-ad05-1944eb1faf84 | -2.82129 | -45.25679 | 2025-12-13 03:59:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0d0c6d3-2181-3303-932b-e91423a1520e | -2.7891 | -45.20974 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b61dcd18-9d09-37d9-abb5-2023c8921b16 | -3.95588 | -41.52745 | 2025-12-13 03:59:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6b642e26-e85d-34f5-bc63-8a6305349564 | -2.7934 | -45.21046 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b2e7e09-ee35-302f-8b51-93af87d0cd4e | -2.57475 | -45.06085 | 2025-12-13 03:59:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab6f6fb8-7451-38a4-b5e7-8cdc83590fef | -3.58637 | -41.66712 | 2025-12-13 03:59:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f4e21b9e-47c1-3a2a-a43f-3cac528eebb0 | -3.70177 | -38.66527 | 2025-12-13 03:59:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20b50d3b-a6cc-3e2f-86f9-96bea20dece5 | -3.20982 | -41.84986 | 2025-12-13 03:59:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 039f0ec2-b68b-3f69-9ff2-3042f27b4936 | -2.78845 | -45.21378 | 2025-12-13 03:59:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38520c83-40a8-3a30-9e95-b0b984897caf | -1.90821 | -45.47491 | 2025-12-13 03:59:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README6.md)
