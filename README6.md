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
| 7a0538ec-f82a-3337-a5b1-2d29e42db6d1 | -12.0266 | -57.0845 | 2025-07-06 04:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 99eb9995-6401-3f06-84f4-90671af88e87 | -12.0266 | -57.0845 | 2025-07-06 04:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 86790f20-0a68-35e6-b873-a65fd0c790b0 | -6.5631 | -51.1126 | 2025-07-06 04:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b3ab73d1-1e00-39ee-b615-bc80e15d75ff | 0.69311 | -51.44834 | 2025-07-06 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ff50748-9f48-392b-8fcf-f5c5d4acd2ce | -3.50518 | -43.24603 | 2025-07-06 04:49:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b61f3c28-2a8f-3133-879f-363fb8f235bd | -2.87649 | -40.2981 | 2025-07-06 04:49:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c977ebb9-a69b-3577-8405-f6f13013231c | -2.58127 | -51.92362 | 2025-07-06 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 986be013-93ca-32e8-9b5e-ca87c8fe8d70 | -2.31938 | -49.16771 | 2025-07-06 04:49:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e7bb8cc-3cc5-327f-95dd-18001ed236c5 | -3.49994 | -43.24528 | 2025-07-06 04:49:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e9b9395-a691-3918-9593-337ca72ad14a | -3.48831 | -48.44725 | 2025-07-06 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 538741e6-03ac-33de-83e5-2fb87677e4f9 | -3.4846 | -48.44676 | 2025-07-06 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecabcc7d-a436-3457-856a-e04b21e60e47 | 0.69258 | -51.44491 | 2025-07-06 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cea7be1-9787-3ff0-b480-3d7256e68001 | -2.87859 | -40.30353 | 2025-07-06 04:49:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9760f3e0-78b2-3f0b-8c3d-9dcd0fbdcef4 | -3.52638 | -48.43806 | 2025-07-06 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d61c535-f072-3fc3-b1b9-14c6e62df356 | -3.3525 | -47.63424 | 2025-07-06 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc05cdae-46c5-371f-bc5b-e84adafa2466 | -2.58457 | -51.92413 | 2025-07-06 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5079e82-88d4-3b78-b8f9-164f5fe0d172 | -2.87578 | -40.3031 | 2025-07-06 04:49:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 946dd344-be5a-316d-81e2-19603e707947 | -3.30591 | -42.6554 | 2025-07-06 04:49:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72fcbe3c-22be-381d-b5b0-ab727d51843b | -2.5884 | -51.92121 | 2025-07-06 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74a0f891-ce9f-3dc7-abda-5c397a5c1e4a | -2.6305 | -49.0756 | 2025-07-06 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f3a3561-b419-3b79-b84b-67e9300f0f01 | -3.50422 | -43.25247 | 2025-07-06 04:49:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a5b119e-0c10-3905-b7df-5b825fb30783 | -2.58787 | -51.92463 | 2025-07-06 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d0e39c5-5f01-35df-806f-f9b8bd16f1ec | -3.5047 | -43.24924 | 2025-07-06 04:49:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cc61bd5-a891-3263-8dfa-5b64a2debed5 | -12.0266 | -57.0845 | 2025-07-06 04:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0e09d4be-2464-39e3-b252-94347c481f84 | -10.65313 | -46.48476 | 2025-07-06 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec6ed8ce-5237-36c9-8359-6ea2b79a8ba2 | -5.60888 | -45.17677 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b026cdb8-daa2-312f-9fd0-356c76672119 | -5.06711 | -43.72904 | 2025-07-06 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2c86eb29-9661-32b4-a30d-402cbcb0a22b | -7.91926 | -61.56062 | 2025-07-06 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb8b36e8-5241-3a91-8246-2854b194f4d1 | -6.39464 | -42.80082 | 2025-07-06 04:51:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fed88f74-3515-33bd-8e8c-37ee13237052 | -11.45351 | -45.10275 | 2025-07-06 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a3f8e696-deec-3616-80c4-354662b1ee6a | -5.22757 | -46.02192 | 2025-07-06 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 101a5549-828e-3e62-8f25-07e608a8792c | -11.4587 | -45.10343 | 2025-07-06 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d24984c-6549-3572-b66b-21dcaca2ba76 | -10.56285 | -49.13042 | 2025-07-06 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cbe338b-3c3b-37de-aa55-92f86e1914e1 | -10.64742 | -44.48867 | 2025-07-06 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2da2011e-9f7a-3aca-b33f-f57a4bc52ade | -10.57899 | -49.13408 | 2025-07-06 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93446b51-3af8-30a0-a8e5-d7ed61888630 | -10.55999 | -52.04744 | 2025-07-06 04:51:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41cc0aca-fa10-3dca-9eaa-45ac2a9feab8 | -7.20633 | -43.12318 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 30c9ebff-42b7-3b0f-9a42-9db14e4c46e9 | -7.19536 | -43.12888 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a26d7495-cc32-3215-b31d-a4f2798d04f2 | -8.30982 | -55.0988 | 2025-07-06 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31a797f8-422e-375b-ac0b-08295ab0e72e | -4.4458 | -47.99398 | 2025-07-06 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 875bf762-0fb3-31b0-a9f1-530caf8756ac | -5.0683 | -43.7314 | 2025-07-06 04:51:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d43135a-36c4-37ca-9321-c79fe03e3041 | -6.93952 | -42.80642 | 2025-07-06 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ad86c0d-b80c-32ab-a7cd-892461fb77a5 | -8.81068 | -45.96901 | 2025-07-06 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c501375c-bd96-3247-a308-4522661c3207 | -5.60193 | -45.19125 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f608dd3b-e692-3ef5-85d2-6d500d8ae6a0 | -10.58288 | -49.13471 | 2025-07-06 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed14686a-dab1-33b1-87e5-0b42160a1d96 | -9.79804 | -47.74069 | 2025-07-06 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26ff9a8c-621e-37b8-acaf-7147a8aae1b8 | -4.25018 | -48.20792 | 2025-07-06 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87689126-c682-368f-af05-69436cc9c837 | -3.86354 | -50.08203 | 2025-07-06 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e124e8ea-dd8a-364e-830c-12de6aa84064 | -5.6074 | -45.18687 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b6fd1c5-6d56-39f6-9e69-050d41381f0c | -5.57066 | -45.20719 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b15f6b50-1931-31d6-8706-4e6673658856 | -11.45273 | -45.10906 | 2025-07-06 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b8f202ea-4284-3387-b72a-f7b8339bf577 | -7.20535 | -43.13065 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b9179043-5c5e-33a9-98c7-1dd9c7a8d1f5 | -9.78326 | -56.132 | 2025-07-06 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dcc6a64-7302-3999-b283-1e5c90a4aa34 | -7.1893 | -43.13164 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 674fb3ad-34c6-32bc-9ae4-62a7409ac63d | -3.32465 | -52.54407 | 2025-07-06 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13c77187-8a4f-39c0-98f0-335b2128736c | -8.02794 | -45.83637 | 2025-07-06 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 833695ae-b637-3713-be81-e2f0f1be1032 | -10.5712 | -49.13281 | 2025-07-06 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29835054-1695-3567-9f53-d8cee08a02ed | -4.44109 | -48.17385 | 2025-07-06 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35560a1f-c365-3181-8814-6a7e828875b4 | -9.33769 | -58.85381 | 2025-07-06 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adbc18f5-bf1f-3f0c-9a31-21ee0d29bdfc | -9.09215 | -47.96238 | 2025-07-06 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 81c7bdc1-da1d-3615-ac07-bee163ce5101 | -2.9101 | -54.48756 | 2025-07-06 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2aa9249-0897-398e-a42f-de21a9f483a6 | -9.35974 | -58.84183 | 2025-07-06 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea2c2a04-5f63-3ff8-9cfd-49c1df2edd15 | -9.35129 | -58.84841 | 2025-07-06 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80bebbe1-0e03-3df4-a4e2-8ff7b383ab81 | -7.14184 | -44.31345 | 2025-07-06 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c1da439-dfac-38dd-9fdc-ce05c66c44da | -7.97011 | -47.22572 | 2025-07-06 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa6418e2-614b-3125-9359-16390a0fe0cf | -5.60833 | -45.18963 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b41a1f3-e9d8-32c6-9839-3118f2fec737 | -9.9448 | -47.95597 | 2025-07-06 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c34953c-3aed-35ba-bb20-1ccdb24482ec | -8.52037 | -47.51798 | 2025-07-06 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f1a65c1-5617-3588-be0d-af4e77a92cb1 | -6.42351 | -47.22443 | 2025-07-06 04:51:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06517afb-d147-33ca-91c6-c6c5301d338c | -9.94898 | -47.95657 | 2025-07-06 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac75ab29-0188-3e12-bd73-2a598bbae87b | -5.61044 | -45.17443 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1c32949-4020-37f3-ad61-44d1ffd64e9c | -7.19373 | -43.13261 | 2025-07-06 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 585037c0-60be-3b78-aa75-422bd59e630a | -4.53862 | -48.01988 | 2025-07-06 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21596be7-1b8b-3806-bf72-dfe4057c393a | -8.52109 | -47.51659 | 2025-07-06 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8a6b49e-a45e-3a46-bd94-fc651ec7e69f | -9.35729 | -58.83789 | 2025-07-06 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d63431be-2bb7-3ea4-8dbe-fbee3dafa00c | -9.09682 | -47.95916 | 2025-07-06 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e5438452-164e-31b5-a970-45d8928a9d27 | -3.32796 | -52.54457 | 2025-07-06 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29a1c7ef-33af-3faf-911c-90f2138f8d9d | -10.25634 | -48.16423 | 2025-07-06 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fdca8e3-75f1-3580-b114-0d78b8ec4ca3 | -4.02756 | -48.0644 | 2025-07-06 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc880fbe-a21c-3e4c-9e4e-df487ee4a382 | -9.35192 | -58.84468 | 2025-07-06 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5ce1740-d564-394a-90ca-9fe2fa2ebb82 | -8.24342 | -46.94436 | 2025-07-06 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcc1f276-fe11-3e61-8aa9-2cabfdc06e50 | -10.25583 | -48.16782 | 2025-07-06 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5ec228b-7a23-3943-8a03-314a813b3f2d | -10.56339 | -49.13171 | 2025-07-06 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa09b066-89a9-3c90-842e-7336b9d78036 | -5.60903 | -45.18457 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a74d9e18-adda-3b78-ab3d-c4f75c00afa8 | -6.93378 | -42.8061 | 2025-07-06 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cb0c1e66-6be4-307c-ab94-4430b6ebab81 | -7.01751 | -44.34243 | 2025-07-06 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4ee5e4a-4513-3b68-9b77-753739717a07 | -5.60814 | -45.18183 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 930def3d-e32a-3d52-845c-a26e944a9407 | -10.55824 | -49.13477 | 2025-07-06 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c2323cb-39f5-3563-9c0b-284696d81767 | -7.96899 | -47.23359 | 2025-07-06 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10c66d69-3aa2-36c0-9bc8-44a1c7da5844 | -9.33833 | -58.85004 | 2025-07-06 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a54708e9-1979-34c2-9284-a01bc30fadfb | -4.8175 | -44.3528 | 2025-07-06 04:51:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c5fbd09-84fa-3e9d-8e64-ca826cee9910 | -5.6029 | -45.19402 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6107f689-0987-385f-b618-988f7d93747a | -5.60666 | -45.19193 | 2025-07-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15bf30ab-376f-3abf-a35e-87f593ccd7c1 | -4.86605 | -47.40959 | 2025-07-06 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1957f43-26fc-3ce8-beba-4d816f1b9b08 | -4.82245 | -44.35356 | 2025-07-06 04:51:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b33c0126-4c42-3da1-8daf-01e5a00686f5 | -7.90792 | -61.51191 | 2025-07-06 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 79cbbb6f-e474-3fc8-b301-c3d982c0a857 | -10.96929 | -47.94826 | 2025-07-06 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d42c07ac-d472-30a8-bf28-1c18b47526ee | -10.65318 | -44.48601 | 2025-07-06 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38cf351a-0a68-327d-8ec3-5ec79dedb36a | -10.56215 | -49.13531 | 2025-07-06 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 258f1617-307b-3ee5-b294-2883dc665465 | -9.09627 | -47.96297 | 2025-07-06 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README7.md)
