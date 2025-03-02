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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f02e7e0-70f0-37b7-90f4-406c532ff65e | 1.03452 | -59.56336 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70714869-3816-3445-b9df-42d1dfa2095a | 1.31187 | -60.07102 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5847803-8a18-3d90-85bb-5f69ca428799 | 0.87952 | -59.44187 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfa7db92-c130-3b98-8bd5-c2f08dcba5d1 | 1.11118 | -59.35102 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 473feda8-bd81-3b15-947a-b80ed96efa33 | 1.32258 | -60.42682 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a48ab1bc-b672-3b68-9dc8-40e75c65f979 | 1.65683 | -60.28735 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52c49803-48c5-3947-b046-e4bc2d32ed7e | 4.34786 | -60.35994 | 2025-03-02 04:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d09b58c4-24bc-3409-9b72-8d91cc18b911 | 4.30892 | -61.05832 | 2025-03-02 04:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df4ecc87-a4bb-3ba5-963f-17e2df39cdd6 | 1.327 | -60.42613 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a2bf53d-bc4a-3f48-8811-e6a3d104f58d | 1.58953 | -59.96832 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc8ecd83-350a-34f7-8f0e-f069f31d8df5 | 0.97348 | -60.52854 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f53e9a5b-ccac-3129-b505-f2d46bf3295c | 1.42628 | -60.79866 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a64dee45-9822-32b6-a7b8-e72a862ea12c | 0.77465 | -60.55206 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a56b7a0-e6f9-3087-8e62-10357729e77d | 1.94153 | -60.38564 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5146006b-4049-3274-8289-49f3dacb12fe | 1.18528 | -60.2077 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32dcd231-50d8-3774-8eec-b047c8bab0ec | 3.90691 | -61.70906 | 2025-03-02 04:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64230c67-75ce-30de-b248-3b0cb6217bf9 | 0.70836 | -60.27566 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2251efee-c03a-3fc2-a43b-e7954ab5185d | 1.84036 | -60.31034 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eda2882e-f2f7-36b3-9770-45e64f6d3a14 | 0.96129 | -60.53358 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0224c30e-1389-3062-8e4d-80b0bfdc8848 | 1.07424 | -59.54562 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c1ea93-62d8-3ba6-a39f-60907e7e4dbd | 1.31816 | -60.42749 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba3aab58-ade6-375d-9461-e3d41636b23f | 0.67719 | -59.64019 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2713a963-6bee-310a-b49c-a281213cf2cd | 1.11048 | -59.35156 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f964457-122e-3140-8e50-72637c6f5760 | 2.58202 | -60.62209 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 24c327ad-ad35-3ab3-857c-80fa572acee4 | 2.41073 | -60.0051 | 2025-03-02 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7964699-9391-38f7-84bd-72cdec983fe0 | 1.20099 | -60.51504 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7f62258-cdfc-3cbf-b78c-771659bf2f2a | 1.65617 | -60.28308 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ed3f01c-914d-38a7-b8e6-bdd826a4662a | 1.03711 | -59.56663 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23f26e6f-b609-3551-80a3-09ece94987ec | 0.77398 | -60.5477 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60f53b68-763d-3fee-9a53-7a6b9a6e70f4 | 3.64909 | -60.79756 | 2025-03-02 04:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bded1de3-3b8e-37ac-9d02-8c5da462e102 | 2.11441 | -61.81516 | 2025-03-02 04:59:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 865cc513-548b-3438-bc4d-709788baafb9 | 1.10614 | -59.5868 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f92f0680-d515-36a4-ba2f-b51f7af1329c | 0.81076 | -59.63933 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abf6796d-1489-36fc-8f5c-9b8da7f3c8f5 | 1.31122 | -60.06692 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd3fe752-24fe-3705-9c8d-c860610aa480 | 2.58274 | -60.62673 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 44971514-49a8-31ce-af29-921953c2fc40 | 0.66396 | -60.30373 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60fd05f0-0b2d-3de9-8208-2c92375e3935 | 1.3195 | -60.43618 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3dc8efdd-d8b5-3386-b873-c2493232eb83 | 2.19328 | -61.85872 | 2025-03-02 04:59:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26d2d9a7-587c-3e6f-a01b-f51d130491de | 1.11176 | -59.35465 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0b49d01-ff70-3757-b989-8cc8ae984341 | 0.96502 | -60.52856 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60a72d9d-b8dc-32a2-a8ed-05d961b6027b | 2.37508 | -60.4593 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a14dee6a-5295-3668-b767-262b57e3cd86 | 1.99482 | -60.55543 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 367cf81c-3cd1-3b38-9005-d6c6fd03800e | 0.76957 | -60.54839 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d6b6364-318e-357e-9af7-56cde83d1fb5 | 0.96945 | -60.52789 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9295b1b-de3f-3a79-8bcd-0ec4e225d5e7 | 1.32325 | -60.43115 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1dfd8338-7c5f-31b5-8189-205ad3fd16af | 0.70337 | -60.27219 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04bda470-93c5-305d-9a5c-435f7d8c2f4e | 1.11103 | -59.3552 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41d50da8-3a03-3a18-9b9d-1ce3c5e5ffd1 | 3.65378 | -60.79684 | 2025-03-02 04:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c70ef4c5-7fda-3d7b-b1de-e7dbdaba437c | 0.96397 | -60.52554 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ceb7dbb-9703-345b-8b1e-d407d6503f36 | 2.11525 | -61.82063 | 2025-03-02 04:59:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 408209d1-507c-3fa6-b141-f029c94c820b | 0.96876 | -60.52356 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a8ca5d7-c957-3440-b482-1a381ba340b4 | 1.43082 | -60.79795 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdd39bfa-f105-3301-8356-4f9e957ca56e | 1.01523 | -59.5895 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de2be840-dade-36c5-93dc-2203cb6824cd | 0.91398 | -59.34494 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1659e389-949e-34bd-934f-e57c117dea64 | 1.07483 | -59.54942 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfe01c45-43bd-3519-b90f-5eb371ea3c0b | 0.9606 | -60.52924 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 097c04ff-c229-3420-af5f-93a7ba5fc3fa | 1.93839 | -60.39494 | 2025-03-02 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6717642d-696e-3bff-96fd-636f30ae265d | 2.18748 | -61.85387 | 2025-03-02 04:59:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc1ad3d6-e5b6-3c96-af21-413d452adbd2 | 0.68133 | -59.63953 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10b6d9c5-40e6-3ceb-9b59-9585296eadc6 | 1.69315 | -60.23068 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90cddbcd-1793-3769-bcec-066fa7fc7fbf | 1.03651 | -59.56288 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbe021c3-f209-3329-a18e-c15681ca6e26 | 2.18832 | -61.85941 | 2025-03-02 04:59:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d4081d0-612d-3848-9c7f-a6f831e893eb | 0.90989 | -60.37926 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af781537-be11-312c-9c40-a053a7f8083d | 0.87522 | -60.24311 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc37db01-3bfa-346a-bb58-b60efb07fd08 | 0.64397 | -60.0084 | 2025-03-02 04:59:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1524e04d-d420-3eac-b833-677d34c59a9d | 0.81136 | -59.64313 | 2025-03-02 04:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cc0ad87-fb2b-3bc5-b034-47810bd1fb58 | 1.31883 | -60.43184 | 2025-03-02 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2338c513-9d1e-33e4-8c4a-9f2df2cb903e | 3.52798 | -60.45758 | 2025-03-02 04:59:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45c9a278-7f34-36bc-907d-ea265f3c90bd | 0.96463 | -60.5299 | 2025-03-02 04:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86b8d915-3f82-3acf-b311-151d7c78a154 | -13.99 | -45.5907 | 2025-03-02 05:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| ace567e1-1ea9-38a3-918e-b010624c7a6b | -14.0095 | -45.5874 | 2025-03-02 05:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e8028539-3bf9-39b5-a488-0d36d03aa85b | -0.02599 | -60.55971 | 2025-03-02 05:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fe5d528-fb35-3c3d-aced-cb496cb0a1e5 | -14.00772 | -45.6018 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f0998ca2-1c53-3dcf-8823-58d8191b0a76 | -14.00254 | -45.59075 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b875aa94-0d28-323e-ba7e-f8e0516026b9 | -13.97784 | -45.58265 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 104c578e-9aaf-37d5-95e0-38737e809720 | -14.00197 | -45.59594 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 29d020e3-4210-3edc-bb4c-13ddf8c98df8 | -11.45056 | -52.92044 | 2025-03-02 05:03:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1871b36-9bdf-39e8-89b0-f364edb5066d | -13.97672 | -45.59293 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9dbce950-ef1c-3908-a01c-5e7eaf37fe29 | -15.85422 | -54.12547 | 2025-03-02 05:03:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d44efed-0cc9-3b51-828e-4fc64806d7e9 | -14.00829 | -45.59663 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0e430bf8-fc0b-3adf-93cb-e60e67b1cf0e | -13.97153 | -45.58186 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee27d86b-61bc-399b-92a5-d19f84df4db2 | -13.98247 | -45.59883 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 779ca2e7-46c1-3c43-8773-0a9a828bc24f | -14.00311 | -45.58556 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4e78536a-b6af-31d1-8cd8-0c520e447d2e | -14.00368 | -45.58036 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3b6e5922-2a21-3356-9a30-aba742dc8d93 | -13.99736 | -45.57966 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 14095c28-dbcb-3c0d-b791-d75fa582a79f | -12.84768 | -43.82814 | 2025-03-02 05:03:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e5ab5c3-9689-325c-89ad-3c6df1a2a31f | -13.99793 | -45.57445 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7c03ed69-4bd7-3f3e-a7ce-5c5eea905d0f | -13.97097 | -45.58701 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a54bdf94-4a26-37e0-b88d-6684cf745c83 | -14.0014 | -45.60109 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 30830845-e4ae-3b07-9dd6-435dd64ccacf | -13.98303 | -45.5937 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d187106e-7f72-3645-926a-ad1b58dd6e82 | -13.97728 | -45.58779 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b77f531-df74-3838-99e3-748bd2abb27c | -14.00084 | -45.60623 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 21e9f1ed-23e8-3d4f-bf12-bf09b37dcdf5 | -13.99622 | -45.59006 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65ce6f92-b55a-3816-8265-1a1428b82a9f | -13.99679 | -45.58487 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69bd8980-739c-3180-8097-4acdb085e214 | -13.9784 | -45.5775 | 2025-03-02 05:03:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 35c3f35b-e4b6-3508-a729-0115fa9f2360 | -20.88275 | -54.79085 | 2025-03-02 05:05:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74572d0f-8e01-3459-af51-b1393acf3aef | -20.88211 | -54.7958 | 2025-03-02 05:05:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 236ebed0-aa80-3bd3-acc4-132c0feacf90 | -22.8417 | -51.05983 | 2025-03-02 05:05:00 | NOAA-20 | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 807f3d31-2f34-3978-9aff-7dfd4bd3276c | -20.39352 | -49.11367 | 2025-03-02 05:05:00 | NOAA-20 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0d33c7c4-ebd4-375c-b70e-1367767c35aa | -17.3325 | -53.73255 | 2025-03-02 05:05:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README6.md)
