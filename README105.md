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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a87194b-5d5e-3c03-a2cb-f39477dbe02a | -4.15941 | -55.14151 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9e5329d8-5453-3b7f-b8a9-14d0855d6cd4 | -3.29918 | -54.06961 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdaeeff7-d327-30ca-a1d6-88cce0d23087 | -3.67645 | -59.62464 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cac81a5a-de38-3132-8ed3-25763238a20b | -3.27841 | -50.42404 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19c99beb-f5fa-3d24-a8cc-a866cf8694e9 | -3.55244 | -59.48037 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9f4fc90-d5dd-3108-987f-33dcd661a0af | -3.51345 | -54.66247 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 025e146e-a10d-3c8f-ae2b-f96375fddac4 | -3.052 | -54.22416 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 680248f4-f5d7-3355-aed8-adb3bb363cd5 | -3.05883 | -54.21035 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f8f775e5-1ed5-357d-b496-7f2b3533e8da | -1.80287 | -57.10493 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 20f41a7f-28d9-3ea0-be31-5a0070199c5f | -4.16253 | -55.15084 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 400dacb1-5bd8-3598-b59a-0e1a358ea96d | -3.28089 | -50.41216 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 578b4098-bc46-3c2c-a9b1-151e6c132919 | -3.27082 | -54.06527 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11ba415f-7a4a-3c99-ae20-a2a049cff962 | -3.50225 | -54.64384 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b31aee3-0416-3a1f-bab4-ba0dec7558ab | -3.0686 | -54.17708 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e173a1f-2212-3d5f-a4c7-65be3ab32b3b | -3.6321 | -55.28054 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c580a82-d6ff-3b5d-bf6e-f467c6de23fc | -3.5125 | -54.66906 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 566e37d4-98a9-3a4c-b772-a92e820829d2 | -3.03269 | -53.89426 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 388214e0-4636-34d1-8720-883100ef44bb | -3.05104 | -53.93346 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aaf3792-7af7-34e9-a7fc-232dd44882ca | -3.16844 | -58.63526 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6464f133-1f47-35fa-b76f-87a42a64d95d | -2.95593 | -54.10528 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a4696cc-c55f-3db6-aa8b-425f34b72de9 | -3.48564 | -50.08154 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d556870-ee58-3229-8a79-8542eb1c4d3d | -1.10615 | -54.15979 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79dce4d3-265e-3e36-9cee-ae17968a578d | -2.92326 | -54.13031 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10b62db2-4f40-316f-89a6-22c4d5ac90d9 | -3.05426 | -54.14492 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61ad8cd2-812a-3356-aed1-d31f2e65e195 | -2.94426 | -54.11849 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee0017ad-0909-3c60-94db-6058c9568bd4 | -1.79766 | -57.11345 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1dfcd5a6-f7af-3ad4-ac14-460cb55c0163 | -3.52432 | -54.65213 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfaf7d4b-0d96-32b0-a190-7e7b05fe8399 | -2.92401 | -54.12546 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcec3be4-ac0b-304a-b5cc-6e0403149440 | -3.09945 | -53.74678 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d19ee441-8cad-38e9-a5ed-75f43295d79c | -3.26765 | -50.41353 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 17c4d21e-470b-35ec-95e9-55159df4af8a | -1.79461 | -57.10826 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29101417-8f51-390a-b8f5-43b7e70dada9 | -3.53094 | -54.639 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de349fbd-9931-37da-b8ec-cac4ecf4a33a | -3.96863 | -55.8222 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4600a8b3-58e4-3d10-8b50-5fed09589ea5 | -3.27767 | -50.43446 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e09e2b0-5501-3aa6-86da-f70e64c40602 | -3.11627 | -53.76534 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 341ee18a-d4eb-325a-8cf3-c0a928f338bf | -3.10748 | -54.17302 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f9448f8-c228-3f30-a6c3-5e4edc278347 | -3.28721 | -54.05255 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5237011-6fea-3b3f-aca3-605cc16b89ae | -2.89759 | -58.45845 | 2026-10-07 05:40:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05fddb92-8ccc-3cb4-86c1-b287ffcda2f7 | -3.74296 | -51.2198 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0b23bf6-61ba-3d09-9ead-eafdd8c64d13 | -2.57099 | -50.68049 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d6302a9-be3c-3415-82dd-a8f16b93323c | -3.26879 | -50.41044 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b858f353-c910-38a2-82cc-ff8978d8c3b7 | -3.54134 | -50.0899 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ad962ae3-9cba-3aeb-85d2-9c0512165b30 | 0.68423 | -60.07508 | 2026-10-07 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44fe0949-28a1-3697-8261-bb3e9e59f284 | -2.94896 | -54.11914 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5a00484-3e74-3154-87fc-f340af66fdaf | -2.76292 | -54.09891 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e4bfa5c-97c8-3a12-bb9b-4f0faa047dab | -3.06705 | -54.25077 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14fd4e9d-bb7b-3e4a-8a79-f584fbbce143 | -2.78266 | -51.68282 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b665eb64-72b9-38d5-b62e-30b1566c3890 | -3.77453 | -58.52177 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fe77ed2-e857-31bf-b197-0d1d3e1eabdb | -3.10399 | -53.77657 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18587f31-eaf5-3970-b311-ba0e66f7f14c | -3.05179 | -54.14654 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 810a425d-fccb-3b7e-8699-c33172caf6c7 | -3.1028 | -54.17235 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b3d1343-ed66-33b0-8e54-e838849d81d2 | -3.27908 | -50.4196 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2128559a-41fe-3d3b-87ca-caad1bbcddf2 | -3.29104 | -54.0205 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1690bbb4-30f5-39ed-bd3e-f1f88aa1c148 | -3.28146 | -54.02595 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15d181dd-4ac4-3dbf-a97d-47d70c71d6c6 | -2.77228 | -54.10035 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 9f3aaf94-9a4b-3a02-89a5-ff464af8356c | -3.10507 | -53.77406 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1526a052-5fcc-390f-83da-5d921757ebb9 | -3.56313 | -54.48611 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85b3415f-8581-31a9-a07f-7eec1741e612 | -2.78089 | -54.10664 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85861ed8-0b90-3296-9576-78b037d06c07 | -3.51489 | -54.65326 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 593be34c-1617-396b-8418-fdc62effea2e | -3.53802 | -54.654 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9556f526-f70b-3afc-ab70-2774f7a5f55f | -3.47745 | -59.46924 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 117ac6b1-7851-3dc3-8b05-b401dab513e8 | -3.0724 | -54.24685 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32d45c91-88e1-39f8-b6ef-53063c2b2c05 | -2.87821 | -54.14331 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720cf0b3-cef2-32b6-aded-5251245df7aa | -3.10586 | -53.76899 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a02443d3-ba8d-3470-916f-8d3e003133de | -3.16229 | -50.44532 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f2ceb13-8fd1-3d20-9e8c-ab6e790cd591 | -3.47878 | -50.08517 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a512adf1-78b4-3ab1-9852-9eec122d11ea | -3.13002 | -53.70078 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f8f14ae-4557-3e4b-94fa-c8b50736f583 | -2.93333 | -54.13836 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92cc2dbd-1420-3d88-8d56-d179e70a2748 | -1.32526 | -56.40468 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3702a5f1-d8a5-3153-b92a-c240e15aebec | -3.09515 | -54.28477 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6874224d-54ca-348b-8f88-755f28d99b5d | -3.48493 | -50.0864 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4e640c8-e27c-376d-b315-9dd752bbf6ca | -2.94162 | -54.11468 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2bcbf442-416e-307c-ae93-0d4d7417d234 | -4.11832 | -50.83027 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19c69630-6dfe-3a9f-abed-746bf371af72 | -3.12123 | -53.70204 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b435b52a-bad9-3b72-9402-743fdeb825e0 | -3.14243 | -54.36622 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddc23695-39de-346f-a50d-54a1ff896d1e | -3.26504 | -54.03885 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| cf15ad90-16bf-3ba9-848a-c80b5e88af39 | -3.06465 | -54.17148 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bb4f856-98a5-34dc-a931-b6205b817b7b | -3.86088 | -55.99927 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a27ca5c-8b9b-35d7-802c-a6322e053ac3 | -3.15865 | -50.44193 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99e640a0-55fe-3895-9476-1cbd8b44e885 | -2.49945 | -56.1297 | 2026-10-07 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 545ea776-20b7-322a-b67e-a2bd8880e2e8 | 1.52085 | -56.02095 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5039adb4-18f5-397a-8502-b4926780625b | -4.00084 | -56.25846 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38dd646b-7f02-3f12-8397-66e055748474 | -2.97228 | -54.13391 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41358913-8e92-3e95-9de9-cc38ff22eee8 | -3.50612 | -54.6492 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2dac0ba8-7671-3a30-95e3-b464290adab8 | -3.34386 | -59.47582 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7d07883-a26c-3859-9769-357c17440cda | -3.47029 | -59.58184 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be06b319-99a1-3cc3-97e2-cb19e9440fc5 | -2.8775 | -54.14801 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c517eac9-5d06-37a3-b1e5-a21e4b6033aa | -1.47774 | -54.51262 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 918ac7c5-8bc0-3daa-8135-16296a21fc77 | 3.13753 | -60.5892 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aefdde6-6a96-37e2-b022-fa8620100b57 | -3.62773 | -55.2799 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcbcff0a-416c-37ba-8eaa-a2f496ea1db9 | -3.28501 | -54.06738 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4dfbd322-bffa-3a7e-a7f7-fd2ed6f36f4e | -3.0471 | -54.14586 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b451d70-7e80-349a-873f-3cd26dae83d2 | -3.67954 | -55.94505 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 315611b7-ab25-361a-84b9-e9da3cd9b1c7 | -3.85953 | -55.9797 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f81799d9-3eb3-33f9-b47d-3e33b92094a9 | -3.99673 | -56.25784 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 625c119f-dbe3-313d-814f-71cdff51ec73 | -3.05102 | -54.15142 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa91787b-7f04-3abd-8645-d6f430abdc94 | -3.2782 | -54.01521 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a21f749a-bb88-35ed-8b2f-403296c21606 | -3.77019 | -59.40245 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0480d71a-0359-3c65-b821-edaec32c2ecc | -3.87516 | -55.81709 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 670a112f-b4e2-35c6-829f-e893cc687a21 | -3.19051 | -50.5597 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README106.md)
