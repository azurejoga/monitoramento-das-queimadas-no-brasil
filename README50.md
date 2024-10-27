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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95a7e652-1d9f-3ea0-aba9-db75938268c1 | -2.54251 | -51.16785 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 837314ad-bc89-325e-ad7b-710b6f01173d | -2.54246 | -51.16829 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f4dbf12-ba66-32f9-9b33-88c2d800561a | -2.54186 | -51.17178 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 004448f2-a16d-3aaf-b3a5-b9b0be9fdcd1 | -2.54184 | -51.17221 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3d5cccb1-5efe-3d69-9138-f384252180f8 | -2.54122 | -51.17614 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 57f52ad8-1251-3f74-b6d7-fadb7dce61e9 | -2.54121 | -51.17569 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9d8d208c-3290-330c-8366-a15149bb70c3 | -2.5406 | -51.18005 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 89bb8f45-a0df-3ad4-bf28-9a6bd1ceb284 | -2.54057 | -51.1796 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 98bf6150-e916-35d5-9ad9-f65800cba6fe | -2.53893 | -51.16326 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b42aefc-a827-3927-bde7-6bc5f7723bbd | -2.53828 | -51.16718 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae23615d-40ad-3462-84ba-91754efafab8 | -2.53823 | -51.16761 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d6802dc-b448-3da3-949c-2a405684a953 | -2.53763 | -51.1711 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 3ff63a51-2661-3c56-b858-818aa0dc66a3 | -2.53761 | -51.17154 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4e551f70-060d-3e80-9580-5636cd3bc00a | -2.53699 | -51.17545 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 02479f52-6d67-3cdd-b334-a535e222456f | -2.53698 | -51.17501 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| fdca948c-9749-38ac-b404-f352ced1709d | -2.53637 | -51.17938 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 5297f84b-fef5-3d9e-a72c-2b0399a62481 | -2.53633 | -51.17893 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| fd727b74-4466-3d37-8aeb-41710cfe3f71 | -2.534 | -51.16693 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e06a1865-17c4-3c6a-aecd-c3d704965d66 | -2.53338 | -51.17086 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 13b62abc-eb6c-329a-a3e0-b469de3b9b52 | -2.53276 | -51.17477 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ae09118f-03de-3cc2-879b-e9d309646c72 | -2.53214 | -51.17869 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 82792c20-b658-3bd2-8a46-ea3afda8d956 | -2.52977 | -51.16628 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66ca3b10-05dd-3479-b527-7c949fef95ae | -2.52915 | -51.17018 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eb3315f9-a731-3af9-8357-71a9e651b836 | -2.52853 | -51.17409 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d111f260-80d4-34aa-b449-380468407389 | -2.52791 | -51.178 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 117ec96e-50c3-3f3c-bea6-2fdea24d8b98 | -2.52729 | -51.18192 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e91c7f51-468f-3b51-9107-5095a54d4063 | -2.52491 | -51.16953 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 52266e74-95b9-36af-bb58-834685acdfbf | -2.52429 | -51.17344 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a8b624d9-b5b9-3cd7-ac48-8234069b7d05 | -2.52368 | -51.17733 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c29b0bb-e51a-39c4-9445-5442c8d59059 | -2.52306 | -51.18124 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72bcb5df-52e8-3f06-a17e-b23413209747 | -2.52006 | -51.17278 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 49d53f89-a8f5-3199-bf55-f799f6acd455 | -2.51944 | -51.17666 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b04fd37f-50b1-36c4-bc41-e8d2133c510d | -2.51882 | -51.18057 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ba8fa2f-a906-38e7-b540-e4503dff4e90 | -2.26938 | -50.65268 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2084a33-85c1-3b6a-afb1-4561f6a8a756 | -2.2688 | -50.65632 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9507a85-06f6-3656-971b-b539ee1c1da8 | -2.26293 | -50.64038 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3123864f-745f-307d-a7b4-739f75a5415a | -2.26234 | -50.64407 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 312c4193-dd7d-39e7-b5ad-40101c5cb8f6 | -2.25824 | -50.64342 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f656836f-90ac-3a38-8e45-67512cc34826 | -3.33604 | -50.75895 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93c68d69-948d-3699-8294-bb55c033e903 | -3.33198 | -50.75825 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 62426870-5e0d-31f6-a142-c4c45c7d95aa | -3.09991 | -51.25769 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5de5d355-f7a7-3b6a-be05-b99d64457c23 | -3.09505 | -51.26091 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33f37586-b0c5-3e8d-98d9-ec76a0b266f0 | -3.09442 | -51.26477 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a89ee55-b4cf-3e13-8362-b85080e5fa94 | -3.07441 | -51.25452 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e5528c5-1392-3707-aadd-d289436f4058 | -3.06976 | -51.25676 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b869c761-97c9-3a55-a7df-bb86f7bbd7f0 | -3.02278 | -51.38769 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e9b8274-a856-3eb5-812b-f2429d314249 | -3.01916 | -51.38301 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aeafde8c-8455-327a-92a0-edf494e270a9 | -3.33662 | -50.75533 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f3d0b320-6fe8-3e58-891c-3249ba1e1a30 | -3.10348 | -51.26229 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6611c830-df76-367e-ac58-1c3259531598 | -3.09927 | -51.2616 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55097276-1dda-3e60-a8ef-110f24b4cd4b | -3.09863 | -51.26546 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 342fc42a-d4d4-37e9-b0a3-4fe2c78c9fdc | -3.09617 | -51.33351 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 921c2e78-105d-303e-ae5a-a8bf0100fced | -3.09422 | -51.34546 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8002756-dd97-3940-a55f-4bcbbb27c796 | -3.07461 | -51.25362 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7440ee5f-d948-3e48-8857-b570c9abd84d | -3.06958 | -51.25768 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7610b0b-6c07-3f65-b54a-f72d0b53f7cd | -2.9765 | -51.05322 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b56e86e9-c1e9-3387-b3b8-07ed6ec07ed1 | -2.97233 | -51.05255 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 864108ef-ad30-31c7-831f-1e50755ebcff | -2.92854 | -51.75164 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06c3dfb1-82e5-3a04-aaea-b40c3b4c0e87 | -2.92785 | -51.75585 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdd72cd6-748b-3bd4-9815-2e1784ee3210 | -2.92716 | -51.76006 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 178fae81-972c-3944-a21d-7cc692c9001e | -2.92647 | -51.76429 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 49572c36-9f21-3299-837f-63c5d920ee83 | -2.92577 | -51.76858 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 05378726-e51f-3a1a-aadc-7000f6b26472 | -2.92508 | -51.77283 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a30e3e79-9e71-392d-b322-93d56067b271 | -2.92487 | -51.74657 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 05d3f7b4-5207-33ac-9bef-f8d460d965e8 | -2.92418 | -51.75084 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 74bae298-4468-3512-981a-b5eae3bc299d | -2.92349 | -51.75506 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 19e07659-7f70-311d-b5ba-12f1f13eb5b4 | -2.92281 | -51.75921 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| dd89337a-7206-3798-9912-248c77810e2d | -2.92212 | -51.76342 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 085592e8-17b4-3928-a4bb-197f442942fc | -2.92142 | -51.76775 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3615a250-6b25-34cc-87ac-46c3b0fb8a53 | -2.91983 | -51.75001 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3e71122f-84aa-373e-b24f-6373ef4488c2 | -2.91913 | -51.75428 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 08183aff-aeb7-300f-9ac3-c9489896ba78 | -2.91844 | -51.7585 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 468f52ea-5fe4-3bc1-b329-9efb6c8c21c8 | -2.91802 | -51.70637 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25e971e5-1dde-3621-a9b8-9e56ba6f7b62 | -2.87868 | -51.31176 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 560b616e-769b-35b5-b575-90542d310316 | -2.87443 | -51.31107 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 058315ac-3d89-39bc-8985-2254103119b3 | -2.87378 | -51.31504 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 500a832a-6ac5-3f52-99d2-b530e99fce2f | -2.84259 | -51.80799 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dcfaa166-afbb-320b-bb0e-91a5db842a5b | -2.8419 | -51.81229 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 23dd3347-2336-346a-a7c8-d4443eaa7186 | -2.8412 | -51.81663 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68b49ac4-31e2-3db3-ad5a-8deb347815fc | -2.83888 | -51.80301 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6a64ca98-169d-3564-87e9-3826eafd9948 | -2.8382 | -51.80727 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c6b189dc-3704-3eaa-ab74-81116e3369e3 | -2.83751 | -51.81154 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e614333-26bc-3df7-a516-2269985c7f6e | -2.8338 | -51.80657 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9471d34e-959f-3f09-8f63-77e7d552efb7 | -2.83311 | -51.81083 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07acea0b-36ad-3b85-b570-81b945d001eb | -2.83242 | -51.81511 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5365527f-fe9e-3cac-93d3-ef6fc3392b50 | -2.82871 | -51.81013 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a71750b-cf4b-3fee-adfb-de4065425f8b | -2.82802 | -51.8144 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24b76ae2-fa8a-38ce-9a26-2c6a1495a81f | -2.828 | -51.03765 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d820542-45e9-3a24-9734-4a62fdcd70b6 | -2.82736 | -51.04159 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 993940aa-00b2-3a20-895e-42b69c8a113a | -2.8238 | -51.03713 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9135e3ff-a1cd-3fa3-8431-6a637c6ecfe5 | -2.82318 | -51.04099 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a29beaae-232a-372b-8824-1726b45ee54c | -2.81962 | -51.03652 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbddfea9-9e94-3464-ad5f-63e169a4c724 | -2.81365 | -51.60051 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a20497d8-ce8c-304e-abfa-3f678f437e8d | -2.79999 | -51.60243 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 149ad475-3800-3565-bc80-2914f0b5921d | -2.79908 | -51.59958 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e06bad08-55e3-3f3a-9be7-e865aa1e2e6e | -2.79634 | -51.59758 | 2024-10-27 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d02b0b92-a760-374a-8fb8-be72c627b036 | -2.79187 | -51.36827 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccaf4ab9-4c15-304d-bacf-3f76e9b26e3b | -2.7876 | -51.36759 | 2024-10-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3343570-f76a-34cd-8281-eb2196036f5b | -1.92855 | -52.08597 | 2024-10-27 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0162b15-6b74-3032-9d68-2dcb074485aa | -1.92782 | -52.09056 | 2024-10-27 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README51.md)
