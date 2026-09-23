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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d85e41b-6059-3562-9e97-467d6f358efb | -12.802 | -50.865501 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1294cd55-b671-3931-b6e9-1eeb0073faa3 | -3.2339 | -46.958698 | 2026-09-23 00:58:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28e15933-857f-3491-a4e1-dae0c762bf0f | -5.8278 | -52.040401 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faf43d59-b5dd-312d-834f-c25da3cbc3d4 | -12.8037 | -50.8727 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 943ee11d-e414-3e51-9094-4b713b3ad3dd | -2.8646 | -57.783001 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9228545b-c283-302b-ab57-5482771a9009 | -10.2102 | -44.140301 | 2026-09-23 00:58:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 84955071-0e20-3ac4-9bd0-0a9cb458238c | -3.7037 | -60.550301 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f54e8c62-7d62-3033-90ff-4747f0262d47 | -5.7625 | -45.113201 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0902268-1a76-35b4-898d-f131b40cad14 | -7.1784 | -48.628399 | 2026-09-23 00:58:00 | METOP-C | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| aa22783c-ca3d-334f-81d7-61626759c942 | -11.711 | -50.925201 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e7e5007-1501-3545-a49e-7f2a37b6fa38 | -3.2399 | -46.941299 | 2026-09-23 00:58:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ceb03ee-eb68-3e64-977e-6550aa20e436 | -4.3294 | -55.437302 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8172b56d-b02f-3d51-b96c-cd2e598b56cb | -11.0094 | -54.143501 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1692a443-4670-3058-95eb-ce3540ab796f | -4.1511 | -60.767399 | 2026-09-23 00:58:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90d76e5d-ace1-39bb-a93f-f8ed8a11b309 | -2.4627 | -57.916 | 2026-09-23 00:58:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0ff271d-7816-3b8d-84fb-dde9b801fc4e | -5.8737 | -52.060398 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3b6c81b-d4e2-3bae-b255-9f49325b9bb8 | -2.8547 | -60.236 | 2026-09-23 00:58:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be9db206-7345-3ac2-91db-153138b31b87 | -12.7972 | -50.8895 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aebc9866-b71a-3aff-95ec-23cad94632a2 | -9.8567 | -48.300201 | 2026-09-23 00:58:00 | METOP-C | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c96b594e-0281-3fe4-a8df-841113ff6596 | -6.6036 | -59.927601 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbbf8bb-1ab8-3114-9f24-1dcae99f7861 | -11.6978 | -50.912998 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06c39ab7-6b66-3eea-94fb-6228b05e60bf | -13.3007 | -47.875198 | 2026-09-23 00:58:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e25eba9-6437-30db-a1fb-096c1893f947 | -12.4219 | -46.953201 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f266b0be-1864-3599-b775-5b8ee2d33108 | -6.7292 | -59.423901 | 2026-09-23 00:58:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f403d80-fd5f-317a-8bed-8b6d0ee18ac9 | -6.6998 | -59.947399 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 609c8357-6907-38a3-9b7b-a3b529e799c8 | -6.6106 | -59.9128 | 2026-09-23 00:58:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05702c3f-a1ab-3ed5-9662-f50edb122046 | -11.6998 | -50.966301 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9416dff-acf0-306c-9249-907b2046731c | -5.3993 | -49.0825 | 2026-09-23 00:58:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1089be1a-2585-3906-978d-4ec348d6735e | -8.1762 | -54.8214 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59ed53b7-c87a-357c-8186-ecf7285d3bae | -9.5293 | -45.352798 | 2026-09-23 00:58:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40b35598-4f67-387c-99d2-e6428c70e2d1 | -12.753 | -50.877102 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a18ea756-fa38-31d6-806e-9a37fcedae12 | -3.5905 | -50.020599 | 2026-09-23 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acf25ae0-1ee7-3c0a-9f7d-7dc3a499023a | -7.4254 | -49.833099 | 2026-09-23 00:58:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06a821a8-06d1-3795-bb28-bee42d2ba7aa | -14.3845 | -47.2281 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da79ec77-5148-3830-9549-6c9cfdbc67cf | -8.6145 | -54.617901 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455a07b8-fad2-36ec-be8a-e4a2629ec160 | -6.6746 | -55.057301 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 104b4bca-ad7c-395f-90e2-03f1ad0e4dbd | -14.6251 | -45.622601 | 2026-09-23 00:58:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33af6186-9986-34a9-b1d8-6502d3b5ee6d | -10.3046 | -50.520802 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1051181-6f35-34e5-ba7c-a7f8e42ba26c | -11.1078 | -48.301201 | 2026-09-23 00:58:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4f31279-9844-39b3-9199-d5ae3d8a7dd8 | -5.2798 | -47.256199 | 2026-09-23 00:58:00 | METOP-C | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38c62599-096d-3376-9e73-0cbb79f0943f | -6.3555 | -58.279202 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c528a700-72b0-3460-8b2b-189f5fbf7c30 | -2.4548 | -49.221401 | 2026-09-23 00:58:00 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30fb3a7f-13fc-3c49-bb73-564bc6d03235 | -12.7939 | -50.875 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a47fec61-d08c-33b1-b735-809cf9046c0d | -8.4458 | -55.013699 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84effc55-cc91-3912-be74-7019f3af73d5 | -2.937 | -57.784698 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e76e1c8-ad6a-337c-a6cc-655f74430b07 | -1.9215 | -58.2509 | 2026-09-23 00:58:00 | METOP-C | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b725733c-2088-324a-9917-4f0ddf560707 | -5.2896 | -47.253899 | 2026-09-23 00:58:00 | METOP-C | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2e47ca2-12e4-371c-847f-138cbb450590 | -8.2338 | -54.6651 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eeb6cf4-ac0f-3104-b1f6-a57138549e92 | 1.4341 | -50.813702 | 2026-09-23 00:58:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9febcd81-769a-328c-aa0b-b1ff1ab71a18 | -6.7904 | -48.6884 | 2026-09-23 00:58:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 16a12f5b-d45d-3bcc-8386-172e5f837b35 | -5.2471 | -48.188202 | 2026-09-23 00:58:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96d6f349-1e89-37df-892e-35edb3ae390f | -6.434 | -48.4506 | 2026-09-23 00:58:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d19b87b6-f3c8-3a41-a3e9-582445fbabba | -3.6871 | -60.567299 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5566f9a8-ab12-36be-8800-7800173fcbcc | 1.1731 | -60.364101 | 2026-09-23 00:58:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3662bba7-a702-36d9-af0b-ad17a650aa16 | -11.6782 | -50.917702 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1a12712-d1f5-3b65-8916-973326418834 | -11.9506 | -46.514801 | 2026-09-23 00:58:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83ea7bce-1f15-3b64-9ed9-41287ea0e295 | -3.0515 | -54.404499 | 2026-09-23 00:58:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d364289e-cb89-3c33-acd6-44e5a7fb47bd | -12.7726 | -50.872398 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7558cbad-6eba-3857-afc7-6f7ea316865a | -6.3432 | -57.7598 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de72bdaf-6b63-3d36-b506-a14c0501cc62 | -8.493 | -57.6031 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cae61a82-da9e-3ac2-a8ec-b800847083ca | -7.6135 | -50.409199 | 2026-09-23 00:58:00 | METOP-C | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5b31ca5-5d6c-3d62-9f9c-a191c0224850 | -7.2768 | -56.458801 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4857c05-513b-32ab-9aac-362f69877029 | -3.6566 | -54.254501 | 2026-09-23 00:58:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b0d8993-43b1-3b96-8986-72131cd300ec | -2.9234 | -57.7701 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da5d101b-a8e4-3388-9040-3d71985be173 | -11.5156 | -51.507999 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15f0321d-d099-35e2-948b-ead3c9000a5f | -12.807 | -50.887199 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2792ecf7-0057-3e61-ac1f-103a080504c1 | -11.6965 | -50.951801 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77532410-a16e-3a52-9323-307c2fe9f60a | -10.4517 | -51.282799 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8194a8-59a6-301b-8240-8ab19f86c26c | -12.7692 | -50.858002 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 541a68f4-5f0e-3954-8f0b-46f2a9062bc1 | -8.9144 | -61.4622 | 2026-09-23 00:58:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60d4fd36-16d8-3285-8506-38b336c08982 | -6.5682 | -55.407101 | 2026-09-23 00:58:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41195913-3ee0-3511-b363-25fe0f601dc2 | -5.6258 | -45.224701 | 2026-09-23 00:58:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 466d7546-1bda-333a-8751-efead3f4d435 | -6.6619 | -58.5541 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8d44322-820b-3f2e-8eb7-5b2af56a5da3 | -6.1051 | -57.658001 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 863db3dc-63dd-30ba-9a9c-d08ae06079a4 | -6.1323 | -59.921902 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1e3597-db58-34fc-8a2c-5fe8686da156 | -3.3009 | -57.847 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f36c8411-3c64-3656-8a4e-8b17276cb1d1 | -4.1642 | -55.164902 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3d02b5-596e-3e09-bbda-e5ce2c32db72 | -6.5763 | -44.138 | 2026-09-23 00:58:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5de56e8a-3036-359c-83ad-9071f2422b9e | -12.7449 | -50.8867 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c636dff-e931-3e31-a204-346466ebc604 | -6.6828 | -55.0481 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a5b712a-81ad-37dc-9bce-9c277f972ae1 | -6.6282 | -43.734402 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 199c51c7-84b2-3aa2-8a52-ac36ceeaa10f | -2.8567 | -57.793598 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69694c95-2732-359e-a86e-e69052c6042c | -10.692 | -48.719398 | 2026-09-23 00:58:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f09cfc84-6c53-3862-a165-4bf0dd567419 | -12.4273 | -46.975101 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23706700-c4f1-315a-8674-d881ef48b206 | -6.7266 | -59.412102 | 2026-09-23 00:58:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5b13a01-2ca3-3c43-b5ed-c71b87c00094 | -2.8672 | -49.617599 | 2026-09-23 00:58:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8269c9bd-9dac-3b91-bdef-18e910926344 | -5.8771 | -52.074902 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d90998a-c237-328a-b298-50448d0891b8 | -6.6243 | -43.759102 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc241e56-c6d8-30cd-bc32-222dac0257a7 | -2.9758 | -50.387699 | 2026-09-23 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df33463a-71be-3102-bf34-476aea1b87c6 | -7.4123 | -44.722198 | 2026-09-23 00:58:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f77f9b64-76d2-378e-9f63-dc5244c094fb | -2.9155 | -57.780602 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b907a6e9-3694-34bc-8eae-c057ff0982c9 | -12.484 | -46.995499 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a3a656d-eaa1-3632-bcfb-5fa87eebc180 | -3.7164 | -60.560902 | 2026-09-23 00:58:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0bba2f39-b96c-3041-a8d3-9080baba427a | -3.05 | -54.397701 | 2026-09-23 00:58:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b199da5-83ef-3228-ab29-8d711ec42b5e | -10.602 | -53.9776 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a7748ab-ca7f-37f0-933f-f5fd09a4c656 | 1.5626 | -55.915901 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc0ef870-40a2-3261-93bb-ca1ad8f9d52a | -11.6833 | -50.939499 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5951159-9e88-33df-9adc-1ff9d182a0a0 | -12.7857 | -50.884499 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bb34358-010c-33c7-b120-f699faf6fe0c | -2.6198 | -59.378399 | 2026-09-23 00:58:00 | METOP-C | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b257ec0c-0546-3043-973c-83c8e1bb598b | -6.0754 | -57.6171 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README26.md)
