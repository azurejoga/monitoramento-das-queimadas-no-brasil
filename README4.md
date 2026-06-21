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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9dbbd5f-4a98-3898-91a9-c78473925726 | -4.35191 | -47.76553 | 2026-06-21 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3c1d1ea6-5a0b-39ab-a2c2-95e3fad8c14d | -7.72115 | -44.56121 | 2026-06-21 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0e0c320-fcaa-39e8-a027-aeaffadc02c9 | -7.17444 | -48.18274 | 2026-06-21 04:23:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01ae007c-1a08-3a0e-9051-176a9b25ac64 | -8.0078 | -46.44438 | 2026-06-21 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82651f05-f16b-3e6a-85c5-41584652fe4a | -8.89326 | -46.93909 | 2026-06-21 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9c02e8a-42f8-3e6f-ab84-436251eb3022 | -6.837 | -47.92326 | 2026-06-21 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3c8aece-fa71-3bb9-93db-65827922af31 | -6.83783 | -47.9183 | 2026-06-21 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da6a3167-bfec-3f15-98f3-eaf45cbe9541 | -9.68958 | -47.69628 | 2026-06-21 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06ea4379-b111-387d-9714-bed80fa8c1a5 | -9.80287 | -47.48483 | 2026-06-21 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 744d3ac7-2338-3b14-8544-81f64a1e40df | -6.15098 | -48.48811 | 2026-06-21 04:23:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fcef7eb-9f2b-360d-9594-5d50dd70724b | -9.30953 | -47.62959 | 2026-06-21 04:23:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbea7bc7-4daf-301e-b501-69ef9b83ead3 | -9.5643 | -48.66867 | 2026-06-21 04:23:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61aa5609-79fa-37d0-89a1-e853e97d8579 | -10.59003 | -44.32884 | 2026-06-21 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d31ed2bd-962e-3b06-9b17-6fce5ecd6efa | -6.84563 | -47.91973 | 2026-06-21 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fff10613-3f38-363e-bedf-a56e7fbfa468 | -8.00946 | -46.44749 | 2026-06-21 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51445c25-4f38-3d42-86a7-c9f3de215818 | -8.3545 | -50.49756 | 2026-06-21 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 86b7d738-ce50-3a25-8fc6-964f64e7b411 | -8.25839 | -46.94662 | 2026-06-21 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e29c1ea-a113-3912-b3ed-13e9cd5b404d | -7.72059 | -44.56476 | 2026-06-21 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 544dfcbd-b9bd-359d-b514-47b8c8b4b733 | -8.0059 | -46.44693 | 2026-06-21 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87ec2cd6-3630-3a66-ad53-d85882a8109a | -6.99629 | -42.88762 | 2026-06-21 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cceae26c-2e4d-3841-a4eb-b97f45d2a07b | -8.65262 | -47.7638 | 2026-06-21 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59be8592-2d52-3d8f-adb5-ff262839067b | -8.3537 | -50.50212 | 2026-06-21 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 90451fff-229c-300a-98ce-7f3be86df7da | -8.00878 | -46.45153 | 2026-06-21 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b1de7c7-2e25-3273-8441-82cceb15028f | -8.3529 | -50.50668 | 2026-06-21 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f52692c-93e6-33cd-a2f3-01827be16d08 | -9.80213 | -47.48915 | 2026-06-21 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7af93648-0dac-3815-b1e1-bdd65c1c6c1b | -6.99574 | -42.89111 | 2026-06-21 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| af162938-c471-3007-986f-421be310aa60 | -6.8409 | -47.92397 | 2026-06-21 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28164364-6114-3819-9755-c0c26dba2beb | -7.18162 | -44.87805 | 2026-06-21 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f18584b-5cd6-3ba5-9640-f8749d6cfe69 | -6.15312 | -48.48545 | 2026-06-21 04:23:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70a7d30c-c7cb-3987-8933-022af468c1a6 | -8.00714 | -46.44844 | 2026-06-21 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2739b37d-f346-370a-bf3e-b7a82bfc4661 | -6.84647 | -47.91473 | 2026-06-21 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79d5fc7d-9184-360a-b7c9-31a0063fb95e | -8.00658 | -46.44286 | 2026-06-21 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49777b30-0d6f-376a-abc9-14067d002b35 | -7.185 | -44.87859 | 2026-06-21 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62a11d93-0d66-352e-83cd-621034514370 | -9.36076 | -40.50961 | 2026-06-21 04:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0d63147-486d-3558-bcc9-07c62165a1ce | -6.85036 | -47.91549 | 2026-06-21 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccaeb070-d109-32f8-95ab-4d3cf15b0a24 | -7.17675 | -48.1851 | 2026-06-21 04:23:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9161d0b2-a3d4-35fc-9807-0aa1fe7b5d8f | -6.99963 | -42.88814 | 2026-06-21 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7e91d135-ecdc-365b-ae68-d0d820fe5737 | -9.58811 | -48.73193 | 2026-06-21 04:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f85b587f-a00e-3cbc-b4d8-cf9d79959909 | -10.58282 | -44.33128 | 2026-06-21 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f313fdd5-71d1-38d8-9277-1a9eb54f8ba6 | -8.46519 | -51.53425 | 2026-06-21 04:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1db24105-0b73-3a5c-8811-7e6870342dc3 | -10.5928 | -44.33289 | 2026-06-21 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 20ab088a-dbba-3e5e-baf4-949b759bc21b | -10.57949 | -44.33073 | 2026-06-21 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4fd4910e-34cc-3429-8fb5-d295abbfa04f | -9.64024 | -43.11823 | 2026-06-21 04:23:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6bfb4289-6027-32c3-bf6c-4d6a92f839bf | -8.25897 | -43.92805 | 2026-06-21 04:23:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 950310d1-2370-3351-b061-bb6f337510be | -10.58337 | -44.32776 | 2026-06-21 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| abbc15d2-2ee7-372d-8eba-7f02574da2d7 | -10.58947 | -44.33236 | 2026-06-21 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e9fef5ac-bbd2-332c-977a-1675f4569d55 | -8.46035 | -51.53339 | 2026-06-21 04:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f916af83-2cde-3680-835e-6eec4c8fbf22 | -6.99908 | -42.89164 | 2026-06-21 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 5ef502b2-03bc-307c-9b9a-8c8d520f4ed4 | -9.80391 | -48.92277 | 2026-06-21 04:23:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4412a6e3-d82b-34eb-9f73-58a4a28762b8 | -9.04091 | -42.68756 | 2026-06-21 04:23:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0759efd3-198e-343c-a042-decff8d06723 | -8.07829 | -46.23027 | 2026-06-21 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12c052db-d529-3436-a636-d564e8b541e8 | -9.29138 | -48.66863 | 2026-06-21 04:23:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b40d4e4b-796e-3d8e-aa54-9f5a5b8c6289 | -9.3125 | -47.63465 | 2026-06-21 04:23:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a01565aa-3c4b-3127-ab2b-ab7676ab94c7 | -8.34919 | -50.50126 | 2026-06-21 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 946f7128-4dbe-33c3-8ec1-b656b8cad88c | -8.64904 | -47.7658 | 2026-06-21 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03191215-782b-3fdb-86f0-7c8eb56697b2 | -8.39204 | -45.5556 | 2026-06-21 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99ff1a90-31a8-34f7-a9e5-637e43259fd1 | -10.59335 | -44.32938 | 2026-06-21 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56b10590-1c6e-3e0d-9dbd-39c48f34e0e1 | -7.18617 | -44.8714 | 2026-06-21 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4e97066-625c-39c0-bdfb-227eb46a439a | -9.04027 | -42.68768 | 2026-06-21 04:23:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 95dff17e-de06-3748-a2bd-6f04d89ddbf9 | -8.35822 | -50.50295 | 2026-06-21 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2fff5a3d-d37e-34ec-8a5c-6c5560d75e94 | -8.64806 | -47.76771 | 2026-06-21 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ea77ce3-521a-379e-80d9-39bb71d2e272 | -8.89393 | -46.93497 | 2026-06-21 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0c5590e6-bdbb-32fe-9d9d-87609d905fad | -9.69033 | -47.69183 | 2026-06-21 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab284925-5a12-3c1f-9024-ea4ef0e2698e | -9.30879 | -47.63402 | 2026-06-21 04:23:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18d79e91-1059-3d6a-960d-c9aedefc9753 | -10.58005 | -44.32722 | 2026-06-21 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb039bd9-f0f7-3db8-a98c-8f200b463ebd | -13.24769 | -51.89748 | 2026-06-21 04:25:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fea24fa1-cd96-3e72-973a-5a6e61ecd027 | -13.56165 | -43.5107 | 2026-06-21 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4510c4fa-59a9-3795-bbf6-95f496e1d176 | -10.83301 | -49.11834 | 2026-06-21 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a024b7d1-0eef-30ce-a73f-bcd6f6435ad6 | -16.49892 | -43.50299 | 2026-06-21 04:25:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4cf5ce6-e766-3dbb-a9d4-939a2d485018 | -11.94674 | -43.96355 | 2026-06-21 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9400ee53-c441-3e7a-958c-2cfc3a0b8eab | -11.19813 | -46.77806 | 2026-06-21 04:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af9e46ef-42cd-3e63-ba47-ba67de4de70b | -11.63567 | -48.53469 | 2026-06-21 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a93307cb-06ad-3505-8055-c37157d080ca | -10.53576 | -47.72798 | 2026-06-21 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f2cedc2-27c6-3a8f-a0d8-fe632b10a8a1 | -13.49944 | -54.4301 | 2026-06-21 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae868cbf-bd34-3b64-ad54-44f94c0ed3e8 | -11.10754 | -54.13137 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ad99ab8-1925-3c59-a0f0-b9fec374e830 | -11.63646 | -48.53008 | 2026-06-21 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a8c944e-b984-3e5a-983f-14d29f5c3481 | -16.93613 | -47.13646 | 2026-06-21 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bcfa5a6f-6977-3698-9ab3-3f8b3c6efd14 | -11.09518 | -54.13641 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5bfb2892-e98b-38e8-a236-2afa55bc5db8 | -13.51674 | -52.16624 | 2026-06-21 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 388f5cd7-86f7-3e5c-867b-cd50570f3825 | -11.54668 | -48.26588 | 2026-06-21 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cce73a8-13e1-3b65-87b9-a90769bccb5c | -17.61296 | -46.69945 | 2026-06-21 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c4a06da-a2d4-3143-8e6a-b25c345d1a5e | -11.09711 | -54.1558 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 262e0325-9fc0-3884-978a-74a58e8c23fe | -11.09448 | -54.13999 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 578ae680-9853-307f-8591-52c400ee6a8f | -10.5387 | -47.73295 | 2026-06-21 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6200247b-aec1-339c-b32f-b2e2aea3c364 | -11.10544 | -54.14223 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8bb2e80b-3850-3319-b33d-65f1b034b48b | -16.05926 | -42.0852 | 2026-06-21 04:25:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f22a84b9-72ed-36f9-9051-c5d59f39389f | -11.10614 | -54.13861 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a1f4b3db-d068-3ddc-a4f8-6cb044a3197f | -10.05928 | -48.09041 | 2026-06-21 04:25:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 756c4e21-8e59-3a84-b1ec-d38427a89d48 | -11.10329 | -54.15329 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ba04890-5a9f-3c5c-a970-3a6dc2e9b81b | -13.51212 | -52.16538 | 2026-06-21 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 871a5353-8894-3cac-8c3e-cff8fe0d7816 | -10.51733 | -51.9387 | 2026-06-21 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae3c995-90b8-33f2-b87c-f4def69d70c9 | -13.56222 | -43.507 | 2026-06-21 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c19e412c-9563-3178-8890-6b56da2c0829 | -11.09855 | -54.14837 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 72366caf-7f04-39ea-a4c3-0d62a1d93dca | -11.88981 | -43.83438 | 2026-06-21 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 423a4666-e235-3256-96a1-95a4c5addc65 | -11.63945 | -48.53535 | 2026-06-21 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 468c4f1b-c0ad-3d22-aa9e-7963a7b6d1f1 | -11.03376 | -49.51628 | 2026-06-21 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cf9f97d-9c0a-3510-936c-f16829d09e5a | -16.93889 | -47.14079 | 2026-06-21 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76bdb75d-65a8-3f3a-b004-636017d767c7 | -12.06803 | -48.42754 | 2026-06-21 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 09d06cfb-27eb-3b5b-8ae5-0fcc15c87a7e | -10.69022 | -47.69959 | 2026-06-21 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca4f3659-bd25-3301-905b-08c225f5d020 | -10.83697 | -49.11904 | 2026-06-21 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README5.md)
