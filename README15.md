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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 854a0022-036e-3559-a414-248ed02cd9b2 | -11.86194 | -58.70953 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3776fdb8-8975-35ed-9a34-f84abbf10b88 | -11.72264 | -47.47199 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c394ad6-9bf6-39f9-8d4d-88f549405ac5 | -10.31765 | -67.3484 | 2025-07-12 05:08:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbe9f2d2-109f-3b0f-bd67-60aaefaf5089 | -10.57495 | -49.12218 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 6a6874c1-1c1a-3b48-b658-a8629845b27e | -13.02035 | -47.8222 | 2025-07-12 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b536e80e-a4ef-3ddc-9777-0d7484dbccda | -12.60872 | -48.3668 | 2025-07-12 05:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c71f5c4-9ef0-38d2-b753-cc7607933ca3 | -10.84445 | -49.10807 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 47c4799b-7696-399b-a3ca-49d1b81bb538 | -12.10734 | -44.97489 | 2025-07-12 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5d2c510-53f0-363c-afce-af1be36ea45d | -13.1476 | -47.31353 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0257c8f-282b-35eb-ab21-062659573500 | -10.35347 | -49.9205 | 2025-07-12 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae8a5cef-6127-3735-81c3-235d8459ee11 | -11.93522 | -51.68655 | 2025-07-12 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cef172e7-6011-3d30-a420-10bcd27f9b82 | -14.85997 | -59.50711 | 2025-07-12 05:08:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1ce3fac-19c3-37a3-a70c-873addf66e78 | -13.65036 | -53.93791 | 2025-07-12 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9df72d56-8fb4-3d4b-87a4-052214cdd269 | -11.73387 | -47.4726 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44f53977-4310-3d9c-974a-b6ea8c1b050f | -13.13268 | -47.31446 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c066edb6-7dfd-3719-925e-04985f7664ab | -12.41202 | -45.35007 | 2025-07-12 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7023e7a3-714e-3b40-bfaf-58428b7a9c70 | -10.22043 | -55.45341 | 2025-07-12 05:08:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2d25dba-82b2-37a5-9068-c46cde848390 | -15.10272 | -56.23032 | 2025-07-12 05:08:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1878fcaa-32a2-3c4f-a2ad-d417576f0776 | -9.01668 | -61.2195 | 2025-07-12 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c8f77c-e0a1-340e-903d-8a14cca73ad9 | -9.65312 | -62.91706 | 2025-07-12 05:08:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77f89a06-6b80-318b-9568-d37f4d92d537 | -9.02291 | -61.23119 | 2025-07-12 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14090130-85a5-35ac-a99e-e30e567bb5d0 | -11.44151 | -45.10503 | 2025-07-12 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56cc5a9b-aef7-3a09-bd8e-a4a3eebdee93 | -13.14444 | -47.31177 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e4bac4e-1a7c-336b-ae05-eff582ecd05e | -15.68462 | -48.2719 | 2025-07-12 05:08:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08b925cf-0f76-39a3-87d3-39ad06824bb4 | -8.80128 | -67.27429 | 2025-07-12 05:08:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da199d76-0439-3b01-bb93-7e2dfda3b3de | -12.11315 | -44.98108 | 2025-07-12 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d30c7b2-250b-3923-9e13-5bf437456c14 | -9.02776 | -61.2267 | 2025-07-12 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08dee7b7-0997-3a15-a8b1-768ef503b127 | -11.93471 | -51.69032 | 2025-07-12 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b95dac51-e904-382d-a3df-eccf2358004e | -10.86309 | -49.11592 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9ce7d68-467b-309b-af10-18cd3dce4267 | -13.15418 | -47.30601 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db01c64f-105d-31f8-aa17-8bdd72a7b641 | -10.83962 | -49.10741 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb687396-9916-355a-a2d6-8a415792d570 | -11.73431 | -47.46893 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 202044b8-cd54-3b59-81b3-ca15c2c08659 | -10.84857 | -49.11407 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0f1e9ef3-9bc0-3411-ae0b-33c94cab23d2 | -12.41603 | -43.4899 | 2025-07-12 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3b71b80-8a43-3090-a1d3-18faddaaafb5 | -8.64575 | -64.17092 | 2025-07-12 05:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba68dbd3-9e21-34e3-b841-2c848b3ec1f0 | -13.12705 | -47.31376 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e7b735e-fddc-3cdb-aca7-dc60de725d7e | -10.84375 | -49.11335 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b69216af-c9f2-35a0-8d97-228ba9451789 | -11.73402 | -47.46993 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcee3ce0-f121-370b-b315-e246b93cf8d4 | -10.67498 | -49.5012 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdfed212-d519-39a0-9594-10966d8e16d5 | -11.87897 | -58.71235 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebf12519-49d7-3147-b311-69b35d6a9466 | -13.13578 | -47.31694 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99aaf128-c203-3c52-92bc-3aede47f1b47 | -11.60378 | -47.61149 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 506c30a5-578d-3a22-b4a6-6e87924f13f4 | -15.05925 | -47.59947 | 2025-07-12 05:08:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4803b52a-c653-38aa-bac7-f346dec31b9d | -11.93156 | -51.69364 | 2025-07-12 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8f629a5-efae-3580-9223-a5af2d6757f3 | -11.86596 | -58.70638 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 659783d3-68d7-3f1d-8ed9-ac840ee8fad1 | -13.13304 | -47.31144 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09626a4c-5733-387d-b8f5-467c42a2acd2 | -11.32667 | -51.44171 | 2025-07-12 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5696638-d9b9-3a69-87ce-66107a97c94c | -11.8367 | -47.50276 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2426da4f-8884-3bf4-b5d9-02728c9bd9e8 | -10.13503 | -57.78252 | 2025-07-12 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e37ccefe-23c7-3e6f-adc2-a4a894af8ec8 | -11.73748 | -48.52697 | 2025-07-12 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d60e715d-e115-3188-b443-4cb07ef0d9b8 | -13.12138 | -47.3134 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d462f83-bd3e-3a80-91b2-f512a065ca7b | -13.20581 | -47.25673 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6437c236-aafb-3bef-9ee6-1f861ccb4c6e | -10.6758 | -56.54857 | 2025-07-12 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3554ac52-d08b-35f1-a287-9eb96db1438e | -11.73493 | -47.46279 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c81b14b9-0ef2-3f3f-bc13-b76dad166c99 | -11.4669 | -45.10787 | 2025-07-12 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f78fe39a-9803-35fc-98f4-c2f9eb4cb079 | -11.87495 | -58.7155 | 2025-07-12 05:08:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fcc34d8-6c64-315d-9e1b-056dbe7e656f | -13.65772 | -53.93904 | 2025-07-12 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e5ec4f9-13c3-3600-8943-141b456fd167 | -16.66511 | -50.63022 | 2025-07-12 05:08:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d20c4459-75cd-3820-8185-1c946a004ce5 | -9.64851 | -65.74139 | 2025-07-12 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e7627d4-8af9-37db-aa5e-b1f4b32d1292 | -12.58026 | -56.98123 | 2025-07-12 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df1800b0-4b42-3ca6-ac4e-fd667d224839 | -10.89366 | -49.20764 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ef373d41-e927-3ed2-a084-29f018299408 | -9.65388 | -62.91278 | 2025-07-12 05:08:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a9c6a3a-1da6-3687-9846-93cf1fe16478 | -13.6614 | -53.9396 | 2025-07-12 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff491874-5258-3b8c-82fd-fbfe4e3f0473 | -9.02378 | -61.22601 | 2025-07-12 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea2eae83-4bce-3a9a-9069-ca9db484e78f | -10.04589 | -59.11307 | 2025-07-12 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f573eb9-e1bd-300a-90c0-6995c6f85bbc | -13.1534 | -47.31276 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dff9646-ebab-3b53-9cac-226379687916 | -12.06512 | -63.22325 | 2025-07-12 05:08:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98ee8361-e48d-3591-8aee-1c4770eabdb2 | -10.70058 | -48.30646 | 2025-07-12 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 133890a3-edc7-3296-9e83-82d65c356ccd | -11.94124 | -49.29971 | 2025-07-12 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2c32d22c-5cd2-3d49-8fa6-7a0a8f8787b5 | -13.12666 | -47.31692 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2af3d853-6f2c-39e1-b208-6d65f0776796 | -9.64318 | -65.74039 | 2025-07-12 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4662142f-eab4-3e06-b16e-8d9ffeeb7b04 | -11.42446 | -46.37841 | 2025-07-12 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e492d8d6-62a6-3dcf-b2a7-bcde4f8a1cc9 | -11.72993 | -47.45841 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a41e825-32c3-333f-af52-d0ed50a94eb3 | -11.72946 | -47.46204 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 842b5837-034a-3124-bcc7-b17617a62394 | -13.65592 | -53.94103 | 2025-07-12 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fb7b398-a943-332e-8a90-b6e2a321fea0 | -13.11683 | -47.30379 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 599c21ad-1988-3567-ac9c-80f6fc20fa2d | -13.13651 | -47.31067 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c55e814-01a6-301d-9ac1-d0ed38314af0 | -15.57016 | -47.85681 | 2025-07-12 05:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 773434a7-5af8-3260-a6be-c056b1a268ab | -13.15024 | -47.31107 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb2a9bcf-2da6-3f2c-a6c4-d16ec0cd8025 | -12.10668 | -44.98063 | 2025-07-12 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c4da48c-0646-375b-8721-bdc98caa8a66 | -16.66557 | -50.63137 | 2025-07-12 05:08:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 507d2880-c077-3237-948d-e3a10c246368 | -11.72855 | -47.46918 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58ce0345-1132-3fae-988c-f05581a832f8 | -15.06491 | -47.60018 | 2025-07-12 05:08:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9c5203d-d556-36d6-a578-eb1e6be69b6a | -11.94946 | -49.29632 | 2025-07-12 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab679eaf-0d7c-3132-a3e6-11f068a99d0f | -17.33019 | -44.90137 | 2025-07-12 05:08:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50fd13f9-0d4f-3ba2-9d0a-91261d66076d | -11.94196 | -49.29435 | 2025-07-12 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 74579b58-8ae2-3d87-9906-4b226c96432d | -10.85412 | -49.10943 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 11ad6c63-a664-3a7a-8e07-7196c71f5a64 | -10.89913 | -49.20313 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7c2f2e7e-3140-3968-a19c-5325d1d2cb9d | -13.16651 | -47.29839 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3becddf8-e96b-39cb-965b-28003719c714 | -12.42012 | -43.48835 | 2025-07-12 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8e631b9-0e04-314d-af65-93615ac0d477 | -11.7297 | -47.46101 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 051d49c3-c0e7-32b0-8a6f-15a075fc59f0 | -13.64669 | -53.93731 | 2025-07-12 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd56a061-26e2-3a6c-95c9-b3ed5e80f53c | -13.11642 | -47.30713 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7afe256d-21c0-32b3-8807-76064210881a | -10.04607 | -59.11194 | 2025-07-12 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c34e9a0f-9409-352f-b443-f925c7c5f6cb | -10.84929 | -49.10874 | 2025-07-12 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9a06ca7b-17ff-3016-a807-7f5ac06d7176 | -11.84103 | -47.50425 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b76872d2-07e2-32f2-9586-dc22fa855436 | -10.67094 | -49.49565 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f89c5ba-48bc-35d7-ada3-c9ddf806753e | -13.14981 | -47.31453 | 2025-07-12 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e412b81-4dfe-3b2e-9462-f01866091cd7 | -10.57084 | -49.11613 | 2025-07-12 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eeee8b8e-5a50-309c-8be8-7d5f972319b5 | -11.7284 | -47.47184 | 2025-07-12 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README16.md)
