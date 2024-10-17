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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9ba2cc0-2162-3229-9ae4-4203d503c145 | -8.18501 | -44.10799 | 2024-10-17 04:12:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da2a9d9a-14c8-338f-acb8-46f91a2c57ad | -8.919 | -44.12857 | 2024-10-17 04:12:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f938d23a-dc77-3099-9cd4-1806297781b0 | -8.89355 | -44.22474 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9060355-84be-3874-8367-8f8947b4e49a | -8.21099 | -44.39244 | 2024-10-17 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f9973b4-c295-3681-ab7c-d595445c2966 | -8.10611 | -44.3901 | 2024-10-17 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ad9e51d-395b-31d4-a544-e19c7e1fb5b0 | -9.14278 | -44.987 | 2024-10-17 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6507f1c7-2f75-3564-8cea-f83b8abcf343 | -7.8659 | -45.35915 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 426c6e33-f18b-39da-b17c-2738204e4648 | -7.86188 | -45.36232 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0c2d47f-9037-30f9-8789-42822c03099a | -8.50601 | -45.4576 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95c55f23-afa0-3752-a519-16549c9b7874 | -8.39937 | -44.74598 | 2024-10-17 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35f82958-6996-37ce-a3fd-e946917ee4ac | -7.87052 | -45.35226 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9c9803a6-3ddc-33b9-9f1e-f5953e3a5c18 | -7.86932 | -45.35971 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e13a4792-efaf-39f2-85be-10104243b540 | -7.86872 | -45.36345 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87c40630-d1f5-3aec-b13b-11ef378dc6f2 | -7.86369 | -45.35114 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 75f13195-fbf2-3b8e-aca4-ce1b267cc800 | -7.86309 | -45.35486 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d9f0ff67-0cd4-315f-9038-4310891c3194 | -7.86249 | -45.35859 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 821e6890-d1bb-3209-87bd-275f799aa811 | -7.85847 | -45.36177 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 323b6c03-01b4-3655-a196-0dfa66e8ac1d | -9.44464 | -44.75369 | 2024-10-17 04:12:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b741a0b9-2e0f-32a1-ae67-be0e07a08440 | -3.60423 | -44.79343 | 2024-10-17 04:12:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84259881-d9b9-3d5b-9447-8d82a37a9b91 | -3.60484 | -44.78961 | 2024-10-17 04:12:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 54027f2b-a9c0-31ed-b9cf-c41ef0352f02 | -4.9804 | -45.47672 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 284ee782-f5bc-3e31-a738-1decae2ecc43 | -4.81935 | -45.39624 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c8424eb-f4b5-347f-920d-a9751b77a2a4 | -4.7761 | -45.973 | 2024-10-17 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13c50578-9542-3e83-b31a-b84ae7f8d60a | -4.6286 | -45.61256 | 2024-10-17 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0464d00f-4c1b-30f2-8dd9-f5ee882674f9 | -4.62505 | -45.61192 | 2024-10-17 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1bc379c2-4e92-308c-b68e-d281c231ef17 | -4.62439 | -45.61596 | 2024-10-17 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4acc178f-b361-3668-a4bc-e361af5f0ab5 | -4.59092 | -45.75349 | 2024-10-17 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4aece1c8-d94a-3865-8736-74a9ad9857b3 | -4.47117 | -45.67294 | 2024-10-17 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 227ae043-1f39-3d7b-8e20-c86e271cb79e | -4.46244 | -44.97611 | 2024-10-17 04:12:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bde5d38e-de88-3840-a2ad-55ebb7744044 | -4.40481 | -45.81096 | 2024-10-17 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 680ff69e-e6bb-3dc1-9b32-088bea39dd85 | -4.38454 | -45.799 | 2024-10-17 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9324a26-7c4a-31cc-9c26-2b08bfd30303 | -3.95782 | -45.61319 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 53989ffe-1e19-3de5-9d0f-02a533a273eb | -3.75815 | -45.75494 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6952154-083f-3c02-b7a5-3974cc1b55e5 | -3.70291 | -45.91132 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| d897c97e-f84c-3432-a73c-52c34a2c9a1c | -3.7015 | -45.91999 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 36a0dd99-887a-3ae7-9620-087e48e9518d | -4.98393 | -45.47731 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d94b88d9-8ec1-3114-a5fa-ad35be161789 | -4.96544 | -45.61361 | 2024-10-17 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8aa6d0e-aa2e-368d-8fe1-b6ba0b0968f4 | -4.77542 | -45.97712 | 2024-10-17 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2f262c8-b25e-3607-ab06-d17585ccd95a | -4.58733 | -45.75293 | 2024-10-17 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8faa1b13-19c6-3036-b045-2bd0ae00db7e | -4.58528 | -45.75355 | 2024-10-17 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82866fd2-2394-3872-a7d9-41b5f4b0b2d6 | -4.53335 | -45.77871 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad2572a8-212a-381f-9c7b-f09ec53de093 | -4.44839 | -46.11967 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f44fe976-56d1-35bf-a0a1-770c43189d64 | -4.44769 | -46.12397 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65109844-49e1-3d92-a114-3334034472b2 | -4.43954 | -45.82523 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2565dff-2065-393a-8b3d-f85e3d5e1082 | -4.38815 | -45.79956 | 2024-10-17 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e850438-b3c7-3f9b-9584-53b26d9cdf4f | -4.36242 | -46.14294 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fbe43b9-cd02-3f62-8421-8aa4c8e09fe9 | -4.35874 | -46.14238 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff6f03d0-82ef-32d6-8005-7b7d1c66a2f7 | -4.05441 | -45.56134 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d669d2c-7269-326f-9959-d05e9738714a | -3.96141 | -45.61376 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| fe82d4df-0913-3fe7-bbee-1ae4eada6561 | -3.96074 | -45.61788 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 680f04cf-bc2e-36e2-80c1-e1bfb3f3d00a | -3.76245 | -45.75132 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7d6f18ef-541e-30e7-bde0-8dd8f82250ed | -3.75883 | -45.75074 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3af98960-2635-3f31-a77b-1bc9006cd1eb | -3.7022 | -45.91566 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 1df36ab6-3242-337a-8661-54534db94395 | -3.69926 | -45.91072 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| f1fd0bed-bb36-3dd3-b650-3ff89c96f2a1 | -3.69855 | -45.91505 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 3ddc0b9a-bc17-3cb9-a0a2-c790bcda602a | -3.69784 | -45.91939 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 382aceaa-afa9-32a2-a004-1c6b6296f973 | -3.6956 | -45.91013 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21f3ec9a-ed38-32bd-965a-73f36f06a9e8 | -3.69489 | -45.91446 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b729ac5e-e889-3f32-bccc-e430dba9111f | -3.69418 | -45.9188 | 2024-10-17 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd75b502-6c51-33be-b48b-a4b625ddb49d | -5.98345 | -45.37109 | 2024-10-17 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| cd8783a2-02db-3fea-9e63-b9c7156913e1 | -5.9806 | -45.36668 | 2024-10-17 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8295ffa-0c3e-3ead-a399-dcc4c667cda3 | -5.70387 | -45.77554 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 36473fab-19de-3a1c-80fa-8951cf73ec28 | -5.70321 | -45.77956 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98e0c3ae-0462-317f-b8c2-d0cd0f52c76d | -5.58513 | -45.32145 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81eeaaba-657a-3c43-91db-243f2e647763 | -5.327 | -45.07393 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4963daa7-919a-3734-8eb5-91d2d1f82785 | -5.32639 | -45.07772 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 973feb75-a9b9-3566-954f-e3298add868f | -5.32354 | -45.07339 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78accfcf-d89a-32dd-b86f-9b6229c77bb9 | -5.32293 | -45.07721 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e8bbe2d-70e5-3037-b5dd-70607f02bc5f | -5.27666 | -45.45771 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59622bb4-38ac-33b2-9b7e-902da99d8ef0 | -5.27015 | -45.2292 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee3395e1-a683-3ea0-a4fd-8be73b8f1a78 | -5.97998 | -45.37053 | 2024-10-17 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| a570fd5d-ae06-3e14-9fc4-b68cd43285dd | -5.97935 | -45.37439 | 2024-10-17 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| ef1da113-97cd-368c-9e64-795d9e2bc8bf | -5.8521 | -46.42896 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0b16154-8439-3cfa-8bdf-265c63d837d2 | -5.84351 | -46.45873 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdf137e5-130c-34f4-bdeb-229910e962d0 | -5.78396 | -46.20104 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40a8ab22-78fc-3cf0-b428-555b169d0aa4 | -5.70741 | -45.77613 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2beb152c-b427-352e-aad6-7adb6f984403 | -5.85576 | -46.42961 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ccf7e770-142b-3a6a-a9e5-24f11d436b49 | -5.8514 | -46.43329 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 158a1802-5e45-3416-b8db-263bc155da19 | -5.84718 | -46.45934 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b03b19c3-3e45-3d57-bbb4-b9f767964fc1 | -5.84548 | -46.23992 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5052de82-2a50-3b77-94d5-201501817287 | -5.84423 | -46.45428 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2234e08c-56d1-3d09-925a-5b9cb6fe48e6 | -5.84255 | -46.23513 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a9c14a20-fc1c-3fd7-b672-455adcdc5585 | -5.78465 | -46.1968 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15089c18-c0cf-3a63-b961-5cf4f4e7a6ea | -5.74658 | -46.5026 | 2024-10-17 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e0bf449e-95dc-373c-aa4f-a2aa0ac5ed68 | -5.56299 | -46.29356 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e655980-40a3-3539-a190-a96920439c94 | -5.5155 | -46.28615 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d0da811-1fdf-322b-ab89-2f955b69803b | -5.98408 | -45.36724 | 2024-10-17 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4804736-96bc-3bcb-80c9-6b682baaa556 | -5.85506 | -46.43391 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6af1939b-3fac-3deb-8257-7fcb701abdc9 | -5.75027 | -46.50317 | 2024-10-17 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2c25b960-530a-30c9-8cdf-b4322181965d | -5.51487 | -45.40153 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d88d0ac-bd2a-35a3-8bca-e0a860e4839f | -5.51202 | -45.39702 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 328c8bb4-fed7-3d6c-b821-987e9ae3cee3 | -5.44276 | -46.31963 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26e10099-97fd-324d-8e5a-4fa786e772a7 | -5.44207 | -46.32395 | 2024-10-17 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3c875d2-2be0-3d4c-830e-ed192b5caf81 | -5.27729 | -45.45379 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd79305c-615a-35c9-b126-9f95ba738943 | -5.21052 | -45.44314 | 2024-10-17 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d48074ca-28d8-3bf9-bfc8-b0f4483099e1 | -5.16699 | -45.39682 | 2024-10-17 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aeb594d-8fde-3445-a3ac-94378d5b2edc | -5.16411 | -45.39232 | 2024-10-17 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac9c57ea-2783-321e-b189-e0fb3177de5d | -5.1606 | -45.39175 | 2024-10-17 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 384f055e-80ec-32bc-8272-5f2c9883d6e8 | -5.09367 | -45.83345 | 2024-10-17 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bacdd0da-251c-3ed2-9409-9581762d851c | -5.09302 | -45.83752 | 2024-10-17 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README29.md)
