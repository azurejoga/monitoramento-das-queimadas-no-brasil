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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b38cece0-0545-33a5-aa3e-fb38b5de0572 | -10.76608 | -56.24053 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc420f06-a7ea-36b6-8984-7c8c9ceda6d4 | -10.76586 | -56.3912 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 567af883-94f2-3a8a-aa7b-f6895e5c9142 | -10.76551 | -56.24411 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58178ce4-ae0e-319c-b24d-5d21567ae5a7 | -10.76367 | -56.38348 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f00cd258-59b5-3b35-b835-4120147fefb4 | -10.75216 | -56.24194 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2d41288-4d38-3209-834e-436e1d42d4d5 | -10.75159 | -56.24551 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d149e9bc-ed32-3da3-a13e-d26fd9141aad | -10.74128 | -56.39456 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afdcc7f9-0b7a-3467-83df-d742311aefaa | -10.73793 | -56.39402 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cda65f0-8c86-36e6-9f70-e7b996ea4d1a | -10.73735 | -56.39761 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6fdcc8e5-6825-396c-88fb-62d5d9f112b2 | -10.72397 | -56.39542 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e8fab9b-96af-3418-b081-923d3f7a6cb0 | -10.72339 | -56.39901 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1072e93f-0050-3b96-8c4b-0621c4059a3d | -10.71611 | -56.4015 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c57570e6-ddde-3b52-b402-7aa97730240a | -10.71218 | -56.40455 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e172ab13-6ffc-3d1a-a6c4-3b9f606410e2 | -10.70825 | -56.40761 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d1e532d-dd8f-39ac-af1e-63bbbf1be1bb | -10.58216 | -56.79041 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d416c2f-b4b5-3c9a-a0ae-777908e41dc2 | -10.57818 | -56.79352 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e66be28-9a2f-30ea-b3fb-294553a95fae | -10.5748 | -56.79296 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6830442d-47a4-313a-be0b-445b9df5595b | -10.49686 | -55.32268 | 2024-09-26 04:59:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33f3ba09-ce13-35f7-bf57-21d783e771ed | -10.48916 | -55.32859 | 2024-09-26 04:59:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 327758a4-5e52-3603-adf0-f301b5125e34 | -10.48861 | -55.33208 | 2024-09-26 04:59:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 043f9066-4ffd-386c-84e0-09230c034fd1 | -10.4721 | -55.32943 | 2024-09-26 04:59:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8bfc00f-7548-393e-abaa-0480d149d2e4 | -10.32751 | -56.75972 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdb3e395-02d2-3c0a-9213-8fd838102fe0 | -10.32412 | -56.75915 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3605094c-e806-3031-92e6-e23169bc7e15 | -10.32133 | -56.75493 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e24578f-7d39-348e-bd47-3429ba4328ae | -10.32074 | -56.75859 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66fe7ed5-e85f-3e62-8a44-a878cc4a7701 | -10.31734 | -56.75806 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe102808-13c1-3480-be37-13198b77b384 | -11.84796 | -56.87836 | 2024-09-26 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eaec8fb-6af8-35a3-9fd7-dce326c422d9 | -12.00908 | -56.49302 | 2024-09-26 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d178322-ea82-385a-95d8-d7b2d75f53cb | -12.00632 | -56.48887 | 2024-09-26 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09574913-9dae-3bbf-8f53-dfd757178ed9 | -12.00748 | -56.48172 | 2024-09-26 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aea1e92-9099-3659-857a-6bf93c14f02f | -12.00574 | -56.49246 | 2024-09-26 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c6a3218-7672-318e-81f3-6feeb43d11ff | -11.86878 | -56.66559 | 2024-09-26 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6c444f4-09c4-385d-bdba-97a32bb558ad | -11.49383 | -56.7788 | 2024-09-26 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dd42a4c-8b3c-33f3-bd66-52f8c84a87a1 | -11.49047 | -56.77824 | 2024-09-26 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 542c50d0-aa76-3d44-b4b2-f29354f17904 | -11.4871 | -56.77768 | 2024-09-26 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 581c5419-b3d3-3242-9432-e1ec5f18f6ce | -11.48652 | -56.78132 | 2024-09-26 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46fb3253-eb6e-368d-8d02-b46b5b71a6b5 | -11.48433 | -56.77349 | 2024-09-26 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 39633689-c6d8-3d4d-b867-d279e0115db0 | -10.97405 | -55.77025 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e6c4dab-a8f0-3772-994f-997f8a9a00a5 | -10.97075 | -55.76971 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b038d9d8-9279-3997-93af-7b1a53ea0c46 | -10.96358 | -55.77211 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65d78aa6-a642-3a96-a470-085d92a9f766 | -10.96302 | -55.77562 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| daeb0dc8-07c6-3404-b816-d376b7349d1f | -10.96082 | -55.76807 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72c17e40-eccc-304d-a44e-30096225ec4f | -10.95971 | -55.77507 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2bc7eb6-d091-391b-9f7d-b74f82b7a134 | -10.9194 | -55.79375 | 2024-09-26 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a61d4f6-370d-3452-beb4-93751e4f92d8 | -13.14307 | -56.40722 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b0599fa-1ce3-3536-9d08-0b3538a3d76c | -13.1425 | -56.41077 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7042b218-ff9d-3e2a-8c7e-e4b5bd414392 | -13.14032 | -56.40313 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4b27941-e38b-32c1-897c-83c07ba72dba | -13.12148 | -56.41459 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1642a16d-2cfb-3f7e-ad85-3808e7ab42c3 | -13.12091 | -56.41814 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e0cb5bf3-9aba-31aa-97de-4cef1e322fb6 | -13.11816 | -56.41404 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b975d82-0da8-3b30-a0b3-0466af1ac4e3 | -13.11759 | -56.4176 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84e71a7e-2cd7-3700-bbbd-3d2982141a78 | -13.11427 | -56.41706 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49704fc9-50e5-357f-8c87-3b21bc62bfea | -13.1051 | -56.36813 | 2024-09-26 04:59:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 999b0417-6066-3380-8827-e8efc2a1f8a6 | -13.10453 | -56.37169 | 2024-09-26 04:59:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6639ab24-67ac-3c8f-95a2-42f9709ca1f6 | -13.10065 | -56.37468 | 2024-09-26 04:59:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3a844da-8558-3361-b4ab-1ab4e4c84855 | -13.06549 | -57.26211 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59dced79-9f49-39ce-8595-d6d6013fc433 | -13.06388 | -57.26218 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a6de94a-696c-3024-9266-54c1cd1f3ccd | -13.03584 | -57.30686 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 700f8d3e-ae0f-3b99-b8bf-7d5ab2244c88 | -13.03366 | -57.29888 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 522720d4-ad97-3f79-93c4-6dac6edefeeb | -13.03246 | -57.3063 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e942da52-d933-37dc-b66d-15b67c70ef28 | -13.03185 | -57.31001 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6f2a81c-8e62-3b89-a94f-eab17de57943 | -13.03028 | -57.29832 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c4ce712-73cf-3ead-b616-504713deba12 | -13.02908 | -57.30573 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e8ef038-d452-37af-b051-6f9b6ef035f0 | -13.02847 | -57.30944 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15de69a0-ebd7-3cfb-8b56-e0601a2469f9 | -13.0269 | -57.29775 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d788cc42-2eb9-3d1c-831e-18d685e0eaed | -13.0263 | -57.30146 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31d486ef-da1d-3418-bb3c-8a7520541675 | -13.0257 | -57.30516 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd4156e5-6d63-35a1-9e92-2d4e44487d68 | -13.00428 | -55.97386 | 2024-09-26 04:59:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f7dd734-7b55-3f27-bc35-98d33130a9ac | -12.92733 | -57.26161 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b291ba6-1140-3a1d-a820-1edba9edf4bd | -12.81595 | -56.9572 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60157871-7b96-3011-8603-8efe1e0721fd | -12.81378 | -56.94936 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 929bc274-da81-36d3-934c-7c43502ffe9c | -12.81319 | -56.953 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c78f74-93b6-3f59-bfc6-463656b3d802 | -12.81102 | -56.94516 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecb8edab-58f4-3c6d-9f3b-efd430e90144 | -12.80984 | -56.95243 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a00b33b-233c-3108-aa23-3fccd5aaafdf | -12.62436 | -57.00727 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46e04c86-f0a7-3d4c-8717-25a33bda25f0 | -12.62178 | -56.98061 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f14f6104-a461-3de6-8d89-2ab1c60c35cf | -12.61783 | -56.98371 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d577c94-6fe2-3610-b9f6-f6fa9190e322 | -12.61646 | -57.01343 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca482abc-6ef2-3c74-95ee-c0bbdffcd071 | -12.61369 | -57.00922 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1127c2a-41ed-3843-82ff-9af9c9ebedb7 | -12.6131 | -57.01286 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 38d38563-d308-352b-be41-f4b8b50c46ba | -12.60479 | -57.00023 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9db7277e-cf81-3071-816f-544698ad7c78 | -14.62504 | -56.67669 | 2024-09-26 04:59:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c23ce47a-8bfa-3f2e-bfc3-728377619af2 | -14.62447 | -56.68026 | 2024-09-26 04:59:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2374b2b-6d70-32f0-b5b7-27079b931229 | -14.6239 | -56.68383 | 2024-09-26 04:59:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 116c755d-5622-30c3-8200-8c39b81e4d46 | -14.03142 | -56.3217 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6db13b0-1ed3-3594-8b65-2a8ce7229e5e | -14.03086 | -56.32525 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4383d2e8-2022-3aa9-bd80-ca2f77b5e92c | -14.02811 | -56.32115 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce1ea0a1-f7ac-3fc8-8574-8a3f24e80570 | -14.02755 | -56.3247 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ee8420d-5b89-38dc-b6a0-d5a013d24945 | -14.01714 | -56.30478 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0de9572e-4b03-3bd9-90be-dd02c1a4a052 | -14.01658 | -56.30833 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66d94a7b-1a6b-3a95-bf5b-abd766784e21 | -14.01497 | -56.29713 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16845dd0-7820-3c4a-9375-b40fd37a9446 | -14.0144 | -56.30068 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25d3b8ff-8194-3985-a9e1-3bcdb23d67f3 | -14.01384 | -56.30423 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e80b6bb-e510-3076-8627-528fa7d76e09 | -14.01327 | -56.30778 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0d88955-c550-3f6a-b9eb-b4f3f698e1e7 | -14.00997 | -56.30722 | 2024-09-26 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8032cd90-d4d6-35bb-844d-15443f327b1d | -14.00039 | -56.3675 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07f2cc05-ac22-361c-977f-4d320542a446 | -13.99982 | -56.37105 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 896fcb2a-804b-33d9-a50f-d84d7b7f0899 | -13.99821 | -56.35986 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cde7d43-0a9d-311e-ac22-bca2a6bcbd64 | -13.99764 | -56.36341 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 103e9fb5-fe62-3b2e-ab00-95b3b8eeccc0 | -13.99708 | -56.36695 | 2024-09-26 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README130.md)
