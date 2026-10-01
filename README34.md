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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53987a4f-2a79-33b9-9d0f-d9262e910cb5 | -8.8459 | -49.70454 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d5c49fe-300a-3a1d-b70a-fd2e7b77e4b9 | -11.21569 | -45.15018 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ab3a1ae-20ef-3a6c-b6b5-d61bcf4cb912 | -8.8566 | -49.7066 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93bc96ba-5ffd-3d83-81e2-b9295272e33d | -4.27596 | -50.79351 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b49029ba-b900-314d-b2b2-1641763b7003 | -4.2699 | -50.7444 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64544ee3-1bf7-3189-9cff-170be50d0124 | -4.29593 | -50.81295 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 08be2c40-88e5-3696-80b0-a36bf474ddde | -8.29236 | -46.7468 | 2026-10-01 04:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 160e9caa-8f82-3828-a1be-e074647b8b47 | -10.845 | -48.70072 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bd906f2-4d82-3646-b0d3-7c990d4cbf17 | -4.26482 | -50.74718 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5d4f6395-0dea-36b6-bc9b-5d5edcb8a21b | -11.4527 | -43.42607 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1eebd71-d4cf-3ee9-b1be-44b63a517fc1 | -4.29817 | -50.73805 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6fa010ac-e539-31a1-b442-8ab4becabeb6 | -4.26289 | -50.74799 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| cad6cf27-2a83-3463-ae8c-89e0822a3e90 | -10.25754 | -44.58329 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 172fae79-2928-3133-9af9-06698f910e76 | -11.4267 | -43.40952 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2256672c-3cf8-36f8-af1d-866781eb5f7b | -4.29037 | -50.74654 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6154d71d-9171-3b5f-8557-15a4be83f00f | -5.76062 | -45.17228 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f8d88ce-c904-364c-83fa-c5cb1d480d9c | -11.3876 | -43.40683 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f4d3ceb-549c-3486-9139-cad45f671358 | -8.98795 | -44.18095 | 2026-10-01 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78f0f42e-48f9-3cc0-b022-b89df700270e | -7.50712 | -45.8352 | 2026-10-01 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f9e92124-b2d5-3be3-b182-93663d404943 | -8.47766 | -44.88687 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f9862e2-0599-33fa-95c8-0978a9de5705 | -4.27654 | -50.81417 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e3878c7a-cab9-31aa-92d3-12bc84dfdd1d | -4.29943 | -50.76798 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 011c56bc-da3b-3bd4-9f21-e1e755ed928e | -4.27765 | -50.78366 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 94103667-a6b7-39ac-a1ce-83fb59813f29 | -7.61638 | -44.55212 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40812d11-1b17-37ea-8ffb-45abeb664136 | -11.44441 | -43.4327 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ced029dd-1e35-3b62-9081-3f82a74e9b41 | -8.12772 | -43.5259 | 2026-10-01 04:14:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a023c63-c680-316b-ab04-5ffe231b2c09 | -11.18815 | -45.11354 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 181f813b-a8d4-3b5e-80da-fc1227458994 | -4.26904 | -50.74919 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 90b4d18e-fe38-306d-84a3-36c936624612 | -4.62691 | -50.61127 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e2b8195-ad5d-3439-b66a-ad6fbc9e221e | -11.2844 | -50.98271 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4b5d72a-bc8f-36a6-a2f0-30d5d5119f3d | -11.42473 | -43.42127 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67fcf926-6798-3903-8b3e-b6b595c3b45d | -11.31289 | -41.18082 | 2026-10-01 04:14:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4158013c-be25-3a01-a6bc-a53f4442f3c4 | -8.3341 | -44.15861 | 2026-10-01 04:14:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b4cc27ae-81c1-3ee8-bac6-d43a96057e14 | -11.44417 | -43.41253 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 36462cf6-9574-3574-9852-be17900ade1a | -4.30082 | -50.74945 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d632d62-a8df-3b33-9257-c0a2498f4ecc | -11.4514 | -43.43392 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1d9aa05e-f625-3ee4-a3a9-a0c6bbd712a6 | -4.26924 | -50.78356 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 35e96d41-0eb6-36b2-b4aa-495478ceffcf | -11.34556 | -43.35579 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f71de9b3-b256-354a-ab3f-cd51c10ae08d | -4.2735 | -50.73371 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb38a486-2977-3630-99d4-b30634ce4d3b | -8.20846 | -45.49163 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92f37b7c-2442-3d60-98a1-7fc2fbacd33f | -7.38777 | -47.0142 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7493187a-6bbd-33c0-b617-36c566189403 | -8.20752 | -45.47223 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10e57f67-d989-3b75-b2ac-5797ebc2e215 | -6.13302 | -53.26987 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b158403b-ff63-3737-a5bd-23b4209d753b | -8.0167 | -47.46473 | 2026-10-01 04:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62ecbe1c-b232-3ea9-95c5-d65ce1770121 | -10.78592 | -50.53751 | 2026-10-01 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2352d51e-44b7-3bc7-bf40-42720684e080 | -8.33786 | -44.15921 | 2026-10-01 04:14:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eafe83e7-5997-3b4a-9cf4-07cc328a35ee | -4.29326 | -50.7669 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ec5563dc-18e9-3ed7-81c1-4e2386084067 | -7.61732 | -44.54932 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 226673a2-78e9-3b44-be80-b4f57ef35323 | -11.44945 | -43.4457 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3e84026c-13ef-3628-8957-85d6709c83e2 | -11.65501 | -43.5561 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a455e1e7-b6e2-3562-baa7-5b4c2e6f4163 | -11.46914 | -43.45718 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfd1d03f-7b48-3e9e-ba72-46704a51a405 | -10.29699 | -44.64709 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c211c175-3794-31d2-9bcf-66bcf6160f0e | -10.85167 | -48.69164 | 2026-10-01 04:14:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09daa30b-de1a-3c0c-94d5-f13e991cfbae | -10.29621 | -44.65175 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d08c942-a159-33c1-b0cb-de6764620352 | -6.86446 | -44.92987 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e66298c4-6284-39d6-8977-84efaca7e4b7 | -4.25786 | -50.75065 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c5dd5b66-6038-333a-9df9-b98f0ca4cfb7 | -4.63228 | -50.61648 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 21189313-038c-307a-ac47-8baaa995a775 | -4.26071 | -50.77098 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d23fd0ea-1ecf-31f8-a1c5-3d4dca240d1b | -7.07527 | -42.30135 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| cdaf65ba-2e67-37f3-a34f-e7837bd3666a | -8.0218 | -49.3835 | 2026-10-01 04:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 341dab3f-68c9-3678-aa03-3fd41da02eb7 | -7.4969 | -45.79271 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 094e5438-0a02-3729-a1d4-1b6668214856 | -5.36525 | -46.22586 | 2026-10-01 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b8598d8-ca83-3392-9426-d635388bd982 | -11.28996 | -50.98384 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cc091d2-7c9e-342f-97a6-0e047a84fe86 | -4.27634 | -50.77953 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 7a7d1a8a-a3da-3684-b2b7-5149db6372ea | -4.26977 | -50.79243 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| df1eccf8-c40f-333b-a9da-aa2f84f0171e | -10.65822 | -50.76266 | 2026-10-01 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49cd01e5-659e-31bd-ae71-fe9154ecf864 | -6.00686 | -49.55639 | 2026-10-01 04:14:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70f47bf2-c50a-358c-9213-6c7043263bc6 | -9.1961 | -45.81785 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 901ac88b-6aaa-36a9-9edc-e85107b8b2dc | -11.41905 | -43.41224 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fec1edbe-ac82-3ca6-8947-d01dcd1ce6b7 | -11.38721 | -43.36657 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 779fb397-3377-37a9-8748-c0f3f5db0662 | -11.18052 | -45.11227 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47006ab4-d962-3718-94df-e8eeeaee7eb8 | -4.26034 | -50.76214 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 12310c62-8054-3456-a813-49800ad97f0f | -11.4073 | -51.02198 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa2c6cbf-d89f-30fe-aef4-2748d4c35de9 | -4.29935 | -50.79363 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5d3f0cf0-b4ab-339e-bf0c-4d2b0ab5c93a | -8.84366 | -50.50774 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 724d0c1c-fe79-3400-9522-4238bc1498c1 | -7.49867 | -45.8338 | 2026-10-01 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2411f41-38ed-3a15-904f-92e971372208 | -9.65236 | -45.11982 | 2026-10-01 04:14:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b454ee0-941b-3204-9160-55b1429d1013 | -11.61775 | -43.54154 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb38ce2d-6ed6-3715-ab4d-042411aee7f5 | -8.13535 | -43.43634 | 2026-10-01 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0be1f518-0fda-3a12-9b65-2b6c812c1f5c | -11.45205 | -43.43 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5158baad-e8ff-3779-a78d-e56284cbef5b | -11.41358 | -51.01936 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c50edf97-9127-3769-888b-fe9c6114c561 | -10.7384 | -44.41537 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46084b9a-6cd2-3945-841f-fbfe28038d7b | -9.81203 | -44.84116 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55131035-63f2-3fd6-8e8e-3af4b311b0b6 | -11.19142 | -45.1872 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2d8a068-8625-35cc-9c4c-274831825639 | -4.26486 | -50.82095 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ad1f7a4-8677-31ce-84c2-67d9ad7f52b4 | -11.40857 | -43.41042 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d02ca22-f275-36ed-9a8f-8cc6f724be4d | -4.25825 | -50.78522 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 493b9a88-3bcb-3018-a57a-20de5c97f82c | -11.45994 | -43.44753 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 82aaa8da-97ad-36a4-bfe2-da2a0d41c2a0 | -11.19216 | -45.19455 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce5cf0e9-32a8-372f-8ba7-bdd66946800e | -11.4501 | -43.44177 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a6dc92c0-72ea-3d35-a00a-a5acc22885d9 | -5.75546 | -45.15189 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e4140407-4d48-3439-947f-78d3300bed64 | -7.19038 | -46.50625 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44eec47a-508b-366a-bd36-6c19878f4617 | -4.26858 | -50.76227 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| a9e2d3f1-e3f0-3a91-ada3-792af840790f | -11.71463 | -43.44011 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0c845e5-7b36-3792-8f4c-91d0099b7135 | -4.27634 | -50.75417 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8c843186-28b2-3c7a-9a70-9b68fc84f04f | -7.72031 | -49.54731 | 2026-10-01 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a292fa7-7e18-325e-bf5d-891659500046 | -7.5651 | -47.20803 | 2026-10-01 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe4c8c2d-9fa5-37fd-8bcd-4e909caefe86 | -11.25984 | -43.52322 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5665f02-f514-33a6-a7fb-f21a713825e4 | -5.74051 | -45.16471 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a74e9a62-0a49-3d08-a3eb-6aab6a628472 | -11.42954 | -43.41404 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README35.md)
