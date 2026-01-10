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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68e3092d-be52-33b7-a15c-c21af565a4f0 | -1.70198 | -45.80588 | 2026-01-10 06:09:00 | AQUA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| de80ce81-5853-3a53-b38d-3b648e6fc318 | -7.4943 | -45.576 | 2026-01-10 06:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 62723c07-7dd5-3798-9f5e-13b4966dc2c1 | -20.22721 | -46.48196 | 2026-01-10 06:12:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0a3a2205-8457-3ea2-8ce5-0cd9b92c929e | -21.04185 | -49.58422 | 2026-01-10 06:14:00 | AQUA_M-M | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2ad30293-f6d7-3457-a734-60271b406a8e | -22.82147 | -49.28562 | 2026-01-10 06:14:00 | AQUA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bdc4b9f-5e73-3144-83af-785d5b085a15 | -7.4943 | -45.576 | 2026-01-10 06:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5f533ebe-7be4-309c-9415-3a638eca6854 | -11.8385 | -48.6551 | 2026-01-10 06:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 18d23063-bfc3-3dff-b501-2987f94ddd7b | -7.4943 | -45.576 | 2026-01-10 06:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| a652e2d5-a561-36a2-af7f-a5ad272be750 | -7.4943 | -45.576 | 2026-01-10 06:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 60fe5086-1fad-38c8-a374-b01f5a18ccfd | -7.4943 | -45.576 | 2026-01-10 07:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 0a03c61e-4fd4-325b-9657-f04b12975e01 | -7.4943 | -45.576 | 2026-01-10 07:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 421d45a3-f18f-3e4e-9323-426ee431fbfb | -7.4943 | -45.576 | 2026-01-10 07:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 58aefee3-66b8-36c3-98cc-a061191eaa7a | -0.28173 | -48.78047 | 2026-01-10 12:31:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 98ba09c8-2614-3751-82d6-1e88d47aa23f | 0.13336 | -51.06603 | 2026-01-10 12:31:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 28221dbb-4cff-3bf7-9df1-f1d7e50b6444 | -0.28008 | -48.79225 | 2026-01-10 12:31:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0956a16f-5223-36ab-bda7-6cd8fabc02eb | -0.27181 | -48.78463 | 2026-01-10 12:31:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 80d0a13c-b4b0-3e25-8a81-21e6e4800266 | -2.79246 | -43.33815 | 2026-01-10 12:33:00 | TERRA_M-T | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 9ea15d6a-7988-3891-99ed-cf02f964deb0 | -2.52452 | -45.53704 | 2026-01-10 12:33:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ecc04fc8-639a-3cf5-b948-eee647511b10 | -11.82489 | -46.60968 | 2026-01-10 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1815aab5-8083-3bd2-a5f1-e6eb2590bc21 | -8.57442 | -44.73753 | 2026-01-10 12:36:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.3 |
| c9cfdee2-0057-3918-81cc-d8c97491c1a0 | -9.92645 | -47.83501 | 2026-01-10 12:36:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 498fa794-d2a1-311d-87dc-18b8da9a11f8 | -11.22775 | -52.83328 | 2026-01-10 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1d546bc7-e638-3643-9b9f-85c09e7d0768 | -11.82306 | -46.60372 | 2026-01-10 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 61594e79-c0ab-34ca-b150-ade1ffe034e2 | -9.60844 | -46.78562 | 2026-01-10 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3721a8fa-6f68-39a7-abf6-fe9be16566d1 | -11.52572 | -52.41341 | 2026-01-10 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5c6d35f7-3e53-389f-9042-0fb5ee882e29 | -9.92594 | -47.84152 | 2026-01-10 12:36:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 41ab5213-471f-3850-b1e4-fa9dda75cf0d | -11.15421 | -55.17071 | 2026-01-10 12:36:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3caf24e4-cea7-367b-b63d-d06dfff33195 | -12.71095 | -56.31734 | 2026-01-10 12:38:00 | TERRA_M-T | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cfbb84d6-8dea-3f92-98a9-a9640583481d | -11.63038 | -52.85429 | 2026-01-10 12:38:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fc7948d3-6703-3d22-9c8d-e3ea876add06 | -19.17785 | -48.69886 | 2026-01-10 12:38:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c1dd12e9-e43f-3ef6-83f5-0f3d3fe1fecf | -17.53102 | -53.34364 | 2026-01-10 12:38:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a8ea685f-3a8e-3e40-8f76-2a18b35f9ca2 | -12.38862 | -58.03996 | 2026-01-10 12:38:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 8f76c43b-61e7-3628-89cf-0ad99ca5e02e | -12.187 | -54.40062 | 2026-01-10 12:38:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 71775ef1-0542-3ef6-affc-f9671aae1ffd | -11.63957 | -52.85555 | 2026-01-10 12:38:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 960e7623-72dc-3f9c-887b-4aabf679ea7d | -12.27822 | -54.08795 | 2026-01-10 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3d7255d5-d71c-39a7-8984-1426724a075a | -12.38767 | -58.04511 | 2026-01-10 12:38:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 923e8e15-9e61-361f-b402-8bfda12264f5 | -12.75501 | -54.43395 | 2026-01-10 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7685b34d-eefc-3f1e-8e02-ac49b64bd0dc | -12.39861 | -58.04148 | 2026-01-10 12:38:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 2cd9b8fd-8764-3cb0-9c19-e6dc1d203a1b | -12.4086 | -58.04307 | 2026-01-10 12:38:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a4938e5f-e8b2-3334-a035-c2d5a4f1639e | -13.04805 | -53.72061 | 2026-01-10 12:38:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8f2642e0-8cd7-301e-8f5d-5cea161b4205 | -15.79928 | -48.14961 | 2026-01-10 12:38:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 94aa3aa8-a4b6-30e2-89a8-eca4b3cd2ae6 | -11.73979 | -54.24133 | 2026-01-10 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 22e91388-d29c-3ff1-aa4d-addbd57a33c3 | -15.32623 | -53.55166 | 2026-01-10 12:38:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eba08676-08a4-3e7c-8459-8baccc1136c5 | -12.96246 | -55.044 | 2026-01-10 12:38:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5efa6f89-a911-37f9-bc81-99cc510f6909 | -16.55435 | -49.18967 | 2026-01-10 12:38:00 | TERRA_M-T | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 173509e0-a1cc-3dc3-af3c-6f19ec25a87a | -19.12964 | -54.53057 | 2026-01-10 12:38:00 | TERRA_M-T | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fcd243e0-ced3-3d75-8e64-b49a287dc67b | -15.73727 | -54.51025 | 2026-01-10 12:38:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 94d88661-c1b9-3cd0-ba25-55f1807fce57 | -18.79437 | -52.62281 | 2026-01-10 12:38:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8f086d40-af0b-34c3-8752-286eef4fef15 | -16.82063 | -53.64015 | 2026-01-10 12:38:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6a609a8d-a584-3b97-8e3b-8624758210a9 | -14.3163 | -57.58942 | 2026-01-10 12:38:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ed720aa2-5c8a-3228-9d0a-cf872fa1734d | -19.52389 | -53.22024 | 2026-01-10 12:40:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e0089d39-a780-360c-b4eb-f2b7e6fbdb74 | -20.24794 | -46.50537 | 2026-01-10 12:40:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e381b2d1-b35a-3524-8bb6-4675576f4819 | -19.79543 | -57.37835 | 2026-01-10 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| fc0fe937-cd2b-3865-9065-f6d2f8f385a9 | -20.23808 | -46.51154 | 2026-01-10 12:40:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| acf69078-d7dd-3526-84ea-7aa218cd95f4 | -20.96743 | -49.58014 | 2026-01-10 12:40:00 | TERRA_M-T | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| b8b19f9a-a9f2-3274-abc6-dfac7c772dbc | -20.2547 | -46.5113 | 2026-01-10 13:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 8aded9bb-c590-360a-accd-a793b4b0eaa2 | -20.2547 | -46.5113 | 2026-01-10 13:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 8216163e-cf34-3d4c-9b12-2d2855dc349d | -20.2547 | -46.5113 | 2026-01-10 13:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 132.9 |


