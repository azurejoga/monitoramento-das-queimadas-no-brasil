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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a2b85ef-7ba4-3975-82dc-5a53c0d675b8 | -11.32726 | -46.50058 | 2025-05-16 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67e81a58-c1a0-30d5-97ad-dd3e2aaba4da | -7.6011 | -43.33855 | 2025-05-16 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d236aa72-945b-3f40-a220-ffa5d3300b72 | -7.30436 | -43.30245 | 2025-05-16 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2317c2ac-46ec-3860-9136-38e6cadb3f62 | -11.32925 | -46.49888 | 2025-05-16 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d267412f-41dc-3345-9f0a-727b572960f4 | -11.42055 | -54.32623 | 2025-05-16 04:08:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 018f390d-bb3a-35e3-a886-27370be3e750 | -11.5544 | -47.6198 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac4bf057-3f84-3ae1-8bba-f08bd228d115 | -10.34871 | -47.98317 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f4ebed1-1c67-32f3-a66d-28f0ee0a0319 | -10.37845 | -49.30713 | 2025-05-16 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74b58d0b-9c4d-3d97-bdb2-3eb91298b790 | -6.66078 | -43.19641 | 2025-05-16 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cfdb2aa9-989a-3d7a-979b-f550f186778c | -11.61614 | -48.01591 | 2025-05-16 04:08:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9d32b72-2f48-3ee3-b948-faf8ecb4e4f0 | -11.02947 | -48.80645 | 2025-05-16 04:08:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87130be3-dc23-3b0a-acc1-cfacdd2b0c1c | -11.79657 | -47.38235 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4c59f34b-c3fc-3fc2-81ea-9ed0aba06223 | -11.42148 | -54.3242 | 2025-05-16 04:08:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c85c31f-4279-3178-ac79-f46e6b5a3f6f | -11.07274 | -47.29995 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d3e143a-e43b-3723-a532-8e4f58257e16 | -11.42668 | -54.32751 | 2025-05-16 04:08:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7395c6b5-0267-3387-b760-a49f53c2b455 | -11.6202 | -48.01661 | 2025-05-16 04:08:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 131a5300-1257-3f5f-95e8-e0e0ba887c7c | -11.63055 | -48.47176 | 2025-05-16 04:08:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fba2f7de-b73d-3f6b-94ec-ddc804bfd884 | -7.45632 | -49.77591 | 2025-05-16 04:08:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9780125-a0c6-334f-a336-86f36d9326c5 | -10.34939 | -47.97932 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6920bfaf-901e-3ef6-820f-68723d9034b8 | -6.66136 | -43.19279 | 2025-05-16 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4569addb-19a3-38df-ae18-48f936874fec | -12.28787 | -43.5393 | 2025-05-16 04:08:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cc4a39a-0533-376c-a702-57da511c5788 | -12.34686 | -49.95611 | 2025-05-16 04:08:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2cf9805-a562-3e69-8f05-bc27765bfdc2 | -6.62046 | -48.00861 | 2025-05-16 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dab1298-8511-3306-a2d3-a9f5260f7b8f | -11.42052 | -54.32914 | 2025-05-16 04:08:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88033134-4ba5-31be-9c08-1795294ed1bd | -7.07526 | -44.91529 | 2025-05-16 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e65cd65-8166-3fa4-8ab1-03eccd936d7b | -11.16229 | -48.67506 | 2025-05-16 04:08:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 64179233-4440-3adc-8199-9a0cc40b8cb3 | -11.78833 | -47.36025 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2eeefee-3e9d-3081-a3b4-20ab08f809b7 | -11.58694 | -47.87172 | 2025-05-16 04:08:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6898ef21-bdb9-3168-a14f-cbafc2e04a14 | -12.26184 | -49.31422 | 2025-05-16 04:08:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1a114dd-6649-32cc-9703-488b97e813b2 | -11.16346 | -48.67629 | 2025-05-16 04:08:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4278efbd-55c9-3d7c-bf97-62b5e3f3b615 | -10.35836 | -47.97678 | 2025-05-16 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6703cb0-b4eb-3bef-b5fa-466c59b71de5 | -9.44845 | -40.40131 | 2025-05-16 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0b350ae4-0fc6-345a-9b9a-2a523ff80933 | -11.55957 | -47.61346 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22305e50-7b5e-35ab-b78e-60f8c1583f70 | -10.06603 | -48.08348 | 2025-05-16 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de74419b-1ccc-3699-997a-a07055d42eec | -10.46338 | -49.05219 | 2025-05-16 04:08:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f992969-074c-37fd-bf95-1e3a8b50ca3d | -7.54402 | -45.87252 | 2025-05-16 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8be9d25-d029-30d8-875e-539cbece47b0 | -10.34453 | -51.69262 | 2025-05-16 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e6d3614-5b08-30c3-bdf3-563578a8d646 | -11.78919 | -47.35524 | 2025-05-16 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fc3482c-8c71-3d0c-93e7-61b1839ffe24 | -10.34517 | -51.6892 | 2025-05-16 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd1d4547-8fa0-35f8-b940-ee1365fcac27 | -11.57534 | -47.60907 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 725e7ac0-f49f-39b1-a90f-697e7b0369d7 | -12.34037 | -50.32541 | 2025-05-16 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| beaf1a44-daf9-34ac-9984-f6c0d391ab3d | -7.54254 | -43.39193 | 2025-05-16 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8a8cd47-ca06-302a-abe6-94b102b47e35 | -7.70955 | -46.32688 | 2025-05-16 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddaecebb-0029-3138-af0e-7d890d137a4d | -13.40904 | -44.14956 | 2025-05-16 04:08:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2a12d35-53da-395b-b8cb-a7eebdcee23b | -11.55501 | -47.61627 | 2025-05-16 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0b43490-553a-3e04-b3ef-4ec494a18c9c | -7.07887 | -44.91586 | 2025-05-16 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0154769-f0c7-3e09-9674-ad20df95a4b2 | -9.3652 | -48.39967 | 2025-05-16 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f44f79a-37bb-3974-92d0-5f418f68a535 | -9.66863 | -47.561 | 2025-05-16 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc71e24a-bea3-368c-9525-04ab331a4b6f | -12.34535 | -49.96318 | 2025-05-16 04:08:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f9c0851-b6cd-3866-ae75-c47267a7d2fc | -7.30378 | -43.30608 | 2025-05-16 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b75d19cc-d108-39b8-92a5-900cbc7f854c | -9.36954 | -48.40037 | 2025-05-16 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01966e2a-bad6-3950-b2f7-221726ff5a3c | -6.6574 | -43.19587 | 2025-05-16 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b8eb8b8c-c202-334d-9aa6-082f0b3c4f55 | -7.21399 | -41.33212 | 2025-05-16 04:08:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0be6beb4-2b37-33fe-b445-5b395be16f01 | -17.486 | -53.83399 | 2025-05-16 04:10:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 398c28b5-4c58-3da2-8072-29b6be061019 | -17.00879 | -49.78028 | 2025-05-16 04:10:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a18122f-0c48-3fd3-a9b4-a10dea3175bc | -17.66497 | -46.68466 | 2025-05-16 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88e3dbc8-0ad9-3479-be4b-7a11c826d413 | -12.87257 | -55.06714 | 2025-05-16 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 102f9022-4ca1-3d0f-a532-3cab04105901 | -14.01425 | -55.13742 | 2025-05-16 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4948452-6ac4-3a7f-abaa-fed5310b447a | -13.67296 | -47.96534 | 2025-05-16 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 601173f8-3d63-33fa-b964-52a3fb0582fd | -13.59513 | -47.37668 | 2025-05-16 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57570dca-df2f-3869-863b-ba4ff0e375ed | -14.17347 | -45.47856 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03dfe3db-a75d-301f-9210-e0e0d9687968 | -14.87095 | -51.97878 | 2025-05-16 04:10:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22cec059-acda-321f-ba0c-eaec542b4894 | -15.18573 | -46.83504 | 2025-05-16 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86e7f488-9bab-3520-b939-4a05f02d8b74 | -21.23998 | -44.16924 | 2025-05-16 04:10:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c69c54db-ede3-3816-b359-e5c97c3476aa | -14.18378 | -45.48034 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d67deef-4ac7-3868-91bc-7364beb6ead3 | -13.28466 | -45.42958 | 2025-05-16 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de5e383e-82cb-3f23-a30d-2e4c555cd49e | -14.17474 | -45.47084 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bbecf64-a55b-3240-ab21-b4a240f72614 | -19.16228 | -47.81857 | 2025-05-16 04:10:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3cb84800-8d3d-3eb6-8131-1bf8c5438bd8 | -14.87593 | -51.97979 | 2025-05-16 04:10:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95237ec4-65f5-39d9-930a-91747096872f | -19.45346 | -45.30814 | 2025-05-16 04:10:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0628c83c-bbed-30e6-9214-bc6b0e8a9d0a | -14.17907 | -45.48747 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dd4640c-97ce-3cb5-b9fe-90b3abafe8b2 | -13.29331 | -47.23125 | 2025-05-16 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72920d64-8a72-3901-9f2f-903db7bea60f | -20.34879 | -40.35997 | 2025-05-16 04:10:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d14c549c-7e6e-35fb-b89f-57ebdd3eb94b | -20.31149 | -45.58143 | 2025-05-16 04:10:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1e81ba6-e223-3a1e-b0c0-cc7a1d654e5e | -19.06894 | -53.45494 | 2025-05-16 04:10:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 24af2be0-5155-310b-af7c-fe5cf95caad8 | -13.04045 | -53.71883 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa658dd4-bc79-3ade-b1e5-fb2ead3129ff | -12.87657 | -55.06529 | 2025-05-16 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03ea7055-04aa-3847-8497-718e22e790c8 | -13.47618 | -47.25503 | 2025-05-16 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f0ca02a-5bf3-3409-8481-26bc47b51271 | -11.9186 | -54.40911 | 2025-05-16 04:10:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6979adf0-18aa-37c7-9c79-a9fc7815e08f | -14.17067 | -45.47411 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4eabb98-64e9-3abd-a273-458902a74044 | -15.26631 | -51.46649 | 2025-05-16 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2da268bd-a4ab-3d78-ae9e-8f0acaa886c6 | -14.17411 | -45.4747 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 984d24a0-05d8-39d4-982d-1048b2a52236 | -14.01626 | -55.12776 | 2025-05-16 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 879e5a59-9049-3f7c-bede-52c93c3a3a1c | -17.47346 | -45.46599 | 2025-05-16 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 799d907c-9f9f-3f66-a92e-ea08fd94da66 | -14.1797 | -45.4836 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 362e9d0d-37c6-3f1c-8344-2d66aa6bd2a4 | -19.53467 | -43.92064 | 2025-05-16 04:10:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e23db6a-4400-3cb5-9c94-506fdd433555 | -18.62715 | -40.67447 | 2025-05-16 04:10:00 | NOAA-21 | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c6966999-65f1-386e-b67b-f0fba1c50d5b | -15.27005 | -51.4728 | 2025-05-16 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 565533a4-b39c-3912-9fe2-13f5af57f0dd | -15.27109 | -51.46743 | 2025-05-16 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e0952884-bfac-3aba-8587-50a53ac12904 | -15.55726 | -44.40398 | 2025-05-16 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9ac54655-2e62-39d8-851f-677e76eb331d | -13.05131 | -53.72068 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d095f2d1-53f7-36b5-8f1e-52a92e9a3ebb | -14.0193 | -50.70977 | 2025-05-16 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adf63fe7-4098-3d9d-a94a-de8218ff5601 | -14.16851 | -45.4658 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2316d676-da77-365a-9862-88abec7e898c | -14.17691 | -45.47915 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fa9618b-7695-34e0-bf15-389d62f0d5d8 | -20.7655 | -46.76775 | 2025-05-16 04:10:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f2701084-c212-3a49-abe8-7a6f51870398 | -13.3973 | -47.50836 | 2025-05-16 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33595cc2-e873-3a97-a6a1-af057a439fc5 | -14.17627 | -45.48302 | 2025-05-16 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6df313cc-3828-3900-ad3f-d2a2c910d91c | -17.8004 | -44.36038 | 2025-05-16 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b63f59a8-0a75-3d13-9a0f-9a3127b6f404 | -13.04128 | -53.71476 | 2025-05-16 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ceff21f-e2f2-3b87-8979-0ac632237296 | -17.48672 | -53.83057 | 2025-05-16 04:10:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README5.md)
