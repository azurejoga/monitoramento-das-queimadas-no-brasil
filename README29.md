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
| 702b1172-5ce2-3ed3-92f2-5fd46d920f27 | -3.2527 | -54.656799 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed1b5932-f921-380e-842d-155aab3534de | -3.8638 | -55.996601 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5593a190-b994-310a-b70b-544dda5a50b7 | -7.3926 | -46.219299 | 2026-10-08 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bff9bc85-198f-3358-afdd-88b21941eb8a | -3.5471 | -54.6847 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6693da70-1d5c-3735-a1f7-f36185330d94 | -3.0522 | -54.2729 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2ea301-e926-316b-853f-184271a02bc0 | -3.3481 | -50.480301 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43970825-af08-399f-9d73-0f9fb7141d91 | -3.0903 | -54.304901 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b33cbad-c7c2-35a5-9a30-ecb66983757c | -3.3595 | -50.4851 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1111699b-a2f6-3e8c-b6a4-22c756786d45 | -2.9881 | -54.1269 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca5fb734-1316-38b9-8f40-d4a009f06c04 | -1.5233 | -54.523701 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fc686d3-3831-3415-971f-3c2408e4eb09 | -3.4733 | -59.6059 | 2026-10-08 00:48:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 787f452e-1e70-32a0-a5f5-07f5cb8a1dd5 | -13.7911 | -52.8074 | 2026-10-08 00:48:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2418d1db-ab4d-3989-8a05-908f291d1419 | -1.2071 | -49.250702 | 2026-10-08 00:48:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b5265bd-aece-37e8-8f64-7a5b31cf98b9 | -3.2908 | -51.574299 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87b9479f-2bc0-3bb7-88f6-7b5e4c6c1def | -6.4563 | -55.473202 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 033996fc-10d1-32aa-b9f8-a878192503f4 | -2.9888 | -54.0397 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2717efdf-5eb0-3fd0-8559-aa16ebc0fc09 | -2.9523 | -54.150799 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e35ff9a9-649b-3a0b-9c25-5d41fb66d6f9 | -7.8922 | -54.727798 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfd41d5-6369-39a2-b5e2-1931f965a172 | -3.1374 | -54.375702 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2b490e6-67ad-3e0e-b295-26b064bc2362 | -6.0928 | -49.4132 | 2026-10-08 00:48:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 445d07a5-0fce-349b-ae0f-fec154dc1f76 | -2.8261 | -54.139 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3d9b001-3fd6-3eab-9011-966ad78e23a4 | -3.3611 | -50.492199 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a462353-fdda-3443-82d0-455c11f1a137 | -4.2468 | -50.753899 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f641c5a2-ff7f-3297-9c77-28944019a829 | -6.2302 | -52.848202 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f10cb2e0-b509-3707-97ff-ad5a0da9e95f | -3.4402 | -56.943298 | 2026-10-08 00:48:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b00e5ad-8793-33b6-b490-6fcff12f808f | -3.5239 | -54.672901 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae27057-71c6-3326-9f22-9213ff9fdee4 | -3.3064 | -54.712399 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63154ecd-a48b-320a-9180-8ec8d31ea2db | -3.1178 | -53.792099 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd721b44-b636-34c2-a332-456b2ea49e19 | -3.7122 | -54.2323 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d9c475-3afd-3fe9-bc4d-38ec04f33a5e | -6.8795 | -43.688801 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c73c61d-410a-3959-9e7e-6f78ae7543f9 | -5.7068 | -53.494099 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1898afef-6efb-328e-958d-4dce2608bad5 | -3.1651 | -50.447399 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe03d19b-cabf-3f50-8b5d-2585a10a72bf | -2.4681 | -56.094799 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64453d1b-cfa2-312e-8937-00b99827a031 | -3.055 | -53.922798 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d06f42c-1009-3b12-9792-5913f128e144 | -11.5332 | -47.599701 | 2026-10-08 00:48:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ecf8d6a1-5fc4-3957-b511-4eaca00ddebb | -3.0384 | -54.528999 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d831292f-321c-353c-9ed4-bf74b8f5c9c6 | -6.1769 | -39.433701 | 2026-10-08 00:48:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ed6cdc73-8be6-3976-ac73-3ab514bead9c | -3.0932 | -54.2719 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4053ccbd-4fec-3f2b-85f0-0b323a4f8a30 | -3.9649 | -56.126999 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7f617fc-3407-3c33-982b-f512098428be | -3.1047 | -53.779499 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87d81c8d-82a5-37d3-960f-4b94404c29b5 | -2.9356 | -54.1227 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69b47414-dbaf-37e6-8690-bf9bd3b506dd | -6.3627 | -43.346699 | 2026-10-08 00:48:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 831a9640-98ce-3ce0-93bd-3e848e33d8a0 | -5.7364 | -45.167702 | 2026-10-08 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 454765a9-c269-3b95-81f9-e4c1e2e95c5c | -3.0117 | -54.185501 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7da7b34c-d510-3b31-8b05-3ccfb5180f83 | -10.4371 | -47.2897 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4177b956-d7e4-3761-98ee-43b296329ff0 | -3.2643 | -54.0737 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8157032-6040-359f-93ef-98713a7a8956 | -2.7697 | -54.072399 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c0d82eb-4937-3f3b-b007-12b863cf99e0 | -3.2921 | -54.059601 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f066ebed-a8b2-3b20-b1ae-7245733a539f | -10.3051 | -46.605801 | 2026-10-08 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67f884bf-d0f6-355a-9963-a408bc039ae1 | -3.533 | -59.5075 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 580ab539-d0b8-372d-bab8-40fae50e80d6 | 1.7079 | -55.619999 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4263b7-92b7-3b67-b09c-1af515e5fdb2 | -13.7972 | -52.787899 | 2026-10-08 00:48:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c98162e7-8dee-3b34-996c-a7fa4e412683 | -4.2972 | -50.7934 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9814fc65-a809-3a0d-9752-11ae89665eb6 | -8.3946 | -46.307499 | 2026-10-08 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51d2ab34-0227-3894-9295-b365530a355a | -3.5877 | -54.591202 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b091e9a5-8eb4-373e-a66a-17a938605cff | -8.3923 | -46.298 | 2026-10-08 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4660fe9a-9b66-33c4-8ab4-238bf15a6a8a | -14.9359 | -48.109001 | 2026-10-08 00:48:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd17dd67-122c-35ef-a639-017d684204f8 | -3.5072 | -59.345699 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83a4fc7a-56f8-3e72-b7f3-205073b03d26 | -14.9699 | -47.540501 | 2026-10-08 00:48:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5741aae6-878d-3e7c-aef6-50411081dd11 | -4.8021 | -54.685001 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6e85059-97e1-3b95-a94b-d9fc72c11c39 | -4.1046 | -59.878899 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ccd054a6-67cf-3a3e-9aef-7e909e09665c | -2.4702 | -56.104099 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a8c6ea3-05a7-3c28-9617-5c71fa9d9e37 | -6.2385 | -52.884701 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57359393-0d61-362b-93ce-a7dc386d7006 | -2.8341 | -57.485298 | 2026-10-08 00:48:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89d2295c-9a26-397d-bbf3-b69daadac6f8 | -2.5066 | -56.2644 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 740a9d6f-2ad2-38fe-9100-d4781d92e9e5 | -3.0174 | -53.938999 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21ac2b84-f413-31df-a278-40d536c56446 | -3.2107 | -50.555698 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec62b0df-6e57-317d-9413-b1530a4b247b | -3.1705 | -53.842602 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 704ba597-8d38-3c4a-8f6e-96c89c6199f1 | -2.8192 | -54.108799 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad295133-043d-301f-945d-937088a42118 | -2.9944 | -54.1096 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29868d1b-1951-3df8-a01e-ea0eb4853f43 | -2.9691 | -54.179001 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6b2d157-f8d2-335c-a0e8-dfa4f1ace21b | -7.4785 | -42.866001 | 2026-10-08 00:48:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 880fa02b-b3d2-345c-9ea5-e594a3cbafca | -3.7345 | -51.216202 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9be5ef-782a-3dd7-860b-5ced7e155363 | -0.8491 | -51.855999 | 2026-10-08 00:48:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7826e479-4be3-3fda-988c-01296190b2c2 | -2.2514 | -51.943199 | 2026-10-08 00:48:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 671fd080-6883-367b-8735-bf669c21453d | -6.5078 | -55.381199 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a139a22c-8641-32ad-af09-43ce39d9b84c | -4.2349 | -49.9884 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33f9a1d6-b526-3106-b9c0-2c6d53746cb3 | -3.5355 | -54.678799 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15252bee-d945-32fc-9e92-b1d0a5d50918 | -3.5318 | -54.662701 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efa1c18c-d4fb-3f18-a7f6-1bcc29279897 | -2.4583 | -56.096901 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79063a08-0a7e-3ba3-bce7-0dc513ca4cbc | -3.0008 | -53.9114 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3616638-16f6-3ea3-805c-78172afeee95 | -9.8404 | -47.474499 | 2026-10-08 00:48:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 901540d4-fe48-3ea4-8517-87ca35d88f90 | -3.5435 | -54.668598 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6e1884f-32f1-3a01-b3dd-a11c2fe21558 | -13.8414 | -49.692299 | 2026-10-08 00:48:00 | METOP-C | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 01604771-9842-3e56-bbb6-6310e6ef7ac6 | -12.4913 | -49.555401 | 2026-10-08 00:48:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7479f22-6215-3a2d-830d-76a200335cea | -3.2788 | -54.0467 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83295602-eaac-3536-9cde-1d1ce6b4b346 | -3.4304 | -56.9454 | 2026-10-08 00:48:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7194db1-0f83-391a-b31d-1ce4b1d852d3 | 3.5422 | -51.274899 | 2026-10-08 00:48:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5a7860-2d49-347f-8a16-0942e12fd887 | -1.5302 | -54.554199 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffea422f-57ce-3b6c-a00f-ef8e76246386 | -6.4981 | -55.383301 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0c040c7-0759-3752-9a69-2e8a6cb2ca12 | -11.3538 | -51.881599 | 2026-10-08 00:48:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 315c5a2e-a63c-3ac2-84e3-621d7c77473e | -3.0963 | -53.742699 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50661fc7-4da0-32f1-a8f9-e6107ecb530c | -13.3729 | -43.880901 | 2026-10-08 00:48:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 876e9382-ea2e-3a07-a7af-778b95d68e1a | -6.9026 | -43.698799 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b245ae2b-a0a1-375a-9490-244d0f188a2d | -13.1678 | -54.321602 | 2026-10-08 00:48:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4133e60b-de72-38e8-ae31-29d9a44b628a | -3.2904 | -54.052101 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723b5be2-9a64-3c01-aaab-a40aaef3a5d8 | -2.8705 | -54.153 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6a3c7ec-c209-322e-9e84-46e8b0b5e105 | -2.3842 | -56.132801 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59db8a6e-822f-3d6f-bb20-557ba3a9fd86 | -3.1895 | -50.553101 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48b1bc4a-f24a-3bba-860c-6166fd4fe7a5 | -2.6548 | -52.5779 | 2026-10-08 00:48:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README30.md)
