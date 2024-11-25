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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7900a15e-68a7-39a3-8293-ab4d97056e1c | -5.58451 | -45.20812 | 2024-11-25 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e0161d7-f708-32de-a0ec-d4f618f8ed13 | -3.67838 | -45.8942 | 2024-11-25 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bec8b588-9aa2-369f-9b06-4b97a6e98eab | -4.80109 | -40.69498 | 2024-11-25 03:40:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a7a9162-a1b0-36f6-8ce9-0464cfb3e437 | -5.8194 | -39.21662 | 2024-11-25 03:40:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0b34ce9d-682b-35bf-8f18-60780fbc59b8 | -3.15601 | -45.4811 | 2024-11-25 03:40:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bab1c92b-28f5-3a01-968e-ce6f11e2c730 | -4.54055 | -43.56627 | 2024-11-25 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3161b1c4-c94c-3e68-bc9b-a9362e8ccb11 | -5.81634 | -39.21125 | 2024-11-25 03:40:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b430cfa-af41-3071-9996-dd1337894dac | -4.54059 | -43.56663 | 2024-11-25 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30ef9a96-674c-3a00-915e-a6a82841bec9 | -4.1676 | -46.81766 | 2024-11-25 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4987860f-d65d-345e-bca1-fd016eed83bf | -4.54459 | -42.89102 | 2024-11-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de8fcf5f-c951-3974-ab3e-487322b40c6f | -5.65832 | -35.27483 | 2024-11-25 03:40:00 | NOAA-20 | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0fd49202-4735-3d53-8e22-f7afcd75155a | -7.43428 | -37.55466 | 2024-11-25 03:40:00 | NOAA-20 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3fb1dfbf-ac2e-3541-99cc-2aaab3eabcb0 | -6.64548 | -43.5933 | 2024-11-25 03:40:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5508ccaf-5ad4-3ab6-bcbc-f811a2e3272b | -4.14857 | -44.28806 | 2024-11-25 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a62844ea-e1dd-3358-a4d1-e22bea1a2682 | -6.80819 | -34.91842 | 2024-11-25 03:40:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c84d10b8-4583-3e07-bf3f-d4fda4c201e7 | -4.31403 | -45.89594 | 2024-11-25 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c3b3c69-a844-38b3-8b3a-41bd27395578 | -8.89954 | -35.53014 | 2024-11-25 03:40:00 | NOAA-20 | CAMPESTRE | ALAGOAS | Brasil | 2701357 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a74c21c4-79bf-367f-851e-d44466c04cdd | -4.31302 | -45.90178 | 2024-11-25 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f32d5162-ca9d-31ff-b7d2-d04593d0b775 | -4.30692 | -45.9007 | 2024-11-25 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebb7934d-3035-3852-9c32-909d19f0a645 | -3.8157 | -41.0119 | 2024-11-25 03:40:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7b9c471f-4ddf-397c-8766-d094ef036a8b | -5.82016 | -39.21187 | 2024-11-25 03:40:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d539b66-eaa9-3e15-be22-2d4c8f17d9e5 | -8.84306 | -35.17471 | 2024-11-25 03:40:00 | NOAA-20 | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d0dec75a-2b0c-34ed-afbf-fb6011880bfc | -4.54516 | -42.88868 | 2024-11-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ace7edb2-c635-3cd4-b179-0e04f38b6c20 | -10.82504 | -37.41487 | 2024-11-25 03:40:00 | NOAA-20 | ITABAIANA | SERGIPE | Brasil | 2802908 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a7c8155d-7f7d-39b7-8d0f-73e231b39ae9 | -3.29555 | -45.74003 | 2024-11-25 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 92e0bd91-2473-3ae3-98d3-caaf6794de25 | -7.35313 | -34.90812 | 2024-11-25 03:40:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7131bf59-6bb1-3846-8de8-008d731c9279 | -6.18293 | -35.2869 | 2024-11-25 03:40:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 23f01330-7ac0-3459-9a8d-3b5db8e189ae | -4.54468 | -42.89144 | 2024-11-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c91326b-35b8-3e6c-a90a-63d3b4e254c7 | -9.31593 | -35.94936 | 2024-11-25 03:40:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 76c90562-3d9b-3653-9a15-a879a9dd22b5 | -4.5801 | -40.77719 | 2024-11-25 03:40:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e4d84c9-7d97-3e2d-b51c-db3a12417322 | -6.7345 | -34.97776 | 2024-11-25 03:40:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a3e1638b-c311-31a1-8390-ff88e08cdf11 | -4.3191 | -45.90301 | 2024-11-25 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 009b60f5-b05c-3a42-bb39-5d70448b867e | -3.28943 | -45.73886 | 2024-11-25 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e4575e1c-cc46-326a-aa2d-54eebb087206 | -4.81173 | -45.75877 | 2024-11-25 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 421d49a5-eae1-3fd2-8fd4-5f193aa3fba5 | -6.99238 | -39.2505 | 2024-11-25 03:40:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0c982c55-d041-3c6c-b24e-a2a0b1b01e61 | -5.57075 | -39.36416 | 2024-11-25 03:40:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e2af4b7-154a-3bce-9691-f74e755e16aa | -4.31651 | -38.12658 | 2024-11-25 03:40:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a1fffbee-b7cb-3a0c-8fd0-408269bd0a13 | -2.79194 | -45.47718 | 2024-11-25 03:40:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9af4226b-9d1c-3a35-b296-991da3f2d277 | -3.29022 | -45.73416 | 2024-11-25 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 19e9e817-c599-3cc3-9cf1-94a996628ab8 | -7.6693 | -35.18899 | 2024-11-25 03:40:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c9d78fad-148d-3f07-9352-6027c30b69ff | -5.1315 | -46.1954 | 2024-11-25 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3c0d265-66bc-385b-95e7-5b0d1552c3ba | -4.58184 | -46.09413 | 2024-11-25 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d78d849-c186-30e0-8577-bb5b1c5013a6 | -5.8184 | -39.21423 | 2024-11-25 03:40:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a6a73156-ba83-3395-9173-eadde0648c51 | -3.39611 | -44.74868 | 2024-11-25 03:40:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e540aa2-46a9-3918-a6cc-1166305d4492 | -4.57777 | -40.77544 | 2024-11-25 03:40:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3c8d4260-0322-3870-88d5-2c30439651e0 | -5.58381 | -45.21212 | 2024-11-25 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f509286-a25f-39be-9145-481157c79b55 | -2.79117 | -45.48179 | 2024-11-25 03:40:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96e6d5e7-d1a1-3414-a8f8-c1b75aada48b | -4.19158 | -42.97648 | 2024-11-25 03:40:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad2a0d95-5878-3b99-8306-15604c6813a6 | -4.32011 | -45.89714 | 2024-11-25 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f3cade9c-0173-3409-9b4a-da7cc523ad40 | -7.35259 | -34.91159 | 2024-11-25 03:40:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8e3b43f9-7e46-388b-9de9-be44a61c7d57 | -4.54505 | -42.88825 | 2024-11-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c98ce6da-a28b-3202-b9ce-29bb031392dc | -6.78124 | -35.37124 | 2024-11-25 03:40:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6c091f53-ba34-3034-b659-ed5b9a8aaad0 | -4.14468 | -38.35248 | 2024-11-25 03:40:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f07bf0f-4be8-3e0f-b502-bcd88aedc83f | -4.86032 | -38.37973 | 2024-11-25 03:40:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| afe34777-c8ae-3872-bf19-260c2549d5bd | -4.14305 | -44.28712 | 2024-11-25 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cae0e111-1e1f-33cf-9326-6027bcef665a | -4.81024 | -45.75621 | 2024-11-25 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6834018c-f16f-3308-a2e6-7e73baf149e2 | -3.29101 | -45.72949 | 2024-11-25 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e48acde8-7ce5-324f-8780-853c0a224df8 | -7.34705 | -34.90362 | 2024-11-25 03:40:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3de30b80-fa6b-3a38-9c78-ff915bc8ff87 | -4.86301 | -38.37876 | 2024-11-25 03:40:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b798943-d056-3567-8d39-a0ff7810979a | -3.15669 | -45.48307 | 2024-11-25 03:40:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b338a376-2c5d-3bc0-a91e-1fc02246a3b6 | -6.52149 | -43.33094 | 2024-11-25 03:40:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8994eb2-0c82-3aab-b81b-309fda559362 | -3.15747 | -45.47854 | 2024-11-25 03:40:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 260a9bf1-9ea8-3798-9f31-c70804a29581 | -4.16674 | -46.82263 | 2024-11-25 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ffa6a1c-5f52-3820-8baf-ceac85552473 | -3.2833 | -45.73775 | 2024-11-25 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48901896-65b1-3987-a649-a67c4c6743fd | -5.9641 | -41.14812 | 2024-11-25 03:40:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3bd647dc-ac34-3ac0-ac76-cb12533479dc | -7.51444 | -35.11451 | 2024-11-25 03:40:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4707b805-82c6-321e-89c0-1524c639da6c | -4.16173 | -43.06196 | 2024-11-25 03:40:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32b907d0-d0aa-344d-85b6-8a2ab8f6e9bd | -4.53829 | -47.66858 | 2024-11-25 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 384461ce-5f08-385a-9815-8a29e31385de | -4.16681 | -43.06286 | 2024-11-25 03:40:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b46f4dd5-7a12-307c-a46c-a383a8450db6 | -6.72732 | -43.56421 | 2024-11-25 03:40:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 410e5009-658f-359f-b52c-16e410ec28b8 | -3.3968 | -44.74466 | 2024-11-25 03:40:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5045c307-e7b4-3e10-bf45-16087fa26e99 | -4.19664 | -42.97734 | 2024-11-25 03:40:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac923f97-1631-3389-ba8c-1d897f9a1fb3 | -3.28863 | -45.74361 | 2024-11-25 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6ed74de2-1a0f-3429-8b43-938f5054f02f | -6.73504 | -34.9743 | 2024-11-25 03:40:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dbe43bc3-c0e4-3356-b4f1-fa2ee3eb1281 | -5.57228 | -39.36202 | 2024-11-25 03:40:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51fcafdb-c06d-349f-aa29-3cd5df4140eb | -5.81457 | -39.2136 | 2024-11-25 03:40:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3545c165-5d3b-3af2-9115-02a49660530c | -4.81251 | -45.75436 | 2024-11-25 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ef4b93b-461e-38fc-b921-748ae9e5278c | -5.13065 | -46.20024 | 2024-11-25 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b06e78c-dd24-35d5-8115-2fd06ecda209 | -3.47019 | -47.68882 | 2024-11-25 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4570ab58-93e7-375e-b55b-60def0a0ba85 | -5.44508 | -46.34329 | 2024-11-25 03:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88b8c4db-3d12-343b-8743-39f096df033b | -4.19207 | -42.97355 | 2024-11-25 03:40:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 737e829b-1bba-3879-bc24-76f4c5b3efd6 | -9.81267 | -48.17335 | 2024-11-25 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47439e24-ac46-3262-8621-62b63f6c8d48 | -9.81414 | -48.17097 | 2024-11-25 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3588571f-ebb3-3077-ba0c-b5ce837ca5fa | -21.93559 | -46.23501 | 2024-11-25 03:44:00 | NOAA-20 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 107fc995-2ff3-31d4-add5-e2ab14dd2d2e | -17.09294 | -43.80549 | 2024-11-25 03:44:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf252d68-43fd-3dd1-8527-67823a58c858 | -19.94306 | -44.11476 | 2024-11-25 03:44:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2c300c13-74a4-3685-8cf3-5586a4401246 | -22.43484 | -47.67964 | 2024-11-25 03:44:00 | NOAA-20 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e51f83d-50bd-3d3d-8e95-814a94eaa22b | -22.87479 | -43.6047 | 2024-11-25 03:44:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7ffb34cf-9fc9-3146-8b01-fea6d5fd3213 | -16.68201 | -43.88563 | 2024-11-25 03:44:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 828a6a3b-46c3-3909-b6d9-1c5d3ee67fa1 | -22.78636 | -43.7572 | 2024-11-25 03:44:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5aac0cf7-9924-335b-b4ab-e402dff7501a | -22.67617 | -42.85714 | 2024-11-25 03:44:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 031cfdb1-dc49-3ef2-815b-d35cd4c39a55 | -22.69884 | -48.26956 | 2024-11-25 03:44:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cef0b4c5-9d43-3c00-b7a2-030b887e52aa | -21.94069 | -46.2336 | 2024-11-25 03:44:00 | NOAA-20 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f2ae3d57-6a2a-3fc6-8dd5-bf13f05265da | -19.94719 | -44.11568 | 2024-11-25 03:44:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 567c78ef-fec7-35f6-819e-0768a040b46b | -21.94013 | -46.23604 | 2024-11-25 03:44:00 | NOAA-20 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08d530d0-958a-3f29-8a3e-41bf18b18c1b | -22.90064 | -43.75233 | 2024-11-25 03:44:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5bbbbecd-5787-3abf-86d7-574090e7e661 | -19.83988 | -44.61227 | 2024-11-25 03:44:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f567d726-20cb-356e-846e-e0040a7cafb4 | -18.21964 | -45.05418 | 2024-11-25 03:44:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1fb290a-6bb1-3212-9ca8-f89b61fe1fb7 | -20.30967 | -45.58565 | 2024-11-25 03:44:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8881d23-55e2-3cfb-a719-ef8619fed2a1 | -19.43769 | -44.34209 | 2024-11-25 03:44:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README13.md)
