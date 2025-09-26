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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8599fd99-269c-34e3-821a-83852da009cf | -8.86072 | -46.20942 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc666344-f118-3bfd-8036-485abe62ddf8 | -5.24146 | -43.72966 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33677bdb-0c60-3b89-b190-3b3a79e60b9c | -5.68576 | -43.06756 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db764823-6400-3b35-9444-55bb99f336a5 | -7.53047 | -47.28547 | 2025-09-26 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89ca7e98-8474-32f9-81f5-1694f672ed78 | -5.73262 | -42.63779 | 2025-09-26 04:14:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 21700e29-5051-39b2-ac4b-212ba0a50226 | -10.00766 | -44.17523 | 2025-09-26 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e546f69-89e8-364d-8546-843892aead4c | -7.31216 | -45.77031 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5853efc4-4b2e-3cbe-9149-7d904075b995 | -8.65672 | -44.02559 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb369d17-6ba0-3e46-b67d-cc13cf057ab2 | -5.77803 | -42.80713 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ca91240-a66d-3fd0-bbd2-c9e837cd1e88 | -9.93614 | -48.79162 | 2025-09-26 04:14:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 220fdccd-6b71-3748-8836-43020a49a340 | -10.94514 | -44.2948 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 583253eb-42a7-31a8-b57e-d6fe0dc44a1d | -5.7227 | -44.99057 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f613855e-191c-33c4-bfcf-bbf0b8b335b1 | -6.99631 | -46.99098 | 2025-09-26 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18ee416c-315c-3065-9595-15a2aadbc5e9 | -10.5902 | -44.0659 | 2025-09-26 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8f2fd11-11c3-3d6d-8dde-7fec330ba83b | -3.25053 | -46.60401 | 2025-09-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10cc6604-8298-37c1-bbb2-1916ee5a26ac | -9.11279 | -48.89643 | 2025-09-26 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b97dff2c-3ee8-3443-99d9-f1070cbeabb9 | -6.67849 | -43.5958 | 2025-09-26 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8eacdc04-2d66-3aee-a8e3-fb3688a957b7 | -10.11335 | -45.33377 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd0485b9-9062-3894-b16c-9d9a559994e5 | -5.46564 | -43.06069 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7f5d2d09-2511-3b12-a01a-ab4aca1ff723 | -5.78018 | -42.79335 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 894a23f7-2427-3c88-8a05-a464582eaea4 | -10.4103 | -46.17126 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2325fe2-a84e-3e0d-ba9c-05ed7ee97bf9 | -7.28204 | -42.98093 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b7b654c-19bb-31bc-af75-ec7298dbfe85 | -6.26318 | -42.48723 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3febd031-86ca-395b-9cc8-1049778125ee | -9.76305 | -45.6308 | 2025-09-26 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eb1ee83-ad39-3f8f-9993-1bdbfcf06d28 | -9.47334 | -48.23346 | 2025-09-26 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8dfae78-2c5a-3141-9bfe-41241640f364 | -9.99754 | -42.56973 | 2025-09-26 04:14:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0c64ec6-87ad-3946-80f3-c71d0deb6eed | -4.69974 | -46.48206 | 2025-09-26 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc2a646c-426e-3d54-a69a-4ed1f754953c | -5.72177 | -44.95242 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b23308b7-ebe9-3d45-af3a-32fb9d59c4e4 | -7.12133 | -42.19312 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3f08faf3-6f10-3f1c-ad90-2b923829a557 | -10.93192 | -44.27122 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eea3c03c-2d71-3c95-9fc6-b11e7d6f5e89 | -7.80288 | -46.01456 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 68c7c37f-54b4-3cfc-9379-c7c7aa46899f | -4.80135 | -43.04366 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b64797b2-83f3-384b-8903-c914be1bc277 | -5.71824 | -44.97461 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eee573f8-d1b9-39f1-a3c8-b08a21270ad2 | -4.7891 | -42.82012 | 2025-09-26 04:14:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 7cacf1c0-ed18-306c-bc58-e47518c05b7e | -5.73367 | -44.96557 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a91ab3c1-9548-30dc-8ce6-a4b43bb943a4 | -4.74918 | -43.26819 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fe596e81-3a36-3ee9-9ad5-444a9de703d2 | -4.48953 | -41.46196 | 2025-09-26 04:14:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fca54219-0dd2-3466-acd4-10866056a675 | -3.33253 | -44.44799 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a2ebf61-f065-32cc-a563-7f398d097738 | -9.95309 | -46.28051 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62862382-5785-3d6c-885d-ee140b2f4f82 | -5.78554 | -42.75891 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7b7227c2-d9ea-350b-a183-78b6de026d3a | -3.93998 | -47.56392 | 2025-09-26 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d6034e6-1c46-353d-a2dd-d5bf0560860b | -6.26479 | -42.47684 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6fcd6df5-bfb4-3fa8-987a-b131ee2ed3da | -7.31074 | -43.81713 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b18d20f5-61e6-36cb-908d-e03902c790a1 | -4.99866 | -44.88165 | 2025-09-26 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95c894ca-7273-33f1-ae49-fcf2eb4552e5 | -5.53148 | -43.87585 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bdd01cb8-a3da-3bec-8d68-0a553b35f91d | -8.71365 | -47.12221 | 2025-09-26 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5f3179a-3a1f-3502-8868-5d9b66c460c7 | -10.13591 | -43.9432 | 2025-09-26 04:14:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d22876d-77aa-31cf-92bc-ee6ba5db4430 | -3.63369 | -43.86828 | 2025-09-26 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa334d16-f82f-38e0-a601-0d9ab5f0b764 | -5.7646 | -42.89312 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53dcfd7e-fda4-3f50-a53c-00dc778f2cd4 | -5.24657 | -43.06871 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1efed3d-203e-3b4f-8ca8-aa108c270ae1 | -4.00941 | -43.27502 | 2025-09-26 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1cfca1b-edaa-3346-8a0f-249ee2eb9053 | -6.21592 | -44.98404 | 2025-09-26 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dfe2c98-33b2-308a-b18a-34eeea749418 | -6.13972 | -44.86723 | 2025-09-26 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f5b5ef6-ce9b-3e23-82c4-c686ad5c5715 | -7.48636 | -43.89168 | 2025-09-26 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a11f5282-c6a7-36c2-9f8b-39d2895ef2cb | -6.55341 | -44.32253 | 2025-09-26 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32f2d503-a6a9-353b-9515-5d8656c7bdf7 | -8.66055 | -44.00129 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6351013-4db9-30e9-ac60-473aa3fb6e4e | -10.39753 | -46.18481 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b4793dd-0d71-3ec3-a7ee-ff5089491f9d | -9.71036 | -48.2515 | 2025-09-26 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e6cdcd6-643f-3e26-baae-149d63744e22 | -6.26596 | -42.49122 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc0b88fd-fba8-3994-8482-8f8669e267d6 | -10.41311 | -46.17559 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1179f43e-9efc-304a-a952-c0e73e6b92a9 | -3.84486 | -40.33716 | 2025-09-26 04:14:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3ed30b17-52c0-3b6b-b46a-049197e29209 | -9.67997 | -37.08659 | 2025-09-26 04:14:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 46ed8408-732a-32b0-af12-624cf18842c1 | -7.05534 | -41.43123 | 2025-09-26 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e4a29128-a73c-3e3a-b228-5a0b5d97a729 | -6.68179 | -43.59632 | 2025-09-26 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2bd3928-402f-3d60-89b6-72e99aa5053c | -5.77588 | -42.82092 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d8ad9b41-4c39-3abf-9603-859f987d5aea | -8.78783 | -43.05423 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6df4e1ef-326e-3db8-bdbe-052c2eb3e9d1 | -3.35965 | -44.78626 | 2025-09-26 04:14:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e02c3fb-d417-3019-827d-56504c13eeba | -9.52169 | -43.07974 | 2025-09-26 04:14:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26776b16-2bd8-3a66-933f-47db98ee6935 | -8.67869 | -43.99348 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e361d7f-853b-321c-a5b0-435033a83bad | -7.59125 | -44.11104 | 2025-09-26 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2c10135-b37b-3fd9-b1a4-5b26fa376176 | -6.57027 | -43.65643 | 2025-09-26 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 623cf38b-10ae-35ea-b1b3-eadf185ca72f | -11.28294 | -40.978 | 2025-09-26 04:14:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0cbb857c-687e-3c36-b91f-f1e485fbb7d7 | -5.72165 | -44.97514 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48542a90-e4b8-336c-bc5b-9143d63f2fdd | -6.4746 | -41.90796 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 56492b2b-0dfc-3a02-9988-7061ec7a4d60 | -9.99648 | -49.26274 | 2025-09-26 04:14:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db6b0ec2-51a2-35ed-9721-1e037fd4b217 | -5.79198 | -42.86922 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 66397dd8-39cb-3c39-bd97-689881976f7f | -9.89845 | -46.18621 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abfde831-987a-3b94-830c-78065c568a7b | -10.30126 | -47.51479 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc789f52-977c-3f6a-9d6f-d4b3fd7f0e00 | -4.81847 | -42.74027 | 2025-09-26 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 934aa507-c1c4-3f62-91f1-01c1f272d990 | -5.7479 | -44.96404 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 10b25b09-5a02-31f0-a684-742b9dc42964 | -8.51711 | -48.22176 | 2025-09-26 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ce0574a-a306-3e41-886c-e080e5ecc8ab | -9.44022 | -40.37851 | 2025-09-26 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 77c2b734-ccf4-35eb-8d82-1fe2adb320cf | -10.9281 | -44.29565 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc4998f1-1409-3423-ab4f-ac0c3d79a6ee | -7.44651 | -41.90944 | 2025-09-26 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d452e96f-92e1-3989-b981-0b0d8fbf9374 | -6.8535 | -43.17453 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| eb323cf7-d9d9-3426-a9f1-3a9f399a6310 | -5.12602 | -45.49857 | 2025-09-26 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2ed4888-5554-3356-9a71-c67ec3e546ba | -6.13286 | -43.45264 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51fa075a-e342-33c7-a0a1-48f840afe58e | -8.3464 | -42.05358 | 2025-09-26 04:14:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3d2158f-305d-36a2-b2ea-f577450d873d | -5.72343 | -44.964 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3936dcc3-f921-3dbf-acda-6dfbbc35c5e7 | -8.51727 | -44.62629 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| def16ca1-72a7-3563-905b-965e693b5d33 | -5.76076 | -42.89605 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07270194-0937-32fe-8d16-50c627f48353 | -5.74555 | -44.97889 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c6cd9194-e645-383c-b541-4091056c37de | -7.9421 | -45.19883 | 2025-09-26 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a3c2d1d-7727-3015-b573-9efeb06d2a59 | -5.6198 | -43.46647 | 2025-09-26 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a00434a-b09b-3699-9053-2b8de3b91a80 | -5.74955 | -44.9757 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c228f6a6-899b-3dbd-b295-61edcea3922f | -6.07564 | -44.07339 | 2025-09-26 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4d482fd-05d0-3a3e-95e1-3f67ac30697e | -6.5916 | -44.61597 | 2025-09-26 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87f8919c-0cbb-30b1-b649-f39efa18d189 | -5.73155 | -47.98238 | 2025-09-26 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33e07528-124f-3077-b663-2d59575918cd | -3.84897 | -50.97314 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24358e45-b6b5-3318-a516-c1197d8745fc | -4.48519 | -47.6782 | 2025-09-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README17.md)
