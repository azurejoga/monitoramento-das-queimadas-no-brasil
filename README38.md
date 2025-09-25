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
| 57360ba8-5b68-30b7-80fe-2ce7425a2016 | -17.9308 | -55.8758 | 2025-09-25 09:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.9 |
| 9ddebaf1-2f37-3635-b1ae-73519a14d916 | -17.9308 | -55.8758 | 2025-09-25 09:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.6 |
| 4cc79f67-fac5-3dda-aa8b-c417f7f4593a | -17.9308 | -55.8758 | 2025-09-25 10:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.7 |
| 38b4bd78-7035-312c-9b50-0771cfd49c86 | -17.9308 | -55.8758 | 2025-09-25 10:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.0 |
| e9200653-1f9a-3de2-9c31-69fafe56d53a | -17.9308 | -55.8758 | 2025-09-25 10:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 190.9 |
| 08109c32-90d0-3cb7-b3d4-62e757757809 | -17.9506 | -55.8731 | 2025-09-25 10:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.7 |
| 4905daa4-8e54-366f-be35-123def7020d7 | -17.9308 | -55.8758 | 2025-09-25 10:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.5 |
| 9faddd1d-a247-3d89-8289-e80e4d998f4d | -17.9308 | -55.8758 | 2025-09-25 10:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 180.8 |
| 42f794e9-a2ad-3ae6-a994-1427f4ecff92 | -12.3188 | -44.1919 | 2025-09-25 10:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 039cbcee-2a01-39b1-b442-b1cd4c43b198 | -12.3184 | -44.2154 | 2025-09-25 10:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 79ca5367-d15c-3ce3-878a-620769d03f1f | -17.9308 | -55.8758 | 2025-09-25 10:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.7 |
| a12a337e-af5d-3797-8d2c-1b3f464c38c3 | -12.8365 | -45.2964 | 2025-09-25 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 2f0d24dc-d803-3bfa-bbca-b9bbcf8e71a6 | -12.3184 | -44.2154 | 2025-09-25 11:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| c7b7ef64-7e46-35f5-85b0-3078677c4608 | -17.9308 | -55.8758 | 2025-09-25 11:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.9 |
| f59d6a6f-ea9a-3e06-9d7f-e5eddb3f7ba2 | -17.9308 | -55.8758 | 2025-09-25 11:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.8 |
| ad5eb9a0-3b9a-3759-89b2-1ac92ee6734f | -12.3184 | -44.2154 | 2025-09-25 11:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 292.7 |
| 5b983914-2059-34dd-88fb-ba57958c8d6e | -3.79052 | -41.72475 | 2025-09-25 11:17:00 | TERRA_M-M | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 2ea9a402-ee5f-3270-8c05-f5d387a2e79d | -5.85386 | -38.33408 | 2025-09-25 11:17:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 47.1 |
| f4797d4e-7385-369e-8eda-76484d689784 | -12.32462 | -42.60202 | 2025-09-25 11:19:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 58.1 |
| 2e0f154c-0866-30f8-a4e7-f2ea48d405aa | -12.3184 | -44.2154 | 2025-09-25 11:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 410.0 |
| aa5037a4-504d-32fb-a731-473c122f18a6 | -17.9308 | -55.8758 | 2025-09-25 11:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.6 |
| ae5bae51-e2de-37a0-a338-4a393987f39a | -12.3184 | -44.2154 | 2025-09-25 11:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 7324cf01-4f29-30a5-a30f-e104e5f8a37f | -12.5384 | -45.8029 | 2025-09-25 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 6100a15b-3a1c-3bee-9a73-c52de4c69d35 | -17.9506 | -55.8731 | 2025-09-25 11:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 2d6219fa-5c41-3bb2-987a-ceef3ce7d60c | -17.9308 | -55.8758 | 2025-09-25 11:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.3 |
| 742e1f7d-a0c9-352e-a15f-c09e556c7b9a | -17.9312 | -55.8548 | 2025-09-25 11:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 818a60ca-5d78-3dcd-9469-99452b69faa2 | -17.9506 | -55.8731 | 2025-09-25 11:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 387c35b1-7189-32a9-810b-41f2e850b93a | -12.5388 | -45.7799 | 2025-09-25 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 983d3a20-29a0-3a8c-9e31-e3bc0fd4947c | -17.9308 | -55.8758 | 2025-09-25 11:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.9 |
| 5cb9892e-2a67-3607-894a-e7b830c32d62 | -12.5384 | -45.8029 | 2025-09-25 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 286.7 |
| 0fc8a339-2af3-3b74-909f-465f51ce16de | -12.5196 | -45.7829 | 2025-09-25 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 7ee7d7b2-6cb6-3f8e-93a3-05075c8cebc5 | -12.5384 | -45.8029 | 2025-09-25 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 535.6 |
| eecbc769-d018-32a2-a36a-c60cc642b557 | -10.3938 | -46.1444 | 2025-09-25 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d389d9c5-cfa5-3f2d-b094-87407ff8d8c9 | -17.9308 | -55.8758 | 2025-09-25 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 7d331666-4e0d-35a6-a044-a9406e95ed9d | -12.5388 | -45.7799 | 2025-09-25 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| b61c8ea3-c270-3e98-a714-bc2151dcdef3 | -17.9312 | -55.8548 | 2025-09-25 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 0dc72802-86c4-3fab-ac26-d1719f9aec38 | -12.5196 | -45.7829 | 2025-09-25 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| efa7b944-c3a3-31c6-b479-35782b2d7ada | -17.9506 | -55.8731 | 2025-09-25 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |
| ec3b7810-15ea-355a-b9bf-493724bd4e11 | -10.3938 | -46.1444 | 2025-09-25 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 32acaf23-c842-3427-b54b-ab5976f4f1a4 | -17.9506 | -55.8731 | 2025-09-25 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 67f4e5a9-6cb7-3dff-b49f-208f5a5451d6 | -12.5388 | -45.7799 | 2025-09-25 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| cf56efd0-37cd-3c26-9bbf-9f4c3c1c746d | -17.9312 | -55.8548 | 2025-09-25 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 069aa2d7-73a9-34a2-9fc3-7d6650d1ed5e | -12.5384 | -45.8029 | 2025-09-25 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 937.9 |
| 8e60292d-d4ab-30db-ad66-4eebcac744a5 | -17.9308 | -55.8758 | 2025-09-25 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.7 |
| a1d029e6-e671-3b90-b460-4907c17017fb | -8.7384 | -45.4299 | 2025-09-25 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 181.9 |
| d7bef161-72d3-3fd7-8901-04faabb9cd06 | -8.7387 | -45.4071 | 2025-09-25 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e23f71e2-bb54-3e69-926a-8e53e9d4368e | -10.3748 | -46.1468 | 2025-09-25 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| ba67a52c-82b6-3ff0-bad2-b583d9062105 | -17.9308 | -55.8758 | 2025-09-25 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.2 |
| dc9b0007-63f3-36c0-9db7-57b66ea4b89b | -12.5388 | -45.7799 | 2025-09-25 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 3b09a4f9-2817-3aeb-831d-011d4fb723d5 | -17.9312 | -55.8548 | 2025-09-25 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| d46ac568-db0f-384c-9acb-600b6d38a629 | -12.5384 | -45.8029 | 2025-09-25 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 720.1 |
| 38c92e14-aa3b-3feb-b8d3-c849f1846308 | -17.9506 | -55.8731 | 2025-09-25 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 8da1c1aa-9428-3ac3-bb55-c3f36eb893bf | -10.3942 | -46.1218 | 2025-09-25 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| f515f4c4-a86b-3969-a82b-cba867ca852a | -6.4131 | -43.0724 | 2025-09-25 12:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ebcf97d8-0e77-365a-a2fb-6366b2ca427f | -10.3938 | -46.1444 | 2025-09-25 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 235.6 |
| b996f968-a6f3-3045-9906-8b182822b36c | -6.4319 | -43.0707 | 2025-09-25 12:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 52b172b7-359e-375d-a37e-67430fdfe77c | -6.4317 | -43.0942 | 2025-09-25 12:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a2cb4394-81df-3568-8617-bca1b1f6c9d1 | -12.5388 | -45.7799 | 2025-09-25 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 62ca1001-30b1-34d8-9867-f49ee76d5264 | -6.4317 | -43.0942 | 2025-09-25 12:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| dfdff072-2beb-3c56-8dd1-268fa5022305 | -6.4319 | -43.0707 | 2025-09-25 12:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 39de674e-da6b-3542-bea3-57e55a178809 | -7.2793 | -42.992 | 2025-09-25 12:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| ba832241-168c-3728-ae64-1b06318d256d | -8.8415 | -46.2095 | 2025-09-25 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e3275efe-bf98-35e1-9ea0-a432f262667d | -17.9308 | -55.8758 | 2025-09-25 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.3 |
| 8884d01b-af43-30f1-99e7-26d9344a02e5 | -8.7384 | -45.4299 | 2025-09-25 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 654c356a-c846-30c7-840a-ac3fa1a1c350 | -12.5384 | -45.8029 | 2025-09-25 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 474.7 |
| 37ccdea7-b282-3d6b-b683-00bd1b33f001 | -17.9506 | -55.8731 | 2025-09-25 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 20b84221-2ca9-3a48-98db-61b18cb0a41e | -17.9312 | -55.8548 | 2025-09-25 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 41f819eb-bff0-3094-aa19-ba7b01613182 | -6.4319 | -43.0707 | 2025-09-25 12:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d497ee67-53be-3e9e-9749-8a3b602dd0bd | -6.4131 | -43.0724 | 2025-09-25 12:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 67d94f7a-2631-37c4-8697-1ecb19b6f205 | -17.9312 | -55.8548 | 2025-09-25 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 56692f1f-6c46-364e-b382-fa7f978b439b | -12.8676 | -44.6878 | 2025-09-25 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 450088c7-ca61-31fa-b2f5-0cfd980383cc | -15.8029 | -59.4835 | 2025-09-25 12:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| ff0e345e-9093-37fd-8a21-dd0616762af6 | -12.5388 | -45.7799 | 2025-09-25 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| a33b388e-5af1-3415-baff-a15cdddeb88b | -10.3938 | -46.1444 | 2025-09-25 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| cc296186-b94e-3960-8d8b-e7cc40161b90 | -6.4317 | -43.0942 | 2025-09-25 12:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a0109403-8e24-3c2e-a6d0-bc8a0b76fe6d | -12.5384 | -45.8029 | 2025-09-25 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 421.8 |
| f8d1eb8e-42b3-373c-a676-119acec8747e | -17.9506 | -55.8731 | 2025-09-25 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 6c2d6199-2506-30a6-bca5-14e8f4484117 | -17.9308 | -55.8758 | 2025-09-25 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.0 |
| 3f6d2d4a-2b2d-38b3-b1d6-51e45b1d0f28 | -8.8415 | -46.2095 | 2025-09-25 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 8db3f23f-5897-3d2f-9ac6-b5cd3653b09f | -12.8676 | -44.6878 | 2025-09-25 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| dff392e6-4f2c-3896-9dd3-5248f36790ea | -7.3567 | -44.4496 | 2025-09-25 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 18642dbb-f045-3871-b5b9-e0778153855b | -12.5388 | -45.7799 | 2025-09-25 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| e5f842fa-5b83-3094-a961-0058998966ce | -17.9506 | -55.8731 | 2025-09-25 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| eb573149-bc01-3617-9bdc-5285fd60faf7 | -11.6814 | -44.4078 | 2025-09-25 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| c67fcf39-0f67-36fb-a2bf-3422fcf3757b | -8.8415 | -46.2095 | 2025-09-25 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 7363db44-ff9c-36c1-809d-3ce783b1782f | -17.9308 | -55.8758 | 2025-09-25 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 552f2a58-113b-3869-a84d-34213d4990f3 | -6.4131 | -43.0724 | 2025-09-25 12:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6e4390dc-ab90-3cbd-be47-86ba80307b9f | -6.4319 | -43.0707 | 2025-09-25 12:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 47ee64a1-d5ad-36b1-a223-0dabebea4d5f | -12.5384 | -45.8029 | 2025-09-25 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 760.2 |
| c7c1d296-e770-31c7-8afe-e9d85baee0ca | -15.8029 | -59.4835 | 2025-09-25 12:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 32a85b0d-534e-3ff8-9f62-4c9e6c0e2a02 | -17.9312 | -55.8548 | 2025-09-25 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 751befd6-ac67-322d-b0b2-2043a3aa9558 | -6.4317 | -43.0942 | 2025-09-25 12:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| af85f759-345d-355f-a291-72bf1b5372e8 | -7.3755 | -44.4478 | 2025-09-25 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b33f0436-51f6-3edb-a930-93861520d2eb | -6.4131 | -43.0724 | 2025-09-25 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6a07b85d-1e4a-3582-93cf-ae2240a112b7 | -12.8681 | -44.6644 | 2025-09-25 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 25e3a478-e4b5-3b62-85f9-999431b3723a | -12.116 | -44.7606 | 2025-09-25 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| e682438a-0a91-3157-bdcc-535f7cc03fe3 | -11.6814 | -44.4078 | 2025-09-25 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 84925d36-14e4-3917-808b-8baae2a27c59 | -12.8483 | -44.6909 | 2025-09-25 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| e595a2e5-134d-3c50-b37c-baa04105ef3e | -17.9308 | -55.8758 | 2025-09-25 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.9 |
| 8caae3ae-fea7-37da-a2d7-5670f5a56c41 | -12.8676 | -44.6878 | 2025-09-25 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |


[Clique aqui para ver as próximas entradas](README39.md)
