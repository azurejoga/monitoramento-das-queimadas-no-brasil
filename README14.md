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
| 9b17cdec-639b-31e2-a50c-2f12d6f49dc1 | -3.00748 | -45.12777 | 2024-11-22 03:49:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b6a6752-7109-356e-ab76-650ef1abb3d6 | -3.65454 | -42.2627 | 2024-11-22 03:49:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 61c206a9-c9a6-3662-a47b-dd59f2ddf804 | -7.66741 | -44.50695 | 2024-11-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c10bc6dd-2c9b-3686-a88b-5212db0ecbd0 | -5.8163 | -44.74999 | 2024-11-22 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 598a3d18-662f-339e-8c2f-f023004e86d2 | -6.12212 | -42.5142 | 2024-11-22 03:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 685e7ee6-37fc-32d0-aefd-f693001c7d2d | -4.22947 | -40.38823 | 2024-11-22 03:49:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 962cb9c8-ebe5-3b29-975a-16ad9e5bdb38 | -8.39429 | -48.05698 | 2024-11-22 03:49:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45312ae0-8ba9-33e9-b91d-fc71eb70f307 | -6.91962 | -46.11245 | 2024-11-22 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef9709be-f89e-3ad5-a780-a956a49b5ccf | -8.7229 | -44.01934 | 2024-11-22 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ff835a1-80a4-3f56-9c7d-a0cea34fd61e | -8.72214 | -44.02382 | 2024-11-22 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ec39074-6edd-36e4-a3be-e6c66f62ca74 | -7.64517 | -35.07011 | 2024-11-22 03:49:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6cdead03-2059-311e-8434-912c4267fea9 | -5.94524 | -46.19238 | 2024-11-22 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5f614f3-5f31-3c73-9d22-2cf587c89222 | -6.11377 | -42.51291 | 2024-11-22 03:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d226b46c-da6a-3c1b-8871-a497f665aed5 | -6.11794 | -42.51354 | 2024-11-22 03:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ea826a6b-99ab-3002-a393-0c053d10ec63 | -2.44373 | -46.54429 | 2024-11-22 03:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 478cee86-9f02-3276-97de-7412fa4f6a9a | -5.5931 | -43.73935 | 2024-11-22 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1893f35d-287b-3e40-954d-7ffc3fa98bf4 | -3.46028 | -45.89798 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67ed2158-5516-3873-9637-60d779a157ad | -8.39354 | -48.06103 | 2024-11-22 03:49:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf4939ba-0977-3d0a-9886-06d8f6a7ff9b | -6.87137 | -38.87495 | 2024-11-22 03:49:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 85b17c66-d1bb-3992-91c6-4daedd32adbc | -8.87181 | -40.78057 | 2024-11-22 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1453d6dd-22c6-3c3f-a84f-2d1de544e070 | -5.24218 | -42.63833 | 2024-11-22 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3b499da8-19cd-3740-a7da-b45ded2f55fa | -4.70539 | -45.80899 | 2024-11-22 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 323ed423-1847-3495-925d-a52d3b23a721 | -7.714 | -45.6614 | 2024-11-22 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce45c885-8918-3621-a548-9f21451c939a | -3.83962 | -41.5596 | 2024-11-22 03:49:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f5c5a949-4d78-3bc4-9bdb-764108f63788 | -3.46884 | -45.91404 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d08e29ac-e5a8-38aa-8c76-fb841ef4f344 | -7.0061 | -45.6155 | 2024-11-22 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f06588cc-d316-3dd1-96b4-4161a22c6cd8 | -5.03722 | -39.85025 | 2024-11-22 03:49:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85da5fac-d3d0-3704-a4c3-c803b089fd3d | -4.09322 | -46.21125 | 2024-11-22 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a8833550-40fb-31a0-8265-987688bda024 | -3.46336 | -45.91309 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 91f331fb-fe4f-3ede-bffd-5c3bb02b1db7 | -2.30595 | -45.50789 | 2024-11-22 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b55caca-14b2-3cd6-a37f-d166cf8b898a | -7.78408 | -34.94131 | 2024-11-22 03:49:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 243c89d0-7182-3fbd-a193-289e8e63bab6 | -1.51555 | -47.065 | 2024-11-22 03:49:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9d07c31-1e40-3834-a567-5e43bf3b108c | -1.70826 | -46.69962 | 2024-11-22 03:49:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 291ada74-38ab-3657-9ac0-cd54d3cc410b | -4.70431 | -45.8154 | 2024-11-22 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 951eb147-7542-330c-a89c-cfda25205f1e | -3.00647 | -45.13494 | 2024-11-22 03:49:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5941cce-febb-3455-9f08-bd4ab4c46cfd | -6.71503 | -38.97152 | 2024-11-22 03:49:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c8d6332b-358f-3729-8277-b995db14e89b | -5.43166 | -45.34334 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35a89f61-e6ae-32e3-af10-b01ab2eb33bc | -4.62581 | -44.22915 | 2024-11-22 03:49:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18896b5a-952e-3c51-a498-2580f049188b | -4.25813 | -48.7025 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5cee869-1f78-3696-9209-da3d0ea40d1b | -5.24283 | -42.63433 | 2024-11-22 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f0c14370-a919-3efb-9a36-4fe97dcf769f | -3.46457 | -45.90596 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| ed2af931-889d-3ef3-af5a-373942c93873 | -3.00701 | -45.13174 | 2024-11-22 03:49:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebcb68f3-f17d-32fe-83e2-fb6613c501ca | -7.0066 | -45.61258 | 2024-11-22 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d377255-0aee-35bf-ae1b-b3d36b284107 | -3.75076 | -46.1251 | 2024-11-22 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 748afd4c-fd3b-3522-88fd-ad87688b8dd0 | -4.43048 | -46.59109 | 2024-11-22 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69d58a34-8923-35db-ba1b-0880dfc18732 | -3.88295 | -43.34573 | 2024-11-22 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| add39b2d-f707-3991-b260-c0ce6ed92035 | -3.49774 | -49.95943 | 2024-11-22 03:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe7ba7f0-1b51-3c70-8ce9-fb5ad2294e02 | -1.74344 | -46.30315 | 2024-11-22 03:49:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fba75d2-c328-339e-ac50-23a18d417c7c | -3.46517 | -45.9024 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| a48b4fbc-2fb8-3995-aef8-e5f0c0f93f6e | -4.00296 | -43.24837 | 2024-11-22 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 271da930-2105-3036-ab73-7ba185b40a7d | -5.19726 | -44.22384 | 2024-11-22 03:49:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fb297e5-225c-3b9c-bbc6-49a7f1b49b4a | -1.74288 | -46.31037 | 2024-11-22 03:49:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57b1fdfe-9b67-30a3-bb7b-fd6c8939d6ec | -7.14512 | -38.6562 | 2024-11-22 03:49:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05d79c3b-c519-3607-b1dc-98be63858e79 | -2.30651 | -45.5044 | 2024-11-22 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4614cc32-7e6d-3a44-a660-c2e00f047c31 | -5.10581 | -43.16456 | 2024-11-22 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 94d0bc98-6f5c-306c-a3c2-28efb93410f6 | -6.56178 | -41.35473 | 2024-11-22 03:49:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a48b749-159a-33a9-a081-c532bb467f02 | -2.70338 | -46.23214 | 2024-11-22 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6533ff4e-69a3-3a9f-b4a8-4cb1eb841ad3 | -6.19858 | -37.43596 | 2024-11-22 03:49:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d47b0bf2-4879-3415-a50f-927b64499e05 | -5.01018 | -41.96085 | 2024-11-22 03:49:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6ba1eb05-ae26-343f-8220-a64dd6c39daf | -5.81721 | -44.74468 | 2024-11-22 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7b811db6-1ccd-3ecd-86e4-c1f5b81f25fb | -2.98649 | -45.12438 | 2024-11-22 03:49:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98ce92cf-5363-35d2-9569-ad6b76cbcc7f | -4.25721 | -48.70793 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 304a7fb2-671c-360d-875e-1d8b302c38b4 | -6.82052 | -46.7751 | 2024-11-22 03:49:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d0254c0-dfa2-321f-ad8e-534a17f506d2 | -5.58779 | -45.21267 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef0c407e-00eb-31df-8bca-c0bf04484435 | -9.36005 | -35.49995 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| ac2dfdf7-5cd6-3b2a-8d77-c81aca6353bc | -8.7156 | -44.00879 | 2024-11-22 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d60ce50-a677-3a3e-9448-0cbccc47320b | -4.25209 | -48.70061 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57f0f1ce-f279-3eed-a290-d45e7a7e50e2 | -5.46072 | -43.23197 | 2024-11-22 03:49:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 930ae777-e029-3673-ba70-f52fde3824e2 | -4.01203 | -43.24982 | 2024-11-22 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10f2a1c5-5e68-3a7d-901c-d1f333121980 | -6.81986 | -46.77885 | 2024-11-22 03:49:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85c1a253-5b92-39d9-85b0-16eae3df816e | -6.34944 | -39.60643 | 2024-11-22 03:49:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 821a15aa-0b82-3ecf-bc5f-41706f3c6a15 | -4.25168 | -48.70129 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97772493-e2ac-39e7-ac37-3cee2340814c | -7.64115 | -35.07334 | 2024-11-22 03:49:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0ed067a7-217d-3020-9445-a5a0674ca997 | -7.66853 | -44.50989 | 2024-11-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c1b431c-4ee9-3964-ae75-b49ec6d17ff6 | -3.34376 | -42.78535 | 2024-11-22 03:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 509f0844-6fed-3e41-a3df-e75993be11c3 | -7.71348 | -45.66432 | 2024-11-22 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 966e81ba-fc6a-3059-ad5f-2fcc7b0033b1 | -3.45299 | -45.90775 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09aa894a-2659-3e17-ac33-598b7a783d24 | -2.98126 | -45.12348 | 2024-11-22 03:49:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 7abd4133-75b0-367e-bed9-e467de8e8a98 | -4.69936 | -46.07641 | 2024-11-22 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c31fa98-5c11-3c04-a802-80e8e0a1492f | -1.96247 | -48.38308 | 2024-11-22 03:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27b99801-f847-3685-9887-ef888a63b4a4 | -6.55951 | -41.35685 | 2024-11-22 03:49:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 590ef456-ce31-39a3-9a44-3899413f1907 | -3.06414 | -45.69177 | 2024-11-22 03:49:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0682547e-bd3d-33ab-b248-7316c9ddd432 | -2.44369 | -46.5434 | 2024-11-22 03:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0138b1cf-5f3e-393d-9162-dadfd42db10e | -4.10446 | -42.46099 | 2024-11-22 03:49:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b16c9349-8116-3800-9882-9a5d96d74abb | -7.45637 | -38.58006 | 2024-11-22 03:49:00 | NOAA-21 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2037ad5-7f26-369c-9aca-cbc28b88c806 | -8.92 | -35.58557 | 2024-11-22 03:49:00 | NOAA-21 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 654ef768-c08b-327f-8bc6-1d8e1a9380f7 | -3.47493 | -45.91137 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2dc8ce0-fe56-39f9-88fa-2335dbb4c56b | -2.30262 | -45.50398 | 2024-11-22 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9d8d980-abc0-31e3-8d23-4488e62f7546 | -2.65479 | -48.78545 | 2024-11-22 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 296f38ec-bbc7-3461-b365-c979814de14a | -4.70037 | -46.07869 | 2024-11-22 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac0bacfe-4076-32aa-a20a-28c1fd4e0cc9 | -5.00759 | -45.51869 | 2024-11-22 03:49:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b13dd377-3924-3c44-a0d2-10c57fb604bc | -4.70487 | -45.8121 | 2024-11-22 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9bc1d738-80c0-3d0a-836e-5e684a59197c | -4.73227 | -45.71429 | 2024-11-22 03:49:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3444613-7e3a-3259-9a41-506485885ca1 | -4.02189 | -43.98767 | 2024-11-22 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b289867a-81b4-30df-b805-48d931a63afd | -3.83844 | -41.56676 | 2024-11-22 03:49:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6a0ea9f-d018-39ca-a610-324952a79ae6 | -4.54007 | -42.98163 | 2024-11-22 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7be14313-f3f6-3c83-9658-32e2e8dbebce | -6.71161 | -38.97097 | 2024-11-22 03:49:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d88e7396-00c8-3d9d-a6ff-084b726e4d5e | -6.11858 | -42.50968 | 2024-11-22 03:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d63e29b6-5460-3d30-8e55-129fb4a75376 | -6.81437 | -46.77786 | 2024-11-22 03:49:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c8f6e5d-18e9-3604-a7e4-e21b881bedee | -4.25111 | -48.70614 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README15.md)
