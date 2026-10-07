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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8920a7e3-9684-3b32-a8fc-4568e1368bcd | -3.0454 | -53.9226 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db6d22a4-25aa-367f-8b29-b5c726eb5be1 | -2.9327 | -54.144798 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6c1e94-a6cf-37bf-b1b9-3035a9b6de63 | -3.2839 | -54.063599 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 559794f5-b642-394c-8e97-a3dccc8ad8c0 | -3.9988 | -56.254101 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f31bf83b-4402-3eb5-ad1e-7f7197934de2 | -3.5457 | -59.457901 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91a9776f-8453-3dee-a1e7-33f07861e9f9 | 3.2201 | -61.0401 | 2026-10-07 00:47:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc9fac4-511d-3b6c-9385-051a8406778d | -2.4673 | -58.069801 | 2026-10-07 00:47:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2094b4f4-71a6-30c3-8aa3-036d1e8953de | -5.2338 | -50.906898 | 2026-10-07 00:47:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6970f7e1-4abc-3856-94a9-fe10ed99a691 | -7.7445 | -49.195099 | 2026-10-07 00:47:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3a5a183b-8eb9-3ed5-99f7-86241314231a | -3.5359 | -59.459999 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e67857e4-83ec-3a11-b619-6ebf0b2e93cc | -3.2209 | -53.881901 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66ab3971-7976-3179-a25e-a42d53f2b7fe | -3.9728 | -59.340801 | 2026-10-07 00:47:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24725dea-ef51-36cb-b133-bee8d868e047 | -3.9911 | -56.265099 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29dc80e6-b938-3b4b-9394-3e78144fdfe1 | -3.2448 | -57.863201 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60ec2b30-abf7-3a8f-82b4-436650b46f37 | -3.0025 | -57.750301 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1abe81-0ac0-3528-bd76-913a9357d35c | 3.8541 | -59.684898 | 2026-10-07 00:47:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a8f2cc73-1be1-3261-a7b5-ab63bfdfc356 | -4.0797 | -54.871899 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d7b5683-a8c3-3f8a-bf63-d4a32a686677 | -3.3417 | -59.4674 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48a17cbc-5516-3f53-9581-2c7e3c2a104f | -6.5777 | -53.023499 | 2026-10-07 00:47:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67d575c8-123a-3b4e-b98f-a5905bc55411 | 1.7779 | -55.545101 | 2026-10-07 00:47:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57a58009-ee8c-3331-9763-664d3b930ba1 | -3.0386 | -53.937401 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 550ce950-687c-3e6a-9424-3819308e8b16 | -3.0626 | -54.216999 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05618fe9-c03e-31e3-9cad-a64bfb8a5a9e | -3.0433 | -53.869598 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2b989c9-e205-3cc3-8fe3-aa8e1a028d48 | -1.2894 | -54.546398 | 2026-10-07 00:47:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f88c18-5e49-3838-8fe0-a2bc8a3b6f3c | -4.3673 | -55.4431 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0033dd7e-4ce2-3fd8-8a62-c748a105ce72 | -5.971 | -55.380798 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f19bd59-1101-3886-8c0d-81e855f03e98 | -2.7868 | -51.685699 | 2026-10-07 00:47:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80320105-54ed-324a-bbf2-1fd908c31a18 | -3.6945 | -58.8866 | 2026-10-07 00:47:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d498fb0f-6e43-3b6c-b6b2-6a44d3e6997b | -3.5324 | -50.094501 | 2026-10-07 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b540ded-c447-3d51-a0af-47e2cf5f01b3 | -4.7582 | -55.6618 | 2026-10-07 00:47:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43505beb-ee21-3f69-b52e-1f7f34e3a5bd | -3.0766 | -54.276901 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91440fdf-505f-3aab-85a7-4ee87eb1f481 | -3.1102 | -53.7598 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b356710-ff35-3df7-af0c-8577235f3819 | -3.2851 | -54.024601 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc30719c-fdf6-393e-9df5-d80a55dc3d97 | -2.7771 | -51.688 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a98e9fe-08be-3262-9303-13ad02ff5572 | -4.0724 | -54.884602 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 911ae554-e126-3ab4-b1ed-9b8d923b29ba | -3.1661 | -50.441399 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbf0351b-9c2a-3ed6-8e4c-e0208177de83 | -3.5878 | -54.307999 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f622d0f8-11a9-3839-8006-6916251ea2ec | -4.9147 | -55.847198 | 2026-10-07 00:47:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d3c86e4-8967-384b-86ec-caacf2efbe1e | 0.4481 | -60.5327 | 2026-10-07 00:47:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c4575f21-2735-3608-9b84-409e28bf1746 | -3.1145 | -53.690399 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24ac6332-f03c-3cf3-9234-9e5afca668bc | -3.0297 | -53.899502 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f310818a-7556-3b29-92ed-0d5f71533cae | -3.5189 | -58.749001 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8efb8f0e-39cf-3b2b-ab20-7b4c085ce476 | -3.0586 | -54.243401 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 740819a0-f064-3552-9932-2c13a2270233 | -2.8714 | -54.146 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56c612c0-4f07-348d-8184-59ded2503612 | -2.9413 | -54.181301 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd52e899-39be-3ca3-9846-30469544243d | -3.1034 | -53.774899 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff0206b7-76bf-3726-8c4a-72d6bfff7c6d | -8.9673 | -65.423401 | 2026-10-07 00:47:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b952cc0e-59ca-3a3a-93e3-0cdd63ef8d63 | -3.5437 | -59.494301 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ddc2fd72-53b6-3d7e-b8b3-bfa53d96d87d | -3.483 | -57.777802 | 2026-10-07 00:47:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c810ea3a-b195-3df6-80ce-e495f0e8aec5 | -2.9494 | -54.127998 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fff1635-b2eb-3b29-b6c9-31c60286573d | -11.0545 | -45.8437 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3155ef6-e48e-3f5e-a82d-0c8df7086cf1 | -4.3867 | -59.894299 | 2026-10-07 00:47:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ab79ee9-891e-32d5-8a11-95b58e37a10e | -2.9201 | -54.134701 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd43f0e-79fa-377b-8ef1-60655f6d7ac1 | -3.6736 | -60.525902 | 2026-10-07 00:47:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82dd780a-f9a8-3ae7-8fc8-d53932aec16e | -3.5205 | -58.756001 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d17d3cc-f5f3-358f-bc9a-5cbf74445d15 | -8.272 | -50.2719 | 2026-10-07 00:47:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d771d85-f50d-3a37-b611-447e3f4e8dbf | -3.474 | -59.459499 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88dd1fb7-64a5-3c20-b9c2-a6d4ba0ccd82 | 3.1493 | -60.576599 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| df2941a3-0eda-383e-9dd1-35fab1071787 | -3.4018 | -58.008701 | 2026-10-07 00:47:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a683fde-90a2-3474-99b8-f0a7c431285e | -3.4087 | -58.8992 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6967ba5b-2629-3e0d-9d95-ad205434f67c | -3.0501 | -54.207298 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64f15324-f76f-3ff3-99f5-0ee1e875e0f6 | -3.2082 | -53.871601 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd695715-b6e5-3639-a9be-1527c590821f | -3.0327 | -53.912102 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c928bbd8-d0db-3f51-895c-67a832398101 | -2.601 | -57.5723 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5528fbd2-59ad-3115-a0d4-7ee07d08711d | -2.7899 | -57.676998 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d210cef7-8403-3e8f-866b-db4998747ec7 | -3.8564 | -55.994801 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b4b629-e2f7-3d60-9434-f3b6c1ce45a4 | -2.0118 | -56.8876 | 2026-10-07 00:47:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2be209c6-9497-38e5-bc70-2024cebd2a0c | -3.2793 | -53.999901 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d433ecbf-0dc3-3ea7-9c62-8857e3aafdf2 | -3.7369 | -59.436798 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 344f0730-5d91-3cdb-9c33-e702ce192446 | -2.7534 | -57.652699 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09a3180b-826f-3e30-9790-9be008994e89 | -12.4806 | -51.298401 | 2026-10-07 00:47:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ecdfa31-8e7a-3093-89b5-3693df8afe03 | -3.761 | -59.316002 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9643092-0025-3ff0-956b-7f6ad6f924aa | -9.1424 | -65.925797 | 2026-10-07 00:47:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b95a82e-64dc-3f0a-8300-f450ba9ec60a | -8.6792 | -68.679901 | 2026-10-07 00:47:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8608eca-c4b4-33ee-a753-4f6033a6397e | -3.1823 | -50.551899 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0569558-7ac7-3635-853c-f050e2ce4094 | 1.7753 | -55.556702 | 2026-10-07 00:47:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a10d02a-13b2-3756-a66b-dc16d6ef4313 | -3.5059 | -54.662399 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2971e59-d898-3a47-8e88-3d5c4118f96f | -2.4949 | -58.055698 | 2026-10-07 00:47:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4497c34f-a0d9-31ed-8e9d-fceada7beb07 | -3.3908 | -59.593201 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0bd108c6-3081-394b-bf32-96519056222a | -7.1855 | -55.106201 | 2026-10-07 00:47:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f867d37f-dec7-354b-9eb7-b870817f9bcc | -2.6001 | -59.379601 | 2026-10-07 00:47:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f773c10-eaec-3434-ad85-172e389207b2 | -2.033 | -55.634102 | 2026-10-07 00:47:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c79e7e4-14de-3235-a7b7-bae6d5e2aa50 | -3.2717 | -50.156898 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb314fa-0ce6-3527-a528-beb1c94b00f7 | -1.8037 | -57.104099 | 2026-10-07 00:47:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13f7007e-2317-30a4-b4a7-33f644fd49e7 | -3.3304 | -59.4627 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 626aaf79-620e-31e2-bcbc-537c48191075 | -2.9522 | -54.140301 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d7833e-0474-34a3-8313-1a81e4f193d9 | -3.5033 | -54.651299 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02ea0e39-6bf8-3518-ab5c-7326087604ce | -3.2959 | -53.8512 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77311b4c-f72a-3dfd-a61b-a8f41cd33c0a | -1.8018 | -57.095699 | 2026-10-07 00:47:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6bf652e-d551-311a-9fb3-ecfefb41b928 | -3.8964 | -59.3218 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b614aad4-be92-31a3-bfb1-aa12df619299 | -3.064 | -54.1786 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ebef961-9eb9-32fb-9dc0-815672bfdca4 | -2.873 | -54.197102 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5df7c1e0-389c-3aab-a59e-3dbb83bdb361 | -3.5754 | -54.298599 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a9da9b-cba6-3b93-b13a-505f398e3586 | -3.5851 | -54.296299 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa11efe-7fa0-3b34-a98b-ed73ab8a831d | -4.7462 | -55.6548 | 2026-10-07 00:47:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7eff6dc-4a56-3c8e-b8cf-9df258e321a4 | -2.9936 | -54.053001 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc716412-119a-3429-b8c1-8f33dcd7e790 | -2.9384 | -54.169201 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6a67d25-94af-3e3a-bca4-e73ca5940a7b | -8.9064 | -49.9706 | 2026-10-07 00:47:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4672e20-b600-3419-a3ca-f7b2162603e4 | -3.3464 | -59.487999 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 914e7dc0-fd0c-3bd8-87b9-27253345af34 | -2.4967 | -58.063202 | 2026-10-07 00:47:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
