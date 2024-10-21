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
| 86fec70f-841d-3b17-855f-fb335f37bf87 | -18.29316 | -56.15506 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e98c4138-cc15-3afb-82e0-2ae2de9a2eb2 | -18.29277 | -56.17921 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 36d3b86a-9724-3f3a-bd30-2ebc26681c6b | -18.29233 | -56.15974 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 861635be-5fe8-3676-8383-76f150de231d | -18.29151 | -56.16443 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 70810002-a871-3b54-9cfa-8f8d2859aafd | -18.29069 | -56.16911 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5f707c1a-bb41-3eb0-a4b8-33e313539b03 | -18.28944 | -56.15433 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ce451096-5757-37fb-8063-881257994227 | -18.28862 | -56.15901 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 183c8d85-4167-3af6-bb44-3500f675b5dc | -18.28779 | -56.1637 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a74bff2e-986e-3b90-8c42-0b33bf63adc0 | -18.28072 | -56.09479 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 0dfc3c1e-3ef5-3fe8-82ba-9a8723207b4e | -18.2799 | -56.09943 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 95307492-53ea-3970-8d3c-b345dda2fa96 | -18.27783 | -56.08942 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f2a5b22c-9ff8-39ca-a67b-23391b05e878 | -18.27701 | -56.09406 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 17eb245e-1284-3518-9657-9d3067f67f3b | -18.27619 | -56.09871 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 71ee7363-ce0a-3062-aca5-7aae9ce45b04 | -18.27537 | -56.10335 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 34d9f74d-7125-38f5-b44b-b3abee56f530 | -18.27412 | -56.0887 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 57b4b96d-39a5-3597-a73f-647e4b99314c | -18.27331 | -56.09334 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 821f7dd1-7328-39f2-9bd0-9a547c32c16a | -18.27248 | -56.09799 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 203e85ad-624a-3cae-9dd2-376284a6e046 | -18.27166 | -56.10263 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 49970384-f13a-3677-b1a0-2256bbf12cf2 | -18.27124 | -56.08334 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3e6a3fa1-513a-3258-a665-8013df292a3b | -18.2696 | -56.09262 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bc9b7b88-94f2-36da-adbe-8f6432412a48 | -18.26754 | -56.08261 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 39313517-ce71-38ed-84af-e821beb90bc8 | -18.26671 | -56.08725 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f80aa2d5-d65f-3d89-b35b-a6d1bd125430 | -18.26641 | -56.67594 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3ff75944-3098-3518-b4a3-aa2bfc4b88c3 | -18.26301 | -56.08652 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4566f180-2260-339b-8546-dff2e1b4c3ed | -11.86975 | -56.88481 | 2024-10-21 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 288f1d79-72f7-3374-8e8e-99231355bd37 | -11.86698 | -56.87561 | 2024-10-21 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 376be628-a0e2-39b7-a00c-8dea6ee42e60 | -11.86622 | -56.87975 | 2024-10-21 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a30826e3-0b46-3d1a-943a-9bdb3a30d7be | -11.86545 | -56.88396 | 2024-10-21 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d43f01f4-3c42-38cb-b041-e5f47293a5c0 | -11.86493 | -56.87674 | 2024-10-21 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1af2743-6215-34a2-9ee5-0e024fa5002f | -11.8642 | -56.88091 | 2024-10-21 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38710357-cfb5-3fdd-945e-72d123a398ca | -11.86347 | -56.88513 | 2024-10-21 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 790ccc01-31a8-3c8e-bf05-11c60cc24f0a | -11.86268 | -56.87477 | 2024-10-21 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5432667-a592-3149-aa96-d2e28f587c25 | -11.86193 | -56.87889 | 2024-10-21 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4145b7bf-1aa1-396a-b7c4-b0d731205df3 | -18.08797 | -57.35896 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d23c6db6-0066-3889-86c6-423a989caa10 | -17.92541 | -57.46346 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4c3fb55f-0698-3c23-ab4a-18c2d72aae06 | -18.0176 | -57.30727 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b86d1541-3a6c-33b2-a686-1c0c69e71c47 | -17.9945 | -57.4315 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5a859b18-bb39-3022-9599-23d9510b3396 | -17.99382 | -57.43518 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2a040336-87e4-39a9-83c6-2b435aeac49b | -17.93681 | -57.46964 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a2844055-1712-3aa0-9c4e-448c01ea1184 | -17.93278 | -57.46881 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 95e3e9c7-ddc7-3ef9-bbba-4419bd392b0e | -17.79916 | -57.48954 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3ecece74-5352-3229-96ca-0d733f7d76d4 | -17.7958 | -57.48498 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| db31a95b-e77e-3348-8c43-791ed84baa30 | -17.78368 | -57.4825 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8a112fac-b199-38d1-a0dc-9e58472c979c | -17.76751 | -57.47921 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 75d2face-bf50-32ae-b12a-fa63264a078b | -17.76681 | -57.48294 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 88f1b716-f157-3492-8f5e-d965ddf30c59 | -17.76427 | -57.56434 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 587f258d-44a9-35c6-ac54-6a9bc0615fd1 | -17.73041 | -57.4756 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7a3ff764-5749-3e9f-ab04-cd19af2697e5 | -17.72973 | -57.47935 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9666de07-479a-3540-907f-169f8723484b | -17.71697 | -57.45733 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d9fb1bef-8179-3973-ae99-5716911f9878 | -17.71628 | -57.46106 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 38744653-db96-3831-8d65-8b0ac57b0c0e | -17.7156 | -57.4648 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c6afc2f3-1433-3f6d-8a16-d2f988450de0 | -17.71492 | -57.46854 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e5e1ffff-dcf3-3384-8c9d-f6ae7718fac0 | -17.71224 | -57.46024 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a7dd6199-8ea0-33ae-b95d-952f824e508e | -17.71156 | -57.46397 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3e91c698-f004-3b85-9c76-4bd13068c251 | -17.71087 | -57.46771 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f8616bb1-0a06-3aa9-b2d2-61b3e583290a | -17.7082 | -57.45941 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 54d23963-bec3-3403-89b8-23b271f9eca4 | -17.70347 | -57.46231 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1756a46e-7cdd-337c-9282-91c1839312e3 | -17.68877 | -57.42835 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 28e01418-4659-3a55-b50a-570e4bd49824 | -17.6874 | -57.4358 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 29efb6f5-dfa3-3658-a06c-cc790efbca35 | -17.68671 | -57.43953 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f93c2110-e53f-331e-abb4-630e11383e4e | -17.68474 | -57.42753 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e0f5b672-77e7-3068-8e92-e4f51e4cc336 | -17.25076 | -57.30309 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 76e1f44f-e3fd-3148-b62b-2f95c77766c7 | -17.24938 | -57.3105 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 5bd52b2e-8b04-3da2-9d97-70dbf5ea4011 | -17.22168 | -57.32481 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 37ecbc3b-30ec-3436-84d3-14fb0e54a2fe | -17.22168 | -57.3242 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 82d9a26a-0205-3fe5-b58c-d276cb2fd680 | -17.20403 | -57.50835 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bfb85958-d474-322b-b6b1-e9f79e6396f2 | -17.02325 | -57.33133 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 851f1e4e-e814-32cb-86e2-8edc59d2c0cf | -17.00493 | -57.52075 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ea365ccd-9315-305e-a9ba-5a334e7ea64e | -17.00422 | -57.52461 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b36279c6-6383-3c37-8f40-ead869a98256 | -17.00083 | -57.51993 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0c21b87a-d69f-317e-b0be-9c81a3df7432 | -16.95453 | -57.52745 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 90568410-4d34-3d2f-b972-76c6b535a34e | -18.08672 | -57.35912 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f47356e7-0671-3a5a-ba3d-3336bc256626 | -18.04879 | -57.34002 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d34a1c5f-9ca5-3619-b4e0-08b8319ecd51 | -18.04414 | -57.34284 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 63bc2602-0533-316a-9f84-30a856fad0b9 | -18.01429 | -57.30283 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 18c78305-f6b0-36c5-bb0a-0200c9c60d60 | -18.01361 | -57.30646 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7ed0b77e-8b96-3833-a66d-2bba42f473f7 | -17.87025 | -57.23726 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4c92ec0a-86b6-3010-8255-793586a7d216 | -18.0448 | -57.3392 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 289fac3b-73c1-3eb6-a0b4-c4f5153d9c9d | -18.01827 | -57.30365 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 68343117-83d0-3ac9-9775-fe1cdd5ed25f | -18.01693 | -57.31089 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a25dc568-f749-35bf-b487-a4f9da467ce1 | -18.01294 | -57.31007 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 10a2e471-b768-3648-9d67-c309e6387a36 | -17.98911 | -57.43805 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e0d7c328-01b5-3664-970b-fdddde610e44 | -17.93346 | -57.46509 | 2024-10-21 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a7609bae-1b35-346d-8358-555a3449e8af | -17.80053 | -57.48208 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7a08a12c-99a0-3904-9dc0-96fb4a92baa7 | -17.79984 | -57.48581 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cc96abfa-4f34-3959-a3d9-9efd30a80d07 | -17.79847 | -57.49329 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c50a8d83-fe55-371c-87fe-2b344a5a4de3 | -17.79107 | -57.48789 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 69958ab6-00eb-361f-94fd-b30f03dc9ff0 | -17.78703 | -57.48706 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 60f9ec72-c877-3454-b0d8-6c0c696bb4b2 | -17.78298 | -57.48624 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b44834a9-e0ac-386b-ae38-358799655baf | -17.76497 | -57.56057 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cd62b31f-ab10-3442-98e5-2df826e0c052 | -17.76356 | -57.56813 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 930a51d8-9494-3855-a454-813dc005b8b2 | -17.72636 | -57.47477 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0902ea71-7325-3c14-9fe4-85d9a4878ea7 | -17.71293 | -57.4565 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a8f94328-e63f-3059-a8e1-86a4dc744650 | -17.70888 | -57.45567 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a7b0e29e-9df0-3f10-96db-b458148f6bd1 | -17.70751 | -57.46315 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d575b978-9fe9-35c8-b531-b3acf4c3783c | -17.70416 | -57.45858 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6eb13786-6bb6-3931-82f1-a3202f070878 | -17.69212 | -57.4329 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8771ef65-81cf-3e77-9d12-af65d34f0eef | -17.69143 | -57.43663 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 98ce15b2-c911-3a39-bc8a-325b9b35db9a | -17.69074 | -57.44035 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e466493b-3b4d-3b9a-b937-65b33bcd4461 | -17.68946 | -57.42463 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README50.md)
