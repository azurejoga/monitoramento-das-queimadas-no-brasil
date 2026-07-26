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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 880f94ff-1690-3e49-8064-da5baf43eb86 | -3.7224 | -48.8696 | 2026-07-26 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| fccf65c5-550c-3e53-9937-06019b35df2b | -11.1443 | -44.4865 | 2026-07-26 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 277bc4c4-935d-3309-8dc5-f30893f3fa53 | -3.7224 | -48.8696 | 2026-07-26 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| c1f3032a-afac-3e16-b395-2518ef7674ef | -11.1443 | -44.4865 | 2026-07-26 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| d1963e8d-df3c-3e7e-ae90-3d76183c0c6c | -5.6815 | -49.8184 | 2026-07-26 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 80aabb63-05ee-3d9c-94f4-325e761ccd5b | -11.1635 | -44.4838 | 2026-07-26 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 6f6e6b55-3db0-308b-ad8e-9037a459828d | -3.7224 | -48.8696 | 2026-07-26 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 60f4edfb-2a00-38f2-8802-f21b2143e25e | -11.1443 | -44.4865 | 2026-07-26 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2ffd3517-6fee-363f-a913-2ca09ca0c765 | -11.1447 | -44.4632 | 2026-07-26 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 386668a6-4f4d-3431-8bd4-9666ed125a31 | -3.7224 | -48.8696 | 2026-07-26 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2beb0b5c-159b-38da-a7ff-02ada35dbb96 | -11.1447 | -44.4632 | 2026-07-26 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c6e06032-e629-36b2-b282-0133680cd948 | -11.1443 | -44.4865 | 2026-07-26 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e53bb938-3d55-3ac4-b9d4-6e2cbf97b431 | -11.1635 | -44.4838 | 2026-07-26 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 91b94ca8-01e6-3d58-a768-24db8d8a290f | -11.1443 | -44.4865 | 2026-07-26 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 3a55e1c2-aa9d-351a-91c2-62dada139cbf | -3.7224 | -48.8696 | 2026-07-26 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| cf50d9b4-32f6-32ed-aae0-484ce7d5ac98 | -11.1447 | -44.4632 | 2026-07-26 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2ae0c560-e9b6-3f45-8b06-3de435f1c584 | -11.1635 | -44.4838 | 2026-07-26 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d79769bd-2883-3046-bee2-9b622dc12e96 | -11.1443 | -44.4865 | 2026-07-26 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e374c023-249b-32f0-aade-a77aa1bdafd8 | -21.27693 | -56.0317 | 2026-07-26 00:52:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2f2c9179-6b8c-36f7-93c3-207f03b778a2 | -18.49205 | -54.10704 | 2026-07-26 00:52:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cdde10d8-5e01-3317-a76f-d93550711ab9 | -9.8365 | -62.2164 | 2026-07-26 00:54:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 48553251-4341-38a1-8262-99243f28fe34 | -8.8957 | -60.60017 | 2026-07-26 00:54:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0cd61e36-3e19-3c3a-abd7-7bb2fb4112ee | -13.80626 | -53.86717 | 2026-07-26 00:54:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d5a3cc23-5320-3771-ae0d-84a6504941a3 | -12.54213 | -57.22534 | 2026-07-26 00:54:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d92cc3ab-e6b7-3990-9153-b1fe25986734 | -9.83773 | -62.22556 | 2026-07-26 00:54:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c88e0005-0a72-3c3f-b235-e2aaff462e98 | -9.73121 | -63.43755 | 2026-07-26 00:54:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eb58912d-db30-3485-a0aa-7fb82b3b77d4 | -9.7299 | -63.42746 | 2026-07-26 00:54:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5395d435-837f-3c4b-81a6-13924996a848 | -12.5403 | -57.21341 | 2026-07-26 00:54:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7db4e0b2-6753-3787-b2a0-3997c8d53c22 | -21.280899 | -56.0214 | 2026-07-26 00:55:00 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a9a10d63-e8ca-3a1b-88f9-c0155fc78a23 | -3.7184 | -48.8759 | 2026-07-26 00:55:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89c2a9a7-0e45-3c10-b4f7-2669c5f31a23 | -9.841 | -62.203499 | 2026-07-26 00:55:00 | METOP-B | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68554f95-a865-36f4-98d5-71dde50cfca5 | -11.0141 | -54.307201 | 2026-07-26 00:55:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01c28578-24a7-3b25-9094-b2176b08bb79 | -9.735 | -63.4203 | 2026-07-26 00:55:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a25a1bd-9d2c-37cf-989c-900774c6b003 | -9.8426 | -62.210999 | 2026-07-26 00:55:00 | METOP-B | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dae36df9-20c7-3dc8-ba07-fa2c990dd230 | -9.4947 | -64.068604 | 2026-07-26 00:55:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 48c6ff1b-a58b-3b81-b0e6-a0c5cf066b9e | -8.5824 | -59.012299 | 2026-07-26 00:55:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4823248c-73a8-3eaa-ae34-cb1084aa2c4c | -8.8982 | -60.590199 | 2026-07-26 00:55:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1a220a-a136-316b-a564-3d3a4c1d2af2 | -18.4928 | -54.092701 | 2026-07-26 00:55:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bcfc4756-45e7-375d-adbc-d0a7fabb00fe | -12.5398 | -57.203098 | 2026-07-26 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe3eba5-08fe-3a59-b704-be36d24a0c9b | -21.2827 | -56.028999 | 2026-07-26 00:55:00 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 16471bbd-41df-3576-a9f1-dd33b98ff99f | -8.584 | -59.019501 | 2026-07-26 00:55:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef9cf64-3656-3691-ab30-71b35c88aeb2 | -12.5416 | -57.2108 | 2026-07-26 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49406fe3-4f9c-392a-b030-ecf39f96c8c6 | -3.17998 | -60.65895 | 2026-07-26 00:56:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c21a1623-5fe6-3445-9534-6ce161a30368 | -11.1443 | -44.4865 | 2026-07-26 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| dc97ea68-9965-3d45-95a5-b387c38fe613 | -11.1635 | -44.4838 | 2026-07-26 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 92a78176-1a7f-38e3-94cd-1c8853988022 | -11.1447 | -44.4632 | 2026-07-26 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 09a6df0d-0c63-371d-9b72-b678d2f80b8e | -9.4773 | -40.3116 | 2026-07-26 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| b01ea317-fed3-3774-a5ed-122b644d8be5 | -11.1635 | -44.4838 | 2026-07-26 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| fb94e735-1e77-39aa-b384-2a42f4bfc0ae | -11.1639 | -44.4605 | 2026-07-26 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b878881e-40b4-30ed-aa8d-ca810458c0bf | -11.1443 | -44.4865 | 2026-07-26 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c2ab4725-3972-30dc-8451-2c53f04c3959 | -9.4773 | -40.3116 | 2026-07-26 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 9ffe9f38-0981-347d-90df-7a0812385b8c | -11.1635 | -44.4838 | 2026-07-26 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 35eacbda-e6e4-30d8-99d7-8e479f1a9dc2 | -11.1443 | -44.4865 | 2026-07-26 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| a063a147-2054-33c7-8b2b-eb0a9e1ca5c4 | -11.1447 | -44.4632 | 2026-07-26 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 97ff09dc-18da-3b71-adb1-e270d860cafe | -11.0212 | -54.313999 | 2026-07-26 01:20:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 776d6c5c-69b0-3ace-8f38-0dabbe6c7afd | -9.4898 | -64.076202 | 2026-07-26 01:20:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 192e0046-6b7a-3cfd-9522-8a3347a0dc43 | -3.1339 | -58.999901 | 2026-07-26 01:20:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c75cc69a-5696-3969-b01c-a53413608328 | -18.497299 | -54.101398 | 2026-07-26 01:20:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0235713c-05b7-30bf-a4f9-4178b226e4c7 | -13.37 | -54.280701 | 2026-07-26 01:20:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55c38e7b-969e-33cb-84cb-0558f711a1e2 | -3.1225 | -58.995201 | 2026-07-26 01:20:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17d848fa-6269-3d09-ad0d-2b315419b0fb | -9.8416 | -62.2206 | 2026-07-26 01:20:00 | METOP-C | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8c4c8978-24cd-3fbb-956c-1bb2ab1500f1 | -3.1323 | -58.993 | 2026-07-26 01:20:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eaa35683-7dd1-363e-a471-48623204f1af | -18.691799 | -44.533501 | 2026-07-26 01:20:00 | METOP-C | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a565977e-ca81-3105-a750-8084a356a5cc | -3.1241 | -59.002102 | 2026-07-26 01:20:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d51c36e8-60b8-3750-a479-3004139734c5 | -9.8396 | -62.2113 | 2026-07-26 01:20:00 | METOP-C | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9360c452-5d64-30b9-9f02-c8a2e4d5f237 | -21.2817 | -56.0289 | 2026-07-26 01:20:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5702e940-b19a-3e1f-9f48-d9f1cc0e0c65 | -12.543 | -57.213699 | 2026-07-26 01:20:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef446716-6dda-328c-9549-bcafc50cc437 | -3.7299 | -48.8666 | 2026-07-26 01:20:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab5ecf15-6703-3e4e-aec2-fa7ec37b9e56 | -13.6911 | -51.896801 | 2026-07-26 01:20:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 19953221-675c-319e-8911-3e87fb68d7ff | -13.3719 | -54.289001 | 2026-07-26 01:20:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f3a9443-78a4-3068-b7bc-837c89416b68 | -8.8924 | -60.596001 | 2026-07-26 01:20:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10a49458-a5fb-31a7-a87f-6e7aab12a50d | -11.1635 | -44.4838 | 2026-07-26 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 1e58e96c-381c-3f33-b3fe-fedfb487123a | -11.1443 | -44.4865 | 2026-07-26 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 3c07f515-d4c6-381e-bb20-e6f0aa61813e | -9.4964 | -40.3088 | 2026-07-26 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 7e3a7a1c-7f5c-39bf-bfb3-76413979a7b0 | -9.4773 | -40.3116 | 2026-07-26 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 97b3ebf0-85f4-3434-94d2-3c135bdda7b5 | -11.1635 | -44.4838 | 2026-07-26 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 081f56a7-fd96-34f2-ba5a-0491c36c4854 | -11.1443 | -44.4865 | 2026-07-26 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e365a622-e383-39e9-82ee-cd82eaa4992d | -9.4773 | -40.3116 | 2026-07-26 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 40c8770a-6c3a-39f6-9e64-18a8837f679f | -9.4964 | -40.3088 | 2026-07-26 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.2 |
| c2c323d3-b80c-302f-b4da-18fadedc5868 | -11.1443 | -44.4865 | 2026-07-26 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 99b826f5-994d-368a-96a7-399f71c8f57f | -9.4773 | -40.3116 | 2026-07-26 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 42091baf-7771-3209-b636-d54fbe9af47c | -9.4964 | -40.3088 | 2026-07-26 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 145.5 |
| e5176b07-a3ac-33d7-b200-4d90ce0b6c60 | -11.1635 | -44.4838 | 2026-07-26 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c624e33f-690d-37c8-9373-c4797590d3de | -11.1635 | -44.4838 | 2026-07-26 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ce84aeba-8301-3c46-8496-a404ab19ede1 | -9.4968 | -40.2839 | 2026-07-26 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.8 |
| d20a80fb-d488-3f5d-9462-ecf9034e51d7 | -9.4964 | -40.3088 | 2026-07-26 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 189.9 |
| ba004280-0254-3b18-8085-5e6ee9103719 | -9.4777 | -40.2867 | 2026-07-26 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 9fe1d1c0-8ac6-3a4b-b0ad-12ca93d8e88e | -9.4773 | -40.3116 | 2026-07-26 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 199.3 |
| b3d13ad6-a651-32d8-bb13-8cf8c5cfd909 | -11.1443 | -44.4865 | 2026-07-26 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3c01ebef-8185-399a-874f-2bdfda1815f7 | -11.1443 | -44.4865 | 2026-07-26 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| f872fb3d-f0c1-39fc-91b5-af5b0253b439 | -11.1635 | -44.4838 | 2026-07-26 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| d5ab88b5-ab57-3044-97f5-2cb032ed26f6 | -9.5 | -40.31 | 2026-07-26 02:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9e5905de-1a63-3790-851f-c32513ff6efa | -9.47 | -40.3 | 2026-07-26 02:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a6fbef39-cf5b-3085-ae17-1985f72804e5 | -11.1635 | -44.4838 | 2026-07-26 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 83c60a25-2b73-31f6-984d-728d0a5e19d9 | -11.1635 | -44.4838 | 2026-07-26 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 1d1aed80-1780-381a-91df-f04ec35655bb | -11.1443 | -44.4865 | 2026-07-26 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 2ba1d7aa-5495-3638-9852-34d07c1e37c9 | -11.1443 | -44.4865 | 2026-07-26 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| b6ec46f7-d988-344e-bd6e-105698ff4640 | -11.1443 | -44.4865 | 2026-07-26 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 00ed9281-419c-3f15-a903-a9dd76a10613 | -11.1639 | -44.4605 | 2026-07-26 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| de111513-dd9e-3a84-86dd-259fa8718461 | -11.1443 | -44.4865 | 2026-07-26 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |


[Clique aqui para ver as próximas entradas](README2.md)
