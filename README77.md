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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d9b486b-4338-3524-a973-0b2f43e07262 | -9.67893 | -57.22664 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5141625-f352-3fb1-b514-32262c814332 | -9.67736 | -57.2146 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 629c6509-2319-319a-9a9e-521c3b0c9a97 | -9.67673 | -57.21842 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd8c022e-2b5d-3fce-9ae2-27552d413d56 | -9.6761 | -57.22226 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e3d8051-73c1-3f57-909e-2660f0d0368c | -9.6663 | -56.96002 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4203b771-35ec-3b9b-854d-5dfea48e4686 | -9.66569 | -56.96379 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e0e4647-5b9d-36e5-b533-8d0b7b4e46b5 | -9.66288 | -56.95947 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16c75bc1-5b82-3732-9139-66e6337b96ee | -9.66227 | -56.96324 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b68196b-f5b4-3f17-8600-bf424b5aa20f | -9.65664 | -56.95459 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a88bba58-540e-3514-82f2-65ee4c28fbc0 | -9.65603 | -56.95836 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 050ba398-f925-395a-9c7d-0a79c8716133 | -9.65322 | -56.95403 | 2024-10-12 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85c069a1-bb2a-30fe-894d-95ec32ffa012 | -10.63832 | -57.97072 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9b55f71-2ef4-32d2-81a2-32f60d16b493 | -10.56121 | -57.97517 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 911fcfbc-c061-359c-8a0b-82d67ecfa607 | -10.54274 | -57.71743 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a79440e-bf4f-392e-be9a-efbdb66edaa8 | -10.54215 | -57.71395 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df7b66bd-e6b2-3d1b-bd3d-b6abcba0e7a1 | -10.54208 | -57.7214 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d2f6c00-4fc2-3c42-8778-7151e3aec5ad | -10.54151 | -57.71792 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65bbdbd3-19f0-39f4-a6f0-f054eb327b23 | -10.54086 | -57.72189 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9967077c-b73d-3d0e-baa9-41ebc61130b6 | -10.53991 | -57.71288 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c41cde5d-9f70-3514-9f5e-820dd564d51a | -10.53925 | -57.71685 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4699dff-de10-323a-be1d-c84348265f51 | -10.53866 | -57.71336 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d56cf3ab-4010-32ed-9231-4a9b314fcd32 | -10.53801 | -57.71733 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| facc7e2a-b111-3a14-b182-0609c286577b | -10.51301 | -57.78232 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4ac2069-3d00-387e-82a1-be1e01ececbf | -10.51236 | -57.78631 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1248ba55-c9d1-37a3-b1af-7a808a14cf00 | -10.33307 | -57.50675 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f6000a0-6198-3f02-844b-1af24276b1fa | -10.29197 | -57.7141 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ec12ad7-2627-3b65-a908-dc1abe20a901 | -10.27665 | -57.71965 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14ac6d52-be88-3e42-890e-a6723bd29b7d | -10.2738 | -57.71506 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b8eb813-1864-35f7-aae5-f8c606139593 | -10.27314 | -57.71908 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d723d5c-367c-303c-b76f-478276c99a33 | -10.26637 | -57.80388 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3687cfa-e5b1-3f77-b2e5-3015e58b7c4b | -10.26594 | -57.76273 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2ab9d8f-bdbb-3c16-962d-0a99b04dccc6 | -10.23489 | -57.81923 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc55e086-9740-3252-ad64-6c88f96df582 | -10.13173 | -57.76204 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da59359c-c70b-3510-ae0c-cd9874d21223 | -10.13107 | -57.76603 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ca4f286-d51f-3161-b213-014285c00754 | -10.12755 | -57.76545 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2c0242b-7205-3b85-8925-7d41a3894a58 | -10.12688 | -57.76946 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ae2d098c-035c-3da0-b717-70bb46afeb01 | -10.12403 | -57.76488 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1ddb5bc-8fa1-3141-9602-7d474d88b57d | -10.12117 | -57.76031 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6df9c0cb-203f-369d-bf2a-4f52cf0dd068 | -10.12051 | -57.7643 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee11d93f-714b-3644-97e4-ed81dad86887 | -9.52251 | -58.01542 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6012ae87-7342-3ad4-b0a1-98b651b76d3a | -9.4751 | -57.9324 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94f4fbc9-7123-3a9c-8931-d957ba4223d6 | -9.47153 | -57.93182 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a3929ee-b3b9-363b-b68b-5b23dc4a4dbb | -9.4645 | -57.66737 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a66f42c-cc5c-31a3-842a-2a7c00316989 | -11.23696 | -58.03959 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4a30342-9bc5-3195-9aa4-b6155edc3c05 | -10.92737 | -58.06683 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4ce44b-f821-3521-906a-7a0b4c575c4f | -10.92031 | -58.06561 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e723c1b1-6297-3a0d-8bfe-96fd190f1438 | -10.92028 | -58.06663 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98637c01-cfb3-3224-8fd7-0502841432cc | -10.91674 | -58.06607 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cb79ef0-7b12-3fa2-8c98-d48c5036fbfe | -10.91606 | -58.06919 | 2024-10-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7452993b-a66c-31f6-a395-eecc15c771f2 | -9.34952 | -58.9653 | 2024-10-12 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37fe93f0-38fa-3747-aef5-dd5e33050db8 | -9.34903 | -58.96752 | 2024-10-12 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83a0fbd0-ab89-3ae6-966f-b3a11302cdaa | -9.26555 | -59.39848 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc288f28-673d-30f2-9f55-8179595a2b15 | -9.23933 | -58.94907 | 2024-10-12 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a545dd37-f519-3bda-9b8a-173c169eebe0 | -9.23923 | -58.95027 | 2024-10-12 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b868068b-8d60-32fd-8f94-0007dfc51e21 | -9.2182 | -58.28053 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6442399-3724-3683-b2f8-7157a7e5cc9d | -9.21749 | -58.28485 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e58bf81d-e658-3f4a-bba3-2aede964b675 | -9.21677 | -58.2892 | 2024-10-12 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff0bf375-b9ce-3644-969b-771b78a105bb | -9.17012 | -59.37209 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 184cc187-3d32-3b90-98db-517b9ab9bf68 | -9.16927 | -59.37699 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0232a9e9-d61a-31b7-b512-bc321637d840 | -9.16895 | -59.37362 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30d8115b-759d-3952-a56b-8d9b3e2cca32 | -9.16841 | -59.38192 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55d9def2-0481-3a13-b203-db1c5b240dd7 | -8.81086 | -58.20021 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5836d97b-17c0-36c9-9a07-65585822f106 | -8.81015 | -58.20449 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b8183af-8ff1-3af5-b232-5e154330cc96 | -8.22106 | -58.29269 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a588680-2752-3f8e-ba15-e8449b3bb53b | -8.2166 | -58.2967 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 576858a9-ed44-39b1-847b-d37729d1450c | -8.1077 | -58.04733 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7de898d6-07a6-343d-b792-c91215c056af | -8.10404 | -58.04675 | 2024-10-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 744c4b9c-b3c6-31a0-8a67-b657976e2540 | -9.99254 | -59.53515 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56ff3252-fde0-302e-bec1-153245200827 | -9.99171 | -59.54008 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83412dd6-bd75-30a9-a9bd-1002689eb95d | -9.88868 | -59.50528 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5c53a1b-a588-3571-98eb-9f175fb5eeb8 | -9.78444 | -59.01426 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cce98bd3-1bd3-3503-a68a-ef08d9cd622a | -9.78441 | -59.01688 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 446ce348-6de1-3d44-9f29-43aa3d149c90 | -9.78367 | -59.01893 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 800589e0-12c3-3523-88b3-929a0a455205 | -9.7836 | -59.02154 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89d87988-e580-3a87-a7e6-a4307b605e8d | -9.78064 | -59.01624 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf6bc8fb-5a9e-30c8-ad08-3b46951c1a72 | -9.7799 | -59.01829 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc78e0ce-4349-31b4-aeae-7e798f7f7aca | -9.73438 | -59.29265 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea491635-d25d-36ca-8539-ed528dfc7d37 | -9.60976 | -59.35101 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58a57abf-689b-3a0a-859d-4eff4834228b | -10.04722 | -59.45621 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9a312e4-b0b8-3e84-98c6-66096ed98fe3 | -10.04638 | -59.46107 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94c6fd70-18fc-3c95-b92f-fc4605bbd8bd | -9.39471 | -59.33417 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c53a9b12-e8cf-39d8-a3b4-3d5085e2988a | -9.39278 | -59.33645 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c04f586a-d681-3444-9dfe-a4a95122ac50 | -9.36599 | -59.52252 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8acbc785-9b35-357f-b812-f8c71c190cf6 | -9.91266 | -58.28749 | 2024-10-12 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 979d5310-9f91-3e53-bff8-15d0662365f3 | -9.69386 | -58.65044 | 2024-10-12 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8642956b-b1db-3c61-871f-2aac7e0b78e4 | -10.72311 | -58.5132 | 2024-10-12 04:59:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c413e8c-a3dd-3ea1-8c09-d1220b84e6e3 | -10.65561 | -58.40597 | 2024-10-12 04:59:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53f91dc5-7c3a-3c12-8252-7023eeb1ca5a | -10.65272 | -58.40117 | 2024-10-12 04:59:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85a3f8cf-df73-324a-927b-e3f985e9c1ce | -10.652 | -58.40536 | 2024-10-12 04:59:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d889a470-c127-3ff7-83d8-80687b0a59ca | -10.65139 | -58.76346 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3717dc0f-c0de-36c5-8812-12121d64609a | -10.64772 | -58.76282 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 97e83acc-fa1d-3f8a-86a4-775cb9d9d73a | -10.64701 | -58.76704 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3b31cd2f-46ff-39d8-9c38-ee7300bff027 | -10.64405 | -58.76221 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5df50f5f-47e3-3f19-9d9c-8ecf991dbaf5 | -10.57842 | -59.40481 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b0bca97-5e72-3e27-a97b-7fe59cfbabeb | -10.57801 | -59.40225 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4eb6ee5-b23c-3545-a055-5bf829720edd | -10.57718 | -59.40699 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2860763-d409-3582-bd60-036430a71a45 | -10.53883 | -59.31499 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92bd9da1-a319-3e89-aa8a-317b67e51c9e | -10.53804 | -59.31963 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea2cc26a-e52c-3b21-bc7a-8875619aba94 | -10.53504 | -59.31435 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2629ecf2-1fc9-3fcd-a655-ba8003034883 | -10.47828 | -58.76741 | 2024-10-12 04:59:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README78.md)
