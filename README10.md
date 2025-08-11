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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57e8f7ce-bb23-3291-b822-aef305cc225e | -7.17197 | -44.28719 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e68e4722-6765-3b5e-a4a5-a83ae0f97115 | -5.48069 | -44.39294 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eacbaeb8-8d6f-33fa-bfe7-45eef1c0ce86 | -7.16587 | -44.2763 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f605cb18-4745-3bf7-b3a4-eec9078e8fe7 | -4.1118 | -48.2072 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15ca6905-090b-3be9-93a7-0a9ecced6a0b | -5.48152 | -44.38782 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efc739e5-7961-3318-b42a-8b54373e64c3 | -5.816 | -47.32144 | 2025-08-11 04:02:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 287f5e5d-20c8-3ee8-9256-eb6654b648c3 | -6.29328 | -43.71319 | 2025-08-11 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b7a0e76-7612-344a-b8d5-d99a283af689 | -3.22501 | -49.34546 | 2025-08-11 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6a874174-1310-3c7a-9c43-fe5d025437b3 | -7.12868 | -44.22884 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d8bd4af-0829-304e-97a4-c0edae680fb2 | -5.48577 | -44.3963 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d16dfdac-413b-3fc7-b0e1-f49a1d6f5392 | -6.57975 | -44.5665 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| a4fdbc19-552f-3ea4-9c25-cce1f5e91813 | -7.16892 | -44.28178 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f36d727-23f9-34ad-945d-a8928c91d0d6 | -7.13107 | -44.21422 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6897a32c-922f-3462-867d-6dcd0179bde6 | -4.29284 | -48.05793 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 335c19f1-fc75-3732-bdc8-86fa606d3791 | -4.77639 | -42.72345 | 2025-08-11 04:02:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 307d96bf-e84b-3481-8527-7c12b1b82f3c | -2.95625 | -49.07018 | 2025-08-11 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44e4a39b-4f0e-3b6f-ba91-3a87566d77f7 | -5.48467 | -44.39359 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| b76667c3-3c45-3cd0-9ec8-e142f043bf41 | -4.77706 | -42.71922 | 2025-08-11 04:02:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 855c2e19-0a0a-36a6-97b4-cd53ab15cf3f | -6.92924 | -42.91899 | 2025-08-11 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0b88d4f2-a2f0-3fb9-bea5-b6b5fea4e0fc | -5.27363 | -37.68141 | 2025-08-11 04:02:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 90a43d7b-b272-309e-8ee8-b70ea3efeeaa | -3.4289 | -49.04492 | 2025-08-11 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 91750199-2530-3473-b67f-39e18b862d16 | -6.58541 | -44.55706 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9237c3d2-5e88-364f-9be6-2663a00e60bb | -6.31582 | -42.34764 | 2025-08-11 04:02:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a8d5b4a-85a1-3a4e-be47-ddf3c64d41a1 | -7.13081 | -44.22634 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33b36a8d-604e-34d6-9d45-3edcc8de09f7 | -4.29594 | -48.07128 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9950a113-6d25-3c46-b292-98d06094d325 | -6.98193 | -43.09361 | 2025-08-11 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7cc67b1-1c49-31ad-8c66-ca6a7ca7e6d0 | -6.28649 | -43.70744 | 2025-08-11 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 484cf54d-3e1a-3df1-acf1-a1e2af164742 | -6.98125 | -43.09778 | 2025-08-11 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0f0bf79-33c6-3d7e-b103-a0f7dc927414 | -6.30815 | -42.35038 | 2025-08-11 04:02:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f26998de-4dea-32c4-86c8-bcf505a1ef61 | -5.48664 | -44.39119 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4656c753-7ca5-3444-a55d-9b8c20194f1f | -7.13489 | -44.21499 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce7dc24a-4c51-3d9a-8f18-449594d6959e | -4.06608 | -47.97108 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1448026-c696-30e6-8f18-b5cb3c7dda10 | -6.28348 | -43.70222 | 2025-08-11 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ba94af3-ad77-3f42-8fb6-a6f9c44c2853 | -4.2923 | -48.06109 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60a62909-398d-3f39-8d6c-3da5e62a5121 | -6.28426 | -43.69752 | 2025-08-11 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af4fa4a7-c87e-319b-89ec-62a5a3299807 | -6.97831 | -43.09303 | 2025-08-11 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 834d29b1-0ad9-3ff9-94d8-34313dd0ae52 | -5.48865 | -44.39425 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| db80253d-9d19-3bd6-8921-a68fd770cb7b | -6.5837 | -44.56725 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 35dcc913-f97c-348e-88e7-16ff39fa22e9 | -4.10991 | -48.1242 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1cb32d1-e602-38b4-84e0-ac16c34cbd7f | -5.47868 | -44.3899 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f17c2105-015f-3049-b8c7-3013c63186d8 | -6.58455 | -44.56216 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 00f5d2ef-f0af-3e10-94c4-12be4999cc79 | -7.17443 | -44.27253 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 780f634d-958c-3efd-8e1b-764b6a7870a1 | -6.31229 | -42.34711 | 2025-08-11 04:02:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03af6a6f-801c-3f2b-b1b9-5ece9f8471ef | -5.48266 | -44.39054 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 26be2088-7d93-34b7-8148-a3e59c391714 | -3.43019 | -49.05094 | 2025-08-11 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 82ed7c32-7475-319d-bdec-4d2ff78f9202 | -2.96195 | -49.071 | 2025-08-11 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ceb029e5-53ee-386d-865e-22aa3ee04bd9 | -4.11237 | -48.20388 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb9fa9db-b8c6-3c96-a682-b86dffc587f8 | -6.57751 | -44.55569 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5a8c7990-59ce-3158-bad4-d8ebbe5ce958 | -3.43085 | -49.04708 | 2025-08-11 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ba236164-3630-3a90-98b1-815f03ad3b65 | -3.50879 | -50.74893 | 2025-08-11 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 079826e1-05d3-36f7-a62f-44c14d58faac | -6.97106 | -43.09188 | 2025-08-11 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c20994d4-8cc9-3297-b186-a359c7ba8b4f | -7.12405 | -44.23296 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ae20ac0-a35e-3612-a3dd-14d41ea6a107 | -7.16974 | -44.27687 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69c63723-1e51-3754-97af-3bbea3c76f04 | -7.17361 | -44.27741 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 176533c3-4142-3154-a9fb-abeb2bc67d2d | -3.42828 | -49.04872 | 2025-08-11 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e473f4f8-762b-3742-b45d-8112a7cd5a38 | -5.49061 | -44.39185 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5dcc8a34-0f6e-30e8-926f-79522d0529d7 | -5.48384 | -44.39871 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2162965c-0d37-3090-ab16-a9404b87d158 | -6.5902 | -44.55272 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c172c6d-1700-3f0c-a82b-e6ab0405e4bf | -6.5789 | -44.57158 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b8cfe240-739e-357d-affe-6e9a3fd5af79 | -4.30115 | -48.07214 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de82cbb0-2494-3d68-8ae3-5b98c6e981ed | -6.58935 | -44.5578 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f95fb292-094a-336a-a2ba-de442e078f8d | -6.28048 | -43.69698 | 2025-08-11 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14bb433c-edcd-3108-91a8-add872637165 | -7.17251 | -42.93609 | 2025-08-11 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2c26cd72-0507-3f82-9b68-6269a40acc9a | -7.16118 | -44.28064 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9db0bb04-257f-34e3-908c-97e6af377a0b | -4.11015 | -48.12395 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b366b601-cbe4-3c61-852d-a2b5348580db | -3.42457 | -49.04992 | 2025-08-11 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7fab3343-0a44-3984-bb47-eb86eccd4bfa | -2.96261 | -49.06704 | 2025-08-11 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9a84a92-566e-30f8-8446-1f2f435f8bdd | -5.48782 | -44.39937 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8d86b5e-808e-384b-a496-946914299537 | -4.07127 | -47.97193 | 2025-08-11 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c36aed10-5143-3850-b973-e2cbbed80027 | -6.58146 | -44.55637 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9ccc9dc6-f4d4-3f41-9731-01e5dc8dccad | -3.42764 | -49.0526 | 2025-08-11 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f025d8bb-b062-330e-b33e-895c744c4d25 | -7.17279 | -44.28231 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90a9bba3-f2e9-3351-b30d-1f03cecb2025 | -6.58061 | -44.56143 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 65322f6d-a4f7-314a-9701-33da5b6a0d61 | -6.5741 | -44.57594 | 2025-08-11 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9753ae4f-e9a0-3987-b117-4b2c44452f84 | -6.31168 | -42.35086 | 2025-08-11 04:02:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a7c894e-cac4-3e71-ac2b-4cb1a7a376e4 | -7.1681 | -44.28661 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f5dd471-9742-34df-88f0-5b558b2ea42d | -3.22567 | -49.34151 | 2025-08-11 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bb1dddc-1c3d-3f33-b3e3-c6652c889f44 | -7.13247 | -44.21662 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 190356b5-8e83-399b-b459-1584837f836a | -7.12949 | -44.22389 | 2025-08-11 04:02:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7304f48b-d428-3f7f-8412-6e3cf3b54ef3 | -6.9717 | -43.86586 | 2025-08-11 04:02:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18438038-237d-35b8-8626-ca6c5f4be9ad | -5.48948 | -44.38913 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 056b303e-4130-38b0-80ab-bcbdc9848686 | -5.4875 | -44.38609 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 8ec95699-635f-3fb9-8c1f-f80af3a92168 | -3.42522 | -49.04611 | 2025-08-11 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5291f7df-2a8b-39be-b41a-bcc25ab695a3 | -6.9436 | -42.92127 | 2025-08-11 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 04a6cc24-48ee-3df0-8854-4b8484582c0f | -6.97469 | -43.09246 | 2025-08-11 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 955e5f9b-ad27-321d-b2b3-8366570ef38a | -7.12894 | -43.49656 | 2025-08-11 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fca24389-e688-3173-b9d2-e3bb7e53f597 | -6.28874 | -43.7172 | 2025-08-11 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73bafbef-377c-38c2-be54-f260a91122be | -5.48179 | -44.39565 | 2025-08-11 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2654db23-d8b6-302e-9220-5264f482a1fd | -2.95692 | -49.06615 | 2025-08-11 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a9703d0-5376-3025-b053-72e238a924ce | -5.27706 | -37.68194 | 2025-08-11 04:02:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| db861a9a-0e7c-3060-91d8-3bd1f105db18 | -9.30369 | -40.21899 | 2025-08-11 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3d9a8c76-eda1-3711-a76e-7a2189b46259 | -12.57468 | -41.27387 | 2025-08-11 04:04:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b73b6601-9231-3dc8-aa21-2b7bd36d3a1a | -9.20409 | -44.52691 | 2025-08-11 04:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36ff3840-3396-375c-8be3-cf2a977e1c3c | -7.61783 | -45.19404 | 2025-08-11 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3c8a4b7-b493-3c6a-be46-17c0ade7aef8 | -10.36153 | -46.6307 | 2025-08-11 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93e709a6-eb86-31c7-aa2b-5b192b043922 | -7.65581 | -43.84495 | 2025-08-11 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06210760-5d95-368b-b6ec-851fb465c651 | -8.30125 | -44.98579 | 2025-08-11 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf630ff8-1696-301c-9a7c-abe8da7afffe | -8.03824 | -44.78124 | 2025-08-11 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a660c10-d8a8-37b7-b5ef-c727385f9645 | -10.36088 | -46.63436 | 2025-08-11 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ca55d29-8129-3eee-a899-72e3cdf27df4 | -14.47619 | -47.07601 | 2025-08-11 04:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README11.md)
