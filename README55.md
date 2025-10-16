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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6eb96e11-89e6-38b3-9cbb-d6199a39edef | -7.29413 | -41.95579 | 2025-10-16 04:38:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0ec03e62-a969-336c-af83-d0c41a507b6a | -4.50421 | -45.39644 | 2025-10-16 04:38:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbf162f9-e92f-3de2-8560-1326ab281d4a | -4.78067 | -47.66177 | 2025-10-16 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfb6c19b-d65b-31d4-9e22-1765a7825a3b | -5.32816 | -42.90091 | 2025-10-16 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6af00d5b-b56d-3740-9088-257de1d9fc7a | -6.77641 | -42.81028 | 2025-10-16 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3940260b-06e5-394d-b2ad-8e72a4d79b7f | -6.27696 | -52.63121 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c345fef-0de3-3b3d-8f48-e6806df8bdef | -7.00956 | -43.74159 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b542c697-290e-3d45-8011-e9a2aef78679 | -5.75972 | -43.05823 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cae43a5c-d7d7-3cb6-bbf8-f8c73dca9ecb | -4.42102 | -40.17804 | 2025-10-16 04:38:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 027e4e16-e824-3c8a-83d7-a303d4d75c83 | -6.06708 | -41.91832 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 75102b29-9b1c-3c7f-8d2e-28a43af1bbed | -2.69281 | -49.5229 | 2025-10-16 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4353901f-4737-3123-99ba-6f18d9196434 | -6.18251 | -44.29703 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 424e25f3-ca35-3043-a459-bc3c30c392ac | -7.93658 | -44.12521 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce667935-b432-3a4d-8d2f-b827db810d52 | -7.16084 | -42.51468 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e93c1902-1a97-394b-a943-69f530b6bd83 | -5.63937 | -45.96656 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b3a36dc-8185-380d-896d-890c42910ac1 | -2.93641 | -54.17064 | 2025-10-16 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c55a976-2f12-3d2b-9f02-647f83f03fa4 | -5.85723 | -43.87159 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 713c50ca-410d-388e-a105-a519769154ea | -3.68591 | -47.63447 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b9b7742-0aa2-38c6-abb9-ba3eea3241bb | -5.65386 | -45.96872 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b846b989-f001-394e-8442-45fef860e38b | -6.95147 | -44.47498 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6d9611a-d438-3289-9678-6b28857de35d | -7.40014 | -44.74812 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9da75c1d-5656-34be-867d-2d019491143e | -3.27493 | -45.84432 | 2025-10-16 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e744b275-12db-375c-97ee-6f9efa06fa59 | -3.29662 | -43.50169 | 2025-10-16 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06ca1fc5-730f-3e28-a6f6-a54d1d730108 | -6.69145 | -40.86801 | 2025-10-16 04:38:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9faf788b-f877-3a2a-98c5-bc52e800630a | -5.88261 | -43.87116 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3566a27-9ce3-3034-8d54-1aeec2391fc4 | -2.25989 | -56.05974 | 2025-10-16 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26f93c71-e744-3dfd-96a3-d59c9df03d96 | -3.26552 | -50.12185 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be5bdcd8-8192-3a81-9399-f738a4822008 | -4.28234 | -48.5887 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 11bf3863-0c31-3c4d-9a5e-66e0b8144a40 | -4.37116 | -43.38525 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2379883a-560a-3576-98ca-671ccd6574a2 | -4.87453 | -44.57457 | 2025-10-16 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bec11b23-ff8c-3e96-93e3-1fbe7f492cc1 | -4.50269 | -50.21798 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f70720f-3ed0-3c9f-a3e9-be21c031039d | -4.67886 | -44.10265 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04a35ed5-e063-3c22-9185-df3dcb729ac7 | -4.42116 | -42.88956 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d67eda6e-f2d4-3c06-a2da-8c660ee399d2 | -4.67629 | -44.10619 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3019dc6-ecb3-39ea-a7ac-c16e7f621337 | -3.15826 | -41.99279 | 2025-10-16 04:38:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec196f23-0ff4-3c2d-88e6-b36430f55d24 | -6.77521 | -44.66322 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d1b9511-c7f5-375c-abc7-323be9132616 | -2.28232 | -48.36149 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f535e45d-5e2b-3d39-a0f6-99dd2469041c | -4.11559 | -50.43125 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e312e7b0-4d3d-3eb8-94d9-e3bd13084c62 | -5.09819 | -44.94344 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f4dd49-e3df-3bda-93f1-78e4d0fa29c4 | -6.4282 | -41.88793 | 2025-10-16 04:38:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5e8c0a76-0aff-386e-9139-24af26b77af9 | -3.51331 | -50.21573 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4505b4ad-a40c-3602-bb70-d2a73bc659d1 | -4.65057 | -47.94965 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faecfbc4-88cd-39ef-b22f-da7023b71e6a | -6.13985 | -41.77959 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1619312b-d67c-3c29-bf95-bfd196cafa97 | -4.28503 | -48.5715 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86551a99-4244-38c2-963c-1d50058b7191 | -4.9355 | -41.71473 | 2025-10-16 04:38:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2cc37161-09df-3229-9920-40afc1be17e1 | -5.33631 | -42.55869 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 03afe2c2-683a-3d59-ae96-7d714a6bcad1 | -7.94913 | -44.12703 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd054d77-e556-3515-a3a9-4255b145a47a | -7.01078 | -43.73299 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1edf53e1-378f-3d19-8824-2ffdb3dc2c65 | -4.8738 | -44.57941 | 2025-10-16 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 09b5a4af-b122-327b-a0a7-96d616ea91e9 | -6.14467 | -41.78006 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6f990a6f-88c8-3f59-a4a0-37fba0b032b7 | -3.60356 | -48.98769 | 2025-10-16 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5afca3e0-41c7-355a-87c9-223ce82246fe | -6.23526 | -41.54838 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d650c731-c6a8-378f-a63d-8670f631d591 | -4.64171 | -43.13186 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7664cdac-d93f-314e-a6b6-19e400ac7351 | -6.40527 | -42.55154 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f64abece-237a-3587-b6f2-c08b94625455 | -7.27824 | -41.96436 | 2025-10-16 04:38:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7bf5cd62-b577-38db-ad78-1fe21fa5b733 | -5.91836 | -42.83496 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 21416469-3daf-3cc2-9fea-51910c3d7cf6 | -4.35755 | -43.3909 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0437e724-266e-33cb-b349-1e644b86e168 | -7.22759 | -41.21191 | 2025-10-16 04:38:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e99c103-d257-3429-952e-c66913eeabf7 | -5.46733 | -42.93333 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| bcdc5a89-243c-3b3d-ad16-1814a66a79ee | -3.1518 | -50.17398 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060d22df-4c5b-3b1b-a470-f9e7a96c4f07 | -3.68846 | -49.57632 | 2025-10-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a17a886-dd2d-33d4-a8e0-d91a758a8fd4 | -2.88224 | -50.72387 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0598c04a-e92c-3597-a267-007462add43e | -5.07944 | -42.90329 | 2025-10-16 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40d85b42-6d8b-36e2-955e-52fbf4e8a761 | -6.22044 | -47.03935 | 2025-10-16 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 784f53d2-2d69-3e15-9859-bab7d673d81b | -5.68485 | -45.16744 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51406726-9f74-3a37-b9aa-b17450a0902a | -3.29853 | -50.17458 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e70e65e7-e0fe-3680-b163-d24c65670a35 | -3.46414 | -51.06429 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0466aa61-354c-3a04-8235-19be06e55a9f | -7.08417 | -44.94188 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 677fa595-1e01-33c0-b6c9-8bfc64c569cd | -4.6664 | -44.09059 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5ad110d-d953-3e8c-b4c4-f35432e7155c | -7.47504 | -42.67865 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 836b6ba8-2e69-3767-9662-8d3f0e8105f4 | -5.88071 | -43.85547 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14f6a4d7-efd8-3368-9984-7be52f62bb45 | -4.39033 | -43.39989 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 90d9568f-9fce-37e7-b2a4-d7edaba59d0f | -7.17077 | -42.51117 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cd902a0c-6293-3156-a804-bf349314ac97 | -5.48547 | -42.93158 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d33e311b-e55f-33fe-8023-8a40f7d341a9 | -6.00677 | -43.12064 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9ae53fa-7626-32a9-bf22-a0a2f5bcb0bf | -7.08203 | -41.96949 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0a95d51f-338e-3e29-876e-9a86c6432495 | -7.16614 | -42.51056 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 33d5a071-8bb6-36ec-adfd-80a97c481f9d | -3.60026 | -48.98718 | 2025-10-16 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2f0345e-a4d9-37ff-8d63-6c38d1f4fff9 | -7.54171 | -44.27853 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac2a373d-6469-3f44-a1db-efc9979ba217 | -5.4025 | -41.15587 | 2025-10-16 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2fd7f836-b55c-32a2-8a94-dd07585470b6 | -8.24168 | -43.4132 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 79bf778a-72be-3a33-886d-f5937f8d15e7 | -7.61888 | -46.47464 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 114d2d65-4365-38cb-9231-ffafb629fb28 | -5.25029 | -43.2275 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 127546e0-1a92-3b0c-ae92-b9974619c4ed | -5.87449 | -43.89748 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cd66592-98fc-3c07-a2b7-228bd0e3f6ed | -3.29688 | -50.01015 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5dae9dd-83c9-3fbc-8d85-97e9143d3c35 | -2.87764 | -50.73082 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2641e223-28e4-3018-af2d-ca4ef18913fa | -7.92643 | -44.12785 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2bf3dd1-8e29-3567-8135-48fa88567c17 | -6.7975 | -45.47476 | 2025-10-16 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6c9a30b-a9bd-3d96-8a52-af26f9c82e21 | -6.33933 | -44.01654 | 2025-10-16 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bb06180-8a93-3c65-b14e-ed0c5070bae3 | -5.61953 | -48.26067 | 2025-10-16 04:38:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e48afc4-b79f-364f-9a85-ef2a56024f0f | -8.20398 | -43.97318 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b43a286-bee7-3153-b41b-361ddd78bf0b | -3.51414 | -52.49619 | 2025-10-16 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 25a11ac1-6dec-3a5a-bf1c-325562f673c1 | -4.27851 | -48.59162 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4fbf76-ec17-3f64-ac69-86e5af04b245 | -6.22846 | -44.15078 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9e7a002-a870-3767-8446-32a32be09e1f | -3.8367 | -47.0746 | 2025-10-16 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6534fed-a35f-38f4-aae8-73d21ee9babd | -2.95207 | -48.5867 | 2025-10-16 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 543106a5-97f8-3819-8ebb-5994d47e5532 | -4.83871 | -42.7984 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 54f23565-d4d9-34b2-80e9-c6c5377425d4 | -4.65789 | -44.09277 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d3ee110-d0ce-3c25-ac03-eb194e8136af | -6.2239 | -47.03988 | 2025-10-16 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05458cd0-3656-3885-af97-479f2572c251 | -2.70786 | -49.85682 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README56.md)
