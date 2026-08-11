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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2598d4b4-1884-3b11-ab78-7308c29e07f1 | -14.00231 | -53.98255 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60d131d0-5488-3855-8e81-e42f15eb7b8d | -17.03481 | -45.89635 | 2026-08-11 05:12:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9743a40c-8841-36d6-abc9-45ff3e525d1d | -15.0221 | -46.59185 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a71f1edd-a168-3462-9424-557a30452e20 | -14.62924 | -47.65826 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4bb4c58-ba80-3cb0-b2ef-eeeb0b4f546a | -14.62375 | -47.66069 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bfad88d-9cc4-375a-a600-f1b19fd1b5fe | -14.62601 | -47.66099 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 150d3bf3-9c06-3323-943a-934aba6fe7ea | -13.87539 | -53.78941 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9664de59-ec7f-3265-bef2-a52b534865ee | -15.06084 | -52.70013 | 2026-08-11 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2d9a583-2995-3d18-9924-88bbf43311f6 | -15.00594 | -46.58656 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 941ca506-4c2d-3bff-9778-5678f5e50f62 | -15.05651 | -52.70406 | 2026-08-11 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7c3e889-acef-34e2-9306-fc6e1113ab08 | -14.61867 | -47.65983 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88b0fa05-63ed-3cc3-b8f6-b24610521268 | -15.01027 | -46.59756 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d51f99a6-ae45-3509-8910-7cf065aeba8e | -15.02798 | -46.58933 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bf54f0e-a604-3ba4-aa40-bf65aa9716ad | -14.12212 | -45.63339 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f0c2a3c-3afa-32b8-a282-0625c5a8f55b | -13.8644 | -53.76768 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c776df4-2a6d-3572-a465-f358fa05b4a7 | -13.63759 | -57.93019 | 2026-08-11 05:12:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 849cb493-7796-34d9-9ae1-18f921033df7 | -14.4461 | -45.67646 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f323c9d7-303e-3f5b-8dcc-1a07dddbb4d9 | -14.12103 | -45.63988 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 886ff5db-734f-370e-be98-f9a11cfa0786 | -18.39555 | -55.54907 | 2026-08-11 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7cbd47d3-0ce7-39fc-a12b-95290ad7993b | -16.66304 | -43.63502 | 2026-08-11 05:12:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| edbf68e7-ad54-3d20-9677-34259f8e0845 | -14.99914 | -46.59716 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c87796d-f39a-332f-b4cc-9844ff536cf5 | -13.86788 | -53.76821 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf2731c1-8700-349d-a5d7-7a534b253941 | -16.667 | -43.63612 | 2026-08-11 05:12:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad10db0e-b3ec-3b68-a152-88397723a6d3 | -15.01902 | -46.57013 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 433e8646-b011-305d-97f0-89a2c5d0e8c2 | -15.01619 | -46.59465 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ea8d24e-7c2b-3dbb-9240-4dee3b1254e5 | -15.02177 | -46.59465 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2887709-1254-3c5d-87a5-60771a551ce8 | -13.86666 | -53.80021 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99159c06-08e6-32b2-bf5a-4de3629a837e | -15.05589 | -52.70848 | 2026-08-11 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4907857b-73f8-32d1-8265-fe44e810e536 | -13.73811 | -53.86845 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17b7657b-cef7-370b-99bc-da6b65d44202 | -16.48267 | -54.65925 | 2026-08-11 05:12:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a196d6a7-a069-35b5-9501-0abe68ee227d | -14.27279 | -45.3026 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5819203c-0d38-3c1a-afe9-5bc942c6c35e | -13.43405 | -57.04437 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c27f8d09-e428-351b-94f1-e520d51d6c49 | -14.10403 | -54.02614 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e587976-048b-3862-95c0-ea4cd94daace | -17.99866 | -44.37861 | 2026-08-11 05:12:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7e0c4b5b-d8f3-3dc2-8e88-7b3f85971614 | -14.00634 | -53.97923 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4eb34ae-0ef1-317f-bb8c-b58dbf32bc57 | -14.12933 | -53.99865 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97ccabf1-8cd5-3df4-b030-2be1a5e7667d | -14.49775 | -49.29092 | 2026-08-11 05:12:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a144e755-2b3b-37a8-91d5-defb48c91ef0 | -14.37503 | -53.33275 | 2026-08-11 05:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 927ccc21-24be-38ed-981b-ea8bfb4945bc | -15.01261 | -46.57716 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0070f8f2-77b9-3f3d-b28a-1c13758d6a1d | -18.42211 | -45.49651 | 2026-08-11 05:12:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 201ab72a-d1c5-3f1c-8ffb-fc60e62d546b | -14.46175 | -45.68897 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 455c17d2-0d1f-3418-8316-2c3b30a7ff2e | -15.06021 | -52.70464 | 2026-08-11 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52317b60-ec23-3083-b700-2656c88593ca | -14.4774 | -47.97842 | 2026-08-11 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2d29248-6c26-3ed0-a831-06398c409043 | -15.0196 | -46.56504 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c964574-223e-3af3-b86f-bbd89882890c | -15.77468 | -46.78925 | 2026-08-11 05:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbeaa23e-740e-3320-95f8-5ad563afd70a | -14.12745 | -45.63829 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b34354fd-2720-3a8b-b1b9-3d5e2e559fee | -14.48167 | -47.98503 | 2026-08-11 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4a211eef-a5d0-38ca-a024-5486feee5946 | -14.27924 | -45.29892 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecaad55f-f9f4-3ba6-8d7d-3ffdb8bb47ca | -18.02965 | -44.40019 | 2026-08-11 05:12:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5018b18d-689a-3004-b495-a7e621874763 | -16.65626 | -43.63465 | 2026-08-11 05:12:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62d21c6d-3223-34d7-9e67-ede00e6152db | -14.27821 | -45.30769 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e2a1321-f969-339d-b3dc-4c7c3acb55db | -18.01296 | -44.36724 | 2026-08-11 05:12:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acea6995-5fb6-300f-a2d7-40ef87668fe8 | -18.02906 | -44.40637 | 2026-08-11 05:12:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| be030b10-8092-30c2-b233-4e5f79d7497d | -13.43011 | -57.04743 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66aa18ec-af89-34d2-99f7-8f99809436fe | -15.03394 | -46.58614 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a49b1505-2521-3028-8da3-32ef3d65e9ab | -13.63822 | -57.92639 | 2026-08-11 05:12:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2facf202-af45-3986-baad-efc3da2d71db | -15.72057 | -56.2091 | 2026-08-11 05:12:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c814cc74-3e58-39cf-94b9-2c1606b6cad5 | -17.04242 | -45.89765 | 2026-08-11 05:12:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c913645-34b6-30b0-bb57-3066c1ba926b | -14.44561 | -45.68064 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ea55417-e1f7-3494-80fd-b216b9a090d3 | -15.01061 | -46.59459 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50a9a801-5db0-3ee3-a423-854cc1c59da3 | -14.76171 | -56.36935 | 2026-08-11 05:12:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df67c9d5-860a-325e-b342-0f14c178755c | -14.45191 | -45.67716 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc1d4701-3c4d-3a8d-8f34-f9da388ea052 | -17.13304 | -51.68318 | 2026-08-11 05:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ead1b90d-73e7-3286-9b4c-a2039909401a | -14.31177 | -54.91409 | 2026-08-11 05:12:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00a025d9-26c4-306c-a87a-4cc1b2e8d23a | -13.59579 | -55.21658 | 2026-08-11 05:12:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 53ad84f1-4650-3045-adf4-dc11e5542b83 | -14.46082 | -45.69733 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87366f83-31a8-3c2b-9fd6-d936055c346a | -14.127 | -45.64229 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ce7fb5f6-dcb3-3329-96a5-fc5d3363bbd1 | -18.02567 | -44.43789 | 2026-08-11 05:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b381b1f6-e460-316c-b51f-80d5a026b064 | -14.28101 | -45.30785 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f627086-6ab3-34b9-b02f-9345d2408de7 | -14.25831 | -51.96049 | 2026-08-11 05:12:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a89a07b-d41a-3936-ae4e-c4d14df9b097 | -14.12123 | -45.64143 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca9b9bd5-46b5-3951-9b67-2d3bcc288fbd | -14.75838 | -56.36879 | 2026-08-11 05:12:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d2df05c-16c4-33fd-80c1-31ca80e7126b | -15.76872 | -46.79267 | 2026-08-11 05:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e2c33048-fe5d-396d-91d1-dceba618ff64 | -14.45062 | -45.68336 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80cd609d-980b-305f-b16a-9c4b69643e89 | -14.50161 | -49.29692 | 2026-08-11 05:12:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2c8235f-629d-3444-9910-8b4e48330d56 | -16.2818 | -56.60087 | 2026-08-11 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7a8b3a67-2d4d-31e9-8e1b-938953307bd3 | -14.62093 | -47.66013 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ada7a904-a2c3-301f-90be-0511ebf92b4f | -14.46755 | -45.6897 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ada344aa-4314-3b24-859b-ee96eca797e6 | -14.62883 | -47.66152 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9039301f-0b91-3364-96aa-f641d154c72f | -14.12198 | -45.63187 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a369352-d3e3-3f93-ae5f-a95ab6a4b762 | -14.12728 | -45.63672 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 90a93331-25e8-34a8-9fea-617b55e02a7d | -14.47241 | -45.69875 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4d2d4cd-aa54-37e2-ab20-c185c8ec762b | -15.00469 | -46.59753 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2cf1505-43aa-3c96-b3e4-d333f7214a98 | -14.28004 | -45.31662 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2790c716-6c17-3c4b-ac6e-db9f0fa58324 | -15.87572 | -56.25674 | 2026-08-11 05:12:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9c0f854-3b30-3abf-bece-d5f74f2ae785 | -16.49013 | -54.65649 | 2026-08-11 05:12:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 889f6608-062d-3e61-8645-115074eaa0b4 | -14.27769 | -45.31206 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 013dda5b-8d86-340e-9599-407dfc588e50 | -14.6264 | -47.65771 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f0890db-2546-3b6a-b318-76bfffd88c95 | -14.45155 | -45.67501 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27a5a877-32c2-3771-ac4c-a5217583586d | -14.45502 | -45.69663 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02c3567e-b67b-37cf-8c76-dc78902ec633 | -15.00436 | -46.60036 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f0c1888-d7d6-3fc6-b742-7fd979c0ad2b | -15.06887 | -52.69683 | 2026-08-11 05:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81b682da-a733-31d3-a77d-e4dd7c2e8f92 | -14.45689 | -45.67991 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d28b5878-4f81-3d79-9855-88f2799da68c | -14.3112 | -54.91777 | 2026-08-11 05:12:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4f7b759-3c63-34b8-9f73-a3c5406d1212 | -14.44528 | -45.67846 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a40390c-b77a-34f3-ae6b-194501072ffb | -14.45549 | -45.69245 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 302e2627-f8ad-37b4-ac3a-5252a2a417ae | -17.04195 | -45.90193 | 2026-08-11 05:12:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39d3d758-5797-326b-bc70-d45f1df6b93a | -13.8748 | -53.79337 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db521f03-5305-3379-a535-efcba270ab6a | -16.66247 | -43.64116 | 2026-08-11 05:12:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5c754ddd-de55-3bae-afaf-fa3950dabdc9 | -14.25763 | -51.96531 | 2026-08-11 05:12:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README26.md)
