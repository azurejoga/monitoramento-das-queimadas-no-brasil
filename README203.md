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

## Dados Diários - Página 203

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a30afb10-5f7c-3039-b4d6-80a29091485b | -10.54853 | -69.09821 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 678f35bb-ef84-3272-9409-991561092580 | -10.5524 | -69.15009 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d77e7d5-1a8a-316d-b9a2-f4c0c68301b0 | -10.55294 | -69.15131 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f04dac28-1de3-3aab-bb3f-ec430e60e909 | -10.55775 | -69.24342 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 581bd449-7c55-3aab-ba94-8af0e519ba4f | -10.55796 | -69.1507 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3831da7b-4104-3faa-b1f8-adf59a5981ee | -10.5585 | -69.15192 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8455225-4ebe-3d3f-9081-11aa37a9e658 | -10.56326 | -69.24422 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a6a8105-860a-3931-8ead-fa8256113507 | -10.56499 | -69.18503 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eb6b484-7946-38a0-a330-c026824be18c | -10.56544 | -69.18137 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870b6569-1532-3f33-82a4-5497dc1aec4e | -10.56595 | -69.44426 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccc3fb38-ec31-31ec-80a9-d4e75afdb219 | -10.56641 | -69.4407 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34704b24-8849-35e2-9dea-123244fa933f | -10.57229 | -69.43797 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b9a3102-545a-3d1c-afc6-b73be8b2ed0a | -10.57772 | -69.43878 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 432331ad-3241-3735-84f3-d1df25015b54 | -10.62192 | -68.7224 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dedf534a-8571-3c52-a7ff-df00569689b3 | -10.62667 | -68.731 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea4a1ad9-4b23-3628-addb-2ff4a130be15 | -10.63239 | -68.73164 | 2024-10-03 06:33:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3c1266a-2809-3a0a-b044-56ebd7ca5514 | -10.63818 | -69.05256 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5db33492-5ee7-3990-bdab-5125c57dba3e | -10.65135 | -69.648 | 2024-10-03 06:33:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11a0c72f-32a2-35c0-8b48-6b23fda27549 | -10.65672 | -69.64878 | 2024-10-03 06:33:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a39151ec-6d8d-39c2-bcf2-6503d480793a | -10.66746 | -69.30122 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91113080-dbca-3fc8-92a7-a1e46c56caf2 | -10.69505 | -69.39201 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cddf029c-d3b5-397f-b757-92795520b2bd | -10.6955 | -69.3885 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92effce2-f003-3930-b49e-3bcc993be7c0 | -10.70051 | -69.39281 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1037d50b-7b93-34b5-8de9-72849b784d55 | -10.70096 | -69.38933 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44ef5c13-c9ab-3cff-9f6d-268a03ccbb0a | -10.70142 | -69.38577 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1df42dd-58ca-3fb7-a9a1-67148a5f1efb | -10.70688 | -69.38657 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd5daa39-8fb2-3852-9b26-dcf4cad5093a | -10.72157 | -69.31557 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49cbe953-d3be-3fff-9d34-f1ad7399f532 | -10.72203 | -69.31203 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1d41fcf-f970-3d38-8de6-2f4f62d3c519 | -10.73661 | -69.10969 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b431816f-d814-39b0-b079-7711a2469939 | -10.82421 | -69.60262 | 2024-10-03 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2592686c-2ec1-3117-a29b-145a387dc18a | -11.68483 | -64.98682 | 2024-10-03 06:33:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 60e61664-cbaa-32a6-b0f0-db4d10e8d81f | -11.68647 | -64.9886 | 2024-10-03 06:33:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4c2b7504-0031-3819-a938-37d3b907ad95 | -11.69213 | -64.98736 | 2024-10-03 06:33:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37f21f87-6665-3d92-b5de-976a702b3057 | -9.0515 | -67.871 | 2024-10-03 06:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 51062a07-112b-3c0d-b93d-4882b393d3d5 | -11.6932 | -64.9785 | 2024-10-03 06:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e4817d48-fbd8-32c9-8ede-fac832aea76e | -12.4037 | -63.0201 | 2024-10-03 06:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| dd0f37d3-5427-33bf-93d6-da6daba22125 | -12.4038 | -63.0009 | 2024-10-03 06:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 409.9 |
| 55e72561-e9fb-3511-9c28-3e55e80d3935 | -12.404 | -62.9817 | 2024-10-03 06:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 204.4 |
| b007dcd2-05b6-32ec-88d4-5ead8c8c8bee | -12.4227 | -62.9999 | 2024-10-03 06:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 279.9 |
| 1b6525d2-e981-3713-83d0-91bf112f013f | -12.4228 | -62.9807 | 2024-10-03 06:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 3da1cfbe-7cc1-3186-9d9c-c803289615b5 | -16.6688 | -57.374 | 2024-10-03 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 5f187501-99ba-3339-9199-90fdd4344cdb | -16.6893 | -57.3104 | 2024-10-03 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 6cb25987-c81e-3eaf-849b-bc9a1631a5a0 | -17.8403 | -57.7076 | 2024-10-03 06:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 5ade519f-cb2c-34d2-bdd6-0340cda939cb | -12.4038 | -63.0009 | 2024-10-03 06:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 158.5 |
| a07b3ec8-ff9f-347f-9bd6-ea39b95b03bc | -12.404 | -62.9817 | 2024-10-03 06:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 0ecea990-0947-32da-a771-95da3bed32b6 | -12.4227 | -62.9999 | 2024-10-03 06:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 239.9 |
| a17ffb0f-973f-3bdb-8ca3-0be1de3db6c1 | -12.4228 | -62.9807 | 2024-10-03 06:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 02208672-3e3d-3dcd-bc97-629b75db3fa2 | -17.0892 | -56.7709 | 2024-10-03 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 556d8130-a3c3-3796-906a-1a3b4a36a12a | -17.0499 | -56.7757 | 2024-10-03 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| e714eb29-44bc-3592-8f39-5080279391fd | -17.0502 | -56.7551 | 2024-10-03 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| ec880859-44ca-38d1-9c01-a8470f1fb88c | -17.0692 | -56.7939 | 2024-10-03 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 70861683-6d2b-3461-b23d-e8733d271198 | -17.0695 | -56.7733 | 2024-10-03 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| f310eb42-82e6-3879-b5f6-8c20efbd57f1 | -17.0888 | -56.7915 | 2024-10-03 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 448bc22a-3ebc-3010-a1ad-b20a08cfcebf | -9.0515 | -67.871 | 2024-10-03 06:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 12276d5c-83a1-3504-a2af-5fa71ed1c57b | -12.4038 | -63.0009 | 2024-10-03 06:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 230.9 |
| 51c3205a-5b5c-3384-bda4-62d4698d801b | -12.404 | -62.9817 | 2024-10-03 06:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.1 |
| ace80e7f-6e83-34bd-878a-b3ace158e2eb | -12.4227 | -62.9999 | 2024-10-03 06:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 223ee7c5-2239-3e14-8df4-5c7d548b9f1a | -12.4228 | -62.9807 | 2024-10-03 06:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 260a0d11-1dc5-3774-b912-c060e0e94b36 | -16.8039 | -57.4811 | 2024-10-03 06:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| e060e080-f9f9-31c3-8b8b-def7785c20c2 | -17.0695 | -56.7733 | 2024-10-03 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 016dae1c-ac70-3253-86da-a2f69d357d0d | -17.0499 | -56.7757 | 2024-10-03 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 305c5f2e-f67c-3e0b-8e29-2eb60cd93765 | -17.0502 | -56.7551 | 2024-10-03 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| ddb3e4eb-90d1-3565-b395-c645f63d9902 | -17.0692 | -56.7939 | 2024-10-03 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| d849ccdc-95a1-30e3-94d1-9c819519da43 | -8.87679 | -70.84906 | 2024-10-03 06:57:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfb407f4-a598-32c8-900f-4ec2682d42a3 | -8.87596 | -70.85599 | 2024-10-03 06:57:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2319faa4-5121-3e00-9d9b-0540c21aac5e | -7.21863 | -72.31632 | 2024-10-03 06:57:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e77bfc93-3cb1-3ea1-8c8f-1369f480d05e | -7.21793 | -72.32168 | 2024-10-03 06:57:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03761806-b3bb-3f7e-844c-a261d5e6a500 | -7.21765 | -72.32022 | 2024-10-03 06:57:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 095b683b-6c20-3504-891d-a5a47e2499b2 | -3.4 | -42.27 | 2024-10-03 07:05:07 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4fe19ea-0a1d-3359-bfbb-5c4d4718b93d | -3.43 | -42.27 | 2024-10-03 07:05:07 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 660c8758-0ed4-302b-bdc5-2297a6d0ae4b | -9.0515 | -67.871 | 2024-10-03 07:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 91a63e0c-093c-3d7c-b493-1df767d79f05 | -12.4228 | -62.9807 | 2024-10-03 07:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 138.9 |
| a17570d3-c832-34b2-8a05-f26a118f38dc | -12.4227 | -62.9999 | 2024-10-03 07:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 347.0 |
| c9a45e93-d788-3486-ac78-034ff2ae9f84 | -12.404 | -62.9817 | 2024-10-03 07:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 68c8152c-f15c-3e32-83df-80aeeb721865 | -12.4038 | -63.0009 | 2024-10-03 07:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 397.4 |
| ece0ccf9-7907-3aee-9cdf-98db85c137b9 | -12.4037 | -63.0201 | 2024-10-03 07:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 5874c878-d13d-3fbc-8c3b-c9dc8bc04a9f | -12.9741 | -62.6409 | 2024-10-03 07:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| a1673fd2-1da7-3413-8de7-1fea7efe1ad2 | -16.1098 | -50.427 | 2024-10-03 07:06:36 | GOES-16 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| dcfa4e0b-e72b-3754-a1e9-7f1937fdcffe | -16.5515 | -57.3874 | 2024-10-03 07:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 0fdaeaa9-bbce-359c-acdd-98638ea2a88d | -16.5512 | -57.4078 | 2024-10-03 07:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 426135a7-942f-3d60-93dd-eb0d74d0912b | -16.6688 | -57.374 | 2024-10-03 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| fcb6aae7-d789-313b-88c9-61b0df553b7d | -16.6492 | -57.3763 | 2024-10-03 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| faa09685-f6e6-3bba-87ba-ebaf4320d3f0 | -16.6489 | -57.3967 | 2024-10-03 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 0878b5ee-e234-368d-936f-33d4379f39bd | -16.6127 | -57.217 | 2024-10-03 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| c5682362-46f2-332e-82d1-6c6d5aa54688 | -16.5931 | -57.2192 | 2024-10-03 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 4b8f0947-dbed-3e5d-a08d-6f2d846000fd | -16.5707 | -57.4056 | 2024-10-03 07:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| a899ef06-35b8-39f0-92ea-1027c255dd60 | -17.1085 | -56.7892 | 2024-10-03 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.2 |
| 5a1cf2c5-56d8-351a-8a85-35bddfb95cf9 | -17.0892 | -56.7709 | 2024-10-03 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| cdffbf3c-5d04-3a77-8134-b281c88b1f31 | -17.0888 | -56.7915 | 2024-10-03 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 68495fdd-1efc-3ca6-8542-26ded6d857d0 | -17.1088 | -56.7685 | 2024-10-03 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| ef023eb9-3c55-367a-a6ba-fe91e243aacb | -10.50837 | -68.66918 | 2024-10-03 07:07:00 | AQUA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 72b3d615-8ecb-339a-87f5-095f7d6210ff | -10.5138 | -69.22936 | 2024-10-03 07:07:00 | AQUA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ca7c4fab-e097-3c48-8b64-755dcee94c9f | -7.37579 | -68.01575 | 2024-10-03 07:07:00 | AQUA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a5714457-b593-38c9-98fb-e34c1be60aef | -7.4275 | -72.72786 | 2024-10-03 07:07:00 | AQUA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c36806bc-ca90-3578-8203-c0e242fdc9db | -7.42882 | -72.71898 | 2024-10-03 07:07:00 | AQUA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 365fe6b6-861e-3364-92fd-4685c3394c33 | -7.63285 | -67.2034 | 2024-10-03 07:07:00 | AQUA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 3cae7416-e66b-3d67-84b9-a961b02766d2 | -8.7568 | -67.70129 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a29ed528-ee16-32b4-b07b-47f162c1fe37 | -8.7688 | -67.70293 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 831f3280-c028-3a3f-9c72-8f265e2da31c | -9.38292 | -68.33417 | 2024-10-03 07:07:00 | AQUA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ae70a114-2fb9-3869-8d67-4a7fbd3d3d58 | -9.28281 | -67.83553 | 2024-10-03 07:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |


[Clique aqui para ver as próximas entradas](README204.md)
