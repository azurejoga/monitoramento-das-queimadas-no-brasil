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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4caec2b4-4261-30b0-a57a-4c678ae0bb49 | -6.0664 | -43.9854 | 2025-08-26 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 5a67704b-6d7b-33c0-94be-679e52589189 | -13.423 | -46.873 | 2025-08-26 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f2441815-bda9-3585-baee-d281ce6a84aa | -11.54 | -52.119 | 2025-08-26 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 0644dce9-6333-3b8e-9e30-4fe65d937480 | -11.9129 | -47.6074 | 2025-08-26 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 77db1845-c915-3132-b9a0-20be0d1eff9d | -7.5673 | -47.4851 | 2025-08-26 13:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| cfa87e83-3299-34aa-a861-bd15cb21a015 | -11.559 | -52.117 | 2025-08-26 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 8c091f0a-8df0-3029-9d83-5f3791770b1a | -6.2275 | -60.018 | 2025-08-26 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d8dc5dd4-4c11-3506-9823-a7b51f540866 | -11.6273 | -46.4126 | 2025-08-26 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| cfa481a5-75e3-37f8-94df-bebc2030a376 | -9.7916 | -64.2461 | 2025-08-26 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 23cd9396-e672-3f5e-93ab-06ba4db7a727 | -11.6308 | -46.2083 | 2025-08-26 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f406b8db-3968-38c9-bdeb-c4e5fe9509ad | -6.8064 | -44.9791 | 2025-08-26 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b6efbba5-3791-3870-ab60-511cac0882f9 | -7.5673 | -47.4851 | 2025-08-26 14:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e05f02bb-217e-39e5-b3b3-b4dc84a293ed | -6.5293 | -44.5687 | 2025-08-26 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 398.9 |
| f03d8c0d-cf38-37e8-aa15-81674f15b6d8 | -10.6818 | -47.1858 | 2025-08-26 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 5c3b08d7-1a15-378b-8c00-2f923f2c4bb0 | -6.8228 | -58.9753 | 2025-08-26 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 312.2 |
| 7dc3718c-f83a-35aa-a355-e5cd439eb6b9 | -6.2458 | -60.0365 | 2025-08-26 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 633a6044-1be6-3ef4-a6b7-73d057dc2b65 | -11.5779 | -52.115 | 2025-08-26 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 78428956-2c3f-3cf4-9f50-c1a795284f67 | -7.586 | -47.4835 | 2025-08-26 14:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 557b6d08-104b-351d-82ce-a0c0df5e8005 | -11.6351 | -44.8561 | 2025-08-26 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 0dcb4a50-462f-3e72-8d0f-093310dc4fa2 | -8.3521 | -62.9247 | 2025-08-26 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 378f1aa1-dc00-3d6b-8155-e55420990298 | -16.6224 | -49.3708 | 2025-08-26 14:00:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 13921146-f01b-3299-acbc-9056dc45cd7a | -11.2423 | -45.4646 | 2025-08-26 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a520cd58-e179-3764-ae53-4b77e4d759cc | -11.559 | -52.117 | 2025-08-26 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| a5aab03b-7059-39dc-a740-87b8c9dd1ce9 | -6.8062 | -45.0019 | 2025-08-26 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| ccf8ed97-eb0d-3b85-a378-3c4c9787ce09 | -6.8413 | -58.9552 | 2025-08-26 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| dae39974-c301-3f9e-985b-e2099112bd18 | -9.1722 | -59.4629 | 2025-08-26 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6e4795f1-bd4c-34ac-a7a9-174edaf9fcbd | -14.3912 | -51.9508 | 2025-08-26 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7f14c30f-63c7-31e1-8fba-3f53c86dedfc | -6.2553 | -43.8314 | 2025-08-26 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 59359a65-62ec-3cc5-94cf-cc68fb044b4e | -6.7635 | -59.6718 | 2025-08-26 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 9af4d1b3-242b-3ef1-82fa-591b54331bb9 | -12.7651 | -48.1348 | 2025-08-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 4d2ed1bd-9dd4-3a1f-9b88-75649a47e8f5 | -14.7135 | -45.3929 | 2025-08-26 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3a1d14bb-34f6-33f3-b718-162eb9849536 | -10.6825 | -47.1412 | 2025-08-26 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e79605c9-d14d-34aa-8183-e97e5ce54f1c | -6.246 | -59.9982 | 2025-08-26 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 36c3b544-c209-3a5d-ab09-2f257cce4380 | -8.9874 | -65.4192 | 2025-08-26 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 45928aaa-c49c-3798-b001-a4314f1c6fa4 | -9.9325 | -44.0232 | 2025-08-26 14:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b76708a5-0681-3dcc-8a77-fa93ca0058d0 | -12.6548 | -47.8616 | 2025-08-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d46023bc-deb2-3c33-ada4-85d5e0f45ab0 | -8.352 | -62.9436 | 2025-08-26 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 115.6 |
| b4531066-f0c1-307d-8e2f-4043112b453e | -12.6741 | -47.8589 | 2025-08-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 8e169286-9103-3224-929b-167641fd6fa7 | -9.8101 | -64.2642 | 2025-08-26 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1fb33896-4173-3f6f-9100-7e3d507c8db4 | -10.6822 | -47.1635 | 2025-08-26 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 191.7 |
| b57eb5f4-cd9e-3c82-bd1c-905120b96f0c | -6.8044 | -58.9568 | 2025-08-26 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| dfdd413a-4ce1-3996-831c-49c08f3814ea | -6.2459 | -60.0174 | 2025-08-26 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 277.7 |
| 429ac6c1-c579-3921-acf5-9341ce33c86f | -12.7647 | -48.157 | 2025-08-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 8e0826f8-ad7b-358f-8f20-b0b54a2413f2 | -11.54 | -52.119 | 2025-08-26 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| feb195fa-1085-3baf-a8ee-ad1a0118df96 | -9.8102 | -64.2454 | 2025-08-26 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 9d897264-8cd5-3a90-b319-279f3cf71208 | -9.7915 | -64.265 | 2025-08-26 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 032e3b16-a2e4-3bc2-9d8c-ae6b118fffc6 | -6.1377 | -44.3711 | 2025-08-26 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| b578d1d5-691b-3ee6-a716-d6aeeb0a7b59 | -11.2014 | -50.5685 | 2025-08-26 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 4cb4859b-cdc1-3a3b-90f5-75963eaf03cf | -6.9128 | -59.3578 | 2025-08-26 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| c40a0f70-f174-3efa-86fd-4435e1ae30f7 | -12.7932 | -49.8624 | 2025-08-26 14:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 298.2 |
| 8dd633ca-d1ff-3195-a054-abc7f3108a83 | -13.423 | -46.873 | 2025-08-26 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| bd46d6db-2e9d-3814-a141-8e4d1a1afb60 | -12.8123 | -49.8599 | 2025-08-26 14:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 182.6 |
| b0655963-ce2d-38fb-8c07-41f00f777cb2 | -6.6201 | -44.8581 | 2025-08-26 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 7243c84e-fccb-3dd1-bb88-db70bc60c069 | -6.8873 | -44.4234 | 2025-08-26 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| e4f393c4-6120-365e-9c13-1c4941fe2dbb | -12.7843 | -48.1321 | 2025-08-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 64cc3612-af33-3129-889c-481d4765ba1e | -11.6086 | -46.3926 | 2025-08-26 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| f00a9aff-49e0-3f77-aa49-7d1e74a66acb | -6.8229 | -58.956 | 2025-08-26 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 239.5 |
| 325daf22-07ca-31bb-a584-0e54104e2f53 | -6.1375 | -44.3941 | 2025-08-26 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 7b865217-4993-342e-a1a0-8f790a306d88 | -6.8412 | -58.9746 | 2025-08-26 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| abfafd62-879c-3224-83c8-7c605955f87e | -12.6737 | -47.8812 | 2025-08-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| cdbca349-089e-33a6-8522-af1003438c56 | -6.9061 | -44.4217 | 2025-08-26 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b9bf22e4-b152-38fb-98b5-debb6bb564cc | -18.975 | -48.1979 | 2025-08-26 14:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 96.2 |
| c7955441-aef5-3a08-b269-0533f5495094 | -6.2275 | -60.018 | 2025-08-26 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 07917eac-6a81-3556-b2d8-5bff4af50999 | -8.5387 | -62.6527 | 2025-08-26 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| cf6426d6-28f2-3058-97df-dfe3c573889a | -6.7819 | -59.6711 | 2025-08-26 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d2512cef-f035-31c5-9c5c-5c9bc77e4da4 | -12.6737 | -47.8812 | 2025-08-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9ace587f-b911-3fd4-9413-0fd5aaa6d261 | -11.559 | -52.117 | 2025-08-26 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 244a3e9c-20f6-35de-9b05-a718c90de592 | -11.9277 | -46.7322 | 2025-08-26 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6415bcb1-6be4-3f57-a1dc-a225399cf0a3 | -8.2333 | -45.1187 | 2025-08-26 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b2deb2b6-d88c-3158-a254-3aa54d371151 | -12.7932 | -49.8624 | 2025-08-26 14:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 23b81a71-cdc8-3056-a02c-33daee758fdf | -11.54 | -52.119 | 2025-08-26 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| e6452c8f-383d-31df-8f24-2dc84c8176fc | -6.8064 | -44.9791 | 2025-08-26 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9050c56a-9982-3a41-896a-3fe487f227bf | -14.4105 | -51.9482 | 2025-08-26 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| ccefa6ec-6d5e-357e-9b0a-8b06aa7c1331 | -6.6201 | -44.8581 | 2025-08-26 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.1 |
| e0fafdb8-ce35-3b4c-8db7-8b49e6355439 | -6.8413 | -58.9552 | 2025-08-26 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 35a068a3-1df5-311f-8300-276eb3178af9 | -6.2275 | -60.018 | 2025-08-26 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| d93bf900-9492-3afb-a5f4-daf88bb0cb11 | -5.4549 | -60.1582 | 2025-08-26 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 42d00be4-de5e-380b-b4b8-7326cef18adb | -8.5387 | -62.6527 | 2025-08-26 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 32f5824a-9c6a-322f-9017-580bb2a34f2f | -11.6978 | -51.6814 | 2025-08-26 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 325267ff-8536-3fe8-88df-7ff25c16355c | -11.6082 | -46.4152 | 2025-08-26 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 70976ff9-448d-3aed-9ba9-5ba456888e8a | -9.1812 | -60.7939 | 2025-08-26 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f8a4af99-e5e8-3425-9a20-dccaba9245e6 | -7.5391 | -44.9362 | 2025-08-26 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6bf29e81-b047-30c5-a248-42e7fb64386d | -6.8229 | -58.956 | 2025-08-26 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 328.0 |
| e82bb754-02af-31f0-92d6-80430d90fb10 | -11.6086 | -46.3926 | 2025-08-26 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 7360d6ac-46c3-3d87-895a-b7413c278958 | -11.6308 | -46.2083 | 2025-08-26 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 242.6 |
| b3bbba4d-6215-37f6-9639-170f4cf6a9c7 | -16.6224 | -49.3708 | 2025-08-26 14:10:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 21afae3a-2145-3c60-b0a2-04ad1a33527a | -12.8123 | -49.8599 | 2025-08-26 14:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 7be38903-ccea-3092-aaba-0e42560d5272 | -9.1375 | -45.2493 | 2025-08-26 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 288923ba-69b4-3d47-b58a-1a51d2815834 | -6.5293 | -44.5687 | 2025-08-26 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 7e38a108-4042-3beb-a48c-f3422867805a | -6.2458 | -60.0365 | 2025-08-26 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| de316653-5495-3d0d-a32a-c6e18e182ee4 | -8.352 | -62.9436 | 2025-08-26 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.5 |
| f2b55396-e9e9-3ce9-99c7-58ff4c4b43ce | -12.7651 | -48.1348 | 2025-08-26 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 73a30ad1-6362-3c93-90bc-4c2d2313b7cf | -9.7916 | -64.2461 | 2025-08-26 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 122.7 |
| eeb4d717-3a0a-3fd7-b8f1-a46e540e0d3b | -9.8102 | -64.2454 | 2025-08-26 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 119c6ee1-e89d-35bd-8076-9f44a2abf80e | -9.8101 | -64.2642 | 2025-08-26 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ffbe62c5-47b8-3552-86f1-0978c0e6e0ce | -6.8044 | -58.9568 | 2025-08-26 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 2712ded7-20e2-3b94-b876-4d4832140381 | -6.8228 | -58.9753 | 2025-08-26 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 508.5 |
| ed083dce-41d8-3425-811f-41aa0df7e427 | -9.181 | -60.8131 | 2025-08-26 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f7e8b22c-087c-34a2-8dcb-331d7972857b | -9.1722 | -59.4629 | 2025-08-26 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 305f5ebe-936a-3737-bb63-ce9b14506ad1 | -11.7165 | -51.7005 | 2025-08-26 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 219.5 |


[Clique aqui para ver as próximas entradas](README107.md)
