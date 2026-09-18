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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 426373dc-1ac1-3d4f-82c5-46378c543cc1 | -7.11759 | -42.08402 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0b4b983e-946a-3506-bea2-b43a97dc10ae | -0.53942 | -49.14172 | 2026-09-18 04:19:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec7c5bb8-78d7-38a5-b263-54eb8ac0b58c | -7.79876 | -44.84 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe9498b7-a980-351c-8f55-c8030108c8f5 | -7.18495 | -44.54432 | 2026-09-18 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90bdfcb3-68ec-36d1-b682-41c8df36f62c | -5.3323 | -45.1475 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00f56ec2-1a25-3a92-9384-a3fef9b47d23 | -2.83156 | -50.4698 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 9ad37c96-675b-393a-bac4-f4a672bade8c | -4.4876 | -55.49184 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31ad00f1-e25e-3107-b88b-477cbeae18c5 | -4.55851 | -42.96644 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24353f2d-5550-3909-a1a5-bdd952b2cfcd | -6.93765 | -43.11691 | 2026-09-18 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d562d7ab-d4f6-3e39-add9-d9a066ffea5f | -2.82714 | -50.46912 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| ccfc044e-89a2-30fb-951c-99d6e75d8f55 | -6.43456 | -47.24994 | 2026-09-18 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 696ed087-2df0-3e5a-9694-57a8f92b2218 | -7.30895 | -42.35291 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2dcb9fa2-bf2c-3883-b1cc-29eefbec1fc1 | -4.53671 | -54.93497 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3568ea67-bf31-3418-9055-561c38066f6d | -7.81551 | -45.10519 | 2026-09-18 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17694180-072b-3dae-bf69-2ad01152dec5 | -2.96721 | -50.33202 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3a4f81b-149b-3f08-a8b7-af61952b31a4 | -5.77613 | -47.28313 | 2026-09-18 04:19:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff09aac7-b913-3ca6-b86b-c3ce30421f56 | -6.49067 | -44.24025 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| add86886-4721-3d82-931d-fcee846b9765 | -6.87546 | -45.09056 | 2026-09-18 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 872dbce4-616e-3244-ba09-eea81414fb94 | -5.63716 | -40.86528 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 300d23b5-7ba1-3033-b69a-10150d84fa07 | -5.6229 | -40.85826 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c5ed244d-97e9-363e-a05e-cdab82df98f3 | -4.00424 | -41.27271 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1b5b7abf-c460-3d32-8e30-94ea20298fc7 | -6.34864 | -44.08208 | 2026-09-18 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2103b5d-d2fb-3d0e-878b-84f36b942f77 | -4.08142 | -49.31861 | 2026-09-18 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b1a0b25-3011-3982-9850-8c4b427a3263 | -6.45555 | -46.00936 | 2026-09-18 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48084c9c-6246-3de1-89d5-7df9479f474e | -4.87861 | -56.06555 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb51bfb5-580a-3250-abb9-22c80f36aca9 | -7.7234 | -42.50959 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 026ac7ba-31eb-3e11-a3f2-49b0ef1f1c00 | -7.72772 | -45.36069 | 2026-09-18 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 863d0aa9-1e45-3659-9548-03be2f7042c0 | -4.56353 | -42.95618 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65ec9f81-9ac5-38b6-94a3-620c6633e3a7 | -7.81104 | -44.89162 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49495394-4532-319e-a068-7338d31610e9 | -5.75453 | -51.92914 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f508cbe2-2c92-325f-b1bb-fc2bd3953454 | -3.36703 | -50.45596 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1b85bf26-4811-3315-924d-e31de79e7028 | -5.22317 | -49.30781 | 2026-09-18 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef9a2b5f-12f0-3091-94b3-31b22ddc1b5e | -5.49534 | -45.25826 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e03fd07d-908a-3367-9d24-fae91af8be6a | -2.90173 | -54.18469 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d3112ae-d784-36a7-aef2-d14313833989 | -2.09962 | -52.03627 | 2026-09-18 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb31c517-0ca9-3b5f-bb33-f494e12fb903 | -7.81059 | -45.11506 | 2026-09-18 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b439c98b-cd97-320f-a7a6-5439ba5fe49f | -6.30582 | -41.77858 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 750f538a-b197-347c-926f-eed5dc6a4f4b | -3.36773 | -50.45174 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0d220bb2-aa34-3391-a2f6-25b4075b2e3f | -2.29869 | -48.58002 | 2026-09-18 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6451fe28-9952-38eb-a778-fcb1733858a0 | -6.58786 | -45.88232 | 2026-09-18 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0b45074-fbe8-32c3-a96e-b48033c13ef7 | -7.00801 | -43.86389 | 2026-09-18 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b235edae-0f1d-3790-9801-60cedcf94cc2 | -5.89395 | -49.77991 | 2026-09-18 04:19:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b639f995-7a3b-3fb9-ac62-ac418f61dcac | -5.62533 | -40.86776 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 11336113-277a-34cf-a1d4-07358f23599d | -4.55587 | -43.56025 | 2026-09-18 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4aa390e-f9e6-36a5-801c-9ad12a6aeb33 | -7.27634 | -46.79623 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e78f67a-82ad-3796-b934-326bb9c12c0d | -7.19116 | -44.43852 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f4abd57-8cc4-3145-8119-1777519140b9 | -7.37322 | -44.47086 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13421e63-68ab-338a-adad-9ee790b89d52 | -3.02548 | -41.15873 | 2026-09-18 04:19:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0ee00da2-848b-3eaf-89cb-caa29a89fc5e | -4.81573 | -42.88745 | 2026-09-18 04:19:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8e72ef11-9e71-32ef-ba4d-0ebaac55ccff | -2.83454 | -50.47934 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be08e48b-6dea-3865-8074-a421cb445977 | -6.99351 | -43.32812 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13507cba-2b74-389e-b0ae-42f19f247ee8 | -7.93787 | -44.81915 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 129ce14f-8a44-35bd-96b1-92e4298e1c4d | -2.81613 | -50.48089 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2e1a57c6-9ffb-3e6d-bb5f-3d05d7ec939a | -6.33487 | -45.67323 | 2026-09-18 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c139cf64-a05f-37aa-bc58-59db82129e6a | -7.63255 | -45.83707 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39a26aae-c0a8-3f49-afa2-487379d73f87 | -6.19007 | -45.3396 | 2026-09-18 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03caa1f1-417f-37ed-8cfd-222ea39558ba | -6.96482 | -42.56815 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e49f2c6-8547-3ab0-a870-0b3da32dc71b | -3.36195 | -50.4595 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 763a1d8d-55e1-37af-86e5-f7249b3abd9c | -7.06151 | -46.22205 | 2026-09-18 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a846c2b8-247d-39de-962e-358c5a755837 | -7.09107 | -44.07218 | 2026-09-18 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0d8d523-f455-3425-9bd1-66693ae3f0d0 | -7.6602 | -45.8342 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2f93d158-459f-327a-b4bb-fe7281596a43 | -3.92113 | -55.92329 | 2026-09-18 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40495049-b5f2-3c70-8a06-7f9a9b456ca8 | -2.79486 | -42.47768 | 2026-09-18 04:19:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6a30cd1b-b26f-36b6-bafc-dc8011e10ee1 | -5.75535 | -45.09732 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a733ad3b-5af0-3879-9da4-c95638ff05f3 | -2.89604 | -54.1838 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65424321-c395-3261-bd85-c7fa1f4780a8 | -7.61802 | -44.73314 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6325fe01-251c-34bc-a026-017fc3913cd5 | -5.73562 | -52.24172 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4fc1935-91fb-37dc-811e-a84bf986cdb1 | -6.2745 | -41.6678 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4e9ebd03-2746-3f13-ac0c-859a19ed671d | -7.67162 | -46.10575 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3198074-09d5-385a-8c3e-6770cdb0d7a3 | -7.0747 | -41.79164 | 2026-09-18 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 97c18927-a679-34f6-b56c-938da5723b6f | -3.36335 | -50.45106 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 55e3fec9-f088-3ab2-8594-fb139ee288eb | -4.43018 | -46.29742 | 2026-09-18 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a4d922d-6b06-365e-8b1c-4404952b4803 | -7.01972 | -43.63213 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f55b384-ac43-31b4-b0b4-9304be3eaab9 | -6.6648 | -43.64004 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 338f99e3-e79b-303a-aa6f-dde7b914234e | -4.5618 | -42.94485 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 04f8d078-6fc6-3c39-a753-1c6d604f0593 | -6.34803 | -43.37513 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 17b589ca-6f02-32f0-967c-abc93d9ca21b | -2.95777 | -49.00752 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47afeada-816a-3007-8993-fdeb61048a50 | -6.30162 | -41.78212 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64a08c33-96d8-3f76-a413-0e6a0f16ee76 | -6.15297 | -47.71551 | 2026-09-18 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 443e8af9-37c6-31dc-8bed-e73c8cf85b9f | -7.05768 | -47.4815 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7440081c-ac31-3d50-b1de-23d3ab1ee4ae | -2.54786 | -48.15867 | 2026-09-18 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b569b54-6213-3c6d-9761-c6e089dbcd2a | -7.34106 | -44.47962 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f365b23-6470-3965-b5a5-33829eb83fdf | -5.61853 | -40.86205 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ced81380-9826-3f7c-837d-487cc9133c7d | -6.4589 | -46.00988 | 2026-09-18 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7d4c4c3-0edf-3e22-9864-99df9ccd4056 | -5.15379 | -55.94083 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c14cc252-ebed-38e6-9c49-c74a82ec2e04 | -7.35612 | -44.47175 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e8df841-3a5d-36eb-a000-a287631a3577 | -7.86831 | -44.54456 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec2d6dce-9cef-338d-a31d-b757f3b5574a | -5.97989 | -53.57948 | 2026-09-18 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0332a21-e643-3b7f-844e-dbd57abe10db | -7.93733 | -44.82262 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a70fdfba-fe28-3d85-b2c5-0e7b3b7f8532 | -7.63206 | -46.16448 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 71cb6218-3512-3e49-8935-f6a2b503d542 | -6.29138 | -41.80147 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3ef85315-e582-3e96-8f6b-6db93ff1cebb | -7.1132 | -42.16202 | 2026-09-18 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fc664d48-0ce1-3e86-bbb9-4942c5083f5a | -7.9637 | -43.97108 | 2026-09-18 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c127ff59-353c-341e-9d0c-f62f1acdd1a0 | -2.81416 | -50.46856 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e058be90-cbc7-36bc-9c5a-e7e083625029 | -4.57137 | -42.95 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 137cb9f0-42bf-36db-a16b-b6daefb53b24 | -7.47892 | -45.29983 | 2026-09-18 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a1addb2-3d0f-31ad-8698-d4d36df8e3ed | -6.29619 | -41.79385 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0a03c2ea-19d9-3361-9ca1-64a10b7a237f | -3.21366 | -53.94648 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbb04052-5889-34c7-a314-9c995e56086e | -7.29762 | -38.96179 | 2026-09-18 04:19:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22ce83eb-e4c9-3d70-8aad-7b4f78854868 | -7.38988 | -44.49489 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README34.md)
