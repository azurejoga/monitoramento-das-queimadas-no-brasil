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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14fab12a-5a9d-3076-b61b-3ce2bd25cc17 | -12.22811 | -57.28824 | 2026-06-04 12:14:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 544b5806-226f-3109-80f1-9cbf79479cea | -12.45626 | -58.46661 | 2026-06-04 12:14:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f69dfdd2-1ed4-3272-bd61-d2389ad67aed | -8.49093 | -51.54122 | 2026-06-04 12:14:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 90defd44-50b8-3308-ad27-debff212395d | -11.25884 | -53.97123 | 2026-06-04 12:14:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6d663cdf-3166-310c-9581-dfe1a794fab0 | -15.408 | -51.06761 | 2026-06-04 12:14:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 240a04d9-16c0-34d3-bc74-a04cc1eef5ff | -12.33993 | -50.00136 | 2026-06-04 12:14:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1000e2d2-f81c-309d-abf9-381807c67da5 | -12.1806 | -54.53973 | 2026-06-04 12:14:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c928233-2268-3e83-a47c-5f6513a4d21b | -12.73933 | -54.19641 | 2026-06-04 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9c1942cd-13a4-3c3b-899c-6ac7940c0cf9 | -19.74003 | -53.54935 | 2026-06-04 12:17:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f6722541-ca66-3dda-b0a0-09bf2007f5d2 | -18.187 | -52.18157 | 2026-06-04 12:17:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 34.0 |
| bf924a32-4254-34b9-8ae4-ea82fc03aa4d | -18.07864 | -52.63988 | 2026-06-04 12:17:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 74d1a646-3bfd-332b-9547-51547e208209 | -30.51253 | -52.61715 | 2026-06-04 12:19:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 13.6 |
| d9e47fa1-87e2-38c1-a8b6-6dc25db9aeda | -11.6329 | -55.1844 | 2026-06-04 12:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 945285f1-940e-3a27-a7a7-47102c40e8b9 | -12.2325 | -57.2872 | 2026-06-04 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 0e420859-6676-3e23-b7a2-d63f92d0986c | -11.6329 | -55.1844 | 2026-06-04 12:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1a154a2e-3c7d-369c-8039-a2d8cc0d191f | -12.2325 | -57.2872 | 2026-06-04 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1837b7c9-4ef0-3710-b78b-5f2cfd005bc5 | -12.2325 | -57.2872 | 2026-06-04 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e3d7d317-e0e7-3748-a86f-e7cc823d1bf7 | -11.6329 | -55.1844 | 2026-06-04 13:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| d406bc06-71dd-3ef9-bce2-138fc7ad1aa8 | -12.4654 | -58.481 | 2026-06-04 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 154.0 |
| b6a25778-42b9-3cd1-8a5e-00f2c34374c1 | -12.4466 | -58.4627 | 2026-06-04 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 9f9fe34c-dfcf-3f9d-8332-e9d37dbe62c8 | -11.6329 | -55.1844 | 2026-06-04 13:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 27ecae7d-81f6-3492-9858-ed5a38556aa7 | -12.4464 | -58.4825 | 2026-06-04 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 169.8 |
| d1267ce9-70e0-3da4-96c3-bdfcd4ded34c | -12.4656 | -58.4612 | 2026-06-04 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| d35171ec-395e-3694-9a77-e28187532fb1 | -12.4656 | -58.4612 | 2026-06-04 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 5d619f29-7c8e-31e8-9419-b6cd99ff7382 | -12.4464 | -58.4825 | 2026-06-04 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 446.8 |
| 32c51de7-c268-3d94-bbe8-163cd5622d5e | -12.2325 | -57.2872 | 2026-06-04 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 75660497-27cb-37c2-8afd-767e3b1f9eb2 | -11.6329 | -55.1844 | 2026-06-04 13:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 80ed4c22-b890-3de5-af25-eafa2e99f70e | -12.4654 | -58.481 | 2026-06-04 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 299.7 |
| 02d77e15-49b2-385f-8c87-0df494761194 | -12.4466 | -58.4627 | 2026-06-04 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 298.0 |
| e4aef330-2440-3fae-a319-03538fac0b01 | -12.4656 | -58.4612 | 2026-06-04 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 610d79f5-55b3-3fac-bc4d-feb4ba3cef24 | -12.4464 | -58.4825 | 2026-06-04 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 593.4 |
| cad6d70e-6206-3459-87cc-c0af167e6ec3 | -12.2136 | -57.2888 | 2026-06-04 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3ae07615-cde8-3d8b-943f-3a1c1eeebcaa | -12.2325 | -57.2872 | 2026-06-04 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 30b8f1db-4450-30e3-89a5-ee9a89ce9495 | -12.4654 | -58.481 | 2026-06-04 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 253.5 |
| 713d86cc-6f79-33b1-b754-6e5885aa74b0 | -16.5973 | -58.2365 | 2026-06-04 13:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| e843f98f-6097-32d7-8815-59b2e83ac218 | -11.6329 | -55.1844 | 2026-06-04 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 3870504a-4ef3-33e2-aa11-4e2df1b70b5b | -12.4466 | -58.4627 | 2026-06-04 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 450.6 |
| cd6d0e8f-a2b0-338f-8555-eb78a7e7e29e | -12.4654 | -58.481 | 2026-06-04 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 6349c3ea-f0f9-3d6d-b03c-c7483996b484 | -11.6329 | -55.1844 | 2026-06-04 13:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 1944812a-bbd9-33d5-a19a-cd86d6524a69 | -12.4656 | -58.4612 | 2026-06-04 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 203.1 |
| ba71065e-4d17-3d98-9863-ac944bd37d4f | -12.4464 | -58.4825 | 2026-06-04 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 761.2 |
| d03ddd53-21b3-318a-9aa0-7ba330e82424 | -12.4466 | -58.4627 | 2026-06-04 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 587.0 |
| 737b1a51-5505-3c62-9b04-16b6b6edef88 | -12.2136 | -57.2888 | 2026-06-04 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 6e393174-4fbe-320b-8952-5fff76ff2067 | -12.2325 | -57.2872 | 2026-06-04 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 884b621b-02af-3b36-8c4d-d12673777114 | -16.5973 | -58.2365 | 2026-06-04 13:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 48af6414-25bb-3db9-961f-dbbb2c46362b | -12.4283 | -58.4048 | 2026-06-04 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 16a108ea-232f-3745-8974-e409b1982473 | -14.173 | -58.9937 | 2026-06-04 13:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| bad78927-493d-30b2-be87-967efbf81f33 | -12.2327 | -57.2672 | 2026-06-04 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c8248880-4ed1-3ac5-8b63-cd83a40185db | -7.9396 | -71.46348 | 2026-06-04 13:53:00 | TERRA_M-T | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 18f3b35c-7c09-3619-abcc-c3de6959af21 | -6.74972 | -71.69811 | 2026-06-04 13:53:00 | TERRA_M-T | ATALAIA DO NORTE | AMAZONAS | Brasil | 1300201 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fe61525c-9607-3738-8dab-8573391feec8 | -14.173 | -58.9937 | 2026-06-04 14:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 035d7268-202a-3666-a40f-804c5fcf2b8e | -16.5973 | -58.2365 | 2026-06-04 14:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| c5087b2a-06ec-3355-a94d-ad2ae0d465c7 | -12.2325 | -57.2872 | 2026-06-04 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 8b401ffa-ab9f-3591-bad7-8fc8237586b6 | -12.4473 | -58.4033 | 2026-06-04 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 447c6d9f-66ed-3bc5-9647-6e959d164799 | -11.6329 | -55.1844 | 2026-06-04 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 67c9cbb5-6448-3428-90f3-36bc6e62db7d | -14.1732 | -58.9738 | 2026-06-04 14:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| a9d0cf49-15a1-3301-b877-b63d8b7fbbd4 | -12.2136 | -57.2888 | 2026-06-04 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b7b893d4-d209-36b6-96ac-3364af9220b7 | -12.2327 | -57.2672 | 2026-06-04 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 592eaf8e-8b1f-3f51-9f08-be36d1e27b13 | -10.8573 | -53.7425 | 2026-06-04 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e9a7f613-02d6-36b4-801e-d331b552cc6d | -12.2136 | -57.2888 | 2026-06-04 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| bcacca98-4c61-30cf-af94-02496e1c9c91 | -12.4473 | -58.4033 | 2026-06-04 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 8e8a62e9-c5d7-3a0b-8e1e-9425d6433e57 | -12.4656 | -58.4612 | 2026-06-04 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 319.5 |
| c4fece60-8d00-3bd5-bc8a-50570693f098 | -12.4654 | -58.481 | 2026-06-04 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 384.5 |
| 86a75634-10a4-3c42-a30f-3464012f5ccb | -12.4466 | -58.4627 | 2026-06-04 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 644.0 |
| 84683b1b-7308-30c9-a938-55b53aecf22c | -11.6329 | -55.1844 | 2026-06-04 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| c84b00e1-2745-38e4-a1ff-bb85d426fd6e | -16.5973 | -58.2365 | 2026-06-04 14:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 2e7b4c8d-0296-39c7-94b9-616226e5abb7 | -12.2327 | -57.2672 | 2026-06-04 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| aa1fd53f-dc5a-3ebc-b28d-c30cf907b7e4 | -12.2325 | -57.2872 | 2026-06-04 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 56f06e2e-84d0-3f22-8158-00f46aefb0ce | -12.4464 | -58.4825 | 2026-06-04 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 759.8 |
| f6c20649-a3d6-3d78-aba8-21e5046b0071 | -14.0917 | -59.3975 | 2026-06-04 14:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5448ba73-4266-31df-9168-f91dc2d1059e | -12.4283 | -58.4048 | 2026-06-04 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 8424a9c1-f3fb-3fec-b787-a54b7b7ae16a | -11.886 | -57.8329 | 2026-06-04 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| fd9dde9a-a55b-30c8-9289-b0613d74a1b7 | -14.1732 | -58.9738 | 2026-06-04 14:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| b45de9ad-feab-3494-bf94-8ac219c915e7 | -16.5973 | -58.2365 | 2026-06-04 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| eedec8ff-fb57-32fe-9f8c-44f483cd87df | -12.2136 | -57.2888 | 2026-06-04 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7d4e1176-1245-3fb4-862c-61caba3d312b | -12.4473 | -58.4033 | 2026-06-04 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 3b4be0cb-f9d2-345e-ade1-869f8f5b4ebe | -14.0917 | -59.3975 | 2026-06-04 14:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 08697aad-f2b8-3e1a-bd98-4acffa8d0a56 | -12.4283 | -58.4048 | 2026-06-04 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 02e273dc-4085-3d31-b9e5-500b26221794 | -14.173 | -58.9937 | 2026-06-04 14:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 82505b0c-fa75-3e11-aa7f-e984a3fd78d9 | -10.8573 | -53.7425 | 2026-06-04 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a456ea53-ad16-3e3d-a7f1-d49a8ba538ca | -12.2325 | -57.2872 | 2026-06-04 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3c81167b-adaa-3019-bb39-b74a6766c025 | -11.886 | -57.8329 | 2026-06-04 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6bf13ee0-f3f6-37e9-a933-1ca957b56047 | -11.6329 | -55.1844 | 2026-06-04 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| ad33bdf2-9ac6-3683-a518-966561161ac8 | -11.886 | -57.8329 | 2026-06-04 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| f1e75eb3-a9b2-35df-8b13-ef8c2ff3ae52 | -12.2325 | -57.2872 | 2026-06-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4c813488-b478-3e9d-bf31-b6db1864f152 | -12.4464 | -58.4825 | 2026-06-04 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 900.9 |
| f8f1a2bf-bfa4-393a-92cf-0fc435df5335 | -12.2327 | -57.2672 | 2026-06-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 969230f1-e434-3b06-90fa-ffe2ac13d427 | -14.0917 | -59.3975 | 2026-06-04 14:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 1f045e2f-24db-3f21-8cfd-9bd9b140d147 | -16.5973 | -58.2365 | 2026-06-04 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.2 |
| 31f0694a-5c93-3e88-aacf-69be0951cd24 | -14.1732 | -58.9738 | 2026-06-04 14:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ad90a5fc-13a7-3619-976e-a28cbeee47a9 | -12.4471 | -58.4231 | 2026-06-04 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e3ddf155-adb2-384f-b2de-f081bf9a3950 | -12.4466 | -58.4627 | 2026-06-04 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 818.8 |
| 75a73926-2d26-3ba4-ba79-a28767b8fdea | -10.8573 | -53.7425 | 2026-06-04 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 12d675b5-ea96-3ff4-927e-40e019ff1d13 | -14.173 | -58.9937 | 2026-06-04 14:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 7e9d565b-a828-31cc-aaea-0c5fd05c9d0a | -12.4473 | -58.4033 | 2026-06-04 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 161.6 |
| c4077715-cf06-3faf-8910-b1b923193dd6 | -12.4283 | -58.4048 | 2026-06-04 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b8596ddd-1081-392c-a3c9-7cd6527de76c | -12.4656 | -58.4612 | 2026-06-04 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 515.0 |
| 98c9c32d-987b-3fe5-9e6e-89f03c953fc3 | -11.6329 | -55.1844 | 2026-06-04 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| fe61c242-5ea0-3cf5-8f0c-d68a6a54a42f | -12.4283 | -58.4048 | 2026-06-04 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 0b464e06-315c-39ac-8f99-5b6992d02d86 | -12.4656 | -58.4612 | 2026-06-04 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 308.5 |


[Clique aqui para ver as próximas entradas](README19.md)
