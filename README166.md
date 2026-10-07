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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb6c2cbd-80d3-3d4e-9882-f3ff86e2dd81 | -6.68816 | -44.96635 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2300afcb-da13-304e-895e-215e5802696c | -5.71093 | -37.70949 | 2026-10-07 16:03:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 5390c94b-ca62-3abc-a393-1dac72696e4e | -6.30336 | -44.11887 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a74977dc-b443-3278-85ef-00686c4e5b04 | -3.82697 | -44.54073 | 2026-10-07 16:03:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fdb8be28-e2ac-390d-8578-bfb667a37178 | -7.39795 | -45.64013 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9fbd0334-db09-3ab3-ac74-9d71fdff271f | -8.03117 | -47.96072 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 33ab07cb-e74b-3c9b-bdd3-a874e785b574 | -7.75185 | -43.83101 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a2154724-4bcd-3323-b332-535132d70105 | -3.10728 | -41.1649 | 2026-10-07 16:03:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 495c9f40-b1cf-337b-840c-a9fb6c305372 | -5.78984 | -43.91577 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ac16233f-da4c-3da4-85fb-b6f8242c5f33 | -2.05677 | -45.97517 | 2026-10-07 16:03:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2c8a933b-3a8b-3716-a68c-02e612314299 | -4.74188 | -43.31258 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00b37c21-1f4f-307c-8d55-0b4e68880524 | -5.84762 | -43.84019 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3263138d-192a-36af-9f47-a9b0a18a095b | -7.00704 | -44.06371 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 42481bec-cf60-3060-91aa-3b905302f570 | -1.87885 | -45.43594 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a7a90e3b-3fd5-37ea-9f1c-fe92f0af92ff | -2.95985 | -42.72765 | 2026-10-07 16:03:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 85c33162-b2b4-3ef0-b228-9abe70d263b8 | -7.00271 | -44.06436 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 36ecf157-a8bd-363a-b6f8-50042eeefbb7 | -5.5549 | -45.26678 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 32991271-de21-3663-9b02-f82fc387cea1 | -6.12248 | -44.80497 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e6c23c7f-d8a1-393a-bbca-4634dc0a295f | -6.94283 | -45.28652 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1f64fb4d-d72a-3112-bc63-253b342379d8 | -5.72172 | -41.73642 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 70b88d98-c0a2-34e0-9a8d-d8df053af303 | -7.27639 | -46.15938 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d6cec45d-65d3-3132-8055-fead9481d901 | -7.30492 | -43.97353 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 4a892254-106e-3537-9029-6bd0c7330bfd | -8.05413 | -45.61145 | 2026-10-07 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aecd6a27-596c-3bf6-be90-72a9acdb50b6 | -5.72301 | -41.74514 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 670faae3-512b-3442-be40-97f581d657d3 | -7.22368 | -44.29585 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 0199cdbe-b064-3fc0-aa7f-035e270db210 | -7.34833 | -43.18233 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 43e9dc08-3299-3c00-a344-f2c964d69d65 | -3.7748 | -41.87711 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| b6615d4d-9008-394d-9742-a758957a1af5 | -3.88786 | -44.1007 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c35e5df0-674a-3ac6-944f-fc0020289895 | -7.75617 | -43.83043 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5e958e20-de82-3ec7-ad35-2599bb066121 | -6.07079 | -45.30914 | 2026-10-07 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 58833c81-39f9-3c82-ab7e-61dd6152a3d0 | -7.46775 | -42.82268 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 373ba878-5ed0-3d23-b7c8-46e8b1548632 | -3.51687 | -43.84407 | 2026-10-07 16:03:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7896b783-3401-34d3-90e3-6cc5774ea395 | -7.7599 | -43.82565 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f87374f7-90f1-32c8-8e3d-64d8e3dc252e | -2.78604 | -51.67986 | 2026-10-07 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f23d99f2-234e-3099-b1cd-0bfd000cdb10 | -6.53278 | -44.1198 | 2026-10-07 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e22da8b3-87af-3254-9c05-9d9414c9a795 | -7.17258 | -43.76762 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b1284a0d-80e4-304f-af10-49f093c35868 | -5.96954 | -40.91995 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 58c6481f-6874-3bc4-a9e3-30944466bef0 | -2.9732 | -42.73964 | 2026-10-07 16:03:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4417f0c0-9334-396f-ad85-d49adc64f99c | -6.6915 | -44.92303 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7b81df14-ee45-39fe-859d-d6ce8c2bcfdb | -7.40282 | -45.63943 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| da4f4769-d766-3669-8178-8332a165ebbe | -3.55122 | -38.90444 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ca3976be-a4af-3869-9a94-d032bf3aecea | -7.2137 | -44.28879 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84625f4d-7309-3e78-b5ff-0af26614f582 | -5.90126 | -43.94032 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 06b79c64-6042-33b6-b19a-960ad123506e | -5.06098 | -37.02475 | 2026-10-07 16:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2c507cbe-d1d0-3e96-93e7-a3b14dd99f79 | -7.10113 | -45.23521 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b9ea1fd7-f9ba-352b-aaa2-41daf99951d8 | -4.96783 | -37.43133 | 2026-10-07 16:03:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 840a8a7d-111c-3031-bb4a-cae3f4c0204e | -4.84227 | -40.39384 | 2026-10-07 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 1c0451aa-4a93-3a28-9cbe-acd3e120b34f | -7.72754 | -46.72725 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ed45c7f-163a-3906-8744-0562fa00c83f | -5.975 | -40.95602 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| b0ee68f4-f974-3897-b75a-965f387e7927 | -3.18698 | -50.55986 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 336d05ee-660a-3c39-9727-0d0c2f245fcf | -4.32497 | -43.8172 | 2026-10-07 16:03:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6d8bfe33-80a9-3d53-bdaa-9c19451b99f1 | -4.18053 | -44.29698 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 50912ea6-b09a-30ad-bec9-17fb8ec8e900 | -6.05715 | -47.32278 | 2026-10-07 16:03:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d364ec16-662d-334f-8161-36fd0cd92d5e | -3.29536 | -39.36819 | 2026-10-07 16:03:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f073bc69-4ce1-38cb-a53b-7230aba982d3 | -3.29202 | -42.27822 | 2026-10-07 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f3dd30fc-b34a-3eba-a5c4-5492a90023a5 | -3.55928 | -39.13576 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 5874a671-45c7-3686-8bd9-c096d4e6e7fa | -7.56052 | -46.72094 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a3df44e0-ab4d-3a16-9ade-3bafdce8bbe4 | -4.03282 | -46.98468 | 2026-10-07 16:03:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b6b9912-33e6-3600-82c9-a6b62c24a103 | -6.05178 | -47.32343 | 2026-10-07 16:03:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 577ac279-e10c-379e-bd1b-dabd12c21723 | -6.53821 | -40.18451 | 2026-10-07 16:03:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b17bec45-d676-3248-9c86-0708d52d6cb9 | -5.48799 | -41.39985 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 84e4de92-1e69-3afc-8c14-bc6522abd2ad | -3.26438 | -50.40948 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 54f765a6-bbfd-3e34-bc5e-434910e90319 | -7.39681 | -45.64442 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 4aa5e6a4-8f03-354d-9b32-0c3abd2d27c8 | -3.88288 | -44.12455 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a1fdb637-e4b6-3482-93d5-aafa8ba939df | -5.95606 | -45.68358 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f5721a2f-7556-3d21-b9a7-989e8cfce3c3 | -5.94289 | -46.38717 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f2e49ce8-9237-3a14-b10b-144897642c39 | -8.02541 | -47.96142 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b3becaf1-ea8d-3f3a-b024-c82b029f9869 | -5.92631 | -35.29106 | 2026-10-07 16:03:00 | NOAA-21 | PARNAMIRIM | RIO GRANDE DO NORTE | Brasil | 2403251 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9eb22425-cfa6-3ec7-a9d1-091c978f8f12 | -4.84569 | -40.39333 | 2026-10-07 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| bd483fde-b797-3db6-99b3-33e9e89a79eb | -2.99218 | -42.83675 | 2026-10-07 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b63337f9-851d-31c2-8958-2f86b9ff826a | -5.93513 | -46.62846 | 2026-10-07 16:03:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 61f5635e-216f-3cc4-ab0e-5c155635c05a | -3.68723 | -45.8368 | 2026-10-07 16:03:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2b11f289-c307-3e2d-8487-7faaba3ce471 | -3.95328 | -41.5453 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 41.9 |
| 621fbe3e-2d6a-3d8b-94a7-ded3df7d5789 | -3.19333 | -50.55902 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5aea0d94-ea4a-3112-9b44-36e437dbf356 | -4.07178 | -38.39281 | 2026-10-07 16:03:00 | NOAA-21 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6c82b826-1a0b-3a71-bbe6-c88e2dba7de4 | -7.76249 | -43.81287 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 19306cb3-42b4-3a17-9b02-59a3b024ccc0 | -5.96373 | -41.34755 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| a6600c67-9c4e-3557-bb2c-f4416cc7beec | -3.06046 | -44.44487 | 2026-10-07 16:03:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e62f95fb-ef20-3dcb-8260-06f182fb5477 | -3.89672 | -44.10325 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8dfe401f-f89d-32c8-b7a6-50166e304084 | -3.15357 | -43.92302 | 2026-10-07 16:03:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7a4d8823-d595-3bf3-8b80-f78c2d81a94a | -3.68255 | -45.83741 | 2026-10-07 16:03:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| a4c01a37-1c43-394d-8047-9ce3c4f1eabc | -4.24872 | -51.04674 | 2026-10-07 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ce4970eb-e63d-32ad-a661-2927dd3b2611 | -5.83541 | -42.42846 | 2026-10-07 16:03:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a26747b6-bb8d-3002-af0d-cc1b1984184c | -7.39754 | -45.64989 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 34a361c1-bc7a-3b50-93d3-cd14c3fc0ab9 | -4.68242 | -40.827 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 1f44aa28-b21c-328f-ba4e-27c816759f8b | -6.33984 | -43.8347 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 17437c4a-cf6f-3806-9d3a-4cee360178aa | -4.27305 | -43.0157 | 2026-10-07 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| f7261100-cf90-3328-852d-4c108eca3374 | -6.89905 | -45.89854 | 2026-10-07 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 796b86a3-8f1a-31de-bf48-dbfc1d2953d5 | -5.98444 | -40.94632 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 26f813ea-6459-3154-9118-c2fcfd9d4721 | -5.72475 | -41.73154 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| a09f1496-b8ba-396e-8791-a6645bc0eb0d | -6.3275 | -43.7486 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| ae1c7d7e-9f8a-37bc-81ec-0be89959b85f | -7.04783 | -44.32247 | 2026-10-07 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 71bd6076-2110-3081-952f-0304a8121d4a | -3.44397 | -50.62181 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6a206146-35a5-3015-a602-9cd562209c35 | -4.27233 | -43.01081 | 2026-10-07 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| b2ebf79d-769e-34c0-a12d-f899a893b126 | -7.57741 | -46.19608 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d62d7081-d4aa-301e-b31b-63194f3a903b | -7.40168 | -45.64374 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 05606ee6-9a1a-3090-8751-e6ff4ac35789 | -3.07 | -44.45137 | 2026-10-07 16:03:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2b0644a4-769e-3f2c-9669-7b5cdc6dfc8e | -4.67838 | -40.82374 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 81894642-89e8-34c5-b965-da426f8b7bbd | -3.89257 | -44.10386 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4a50fa12-f8a5-345e-baa7-0e631601771e | -8.04427 | -45.6124 | 2026-10-07 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |


[Clique aqui para ver as próximas entradas](README167.md)
