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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8566d222-da14-32ba-b865-604ed821db29 | -20.6358 | -47.4322 | 2026-08-22 03:10:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 8fc9504d-5373-364f-af6b-4edb3efc73cc | -8.5218 | -54.8411 | 2026-08-22 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 383fb953-fb6d-3b56-bb0d-8bb50b332da1 | -6.78 | -59.39 | 2026-08-22 03:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 701780e1-5040-3244-8151-a9b03571ff58 | -8.5218 | -54.8411 | 2026-08-22 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| e5a1e965-53af-37dd-9396-f79e78fc8deb | -10.7512 | -50.254 | 2026-08-22 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 640514e3-09d6-3ad1-8587-22551a184a0f | -8.522 | -54.8209 | 2026-08-22 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 213115da-5635-3b3c-9f4a-4ee501cd4234 | -6.7878 | -58.6477 | 2026-08-22 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a4fae29a-a616-36dc-94cd-572dc0554538 | -6.7693 | -58.6485 | 2026-08-22 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 685219e9-f49c-375a-a3c5-8a4b30d552cf | -6.7692 | -58.6679 | 2026-08-22 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 155.7 |
| bdbf6caf-2980-31c1-819f-267ff6d33d96 | -8.5406 | -54.8197 | 2026-08-22 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 3f686404-d18b-3f48-9742-0da45841846a | -6.8188 | -59.6696 | 2026-08-22 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 65ed614e-b760-3269-94fa-9a4899a98934 | -6.97 | -59.0465 | 2026-08-22 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 361f7bc1-6a77-3e32-bdc6-e52fd6e54262 | -6.7691 | -58.6873 | 2026-08-22 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| d2a80f8d-34b0-3868-a5a1-c06efe950c44 | -20.6358 | -47.4322 | 2026-08-22 03:20:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 142.2 |
| bc9cce18-e88b-376f-966d-42835636bbb3 | -20.6351 | -47.4558 | 2026-08-22 03:20:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 709d949d-20ce-36e0-b29a-bb7d130cad53 | -6.7507 | -58.6687 | 2026-08-22 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 1dc263c0-0862-3e20-8395-40ca91ba7abc | -20.6563 | -47.4274 | 2026-08-22 03:20:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 63.0 |
| f5d692e0-6744-350b-8695-166b73ad3c9e | -9.1909 | -59.4619 | 2026-08-22 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| db010390-c850-3f1f-9d91-a9af4b3209ee | -9.1724 | -59.4436 | 2026-08-22 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 47adaf75-d314-3cde-a72a-dfe1d41ab590 | -9.1536 | -59.464 | 2026-08-22 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 605af7a5-f4c0-32f9-9e41-19b866008bcd | -9.1722 | -59.4629 | 2026-08-22 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 147.7 |
| b168dad1-04b1-32cb-9c0c-e7072bb938b8 | -6.7509 | -58.6493 | 2026-08-22 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| aa166b02-763b-3bea-9ea5-d876b4a0622c | -8.5404 | -54.8398 | 2026-08-22 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7d4390d3-178c-33b0-b0d3-14cd2b45c214 | -5.09811 | -37.9593 | 2026-08-22 03:21:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6a88d2de-87f8-3642-9f7b-915181f735f2 | -5.19225 | -35.84738 | 2026-08-22 03:21:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fbebb576-bfb4-3944-8a4b-df39d55c910f | -7.724 | -35.18596 | 2026-08-22 03:21:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b31c4ead-3a12-35e6-afc6-b991ba1469a8 | -5.19172 | -35.85048 | 2026-08-22 03:21:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3f382bab-b68b-3afd-828d-a2f582787937 | -7.72436 | -35.18428 | 2026-08-22 03:21:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8fb9444b-d6d5-393f-94b1-8069b02a351c | -7.72348 | -35.1894 | 2026-08-22 03:21:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b2155593-e0a4-39b5-9eb1-150b0304dca6 | -5.86998 | -35.65629 | 2026-08-22 03:21:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 02586604-2975-3cfc-bd05-8a27c77e074e | -5.87504 | -35.65732 | 2026-08-22 03:21:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6456035c-6918-360d-8d03-dbd4bb6422e7 | -15.8064 | -38.91116 | 2026-08-22 03:23:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f07eb45e-28c1-3546-995a-eba36c8993c4 | -12.27602 | -43.15931 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ba380618-622b-3d9c-851e-04ffade31e1e | -14.40046 | -43.80228 | 2026-08-22 03:23:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca1d88cb-88c4-3b9b-9039-e900a6ca1da8 | -13.99608 | -42.48086 | 2026-08-22 03:23:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 856a6c3e-b51b-304d-b81f-ec9750001d8a | -13.37982 | -41.34441 | 2026-08-22 03:23:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0774d088-4844-3b30-a90c-515ef13649c7 | -12.24646 | -43.18735 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 78ee6481-1888-3bcf-8a8b-0b50a121bd37 | -12.25349 | -43.1898 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3741dfdc-a256-3bbe-85b4-f97e484c6c4f | -12.27425 | -43.16734 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3f068396-2c74-3139-84c4-b429fabbf130 | -15.81167 | -38.91232 | 2026-08-22 03:23:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 957d376a-1c23-3f1e-971b-9da58ba59d50 | -12.24761 | -43.18538 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a2a67366-e672-3515-b46a-b6fc0a7d0d8f | -12.26409 | -43.17555 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ab681968-6ac6-3a81-ade3-160d16b2bd8c | -12.25547 | -43.18054 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8c19d45c-ea03-3d28-a787-bce3852fd780 | -13.37858 | -41.3503 | 2026-08-22 03:23:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21e9aaca-45ad-39d7-8716-7e97568165aa | -15.80046 | -38.91335 | 2026-08-22 03:23:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dc201be6-782c-3c38-a683-480083c713e6 | -12.26532 | -43.17363 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| db5bb4f9-56cb-3a7f-b658-5fa7ad598414 | -15.79977 | -38.91673 | 2026-08-22 03:23:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e408d234-c94e-30f7-9f66-0e2678ca4477 | -12.27302 | -43.16906 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0209b895-69f8-3cfe-b3fe-f79d631bd15f | -12.27244 | -43.17561 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 060efb4f-39da-3e5c-bb2c-131e3b35ecd9 | -12.27121 | -43.17755 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0f80c1d0-d759-30ae-bee7-d81fda434986 | -12.25461 | -43.18793 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| be314583-cb8b-38ac-a2c9-d05b9752f337 | -12.26349 | -43.18193 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| df08a4de-c042-350d-8b6d-099621382d2d | -14.40215 | -43.80158 | 2026-08-22 03:23:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7779a390-e6e2-33dc-923a-608629fc9233 | -12.27061 | -43.18392 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a63fc3aa-31b3-3ff3-ba0d-a1c8aa5dadd5 | -12.25664 | -43.17872 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| dfeb179d-66c8-3521-b7cf-8901dbc65174 | -14.00284 | -42.48225 | 2026-08-22 03:23:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 91d4de37-22cf-34d2-9682-63dd062aceb7 | -14.4021 | -43.79485 | 2026-08-22 03:23:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8c127ed-0ef1-31c1-8c41-328750cf73b2 | -12.27475 | -43.16092 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 63364358-4f33-3303-8246-10dcf1fa8d9b | -12.26232 | -43.18385 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fdbf475c-650b-3573-a1cf-8cbe47d6d269 | -12.26943 | -43.18586 | 2026-08-22 03:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1a3ccce9-682f-3695-b74d-58f7911d7d24 | -14.40385 | -43.79414 | 2026-08-22 03:23:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9bab70b0-801d-32a9-8a3f-13b91caf4197 | -11.84096 | -39.18696 | 2026-08-22 03:23:00 | NPP-375D | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 926c4126-00f9-30e3-b256-e6d1ae31cf1d | -17.92073 | -44.40844 | 2026-08-22 03:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ec07fbd-ca23-362a-8e83-a60221fa20b3 | -18.87193 | -41.98953 | 2026-08-22 03:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 07a2d562-07b8-3a69-8df4-638042ee234d | -18.87407 | -41.98558 | 2026-08-22 03:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c9a9bca8-f27c-35fd-a2cc-06d49dae56e9 | -17.92036 | -44.42122 | 2026-08-22 03:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c081811-dadc-375c-8bb6-ddbea9018885 | -18.33609 | -42.46795 | 2026-08-22 03:25:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a49eba60-0df7-36d2-ab65-74431301d855 | -17.96234 | -42.73608 | 2026-08-22 03:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96e774dc-906b-311c-9f18-e12d452476e3 | -17.95717 | -42.72705 | 2026-08-22 03:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cb438e6d-8875-3a5e-800a-38ecfc8eba55 | -17.9577 | -42.72713 | 2026-08-22 03:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 35dc0b6e-d105-3e57-9895-c8908e574d11 | -22.00796 | -45.31582 | 2026-08-22 03:25:00 | NPP-375D | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9a0054f1-34e8-3955-b27f-cc34de2c8156 | -21.59386 | -44.01186 | 2026-08-22 03:25:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 58ddfe0d-a05d-3b31-b8de-995cef21110e | -17.95623 | -42.73347 | 2026-08-22 03:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0fc7b07a-c7f4-3f77-ba5e-1117f9a6a72b | -17.9189 | -44.41611 | 2026-08-22 03:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62aa8680-f06e-31f6-b114-a81eed58b7e0 | -21.59518 | -44.00644 | 2026-08-22 03:25:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 38f9c5f2-9822-3aa8-b92c-5a584f18314d | -20.20754 | -40.36609 | 2026-08-22 03:25:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 63d23b2d-74d7-3914-a9e5-1d119a31baf0 | -18.33727 | -42.46284 | 2026-08-22 03:25:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 533a1b7d-f7d4-3556-8470-b80ce2f17e1a | -22.00763 | -45.31932 | 2026-08-22 03:25:00 | NPP-375D | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 71f9d41e-b1f7-365b-824b-70ee350d5f43 | -17.68836 | -44.44754 | 2026-08-22 03:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e562acea-9229-3702-b7c4-eb6d47ec0b07 | -17.15762 | -39.51049 | 2026-08-22 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bc376e6d-f563-3277-9726-9dad21cb2120 | -17.95575 | -42.73338 | 2026-08-22 03:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c7733cfc-adfc-3053-85af-7efc721e75b0 | -17.96877 | -44.36145 | 2026-08-22 03:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe50bb7c-abb9-3c81-9767-7cf6982fa16d | -17.97416 | -44.3697 | 2026-08-22 03:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 496ece5d-c644-30de-bb97-ea46d88fcc39 | -18.342 | -42.4708 | 2026-08-22 03:25:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5b65d95d-62f8-38e6-bf44-64090df40297 | -21.60016 | -44.01375 | 2026-08-22 03:25:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b866be5e-37b7-3bc4-b066-11e7381bbbec | -17.9726 | -44.37628 | 2026-08-22 03:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7da0dd2-4b37-390a-9a92-0d2b40b7a696 | -18.48845 | -43.86755 | 2026-08-22 03:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 215e9d81-0f26-302f-a125-ea9e27b0338f | -18.3397 | -42.46546 | 2026-08-22 03:25:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2b721215-1f73-3735-9d01-13a8806242d2 | -17.91893 | -44.39576 | 2026-08-22 03:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d843b93-6c5b-39c7-86f6-b4a4d077397b | -17.96186 | -42.73601 | 2026-08-22 03:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6a9d8513-b243-3413-903f-a9f1741ac473 | -18.33855 | -42.47059 | 2026-08-22 03:25:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a1960b95-0bab-3b19-9f81-4e33d1bbf985 | -17.96396 | -42.72905 | 2026-08-22 03:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b69be792-c82d-3b44-afb5-23b96239f010 | -17.15429 | -39.50932 | 2026-08-22 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8a01dc34-574d-310e-9293-bf499c349aaa | -21.60152 | -44.00813 | 2026-08-22 03:25:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7b486513-ef05-33b6-9f7a-020809135b8f | -22.00628 | -45.32261 | 2026-08-22 03:25:00 | NPP-375D | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3f7daade-de2b-34e5-8a01-eb20f0f0aec0 | -17.6954 | -44.44911 | 2026-08-22 03:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 983cb3c3-c824-36ad-9e3e-a33a19289031 | -18.87292 | -41.98508 | 2026-08-22 03:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3835d8f3-667c-36de-9206-afd3b52bbe9f | -20.21051 | -40.36412 | 2026-08-22 03:25:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 52a8d1ea-b5d0-3e29-b04e-93017bad4e8e | -19.74893 | -45.10476 | 2026-08-22 03:25:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad210e6d-1f95-384d-a944-495c90b531f8 | -20.20974 | -40.36762 | 2026-08-22 03:25:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
