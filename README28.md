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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abe364e7-1164-308f-84c6-fed5ebc9a8db | -11.74209 | -44.94649 | 2025-08-16 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53fa2136-6988-3a52-a218-32d7d401344e | -7.24148 | -44.78759 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82516cd1-ee64-3985-b364-b80bf2f932ad | -12.54086 | -46.94954 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 740a2936-f4a1-3950-a74b-54b013949a0a | -13.42411 | -43.68034 | 2025-08-16 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5c3c9564-a393-3f55-899a-e59fabd2e566 | -12.60178 | -46.96044 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 64acc700-78b5-337c-8545-33483868a110 | -8.38071 | -47.00865 | 2025-08-16 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 54b1b417-7073-35e9-8201-a6763523a11c | -7.09618 | -44.41756 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 896deabc-b04d-3d20-81a0-50fea2561b62 | -12.5447 | -46.95005 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 52f96a1c-fce7-39a5-8f80-b3edef6dcdd8 | -8.99352 | -49.87358 | 2025-08-16 04:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4209b7f-f70e-3498-bd83-6ec309030187 | -7.3887 | -44.91336 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 456ff2b6-c4b5-3ce4-9574-0a49e4c1b6d4 | -12.60974 | -46.9369 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 6ab6deaf-3ff6-3659-9fa2-8184d236fe35 | -12.56926 | -46.94426 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b2a37cf-434b-30d1-b9a5-9a190dc6bdd1 | -12.56419 | -46.97339 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c47a0795-b3fe-390d-9d4b-6f639fca9752 | -6.11841 | -45.92299 | 2025-08-16 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bc1284d-9a24-3413-a6db-4ed8246791fa | -12.59533 | -46.92955 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0f599ae5-f6c6-3dab-abcc-be135dbd8d15 | -12.57306 | -46.94495 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c440b419-d1ef-3769-be5d-2def79a6ac10 | -12.6026 | -46.95569 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0538cd77-e69f-3971-b1d7-2f920fc568e7 | -12.54131 | -46.96936 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 70f8f6af-f876-3699-ae4b-df710c453175 | -13.49673 | -43.6118 | 2025-08-16 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| bab344a7-0649-3950-8f84-35576b817583 | -12.70015 | -45.09186 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ca79d0c-8c15-311d-b6e4-af3019a9cb6b | -9.7029 | -46.26844 | 2025-08-16 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6b8eb077-7315-3c21-bb74-565cd4b08d08 | -13.42077 | -43.67978 | 2025-08-16 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 76f5a2eb-60a8-3ef1-9df6-c0a125dec805 | -12.54002 | -46.95428 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1b3c49b5-66b9-3d59-9e89-dcc5a6e88e6f | -12.60434 | -45.23622 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd80fdf4-161b-3571-96e1-bddd424e8656 | -12.82598 | -46.01907 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c03fd704-d3ee-3fa1-bc81-af8e1d3304d0 | -8.80642 | -52.07114 | 2025-08-16 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 341bc8f2-3ccd-31e3-8ecf-d8da69bc8dfb | -12.61732 | -46.9384 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5b5675d9-0319-32b9-8dc3-23afd3711cda | -7.3908 | -44.90073 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7700c501-0a7f-3e2c-947c-853686588e7c | -6.54755 | -43.04818 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f48ecaa8-d2ab-3ea1-933f-8db95ae71d7c | -7.09652 | -44.43813 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3af8c92-c935-35ea-88d9-8467d0093675 | -9.85369 | -44.68188 | 2025-08-16 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ed54476-6e23-3b77-8a67-088d7a2e7b39 | -11.31171 | -42.13144 | 2025-08-16 04:10:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ec2b8ea-72c8-3b05-bc7a-dee26bf7ddd1 | -6.56427 | -43.05437 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3b06f1c-591a-3269-bca5-c2d25e034097 | -11.35231 | -55.43204 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4f20679-d949-3a2e-ae9d-2b8b3196b8eb | -12.55445 | -46.96163 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| bc083b3e-5c23-30f5-a721-ff967e9e279d | -13.6092 | -46.90951 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fe6432c0-5fa4-3d49-896a-7d212b69da07 | -12.60478 | -46.96585 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd1dba85-7dea-32df-8815-26a3b4910a7b | -7.37569 | -43.82685 | 2025-08-16 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f4d9519-b155-3489-b547-11b37cb76c31 | -8.29863 | -44.96609 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f9109713-91b8-39df-96c4-d546a6225fda | -12.6861 | -44.9618 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d32b33f3-17aa-3d01-90a5-2da435367af5 | -10.17839 | -49.51125 | 2025-08-16 04:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 643f8777-5284-3832-bf9d-dddf60be8939 | -12.59836 | -46.93469 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 13dd976f-c916-38d8-a2f3-e2533e0aced3 | -8.10885 | -42.35704 | 2025-08-16 04:10:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab008c62-8fdc-38fe-8a64-b332ee0d77a0 | -11.35065 | -55.40679 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ff03b1c-29ce-3988-b468-b3c543ed0906 | -12.5883 | -46.94759 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55508f27-cc6e-3b9e-ab90-761761be062b | -6.78339 | -44.35536 | 2025-08-16 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da521f64-c99a-35e5-b1d6-31d8d243c2e1 | -11.90691 | -43.43682 | 2025-08-16 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c655251-76d0-3fe0-ab7e-fa84c659ab9f | -12.79787 | -45.96655 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7c36c96-3780-3104-93be-a651aa375f16 | -12.61268 | -46.94265 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 155329fe-5aa3-32f6-b353-30bcfbaf282b | -7.26131 | -39.66839 | 2025-08-16 04:10:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6675dddc-b253-32d6-82ba-45145be42df6 | -11.3643 | -55.4411 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42856b8c-be66-3199-9709-f5af2b9bad30 | -11.35894 | -55.43349 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17acdc96-4815-351c-8cd1-d4014244b57f | -12.62319 | -47.87061 | 2025-08-16 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d9819b7-6900-3f77-97a0-854283e90c3e | -13.61937 | -46.91815 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79685175-f2bf-3bf3-b77d-e74b11291ca6 | -10.96224 | -49.57204 | 2025-08-16 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9f3f9ae4-5cd5-31d0-a419-e016bf68511c | -12.56122 | -46.9679 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 36a02e1e-116e-3f6f-8978-3a15738ecf8b | -8.18963 | -45.0169 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9997943-ced7-32a6-8f6f-2d1d41505df2 | -13.67219 | -45.89361 | 2025-08-16 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4a7fae1-718a-3882-a12d-dc524945bb5a | -6.54191 | -43.03978 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa133924-8df8-386b-b263-cf89fe50b5b9 | -12.6288 | -45.24046 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aac5cd6c-75fe-3b3c-a0c1-8ced6d8f58ee | -6.543 | -43.90936 | 2025-08-16 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4cf1c6c1-9969-3f3d-b7cd-01c9e94d99d5 | -7.42045 | -44.87978 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54b67553-0002-3b4f-994a-0d5bcc9b42e9 | -5.93436 | -53.6484 | 2025-08-16 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff0db485-90ea-378f-bae4-677d89176cdb | -10.96312 | -49.56716 | 2025-08-16 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 169061de-8411-382e-9803-c0fcf4bd1ab2 | -13.57029 | -46.9785 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ff9fe688-9968-3292-a57c-999f44ddf2a9 | -8.16229 | -45.02265 | 2025-08-16 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9756e10e-f939-329b-8db6-186d40b90626 | -7.39306 | -44.90971 | 2025-08-16 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8398b920-66ee-34f7-9081-41a7a52590b2 | -11.35498 | -55.4394 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6dc3ac9-154e-3305-b33d-7be3513a657f | -12.45678 | -46.99168 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d2eef86-84b9-3713-8c1e-f6258e9ecd60 | -7.44589 | -46.13201 | 2025-08-16 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c03b6732-e9b9-38f0-8b3b-a22924fa1605 | -6.62097 | -42.74768 | 2025-08-16 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8564b031-5ebe-321a-93dd-b7e911e51d91 | -12.83535 | -46.0295 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb4d390e-da92-370d-804e-4b3d85cdd12d | -11.35103 | -55.43821 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 169309d8-42be-3fba-b6d9-e00fa200e82e | -9.33777 | -45.9781 | 2025-08-16 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 947f21c6-6619-3b5e-aff2-6185e8c2bd06 | -13.56666 | -46.95469 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4263ff49-d68b-3085-b1fc-83e77cf8170c | -12.60155 | -46.91623 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 48d68416-1833-3070-8370-7a84df409b5f | -11.35441 | -55.40785 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b8fb7e1-e61c-3fa4-a0cc-203979aec044 | -13.61298 | -46.90991 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 169b625d-211b-3d14-aa73-1218ef6a7352 | -12.59125 | -46.95322 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa0511c3-b462-3086-9631-2e98bb92d587 | -12.83102 | -46.01132 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47c91c85-e598-3b57-98da-6d4054522e68 | -11.51405 | -47.24104 | 2025-08-16 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65663c80-d57e-37ad-932a-95e90d8d5f83 | -12.68265 | -44.96119 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e9db2f1-4ce4-31dc-a403-b6af11a2b9d2 | -6.5561 | -43.03834 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 693329ca-3714-3ac8-8cf8-8dd4d7c42a53 | -13.58248 | -46.97521 | 2025-08-16 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5a126fd-9854-323b-a632-4a71f7e2ebfa | -7.36466 | -43.8289 | 2025-08-16 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1912704a-cd34-3ce3-b4e0-ce972b8063f6 | -11.54987 | -47.26831 | 2025-08-16 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 29f8e6dd-348e-3362-8108-0bd8354c7eed | -6.56009 | -43.03523 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 95358905-363c-36be-a0d1-df1fa686c4b9 | -12.40485 | -47.78645 | 2025-08-16 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65448905-2613-3423-aea9-7b209540d6fa | -10.86294 | -48.4846 | 2025-08-16 04:10:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60db2df2-db63-3c1c-8fe1-6e73e633fad2 | -8.94742 | -45.81575 | 2025-08-16 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 290aaa81-7f96-3975-868f-651515494b1d | -11.35324 | -55.41365 | 2025-08-16 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d02997d1-61cf-3abc-91f3-a87ee3ca193e | -6.55105 | -43.02629 | 2025-08-16 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98732ea3-acba-3fa7-9a05-c5cca9cdf13f | -9.29963 | -40.49906 | 2025-08-16 04:10:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e96d6e02-a2e7-3eb3-920e-6b6be150049e | -9.85305 | -44.68582 | 2025-08-16 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27f53031-c066-3e3f-96c5-f1a120cf33f6 | -12.81876 | -45.99611 | 2025-08-16 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cb7e1a3-1fdb-317c-a721-ae1254f0859e | -11.74273 | -44.94264 | 2025-08-16 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 369b5348-46b4-31a4-b7d7-c9fbc64b54da | -6.90064 | -44.10778 | 2025-08-16 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90414f81-b556-3585-95b5-b0edc48578f9 | -7.08245 | -43.85161 | 2025-08-16 04:10:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f60f801-b5b4-3117-b32b-c4199ed733d9 | -12.24858 | -45.05037 | 2025-08-16 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a439f28-fb18-374b-bdc0-495cb69aa3c0 | -12.55656 | -46.97206 | 2025-08-16 04:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |


[Clique aqui para ver as próximas entradas](README29.md)
