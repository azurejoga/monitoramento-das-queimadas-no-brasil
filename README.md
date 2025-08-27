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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fef3fd79-35d5-3aca-ab32-2f1e1591f060 | -10.0791 | -62.8904 | 2025-08-27 00:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b7ba5f1b-a1d3-3837-b89d-9abb9ca84bd0 | -9.4065 | -60.4941 | 2025-08-27 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 8f811265-1c7c-3f0e-9f41-4673a2aa367a | -6.6385 | -53.3362 | 2025-08-27 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1ebb5733-863e-3052-80e3-3b3b6c9a8f61 | -9.0586 | -66.07 | 2025-08-27 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a1a01e98-a322-3716-b374-61a3665b5551 | -9.8101 | -64.2642 | 2025-08-27 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| fc7ce63d-047e-3fcb-8dc0-042f3d4c3e3a | -9.7915 | -64.265 | 2025-08-27 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 8bce9f41-6624-32f6-a603-5392d9cc730b | -9.181 | -60.8131 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 2ce8d2c7-cfcf-39ca-af6a-05d3ee647f31 | -10.0977 | -62.9085 | 2025-08-27 00:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d89c5cc6-f8e0-368a-8a00-60186e75a8cb | -9.1009 | -49.5621 | 2025-08-27 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| a37f1583-70fc-3b03-b931-f43315faa358 | -9.1007 | -49.5835 | 2025-08-27 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 425c3dc6-7079-3a39-8a99-90084ca0a3a2 | -13.1644 | -45.2897 | 2025-08-27 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 446ad8a8-4b34-334d-9531-e92adbba617a | -6.5769 | -47.3881 | 2025-08-27 00:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 78b6c2a2-1e43-365f-8257-ad85b6aa523c | -8.9026 | -60.769 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 0bace6c3-43c5-3c00-b223-7aeeecc43c09 | -21.5776 | -47.4852 | 2025-08-27 00:00:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 393771e4-8dbd-324c-9b5b-748a5f301fa1 | -21.5984 | -47.48 | 2025-08-27 00:00:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 679da453-34d1-38bc-906e-9d36b0e77851 | -5.1181 | -43.1964 | 2025-08-27 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| a5dd1e43-46e6-33df-bd0a-0aa59d7ba0c0 | -13.1837 | -45.2865 | 2025-08-27 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 9b194197-a18b-3dc6-bc50-69c4bd9afbba | -9.4062 | -60.5326 | 2025-08-27 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 259.4 |
| dfc8e4f1-7824-310f-b6e6-60bd2ee27593 | -9.425 | -60.5124 | 2025-08-27 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 8edd13ff-0c2f-3039-98f4-e43e7738959f | -12.7451 | -48.1819 | 2025-08-27 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 2e7bc4d1-77e3-3d97-8ae9-a2945d1e9dd9 | -9.8102 | -64.2454 | 2025-08-27 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 8d2a8547-86de-3fd3-8d9d-317e7f8090b7 | -8.9028 | -60.7498 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 33603ba8-06b4-3edf-8149-cd4c55435c3e | -21.5991 | -47.4562 | 2025-08-27 00:00:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 98ac232c-6955-3b56-98f3-1c5c9ad717bd | -9.0821 | -49.5638 | 2025-08-27 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 6b364595-9362-3871-be28-67beb180a853 | -9.4064 | -60.5133 | 2025-08-27 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 237.9 |
| 096d0cf6-4b88-35ab-8e08-83279cf17d95 | -5.118 | -43.2198 | 2025-08-27 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b2613d26-3e00-3599-a6b1-e27ac3f6c160 | -6.8228 | -58.9753 | 2025-08-27 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 15ef8508-e350-32d8-9be5-85490321c041 | -9.1529 | -59.5609 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 51d11e3b-d618-3ccf-856e-152d285e14a2 | -5.5584 | -44.2539 | 2025-08-27 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 91eba836-bba1-3ff6-8575-c01f3ee1f889 | -9.0819 | -49.5853 | 2025-08-27 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| fd6624f6-bd7b-37e6-8d80-f6398ce39c34 | -4.4977 | -46.3731 | 2025-08-27 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| ba2b5e6f-d9a0-396f-8542-0bf9994001c9 | -21.5783 | -47.4614 | 2025-08-27 00:00:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 7ffe6207-3fef-3ec5-8fdd-603a446fcd83 | -13.1648 | -45.2665 | 2025-08-27 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 718dceaa-3040-35aa-a703-13b90eca6c27 | -6.62 | -53.3373 | 2025-08-27 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 3477dc5a-09a4-3038-ba5c-bcaf2fb36897 | -8.8842 | -60.7507 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 219.0 |
| b3932c63-8362-3cc7-b0d0-31a59fa03038 | -9.7916 | -64.2461 | 2025-08-27 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 3914ce88-c8e6-35d8-bc0e-8d19cef0b783 | -9.1717 | -59.5405 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1e63db34-0637-3083-9a3a-27e7e4ca3625 | -9.5998 | -55.3699 | 2025-08-27 00:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d799639a-b114-3122-89dc-8534dd3719e6 | -6.6201 | -53.3169 | 2025-08-27 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e1ea199f-7a27-3be2-a280-5f1a435f1ac7 | -6.8413 | -58.9552 | 2025-08-27 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| f83ec1c0-5e68-31e1-aab0-edd3c6fc02a1 | -9.4249 | -60.5316 | 2025-08-27 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 207da154-5083-3162-bced-a0ce17e9a387 | -9.1812 | -60.7939 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 68a45d09-378a-3fe1-89ff-04a05493f42d | -6.8229 | -58.956 | 2025-08-27 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 4c9d848f-aa64-3524-b43c-c6afe8dafb04 | -9.4061 | -60.5518 | 2025-08-27 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3ca7edb0-ea11-325a-ae10-24568789f5cb | -6.8412 | -58.9746 | 2025-08-27 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e274df91-92e6-3898-9f2f-deab0ab8e625 | -10.0978 | -62.8895 | 2025-08-27 00:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| fb0c503d-b74a-3c68-a9fb-6c71a083242b | -13.0674 | -46.3153 | 2025-08-27 00:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6c107a3b-96f1-373a-add8-99cbf398a498 | -8.8841 | -60.7699 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 327.6 |
| 5652769f-822e-381b-9e84-d54b360704fc | -8.8839 | -60.7891 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 11febd27-1b5a-3646-9970-495f826c7a43 | -9.0771 | -66.0695 | 2025-08-27 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 50ee659f-aa72-3578-ad19-eef4dd104fba | -5.5582 | -44.2769 | 2025-08-27 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 573cc570-192b-3d7d-9c8f-9f794ab38184 | -9.1715 | -59.5599 | 2025-08-27 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 6adaa176-7e82-3350-a97a-37c21014ea53 | -6.8228 | -58.9753 | 2025-08-27 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 077759e3-0de8-388d-aecd-e0a44fce3e02 | -9.1529 | -59.5609 | 2025-08-27 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 82abb4ac-ffb5-3721-8886-e384eebada19 | -12.7451 | -48.1819 | 2025-08-27 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 6cead6ea-b3b0-3ffe-997c-eed4b4169ad7 | -9.0821 | -49.5638 | 2025-08-27 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 483c21ca-ac0e-3eff-a24c-98775fe08f38 | -9.5998 | -55.3699 | 2025-08-27 00:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9e0f400a-fe9d-3c4c-b6cb-eb89c22430ad | -9.425 | -60.5124 | 2025-08-27 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 05ec4a6b-8bd9-3f6d-82ea-fbac61e3717e | -9.0771 | -66.0695 | 2025-08-27 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 1865344e-ce71-323a-93db-3e02cdae6ee6 | -9.0819 | -49.5853 | 2025-08-27 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 8d083cbf-193c-3b73-9ed4-f0bf9ccc7d07 | -9.1717 | -59.5405 | 2025-08-27 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 463ea77a-be52-321c-ac9e-65f96a311b8e | -9.1715 | -59.5599 | 2025-08-27 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 2317658a-6bb0-3cda-af39-542faa154807 | -9.4064 | -60.5133 | 2025-08-27 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 235.9 |
| 1ebb2e82-a7f0-301e-91a3-5721a0e07d67 | -13.1644 | -45.2897 | 2025-08-27 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| e5f806f4-cd12-309b-a27a-48414831ccc0 | -4.4977 | -46.3731 | 2025-08-27 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bcbd50e3-745c-35c6-876a-7638e385d196 | -9.7916 | -64.2461 | 2025-08-27 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| a08cdea4-ae41-3cee-834b-d69862ebaac7 | -6.62 | -53.3373 | 2025-08-27 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d002ff91-89cd-3e39-a46c-d97611a8487f | -10.0978 | -62.8895 | 2025-08-27 00:10:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a7ffc17a-071c-3ff0-85e4-75db0d0a67af | -6.5769 | -47.3881 | 2025-08-27 00:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 82deaf48-34d1-318d-9a4e-9ec46dde89b8 | -6.8229 | -58.956 | 2025-08-27 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 206a694d-afdf-3f96-91a1-fdd933bcdd0d | -9.4065 | -60.4941 | 2025-08-27 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| b6e04509-1ef9-3705-bf24-857748634c80 | -5.5582 | -44.2769 | 2025-08-27 00:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 13d6f7f0-bc04-38ee-8f72-ed6358db9f60 | -8.9028 | -60.7498 | 2025-08-27 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 9504c636-b24b-3e88-ab85-eeb269b018d9 | -21.5783 | -47.4614 | 2025-08-27 00:10:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 732fe97b-e85f-31bb-93da-77df04591544 | -9.4061 | -60.5518 | 2025-08-27 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 9a7d8d36-197d-376d-ba91-3ece8748a40a | -9.1812 | -60.7939 | 2025-08-27 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ab8ac4f9-9454-3131-9c12-f58ffee1ae67 | -21.5776 | -47.4852 | 2025-08-27 00:10:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 121.0 |
| f681f0a1-46bf-3e4e-a035-97532f35d9b8 | -9.1009 | -49.5621 | 2025-08-27 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 5609c40c-990c-3287-b1c5-c88850e81e2e | -8.8842 | -60.7507 | 2025-08-27 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 8322fa5d-6814-3fe2-8815-1d29e62efb42 | -10.2742 | -64.5096 | 2025-08-27 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| e0e60026-3554-3660-a36a-064a8e4d2ac3 | -6.8413 | -58.9552 | 2025-08-27 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 50712768-fc15-373a-919c-33f6a048c710 | -13.1837 | -45.2865 | 2025-08-27 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e9a9193a-62d9-352d-93f9-a73a24ec15de | -5.118 | -43.2198 | 2025-08-27 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 845db59c-e847-3eea-b101-fb82b47a6043 | -9.1007 | -49.5835 | 2025-08-27 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 6cca2e20-4e94-311b-9e1d-67878a78eec1 | -9.7915 | -64.265 | 2025-08-27 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2c74d22c-369a-3b15-925f-c379d5cdf46a | -21.1071 | -48.8334 | 2025-08-27 00:10:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| 2b0d482b-2cad-3ef3-9663-a99856b2f73c | -6.8412 | -58.9746 | 2025-08-27 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d8713ec0-5e1a-398f-810a-e3c44aad07dc | -5.5584 | -44.2539 | 2025-08-27 00:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 24b773b4-c643-3f0a-94bc-01c19881d762 | -21.1064 | -48.8566 | 2025-08-27 00:10:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| 95577a80-6411-309e-a10c-1134e155aa2c | -9.8102 | -64.2454 | 2025-08-27 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 279a6068-bc8b-3765-82e3-f09a7e0f9cba | -8.9026 | -60.769 | 2025-08-27 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.7 |
| fdcb64d5-e783-3782-ba7d-194aaf4a4c18 | -21.5984 | -47.48 | 2025-08-27 00:10:00 | GOES-19 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 58aa09a9-2cae-3a96-8f08-1ac1d773f2e1 | -5.1181 | -43.1964 | 2025-08-27 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 91e618da-2b51-3911-82a3-55a3c3e1cbca | -8.8841 | -60.7699 | 2025-08-27 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 327.6 |
| 293fe174-b8bb-38e5-b678-0591879b6e44 | -12.9068 | -44.658 | 2025-08-27 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 30afecf1-7ab6-3a81-95b4-26af2fcf9cc1 | -9.8101 | -64.2642 | 2025-08-27 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d273de45-7d50-3f53-b110-e7ac1e63bdc0 | -8.271 | -45.1149 | 2025-08-27 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 5ea3fe7c-05c0-3698-81b2-9917dd70d7c7 | -9.181 | -60.8131 | 2025-08-27 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 3ff62cf0-cbbd-3b9a-8b72-fb133f84f135 | -9.4249 | -60.5316 | 2025-08-27 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a1b66811-c5d4-3b1f-9868-2071c9205019 | -9.4062 | -60.5326 | 2025-08-27 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 219.4 |


[Clique aqui para ver as próximas entradas](README2.md)
