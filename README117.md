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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6802d7d0-075e-3d0f-b931-cf3d0b581569 | -17.96705 | -57.39831 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.5 |
| c23f4314-4b9e-3703-8910-5fdd3cf8d979 | -17.96587 | -57.40647 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| c2cf903c-f60f-3047-9c83-dc472e945551 | -17.96236 | -57.40592 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| bf841210-f313-3c95-b210-d55e3dcbc791 | -17.95945 | -57.4013 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e06218dd-f5a9-3290-b9b4-cdd47f6a98f4 | -17.95886 | -57.40537 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| cd99877e-e70d-3d1b-b69c-adab2691bf4b | -17.95827 | -57.40945 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 870ce2fd-7766-3a4d-b079-e43b15071833 | -17.95653 | -57.39667 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 2df38157-5572-320a-b0ea-8e23447b26f8 | -17.95594 | -57.40075 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 45cf3ad8-db2f-3338-b6f3-8fecd20dd249 | -17.95535 | -57.40483 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| d2671571-2e2a-3d9c-95ee-037f7d0ecbe5 | -17.95476 | -57.40891 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 5b050260-8ee8-39f1-8f35-0362e8973f17 | -17.95361 | -57.39204 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 6d4a27d9-9541-3c9c-9a1d-a53a9bf27eab | -17.95302 | -57.39612 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| c4c58321-f11e-3952-9d22-26ad97feb0cd | -17.95245 | -57.37514 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 65c43029-14a0-3040-a215-982f239abcfd | -17.95243 | -57.40021 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 020a69f4-c579-3cd3-906a-28404ad88bf9 | -17.95127 | -57.38331 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| e88cb5f5-b157-31ca-870d-fa2719d28454 | -17.95069 | -57.3874 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 4791cdbc-3fc3-3942-b144-e22f792b9375 | -17.9501 | -57.39148 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| dcbe3523-dbfc-3712-8af3-7693e8405aeb | -17.94951 | -57.39557 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 60d32ea5-dd5a-3a74-96e0-38e102c818d3 | -17.94894 | -57.37459 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 8ea9f0d0-d54c-3f73-a689-6d6731e74718 | -17.94835 | -57.37868 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9013768b-4947-3f7a-abb4-491b5fab05d6 | -17.94777 | -57.38276 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| abf52f99-12af-3004-9aff-8aaf32bcb158 | -17.94718 | -57.38685 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| bd36c19b-a729-3f57-ac09-8a90de2c97af | -17.94543 | -57.37404 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 56775928-e324-3052-b3f8-0a8002b9bd9e | -17.94484 | -57.37813 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b6a8a87e-4de1-3640-a73a-2fd04825c8fa | -17.85694 | -57.2857 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 77899b2d-56d5-3e3d-b6d6-9cb497e1a0d4 | -17.85401 | -57.28104 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 4832dba0-e57c-30b0-be0f-91e709e170f6 | -17.85342 | -57.28515 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| ae8799a9-acde-3ec7-b0c5-689f330dfb11 | -17.8499 | -57.2846 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4e5de207-344c-37d5-be2b-09de66ff384a | -17.8628 | -57.29502 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 3184a1ac-ee76-3ac6-bab4-745ae94c33e9 | -17.86221 | -57.29913 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 75d6bfce-2125-33bb-aa95-91e9a87bd4f7 | -17.86164 | -57.27801 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ca21f66f-22e0-3382-a25f-5a2630b30ed8 | -17.86162 | -57.30324 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 71927368-38fc-36b3-a432-fd8bbae9a461 | -17.86103 | -57.30734 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 622efd3a-8828-31f6-b90b-ecf51f839901 | -17.86046 | -57.28625 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| d2d70bd3-f103-3a70-b941-0279a40ab40f | -17.85928 | -57.29447 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.0 |
| 2c731be9-a931-361b-98db-af99375e2f50 | -17.85869 | -57.29858 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 10c71307-791e-3e01-b9d2-6ce55a7e7f8f | -17.8581 | -57.30268 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 6b89169b-4860-33e4-a020-18e211ef0f8d | -17.85751 | -57.30679 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ed52c8e2-d849-32b2-bb3d-5553031a560f | -17.85576 | -57.29393 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.7 |
| 0464d245-74de-39b7-82ca-5bdd5c087726 | -17.85517 | -57.29803 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 9198f36e-5a0c-3abd-9982-1e0eb25e465f | -17.85458 | -57.30214 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 38321014-e47f-3216-946f-378b507dfaf0 | -17.85399 | -57.30625 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b4a4efb1-766c-3f03-a2b8-7f46ffcb6d0c | -17.85224 | -57.29338 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.7 |
| fd2000f4-b526-3962-9e44-8a74580080c6 | -17.85165 | -57.29749 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1a7e0b0c-5e6a-3d9b-82c7-c11958088b05 | -17.85106 | -57.30159 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 0d6739c6-a95b-382a-bc92-11643909a771 | -17.84872 | -57.29283 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| 6cb52271-186b-39ee-bc34-36505c3953d0 | -17.84813 | -57.29693 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 451129b5-3e01-3c54-a14b-13ba6a259a90 | -17.84754 | -57.30104 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| ee9dceac-a907-39f9-98a8-4bb9e3873cde | -17.84695 | -57.30515 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| df4bcd79-0e0e-3e60-bb1a-ed47ead7f60e | -17.8452 | -57.29228 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| 2f918ac3-be92-3e45-859d-05f3834faa27 | -17.84461 | -57.29639 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| fe308b0d-b40b-3bbe-9a25-5ef9b6f07aeb | -17.84402 | -57.3005 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| e47dccf6-0c51-31da-afbe-86ace6e57f1e | -17.84343 | -57.30461 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 60b0cd99-2397-3f53-ad71-073610986b62 | -17.84168 | -57.29173 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0c9020b3-76ab-31ae-b5bf-d3a169c44928 | -17.84109 | -57.29584 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.9 |
| dbb66522-34ca-3072-863e-9c1a1ff7144e | -17.84051 | -57.29995 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.9 |
| fa0b18fd-4049-3e00-9bf5-d6906278e625 | -17.83992 | -57.30407 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| d84b91f4-e218-393a-8793-ff5c741400d8 | -17.83933 | -57.30817 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 0fa6ed6d-780c-3a41-8561-d875d674483c | -17.83757 | -57.29529 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.9 |
| 9747f4cf-d46c-3625-a7d8-499de413edf9 | -17.83699 | -57.2994 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.9 |
| ec0e7f5a-9402-3367-8b0b-f9e63c3264b0 | -17.8364 | -57.30351 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| fa6fd7aa-d007-36e7-b51a-67e33f45922f | -17.83581 | -57.30762 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| e93c8db0-dd01-34a0-ba60-52b4b5c7ebc4 | -17.83523 | -57.31173 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| cafe1766-8f05-3335-a896-0808d4cb9a43 | -17.83347 | -57.29885 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bb8e7975-60d7-3a3c-930f-687d48c67cc7 | -17.8323 | -57.30707 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.4 |
| cb04015b-d8e7-31a9-935d-b0489521471e | -17.83171 | -57.31118 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| a21a1c7c-0d99-3602-b08f-7717af08497c | -17.82878 | -57.30652 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.4 |
| 66fd18bb-ec78-3acb-a569-5b7f6678bdb3 | -17.82819 | -57.31063 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 292052cf-2a3d-3ffe-9dd6-0733f7cab8eb | -17.82761 | -57.31473 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 31ff2b27-dad1-3db2-aaf7-fdf7b8f82fab | -17.82702 | -57.31883 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 1d1d1ef1-29ec-3df5-9bdd-7a46f595b5b3 | -17.82409 | -57.31419 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| acd5f879-1e09-3b08-bbc5-39dd39f80670 | -17.82351 | -57.31829 | 2024-10-14 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| bc511b94-b0bc-3bf4-8dce-bd3a3d214fc9 | -17.82292 | -57.32238 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| f39fdc05-b0c4-344c-8b41-f83cf7bac989 | -17.75813 | -57.11939 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bfbb7b85-cc1c-3f5f-bcfd-7b4dd4fe2b6f | -17.7475 | -57.11775 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 843e6659-16a3-36d1-9d78-363561ba8cb6 | -17.22048 | -57.3187 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 146312fc-f128-391e-b615-d447a803180b | -17.14787 | -56.87148 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6e4c8b8d-bc02-3eee-87bb-9eb26e5cc4ad | -17.14314 | -56.85358 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5e8ef208-acbb-37ef-88a1-5fc5c09a265c | -17.13778 | -56.86565 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c8c45325-70f4-3d7b-b0fe-78f1429553b5 | -17.13066 | -56.86455 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| cbbceedb-d23e-3e49-ab67-9c00491be35e | -17.12591 | -56.87239 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d81b0350-2b05-3a71-a8cd-24e814401223 | -17.11582 | -56.86655 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0fa05ce7-6765-30f2-b938-88e8205e9ba6 | -16.87035 | -57.29668 | 2024-10-14 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 43c39733-b9e2-3c91-b239-0ddf44307c73 | -17.19076 | -57.42494 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| edb2b597-8294-31ce-8391-65ac38887c61 | -17.18728 | -57.42439 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 591c11b1-2386-3918-a8a0-62bec7cc21f7 | -17.1867 | -57.42839 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4e2647f4-08cd-37f0-8a68-9179b4737d18 | -17.18438 | -57.41985 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 513481f8-2bf1-352a-9f0c-f9cdf3a41f94 | -17.1838 | -57.42385 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 70ce44d3-8779-3d14-8895-db3b75ae8b74 | -17.18322 | -57.42784 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4d2a2415-3d5d-34aa-b80e-1025d1fa2bd9 | -17.1809 | -57.4193 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 07f20ef4-3015-3e08-b3de-09d76f50ba98 | -17.18032 | -57.42331 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 85266f01-ff0b-3078-973f-3d65dceee6b1 | -17.02864 | -57.42916 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 74b781a7-6266-3755-ba29-27d77c7cb695 | -17.02806 | -57.43315 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3373cc1f-f662-3551-9576-735291e659fc | -17.02573 | -57.42464 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4b670a68-6183-3224-951d-1d68f9cf69e2 | -17.01993 | -57.41558 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 33790c0b-9b8f-3ec6-b7ed-c02c8f2a467f | -17.01936 | -57.41956 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c6cfe2ef-21b1-37e6-adce-b9c46f8f6a42 | -17.01879 | -57.42355 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bd67582e-12d0-30c4-9db9-791c0130f2bd | -17.01764 | -57.43151 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 634bf1c4-af47-30ad-8cbe-7a7b87a75ccb | -17.01645 | -57.41504 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| f1f243f3-99e5-348f-a786-a6ebe137e36b | -17.01276 | -57.42807 | 2024-10-14 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |


[Clique aqui para ver as próximas entradas](README118.md)
