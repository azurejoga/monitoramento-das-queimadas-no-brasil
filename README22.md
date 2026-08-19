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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ca49a4e-9532-3474-8521-6e282b729392 | -5.9011 | -43.6279 | 2026-08-19 04:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| beda7a38-6e1b-34ab-a1bc-cda2a2353502 | -9.3873 | -60.5721 | 2026-08-19 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 660d1661-64b0-3409-8358-97c1bf23768f | -5.4319 | -48.3996 | 2026-08-19 04:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| e304d59b-5d90-3754-a414-c269f4aa7ab7 | -6.6938 | -58.942 | 2026-08-19 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2485a678-3582-3e04-a945-7c36a85a1e7c | -5.4503 | -48.4201 | 2026-08-19 04:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 582bf05e-3cc0-3aee-bd7e-27d1ae7ba061 | -8.5598 | -54.7579 | 2026-08-19 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 173fd609-8506-391b-b88a-2ad9bc3aa70b | -6.0178 | -57.8631 | 2026-08-19 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| a1980ac7-c010-35d6-b793-044960ba5353 | -5.4319 | -48.3996 | 2026-08-19 04:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 232cf09a-b237-3367-8d40-b0c910648a97 | -5.9011 | -43.6279 | 2026-08-19 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4d206177-2efb-3c50-881c-a6841c7c63e5 | -5.9198 | -43.6264 | 2026-08-19 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| e52f14e6-fba9-3d02-8a0f-e51167c18250 | -9.4256 | -60.4353 | 2026-08-19 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 5ecf21de-ebba-31dc-a72e-0a7e0adc972d | -6.0912 | -57.9187 | 2026-08-19 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ed242577-afdd-35e4-aac6-52c3cb4bf6cd | -5.4317 | -48.4212 | 2026-08-19 04:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 15c0582b-bd12-3b48-a6c8-61a11be45eb7 | -5.9994 | -57.8639 | 2026-08-19 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 5c50d5dd-27d7-3e14-b099-62d34ba69f35 | -9.4257 | -60.416 | 2026-08-19 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 78d6154d-53d5-3134-858f-ee47bede836d | -9.4061 | -60.5518 | 2026-08-19 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 61f8309b-720c-37c9-99a5-eea1ad04f002 | -8.5413 | -54.7389 | 2026-08-19 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5d43c89c-3382-3e4a-95c6-332de750c997 | -9.406 | -60.5711 | 2026-08-19 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| da44cb71-abf7-3e15-8f6b-39c6193f3f03 | -9.3875 | -60.5528 | 2026-08-19 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 88fb77ba-8cf2-3c70-b681-088d67e8032b | -8.5412 | -54.7591 | 2026-08-19 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5ccbc954-3632-35ce-b86e-f53c55bcdb78 | -8.56 | -54.7377 | 2026-08-19 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 747a1942-0c0f-3662-b4de-99d11bfbee5c | -8.5787 | -54.7364 | 2026-08-19 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2cfc407e-343a-3074-a662-541799449583 | -8.5785 | -54.7566 | 2026-08-19 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 8469f9bf-3b3c-37bf-bc54-c04748ccaac7 | -5.92 | -43.6032 | 2026-08-19 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 75d7a07c-3913-38dd-8f32-e06838b5a26f | -5.4503 | -48.4201 | 2026-08-19 04:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| eec6e06d-58c8-3a98-a281-1a52df5ad0ea | -5.90887 | -43.62305 | 2026-08-19 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33b3196e-717f-311e-922e-1d5ac6ddc842 | -5.43936 | -48.41403 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 82fd53bb-2dda-31e5-8579-ae540bdbe799 | -5.43475 | -48.41322 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 78f8346c-a81d-3f0f-857e-bae27285d5fb | -6.53347 | -43.10902 | 2026-08-19 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f8ab095-bce2-33ad-a143-beba6e030d2f | -5.1452 | -40.66017 | 2026-08-19 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| affd2840-8b44-3ab3-bad1-c8246e5ca37e | -4.70596 | -47.15793 | 2026-08-19 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 97476ae2-e1c1-3c3c-b2ea-fe1e18d9a724 | -6.36796 | -42.53128 | 2026-08-19 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02d5fa6f-7235-356d-8576-ee78d37ccf9d | -6.16282 | -45.35178 | 2026-08-19 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 813b5e92-23b4-317c-b789-73fda24cb9b8 | -4.71024 | -47.15863 | 2026-08-19 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dc474d1f-7715-3afb-a522-3fdc56b4fa2a | -4.71093 | -47.15457 | 2026-08-19 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 74785bfa-4f16-31fa-b58a-f7266c8911b6 | -3.51453 | -44.2388 | 2026-08-19 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 902baf66-2642-39bf-9777-f4a4e59811d3 | -3.67732 | -47.6542 | 2026-08-19 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11188c27-e446-3c28-b261-58977d9a036b | -6.29293 | -43.6439 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff25aec3-049b-328a-ad33-0a6dba9e957f | -3.42878 | -51.51464 | 2026-08-19 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a34a4faa-104c-34c6-a6ea-a4ed1b168a33 | -3.68708 | -47.65121 | 2026-08-19 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 60c8b508-33b3-39fa-9b39-9c8c8c276803 | -3.27096 | -49.52507 | 2026-08-19 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bdcaaa5-7821-3135-9e33-34b472939e5d | -5.91171 | -43.6274 | 2026-08-19 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 8d80a572-0657-3ca7-aa1f-f0ff7c15bdcc | -3.73247 | -42.55617 | 2026-08-19 04:17:00 | NPP-375D | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a30371c9-c783-3bca-8e97-9f8d80b51b28 | -6.27564 | -43.27741 | 2026-08-19 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 37fede71-fbae-31bc-8946-786e36dfeb40 | -5.79318 | -43.91805 | 2026-08-19 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 64b70546-32d2-38b3-aee9-adcc36b419d1 | -2.76975 | -48.57432 | 2026-08-19 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2313eab0-a628-3002-bf5a-7f4d110b3d6a | -2.49933 | -48.14142 | 2026-08-19 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d384e02-3461-3d2d-a2d6-931ebfc9c7ac | -6.29071 | -43.63585 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2544f780-4d90-35e2-8851-923c75d1e094 | -6.33726 | -44.08182 | 2026-08-19 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84f35ad5-cd7f-3171-ba45-6343978e1a19 | -6.3414 | -44.0785 | 2026-08-19 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5fffcbf-4fa0-36f5-828d-f1c07aeaa0fe | -3.27044 | -49.52818 | 2026-08-19 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 617d46c5-3985-3ed4-afae-aaaa9af08be4 | -5.42934 | -48.41719 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 634de0b7-f350-362e-b278-25e8c43ccbbf | -6.63746 | -41.43275 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 53c282f8-de74-3322-aa91-9854f36cbd15 | -4.70331 | -47.15865 | 2026-08-19 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2bbf275-158e-32d8-9e5b-a70fc4ed0460 | -4.00718 | -48.06113 | 2026-08-19 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e1d049a-a461-31b1-a3b8-7cbc656ea75b | -2.80057 | -48.94345 | 2026-08-19 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5be4056-9f50-3597-b7e9-c4e55e70c63a | -6.22339 | -43.71101 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d009b63-9a08-3758-88b7-83a72ca41137 | -4.00254 | -48.06057 | 2026-08-19 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3816da43-09b7-38aa-9154-70456716641f | -3.51521 | -44.23458 | 2026-08-19 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5c2926c-5ed2-337e-a375-62d714973ea0 | -5.78841 | -43.92524 | 2026-08-19 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37381cee-919b-3be5-9fe5-74f5038f575e | -5.42009 | -48.41574 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d324e5d7-df8b-304a-8453-659fb37cd7f0 | -3.26686 | -49.51793 | 2026-08-19 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 295f78c5-485f-37ad-b8c1-6802fe19bf64 | -5.91293 | -43.61983 | 2026-08-19 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e90f5845-ee10-3e2f-9bd3-9a9790f80de9 | -5.78777 | -43.92912 | 2026-08-19 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57d2ed70-c937-3815-ab8b-c8ce8e01b305 | -4.97281 | -42.21181 | 2026-08-19 04:17:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a8ff712f-f92f-32e4-9820-8484292865fe | -5.79255 | -43.92191 | 2026-08-19 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a677f1c2-aca7-3c87-b332-4b80378fdd01 | -6.28726 | -43.63531 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf8a236a-180b-306c-bcb3-3dee221ee0d4 | -4.00421 | -48.05884 | 2026-08-19 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e14862b6-66ed-3d71-ad51-0831c5a941b5 | -6.2901 | -43.63959 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eba4294a-ebd9-3934-b4da-4b80dff7306d | -4.01349 | -48.06 | 2026-08-19 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a942bb8-6481-3ec8-b119-75e2d6e91b8f | -6.23456 | -43.68561 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33364810-c05a-32b7-a585-d0b6e837fad8 | -5.91923 | -43.62473 | 2026-08-19 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 989e288a-a7d6-3804-92f4-9ec1c1faef3a | -5.79731 | -43.91475 | 2026-08-19 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f595c30-97a5-3e7a-9113-d58aa5159a14 | -3.26634 | -49.52102 | 2026-08-19 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 075f1dc2-132e-3a76-bf52-910c6b56ff8e | -6.06813 | -45.36128 | 2026-08-19 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42a5e4aa-db57-3d9c-9adf-0baf3376793e | -3.42713 | -51.51208 | 2026-08-19 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27a03965-2584-363d-a77a-62126a39e046 | -5.73327 | -44.50536 | 2026-08-19 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5db578c-ac71-30ee-b805-ba75b84634cd | -3.68182 | -47.65496 | 2026-08-19 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 728a79f6-5322-3e2c-a94f-9412507e9ea9 | -5.43555 | -48.40849 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 6bbf367d-a73a-3373-a7b2-e731cc70c0e4 | -6.06739 | -45.3658 | 2026-08-19 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05e1b164-eb08-39d9-b6d6-ce2ef20d756a | -5.14574 | -40.65668 | 2026-08-19 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a91c6dcb-772e-3829-ac82-53014692fd93 | -6.23396 | -43.68937 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b64cb0a3-be20-3631-9ba7-8f02067ea456 | -6.26883 | -43.27632 | 2026-08-19 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3a1e2783-b0d4-3e1f-9e5d-74363451669b | -4.00885 | -48.05942 | 2026-08-19 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65590aa4-9dad-3f83-bd00-e618c59568d7 | -5.82278 | -43.39862 | 2026-08-19 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06cf8f7d-49e5-30d7-a657-2d9dbc4453f5 | -3.01234 | -51.05787 | 2026-08-19 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 041ca693-a9a4-32c3-a95a-0cd9cd420288 | -6.28949 | -43.64334 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cafbe453-d3d1-3be0-9cc9-16198ddc3ba2 | -6.37074 | -42.53535 | 2026-08-19 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af28dd4c-d9ab-3d78-9183-7106e73fe2bd | -3.69156 | -47.65208 | 2026-08-19 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 593a2e8c-b5b9-369b-a628-867ddbbf0616 | -6.29576 | -43.64821 | 2026-08-19 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96ecb7f9-aac2-3e45-bc73-6d435f3f6fd9 | -3.68258 | -47.65041 | 2026-08-19 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 569a7734-9853-3961-a4c6-2fa9d7be1509 | -6.33853 | -44.07405 | 2026-08-19 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d438abe-df30-3f2f-a9f4-584ca8236c44 | -2.69131 | -45.3714 | 2026-08-19 04:17:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 955fa19b-490c-3adf-8a2d-e0fa8b756d74 | -5.91517 | -43.62796 | 2026-08-19 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| fd372c87-67de-3c59-bd79-95093ce4b570 | -2.79982 | -48.94409 | 2026-08-19 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9868a22d-8418-3358-883c-49d983b42c39 | -5.42552 | -48.41166 | 2026-08-19 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| e31e3f56-9800-32f1-9110-390bedff53ed | -5.79668 | -43.91859 | 2026-08-19 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea475c42-5254-38dc-b2a3-8eb5e7d58310 | -4.01184 | -48.06164 | 2026-08-19 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 54dc08ab-9aa2-372e-b521-089df090334c | -5.49487 | -46.65469 | 2026-08-19 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc9d5652-3e59-3dcc-973a-c506f19701cf | -5.78905 | -43.92136 | 2026-08-19 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README23.md)
