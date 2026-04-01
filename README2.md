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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffa0fdf2-90d8-3a24-ab99-3fd390177580 | -15.24281 | -50.8317 | 2026-04-01 05:01:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91c9fbee-87cd-391c-9cb3-18375c6420dc | -15.23868 | -50.83115 | 2026-04-01 05:01:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a27362e-5efc-3fec-be67-50eef09d754d | -10.71171 | -56.04637 | 2026-04-01 05:01:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8d990d5-7300-3068-aedf-45702400066f | -16.42945 | -54.91504 | 2026-04-01 05:01:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05b51b79-f03f-3e94-b02e-babdc1740436 | -14.19461 | -57.42249 | 2026-04-01 05:01:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0da212a8-c9e0-3622-819f-c6fc6e7f11ed | -14.19797 | -57.4231 | 2026-04-01 05:01:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8de2e93-ca96-3717-af71-da49fe8b7fd9 | -10.70839 | -56.04583 | 2026-04-01 05:01:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dca51183-9c61-31ad-93d8-fd578a72e968 | -15.35056 | -60.22176 | 2026-04-01 05:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30564e34-52d7-3239-8db2-626039226abb | -17.90436 | -54.12489 | 2026-04-01 05:04:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4165c21f-eda5-3f85-a6b3-9ad1bfbac7c5 | -17.95737 | -53.67143 | 2026-04-01 05:04:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 655501cc-5524-3827-be33-4aac402216b3 | -20.14374 | -52.83601 | 2026-04-01 05:04:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50ab7eaa-332d-3e99-9e89-c1ffcf169e39 | -20.50758 | -54.56158 | 2026-04-01 05:04:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce9c724a-6d52-38d0-8573-aa10c0705832 | -23.58215 | -54.74998 | 2026-04-01 05:04:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 64db5a55-3042-3033-a9ae-a63121c2fa9f | -20.50664 | -54.56009 | 2026-04-01 05:04:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5d7f791-3d01-3283-91d4-a432d6bf7772 | -21.60866 | -56.62745 | 2026-04-01 05:04:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98808cc9-f261-3000-8d6a-01e4b810a5e7 | -19.98793 | -54.7395 | 2026-04-01 05:04:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e53d2614-514e-3e98-9e4d-a616db66bd20 | -23.5858 | -54.7506 | 2026-04-01 05:04:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 35e36904-0987-3366-a734-75ebba561085 | -20.04196 | -54.51177 | 2026-04-01 05:04:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4307fe94-a83a-3690-b8d5-812e831823dd | -20.09758 | -57.2282 | 2026-04-01 05:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75c1440f-4023-389d-96c8-9981f6b073aa | -20.81756 | -55.67143 | 2026-04-01 05:04:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d68390f-714f-30f1-ad44-abdd09479846 | -20.82038 | -48.28228 | 2026-04-01 05:04:00 | NOAA-20 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8b351a6-7d1c-3753-a234-7e0fcfb431f9 | -16.30793 | -58.46946 | 2026-04-01 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1ef7f883-4c80-3b0c-bb59-46799fc06706 | -21.6053 | -56.62687 | 2026-04-01 05:04:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11dadc48-de2a-3e4e-9ed4-fb7d13525049 | -17.47102 | -55.20096 | 2026-04-01 05:04:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 85805fe9-81e5-3b2a-917e-42ca87766cc7 | -28.55877 | -55.70414 | 2026-04-01 05:06:00 | NOAA-20 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 240134f7-fa84-3525-9557-8591bbc6fb5e | -15.35105 | -60.22019 | 2026-04-01 05:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 303f45a8-9b05-35d3-9c14-e375f2f61728 | -16.43107 | -54.91584 | 2026-04-01 05:53:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b47eacc-9133-3083-93a4-64b444370c57 | -16.43469 | -54.9126 | 2026-04-01 05:53:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bbbb6d4-92a9-32c5-8de5-055802fb4356 | -16.42749 | -54.91212 | 2026-04-01 05:53:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e64ad491-dcc6-3a8b-b129-d28baef3c227 | -16.43173 | -54.9088 | 2026-04-01 05:53:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f79bece-5a3a-3a37-b553-fb90715b08f8 | -21.6093 | -56.62887 | 2026-04-01 05:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79a5cd08-b3a0-324e-8538-df7043522912 | -12.07227 | -45.33247 | 2026-04-01 11:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 33d328d0-bd4f-3f7c-9ed4-a7ee3e42b589 | -12.06929 | -45.35043 | 2026-04-01 11:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e8175e3b-4413-3950-a8ef-5a679fe57ea1 | -18.36731 | -39.95177 | 2026-04-01 11:30:00 | TERRA_M-M | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4c15830d-c6d6-3b72-86f8-2fab3e7bd5de | -19.60394 | -40.068 | 2026-04-01 11:30:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |


