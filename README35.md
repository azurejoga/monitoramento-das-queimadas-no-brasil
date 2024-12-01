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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b1dc0ca-899a-391f-8ab1-f47118b32947 | -3.72531 | -54.5301 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e28cf43-7594-3b81-91b1-d1af395098ea | -4.00394 | -54.61506 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0572177-a991-3305-9fa7-2d410b2b74c1 | -6.35403 | -44.79184 | 2024-12-01 04:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 079f26da-7be3-30c2-86b3-f74d15fe7af7 | -3.74157 | -51.83348 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d11ba504-61e6-3467-80db-0efa376deb6a | -3.25137 | -53.63478 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76485d9e-69e3-3218-b024-4ea4a2ea62ee | -7.02581 | -44.84471 | 2024-12-01 04:23:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f88b7ee8-2ae7-3033-89c3-5a91b3fa951f | -6.31436 | -43.46198 | 2024-12-01 04:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d5591d20-2e5b-37b1-a797-6770cf11a592 | -5.53995 | -45.42864 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| add4729b-3fa4-3642-9095-ee2e5c6437df | -6.08995 | -43.55239 | 2024-12-01 04:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fe95a10-c4d7-3047-bcb7-9705bbb54cb1 | -4.07613 | -50.02605 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cac387d-fd9a-319d-bcf7-158010751b05 | -3.69715 | -51.80312 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 65d112e0-cff1-3ddb-a30e-75f7c9342347 | -6.67366 | -39.33059 | 2024-12-01 04:23:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9071291d-bef8-3440-8ec8-2340502b5a77 | -10.65867 | -44.49472 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e965d8ee-88a3-38f0-b5ee-b6104888c895 | -4.14789 | -48.23593 | 2024-12-01 04:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7157cca7-fb36-321d-8e38-bd2203e7ba4a | -6.19368 | -44.42368 | 2024-12-01 04:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9beb6458-9150-30c0-a4f4-f7d6af8b1a16 | -3.86511 | -50.53875 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acf367bb-2f63-3b78-912c-cfd875fda812 | -5.10762 | -50.61599 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9b403a7-0456-3482-bb04-dfb490c2b570 | -3.31387 | -53.86839 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fc5560d0-51f8-379a-9aa2-405aed249869 | -4.61697 | -45.50124 | 2024-12-01 04:23:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6991263-3b57-3898-8756-fede250d2047 | -3.13445 | -54.53286 | 2024-12-01 04:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 7e954f97-b38e-395d-97f5-5c8713e04798 | -8.83052 | -44.78339 | 2024-12-01 04:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a898c745-0fda-3ac6-ab6c-de886ebd9b3a | -3.8058 | -51.00423 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bde636e9-9d64-3663-8818-b625e3bac218 | -3.50082 | -53.83278 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f46a0b84-9dc0-314e-b059-306d7ed59ab6 | -10.65922 | -44.49108 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e18f8898-1e25-3163-a4f7-86f258c3848c | -5.3634 | -43.41586 | 2024-12-01 04:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90213eea-28b5-338e-874b-8f29b88bfa09 | -4.55691 | -45.73013 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afd9cc70-e5ce-3e6e-bc09-b26b8c0b60ad | -8.13402 | -44.47267 | 2024-12-01 04:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac317681-fa8c-398c-87c6-83e38250352c | -6.71713 | -47.26762 | 2024-12-01 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f85b08e-9d39-3780-9a3d-6acf098a9d73 | -5.484 | -46.3463 | 2024-12-01 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8352e3be-53ed-3c48-8715-f4b4a700d285 | -4.26728 | -48.3603 | 2024-12-01 04:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9f1d28a-db52-31bc-964c-fe1f4a8cb45e | -3.94471 | -51.099 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 256a98f7-9672-355c-a1dd-deb9faff9169 | -4.6878 | -46.80412 | 2024-12-01 04:23:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e6fc0f9-7c49-35e1-b00c-51f43ac52e4e | -3.25856 | -53.62525 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bfd26643-e90d-3dcf-913d-96f4027fe190 | -5.69432 | -46.30532 | 2024-12-01 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 856c312f-03bd-31e9-bafb-18ebc52f5c5d | -3.25681 | -53.63556 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80794a51-b4f7-3e46-ae90-d35857842832 | -3.26648 | -53.64439 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 85e55115-3906-3a8f-b258-4d772ef8fe15 | -3.3029 | -53.83339 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f99d37ea-34a1-3355-bd78-f63325574267 | -8.93632 | -44.24835 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0ae9c95-9f0e-3555-9daa-6f5340c8d2df | -5.58483 | -43.61282 | 2024-12-01 04:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a57ebbd8-f3c8-35a8-9e73-6f668ad0c7aa | -4.18522 | -50.67783 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 368eff9e-0eb5-3464-8e92-6e6b65992646 | -10.93941 | -45.12457 | 2024-12-01 04:23:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d71910f-fa74-33f5-a700-1793d6a15c69 | -4.34206 | -50.76668 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bc9d260-647a-33ee-99a8-4c5a00ef077f | -3.72712 | -54.52971 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d20343bd-548e-31fa-8a81-03c0c10790ec | -4.8432 | -45.83309 | 2024-12-01 04:23:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33a1013f-a80c-3ccb-aae8-5aaa253f39b0 | -4.85706 | -50.71228 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bd2f274-9042-38dc-979d-67f1412ba1f2 | -4.76076 | -50.99235 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4dd75b38-ad59-30c9-8066-19ae833494e9 | -6.9254 | -43.53975 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a3de40b8-ee22-3382-8d0b-c86f7f23b155 | -6.76184 | -46.52526 | 2024-12-01 04:23:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79422d46-2882-3d66-92b9-3cf6c0faaaa1 | -3.70607 | -51.06377 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 641ce209-ba01-3632-8a17-7ebfe65a0a1a | -10.66148 | -44.49887 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 790f40d9-aca6-3300-af96-0737a3a71fe2 | -5.79945 | -49.98787 | 2024-12-01 04:23:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86e6b13c-915f-3d04-9d87-4e734c761d0b | -3.66779 | -52.29697 | 2024-12-01 04:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9434cf6-9692-33b6-bcea-ebfaaae1488f | -6.15146 | -52.04599 | 2024-12-01 04:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d26a3fb-1d02-3241-9525-6ea3e07a4a6a | -4.61826 | -46.4711 | 2024-12-01 04:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cb65e0c-8c3f-3723-bd34-a70fde8d419f | -4.5689 | -46.29692 | 2024-12-01 04:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e46cd0cd-8109-3860-bf28-f2ccc8a030d9 | -3.69394 | -51.33831 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55da8134-bfe7-35c4-97c6-84a91ef8c249 | -3.26706 | -53.64091 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2dc7ec54-4aa0-3ae3-bf05-0465eac6209d | -10.60726 | -52.81672 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 16848225-e6d0-37c4-8efd-41c9ea935ce5 | -3.25505 | -53.64601 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b26ccee-3ec7-3db9-89a1-638bdcdca19a | -8.83824 | -44.77742 | 2024-12-01 04:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ad930de-41bb-3ba6-8456-efbcfe25f3d1 | -4.55132 | -45.72206 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 557c8126-d289-3699-acdf-5632a3b5bbca | -4.58886 | -49.60152 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e219c0f-26a5-3b7b-a711-4b182e19351a | -5.92613 | -43.9328 | 2024-12-01 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9d9d540-ca85-337f-a0b7-1b3d1dc6a8ee | -4.58469 | -50.96563 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8c1f20d-96f0-36a9-ac53-8bea4e81a6b3 | -5.31452 | -50.57093 | 2024-12-01 04:23:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5d68df8-7e70-39a8-8362-33da837058ba | -3.6347 | -54.44232 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6123bb78-1ded-3987-88b1-912d1ac23e36 | -3.33386 | -53.37357 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c5fa3a6-e5c2-3fdb-bbb9-a1bbf037c259 | -5.18925 | -43.95004 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4779ef83-9465-3e29-ad16-76fe02aed56c | -3.49958 | -53.84029 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5fcf1c87-2962-369d-897a-2e5fbb97b477 | -4.61781 | -46.47448 | 2024-12-01 04:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85d793f9-4df6-3077-a4fc-c0e88f678712 | -8.4489 | -45.11966 | 2024-12-01 04:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24b8f1eb-05e6-31c4-a245-72685b0da0e4 | -3.63786 | -54.44369 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d7d1c76-dfae-3dfe-8b7a-5bcb7b504f46 | -3.2974 | -53.83252 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6926f3dd-a488-3d83-8c73-c8fa9f4849d1 | -3.33498 | -53.36689 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 472cdab7-3af2-3d32-88d2-ba528ac0a2f4 | -3.21495 | -54.08699 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17d68aee-bfe1-3c8f-8d65-13d90e1ec48e | -4.1032 | -49.0775 | 2024-12-01 04:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7bbcf880-eced-34ac-9660-7e6c3e640011 | -3.72599 | -54.52599 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d08e36b2-d342-374f-8a94-24a695a49a5f | -7.95253 | -44.87748 | 2024-12-01 04:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a6c11a6-f8e3-35ce-91ce-65401d39151d | -8.84093 | -44.7599 | 2024-12-01 04:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f89a9779-9105-3cad-8246-de11778bf0b4 | -3.30784 | -53.86948 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 032157c8-4ba6-3c26-9736-47932785818b | -8.83438 | -44.7804 | 2024-12-01 04:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ec2ef93-e09b-3450-899c-ca4a8ee41c7b | -6.71243 | -47.27472 | 2024-12-01 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dc9fa36e-851a-3238-9072-8fe5cb791507 | -6.71589 | -47.27528 | 2024-12-01 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8057b533-8bd8-3dfe-998f-e354394798d5 | -6.14687 | -52.04487 | 2024-12-01 04:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33b48ddb-982a-3381-9280-7e7ec29ba51e | -3.80364 | -52.14455 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f67e7a5-46f8-3ad2-ac12-7ea7b942d05b | -4.9008 | -47.14526 | 2024-12-01 04:23:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70bb5d80-1ad1-35b7-9d93-5ee2413f6b17 | -5.18817 | -43.95699 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 407aed5a-50c2-3a94-b2ed-6f55b78b7f4c | -6.19037 | -44.42317 | 2024-12-01 04:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d108a36-f74f-36de-a12a-91c314431871 | -3.82333 | -52.2557 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cba07441-7155-3fed-960e-05952aa92571 | -4.78315 | -49.45427 | 2024-12-01 04:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1489abc-b8a4-3125-9485-cb370db464a4 | -9.5255 | -37.03015 | 2024-12-01 04:23:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| be5a9a3d-a4f9-32ef-9455-569957abd438 | -5.01962 | -43.23898 | 2024-12-01 04:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9bc0fbe-17d7-30ce-85b7-989231a54ecd | -4.67652 | -46.37 | 2024-12-01 04:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a412ed3-a7e1-35b8-915d-463ef719de53 | -3.21495 | -54.22581 | 2024-12-01 04:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4abfb20-a69d-3791-869e-b48db8cdafbc | -4.10396 | -50.98388 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14d3eb39-0c57-38b2-b3fc-162f1127f84a | -6.71305 | -47.27088 | 2024-12-01 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 437942d4-9c1a-3788-ac24-76aa43d3a6a1 | -4.8607 | -50.71712 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a19399a0-32a0-3d3f-8ffe-0b8e2a76f1f4 | -6.48848 | -44.16657 | 2024-12-01 04:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 027f8fe8-dce5-37e0-9a75-ed3d967f8025 | -5.53941 | -45.43211 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e014e31-70ae-348d-af5a-2a48c32e4cbb | -4.55747 | -45.72659 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |


[Clique aqui para ver as próximas entradas](README36.md)
