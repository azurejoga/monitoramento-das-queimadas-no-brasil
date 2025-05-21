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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ac49c2a-14f4-35fe-8c25-12b50437a558 | -12.30188 | -52.48764 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1bce91e1-27f4-3e46-87a6-5ee842b6d858 | -14.15923 | -45.47363 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6025257-f7db-34dc-84fa-c7569223e852 | -11.67114 | -54.94432 | 2025-05-21 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 829e2891-ec24-35ac-b3b3-d552d0ee21f0 | -14.67568 | -45.11404 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c11f42bc-0b8f-3072-89fa-71ca6bc6f82c | -11.69385 | -47.79827 | 2025-05-21 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7cb15ab-ed17-336b-a1d9-4bd7bf1dfda0 | -12.03959 | -54.96837 | 2025-05-21 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0da80b18-c883-3c19-93c0-f2c8eb826fc9 | -10.68111 | -57.60251 | 2025-05-21 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0bdc816-6416-306a-aa41-27db0ee70731 | -14.16293 | -45.47823 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a519060-d41d-3eb7-98a2-f03927b612cf | -14.0415 | -50.51629 | 2025-05-21 04:42:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d45e18a7-37cd-3201-9e80-fc0fe6ef00de | -12.42784 | -43.72738 | 2025-05-21 04:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 15fa37df-9651-3271-8b93-236ae1c3a8cb | -14.01444 | -55.13471 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2a87f00-bce1-3311-9628-71df5b21749c | -12.49919 | -57.22223 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ab6cfad-6556-3b8f-955c-8dae4ecf6f4e | -11.57458 | -54.56499 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dae1e799-df96-39df-94ed-055c4016f0d1 | -13.49473 | -55.66303 | 2025-05-21 04:42:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fe75eac-e382-3d40-a929-82d56b0e2720 | -12.13115 | -54.65981 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cebbbbd5-29d6-3ab6-ae57-1465e354197e | -14.02135 | -53.01658 | 2025-05-21 04:42:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4989dc8d-6de5-3585-8459-a2c59bbeb039 | -14.02863 | -55.14201 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60a153b8-83c7-3872-8c6d-771327a4e20c | -16.13904 | -45.94876 | 2025-05-21 04:42:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0dfe57b5-e41e-3f48-8e39-bf7292023c92 | -14.04644 | -56.06496 | 2025-05-21 04:42:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f6e706a-bf9b-3f8d-8c9a-252d4d693617 | -12.29104 | -52.48962 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b967be95-eefd-3aa7-8a93-73beb8313ecf | -14.1714 | -45.47945 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 199e93a1-35d5-3367-9d58-ecae6beeb2da | -10.77082 | -49.0365 | 2025-05-21 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ff3b036-f399-30fa-ad87-0ab5f2a526cc | -12.2997 | -52.47963 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 599c4250-84d1-387c-a5df-79455a7c2c5d | -12.4325 | -43.72799 | 2025-05-21 04:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e0f22042-fcd1-3b83-a279-fb869db1c011 | -11.64778 | -48.10647 | 2025-05-21 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8991004-2738-3aec-8d30-dc0cc741be36 | -10.34494 | -51.69538 | 2025-05-21 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0be49700-15b9-350b-8392-849ffac699b5 | -11.66816 | -54.93879 | 2025-05-21 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37df6d4d-b317-3e0f-a262-a3fd79273eff | -16.04281 | -43.80477 | 2025-05-21 04:42:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 573296a3-5dea-33fd-b9bf-f7cf2fb1d178 | -14.16031 | -45.46564 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cb4e797-03f8-3049-9a4b-e9f9b3024fd9 | -13.66771 | -53.93615 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b7e1a1e6-3809-311c-8fa0-c846e529be3f | -13.6109 | -55.45573 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8a28ee11-6e92-38b0-932c-9227262c1294 | -12.36768 | -49.97415 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ec55ef0-a81e-3a64-a5be-339374415333 | -12.2935 | -52.47476 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 014fd383-a166-3183-b63a-afc1243baad6 | -12.36378 | -49.9772 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cdd4b3db-33bf-3cfa-ad6e-fe0b26dd3000 | -12.13153 | -54.65775 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdc9c1f3-74cb-3f22-805d-a5bf16b1d289 | -11.08657 | -54.77246 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 24f25a8b-6962-323d-941c-48ab528eed53 | -11.08192 | -54.77656 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fa1ad351-25c7-39cd-a472-5e59457b58b6 | -16.04768 | -43.80537 | 2025-05-21 04:42:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe102e1a-4190-30d0-8aef-65ce438ef8eb | -13.66677 | -53.9348 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8a6fcb09-774f-32cd-94b1-a4dbf97affd0 | -10.62307 | -51.79327 | 2025-05-21 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51a8bee0-e8ca-3aa4-b071-a42585fc59e1 | -10.07508 | -55.4931 | 2025-05-21 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67e03b30-07a3-3048-be87-32eb1dfc572a | -9.29086 | -57.55171 | 2025-05-21 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0539867-d359-3339-8a76-5687253d63a5 | -12.40935 | -52.14994 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd9e85ed-5cbe-3d8d-a1b4-e1c23266b9c5 | -11.88205 | -56.41452 | 2025-05-21 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae3a960-f29b-3224-b428-89462c6d9022 | -11.0789 | -54.77116 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e465ff9e-e2af-3632-83ad-9e16f59a9033 | -13.66484 | -53.93147 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9ac562f-0581-3381-84bf-cd5c02541c4a | -11.78378 | -44.28281 | 2025-05-21 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dab528e7-9817-3614-9c34-0c8186b871cc | -11.9215 | -54.41468 | 2025-05-21 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcc81087-f9d3-3cab-ab67-dcd7cf73c196 | -16.03088 | -43.67916 | 2025-05-21 04:42:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c41478f4-3886-3b87-8291-53b03e471644 | -13.61658 | -55.46055 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d49ab48-97e2-3a5c-a101-c8f8337f6639 | -9.41877 | -58.32076 | 2025-05-21 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e322f8b-d229-3937-98a4-20274068fb0c | -14.16609 | -45.48681 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1dee102-0e14-3cb6-a178-918380a6584a | -14.02488 | -55.14132 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6635c67d-42f2-3907-91b2-076c284ffded | -12.29847 | -52.48706 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 00d7e353-87af-3f15-bf05-ea019de753f8 | -12.12171 | -54.67013 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 521f58b9-1ca0-3383-9e09-afe52ce90086 | -12.03112 | -54.97183 | 2025-05-21 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e317b47-c6ab-3d85-af4f-114bad5d30ed | -12.87199 | -43.18032 | 2025-05-21 04:42:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98b2e90c-56a6-34f4-a495-b59c6c245f1e | -12.33732 | -49.95853 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8907d19a-ce6c-3632-97c9-e382d86ecb75 | -12.36042 | -49.97667 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a6df493-39d2-3c31-8dc1-e32089601d3e | -11.1565 | -48.67593 | 2025-05-21 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 157c5ad0-b73f-3017-8a3b-4fbdc7b1f73c | -10.68024 | -57.60726 | 2025-05-21 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc47e857-a804-3d5f-b14c-ba848749b742 | -12.03411 | -54.97733 | 2025-05-21 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25e3f41a-4a99-3fff-8f95-9e73ccad3903 | -13.67126 | -53.93681 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b86a60ab-fb02-3095-b408-f04e5dbcabce | -12.40597 | -52.14938 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58998b71-abdc-3930-975b-1bec7ab17045 | -13.61558 | -55.45153 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| edb6606b-624c-3c5e-9503-d0f4ba098703 | -14.15446 | -45.47701 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fa432f7-bf36-3229-931f-016f2ddd1997 | -11.64838 | -48.10248 | 2025-05-21 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2cf8d069-36fa-35f9-ad32-9aec0a2c3591 | -14.16183 | -50.50204 | 2025-05-21 04:42:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7189dc08-92b5-38b7-8ad8-3af68d6e7db4 | -13.66417 | -53.9355 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61bca4fd-a00c-375b-9262-09f324173340 | -11.08273 | -54.77182 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e705c070-4142-3599-a926-6c5d10deb29c | -12.50279 | -57.22728 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82d91412-7ce0-3d9d-bc6f-2d3898099bc4 | -12.33677 | -49.96212 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0affd1ac-d24a-3379-b48e-dc2adb583aef | -12.34068 | -49.95907 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87102f2e-b226-33bf-8092-d47060f4f863 | -14.03815 | -50.51575 | 2025-05-21 04:42:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1a3d8d7-ea9c-376e-8d13-177bd3acc18d | -14.04662 | -45.5114 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa558ef4-c278-382a-a082-e0377d6bcb59 | -12.35963 | -54.52136 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 506e0901-19b7-3e44-a5e8-b17e58454ce0 | -10.68661 | -57.59856 | 2025-05-21 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e4b4611-2031-3172-af24-0f62482c29bb | -14.1587 | -45.47762 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bbbc20f-54d5-37e0-b40c-226c260e1836 | -14.69326 | -45.11417 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| babcc5c5-779d-32c0-9e2a-765a916ed11b | -14.01731 | -53.01976 | 2025-05-21 04:42:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c73e8b74-ef8b-3172-b2d5-283f85548eac | -12.47335 | -57.19074 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a6ee748-5c0f-3c2e-9eec-6cc558aeb16e | -14.155 | -45.47302 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2ce4264-fbdd-3488-b2e1-1768e458cf36 | -11.15594 | -48.6797 | 2025-05-21 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5fb458d-28e2-3249-9084-e6696e5e5dab | -10.65491 | -59.28786 | 2025-05-21 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b4d99b57-2399-33aa-95b5-a65f24b0965b | -13.66607 | -53.93885 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f1339868-9ebf-3df4-b193-221394e67efc | -9.41382 | -58.3198 | 2025-05-21 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b07d291f-7237-3ee9-87b6-941c223af7c1 | -12.28525 | -52.485 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ccd4a6e-f934-362f-8727-d5f489035c94 | -12.28948 | -52.47791 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc07b1cf-bafe-3ca9-8e3e-9e591293b3a3 | -14.68014 | -45.11237 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86bd9033-52f5-37f6-a28d-e8c5b14a39a9 | -12.42848 | -43.72249 | 2025-05-21 04:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 50d058f2-a820-30bd-b2ba-f491c4b3be44 | -12.72365 | -54.97401 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ae144410-e1cb-344c-ac6f-12678c1a4bfd | -13.66838 | -53.93213 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 56369e7c-0fd0-3071-8bde-25390aedb233 | -15.07957 | -48.9425 | 2025-05-21 04:42:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5adabee-6bd0-38b7-aea8-b77e7917ee6e | -12.68647 | -58.12895 | 2025-05-21 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d270bd20-c94b-3e5f-8a70-1fe0521a9a03 | -12.47413 | -57.18652 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9f80868-8c9d-3c72-98c3-6d5ec3de5169 | -14.01855 | -53.01221 | 2025-05-21 04:42:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae2f1193-fe22-3021-9779-14a03e6b69d7 | -11.44598 | -54.09035 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1237e05-6dc4-36e0-8b64-00fc48c42903 | -11.57755 | -54.57026 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 743e4650-8438-3d9e-aaf0-eab57891157d | -12.50357 | -57.22301 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27414e91-7370-3ea3-b59a-4fe46a6e6899 | -14.17086 | -45.48344 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
