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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fac48eb3-6aaa-317b-822b-d2abf6983e1d | -14.57536 | -48.0348 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8497df15-6e76-3d23-befd-15d7131a5961 | -22.21143 | -41.77863 | 2025-09-06 03:51:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 51ac2b6f-f42b-36a9-af74-b866dc8c39ac | -20.53493 | -46.47252 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d36b5d2a-a87a-3bf4-8d1b-5a9acced7dbd | -17.71452 | -44.50838 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 782e7962-e700-3507-9059-fd26ef5ddd33 | -14.58741 | -48.08297 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d978fd5c-c8df-3965-b624-aceb8bd65635 | -18.59472 | -43.64433 | 2025-09-06 03:51:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5524b52e-b6b1-3fa4-ab6a-df635699df93 | -21.03946 | -42.92604 | 2025-09-06 03:51:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2bf18b7b-0bcf-3ae2-9bd9-81f6c4b25a63 | -18.08891 | -45.80179 | 2025-09-06 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c395e0dd-ab07-3db4-9387-e16688bb07d4 | -14.1839 | -53.07481 | 2025-09-06 03:51:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3f1dc5bb-024c-3c16-aaa9-30da5b9629c9 | -19.41547 | -44.31588 | 2025-09-06 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d91a6df-85bd-38e7-b205-35c9ee7df57f | -14.75717 | -42.6482 | 2025-09-06 03:51:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56812d24-1cff-359c-8f4a-9ae9b370be73 | -13.85479 | -46.25387 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55c7c731-5f64-36b2-bd4c-575aef26bfdc | -17.06784 | -46.47797 | 2025-09-06 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2945d206-946f-3a37-b26c-a524700e2ff6 | -20.52925 | -46.11126 | 2025-09-06 03:51:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 906d52e8-8c36-358c-9359-a3da843c0a71 | -14.79818 | -48.11654 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5e3a5ec-8c57-387f-8804-e7388f629172 | -14.90246 | -49.45136 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| a2835bd7-1aa8-3ecf-aa0d-eaceef21d823 | -13.73204 | -46.91173 | 2025-09-06 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21b5f1e1-e313-3f5b-9f32-f6cc50df7ff4 | -14.58181 | -48.00189 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2be36ed6-2e6b-32d5-b34e-4f82c44bad5d | -14.1855 | -53.06753 | 2025-09-06 03:51:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f2d81ee0-16df-30b1-ad99-8af3a2b1bcf8 | -14.59067 | -48.0938 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 335db15e-bb71-3aad-91d7-1e5dc9d95467 | -14.89763 | -49.44611 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 192.9 |
| adc526d0-049e-3991-b1a0-fa047d4f8de3 | -20.24791 | -41.95066 | 2025-09-06 03:51:00 | NOAA-21 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a20fc3ee-2e65-3fbd-9394-b29398a4bd5b | -15.55001 | -49.81942 | 2025-09-06 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 50f5c941-4e5a-3054-96fb-c1104806267e | -13.56997 | -48.12245 | 2025-09-06 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e57cce7c-48b9-3d52-aa06-0f6e018ef940 | -18.44015 | -45.93224 | 2025-09-06 03:51:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0768e20c-4430-3957-bed3-65e10f582e6a | -14.57451 | -48.01148 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4425e19-450c-3d4f-9560-3d4d0dcf3675 | -20.02005 | -44.59659 | 2025-09-06 03:51:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 20b92f5f-e303-3f8e-ad10-a0f6026ffbf6 | -13.84525 | -46.27163 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5019b2bc-11b0-37a6-be65-9190cccb2146 | -14.57618 | -48.03061 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3c63053-4490-38b7-82c7-c99534775acd | -14.18788 | -53.02298 | 2025-09-06 03:51:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6c2c456-bddd-3aaa-b5ca-020b82ea9ede | -13.90352 | -48.02615 | 2025-09-06 03:51:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34a332ec-081d-3e57-b425-115f4133c67c | -18.59051 | -42.52703 | 2025-09-06 03:51:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 04bd10c9-bc38-3c31-8c7a-432717c9414b | -14.89845 | -49.4421 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7415116-1953-3ca2-a373-8f55145566d4 | -19.63017 | -49.388 | 2025-09-06 03:51:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1cc91a9-aace-3092-bfe5-4e00b775ac12 | -19.93322 | -43.60801 | 2025-09-06 03:51:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f93a9baf-052c-3a4b-b705-4c5b2a112388 | -13.55992 | -48.11696 | 2025-09-06 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a7e02c3-2525-3ac4-b785-91c455c5aa7c | -18.69136 | -44.6081 | 2025-09-06 03:51:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7201455-1218-3fad-8a2f-89cd7d0edbbe | -19.83388 | -43.18473 | 2025-09-06 03:51:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 254b6432-a015-34ab-a42f-ad555c8d5ed9 | -15.36828 | -46.41717 | 2025-09-06 03:51:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6211c3c-93cb-37c3-aa04-fba598164022 | -14.58681 | -48.08592 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9da6124-c5b1-3159-ab58-9062f5194f51 | -17.72716 | -42.66051 | 2025-09-06 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a5f0d039-dc43-334c-aa75-f21728173aaf | -14.89517 | -49.45802 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 30617c9d-fd2e-3851-9801-8a4af98a77e5 | -14.57579 | -48.00492 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f9191e1-daa8-3803-92b4-2a5513b1cf8f | -15.643 | -41.85681 | 2025-09-06 03:51:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 364e52e8-adb3-3fb3-9652-60a64c5e82ad | -14.57515 | -48.00821 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f9728b5-2157-3fc2-9b17-af1a7c20213b | -20.79131 | -41.1297 | 2025-09-06 03:51:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 38262428-b50d-3b12-af73-0e3b1c4530c3 | -19.97851 | -43.39462 | 2025-09-06 03:51:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9e90ccef-85ba-39fb-a674-ed1d16520243 | -16.72717 | -49.39576 | 2025-09-06 03:51:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4f9575f-1bde-3bbe-aae6-be7ba1038f6d | -18.08546 | -45.80119 | 2025-09-06 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab827224-ab4e-3826-8766-3425877db690 | -17.60764 | -50.56353 | 2025-09-06 03:51:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b035bc2c-1133-3e1a-a20d-32611a716c1c | -14.56852 | -48.01435 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f235336b-2891-3932-9749-ebabb20db472 | -13.90477 | -48.0198 | 2025-09-06 03:51:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdd24bf8-aa9e-3cd7-9ed8-304ec83c5e0b | -14.80352 | -48.11802 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a98178cc-8d11-3410-9a4b-603e6fd18b47 | -20.46739 | -48.79192 | 2025-09-06 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ad10692d-6435-398b-8746-39e11718931e | -13.55311 | -48.12332 | 2025-09-06 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fa8dec8-2b75-38a9-8998-f553df156a70 | -23.19704 | -50.34925 | 2025-09-06 03:53:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c140e6fe-9851-3ef9-bf43-3f2c6864eb54 | -22.65874 | -46.82333 | 2025-09-06 03:53:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d2cc426f-12f8-3a94-9985-e340d002444a | -24.51756 | -50.74989 | 2025-09-06 03:53:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e33cbbde-58ca-3f2b-b3f6-1ad8967d0148 | -22.24761 | -48.77093 | 2025-09-06 03:53:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 5fcbaa11-c797-30b5-9537-3466d5cc4882 | -23.42182 | -47.04546 | 2025-09-06 03:53:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3a935003-9ebe-38c4-bf05-779e8a7fc47d | -22.24409 | -48.76413 | 2025-09-06 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 461c9035-377a-3fa3-9b33-e42973ccc6cf | -22.74035 | -47.03278 | 2025-09-06 03:53:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 75e8bbc5-f326-3d00-86f0-6760e4534c70 | -23.05037 | -47.08194 | 2025-09-06 03:53:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 252291de-263a-32be-b73d-8fd4472081b5 | -23.42118 | -47.04245 | 2025-09-06 03:53:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 670dcf3a-6098-32a5-a71a-9481bfdb87c3 | -24.51247 | -50.74863 | 2025-09-06 03:53:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a17f21b9-0fc1-3b4a-8153-6fcb8121091d | -22.56357 | -45.7743 | 2025-09-06 03:53:00 | NOAA-21 | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e9440068-e57f-30f9-9465-b47f41d73c40 | -21.83614 | -46.46231 | 2025-09-06 03:53:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cf02471a-3fe3-3cd3-9aeb-f14b83e911af | -21.84027 | -46.46315 | 2025-09-06 03:53:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 276a135e-6094-3c7f-8077-7b793952d786 | -21.82653 | -47.99667 | 2025-09-06 03:53:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06b968d8-2bdd-3ea4-b38c-acf1aa846834 | -23.19626 | -50.35276 | 2025-09-06 03:53:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4604ec49-85b5-3695-8c24-6a80d84b49a0 | -23.19192 | -50.3481 | 2025-09-06 03:53:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ca9ede50-ea31-38d0-a2fc-8d0162e06134 | -22.85082 | -47.225 | 2025-09-06 03:53:00 | NOAA-21 | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4b1da7f5-6d36-3c57-bbe8-14a6dea36d8d | -22.24648 | -48.7527 | 2025-09-06 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| d1fcfc23-1194-374b-842c-e6acbbed46cd | -22.78605 | -50.61882 | 2025-09-06 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dd444f14-c06d-3e8d-8e00-76558e59bbd9 | -22.85881 | -42.00831 | 2025-09-06 03:53:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8d4e294f-fe49-34f1-8c3b-e15725a1d696 | -22.25228 | -48.74855 | 2025-09-06 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| e4d357a9-01ce-3d8d-8e52-49e53be392d8 | -22.25693 | -48.74994 | 2025-09-06 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4a3515a6-07ea-35ea-85e8-e3a70b84cbcd | -22.25883 | -47.30286 | 2025-09-06 03:53:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e7a09dd8-44f1-3a4f-8283-3499eb9ca5a3 | -23.04955 | -47.08613 | 2025-09-06 03:53:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a913b771-d365-3b36-b734-93e4156ef1d6 | -22.24529 | -48.7584 | 2025-09-06 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| 4bd4e9e7-7ede-3a77-97a9-75dcf40743ff | -23.43173 | -47.03922 | 2025-09-06 03:53:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| aee4665c-6bab-3449-84be-66be3ac4e22b | -22.78685 | -50.61527 | 2025-09-06 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aa2aad8f-7eba-349a-ac44-1718cc38dadf | -21.76704 | -47.27934 | 2025-09-06 03:53:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4614cb3c-c58a-3de2-a1bf-bbcf6cc432c5 | -21.30254 | -48.55511 | 2025-09-06 03:53:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8afad262-ee47-32d9-8d48-805e58a53c2c | -21.83212 | -47.99257 | 2025-09-06 03:53:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6c17d6f-e2bf-32bc-a3b9-973f1ce10b9a | -24.51037 | -50.74759 | 2025-09-06 03:53:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8b24984a-53ad-3091-b157-54c9d3743f37 | -22.25797 | -47.30727 | 2025-09-06 03:53:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a6efcad9-8dce-316b-a093-11f557395df9 | -22.78721 | -50.61707 | 2025-09-06 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7c49ce16-4946-3cf4-8044-475457b127da | -23.12179 | -47.03139 | 2025-09-06 03:53:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b1980fcb-33f1-3c24-bd9f-e7e20cef81ed | -22.78165 | -50.61388 | 2025-09-06 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e745dc21-1320-3652-a523-b6ab216546f9 | -22.26159 | -48.75131 | 2025-09-06 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f21c01ce-0e76-3402-a3c5-83f3812a541a | -21.99907 | -49.9152 | 2025-09-06 03:53:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4041e880-441c-3d21-a6c7-009b0fc0d78a | -23.41765 | -47.04461 | 2025-09-06 03:53:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 68e19e89-883d-3553-9616-f1b071227794 | -22.12277 | -45.78588 | 2025-09-06 03:53:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6481a2b6-94ae-3777-aa90-7164081834ee | -22.78085 | -50.61746 | 2025-09-06 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 159576e9-2fa4-3aea-9a1c-c79bc7b99c06 | -23.42677 | -47.04234 | 2025-09-06 03:53:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d62a8d93-7478-3e80-abfd-8510079879ab | -21.93709 | -46.13435 | 2025-09-06 03:53:00 | NOAA-21 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8ed36630-f3db-3270-9f5b-5209d26b088e | -23.42261 | -47.04147 | 2025-09-06 03:53:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 246b6829-0bac-31f0-a31f-31f4c4947581 | -23.41845 | -47.04061 | 2025-09-06 03:53:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0968fc03-176f-3593-9cc0-ec4ff7665b9f | -23.42611 | -47.03933 | 2025-09-06 03:53:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |


[Clique aqui para ver as próximas entradas](README30.md)
