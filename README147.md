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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28ba9eb1-09a7-38f1-865b-30877b2432af | -20.57636 | -51.39388 | 2024-10-05 05:33:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3c20d436-4dfa-3304-8746-08b7b98e8b7a | -18.78804 | -52.63046 | 2024-10-05 05:33:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37d37cfd-4be5-39ba-8994-e4e4099f203d | -18.78757 | -52.63588 | 2024-10-05 05:33:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a82d357-9962-3972-bc53-0309c42e7c7d | -18.7859 | -52.63042 | 2024-10-05 05:33:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0732f47-d1bf-362d-a7a3-1ca193b9c4ec | -18.7854 | -52.63585 | 2024-10-05 05:33:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 273c5a20-502c-35f3-92e4-94e613b7eee5 | -18.51599 | -52.8557 | 2024-10-05 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3e2a61c3-8e9c-3877-a772-2c1aa7f6ba2a | -18.50974 | -52.85484 | 2024-10-05 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 66aa4a04-e146-34f2-bd8b-7efaf9368b73 | -18.50396 | -52.84885 | 2024-10-05 05:33:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06aeaaae-4249-39dd-8b11-e14e45516677 | -18.50348 | -52.85401 | 2024-10-05 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e752f4c5-fab3-3dc3-aaac-5689d0a99c73 | -18.4981 | -52.77419 | 2024-10-05 05:33:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ab14e874-9544-300e-bc6d-8b998b266765 | -18.49762 | -52.77941 | 2024-10-05 05:33:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2f097471-c486-328e-96c8-e20a5fdf50e4 | -18.49722 | -52.85324 | 2024-10-05 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3efc0c51-3f5a-3278-ad22-b67ed5e9630d | -18.49674 | -52.85844 | 2024-10-05 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 365c5390-90e4-3fb4-807f-35c6184c669a | -18.49132 | -52.77878 | 2024-10-05 05:33:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2158e950-ecb1-38ba-b2bc-4a14bc966e23 | -18.49046 | -52.85789 | 2024-10-05 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9feae2ca-e623-32d5-aca2-5f975bbcc962 | -18.48999 | -52.86308 | 2024-10-05 05:33:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9e88e63a-97ba-3383-b6a8-bd2851fcdec1 | -18.88779 | -54.53711 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40f3596e-86cb-33a6-97f3-5916cc1a965d | -18.88216 | -54.53605 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5001645b-7012-3e35-8174-42ceb8caa732 | -18.8768 | -54.53222 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6f614d4-1797-3467-84b7-a2a511c4b582 | -18.87645 | -54.53571 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eeb58a31-dd92-37ef-8dab-732309a0f50f | -18.8761 | -54.53921 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 84ad5c89-b968-308c-9e8d-8ba1be9ff099 | -18.87576 | -54.54261 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f91f54a3-d447-3ca8-8532-32e01e5c0ac7 | -18.87004 | -54.54237 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1abc2e06-185b-322a-9802-851924c3521c | -18.86476 | -54.53774 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0f16cdd-73e0-31f2-81f5-c30303cc0934 | -18.86441 | -54.54123 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c97d72a3-4615-3de5-8ea1-5d74c54ca2fa | -18.86407 | -54.54472 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4cefee3a-2205-366f-9fab-aa123f935cc0 | -18.86043 | -54.52346 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 056d24ba-7781-350a-a56b-d9e45bebca54 | -18.85479 | -54.52237 | 2024-10-05 05:33:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74f20377-bd08-3f31-87f5-e79a83eaec2a | -18.85415 | -54.47019 | 2024-10-05 05:33:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20cdb029-6d16-3450-ae59-3e5bbf283bbb | -19.66594 | -56.45361 | 2024-10-05 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ae5e0b82-d40c-38da-b48e-70bf22e20749 | -19.6656 | -56.45671 | 2024-10-05 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 881da360-1914-35c1-b9dd-ed20dfeb26df | -19.66088 | -56.45297 | 2024-10-05 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dc50a937-8e24-3365-9166-07ed89344824 | -19.66054 | -56.45607 | 2024-10-05 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0c9c3319-778f-3ff2-9152-45ff20f9184f | -19.6602 | -56.45918 | 2024-10-05 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7dabcce7-2cc7-3bf5-bb0c-413c9b7c42d9 | -19.64605 | -56.49498 | 2024-10-05 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3c3a721b-cab0-3b47-aafc-9c85cb69cb3d | -19.64134 | -56.49126 | 2024-10-05 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6dd0010d-9935-371c-938b-43a7937dd833 | -18.6637 | -57.28535 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 3e87a1a4-674a-31c7-916e-b5b54488b4cf | -18.6631 | -57.29062 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| a345ffa1-793b-3625-88ac-877c944fffd0 | -18.66016 | -57.27414 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| bd9c7f7a-8f13-34ab-bea3-a2fb3732a693 | -18.65957 | -57.27942 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 60fda4c1-1713-3190-87af-7d5e372a02a3 | -18.65897 | -57.28471 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6855dad6-7555-3fc2-9209-e61e008b7d1e | -18.65484 | -57.27878 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 9b63b179-804d-3b72-abed-6a9059f2cf08 | -18.70152 | -57.29041 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 804658aa-d82c-32f6-a71e-66ce5ed356ad | -18.70091 | -57.29569 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 68928035-fc9e-3cba-952c-88cd211b1b39 | -18.69741 | -57.28448 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| e2873689-f4a6-35ea-8a20-39da016cfda2 | -18.69679 | -57.28978 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| a2f65a65-e4cf-34ed-a1cf-cf68a5c42a8c | -18.69268 | -57.28386 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 7e4b4455-6ead-3493-aeac-8b1725bc7312 | -18.68855 | -57.27794 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 3ba068bf-8e37-3d27-83df-6d87962b0ae6 | -18.68795 | -57.28323 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 68171378-da25-301e-bb1c-1e60ec8a7f28 | -18.68382 | -57.2773 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 5f3fee1e-8cc9-3e02-ac1f-24ab9244c4a3 | -18.68322 | -57.28259 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 96427207-b9e0-3f24-b981-6ff241b524f9 | -18.682 | -57.29315 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| eb7bedcb-e514-3a6f-ad2b-dcb37a92d2ce | -18.67909 | -57.27666 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 810b5a61-582f-3e43-af9b-2f140bde92df | -18.67788 | -57.28725 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0afa2e01-0d46-32b1-92ec-da58e00a3735 | -18.67436 | -57.27603 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 0d1e1f48-a5b4-37d5-9bbe-30684f5d35b5 | -18.67376 | -57.28132 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 88620481-767e-3423-9ab1-b79ddd204f0d | -18.67315 | -57.28661 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f8509697-01c1-3003-bdbf-7989dd70ada1 | -18.66963 | -57.27541 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 5c6ef456-80ac-3eff-8c10-fd64d95b1307 | -18.66903 | -57.28069 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 2280eb70-d78c-3ced-ac58-c284549df598 | -18.66842 | -57.28598 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b910d1fc-82f1-3243-a502-bb510da949aa | -18.66783 | -57.29126 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 12c75f93-3228-3f88-b325-e3663f6ac50b | -18.6649 | -57.27477 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 263cffbe-e73a-3d7f-9cae-5d115e29981b | -18.6643 | -57.28006 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| e368874c-f3c7-3d9c-b3ef-0f4b6b09267a | -18.65424 | -57.28407 | 2024-10-05 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 17ae598b-8c20-3ead-b23b-61cabac6ce05 | -7.01488 | -59.40364 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fcc3a8d-b74c-3ad7-9a0c-ee3673a00938 | -7.0118 | -59.38636 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f46e49f-67ac-3ddb-8450-0e1fa5827e05 | -7.00691 | -59.38216 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1086166-70b2-3982-a9ee-a0cef38e93b7 | -7.00645 | -59.38554 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 020f9f5d-cb5a-36d8-8940-c94e1315f6ff | -6.91717 | -59.45481 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efa7abb5-addc-3df0-aae5-921fda9457bd | -6.91231 | -59.4507 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51d879c7-3abf-35ad-b3d8-f5b4e62d1c1c | -6.79128 | -59.3613 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6c21f54-5107-38f0-b9c9-44dc1fb78f83 | -6.79083 | -59.36461 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2cf2834-9bc7-33f0-be5e-22cae2a03e42 | -6.79038 | -59.36792 | 2024-10-05 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3040d1c-3a0d-3de0-bbeb-d30fa608f09d | -6.82228 | -60.05913 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 712c297b-c957-330d-b673-aedb45de8e5a | -6.82185 | -60.06218 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f02d8e1d-f913-3379-9a5d-a68b472446f2 | -6.81762 | -60.05523 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0ed24d7-9889-3c98-8d61-58f5c9ba1d57 | -6.81718 | -60.05838 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82adfb50-f0dc-3091-8637-aee216476388 | -6.81674 | -60.06152 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5254653-b19b-3e4e-a56b-b467b8e2b99c | -6.70949 | -60.1049 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cc4c6c7-e10d-33a2-91f5-6aa91781325d | -6.70441 | -60.10417 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73c714fd-8cda-337c-b0e9-b45fe71d55b4 | -6.64694 | -60.04644 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ff1857b-64de-387f-a588-9b77fcd27dd0 | -6.64609 | -60.05244 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a80f0ab-d233-3a3c-be78-4b6e3c166602 | -6.64186 | -60.04566 | 2024-10-05 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ce8c134-9ceb-332d-9215-d35d892a8448 | -9.27811 | -60.83144 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21c2e519-abce-3cd4-b59a-a2243919c4bd | -9.27309 | -60.83079 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81beb340-43fc-32ca-ad02-e580c6bc5757 | -9.26744 | -60.48025 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61b714a7-973c-3ccb-95a9-3c22c08550e4 | -9.26704 | -60.48334 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f8b51f9-1023-3ee0-9c76-ec056634a205 | -9.26548 | -60.48297 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b377c74-609e-3863-8702-81abb6965307 | -9.26505 | -60.48606 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 689b0b11-4a47-3d56-9203-c7748c7fbcff | -9.26466 | -60.50177 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 787762de-f154-3bb5-a898-172f4fd1edbc | -9.26296 | -60.50136 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 378b5731-4cb0-3478-a95f-46070e11572c | -9.24473 | -60.44276 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b0ee4368-7651-3bc9-b047-8ad4b4da569a | -9.24432 | -60.4458 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b7d3faf-8580-3bd5-ada3-4ba776d6c6f8 | -9.16825 | -60.50672 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be6c69ce-28b0-338e-b05b-e3ef7847b7a2 | -9.16785 | -60.50979 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b61340e-cbdc-3db6-b660-9ebd034380c0 | -9.16745 | -60.51286 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24433978-640c-31a2-928c-d2d608464337 | -9.1653 | -60.50904 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d1b303b-6d54-3112-8571-9729ada54949 | -9.16488 | -60.51208 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a5475f-71a7-3278-8f15-f11f67249a3f | -9.16233 | -60.51215 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4366c184-3a18-3b91-b069-3d246089050c | -9.15975 | -60.51142 | 2024-10-05 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README148.md)
