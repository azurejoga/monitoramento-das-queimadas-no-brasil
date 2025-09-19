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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 997fd878-49cd-3a7d-90e1-a62313fd6d4a | -5.80724 | -45.71875 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0392bc1-8c6e-3036-bc9d-0709a888d47e | -5.92394 | -45.08013 | 2025-09-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d62819b4-79f2-3e08-a220-8667d34708a0 | -7.65935 | -45.12902 | 2025-09-19 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a76d7e5b-bce2-3219-b2ad-55515a34a19c | -7.6076 | -44.61595 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f4e58bb-eb4f-359a-9ace-81e24c3f5fde | -7.58165 | -45.48725 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 689d1a1b-55f2-348a-94ae-f51c32ff185b | -8.13854 | -46.77573 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bae5e5a7-4fce-38e5-bed6-4fb4b359c4af | -5.08319 | -47.51892 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb1a06cc-7bdd-3096-8912-0d29bfd2d272 | -6.12848 | -43.94914 | 2025-09-19 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14e2b854-20da-31ea-905c-3adffae33be1 | -8.13521 | -44.47211 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dbde838d-14bb-31fe-82a4-262de671dda0 | -6.9002 | -44.76729 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 909ea521-f670-3506-aee6-90bf0d0e572f | -7.99796 | -43.81276 | 2025-09-19 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 27225fd3-3f21-341a-8cd3-2790798bd6f7 | -5.7565 | -43.39152 | 2025-09-19 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abf55e3b-5cc4-3ae6-aa19-6deea68e08af | -7.35908 | -38.96016 | 2025-09-19 03:53:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6db03991-1ed5-33cf-8e30-655c90df98c1 | -5.90028 | -45.71996 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e762d39c-951a-31d7-8607-0fc2ea70e1a1 | -8.14228 | -43.62957 | 2025-09-19 03:53:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31f3c343-5fb7-3617-925f-d684cf8d94f7 | -10.51775 | -40.32929 | 2025-09-19 03:53:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0c80d187-d24c-3731-a738-6033a669df1a | -7.5824 | -45.48459 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bd9e289d-e9d5-3a7a-bda3-539b68738043 | -3.27644 | -49.15307 | 2025-09-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 253d5a1b-fd82-398f-8987-6f2812546fec | -4.61719 | -47.0247 | 2025-09-19 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6ff12d6-255d-332b-94eb-6795294503f7 | -5.79856 | -45.37072 | 2025-09-19 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 929a4140-6cfb-301b-9320-522fc02aa5dc | -7.70615 | -44.39242 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 277a5450-e89a-3e69-b7ed-44c4ff67bd0d | -8.13752 | -46.78142 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 16510a61-4fa1-3dcd-8b9b-a4b0d6b3f984 | -10.37086 | -42.45804 | 2025-09-19 03:53:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 05421f2a-58c0-3523-93e8-51505c904081 | -8.13954 | -46.7702 | 2025-09-19 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35f3f9c9-9e56-3322-86db-707772839fbd | -5.91854 | -45.08414 | 2025-09-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 82a4c7a3-7d37-3667-b71d-ecd9248a7bb7 | -6.83178 | -41.03907 | 2025-09-19 03:53:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d07a2964-0fcc-3ec9-b95c-b19ad2f8c91d | -7.4564 | -46.38223 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bed4a078-e892-3630-a9e3-ca47cfd512ef | -7.70165 | -44.4692 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4737bc3a-88d2-34c6-9b2a-8cf84faae940 | -7.61662 | -44.45935 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 812eed2e-7566-38f0-b835-0390feabb897 | -5.78906 | -43.90345 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33726cd7-04e4-3849-be55-1ad85fafb37e | -8.48496 | -44.73834 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3526bce0-f514-38d4-9cff-425b9d706e7e | -5.47176 | -46.69194 | 2025-09-19 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0894dafb-d785-3070-ac0c-f4cf61da5066 | -7.2848 | -43.93246 | 2025-09-19 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9c0213e-0650-34fa-a334-c857a257fc17 | -7.19711 | -46.68039 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6a4df91-4c9b-3b96-8873-f0db4061b0c9 | -7.26188 | -46.34323 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0eab7506-e6e8-331c-a65f-4121a9265984 | -5.4751 | -44.11888 | 2025-09-19 03:53:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b52b246-6457-3b94-8dd7-5f6c72066bd2 | -5.91865 | -45.08198 | 2025-09-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 71ef813f-94a6-3939-9144-a7207c03cebe | -7.35939 | -44.59219 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85c106b0-d46d-3279-b281-d311832d82f0 | -5.12651 | -47.83003 | 2025-09-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 15366e0f-086c-312b-b4e6-2aaecea0933a | -8.95038 | -44.20082 | 2025-09-19 03:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ff3c7ba-5ecb-3ac8-8115-eca5948581be | -5.79786 | -43.92909 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79e718b9-b35b-3a57-9b7a-ba7e1521cb9b | -7.49677 | -44.39872 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee587146-117b-368c-8dae-c9ba8e4e669f | -8.48809 | -44.7382 | 2025-09-19 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 650bbab7-5d88-3060-8304-1a8581a42669 | -7.32366 | -46.60607 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1fe0cf90-3d41-33d0-b0a1-4685e38436fa | -5.79814 | -43.90093 | 2025-09-19 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6eec0120-1ee4-3d5c-ab85-ec77b0a357b5 | -6.58075 | -45.58997 | 2025-09-19 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec70458f-3287-3b76-919b-72dde2412f26 | -7.23137 | -46.60234 | 2025-09-19 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c41b654-9b77-3d62-8264-450087643045 | -7.5602 | -45.50284 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 021e5e32-f293-34ef-9c15-b4828599e920 | -5.62958 | -43.89813 | 2025-09-19 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d47013e-1e68-3d0a-be66-b9fcfaba5390 | -9.12701 | -40.32822 | 2025-09-19 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 369427ef-c4db-3bd1-883f-39299f77806d | -9.15934 | -44.90094 | 2025-09-19 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ccd027b-79c0-3a13-aab2-544994e5bd85 | -7.36014 | -44.58785 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d97dcf5-952d-39f8-82f5-93bca96ba2eb | -7.5527 | -45.49179 | 2025-09-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 67ea50bc-3354-3967-8118-17e841172a4b | -9.72965 | -45.92305 | 2025-09-19 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28775ed2-0718-356e-8d82-b3c2d6b8102c | -7.33223 | -44.56989 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d9c40ce-4cf8-3086-9e52-30f96e8e3b43 | -5.39972 | -37.55749 | 2025-09-19 03:53:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1c30d4a2-428b-3c9a-927e-2003a78a2df8 | -5.82697 | -45.91773 | 2025-09-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d98e15d-0d63-33ad-a0b1-37133fd1c7ea | -9.2122 | -40.2496 | 2025-09-19 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 53e860a5-7d28-3aab-adf4-a15e19d896cd | -6.20541 | -44.05768 | 2025-09-19 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0098c0fe-8dc5-383a-91f9-0773111ab2b7 | -4.68431 | -43.2421 | 2025-09-19 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 436f2a0d-dae3-310c-8090-0e986aadbc1a | -9.18539 | -45.32087 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00da9213-669a-38bd-8b5e-95d9f121730a | -9.18025 | -45.32434 | 2025-09-19 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1678bb8d-726b-3d58-9487-49f5cd3b2c23 | -8.05862 | -44.08879 | 2025-09-19 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71a6a2e6-3c62-3d8a-8db6-1f21a3a31d1a | -7.84934 | -45.6275 | 2025-09-19 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d86ed3a-d64c-3b2f-aea1-7569c39c8007 | -6.20626 | -44.05418 | 2025-09-19 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e01ed5d8-9209-390f-8528-c54428d92101 | -5.13124 | -47.82912 | 2025-09-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0250ce10-7769-3995-bf61-839e0e9a618f | -4.16495 | -43.00046 | 2025-09-19 03:53:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94a52deb-0d40-3234-b386-6d3e6b2dbaae | -7.21915 | -44.37457 | 2025-09-19 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 922f9710-e57e-3281-8e4f-9b140c1dcfad | -5.08344 | -47.52223 | 2025-09-19 03:53:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3665c7f4-b4c2-3a21-8f0e-24d64657fd3d | -9.37168 | -40.41653 | 2025-09-19 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.1 |
| ed37db02-1608-300f-98df-9f448ca6bf11 | -14.50011 | -47.35352 | 2025-09-19 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 451cd37c-c3c4-35b7-9b5e-0262d1335301 | -10.91701 | -45.65871 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af3e8205-ffeb-31f2-90ae-e596a4bf2c3c | -10.3234 | -45.24837 | 2025-09-19 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1d0ff13-a829-3859-8452-69d10a34149b | -16.21381 | -46.67352 | 2025-09-19 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c785b9d5-3bef-3e78-836f-9456bab33101 | -17.19681 | -45.94211 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d20100e-b39f-3068-902c-7a40cbaedabd | -12.08888 | -44.82558 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd8a556d-1311-308a-934d-7178fce106da | -11.43293 | -40.65982 | 2025-09-19 03:55:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 8ade11f2-86fd-3d55-b0d5-2acd5c6f9817 | -10.29272 | -50.2374 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e09c3e34-3e07-319b-b4b7-c07973b8774b | -11.21054 | -49.63651 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fb1475e1-8ae6-3ed2-8e3a-7f83bbc25b8b | -12.151 | -44.94668 | 2025-09-19 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 054723b6-e82a-33d2-9a87-19210f2779c2 | -10.48447 | -45.16767 | 2025-09-19 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62d15c68-d031-3945-a3d2-3e389b6ce36f | -16.53856 | -44.9026 | 2025-09-19 03:55:00 | NOAA-20 | CAMPO AZUL | MINAS GERAIS | Brasil | 3111150 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f87ab4b-e661-37cb-94bf-a1c5567acdf4 | -17.0634 | -45.90915 | 2025-09-19 03:55:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b9b77558-7918-36ab-ab54-f7046c0874af | -16.67951 | -49.44335 | 2025-09-19 03:55:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46b9d6f8-fe91-3e72-bbcf-853a3ee8890d | -11.08974 | -41.07153 | 2025-09-19 03:55:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d9335a8b-9468-3512-a871-baebe6e7a9f0 | -13.95647 | -44.54617 | 2025-09-19 03:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb9d4bb9-58b4-3750-9de2-c3caf6302a90 | -10.29841 | -50.22383 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| ac37bb95-101f-369f-a6f9-7e04d9859f21 | -18.55716 | -40.04745 | 2025-09-19 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8e3f1764-699f-337e-a212-4fb4e43f3d65 | -11.21129 | -49.63263 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 688522ac-83e9-3b1b-a2a0-232d718550d0 | -15.70397 | -41.75332 | 2025-09-19 03:55:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2120527b-3148-3c4a-8134-e385368bc9bc | -13.66892 | -44.22262 | 2025-09-19 03:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 774b5449-b8f7-3200-8be7-0542b3360112 | -13.16928 | -44.5974 | 2025-09-19 03:55:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee3cb53c-e31a-322a-b6e5-086e39f28590 | -15.32482 | -42.05537 | 2025-09-19 03:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 9bc92609-bd1d-368a-95a8-e724e440f089 | -12.92389 | -50.56683 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 982817fe-0a78-3efd-b634-c51b00907967 | -15.61006 | -40.79575 | 2025-09-19 03:55:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 80c7b0fa-6727-33cb-9979-6591f90e8d85 | -11.08696 | -41.06727 | 2025-09-19 03:55:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b25239d6-97f5-34d2-9d06-7c6f33b05551 | -11.41274 | -41.41232 | 2025-09-19 03:55:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 93c5c40e-9ab5-3fc2-9d9b-ec4f4e16fa05 | -17.45884 | -44.78157 | 2025-09-19 03:55:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6fdfaee-d5b8-3805-8020-6c885e3ae0c1 | -11.21616 | -49.63766 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6e004a8-2cb0-3747-99f6-c2a6c750b7c7 | -11.17909 | -45.37141 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README15.md)
