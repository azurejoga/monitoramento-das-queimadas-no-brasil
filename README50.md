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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60690c9e-ce08-3869-b544-2612c4a7b6ba | -16.70183 | -50.41456 | 2025-08-27 04:27:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 276f9381-a312-3343-aa3e-5c3520ea583e | -15.03973 | -48.68074 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 714244e9-55ff-3a96-bf9f-136cd377390a | -16.38426 | -48.81079 | 2025-08-27 04:27:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e428e49-8a06-31c7-a455-9ecdb931bbc4 | -15.10719 | -48.61867 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f64ab327-6df7-389c-bb59-ab42ea923ed3 | -15.61763 | -52.71691 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90f0b8a0-8ef7-323c-82c9-3fd0af1c01d0 | -13.40475 | -46.91634 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3121212-9848-381d-b03f-0d1c95b33998 | -12.76103 | -48.18673 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bcea607-29c4-3f37-bc22-1db8d0d51285 | -16.71785 | -49.42194 | 2025-08-27 04:27:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9f57f39-18d6-3548-abd6-4619440c67dc | -13.35216 | -54.39363 | 2025-08-27 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce8d6c98-ca6e-3111-91c2-93b40416ef17 | -14.30025 | -53.06106 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b5bb781-661b-319f-9569-91f1de42faf1 | -15.03367 | -48.67606 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1de05e2-5c55-3ad7-a57f-cb45da22ea2c | -13.62473 | -48.20166 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3145c70d-3750-37c6-aa0e-7ce853083c7a | -12.40139 | -46.50698 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a71adbd8-db55-39f6-95f8-64574223dac3 | -12.72788 | -48.18126 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 473c9157-4fb0-39d3-bc3d-1726dc6c16b8 | -12.87539 | -48.10756 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5999b83a-ff28-33b3-9311-5903e4874b13 | -18.15158 | -44.42347 | 2025-08-27 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c100f51f-991f-3f4a-957e-0b664c4b2885 | -18.15487 | -44.42859 | 2025-08-27 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12212d76-e179-3936-8662-b81da97130e9 | -12.86988 | -48.09943 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1333157c-04d3-30bc-bcdb-5dedb4d8308c | -15.18496 | -52.32234 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5136c41-c6dc-31b9-99bf-1d915ff6e377 | -14.26518 | -48.0164 | 2025-08-27 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8c80e35-755c-3de7-8bc7-37e41419a72a | -16.74014 | -48.53522 | 2025-08-27 04:27:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3a3941d9-eeb7-33d6-bdc7-c950fa2eed65 | -15.09356 | -48.62021 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66e7d90f-c5aa-3f1f-a02e-d7a9e0735e69 | -14.24309 | -48.02729 | 2025-08-27 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e4aac1e-1207-39ff-9090-d927de944523 | -11.31683 | -55.2108 | 2025-08-27 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88ec0403-8735-3106-b844-86dccb090ae1 | -19.64495 | -43.9871 | 2025-08-27 04:27:00 | NOAA-20 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 372b97c2-cf2d-38ba-8a11-d69444c875df | -15.62887 | -52.73666 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d79675a3-a3a5-3061-8959-f1d5fd306b29 | -15.08856 | -48.63039 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d452367-f67a-33f9-ae99-f52d5127defc | -15.6508 | -52.74589 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f74d438d-dfab-3bf8-84d8-f2f0a0161720 | -15.62387 | -52.72072 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5fab7a2-c3b6-3d6a-a573-f3f60c1b2ba2 | -12.70688 | -48.185 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0506542f-eed1-38c5-98d1-aee28c90de3f | -16.73952 | -47.59525 | 2025-08-27 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8b2f0c2-72c0-356f-a655-bb2fbe289bef | -17.77785 | -44.47754 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 498bff96-96eb-36d0-9c08-69f099ef19f6 | -12.77449 | -48.10187 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4da7715d-7a7f-34ab-b737-1fa5b7ff2103 | -12.73973 | -48.08533 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 842a68ab-2c61-3019-9baa-60c03eaab721 | -19.08109 | -44.32735 | 2025-08-27 04:27:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1773a31-71fa-3925-a1db-b9566d84eb1c | -12.24424 | -45.06184 | 2025-08-27 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8f1170c-3830-37e1-a01b-46c16c5f92fa | -13.4239 | -47.00763 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8080d1ce-8f9d-38b4-b8b3-73893a706740 | -12.68377 | -47.88059 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7e3d520-3c93-3f08-a355-5e7d8cf93742 | -13.84155 | -46.69778 | 2025-08-27 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db5c5ce0-6607-361b-9473-a0a6cebc7429 | -12.77444 | -48.12361 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42728e40-ccb3-35a2-bce1-24352e4aba46 | -11.92693 | -47.59851 | 2025-08-27 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c371aab-ab91-3f19-952e-65b1eb698d14 | -18.21877 | -44.52137 | 2025-08-27 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d85c246f-e4c9-32ff-a77a-bb20783ec54b | -16.76189 | -43.11022 | 2025-08-27 04:27:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdac4294-eddd-382d-8083-fe8582dffa0b | -16.95217 | -49.21372 | 2025-08-27 04:27:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b773da1-ec0a-3a89-888b-83fbc6ed8839 | -13.18266 | -44.04176 | 2025-08-27 04:27:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53b305bf-d616-376d-bd07-4c4a8e66d188 | -12.7436 | -48.08234 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c133109-66bd-382e-a93f-f4f9fc860b1d | -11.02893 | -52.02789 | 2025-08-27 04:27:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c0e0cbd-156e-3be8-b438-a78b2f1e71ff | -11.82102 | -46.79773 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5f5d8c0-786c-3533-b115-9ca33a74f8c8 | -13.60222 | -48.15077 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5a0aec1-48a8-3d75-ba76-1334ae4d7d22 | -12.74416 | -48.07882 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b1efb9b-387c-3973-9a6b-cbb46514a636 | -13.5325 | -46.89573 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 263e970e-f847-330b-9f83-eb7da72c8651 | -13.07005 | -46.92963 | 2025-08-27 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e10ba8bb-54a7-3138-95ec-b6caef14ee8f | -18.72323 | -43.81928 | 2025-08-27 04:27:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 886686be-1c4b-309d-a02c-a2b5408217cc | -17.77399 | -44.47692 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6764273b-3ca6-3a2e-92d2-b03ff0d061b8 | -12.77169 | -48.1195 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01cdd2ce-1f05-3cba-8551-26683d2e9285 | -13.42922 | -46.86079 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69213aaf-e46c-381f-9af9-5efdbc68d3af | -10.76424 | -60.79391 | 2025-08-27 04:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7aaa4bb-ad85-32e6-84de-804e25ba37a9 | -15.60327 | -52.70927 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d37e1ee2-cca9-3d47-825e-08c0b3cddf76 | -15.20985 | -53.79657 | 2025-08-27 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba561cfa-4591-31ea-814e-e8f01a4378bf | -15.09267 | -48.56151 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6be92f59-1ed7-3047-9fe1-9341c163f541 | -12.93105 | -46.33167 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 697aea3e-2017-3d5f-8a2b-83f2a1710b43 | -18.07984 | -44.05983 | 2025-08-27 04:27:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaf6b64e-d5dd-30ea-8438-79c8a85b9b17 | -15.62418 | -52.74088 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43a1eed9-8cc5-3a24-a130-1f4f876473ac | -14.36873 | -53.35591 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bc7f86e-6aa0-38ac-b0c4-63959d1815df | -15.53504 | -54.74437 | 2025-08-27 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c376ce3-56a5-3c3d-9f4b-604ece4a40f8 | -15.11352 | -48.5575 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9cec71e-7417-3f8f-903a-80e642f666d4 | -12.73451 | -48.18237 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 390c55b4-bd9d-3700-8fcd-739edf8a0ecf | -13.40143 | -46.91574 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceca0699-67a4-36d5-8912-417840ee2be3 | -11.31587 | -55.21605 | 2025-08-27 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 162a7a7d-c8d4-3e73-8522-e102be05e1f6 | -13.06127 | -46.30337 | 2025-08-27 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4965eabe-e1b0-34ae-96aa-aa0220048ff3 | -14.48553 | -52.05249 | 2025-08-27 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fed6048b-e96e-3b73-85f1-10c3bd480f0f | -12.79529 | -48.11972 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 803cf502-9905-31b3-89f6-a122a9f3e05d | -12.74002 | -48.19054 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98ad4ea9-4332-3567-abe7-bdfa34d55ee9 | -17.7766 | -44.47496 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c6537ae-5e26-39c7-bd12-b7f17d7b004e | -14.30229 | -60.36378 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b09e05c7-a03e-3b06-bb8d-fe449871d01b | -13.40863 | -46.91336 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ab5351f-7dc6-3841-9292-d90d1e57ad2a | -12.72845 | -48.17771 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bdb93af-df98-38aa-9e5d-63bc3d311c67 | -13.40532 | -46.9127 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9321f3d-8aa2-316e-bea3-4d3f628d293f | -18.27526 | -42.12757 | 2025-08-27 04:27:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fa808d64-bcf8-3b20-a5d9-d5d2fb8c3b9a | -14.24324 | -53.31028 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1322e87e-3e35-30c3-a826-d0855edcef3c | -11.89305 | -47.14262 | 2025-08-27 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cbe69fd4-c6b2-3b8b-9427-43940f6bc319 | -15.09025 | -48.61965 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eca74ad1-ca15-3103-86e1-b78128d31e94 | -13.6674 | -46.90202 | 2025-08-27 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46dec287-7c30-3489-986c-36c2953b4e50 | -13.17427 | -45.29367 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 393fab6d-4e66-3be4-b507-911f97dd0c01 | -12.57324 | -43.78888 | 2025-08-27 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7cbb3fc-b886-3e9c-924a-1fc056950c62 | -12.74803 | -48.07585 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f3c6b3e-cc97-3f20-b3d7-407a4f084f0c | -12.74552 | -48.19869 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc913b92-3056-3870-965d-e75cf82ebc36 | -13.61312 | -48.21067 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0d5ef51-187f-3776-8b66-791e3dfb7a91 | -12.78803 | -48.14394 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 496541d5-a525-3179-bf51-15db0641ffce | -12.65568 | -47.84345 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46760eb1-6b69-33f4-83bc-dd24f999750e | -18.49023 | -47.23349 | 2025-08-27 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ea5314a-e21a-33ea-878c-73974a934bbb | -17.80894 | -44.51007 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e504c2c-b5e2-3c66-8499-a00a5f028a1b | -13.38697 | -46.92068 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8259ca97-e6fe-3d08-ab30-11a68fc2c80c | -12.49524 | -47.24221 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9773d2f-8856-3bee-afcc-ab0f831595a2 | -13.22396 | -44.54585 | 2025-08-27 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9aecc4a-7f0d-3a18-9e4a-b0cacf5c2116 | -13.49446 | -46.8601 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 229aed38-e25e-34bb-9d5a-59e78bf13cd8 | -15.7544 | -50.41138 | 2025-08-27 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16949f07-97e8-3aac-8dfd-9d9ea7ffd7d5 | -16.70586 | -50.41136 | 2025-08-27 04:27:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1c1d8e26-2041-3173-b542-c1fd8d5ad555 | -13.06918 | -46.32661 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7ea5df1d-7f7d-347e-b9b9-353b78e43951 | -16.73739 | -48.53107 | 2025-08-27 04:27:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README51.md)
