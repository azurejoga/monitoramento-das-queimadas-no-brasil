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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9944300-b823-3303-9ec3-ee4019822b81 | -11.9211 | -47.115 | 2025-08-26 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 174ce195-54c9-3fbd-90ca-1efb307274e5 | -12.6741 | -47.8589 | 2025-08-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 28ea1bd0-c984-3a8c-9118-36f244ed1cf2 | -6.246 | -59.9982 | 2025-08-26 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 18027baa-2c83-3c18-ae43-4a79c2e02e40 | -8.3521 | -62.9247 | 2025-08-26 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 1d7fa73d-44e6-349a-9ed3-67a5cf75218f | -11.6273 | -46.4126 | 2025-08-26 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 9f959d34-45ef-3034-bedc-cf826e7c6910 | -7.5673 | -47.4851 | 2025-08-26 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 546c3b41-1e7e-3392-822d-31c503705540 | -6.7635 | -59.6718 | 2025-08-26 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 5575fa6a-299c-39a7-a426-42be5740b1c5 | -7.586 | -47.4835 | 2025-08-26 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5a93681a-ffb3-3c14-90b5-5fc2cb7b3fac | -9.7915 | -64.265 | 2025-08-26 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 46118869-b543-3bbd-b769-28d12467e574 | -6.2553 | -43.8314 | 2025-08-26 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 29e6af03-76dc-33e2-8f24-bb072816e6ae | -10.6818 | -47.1858 | 2025-08-26 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 5e68798b-39e9-3977-854a-f2f9b21d491b | -6.8062 | -45.0019 | 2025-08-26 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b8a9aebe-62bc-38ca-9aaa-ea4c4dabda13 | -6.2459 | -60.0174 | 2025-08-26 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 428.9 |
| 5405e596-77b0-3995-81fb-fdc90a76e314 | -12.6548 | -47.8616 | 2025-08-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 19df2d6c-e3d5-375b-85e6-4e79b20e2753 | -12.7647 | -48.157 | 2025-08-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| b6286c16-1126-3a91-9f02-3361664878b3 | -11.6112 | -46.2337 | 2025-08-26 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 39fe423e-a2ef-3916-9fde-8990eac1b255 | -14.3912 | -51.9508 | 2025-08-26 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 7aee1ca3-4e3f-3cfa-a22f-e573b6d2108a | -12.7843 | -48.1321 | 2025-08-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 269.8 |
| 547de085-49f6-3917-bb1a-aba8642fcd78 | -15.1101 | -48.7352 | 2025-08-26 14:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4ac8b832-34ba-32ce-8ea9-4d14061c14e8 | -7.8854 | -45.8779 | 2025-08-26 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b79ea112-fa5f-36e4-ad5a-e70284fc08c2 | -10.6822 | -47.1635 | 2025-08-26 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 688d3c21-d851-3ad8-a591-069fda519590 | -6.8412 | -58.9746 | 2025-08-26 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 5bf32f90-6993-34f0-aa70-4c7c69f334b7 | -6.6961 | -58.5546 | 2025-08-26 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 639debe1-126b-3627-a3b2-3da52102ba90 | -6.9128 | -59.3578 | 2025-08-26 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5fb11076-6606-3802-9de1-2788aa8381f7 | -11.2014 | -50.5685 | 2025-08-26 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| b7abe59a-3d4a-3be7-927b-35d9d9d3c441 | -6.7819 | -59.6711 | 2025-08-26 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 59454294-3324-3dc5-954d-9dc60908e13e | -10.6825 | -47.1412 | 2025-08-26 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 799585b2-6005-320e-90eb-235664732b14 | -8.9874 | -65.4192 | 2025-08-26 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 349a8e90-28ea-3782-abf9-71410c1600b2 | -7.5858 | -47.5055 | 2025-08-26 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7bd71168-865b-3b3f-8530-bd71848c3ece | -16.8615 | -49.2398 | 2025-08-26 14:10:00 | GOES-19 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 08612f97-7d39-35e3-ab3f-6cd93fd57aa4 | -9.1812 | -60.7939 | 2025-08-26 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 556d9c7e-b05b-30b9-aca5-b814ace47bb1 | -12.6737 | -47.8812 | 2025-08-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 3901f441-31e0-3f63-a74e-004b8880d669 | -9.1722 | -59.4629 | 2025-08-26 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9c670dbc-08af-368b-b3f1-771769ccbc14 | -13.4397 | -47.006 | 2025-08-26 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d6054a38-97d6-39d4-b5be-891b66ddbc21 | -9.0059 | -65.4186 | 2025-08-26 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| fa36e72e-5676-3ff9-b7a6-aae815c41838 | -12.6741 | -47.8589 | 2025-08-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 4724149c-f121-3212-bb24-0a43a5e42897 | -9.7916 | -64.2461 | 2025-08-26 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.8 |
| af5ceaf4-03d5-3dd8-98b8-77a2eea0afa8 | -6.6201 | -44.8581 | 2025-08-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 89411a2f-94e7-328c-8a44-5fdf9460640d | -16.8615 | -49.2398 | 2025-08-26 14:20:00 | GOES-19 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 1d546a29-7cbb-368a-8d6e-068189efcd60 | -8.0838 | -45.0199 | 2025-08-26 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| eed30c4f-b258-3142-8843-bb7d28f7b66a | -12.7932 | -49.8624 | 2025-08-26 14:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 211.3 |
| cecf94a9-b0f4-3c20-80a5-5f7a46e491da | -6.6961 | -58.5546 | 2025-08-26 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c6d1f64d-996a-3c71-ab37-c03b7b16ba52 | -10.6822 | -47.1635 | 2025-08-26 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 43c7f33d-f2e0-311b-9423-f162477aa577 | -6.9128 | -59.3578 | 2025-08-26 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| bfbe277f-48af-3c09-88a8-61d154fbe1bd | -14.3912 | -51.9508 | 2025-08-26 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 4dd4ae9e-2684-3a38-8626-4321ff468b4b | -6.5293 | -44.5687 | 2025-08-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 9a97e3d4-331b-31b3-8a85-4e687ea41b4d | -12.6548 | -47.8616 | 2025-08-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| f6186872-d9d2-3fec-989c-983baf12067a | -6.8064 | -44.9791 | 2025-08-26 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4d67b9b0-a9de-3f5a-abd6-2370328a0ea0 | -11.6978 | -51.6814 | 2025-08-26 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 5a7539eb-9ab2-324b-be57-39e6e2eadcb2 | -11.2423 | -45.4646 | 2025-08-26 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 270a6bf1-5968-3be3-8a2e-1e8f8768b283 | -9.1909 | -59.4619 | 2025-08-26 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 2cb2ffd5-302f-33ce-b912-7c0d50585f00 | -11.54 | -52.119 | 2025-08-26 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| a484deef-a84f-382c-9079-59fa2a6137ce | -6.7635 | -59.6718 | 2025-08-26 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 6ac3fe82-2b66-39a4-a554-15789f55ca1a | -9.7915 | -64.265 | 2025-08-26 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 68a5b4d1-11a7-353b-b6be-45d273ec24a0 | -13.0674 | -46.3153 | 2025-08-26 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| da9ea97d-9aba-3f9e-a734-0143f057a2fa | -13.4423 | -46.87 | 2025-08-26 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 4411b52f-3d7f-3d60-9910-6acc2bcc890e | -15.6557 | -52.7366 | 2025-08-26 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b9d94f17-8d30-3b6c-b4e1-142d6a084ea7 | -11.7165 | -51.7005 | 2025-08-26 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 309.9 |
| ee11e35e-a495-3ce7-8875-8cf4c2e9aa4a | -6.8873 | -44.4234 | 2025-08-26 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c01f27a3-2af9-3335-80b5-c4c0f42b1b9a | -6.2458 | -60.0365 | 2025-08-26 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 2645afff-b318-3d19-ac7e-9769286a19eb | -12.7651 | -48.1348 | 2025-08-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 6892a34c-9d38-3199-a7f1-b8841469ba7a | -6.2276 | -59.9989 | 2025-08-26 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3ccb9cfc-37d1-34bd-8984-4cba987486d8 | -14.2876 | -49.1291 | 2025-08-26 14:20:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 671cd478-4c8d-3dc1-8a1f-0a013182ebc2 | -9.8101 | -64.2642 | 2025-08-26 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 2cbb700c-9bed-395f-9a1a-2a66a4bf7bbc | -11.559 | -52.117 | 2025-08-26 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| f795a50e-6e8b-3545-9d53-5ce12582efb3 | -9.8102 | -64.2454 | 2025-08-26 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 09f3ce8f-8f55-30e1-8d54-ae2f83761bf7 | -12.338 | -64.2272 | 2025-08-26 14:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 871a4fec-4819-3207-bbf5-8ba9c7c4c274 | -11.2232 | -45.4672 | 2025-08-26 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 125df498-8dd9-34c2-b48e-636dbb0f93fd | -9.191 | -59.4425 | 2025-08-26 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 1a069cac-5459-32f4-919d-fc2807abb53b | -7.5391 | -44.9362 | 2025-08-26 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 17364e9c-c576-3cba-b6a8-8af4805b9e27 | -6.2275 | -60.018 | 2025-08-26 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 6383b77b-5c84-3245-982e-51eaeaa71e73 | -11.9277 | -46.7322 | 2025-08-26 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 34bdc5fc-2af6-3c0b-a823-99fd096c319b | -6.2459 | -60.0174 | 2025-08-26 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 329.2 |
| 294c0e75-09ba-3b31-828e-f43fd9fd7437 | -10.7597 | -47.0648 | 2025-08-26 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 62c2dcc6-289d-3ef7-94e8-18cf869f2965 | -8.5573 | -62.633 | 2025-08-26 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f42e888c-8f80-3baf-b043-8cf775319130 | -9.006 | -65.4 | 2025-08-26 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b10f86fa-08f8-30a1-891d-064214f1d9f2 | -9.0415 | -65.7349 | 2025-08-26 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 1d27aeaf-a22f-3513-98c6-55864eee778e | -7.8851 | -45.9004 | 2025-08-26 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 04d1574c-ad01-31bd-9839-8b793e26883b | -8.5387 | -62.6527 | 2025-08-26 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 06741e64-db60-3e84-b508-e3c94432d360 | -7.8854 | -45.8779 | 2025-08-26 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| f445ca88-be04-3cbd-b518-25b9355dcb42 | -6.7819 | -59.6711 | 2025-08-26 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| ec2af28e-afac-3cde-96fd-5ec65e29b913 | -11.6308 | -46.2083 | 2025-08-26 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d7fe9985-9ef6-30ca-8888-8d51adeddc4d | -8.2333 | -45.1187 | 2025-08-26 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 158.5 |
| f020e934-93ae-33ad-a7a3-1760d276cd09 | -8.2522 | -45.1168 | 2025-08-26 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| d66d4249-2cbc-3fe0-aa8e-d0708c98de15 | -7.4224 | -60.6236 | 2025-08-26 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2d8ac2eb-734a-3b48-822f-b16095547536 | -11.2014 | -50.5685 | 2025-08-26 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| f726ddc7-88c7-3835-ae1e-64b18aaa3b64 | -8.0841 | -44.997 | 2025-08-26 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 34e8c9ec-e275-34c5-ab51-f68b7967ad21 | -7.5394 | -44.9133 | 2025-08-26 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a573a1bd-b7ee-30e2-8ec4-f785fe7195e1 | -14.7135 | -45.3929 | 2025-08-26 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| fbef44d4-c5a2-38d2-a4b8-78af561ffcf6 | -6.8062 | -45.0019 | 2025-08-26 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| b39524ed-26ac-3730-9aa1-5d65b5ff4d6d | -9.4064 | -60.5133 | 2025-08-26 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 90e702d9-7e65-32cf-b6b1-9312ebe9040b | -6.246 | -59.9982 | 2025-08-26 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 32d8fe48-cd09-31e8-8497-b3a7c2b649bb | -12.8123 | -49.8599 | 2025-08-26 14:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 19e0049d-81f1-39f7-9ecf-6d99c5513cd7 | -12.7843 | -48.1321 | 2025-08-26 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| df833cf9-a503-33cc-82db-7c337ccc6144 | -9.5811 | -55.3713 | 2025-08-26 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 0dec948a-75cf-32a8-aec1-bfe8f60471d6 | -9.8102 | -64.2454 | 2025-08-26 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 688a7c88-d775-3ba6-a480-58591c658c7f | -6.7144 | -58.5732 | 2025-08-26 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| de40dfd3-cd65-33c8-8818-eafe4f41fb9c | -15.6175 | -52.6994 | 2025-08-26 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 18c114b7-040f-33c8-abc8-5719bc0591b2 | -16.8615 | -49.2398 | 2025-08-26 14:30:00 | GOES-19 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 2bcb5480-de06-3fb5-8d97-f63a3970b62f | -6.2643 | -60.0167 | 2025-08-26 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |


[Clique aqui para ver as próximas entradas](README108.md)
