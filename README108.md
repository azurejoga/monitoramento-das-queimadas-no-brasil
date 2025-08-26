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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30b4929a-6958-3421-a979-a33b0fdc1821 | -8.2522 | -45.1168 | 2025-08-26 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 40f2a2ad-4a41-323d-af63-fc60b9600618 | -11.2014 | -50.5685 | 2025-08-26 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 58bee9a4-52ec-3859-9f0f-76c15a9f3228 | -10.9361 | -50.5759 | 2025-08-26 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| dd852a7a-f38f-3975-905d-3b550edaa7cc | -6.1377 | -44.3711 | 2025-08-26 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5c8f15b7-502b-354a-a2aa-944e4adc57c3 | -8.9874 | -65.4192 | 2025-08-26 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c50cb64e-0405-3a84-976b-914d021725d9 | -11.2201 | -50.5878 | 2025-08-26 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 75e17bb8-8853-3bf6-b7a6-a6aaedf80b30 | -9.4064 | -60.5133 | 2025-08-26 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 318.4 |
| 42e2511f-60bb-3cab-b984-6489b08fa112 | -6.6201 | -44.8581 | 2025-08-26 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| a2c5c46a-9d32-3276-a670-baae35e6368e | -13.423 | -46.873 | 2025-08-26 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d7ef24a9-5a2c-3014-9f24-811a9d32f9d0 | -8.8734 | -62.4495 | 2025-08-26 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a17e3d56-09c4-365b-b262-cea8de2425f0 | -8.5065 | -47.4002 | 2025-08-26 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d60ebd2f-2a15-3cff-8c26-ced91302d33e | -9.181 | -60.8131 | 2025-08-26 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| ae74cc9d-fb70-34c4-a914-818990be66ac | -6.8062 | -45.0019 | 2025-08-26 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| b8fac13b-08d2-312c-b774-a431ef9480d9 | -6.7145 | -58.5539 | 2025-08-26 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| f7a2b233-b9e1-3aab-aa1b-2013668a1e28 | -8.5387 | -62.6527 | 2025-08-26 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.1 |
| cb791b6e-8971-3ea7-911b-5411b094797b | -11.3979 | -47.608 | 2025-08-26 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| d8c389d7-6336-3aa1-9889-359c57862fda | -9.7916 | -64.2461 | 2025-08-26 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 2cec254f-9d62-3a9e-9852-ac66241dfe8e | -11.54 | -52.119 | 2025-08-26 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 6b188d74-ca34-3b67-898b-9935c09e0fdf | -14.3912 | -51.9508 | 2025-08-26 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 11a4bab7-3a0c-39de-b431-b0dc36e1ba99 | -8.0841 | -44.997 | 2025-08-26 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 95cef8a0-2a32-3057-877b-41f82ae47132 | -6.7635 | -59.6718 | 2025-08-26 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.9 |
| a147e9d4-0fb6-30de-9855-9413f19b22d8 | -9.0415 | -65.7349 | 2025-08-26 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 87231b1c-9b75-3d93-8c7c-fc975c48ead8 | -15.6557 | -52.7366 | 2025-08-26 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a6b0aae4-9e9c-35b6-be06-48aa3b45fae2 | -9.1375 | -45.2493 | 2025-08-26 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 268.8 |
| b352cf5c-b544-3b7a-9e97-0ea7bfa375c8 | -7.5391 | -44.9362 | 2025-08-26 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 739df86d-7f0a-3e01-a1f4-b3f84e76c6a2 | -13.4397 | -47.006 | 2025-08-26 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8ad59210-ea1e-3a3e-8640-928e52382bf7 | -6.6961 | -58.5546 | 2025-08-26 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 4d854346-984b-3996-bf79-47eb1ccd70a8 | -12.7843 | -48.1321 | 2025-08-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 97251cf3-18a2-3cb0-90d8-e57f3845beb8 | -7.8851 | -45.9004 | 2025-08-26 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a233c5e1-fe41-3251-a879-949690fa6622 | -11.417 | -47.6055 | 2025-08-26 14:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| f01b96bd-cb35-3812-aa66-a66234390103 | -9.5811 | -55.3713 | 2025-08-26 14:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4b3033a4-4d9e-3147-b95c-258fd5ee2f01 | -7.9042 | -45.8761 | 2025-08-26 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1fe478ec-b4c0-348f-84d1-ce0c53a943d1 | -5.4549 | -60.1582 | 2025-08-26 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| f89fd0ca-a421-324f-a6f4-5d44492f31c8 | -9.1812 | -60.7939 | 2025-08-26 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 6a6f0390-9be5-3586-a79a-1ae4d3cff650 | -8.1587 | -45.0579 | 2025-08-26 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a6138a96-956e-3d2f-b780-c539b906c268 | -11.559 | -52.117 | 2025-08-26 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| e8d5cfb1-8670-377e-b657-28a95c69cc45 | -8.855 | -62.4313 | 2025-08-26 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 1de31ae7-2137-3536-b145-f27e8c06408a | -6.2458 | -60.0365 | 2025-08-26 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 7114f9a5-c51d-3acd-aa3f-a5140f89516d | -8.8735 | -62.4305 | 2025-08-26 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b7cbfa90-af14-3547-b27b-854371f85557 | -9.1722 | -59.4629 | 2025-08-26 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 29e5eab2-6294-350d-8c8b-d936f0557dda | -6.9128 | -59.3578 | 2025-08-26 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 61357832-7d38-3bd7-9f7c-d2e3b8407eb5 | -15.1101 | -48.7352 | 2025-08-26 14:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 100.7 |
| b896128e-6f54-34e5-9c49-8489b493eab2 | -6.8873 | -44.4234 | 2025-08-26 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 8d7ebb38-b4f4-3228-8559-c4e8384dfa9f | -9.2628 | -59.7874 | 2025-08-26 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6fc22136-6d35-3db1-be22-c2e168cbbd08 | -9.006 | -65.4 | 2025-08-26 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 2044079c-c54f-3eee-b610-b5f303cc33ff | -6.8064 | -44.9791 | 2025-08-26 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 32baba9e-4487-394f-bb67-9fa454a48470 | -6.5293 | -44.5687 | 2025-08-26 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 8092476b-bbfa-3ee3-b692-88cadb98e7d3 | -12.6741 | -47.8589 | 2025-08-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 77321053-b673-38a1-baaa-9d59befca477 | -8.2333 | -45.1187 | 2025-08-26 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 214.4 |
| d130b691-cd5a-36f0-8ba3-dd6182766180 | -12.338 | -64.2272 | 2025-08-26 14:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 7d3fb99c-175d-3e16-bc6d-af7f3f4f17e1 | -12.7651 | -48.1348 | 2025-08-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| bb3f685e-9351-34b3-a75b-1538d2e312b5 | -10.6822 | -47.1635 | 2025-08-26 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 8191143b-ed38-386b-95b9-58eb6da8bcb6 | -12.8123 | -49.8599 | 2025-08-26 14:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6ebccd6f-7d47-34c4-ab8a-5682928b560d | -6.2276 | -59.9989 | 2025-08-26 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4640ee78-4785-3060-9ee7-8bff3c18b148 | -6.2459 | -60.0174 | 2025-08-26 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 299.5 |
| bdf5d844-ed69-321b-8fc5-cf10dfaeaf37 | -8.8548 | -62.4503 | 2025-08-26 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 7e4a9311-92e2-3fbb-91c9-7a92cb946281 | -12.6745 | -47.8366 | 2025-08-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 2d235c35-5c6b-3b03-bd2a-8ee97bed25ca | -9.8101 | -64.2642 | 2025-08-26 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 21cab15b-aaff-3f64-b084-eaaff030762f | -12.7451 | -48.1819 | 2025-08-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 167b2dc2-f621-3e65-8bfa-abfd3e658090 | -6.246 | -59.9982 | 2025-08-26 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| fa72b8ee-3d2b-3252-b6b4-9590318648bd | -6.2275 | -60.018 | 2025-08-26 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 0c7c9b47-184a-3a92-89be-d6b7878952ea | -12.6737 | -47.8812 | 2025-08-26 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 1851d8cb-a2c0-3783-a2e3-fcc9deb8c495 | -7.4224 | -60.6236 | 2025-08-26 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 40a5a2a9-3020-32de-a463-375f0dc127a4 | -7.8854 | -45.8779 | 2025-08-26 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 4ac70d83-2b89-3868-b269-d9ca7841307a | -6.7819 | -59.6711 | 2025-08-26 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| bd8acbb7-b3ec-3727-ba30-848653c988e3 | -9.8287 | -64.2635 | 2025-08-26 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 15ad3989-651e-3ee1-9ba3-be2ab525d32c | -11.9129 | -47.6074 | 2025-08-26 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 80bdff57-f35b-375e-9465-ef2d0af33614 | -9.7915 | -64.265 | 2025-08-26 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 229a650f-da82-33d5-9c8c-3759d5dcc961 | -9.023 | -65.7355 | 2025-08-26 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |


