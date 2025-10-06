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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f28287d-a61f-3809-a258-8ea09bd947a4 | -15.60686 | -52.54744 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| dbf30745-80a9-374b-902f-f7100950b230 | -14.68332 | -48.40612 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f5a314fd-ed0f-3005-8aa3-7bb989d9328f | -18.177 | -53.3792 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4fa5ccb2-142a-357f-bb9c-73a1eef30332 | -12.37878 | -63.72193 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47ee4095-9c29-33ff-8f85-71801ad8e6bf | -13.0875 | -47.83514 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 417a5964-e017-3908-8b16-711e181c0414 | -15.98996 | -50.93028 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a526fa83-ab6b-3149-9520-6373dfc375ab | -13.25384 | -48.46723 | 2025-10-06 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43cd3c24-ebe6-38d6-895d-81d1f683a6af | -18.14605 | -53.38873 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 631898d2-f154-3fd7-92e1-6cbcfa5cbaaa | -12.3068 | -55.11787 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3763a028-90cb-3d0d-b1d5-55cf1b6c19cd | -11.86911 | -56.8859 | 2025-10-06 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af110133-9fb0-3796-afc4-9ef78628d5d1 | -17.68035 | -52.24305 | 2025-10-06 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72b7abd4-ac9f-32f0-aec3-377ad037d947 | -12.38028 | -63.71317 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2cf17d6-9111-303b-936c-63d295a570fc | -18.19021 | -53.36954 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f53a3d13-383b-3740-a703-3d30ede367aa | -13.0798 | -47.83421 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b00f4990-a0a1-34b6-9027-5f2950bc7ccc | -16.00372 | -59.52658 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28bb6801-e32b-372b-a138-1ae718fd4da0 | -13.35907 | -47.5689 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2694eecd-6f73-3b1f-8e63-5eff9f28d870 | -15.62424 | -52.48539 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66467a10-b3b9-333f-93d6-9a2e41b00dc0 | -14.61082 | -52.49566 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2024d949-62f8-37a1-a2dc-8a62c5388f79 | -14.90781 | -46.85482 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4b6a205-58f8-342b-85f4-aad97c121ef3 | -17.83915 | -57.61963 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a014b769-1ff4-3643-b2e3-07ed55ed61c7 | -12.32794 | -55.14275 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fda8e12c-7dd1-34b5-87d8-8526641840b7 | -15.8789 | -59.3808 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 834456e2-29f7-3650-9614-13423eb03de2 | -18.11862 | -53.41133 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c95b8385-9c11-3694-872b-d762ba464f32 | -16.94874 | -52.67632 | 2025-10-06 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7298c689-253e-3396-858b-b7a346e386c2 | -14.74472 | -54.66809 | 2025-10-06 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89b75dcf-1853-3b3d-ab9b-6d2999fbfba8 | -14.48847 | -47.55794 | 2025-10-06 05:18:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 414b573f-e1c9-3dc5-9f51-9040caece59f | -18.24042 | -53.36574 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd9c66b0-3385-3b29-b04d-0adcbe7adab5 | -13.08026 | -47.83001 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 400c41f3-3696-3fe9-8e52-35417403fed0 | -13.23429 | -48.47025 | 2025-10-06 05:18:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00a6240d-07ea-335d-9adf-b6acd4677f5e | -15.99315 | -50.85192 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bec5c02-63b4-3b61-9233-8b42687059f4 | -14.92468 | -46.82909 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7ab8d0f5-6207-3942-8b64-dc7b25bd1594 | -14.3462 | -47.72252 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7dfaeab-849e-3a55-840a-a1a2a848a2c8 | -18.12044 | -53.39554 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d3b0e1c3-35d7-3874-bac0-ce9d0649bc6e | -15.56607 | -52.46199 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd583c1e-2a6e-3986-a94a-f7d97ba7617c | -14.70095 | -48.36736 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e87996dd-348a-38db-b78f-4c73aabcc8dc | -15.60619 | -52.55125 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9ea275a8-d7ed-3c71-9ba9-d292f2e2f074 | -11.88007 | -56.86164 | 2025-10-06 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a43996c8-1b40-399b-822c-1f3e75bfc72f | -14.68972 | -48.28413 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31076bbe-aa1d-3429-9cb8-77284bd1d0ab | -12.90042 | -54.74751 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 595ae62c-da82-31a4-9a4a-289dc7b5cb3b | -14.32266 | -47.6582 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e6aa09e-02ab-322e-a5de-5b410bc602f6 | -14.36282 | -47.72653 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fcb95bfc-8dc3-3b4c-a1e2-4cd372d0e1c3 | -16.00918 | -50.8425 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a164cce-27eb-36a6-830d-f431966a8b74 | -15.56573 | -52.46485 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c67c4d2-d7bf-3ab1-a7c2-6efc28d40590 | -12.9908 | -51.04689 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45274e49-7da0-340f-816a-52e3a80efb63 | -15.6182 | -52.53733 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88a209c1-05f8-3419-aa4b-3dee65996807 | -15.23542 | -56.79151 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8de921f-a071-36a5-9f9c-4ffaed9a35d4 | -14.88373 | -51.47869 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7056099f-cfe0-3348-853d-2f23aba62cca | -14.55016 | -46.95578 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a1473e9e-0bd9-3d46-833f-1f0ca8e93390 | -13.60268 | -48.69306 | 2025-10-06 05:18:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 959106e3-f5c6-3e9a-a666-992fef779c92 | -14.92119 | -46.8642 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 494a3180-e96f-38cc-a55c-6093aa812752 | -16.14639 | -57.56998 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2418ff48-c6a0-30ae-a4f8-39f60166c8b5 | -14.55636 | -46.69019 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae4e4f72-7c9e-3323-99b5-bac84e54b855 | -12.2967 | -64.02016 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15b20ab8-d658-3a2b-87cb-1e3bd3b82b65 | -13.08581 | -47.84012 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df563003-964c-3dbd-8ade-70fdfdc08299 | -15.66315 | -53.83508 | 2025-10-06 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66c3f192-0be5-383d-8a06-f60a74d548b1 | -13.63025 | -48.70857 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e754b133-07ad-3c12-b391-324b9139b572 | -13.10769 | -48.00212 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28330fa3-a4f2-314d-8ab4-a356f0478010 | -13.36058 | -48.0394 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b155be25-3160-3a38-878c-b549a176b42f | -14.88422 | -50.1331 | 2025-10-06 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c58d7e10-bd6f-32be-8259-a500cca4b5ed | -12.90094 | -54.74367 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 224e77cb-c4c6-35c0-b574-a3a598551348 | -14.75644 | -54.6785 | 2025-10-06 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c1b27ab-f6af-3b92-9630-4ac6cc79ccd8 | -15.87551 | -59.38026 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2711a6be-c4c2-3ca1-8a47-3d28cd83c5e0 | -14.69967 | -48.37605 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5058d8cb-d47d-3d45-8876-ed1b4eba8ee5 | -18.13986 | -53.39924 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 77d86429-8c1c-3f5f-89bb-c4624e10603d | -14.84016 | -54.79241 | 2025-10-06 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c59598b-69aa-337c-a40b-e23f7e4f0a2b | -14.68926 | -48.29047 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2245767-df69-3616-b13a-3ce78cbd2d3b | -11.71903 | -59.13408 | 2025-10-06 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77816051-413c-3fa3-9fff-0ae6530a7714 | -14.66624 | -48.3827 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99b3187a-f62a-3843-9d50-a739f56e796c | -12.9202 | -54.72672 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdaf64bb-5446-3e81-ae87-7d069f9451eb | -17.95915 | -48.54946 | 2025-10-06 05:18:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91d915d7-d7ad-3e4b-8d0d-bfefcbf63a42 | -15.61367 | -52.53253 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36d09d46-a904-383d-890f-00508e1c6f3a | -12.9249 | -54.72341 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 047b8098-0a6e-3cb6-bcf5-927770ce5162 | -13.62874 | -48.72227 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbff4579-f21d-3d83-a46f-a5384601a0fc | -13.34623 | -48.04808 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b844b1c4-1619-3535-ae83-393ebdf818c7 | -13.35272 | -48.04887 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2bc97a45-15e2-3be8-8fa9-52bd6c6ad364 | -14.86665 | -51.47387 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f5d95632-4e5a-3ace-bce0-722758952c1c | -15.99804 | -56.01594 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1e8c5bf3-51c2-354a-8453-6645067e8dd3 | -13.26594 | -48.47365 | 2025-10-06 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cdadba2-bd64-3da1-b9e4-fe706e6d45d1 | -13.10665 | -48.01153 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 434118d1-ee7e-369a-a468-b9e99f56df8a | -15.60117 | -52.55069 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0fd5b63f-628c-3edf-bb5d-c8cd397fa2c4 | -15.22212 | -56.83146 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e5492d2-c064-3f12-913a-6a6a637cb44b | -17.83847 | -57.62452 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8ba8af09-a2d2-3edd-8049-cb67220d4359 | -13.31789 | -48.06643 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 713cf35f-1125-3c99-b837-aab31e516803 | -18.27015 | -53.32447 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2380ea05-f203-3178-806a-6ca215de7299 | -12.27465 | -55.11307 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2218ff41-ab65-3de8-8374-f231c4c8537a | -16.02555 | -51.05745 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2732ca22-6dc7-3d6b-9aea-b54091da3e93 | -15.35077 | -48.0024 | 2025-10-06 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18051f2b-ed39-3760-aa36-94dac3b4bbe7 | -13.2704 | -47.83349 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d99a171a-0840-3858-a9c8-91fb8ee6841c | -14.61929 | -52.50853 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d2457eb3-2f8e-3a88-be1a-ad374d98c035 | -18.11375 | -53.41053 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12b4e274-4d45-3616-a220-71b1e542dc68 | -13.04553 | -47.91248 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b72866f-8484-3d60-a3e6-1e268cfff96f | -18.13815 | -53.41392 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6575402f-cf91-309e-8eb6-ad49e623b381 | -13.1343 | -48.00165 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e31a5606-5e9c-322c-b87d-3bd5c645c014 | -12.78766 | -56.96154 | 2025-10-06 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72a186cf-203f-331f-bf8e-5ab6c2673180 | -15.58362 | -52.44355 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6376f1e-4547-394a-a7ed-e7a030ee0d80 | -14.66088 | -48.37167 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 56e8024f-99e0-394e-b1f2-699b9e3ce813 | -15.61188 | -52.54632 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 76e29e57-a841-3b06-a617-032aca8eea50 | -14.67797 | -48.39519 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3052d7a0-37ca-3692-b2cc-9bf738f6214c | -14.60866 | -52.51312 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17d96a11-deb2-3fe0-bdec-805f5baf1212 | -14.86521 | -59.65354 | 2025-10-06 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README69.md)
