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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87146833-21b7-383a-b651-f1ac95f85f35 | -5.87213 | -42.96109 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9028a628-3b49-3e3a-84e4-0057ac76ce28 | -2.31002 | -46.99451 | 2025-08-29 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52138022-eee3-310d-bdeb-5ca853f89581 | -12.6878 | -48.1677 | 2025-08-29 04:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 97a0b3be-b1e7-34be-b744-7b87afd6ba1c | -10.9903 | -46.9018 | 2025-08-29 04:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 4e9e57da-5b99-36c9-90a8-660a29ef9103 | -9.1156 | -65.7513 | 2025-08-29 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| e31bdf18-fba4-331b-aba4-b2ec111f5efe | -9.462 | -60.549 | 2025-08-29 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 65badd17-cd17-3e3c-92b2-09bc52fe1ae4 | -9.773 | -64.2469 | 2025-08-29 04:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| b1c4b9a9-8255-380d-976b-7e7d770bb72a | -12.7067 | -48.1873 | 2025-08-29 04:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 946215c0-577f-362b-9d31-68e2bc1704e2 | -9.1155 | -65.7699 | 2025-08-29 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| c498e6ae-2b2a-3cd5-b04c-3e31f65e0dc2 | -6.5546 | -43.9221 | 2025-08-29 04:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 35eaf954-fbe0-3e75-9d62-c08ced330ec8 | -9.9328 | -59.9247 | 2025-08-29 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| ecea51cb-0245-3ca3-9e95-9c8ec206c9fb | -9.4432 | -60.5692 | 2025-08-29 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8233bab7-7439-3648-9f33-b5e93cc63343 | -9.4433 | -60.5499 | 2025-08-29 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| da65ca3b-7f74-3ca1-9cc5-55a3c0a680bb | -12.6875 | -48.1899 | 2025-08-29 04:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 171.0 |
| b2fe453e-8d2b-32d6-8581-987143af7e9e | -9.4618 | -60.5682 | 2025-08-29 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| d7e2de2f-455f-3cf6-96de-fd870615fe12 | -9.7322 | -64.9067 | 2025-08-29 04:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 79f2dad8-3fcd-3150-9062-ac20582d44e5 | -8.1758 | -61.3755 | 2025-08-29 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7aad4bc7-a76b-3db6-8081-2c0ee9de2649 | -9.7728 | -64.2657 | 2025-08-29 04:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f34aaf38-7b00-3417-979e-01f13e9e7f94 | -9.1154 | -65.7886 | 2025-08-29 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ef26fd90-2f93-3b80-8629-21067d0098b1 | -9.7916 | -64.2461 | 2025-08-29 04:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8e02af0b-9f54-392a-b085-27d39389b071 | -10.9712 | -46.9042 | 2025-08-29 04:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 523de616-a7b3-3fad-bfa2-b1c0a551da38 | -12.81793 | -48.19053 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82107b06-4a77-30ed-9c03-a77ea0f474ad | -6.54385 | -43.93216 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6b9477b6-e194-34f2-b1a4-a405659487a1 | -11.24827 | -45.00668 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c832cff2-c825-3378-8da4-7a5f75d46f9b | -6.54315 | -43.10453 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9283bffa-e1fb-34b0-bbf5-e42f9262f1cb | -6.5444 | -43.92845 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| dfc9c84a-4c18-3bc4-b5f8-44467960e352 | -6.19335 | -43.32019 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdd0bca2-802d-32d1-96a9-b473834a3c7c | -7.5664 | -47.4976 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a814d152-70b7-3b23-850b-0c14528ff6ed | -6.34998 | -44.47837 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54df781a-3170-3f4d-b835-7aaaf4755e96 | -6.54497 | -43.9246 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d0481f60-9091-3279-919f-615c70ffe41b | -10.67452 | -47.09349 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1d51158-0833-3e43-9a33-9ac210177c48 | -8.10121 | -44.99787 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3e3f4db-3763-3e3e-a124-84ca0dc05753 | -11.30709 | -43.5516 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bf4c48c-4cfa-3130-b4e1-df9a3b101510 | -11.41168 | -46.91061 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc29bc5b-e541-3b81-9da3-9b87afc93485 | -11.35462 | -43.53974 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4db9b9c-5df0-32a9-9840-f0ba29b25b3f | -10.97082 | -47.39626 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92f7252a-223a-34ad-aee0-5b17b3a4ff08 | -11.6227 | -47.30797 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5940372-de38-3e87-b3f1-db2650a6eab4 | -10.67943 | -47.0854 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bb4e9e6d-39aa-393f-9605-6ca1e5ac5888 | -6.53612 | -44.11056 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8759172-761b-3be4-b36f-3df6572e4d1d | -7.76884 | -50.72546 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3442592b-664d-36c7-af15-c1f4d8bd2349 | -6.26839 | -43.83679 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b27bc0eb-9ad4-3aa3-962b-bc883ec40346 | -6.69843 | -49.46356 | 2025-08-29 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cd9544f-121a-349e-a846-8b2a68d917f7 | -12.09242 | -44.72167 | 2025-08-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 823e384e-a4bc-3635-8655-64848ea9987b | -6.70558 | -49.46114 | 2025-08-29 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 272e1d8f-482d-3335-b743-d6edd29cc754 | -6.72869 | -43.57656 | 2025-08-29 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5dbf6bd7-34c3-3d9a-b341-aaf58bcf5373 | -11.15373 | -54.30712 | 2025-08-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b21e2a02-4034-3bd4-8186-a7f46cc1cfcc | -6.54057 | -44.42874 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb0db29b-7aec-3acb-a59f-1d955434b281 | -11.32758 | -43.57471 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bd63fbb-c4e0-3e4b-bf7e-bf3fddf60b74 | -6.04447 | -44.46604 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 150d6edd-e7e1-38de-a594-0dca83d14d93 | -7.40367 | -43.37906 | 2025-08-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33478a7f-b8ef-3b2a-aeb6-8f38a64ec163 | -9.14974 | -59.57359 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a00ff0b7-e094-32a0-b621-b07cb247e198 | -9.29593 | -56.81385 | 2025-08-29 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53dad606-95bb-367e-82df-2033d26f231a | -10.98201 | -46.8989 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 367022b1-b4da-37ae-b6a3-6e0a140a3401 | -9.15096 | -59.56699 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6a838f7-a5f9-3b14-8e43-cbd6298af547 | -12.87661 | -48.13163 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c63a9a05-9646-3f3e-946a-7e2126daa674 | -10.84728 | -47.49937 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 075e445d-8cd3-3ed4-96ca-d9f68620d42a | -5.8384 | -45.30301 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a7e96f8-ac2b-37ed-a2b6-d4d0dd69c1cb | -9.48931 | -45.39386 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b94a3d42-53a5-39ec-b8af-a0a66223a63b | -12.40916 | -46.47731 | 2025-08-29 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61793e3b-7e76-30b9-aa93-626778fc1176 | -8.10769 | -45.00953 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f767a0c-da7c-3541-aa0f-76a9d4c1b79d | -12.82799 | -48.17145 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8ce8f6e3-d127-323d-a9ea-6066806c5700 | -9.45922 | -60.55789 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2c74c98-0eac-3514-9e99-0efddb666259 | -9.49875 | -45.38462 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14b2a1ff-bf3f-34f1-b1a2-e50a4a20d0bf | -9.76965 | -64.26085 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 32cecbea-7799-3d94-8c17-72a5304c0c38 | -11.53448 | -47.32325 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c08e41f3-c669-34a7-94d2-40252ad1f65b | -6.43162 | -44.57435 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5887e7c9-d56a-38e0-b57f-3287589defdb | -7.23219 | -45.42878 | 2025-08-29 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e620601-ec5b-306a-9a83-bd10587041aa | -12.83033 | -48.10545 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2a605b4d-484f-314c-a534-2fffaaf945ba | -8.69248 | -50.39074 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e5566ab-e45b-3e5b-91f8-c6d83f7e98c2 | -11.04023 | -45.13968 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56cbd238-da29-3414-b9ba-11815e0876f1 | -12.81497 | -48.18593 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b63afd7-8462-3e72-b418-47bf484b0bca | -8.28297 | -47.20589 | 2025-08-29 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94fed21d-16b9-382c-ac39-0f57c9d31432 | -7.08365 | -44.2983 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1a12796-efd8-3b80-86f0-e328e3585a83 | -11.26118 | -45.4986 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a07967cf-8eaa-3eeb-8af5-616907ecdfc8 | -11.42284 | -55.17245 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3fdc23a-2c1f-32ec-ba27-8c981e724f88 | -11.58098 | -46.26994 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9d62e14-01fa-3a7e-bba8-9caf27731884 | -8.28585 | -61.40441 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77c28834-cd64-3d5d-8c63-e2a9f0821e22 | -10.97893 | -46.89383 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5419ddf8-197e-303b-9adf-5ab3e4025b21 | -11.06386 | -44.77131 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 250c2604-38dc-393a-aa21-afbd41dfe8bf | -7.72317 | -50.28168 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 654daf2b-cf3d-387c-9f59-fdc52b298bb1 | -10.97578 | -46.91634 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 0def6274-1831-3283-bbbb-411bfaa13979 | -6.53723 | -44.10277 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27e033c7-2884-3825-9bf6-6cecbb763b9d | -6.19099 | -44.00742 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cce1d77-5628-329e-b35c-b8f07cddc99d | -11.16289 | -47.15496 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7c29be6d-dca5-372b-adb6-91bd7e35f981 | -7.67717 | -44.99274 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5c37799-e88d-30c5-a1e9-6b10e772d502 | -5.84221 | -45.30363 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba33e2f5-d54c-30d5-8f63-3304d959d10f | -10.97949 | -46.91686 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 7a363161-14e6-3b88-9ff5-0dd903b150e7 | -6.19156 | -44.00351 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9f9ffb2-8345-38e8-a038-2d6aaa91d7b0 | -12.02435 | -49.70973 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0019795b-c754-3ee0-ae11-39a787668586 | -11.56625 | -46.37386 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04ff4468-ad66-352c-acf6-19648c4dd576 | -10.47972 | -57.93461 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b60a1d68-92ca-3820-a3de-2a0208b04cc4 | -11.22348 | -55.05443 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18259fda-09f6-30a3-ba4a-4d17eed13ff8 | -12.86726 | -48.10224 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 344a4161-6186-3583-8556-d362835c44dc | -10.46569 | -57.93201 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4fa40d69-da88-3c9b-828e-631b852fc633 | -11.55467 | -46.3722 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 34faec21-95f1-3de8-a37f-b426ccaeb079 | -12.84108 | -48.15648 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 169975f6-6c42-3159-92b8-ce28590e86d6 | -13.19436 | -45.28419 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 81865139-4ea5-390c-9445-f0ed16bf4ae8 | -7.54901 | -47.47105 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 524343de-88dd-3df6-bac5-4b1f69317910 | -9.60049 | -40.35535 | 2025-08-29 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 42b27942-ba67-3a09-a6ff-98e43a919bfd | -10.02542 | -51.10754 | 2025-08-29 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README41.md)
