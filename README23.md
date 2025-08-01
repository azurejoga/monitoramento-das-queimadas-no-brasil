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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95a38540-b75c-39bd-a079-3172e43d5f62 | -4.31312 | -48.09989 | 2025-08-01 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c46cb135-a0de-3fad-9fb6-6585b29c6cd3 | -5.05862 | -56.93028 | 2025-08-01 05:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d7375b2b-ec49-314b-a817-cc96fb92f3b9 | -4.31215 | -48.10657 | 2025-08-01 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2c42591-cd68-3813-94c1-6da6b8d5427e | -4.3171 | -48.09916 | 2025-08-01 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b24d3973-e787-316e-81ee-5ab5ccdc656b | -4.31616 | -48.10591 | 2025-08-01 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 80d5308c-fa26-3868-bf02-ad7e5da94bb5 | -4.31004 | -48.09818 | 2025-08-01 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1301f695-230d-3469-8751-385d2c3672f1 | -5.06342 | -56.92564 | 2025-08-01 05:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d4488a7-02f0-3475-8865-7eeafbe9d041 | -5.05943 | -56.92503 | 2025-08-01 05:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f28d3d89-9a2d-357c-9ccb-e77e10474761 | -8.0513 | -43.1001 | 2025-08-01 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 93dc9ab1-ff1c-3df6-8d8f-25a6f3d0e5a3 | -6.7478 | -59.1716 | 2025-08-01 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.4 |
| b1e14e6c-2bb8-3296-bd90-bd6f9720a0f8 | -8.0324 | -43.1022 | 2025-08-01 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| e089a117-d75b-32dc-8120-86ebb2a53a72 | -6.656 | -59.0981 | 2025-08-01 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 9b44a82f-66ad-3798-8a29-bd8e6530424e | -6.6328 | -59.9841 | 2025-08-01 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 92511c96-594e-36e3-ab63-dc5d031421ac | -8.0321 | -43.1257 | 2025-08-01 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| aefa62b2-29a9-3031-93ef-0cef0d3485a4 | -8.051 | -43.1237 | 2025-08-01 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| 4147e076-b50d-37e7-bf79-8fde999643f0 | -6.6376 | -59.0988 | 2025-08-01 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e8ad5da6-0e08-31f3-a9ab-63aff0adab0f | -6.7477 | -59.1909 | 2025-08-01 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| fc673bba-f59c-303b-a8b1-8b7eb2112d52 | -6.7293 | -59.1916 | 2025-08-01 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| a79b1ca4-523e-3ed9-843d-7a95edc488f9 | -6.7294 | -59.1723 | 2025-08-01 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 245.9 |
| c2a59251-71a2-3280-a8e6-53a4921518f3 | -6.7295 | -59.153 | 2025-08-01 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 064a7c8c-8405-3bcc-b168-333f4dd56bb2 | -6.748 | -59.1523 | 2025-08-01 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 2efe0328-d1aa-362c-84dd-483f4b3bf62e | -6.64693 | -58.82423 | 2025-08-01 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06eccfb2-b574-3b0f-a34a-ff40ba038c88 | -6.82937 | -59.26497 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| bfbf0e4b-6cc2-305a-a5ba-67229f004a19 | -6.62297 | -59.97598 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9c2bbd8d-ab9e-3fac-a3be-0b7b6d3bef07 | -7.33328 | -59.62333 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a188b87-9076-3229-acc2-317fd26bcfac | -6.82518 | -59.26848 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 7ebaeaa9-6e01-3772-aeac-b700183cffb3 | -6.82161 | -59.26792 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 92ef0af0-0a4a-3ed9-a948-b8fb9e504edc | -6.63903 | -59.09631 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed2afdee-94b5-3a9d-ab5d-a3b825387bbf | -6.74539 | -59.15727 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 699389bb-726a-3934-9d93-9e3efcfaee63 | -7.32621 | -59.62225 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d7ec14c-783d-38dd-91f3-bd652b39c755 | -6.74897 | -59.15788 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f4280ff1-46d8-306d-86a5-e6a3a8660a7d | -9.37385 | -67.77207 | 2025-08-01 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20da9df1-c7ec-35c6-bfe4-97a4d3a95d5f | -6.65057 | -58.8248 | 2025-08-01 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6069a1e5-1860-3f34-a27a-1bc40d65d496 | -9.63205 | -61.45659 | 2025-08-01 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0779a156-b42f-37a7-af5e-5e9891a819f7 | -7.07527 | -60.04179 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99b46db9-689e-3a11-91d3-6470c40ebb35 | -7.32328 | -59.61776 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13754153-53cb-3e0b-b909-569e7308f5e5 | -6.64326 | -59.0927 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93634a30-fd12-3f12-97de-fedc947ff676 | -6.82705 | -59.25623 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d56fd729-1460-369c-9ad8-9aac1f17b765 | -6.7315 | -59.17606 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d4087b68-6cd6-35c9-8610-b074a9f8f1a2 | -6.81804 | -59.26736 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 9bfec776-0059-3864-b1c2-19da34a75e72 | -7.32914 | -59.62676 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7963252-9d14-3f43-a8c3-3f36b3e05f94 | -8.66451 | -63.85193 | 2025-08-01 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1b23c8b-8d54-303c-b5c8-424f020715d2 | -9.45727 | -57.83993 | 2025-08-01 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 99fb3841-3960-3003-aa1c-118ccce8c9f7 | -11.52184 | -58.00238 | 2025-08-01 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c657b778-10f7-3f05-8d41-9bb16bb7cc3e | -6.74243 | -59.1526 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a06297d5-41a5-38e5-9dca-e6e828e30d91 | -9.45277 | -57.8428 | 2025-08-01 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c88f2bdf-01e4-389f-9d4f-5f7ca099f500 | -6.73884 | -59.15203 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d9f3eae-57d1-3778-8e7f-719dd0bf9c0b | -6.81742 | -59.2714 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c6c2b6cc-60db-3156-b75c-feb2aef3d810 | -10.09767 | -63.1903 | 2025-08-01 05:31:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f736bd9e-2be8-38ba-9661-96f8eb54dd1d | -7.32207 | -59.62569 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 560cda4f-cb29-3749-b9d4-eb7549611ba4 | -6.81989 | -59.25518 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee2d9b87-1da6-303e-b07f-6860ad590d4e | -6.74117 | -59.1608 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 690c2111-0d5f-3ce5-b9a3-211474fddb04 | -6.74834 | -59.16198 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5fe3f744-7ac1-354f-b068-13c39f6c6b5e | -7.07816 | -60.04613 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ee8f675-dd12-38f6-93b7-db5f37a7e5bf | -6.64686 | -59.09325 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| e0846dad-a38a-3ff8-bed2-1b86aaad14d1 | -6.73571 | -59.17252 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ce69f57f-f4f0-3d07-8e05-818f3f7dc952 | -6.73992 | -59.16899 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 11ef11da-6526-352b-be7e-89cedd242f87 | -6.62122 | -59.9873 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ac8c02e-69b4-3b95-af16-1ea1a33880d0 | -6.61892 | -59.97924 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 28736fe7-e3ba-3059-b587-df01e77436e0 | -6.61951 | -59.97546 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9c42a9c5-a2ae-3106-85f3-01f09eb7cde5 | -6.62009 | -59.97168 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cd59f3e3-cb8f-3ee0-a0a6-02168c97c621 | -6.64559 | -59.10155 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8db754c5-f30d-3569-9998-e71480136cb8 | -6.96066 | -56.38142 | 2025-08-01 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff3887fc-65b6-3b48-b9f1-41345b926a7d | -10.10852 | -58.22628 | 2025-08-01 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83f3dd6a-8d27-3ffd-bb1e-1b6fa777d858 | -7.72515 | -66.353 | 2025-08-01 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fe2643d-bd4c-3a26-ab37-7c98c9d2a333 | -6.82813 | -59.27309 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 7e363e4d-d240-31f5-b392-2bcd51711c86 | -6.957 | -56.37673 | 2025-08-01 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 097dae02-0eb4-3fc4-a6b8-9b4b4901fdda | -6.7418 | -59.1567 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60313567-1141-31b1-a4e4-bbdb1c560db0 | -6.64622 | -59.0974 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| ea52a74a-564c-3234-9bc6-9969f7555fb7 | -6.82099 | -59.27198 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 9cc64dbe-3ab2-3280-be76-739efa36975a | -6.73088 | -59.18016 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 86b45ae1-2ad3-37fa-8d63-ec3726807b98 | -6.74476 | -59.16138 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4d56d639-9831-318e-8788-924ccf22d402 | -6.68253 | -58.85994 | 2025-08-01 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8c07d5b-8678-3da7-a939-02c7e11a0180 | -10.34593 | -56.49009 | 2025-08-01 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e79d2167-287b-3c0d-aae0-2fc7e54019b9 | -6.74288 | -59.17365 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fad58290-999b-35aa-bca9-480e6fe55db3 | -6.83358 | -59.26141 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| e3fe225d-0a12-3bd4-a4ad-70b0e79dd4e0 | -8.12017 | -65.43766 | 2025-08-01 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c85e0eb7-d031-3e13-be0a-64fe5604bc05 | -6.81385 | -59.27084 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c9d10e19-f670-30ee-b28a-1b55065e2fe8 | -7.3256 | -59.62622 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40c6d125-02fb-3c81-a196-3b1004bb3857 | -6.73508 | -59.17662 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 19de522b-c650-34b4-8afc-31ee7ecb4372 | -6.73462 | -59.15561 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d0fe51d-8e57-33ef-a7ab-6914b7a38e36 | -6.73634 | -59.16842 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5187d543-417e-35cb-9633-67a0a0f2ffad | -11.90201 | -55.88629 | 2025-08-01 05:31:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6162a75-3a02-335a-ac0b-50e17046afdd | -6.72791 | -59.17552 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3630f43f-ab38-3007-90a9-26f7e91855f4 | -10.11172 | -58.23198 | 2025-08-01 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| debd822a-81f3-379c-a441-15cf1ad3091f | -6.82456 | -59.27253 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 8fab892b-1540-3e51-bf14-116a4eb3ff3a | -6.8109 | -59.26623 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cad57a4-b946-3de5-b0f3-87b9c88c5d92 | -11.33198 | -58.5879 | 2025-08-01 05:31:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38dea462-67c0-3c5c-9b37-b410d9544e0e | -10.10778 | -58.23138 | 2025-08-01 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f694fc65-7b52-31d8-b999-b06906ba8f2b | -9.53339 | -62.06978 | 2025-08-01 05:31:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e55f6da-dcbb-3356-881e-615d0d86c74e | -6.81508 | -59.26274 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 4dc46926-d6c4-33e1-8f6a-81bc535a7055 | -7.32682 | -59.61829 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11e6d1c1-32b9-3f48-a80b-f58228bda5f0 | -6.74055 | -59.1649 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| cf1f5df7-7c1c-35cb-b795-866626109ac6 | -9.46078 | -57.84404 | 2025-08-01 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9d24eb6f-3049-396d-ab40-f66846988bae | -6.82642 | -59.26034 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 85e66830-1147-31ca-90ab-fda5a2e04e4c | -6.62526 | -59.98404 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33dd6cd3-8894-33ec-8faf-5b57f18eb3e4 | -6.7435 | -59.16957 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3ff2e156-cf7e-32bf-84fa-90d59ba7f66b | -7.0718 | -60.04128 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bafcc6c1-a1a8-3a49-a4c4-415028213046 | -6.72853 | -59.17144 | 2025-08-01 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0f18e8dc-218e-331f-a09d-24e9741c2fc2 | -6.62643 | -59.97648 | 2025-08-01 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README24.md)
