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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0837227b-0032-374f-8f8f-aacfdb4a42cd | -8.53514 | -54.81986 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 919f19d2-fe11-3733-95fb-5c08048d8da8 | -6.77181 | -58.68989 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5296fb6d-7c5f-3241-971d-63e3d2557487 | -6.25537 | -55.39458 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 279ee2b9-5fd1-3932-9a4b-e675d011f512 | -8.52927 | -55.32336 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9c18a2e-cac6-3a40-a608-900d71513fd3 | -6.02846 | -57.68481 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 182cace0-771b-3161-8993-83b50be966c2 | -9.11877 | -61.58653 | 2026-08-22 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f675368-b9af-3e73-ae67-a908a27e79dd | -6.75249 | -58.67426 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8bbf1d1a-8009-337d-83a9-a68888e601f6 | -6.80273 | -59.01496 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 770617f7-9b34-3485-b62c-3afcb7877167 | -7.74094 | -46.16082 | 2026-08-22 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72b45880-de04-3341-8cc2-965d3012e9a3 | -6.8513 | -58.971 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55acf5ec-ba9d-3f2f-9c93-7616bea57ea7 | -8.59761 | -54.71401 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f7b33ac-6ff2-3dc4-906d-661c33b99a47 | -9.16125 | -59.46605 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e855a123-bae2-3e81-864d-a991c74104f5 | -6.13459 | -59.89913 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4cbb2cc-bb54-30ea-913b-caaa237d4f0c | -6.43345 | -54.9519 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fb52e58-d5cf-35a1-bd77-70ee28aab053 | -18.79191 | -43.7757 | 2026-08-22 05:06:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7189336b-5fd7-3cc0-b63b-0a0430e28656 | -15.51947 | -45.86347 | 2026-08-22 05:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40fd22b7-df06-3b01-a7f4-77b1c6e99c56 | -17.97393 | -44.35653 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2975342d-5d6c-351c-9de3-5a920d45542d | -13.93307 | -58.25982 | 2026-08-22 05:06:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51a17887-d6ba-3def-8d9f-c0705da5ad7c | -16.48893 | -47.94344 | 2026-08-22 05:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a8a0d6ed-0ad0-3d36-8a77-c504fbbc8844 | -12.95065 | -56.62748 | 2026-08-22 05:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4cfc66e-ced1-3baf-95ca-3e6716458169 | -15.33794 | -52.92592 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da1bd3a9-f517-3a06-b0ca-12789494a5c1 | -17.9597 | -42.73033 | 2026-08-22 05:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bc7792a5-4363-34bd-9dd4-c7b6a11ec4f8 | -12.93671 | -56.625 | 2026-08-22 05:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2044a16-dcab-332e-a48a-7bc8551baa0c | -17.97193 | -44.37572 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 917f9aa8-4108-3efa-8357-5bfbadb10f6b | -17.32971 | -53.23399 | 2026-08-22 05:06:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e6f4751-1b8e-3667-af5f-af6811517dda | -13.82635 | -53.99852 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 976abedd-d237-31b6-aa0b-038b890bb2c9 | -17.69388 | -44.4481 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46b530f1-09d9-39ff-ad90-22f5e98c0667 | -18.09101 | -46.94306 | 2026-08-22 05:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cf9af4c7-2993-3814-acaf-c32b9e14fa2a | -14.5637 | -53.04746 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02cc040d-ec11-31b1-bcfb-7ad7ae29a09b | -14.97407 | -52.65929 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b34e3b0-cefe-34e5-9b52-14ad7367cf67 | -17.91544 | -44.39998 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 077f68ea-882a-355b-897a-73898bc686c3 | -17.95928 | -42.73489 | 2026-08-22 05:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a62d3c23-6950-3b28-bc29-92ad1767b2e2 | -14.43226 | -52.9235 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42151d9c-832f-3d59-8cdf-59b670e80b7c | -14.11757 | -58.83398 | 2026-08-22 05:06:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbf92730-351d-3857-a63a-6873549848d7 | -12.9402 | -56.62561 | 2026-08-22 05:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d427f40-1e6a-36f7-8f3a-f4fc93bc14d7 | -13.38193 | -54.36679 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 006f2fac-aac4-35df-83b3-878c0dbc7e98 | -16.48835 | -47.94806 | 2026-08-22 05:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 83e03d52-94ae-30a6-94cb-c3638fbe5ed6 | -15.51986 | -45.86016 | 2026-08-22 05:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60e4bb09-9532-3527-af34-783915e944fb | -14.55974 | -53.05065 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21cd0a41-c9e7-3b07-a296-25712337f6a0 | -16.74017 | -49.34894 | 2026-08-22 05:06:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30aa61ef-06ba-353b-868a-65618189e3b8 | -16.70827 | -47.70446 | 2026-08-22 05:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7b0eca1-8a27-37d0-8656-2336d8101f39 | -16.31005 | -53.16096 | 2026-08-22 05:06:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c704ea21-3824-3ef9-bb4c-a9cd145b7dea | -18.08529 | -46.94839 | 2026-08-22 05:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30c19387-e721-34ac-be93-6496b66bb096 | -15.05079 | -48.69858 | 2026-08-22 05:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbd53f2b-a73c-3109-8b1f-7a7f9ab11647 | -15.2434 | -52.83757 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0becb32c-4005-37d3-b235-a027046e4e1d | -13.3919 | -54.36844 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7a9c2c0-30ea-34ad-876b-f21cc10aa04e | -14.33659 | -52.93518 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fcd0180-6ccb-3f04-9c1a-151442af5f7f | -14.55915 | -53.0085 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20bec667-c78e-38d1-83d4-7c7939ae0d2a | -13.38914 | -54.36435 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae46c0e0-e757-3d52-92e2-69200a12e7be | -17.91966 | -44.4174 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b3979d3-569b-337a-bb0e-a459e0a4ff79 | -14.13816 | -48.07064 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c04435ce-2d83-38f9-85c6-bcde18954cd1 | -16.50026 | -55.18513 | 2026-08-22 05:06:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f2868c3b-c301-3d32-ab15-ea2fb240e15a | -14.00642 | -53.68276 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edd1ebb8-9760-3fb3-bdc4-a0c273d3fb6d | -16.60495 | -50.79584 | 2026-08-22 05:06:00 | NPP-375D | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8dca9e31-2e8b-3036-a2f3-dfbbc0614193 | -17.97097 | -44.36077 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a10f8db5-addb-350b-a2b7-b3d6230bbff5 | -14.13923 | -48.06262 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fde293a4-747f-3ffe-af9d-49aaac706676 | -14.55807 | -53.08469 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18fc1ee5-51dd-34c3-92ee-0f9c67e1004b | -15.24627 | -52.84193 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3597e097-c306-34d6-ab1d-d8638913edfd | -17.96746 | -44.36098 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34acecca-db71-3e6f-b0ff-5a52a2d8717b | -13.99471 | -53.66981 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 003cb63b-0374-3674-b848-c0481b0591e8 | -15.00627 | -52.69546 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61f91d96-69e1-33ca-b18c-847c5927869c | -14.00977 | -53.70541 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb01c721-d326-3ddb-bd9a-a2e44c94cda4 | -13.92483 | -58.26304 | 2026-08-22 05:06:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1c9a7d6-71e2-3cfe-a062-c56d7b257abc | -14.28013 | -47.41943 | 2026-08-22 05:06:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a953c36c-7611-382a-9971-821e23c1fcaa | -14.39603 | -51.79825 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25cb30f7-a557-3b7f-86be-63fd4c5a165b | -14.97752 | -52.65984 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68c7b5f0-4ac2-3a8e-a9db-d78677238b9f | -14.01255 | -53.70954 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 29ed3729-6e84-3a66-b0df-2b76570af328 | -13.38526 | -54.36734 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b1f0db6-c2b7-33f2-a256-1c4b416fb8c8 | -15.17413 | -48.7436 | 2026-08-22 05:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b558c247-d877-35d9-b73f-6e8fd877e061 | -16.02828 | -52.17388 | 2026-08-22 05:06:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e02da84f-0bbf-3956-ac7e-c1a0b0f8ec36 | -13.8308 | -53.99192 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4180c20-6cba-3347-91f8-a3b82db32c5f | -17.92213 | -44.39315 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bfbf1245-06c4-3717-9bac-e9a8cde031b3 | -14.55235 | -53.00737 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d770afe0-0e1e-3c53-ad1a-e1d60f79d131 | -15.21753 | -52.77477 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 012b6b46-76da-3a23-aab2-afca7ba8de7a | -14.14314 | -48.06705 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35ec00b3-8b83-38f0-be2d-ef0c4a30b7b2 | -14.56139 | -52.99361 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91f0b442-e2c3-3aa6-b9c6-14dd347d9d7b | -13.98421 | -53.6795 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aa31a5c-2d81-3658-b1cc-0570f9dc7595 | -14.12927 | -48.06982 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a4276cd-0535-3c26-a55a-27d40bcd4120 | -17.97555 | -44.37542 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c2ce688-e982-35bf-a15d-a212d7ac80d9 | -14.55291 | -53.00364 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0153eb2-ced9-338c-a2c3-59895ceddf6d | -14.31629 | -53.00071 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf495c51-8d86-372b-9ffc-e9b3f9bd9d60 | -14.39544 | -51.80235 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2f7f2490-da8b-32bb-93cf-f2771c37f2cc | -17.97147 | -44.3556 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e55959b1-5aa7-37cc-bef8-52ffd486c3e9 | -15.86195 | -55.5543 | 2026-08-22 05:06:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfb443d2-c5fc-3bd9-be6f-f6789474a7ef | -14.01311 | -53.70595 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7d2fbef-fa6d-38b8-99c5-77adeb6e026f | -18.53283 | -48.25304 | 2026-08-22 05:06:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 145f70f0-53f2-3f72-894e-5162bb435bed | -14.55575 | -53.00793 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f962e12-75f0-3262-a2be-20fb8a464250 | -16.49969 | -55.18874 | 2026-08-22 05:06:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3ce3b367-6475-39bd-90e9-d453ed123584 | -15.20005 | -52.78053 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 916935b1-3309-3822-9015-fcefac6a549d | -17.97239 | -44.37125 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aedf1580-e16a-3709-906b-c6fae915cc5d | -17.91924 | -44.42159 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2d6203d-4953-3058-9119-ca3bafc03942 | -14.4215 | -51.79801 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1c6d4f4-91e7-3f03-8217-59e99aa80df7 | -16.2843 | -57.66949 | 2026-08-22 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8bebf78c-1172-3013-9263-f0d59c214652 | -14.39248 | -51.7977 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3fc25fe4-b32c-3640-9bde-a355dee73c8b | -15.17466 | -48.73953 | 2026-08-22 05:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee2eb5c1-b24c-37a4-8bc1-dcdeba1d4970 | -19.64714 | -46.03415 | 2026-08-22 05:06:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e38be395-7a8f-381e-8f68-fc4a630aefdf | -14.00474 | -53.67146 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ee8c9ded-b4e3-3a47-91ae-535c93c41518 | -13.82748 | -53.99137 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b6f5ca0-9ee6-31bb-aa98-ee99cbab0c2f | -15.00395 | -52.69532 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f89e49ec-ed01-3740-a7ea-cb0ec8f37e56 | -18.76072 | -43.79723 | 2026-08-22 05:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README54.md)
