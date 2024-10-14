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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 446d775b-616b-3576-ad6f-30cdfe56c784 | -7.83677 | -43.99553 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45095f47-5f02-34a7-a5fd-0eec3e5081da | -7.83399 | -43.99146 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00867adf-866e-38a3-9c85-334e373a2702 | -7.61793 | -44.06927 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2fca468-86af-327d-bd76-60f95617df82 | -7.60783 | -44.63798 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65166f44-ea8e-33de-94c4-1e13db426bbb | -7.60453 | -44.63746 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba363819-acf1-3ce9-919f-2a30b52eab80 | -7.60123 | -44.63694 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff6eb0a4-db45-3d34-9d7b-bcf521e28efa | -7.60069 | -44.6404 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92bcc8db-9aa6-39ed-9f83-768c47118c23 | -7.5995 | -44.01234 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aff41827-7bb2-3d1d-ae3a-53adacdc7e8c | -7.57085 | -44.78808 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fe088b5-2360-342d-898d-f320626eb640 | -6.65137 | -43.96431 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4826dd01-96b6-358e-97d1-12ee7e29b3e4 | -6.64908 | -43.93533 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c012c24-a0d1-3954-a4f2-3eef449b9ad5 | -6.61641 | -43.72957 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35e09281-8f82-3a6d-91bc-6549e6fffe26 | -7.31321 | -44.97758 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ac5a6b7-bda0-36ea-875d-fcfb793beb64 | -7.31267 | -44.98103 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bc4c279-a74d-30d5-890d-b68e3cad71c2 | -7.30937 | -44.98051 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 675d254f-1fe2-37cc-a5a8-dc5bea90a342 | -7.27129 | -44.95973 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01ca9545-659a-3456-85e8-72bffdfe6ba4 | -7.27074 | -44.96318 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2798bd1b-90a0-379c-8e4a-f13046cd33c4 | -7.26966 | -44.97009 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37173766-f4e3-3ffe-a47c-c8dd2f62b169 | -7.2669 | -44.96611 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd839f8b-788a-35da-a4dd-df3b48b84a26 | -7.26636 | -44.96957 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3119f697-8609-3a83-8f5e-3c38f0a15f54 | -7.2636 | -44.9656 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37ad400c-5a40-383e-aecd-523a89c293ef | -7.26085 | -44.96162 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 556f21b2-c9e8-3503-aa3f-219b841e07c0 | -7.2603 | -44.96508 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 223d4c8b-948a-3387-bf9b-bb7e2d80ea74 | -7.25976 | -44.96853 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e37a6d5-1634-3c16-92e3-c728d98d1038 | -7.25755 | -44.9611 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cf0bde58-34ab-3010-9273-c159491207b7 | -7.25701 | -44.96456 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a192f464-40c5-35c5-ad87-d7bb50b0f030 | -7.25425 | -44.96059 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dac5a932-2b9d-36ab-b9d2-a797a90b64b1 | -7.25416 | -44.91813 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cbd6c5a9-8bb0-363d-9abd-f214837f5299 | -7.25371 | -44.96404 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03b717f3-a52a-38ce-b518-dbfde5faf96f | -7.25095 | -44.96007 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d670b5fa-3ff8-35d7-a256-a3d4e0f182d6 | -7.17128 | -44.75282 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99a3dfd2-de70-39a5-a3fb-826c7e1c991a | -7.17004 | -44.50135 | 2024-10-14 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 970d2d9f-2b44-3f18-8bd5-5e61a86070d2 | -7.13411 | -44.83894 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 966a5d23-106e-316b-9912-9a1b1cd0d2e3 | -7.13347 | -44.79993 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d13c7bf6-ed9b-3c85-ba66-262e2d2a4788 | -7.13239 | -44.80684 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5e579a2-2601-30c9-a05b-0f1609003d75 | -7.12958 | -44.78164 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f23ca43-5edd-3375-a74d-b8e3b01f5bb8 | -7.12855 | -44.80977 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a36486b-51ae-3b8b-a1f2-437050428879 | -7.12801 | -44.81322 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e412ca24-a8ba-3ecc-9d8b-2b3cc98c2c78 | -7.12574 | -44.78458 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 295c9690-20b5-3470-af25-757281bd4ecb | -7.1219 | -44.78751 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6c72ab9-9052-3baa-9869-5bc2b0066dfd | -7.12082 | -44.79441 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4485ecbe-8ba7-3d61-ab75-398fc42b7963 | -7.00372 | -44.86799 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 542483b1-c897-3a00-a678-015b2b57b864 | -7.00117 | -44.70781 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd0e0cb3-05c1-328c-8a15-0ebbc9513fa4 | -6.98959 | -44.69538 | 2024-10-14 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6317d73-54bb-30d3-913f-e69aa51f583c | -6.98635 | -44.71609 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7f351e4-e063-36f3-89a7-8c0885f3dea1 | -6.98581 | -44.71954 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fbab800-5d65-3dc2-9bbb-377d17048495 | -6.93712 | -44.59887 | 2024-10-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd264a1a-262d-334e-a87a-37f6ec5795af | -6.93659 | -44.60232 | 2024-10-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1db1144-8642-3b43-af5d-5ccdf9b36f08 | -6.83583 | -44.85159 | 2024-10-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f20ac681-1291-3b4b-aabe-fb2eb43cdf7d | -6.72047 | -44.67786 | 2024-10-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27ef61d9-94ea-3951-bce2-718b3abdaca1 | -6.62589 | -44.69417 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c5449dd-08a8-3fbc-b374-6795698267c0 | -6.61707 | -44.68573 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef2c5612-2146-36ed-9937-b8803d8d94c1 | -6.50653 | -44.69661 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 008e0aa2-6f43-3d4f-9086-1fb414425eef | -6.68317 | -43.64931 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 814a3431-0c05-3060-9c4e-d3b52b060621 | -6.66077 | -43.96933 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1260b1e-0d64-3ff3-a2ba-9577a0143321 | -6.65239 | -43.93584 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34b03765-8369-31a2-8929-ac5ba23c84aa | -6.64962 | -43.93183 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72c27e80-f865-32be-8641-563f2b37dad2 | -6.658 | -43.96533 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfe777b9-f096-35c4-846a-4e5ad1c71320 | -6.65294 | -43.93235 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60617864-8dde-3725-a7ef-b1ffa63936e5 | -6.64853 | -43.93882 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0b2f01e-2d71-3aa6-88a6-debf9249ecae | -6.62579 | -43.7559 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab9ea2ad-e58b-3a0d-83d5-ef3df4e6bd41 | -6.68488 | -44.03366 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80c79be4-cf83-39e6-99eb-c4245d7041d9 | -7.96498 | -45.13839 | 2024-10-14 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28157cc1-37ca-39d5-980c-e7f34eaf0d9d | -3.27625 | -45.63841 | 2024-10-14 04:19:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ada34b4-a479-3c1d-bc09-1cfce5370db5 | -3.05679 | -44.4709 | 2024-10-14 04:19:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5956e17-9dfd-3abb-887a-cd919ebed4e9 | -3.05624 | -44.47435 | 2024-10-14 04:19:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfb9c9da-889d-3dfe-849d-17f06ac173b7 | -3.05348 | -44.47039 | 2024-10-14 04:19:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3ea3429-f787-3522-9420-555fac0a5ef9 | -2.40495 | -44.78401 | 2024-10-14 04:19:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a79494a8-ae6c-39f0-bd74-193339ae0a1a | -2.39551 | -44.77896 | 2024-10-14 04:19:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4539f08f-c9cb-3075-bdb8-a95bb9f79292 | -2.38052 | -45.74343 | 2024-10-14 04:19:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 210bc7be-b1b5-359b-a741-ecbe44e1438f | -3.63562 | -45.49928 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09d211fb-3d26-3c4f-b47b-d928149caebd | -3.63226 | -45.49875 | 2024-10-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f66e487-55b8-331f-b12d-d0d0a27a6f4d | -3.90117 | -45.6994 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a96f404c-f4f0-3348-ac5d-10f4f758e3c5 | -3.9006 | -45.70302 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc2d1673-15d0-3e19-bb2e-bc78e06efbee | -3.89779 | -45.69888 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5910916e-3dfc-36d5-9b8b-fbd37ebc3807 | -3.89722 | -45.7025 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 294461d9-f4f1-3e05-af6b-21b90478e08b | -3.87245 | -45.97464 | 2024-10-14 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3af7fad-e4d6-360a-b929-32602a714590 | -3.87169 | -45.97482 | 2024-10-14 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46ec04a6-01a5-3d28-8385-2d52fdf392df | -3.86886 | -45.9706 | 2024-10-14 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72ca6ce1-d239-34e8-bc3c-9928be698764 | -3.86828 | -45.97429 | 2024-10-14 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef839406-921e-37cc-81d5-e3ee693308d7 | -3.86545 | -45.97007 | 2024-10-14 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77a4e195-302f-3ab3-a0b5-8d02168740ad | -3.81021 | -44.69965 | 2024-10-14 04:19:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 244060a1-de76-3c90-bd42-330d374beb3f | -3.78176 | -45.2454 | 2024-10-14 04:19:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4bb6ab0-9bcf-30ec-ab31-76b3339cff78 | -3.77898 | -45.24136 | 2024-10-14 04:19:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 050f67ab-a0f5-39ac-b685-2eefecb6da4c | -3.74324 | -45.31916 | 2024-10-14 04:19:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aed2c1ee-a730-33a4-9ec9-db7638381d55 | -3.74268 | -45.3227 | 2024-10-14 04:19:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b432f738-fad3-3cae-a516-b76134080130 | -3.73459 | -45.73589 | 2024-10-14 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 072fd2b7-0b2a-32f0-b744-d580def155b4 | -3.73179 | -45.73173 | 2024-10-14 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ff5687f2-879f-3ad7-b7f5-1124800c8533 | -3.73121 | -45.73535 | 2024-10-14 04:19:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2ab214bd-9b6f-3495-abd9-544860667a91 | -4.52389 | -45.6754 | 2024-10-14 04:19:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35eff460-52b2-31d2-828f-2befc237a94e | -4.46904 | -45.93308 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ad61fce-9afd-3c2b-9f23-026670747d3f | -4.20986 | -45.7699 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69399535-c6fc-3c5a-a94c-352c2cf09d6b | -4.20929 | -45.77351 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1435609-2835-36d9-92ae-a085d130a7cc | -4.20648 | -45.76935 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fc939d0-92e9-32bb-863d-9877eea1327a | -4.20591 | -45.77296 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75a75d5c-078a-36ce-8a5a-941f37e07034 | -4.20368 | -45.76522 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb04f41b-c19a-362a-b442-41cb1d08913d | -4.20311 | -45.76882 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bd86851-c09b-36e3-b0dd-839cbcd47d74 | -4.20254 | -45.77243 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bd9c6d7-2af0-3dfc-b311-0761ea3367bf | -4.19916 | -45.77193 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11cec2ba-11a2-3ac0-826e-c3e72618ddd0 | -5.12026 | -44.96046 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README43.md)
