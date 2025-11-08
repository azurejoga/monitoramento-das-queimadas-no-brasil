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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 418d6e58-54e5-3763-80ff-7b44436bbfea | -3.0499 | -50.25774 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1365b2bf-b7d4-3948-a3f0-e2714084cb72 | -4.28609 | -45.89078 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3752d07-8a49-317d-94b5-cd0a64f4c8cc | -6.85363 | -39.11993 | 2025-11-08 04:06:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0f92789d-ba43-37a2-b60e-f7b355337bfe | -3.45785 | -48.83915 | 2025-11-08 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 43c70f0e-582f-3b0e-ae56-48988e27430f | -6.1109 | -41.56538 | 2025-11-08 04:06:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 30ebf3a7-5f33-3d98-bafa-98e5b85c07fd | -6.70143 | -39.6827 | 2025-11-08 04:06:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a0c845ff-0174-318a-bd2d-1770f0f27815 | -5.22695 | -42.79856 | 2025-11-08 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9909e52-a100-331d-9b46-e4eaa2995251 | -5.61603 | -41.07745 | 2025-11-08 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8d2f82bf-0740-3bc7-bab3-d89fc8e1f23f | -3.34725 | -50.20586 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 13b4fb87-616a-361f-8ed7-8fe3d3af989e | -5.44231 | -44.65659 | 2025-11-08 04:06:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2ac5fa13-6939-3ac0-ba8a-d6997483782e | -3.34832 | -50.20438 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b7929f94-a2cc-314d-9b4f-58b925a9436a | -4.40541 | -42.32452 | 2025-11-08 04:06:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef02df92-3fe0-3858-b82a-c187f9ed8b1d | -6.58784 | -43.75605 | 2025-11-08 04:06:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 152f5d0e-9737-34d5-bb02-1838b7de3e99 | -5.62922 | -41.0795 | 2025-11-08 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 17e264e7-0aa1-3d1a-93f8-d58faefaa316 | -5.0113 | -44.60727 | 2025-11-08 04:06:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da539db2-28e2-301d-920b-c1c8ba42cd74 | -4.89889 | -45.63087 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 700f1d57-3b7c-3103-ba61-d62fce036b23 | -5.76238 | -40.79331 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5185c5ae-90c5-335d-868c-30d34e867591 | -6.26949 | -43.6819 | 2025-11-08 04:06:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 288a7504-aee1-3ed1-9b67-8931b749fd93 | -4.10014 | -45.00626 | 2025-11-08 04:06:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1b37576-af9b-3252-be6b-c5aa54959eae | -4.32568 | -45.98462 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5603bbe1-ace3-3615-8293-647b9090a645 | -3.34119 | -50.20856 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 60aa1ee3-6662-3f44-906b-cab8bdac8b8c | -5.70287 | -47.75093 | 2025-11-08 04:06:00 | NOAA-21 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 322e3051-0e0e-3f87-9eff-81a6bcadb773 | -7.58612 | -42.30969 | 2025-11-08 04:06:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9cae99f2-5718-3b80-ad6f-b4648aab8e9e | -4.40877 | -42.32505 | 2025-11-08 04:06:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca9d2200-0cc9-3e10-acc7-54b538806be2 | -4.02928 | -49.27303 | 2025-11-08 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 210b2d06-2476-3949-a480-86862c5f8edd | -3.98385 | -46.03164 | 2025-11-08 04:06:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a30b1685-a0e6-316b-8f77-b0cd15855793 | -4.63356 | -45.89487 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2708d62a-fb42-39bf-9785-fe2f420f9092 | -6.85476 | -46.27023 | 2025-11-08 04:06:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc2f1be8-327c-30b1-8dad-3198fd614c24 | -5.91291 | -44.52928 | 2025-11-08 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fdea7aac-ac55-3a40-a150-762e867aa284 | -3.84339 | -49.90903 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28a064c8-3ce5-3d5d-94c2-11d93fe16320 | -4.46835 | -45.5061 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3699d7be-83a3-36fc-8d4d-8148ea1553b0 | -4.81328 | -45.66115 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eaf8156-af7e-32ad-9866-04f4bce813ee | -4.33484 | -45.53334 | 2025-11-08 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 847455ef-0816-3481-9636-af18563609b5 | -3.2505 | -50.13914 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed61775c-a7a1-3a8a-b54c-f3b63beca813 | -4.44731 | -46.43785 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a48e5a9-b55f-3a37-b5e2-d66c0eb400fe | -3.17105 | -49.24108 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2059d3b4-aec0-3a5b-bac8-5316c475ea9f | -4.59434 | -45.99937 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| c8442332-ef43-3a1b-bfda-3a61c3b268c4 | -5.47399 | -44.59963 | 2025-11-08 04:06:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a40157ab-3bd3-31c3-b665-801953f0d516 | -4.82931 | -47.79014 | 2025-11-08 04:06:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 609b914f-bd1d-30da-985c-41dcf28b9eb4 | -6.702 | -39.67895 | 2025-11-08 04:06:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 406b7632-b529-3497-aef4-5b0165f36bb7 | -3.78037 | -45.8458 | 2025-11-08 04:06:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e09f18b0-123e-3e9b-8d06-08a8fbe32157 | -4.68315 | -42.09167 | 2025-11-08 04:06:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8345e157-ff61-3355-8158-a5614086cc3f | -7.1427 | -39.4311 | 2025-11-08 04:06:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dec54104-b153-32b8-986e-e6e8bcfb5882 | -6.82359 | -46.77696 | 2025-11-08 04:06:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9104adc-914d-32e6-9de0-7bc6445be39c | -3.35196 | -50.21592 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 82f9a987-8ae6-3e0c-b3dc-a7edaf6f97df | -5.39637 | -44.24236 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a62e554-d2ee-3d39-ae08-62a16f835069 | -6.10345 | -41.69868 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 73f1ec1f-033e-3717-ac7a-7f777e5a0fce | -7.24066 | -41.91186 | 2025-11-08 04:06:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 18aa70d9-b661-3189-b719-15cc19edf561 | -6.08917 | -41.72485 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 594c922c-1666-3ccb-859a-825bd713f342 | -3.59502 | -51.2354 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6acc4f17-1e07-315c-b75d-938ad64d8b9a | -6.73507 | -44.15218 | 2025-11-08 04:06:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 390df984-e50b-3a53-9a4e-86dfbbe2b5b8 | -4.4755 | -45.33364 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 025bc194-6df6-3e91-a39e-c214bc563be5 | -5.72503 | -43.52673 | 2025-11-08 04:06:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e587a7cb-d218-33ec-9f8f-10892cc1b0e0 | -2.79125 | -50.3158 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf080de8-a140-3356-adc7-a2fee307e27a | -3.85779 | -45.22764 | 2025-11-08 04:06:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2eceb8d-bdbe-3a0d-9e55-ab8214a5304c | -4.6938 | -39.41162 | 2025-11-08 04:06:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0ba60629-90fc-3475-9b65-d383b8ad7e1f | -4.9152 | -43.01025 | 2025-11-08 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b946fbab-2a17-35e7-9a2f-8654bcbabaaa | -6.09356 | -41.71844 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce43334b-73f0-3279-b26d-a6cf6b1f32dc | -4.44668 | -46.44162 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98c5f987-3723-3211-a5d7-47e0a9967b3a | -3.63852 | -44.23251 | 2025-11-08 04:06:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddce46ab-760c-3ade-b271-8dc6a1927ab5 | -5.22727 | -43.5363 | 2025-11-08 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89d4e15f-81bb-3ce3-a31b-721fd3c157e3 | -5.15483 | -41.24073 | 2025-11-08 04:06:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 25fd3d1f-d602-30b8-bd9d-fa2a69ffa02d | -3.13072 | -49.1035 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac537739-6dbf-3872-8a45-3d33745747f4 | -4.30303 | -42.32646 | 2025-11-08 04:06:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9c55c4db-8e76-3e90-911e-4857836bbf46 | -2.97593 | -48.70681 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aaf21374-f8f3-369a-b4dd-f74e0b69183a | -5.6534 | -43.00813 | 2025-11-08 04:06:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b8d160da-6f4c-3246-beda-f698e8c77246 | -6.31908 | -41.94931 | 2025-11-08 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d41def2e-4a51-36c4-a584-8cb5bec83e25 | -5.63252 | -46.24484 | 2025-11-08 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3821fca6-64be-3a45-bd77-a2eb1a9fceb1 | -3.93569 | -45.4141 | 2025-11-08 04:06:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e1d9532-a2b6-3f9f-a453-b4e869786c05 | -3.58714 | -51.24667 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| acec4eaa-5b0d-3681-acab-9aa972eb40d8 | -3.32114 | -49.13194 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b38c9953-80b1-3c64-b749-dbef75136747 | -3.25719 | -50.14024 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90aca3c1-d1bc-3fae-a397-3f74e8acd3a8 | -3.42586 | -50.04441 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c002fa40-6f95-3696-8b66-38df1577fdf2 | -4.46856 | -45.32743 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ab38cd22-2b20-34fd-bd2f-1882e920c30d | -3.8394 | -49.82783 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d077a5c3-4cf2-36ec-8083-e791357b6a15 | -3.34708 | -50.21157 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c5a2ac5d-4737-391a-b646-9f62571c6741 | -3.52783 | -47.54315 | 2025-11-08 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b113dc01-a1b6-39a4-bcf3-e690a3d1dcac | -4.33349 | -44.71699 | 2025-11-08 04:06:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdf93c85-3dd2-3067-a617-26347a2f734f | -5.79325 | -43.73572 | 2025-11-08 04:06:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8be18f22-4578-3fb4-bcd1-c968d7a094b4 | -5.93243 | -38.17808 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c1c9f356-803f-30b8-b15b-e3bb7467d7f1 | -6.47207 | -43.22782 | 2025-11-08 04:06:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17e91a30-a158-38fb-aef5-dbcc7d41e71f | -6.6417 | -44.55011 | 2025-11-08 04:06:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f866f805-bdf4-3081-9da5-2be81c74f9b4 | -3.52728 | -51.56667 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 211f371b-3234-3101-bfa7-2769a63c9fcb | -3.47134 | -48.97566 | 2025-11-08 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e05217f-1576-3191-82af-72def4f8de67 | -4.23182 | -46.89586 | 2025-11-08 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30b8a866-3e3b-3ccf-83f4-61e04b53bd86 | -4.64318 | -47.94796 | 2025-11-08 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d6a34dbe-c262-385d-87b8-a49f8fbf61bd | -2.98063 | -52.82423 | 2025-11-08 04:06:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a702389e-6773-3992-88ef-4b266e1adb97 | -3.33625 | -50.10291 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 859dc700-51e0-3fd2-84c7-b9bd011922f5 | -4.67905 | -46.40192 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5af4659-ad93-3051-b1a6-2445df511c27 | -3.7685 | -44.28776 | 2025-11-08 04:06:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdad76ef-9035-388d-a029-aac05d8fbb88 | -4.33543 | -45.72499 | 2025-11-08 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60fa9df0-12a9-3e5e-bdc9-adef996d49fb | -3.40444 | -50.27209 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cfef846-968a-3e6e-9049-9ff4f2bfe5cc | -4.52511 | -45.60208 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c38ea32-6a5b-3bed-af15-3f2de55f9b8c | -4.617 | -46.59481 | 2025-11-08 04:06:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b8e18dc-2306-341f-800a-779724d7d8cf | -4.63698 | -45.89903 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1780d468-8e91-3468-aa08-63b60598edc3 | -6.89699 | -39.61489 | 2025-11-08 04:06:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c88314a7-8e2a-3709-b80f-d52200dd5fb1 | -6.66267 | -38.35197 | 2025-11-08 04:06:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2afa08f5-4e80-314a-9b97-ae6c78ba9184 | -4.62117 | -46.59563 | 2025-11-08 04:06:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df3b6987-36bf-3d25-ba4c-b9934638e4c9 | -5.74264 | -46.44057 | 2025-11-08 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 264874f7-abe8-3ee1-9379-099e210e0be8 | -6.09354 | -41.69713 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
