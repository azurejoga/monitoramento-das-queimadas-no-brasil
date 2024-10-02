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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f24e309-0aac-3648-8d04-c47bb22d9de3 | -12.64116 | -63.13364 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b236b65c-841c-3867-a27b-5cb78198c895 | -12.38475 | -63.00409 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0111cfa0-31ce-3d12-9150-b4ceecb3e678 | -12.99907 | -62.71524 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc715de5-0427-303b-b841-e4f8d47c6de1 | -12.98662 | -62.71021 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1da41905-fa43-3308-aad3-838f03767157 | -12.98311 | -62.70793 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 15bcff66-6e3a-3dc4-8b62-8d24dc50784f | -12.98105 | -62.70908 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fc465e7-2aad-33ad-9ab0-aed334ed624a | -12.96876 | -62.6338 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66f10d76-3c6a-3e8f-8de3-8c8d6d182629 | -12.96204 | -62.66784 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a69f5f58-0096-3760-817f-6638b1fafdb5 | -12.95903 | -62.68312 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 033cbc82-2053-33c8-89ed-598c7e0d1944 | -12.95827 | -62.68694 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29685502-741e-3035-b1e2-876e6e82b919 | -12.95752 | -62.69078 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0d48ee4-4a77-383b-bb14-e2e6bac00b65 | -12.95676 | -62.69462 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0c94285-70d8-313e-8061-24100613f151 | -12.95647 | -62.66677 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 413a78dd-8934-3485-a095-e19018c4b22c | -12.95497 | -62.67438 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be644c83-17a8-36bb-be9f-6f60f21ba0bc | -12.95421 | -62.67821 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 647141be-c0f8-3aaf-bca9-ef84d1b38fe8 | -12.95269 | -62.68588 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7124e95-f816-3a80-8767-3344901498a4 | -12.95118 | -62.69353 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5684ce35-f750-3cd0-a6df-ecfc7f3bbde8 | -12.95042 | -62.69735 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 544e837b-5574-32a5-bac0-427d1724bbe1 | -12.94485 | -62.69625 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3773ea54-85f6-3465-a04b-45b47164e72b | -12.9441 | -62.70004 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aa110f2a-80c0-3b1f-8bd0-997c47c318c8 | -12.93927 | -62.69514 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6bda70c4-ac29-3660-a84c-48a2b30feff6 | -12.93852 | -62.69893 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2154108e-09a2-3b4b-af24-d37d974c2358 | -12.93294 | -62.69783 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 837aae1b-2b6b-3a3a-afb0-e16b02d858b6 | -12.92736 | -62.69673 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 577d0145-ed67-31bf-8c56-cfc5d5f94fc0 | -12.9266 | -62.70053 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 688cf87c-ca2f-344a-8ed9-f7e567e4cf2f | -12.92101 | -62.69946 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac228535-919f-38b4-9efd-ef2b1d614811 | -12.91544 | -62.69834 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d50cc67a-b5d7-33f0-ac39-86a8a04b8698 | -12.90133 | -62.66055 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81c73314-8fe0-33cb-837c-b38b58363261 | -12.90007 | -62.65942 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e85a116d-b6f7-3daf-9c7f-8595bd92818d | -12.89931 | -62.66324 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4151a1ac-953f-3dd0-a7b6-6e06f18157ac | -12.87887 | -62.77624 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 141bc610-af6e-3802-b412-bc8e9bac1a06 | -12.87679 | -62.77476 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f227bbf-a350-31c7-917b-4885fe06e665 | -12.87601 | -62.77864 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c767d96-a950-3c0a-a84a-f9c2e740577a | -12.87401 | -62.77122 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e39ec59b-0669-3061-bd90-846418f9f28f | -12.87326 | -62.77512 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 915b3017-97cc-3db9-834c-380ab8fdf211 | -12.8725 | -62.779 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6162b66-b419-3625-a405-088d72513dee | -12.87118 | -62.77363 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fefb1ac0-fb31-398c-9db5-f7f9f00484d5 | -12.8704 | -62.77752 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2493d82-4204-3f30-b407-dbc6bef28700 | -12.86961 | -62.7814 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2b2d3e9-cfec-3b7c-b5bd-9bd0810fca47 | -12.86765 | -62.77398 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 709c8535-75ef-32c7-9592-897341a89f90 | -12.86689 | -62.77786 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9076773c-c3b7-3675-97c2-f0bbfc8c9666 | -12.86613 | -62.78175 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95d04d13-71f5-3ed5-97a9-b034785c75f1 | -12.86439 | -62.85066 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aefb10e4-3fee-3f07-9ed0-36c62c4c3aa7 | -12.864 | -62.78028 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d186ed6-56f9-3d0b-b4d0-8f745d634e29 | -12.86177 | -62.84903 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6ce55742-a649-3731-bfed-7dd418aa9d8f | -12.86052 | -62.78061 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebbb72fd-0de6-3d34-8863-8f653565edd2 | -12.85976 | -62.78451 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb0423b9-08d5-3988-9f00-b6bbe851411f | -12.859 | -62.7884 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 469b26b4-b056-3e20-a47b-d907a90e91a7 | -12.8568 | -62.78694 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 74dd0d1c-c26e-3b4b-bd11-9561ca8d8948 | -12.85602 | -62.79082 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 644c9e80-5fae-3604-a840-c6633ca0a02e | -12.85415 | -62.78337 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca6b2053-b0d5-3dfc-8a84-ae844d445497 | -12.85338 | -62.78727 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4da8a95-ff80-3b2f-ac9f-47cb6aef770e | -12.85262 | -62.79115 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7094b52b-b583-3c72-b4a0-45ac7446aa38 | -12.85186 | -62.79503 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41968622-84a3-380c-8ac4-be2df1d44619 | -12.847 | -62.79002 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 934de660-916c-3466-85cd-dcf003aaaf7a | -12.84624 | -62.79391 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e024b34-d031-3143-b9ee-f1d54e3d6664 | -12.84547 | -62.79782 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68da51dc-f395-3c00-b2b5-2af7c6315164 | -12.8447 | -62.80174 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e405d05-bb96-3f5c-9327-806b91b19626 | -12.84396 | -62.71673 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 942cd07d-1cc8-30bb-931b-76b19d12aede | -12.83985 | -62.7967 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19c17c36-cc0e-3b2d-ac89-1b92f5f08ef2 | -12.83908 | -62.8006 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe7275fd-2308-390e-806b-110c3ff41ff0 | -12.82766 | -62.88839 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d459359-9eb5-3554-a8f0-8ec821f8c95d | -12.82689 | -62.89228 | 2024-10-02 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8edadec-4800-32ac-85e3-6d90050cd051 | -12.87513 | -62.52935 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.8 |
| eae631c5-f233-3612-ace5-57f59e14b005 | -12.87439 | -62.53308 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 5abdcb12-e231-3025-9d72-79d6751053f4 | -12.87035 | -62.52449 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.8 |
| c1b040cd-352f-3b97-880c-1e3f1c5c90ce | -12.86961 | -62.52823 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 6c563c42-dd8f-320e-9fa3-d2ef940376a5 | -12.86887 | -62.53197 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 78a9261e-c23d-34ad-95c0-daf3a64e89e6 | -12.86813 | -62.53572 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 08d9407d-4ad0-3468-876e-4ad342945e2a | -12.86739 | -62.53947 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b59de255-fdc8-35a5-8bd8-c592b94714db | -12.86665 | -62.54322 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 40382464-98cf-3753-9d59-2d5258b3c29e | -12.86409 | -62.52712 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ef99fca8-2d29-3072-8723-8625e7e17f08 | -12.86335 | -62.53085 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eeaf4a2a-1cdc-338e-b18d-2f1e2cf26e53 | -12.8626 | -62.5346 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2009d32a-f5fe-33fd-ad60-e3eff3fd2934 | -12.86186 | -62.53835 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7f0ab1a0-11fb-39c0-8c44-d1e719d3670a | -12.86112 | -62.5421 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| be1143e5-118f-3a87-a4d5-6ac862cf53ff | -12.85931 | -62.52226 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d5d14311-a127-39da-aaca-7ef8fa80e7cb | -12.85857 | -62.526 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 49895036-2f02-3ae6-a995-bdd88d9989d3 | -12.85559 | -62.54099 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8040ed36-43ca-332d-9045-b877153a76ab | -12.85485 | -62.54474 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 7d3be51a-03b1-3081-99be-a1c4598af112 | -12.85411 | -62.5485 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d150ace5-951b-3107-8558-def889419855 | -12.85379 | -62.52113 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59da303d-20d5-3379-aef9-e965a7d0e046 | -12.85336 | -62.55225 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| de0392c8-602b-36f1-ae3b-1c8d92003266 | -12.85305 | -62.52488 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 750428e3-a692-317e-9d34-cc28255fccdd | -12.85262 | -62.556 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c093648a-c65c-3020-983a-a59e0fc4583a | -12.85156 | -62.53238 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8eb378f4-4457-3ce1-83f2-00ac8ca420b0 | -12.85007 | -62.53988 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 24e8c4f1-7ee7-3ca7-8d7b-6e10470ec0a8 | -12.84932 | -62.54362 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 50e9f991-c73e-3361-93b9-6c0294d75d2c | -12.84858 | -62.54738 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6b374c01-980e-37a4-a016-8a2b5f59b48c | -12.84827 | -62.52002 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea4e6367-5653-3c05-8c3b-a80699801518 | -12.84783 | -62.55113 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f85cc6e7-eab8-34ab-b523-e1284c986118 | -12.84753 | -62.52376 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e387871-8e3e-3990-b6e6-503c88bfe88b | -12.84604 | -62.53124 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0e55186b-e577-3cc4-900e-25e1b24d3802 | -12.84529 | -62.53501 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bc0a87f6-7707-3d8a-9c3b-7ae92b663eef | -12.84379 | -62.54251 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e1ec749e-ca31-3ccf-9132-e4a59d59bf7c | -12.84305 | -62.54626 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 107e3902-7f55-3962-a666-f62b1b8b4045 | -12.842 | -62.52265 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ead59815-a36d-3d73-8a4b-83e6a14cde63 | -12.84126 | -62.52639 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f7edd7c8-35c7-3d14-920a-bb3275609a7e | -12.84051 | -62.53014 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 684ed827-b2d1-38a4-8d8f-9163e19af4e5 | -12.83976 | -62.53389 | 2024-10-02 04:49:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README116.md)
