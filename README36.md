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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d17332e-f14c-3d73-a167-ec1ea5705eca | -7.75542 | -66.90889 | 2026-09-11 06:33:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5c2992a-2e18-3433-9969-b18168441f4b | -8.88303 | -70.84042 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c7a656f-5db0-37dd-abd3-56bafcdb541f | -9.11179 | -67.694 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9378aa6a-a77f-339e-88de-ff3871b1dda1 | -9.04109 | -65.42049 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d9092585-ab00-368e-934a-8805699e8789 | -9.22408 | -65.58949 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4bdaaa15-de9b-346d-907e-3da921e7685e | -9.11123 | -67.69853 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c709bae-3158-37d9-86e7-21ec27135c5b | -8.64734 | -69.79587 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40017375-34c4-33b6-a236-7ceaec19dca0 | -9.21796 | -65.58246 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d753d8f8-fe9f-3730-9e1c-e0a94789d91f | -9.18365 | -68.21218 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 557dc7bb-72fe-33d1-9931-0641e5330f1c | -9.75937 | -64.94081 | 2026-09-11 06:33:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc1b6f4a-037a-37f8-bc99-95b4a1206aa5 | -8.65257 | -69.79655 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f063cce-5d1a-3bf1-acff-9510784d0083 | -9.42297 | -65.85725 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a450c65-c386-3996-95a8-e346ca154bb7 | -9.03496 | -65.41309 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c528a682-4a8f-32c4-897a-c08056df8956 | -7.37046 | -72.67738 | 2026-09-11 06:33:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b425dbb-01f9-37f6-ab41-ae2dc67917bb | -8.64776 | -69.79272 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc423d6d-c145-3912-bbfc-f0ca4c3b225a | -8.64023 | -66.51591 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c352027-aa6a-357c-af2b-c03ca8faeee7 | -9.17887 | -68.20298 | 2026-09-11 06:33:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6048cce8-06cb-3daa-8e26-e9b5a84b6bea | -8.6534 | -69.79029 | 2026-09-11 06:33:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ababbbf-68a7-3aff-a222-b2e05a028b56 | -9.50063 | -66.78989 | 2026-09-11 06:33:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 985b4450-5998-3c86-9fd2-e0641574efb8 | 1.29005 | -50.67908 | 2026-09-11 07:12:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bdf53eeb-cf02-35d1-8eed-27aaa5bc277d | 1.28064 | -50.68048 | 2026-09-11 07:12:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7b2b5957-6e5f-35c3-896d-779a7496eae1 | 2.51731 | -50.85183 | 2026-09-11 07:12:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8c4c95ab-3d82-3e0a-9d16-704edb0d283e | -8.63421 | -47.41172 | 2026-09-11 07:14:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 7fe37ec3-b486-3869-84a1-452f2ebcfb82 | -2.73773 | -57.62586 | 2026-09-11 07:14:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0fbbf068-f249-39fb-817b-2ed3e3c9e73f | -2.85796 | -49.53842 | 2026-09-11 07:14:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| b82f78b8-b9ee-3481-81fd-e693a1c5bf87 | -9.63498 | -49.0059 | 2026-09-11 07:14:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 6101de54-999a-39f5-9370-72ce427dc2c6 | -8.07899 | -54.84047 | 2026-09-11 07:14:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ec82d221-a973-340d-a702-997b68bd77b2 | -2.73963 | -57.61371 | 2026-09-11 07:14:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a29c0421-7dd6-3718-970e-45bb4ed20d10 | -3.37697 | -50.75237 | 2026-09-11 07:14:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0ac1063a-0ff9-3764-812c-5333dff455ed | -2.71928 | -57.61736 | 2026-09-11 07:14:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| e4f36644-f042-3b76-9a2b-825c8ed35eb2 | -4.29924 | -49.11245 | 2026-09-11 07:14:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b936905b-1b62-3dfd-b2fb-92eea4ecffa0 | -2.71916 | -57.61062 | 2026-09-11 07:14:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ff25e616-302d-3580-93f7-400e03fa98b7 | -3.36697 | -50.7509 | 2026-09-11 07:14:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8981b9b9-b500-374f-8a6e-5108142fe0ca | -6.24406 | -51.68975 | 2026-09-11 07:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 45dfdb6d-ad18-3168-ab3c-cebea4448ecc | -4.52801 | -54.96317 | 2026-09-11 07:14:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 811e2b5f-dd0d-3cef-9fad-9c154482c391 | -4.30149 | -49.09658 | 2026-09-11 07:14:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 1fad9128-9c6a-3a7b-826c-49382c271a7a | -4.28992 | -49.09502 | 2026-09-11 07:14:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| a7cce20a-6eec-34f7-9871-a6da780dfb2f | -2.71724 | -57.62277 | 2026-09-11 07:14:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| ee0e2313-0b9f-3697-b49c-d069e02de3ee | -4.53815 | -54.95567 | 2026-09-11 07:14:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a53dacef-2e96-3875-bece-c91eb011617e | -2.93821 | -50.46586 | 2026-09-11 07:14:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| de4223fc-6306-31d3-acc9-e8d536b20400 | -4.85844 | -56.00522 | 2026-09-11 07:14:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d05821da-cb13-3687-80d9-1ebf6889bfa7 | -6.23425 | -51.6884 | 2026-09-11 07:14:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ef4f66c5-1ecb-3fa3-8b7d-415e221f6107 | -4.53681 | -54.96446 | 2026-09-11 07:14:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1f0a175c-33f5-3ac5-86b4-c51035e8cd1f | -4.52936 | -54.95435 | 2026-09-11 07:14:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ba73fd5a-488e-3410-98ad-4d9e03ff7039 | -4.35176 | -54.77409 | 2026-09-11 07:14:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ebf17ec9-e190-37b2-b37a-98c1bf4992a7 | -2.71744 | -57.62955 | 2026-09-11 07:14:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a6a30666-1e40-341c-a41d-a5532a28c8cf | -4.86746 | -56.00674 | 2026-09-11 07:14:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bfe13233-e7d7-3d23-ac5c-124b40018ec3 | -1.77387 | -54.94281 | 2026-09-11 07:14:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 054af41d-53ff-33ff-be2e-e3fe7fb5898d | -8.62377 | -47.41513 | 2026-09-11 07:14:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 3c08b684-fe7a-315f-9ba6-a50709e2e420 | -11.8021 | -60.45512 | 2026-09-11 07:16:00 | AQUA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1ceb06e1-af9f-3abe-adc2-95329bf59714 | -9.03812 | -65.41473 | 2026-09-11 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 4fb1edc8-30e7-389d-92a1-5edd8f6935f2 | -11.81295 | -60.45683 | 2026-09-11 07:16:00 | AQUA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 583a757f-93d9-3c39-812e-8fea9d202689 | -13.26404 | -61.59225 | 2026-09-11 07:16:00 | AQUA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 23fa6874-b8db-3bdd-b26c-8a4b0ccbe5a7 | -12.1538 | -64.13605 | 2026-09-11 07:16:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 21.8 |
| f93da975-6845-399d-ac9b-ed577dbab21b | -12.15064 | -64.13014 | 2026-09-11 07:16:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 22.6 |
| c952f7c4-ab4d-3cac-b603-950aacdd7b36 | -13.25966 | -61.59843 | 2026-09-11 07:16:00 | AQUA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 6ea62a3f-df05-3741-ab0f-629f2c2ed3a7 | -8.83011 | -62.47599 | 2026-09-11 07:16:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 57dd8bc1-a79e-3fbc-b1cc-54a474b4f184 | -22.26491 | -55.83838 | 2026-09-11 07:18:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 33bc1b10-230f-3cce-9c7e-15bcdfd878b2 | -22.27433 | -55.83986 | 2026-09-11 07:18:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b5381411-5e8c-3e90-b01f-2e492166793c | -20.49315 | -57.45936 | 2026-09-11 07:18:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 9055499c-be17-310d-8d58-fa1023cccc39 | -10.641 | -46.136 | 2026-09-11 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| d6664dff-9e34-319c-8288-c577d756c974 | -7.2895 | -42.218 | 2026-09-11 11:08:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| eace33c2-039a-32ee-9dc4-b62981e8e203 | -7.4614 | -42.11798 | 2026-09-11 11:08:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| b5c72e31-35df-3407-bfbd-5823d133970a | -7.60464 | -45.15169 | 2026-09-11 11:08:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| da4928a6-811d-32ab-9d7d-49716c868522 | -8.63242 | -47.40326 | 2026-09-11 11:08:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e5ef9f48-c909-3d8c-8158-db9d65008c0a | -4.76746 | -42.6673 | 2026-09-11 11:08:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| b84a6054-a833-3e04-a357-da7054082839 | -8.65103 | -36.82045 | 2026-09-11 11:08:00 | TERRA_M-M | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 33bf6feb-4270-3ab0-8d4d-8b7d27738f22 | -9.32324 | -45.64354 | 2026-09-11 11:08:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c44f98ee-7ffd-3a23-8a6e-676d186456b4 | -7.12109 | -42.11377 | 2026-09-11 11:08:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| d18c915c-67a3-3846-8e25-93189d76cc90 | -8.62715 | -47.40974 | 2026-09-11 11:08:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 3185def0-a08f-3b82-8bab-0bdb715f2b52 | -8.62722 | -47.43479 | 2026-09-11 11:08:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 2df8316e-43a9-3fcf-a0e8-f529f1ed958b | -5.10418 | -38.09956 | 2026-09-11 11:08:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8f351469-4cfb-3ec3-87f7-fdc34037d412 | -9.21371 | -41.03404 | 2026-09-11 11:08:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9e0b49a1-e2b0-3f40-9aa6-4afef3ce3b31 | -6.37832 | -39.24895 | 2026-09-11 11:08:00 | TERRA_M-M | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e0815578-dcf3-337e-91d0-7d6e87864213 | -10.63519 | -46.13883 | 2026-09-11 11:10:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d9a639d4-8d4a-358f-981e-5b32b4f97b71 | -13.45956 | -42.63296 | 2026-09-11 11:10:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| ed1424fc-5571-3c29-a10f-9c3f70f954f4 | -10.78383 | -45.96393 | 2026-09-11 11:10:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d6a1d14f-2d5f-30ba-bd6e-6206f80ebe3a | -10.64874 | -46.1412 | 2026-09-11 11:10:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 1b5691df-dbe1-3d68-844e-66d07a28c877 | -13.65138 | -43.63469 | 2026-09-11 11:10:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d9d62923-0333-3838-9255-fe50b350c81e | -10.74054 | -46.14139 | 2026-09-11 11:10:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| c93c23ea-5fbc-397e-b569-5dd7b59bc3d3 | -12.38018 | -43.43409 | 2026-09-11 11:10:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 90c9524a-9fcf-3fb2-befa-f9a787aaaf4a | -13.44355 | -43.85019 | 2026-09-11 11:10:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b632d50b-b40b-380d-b199-dbfdb7a241d7 | -14.0662 | -45.61845 | 2026-09-11 11:10:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| a2fc4acb-0579-39c8-b1cb-ff975b54835b | -10.78735 | -45.94262 | 2026-09-11 11:10:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| db306d1b-f040-36be-8ca1-26722292413c | -13.44579 | -43.83609 | 2026-09-11 11:10:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e175dd7d-8591-3363-949c-594abde59991 | -13.46133 | -42.62143 | 2026-09-11 11:10:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 399d4204-5962-38c4-b732-a696096eed84 | -17.95964 | -40.22334 | 2026-09-11 11:13:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d2bbd44e-c943-35b6-80b2-73786b73a5e2 | -17.96095 | -40.21409 | 2026-09-11 11:13:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 1684c236-a751-328f-aa35-4a816950a83b | -15.44666 | -41.39301 | 2026-09-11 11:13:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 63192af8-c9bd-36da-a934-ea783f6b8c76 | -17.88907 | -41.28904 | 2026-09-11 11:13:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| be4c0855-9814-3003-b63a-0c50688615d7 | -17.76883 | -43.74783 | 2026-09-11 11:13:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 86d137f1-b9c7-3a1f-82ad-34d8d16bc4a3 | -14.85464 | -48.1605 | 2026-09-11 11:13:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 14064009-f094-31b8-843a-f3043a08b0fd | -17.77687 | -43.76128 | 2026-09-11 11:13:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 758406ab-9a18-3571-8f2e-5ed8bc057073 | -15.02403 | -41.25674 | 2026-09-11 11:13:00 | TERRA_M-M | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 472264bc-a527-33f1-a90c-cb9d41ab5b50 | -17.76692 | -43.75972 | 2026-09-11 11:13:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 2b30f96f-0e9c-3afc-8df1-18b74afe5583 | -15.44811 | -41.38335 | 2026-09-11 11:13:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 65b65105-048f-3eff-aff9-4e4488aea4f4 | -8.6192 | -47.4114 | 2026-09-11 11:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5fd12dd4-f926-3f3c-9920-3e5129b0d75a | -10.7959 | -45.9575 | 2026-09-11 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 712d848a-1d99-3887-a8ab-49fb9635e4a5 | -10.7963 | -45.9348 | 2026-09-11 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| eae5d4b7-e540-3f79-a99b-94688127181e | -13.4453 | -43.8366 | 2026-09-11 11:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |


[Clique aqui para ver as próximas entradas](README37.md)
