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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbe5303a-855d-3844-b42b-73646c15e3ea | -13.61866 | -51.1748 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dafc657e-1ba6-3418-a0fa-8363fc0616be | -13.61604 | -51.09055 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| fdc128e5-8a04-3bb1-ac5b-d7d2022a2e28 | -13.61483 | -51.09624 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a6a6f82c-dede-30ec-bec8-2f03a7e6df2c | -13.61362 | -51.1019 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| be07ba41-8185-388f-af64-43a0b8244437 | -13.60953 | -51.08909 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0777070f-1573-37f1-b92d-8ad99d312e47 | -13.60424 | -51.08192 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d227809-7823-3ca0-9d86-087e5c8251f5 | -13.59943 | -51.07967 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71b5209e-e65d-3212-92a5-87ec691473b9 | -13.59894 | -51.07478 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f42969e-68e9-3788-b576-9a02940b1fee | -13.59773 | -51.08046 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8fc8043-a347-3c0b-958c-9c281b3569ae | -13.59375 | -51.16302 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8ea172b4-a072-3c4e-bcd1-b384e77c389a | -13.59253 | -51.16877 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1d383d7d-7bcc-3e5f-8ff9-6ac60bd87bf1 | -13.5913 | -51.17453 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a5621cf5-af1d-34b1-a99d-d0c5a011006d | -13.58721 | -51.16158 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 995ee6e1-a100-325b-9bfc-1838ad9cfd40 | -13.58598 | -51.16733 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 001ec26f-21d3-30b3-8e1c-39c7772c02a8 | -13.58475 | -51.17306 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 57048679-8111-387d-b8bf-575b7dc46b4c | -13.58169 | -51.16528 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cf9341ab-e730-3273-be99-6504a36d40e3 | -13.57944 | -51.16584 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df8da82a-9b3c-39fc-b2ef-c14b479d9bb2 | -13.57754 | -51.15228 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2c7f9b0-357b-3245-a27d-e9ae824b036f | -13.57659 | -51.14719 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8b2197e-8d1b-30d7-9579-58e5e7d574a8 | -13.5734 | -51.13927 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf0f6d20-418f-37f3-920a-6a101161843a | -13.57221 | -51.14502 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6beb07d3-8ee5-37c6-8f28-3a8b7cd3a6e6 | -13.57129 | -51.13998 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66764827-415a-3143-9b75-433278fd1852 | -13.57006 | -51.14571 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 040607e9-d0f5-3894-b545-1c3df68b0bf6 | -13.56845 | -51.12138 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56807b99-91a9-3818-a4ae-d467f3939d2a | -13.56687 | -51.13779 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f030906-bb09-3481-81e9-365450114d65 | -13.56599 | -51.13278 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c3942ec3-2bab-3c1d-bbd2-24bcf1be1bda | -13.56393 | -51.1191 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1dc1407b-bce2-3d1e-80c8-a5dd51b6ef5c | -13.56275 | -51.12479 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8dea8d4a-c3b2-3e32-98da-c7278840fa4b | -13.56193 | -51.11988 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f0f4487b-f23d-33af-b8a9-e92d287f0cd0 | -13.56155 | -51.13052 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5814786a-b9ff-389c-9853-d39249f56852 | -13.5607 | -51.12558 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ea07850e-9c82-3f3b-b86c-8e18c21bcf4a | -13.24832 | -51.24017 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6ae9712-de5f-3b56-b36f-1d2ca706e5bd | -13.2454 | -51.23971 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4cd6ce28-2d3e-3040-9dd9-b8fc01922388 | -13.24172 | -51.23864 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1dd4332-aa5d-30a8-909a-4a0aea0929f4 | -13.23512 | -51.2371 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 702941a9-0c27-3338-a51a-aacdbc67edeb | -13.23344 | -51.2307 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 653cd5d4-7dc7-3547-b62a-11abc0a302b4 | -13.23221 | -51.23662 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ef08184-a018-3098-903b-5509c81429b4 | -13.22979 | -51.22969 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 295c242d-9f3a-355d-a5c7-bb6eda5cb06d | -13.22684 | -51.22917 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f7c0f07-f75f-3929-b563-9e7951dd5e68 | -13.22658 | -48.58126 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1620ef64-f1f7-339d-a3c6-daf6e2245246 | -13.22571 | -51.21648 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e59b3fb1-f812-39a9-9b3c-22a6d114e87f | -13.22478 | -48.57982 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21fd300d-7747-3d1b-bba6-3d9e2249774d | -13.22445 | -51.22234 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cfff53c-27a4-3b38-80af-c5c91130919d | -13.224 | -48.58385 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3a2ce91e-4de6-3190-8cf9-7fdff82407b7 | -13.2239 | -51.21008 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| ff0bbbd0-f922-336a-b524-eb393b196190 | -13.22269 | -51.21591 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c73cb6fc-0ce4-35d6-b91b-c5a512cb0d1e | -13.22261 | -48.57185 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00944927-6d76-3a7d-b3b8-b8eb175704c8 | -13.22256 | -48.5612 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59406c5c-93c1-36ce-8acf-7e36c22c637b | -13.22175 | -48.57611 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e9ed43e-41f8-3dc5-8fb8-4af29210ad0d | -13.22146 | -51.2218 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a35a6d10-0e8e-3e37-9880-4a7f2a321951 | -13.2209 | -48.58027 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e7747a8-80fc-3ee9-bff5-7268c22af5c1 | -13.22036 | -51.20918 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a94fa190-ccb7-3dcb-9f86-db9894161e19 | -13.22023 | -51.22768 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1f1376ad-e4af-3d70-a474-a28d4790105f | -13.21995 | -48.5745 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d328dd6a-a7e4-3516-bcab-a4fef0dd6f4e | -13.21991 | -48.55629 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83cb0dcc-43ba-31ca-aa6a-ed5c6ce19ad6 | -13.21911 | -51.21498 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 44ca18d3-a799-35a9-85c3-de0a044caa77 | -13.21911 | -48.57877 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4bb1ad3-3fbe-3093-be30-33dd3413b4f9 | -13.21882 | -48.56162 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bcfd628e-8229-32d7-b60a-202c0594fed0 | -13.21784 | -51.22087 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a666a57b-dc1b-34dc-9180-a68b08e0f96c | -13.21701 | -48.55952 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bad2cbe-c10d-3493-93b3-53a2fffc5b38 | -13.21609 | -51.21439 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 042d619a-76b6-3a2d-870c-5670bb0fa69c | -13.21609 | -48.57499 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b24a37fd-65fc-350c-a338-8b545735fb07 | -13.21524 | -48.57915 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94d4b04d-af9d-3db3-a6a9-2a0cc26e6e63 | -13.21486 | -51.22028 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bcd81d06-1923-3f03-9f5c-ef2fd3719200 | -13.21428 | -48.57343 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 250d9890-2aa3-329e-9aeb-2c80ceb3e07e | -13.21346 | -48.57761 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dfeccf5-9940-3812-9995-ec572b6affbe | -13.21267 | -48.5816 | 2024-10-01 03:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08f7d36c-d19e-3567-a8e3-17a96cbff682 | -13.21251 | -51.2135 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 043da39e-4b9b-3948-aad5-1827ec6af9f2 | -13.21124 | -51.21938 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0974463f-5fb6-36b4-8dcb-15f6f79ef1bf | -13.20949 | -51.21291 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f540f57-d7c0-318e-9042-2b17b9036bf2 | -13.20825 | -51.21881 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e151c7ff-19c7-36e2-9330-e36cbd13ea19 | -13.20463 | -51.21797 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3609c54-7a55-3cb2-91c3-9e8720e6b12b | -13.20165 | -51.21732 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a05ce57-25ba-3ed0-9670-4a2267f1806a | -13.11756 | -48.22469 | 2024-10-01 03:49:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f2f30d9-c1da-3169-a24c-5240c5e28093 | -13.03865 | -51.25031 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5277e491-187b-33fa-ab82-9029b1af6a51 | -13.03328 | -51.24289 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0306c55f-f4ed-3357-9584-2ba66a2b96db | -13.03263 | -51.31145 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 295899c3-94c5-3653-9c13-dc75598ddb81 | -13.03202 | -51.24881 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 31e9f9fb-1780-35c0-bd0c-c9aeeff5e31a | -13.03136 | -51.31743 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ed63a896-20d2-3be8-89cb-4da13d9cd49e | -13.03076 | -51.25473 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fdf49002-4563-3147-adec-1edbef8aff93 | -13.03055 | -51.24292 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 89be84dd-fe9a-3093-8419-317f39a21274 | -13.03008 | -51.32343 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c921e4c0-0de0-376f-baa3-c3c920129822 | -13.0295 | -51.26068 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d18175a4-8a34-39f8-bfbb-9fc8c359b2f6 | -13.02932 | -51.24886 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 902e7610-5834-3513-9806-de2324678cc5 | -13.0281 | -51.25478 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f6197443-15ea-32d7-9dda-4c401a733cfb | -13.0276 | -51.22361 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd0d449a-9b50-3505-9576-de4b549fc3f0 | -13.02725 | -51.30394 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.6 |
| a13af766-2046-349b-9f5e-a7af270595b9 | -13.02687 | -51.26074 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4eb7eff3-28df-3c11-b9e8-1b24067cd042 | -13.02637 | -51.22954 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a1b38667-8b59-3f39-b75d-94be288d7a8b | -13.02597 | -51.30994 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| cd6d499f-3eae-3201-b0d2-a292aa123d55 | -13.02539 | -51.24731 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1b6d9ada-5850-3b3d-b1f0-aef9d7fccdad | -13.0247 | -51.31593 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 6c6d20b5-e1df-3829-a30b-fcaaeeab0a6f | -13.02413 | -51.25323 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 74d0e749-8f00-3820-94d1-c6896b093cd6 | -13.02382 | -51.22215 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0ee5ac3c-1db8-35cc-b605-43f0d9f11c79 | -13.02343 | -51.32191 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 8ae3530f-b1f8-36ec-8a3c-c3e9d1c09ae3 | -13.02286 | -51.25918 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 13b0a9fe-2bc5-35d5-904d-012efbfe0749 | -13.02255 | -51.22807 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c8b4c724-64b1-3ba5-8913-2703c7060581 | -13.02215 | -51.32792 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3231b89f-572a-37ff-bd24-e8e1a6dca6b0 | -13.02158 | -51.26514 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3aecc743-5641-35f0-a122-90cabc7a1094 | -13.02147 | -51.25325 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README50.md)
