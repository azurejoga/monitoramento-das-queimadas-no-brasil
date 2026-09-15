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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3593ed40-b402-324f-a57d-948f7c94b99e | -9.1337 | -65.8253 | 2026-09-15 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 39277d01-1e73-32a9-a9f3-ae3941eed9b3 | -9.7684 | -46.1293 | 2026-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 7aa9b9c3-d261-3418-ae02-31f9b017f8bc | -9.4234 | -47.8588 | 2026-09-15 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 79606e83-36fc-31b8-b2fa-5d8eaa7a67cb | -6.7473 | -45.2566 | 2026-09-15 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 3b082a5e-212a-3bd0-828a-3153ef573d1e | -6.7869 | -58.8027 | 2026-09-15 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 2b0a6152-be70-3bb6-9ba5-a491a98b0537 | -6.5837 | -58.8498 | 2026-09-15 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 568ffc90-8966-35bd-9009-18d2c85d92b6 | -10.6827 | -54.1679 | 2026-09-15 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cbbc76bc-d5c3-3b1d-9f50-9993ebf1b6d4 | -18.1709 | -51.7685 | 2026-09-15 14:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 70bc1989-9b90-30b6-aaca-a2fb55f59c1d | -13.3949 | -57.0242 | 2026-09-15 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 15efbbba-ff78-3de2-b172-ba2ae1ea06fc | -8.0619 | -43.7545 | 2026-09-15 14:10:00 | GOES-19 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| aaec0c50-155b-3224-81af-56fb039beee0 | -13.3059 | -51.3022 | 2026-09-15 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 9184524a-63cf-36a8-ace8-0b54eddb0739 | -12.3273 | -47.9735 | 2026-09-15 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 248.0 |
| ec30fe9b-0ddb-3937-a6da-9fbf9f99c1d6 | -10.792 | -46.2071 | 2026-09-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 65eb5bd5-bfb0-34dc-87d9-d7a78e2348ac | -10.6829 | -54.1475 | 2026-09-15 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5b6a2f32-d91c-301b-adf9-94a8f2bca491 | -7.082 | -42.1346 | 2026-09-15 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |
| 82ee2db8-ab02-39d8-aace-11402061ee51 | -2.9025 | -50.4214 | 2026-09-15 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 96bfae01-1e98-3f2d-9088-90671527a2ec | -9.475 | -45.4612 | 2026-09-15 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 6b5d5ded-d58c-36a1-9c8e-4efa589b2202 | -11.2302 | -54.119 | 2026-09-15 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ccf94131-cb73-309d-8c52-e9e2fa5aee8f | -9.4139 | -50.1103 | 2026-09-15 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 87301cbc-aa2a-3785-b740-f07acc7f69cb | -7.0166 | -44.6184 | 2026-09-15 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f85346d4-5529-380f-9af1-541b3d4b3e65 | -8.5415 | -54.7187 | 2026-09-15 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7109929c-b931-3902-9000-f8601f689f95 | -9.4137 | -50.1317 | 2026-09-15 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 3fc471eb-0f97-303e-9aa7-4c747b371313 | -8.8078 | -45.8979 | 2026-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d9447b9a-32b0-3adc-8662-6fba376de191 | -11.5045 | -45.771 | 2026-09-15 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| af9f39f4-d6d2-349c-b14d-8c0b4e872e68 | -15.2827 | -42.783 | 2026-09-15 14:10:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 552e7553-d7a2-3904-8ad8-df2b331e4c45 | -13.3062 | -51.2808 | 2026-09-15 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| d3e5f3f2-109d-39fc-878d-fc707df95ff1 | -11.2113 | -54.1208 | 2026-09-15 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| ebe64c98-cb90-3c22-bcd7-42ace097e2c5 | -10.6641 | -54.1491 | 2026-09-15 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8604fd4d-1164-3aba-b1d9-0d20b4d70ee0 | -13.2678 | -51.2856 | 2026-09-15 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5e8a9a24-a0d1-37ea-a3b3-81cc85588ed4 | -6.8405 | -43.5254 | 2026-09-15 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 8df772c8-ae9d-375a-8d0f-f64e8b73d9c3 | -14.6969 | -48.0209 | 2026-09-15 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 62baa0f2-27f3-3f5f-af88-548b9489feec | -13.287 | -51.2832 | 2026-09-15 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| bee54e06-6638-3369-9b7b-6f43bd138dba | -4.6774 | -42.0951 | 2026-09-15 14:10:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| 764b1adc-b9b6-3d00-8a6d-df1ebaa16bab | -7.1525 | -44.2154 | 2026-09-15 14:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 7589adfe-c5d2-3fdb-85bd-d82bcbea83eb | -13.414 | -57.0225 | 2026-09-15 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 98d76c47-c395-3582-b508-d6c86f1fee46 | -5.144 | -55.9345 | 2026-09-15 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 191.0 |
| 22426619-feb0-3a4c-8f71-f98ff8fb8456 | -2.9025 | -50.4004 | 2026-09-15 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 89499777-a7d0-3f5d-89c6-96287484bb54 | -10.0008 | -45.7851 | 2026-09-15 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| c954d115-9320-3dfe-8ea6-7ea0149eb14a | -2.921 | -50.3999 | 2026-09-15 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b89499fb-59ab-3148-a70d-42dd444d2dc5 | -12.3277 | -47.9513 | 2026-09-15 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 6379675b-605a-3fb4-ad27-b4970fdbee87 | -5.1256 | -55.9352 | 2026-09-15 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 54b5e02f-e1d1-32d0-9863-93e0ba3fb7b6 | -12.3085 | -47.9539 | 2026-09-15 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e0207af0-f97c-37fc-bcf3-0302d42fa10c | -6.6021 | -58.849 | 2026-09-15 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 59e392af-54c4-3bdc-96d0-3e9b290fac5a | -10.6962 | -47.4953 | 2026-09-15 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 8e8c24b5-d0aa-377f-b208-b897d58ab522 | -10.7726 | -46.2322 | 2026-09-15 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 048109c5-7854-3a7b-9313-a3193ee03ce7 | -11.9033 | -43.8112 | 2026-09-15 14:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 6b588fd8-6ae1-30ac-88ab-ef0f42d39a3e | -12.126 | -44.2225 | 2026-09-15 14:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| d4d989be-3cba-3dff-8a49-15656884fc5a | -8.5468 | -50.4423 | 2026-09-15 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 1f57a321-bef1-35e4-9d8d-030eb1489b33 | -7.14 | -44.27 | 2026-09-15 14:15:00 | MSG-03 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b0b2418-ea1d-3a6f-8330-65312f622139 | -10.32 | -45.35 | 2026-09-15 14:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d71fd02-c471-37dc-984b-649483febc23 | -7.17 | -44.23 | 2026-09-15 14:15:00 | MSG-03 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9bf48ba1-d1bf-3fa5-b532-0fb64c49656d | -11.7962 | -46.5926 | 2026-09-15 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a934eca5-d4eb-37f3-a677-15fa81fc55bf | -14.0133 | -53.8709 | 2026-09-15 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 02aa3a22-b0a4-351d-bba3-a9b3b80f33ef | -10.6829 | -54.1475 | 2026-09-15 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f015bd6a-0983-35f3-9cd8-786df1765345 | -6.8408 | -43.5021 | 2026-09-15 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 29721f72-151d-3abd-8b38-205b0f7b77dd | -9.7687 | -46.1067 | 2026-09-15 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 1c8ead73-53fc-3dfc-8889-d3f365aa28ab | -11.8154 | -46.5899 | 2026-09-15 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 4e8b8c31-9437-35a7-97ca-a562a52308f2 | -9.3577 | -50.0943 | 2026-09-15 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| cf3f128b-1f60-3e59-83a8-5614f3509fc2 | -6.8217 | -43.5271 | 2026-09-15 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 7edad793-85b4-3295-8264-01e4394b199c | -10.6962 | -47.4953 | 2026-09-15 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 2579bb96-6888-33b0-8a4f-7828a2197e6f | -18.1714 | -51.7466 | 2026-09-15 14:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| cedcdf71-00b7-38b4-960a-0c4cf284edf8 | -10.6958 | -47.5175 | 2026-09-15 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| cec07777-602d-32ab-80b9-b6a985748d8e | -9.6089 | -46.7087 | 2026-09-15 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d94f58b9-4e5e-3da4-b1ed-54bbb3463327 | -13.9941 | -53.8731 | 2026-09-15 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e96af3a8-bc8c-3c01-8f82-38436afdae35 | -6.0196 | -51.7893 | 2026-09-15 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 7cc50e10-f496-34c6-a7c6-789a50cd80a9 | -9.4234 | -47.8588 | 2026-09-15 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 36f4d2e2-698b-3f30-ac32-016db3afccb6 | -9.1711 | -49.9835 | 2026-09-15 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 4b6d08aa-c7db-3ba4-bee4-6ed6590239c9 | -11.5045 | -45.771 | 2026-09-15 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 5e54cd38-d10a-37bb-bcb6-98c224b522e6 | -13.2232 | -51.6744 | 2026-09-15 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2e65230c-270e-31cf-b135-5534d11f3b37 | -13.3949 | -57.0242 | 2026-09-15 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| a3000856-3437-3021-b7c1-86d16edabe1d | -18.1709 | -51.7685 | 2026-09-15 14:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f3cfa2e3-0862-366d-8463-566c26b32fd0 | -10.9495 | -48.3255 | 2026-09-15 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 4c628978-2c2c-3cee-8749-8c251b0a2ed8 | -11.3638 | -43.9642 | 2026-09-15 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 51930d0c-7ac3-36aa-bd95-9876fe3f1547 | -8.7889 | -45.8999 | 2026-09-15 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| f9725836-81ab-37fb-afac-530d0149c427 | -4.6776 | -42.0713 | 2026-09-15 14:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| a77a5d7e-a839-3b01-afba-0c000e7d2157 | -9.4266 | -60.3003 | 2026-09-15 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d35e9aae-0e55-3f37-844e-e4cedf68a736 | -8.8459 | -45.8713 | 2026-09-15 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 59ffbaa3-18bf-37af-85e0-da50125ffdc1 | -10.7274 | -50.6192 | 2026-09-15 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 76ea114c-afff-3840-8279-4feb2b4929d5 | -5.1255 | -55.955 | 2026-09-15 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 142.4 |
| c0312b1d-3a5a-3869-8612-cc39f5898ec6 | -3.591 | -58.5384 | 2026-09-15 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 122.3 |
| e7f1ba53-9bf2-3930-ae40-39fe151d7f46 | -9.3572 | -50.137 | 2026-09-15 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d3fda7b3-81bf-33b8-8b67-36ae26f2e056 | -6.8405 | -43.5254 | 2026-09-15 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 221.7 |
| bf0cb775-8b01-3cb2-ac78-320039b5ca88 | -10.0194 | -45.8055 | 2026-09-15 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f1123155-269a-3776-96eb-3379ae60f524 | -2.7767 | -49.4765 | 2026-09-15 14:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 696c18d0-8a5d-3d86-b1dc-e5c3a4ed3498 | -10.6827 | -54.1679 | 2026-09-15 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a5b5ffab-85fc-3f8a-b56a-9bb9644fdd72 | -13.3202 | -51.5986 | 2026-09-15 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8871961a-e6d6-3538-88dc-077ea8514635 | -9.7358 | -47.0958 | 2026-09-15 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 79f563b2-f5ec-34d9-92ab-8cd83e203e0e | -13.414 | -57.0225 | 2026-09-15 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2a7b91b4-a0a2-3203-8c07-d8a2b86993d2 | -8.5656 | -50.4407 | 2026-09-15 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| ad07da6b-d5bd-369a-a49c-0e3808d93e47 | -7.1711 | -44.2367 | 2026-09-15 14:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 307.2 |
| 523b9f06-ff62-3139-bfa2-3d1d3f895f3a | -5.9333 | -53.5362 | 2026-09-15 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| f2e12e0b-0997-3578-b668-b34c11b778d7 | -13.2235 | -51.6531 | 2026-09-15 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| acd112d9-589c-346a-8cd5-aa02e0b75a9a | -9.5899 | -46.7109 | 2026-09-15 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 63cfcba1-0364-33a0-9cd5-15e1c4570307 | -10.6522 | -50.5845 | 2026-09-15 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ab61d36f-443b-392c-9248-49e0dbf6bbe0 | -12.3273 | -47.9735 | 2026-09-15 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 221.3 |
| f4123ae2-2719-3bc0-a98b-bc4d81064eb1 | -11.5041 | -45.7939 | 2026-09-15 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a5c4bbe1-30e4-3b15-b656-3a2002a83928 | -13.3062 | -51.2808 | 2026-09-15 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 2a30468c-b686-3c5c-95bc-8d991e3f61ed | -9.1337 | -65.844 | 2026-09-15 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e72a20b7-640e-3a7f-b868-01fbd2336206 | -14.6779 | -48.0016 | 2026-09-15 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e9aa8353-6f00-39ba-97d3-7be6ed2a37d1 | -13.7002 | -51.8274 | 2026-09-15 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |


[Clique aqui para ver as próximas entradas](README80.md)
