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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51a06046-6d22-3c23-b5ac-636e5fb24c3e | 2.2333 | -60.7018 | 2026-02-25 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 09716927-b0a7-3243-b50e-efddef89e3fa | 1.5046 | -59.9306 | 2026-02-25 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| f840f658-b98d-363d-b087-dc48f37470a9 | 1.5229 | -59.9305 | 2026-02-25 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| fa87fbc8-9fb4-3f03-9ab1-42efb9614c60 | 1.4864 | -59.9308 | 2026-02-25 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.1 |
| f630e6f0-2f59-34e0-a81e-8934976fe191 | 1.5046 | -59.9497 | 2026-02-25 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6b129ede-a5b6-3b4e-afda-5d71e222f80a | 1.5046 | -59.9497 | 2026-02-25 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 171.7 |
| 811816d1-59a5-310b-b2f4-77768d0ec826 | 1.4864 | -59.9498 | 2026-02-25 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.3 |
| c71764fa-2405-3e35-8917-dcdb1b2e47c1 | 2.2333 | -60.7018 | 2026-02-25 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 904be089-f719-3ea1-b39b-de6f34f5c061 | 1.4864 | -59.9308 | 2026-02-25 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 98ea1700-e862-3069-aca6-faed86c45d8e | 1.5229 | -59.9305 | 2026-02-25 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7fcadfa0-7691-3375-bb78-a52698a12dbb | 1.5046 | -59.9306 | 2026-02-25 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 205.6 |
| f6c4f27f-4e1e-353f-9be8-827338a83883 | 1.5229 | -59.9495 | 2026-02-25 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8199fd72-08c0-3a0b-b333-6e2b3ab6b056 | 2.2333 | -60.7018 | 2026-02-25 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2273eb33-edf9-3b02-8d45-194116c3cd41 | 1.4864 | -59.9498 | 2026-02-25 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6a3a15c1-0c0b-354e-90b9-780ddb355710 | 1.5229 | -59.9495 | 2026-02-25 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f62f7d28-3d81-3a54-a4dc-4e2138e47aa5 | 1.4864 | -59.9308 | 2026-02-25 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 0ed42347-2c94-3b17-82e1-361174c3ee89 | 1.5229 | -59.9305 | 2026-02-25 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 799a22c1-37f5-3645-8a6e-71eb9d92c92d | 1.5046 | -59.9497 | 2026-02-25 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 71b595cf-d418-3441-8ae9-ca0e4de7840b | 1.5046 | -59.9306 | 2026-02-25 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 5ebd1a37-9937-3fb5-a47a-3a9c4f4cb26e | 2.2333 | -60.7018 | 2026-02-25 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 09397e5d-a90b-3f3a-a41d-376e4bdb2dff | 1.5046 | -59.9306 | 2026-02-25 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 203.9 |
| 3e7b711a-ced4-35de-8a7b-abcc97a15ca6 | 1.5229 | -59.9495 | 2026-02-25 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b182e97c-d9b4-3a1c-ac22-2ec0a4cfa577 | 1.5229 | -59.9305 | 2026-02-25 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e941950e-cf9a-3533-8c7c-d14b79aea800 | 1.4864 | -59.9308 | 2026-02-25 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 69d69906-e40e-371a-9084-2b68b5216664 | 1.5046 | -59.9497 | 2026-02-25 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 184.7 |
| b12f9c4d-8af2-36e8-b0e4-b2d0637b2ee6 | 1.4864 | -59.9498 | 2026-02-25 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.2 |
| b24c17cd-85f5-3fd4-94b0-f5fe2dfea4d9 | 1.4864 | -59.9308 | 2026-02-25 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 07c058cc-b9ea-3ea5-99a8-a3e608c7c876 | 1.5046 | -59.9497 | 2026-02-25 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 05cde80a-a67c-3460-b98b-8a173dbcccdc | 1.4864 | -59.9498 | 2026-02-25 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 102.4 |
| fcfc6bda-a951-3385-b5f9-4f0252ebcfda | 1.5046 | -59.9306 | 2026-02-25 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 209.4 |
| 2af83136-3c31-38d2-a8e2-b22bbc2b623f | 1.5229 | -59.9305 | 2026-02-25 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8429ff85-1962-3eb6-93ad-7660637ab102 | 2.2333 | -60.7018 | 2026-02-25 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0673f93c-b344-3ba8-b3df-111f944edc8d | 1.5229 | -59.9495 | 2026-02-25 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7c65aa75-2c98-3582-a4a7-419bd57ccd1e | 1.5046 | -59.9306 | 2026-02-25 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 228.5 |
| d4aaafc8-0556-3483-b1e3-4c03661533f8 | 1.4864 | -59.9498 | 2026-02-25 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 8f093790-f1af-3051-a2c7-40fdb706bc98 | 1.4864 | -59.9308 | 2026-02-25 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 9e870b46-9884-3350-ad26-6a4a47cd7e63 | 1.5046 | -59.9497 | 2026-02-25 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 892bac66-fc4b-3741-84bb-063e8a5da9f7 | 1.5229 | -59.9495 | 2026-02-25 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 3cfcc5b0-2bda-308e-adfe-0e33d95b00bf | 2.2333 | -60.7018 | 2026-02-25 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9bb1a4b4-57d8-3db2-90e1-97c56265623a | 1.5229 | -59.9305 | 2026-02-25 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e164287a-52df-356c-8266-5cdf0daa999f | 1.5046 | -59.9306 | 2026-02-25 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 191.3 |
| a9d8a6c4-3dd7-3693-8d41-cbe6145f8161 | 1.5229 | -59.9495 | 2026-02-25 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3729d88f-cb91-3c80-8889-c4638a3c5d74 | 1.4864 | -59.9498 | 2026-02-25 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 191e4367-2948-34ca-bd5c-c6392d82c3c6 | 1.4864 | -59.9308 | 2026-02-25 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 03a9ab47-5ff1-3a7e-8849-cf326c7ce97c | 1.5046 | -59.9497 | 2026-02-25 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 549d6275-0d10-3bcb-a3f3-89a5b6291210 | 1.5229 | -59.9305 | 2026-02-25 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b9777c9c-588e-3c26-8e93-568fe886c474 | 1.4864 | -59.9308 | 2026-02-25 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 6f66e365-b912-31c7-8808-b6bfb18fb5a9 | 1.5229 | -59.9495 | 2026-02-25 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| eced4c6c-1877-3998-90f0-e7f5ee897f2a | 1.5229 | -59.9305 | 2026-02-25 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 54d43fe4-279e-3ced-b46c-911c0da84e8f | 1.4864 | -59.9498 | 2026-02-25 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 9cf5bdb3-717b-3e11-828c-2906921f41a7 | 1.5046 | -59.9306 | 2026-02-25 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 1b477edd-f102-36cc-902d-28caf4ece993 | 1.5046 | -59.9497 | 2026-02-25 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 5bc17979-f184-38e0-8fc2-f8f4bd375e0c | 1.5046 | -59.9306 | 2026-02-25 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 177.8 |
| ad1ab52c-476b-3087-885d-05a8ebd91fcf | 1.4864 | -59.9498 | 2026-02-25 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 76a9a793-ab0f-304f-97f7-f05a2a5ac81d | 1.5229 | -59.9495 | 2026-02-25 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 29034fc2-ef02-392b-94ff-839e8367f10d | 1.5229 | -59.9305 | 2026-02-25 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 65011dd7-ea5e-3124-a246-eba1b2161ef0 | 1.5046 | -59.9497 | 2026-02-25 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 177.7 |
| e37ceadb-1c75-3072-8c58-935036a9b511 | 1.4864 | -59.9308 | 2026-02-25 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 5c484bce-2153-3331-88ae-162193ac2970 | 1.4864 | -59.9308 | 2026-02-25 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.4 |
| e5b80a5b-b08c-3ff5-bd01-595017b3b62d | 1.4864 | -59.9498 | 2026-02-25 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.6 |
| b4650a1a-be4a-35ce-8245-861754dbdb68 | 1.5229 | -59.9305 | 2026-02-25 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f85ebf0b-8516-3a3f-a168-4cbf2202c2a5 | 1.5046 | -59.9306 | 2026-02-25 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 3b34bfc3-b5ac-3dd2-8fa0-d1204f84033d | 1.5046 | -59.9497 | 2026-02-25 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 52d54b33-3920-39b9-904b-346df40c426d | 1.5046 | -59.9306 | 2026-02-25 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 5a970ff7-67ae-3aad-80b4-6a5023db903c | 1.5229 | -59.9495 | 2026-02-25 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 59fafd25-474d-31f0-8e8f-d2d77383cd67 | 1.5229 | -59.9305 | 2026-02-25 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| cc84f33e-0b8d-3b3f-b5d8-162cfa2c0009 | 1.4864 | -59.9308 | 2026-02-25 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 19fec8fa-7836-3888-872f-699fdcfe5edb | 1.5046 | -59.9497 | 2026-02-25 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 0318baea-ffbe-397d-93c9-cd9bf5b394ad | 1.4864 | -59.9498 | 2026-02-25 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 9408286b-2007-39bc-a7e8-1110bee23910 | 1.5229 | -59.9305 | 2026-02-25 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 701f2f2f-cf07-320c-8896-4f3b3268f4e7 | 1.4864 | -59.9498 | 2026-02-25 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 137.1 |
| d972da3c-5979-3cb3-941d-47459487d361 | 1.4864 | -59.9308 | 2026-02-25 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d3ac4b62-2177-3b97-a623-91423aa39d73 | 1.5229 | -59.9495 | 2026-02-25 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 7d068ee2-b5a8-396e-a208-d7d1ce9ce36f | 1.5046 | -59.9306 | 2026-02-25 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 159.6 |
| b0bcf26e-3e4a-337c-8d5d-96f547967749 | 1.5046 | -59.9497 | 2026-02-25 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 29cc5a80-94a1-3250-abb4-46393da9de8b | 1.5046 | -59.9306 | 2026-02-25 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 91636c5c-e892-3798-a614-33ba5169275a | 1.4864 | -59.9308 | 2026-02-25 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 8e72dff5-5b4d-355e-93ce-7b25e05e5a88 | 1.4864 | -59.9498 | 2026-02-25 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 1e3e6a9c-d943-3103-b709-a49c4719702c | 1.5046 | -59.9497 | 2026-02-25 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 167.7 |
| bec4b2a0-ec9f-3301-b837-16d797418281 | 1.5229 | -59.9305 | 2026-02-25 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 16d9c834-57d6-31fd-bc5a-b7a209b24746 | 1.5229 | -59.9495 | 2026-02-25 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 7cd3c71c-73c1-34f1-926c-66d8f4608856 | -5.4145 | -37.4804 | 2026-02-25 03:23:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 902651b1-d566-362d-afc5-f669a11a4536 | -6.08011 | -37.30999 | 2026-02-25 03:23:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef6d99d5-8e88-3839-9155-851fa8177138 | -6.07557 | -37.3092 | 2026-02-25 03:23:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a5931b5-ac86-36dc-97e0-97ebc7335903 | -9.92968 | -37.45316 | 2026-02-25 03:25:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b2742453-f449-32fd-b953-a7a102e5db21 | -9.98349 | -35.99827 | 2026-02-25 03:25:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| a13863f5-8f75-3258-bd05-b7a10702046c | -9.93199 | -37.45373 | 2026-02-25 03:25:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4bfddf01-ae06-3573-84ee-b087a93c75ee | -9.41297 | -35.56113 | 2026-02-25 03:25:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 20627533-e515-3f7a-958a-23964c52ffcc | -10.18718 | -36.50775 | 2026-02-25 03:25:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c70a339-548a-34d3-aeb3-63a8afac4627 | -10.19181 | -36.50491 | 2026-02-25 03:25:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50219d7f-c8bb-3efa-99bd-2ac566ceaf78 | -9.9277 | -37.45295 | 2026-02-25 03:25:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c935d698-f650-3967-b4df-6c6c2697603b | -9.41215 | -35.56593 | 2026-02-25 03:25:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c1a7e737-525b-3923-959e-ec3e5d2d2aee | -9.62121 | -36.97177 | 2026-02-25 03:25:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 398176e0-4e63-3c15-a874-a4a36b2ca12f | -10.18779 | -36.50421 | 2026-02-25 03:25:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 23ceef34-b35e-37cf-87dd-9b64e35dbb89 | -9.98739 | -35.99898 | 2026-02-25 03:25:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| ba053042-5243-3ca7-9bcc-4caff6a57fb4 | -9.69982 | -36.99714 | 2026-02-25 03:25:00 | NOAA-21 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6834d67b-8756-3b6e-9b1b-54a6010e46e2 | -9.81033 | -38.10226 | 2026-02-25 03:25:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2138aef2-f658-3515-b11d-e1c55a5badfc | -9.81121 | -38.09747 | 2026-02-25 03:25:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 454bcbc5-3358-362a-b270-c1af05fd6c89 | -9.76061 | -36.1442 | 2026-02-25 03:25:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e74205a7-3746-3725-8e0c-de67cc7abe34 | -9.81368 | -38.09845 | 2026-02-25 03:25:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README3.md)
