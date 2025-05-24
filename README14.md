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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a0f7741-c30a-3e22-96e0-43226a8aff10 | -13.78159 | -54.30725 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80dbd303-0d2f-35c1-9877-fd4825ab8829 | -12.40234 | -49.98441 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3603218c-40dc-3863-aae0-66a65b19be31 | -13.98149 | -56.02208 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fd81154-3b34-3560-8ac4-0570a7757455 | -13.78835 | -54.30833 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27a575d6-4598-345e-a68c-c03335a778dc | -13.67503 | -53.93834 | 2025-05-24 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3273ca7-1bf2-383e-b759-72dd9340e34f | -14.67874 | -52.44221 | 2025-05-24 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 722a0beb-d70d-3d90-b120-100fd404995c | -11.99318 | -57.21236 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45238494-c541-322c-a383-f24835e4272a | -14.01648 | -55.13669 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e16d20b-7fac-3147-aa63-3fa05e76f25e | -11.99379 | -57.20866 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ea456f1-fda4-3036-8ba0-7520be4297f8 | -14.01593 | -55.14028 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc08d46f-1ee4-3546-9cd0-43336e9247e2 | -13.98534 | -56.01909 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9e74abb-545c-3e67-94b1-4d5ce0ec77ab | -13.36973 | -54.27006 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 25c09a9e-08f4-3094-bab8-3494a176f473 | -13.1514 | -56.81355 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f19ae518-8235-349e-9964-97b6504a10a5 | -13.19223 | -53.58089 | 2025-05-24 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| dff2b0b5-645d-3523-859f-eb9c31c15a2f | -14.06753 | -57.10726 | 2025-05-24 04:59:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99362d8b-b17c-3fbb-8809-cf41f55ab383 | -13.15806 | -56.81464 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 65d08996-58f5-3d3e-bf57-72fdd0ece0b4 | -12.14365 | -55.30753 | 2025-05-24 04:59:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d094760-96ea-3a01-96f7-089103fb9253 | -13.99195 | -56.02017 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7781dfb-52af-3e8b-a578-42173715c545 | -12.40431 | -49.98403 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9ad1283d-e7fd-3ad1-9f98-d1eb7e2f0b03 | -14.0198 | -55.13723 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a101980b-a866-3687-83f7-4c8fde26726a | -13.67161 | -53.93784 | 2025-05-24 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca365aa2-799d-35fc-ac7e-01c281189043 | -12.39818 | -49.98382 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97986cfe-f7c1-3693-8034-40629fbddf71 | -12.32544 | -49.98872 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da965ff9-033c-3e0d-aaaa-2ee5633df96d | -10.68034 | -57.60772 | 2025-05-24 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f691a143-cefd-3b76-9a9d-35219d16d8c7 | -11.35775 | -55.13462 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a86c19a-1d55-309e-86aa-27841b177cbd | -14.03364 | -55.13578 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76d4c341-72d8-388c-917f-528fa373128b | -12.38518 | -49.98578 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 763a57b0-3326-3014-af7b-b16f84b37bd5 | -12.40705 | -49.98107 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 26b6c7b2-5450-3c2e-8de2-795a935c6450 | -13.9892 | -56.01609 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 114da1a9-e4c3-3a47-a645-53d6ff0078e9 | -11.29632 | -53.98083 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a54d5140-dae6-305c-8188-5f051cca33bc | -12.90887 | -55.04399 | 2025-05-24 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f42444d-0aa2-3043-bffc-80939ae34d74 | -13.9859 | -56.01555 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0ae43e0-f89e-34ec-ae2a-c7ca9d5aa9ed | -13.15197 | -56.80996 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| afb40588-ef9b-3cff-a1a2-b77e6da40348 | -13.36409 | -54.26163 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c1a0b14b-8b97-3f75-aa95-74266596715f | -12.03678 | -54.96656 | 2025-05-24 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba08dba7-0ccf-3251-9a19-afebfef8acab | -12.14695 | -55.30806 | 2025-05-24 04:59:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c787e02a-2e60-3d04-9941-cb6b471d425a | -11.36159 | -55.13165 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e23a538b-d32a-31d9-9ec2-277f75237da8 | -12.38466 | -49.9896 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37027df5-0a0f-3c5d-a7a2-1afa1c579e1e | -11.99995 | -57.21347 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e705ee48-a061-3bcf-9f71-6785375ac131 | -13.83517 | -59.64853 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 375aefb7-5de2-3e93-b01e-224e3c921d52 | -13.36747 | -54.26217 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1583a240-c5a1-3152-a956-a7e963609761 | -13.78779 | -54.31205 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 675aa370-d5c1-3d74-971a-0bdfd50fca30 | -11.36322 | -55.12116 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e34f7fd-1d25-30dd-9de7-9f6c1ecc67db | -13.987 | -56.00849 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c93c679f-7926-3ecc-b47a-5d7dd9f146c0 | -11.08211 | -55.0687 | 2025-05-24 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4c7cda9-ba8c-3cdf-a234-2cdd182a0d61 | -12.39872 | -49.97995 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d183c48f-833e-37a0-b117-0143e1a9ad80 | -14.03751 | -55.13273 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b76aa41-257b-32a1-b4dd-54bdb3ddac15 | -12.37688 | -49.98449 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8c81e66-a454-329a-a537-64ddb3c842d1 | -11.29686 | -53.97721 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dc28b49-d623-3222-b100-e9afe0390ca1 | -10.68097 | -57.60386 | 2025-05-24 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4dfd99f-a0a2-3e0b-870b-8c1f9f6ce541 | -12.02478 | -57.10394 | 2025-05-24 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b0620e2-0949-3e53-ad3c-1c49485be85e | -13.46203 | -47.48467 | 2025-05-24 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 196aefca-2068-3870-9f2f-af0a9e365cab | -14.03254 | -55.14294 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a26e40a3-9e4e-381a-8b8f-61e68b5d09f9 | -13.18936 | -53.57647 | 2025-05-24 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a80f923-91e4-3306-8ede-204f403b0e91 | -13.19166 | -53.58475 | 2025-05-24 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 01f561e5-1043-3d0d-b0ae-e0e23855178e | -12.38156 | -49.98127 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70f1e3d9-798c-3335-a30a-5e8ea6934e94 | -12.19806 | -54.26892 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7643873e-dca0-3796-be94-9ae505c3c56c | -12.84108 | -47.39148 | 2025-05-24 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 209e5d7b-dc11-31b5-995a-1217ed2c274b | -12.38051 | -49.98896 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3e58555-6586-37fc-8dc7-6eee799a1918 | -14.02257 | -55.14135 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c369dee-03fa-379a-9da6-097e27d9b6eb | -11.752 | -54.22888 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aaa922ef-4d72-370d-a427-bea6c9575e32 | -12.37635 | -49.98833 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdf80920-9932-36ae-98dd-05ed9a9a8e71 | -13.85504 | -59.72438 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c332138a-936a-3cdc-8fc0-0e5f0f78b1fe | -13.36802 | -54.25848 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cd12f56-5ae1-352b-88e7-0e81bed66a98 | -15.58513 | -56.035 | 2025-05-24 04:59:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa199ad7-0a76-3df4-a339-ace51cedf293 | -13.85794 | -59.7296 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2db1ba0-2a50-3fa0-96b7-38911145ee3a | -12.67246 | -58.21562 | 2025-05-24 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de5f2b25-b171-361b-bf4e-96ee2e6d6b9b | -13.34096 | -48.0169 | 2025-05-24 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 140062bd-d3c8-3777-ba35-4d98abba20ff | -12.409 | -49.98067 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bea3ecf-000d-3f71-9f00-9063d91e5b14 | -13.18879 | -53.58033 | 2025-05-24 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0bd6a56a-c5d2-365c-868d-aaaa0b10771f | -12.37946 | -49.99658 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bacaf7bd-6c11-305c-9568-c1c5dcc24e01 | -12.40759 | -49.97719 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9ea33f24-ac93-3dcf-8805-ff157f5fbd50 | -14.01342 | -59.65967 | 2025-05-24 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6147d5db-74cf-3f4a-9984-3ee3b16c8d88 | -14.01758 | -55.12952 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e69d1c0-bcd9-32c2-9b48-2ed08206cc81 | -11.80329 | -57.36059 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6b07c3e-0583-302d-ab87-8af65ab5ee65 | -13.37084 | -54.26271 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 728e9ecb-b9b8-3a5f-b4a7-3ee0b53ffee0 | -12.39455 | -49.97936 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14248558-6897-3132-ba3d-981ad3d441ee | -13.15531 | -56.81051 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7584d1d2-95e1-3689-a016-8a828e404352 | -14.03086 | -55.13166 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e741f215-e91a-3cfb-98cd-123c9c1e93bc | -12.08912 | -57.37685 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fb3d731-2fd5-3bd7-8cc8-c1407cf06d6c | -12.66484 | -58.21836 | 2025-05-24 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1970b569-8262-33d9-8c8c-37ca7ba50ee8 | -11.67104 | -54.933 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 846e32d1-699c-39f7-a08a-2100bb5cacad | -12.354 | -49.93398 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 568cb894-6e40-39ee-a657-a6bad9f1f998 | -11.81071 | -57.35798 | 2025-05-24 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a7c2c6b-5a29-3fdb-9107-fd552a372138 | -12.35036 | -49.92944 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d07359a6-955a-378a-8974-77730a674e5d | -12.35923 | -49.92673 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77264dd3-d4c8-3b8f-a351-c4f017bcb6d6 | -17.15443 | -54.0032 | 2025-05-24 04:59:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f75ad69-ab01-3891-bfc8-77215fce19cc | -11.75924 | -54.22631 | 2025-05-24 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5d7a4417-56e5-3ed1-9849-6342dfd07dcc | -11.30135 | -54.70826 | 2025-05-24 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df25ed9a-09cb-3425-9bc9-78cbeb96c353 | -14.03641 | -55.1399 | 2025-05-24 04:59:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6672c1a8-95d1-3a5a-8ca9-be32f94b5a78 | -12.38103 | -49.98513 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b7ec157-8aa4-30df-ae85-6f91bfe8f7e3 | -13.47352 | -52.27906 | 2025-05-24 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b76d5f5-a5b4-33b6-8f3d-b6c264fd6c29 | -16.28178 | -58.67284 | 2025-05-24 04:59:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 10720c2b-f8d0-3db5-b0d9-4b5271b9f80e | -12.38571 | -49.98193 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20b93198-e8f5-3416-aaf1-290f2ae5e807 | -13.14922 | -56.80582 | 2025-05-24 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe20caa8-95d5-32f6-ae5f-f6895efd6656 | -12.83571 | -47.39376 | 2025-05-24 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22a903a0-e3dd-3da4-b623-597238ee2ba7 | -13.37366 | -54.26691 | 2025-05-24 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fa3c122-db4e-318d-8986-b8c6eeb99fce | -12.13826 | -54.65995 | 2025-05-24 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 21fa87b9-f135-3ba2-ad89-1ea4588478e3 | -12.07617 | -48.45866 | 2025-05-24 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19981c73-45f7-3a40-aeec-27237e3f9840 | -12.40015 | -49.98345 | 2025-05-24 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README15.md)
