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
| 10b5b031-2a8b-357e-ba99-092e91c729a6 | -14.39095 | -52.95776 | 2026-08-24 00:07:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d630be17-6f59-337f-a721-b33f67b3d017 | -15.5851 | -56.00637 | 2026-08-24 00:07:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 5d7f65df-1ee4-324b-a57f-458407e583a5 | -14.44152 | -51.80196 | 2026-08-24 00:07:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d8b2d83e-ff90-34f7-aec6-8277baafd9e5 | -17.67865 | -46.38858 | 2026-08-24 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e075e7f2-8f50-37f3-8446-b4fe7ddf80c0 | -16.41453 | -51.84489 | 2026-08-24 00:07:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| bccd8add-6e57-3abe-b456-069407c36478 | -15.33247 | -53.76081 | 2026-08-24 00:07:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 50d7ad55-2943-3322-b167-3f698116a3d1 | -14.57337 | -53.0373 | 2026-08-24 00:07:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1c6e93a2-014c-3c26-a592-9df5185d491a | -17.67091 | -46.40039 | 2026-08-24 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 279.6 |
| 99ebdb2a-01e1-32bf-9028-6ddf969706a4 | -11.91563 | -55.91158 | 2026-08-24 00:07:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| dee1bc19-35b9-3508-93a6-439db686fb70 | -15.34763 | -52.7708 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6659027e-3844-3fa7-b8e6-d63f77a1cbe5 | -14.80262 | -48.77458 | 2026-08-24 00:07:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 61bbf585-f9f9-31e0-b409-db66d4cfb552 | -15.50758 | -53.98693 | 2026-08-24 00:07:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d419906b-ca74-37e2-9032-1a8f9947b358 | -15.76908 | -50.05231 | 2026-08-24 00:07:00 | TERRA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a0437091-a8a7-3a8d-9042-f57caa43b1c2 | -14.93602 | -52.66144 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 15abc8a2-af11-333d-b070-14dae9c05f66 | -14.9345 | -52.64915 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 561387b7-b7fd-3616-a646-4ffbb6786717 | -17.67244 | -46.41064 | 2026-08-24 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 306.9 |
| 869eafdd-91bd-362c-8c7f-99ebc0a53f07 | -14.58374 | -53.03599 | 2026-08-24 00:07:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2eb9ea71-849f-37c8-af9e-ec6ff5662b4a | -16.67659 | -50.16729 | 2026-08-24 00:07:00 | TERRA_M-M | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7e57d53e-5bcc-3bc4-a21e-533761cd65ba | -14.79381 | -48.77594 | 2026-08-24 00:07:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b0170263-e39d-34cf-b5d2-deef5c3e7dd1 | -14.95782 | -52.67083 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 93e45d7e-29bc-3c3b-9485-8913d04f619c | -12.06397 | -50.56959 | 2026-08-24 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3027aaf3-cf87-3b15-8d7b-e2e48c7f90c9 | -17.83503 | -44.472 | 2026-08-24 00:07:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 20704a33-9128-331c-bf3e-c8e4eca21f0a | -17.66164 | -46.40193 | 2026-08-24 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 8714aaf1-f0ea-3c38-bc1c-89d59a8bf010 | -12.58263 | -47.94227 | 2026-08-24 00:07:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e4ea3206-af0b-355e-a3a8-87ec694638cb | -14.27602 | -51.79315 | 2026-08-24 00:07:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ca78fe41-111c-373d-8efe-f8c580693bf1 | -13.09042 | -43.34571 | 2026-08-24 00:07:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8b8e1a52-0427-3d1f-ba52-cbcd0fdc18ce | -12.10759 | -44.9595 | 2026-08-24 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5389acdf-e36f-32a8-b5e9-9677037a266b | -17.66318 | -46.41218 | 2026-08-24 00:07:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 36.5 |
| d7dfce08-4f20-39d3-ae0d-d4bf92b6a0ff | -12.08419 | -50.58531 | 2026-08-24 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 555429bd-67fc-3d5d-866a-9a60e850d410 | -16.40335 | -51.83518 | 2026-08-24 00:07:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6b99eae7-c18c-365c-abc8-796cfa6a81a1 | -15.33588 | -52.76022 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5e98d237-cf32-3419-af5f-acbcf68eaf60 | -15.49629 | -53.9884 | 2026-08-24 00:07:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 17f06e17-61d0-30a9-9918-3ec5fa0040dd | -11.80851 | -47.25082 | 2026-08-24 00:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8a63b39d-0f5a-35d9-aaa8-1162c82b3de2 | -14.98129 | -52.69311 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 80ac97ea-4c97-34a5-9028-63688bd7daeb | -14.77744 | -48.78765 | 2026-08-24 00:07:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a64703a8-136e-37ee-a3d0-936fb3f72e06 | -12.58401 | -47.95193 | 2026-08-24 00:07:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 41134ef3-fe04-38dd-ab6b-6586faca8fde | -16.42366 | -49.92411 | 2026-08-24 00:07:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| af76d9dd-07cd-3e65-b23e-c26ad4013c5e | -12.14933 | -43.40061 | 2026-08-24 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 8259826d-ce65-398e-96c1-7e193fca6714 | -16.85652 | -49.44856 | 2026-08-24 00:07:00 | TERRA_M-M | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 6a62588a-e236-3e67-946f-ab81e332b999 | -12.72289 | -48.40895 | 2026-08-24 00:07:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| efa0a84b-906c-3881-b7f8-6aab328e77c6 | -16.14401 | -50.24517 | 2026-08-24 00:07:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 91482c95-6ee5-3a34-9d1a-475057da0da0 | -17.54081 | -42.54019 | 2026-08-24 00:07:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 694a3bd8-15ad-3cc1-ab1a-be189c260ba8 | -12.85357 | -48.48763 | 2026-08-24 00:07:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a7ddd49-e773-324f-aadb-8de90283c944 | -14.3547 | -51.76594 | 2026-08-24 00:07:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 334e797a-afa5-34de-8a45-5397b1ac82d7 | -12.61601 | -52.46333 | 2026-08-24 00:07:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 83780348-6267-3b75-a640-a9b79bd22661 | -14.94461 | -52.64758 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| eeafc866-00ff-3884-a3d2-363a096f86bb | -13.0882 | -43.35164 | 2026-08-24 00:07:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1d445c01-fa8e-3499-a659-a3d6dca4ad50 | -12.75589 | -48.37876 | 2026-08-24 00:07:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 56a39adf-2e42-31f8-b903-47b6451f60ee | -15.26447 | -52.84052 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 21e4bfe0-50bd-38b4-9e0a-05d2b98efa4f | -16.41345 | -49.91591 | 2026-08-24 00:07:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 483e3a46-3ff1-342f-9592-a4ed91bfff2d | -14.80388 | -48.78372 | 2026-08-24 00:07:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dc3a3780-78c3-355b-95fe-66683a444657 | -13.14952 | -51.39584 | 2026-08-24 00:07:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ce4f45d4-5e02-36a4-b27d-32d5b9d3dffb | -13.90118 | -54.03817 | 2026-08-24 00:07:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| c98de9c6-c123-37f6-976f-998afbaba4ae | -15.273 | -52.84588 | 2026-08-24 00:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d222566b-9b7f-3979-974e-4645e9baf6d6 | -15.43219 | -56.14871 | 2026-08-24 00:07:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 448b3a17-2eba-334f-a9be-81d49ec6944b | -16.4147 | -49.92535 | 2026-08-24 00:07:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 40afd5cc-8abd-3baa-bdc3-73b9dac3b57b | -6.37621 | -54.98284 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d036d137-ae40-3472-bd08-0f4f33ea2c5b | -6.43632 | -52.75593 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 40b0a87a-72d7-3f88-b3a9-060744b87e67 | -7.28803 | -45.3754 | 2026-08-24 00:09:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| ce8d519d-410c-30ba-a2c4-20eece70f47d | -7.35178 | -45.80011 | 2026-08-24 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 1f0055a8-65f3-3870-8fad-c71cba820d30 | -6.8336 | -52.49514 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9d0914db-5410-34fe-8f2d-9797e3bddcfd | -7.24862 | -49.86785 | 2026-08-24 00:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| a5439214-8864-3dfe-86f9-62524ef3ef91 | -5.77226 | -57.55851 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| ad15f7f4-3a78-352f-8cd4-1c971f196b96 | -5.07583 | -49.37457 | 2026-08-24 00:09:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0eb5e671-07a9-3678-8a77-fd6c2a6bbecb | -5.78785 | -57.57713 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 4f75e5ed-ce15-35ce-98f7-c757a1c823fa | -9.20147 | -59.59102 | 2026-08-24 00:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 1a544638-2eec-324e-97ea-7cb1f502de1f | -10.82471 | -50.94197 | 2026-08-24 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| d8000cbc-917b-35d4-ae6d-d0b95feeca8c | -6.55278 | -58.53093 | 2026-08-24 00:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| db4759ba-9e56-3a88-b8e5-436b35ab01f6 | -8.59072 | -54.735 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 19b5d2ff-aee2-3f8f-abe9-c404fe0a1fba | -7.36533 | -45.8135 | 2026-08-24 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 253.5 |
| 061ef528-580d-3c59-8157-e9ff49c734df | -6.84401 | -52.50346 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b416e185-85cc-3be8-853b-fa20d73691fa | -5.92066 | -52.14673 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 36da8a90-19bc-321f-ae41-19e22c8ebc4b | -6.81698 | -58.65383 | 2026-08-24 00:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 22a038e7-2caa-3a1c-8b75-8c693484a6f7 | -10.39991 | -50.39336 | 2026-08-24 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ff11b2e-f106-31f2-b9eb-f3c2ab851215 | -6.43255 | -55.00188 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| ee1491f7-fd29-36a6-8129-aa0e594ec47f | -8.11141 | -51.65938 | 2026-08-24 00:09:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab4c6f97-7503-378d-96fc-13914a4127d8 | -6.6237 | -53.34767 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 13ccabab-4338-324e-8a84-5553a3a23be2 | -10.8069 | -50.94448 | 2026-08-24 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0c5a16d9-c313-35a0-b770-41c59ab118b1 | -9.04037 | -50.82341 | 2026-08-24 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f5d23744-26a4-3144-bbc9-bd056e8f19bd | -8.58525 | -50.00025 | 2026-08-24 00:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e9410634-e0cc-3205-8789-3a5dbf473650 | -6.84271 | -52.49387 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 39c437d8-9e91-364b-b993-05005855e053 | -6.705 | -52.09151 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2180e7d0-2f28-31e2-a1de-6447597c8dc4 | -6.59746 | -52.45311 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e61e0b90-76a4-3de6-a1a5-e4cfe9a7efde | -6.18114 | -55.4384 | 2026-08-24 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c489f1b0-e61a-3b5c-9544-df68e67f1133 | -6.14917 | -57.95687 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 4b6c7f3a-86c9-359c-bf08-e11126f52b4d | -10.73246 | -47.96754 | 2026-08-24 00:09:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e3608bd-6f97-3079-990f-ccebca48feb0 | -6.84529 | -52.51291 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c29d7b94-8d64-3f14-a7ca-ab8b5ea95a88 | -3.25957 | -50.82711 | 2026-08-24 00:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0d49eac-5d52-3b50-8e39-5211c99a4deb | -10.43366 | -50.4431 | 2026-08-24 00:09:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 14a73f2d-c003-3419-93b0-66d0e76291f7 | -4.61275 | -55.74291 | 2026-08-24 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ffaf04b4-2aca-30af-9dcf-0ec3da051c1b | -3.53369 | -48.19139 | 2026-08-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ad10136f-433e-3b59-8696-e753a994c3e2 | -10.0451 | -46.41353 | 2026-08-24 00:09:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a25359a8-7442-3074-ac9f-243bf75fa53c | -7.35405 | -45.81526 | 2026-08-24 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 886a0b16-65b8-311d-956a-44316975cb13 | -5.77356 | -57.57237 | 2026-08-24 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 42198e00-0069-39b7-b7a6-f2b7681b75b8 | -9.23941 | -60.39658 | 2026-08-24 00:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 90e338b1-0616-3097-8139-0c73612e50d9 | -6.34031 | -55.87079 | 2026-08-24 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 770a5a65-1f57-3b2f-badf-701298c0a183 | -7.36756 | -45.82847 | 2026-08-24 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 737a9c6f-87c8-39a4-a113-203b39151076 | -7.37883 | -45.82674 | 2026-08-24 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 7640ab57-a387-39c1-9b88-deee604bb7e8 | -3.53204 | -48.17986 | 2026-08-24 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| bd1bb36c-4fa2-3438-b17a-f9d55467fba9 | -9.46724 | -56.92729 | 2026-08-24 00:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |


[Clique aqui para ver as próximas entradas](README3.md)
