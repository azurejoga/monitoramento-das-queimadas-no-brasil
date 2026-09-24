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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c34eba21-b37a-3add-8bd9-ef8904c22ae6 | -4.54955 | -54.93891 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96806fc9-07e9-3c9f-8d37-a738fe26895b | -2.7422 | -51.54587 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fef1e5c0-0459-3e6d-b676-690145763d6d | -3.71587 | -54.20094 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd842d53-7228-3535-bf94-cb5ed9a83024 | -8.59627 | -54.61594 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11eeb7d6-2a74-35c5-a185-17f46f0741ed | -5.25987 | -49.22978 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f70916b-869c-3db6-ab38-d5a729f5ed30 | -3.44768 | -50.07415 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cb12f6b-65aa-37fb-83a8-e45a1f1c251e | -3.7087 | -54.20337 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4a7571f-eea1-3da7-aa3e-ea06ff3c2c51 | -6.10022 | -57.67979 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7118a483-b0d3-3735-9d81-c2dba3625fec | -3.81324 | -58.8895 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0afad821-f169-37e2-bd79-b05509b0f6c4 | -3.44726 | -50.09026 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a61b6acc-bd93-3eff-9b38-55876e8276ba | -6.65624 | -55.06741 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4b14c91-c6cc-3e23-97d8-f7a11f4c981b | -2.11206 | -56.30002 | 2026-09-24 05:04:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baea711a-41dd-3fa1-bb7d-5b936b2d0d54 | -6.68169 | -55.05718 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 162f74c0-cc89-3494-afb5-cabcaa76b8f5 | -2.93211 | -56.58345 | 2026-09-24 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7060ea1-e2cb-323b-9718-8c29291bd718 | -6.14476 | -52.75264 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dcd101a-3916-353a-b073-d3610b4818a9 | -3.4537 | -50.08411 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 380ecf2c-af0e-39bb-a471-046f8ae3c227 | -4.28307 | -55.43708 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5719dada-02da-3e45-ac96-81d4e1c00705 | -4.99696 | -45.55299 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6dc2113a-e163-349f-a72a-0131752f9826 | -6.11072 | -59.8808 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c61735fa-7cf6-3db6-b504-7474785065ba | -5.14126 | -60.31588 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07be727d-5424-3900-a146-1d0c11f8d9f0 | -2.50251 | -56.23477 | 2026-09-24 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 040bda37-9e5d-3b24-885a-4874c1fa52d6 | -2.1085 | -56.29945 | 2026-09-24 05:04:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ba9705a-494d-388c-b5d7-319a0b8ff332 | -1.19737 | -54.14149 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f271fc0e-23cc-3b8f-850b-2d407f4f85ce | -5.30677 | -56.00612 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca8e466-fa63-3885-89c4-bd093f9bec7b | -4.2978 | -49.12578 | 2026-09-24 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f64cae1-4f94-3660-a7bc-9e2d873c2caa | -6.15791 | -59.93986 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93df8c06-e982-3223-b4f1-efcd15adce33 | -6.61625 | -59.92141 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4d2545d-5fbf-3082-b6b1-f5189577a19a | -2.47047 | -57.91389 | 2026-09-24 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf280656-1c40-3d6e-852e-5a5c7a8408f7 | -4.71726 | -55.98537 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 03f97665-751a-3f57-9066-19f02b637ba6 | -2.16936 | -48.3217 | 2026-09-24 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8092fea-e4a8-31b8-9f45-7fde17c9fded | -4.49948 | -54.95654 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3132338-00f0-3fe8-95b9-573ae97e0c29 | -8.3577 | -57.67918 | 2026-09-24 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73dedad9-bdbf-3bd1-8e1d-dd9297e6957f | -3.7929 | -59.37341 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e20bfe2-28ab-3277-91be-0826928cc64d | -3.71863 | -54.20491 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56673c05-61dd-392a-90bf-2af5b13b7c41 | -10.09451 | -46.06423 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71f9ccf9-cc12-39c7-abc5-897a67051418 | -7.5164 | -61.47491 | 2026-09-24 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c65aedbc-2558-3d16-a047-ac68d46f7163 | -4.95301 | -45.14606 | 2026-09-24 05:04:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9a37025-a392-35fd-8fd6-7bcf4f87a3d0 | -5.19642 | -44.69136 | 2026-09-24 05:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8edd40cc-6fe4-3ac7-91a0-cc2e77ad0956 | -5.57168 | -42.73682 | 2026-09-24 05:04:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 16b49e50-3221-3624-89c6-d01e93b395bb | -6.88254 | -55.56439 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcfbdaf6-c55d-37ed-94da-39ffe9d5d247 | -3.15656 | -54.60044 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9f9e4d69-0968-3774-a5ee-22469eb0d6a0 | -3.45364 | -50.07312 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 956e72d2-022d-3fda-8d40-7c1869280a34 | -6.06875 | -57.80229 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19f51881-469e-3151-a2e0-0fae85180108 | -2.9693 | -52.15237 | 2026-09-24 05:04:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3618bb-44ff-3f47-abc5-e49e0d5dc783 | -3.70979 | -54.19646 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25f3deb0-28ca-31bf-ad0b-ce17d8698af5 | -6.57455 | -51.49431 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7791e887-56f2-3cef-9b1f-b969d5927204 | -2.89331 | -54.09581 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a480e16d-ee9e-36f5-8ae5-410763e2c47b | -7.58803 | -57.66314 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae214664-74ee-3fad-a500-9be5ec9af030 | -5.99597 | -57.72086 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9f93966-154f-3b52-aba9-105b4f7e969d | -5.90824 | -59.92973 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd742827-0f86-3186-92a3-7b93e38b8dce | -6.64722 | -59.92609 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d27d78-e478-3248-b1a4-4054b6a7d76a | -3.49596 | -59.17459 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55f72e0d-73e8-3af0-b92b-b368428d4386 | -6.62621 | -59.98952 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74eb682c-1f4b-316f-9843-001c039feb3f | -2.71052 | -57.50946 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e82b55ba-18d7-312c-b7fd-22d81e971545 | -8.2652 | -54.77718 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e974232-6d3b-39d7-aaa8-0c4d918c2094 | -1.92119 | -58.26157 | 2026-09-24 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 338493f8-412f-35b9-9c6d-0f4e7aea6b98 | -10.09414 | -46.06713 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7970817-60bd-3f13-904c-e8052cf92449 | -5.86251 | -51.95674 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 250c1f13-9ecb-38b1-a3ed-d5aa7e4043c0 | -7.04745 | -62.93981 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 081cc9e0-9030-3474-a434-8e89f540ab2f | -6.44773 | -57.77618 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c52abc62-a217-3d8d-ab0d-96c58a8e2e1c | -3.44254 | -60.57534 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 11fc31d3-f7e6-3cc2-9bfe-4fc64f257e35 | -8.27898 | -54.77581 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b91e60ab-230c-3b46-913d-30ce8c1acbdb | -4.41905 | -55.07386 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4b50fb3-915f-3e45-8f37-3e1d06b459df | -2.15184 | -59.23613 | 2026-09-24 05:04:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e4c569e-11ab-3d4e-a016-f406169947e9 | -6.00016 | -57.69525 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2263811-0008-39a0-90b2-5011b8a70aab | -3.07145 | -54.38652 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d786cc69-55a3-3644-bea4-58aca898ad9b | -6.08602 | -57.62991 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42b4f164-2d96-3965-bb02-59923f085fd7 | -7.09282 | -52.76163 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b92ac3e8-b0e8-387a-ac48-c1981932c61f | -5.25187 | -49.22858 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 595365f4-1dab-3667-918f-3ba74009753d | -6.12919 | -57.75485 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa4b88ad-aec3-3973-957b-bc36c21d02c0 | -5.8298 | -50.21659 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38403831-deca-387d-b2f0-97255b8948af | -3.26963 | -54.27219 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07f24af9-8be2-3dba-ba03-3d555a8be87d | -2.94198 | -54.08969 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f88afef-ea37-34d5-bf8a-9e97a767f4a1 | -9.5795 | -46.51597 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3159a71f-6a2c-3c33-a4ba-48f99aa4f3a6 | -7.41566 | -49.86382 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 028050f0-0255-39e2-8acd-96a132dcdddf | -2.4666 | -57.91325 | 2026-09-24 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab2635b-6c68-3e7d-a5a6-27faf09ff378 | -6.34223 | -52.74561 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b030d8-c7db-38e5-ad93-0a00692c473d | -2.89939 | -54.10031 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 05a98b82-0f5e-3085-bf80-dd153cbbcefe | -1.79763 | -53.74264 | 2026-09-24 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 158ee63a-41cc-34f1-b0c1-cde10b7b4884 | -2.45475 | -49.21865 | 2026-09-24 05:04:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04cb4b6b-c5ed-3f87-be40-580977f1aabb | -5.59875 | -45.95592 | 2026-09-24 05:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ff9dd58-0e8d-3cba-9248-01679cb0450d | -5.91309 | -59.92657 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd4b679f-5020-3f77-a087-6254e334d957 | -6.11219 | -59.88092 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf8e4392-c43e-3ea9-88a3-b3152f7d0820 | -7.19638 | -47.47238 | 2026-09-24 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bbc8142-cf61-3a2d-a4cd-777e0282d7cf | -3.85564 | -51.99792 | 2026-09-24 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 853e4625-d5c5-33e8-86b1-57c9cd8ffb60 | -3.16465 | -60.10069 | 2026-09-24 05:04:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17482c3b-27c0-336f-91aa-007b713e4b9c | -3.04317 | -46.92738 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b8dab5a-6a1f-3ae7-af29-80ceb4cf8e92 | -9.25892 | -47.34771 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b54f5819-c4b1-3c36-9257-c3f2fe7b7698 | -5.25535 | -49.23263 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a7d2c03-eece-3e53-977c-89eb3f8ff703 | -5.97924 | -55.37243 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae1e8ab2-0434-33ba-b5ac-dbbfa60f1dfb | -6.61727 | -59.99185 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b86908f-3461-331b-8ca0-0ab047b01a53 | -8.58855 | -54.62184 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f448ea2f-e2c2-38eb-ab95-610e9726a65d | -8.23076 | -54.67172 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b654e5fb-a03e-3d0b-9530-e7dca30c73fe | -3.80861 | -58.89236 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88945be4-dc78-3d2e-8079-0f81c2e1fb1a | -5.98315 | -55.36942 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e3f04aa-43fa-3391-9424-cf2b3aaf0e5f | -4.94311 | -56.02053 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b47ebf5b-dd2d-32b8-b0b3-3a28757d8731 | -8.59571 | -54.59801 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86650272-3c40-316b-8059-efa8a89850da | -8.26354 | -54.76623 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed6cc0c1-9ae8-3b7a-85fe-3397c13dd49e | -2.8911 | -54.08838 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34ba2a45-b097-3216-b6de-afdc248da206 | -7.9146 | -54.75975 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README64.md)
