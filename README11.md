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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccb54c74-c5a0-3a79-90f9-8fe0c260fee0 | -2.907 | -50.382702 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb80107d-89b4-3f4a-9ddc-a703e8aa8199 | -5.6127 | -45.234901 | 2026-09-15 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04506449-9cc4-3c64-8151-765d17838d35 | -7.545 | -46.8582 | 2026-09-15 00:25:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff96ac74-4540-3e5a-aee9-d9e26e090033 | -7.0813 | -42.125301 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4def1a8-0540-3f16-90cc-c4c4d62a4ea0 | -1.7822 | -54.471401 | 2026-09-15 00:25:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 348330dc-c0c5-3910-b22c-e0fd31ba52c6 | -7.2077 | -46.133801 | 2026-09-15 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf79b694-6703-355a-b2ae-d32b32fdc21b | -15.9884 | -43.266899 | 2026-09-15 00:25:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4fb63eb5-745c-3fa9-9b75-2719dd7a1ff4 | -4.1523 | -40.857601 | 2026-09-15 00:25:00 | METOP-C | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8b4319dd-561b-3466-aaf7-7ea60f59d7e8 | -8.0898 | -50.9561 | 2026-09-15 00:25:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92de395-2e58-3488-be47-0db325b3f180 | -6.6136 | -44.201599 | 2026-09-15 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b13260f-bef4-353e-a9fb-b09ba6d857f9 | -10.5719 | -47.738098 | 2026-09-15 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cca6aade-d1d9-3abd-9596-1d47c40a970a | -8.791 | -45.895 | 2026-09-15 00:25:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7465b871-95f4-3216-ba83-c6f5a3e7a77f | -3.5328 | -53.959702 | 2026-09-15 00:25:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d49a554-36b4-3e2c-9f64-f86f9d29d02d | -6.7639 | -42.7547 | 2026-09-15 00:25:00 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40eb0df2-57b8-33f7-8bcd-a371bfd90962 | -7.5565 | -46.863602 | 2026-09-15 00:25:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a7d443b-98fe-3f64-bafa-19ec02e1a1ff | -11.1735 | -42.8092 | 2026-09-15 00:25:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 147be377-28dd-3b9a-8ee9-18b9bab2119e | -6.3372 | -43.361599 | 2026-09-15 00:25:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58543388-464e-3afa-85f9-e8008ea69cd3 | -2.8867 | -50.429199 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ea91695-a442-384c-9e42-9889cabb4f97 | -9.3183 | -44.349201 | 2026-09-15 00:25:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aaca7546-e51f-35a7-a7c9-48c06a3b9e20 | -8.7966 | -50.489799 | 2026-09-15 00:25:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b77f21b9-ec89-39c9-bc70-150dd49798eb | -15.256 | -40.9972 | 2026-09-15 00:25:00 | METOP-C | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 74b3ff4f-bed4-3c94-8cc9-7e758974e6ad | -6.4351 | -43.071701 | 2026-09-15 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c50f55f-da0d-386c-9ed6-0e06359acb07 | -10.7968 | -46.222099 | 2026-09-15 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bcf0df10-f9af-34ba-abf6-97136d7f8bbb | -5.5494 | -43.435001 | 2026-09-15 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb3df3f1-31a2-378c-92f3-2643a19f68e6 | -12.4937 | -44.637001 | 2026-09-15 00:25:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2d2dacf-9292-379a-a50d-6ba9e0340e02 | -11.1931 | -42.8046 | 2026-09-15 00:25:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8029001a-5541-3613-a68d-3cd0cec6cfa5 | -7.0828 | -41.7799 | 2026-09-15 00:25:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a6dd281d-e555-3f8f-89a9-fb80e6ae8167 | -6.2607 | -41.971001 | 2026-09-15 00:25:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 431a9d6e-2c3d-339f-9cca-8341c05bf9b3 | -12.0309 | -47.809502 | 2026-09-15 00:25:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b10859d8-9fc2-31ff-a7e5-256a851b9553 | -11.2463 | -43.442299 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70894c02-ee77-3d26-8e11-16a656a93ef3 | -7.0923 | -41.820499 | 2026-09-15 00:25:00 | METOP-C | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51014b10-6378-3778-a44f-ba61be2f6592 | -16.3358 | -43.442101 | 2026-09-15 00:25:00 | METOP-C | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d40a054e-4544-3480-86e8-a9e5b434f4cc | -11.251 | -43.4632 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 088da2fa-df81-3edb-95b4-f64257a01e70 | -11.2479 | -43.4492 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd1a06ea-bd7d-3891-9e82-5f6f2d30b64b | -10.7853 | -46.216499 | 2026-09-15 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e1ddac4-1b45-3594-b544-5a34ddf3b2cf | -13.2128 | -51.6278 | 2026-09-15 00:25:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9aea3db-37d3-3b2f-8471-d9b0d473f6d6 | -11.2397 | -43.4585 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 833e2c68-7cce-34bc-92b7-cb0f600397ef | -6.7233 | -48.109798 | 2026-09-15 00:25:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5268aa65-9edb-3d02-a920-07844db60583 | -6.1067 | -44.0611 | 2026-09-15 00:25:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4e50c81-1451-3fe3-b6f4-e11016e4aedc | -11.8089 | -46.578899 | 2026-09-15 00:25:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b917c1cf-8090-38eb-b91d-2c7f6160deb7 | -10.4342 | -48.626499 | 2026-09-15 00:25:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c12c8e4-f2d6-31ee-a72d-db8620c0f4c1 | -11.2495 | -43.4562 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8fad79d6-ecfa-3094-aed4-5b8c1383b3da | -7.4814 | -42.114799 | 2026-09-15 00:25:00 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f4bb143e-169d-3d35-87ce-b63bb8482eb6 | -5.5575 | -43.425499 | 2026-09-15 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb1a251f-84fe-3192-9479-db3c56b10a2f | -5.8902 | -49.959301 | 2026-09-15 00:25:00 | METOP-C | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faefb6cd-a851-3f0a-9152-dafc75e1beb3 | -9.8769 | -47.794899 | 2026-09-15 00:25:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 642bc4cd-c5d1-3503-a522-44f5f19a5444 | -16.3342 | -43.434898 | 2026-09-15 00:25:00 | METOP-C | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7a8f154-2ee7-39c6-bc6d-e0bba53a3087 | -6.4317 | -43.056999 | 2026-09-15 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d0c1603-8b84-30e0-91b7-d530fc16d7b6 | -13.7217 | -48.975601 | 2026-09-15 00:25:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7cb4cba6-6664-320a-9bfa-4cc87fee7af1 | -7.966 | -43.981899 | 2026-09-15 00:25:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67450728-2f7b-3cc0-9780-696e82c9f267 | -10.4385 | -48.6465 | 2026-09-15 00:25:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 312d53ea-8f2b-3a81-8353-9eb5f79c4e80 | -15.2536 | -42.790001 | 2026-09-15 00:25:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c4a569a6-3704-3837-9b5b-280151f46330 | -15.2617 | -42.780602 | 2026-09-15 00:25:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9ca9bf53-0140-3754-a487-0c38ee56bbe3 | -15.5798 | -48.805801 | 2026-09-15 00:25:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09c63b98-bdd9-3d04-98ed-00e260f7ee75 | -15.2829 | -42.7831 | 2026-09-15 00:25:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57252edd-92d8-310d-957d-c404e555f2c5 | -5.472 | -45.115601 | 2026-09-15 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc5fcc7b-c39a-3539-a9d6-2cd69e948573 | -3.2261 | -50.569199 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7a53a72-4481-3177-8410-343aee05f8ef | -15.2861 | -42.797199 | 2026-09-15 00:25:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c7922747-2c0b-397b-9714-84a194ff604c | -8.5932 | -44.470001 | 2026-09-15 00:25:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a363ff6-8dbd-3f30-b012-4ec99f378131 | -11.889 | -43.8214 | 2026-09-15 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 111bc56a-56cd-3be8-89ea-5f0e1ef956db | -13.5096 | -44.159401 | 2026-09-15 00:25:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7a5a1e9e-ef0a-34d0-95cb-0502fb004e5d | -10.7951 | -46.214401 | 2026-09-15 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2780a101-8f5d-3193-a2a6-6bd620253dbf | -4.5105 | -54.9389 | 2026-09-15 00:25:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7bf7667-5fc7-3132-9c05-c446f2d7371d | -4.6563 | -42.081402 | 2026-09-15 00:25:00 | METOP-C | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5bea9449-3c7f-395b-b881-b23f6d78e308 | -4.1499 | -40.847698 | 2026-09-15 00:25:00 | METOP-C | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5882b35f-2d0d-397f-9e8c-d10c02a9e04b | -7.6195 | -47.285702 | 2026-09-15 00:25:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d266dcc-9662-34ef-b3d2-3d4d7c8c75f3 | -7.7299 | -44.708401 | 2026-09-15 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e9ddf2a3-7306-34e8-9464-9e07a20b313d | -15.5312 | -41.7859 | 2026-09-15 00:25:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfaaefcd-1b04-3f51-809b-ee68bfc40aec | -7.0166 | -44.609699 | 2026-09-15 00:25:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83993e9d-6dbf-3085-b134-2e50d3f6dc93 | -6.4219 | -43.0592 | 2026-09-15 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55d45839-6f79-33a0-8ea9-ec2370a52f8d | -5.6105 | -43.564999 | 2026-09-15 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f732802-1581-3f15-a35f-0f81bbc6ed09 | -15.5383 | -48.801601 | 2026-09-15 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 310ef3b0-2758-3913-ba97-3f9007323324 | -15.9915 | -43.281101 | 2026-09-15 00:25:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d2fd1569-b3f3-34f8-bc62-f8be3693833b | -9.361 | -50.167301 | 2026-09-15 00:25:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10662fc1-4a6e-34a1-a94a-68392650f8b9 | -11.1866 | -42.821098 | 2026-09-15 00:25:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d5fa5eff-1790-387c-9c37-ba2cd8c6d162 | -8.7894 | -45.887798 | 2026-09-15 00:25:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dc414d8e-af9a-31bd-af49-573dc7f15579 | -14.1689 | -47.079102 | 2026-09-15 00:25:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 963e4c8a-d3da-334d-a41d-f7d0a72e3f11 | -4.674 | -42.0686 | 2026-09-15 00:25:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4229519a-a1b3-3fd1-bf6a-97db67b3967c | -10.5738 | -47.747002 | 2026-09-15 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afd90a54-d35b-3b2c-834f-ebb851811ab8 | -10.858 | -46.313702 | 2026-09-15 00:25:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91dc5504-6d5e-3592-8779-1f04e7f05a99 | -8.5045 | -50.124901 | 2026-09-15 00:25:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7862d94-4c7b-3179-a42b-7939025ecb98 | -5.4293 | -43.986698 | 2026-09-15 00:25:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bbdacfa-bc4f-36e2-8d78-7b1590304833 | -11.2349 | -43.437599 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5df444b7-f5be-3a12-b34c-b910d2b824f6 | -7.0831 | -42.133202 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08a80438-e3bf-3db7-a300-a810b79cebd1 | -3.2308 | -50.59 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 600802a7-f571-3f31-a097-8534c7c14f17 | -6.7604 | -42.739799 | 2026-09-15 00:25:00 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79d3d33d-03be-30ca-a900-cbc4bb58bbfa | -17.315901 | -42.519501 | 2026-09-15 00:25:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 977fc951-e751-3280-949b-5c524a94c083 | -12.5495 | -47.116901 | 2026-09-15 00:25:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86525de6-85c1-392d-ab33-d2c8cad13c5c | -10.653 | -54.114498 | 2026-09-15 00:25:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47a5544a-54f8-346f-a802-1942a392ec28 | -6.335 | -39.375599 | 2026-09-15 00:25:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 671c3eb5-4832-3f35-b5c2-7cf2e40b462c | -7.5611 | -41.838402 | 2026-09-15 00:25:00 | METOP-C | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2b0c585a-401e-34b5-9422-a8a5cf6d80a7 | -2.8597 | -49.626999 | 2026-09-15 00:25:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bd49c91-ae8b-338b-88ea-e06d15f7ac6e | -2.8941 | -50.417 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee007da-80af-318f-bd9c-d4d093fffa78 | -7.5615 | -44.919701 | 2026-09-15 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c14ccdb1-c33c-3aa9-9f93-e8b6a0ce58b1 | -13.5553 | -43.5336 | 2026-09-15 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02273113-1c9f-31a9-9599-33a26ec4c526 | -8.3936 | -42.2187 | 2026-09-15 00:25:00 | METOP-C | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6f4e9cc6-c797-3631-bc3e-76472ea0ee66 | -9.5162 | -40.328201 | 2026-09-15 00:25:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 515f78cc-6b56-3b6d-8687-cbcb91fecbef | -11.2412 | -43.4655 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3e964fb-db97-3735-a79e-e53739849412 | -11.1686 | -42.787998 | 2026-09-15 00:25:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 86ae0972-6941-3257-8897-53b83643c758 | -17.473499 | -43.660599 | 2026-09-15 00:25:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
