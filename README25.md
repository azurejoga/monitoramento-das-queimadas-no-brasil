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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a5e9534-c763-318a-87bf-3353197c1621 | -9.73659 | -48.01961 | 2025-07-25 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 101f8133-bf6e-3914-a62f-2ca64a6add09 | -12.04671 | -45.43046 | 2025-07-25 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1191349-1648-3b4a-8efb-5a89f98edd1b | -9.85229 | -44.70323 | 2025-07-25 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5d9392a-3647-36ba-b455-2d1ff5576623 | -13.69814 | -45.68691 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78615b34-3972-3998-b0a8-91ae9b359b2a | -9.96476 | -64.95451 | 2025-07-25 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d06d7a2e-2654-342e-8aa5-ab0c96b078b7 | -14.74387 | -46.29965 | 2025-07-25 04:46:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c67cf861-c163-3714-b74b-992b2ee70a03 | -14.94449 | -46.97655 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c95c091-2a45-3122-88fb-0765d33cbeba | -10.74371 | -48.18578 | 2025-07-25 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 866883b9-9c53-38c4-9af4-2ffb887367e6 | -12.4588 | -44.65693 | 2025-07-25 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73193d7c-1936-3d9d-9ac1-a68e9bbf3512 | -9.74022 | -65.10748 | 2025-07-25 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbb91358-ce37-3fc8-bd65-9782a56e2647 | -10.42572 | -47.22369 | 2025-07-25 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cef5dc37-18c8-3e1d-8fd7-389ae9cffdbe | -13.4023 | -46.80259 | 2025-07-25 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c9c52ce-38ce-301f-8b45-f136552a14c9 | -12.42177 | -45.38424 | 2025-07-25 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7da661da-48de-33dd-9fa0-c5ea580a53e8 | -13.70865 | -45.67844 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fb11e6a-2292-32ad-8aa6-5cb50ac235c3 | -13.71333 | -45.67106 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 10a8ffd1-c536-3e10-ae71-a2abcc07e63c | -9.73175 | -48.02118 | 2025-07-25 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bf5ea93-4f46-311f-852a-737ff494b2e9 | -9.37384 | -48.01134 | 2025-07-25 04:46:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a55d4ccb-922c-387a-aa6a-893e2de086b9 | -13.70994 | -45.66867 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca8e547a-9b17-3cf0-a92d-591a211fadc3 | -12.69353 | -46.98497 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e44362da-c26f-3810-86e1-e02ec1b2bff5 | -9.59499 | -43.86945 | 2025-07-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 90f09628-e614-3534-9e7b-83210b975503 | -9.2603 | -50.042 | 2025-07-25 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 804fd0bc-9a76-34b8-aefd-6da780a07e33 | -8.88964 | -45.58034 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe2abbf6-b835-32a3-ae3d-6d46f83a3842 | -10.617 | -44.76471 | 2025-07-25 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce9d0462-b588-35d4-9179-d49d3e0ce605 | -8.89639 | -45.576 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 03e02649-bd1c-397e-ace9-07dbd9e15d2b | -14.95634 | -46.98675 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8335a09d-a64f-3daa-8353-1e7d9ee05dd2 | -9.02316 | -45.3367 | 2025-07-25 04:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b31dc67-734d-3a8f-b186-3e8fbfdc06e5 | -9.59251 | -46.33452 | 2025-07-25 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7c09dde-0cd1-3f71-8d8a-b2eb535b2230 | -13.71262 | -45.68395 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae1570b8-37f3-3198-af9f-2ad1786c5e3a | -8.8928 | -45.58909 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30072651-9378-32dd-a16a-773cafd740e1 | -10.00331 | -48.12107 | 2025-07-25 04:46:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acb38b2f-3d32-3f94-9247-b278cc6cf892 | -9.58888 | -46.33014 | 2025-07-25 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 941f591b-5429-3d50-ace9-df2480607c31 | -14.94149 | -46.98069 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2238ec8e-9887-3201-8a5a-84087ad489f1 | -9.02346 | -45.33863 | 2025-07-25 04:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65690824-072c-3b7b-bf46-0fd00662835e | -13.64369 | -45.70897 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff229fe0-b341-3ea1-a0c9-bd983d1c1bc1 | -13.21034 | -51.11775 | 2025-07-25 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a05289f1-5e8b-356b-ac5e-36941b07a5f5 | -9.65921 | -40.59725 | 2025-07-25 04:46:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 76985e51-5ad6-317d-bbc5-ebe325de0364 | -12.7293 | -46.30357 | 2025-07-25 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9987ca5a-aa30-3ca2-ba4c-e34b37938799 | -10.44939 | -49.05262 | 2025-07-25 04:46:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89308caa-4681-361d-b724-91f20a87a994 | -12.0513 | -45.43105 | 2025-07-25 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afcf991b-769f-34ec-a4c9-396a2887fa5a | -11.311 | -55.22416 | 2025-07-25 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1437a7c5-9080-3b3e-96f2-aa46f8d7dc1b | -8.89413 | -45.59249 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 151772a3-0597-3591-9c1a-6d2d1a997d90 | -13.71734 | -45.67654 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81330583-9976-3025-9071-8e3a8b9fd526 | -14.94575 | -46.98161 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 695a519c-beb6-3094-9bb5-505361260c7a | -9.0497 | -46.61922 | 2025-07-25 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef6040a0-e807-3d4d-84e6-21157bcbf24f | -13.64308 | -45.7138 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74ac266c-9c76-3177-babb-0966932a8482 | -11.74701 | -58.34503 | 2025-07-25 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93abcb5a-2a8c-33fc-bd15-91ef7e839ea4 | -11.46068 | -45.13094 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b04163fc-dbe4-35a2-8a9c-5c5f72f27638 | -12.34549 | -49.30448 | 2025-07-25 04:46:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0c478e0-88f9-3dfa-827e-41eaa220c8c0 | -12.46367 | -44.65754 | 2025-07-25 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a205fa6-4951-3e15-9c13-4c37205ee32e | -10.04407 | -59.09513 | 2025-07-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41a26851-ccd0-3510-b6b7-14fa1cafa755 | -9.42646 | -44.73413 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10ae720b-7041-3d02-92f0-57c46c096cb5 | -13.70749 | -45.68022 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97115e4b-9f97-30b3-a4be-98b3ed0416b7 | -9.13488 | -49.67123 | 2025-07-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68308fe9-ac8f-31ab-bda0-2a08525696ff | -9.65981 | -40.59259 | 2025-07-25 04:46:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bd826916-c6a3-31be-9f40-b48a01929baf | -12.25231 | -44.77822 | 2025-07-25 04:46:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2ca15cf-629d-390e-ab05-20932b124ae8 | -14.94872 | -46.97782 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32864b8b-f9f0-3607-a87b-764d2f1a02dc | -10.46414 | -52.7302 | 2025-07-25 04:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8c0b5f0-8079-38a8-9041-6c94907a9e2f | -12.42705 | -45.37996 | 2025-07-25 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47beef5f-657e-33fa-ab25-7b171a87d4e9 | -9.05322 | -46.6234 | 2025-07-25 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03862eb1-6a66-3571-a0d5-5cf5ecd1e9b7 | -11.31464 | -55.21893 | 2025-07-25 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26e2122b-f720-39f0-9a86-0d7dae5efb17 | -8.89459 | -45.57672 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| c68d9a79-3a0c-3bcc-9efd-c38f14f08f44 | -10.64118 | -44.76296 | 2025-07-25 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 039fc9f5-c724-39b8-a05c-75766bc6b3fc | -11.46197 | -45.12119 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 740dbe3b-0965-3ea8-8fee-19f0bded6bae | -15.59664 | -46.52402 | 2025-07-25 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a05612b-748b-3155-9b9c-052c43b0189f | -12.69715 | -46.98973 | 2025-07-25 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5e04062-b6c8-3b43-934b-c4e8d18d7150 | -11.31524 | -55.22065 | 2025-07-25 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efb9366c-929b-34cf-8392-cd17905c8e2c | -13.64246 | -45.71865 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52fecb7b-19f6-3299-825e-6e05ca07c024 | -13.7212 | -45.69004 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d54e5d7-faf5-3734-962b-4a147ab74ba5 | -11.94964 | -58.76326 | 2025-07-25 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0474313-9bda-31e4-8066-cee7dc0c0251 | -13.2109 | -51.11405 | 2025-07-25 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab20ae5b-ba1c-3451-a509-ee97495bb739 | -9.85695 | -44.70393 | 2025-07-25 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d679000b-03cb-3d02-8b3a-9521f809712a | -15.79609 | -41.96498 | 2025-07-25 04:46:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1f6ac82c-df13-3ed4-8153-f28217ab0527 | -9.07282 | -46.6333 | 2025-07-25 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d99e40a5-2647-39e5-a9b0-1c19332ec98f | -8.89356 | -45.59656 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 701e2b9c-b0cd-3639-a5b7-f03450c7a075 | -9.58998 | -46.32236 | 2025-07-25 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85a56c60-67da-3dab-8c49-48ee008f6900 | -8.12263 | -50.46801 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eaa2ca05-b8b2-3c6b-bb8f-68fa485fdf4a | -14.93924 | -46.98336 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bcf4859-2d48-357e-b515-e3d0d78422d3 | -13.09412 | -52.14317 | 2025-07-25 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ee95aa0-6681-31cd-b1be-4becffc61bea | -11.45265 | -45.12008 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 69abf76d-727f-3735-9087-40cd968f21c1 | -8.88922 | -45.59601 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 921a900c-3e7c-3548-8e4a-1d717a7709a3 | -10.50385 | -44.88312 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3dbdade-5143-3d34-9dc9-617b18a1fbdd | -11.77766 | -47.32328 | 2025-07-25 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 379c2e15-7754-3330-93a1-9b8a84576916 | -19.01818 | -54.65926 | 2025-07-25 04:49:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| daa74477-4754-3491-8899-a17105f8fd43 | -19.75437 | -53.99918 | 2025-07-25 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d16efad5-a8e1-33e7-94a7-319cabc6a0ac | -19.54103 | -46.76094 | 2025-07-25 04:49:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1249532d-dcb5-3f18-b240-9a436e132d73 | -17.34607 | -45.70536 | 2025-07-25 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 736777d4-6e10-32c4-9fb0-85ec11a11492 | -18.9734 | -54.38522 | 2025-07-25 04:49:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14e4bb61-c73d-3ed2-a5d9-9c449bf0c9cc | -18.97067 | -54.38099 | 2025-07-25 04:49:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e47d097-5bd3-3cc5-bf89-149c892f830c | -20.47656 | -53.67558 | 2025-07-25 04:49:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb6bfbe2-7192-3a47-af9e-be386577bca9 | -19.42813 | -44.81349 | 2025-07-25 04:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 250c7ba7-9fb0-3fdb-8671-8231343ec2d0 | -19.99906 | -45.39403 | 2025-07-25 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b28f17dc-1ac7-31f0-bf1f-423a56185829 | -19.42779 | -44.81672 | 2025-07-25 04:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f2acc47-d826-32d9-8b02-2e0eabde156b | -18.85105 | -41.98972 | 2025-07-25 04:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3df97851-1156-32d6-9e2b-5a53d20b5653 | -20.30165 | -55.46859 | 2025-07-25 04:49:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e409d1dd-98bc-32c5-ab91-8ac22a174b63 | -20.00419 | -45.39466 | 2025-07-25 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9592e34-ec23-3d56-99a1-5d6da19985e1 | -16.82146 | -47.59703 | 2025-07-25 04:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf89ce1d-2338-3589-ae48-802d75581737 | -20.47493 | -50.90799 | 2025-07-25 04:49:00 | NOAA-20 | APARECIDA D'OESTE | SÃO PAULO | Brasil | 3502606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 618b0e13-1296-38df-92cf-2b617f4aa5de | -20.68014 | -46.31091 | 2025-07-25 04:49:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1ae7a6c-6381-3c2c-a920-9a5c17793f30 | -19.28884 | -47.421 | 2025-07-25 04:49:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd2a8f4d-52a8-3c20-8d6a-5fa40f48c052 | -18.2237 | -54.54797 | 2025-07-25 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
