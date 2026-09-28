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
| b65b4285-7005-3c9f-96df-3acd6fee464b | -2.116 | -56.883701 | 2026-09-28 00:33:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c962fd8-a4d9-302e-8583-42d6912318a5 | -10.8183 | -60.737598 | 2026-09-28 00:33:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ebcc491-b791-380e-8c28-1fc87ecd18f8 | -10.4231 | -53.7789 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a033462-2d53-365b-8eb3-b45c55028b8f | -21.3866 | -48.709999 | 2026-09-28 00:33:00 | METOP-B | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8b876d2a-6f24-3a03-bbde-fa41fe1d2c04 | -15.1438 | -43.6366 | 2026-09-28 00:33:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| d7c4ba83-6806-3ba6-ba4e-56ddfc55e033 | -10.8162 | -57.224998 | 2026-09-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bdecbd9-b6f3-37e0-9162-6409938008c8 | -3.4101 | -48.348 | 2026-09-28 00:33:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91f90c0e-dbe6-3c02-a94d-51635367c53f | -11.1226 | -50.0569 | 2026-09-28 00:33:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3fd500f7-fe98-3b6a-907a-ae9451a7dfd9 | -6.6589 | -55.093201 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77546b9d-7032-32a0-90ec-64a51635e2e9 | -2.7657 | -49.487 | 2026-09-28 00:33:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acad0f8c-ae45-3283-97ef-9dfdcb71b53b | -12.1888 | -50.366402 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e922d303-36aa-36bc-8787-68df5d4db8ed | -7.8325 | -55.132702 | 2026-09-28 00:33:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aebdfc98-d810-3fce-bd06-9c5716883b29 | -7.8243 | -55.1418 | 2026-09-28 00:33:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e31a9c9-acee-31f8-a63f-ff9799e3bd4d | -12.1813 | -50.378101 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 587c99e9-960d-35e8-a21a-094ad7486190 | -11.1446 | -50.062199 | 2026-09-28 00:33:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f0d5c8b-be2d-38f5-9c60-036376099dad | -2.9907 | -54.740501 | 2026-09-28 00:33:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd24764a-2229-3376-ae70-3c68671dd283 | -7.6854 | -54.846802 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a26b70-df41-3c98-af75-cbac74504f3e | -12.8739 | -44.814201 | 2026-09-28 00:33:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a239cb24-fe64-3fca-afe3-82d63e769450 | -1.7401 | -57.181599 | 2026-09-28 00:33:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 089d0c1b-fe8d-3eaf-80e9-895594d6f9fe | -2.9135 | -54.131302 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09024465-e362-315d-9361-8f0f4421555b | -2.6531 | -51.742599 | 2026-09-28 00:33:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bab26263-967c-3b3c-8131-e368abec2f80 | -3.965 | -59.341801 | 2026-09-28 00:33:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85611300-86fe-3c1c-8524-ad934011da67 | -7.4638 | -55.005901 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f5c24f6-420d-3c2d-9651-ce12fa068abd | -12.6461 | -47.340801 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b12fbc0-941e-3c81-92e2-b5adc171c754 | -2.7916 | -57.685902 | 2026-09-28 00:33:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d8bd4f1-86ad-35f2-be4e-d61dacb6fddb | -10.1133 | -50.1982 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f50c96a9-15c1-32ed-b3ee-decdc84bd0a5 | -8.6594 | -48.964298 | 2026-09-28 00:33:00 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3541fbc6-0d62-3653-b6cb-d9d0670d0338 | -13.4556 | -48.597599 | 2026-09-28 00:33:00 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0a4b62ef-57c9-31e3-83c5-800d1f7c07f2 | -7.687 | -54.853699 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65087269-b2ed-34f6-878d-80de1a7a5ddb | -13.1521 | -48.541199 | 2026-09-28 00:33:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0866bb93-210d-3335-b151-fdcb56cf937c | -11.3443 | -54.1138 | 2026-09-28 00:33:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e871aab2-c292-3f5e-8ea1-506df2fdfc65 | -13.6842 | -48.812099 | 2026-09-28 00:33:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d4de331a-dc8f-3e28-be55-03263deb792a | -3.0686 | -58.0019 | 2026-09-28 00:33:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94f976b7-c2e2-371b-95cc-d0a69b6a4706 | -3.2237 | -54.315899 | 2026-09-28 00:33:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6793020-d975-3e4c-b639-2453f667ce71 | -7.6772 | -54.8559 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78b93677-a192-3152-8e70-dd3cd296fcb2 | -10.4229 | -53.8237 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60f6e2a1-8221-3944-adfa-8c6647725cba | -10.8216 | -61.4025 | 2026-09-28 00:33:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20ae7a41-152d-3bbd-811b-816c1f3c5a51 | -1.7672 | -53.758999 | 2026-09-28 00:33:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9060945b-1252-35fd-a3bf-46f314381fdc | -12.7396 | -47.301201 | 2026-09-28 00:33:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 962bacee-c8aa-3673-b106-9568db428391 | -12.8589 | -44.796101 | 2026-09-28 00:33:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc886cfc-d5fb-3a00-840f-8607a80fe0a8 | -15.2802 | -47.691898 | 2026-09-28 00:33:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ecf8aeda-212f-3a20-a6bf-6a4d89cccc64 | -11.0993 | -51.3484 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78b102b4-f622-3799-af1d-87fef6f38f7f | 1.6804 | -55.9557 | 2026-09-28 00:33:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74a8e71c-c626-3f1f-b1f5-6617d7a65702 | -11.0953 | -51.331299 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a115b0b-eb52-39ba-bfe2-2008a9cc4f2a | -9.9721 | -45.3512 | 2026-09-28 00:33:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1da608aa-21a9-3683-935b-049d8cc9089d | -11.0814 | -51.316502 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbf48909-bb89-34fe-a8af-20ede5e96846 | -11.1013 | -51.356899 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92510e00-7b18-35b6-8080-83addbe4fb61 | -11.0384 | -54.037102 | 2026-09-28 00:33:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5427d6ea-3109-3ebc-8eda-f54a095b1486 | 1.736 | -50.8606 | 2026-09-28 00:33:00 | METOP-B | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0d77084b-baf4-3318-a2b4-35320d376d76 | -10.006 | -50.138199 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3d6c2d-a133-3cbe-b863-9d09da2a75a5 | -10.4261 | -53.837799 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6163111-e235-3cec-854f-f3e6cf8a463c | -2.051 | -56.869598 | 2026-09-28 00:33:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8688828-0c84-34cd-858d-af151aa645d5 | -12.1454 | -50.357399 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39a80373-4f0a-3b46-b587-0b6cda56cb02 | -10.1679 | -63.042702 | 2026-09-28 00:33:00 | METOP-B | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9de0f664-c954-3ded-8a90-467915c143be | -13.5564 | -46.364899 | 2026-09-28 00:33:00 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 749466c5-7450-31e1-a32b-8f70bd13aaac | -2.7559 | -49.489201 | 2026-09-28 00:33:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc523102-1b35-38ce-9982-1986f44f47a2 | -12.6558 | -47.338299 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79fb7682-9cb4-3e29-9b28-0d8698c5421a | -1.7386 | -57.174801 | 2026-09-28 00:33:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66ead277-7197-39e5-94b6-67569d495294 | -10.0206 | -50.242199 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2226392-422a-3c96-a610-e6c83f41fa20 | -7.7188 | -61.233898 | 2026-09-28 00:33:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e276a702-18f3-31f4-a145-7e1786e1281c | -3.2128 | -51.050201 | 2026-09-28 00:33:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de1d67e8-6812-38d6-b557-5b397ef5275e | -13.9658 | -53.993999 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9e54a0a-5ec6-3c56-8f44-58398b129b67 | -11.3635 | -43.436199 | 2026-09-28 00:33:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5953f8b8-b63f-3658-8806-fc6d4d3fd322 | -1.0429 | -53.563499 | 2026-09-28 00:33:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 075ee2d9-02cd-345b-b1bb-b98801d6e743 | -2.5339 | -57.2281 | 2026-09-28 00:33:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00f1452f-ac49-3289-84ab-1b21f3c2680e | -15.2772 | -47.679699 | 2026-09-28 00:33:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53f1fa5e-953e-38c9-8d00-a2d748eb829c | -12.1955 | -50.394299 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb81a1b1-3f09-3536-8b13-5cff44852764 | -1.2287 | -54.1082 | 2026-09-28 00:33:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb26bb6-8a0d-3be1-8bbd-026dafe2413e | -11.3731 | -43.433601 | 2026-09-28 00:33:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fea25b07-22a4-39da-a435-966c1c3b742f | -8.2267 | -45.481899 | 2026-09-28 00:33:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 832b6aff-3fd3-31a0-b1d8-899eeec0b625 | -7.8678 | -61.165901 | 2026-09-28 00:33:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b421e9ff-7aa9-3445-981e-07ad6e045779 | -20.176001 | -48.589401 | 2026-09-28 00:33:00 | METOP-B | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 00c9f1da-3080-3ca6-9c66-d68697ec78f9 | -10.8178 | -57.2328 | 2026-09-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c80aed8-713b-3dd1-b314-c71b4c16d8ef | -2.9507 | -57.797798 | 2026-09-28 00:33:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16bd6855-e432-3c79-bbf5-36eb0fe0f28d | -21.168699 | -55.751499 | 2026-09-28 00:33:00 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a17bf442-38c7-31e5-b100-123da13ddf4e | -7.419 | -55.630001 | 2026-09-28 00:33:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a2b120-6f48-30ea-8cd9-34a4cfa2cefe | -11.105 | -51.328899 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11876e29-3fc7-3592-aec0-a2fda8966312 | -21.5116 | -45.108002 | 2026-09-28 00:33:00 | METOP-B | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5cb491ac-28c4-3b0e-bc4a-c079b2f98637 | -3.0696 | -57.639198 | 2026-09-28 00:33:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6976f365-ac90-325c-883c-a69e52a10fda | -7.2828 | -55.5741 | 2026-09-28 00:33:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 196b737e-9444-3a2a-b1f9-38654e159ba3 | -11.6966 | -44.5364 | 2026-09-28 00:33:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4b78a0e-4606-319a-8e64-3877f87be7e5 | -1.9245 | -52.152901 | 2026-09-28 00:33:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f75d1ff-2388-3e77-9243-65ed01bbeff8 | -11.1421 | -50.052101 | 2026-09-28 00:33:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1df66a-28d5-3a6e-8097-0b9eec134ada | 4.3099 | -60.819401 | 2026-09-28 00:33:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a5e77423-d610-3bb8-9f12-dbac991c5cee | -3.0128 | -54.205002 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86db9050-1ff2-397d-b4ca-aeed128ea7af | -9.8236 | -52.117599 | 2026-09-28 00:33:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef2d332a-ac0c-3c01-b463-1090e22aac0b | -3.5727 | -54.354801 | 2026-09-28 00:33:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70babd81-30a1-3dcd-8c92-b1decce186f6 | -13.3473 | -51.330898 | 2026-09-28 00:33:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 686a92cf-dcff-3c1a-98d1-d3cb3f25bea1 | -11.3701 | -47.444199 | 2026-09-28 00:33:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85604ee0-d336-3cd8-bd7b-60e7f757524a | -3.0702 | -58.008999 | 2026-09-28 00:33:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45a38e0f-5aa6-3b1d-9d62-60cc197be767 | -2.9523 | -57.804798 | 2026-09-28 00:33:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75657801-0974-3385-a7f3-881f58bcbd2c | -6.6987 | -45.606098 | 2026-09-28 00:33:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe2bb782-480e-3a33-9769-54df53f64846 | -11.2257 | -44.784199 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c5d53f8-4a1d-3686-b5d7-b9377de7b8f9 | -15.1152 | -53.8825 | 2026-09-28 00:33:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3df51986-5ca9-3c3f-bde0-cef97f8fb8b5 | -15.1038 | -53.877701 | 2026-09-28 00:33:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31008efd-0b39-3482-9271-231cfbc75d5c | -13.9756 | -53.991699 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8af29116-ef9d-3a06-a805-6bbf03af6887 | -10.4247 | -53.785999 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be0fc011-1c84-3391-b98f-b490c39a4f84 | -13.3883 | -51.329399 | 2026-09-28 00:33:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de2e10ab-3929-37d6-9919-54171b2d0c09 | -10.2105 | -50.000801 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4fec81-eb6a-3208-bb2a-0d5b719adbae | -9.075 | -49.872501 | 2026-09-28 00:33:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
