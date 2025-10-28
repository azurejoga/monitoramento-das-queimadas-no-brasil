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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adad9abc-aed1-34c6-b61a-3cc2190144a1 | -8.47801 | -48.21546 | 2025-10-28 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ed1c313-67d9-3222-a923-fca1f2493405 | -10.92889 | -50.27333 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d6663ec-3114-324e-98c4-88c9bb12ca57 | -8.57492 | -47.14826 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5354ad0d-dd05-3e6d-8a48-8ecc7137be12 | -10.88304 | -48.38147 | 2025-10-28 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 110fca37-9cda-34fd-ba98-9d9f1047c168 | -10.99825 | -50.36706 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3894b7f-6881-337f-86f4-eee8e60dea79 | -9.9605 | -47.11597 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b01343f-d37e-3248-850f-a5f71e4b06e2 | -9.27172 | -45.57693 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89242e7d-69a8-38e3-974b-f91e140863e8 | -13.94279 | -48.41837 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b12f5f64-c185-37b5-9f16-a6b6d7873b63 | -9.46737 | -46.88045 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91e2c7c4-30ac-38f9-b7d7-5be182760200 | -15.1735 | -47.21852 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57286c08-8267-3075-af6a-9a5d7639b1a8 | -13.63044 | -46.46848 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0194dc5a-bc09-365c-b2d6-52d787376dd7 | -11.35399 | -46.09059 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7011acbd-c6d1-33a5-8642-72f50bf8209b | -10.58795 | -49.79621 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 09ec530d-6262-34bc-82ac-30ba23f751b3 | -10.76113 | -47.9019 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47781979-8db8-3291-98e5-e51f9443a3b8 | -14.66807 | -48.40823 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8ceae09-9cbb-3f69-adb9-62952c07ff28 | -8.1882 | -48.17525 | 2025-10-28 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6b07468-8fea-3529-a4f6-ef287879da4c | -13.90845 | -43.8984 | 2025-10-28 04:44:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 872e5dc3-5a46-36e7-8e3e-188ae7ef3d0e | -10.92445 | -50.25819 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8e57c38-5238-3ec4-af5b-89b4d687d7d6 | -10.92167 | -50.25413 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce2dcdb8-2f75-3f32-ae45-aba2407c19b4 | -8.63309 | -47.70988 | 2025-10-28 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b606593c-5547-327d-a3ff-b5889293ee7c | -14.53168 | -47.99291 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05434763-45be-3ff3-b939-aa8330c5809d | -14.763 | -44.9646 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70f6ea44-c103-3153-b08f-a8774a1fba13 | -7.12781 | -55.11616 | 2025-10-28 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b8b72e1-3d2c-39e0-81e2-3759d2cdc49b | -10.56956 | -49.76065 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27d1622e-5b02-3ebf-a99b-f11d2eb64af1 | -10.307 | -47.16338 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 390694bc-8b49-3f54-9489-51a3788bc613 | -9.963 | -47.09904 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d36d4f10-349b-3f9d-8426-483e210f8d2d | -10.24142 | -52.69353 | 2025-10-28 04:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42eb2437-669c-3eba-9377-3e23121c1fbf | -10.86623 | -46.04577 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbeb9f82-c8a0-3881-82aa-4f227ceb2776 | -14.54751 | -47.98129 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fbfb7cd6-5002-3763-bb54-17399f3c407f | -10.84525 | -47.89411 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d64609fb-f1f0-3cc3-8bcc-e5dfc1db77ca | -13.25 | -47.96244 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d4d85c2-353a-3e89-bf32-97ace2fd1adc | -15.15778 | -46.60489 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a186a54b-80ea-3ed0-bb59-17731575d014 | -10.75895 | -44.75601 | 2025-10-28 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 36b42ddb-00e0-318e-a5f7-3696257021b7 | -10.88767 | -48.37432 | 2025-10-28 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b84cb73-7464-315c-9006-c3ff836d79b7 | -11.07461 | -48.33141 | 2025-10-28 04:44:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 984c2ae3-7202-300a-989c-25f188904f6d | -13.53213 | -47.16488 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8cc5e26-8f92-356c-84bc-de07d1e4fe2a | -10.92279 | -50.26874 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7132a43c-531d-3130-9dc0-188fa33b2c50 | -10.5618 | -49.78842 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2365c66-6c79-3617-9151-ad280c3f4413 | -9.29601 | -45.21741 | 2025-10-28 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f39412c8-e17d-3fe9-9d58-60cbe67c1e2c | -9.13898 | -45.86118 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3766cdd-311e-32bb-9e1f-7921f9dd25ad | -10.88608 | -48.6339 | 2025-10-28 04:44:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9a34183-0dfc-3480-9e71-0cc7af786453 | -12.29981 | -47.44048 | 2025-10-28 04:44:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec11fa20-94e0-392f-91ac-bbf822b01ec8 | -9.91649 | -47.67911 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99271465-bba4-3297-8461-c643a9abdfe2 | -15.20189 | -47.39546 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fb1ad32-07df-3508-aca1-385601f75794 | -13.56039 | -47.15615 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c15b126d-15cd-31aa-877e-37867172c407 | -14.31324 | -46.5154 | 2025-10-28 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 30bddd96-4063-3e8b-96f7-f1b61fa36cad | -12.25974 | -51.33179 | 2025-10-28 04:44:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b62edda-5184-3fee-afa5-51ef400fe28b | -10.58515 | -49.77038 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8da1f28f-4c88-36d2-be6b-8fce2c4eeb70 | -10.56571 | -49.80717 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b33026bd-13ec-33e5-867d-7fab57cd0230 | -10.56459 | -49.79249 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b996a43-3312-32ad-ac9f-32a124e337ea | -10.91009 | -48.01226 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6cc0c22b-2fff-3185-8b59-767609639644 | -12.19115 | -47.01974 | 2025-10-28 04:44:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0225cc98-6fdd-3968-8b45-6c088ccbffc9 | -8.17971 | -47.30804 | 2025-10-28 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c753ef0d-cfe1-3217-9172-18aaa63b3dca | -10.07945 | -50.52857 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f58c610-b5bc-3051-8da2-503a6256cdad | -15.15341 | -46.598 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b20d653b-f177-3d1c-9339-a32ffaa88627 | -13.23239 | -47.10871 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9034c51-0c35-32c0-aa8e-e34c65115ed4 | -8.48738 | -45.56582 | 2025-10-28 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e71a75e9-8bb4-3435-b6f9-8c512e048405 | -9.89094 | -44.9062 | 2025-10-28 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d42244a4-779e-34f3-9baa-235dd1d5af50 | -9.33776 | -47.8401 | 2025-10-28 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f1c0287-6a50-3c5b-9261-da4edfa737e2 | -9.47579 | -46.89914 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2aabe882-f685-3ecf-907a-a8de52eceb5f | -8.87287 | -50.33066 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de44cc76-fc05-3d32-9936-1b4613c68bdc | -8.23149 | -46.93648 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d87432e1-895e-368d-bff8-acfd2aba007e | -12.62763 | -45.08289 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f289cb3-bad0-3e70-8776-6126ef8b52fb | -14.42572 | -47.84989 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5b057d9-a931-33df-a1f3-06f9014ae425 | -9.91589 | -47.68311 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4dd1630-0c7d-31be-97c1-37ec60e7fbcd | -13.73544 | -48.43585 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 080f90f5-2886-3293-9e74-4f694845540b | -11.64536 | -48.52909 | 2025-10-28 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e15e3af2-9526-3b5c-8326-4815e65590ae | -12.07992 | -46.39436 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a2f38386-b5bf-3b2f-b632-11486ed8fd2b | -10.92887 | -50.23003 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5b9797a-9d70-3e71-b695-7fd2c10e43d8 | -14.5366 | -47.9791 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a9ac6c9-4c96-3f48-9f0c-818f60546095 | -8.10386 | -55.08044 | 2025-10-28 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fc89e38-7295-3acf-8276-841afb252d69 | -11.13813 | -47.04541 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b13838b8-a731-302a-977a-6548207931cf | -13.27828 | -47.97088 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fca9412-74af-3460-ad8e-8eb9cde4f31d | -11.73158 | -49.33143 | 2025-10-28 04:44:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4c08959-98b7-3670-bb52-9497cbaab7ce | -10.6629 | -48.50049 | 2025-10-28 04:44:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baa8c468-f4b0-3a44-801d-b8f7b91b30ec | -13.86088 | -48.51291 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5665e6f5-6517-313b-ac13-9c4b93a02473 | -9.59328 | -46.85824 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc8c1344-0d87-320a-a1b2-b5e2b027bf2b | -13.31888 | -47.44129 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02d311fc-66fe-3a5c-af4e-9ea441242547 | -9.46434 | -46.87567 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2034ec68-d68f-3a77-959f-9d3e6ce6ef13 | -10.32721 | -47.2267 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89fe1875-f8f5-3a4c-b88d-403f3b9f7354 | -9.96112 | -47.11175 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8a960a9-2096-3239-b66d-98fc674c41c9 | -9.88842 | -44.89436 | 2025-10-28 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1c80438-73f8-319c-b746-616102bfc99c | -9.46372 | -46.87988 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9349765a-6a4f-3294-9582-8849f0e2ea86 | -10.54656 | -45.05325 | 2025-10-28 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb3bcb23-a0a1-34b3-98e5-17d6704914dc | -14.48063 | -47.93219 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5be2a9d5-c2ba-3fdf-9ffb-9b22e80a258c | -14.2974 | -44.534 | 2025-10-28 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1cc7ca1-a6c2-3531-9208-e950e0c28960 | -10.31944 | -48.78461 | 2025-10-28 04:44:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a60337fb-d695-356d-b503-e27f0cf3cfee | -15.15652 | -46.58369 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71a8e080-d4b6-38d1-8887-8149ab518265 | -11.74844 | -50.21952 | 2025-10-28 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 094c2aa6-28d8-38dd-a869-8edce990d052 | -13.90293 | -48.49797 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a9f741d-9fc4-3869-a5b4-911d02bc50e6 | -9.53546 | -46.97153 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70da9d36-8967-3afd-abdd-18cbd6398f83 | -9.46496 | -46.87149 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e5e79ac-e255-3ff8-91e0-0d5530b0c10e | -9.47607 | -47.78091 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 992f0a60-8cf8-3c32-87f8-0ff5429b729c | -11.73496 | -49.33196 | 2025-10-28 04:44:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a3c898e-1d12-3423-9cc2-a051c597f470 | -8.57482 | -47.02732 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ac273e72-bbb0-3ff9-b7d4-fa2c214e367f | -15.21297 | -47.94726 | 2025-10-28 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30d37871-c1f8-3b89-b814-f41ff69b1ed5 | -11.18683 | -49.78879 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e3b6164-a521-37be-85a8-fc1615daf18e | -13.38968 | -47.35313 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89ad2766-2dc0-308f-ad03-e7d5986285d4 | -13.87381 | -48.49882 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91c3c30d-777e-3099-97d9-1b3ee102ea23 | -13.67129 | -46.52057 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README69.md)
