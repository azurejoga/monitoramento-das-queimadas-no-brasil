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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb05b1f7-d510-3722-919a-758eadc6cbd0 | -5.23883 | -50.90794 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e578bb07-ddb1-3100-b220-9a278dfd44b7 | -5.95621 | -46.37969 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51c66aa5-c21d-32e2-8a4f-bf143abf3c65 | -3.84949 | -51.92985 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1a9bf37-2176-38a3-8746-bf2178201168 | -3.02876 | -54.2324 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f367a0c7-1846-3ecc-bc71-ececd4b5f2a1 | -3.52705 | -54.6317 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f615674-fc09-3320-bcf6-7f1d4f31b466 | -3.31754 | -54.05054 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3634ed2b-81c9-3260-94b1-0352a26ab598 | -8.71935 | -45.18154 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bde5480e-143a-39a4-91ab-3e3a65fedbd3 | -3.74685 | -59.44551 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a7aebcc-7be2-308d-95e4-8e6c3f1dd30a | -11.40133 | -46.69699 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 98d9ec44-cbcc-3527-9df3-2f1c5d252b5e | -3.47855 | -50.08631 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a0c0cd6-e96e-3c3f-bbc3-dc0b1baf20fa | -3.02009 | -53.89359 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5424d36d-103e-313d-abeb-caa6487097be | -7.22412 | -55.16536 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f48dfcc4-88bf-39e4-9948-bcfdd55406d3 | -3.0751 | -54.27625 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c7b4d1b-7fa8-3419-9064-8ec4b2cc4b19 | -6.98976 | -59.11311 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5571fd8-6eac-3b74-9d53-53c1d0f6ee6e | -3.05377 | -53.96469 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ae5b6e9-fc65-3463-8412-79e113e0f49a | -3.61069 | -54.59297 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 783a67a1-dc8a-3ce4-9b9d-010433dfc5a8 | -3.26328 | -54.03911 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 86fd5298-d04a-39d3-b59a-131f02bfff0e | -5.34242 | -50.98461 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39452a48-0dbd-3a0d-b2e8-83d124f3bb98 | -3.96081 | -56.11497 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36ebcbc4-07f5-32a5-a5b2-9bddc07d055d | -2.89068 | -54.16454 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62734e3d-3e30-320f-a652-d40e083d6424 | -6.27426 | -56.00339 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28007cde-2940-3e79-be20-10fd3ec983c1 | -8.7232 | -45.18651 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d1fd06da-cad6-37e2-9324-75897fa9f035 | -2.85765 | -59.11165 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c119d81-84cd-3a54-a1a2-d1243eb28143 | -2.49038 | -56.10326 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22bce516-2519-3f69-b239-ffcba18642d5 | -7.21638 | -55.09595 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd24ff34-927c-3b01-9b56-61c129e2ef26 | -3.07971 | -54.29523 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 457f381a-23cb-3393-a39d-23cdb56d6ed8 | -3.04226 | -53.91895 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35c2a2a7-9654-3f1a-a291-9fcfd34ba881 | -3.10564 | -54.27631 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fc25ce59-0de6-3a64-b029-3c14a207e9ef | -5.26147 | -45.40567 | 2026-10-08 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21f49944-81cd-3d83-9b09-e82dc8f0848e | -3.26803 | -54.00895 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc3b8ebd-d7d1-302e-8bf4-58efaa294376 | -3.03954 | -53.93604 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 859b97b0-4660-347f-9023-bb53cff2baea | -2.50656 | -56.13794 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 536d713d-4ea0-333d-aa66-b63af9461612 | -3.26925 | -54.04892 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a2cf5f06-e82a-360f-8186-5df5728eb4fb | -5.11482 | -47.11794 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50d66cf3-6e1f-3338-8ac4-baf81d6073a6 | -2.55126 | -56.29191 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6fb62a2-7ac4-3399-9673-c2d6926805a2 | -5.4885 | -42.85723 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5fecaf32-71d9-3e70-80ad-9ce71ccbc16f | -3.22845 | -54.30841 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a318afd5-096b-3c25-8f59-73168f9ad82b | -3.56011 | -59.49675 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff0534f0-3da1-31d8-a985-b0f47c27ffd2 | -5.38321 | -44.17327 | 2026-10-08 04:46:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54fd2b90-e35f-3f4d-81e6-2f1a000b5e23 | -4.33973 | -43.79964 | 2026-10-08 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| da140ee3-4461-3b1c-83e1-8a8e2b4382c9 | -3.28539 | -54.06324 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdd1e8da-091f-3902-849b-8f575044ee65 | -10.26614 | -48.94711 | 2026-10-08 04:46:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f77c2a17-b9c5-3424-b622-5ab134f5d8fd | -2.93962 | -54.16763 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5d75555-7a46-3e2d-8a18-ba6695920653 | -3.48185 | -50.08682 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8871a88b-f9a3-3a7f-a509-026cb6d73b7c | -5.70362 | -53.4972 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a5c25728-75d2-3d00-ac55-1e1b26e55fac | -3.08684 | -54.25056 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72dc3581-7ad4-30f4-8fe4-bbb0acd6d243 | -4.14557 | -54.03191 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1f2e03f-a55a-3ecc-8211-a00761cd025d | -7.35244 | -44.36922 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 845dce80-af12-34f0-b39d-525975998660 | -3.74206 | -59.47402 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96fd2314-74c4-381f-a01d-d398919669a5 | -5.81766 | -53.8276 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e456bf14-232c-315b-8903-b633bf40bbba | -3.83767 | -55.97694 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f1ce10d-5665-3042-a718-e18251a1f576 | -3.2127 | -53.88671 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a2f11fd-b7d8-3ccb-8944-f3abd01659f2 | -3.30221 | -54.69991 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9c90a23-9040-3d66-9a87-192192008550 | -3.87884 | -55.82476 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b93ec564-49a3-3c23-ae44-20eafda6799d | -8.71812 | -45.19036 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 691b0548-bb71-3f01-b40d-f3a58230ba66 | -6.98692 | -59.10528 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfdf4ccf-5856-38d2-93c9-77187f8d8002 | -5.67859 | -53.49762 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 874035a1-ea34-39e3-96fa-b76b536764c4 | -3.61782 | -55.28274 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6881a64a-7465-3175-b6ed-6539567de1fc | -8.60322 | -45.63296 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36395ec6-373d-30b5-b824-d474cae36ce4 | -2.97895 | -54.03276 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3526483e-4b98-364a-b9ea-3e3fb4c11339 | -5.81709 | -53.82776 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ad44ec1-6dc2-32f5-81de-ac99083e6eb6 | -5.87598 | -45.96574 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae2bb8c0-fa2f-3fc3-835b-632d327f6ef9 | -3.05703 | -54.24619 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dd0a8a5-400e-301c-9e23-cc7e59b6841b | -3.53546 | -54.67551 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9b307b89-b2a9-39fd-993b-8258298640f0 | -2.98753 | -54.77329 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ff53bf6-2e6b-3bcc-9e5a-673986b88f63 | -3.51422 | -54.66272 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b31ca43e-22c2-3834-afbb-aaacb347ffe5 | -3.43502 | -50.43136 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c29ab1d-2800-3930-8ac0-acd4c1407373 | -3.04414 | -53.95438 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0730c97-23fd-3ffd-b87c-995d1a8dbc9d | -2.86874 | -54.20655 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb5c01fa-3601-3964-be65-afe01a8c36e3 | -2.7749 | -54.06607 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed29ed66-cf65-35fe-8f33-3ad8c14257a4 | -3.93133 | -54.57813 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde3e182-7292-3b48-9c94-c555dda5b9f8 | -11.31633 | -46.68617 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d54bc217-6c85-309e-b623-9bec1cbae944 | -3.27293 | -54.04945 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aafd1ba3-8687-3b26-b7e4-7a23cbab6f96 | -3.49782 | -59.28473 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11d361cb-856e-3520-924c-c784d9b8eb8f | -7.87913 | -54.99113 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cb868fe-f092-38bc-aaa1-37122cf17130 | -3.81288 | -47.49189 | 2026-10-08 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d8403ca-0ac0-3eca-89fb-f6f85f261274 | -3.08011 | -54.24494 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15e945c7-9a89-3dd8-9017-387952324cbe | -2.50233 | -56.13727 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9cbd3ab2-8550-30f2-91ea-5a57b1b757fe | -3.2477 | -57.86664 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f8fde49-b361-34dc-a307-88a7c720ff3d | -3.57933 | -54.6684 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d928027c-79d2-30df-a54e-84204ebf10b4 | -3.02011 | -54.1062 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 45ccc3a8-95a8-34b9-b874-6449bf681190 | -3.03818 | -53.94463 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f5ad040-57cd-3ea6-8df5-46dc271365ee | -10.24917 | -49.66926 | 2026-10-08 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a0098e5-90a7-3c52-b0ea-284193835295 | -2.50018 | -56.06873 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8fbe3778-deb7-32a2-88a0-51d7016be64d | -3.53237 | -54.64666 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59ce3257-d72e-3845-b561-458b020fe722 | -3.27795 | -54.04138 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9823bc10-d92c-386a-9492-cb913a5c01f6 | -10.46628 | -47.24046 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f5b9e74-2335-3b5a-8efe-826f45fa22c7 | -3.10412 | -54.1899 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0f404a9b-a9b0-3303-91ce-1939c5003b0b | -9.42946 | -48.84826 | 2026-10-08 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7010f9c5-b2c6-3875-a3b5-fe15e60dbba0 | -3.30459 | -51.11021 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4c56831-6ed4-31d3-8943-74a0f454f697 | -5.7356 | -45.14797 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b496337-70b5-3ba6-b6a1-f304ac4b189a | -7.16713 | -47.79282 | 2026-10-08 04:46:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64264095-a012-36bd-934f-1f52406b055f | -3.00287 | -54.2392 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5735696e-d623-3b7e-967c-5a4df6ff3e17 | -2.99266 | -54.08847 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e5fc9709-9fdf-31de-a1d0-0f903a76a10b | -2.97366 | -54.11248 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3975b56f-30f1-331e-aa35-ee61b2a3d994 | -2.99137 | -54.77392 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9095f97-0a38-33be-aed4-cb58d5e80398 | -11.86283 | -43.55947 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b29fdf45-67d1-3df5-9db3-e916705cd9d6 | -4.24657 | -50.7483 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73dbf665-9d9f-3dd0-ad3b-52c0e9f04751 | -9.80913 | -44.7794 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 298e44a8-c6ba-32b3-b59c-a9efbae5efdd | -3.95668 | -56.1143 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README103.md)
