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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f280555-5b67-3ca9-a7fa-7ed8d13fe0ad | -6.97926 | -40.00583 | 2025-01-04 04:29:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 82133ac0-e3c8-3dce-93b8-f33d152ddade | -8.30645 | -38.76468 | 2025-01-04 04:29:00 | NOAA-20 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c82777dc-a6a8-3cf9-a472-3c57278d402a | -4.16199 | -42.02727 | 2025-01-04 04:29:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fa659edf-331c-30b9-83da-db4e7cb76092 | -2.4543 | -48.90672 | 2025-01-04 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9678f0db-06d5-30f0-ab87-1ce1863c59a9 | -2.44562 | -49.02764 | 2025-01-04 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c79937af-d093-3e14-9e33-12e96b957549 | -1.99547 | -46.52468 | 2025-01-04 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eb87ab8-ef4e-3f73-98e4-559dd9f676cb | -6.70869 | -44.31799 | 2025-01-04 04:29:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dadb6eb6-61e2-34ad-84c7-10f07ac9bdef | -5.71327 | -41.41179 | 2025-01-04 04:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ddb0815f-05b7-3551-8050-fe769363e05a | -4.00475 | -40.93283 | 2025-01-04 04:29:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bde42990-fd00-3dcd-a796-3ff1174b9524 | -1.99216 | -46.52417 | 2025-01-04 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0d70daf-f811-3f30-9e4c-8751a5a64782 | -6.98335 | -40.01237 | 2025-01-04 04:29:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d5b3a193-85f8-3520-a9c3-7407eef0c394 | -2.96202 | -41.8544 | 2025-01-04 04:29:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2423198f-637a-3308-85a3-a6b5127ba671 | -5.16728 | -40.76423 | 2025-01-04 04:29:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ead066ec-fd67-3c7c-8ddc-4d4101aed450 | -5.98821 | -45.3913 | 2025-01-04 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 520d48d1-cdcf-351a-ad3f-12ec72f21c8f | -5.50356 | -44.82734 | 2025-01-04 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b1b2f60-ba62-312d-a34a-0d277fbc51b4 | -5.91452 | -48.07999 | 2025-01-04 04:29:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e0919af-def9-3101-8f6b-0696f39ecede | -4.23625 | -53.4931 | 2025-01-04 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05a71576-9eb9-3cfe-b291-239ce4b82973 | -6.12214 | -42.53971 | 2025-01-04 04:29:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6fb8538a-b77f-3aed-ab92-ec96b48a6b01 | -7.2155 | -38.6371 | 2025-01-04 04:29:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c7d89476-dfd1-3514-9242-cb50d0cda185 | -2.44906 | -49.02818 | 2025-01-04 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a5fa7ac-2cae-3231-930d-6b3d0b0437bd | -6.97845 | -40.01151 | 2025-01-04 04:29:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7057eb1d-7320-3c00-b6cd-6b77a226b03b | -5.49793 | -44.30035 | 2025-01-04 04:29:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f0670df-b33f-34f6-9498-fa1059019f77 | -5.41238 | -46.86654 | 2025-01-04 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd50a5b2-6f73-35be-9ea5-ace320b71b61 | -5.50223 | -44.29662 | 2025-01-04 04:29:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8840c34a-43b7-3abf-b848-cd4609f59af3 | -6.31934 | -47.42857 | 2025-01-04 04:29:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 31db6e8a-c4c8-3949-b558-27dd27dca426 | -7.21504 | -38.64031 | 2025-01-04 04:29:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| acdb5f61-fa1c-376d-b172-e75b4d51e913 | -9.8923 | -36.2668 | 2025-01-04 04:30:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| e99c8ec8-5700-3626-ba78-05439081957a | -10.6124 | -44.3517 | 2025-01-04 04:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| f869529e-05da-30ed-9056-bb7390acfcde | 1.34 | -60.3122 | 2025-01-04 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.4 |
| dbaa3939-5a66-32f8-aa82-e773b4c68d27 | 1.3401 | -60.2932 | 2025-01-04 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9f2ac8b7-4021-3086-bc76-cace4d535652 | -10.6128 | -44.3284 | 2025-01-04 04:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 7b593622-4e66-3d40-87e2-d13aed865a4c | -10.61027 | -44.34547 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 3950da97-4365-3d0c-ab91-71ceb6cea376 | -9.8921 | -36.272 | 2025-01-04 04:31:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e03ab474-ebb7-3859-b50d-a12b5c26d5c5 | -10.60639 | -44.34491 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 1bd0844e-60c6-3978-994b-1001a30b653f | -9.84945 | -37.12612 | 2025-01-04 04:31:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 16.1 |
| f2f0eb63-73d6-3073-ab68-cab373a0f40b | -10.61188 | -44.34237 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 272bc7b9-a5ae-3e39-9cd2-8aedd9f86540 | -10.61242 | -44.33081 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e2279ba4-e517-38d9-ab64-bdda68940ad8 | -11.50768 | -49.07189 | 2025-01-04 04:31:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11d8d09e-813e-3035-8c69-06d7f4869471 | -10.62358 | -49.03635 | 2025-01-04 04:31:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d879ca28-5eb2-3960-bd1a-c931796b4eb4 | -8.83822 | -49.8983 | 2025-01-04 04:31:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6f25ec2-52e1-3bf3-8652-f940f04cca43 | -10.60868 | -44.33691 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| b3046d30-1bd1-3fa8-bb61-1517cda4f506 | -10.82544 | -45.15078 | 2025-01-04 04:31:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb869538-90b3-3811-912e-af30cd41968a | -8.83704 | -49.90558 | 2025-01-04 04:31:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97e795bf-40a5-3f23-ad63-ffa1a4de5e06 | -12.21816 | -42.44807 | 2025-01-04 04:31:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2991bcfc-3b80-34a9-b527-4e87b042d252 | -10.608 | -44.3418 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 1c16124e-13fa-309d-afa7-6326caccc327 | -10.54126 | -44.68225 | 2025-01-04 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1223f86-40c4-3551-a554-7cb21d14ab5c | -11.80054 | -49.32431 | 2025-01-04 04:31:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c32e9b8-42d9-3b0c-ba66-11eccf93dc64 | -12.35006 | -47.99144 | 2025-01-04 04:31:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5699d633-a6ff-3ab1-8e32-784610f61afb | -10.61325 | -44.33256 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e76f2e1-ac38-3e7d-9b6e-1c2dc6683a19 | -12.71908 | -47.62834 | 2025-01-04 04:31:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27e8fa0a-90d7-37dd-9642-d98a179203dd | -10.6117 | -44.33571 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 70a0bace-74f6-38b0-ad30-359660a101ce | -8.83484 | -49.89775 | 2025-01-04 04:31:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 460c4e7b-b6aa-3f44-9a2e-198494527212 | -8.27394 | -41.08303 | 2025-01-04 04:31:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6e24fc07-0305-3d03-ad75-074292c5eec3 | -10.60937 | -44.332 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ed68c7a-d1ae-34a2-b95a-6fb2b784925b | -10.21634 | -44.76651 | 2025-01-04 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23a3bbe3-75c7-3110-ad56-40311ef3726a | -9.85005 | -37.12117 | 2025-01-04 04:31:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 770f18de-a812-3a2f-99dd-9c8a25af720c | -11.1103 | -45.29588 | 2025-01-04 04:31:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0329d166-6541-3b04-be97-0f8849337531 | -10.55864 | -37.03583 | 2025-01-04 04:31:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f47e23a5-b7d0-32c5-9a3c-a30e75ef860b | -10.6112 | -44.34724 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0860353a-eb57-3925-af75-67fdd5f04843 | -10.21638 | -44.76416 | 2025-01-04 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 61be5a52-1e8d-3903-b439-4b9422e6a56e | -9.84408 | -37.12761 | 2025-01-04 04:31:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0fa801e8-8f3b-300a-900b-bcaa442ef4a3 | -10.21699 | -44.76188 | 2025-01-04 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad106c2c-ee38-3135-94f8-0fdd918c7e13 | -10.53746 | -44.68169 | 2025-01-04 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62f17470-4862-3249-a2b8-45a0f92c25ba | -12.10487 | -44.75545 | 2025-01-04 04:31:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a121c283-1db9-3a4d-a7f4-5e6edb1518fb | -11.79667 | -49.32729 | 2025-01-04 04:31:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44420676-71ce-31b9-901b-4eba02fb8948 | -12.47003 | -46.93882 | 2025-01-04 04:31:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1edb211d-d797-3f8d-b9c3-56a5a84a73b8 | -11.11192 | -45.29323 | 2025-01-04 04:31:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3d650c1-5e14-3545-acc6-d4bc19bd18ab | -10.42012 | -39.86646 | 2025-01-04 04:31:00 | NOAA-20 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 294dd332-0095-3c8b-8627-2dd115795dba | -8.27142 | -41.07998 | 2025-01-04 04:31:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a1c795ea-3c52-30cb-a137-515eff2bb407 | -10.56489 | -37.03698 | 2025-01-04 04:31:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e350c19-ce66-31a6-bc03-d78fd7b4bf6d | -9.89278 | -36.26636 | 2025-01-04 04:31:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 318e0ff6-52b6-315a-8670-671a8c861482 | -8.83425 | -49.90139 | 2025-01-04 04:31:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0b699cc-2540-3e7e-8633-855bda179bcd | -11.30905 | -48.88848 | 2025-01-04 04:31:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8619a68-26bf-3a7a-8964-6353483cc727 | -10.50315 | -49.13157 | 2025-01-04 04:31:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e341abdf-32ce-347f-8c8e-836e6fff0957 | -9.9839 | -36.38694 | 2025-01-04 04:31:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 86c81d01-c231-3213-8ca0-aef965e867f1 | -10.61098 | -44.3406 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| f0dfeaf2-6b89-3c0c-aa14-c64e9d9b4422 | -11.79998 | -49.32782 | 2025-01-04 04:31:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5566c85-a501-3d3b-a1b7-cb91e87a464d | -9.2819 | -43.04797 | 2025-01-04 04:31:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2157104-7520-37c5-a402-2e31e3b7f355 | -12.47061 | -46.93494 | 2025-01-04 04:31:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb647fe6-16fb-3ad8-81a6-bbce94438925 | -8.83763 | -49.90194 | 2025-01-04 04:31:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d40f7084-3a73-385a-98b3-93d0a699be5d | -8.2746 | -41.07817 | 2025-01-04 04:31:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d3915e42-de0f-3407-a31f-ea6a1e02072c | -9.85094 | -37.1233 | 2025-01-04 04:31:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 8269b2b7-5f03-3e19-83f7-c7b1b605254f | -12.46309 | -46.93775 | 2025-01-04 04:31:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ba902eee-df98-3d9d-945b-5431b469db36 | -8.59768 | -39.54317 | 2025-01-04 04:31:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0c04943-ec12-3ce9-a117-6be4956769aa | -10.61576 | -44.34293 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 6ec44392-cb82-3bfb-a811-e2eee86f06ac | -9.89864 | -36.27286 | 2025-01-04 04:31:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 1c30e485-2075-32b0-aa09-1fe985f93769 | -10.61005 | -44.32709 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc7369e2-1672-3cb2-ab75-bc4dce06f4ac | -11.80385 | -49.32485 | 2025-01-04 04:31:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a93c8e0e-5e57-3a81-a2d7-e1db3419c067 | -11.8033 | -49.32837 | 2025-01-04 04:31:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a14e0c15-a5ee-303c-aa2c-d132687ff1d0 | -9.25961 | -50.08976 | 2025-01-04 04:31:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bcdccbe-f9f5-34d6-9fbc-567fa73f44b1 | -10.60853 | -44.33026 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 171d2f1e-451e-38b9-974b-994f169f35e5 | -11.15374 | -49.69683 | 2025-01-04 04:31:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a961b720-0bc3-3437-b674-2373d7749232 | -11.15041 | -49.69629 | 2025-01-04 04:31:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3d52862-2b51-3b97-8eec-4c1b91b25036 | -10.45948 | -49.65996 | 2025-01-04 04:31:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7237ee6-dc9a-3fe6-8391-a9ee56793670 | -10.61257 | -44.33747 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| f5dfcc3e-b0d3-3fca-b9bb-8c183ac8cc7c | -9.62659 | -48.55378 | 2025-01-04 04:31:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e59befd1-1159-3889-8690-70e93654a18d | -9.89932 | -36.26723 | 2025-01-04 04:31:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 94739d4e-f1b9-367c-b787-8e4a0ae6a53d | -9.31676 | -43.1595 | 2025-01-04 04:31:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c8340c89-fd62-3cce-940a-39d224d32e5a | -9.8503 | -37.12824 | 2025-01-04 04:31:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 9.3 |
| fcd59a1a-c84d-37fc-9d83-ef789e14f396 | -12.71851 | -47.63205 | 2025-01-04 04:31:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
