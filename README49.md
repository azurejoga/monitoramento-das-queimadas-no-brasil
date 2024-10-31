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
| 656327a1-0cce-32db-8beb-f8d55b47a5a7 | -19.49109 | -56.70878 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ee363b99-3aaf-3aa5-b2af-da2d0eb3e32d | -19.49065 | -56.71356 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3f352524-df18-3017-8e5f-f32ad94bccb6 | -19.49022 | -56.71833 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d9404020-54a3-3181-8dea-c75cd0a836d1 | -19.48937 | -56.66003 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| afeca0d6-c80a-35c4-8768-6b8e0d3ff094 | -19.48893 | -56.66486 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| eef7882c-418f-3b85-94cb-ca211967295f | -19.48632 | -56.62553 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 6e0f52a1-fe5a-3fbc-8394-0c17bd36b4d4 | -19.48459 | -56.71285 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6f7b5d1f-8b4f-36bd-92d4-5e36bf3ad4cc | -19.48416 | -56.71763 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d37d37e1-8066-3561-9823-22370040b56a | -19.48285 | -56.66419 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 39f10012-4869-3770-8871-7891aa58e438 | -19.47853 | -56.71217 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 45eee90d-a4b9-3161-acf7-fad4f20bc583 | -19.62226 | -56.6949 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d6aa1192-f542-38b0-bfba-60555fe40cfa | -19.62182 | -56.69971 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9bfa9ddb-5cf0-30a4-8aa7-03dc71ace8f6 | -19.62138 | -56.70452 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d3ea3064-0bd1-39ed-88f8-baa030adabcc | -19.62094 | -56.70932 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c715dfc3-c3e5-3ff6-86ae-f93f281c1f9c | -19.62049 | -56.71412 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9b1fc9c3-e92b-31e6-8846-3048fc75a9e0 | -19.62005 | -56.71894 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d06080aa-dabd-330b-b5d9-4d14082eb740 | -19.61961 | -56.72373 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| c8880daf-0d63-31fe-8dd8-e23b869110b5 | -19.61917 | -56.72853 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 182375e6-9ba7-3a3d-95c4-3ba9eea16c01 | -19.61873 | -56.73332 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| fb750ce5-6dad-33aa-864a-1fc02aebef70 | -19.61829 | -56.73809 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| e39df4d8-c238-392a-a32e-b9a6bafe2149 | -19.61575 | -56.69902 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7abfae25-e937-3ccb-8ecd-870d11bec29b | -19.6153 | -56.70384 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bf4595b9-2398-3573-9f16-b1b19b7c7097 | -19.61486 | -56.70864 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8848b128-d699-30eb-b595-0467fb84dbab | -19.61442 | -56.71345 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1c809d22-1937-3c93-a8de-11459c4aa404 | -19.61398 | -56.71826 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e3597ee2-2756-3250-b07c-d8879c295a79 | -19.61354 | -56.72307 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 72d65907-908a-3745-b4e6-03de6231ff48 | -19.6131 | -56.72786 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| eaa78bf2-d5cf-3a3d-a4f7-4059cf9155fc | -19.61267 | -56.73264 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 2a865569-d726-3c64-b967-4e918ad34592 | -19.61223 | -56.73741 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 713d65ea-11c8-3c02-88b0-051acbec52cf | -19.61179 | -56.7422 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 139ebb9d-4077-3558-97c2-0025d93f0fcf | -19.61135 | -56.74697 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| c14007b9-45aa-3b1c-90b1-a94cfef9b562 | -19.61091 | -56.75174 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 34c25dbe-89d8-3281-8992-0ed8f8e70690 | -19.61047 | -56.7565 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ce658605-d93f-3401-bc91-a8a4d871b437 | -19.60967 | -56.69835 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| cd9d4c95-5704-3f43-a07a-39e4a8f7ab0c | -19.60923 | -56.70316 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 1b33d942-a480-34be-bbc8-91ba72460cc5 | -19.60879 | -56.70798 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8db3f600-1643-3997-b6fa-cbfc9bfc9dc8 | -19.60835 | -56.71278 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 5926aff2-3be4-39c2-ae9a-441f5c0161ab | -19.60791 | -56.71759 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 81f06396-48b8-314e-b00f-07aff5c5eac4 | -19.60748 | -56.72239 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 767a7564-6004-3734-8c52-96cdb23aef04 | -19.60704 | -56.72717 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| d3ee3906-5d21-3234-9bc9-e3571ecb7ba5 | -19.6066 | -56.73195 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 42.3 |
| 01125626-e51f-356e-8cc7-c73d4771b8b2 | -19.60616 | -56.73673 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 42.3 |
| 15b99f98-a368-3924-baa9-9d60511ebd9c | -19.60573 | -56.7415 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 202.7 |
| 4faef129-adbe-3809-b2de-2b9b28148d5b | -19.63442 | -56.69624 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 52932595-95da-36a9-a52e-ff1bd927128d | -19.63397 | -56.70105 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 7b7c6dec-e619-37d0-ad50-d693ed387897 | -19.62879 | -56.69077 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 00198ca6-5c4e-3144-87b6-bbf7026c25da | -19.62834 | -56.69558 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 45be8793-3c6f-33d3-99bc-a96738e1c8b6 | -19.6279 | -56.70039 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| dca8b3e2-d7ce-3e5e-85ba-1f14cca56702 | -19.62745 | -56.70518 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| d1230fa9-1174-34b1-b1c4-6115de6d7ae6 | -19.62701 | -56.70999 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 92501981-717c-34a7-b32c-53ca7a3020cb | -19.62657 | -56.7148 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 039c2c77-0f7e-3d05-bb04-0760ebd2d827 | -19.62612 | -56.7196 | 2024-10-31 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| ad02640e-8156-343a-89e7-e464d14b67f1 | -19.54723 | -56.7107 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a06a3713-a6ac-3228-8ea7-b55a05d1ee7b | -19.54612 | -56.7101 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7e835e92-4abf-31ae-8608-b4fdefb86768 | -19.54116 | -56.70999 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4a1ea3b5-7cdd-32ef-86b0-51d27d5bf6b6 | -19.54074 | -56.71479 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 3f9688a9-1620-3c68-bd9b-b9ad2722c6e8 | -19.54033 | -56.71957 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| edaa41a2-5dd2-3f89-9cbc-9ff3ea67fd23 | -19.54006 | -56.70941 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9622ec8d-774c-341a-bc43-d2cf54f627ad | -19.53961 | -56.7142 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 43e321f2-0855-3d7f-9cd3-247b171cfe24 | -19.53916 | -56.71898 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 00ac7d4e-bc32-3e31-8982-2a3d8c17f671 | -19.53509 | -56.70929 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6a92406e-8874-32e0-917d-7a63b7a857e2 | -19.53467 | -56.71408 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 923361d8-7114-3dd6-8c2b-55233db343a7 | -19.53426 | -56.71888 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.5 |
| e72301d6-2928-3458-b42a-fafa47a911c7 | -19.53399 | -56.70873 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7043f5aa-1bf1-3f49-9442-5a30b9e464d6 | -19.53354 | -56.71352 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e6de2f92-d52e-3705-9379-bf1ff8d0c48e | -19.53309 | -56.7183 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 5d44f00e-c396-3f20-9932-3bc7f2ec6902 | -19.52902 | -56.70859 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| dff83476-e2b3-3c16-9572-efb8d53d1367 | -19.52861 | -56.71339 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 48e33247-10f6-3b92-a72a-3a11cde1d22a | -19.5282 | -56.71816 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.5 |
| bc6cb7d4-8d51-37ea-8e59-2c5b44d81e4b | -19.52792 | -56.70805 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| cb90a09b-fc1e-3c7f-ac89-5d48fff4af80 | -19.52748 | -56.71284 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 8cdcbf1a-d3d2-3f40-b469-9e4084b11ccf | -19.52703 | -56.71761 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| eb35d871-e337-3e9d-be88-dd86e6e9b709 | -19.52319 | -56.69299 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5475342e-7b83-3b26-8473-edc6578529d9 | -19.52275 | -56.69778 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6a3f1bda-a256-3eec-8627-06f2087be62f | -19.52186 | -56.70737 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 665805f4-01a9-32b3-82fc-6c3ff5f718b3 | -19.51149 | -56.68684 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 360fc3c3-3793-3147-9509-7c45f571d5b9 | -19.51105 | -56.69164 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| afce5102-41af-3f2d-b871-4474483e1777 | -19.5106 | -56.69643 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.0 |
| d3440125-a360-32a9-a5dd-b844b1a2f973 | -19.51016 | -56.70124 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.0 |
| 56d07d79-aa05-301e-b1d6-3fdebb2b3b24 | -19.50972 | -56.70603 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 374bd8d2-5adc-3805-8f2d-fd710649229b | -19.50928 | -56.71082 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 2ed1f2eb-3fcf-3aa0-9a1f-01db44176c87 | -19.50902 | -56.57899 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 59ad886c-dd44-364b-acec-f8b164e7273d | -19.50884 | -56.7156 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 39315faa-db49-3041-8a4f-116647801616 | -19.50858 | -56.58387 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 60922f93-22a2-3762-8aab-516a5adb4f93 | -19.50813 | -56.58873 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| dde888b9-9421-3f70-b364-96c4a714f254 | -19.50769 | -56.5936 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| f38e1288-ec12-3f18-96f7-0b88f60546b8 | -19.50725 | -56.59847 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e9a9469c-201c-3f1e-aa07-a73e4507230c | -19.50541 | -56.68615 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 77eb307b-e414-3d27-9016-8a6fc7ff5c88 | -19.50453 | -56.69577 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 0cdc314b-dc79-3aa7-b3e3-562ba973f8c3 | -19.50409 | -56.70057 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 1dfc5117-f1fb-3dde-b6ee-edb9c32f392e | -19.50378 | -56.56856 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| cb9fbe8e-5d27-37d5-8dd1-c8ab62571c0d | -19.50365 | -56.70536 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| ecb62ac7-3751-3aaa-8f56-b85161e4f6e5 | -19.50334 | -56.57342 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ad5ad9d8-88e8-33ac-9321-9343e3af6e27 | -19.50322 | -56.71014 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| d99899c9-07a2-37bc-a955-4ca95f195f30 | -19.5029 | -56.5783 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 8c3bd59a-77bb-3a3d-a765-938b7d61f5ae | -19.50246 | -56.58316 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| f4874459-1ecd-30ac-8808-6d5b2ce02656 | -19.50203 | -56.58802 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| be749620-1d44-3fe8-a0ce-77d91857c0fd | -19.50159 | -56.59291 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4c694c55-3250-395c-a875-8240a61d5c29 | -19.50114 | -56.59779 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d815caa7-bafc-3e36-ae62-ea31edfd6ea0 | -19.50071 | -56.60265 | 2024-10-31 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |


[Clique aqui para ver as próximas entradas](README50.md)
