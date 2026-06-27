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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c101780c-44b4-3174-bfc0-aca52c61f7af | -13.2392 | -54.4129 | 2026-06-27 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 3c034aa1-68b9-301b-b535-3dbe5f3b473d | -13.2201 | -54.415 | 2026-06-27 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 183.2 |
| 6730009d-cd4c-3dd2-a2a3-989045b106f4 | -12.4464 | -58.4825 | 2026-06-27 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 7b97b6cc-6353-3852-9152-a06e1e9fa318 | -11.9095 | -57.4134 | 2026-06-27 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 149.5 |
| d2951130-cfcf-3e23-955d-31fc99860899 | -11.9097 | -57.3935 | 2026-06-27 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| d5480ecb-c9cf-3635-8fb0-69f6420157d1 | -12.4651 | -58.5009 | 2026-06-27 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 730.4 |
| 4b8f858d-2a9d-32b9-ac94-87455b9c2dac | -11.9284 | -57.4119 | 2026-06-27 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 145.1 |
| c5f5e673-e82f-39b4-adea-2e1935930c0c | -12.6236 | -57.8926 | 2026-06-27 13:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e294aedd-e6e8-3b37-a326-048e93c466d7 | -12.4654 | -58.481 | 2026-06-27 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 75b14463-c59a-389b-a118-890331dfbc4e | -12.6046 | -57.8942 | 2026-06-27 13:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b44c6ad7-1959-3292-aa5b-796168ee83b3 | -10.7777 | -54.0983 | 2026-06-27 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 455d6b77-f38f-3a41-ab31-8ccd5909d4bc | -12.4464 | -58.4825 | 2026-06-27 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 02e937a4-4e0d-3cfc-8f8b-789f03822b42 | -12.6236 | -57.8926 | 2026-06-27 13:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2159667b-1806-33b9-9780-1055a6a2d698 | -12.4651 | -58.5009 | 2026-06-27 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 795.9 |
| 5e18267c-9300-31af-9a81-35fb4a48d682 | -11.9097 | -57.3935 | 2026-06-27 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 219e37dc-bd0e-3a81-9ae1-18f67a406a34 | -12.4654 | -58.481 | 2026-06-27 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 235.5 |
| dbbd5d65-12f1-3c6c-900a-02b264739e8e | -11.9284 | -57.4119 | 2026-06-27 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 211.3 |
| 8bb0f7be-841c-3874-be4a-182e15407041 | -11.9095 | -57.4134 | 2026-06-27 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 85af4041-1372-3e98-abd0-8f7553ebca9b | -12.4462 | -58.5023 | 2026-06-27 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 411.8 |
| f6560b2a-90e3-3ce9-85a0-90af3ad21513 | -13.2392 | -54.4129 | 2026-06-27 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 344.1 |
| 6f1f1623-e8cd-3dac-bfa1-040ef0214866 | -13.2201 | -54.415 | 2026-06-27 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 194.1 |
| 0ee06d00-b9d6-360c-bb5f-74605cad585b | -12.6046 | -57.8942 | 2026-06-27 13:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b9546f96-04df-3f89-af15-eb4e3faf3e75 | -12.6236 | -57.8926 | 2026-06-27 13:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 871d00e0-898a-34f4-bcc6-aa50485315de | -13.2392 | -54.4129 | 2026-06-27 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 321.1 |
| b1594934-8cbc-3e5e-a0f0-73f85e194354 | -13.2201 | -54.415 | 2026-06-27 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 135.3 |
| f4144583-5ee1-3bb5-99cd-99d5130140be | -10.7777 | -54.0983 | 2026-06-27 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ab19cdd6-9ce8-390c-a3c1-2beb55d56445 | -11.9095 | -57.4134 | 2026-06-27 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 228.4 |
| 1f4bc1e6-7ee5-3b78-bce8-74cad269d5af | -11.9097 | -57.3935 | 2026-06-27 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 0dabe856-7922-381a-a653-9115ee875459 | -11.9284 | -57.4119 | 2026-06-27 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 202.8 |
| e469ba95-b157-3e75-b8d9-b8588b87d892 | -12.6046 | -57.8942 | 2026-06-27 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 00bd7a20-b5d2-3637-8d65-6ec8ceaae13b | -11.9284 | -57.4119 | 2026-06-27 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 213.1 |
| c41dcaad-2055-3d48-9a7f-343052c9dc85 | -13.2583 | -54.4109 | 2026-06-27 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 89903af8-8f53-3e23-bb86-42fe1db7ffaf | -11.9097 | -57.3935 | 2026-06-27 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 161.1 |
| d2532cdd-5b43-3e92-aa86-844455bc445d | -10.7777 | -54.0983 | 2026-06-27 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9fce07f5-c750-3972-8d99-7863b1ec298a | -12.6236 | -57.8926 | 2026-06-27 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 73471715-8e40-30aa-a391-051ebf6b206e | -11.9095 | -57.4134 | 2026-06-27 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 300.7 |
| 6412c6df-5492-38ed-ac20-0ece5228a21d | -13.2392 | -54.4129 | 2026-06-27 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| b9f4da29-0efc-395d-8f86-69a91757dfb0 | -13.2201 | -54.415 | 2026-06-27 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 142.0 |
| d63fc727-cbb6-34e4-8aee-8ff33a64ba02 | -10.7774 | -54.1188 | 2026-06-27 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 0ea6918e-3779-3607-bce7-15586e26e85e | -12.6046 | -57.8942 | 2026-06-27 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 32b8dcca-d732-3b60-a560-dce1134ba60f | -12.6236 | -57.8926 | 2026-06-27 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| ccac1fa4-40a2-3e92-b3d6-ba44602c3b03 | -11.9284 | -57.4119 | 2026-06-27 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 266.8 |
| 7d8747db-3c18-3b39-8a8d-8f4ff9aa2ae2 | -12.6048 | -57.8743 | 2026-06-27 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| adbc3a63-393b-3009-bad6-be418b8242ba | -11.9095 | -57.4134 | 2026-06-27 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 01dc8af6-41e3-35e2-af14-bc2a93f1de0b | -10.7777 | -54.0983 | 2026-06-27 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7979e5c2-1bd7-3269-b4de-140252624c94 | -11.9097 | -57.3935 | 2026-06-27 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 3534b55f-8469-3563-81c9-0590896d54c4 | -11.9095 | -57.4134 | 2026-06-27 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 187.8 |
| f6323e40-0249-31c5-b551-04e00645edcf | -10.7774 | -54.1188 | 2026-06-27 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e1fadb30-a7cf-3977-a61f-cda1ae40654c | -11.9097 | -57.3935 | 2026-06-27 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 1c5fd4eb-ca94-3dc3-9eb4-d9dfee92e257 | -8.3095 | -48.1859 | 2026-06-27 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| f52a8103-93e1-3731-96c1-cb271efa607f | -10.7777 | -54.0983 | 2026-06-27 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d05c1b3a-6107-3f1b-9447-6b207e5d645c | -12.6046 | -57.8942 | 2026-06-27 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f0066a70-0f8a-352d-88b3-60fe20438a77 | -8.3093 | -48.2077 | 2026-06-27 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 211.3 |
| cd0fb0b7-6054-37dc-a05b-8cc442fc5620 | -11.9284 | -57.4119 | 2026-06-27 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 297.4 |
| ef1e86fa-91ba-394b-86b6-a3137d593dae | -12.6236 | -57.8926 | 2026-06-27 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 06e92aa7-769d-34c0-964c-6fe1ee2707e5 | -13.2392 | -54.4129 | 2026-06-27 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 359.8 |
| 4938ad1f-dca8-380f-9639-21d75e6c7fa4 | -12.6048 | -57.8743 | 2026-06-27 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 62d576e0-0838-360d-b95d-afceea68ca5e | -13.2201 | -54.415 | 2026-06-27 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 216.0 |
| 9155dac3-8534-3da4-a9d0-da46bb7e4784 | -13.2389 | -54.4336 | 2026-06-27 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 76ce1f91-da44-3d1d-af90-7fb714618843 | -13.2583 | -54.4109 | 2026-06-27 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| de9c80ae-b9fa-32a6-92f1-84899ff9e97b | -13.2198 | -54.4356 | 2026-06-27 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 47d368d7-fdcf-35e8-9a3d-a6573ba362fc | -10.5374 | -53.7094 | 2026-06-27 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 083fcdba-945c-3890-83c8-cdebf5292539 | -8.2905 | -48.2094 | 2026-06-27 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 212.1 |
| bd352ace-e943-3030-84d8-0497144277db | -13.2583 | -54.4109 | 2026-06-27 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 9cadf9b4-1b2d-33e3-b3b0-a38aac1558d7 | -10.7777 | -54.0983 | 2026-06-27 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 5dde8c12-e494-3398-a810-a9a4cfd6e711 | -10.5374 | -53.7094 | 2026-06-27 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 44d631b6-018a-3da0-a8fa-e4125fd6b0ee | -11.9097 | -57.3935 | 2026-06-27 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| b11a427b-5713-34fe-9972-818ea5821802 | -11.9095 | -57.4134 | 2026-06-27 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 239.6 |
| 69ce2c40-9e88-3075-bd5d-b17b2ad0b8b6 | -12.6048 | -57.8743 | 2026-06-27 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| f88e05e4-43b8-3fdd-bdcc-70b47e8608a7 | -11.9284 | -57.4119 | 2026-06-27 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 349.5 |
| 0eaafbe8-378f-3074-b8a8-9fb8a9af71b9 | -12.6046 | -57.8942 | 2026-06-27 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 10b95e97-40b8-3527-b084-e90b0be74f0b | -12.6236 | -57.8926 | 2026-06-27 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| df402aa5-038d-3f3c-8906-fdff9010ac3b | -13.2392 | -54.4129 | 2026-06-27 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 227.9 |
| 7d8c8292-d2d5-31e7-9281-e881898f357b | -13.2201 | -54.415 | 2026-06-27 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 11e43fdd-3b17-36c8-a6df-321de9b69733 | -8.3093 | -48.2077 | 2026-06-27 14:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 449f1fb8-76b1-31d5-924e-90223d2979e6 | -8.3095 | -48.1859 | 2026-06-27 14:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| e148005c-4973-3261-8e22-4250c4c65f73 | -13.2583 | -54.4109 | 2026-06-27 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 21e9ed2b-5abd-323f-9d9e-a59b81ad4f63 | -8.3093 | -48.2077 | 2026-06-27 14:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 35a25bdd-23f5-3f09-a99a-a778887516bc | -12.4462 | -58.5023 | 2026-06-27 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 359.3 |
| 06e8276a-3bea-379c-9bda-3bbd175ea66a | -12.6046 | -57.8942 | 2026-06-27 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 6bab08db-e555-3ff0-939d-c326ca7a1db4 | -10.7777 | -54.0983 | 2026-06-27 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2a6a121c-349b-30e0-a1e8-7ce88e49dd67 | -12.6236 | -57.8926 | 2026-06-27 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 00c2521f-54c0-3039-9931-fdb1fd00e86b | -12.4654 | -58.481 | 2026-06-27 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 315.1 |
| 2f8e424e-9780-31fc-9006-4c66a4abcb90 | -12.4651 | -58.5009 | 2026-06-27 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 942.3 |
| c7681a01-6ac5-32cf-8731-771790141337 | -13.2392 | -54.4129 | 2026-06-27 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 257.3 |
| fb86a13c-4027-3c90-9498-260cae32934d | -13.2201 | -54.415 | 2026-06-27 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 202ff113-232e-3177-8df7-0c496c30ca1e | -12.4464 | -58.4825 | 2026-06-27 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 68a2d9b6-0f7e-3d6f-b503-82863a7ab30e | -11.9097 | -57.3935 | 2026-06-27 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 2a24a2e9-b813-3ed4-b2b3-b759036e7416 | -11.9284 | -57.4119 | 2026-06-27 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 310.1 |
| e59d2c50-b48c-3797-a3cc-04bed679e077 | -11.9095 | -57.4134 | 2026-06-27 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 279.8 |
| 83e54395-7006-3e3e-975f-bd3ead473cbc | -8.3095 | -48.1859 | 2026-06-27 14:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 7ac84491-5692-3dbf-a952-592e8bd9ec67 | -10.5374 | -53.7094 | 2026-06-27 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 91449d62-e164-3edd-ae5a-39c87bc0ab0e | -13.2389 | -54.4336 | 2026-06-27 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1bbf71b6-b5cf-3b07-a0f1-09f0debc364b | -11.9097 | -57.3935 | 2026-06-27 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| f7f614c7-d8cf-3582-91d6-9f2ac13a69da | -12.6046 | -57.8942 | 2026-06-27 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 67712fa1-2363-3297-87d3-4f24c0dfb297 | -13.2201 | -54.415 | 2026-06-27 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 9a8a6d1b-f79f-336f-b83d-11362f4b758d | -10.7774 | -54.1188 | 2026-06-27 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d7aa6910-d04e-38cd-ba3d-eb251ecde4ff | -11.9284 | -57.4119 | 2026-06-27 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 368.1 |
| bf74725c-cf7f-3085-85a3-a34ccf5c284c | -13.2392 | -54.4129 | 2026-06-27 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 241.1 |
| 7cddd350-84ab-353d-b453-ca1b9024dc41 | -12.6048 | -57.8743 | 2026-06-27 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |


[Clique aqui para ver as próximas entradas](README24.md)
