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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff8319b9-4fee-3585-9337-e76e37df1084 | -7.03409 | -44.45958 | 2025-10-02 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| a509c2c0-9e0c-3746-a961-ff8452aadd3b | -8.57821 | -49.5975 | 2025-10-02 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d4971249-032b-308d-9523-0bc3ac04f3c5 | -5.7235 | -43.65232 | 2025-10-02 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ee068044-7601-3613-826e-813fa97a3e2a | -5.33187 | -44.81554 | 2025-10-02 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 33997850-83f1-39af-b944-e5bfe7bd17a8 | -10.22606 | -50.33429 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 6c72cc86-e8b7-3f47-9156-fec6fb0b4859 | -9.44586 | -50.8892 | 2025-10-02 00:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 63fd9e7b-e71a-3752-a4c0-9665ba221517 | -6.96789 | -45.32082 | 2025-10-02 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f07bdeed-e2fe-375f-9f01-53ceb7c47fef | -6.55891 | -43.8861 | 2025-10-02 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6711bdf8-a240-36d9-8714-47ded61f254c | -7.84203 | -42.84945 | 2025-10-02 00:13:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b6197907-12f3-34c6-a179-c17d74792a99 | -6.02202 | -43.80967 | 2025-10-02 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 36ead4d8-a721-3d19-b523-17bd3455eb7b | -4.8448 | -45.42607 | 2025-10-02 00:13:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d39766d-ee32-36ff-ac29-a101cca71a8a | -7.8778 | -47.30026 | 2025-10-02 00:13:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8fe0fac6-21ef-3c44-9802-99918a1ebbf7 | -6.83678 | -43.04387 | 2025-10-02 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6c1a4796-8efb-3f4e-8200-7a2805ada080 | -6.02078 | -43.80084 | 2025-10-02 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1781fe9b-3d79-3a46-b74d-057849463b47 | -3.0977 | -47.00952 | 2025-10-02 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| dfee4e68-02d2-3da1-853a-a8ced5aa4ad0 | -4.84357 | -45.41712 | 2025-10-02 00:13:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5143f4f8-52bc-357b-a323-8245004fd42e | -7.84332 | -42.85859 | 2025-10-02 00:13:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 9b3669a6-5cc1-337e-b467-5e6a81757d94 | -7.77817 | -42.5274 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 237.2 |
| b92e15b3-54bd-378d-8a3f-4c313724be67 | -6.28597 | -43.65386 | 2025-10-02 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 00e7e746-dcdc-382f-8410-90aa2e55cab2 | -4.8359 | -45.16456 | 2025-10-02 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4c5d91fa-88ce-3c84-a1f5-791d11f42420 | -5.98208 | -44.59157 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 490cbc82-6410-3406-8153-d507373c0a7b | -7.37231 | -47.03038 | 2025-10-02 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dff80b27-e4f9-3931-8318-98446162c9e2 | -6.09974 | -43.44585 | 2025-10-02 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a498f5d4-b832-3736-bf92-f40918d13b9a | -5.89016 | -43.19494 | 2025-10-02 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6641004c-78c8-3fc9-9bcd-6d5c1ac26629 | -3.51923 | -44.03942 | 2025-10-02 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 27d1b89b-0ce5-3a13-8f0e-3943fd1da257 | -8.82164 | -44.7935 | 2025-10-02 00:13:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6b0ed2fb-8a69-3050-b0bb-0c655e4b70b8 | -7.7859 | -42.51672 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| f832ea20-1a8e-3d1c-aadd-90ed38aa5703 | -5.19191 | -45.07221 | 2025-10-02 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 8332329b-a391-3e2d-95d2-10e8a49496aa | -8.89781 | -47.61611 | 2025-10-02 00:13:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 39b037e1-3cf5-38f6-97b0-90bb36bf2528 | -6.34023 | -44.84076 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3ded399b-1418-3b44-bce6-1430d756cdf7 | -5.24807 | -42.89315 | 2025-10-02 00:13:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 00d51594-3d55-30ce-9d66-8cd5c4573a85 | -7.03532 | -44.46845 | 2025-10-02 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 2001883a-2c12-3ad6-b27d-10da773f0a43 | -6.27703 | -44.0588 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5401764b-0058-31f3-90ec-e23fd7d0be3f | -10.2234 | -50.31286 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 063dcb9a-de73-3b36-8251-ef72cb300c6d | -8.50873 | -47.82776 | 2025-10-02 00:13:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4c9b2650-f5ff-30a5-b9d0-9c82dec75012 | -4.62616 | -49.36283 | 2025-10-02 00:13:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0e2d9b99-32c8-3681-8112-6e099e22fc76 | -6.35575 | -43.2988 | 2025-10-02 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8006b2b3-ec5f-3b73-ad5c-739c8750ef74 | -7.41987 | -45.1899 | 2025-10-02 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dc3b3ba7-bf90-381a-b3d2-040798dd0f13 | -5.83853 | -45.75397 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 75ef285d-afcd-3c7d-a4a6-60fd1883345b | -8.61551 | -50.40124 | 2025-10-02 00:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 31145d33-6444-302b-b086-330fec3b021c | -8.66549 | -47.70357 | 2025-10-02 00:13:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3e21a96d-a4e7-35ee-8813-70b7b03cb32a | -10.21282 | -50.3359 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 69b9aae6-eca7-37da-9187-74b95a4b93ae | -6.3575 | -44.63997 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d74d4578-1d72-379d-9798-dacee1f9f3c3 | -6.16492 | -44.58054 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ee025cd4-7ee0-37ab-8bfb-ac150ef2aa7a | -5.97964 | -44.57397 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 706150cc-e90f-3dc4-8495-b99f646fa177 | -8.56606 | -49.59888 | 2025-10-02 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 6c5b0ffa-d5d3-3529-9767-7793742b8391 | -6.78145 | -45.57455 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 20404edd-88b6-35db-8bad-ac6dc4f4dec7 | -5.85583 | -43.41022 | 2025-10-02 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 53b1eabb-abcb-3431-a5a1-137ecd24d29c | -7.41093 | -45.19116 | 2025-10-02 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 02dadfc8-d6d9-386c-9035-7ebd8a8f06c7 | -8.65744 | -47.09383 | 2025-10-02 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 67cbdd01-6ce9-3e0c-8c57-3aa92ec9cde5 | -4.8347 | -45.41838 | 2025-10-02 00:13:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 04dd69dd-42b0-39c1-8a50-e41124eb36d8 | -7.55817 | -42.40804 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5cf0cadf-4bd2-39a9-b77a-fa884febe78f | -5.63812 | -45.97411 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e8a690d4-5c68-3a6a-b277-5eea2c3db2a1 | -6.16614 | -44.58934 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f0c37bfc-03ab-3a7b-9416-85a0a0a5da31 | -5.69253 | -43.0379 | 2025-10-02 00:13:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a95874ac-eb58-3b64-8a16-cebe87668e52 | -5.79221 | -45.75093 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1f5eacb2-d901-3d5f-aa54-84a4dcba0098 | -5.91906 | -44.86719 | 2025-10-02 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9af604a8-ab90-3a7c-b63f-3ba8b5afd52a | -6.55767 | -43.87724 | 2025-10-02 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 64e4b994-9f8f-34c7-84e0-aa91979d5834 | -7.51778 | -44.28233 | 2025-10-02 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e4b59fa-32bb-318e-bc6e-6967bdc1cd2d | -6.35018 | -44.58702 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 422304b9-ca35-3179-ae44-239282dd9261 | -5.89147 | -43.20411 | 2025-10-02 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 3882d402-401d-3ce9-ad03-ff8c22e23b1c | -4.85206 | -45.21639 | 2025-10-02 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d114f289-906d-3728-b209-40a7f1fb7c69 | -6.81603 | -44.47556 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e6ad83b7-9dc8-35cc-acf0-55d781600682 | -7.78723 | -42.5261 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| b4c59619-bb72-38dc-8527-66f2afb45711 | -8.58262 | -49.59129 | 2025-10-02 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| db05dce5-a402-3ac7-9965-70e053782111 | -5.82168 | -42.77417 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e77e17f6-29b9-3759-a87f-0f87b998fc69 | -6.46133 | -44.57708 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 529e939e-08df-334e-abbc-f3028eafaaf9 | -6.69073 | -46.06148 | 2025-10-02 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0f97de48-d2ba-3601-a6ac-557e8532996e | -7.63926 | -45.44786 | 2025-10-02 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 06ef36a6-1b1d-3c83-bd7b-6216db1406f9 | -3.81668 | -47.59256 | 2025-10-02 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9bd34dac-e00c-33e1-824c-9b6351c0e222 | -3.83031 | -40.37873 | 2025-10-02 00:13:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b3f7de52-1a4f-33d1-9c6d-cbcaf2373878 | -3.81922 | -47.58581 | 2025-10-02 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 198f2e12-6ec7-349a-be13-4720c4be6ee4 | -6.68423 | -46.69833 | 2025-10-02 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3815d5be-cb2a-3d66-9d65-b9b037360463 | -4.82853 | -43.51352 | 2025-10-02 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 82baaaff-215d-39ca-9529-379e5d859dba | -6.72297 | -44.14426 | 2025-10-02 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fdf9109b-19ec-317f-8efb-cc2ad3e804de | -4.60566 | -46.17104 | 2025-10-02 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bc3338a9-6c18-34a1-9569-347312606f88 | -9.71798 | -48.95261 | 2025-10-02 00:13:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bb4a5116-5f8a-3963-a8ce-ba93a591a119 | -8.57261 | -49.61037 | 2025-10-02 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d2bd6ad4-a00c-395b-b6bf-b5f39cff97d5 | -6.72419 | -44.15308 | 2025-10-02 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a6cbc460-4828-32fe-a159-c52c9d8b817c | -8.88843 | -46.59797 | 2025-10-02 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0f089e5e-0017-316f-9831-a8434e0c79b9 | -6.54622 | -43.924 | 2025-10-02 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 67138978-e030-3e8d-8ead-946567a77902 | -6.28348 | -43.63601 | 2025-10-02 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1111f35d-525b-33f6-bfec-dcc6cad7f38c | -7.0503 | -43.31541 | 2025-10-02 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1accb2b6-fd37-3536-a536-90e2ee681985 | -4.87186 | -45.62371 | 2025-10-02 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bd30d9ae-bb4e-3191-8794-05d6f2d78302 | -6.60008 | -44.31171 | 2025-10-02 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 19dae0d4-bbf8-3e13-a0a5-5d5df0e19059 | -5.31183 | -44.80043 | 2025-10-02 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 830631d0-264a-3e5a-af8d-231a3b6c6058 | -8.58477 | -49.60892 | 2025-10-02 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ccfe3b23-8c38-3247-8d5e-744be7bafcd7 | -9.62477 | -48.202 | 2025-10-02 00:13:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4e5056a4-541b-3dbd-b1fd-9f22f48026fa | -7.37376 | -47.04138 | 2025-10-02 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 7759a814-ea2a-3ba6-a9d4-aae156d3cf6e | -6.71561 | -44.62816 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c66372c4-a4c7-3e91-9b6e-a00996cfd312 | -5.98329 | -44.60038 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 24a0612d-bf6b-3370-8789-4367618e062f | -6.23248 | -45.33316 | 2025-10-02 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 20fd1738-27a8-3ba5-9bfe-5554a71d7732 | -8.33059 | -46.22228 | 2025-10-02 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fed5d1b2-41da-3f2c-a412-26147abdea3c | -6.24142 | -45.332 | 2025-10-02 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| cd48d015-a7ea-39ed-92d4-a7d05388096e | -7.30359 | -42.8893 | 2025-10-02 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 287517c0-8a9a-3dfd-8055-3811086b3d8e | -6.69371 | -46.69693 | 2025-10-02 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 79a96011-7ec0-3925-9d3f-b135fc859be6 | -10.21188 | -50.35125 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0558d2a3-9983-3a18-970b-284ae25560f4 | -6.08597 | -46.08038 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a625e872-a5e6-36d0-a2bf-b7716a5121ee | -5.4066 | -41.34703 | 2025-10-02 00:13:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| cbbb29e8-f0ac-3078-994c-e8ac5e938ec3 | -5.99489 | -44.60142 | 2025-10-02 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |


[Clique aqui para ver as próximas entradas](README9.md)
