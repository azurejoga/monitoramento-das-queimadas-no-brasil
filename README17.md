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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cc48577-547e-320c-b10e-2490f584215a | -6.35257 | -43.34588 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67548455-b87f-3865-8d05-a14c36379cf6 | -2.93129 | -48.02269 | 2025-09-25 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22536798-731a-313a-a10c-47467d11afae | -7.59457 | -42.33117 | 2025-09-25 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 266a3d2d-cd29-3327-aa2f-599900c3ef1a | -7.26591 | -44.91086 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 419e2350-1c74-31c7-bf5a-206372d628f8 | -5.3039 | -44.43477 | 2025-09-25 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8c68d2d2-0966-3c7c-b153-5fc847947e04 | -3.61549 | -38.76277 | 2025-09-25 04:32:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 059bd8ff-2eca-3fa2-b362-6a38118bc2a3 | -1.53476 | -51.61605 | 2025-09-25 04:32:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31f33f04-9d1d-38cd-8502-f7c04549ac40 | -7.13589 | -44.3407 | 2025-09-25 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24973cb7-58b6-34ee-b29e-228269ad6b8d | -4.14518 | -41.54915 | 2025-09-25 04:32:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6daa4166-b6ed-3ff7-9517-8543b7cce71e | -1.76584 | -47.22775 | 2025-09-25 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f92b6cb-1581-31b5-a3e0-f7ce4fdeda48 | -6.42027 | -43.07872 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 38b95563-195c-3fcd-995d-fa613d8f245c | -4.01313 | -43.27162 | 2025-09-25 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5aff03be-e7bf-3da8-b963-0dcb5c032b41 | -3.78816 | -41.73608 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0233edf6-ab02-345e-9449-6a3868818411 | -5.9263 | -47.26291 | 2025-09-25 04:32:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcbb1e6f-562e-3ff4-acd0-335c038b3198 | -6.59362 | -44.62127 | 2025-09-25 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 982f158b-7963-3b8f-bd4b-7f9cff13fe91 | -3.78455 | -41.73162 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f564b59a-9f0f-31b2-aaea-969d36dd4cf1 | -5.09338 | -47.47432 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dcf661d-ebe9-3a5e-9cc9-54fe3a086e09 | -6.5516 | -43.83152 | 2025-09-25 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2f03266-b4a7-3c74-9d2a-9ef329ddf017 | -5.78517 | -42.55802 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 89278935-0cf8-3611-8528-1889a6f72495 | -3.17143 | -43.87086 | 2025-09-25 04:32:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e861a748-7cc3-3cda-81da-0ea4b76834f2 | -6.84378 | -43.17251 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 53c6d2a5-e44e-3749-ada3-aee7259ac0b9 | -0.45951 | -52.15612 | 2025-09-25 04:32:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04d50ee6-7b30-328a-8f7b-6d76e94f5bda | -3.94343 | -49.40207 | 2025-09-25 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2922f0a9-4f31-31e3-90f1-54d5feb1d814 | -7.32362 | -45.76071 | 2025-09-25 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d1fc16d-899e-3462-ae2c-7d4a63a53ba2 | -4.67288 | -48.15868 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cea7d672-e9a6-3349-9790-7f9cda108ef4 | -5.95977 | -42.90375 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8ad171ba-ef0c-3227-897d-c1ea38b3bf2c | -5.39335 | -42.27507 | 2025-09-25 04:32:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f401b614-9036-3d38-8c4b-251de48b8bfb | -3.46257 | -42.64155 | 2025-09-25 04:32:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e60c1cb-dd16-3d28-b99f-69732148df5e | -4.03234 | -47.77487 | 2025-09-25 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89f1949e-263a-316c-8be9-4310074bfeaa | -6.4227 | -43.08976 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8a59462b-dc4b-39fc-8394-c04fb79df48f | -5.06264 | -44.31688 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a31ec555-0d36-34b7-9c81-731dfcdadf54 | -7.08126 | -40.34797 | 2025-09-25 04:32:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c18da2b8-8a1d-36b5-844d-e675a6b7c01c | -7.19434 | -45.3726 | 2025-09-25 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4805f74-5556-3848-89f9-75c61fc086b6 | -5.78714 | -42.79971 | 2025-09-25 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 70fea45b-10c6-3b27-b26c-7d5bdf31795b | -3.74393 | -51.38343 | 2025-09-25 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac5c7e43-19a9-394e-8786-b6839ffe47f7 | -7.37659 | -44.43747 | 2025-09-25 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b097fcf-7e45-3f6c-8d67-5aefc8710faf | -5.51972 | -43.86904 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 213f348a-d2f6-38a1-8751-37c4e4c9e22f | -2.92514 | -48.30112 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1578c9bf-992e-347d-8696-087aedcaa22a | -7.99047 | -43.58358 | 2025-09-25 04:32:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c25026fc-a299-3924-b0e5-dbec6861187e | -5.54504 | -42.80605 | 2025-09-25 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b1c65ad1-8022-31fa-8fb9-b88c9ae2c6d2 | -7.11461 | -44.48704 | 2025-09-25 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58de361e-8565-32ea-ad0d-2c3000709c7e | -7.27572 | -42.9843 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8dfb1a8-2392-35e1-8afe-a0cf1fd3caea | -5.76374 | -42.56209 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1e6380d3-9915-3113-82db-fb28fc16ff34 | -7.2986 | -43.91063 | 2025-09-25 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0621f6a5-ded2-3156-9066-56cd0cceabfb | -3.35593 | -51.60285 | 2025-09-25 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1138c11b-2bfd-3fa8-9bb7-f92d424c3d19 | -5.72653 | -42.61661 | 2025-09-25 04:32:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 193d7cb5-bc60-3dda-8ec6-9907eefbbb3d | -7.59908 | -45.741 | 2025-09-25 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c01d643a-f3db-3e9b-a756-3c119991254b | -7.25991 | -44.90133 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e88b9800-bbe2-37fa-87d3-9ecf4a7bfdb0 | -6.1305 | -44.43939 | 2025-09-25 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b6df64e2-37c7-3dee-8b3a-6de0a51246a5 | -4.34915 | -47.46619 | 2025-09-25 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e524be9-b73c-3cea-a6db-cfabc6b45caf | -5.77274 | -42.89732 | 2025-09-25 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 001b43f2-9085-3bcb-8d20-d1a80879b996 | -2.92404 | -48.30817 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0abfe667-5b03-33b8-8d6f-59ab87790eb2 | -3.90769 | -54.55976 | 2025-09-25 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 505139aa-058f-383a-827d-2a70aaabf2d6 | -2.83431 | -46.72869 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f11eddf-3103-30b3-880d-1128c89dd6a5 | -3.69962 | -49.5685 | 2025-09-25 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a747e04d-c2c5-3b16-8e04-f675252c2bf8 | -4.42891 | -47.26422 | 2025-09-25 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aade5048-2beb-30e3-97b9-9d8400613fd1 | -4.91376 | -46.83771 | 2025-09-25 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ed39545-b75c-3eab-b52f-e7d6c411f48c | -3.35809 | -43.37616 | 2025-09-25 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3599a4f-f6da-3404-9c99-feb3243b7326 | -4.57239 | -48.01911 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bf35ac3-2edb-3532-b071-a95f1dad2827 | -6.57962 | -43.64993 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 487f31c0-526a-37a1-bac5-1922f2a4635b | -6.41578 | -43.08155 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 85b4e11c-9f6c-3937-8e92-ce374b873cb9 | -3.82317 | -50.97172 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b909000d-6c85-3916-869c-7d1e3d7e63ce | -4.67673 | -48.15573 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| add5bce3-d3bd-315b-8829-07e554f41264 | -0.45535 | -52.15541 | 2025-09-25 04:32:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0df2b901-e859-3f71-89cc-154cf95604d1 | -2.38474 | -57.24225 | 2025-09-25 04:32:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edbd6075-2253-3f4f-ab68-111b9141d7c2 | -5.37879 | -42.82408 | 2025-09-25 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48d499cc-422a-325c-8100-08f546581b5d | -5.51666 | -43.86388 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 28c69bc7-66c3-37a5-bdd1-0715e7c07f2c | -4.80137 | -47.27343 | 2025-09-25 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45473c11-d4aa-37df-a9cc-f9a97319ea5a | -2.45123 | -57.94434 | 2025-09-25 04:32:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d325e421-e9bf-3219-9afa-b6c26a8657bc | -6.07764 | -44.08397 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b9a1d1f-ddac-3515-96df-b3d20197a09a | -5.76019 | -42.55774 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4974c7d9-f656-3dcc-9bd4-96177435f3bd | -4.80083 | -47.27687 | 2025-09-25 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62a5176a-244d-36f0-8a2c-c3bb622e393b | -5.39846 | -48.84632 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e98b71d-17e6-3ff4-8725-ced17e1b7938 | -5.54204 | -42.79859 | 2025-09-25 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2c2946ea-d446-30e9-9c42-c780a86c952e | -3.82984 | -50.97723 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 24c74d64-d3e7-30ac-a0d2-00f02645b081 | -4.71093 | -47.98076 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| edb5d44d-bc1f-3eb0-8f3a-1dca1ca07106 | -3.79294 | -41.73282 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b0120cc7-d7bf-3b4d-b328-86c8a67ec91e | -3.34284 | -51.63541 | 2025-09-25 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15350945-8e33-3340-9f9b-d0d29a36c6a8 | -4.52314 | -43.64496 | 2025-09-25 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 799e95a7-e629-3b10-8a30-1bb83ef904ac | -3.7446 | -51.38142 | 2025-09-25 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f09f849-5544-35eb-a391-02b69ec8f517 | -6.56349 | -43.65252 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| def4381c-4338-3620-b0c1-aa0faab2b03c | -2.91739 | -49.56158 | 2025-09-25 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f63218-fc7a-3473-9ffb-ce9ad5c278d7 | -7.31667 | -45.75967 | 2025-09-25 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9621f742-9f80-3b60-ba19-6483922c146a | -3.30874 | -42.17743 | 2025-09-25 04:32:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 662aae90-634b-32fb-9dab-464285a14378 | -4.58199 | -49.693 | 2025-09-25 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89baf5b2-4901-3fc6-88d0-da15cbed4acf | -6.55176 | -43.83436 | 2025-09-25 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 146a6082-ef88-32fd-9a8a-85da3bfd9f02 | -6.59791 | -44.61747 | 2025-09-25 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 555a687e-e46a-3e0c-977e-1eea62ccaa3e | -6.20349 | -43.93778 | 2025-09-25 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77318a31-bc31-33cb-9892-48005a025208 | -4.34567 | -50.50512 | 2025-09-25 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b941f83-37ef-398d-9145-62aadeea4f4c | -6.48989 | -42.86514 | 2025-09-25 04:32:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b997f9e-3b6d-3cc4-bc79-6ce814716f03 | -7.31956 | -45.76406 | 2025-09-25 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faad1656-24d4-357d-a6d2-5a2a06871c6f | -6.73568 | -43.17044 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 130df9e9-2168-33d7-ab55-d5913fefa1d5 | -7.50071 | -43.67035 | 2025-09-25 04:32:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9a5c544-c33e-3024-b901-6c6c2a9ac3e0 | -3.83196 | -50.96416 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b00765b1-391e-3bd9-9245-86c2326e1646 | -3.23816 | -46.80238 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ec85507-64a2-3ce5-98a6-f496c46cdc6c | -3.43901 | -44.48181 | 2025-09-25 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c0de5b2d-4ffc-39a4-9d1f-a120892ce7c9 | -1.82618 | -55.27714 | 2025-09-25 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f5c1beb-f147-37f0-b574-84c6851fd223 | -6.39807 | -43.53059 | 2025-09-25 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8780b419-2ca2-333d-84fe-de59f327b54c | -5.93672 | -42.92195 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 05e0f534-1d0b-3d6c-be29-a21a9038dbfc | -3.20646 | -54.958 | 2025-09-25 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README18.md)
