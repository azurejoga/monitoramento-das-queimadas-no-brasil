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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e3b0e7a-5bb5-3d34-86be-dda54ed31ac9 | -9.8932 | -48.456699 | 2026-09-22 01:19:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 956596ff-8ae6-3c4b-abb3-b19a235f6a62 | -3.7618 | -59.480202 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf8fb1d2-bbb8-3230-bf63-d786585ed3f3 | -12.8472 | -54.040699 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4ec181-eea9-35e8-a980-07b4d6278fc3 | -11.3302 | -51.3633 | 2026-09-22 01:19:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eac85800-7e6c-36e4-b046-62b6764a06d1 | -6.4335 | -55.6143 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22f53140-df8c-3997-a28e-70f87be91403 | -6.121 | -57.764999 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64b149e0-4fff-3123-aa83-a0a181048403 | -11.4133 | -47.3456 | 2026-09-22 01:19:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd4d3fd2-26cf-34f0-bf73-b2dbd94a4451 | -8.6268 | -54.632099 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e32a9a4f-2b04-3392-bae0-0751c3de37d2 | -10.4265 | -50.364601 | 2026-09-22 01:19:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea23c574-8e73-3616-9ece-cfded3e136c1 | -3.3803 | -56.939201 | 2026-09-22 01:19:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31274694-bd8e-3a57-a7a5-e998ca80283f | -3.7083 | -60.552399 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 156bcbb3-99a8-3960-8479-c231c0bb78a7 | -6.9203 | -59.6306 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57f51c15-6e47-3548-8286-c707b10e6703 | -6.143 | -59.928799 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab77bfa8-3bbf-3886-8487-00a2682a41e1 | -2.9294 | -57.7962 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60756735-036b-3480-8376-6f7c53b045ec | -3.6919 | -60.570801 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df0cd37d-3b63-3425-b43c-4fcfe02d4207 | -3.6851 | -60.631001 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca1ddb8b-dbe5-3720-ab4b-d6f4426855d6 | -11.7635 | -50.826401 | 2026-09-22 01:19:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dcab0f37-1c41-3e3b-b92f-12cd9aa45245 | -5.8139 | -57.7309 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a85ac65-34fa-3461-a7f0-a407038a94d4 | -8.1857 | -54.7747 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e24fff5b-fdaf-348f-acdb-36dc5cec5168 | -3.3327 | -59.812698 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30172ed2-ea90-37b5-b2e0-e079f06496e9 | -3.7197 | -60.557201 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba6fd797-ab3a-3319-a051-aed9fb3178d6 | -10.4402 | -50.377499 | 2026-09-22 01:19:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08586066-628a-3a09-bafc-fb40ca52703b | -3.4835 | -59.571201 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4fe677c-0d7a-3dca-88cc-81bcff1db5b6 | -6.3436 | -59.9501 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7322e1b-a081-30b6-ae22-2ba085b484a8 | -6.311 | -59.9426 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3a70b55-a1bc-3ee1-8751-13d956d3e830 | -6.3625 | -58.274502 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f64c7a90-c847-3ae1-9b16-9f14323fbff8 | -6.8386 | -55.5373 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb84f18-5b70-34ca-acff-2a99335d7034 | -5.8253 | -57.735802 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1890c77-e6d8-3e97-94af-a9f8ae083fea | -6.8142 | -59.436001 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1a94444-317c-3b4c-b0ca-bc811a1a7d1c | -4.2941 | -56.258099 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f888c71-ef0b-3b6a-95d9-f2ac87bf809d | -8.1529 | -54.810398 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03685295-5653-30e3-810c-8c563193d9eb | -3.2245 | -61.051601 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0c9225e-d6c7-33ca-93ea-cedd22ad91bd | -3.1477 | -61.392601 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f78fe49-a321-331b-921a-aa8bf2d04d1d | -3.228 | -53.965099 | 2026-09-22 01:19:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4623edcf-f78b-3804-85d0-a7a98677acb7 | -3.2225 | -53.942001 | 2026-09-22 01:19:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43e88bc0-3055-3a59-95c2-6777b3018b11 | -6.3057 | -60.009998 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 295cff77-b2ab-3703-b1f2-32cf187288a2 | -9.681 | -54.3316 | 2026-09-22 01:19:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0259bea4-9b31-38a9-8af6-c789e25144e5 | -3.3452 | -59.867298 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a8f9eab-76c1-3c38-9a63-6ef9e4f45319 | -7.3172 | -54.943199 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af37522b-5d1b-35cc-9241-1b3ab8754ff0 | -11.257 | -54.137001 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f830808-ecc3-3c3d-b048-c49ae30c956a | -4.0875 | -62.083698 | 2026-09-22 01:19:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46d6229c-04b4-3231-92c8-9ef050f5a87d | -8.259 | -55.2561 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb1feb1-7071-3ecc-af4d-c5de8080fb21 | -4.6836 | -55.6329 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2e0103e-3db4-369f-a3fa-c7d7237ed466 | -9.8764 | -55.7187 | 2026-09-22 01:19:00 | METOP-C | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f916a496-1cb6-38cf-9786-8d4f60e5f80e | -2.8638 | -60.916901 | 2026-09-22 01:19:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48f8b1a0-fa24-3604-bc8f-ee495d9f0704 | -3.4521 | -50.614899 | 2026-09-22 01:19:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5568c12b-344c-31a5-853e-4ba54e417d22 | -8.4921 | -57.620701 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77ec47c1-d9da-3375-95a2-baf8e3149b3e | -7.3259 | -55.5895 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47f24677-26ac-35e3-b6b8-d60f1a590dc7 | -11.7732 | -50.823898 | 2026-09-22 01:19:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79bee0ee-e090-3663-90cb-a158fd2ce994 | -5.8707 | -53.6423 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81b7e49d-2e3f-3827-9e13-cd049dd55d3f | -2.9277 | -57.788898 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f141cb3e-e4f3-36c3-b6f3-2da8d06dc755 | -5.4148 | -60.216099 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa6b782d-1af3-36fd-87b4-d24c93bfd33d | -1.6128 | -54.622002 | 2026-09-22 01:19:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7d2408-8125-3d35-9e70-04168d714bff | -12.8061 | -54.041801 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 048402ee-e6f9-3867-ac43-bbd4d6932760 | -4.4246 | -55.496899 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c84117a-1067-3a53-a3dc-aa3fa144d541 | -6.4218 | -59.9767 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf92c34e-6236-35fd-9cc3-f426da3cfcd2 | -7.7155 | -61.244099 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b27ff792-11b1-31ec-add4-3a7c630d7a47 | -3.6885 | -60.600899 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c152a05-0c88-35e9-b5d3-b7b060945095 | -16.851601 | -56.789299 | 2026-09-22 01:19:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2bb3b783-c3c1-3f92-bebb-f61154cc3d51 | -6.1161 | -57.7439 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5fc47de-03d9-3b39-ad7c-ed391e150db5 | -6.072 | -57.731602 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29bd454a-5657-3288-a327-dceb4a048464 | -6.2811 | -57.743301 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9769f25a-603c-3aa3-a9f0-b0b3735f2b94 | -8.1508 | -54.801601 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a06e046b-006e-31cc-bad4-0164a9495514 | -4.2096 | -59.903801 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fed9b6a3-3f6e-3000-bb94-bdd996af2193 | -7.5745 | -57.669201 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 676b8a35-9a4a-3982-8106-33bde23ad29f | -6.054 | -57.8321 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 466fab5b-4bdb-363a-b058-c715f5820a53 | 1.7699 | -60.2313 | 2026-09-22 01:19:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 30d9dafb-5bbc-37f2-be28-2a9a443c3d6a | -3.6102 | -60.574299 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60b0aaa2-8598-3e5e-8031-1ede790419b5 | -7.7253 | -61.242001 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e07cf3a1-ae91-3d2b-9d3c-cd1e3061b78e | -3.2867 | -57.8685 | 2026-09-22 01:19:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d3228a6-074a-38be-8078-193e21180a2f | -6.201 | -57.7542 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4714684d-e84c-396d-b12b-32675b91e77a | -10.2181 | -53.901299 | 2026-09-22 01:19:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a81340c1-4c9a-342c-af33-7a737b59e02c | -3.5974 | -59.438202 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5746d9d-0b2a-3024-be94-60e92526c0cd | -6.3122 | -57.743698 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd7d58e1-18bd-36a4-91a1-fddea7773e63 | -17.6199 | -46.6772 | 2026-09-22 01:19:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 86cc75fb-ba90-382f-95e4-55337f21f589 | -8.3042 | -50.375599 | 2026-09-22 01:19:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64e17f08-564a-3a43-bec2-4e2f4eecad82 | -4.8581 | -56.0238 | 2026-09-22 01:19:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f1dee31-e359-3395-9573-809a3bc18575 | -4.2644 | -55.429401 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09f3124b-91d6-373b-8b1c-5946a04adf6e | -10.906 | -53.967098 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e498b6c-3f6f-380e-b92d-269e94ec5f8b | -6.0298 | -55.347698 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 711bb5c0-8b54-3913-970e-981c1b288380 | -11.4197 | -47.3694 | 2026-09-22 01:19:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12404d5f-3c95-34ce-b2bd-d2d9c19bffac | -12.7964 | -54.044201 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28a0350a-02c0-31d1-914c-3c37f758e2b1 | -6.8346 | -58.983299 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae2be0a2-e334-3f75-aec9-124f09894fe9 | -8.2629 | -55.2728 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbf808b0-c4a1-37b6-9aaa-5fecfbd0c4cb | -6.4414 | -59.972401 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1673b747-a403-3530-9da7-06a207bcbe64 | -7.4049 | -55.2258 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31479a38-dfb0-3f44-80cc-c5d366acfd14 | -17.6238 | -46.653702 | 2026-09-22 01:19:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4797a936-d6d5-3ea2-92c7-3d8527456595 | -3.383 | -61.294701 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebed27c1-e718-3a8a-ab71-017316fcfab6 | -9.2945 | -58.9217 | 2026-09-22 01:19:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7544a22e-5916-31ca-a3eb-5677ba0ef9e4 | -1.9409 | -56.6031 | 2026-09-22 01:19:00 | METOP-C | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 454634fe-7379-3de2-8852-946b08d86ba1 | -7.2339 | -55.5937 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49a2d760-c293-314b-b0fc-8fad27e42e82 | -6.6442 | -59.9123 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 369d3a7e-7e7f-3c9c-9dec-607407df8a9b | -6.7056 | -59.005199 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50a5e47f-a194-3329-9651-a03b4457fa2d | -7.5892 | -57.688 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f9f3b7-3050-3d85-bb6a-be9897a6131e | -7.7271 | -61.249901 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9168591b-bf4d-3772-90a8-fcfe53c09b94 | -6.7161 | -59.458 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df9355dc-b743-3ec3-8b58-94bc0379ae40 | -6.6962 | -59.959801 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 764ee196-9db5-3381-85bb-adb1c9ae7bd0 | -8.2472 | -55.250099 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41089158-5791-3e8a-8915-30a14e4924e6 | -5.9355 | -59.9678 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6370bf0a-c2d0-33ae-8a12-20ce008ba7a5 | -17.614201 | -46.656502 | 2026-09-22 01:19:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README20.md)
