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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c566f62-48a9-35ee-8782-f714fa07e27c | -17.71905 | -57.07962 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b004efa3-4bc1-396c-af35-bae1260440bc | -17.71839 | -57.08458 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9a1ccfef-4e30-3fb1-8571-2f5381940c26 | -19.11139 | -57.51758 | 2024-10-07 05:21:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8043459d-b4ce-3c44-b140-16d7069f79f5 | -19.1082 | -57.51234 | 2024-10-07 05:21:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| e491f85a-38e0-3a61-bb5d-3ad0e98fd021 | -19.10522 | -57.47667 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fbd78c3b-24d1-3d9e-bb6f-7bf390d0f078 | -18.88816 | -57.74327 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 627893e9-d3c5-3867-bc82-086b2c2c5246 | -18.8777 | -57.73898 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fd18bfff-966a-3f40-93b4-a9e25b421893 | -18.73144 | -57.29659 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6c9982d3-e1b1-3440-91ac-488528040ed4 | -18.72895 | -57.29267 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 48e7d8ce-10e8-394a-a97f-376fdcac35c2 | -18.7283 | -57.29766 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 764bd807-c761-3158-8e72-bc81ae04fc8a | -18.72827 | -57.29104 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cd2310b8-0e38-3037-858b-2a5a2247fdbd | -18.72758 | -57.29602 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3ee9f488-f4aa-311b-901a-27e788440bd5 | -18.7269 | -57.30101 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0cfb6613-7ec5-3c7a-8d1a-a64990e2bbad | -18.72509 | -57.29211 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5cd9c425-a252-3145-9c06-a177b1e55a03 | -18.72444 | -57.2971 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 855ceed5-48e4-359e-a8a7-ee0869d024b8 | -18.72441 | -57.29048 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| da5be3c2-979a-3691-8332-b32d81cfcba2 | -18.72379 | -57.30208 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 8e6b2b4c-f402-32a8-ae8a-1d75f11183a4 | -18.72373 | -57.29546 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 943d6d56-d2b3-3136-9a7e-89416709ca20 | -18.72305 | -57.30045 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 7e957438-baa0-3402-951c-42ed49b248ca | -18.72237 | -57.30542 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 102ad043-a568-35c5-86c9-23e5d39e9ba2 | -18.72189 | -57.28654 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7d847a3a-dd77-3bc8-82e5-5f71b3505d36 | -18.72124 | -57.29154 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8350e1d6-6c1e-3b37-8a58-24d3458e7634 | -18.72058 | -57.29654 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7f9fe11c-8f5d-3bac-b7f1-3d87b76cc68e | -18.72055 | -57.28992 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| cb013138-d4cf-3e53-8913-1cec9ae99ce0 | -18.71994 | -57.30151 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 3e9e6e3b-5bd5-3cdb-a0ed-854775946c45 | -18.71987 | -57.29491 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| b83fd119-a990-3a1c-83bb-0e2142c56874 | -18.71929 | -57.3065 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| e76c39d2-4cf8-391f-a5e4-554f3bf23eee | -18.71919 | -57.29988 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 0ef084b9-a128-326f-a3cf-a01e2fe52ade | -18.71851 | -57.30486 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 8e4142ac-aa02-3836-ad91-fd61d70f2123 | -18.71803 | -57.28597 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f5b21eb2-a59c-3851-847a-8b728e37616c | -18.71738 | -57.29097 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f7c083b8-beb9-3f15-a05b-465f08ea20e3 | -18.71673 | -57.29596 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7e2e2367-0bfc-3ae8-8fef-36e701ce7907 | -18.71669 | -57.28935 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 32a7e7f4-8bce-35db-84d8-e9fb294afc60 | -18.71608 | -57.30094 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| d96d67bb-4bf8-3bdf-bada-da3d3fa816df | -18.71602 | -57.29433 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a804bfab-3586-3566-844e-e023aec28ffe | -18.71284 | -57.28878 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4c8f8902-f05c-3f61-ac6a-fd68244f3918 | -18.71237 | -57.2632 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8bcede70-b2d4-3c75-ab97-1007c6d009f9 | -18.70851 | -57.26263 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7d8363e2-d487-3f92-8474-daf48a31a64c | -18.70464 | -57.26207 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a1411541-4bc8-3a84-a0cf-f7608552760c | -18.70078 | -57.2615 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 5fdbdcd0-3c5d-3d9b-8ab4-e4a7007fe0d9 | -18.69692 | -57.26093 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a088d687-5ea3-31c0-bd2e-5283760983d1 | -18.69373 | -57.25535 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8603b5d2-3a4c-3471-9fee-3647b8a31eac | -18.69306 | -57.26036 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2022864d-1e0d-37b7-b7de-e15bb8400310 | -18.6776 | -57.25808 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 37314ee5-a2e8-395b-a2ff-2ac4ab75029b | -18.67441 | -57.25251 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f69a9413-04ea-3cc9-9e53-e8f072435bc3 | -18.67374 | -57.25751 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 36ca5eeb-1a22-3caa-9b94-aade7962a687 | -18.67054 | -57.25193 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6cb8a994-b217-3e01-b3a0-bc04a3a58ce0 | -18.66668 | -57.25136 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 90ee7984-f880-3cb9-ac18-2fd739d99a5a | -18.66282 | -57.25079 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a74aab44-8300-3d6f-b42c-856096522f54 | -18.65962 | -57.2452 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c935dfcf-e457-36ae-a0d4-a5648b2915f6 | -18.65895 | -57.25022 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 38737f64-133f-3999-9b92-b2c813d02a9e | -18.65575 | -57.24463 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d7da8f74-8eaa-3c93-9f22-f313c8fa6871 | -18.65509 | -57.24965 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0bce0185-df1b-3be1-8cd3-8e7264b9ed65 | -18.65189 | -57.24406 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| f024edd6-9e9d-3e5e-8004-7a663f0c1f30 | -18.63381 | -57.26181 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9ca5e3b6-ed75-3600-9927-17b0dc2dcb96 | -18.63315 | -57.26681 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5a5c7667-aefe-3b37-acbb-681504ef9e26 | -18.62995 | -57.26123 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| de45af76-63a4-3711-82b3-0c7551823887 | -18.62864 | -57.27124 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9c83882e-0946-3add-88db-4d238bbf2b2c | -18.62743 | -57.26932 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4c567f05-7090-3fe0-a1a8-3e199500943b | -2.21775 | -53.7043 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b968514-552d-38fa-bbe6-6e11513cf387 | -2.21839 | -53.70004 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05853e33-3953-3bf2-893b-9efdb86dd469 | -2.21904 | -53.69574 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2f5907d-5544-3bcd-b72d-57d20dc773b8 | -2.21968 | -53.69153 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1ac9380-12ea-3c05-9a7d-a78e7d45872c | -2.22426 | -53.70106 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff8aefe2-0aeb-36fb-8114-b567cbcbb031 | -2.2171 | -53.70861 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb6e789f-e1f7-3d49-bd68-d12b8ff31c2c | -2.21645 | -53.71289 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f198278-9915-34cb-a4f0-7a40fde80b1c | -2.21443 | -53.6864 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26bfe54a-abad-3eaf-91db-480082309214 | -2.2138 | -53.69056 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 065b22c8-6f05-3479-88e0-f9d3dd8707da | -1.04303 | -53.54012 | 2024-10-07 05:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14dbc376-48a7-3033-a157-8def981b9914 | -1.03719 | -53.53922 | 2024-10-07 05:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc21224b-0235-3779-9774-ba2fa3d6cfa4 | -1.03653 | -53.54351 | 2024-10-07 05:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80cbe4aa-d5fc-3a47-9f5e-ba709e294992 | -1.03046 | -53.73759 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01740355-e162-3d9d-92c1-fe7bfd916054 | -1.0299 | -53.74123 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ca0c59e-b4d9-328f-841a-db20c76da10e | -1.02617 | -53.72716 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5ee2c1a-7a31-3682-be15-203b3468ea09 | -1.02545 | -53.73182 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 97bbf632-8076-3804-913b-90caa36c8766 | -1.02472 | -53.73652 | 2024-10-07 05:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 626e5856-dd2b-3460-8efa-ec6bc9277233 | -6.82157 | -64.32654 | 2024-10-07 05:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eeca420-e788-30ed-a135-f8e0f470f748 | -6.81879 | -64.32249 | 2024-10-07 05:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fb66177-da29-3dbb-94e9-dadd7c709907 | -6.8149 | -64.32551 | 2024-10-07 05:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5968f101-224a-3c74-ad14-694147955920 | -6.81211 | -64.32146 | 2024-10-07 05:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ba4f61f-c569-3cdd-8d6e-11d32c9ed3ad | -8.30111 | -64.07966 | 2024-10-07 05:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 376147ea-3f72-313f-a3f8-459d60c73bcb | -6.93433 | -66.31179 | 2024-10-07 05:40:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a870b14-c180-3b92-b615-771c921cd2a9 | -6.93655 | -66.31937 | 2024-10-07 05:40:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 962fdf76-49ba-39bf-9471-7a5e41d6e076 | -4.90474 | -65.33006 | 2024-10-07 05:40:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1cb01e0-0d28-34dc-9ae3-a992fb8d2e9a | -3.53598 | -65.02586 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28b6ec74-371b-33d0-bcff-f3ea6462c1e8 | -3.53875 | -65.02984 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a8b2da5-67a6-3496-b82f-00b41fd863ef | -3.53929 | -65.02638 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04eed2dc-a8a5-3c97-a392-d174bca13cbd | -3.54206 | -65.03036 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 709bea01-f020-37eb-a233-a5bc1d43bacb | -3.5426 | -65.0269 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49c9b545-f079-3f38-aa5c-6d1db359caca | -3.54315 | -65.02345 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac0a60a6-96e5-3028-a8f2-26f50dd9e88d | -3.54591 | -65.02742 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c607192-dd36-39ed-ac2e-523166d29e40 | -3.54645 | -65.02397 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eb09e8b-106c-35cf-8416-3018eccb59f5 | -3.62871 | -65.01921 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| badcccbd-8dcc-345d-9907-81193847a252 | -3.62925 | -65.01576 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd617b55-5170-30fb-b089-137fbb153f71 | -3.6298 | -65.01231 | 2024-10-07 05:40:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc4f6be-9dc1-3934-aec6-29f9cc27f5f1 | -9.20996 | -59.37479 | 2024-10-07 05:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| debbd30a-1be2-3eaf-962d-4875f2fe020b | -4.28225 | -60.01712 | 2024-10-07 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79fedfe5-2042-3ebe-a991-b858b8ab6502 | -3.96518 | -59.1934 | 2024-10-07 05:40:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de77c50a-0024-3fec-9787-067d75b93499 | -3.96246 | -59.68423 | 2024-10-07 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d881b1d-57d6-345a-8022-4ecf312d198a | -3.89313 | -59.72763 | 2024-10-07 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README131.md)
