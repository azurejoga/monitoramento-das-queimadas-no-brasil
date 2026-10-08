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

## Dados Diários - Página 232

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7efd512a-1e17-3ed8-9e0c-a57059c43dbb | -11.61116 | -43.64879 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b3a3ec5a-49f7-336f-81c0-c70669bf09f1 | -18.35346 | -42.77072 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| f8c6fc54-d02f-3dc1-a60d-8d9310539d46 | -13.35795 | -43.87312 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 114d5ed8-198a-385b-a356-0bbbdc4d6c14 | -12.08889 | -38.76132 | 2026-10-08 15:39:00 | NOAA-21 | IRARÁ | BAHIA | Brasil | 2914505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 94081df3-cd05-3500-a9a2-78a20de1055a | -11.33334 | -40.91972 | 2026-10-08 15:39:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 7e1580c7-ee39-3220-9b4a-87b30e733c0c | -11.5937 | -43.66049 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| becb94de-13c4-3700-8073-9886eb7aa38c | -11.62961 | -43.59598 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9b3861a1-7eab-3a01-87da-c9d36bbc1f13 | -13.37834 | -43.88175 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd54b508-179d-31fe-aed7-7ded75e63a54 | -14.77658 | -42.65975 | 2026-10-08 15:39:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6b61c652-bb04-3ce4-9151-ab490773273c | -14.30105 | -39.2103 | 2026-10-08 15:39:00 | NOAA-21 | ITACARÉ | BAHIA | Brasil | 2914901 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 382b96aa-25ec-3ada-ac49-9a2e649c806e | -13.38529 | -43.47762 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5bc23780-782d-3ec3-bfcf-36329f048dc1 | -11.77173 | -44.68573 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e6445b37-4bba-3a45-9982-faf5e6ec96f4 | -12.22778 | -43.92798 | 2026-10-08 15:39:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 597948f0-402c-3a29-88b1-52774e471de1 | -13.74371 | -41.11071 | 2026-10-08 15:39:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d2ddbe80-cbdf-3adc-8d25-d82a479d2b99 | -12.18522 | -44.83223 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 1e30f9dd-fe4b-320f-a509-1392c512e5a1 | -16.46145 | -41.26056 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| bf494df2-baca-3737-975c-7575315048b4 | -12.23699 | -44.71515 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 599b5dc4-98e4-3bb0-96c3-eaae2474c52e | -11.63597 | -43.70732 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 98833450-df72-36a4-a37d-12742ecb0ff9 | -15.59927 | -41.16355 | 2026-10-08 15:39:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 62d0319c-3b91-3392-949f-ad985995b075 | -15.5483 | -42.35425 | 2026-10-08 15:39:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cb7231a5-288d-37c5-89bd-3cc007b92af9 | -12.18248 | -44.80822 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 13e1313d-2d24-3d1e-a126-80402bd6cad9 | -15.54622 | -43.17444 | 2026-10-08 15:39:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e43ef5f1-cc0f-3ff6-843d-26ad5bce372b | -14.45009 | -41.20069 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 6ac8cd92-756a-3e38-8c8d-356482d37454 | -14.90451 | -41.10926 | 2026-10-08 15:39:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 175b8b56-ef82-3c0b-ab76-622b9c9ee3a2 | -14.61679 | -41.74375 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a91b9385-3823-369b-9b32-2a1e04ae1f24 | -11.34208 | -41.58945 | 2026-10-08 15:39:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 125d0c08-5057-3482-9a56-32d8d1e1eb2c | -13.69272 | -39.93032 | 2026-10-08 15:39:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| f2991868-8b03-3d26-9894-247e7a512a4e | -14.68404 | -43.13065 | 2026-10-08 15:39:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 25.7 |
| d4094caa-6f05-3cdd-b552-13d2e8a5a45a | -11.35348 | -43.14467 | 2026-10-08 15:39:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 9009df8e-9b86-3b0d-a95f-2b5446384640 | -10.65507 | -37.34594 | 2026-10-08 15:39:00 | NOAA-21 | MOITA BONITA | SERGIPE | Brasil | 2804102 | 28 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 961772b3-2971-3b7b-891a-708d73d6ce37 | -15.38137 | -40.7632 | 2026-10-08 15:39:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1bcba90b-29fa-33af-84ec-d3f738a16cff | -11.76962 | -44.94434 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 06c2297b-738d-334c-87a7-c3cbc8c4920b | -11.61001 | -43.63919 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 9eac01f6-2a26-39f7-a60e-d7c82c5d06db | -14.13795 | -40.79166 | 2026-10-08 15:39:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 153b0a00-f954-331f-a7ba-c737e05df83d | -14.53631 | -41.27161 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 709d81ab-262c-3774-90fc-d085512cc96a | -14.40968 | -41.28978 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 231.0 |
| 95fd95e8-06be-3326-92f3-1b97d2f456b1 | -13.45617 | -41.92263 | 2026-10-08 15:39:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 3553e49f-481d-3b30-988a-2955ff1a637f | -14.46646 | -40.72663 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 348.8 |
| 35d183f4-4c4f-30f1-a924-57dfe6e43387 | -14.94087 | -39.42468 | 2026-10-08 15:39:00 | NOAA-21 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| f85eeff6-e000-32b9-a480-57797a460d2d | -11.47577 | -43.39458 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75f6b44b-313a-33ec-ace0-8f4b9490a548 | -11.35097 | -43.1498 | 2026-10-08 15:39:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 77a100cf-b966-334a-86f5-12b23fe30def | -13.35851 | -43.87846 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 57706c2e-0603-3209-ba4e-fc10d6f56b74 | -11.61758 | -43.65586 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 586467e1-1e2e-3416-8e21-43e5318fac80 | -14.05809 | -43.82068 | 2026-10-08 15:39:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 4a1544a9-5447-37b1-aad0-46042ecabe77 | -14.42602 | -41.13438 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 50.5 |
| f5fb9132-8e8d-3967-8514-07c3ac3dbc59 | -14.43611 | -40.79025 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e70cd473-20f7-3271-bb5d-a401a054708f | -14.56448 | -44.07299 | 2026-10-08 15:39:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 8fcf40c7-b858-3894-8d4d-b0a68fb7bdb8 | -12.71543 | -45.81537 | 2026-10-08 15:39:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0ba57240-f1f1-38d5-a092-d38188327a6e | -13.36436 | -43.87242 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f3bf893a-0b77-340a-8cfc-9639da77d1c5 | -11.14772 | -40.29611 | 2026-10-08 15:39:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| e7a1db6d-952c-3aa4-ab27-d760141a4c5a | -12.61315 | -44.54732 | 2026-10-08 15:39:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 235.5 |
| ae658cde-d938-3a2f-83b7-4fc16fcdafd9 | -11.63525 | -43.5906 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 65dfc5c2-be85-3e46-9ba0-eae7d3304959 | -14.75318 | -39.81046 | 2026-10-08 15:39:00 | NOAA-21 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4c2c4b74-2430-3f91-a82a-a4b117d16d38 | -11.82261 | -39.18952 | 2026-10-08 15:39:00 | NOAA-21 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 8be00a3e-9585-33ce-a2b4-2e6285b7ac43 | -15.05547 | -41.25383 | 2026-10-08 15:39:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b5775f69-f699-34c0-ab13-783bd2b07e49 | -15.57354 | -42.90065 | 2026-10-08 15:39:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f494c162-4007-3725-bf16-65a8aab031b9 | -14.5226 | -40.52483 | 2026-10-08 15:39:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| acd2110f-6dbc-3dd2-9dd2-66c2545cc114 | -12.1812 | -44.82281 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| abc55751-8a2a-3168-9115-25afe3f7d82b | -11.64543 | -43.67981 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 6789c351-8bf7-36b6-b447-9b855b0a4cbf | -12.18186 | -44.8289 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 34f57750-dc97-3397-9f45-f2de38707b36 | -11.75846 | -44.93368 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8bc909e7-8a3b-3e60-a6ad-f3875ea6cc8a | -11.61887 | -43.61169 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 655d952c-2ebd-37d0-972a-a9faebc56bd9 | -14.4505 | -41.20436 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 5d1b14dd-dff9-375e-aad6-3dcacd6d687c | -11.76935 | -45.55869 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1b2e9af5-5758-303d-9cab-9caaa255ebcc | -11.76863 | -45.5521 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 015a97e8-41c1-3c21-800f-2fc154a964d4 | -17.00565 | -42.37772 | 2026-10-08 15:39:00 | NOAA-21 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 36edd622-0086-3903-abe1-e748f09d6351 | -11.77923 | -45.58462 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 7f72fb3a-7f1d-3b31-a4d9-c67501cd1a44 | -12.54568 | -40.21755 | 2026-10-08 15:39:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0687c02b-fb7b-39a7-b15e-68969c49fd8e | -13.48424 | -42.4838 | 2026-10-08 15:39:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 4e626dca-74fb-31ab-aafe-e2a3fae335d3 | -14.55788 | -44.07347 | 2026-10-08 15:39:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 2ce1c749-a995-3648-b938-cac439075599 | -12.61252 | -44.54152 | 2026-10-08 15:39:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 235.5 |
| b0292419-72a5-353d-b7b6-88393b5bc9e5 | -13.96436 | -44.85173 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| be905a42-11c2-3157-982a-6f68a0a5a492 | -18.26056 | -42.17744 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| 50d7f7b5-b5fb-353d-ad4f-92c7e37a83af | -16.48618 | -41.80987 | 2026-10-08 15:39:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 9c98862e-95e2-3a5c-938e-693972686d67 | -14.03577 | -40.55802 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d63a47d9-37d1-3330-9c09-3d653d8e8496 | -14.85781 | -42.06358 | 2026-10-08 15:39:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 417d88ab-cdd0-358f-a985-244d6b64a901 | -11.7715 | -45.57838 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 29246c5e-0816-3e5b-a94b-fc320f8eb4c4 | -14.11024 | -41.86281 | 2026-10-08 15:39:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 6eccf098-ad66-3cf9-b329-35d3e934841c | -14.174 | -43.66723 | 2026-10-08 15:39:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 886d8e84-a6b3-3830-896f-eebf2f98a323 | -11.85315 | -43.53486 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| e90c8713-f278-3351-bad3-2a64b05ced46 | -13.37192 | -43.88242 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 1a74898c-e50b-30aa-9596-23a7c2dfca45 | -12.04114 | -43.43454 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 69168fa3-21ed-3b21-9272-fbe1622f428a | -11.61649 | -43.6462 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d1e32510-0ab4-36b0-a64d-74706edf7860 | -14.52221 | -40.52145 | 2026-10-08 15:39:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| e7cc1473-2dc6-3382-8d2c-345fa31da7c0 | -15.47717 | -42.07464 | 2026-10-08 15:39:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cc2f2885-e317-3163-b53b-1835593ee0c2 | -15.57311 | -42.8963 | 2026-10-08 15:39:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 611d51a8-8e7f-3e79-bbd1-fa4d4b4b054a | -12.15998 | -42.26802 | 2026-10-08 15:39:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 44.2 |
| 0b22ff06-551b-3682-90fd-5775085130b0 | -11.81982 | -40.48987 | 2026-10-08 15:39:00 | NOAA-21 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ae4c0d84-f56a-3da6-80ea-491029b15272 | -11.76232 | -45.49426 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 2d6ddac6-0bcb-37cc-a297-4da7e5107b20 | -11.62285 | -43.70272 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 8097df63-6006-3328-ba41-d7e6d1bdadf7 | -11.74339 | -40.60991 | 2026-10-08 15:39:00 | NOAA-21 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a0fc573f-c162-37a5-ac26-32429a27b3d6 | -14.91842 | -41.13366 | 2026-10-08 15:39:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 2ea7e197-74f7-3400-9265-67d9cb65f04b | -11.83862 | -43.56856 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06386074-4ded-3476-afcc-9f461fa00808 | -11.30824 | -44.83647 | 2026-10-08 15:39:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| f962a35b-854e-395f-a272-834bc581c73e | -15.31384 | -40.64495 | 2026-10-08 15:39:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 0061bc55-e529-363d-8951-83f240388f2c | -11.77804 | -43.53237 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 120f2154-4450-3b0f-8822-813a4d8a10d6 | -14.53675 | -41.77293 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 127.2 |
| 93013396-cd91-3c31-891a-8aaa01eca9fa | -11.63043 | -43.70475 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e04e6b21-0290-39a8-983f-852bc8aef3e5 | -12.24436 | -39.6796 | 2026-10-08 15:39:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 286776e9-f571-3595-9242-e877702d55b4 | -14.76085 | -41.32645 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |


[Clique aqui para ver as próximas entradas](README233.md)
