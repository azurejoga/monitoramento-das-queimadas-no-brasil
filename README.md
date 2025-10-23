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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cb85d50-bfd3-3866-8d9e-83bbdc0319b1 | -11.3646 | -49.7779 | 2025-10-23 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 2e546df8-40a3-36ae-a532-da45860acc1c | -8.6234 | -41.4081 | 2025-10-23 00:00:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| e35e384f-5625-3155-a886-8d465d15603c | -1.7868 | -54.8516 | 2025-10-23 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d3572783-fcd7-3f1c-9f37-e8044f7a4060 | -3.0354 | -49.4688 | 2025-10-23 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| b6152668-6f6b-311c-92d3-b6595ce90aa5 | -5.6933 | -45.9667 | 2025-10-23 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 43abd723-a5f6-3c98-a320-5c9862f7c3e0 | -10.5249 | -50.2137 | 2025-10-23 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 313472e1-bbb1-373c-ba74-10924e7cbc2b | -11.3453 | -49.8017 | 2025-10-23 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 59eb10d9-238a-389a-9e75-0f8096dd0a62 | -10.3406 | -62.8401 | 2025-10-23 00:00:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 3d8df560-a388-3b82-bdcb-f3e46f27375a | -3.0353 | -49.4901 | 2025-10-23 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| f55834bb-d349-3af7-bb2b-579e9011d7e2 | -3.4762 | -50.0883 | 2025-10-23 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9303b14e-5338-303e-8ef7-8e65059ef745 | -11.3643 | -49.7995 | 2025-10-23 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 257f284b-f79b-3fde-a4d6-64c22ef01f41 | -13.7451 | -44.3268 | 2025-10-23 00:00:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 6b554da3-7d2d-3d8a-95b2-4da18de77e6c | -3.4763 | -50.0673 | 2025-10-23 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 107c4643-f858-3e84-b5c4-ac10db1e2f86 | -3.0168 | -49.4906 | 2025-10-23 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| ce9cb4c9-e456-3745-b740-67f609778d68 | -11.3456 | -49.7801 | 2025-10-23 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| a90f7655-b7b3-34b5-b4e5-bf9157fe14a3 | -10.5246 | -50.2351 | 2025-10-23 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7dfcfac2-e99d-3caf-8717-004f9e9be4d3 | -12.1212 | -62.9591 | 2025-10-23 00:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| c33df667-3d40-3763-9ae6-8f855a0316b1 | -3.0169 | -49.4694 | 2025-10-23 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 8d4c443f-dea1-3cd3-991a-6aeb033c3816 | -3.0353 | -49.4901 | 2025-10-23 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 16d39e7a-ef02-31ef-9405-27831f1d980a | -5.6933 | -45.9667 | 2025-10-23 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 5f67c07a-6379-3084-b754-15827bacdb06 | -3.0354 | -49.4688 | 2025-10-23 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 209d246e-5268-33a7-8dd4-86d0aafa2b93 | -10.4648 | -49.0789 | 2025-10-23 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 64c26276-1fa4-3839-9b0e-3b943298dec5 | -1.7868 | -54.8516 | 2025-10-23 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d294e748-1c0e-336a-8ba1-10d464b789c6 | -11.3646 | -49.7779 | 2025-10-23 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b1328544-81f0-3d87-be27-cde2d6cad16b | -3.0168 | -49.4906 | 2025-10-23 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 2e045896-fe25-37a6-8603-b46088e81ae2 | -10.4645 | -49.1006 | 2025-10-23 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 0c1d4142-c07e-37b4-83e6-ce2574a88158 | -3.0169 | -49.4694 | 2025-10-23 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| d4e40279-2979-3fc0-b60d-78dd5b893867 | -8.6234 | -41.4081 | 2025-10-23 00:10:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| af0ad8fb-91af-30fb-9826-ea552aba48c4 | -10.4834 | -49.0986 | 2025-10-23 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9072cee6-0b59-364a-9db1-ad186ade095a | -9.6879 | -35.8698 | 2025-10-23 00:10:00 | GOES-19 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| 63d9f3bc-9b22-3715-ac1f-cb7804515341 | -11.3643 | -49.7995 | 2025-10-23 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5512142b-b999-398b-9739-9ae24bbc36d2 | -13.7451 | -44.3268 | 2025-10-23 00:10:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| d0e59a77-0eba-33a6-9b6c-abfe36a49d02 | -3.0169 | -49.4694 | 2025-10-23 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 28b71950-8755-3844-b021-11b8cf1aadf0 | -11.3453 | -49.8017 | 2025-10-23 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| cd8b06ce-a1ce-341f-9b9b-67c0f68f2a35 | -11.3456 | -49.7801 | 2025-10-23 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 5d81e1cd-5eae-3d75-ab9c-c3069a6975a1 | -2.8155 | -54.3736 | 2025-10-23 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| aae645e8-4ab1-3534-876a-1ef28105f9ea | -11.3643 | -49.7995 | 2025-10-23 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 44b2da02-2956-3aec-a1ac-876f43360b89 | -3.4763 | -50.0673 | 2025-10-23 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d62ed6e6-0c15-3694-8e7c-c5fffc69dcef | -12.0032 | -46.7892 | 2025-10-23 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ddf123b5-415b-36ee-b4c3-1f1bd88d5f62 | -12.0036 | -46.7667 | 2025-10-23 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 564a0814-79f9-3f13-bf32-51fa82464de4 | -10.4834 | -49.0986 | 2025-10-23 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 09b1ea24-8b55-3605-b7fe-4748669b8511 | -10.4645 | -49.1006 | 2025-10-23 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b6dc946d-3055-3d3a-ac11-6381bec3766d | -11.3646 | -49.7779 | 2025-10-23 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 0077105b-4562-3253-bcd2-c529fe3e84f0 | -3.0354 | -49.4688 | 2025-10-23 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6e164102-03b7-3040-8b4f-6bcb1463c27a | -3.0168 | -49.4906 | 2025-10-23 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 54daed64-982b-32f4-9f05-d02a229174fd | -10.4648 | -49.0789 | 2025-10-23 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| e8fd6a1b-c1a0-3bc3-88c4-cb341dd2b074 | -5.6933 | -45.9667 | 2025-10-23 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b4a30cd0-4826-35db-a6fe-aa59e896dc42 | -8.6234 | -41.4081 | 2025-10-23 00:20:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| fb0159d0-04c7-3c61-be7b-33746aa9f531 | -13.7451 | -44.3268 | 2025-10-23 00:20:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 24b59236-160c-3cf8-b99c-ac6a2a1614b7 | -10.5441 | -50.1903 | 2025-10-23 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| a093ebfb-b457-35c3-863b-64dc33185899 | -11.3646 | -49.7779 | 2025-10-23 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 9b1c76bb-2f9f-36fa-87eb-1a547a930827 | -10.5252 | -50.1923 | 2025-10-23 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d44acae5-bae7-3532-89c2-05e45087faf1 | -10.5246 | -50.2351 | 2025-10-23 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 325e8e95-f3f9-3aa0-a029-906d652f587e | -13.7451 | -44.3268 | 2025-10-23 00:30:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b6dfdbba-dbc7-3975-a2b9-743ef0d94944 | -11.3643 | -49.7995 | 2025-10-23 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 01028090-564a-38a4-8548-f5401cbe89fc | -3.0354 | -49.4688 | 2025-10-23 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| fe404fe6-296c-32d1-a806-1c66bc477076 | -11.3453 | -49.8017 | 2025-10-23 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ada2d9f4-bf76-3b9f-8f8a-b28c877ef39a | -10.5249 | -50.2137 | 2025-10-23 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| dada98ec-218c-329a-bcd5-2831b53e7b2e | -3.0168 | -49.4906 | 2025-10-23 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 93fe3d7c-cb6d-37b3-ab07-a60b105f19f6 | -3.0169 | -49.4694 | 2025-10-23 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 2850119f-dc28-362d-80f6-cffed1a2f85b | -6.0937 | -49.3897 | 2025-10-23 00:30:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| be2c14b1-8ca3-3e5b-be8a-e787d321f164 | -8.6234 | -41.4081 | 2025-10-23 00:30:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 2fbfd22e-6691-3ad1-8b7a-79e45bcc4cf3 | -5.6933 | -45.9667 | 2025-10-23 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c92124cc-abdf-337c-9e58-2f24405551b1 | -10.5438 | -50.2117 | 2025-10-23 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 2a159c4f-61db-3b4f-981e-d4dd67c3f073 | -2.8155 | -54.3736 | 2025-10-23 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 6a6e7cac-e46c-3b7b-b04f-2124fce410b2 | -3.0353 | -49.4901 | 2025-10-23 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 8722a8e7-fcee-34a8-a17d-97485466fedf | -11.3646 | -49.7779 | 2025-10-23 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ff1f7eee-823f-3c92-9139-32007f9a3338 | -11.3643 | -49.7995 | 2025-10-23 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| d327f73d-546b-3482-844f-4aae5f632f65 | -6.6079 | -44.2176 | 2025-10-23 00:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f77d25d4-7057-3c53-b152-53f199140bfd | -17.6167 | -46.614 | 2025-10-23 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b6080dca-e9ea-3b3b-8bcd-eb9a0824b453 | -6.0938 | -49.3683 | 2025-10-23 00:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| d5dc1b1a-2734-3bd2-ae6f-f568ddfa4759 | -13.7451 | -44.3268 | 2025-10-23 00:40:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3328ff2b-ab87-3746-8bce-3b939874a23e | -5.6933 | -45.9667 | 2025-10-23 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e0a64e9a-4fac-31da-9e23-f3dd35a2fcf4 | -6.5891 | -44.2192 | 2025-10-23 00:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2fa36096-c3c6-3f5b-8142-c4424fcc123d | -3.0169 | -49.4694 | 2025-10-23 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 169.0 |
| 8e26d747-5595-38c2-a701-b6dcdd119fa7 | -10.3406 | -62.8401 | 2025-10-23 00:40:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 366f5e8d-41d1-3d5c-be1d-05d86ce48a1a | -3.0353 | -49.4901 | 2025-10-23 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 786a14ed-32fb-34e7-8d1a-1987431a7cc9 | -2.8155 | -54.3736 | 2025-10-23 00:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b6e3ceb9-c72e-38ab-bea0-af7ee784d4d0 | -17.6173 | -46.5906 | 2025-10-23 00:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e04c6394-e0c5-3265-b183-5e43eed1d56b | -3.0354 | -49.4688 | 2025-10-23 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f83bbf68-8305-307a-80cc-4fcb16ed1280 | -6.0937 | -49.3897 | 2025-10-23 00:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 375635eb-4ba0-3059-986e-46f86d81f510 | -11.3453 | -49.8017 | 2025-10-23 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 8c0aebff-8134-3c3e-bce1-52ca6f91e590 | -3.0168 | -49.4906 | 2025-10-23 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| a7428388-c523-34a5-ab06-e9d0cfb9fbbe | -28.2309 | -50.34684 | 2025-10-23 00:48:00 | TERRA_M-M | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| f8519601-766f-312a-a2de-2c544fec72c5 | -28.23226 | -50.3569 | 2025-10-23 00:48:00 | TERRA_M-M | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| c595430b-ee0c-3271-83a8-419426523d10 | -32.86706 | -52.52651 | 2025-10-23 00:48:00 | TERRA_M-M | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 14.6 |
| 22b299fe-70ac-3f86-a5b0-736e48487022 | -32.85695 | -52.52807 | 2025-10-23 00:48:00 | TERRA_M-M | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 33.4 |
| a5506ceb-d773-34bb-b05c-8e1d9406560e | -11.3453 | -49.8017 | 2025-10-23 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f541b975-77e0-30d3-854e-1edfad6062bb | -3.0353 | -49.4901 | 2025-10-23 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| d55beffb-9989-3481-8217-f9c9e7a4b399 | -2.8155 | -54.3736 | 2025-10-23 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c1dc5bfa-3a98-3573-b819-876de06a3761 | -11.3646 | -49.7779 | 2025-10-23 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| bfed3a57-de5d-3a33-b5ea-ecaca5787798 | -6.6079 | -44.2176 | 2025-10-23 00:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f4990bec-acc2-3857-b3b6-fdaa1c379db7 | -17.6173 | -46.5906 | 2025-10-23 00:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 72415cb8-5e87-3523-ba0a-15077b5ad048 | -3.0168 | -49.4906 | 2025-10-23 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 1da566f1-d37d-30f5-83ca-c12cd2d28fac | -3.0169 | -49.4694 | 2025-10-23 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 87d9a41e-d790-3a3f-a987-fe14de9cb06f | -3.0354 | -49.4688 | 2025-10-23 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 9e38738d-f2da-32d9-b66b-726e632b18f0 | -11.3643 | -49.7995 | 2025-10-23 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| d128d232-783f-33b5-8962-fb21d6ec2818 | -9.1174 | -65.359 | 2025-10-23 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 30bddf6c-cf59-3308-8c01-bfc497167bf6 | -10.3406 | -62.8401 | 2025-10-23 00:50:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ea6a402f-d10f-361d-9141-032010cb359e | -5.6933 | -45.9667 | 2025-10-23 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |


[Clique aqui para ver as próximas entradas](README2.md)
