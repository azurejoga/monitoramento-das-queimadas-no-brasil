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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23eaace9-11b7-3edd-9b4e-c79d10d78578 | -11.91571 | -40.73056 | 2025-10-27 03:42:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 279d618c-5fba-363a-be6d-a50b6958b357 | -8.6957 | -44.44311 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c704016a-a0d9-364b-99b1-d676fef329dd | -8.02712 | -46.77134 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a252136-c58b-3820-9b1a-3b68e2a330ab | -8.35499 | -46.1608 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbfeac8e-276e-3824-ad07-f351ef7ef6bb | -8.64791 | -44.76641 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4da7ab03-98f1-3cc8-b9df-8c3f01e4df54 | -7.83549 | -46.47719 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3ea7348b-d738-372b-a844-dd39f97284b5 | -6.81634 | -41.56525 | 2025-10-27 03:42:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1d5902d-c5ae-3682-b3e9-f8086602b274 | -9.58687 | -44.94271 | 2025-10-27 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 493f2254-aa57-3b6a-a7c0-fcf723c3f0d0 | -6.98605 | -39.11215 | 2025-10-27 03:42:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9d7f6534-907f-336f-9ced-d10d807aafd8 | -7.82536 | -46.43176 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88773b29-3ae1-352a-a559-662038ebf8f0 | -8.12386 | -47.03612 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2626bdfa-6d58-3b97-af47-24e0e338a7a8 | -11.419 | -46.11063 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c30ab42-78a6-3a68-9cfd-a916478075bd | -10.4206 | -47.65395 | 2025-10-27 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c822db0-d28e-3110-954e-f2588c115ae2 | -8.88259 | -47.99995 | 2025-10-27 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1116e1f2-a875-3445-ae2f-f4037b5a4d54 | -8.95971 | -47.18909 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| aeabb5ee-5589-3f91-8fe1-b178e854afc2 | -9.58682 | -44.94967 | 2025-10-27 03:42:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa53cfe0-cec8-3a3a-9f48-0c6aebb220c4 | -7.59173 | -45.69012 | 2025-10-27 03:42:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7ec13af-f0f2-3e32-98e1-187d630eea54 | -6.12667 | -42.45129 | 2025-10-27 03:42:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3fb848bf-8073-374c-91bf-5a0f03a8f709 | -8.8812 | -44.84391 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ed708ea-6aae-3475-b0a1-de1b17b8cc4e | -10.41536 | -47.64799 | 2025-10-27 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e67e11b7-779b-39b3-819c-0abc6fe5a245 | -7.33939 | -42.44728 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bb37bd05-7635-36b5-9b99-c45093c26d70 | -9.17973 | -44.57204 | 2025-10-27 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6aefe162-1fb6-39a3-9d53-0ebebc33db95 | -6.42856 | -42.02456 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8f071bb8-822d-32c4-984f-31d0b5037bde | -7.78472 | -45.37737 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c06af927-5dd1-3496-90e4-3b684bcffc60 | -9.26141 | -45.58038 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2b46ec3-809f-3b4c-9ab0-26079cd67d72 | -7.84484 | -46.49372 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4bca0aa-bffa-3f18-86b6-4be72d2b1b25 | -6.14609 | -43.13234 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 68b9811b-8e4e-33ad-985b-3de16e0a2a26 | -7.84489 | -46.42658 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d35b37ef-4bae-31e1-bac4-c3fe2da6f39b | -7.7619 | -45.39411 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 564a9052-3412-3046-b8db-56dd31eeaec7 | -10.31456 | -47.18922 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bcb60da-0ee7-3f81-bbdf-a663c8523be8 | -6.8864 | -43.57957 | 2025-10-27 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 14817938-c8fc-381b-846f-b3d7df76d917 | -10.01806 | -45.00974 | 2025-10-27 03:42:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d37fba67-0589-3411-bf22-82238d504c6e | -9.52387 | -40.30361 | 2025-10-27 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b632144c-a039-399c-b57c-12b92c8a866a | -6.98531 | -39.11665 | 2025-10-27 03:42:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a1d23283-0182-360b-b2c6-f348adbd2cf8 | -6.43228 | -43.14024 | 2025-10-27 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f29833a-b104-39b2-8b0f-0de0af2113ec | -10.31545 | -47.1846 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8363f6b7-6dec-35b2-b894-f09c328d4201 | -11.41489 | -46.10212 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa63c4c3-dcf0-376f-b2b6-17503fa7d509 | -9.12853 | -45.86679 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a325313-bab3-3552-9c87-a04329a0398c | -11.67099 | -41.32235 | 2025-10-27 03:42:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 781a29e2-ca89-3343-a4bb-83f137430372 | -8.0696 | -46.95023 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79ef8396-53e6-3919-bc2f-48d98116de2b | -7.0571 | -46.75833 | 2025-10-27 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 237fb517-34a1-39d9-ab15-cab1973f629d | -7.06329 | -46.75946 | 2025-10-27 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 89605f94-4dd6-3693-9e7b-ba2e69f12773 | -7.81214 | -45.40465 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bb9c7691-3ac7-30ff-a1eb-9399a7ffac5b | -7.80817 | -45.3947 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c115e93a-cb1c-30c6-b36c-c0718792902e | -6.89048 | -38.27904 | 2025-10-27 03:42:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b0f6db48-3ef9-364d-a9e7-08c535592c9e | -8.11846 | -47.03073 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f907b02d-230e-3ac2-a627-56304b1b4964 | -7.97105 | -45.47507 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 505dedb1-2ef1-3fb7-98bb-f7d04d8f6352 | -8.03244 | -46.7426 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 724a1175-56ad-3d70-8bc7-788bc6321a3e | -7.87569 | -47.25498 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e62e741a-5506-30a9-b29a-90a5439edf37 | -6.88216 | -45.1535 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98c9d687-e736-3abd-a6bd-12d31976a39c | -8.69859 | -44.42753 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d037398-6496-3189-9ce0-2b0975e6570d | -8.69659 | -44.4322 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b080bc4-abe6-330d-9d89-5230d54c5ef8 | -9.26817 | -46.3976 | 2025-10-27 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bd85bd5-c500-393f-bef9-76299b7ce13c | -6.26023 | -41.82702 | 2025-10-27 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9fb31fd-887a-3e2c-a489-a465894b09cb | -7.82956 | -46.47568 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9937efee-c529-3595-ac12-507a3aabd767 | -7.83886 | -46.49247 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddd166f8-12ac-364c-9a9c-c1959838510e | -11.9734 | -44.30921 | 2025-10-27 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39937f26-e7d6-3a2c-af0a-ff693a77f7a7 | -7.96267 | -45.47451 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e6dc8d8b-659e-386a-a2e2-6c2a4da5c779 | -7.24484 | -46.96095 | 2025-10-27 03:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d7798b4b-d317-3eaa-a59a-ea2b12981127 | -7.24011 | -46.96547 | 2025-10-27 03:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a5359ff5-1969-3d6b-bc0c-f438acc3799a | -8.02801 | -46.76654 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46d38c24-50cc-3aa3-8ec8-b75215719839 | -10.33844 | -47.22754 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7e69d65e-4f06-354d-bfec-6e2d810e5eae | -8.53168 | -45.56551 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ff09213-bf8f-3794-9921-e0e1a2a343b2 | -8.04355 | -39.87042 | 2025-10-27 03:42:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 958fc371-8302-38a9-8b8f-3d47f086ef22 | -7.81289 | -45.40055 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 188769bc-963e-39f6-b191-f55e3e2aab74 | -11.64297 | -45.23478 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 156d0cb3-fa20-3793-a638-17d73f898566 | -9.99562 | -47.20138 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d59cf810-91e8-377f-8835-9097a2d7b3d3 | -6.59486 | -42.67572 | 2025-10-27 03:42:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a042297a-e320-3f4b-8c57-f908d64e2882 | -7.78159 | -45.38176 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2b22bae-8742-309f-8089-2e7a49516af1 | -7.86947 | -47.25344 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34346f00-3c24-3828-84d6-f53c59841928 | -9.47978 | -46.8554 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74910545-9826-3f1e-aa50-c49db4ce46d4 | -7.77918 | -45.37598 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e410dcc4-cd53-3549-85e6-a79ad22fb20a | -7.08927 | -39.56312 | 2025-10-27 03:42:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02d67278-1fdd-370d-8623-92388b7ac823 | -8.87591 | -44.84284 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6506a8a1-8a6d-30ec-bb14-b9ceb4f7c1f8 | -6.63586 | -44.63053 | 2025-10-27 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e90be31-1a05-3405-bb67-9ae3b339637c | -8.58088 | -45.11043 | 2025-10-27 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f410d5cc-8b1a-3ffa-8f46-a318659c40c6 | -10.3542 | -47.17756 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b5893f1-eba2-30d5-a9c4-7559a76d475f | -7.9352 | -47.19644 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36782a16-ee89-3ab7-8dc4-239b632addc7 | -10.41158 | -45.30487 | 2025-10-27 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae6f30f8-e9ce-3a0c-ab26-5fca8f339634 | -8.09998 | -47.06146 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35bd1f05-ac5d-33fe-8165-9894220562d3 | -8.58214 | -45.11117 | 2025-10-27 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c7f8323-e3f1-3189-8ea2-648a29abca09 | -10.91489 | -48.02591 | 2025-10-27 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdb1a4b9-a253-3523-b2ab-fcec352267a8 | -12.55461 | -39.62766 | 2025-10-27 03:42:00 | NOAA-20 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a832cc54-b5fe-31c2-a78c-2f074f01d040 | -8.06283 | -42.49048 | 2025-10-27 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a1ebbcc-6e79-39e8-99bd-d0ce4dfcabfd | -7.24537 | -44.96427 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b6b3030-65a9-354d-8dfc-bb1ae7858177 | -7.68756 | -42.18472 | 2025-10-27 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6766ae7-6b5b-3c17-a75b-8a2f77e0fa58 | -9.26732 | -46.4021 | 2025-10-27 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29a19071-4f33-3930-a269-8c93d328a5ee | -8.70007 | -44.44276 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9652b245-1954-355d-a014-eafe13462ccb | -10.04295 | -48.17241 | 2025-10-27 03:42:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9b9aac1-2035-3e88-9780-385bc5ef7b0f | -7.35244 | -42.45465 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dfc5da2b-848f-3644-bad8-d384a9deb697 | -7.23638 | -44.98254 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b767de2-0c7a-3a79-8a61-c1a81ce97114 | -7.43172 | -41.87004 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b3aeb976-00b8-3928-b47d-40a994d0906b | -7.87256 | -47.25294 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d274b08c-16e7-38ea-ace9-4b8db2ddd812 | -8.14121 | -43.41753 | 2025-10-27 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ddd1d82-2087-3b5c-8ace-9af335212a36 | -11.42575 | -46.10513 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0761271f-69bf-3658-a4d8-b7ddf9acdfee | -6.43162 | -42.03405 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 18d96433-df40-3f6e-b2df-ec5c0f7b8bfc | -11.90991 | -43.83244 | 2025-10-27 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0c9326da-746d-375c-a87c-14cbfc91f68d | -9.26207 | -45.57684 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ffffa3b3-82d0-3137-b094-d78b29bda677 | -6.25942 | -41.83166 | 2025-10-27 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9e978349-07e8-3f02-84a9-90e207160872 | -7.81364 | -45.39644 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |


[Clique aqui para ver as próximas entradas](README19.md)
