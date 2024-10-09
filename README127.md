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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb6a3658-e327-3238-89ff-0593f616379d | -2.94557 | -53.70691 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be02f114-c9da-389f-80be-87dc288c5085 | -2.93771 | -54.82005 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c963f655-8f1e-3ecc-807b-6cb49ba739f0 | -2.93357 | -54.17448 | 2024-10-09 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 388d9422-d0db-3d25-b01f-ade7e975017d | -2.93328 | -54.81945 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a65085a8-0b65-3763-a7b8-ad32f06eccba | -2.93294 | -54.17839 | 2024-10-09 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16880b2a-8dd1-386f-b6c8-386b135c1987 | -2.93231 | -54.18231 | 2024-10-09 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c4ee085-92d5-3cdc-acfe-9d730781ca8e | -2.91935 | -54.12843 | 2024-10-09 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebf540e9-d4f4-3029-92f0-7be64c617cc8 | -2.89864 | -50.71474 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af139d81-dc9d-35cd-86b5-a3083a177bac | -2.89639 | -50.70659 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47a6bfee-fa72-3dd7-a75a-9d5c7f755f01 | -2.89578 | -50.71039 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d50d9df4-2381-30a3-b377-a93c64228335 | -2.89517 | -50.71419 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a422e55e-7a67-3b75-a2fa-55d2f82f32cf | -2.89169 | -50.71364 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 798f54f3-8e9a-30a7-aeff-c660ac633a58 | -2.88969 | -52.40022 | 2024-10-09 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b585b8c8-463d-39c5-a748-a5d463b852d7 | -2.88536 | -50.70874 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7d9219a-43d7-3e91-9b5e-d90153c9f114 | -2.87808 | -51.67591 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d0fe7b2-02ba-3e47-8248-c81eff34b34a | -2.8777 | -53.95843 | 2024-10-09 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b7d1abd-7851-3672-9d21-5af0e90b557b | -2.87751 | -52.90188 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2848cc67-661f-37e2-8e77-2a8bc9580d8d | -2.8771 | -53.96217 | 2024-10-09 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dc00a2f4-8991-3d14-9750-2f3fc001fa6d | -2.87672 | -52.90672 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67f5e7fe-5f5b-36fc-8007-3172fcb4593c | -2.87353 | -53.95778 | 2024-10-09 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9d75772-d406-3c50-8a38-6762aef7694e | -2.87293 | -53.96151 | 2024-10-09 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4ea509f0-a18f-3b3b-b30d-686b975d0bbc | -2.87282 | -52.90616 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f03b66ff-f23b-39ad-a2a9-5946bd6f185e | -2.86035 | -51.02083 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b3c985d-06d6-31d7-85bf-ec110b4437d5 | -2.85683 | -51.02028 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57892f31-5e02-38d9-b0ea-622c720142e6 | -2.85511 | -53.93935 | 2024-10-09 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03d6d3da-25fe-3005-ae11-92ad7e4e35fc | -2.85094 | -53.93872 | 2024-10-09 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb7ba196-eeb1-38eb-84c0-eee7530d87c3 | -2.84678 | -53.31792 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07dffd91-8cdb-3b86-a3b9-29d27b919791 | -2.84278 | -53.31727 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af8c41f4-f4ad-37a7-8988-3e31efa0bcbc | -2.84195 | -53.32244 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c6b070f3-3065-3efd-b8dd-f583d798c1af | -2.84052 | -52.9595 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f296c3c3-7eb0-3308-9fa5-92df3643192f | -2.83982 | -52.96109 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31ee555d-bb34-3b0e-a17d-0275e7d94147 | -2.83974 | -52.96445 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3999ff3a-4a55-3a03-a8cc-b9774e1bdfb7 | -2.839 | -52.96603 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b94a93d2-7127-32d8-9157-998f1a388374 | -2.8366 | -52.95894 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 376caccd-4bdc-31d5-a764-4363abd4252e | -2.8359 | -52.96053 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 898e29c2-d7d4-3980-be4e-fcc904b28784 | -2.83582 | -52.96387 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7da1dff2-8a24-349d-9656-55b7d16b8e87 | -2.83509 | -52.96546 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ff62654-8d20-3c14-982c-59468ab23c3d | -2.81384 | -54.35984 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c07a40dc-99be-3ff2-8912-49b501d8e1b6 | -2.81321 | -54.36378 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db691902-0038-3f85-997c-f0f248dc7988 | -2.8129 | -54.59205 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4005e02-3195-3a1d-9e0b-c210aaf743b8 | -2.80955 | -54.35917 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c36c86b5-310d-32e5-b167-d3d829b0222e | -2.80892 | -54.36313 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7fb9a12e-31d2-3a21-b8a8-597f0df35fb9 | -2.80816 | -51.39209 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 036dfff8-e3cc-3dee-bc3b-29cc4bf43bdb | -2.79621 | -54.58277 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d611a0b-6dad-3a9f-952e-8f78af145c7d | -2.79617 | -54.58509 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed3a0c35-1b06-362c-adb7-76a772803be1 | -2.77262 | -53.21003 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15a68833-93df-37e1-8b6c-dd45fd99d86a | -2.74466 | -53.95426 | 2024-10-09 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7fe2ee3-25bd-3935-9232-8b9a3baee23b | -2.74405 | -53.95807 | 2024-10-09 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c976b1dc-5b96-33ff-89df-411a870324fb | -10.12746 | -48.7125 | 2024-10-09 04:38:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf263580-4bcb-357b-8796-3aba229dc6f5 | -10.01248 | -48.84686 | 2024-10-09 04:38:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88f47fa0-1e75-3534-9195-cecb3ab11360 | -10.00911 | -48.84632 | 2024-10-09 04:38:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28aa2aac-cd54-3e4e-8c2b-b9f3516bb56c | -10.00856 | -48.84995 | 2024-10-09 04:38:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d2b3c71-7f3d-37b4-a4b4-1acb914d3536 | -10.96957 | -48.5372 | 2024-10-09 04:38:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d582429-a9e8-3f83-9bf3-b4d4e4c10719 | -10.96443 | -46.71841 | 2024-10-09 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dd32875-4983-3f00-bc72-8ac3152708b0 | -10.75775 | -47.91471 | 2024-10-09 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 380e2c3f-463f-337d-a05a-4189d8258970 | -10.72494 | -49.83698 | 2024-10-09 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4e86213-6721-364d-ac79-f4315d5e2a91 | -10.67671 | -48.72115 | 2024-10-09 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a8f54fd-0b91-385f-a509-da0b13f842c7 | -10.5543 | -47.76004 | 2024-10-09 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7cf9a9cb-6c1a-365d-9faa-550b3618bb30 | -10.53967 | -49.46029 | 2024-10-09 04:38:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df8a989d-0a32-3467-87d5-0f9e6607781d | -10.53912 | -49.46384 | 2024-10-09 04:38:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd9a6828-461f-346d-abd1-2f1bedfe541d | -10.53785 | -49.46043 | 2024-10-09 04:38:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eabd25b3-4508-3931-b85a-6107217c7307 | -10.5238 | -49.10714 | 2024-10-09 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec041c4f-4c7d-381f-b715-9ac9dc0875d1 | -10.52325 | -49.11073 | 2024-10-09 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24e5b12c-a5bd-3eec-95e1-a87fb396fb41 | -10.52044 | -49.10662 | 2024-10-09 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebf98a11-c21b-3d07-bf00-cf8604d51ce2 | -10.51989 | -49.11021 | 2024-10-09 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b359898d-3c20-388c-8c21-b701e05f0df5 | -10.51708 | -49.10609 | 2024-10-09 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4437073-3103-30cf-8f7e-a40487faf482 | -10.49487 | -47.5321 | 2024-10-09 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4b6cb9b-ec3c-3a41-ab08-a64b994af739 | -10.49426 | -47.53616 | 2024-10-09 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dac03d9-689e-36b5-ab70-94d281f36d7b | -10.45645 | -48.03184 | 2024-10-09 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 143e2305-1d16-347f-9378-d65602613dd0 | -10.40751 | -49.42493 | 2024-10-09 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0108ed0c-947d-3e27-8010-80a1477602f6 | -10.40696 | -49.42848 | 2024-10-09 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0702ea35-99ea-369b-85b6-6fc93849fd74 | -10.40417 | -49.4244 | 2024-10-09 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3248be8-2941-3109-a743-72bf49c5ee0d | -10.2327 | -47.50221 | 2024-10-09 04:38:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e09393d-ddfd-3800-a983-44158537489c | -13.815 | -44.60083 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b6805152-f4c7-3f88-aa50-4a31f9710585 | -13.82415 | -44.59094 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79476f43-b629-3702-99dc-4212b531ffed | -13.82358 | -44.59541 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb08f0ee-7517-3af1-96b4-36f37afdadd0 | -13.8206 | -44.5926 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2fd66a54-dc5e-3cd9-b699-3f19cd7aa819 | -13.82 | -44.59704 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e13d4056-c08d-3442-8683-7db9c5703e2f | -13.8194 | -44.60147 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a95d85f9-959e-358a-9263-2213a5df2714 | -13.81881 | -44.60587 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6d954255-0740-344a-9e05-61b41556abbb | -13.81862 | -44.59917 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b44f821d-389b-3b39-aaa8-b0d42e9f4c49 | -13.81805 | -44.60361 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| cee8826f-2d72-3e20-9b4a-28b1c60606a6 | -13.8175 | -44.60798 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3fa3f671-25eb-35bb-9f3f-cb483fc64478 | -13.81707 | -44.61876 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d13fe739-de37-3a3c-abc8-8bcdca1af310 | -13.81641 | -44.6166 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6f88213-5564-3569-b190-9aeacb9a615d | -13.81619 | -44.59195 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f1120edd-74db-3ee1-9e3f-e41d5915bf32 | -13.81586 | -44.62087 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 408c9c7f-900f-3739-8240-6914cd9872c0 | -13.8156 | -44.59639 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 741e367d-dbe7-3c6d-827f-2a4ae7ba026a | -13.81478 | -44.59408 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4433e1ba-4da8-326d-8b4d-4ab48e5818f2 | -13.81441 | -44.60524 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5a0a87db-c9ca-36fd-a9ce-cf5ad474ece6 | -13.81421 | -44.59853 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bbb71fc2-ce80-3004-bf85-29755c1bec61 | -13.81365 | -44.60298 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b90fa37f-bc02-3ace-84ae-db58779ca5ab | -13.8131 | -44.60735 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0b49c8b4-1e9a-3531-967f-7dbbddfa248e | -13.81268 | -44.61814 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 58d42252-5286-32c5-aa0e-510c9a5e2d89 | -13.81201 | -44.61595 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e207b587-d9d4-3958-93b6-515ae984163c | -13.81146 | -44.62024 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ff2c21a-96b4-39c7-920d-d52f9456cdbc | -13.9024 | -44.50817 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da503bb3-7387-36cb-8611-79430fa5fed5 | -13.90181 | -44.51264 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1339d2a-a4da-39bd-877a-1ab88da0960e | -13.89585 | -44.27773 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52f52360-0f14-31b5-a4df-c3799846edfb | -13.88336 | -44.6527 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |


[Clique aqui para ver as próximas entradas](README128.md)
