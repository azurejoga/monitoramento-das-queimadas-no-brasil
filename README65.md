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
| af41f1de-fd1f-3afb-b5b2-931c79f914d6 | -7.67618 | -45.4871 | 2026-09-24 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96179938-1c38-3c77-9ed1-6876f67b4b64 | -10.09944 | -46.06803 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33e33515-9abc-3fa6-9c43-83b3b4a69117 | -6.89756 | -55.57768 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d285d99-ae04-3c7f-b5db-fd872a145902 | -4.47666 | -54.9709 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a7a629b-4538-3ff1-bf39-75f354e39ffd | -4.14882 | -60.79554 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aeaacde9-570a-3e2f-8e79-485412a7e53b | -3.76986 | -60.72739 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f301e79b-250a-374d-b32f-eac18dd8bd04 | -7.58871 | -57.65905 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd753eb2-b07a-393e-a6d7-39e196dc75e9 | -9.2348 | -47.37305 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54d58aa9-56ad-37ab-83d6-ad75ef165754 | -7.27067 | -46.79274 | 2026-09-24 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 451925d4-108c-344b-a858-c6af3e242dec | -2.38765 | -48.52138 | 2026-09-24 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6366bcc-3c3a-32d2-a8d0-f94b79d79cc2 | -3.71654 | -49.04418 | 2026-09-24 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faf86ea2-2d47-3d91-a490-446a4782a58b | -6.63507 | -59.93633 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| edb845e8-c4e6-30a2-a0c8-0b088eaeea99 | -4.99225 | -45.54926 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c50e717e-454d-3c2e-8424-aa7a96cfe658 | -6.7158 | -44.15416 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e10d1909-58a0-36fa-9282-e0301928c45d | -6.77719 | -48.67298 | 2026-09-24 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88451b08-7cbe-31df-869f-c13e10e7c412 | -4.06661 | -52.12724 | 2026-09-24 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91e4f976-444b-31e8-bfb2-f09da60edfbb | -3.44622 | -50.072 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 09325233-9796-3a8d-8ab9-3576b532c592 | -7.88535 | -54.73019 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2c849ad-83b4-3e37-9619-7599e40fdc5b | -5.19492 | -50.0928 | 2026-09-24 05:04:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c76ea28-2ce8-3fb2-b73a-10799fdcaf7c | -6.51393 | -55.36423 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8932de20-2987-3971-a0bb-a8783ae0407c | -3.00614 | -51.53515 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e56555b8-f1fc-3b7c-b2e5-bdf15f70fcb1 | -4.99181 | -45.55237 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 019737d4-f4b4-330b-ae3f-c629d41a572a | -5.86599 | -51.95722 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2fd441f-a01a-3ced-9762-1de88425b4ac | -5.80169 | -57.5346 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e200501-8fd2-3ddf-80f6-1ab68f0fca06 | -7.09171 | -52.74619 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd492a98-a965-3b5f-9d24-c4c5588a5238 | -4.06679 | -59.86396 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcec5b79-260e-360d-a2d0-499b256bead4 | -6.51607 | -52.82359 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe687ac9-453f-3d38-a941-c342585b2439 | -1.62045 | -54.91706 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04e3c1c9-f716-323b-8331-8fed963f0cdb | -3.78815 | -60.75951 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d8d39be-9e1f-31fe-9134-6f42ba3782f5 | -8.12606 | -54.81868 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf3afd47-b696-3b44-97a0-e07176a9f735 | -3.48401 | -59.19579 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 038ff7eb-4ece-3821-97a9-d2ded91ce5cc | -6.60605 | -59.93143 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4232ff63-ba55-3993-9b82-6e00d31f4678 | -1.63267 | -55.12426 | 2026-09-24 05:04:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3791753e-1241-3395-b78f-66160729f13b | -4.25759 | -60.00879 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 785e91c1-fa4a-3e94-a4ab-cbfb26d000d1 | -7.88866 | -54.73071 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3bfaf05-0a65-34fd-8691-d40729fc78de | -1.83736 | -54.71582 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e924728-a018-3a1b-bed7-9637548536cc | -2.12773 | -49.53028 | 2026-09-24 05:04:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cc11b60-879f-3100-b1ac-2a5abb13e4e0 | -2.88447 | -54.08735 | 2026-09-24 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44783b50-74ba-3eed-aee5-74546346ce8d | -3.4523 | -50.08199 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e14cc8e-5121-30fb-a0ff-12b917f3cbf8 | -6.62263 | -59.93425 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daa657d1-eade-382e-ae76-794d53780a38 | -7.20305 | -47.45858 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bda2b152-a1dd-3410-9b59-3fe9f4325795 | -5.94346 | -57.74286 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cac76eb3-c434-355a-946e-6d519ddfcdcd | -3.55373 | -43.46424 | 2026-09-24 05:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9254fd05-803a-3c23-a2a4-3abcabf1e282 | -2.29798 | -47.88752 | 2026-09-24 05:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64531c61-7319-3c08-9485-74844138dde2 | -7.57084 | -57.65604 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a4e0293-80c2-31d6-a0b5-b8dbcae985de | -5.65576 | -60.21474 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb6ed763-0b72-30ae-a2f2-d00c9f9ba4b1 | -5.21862 | -60.05386 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 910b3148-787d-3a28-a5c4-f182d5075b70 | -6.66608 | -58.55351 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95ae1267-0652-3fbf-844d-27c4094a8846 | -1.84072 | -54.71636 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1d79e289-3e1d-3bde-93d7-bd9cea21e3c5 | -6.2413 | -60.0365 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fa79021-819f-3a5a-a912-68d64ae88874 | -4.55566 | -54.94348 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cbf84ea-7762-3a18-b4d3-1c50ea793ec1 | -6.51946 | -52.82412 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 259036b4-ccf1-3b1c-953b-979e21b5d5ec | -2.7138 | -57.51233 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dc55c314-04d2-3207-802c-eab819bfc04a | -6.12141 | -44.59883 | 2026-09-24 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2c7edb5-6057-3331-a824-4c307f22fa69 | -6.4625 | -55.00407 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 267e763a-ca4c-3f14-92da-7b72a250d6d8 | -2.62978 | -51.70298 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f73a9c72-140b-3208-ba4d-26a312301f1c | -7.19905 | -47.45329 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4715b0b6-615a-3225-9c46-75392a6713b2 | -6.43331 | -59.95657 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8ca8f362-a141-3765-aaf8-4027a36a4a67 | -3.44926 | -50.07699 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e178662-60aa-3ec7-9b89-bc401b204ccb | -4.301 | -49.13146 | 2026-09-24 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84b127f8-1800-3818-9a2d-919dae891853 | -1.62442 | -54.91397 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 005bb786-3842-3319-9075-aaa7d35c40f1 | -6.26675 | -43.12971 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 190a723a-e6e7-3dd1-b4c2-68169d4b2332 | -3.96232 | -59.34883 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d88e15e-3d33-3b00-abe2-4edd0fa58de5 | -3.45329 | -50.60984 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd938230-e822-3a4d-9d71-a39a7ada7a4c | -8.90329 | -45.90902 | 2026-09-24 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6f7d0cf-3954-3be3-bc95-6240c8ecc9f1 | -5.41995 | -60.24795 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e446ef47-d269-3c9f-bcf6-4e748b0089aa | -2.20409 | -48.15302 | 2026-09-24 05:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7557dfd-ff4e-3b15-a01c-5db7d92a614b | -5.59915 | -45.95306 | 2026-09-24 05:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd26d803-97ce-39ba-9d52-9025289ffbff | -4.11389 | -51.08189 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6d94d176-0d2f-3d39-bc98-98957f802695 | -2.57318 | -54.74298 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a8d4dd-15f8-35e9-9951-68d904109726 | -6.08309 | -57.62508 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7114f384-d9d3-389e-b434-f05c566ccc49 | -5.99231 | -57.72027 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de5c926a-f432-301a-9ded-749c276ea8b0 | -8.26244 | -54.77317 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04269241-9a26-337f-8f7b-6145378adc47 | -2.1688 | -48.32527 | 2026-09-24 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7093f94-423b-3652-99bf-b8432896bf76 | -3.78879 | -52.4254 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c18e73d7-cef9-3e25-b9d2-2dae1562ddb9 | -7.6076 | -57.61178 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a513e460-840e-32f8-9cca-92cb9af197de | -2.71127 | -57.5049 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6b974ba5-1cde-3a0b-8b48-7c6d7fb865de | -2.37382 | -47.98822 | 2026-09-24 05:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d7d7d45-61f0-3aba-ad3d-64bddc77725f | -4.47054 | -54.96636 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19f228ec-f738-3f61-a021-0f45e637fd46 | -5.14561 | -60.31663 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b611270-58d9-39ca-9362-acd1168156f6 | -7.19232 | -47.46759 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d264d1b-5cd7-3005-b9f1-cc3f55718f72 | -5.3301 | -48.98385 | 2026-09-24 05:04:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 251067a0-7fe0-323f-8462-ee1601e50233 | -7.4658 | -54.99738 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dfde88e-0e3b-339f-9cc3-c9f511cccd13 | -4.65779 | -54.47447 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b67779fe-d791-3b37-ad25-5285721d5128 | -5.24719 | -60.17123 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f479fab-a1bc-3d8d-846a-f7420b884ecb | -6.63092 | -59.93565 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6e928d5a-f9c6-3c96-a6df-5fcde5dfa698 | -4.1145 | -51.07792 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fd54507e-c453-332b-a51e-36b6f05825a3 | -9.25352 | -47.34307 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1fa72ec3-39ac-34e8-bdf2-37184673c229 | -3.06869 | -54.40392 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b845c7ab-b164-3066-b3d7-fa6361c207cd | -2.12678 | -49.53189 | 2026-09-24 05:04:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 428515c1-eded-3199-ad5a-14b07bb80e43 | -7.47477 | -44.57241 | 2026-09-24 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1510cdf3-af32-3877-90fe-3ac071690b2e | -6.67607 | -58.74596 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 140f7b32-26d3-35f4-bad3-86b0b45a2543 | -7.03989 | -51.39442 | 2026-09-24 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c98f2b54-9d69-3b37-b1ec-6ada1b99404d | -6.27268 | -43.27383 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9fff40e3-cdfb-3ce6-ac5f-05e465b80f47 | -3.41961 | -54.01317 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92664ef7-776f-30da-aa98-25d3e1aad4c2 | -2.40843 | -58.2714 | 2026-09-24 05:04:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eecbe57-b06e-3b6e-ae07-c7eea7918b27 | -4.11803 | -51.0786 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0ad362b1-57e0-3670-8d4c-dfef87877b7f | -6.44229 | -59.95416 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6316a0d0-b9ee-3a81-b8fc-ab17638eba6a | -6.08966 | -57.63051 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8ca4c5c9-a1ca-389b-a8ac-51687844e594 | -5.86504 | -60.15656 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README66.md)
