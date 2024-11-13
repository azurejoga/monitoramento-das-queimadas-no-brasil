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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fea8b940-8fc3-3eb4-99c6-2991e113eb15 | -3.94962 | -48.17969 | 2024-11-13 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a577c5cf-84e8-3da4-92f6-0bf28f27b34d | -3.05761 | -50.32856 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96526ed2-8771-3caa-9d97-1cf7471524f5 | -3.94059 | -48.15251 | 2024-11-13 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc263c64-29e2-3fff-b0db-5073c2ccff83 | -3.08644 | -53.25776 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6289dea-1b18-37d6-99f3-77ffd025449a | -3.88026 | -51.17033 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e090f134-df45-37e8-9f9b-83810d6373ac | -3.04953 | -50.33525 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5d053797-0f45-349d-9db3-01202278d352 | -3.95694 | -46.41365 | 2024-11-13 05:22:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e576fb4a-31d5-3faf-a66c-130780c2082f | -8.16747 | -55.19224 | 2024-11-13 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ff0cdb4-7eb6-3473-afdb-a18393d36095 | -3.16243 | -50.45263 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aa39d6a4-546f-3205-a760-2eb32f4b32e7 | -3.10161 | -53.97989 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4359b94-e96c-3311-b3f3-a088654ec5ea | -2.7115 | -54.68919 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f20e4c10-ccca-3eef-917c-679b3b2a7f43 | -2.98598 | -51.34678 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9067fb86-406d-3d10-8a2c-b39e57f4df4a | -3.40656 | -58.41033 | 2024-11-13 05:22:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acd1f423-b87e-3d55-9a20-eadd90da9f7d | -4.32968 | -50.41935 | 2024-11-13 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2afa1e13-1d15-3f3d-961c-9acf9a6635df | -3.49593 | -50.24884 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b42486a6-c431-3530-8595-5f7c9ea51f5e | -3.13147 | -50.43745 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e487ea19-5807-3601-bfdf-359379392912 | -2.56047 | -53.99744 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e609540-65eb-3529-a302-37ce2adf6d53 | -4.04224 | -48.09547 | 2024-11-13 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f0381dd-66c4-35f9-bc23-606ed82c3078 | -2.93299 | -53.22795 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ebdd64a-d809-3fbd-b5cd-37251594340f | -4.66334 | -47.43167 | 2024-11-13 05:22:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a9f4b916-6ec2-3f3a-8f75-d139b670c4fc | -3.85357 | -49.1141 | 2024-11-13 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6def3471-5d68-36a9-87f5-58440ccbb456 | -3.05607 | -50.33907 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5a7da10-22f0-3c9b-9468-0b1cf20bfb3d | -3.22751 | -54.8607 | 2024-11-13 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 388dfea1-626f-378a-b736-781d7519259a | -4.04148 | -48.1008 | 2024-11-13 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c6cfe76-6e63-3da5-be43-8aec2854f9d7 | -2.87655 | -54.20958 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc0eb003-caa5-3077-aaad-de00f62b5d43 | -3.49495 | -50.84017 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c95b1cd-295a-3851-8f89-0a4366a2e9fa | -3.06849 | -50.33025 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc17161b-c6de-3f77-8bbe-26aa182c40fb | -4.21899 | -46.45416 | 2024-11-13 05:22:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d143a0d0-9cda-37d6-97b6-cf1d446fd753 | -3.04409 | -50.33444 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7a9c077e-dd8e-374d-b0d8-6811d75a77a9 | -3.9527 | -46.41467 | 2024-11-13 05:22:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6af7444a-abd9-364a-ad8b-10f57aa8dfc5 | -3.10103 | -54.3026 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4962d0db-7035-3bd7-a7eb-d7e4b44eb558 | -3.87965 | -51.17336 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b429d9-3124-3414-89d5-7f823678893c | -3.01983 | -51.09054 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd0ebd88-85b2-3f81-b243-205a26a9e8a6 | -3.14836 | -53.24031 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e322df56-7562-3a92-9702-7a8afec5d223 | -3.16733 | -50.45686 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 22f1509e-3be6-38c0-b6ff-b3e20a92f90b | -3.30038 | -51.5936 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23c6448b-d1ca-3384-85dc-3bae14a62fd2 | -3.24989 | -50.31348 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ea7cb1a-ae99-3c2b-a973-0534cf5a32e5 | -3.69972 | -54.61966 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d4ac1bd-dd53-3d8a-9be1-26c48dd03873 | -2.37618 | -55.7618 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e8f1de2-8cfa-32a5-85ae-f26294d1f514 | -2.95025 | -54.21212 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb724ebf-2899-3eae-9271-6644d11b307b | -3.36879 | -54.644 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81bb57ba-67dc-358c-8710-97d7892b46d6 | -3.0457 | -50.33392 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 532f77e0-4168-3d11-b176-431f27e0f6e1 | -3.4973 | -50.83701 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed5ff63f-9160-37ee-93c4-43677f2bb68f | -3.10214 | -54.2952 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbf57a5c-9c06-3222-9a92-c576345ea32d | -4.20287 | -55.15791 | 2024-11-13 05:22:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef165fde-aab0-3367-aab5-5906cf1c7029 | -3.2843 | -53.66578 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01c856be-9ba0-3506-8414-06798b24cfd7 | -7.41926 | -63.04342 | 2024-11-13 05:22:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7d1e493-54ef-3e98-9a0c-355daf9afbba | -3.15385 | -59.15569 | 2024-11-13 05:22:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05a9181d-6e9f-3b1b-b0cc-4ee815bebf4b | -3.02733 | -50.97129 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 179e8ea5-382c-364a-8be9-ab6acfcf05c7 | -3.05008 | -50.3317 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e77e22b9-37c0-33f7-be88-26c909bfe092 | -3.0119 | -54.11716 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a61153e9-1d73-3acd-9321-bba55b14e223 | -3.03545 | -51.09886 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ad3de4b-cb81-3caa-9cda-c35d0c5c6ea5 | -3.0587 | -50.31182 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d0132ea-46bf-3326-bf08-3738327cec9a | -6.82151 | -46.77731 | 2024-11-13 05:22:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a46750b-427c-3d84-8aba-f8d282b27b65 | -2.98136 | -51.34302 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f45781db-4905-33d4-9015-a0dc9debe98e | -3.88011 | -51.1703 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94b6abcb-fae7-33ab-af6e-bb2f61580f9a | -3.86192 | -49.11819 | 2024-11-13 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ad99942a-d1e4-38e7-bc71-9514817d5996 | -4.04276 | -56.11093 | 2024-11-13 05:22:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33d687b1-dbf7-3cca-ac1a-04d3c146c67c | -3.24548 | -50.30564 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d6e7c86-c7fe-3cd1-873f-6e214c3ba549 | -3.95864 | -54.66429 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 780e1f49-d7d5-3585-aec6-57a7ceccf98b | -4.51492 | -48.92899 | 2024-11-13 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ba21a45-1af4-3eac-9034-bbad0448d932 | -3.2952 | -51.59343 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5812216-bf22-31dc-8f94-45911a7f15d6 | -2.98099 | -51.24261 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba245da6-aa30-3ab6-a3f0-173b4d14739c | -3.94996 | -46.41217 | 2024-11-13 05:22:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2570c8d7-284f-3a8b-9be0-b303efa28d69 | -3.14497 | -54.4855 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81f854e9-0580-3ed3-aa28-1a1c403e0325 | -4.89763 | -55.90672 | 2024-11-13 05:22:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39de8116-b96d-3680-838e-dbe0c43bbe07 | -3.10049 | -54.30629 | 2024-11-13 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b15f2e16-6976-3855-95c1-5cfe60de3d90 | -3.05498 | -50.33604 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f778cd7e-bcab-3ed7-947e-32a902785269 | -2.98692 | -51.34064 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dab7e09-c038-37ff-acfa-aa166c5ec182 | -3.98377 | -56.24072 | 2024-11-13 05:22:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99431812-283f-31f0-b732-8ffdc4d1b4b4 | -2.56349 | -54.00573 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f9464e1-e30a-33f0-974b-fc2b0aa39d26 | -4.32629 | -46.54416 | 2024-11-13 05:22:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| feba3476-cf64-3982-a8e1-9d2e4c5c1da6 | -2.68157 | -57.37632 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c028cbb-660c-33e2-ac10-c82fe33a9454 | -3.0457 | -50.32394 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74968ae0-c733-39cb-8922-519f0de64133 | -3.62518 | -51.49423 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f76da634-8023-35a4-a55a-832819ec23f9 | -2.7147 | -57.34641 | 2024-11-13 05:22:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db64d412-b293-3453-9fc3-dbf7a10ae3a4 | -3.41332 | -50.31286 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bed28923-0c7c-3329-83ea-07b29095b362 | -3.48699 | -54.02185 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3876379-7bca-3e32-918f-b57db467ed09 | -3.40785 | -50.31204 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 376d38ac-b5d5-3301-beeb-048241d7e518 | -4.65667 | -47.43048 | 2024-11-13 05:22:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dd5e052f-df91-3633-98f9-4f366bff6228 | -2.62533 | -54.2745 | 2024-11-13 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5d8dee5-df63-3535-ad21-b396232ee571 | -2.99149 | -51.0329 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3ee14201-2581-3e76-a855-49e1265b9305 | -3.43135 | -50.30465 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2b00da2-fb41-341d-9463-40493fa085b0 | -3.15282 | -53.24094 | 2024-11-13 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4b0aac8-671e-3655-9741-30f021f8fbf2 | -4.39729 | -50.69016 | 2024-11-13 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dc49af6-aaa3-3fd7-8536-65e0b5164a48 | -10.72769 | -49.51921 | 2024-11-13 05:22:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95778645-5b48-357f-91e6-db264fc23f2f | -3.57237 | -54.61882 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 959394e8-f66e-3765-b5d3-35bba05d4fbe | -2.98739 | -51.33755 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fd14f84-c50c-37ee-a35b-63a780107b80 | -2.98552 | -51.34975 | 2024-11-13 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab4fb8da-5dc3-3614-b570-7e40fbb91f86 | -3.76186 | -54.65164 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56bf4f7b-65e0-3f19-a551-43ad0571af78 | -5.15242 | -48.18488 | 2024-11-13 05:22:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 565dde6a-a3d3-3871-84e0-e951867402f7 | -4.62357 | -59.90265 | 2024-11-13 05:22:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59025aa0-0463-3e3c-97d6-a24b9acbe2ab | -3.4968 | -50.84033 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08502041-05ce-311e-b2e2-97b7214f931c | -3.41281 | -50.31638 | 2024-11-13 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f27b15f-85b6-373e-b056-9a62dbabf99b | -3.69708 | -54.39691 | 2024-11-13 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f80d316-f719-3683-ba2f-0e3aae083043 | -2.55628 | -53.99679 | 2024-11-13 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dddaf0a-8748-327c-8562-36e5bc41dcb7 | -4.51604 | -48.92577 | 2024-11-13 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8506eb8-5657-34a5-9ded-a035ae08defa | -3.34513 | -48.95147 | 2024-11-13 05:22:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d857869e-53e0-3476-a9d5-ebd714c36885 | -3.05113 | -50.32482 | 2024-11-13 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e8ebc2a6-5bcd-32b6-848c-550a899449b3 | -3.34623 | -54.18785 | 2024-11-13 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
