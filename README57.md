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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10f26f55-afd9-3229-9119-349fc756bc25 | -6.69708 | -58.55169 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d79db52-1306-3fd0-8d2c-5a3d8106d2b6 | -10.4232 | -57.69149 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99b9fc35-5044-3619-b59b-7e0e875ade94 | -8.63868 | -62.65084 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0ce1c75-96cb-3193-aa3c-959f41d30c7b | -9.27928 | -56.90836 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7393bee5-fea9-3e20-9e57-978cbe8799c9 | -9.17265 | -59.51591 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c822b1a3-69ba-3a1b-916f-238b1813001b | -10.45817 | -58.0023 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39e49e28-566a-37e0-b1b2-39c03dce0886 | -9.02114 | -65.68587 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bab3c221-d475-355f-84b6-eae83f49e031 | -9.58156 | -55.37786 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee52dae9-f9f9-38d8-8fb6-bd015cb93163 | -10.31754 | -46.79777 | 2025-08-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9dfb5a8-8cae-3367-ba1d-660f6a00a3f0 | -10.45761 | -58.00603 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1e5817d-6fc6-3bb9-9999-a1e2fba10da5 | -6.24309 | -60.01776 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2914c918-242b-3a77-95ac-a8dc6bcfee14 | -9.19248 | -59.51903 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9c0283d-07da-3590-85cf-c69706b99d7b | -9.15435 | -59.56581 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff7635af-f93d-37bf-b078-3d5bcaf3067d | -7.05044 | -59.81749 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32cc5223-1fb2-35b5-a941-737ae6e2e456 | -9.32891 | -63.20566 | 2025-08-27 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65a74ea4-7b6e-357b-aac4-c0be2a5967cb | -7.35584 | -59.67009 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e01d5a0e-f663-32e9-8150-535a5358c923 | -9.41073 | -62.47838 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ced20e9-f0e6-339e-891d-4f6ff59c88bf | -9.1813 | -59.46022 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef29959f-8a65-3392-b3d5-c7f3661874ba | -6.94359 | -59.56546 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08a103b2-78a5-3bfe-916e-7b06169c52c0 | -11.31934 | -55.21562 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b7d266d-439d-3365-ba9d-60edcef353c0 | -6.63301 | -58.54883 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b733d35-7ea1-358a-9699-306d2e4e8e13 | -7.42432 | -60.01267 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 329f7f1c-6ae5-3f9e-b743-2d011f1ecfb2 | -7.90095 | -61.521 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d75c2d2-d61a-3eab-8695-ae8411041465 | -6.70825 | -58.56766 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9d9fef4-bcb6-3578-ac99-3dda3aebcf90 | -8.89853 | -60.54383 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7721a90d-326a-3fec-9978-842163e6b528 | -10.31884 | -46.78671 | 2025-08-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a80b748-e375-3013-804b-85d761fa5eb1 | -8.50539 | -69.80192 | 2025-08-27 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 075edda4-762d-3f47-8eb8-954a5141745b | -8.96271 | -65.97775 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e260da4-a479-3f35-880f-750d90b7b123 | -6.83799 | -58.95708 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f101df3f-3f50-38ad-9421-11204f1b478f | -9.9516 | -46.37727 | 2025-08-27 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bba0577b-9e4e-34a8-9b40-c4d9c64a4cb5 | -9.15376 | -60.7809 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cd305e7-1af4-3b79-aede-610b90032d5a | -6.82484 | -58.97629 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7476923f-23f9-3a11-9ee9-ec509eba61a1 | -10.10059 | -62.89772 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c132fa69-3f73-30b4-95a7-f5fe9586a1f3 | -7.05603 | -59.2397 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec8938b1-de9e-3453-aa20-39ccf6e148e8 | -9.5932 | -55.37961 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d28d1e4a-a476-3ebf-8cb1-a104327ba082 | -9.40636 | -60.53947 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48fabe29-e4a1-3a89-92ca-c674352e93b1 | -8.88291 | -60.76987 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba0b2bc3-d59f-3ed5-a976-8e23cd4fd865 | -9.10218 | -60.31076 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b1a848c-77c8-3bfa-b9e9-c43138bc758c | -7.48369 | -60.666 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fad3b33-6d53-3cfd-9453-7fe77cbece30 | -6.94083 | -59.56149 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8d63198-66cb-36fd-b7e4-ee23ab0432cc | -8.85464 | -62.4391 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 566ae1da-674c-3253-be5d-97db3ac75110 | -9.15042 | -60.78037 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6afadbc6-985a-322e-bc67-8f495f28ed5c | -8.53888 | -62.63984 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ddbd206-3f6d-3f25-bc57-87212b085128 | -6.24365 | -60.01424 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9eef7982-0335-3bad-b130-c7f365ec8c32 | -8.34822 | -62.93668 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc0f7779-3261-310e-a683-bf91ddfb676f | -7.62521 | -61.03303 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b4e45309-1d60-3dae-b327-debffeb5c294 | -9.40915 | -60.50031 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| c85607df-b7a7-3434-a09d-22c22b39b5f0 | -6.71049 | -58.57513 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 042481b9-6fb2-361f-9ad5-de30f9ee079b | -8.96924 | -63.38433 | 2025-08-27 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45d34194-0430-3098-ad42-e02f1acd18a8 | -9.67105 | -67.50124 | 2025-08-27 05:18:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f6bcab4-a75c-3bea-b64a-ae8a7776981d | -8.88739 | -60.76329 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dea29e34-5c1a-30bb-abeb-bca81d7f4879 | -7.46695 | -61.40231 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40413b01-c6d2-30f9-8f18-93ceaf1cf0c6 | -8.95761 | -65.95518 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3cda6d4f-20f8-3077-a2a4-284582bc644a | -9.40417 | -60.51031 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 54b4a2d6-0cf1-39ab-8beb-a5825cbfa01d | -6.63112 | -53.33408 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed70690d-8578-304c-97a2-70b0e0fbfe9b | -6.78672 | -59.63318 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d430f255-6e27-32cb-9c0c-7b9ad1a5d8be | -6.87404 | -59.89964 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff3083cd-53a3-3c4a-bb0d-6782ed524c83 | -6.3109 | -59.86713 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8eba275-b484-333e-97c6-23cd08c1aa13 | -9.16658 | -59.51139 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14c49fd8-8dcf-3d1e-a989-0884b0cebd03 | -9.07574 | -66.06123 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fde37bd3-c733-3da4-9a2a-12ee8f3964e2 | -8.24229 | -61.45245 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0abc7f58-894f-3cd5-91dd-960a398c61a1 | -9.15466 | -59.58786 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 537a9fc9-56ea-328d-90d0-17dd9ae52c32 | -10.78621 | -47.06145 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| d04d6ca2-08c4-3240-8f8f-5b1cf4ff5d3a | -7.54668 | -57.73641 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c46e70eb-a04d-33b7-bf1e-5dbfc10f233a | -10.1236 | -47.43439 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3a927d6-0af2-3f28-a40f-6f8396fdd7c5 | -6.84022 | -58.96451 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 16cbc776-fbb8-3522-92c0-4e1667a4756e | -9.49642 | -60.55034 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3487d7a-0013-31a6-8dec-8bf17028d460 | -7.66192 | -62.54244 | 2025-08-27 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66ba72fb-4c80-33fe-981e-b330d9d6e513 | -9.4086 | -60.50382 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 9cd4a429-5864-3361-8782-8f3234a4f386 | -9.41578 | -60.52297 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 253febbb-68ac-3e94-9ae7-705385849e8b | -9.1715 | -59.50147 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93a488cd-690b-3a32-ac55-5773b3bcb801 | -6.62584 | -58.55127 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79436b69-cef0-352f-9fc4-a8cfefdd9322 | -10.79332 | -60.78254 | 2025-08-27 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b8df8cc-717e-3627-932c-b5bdd38daf5a | -9.40637 | -60.51786 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e7691c7f-88bb-3554-bf97-9d8304dd7cca | -6.25474 | -60.00879 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 430df1aa-2a96-3b25-9009-e4cde4a786b2 | -9.15953 | -59.55656 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc836997-936c-3295-afc5-c0aabcf7f944 | -6.94457 | -59.51606 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d155be7d-083d-367d-8889-95f910d9f3ec | -11.30476 | -55.11522 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2494cc9-e0c9-3247-8549-a48bddbb156b | -9.40812 | -62.49429 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2070550-2026-3cfb-8442-f6a9bda09035 | -7.4817 | -61.35477 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2446f9ad-970e-33cf-9cc9-50e7ba41a264 | -7.42351 | -60.61974 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7c3427c-bb99-3f5a-963c-c09919b0f354 | -9.40361 | -60.51382 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4a449a8-5b1d-3469-b60d-46c6296001a2 | -10.03002 | -59.35824 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23b913b8-f444-3050-abb2-a681731bff9f | -7.03812 | -59.85063 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0da64fee-406e-3f4f-9399-d9ec62e9a4c9 | -7.1709 | -59.744 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e35affa5-e90b-36ff-a99b-010fc44e76d2 | -9.27277 | -56.90319 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f926f2a5-80c7-3a5a-9f12-8d347743b2e0 | -7.53007 | -50.53446 | 2025-08-27 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef778383-7b92-3f1b-a93b-b73f876e0c89 | -8.95544 | -65.96786 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7f0aff57-0693-364f-9c83-82cc09cffa64 | -9.16501 | -59.54317 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e7d1edc-74ce-3d68-baf7-f53e5882756a | -9.52687 | -60.53 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e46ba47f-d56a-3c4c-b482-fe1731c4a8a7 | -8.89961 | -60.77254 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ff134df-1d94-31ad-822c-264cf4cc3473 | -8.25414 | -61.46588 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 835052b1-e1d6-3e08-8f82-96151398deed | -9.08493 | -65.71684 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78bf30ec-6172-319e-8c0a-1061ac82fe50 | -8.34165 | -62.93121 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f2d6c03-d1cc-3167-83c0-ee0ee18033ae | -8.11057 | -61.48529 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5b533b6-6109-344c-a2d0-eddab6c26fac | -9.23393 | -60.91786 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa2675cd-3040-3582-a1b7-4e39f7784cec | -5.35867 | -60.39892 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b1022c0-dbed-36e4-bef1-b52e8cd8c089 | -8.92725 | -65.92391 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0faa31df-81d7-3db8-ae34-1aa9b8efefa7 | -7.54317 | -61.38766 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2adeab4-bf10-3a41-9ebe-a1609359df93 | -9.70254 | -61.28513 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README58.md)
