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
| d91e7351-70c2-3aee-bf14-b573dd0e316f | -6.005 | -53.506901 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a597cc22-7dc7-392c-8a27-b81e903c4eb2 | -4.2685 | -46.3577 | 2026-10-04 00:09:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9df20c9a-45cd-35e1-891e-7c5641852e41 | -0.4966 | -49.103401 | 2026-10-04 00:09:00 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 567288f5-78c3-325e-9681-ce846c06bf1a | 1.9126 | -55.746399 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 088f2608-fadc-3e3a-ae80-1349400bcf17 | 1.7728 | -55.637402 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 867b8cf1-6775-3af2-907b-49ac703e8787 | 1.7672 | -55.616901 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0f2d37d-0253-3414-93e3-e0d3ad652a6e | -2.0007 | -55.959801 | 2026-10-04 00:09:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d32ebb5d-f1d5-3892-b87f-c82f43ea31e2 | -2.9022 | -49.392899 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 437b5c6b-f320-3eb4-b672-e6e67a68348e | -4.9763 | -46.032299 | 2026-10-04 00:09:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2cb5272-3416-31ee-86e0-0b15626e4234 | -5.2649 | -47.907001 | 2026-10-04 00:09:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af9ade69-715a-32c2-b87d-35d5e383973b | 2.1002 | -50.745998 | 2026-10-04 00:09:00 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 496c20c8-59a0-34e9-815e-b0e2888f9f87 | -3.0152 | -53.877701 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1e87da7-b2ae-3aaf-a427-aa1b3ea1925e | -2.9727 | -54.1021 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 595ee4ea-7341-3246-8c88-5198477b0823 | -3.1824 | -54.074501 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 713a43d3-19b7-3c35-b0fd-08eb1dce7f21 | -3.5025 | -54.590099 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bee7eee-8bcb-3e87-ac0c-b72b22e2197b | -4.2761 | -50.269901 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19e745d8-c8b7-31fe-a482-6a43ef2082a9 | -2.9806 | -54.091301 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae36b47-4a0c-3de1-811b-66f2708fe1ed | -2.9247 | -53.932999 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4009a59-3f50-3ab8-855e-4b4e5d62aa2f | -2.9531 | -54.1064 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82701234-13f4-3fd0-981e-f7fa7d466d30 | -2.8216 | -50.493301 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd256d95-ed3a-3467-9d60-254f564ef81b | -13.3706 | -41.334599 | 2026-10-04 00:09:00 | METOP-B | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7e973a5f-b8a4-32de-bc3b-6deb1633af47 | -4.2703 | -49.970299 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaa90da6-68e3-3101-9547-4ea90904434a | -4.2718 | -49.9771 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d60cd326-1c86-3890-88d9-45b090b7c857 | -5.7401 | -45.1549 | 2026-10-04 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1265f37-32aa-30a9-921e-a7dafc4cbcce | -3.4744 | -50.097599 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad51eb4-9fb8-3897-b98b-e254a9cb97b5 | -1.8561 | -47.966999 | 2026-10-04 00:09:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e5e4ae3-95e7-31d5-97b0-025498c75fe2 | -2.0218 | -46.934799 | 2026-10-04 00:09:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b23dffc9-06c9-3943-9607-ff0a5ff26d39 | -3.2095 | -50.750301 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d1998dc-5059-307d-bf2b-759246b6291d | -3.7132 | -50.652802 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a71c18d9-062b-31d8-8e4c-49472fa4f7e3 | -3.9413 | -48.4319 | 2026-10-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 545cf375-13b2-3c2e-b6d0-f7d017e0d37c | -2.8141 | -54.0825 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 508a33b2-8ebf-3fcc-aa8a-1b20c053a29c | -4.2875 | -50.274502 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85722c45-e8e2-3a8b-886d-da3014664750 | -2.8253 | -50.463902 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca18faa6-01e8-399b-9513-6232877cab45 | -4.5434 | -55.965401 | 2026-10-04 00:09:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcd3311d-133c-3c03-8a23-56c0fe349ab6 | -3.0807 | -49.543201 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73164a74-aecd-3242-bbb0-b31bd631126e | -2.8218 | -54.117001 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb9764bf-9b5f-3425-b25b-d7a8e0e80bc4 | -5.9952 | -53.509102 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27136927-34ee-3fe0-8daf-15b954d8a6c4 | -3.1164 | -53.732498 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f292d412-0eab-350d-bbb3-90ec8789abb8 | -2.1109 | -48.995602 | 2026-10-04 00:09:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a82ae45-8d11-3f27-bf7c-8c743404b474 | -3.887 | -49.689201 | 2026-10-04 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90b4e0dd-9cf2-331a-9d52-d82ee4935206 | -2.2255 | -53.7038 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb319e0-19db-3be2-a1a0-5aff888574c5 | 3.4301 | -51.2939 | 2026-10-04 00:09:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 574bb482-e6a9-38a7-8669-b8b2047abee7 | -1.9983 | -55.949001 | 2026-10-04 00:09:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2c17c57-a472-3c92-aa57-56e229a34928 | 3.3671 | -51.3447 | 2026-10-04 00:09:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 77f09910-9a9d-3bd4-ab55-c3927b37bf82 | -2.9298 | -48.743698 | 2026-10-04 00:09:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33c42bfa-c392-356f-84c7-f4f875f973c0 | -4.7124 | -56.1301 | 2026-10-04 00:09:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fed80c6-6c0c-373e-9daa-c8f929b0e837 | -3.0431 | -54.187302 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c83bd58-2797-37e7-91ff-3ca1f4ef93ae | -3.5091 | -52.956799 | 2026-10-04 00:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba17aa1-6b97-3b31-9d0c-239e762e0a54 | -3.869 | -55.785 | 2026-10-04 00:09:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fe8e307-7673-3129-9f0e-4e0fe3636e31 | -3.463 | -50.092999 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afc1eec2-6b55-309f-9f08-bb64c07716e3 | -0.3627 | -52.065399 | 2026-10-04 00:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb8e747-2a79-3eb4-a8fe-da58e8958f32 | -5.5373 | -44.207298 | 2026-10-04 00:09:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da1fcc64-3c16-3907-893a-0ada69a3724e | -4.1497 | -47.5406 | 2026-10-04 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94310163-bccd-35dc-9201-4b8247dca016 | -3.1843 | -54.083199 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3c78407-1c01-3e34-9230-678cae88b2cb | -2.5835 | -51.859402 | 2026-10-04 00:09:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 905a9b77-f8d1-3848-8265-5a942f79a43b | -3.2799 | -53.819901 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adeb7144-9be9-316d-b714-f728dad8c7a2 | -2.2467 | -51.919102 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 445c5487-0e79-37f1-8cfc-c2e65988ec82 | -4.4811 | -45.5429 | 2026-10-04 00:09:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd30ce1f-8517-36f9-8853-0b6c0b65280d | -4.2053 | -53.451099 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9ca13e4-70ba-3968-af0c-dc332a6a37a4 | -1.1186 | -54.136398 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2eab79-04c2-36bb-af7b-8e1c403fc695 | -2.8081 | -54.101898 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66d6b947-adf0-3108-81b2-bd69319d4f8a | -6.0581 | -53.467999 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0312436-ffd5-3408-b983-b49c27b936ad | -2.816 | -54.091099 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 577eaa0b-0caf-3e01-8696-2b39ae4eb3db | -4.4788 | -45.532902 | 2026-10-04 00:09:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45f6d360-febe-3c79-b32e-fdedd19a8997 | -2.8024 | -54.076099 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa06c8b7-e500-3c6a-9ba9-d7ee4e6b0607 | 1.9105 | -55.7556 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9449adaf-7328-3478-bdba-80a9583ca16a | -1.0236 | -49.245899 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62f1369a-0234-315b-8f58-962a22f0c9ea | -3.1029 | -53.717999 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69018e09-a4b3-3c2f-9bed-5ac84a434fa1 | -3.4646 | -50.0998 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e0ba76-fcaf-3c1f-987d-0acc89d044ac | -2.8438 | -51.276901 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca8fec5-b24e-38b5-9e06-aacb65a3f374 | -2.5309 | -58.018501 | 2026-10-04 00:09:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01cc7deb-89eb-3504-83aa-04c7b2149885 | -1.1014 | -54.105598 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4746ef50-874d-3474-b2e3-4eb2fb44a8c5 | 1.9168 | -55.727798 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a671182-17b2-31bb-ab8f-2f3512fcb12a | -2.1093 | -48.9884 | 2026-10-04 00:09:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7bfc39d-cc7a-3de9-be09-cbb7680b4c2d | -5.9929 | -53.639198 | 2026-10-04 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dddfd02-fde1-3510-b577-0bfe335606dd | -4.1266 | -46.8139 | 2026-10-04 00:09:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d6ca4e0-4d82-3aa5-86d9-8afab269be63 | -1.0977 | -54.0891 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd9e98c-4882-3336-9768-942486401b9f | -2.3603 | -50.595798 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71f33440-a80b-3b9e-baa7-cc18746b5d8d | -3.1966 | -50.7388 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbdd6df1-00cc-3f50-81ad-0a465ff8d99c | -6.5704 | -44.1329 | 2026-10-04 00:09:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9133d4d2-c5f8-39dc-ba52-9b5cb9f97847 | -4.8162 | -49.877102 | 2026-10-04 00:09:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cac202c-6baf-3f67-bb82-2906f72f7d16 | -8.5129 | -48.901901 | 2026-10-04 00:09:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 63cb235b-c579-341a-a712-b1a4d7d9fc7b | -2.2218 | -53.687599 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9949cad-5e78-3998-ab2d-0987ac7fa48c | -3.8592 | -55.787102 | 2026-10-04 00:09:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7a9989d-d8cc-3e83-a7a1-ee095d1902da | -7.0128 | -47.523499 | 2026-10-04 00:09:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fae03d6-5b28-3b3e-943a-37eed4693d3d | -4.5265 | -49.690399 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41e7eb45-ddfb-3467-bd45-775a330df847 | -15.2374 | -40.532501 | 2026-10-04 00:09:00 | METOP-B | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61d3a811-026e-3f06-b0e9-024cf68365e0 | -3.0014 | -50.467602 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 807f4a38-faa7-3ad2-9be9-e9ea7a9681d6 | -6.1977 | -52.793598 | 2026-10-04 00:09:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 266f7a95-b24f-3113-a20b-c105db41b868 | -4.2777 | -50.276699 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79cc907b-c3dd-391c-8446-ad82dcd0bb3a | -5.8643 | -43.590401 | 2026-10-04 00:09:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 963aac67-804b-3ac1-b8c5-b57b1a9bc9e8 | -3.1342 | -53.719898 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 587396de-3284-3d4d-9344-185bb907f8cc | -1.4891 | -49.435001 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5508e900-502e-3470-992d-c7a3709724e0 | -3.1882 | -54.100601 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7dc0dc-05ba-3e66-aa05-cb5baf275b6d | -4.4561 | -50.977699 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae9e1f18-24ab-3932-ac38-a43639b7136e | -3.5123 | -54.588001 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff50d5a8-04f8-3b2b-9b7e-244863fe410b | -4.1286 | -46.822399 | 2026-10-04 00:09:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3450a7-3805-35fd-bcb3-ad33f7cf7a40 | -1.6216 | -55.001202 | 2026-10-04 00:09:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04e97226-c785-3ec4-80ff-37873e12057b | -3.1066 | -53.7346 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df73fe88-7d4e-365a-9053-20bb6f928ce1 | -2.8314 | -54.206001 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
