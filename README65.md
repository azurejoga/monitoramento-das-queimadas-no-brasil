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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 531b547b-0425-372f-85fe-5e1609d6a2f0 | -8.49323 | -54.86767 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0c6e513-7bfb-3825-ad0e-6019442c7fcd | -8.56677 | -54.66934 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfd85a16-72a2-33bb-9815-f8a48a9eff40 | -7.34104 | -55.6799 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79be7464-1c3d-3524-a0cd-7bec8c442e90 | -8.66772 | -54.63739 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| f92db8df-b1a4-330a-a393-f22b80114aa2 | -6.80567 | -59.44476 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75302042-519e-3052-9a30-3a27686adbe7 | -8.09958 | -51.66102 | 2026-08-20 05:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 718bde9f-6ef4-3575-bdd2-ad563afacfa2 | -8.6827 | -54.63956 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eb36990-1f0e-32e7-9507-b6905b118122 | -11.20371 | -55.05695 | 2026-08-20 05:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 49607fa7-f52e-3341-b86a-b031460b65b1 | -9.42217 | -60.40726 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c839be63-1ff4-3bc0-a8aa-dc55cff70550 | -6.58064 | -58.98064 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9bda508-9801-3e8a-a95c-764008ea646a | -6.88476 | -59.03887 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5587a1e-f09c-324a-854b-565a479e8ef8 | -9.13525 | -60.61596 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3af394e9-8975-3e81-b8b8-7d2eb98878bb | -8.89667 | -60.54654 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ae1a2a78-6003-3a3f-8e81-f131458b97f2 | -9.42151 | -60.43538 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 430dcb00-afb0-3733-9ef4-822e385c980b | -6.87203 | -59.02558 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 136970bc-2d9d-3419-84ff-87573646552c | -7.44484 | -60.00603 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 101de568-3fe2-3412-a66b-60a8c66aa82e | -9.41621 | -60.44663 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98c28b9e-20d2-3b1d-8bd1-d53938590581 | -6.71331 | -59.09007 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 636f1cbb-8c99-39ea-b367-62290eb234c0 | -9.74327 | -59.31498 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8eda0bc-494f-3c1b-9e26-441bf3af87b4 | -6.58127 | -58.97638 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c6dc7f8-c529-35db-a435-f71a0e2ae520 | -6.70902 | -59.09379 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18e9f0ef-0532-3ab4-a402-23f9eb1f43bb | -9.02456 | -60.49321 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a01132e9-f5be-3358-bd38-83bed8a5af16 | -6.89013 | -56.44004 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7647ad8-0e78-3ca9-9f14-5f1dabab51ec | -9.10525 | -60.93047 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 50a6657c-d1a5-33c8-868d-b77158cc677e | -8.71694 | -49.61861 | 2026-08-20 05:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e3f76d4b-1486-3873-8b78-dc4df9205d3f | -9.42441 | -61.97926 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef4f7fa8-42fc-3810-aac7-c2d0e29619cd | -8.56572 | -54.67282 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3078069-4828-3d4e-be75-11bfbddce4c4 | -6.70773 | -59.10222 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d9178cc-7ae2-3e25-8ed5-9a3c4a1a7721 | -6.88583 | -56.43942 | 2026-08-20 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 453978e8-dbdc-304b-b2f9-7885db3bf2d1 | -10.39235 | -61.20406 | 2026-08-20 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0faf8c82-6486-371d-8996-800e19af2d9b | -9.42032 | -60.44323 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 168f7fc6-eb19-37fb-ab57-df8760523f7f | -10.77975 | -50.31003 | 2026-08-20 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4b784b2-629d-3edc-b136-8f0744d36913 | -7.60796 | -60.95844 | 2026-08-20 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 928c837a-ab2a-3142-860b-6c964fe52bde | -6.69982 | -59.10535 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cea98b8-615f-36ca-95ce-6175f0bedadc | -6.69019 | -59.09529 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d861f291-4cd3-32d7-8cf1-73ae1ac0ea53 | -7.37576 | -55.53365 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bc22cdb-cf3a-3eed-8d3c-74f3efcfb289 | -11.21014 | -54.00297 | 2026-08-20 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36a61600-85a2-36c4-8748-f46c9929361d | -7.54509 | -55.59037 | 2026-08-20 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8420e032-4475-3fff-98bd-7a8fb104044b | -9.418 | -60.43484 | 2026-08-20 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 37dcbaae-7d4a-3a79-b38c-fc9b68dd2004 | -6.70837 | -59.09802 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86c0a158-915e-370e-b87e-d8073579d520 | -6.71032 | -59.08526 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e616f6f-b20a-3b24-9c9f-6beb178267e5 | -7.44835 | -60.00659 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70097949-8a0c-3138-82e1-57510653792d | -9.12079 | -61.60258 | 2026-08-20 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc53f8c0-4419-3157-ada5-d758cdcb0577 | -8.28499 | -62.89735 | 2026-08-20 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52f144e9-66e0-3a03-8b45-3c39407f8c29 | -8.56911 | -54.72775 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90298092-3929-33af-a876-d3f5ee37e7f9 | -8.66612 | -54.6488 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fabb93de-fd18-3b55-b52e-bf693836f1cb | -6.75614 | -59.46748 | 2026-08-20 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c7f5fb3-01a8-3ff2-8d00-e6280e3fbf2a | -8.67139 | -54.64418 | 2026-08-20 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6cedb2c4-e75a-3b18-b369-da04c1f2bbdc | -9.02332 | -60.49406 | 2026-08-20 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfd8bd86-c3ee-3db6-bd2c-c5a7305e740f | -7.86464 | -63.76057 | 2026-08-20 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f656832-96b8-3587-83fb-f25565f9f036 | -14.08961 | -58.82021 | 2026-08-20 05:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffc98ef5-f08c-3d5e-a214-9ef38365d4e7 | -16.08061 | -54.97292 | 2026-08-20 05:44:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb8589de-c91e-3cb5-83af-1a6e4122382b | -14.09304 | -54.00315 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7c2d643-0ec3-35be-9081-4d414e14c5f4 | -14.09368 | -58.8208 | 2026-08-20 05:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c17801a-818e-3426-ae78-065b0a99e97d | -16.5019 | -55.18454 | 2026-08-20 05:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d0271309-6c0c-3661-a469-581e8f028a29 | -13.40491 | -54.3852 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e9d5f8dc-d6de-3bc6-ba13-9434a3e465c7 | -15.35938 | -52.77709 | 2026-08-20 05:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 803faf52-6de0-303b-9b27-1c14e0dcd1fe | -13.93978 | -53.86921 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 750f3fb4-0df2-3265-8e14-caa0d2a72912 | -15.36457 | -52.78084 | 2026-08-20 05:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9be42762-82d8-31da-8264-6193c766a51f | -15.86825 | -55.55578 | 2026-08-20 05:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26307e1f-af27-3eaf-b9b9-20021e9cce03 | -14.08991 | -54.00491 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06e3b484-6932-31f8-80df-efda65968dd5 | -13.40612 | -54.37481 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c711692-17a4-3988-9ad3-c9812347c111 | -14.09774 | -58.8214 | 2026-08-20 05:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cbdc857-d26d-3117-83db-0a9857820448 | -13.40571 | -54.37831 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8e80f790-8ff2-3dc5-b77e-020dc7a3e5ba | -14.01623 | -53.67355 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aef1b72d-d2ba-3b73-8566-5b3b65e4807b | -14.34541 | -51.89719 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7213b86a-ab76-3a2d-b225-7aa46fe0a285 | -16.50416 | -55.18373 | 2026-08-20 05:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 49541ec5-3097-37a0-83ec-9c59fe839c8a | -13.94024 | -53.86524 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25e0fe29-81da-3b54-b257-e52ef2ad39ee | -14.15189 | -53.05055 | 2026-08-20 05:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0af08f53-9da2-3292-81f1-1cdb4c14699f | -14.31745 | -51.91536 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3fd4344-2d56-3359-8b94-976a3b1794e5 | -13.44553 | -57.07694 | 2026-08-20 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 873950e9-5587-3881-bda1-a265fcb090fd | -14.31715 | -51.91506 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fde024f9-c80a-3119-8b1d-f5fce25feec6 | -14.27452 | -51.88787 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4565e6d5-858a-320c-8fc0-bba9b307d1da | -16.50231 | -55.18108 | 2026-08-20 05:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b0537891-d6d9-3eb8-b379-6185afd4cf6d | -13.4416 | -57.07173 | 2026-08-20 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6dc75f0-8955-33ba-958b-ceda5647a1a1 | -14.08554 | -58.81961 | 2026-08-20 05:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c5f2a018-29ee-31f7-ba0c-ed0feb1f99fd | -13.738 | -51.86843 | 2026-08-20 05:44:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7efa5c1-f6d2-3e34-8f5c-bc5a4094b217 | -13.73743 | -51.87371 | 2026-08-20 05:44:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f06baa52-2064-39f5-8195-5e6bc27b2186 | -13.39988 | -54.38099 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed2a1b86-201b-3b17-a0ea-ae4699721099 | -15.36514 | -52.78161 | 2026-08-20 05:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09ebdb86-1758-374c-aef3-b8a7e1e399a7 | -14.32053 | -51.9481 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b4c1ef6-11b1-353b-8c0b-6e3aa868001c | -14.01666 | -53.66976 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ff497c1-96c4-3efb-8423-8e278f6658ef | -13.43828 | -57.06183 | 2026-08-20 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9798b55-136d-3961-8ce7-a888e6a1341d | -14.23135 | -51.92624 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e380636a-0f68-328d-8680-a00b1a9b3512 | -15.856 | -56.08817 | 2026-08-20 05:44:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b32f9840-128e-3341-a244-465f23775e69 | -14.32385 | -51.91639 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16f71825-edf3-3489-97ab-6344f450b6e6 | -15.36608 | -52.77298 | 2026-08-20 05:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbaf675c-4e54-35c7-9f75-8cc15d0de402 | -14.10181 | -58.82199 | 2026-08-20 05:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44795cc8-eb12-3994-aea0-98f1628b592d | -14.09258 | -54.00694 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdaa4962-ce99-3d23-af80-8cc8bd52d824 | -14.31801 | -51.90999 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a848a780-3488-3ca1-bb48-3cd5c35d1055 | -16.07066 | -54.96406 | 2026-08-20 05:44:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfb5a34d-97c3-318b-ae96-3b2a53993289 | -14.08147 | -58.819 | 2026-08-20 05:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8352fda0-8008-3326-b863-5d86053e1a5f | -14.31774 | -51.9097 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d90948ee-5ea7-330a-b2f5-b5de74aa1dfd | -14.23192 | -51.92091 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 686683fd-0703-3029-93cc-0d86b3b092dd | -13.43315 | -57.06579 | 2026-08-20 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e21049e-6ef8-3d9d-84e5-40147a3aaaa0 | -13.40531 | -54.38177 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ecb1f76-67ec-3fca-92cd-07b12cb9b10b | -13.44613 | -57.07236 | 2026-08-20 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07d3ab2b-cf73-3d8f-9910-2e9f92a5abfa | -14.01581 | -53.67726 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6e822fd-f69d-3500-9eb6-98ff6cafa072 | -14.02094 | -53.67192 | 2026-08-20 05:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ada6236-4424-356e-90c0-a8b323fe05c6 | -14.32355 | -51.91606 | 2026-08-20 05:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README66.md)
