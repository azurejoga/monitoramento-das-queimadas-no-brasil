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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0db369d5-7337-3526-a108-471edea6354d | -4.68373 | -47.87344 | 2024-10-10 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2b60a5c-6def-3703-911c-e842b7e48424 | -4.66867 | -48.58252 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 386de105-bc94-3848-9ca7-b89b05e7ebb3 | -3.94059 | -47.95851 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1663abf5-8fb9-3d06-8a12-702c1116b70c | -3.91533 | -48.34511 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0d3e91b6-6ae1-31e9-826c-35889620f99e | -3.91453 | -48.35 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3f0d115a-b935-30b1-89d8-66a2f8887551 | -3.91372 | -48.35488 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76389051-ec7e-3534-954d-afc56a44f195 | -3.91226 | -48.33952 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2f06d5f6-41bc-3d2e-8da5-0e3bb4dea546 | -3.91145 | -48.34443 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 415a046d-799a-3b31-b89d-d832303b483e | -3.91065 | -48.34933 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 85c78d84-8873-3653-9d97-d8bb28a86d82 | -3.90984 | -48.35423 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f27b8826-6a00-39dd-ab9f-88c1601a27ce | -3.90838 | -48.33888 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f014bafc-c447-3415-b585-f00527c2c4d5 | -3.90758 | -48.34374 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bd79afbb-f7a8-3b48-b8ad-836116a64c7c | -3.9037 | -48.34307 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6859a922-846a-3526-8cd0-f2fc6970a136 | -3.89277 | -48.35839 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e32759e-f215-33ef-b586-1e208889e404 | -3.89268 | -48.36146 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f2ca669-ef76-3a06-8852-d048485c8a50 | -3.89198 | -48.36333 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86036639-d1be-397b-8f75-2c4440e42917 | -3.72649 | -48.34949 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f60026b-3336-3959-a9c4-12737f552ac4 | -3.72568 | -48.35451 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ecf9bf3-66f2-3803-8093-11db96b9a100 | -3.72261 | -48.34879 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9826509-1c83-36c4-b12f-ac5c0f578fad | -5.06766 | -48.44941 | 2024-10-10 04:17:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e206c157-76b1-3ac5-98d9-fcd05450e121 | -5.06663 | -48.44733 | 2024-10-10 04:17:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4bff530-950a-31bf-877e-a18a1128d986 | -4.98905 | -48.41483 | 2024-10-10 04:17:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2cd089b-2261-3bbb-8c5f-a8d2b4852615 | -4.89571 | -48.5645 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 419308a7-ef74-31b3-8be2-e5321e0309f3 | -4.60305 | -48.06028 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 409d6f58-d6b8-3654-965e-4989dd857915 | -4.6023 | -48.06483 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03ee904e-bf20-334a-a846-43802e674c21 | -4.59852 | -48.0642 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cc6a61c-e26a-3edd-b6d8-ad87ef7ea749 | -4.57638 | -48.01075 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 601cea03-02f0-308a-b6e6-206f9fc84493 | -4.52707 | -49.06776 | 2024-10-10 04:17:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c10e2c4-ab9f-3a08-aa1a-606c6ecdeb9c | -4.48274 | -48.10863 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9fa1ecf5-6028-3408-be2f-0d537f24c4e6 | -4.38532 | -48.62372 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e94d4160-a2b5-3536-8ff4-8dbe56cd695f | -4.38194 | -48.62579 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f11541d9-c1c0-366b-b36d-7ae38caeb64e | -4.3814 | -48.62304 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb0ccdcb-46e0-3b41-9206-ffd470a78b2a | -4.32075 | -48.01553 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e016bdd5-93a7-3005-8735-1936676761d7 | -4.2875 | -48.63593 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e50a617e-7dc8-35bb-b36c-d29a213cdf69 | -4.2813 | -48.62467 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a389e246-64cb-30e4-b10e-d71299f1856a | -4.20493 | -48.13697 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48a6cb87-c241-3502-a86a-48901355f4c3 | -4.1812 | -48.01889 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7ad8018-65e4-32e0-98f2-02540067c7be | -4.17892 | -48.00911 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57142c92-8158-3a28-af80-7477237f6135 | -4.16273 | -48.62189 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb03ae90-4e17-3870-9efc-f30d2c99ad4c | -4.16195 | -48.61858 | 2024-10-10 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99a95c8e-40c9-3ea4-b409-31cdaa3ca9d2 | -4.14737 | -47.87064 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2f00378-6739-305f-be1d-8a07a2573189 | -4.14664 | -47.87511 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20c45de2-1556-3951-a94f-f53220e248c6 | -4.14359 | -47.87007 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea9a2a26-740c-3ac1-af06-9b25071a13ee | -4.14287 | -47.87456 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12d7bf31-8232-31e1-89d2-06686f27ce98 | -4.1198 | -49.24685 | 2024-10-10 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| de7acd06-7c96-3186-8c76-c588bf3309ab | -4.11642 | -48.26837 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 99719646-42a7-31ae-a1c0-cabf7c7ed572 | -4.11562 | -48.27322 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d2241fa2-2565-3824-9794-5cdbe4334d70 | -4.11534 | -48.26572 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 3121707d-075c-3a87-87bb-cea3090d8d9e | -4.11457 | -48.2706 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 9c14a737-ae33-3aa2-a0a7-5391bf8eba59 | -4.11257 | -48.26773 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 50c333d7-f0fc-35c7-824e-bbaf14cf6b72 | -4.11176 | -48.27258 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 080509c8-f750-30de-9e70-5acfd9ccaa8c | -4.11149 | -48.26508 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| ab168357-132b-3a77-970e-306d6cee12a8 | -4.11071 | -48.26996 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| d23e41cc-8884-36b0-9ee6-eab7efe100d1 | -4.10841 | -48.25961 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 12b2a427-d4ca-32d5-ad55-5e1bde71f966 | -4.1082 | -49.06364 | 2024-10-10 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e24aeb3-e047-34fe-8945-5aa9a916eea7 | -4.10763 | -48.26447 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 184d7e69-5d39-37ad-8238-f81322655110 | -4.1076 | -49.06721 | 2024-10-10 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 23826283-9a3f-3076-a75e-923b2b721fc0 | -4.10686 | -48.26934 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| d329a678-25ae-3b59-8af7-7d79f2401571 | -4.10608 | -48.27418 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 84bed968-b93f-304b-b765-dcb67ad25b95 | -4.10533 | -48.25414 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 4ac469d0-22e8-30ff-857a-0712a2790e6b | -4.10455 | -48.259 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| afeeb8a1-b9ff-383b-b178-06077add4d7a | -4.10378 | -48.26385 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f34f87d6-21dc-3e7d-be07-e65227eb0645 | -4.10354 | -49.06657 | 2024-10-10 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 65931e0c-a7ab-3bb2-8f40-4574a7f33db6 | -4.103 | -48.26869 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c36c627f-a793-36d4-bcb0-da13b5d6af9b | -4.10223 | -48.27349 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 10e9f25d-2181-3b69-8025-e0defc681b3b | -4.10148 | -48.25352 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| afef16a1-4f11-3718-b203-8863b080cdac | -4.1007 | -48.25834 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| c5fd7b02-a86a-3e0c-bd05-c926605ff812 | -4.09993 | -48.26316 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7ed44c03-3841-34c7-ac83-f9300d528a93 | -4.09916 | -48.26796 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| da731df9-2976-3c74-a827-493e9cc84379 | -4.09839 | -48.27276 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 0037c04a-bc42-3998-90ab-6b1c6777427a | -4.09838 | -48.24821 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9028b6fd-1663-31cd-b27f-551687e9154c | -4.09762 | -48.2529 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a393f929-f159-34c6-9bbf-b8b63ca91c2a | -4.09686 | -48.25768 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88e35487-1e4c-33e4-9021-0fe45257c3c8 | -4.09609 | -48.26248 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4255b7bf-42c7-3972-b638-e775c17ed46e | -4.09532 | -48.26726 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 443ea805-1808-3530-956e-c9772ef3a6fe | -4.09452 | -48.24763 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37adfcad-96e8-3cd0-9a4d-f623a77491b3 | -4.09377 | -48.2523 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6e99c59-7266-383c-b3d3-25d02c5cc4c1 | -4.08606 | -48.27561 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40a33727-bf09-3dde-931a-56a509c1d322 | -4.08528 | -48.28043 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6028a3d-440c-3ccc-a79d-31c6d1e7172a | -4.07681 | -48.11391 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d893719e-deed-3a18-9f61-be2f9a114fb7 | -4.07605 | -48.11854 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 728d7b02-7781-366c-8707-4b214a0b13ea | -4.05434 | -47.92349 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e2d9c6d-6243-3f82-8fe6-6486313ebb0b | -4.05056 | -47.92286 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04a0c446-35c3-3477-af38-f23009065330 | -4.04983 | -47.92743 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9edae1ea-d370-314f-be0b-b894ba266a55 | -4.04606 | -47.92679 | 2024-10-10 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e0ff652-9ac8-3bc6-bc3f-25041f714b88 | -4.9577 | -49.05701 | 2024-10-10 04:17:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ae6663c-b718-37ca-b997-4f6b31020fca | -4.95685 | -49.05545 | 2024-10-10 04:17:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b97fb59-6a2f-33e5-a48d-0150563d5c64 | -4.95601 | -49.06063 | 2024-10-10 04:17:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e456bfb-3875-390c-8e29-3a7cf185e78c | -5.77549 | -49.01304 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 25c5f2cc-5526-3a13-ae83-834acbc4c4f8 | -5.75498 | -49.26065 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 816a2997-99a0-3814-8f4b-723049de3a4d | -5.60017 | -49.03626 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7f8d21f-7565-3d80-8aca-b6ba9f891ef5 | -5.52334 | -48.36051 | 2024-10-10 04:17:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a879f81c-b67c-3962-8457-78cb0b9a86a8 | -5.45581 | -48.2574 | 2024-10-10 04:17:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1424950-a674-30a8-b74f-a190a182f42c | -5.45506 | -48.26198 | 2024-10-10 04:17:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 776e1e85-07ab-3efc-bd62-22eae9f930e2 | -6.03865 | -48.21218 | 2024-10-10 04:17:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42ff6eaf-0981-3c9e-8ff9-c5990558174b | -5.3249 | -48.01691 | 2024-10-10 04:17:00 | NPP-375D | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cbb9a15-5c0e-3ea9-90e9-c453c19f6c9b | -5.32418 | -48.0214 | 2024-10-10 04:17:00 | NPP-375D | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d1de775-7af8-36f9-81bd-53e4ce913b45 | -5.32116 | -48.01633 | 2024-10-10 04:17:00 | NPP-375D | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be0cbe45-eeea-317d-9ea3-d674803179e9 | -5.22547 | -47.9615 | 2024-10-10 04:17:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 393f6d4b-bda7-3efa-874d-3c4a99ecdf29 | -5.22475 | -47.96598 | 2024-10-10 04:17:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
