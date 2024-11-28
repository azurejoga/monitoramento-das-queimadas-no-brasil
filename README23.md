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
| 007565ee-30ae-39b6-a926-ea96151569b6 | -3.1113 | -53.8242 | 2024-11-28 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b0e64130-6469-3024-8393-371975dfc115 | -6.1039 | -43.9824 | 2024-11-28 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| fdf7fb3a-00a4-3647-8314-9233b2a74412 | -1.6445 | -52.4543 | 2024-11-28 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 426fd273-f1d8-37b9-bff9-601f220fdece | -4.7722 | -44.4205 | 2024-11-28 02:00:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 688a54fc-152d-3f1a-9ed0-a31f54c4f65b | -6.1041 | -43.9593 | 2024-11-28 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 3d296b50-9d5c-34f0-98c9-a4c978b8741a | -1.3329 | -51.9257 | 2024-11-28 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| bbc72dbe-2608-309a-99f6-8866cf801362 | -6.0862 | -48.0339 | 2024-11-28 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 10478444-d813-3ca6-af3a-ba4564bc14cf | -3.9747 | -50.1962 | 2024-11-28 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| f25375c6-45ee-3a13-9de6-36cbb189ea2f | -6.1048 | -48.0327 | 2024-11-28 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 86c32a98-61e7-34f3-9d75-50d59ab3cb90 | 1.2537 | -55.9664 | 2024-11-28 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 56df66ce-30af-3815-a31a-4745f5036a1a | -2.5963 | -53.9771 | 2024-11-28 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1cc54159-4705-3f48-9828-4460b5792c6b | 0.9857 | -50.1224 | 2024-11-28 02:00:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 38478e3d-3955-3091-b185-e2601bdee040 | -1.6445 | -52.4747 | 2024-11-28 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 26c1551a-66d9-31c2-a16a-6925b34b8b4f | -5.9975 | -45.3607 | 2024-11-28 02:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| d3b8c79b-8ce2-36bf-9cf2-22381dc9624b | -2.9909 | -51.4598 | 2024-11-28 02:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| cf8c31fa-dbf5-333a-ad7e-277758410d55 | -3.4022 | -50.1119 | 2024-11-28 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 46a89c49-ed83-3cc9-9ff5-0b22760bf025 | -5.97 | -45.35 | 2024-11-28 02:00:00 | MSG-03 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5fde74a-492f-3411-a74c-0e9a9901e8d7 | -5.979 | -45.3395 | 2024-11-28 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 966d57b6-5234-32b6-bc89-48acc4d1e029 | -6.086 | -48.0557 | 2024-11-28 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| fb838b13-11da-3484-b4ea-51b69149555b | -9.1342 | -35.665 | 2024-11-28 02:10:00 | GOES-16 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| f4034231-8d83-356d-9a74-1af9de033c17 | -6.1048 | -48.0327 | 2024-11-28 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6da87071-5bfa-3b22-a8ad-08503c28c55b | -1.5897 | -52.271 | 2024-11-28 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| d0aba24c-2aa5-3f41-8060-d60f7a024f71 | -2.861 | -46.8406 | 2024-11-28 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 57c53a16-beaa-3052-8374-be7391e9eaa8 | -4.7722 | -44.4205 | 2024-11-28 02:10:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 79b2937c-1d48-3e8f-845f-5a4098f17ba7 | -5.9788 | -45.3621 | 2024-11-28 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 187.7 |
| ae86b7d7-5508-3871-9de1-c94f383cdbec | -6.0862 | -48.0339 | 2024-11-28 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d172a9d5-790d-3be4-a3bb-7d36b332deb5 | -3.1113 | -53.8242 | 2024-11-28 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| cffcd1ae-8d5c-3bc6-adf6-0582f6b081da | -1.5713 | -52.2713 | 2024-11-28 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 3c323b12-9f5e-370d-b680-2ab0215da8dd | -3.3837 | -50.1125 | 2024-11-28 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 991ad721-dfd5-3761-be9c-ad22e69261cb | -1.3145 | -51.9259 | 2024-11-28 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 7809f95b-c9a2-35a5-8295-f9b6b24e1ad3 | -5.9975 | -45.3607 | 2024-11-28 02:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| fdf8df93-a69e-390c-a1ee-99b609b76b33 | -1.5898 | -52.2505 | 2024-11-28 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6852b676-7a08-39de-9ef4-4de1dc478395 | -6.1041 | -43.9593 | 2024-11-28 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 7eaefcbd-1e70-353f-8438-5eb8c6f3ac1a | -2.8794 | -46.862 | 2024-11-28 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b59d2698-e1b7-33ed-ae55-69ca1bb21e10 | -1.3145 | -51.9465 | 2024-11-28 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 64a2a0db-070a-353f-a28d-4e1494fd0b6b | 1.2537 | -55.9467 | 2024-11-28 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 6046117d-55d2-341b-8eed-e5d3afbcec6d | -4.0899 | -46.1493 | 2024-11-28 02:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 9815cda4-24b4-36bb-b63f-34d2e71008d1 | -1.6445 | -52.4747 | 2024-11-28 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 79d33544-3286-3bea-a502-8b5584852b57 | 1.2355 | -55.9272 | 2024-11-28 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 2b176b1e-8340-3215-a956-f26326f61909 | 1.2537 | -55.9664 | 2024-11-28 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c6419be5-8fe2-33ba-9f83-7f2a73f730e3 | -1.6812 | -52.4946 | 2024-11-28 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| cb8b0ae9-2ecb-3739-94f5-cc63e13ef393 | -2.5963 | -53.9771 | 2024-11-28 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 412abf48-7a59-3736-9ed5-0bb792ed57f5 | 1.2538 | -55.927 | 2024-11-28 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 8f67e384-2309-3743-b5f6-ee8893caed9a | -1.6629 | -52.4744 | 2024-11-28 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 2808e04a-a878-3e90-96b6-07995560c8aa | -2.8609 | -46.8626 | 2024-11-28 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 73403d26-cc46-3843-822c-6139972e3f5c | -1.3329 | -51.9257 | 2024-11-28 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d8ff0465-6b50-35c6-9815-481a90135834 | -1.6812 | -52.4742 | 2024-11-28 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| bcf14538-660c-3b15-bfe6-5a1d953821c6 | -3.9674 | -48.0851 | 2024-11-28 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ed06c924-a321-3981-9d38-d13fe136e349 | -3.4022 | -50.1119 | 2024-11-28 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 0496879a-a348-38f7-bfce-c6d6180df3b3 | -1.3329 | -51.9463 | 2024-11-28 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| abf8648f-5938-3501-9439-e9b9badfbdaf | 1.2354 | -55.9469 | 2024-11-28 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 80054b93-d9e8-33a0-af75-ae35c6665526 | -2.8795 | -46.84 | 2024-11-28 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d99d6bd1-23a5-30d3-afc1-a2b9b049cb52 | -3.0929 | -53.8247 | 2024-11-28 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ce090fa0-2ab6-3fab-b8ad-1cce579f05ff | -5.9975 | -45.3607 | 2024-11-28 02:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f86fa2b6-fd7b-3e30-87cc-4dc62756bce7 | -2.8795 | -46.84 | 2024-11-28 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4a9a1d9a-d3a2-35ae-a295-210b1c3e9d26 | -1.5898 | -52.2505 | 2024-11-28 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d8562a16-87d1-32c3-8fc1-4d617efb2516 | -1.6812 | -52.4742 | 2024-11-28 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| e352b432-e4d6-3050-8e84-dd716d62aaf7 | -1.6445 | -52.4543 | 2024-11-28 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0c378fae-9065-3f35-97d8-be4d2042ea81 | -6.1041 | -43.9593 | 2024-11-28 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f5c8c8ab-4061-3c6f-8ca8-090bfecbad19 | -2.8609 | -46.8626 | 2024-11-28 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c66e81b9-9caa-3591-8b5f-73e699c52f63 | -6.1048 | -48.0327 | 2024-11-28 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5d937262-b73c-39e5-a483-9464333f1a44 | -1.6812 | -52.4946 | 2024-11-28 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a099086d-3e22-3e4c-91dc-bc5ba481aced | -3.093 | -53.8045 | 2024-11-28 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 31e67128-c7b8-35a4-be5f-46d25df082e2 | -1.3145 | -51.9259 | 2024-11-28 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| cb712415-f714-31aa-9d94-7d4ea5b0f953 | -5.979 | -45.3395 | 2024-11-28 02:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 5050acfe-8983-3ddf-9a79-d0c7083fe792 | -3.3838 | -50.0915 | 2024-11-28 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 60c650f9-4d61-3489-802a-4b3b33764640 | -4.7722 | -44.4205 | 2024-11-28 02:20:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b25c78b3-5b43-3c26-bdd6-1f79426d250f | 1.2355 | -55.9272 | 2024-11-28 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1d1c9a83-3106-3894-b6d9-1f994fe815e4 | 1.2537 | -55.9467 | 2024-11-28 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 36ad7a15-c62e-3c0c-b1af-e8c311ca4593 | -1.3329 | -51.9463 | 2024-11-28 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| f8d0b8df-f118-3d4a-aa9f-319d2aca2cd3 | -4.0899 | -46.1493 | 2024-11-28 02:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 91fa6882-2d08-3979-99cc-3358cf8f5efc | -1.6445 | -52.4747 | 2024-11-28 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f06000ed-e95a-318b-9e13-4ea347b801d9 | -3.1114 | -53.8041 | 2024-11-28 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c2cd79cb-e52a-3d07-a8dd-771151ac5dce | -6.0862 | -48.0339 | 2024-11-28 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| eff5a8d3-57ee-34dd-8287-dc7c25e1f3b5 | -3.3837 | -50.1125 | 2024-11-28 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| c329f96c-1553-3d5e-9655-c7fc305637ff | 1.2537 | -55.9664 | 2024-11-28 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 26340264-8710-3a1b-ad2c-9061e44f9908 | -2.8794 | -46.862 | 2024-11-28 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5e5906b5-f353-3b9f-b136-c5354b76f381 | -1.5713 | -52.2713 | 2024-11-28 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 515e3abe-9f77-35cb-96a0-1ef1cc6506fd | -6.086 | -48.0557 | 2024-11-28 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| bfdaed02-d50a-3655-9511-c1f1ddf7d89e | -1.5897 | -52.271 | 2024-11-28 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 0137d576-fac1-3ab0-90bc-312c28073a91 | 1.2538 | -55.927 | 2024-11-28 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 70e8f1c8-14d6-389e-9cb7-cd9e2155a45e | -1.3329 | -51.9257 | 2024-11-28 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 85568bfc-10e9-345f-9355-ae7566f1c184 | -2.5963 | -53.9771 | 2024-11-28 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| fc020266-6bb5-3809-9039-e6e80b53d386 | -2.861 | -46.8406 | 2024-11-28 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 89a9b940-ce5b-3458-843d-80d300a978f2 | -18.784 | -55.8416 | 2024-11-28 02:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.5 |
| 9035c7ed-0555-3b58-b49f-9c77b6256c24 | -3.1113 | -53.8242 | 2024-11-28 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 7dd6a01e-4e09-3cdf-91a1-653c2a3119ce | 1.2354 | -55.9469 | 2024-11-28 02:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 60b9fbfb-5332-3e4f-a3ab-cb35dc693665 | -5.9788 | -45.3621 | 2024-11-28 02:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 14ec452f-9051-3e39-9525-749706b535c9 | -1.6629 | -52.4744 | 2024-11-28 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ccb1e888-74dc-3215-b827-4b94809281b6 | -6.1041 | -43.9593 | 2024-11-28 02:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3a4cdc2c-0bd3-36f6-bb4c-a88e41078f2c | -6.1048 | -48.0327 | 2024-11-28 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 218a69db-7559-3bfa-b7b6-33905148ed6e | -18.784 | -55.8416 | 2024-11-28 02:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 8b9ce511-5d8e-37f6-8b1a-b641fc6b55d7 | -2.8794 | -46.862 | 2024-11-28 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d16f63ee-996a-3410-b684-22615a97896f | -5.9975 | -45.3607 | 2024-11-28 02:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5cf95842-22c9-3c1e-89eb-a34f944c8d22 | -1.5897 | -52.271 | 2024-11-28 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 6a3a0f09-325c-3ed0-85c2-30fd09c5d164 | -1.3329 | -51.9257 | 2024-11-28 02:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0e02db0d-0564-3006-bf10-4298c8d7dce7 | -1.6445 | -52.4543 | 2024-11-28 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ffbc4e0a-df6e-3643-9080-5b71c9190ef5 | -3.1113 | -53.8242 | 2024-11-28 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| caa60510-560a-3588-9727-d4dc0aa6d83a | -1.6445 | -52.4747 | 2024-11-28 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2e361efb-e9ea-3d7e-ae97-d52e45edacab | -1.6812 | -52.4946 | 2024-11-28 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |


[Clique aqui para ver as próximas entradas](README24.md)
