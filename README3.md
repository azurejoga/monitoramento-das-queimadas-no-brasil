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
| 0c912b26-5b02-38f7-81ba-d8757232f1b5 | -9.3802 | -47.09104 | 2026-07-22 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f49a9b05-4fda-3d68-8077-a17cb9d70c72 | -7.01373 | -45.8511 | 2026-07-22 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b755ac0f-5799-32be-bac4-816789afb944 | -7.00551 | -45.4271 | 2026-07-22 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d077b538-79de-3a40-a89d-7efae90a8f2c | -5.75097 | -43.26805 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0f16c9e-7fe7-3c7d-b91b-d818fe2f6211 | -6.04812 | -43.87215 | 2026-07-22 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77c20ec9-1c38-3dfc-82f8-ade84ef24437 | -5.98453 | -47.0685 | 2026-07-22 04:08:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79553fa1-2b00-30ca-8107-9e9277b23a21 | -8.11571 | -44.8237 | 2026-07-22 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e520eb3c-0e50-3478-bac9-aed7722e123c | -3.73076 | -49.27302 | 2026-07-22 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a88e8f5-bdbd-3abb-91f1-ba1c908afdf9 | -5.79951 | -43.73135 | 2026-07-22 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e59374c-d829-37c8-8cdb-875ad88a948b | -8.7374 | -49.44348 | 2026-07-22 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43621499-e2ec-3656-b4fd-16f7faf1f268 | -10.35649 | -44.75119 | 2026-07-22 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ad4506a-8153-3f15-ae63-a215c2237620 | -8.75555 | -49.08122 | 2026-07-22 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec46b99b-aed1-33a9-bcaf-5f9e5b66284a | -5.55431 | -45.18226 | 2026-07-22 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e90bfc0-40d6-325c-ad4e-5835a4679177 | -7.49036 | -47.59927 | 2026-07-22 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1df488e5-b849-38d4-b48e-6ddd30ca0208 | -6.56759 | -51.69717 | 2026-07-22 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b2fc0aa-9958-35b4-8c97-77f5c2a44c90 | -9.90463 | -47.8784 | 2026-07-22 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d446ceaa-7ff0-3227-8fc9-41712fcd249a | -9.01133 | -40.99147 | 2026-07-22 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b5ec7e8-f5d4-3e30-b804-2eaa5a09ec0c | -9.01467 | -40.99199 | 2026-07-22 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 370dfb9a-f5ed-36ce-b2d4-47a51bca25e0 | -9.64146 | -47.80965 | 2026-07-22 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf6dd311-f204-3af5-b785-ab5ea64a5013 | -5.74756 | -43.26749 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a71c2072-15ae-3970-8a21-e28e8b5720c0 | -7.90817 | -48.28021 | 2026-07-22 04:08:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaed3360-e624-35cb-ac66-fe8fdb298ddc | -8.49098 | -54.77497 | 2026-07-22 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cdcd5541-8e21-32bb-8681-98d1fa6310b0 | -7.17969 | -41.40403 | 2026-07-22 04:08:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9e6205ab-818f-3e05-b205-d45563e7de3b | -5.67774 | -43.57555 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1147b6c1-e500-3bf4-97c3-17fdaf1a6653 | -8.74636 | -49.07975 | 2026-07-22 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d542ae45-de88-3ff6-803c-4bb72875f845 | -8.75179 | -49.07575 | 2026-07-22 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9d813552-af39-30f5-8757-c329d0bba181 | -4.70371 | -40.8099 | 2026-07-22 04:08:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc12347d-754b-3f60-8988-f7befc10080c | -6.8685 | -40.79987 | 2026-07-22 04:08:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c5190cc-b227-3a96-99f6-12cd8088d65f | -3.63678 | -49.70684 | 2026-07-22 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a5d7408-22d5-35a6-8596-25326c2d98a0 | -6.15453 | -47.11944 | 2026-07-22 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9eaaf0f-43f9-3b04-a0de-6544cea450aa | -5.67428 | -43.57501 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4a7e6eb8-8d75-3688-ba40-5133d862f0c1 | -5.74298 | -43.27436 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 824fcf0b-82a3-3307-8939-b15ddc46c5b3 | -3.52721 | -49.26064 | 2026-07-22 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e114142c-3dbd-36e4-a3bb-a66bea7f48d7 | -5.55301 | -45.18317 | 2026-07-22 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d4ae184-f653-31db-9276-864fe88ac8b7 | -5.67083 | -43.57447 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6887c467-62aa-3fd2-bc73-a71e064c896e | -8.81167 | -39.99798 | 2026-07-22 04:08:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 84607d02-200c-3af1-822c-38bb3e89bd07 | -8.75472 | -49.08598 | 2026-07-22 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47109db6-7491-3c57-8dbb-7227337fcb5f | -7.19649 | -45.4964 | 2026-07-22 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b916fee-28e6-3b61-98be-0f72ab4f2ffe | -9.18937 | -41.02584 | 2026-07-22 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4dd8aed5-09a3-36fb-84e7-f41cd354f877 | -7.0085 | -45.43222 | 2026-07-22 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a6e41652-eee9-3b53-bcd5-0d5930c7562e | -3.98676 | -48.3852 | 2026-07-22 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ddc8adea-fa8a-3b9d-a353-b28a0d5256ae | -6.15518 | -47.11557 | 2026-07-22 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab96c6cb-d39a-3682-a3db-e8cc15f9ccda | -6.04401 | -43.87548 | 2026-07-22 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5a996e77-7762-3dc9-b320-a57309b999b2 | -7.00179 | -45.42648 | 2026-07-22 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b712208f-8ce3-3758-b429-87e126011954 | -6.20457 | -43.29008 | 2026-07-22 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61ea7c70-78ec-350f-8a68-c401f371433d | -9.69793 | -47.70258 | 2026-07-22 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a6ab94d-95e1-379d-9014-afcbb2f347ec | -5.73957 | -43.27382 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3fa2ffb-50b1-3613-a0c7-efdb5d15552d | -5.63618 | -47.10209 | 2026-07-22 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9546e1b5-f561-3fea-9e68-6a42d509ae81 | -5.6368 | -47.09833 | 2026-07-22 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2217515-974e-334b-a25f-4ce1102089ec | -5.67143 | -43.57067 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4bae4ec4-10d9-3197-97be-5a0ccfa1b49b | -7.83667 | -47.10949 | 2026-07-22 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 627b35e5-3ee5-3a8c-a6e4-4c5b6ec8d745 | -5.75152 | -43.26771 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12ad8a79-6144-35cd-b651-00a176117f81 | -7.00923 | -45.42773 | 2026-07-22 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b6ad7635-bfe4-3833-a393-b7812b4fd6ed | -2.1573 | -53.65453 | 2026-07-22 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b48661bc-7313-3a14-8c13-7cb57cef0390 | -10.30481 | -40.72339 | 2026-07-22 04:08:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7d15bf3-a934-3ded-991f-17876d6d79df | -9.22718 | -48.55673 | 2026-07-22 04:08:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 978d2f83-b209-3d8c-86dd-a1fa8caea055 | -3.52672 | -49.2636 | 2026-07-22 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ed603e-a7e2-36a1-9ae7-3d737d256545 | -9.20648 | -49.82371 | 2026-07-22 04:08:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c80f765-406d-33ed-bb28-033fa5e3c740 | -9.70206 | -47.70321 | 2026-07-22 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6eceb0a-7079-362a-b8ff-d74db1324095 | -7.8057 | -47.11913 | 2026-07-22 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83c37af0-1327-3dad-bc6c-17807f0cead2 | -9.69856 | -47.69884 | 2026-07-22 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2827ac62-9957-3b3b-ad16-63703bf8f639 | -5.66797 | -43.57014 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6b52d81-023e-3b48-b098-31c9345703e7 | -6.0475 | -43.87603 | 2026-07-22 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8dd5f3a3-7f7e-3dd8-b5ae-d41ec559db8f | -5.74698 | -43.27119 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 712bdead-db71-3f6c-aeec-aadbd2e7d34d | -6.0516 | -43.87271 | 2026-07-22 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9e48ea0-f462-395f-b5da-62a5aeafbd4a | -6.56689 | -51.70109 | 2026-07-22 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc6b2f90-0c5b-3566-b344-e2f14aaefcb2 | -9.46744 | -45.65488 | 2026-07-22 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22c587f1-9481-3856-b199-0bdbcd22f904 | -7.88789 | -46.90688 | 2026-07-22 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bf3ac33-0fa1-3c11-a13e-28c0194bcc73 | -9.22699 | -48.55938 | 2026-07-22 04:08:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cbcf830f-6abd-3614-81bb-cfd3ac3e521c | -8.52443 | -39.3493 | 2026-07-22 04:08:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| afb47eb0-2a09-3b38-8f05-9f508358c235 | -3.63633 | -49.7095 | 2026-07-22 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6f9c92d-e9f3-3f12-b92e-468996b64e65 | -9.70075 | -47.70267 | 2026-07-22 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8ff8fdd-0705-3eee-a234-68a769a5a087 | -8.76014 | -49.08197 | 2026-07-22 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b754cf3c-e382-3972-b281-67303e7d1437 | -17.5748 | -47.4996 | 2026-07-22 04:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c5db8465-0828-3464-a3be-1a5a3e257c6b | -17.5947 | -47.4956 | 2026-07-22 04:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 6b51a339-253e-3038-b957-80981137ec10 | -17.57747 | -47.51657 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b8bdb685-f7bd-33ed-8259-cf567dc57729 | -13.56838 | -43.6171 | 2026-07-22 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d97d2d61-bb8f-354b-9263-af16f3c3a4f1 | -17.5771 | -47.50126 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fdbadb3b-2f4d-32f9-b7d1-a74261a9f6f0 | -12.69157 | -45.32266 | 2026-07-22 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53c3661b-10cf-30e1-9091-a6bb99939e11 | -11.89076 | -43.82981 | 2026-07-22 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b8eead88-bc4c-367f-8c12-0438277df39f | -17.58184 | -47.51279 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c8778917-a518-33ea-9f11-5eca38d9ff1d | -12.51921 | -48.25373 | 2026-07-22 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08d24e67-584d-35c5-bf62-5f9f0eaf5eb0 | -11.91574 | -43.84493 | 2026-07-22 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9612f2cc-ff94-3938-b1d3-55fdd01a5a1c | -15.24226 | -48.57011 | 2026-07-22 04:10:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8f2b24e-28e0-3a96-9f58-e754f59f4c83 | -10.66787 | -49.56101 | 2026-07-22 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e12d781a-c076-359e-aae2-f7b07e771424 | -12.52392 | -48.25082 | 2026-07-22 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47c5c332-e4d2-339a-be17-4c39be600bc2 | -17.57461 | -47.51141 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d0304c59-b18e-3318-96f1-296f12ac2ecb | -17.57633 | -47.50563 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| e1aeab83-577c-3ae8-9b03-e7586ab8e541 | -15.24163 | -48.5736 | 2026-07-22 04:10:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6739c9bd-0757-3a7d-b4de-a61bef729691 | -11.40076 | -47.49023 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 700afbe6-3796-3fdd-906c-5fb8ce1efdf1 | -17.58356 | -47.50702 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a33e012-2ee6-3c8c-87bd-39805ceff1e3 | -12.14068 | -48.26142 | 2026-07-22 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e1a9ed1-cd8e-3b15-9d04-317851288c0d | -11.40295 | -47.50109 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48af695b-aeea-3a07-8282-d4deec929836 | -11.63296 | -48.54492 | 2026-07-22 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91e3d09c-d864-3d1a-b108-7fd69c398bca | -17.56888 | -47.50126 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d64cb01-e689-3b4f-9c8a-29537496c5ba | -12.32089 | -53.27691 | 2026-07-22 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 742296bb-bb60-3e31-8cd2-e27513c4df04 | -11.37326 | -47.48464 | 2026-07-22 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d6521b7-0a01-3c87-a6da-e4d2316b84b5 | -17.58071 | -47.50195 | 2026-07-22 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 42c6f968-f1be-3951-b9a2-f7d5fc2d47d5 | -13.44329 | -43.67616 | 2026-07-22 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63fbaead-b0c3-3156-8de0-2d08cf36725d | -11.63717 | -48.54564 | 2026-07-22 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
