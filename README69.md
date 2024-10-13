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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8df9b3d-d45b-3e86-a923-f8a7cd2e9163 | -13.65704 | -44.2258 | 2024-10-13 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5baf5229-8c0b-30d7-a714-1b5d7e446dd2 | -13.65192 | -44.22985 | 2024-10-13 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 552253b8-a66b-35b6-848f-01775119f362 | -13.4641 | -43.66279 | 2024-10-13 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 456326b5-bae9-3275-bcfa-d43de88002cc | -13.46206 | -43.65976 | 2024-10-13 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 414b348e-7b3d-3f0e-8453-0d40fa014819 | -13.46143 | -43.66488 | 2024-10-13 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e83d7ecb-64dc-38b6-8016-d67d6a103758 | -13.45941 | -43.66214 | 2024-10-13 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 231b5a61-c6ef-3873-84e0-ab460ac37f2f | -14.19268 | -44.31317 | 2024-10-13 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 279f5b89-a1f5-3997-9bbc-c36013fd2d31 | -14.18816 | -44.31247 | 2024-10-13 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47b61d98-5d50-3e8d-9fec-7e9752616336 | -13.03085 | -48.64728 | 2024-10-13 04:42:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d40ec6ea-f5b5-39c2-88cc-318a413cbbe4 | -13.03028 | -48.65118 | 2024-10-13 04:42:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e37b574-01f0-399d-b051-b5ae01ecd459 | -13.02739 | -48.64673 | 2024-10-13 04:42:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c231914-0028-3641-9cc7-a4571ba71806 | -13.02682 | -48.65062 | 2024-10-13 04:42:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dad6ba6-a900-374c-bd36-9fab87e5e72d | -17.27062 | -42.65861 | 2024-10-13 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7a6b014-0c40-3c83-a6cc-a449d008c2fd | -17.26536 | -42.65777 | 2024-10-13 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6741e57-00b7-3046-811b-2692adeeb5b8 | -17.25971 | -42.66047 | 2024-10-13 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 018df27c-c8a3-3f0d-a227-13873eb2a1e6 | -16.68348 | -43.88683 | 2024-10-13 04:42:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c21e08d0-a6ac-3f62-bca1-2adf62137308 | -16.47047 | -46.15699 | 2024-10-13 04:42:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44bcc4b7-0fd5-395e-b337-acfe5e2558f5 | -13.78678 | -44.23283 | 2024-10-13 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8ebbd44-8cc6-3dc8-872f-b306eedaee42 | -13.78579 | -44.34567 | 2024-10-13 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25c593c9-828c-3002-9995-b88fdf23ca25 | -13.28797 | -41.90236 | 2024-10-13 04:42:00 | NOAA-21 | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74d0dcaa-e836-3b0e-9b23-6e0c1d155f67 | -13.28755 | -41.90588 | 2024-10-13 04:42:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7cda9492-5a5e-342f-a656-0f8d0ab89d9e | -12.83691 | -60.83524 | 2024-10-13 04:42:00 | NOAA-21 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8410c78e-c2d1-3658-a7f4-a042f3632364 | -12.83687 | -60.83504 | 2024-10-13 04:42:00 | NOAA-21 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4af46642-f751-36d3-b30a-50a1b95de5c7 | -12.83141 | -60.83385 | 2024-10-13 04:42:00 | NOAA-21 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb7ac42a-a567-3150-88f8-6125538427ee | -13.28285 | -41.90043 | 2024-10-13 04:42:00 | NOAA-21 | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8c5c4aea-c83f-3da6-93c0-6d4d1d187fb1 | -13.28231 | -41.90498 | 2024-10-13 04:42:00 | NOAA-21 | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7869ae50-1c81-3caf-a79a-1bc989b913b2 | -15.32092 | -41.89391 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7c7c2d2a-a27f-3923-b103-be32c1e8dcbb | -15.32053 | -41.89737 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fa66d836-f2a8-33fd-be2e-f312c2b5c7ce | -15.32014 | -41.90078 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e6936675-6ee1-3c58-9bfd-d9d34c59e912 | -15.31976 | -41.90421 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ea0fa178-8481-3516-8ec5-94ecbe474484 | -15.31936 | -41.90774 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d2ce92a6-d18b-3412-bafc-1cf49e73d8c7 | -15.31631 | -41.8861 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 06c8b7ef-6f5b-33b5-bfe4-d47540de9b00 | -15.31592 | -41.88956 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2fcd2453-388a-355f-8afb-b1ccaf5a3a38 | -15.31552 | -41.89304 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 921ca234-0b02-3966-b70c-00faea807d6d | -15.31513 | -41.89655 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e4839ffd-b8ef-33a5-a92a-31ee3fa4cad9 | -15.31473 | -41.90008 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 92cb24e8-fab6-3ade-8cbb-8762f33c771e | -15.31433 | -41.90366 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9dbc7867-68b0-3095-b512-7dd3bca8cdfa | -15.31392 | -41.90728 | 2024-10-13 04:42:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4eb6e991-c1ce-3b8b-ad55-d13a1ebf2f5f | -13.6527 | -43.09856 | 2024-10-13 04:42:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 72f0b336-f131-31c6-bd00-f8ca8427433f | -13.787 | -42.53991 | 2024-10-13 04:42:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fbbbace7-0092-315d-83c7-9f99cf6c5fd5 | -13.78662 | -42.54302 | 2024-10-13 04:42:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8340b3df-970d-32c0-a631-f1e51f65140f | -13.89748 | -44.27867 | 2024-10-13 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8ecaf7d-991f-37e9-be42-c5536ac546bc | -13.86213 | -44.40926 | 2024-10-13 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfef00a7-6455-31d5-b0bc-fe0c7e353d59 | -13.86153 | -44.41389 | 2024-10-13 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 240e6cca-5b6e-3f62-a36d-f546e160207f | -13.85766 | -44.40861 | 2024-10-13 04:42:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 927f9670-d207-302b-a78d-8f22c3e73db2 | -17.96711 | -44.93471 | 2024-10-13 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 748c76e0-f318-349a-8677-d35b2961de25 | -12.7 | -47.63435 | 2024-10-13 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8f3089e-1c0c-39fb-b1e4-d1f71d5336de | -12.69848 | -47.63594 | 2024-10-13 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b799cd45-dab4-3ce7-b9d9-d6474b35c386 | -12.54327 | -47.65253 | 2024-10-13 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b38ce1c-a840-3bd3-abbe-15c72683e699 | -12.51711 | -47.41906 | 2024-10-13 04:42:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10c80c20-e770-3490-9dd6-a38dc2ff8f25 | -12.55832 | -48.71547 | 2024-10-13 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4cdd6053-5fc5-356a-81c5-ea11ffa04408 | -12.18503 | -50.72263 | 2024-10-13 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 808c1287-6bc6-3b2e-a0f5-8f535524faab | -12.18393 | -50.70807 | 2024-10-13 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f84ef4e-51f9-3224-8168-cc50068fa596 | -12.18173 | -50.7221 | 2024-10-13 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dafeea4b-c545-34d5-b38e-f8c1f68ac472 | -12.18062 | -50.70753 | 2024-10-13 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7dab905d-57cb-32fb-b70b-fd471f759d5b | -12.17402 | -50.70647 | 2024-10-13 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f13bfff1-27ed-3323-9b9c-2fce2db5f688 | -12.12284 | -50.5754 | 2024-10-13 04:42:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1212450d-8a26-38b6-9f1b-52213b113f8d | -12.07885 | -50.68335 | 2024-10-13 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0339b219-e1d6-32ec-8dec-0ab251984564 | -12.02927 | -50.9126 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74474361-e3b4-37ef-85b8-f0372b72ec7d | -12.02597 | -50.91206 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5fd27c5-720d-34f4-b9fa-68f8b5563db2 | -12.02045 | -50.92556 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a536a8a7-e372-3c8f-878c-5b174231fdb1 | -12.0199 | -50.92907 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0171b098-0d18-31ad-b3f5-866477c18c34 | -12.01934 | -50.93258 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89b92f79-d126-392b-b5ae-c48427a09d23 | -12.01659 | -50.92853 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37bb07b4-b59f-3e2d-82f9-80c5cd549c61 | -12.01549 | -50.93554 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0d649c6-45d4-3ffe-b33c-6af0c88728a0 | -12.00888 | -50.93447 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff678c90-04b7-3fd2-bf5e-21c731053ee1 | -12.00558 | -50.93394 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0d30a14-ffbf-3a1c-b310-639eff297a8b | -13.25738 | -51.1071 | 2024-10-13 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85a4d247-819e-3af4-b3fc-96bc0c0fe7f8 | -13.25463 | -51.10304 | 2024-10-13 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01debbcc-cd66-333c-9736-bef798dde7a6 | -13.23703 | -51.0857 | 2024-10-13 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2ec22b6-2981-32d4-8eea-549e094adaf0 | -13.23428 | -51.08165 | 2024-10-13 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7417cd9f-28bc-3eb0-b6e7-a6c85c1bf5f7 | -13.23373 | -51.08517 | 2024-10-13 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d38083a-a9ec-3ac1-84d6-f37ebe08249c | -13.23043 | -51.08463 | 2024-10-13 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75b8605b-ff66-31d4-9e9a-0cef1b1db66f | -13.20797 | -49.825 | 2024-10-13 04:42:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 43394219-b3d6-3138-b4fb-964541cd64f2 | -13.20518 | -49.82085 | 2024-10-13 04:42:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3765359f-ef58-368c-9879-d770959b37a5 | -13.20462 | -49.82447 | 2024-10-13 04:42:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 18743f86-00f5-3831-bc2e-fb6d5afb0bf6 | -11.87224 | -52.39606 | 2024-10-13 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e8a8e3-a073-3182-a0dd-fce6b4dac613 | -19.25192 | -54.73884 | 2024-10-13 04:44:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7caa2145-9067-3532-b692-9b5cd7e5aab8 | -20.5063 | -54.7318 | 2024-10-13 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32c37c2c-2fc6-3584-882b-44db851b277b | -17.65737 | -56.25271 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4189b26c-57ef-345e-bad6-23ff58380567 | -17.73184 | -56.27202 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ec33a48a-94e7-3dc9-9de8-fdb66a7545c9 | -17.72808 | -56.27129 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4aae0c51-fd57-33a2-9634-945c91d72773 | -17.72431 | -56.27057 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 47b0905f-804d-3dfe-84c8-1f8717925645 | -17.68764 | -56.32323 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 32dfe9e5-bba9-316a-b488-747dc1659e25 | -17.68386 | -56.3225 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| be884f90-0cdc-37f6-8f65-2b159ac65164 | -17.683 | -56.32734 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 39c470a7-d995-3083-9034-de075ea08fb6 | -17.68008 | -56.32178 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e4f90239-2799-33f6-baa1-19b381cffcc7 | -17.65971 | -56.28294 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8475567a-0a1a-39aa-97a2-4a00869a07aa | -17.65884 | -56.28775 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 228fb755-8f55-32e3-bf12-d37840230f89 | -17.65797 | -56.29257 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f070a29f-bd00-3028-8c98-61b0d845cf56 | -17.6571 | -56.29738 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6fa224b4-c812-3316-b3bb-74e228f49d0d | -17.6568 | -56.2774 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1928e32b-05ed-3846-b218-52b356456b4e | -17.6565 | -56.2575 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1225a0dd-e349-307a-abc2-47813850b2dc | -17.65594 | -56.28222 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| baf3727a-eb0a-3620-bd7c-8e2102639ace | -17.65507 | -56.28702 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 04f117c6-186e-320e-a2f9-8b1b34083b93 | -17.6542 | -56.29184 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e9a42e84-831e-30f4-9cec-4971571d72bc | -17.6539 | -56.27188 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 73d6d867-81c5-3bf2-ba88-a13125d0a6d9 | -17.65333 | -56.29665 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d7db32a2-c7a5-35bf-875c-a8e4b3063860 | -17.65303 | -56.27668 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 1fe33b66-32e8-337b-8f0a-6520033cc582 | -17.65273 | -56.25677 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README70.md)
