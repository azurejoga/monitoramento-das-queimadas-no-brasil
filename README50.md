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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77ade872-44e5-3db2-a3b8-6ee320ebda3c | -14.2982 | -51.75 | 2026-08-24 11:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 24fbe7f8-8110-3bfe-9c72-5a2bd58e4e0b | -13.1512 | -51.3854 | 2026-08-24 11:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| e0dcee8e-891b-3dae-bb83-1936664a9a75 | -11.0969 | -46.19 | 2026-08-24 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 378.5 |
| c9ed7502-a039-3360-80e9-f19f2912ec07 | -13.1512 | -51.3854 | 2026-08-24 11:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 325d74c1-af4f-3c94-98d9-5181c4429801 | -11.116 | -46.1875 | 2026-08-24 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 7c84d618-8a7d-34ef-a45f-64cb23c928f3 | -11.0969 | -46.19 | 2026-08-24 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 1643802c-0b33-3cca-b87f-ea3ffc9d923b | -8.5895 | -49.9713 | 2026-08-24 11:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 306f2eb7-40ca-3595-90e8-e4ff0da5be1a | -11.0969 | -46.19 | 2026-08-24 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 01cd5f3b-bcec-31c8-871e-8b90067d0a32 | -13.1512 | -51.3854 | 2026-08-24 11:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 849d5d0e-e00c-3f76-8e15-1196c84266a6 | -11.4494 | -44.5353 | 2026-08-24 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 20c5e367-12e3-367f-abc4-9ed0e8ca564a | -11.0969 | -46.19 | 2026-08-24 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.0 |
| f3600151-b432-3866-9e41-847022e36f80 | -15.3431 | -53.9592 | 2026-08-24 11:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 696bf9ae-d13e-31c5-a56a-cebad79b6e02 | -11.4494 | -44.5353 | 2026-08-24 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 41157491-fa6a-3db8-bc32-9587c708c034 | -15.3237 | -53.9617 | 2026-08-24 12:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 60a374ff-394b-35cd-a64c-e7b994bb3992 | -7.2901 | -45.3683 | 2026-08-24 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 0ba8e360-7ba6-3047-82f1-1c1cb062bbbd | -15.3431 | -53.9592 | 2026-08-24 12:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 86390185-23d1-3116-81e6-b3b6b74bff5b | -11.0969 | -46.19 | 2026-08-24 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 1b278991-60e5-3917-8253-136426d7827d | -11.1163 | -46.1648 | 2026-08-24 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| acab10bc-f959-3a4d-9d69-fd83df16efac | -17.7021 | -46.3866 | 2026-08-24 12:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 898c47d6-3e74-394d-9a59-14ce095aa414 | -15.3237 | -53.9617 | 2026-08-24 12:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d150a003-5a4a-3278-ac21-b526f5c0bf47 | -7.2901 | -45.3683 | 2026-08-24 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e73fb73e-077b-3040-b5ec-0fd59776a0e0 | -10.7985 | -50.9518 | 2026-08-24 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 50482028-6a6e-3b07-aae4-b7295e96be6b | -11.0969 | -46.19 | 2026-08-24 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| c14306b7-6506-3941-b633-32b9279d9326 | -13.1512 | -51.3854 | 2026-08-24 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| f3ada912-024b-32b9-8d59-23d707719041 | -17.7021 | -46.3866 | 2026-08-24 12:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 123.6 |
| db99a063-7646-387f-9cb9-c0ff1323e183 | -15.6951 | -53.8088 | 2026-08-24 12:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 05251d28-729f-3e1f-b0b4-881b41adb364 | -8.1111 | -47.4812 | 2026-08-24 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 27e237e0-f10e-37c6-a1cc-d8cc16d4d9a2 | -7.0193 | -48.0106 | 2026-08-24 12:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 617a3c23-8039-3d31-b87f-eea0f3ce8685 | -7.2901 | -45.3683 | 2026-08-24 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| fae63d5f-6769-35b3-b0ba-edf2e69000e6 | -10.7985 | -50.9518 | 2026-08-24 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 849a286e-5f0e-3a8d-99db-d2a7469bba52 | -11.0969 | -46.19 | 2026-08-24 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 24638aa7-fbce-3de8-a8b2-f0ae7a3d525b | -12.8743 | -48.4735 | 2026-08-24 12:20:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 7e703b78-3889-3887-9789-3346b469270a | -15.6955 | -53.7878 | 2026-08-24 12:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 4215337c-6f9e-3e13-b235-5df23f590465 | -1.32025 | -53.13322 | 2026-08-24 12:29:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fd78d1a9-ad35-34f3-a2c2-893e84f3d330 | -10.6305 | -52.2518 | 2026-08-24 12:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 2b859095-dbb4-33aa-a88f-607b2c425b21 | -15.3237 | -53.9617 | 2026-08-24 12:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| fe472f36-5886-3165-a342-7a6234a1f89d | -10.7985 | -50.9518 | 2026-08-24 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| ebd387e5-1c68-3cad-a25c-5a82e183898b | -9.7321 | -46.0207 | 2026-08-24 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c3e2f247-cf58-32a7-8754-9b194cb6caab | -9.7131 | -46.0229 | 2026-08-24 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d85e3cc1-1c68-3d96-9495-fce86e7c7061 | -9.7324 | -45.9981 | 2026-08-24 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ed11d7e3-7463-327b-b9bb-af17ad14cdd9 | -12.0566 | -50.5567 | 2026-08-24 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3c0da67f-96d4-30ef-a241-961fd3339e8f | -9.7134 | -46.0003 | 2026-08-24 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 9b5999b3-397d-38d8-880c-c5f9d1a6523c | -14.3558 | -52.9083 | 2026-08-24 12:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5d8955c9-4c25-3588-a47c-d3309bc9d96e | -6.8491 | -52.505 | 2026-08-24 12:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 1bc8ce1a-ea4e-3c55-bb2d-0f8d981d1314 | -6.8305 | -52.5061 | 2026-08-24 12:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 3e37d51a-5d82-32ad-b4b1-748c5e634a4f | -7.2901 | -45.3683 | 2026-08-24 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 3b0b7c00-b927-3903-b638-c912873a37fc | -7.0193 | -48.0106 | 2026-08-24 12:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 28129715-533e-3e41-827f-92ff78234a28 | -5.78473 | -57.56295 | 2026-08-24 12:32:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f3385772-e3fc-3136-978a-c6598bbdbeb2 | -8.96198 | -50.74966 | 2026-08-24 12:32:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e1f7dea4-ce6e-3d8e-9d04-faf715e4197a | -8.59988 | -49.97755 | 2026-08-24 12:32:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7f8636de-dcf6-32a0-a34a-8c8471012246 | -7.44056 | -59.77742 | 2026-08-24 12:32:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b734d499-828c-37cf-9e4a-d439d47711e8 | -6.34846 | -54.75124 | 2026-08-24 12:32:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e8eb8183-9bcb-35a9-b824-6d528c5263c1 | -5.94486 | -57.73419 | 2026-08-24 12:32:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 943e2a95-399d-32d9-9813-e14f3f28f726 | -6.22785 | -55.92237 | 2026-08-24 12:32:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29ccffab-5ef4-3de8-be22-779872ea6d28 | -6.15531 | -57.94542 | 2026-08-24 12:32:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fb7be279-68c5-372a-8828-24f207b276fc | -6.12401 | -57.83491 | 2026-08-24 12:32:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 50578885-f137-3e23-b8fe-2e0834b6dbf2 | -6.64111 | -58.48284 | 2026-08-24 12:32:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6ea1f5b2-f421-3a10-91d8-bb962ce7f546 | -7.76261 | -61.10565 | 2026-08-24 12:32:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0bb55d2b-d2b8-38e5-ab56-ae05f349b952 | -6.84121 | -52.50418 | 2026-08-24 12:32:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 168.2 |
| a920db13-9f05-3420-b2ef-b2fe1ce5714a | -7.22571 | -60.62568 | 2026-08-24 12:32:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ff25e842-3783-3bfa-84c7-b42d1f1fdc1d | -6.23051 | -55.61927 | 2026-08-24 12:32:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7cf656c5-6afc-3167-8d4a-4d99a524add2 | -6.13981 | -59.9063 | 2026-08-24 12:32:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7ffa1a02-cf31-3050-83bb-d531537454ae | -7.26227 | -60.61756 | 2026-08-24 12:32:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6b515056-092d-36ac-b66e-bfa6216aa4fd | -6.56047 | -58.5911 | 2026-08-24 12:32:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8f3dbb97-73b4-3c31-bb0b-2b8cb606f1c6 | -6.77412 | -59.73173 | 2026-08-24 12:32:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2f0d1575-2f4f-3ff4-a48f-70fc94b0ee54 | -7.78584 | -56.28582 | 2026-08-24 12:32:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 67614443-52af-35e1-9759-0d13721f66df | -6.63228 | -58.48161 | 2026-08-24 12:32:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fbcbf9f1-3f6e-3a10-9ebd-31e94c245e8d | -2.88455 | -48.84184 | 2026-08-24 12:32:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e2b41e43-04d5-32eb-9b03-81fe337262be | -6.61721 | -58.38308 | 2026-08-24 12:32:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 803072d3-e7db-341b-9860-3c142fc09257 | -5.94613 | -57.72523 | 2026-08-24 12:32:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| be608e4f-6cab-39df-8fce-4a4174aa3542 | -6.21829 | -55.92107 | 2026-08-24 12:32:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9a8dffa1-9795-3dd1-ad4a-d67094883299 | -7.26372 | -60.60774 | 2026-08-24 12:32:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0730375a-94d4-3e09-bbf3-37ef810e70a4 | -6.14771 | -57.9353 | 2026-08-24 12:32:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c8baaba4-15d4-3be3-b6fb-0120042a595b | -10.88021 | -51.04617 | 2026-08-24 12:34:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 8217961b-e31a-3400-b7e6-12aa809fc861 | -14.39677 | -52.94271 | 2026-08-24 12:34:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a61bbbd5-c201-3166-99e0-f278f7bfc5f1 | -14.24784 | -51.76845 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 35ba2cd8-b02c-3f6c-b2b6-33194c7ba7b3 | -15.32744 | -53.94291 | 2026-08-24 12:34:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f3dc6d0b-1023-37be-b187-14661075cc14 | -15.33789 | -53.96439 | 2026-08-24 12:34:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 7e6363ec-27f3-3652-887e-ccdbd5775b83 | -15.268 | -52.83272 | 2026-08-24 12:34:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 47780670-9ffd-3f05-add1-c610467c7830 | -15.29435 | -53.17517 | 2026-08-24 12:34:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 4bfa27df-946f-3f79-aee4-e9d69f365a70 | -14.2634 | -51.76316 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 557.0 |
| 6ef73074-29c8-31f0-bead-d1ba582ed110 | -10.80246 | -50.9381 | 2026-08-24 12:34:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2fd159da-d9eb-3562-9c68-2b4f417df424 | -15.40987 | -55.77411 | 2026-08-24 12:34:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c03281b5-b4b7-360d-8231-ad7c3ee9bb48 | -14.2806 | -51.74322 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 7ac38e20-0daa-3bc1-8680-4ae854b690cc | -14.26656 | -51.73473 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| f952676b-e7ae-37a0-a632-0215438dc3ed | -12.06641 | -50.57486 | 2026-08-24 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 77735c46-8162-391e-8c84-a18a2be8ef24 | -15.51869 | -53.9781 | 2026-08-24 12:34:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8247ae9f-f9c8-3ecf-8b71-28de2e798d45 | -14.2776 | -51.7717 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 981d5cf6-a911-38dd-ae54-d2d5ea859371 | -14.29248 | -51.77333 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 07b5039f-796d-3121-8836-61befe009586 | -12.0568 | -50.56663 | 2026-08-24 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0a3ee869-9402-397c-9dad-e551ac25f216 | -10.80105 | -50.94302 | 2026-08-24 12:34:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 2024cf78-919c-3e43-839f-2616d3b29f6e | -15.26548 | -52.85601 | 2026-08-24 12:34:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 93e1ae8a-6b50-387f-bee4-8ac6d4144092 | -10.4392 | -50.43853 | 2026-08-24 12:34:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 60563250-af40-376f-9053-da096a8ba5a0 | -10.02121 | -59.34966 | 2026-08-24 12:34:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d30dbf63-979e-3ba9-8680-d1e0dfe5fc05 | -13.87405 | -54.00513 | 2026-08-24 12:34:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 19eafbf5-e856-31f1-8cff-16dd8f6e70c9 | -14.25077 | -51.73996 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 31065158-a203-3cfe-a55d-c8f7f8b552cd | -10.632 | -52.24126 | 2026-08-24 12:34:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d6fbee33-e437-3cd7-bbf5-a4dd07a0bc1f | -12.05691 | -58.03449 | 2026-08-24 12:34:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 9ecb7ae1-50bb-35d0-b7d8-f5345f21b374 | -14.35079 | -52.90794 | 2026-08-24 12:34:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 8654be42-b47d-3896-9ae0-a402ea7b6621 | -14.24851 | -51.76158 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 191.1 |


[Clique aqui para ver as próximas entradas](README51.md)
