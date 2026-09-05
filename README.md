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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5211824-1ea4-3dc7-9fc1-c1c8fdeaa021 | -5.7758 | -45.0599 | 2026-09-05 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 859c2607-1db2-39d9-9e06-196103c89262 | -17.1078 | -56.8304 | 2026-09-05 00:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 2b054a54-128d-300e-a2ed-95ef47c08c5c | -3.7645 | -61.7737 | 2026-09-05 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 89308cb6-a411-3ffa-8745-1e6e7c2a47a5 | -3.1462 | -60.6317 | 2026-09-05 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 00e53d50-3c54-3366-864c-247b32045928 | -20.2498 | -51.2127 | 2026-09-05 00:00:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 126.4 |
| 8023881f-a9ff-3449-9a6b-df6159996147 | -9.1257 | -67.8137 | 2026-09-05 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| aeb3ed1a-f64b-34eb-8f1c-896365a93f16 | -5.7571 | -45.0613 | 2026-09-05 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2a899c77-d636-3250-99bf-64c05793dee7 | -3.1462 | -60.6506 | 2026-09-05 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5da03d1c-06f5-378c-99fe-9f86ef20bdbe | -13.4259 | -43.8401 | 2026-09-05 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 411eb60f-2440-3950-8d2b-8ebda2817a63 | -19.8254 | -49.5921 | 2026-09-05 00:00:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| 6e886ae5-8e20-3782-8784-1dbb9b14e2b4 | -17.513 | -40.2464 | 2026-09-05 00:00:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 138.2 |
| 88066f57-04af-3d29-adc3-b9579956133f | -13.4264 | -43.8163 | 2026-09-05 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 208.3 |
| c818d1e1-8fe5-350e-b65b-f9f3bc4a4f75 | -1.1832 | -53.818 | 2026-09-05 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 15f8d4e6-afaf-3120-9265-a3f72171d860 | -3.7645 | -61.7548 | 2026-09-05 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d4e260b7-1e01-396c-8467-04c5662e14cb | -3.128 | -60.632 | 2026-09-05 00:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 7874afbb-e2b6-3813-89ad-3ce74374e8bc | -2.7981 | -48.6873 | 2026-09-05 00:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 63af4a1b-f25e-310f-a5c0-4a5cef9aeec3 | -13.4458 | -43.8128 | 2026-09-05 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 305.9 |
| 720885b2-6e9e-37f6-b9b8-a8faa6bd418f | -3.7828 | -61.7545 | 2026-09-05 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| bdd53472-a3c1-3742-9a59-011bb6c0af5b | -5.7756 | -45.0826 | 2026-09-05 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 94df9ea4-ae95-390b-8e18-e82e79381f5e | -20.2295 | -51.2167 | 2026-09-05 00:00:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 93.9 |
| 7bbfb673-f8d5-3f74-b4c5-e9fdc7240933 | -13.4453 | -43.8366 | 2026-09-05 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 6a026c13-854d-36a1-96bf-093b6f2e7ceb | -3.7827 | -61.7733 | 2026-09-05 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 9def3ae2-8ae5-3703-b489-3cb4f7047c1e | -7.6968 | -44.3247 | 2026-09-05 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 812ea2d1-17a5-3090-97e7-e499176fd747 | -17.5123 | -40.2724 | 2026-09-05 00:00:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| 82b8955f-6ae1-36c5-8387-ee21a625693e | -13.4463 | -43.789 | 2026-09-05 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 05c002fd-77b5-317d-9517-5fc63b11f86a | -2.7668 | -47.7686 | 2026-09-05 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 468d921d-521c-3b08-aabc-fb7f17b04998 | -17.941799 | -42.625801 | 2026-09-05 00:08:00 | METOP-B | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9767f956-0644-3516-9f5a-eebd02268fcf | -20.4814 | -47.529701 | 2026-09-05 00:08:00 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c0333a4b-87d4-3b2e-b147-c5fad14f1ef8 | -13.3148 | -44.031601 | 2026-09-05 00:08:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0dddb356-f1a1-3956-a726-2eb5e0c11e76 | 2.3741 | -50.765999 | 2026-09-05 00:08:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 16b67e33-87c4-346c-bf2e-16cc21b44d24 | -13.4256 | -43.8032 | 2026-09-05 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac353519-28c8-376f-af88-e7e20998bc58 | -3.7899 | -55.862301 | 2026-09-05 00:08:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5801edef-5382-39ca-8d9f-d39a899c1a1c | -7.664 | -44.317402 | 2026-09-05 00:08:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33ef39ac-ac89-389a-9c27-6cc6699aa209 | -2.8074 | -48.6703 | 2026-09-05 00:08:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9af3519-6d57-3824-b665-e18246b764ea | -3.4394 | -52.799 | 2026-09-05 00:08:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdedddf9-3f9f-3594-bac4-6d857ff45ea6 | -14.7437 | -47.140301 | 2026-09-05 00:08:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7c8b9d69-c47e-30e1-a439-793506a66d27 | -3.5852 | -51.4734 | 2026-09-05 00:08:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b91f32-040f-30df-9ac7-9b23cdcaf66f | -18.5886 | -46.416901 | 2026-09-05 00:08:00 | METOP-B | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ba736453-a463-348b-ba89-e98d8a7b6601 | -12.9148 | -42.419201 | 2026-09-05 00:08:00 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 747d5fca-9cba-38eb-a86a-26d359b0e720 | -7.6709 | -46.059799 | 2026-09-05 00:08:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79539a9c-1547-3484-a302-7addb2fe13ac | -1.9529 | -48.220299 | 2026-09-05 00:08:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d49be1f9-12b2-3863-8f02-001719805b3b | -21.5819 | -48.658501 | 2026-09-05 00:08:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 36a4ce7b-d2bc-372a-9f7d-cdf880283f25 | -13.4354 | -43.8008 | 2026-09-05 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52222eb7-0f88-3b0c-b95d-fd4379f16a1e | -20.2318 | -51.203602 | 2026-09-05 00:08:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a5705a0-c311-3201-b26c-ade267cbff7d | -20.943701 | -48.890499 | 2026-09-05 00:08:00 | METOP-B | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a5886296-bd65-3653-b6e6-49ce9bb316dd | -3.4412 | -52.806999 | 2026-09-05 00:08:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd563634-f307-36e0-8d06-800b35330213 | -15.0772 | -52.512501 | 2026-09-05 00:08:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1bf628b-5dde-3e7b-84c3-5aec8607c34e | -13.5589 | -44.1022 | 2026-09-05 00:08:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc9b37f2-ea52-3b8c-a648-feedb0888d32 | -3.5832 | -59.3871 | 2026-09-05 00:08:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e929da26-2010-33e5-af5b-0c271ee73e11 | -10.9385 | -45.339901 | 2026-09-05 00:08:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dbd550c3-b8ed-38ef-89e3-cab510468db7 | -7.6746 | -46.076 | 2026-09-05 00:08:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b947143d-a8b8-3fdb-acd1-eb679bdd4158 | -2.7557 | -54.662399 | 2026-09-05 00:08:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbcd410-b07d-3540-909d-da8d9553ef59 | -20.256701 | -46.328201 | 2026-09-05 00:08:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 65124e33-1d48-34a7-936d-6705154ef68d | -20.249201 | -51.188599 | 2026-09-05 00:08:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e158774-7f6c-35bc-a555-0abf2e22564b | -2.8232 | -46.7108 | 2026-09-05 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50ee9198-625d-3e9f-b6f7-95a1c90fff07 | -13.4278 | -43.812302 | 2026-09-05 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a3d4103-b174-3997-af48-bc9f18f3eebc | -13.4419 | -43.828201 | 2026-09-05 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 346c93b2-ea1a-3fea-bfdd-7bd8299432fd | -5.8506 | -52.039902 | 2026-09-05 00:08:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 701c99aa-8424-3e0d-8a9a-2837526ab676 | -19.815901 | -49.584301 | 2026-09-05 00:08:00 | METOP-B | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b52e6fab-9809-3255-848c-9f6077ca7068 | -18.899799 | -47.043301 | 2026-09-05 00:08:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 26ca342e-dc4f-364b-a89f-f00ea0840dab | -20.253401 | -51.2104 | 2026-09-05 00:08:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e10009d8-757a-3366-a4d0-2eaff17f898a | 0.7317 | -51.512199 | 2026-09-05 00:08:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ed0ddc11-4e75-30c6-87d3-efe78b96fcaa | -10.4784 | -46.067101 | 2026-09-05 00:08:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2eae8e4a-8b19-3560-95dc-94d93479d36e | -17.6068 | -48.248798 | 2026-09-05 00:08:00 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d9fb70f3-017a-3c38-af19-4ce6f1b3ff0c | -2.7615 | -49.4659 | 2026-09-05 00:08:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20518e2a-894d-3bbe-94a3-b36b899d6dde | -3.6897 | -51.986 | 2026-09-05 00:08:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26305032-d830-3edc-9542-892070380df8 | -7.698 | -44.330601 | 2026-09-05 00:08:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d6439f93-882b-3bff-9ba9-aaa929184746 | -17.513 | -40.231998 | 2026-09-05 00:08:00 | METOP-B | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b9683b0-f9f1-3949-8753-a604816eb9e8 | -20.258301 | -46.335499 | 2026-09-05 00:08:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a8175a3c-67d9-36f0-a771-7619bc93007a | -2.763 | -49.472801 | 2026-09-05 00:08:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a87be461-559a-3513-a635-1f622c9da001 | -11.8043 | -44.806499 | 2026-09-05 00:08:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c915caf5-5ff6-3575-ae43-6d533a6ad5f0 | -7.6956 | -44.320599 | 2026-09-05 00:08:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5fcd3b2c-0a52-3b84-a86c-ffdc3d36bade | -18.9014 | -47.050598 | 2026-09-05 00:08:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1c609430-3385-3a11-a625-4d110ab9d17c | 2.3854 | -50.761299 | 2026-09-05 00:08:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 90dd52f9-f8c1-310d-b2ba-a97312b7a01d | -2.4557 | -47.579498 | 2026-09-05 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb1421ba-5941-39ab-a277-4e2acd95647f | -20.251301 | -51.199501 | 2026-09-05 00:08:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71139de6-42eb-3756-8ee6-adaef3bb29f9 | -20.8277 | -46.305698 | 2026-09-05 00:08:00 | METOP-B | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d0c99b30-c238-343b-9852-a09714c68926 | -3.4338 | -43.271999 | 2026-09-05 00:08:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71840282-4824-302c-b939-72b44134ae3f | -11.814 | -44.8041 | 2026-09-05 00:08:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| afc7a4b8-6950-3d6a-b477-13346b563e64 | -19.2623 | -46.865501 | 2026-09-05 00:08:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 70df006a-27cb-3a28-916e-fe004cd17cde | -5.9278 | -47.8918 | 2026-09-05 00:08:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59c8da9e-b04f-386f-b986-735c1dc5d5d8 | -1.1817 | -53.827801 | 2026-09-05 00:08:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00291411-8547-3d0d-ad79-2c211c058552 | -7.1263 | -42.2472 | 2026-09-05 00:08:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0d81df19-1c03-3c6f-8b14-abaed4854585 | -13.4398 | -43.819099 | 2026-09-05 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 494c6a89-9285-3d4a-8bc5-59564f3b3f54 | -19.817699 | -49.593102 | 2026-09-05 00:08:00 | METOP-B | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b85674e-f89b-3687-8890-1122a1922b7d | -1.1896 | -53.8172 | 2026-09-05 00:08:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c667ed9d-721c-337c-b4c5-8601eb53f1ca | -2.4539 | -47.571701 | 2026-09-05 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd01ed6-bd48-3b0b-acd2-e9a817df6870 | 0.7332 | -51.505402 | 2026-09-05 00:08:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| de9bf4a8-6c80-3108-a5cf-36ab30680771 | -4.2761 | -54.768002 | 2026-09-05 00:08:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81ab3d9d-ddd4-3b59-aac1-d1b440f2d9cd | -17.5261 | -50.030602 | 2026-09-05 00:08:00 | METOP-B | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f8559a07-79d8-3761-a8f9-962f0ee7f9b7 | -17.9396 | -42.616402 | 2026-09-05 00:08:00 | METOP-B | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff132225-aa19-36e4-abe2-593b089a06e7 | -3.6214 | -54.5882 | 2026-09-05 00:08:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca57520-40c6-349b-9c8b-00ebbf62f826 | -20.2395 | -51.190701 | 2026-09-05 00:08:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b686a61-2f5c-3907-9d46-6a1dcacb8d76 | -5.7588 | -45.067799 | 2026-09-05 00:08:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 355a0a0e-89aa-30ab-bafc-a937ac066d24 | 0.1812 | -51.440498 | 2026-09-05 00:08:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fe4ac1d0-dc8a-3046-97fa-afa53b1ebd8b | -17.5163 | -40.245098 | 2026-09-05 00:08:00 | METOP-B | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f8a5617-bc54-3820-ad9f-ad613b517739 | -20.1747 | -47.387402 | 2026-09-05 00:08:00 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2c3d9d09-f357-3bdc-9a24-4e398797a227 | -2.809 | -48.677399 | 2026-09-05 00:08:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e70e8755-0b02-3c70-9786-2ce265dc1b79 | -13.43 | -43.821499 | 2026-09-05 00:08:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 071cbf3b-bb54-30ec-bf04-6361ca5d0c37 | -7.669 | -46.051701 | 2026-09-05 00:08:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
