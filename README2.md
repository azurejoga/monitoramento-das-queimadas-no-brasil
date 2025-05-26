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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1306f01-ade3-325a-863f-05820f60d330 | -9.9759 | -52.132 | 2025-05-26 00:44:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e831435e-b384-3c6d-b8c7-51374bd170ef | -8.0118 | -43.161301 | 2025-05-26 00:44:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4cca4c28-3e06-311e-b779-b07fadb92d7b | -11.1452 | -53.916199 | 2025-05-26 00:44:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f42bb1cd-c4c6-3549-a5dd-fd106a7ccfa8 | -9.9777 | -52.139801 | 2025-05-26 00:44:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4352258b-9d56-30b4-8cf5-88a25b41699a | -11.2992 | -54.0056 | 2025-05-26 00:44:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1c064db-abe0-3c34-867d-00b8fc32a219 | -10.4532 | -47.937698 | 2025-05-26 00:44:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20df5919-a40b-3e2a-92f4-1efcb8b77ae9 | -7.6618 | -46.1049 | 2025-05-26 00:44:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2af73a98-93b9-3040-b0b3-09591775d28c | -8.0276 | -43.2225 | 2025-05-26 00:44:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 503565fd-f87c-374b-ae21-9e2df49fb47e | -20.6094 | -48.8605 | 2025-05-26 00:44:00 | METOP-B | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 298e3054-90e3-3d6a-b669-4b6e1f4eff33 | -8.0517 | -43.117901 | 2025-05-26 00:44:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 118e1475-cd36-3b6e-ad03-5d61a32f8e7e | -8.4474 | -49.6236 | 2025-05-26 00:44:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd1f79bc-95c7-36f2-ab15-57253b52c719 | -13.7866 | -54.312599 | 2025-05-26 00:44:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98dc9750-8b30-3b9a-a34f-83905799a2c3 | -11.3007 | -54.0126 | 2025-05-26 00:44:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 939b77f4-15d9-3896-a72a-6d980e410b1e | -11.8692 | -52.243099 | 2025-05-26 00:44:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86c85629-9c83-3543-b50e-e9001b0f6224 | -8.0214 | -43.158798 | 2025-05-26 00:44:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d505b0c-0aba-363b-975a-11795e432ab2 | -8.0102 | -43.1945 | 2025-05-26 00:44:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 540432ed-33c9-3da0-86cf-f4411f8228d6 | -8.0693 | -43.146198 | 2025-05-26 00:44:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6e859d0a-2246-3830-92ca-a429e3b711db | -10.4499 | -47.9244 | 2025-05-26 00:44:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbd71598-0a3d-356c-81c0-d71b959391bc | -8.0613 | -43.115398 | 2025-05-26 00:44:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db8c6375-b937-3425-960b-15e52ff2ff61 | -19.884501 | -54.353901 | 2025-05-26 00:44:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 20ab4719-bd4a-32e4-8ef1-6b0a0d3d1c37 | -8.0198 | -43.192001 | 2025-05-26 00:44:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e4be631-f4b3-37df-8945-0cef7c1ce0d7 | -21.276501 | -48.616199 | 2025-05-26 00:44:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 475ec089-93e3-3478-99ad-b44106394c07 | -10.4564 | -47.951 | 2025-05-26 00:44:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 926e4ad6-4f0b-3300-bb8c-0b4800d63a51 | -7.6569 | -46.0853 | 2025-05-26 00:44:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cc72508-4220-3f67-a194-85a9e052227e | -11.1468 | -53.923199 | 2025-05-26 00:44:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82e8bfd2-0978-38a4-9d43-02ed56916649 | -10.4629 | -47.935299 | 2025-05-26 00:44:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd090a71-5c46-3dea-919e-28e6a74a2fb0 | -11.3689 | -55.109901 | 2025-05-26 00:44:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adc8cd8b-d11b-339b-9e2e-620ee6f53bb9 | -8.0293 | -43.189499 | 2025-05-26 00:44:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3188f073-1a1d-351e-9495-d16281448dd5 | -19.876301 | -54.363998 | 2025-05-26 00:44:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d721f9f7-6d53-36e4-aa69-3c00bac32fad | -8.0312 | -43.1964 | 2025-05-26 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 162.5 |
| f755472a-a023-37e3-8c00-07e205174acf | -8.0123 | -43.1984 | 2025-05-26 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 698d03d5-1bc3-3965-a4c5-b61a3aa448a0 | -8.0315 | -43.1728 | 2025-05-26 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 95438ce1-4ed9-3e77-ab7a-e27ad289ac5f | -8.07 | -43.1216 | 2025-05-26 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| d53b93ee-62a3-3130-a98c-5efb03e12f5a | -8.07 | -43.1216 | 2025-05-26 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 99cd0fb7-9e52-340a-9453-87f5294f0b44 | -8.0315 | -43.1728 | 2025-05-26 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| b44140df-833f-3ad3-9ad9-fb5347a6aed1 | -8.0123 | -43.1984 | 2025-05-26 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| e1d7a30a-6277-3c14-9483-1f049f6fb6fc | -8.0312 | -43.1964 | 2025-05-26 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| be026b01-bab3-3c4d-846b-06f175bf5253 | -8.0315 | -43.1728 | 2025-05-26 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| ba688186-44dc-364a-b0a2-974f054576d4 | -8.0312 | -43.1964 | 2025-05-26 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| 43e922f8-ac0c-3a51-bb01-08aea38ec7cb | -8.07 | -43.1216 | 2025-05-26 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 6f86509a-63b3-3748-b9ab-1c328eb65928 | -8.0312 | -43.1964 | 2025-05-26 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 82600add-d2f1-30ce-874e-b1d5012a6751 | -7.6574 | -46.1013 | 2025-05-26 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| f2936e2d-99cb-37ba-8e98-1865e38f51bf | -8.0315 | -43.1728 | 2025-05-26 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 9640b198-ea26-3a28-aa76-83d545d64657 | -8.07 | -43.1216 | 2025-05-26 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| ec983c2e-a7a0-3ffc-9888-b1fca9d93b3d | -8.0312 | -43.1964 | 2025-05-26 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 32c0d84c-4ea5-36d5-9b4c-70eea28e31c2 | -11.3054 | -54.021301 | 2025-05-26 01:35:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3d1685-ea88-3054-9eb8-477495b101e4 | -6.5771 | -51.1161 | 2025-05-26 01:35:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 824390d3-e204-3f4a-aae1-bdb9a8882c1b | -19.8797 | -54.3568 | 2025-05-26 01:35:00 | METOP-C | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 76fa394c-ed49-3f3f-81c7-e7b383fa58bf | -19.885 | -54.377998 | 2025-05-26 01:35:00 | METOP-C | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1b7e34aa-b607-34ab-bbfa-4d60ce46674e | -19.882299 | -54.367401 | 2025-05-26 01:35:00 | METOP-C | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 43aee6e9-1721-3fbc-9f18-303512720e84 | -8.0315 | -43.1728 | 2025-05-26 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 44ec016d-4621-37a7-80cb-ea59181e8616 | -8.0312 | -43.1964 | 2025-05-26 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| e72e74eb-da91-32a4-9b25-673da99a6146 | -7.6574 | -46.1013 | 2025-05-26 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 5cb303e1-edb2-3972-8527-89fe49b428b1 | -8.0312 | -43.1964 | 2025-05-26 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| ca0c6038-83c2-3a56-81f0-a9c741e9c141 | -8.0312 | -43.1964 | 2025-05-26 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 8c4ae24a-4608-32bb-b68e-cb9246164162 | -8.0312 | -43.1964 | 2025-05-26 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| cfa40651-30b7-3467-93cb-dab359099871 | -7.6574 | -46.1013 | 2025-05-26 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| f8d9d08b-1de5-3404-8693-08c9ee6df764 | -8.0312 | -43.1964 | 2025-05-26 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 33f1f3cc-9375-3d83-af78-b3593501e1e6 | -7.6574 | -46.1013 | 2025-05-26 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 121ec606-d4ad-3e01-81d1-93899a9286cf | -7.6762 | -46.0995 | 2025-05-26 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| abf0a342-c6e9-3681-b84d-cdd6a2b708f3 | -7.6574 | -46.1013 | 2025-05-26 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| d625f5bf-6e63-3a37-9b08-01976e231fc3 | -8.0312 | -43.1964 | 2025-05-26 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 126.6 |
| 68773b86-f774-3440-98ed-8bf22cf2e621 | -8.0312 | -43.1964 | 2025-05-26 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 6561d141-d405-3b5e-b795-e24b9a9a9047 | -8.0312 | -43.1964 | 2025-05-26 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 8d3a15f9-64be-3602-a961-8b002a9d9b94 | -8.0312 | -43.1964 | 2025-05-26 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 33fc7a6c-57a7-3137-8fed-d1831d708077 | -15.42966 | -42.17071 | 2025-05-26 03:08:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 579b89e7-e5b9-32b5-adbc-3a8252c92e26 | -15.4267 | -42.16946 | 2025-05-26 03:08:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 22390037-a587-370b-b0f1-84570a7ae566 | -15.43361 | -42.17184 | 2025-05-26 03:08:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9d08f4bf-b0d7-3524-99d0-b3cb07b72ed4 | -8.0315 | -43.1728 | 2025-05-26 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| cafd9d56-0dd5-3600-811f-37e8f20644e7 | -8.0312 | -43.1964 | 2025-05-26 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.9 |
| ba3c7d12-ebdd-34d6-a44e-982d81010ccd | -8.0123 | -43.1984 | 2025-05-26 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| e8890da8-dafd-3ae1-910a-3fdd826b2c22 | -8.0315 | -43.1728 | 2025-05-26 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 39ec1880-c858-325a-bc06-f76748a09960 | -8.0123 | -43.1984 | 2025-05-26 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 24efbcd7-ecfd-336f-8684-8c2c9d57c507 | -8.0312 | -43.1964 | 2025-05-26 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 223.2 |
| bd85c9bb-1efe-3ae5-bc18-4b41ab65876a | -6.83389 | -44.63195 | 2025-05-26 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed9cc5cb-593d-3ebf-99a7-d76c418e8148 | -10.49658 | -42.42638 | 2025-05-26 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 901a497d-0298-3cca-9f67-0a5a95518cf9 | -8.02076 | -43.18578 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7ab20d7b-9c98-3f2a-831c-51ffeeed9cf9 | -7.59484 | -46.28557 | 2025-05-26 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9200f34d-6cf6-3149-aace-f90401e98371 | -8.03087 | -43.19723 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| e50d7232-bcb7-3ac1-b546-f6cb66280aa0 | -8.01832 | -43.19897 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 45dc0664-12d8-31b4-82d3-bc06eb8341b8 | -8.02156 | -43.18148 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 1c16d489-f35c-3dd0-a0da-a4ce00295ec8 | -8.07121 | -43.13245 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 0e20b9bc-228c-3fe7-85ec-e250f7349f54 | -8.06738 | -43.1314 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| ca37e0f9-4d82-3878-a5ea-4c3d8186c49d | -10.49724 | -42.42294 | 2025-05-26 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| adbc7be2-efb7-3841-8b4f-b67a18aaced0 | -10.49541 | -42.42187 | 2025-05-26 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9ab47002-8ccb-3e8c-afb9-b6c874ce4ce1 | -10.49477 | -42.42531 | 2025-05-26 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 4455550d-a817-3fe3-bed8-c6cd447ce326 | -7.66306 | -46.10344 | 2025-05-26 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58669e98-a15f-3af0-af5d-3cef6bbc1bbb | -8.01749 | -43.20339 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c9053a1d-453d-3e19-963a-64aabb85863b | -8.03168 | -43.19285 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 16caddcd-8457-3cdf-9709-07f86859080f | -8.01913 | -43.19456 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9e54855-6255-304f-98c3-19a224aafb96 | -6.83505 | -44.62563 | 2025-05-26 03:28:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d30036ea-4d90-3c82-b8a5-0595358762ef | -8.07325 | -43.13258 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03624241-5c93-3d48-9c41-087161c1294e | -7.54306 | -45.82948 | 2025-05-26 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15c54b0c-5f73-3c85-a6b4-c52cbbe7f9e5 | -8.17138 | -34.97913 | 2025-05-26 03:28:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4ea3ea8c-7f5f-3ca4-bc43-0d117fdc68e6 | -8.02744 | -43.18277 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7a100863-22c0-3f34-84b1-5935ab6e1763 | -8.02418 | -43.20037 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| d79b1168-4d86-332d-ab88-2de4668741dd | -8.06657 | -43.1358 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| fd6f6dff-6849-3a41-a8e2-74f64af235a0 | -8.03249 | -43.18846 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 50c03435-ea15-3a3a-a10c-d65da61ed358 | -8.02662 | -43.18715 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| c8870ea0-16ed-367f-930f-336662b240ba | -7.66687 | -46.10563 | 2025-05-26 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README3.md)
