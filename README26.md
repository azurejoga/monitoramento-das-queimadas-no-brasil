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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37371a20-b63e-3b8e-8eba-9dd4473516a5 | -13.23487 | -42.33479 | 2026-09-18 03:38:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 150.4 |
| e2b546c0-a976-33a6-b47b-fe37e76530ac | -13.23602 | -42.32881 | 2026-09-18 03:38:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.4 |
| 1bcd4b5c-602f-3225-9ff7-639a8b4d6071 | -11.22183 | -43.43027 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa04aca9-2215-3be0-92c6-c1e274667eef | -14.79908 | -48.57116 | 2026-09-18 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72310eac-08c8-3a6a-ab9f-cfbff10b388c | -10.01692 | -45.51278 | 2026-09-18 03:38:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e587247-a323-3fbe-bc0e-1d96ce69ee4a | -11.31339 | -46.77046 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa5b2cd0-2cc8-3c5e-be65-3c2dca54e5ad | -11.16385 | -42.78727 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 54468ab8-bb87-383b-be5f-5781d760fb4a | -9.90737 | -46.55417 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 940e6571-8121-31db-bc7c-3b23835034d3 | -11.31154 | -46.78159 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6d977b01-674d-3cf3-a066-70d65a688a8f | -9.39396 | -46.86615 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b7a32f15-6d9b-3bb8-aabe-af3557affd8f | -14.22271 | -48.51165 | 2026-09-18 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 25b309e4-6b78-321c-8f65-1bd44e7483f1 | -9.92239 | -46.51552 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65880914-33b6-30da-9a3c-e4d5e5a15a78 | -11.15848 | -42.78619 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 87e0bad1-1dc0-33e0-88d0-72ea08f78701 | -11.28715 | -43.35252 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c4c5114b-0b42-3bdb-a9b7-5708547b98e1 | -16.55818 | -43.99267 | 2026-09-18 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c0ec559-e028-3ec9-9b73-4df21f689d40 | -13.40075 | -42.27892 | 2026-09-18 03:38:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5d96d760-4c36-3a9d-9781-078ea209ffa3 | -12.17193 | -46.97809 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c1e2dd92-188f-3f2c-8411-b2a48628344e | -10.53407 | -44.84914 | 2026-09-18 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b60fc3cf-96d5-3d75-abbe-24e31f114686 | -16.56272 | -43.99726 | 2026-09-18 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b5504c1a-74f8-3c09-ab60-f6fe4859869d | -10.12564 | -45.57316 | 2026-09-18 03:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8eb49eec-2e36-3e6b-8fdb-2b862f6f78c6 | -9.93737 | -45.33856 | 2026-09-18 03:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34a7a6b6-5c1a-3d97-872d-2717bd268f2d | -10.54748 | -44.85366 | 2026-09-18 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 402779d2-9889-3f32-b9a5-2884751a8d9a | -11.52365 | -46.8601 | 2026-09-18 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76fa30b9-b38f-34b2-b7ed-f8dbfcff0c9a | -9.45957 | -45.45135 | 2026-09-18 03:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69de9d11-0b06-3de9-8dae-a01cf1297f51 | -11.1685 | -42.84979 | 2026-09-18 03:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b2cd507-e381-3c3b-b090-de6fe854d8aa | -9.38981 | -46.85048 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd8c0d1c-e665-360c-a67e-d6b6c984f9a2 | -14.43375 | -44.86173 | 2026-09-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbde46f4-73b9-307e-8f76-461a53bc53e0 | -11.32155 | -46.76531 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f290744e-2487-3ecc-9987-acc4087dd995 | -11.52393 | -46.86019 | 2026-09-18 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0356445e-548c-37ce-a682-6ab74a285991 | -10.12003 | -45.56744 | 2026-09-18 03:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a58bf725-25ec-306f-aad2-42da5f465233 | -11.88588 | -47.57394 | 2026-09-18 03:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49354f5d-c43f-3f0d-b9ce-8968827ecdaa | -13.2577 | -46.91621 | 2026-09-18 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f7f830a8-e2d7-3c69-88f6-97f0db4ec6c2 | -12.17017 | -46.98309 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 518f376a-563c-3eb2-a3c0-9108b2d30bd0 | -11.32111 | -43.35593 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7471807-c12f-365b-a7d6-09405aff5750 | -9.94377 | -45.33999 | 2026-09-18 03:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3e1da79-6d57-33cb-999b-02b76e0c3ddd | -11.33562 | -44.02092 | 2026-09-18 03:38:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ea5b80e-5733-31ba-9089-d290450ab71d | -13.69978 | -43.62447 | 2026-09-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3aed69a1-ede6-348c-98ae-6b631be63141 | -9.93897 | -46.60761 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5bd56d1a-7268-349f-8469-054b4b8f5ee0 | -11.27968 | -43.50993 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8ca1fdf-9c87-36b4-b146-7050e94c7da6 | -9.18658 | -46.76232 | 2026-09-18 03:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 15037ded-1be8-3dfc-86a4-0bfe0efa6d7b | -9.91551 | -46.51413 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b84feeea-fed2-3261-b852-96a57cb8f313 | -14.79898 | -48.55276 | 2026-09-18 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32248f1a-bf42-3a0c-85b8-8e054b74c6cd | -9.91026 | -46.53998 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8148a458-70ae-3788-8ac6-218d0e85a189 | -9.08862 | -45.72618 | 2026-09-18 03:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 41c240e9-455a-3874-9b1d-f1f0d4f290fe | -11.16136 | -42.78785 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c238249-4ba1-3dad-be95-11a75781bef1 | -12.17744 | -46.9856 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8b43a98f-29e1-3f99-8250-6864f5f40f64 | -13.34367 | -43.78527 | 2026-09-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c39581d3-78c1-3cb2-82f5-9f4bf3900b38 | -12.78534 | -47.56396 | 2026-09-18 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0924d6f-0710-3b17-b0bb-31b3fa91d983 | -13.6963 | -43.61947 | 2026-09-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee7123e6-308b-3a7f-9f83-423877bc7202 | -10.51782 | -46.7471 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81f81632-8813-332d-a2d2-7089333c0b40 | -11.16782 | -42.85329 | 2026-09-18 03:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c08d5861-8b6c-3fe0-9120-4abff4d231ef | -11.28501 | -43.36347 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be03f279-9ce9-34f6-86c3-339960300523 | -12.52752 | -47.08977 | 2026-09-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b0ce9425-3984-38b3-9454-c498e09a3342 | -9.10315 | -45.7228 | 2026-09-18 03:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0767931-6d6d-3351-aa57-6cad7705f055 | -14.106 | -46.94169 | 2026-09-18 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81df95b6-785d-3a3d-9c47-db63f5ae7c29 | -16.01839 | -43.60424 | 2026-09-18 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5afae0b7-08ce-31bc-8404-43de3e6ba491 | -9.91294 | -46.56209 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbc27867-bc28-3dfc-80ac-8d1ba7bd0c19 | -14.10374 | -46.94163 | 2026-09-18 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9799ca49-b0ac-3304-8ca6-e126981c0c3b | -13.61645 | -46.95916 | 2026-09-18 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6f2289ba-d093-308e-a2a9-28d3e146a0af | -12.7839 | -47.57079 | 2026-09-18 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ccaa790-c593-3daa-a6a5-e9b430ed4115 | -15.5681 | -46.44283 | 2026-09-18 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32e38da9-6d6f-3048-8914-6377798c4cfb | -9.08574 | -45.72354 | 2026-09-18 03:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 29cb9aeb-0c4f-3274-aa15-1953f34c9964 | -12.31112 | -47.96871 | 2026-09-18 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9b52e3ec-0e93-3032-9123-242e8f2f96cd | -10.51227 | -46.73914 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b55b6ea2-ae56-3ecb-bed4-c2de646612a0 | -10.11004 | -45.65155 | 2026-09-18 03:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a605c98-7239-315e-a447-680ea14256dc | -12.16399 | -46.98199 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6b3adb19-142e-32c6-ac4e-04b5991cc246 | -12.17125 | -46.97786 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d3edb0a-5231-35da-99d8-205977261bea | -11.16115 | -42.80117 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3f097651-52ba-39e9-9e0c-f44db08c52c8 | -14.43469 | -44.85722 | 2026-09-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f7fd563-b461-34b0-9f8a-441283c0096d | -10.54025 | -44.85039 | 2026-09-18 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d42942bb-b619-32ef-8413-c4f75199814f | -13.24979 | -46.92077 | 2026-09-18 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a50f9b1f-93be-36fb-8918-66dd69f6b39d | -11.16201 | -42.78439 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9294a1d2-16b9-392f-bfa1-74fbffd06633 | -10.51498 | -46.72598 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| deb03121-85dd-3ab7-9da3-f09f324782b7 | -9.3903 | -46.86606 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 11fb7e66-d8c1-3e88-b080-d68afffe1e8a | -13.231 | -42.32779 | 2026-09-18 03:38:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 0f8da44d-de5a-33d8-989c-38da8494b00f | -13.62539 | -46.94973 | 2026-09-18 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ea28f93-9180-31c3-88a5-c5d2c1413af0 | -12.16909 | -46.98832 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e0f3338-45bd-31e9-9368-8370df7b4d0b | -11.52129 | -46.87266 | 2026-09-18 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0685cdb7-81b1-3d7a-b668-9358c1616bfe | -9.76473 | -46.08624 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e862a8b1-9bd1-3d78-9867-197cc589ad4d | -9.95431 | -45.45622 | 2026-09-18 03:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec19cddc-84fa-3095-be9f-7c58459193f7 | -9.59379 | -45.86494 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ae44820f-548a-3e5b-9c63-704043397b62 | -16.56344 | -43.99378 | 2026-09-18 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75ec0fea-516e-3793-ae48-d17bf90d80ef | -10.60555 | -46.56203 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5a70956-772f-3a00-ba22-44b8596c63d4 | -10.10954 | -46.29526 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10a96315-0de3-3757-b1d4-45f0f20478f2 | -13.35805 | -46.3051 | 2026-09-18 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adc0b047-10aa-364c-b178-b96274f29ced | -12.53431 | -47.09127 | 2026-09-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c68bd4e7-65cc-3b2a-b174-0cf271197d70 | -9.76327 | -46.60006 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a45ea4c9-8ca8-381a-b76b-3278638f5230 | -10.54544 | -44.85651 | 2026-09-18 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dba73ec6-15c8-36fb-ba1c-ad799d85c8bc | -9.08193 | -45.72502 | 2026-09-18 03:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cff4e960-817b-3922-af12-a7b0a9d09f88 | -9.5924 | -45.85308 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a236d00-16ea-31be-aab8-4eeacc46929b | -11.29564 | -43.39796 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7efc0226-6c4c-3d10-bedc-b88432128086 | -11.88436 | -47.58092 | 2026-09-18 03:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1be30978-74cb-37b6-9bf3-a52f1e7ba7ff | -13.24453 | -46.9127 | 2026-09-18 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c2487191-2c3f-3618-81b2-751bb31ffd63 | -13.64701 | -46.93118 | 2026-09-18 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a7e4b2f-0eaa-3b0a-a0d7-e724b7acc3a4 | -10.53513 | -44.85108 | 2026-09-18 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 381779eb-2aed-3328-bfc5-60f82812f26f | -9.93353 | -46.53121 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e6760ac-7322-3f31-ba8b-95811810d3b3 | -9.75803 | -46.08471 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 076f3c81-aca2-3e98-ad67-d052280d4c51 | -12.17082 | -46.98329 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3a79a0bb-228a-3c90-8e26-2d7b4e606fd5 | -10.11237 | -45.57196 | 2026-09-18 03:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc4f3968-ecba-3813-8228-1b3d553bb6a8 | -10.01804 | -45.50716 | 2026-09-18 03:38:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README27.md)
