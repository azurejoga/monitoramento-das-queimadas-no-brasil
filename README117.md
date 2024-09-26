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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eab9c94-20d2-315d-ae29-713253bba540 | -10.50123 | -51.15707 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ac51728-38ee-372c-bda3-b855b77a1f67 | -10.49799 | -51.2314 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad6015ef-bca0-3757-965e-59c083dbf4d9 | -10.49682 | -51.16102 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afbb0cc9-6ac0-3540-82d2-03402adb5971 | -10.49668 | -50.75681 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7158bce-ae43-3b08-b355-f4ddb7316eb5 | -10.49489 | -51.22651 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9bcd750-c257-3faf-bc3e-deaee9763bf8 | -10.4945 | -51.20307 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b1bda40-527c-3420-8266-c3480a344418 | -10.49379 | -51.20794 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 212faba6-a8fa-3a74-b0ff-82317e3b938d | -10.49284 | -50.75624 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7549f76d-556c-30c5-843b-22ba74e018a5 | -10.49277 | -50.83982 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87031144-40c0-31eb-8b45-b7701a40b78d | -10.49242 | -51.21733 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf3120aa-a39b-3131-8264-165e3ce673c0 | -10.49177 | -51.16936 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7780377a-65cb-3d98-8e79-b7a369086474 | -10.49176 | -51.22178 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed01ded7-ccfb-347e-8266-3ab797150564 | -10.49111 | -51.17392 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6db468a-49fd-3434-a357-3a0803d596b9 | -10.49098 | -50.8249 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8faa2e17-dc27-3f50-bebd-dfd3d344ac88 | -10.49074 | -51.20268 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eadb335-03c0-3dc8-8af9-1ca5051e48cd | -10.4903 | -50.82972 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 647335bc-9f2b-373f-8c36-b08bd893c70e | -10.48332 | -50.82384 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e69fc0ae-124a-32b2-86ef-d340b4d1db11 | -10.48062 | -50.7595 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 769a81c6-df3d-371f-8756-18798f12a853 | -10.47949 | -50.82331 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5dc7f536-165d-3fc6-ab06-d337297828b7 | -10.47608 | -50.76401 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a26bdae4-2351-3b29-9b8c-c27149400ef9 | -10.47328 | -50.76685 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28d24467-d56b-371c-9e48-f0590b7bae01 | -10.47221 | -50.76369 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b2ba991-7559-3904-ba21-603cd4b282c5 | -10.47002 | -50.80727 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee3aabc4-f011-375b-bbf0-1eec817760d8 | -10.46943 | -50.76637 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb6fc4f5-1727-3614-a7ee-7c8ecdf0fc49 | -10.46935 | -50.81209 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac6aa9fc-4b30-39ea-b5ce-300205a71bb2 | -10.46873 | -50.77114 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b39c2d69-1c66-351b-b5f1-4d87570235aa | -10.46804 | -50.77586 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbf9445e-e7ea-3892-987d-33b4749dc11d | -10.46771 | -50.76786 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0922b449-4151-30e4-807d-bfc33b91ac15 | -10.46769 | -50.80496 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8845ca5-7d56-32c7-b00b-ffc306b12bba | -10.46704 | -50.77263 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e28febaa-54f5-3cce-827b-90c38fa93059 | -10.46688 | -50.8018 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0223cb33-3319-39b9-a8ca-a9f2d54b616f | -10.46638 | -50.77735 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 653c0f46-50c2-3dba-8e66-a55b591378e9 | -10.46572 | -50.78206 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4eadb738-2113-3822-98c5-bb90116c3666 | -10.46493 | -50.77036 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40a950de-62bf-3747-8cb0-b33d122819ed | -10.46458 | -50.79953 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb68f89c-32d5-369b-82ad-81051f71dd02 | -10.46424 | -50.77509 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4fba10a-29d5-34a7-b590-2a6eb2033b94 | -10.46373 | -50.79636 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51152b12-bf3f-3eb0-8718-48a0b2d496f7 | -10.46355 | -50.7798 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9f27556-8e51-300e-8a31-da2b5713ac04 | -10.46323 | -50.77185 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31dc7231-914e-3caa-b34e-1c2475a0bf47 | -10.46286 | -50.78453 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6776a3c8-3e0e-387e-9d87-e8885ca12ec5 | -10.46257 | -50.7766 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c713ab56-e83a-3510-a76b-a4962ef18b19 | -10.46216 | -50.7893 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48f5fe25-2500-3af2-a831-971657335ed4 | -10.4619 | -50.78134 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33a7c6a1-7b72-353b-a980-44c793fb2720 | -10.46146 | -50.7941 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60568dba-56b3-3403-aa74-0177dbe5febe | -10.46057 | -50.7909 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07b9028b-a914-3538-b652-7479ba57fcd0 | -10.86773 | -51.16772 | 2024-09-26 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 590c99e9-32e7-328b-a82e-65cd5e7d4f22 | -10.86396 | -51.16717 | 2024-09-26 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1254abc7-c410-3e81-b570-fd9a2d64ff14 | -10.86019 | -51.16661 | 2024-09-26 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a8417e3-e601-3de6-ab4a-42c1d7be9929 | -10.85642 | -51.16605 | 2024-09-26 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 981db5bd-cbd2-3bb2-8cf3-95958a314885 | -10.85266 | -51.16549 | 2024-09-26 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d284d344-89da-34e7-ad0e-bc8a6a66995e | -10.852 | -51.17014 | 2024-09-26 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0568e3dc-a971-322d-8531-7373c9c93111 | -12.21656 | -51.30925 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7f028fd-4670-322e-bf6e-3f4ceac96f3b | -11.21824 | -51.15042 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 870aae6f-5151-350c-b526-5e33f98578d9 | -11.21757 | -51.15511 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 0ea2d1c9-d326-3da2-956a-4fc307bbb480 | -11.21445 | -51.14985 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 54a18c8a-fc98-31c2-ad78-2414d23d89e4 | -11.21378 | -51.15454 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1820a46a-6f44-3fe1-a245-2d7852ece871 | -11.21066 | -51.14928 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3f0991a9-2e79-34e3-b07c-352a1a824ad6 | -11.21 | -51.15397 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56464049-6249-3210-8b60-80ca343aad85 | -11.13021 | -51.32943 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb237523-1d3b-3df3-bf96-beddf3b15621 | -11.0813 | -51.45649 | 2024-09-26 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fb4dbe3-fb82-3bdd-b94b-38efdccefc17 | -11.06159 | -51.43511 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d24b924-4b52-33af-b062-65fdfe438cdc | -11.0598 | -51.42101 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed5efe10-0e5b-3093-9911-c218d226aa4e | -11.05916 | -51.42552 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f8767e6-abcb-3ca3-977b-2ce6a7eed7e6 | -12.85864 | -51.22415 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 242.4 |
| f362e698-610d-3a8d-9928-6fea3981f2bb | -12.85795 | -51.22905 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 3189f97d-7e89-3265-a050-ee05a26dbc5c | -12.85726 | -51.23395 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f0c2cc79-33a2-3e5d-a0a5-436f73a36efb | -12.85685 | -51.20887 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 8430f5e6-877f-39b5-bfb1-6def78648c32 | -12.85657 | -51.23884 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ce2ea04c-cabe-3eb7-be03-d5ae1e8654d5 | -12.85616 | -51.21377 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 718.9 |
| e244a096-e6fd-3e26-ba8e-b4f4f052dac1 | -12.85588 | -51.24372 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 358.9 |
| 85b72ae1-708e-32eb-a433-b4eedf79f29c | -12.85547 | -51.21868 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 718.9 |
| 8e78ef7f-982f-30d5-a95b-75696fffa73b | -12.85479 | -51.22358 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 88c0cf4a-2645-3845-bff4-0b4579de04ce | -12.8541 | -51.22848 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 29680384-a62e-32db-936a-8eb29d969707 | -12.85341 | -51.23338 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 550fd42c-fd75-35b4-a863-c71cf421ce43 | -12.853 | -51.20829 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ea762b6b-a704-3361-8198-2ad7d8bf5cd1 | -12.85272 | -51.23827 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 3377f0c7-efa4-36a0-886f-c662cebcf525 | -12.85231 | -51.2132 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 657935b6-e77d-3d65-991d-40749d91b4e0 | -12.85162 | -51.21811 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5b07e937-8662-3247-b062-87f8a0822440 | -12.85093 | -51.22301 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 96bdd9a9-15b4-393b-849d-e246017d5bf7 | -12.85025 | -51.22791 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 93d71bba-98e4-36bc-84ad-53a349d83279 | -12.84914 | -51.20773 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6662872e-c397-361a-9dc0-60983eb15a96 | -12.84887 | -51.2377 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 490.3 |
| 95077b2d-7928-304b-b516-1d7692b5472e | -12.84845 | -51.21263 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 059f24d7-9567-3e67-9b60-814a3ede2276 | -12.84819 | -51.24258 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.6 |
| b07ff3d7-7947-384c-9a38-3a771bb1c55d | -12.84777 | -51.21754 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6242955b-682f-37b6-82ca-374b08b068cb | -12.84708 | -51.22244 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 4c26734c-98fd-3d98-8ded-a4e3c000a2c6 | -12.84639 | -51.22734 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.5 |
| f539a825-8d3b-3459-954f-c5251a5a0b47 | -12.84571 | -51.23224 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 490.3 |
| bd89d7b1-7a58-36b5-a374-eb6fe1189fa6 | -12.84528 | -51.20715 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a94ae3b-31fb-38d4-bea1-af93f257e14c | -12.84502 | -51.23713 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 490.3 |
| f8328639-6fba-3ea7-b55f-04f2ae9c1117 | -12.8446 | -51.21207 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cdf3068d-887e-39f6-ad10-20a00f95c014 | -12.84434 | -51.24202 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.6 |
| ee0c88ae-d6d9-38f5-bcd4-4fa20ab8700c | -12.84391 | -51.21697 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8011d7e-2ef5-3ffa-90e3-bba29c5fc621 | -12.84323 | -51.22187 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ad179de-35d5-3304-8ed6-42af81f271f7 | -12.84254 | -51.22678 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca4e4410-191d-3081-a4a1-82b68fec1a64 | -12.84186 | -51.23167 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| d07dec0b-ba18-337b-8092-bae8d2472168 | -12.84143 | -51.20658 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7b237dd-a1a0-3805-813a-a6ba7668e4b9 | -12.84117 | -51.23656 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f9f44f46-1127-3dba-881c-0641de5ef4a0 | -12.84049 | -51.24145 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 673f67b1-1224-3eaf-820e-9b6b6eea24e2 | -12.84006 | -51.2164 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README118.md)
