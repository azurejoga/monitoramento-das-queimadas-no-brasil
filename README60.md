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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b0af5da-86ae-36b0-94f0-5114a64e5530 | -4.87089 | -56.00154 | 2026-09-13 12:27:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1b548be6-b31d-39b8-9b7d-cd8cbcdde999 | -3.45094 | -59.518 | 2026-09-13 12:27:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| c4774734-b749-33d0-9080-e706712b691d | -8.28562 | -51.2145 | 2026-09-13 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d4b45f1a-4bd5-3802-8f5e-31c1b444c72b | -8.76443 | -61.40305 | 2026-09-13 12:27:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| e0597514-acb6-3ded-be0f-7ac522c9cf1b | -10.68449 | -54.15772 | 2026-09-13 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 514.2 |
| 14f6ab9c-533c-38e7-bfb0-c7e9b54de333 | -9.3899 | -57.29393 | 2026-09-13 12:27:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d5d7391c-9e05-3868-9a66-40bcfdd4a949 | -3.87377 | -51.18113 | 2026-09-13 12:27:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 14160d4c-8492-38f0-a8a2-73b5381edf9b | -3.91325 | -55.73325 | 2026-09-13 12:27:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f60c1bee-d2f6-341c-81a7-ddb638571c25 | -3.89261 | -55.81501 | 2026-09-13 12:27:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 50e14590-9c2c-35bf-9592-f090c3db96c1 | -6.03136 | -52.73563 | 2026-09-13 12:27:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 88390e94-646f-3144-94a2-e5c8354ae6a6 | -10.68627 | -54.14376 | 2026-09-13 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6bf173c1-7141-3100-a091-ae3938b99a08 | -6.23837 | -51.68583 | 2026-09-13 12:27:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c78efc70-b9ff-35df-abb8-9a11ebe8519b | -9.70156 | -58.15583 | 2026-09-13 12:27:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1be65ba8-2a79-38ee-a098-b8523c3cd707 | -9.75646 | -60.44751 | 2026-09-13 12:27:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 656fddee-1de2-3ae1-849e-81e7f2b2fe7e | -10.69533 | -54.15912 | 2026-09-13 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 164d072a-da36-31ee-b768-10ced8fc3d88 | -10.68272 | -54.17155 | 2026-09-13 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 1449a17e-41e9-3520-94bf-49047ea03b20 | -9.38861 | -57.30302 | 2026-09-13 12:27:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 37d2b448-14de-336d-8cde-06da0e2a4c43 | -4.36139 | -54.77402 | 2026-09-13 12:27:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ead2c7c6-b792-3c4e-96c3-dfe58b535376 | -8.54215 | -54.70742 | 2026-09-13 12:27:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 3e9721a4-de5b-3a0e-bbb0-9451a4706d5a | -3.60294 | -59.06673 | 2026-09-13 12:27:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 12722c4d-f920-3118-8df9-829a6720fa78 | -4.41247 | -54.86059 | 2026-09-13 12:27:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cf6c6ea0-1749-3c3d-acee-20d76a639890 | -13.31744 | -51.72319 | 2026-09-13 12:29:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8b871a03-bbdb-36db-9123-df300f416f6f | -13.34649 | -51.77983 | 2026-09-13 12:29:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| db7cc3ea-4421-3e8c-9f10-c1f37cfa7047 | -13.98012 | -54.07217 | 2026-09-13 12:29:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 90c5cd8d-b483-30a9-ba16-5d8dfdf5fea1 | -13.30639 | -51.32376 | 2026-09-13 12:29:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| fc3e04e6-2493-337c-833e-a574bda212a8 | -13.98202 | -54.05627 | 2026-09-13 12:29:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 2140c74d-3f13-326f-89fa-88f21231ff70 | -6.8567 | -47.4328 | 2026-09-13 12:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| ea1fd05d-d53d-30f8-b2b3-0d8de3ddd3fd | -6.8755 | -47.4313 | 2026-09-13 12:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1625ffb4-d7ac-3020-80b5-a35775a62fb0 | -10.6829 | -54.1475 | 2026-09-13 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 261.8 |
| a18f67d4-61b2-3158-ba86-b113d6c74bb0 | -11.8189 | -46.386 | 2026-09-13 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| af536e69-1000-355d-970d-a3b0fb70541e | -10.7015 | -54.1663 | 2026-09-13 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 507aae26-5d09-3ab4-bee8-642376188f74 | -10.6827 | -54.1679 | 2026-09-13 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 241.5 |
| d8927ac5-e7e9-3ae8-bab3-4e91371b722a | -7.0166 | -44.6184 | 2026-09-13 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| d153037d-efa7-36a5-8d66-9afc011ce0a9 | -10.7535 | -46.2347 | 2026-09-13 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| c6a91c4d-b8e9-30d1-abd4-a16a4f181284 | -13.3055 | -51.3235 | 2026-09-13 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1b27f3e3-d625-3a8e-adc6-3aecb47fc23c | -9.5129 | -45.4568 | 2026-09-13 12:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 74684429-c3f8-3681-a1f3-b9e1feee9807 | -11.0623 | -47.1609 | 2026-09-13 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a8e882c2-8686-3af5-984f-db43c6b430f2 | -13.4507 | -48.48 | 2026-09-13 12:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c75ac209-754d-3961-a10b-d5df9e8b0617 | -11.3532 | -46.8324 | 2026-09-13 12:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 1e5f2742-256d-3b46-bd8d-18729925cdf4 | -10.7018 | -54.1458 | 2026-09-13 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.1 |
| c08f794f-e57b-37e7-a6de-ebe30d4c895a | -7.0352 | -44.6396 | 2026-09-13 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 09ba8c7e-adf4-318f-9109-2c673fd1b27b | -10.7532 | -46.2573 | 2026-09-13 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 453.4 |
| 02bf79e8-ef08-3fde-a49f-7017878f386a | -7.0164 | -44.6413 | 2026-09-13 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 273.2 |
| 799c4794-116b-3414-81a4-24f8c1902d77 | -9.5129 | -45.4568 | 2026-09-13 12:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 14e8f4ca-ca3f-3d77-8d2a-f38c26baadf9 | -7.0164 | -44.6413 | 2026-09-13 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 8aed64a2-2482-33a6-9a02-97fb6c3ed23b | -11.8189 | -46.386 | 2026-09-13 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 13d98c99-d1a9-3db6-98c8-04f3d3a9a94f | -10.7018 | -54.1458 | 2026-09-13 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 12ac5973-4a0d-3516-bbd7-b74994ed60db | -2.9579 | -50.3988 | 2026-09-13 12:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 488d4008-946a-331b-aafe-feec98d4fb44 | -10.6829 | -54.1475 | 2026-09-13 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 341.0 |
| 85472d84-9721-3849-bd0d-848c6c26a4fb | -13.2993 | -51.7075 | 2026-09-13 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a4820a47-2899-3b0c-8f0c-5fc21bfd42a5 | -13.4507 | -48.48 | 2026-09-13 12:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2e3cad8a-ce74-3944-9173-be52c568c718 | -7.0166 | -44.6184 | 2026-09-13 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| e0530c12-f3da-36ee-9161-0ae995535e3b | -10.7015 | -54.1663 | 2026-09-13 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 209cb453-f6c4-34b6-b705-0292c6da6455 | -6.8567 | -47.4328 | 2026-09-13 12:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| b462a7b5-1c2e-37fb-98d8-5feb728c2af4 | -10.6827 | -54.1679 | 2026-09-13 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 336.9 |
| b56436d1-0167-3a57-beb2-a50cbcf41375 | -11.838 | -46.3834 | 2026-09-13 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5202eaec-12ee-30df-87ad-5734cc6a83d0 | -6.8755 | -47.4313 | 2026-09-13 12:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 68f5c866-41ac-30ce-bfce-4cab4e858aa6 | -13.299 | -51.7288 | 2026-09-13 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 07c9a19a-b277-3847-ba72-382f105cebf4 | -7.0352 | -44.6396 | 2026-09-13 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 662bb5d7-9615-3526-b1d1-8354632f4f14 | -7.0352 | -44.6396 | 2026-09-13 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 7d40e2cb-901b-3bf0-8fb8-817c93daae6d | -10.6829 | -54.1475 | 2026-09-13 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 372.5 |
| 36d2d439-a0f9-39a3-8988-1c681787fc13 | -8.6005 | -44.4378 | 2026-09-13 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0eaf26d5-3f67-3439-be64-e3683df045a0 | -8.9272 | -45.4321 | 2026-09-13 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| af2e2d96-e42c-3d4b-bfc6-4b40da2e144c | -10.7532 | -46.2573 | 2026-09-13 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 215.4 |
| d950ed31-f172-3501-8722-33564c5d1a5a | -8.8132 | -46.9495 | 2026-09-13 12:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0cc726fb-aab6-3305-aa40-f48913419e77 | -6.8567 | -47.4328 | 2026-09-13 12:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 92ae3bdd-1001-3ced-a794-5b6691032d0a | -6.7269 | -45.4168 | 2026-09-13 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| abcd9f76-059d-34e6-b1e9-728d4d1a16fe | -13.299 | -51.7288 | 2026-09-13 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e75e59a5-4cc9-3fd5-bf59-d0673a37381d | -10.7015 | -54.1663 | 2026-09-13 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 38101dfc-7a2e-3374-a101-da481d52d93a | -11.5793 | -47.0043 | 2026-09-13 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5590a87d-7347-3eb7-84ab-38e47597b1c2 | -2.6785 | -57.531 | 2026-09-13 12:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| a1d484e5-0485-330c-a867-5663e6028662 | -10.7535 | -46.2347 | 2026-09-13 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 62b79f94-3023-3c7b-8b54-1c9d71245018 | -11.8189 | -46.386 | 2026-09-13 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| a72087b2-91d5-3b2d-913d-f421a76c827b | -7.0164 | -44.6413 | 2026-09-13 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| e34459de-4c03-3270-99fe-a1702709cf21 | -6.8755 | -47.4313 | 2026-09-13 12:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| def83ce9-0731-368d-bd27-59b4d4a2c149 | -2.9579 | -50.3988 | 2026-09-13 12:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| fb2a6145-0e5e-39b5-9462-c5f87fa6ef34 | -16.9909 | -45.4594 | 2026-09-13 12:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f9859031-6d26-39bb-b45d-5c552f82b8ed | -10.7018 | -54.1458 | 2026-09-13 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 24dca57f-cef0-383e-af08-0bbfaebf4bc8 | -10.6827 | -54.1679 | 2026-09-13 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 430.0 |
| e6019259-a310-379d-9616-bec7941c84d2 | -7.0166 | -44.6184 | 2026-09-13 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6c502a79-0a02-303b-8ce8-a6da2d9ed5ae | -2.6784 | -57.5504 | 2026-09-13 12:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 1b685976-6fdc-3a03-8cd9-dc68692c0b5d | -6.8755 | -47.4313 | 2026-09-13 13:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 210de126-f199-30d9-b198-6a383b1c48ca | -13.4507 | -48.48 | 2026-09-13 13:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 238d92b5-35ac-3cfd-b660-ce186fc3f99e | -11.8189 | -46.386 | 2026-09-13 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 36bf80c5-5e2d-394e-bae6-3c3729a9a023 | -2.6785 | -57.531 | 2026-09-13 13:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 2415f842-0e63-32d7-ba20-47159861e420 | -11.838 | -46.3834 | 2026-09-13 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ecac90ad-4a83-3759-8cc3-5385e8a03f39 | -8.6005 | -44.4378 | 2026-09-13 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 4df6ebc4-0a9a-3356-a8bb-b24509c1aa63 | -6.8567 | -47.4328 | 2026-09-13 13:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2cf164b9-5581-3592-bfbd-7c84cdeb2747 | -9.5129 | -45.4568 | 2026-09-13 13:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 636ee1ad-db47-3a9e-88b8-49e0b8fcc831 | -13.3055 | -51.3235 | 2026-09-13 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d7294a28-b708-3d48-94f2-20acddc01651 | -8.4292 | -46.0271 | 2026-09-13 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 28f1be25-d897-32a2-bc75-e9c01414a236 | -5.1255 | -55.955 | 2026-09-13 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d7a87e75-aecd-3a5e-9590-d99774ee35d8 | -10.6829 | -54.1475 | 2026-09-13 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 337.1 |
| b14b92a1-b662-3765-af26-295d4c3642f1 | -14.0818 | -41.4383 | 2026-09-13 13:00:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 138.1 |
| 18fb68ac-71b7-3324-8295-be55a9c1e1a5 | -7.0164 | -44.6413 | 2026-09-13 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 183.3 |
| fb70aae0-70f1-3d4d-8ba6-9f8fd8f992c4 | -10.7018 | -54.1458 | 2026-09-13 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| fc6b4039-f7f6-3994-8962-a808398f277a | -10.7532 | -46.2573 | 2026-09-13 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 59ff9252-f523-37e4-9bbe-8823af35c1bf | -8.6008 | -44.4147 | 2026-09-13 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| cea11514-a7aa-3980-b5e0-00b49dd9a204 | -10.6827 | -54.1679 | 2026-09-13 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 464.4 |
| 0fb91af8-0c71-3f7a-be87-41300825d6bb | -10.7015 | -54.1663 | 2026-09-13 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |


[Clique aqui para ver as próximas entradas](README61.md)
