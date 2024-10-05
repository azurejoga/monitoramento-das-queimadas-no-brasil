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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b469632-6a1c-36a4-b6f7-024e83e088ec | 2.13348 | -50.69697 | 2024-10-05 04:34:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06d6086e-5b6b-3bc4-8930-927467cdecca | 2.13051 | -50.70171 | 2024-10-05 04:34:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c08ae228-4562-310b-8ded-841ca559dcb1 | 1.31695 | -50.85597 | 2024-10-05 04:34:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48bfe2a5-41d7-34ec-b6bb-85b0145080f1 | 1.31573 | -50.85507 | 2024-10-05 04:34:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35e02b49-863e-3a40-8d89-44b7367fe9f6 | -2.9014 | -50.7142 | 2024-10-05 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 7af54d14-d683-3932-9c60-0589ec563f07 | -6.9514 | -59.0666 | 2024-10-05 04:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 89891fa3-fe24-3993-9d1c-de61311ac4b3 | -8.7959 | -49.9533 | 2024-10-05 04:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d4accb38-2b65-39ea-a4cf-66bc0e216f24 | -8.7772 | -49.955 | 2024-10-05 04:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a1cbbd92-f887-311d-8dd6-d2f355476cf5 | -4.86411 | -38.43799 | 2024-10-05 04:36:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a090439-c04b-341e-b639-8df2cd82c50a | -5.11983 | -37.56717 | 2024-10-05 04:36:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c1c3ae4c-7848-3dab-90f5-84f8247878be | -5.11914 | -37.57205 | 2024-10-05 04:36:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 86d12587-b452-3881-834a-4095e23c80fe | -5.11757 | -37.56852 | 2024-10-05 04:36:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f94f7fdc-01db-3fec-94fc-9da8ccc0ae2b | -5.17706 | -41.29768 | 2024-10-05 04:36:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 11dd9cfe-b888-31ff-99fc-44c00deab5ba | -6.64134 | -41.99482 | 2024-10-05 04:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 25e45e47-b9d0-31c5-988f-32a81b0dfb46 | -6.64064 | -41.99991 | 2024-10-05 04:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aec23a7f-8349-384b-97e3-ceead4f95ff6 | -6.64003 | -41.9981 | 2024-10-05 04:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0cfa7dd4-797f-3dfa-98e4-3d450ab7cab0 | -6.63529 | -41.99742 | 2024-10-05 04:36:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 38e3da56-7d2f-36b4-88d2-2de31a822996 | -5.05489 | -42.67089 | 2024-10-05 04:36:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91d8d245-10e0-3a9e-9392-b832518c3332 | -3.21668 | -42.69968 | 2024-10-05 04:36:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5419cb60-155b-3ebd-acd0-0afca145a42b | -3.21608 | -42.70373 | 2024-10-05 04:36:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c12f1fc7-a82f-36bf-93c6-ed73a203153b | -3.79957 | -41.59837 | 2024-10-05 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ed101d6-5edc-38b8-8c9d-93082012a415 | -3.79797 | -41.59052 | 2024-10-05 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 027e5b3d-b06c-3533-a7ba-329f1bc9335e | -3.79723 | -41.59541 | 2024-10-05 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 502e9b22-a6ee-34c0-ae3c-700762455a26 | -3.7963 | -41.58792 | 2024-10-05 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d6a01b44-5751-320b-a1e0-c0d4ca8febaa | -3.79559 | -41.59285 | 2024-10-05 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5997fc86-17fd-3563-80f0-c340b3be90f1 | -4.89591 | -43.20201 | 2024-10-05 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2adf9c15-e61a-32ec-9d21-5b2db63a357e | -4.89166 | -43.20138 | 2024-10-05 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22ed311f-0dbc-3c8b-a6f8-60e4d8396f5a | -4.46482 | -42.88311 | 2024-10-05 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eececa6b-33c8-3d38-acde-27c492aeb6bc | -5.05446 | -42.66903 | 2024-10-05 04:36:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b34a6057-1f56-3889-a6f0-dfbafc685def | -6.28445 | -42.76978 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e2ee452-d0e5-3eb0-98a1-da120c503d51 | -6.2806 | -42.76484 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 46e2f60a-6660-3eb5-a26e-df6597e31fd3 | -5.68834 | -43.15818 | 2024-10-05 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7154f658-7610-3b42-9680-4c0f38c2a352 | -5.68774 | -43.16227 | 2024-10-05 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7bbd7fe3-eef9-308e-8bd1-c7d937f08875 | -6.43879 | -43.12978 | 2024-10-05 04:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6253cb93-304a-3a89-87dd-9f4c6e9896cb | -6.28908 | -43.44685 | 2024-10-05 04:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a482ef8c-da8e-378d-9e6a-468635d07393 | -6.28617 | -43.25473 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91ea9b7b-9667-3c0c-9b6d-8fc081aabcef | -6.28558 | -43.2588 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 774bf3c9-929f-3726-908e-cf51b24cea10 | -6.28342 | -43.02323 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 513e15c1-0d75-385c-bfad-92c5a76400b5 | -6.28322 | -43.02496 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ee9a2a18-4381-3bb0-a9ad-a91534c1f3b6 | -6.28126 | -43.25817 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f99b67d3-a4a1-3418-b704-3c9d965aaec4 | -6.20169 | -43.27707 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cedcec1c-197e-3b65-9df8-420719b4d538 | -6.06721 | -43.08636 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45714ef8-b459-3b7e-8a96-486c3e1ceacf | -6.06657 | -43.0906 | 2024-10-05 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78846c5b-088b-3f41-a6d2-c7aa2a1caf89 | -5.64505 | -43.24385 | 2024-10-05 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c53376b-0f2b-3863-9f4a-25b9764a15d1 | -6.47361 | -43.35947 | 2024-10-05 04:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b988079-847b-39cd-a843-c31e9bce022f | -6.47359 | -43.4211 | 2024-10-05 04:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85a77cd6-1daf-3a2a-92b2-5fdb25a47ff9 | -6.4693 | -43.42046 | 2024-10-05 04:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5969ca12-821b-3d05-840a-d63c5bb685ca | -6.46874 | -43.36282 | 2024-10-05 04:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 920dfb7c-5807-347b-b343-ecdfc94aba95 | -3.47604 | -43.3633 | 2024-10-05 04:36:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cab7b42b-3113-3f6a-b56e-0643f8e4506d | -3.47247 | -43.35898 | 2024-10-05 04:36:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a93adfb6-8ffe-3403-9836-122b9a8e6a81 | -3.47192 | -43.36268 | 2024-10-05 04:36:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85190754-aa1b-3725-acba-b62b5fdd0b66 | -4.94795 | -43.78 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 776eb41f-d28f-3405-b3d1-a14d938a71ff | -4.9444 | -43.77577 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de791d09-193f-3e83-b024-75342a2f9341 | -4.94385 | -43.7794 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| defad997-a1a7-3b7f-9ac5-213eedae5443 | -4.93565 | -43.77829 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19454cb3-206f-3b1e-940c-57da9925b430 | -4.93155 | -43.77775 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fe73318-1e94-33f4-89f9-fcccb8aa1277 | -4.73373 | -43.59775 | 2024-10-05 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3e04362-8885-3b69-b245-d5ed0896ec30 | -4.65995 | -43.76107 | 2024-10-05 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2228ccc3-64b1-3592-b640-210c6bb4fb8e | -4.01645 | -43.24962 | 2024-10-05 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 170e6af0-0a2e-3f13-854b-0e3f3a7b9fbb | -4.01226 | -43.249 | 2024-10-05 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f7baa2f4-61e8-3d29-bd9e-79a8bbf0ed66 | -4.00808 | -43.24837 | 2024-10-05 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d21cc019-ab43-397b-a884-b5cceecb6c74 | -3.99915 | -43.25093 | 2024-10-05 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5723baef-b05f-38a5-a18e-ef1f17b90e62 | -3.99859 | -43.25475 | 2024-10-05 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 897eef15-4c93-3c53-af48-1e2721a17de0 | -3.99803 | -43.25854 | 2024-10-05 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c385e767-e7cb-3d16-9bfd-43cdacced16c | -3.99497 | -43.2503 | 2024-10-05 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95ea4f12-ab63-383b-b7a3-a3ecf328535f | -4.94849 | -43.77638 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce792d72-e1c8-38f0-b66c-c14e1a01f36c | -4.93975 | -43.77884 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 44e0b5a7-5495-3b1b-a3c9-ae600e2c3574 | -4.93921 | -43.78244 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 52e67d1c-63d0-39e8-ae70-270b35e1bd12 | -4.93208 | -43.77414 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 502538de-25b0-3ace-ba74-689863ae59c4 | -4.92799 | -43.77355 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f1db0e4-092e-304d-a348-ec8bdd0a9160 | -4.81723 | -44.35559 | 2024-10-05 04:36:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1633c98e-0031-35c4-a6f9-8f419d8c5f6e | -5.36687 | -43.34822 | 2024-10-05 04:36:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78f292f3-7012-3500-b93f-67f17a4bc9f6 | -5.53347 | -44.31215 | 2024-10-05 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2b914b6-ac2d-367c-8a18-15af90d96122 | -5.53296 | -44.3156 | 2024-10-05 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cc045d9-e3ac-3d15-91bb-3827628eff2a | -5.53244 | -44.31905 | 2024-10-05 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ff0017d-e245-3330-8ed2-e68824ec9d70 | -5.52952 | -44.11885 | 2024-10-05 04:36:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f189852-bb17-34c3-8a0a-a5d57c958a4a | -5.52949 | -44.31155 | 2024-10-05 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41129816-1f76-3693-95c0-4b05b3e8b9c0 | -5.52897 | -44.31499 | 2024-10-05 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64cb429b-7508-3e1c-b774-89875d6cfbb7 | -5.8832 | -43.71628 | 2024-10-05 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ba94225-6857-32a1-a434-39294de5e2d1 | -5.66535 | -43.61172 | 2024-10-05 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7db28b03-abf2-3b34-b268-2ff2577a56e4 | -5.93648 | -43.90062 | 2024-10-05 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b61e84a-11ac-37df-a782-3d3aefff9763 | -6.21138 | -44.3199 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 613decdd-c202-391d-a082-a7a1b1d8c124 | -6.21001 | -44.32021 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a4ec437-490f-3770-9803-50129b2d5790 | -6.1839 | -44.1349 | 2024-10-05 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b84dad6-c0b2-3cc7-9428-2fa1e1459a71 | -6.17164 | -44.13342 | 2024-10-05 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0abecca9-78b5-3197-84f7-7c109ffa1572 | -6.16806 | -44.12944 | 2024-10-05 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60a5ee5c-a523-30fc-96c2-929875995177 | -6.16705 | -44.13635 | 2024-10-05 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6acf65dc-667b-3415-b32d-a20098df6afe | -6.16505 | -44.15006 | 2024-10-05 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbb28de9-e0ce-3d09-92bf-505cf1d79f14 | -6.08401 | -44.70207 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03ee81a4-9053-3766-a738-7ae538cec690 | -6.08009 | -44.70145 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59918e3d-fc23-3bc0-830d-cbde1c5412d1 | -6.07618 | -44.70082 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a1b6e3e-21fe-34f2-bdb9-1ce17082c7dc | -6.07227 | -44.70018 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7299b257-9daa-3c01-9776-1f34c4d919e7 | -6.06836 | -44.69954 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cf530ae-8dd6-32bc-a812-9a8d3478ba80 | -6.06763 | -44.70447 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a068e0a5-0bfa-338b-82a0-0d84060b80eb | -6.00895 | -44.56053 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d685deb-5c9b-3a41-aced-da8211bd5a68 | -5.82287 | -44.1326 | 2024-10-05 04:36:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 7ea35dac-c8a1-3337-92e1-d4a8e3c8cd2e | -5.81987 | -44.1248 | 2024-10-05 04:36:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 71d2ea9e-7c95-39bd-b542-6226dd3388cb | -5.81882 | -44.132 | 2024-10-05 04:36:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 02f98128-0058-37d6-8532-fd1d19e42df4 | -5.8183 | -44.13557 | 2024-10-05 04:36:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b4d9b29b-5e10-32cc-abf7-e6e32136a7a3 | -5.81478 | -44.13138 | 2024-10-05 04:36:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README88.md)
