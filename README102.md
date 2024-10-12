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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c974a311-9687-3f66-99ed-f723329052f0 | -7.82859 | -54.72177 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45c262a5-5de1-30ba-b0d3-0612658d1e1b | -7.82803 | -54.72575 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69b870cb-484d-3907-ad96-e5323c6e18f4 | -7.82748 | -54.72971 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eade0aa-c758-3513-bcb7-e1881b23d46c | -7.8265 | -54.72309 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed12f22e-0525-3acc-8a96-1cb318fe2adb | -7.82592 | -54.72708 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44f2e9ad-fddc-3d46-9e5e-ee5867c4a4ff | -7.82534 | -54.73101 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c568387b-11bd-3d90-a819-314aaca2b581 | -8.44084 | -55.4668 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 372cbac5-3744-36e6-9302-eb9520553d16 | -8.43776 | -55.45881 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eefb822a-cf9e-3a34-bed7-8e0e46ea5b81 | -8.43723 | -55.46249 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1587cd8-7be0-3e68-b278-8a0e0e968f3b | -8.43669 | -55.46622 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6f39734-e8d7-3dcc-b425-f181fa50d068 | -8.43615 | -55.46995 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f7e2e32-14f4-3658-be5f-2a67bd7e296c | -8.43361 | -55.45823 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f976936-5af7-35e3-bc13-8d2d401b31a6 | -8.43307 | -55.46193 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94c4b8ea-de16-3ce0-8e53-f18636c47ff8 | -8.43254 | -55.46566 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9731633-d6fa-3c03-a4b4-4f56e14d2e6e | -8.432 | -55.46939 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef70c56f-55ea-3df3-aae4-02186f892e58 | -8.42946 | -55.45766 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6bde8a7-2b05-3f52-be9f-d97e396db231 | -8.42892 | -55.46137 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09e77d2d-4b6b-3abd-85af-29ee77d555cd | -8.42839 | -55.4651 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c64032d0-237f-3260-bff9-57fe8703fda0 | -8.42785 | -55.46883 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cd046cb9-d8ff-3d2e-b619-0afab2cc68b7 | -8.42731 | -55.47256 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6fb879f8-4b29-3a50-939c-1b67203a662a | -8.42531 | -55.45707 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| adafa024-50c1-3d83-80f5-00dd81c6b37c | -8.42477 | -55.4608 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e9bee7e-80d4-38b6-b215-b98614ef5683 | -8.42424 | -55.46452 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f30e2fb-3be2-3883-8db7-038d7f125b6f | -8.4237 | -55.46825 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f25c430c-34d5-30db-876a-307413fa8931 | -8.42317 | -55.47197 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d651449-25bd-3f92-8214-c715a84da240 | -8.42062 | -55.46021 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8e357ee-d50c-3fab-b1bf-848bdb102565 | -8.42009 | -55.46393 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 095f4272-b561-36e9-9524-9b1b8f483f3c | -8.41956 | -55.46764 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec0ce360-d8ca-363a-9314-e45c666104a0 | -8.2945 | -55.38099 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc5d1b8-a174-3fc9-a95d-350a86fbb56c | -8.29087 | -55.37663 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bed0a45-c64c-3c54-9f39-cfbea1e118a9 | -8.29034 | -55.38039 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b96c79b8-065e-3924-b612-a6c52b6a8aa7 | -8.28981 | -55.38414 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91f2a08a-2fb5-3f7e-aedb-6cf42c1d0c1d | -8.28724 | -55.37224 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fd367e3-55fc-307e-a39f-e30aedb7109e | -8.28671 | -55.37601 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccddcf13-1001-33cd-995a-69a905a489f7 | -8.28513 | -55.38726 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1dd2f24-41d5-3369-a71a-d00d84b98354 | -8.28308 | -55.37161 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ad73355-cf04-38cb-9af9-0843ec7ce25d | -8.28256 | -55.37538 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22a21377-78c0-35ce-806b-58edc9a343a6 | -8.2784 | -55.37474 | 2024-10-12 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2c3913c-bce7-3549-92ab-c24588071263 | -8.11262 | -55.08577 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0629d3c-13f3-3458-b5cd-4ba18b77160d | -8.1084 | -55.08509 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d85a6727-cfd9-33d6-ab4c-fe601324074f | -9.70057 | -56.39601 | 2024-10-12 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be4a9b5a-fb48-35dc-9fa8-93e9f1083ccf | -9.95988 | -55.33166 | 2024-10-12 05:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3544f91-1da4-3217-8851-744d1909f26b | -9.57858 | -55.80441 | 2024-10-12 05:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 59cec9e5-7684-3af9-93cc-343a4db7e3ca | -9.57499 | -55.80011 | 2024-10-12 05:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b5ef57aa-584b-3805-b6c5-1d8dafdfb355 | -9.57446 | -55.80381 | 2024-10-12 05:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 002a0c42-7287-3567-b916-4aaf1e43b714 | -9.57086 | -55.79955 | 2024-10-12 05:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 08461028-a551-3bca-92fb-57b461e06df9 | -9.57034 | -55.80322 | 2024-10-12 05:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c488c206-6bd7-31df-855f-60370119aae4 | -14.85939 | -57.47071 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d598e83-ad34-3248-a490-a7d0f7484a98 | -14.85868 | -57.47602 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4253ec64-70c6-359f-86fa-0f1e283dbc25 | -14.85733 | -57.47465 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f150f4cd-dca3-34af-87d9-5ba700c36daf | -14.33305 | -57.57308 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d451901-8d03-3fb9-b2a1-17d520a4142a | -14.32551 | -57.59921 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33189a96-aac1-3db2-b702-259747fee3f4 | -14.32227 | -57.59359 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a69459d-bca5-3292-a3cd-b80bb05a1d14 | -14.32159 | -57.59862 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6bfe4f34-ae86-38ec-96ca-809ea7efe772 | -14.31903 | -57.58795 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e19782d-1205-3b03-856e-2e9d257fea35 | -14.31834 | -57.59301 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4fcfa8e4-f81b-341c-8a27-e1e179d711f4 | -14.31547 | -57.55899 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68c11662-78a3-3786-afff-4ce8853fde48 | -14.3151 | -57.5874 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 873ea776-9a83-36be-be4f-6777a116744f | -14.31476 | -57.56397 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7a0554f-d665-381d-976e-a5c4bab92676 | -14.3147 | -57.56055 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 03b1c77c-4021-395a-a678-17641e90482e | -14.31442 | -57.59243 | 2024-10-12 05:23:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb9d4d29-6261-3347-8664-7962bfc4e31d | -16.18633 | -57.4178 | 2024-10-12 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 412beafc-93f5-396d-8419-61d17aa28c90 | -16.18225 | -57.4173 | 2024-10-12 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a5a7dca-a598-36c8-b188-82092fe5e622 | -16.02518 | -57.51239 | 2024-10-12 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de556e68-46c5-3582-8940-bf521e620089 | -16.02471 | -57.51587 | 2024-10-12 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac7b7070-00b1-3792-b4e5-e35d4cf6caa2 | -15.8652 | -57.47789 | 2024-10-12 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2640ea5d-7e2f-34da-84a3-f61605931183 | -15.86348 | -57.45978 | 2024-10-12 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1f77aa7-a21f-37f0-b909-44e30e8a67ca | -15.85946 | -57.45906 | 2024-10-12 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 781dc1cd-5fbb-38ea-808f-8b1184a53cc3 | -15.85544 | -57.45833 | 2024-10-12 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0fd9fe2-31a1-3555-b7ff-0faa6e5612f7 | -3.59007 | -55.56643 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83c04486-5607-3542-ba2c-ea6feefe6578 | -3.58697 | -55.56099 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae96fb6c-12ea-3794-9f8e-d567d08d4718 | -3.58622 | -55.56584 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0228b3be-7394-3a3d-8bfe-c9fc45dacf81 | -3.5243 | -55.45373 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a45ff45-ae25-3f9f-a3c8-4007c121f4da | -3.52309 | -55.45674 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fc97472-5af1-3d0b-9749-387e77a447e5 | -3.52043 | -55.45313 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0724b10c-71d5-3d22-9ca9-78103542c390 | -3.51375 | -55.44046 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46a5f3b6-73d1-30cf-9406-1422af8b78a5 | -3.513 | -55.44527 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9683472a-bdc7-3a0a-b856-4fd38b587cf2 | -3.50987 | -55.4399 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a489746-d6e1-31f9-964f-236b5db07da2 | -3.50912 | -55.44472 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ce70c0c-5229-3243-a516-ea247fd461b2 | -3.50838 | -55.44952 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e23506d-fcf1-3588-a2e1-79f59fb9ced5 | -3.50451 | -55.44897 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9af5aaad-677b-31b8-b768-42bcccf09dd8 | -4.97766 | -56.19376 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c99ab6f4-6ebe-3bfe-b20b-8844bba7d538 | -4.94182 | -56.01815 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6abac8d7-5cc4-3793-be21-31e0eae47f89 | -4.90191 | -55.90547 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cb7c11f-42af-365a-a85b-f019c33422c0 | -4.89878 | -55.90017 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1405b7f6-7457-32d0-bbd8-820e75abdf72 | -4.89805 | -55.90502 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06e35906-a348-336c-ae25-e5f7bc7ec044 | -4.89666 | -55.91432 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 900b0c6a-ae6d-3d9a-a1b0-c3b4fffe576d | -4.89421 | -55.90445 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0fde225-39c4-36e0-a58b-b356e725b1f3 | -4.86355 | -56.00506 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbf0cb84-0e5b-305a-97e9-bee92556566f | -4.85267 | -56.18122 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 177f7d57-90a7-36ac-a050-1c722bfcff4b | -4.82539 | -56.15668 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffec8a50-32c6-38de-8454-c0e6b89e9ad1 | -4.82514 | -56.15895 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbe7d142-e3d5-38d7-aee1-c44313c7c667 | -4.81028 | -56.15453 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8335073-d5b7-3dc1-8a42-4a281fd63c03 | -4.80956 | -56.15917 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26f6dcff-b746-3a73-a6b7-9a836687995a | -4.80651 | -56.1539 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8648617c-b481-371f-b2bf-aaaff50ac331 | -4.72326 | -56.03851 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd446f3c-850c-3c55-bb3b-d83d3bf43054 | -4.64574 | -56.01916 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cc972d9-47fa-3250-9f89-bd817bf0a9c2 | -4.60801 | -56.11659 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13e2dcfe-b3cf-31d8-abae-69760eedbd87 | -4.6077 | -56.11806 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ac764e1-876a-3993-8fb0-491ff61a6d2b | -4.60734 | -56.12114 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README103.md)
