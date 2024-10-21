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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d1b868b-2fe9-3017-8867-37d11a1a3587 | -4.4065 | -48.07243 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 044da417-1962-3804-8d35-cb731a29529d | -4.37026 | -48.4796 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8b2b2de-ebf1-32c9-9508-a0389e5fca3f | -4.36696 | -48.47909 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 843e5409-ea34-3fa9-b421-68ddfc010f8f | -4.36682 | -48.60987 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c9d6560-aeeb-32e3-bbab-b5e50ec71fb5 | -4.36365 | -48.47857 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85040099-c256-355d-9d41-3f3955efc24b | -4.36311 | -48.48202 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48cd0542-1aeb-36ad-833c-0c659e282416 | -4.3598 | -48.4815 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d7057f3-b7c9-373f-a927-8a483079b749 | -4.34044 | -48.62696 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db16c028-1160-3d74-a39a-59b4e7d5ab4e | -4.34018 | -48.71504 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e794a78-a5da-3841-bf75-5ac536013192 | -4.33964 | -48.71849 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d76f8e79-bebc-3dd9-81f5-7e003ffc7c35 | -4.33742 | -48.71108 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 067006a8-807d-394b-bff7-520c168b7613 | -4.3316 | -48.61853 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 02118d26-4d03-3d44-8f71-44a8874c4cb9 | -4.33106 | -48.62197 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1059645a-81d9-3898-892b-6c031d90e606 | -4.308 | -48.63955 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 462825c4-e166-3d41-b819-1fa4984bdd93 | -4.30746 | -48.64299 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c642cc3-4a3b-399a-b22c-cf79eaf92d1e | -4.29598 | -48.60645 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c43b1b0c-63cf-3d0e-ac60-ff5326740fd7 | -4.2165 | -48.55172 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27f1cef6-67c1-3952-861a-9854325fc174 | -4.21596 | -48.55518 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0076c6d-9cad-3e05-bc3d-c6956cf3fe1d | -4.2132 | -48.55121 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d6386ee-86d0-3175-8256-c373f05da1aa | -4.21266 | -48.55466 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8c6032e1-e5e1-33a8-9e3d-be0ec4f7c2ea | -4.19971 | -48.02659 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96bd04ab-03f4-3174-a4a9-a8f102bbbbc5 | -4.19091 | -48.58271 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28a8fae1-a9fc-31e3-98da-ccf7e8c70ab8 | -4.19036 | -48.58616 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0540bb3-6793-3ed7-98c9-ef0d7dabdda4 | -4.19034 | -48.043 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 736d1975-6d21-341d-8055-19388c29edbf | -4.18648 | -48.04594 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6153aea3-967d-30a4-aee0-e411bc8f6712 | -4.18369 | -48.04194 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b845f08-9148-3a83-92ad-9de51eb96fa9 | -4.17991 | -48.58807 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1c138e1-3db2-33fc-a313-0fd16662b00c | -4.17714 | -48.5841 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9e503e4-4746-3a85-b5ca-66f9caeebe1b | -4.1766 | -48.58755 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b32c72c-01df-3228-a4f0-2826510f3939 | -4.13262 | -48.2835 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 796eb81c-c9d3-368a-9e72-d6ba64729df6 | -4.13039 | -48.27605 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7fd3370-c7a5-3b8a-b2b2-2b7294d7695c | -4.12876 | -48.28646 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b94cd2a4-f341-3363-9b49-9232f98ee2a9 | -4.12816 | -48.2686 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b87b7d75-76d1-37c0-9fdd-8162141d30c4 | -4.12708 | -48.27553 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0203dd82-8a0e-3bf7-8e18-9fbcb3f339bd | -4.12653 | -48.279 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f96a5c78-dccc-35d2-9ba5-99b28308a01d | -4.12539 | -48.26462 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a58beca7-4bab-3eae-9927-f3b031e4609a | -4.12322 | -48.27848 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dc53e1b-6565-37d5-993d-fc5bfd75c3a6 | -4.10544 | -48.24023 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10e7e181-5345-318f-bf7b-38751e8a2e02 | -4.10489 | -48.24371 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 700e0425-f62c-355f-812d-9c6ad40693e8 | -4.1036 | -47.70896 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 479adcdf-1f28-3869-b2f6-59e0a5c13839 | -4.10212 | -48.23971 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f6b0f0d1-d973-3dfd-818d-4bbd92733fbe | -4.10158 | -48.24319 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c55ad3f1-eb9e-37c9-8f7a-dfe64378bde1 | -4.10103 | -48.24666 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf86b07f-52f6-34bb-a5ae-6520547912a0 | -4.09881 | -48.23919 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27a24e39-c0e8-34f2-a3b8-65aa0bda4dbd | -4.07011 | -48.24897 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9dc89d6-f645-3cb6-b401-ffe95f72064e | -4.89832 | -48.27437 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce18cfb2-eaa4-3bfa-8238-b84047eb8822 | -4.89777 | -48.27786 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8c38c63-d6c1-395d-98cd-b9e240e66a32 | -4.89723 | -48.28135 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 247263f1-c97c-33be-be81-ff50b89526bd | -4.89445 | -48.27734 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61e1cc5f-8650-39e1-ae07-a75d430e5d05 | -4.8939 | -48.28083 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ae307a7-ad5f-324b-a84f-df85411b19e3 | -4.8738 | -48.21338 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f07684b-f579-32ee-b9d6-15336101dec1 | -4.8736 | -48.65054 | 2024-10-21 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07672b51-3a3a-34b7-854b-a74ad36ce6ec | -4.87102 | -48.20938 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dcbfcdd-ba65-3463-b423-330225e2de0e | -4.87048 | -48.21286 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 479a9087-fbc3-3d9c-9d98-42a0c2794a4e | -4.7969 | -48.74838 | 2024-10-21 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8356a8a8-03ee-3bed-a2ba-902e2916473b | -4.62923 | -48.7363 | 2024-10-21 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1851cb2c-433a-328b-9954-cee44302697d | -4.5668 | -49.22002 | 2024-10-21 04:36:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 36394089-5ad3-37e6-89c4-f65b29256771 | -0.64652 | -49.56024 | 2024-10-21 04:36:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9013f03-651e-334c-8cec-a22367fc9bc0 | -1.48394 | -48.9652 | 2024-10-21 04:36:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4759312d-81ab-342a-9aa6-6c75ab3e0841 | -1.48062 | -48.96468 | 2024-10-21 04:36:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7b98d12-639b-3116-a577-9418639a0186 | -1.12529 | -49.19359 | 2024-10-21 04:36:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dc528bd-10c1-3274-b4b0-9949f36a0a1f | -1.12251 | -49.18958 | 2024-10-21 04:36:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43edc74a-8eb1-3028-b35e-5277421ebc2d | -1.11918 | -49.18907 | 2024-10-21 04:36:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af036bd0-4471-35c7-9ca4-e5582adf69f8 | -1.09033 | -49.17743 | 2024-10-21 04:36:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6265c7a-7a0e-302d-800f-cd1d975b9d26 | -1.07979 | -49.17936 | 2024-10-21 04:36:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a37d66ea-fe35-3805-b83e-22f7c05650e4 | -1.07924 | -49.18285 | 2024-10-21 04:36:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ed9c18f-9b6a-32bd-bd1f-d263c852083d | -1.07536 | -49.18583 | 2024-10-21 04:36:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f91d40b-90d9-3ea0-9d0b-18e4b652dab1 | -1.88899 | -50.02072 | 2024-10-21 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 404eddee-e0d8-32ef-a197-ea8063b4eccd | -2.19225 | -49.12902 | 2024-10-21 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fb933ad-a524-3c06-b3a5-33009ea53d38 | -2.18893 | -49.12851 | 2024-10-21 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27e6abdf-6f9d-33f8-b205-e5fb00eadc04 | -3.55198 | -50.30745 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37f49bd1-35d6-39b0-a8bf-cef2523dcb16 | -3.54918 | -50.30334 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad60f804-b385-385b-8cdc-8edf62577651 | -3.54861 | -50.30692 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1ac148e-4774-31b6-83b3-83b1e9e49c68 | -3.54466 | -50.30997 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 610e65b5-c1ed-3bf7-ac22-4e3859e78ae0 | -3.50212 | -50.53356 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c4c2691-6f88-3ea6-b289-05afc6011154 | -3.43185 | -49.97485 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77a8b312-56fa-3206-a4c9-a56a07e0fc21 | -3.4285 | -49.97433 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0c78213-3761-357c-bb4a-70fd181783e1 | -3.42794 | -49.97787 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a824fc17-0a7c-356c-abfa-bbc08e52e6ff | -3.38531 | -50.34452 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cf5b9e6-9174-3067-9c88-d18c5eb074b2 | -3.36666 | -50.30116 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4cfc5b2-df13-3623-9c24-6f1b16ff02ea | -3.36328 | -50.30062 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a94bf83a-d1cc-343f-b687-0dbb926e3549 | -3.35296 | -50.10438 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfd95930-f3dd-36c5-a31b-e1b9b3866cc1 | -3.30617 | -50.1041 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de659c8d-6454-30f0-b233-7d0717a98b4b | -3.30281 | -50.10357 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58a7f152-235b-32a2-940c-f567ab56d35d | -3.2696 | -50.22681 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38525e71-43cb-3b14-b78a-598a8eb1f02e | -3.26749 | -50.13092 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b37e4bf-dedd-3073-9a43-c25b3c159433 | -3.25056 | -50.1943 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce416fba-f41c-3b3e-8ff5-f207a19f9b7d | -3.2209 | -50.35958 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de1421bc-f398-3266-af67-5e9a61392750 | -3.21751 | -50.35904 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff34853c-b273-3e7d-b4f8-d6757e81a216 | -3.15433 | -50.37913 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72aa0834-3d6c-3802-b89f-fdd6d21c1fca | -3.09402 | -49.22843 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e753ee13-4478-3e64-8286-788773bbd312 | -3.07241 | -50.50085 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87640eeb-8989-3494-8045-9764b9127488 | -3.07183 | -50.50452 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dd83ba2-b0b7-3cab-a0a6-481cf08377ce | -3.06901 | -50.50032 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d6e51ad-b5c5-3d19-8f43-c06e7b5f782b | -3.06842 | -50.50398 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7adccc97-4167-334c-a480-b8de23c77bfe | -3.05254 | -50.38548 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91a6ca90-107c-3689-83d2-51b8f4a6e048 | -3.05154 | -50.38533 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 319bdaf5-6e70-3e91-a357-e310f3b2132e | -3.04815 | -50.3848 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51d2887b-9bb3-3129-ae47-de5c74e4f6a2 | -3.04758 | -50.38844 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7f1dfd1-b42d-36e4-a260-238e98985690 | -3.04418 | -50.3879 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
