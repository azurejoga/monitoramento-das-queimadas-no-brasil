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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24dac92e-ba90-390e-8f4a-743c540b43da | -21.65222 | -46.23185 | 2025-10-23 04:12:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 91054211-d0dc-3150-98f8-e6403cac2cdc | -21.74012 | -45.64645 | 2025-10-23 04:12:00 | NOAA-21 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 377d6ba1-851a-32d8-bf7c-1ac761b5156f | -22.24849 | -49.92083 | 2025-10-23 04:12:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 992a25aa-ce02-38e2-bc3e-85d520a0e4e1 | -21.86606 | -53.31116 | 2025-10-23 04:12:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc77384a-f4e9-3e6a-abf7-958edf0cf46e | -23.77176 | -51.72664 | 2025-10-23 04:12:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ccf39464-4e02-3e49-850e-df338b317159 | -20.55356 | -54.55501 | 2025-10-23 04:12:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c25bfa9-f3d2-3c78-aa9f-47740c04a333 | -23.40578 | -46.42274 | 2025-10-23 04:12:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5a0766d2-578f-3ec5-9c7f-389b2c898107 | -25.22558 | -50.90063 | 2025-10-23 04:12:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e044be6-b02b-3564-9da2-4e3b57e0be46 | -23.65186 | -51.69088 | 2025-10-23 04:12:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ae7afe97-3cec-3f69-8979-0be65a6e3ad2 | -27.44931 | -48.44683 | 2025-10-23 04:12:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1ff0ec7f-c64b-3aad-bd23-5cf41b8473eb | -29.68132 | -53.86795 | 2025-10-23 04:14:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 836639c1-6cf3-3852-a463-0b7131dbb863 | -28.41443 | -48.94282 | 2025-10-23 04:14:00 | NOAA-21 | CAPIVARI DE BAIXO | SANTA CATARINA | Brasil | 4203956 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| cb161302-874f-31b3-8702-a8ac6777131a | -31.55952 | -53.72324 | 2025-10-23 04:14:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| fe18ca42-13e6-3c8f-9672-cc1d891f9124 | -32.86105 | -52.53088 | 2025-10-23 04:14:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| c85ca860-a13f-3a46-b195-1363a5b35fb9 | -32.85736 | -52.52988 | 2025-10-23 04:14:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| d3574f65-d13f-3037-9fcf-c56ea7b6af46 | -29.68103 | -53.86579 | 2025-10-23 04:14:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 8c917a09-afa0-36ca-8adc-3d6a52ea8317 | -17.6167 | -46.614 | 2025-10-23 04:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b1d8519e-b273-35d7-b0a2-df1bcff54896 | -3.0168 | -49.4906 | 2025-10-23 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3cee6231-2dba-3222-8ecb-fedceecaa9e4 | -3.0169 | -49.4694 | 2025-10-23 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8391429a-8a61-3bfd-b125-3ca7364f1480 | -9.6295 | -40.3392 | 2025-10-23 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 60af7f68-3654-37a8-826b-2f4daaf2647b | -3.0169 | -49.4694 | 2025-10-23 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 44bb8d04-93ea-3f13-96b9-05edee4633a2 | -17.6167 | -46.614 | 2025-10-23 04:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 693db983-aa52-38ad-9ed7-c812f3627c2c | -3.0168 | -49.4906 | 2025-10-23 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7772216c-8c47-338a-a42e-ce04fb5c38ee | -12.0036 | -46.7667 | 2025-10-23 04:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 976f9230-36ee-34ee-b1e1-42a1946bad06 | 0.38098 | -50.94157 | 2025-10-23 04:34:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc922f4d-ea48-348a-99fc-fe51aeb01671 | -2.9936 | -40.18894 | 2025-10-23 04:34:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea301cd8-2396-383d-82dc-273c1005245a | -1.07666 | -46.60587 | 2025-10-23 04:34:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9d73979-c894-36b4-9ccb-42407a4231ce | -2.23603 | -51.99632 | 2025-10-23 04:34:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80e110d2-8413-3ed7-ae6b-5d0e85067720 | -3.79988 | -40.84636 | 2025-10-23 04:34:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc701cf7-d5ea-35da-a1df-a63c9514fa02 | -2.78019 | -48.6784 | 2025-10-23 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d364b8ac-d0aa-3a26-8992-7afd8d484122 | -2.78019 | -48.67839 | 2025-10-23 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5dd1383e-c40f-3e5f-8ee1-d46cc743a8fd | -1.89673 | -54.07188 | 2025-10-23 04:34:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe313f67-8a5e-388a-811b-c6ca5c315f7e | -3.79607 | -40.84124 | 2025-10-23 04:34:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 30e8fa87-09c3-3226-b07b-6482e60ad409 | -2.73988 | -48.4287 | 2025-10-23 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d5b361c-08b2-3e84-977c-91f7bc073cec | -2.24821 | -51.92245 | 2025-10-23 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a2b2883-28cb-38ff-9d61-9260a3d4cfcd | -3.6653 | -39.48444 | 2025-10-23 04:34:00 | NPP-375D | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c9f58e40-4ea1-381f-a523-71cbc0d30009 | 0.98456 | -51.29305 | 2025-10-23 04:34:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2ad5b14-d519-34e2-baf5-41caba7d2e9a | -1.49212 | -47.81205 | 2025-10-23 04:34:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a13922a-567a-3cf6-93b6-418d3522f34b | -3.1175 | -45.23487 | 2025-10-23 04:34:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 06aadcd5-33b8-32b2-b93c-0dabc6dd714b | -2.29484 | -47.99483 | 2025-10-23 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e5dcc9b-445b-3b0f-8633-0fea1762a3ea | -2.73734 | -48.29301 | 2025-10-23 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6e9376e-fd3d-3085-9f9b-30265861c535 | 1.65707 | -55.75927 | 2025-10-23 04:34:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d52b624-6e9e-359c-8014-17b5831da81a | -2.73341 | -48.29603 | 2025-10-23 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e884944-580f-3c05-a2cd-5c4477dd2353 | -2.11187 | -47.10061 | 2025-10-23 04:34:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fee314f-ab12-35d0-a272-686e597e73a9 | -3.34952 | -40.42473 | 2025-10-23 04:34:00 | NPP-375D | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7e876e9f-a863-33c7-9b09-010d00ab5678 | -2.2479 | -51.92291 | 2025-10-23 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c89a297d-4241-3663-b958-ecea33e2a3e1 | -2.44838 | -49.00819 | 2025-10-23 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 385dac70-1ca4-3aa2-929b-a259d25a870c | -2.87246 | -40.42474 | 2025-10-23 04:34:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0741be9e-abd9-3479-976c-474325ad7390 | 0.98399 | -51.28949 | 2025-10-23 04:34:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 109a37d5-4573-387c-9af1-9b71f780e2a0 | -2.25224 | -51.9231 | 2025-10-23 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f663ad11-8ff7-34f9-8029-1fc6b480e7cf | -2.16096 | -51.94855 | 2025-10-23 04:34:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 245223b7-7012-34cf-ae7f-b64e45650345 | 1.6565 | -55.75558 | 2025-10-23 04:34:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba86e968-5d4b-38ad-a36c-c2f1cd20dd5d | -2.74071 | -48.29354 | 2025-10-23 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcdaa697-df74-3059-adba-d84e12d0e7b6 | 0.38884 | -50.94033 | 2025-10-23 04:34:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f9a8054-f8dd-3f28-821e-7ba3a27792b5 | -2.25223 | -51.9231 | 2025-10-23 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11e0d7cd-12aa-396f-b61a-a8a88b9435b0 | -2.51809 | -49.13759 | 2025-10-23 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91832b66-1733-3577-8f30-032c6e4576d6 | -1.8959 | -54.07686 | 2025-10-23 04:34:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f66e9c81-50f3-35d2-9d69-a9177407ab8b | -2.25626 | -51.92376 | 2025-10-23 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7eb7006-be87-3540-8e7e-1c2838bfa1cd | -2.83719 | -48.56139 | 2025-10-23 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fd2a9c1-ff3a-34a2-bf7c-1407596aab24 | -2.73454 | -48.28893 | 2025-10-23 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea595f2e-f874-3182-ad75-e4dbcac16833 | 1.34503 | -50.69161 | 2025-10-23 04:34:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b94f7e67-c98e-3feb-9f2d-d86f8427f3d7 | -2.31122 | -46.99395 | 2025-10-23 04:34:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c10920f6-81d1-382b-aaea-bfd0a0e8d005 | -3.79607 | -40.84123 | 2025-10-23 04:34:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b153c316-2285-37ae-8907-e135c7afedf4 | -2.73398 | -48.29248 | 2025-10-23 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55644c7d-1fb9-326b-894d-c4aa8f05776e | -2.44473 | -49.37182 | 2025-10-23 04:34:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be3c8e5a-41a3-39fe-8009-43851dabd654 | -2.24763 | -51.92593 | 2025-10-23 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e6b397f-fb82-384a-a310-812eb62b2511 | 1.6565 | -55.75559 | 2025-10-23 04:34:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e00ae5d0-8636-34ab-8fa3-b177d6b7f79d | -2.5646 | -49.50174 | 2025-10-23 04:34:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de50625d-c011-3551-9613-cc2d12cd91d2 | -2.44473 | -49.37181 | 2025-10-23 04:34:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9801eb4c-e930-3428-a2db-6c1cae81b999 | -3.34952 | -40.42472 | 2025-10-23 04:34:00 | NPP-375D | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 950342c5-4ee8-3868-8a68-3f1eaec80e45 | 1.34424 | -50.68667 | 2025-10-23 04:34:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bed1d795-de2d-392f-9745-481656de5389 | 0.38491 | -50.94095 | 2025-10-23 04:34:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79a82390-70e8-38f3-ae55-2bef5dd1bae8 | -2.43721 | -48.44027 | 2025-10-23 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f516bc4a-2c13-3d98-8847-035e31266215 | -2.43642 | -47.18659 | 2025-10-23 04:34:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e9b4515-5d2e-35e3-b8c4-71800f943c54 | -2.7365 | -48.42816 | 2025-10-23 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f43c92c1-4ec2-34f9-81d1-a9da577c1a7b | 0.38805 | -50.93536 | 2025-10-23 04:34:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9ff3920-7131-383a-8b59-cc8f10561c61 | -2.44411 | -49.37566 | 2025-10-23 04:34:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19dd6caf-70e0-3873-8fb1-ad2ac3669ff9 | 1.34422 | -50.68969 | 2025-10-23 04:34:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a409a40-563b-3ad5-87a8-e210e7b7f2db | -2.56523 | -49.49784 | 2025-10-23 04:34:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb3db3f3-47a3-3145-93ac-119a549d992a | -2.83381 | -48.56084 | 2025-10-23 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c8e537b-f2aa-3ab2-9165-a1ed863aa4a2 | -2.23625 | -51.99695 | 2025-10-23 04:34:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab7db831-010a-30e3-81bd-4e056f111179 | -0.86866 | -47.55959 | 2025-10-23 04:34:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53d1fea4-9aa4-39ae-b574-f104b57e9c90 | -3.11807 | -45.23115 | 2025-10-23 04:34:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78233bce-e598-3173-8e68-5d54e574b81d | -2.23603 | -51.99633 | 2025-10-23 04:34:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f5bc854-22ae-323f-bee6-a15b654f73fc | -3.11406 | -45.23434 | 2025-10-23 04:34:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7f395a85-0147-323c-a8c3-fb836138e555 | -2.25166 | -51.92659 | 2025-10-23 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d149b2-f01e-33ed-b45d-abd98c1c26bf | -2.25569 | -51.92725 | 2025-10-23 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a24fc11-d52a-3eed-9330-7e6487264347 | -2.42838 | -49.26812 | 2025-10-23 04:34:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2ce6c5e9-23cc-37dd-b501-30a292a0b08e | -2.16153 | -51.94503 | 2025-10-23 04:34:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23586653-2bc2-3e54-880a-5ca074c5236a | -2.11133 | -47.10405 | 2025-10-23 04:34:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c8097fe-f758-312a-9b92-5a6e4a8fd9db | -2.73791 | -48.28946 | 2025-10-23 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c72747ac-074b-396b-ae96-9b372dd349c3 | -1.89474 | -54.07522 | 2025-10-23 04:34:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f25a5617-4692-3ac1-9966-4812aa21d7e0 | -2.25281 | -51.91961 | 2025-10-23 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d98b09a8-a6ba-3c2b-bed1-ac92f6fb9f8b | -7.41963 | -46.65127 | 2025-10-23 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05eb4c9c-3f98-3e7f-af50-617ffd7793ea | -3.47458 | -50.07996 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04089bcb-78e4-31bc-bdcb-84ab2b0bc65e | -8.35281 | -46.1906 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc12658a-cc4f-3611-8599-111a9c0be3ff | -6.30196 | -41.88396 | 2025-10-23 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2c83d391-b9ce-36c0-b1cb-09fe93f7ad2a | -6.28198 | -47.01409 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91ce58d2-710c-364d-a4f4-4c798055c276 | -6.60557 | -44.21337 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e94e17d8-537c-3a50-b146-69837289a04c | -6.78949 | -45.44018 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
