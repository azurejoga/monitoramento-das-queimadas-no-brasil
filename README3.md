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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54e3bab1-ab09-3537-aec2-afe4ceb1a4ca | -7.575 | -44.8932 | 2025-08-05 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 812ae05c-7270-3122-b0f2-bc0ece7c6c87 | -8.9683 | -46.739899 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b42746f-9eac-33ea-88ef-d541b7fd65cb | -8.0796 | -42.9603 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c26f5b31-5c81-3d34-a41e-ed9f5f0b69e5 | -11.0729 | -48.354401 | 2025-08-05 00:28:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61a85639-aaf8-3630-972c-a81517008fa9 | -10.4566 | -44.371601 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4171f0e-dbde-36f4-b924-fa2d10cab17e | -6.6899 | -49.7752 | 2025-08-05 00:28:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c00b998-ced1-342b-8abc-4b0c8d2cc34f | -10.5442 | -42.5471 | 2025-08-05 00:28:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6461e36e-1bd5-303c-b36b-4fdc822c32c7 | -10.5327 | -42.542198 | 2025-08-05 00:28:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a7847a82-ee8d-359e-87e0-1e3119d787bf | -8.2307 | -45.056702 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b96d57a9-ab32-3ec0-8994-349ab6b7d9e1 | -9.4036 | -45.506802 | 2025-08-05 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82ba277b-dee1-31d7-8a74-d3827673273a | -5.7298 | -49.096901 | 2025-08-05 00:28:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6f61cdc-a7e5-3261-80f7-baa249b3df13 | -3.788 | -41.689499 | 2025-08-05 00:28:00 | METOP-C | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5080069-3535-394a-8fcf-19564df02a5e | -11.281 | -44.646702 | 2025-08-05 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00b43ee2-d359-3d2d-b2b8-c725605a94fd | -6.4704 | -44.573299 | 2025-08-05 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7168b661-6d2c-3a54-b2e8-1d0e40df59e7 | -12.6912 | -48.124699 | 2025-08-05 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 969b707e-17d5-371c-89df-76474b1ecb04 | -3.1873 | -49.444302 | 2025-08-05 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43221b07-2815-344a-b308-a237818c7431 | -6.3866 | -43.716702 | 2025-08-05 00:28:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27e4547b-d8e6-3ee6-a83b-ed654b4fddf0 | -6.6921 | -49.785599 | 2025-08-05 00:28:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb383599-c277-3587-a122-517eaf4e282a | -8.0153 | -43.2169 | 2025-08-05 00:28:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 436b4691-35dc-329d-abe8-3ab077008937 | -3.0284 | -49.423599 | 2025-08-05 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4070694e-f077-3c0a-981d-800fbb715585 | -8.0071 | -43.226299 | 2025-08-05 00:28:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b09f06a1-c78d-3fd5-88b8-f425e8faf278 | -5.4884 | -42.1651 | 2025-08-05 00:28:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6252fc4e-d0bd-3410-a6e6-6e1e0a234b25 | -14.3577 | -47.0951 | 2025-08-05 00:28:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 759d8a50-fa5e-3a13-80e9-ae9efa22e099 | -6.9842 | -42.867001 | 2025-08-05 00:28:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2ea7f9e-ffb5-30ba-9b9e-03719dd721fd | -6.9727 | -42.8619 | 2025-08-05 00:28:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51cc7ed0-6e54-36c8-8021-d9c1ea37399c | -8.9469 | -46.7365 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39805d99-c1d7-3f40-8e68-fd61de68e929 | -7.4029 | -44.636398 | 2025-08-05 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f388f8d-e222-3c06-8e17-0336524d14f2 | -12.7165 | -48.0984 | 2025-08-05 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18587464-bb52-3901-b4d2-197309cc61f1 | -12.7263 | -48.096298 | 2025-08-05 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ee046e7-8c51-394a-b225-77a17a288174 | -8.0136 | -43.209702 | 2025-08-05 00:28:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6daa283a-adbf-36d2-9e6f-3577a3149fc2 | -10.9197 | -48.3564 | 2025-08-05 00:28:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ccb0fe4-6a2e-31c8-805f-6a67ef52c582 | -10.5683 | -50.4753 | 2025-08-05 00:28:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcf58301-6817-3c86-9712-a549934007a7 | -5.6587 | -42.584 | 2025-08-05 00:28:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a348640a-7bef-3190-a789-4cee1621344a | -15.7078 | -48.98 | 2025-08-05 00:28:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83957b00-2d17-3013-9c69-ec64278eafec | -9.4134 | -45.504601 | 2025-08-05 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 800fb7dc-13b5-3789-a905-bfab742ce749 | -10.4597 | -44.385502 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e7b46be-d4b8-32ab-b08b-6cebc23d985f | -7.1239 | -47.833599 | 2025-08-05 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c76d916d-ddfb-361c-9a8d-cae7e2090483 | -8.9487 | -46.744202 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6007e40e-f5ec-337e-a45c-e7fb4455c8be | -8.2829 | -45.059502 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dee61efb-ca49-3b89-8799-b37fdbea0d25 | -9.5611 | -40.3512 | 2025-08-05 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| acc134ef-86f6-370d-ad6f-5829ed127668 | -8.273 | -45.061699 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2be4a0f-1a40-3c44-8b45-f82a33ba0661 | -8.0052 | -43.129002 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 07b7c77d-81eb-37a5-81e3-ca8fa5536d45 | -11.7909 | -44.994099 | 2025-08-05 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6fd88778-3424-329d-9177-32ad04f6f279 | -7.7658 | -45.233799 | 2025-08-05 00:28:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce3b809-ed62-3e39-82b9-ef491e6014b4 | -8.8622 | -47.610901 | 2025-08-05 00:28:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1981a370-8f92-3c94-8313-fede9db5a38f | -7.3775 | -44.165199 | 2025-08-05 00:28:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2489ff1-5ee4-3f72-8b38-aa7dff71b2a7 | -6.4339 | -44.819099 | 2025-08-05 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 543797bf-3401-36e4-bb4f-4ace839c099d | -11.0485 | -47.6166 | 2025-08-05 00:28:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7eaf224-e746-351c-940b-d9fc3258df67 | -12.7025 | -48.080399 | 2025-08-05 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 413bd16e-8eb0-309a-9ede-b567f345ac79 | -9.0643 | -45.051399 | 2025-08-05 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5844b038-a839-3c9a-a95b-4dcd362033aa | -7.994 | -43.1534 | 2025-08-05 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 7cfd0b8f-fd09-3abe-93ce-5b7f32921b76 | -8.9478 | -46.7354 | 2025-08-05 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ec9d3b84-cf32-3df3-b49a-a58d8e906efe | -7.9943 | -43.1298 | 2025-08-05 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| a05b3bba-9fbb-30fd-a48a-d24830efbc5e | -3.1649 | -49.4435 | 2025-08-05 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| f5c10375-1726-3ecb-aa6a-d3051161da50 | -3.1832 | -49.4642 | 2025-08-05 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| bf9de4b6-cdfd-3562-b40c-3768b1cc353a | -6.686 | -49.777 | 2025-08-05 00:30:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| ab908c59-72c0-3051-a994-d6d78e89d75b | -9.3989 | -45.4928 | 2025-08-05 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 1c1d102b-cdfb-3c31-8737-d9fdcde60279 | -8.0129 | -43.1513 | 2025-08-05 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| acac549f-a1a4-3a54-bb72-d2044e052547 | -6.6672 | -49.7995 | 2025-08-05 00:30:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1fa31a4f-2a23-399d-97f4-6c5e8133ef43 | -3.1833 | -49.4429 | 2025-08-05 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 7be15878-3d4a-3e01-8bc3-0c1969d6a868 | -6.6858 | -49.7983 | 2025-08-05 00:30:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a10d08a5-a5a9-3984-9377-bab2f53616c5 | -9.553 | -40.3503 | 2025-08-05 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 40.8 |
| 9daa1fdc-0bf7-3697-80e3-677faa3018b0 | -8.0132 | -43.1278 | 2025-08-05 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.3 |
| b1f716b0-4969-3988-8a93-8e9f1818680d | -3.1832 | -49.4642 | 2025-08-05 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 5a9ba10b-b6a3-3e73-b5d9-684eeb9985c1 | -6.9607 | -42.858 | 2025-08-05 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| d1f04b10-9c3a-3903-9082-5ae1edfdbd38 | -13.0723 | -56.9131 | 2025-08-05 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| cf1b354a-fbe0-3b00-8199-d847de2c95aa | -6.6672 | -49.7995 | 2025-08-05 00:40:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d55b1f8f-0736-383a-a0a9-6e2b8425c51c | -9.3989 | -45.4928 | 2025-08-05 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 3ab13397-3d8c-3ff2-a758-cc7b9b0eb73f | -3.1833 | -49.4429 | 2025-08-05 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 305320d2-d58c-3f35-a8ec-c631faa7e872 | -9.3985 | -45.5156 | 2025-08-05 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 1ee4fe9d-fc15-3d32-a526-04a609ff8d35 | -13.0535 | -56.8947 | 2025-08-05 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| bf0b054d-5a1a-34fa-b49a-25b3f60747d4 | -6.6858 | -49.7983 | 2025-08-05 00:40:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 7a4e4ad5-d8f5-3b33-a04e-af4da548f9b6 | -13.0726 | -56.893 | 2025-08-05 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| adeca4b3-f659-3011-97cc-697c051a02c1 | -13.0538 | -56.8746 | 2025-08-05 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 5a74f406-ebf8-3e47-aa72-5bd9aae84f34 | -8.9478 | -46.7354 | 2025-08-05 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f1a97392-9854-32ae-8b38-19a29cc2a2fe | -14.3083 | -54.6871 | 2025-08-05 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| cc82aa1c-296c-3e6b-b9f4-fcbe6a3e979c | -9.3989 | -45.4928 | 2025-08-05 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c0c21c43-4076-329c-8bdc-f4dbf7d80b94 | -13.0914 | -56.9114 | 2025-08-05 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b1222aa7-6187-310a-8369-cea9df0c10d1 | -6.6858 | -49.7983 | 2025-08-05 00:50:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 134a2848-bac3-36c2-8612-beaeb2e06db0 | -7.994 | -43.1534 | 2025-08-05 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 820a4fb1-55ea-3afc-8ac0-b748c6f0f21c | -13.0533 | -56.9149 | 2025-08-05 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| eded491f-8978-38fe-9573-c477f6f9c5f0 | -10.3311 | -47.8256 | 2025-08-05 00:50:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a5b92130-24ca-3b85-ab7d-a7d11b73f993 | -9.3985 | -45.5156 | 2025-08-05 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| fafc14bd-b7e5-3b25-b87a-423189f75bba | -8.0132 | -43.1278 | 2025-08-05 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| da2f18cb-7a43-30f6-be09-6235d6419eae | -10.7853 | -46.6361 | 2025-08-05 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| dbe865a3-3fec-3f8f-8f3e-eff34e15dcdd | -10.7849 | -46.6586 | 2025-08-05 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 808123bb-04ec-3ad8-a8c6-032444d2b0ae | -13.0726 | -56.893 | 2025-08-05 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 75c7f72b-9807-3d4f-baeb-5adcf47fdfa8 | -3.1832 | -49.4642 | 2025-08-05 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 635cd5f5-2156-3e6e-ba32-c685d149a282 | -3.1833 | -49.4429 | 2025-08-05 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| f679576a-260c-3d03-9cc0-050f8a29ba37 | -6.9607 | -42.858 | 2025-08-05 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 4ac30b13-37fa-3389-ab3a-e57a7892452f | -8.9227 | -60.5568 | 2025-08-05 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 4691b6d0-35a6-39e3-83a9-0d5469f38f92 | -13.0535 | -56.8947 | 2025-08-05 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b3184a28-8c18-3304-9470-7fc32c3f5202 | -7.9943 | -43.1298 | 2025-08-05 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 22754a7f-f051-32bb-b90f-cd1aa96b0d0e | -13.0916 | -56.8913 | 2025-08-05 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 10083a8f-5f1c-3f20-973a-8fdaaf1e0137 | -8.9478 | -46.7354 | 2025-08-05 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| be2ec0b4-065d-388f-960a-219e997e0cc7 | -13.0723 | -56.9131 | 2025-08-05 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 738da396-935d-3247-81de-d0956dfd9166 | -3.1832 | -49.4642 | 2025-08-05 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ce540fee-8344-3eba-99c7-42f9d522285e | -9.3985 | -45.5156 | 2025-08-05 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7da35d19-6bdd-3588-bae0-b07dfbd69c24 | -11.9403 | -44.9264 | 2025-08-05 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| c0f24226-a71a-338a-a108-354f2d275fa0 | -11.9207 | -44.9525 | 2025-08-05 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |


[Clique aqui para ver as próximas entradas](README4.md)
