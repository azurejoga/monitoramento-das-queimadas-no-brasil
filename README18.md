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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6cf2758-fe89-34be-9478-f99928a182fa | -14.2247 | -45.5036 | 2025-06-30 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 4be95a78-e251-3d0e-b700-7b7639216829 | -12.5175 | -57.2231 | 2025-06-30 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 9b1b1e69-85c6-36ec-ac66-a239c25fd1cc | -14.2052 | -45.507 | 2025-06-30 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 46c24975-3e58-3247-89f3-d688c1cf6133 | -8.5722 | -51.5761 | 2025-06-30 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 66737e7a-70d4-3122-9dc4-b704ca7650ba | -14.2247 | -45.5036 | 2025-06-30 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 43e394de-e142-35f8-a9ea-c48ebc2e188b | -11.5812 | -44.6554 | 2025-06-30 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 1076bce0-2aa6-3dc1-9843-bebfa6ea81fa | -7.7133 | -47.8453 | 2025-06-30 12:40:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e6cad4b4-547c-35ba-9043-96e7e0ebe54c | -14.2052 | -45.507 | 2025-06-30 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| d8e4d329-387f-3636-9525-02a1adf1b23d | -8.5722 | -51.5761 | 2025-06-30 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| bfaf72cc-6833-3d12-a901-7e9bac5256d3 | -11.5779 | -44.8413 | 2025-06-30 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| c595bcfc-ee2f-3c50-afef-5b547ac1740e | -7.7346 | -47.6025 | 2025-06-30 12:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d2abbc02-62dc-36a2-8edc-79c8287d500d | -14.2242 | -45.5269 | 2025-06-30 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 975aa423-fd79-3922-8288-5126e3b93b65 | -14.2052 | -45.507 | 2025-06-30 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 219.8 |
| d07ef36e-ec85-308d-82a9-ce785669073f | -14.2242 | -45.5269 | 2025-06-30 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 0fa93ce5-91a7-3f17-8ac0-027d2c42f025 | -11.5779 | -44.8413 | 2025-06-30 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 35de22e8-18d9-345b-b432-841b8de797eb | -14.2247 | -45.5036 | 2025-06-30 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 9f67e2d6-7101-3a0b-ac5b-054f136b5769 | -11.5812 | -44.6554 | 2025-06-30 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 30c517b7-2a36-3fda-b8ad-aa68c05807b0 | -8.5722 | -51.5761 | 2025-06-30 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 06bf05c7-fc8e-3ebf-b2e7-52062ca72ebe | -8.5722 | -51.5761 | 2025-06-30 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| ff20d9aa-cb1d-30d9-9e36-7c042605d175 | -14.2242 | -45.5269 | 2025-06-30 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 293c7856-2ecb-32b6-bb71-06883218235f | -11.5783 | -44.8181 | 2025-06-30 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 8f8d4903-31c2-3b8a-9159-d74b7a6b341f | -11.5779 | -44.8413 | 2025-06-30 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| d5fffeb0-cc94-3e09-99c9-5052fb9c18c7 | -7.7133 | -47.8453 | 2025-06-30 13:00:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3c546ccc-bb6a-3bcf-92c6-06bf515a444e | -14.2052 | -45.507 | 2025-06-30 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 236.7 |
| b98788c5-ec2f-3fa9-b6b3-57e607472f28 | -11.5812 | -44.6554 | 2025-06-30 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 177.9 |
| bdf421bd-5e81-38dd-b91f-af3cb53004fa | -14.2247 | -45.5036 | 2025-06-30 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 9b14dcb6-12cd-3a01-8cd5-9c4c05ddf5cd | -11.6004 | -44.6525 | 2025-06-30 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ec49e2c1-04d0-3dc3-bf1d-a1bb3467b2da | -11.54442 | -52.78101 | 2025-06-30 13:06:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 7902d1dd-c5c2-3b48-bd64-8be1ce98b293 | -10.86826 | -53.78249 | 2025-06-30 13:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 8e5a98f4-c975-3239-87a4-a562cb1c2487 | -10.8701 | -53.76825 | 2025-06-30 13:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| b5eaba33-a212-3727-9794-d9077ef6d6d4 | -8.57515 | -51.56514 | 2025-06-30 13:06:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 98daad6c-bf51-38bf-b3a5-ddf922cef73f | -10.2966 | -57.13793 | 2025-06-30 13:06:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ce433c03-a337-3933-9e2f-061f4254bb0c | -7.71984 | -47.83637 | 2025-06-30 13:06:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 3765dfc3-c336-3f6d-9d77-14d69228ecd0 | -8.57264 | -51.58496 | 2025-06-30 13:06:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9793432e-1a3e-3931-81e1-735b3128e9fd | -7.73842 | -47.57357 | 2025-06-30 13:06:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| a586c1c3-9199-32fb-a451-20aee2551d61 | -11.02574 | -56.27022 | 2025-06-30 13:06:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 359b9ce9-e844-3c00-8302-3569fb607d55 | -8.55999 | -51.58314 | 2025-06-30 13:06:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 34ce2b1b-45fc-318b-9660-ef908ece9ad3 | -10.30054 | -57.04402 | 2025-06-30 13:06:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 697caf91-0bf9-368a-b74c-6262f50f871e | -7.72418 | -47.84394 | 2025-06-30 13:06:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 5e774ceb-9c22-332c-b201-5ba6aefdb525 | -11.54871 | -47.87443 | 2025-06-30 13:06:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 0c35ebbf-52e9-34f2-a057-6870abe81e8b | -10.13268 | -57.77368 | 2025-06-30 13:06:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7fad183e-7f64-3457-a815-08a678df2d7e | -9.24415 | -58.75181 | 2025-06-30 13:06:00 | TERRA_M-T | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ed34d4d2-3e8b-3c48-a3c0-519285302a01 | -7.73389 | -47.61282 | 2025-06-30 13:06:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 7d08afec-ff63-31d1-8da8-76924c1dce06 | -10.12384 | -57.77242 | 2025-06-30 13:06:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 862d902e-f24c-3562-85e5-391659ac0dd3 | -11.20957 | -55.91992 | 2025-06-30 13:06:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 97c80eeb-7cd4-3411-b7b0-1ce118685a17 | -9.08899 | -59.49274 | 2025-06-30 13:06:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2fb58d87-dfe7-38d3-ba56-eb5e116d4992 | -10.86275 | -53.73802 | 2025-06-30 13:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 1c6e9f1d-dfac-3843-b337-fc854ba4af21 | -10.29789 | -57.12872 | 2025-06-30 13:06:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 32f7c7af-7629-324a-a62d-72565a7a9f19 | -9.54142 | -50.73821 | 2025-06-30 13:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 6172ab29-713c-3c49-a5de-cb8d86687b94 | -10.10092 | -51.57112 | 2025-06-30 13:06:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 35.2 |
| ef2e7d4c-c5f2-3aec-b715-6939950faebe | -8.56244 | -51.56353 | 2025-06-30 13:06:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 95fc9635-9d5f-3ea7-8f16-cbc87caed931 | -11.58619 | -52.11878 | 2025-06-30 13:06:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3192cc4d-79d2-3922-876b-faa85f4bfce7 | -10.82677 | -53.74189 | 2025-06-30 13:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5ed95268-67cf-3d3c-98f5-98a1fbbe4c9e | -11.54862 | -47.88148 | 2025-06-30 13:06:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 997ff667-b483-39ba-89bc-891864a48fc2 | -9.35877 | -58.8481 | 2025-06-30 13:06:00 | TERRA_M-T | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 804f19c1-3795-384d-8b83-170723a59c72 | -7.73107 | -47.60535 | 2025-06-30 13:06:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b4608213-243e-3d1e-b015-ae5e2bc833cb | -10.1028 | -51.56576 | 2025-06-30 13:06:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 38e47038-f843-367b-82ac-d66f19ac4035 | -11.13658 | -53.92219 | 2025-06-30 13:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 14be24e8-9296-3afa-9490-9e5f26b6b45d | -10.30557 | -57.13916 | 2025-06-30 13:06:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d7686a44-6f4f-3a6a-a764-6da9de790088 | -9.53372 | -50.74378 | 2025-06-30 13:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| cdfbe123-fc2a-3079-824c-674edaad5641 | -9.71032 | -56.18476 | 2025-06-30 13:06:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5586c357-cb98-319a-8509-91bf46bce47b | -11.11928 | -55.44287 | 2025-06-30 13:06:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 97529495-9602-3891-b977-49c7de40122b | -10.1034 | -51.55051 | 2025-06-30 13:06:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 72534e65-9896-37cc-8c18-5df809855952 | -11.20003 | -55.91864 | 2025-06-30 13:06:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b0a4fbfe-c9a6-3258-99be-56bf5ec9eff1 | -12.63486 | -54.21967 | 2025-06-30 13:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4607063d-91b3-33f9-b501-d803084d4a68 | -12.62568 | -54.20412 | 2025-06-30 13:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 654f090e-4c40-3e32-bed1-891a191e1027 | -11.81484 | -57.3527 | 2025-06-30 13:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 56c06374-fdff-33bc-9de4-c048c0c83961 | -11.9403 | -57.44278 | 2025-06-30 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e6c546f8-d971-3803-ad02-0324f739b1bc | -13.49339 | -52.94876 | 2025-06-30 13:08:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c624133d-c4d8-3dc7-993a-f1f7d8213795 | -12.52313 | -57.22635 | 2025-06-30 13:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| d426761d-c4c8-321a-87a8-32e19ec0f27a | -11.939 | -57.45206 | 2025-06-30 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 0f444b43-2342-3803-ac68-6710b412544d | -12.52065 | -57.17722 | 2025-06-30 13:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 7bbcee99-05ba-30dd-ad31-2656f412bb6d | -13.4842 | -52.95417 | 2025-06-30 13:08:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9e4dc83d-38d6-3ae8-8091-48661d833eea | -13.54559 | -52.96175 | 2025-06-30 13:08:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 544dfb21-9755-3164-92d9-5def0533ac1e | -12.09775 | -54.67057 | 2025-06-30 13:08:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 28e437b9-258b-34ef-a620-70e5d6e70161 | -11.93003 | -57.45078 | 2025-06-30 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5d6f672e-e22e-373a-8836-b58ac911c13b | -12.52445 | -57.21679 | 2025-06-30 13:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 77715cef-14e3-3b1f-8230-c3d0c8c4d7f1 | -12.52181 | -57.23589 | 2025-06-30 13:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dabbcc60-abc7-3f1d-ad5a-d20b70d08c8e | -11.91675 | -54.8163 | 2025-06-30 13:08:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 71eec502-d223-3906-af0a-7301595b89a0 | -12.28699 | -57.26804 | 2025-06-30 13:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 886566a1-ee55-353a-9244-2cd405f2ea0d | -13.49113 | -52.96701 | 2025-06-30 13:08:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 7afe8b7f-21c7-3c3e-96e8-409e841dcecb | -12.62391 | -54.21828 | 2025-06-30 13:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 3e0cff67-f8c1-31bc-a3fa-316d46bcc4c4 | -13.49648 | -52.95567 | 2025-06-30 13:08:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 1b85ac64-b7d2-3bca-aed7-0f9d690280ef | -12.52577 | -57.20724 | 2025-06-30 13:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a055250e-c21f-36fb-8b66-eaa3c5fb803f | -13.80426 | -54.30253 | 2025-06-30 13:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| df48d728-8cb3-31e4-bff2-b6ceae429a1a | -11.5779 | -44.8413 | 2025-06-30 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 0cbef495-6db6-3148-bb21-5262483dc41e | -14.2247 | -45.5036 | 2025-06-30 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 904cc009-f766-387c-a2ce-e764789f5ac1 | -14.2242 | -45.5269 | 2025-06-30 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| da83ee19-c791-357c-8ae5-365b6c1c0700 | -7.7133 | -47.8453 | 2025-06-30 13:10:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 543b72b2-b94e-320d-9195-cb67ebb79080 | -11.5812 | -44.6554 | 2025-06-30 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 4c7a00eb-8d79-3966-baf6-affb6f158005 | -8.5722 | -51.5761 | 2025-06-30 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e3b092b1-d564-3a92-a3d6-89e248a908ea | -11.546 | -47.8772 | 2025-06-30 13:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5974f420-6fdb-32fc-9cb8-c4c99ade0d9d | -11.5783 | -44.8181 | 2025-06-30 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 60e36def-75b5-329b-acc4-828d1db0f3ca | -14.2052 | -45.507 | 2025-06-30 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 4623826c-7d35-3987-a932-469ed40b37ef | -11.546 | -47.8772 | 2025-06-30 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 79236a81-fde8-314a-ae00-df4a7ac9e4de | -14.2052 | -45.507 | 2025-06-30 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 300.1 |
| 7f936723-49fe-3608-9201-da4fdfe86c70 | -8.5722 | -51.5761 | 2025-06-30 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 335562d7-09c9-3939-a0cc-3135afc20c5a | -11.5779 | -44.8413 | 2025-06-30 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| cfdfe1bf-5f08-3fc4-a43b-0e295c4b18f2 | -14.2242 | -45.5269 | 2025-06-30 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c56598e7-dc78-376a-b53c-41db391c8a20 | -11.6004 | -44.6525 | 2025-06-30 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |


[Clique aqui para ver as próximas entradas](README19.md)
