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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2732d473-40dc-3b30-af47-a6c0b1508489 | -10.3894 | -61.2502 | 2026-09-29 10:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 171.4 |
| ca3a176c-847d-361a-93bc-0ffe0d875c5f | -12.7421 | -47.2684 | 2026-09-29 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 5de5d285-13a9-3944-9edf-6b7a793edbe9 | -12.7417 | -47.2909 | 2026-09-29 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 905f91da-ad9c-303c-a183-d3ebdee9112f | -10.3894 | -61.2502 | 2026-09-29 11:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 279.4 |
| f2c53c20-4ebd-3af8-a2c1-f443b6a1b360 | -10.3895 | -61.231 | 2026-09-29 11:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 132.8 |
| b5139ccf-b1b2-3ebf-b436-b4bab22f9709 | -12.761 | -47.2881 | 2026-09-29 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| a3dfb514-27ec-3fab-91c0-ad32ffbaa6b0 | -11.1775 | -44.7832 | 2026-09-29 11:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| fd5df6cf-065c-3e54-91bc-371c9f19fe56 | -10.3895 | -61.231 | 2026-09-29 11:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| cbf77a44-5c40-3376-bbca-58d487ba630c | -12.7614 | -47.2656 | 2026-09-29 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| be3b3b00-2bd4-3786-a691-00ba9f2d0d40 | -11.4302 | -43.4596 | 2026-09-29 11:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| afb63cee-36e1-34ed-bb56-b91ba55a5061 | -12.761 | -47.2881 | 2026-09-29 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 7052b6dd-3930-3bb3-953b-2afac633365f | -11.1775 | -44.7832 | 2026-09-29 11:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c1e95741-1119-3395-bf44-0f392ea17289 | -10.3894 | -61.2502 | 2026-09-29 11:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 333.9 |
| 6397c8db-700f-35f5-82ab-e18d0d0429ac | -12.7421 | -47.2684 | 2026-09-29 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| f879726e-0679-3dcd-9da4-de45417b2b26 | -12.7417 | -47.2909 | 2026-09-29 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2ad29c06-1a6c-30c5-9c65-dee15819c1a5 | -12.761 | -47.2881 | 2026-09-29 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 521043a1-fd5d-3b2b-8e3b-6b240ac62a5a | -11.1771 | -44.8064 | 2026-09-29 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 80c8448a-79be-382e-8b48-ce195311287a | -11.1775 | -44.7832 | 2026-09-29 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 30690c86-3bb8-3ba6-b84e-4ec4f5fa2865 | -11.4302 | -43.4596 | 2026-09-29 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| a02c9412-e57a-3ce0-87c4-7b5f146c3afd | -12.7036 | -47.274 | 2026-09-29 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 465aeaee-6fbc-318b-95ed-dbbae91c1493 | -11.4307 | -43.4358 | 2026-09-29 11:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| f0f2471e-193a-36a4-a992-0b61cad25c36 | -12.7421 | -47.2684 | 2026-09-29 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| e0992644-fbd1-3f12-b1a3-8d43c8344d58 | -10.3707 | -61.2513 | 2026-09-29 11:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 10a4ba18-0216-3a10-a0b7-b7a61e7d71fe | -10.3894 | -61.2502 | 2026-09-29 11:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 405.2 |
| 2ed79b7e-7d5e-3a68-947b-dcd10f218c97 | -3.97399 | -41.52359 | 2026-09-29 11:21:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 028e9ddd-d671-31d7-a708-3330fd9e105e | -4.48167 | -42.15908 | 2026-09-29 11:21:00 | TERRA_M-M | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 64519409-1468-3f7e-bbb7-b67a8f4a379f | -5.43221 | -43.44242 | 2026-09-29 11:21:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 81ec4fe9-a3e4-3da4-88b4-5751185bc748 | -5.02731 | -43.56573 | 2026-09-29 11:21:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4a0e0ccc-3a89-3015-b3f0-be50095bee2b | -5.02593 | -43.57531 | 2026-09-29 11:21:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 245e2b53-6099-38d8-ba51-1dbc94f55a64 | -5.03437 | -43.57318 | 2026-09-29 11:21:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 766237e0-b9ab-329d-a329-fc54b28aa94a | -3.31124 | -42.34631 | 2026-09-29 11:21:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 68f53dcd-4a41-3f83-999c-9055020bfdf3 | -3.19382 | -43.86191 | 2026-09-29 11:21:00 | TERRA_M-M | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 09e51733-c3a5-38fd-bb71-763fe3b408c9 | -5.03579 | -43.56359 | 2026-09-29 11:21:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 79b57e72-eec6-3d37-abbc-528fad1014af | -3.97274 | -41.53234 | 2026-09-29 11:21:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9a93adf8-7ead-3bac-99ef-4567d5baf7ff | -3.25337 | -42.55827 | 2026-09-29 11:21:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8ef39075-9a31-3af8-9272-a4bef590fb10 | -5.74668 | -43.43889 | 2026-09-29 11:21:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 77ed7913-9b79-3aeb-af7e-444cab2e9df8 | -5.75071 | -45.16122 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5475bdb1-46c2-3249-8568-0db17aede491 | -10.28018 | -44.62571 | 2026-09-29 11:23:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 08d9d8ca-6666-3ddc-91d8-2f6210b6c4d3 | -7.50293 | -44.55087 | 2026-09-29 11:23:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1d7f2ed9-76e1-3fda-a1af-0fe3706d6e20 | -8.97408 | -44.15572 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b8e3e39e-baff-3e7a-a710-91d4fc216fb5 | -11.42384 | -43.4376 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| f6c4bd6d-33ac-35fe-8532-5c95dc4e66a1 | -7.46911 | -45.80508 | 2026-09-29 11:23:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 260c3240-998f-38d8-98d5-0a6284652a02 | -7.6698 | -44.23863 | 2026-09-29 11:23:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 983f1848-f71b-333d-9a60-b2904f36255a | -8.64255 | -45.35109 | 2026-09-29 11:23:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dbc3c31c-0bd5-3b5d-ad64-c152cdb8d5cd | -6.31208 | -43.61337 | 2026-09-29 11:23:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 85dd8632-ae0a-3371-a7ac-94af01261202 | -7.66838 | -44.24832 | 2026-09-29 11:23:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c7a5d4b9-2c0d-3b20-870f-54c33e391b0c | -7.99402 | -44.16335 | 2026-09-29 11:23:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d80157a2-4067-3bb8-b212-7dfa99df6f1a | -10.63995 | -44.75301 | 2026-09-29 11:23:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0eed7ff5-610e-3367-b58a-608ac4025704 | -11.43393 | -43.42994 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0d87dac8-8cef-3c78-84f5-24c43eb9039f | -11.18013 | -44.7824 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0d817a20-9aa0-38b8-ab54-a8d43d483201 | -6.33288 | -43.91367 | 2026-09-29 11:23:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5694a067-62b1-32e5-8cd9-b93b68490a95 | -9.05228 | -45.00817 | 2026-09-29 11:23:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7eee8938-6124-34be-bbd5-a974daa1b48d | -7.72371 | -44.56444 | 2026-09-29 11:23:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8cd801d6-77c7-3e2d-a71c-6edc1cc4cd97 | -6.90915 | -43.69543 | 2026-09-29 11:23:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 9d0346c7-d765-3312-87c3-751d892c3ffa | -11.43265 | -43.43887 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 138b8c65-6599-3665-83fb-c35090e306e3 | -9.2533 | -45.32278 | 2026-09-29 11:23:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| df0521f2-00b2-3d13-8a25-47c55e907713 | -6.45694 | -43.8885 | 2026-09-29 11:23:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 29db8831-4f80-3fad-8d6a-92331b8875a0 | -12.29832 | -42.26416 | 2026-09-29 11:23:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7934ab65-462e-3aea-bd9e-3fd8ae771d02 | -8.21886 | -45.45168 | 2026-09-29 11:23:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 91cedf35-75a2-33e8-847c-739e7fa41ab4 | -9.4692 | -45.79569 | 2026-09-29 11:23:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 674fa277-c418-3681-aeb4-437760bc5b57 | -8.36515 | -45.44133 | 2026-09-29 11:23:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 277765fe-57f4-3fe0-af8a-ed35478e197e | -8.3255 | -44.17214 | 2026-09-29 11:23:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 7af1fc59-83c3-301b-92f4-6a06ced6b8d3 | -9.78732 | -48.21603 | 2026-09-29 11:23:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 126ab3bb-e37d-3997-81cb-8f63f7236bcf | -7.8456 | -45.81966 | 2026-09-29 11:23:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 47431d99-a041-331a-a7ca-c0eceac4aeb8 | -10.25572 | -44.60216 | 2026-09-29 11:23:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 886aad85-4d49-3603-9bd3-c5bcb6958376 | -7.83686 | -45.81187 | 2026-09-29 11:23:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| a8120ab5-5d16-3eaa-bc7e-94efed55dd0a | -6.32877 | -43.37021 | 2026-09-29 11:23:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| d9cf5a26-2ab4-310b-ae59-3aa3c59da856 | -6.14344 | -44.14228 | 2026-09-29 11:23:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5b3c6f70-e104-308f-8d77-fbab25bb757b | -7.98523 | -44.16579 | 2026-09-29 11:23:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 51e485b5-f186-3e0a-862f-71411af4fc00 | -11.18199 | -45.13693 | 2026-09-29 11:23:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4c480e40-2816-37c0-a534-24c45322dd09 | -11.42512 | -43.42867 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| ad684570-a1c6-36e5-b36a-92a5e2b508c3 | -12.1454 | -44.99609 | 2026-09-29 11:23:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3e2e1e49-7502-38c4-8ce4-e31d361556da | -12.24946 | -44.60466 | 2026-09-29 11:23:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 523fdd7b-935c-3397-b327-9c3a17b3c58d | -7.68651 | -43.99735 | 2026-09-29 11:23:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c5abf7a0-1abd-31de-9dd1-1d4b9252d948 | -9.77 | -44.82661 | 2026-09-29 11:23:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 87e2001e-2794-32f2-94cf-7a9454228636 | -12.74255 | -42.71849 | 2026-09-29 11:23:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ad0e5d37-3e60-3a9a-a319-2800b0089086 | -6.44994 | -41.88306 | 2026-09-29 11:23:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 3fef104f-ba16-39a3-b95b-6a9b5ed7e66f | -12.88788 | -41.72667 | 2026-09-29 11:23:00 | TERRA_M-M | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 3e692e9d-4119-30c4-aafc-d9b180e2d2ea | -5.74899 | -45.17268 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 410.1 |
| 714102b9-5265-3a87-8e66-2364c7df202a | -12.14396 | -45.00573 | 2026-09-29 11:23:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4991c899-4859-357e-8aa0-a84b8e02a00c | -6.31979 | -43.36897 | 2026-09-29 11:23:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6827a881-7217-314e-876a-c6df73534bd8 | -9.31676 | -42.4197 | 2026-09-29 11:23:00 | TERRA_M-M | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| dcfd543b-9724-3e70-8bfb-c38b54820906 | -7.46905 | -45.79959 | 2026-09-29 11:23:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| fdd64ee2-0050-3dee-a515-fd932422c22c | -6.59575 | -43.88202 | 2026-09-29 11:23:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f92c3e51-fc3c-33d5-baca-0949f50c5027 | -11.06253 | -47.67577 | 2026-09-29 11:23:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f3fac38f-6bfa-3f3e-948a-82a186313739 | -9.77335 | -44.86758 | 2026-09-29 11:23:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3360db01-1cbe-3cad-b9d5-ddc489f4172a | -6.29761 | -43.64954 | 2026-09-29 11:23:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 31809d43-233c-3669-aad1-bbc795918bc7 | -8.9727 | -44.16519 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a10ac982-6dfe-3f00-98c2-4f21b629bd4a | -12.00877 | -44.92375 | 2026-09-29 11:23:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e6e11fc2-c850-348f-b9ee-6d9bea63bab5 | -11.42879 | -43.46568 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 878be8e7-b9dc-3e4b-8b2e-09abf663f654 | -7.0037 | -43.74364 | 2026-09-29 11:23:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dc75a6a6-e398-39f4-b871-d8884893311a | -9.40269 | -46.84211 | 2026-09-29 11:23:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bf9a3008-6ccb-32c0-b066-4c900a4b72f0 | -7.38659 | -42.63655 | 2026-09-29 11:23:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 0d26ace5-839f-33e8-b39d-53ba150a6b59 | -11.83333 | -46.8981 | 2026-09-29 11:23:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0df9e765-e421-3e8c-881f-a9840c912074 | -11.77035 | -42.6141 | 2026-09-29 11:23:00 | TERRA_M-M | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 33c3c519-a54f-31bc-9aa5-3888dcff4b30 | -12.01023 | -47.8041 | 2026-09-29 11:23:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d0dc2e63-694e-3795-be29-69da963dbc94 | -11.18348 | -45.12706 | 2026-09-29 11:23:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e2b9c710-518c-3cf7-a8e1-3bdb4673661f | -11.17102 | -44.78107 | 2026-09-29 11:23:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 47a69c26-2ae1-38a8-9d33-f425382b16e5 | -11.4275 | -43.47461 | 2026-09-29 11:23:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 3d80a945-838d-3df9-8c91-7ce0b7f09a1d | -11.86769 | -47.08188 | 2026-09-29 11:23:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README72.md)
