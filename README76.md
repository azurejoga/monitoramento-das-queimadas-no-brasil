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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a94cb0ac-33b2-3796-9cb3-9a8bb09d7609 | -1.35825 | -54.63888 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de8e5376-f8b1-353c-a72d-7c552b4c28a7 | -2.3392 | -53.86739 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6808735b-84b0-315d-9869-db8581e32a3e | -3.07286 | -50.33128 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91681488-ad24-3340-b05a-4a9d69c445c0 | -3.7447 | -52.26507 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f924c5d1-3e9d-3922-8aab-6959303bc7d0 | -2.6342 | -54.22766 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db483d79-5106-3d29-b9de-30e7986668e2 | -4.56508 | -48.61225 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12e048c5-6800-3775-94c8-0bfd565ff3af | -3.29792 | -53.67894 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8b12e80-37f5-37fc-925a-82a5242621cb | -3.98678 | -46.64371 | 2024-12-01 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 827ecd18-4156-3da6-9520-ba62d752d99c | -3.24495 | -53.92733 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 016bb0b2-0b3d-3a9d-8e49-fcbfe170bb6b | -2.92628 | -51.44538 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc3853c7-19ec-3f8f-9861-27f98b3368e6 | -3.26381 | -50.04884 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36b155fc-9efe-3638-ac62-53dc2ce6e6a0 | -1.70659 | -52.77129 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44a720b1-4d3c-3784-8021-f01fb601d4d3 | -1.60686 | -53.82692 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14f4e7bf-dc66-353f-b1b6-64ac1818feac | -2.42164 | -53.93533 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7ed27df-ac22-3cd8-9607-9dd744d02901 | -2.50078 | -52.1041 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 276fd8a3-f6b2-3771-9bac-cc1ad418e35e | -3.82595 | -50.14131 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfe164d8-8f24-3596-a7d4-29c4a005343c | -2.04303 | -54.67214 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ad22455-5505-3eb9-a5df-8a441f4d9182 | -3.16042 | -53.23796 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37c134bb-0612-3eeb-9dc4-7601d847c93f | -2.89689 | -55.22405 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24d9029e-d370-3310-9e36-d6d00895f1d7 | -2.83495 | -54.04744 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c8af0dc6-cd0c-3a93-a93d-bade330527dc | -4.26509 | -50.83989 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dcc9f3c-e093-310a-9f47-7aeb6251869d | -2.89146 | -53.96756 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b0aae06-8f20-30a7-b802-dc9bc9298507 | -2.84244 | -52.54233 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dcc7901-bccf-3727-bd88-0fa44cc23488 | -3.30321 | -53.8315 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aec25dbe-2f90-3f02-bada-d85a5af20585 | -1.62494 | -52.3787 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f030116-ed04-351d-9faa-a49b18bb8dad | -1.61875 | -53.88772 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 42a915a3-6e01-3c5c-a2f6-0d6a0e32e016 | -3.21836 | -54.23678 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11641aa2-5b94-3d1b-851a-e5b050bb4126 | -1.26279 | -54.55351 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f43fd116-b6ca-347b-951a-d2e89ef90c7f | -1.47994 | -55.38286 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2805d268-d715-398b-b28a-66c6ef4840e4 | -3.77274 | -51.68039 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7cff5c5-72a6-31bb-98fa-3b94865192f5 | -1.63685 | -53.86288 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d332b8ac-3ea4-3b64-8662-015fe4909c90 | -3.25838 | -53.62747 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a5d9b7e8-8036-3369-afd8-5a5c4adf0d86 | -1.62703 | -52.36522 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5d2207b-4b85-3b26-b29b-e6ac50ba670e | -1.19731 | -53.87238 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edaabecd-fc48-3703-b767-63d0fa177e52 | -2.59546 | -53.98434 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 144b9bae-1719-3872-9a90-b3c28eab8d37 | -1.36996 | -55.11176 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3e11cb9-1a3d-3046-ade3-eab149aa5497 | -3.05677 | -54.41756 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 654c32bc-7587-3813-95d3-35a988c15362 | -1.44938 | -55.18861 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5687c39-eade-32c6-ad27-1ba7dd5a015e | -4.10522 | -48.88864 | 2024-12-01 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d944b908-5b4b-3807-8893-1a5927ea4f11 | -2.37858 | -53.68106 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d589b0e4-d7f8-3140-a3c0-c0a175cdb966 | -3.23791 | -53.92627 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16984ded-3d0b-3640-9788-d5029eba53ab | -1.72183 | -55.02893 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 289e0e30-718f-3905-9e1b-68f4ceb572a6 | -1.27237 | -54.55867 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1d59ecb-e620-31c1-a832-6c85519229db | -1.49176 | -52.416 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a78f0181-63dc-3379-b1e4-c53e3aeccf1e | -3.81682 | -52.08155 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| fff8ff7c-f600-3c06-9442-ebf554af0473 | -2.80296 | -54.04651 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfaaa683-73e6-3c5d-b391-dfe0bda6f2ea | -3.09623 | -53.2928 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1a523e4-49ad-345f-9f1f-4053b01e10a4 | -3.53592 | -62.77332 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a8712d8-0e6f-3d78-8586-2a6f7e2dd9f8 | -3.29428 | -53.84232 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b910d97a-6040-363e-9e2c-a7171565303e | -2.86452 | -54.00312 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 424d646a-f912-3861-b914-70c869548289 | -2.62862 | -51.74973 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d721375-6718-3c36-9940-b52664dd4272 | -2.80126 | -53.04437 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ca0a164-80c0-3fc6-9815-ed3b60b54d71 | -3.22382 | -54.17889 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33115c68-c5a3-359f-9980-f997587ddcd2 | -2.87738 | -53.98924 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fa30152-7f3b-3965-8aac-ba7716133643 | -2.86769 | -53.32071 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeef45aa-a958-358c-8f42-3311016e2206 | -3.75362 | -51.78106 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f154c0d3-5cae-3c64-b45e-951188b9a930 | -3.30314 | -53.69226 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03583525-c076-33d7-82ea-1b22207df07c | -3.4525 | -54.62152 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cd5540a-21db-352c-acf5-08695ad9b245 | -1.52827 | -52.6684 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c32eab0c-0b74-3787-a6dd-7e5e45f07eb7 | -1.66876 | -53.77319 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a5e6eb83-a550-363d-a89a-f784b5a8a4d2 | -4.56548 | -48.60946 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67ba8f89-7288-3cf0-bb91-3a12c7558432 | -2.76822 | -55.30946 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 057f30e0-7128-3a31-9198-0ac90da7ac91 | -4.50387 | -55.83291 | 2024-12-01 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 792d3fa9-ac21-334c-b37f-57a285176c41 | -4.00248 | -44.76151 | 2024-12-01 05:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4ace3874-0acb-37a4-ba80-0b2565d69bbf | -3.07067 | -50.99148 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ef18f5fa-c510-3737-92b7-c66e6b857499 | -3.32008 | -51.533 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2022a82-b2db-34c8-927e-1883ea6793ca | -2.58108 | -54.21269 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10b305e4-acec-3fb3-bc96-4400e25767f3 | -1.25659 | -54.54888 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b54afaa-b314-3e46-bb7b-a6ddf6a42bc1 | -3.41298 | -50.16848 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6be5425b-f8f3-35b5-8f2a-f3316b01f6d6 | -3.49521 | -53.82988 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f9a2a16-fb98-353d-8adc-7d606debf82e | -3.38441 | -49.86019 | 2024-12-01 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a75da49-4c27-365b-bd58-1911147ce82d | -3.24459 | -53.6461 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8543816f-a5b3-39a3-b19a-39e1ea339d01 | -3.04846 | -52.75904 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f294d25-59d8-3dfb-ba2b-849203455f5b | -4.5559 | -45.72948 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3127ba1-3141-3cda-9033-de9cab1eb184 | -3.05979 | -54.04448 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4068b4ce-a0e7-333e-a4e2-5b320a171dda | -2.89954 | -51.58418 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f261bf8-bfbc-3099-b6fb-28a32ab86c46 | -2.45019 | -54.01323 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43eca1ab-9f0e-386e-90d5-fd54d4c774f4 | -2.80724 | -55.30096 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 506e3625-aa25-3e9c-b92d-131f6934c2e0 | -3.29958 | -53.69172 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72f986ac-a507-3e00-84f3-53d3ad25e954 | -2.69795 | -52.917 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d226f69b-a64a-302b-a1ea-4d0b0fcc9cc1 | -5.58388 | -45.21629 | 2024-12-01 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10228624-9d13-34a0-a268-bafd16d9fb0e | -3.84161 | -52.0236 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12941ebb-09ba-3fab-ba56-df0e5893c0ef | -3.10803 | -53.80605 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d582da81-9c9a-3c83-aa54-d807dbc56d28 | -3.74235 | -53.39518 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9d070f0-55bc-3476-a67f-8fca24bca6a7 | -1.27293 | -54.55506 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e51c7fce-98c1-3e7d-8575-27f162ae0145 | -3.72637 | -54.52866 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 745f7e41-0e80-3fa5-a8e3-2281301f079f | -2.31937 | -53.84882 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24ba39f6-a677-33c3-ad00-6bdf0687e4d7 | -3.02315 | -54.027 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a75b740a-1803-367e-90ed-01d6b01b5d1e | -2.51552 | -51.83275 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ce16fcfc-42a3-3f54-b097-a8040537c6ba | -4.06061 | -54.2452 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee0973b8-bfa5-3c13-b0ac-b98264378314 | -2.59902 | -54.24952 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd97a46f-d131-3360-855c-4780c67b6ab7 | -1.3541 | -55.64295 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86328752-7924-36fb-a454-b3df98c439ea | -3.30259 | -53.83547 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1bbe9fb-dcaa-3b1e-a8b6-88557075afad | -2.90512 | -54.17847 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b950612-a1e7-3fe7-bc6b-94892cdaf836 | -3.32421 | -50.21718 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5ccbb06-cecf-36f6-920f-a68cbd71f994 | -3.26551 | -50.09863 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dac16db9-ba4e-3955-97f4-199ac274fabd | -3.36992 | -51.53698 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62736c61-09e4-395b-97b5-6b8f97f96083 | -3.05828 | -53.66013 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a6158f9-994a-331d-a3bd-da7067ab4892 | -3.70658 | -54.61034 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a29c8add-a7aa-345d-b578-2bfc92bae564 | -2.83874 | -54.09133 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README77.md)
