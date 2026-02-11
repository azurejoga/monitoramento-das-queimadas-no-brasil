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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f26a7d05-6007-3300-9fc0-f96059beae9d | 0.9598 | -60.52477 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4bcf6ce-8d48-3f1e-b749-3f02b5a0e530 | 3.6744 | -61.09067 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df023ad-6ff3-3756-8c70-0f3af4119872 | 0.96209 | -60.516 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68e520bd-a33b-3b26-a293-bf631a7e9eb4 | 1.34633 | -60.06128 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a386f9d4-b2c5-3eb8-8292-27c47f9c8b19 | 1.27903 | -60.43725 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14118af9-5608-3183-b321-b002e7e82abe | 1.93137 | -60.21817 | 2026-02-11 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 731c848c-4e23-3a3c-9a68-7f84773b6002 | 0.65846 | -60.36166 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8ab83ff-64bb-36b5-b89e-ce1d50038620 | 1.14168 | -60.51134 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2b8280f-6470-3356-9c73-5d91d866a8a7 | 0.87754 | -59.58706 | 2026-02-11 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebd017f0-e038-3a67-8505-da31401a6ceb | 3.71565 | -61.02618 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cca5409f-e76f-3f00-b472-6b8528d3b12e | 3.6219 | -59.92218 | 2026-02-11 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 59e810ff-a744-3973-8cfc-a058d9cc14be | 3.38674 | -60.65211 | 2026-02-11 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c444f346-20f5-36df-91cb-51b36a4226bc | 0.52641 | -60.4624 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59b1d915-2fcc-3564-b97a-10a5a0ad3800 | 1.13513 | -60.51659 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2193e861-1dc2-3746-9eb0-59d49ff6c8ca | 0.95555 | -60.52123 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3750380-8a5d-391f-9842-61475b52d9b0 | 0.95849 | -60.51656 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ecf3b455-286d-3859-92a0-294b52bbf972 | 3.62487 | -59.91753 | 2026-02-11 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3a67507-fdc3-3450-ac80-07348b19e3c7 | 1.3479 | -60.02464 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 065b4e86-2f17-3d2d-a645-7f1ba02aefbb | 1.6903 | -60.36086 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b68dfe67-5ec2-3207-b5a7-bc4ab6a417a9 | 0.92394 | -60.36753 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58392fc0-fb0d-369c-a0b0-b149cb972c7e | 0.97091 | -60.59494 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea0f9434-ee12-3380-b0d5-bba84aac42c2 | 0.97156 | -60.59909 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a725573f-4542-3df8-8357-c03cebc81c86 | 4.89095 | -60.27822 | 2026-02-11 05:16:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d06a3a29-df60-3418-b5ee-a1f504566172 | 1.34498 | -60.02911 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 300711e7-212e-334c-ba4f-88f4e08244af | 0.65908 | -60.36568 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e9a5de3-29c8-3555-b8ef-4d666995cdd9 | 4.10461 | -60.5337 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baa6c426-5460-3130-a084-03364eff34aa | 4.40888 | -60.77607 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5db11f9d-283f-349c-baf1-fb2551550410 | 0.78816 | -60.6721 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b58f8b23-28e1-396e-b40e-4a847c805707 | 3.7197 | -61.00142 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36eeec69-776c-3e99-9a3e-05df115cd5a6 | 0.96568 | -60.51545 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 535ead69-f906-39d3-a7de-e892437ebbb1 | 0.66201 | -60.3611 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f103d2-8da5-38fb-b39c-c1310038c8ce | 1.11821 | -59.19798 | 2026-02-11 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e516e10-1968-3005-80d4-066d017cb720 | 3.38866 | -60.65469 | 2026-02-11 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc89aa40-f117-3f62-945e-5d0c4c91624e | 4.10392 | -60.52923 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b583ba44-558a-3998-8f22-376dc3f1ae48 | 4.20415 | -60.8813 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39bb10ca-cb93-3414-b9d8-079a015049b5 | 0.95425 | -60.51302 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef5dd2a9-ebd8-3480-a1cf-924ecb683ab8 | 4.41029 | -60.78548 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84e8c352-fd5f-3cab-8b27-e03752e542d1 | 3.71422 | -61.01676 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71804b58-17b1-3e42-8f16-372c2b43a9b0 | 0.96699 | -60.52367 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f38d692-2f79-32e6-969c-c770b87cba86 | 1.28784 | -60.42328 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac8125a8-1e07-3d8e-b862-52cec5eebb2d | 1.34851 | -60.02857 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 422daea6-95bf-3767-977d-07cf9ee8e3d2 | 0.97517 | -60.59853 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5b80610-f0ab-3259-aad1-d3679fbd441c | 3.69465 | -60.9909 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33f9fe18-3d83-3ee7-a1ef-984b3a87c4f6 | 4.40679 | -60.76209 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa393936-5387-3e11-b1fc-153071bba32e | 4.20869 | -60.88551 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ad979ff-0ba9-31e4-a283-25695553b686 | 4.17416 | -60.16018 | 2026-02-11 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6b40d68-5422-3b12-90a3-a07541231f04 | 0.95261 | -60.52591 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04631e2b-8d8e-3146-89ed-95ee96dab549 | 3.39116 | -60.65599 | 2026-02-11 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7a3ae42-5524-3e4a-9636-bf3dcaa15e7e | 0.96274 | -60.5201 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e1eeae7-3728-3fab-bb3d-ecc68d4c54c5 | 0.78881 | -60.66917 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bd3e37d-d56f-31c0-ba26-d96bcf8c8aca | 1.87159 | -60.58397 | 2026-02-11 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a93adbb0-0ea7-3f23-8498-1cdc6ffe9c96 | 3.67511 | -61.09542 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5673af62-9fbe-315b-ac2f-2dcce35a31e4 | 3.87618 | -60.09461 | 2026-02-11 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5c098c9-73ee-3e98-83be-1fe9061923c5 | 0.9549 | -60.51712 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6eb318e-a762-362e-b4ab-2478dd2a869e | 0.80145 | -59.86265 | 2026-02-11 05:16:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c86a4ac8-d51b-3842-851b-443127d68740 | 0.9562 | -60.52534 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7802adb-88ac-3b2c-96bc-57de19c5c1d6 | 1.28849 | -60.42737 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 398519ed-e02f-30f5-9add-2918c190c2c9 | 1.11881 | -60.50649 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 082f91fb-b702-3cb6-8ef8-920c8f8c2598 | 0.96633 | -60.51955 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64ec0ada-f6d1-386a-b9cd-5a190ce94662 | 0.78027 | -60.66908 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 503f9d8c-bf73-3933-8a46-d81b9bc251e0 | 4.20798 | -60.88082 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 720a89ac-112b-38c4-869a-1ce6b2d2f204 | 4.20344 | -60.87657 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bb51b2d-f2a5-3104-82c4-3d8a4e2ec208 | 0.92751 | -60.36698 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f277dfeb-ef6f-3a2c-aa42-eb880adc17d7 | 4.39435 | -60.67928 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 668c9078-549d-313f-a01d-1698b0ec3952 | 3.28252 | -61.2869 | 2026-02-11 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ab7c934-303c-3572-81d8-079252ef5660 | 2.74396 | -61.25363 | 2026-02-11 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 39577cc6-2b7a-308d-9eee-16112d601052 | 1.28491 | -60.42793 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 160481a8-2bb4-33c8-8c49-89c0bf8dad13 | 1.3461 | -60.06027 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23e6f301-0f4d-37c3-8c8e-8fbab41fa548 | 3.39489 | -60.65541 | 2026-02-11 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e8090d5-4999-342d-89a8-18c2a2add315 | 1.11585 | -60.51117 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f67a9712-48ba-3f9e-a13d-60d68c4c432e | 0.95196 | -60.5218 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75495aaf-dd1c-3f99-a5f5-17ecae55a03e | 1.11481 | -59.1985 | 2026-02-11 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 929a34ba-5442-32c2-ae1e-fc1f82211a39 | 2.48113 | -60.72717 | 2026-02-11 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f2f62f4-6537-3c3c-a162-d35a1f6635d2 | 1.33853 | -60.7186 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fd5d88e-568a-3dbf-b9f2-e77b2de625e3 | 0.95719 | -60.50835 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0e38064-8d9c-30c3-a1e1-94c62ffa4ccb | 1.28556 | -60.43204 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b705e4f-ccff-33ad-b2ce-a85d65dd484a | 3.71732 | -61.01144 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d4122fd-ad2d-3ad3-a73f-69e62b28089a | 3.38604 | -60.64766 | 2026-02-11 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46035c03-ce05-333a-b341-7a47ff48d2ee | 1.11945 | -60.5106 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2437e2ef-9973-3389-b6bc-a6ed94e5369d | 3.71493 | -61.02147 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6177c370-cf16-3cf5-bb68-e987875fb3dd | 3.38933 | -60.65914 | 2026-02-11 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62321521-1da6-30c1-bc6e-b42c77c2a4b4 | 0.95915 | -60.52066 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84cf9eed-a78f-312d-9951-34e761dfcbc4 | 0.96339 | -60.52422 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1909318a-b50d-356b-bfaf-5f9dfd4f85d7 | 3.31916 | -61.03841 | 2026-02-11 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd63e783-705a-36c1-b973-8dc8c39805f3 | 3.31844 | -61.03376 | 2026-02-11 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ae6e84-e051-33d8-9abe-94790968b51e | 0.80188 | -60.28284 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe318d46-0e02-3321-ab88-95e5d9dfcf2d | 0.96144 | -60.51189 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa3af340-2dde-3cc5-85bf-7531880ca5ae | -2.98611 | -54.2174 | 2026-02-11 05:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64db5668-fdbc-3352-930c-78033e8fb1db | -6.22432 | -57.78076 | 2026-02-11 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d22295b3-0579-3157-915d-ed21cb16d5fa | 0.9569 | -60.5233 | 2026-02-11 05:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 2a623386-714e-3ad0-87fb-9a542f3b0d4e | -16.02504 | -59.90939 | 2026-02-11 05:22:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dbe99cb-e99c-3c92-9bfb-077dffe66e62 | -21.17341 | -56.50126 | 2026-02-11 05:22:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b16a5d14-04c4-3abc-acdb-7f09923bfb37 | -15.60383 | -60.07276 | 2026-02-11 05:22:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cf9f577-5905-324d-89b5-d3b3258b71c0 | -18.89686 | -56.05573 | 2026-02-11 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2c6b3100-ad54-31f8-8dca-d8e9a80e8966 | -20.72724 | -55.15479 | 2026-02-11 05:22:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5bf01bb-8110-3d4c-ad0c-c2341aa4ad5b | -18.97256 | -52.93301 | 2026-02-11 05:22:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93ceab82-cc7f-309d-ab1d-81125b2f83ad | -20.86855 | -56.04631 | 2026-02-11 05:22:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e87ae248-95b6-3ef0-951a-833047c84f68 | -16.58128 | -58.21438 | 2026-02-11 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 619ee896-71f2-3db9-9713-be200ead76d6 | -16.58488 | -58.21497 | 2026-02-11 05:22:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8c2a88e9-38d5-3fb5-8e46-67373c1e37f9 | -18.97292 | -52.92966 | 2026-02-11 05:22:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README4.md)
