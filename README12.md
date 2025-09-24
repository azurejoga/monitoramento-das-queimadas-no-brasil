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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5cbc65e-c0bc-3133-86b8-3c025f863c07 | -21.00406 | -47.38302 | 2025-09-24 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3dac500e-eed9-3fda-9421-7df1e5cec957 | -23.37539 | -50.31075 | 2025-09-24 04:04:00 | NOAA-20 | RIBEIRÃO DO PINHAL | PARANÁ | Brasil | 4121901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 524ad604-e177-3fb5-826e-0c15dccc4644 | -21.2274 | -46.98292 | 2025-09-24 04:04:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee345227-fbe0-31ed-9b49-d279184fa1db | -20.37071 | -42.42475 | 2025-09-24 04:04:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fadeea46-9dcb-343a-856a-19534dea7b71 | -20.61704 | -45.67632 | 2025-09-24 04:04:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cc142147-b8ad-331b-b3d9-aee873b5fcb9 | -22.45997 | -48.98087 | 2025-09-24 04:04:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d06c833d-8d8e-31f7-affc-ce16010f647a | -20.09092 | -48.29899 | 2025-09-24 04:04:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1e10ab8-7610-34e5-8479-7507a0b31854 | -20.9552 | -43.07421 | 2025-09-24 04:04:00 | NOAA-20 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a5dd1773-0f5c-39e4-83d7-3400c3203221 | -21.00034 | -47.38217 | 2025-09-24 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a7c35f2-be75-3705-b086-8950d3360e54 | -19.55436 | -49.25962 | 2025-09-24 04:04:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4222a1ee-8d9a-351c-8575-9d74fc253669 | -22.61122 | -49.02192 | 2025-09-24 04:04:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 472738f6-e8ad-344e-b85f-d960d5f4becd | -22.3772 | -49.47581 | 2025-09-24 04:04:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7d17e05-8eae-3c4b-a3b4-bfbb95c4f110 | -21.00323 | -47.38758 | 2025-09-24 04:04:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3daf5a20-fb16-3c1f-84a1-60929cb34ad8 | -22.37892 | -49.48904 | 2025-09-24 04:04:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32dd6d84-420f-3521-b9d6-9bc5acadfa53 | -19.2235 | -43.74974 | 2025-09-24 04:04:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4c3ee42-91fc-3127-a037-7d4b74651200 | -17.94844 | -55.87839 | 2025-09-24 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aaa7225c-c66c-3de1-89bc-092789822dd8 | -22.6087 | -49.01331 | 2025-09-24 04:04:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8de7f4e1-bbcc-3b94-b894-47e7064d4c61 | -19.94438 | -44.71868 | 2025-09-24 04:04:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf3ac8cc-8ef5-3e0c-83c3-376503e67fa1 | -27.44937 | -48.44148 | 2025-09-24 04:06:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0f73a74f-31d8-3c12-abd2-ca8e7a3cc1c4 | -29.77489 | -51.17995 | 2025-09-24 04:06:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| a09a5429-0a32-365f-a6a8-97ce7d94a5e6 | -3.63103 | -51.91055 | 2025-09-24 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b892f4d7-772a-36b0-8250-16797be52ee6 | -3.41553 | -52.6785 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 21f10a2a-4e60-380a-a217-86858793a3bc | -2.97035 | -49.5704 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d970da7a-2353-3150-b3e2-87ed6d2eb2ff | 0.93446 | -51.19999 | 2025-09-24 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32744f1e-6007-341f-a9da-30f57f41d6b4 | -0.99324 | -47.06221 | 2025-09-24 04:49:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9213528d-5d84-39d2-a533-1c2f5cda84f7 | -3.18778 | -48.81255 | 2025-09-24 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e40e460d-801b-346f-8a72-410c27be40a6 | -3.79882 | -47.58876 | 2025-09-24 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f05e1fb-c27d-3bf9-9b48-8efd32c75467 | -3.69725 | -49.01093 | 2025-09-24 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b6ad27b-41d9-39d4-9934-12acb309f6c9 | -1.08768 | -54.11343 | 2025-09-24 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3542cd1-affb-32d5-9840-072f47ba9618 | -2.96976 | -49.57421 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f274fd44-512f-3482-b173-6276dce34fa3 | -2.80427 | -52.47696 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e5b356e-6cbf-37c9-bf4d-ebabb80a30cd | -2.79445 | -49.59899 | 2025-09-24 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| caffceae-86d1-36dd-89be-0203038b54db | -1.08479 | -54.10897 | 2025-09-24 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73b98e15-acdc-33d0-a80d-f2368d698787 | -3.41276 | -52.67453 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 58bc8965-b629-3177-80ed-2657f6dee9fa | 3.14292 | -61.00532 | 2025-09-24 04:49:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12408ad5-495d-3f7a-8f41-0bb88fce00f0 | -2.42953 | -47.1596 | 2025-09-24 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3978a115-1063-31c7-9e28-65b29ca086e2 | -4.01369 | -43.27107 | 2025-09-24 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d3c418c-4075-3049-9816-88e4d822d65f | -3.51897 | -49.44426 | 2025-09-24 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04d37d73-c9b1-350f-be17-e345f3bf5fcc | -2.96629 | -49.57369 | 2025-09-24 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5114a39-360b-3095-8b16-f79e979f15f4 | -3.79957 | -47.58373 | 2025-09-24 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0109d28e-186e-395b-b9e0-65909a2200ae | -2.91306 | -40.39157 | 2025-09-24 04:49:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 86aac369-d1ea-3754-a152-02ef77317bfd | -3.39519 | -47.49451 | 2025-09-24 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8af5f5db-6cb6-338d-b0ac-b56b84968004 | -4.79729 | -43.53681 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 09dcca93-96a6-348b-accf-79bb9884619f | -2.1553 | -53.66396 | 2025-09-24 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90c15a5a-6113-3bec-b1cf-ee7da15e319e | -4.78686 | -43.53522 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6eb30902-a945-3750-89a5-971662545645 | -3.63055 | -51.78398 | 2025-09-24 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd4af390-71f8-372d-9810-0c2b89e06844 | -3.27543 | -52.42378 | 2025-09-24 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a14a0475-65dd-3cc7-8cd5-8af8a33c3173 | -4.75224 | -43.62181 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6722f4db-df8d-3bf0-a888-2531c81a12d2 | -1.0571 | -47.89997 | 2025-09-24 04:49:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6475020a-0dd3-375d-8e8a-7d9612d7f3c7 | 0.68885 | -51.45974 | 2025-09-24 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64163186-c21b-3500-b66e-862805c67577 | -3.51837 | -49.44818 | 2025-09-24 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0325bd71-6aad-3045-99f0-2d1f40902295 | -1.01894 | -50.55122 | 2025-09-24 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fb833ea-1447-366f-81f7-f68d852a8ccc | -4.78586 | -43.53695 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e479387-1695-3602-973d-f329cda38b7c | -3.19202 | -48.80893 | 2025-09-24 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6f9ec34f-001f-3ee8-83aa-9f88be4ae685 | -4.79059 | -43.54099 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3973fc5-0a6b-3a5d-87ef-1c8c36715572 | -3.696 | -49.01918 | 2025-09-24 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 465a2669-25bb-3ff7-aa2c-189bc877d9a6 | 0.94381 | -51.19505 | 2025-09-24 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdc41806-3f21-35c1-a702-377a252d36b9 | -4.79796 | -42.75668 | 2025-09-24 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e7adc465-b40a-33d3-a279-0bcf7fb7d069 | 0.94052 | -51.19556 | 2025-09-24 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e617cf8c-2ef4-3654-97bb-955d5fa5c81f | -4.79877 | -42.75499 | 2025-09-24 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cca46802-2094-3d02-8da3-e1b52e9c443f | -3.41661 | -52.67158 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 728617ec-2747-33d2-af0e-14127d4f5382 | -3.18417 | -48.81199 | 2025-09-24 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e2d3bb28-c2f4-3fed-9c36-2bd8a7a30509 | -4.79106 | -43.53775 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5444f6aa-f2ab-3af0-80a1-1d5094e02b8a | -2.36617 | -48.54824 | 2025-09-24 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de1cb9db-a901-3ed5-98d7-d896ef560da3 | -4.63811 | -43.19085 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 022526ad-a9c3-307e-94c7-50016b219181 | -2.43011 | -47.15596 | 2025-09-24 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f357e124-bf3f-312c-b28f-4c25e0ddda8a | -3.18841 | -48.80838 | 2025-09-24 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0866a827-8c1c-3b22-aadb-e6f48ed36285 | -3.69663 | -49.01506 | 2025-09-24 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 763e102a-4bbc-33d8-88c4-55b59928c7f6 | -2.42619 | -47.15528 | 2025-09-24 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8dbb105-1545-31f3-8f0b-9b43699e41a3 | -2.18651 | -54.4637 | 2025-09-24 04:49:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbd9eb19-3fdf-38fa-a44e-9053e0399e3e | -4.16903 | -47.23051 | 2025-09-24 04:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 397452fa-7372-3ca8-a4cf-d6d18acfd389 | -0.84468 | -50.12088 | 2025-09-24 04:49:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71f4e21b-32f9-3d80-86fd-591255ab7712 | -4.6366 | -43.18968 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d58460b-52f3-339a-923a-148d7d1e74d9 | -3.3088 | -42.17268 | 2025-09-24 04:49:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 894df95b-ec0f-38d0-a87a-c4b08facd4f6 | -4.78633 | -43.53371 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f437dc8-9731-3238-95bb-0f8b6692a22d | -3.37924 | -52.71538 | 2025-09-24 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 726d4cdb-fff8-3399-bcea-98ae7c167729 | -2.4256 | -47.15896 | 2025-09-24 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dfe52e4-e4ba-3b31-8d66-2f5f441d3458 | -3.17642 | -52.4471 | 2025-09-24 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e43b69f-4860-389e-bca2-d94c85c72f0d | -4.79745 | -42.76015 | 2025-09-24 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8284a03f-907c-31a6-b4f2-9f02b04154b4 | -4.63859 | -43.18755 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 142f8dfe-2998-3eac-8869-79f8ad35c5c0 | -3.74511 | -47.19478 | 2025-09-24 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ecdb2c3-62ef-3b57-9809-4cc45a0d017c | -4.79162 | -43.53926 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2a72989-fe93-3f53-83ce-435cb89ae5d2 | -3.38309 | -52.71244 | 2025-09-24 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a3e1d35-901e-3a45-adf5-f90a5f3339c9 | -1.77072 | -55.50159 | 2025-09-24 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5356535b-addb-3d3a-bf27-9d578b05c2fb | -2.80096 | -52.47644 | 2025-09-24 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae16da3d-cada-32f7-9209-4147ed7eda98 | -3.05124 | -46.92673 | 2025-09-24 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71d899ab-5987-3806-bf47-729649f54c4f | -2.79591 | -48.67748 | 2025-09-24 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b1d2c9d-13b6-3f67-ba7e-6f71add9ff5e | -2.4303 | -47.15466 | 2025-09-24 04:49:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4619a4d6-e5e7-3d66-b052-0311a1780851 | -0.90655 | -47.5434 | 2025-09-24 04:49:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ccb196ff-81aa-3f03-be54-25ab8bdd9dca | -1.09118 | -54.11398 | 2025-09-24 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01086faf-8613-3b90-93bb-e75faabf3bb7 | -3.80273 | -47.58928 | 2025-09-24 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2bc15d8-07ab-37fe-b906-1477e27185cc | -4.79628 | -43.5385 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| eb518f41-2dd8-3b43-950f-0e721fd6423a | -4.79117 | -43.5425 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8d0b6b2-9ac5-3c4b-9186-26182bd1f3b9 | -3.05177 | -46.92322 | 2025-09-24 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f948a302-3f97-397d-bdb0-b3c81a3567c8 | -4.79581 | -43.54171 | 2025-09-24 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f93e3e06-1b8a-3807-909a-39ae5220a8dc | -3.05527 | -46.92732 | 2025-09-24 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83e8c941-e22a-3ffa-9e4c-f14eeca88123 | -2.79527 | -48.68164 | 2025-09-24 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ff86d2b-fcd3-3c25-a65e-07bc296f5494 | -5.49487 | -39.1657 | 2025-09-24 04:49:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 969a54fe-610c-3c96-b913-316950102abc | -3.96565 | -49.29401 | 2025-09-24 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c828a688-7f40-3ab3-9c3d-407314fe58a2 | -4.79828 | -42.75848 | 2025-09-24 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README13.md)
