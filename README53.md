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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 359c7bc4-c376-3de9-b060-c2c9ffb24d86 | -18.82696 | -41.96496 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| e1e46e06-bbc9-3fdc-ac6b-e37cb794f162 | -18.82639 | -41.97131 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 4f17448e-1c6a-3edb-984d-7a3f89f4db78 | -18.79794 | -41.90527 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1cc606da-6d6f-3619-a5ea-89f21ccd6482 | -18.79739 | -41.91156 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6ab4759b-710c-346e-aefa-01c9666da5cc | -18.79111 | -41.9048 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 709f3db2-3bf4-3b9b-9c50-6c3c2db4ffbd | -18.79061 | -41.9107 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f074558-118b-3fa9-99af-43d824614ef6 | -18.79003 | -41.91743 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 42a9c63d-de91-36bc-8bdc-a9564f3dc163 | -18.78324 | -41.91656 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4d301a07-960e-30cd-a6a5-54193f93eaa3 | -18.3967 | -42.80128 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f24ef6cc-54af-30e5-8a74-98fa26222344 | -18.29294 | -42.15474 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4d7aac03-b05b-3c70-ba31-8b596290cd74 | -18.28599 | -42.15702 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1b1ce5a2-3f55-3306-aa19-7d985ea9c4c5 | -18.27841 | -42.1662 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 007099af-7085-334a-930c-4bfc61c0ef95 | -13.35789 | -42.06288 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d1a70223-adff-3b66-a5ba-b7cc39cabcc8 | -13.35434 | -42.06066 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b118de15-8c1a-3364-a2a4-8ab9b43c4262 | -13.35389 | -42.06488 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e5ae9d91-aa93-3fde-bc0d-3f55c42f7830 | -13.3515 | -42.0624 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2632398d-a714-3fc6-8cab-38d08b1de5e1 | -13.35103 | -42.06658 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d212cc3d-adc4-313c-9fb2-59d789b6ac28 | -13.34797 | -42.06001 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a569f41-6f15-3ec7-b7eb-f1629d2b455e | -13.34753 | -42.06418 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57aba31b-e67f-310a-963f-80cea7a6c5fc | -13.34513 | -42.06177 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e5ec02c-0ebd-3477-8e83-53611ed5b73f | -13.34467 | -42.06591 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cdd2ea94-e0f2-30b8-921a-cb169855efc6 | -13.34114 | -42.06367 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fe763580-fbcf-3561-85f3-9b71fc8d7349 | -13.34071 | -42.06778 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 14fbee01-f6bb-33e5-9022-c05a01e9731b | -13.34025 | -42.07204 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0d5feb27-3e74-34ac-a852-774b7c450638 | -13.33828 | -42.06549 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e067b646-b52b-3872-8cd7-e592ce97f7f1 | -13.33782 | -42.06956 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e12a49f-8961-30fa-96a7-a03a78294ab0 | -13.32535 | -42.06595 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c3d817e6-8582-3114-b26c-f74d326dede0 | -13.31893 | -42.06575 | 2024-09-29 04:51:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 868b82b2-25c3-367e-923f-b20a958f2fc8 | -13.19916 | -42.25077 | 2024-09-29 04:51:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7cb8a278-c77a-36eb-be19-697f300749c1 | -13.19288 | -42.25007 | 2024-09-29 04:51:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2682b6da-4d82-372b-8524-8168d21d0174 | -13.43446 | -44.02626 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86707bce-4527-37de-ac71-17390c298795 | -13.434 | -44.03012 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ed24111-4290-3bd3-b8a4-cb85f9050cfa | -13.42839 | -44.02937 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 941bd4bd-d2f9-3ae0-8458-91a5fede5baa | -13.42793 | -44.03318 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a9b83c3-9138-333a-93f2-cff825c33c12 | -12.81964 | -44.82856 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 305651da-eb44-355d-a568-8ae75d83aee3 | -12.81929 | -44.82599 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a28af84d-4916-3288-9ed3-da5877278376 | -12.81797 | -44.84181 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 496efac9-d141-3ed7-9aa7-bddf572cb170 | -12.81772 | -44.83927 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 672bd9a3-8229-3e84-9cea-1f09c6fdb30b | -12.81755 | -44.84511 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2095487-0880-3cab-9dc6-abf6644dce14 | -12.81733 | -44.84259 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bd8c1d04-0f64-3560-8c2f-c6f89a726825 | -12.81714 | -44.84842 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 006fc28e-fd6b-3b51-983b-6dde460e813a | -12.81694 | -44.8459 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cdd8d0f9-ca26-39a3-9b71-d4d56831216a | -12.81672 | -44.85173 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f178e4a2-fda6-3202-a97d-2b9056322c4a | -12.81654 | -44.84922 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e29b573f-cd49-326b-a6f1-c37c0a98a70a | -12.81519 | -44.82124 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7558a6f0-786c-3f8d-bce7-70026709f378 | -12.81477 | -44.82457 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 388701b0-29a9-366e-8628-bc460025f007 | -12.81439 | -44.82198 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11a04c08-d611-35a0-9553-913ca91a4cbb | -12.81435 | -44.82789 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2322e8dc-fe27-34b1-b6fa-b95fd255c49e | -12.814 | -44.82531 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ded7e264-5e30-3bb5-8727-be330f49eafa | -12.81361 | -44.82864 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a973fb0-9a39-3a12-88e2-c27a91d401af | -12.81269 | -44.84114 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a0df6d0-b6fe-3425-88d1-f1f366548ebc | -12.81244 | -44.83858 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 264a130f-b271-3de4-b933-e3fbf2d4e064 | -12.81227 | -44.84444 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab097d8c-b4c8-3bf6-9ee4-f636c7159f78 | -12.81204 | -44.84191 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8b8e8987-2622-3888-bbcc-c7e0a320456a | -12.81186 | -44.84775 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e86da37b-3366-3423-ad25-a5d4a1ea168b | -12.81165 | -44.84521 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| faa0539e-a26a-36a8-a221-8354d5f527bc | -12.81144 | -44.85105 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 68d185a3-3168-3011-9f8d-efe6b3be6853 | -12.81126 | -44.84853 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d646dc08-d8f5-3f3a-bf22-a869aa7116d9 | -12.81031 | -44.81725 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ec77996b-c6a7-3669-991c-0ae07f65a3c4 | -12.80989 | -44.82058 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 54a33c93-c73e-359b-af0d-1eaac72963a7 | -12.80948 | -44.8239 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dc52084e-fef2-3cc5-917b-4e6ba652692e | -12.80906 | -44.82722 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8952d016-9898-3a58-a6d6-cac3a9466b42 | -12.80865 | -44.83053 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09b7dc95-8ef2-36ec-b24d-54dcb96b7be0 | -12.80823 | -44.83384 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74eacc96-66b6-38cd-8ed7-e95ed11490ae | -12.8074 | -44.84045 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e6d8cbe-f3d6-3c91-b54c-f449045b1c89 | -12.80699 | -44.84377 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04bcfee3-b857-3b65-9b57-644d5445b539 | -12.8046 | -44.8199 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8ae60390-27a9-3c46-a531-7e82a4c36b39 | -12.80419 | -44.82322 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4f408e4d-0ef7-332e-a699-f7e8404b55b5 | -12.79973 | -44.8159 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cef3aa47-2288-3cbe-83e0-f9c5e0e01b29 | -12.79931 | -44.81921 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1cd9645b-14dc-3fc6-9912-c5e7ed2fde5a | -12.7989 | -44.82254 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3e3402d-5b33-3b2d-843a-d4658fc38091 | -12.79485 | -44.81188 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2168a841-4ed7-37f1-9936-1fa30aec33d7 | -12.79444 | -44.8152 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79dac25e-3cc9-307c-b2a0-220fc5d99bcd | -12.79402 | -44.81853 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da113024-51ce-376a-afb1-80687712063b | -12.79361 | -44.82185 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6588258-f776-3af9-960e-ce0c01eaf2c7 | -14.51917 | -44.97072 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93a02979-d5f8-3479-9d76-0aa95ad423bc | -14.51337 | -44.97373 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b220b8d5-2124-36a2-af7f-675f11f2dff2 | -14.51292 | -44.97745 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8255323-2172-3f30-9ed1-adff431c54ae | -14.51143 | -44.97235 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42120eb8-1d28-3e85-a21c-92c2b594bbe4 | -14.51101 | -44.97608 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0f5a87d-d3c3-30c4-9658-3edb7d47aac9 | -14.508 | -44.97314 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c46406a3-e0f3-3193-8af5-898304588379 | -14.50756 | -44.97684 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d052696d-bdee-3723-b75c-1641d7478a39 | -14.48067 | -45.24208 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee824240-8e0a-35c3-bc6a-1350d802d762 | -14.48064 | -45.24278 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8978090-713b-388e-b792-1c939e4b2e11 | -14.4803 | -45.24531 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 604c482e-77d2-32c1-95e9-5380a28afbd2 | -14.48025 | -45.246 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85dccb06-0d0a-3933-b486-3b7ab71f08e6 | -14.47595 | -45.10441 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f8de379-4c78-3fc4-a16d-ffc0a0c41e00 | -14.47554 | -45.10787 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39c4289f-7b30-3b08-9c84-75c38e5b94dd | -14.4754 | -45.24199 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d3da2f7-21f4-3843-964e-79638792a380 | -14.475 | -45.24527 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82d20105-1081-3afb-b02c-f249ee4087c3 | -14.39542 | -45.19544 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1f8553b-7181-3590-bf46-e5b6fae0666b | -14.38939 | -45.20132 | 2024-09-29 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84e209d3-862a-3886-8770-16cd4487995b | -14.18544 | -44.24228 | 2024-09-29 04:51:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25aa1a9c-2d6f-394b-a3e8-b02372e0a37c | -14.185 | -44.24615 | 2024-09-29 04:51:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 597c4fc7-8646-3dce-be20-8c9ff069c4ff | -15.88525 | -45.04571 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2e827ef-52d1-35a6-b79f-c9bc8750d7fe | -15.88486 | -45.0493 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b8af973-c283-3af4-9c4d-4654ab862420 | -15.88447 | -45.0529 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a2a4c68-b475-3d9f-9e5c-4a0e7f5452ad | -15.88363 | -45.04598 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfb5848a-82c3-3403-8967-272c3726e3b9 | -15.88322 | -45.04956 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9229f16-9324-3058-b8ac-6df16ccfc172 | -15.8828 | -45.05315 | 2024-09-29 04:51:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README54.md)
