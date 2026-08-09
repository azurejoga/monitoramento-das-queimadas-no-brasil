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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e32347ed-b84d-34c8-9304-f8cdbc2c1e12 | -6.82348 | -56.41811 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bcfb3b2-8dee-3a7f-9add-5dbc505dc85e | -7.55255 | -61.16158 | 2026-08-09 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e6c8229-2adb-374b-81c3-8ddfbdb0a8d6 | -8.63672 | -66.52833 | 2026-08-09 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f55e241-00a2-3157-af11-65a73970d3f2 | -8.64018 | -66.5289 | 2026-08-09 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7d87520-e120-3cee-b508-bb2c26d1cd0c | -6.87106 | -58.92738 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eeb6c71f-1f39-3445-bff8-0e172d30a3f0 | -7.3871 | -59.96961 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e55dc0fd-312f-3048-b57d-d2ae80d8d73e | -6.84494 | -56.40538 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a262f894-0394-3bb5-921c-48492735dd3e | -8.15163 | -55.40433 | 2026-08-09 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96fe4324-df00-365c-a997-5dba96c54e23 | -8.69168 | -62.86955 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2e1399b-60b9-3cc2-b4ea-23ac8b96e4ff | -6.84647 | -56.39485 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50882f25-7a85-399c-9c39-36627e5a350d | -12.35232 | -53.15601 | 2026-08-09 05:48:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5821cff6-fea2-3834-9125-27f1100c0535 | -7.39022 | -59.97485 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 942e4fb4-2dd8-3f47-a3c0-20b76adab5d7 | -6.85052 | -56.40081 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 590f721b-8e6c-3d47-a393-167d5fe39f13 | -6.71005 | -58.95049 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2053cff6-06ae-3bf4-b11f-65e9da2117d9 | -9.33149 | -63.44785 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b2a22b6-68d6-38f3-8058-50dfb4440c15 | -8.87702 | -70.80278 | 2026-08-09 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6689eff0-2d20-35cd-88aa-842274a82359 | -8.67473 | -62.86689 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df6d6040-155c-3469-8304-619feeb211ec | -8.51019 | -63.36005 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c674c249-6cb6-3692-bbe5-5208de5130da | -8.68433 | -62.87214 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5eba13ec-b683-3f4c-955d-a2e98e777a25 | -6.89017 | -59.89297 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c07946b8-2cf9-3081-85ac-9a7c9b85df11 | -6.82049 | -56.43899 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4247b7a-a6ca-3e55-a05d-153e3ba8fb30 | -6.83637 | -56.43074 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a2b4136-a166-3bb0-be2e-4530110afa3f | -8.15253 | -55.3978 | 2026-08-09 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 932d3634-cfed-3246-92da-8e025e6d1ff0 | -9.27168 | -60.89399 | 2026-08-09 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f17d60e5-9832-3ec7-838d-ab08ed84b714 | -8.67812 | -62.86742 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ebabb98-2be4-3301-b8e0-764b3a01b38a | -8.33499 | -64.01971 | 2026-08-09 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11ce2b08-16f1-381e-b92b-f077b6e4991d | -6.83661 | -58.93667 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e55de2a-eb29-3d26-ac95-2aae046ed1aa | -6.85613 | -56.39599 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27f11efd-a192-3493-b808-3725858fb5c0 | -7.39404 | -59.97539 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 073bddec-43e4-3b07-9107-8e7309c117bb | -6.83863 | -56.41513 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fa5f74cc-7041-3e65-ac8f-65aaf9498bf9 | -6.8746 | -58.9315 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eb848bd-a06f-3092-875c-c60ab5e5029f | -6.72144 | -58.92999 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38ed76b4-3219-327e-9969-bf9625bd9c46 | -6.82753 | -56.42407 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c480f577-3c7b-3bab-9bb4-d90704ea52ca | -8.6361 | -66.53214 | 2026-08-09 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e217e953-0054-3b33-a356-55569a87135b | -6.83082 | -56.43524 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2678bf95-79de-3d01-997d-9d7b6ac3d8b7 | -6.88622 | -58.93684 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66b1cfed-12a3-37e1-9b6e-6bf8480985ae | -6.82452 | -56.44499 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee0180ee-0750-3f35-b9c0-175ad539c249 | -7.38781 | -59.96486 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a93cfed1-92f4-350e-836e-38e68ebf3884 | -8.68094 | -62.8716 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c7a40b2-155f-37b3-b6c3-2c40f6ad45d3 | -7.38398 | -59.96429 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cca7f425-35ce-371f-9130-4ce852256df0 | -7.39092 | -59.97015 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2663659d-6a32-3780-87a7-017b89256a18 | -8.15734 | -55.40177 | 2026-08-09 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 437a154b-a5a6-33ac-a35f-51ada5ab6894 | -7.55317 | -61.15751 | 2026-08-09 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8c25d03-7007-35f0-8e4f-a7b0aab2dec9 | -7.03981 | -55.49785 | 2026-08-09 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69fc5ecd-314b-3964-8028-7c3f533df336 | -6.83383 | -56.41434 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c00b30a1-d02a-3a5a-b335-a19648612822 | -8.15208 | -55.40107 | 2026-08-09 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 844fd09f-9324-3ff9-bb3a-f9d87d17913e | -12.32661 | -53.15286 | 2026-08-09 05:48:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb5858de-9a03-3c79-ab14-615a76b54a60 | -6.89195 | -59.90018 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8683ff00-f26b-3336-b4b8-1ffbb981ac5b | -11.10122 | -62.36114 | 2026-08-09 05:48:00 | NPP-375D | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf73fc42-45b9-34b5-932f-3c463fe0b799 | -8.6736 | -62.87418 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed15cb09-c57d-3946-9f2b-e715f013dbd4 | -6.88675 | -58.93326 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f290a8c9-ea34-35ab-ba0e-d216fba34690 | -10.92683 | -57.12056 | 2026-08-09 05:48:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d6219ea5-755c-3dee-bdfe-3d7d32b270dc | -6.83308 | -58.9325 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e7a9230-2dd2-3dad-aa99-0f7976a4de9b | -8.51354 | -63.36058 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39a8de0a-de66-35e7-80f6-23503a8c6e93 | -10.14817 | -69.31851 | 2026-08-09 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e1e63a2-309c-370a-99bb-3c249276c199 | -6.82528 | -56.43974 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b04965b8-ca77-3404-8209-2f7b8c2f1d48 | -10.076 | -60.50001 | 2026-08-09 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 273dbb68-a39f-3e7f-a4a4-50df7dcf2e5e | -8.15147 | -64.09072 | 2026-08-09 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc499744-3588-3e6a-8c6c-aac64ce5a296 | -6.84014 | -58.94082 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61bf6877-8799-321a-9c59-51eb25070858 | -8.68377 | -62.87577 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a353caa-3951-30ce-960c-8cdfadc39948 | -6.88113 | -58.9433 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa55aa66-9ecb-3259-a83f-a51bc362f052 | -9.33429 | -63.45196 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d5b0fd1-a3cc-38b9-8196-21b4558fb2f6 | -6.88165 | -58.9398 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 587f5288-f175-39aa-acef-533d89ae133a | -6.84975 | -56.40609 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 329d6de0-82bc-3554-9092-ebe6e004511a | -6.70898 | -58.95756 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eadc0de2-6261-383a-928f-2c0d63d9b302 | -6.89332 | -59.89083 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15148544-0815-3972-8ecc-8e3935ff4f6b | -10.07984 | -60.50061 | 2026-08-09 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f60e4b5-5729-3192-b9ed-4cffd6259ee4 | -10.92123 | -57.12537 | 2026-08-09 05:48:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1d2aa904-5d9a-35f5-8394-1574ce5ee461 | -6.84091 | -56.3993 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 24c3de69-2dfc-3fff-a4df-59f5d7a6f252 | -6.82199 | -56.42852 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 985f912b-5f24-35ab-a6f4-589c890797cc | -7.03939 | -55.5009 | 2026-08-09 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a92c4d1-ca7d-38e9-b26d-80de20cee8fb | -6.83158 | -56.42999 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e55a9e51-0a2d-3f61-850a-470c84dbdcba | -6.82273 | -56.42331 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b80bf2ad-4388-3f68-951e-75cef9f0c3ee | -6.84595 | -56.43228 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6f177e1-3b1e-3c5c-a89e-6fe64a5cef9e | -8.63264 | -66.53157 | 2026-08-09 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14a904a1-ca93-3c36-bdf4-82ae7b475c1b | -8.78536 | -64.21293 | 2026-08-09 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0df87dbf-8ddb-32ed-9a99-acbae72e547c | -6.72497 | -58.9341 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2e6fc29-4f3a-33f5-aabf-f79fd6aed39b | -6.82827 | -56.41887 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96729ef9-97f8-36f7-8f72-0ac69a9196b3 | -6.82603 | -56.43448 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77044ca6-baf3-3da0-9c72-1f4d8155d097 | -6.87708 | -58.94272 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a768050-7f49-3a39-8216-874ac4c9b73b | -10.9171 | -57.11925 | 2026-08-09 05:48:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85d90635-5bd4-31dd-89f0-b4ae2603b1af | -6.87054 | -58.93093 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1aec3651-9e78-380e-addf-d2a59f6b0c4c | -8.15779 | -55.39853 | 2026-08-09 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adf9be9c-f95a-3524-828f-48e04d6061cb | -6.83561 | -56.43599 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48b7ab22-d6dc-3c2a-9ee4-f30f85503be4 | -8.63548 | -66.53595 | 2026-08-09 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ee452a9-0186-338d-ba2a-20929e2149a1 | -8.67416 | -62.87053 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d91e2cef-d2cf-3c33-aa12-911e1598c436 | -10.92197 | -57.1199 | 2026-08-09 05:48:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d140187-8ab4-3947-b3a5-88e4eb273d23 | -6.85457 | -56.40675 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f0fc825-d2a6-36ba-acfb-265898f574e5 | -6.82678 | -56.42925 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9c9b6e2-5f0c-3954-8439-6b36c3838ed5 | -6.8513 | -56.39542 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4e1fc5f-dd58-3ee8-afd3-a261996ca9a8 | -8.92113 | -64.29889 | 2026-08-09 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 936983c4-ea54-3ac0-bba0-72fa2797c51c | -8.68038 | -62.87524 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d58c2f6c-6ca7-3946-9b30-2072e37862cb | -7.55193 | -61.16567 | 2026-08-09 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b55ed81-ff34-3e04-9762-bf54230690e2 | -8.63956 | -66.53271 | 2026-08-09 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a357005-57c6-30ce-bcae-d98b9af9775f | -10.9261 | -57.12598 | 2026-08-09 05:48:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 992c09b6-bdd0-3b0e-975d-661fb0fa103e | -8.63202 | -66.53538 | 2026-08-09 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac3c43b6-e9e6-3a9e-83a0-71ea3c8269af | -6.89028 | -58.93741 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2407bcd-a399-355f-bd15-09d5074c426f | -8.72431 | -62.88524 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 304d5d48-40b0-37b3-ac8d-ab69a210da91 | -6.83459 | -56.40907 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 381f28f2-51cc-3bad-b646-369d425ef278 | -8.6849 | -62.86849 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
