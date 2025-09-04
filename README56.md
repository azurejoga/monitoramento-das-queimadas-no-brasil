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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cceed925-9980-32e6-b76c-fc8d4af3af7e | -6.25954 | -43.31466 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00c07d69-2523-3595-a217-dc7396579ad7 | -6.46725 | -43.97485 | 2025-09-04 04:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d90b167-05e9-358c-a8ed-300018491f25 | -6.46764 | -43.97211 | 2025-09-04 04:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 105f431f-7664-3696-88c2-f8171381d56b | -6.26519 | -43.28487 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17068999-fee7-30fb-914c-2fc1c43044c3 | -7.94296 | -44.94147 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9ca5653d-12fc-33b7-b6e8-7fabe9778aa1 | -6.16647 | -43.31233 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3642206f-bbfd-34d8-bb46-ff640647eecb | -6.68305 | -48.41025 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0fe95101-047a-3574-a21f-03827a301dc0 | -6.78727 | -44.08784 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 630d80fd-2c38-3d0b-b8e7-95134cb9e8dc | -6.46826 | -43.97809 | 2025-09-04 04:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d3fca80-4b4a-3823-8c94-f82b55642a61 | -6.69301 | -48.40889 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9a89dd0-ddfb-3437-972f-4e9d071e94a5 | -8.01095 | -44.77716 | 2025-09-04 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ac0f622-4014-3de9-8ef9-eb009ffdb9bc | -6.26843 | -44.50748 | 2025-09-04 04:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e2fbb42-9a1e-3ee4-8ec3-bd816200dbd3 | -5.6095 | -57.36527 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d983adff-b3fd-3b9c-bca4-0fb0da7e3a3e | -7.70777 | -50.25126 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72f973a5-576e-3cb4-a753-c5598345b7d1 | -8.53381 | -51.31362 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3969867-9221-3f33-af49-64712c33eeaf | -6.28344 | -43.85059 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a46eeb2e-7656-3de6-ba80-b13bff57ff46 | -9.0601 | -46.98898 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f795f843-af63-379c-927b-5d0ec020ed6a | -7.74122 | -48.76596 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a2d87a2-60d6-3476-810e-7079fb080008 | -7.60587 | -55.26867 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0435b589-5acc-3f42-a544-63021a950289 | -7.04659 | -43.2637 | 2025-09-04 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d0339777-0b82-37f3-9e82-eb9a1e2850f5 | -6.84674 | -59.15354 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 556e3fa4-0756-38f5-b580-ed4259b394fa | -8.37823 | -48.3338 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3730c44b-554f-3e93-a7cd-dfdb588a5dcc | -8.44599 | -45.09794 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ccca11c1-3bd3-3060-aabf-ca6dc0d536b2 | -8.87101 | -52.02565 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cd041c8-cfa8-3160-858a-a7afb0f25050 | -10.03674 | -46.09904 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a33ef4a2-21fa-3a78-9955-5edb3f62034c | -5.70534 | -45.16893 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ebc6b122-5b77-3792-b175-230d6393cf69 | -5.87126 | -46.11628 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82442f97-0a4e-31df-b681-65c950a4f980 | -9.98308 | -51.62207 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 679d829e-c6a3-3f1e-b185-064e6abd11ae | -8.53324 | -51.31739 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cabea5cd-4ed1-326a-98a8-59fef7bf9c1a | -5.00043 | -56.25433 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 7d86bff6-ba7c-386a-9035-e98c8b278e5b | -9.47267 | -47.60532 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9de5805-bdfb-3372-a2b2-e5e2acfab929 | -8.89592 | -45.798 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f51d5f37-3cea-3294-b0c6-1ca0e7e0558f | -7.6049 | -46.21715 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6516e80-6642-345f-94f9-df3068eb978b | -6.67746 | -48.39526 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cad90260-ef1a-3a08-b550-10b8fd1f5383 | -7.64113 | -46.55951 | 2025-09-04 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b7725f2-1cec-3d7d-952e-6e1b9f6a68fd | -10.30844 | -46.35953 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84094275-ea15-3cb9-bc90-14e589903110 | -6.26563 | -43.28166 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aeeb1b87-e694-3376-ad50-53957c119ce8 | -8.00473 | -50.09785 | 2025-09-04 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e03c9c02-e48e-3395-b852-88db303c86e3 | -3.43607 | -59.56979 | 2025-09-04 04:53:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 883f067a-d5f1-35fb-b083-2fefad6f99df | -10.44684 | -50.3899 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21d7fc01-897d-335a-bc50-58e88df4ac81 | -5.8877 | -51.95053 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7aa1349f-35a2-3dcb-9d40-7c18081cb82a | -8.08268 | -45.35388 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 899420c1-5293-35f4-ab89-8aff5e890bb9 | -6.69462 | -48.41178 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28b5bffb-3a04-3537-9c3c-2049d5de1c77 | -9.6055 | -47.04784 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2f28eff7-f5ec-3e4a-9256-7253fe125df9 | -6.88545 | -59.08804 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 278844c1-4f73-33c3-bd56-6cd2a4abb2c3 | -11.24815 | -44.96028 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eea82031-5544-3970-aaa6-43c6cf447a07 | -6.25707 | -43.29375 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1da5d5d5-2672-390f-9d61-5ef8c00a3b9f | -5.53928 | -46.43 | 2025-09-04 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20da1fa8-ce70-3921-9224-ad5bc6e3ca3c | -6.50441 | -43.09436 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7799c4dd-d17b-36d1-8c9d-843a5a008e74 | -6.87396 | -45.19475 | 2025-09-04 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd8d84f3-9053-3302-b5c7-0cf9ea438520 | -6.22461 | -43.54005 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a515b27-9f2a-3a6c-a0b9-d0bdbe27786b | -9.04416 | -47.00789 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 045c6588-627e-3917-ace4-4cc3e6f8bc7a | -5.69154 | -45.9387 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5eb8af89-9e4a-3998-910f-c72132dd2fbd | -7.97452 | -46.34438 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 42039660-bdd4-3dd9-92db-1e81618fae5b | -9.58477 | -46.68734 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd4ed0f4-2c06-3308-9423-91484e207aa6 | -6.78283 | -44.09175 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c6da2bd5-b560-33a1-8cd9-a60140082487 | -9.70071 | -51.04639 | 2025-09-04 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06249ad9-6f78-3ee8-9701-6d41eddd8986 | -9.70168 | -48.99395 | 2025-09-04 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a9e7faf-eb3d-38b7-bb63-590d34d87ea0 | -5.31164 | -55.8572 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7869d94d-689a-3742-b998-6e9bb17da85c | -6.17678 | -43.31709 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 044846ba-dff4-3742-850a-95f95094cf1f | -6.73913 | -58.732 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 80a5e83d-5180-30a7-947f-485dce358d31 | -6.24477 | -43.55078 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 290e234c-1fab-355d-b9a1-57c3fa316a70 | -9.958 | -51.64863 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d9d35df-b6c3-302b-9109-837825f78f31 | -8.91016 | -45.8703 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| add9d8a8-8ad7-3f98-8f81-814f22e04406 | -7.70069 | -50.25114 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f326466-b722-340f-bf19-91b4f73fb58c | -6.85082 | -44.27745 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45afd58f-a022-3a60-9fb6-4f4c6831d447 | -5.90966 | -45.94485 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb065549-20a6-3a00-90a1-f9d65592f93f | -5.48723 | -45.22696 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1246610-151e-3752-9c7e-9b5f160f2f03 | -11.23741 | -44.9618 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b34ae2ba-a29f-3281-b7ae-a8b05bd08641 | -9.58414 | -46.69181 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4caf7d04-d293-3782-bc23-0129a9feee48 | -6.89391 | -45.55836 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8048dcb6-a19e-3c6c-82e8-d123e1873510 | -6.84138 | -46.40099 | 2025-09-04 04:53:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b6df187-3990-31c5-860c-279e263ffc23 | -6.68397 | -48.41701 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e90004c9-cc1e-3814-aa29-934c67e6444b | -6.78062 | -63.13263 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c64be63a-137c-3300-bc3a-3ec77e2d260f | -6.66542 | -60.03018 | 2025-09-04 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52d963da-e285-3903-8c80-2f7fcd453bbb | -10.05482 | -46.0713 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8fd18ce-cff9-3c9b-8dc6-982eb8392a6d | -6.78241 | -44.09486 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 04425305-11f7-3a38-8376-7e29de2884c1 | -6.1763 | -43.32056 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 634a8ae2-985c-3721-aa0f-e74ecacbc6de | -10.14321 | -46.24348 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21d170da-bc6c-316d-b6fc-95985d20a2b9 | -6.84304 | -59.14837 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5664bef3-81ea-387b-b96c-b11ec5728c48 | -10.43548 | -50.36678 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7b0c6bf-5633-3a51-9f5a-057c0458be02 | -5.61244 | -57.34789 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c026c9f-caa5-3797-a78b-43dba7682c11 | -7.71824 | -50.32584 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a9b5cba-d167-3dfa-b9c2-7bd0aad2fee6 | -11.09421 | -45.12299 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cf933b2-e471-368a-95fe-6590887157c4 | -6.74277 | -58.73689 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| a1a4e5b4-069f-3000-9715-56dd6a26795c | -6.75264 | -45.91982 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99534016-f0eb-327d-8176-4f211f7fa27e | -5.30234 | -55.97147 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b50f8604-4513-3d63-a958-7a713458d903 | -7.70504 | -50.29306 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5552d4ff-3d64-378d-9853-20a6aa548809 | -6.32835 | -45.66177 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff74136a-c716-3ec0-801e-35695e5b5128 | -11.05774 | -45.39899 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 598647d1-6d16-3d90-a6f0-69bccc3c9ff1 | -7.71995 | -50.75986 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d51eaa0e-fd67-3439-9fee-fada1870cd9e | -5.93541 | -51.96861 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03b17edd-215c-352f-af4f-ec6d82a0746a | -9.43019 | -48.09559 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc95574b-6e3c-351b-a2f4-efd5996637ab | -9.97623 | -51.62108 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83066d91-efe4-37da-857d-49131174c3ea | -9.32982 | -55.21828 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9f1ffc3-0226-3b53-81fb-6b4d51405fc6 | -7.70531 | -50.29201 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdd00b2d-9f1f-38ec-94fa-7bfddfdfc067 | -5.72964 | -45.36164 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fc02ab0-bdd0-3058-9619-8abb3a21e8d8 | -6.32486 | -45.68544 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4b38e5a5-e2e6-31be-82cd-908b2696e575 | -9.72594 | -48.31835 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61925194-b3fa-3dd0-a89d-92adedd80f3b | -10.99415 | -45.91225 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README57.md)
