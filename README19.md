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
| e6832a5b-7e4c-3e5e-af34-1b0636f14204 | -11.1634 | -46.923302 | 2024-10-05 01:08:47 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb16b98d-ff19-3ee9-9ec0-dc72ec26c26d | -11.1486 | -46.905998 | 2024-10-05 01:08:47 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ac17bdb-60b8-3e15-aea7-e73b0d0e3df0 | -11.1537 | -46.9259 | 2024-10-05 01:08:47 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d45fce9-7798-36db-ace4-cc5161657fc7 | -12.1295 | -50.8223 | 2024-10-05 01:08:47 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a68081cb-f49d-32de-9b58-c32e1a4d17cd | -12.1197 | -50.824699 | 2024-10-05 01:08:47 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa907d87-6ff0-3d10-9185-4283a2ed502c | -11.9243 | -50.108799 | 2024-10-05 01:08:47 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67780c68-4636-3267-b6fc-d356d94bb1d7 | -11.9272 | -50.120701 | 2024-10-05 01:08:47 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 964bd370-6e38-38d1-bc92-7d311376bf1d | -12.602 | -53.113098 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1f57fe8-d039-3be9-80d1-320d98ff8012 | -12.6039 | -53.121101 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c53a08a5-8840-3b2f-85ea-4c87d43a21b0 | -12.6058 | -53.129101 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a4d6d51-4030-3d44-9876-50491fceb1e5 | -12.6076 | -53.1371 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec24cd61-4340-38f7-8f94-77decf4b84c4 | -12.6095 | -53.1451 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e9f88e5-70b3-3d14-a12e-9fea6645248c | -12.5886 | -53.0994 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e690b18e-3435-37e9-99ab-0c9735b60c0a | -12.5905 | -53.107399 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b2615d5-c562-3bf9-9940-d0e5979012fb | -12.5942 | -53.123402 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7576527-8b9c-372b-b8d6-225c85e3c319 | -12.5961 | -53.131401 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8fab94-a3aa-3cd8-91b8-bc6c38529025 | -12.5807 | -53.109798 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b4fc339-e37d-3c4e-a465-e3c576313c18 | -12.5825 | -53.117802 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa235077-9563-3c81-9059-d34a404a17d7 | -12.5844 | -53.125801 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b6ce3fe-327e-33c0-88b7-6d674d34414b | -12.5863 | -53.133801 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 628e9299-1a9f-3e64-9ee4-3303ac84cc0c | -11.9175 | -50.1231 | 2024-10-05 01:08:48 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a32a692-b8ee-3462-8649-6ddec69eaaa0 | -11.9204 | -50.134998 | 2024-10-05 01:08:48 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 314b50e2-0df4-331f-a3f8-8a12a1a0bed5 | -12.6295 | -53.098 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13fce252-8a08-34b8-8ff7-f73ee8e57d9a | -12.6313 | -53.105999 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5682b7a4-b5b1-39b3-a1e7-75e9ee52041a | -12.6179 | -53.0923 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e65bd7e5-e561-3399-a443-e7db9a06bf68 | -12.6198 | -53.1003 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd8a64b7-d497-32c2-a7be-a1a993807ee3 | -12.6216 | -53.108299 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7540f213-c514-36f3-a124-68e520fae430 | -12.6235 | -53.116299 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef8bf1ef-d46d-3dbd-b0a3-c2c46f0e88cf | -12.6081 | -53.0947 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80b88877-a54c-3e4b-9c3c-2c5b5e1b3930 | -12.61 | -53.102699 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9a62d7e-8847-30ba-aecf-3bff80245d56 | -12.6118 | -53.110699 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 433ae166-4cd9-3ab0-8344-cfc969cfe147 | -12.6137 | -53.118698 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd6d26a0-1064-3f79-a595-77e7fab44bd8 | -12.5983 | -53.097099 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3348fec-af9a-3be0-8482-85bf3e1dcfeb | -12.6002 | -53.105099 | 2024-10-05 01:08:48 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67b432c3-d7c1-31b0-a129-5b68dbd3a19e | -12.569 | -53.104099 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60d9960f-5d6a-342f-b108-e69a33590ee9 | -12.5709 | -53.112099 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6795f927-43f2-3eaf-9bbf-82817ef32b2b | -12.5727 | -53.120098 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abfe1840-0c30-3dad-a977-64ab2ce42840 | -12.6178 | -53.4916 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dff72c97-28fd-3a8c-ba72-d1a1d952e44f | -12.6196 | -53.499401 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd10dfe7-cff2-3342-bbb8-c4b3aff513ad | -12.5182 | -53.107899 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1a3767e-0e72-396c-b319-ec246be1c572 | -12.5201 | -53.115898 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa92d8ce-f32e-3ac4-96a8-5fe852f68da3 | -12.6044 | -53.4785 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9021a15a-065e-3cc6-b902-35c3064d023f | -12.6062 | -53.486198 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2ac238c-13a8-3a42-90b9-4bf9ebe0ff74 | -12.608 | -53.493999 | 2024-10-05 01:08:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18453cc1-e372-3b0b-9fbe-21e0e810c1cd | -12.5928 | -53.473099 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8378a21c-c24b-3f9a-8053-c3fadc2770e2 | -12.5946 | -53.480801 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bbe8a42-8c41-31d0-8d34-bacc9956a63c | -10.8955 | -46.6446 | 2024-10-05 01:08:50 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e22aaa78-91ba-3006-9127-e4a6ee6977eb | -10.9009 | -46.6656 | 2024-10-05 01:08:50 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4cec120-fa55-309a-98d8-0cd9318bf045 | -10.8859 | -46.647202 | 2024-10-05 01:08:50 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a4b61ab-3941-354f-9b3c-040ec6b7fac0 | -10.8913 | -46.668201 | 2024-10-05 01:08:50 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3c5eddd-a284-34a2-8ab1-86a239f3cab9 | -12.4829 | -53.1334 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8897ce7f-f2df-3413-8468-b955b904f9c9 | -12.4978 | -53.1973 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 979562bd-c231-3595-ae99-faf1bcf58556 | -12.4996 | -53.2052 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4e6cef2-44d7-3163-bab0-8b8314d77061 | -12.4805 | -53.167702 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbd31912-5df0-3edb-97ed-a48a1832a9d6 | -12.5483 | -53.459099 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4a99b59-2708-3570-85e3-e3a72f1b1168 | -12.5501 | -53.4669 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cc6d3ee-c2f7-38f3-8e4e-09bbf104b0aa | -12.6949 | -54.0952 | 2024-10-05 01:08:50 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df485351-584d-30ff-bc4e-4af738e077b6 | -12.6966 | -54.102501 | 2024-10-05 01:08:50 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c048c38-708e-3c27-9fa9-e07059ff4451 | -12.469 | -53.162102 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfe41bc4-be60-3661-86dd-5fd42527c0d6 | -12.5385 | -53.461498 | 2024-10-05 01:08:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5aba5f5e-196f-353d-94dc-d6475dce69db | -12.6851 | -54.0975 | 2024-10-05 01:08:50 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25ff527f-2ad2-327d-ae14-ccceefdf91ec | -10.7416 | -46.170898 | 2024-10-05 01:08:50 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a78defa-85d1-3fd4-b51d-5953ddd79281 | -12.66 | -54.0331 | 2024-10-05 01:08:51 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bd6f12e-b0e6-3aed-bd48-20c652c81678 | -12.6617 | -54.040501 | 2024-10-05 01:08:51 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb2b0371-c474-36a7-8de7-984ea8ff2161 | -12.6502 | -54.0354 | 2024-10-05 01:08:51 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e13bbe69-9847-3c87-9d26-7e1e14b83106 | -12.6519 | -54.042801 | 2024-10-05 01:08:51 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1064ebf0-c3de-3f9c-854a-0ba4d6b26a4f | -12.6536 | -54.050201 | 2024-10-05 01:08:51 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6c180a7-23b5-3c32-aefc-ad2ecbd90d2e | -12.6587 | -54.072399 | 2024-10-05 01:08:51 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1f8392-5aea-3b1b-bbbd-2665036e184b | -12.6473 | -54.067299 | 2024-10-05 01:08:51 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c06b97cf-2146-3aca-a7f9-31fe268d914d | -12.649 | -54.074699 | 2024-10-05 01:08:51 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 541702fd-f6a0-33b1-8727-8305541d2777 | -12.6507 | -54.082199 | 2024-10-05 01:08:51 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1efd83db-3821-3e18-ad09-aa177b18b67e | -10.732 | -46.1735 | 2024-10-05 01:08:51 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f1f563e-6e99-34b5-b81b-71dd0a4d074e | -12.6887 | -54.6563 | 2024-10-05 01:08:52 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e9434f6-c1dd-3f9c-bca5-50d06dc962c3 | -12.6903 | -54.663399 | 2024-10-05 01:08:52 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37517db9-8007-3374-9a55-86755be2f955 | -12.465 | -54.172798 | 2024-10-05 01:08:54 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac3fe36-4cd8-3bb4-9ce2-975b2da676be | -10.7052 | -47.7103 | 2024-10-05 01:08:57 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf952c10-e844-345e-b552-170ebca07b0e | -10.7098 | -47.728298 | 2024-10-05 01:08:57 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 837008e5-99a7-3693-8d2e-2d9e29fd9df4 | -10.7624 | -47.9762 | 2024-10-05 01:08:58 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d6d9e0d-7358-3ee2-845e-35e681e190fa | -10.2237 | -47.681099 | 2024-10-05 01:09:05 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37177788-9561-3b99-bc21-cb51cdec56b0 | -10.2284 | -47.699501 | 2024-10-05 01:09:05 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69176fcb-d9f7-3f05-815b-c19e3180c7a5 | -10.2188 | -47.702 | 2024-10-05 01:09:05 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2556a264-998c-3fc4-bf74-926c9cfec6d9 | -10.2234 | -47.720299 | 2024-10-05 01:09:05 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c53dcb1-73a3-315a-8c96-34bce7cee63c | -13.4124 | -61.9305 | 2024-10-05 01:09:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 11481a1e-2483-36da-a7ba-1adad657302f | -13.4002 | -61.919701 | 2024-10-05 01:09:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a0264314-9516-38d7-99ac-5187de7e9c36 | -13.4027 | -61.932499 | 2024-10-05 01:09:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d513d647-4fa2-3876-8c63-b2df9981eb33 | -13.4053 | -61.945301 | 2024-10-05 01:09:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dab86a1c-d620-331e-b228-712e08033650 | -13.4078 | -61.958099 | 2024-10-05 01:09:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e8bb6f0-d2b6-33c6-a9ea-9e918a456fc3 | -13.3929 | -61.934399 | 2024-10-05 01:09:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c46f908-b094-37e0-9791-612dce46dd48 | -13.3955 | -61.947201 | 2024-10-05 01:09:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eceb0371-6284-382f-bf6d-d903d4973141 | -13.398 | -61.960098 | 2024-10-05 01:09:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be381f5b-b770-3bd5-bb72-42a572fd5446 | -13.3857 | -61.9492 | 2024-10-05 01:09:06 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 33159e86-4bc2-3e37-8a7a-e70ccf4b8cf0 | -11.3812 | -54.3503 | 2024-10-05 01:09:12 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22397f9c-ee88-30b7-a120-bc820e08e45f | -10.4311 | -50.7187 | 2024-10-05 01:09:14 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 177a8e08-da61-35c0-8d86-5d03fbe0c754 | -10.4296 | -50.755402 | 2024-10-05 01:09:14 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 538901bd-a15b-37f7-8450-fc40fc43a771 | -10.3023 | -50.528702 | 2024-10-05 01:09:15 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cdb1c707-6382-308e-9d79-145030d18371 | -10.3052 | -50.540501 | 2024-10-05 01:09:15 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c69da01-3ef8-39fd-b68f-ca449729d7af | -10.308 | -50.552299 | 2024-10-05 01:09:15 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4307715-c222-3ebf-aeb4-7b9dbebea8b0 | -10.2925 | -50.531101 | 2024-10-05 01:09:15 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6217be1-505f-34b9-bf17-22cc7c3a0c42 | -10.2954 | -50.5429 | 2024-10-05 01:09:15 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86a368da-b3db-3d92-9aa5-f7e8f8306dd1 | -12.927 | -62.4543 | 2024-10-05 01:09:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)
