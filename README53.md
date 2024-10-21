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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ad02109-1379-3b08-bc7a-9d65fb586cc0 | -2.36068 | -52.51892 | 2024-10-21 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| deb0f312-6c37-3aa0-8b2a-e2b564b0262c | -3.11136 | -53.11518 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 836b6e02-3082-319f-a4da-93f2607de4f8 | -3.11092 | -53.11812 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15459d0b-5c55-346d-bbba-ca187db9c77d | -3.1096 | -53.12706 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f2dbbc8-ead1-31a6-a714-407cb6c53763 | -3.10915 | -53.13007 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6058824-d011-3e5d-aac6-47afbfce9fc0 | -3.10635 | -53.11434 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3bc16eb-6f90-3126-9076-1d7a67884dc9 | -3.10591 | -53.11731 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a1ec67e-5192-34c6-a7af-de921768cc35 | -3.06773 | -53.23751 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff5ad2a8-b02e-34aa-b38d-9556830ad813 | -3.0673 | -53.24046 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7097f619-330b-3a40-bf7e-6ee2a741bd7f | -3.06687 | -53.24339 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91f4b561-ce46-3580-ba6a-75c3dc88afe5 | -3.06277 | -53.23665 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cca2330c-6101-3fb6-b13b-b67a30b5da69 | -3.06234 | -53.23959 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 773fc645-562a-340a-91c7-beb5845f3a44 | -3.06191 | -53.24255 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e6de2e6-d42f-3ac8-b463-f212fab3249b | -3.06165 | -53.27894 | 2024-10-21 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a7979ee6-e2d3-327a-9aa0-d781b81796a4 | -3.03314 | -53.86909 | 2024-10-21 05:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7cc1660-505f-31df-bb57-b7e47fdc41d2 | -3.0206 | -54.35294 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1c4fa18-59c3-33e7-a789-62f9cc7f943c | -3.01669 | -54.34762 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 145a7ab9-f5df-3722-9d4f-95ffe8553403 | -3.016 | -54.35221 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 342e08d1-d9eb-381e-a44b-b21791f81545 | -2.95569 | -54.15903 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4599eda9-af7d-36c2-9e6d-b87539737d33 | -2.95102 | -54.15837 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab2fb827-d4c5-3daa-ab73-a93342b1fa20 | -2.88771 | -54.48817 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee90c418-d6da-385a-86ea-c7ab8cca0e09 | -2.87036 | -54.10443 | 2024-10-21 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb82168c-ee2f-3b28-aba0-4731f8b82287 | -2.84049 | -53.98311 | 2024-10-21 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 43bab511-61d9-352c-a42e-47ef5c2adb46 | -2.75372 | -54.03471 | 2024-10-21 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8074ee1c-0f06-3727-91d6-2601fc648cfb | -2.71953 | -54.76996 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dd52023-c579-336c-bc58-edbd64b9d359 | -2.71824 | -54.77867 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79c4ebf4-d7b3-3353-997b-b98f1f8f6c14 | -2.27548 | -53.75637 | 2024-10-21 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e1932a7-852b-3d85-bb88-a552865896d5 | -2.27073 | -53.75564 | 2024-10-21 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4e6cabea-4a8e-3351-947b-0d84f318cb37 | -2.27062 | -53.72435 | 2024-10-21 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22e9131a-4a03-36e6-85f5-905b097411ec | -3.08875 | -54.15158 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25a1c9fe-ec4b-3a27-ab01-df677dac15f5 | -3.08497 | -54.17661 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e5c8e874-c49c-35f0-9869-7f689b36a147 | -3.08422 | -54.18156 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c787d484-d268-34a9-919b-f3b008dce727 | -3.08348 | -54.18645 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab393cd9-29da-31d1-aed7-ce2bfd960f55 | -3.08106 | -54.17086 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 62e98989-f51b-3857-9d5a-6d935d8dde68 | -3.07956 | -54.18083 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6d0404cf-e4fe-3a2d-9f86-b8a9bcbe17ec | -3.0266 | -54.34429 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e58a1c36-2c08-337c-a30d-300444e47bae | -3.0259 | -54.34896 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28e74006-5332-3b13-96d0-8d5caf3c9a9f | -3.02198 | -54.34368 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54076d9d-7c17-3048-a8a7-0693932ef84a | -3.02129 | -54.34831 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbf15c6f-c977-315c-9334-e3488625115b | -3.01991 | -54.35762 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f6b43ef-1522-333f-adeb-f03f20819f5a | -2.887 | -54.49293 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3167637c-49a3-3a82-90fe-6988693f1912 | -2.84455 | -54.0853 | 2024-10-21 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d38dfed-a98d-3d84-805f-58540ee87348 | -2.71889 | -54.77431 | 2024-10-21 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f7e2d7c-62ab-3be1-abb0-293d011c3ae7 | -2.26599 | -53.75492 | 2024-10-21 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| de2a54e6-7d11-3f10-9b05-09004d7519d0 | -2.22149 | -54.81784 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e516df7-ea0a-3b77-aae1-e904ed1be399 | -2.22083 | -54.82214 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26c78091-2332-3c7f-b262-2f92183aa36e | -3.088 | -54.15652 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 0cb6c0a2-35ce-3d7a-a82f-ca68d2f71a25 | -3.08725 | -54.16153 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| cedd36d7-343d-3869-9338-b43d696b391f | -3.08648 | -54.16657 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| db579f08-a3e4-3194-8e9d-6624c56c96e5 | -3.08572 | -54.17162 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| a58b2b1e-1b43-3479-9eda-c2ab81e86b3f | -3.08258 | -54.16082 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1434d80-f813-370e-9724-fef3ff085f64 | -3.08182 | -54.16582 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 346651ec-561f-31ab-9ff1-3f5952599712 | -3.08031 | -54.17586 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 310623ed-b69e-39c4-9afe-ab359bb58e1b | -2.18425 | -55.03223 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 02cfc203-0182-3d6c-a13c-d80ae75cffd6 | -2.55488 | -55.90382 | 2024-10-21 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e82622cd-f3a3-3d51-b266-521f4afeae72 | -2.40214 | -57.14737 | 2024-10-21 05:27:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 828b5236-fe3c-3a82-a69c-de82bd1f9eef | 4.15977 | -59.84539 | 2024-10-21 05:27:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90e93b53-fb57-33e1-adb4-24d1b87fa001 | 2.3588 | -60.90723 | 2024-10-21 05:27:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5d4c28c-a80e-3c3b-81fe-083af6feb67c | -4.87447 | -48.20867 | 2024-10-21 05:29:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 442d3957-233c-377c-a7d0-20345169c18d | -4.87361 | -48.21494 | 2024-10-21 05:29:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d22ee921-3838-3de1-b9af-faf0ecc99593 | -4.66816 | -50.63587 | 2024-10-21 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e1bb93d-07d0-35fa-b240-96d9ada97833 | -4.61197 | -50.6706 | 2024-10-21 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffad17bc-6ba4-3943-9256-0331bceaa90c | -4.42231 | -49.79834 | 2024-10-21 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecad98f2-743b-34cf-8e95-dc341010eeea | -4.42159 | -49.80353 | 2024-10-21 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9aa564a-8dd5-36d7-b439-4ad74a43bbe3 | -4.41973 | -49.80056 | 2024-10-21 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76b96274-67f7-36da-9885-ca1d0a1a063d | -6.49053 | -49.81106 | 2024-10-21 05:29:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 282e9ade-8653-379b-9785-3b754aaa1bcd | -6.48985 | -49.81612 | 2024-10-21 05:29:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f029c19a-2247-3a65-a4aa-37329cdb1346 | -5.59318 | -50.16116 | 2024-10-21 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d33848a2-7324-300d-a6f7-98c044786030 | -5.50359 | -50.57961 | 2024-10-21 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 923d5a75-71b8-3a4f-a68a-6decd88624b1 | -5.50293 | -50.58439 | 2024-10-21 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ebd9b7d-a4fe-3ff6-9998-52d043dac4dd | -5.49746 | -50.57856 | 2024-10-21 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69c13238-0b9a-3fa1-a0e2-c934c0d268f1 | -5.49681 | -50.58333 | 2024-10-21 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d0cdd73-804b-3ed3-9d07-6164197515ac | -5.49615 | -50.5881 | 2024-10-21 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bc82b76-7fda-3c15-8f05-48075abd604d | -5.49001 | -50.58718 | 2024-10-21 05:29:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d832bf4d-e731-3c24-aa12-09c260fe2e53 | -5.16537 | -50.71439 | 2024-10-21 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fba8f608-3ead-3a04-b048-cd5a5ca65d62 | -5.16479 | -50.71858 | 2024-10-21 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec7b72e7-cb5d-36df-ac10-4535fa9fea96 | -3.54619 | -51.38164 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95a2c7a6-965d-307a-94a2-9edd0a99b70d | -3.5456 | -51.38575 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c38eca4a-8ab8-3bf4-b2f7-ef25f655e92f | -3.54353 | -51.38352 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| edd26a5d-a14e-353f-8205-264168a2f5d3 | -3.54292 | -51.38756 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fac22a91-31da-3a96-8ae6-20b43e93bd8c | -3.48212 | -51.60096 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e6e8d35-3bfc-394a-b349-53c163396cc1 | -4.66321 | -50.95121 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9303f087-6c7c-3db7-abe5-a823b87b6bb8 | -4.65978 | -50.94973 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec81014-a7d9-3658-94a9-a30e2f87b306 | -4.56956 | -50.95983 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bfb6961-f15f-36e6-a6e4-8668db64b6bf | -4.56778 | -50.95768 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e8ea305-9f6b-3df3-b8dd-a41ff1b6cae6 | -4.56717 | -50.96208 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2c1d8cd-98fb-32d1-920f-f4fc887322fb | -4.25542 | -50.98763 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 829aff21-98b6-32ca-af5e-b20d9fdb240f | -4.25482 | -50.99182 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2dd3b1b-6514-37a9-9243-1c99429d1eae | -4.25424 | -50.99596 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7ce80b3-799e-38ee-8020-eee29944fffb | -4.24948 | -50.98706 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df6345e2-bcff-392b-a580-d260d920aa37 | -4.2489 | -50.99123 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce19d7cb-17f7-3fcb-aa1f-8a3183e28162 | -4.24832 | -50.99533 | 2024-10-21 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85bfbac0-225a-3e72-857f-fa77c1e50162 | -4.04846 | -51.02514 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 959ee211-0ec6-38a6-af8f-0401f7fdf556 | -4.02783 | -51.00906 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e38d64c7-2eff-3833-af0e-141ed7dab975 | -4.02725 | -51.00592 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61b120ca-3781-39b5-8894-e77e83957f8f | -4.02666 | -51.01007 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4588c93-0359-383b-8c33-2c4b2308b903 | -4.0221 | -51.00732 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91c074d3-1dd6-380c-a636-e68cec5b0a86 | -4.02147 | -51.01154 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04daddfe-a74d-3695-b114-30b8dc84b463 | -4.02091 | -51.00836 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab3ecc44-74e0-319a-be2f-d76b071f15db | -4.02031 | -51.01263 | 2024-10-21 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README54.md)
