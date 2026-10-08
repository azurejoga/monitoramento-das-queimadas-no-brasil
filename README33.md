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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef2d8dfd-bf0c-37dd-9835-4768712dc535 | -6.0982 | -53.495701 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d4fe828-74ef-31ae-bfea-2e324d81dbd6 | -1.476 | -54.542198 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aec53f5-1f5a-3329-80c2-03cec3148c40 | -1.0035 | -47.661999 | 2026-10-08 00:48:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7e12409-917a-3f88-b4c6-6a6cb5880c38 | -3.31 | -54.047699 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc63553d-cff4-3326-a579-882103300694 | -3.0383 | -54.2117 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c461231-a89a-3253-b473-23b34c7d1a5c | -11.6301 | -43.6987 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa6cf3ec-08d8-3a24-8e1d-d4e948a0a2dd | -3.3001 | -53.8685 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58feb73b-0bfb-3000-a3c0-9f10bfcff8db | -10.2488 | -49.670601 | 2026-10-08 00:48:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 728f6c8c-3547-33f0-af67-2cc86ceb9dc4 | -3.0851 | -54.281799 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce8d7e8-8b89-39c4-8392-d75e9a62f1f6 | -3.1195 | -53.7995 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27567cbe-5008-35c7-a6bd-ee413f3ca72f | -6.8867 | -43.718102 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e33eebf9-55d2-30e0-9518-e882d570cc3b | -3.5169 | -59.343601 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9f5927a-cca0-39f3-96d5-19110684ee49 | -6.3103 | -43.3428 | 2026-10-08 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 561ba920-dc38-3273-a49a-25f0a11f569d | -3.0221 | -54.231201 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 512799e9-6bc3-3b57-8396-3eb6d9e2fd0b | -6.9582 | -45.275398 | 2026-10-08 00:48:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43f84890-d6db-3322-9571-6b0b24762a92 | -11.6464 | -43.681301 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13784c33-8072-332f-b478-b844156e8cdf | -5.7409 | -53.4627 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 008997b2-f447-35a1-bbdd-7ff05da8c940 | -2.7911 | -54.0756 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6863e817-4895-3132-adbe-1965dfb19e34 | -3.0171 | -53.8922 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24d70e7a-4298-34e9-9ba6-dae7f8c0e8b7 | -3.5939 | -54.573002 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98e16c7b-8253-3f88-97a4-f97ceb278695 | -2.9506 | -54.1432 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6360aedf-5803-3ccd-bf84-c6b2dc33c4ea | -3.1011 | -53.718498 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faa9a1f0-871d-3735-9151-ef757009cc46 | -2.6436 | -56.551498 | 2026-10-08 00:48:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4c1914-d1bc-3927-83b2-be4f32c3190f | -7.4024 | -55.581001 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8071e48e-54ae-3e47-af17-406582a34098 | -3.1797 | -50.555302 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 834e1b9a-e41d-3083-87d1-818fd924cd1b | -3.592 | -54.564999 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46a14b51-6855-301e-9faa-abd618397dd7 | -11.391 | -46.695 | 2026-10-08 00:48:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04cf71ae-edf7-35ba-9f7a-3b0f4c34ed92 | -4.2956 | -49.095299 | 2026-10-08 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e74ce44-5b1d-3377-b849-8efcac4c6423 | -9.1586 | -49.818901 | 2026-10-08 00:48:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f75d334-651f-36ca-9f6c-b69bb20f4aa0 | -6.9274 | -49.6297 | 2026-10-08 00:48:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd586271-ca31-3ae3-b6b2-b8db3117f75a | -3.0037 | -54.060001 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b580c1d1-5987-391e-924d-8fbbdb541791 | -3.0946 | -53.735401 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2e13b0-2054-3d7d-aada-688dfac727ba | -3.1453 | -53.7318 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc41c972-78e0-36f0-8c09-5cc15a7e6710 | -3.2769 | -50.038799 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe315b4-a086-389b-a36d-e873131fc2a8 | -3.8709 | -50.421398 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9c50e50-1937-39a7-89cb-fcf17477adcc | -3.5943 | -54.665798 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbf96848-153c-324d-ad69-5d8040cd4792 | -5.7085 | -53.501598 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9788d69-0797-302b-ae3d-643335eec03d | -3.4817 | -54.623001 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 551da0e4-cf08-3cad-865d-631e17c1e8a7 | -6.2335 | -52.680199 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d45a71af-8bdc-3f5b-9693-a0e812b61fbe | -3.5802 | -54.694401 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68bbc325-750e-34d5-8bcb-208e5c70c958 | -5.9616 | -55.369999 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53fbde32-a523-399a-b31a-68e42dc5bcf7 | -13.3035 | -48.6852 | 2026-10-08 00:48:00 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 886f8e5f-6016-338f-90d5-f0e5f332a62a | -12.1998 | -48.419102 | 2026-10-08 00:48:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba205c29-d9d8-3515-89c3-09dd7b06b9ce | -4.3496 | -43.817101 | 2026-10-08 00:48:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23f6483e-1301-3d82-8782-7580aec9c5c2 | -3.269 | -54.048801 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2f445c8-3282-3a58-89fa-92ad6357a73a | -3.0285 | -54.0783 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9464897a-5489-3476-b9c2-42028c59ac0d | -3.0215 | -54.183399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 176abcde-8e96-3b29-848f-a873eaee4e73 | -2.9224 | -54.109699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1307f143-8072-30e7-b66b-f5fa4aba9ae8 | -2.8803 | -54.150799 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67dc7704-ce58-3767-9fbd-6886b999d809 | -3.0568 | -54.2477 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d41a742c-0ec1-3979-a3d2-db64f07447e5 | -11.0215 | -45.462898 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a94a607-759a-37ab-bc29-0beaa6609696 | -13.7814 | -52.809502 | 2026-10-08 00:48:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce2c6e3-4338-34f0-a1c6-e1c0931596eb | -2.8407 | -59.106098 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4af8858-2b3b-3e83-a16e-57823a34004d | -5.7393 | -45.179901 | 2026-10-08 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13ba4006-193f-3dc8-8352-ad30bc7fa33a | -9.1602 | -49.825901 | 2026-10-08 00:48:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af375554-4126-31be-bdce-8acd8cd97f8c | -3.2874 | -54.084599 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b9daa8b-b165-3d83-934a-ed4f92275765 | -3.1692 | -54.742699 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a79bc869-9774-33fa-aa02-bc20815d75d0 | -2.4723 | -56.1134 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eafeffa-4d73-31d4-942d-b61045bb0880 | -4.1422 | -54.040001 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db8dd065-812b-3f26-85fe-e5a2080a48b0 | -3.0435 | -53.917599 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 003dc118-571a-3a73-9277-ae2d265f8c1e | -3.0971 | -54.198601 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56fd3d53-1e7f-3668-8306-2ed95d46ff59 | -3.1699 | -50.601799 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b63136c-97f9-30d3-9ad3-d8fcdc133ce1 | -3.2716 | -54.694698 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8cade5f-e24a-39e5-9a79-1239a1b435fb | -3.3022 | -49.126499 | 2026-10-08 00:48:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eaf7e7b-3388-339b-9a8f-776c90ea9c81 | -2.5719 | -56.190102 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9449276-d207-3d74-9ad9-a184195d1a82 | -3.8595 | -50.416599 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a1d2ac-abce-37d0-88c5-611603d73a4e | -2.9846 | -54.111801 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3faffc02-f78a-3e53-989b-652f81c48fec | -5.6936 | -53.481098 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f39059e6-e0c4-31df-930c-5120a6663c3e | -6.2483 | -52.8825 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 202cce62-7a8e-3fcc-81de-72d3b44b11a8 | -2.9697 | -54.0914 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de6d43cc-baf0-3c4a-a32b-5eaf1ea9422f | -14.9181 | -48.120899 | 2026-10-08 00:48:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 99151ee2-2091-32b0-8f27-2bea8a8ff675 | -2.2226 | -53.7071 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47c8f292-eebf-3aa9-9a88-aff503f12c05 | 1.7097 | -55.612099 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4b637ce-66bb-34be-9af8-03140d7a4fcb | -6.2106 | -52.8526 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 118dd90f-2ee4-3b7b-aa0c-a0e7b65edd44 | -5.9658 | -55.388901 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1c47c89-582a-3ce0-bb9b-3614c90e2729 | -3.8399 | -55.981701 | 2026-10-08 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e1d4f00-0c43-3040-81b0-69ed7709b0dc | -6.2351 | -52.687401 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a25e2eb9-2cb0-3495-922d-85f50d2aa35d | -5.8705 | -50.1008 | 2026-10-08 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b72c79cc-a2d8-332d-806a-0040ba3ed918 | -6.3903 | -55.2672 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5839a54c-6018-31f9-a1d0-d123a599f70e | -2.3828 | -57.892799 | 2026-10-08 00:48:00 | METOP-C | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21a5f537-1a7c-34c3-9859-8165ebeb1dc3 | -2.4039 | -51.306099 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7d93a39-ae24-344b-abbe-97f6178af303 | -3.0198 | -54.1758 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d29fdfa-f2da-3a45-b3a8-0ed07e84c414 | -10.445 | -47.279301 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42e71d8e-9112-312f-bd81-b57560e880a0 | -10.9875 | -45.408401 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ecb2aa5-05e1-3acc-a537-39b35d9647a7 | -4.1387 | -54.024601 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2daecec7-6e74-310e-9f73-1d1c7a11d5f0 | -5.8572 | -53.476799 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc49a50-5c98-3cb0-b2c1-10298e3b784e | -6.8715 | -55.589802 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2dbea31-c485-36a6-858f-ed43edb802f5 | -3.1582 | -54.105202 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5ef6e3b-aed5-36e0-848d-d21a34b4b1b7 | -16.8566 | -40.587002 | 2026-10-08 00:48:00 | METOP-C | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31d8eaa6-5db8-3a01-8c43-4486a79403a7 | -6.24 | -52.846001 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b873a282-d4e6-36ce-96ac-90bf6cb71ac1 | -3.0585 | -54.255402 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc3be200-1fa5-384b-97cf-405758743904 | -5.6774 | -53.500599 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d01d0843-c577-3ad8-9971-f8ab66303b1f | -3.5822 | -54.5672 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4e8bac4-2c41-304d-bcb0-e29af4fc58b9 | -3.0613 | -54.2225 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c6a2899-ebbd-39d0-90be-75eb79417872 | -2.7945 | -54.090599 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52297f25-2617-36e5-a0a5-6cbe9746f02f | -3.0225 | -53.9613 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 525f38d8-6dca-351d-a20f-66a8fb269f78 | -13.8009 | -52.805199 | 2026-10-08 00:48:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f212d07-4e23-3fb3-85b9-6a9d0a292103 | -3.2314 | -53.883701 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c8d3ca2-b08e-382f-b611-3f75a3401c43 | -1.803 | -57.101601 | 2026-10-08 00:48:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 552e915f-a0b2-3d6d-890e-56b4327f19d8 | -2.48 | -56.101898 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README34.md)
