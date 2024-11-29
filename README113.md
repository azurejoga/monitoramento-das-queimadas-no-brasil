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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdd7ca59-cc74-336d-96ca-ea0a0782313a | -3.6943 | -47.1168 | 2024-11-29 14:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 8d06729c-d695-3e02-b8d5-ff1e4d54d835 | -3.0382 | -53.6849 | 2024-11-29 14:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 26574174-379d-3f65-8ffa-65c040af1d50 | -3.41 | -44.6283 | 2024-11-29 14:10:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 64cfa86a-293a-3962-9701-fc4d0afbfed7 | -3.1787 | -46.2995 | 2024-11-29 14:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| dce68b4f-5faf-3b89-8330-c0b212d2688d | -2.8851 | -45.5073 | 2024-11-29 14:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| bab72ed1-4119-3c31-acb7-6493353d364d | -17.5862 | -57.5944 | 2024-11-29 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| f41d3232-f98c-3622-93c3-0d2a9d1aab13 | 1.4552 | -55.9053 | 2024-11-29 14:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 1fbf6720-6ee6-3419-a1dd-41481179d627 | -3.7129 | -47.116 | 2024-11-29 14:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 282b0ffa-fc00-3781-9e72-c93ea27c5a98 | -2.3233 | -46.8786 | 2024-11-29 14:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| ebd920fd-19d0-3ae3-8f69-98c99ff74598 | -4.1761 | -44.2716 | 2024-11-29 14:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 160.3 |
| c12c9bbf-35e7-31c5-825d-d24e36fdb48e | -3.6135 | -41.6328 | 2024-11-29 14:10:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 4f56b7e7-0b25-34de-872b-83c2b20329e2 | -1.7507 | -46.2523 | 2024-11-29 14:10:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 1b14a8fe-9d2e-38c9-a1b5-c0c4aa9253ac | -2.6498 | -48.7986 | 2024-11-29 14:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| cbf1feb5-64ce-3b78-9ed6-a19d74c79834 | -2.5718 | -50.0103 | 2024-11-29 14:10:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e556580e-0605-38a5-ba9b-c05a6e88f22f | -11.4018 | -45.0746 | 2024-11-29 14:10:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| eddc9e4b-8ae6-3c98-a59e-44b123438f7c | -2.6684 | -48.7767 | 2024-11-29 14:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 10f53504-d4ef-38b7-b0d2-8c5cf194f54f | -1.5869 | -53.8336 | 2024-11-29 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 874546c1-aad1-30a0-8c55-6337e6b239cf | -1.7696 | -46.1188 | 2024-11-29 14:10:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| aea65b4f-220d-385b-ab27-b7118b5f9444 | -6.9424 | -42.8126 | 2024-11-29 14:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 003a5521-9525-3ce6-ad83-75bf62d8f8b5 | -3.2396 | -53.9216 | 2024-11-29 14:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7430333e-ff0c-366b-8525-368ac3eee493 | -4.6817 | -46.6732 | 2024-11-29 14:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 37aab849-5469-301b-91ca-5dac3b1c6230 | -3.7897 | -40.413 | 2024-11-29 14:10:00 | GOES-16 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 6dee9152-f12c-3366-b183-ce201b285a83 | -3.4899 | -40.3804 | 2024-11-29 14:10:00 | GOES-16 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 98.7 |
| d8785502-446a-31d3-9200-91099a351551 | -2.0439 | -54.6883 | 2024-11-29 14:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 3cd67016-eb2b-32f1-b7cf-d764d769d4ad | -3.403 | -42.4748 | 2024-11-29 14:10:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a499dbaf-4d3a-34ba-b8fc-14e58bf96698 | -2.8424 | -46.8413 | 2024-11-29 14:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 059c9a5a-d9d3-3de7-8cf9-233c253142c4 | -8.2737 | -48.0364 | 2024-11-29 14:10:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 485ddb12-d499-3cd7-a97f-864ea46d5d89 | -3.6584 | -40.4203 | 2024-11-29 14:10:00 | GOES-16 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 1b18ebe9-0d9d-30b4-9236-9122a3bcfe41 | -2.8611 | -46.8186 | 2024-11-29 14:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 180.9 |
| d43d201f-2a3f-3595-871f-2ac851be59ba | -4.8527 | -41.2687 | 2024-11-29 14:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| 86356203-1109-337a-98bb-f4a7fc2bd1e1 | -17.5495 | -57.4347 | 2024-11-29 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| e1229ed6-e706-3455-8f80-0542eee1f45f | -2.3059 | -46.5488 | 2024-11-29 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 223.1 |
| 2c41d667-5328-380f-9ad1-348e8dcc6e9a | -2.9844 | -53.2819 | 2024-11-29 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 78d87d53-c7b0-3a0c-b737-9d8eea46b092 | -3.6942 | -47.1387 | 2024-11-29 14:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 268.2 |
| 2e021aaf-d44a-3151-8f8f-e5dcbe918ba8 | -2.8426 | -46.7973 | 2024-11-29 14:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f39b8466-d2d2-3078-95cb-6321a1b92af9 | -6.9613 | -42.8108 | 2024-11-29 14:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| f2eb541c-658a-364f-b147-497d321c0ddd | -4.0866 | -50.0232 | 2024-11-29 14:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 7d6d2387-bff5-377e-a5bb-abeb34f15d97 | -4.4404 | -46.5975 | 2024-11-29 14:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| abac3ceb-35a0-3534-a827-aee3ec045398 | -2.5718 | -50.0103 | 2024-11-29 14:20:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b0512c35-7c1a-32c6-844e-c3fb7b5fa47e | -2.3636 | -45.9485 | 2024-11-29 14:20:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| db3dcd98-400a-3c41-97a1-178c18365b13 | -1.7693 | -46.252 | 2024-11-29 14:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 0637ccc0-4bc9-3117-919d-727fb3f79a9f | -1.6235 | -53.8733 | 2024-11-29 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| eabf21c9-748e-3932-b938-637d58dacd83 | -3.7129 | -47.116 | 2024-11-29 14:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 71dab9f1-ead2-3e58-9354-9a70ca78d8a6 | -3.1421 | -42.3686 | 2024-11-29 14:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c41b7504-31de-3d67-a2aa-bb05ea153d4f | -3.4531 | -43.5474 | 2024-11-29 14:20:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7a52e64c-9a7b-31df-bf3a-0c11a27ddce0 | -3.41 | -44.6283 | 2024-11-29 14:20:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 47131881-70c8-3337-b0e3-8805e7f200d9 | 1.3535 | -50.6207 | 2024-11-29 14:20:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 8514b5bf-5a6e-36b7-9993-41303dcf9451 | -2.0439 | -54.6683 | 2024-11-29 14:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 4228c802-e097-3ff3-a364-a39d6c242024 | -3.8431 | -47.0666 | 2024-11-29 14:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| caf39a09-d88c-3404-800e-0104f5d5f1f6 | -6.7782 | -44.0876 | 2024-11-29 14:20:00 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a4b789c9-da48-3fd0-bd65-115d32d30fb5 | -1.6181 | -47.5065 | 2024-11-29 14:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| df2f7d80-747a-3c05-89a4-67e14a27fa5f | -1.9698 | -47.4342 | 2024-11-29 14:20:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f4d55232-a49a-39a0-a447-ed466a701219 | -3.0673 | -42.3955 | 2024-11-29 14:20:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 0d7201c3-a63a-332b-8e3c-052c7d500a7d | -3.6942 | -47.1387 | 2024-11-29 14:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 257.8 |
| d2e9163e-a124-34b6-9bd5-64a792a3b673 | -2.3259 | -46.1275 | 2024-11-29 14:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 661aa7f7-289f-372e-9491-b9c8f7b5ddb3 | -2.8611 | -46.8186 | 2024-11-29 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 175.9 |
| d5216e9d-e2d3-3261-9605-ff63aeb73b52 | -2.9399 | -45.7293 | 2024-11-29 14:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 20509a5b-7075-3dc8-910f-9e6170ed737f | -3.6943 | -47.1168 | 2024-11-29 14:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 9f779147-23c7-3f5b-8621-17cfcef3812f | -3.7407 | -42.2453 | 2024-11-29 14:20:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| c588b35e-53c5-383e-9ad2-01978d141596 | -1.5868 | -53.8537 | 2024-11-29 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a8d02cb7-99e8-3181-85be-a26fc0e59bb1 | -3.6135 | -41.6328 | 2024-11-29 14:20:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 5c54e54b-0de8-3627-b8cb-3376cdd8ad13 | -3.7406 | -42.269 | 2024-11-29 14:20:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 0d608ca2-8a2f-3bd9-a1fb-136a96aec598 | -1.7507 | -46.2523 | 2024-11-29 14:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |
| cba68a2f-1ad7-350f-9087-f757910ee9e5 | -4.1953 | -38.8217 | 2024-11-29 14:20:00 | GOES-16 | REDENÇÃO | CEARÁ | Brasil | 2311603 | 23 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 7dac71ad-d24c-3348-ada2-0ed14a44c305 | -2.6498 | -48.7986 | 2024-11-29 14:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 92430d03-d7a6-3c84-b6e8-29e0885a3fd8 | -1.22 | -53.7573 | 2024-11-29 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 84854c7d-06c4-30b7-9a95-0aa1bf4777da | -2.8424 | -46.8413 | 2024-11-29 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| d02320dd-3df6-385c-9cc5-8c4c174da5d5 | -2.8795 | -46.84 | 2024-11-29 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 75baa0d6-f525-3412-bad6-7c49c2175ed5 | -3.4102 | -44.6055 | 2024-11-29 14:20:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 091a5873-f890-3757-9129-5cc8dcd4a8dc | -1.5685 | -53.8338 | 2024-11-29 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f5cb999a-0ffc-3868-8f6f-e9a1956a041d | -4.4999 | -43.3295 | 2024-11-29 14:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| bada0dfc-aab2-30b9-8216-43707d23a4e3 | -2.3059 | -46.5488 | 2024-11-29 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 163.0 |
| a060fdec-ec11-34e7-b9dd-154d59b4970e | -3.6133 | -41.6568 | 2024-11-29 14:20:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 609e3403-a297-3ad7-8d03-3e9c15c97a5b | -4.1121 | -39.9263 | 2024-11-29 14:20:00 | GOES-16 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 40c97cb9-9edf-3f3a-b56e-86667577299d | -2.966 | -53.2824 | 2024-11-29 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| b60d8a14-dc12-3251-8caf-64bb3f30b202 | -6.9424 | -42.8126 | 2024-11-29 14:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 69ed3b8a-0504-3af0-88e0-d3efa00969fd | -2.6499 | -48.7772 | 2024-11-29 14:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 23e7e095-e93a-391c-b987-d31ab267c948 | -2.8426 | -46.7973 | 2024-11-29 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f95ce282-1622-3f3c-bdd1-dac1e79ebd2b | -3.142 | -42.3922 | 2024-11-29 14:20:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f2dbfc2d-f23b-36d5-b333-506589690d3c | -4.8527 | -41.2687 | 2024-11-29 14:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 131.8 |
| eb801409-4fb1-330d-9102-a06ce0ddc2bb | -0.616 | -51.7058 | 2024-11-29 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 38ea86c6-fdac-3be3-b209-f7152d225284 | -4.4222 | -43.7516 | 2024-11-29 14:20:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 913a224d-32ef-3eb3-866a-25b77a93beb7 | -4.0866 | -50.0232 | 2024-11-29 14:20:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bba1e111-eb80-3ca7-8662-6cd1365f1ccb | -11.4018 | -45.0746 | 2024-11-29 14:20:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| b5759f5a-06db-39fb-b69c-6d3965ec4b51 | -1.5869 | -53.8336 | 2024-11-29 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 67fc0544-f9af-328a-a30d-ae31f2714c86 | 1.2171 | -55.9471 | 2024-11-29 14:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ec54bafa-e237-39d2-9ab1-2ab3bb25de89 | -1.7696 | -46.1188 | 2024-11-29 14:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 4115e3dc-4f7e-3573-81e4-2434375b6b11 | -2.9646 | -53.7271 | 2024-11-29 14:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| fb10f070-4991-3450-a1ac-85d0dd59f6d2 | -3.7128 | -47.1379 | 2024-11-29 14:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 004da69a-7440-3874-b393-be4aad1056e2 | -5.9766 | -37.9856 | 2024-11-29 14:20:00 | GOES-16 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 174.7 |
| 568f93a2-6d77-35a5-ac87-e1e7c94dc99f | -2.6684 | -48.7767 | 2024-11-29 14:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 378080f6-e8be-36c8-ac3a-7e10e8c732d8 | -4.4405 | -46.5754 | 2024-11-29 14:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e0ba3d52-2e79-3f0f-ae3e-c7e4161ae3f2 | -2.8425 | -46.8193 | 2024-11-29 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| cf386f66-41c4-3021-b222-1b436b9067e8 | -3.202 | -41.629 | 2024-11-29 14:20:00 | GOES-16 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| ff82b793-b40a-3834-b1d1-dd8405bacde7 | -6.9613 | -42.8108 | 2024-11-29 14:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| d14662da-66f8-3c79-9ed1-4fd6f32e906a | -2.5718 | -49.9892 | 2024-11-29 14:20:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5b66ac39-cc2f-3448-b53c-1b31d6f2b2ca | -4.5751 | -45.9236 | 2024-11-29 14:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7cb94c99-e678-323e-8004-fdc2b59c6ae4 | -3.1787 | -46.2995 | 2024-11-29 14:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| a074f6e7-e8fb-351b-bd46-1ff1b09e4e18 | 1.3719 | -50.6205 | 2024-11-29 14:20:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 89859d4c-db12-3d3b-81a5-7502ef240c40 | -3.6584 | -40.4203 | 2024-11-29 14:20:00 | GOES-16 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 100.7 |


[Clique aqui para ver as próximas entradas](README114.md)
