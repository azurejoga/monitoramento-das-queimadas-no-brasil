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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ea2b1b5-49ea-35a2-a97c-08e4049428f8 | -16.90021 | -40.89519 | 2026-10-08 04:49:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cc5cadfe-b1bc-352e-b1da-512e95c93775 | -10.61472 | -60.48788 | 2026-10-08 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 118ff2be-36ff-3f1e-8d03-30c0e85aeae3 | -15.68194 | -50.5674 | 2026-10-08 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73933804-6be5-3ae9-8305-75c9b9dc6764 | -12.22898 | -44.71774 | 2026-10-08 04:49:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ee225a5-b8b2-3daa-ba45-5b40ab1394b4 | -16.46954 | -52.70494 | 2026-10-08 04:49:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bbdcb50-6f56-3512-9b20-1b5e3acb3365 | -13.30224 | -48.67687 | 2026-10-08 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43aaf53f-b39a-3215-9058-97b4c31892f5 | -10.66543 | -58.92667 | 2026-10-08 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b006b0e-6ef4-3558-bfba-63e7112b23ea | -9.47806 | -64.35784 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2cd7931-6b1a-35b8-903e-c908c22e84d6 | -9.4868 | -64.34636 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37b91bb8-9026-30d8-b42b-efa984365940 | -15.24799 | -47.41313 | 2026-10-08 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02db0966-a6ec-3944-99e2-79dd5fb52bda | -15.56254 | -44.51686 | 2026-10-08 04:49:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ff5f8db-2ee5-3a76-9aa6-021d3a29a3cf | -11.75428 | -61.05597 | 2026-10-08 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3442a2f8-7a63-306f-a0c9-3a22914fa94b | -11.81116 | -47.34895 | 2026-10-08 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| feaa3920-4bc6-3d65-b13b-59600068722e | -13.1892 | -47.87262 | 2026-10-08 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55c09c6b-71c1-3e58-8bfd-0321ccd6c741 | -11.75875 | -61.05993 | 2026-10-08 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d8a21a38-c326-3d01-b62a-587fdc9c70ef | -14.93398 | -48.11049 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 780bcade-dd8d-3316-8bff-6cba52808d74 | -10.81392 | -56.4982 | 2026-10-08 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f6d581ca-6435-3da9-9ec4-68695909f326 | -15.10959 | -43.62849 | 2026-10-08 04:49:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 634a2286-4057-3273-b3d2-65515f8a3fe7 | -11.34431 | -51.8754 | 2026-10-08 04:49:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 26c7d13c-2a2d-340a-85b2-5e06bf491ec6 | -9.4727 | -64.35112 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d70d0b3-1697-39c9-a74c-6e548221be2d | -13.19791 | -47.86813 | 2026-10-08 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8caa6deb-84d3-38d6-b225-a3203b7b00e8 | -9.48575 | -64.35185 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 054cd466-ad1f-3f83-b1b9-bdef986f8237 | -13.18104 | -48.13581 | 2026-10-08 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2102a551-95d4-3769-bb8b-e7f1e3d9422a | -14.59183 | -47.97292 | 2026-10-08 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40a66b8d-8054-396b-a629-86abaefea696 | -11.77019 | -46.77367 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40761538-f086-3c1e-91f8-949f99143f2e | -13.69706 | -49.08481 | 2026-10-08 04:49:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b771ca65-ea54-3078-84e2-244fcae532fe | -14.938 | -48.11096 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a548b00d-e57b-313f-a48b-21337710feef | -9.49098 | -64.36034 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 755f7e5d-9419-397b-ab46-48d9f8c0d4ae | -11.02337 | -65.20872 | 2026-10-08 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41053ed1-9857-3f8e-b29b-c957ae56ea84 | -11.53371 | -49.93882 | 2026-10-08 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 767e2c38-6636-3a24-8e8e-7158f79099c4 | -9.07244 | -65.48412 | 2026-10-08 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd9a9814-2265-3fef-97fd-fe7b79fa7d0c | -13.16209 | -43.28541 | 2026-10-08 04:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 3daa6660-25d9-3548-99b7-1288a2dab50a | -14.96908 | -47.53759 | 2026-10-08 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e679ecb8-34ee-32c7-bf1c-f142ca3655b2 | -16.36119 | -55.33095 | 2026-10-08 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f862868-ef02-3d5b-8369-2f0c48bbe4cf | -13.80416 | -52.79136 | 2026-10-08 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2898a568-e9c1-36e6-a5e6-8399698eb7bf | -11.86503 | -48.03742 | 2026-10-08 04:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c2e888e2-5c60-3b68-a369-ae9325d33ca3 | -16.36057 | -55.33474 | 2026-10-08 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ec192cd-26d7-3b38-939f-7901da637abe | -16.83367 | -41.04038 | 2026-10-08 04:49:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c95d80f6-3b1b-30ee-8c99-579512a5f675 | -13.19318 | -47.8731 | 2026-10-08 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 06b5cf29-89c3-31c0-8582-ee757babe24a | -9.47696 | -64.36333 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 165d51e8-d4e0-3219-9202-70fbbbff9a7b | -16.01429 | -43.60352 | 2026-10-08 04:49:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0876a512-916e-358f-ab88-251111c5c626 | -15.62279 | -42.99145 | 2026-10-08 04:49:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 98023fc0-a9a1-3196-879e-915537fffd62 | -9.49115 | -64.3586 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca9ea853-f42b-30a4-9782-b26d5f42caae | -9.13777 | -65.30027 | 2026-10-08 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 303ad998-1c9a-35c0-b142-2c3507ff6c0f | -11.06896 | -50.6753 | 2026-10-08 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 224db26f-9b2c-3517-955a-b69bb378d8d7 | -16.8336 | -41.0424 | 2026-10-08 04:49:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 257a20ed-5cd6-3988-a3a3-5b0f491e4340 | -13.90975 | -43.99345 | 2026-10-08 04:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be9dfd83-83bf-3211-9b8e-4899ce2b36f7 | -16.90717 | -40.89178 | 2026-10-08 04:49:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| c0350bdb-0401-3f1c-bf1c-4812000751a9 | -10.62566 | -53.85646 | 2026-10-08 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 815ad670-2acd-3798-93c2-4912c5810535 | -13.17645 | -48.14011 | 2026-10-08 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b4e3b8d-cfa5-3602-a28d-37f78cbe174a | -10.36014 | -56.44349 | 2026-10-08 04:49:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ea450e1-56dc-39e1-9214-9decf75939e0 | -15.42052 | -43.70544 | 2026-10-08 04:49:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 96b2722f-fe00-3f70-a920-5403ad9621f3 | -16.12803 | -43.74865 | 2026-10-08 04:49:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da07ea4c-f53d-39f8-9968-e932c529d06c | -15.33908 | -42.77704 | 2026-10-08 04:49:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4073e185-a04f-3bea-8b81-b44426b90e8d | -10.28504 | -60.53862 | 2026-10-08 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c9782a27-6a3f-35d6-8b7e-4105e1500d7a | -11.74898 | -61.0633 | 2026-10-08 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 95ddd382-f70d-33d0-8682-657e091a89ba | -13.50226 | -44.37168 | 2026-10-08 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c890a564-5742-35e5-87c9-101682d144e1 | -14.90916 | -48.08263 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 45e97399-8fda-3492-80aa-e8e9ead416a5 | -12.19742 | -48.42317 | 2026-10-08 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00b8be07-297f-3c8c-a0ff-2c3aa36f832c | -11.78465 | -46.76992 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c27ee521-433e-3677-803e-d6d6b6e57d67 | -14.63396 | -54.25887 | 2026-10-08 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f68a8846-4868-30f0-9c78-7ccc88e0d249 | -11.34544 | -51.88995 | 2026-10-08 04:49:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aae04e7c-2aa0-33ad-85bc-b98e85fdd824 | -11.75515 | -61.05817 | 2026-10-08 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7667f236-533b-3d9d-9052-8ce87730c380 | -14.96853 | -47.54184 | 2026-10-08 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4804cdee-db3d-3fd0-a2a9-f7a8d339aa5e | -13.81021 | -52.79596 | 2026-10-08 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64f741ac-c15e-3424-8597-348f16f77799 | -11.76991 | -46.78476 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44266237-1e28-3eb3-aeff-2fdcb90c1b67 | -16.90062 | -40.89093 | 2026-10-08 04:49:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 29c4aecf-784a-3b19-954f-5b75bcc83d87 | -11.0222 | -65.21455 | 2026-10-08 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b671faaf-ed11-3b6e-a06a-52765621a1df | -10.62228 | -53.85592 | 2026-10-08 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88b0bd95-a3e6-3091-a3ff-dddcaebe44b6 | -14.58785 | -47.97205 | 2026-10-08 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01c68127-504f-335f-a4c9-5d9738c53aa5 | -11.90736 | -46.56194 | 2026-10-08 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d11a5e25-326f-3d2c-8605-e2775bd56b98 | -10.62506 | -53.86013 | 2026-10-08 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ebfb11b-a251-3509-afd0-1943dc7456fc | -11.77153 | -46.77239 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a06e1f10-d443-331e-93dd-6630f4bc8e5f | -11.78302 | -46.78225 | 2026-10-08 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b4f9fae8-4312-32e1-b07d-cc2fb7ef1208 | -14.35998 | -55.03594 | 2026-10-08 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 750fc848-b1d2-36d7-9b17-315b77bc0b76 | -10.36536 | -57.73878 | 2026-10-08 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a938357-92b4-359d-93bd-783c53c600ee | -17.18487 | -51.75465 | 2026-10-08 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 016872e8-f4e2-37b7-b2de-05e69e1401cb | -9.49221 | -64.35311 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d129f4f0-eae1-339a-97cd-d204ae5eb1fa | -12.41323 | -54.36327 | 2026-10-08 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3a0eb4f-4373-3023-a9f2-e8c281a468fb | -9.48562 | -64.35361 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3a50a1e-f599-3bb5-a3bf-087e25747418 | -11.06986 | -54.51431 | 2026-10-08 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 758389c2-ae0d-3d0d-a7bb-5702df678eef | -16.75745 | -53.37602 | 2026-10-08 04:49:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f57e2388-2fcf-3aa1-8dea-d31d509f3b7b | -9.48258 | -64.36833 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 66c8bb1d-1f4e-3fab-b43b-3171df1638a4 | -13.82806 | -56.44434 | 2026-10-08 04:49:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb0b8f18-3bf4-3bfb-80e9-90bf21b7610a | -16.55799 | -50.37913 | 2026-10-08 04:49:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38db73f0-0db0-3da1-b7fb-7b0ee4b91b12 | -13.15752 | -43.27773 | 2026-10-08 04:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 836e8687-5dbe-3565-98b6-9404a7596175 | -14.93536 | -48.11422 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a97e395a-147a-310d-8d89-88107018a822 | -15.68137 | -50.57149 | 2026-10-08 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43d607a5-6fc7-30d0-ac0e-3ebbad691a3b | -15.55497 | -42.97906 | 2026-10-08 04:49:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e272b86d-08a4-369e-b937-d1b1d99f9eea | -14.93135 | -48.09981 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be5263ac-aa4e-35d5-897c-defa482c6483 | -14.92091 | -48.11659 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aaf1b340-0b7d-303d-a4af-01ec63ee18a7 | -13.30537 | -48.68217 | 2026-10-08 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17831456-9017-3c76-8cc4-8adb0c87769c | -11.5307 | -47.59224 | 2026-10-08 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 34662db1-72e1-374f-b259-9ef56b7a4b42 | -10.64714 | -53.85241 | 2026-10-08 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f676434-c5b6-39ff-a36c-1b360a912d68 | -11.63255 | -49.83588 | 2026-10-08 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a11c7f6-46f1-3e2f-b50f-7d7446cafe9b | -9.47824 | -64.35606 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0688a7a4-53b2-304d-aae2-f807ed34af10 | -11.86571 | -48.03252 | 2026-10-08 04:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4070cd38-0657-3b86-a9fd-27da443d46d1 | -16.76019 | -53.38015 | 2026-10-08 04:49:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 05d17a3b-1b94-3aa0-b924-76c6eb7d70bd | -16.41155 | -51.86887 | 2026-10-08 04:49:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0174f175-9588-3e77-96fb-5b78065088f9 | -14.67344 | -51.46358 | 2026-10-08 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README122.md)
