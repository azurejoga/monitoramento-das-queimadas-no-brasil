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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f59dac40-65db-367c-b9d8-c8442337744e | -10.8677 | -44.80315 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13f179b5-79ab-3f45-8e43-76b737a47f79 | -10.86656 | -44.78844 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11317a09-c12e-31ba-93ba-efbb891849bf | -10.86601 | -44.79198 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f01d5d3-be55-30a4-92b4-530a9f4dadbd | -10.86546 | -44.79553 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae68df46-1fb6-38b1-af96-add3f2888981 | -10.86323 | -44.78791 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07c47e44-66ae-3ffa-a665-fee8e676c118 | -10.82437 | -44.95179 | 2024-10-14 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c576de9e-1e3b-3b05-96fc-e31628989307 | -10.7379 | -44.69569 | 2024-10-14 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9d48a2d-eb1d-34c6-bc38-04a221e9b200 | -10.73736 | -44.69925 | 2024-10-14 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 739eccf2-a733-3211-9950-eec6a4248ac6 | -10.72738 | -44.69766 | 2024-10-14 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9aa2989-2e22-3244-9a47-67e2e72133db | -10.72635 | -45.20994 | 2024-10-14 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cd981e4-7e5d-3512-936f-212174f294f3 | -10.51661 | -44.85247 | 2024-10-14 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b4b7cd8-e3d3-3d2f-a083-01e69739677e | -10.51607 | -44.85599 | 2024-10-14 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a880af36-6a41-3cf7-b817-1a47f0c754aa | -10.51392 | -45.15428 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d824afa-fe14-34f8-973b-c8132da6b671 | -10.51329 | -44.85194 | 2024-10-14 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0bec27f-9e0c-33af-8dfa-423805199484 | -10.51275 | -44.85546 | 2024-10-14 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c40d6a21-3457-339d-972a-e86241d61bfb | -10.49024 | -44.9133 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b96e697-629d-33cf-88b1-e652d29be9ca | -10.45247 | -45.02608 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a3288eb-9bc9-379a-abcc-fd67087503b5 | -10.44916 | -45.02555 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| accb76c5-c764-3829-a407-ba1f5cf59306 | -10.44437 | -44.94568 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 96ba35a0-40bc-3592-b21e-b17d7b9d55a3 | -10.44382 | -44.94919 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0eb8cd9b-d598-3357-9781-f034591f63f5 | -10.44106 | -44.94515 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f460c795-7aac-3370-a5b0-9428e84317e9 | -10.44051 | -44.94867 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b7a50450-c6d9-3a70-bf95-1bbba6564280 | -10.43774 | -44.94463 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6a603a93-3272-3d48-8db2-e9144030151b | -10.43607 | -44.93356 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c6fe3ae-517c-3dec-9de1-942e831c571f | -10.43552 | -44.93708 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 99327f44-6d53-3caa-8889-59e7314cba31 | -10.43443 | -44.94411 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 868106d8-5ca8-3214-b582-df19e7141f92 | -10.43275 | -44.93304 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c4d4f6c-15ba-395c-8278-735aa45612c2 | -10.43221 | -44.93656 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 064e9c88-8910-350d-b3af-a6998dbe7221 | -10.66951 | -44.49903 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16b84fe0-815b-33cc-a7bc-e58d8e01e272 | -9.83257 | -45.05266 | 2024-10-14 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cf8fd4b-56f8-37c3-b4ee-a6013a059abc | -9.83203 | -45.05614 | 2024-10-14 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dbbd16f-dcf3-3ba0-937a-30b805ded7cd | -9.82651 | -45.04812 | 2024-10-14 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e028901a-7829-3666-808a-a2e6c5e1a87a | -9.82597 | -45.05161 | 2024-10-14 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b6c0e50-616a-3866-adbd-0ba2cc252b32 | -9.82542 | -45.05509 | 2024-10-14 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29161f2f-48ae-3b54-b5aa-e34a4f0db584 | -9.56769 | -44.47895 | 2024-10-14 04:21:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b1bff546-4ac6-3746-b425-47c878f6f4b2 | -9.42356 | -45.51447 | 2024-10-14 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4d87418-2f01-3c60-a85f-203191e64dd1 | -11.58572 | -45.01863 | 2024-10-14 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec13b8fd-d0e7-36d2-9d03-4de33690a8b8 | -11.5609 | -44.85018 | 2024-10-14 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 28cd3afe-d40a-3bf9-8ef8-8437207cb815 | -11.55757 | -44.84965 | 2024-10-14 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 236cce4d-dc12-3607-8400-5207aa7dafb8 | -11.03452 | -45.28445 | 2024-10-14 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06d59d39-24de-3286-917e-8b93a2f7274e | -10.95346 | -44.68584 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78918177-cae8-3202-badc-1bcecccd4e9b | -10.95292 | -44.68941 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63c3c340-0c95-3869-9272-e9212ace1d3b | -10.94897 | -44.67052 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cf79186-b861-3709-9993-2d478ec0b327 | -10.9472 | -44.63733 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05a16e7a-e113-3e12-aa78-b6dc599351c6 | -10.94292 | -44.68784 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49d350f5-f753-3273-9a07-d51284c9f621 | -10.94122 | -44.67661 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5191a86-bb1a-3c39-88f1-afc5e036d31a | -10.93959 | -44.68731 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c05e842-7741-31c4-82b9-a7d9a6d76c99 | -10.97473 | -44.54631 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd1acf12-5325-3482-b17b-9ca23aba388b | -10.97139 | -44.54579 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eea27308-6c2c-3b0d-b2e9-a9298bde2180 | -10.96859 | -44.54169 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17eb464b-bac6-3cc3-82d9-599e6674ad28 | -10.96804 | -44.54527 | 2024-10-14 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dd90485-e821-3d22-9589-66e8ad92f766 | -13.70967 | -45.46565 | 2024-10-14 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77b55430-8220-3044-a9cb-f49dffbd368b | -7.97576 | -45.60913 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf45e271-f929-348f-980c-0191351273c2 | -7.97466 | -45.61608 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f2148ba-cb2c-3907-b2a8-5cddc01b76f4 | -7.97246 | -45.60859 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 105d1069-1ec7-3489-98be-24dec5a7ed24 | -7.9719 | -45.61207 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee4573c3-4ef4-364e-b7c4-ae6ab4510ea4 | -7.97135 | -45.61554 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 512b5454-4c63-31bb-a436-800152baee02 | -7.91835 | -46.16137 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b25fa358-0f96-3434-a1ba-8d52bcf38164 | -9.23676 | -46.68586 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c86708b-9390-37b3-866c-dbc7aa2f7bfe | -9.23618 | -46.68946 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b73c733e-c3ce-36b6-9de8-a9fcdef18b1b | -9.23282 | -46.68891 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30274827-370d-3321-965b-3a3d38ad9811 | -9.17489 | -46.62808 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0b4b858-8188-3956-b1e8-6fd9b6e7a3ba | -9.10046 | -46.49853 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ce866ef-1775-3682-9187-e4f91fbba559 | -9.09769 | -46.49441 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d99cbba-d2bd-320c-98a8-ac2bc969b270 | -9.09712 | -46.49798 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31376051-b360-3b5f-8569-fbf9a1f8cc2a | -9.08884 | -47.05478 | 2024-10-14 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1db05b1-f210-3e9d-87c8-6b35462a4075 | -9.08605 | -47.05053 | 2024-10-14 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 009461e3-896d-3c15-aa37-606dac5bd0d3 | -8.77891 | -46.48698 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19ba6d81-345d-3cfa-8b43-cb53c8d6f1b4 | -8.72457 | -46.63298 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 663a1e1e-8e82-3f9f-bd02-720054cee6fd | -8.72399 | -46.6366 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4ff8857-de6b-3839-ba40-c2072620a442 | -8.72063 | -46.63605 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb543cd1-60d8-39ca-ac38-8d971ed16efa | -8.71727 | -46.63549 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e15ebb1d-a511-3521-a126-b4899a797fe9 | -8.71391 | -46.63492 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a09a3209-127b-3672-a3b2-6fd7aa27533d | -8.71056 | -46.63434 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 621158a4-5226-34c9-b0ca-1ee02ddd12c3 | -8.70998 | -46.63796 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b87cf9e9-2ae0-3430-b283-f280dc6e8c8f | -8.70939 | -46.64157 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3e55c90-6e7b-3b25-8668-e60df7e4c67f | -8.70663 | -46.63736 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31dcc17d-28b7-37d3-82dc-66b0450fe3c2 | -8.70604 | -46.64098 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbaa5b67-758d-3d39-bb2a-21b2261c4fff | -8.70546 | -46.6446 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6782c404-4d3a-30ce-bb4c-367ce17a6839 | -8.69761 | -46.7361 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7da10b22-03d5-3d40-8893-6b0af58190c3 | -8.5348 | -45.98948 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a872dd76-faf8-30b5-99ef-1bb4220b1433 | -8.53424 | -45.99301 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 381c789c-9ee0-32fd-b94e-bed571d019b8 | -8.52705 | -45.99545 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b86db84-07be-3c8a-86df-c75c4aaea02a | -8.52649 | -45.99897 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f76b23c1-dc79-3308-b3b2-ede37340f03f | -8.51433 | -45.98982 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cb82202-35d6-3549-b1fd-5edb3e0c30f2 | -8.39615 | -45.76963 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db9928b3-3a8e-3b7e-9263-1b471a769161 | -8.37419 | -46.90924 | 2024-10-14 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1268208f-f33d-316a-993e-db26fc52a194 | -8.36623 | -46.3428 | 2024-10-14 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f8c1ea6-f6d7-392f-9a7a-6a8cf68d39a6 | -8.28779 | -45.72374 | 2024-10-14 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85ebec87-fcf6-386c-b920-da80d0419cf0 | -8.21786 | -46.79305 | 2024-10-14 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 709cc984-dab0-3bd4-b412-ce67b2b04431 | -8.21387 | -46.7962 | 2024-10-14 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece0f12f-85d5-3f31-8fe6-08212f5f187d | -9.49397 | -45.82224 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8954a478-72ab-39d6-bb28-24ed32f923dc | -9.49342 | -45.82571 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b982c0fe-ccb9-3acd-acf3-17623ccd5b08 | -9.48956 | -45.80727 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67a9f438-7f39-35d7-a06b-2a17db18438d | -9.48571 | -45.8102 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f2a3e9a-82f7-35bf-85ad-1408d20d7673 | -9.48461 | -45.81714 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1526eca3-0261-33cb-942b-1b36dffaeaef | -9.48131 | -45.81661 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09a2186b-9c2d-3fb6-ac2b-0f8935beaba5 | -9.46588 | -45.80704 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d847cd24-44fc-3a8f-9fb0-f703e0eec3ff | -9.9926 | -47.35726 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6c8e6fb-846c-32be-9245-f8ba9486ac4e | -9.98981 | -47.35299 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README56.md)
