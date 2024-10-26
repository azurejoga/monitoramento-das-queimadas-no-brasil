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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8acfe9b2-6948-396b-afad-327921d7bac4 | -17.26797 | -57.29507 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5d6af76e-eaf9-32f6-9991-a7fe804314dc | -17.26717 | -57.29961 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 74eb47ed-2592-332f-ab14-a654a8e05aa9 | -17.26543 | -57.26642 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 1b915e6d-dfc5-36d6-b61e-e19f4fa717db | -17.26336 | -57.25666 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7bc0bb96-36bc-3b8d-acd7-9cf45804775c | -17.26175 | -57.26572 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 1db5fc0a-e3f7-3c28-a19a-93b6a760d104 | -17.23727 | -57.27509 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 07b94840-26ed-300d-8cb8-c707cad71de0 | -17.2323 | -57.2011 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fc18f63f-aec6-3e52-a2fe-7d19a2d7c172 | -17.22785 | -57.2049 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 29bd611e-b144-3175-82e7-1b887761e92a | -17.22629 | -57.21393 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 78e3013c-cf3f-3d2c-a844-e6ac5e406e4d | -17.22419 | -57.2042 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 494ef921-507c-3afd-8ad5-b2d14914b251 | -17.22184 | -57.21774 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4b20345a-ffc6-3095-8b84-f0131a63f084 | -17.22105 | -57.22225 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 86d03abf-b541-352d-91e3-c8d0eb812eb6 | -17.21932 | -57.33281 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f02574ab-cc2d-3032-83df-ac9fda24f35d | -17.21791 | -57.24034 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d43811c0-0300-3dc5-ad33-456893e19090 | -17.21685 | -57.33416 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f33568c1-8119-3d29-a403-d4d90ef10930 | -17.2166 | -57.22606 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| b943575b-4175-36b8-8b81-08ab70048a7a | -17.20741 | -57.25706 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ce5a3aae-8d3b-3db8-8dc4-94253944390d | -17.20135 | -57.26996 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3405798d-2678-346f-b827-d8682598a3ee | -17.19767 | -57.26925 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 042f4d72-6ff2-311d-9f32-c574eea535be | -17.195 | -57.30637 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 46c438a1-9b1e-3f9a-aacc-57c0c8611c92 | -17.19002 | -57.29128 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2c520485-3b29-3ef3-8fbd-47931b4f591a | -17.18633 | -57.29057 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cee664fb-09e3-3bb9-aa1e-686fd2a8e370 | -17.18185 | -57.29442 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7317ff10-0eda-376f-acca-af6b5d55244a | -17.05149 | -57.3948 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| cef2bbe4-7e1a-3707-992e-2209e1c2586b | -16.99451 | -57.33831 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e14c4742-70ed-3b71-b022-efad668e1547 | -16.99341 | -57.36668 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 924a1654-6c54-3de6-9ebe-d1bedb43f834 | -16.99261 | -57.37131 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bcd7b722-f646-3f8d-83fb-aeb19dcff02e | -16.99 | -57.34221 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 90c8ec0b-fe5f-379c-bf4c-b9393e9b5c95 | -16.98649 | -57.38446 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 006b6208-17e9-333c-a2cb-6dbf4a2f5c78 | -16.89406 | -56.75066 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0e726ced-6de8-31ac-9bca-d030dad5e2c1 | -16.89046 | -56.74998 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e55fbb7a-4d0b-3e3c-a5de-d8d578000cd8 | -16.8331 | -56.6879 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7fd0fdbe-c311-3d56-8a4b-b62bc71113a1 | -16.83161 | -56.69651 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 46cb8348-5797-33c1-a6ca-4af98aefe1cb | -16.75654 | -56.73762 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1f61ad3a-c492-3490-a447-1e2b71808ac2 | -16.74609 | -56.66883 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0b24192c-1919-3d60-8573-7db3909c611f | -17.9095 | -57.23811 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 948163f8-7f93-3dec-8ca9-6af0a8e326dc | -17.90665 | -57.23296 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 34665d1c-714b-3e3e-9ac4-e6279bcdb55a | -17.85507 | -57.24844 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e9f883cc-ab62-3349-b1c9-09b1242cb22c | -17.79387 | -57.33863 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 86729529-4590-35f0-bf59-5c0808d0339a | -17.79353 | -57.36191 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3705dd6c-5346-3ae9-8d24-ed2090cbc73a | -17.79307 | -57.34313 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| d51ba62c-d185-3e6c-977a-612f27be388d | -17.79273 | -57.36644 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| ce031847-2ed1-3421-b5dd-10c15a0c1dbd | -17.78986 | -57.36121 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b4b0f916-a270-39a5-aa59-bad191d5da29 | -17.78208 | -57.34101 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d562436b-dfda-3961-89f6-6ec71dcbf731 | -17.77314 | -57.34863 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 43c7d37b-841f-3307-b69e-fdf12ffedf01 | -17.76947 | -57.34792 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 397bad17-dcf0-3d8d-9d22-4d0a36c62917 | -17.76867 | -57.35244 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f756e9d3-89a1-3911-ae3c-6ab2c991b77d | -17.76121 | -57.35793 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 5ae21f52-3bef-32c9-8698-45a602886ff3 | -17.75971 | -57.36006 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| d4bfae9d-aab9-3516-b20e-fc4ab1886185 | -17.75754 | -57.35721 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 9e3520c9-4f8c-339b-b2f7-8693a8e6806f | -17.84122 | -57.54587 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| f61d877d-ffcc-39c8-b4d9-32807e1e8667 | -17.75647 | -57.37816 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 91982789-c34a-3bf7-9d4d-154b8d45c481 | -17.7544 | -57.37535 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7b1771c4-cfd6-3bc8-a6ce-3a6b61efe4d2 | -17.69023 | -57.33018 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6ee95f0e-8f0c-3c19-aad1-b49885dcb376 | -17.84921 | -57.4999 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 62a7f6e4-90d7-394a-b961-81806db1aeaa | -17.84809 | -57.497 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 25a232bf-9c44-30d5-8380-e9c96220bf94 | -17.84727 | -57.50157 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 40aed34c-fbe1-38e7-aaf0-a3e3db922b5a | -17.84552 | -57.49918 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 36785af5-3133-3d8e-bf60-713baf4fae3c | -17.84472 | -57.50377 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e2ef1d13-2994-39b6-b05b-9576dcb0b9df | -17.84358 | -57.50086 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| ff4fe2e3-a0ba-39be-8759-06b1394bb58b | -17.83284 | -57.50621 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e4148a03-1cb9-39cd-893a-429762ec53d7 | -17.82995 | -57.5009 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 1489399b-b20c-3458-b8c1-4ec44ed25d72 | -17.82915 | -57.50549 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| aba815b2-892a-3246-a312-4d929309e2ff | -17.82706 | -57.49559 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| b73b35a6-52b6-32dc-8874-b739d1540bcb | -17.82626 | -57.50017 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| d5e166db-34a2-34d1-8188-9499b70cd23c | -17.82545 | -57.50477 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| bfd83fa4-bf0f-3128-a255-16732c024d11 | -17.82337 | -57.49487 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 14b48d3e-584e-326a-8ea4-62a88347f246 | -17.82257 | -57.49946 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 9bf5d59d-c1f3-39ac-867a-3c1bcb914e36 | -17.82176 | -57.50405 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7f9e2749-3188-36f7-a9d0-1379ab6f8796 | -17.81726 | -57.50793 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7e7cccc5-9ace-3734-b571-611bea32a3a5 | -17.79066 | -57.35668 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 22377cfd-7b91-3f97-9a8f-ad9d8bd86882 | -17.78906 | -57.36573 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 0bfee2b4-d6d9-31c4-b7d1-7f54cfe0288f | -17.78654 | -57.33722 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 9baf112e-146b-3176-a1dd-4cfc16a63fa2 | -17.78288 | -57.33651 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e8eaef7c-6ff5-3c01-ab73-6c3e179710bd | -17.77869 | -57.50993 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 19aa1365-7b0d-350f-bc1a-19005b8369d3 | -17.77841 | -57.34031 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d8e0479a-cc15-3742-bdea-23b2c8ffe418 | -17.77806 | -57.3636 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| f78a4d6b-48dc-329d-bd97-d3b04b478e7c | -17.77761 | -57.34481 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1cfcf9b3-2585-3901-a8db-9ee3a163cecc | -17.77089 | -57.34578 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 15f870cd-21cf-3b7c-bc81-e00c8d63bfd6 | -17.77011 | -57.3503 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 12de011b-1e7f-3ba5-99e8-4dac5d5670c9 | -17.76645 | -57.34959 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7cc4abb5-fb50-3079-a22a-82a6cc477be3 | -17.76581 | -57.34721 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2a03e3b8-ef94-3671-af37-7a23db8794f4 | -17.76566 | -57.35411 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8b0b8559-b204-3142-b360-0a2410c00af8 | -17.76278 | -57.34888 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| c917f490-66b8-364b-a340-206caf1be506 | -17.76267 | -57.49257 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c969085a-1368-3faa-aef2-0453c6c5a1ae | -17.762 | -57.3534 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 0d4a9fde-00d4-37e8-a6d5-1a773261c08b | -17.76052 | -57.35554 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.7 |
| 711e7314-863d-3d2c-9c43-533a4b6ba68d | -17.76043 | -57.36246 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 549aa280-1ef6-3483-94f4-05d636ada655 | -17.76021 | -57.50634 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9b1bb255-15a7-3c51-8aad-509301c34314 | -17.75807 | -57.37606 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 939b9aa1-4269-3ed3-a211-b631a7d343a3 | -17.75676 | -57.36174 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ad5318a7-5006-3998-be19-72e96e4dcc9d | -17.75361 | -57.37989 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3dd61eb7-6e84-3884-9a97-fec8b8a295f3 | -17.75281 | -57.50491 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c1ce2278-486d-31e8-a6c6-dc1252c56035 | -17.74994 | -57.4996 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7ec2196e-ce6e-3242-8d6f-e9253f8f5723 | -17.74912 | -57.50419 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 426d275f-dbdb-3015-850a-ef223b16f6d9 | -17.7405 | -57.36795 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e6e62cf0-6fb8-308c-b35c-d82e869e5621 | -17.73803 | -57.50204 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 05995e65-1174-3484-8a6d-9a7c3b740ad5 | -17.73745 | -57.49485 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dcf0eef4-3986-3eec-91e2-a270032fdcae | -17.73665 | -57.49944 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4becb4d7-29c1-3df6-b033-cfe65a63c44a | -17.73585 | -57.50405 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README87.md)
