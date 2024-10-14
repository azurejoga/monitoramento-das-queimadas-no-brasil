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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f4dacf6-0fff-3ba4-9079-2897c5152f18 | -17.94192 | -57.34837 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 035e2fa6-9482-38bf-9c51-9ed522d068d1 | -17.94192 | -57.32319 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 5b8a2830-290a-3917-8238-4e92030028f3 | -17.94134 | -57.35247 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 7b4eb82a-d871-3f34-97df-00dfac01bc46 | -17.94075 | -57.35656 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 13a606af-831c-3e72-9eb1-9ac88e29f6b9 | -17.94075 | -57.33141 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| edaed03c-f264-3429-9d2e-e87fdda88c87 | -17.94016 | -57.36066 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| f4863aff-781a-3f52-ae0e-951bdf6f44c5 | -17.94016 | -57.33551 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.9 |
| d614f44a-3cac-3c30-8e66-b3e1e7fb6dff | -17.93958 | -57.36476 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 67bc796a-0449-380d-b58c-230f0029d66a | -17.93958 | -57.33961 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 2094546f-34cc-3623-ad12-c4ecdb951006 | -17.93899 | -57.36885 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ad39cd10-18fc-39ed-a4b1-720fc0cf5007 | -17.93899 | -57.34372 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| c5d1b4b4-6db3-31e9-83cb-0277d5c3e768 | -17.93841 | -57.34782 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 1d7d221a-7321-3764-9d5c-53727485f3ed | -17.93782 | -57.35192 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| c70653a3-b671-33c6-91b1-140160b4335b | -17.93723 | -57.35601 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| a42daa56-3940-3c94-baa0-fa37eb26dc90 | -17.93723 | -57.33085 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| adcb3afd-d9c1-3eb8-b137-b28b0c5b3d1a | -17.93665 | -57.36012 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 74552a16-e15c-3279-8eaa-bdb56c824f7d | -17.93665 | -57.33496 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a0961a9c-4676-3ac7-9812-34335cd1239a | -17.93607 | -57.36422 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 0ea93c8c-1b64-335b-8fbf-37067ed941be | -17.93606 | -57.33907 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2463013d-bd5f-398e-9367-f6db9ca781fd | -17.93548 | -57.36831 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0602fd26-443a-319c-b653-25270ef38d17 | -17.93548 | -57.34317 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ba05e311-30d8-355c-b883-8f39ef6ec3eb | -17.93489 | -57.34727 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 00be51aa-4e82-354f-a9d7-4ce9e8a50ec2 | -17.93489 | -57.32209 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 53994a96-5824-3bf1-9389-6bf1d3682283 | -17.93431 | -57.35138 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ab168cee-da4c-3e07-a124-ebb138b31bc9 | -17.9343 | -57.3262 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 16be87c6-be3c-3ceb-8482-e7af70582e32 | -17.93372 | -57.35548 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 09e4916e-c5c5-3311-85ca-9395e4a4c0d6 | -17.93372 | -57.33031 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ae4ebdcc-265c-333b-be55-b1054e98fac7 | -17.93313 | -57.35958 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.1 |
| 0f85493c-e45c-34f2-8dd7-58416cf6532c | -17.93313 | -57.33441 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c8f6c6c5-9bea-3a80-b310-89e3e1cb2038 | -17.93255 | -57.36368 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.1 |
| 277177ec-641b-3464-b95b-50ee8b67c6ec | -17.93254 | -57.33852 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6e5bed29-b2d9-3b76-87ac-b9828a51542d | -17.93197 | -57.36776 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| a0f505b8-23ca-301f-8baa-28bd27573476 | -17.93196 | -57.34262 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b9f990c2-9bca-3e68-b29e-2819a9440e2a | -17.93138 | -57.34673 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fa469c93-e798-3ac3-9b6a-608b21820f4a | -17.93137 | -57.32155 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5d1c15aa-45e7-33a5-bed7-b207312367e9 | -17.93079 | -57.35082 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| bd0e708f-51fe-336d-a54a-91a9408be067 | -17.93021 | -57.35493 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d3b48f11-7a81-32bd-aaac-4e274fde28ec | -17.92962 | -57.35904 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.1 |
| 2ee6dec2-2010-392b-b90c-cff51a057321 | -17.92904 | -57.36314 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.1 |
| 98005450-0bf5-36a5-846e-79ee6db26f74 | -17.92903 | -57.33797 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5d35d01e-d679-378a-b21c-6a94c545bfb5 | -17.92845 | -57.36723 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 87f42cf1-6cd8-365d-b19c-fff2b29ea63f | -17.92786 | -57.34618 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| cbd294a6-74b9-35f3-b608-34e485db7df1 | -17.92728 | -57.35028 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b27a5b96-f966-3e30-a4d3-0b22ed0e2ae5 | -17.92726 | -57.3251 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 63ee4187-195f-322e-b395-9d3846624634 | -17.92669 | -57.35437 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5c072e19-c6a9-3ded-a1b5-19b68ff02204 | -17.92611 | -57.35849 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| a8ecfa5f-2d78-34a4-95f9-c425fcc2932e | -17.92552 | -57.36261 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| c1529bb3-f3f7-3e7a-9b04-639350e3ea7c | -17.92494 | -57.36672 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 29654c70-8cd7-3b6b-94bd-a628331c93ad | -17.92376 | -57.34973 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 72fc811a-b763-3ad4-9d8d-11e94a380e8c | -17.92318 | -57.35383 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b42776bc-a884-3d41-aa83-5e117c7ec7ee | -17.9226 | -57.35793 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| e494bd85-7b32-3621-87fb-00927b5703a4 | -17.92201 | -57.36207 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 1526e452-73ae-3df0-ad2f-a94521abf3f1 | -17.91908 | -57.35739 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 024fc0f1-270f-36d2-9255-6458b828be67 | -17.91906 | -57.33222 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2db760ca-0510-351e-9192-4c941b56cae8 | -17.9185 | -57.36151 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1ff5b465-0ea9-3988-ae1b-8e9b95389ac6 | -17.91791 | -57.36565 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ce199474-11cd-322a-a602-582b297ef19e | -17.91615 | -57.35274 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 93bec6e8-c8c7-341e-9bc6-61af00752d2f | -17.91613 | -57.32757 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3b1f0206-c6f8-30d0-9cda-fbb289b05803 | -17.91499 | -57.36093 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e1524d93-25bb-3b4b-8d66-60f2b0f11c4d | -17.91496 | -57.33578 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 381bd8fc-7477-3137-8758-2a7933c9a6ba | -17.9144 | -57.36507 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4f19688c-5f64-37b8-b61c-cbf17a60de34 | -17.9138 | -57.36929 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7504df47-b655-370b-978c-8bfe9794876b | -17.91089 | -57.36452 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 0add9a75-e3f9-34f6-944a-9f1e1c729239 | -17.9103 | -57.3687 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| eb0fd935-d797-3469-b24b-8e03a2836ca8 | -17.90967 | -57.32236 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bd6b95f2-7565-314f-baaf-4fb3ae527ce5 | -17.9068 | -57.36808 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| e50224b5-6dee-385d-850e-584291550ece | -17.90622 | -57.37218 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| ddf699d9-974d-3be8-a5ee-edaa1567e8de | -17.90329 | -57.3675 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b0ec6f1c-bd81-3b48-8df4-2fb2e8c93315 | -17.90271 | -57.3716 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| af927e5e-4551-3945-8204-ecfcf5114577 | -17.90213 | -57.37566 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 931aaaac-96bb-39b0-ab4b-695122d6b955 | -17.89978 | -57.36694 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6c686e25-a81e-33c0-b045-9fa2a9f2df5c | -17.8992 | -57.37103 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| a27ec47f-8a51-37e5-9dc5-1f0b8816c9e5 | -17.89862 | -57.37511 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| e43a0a3c-e3c3-37f6-bfde-e7e4f22f2fd3 | -17.89685 | -57.36227 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 403f223c-4978-3396-86be-8ca47537d832 | -17.89627 | -57.36637 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4de8abe8-a608-38a3-9572-5a3629928ab3 | -17.89569 | -57.37047 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 4202b7d0-f3a2-3c00-a86a-b8c420b0049b | -17.89511 | -57.37455 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 9abbc209-39de-31fb-bed6-eb0539374535 | -17.89334 | -57.36172 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 04b5db3f-fe6a-38ca-b943-fb6ac27c59ad | -17.89276 | -57.36582 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7d157018-17ce-33c4-a0d6-aef6b00e690c | -17.89218 | -57.36991 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| fde74152-0e60-3959-ad73-88c27d0c9b51 | -17.89161 | -57.374 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 4b5d2bd5-86c9-3513-9b8d-568c1aa3d055 | -17.88983 | -57.36117 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cbc05bd4-7c5c-3e5c-b55f-8e8773e2de56 | -17.88965 | -57.35788 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4c2c4d72-cc16-3a51-ae1b-f95a481ac361 | -17.88905 | -57.36197 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c62f1a4e-d562-31f2-9e81-3c1093930549 | -17.75459 | -57.11884 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 89538ddb-1ac6-374c-83a6-46c6208dfaa9 | -17.73982 | -57.12083 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 45f7277a-3ca5-37a5-891e-53f77106b078 | -18.00221 | -57.38156 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 871b053f-e803-312c-adf4-f65ab101a8e7 | -17.99167 | -57.37706 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6feef7c5-0a78-3441-9566-5af1e302e76d | -17.98286 | -57.38824 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| df48abfd-5a39-3efc-a87a-f1b8b1db2e38 | -17.97644 | -57.38306 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2cd90857-c9ec-3491-8299-631c32a0a4fe | -17.97585 | -57.38715 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 09851132-8561-3bee-91b6-6436a94f6ac4 | -17.96354 | -57.39776 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1ba90912-3cdb-3837-bca7-12c029605b88 | -18.00689 | -57.37392 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1a1775a9-4618-3677-af55-07b3aa210638 | -17.99986 | -57.37282 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 46c22665-261a-397b-8a2d-ecd3cc3fc802 | -17.9987 | -57.38101 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a81b58da-6382-3413-a455-558d7493fcbf | -17.99519 | -57.38046 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bc19ac78-f55f-39df-bde3-044385f96668 | -17.99459 | -57.38169 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 82e551bb-4fe4-35ed-ad0a-3880973da72a | -17.98405 | -57.38006 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 722110a9-ea79-32a0-ab06-6181813760d0 | -17.97233 | -57.38659 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 603197fc-10c2-3c4f-b844-b948b70ed5e9 | -17.96997 | -57.40294 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.5 |


[Clique aqui para ver as próximas entradas](README117.md)
