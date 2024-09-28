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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64f38141-930e-3b12-a543-f836961d7306 | -11.20874 | -54.75088 | 2024-09-28 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7198a6e7-3cd6-30a5-88ae-609de7013224 | -11.2081 | -54.75533 | 2024-09-28 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ef42ddd2-5cee-328f-8e10-952d8c0065d0 | -11.18745 | -53.90496 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2079524-7830-316a-90a7-2381baa625c9 | -11.18674 | -53.9099 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 893ed605-0d89-3ece-84c0-d9d6f2664871 | -11.18602 | -53.91484 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f125d39-d97e-3b4f-a23a-8140ba681c78 | -11.18531 | -53.91975 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e6658b3-68c7-3949-aa17-1b86150ec720 | -11.18429 | -53.8995 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a5cba18-cee0-3a58-9a93-d586a3baf5f2 | -11.18358 | -53.90442 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f514395f-68d1-33d8-977e-5951d7f6920d | -11.18287 | -53.90937 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 503eb28c-5906-3793-9b05-cdf21f3e3554 | -11.18215 | -53.9143 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43037ce9-0c63-3e40-be26-3dcef25ab54b | -11.18042 | -53.89896 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| eed5b33e-66e5-3606-b31e-ebff33fc9bfc | -11.17971 | -53.90388 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b43674d5-488b-373d-8078-5226eaf54cce | -11.17899 | -53.90883 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 50b11581-79ab-394b-a7e0-bcf656350aea | -11.13625 | -54.17717 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb3d78f6-89f9-3143-8df6-7d6b12945766 | -11.13556 | -54.1819 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b1aba9d-6031-3301-bfc8-e3ee1d7299a2 | -11.13196 | -54.09905 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07b9bef2-cf3c-3aac-803a-c7c223e73dce | -11.13176 | -54.18136 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5879c445-0787-35a7-8ebe-e172cb7f7f36 | -11.12795 | -54.18082 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 841e3ab6-5623-33aa-bae3-61a29a83d5df | -10.93959 | -54.25599 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 572444a0-7454-39a8-b2b2-4441f6432adb | -10.93893 | -54.26068 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 403f3929-997a-3fa3-9031-78307499951d | -10.93827 | -54.26533 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa14b8f8-15a7-37ef-9d45-11db51bca579 | -10.93647 | -54.25077 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 180257f3-d4df-32ab-ae61-055aeb184d88 | -10.93598 | -54.25267 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da2f1be7-bf42-3e54-8d62-eb19b5bd127e | -10.93581 | -54.25545 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 67e1b2ce-06bd-3bdb-b58d-364faadab22a | -10.93529 | -54.25734 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40c397bc-f925-30d8-a3d0-6dc67e3423b5 | -10.93515 | -54.26012 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fcd3fda7-07c1-3be1-93d5-3ae26f737739 | -10.9346 | -54.262 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70b99f09-f7e5-37ff-a109-8d9327dc35da | -10.93449 | -54.26478 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d33317e-1335-32e9-a44c-533c60beb322 | -10.93269 | -54.2502 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51a1a590-f896-328f-be3c-d9791d71b2d3 | -10.9322 | -54.25211 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67a2161f-4c23-3bf2-91d4-52a804b70d9b | -10.93203 | -54.25488 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f9fef73f-f055-3345-950c-719195ed7a9c | -10.93152 | -54.25678 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa654f9e-b96e-3e56-9665-e87176d07253 | -10.93138 | -54.25956 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| df63dfe9-9566-3d4b-8ae5-6a5971f7b886 | -10.93083 | -54.26144 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6de50fa3-a48b-33e0-997b-eed235c6376b | -10.93072 | -54.26423 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73304e40-92b7-3932-8514-495a6d14e149 | -10.92891 | -54.24964 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5173a2d-1424-3ec2-ae70-0940c6428af9 | -10.92843 | -54.25155 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99f13f63-f5b2-3a75-8f15-08a3a0f0b30a | -10.92826 | -54.25432 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e9a2c3f-691b-3477-8f35-ce43a8676bf5 | -10.92774 | -54.25621 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53c56d86-0ab3-3bbb-96dc-a53026666f7a | -10.9276 | -54.25898 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55675ae6-9b1a-3101-8a1b-8b3a439367f3 | -10.92706 | -54.26087 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a67fdcfd-7567-39f6-ac42-00ff28c05fa7 | -10.92448 | -54.25377 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a02aa516-bc8f-3636-96ef-936de2234846 | -10.92397 | -54.25566 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c84090b-318c-3497-ae20-8a719c4e8ed7 | -10.92383 | -54.25842 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07c423b6-e40b-3f1e-8fcd-e45b8e28d5e3 | -10.92329 | -54.2603 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ded6b14-b7ca-3d84-9b4a-27704c5dd042 | -12.69969 | -54.69154 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5c39643-58c7-3c32-acf9-8820e5a13e0a | -12.69905 | -54.69622 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af6c188a-d292-3215-a581-d823eeebb501 | -12.69893 | -54.69468 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fe686b1-bf26-3353-8dce-96d5356cd392 | -12.69711 | -54.71021 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a493d7e2-d8f0-3b88-b0e6-61ed86b80a66 | -12.69647 | -54.71484 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9216e2e6-04f0-3e31-af84-0a8680ad9dd7 | -12.69624 | -54.71328 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72db2790-4ff1-3a4d-887c-f74c87b27e07 | -12.69557 | -54.71792 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9fd4a4c-aec0-3aa6-8d3e-40dffa7d33aa | -12.69248 | -54.71276 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d535966-8cd0-3f74-9d04-2b0934bae10f | -12.6918 | -54.71742 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79dbcce4-0e2d-372d-8435-c92158f763e1 | -12.68804 | -54.71691 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19046928-bf23-350d-b7c0-f8ab37c3f81d | -12.6867 | -54.72616 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 462f0583-3acb-3cd7-b8a8-fb5ff6a76a5a | -12.68604 | -54.73077 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e00b930b-beb7-3e42-a88b-332e94657a13 | -12.68427 | -54.7164 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64d0f8bd-a395-3928-8c63-0472198d7353 | -12.6836 | -54.72104 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0847bdd2-70c8-3a66-a3db-c98db643237d | -12.68294 | -54.72565 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| db7bde05-be23-3eea-9ae5-00a3339ab298 | -12.68184 | -54.70659 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc27f862-868a-3f09-97d0-ee8d4eff29bf | -12.68117 | -54.71125 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f6c8043-e546-31fb-b927-1fba1240742a | -12.6805 | -54.71589 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 315981dd-d14d-3a67-8df1-049e98c0b19a | -12.67984 | -54.72052 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 99e359e1-f1c5-3990-a3d7-d760c0bfc11e | -12.67917 | -54.72513 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ce5517b2-e648-3c00-9e57-8391efab46b2 | -12.67851 | -54.72972 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3ed1a786-8221-3a9f-aacc-bd024346bba8 | -12.67741 | -54.71072 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6f88b047-d568-3c31-9adc-8ee545cd3f4d | -12.67674 | -54.71536 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce9ff06b-d684-3e62-a4da-501fca21ab83 | -12.67608 | -54.71998 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7b2b3d61-d7e9-3341-880c-d2b7c899f0b7 | -12.67542 | -54.72458 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 52b772ef-1622-33ec-9330-3007c1c90cbf | -12.67364 | -54.71018 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8fc5fe57-2cdf-313d-8418-7aef16e6f697 | -12.67189 | -54.6956 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a563f48b-e511-3327-9d83-4f5fb023ade4 | -12.66812 | -54.69506 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c851a693-3bdb-3d8c-809c-ccdaefa92efa | -12.66745 | -54.69975 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 688eafe6-728f-3e15-9ab7-74d78063622d | -12.66679 | -54.70443 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2567c4b-2cae-3a4c-8485-ec153dac42b4 | -12.66593 | -54.65649 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ca7f8e68-fd7e-37de-b841-bdaec35a0a4e | -12.66526 | -54.66119 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12fdf669-0754-3c81-bcef-4262fd015733 | -12.66436 | -54.69453 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e46ca8e-037b-3283-b29d-76fea5aa03b1 | -12.66369 | -54.6992 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 59b1460c-60f4-3420-8d91-1fac12f2ed46 | -12.66126 | -54.68929 | 2024-09-28 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 50cd6193-c185-39c4-a527-0a9dd1a99dc1 | -14.75587 | -55.32327 | 2024-09-28 05:10:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c77c509f-c3e4-3d5b-9b84-970b41632c69 | -13.98042 | -54.58286 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d9506e1-8ff8-39a0-a64d-71fa93afcc93 | -13.97657 | -54.5823 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2b7f567-0a17-3a75-a853-c0f9f5ce0684 | -13.97589 | -54.58718 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62839105-d964-3271-b379-6ea0e4679952 | -13.97452 | -54.59699 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27a7ab84-4adc-3194-9ae2-199bba6dab32 | -13.97204 | -54.58662 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b60edec0-b378-3ab1-a35e-9374fb89d5cd | -13.97135 | -54.59151 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f9dbed0-17f8-3f06-a8ee-d7b35488580f | -13.96818 | -54.58607 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0db5b187-d20c-3b52-aa31-a069d4656388 | -8.77866 | -55.0084 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 329e4df3-e2bc-328e-8fc3-b426aabfcd88 | -8.70443 | -55.04679 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7fa478b-92b9-330b-b263-ab6c1d0bdae5 | -8.52133 | -55.18557 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72276dbf-00bc-3b5a-bde1-2c679d061f7f | -8.52075 | -55.18948 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbc5a435-9dcd-3b80-95fb-78addc6a0e86 | -8.52039 | -55.1863 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b809f58-86a6-312b-b370-e1d300e5b84e | -8.51979 | -55.1902 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dad8d89f-8d53-3541-b0c0-df71847c8a6b | -8.5192 | -55.19411 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fed53737-e10a-371f-8640-e48f8cfbf229 | -8.51783 | -55.18504 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68fce5da-c5f5-31ec-94d0-59746de24ad4 | -8.51725 | -55.18895 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59cb2fec-116c-319c-9d69-70f088b804c5 | -8.51689 | -55.18577 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f370fd0f-2c38-3534-9ced-4ab08256d2ae | -8.51667 | -55.19286 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7007e1c1-f593-3d0c-9981-43a181b483c0 | -8.51629 | -55.18968 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README83.md)
