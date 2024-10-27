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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e0206ff-03dc-37e5-9d0a-ab94b8f451f3 | -4.93903 | -42.90718 | 2024-10-27 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 9140f59e-5691-3693-8d81-3d7c5b5c8d2e | -4.86173 | -42.62106 | 2024-10-27 04:23:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43c779da-b8c7-3a56-bb64-7cf25fa18d25 | -4.84922 | -42.95311 | 2024-10-27 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3224537a-b6d2-35e2-8396-a7c4fbe7cff7 | -4.33754 | -43.03779 | 2024-10-27 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eda9156b-ad0b-3267-8426-78b12c3bf9da | -6.3345 | -42.05371 | 2024-10-27 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cad06565-b806-3d41-80a7-6ff2a6942e36 | -6.23862 | -42.25434 | 2024-10-27 04:23:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7b1f40bf-b10a-37fc-a4cc-8c1eb3504a15 | -6.06123 | -42.8489 | 2024-10-27 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 19d93255-2eb4-3eb4-9b2b-21a096bfcd4d | -6.04988 | -42.72613 | 2024-10-27 04:23:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59e690d1-b954-34dd-b8b4-10b7aff9aa10 | -6.04922 | -42.73045 | 2024-10-27 04:23:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 980dc138-253c-3783-b2bc-042f36fcb6f3 | -6.04915 | -42.72905 | 2024-10-27 04:23:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| eb32f6d1-5f1d-3c0a-8cc3-3795a6bd2d11 | -5.97231 | -42.12168 | 2024-10-27 04:23:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9ce872a6-e6bc-31a1-9d7b-30198cb2d087 | -5.97161 | -42.12639 | 2024-10-27 04:23:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5d1e13dd-3d26-3835-80d2-ff60c696f51f | -5.96852 | -42.12112 | 2024-10-27 04:23:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| abb26091-47f0-3b33-b1df-a289d1408ce2 | -5.96781 | -42.12585 | 2024-10-27 04:23:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 259dadb8-fba1-3ca1-8128-e86377d70871 | -5.91173 | -42.42452 | 2024-10-27 04:23:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43df003c-2b41-31ac-abcd-d9484fc6b9a1 | -5.84304 | -42.63622 | 2024-10-27 04:23:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8867afe5-c682-3b53-8afa-4f005b772d7c | -5.8427 | -42.63478 | 2024-10-27 04:23:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8534f915-cdf7-3cda-a51a-084bd999d299 | -6.24926 | -43.40336 | 2024-10-27 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3441ffc9-2ea2-3adc-aabd-aff5578909df | -6.2434 | -43.39422 | 2024-10-27 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58df1484-de8f-3e95-a6d8-7d5184e5dc3a | -6.08226 | -43.45372 | 2024-10-27 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67aeb1f2-b2d7-3967-86c7-f9e5e8e219bd | -6.06515 | -43.47126 | 2024-10-27 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65cded6e-b585-3ecf-9949-c0da8c8b1eff | -5.63223 | -42.76919 | 2024-10-27 04:23:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af661df6-a3f1-3583-8e53-730afbde64a2 | -5.59783 | -42.97397 | 2024-10-27 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d31600a-10b6-3042-98d6-e2924b57da28 | -5.59722 | -42.97807 | 2024-10-27 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8253b291-3ed9-3b5a-aa03-47abe0cbe3c5 | -5.59362 | -42.97751 | 2024-10-27 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 96a97598-64ca-3e47-b10a-e83ef8ea1c07 | -5.54679 | -42.81355 | 2024-10-27 04:23:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 740d143e-04ad-3997-b639-c778857dfaeb | -5.67683 | -43.31381 | 2024-10-27 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 543efc95-b604-33e8-9576-642e088a4548 | -5.63627 | -43.2971 | 2024-10-27 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 689ff1a9-e15e-32cd-a427-1ae1288d8902 | -5.6361 | -43.29531 | 2024-10-27 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0e141a4-4ce8-33e1-9da8-500d9ab5f5bc | -5.4813 | -43.33931 | 2024-10-27 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 594bc1b6-20ee-3453-b333-c928168b9daa | -5.48069 | -43.34328 | 2024-10-27 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c2bafdc-acbc-3c16-ab34-69e4ba9fb557 | -5.29954 | -42.94088 | 2024-10-27 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 883edbd0-fa8b-32c1-a9af-04b12e551aad | -5.29594 | -42.94036 | 2024-10-27 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc62dd55-1e12-3e65-b95c-7f6fd3c69692 | -6.60241 | -42.06775 | 2024-10-27 04:23:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 53a585db-0ebf-342b-85c5-ba7ad2ebf9d3 | -6.59857 | -42.06717 | 2024-10-27 04:23:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd844d19-52c6-30a5-bbf9-8cbf08aca391 | -6.5095 | -42.35576 | 2024-10-27 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf447d4d-55bb-3f29-ac6a-f04a8a757b99 | -6.50882 | -42.36024 | 2024-10-27 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dc3a19aa-74bf-377d-86be-c5229692f4ba | -6.5071 | -42.34612 | 2024-10-27 04:23:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a0eee6d9-bff3-39f6-9238-5ed2eff9e977 | -6.50573 | -42.35521 | 2024-10-27 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a67833dc-1582-3a28-a0ae-28cdd54eb66b | -6.50505 | -42.3597 | 2024-10-27 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 66612d80-9a7b-3e37-a87d-5b7abdd88276 | -6.49819 | -42.35411 | 2024-10-27 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 45dd3a56-3f8c-3cd2-bcaa-95e7c307df45 | -6.81618 | -43.29049 | 2024-10-27 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65331e8a-f541-3763-af03-4969b86e6c76 | -6.81259 | -43.28993 | 2024-10-27 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1bedbaf7-e0c3-3da9-837f-37ea68ac54ea | -6.81196 | -43.29407 | 2024-10-27 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d809b5f4-eebf-3b6f-9b1e-0ab331cd35bf | -6.80837 | -43.2935 | 2024-10-27 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1f3a8f2e-55c6-3c35-824f-ea9d0abf30e2 | -6.85233 | -43.57424 | 2024-10-27 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd62c6c5-62b0-3b8b-baeb-c8887a75e7e8 | -6.85172 | -43.57826 | 2024-10-27 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36edcfb7-1964-30ef-8f68-705beec926da | -6.76982 | -43.54601 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1e6c5c7-b786-30d7-84f9-bbebefe4dcbd | -6.6688 | -43.54515 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f567f07a-7596-3b6d-bed7-f84d15d00e62 | -6.66526 | -43.54461 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14070862-4654-375d-8607-9df86507fff6 | -6.6285 | -43.57193 | 2024-10-27 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a130aec0-37d7-3d4d-aa9f-78c2240d5f61 | -6.59482 | -42.27771 | 2024-10-27 04:23:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ce799ed-58b9-313b-ba40-1693b68f9edb | -3.41578 | -43.19712 | 2024-10-27 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afddcf00-7e0b-3032-90bb-7ef1fd21544e | -3.37204 | -43.31973 | 2024-10-27 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e53ee42e-2a8f-310d-a88f-a49f36b9a5e7 | -3.37146 | -43.32354 | 2024-10-27 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a792f88-a633-3055-8306-aaf020f575e8 | -3.06661 | -44.33537 | 2024-10-27 04:23:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| b64b8b02-2d92-34a5-b0b3-7d0fb023c91f | -2.50661 | -44.1333 | 2024-10-27 04:23:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b368c70d-0c6e-3e11-a2c7-e1739a809736 | -2.50606 | -44.13684 | 2024-10-27 04:23:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85175e2e-1c80-368e-915d-59c4adae50a7 | -4.74206 | -43.25365 | 2024-10-27 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfedc40a-e819-38d2-b2f1-21fd0225a669 | -4.74145 | -43.2576 | 2024-10-27 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99dc8447-02b8-3e53-9ea1-d3c264137d82 | -4.73502 | -43.25256 | 2024-10-27 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78d6d612-f94d-3d62-a286-5e585c7eac99 | -4.71103 | -43.88317 | 2024-10-27 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bcb907e-2911-33ee-92e4-9d379460607a | -4.70817 | -43.87891 | 2024-10-27 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27943f81-50c7-362e-880c-e33add0073a9 | -4.70703 | -43.88638 | 2024-10-27 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79c71456-9935-3854-9cf7-13fd8eb9509d | -4.70474 | -43.87838 | 2024-10-27 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cce54012-7040-30ae-9eae-9676501668c3 | -4.7036 | -43.88586 | 2024-10-27 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 979082d1-506a-35c5-8fe5-241ed5a8c918 | -4.53863 | -43.56818 | 2024-10-27 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ebeaa488-df38-3c2b-bfc6-960889b01c40 | -4.37757 | -43.54935 | 2024-10-27 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8485a3ae-94ee-38e4-b7a7-380f95529df0 | -4.21824 | -43.62641 | 2024-10-27 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dae3698-805e-3e01-880c-25370e983283 | -4.21479 | -43.62586 | 2024-10-27 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 673e0da1-ef89-32a6-b9b2-5c1511149f8a | -4.15772 | -43.70192 | 2024-10-27 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e2d7e74-29eb-3db4-afda-8464c0995f2c | -4.15428 | -43.7014 | 2024-10-27 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5ebf9aad-f885-3069-817d-e664a3a46da6 | -5.80077 | -43.9252 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 765f725c-0f00-3792-ab6d-428177ba3b42 | -6.40303 | -44.15367 | 2024-10-27 04:23:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39509e1f-8b59-3bce-aab8-b45eaf8350af | -6.3691 | -44.01297 | 2024-10-27 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b07268e-80d5-3bf4-8906-5fb640dfe266 | -6.36852 | -44.01679 | 2024-10-27 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9759b5e-7fa9-34e9-b86c-060c13400c55 | -6.36563 | -44.01251 | 2024-10-27 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70927822-9639-350f-a3fb-8213753ae631 | -6.36505 | -44.01632 | 2024-10-27 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44f9964d-2cd2-38b1-8328-d15f2f07a579 | -6.36157 | -44.01587 | 2024-10-27 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5101fe6e-5d5d-3b72-a14c-0a91450336a3 | -6.28169 | -44.73526 | 2024-10-27 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b48f4380-9c3e-3420-a34c-02dcb6e79d85 | -6.21456 | -44.63235 | 2024-10-27 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f41d599-1a8e-3a38-8bf2-fe01973f0066 | -6.214 | -44.63601 | 2024-10-27 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a472e40-dfa0-3a00-a67c-021665a72ea6 | -6.18003 | -44.3302 | 2024-10-27 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7012345-16c1-3818-9d72-ec77e80ca8ec | -6.17661 | -44.32966 | 2024-10-27 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 358accd0-3b2f-3752-be62-fa638c174ce5 | -6.14164 | -44.05703 | 2024-10-27 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75a300c2-4353-3139-8f93-d75ab7b394a6 | -6.06082 | -44.90329 | 2024-10-27 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24f64f62-2f48-357b-9681-33e476388a95 | -5.92491 | -44.66633 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4c5eb7b-7025-392f-b416-5abd4fb0eb3f | -5.92218 | -44.72854 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5733eb9d-6230-372b-8503-a4c8037c60e3 | -5.92153 | -44.66582 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9850898-30cb-38c8-8f36-1b01c5f803e1 | -5.83246 | -44.90858 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7ad9e5a-3554-3304-803f-905258e4bd51 | -5.82966 | -44.90451 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f509259-8ee7-3d26-a4a1-30ec0a47d15f | -5.82911 | -44.90806 | 2024-10-27 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd206a3e-47a2-38c2-bcb8-3b0336bd5962 | -6.52542 | -43.96908 | 2024-10-27 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0ab8e6a-afeb-3923-a9a9-1e4f778886d6 | -5.73066 | -43.8137 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d9e8075-c13d-35f3-9716-a8ef5497f59b | -5.72719 | -43.81316 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5eb01b70-4dbd-355c-9e12-07ae2b65a7c4 | -5.72372 | -43.81262 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6d7d4a2-050b-32df-b284-24c76c6b5d87 | -5.71905 | -43.84313 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13b3325c-eff0-3da0-9636-f857a7e3dd12 | -5.71617 | -43.8388 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a2fd72f-e6b1-36bd-9af5-fd59fbd24da6 | -5.71558 | -43.84261 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a02291a-847a-3911-a96b-a327d2063edf | -5.715 | -43.84641 | 2024-10-27 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
