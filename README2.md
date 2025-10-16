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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbd6ff92-f9bc-35a2-91f2-edb19bd24644 | -7.9628 | -44.1362 | 2025-10-16 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 269.2 |
| 9c31e26c-5341-3108-8781-7ebe5bfb9f4a | -4.8644 | -44.5748 | 2025-10-16 00:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 73a094c7-f638-3270-abad-24df1790018c | -10.8856 | -48.7923 | 2025-10-16 00:10:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b949b291-1b54-3d5f-b9d6-453e034fd8f2 | -7.9817 | -44.1342 | 2025-10-16 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d3a2d89b-1af4-340a-9466-5d83e4fcda4d | -7.4706 | -42.7605 | 2025-10-16 00:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 173.1 |
| b1306de1-69ec-37fb-9de9-880a944bf1f3 | 1.8401 | -55.7429 | 2025-10-16 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| f089b5f0-ae2e-39e6-8c91-3710dadb9f11 | -15.1939 | -49.4083 | 2025-10-16 00:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 7fcb0ed1-dc86-3569-9c85-0a3c77f899ca | -12.6805 | -43.4235 | 2025-10-16 00:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 302.6 |
| eb75d3ca-eae9-3b86-b274-19bfb788cb18 | 1.84 | -55.7626 | 2025-10-16 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| b4240056-f253-347e-b8b6-5515ae76fa4a | -8.4714 | -44.1978 | 2025-10-16 00:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d0cdd8ca-d683-3589-bfec-27605142e9d3 | -4.5041 | -45.4118 | 2025-10-16 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 7d5c6f9e-a574-3eff-9505-9227dbbc2961 | -9.2397 | -63.2678 | 2025-10-16 00:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| addbbbc3-93e1-328f-9187-93f21a9da81d | -7.9439 | -44.1381 | 2025-10-16 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 53f10ac4-7651-30c1-bdf9-69e1d2b7cb96 | -5.2068 | -43.7945 | 2025-10-16 00:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 70cc7cd6-db9e-38c4-8f87-b443f165543d | 1.8401 | -55.7429 | 2025-10-16 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 613e997b-d3a0-31ac-a58d-07d843dc65a4 | -12.6607 | -43.4507 | 2025-10-16 00:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 0e6937e6-7af8-3118-a3f3-51917216c0d2 | -4.0974 | -48.0361 | 2025-10-16 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 5d95f7a9-fdbc-317c-b4e8-e4bd51f766ae | -10.2334 | -46.7262 | 2025-10-16 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| aa92ae23-6eb1-3481-b9a8-5ba6608c5308 | -3.2737 | -45.8509 | 2025-10-16 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| bdd0ab18-bf97-36c6-9973-6e4569d4b552 | -12.6612 | -43.4268 | 2025-10-16 00:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| c39d79fc-3a02-3dc8-8305-21bc6e16c4ac | -4.35 | -43.3849 | 2025-10-16 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| bd41c84e-33f2-3895-b00d-47582c75a789 | -7.4706 | -42.7605 | 2025-10-16 00:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 251.1 |
| e7fd4709-b553-3456-b84b-6eafeeb4c238 | -8.4528 | -44.1767 | 2025-10-16 00:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| f1234613-148b-3a00-977c-3364ce2387ee | -7.4897 | -42.7349 | 2025-10-16 00:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 1f4f4b5c-2a06-35bd-b758-5772f59846c5 | -10.8856 | -48.7923 | 2025-10-16 00:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9aceb242-71f6-3fa1-ae15-db40310e8251 | -11.4368 | -44.1641 | 2025-10-16 00:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| a5b0194b-4c28-3350-933c-5b6d8135076c | -4.5042 | -45.3893 | 2025-10-16 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 132.4 |
| db6d8a6f-5d54-3ff9-a285-76161f6b75b5 | 1.84 | -55.7626 | 2025-10-16 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 476b32d6-7de1-347d-82c2-3904f3bab59e | 1.8401 | -55.7232 | 2025-10-16 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| cb4db724-6378-3959-a614-bc99d2c17740 | -5.4762 | -42.9367 | 2025-10-16 00:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 2b103f7e-97ed-38c7-a826-09ed7e3ead8c | -3.2298 | -43.4646 | 2025-10-16 00:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| c577f5cc-da89-35d2-8c8f-f9f87d6fbbdb | -9.2255 | -48.6 | 2025-10-16 00:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a6dcbbc9-0a1f-3deb-b6bf-247e574c0b49 | -7.9817 | -44.1342 | 2025-10-16 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f09a5f3f-0a47-35dd-acc9-ad601377a3b6 | -10.133 | -44.5777 | 2025-10-16 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| ac75753f-b02d-30f6-9f0f-cd6c574764df | -11.456 | -44.1613 | 2025-10-16 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 20812f4a-2c46-3fd5-8c1c-4d247d28d80d | -3.2738 | -45.8286 | 2025-10-16 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 0cc92c01-b05e-3999-a4e0-9dd20926cbcc | -4.3687 | -43.3838 | 2025-10-16 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 291.8 |
| 628bc9e7-4981-3904-85e4-2686f8e2b75f | -4.116 | -48.0352 | 2025-10-16 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 4c1c27fa-8bf2-3241-9aa0-0d4f255275ed | -7.9628 | -44.1362 | 2025-10-16 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 1fb41268-74e9-3dc7-97bd-22801a33b915 | -7.9442 | -44.115 | 2025-10-16 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 0bd8365b-8323-33c9-a7f7-2ae982687eb6 | -4.3685 | -43.4071 | 2025-10-16 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 292.4 |
| bbc8aaf6-d237-319b-9006-8d13deff6a74 | -10.8666 | -48.7945 | 2025-10-16 00:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0b50e57f-fa72-3e6d-94b0-7e9359bc52fd | -4.1161 | -48.0136 | 2025-10-16 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| f6a001e0-8f8f-3dbe-8735-25f8c7f186fc | -12.6801 | -43.4474 | 2025-10-16 00:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 944adea6-80ba-367b-85c4-952adebc2852 | -3.0157 | -45.3903 | 2025-10-16 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ea0dc710-0901-3865-9011-f2e658d3e3fd | -12.6805 | -43.4235 | 2025-10-16 00:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 254.2 |
| 6e4e57ac-9bd9-370d-b933-91eb153fadc9 | -7.9631 | -44.113 | 2025-10-16 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 1d9285f1-01ef-3c25-b646-594a93c78d86 | -9.2398 | -63.2489 | 2025-10-16 00:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 0ef0f48c-4ffb-3413-8f70-80027945c628 | -4.3498 | -43.4082 | 2025-10-16 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| af72fa44-ab64-331e-9f97-6d20bc4a7ef7 | -7.4708 | -42.7368 | 2025-10-16 00:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| c4804fb7-946a-3266-a32e-b29f295c59a3 | -11.4556 | -44.1847 | 2025-10-16 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a254366c-e35c-3c73-adab-3526838cd743 | -4.3872 | -43.406 | 2025-10-16 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |
| e637205e-3d8a-37a6-acde-c7e45cce9ca8 | -8.4717 | -44.1746 | 2025-10-16 00:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 9af374eb-7a15-324d-b92e-084e282b87a8 | -26.8188 | -50.5512 | 2025-10-16 00:20:00 | GOES-19 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| e2721069-7b48-32cf-a029-dc184b282893 | -4.3874 | -43.3827 | 2025-10-16 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| b6acf6a2-7d64-3308-94dc-bb5e9d83e394 | -5.9221 | -45.434 | 2025-10-16 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 8ccc6ee1-b33f-3ead-bd0e-a3faf75f1c7d | -7.4894 | -42.7586 | 2025-10-16 00:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 154.3 |
| 1d007f8d-3d6c-3f41-8b04-c4c48b333392 | -4.0976 | -48.0144 | 2025-10-16 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| cd045130-2f24-34b6-a3cb-88f4355a75b1 | -5.2255 | -43.7932 | 2025-10-16 00:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 385163b4-0cea-3798-bbcf-7568362fc443 | -4.0976 | -48.0144 | 2025-10-16 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 26446df3-ad75-361f-ba12-c0563768f71f | -7.4894 | -42.7586 | 2025-10-16 00:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 127.0 |
| a20190c6-5fe1-3e19-bd86-8c3e323f9df2 | 1.8401 | -55.7429 | 2025-10-16 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d7974c2a-df73-3193-85a1-434e90c5f46a | -4.4856 | -45.3903 | 2025-10-16 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c334511b-94f7-3efa-94b6-0805cb7e0a41 | -7.4708 | -42.7368 | 2025-10-16 00:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 48b8e68d-b4e8-3edf-ac8f-4a75d5a2f825 | -8.4528 | -44.1767 | 2025-10-16 00:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| f489fc9a-d76e-30aa-acfb-0b389b04b0b5 | -5.4561 | -41.0054 | 2025-10-16 00:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 7c7dbbb6-f710-33a3-b3e6-a45b6c5a97cf | 1.84 | -55.7626 | 2025-10-16 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 35a6d42a-77a9-36ef-a2df-2441f8207aa4 | -9.2255 | -48.6 | 2025-10-16 00:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| f5378cc4-22fc-3728-a1bc-319e14d09925 | -9.2398 | -63.2489 | 2025-10-16 00:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 4ede0d5e-2dd5-37d0-8e46-834d329fec10 | -7.4706 | -42.7605 | 2025-10-16 00:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 195.2 |
| 607ac341-a130-3aca-b44a-d2e7605af9ea | -10.133 | -44.5777 | 2025-10-16 00:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 7f716682-b0bd-34fc-8597-e44dd7f502f0 | -5.9221 | -45.434 | 2025-10-16 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| a4cf75a4-39df-3a70-a72a-2e2299e55364 | -4.5227 | -45.4108 | 2025-10-16 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c958b1e1-210a-39d7-9039-e8f23764eba5 | -4.3498 | -43.4082 | 2025-10-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 07ae6de7-13a8-352a-a800-c808b4020549 | -7.9817 | -44.1342 | 2025-10-16 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d0669920-8a9d-3656-9114-0f4aa6f11c22 | -4.3874 | -43.3827 | 2025-10-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 237.2 |
| 32f12dfa-4d45-3fb9-8bab-5e2962a4b6c0 | -3.2737 | -45.8509 | 2025-10-16 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7e25ab6c-78e3-3e23-86cc-736798a3c454 | -3.0157 | -45.3903 | 2025-10-16 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 66e5e901-9886-3108-9d6b-a0b0f4945d76 | -4.116 | -48.0352 | 2025-10-16 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| c6b8eab4-6ef6-3728-bc39-42889897b5f4 | 1.8401 | -55.7232 | 2025-10-16 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b1877942-9850-3a2e-a670-433303666a3e | -12.6607 | -43.4507 | 2025-10-16 00:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| e200c60e-511f-31f1-a80e-1d41508152ce | -4.3685 | -43.4071 | 2025-10-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 331.5 |
| bddc7a1f-d838-35c2-aab5-c47847dbd6b1 | -12.6612 | -43.4268 | 2025-10-16 00:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 201.9 |
| fe87decd-200c-34a3-a534-90891eba0082 | -5.4762 | -42.9367 | 2025-10-16 00:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 8719da33-9a77-3cad-8d0f-330ff2ec452d | -7.9628 | -44.1362 | 2025-10-16 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 205.6 |
| e891ffd9-367f-3772-864f-9df3765272b9 | -8.4714 | -44.1978 | 2025-10-16 00:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 9ecc3ba4-8497-3d71-b163-9d2d7d4d56f0 | -11.4368 | -44.1641 | 2025-10-16 00:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| aed24b87-751d-311f-8c0b-d8de407eb232 | -7.9439 | -44.1381 | 2025-10-16 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 5d5559c4-79a5-34ea-ba8f-46a78d6c6eef | -4.5229 | -45.3882 | 2025-10-16 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 37c0fce6-1350-342c-a7fb-736c9e380119 | 1.84 | -55.7824 | 2025-10-16 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 8caba8c0-ea11-3542-ba8c-0263d67077f8 | -4.0974 | -48.0361 | 2025-10-16 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| c02a9731-5286-38c3-9be7-e8ccbc2af859 | -5.4558 | -41.0297 | 2025-10-16 00:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 47.3 |
| b7ac678f-7505-3d0e-8800-1182b808b478 | -12.6805 | -43.4235 | 2025-10-16 00:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 280.4 |
| d932527d-bbb1-360d-b3de-a7e0bb4df73c | -26.8188 | -50.5512 | 2025-10-16 00:30:00 | GOES-19 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 49.7 |
| d2128980-48b1-3e10-9668-d80aa3b815e1 | -11.456 | -44.1613 | 2025-10-16 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 92c72adf-7cdc-36de-961d-4777a8a3c949 | -12.6801 | -43.4474 | 2025-10-16 00:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 750dc260-5de8-3e4c-a396-3ac1027f1d02 | -4.4854 | -45.4128 | 2025-10-16 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 2ffd859b-3c1e-303a-bc2f-b1feb6e7d167 | -4.3872 | -43.406 | 2025-10-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 93235734-95f2-3fd6-b608-e17e79a7d42f | -4.35 | -43.3849 | 2025-10-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| a9f39f6a-3b24-3b05-ba48-ac64a1e41643 | -4.5041 | -45.4118 | 2025-10-16 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 101.1 |


[Clique aqui para ver as próximas entradas](README3.md)
