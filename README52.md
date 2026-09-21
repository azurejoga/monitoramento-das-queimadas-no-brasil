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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac152c27-6475-3083-87da-892cea14b084 | -8.18184 | -54.73288 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55557f0e-e004-3911-9dc9-526ae7fb13ff | -10.79905 | -50.75416 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b1d05f4-a625-3a47-9e55-49e128569cf0 | -10.44229 | -50.26347 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 535aa84a-4852-3d8a-8b33-d17925ea9d31 | -15.46108 | -48.41865 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb0a11cc-0772-340d-b40a-4ba751d1d2d8 | -13.25886 | -51.80444 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc9c8e7e-4dd1-3360-b4fc-51fb7f834647 | -10.6775 | -48.72023 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2c3c8e97-2bbd-3013-854f-3440157b3b2f | -10.76905 | -50.82074 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bdb168e7-f911-320b-b5f0-101b5d29ac80 | -10.38327 | -50.22315 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| db3739f6-800c-3178-a15d-6b092631532d | -11.15136 | -42.82132 | 2026-09-21 04:21:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7863d771-7f46-3f0f-996b-546d3477a606 | -11.43961 | -47.29215 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb208cd0-824f-3e2a-a6ef-6b9bb53428e4 | -11.02263 | -48.31951 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e875aa1d-ebd5-3465-a663-01b6a0368a22 | -15.44605 | -48.46378 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c4077e2-4bae-388f-af40-d3abfa43dc39 | -13.93755 | -47.83901 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60ed2be6-afa6-3074-8725-27710d4432e0 | -11.15361 | -42.8292 | 2026-09-21 04:21:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5b50cd52-d96d-397b-ad9e-7ee0fa3ed10d | -14.04946 | -52.07144 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 791d883e-822f-34e0-8cf5-9e5df09acdcc | -13.03193 | -46.96988 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 31ec1bc2-0df1-3515-8809-4843aa9673ad | -12.4232 | -45.05831 | 2026-09-21 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc324062-8502-3bc0-b5e6-4a44b349b88d | -11.09413 | -48.30839 | 2026-09-21 04:21:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e78d54bb-28dd-3014-bf81-11fc268ddb01 | -9.16373 | -50.0766 | 2026-09-21 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08040128-b27a-35ef-b663-2dd7df2803fc | -14.6138 | -52.11656 | 2026-09-21 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26046636-2dae-3ee8-96aa-39f46ac38dac | -15.4618 | -48.41441 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea9d71ae-fad2-355f-a818-23cdbda1888f | -11.40935 | -47.34124 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a59aa56f-5a9e-355e-9af7-fd1cf10d42f3 | -14.05713 | -52.10958 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60f04fa9-c33e-30f5-9cae-aaf5c2f55e5f | -14.9244 | -49.89513 | 2026-09-21 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b2206b0-f460-3ccc-8898-033e6326f58d | -12.53744 | -50.03954 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25a967b3-f87b-3a1a-9466-a9ba88e1ca4b | -15.45963 | -48.4706 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 45b594c3-8c19-3bdf-b9b6-78cb1c683274 | -9.81719 | -48.41169 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c9feccd-212b-35e0-8428-5d304141649a | -13.48151 | -46.92674 | 2026-09-21 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4f82b5f-1e91-3933-98c5-e016877cecc7 | -15.52489 | -42.65546 | 2026-09-21 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ec6132f0-c465-311a-aa34-bd22d3fac337 | -10.70063 | -50.77489 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9009e9f-aa0e-34ae-8a01-a59df85602fd | -9.81635 | -48.41651 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 919ea124-feee-3090-b70a-333fdbeeaf22 | -10.88022 | -54.06576 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46d7704b-1c80-37cf-b535-6d4d8b035ccb | -11.99422 | -44.8939 | 2026-09-21 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65685d0f-4515-3110-96bd-6a75263dbc45 | -11.10569 | -54.01859 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14644cdf-7f52-380e-a113-bf69801e986f | -11.25135 | -54.14621 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6698aa30-1f2a-34e4-b9c3-795ccf5ce32e | -11.04993 | -46.56292 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 623c43bc-ff92-39d5-87a3-7d252c4bab18 | -10.55194 | -51.29673 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dae3aa1c-2faa-3cf8-a54a-f8b4f4f66cde | -13.90251 | -48.58125 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9f17277-7a15-3af6-a31f-7c1e276588a0 | -10.70405 | -50.77692 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 720a47d9-bd5a-3629-8507-29741088cdbd | -16.04275 | -52.51515 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| af82ea7c-98cb-3902-8164-961d966d47c6 | -10.80037 | -50.7724 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8db57285-c6f9-3039-903b-b64097c5dc66 | -15.46113 | -48.47299 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90cf992a-9f94-3962-8d9e-a7008036918a | -9.82451 | -48.43787 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1162ef0e-b453-3a79-b9eb-4d54870dbb1f | -12.30818 | -50.69134 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25515c76-4f04-372f-8433-66367ea8d5ad | -8.60213 | -54.62516 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81f183ac-18ac-3863-bfaa-25293569c7d8 | -13.86271 | -48.59298 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71cdac2c-5633-3c31-8218-7698b77c988e | -10.91041 | -53.96765 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cadd102-cd69-3aad-aaca-fe8ee851526a | -14.61376 | -52.06794 | 2026-09-21 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df6cf9a5-2573-3e58-926d-e46ed841a993 | -10.79104 | -50.74817 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 4038e1dc-5111-307f-a9c0-eaeb863d2d1b | -11.08121 | -54.02859 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f0e20d0-c4f1-3e9b-b2f8-5f10ed3c630e | -10.379 | -50.22237 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d46d7521-15b1-3b4d-a931-ad6649a8e726 | -10.42379 | -50.2432 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 04a5a19c-841e-30e2-8dde-2636a6514cd1 | -16.68385 | -47.88754 | 2026-09-21 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d58164e4-4dee-3e13-bd91-8670de123341 | -14.70156 | -46.6825 | 2026-09-21 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c69b6aac-9262-3324-8892-5bf9be350168 | -10.38333 | -51.87095 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 990f128b-47d3-3e4b-9791-12b621fa2cb8 | -11.9506 | -46.48559 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40babbc1-fecf-3428-9bd3-1c212535b491 | -11.74396 | -54.56915 | 2026-09-21 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fd06b53-902e-34d5-990d-130da3921041 | -12.11205 | -47.04166 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fe79191-af2a-3aaa-8c33-ef8e39810922 | -11.09573 | -48.27644 | 2026-09-21 04:21:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3952767-683d-38b0-b9d8-0847e1e372e7 | -16.18345 | -51.11952 | 2026-09-21 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb21bb74-d183-3872-8e8e-d11f51c0868a | -9.97757 | -50.26019 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 500ce18b-7deb-3713-9889-416ec04f268c | -16.03114 | -52.50289 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 5f793e19-d7e8-3746-b9a0-60619e1d7aea | -10.37778 | -48.9187 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6995e828-bab8-3384-92f4-128ef133a117 | -10.39607 | -50.22549 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8d689b58-66e2-3a98-9f15-6c423c62433d | -14.92834 | -49.89553 | 2026-09-21 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b741ffc-2355-3bec-9803-7d6a06a53c1c | -15.45818 | -48.47919 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ddc3717-05ff-320f-991c-d21f7aaf8a64 | -10.46653 | -50.27641 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| eee95600-6a08-31ac-80d0-de1c03e17495 | -11.03805 | -54.1614 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 88fb3b3e-d88e-31c3-b07d-32f0315e3a94 | -8.17588 | -54.7317 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 728cfac8-2af4-375d-804f-cc51cff9f73f | -14.18346 | -49.59068 | 2026-09-21 04:21:00 | NOAA-20 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86bcdcf7-d071-356e-bd21-3404ce6b3d22 | -8.18713 | -54.77072 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 076844b4-0322-3a58-912e-9d9b97e1f935 | -15.05926 | -48.57684 | 2026-09-21 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f49e2354-80f6-3c64-a863-cd5b5c5b1480 | -11.02181 | -48.32114 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcd5381f-8087-327b-b79e-d5b993a9f553 | -10.8084 | -50.77841 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 21dc71e4-657e-385f-a0b0-8931fe11094f | -11.82423 | -46.84114 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 175a98db-3eb0-3236-b077-5037b790d401 | -11.03465 | -54.14932 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd65f08a-6040-3765-80f6-893454e397eb | -10.09525 | -50.25949 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7d061fbf-2a6b-364c-b722-f0410344836b | -11.34161 | -43.38517 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4f541ed-d078-3444-b4c3-394641446780 | -11.93726 | -46.50256 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 756257dc-03d7-3caf-9f43-97cfeca7bde0 | -11.88077 | -49.00911 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 462465b7-2fa1-37de-bff8-d05a1df7913e | -10.7662 | -50.81114 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96014c45-b3c7-32b8-848f-dabc1b38fb11 | -8.18681 | -54.70647 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8cfcdc2-5115-3a4e-94a7-9eb859b0d301 | -11.02443 | -54.1433 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5262211f-f7a8-3e25-86c8-bc072b55dd65 | -10.43801 | -50.26268 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 86807b88-b50a-320d-82ab-4af3993f1332 | -11.04807 | -47.67376 | 2026-09-21 04:21:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83814c42-a9ab-3040-a2c1-562f1fc48b43 | -11.89494 | -48.99657 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d60a1df-0335-3406-a9d3-b103606083aa | -10.78742 | -50.74301 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3ffcc823-a1c0-3b1b-8288-123cc5d22efc | -11.9818 | -44.99304 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27aeff1e-b84a-3899-b8b5-0d51cb114644 | -13.28756 | -43.54908 | 2026-09-21 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 064772d0-86dc-3a66-a6d0-25a56e990da7 | -16.02749 | -52.52154 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2ae8719-dafb-324e-8a7a-51a5b0414861 | -15.45962 | -48.48159 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 759e8c01-32ee-3c17-b0b8-20a4f7b5f218 | -8.18197 | -54.76518 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc6bc80c-e56a-36ec-b100-d3914959a154 | -11.04419 | -54.159 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71d6c668-1bf8-36c8-8d19-16de8c2c3c84 | -11.04227 | -48.29552 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4952797a-fa53-35a9-9eba-2f366839bebc | -10.79502 | -50.8243 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e35144b1-5f55-351f-be65-ef8b3b5f121d | -8.18114 | -54.76962 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06e17756-901d-3f05-b8f9-1711667d05c4 | -10.67962 | -50.73939 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 284129f5-730b-36c3-a533-a4d4010dea21 | -10.39534 | -50.22956 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| cbd04c5c-a948-3831-9293-770bbe473815 | -12.39048 | -47.00764 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd7bb02c-e712-33c8-b18e-0c9c5773e8b1 | -15.47007 | -48.40083 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README53.md)
