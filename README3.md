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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68d6f440-94a6-3d72-b612-fa957cd55fd5 | -9.0226 | -47.74558 | 2025-05-21 00:37:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7c6ad81e-f79d-3eed-9ebb-785ca6759034 | -7.08596 | -44.39168 | 2025-05-21 00:37:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1dc6b819-4586-3ced-a745-738b5f9340a1 | -6.20564 | -43.32515 | 2025-05-21 00:37:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d6188b83-0b46-3a57-b0d1-27aae928c47a | -5.57832 | -45.2104 | 2025-05-21 00:37:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fc0d9fb-8609-32b0-a986-a836378587fb | -11.0903 | -54.7648 | 2025-05-21 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 882b0c9f-fffd-34b8-9d0f-1167685cd3c6 | -11.0901 | -54.7852 | 2025-05-21 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 19c598ef-be02-3777-86e4-5a5c521b76ac | -12.424 | -43.7274 | 2025-05-21 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| daf0798d-128c-36f5-8c08-4c0d34a2cfc1 | -12.2943 | -52.4995 | 2025-05-21 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0ad37fa0-00b6-3095-be3f-bab8851957cd | -11.818 | -44.2703 | 2025-05-21 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d6b30a4f-ea27-35c6-add9-a212af3e726b | -11.0712 | -54.7868 | 2025-05-21 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| d9d69963-5b19-3671-9907-67cac1158451 | -14.1672 | -45.4673 | 2025-05-21 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 4104ff1f-2686-3fe9-893f-2c90d2e880f7 | -12.2946 | -52.4785 | 2025-05-21 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 5427bc0c-aa2e-3d1f-8ebd-2fb834c1196d | -11.0714 | -54.7664 | 2025-05-21 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 114912f8-74ad-3da5-9356-2942489984d4 | -9.0291 | -47.7452 | 2025-05-21 00:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4093645e-fdaf-35dd-a646-62395236861a | -9.6588 | -47.550701 | 2025-05-21 00:47:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3af59560-de02-3b0c-92f0-e1a69f1ff0a0 | -11.1464 | -53.922401 | 2025-05-21 00:47:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d06115ac-321a-32ab-a55f-149c1eecede0 | -11.0796 | -54.768902 | 2025-05-21 00:47:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f06a4b31-7d07-364d-9e6a-9efaa4a0b1e4 | -12.6897 | -58.118301 | 2025-05-21 00:47:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0edfa150-e767-38c1-b1bb-779ef003d6b5 | -10.831 | -56.9547 | 2025-05-21 00:47:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3a05122-5163-3083-81de-235c07a786e5 | -10.6829 | -57.599899 | 2025-05-21 00:47:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ecc1cc1-7fbf-34b2-8d0a-63af14847d1b | -12.0405 | -54.966801 | 2025-05-21 00:47:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4664e2-1d15-357e-a4db-fd134269e4e6 | -19.7348 | -54.5084 | 2025-05-21 00:47:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| da8719e0-8219-3304-a6b8-40f60b3660da | -10.6813 | -57.592201 | 2025-05-21 00:47:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c60441f2-c376-3584-99aa-b5441f80bd66 | -19.0574 | -53.452202 | 2025-05-21 00:47:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a8f41d1c-d909-375e-bb08-344a4d6588d7 | -19.117001 | -52.690701 | 2025-05-21 00:47:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0047859e-d4ad-34a5-be41-f0519641dc7e | -10.6001 | -52.842602 | 2025-05-21 00:47:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8704ca55-36f9-3412-958f-7ece90eaa3aa | -12.0307 | -54.969002 | 2025-05-21 00:47:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e686e5e-250f-34da-8cd1-7868e6ca9075 | -9.0273 | -47.745499 | 2025-05-21 00:47:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24823ae8-f63d-39f7-a47f-947a7b7fa1d2 | -12.6915 | -58.126801 | 2025-05-21 00:47:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c5b280c-5b38-3d5b-9f8b-812254205ba3 | -11.0713 | -54.778 | 2025-05-21 00:47:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1946739f-4c3c-3d16-9e34-592d8b54122f | -9.6629 | -47.5672 | 2025-05-21 00:47:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e98cf5b8-c3cf-39cd-b494-9cc6dfd1ed3c | -12.4818 | -57.1828 | 2025-05-21 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff39f184-053a-3892-b32f-2a1fccb4429c | -19.055799 | -53.444901 | 2025-05-21 00:47:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b7d508b3-2b39-3a51-9c1d-6be020ff04b0 | -11.2933 | -53.978802 | 2025-05-21 00:47:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71972116-3183-3190-9ba3-2576faf44507 | -11.2916 | -53.9716 | 2025-05-21 00:47:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e06313aa-0046-3b8d-aa7b-afa7333e95d0 | -11.9255 | -54.405701 | 2025-05-21 00:47:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee0e719d-e3f2-38af-8c8b-0bab0d522c49 | -11.3014 | -53.969299 | 2025-05-21 00:47:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1c03c3c-6ee7-3bbb-8b21-147c6f0decac | -11.1366 | -53.924599 | 2025-05-21 00:47:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1ced0df-0c54-3962-a818-daf1945f927b | -11.3544 | -55.123001 | 2025-05-21 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f46e24b-d9eb-318d-a71c-e9d7dcb96a0f | -11.078 | -54.761902 | 2025-05-21 00:47:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a83648e-275b-3f45-b8aa-bfffb234f01e | -19.733299 | -54.5009 | 2025-05-21 00:47:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 68997669-9fd9-3b94-89db-0db3029e0984 | -11.6726 | -54.933601 | 2025-05-21 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2400844-9f74-37a5-adf3-a99cbc9a3246 | -12.508 | -57.2094 | 2025-05-21 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b319cd26-ef26-352e-9f5f-6190b48773d1 | -9.0332 | -48.942799 | 2025-05-21 00:47:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c298b83a-e5e2-3ce4-8fa0-63111f96d210 | -11.148 | -53.929501 | 2025-05-21 00:47:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7798f03-cbb8-3046-956f-d3b044d435c2 | -19.118601 | -52.697899 | 2025-05-21 00:47:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0e983db6-f691-3a4d-9f76-9da7ee737d79 | -12.1269 | -54.661201 | 2025-05-21 00:47:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bec8b629-3e84-338c-9d43-b365859ae38b | -11.3627 | -55.1138 | 2025-05-21 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8467dc2e-f910-30f7-ac69-6c594682f384 | -11.3031 | -53.976501 | 2025-05-21 00:47:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd496d4f-3f5e-352c-8ce7-e16ba624fa43 | -11.0909 | -54.773499 | 2025-05-21 00:47:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 536a018b-3427-3dec-8b5f-7dc5ad32a5a6 | -11.3642 | -55.1208 | 2025-05-21 00:47:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8baafec-0b4a-3607-9dbf-f8acf2acafd6 | -10.8294 | -56.947399 | 2025-05-21 00:47:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5a2597-98d2-380c-98d1-1a021362a07b | -12.039 | -54.9599 | 2025-05-21 00:47:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c2cc0b3-43a6-3b2a-bd5e-b02f990227ab | -11.0827 | -54.782799 | 2025-05-21 00:47:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e561bd2-c259-3879-b5ad-47b9d91cfd2f | -20.955799 | -56.603001 | 2025-05-21 00:47:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5fff7908-49e3-3e6b-984f-565152ba29ce | -20.954 | -56.5938 | 2025-05-21 00:47:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a0deeed7-71f8-38a7-a631-8c3a6f9b786d | -19.1154 | -52.683399 | 2025-05-21 00:47:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ed377625-4956-3342-a93e-dda9bbce3ef9 | -20.217199 | -50.752399 | 2025-05-21 00:47:00 | METOP-B | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27511230-d948-38c8-9a2d-1828793feed8 | -11.0811 | -54.775799 | 2025-05-21 00:47:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 672c001e-f9ba-33a0-b683-8eaba919c45b | -11.0894 | -54.766602 | 2025-05-21 00:47:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d6c93e6-58d9-305d-83de-d7bae753ee55 | -12.4099 | -52.145 | 2025-05-21 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5ee5c7c-1a16-348a-8ea7-5f077c560b9f | -12.3692 | -49.9683 | 2025-05-21 00:48:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec28f7b5-5cd6-3cbf-a6ad-64e4bb15b594 | -12.3595 | -49.970798 | 2025-05-21 00:48:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2020d8d6-a17d-3abd-8a8e-7ba5e3a28b01 | -12.434 | -43.743401 | 2025-05-21 00:48:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bbd43e77-74b4-3a8d-bec6-9dc0bdddb4b9 | -12.362 | -49.981201 | 2025-05-21 00:48:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c792ef8-2b82-3ab0-963f-247c6ff181b3 | -12.9296 | -56.8283 | 2025-05-21 00:48:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53f28b01-1ef5-3f92-89a9-8f6b11ba8e33 | -14.0212 | -55.127102 | 2025-05-21 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d8d53b4-f2b0-3cb7-8218-21bf527e1c7b | -12.3018 | -52.480301 | 2025-05-21 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdfd4121-027b-3b5a-84fe-66da7182f3b9 | -12.2982 | -52.464699 | 2025-05-21 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d7def18-2ad9-35ef-af25-d39322024844 | -12.2903 | -52.4748 | 2025-05-21 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a10d9947-f66d-3f96-a603-3fcc9c596fbf | -13.665 | -53.936001 | 2025-05-21 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a15bc347-41e0-35cb-b355-9bb58e2e41c8 | -12.2921 | -52.482601 | 2025-05-21 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 889fc014-3b47-3090-82c6-0f670721df20 | -13.6169 | -55.442101 | 2025-05-21 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bea44f5a-eddf-3e09-bd4f-e7ce929eb92f | -14.0227 | -55.134102 | 2025-05-21 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6dea48b0-3888-3899-929a-bba864b8677e | -14.1613 | -45.463001 | 2025-05-21 00:48:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20fa2e61-50e7-38c7-bab5-2077e71b27db | -12.72 | -54.9659 | 2025-05-21 00:48:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 493daacd-9136-333b-af55-456ca393c18f | -12.294 | -52.490501 | 2025-05-21 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4777af54-2ea2-3d0b-ba12-09081aff504b | -12.357 | -49.9604 | 2025-05-21 00:48:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83aa8a95-0c50-3473-8b15-1f73a28a043c | -13.6634 | -53.928902 | 2025-05-21 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ef78be9-bdcf-3b18-9ed7-ee4625dbf76b | -12.7215 | -54.9729 | 2025-05-21 00:48:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ef80db4-1efd-396f-9764-556ea9e83ca2 | -12.2885 | -52.466999 | 2025-05-21 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7995ae5d-3871-351d-928c-12f9f44b429f | -11.7987 | -44.256302 | 2025-05-21 00:48:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4382f47-31a6-364c-aead-caa5dbd2e508 | -14.0325 | -55.131802 | 2025-05-21 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49f8b581-f834-3be0-abf8-6e7016a4b0fc | -13.62 | -55.456299 | 2025-05-21 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 484712a6-f881-3a08-bc90-700c85ed20cb | -12.0803 | -47.334 | 2025-05-21 00:48:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16b8f5a9-a014-3d2d-b93b-e2f52224b432 | -12.4172 | -43.719398 | 2025-05-21 00:48:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1f077b0-cce2-3349-85bd-4ffc90ba9a96 | -12.3037 | -52.488201 | 2025-05-21 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd92f13d-2b10-3b46-82c3-23550e1b0250 | -12.3349 | -49.9547 | 2025-05-21 00:48:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef95800f-23c6-3899-be0e-fac9fdba2ff2 | -14.1517 | -45.465698 | 2025-05-21 00:48:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e10a1cd2-7024-3583-9595-30edbd26cb77 | -12.7298 | -54.9636 | 2025-05-21 00:48:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9185cf5d-d83b-39c3-b3a8-9bf46425a0a0 | -14.034 | -55.138901 | 2025-05-21 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f545524f-5084-3d25-8866-34e98345c742 | -10.9061 | -48.5453 | 2025-05-21 00:48:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58e25b29-5eaa-39d4-94e7-c605f4fe6cbb | -11.8054 | -44.281601 | 2025-05-21 00:48:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3483153e-2422-3256-a7bc-970562bba505 | -10.9028 | -48.531799 | 2025-05-21 00:48:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97d75cf1-84a8-3ba6-b8be-dddc0390bd35 | -13.6184 | -55.4492 | 2025-05-21 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 41fc41f2-4780-3d83-b0db-5f927988706e | -12.3375 | -49.965199 | 2025-05-21 00:48:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30ba5b1e-628b-364a-b8f9-8a0d52c76529 | -12.0763 | -47.318401 | 2025-05-21 00:48:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32ada978-6685-3e18-9d8a-b987856e1c58 | -12.4268 | -43.716599 | 2025-05-21 00:48:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 534daa40-b2a5-3aae-9cd7-415c1ece1278 | -12.3 | -52.4725 | 2025-05-21 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e829965-9063-3760-8cc1-422274161d9c | -13.6748 | -53.933701 | 2025-05-21 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
