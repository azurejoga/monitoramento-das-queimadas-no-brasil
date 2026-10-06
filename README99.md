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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e552f1dc-28c1-39db-986d-ed9a58aab531 | -11.6946 | -43.6787 | 2026-10-06 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 1cd0e1be-1be1-3b56-8186-5e610fb7cdf0 | -9.0892 | -67.685 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 314.2 |
| 09a4ed45-3843-323c-b344-077892b17160 | -10.7361 | -69.609 | 2026-10-06 18:20:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e866f428-943e-396b-892f-2992456b3cf1 | -9.1334 | -65.9 | 2026-10-06 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| f910bb0a-e4af-39ec-bc63-5619cdeb6ca8 | 1.7304 | -55.6061 | 2026-10-06 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2d6b32ab-9436-3df7-aeba-ee256abfcdad | -3.9798 | -42.8688 | 2026-10-06 18:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 118.2 |
| fbae2990-7286-39c7-a652-36b40ebb6f9c | -8.573 | -67.2163 | 2026-10-06 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| bdbd1ad9-6818-3855-9f72-4eeeba8218d0 | -4.0737 | -48.9622 | 2026-10-06 18:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 58ec0755-9bb4-3cc5-a04d-dd5d911db00f | -11.6951 | -43.655 | 2026-10-06 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 2ba163bf-b7de-31ee-b98f-75f525472c7d | -11.0485 | -45.6511 | 2026-10-06 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5058a637-9347-3fa5-9620-593b60dd063a | -6.8764 | -43.685 | 2026-10-06 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 7133e8fe-af11-3d66-bd16-df837986db43 | -11.6946 | -43.6787 | 2026-10-06 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| e3678d4a-4c47-386f-85e3-52b02ccac2a9 | -3.0461 | -65.0844 | 2026-10-06 18:30:00 | GOES-19 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 191088c2-484d-3b40-90d0-7ad7e593e21c | -11.6374 | -43.664 | 2026-10-06 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e7844d73-99d1-3bfe-a674-8e8781b17bb5 | -4.1416 | -46.8331 | 2026-10-06 18:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 846fcdf3-cc59-3478-a3f0-3885c4578045 | -9.1055 | -68.3135 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| d0ed703b-a934-37d9-ba93-747d659e7f28 | -9.0705 | -67.741 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 94a87e63-d464-3a7a-86f3-71ecef84c3f2 | -9.1242 | -68.2761 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 5f8c273a-f766-3109-ab42-1cbfeac63d7a | -3.3607 | -43.3893 | 2026-10-06 18:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 473.9 |
| 5a0cf0a5-5e6e-3aae-af95-4d9545778566 | 3.5263 | -51.2778 | 2026-10-06 18:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 27b87270-a5f5-3a1b-abaf-1850f4509a28 | -9.6049 | -68.5979 | 2026-10-06 18:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 92.9 |
| b90e875b-b4d3-36bb-b4f0-49c64adddaf2 | -9.1077 | -67.6845 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| f0b2d895-185c-3976-a42a-27f4458e85f2 | -9.0892 | -67.6665 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 413620d6-88ec-3fd7-ba6b-8194e14ff02a | -9.2366 | -67.885 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 24d5df16-600f-3776-ad1e-157ce94e4085 | 1.7304 | -55.6259 | 2026-10-06 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b19063b5-6948-3219-88b9-67d5b6d8c352 | -11.7143 | -43.652 | 2026-10-06 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 38b0e4e0-36c0-3e2c-b635-4fd709daebae | -8.5367 | -67.0505 | 2026-10-06 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 21c902e2-76a1-30f2-b0ec-b973ad8b81bc | -4.2967 | -42.9915 | 2026-10-06 18:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 6c9e67da-ffa8-3dc3-8eb8-dc34e9421fe0 | -5.4174 | -39.1062 | 2026-10-06 18:30:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 203d4f88-6485-39be-94df-ee3654426827 | -5.7378 | -45.1307 | 2026-10-06 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 163be455-eb2f-3a5d-8373-322a978dcd93 | -6.6217 | -37.8923 | 2026-10-06 18:30:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 322ae832-6a09-3948-a04e-a08b190ba4a8 | -9.5151 | -67.7484 | 2026-10-06 18:30:00 | GOES-19 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 3dfa400c-f2ee-3283-8e10-ed95fda2e9d7 | -9.0705 | -67.7225 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 16fee484-59ab-3b65-be16-2f29dd2123b9 | -9.4621 | -67.0817 | 2026-10-06 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 5453edff-e587-35ba-8618-7055c4d638b2 | -9.7686 | -65.0556 | 2026-10-06 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 141.4 |
| f46c7673-05a7-3a01-a6d8-ce0a32356cfd | -5.7376 | -45.1533 | 2026-10-06 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 962.9 |
| 1a68a964-ca83-3d3c-9126-ca89a484a13b | -5.7563 | -45.152 | 2026-10-06 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| ebba64ce-737d-3f2b-aa7d-7d8d45e31429 | -11.4507 | -43.3854 | 2026-10-06 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 1db8f9b3-0bff-322b-96bc-bf9482bb0f28 | -3.1951 | -42.9538 | 2026-10-06 18:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 010deb4c-c682-350b-8b51-92e53efccab2 | -8.9188 | -68.8527 | 2026-10-06 18:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 347c039d-cacf-3c19-bc24-8d0b217458b6 | -9.1333 | -65.9186 | 2026-10-06 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 1eed0637-01aa-330d-8ce4-4bf184e4ce06 | -9.1885 | -66.0102 | 2026-10-06 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| a1da8ada-bd38-339b-9019-70b1a0559af5 | -7.8356 | -45.3175 | 2026-10-06 18:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4e0ac816-bf0f-31a2-b45d-ebe20aedd65d | -5.5148 | -42.8164 | 2026-10-06 18:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 145.9 |
| 6d51711f-086c-396c-a0a3-113953bb89ba | -7.5657 | -73.0437 | 2026-10-06 18:30:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 542ae016-77a4-3c4a-91a3-fe60d5bbbfa2 | -8.2495 | -70.8289 | 2026-10-06 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 8647d293-4ba2-3e4e-aa1a-a21c41544ad7 | -8.1949 | -70.4634 | 2026-10-06 18:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 67a0a696-49bb-36be-b23b-f7f744b085e4 | -9.8824 | -44.8171 | 2026-10-06 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 385.5 |
| 3e26ab60-ff3e-301b-b7a1-fdede4bcdab9 | -6.914 | -43.6816 | 2026-10-06 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 3d0fc7c3-087b-34f1-89fb-409dad282703 | -11.8216 | -47.3521 | 2026-10-06 18:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 0e5b0c5d-e8e1-3525-ae22-4fa26f0f28d1 | -7.8167 | -45.3193 | 2026-10-06 18:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 3eb56d68-1ce4-361e-ba9b-fa32be41fc63 | -7.817 | -45.2966 | 2026-10-06 18:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 49644235-b8ca-3c0e-a9ef-462aae9c837f | -6.9143 | -43.6583 | 2026-10-06 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| d92111b1-68c8-3a4c-84ab-e0ac6b8180ed | -9.96 | -43.481 | 2026-10-06 18:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| e6626cf8-cb75-3994-b175-0d67263dcf17 | -9.75 | -65.0562 | 2026-10-06 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 151.2 |
| d09e7ecc-d28e-3856-bbe4-9aeef799a6fb | -9.5468 | -64.8196 | 2026-10-06 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 281.9 |
| 92b4f359-a08c-390c-b2de-5c4eead03f32 | -7.695 | -72.4052 | 2026-10-06 18:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 89dded2a-0307-3d2e-b181-b34e7d071c36 | -3.7811 | -41.7675 | 2026-10-06 18:30:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| e626e89a-c5e0-3b1f-bd1a-cd6f4e13405c | -9.4565 | -64.3344 | 2026-10-06 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 32f11610-7e16-31fd-b9a4-d0c3a7c3e66f | -6.8952 | -43.6833 | 2026-10-06 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 2da3bd34-6c31-3db1-9acf-3cab5ce2d953 | -9.1256 | -67.8507 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| d0c08c51-4668-387b-8647-3450e4a36c85 | -7.6949 | -72.4235 | 2026-10-06 18:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 42451959-3b21-37cc-a393-6820a1046abc | -9.1076 | -67.703 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 6c34d247-8a06-3fe1-bf09-052533f16f2b | -9.1829 | -67.3861 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 26ba1314-6377-3e58-9b96-119fa8b1cb29 | -3.3923 | -44.4695 | 2026-10-06 18:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 79229b64-0ba1-3e3f-92d4-f85ba122e953 | -9.1253 | -67.9432 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 7898fbd3-8047-3b8f-84cb-22f3d335590c | -11.6387 | -43.5929 | 2026-10-06 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 214.1 |
| 53efbf5d-c8a0-3bcd-b619-e2f63117f792 | -9.1334 | -65.9 | 2026-10-06 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 1dfd78b1-d166-3eec-80b4-256daf54d589 | -5.496 | -42.8178 | 2026-10-06 18:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 628f09e9-9aca-31d1-9e63-43165b0851a4 | -8.7788 | -66.5804 | 2026-10-06 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 197.3 |
| c80b4660-8cfe-3b93-b54b-614fdd14bed9 | -9.2365 | -67.9035 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 0044ed3a-9390-3f7c-a339-ae6040933f1a | -12.7673 | -44.8904 | 2026-10-06 18:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 46e43ed2-46b3-34d5-9765-f96d4ccac5ba | -11.6951 | -43.655 | 2026-10-06 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 802a028e-1901-3709-a409-e2f32c1491bc | -9.4751 | -64.3336 | 2026-10-06 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 90e0ef07-a45f-3950-a7ca-efebb647392a | -7.4001 | -45.6072 | 2026-10-06 18:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3076d831-8d3e-3017-bed4-547cef0e23e4 | -8.563 | -70.8615 | 2026-10-06 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 6ba2e323-7a8f-326a-b0c2-93c065c3198d | -9.7687 | -65.0368 | 2026-10-06 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| b9b4c2fc-68e1-3dde-85e7-11a60c3b340b | -11.6378 | -43.6403 | 2026-10-06 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 97201c9a-28aa-3e49-8394-e47721fc17b5 | -11.6382 | -43.6166 | 2026-10-06 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 550.6 |
| 2c42f56b-dcb4-3bf0-b5bb-312f2f905f7d | -9.8634 | -44.8195 | 2026-10-06 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 55374f82-5d4c-3100-9bb2-07c1bc18cfc7 | -7.8682 | -44.169 | 2026-10-06 18:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 3b0cc717-1f12-3c4f-ae2f-b62ce409caa6 | -3.292 | -42.2673 | 2026-10-06 18:30:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 245.9 |
| 7767ca9f-1727-3457-afcc-b7707c4dd2a7 | -9.3634 | -68.7511 | 2026-10-06 18:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 85.3 |
| ec188750-501c-3393-8c1c-464f93c9577b | -9.3431 | -64.7143 | 2026-10-06 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 55de1c6b-6d13-32a8-8662-d43421c15c5e | -3.3793 | -43.3884 | 2026-10-06 18:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 9dca24b2-9041-3ccd-a231-1d84ad9b5b49 | -9.1072 | -67.8326 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 1cab0bdf-14dd-35e1-8b08-8db014d3d259 | -9.5469 | -64.8008 | 2026-10-06 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 50c89369-4648-3e51-ad26-1bc31f824897 | -5.7321 | -41.6349 | 2026-10-06 18:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 197.5 |
| 5b833eeb-08b8-3950-8387-086c1e9a0eb9 | -8.9188 | -68.8711 | 2026-10-06 18:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 2cb5f710-3465-3687-ba75-d23f861ec348 | 2.4585 | -50.8299 | 2026-10-06 18:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f6e4149f-aa0f-3515-9fe0-e4bd4286eee7 | -9.8844 | -64.2802 | 2026-10-06 18:30:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 47ea8cbd-37a5-3457-bc46-6fe1aa6adbf0 | -9.6048 | -68.6164 | 2026-10-06 18:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 874969e5-d5ac-36d5-b03e-86f5ea780f73 | -9.4819 | -66.7836 | 2026-10-06 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 1b428d89-bf2f-3f64-8307-3989454ac309 | -9.0892 | -67.685 | 2026-10-06 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 287.9 |
| f6515c48-153e-35f1-9638-247cc476acb1 | 1.7304 | -55.6061 | 2026-10-06 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 50e262d8-6131-3b16-a763-911a19d2dea8 | -3.3921 | -44.4923 | 2026-10-06 18:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 28dde0bb-d603-3713-921a-cff8c295069d | -7.47 | -42.8078 | 2026-10-06 18:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| d96d6cd3-b716-391c-8217-7768e7c4ab94 | -5.9838 | -40.9123 | 2026-10-06 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 258.1 |
| cf288c59-1a06-3c08-8361-7e230b8f560c | -11.8296 | -44.688 | 2026-10-06 18:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 65f7bcfa-8c15-397a-b44a-a320b37381ba | -3.342 | -43.3901 | 2026-10-06 18:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |


[Clique aqui para ver as próximas entradas](README100.md)
