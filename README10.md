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
| dd1519e2-0662-3ed3-a1d1-06f268f284db | -7.53666 | -46.09432 | 2025-10-20 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3049b48b-c651-3429-a3fe-ba234e848d63 | -6.38496 | -48.34898 | 2025-10-20 04:12:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef8c6a86-0704-3e6b-b97a-1c8f89a09fbd | -4.80849 | -41.12576 | 2025-10-20 04:12:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c4291eaa-7c2c-3f87-bd8f-acae01537463 | -6.18226 | -44.09031 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 048de54f-ede7-3666-9313-0d3ff81c6ca6 | -5.62692 | -46.41669 | 2025-10-20 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f114600d-2259-3bab-b8d3-586f117193d5 | -5.37902 | -45.008 | 2025-10-20 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b1d01cb-e729-3769-8c82-8af9683d9dd2 | -3.09613 | -51.29618 | 2025-10-20 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acc46c0e-0e36-3492-8fb1-329b2b2d48ce | -4.40217 | -43.31707 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38f77708-2b7c-3457-a099-b0ed973e311e | -4.42157 | -40.1686 | 2025-10-20 04:12:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e4dda1b-f427-3a0f-a7c2-4d9eed6975e0 | -5.46446 | -44.88837 | 2025-10-20 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e893fd4f-fb60-307e-9f49-726045dfe8ca | -3.33209 | -50.74942 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c3d70ce-5b4a-3ebd-99f9-c765152e1f23 | -7.01717 | -35.22376 | 2025-10-20 04:12:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| aac47527-ad48-3810-903e-7a1a8dd38776 | -6.9001 | -39.74817 | 2025-10-20 04:12:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae9dc339-29db-394c-93ad-23a7a97af526 | -5.30053 | -44.44765 | 2025-10-20 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85f3cb9c-8a2e-385f-bb94-47fdcb7b1930 | -7.08103 | -47.18024 | 2025-10-20 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91ecf759-f786-35a5-9c37-65d9d7f0b257 | -3.28078 | -40.88027 | 2025-10-20 04:12:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2bc33ad5-139f-3d63-b773-73ab1f16ae8d | -6.09864 | -44.0185 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fb3e51b-7568-30e4-b7cc-bf992f7612c5 | -5.91197 | -45.41192 | 2025-10-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 740fbac0-928b-355d-a0ad-7a26ab991d08 | -4.63593 | -45.0523 | 2025-10-20 04:12:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bafdd99-f7c2-36c5-a581-81a5c96e4048 | -6.14533 | -41.80888 | 2025-10-20 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49d8bbc1-aae1-3ea0-9e8b-c169f28f8006 | -3.14293 | -50.24872 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 961fbbed-c3d1-3cd6-855c-c709b3b0d21a | -7.07245 | -45.20665 | 2025-10-20 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b385f8ee-9478-3ecd-881f-5b00b5be093c | -3.14345 | -49.52229 | 2025-10-20 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5eea38ba-363d-3a8e-9d6c-a4a85798ff97 | -3.24155 | -50.0295 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c30c811b-8319-3712-b65f-9ec8301f6a45 | -6.13019 | -41.73062 | 2025-10-20 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 399f2bdf-fa39-3091-92ed-ec0f2c1c7547 | -5.22993 | -46.16064 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f286c6a3-99f1-3719-920a-4e3e6f9ddfb3 | -7.12926 | -44.24494 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cb9c34a4-add8-3f15-8cca-d36fd6bf9a87 | -4.45796 | -43.75578 | 2025-10-20 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a89b1e2d-de01-307b-ba98-05086c8d00ca | -4.738 | -44.43463 | 2025-10-20 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9707b7b-57e4-3b55-aef6-b151956a036e | -5.46384 | -44.89216 | 2025-10-20 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcf9a305-0ae1-36c7-95e5-a00532eb92eb | -1.92305 | -52.13907 | 2025-10-20 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c636c84d-bb77-372d-836e-502e987535a3 | -7.80963 | -38.89251 | 2025-10-20 04:12:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6335007e-56b3-3673-83a0-ee7d599389d2 | -5.53296 | -44.02765 | 2025-10-20 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfef13bf-3942-32c5-8729-fd8da3d9eb7a | -3.3321 | -50.22495 | 2025-10-20 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5b267094-cd2c-3609-b222-0f3bdb32c5a8 | -5.30852 | -42.68085 | 2025-10-20 04:12:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 764fe661-693f-32df-85cf-13f0291e6546 | -4.59751 | -43.47726 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b81430dd-aba5-3e00-97c9-b5cc87d38d98 | -6.26443 | -44.34215 | 2025-10-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 483861b8-704c-375b-b564-b4e9bf6f60c5 | -4.48272 | -45.3087 | 2025-10-20 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb6d698d-9b6c-3499-acbe-5b3603d3ce3b | -3.3326 | -50.74636 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edb20117-fb97-39ee-9f3d-7b52c0c22d79 | -5.23269 | -46.14346 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9deeb111-a408-39a3-aa8f-431e12223368 | -8.15555 | -38.63458 | 2025-10-20 04:12:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 68e5343e-b535-3b99-922f-8989b871fbfd | -6.98603 | -39.69593 | 2025-10-20 04:12:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dffb6b1f-0def-319d-a9eb-89ddf69c4028 | -7.54086 | -46.0858 | 2025-10-20 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49683a9b-ac34-3c3b-8f09-84f635c38492 | -3.09398 | -51.29746 | 2025-10-20 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8feb75f-1d9e-3e8a-81c5-4caa56ae5046 | -2.27478 | -51.92516 | 2025-10-20 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1880601-3563-3939-be03-aad263d29277 | -6.09529 | -44.01794 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6323fd34-64f6-3ae3-8280-8d8f280df07a | -7.99988 | -39.63057 | 2025-10-20 04:12:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cbe133c2-dee6-3b04-8863-6834b6c3ca19 | -3.5979 | -41.65514 | 2025-10-20 04:12:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cc746479-b2ae-3598-ad78-dbd87600d980 | -7.07589 | -45.20721 | 2025-10-20 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95c82230-88cd-3fe5-90d3-9999ef94be2f | -6.09195 | -44.0174 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52273b47-6f17-34ef-a344-5cd8ee354f23 | -7.0698 | -46.20248 | 2025-10-20 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6516d42a-139f-3bff-afa0-625749ad0fec | -5.96075 | -43.43254 | 2025-10-20 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1211fa7-5940-321f-9361-24f9a47dc56b | -7.65805 | -44.7345 | 2025-10-20 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f956314-ee13-3408-a7c7-2de39c375052 | -7.39394 | -45.63869 | 2025-10-20 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54910007-dd1e-3890-8717-eb700cc6baad | -4.47982 | -45.30409 | 2025-10-20 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea55ec90-4845-3b69-a658-05047aeb4b0e | -8.15948 | -38.6352 | 2025-10-20 04:12:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5a836a14-d7e5-3b05-99f0-dcb6709435fb | -4.42791 | -40.17348 | 2025-10-20 04:12:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba082a57-97d6-3660-8765-cee7a81e8796 | -5.37891 | -43.15868 | 2025-10-20 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95d89364-3901-3ce6-a7a9-3243883ca341 | -6.10029 | -44.02962 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef0acf94-833c-3ce2-81fe-9f0ffc4f3926 | -4.48691 | -45.30527 | 2025-10-20 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07dfeed1-789e-3f31-8ebe-ac216c1ccf6f | -5.10449 | -43.19661 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 191b9b96-a99e-3d34-a567-27550781db48 | -4.56562 | -43.78356 | 2025-10-20 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a13faad6-06c5-3742-b57d-d205deae9a4f | -5.39566 | -43.24696 | 2025-10-20 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2b42e30-73b0-3b75-9b16-6cbc57f1f416 | -4.39829 | -43.32005 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75491acc-626f-3c57-8ce9-6ad5e2dd3786 | -4.42731 | -40.1773 | 2025-10-20 04:12:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c614e58c-6dd2-3667-a01d-1db5155a5d08 | -8.16024 | -38.63013 | 2025-10-20 04:12:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 378cd249-ef2e-3aa2-aed6-660ec9e84a02 | -4.86586 | -44.44682 | 2025-10-20 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8babade-636e-3c15-a758-8a1a200a9131 | -2.44098 | -49.37121 | 2025-10-20 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8d6300e-a3ea-3dec-8edd-c1d374aa138b | -6.3618 | -46.15874 | 2025-10-20 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f713a26d-5880-3e04-bd12-3326120cc93b | -5.90846 | -45.41135 | 2025-10-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 978f952d-7248-3141-b46b-2ee7304c194c | -4.17939 | -42.19189 | 2025-10-20 04:12:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| cd26e588-1249-3ff5-b5d3-97b0a82f4077 | -1.44653 | -48.89497 | 2025-10-20 04:12:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22d0d4e9-31a1-3b42-9b5c-8fd98097ad3d | -7.24069 | -45.12162 | 2025-10-20 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf8745de-44db-3550-9f06-7ec6d9451c11 | -4.83525 | -45.79688 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 261a379e-0513-325d-87d2-b05b118744ad | -4.17609 | -42.19137 | 2025-10-20 04:12:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 83ac809a-d426-3c38-98dd-ba64aeb5f0e7 | -5.1592 | -44.54227 | 2025-10-20 04:12:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6032283e-f949-3d2c-a5d3-b824b3a2f4f2 | -6.91899 | -41.45852 | 2025-10-20 04:12:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7251ba96-6c1a-3903-aecd-ad75689684b2 | -5.51749 | -45.76866 | 2025-10-20 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 196d6c69-c603-3c50-95d1-e2956c444a4d | -3.51783 | -49.93502 | 2025-10-20 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5ea81fd-10a7-3154-999e-bda7cba19c62 | -5.16242 | -45.99734 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2dc71aa6-e706-3d3e-8a23-dcbc44d6baf8 | -7.30124 | -39.27185 | 2025-10-20 04:12:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9fc8130f-d293-3701-8ef0-0d193d20b2fc | -1.97444 | -50.81498 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4273df20-2a40-33f6-9bb6-e48cc2aaafce | -6.33737 | -43.28624 | 2025-10-20 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cabef57e-ddf4-39a1-8eff-aeb9af6b56a0 | -7.65746 | -44.73813 | 2025-10-20 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3a16a97-c96b-3107-9e32-cd33038155b0 | -3.09777 | -51.28604 | 2025-10-20 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ed87eb4-4247-3dc0-8784-823afa8a1984 | -5.36272 | -45.51066 | 2025-10-20 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01e4de6a-b93c-39ed-a23b-ed352b6b07d8 | -7.0426 | -39.22021 | 2025-10-20 04:12:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| baae2d8c-1eda-3556-8b74-2bf2b6ea45b4 | -6.55495 | -41.66131 | 2025-10-20 04:12:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ee2dc3f2-eaf9-36ac-9384-01048bbe25b6 | -7.53594 | -46.09334 | 2025-10-20 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e0a73a9c-673c-3218-bdbe-a9fbb1e6dd81 | -6.96032 | -39.64362 | 2025-10-20 04:12:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f4e3b98-ec27-376d-95fd-37671362b36e | -5.6094 | -43.65565 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6c696be-27a2-31e3-af50-8b709621ec05 | -6.95733 | -39.63864 | 2025-10-20 04:12:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2bdf563f-17de-362b-a439-f74d3ffd6f67 | -8.01347 | -43.92146 | 2025-10-20 04:12:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11443824-5a58-348c-a454-599d534f2bf8 | -7.14044 | -44.23944 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa5c7607-23c2-3da9-b822-becb5f9ef657 | -4.80793 | -41.12933 | 2025-10-20 04:12:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 454fcb96-1daf-3b04-a78c-be9295fc184e | -3.59126 | -41.65412 | 2025-10-20 04:12:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 79a48665-e003-345e-ba60-5b6be94571bd | -6.2162 | -40.97466 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4d020c78-91d9-3bbd-b272-785ee83c98a6 | -6.11412 | -43.7284 | 2025-10-20 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 456be2c5-5893-3d93-bedf-4531bd2664b2 | -6.12854 | -44.23211 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97b91f55-4ef9-39ee-b5db-0ab517165a91 | -2.30564 | -50.53477 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
