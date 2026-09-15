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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83c49f23-67fa-3a05-80e9-e027335a34a8 | -3.4943 | -50.357101 | 2026-09-15 00:02:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8cd42d0-2804-3d8a-a340-30319badf2ba | -5.3111 | -49.2304 | 2026-09-15 00:02:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3efee40b-10a0-3298-8f92-40f7b6a96c24 | -8.5102 | -50.124298 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c49faba4-5c1c-3f43-a410-bf4ad19aad35 | -9.1633 | -49.9655 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e691ae-7136-337d-85f5-231db53b00b1 | -6.3191 | -44.112 | 2026-09-15 00:02:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 998ddc63-bcf8-3620-9b36-cf44544f9acf | -10.4419 | -48.619999 | 2026-09-15 00:02:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 443bc2b1-696e-3713-963c-7fa4ca7012f9 | -2.9155 | -50.391998 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89db560b-ce1f-32cb-8249-bdcbe37a3c69 | -6.8438 | -51.473 | 2026-09-15 00:02:00 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b97dfa4d-86d7-3083-be61-2dd3b5920233 | -13.7238 | -48.948502 | 2026-09-15 00:02:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 857ae139-96d2-3ff1-8bbe-2c04f1b7d137 | -9.6721 | -47.878201 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e909f83-33a2-3538-9327-e3a2e16007f3 | -6.9499 | -44.518299 | 2026-09-15 00:02:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a3eb67c-71ee-38b0-a8bd-8eb6bd93a863 | -4.6417 | -42.056 | 2026-09-15 00:02:00 | METOP-B | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 09f3c98a-d846-38fc-9695-55fcf4350e98 | -11.1795 | -42.7976 | 2026-09-15 00:02:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 74a66dfc-b470-3e2a-95ec-83d608bdcccd | -6.1009 | -44.060799 | 2026-09-15 00:02:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b350d950-068f-3cf6-b0a4-965c2e96e71c | -2.9188 | -50.406601 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85c92817-d48b-3fd4-9c17-946b1e411550 | -3.4877 | -54.627602 | 2026-09-15 00:02:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9716e70-af87-3d52-8560-0ca2d262ab60 | -7.0687 | -42.087399 | 2026-09-15 00:02:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 38192287-4875-30bf-a21a-bda7c75b418b | -6.1786 | -43.995998 | 2026-09-15 00:02:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28ab56ac-000e-3cb6-ac6f-d62a75b9b937 | -3.4861 | -50.366699 | 2026-09-15 00:02:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc2c37bb-e90a-3d85-8d2e-c789be89aa99 | -2.8991 | -50.410999 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b207211d-8e6c-3537-8763-ff963edd1689 | -14.8546 | -48.138802 | 2026-09-15 00:02:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 75a4ad29-e3a0-35e2-93c9-37277233c095 | -2.9171 | -50.3993 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b183b38d-4fc0-3e49-b842-237d6f3e9b00 | -5.1962 | -49.315201 | 2026-09-15 00:02:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9a5bb7a-29e3-3825-bf18-08aeb20b2b67 | -9.2492 | -48.5242 | 2026-09-15 00:02:00 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70590260-e992-30ee-84a1-7f863d9f2dbf | -6.3289 | -44.109699 | 2026-09-15 00:02:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32c4745c-ce26-3ec3-9826-b713ee458a8d | -4.3023 | -49.093399 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb8052d-4bad-3449-aa6b-40a9894e93ac | -5.296 | -49.071201 | 2026-09-15 00:02:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab353be-9556-371c-9e8d-94c746657d07 | -3.4807 | -54.642399 | 2026-09-15 00:02:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3327b7-546a-34e9-a496-e426e9298000 | -9.3633 | -50.084099 | 2026-09-15 00:02:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f3cdffd-470f-3dfe-9859-a3db2582a469 | -10.708 | -47.4911 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5d903cc-e9a9-3c12-b2ad-7d353cb9e4ff | -10.6725 | -54.106098 | 2026-09-15 00:02:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07e3513d-1e9a-3a99-a19f-626665ea39ea | -5.5974 | -44.822102 | 2026-09-15 00:02:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dea7e6d6-9d93-37de-b8d9-dad3048840a8 | -5.9672 | -49.264599 | 2026-09-15 00:02:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d8eadd-27ec-387d-853a-883b32756ad8 | -11.2371 | -43.435101 | 2026-09-15 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30dabb29-c073-37f0-bb47-12f5ca458266 | -11.1676 | -42.791 | 2026-09-15 00:02:00 | METOP-B | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2b4b7730-d6b8-386d-8853-526cf3f0cf38 | -4.5517 | -50.438999 | 2026-09-15 00:02:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9c7d38-6cef-3748-8fdc-4b38b7c27445 | -7.152 | -42.091099 | 2026-09-15 00:02:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab43042b-cc6e-3ba5-a53c-3679c389ed09 | -6.7811 | -43.179501 | 2026-09-15 00:02:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b79602de-6022-33d2-9c29-63b34f29358a | -17.470699 | -43.644798 | 2026-09-15 00:02:00 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fde489f2-f988-3de3-84f5-87b7c51a95d6 | -10.572 | -47.713699 | 2026-09-15 00:02:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39397dd7-be1f-3aa9-a32b-fa5e506610da | -5.4229 | -43.982101 | 2026-09-15 00:02:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f1693ef-5f20-3868-ac4e-495dc3f7625d | -13.773 | -48.7929 | 2026-09-15 00:02:00 | METOP-B | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c5ebac71-cc56-3736-9444-9c462e2adfdf | -8.5103 | -48.485298 | 2026-09-15 00:02:00 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69393eae-04c6-3b0e-912c-f43cc7727a7c | -13.5113 | -44.157101 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5bc51ec9-2290-3929-9d35-a87f71962517 | -10.2997 | -54.119099 | 2026-09-15 00:02:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b91c189-3147-366e-a1d8-357c3e043703 | -15.2652 | -42.773399 | 2026-09-15 00:02:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0e980b7d-2c80-3843-8df8-1773cfc900f9 | -4.5122 | -54.9193 | 2026-09-15 00:02:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10d27042-6386-3ee9-979a-ad773f34541e | -13.3257 | -51.5793 | 2026-09-15 00:02:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f189a83c-a43e-3295-ba52-415c00ea8cee | -13.225 | -51.635502 | 2026-09-15 00:02:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b5cd4fa-0c70-319f-8c8d-4b124bcc9384 | -6.9537 | -44.534599 | 2026-09-15 00:02:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67687c13-9284-3c95-8ead-5c5c01df1da4 | -10.3027 | -54.133999 | 2026-09-15 00:02:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffead5ed-a6e0-3d8b-a8aa-3d04116bce13 | -8.5119 | -50.132301 | 2026-09-15 00:02:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed7643b-ff6d-3b39-b1ec-927e7def554d | -2.8958 | -50.396301 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f23529-0467-3522-965e-de627427c255 | -14.6829 | -48.006001 | 2026-09-15 00:02:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 60056fe9-5612-3355-8aa1-c2600623564a | -3.9161 | -54.482601 | 2026-09-15 00:02:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb32558-92ab-3834-9062-2654734e1d17 | -14.7553 | -42.934799 | 2026-09-15 00:02:00 | METOP-B | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 5a98b62d-17c9-3186-878e-8fc2141b9752 | -14.6698 | -47.992599 | 2026-09-15 00:02:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 62506fdd-440b-3c17-9144-0b6557c4e280 | -6.0187 | -52.156399 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8b6dfb-b11c-3420-8fc8-741d8bd2dd18 | -2.8236 | -51.314098 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61175791-8ec6-3bb8-ac00-7685b0f6bbe6 | -18.309299 | -44.115601 | 2026-09-15 00:02:00 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 746f5bad-e197-3fd9-9b79-adf18b7ae83d | -6.7286 | -48.1119 | 2026-09-15 00:02:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d0fafbae-2fb3-3a76-b34d-e834ad207e85 | -4.5219 | -54.917198 | 2026-09-15 00:02:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a133d9-5669-376e-8a13-bc7ea709a567 | -7.2224 | -46.149799 | 2026-09-15 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23c27edf-9c7e-3b03-830a-e7fe484bd908 | -4.2925 | -49.095501 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad30aa8-4708-3e8b-b536-5e795fbe317d | -9.6353 | -47.665798 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28d35dc4-c579-3b28-9a3f-aaf356ad3459 | -8.8277 | -45.865002 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0ea444e-675e-3bac-b536-279508ffc5a1 | -12.4717 | -41.3801 | 2026-09-15 00:02:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c50b6638-89ea-3741-8fc9-dde0a94b1a17 | -8.8392 | -45.8699 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e3876e1b-63d0-3c26-ac8f-ff9cb3fd005a | -4.1821 | -49.383701 | 2026-09-15 00:02:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8104f83f-1f8d-3118-86f7-e31c95fbb5ac | -4.5368 | -50.4184 | 2026-09-15 00:02:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f966e773-edc4-3311-86b0-c1bf20ba8737 | -3.4905 | -54.640301 | 2026-09-15 00:02:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd6992f1-a928-3244-9cb2-9a53bd0de2f6 | -4.6514 | -42.053699 | 2026-09-15 00:02:00 | METOP-B | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3e05b705-e2b7-347e-a824-824beb8db5c1 | -15.2632 | -42.765099 | 2026-09-15 00:02:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bcd28830-5a96-3027-bf9a-177959fc9cf0 | -11.096 | -40.444599 | 2026-09-15 00:02:00 | METOP-B | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| adfeb7e9-26d1-3ff3-99c1-583589e9a4ea | -11.974 | -44.921001 | 2026-09-15 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82ae950a-02da-3059-8997-6da75e9f6abc | -6.0522 | -52.1693 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f831d408-f3af-37fb-843d-d466a66f5aa5 | -6.4144 | -51.1973 | 2026-09-15 00:02:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2101bbd-f624-3a93-a506-8f2c1c2afbb6 | -7.4544 | -46.126999 | 2026-09-15 00:02:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a12fad9c-f4e4-3664-afed-7107d945478a | -5.1194 | -55.888901 | 2026-09-15 00:02:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7037a7b6-6b45-31be-91e0-8b3dedf310c6 | -2.9008 | -50.418301 | 2026-09-15 00:02:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d92bedcd-868b-3722-88c9-35dbf7878c95 | -12.4244 | -47.297501 | 2026-09-15 00:02:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acfbb9c9-95c7-3670-b2d7-7f924cc6641d | -6.9401 | -42.543598 | 2026-09-15 00:02:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 300b06c1-a535-3a8b-8285-55eaf1899f1f | -8.7934 | -45.895401 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae14786-2d98-3cea-bb65-76676c928f99 | -7.0713 | -42.098598 | 2026-09-15 00:02:00 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3292e5d-db32-371e-8682-ec4193e33866 | -6.7843 | -46.4436 | 2026-09-15 00:02:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd9f3a87-191b-3d16-ab3c-058c5a2ad6c2 | -5.6079 | -45.225101 | 2026-09-15 00:02:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ee0933b-0ea4-3db6-8779-f471e81ea650 | -12.8469 | -44.363701 | 2026-09-15 00:02:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ca44b7f-228f-37c3-974b-54c083bf0a50 | -13.8698 | -49.400799 | 2026-09-15 00:02:00 | METOP-B | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| afea12b7-a135-3059-9124-a17d7ebb53e9 | -8.8261 | -45.857899 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af8f2bfb-1ac5-3ffb-810b-fe9d2cd48463 | -4.188 | -48.677101 | 2026-09-15 00:02:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3829390a-6a65-3700-b2a0-968163884e09 | -6.7788 | -43.1698 | 2026-09-15 00:02:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b764ad32-d33b-3439-bfeb-f671de880232 | -3.2608 | -54.4804 | 2026-09-15 00:02:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b64b4fa-b018-33b7-b0a3-4100b6634a40 | -9.4579 | -48.538502 | 2026-09-15 00:02:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 247dd142-e089-30c5-a457-2132a19751f4 | -9.8882 | -47.7855 | 2026-09-15 00:02:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c632ef0-e3a6-3a0c-a2d6-06c4c32e92e4 | -13.578 | -47.877899 | 2026-09-15 00:02:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6498e091-35cb-3481-9fe6-294d540b8d9b | -8.7902 | -45.881199 | 2026-09-15 00:02:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5a79514-6e87-3d1b-b356-befcfc098bb3 | -11.4956 | -45.764 | 2026-09-15 00:02:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b0e2214-5b1f-38be-8134-8700d254adbe | -11.8099 | -46.566601 | 2026-09-15 00:02:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27a0d6a8-5786-3e41-92c8-fa24a1962975 | -5.4101 | -48.477699 | 2026-09-15 00:02:00 | METOP-B | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9789c4-f1fa-3b36-a57a-6e960d4ee0e1 | -3.9188 | -54.495098 | 2026-09-15 00:02:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
