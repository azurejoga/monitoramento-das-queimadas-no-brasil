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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 633d2f99-3ae0-3ae4-9fe9-2d86043658d3 | -3.45877 | -52.87064 | 2025-11-04 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97178ec4-c0de-3760-a53f-bc797128385b | -4.19425 | -45.68909 | 2025-11-04 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3496219-b402-3df7-bb51-17cfefe8b338 | -3.49008 | -50.3156 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bb59f5c-2764-371c-90ae-8d3e12dd7738 | -3.59111 | -49.44131 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96496d35-32c0-3df3-8aba-e726c1475a7c | -9.24267 | -47.54429 | 2025-11-04 04:31:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a143c2f5-0367-3e1c-ba91-edcb2b79c0c8 | -5.92329 | -41.31459 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e2cc00fd-7d23-3230-857a-d16ef029ce0b | -3.66195 | -50.61695 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd80936d-d205-391d-911b-1103768d7429 | -3.44488 | -50.22066 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a20bcf90-a132-36ce-82d2-72a52a9a0e91 | -4.57926 | -43.34227 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 25418d45-87aa-38f8-8ead-de4727395fa1 | -4.64832 | -48.32648 | 2025-11-04 04:31:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c10d897-e42b-3b34-b9be-a62dc2b9a598 | -3.60493 | -50.62329 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f8a0e4b-1330-30ab-be62-741dd62c5247 | -4.34553 | -50.79245 | 2025-11-04 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06c066a8-25e6-381f-a0c4-146d6964f203 | -3.49884 | -50.46757 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e53ba28f-1f86-3553-90f3-6092cc8b6743 | -3.01793 | -51.09129 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b9ab5b0-a0f1-3d09-ad17-127b0f219fe7 | -3.51828 | -50.32439 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbf263bc-d927-3c71-bf9a-68abc5c03fc3 | -3.23967 | -50.79723 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cc7186c-7ef4-3bc5-a7c7-e644184c2ec7 | -5.30195 | -44.80849 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc24271d-2331-3409-80fd-e8a4a69496e2 | -5.99522 | -42.9535 | 2025-11-04 04:31:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c93de755-3716-3500-a394-73086ea9be78 | -6.3279 | -46.32835 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c1b3a5c-6c08-3075-a5e0-585704d894be | -4.76908 | -49.53022 | 2025-11-04 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cce3f7a-e2f3-343e-a5fc-ea76e235fbdd | -6.4685 | -43.21987 | 2025-11-04 04:31:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f284010c-d92b-3472-8c90-9e391cdfb594 | -5.62347 | -41.09143 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e7997aa-ab40-3659-96db-d625d53910c7 | -2.62154 | -49.23043 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3aa5a120-0a03-3ad5-93b5-05cee4d1af97 | -3.66125 | -50.62125 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2d823c7-d3c3-32f1-a128-7b229771eee8 | -5.56931 | -42.29823 | 2025-11-04 04:31:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bff04e7b-2c7b-3476-8b6a-0202b7d21768 | -6.84762 | -46.30062 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8dfc16c-c06d-3085-9bce-49e28690f3b8 | -3.43863 | -50.23659 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 425053af-e44a-3948-b6db-fd55e29e7eb9 | -3.29427 | -51.62963 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a24c6acf-7287-37b4-a7b5-5214dcb0ca24 | -4.19303 | -45.785 | 2025-11-04 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f7ea5d49-7e97-3ca9-b531-022457f9adb6 | -3.92021 | -47.68831 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb6b5ccf-15f6-3632-833a-2e00d81e4a98 | -6.13202 | -41.54322 | 2025-11-04 04:31:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 94ee9765-0426-326b-84e8-3e36bc95d006 | -6.10254 | -41.74019 | 2025-11-04 04:31:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 92e97998-3c89-3122-974e-8d10bc2cc848 | -2.49136 | -48.15004 | 2025-11-04 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 592b8497-9660-3c09-8341-64a619e3fcf0 | -4.47286 | -43.22848 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0f681e86-fc6a-3b5f-9efa-0e3229baf38f | -3.03883 | -50.34515 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fe46758-6d21-38e2-9c8e-ab92f580c8a6 | -4.57931 | -43.33993 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5b821d6-2a88-3735-92f0-77107f39f35d | -4.18966 | -45.78448 | 2025-11-04 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fee17fa7-91e4-3618-bebf-81210eed36e3 | -5.2335 | -44.21209 | 2025-11-04 04:31:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f24904b8-b76f-36d2-9ab8-cb68a28013ef | -2.43207 | -48.19887 | 2025-11-04 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44dd33d9-8167-3ebd-883c-c97e53140c95 | -5.65546 | -44.06939 | 2025-11-04 04:31:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c6868d3-2e1c-33a1-a021-a8be2cbd3660 | -4.87316 | -47.54935 | 2025-11-04 04:31:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c67af03-517c-32a3-9b9b-eabf54e99c5c | -2.84414 | -45.5862 | 2025-11-04 04:31:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| facc3e48-935f-3f2e-9a49-afc0e09d6356 | -4.76848 | -49.53395 | 2025-11-04 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2e35181-ab3b-38eb-b1b5-0ac4f65738bf | -9.31545 | -43.10049 | 2025-11-04 04:31:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 34a40b63-722c-35ab-a60c-f42b6630cc10 | -3.49746 | -50.4761 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31f85e36-e267-3e71-aa9c-c460890e6308 | -3.92242 | -47.69574 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6237b954-fa34-3b84-b80f-86c9740ff65c | -6.7065 | -43.56589 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be512ff8-d971-35a1-8128-c2477c84e4e5 | -7.08108 | -38.83024 | 2025-11-04 04:31:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37005034-25b2-3877-9c20-19e036b953c1 | -5.83753 | -44.07491 | 2025-11-04 04:31:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9e557096-869a-301b-9e75-74fa262db385 | -6.14577 | -44.58293 | 2025-11-04 04:31:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea8af121-c307-3eb5-90b1-dacd4e714e33 | -6.42306 | -43.06755 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 42dd92ce-680e-3050-b6f6-25413b5ebb9e | -3.31817 | -53.84769 | 2025-11-04 04:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4910ce26-77a7-3521-b49a-4c912123f363 | -6.09869 | -41.7071 | 2025-11-04 04:31:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 66174044-0b91-3951-829c-425e1ac524cb | -4.74574 | -46.56654 | 2025-11-04 04:31:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82f12074-5df2-311b-9da9-d276bbff4a22 | -7.07336 | -46.73575 | 2025-11-04 04:31:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86b61061-adc2-3983-a925-4ea7efe93d96 | -6.60868 | -43.76173 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f4c118e-c1bb-3c3d-acd7-54105495b3f5 | -7.55253 | -45.85465 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fad4c602-2e26-3827-b8c3-aa26686e5a47 | -3.54609 | -49.43412 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c80a88b9-4537-3e01-847e-1702608b09b8 | -5.62792 | -41.0921 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 89234a16-8163-3520-bd55-3af34299769d | -2.29908 | -48.56809 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d814909c-7dd3-351a-8e92-a5533064cb81 | -5.87813 | -44.34927 | 2025-11-04 04:31:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78715beb-d263-3df2-82b4-6477b06eeb0d | -3.53434 | -54.8697 | 2025-11-04 04:31:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2c0324a-a149-3558-b930-ce4a99338f75 | -3.85132 | -51.40748 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22c55ebb-cd5f-3dd1-a5ea-8ce2ca77a11f | -3.50109 | -50.47672 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b65d303-e2f6-3cda-8adb-03b16581a04c | -3.7657 | -42.63918 | 2025-11-04 04:31:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d85b6fb2-f89e-3133-9ac4-8d613cff1c40 | -3.87481 | -51.96181 | 2025-11-04 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79b28ef3-6ad3-3902-95a4-cc9a69efd0d0 | -5.37024 | -44.74066 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49f8225d-2fec-3191-96f8-351d710fc92c | -2.79364 | -50.28697 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbb92a5a-9ebd-35d1-a05b-ef3d3678b728 | -6.41759 | -43.07712 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b310817-7771-3e44-b594-c3aa68af1412 | -3.49953 | -50.46329 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da57f61c-466b-31da-8371-c285f7af0edb | -4.42822 | -45.56078 | 2025-11-04 04:31:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73e1688f-863e-3825-b61a-b3bb5fa39c9c | -3.42702 | -49.17261 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3393d979-653b-3291-9772-87e3cb3eec8d | -5.5177 | -46.23706 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ed3566f-d94c-31ff-bb2f-b5e639a6d312 | -3.98531 | -47.08165 | 2025-11-04 04:31:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46ad9009-5720-33ba-b77f-6a0ef71dd9c2 | -7.5531 | -45.85086 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04949a52-478f-3bc7-b0f2-68d4bd5b9f74 | -4.55244 | -46.0235 | 2025-11-04 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f9c4005-6982-37e6-86b4-a989f87fd124 | -6.32453 | -46.32783 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 999ee8dd-edce-3909-a85a-eb0fcb432199 | -3.48236 | -51.58822 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 549bc6b9-fb46-363b-bf47-c3006ac22a8e | -3.48475 | -51.59243 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aa11770-62d3-359c-9495-894a3c791327 | -4.80637 | -46.72235 | 2025-11-04 04:31:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1f7dfa8-76a9-3322-af83-65297836224d | -3.15929 | -46.58882 | 2025-11-04 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 231e76ee-bf28-3390-9675-bb5659bf22fa | -8.51087 | -44.17791 | 2025-11-04 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad02f040-677c-3227-b6a5-41cb52e4baf6 | -7.85611 | -44.21405 | 2025-11-04 04:31:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fb277e4-d51a-3f38-8b59-5a4bed480988 | -3.91636 | -47.69125 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 71f7a636-1e0d-3990-8997-140387bf5345 | -5.75349 | -43.39891 | 2025-11-04 04:31:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33b9b04a-9668-3ff5-9929-3c9b96543130 | -7.55342 | -45.85509 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 074fb49b-63f4-3da3-b296-73b0db60b7c5 | -7.8568 | -44.20938 | 2025-11-04 04:31:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b50c5911-17a7-34b8-9497-e297e9b97457 | -4.62844 | -49.46598 | 2025-11-04 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 609c170b-78f6-3d38-8890-a7447b12e287 | -2.37475 | -47.7252 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 00f4bd04-5b76-3e76-a675-f936c3129d60 | -7.61195 | -46.47543 | 2025-11-04 04:31:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 705023c0-398f-3dc6-8045-e54b77581d33 | -5.67843 | -46.72935 | 2025-11-04 04:31:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e1afeec-3999-3dec-9aea-32c683a02c2d | -2.80644 | -48.66551 | 2025-11-04 04:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1073ebcd-7bba-3fbd-8aa8-c217f7d0c97d | -3.4503 | -51.0531 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40e4ce9d-8e76-361e-b0e0-95e20712c389 | -4.61091 | -45.75991 | 2025-11-04 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c927545-b129-3824-a284-1de226ca3116 | -5.75419 | -43.39415 | 2025-11-04 04:31:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99278182-737e-394a-8956-83d5ef845a35 | -3.18185 | -43.39543 | 2025-11-04 04:31:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adde6639-5bdf-3147-8938-fea74a9a1894 | -3.50247 | -50.46819 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c889c629-e1c0-3f82-a1dd-6c0c99fd74a1 | -4.91837 | -47.32722 | 2025-11-04 04:31:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40def7e3-903a-3e57-bc2b-5ba3560d1768 | -5.82733 | -47.61923 | 2025-11-04 04:31:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a02b72b5-ce2a-3800-b6e3-666f8541b1cd | -6.31508 | -43.81028 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README20.md)
