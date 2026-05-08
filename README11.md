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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0866bd3c-1380-33e6-be95-20623a9ed577 | -8.6933 | -49.0833 | 2026-05-08 13:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| ec45b9ef-e70f-34c1-9fa1-3774ed414982 | -9.4468 | -46.1211 | 2026-05-08 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| ca944887-cec9-3dc3-ae19-863b49d51fe6 | -8.6933 | -49.0833 | 2026-05-08 13:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 8e8a4ef2-4903-3bb1-811d-702fa48a2546 | -8.6936 | -49.0618 | 2026-05-08 13:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 00e2c001-1047-3c2c-8f71-a979c6ccb412 | -9.4468 | -46.1211 | 2026-05-08 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 14bac545-3a10-3730-90aa-0ef35341467d | -14.0118 | -56.6215 | 2026-05-08 13:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 88a0093d-f942-3153-bc04-e713c9e5e104 | -14.0118 | -56.6215 | 2026-05-08 13:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b159be7b-de1d-3d8a-86ad-57946e4d5a3c | -8.6933 | -49.0833 | 2026-05-08 13:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a3fc17c5-8f66-3916-b3a3-0bd47bf2c10f | -9.4468 | -46.1211 | 2026-05-08 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 205d8016-e0e4-3294-8c5a-a1e250168219 | -8.6936 | -49.0618 | 2026-05-08 13:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 4e7f0e9a-f58c-3868-b58b-084cb5e99645 | -14.1926 | -57.4318 | 2026-05-08 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 145882a4-be2f-3853-a7ef-2f457da41a27 | -8.6936 | -49.0618 | 2026-05-08 13:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 5f30090f-559d-3f8d-ae60-89beec96553e | -8.6933 | -49.0833 | 2026-05-08 13:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| dad6056f-273b-3064-8f8b-ac650f647d18 | -14.1929 | -57.4116 | 2026-05-08 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 09c831c4-12e8-3f63-bbaf-97e04528af9d | -9.4468 | -46.1211 | 2026-05-08 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| cc8876bf-de10-3911-9d30-1c366e95619d | -14.0115 | -56.6418 | 2026-05-08 13:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 141d85a8-c148-3220-a650-6f839b7ecb52 | -9.4468 | -46.1211 | 2026-05-08 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d3aebdc7-9cce-39b0-afa0-8cfe50058e8a | -13.9924 | -56.6437 | 2026-05-08 13:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d5b67307-6648-373f-ba82-646a4edef3bc | -13.9926 | -56.6234 | 2026-05-08 13:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| bde70f7d-9242-33ed-a9fd-8c25a6ac55a9 | -14.0118 | -56.6215 | 2026-05-08 13:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 6558eccc-a881-31be-bb63-49decf28fac7 | -14.1926 | -57.4318 | 2026-05-08 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f5834d35-0e46-3f20-8868-2fe7e95eb179 | -14.1929 | -57.4116 | 2026-05-08 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 65bd512f-b3f8-3a7d-95e9-20b515595ca8 | -9.4468 | -46.1211 | 2026-05-08 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 48be497f-ac4b-3795-bcb0-8c13953f750a | -14.0118 | -56.6215 | 2026-05-08 14:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 170.8 |
| fc8d556b-d83f-323a-9080-d92dadda3bda | -10.6835 | -49.6818 | 2026-05-08 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 914dd6d0-2205-3747-957b-a1c338f95d1b | -14.0115 | -56.6418 | 2026-05-08 14:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 930e5fa3-14ab-3da0-b669-c364735c1ae7 | -10.3517 | -46.4201 | 2026-05-08 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 441eb846-b5c8-3b0e-b844-a00bcf1ca7a2 | -13.9924 | -56.6437 | 2026-05-08 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 17fece4c-2087-3f81-8285-51e675e42b3b | -14.1929 | -57.4116 | 2026-05-08 14:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 4f2dd231-bf62-39d9-aac9-bd878dcb6b5c | -14.0115 | -56.6418 | 2026-05-08 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 31454c39-811d-3760-ac0d-2f2fbf9e981c | -13.9926 | -56.6234 | 2026-05-08 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 031fdc10-01df-340d-9f50-72f9580c5ceb | -9.4468 | -46.1211 | 2026-05-08 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 40f109d5-329b-33bc-b98d-6458535af5fc | -14.0118 | -56.6215 | 2026-05-08 14:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 2bdfbb8e-af11-34be-8d6d-408a4e4467ec | -9.4468 | -46.1211 | 2026-05-08 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| fcd01739-716b-347d-9254-1d2ed8b91e67 | -8.6936 | -49.0618 | 2026-05-08 14:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| c325cddc-b9b8-3f7f-848a-02de818955e3 | -13.9926 | -56.6234 | 2026-05-08 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| e12bddcc-8c08-34a6-86e4-e870ddff9306 | -14.0115 | -56.6418 | 2026-05-08 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 4d68ac9f-d6ae-309a-8427-5aa0785f5b72 | -13.9924 | -56.6437 | 2026-05-08 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| aefaef53-bb2f-3596-b94f-215fd731c65f | -9.4071 | -50.6847 | 2026-05-08 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 36c3b272-aa32-3a0f-9cd9-1ac9fee3b072 | -14.0118 | -56.6215 | 2026-05-08 14:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 6ee41389-c4d2-352e-9344-c9bcf6921fe8 | -14.0118 | -56.6215 | 2026-05-08 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 244.8 |
| 38a6f56c-eddb-36f8-8c0b-f0399940ea39 | -17.9475 | -52.9524 | 2026-05-08 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| c5fb1802-3b0e-36e6-9382-fe283008a8c0 | -12.3508 | -50.0266 | 2026-05-08 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| b4802c95-5224-3f94-9719-5bc0431ade8c | -14.0115 | -56.6418 | 2026-05-08 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 1af5c723-0fb1-3705-a7a2-8ae2335124fc | -9.4468 | -46.1211 | 2026-05-08 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ff0a4e50-7277-31a9-8a75-3045b9cf4ab6 | -13.9926 | -56.6234 | 2026-05-08 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 588b9cc8-12f3-3ab5-868d-66b3e61e3eaf | -13.9924 | -56.6437 | 2026-05-08 14:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 91ebd962-3871-3cc0-9552-4bbef490b5d6 | -9.4468 | -46.1211 | 2026-05-08 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| f5aee892-0b5a-3c60-b918-b2ef1474c409 | -10.893 | -49.5941 | 2026-05-08 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 1f3465bd-af36-3b7d-b2ce-29ca9ed4fc60 | -13.9926 | -56.6234 | 2026-05-08 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| bfbeca9c-6728-3725-bf7f-ed64312894aa | -14.0118 | -56.6215 | 2026-05-08 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 280.4 |
| 32c3fb99-5d15-3da5-9355-7564335ce346 | -14.0115 | -56.6418 | 2026-05-08 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| e0476c37-687d-31dc-b157-94b187b85a5e | -8.6936 | -49.0618 | 2026-05-08 14:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 7bc1c408-2bda-389f-a928-febaa948c38c | -8.6933 | -49.0833 | 2026-05-08 14:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| f9376e32-0289-34b5-8c25-ce2c52f0c353 | -17.9475 | -52.9524 | 2026-05-08 14:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| f83d13fd-c908-30e9-bbf8-5bbcf566241d | -13.9924 | -56.6437 | 2026-05-08 14:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e43c4e62-feab-3464-a2d4-bd2f053631a7 | -13.9924 | -56.6437 | 2026-05-08 14:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| bbc2318c-19ec-32eb-b955-4d79f16e1301 | -14.0118 | -56.6215 | 2026-05-08 14:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 268.5 |
| 235acd1f-072c-3b35-ab86-0c9bbc85c765 | -8.6933 | -49.0833 | 2026-05-08 14:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 58ff8b80-4ce0-37b7-8f4e-5b05e15273a8 | -9.4468 | -46.1211 | 2026-05-08 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 38ac5e2f-8c5f-3e74-a2f0-9b44e02b7095 | -13.9926 | -56.6234 | 2026-05-08 14:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| b3c59c61-860b-3562-a278-4ec675d10f6e | -8.6936 | -49.0618 | 2026-05-08 14:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 95515b4a-fa54-307d-9e23-ab57126a674e | -12.3508 | -50.0266 | 2026-05-08 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| e35cc1f6-3218-3dbd-a168-786a80b6cd85 | -11.9366 | -49.6885 | 2026-05-08 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ef387cbe-3c86-3cdc-84b3-ba28d9956422 | -9.4468 | -46.1211 | 2026-05-08 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 144ecede-9936-3d60-b38f-198cfbe81099 | -12.3508 | -50.0266 | 2026-05-08 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d271cb68-9d23-36b7-98d2-860696611729 | -8.6933 | -49.0833 | 2026-05-08 15:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 428e856a-197f-3f5f-916b-38efcf7f5062 | -14.0118 | -56.6215 | 2026-05-08 15:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 246.1 |
| f8b13c2d-5fce-3a1e-b689-2f7414f7cc8f | -8.6933 | -49.0833 | 2026-05-08 15:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 578c46d3-87c0-3395-892b-3fe28556ace0 | -14.0118 | -56.6215 | 2026-05-08 15:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 276.4 |
| 76b108a8-4af9-30d6-ba5c-b45276af3888 | -12.3508 | -50.0266 | 2026-05-08 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9ece0ff2-d44e-3aaf-97c3-f18fc13d2d06 | -9.4468 | -46.1211 | 2026-05-08 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| fc9a8b3f-bf85-32bc-93f2-8e1f1f76b803 | -8.6933 | -49.0833 | 2026-05-08 15:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 83e7c90f-5156-39be-88c0-76337f51f94d | -17.9475 | -52.9524 | 2026-05-08 15:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 29aa039c-b45b-362c-a2ac-746539c1f6c0 | -9.4468 | -46.1211 | 2026-05-08 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 4eade128-1270-3f7d-98cc-d283468791a4 | -8.6933 | -49.0833 | 2026-05-08 15:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 26191a3d-0384-3748-8710-2fdb343ae8c9 | -9.4468 | -46.1211 | 2026-05-08 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |


