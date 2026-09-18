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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 634c1b31-621c-314a-b9a7-f525ff23d97b | -11.52001 | -46.87867 | 2026-09-18 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f34fb585-e12b-384c-85ab-965bed95143c | -10.52055 | -46.73381 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3bf3def-7c54-3490-9b3f-8ef2cb639145 | -9.59128 | -45.85867 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f24f42c-b762-3146-b1ee-62c0b8f150d8 | -12.67535 | -43.91624 | 2026-09-18 03:38:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 178524d6-84ab-3d8f-93bc-1a63d7700bae | -16.55746 | -43.99617 | 2026-09-18 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b69f400-01e3-3727-9562-dede751928d2 | -11.88793 | -47.58007 | 2026-09-18 03:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbe0c6dd-bed2-3f73-9e33-35ba0d783cfb | -11.32184 | -43.35219 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fca8001-0776-37c5-847c-40fea0e9c40b | -12.16853 | -46.99407 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 47944032-532b-3023-abb1-3c057550e0f7 | -11.27943 | -43.36248 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 797d7750-3b27-3f1d-a6ad-8e6574aef0c9 | -9.2426 | -45.91131 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9b8aa72c-8b95-34b0-af36-c197303c8226 | -11.30595 | -46.77435 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 627b5fe0-34a1-3e7b-b8db-cffbf8323303 | -9.76865 | -46.60406 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 95213536-bc61-3024-aef2-45f3636cabb8 | -10.48248 | -46.31781 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 042ab141-608d-3d04-8a68-6b1b502bff53 | -9.94066 | -45.32202 | 2026-09-18 03:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1616bbe7-9e77-3f36-8592-efd8387b8674 | -11.27866 | -43.36639 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76bc26d7-e323-31b0-940b-5eb91468bdfa | -12.53296 | -47.09769 | 2026-09-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d10a9932-7e39-3890-be73-6305fd129470 | -11.29271 | -43.35362 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f9ccb28-549b-3c8c-adbb-00f8cd01903d | -11.31041 | -46.78505 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a825f87c-f610-3061-b5d8-5e7aec7a2ded | -9.9478 | -45.45511 | 2026-09-18 03:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0bc845b-fe17-36ce-a73a-5d20e82b43c0 | -8.77542 | -46.90147 | 2026-09-18 03:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2dffcb9e-ed80-3ab2-bcb6-45d6a73868ed | -13.69508 | -43.61971 | 2026-09-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b749b648-07a1-37ed-8c18-48277e6fe3bd | -11.16006 | -42.79481 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2fdcc705-218b-3d85-bb06-6afc1a5f74c9 | -9.92662 | -46.52998 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3892740-b827-3458-9ac1-8283f181f40c | -9.75991 | -46.08551 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9ef7f4d-0280-3095-9ffd-94a95df6dc06 | -10.48374 | -46.31144 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b8837a2-3a8b-362d-8915-6f7e55e8ae64 | -11.33659 | -44.01732 | 2026-09-18 03:38:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0712cbb0-04d3-3e9b-9737-f1b285a1f1c8 | -14.79724 | -48.56033 | 2026-09-18 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03e342e0-6de6-3a51-91a2-97a5d3c5a730 | -11.27789 | -43.37034 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5be94f83-8897-3f4a-a321-d1ce24b550bd | -9.90891 | -46.5466 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36f5fde7-1b23-3b12-9b5b-907a794723d2 | -13.64342 | -46.93004 | 2026-09-18 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d16189ed-ca29-37a6-ae9d-d6fe8df501f4 | -13.64889 | -46.93689 | 2026-09-18 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aa11721-437a-3882-92aa-5f88e9b6aa74 | -9.23781 | -45.91283 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 575364b7-8c22-34ef-ac50-fdb3ccb98454 | -11.32495 | -43.39599 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5da4ee39-cf92-3b8d-9b5b-e360d88afe96 | -11.16182 | -42.79768 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1eb65108-337a-37f7-9a37-7fcaba6797d8 | -10.54131 | -44.85236 | 2026-09-18 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88a9ea19-dda7-3397-8884-4a11e3e1a142 | -16.01321 | -43.60316 | 2026-09-18 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fa82417-0e65-38ce-a209-ee47efb2d45b | -9.75861 | -46.09193 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c0874bf-5f19-3cd6-9c23-023d471e6872 | -9.59496 | -45.85893 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8a6db922-0d02-35c4-97f8-2545ce9d6430 | -9.75676 | -46.09122 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4704d716-9e19-3696-8368-ef93c5724a7f | -11.28345 | -43.37143 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c878f77-4bf4-3ea9-afeb-41509ae02815 | -15.86375 | -38.93861 | 2026-09-18 03:38:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 22755625-fa38-3a97-8b85-27722b010008 | -11.52237 | -46.86636 | 2026-09-18 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82fa5fef-00be-34c8-b023-24b50807386a | -11.31457 | -46.76723 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2f802fcc-96c8-35e4-8370-10c81d9bedef | -8.77376 | -46.90975 | 2026-09-18 03:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a6fedae3-d4f7-3dc2-a173-a916a9bfe9de | -11.30472 | -46.7781 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8ce4bbb-1404-3fd2-9d64-6e61731f8e2f | -16.55788 | -43.99889 | 2026-09-18 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8a036c9-d7a4-35f2-b30c-3b088f7fad07 | -12.31273 | -47.96123 | 2026-09-18 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b45aa9b3-c302-358a-aa36-977fbae804ee | -15.56697 | -46.44808 | 2026-09-18 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d7c2004-333f-3fad-940b-c924c9e1baed | -11.29637 | -43.39417 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b174546-ebf7-3150-8c92-70bc3bb6a1d2 | -13.64218 | -46.93592 | 2026-09-18 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efe3a656-3e3c-3e83-b2af-f7ac253df13f | -11.3119 | -46.77774 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45d5c045-a8a0-32ca-a918-373d37bd7686 | -13.34314 | -43.7854 | 2026-09-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a2d1be5-5fa5-3d40-89fd-76c30df3a9d0 | -12.16971 | -46.98854 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e1f03303-5c06-3bc7-8d63-d163c3c7295c | -13.34389 | -43.7817 | 2026-09-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c3a42ae-8134-3d1b-aaee-9ea9f38c8645 | -9.94268 | -45.34546 | 2026-09-18 03:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 523511fa-190e-31e4-b690-c3706153ea2c | -9.73882 | -46.12025 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3ef16189-706a-341d-bca2-b1392f089c71 | -11.2913 | -43.36084 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd20f45f-30bf-38c7-9d89-94705f446da2 | -9.59912 | -45.85412 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 76b1719e-7ba1-3f1a-a44e-90fefa3c356f | -9.91124 | -46.57048 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d85f65b2-f1d1-3fe9-85fe-7c4e3c59c0ba | -9.93958 | -45.32743 | 2026-09-18 03:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2b5e901-11dd-3830-9eb8-c88ca34c1be8 | -12.67612 | -43.91228 | 2026-09-18 03:38:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd86b859-7fcf-30d7-a358-6b25104a0b82 | -11.15876 | -42.80178 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3f3b2e3-04a8-37eb-adf6-c902bcd14024 | -9.76986 | -46.59816 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95834ac9-0e10-38a4-b5b6-adf262a622d5 | -9.18826 | -46.77079 | 2026-09-18 03:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d98bac6-5db7-3572-baf0-e441344fa5ed | -11.51856 | -46.88492 | 2026-09-18 03:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9b08d4f0-4bdb-3285-bc9b-aff5ddbb1731 | -9.39731 | -46.86779 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| beb7cd08-fc82-3df1-9fea-aa612f787560 | -9.09242 | -45.72477 | 2026-09-18 03:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 110c5b85-bd18-396f-b80e-d7e1e3f3ef2f | -11.27332 | -43.51265 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dcc1e6d-9a83-30d2-b33d-398f38281061 | -11.27257 | -43.51648 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3c10cd3-5005-3b10-b7db-d31dccd3ae0e | -9.93779 | -46.54562 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75a852b0-5019-307b-b2f0-6b7d1dd43192 | -11.29786 | -43.38649 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a37a8f62-c077-332f-977c-da9364491dae | -11.15781 | -42.78966 | 2026-09-18 03:38:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1be59576-bdba-383b-abe9-2dbb6e35411e | -9.91147 | -46.53402 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c29e7e07-3a06-3482-8f37-0d1aca782824 | -11.28043 | -43.50605 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba755c98-11e7-325d-a3ea-6a72a9c92983 | -13.69437 | -43.62329 | 2026-09-18 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a392fb28-4db0-3e54-b190-21b44e733cd6 | -13.61961 | -46.94438 | 2026-09-18 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46d4b632-12f3-3751-9b77-d67142b9c286 | -11.89064 | -43.82175 | 2026-09-18 03:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b4028e3-df08-383a-915d-afbf4f33a1e0 | -11.3283 | -46.76706 | 2026-09-18 03:38:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ebfdc3e-968b-394f-99dc-adc449c0f415 | -10.48602 | -46.31082 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da43b726-dcd3-3450-9856-33d5ce60d027 | -14.95484 | -47.53581 | 2026-09-18 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b01423e-9133-3e7c-9b9e-632187f71988 | -13.74096 | -42.60334 | 2026-09-18 03:38:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c4dbdec-78eb-3dbc-8d6b-62bfd155a291 | -14.22 | -48.52378 | 2026-09-18 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 349d4a83-928a-3340-ad26-dab8cee8c0a8 | -8.77691 | -46.89405 | 2026-09-18 03:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43e1378d-7ce7-3e08-aada-5a63e4a04cc0 | -9.93627 | -45.34409 | 2026-09-18 03:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bf84df1-3e2c-3ac7-8f8c-71db1a31f850 | -14.10477 | -46.9475 | 2026-09-18 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39026246-5687-3222-b359-bb8bae890875 | -12.16333 | -46.98184 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ca5f31f3-a5b1-35b5-bff5-2576c5c5317a | -9.75735 | -46.09815 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f20cf744-0b35-3ddc-bfad-f0422b6149a6 | -9.93226 | -46.53753 | 2026-09-18 03:38:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aabe847b-4b81-328a-8be5-5e6997ebbcd8 | -9.18966 | -46.76367 | 2026-09-18 03:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e2f66dd-4aae-3cdd-bdd2-9563d1c52940 | -9.59679 | -45.8657 | 2026-09-18 03:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e3e03654-84b9-3828-b62c-af9efdd4983b | -13.22985 | -42.33376 | 2026-09-18 03:38:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 26.3 |
| ea698c85-8311-3cff-8129-9244144facf6 | -10.61225 | -46.56401 | 2026-09-18 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea252773-8d08-3592-afb8-519f56de9d57 | -9.39538 | -46.85919 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5be9612a-41b9-3264-a7bb-04eff183a8f0 | -12.16795 | -46.99384 | 2026-09-18 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b195ba98-1f8b-3ecc-b699-b72be2bd7d98 | -13.23043 | -42.33077 | 2026-09-18 03:38:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 617ad92b-b171-337f-a45d-f45b397d27e5 | -11.27637 | -43.37806 | 2026-09-18 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d961bd5-2a0a-3735-9f5a-c5c5846209ca | -13.24745 | -46.91385 | 2026-09-18 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2f15c0da-bd14-3ddf-ac4f-470c199225e3 | -13.74036 | -42.6064 | 2026-09-18 03:38:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f3bacf74-b13c-3792-9217-4f9785a2e049 | -12.78423 | -47.56175 | 2026-09-18 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4a3979d-cacf-3362-b5ee-be8404642668 | -9.38605 | -46.85033 | 2026-09-18 03:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README28.md)
