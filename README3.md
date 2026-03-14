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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 764a47ef-3024-3582-a507-dad62961cdb2 | 2.31585 | -60.24282 | 2026-03-14 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87fe3584-256a-32a8-a26c-31eea3dc40d2 | 3.02589 | -60.60673 | 2026-03-14 05:36:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88ce51b5-ab82-31e3-bec8-6e33753bb9b0 | 2.31246 | -60.24331 | 2026-03-14 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce1ba8b1-9d74-3d38-b8b2-c332b57a16a0 | 0.91184 | -60.30205 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df114bdb-63b0-3e47-8d29-0976c1052573 | 0.90785 | -60.2989 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d0f8fa6-66a6-34cd-bbff-77fec1e53729 | 2.31189 | -60.2397 | 2026-03-14 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f80f73a-40e9-3077-b4c7-6fad5c0b652f | 0.91467 | -60.29786 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e55c682-aeb7-3166-b671-43371e551785 | 1.09762 | -59.2738 | 2026-03-14 05:36:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66765b63-eb54-3f7d-9c74-c38aa8682c53 | 1.37242 | -60.37756 | 2026-03-14 05:36:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38186ae7-b9a4-3613-b4b2-f463e35a8485 | 1.08692 | -60.36524 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b62bb393-d9c6-36c4-a3c7-784ff2166f7b | 1.09826 | -59.27782 | 2026-03-14 05:36:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6483650-5e67-3332-a9e0-01b04121af97 | 2.31471 | -60.23565 | 2026-03-14 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5784f677-14a5-366a-985d-847757d00d6a | 2.40168 | -60.23003 | 2026-03-14 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e17691f-b496-321d-b7dd-02f4d2d7e7ee | 0.91409 | -60.29416 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce471bda-97e9-3e90-bd60-7550b5008261 | 0.91068 | -60.29468 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1fae32d-d184-3b4e-8f23-a610b2c0bff3 | 2.31811 | -60.23521 | 2026-03-14 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ac0d336-39a5-3bb6-a69a-c1f080ef0ff9 | 2.31528 | -60.23923 | 2026-03-14 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4cabc6e9-49e6-3467-b0ab-578a13355d1f | 0.90843 | -60.30258 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4383a74a-9c6d-363d-915f-4799b5d5f37d | 1.08294 | -60.36212 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5af04079-6e05-3608-915c-dd621e97985e | -22.03488 | -56.30275 | 2026-03-14 05:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f54912e1-e0d7-3de5-9072-05b33a09680c | -22.03448 | -56.30715 | 2026-03-14 05:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fba61b54-3c13-311b-9033-5cec00d901fc | 0.91107 | -60.29174 | 2026-03-14 07:01:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0c3d5093-ee90-347d-9a5b-d45212ef7872 | 1.08862 | -60.36452 | 2026-03-14 07:01:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d47fa000-883b-3d4e-a1cf-a207fb6cc45f | 2.96408 | -60.62047 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 35.7 |
| b51107d9-209d-3b6b-9f2e-257dfe414232 | 3.0293 | -60.61175 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 865a2439-4b66-37c4-a165-d475dd90e8e8 | 2.99862 | -60.62988 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 1364442c-8e0a-3ad7-afa8-88d680f164ed | 3.02476 | -60.6344 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 527fb904-3e47-348a-b354-88f03a2e17ce | 3.02039 | -60.62699 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 41e60630-d727-37bb-9779-f9560c21a34f | 3.19235 | -60.61935 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 307.4 |
| c75afea7-fe7f-3cca-9b5a-ec260e3a093b | 2.98966 | -60.64516 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 3bd4a68c-1669-333e-8669-079bce6c53f9 | 3.0229 | -60.62057 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 476a9deb-e2c0-3dd5-a1fa-69027b4f35d7 | 3.1904 | -60.6055 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 517.6 |
| 78c0ce2d-fcde-31a8-9fe5-2af3a758eca4 | 3.2013 | -60.60407 | 2026-03-14 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 03a6aa7d-a384-3896-b4d0-eac208d05c96 | -13.18849 | -55.61372 | 2026-03-14 12:49:00 | TERRA_M-T | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0d52d9f3-f9c8-34ad-a4dc-c60aeb960a32 | -12.61728 | -56.8591 | 2026-03-14 12:49:00 | TERRA_M-T | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c6e7aa96-01b5-3623-89d8-0619ecdabe24 | -12.51912 | -56.90456 | 2026-03-14 12:49:00 | TERRA_M-T | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| acacb3f4-3b61-33bc-8c8d-bcd301ddd712 | -20.69978 | -55.12364 | 2026-03-14 12:51:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f660ca5d-5629-3bbd-864e-485ceb42928d | -21.97218 | -57.30578 | 2026-03-14 12:51:00 | TERRA_M-T | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |


