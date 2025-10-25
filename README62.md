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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ef510df-4f63-347e-bb02-72cb00e6a9d8 | -12.0655 | -46.39659 | 2025-10-25 05:59:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2de2e5ea-6733-3247-a88a-43bf035d9687 | -9.32534 | -46.9805 | 2025-10-25 05:59:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7721928b-9636-3149-adfa-c06d794f0a02 | -12.7918 | -48.6694 | 2025-10-25 05:59:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ae592274-14ac-36ed-9ae9-29b76d9782c4 | -10.66673 | -48.06122 | 2025-10-25 05:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6d19274b-1c4f-3421-b290-e3b86f710649 | -14.43775 | -48.06771 | 2025-10-25 05:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cb0ceb11-eb31-3cca-b0fe-e74612acc75d | -13.33434 | -47.91213 | 2025-10-25 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3d44730e-e25a-393f-b754-8febeda46660 | -14.99959 | -49.97447 | 2025-10-25 05:59:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 49f3aebe-b7f0-36ab-b684-79b7bc0797ca | -14.48134 | -47.89873 | 2025-10-25 05:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d769087c-1dbe-389d-94c0-e57556384c33 | -13.72474 | -48.3772 | 2025-10-25 05:59:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 083b8506-5cf2-3e15-8e44-dafd5814b356 | -13.28662 | -47.49454 | 2025-10-25 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 64177b71-acc3-311e-b0cd-ab9970855e1d | -8.33716 | -46.17955 | 2025-10-25 05:59:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb871401-e0aa-36ae-ac84-54c3e173d810 | -10.68378 | -48.07909 | 2025-10-25 05:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 107a1591-4494-31b4-96bb-0138a0208dc3 | -9.31596 | -45.19127 | 2025-10-25 05:59:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7dbf21e9-5446-3810-b081-5047826ad5b9 | -14.86833 | -48.09293 | 2025-10-25 05:59:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c2ba9c46-8102-3689-89d5-e40c2f9130a0 | -14.85954 | -48.09151 | 2025-10-25 05:59:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 506d83b0-9c57-35fd-93d0-1f7ac8c22bca | -10.40572 | -44.73967 | 2025-10-25 05:59:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d773d15a-d49a-331e-b005-cc0858bc40ec | -7.86578 | -46.73369 | 2025-10-25 05:59:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c716133b-0a8a-3ee1-94c1-ee18d1dc0de8 | -13.90338 | -48.41796 | 2025-10-25 05:59:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5e4633a7-1518-3b57-a9a1-8eefd604d3ad | -7.7906 | -45.39193 | 2025-10-25 05:59:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df8af8c7-291a-31f5-9096-dde0cbe0fcca | -7.78174 | -45.39055 | 2025-10-25 05:59:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3dd1200e-05ac-3038-9b0e-f1a054ac5337 | -22.82889 | -51.3559 | 2025-10-25 06:01:00 | AQUA_M-M | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.1 |
| 46d5a9f5-b16b-3fb1-92f2-44eb77ebf608 | -20.47343 | -50.05297 | 2025-10-25 06:01:00 | AQUA_M-M | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 60.3 |
| ede6910a-2951-301d-848a-26b9a53f7d8d | -18.1599 | -51.75682 | 2025-10-25 06:01:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3918fa3d-e4f2-3d7a-b128-f6a6eeaa9dcb | -20.47491 | -50.04347 | 2025-10-25 06:01:00 | AQUA_M-M | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2729e242-6636-3c73-a22c-8786e9e2855b | -19.76118 | -48.28987 | 2025-10-25 06:01:00 | AQUA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a1b139a4-7a4c-3042-a84b-9609c03f3034 | -18.16969 | -51.7587 | 2025-10-25 06:01:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d36fd2ab-899f-34fe-a3d7-19cf40f171fc | -19.76257 | -48.28046 | 2025-10-25 06:01:00 | AQUA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6bbad50d-02af-31a3-9515-3efc0af53339 | -18.17163 | -51.7471 | 2025-10-25 06:01:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| bbb06455-d92d-33ed-b217-74944f106a4c | -23.13136 | -47.33044 | 2025-10-25 06:01:00 | AQUA_M-M | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 7fc25d9b-3b6d-3e5f-84af-8d398cbc229a | -18.16185 | -51.74521 | 2025-10-25 06:01:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 77c92604-f730-33a5-bcdb-1844225906dd | -18.55391 | -50.26449 | 2025-10-25 06:01:00 | AQUA_M-M | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 31.5 |
| e9a943f3-e97d-3abf-b1f1-ce35362a55ae | -21.91315 | -46.52725 | 2025-10-25 06:01:00 | AQUA_M-M | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 16d5d300-1c9e-375c-9d37-18c29776b3c6 | -18.55236 | -50.2743 | 2025-10-25 06:01:00 | AQUA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 38.7 |
| c3c138dc-583e-3953-b358-bf1116600d86 | -18.47788 | -48.04566 | 2025-10-25 06:01:00 | AQUA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 037f40f1-0dac-39b4-90ba-6a8e03e2ee8a | -19.32823 | -49.08757 | 2025-10-25 06:01:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4300b9a5-0897-3c0a-bf95-839dd87493a1 | -11.71276 | -62.93554 | 2025-10-25 06:01:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0d75dde-ff0e-3da0-89f8-d2cc2cb89f89 | -10.6183 | -67.93285 | 2025-10-25 06:01:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30090372-594a-384e-8718-486b0898f2f0 | -9.27404 | -68.26411 | 2025-10-25 06:01:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2112bddc-d566-3d9f-b5fc-fa8aab097881 | -11.78308 | -63.18263 | 2025-10-25 06:01:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 64570ae0-e300-3edc-883d-0fd25de27e0e | -9.97432 | -65.11407 | 2025-10-25 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b88f23b9-a911-371b-aaca-75d14efef4c1 | -11.71773 | -62.93629 | 2025-10-25 06:01:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6651bcbc-814b-32bc-886f-72649612ebee | -9.92468 | -65.0116 | 2025-10-25 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25f71123-74c9-31f4-94ed-d242b05b16b5 | -9.97561 | -65.11389 | 2025-10-25 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86698c2c-8725-3e9d-bbee-df2892ef67a3 | -10.40557 | -63.09992 | 2025-10-25 06:01:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b0ee24e-93de-364c-ac1c-e118fab791d1 | -9.7233 | -67.47024 | 2025-10-25 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37c611ad-7264-342e-b3b3-f8549c25d477 | -10.62187 | -67.93339 | 2025-10-25 06:01:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cfbcfc8-3bb4-300e-8dc4-ad38bc225762 | -12.47992 | -61.05602 | 2025-10-25 06:01:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 779473ad-4497-353e-852c-a002c2206521 | -12.47943 | -61.06012 | 2025-10-25 06:01:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5d387dc-91be-3ff0-96d0-57f3546a31d2 | 1.6386 | -55.7455 | 2025-10-25 07:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 956f7c35-b41e-3eb7-99c1-37e453a60b9d | 1.6203 | -55.7457 | 2025-10-25 07:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 51790faa-7306-355b-a111-245bbff19886 | -16.5445 | -49.3399 | 2025-10-25 10:50:00 | GOES-19 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 64c5b779-723b-3124-baae-58573a3240a0 | -6.9706 | -43.48239 | 2025-10-25 11:19:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 6ac4bab3-4e22-35b1-9894-a0952c9a3554 | -6.33639 | -35.13723 | 2025-10-25 11:19:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| c7e50f3e-9f20-3de8-b849-762293d81fab | -6.97047 | -43.48981 | 2025-10-25 11:19:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 92ca1114-8cda-3c1e-83a4-7395a718e476 | -6.33793 | -35.12703 | 2025-10-25 11:19:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 56476df0-61b6-3b48-ad12-5dbf4925bd83 | -7.21665 | -35.32209 | 2025-10-25 11:19:00 | TERRA_M-M | SÃO JOSÉ DOS RAMOS | PARAÍBA | Brasil | 2514453 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0f126e40-3680-32d8-a750-1171d7143ba9 | -12.3901 | -49.9569 | 2025-10-25 11:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 92b1c2a1-441e-3356-9194-5886ec66bec0 | -16.5914 | -43.51711 | 2025-10-25 11:21:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 95ef88dd-6f19-30af-a765-47885e9fa192 | -12.3901 | -49.9569 | 2025-10-25 11:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| dac8a082-8f2b-3b88-9dc6-31d9898ac86b | -12.3901 | -49.9569 | 2025-10-25 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 0d615e0c-4ee2-32df-a18f-9aa6b34be5df | -14.9041 | -52.4566 | 2025-10-25 11:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| b499c49c-1c7c-3e97-86dd-b34d93558d4d | -12.3901 | -49.9569 | 2025-10-25 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| aabfd634-c613-3185-842c-55f525fada1b | -12.1195 | -46.7053 | 2025-10-25 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d6828591-d783-3aff-8648-b0b51044c5a8 | -12.1387 | -46.7026 | 2025-10-25 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 669eb7a2-b311-3f66-bbf5-d2176dadb1e3 | 1.6386 | -55.7455 | 2025-10-25 12:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a1a9bb0c-7d80-3628-b2fe-2ee7cae0e9ae | -12.1387 | -46.7026 | 2025-10-25 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ed4de317-3426-3d29-9fd9-3f3a49415970 | -12.1195 | -46.7053 | 2025-10-25 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 21269ba9-7abd-393e-9982-143fee761218 | -14.9041 | -52.4566 | 2025-10-25 12:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d6bf4cba-ecc1-397c-8422-ac8256776e3f | -12.1387 | -46.7026 | 2025-10-25 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 3c3fceba-e989-3c87-a063-fa71fce0afbe | -12.3901 | -49.9569 | 2025-10-25 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| facf3df0-7adc-3203-a3c4-113d36b8610f | -15.1927 | -44.0773 | 2025-10-25 12:30:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 119.8 |
| b4278b14-8de9-31db-95f1-85623232bdeb | -12.1383 | -46.7252 | 2025-10-25 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 2e0fc069-dd64-3194-95e2-4ab25125bab5 | -14.9041 | -52.4566 | 2025-10-25 12:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 0937f6c7-5654-3489-8524-8ef8f73d7db4 | -12.852 | -48.653 | 2025-10-25 12:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b178696f-48df-3c3e-99c4-dbd9f6dd5c4e | -13.9147 | -48.4112 | 2025-10-25 12:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b6ab2c35-6c4c-393b-aeb1-c5c2b5dbcbe0 | -10.9956 | -50.3774 | 2025-10-25 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 34720458-5de6-30e4-93ad-ec4b60087ede | 0.3589 | -50.9206 | 2025-10-25 12:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 1eebf789-1792-344e-bf88-fff9edcb9bf7 | -13.9147 | -48.4112 | 2025-10-25 12:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 829cd727-040f-3aa4-a5b9-5e8c3345d6d5 | -15.1927 | -44.0773 | 2025-10-25 12:40:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f8fbc6a0-ea12-3ca1-945f-576061611df0 | -14.8706 | -48.0822 | 2025-10-25 12:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f41dcdda-1b67-3090-9bf6-cea662d136cc | -15.1927 | -44.0773 | 2025-10-25 12:50:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 134.9 |
| c8bdb2bd-ee73-3dcb-9318-d6d5b5eafede | -12.466 | -44.5428 | 2025-10-25 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 61ac760e-ab23-335e-884d-4be8ade7560b | -14.9041 | -52.4566 | 2025-10-25 12:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| fb4c6381-6868-3ad3-b412-7c6ec0f03652 | -10.9971 | -50.2702 | 2025-10-25 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 6f2f3840-0109-39a9-91e8-7b3d2f37daa9 | -10.9956 | -50.3774 | 2025-10-25 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 5c6250be-7f47-37fb-ba3c-d0f7ba8e4ec9 | -17.34303 | -55.02461 | 2025-10-25 12:59:00 | TERRA_M-T | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 9d5ed422-8fcd-346c-869b-df73286ff0aa | -18.64024 | -52.1179 | 2025-10-25 12:59:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a965a3c6-e626-344a-90f5-c553229158d8 | -20.14172 | -54.52127 | 2025-10-25 12:59:00 | TERRA_M-T | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 4cb19bba-eaa7-3773-91cd-cabb1879782a | -17.34482 | -55.00971 | 2025-10-25 12:59:00 | TERRA_M-T | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| d86ce133-588d-375c-8d6e-9a02b2456ab8 | -20.1397 | -54.5395 | 2025-10-25 12:59:00 | TERRA_M-T | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 41b1e392-bc6b-347d-b96b-594c78a9a877 | -17.01952 | -55.9096 | 2025-10-25 12:59:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 6e07dc5f-86e6-3526-9cde-bd7828f7105d | -14.9041 | -52.4566 | 2025-10-25 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 507b2b97-0f3e-32fb-8f03-e266f541a839 | -10.9589 | -50.2958 | 2025-10-25 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| b1af2203-c324-3651-8500-ad716c8eb246 | -14.318 | -46.6143 | 2025-10-25 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 9bb9a06b-8337-3fa6-abb5-fedf630fc816 | -10.9956 | -50.3774 | 2025-10-25 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| f0cd38cc-9fe8-3c9a-bd09-2a335b666610 | -15.1927 | -44.0773 | 2025-10-25 13:00:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 224.6 |
| d7831ed8-db38-34f5-8bbf-5e11253b6535 | -10.9962 | -50.3345 | 2025-10-25 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ee0392c9-fd44-3f15-8448-f91c22a45715 | -12.2203 | -43.3103 | 2025-10-25 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 190c7baf-c7b9-39be-9ff8-1fe34ac34187 | -14.3375 | -46.611 | 2025-10-25 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0b59fb11-855a-3bef-a63b-b6867e3fcf0b | -22.23172 | -51.72729 | 2025-10-25 13:01:00 | TERRA_M-T | PRESIDENTE BERNARDES | SÃO PAULO | Brasil | 3541208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.9 |


[Clique aqui para ver as próximas entradas](README63.md)
