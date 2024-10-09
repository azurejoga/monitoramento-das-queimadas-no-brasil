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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cbcfb47-d3f6-30d7-9774-0b7d50dfefb5 | -18.05939 | -42.10826 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1809e0fd-3e57-3460-b1e0-b9f669d8bb02 | -18.059 | -42.11198 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 37c5d4f0-e064-3a84-a9ea-81588afa3eb9 | -18.0118 | -42.13604 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 40f073e6-923c-3286-9035-a3fc843afb6e | -18.0066 | -42.13253 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7d7f1094-2d80-325d-8f54-73a207f34f96 | -18.00626 | -42.13575 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 192c4fed-ad59-3c28-aeb1-c8ad42209872 | -18.0059 | -42.13912 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2ee53767-9cc9-3f85-b892-5806f595e69c | -18.0011 | -42.13188 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a2b466c4-80f6-363a-ba35-882b7aae95cf | -18.00076 | -42.13512 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3ae557ba-e61e-3f8c-b911-8b0f7ed58514 | -18.0004 | -42.13848 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5fcae200-57bd-38d6-bac3-b347ea80c113 | -17.99567 | -42.13052 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d4348012-b543-39c9-b796-801aaf19d180 | -17.99529 | -42.13412 | 2024-10-09 04:40:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1ddc9e06-95ef-379d-ba32-989404c6706d | -17.89297 | -41.42769 | 2024-10-09 04:40:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f79c89a3-dbe5-305e-88be-c53eb1193430 | -17.8925 | -41.43211 | 2024-10-09 04:40:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1937f932-4d24-33db-936b-39b2c1a6f08d | -17.89168 | -41.43995 | 2024-10-09 04:40:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 41ae4e4f-e74f-3f41-8e86-55b3b1c55d6c | -17.89131 | -41.44342 | 2024-10-09 04:40:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 26540453-a275-3a21-bb1d-329599bd9c00 | -17.88732 | -41.42604 | 2024-10-09 04:40:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f9293f49-6395-3ece-b9ef-d68dda77a02e | -17.88687 | -41.43032 | 2024-10-09 04:40:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 61a18ab3-6ed5-3c91-9d69-88793f1170d3 | -17.84165 | -42.22439 | 2024-10-09 04:40:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d6c4f02c-c66d-3117-9eea-339bf0784c9c | -17.76137 | -42.08418 | 2024-10-09 04:40:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b3b129b5-c69d-3b5c-9482-0b85014ef4fe | -17.761 | -42.08775 | 2024-10-09 04:40:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b57faa41-00f5-3a11-b1dc-9597311accf7 | -17.10699 | -41.33103 | 2024-10-09 04:40:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 737a95e1-759b-3228-8122-f4f37ec393b4 | -17.10169 | -41.32622 | 2024-10-09 04:40:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ca7c2e9c-7844-3b7d-af6b-376628a57a0b | -17.10131 | -41.32995 | 2024-10-09 04:40:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 97a2e1bb-3251-3eca-b5b5-a37eb15e5800 | -17.10096 | -41.33324 | 2024-10-09 04:40:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f9e536d9-5f80-386b-877d-059ed0f74990 | -19.27854 | -42.85063 | 2024-10-09 04:40:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5f3cc359-921a-3667-9eea-1dfaf6b05da2 | -19.2782 | -42.85389 | 2024-10-09 04:40:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 60003c48-1c14-3b55-9c6f-ad18b82a2f73 | -19.14329 | -42.71198 | 2024-10-09 04:40:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4f0d25d8-20c6-3c97-98cc-fd65f47e5098 | -19.14292 | -42.71567 | 2024-10-09 04:40:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 086d0c5c-6791-31f7-a5ef-60e8d2eca3ac | -19.14124 | -42.71282 | 2024-10-09 04:40:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 864df484-4403-3e84-8a96-3898d5ec57cf | -19.14081 | -42.71684 | 2024-10-09 04:40:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bfe88036-5aaf-3c31-96ed-0699af47a8b1 | -19.13626 | -42.70858 | 2024-10-09 04:40:00 | NPP-375D | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e017ed76-a6b8-37f6-ad05-db367935ac56 | -19.00727 | -43.21631 | 2024-10-09 04:40:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 588d62b2-c4f9-3fd0-8be3-4c5d1fe338a4 | -19.00694 | -43.21948 | 2024-10-09 04:40:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3e43c036-5c9d-3a0a-afc1-fb61e729ee29 | -19.00209 | -43.21562 | 2024-10-09 04:40:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 996a390d-e63d-37e0-bbe3-2d96faa5683a | -19.00175 | -43.21881 | 2024-10-09 04:40:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4b5d1064-d0c3-3778-9378-46b48efa37a5 | -18.4492 | -43.42756 | 2024-10-09 04:40:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1620792a-9e2b-3ba9-bce0-33a485b762df | -18.44886 | -43.43065 | 2024-10-09 04:40:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| eebc5f8a-f014-3bc8-af95-75e304ec00f1 | -18.4463 | -43.42863 | 2024-10-09 04:40:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 88f097cc-4d43-3507-b4e5-015a02b45d52 | -18.44594 | -43.43174 | 2024-10-09 04:40:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 01720b04-450f-3981-876a-1982978183df | -18.41267 | -42.62343 | 2024-10-09 04:40:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 46883b3a-048c-32c5-9eae-6ec49e7d9c35 | -18.41023 | -42.61695 | 2024-10-09 04:40:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 60c08abe-0086-31b4-9021-24331c234f5c | -18.40984 | -42.62049 | 2024-10-09 04:40:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 05255a30-eab7-310c-8826-100d4f3065d2 | -18.40945 | -42.62407 | 2024-10-09 04:40:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f1fa4285-5b88-345b-a89f-a314d37a84b3 | -18.25726 | -42.55403 | 2024-10-09 04:40:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7ec6be11-ee2e-3c59-9bf0-b4f7f3025d57 | -18.24543 | -42.95909 | 2024-10-09 04:40:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 022143cf-18df-39ed-9c07-64d82b0b6a72 | -18.24018 | -42.95868 | 2024-10-09 04:40:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3cfa6871-3e8d-359c-a0b5-66d37dfdb0cc | -18.23662 | -42.94289 | 2024-10-09 04:40:00 | NPP-375D | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 75e9d4c7-d02f-32fd-bfea-5d690daec5e7 | -18.23627 | -42.94605 | 2024-10-09 04:40:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c2aea693-e352-351b-9e96-6f590155256b | -18.23594 | -42.94905 | 2024-10-09 04:40:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 129b34bc-b74c-30ca-afd2-ba1ab3662f7f | -18.23071 | -42.94838 | 2024-10-09 04:40:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 77420775-80dc-3c31-964b-267d92219801 | -18.18576 | -42.58489 | 2024-10-09 04:40:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e441182-447e-3146-bfff-24e131b83cc7 | -18.18538 | -42.58837 | 2024-10-09 04:40:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8494256e-34ca-3abd-921e-57b70eeaa866 | -18.18045 | -42.58381 | 2024-10-09 04:40:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 39207a13-2481-3941-b4d5-48ae20eb0575 | -18.17513 | -42.58282 | 2024-10-09 04:40:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04c5c30b-4dee-31c8-b81f-3dde17c9d3cb | -9.99576 | -54.842 | 2024-10-09 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09f9b559-e40d-361c-9410-0a5843065038 | -9.99358 | -54.83977 | 2024-10-09 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4f094ce-d93d-37ae-b198-3fef58338068 | -9.97875 | -59.87377 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef7b16d4-ae46-33a3-90ed-dcf039cb1ece | -9.96383 | -55.33636 | 2024-10-09 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 733120cf-19f7-3d90-ad3f-12bce7dc4136 | -9.95911 | -55.33934 | 2024-10-09 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab4f148b-8f99-31f1-8010-1e35b3762318 | -9.95566 | -55.33495 | 2024-10-09 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aecca69-7f8d-39d9-ae7f-dd281268a0c1 | -9.95503 | -55.33863 | 2024-10-09 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d9f4976-ce2f-3cf0-9c8b-10380d268ed0 | -9.95221 | -55.33061 | 2024-10-09 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a6508e8-982a-36bc-b6da-9d7b90acdcc1 | -9.95158 | -55.33426 | 2024-10-09 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f225f99-2ba0-3ea9-9ba4-feb0f69f57ea | -9.94663 | -60.13495 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e81bb328-7788-330f-a994-d4db915ff93c | -9.94591 | -60.13876 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61c48563-f35b-3c54-8437-dd82040b7453 | -9.94518 | -60.14263 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2e99bf6-d5b0-3332-9ffa-57b87c67cdef | -9.93048 | -56.74121 | 2024-10-09 04:40:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2a3746c-77e3-3707-afbe-a825c9b56c77 | -9.92794 | -58.13211 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 074d3af2-9444-34dd-bfbd-7d8ba5752e61 | -9.92402 | -58.12566 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f82e77b8-d72e-3630-87b7-533f93ce37bb | -9.92302 | -58.13121 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f743290c-abf2-3fdc-a11a-5727ef819186 | -9.92201 | -58.13685 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc9c99c8-dc24-3413-b4eb-677eab5ebb5f | -9.9191 | -58.12477 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e3a8793-90de-3c76-8cc2-2f18e5d6f996 | -9.91813 | -60.31664 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4cf36b2-dbd6-3b27-9577-877649e11f06 | -9.9181 | -58.13033 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76df2458-0c8e-3781-a0d1-e9ff37285e1e | -9.91741 | -60.3205 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c430c7da-0d4a-3046-868f-ccfae5c45db1 | -9.91708 | -58.13597 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4005fea3-7cbb-387c-8f1b-8ddf48666ef9 | -9.90187 | -60.30932 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfc3c8db-4ab2-3285-a35b-ba14f7105792 | -9.90111 | -60.31334 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2544aa15-c295-33ec-93b2-a6659e3a68eb | -9.8913 | -60.2112 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f7a5a40-c8d8-36fe-8c6b-79f681ce85ea | -9.89126 | -60.3033 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdb9a1d5-f48d-30a7-ae21-2bb5de5ebec4 | -9.89056 | -60.21507 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17b178ce-d64b-35e0-8602-32291e709a56 | -9.89027 | -60.2471 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ca93adc-25af-36e8-b922-2b1cc93c39ba | -9.88981 | -60.21896 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 505d0043-26c8-33b7-809d-6d226897cf54 | -9.88872 | -60.21153 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 152023ba-252d-3ff4-aaa3-4ed5cf859b99 | -9.888 | -60.21542 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16d5845f-7fcf-3b69-8fa7-b84416e8642e | -9.88727 | -60.21935 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbcc378e-0a37-384e-9cec-cd887f4a1773 | -9.88556 | -60.30233 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5659e983-3a3e-3162-bbc2-18ebc7311161 | -9.88492 | -60.21397 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f3a10cf-dcb4-31c9-9558-be8813a83f0d | -9.8754 | -58.33871 | 2024-10-09 04:40:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79bea08f-ed22-3cdd-84b2-8c0694dc5c94 | -9.8727 | -60.10954 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 115693fe-4e5e-3963-994c-7b6945a0107e | -9.8678 | -60.10471 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4761bb76-f951-3ac4-aa82-2ae6dc583e33 | -9.8671 | -60.10844 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02dbb4da-cf60-3e31-80e3-0d26fc94fbd5 | -9.86098 | -59.83559 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f353e64-a667-3d0b-bbcc-bc86a6496325 | -9.86028 | -59.83925 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89bf93f8-14bd-3591-9e52-83b3b8e8659f | -9.85345 | -60.21259 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71f8fb7c-c52a-3050-9129-c70fcddf9ea7 | -9.85273 | -60.2164 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6774e15d-462a-3c29-9e68-4755498400a8 | -9.81752 | -60.46788 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93dcea20-282d-3fa2-a1c8-2e8dcfc484fe | -9.81271 | -56.41405 | 2024-10-09 04:40:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31b30c1d-e789-3f03-ba71-7c26b473bfc6 | -9.81197 | -56.41831 | 2024-10-09 04:40:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2ba3e50-d193-3bbb-b3e0-204fcdd97d76 | -9.8118 | -60.46663 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README131.md)
