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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef61eef3-a3d1-30a7-8b20-2e3437e76fb5 | 1.50711 | -59.90956 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f74cf900-6427-3e12-a8fb-d3abe73238c5 | 1.14924 | -60.88518 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f8535d1-6541-392f-a64c-ad492a892fa3 | 0.49577 | -60.4994 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8d450f3-aab2-319a-bc43-00370bab6d5e | 0.06041 | -60.97738 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a86ae158-a9a7-356b-a2f5-3f43c4825b42 | 0.73135 | -59.91054 | 2026-03-04 05:01:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a36496d5-7fa9-3721-9101-378c1694c4d6 | -0.61661 | -50.82161 | 2026-03-04 05:01:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 593221c6-1749-3b4a-b972-e3f4c4352dc0 | 2.91438 | -60.43548 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0555cf0-897d-30f7-9e65-c0d18cf95c72 | 1.11215 | -59.20581 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89d42e3f-c733-3eb5-8cd0-995c8265b04f | 3.06169 | -60.71647 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b8427c7-ba3c-3c4b-8aed-aab0c7fccd99 | 1.50235 | -59.91052 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8a06575-c03d-3e5d-b49a-f5eb388699be | 2.64636 | -60.4444 | 2026-03-04 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 363df5ff-ecba-357d-b657-03d68f76eac2 | 4.04786 | -59.86082 | 2026-03-04 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6b144d0-56bb-372c-bf45-e34555b36f8b | 0.0517 | -60.98767 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.7 |
| fe8faf86-deb8-3195-ba2b-d7f220f7af9d | 3.05691 | -60.64442 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3dfa5571-3d0f-3b0d-86a6-10b5f11e9f43 | 0.27922 | -60.61673 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45d57e8c-b695-39d0-b7c1-d6c9cc5af4f6 | 1.06321 | -59.48652 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 430e00bb-32b5-3728-8a7f-c6a62082a23d | 0.46022 | -60.39948 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d502357c-c3fb-35f2-8225-967aa8514829 | 2.91129 | -60.43689 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08e994c0-44c8-3eb3-84b3-e58d1832f7f2 | 0.28007 | -60.62224 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9313919-59cd-36a7-bb81-6f0ee785bcde | 1.50398 | -59.92099 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e1d7ae73-d174-395c-9107-9ad25b5b7328 | 1.51268 | -59.91379 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d1f3fdc6-bf08-35fe-b424-ec56232d3816 | 3.06641 | -60.71259 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f8fd707-1b2e-39ea-ae8b-bc7c176b2170 | 0.45939 | -60.39409 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 60522ea3-dcea-351c-95de-f9616084e703 | 3.03998 | -60.64405 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 400b030d-ef33-3b7d-bc7c-4eb17a4fb8da | 0.0398 | -60.97778 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f0eaf37-66b8-33f4-9080-834639e082d7 | 2.92051 | -60.4628 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0656eac2-aca7-302f-adfe-2944a14d603a | 0.49662 | -60.50486 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf4cf131-5983-3d2c-ac36-7a9e6b2acbc2 | 2.22737 | -60.74751 | 2026-03-04 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 741a289d-9b5b-3d51-9bf4-8614c947c626 | 1.031 | -59.46249 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 43742c9b-6b98-35ee-8471-9104a1ba8b32 | 0.48852 | -60.51754 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ba4f782-0f91-3832-8399-d26a7a71673b | 0.65269 | -60.00262 | 2026-03-04 05:01:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54e89002-aab0-3e31-9a68-e8657422646a | 0.04575 | -60.98278 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3f288008-f1ac-3594-9a26-9ec6e250c195 | 0.0549 | -60.97523 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f47eabe-06dd-325b-b776-719f7fcdc64e | 1.01391 | -59.5041 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c2420f5-f520-340e-b0f1-e199506c969b | 0.04164 | -60.98951 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3ab6abc8-2823-32f5-b2cd-5d4697cb29ff | 1.08233 | -59.25262 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 310dacb2-3aff-3755-85dc-5bf6aaca4079 | 2.92849 | -60.46068 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8470df2e-2eba-3a0a-9a04-05147a209b0c | 2.67268 | -60.41341 | 2026-03-04 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30bde494-593a-3087-bf77-860001823b5b | -4.70363 | -55.96061 | 2026-03-04 05:03:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21875d31-9d10-3845-b660-4b13a72d7f0e | -0.50349 | -64.61032 | 2026-03-04 05:03:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc6fc36c-1a41-3285-af4c-4f7df28546a7 | -3.06153 | -52.87551 | 2026-03-04 05:03:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 319e6583-abb4-3abb-bcdd-877eec5ef000 | -15.42686 | -52.19364 | 2026-03-04 05:05:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 709be27b-de83-343d-bbe0-d601936db3f1 | -15.42621 | -52.19841 | 2026-03-04 05:05:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ceecb7c-650c-33f4-8a22-8f7cf64551b8 | -15.4273 | -52.19668 | 2026-03-04 05:05:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e7d0e19-1990-367c-9769-dc0687cb0501 | -15.4235 | -52.19613 | 2026-03-04 05:05:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 078b306d-2420-325a-ac7e-fe92e8db3003 | -18.80468 | -51.60639 | 2026-03-04 05:08:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79f62d8f-d78d-3bcd-a1fa-736536a632a7 | -20.30303 | -49.58529 | 2026-03-04 05:08:00 | NPP-375D | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 159b67f4-c072-3071-a4a9-ec2072ef5b86 | -20.81977 | -48.28115 | 2026-03-04 05:08:00 | NPP-375D | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edc7be20-4c49-3d97-943e-5a7d2fd51354 | -20.81933 | -48.2807 | 2026-03-04 05:08:00 | NPP-375D | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22f3e6c7-d9e2-3047-a8d5-682211ad9b25 | -16.44046 | -52.47738 | 2026-03-04 05:08:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98464c4d-cb6e-353b-be62-9c563b4e4531 | -20.8194 | -48.28461 | 2026-03-04 05:08:00 | NPP-375D | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e93acf36-d162-349b-8acb-faf9c4912930 | -16.58815 | -58.21756 | 2026-03-04 05:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 72667273-ba70-3ec2-8fcd-d823910d539e | -18.80879 | -51.60706 | 2026-03-04 05:08:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c4df585-a487-3d16-94f3-6085d3886d21 | -21.70286 | -48.43636 | 2026-03-04 05:08:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02fdb0cd-fa41-3ae8-9195-aed20d63f1a1 | -18.80829 | -51.61091 | 2026-03-04 05:08:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 678f4b21-9d11-30b0-8127-1284093c581f | -21.7032 | -48.43301 | 2026-03-04 05:08:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 801ac201-b34c-3852-af4d-0eabc3dd9deb | -20.92203 | -50.52718 | 2026-03-04 05:08:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed08273a-c266-3304-b2fa-0dad67ce06f6 | -21.60545 | -56.62649 | 2026-03-04 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58c469c4-6844-3047-8921-98a587059bd0 | -20.81898 | -48.28417 | 2026-03-04 05:08:00 | NPP-375D | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9e50ceb-2d85-32c6-a71a-7e020224f7bf | -16.58302 | -57.80544 | 2026-03-04 05:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fe873aae-ee05-3f0a-a8c2-459364310728 | -16.58475 | -58.21697 | 2026-03-04 05:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 32844c85-9ec7-3f4b-8601-3ad0fcbae50d | -21.69757 | -48.43592 | 2026-03-04 05:08:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f246cbf1-6970-3b29-ace2-6a840e6bb810 | -22.6267 | -54.95116 | 2026-03-04 05:08:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1d9b6093-912c-360f-8ea4-dfa59d74ee3f | -22.91194 | -48.61194 | 2026-03-04 05:08:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b57af8b5-0c1a-36e1-a0ab-67c5c2e10e01 | -20.91691 | -50.53155 | 2026-03-04 05:08:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e53ed7fc-816d-35e8-9121-ec238ebe4b75 | -15.77317 | -59.67713 | 2026-03-04 05:08:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4b9542c-ee92-3fae-95d1-9c4e59b6f50e | -15.77287 | -59.67975 | 2026-03-04 05:08:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4679dff1-ca94-345c-89aa-cf009fb774a3 | -18.8134 | -51.60387 | 2026-03-04 05:08:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f962e96-ad06-39eb-81d8-0c595985caa3 | -16.58412 | -58.22075 | 2026-03-04 05:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f3b40aa5-d9c2-305e-8b68-09923c5fdc07 | -21.70333 | -56.32029 | 2026-03-04 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7307529e-26df-3b7c-a89e-1cd31ab858a2 | -18.80929 | -51.6032 | 2026-03-04 05:08:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 607636dd-601f-33cb-8698-4e227472547a | -21.70672 | -56.32088 | 2026-03-04 05:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eea5ae7-b70b-3db0-a0a0-1257b503e863 | -22.58243 | -54.97996 | 2026-03-04 05:08:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b585174d-f5b9-3c1a-9d26-25257d7fb08b | -22.78411 | -55.39569 | 2026-03-04 05:08:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c770b6d7-0cd0-3ddf-ba8d-62fa95f27dc4 | -22.91229 | -48.60846 | 2026-03-04 05:08:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 13012d58-f66f-334e-b797-12981067af7c | 0.0455 | -60.961 | 2026-03-04 05:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a6e06bf7-1ca8-362e-9d04-e5fbaee60ac4 | 0.0273 | -60.9988 | 2026-03-04 05:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 75df6824-4242-33a2-88d0-087b2c010ba2 | 1.5047 | -59.9116 | 2026-03-04 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9a7ac7c6-5d32-347c-8e1f-41c255a37d34 | 0.0455 | -60.9799 | 2026-03-04 05:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 372.0 |
| 919ede8e-1397-391f-9606-42ac24f7a537 | 0.0638 | -60.9799 | 2026-03-04 05:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f0787ee2-a39a-3406-8578-8678b5509e7d | 0.0273 | -60.9799 | 2026-03-04 05:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0e03cc4a-b958-37ed-9dba-b503d213c2af | 0.0455 | -60.9988 | 2026-03-04 05:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 231.7 |
| a798c709-e988-3823-b054-e76d0c60e6f7 | -30.2452 | -50.2442 | 2026-03-04 05:10:00 | NPP-375D | BALNEÁRIO PINHAL | RIO GRANDE DO SUL | Brasil | 4301636 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| d99688e9-9310-3d3c-bc8c-784321ab82d9 | -30.25014 | -50.24596 | 2026-03-04 05:10:00 | NPP-375D | BALNEÁRIO PINHAL | RIO GRANDE DO SUL | Brasil | 4301636 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| d04238b2-0bce-3bdc-b6c7-aa96dcf097df | -29.79792 | -51.51156 | 2026-03-04 05:10:00 | NPP-375D | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| ba2fadbc-6a2b-3e40-9347-e88c21573487 | -30.24494 | -50.2454 | 2026-03-04 05:10:00 | NPP-375D | BALNEÁRIO PINHAL | RIO GRANDE DO SUL | Brasil | 4301636 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 815d59d3-d279-3f6e-be37-52b6bc282078 | -30.25041 | -50.24477 | 2026-03-04 05:10:00 | NPP-375D | BALNEÁRIO PINHAL | RIO GRANDE DO SUL | Brasil | 4301636 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 16461c65-3475-34bf-874a-120a790b0dc0 | -25.21897 | -53.28593 | 2026-03-04 05:10:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 61aabbd4-5751-3485-870a-38ecd8ba1669 | -25.00097 | -49.29942 | 2026-03-04 05:10:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e80db8f7-da92-32cd-9fad-120ebf98f03c | -25.09776 | -49.16377 | 2026-03-04 05:10:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f56ac9e6-5cb8-39a0-90df-d115b99e1c65 | -26.99311 | -50.59103 | 2026-03-04 05:10:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ad265d6e-c653-3270-9168-933ee6bed0aa | -25.00615 | -49.30019 | 2026-03-04 05:10:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6ec86ebc-bcbe-348f-a9ed-b156768c4d91 | -25.00582 | -49.30363 | 2026-03-04 05:10:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e8b24b2b-10fc-3a57-8194-f353dec682ca | -25.09805 | -49.16063 | 2026-03-04 05:10:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd87b579-7cda-34ff-9449-a5b4deea8385 | -25.00067 | -49.30265 | 2026-03-04 05:10:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f30996dd-77b7-38ff-a3ee-926ea6862825 | 0.0455 | -60.9988 | 2026-03-04 05:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 4b2ae3d8-fcf0-31d2-96da-d16a3d414953 | 0.0455 | -60.961 | 2026-03-04 05:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 238bf63d-ce82-35f1-b7a9-d4744be3db28 | 1.5047 | -59.9116 | 2026-03-04 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 1fa598f7-e9f4-3c24-8a78-9af73f4c0f6a | 0.0273 | -60.9799 | 2026-03-04 05:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0e86ce21-6665-3dca-901a-4e50c55429f9 | 0.0455 | -60.9799 | 2026-03-04 05:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 357.5 |


[Clique aqui para ver as próximas entradas](README7.md)
