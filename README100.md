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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6c1f2a4-2d62-33ed-898f-baab28f0a215 | -8.62383 | -54.63301 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61cd10e6-2e1a-33d9-b6ef-3473059be117 | -7.45848 | -61.37616 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3fbda4f-1414-3e28-ae91-5edf1859a45e | -8.26361 | -55.30301 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e059e940-4886-3ae1-8cda-a3752623ada9 | -10.87142 | -50.16223 | 2026-09-22 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23f7d2df-74fe-3c3f-aa99-7cd7db81e55e | -8.60863 | -54.63505 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af1cd197-416c-3bc1-9fe0-fef9514cef26 | -11.15484 | -51.09902 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77a2fd8a-59c3-37ed-ba87-84efb3933dce | -15.43655 | -48.45009 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 982e7d52-6e29-3617-944a-ebf0a0be5cfc | -9.29442 | -58.91525 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6225b77-dec0-3180-99bb-ba544e8d5db9 | -9.95196 | -53.98425 | 2026-09-22 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35c0a5ea-a925-3431-87eb-a418e1cc348a | -9.71813 | -47.7677 | 2026-09-22 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e20e276-2b05-374d-9c0e-3eeb24727653 | -11.39713 | -46.76453 | 2026-09-22 05:25:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 996eaf73-f7d5-30f4-a627-e46cc1372c43 | -10.60118 | -53.98989 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8dbb8ef4-c772-34be-8ad2-ecd13071caff | -18.52277 | -50.3151 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a6707361-511c-36f2-9be7-ea1c6d0b0f08 | -8.24258 | -55.27586 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37c7dd7c-5db3-30f6-90e4-36d38af05eb7 | -10.60189 | -53.98504 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8acaa4de-6c49-3616-b495-d89c550216c6 | -9.07594 | -60.43866 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 195b93b2-997c-3347-a529-7e138d957279 | -10.58955 | -53.98823 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cc414e9-f528-38ef-8837-3656d661710a | -8.63175 | -54.62988 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f7ff20e-8d47-3ad7-ae6f-128f7b3e2647 | -10.74211 | -50.81332 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37fad002-4acd-31ae-9efc-366839060359 | -9.15438 | -50.01194 | 2026-09-22 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 113d1208-5e1a-3f65-ab02-8354f59cdd26 | -8.25658 | -55.30194 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 281c39ad-1696-3ca0-89ec-d69c6c43929b | -10.59873 | -53.97961 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da2fce6f-7e2e-3b13-b97e-e6f8fed7cb5d | -9.65819 | -54.32927 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fa11685-cdca-3f46-91f0-7d853772f44a | -9.12315 | -58.92044 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4454587b-6e9d-38de-b68e-8926245f0bae | -9.88548 | -48.45625 | 2026-09-22 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bcd7d86f-4984-3870-9bb2-ab65b7379a92 | -10.58253 | -53.98213 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2873b174-fc5b-328c-9447-38e5258c9364 | -10.90786 | -47.37648 | 2026-09-22 05:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79d8a30a-ba26-346a-afc0-54798a807662 | -9.11301 | -60.95147 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1072c66-801b-3858-8174-8b246f8d34fa | -18.03692 | -50.92966 | 2026-09-22 05:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b8b85abe-12ac-30a9-b8ec-fe0cda3aa674 | -10.68314 | -48.72248 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0643cc13-c576-3a2f-9237-3bfda27848c6 | -8.54046 | -54.69122 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea7b500e-862d-3ca4-84a9-a291c3b646e6 | -8.91872 | -64.30444 | 2026-09-22 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 958b765e-40f9-34f5-a3b0-1b31cf6f7c3e | -9.27952 | -60.62563 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd7486c3-57e5-3ca9-9baf-e97bb12f895b | -10.59659 | -53.99423 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2be6ddfa-c0c8-3b22-b167-51bf78ffb328 | -9.20492 | -60.28838 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74de3747-c9cf-3e0e-8d98-604fbf5064cc | -9.84855 | -48.30627 | 2026-09-22 05:25:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1df673d-d567-3e46-b30b-d7bc01836767 | -15.44238 | -48.45201 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7139bdd9-920d-361b-b7da-d026ea396db6 | -8.60925 | -54.63083 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3e67b95-24ce-35a1-a193-5ca374724e50 | -8.62208 | -54.61979 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b722bc3-bcf4-310e-916d-0323488f208a | -10.58568 | -53.98763 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 841fa789-ac00-376c-9936-5c240018ca6a | -8.48969 | -57.61287 | 2026-09-22 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87fd45ea-a832-3823-a35d-9e75bb381c06 | -8.2658 | -55.26617 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c573aa95-e465-389c-9d81-2be0a6c1e5e6 | -8.60624 | -54.62602 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73295c4a-01d1-3286-bdc2-9fc2bff0f8a4 | -9.84805 | -48.31011 | 2026-09-22 05:25:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a817cbb-8660-39e4-a20b-854f5a13a51a | -10.09682 | -46.08878 | 2026-09-22 05:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adab023a-c9d8-35b0-99ff-8899e8251c28 | -7.71114 | -61.25004 | 2026-09-22 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21653542-ce45-3d29-865d-ae33597bee6a | -8.62081 | -54.62827 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d53be3a-b551-311c-b092-c6e14817446f | -7.69775 | -61.54088 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38b7d26a-e909-3b2d-ab44-f7becf0a6cd5 | -9.66061 | -54.33876 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a72864bc-58a0-32c9-8ad1-b28235b89118 | -8.26554 | -55.26721 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27907a34-1af7-3c87-b3ee-4993186657f7 | -9.96982 | -50.25347 | 2026-09-22 05:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0dffc498-73f6-35af-b15f-55ac50294a6f | -10.60333 | -53.9753 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3fd94597-7387-338b-bd5e-096a580919d3 | -10.7235 | -53.99955 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ab50d0c-04c2-370c-90da-78fab60961b7 | -9.88433 | -48.4584 | 2026-09-22 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 777d8ccb-70e3-34a3-b4e0-1aa3c493875d | -10.60648 | -53.98074 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 080d6233-3058-3b23-859a-02d063e391c5 | -9.66128 | -54.33428 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb137606-ce66-3175-a40e-a4f7d8dc4e08 | -8.91947 | -64.30013 | 2026-09-22 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8668a9b4-7450-359c-a17c-a1679ed24644 | -11.10082 | -48.32849 | 2026-09-22 05:25:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7946a60-0d49-3359-9ed2-96c4c64ba925 | -10.74152 | -50.81026 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c270eafc-5e29-3dd6-b3ae-34c0ae6e4cca | -8.61289 | -54.63139 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cbd6c5e-b8da-3c79-baf8-d9f9c6db48a8 | -9.66503 | -54.33484 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d1cce2b-960c-3a46-8f50-1246051ecc85 | -9.75516 | -54.30008 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a6b443b-0629-301a-a0b9-70ec69ff12dc | -8.24974 | -55.25277 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f56b1a63-89bb-3d2d-9d47-0632492a71cc | -15.45099 | -48.48341 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaf6922e-7022-3fb7-a984-f3c7ba9edb31 | -9.68 | -54.33724 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9f86198-db2a-3a83-87c4-32f99e21342a | -8.26403 | -55.302 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1d7382e-9c9b-3914-b638-7d2aff88a0a5 | -10.09746 | -46.0835 | 2026-09-22 05:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d410a3e-8295-3a3e-a0b9-a267cc1f09a5 | -8.60021 | -54.61643 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3274b86-7f50-3c1b-9689-c2fd06694a2a | -7.50787 | -61.37995 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e39b2bd0-2dee-3f7a-90d4-1c9488ce5e39 | -8.61843 | -54.61924 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 212ddcb0-a282-3fc9-81e7-1b9595cb26eb | -9.48061 | -54.44238 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1b4dae4-00d8-3c39-9396-98b5794f8e9a | -10.4533 | -51.34016 | 2026-09-22 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d28a0b23-7a55-3afb-a404-e4861392f7a4 | -10.60969 | -53.99286 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c29f0816-4643-3535-860a-ac3d168d6aa0 | -11.16363 | -51.1054 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 21f5767c-df62-333f-a337-5ff0994691ac | -16.99738 | -56.45852 | 2026-09-22 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a68a0da9-782e-3a9c-99cd-ad6efca5b84c | -10.68315 | -48.7233 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f67a74c3-5cf1-3443-afe2-b5dbf4eba00a | -9.28437 | -60.61829 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 488ed3a7-2ff6-3561-bb2c-78f7142d5675 | -9.28458 | -60.63876 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1dfa47f-bc1d-3223-a5c6-c42221826186 | -10.59975 | -53.99959 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 853ba9d4-7ce0-3219-b0e0-712e26a01115 | -16.81726 | -50.56548 | 2026-09-22 05:25:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c66eb1-d89a-3156-980b-381e8cf915b7 | -10.719 | -54.00648 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95869ae7-0fff-39e5-9ef2-a82e0bebede5 | -8.91892 | -50.92738 | 2026-09-22 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2a6794ea-230f-37cb-905a-d7e7ce5ee1a9 | -11.107 | -48.32538 | 2026-09-22 05:25:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c46d7887-d19f-307b-b768-2205f1967725 | -10.74632 | -50.81093 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed202591-b86f-3162-be4b-ce019c5ccfd7 | -9.88479 | -48.45477 | 2026-09-22 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b45bb8ff-d36e-3b7c-8871-a8d12a4f8ea2 | -11.09507 | -48.32822 | 2026-09-22 05:25:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 607b25e5-9325-3814-b197-24a0aeb22ebc | -16.85048 | -56.78203 | 2026-09-22 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 33132e95-10f0-3ad5-988a-1496461f83ca | -15.60318 | -48.33128 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80f828b3-9b31-33e4-89c1-184e77998d79 | -11.1643 | -51.10034 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4ce76dd8-ba4d-3618-8c8c-13b409a85900 | -9.10942 | -60.95085 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e036e25-95ef-351b-b73f-45354ade940c | -9.94812 | -53.98364 | 2026-09-22 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 537f3bb0-4ede-3bb5-ab65-fa57ad78d03f | -8.60988 | -54.62659 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60cda02c-a3b4-3b48-b26c-6e235fb7c02b | -10.45602 | -51.32963 | 2026-09-22 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f47fd0e-173b-3b1e-a820-a557b2185b5a | -8.61406 | -54.74778 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 412516ce-3522-314a-acf4-159a72a94289 | -16.93081 | -53.57998 | 2026-09-22 05:25:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf5ee108-281a-3a7d-b10b-1c13f7b93d0a | -8.60561 | -54.63026 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d40883f3-2717-3e50-930d-73c800a8e187 | -8.49247 | -57.61689 | 2026-09-22 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a268e2b-b58c-3f87-bb49-210ef0a434a5 | -9.72909 | -54.80602 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a89ccfa-cbf4-3ace-b13a-280be6ecbd95 | -9.9283 | -58.31325 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 643be16a-8100-3c5d-8b87-35f5191b3105 | -10.60514 | -53.99714 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README101.md)
