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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22bb7773-a744-39a1-94e7-9eb5d88283d3 | -17.192 | -57.35655 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| acb87ba0-c028-3b8e-8658-4a97622947de | -17.1915 | -57.36171 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 86cf187c-79b1-38db-bb38-964eec75034f | -17.18573 | -57.35581 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2b1caa1d-77d0-3994-b3be-755094c4bebc | -17.18523 | -57.36097 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d1326c7d-6b5c-3dd3-adb3-d51abbe5e8c1 | -17.17548 | -57.39619 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 27400896-a63e-3c93-87e9-371a8e8c0531 | -17.1712 | -57.37494 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4ae254ef-fe12-3ded-9226-141f3daa3355 | -17.16922 | -57.39545 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 33dfc0c5-b682-3448-84df-246678d3ad71 | -17.16872 | -57.40059 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 3669b9ac-2475-3be9-8db3-f128e79ed28c | -17.16542 | -57.36909 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6458e3c0-a677-3e91-a802-9b73171ae8c1 | -17.16493 | -57.37423 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c97a5e65-7213-338e-a23f-9cadeafacfd6 | -17.16443 | -57.37936 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3b9a5fea-cc43-3d6f-810b-3d44de012f1a | -17.16296 | -57.39475 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6a2701c3-20ef-32bf-947a-46ef70d07cc0 | -17.16246 | -57.39988 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 227ed7f5-d093-3968-8775-052e8c97119f | -17.16197 | -57.40501 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 7e444a30-54dd-3783-b239-3aac614b1343 | -17.15965 | -57.3632 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 3fdfe48d-3afa-3529-99ee-7a7ed2392946 | -17.15915 | -57.36833 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d1b428c7-11a0-3464-a387-6ed8fabd44e9 | -17.15866 | -57.37347 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 957fba16-4c58-37ca-967d-72d0eab0bd61 | -17.15817 | -57.37862 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a079ef3c-6a26-3786-9280-d9e6f37406dd | -17.15768 | -57.38375 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9543d012-5ee2-3bfc-b9a6-459876c1fed6 | -17.1567 | -57.394 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 43128c27-1123-3d3b-83fd-4eabd305dd54 | -17.15621 | -57.39911 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| c79bdc5f-7ec6-3a8e-88cc-e924405f2611 | -17.15289 | -57.36757 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5233d2ff-f2fd-3774-9d77-183e698401fe | -17.15191 | -57.37785 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5acdfc40-1e64-356e-8fbc-60001d0c4e8d | -17.15044 | -57.39325 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1182a016-bd29-3170-8f86-8a87685a4b14 | -17.14995 | -57.39838 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 380b26c6-f1a9-3f8e-804a-7df321f9618c | -17.14618 | -57.39497 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| cdc8abd8-7f8c-3e23-9277-1c22f589a6f3 | -17.14566 | -57.40006 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 6671ddf0-a0fa-3662-87f4-d6869089e6ab | -17.14514 | -57.40516 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 16471a66-401c-37f8-9848-5b44b48445a4 | -17.14418 | -57.3925 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 58309b7e-32ec-3099-a9e1-4f39596c29ae | -17.1437 | -57.39763 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| f5f64a96-6d5a-3556-848e-519ce5320d82 | -17.14322 | -57.40272 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 744ca1c4-c74f-35fb-8363-802961413b13 | -17.14044 | -57.38911 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1ad3323a-3656-32a9-9b51-f0a92b3daeaf | -17.13992 | -57.39426 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c8359cc7-3c74-3141-8c0e-6bfc3341cfc9 | -17.1394 | -57.39936 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| ca1855d0-64b0-3349-86d7-a94b91f6ba6f | -17.13889 | -57.40445 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| fc4d0365-78c8-3880-85d6-39274465f7f2 | -17.13793 | -57.39176 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8bf8ae67-6fd3-3568-bcbf-277563dc0820 | -17.13744 | -57.39691 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| b3c325f4-e5f6-3db2-a158-976eb760195b | -17.13696 | -57.402 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 5e4ac782-c30d-30a2-8df6-304ae3dd411d | -17.03708 | -56.70792 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f8038bf5-c1c2-3efa-8755-1b45d0ef10c2 | -17.02088 | -56.74033 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2015431e-705d-3722-b962-036a2fbab392 | -17.02035 | -56.74597 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7d83180b-2344-3831-95cf-e10ad95c85f5 | -17.01438 | -56.73959 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 0cc7fcca-2c15-3fee-b5e1-3489f3212372 | -17.01385 | -56.74523 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 75037767-c552-3db2-8971-89b8dee1ac2b | -17.00735 | -56.74446 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 88441a4c-6f20-365d-90a3-77a3fc738522 | -17.00683 | -56.75008 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| f70976d3-4b85-3bb8-bd1c-664238c04bd1 | -17.00086 | -56.74368 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 9abb6c6e-d5ac-35cd-a709-d317022d39a8 | -17.00071 | -56.74447 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e1026dcd-45e4-3c1b-83f8-2f21e338ab63 | -17.00034 | -56.74932 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a7f0ab56-8254-3662-a9a6-0cbd279bf0ea | -17.00015 | -56.7501 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| cee2c0d9-7d45-3aa0-be5a-5ad414d54701 | -16.99981 | -56.75496 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ea4ba703-b3d6-394a-8506-b02e391ad39b | -16.99959 | -56.75572 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 04c5c956-8e30-304b-be60-349b7dac11b1 | -16.99332 | -56.7542 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ba160a29-9f5e-3951-98f5-89d215bc4d96 | -16.9931 | -56.755 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e19f28a6-e81b-33c8-9090-512b5e7e4fa5 | -16.7918 | -57.82643 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3028da55-6486-32c5-9862-ce9c89ae493a | -16.79133 | -57.83117 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 07fd408d-b97c-3d3b-abf9-a06fff3bfd82 | -16.78526 | -57.83044 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 84d6faa3-bbf3-35c7-b1de-4495851de131 | -16.75571 | -57.75453 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7dd037ad-4c0c-3486-9d3c-2b2362956989 | -16.75525 | -57.75932 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a627a47c-75e7-317d-9d21-c7bc0066c17a | -17.11557 | -56.78425 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 41e384d7-12c6-3ff9-88e9-632edb8dff93 | -17.11505 | -56.78987 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 617446cb-e2e0-3656-954e-e8d39ffed026 | -17.11013 | -56.77225 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 88cc7f7e-badb-33d4-acbc-c0310b3d5cb6 | -17.10961 | -56.77789 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7bd07c49-47d4-3faa-b696-caf1c9497ee8 | -17.10908 | -56.78351 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b6cf34c6-591e-3a17-be35-d4f51c4d4e1e | -17.10856 | -56.78913 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3bd0b2ea-6cd4-3f69-bfd6-3a773ca87cf1 | -17.10803 | -56.79479 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 59d9dbb2-ef4b-347b-b078-d4bbf06bdedd | -17.10259 | -56.78278 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c425a771-e965-344d-8646-2a7f8cad9127 | -17.10207 | -56.78839 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ba67edf6-3c9d-3b1f-84b9-48838be8e317 | -17.10201 | -56.78374 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b2860af6-6c64-375b-b849-21e25553f175 | -17.10146 | -56.78936 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a069efb7-2c0b-302a-ad65-566b3f5ee9f2 | -17.09559 | -56.78765 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 408adf30-f1eb-3f2f-a42d-d67773743291 | -17.09497 | -56.78863 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fa3b5253-2ee2-3098-9304-3571996977a6 | -17.08962 | -56.78127 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0743f2f6-d9f8-3237-bfad-bf93cb8f3ebe | -17.08904 | -56.78228 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e9ea3e0f-caad-316f-b02f-8ae7a11e028e | -17.07664 | -56.77973 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1ff6e60e-2080-318f-8be1-989c870c385d | -17.07613 | -56.78535 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8530a4be-55e8-30b1-afab-16e53eb1f585 | -17.06147 | -56.79613 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7758789a-0e5f-3e93-a2f8-157d127e13da | -17.05499 | -56.79543 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5baaad4c-fd84-3912-aeaf-364d774f3ef1 | -17.04851 | -56.79469 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 643b00ef-618b-3493-b9d4-896b666489a2 | -17.04257 | -56.78833 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f68c7459-067e-3a6f-bf7b-61414fde967f | -17.03662 | -56.78198 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 490205f0-da9d-344e-b82b-9c5f90ad21ef | -17.03609 | -56.78758 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 996fa971-92bb-3965-bd69-01504fb93933 | -17.03014 | -56.7812 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5d7a997b-68d9-3f6c-a006-364811f92e31 | -17.02365 | -56.78046 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 225432e9-7bd9-3196-956d-ff7b5a1c8de7 | -17.02312 | -56.78608 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 57a71dae-98fc-3d6e-835f-9d618e1041e5 | -17.01717 | -56.7797 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2c41b02b-9811-374b-a363-4f49c6acdb0b | -17.01664 | -56.78533 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| af308694-3966-3e3b-a5cc-6dd87f9a30a2 | -17.01122 | -56.77334 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5eb7b72f-2ca2-3413-aa5d-55bf9a7316cc | -17.01069 | -56.77895 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 25cbf277-ebd0-3503-81b7-84e98e1df774 | -17.01016 | -56.78458 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| a8e4efcb-0e6a-3c39-a78f-10e18c611d4c | -17.00526 | -56.76696 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 6ad50de7-45ce-3b83-891e-a0107fda3ab3 | -17.00473 | -56.77258 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 25dcd775-4a5d-307c-8f7a-ea8499bcb5f7 | -17.00421 | -56.7782 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ab1b055e-78a9-3ea3-8bc5-d73354c10bc7 | -16.99877 | -56.76623 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| b304d5cb-bf94-3cb6-96e5-e4efbd198d5e | -16.99847 | -56.76697 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b364431e-ab09-34a6-96d2-5b04ef82987e | -16.99825 | -56.77185 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 71d60509-08fd-34c0-b579-13da171b6dae | -16.99791 | -56.77258 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 14ec3262-5f37-3f26-aa48-e74fc1c2d937 | -16.99772 | -56.77746 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 1cd7afd5-096b-3e4a-b81f-af001457a17d | -16.99735 | -56.77818 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 2d3f9475-9e85-36e4-a769-5fd78ee81712 | -16.99228 | -56.76547 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 28c7e102-9f5e-3e1f-b9ee-f732bbc06746 | -16.99198 | -56.76625 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |


[Clique aqui para ver as próximas entradas](README180.md)
