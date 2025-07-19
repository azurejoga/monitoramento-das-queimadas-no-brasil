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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9405abe-674e-345b-96a1-7faa839560c1 | -10.68005 | -56.54485 | 2025-07-19 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bd1cf0b3-e067-3e12-9a39-6f649970b273 | -9.81129 | -47.74623 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2582c3c-22a0-3b3b-8f1e-c9876d46aee5 | -10.80533 | -46.76812 | 2025-07-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da722eac-ffc0-381f-8b14-3af2d6123ece | -10.98525 | -49.38745 | 2025-07-19 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a323e84-c43e-3f2a-8e12-ac278a762d68 | -13.04578 | -49.17768 | 2025-07-19 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04ad635b-dc91-3922-87f3-ff05169db9f9 | -12.99333 | -46.94296 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0df03b5-f65b-3954-adf8-a3d4d0874b86 | -11.48228 | -47.3296 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bdccc479-fc81-37c9-a24b-bfa17e7471e2 | -6.75002 | -45.51921 | 2025-07-19 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f56e077e-8f55-30d7-944e-ac140a1fa165 | -7.48897 | -47.50447 | 2025-07-19 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e21598b3-4d3d-3a31-ac72-aa6c10fcb1f3 | -8.32652 | -47.50032 | 2025-07-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 682cc878-a851-3fe1-ad5f-bb53308c9bdb | -11.83843 | -48.20999 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cf532aa-ca76-302f-aa3a-15afc71bca05 | -9.24352 | -48.56228 | 2025-07-19 04:57:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1829976f-3fc3-3512-8fd3-176a98c164a0 | -9.76499 | -48.74609 | 2025-07-19 04:57:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 244756fd-0f42-3840-8791-444564d3b92b | -6.76236 | -45.5076 | 2025-07-19 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37a1a372-ea3d-3223-b3fa-aa79ccaa52c1 | -10.93484 | -56.83863 | 2025-07-19 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fde94fe-a861-3e69-b5c1-5ce80e07753e | -8.07004 | -50.07499 | 2025-07-19 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbd7ac48-a28e-3b85-82a3-6afc448cc4b5 | -10.81731 | -49.28577 | 2025-07-19 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7046e6bb-e544-3feb-a28e-845a6df5d416 | -7.10147 | -49.93407 | 2025-07-19 04:57:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1eff8f3e-0c1e-3ac0-8070-3f21a048e445 | -7.48924 | -43.93426 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a24373c3-6120-3d39-aece-6c7905ff26eb | -8.2656 | -55.16845 | 2025-07-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eafb8949-51eb-3709-8dce-d4dbeacf8205 | -8.88263 | -50.15741 | 2025-07-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 271bc197-d44e-383d-86bd-050da5338460 | -9.94864 | -48.16939 | 2025-07-19 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38b78e36-ec2f-3bbb-a457-b517c4fdb0e6 | -8.96781 | -61.50504 | 2025-07-19 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acc1ffe9-9284-3fac-ab9e-f29c92a7532f | -7.903 | -61.51044 | 2025-07-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7429bcb0-7c72-3472-a20f-d1676f192942 | -10.63736 | -45.23643 | 2025-07-19 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8be309f2-1dfd-3216-b2f9-a35d9e8a8e6d | -13.60613 | -45.6404 | 2025-07-19 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb7dcd42-1e91-34f4-92bf-c3c40bd3053e | -11.56424 | -47.09372 | 2025-07-19 04:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 738bbe89-ba21-3d7a-85e4-cf72edd4ae3a | -7.70646 | -47.28962 | 2025-07-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50654538-583d-3944-bcd5-9a07cdb58c85 | -11.32338 | -55.20992 | 2025-07-19 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 203b48d7-d08b-3605-9794-1ca47bc75cb3 | -8.07335 | -50.10661 | 2025-07-19 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62e97e8b-24b5-35e7-9d76-c97bb9e14fcb | -11.55919 | -47.09302 | 2025-07-19 04:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c11b9f90-756d-3fa6-b27a-02f1c953b504 | -8.54811 | -47.84971 | 2025-07-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98a276f4-1e4e-3ffa-b40b-7726cac168a9 | -10.75978 | -52.76528 | 2025-07-19 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 251a17a6-dc3e-3f43-a1cb-1a12f7467b2e | -6.91884 | -44.83173 | 2025-07-19 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0f6db3d-085d-3081-9463-3654a386c9a2 | -11.55958 | -47.08997 | 2025-07-19 04:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3314b8e-43b7-3fd7-9f81-e9615bbad681 | -6.91333 | -44.83092 | 2025-07-19 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60d12368-abc4-3955-9689-b76e6af0c5ef | -8.06927 | -50.08019 | 2025-07-19 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfe08d19-54cc-35a6-aeb4-121ae388e58a | -8.97218 | -49.84953 | 2025-07-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3ce7b93-f4e1-381e-b13c-adec4f2236a8 | -12.97484 | -46.92126 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b15a29e-2ec1-3843-8152-7384e34bd025 | -11.96306 | -45.46981 | 2025-07-19 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0769872-e5da-3e1c-a0fe-d080955960f8 | -11.83308 | -48.21432 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 82f818d2-def9-365f-8d76-dc1fe7b340b0 | -6.44529 | -51.88833 | 2025-07-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 472bd477-197f-34a5-b258-613f55577eee | -11.48803 | -47.32441 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1621e833-2fba-349b-b406-b4c135b15d07 | -10.06213 | -59.10025 | 2025-07-19 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fb8a320-7153-3a17-a923-31176c58a249 | -10.68207 | -49.67423 | 2025-07-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33f86408-53e1-344d-817b-d975e81e28d6 | -10.62537 | -44.76971 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 501b9824-439c-34a6-ab89-617949c5e5b1 | -7.35366 | -45.32234 | 2025-07-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebb7ba85-a7f9-3d01-a92d-4809ffa13391 | -10.63148 | -44.76462 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e33e30c3-2b4b-3906-863d-4af06251e947 | -12.36926 | -50.33344 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ff4eb4d-767a-30c4-a51a-1d703141b6df | -7.35625 | -45.32276 | 2025-07-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d89d217-a43d-3be0-ab6c-16a3866da653 | -6.75574 | -45.51659 | 2025-07-19 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00571962-545d-3746-930b-f413ab67aa35 | -10.72726 | -46.78752 | 2025-07-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7218cc59-14f1-3108-bf76-fdc5207bde80 | -13.05025 | -49.17836 | 2025-07-19 04:57:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 99b0d114-e855-3b77-9b12-eca8e3b19e5b | -13.61184 | -45.64119 | 2025-07-19 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3372664b-6850-3fdf-8dea-781879ca36af | -12.42877 | -45.37364 | 2025-07-19 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c267a163-fb8b-3b81-933b-69559facc5a6 | -10.36305 | -57.50506 | 2025-07-19 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cadc209b-678c-3433-8ae7-88b893c5cc66 | -9.80931 | -48.55992 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e0bbabfa-5858-3fa4-afd7-110a27bc2276 | -11.48306 | -47.3238 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4563b198-7e8a-3c17-92a1-e368a3f53d5a | -10.68221 | -56.54429 | 2025-07-19 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b16dd58-61d0-3003-8014-58c4e9dbd239 | -11.5658 | -47.08158 | 2025-07-19 04:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bee1a6f5-4519-31a9-b1d1-4d22d5f8a14a | -9.81348 | -47.74183 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 69cba5bd-81df-37d3-a69f-d8cb4c8854d2 | -9.02153 | -59.76693 | 2025-07-19 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 843d077c-24a8-350f-b7cc-b68c74080d70 | -12.37062 | -50.32997 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca2eeed3-0611-3025-ba22-1311c3afa14b | -11.47808 | -47.32317 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dbe0db72-a14f-35d5-b995-6d0c26210112 | -12.06669 | -47.34637 | 2025-07-19 04:57:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1686ded7-2a45-3084-8bfb-6d30ae3fff29 | -7.1707 | -44.10257 | 2025-07-19 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27479b4e-70cc-3a56-9a6e-e3c9491215f2 | -9.80485 | -48.55936 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ad819f2-7fa5-348e-993e-da20076f7400 | -10.62566 | -44.76386 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6e2db64b-6d2f-3e63-a172-cc2c4534cadf | -10.76037 | -52.76132 | 2025-07-19 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08cc2de7-b984-3408-83c5-fe159ea0deec | -9.48072 | -40.38352 | 2025-07-19 04:59:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| c0c5a209-de1b-30ea-8a88-992e8e21e322 | -5.65285 | -43.72592 | 2025-07-19 04:59:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 889086ef-f061-30a9-bfc8-6ebb4b3f5c78 | -9.48819 | -40.37177 | 2025-07-19 04:59:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| cfaf1a2c-193c-3382-8929-93f8cc404b1e | -14.78373 | -48.29609 | 2025-07-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f59f01f-4abd-317c-9f82-909a7724469d | -18.65889 | -55.71694 | 2025-07-19 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 975ffa66-87b2-3397-a966-29b51435defb | -18.2057 | -54.46374 | 2025-07-19 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6aa2b465-5dfe-3f57-b70a-254f2bfea6c3 | -14.70883 | -45.06926 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a086aead-1b1e-3b12-beb3-a7f00e976f7a | -14.69683 | -45.06754 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ad8cec0-d457-320b-b60f-75c7a1547bbd | -14.78434 | -48.29124 | 2025-07-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c13580a-ea28-3345-9e5f-8ee8683343b9 | -14.48297 | -46.36013 | 2025-07-19 04:59:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3dcc058-b23e-3b49-9db4-a2b4ef32151d | -15.70109 | -48.13193 | 2025-07-19 04:59:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb4d7242-8e97-3e7f-846c-96680a9924fb | -12.25596 | -63.82423 | 2025-07-19 04:59:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a328d08-a3d8-3ccc-8e5a-23140e0cd581 | -15.89229 | -43.45799 | 2025-07-19 04:59:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 88cba2ab-9f2d-3884-b0e3-7bc49dc11576 | -14.84496 | -49.1264 | 2025-07-19 04:59:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23310982-0ab3-3bf1-8531-f193cf1e7b6b | -15.70175 | -48.12634 | 2025-07-19 04:59:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab9efd04-552b-3aad-ad80-9962b44e8e22 | -14.78241 | -48.29244 | 2025-07-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 40c7c14e-9ea9-30c8-931f-2a28818e3de1 | -15.99215 | -49.81846 | 2025-07-19 04:59:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d3e11cc-5aad-33a5-9828-0a8c92c2d76c | -10.97927 | -68.52935 | 2025-07-19 04:59:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cb5a033-8379-36cc-a7a8-1c2a9ff5ef5c | -16.89888 | -52.68027 | 2025-07-19 04:59:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 192da628-d81c-3ed9-b3da-0df20c546877 | -15.99449 | -49.82106 | 2025-07-19 04:59:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a819a4a-3234-3b8e-89d2-281fae8d1986 | -18.66227 | -55.71749 | 2025-07-19 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 866da750-c9a9-3c08-bc67-1cde3c1c50f8 | -12.3537 | -60.71199 | 2025-07-19 04:59:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c586d0-fa11-36cf-84b5-16e4cf021555 | -14.70335 | -45.06371 | 2025-07-19 04:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdea0fce-8fa6-306a-b33a-8509d68eb9f3 | -14.47745 | -46.35944 | 2025-07-19 04:59:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4abaebab-929e-3de9-840a-904df13db4ef | -15.66912 | -58.67887 | 2025-07-19 04:59:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 2894f8d6-da21-38a8-80e9-f682df2d2155 | -13.66247 | -59.83867 | 2025-07-19 04:59:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80f1e2a6-e92e-34c6-9600-5b3bf2af9de0 | -18.95128 | -53.74618 | 2025-07-19 04:59:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37c2e21b-4dce-33f1-919f-fd2e2d8def0e | -15.61392 | -55.98058 | 2025-07-19 04:59:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 843486d1-6f81-3959-9f1f-d61833189421 | -15.99602 | -49.82369 | 2025-07-19 04:59:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48897bf6-5cb4-3e38-a5a6-fb75e7e6439f | -15.99661 | -49.81913 | 2025-07-19 04:59:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be6e8857-6c74-37c9-b2b1-06ae1f80b7c6 | -14.17677 | -58.1973 | 2025-07-19 04:59:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README29.md)
