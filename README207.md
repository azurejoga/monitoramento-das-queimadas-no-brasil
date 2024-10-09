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

## Dados Diários - Página 207

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 927bc10c-b6af-30f0-8973-1af983c67227 | -11.6867 | -64.00916 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5df1fdf6-4ea2-3bc2-a494-4af8ccaff7e8 | -11.68513 | -64.02044 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6af62b3b-d13b-3cb8-8870-a4c6b9ed6345 | -11.68392 | -64.02917 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| c0daffd9-60be-35c7-be84-be472e9b5500 | -11.6834 | -64.03291 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| e4ee4a23-3a4e-3e6f-9d7c-8d6e17fcf2f5 | -11.68301 | -64.00503 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08affc69-3ebe-3fc2-ac5a-e8997a584bac | -11.6829 | -64.03656 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a29f406d-8552-3b3f-9b22-75b49b5744a6 | -11.6825 | -64.00865 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a233ca59-b5f4-3244-8ddf-09e5b56c2f7e | -11.68093 | -64.01998 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe407e23-418f-3097-816b-21a80b7b6a99 | -11.68034 | -64.02429 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c962cbb-868a-3f1e-ab01-68203bbe8822 | -11.67974 | -64.02866 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 13b7ef4a-ce0d-3665-8447-964290f6dc04 | -11.67921 | -64.03243 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 5675819a-2cb4-3c91-95b9-0a7325ccdcda | -11.67871 | -64.03603 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 667e4f2b-3aab-302b-bf3e-070650c2cc44 | -11.67781 | -64.01173 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f5f5f04b-734f-3188-8d50-dafdde574f0c | -11.67615 | -64.02381 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21f2a078-b1bd-34c0-a567-a471aecb6cf2 | -11.67556 | -64.02808 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 3eb45369-83ee-3b38-83f9-5f73dbc0b525 | -11.67503 | -64.03189 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 32d5a2ce-67be-31e2-95b9-8ab1f0de30e5 | -11.67453 | -64.03553 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d180469-b1e3-3ae4-a545-bf9903b845f6 | -11.67401 | -64.03928 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c87de514-c82c-36b9-8a06-0a66f05f7e74 | -11.67348 | -64.04314 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 654667a6-4c86-31a5-ad40-de474438142f | -11.67295 | -64.04696 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ae00c6c-2815-3194-b1eb-771f91df977f | -11.67195 | -64.02336 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95f1407c-5f38-3dad-8ddd-feba73ff4350 | -11.67139 | -64.02747 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 351d20e7-fdaa-37e6-a848-e556d7597f27 | -11.67086 | -64.03133 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 19ea9372-bf03-3f21-ad5d-0500c7813ba3 | -11.66982 | -64.03882 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f454e0b5-e7e0-3a51-b926-0c266536db09 | -11.66668 | -64.03078 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e7ad98f-0297-3c74-aaf6-37fbfa66a437 | -11.66303 | -64.02637 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca4052e9-fa6a-3a3d-a7f6-4b6c47898359 | -11.64854 | -64.03889 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cedc318-1909-3464-ab0e-512908d6911d | -11.60969 | -64.26155 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2882ba65-1349-3726-9e09-82cc7376dee7 | -10.95764 | -63.59879 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6de90b9b-f5e8-3637-b599-85d6e8cce463 | -10.97888 | -63.95222 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b791333d-36a0-374a-9fbb-b826564aac9a | -10.97843 | -63.98671 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42e6e9dd-6f9a-318a-8423-de7b58031e29 | -10.97834 | -63.95626 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79e19cc5-3795-338e-b977-09aa2575ac4e | -10.97779 | -63.96029 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4d16b89-6ef2-354a-badb-822b388adda1 | -10.97727 | -63.96413 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77e176bc-60a3-313d-b89f-0609a88660f2 | -10.97677 | -63.96782 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01a40e51-6e8b-3084-9254-e9a8cfd5851d | -10.97531 | -63.9473 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5548b04-ef60-3f1a-8a2c-ae5a741e50c2 | -10.97477 | -63.95125 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7619a1cb-9747-3cb3-8b16-264d7b75b5de | -10.97476 | -63.9826 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ef545f1-625d-3b8d-b731-508429118fbb | -10.97424 | -63.98649 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7f4e7441-d20b-3074-aa07-552e8c48d360 | -10.97424 | -63.95518 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36e6d6d0-7619-38f1-9b81-db166ff63866 | -10.97216 | -63.97065 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e1f8c00-0ccf-3787-8011-0ed72204805a | -10.97164 | -63.97443 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cac86ce0-7b4d-397a-ab73-79f22d85388c | -10.97061 | -63.98212 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 157a04b6-649a-3e99-86ff-5af97888ff65 | -10.91061 | -64.15159 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0631d910-4dc6-3e4d-a940-86d3e463d76c | -10.91003 | -64.15569 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce2f98ac-515b-38af-bd2b-494975103d9a | -10.909 | -64.16296 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfd8086d-a89a-3be1-bb83-1845bc242d49 | -10.90854 | -64.16624 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 308c6cba-8468-3620-a7a6-d9f949f1baf8 | -10.90649 | -64.15118 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25b88b4a-bcae-31ba-9628-e6cd9031b302 | -10.9059 | -64.1554 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdbf9432-26eb-3ffd-95e8-b6298fd97e83 | -10.90486 | -64.16277 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b71a53e-2646-3e17-bd91-d11a965501ec | -10.89779 | -64.15362 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7537cefb-6152-3add-84ca-db852e7a5c91 | -10.89726 | -64.15738 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7e4cca5-a6ef-3a0d-98e0-a68769de9b15 | -10.89674 | -64.16111 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3bf4ca44-f65e-3090-9ae9-ee72e06727e5 | -10.84054 | -64.17547 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 532cc75d-71e1-37af-b5c2-198a32bf36c2 | -9.16809 | -66.04819 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a593a5-b271-311d-9201-010886145aeb | -9.18929 | -67.20461 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59ba9eaf-4db8-3c12-91ac-3012022ecff0 | -9.18874 | -67.20834 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9555815d-62b4-3af5-a72b-f0f797073043 | -9.18858 | -67.20534 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10c8cd6a-b1cd-3762-abbb-bd296e0aed20 | -9.18801 | -67.20905 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b27bb941-6b26-3b0e-86eb-138b476d57f0 | -9.02163 | -67.26743 | 2024-10-09 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25913748-9d06-3343-8c00-fc71c3163b93 | -9.40304 | -66.54234 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13398400-d9a5-30ed-ac97-7c358fafa6c5 | -9.40246 | -66.5463 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a26885f-6e80-3c82-b063-e28b89f0f967 | -9.40188 | -66.55025 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a7f04e0-0eaf-3493-be30-9ecf4a662592 | -9.39954 | -66.54181 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74af4047-e560-3083-be9d-b8326db25691 | -9.39896 | -66.54575 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a39ec5eb-8014-3132-a72a-85d5922f81e8 | -9.39838 | -66.54971 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66d30aa4-8e8a-33be-8902-469a3e5bec19 | -8.87681 | -66.64673 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd6ee42b-be70-3b32-821f-3f624834c58b | -9.16749 | -66.05231 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b9b1bc7-5c0c-3f90-977e-d5c72e9696de | -9.16271 | -66.05997 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07cf0d88-bebd-3b86-bf02-70a9e5ffec61 | -9.16094 | -66.04706 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 177a0f3b-a370-3446-a6c1-dc9c1b8089de | -9.16034 | -66.05119 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 363a921a-bc5e-3518-a213-7e618bcdf87f | -9.15913 | -66.05943 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a57517f-280f-33b8-9120-1925bd26cf81 | -9.15853 | -66.06356 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f872a3b-3cca-35d7-bcb9-386f7fae9977 | -9.15796 | -66.0424 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38116128-ac9a-30be-904b-5243d4d4fea3 | -9.15736 | -66.04653 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06546cb2-b622-32d6-a344-970e963a2440 | -9.15676 | -66.05064 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c039a0-d0c0-3d8f-968f-55ef3cf60a47 | -9.15555 | -66.05888 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d72ec064-b8a9-32de-9a6f-84052d7d9013 | -9.15438 | -66.04187 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3909fab-e2bb-3cf3-990b-bdd1fc027f8a | -9.15378 | -66.04601 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bbf4fc1-f971-32b1-8440-d26841195756 | -9.15257 | -66.95748 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6be2a78b-05eb-376c-b680-f7b5b038c169 | -9.15079 | -66.04134 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d47c9cae-8e0d-3765-b8a5-b650db56ad90 | -9.15019 | -66.04546 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42153ef6-e725-3ac1-b1dc-bdc368453c68 | -9.1496 | -66.04958 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4bab48b-12ef-308d-a419-b5d15e9edbb3 | -9.14828 | -66.04192 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c55570c0-b558-3017-b3e6-a861ac23a2c5 | -9.14766 | -66.04603 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d19d5f24-2add-3d3b-81be-d41205127d23 | -9.14721 | -66.04082 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91364ab5-882e-39e8-a124-071637c7617c | -9.14661 | -66.04493 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68561cbf-dad5-3f0b-a871-a813a9022986 | -9.14602 | -66.04903 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37ed02e3-7d3c-3b3c-9819-af69de66cb09 | -9.1447 | -66.04139 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 531cb4be-4766-3a78-9ad0-f1be3b5530d1 | -9.14408 | -66.04549 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 434e2532-0566-3ab2-8002-44d3d8d54de6 | -9.14346 | -66.04958 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bb1d8d7-5091-39a2-9396-46cea3961320 | -9.14303 | -66.04438 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad7dd10d-5686-37ae-86cf-e5434f4f052b | -9.14244 | -66.04848 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bec7432c-9059-3781-b98e-f19ceb0bb638 | -8.88375 | -66.6478 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5eb0be1-1f48-33a8-bfd3-f23c200253d9 | -8.88028 | -66.64725 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eedeb92d-d42d-3c68-9b93-318d0ceaf5fd | -8.87623 | -66.65061 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12ec0956-ebd8-3584-b261-fb4dd149498d | -8.87333 | -66.64621 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f584b68-a4de-3509-8885-994cafbe437b | -8.87275 | -66.65009 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e10243fc-bc0e-3596-8fd0-585cfb2b7497 | -8.86928 | -66.64957 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bd7a2d1-58e5-3b10-8926-703f75965d9d | -8.74798 | -66.92107 | 2024-10-09 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README208.md)
