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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 681ffdd9-678f-3f5c-ba78-584f66b1cf70 | 2.68554 | -60.41469 | 2025-10-29 05:31:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d742c2c0-4d04-3cb8-ac6a-6e38353b7d96 | 3.14136 | -60.69263 | 2025-10-29 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c8d22d1-ec0a-3466-a037-40fdec7eedd7 | 4.22455 | -61.00146 | 2025-10-29 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61140cf8-d388-38c5-8155-b42315f63cc9 | 1.60453 | -55.69592 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac661d58-271e-3557-958d-61a41116b548 | 1.63211 | -55.67447 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e03fc609-6fd7-3da2-8699-9790510bc969 | -0.64742 | -58.05381 | 2025-10-29 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 730707e5-fa02-3be8-80e5-8bd77d169b17 | -3.32669 | -54.0872 | 2025-10-29 05:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6e5aeee-2a3c-3cf8-a41c-4db2dfc2b9d6 | -3.57871 | -58.55435 | 2025-10-29 05:33:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8006c5e-1e21-3aaa-b749-946320c74ce9 | -3.20325 | -51.00363 | 2025-10-29 05:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4bc14618-bb7d-3052-86d4-cb0a4127d883 | -2.42768 | -49.30574 | 2025-10-29 05:33:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ff108f27-127f-3c94-99d4-7b705081953e | -1.19872 | -54.21465 | 2025-10-29 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bd82e6f-86bd-3c0c-93c8-fc151fe48c19 | -3.57944 | -58.54955 | 2025-10-29 05:33:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc6b6038-2f23-39eb-80ac-6b4617e0d31b | -2.42868 | -49.29913 | 2025-10-29 05:33:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be116935-537a-3f9c-92a0-8dd971f45685 | -4.32117 | -55.61577 | 2025-10-29 05:33:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85f64b2a-9944-3697-a655-ef555152c11a | -4.21601 | -50.06662 | 2025-10-29 05:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6a12d6a-8491-30cf-ad2d-89690981997b | -3.59141 | -58.60072 | 2025-10-29 05:33:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb4c0732-2a1c-377d-add4-5fab8dc2e7e8 | -3.32218 | -54.08646 | 2025-10-29 05:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fc93edf-8e53-3476-b183-9d2980d71a41 | -4.20917 | -50.06568 | 2025-10-29 05:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96508c50-53b8-31af-aee3-4490bdf4ebf3 | -2.94083 | -55.78801 | 2025-10-29 05:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31cbff3c-0059-3a45-be80-d83df92c1480 | -2.42171 | -49.29806 | 2025-10-29 05:33:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2ddb75b0-e832-3792-964d-fce2ca6974fc | -3.03833 | -49.51944 | 2025-10-29 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2987fca8-af8f-3e4b-a6a8-1c10b9aa4ced | -2.42072 | -49.30463 | 2025-10-29 05:33:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f32261fa-2da4-3447-b030-1d40794c3bd3 | -3.04494 | -50.26172 | 2025-10-29 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da300b70-1d40-3348-aea6-205679b397f8 | 0.44745 | -60.48571 | 2025-10-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1db6a227-52c0-31ea-9106-93bd4c22758b | -2.41895 | -57.6751 | 2025-10-29 05:33:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72af2c3a-ddd8-31b2-a13c-2eac899ccc01 | -3.90184 | -55.7973 | 2025-10-29 05:33:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f552ebaf-3d88-3f2c-979c-df5bae6dbc2a | -2.43411 | -49.30442 | 2025-10-29 05:33:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d119e356-d3e0-3873-896a-4552c91e51ac | -3.04411 | -50.26752 | 2025-10-29 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5af29f3b-2564-3cf2-8080-5b1a7a2995bf | -2.42619 | -49.3099 | 2025-10-29 05:33:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 80764b74-ab39-3b62-a3a5-38b26c78b5c1 | 1.2991 | -60.42752 | 2025-10-29 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1a840fa-e9d4-3624-b133-025c4102464a | -2.42714 | -49.30333 | 2025-10-29 05:33:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1e04cb3e-8e52-3838-93de-fdd00e4cfdb9 | -1.19828 | -54.21753 | 2025-10-29 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aa0706c-41f8-3b79-9094-5ea47cba7c84 | -3.35452 | -52.80455 | 2025-10-29 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3577789-ed8d-3ce7-8082-d2d789ee5aec | -3.68935 | -60.5612 | 2025-10-29 05:33:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dd624ff-275e-3507-a548-a2b4c71ab943 | -3.58331 | -58.55013 | 2025-10-29 05:33:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5622459e-3fac-35ec-be2e-14ada8b02c80 | -3.90651 | -55.79808 | 2025-10-29 05:33:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c1664cc-a392-3e97-b8ba-15ecc46af842 | 0.45082 | -60.48519 | 2025-10-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60514f72-ab49-36b6-8c0e-970366ca82dd | 0.63417 | -60.28675 | 2025-10-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6a8515e-669b-3765-9b21-ccad14c8645c | -0.42085 | -52.04935 | 2025-10-29 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e0bbd31-0c3b-39eb-a9e7-2aa3ea49e3bd | -3.32787 | -54.08392 | 2025-10-29 05:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce62cf89-8159-34bd-9570-c65f6f5db269 | -2.42298 | -57.6757 | 2025-10-29 05:33:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ff7d067-10e7-3481-9cb2-1d75451f3328 | -2.94544 | -55.7887 | 2025-10-29 05:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2d70ce8-ac33-30ae-aa94-b6eae838b0b1 | -1.49929 | -53.12865 | 2025-10-29 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a277a931-972e-3266-b3f6-28cbdbd920dd | -0.43415 | -52.03897 | 2025-10-29 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 644dcc61-0483-3056-a926-0cc40f440d87 | 0.45419 | -60.48466 | 2025-10-29 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08a7cb66-a290-339c-911d-ba5bd65c4b14 | -3.32744 | -54.08691 | 2025-10-29 05:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8ebbd11-e30a-3a38-be18-55e5b73a4530 | -0.42722 | -52.03606 | 2025-10-29 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db057eba-074e-32ef-b9a4-519d733f4715 | -3.68994 | -60.55735 | 2025-10-29 05:33:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52497828-2549-3b5d-b9e9-4e63f542fb10 | -1.5064 | -53.15444 | 2025-10-29 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfaee2b3-2f8f-34e2-a3bf-f8e9e450f18d | -2.42018 | -49.30219 | 2025-10-29 05:33:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a9d919f0-0222-38b1-ab5b-426cdb29d998 | -3.32715 | -54.0842 | 2025-10-29 05:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91bc099b-d102-3163-b24d-5853ea27dba5 | -3.77112 | -51.71107 | 2025-10-29 05:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6947aa5d-0b27-3398-a767-02010ed0990e | 1.30246 | -60.427 | 2025-10-29 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d4ff2b7-3a0a-3398-9a67-421fc8c49f6d | -0.42269 | -52.03724 | 2025-10-29 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f6ecf01-3feb-3e96-b60b-1db15a8dd378 | -0.42659 | -52.05011 | 2025-10-29 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65865259-b5dc-32a6-9d11-2daa2814133e | -3.11736 | -51.21366 | 2025-10-29 05:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 318bb691-442b-3d99-be67-67e4ee30b638 | -0.42148 | -52.03527 | 2025-10-29 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebcf310e-c71b-31c3-baf5-85fea872991b | -0.42844 | -52.03801 | 2025-10-29 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0c42701-5f40-37d8-9010-1806d84dd70b | -3.20249 | -51.0088 | 2025-10-29 05:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 743f41da-6cf7-30ce-a127-7f027e5834e5 | -3.58756 | -58.60013 | 2025-10-29 05:33:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e583728b-4f7e-3e36-bcf4-8f24e0119c98 | -1.88186 | -55.5232 | 2025-10-29 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33436650-2c0f-3fcb-9f78-f8e77c450068 | -0.42331 | -52.0332 | 2025-10-29 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf07820c-285e-3a5a-b793-2f58bc5589f3 | -9.02002 | -63.5729 | 2025-10-29 05:36:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c84a0b7-1f69-3d1d-a680-f1344db52e85 | -12.43999 | -57.86619 | 2025-10-29 05:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e20c6503-79c4-36f2-8a29-076e180a61c8 | -9.0211 | -63.56591 | 2025-10-29 05:36:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de08af46-c55a-3893-bf99-32b385bc3e5d | -9.02056 | -63.5694 | 2025-10-29 05:36:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e45654e2-6cc4-33e0-91e6-33e9cd332f3f | -9.02387 | -63.56992 | 2025-10-29 05:36:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58669291-de70-3caa-bafa-8731789b682e | -12.35639 | -64.14069 | 2025-10-29 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e0319b1-ebb9-3ac8-a5f5-ad8a2b9f4614 | -12.43112 | -64.14159 | 2025-10-29 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1c2d761-30cd-384d-a7e6-d39adb52682f | -3.1094 | -45.2293 | 2025-10-29 05:40:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ab04f66e-5448-3980-8a4c-412b25d1626b | 2.68277 | -60.41677 | 2025-10-29 06:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e004eda-4792-35e9-9b24-b620b97f21ff | 1.58389 | -55.72086 | 2025-10-29 06:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0b0ee82-e721-3601-a489-680b9f65f342 | 1.59054 | -55.7196 | 2025-10-29 06:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 698b08db-8e38-3543-a98d-b572bf0eeb4a | 3.29804 | -60.68359 | 2025-10-29 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3ae5129-36a7-3486-a242-3956373301fb | 0.45494 | -60.48738 | 2025-10-29 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0c58837-da15-3242-a560-6debf67ba988 | 1.58753 | -55.72612 | 2025-10-29 06:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68e26150-237b-3ca2-8a4b-c75822ab9e53 | 1.60197 | -55.70567 | 2025-10-29 06:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f89667a6-f9f0-3594-931d-06d097cb091e | 2.45545 | -60.91426 | 2025-10-29 06:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c77cbec-9951-3a86-a84b-a05f4d57e2c0 | 0.44995 | -60.48816 | 2025-10-29 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 13bde928-206b-3743-9de0-a4ff29ec99bd | 2.45741 | -60.9174 | 2025-10-29 06:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1148cc0b-8c5f-3789-81ee-5977500fe89a | 0.44939 | -60.48741 | 2025-10-29 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fb3088c-4f85-3a51-8b99-6a20f6b24ee7 | 0.63265 | -60.28543 | 2025-10-29 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c8c6375-bc98-35fa-9fb7-43741aad72b1 | 1.58482 | -55.72649 | 2025-10-29 06:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e21a53f9-1cc2-308a-9bce-1fedcf0ddf65 | 1.58657 | -55.72053 | 2025-10-29 06:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cc5b298-fa13-3fc5-8c3d-b44449084272 | 2.46012 | -60.91341 | 2025-10-29 06:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b90458db-1778-3325-9a02-8297d3839409 | 0.45438 | -60.48663 | 2025-10-29 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 066d0370-3b90-35f6-bcd7-3a874bbc9383 | 1.6077 | -55.69872 | 2025-10-29 06:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b01a25c4-a577-3a56-b899-ff5c0947cd13 | -9.02066 | -63.57274 | 2025-10-29 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c9ce67f-79cc-382a-a137-2d49b0a074a6 | -9.02135 | -63.56785 | 2025-10-29 06:05:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a66807a2-0ebd-3a45-a2f3-7546cbfec775 | -12.378 | -64.01538 | 2025-10-29 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1e70a6d-80bc-3107-914f-9013b96fa9da | -12.43 | -64.1429 | 2025-10-29 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2e7b86e-3394-349c-8f33-0ddfe67c0194 | 0.45417 | -60.47951 | 2025-10-29 06:52:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0046a4da-b0d4-3681-895c-f409b7a0fd7f | -15.1072 | -47.9307 | 2025-10-29 11:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 7821979b-19e9-323a-bd53-2f219cf6f711 | -7.0635 | -44.47739 | 2025-10-29 12:17:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 325805ae-02cb-364e-9cf7-2f53b16e0527 | -7.34426 | -43.91688 | 2025-10-29 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6bd93fce-77be-3f60-a117-70ed0c550ffe | -5.84284 | -44.86777 | 2025-10-29 12:17:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7a043449-2769-3328-b7e8-4b7fdde5316d | -3.66539 | -44.20417 | 2025-10-29 12:17:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1af2df98-84fc-33e2-8108-bd91354c8d06 | -7.34014 | -42.48925 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 186.2 |
| 1345309f-4f6b-3160-a63e-c49e0fc356f1 | -2.82989 | -49.39699 | 2025-10-29 12:17:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b810387c-8daf-362f-8ed5-61acad10e623 | -3.86644 | -43.35373 | 2025-10-29 12:17:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |


[Clique aqui para ver as próximas entradas](README80.md)
