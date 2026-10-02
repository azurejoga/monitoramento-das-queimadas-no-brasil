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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0469279-ef7e-3b0d-9beb-47ad00cd114b | -9.33437 | -47.24868 | 2026-10-02 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3f52765-4cc3-34cb-9c66-d2211ab66b9a | -11.46014 | -43.41832 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d9a6194-dadf-34a4-bdd5-150ccc983e07 | -11.45642 | -43.41257 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27c94875-d25b-3f55-bca5-18488fdcb233 | -12.53606 | -43.08884 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2bd07c88-b6f3-3d76-8000-26d94fae743f | -11.41029 | -43.40375 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 226b67ad-44b8-3bd1-bc1b-d06c2e318fc6 | -13.48081 | -42.48318 | 2026-10-02 03:55:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9cd910db-f71c-308b-a763-25d86819652b | -13.34119 | -43.85003 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 339a5a36-6ccc-38c9-b66e-eae1c930439b | -9.07728 | -44.99196 | 2026-10-02 03:55:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98dfc0a5-c303-37ff-839e-a66239e9198c | -13.86587 | -43.63225 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 747ed6f5-dfaa-3071-8b91-d6023748da3e | -7.74807 | -49.20747 | 2026-10-02 03:55:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 36a4ac53-6401-356c-bd40-78b17198e2ca | -12.99453 | -51.29757 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 72b59ac0-4356-3523-8ff9-40abcc570084 | -11.76081 | -43.57339 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 2ad48853-8538-3a78-9307-082310aa77d1 | -9.44573 | -36.58536 | 2026-10-02 03:55:00 | NPP-375D | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e53c9a6-c687-35ca-a679-caa090781350 | -11.42502 | -43.40162 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5bfa8e5-2ea8-3206-907f-4e8da5a67261 | -9.52265 | -45.34596 | 2026-10-02 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a285783-be23-3cdb-9df4-bc0b30b5e167 | -13.34304 | -43.86567 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0112bbde-5703-3bcd-ac83-b9e868f597e8 | -13.39129 | -46.81814 | 2026-10-02 03:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9988903-c751-3642-88bb-414020c9c718 | -11.14835 | -44.62403 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 353015fb-0366-310b-a682-47a39ec6dbcf | -11.73432 | -43.4398 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8074de6-ba8b-30fc-a36a-0c757ba1f6e0 | -10.21578 | -45.30762 | 2026-10-02 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94a3cf4b-1819-3ff2-b3ca-5ec91f510ccc | -11.23878 | -45.232 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a2b8e18-41e9-37ab-8126-9a78568f2175 | -15.49532 | -41.552 | 2026-10-02 03:55:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c4c09cc-3f82-357a-93c3-0a4f6d13f2ff | -10.90705 | -43.83894 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| babbb61d-f756-3458-b3f9-2178cb73d027 | -11.74813 | -43.4424 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 500d90c5-12fc-32a2-8da5-9da0e6056556 | -7.86928 | -44.17514 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 241e7968-6c83-32cf-8397-e81111989dc0 | -11.60107 | -43.53965 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 727dad39-9eb8-3961-af28-4935717cc093 | -9.84787 | -44.83765 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cadee2f-294f-36d0-9c3f-63b82fbdcb15 | -11.26126 | -44.26352 | 2026-10-02 03:55:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 455ec653-142a-3897-bc1d-1474cf5c4318 | -7.87848 | -44.18338 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7601abaf-e8c1-3846-8751-ce8c21639481 | -11.65792 | -43.59614 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d5fd9477-ffc8-3e4e-8346-22297631a94e | -11.73892 | -43.44067 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a22302c-d566-38c4-8216-46be91c3164c | -14.87545 | -40.69875 | 2026-10-02 03:55:00 | NPP-375D | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| bd6a8a3f-0304-390c-b79f-5a91ce2e7c63 | -12.51331 | -43.11302 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| af87458f-9745-3a11-b1d2-7ad9364bed55 | -8.00699 | -47.43807 | 2026-10-02 03:55:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcbdee2d-3fb4-3795-a331-b3637b7d8420 | -8.78103 | -41.08112 | 2026-10-02 03:55:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e22ad3e1-59a6-3719-ab82-1dcfab526478 | -11.70513 | -43.58825 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6544c821-e832-3614-a41f-de5daca4c015 | -11.15338 | -44.62499 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8122f83b-9fc6-3790-8858-c01566bf1bdd | -13.86336 | -43.64597 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3aca644c-892f-3846-ac25-12d9ffade44a | -11.66079 | -43.60672 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 24d59506-c490-3cb4-b080-9056c7240307 | -11.12989 | -44.61132 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c37e4e42-2a7d-3218-a517-cf89831779cf | -7.86987 | -44.17186 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| dfed9173-8140-3dad-8489-6f74d20fc32b | -14.77802 | -40.33578 | 2026-10-02 03:55:00 | NPP-375D | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d9a17828-e128-3f33-8c7f-5ba8309d76c0 | -11.47043 | -43.44033 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0bb192b5-aa30-3c5b-bfce-0880960ecea8 | -11.74633 | -43.44558 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15573b16-5a4b-391f-b423-fdef239e34cf | -8.74515 | -47.59249 | 2026-10-02 03:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2dda78d-a94b-3ba8-b6bd-4e16c9df41f5 | -7.74102 | -49.20601 | 2026-10-02 03:55:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 96f61fee-d5b9-36ae-af63-7c4a5e73ff12 | -12.8307 | -50.64935 | 2026-10-02 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4f66d50-5b70-3455-ba84-1f4b0aa18657 | -9.83441 | -44.85202 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21cdcb34-1c9e-3081-a44f-43ad38cc8194 | -11.16396 | -44.62417 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9be54ed-e8dc-3485-b130-e9050fe7ad6d | -11.65326 | -43.59527 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a29f19b-b5a4-30d4-97af-2c761030e063 | -11.71661 | -43.51143 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6156d28-3489-37b2-98d3-aa5ac7f37076 | -11.41119 | -43.39893 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17bcacbc-fc39-3dc2-85ac-8fe73747ff12 | -10.24841 | -44.56985 | 2026-10-02 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20382bf3-ed64-3d23-8109-a14121e4e0a6 | -12.52461 | -43.10139 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c8d73546-d08f-3d5a-b2ae-9496d33c79ba | -14.03271 | -41.60043 | 2026-10-02 03:55:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aa34209a-1b02-3faf-9834-8518bc6478d4 | -11.26532 | -43.56493 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04917216-8347-3bbc-b7cf-bba23b0094f5 | -8.53756 | -44.05307 | 2026-10-02 03:55:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 769871ef-794c-3090-801b-6e03cd336f7e | -11.68053 | -43.49929 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25283530-69cb-3235-97e3-33604219abca | -9.84488 | -44.85394 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74f78240-c873-3607-a5e6-32ac0759e6a8 | -8.32965 | -44.15723 | 2026-10-02 03:55:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 249ca7a5-a244-368d-9fc6-114ee8169a63 | -9.52527 | -45.33181 | 2026-10-02 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f8f293d6-6973-38f8-bf79-58550a95fd11 | -11.12876 | -44.61733 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9d55549-2f7b-3bd8-a2d9-dce5f5485fa6 | -12.66708 | -45.09687 | 2026-10-02 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dc770c1-d103-31c5-81fa-51688ac49968 | -11.69695 | -43.59339 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6203f24-d3d8-3702-8632-981686b48772 | -13.01792 | -51.29517 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d15f4591-3cba-3484-88b3-243ec30952b0 | -13.86952 | -43.63771 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 728d31a7-094b-31af-a502-09e83302ab6b | -7.8635 | -44.17749 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 048d81de-cce3-3117-8ab7-a49640730574 | -11.4158 | -43.39984 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 269439e8-cf62-3c73-9729-c49275769fdc | -12.52715 | -43.08743 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9c4f2f0f-e6a6-3249-97ab-22a6db261d40 | -11.70648 | -43.51452 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61aff88e-62d0-3d1d-84d2-0ac0270ab6dd | -11.46759 | -43.42979 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82995922-620e-3b94-a019-f04f96bd8469 | -11.43178 | -43.40128 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c457e334-905e-3a9c-8ed8-cf716b0fc60e | -15.30773 | -42.77734 | 2026-10-02 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45edf2e3-65ca-3e05-8a76-620c85ef4591 | -10.59451 | -50.08707 | 2026-10-02 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39011f6f-26d2-3e10-9374-c3961ae0a4ce | -11.72443 | -43.51138 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93945a13-6fda-3799-9be8-494b2620ae64 | -11.41247 | -43.40252 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b65ca9f6-db9b-3476-b9f6-72f5e7de19ad | -12.99064 | -51.28074 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 04e7f723-e956-34ea-a437-ec0eccb1c895 | -13.34855 | -43.86168 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dc8b2b2c-c174-39ed-8e04-0edbd2f7da91 | -11.72885 | -43.44371 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d9e45a6-10e3-3dab-94d9-c01a029cae0a | -11.43092 | -43.40611 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eeeaa1d9-b749-3b50-9361-0a863dafeab2 | -12.98759 | -51.29286 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d498b11d-518f-3ff1-8ca3-99999a7549f7 | -11.65508 | -43.58544 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d0210b7-7aa8-3e03-b373-74ae449f7a74 | -11.41708 | -43.40343 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ef3cef7-4c9f-3a8f-ab1d-da39612af40d | -11.42169 | -43.40434 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 462d3b22-c7b3-3884-a606-f3e06fa1d2a0 | -7.74539 | -49.20488 | 2026-10-02 03:55:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2cdb8ab9-ea8b-3fed-a255-8204c00f1fc5 | -11.77489 | -43.57521 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c4a1ae04-3d2e-392b-be15-62aa52c19951 | -11.15785 | -44.62899 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b878589-7d5f-36e2-a306-fb2c9d49fa10 | -11.73519 | -43.43499 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9390a20a-52ac-3f8b-b184-b62518db6fc6 | -11.72211 | -43.50745 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1178e594-005b-305f-8924-a2e72857caad | -11.21523 | -44.84162 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1474b31-9e41-3e43-aaca-b73cb79af460 | -13.52217 | -43.8116 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 477c0097-5cf5-387c-baaf-d839a1144316 | -11.64566 | -43.55828 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0166d018-978b-3b1f-a19b-44f8d38f9877 | -9.8195 | -44.81567 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 856cd0fe-8292-3fe6-9cef-61ced6990f8b | -11.67655 | -43.59963 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33fb258c-e7cb-379f-81d3-8dd5b56defbf | -11.44347 | -43.40512 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff846439-8034-306c-8a12-67a03a6d2868 | -7.87445 | -44.17605 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84717830-92d2-3185-b033-4638de65c6e0 | -13.34395 | -43.86077 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6808e79-eb8a-30ab-b921-08574a46e94c | -9.83799 | -44.83255 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d178795-de4f-34f8-a95b-a2a9e8f7976b | -10.30136 | -44.65454 | 2026-10-02 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8441475c-ae32-3c86-8349-d74e0b27b499 | -11.5269 | -43.51334 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README31.md)
