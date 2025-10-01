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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47eed3ad-31a0-3498-9ac6-de3ed327e1b7 | -6.08366 | -42.48253 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e583d5fd-cb6d-3330-958d-39079301462b | -7.86108 | -45.27243 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c08a08e-b30e-38fd-957a-15a3fe2e2f66 | -5.85229 | -43.40023 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 00a3b841-d7d2-3ab0-a590-562dc33e9cc8 | -9.93484 | -43.61501 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b034eee-ffa4-3df9-8999-9da420f86279 | -5.49566 | -42.75238 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7e6960bb-5df5-3159-b5e3-3953b2ca6a15 | -5.95566 | -42.95246 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c100b87f-fcb1-3f33-8167-578d1b5a4d83 | -5.02892 | -43.00426 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fc3d0ab-0f7b-38dc-a2c3-987e6b156983 | -5.90479 | -42.92242 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea54761f-722f-352e-a76d-4d3d85d6bfa3 | -8.91823 | -46.08057 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7f426b4-4837-37c5-abd7-3a64424b25af | -6.72768 | -44.58002 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8234c906-18cc-39a7-8634-3733e118c2bd | -3.555 | -50.32893 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a76fa97-465f-32d5-aac8-8faa868bb717 | -4.62728 | -43.35925 | 2025-10-01 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7637fb24-a0b2-386c-8743-16276330a568 | -7.15841 | -50.54558 | 2025-10-01 04:19:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5292355f-dc96-35b0-a1ba-9b82de418507 | -6.68069 | -42.8014 | 2025-10-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 32e8be00-a047-32a5-a17c-2d0ee7bdf2e7 | -6.11345 | -42.65617 | 2025-10-01 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 748dabb2-35a6-348d-99f0-913e05773067 | -6.14856 | -42.65676 | 2025-10-01 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 70fd5773-0df2-30c8-9450-760ca87718f8 | -4.80844 | -42.76437 | 2025-10-01 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8e205ac-72ef-3322-b9a4-680bc1c9ccdb | -9.35449 | -46.33469 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e910a7bd-0895-3120-b494-5695571bb9bc | -4.80762 | -50.73674 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22147379-031d-3a59-96ed-f0798d5c06d2 | -7.7209 | -47.23279 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 290c4cde-c431-3617-93c0-cf744eb2e634 | -8.63979 | -43.98253 | 2025-10-01 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a91bc0f6-98b5-39e8-ba79-0174fde9271a | -7.47276 | -47.27184 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0476c814-2fc3-3ded-80c0-040a2f51c7ad | -2.26811 | -47.84687 | 2025-10-01 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c989db82-b60b-3694-a7c6-ca52e08f5090 | -6.11144 | -45.89754 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e47e052-6244-36a8-a455-ed64e1e55897 | -5.83198 | -43.95039 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2415bf52-f449-38a9-b930-084e32fe037f | -6.11788 | -43.48868 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 743879cb-e18f-37c9-828d-bdc9a82bb99b | -9.93266 | -43.65292 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8d9eadfe-3c0f-3502-9760-df29ce81a0ec | -6.05926 | -43.60239 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ffe903f-bff8-3097-847d-0a76f339ef8a | -5.16378 | -43.71719 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fab4f74-9110-36b0-bcad-0971045a99d1 | -7.79585 | -42.51506 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 52016e40-4924-3a5b-93c8-fe61b71b40d2 | -7.39685 | -44.60782 | 2025-10-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e867a7cc-a71e-3b20-ba84-54ec3e78ceba | -7.41717 | -45.41093 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7b8ad70c-8418-37ea-b903-b938858f47e9 | -8.92154 | -46.08112 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae24bef5-1260-3a28-89b2-8031cbe0c5d2 | -5.78188 | -42.85543 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ce4af29e-5a4f-3d6d-bc92-7177bfa3abab | -5.32723 | -42.7716 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 17507085-d030-335c-b58e-2ee53d650934 | -2.78924 | -49.62103 | 2025-10-01 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef32dafc-c451-38dd-b149-743c6172cf39 | -6.73198 | -49.63502 | 2025-10-01 04:19:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e678009-1aac-383a-a6fe-8abfbe15bc92 | -5.69666 | -42.65081 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8673a8d5-c2e5-3529-bff5-414e799a666b | -5.63657 | -43.91592 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ff25c6e5-b585-3be5-9460-433bf4733390 | -8.91327 | -46.06898 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 768f52be-4e5e-3166-82ec-0be5276fcb97 | -9.24425 | -44.49429 | 2025-10-01 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb23daec-aa01-3335-871b-2d014b03f8e9 | -7.86437 | -45.27295 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01309aaf-96da-303e-81b2-ce33f7c8bf63 | -4.14032 | -44.27643 | 2025-10-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ba6ab9f-acf8-3d53-b35e-84742f836455 | -4.40539 | -50.84346 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 81ff88c3-1526-30e0-9c95-39e9e2a5ae7a | -6.67671 | -42.8046 | 2025-10-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| da514488-3d4b-348d-8d70-0a316190698d | -5.82683 | -43.95953 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 00694744-58cf-3dab-a7fe-2ec1f9a9c15c | -7.41772 | -45.40746 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98ebacd4-406b-3c7d-97cd-c16a36067eee | -4.12227 | -48.80009 | 2025-10-01 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cdd90d3-d37e-3679-bc65-2c3a9a4146e0 | -8.90941 | -46.07193 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e69d022-a09d-33c9-bdde-964c37c642bb | -5.7737 | -43.62271 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e46ff208-733a-3a5d-b30a-f9e0e4c3e19f | -7.05808 | -45.18711 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd4b36ba-0df0-366f-968f-a176d486f168 | -5.74725 | -42.68903 | 2025-10-01 04:19:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 19b63bfc-6e1c-3365-b13a-b4a32e903fcb | -7.02335 | -44.47038 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dabbe16-8aa2-3202-8c26-938662f69b3b | -9.99456 | -43.61278 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 743ed151-c7ab-3f73-b1e3-b9fc47af6e70 | -7.48028 | -47.26912 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5db91d71-05af-32ab-93ab-0b8601deccb0 | -3.1174 | -40.83139 | 2025-10-01 04:19:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 41b26edd-6532-3c90-81ea-f413540ae1c4 | -6.43003 | -40.62219 | 2025-10-01 04:19:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 60435c14-25ea-34f4-bef1-9028816f0ff6 | -5.74384 | -42.68856 | 2025-10-01 04:19:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3ab95eea-daff-38e8-83a8-8f3ae993055c | -5.15062 | -46.41352 | 2025-10-01 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f83cd38-1338-3837-95b2-a1024783dcb9 | -7.47692 | -46.47488 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b2ee467-e896-30e2-9d7f-111664f2a6ca | -5.83036 | -42.78811 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aa38d8f0-8bf6-3dce-8098-b51f647dc857 | -5.82034 | -42.87645 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4cd91d19-0f6b-330c-979f-f71ca5f9e12c | -9.95411 | -43.57964 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e70e0d4-c65a-322b-81a9-63ec0e1e09df | -5.6422 | -43.94519 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62e59039-458a-30de-88aa-c997a20c4203 | -5.83116 | -43.93181 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b3d53b9-b3ce-389a-aae2-42ce5887b94d | -5.95514 | -45.8549 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49eb3024-52e5-3d8d-8591-7d6e88af2999 | -6.36605 | -44.58228 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4990e229-9265-3d3d-8b46-25da59f91471 | -2.2674 | -47.85145 | 2025-10-01 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 97c764f1-d0e6-3d61-9e42-287456cbfd2c | -3.93038 | -41.58106 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ed4911f9-721f-3583-975d-bd7b6d4d97b6 | -8.56062 | -44.75964 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 80954bf8-6f2a-3a50-964f-e3d750e1f7f2 | -5.71413 | -42.88289 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a0e556aa-ecc2-3119-9431-3768bbe725ff | -6.69382 | -42.80724 | 2025-10-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ffafdf4e-3891-3d00-b224-b02fee28702a | -5.9172 | -43.70654 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 202327a5-c056-3199-bcc8-691bf892f5c2 | -7.16058 | -50.54164 | 2025-10-01 04:19:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aec34bf-8063-3102-a2c0-937ac3a23441 | -6.73567 | -43.75731 | 2025-10-01 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb40b02e-b2d4-34bc-8658-4248be0e5431 | -6.10834 | -43.43989 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9db3353e-b32e-33de-a55d-4082983c353d | -5.90058 | -43.30932 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 065e68fd-0579-3402-b208-e9b97debf375 | -6.27715 | -44.06258 | 2025-10-01 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e287ff1-a6f0-31fc-8de5-9e7f6b7e0468 | -6.31131 | -43.4019 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 657080d4-ef87-3443-8263-0d0adbac9bf0 | -6.81139 | -44.47643 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e71980a-d8d5-3942-bdde-5c9000a07fec | -5.40907 | -41.33438 | 2025-10-01 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 57b2b008-e755-3043-9d67-26015b9c38d3 | -2.69956 | -54.76578 | 2025-10-01 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ebe9c3e4-f049-371b-85a4-d5fa87f999c5 | -5.83251 | -43.94692 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55977729-2502-380a-bb0e-baa1a94104d6 | -5.90025 | -43.92552 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6fe48302-d33e-3ac9-94cc-317ed5235a88 | -5.73155 | -42.81448 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 31e0b5c7-90f3-305b-a6a6-7ab729f818b7 | -5.6448 | -43.90649 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cbaeaa3d-a717-313d-84b8-ccb89ccde7f9 | -5.94005 | -45.90716 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1a4453e-e405-3a41-8f4f-c99bcdba877b | -5.89607 | -38.4826 | 2025-10-01 04:19:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f397b3d8-53ae-3b49-bb63-35ca1d8c627e | -6.06725 | -42.68349 | 2025-10-01 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 81be9536-de96-35df-923a-f55aa4a3957d | -7.70339 | -46.82086 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d23bb8b-be62-3a74-b047-684ded5c4046 | -6.5073 | -44.24432 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67b383ea-a991-3362-aabd-a893fa53f428 | -9.7968 | -45.92849 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecfd145a-a00f-39b3-b91c-d225aedf3dc5 | -5.09446 | -43.0475 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ce0e9b3-4972-32c4-87bc-866ac89d61df | -9.85653 | -44.60456 | 2025-10-01 04:19:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 77dc8c00-9dfa-3880-9ad2-5d3fcfb0507a | -6.26853 | -43.65686 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53d3e05c-1dc1-3436-b384-791388866102 | -5.81684 | -43.93668 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d033044e-91aa-38c0-8d83-284f22c409e7 | -5.27432 | -43.15847 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45839c2e-fdb3-37f6-8239-84667cd0b4c0 | -5.81584 | -42.88319 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a59638c5-adfe-3436-9b2a-67e0a97c86f7 | -6.99965 | -42.80259 | 2025-10-01 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a342241c-1864-3a8e-9b26-94ef1dbf2d1e | -6.08078 | -42.43144 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README39.md)
