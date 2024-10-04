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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32ac4141-05ac-32c6-85cc-f76b3a30ddf8 | -11.0459 | -46.515202 | 2024-10-04 00:43:13 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3092d995-06c8-3e53-9c7e-5324193d0632 | -11.0475 | -46.522202 | 2024-10-04 00:43:13 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d906f7ba-20a6-3b3f-8019-06b19e74a231 | -11.0491 | -46.529099 | 2024-10-04 00:43:13 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce819da7-a518-331d-830e-c55a84c1259b | -11.033 | -46.503502 | 2024-10-04 00:43:13 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d31f3e89-deca-339e-88df-fceb198b35fc | -11.0345 | -46.510502 | 2024-10-04 00:43:13 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 095e9cf8-2411-3e99-b5f6-a62cc55e59b4 | -11.0361 | -46.517399 | 2024-10-04 00:43:13 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d55d7f8-52f9-3eea-801d-bcf76096c466 | -11.0377 | -46.524399 | 2024-10-04 00:43:13 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8dfe3fbf-ca90-3fc9-858e-73c68f1c1938 | -10.9055 | -46.306198 | 2024-10-04 00:43:14 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 277368f0-1da8-3912-83e2-84a6f2b21048 | -10.7531 | -45.596298 | 2024-10-04 00:43:14 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b82289e9-ae15-39ab-abd9-b3f466c19fe2 | -10.6392 | -45.193199 | 2024-10-04 00:43:14 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ec6878d-e9ef-3650-803b-3b71f3ad5009 | -10.6294 | -45.195499 | 2024-10-04 00:43:14 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b6ed3090-98ee-3798-889e-f7f91915b4d1 | -9.4584 | -40.368301 | 2024-10-04 00:43:15 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a1c930f8-fe37-32fb-b81e-be78cb08263e | -9.4617 | -40.381401 | 2024-10-04 00:43:15 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 18e6e992-0057-3635-bb1c-17944efc9cd4 | -10.9065 | -46.627499 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d0ed33a-8ebf-369d-b491-c20f320ca62d | -10.908 | -46.634399 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c377f6dc-73f0-3860-b924-129f9f35e149 | -10.8888 | -46.5951 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cda2913-9e56-352b-8109-5e291c411960 | -10.8904 | -46.602001 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 835f93cb-425f-35e9-b59e-f6d6ec3bf93d | -10.8919 | -46.609001 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c93c9b9e-c29c-3a43-aa84-559c081a1801 | -10.8935 | -46.615898 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e49d789e-e62d-3296-bcfd-288ffbb34767 | -10.8951 | -46.622898 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed1e51c6-03e5-3327-989c-3b63ac2548df | -10.8967 | -46.629799 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d24a960-b4a3-3ed3-89e3-4f164946914e | -10.8982 | -46.6367 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d03b04b-0423-36fd-8379-26b7d9ae0f43 | -10.8998 | -46.6437 | 2024-10-04 00:43:15 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ddb26f9-6bbf-3058-afc0-b2367c40f4fe | -10.6163 | -45.1833 | 2024-10-04 00:43:15 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f5a6422-5fa0-3ffe-8b59-59ebe0d8e253 | -10.6179 | -45.190601 | 2024-10-04 00:43:15 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 402d5c59-05fe-3d1d-aa0e-e7503842b541 | -10.6196 | -45.1978 | 2024-10-04 00:43:15 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11bbd39e-748d-3d42-97ba-7be4bf50221f | -10.6213 | -45.205002 | 2024-10-04 00:43:15 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3e7075cf-b626-3e39-bea0-4c13466d94fb | -10.5984 | -45.195099 | 2024-10-04 00:43:15 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72d644dd-216a-3f91-85a1-4402fee34632 | -11.3209 | -48.997501 | 2024-10-04 00:43:17 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47669cf3-fc37-3a94-b41b-894fd1e8b38e | -11.3111 | -48.999599 | 2024-10-04 00:43:17 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3881c85-bf3c-3df4-9d39-d91df64e566c | -10.5241 | -46.306099 | 2024-10-04 00:43:20 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53742c29-e219-39c8-a450-f83599bfd95f | -10.5256 | -46.313 | 2024-10-04 00:43:20 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0751f16-79d1-36bf-8cb1-84f959288ef0 | -10.7438 | -47.642101 | 2024-10-04 00:43:22 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1744953a-8ef9-3b85-8ad8-0d6e1017f2e3 | -10.7454 | -47.6492 | 2024-10-04 00:43:22 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5821151c-a483-32ac-895a-349fab62d7f7 | -10.7308 | -47.6301 | 2024-10-04 00:43:22 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3138249-29ba-32dd-9976-25ef89f890d9 | -10.7324 | -47.637199 | 2024-10-04 00:43:22 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c53d337-e414-3ece-a9ce-c2852004a7ca | -10.734 | -47.644299 | 2024-10-04 00:43:22 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44cffd24-a2f1-39f9-b312-7f12a9ba5d42 | -10.7356 | -47.651402 | 2024-10-04 00:43:22 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 294ac5e9-21e9-3fdc-a4ed-4369c6a693d6 | -10.7287 | -47.712601 | 2024-10-04 00:43:22 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 025e347b-ec56-3525-b0ba-0d86fb7f0a53 | -10.7173 | -47.707699 | 2024-10-04 00:43:22 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00a6cf48-8399-399a-b43d-07d34526b90e | -10.7189 | -47.714802 | 2024-10-04 00:43:22 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d64b477-46a2-3226-8a3d-47ce5b451cb9 | -11.1365 | -49.6119 | 2024-10-04 00:43:22 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ab8f875-6cbc-397c-bbdb-046d8d647330 | -11.1382 | -49.620098 | 2024-10-04 00:43:22 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0942eeba-a307-36c3-a946-3b7f5823f773 | -11.1115 | -49.591301 | 2024-10-04 00:43:23 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 621640f7-983c-353f-bc3a-95920d2f0d92 | -11.1133 | -49.599602 | 2024-10-04 00:43:23 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba0e3218-865e-31b5-9563-965d7c7886fb | -11.1151 | -49.607899 | 2024-10-04 00:43:23 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64b47bac-2596-3349-8d60-f32d02533ebe | -11.0821 | -49.597698 | 2024-10-04 00:43:23 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7cd2d3db-f742-3c97-be0d-4149e316c22e | -11.0839 | -49.605999 | 2024-10-04 00:43:23 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e4ee45f-f3c8-31f2-afc2-201169b1cd62 | -11.0741 | -49.608101 | 2024-10-04 00:43:23 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 320a0b3a-8114-36b0-93d1-82152e9861b3 | -10.6079 | -48.047699 | 2024-10-04 00:43:25 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 650f28b1-92be-31be-b4fa-7e3ba5ee8816 | -10.5981 | -48.0499 | 2024-10-04 00:43:25 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c87fe887-d061-347a-8aad-26292cbb81ff | -10.1293 | -46.338299 | 2024-10-04 00:43:27 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68645f9a-1cf2-31a4-9b6c-ab2b1830d45c | -10.1309 | -46.3452 | 2024-10-04 00:43:27 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be3e3e96-970f-365e-b922-fe0371840049 | -9.9271 | -45.906799 | 2024-10-04 00:43:28 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9db5da3e-ddd4-3950-a2b6-dceb62103186 | -9.9288 | -45.913898 | 2024-10-04 00:43:28 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2da59896-8e3f-32b4-96ab-f788bce847bb | -9.9304 | -45.920898 | 2024-10-04 00:43:28 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36b80905-e8c5-37dc-bf76-69446ee0fc13 | -10.864 | -50.1064 | 2024-10-04 00:43:28 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa0c590e-8118-3f2a-bbba-86ed19ff127e | -10.8659 | -50.115101 | 2024-10-04 00:43:28 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 309a0f45-698a-3272-b192-cd3d31960527 | -10.4069 | -48.1609 | 2024-10-04 00:43:29 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d4e2ae9-678e-3b7d-91a5-db807eaa966f | -10.4085 | -48.168098 | 2024-10-04 00:43:29 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7b6c5e4-2955-33fe-b897-5665bf62e8d0 | -9.9776 | -46.3512 | 2024-10-04 00:43:29 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13e15526-900a-39ed-a813-b2e20c04a326 | -9.9792 | -46.358101 | 2024-10-04 00:43:29 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15452973-9043-36b5-afd0-255f083f23bf | -10.2787 | -47.679901 | 2024-10-04 00:43:29 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e96398f-5b73-3376-aa7d-fa2092566470 | -10.2689 | -47.682098 | 2024-10-04 00:43:29 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a44030e-ac24-30d0-ad1d-7673be5afc12 | -10.2705 | -47.689201 | 2024-10-04 00:43:29 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b90f4d1-098f-3d14-966c-7bb4d8ee3b75 | -10.5539 | -49.011501 | 2024-10-04 00:43:30 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08c1dfe6-1720-35ff-a81e-bfd2165fc9e6 | -10.5556 | -49.019199 | 2024-10-04 00:43:30 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87acf735-22bc-3a87-ad1d-d6b5ea912090 | -10.5573 | -49.027 | 2024-10-04 00:43:30 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42e1f28a-97a3-3523-bd98-3778c174f7e8 | -10.2509 | -47.6936 | 2024-10-04 00:43:30 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5dda7b5d-0f73-3e9b-a0ad-3bf3724073b0 | -10.2525 | -47.700699 | 2024-10-04 00:43:30 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3245835-2210-3f35-8784-b81da6a50ac9 | -10.5475 | -49.029202 | 2024-10-04 00:43:30 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17b0addf-4e2e-3d96-8bc5-93e57dba4ee5 | -10.2281 | -47.683899 | 2024-10-04 00:43:30 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 508f5b1d-552c-35a9-852a-c0c1246971cd | -10.2297 | -47.691002 | 2024-10-04 00:43:30 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf4e1bcb-4476-36b9-a431-8b8f7da64b30 | -10.2278 | -47.7285 | 2024-10-04 00:43:30 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b1fa4fa-e131-36bd-bdf3-fa00460d2b36 | -9.257 | -43.487301 | 2024-10-04 00:43:30 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ed699e4-d3b2-3438-a971-8e38a12e2794 | -9.2591 | -43.495998 | 2024-10-04 00:43:30 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 837f3561-8ab9-306c-83e0-e1f69018d2a9 | -9.2472 | -43.4897 | 2024-10-04 00:43:30 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 19dc7b23-a87a-3fa5-9ce2-4f544593a3d9 | -9.2493 | -43.498299 | 2024-10-04 00:43:30 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20ca932f-3616-3056-a640-a0952d73c9d9 | -9.2513 | -43.506802 | 2024-10-04 00:43:30 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| acd8ec56-09a1-3d5a-8e55-0f625e42d4bc | -9.1557 | -43.1493 | 2024-10-04 00:43:30 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 991ad891-e1c3-33fa-8c35-f8ab38a846d2 | -9.1578 | -43.158199 | 2024-10-04 00:43:30 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6673f13-878d-357e-9e7e-81505e5f120c | -10.2294 | -47.7355 | 2024-10-04 00:43:30 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2f7716a-aa7e-3a7b-90b2-1ce932061514 | -10.218 | -47.730701 | 2024-10-04 00:43:30 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2c71c28-b5b4-302d-a2d7-8a6818dfa7e1 | -10.2196 | -47.737701 | 2024-10-04 00:43:30 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1dbe3da6-6c1f-3cfd-bf5a-925469170e17 | -9.1437 | -43.1427 | 2024-10-04 00:43:31 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50a6f2fd-4810-3dd4-8572-fa0eb3965988 | -9.1459 | -43.151699 | 2024-10-04 00:43:31 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1cd64320-4b00-3f52-958f-e0c8dff999bb | -9.148 | -43.160599 | 2024-10-04 00:43:31 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e4e2b33-8f93-34c8-8a16-06f6d7d48f4b | -9.1501 | -43.169601 | 2024-10-04 00:43:31 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44dd60b1-217d-3048-bfb2-cea8e5e119fa | -10.5172 | -49.125198 | 2024-10-04 00:43:31 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1e5c8b5-b2ca-3a59-91d8-ee1da1f1cb0e | -10.5189 | -49.132999 | 2024-10-04 00:43:31 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce89877f-971b-3f9a-afbe-d0fb4cc747eb | -9.8314 | -46.749298 | 2024-10-04 00:43:33 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5338f738-e53b-3054-85d4-cb64d7ee2134 | -9.833 | -46.756199 | 2024-10-04 00:43:33 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1874aff3-9c2a-336b-89c7-0d7a866cb6ac | -9.8345 | -46.7631 | 2024-10-04 00:43:33 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 853bb2a8-3f83-340b-96ef-e9331d9395d5 | -9.8361 | -46.77 | 2024-10-04 00:43:33 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40bf4fd4-2db7-3a7c-afd4-1b6888b5bfbf | -9.8377 | -46.777 | 2024-10-04 00:43:33 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5de1fdf-67b4-3bcc-bb8f-06993fd442f4 | -9.8393 | -46.783901 | 2024-10-04 00:43:33 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b84e302a-7187-3d16-80b8-34f3b5dff4ac | -9.8408 | -46.790798 | 2024-10-04 00:43:33 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 983c2722-ea9f-3896-9763-7216a7b5e7b1 | -9.82 | -46.744598 | 2024-10-04 00:43:33 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ac406f7-d20b-343f-968d-bb9e4664fb9a | -9.8216 | -46.751499 | 2024-10-04 00:43:33 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b385ed4f-7039-3bb7-bf6a-240ed8e6d614 | -11.0335 | -52.499802 | 2024-10-04 00:43:34 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
