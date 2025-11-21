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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d371f1b9-93a3-3375-96d0-de3a0e0707c7 | -5.42621 | -40.67082 | 2025-11-21 03:51:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9a66bac-6df0-3522-8329-b1a88d22e039 | -3.85035 | -43.36428 | 2025-11-21 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10edb55e-8e4a-3799-84c0-3eb074ac00b4 | -4.16885 | -43.68172 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ed29ede6-9a23-36a6-8ccd-0d0828b29d0e | -3.85586 | -43.36012 | 2025-11-21 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b67d77ef-a3d7-315d-9493-1b41e9d66c68 | -8.91774 | -35.17607 | 2025-11-21 03:51:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ce9acafc-7114-345e-a885-f4d8a378e5d2 | -5.73386 | -39.39159 | 2025-11-21 03:51:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d442b89e-7c21-3832-ab49-0d2477cab020 | -4.14724 | -43.69384 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 628ba9b0-935b-341b-99be-614476f7e413 | -3.65225 | -40.82188 | 2025-11-21 03:51:00 | NPP-375D | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b84ff870-4246-3e9f-8366-552ac2a1c931 | -4.16494 | -43.67574 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 508b1b34-86d8-3f38-9f33-c9b0c50f25c8 | -6.79591 | -39.54252 | 2025-11-21 03:51:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f40ba8c7-52a9-38a3-985d-4f141151fe7d | -4.91678 | -40.00541 | 2025-11-21 03:51:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 57b2b8a6-b1b2-3887-a246-5b1e58b60f34 | -6.31281 | -43.81675 | 2025-11-21 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aeec2022-684b-36be-b70f-8785e125bea5 | -3.48653 | -42.09586 | 2025-11-21 03:51:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03c86e0a-f5f8-3915-bbe2-af9856b7a6d8 | -5.502 | -46.3668 | 2025-11-21 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46f05635-a7b6-3d64-b62e-afab3cda018c | -3.14454 | -40.17792 | 2025-11-21 03:51:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f861d3e-1e27-3a38-8f89-6df78ab18437 | -8.28782 | -35.26515 | 2025-11-21 03:51:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 57351b6a-62cc-331e-9b1f-dfad5b3cecbf | -4.15542 | -43.6741 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bdad3ea5-5c78-3333-b2b1-7ae3f36457b4 | -6.23857 | -37.23212 | 2025-11-21 03:51:00 | NPP-375D | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa8edcb3-48f7-3c70-a462-af3bea9eb088 | -4.3713 | -45.52477 | 2025-11-21 03:51:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc70a16c-8090-354b-bdef-80d9524b49b2 | -4.16103 | -43.66979 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d5d0b5e-f238-36c6-8adf-8d46f7689d9c | -7.50452 | -38.33625 | 2025-11-21 03:51:00 | NPP-375D | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3fb799e-eeb4-39ec-9308-0a2111c096b7 | -6.22234 | -48.08098 | 2025-11-21 03:51:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c901e066-d3bb-39c0-ad63-8613bc1950c1 | -4.1697 | -43.67657 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 647e1b43-ea4e-3095-9a90-08c19f08bfd5 | -2.89421 | -41.68932 | 2025-11-21 03:51:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abbf9a10-9308-3f85-aa51-8b076a97322a | -4.14162 | -43.69817 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 269cece6-94f7-3097-8aa5-eb5e5962ee1d | -4.35241 | -38.89489 | 2025-11-21 03:51:00 | NPP-375D | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0092bf15-4d57-3967-ab8b-2e2e44fd9b15 | -6.68031 | -38.48382 | 2025-11-21 03:51:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c348071-73f0-3426-ac5d-45ed18d51681 | -4.62513 | -37.94352 | 2025-11-21 03:51:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a56eb1d1-7046-3a1b-b30b-5ba2ae03926e | -5.75795 | -40.45794 | 2025-11-21 03:51:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ce2713b-a333-3ea5-ae3f-81f39d7eca0e | -3.96752 | -38.55331 | 2025-11-21 03:51:00 | NPP-375D | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a41177cf-f882-3f96-b3aa-03e705602346 | -4.15066 | -43.67329 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c94e44d0-bcb2-3227-b61a-1040277456f0 | -5.69494 | -35.33421 | 2025-11-21 03:51:00 | NPP-375D | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 02fb3bae-37b8-3a24-b1f6-95dbb7890c60 | -5.98292 | -42.08338 | 2025-11-21 03:51:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63176378-c349-341a-80ce-e70b37239084 | -6.03954 | -36.78409 | 2025-11-21 03:51:00 | NPP-375D | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 302e1d08-8df6-3f41-92cc-89be36ca90f9 | -6.21745 | -48.07812 | 2025-11-21 03:51:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b050d405-ca6b-3238-b208-b2eaa496c9eb | -4.17055 | -43.67141 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c5a98f4c-907d-3d3f-a5c4-f6c18e58f2b8 | -5.4922 | -39.16591 | 2025-11-21 03:51:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3d03c801-a7f9-34be-a4e5-b6d78c86144b | -4.14504 | -43.67761 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c732b64-2941-301e-a51f-32c9cc311eb3 | -4.16409 | -43.68088 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9752f705-af6c-30db-b753-b973ab661fed | -4.14638 | -43.699 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a847ed83-e571-3e58-a20f-24f110441847 | -3.77791 | -43.94551 | 2025-11-21 03:51:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f58d0d1-141e-3ae2-b96a-d9ac804e5fba | -5.82598 | -46.48302 | 2025-11-21 03:51:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9abca05d-5cff-3af9-bc8f-7810d6f04243 | -4.16579 | -43.67059 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| deae4e2b-1718-3b37-b858-df7a09742bd0 | -7.11001 | -35.12218 | 2025-11-21 03:51:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7bf918a1-905d-369e-900f-95d6c6f21ff8 | -3.14628 | -40.18025 | 2025-11-21 03:51:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0a5cbf5-dd2d-3a71-a869-34b4a8682b5a | -4.16018 | -43.67492 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c8c3f31e-40e9-38fa-8a03-71ad9beee62c | -3.43142 | -44.3698 | 2025-11-21 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e16804ab-7f27-3334-a8e4-0089a7adee91 | -4.14981 | -43.67843 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 645a6c1e-f48c-3e39-8600-110169dbf477 | -6.00241 | -39.51411 | 2025-11-21 03:51:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6fc7fd4a-399b-3ceb-a012-b4aa0c78f0e8 | -4.37667 | -45.52577 | 2025-11-21 03:51:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6029975f-548a-369a-b705-93e82730235f | -2.89483 | -41.68541 | 2025-11-21 03:51:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8048715-4435-3e9c-8529-f4efd7d744bf | -5.42545 | -40.67551 | 2025-11-21 03:51:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6833f0fd-8d71-3f4d-b901-dd03e6f47b44 | -4.37187 | -45.52142 | 2025-11-21 03:51:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c17d4fdf-2463-309d-afee-aac2fed42c50 | -6.31425 | -43.81853 | 2025-11-21 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ffd12e9-55dc-3e5d-91a8-36a891e05672 | -3.99731 | -41.05485 | 2025-11-21 03:51:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2b4f9441-dd4e-31c2-ab1c-4d940bf04273 | -4.24399 | -39.74343 | 2025-11-21 03:51:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a2c47b2-2fa7-3684-8084-cf94586f4981 | -4.89299 | -42.08305 | 2025-11-21 03:51:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ea7b455-afc4-3990-898c-2507332a0a76 | -4.24328 | -39.74778 | 2025-11-21 03:51:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eafe36fa-4867-33a7-8abe-9ef410e5af1c | -4.15627 | -43.66896 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31466a5c-fb18-3c45-bb6f-a8b32822d83c | -5.50265 | -46.36309 | 2025-11-21 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca73a3be-a263-3e54-8d4a-4bc0bcf3ff40 | -3.20557 | -39.58985 | 2025-11-21 03:51:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2c82a759-e3e4-3fb6-84fe-f4ef4384b18b | -4.43162 | -38.67217 | 2025-11-21 03:51:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5e1a65bd-d9a6-346e-a6fe-323922227f38 | -5.16983 | -35.85871 | 2025-11-21 03:51:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c133400-4b61-3347-ad6c-30096ab08a58 | -8.9202 | -35.17334 | 2025-11-21 03:51:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 64ed63e2-9b0a-3307-81e9-24c2818bdba2 | -4.46206 | -40.81324 | 2025-11-21 03:51:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eb81678c-78a7-3197-9e76-9b5284325c5f | -8.91961 | -35.17715 | 2025-11-21 03:51:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a08b9061-783f-34c6-b001-000996d2e9ef | -6.31967 | -43.81464 | 2025-11-21 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aea6eff9-b375-375b-a1be-6283b7b76bfa | -4.89233 | -42.08694 | 2025-11-21 03:51:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7e81a727-1b5c-319a-82e9-efe4cf580b8e | -2.89389 | -41.68496 | 2025-11-21 03:51:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed553a81-e6fb-34f7-8344-91acaa5fc57a | -5.75213 | -45.11298 | 2025-11-21 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cf38cb5-ad11-38dd-89ad-31ed1c299ec1 | -6.22358 | -48.07938 | 2025-11-21 03:51:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72d437b2-ff87-3e72-a462-6f89fda36342 | -4.04691 | -46.03519 | 2025-11-21 03:51:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4ddab55-c70a-3b0f-9b86-adec1a6b6649 | -4.14419 | -43.68275 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c458f53c-4086-3d8e-ac4a-a9cee61d7c32 | -6.31198 | -43.82144 | 2025-11-21 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f75d0023-fa75-34db-99e6-703dae88f919 | -2.89059 | -41.6847 | 2025-11-21 03:51:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae91127a-c0df-3e5e-b669-a41f4f3dd01d | -6.31827 | -43.81285 | 2025-11-21 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4b3942e-f945-37a7-8be7-2b24b4b3426f | -6.79881 | -39.54702 | 2025-11-21 03:51:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 203b46f1-19e6-31e9-96cb-d2877f59bfa5 | -2.84347 | -40.10791 | 2025-11-21 03:51:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3366f071-18ba-3d20-bd2e-4096b57c8c7d | -6.03899 | -36.78755 | 2025-11-21 03:51:00 | NPP-375D | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 60170f72-e3ea-3b17-a710-86a439e369da | -4.89047 | -40.44588 | 2025-11-21 03:51:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8834e452-a44a-3d66-9ac6-ccd7c8227705 | -7.66122 | -38.38651 | 2025-11-21 03:51:00 | NPP-375D | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 80a009c4-de2c-3090-bec0-1dd3cfbca481 | -5.7332 | -39.39563 | 2025-11-21 03:51:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1cebd2b5-b43c-36d2-9916-3134cc04f5da | -5.42698 | -40.66613 | 2025-11-21 03:51:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dd67cebf-87c4-313a-b830-49c5fcca9086 | -4.1459 | -43.67249 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 126b7677-c024-370c-b4be-cc5e07113c87 | -4.37724 | -45.52237 | 2025-11-21 03:51:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9fb70e8-8915-389f-a5fa-54b54cad98a1 | -5.74758 | -45.10879 | 2025-11-21 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c10b34f-91f3-33f6-8383-5ec2ae5e7842 | -3.14245 | -40.17965 | 2025-11-21 03:51:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ce0f548-3dd0-3aa4-93d4-b248689aba0f | -5.17038 | -35.85523 | 2025-11-21 03:51:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb42f30b-0a05-31c4-a1a2-92673b4c658c | -13.70718 | -48.43221 | 2025-11-21 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 411414a1-5ff1-3bf7-b6c8-995de5c0fad1 | -13.73713 | -48.45521 | 2025-11-21 03:53:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cc835ac-24f7-33d9-b843-bff8eb38c19c | -13.79028 | -49.57977 | 2025-11-21 03:53:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 392e4ac3-6741-3e63-a3d6-b1e1bc845e17 | -14.51699 | -49.33956 | 2025-11-21 03:53:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5ab97e9-2a8a-37fe-96e6-1fbd769cfb62 | -13.7009 | -48.43481 | 2025-11-21 03:53:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6640388a-769a-3d3b-8f71-a68974e34679 | -13.78435 | -49.57854 | 2025-11-21 03:53:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 047628ba-e11d-3402-9286-59e7b632f2b2 | -13.73548 | -48.46352 | 2025-11-21 03:53:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba05318b-fb94-3ce2-b5aa-7023c209ceb2 | -13.70642 | -48.43599 | 2025-11-21 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6b5eb5a-8d52-3419-b005-21eb1d931547 | -14.52356 | -49.33685 | 2025-11-21 03:53:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 390dc8a9-a3bc-3dfe-9e6b-43aca8b3f29f | -13.70791 | -48.42854 | 2025-11-21 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc72f75f-7eef-319c-9780-00efcbe1fc3c | -15.44427 | -43.83551 | 2025-11-21 03:53:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92e257f1-639d-38cc-b7cd-6a2a2a2a465b | -13.70248 | -48.42692 | 2025-11-21 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
