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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9618017d-ef19-388a-936a-f8a519726f7d | -4.13267 | -51.18649 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fb8a363-9daa-3eb5-9e3b-b384fd085082 | -2.86637 | -46.76762 | 2025-10-27 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e03a2369-d443-3f26-9c82-c168fdb78cd6 | -3.3902 | -50.39904 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0763c23e-37cd-3660-b0f6-193c673e7a15 | -4.39549 | -43.32149 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a008679-96b2-36d0-83ed-630d6de170d7 | -4.4293 | -45.98104 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2888ecc-e18d-394d-a47c-7df774025a7d | -3.84243 | -55.79435 | 2025-10-27 04:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c00d27c9-b381-38f5-ba73-67ff5cc977df | 0.16471 | -51.01765 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0cc14c9-16ca-3a00-90b6-6e5e2d12243b | -4.47436 | -43.42757 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e3febce1-223a-300d-947b-3e264cbeff3f | -3.39085 | -50.39482 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ea5b752-09fd-3778-b4bb-a40d4d898f75 | -3.8653 | -50.88855 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2d11a4b8-b105-31ef-b97d-e1acee80709d | -4.8003 | -43.30483 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38425451-9ad6-3dfa-80c1-c2b27cd7eaf9 | -3.25591 | -50.04197 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca293687-df4f-3001-880e-268a4e8d36ed | -4.31441 | -48.22674 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cabba93-b499-317d-9bd6-79fe6aac2b80 | -3.09605 | -49.45807 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fa01550-d519-334b-ab0b-32a2b80ebb05 | -3.83896 | -55.79382 | 2025-10-27 04:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d5e995f-dc48-3b79-9807-33dcd5869bdb | 1.61935 | -55.7294 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e062c95-c592-3261-9124-5aed4a9d1eed | -3.23849 | -50.65475 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cb5db65-ada9-3d70-8da5-4c824763246a | -4.44681 | -43.42162 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 394d5050-f25e-3cb7-956f-d8970e1d8264 | -3.98618 | -51.03514 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c74e2bd-43d9-3e02-b30c-b2d82e5842fd | -4.83331 | -45.3358 | 2025-10-27 04:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13cc6634-5f06-3d41-a701-83e149c3ce3f | -4.20893 | -48.35452 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0854303e-5ca3-38b3-abee-dadc3cd8e535 | -1.38173 | -55.34463 | 2025-10-27 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f28680ee-8b89-35b7-9535-6c306e9b2ec5 | -4.95239 | -44.8763 | 2025-10-27 04:59:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1273f4d-3b1f-3570-90ab-3f51dbbf48ea | -4.12433 | -48.80988 | 2025-10-27 04:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8e9e03e-0ebd-3964-b0d6-44c8250194ba | -4.47493 | -43.42347 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 66301c6b-0ebb-3687-8b5b-3d5acbad047d | -2.90448 | -53.13226 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d6a27a5-dc59-37ab-af35-5353359c8bc6 | 0.43812 | -50.82525 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0216615-9d0b-3c99-89fe-12865f399fc4 | -3.72936 | -51.3485 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd7a0b1a-d21c-3e88-8116-a1d2610de7f0 | -4.10389 | -48.02295 | 2025-10-27 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3404b50a-0e12-30bc-90fc-4c3be8ada1fc | -4.44503 | -43.43377 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 319b16b6-0d54-373d-bb6c-d9b09e784243 | -3.27158 | -51.62739 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14e3ad00-d717-3b1b-a8e7-3f1be350a18c | -2.63294 | -47.2975 | 2025-10-27 04:59:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 079aff48-4e9e-3103-8fb1-fb91d633beb6 | -4.51721 | -44.04312 | 2025-10-27 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7553c55-8e80-3f02-b4e9-dfee734d4ca0 | -4.45265 | -43.42242 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cf544d5-ded3-3329-ae57-9646c403cc65 | -2.44321 | -48.99782 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f821d1d8-58f9-3300-b613-35986646956c | 0.45066 | -50.81572 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 761929ef-112f-380d-9e07-219bf6c091c0 | -2.81126 | -49.15156 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cd4ebf1-b5cf-3a08-a251-80efc2926a99 | -2.1866 | -52.49353 | 2025-10-27 04:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9c8fd57-852a-3f6e-8b75-0d2237fab1b5 | -2.67709 | -54.65052 | 2025-10-27 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06d9b380-7482-3110-bab1-220cce5ec4fe | -4.3572 | -48.66359 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a547024f-c5c0-3db6-9607-0b6117424be2 | -4.46854 | -43.42659 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2231d370-6691-3586-b87e-55a12f5d556e | -3.12023 | -51.20819 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed93ceef-0fd5-3e64-8f3a-629df0e4f10b | -3.83853 | -50.19626 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 240ac478-9d9b-391e-9796-b38dd51c0bb5 | -3.11208 | -51.21474 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c4b1349-bc09-3a1e-9c53-531d6a5893dd | -3.23554 | -50.65015 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e058990c-5b6b-31f3-821a-3ca30db64f84 | -5.5248 | -41.71672 | 2025-10-27 04:59:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 956d86e2-6990-30cb-adf7-a6724ea7575a | -1.15466 | -54.20506 | 2025-10-27 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c2e4f2-f338-3066-9832-08ee3616f96a | -3.85672 | -52.17306 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 061acba7-3e42-33cb-932b-2c569723b33e | 1.14307 | -51.06404 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f113b6b1-9da6-3c32-bd5e-2a419b53aeb9 | -4.44087 | -45.98487 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 03f546e3-755d-3134-aefb-53b4740c8ace | -4.95771 | -44.87718 | 2025-10-27 04:59:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0913f7bc-d1c0-37b6-be95-bdb24a4e0b65 | -1.94106 | -56.76581 | 2025-10-27 04:59:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 026ccbf4-d5d1-3149-99a4-3520961ec72b | -4.45138 | -45.45707 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b8a2e6d0-a602-34cc-a606-168f22a913f0 | -2.61436 | -51.74682 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ffe8947-67a2-38d5-a9ca-7cab0839cbcf | -3.04339 | -53.02256 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6923419-6c9d-35c9-93c6-4bb15c22c338 | -3.56961 | -44.52498 | 2025-10-27 04:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 492d9716-19fc-3f3b-b745-190ccfafa0ed | -4.83138 | -45.34216 | 2025-10-27 04:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a516050b-7dbf-38e5-812e-3998dc9c0d98 | -1.19378 | -53.38288 | 2025-10-27 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca9463ce-d627-30a0-bcd4-f750b17bdacb | -2.86257 | -41.75783 | 2025-10-27 04:59:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 667d4695-62b9-3e77-8a03-92dacbfdc66f | -4.83197 | -45.34526 | 2025-10-27 04:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81eec87d-50fe-3fe4-9746-b51fd926ba72 | -3.80072 | -49.29233 | 2025-10-27 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 57fdf29b-52e7-3cb0-b5e7-a88545e993e4 | -3.46528 | -47.68951 | 2025-10-27 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19a23044-7f79-3f1d-9971-5a1881812d5d | -2.94773 | -51.75967 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc937d34-a0dd-3f22-ae4b-2028072bc684 | 1.24711 | -50.90738 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d15806df-f1ac-3204-a2ad-d96f66eabe49 | -3.57986 | -43.60458 | 2025-10-27 04:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b37b4fe8-978c-351e-8a6d-46bc728ddc2d | 0.44723 | -50.81625 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06c9ff2f-dbe0-3e84-a70a-5cc13fddbbf6 | -3.88328 | -52.2473 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b80b27c-cf2e-3cfc-9c85-f158018f1d32 | 1.6157 | -55.72995 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54dbe68e-32e5-300e-b2c2-3fcae424f60f | -4.46955 | -43.42906 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 308850cc-88ed-3f4e-bc7f-b36caa7cdc6e | -2.355 | -48.29065 | 2025-10-27 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08590da4-cc33-37c2-b36b-0b364a973318 | -4.47084 | -45.32457 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1da57a6-64f0-3ae5-aeb8-dc6fde6e4dc3 | -3.67179 | -52.5111 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 437231f4-9a4d-3047-99ef-a6007d6b7fb8 | -3.09986 | -49.45866 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 931241a2-0962-3810-a8aa-a6f97eae2918 | 0.43469 | -50.82579 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0ea079a-42e1-38cc-ae71-7f42b614b1e8 | -3.98192 | -48.98984 | 2025-10-27 04:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68c2075b-4628-3570-b02f-217e113b1d35 | -2.22774 | -51.87304 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2649610d-8251-35c9-83b4-16ccd8a05e07 | -2.12568 | -56.84475 | 2025-10-27 04:59:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c381c6a-ddb6-31ef-98de-91edf846e5d0 | -4.4778 | -43.41357 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 940c7325-39c6-349c-8e79-853fb7125a49 | -3.9383 | -54.8476 | 2025-10-27 04:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5a26f61-973b-340e-becd-e60d095aac9a | -1.38459 | -55.34902 | 2025-10-27 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 761db0a9-c0a1-301f-a0ed-236ff6e8c6db | -1.69375 | -55.67183 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f04a5f11-1110-3cc4-850c-738e485f2790 | -3.94723 | -48.09143 | 2025-10-27 04:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1ee4298-f6a5-39de-99e2-6a3adfa66bd9 | -4.47137 | -43.41671 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5efe2d5c-9d16-335e-b8d8-5587e09030c5 | -3.86051 | -49.80067 | 2025-10-27 04:59:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc95d422-2e52-3118-999e-3b7928271d36 | -4.3734 | -46.80676 | 2025-10-27 04:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1313d62-b558-3150-ac8d-b293e019c344 | -3.09817 | -54.61825 | 2025-10-27 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6624f914-54b2-3650-8c5d-f41012657fb2 | -2.4841 | -58.04246 | 2025-10-27 04:59:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efe1b0d8-eb6a-3e11-a6a3-5b324b19db92 | -3.05113 | -53.01665 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 098fbb3a-070a-3f0c-b143-588c4c729192 | -4.4474 | -43.41757 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67106c42-d359-321a-b35d-4e819d8e6b8f | -4.14237 | -50.6867 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40ba2bb8-67a8-35fa-99f7-f10af31321fe | -2.97415 | -51.03306 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15e3f801-b1dd-3e29-95b9-84cf540619e3 | -4.26365 | -50.50834 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eb24520-160e-3e75-86a1-d749fa09217a | -4.63076 | -50.41769 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 148c710f-4441-3601-af9b-6630ece1b00f | -3.46896 | -49.96412 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e072496d-1637-31aa-948e-a5e59237703b | -4.45909 | -43.41913 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cdf3669-9d1b-3689-b7c8-1ca23ddea102 | -3.92866 | -52.25109 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7daf1e7-f97e-327b-8b34-85e9ec93313b | -2.94091 | -51.75859 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ed35811-cafd-3ad3-b9ce-bc832b1fc8dc | -2.0084 | -56.90012 | 2025-10-27 04:59:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5300c403-0509-34e0-bc76-c942e5c52528 | -4.44166 | -45.97943 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0b60d2cb-f646-345e-ab0d-965842433e36 | 1.15209 | -51.05524 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README57.md)
