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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 721e7319-b882-3b5e-aab9-e164c0172aa2 | -6.7839 | -62.9782 | 2026-09-16 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 68b7826d-04c7-3d00-80f0-f24b6928dcea | -13.3062 | -51.2808 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| d7801acd-5047-342f-abef-76d797b54a13 | -7.4784 | -42.1179 | 2026-09-16 14:40:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 153.6 |
| ff95de11-328d-3b54-b65d-264f64f8f85f | -6.7498 | -58.8236 | 2026-09-16 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8fbd662a-6853-3422-9896-9178b95a5ccc | -12.126 | -44.2225 | 2026-09-16 14:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 61cbf1db-ebe2-3570-9e65-225fa73de74e | -10.0295 | -52.0991 | 2026-09-16 14:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 04f538d1-d73e-311b-95c0-1b77fb4f525c | -6.1609 | -52.7496 | 2026-09-16 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| bead449d-db14-36e2-91dd-bb3fbf80d295 | -6.2731 | -55.2904 | 2026-09-16 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e8a6fe05-cd41-3899-a0f1-a61e3ec253a1 | -9.7322 | -64.9067 | 2026-09-16 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 2ad52173-ce2d-3542-9ca9-d34ac2a835a6 | -13.3199 | -51.62 | 2026-09-16 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 4cd406db-1b8b-318e-a48c-45283aadeb40 | -5.3646 | -56.0249 | 2026-09-16 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8fd00d21-a0d6-3d2b-9ae8-01d26e6110c9 | -10.9108 | -48.3739 | 2026-09-16 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| fac3c1fc-69e2-3b65-9604-58703b40fc82 | -9.1337 | -65.844 | 2026-09-16 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| bbd11ad7-d6df-32d6-8d51-71025f8f9443 | -13.3387 | -51.6389 | 2026-09-16 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 85b4cdec-e74f-3d55-b3d3-e4124c45715e | -11.4167 | -51.4371 | 2026-09-16 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 58e2b656-db70-3ff3-9417-5b7bbfadd32c | -15.3602 | -52.9678 | 2026-09-16 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 7c472d63-dc74-3e66-a280-bcde1e161bc6 | -5.1624 | -55.9338 | 2026-09-16 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 185b0a77-beba-382e-86bf-158f96ff63d1 | -11.9906 | -52.4695 | 2026-09-16 14:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 38671723-63eb-3dca-989d-79c313220f0f | 3.859 | -60.6561 | 2026-09-16 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 39c8c132-054d-3243-b2f9-ec43f1ac0afe | -13.3946 | -51.7382 | 2026-09-16 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 9b7d49b2-b2fa-3d9b-82a9-794d8c6ef42a | -6.602 | -58.8684 | 2026-09-16 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 152241ab-a9c7-35fa-9713-b3c677e8fcfc | -7.4784 | -42.1179 | 2026-09-16 14:50:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 140.7 |
| 36dc835e-f896-34ff-bfb1-f52b9851d0dc | -10.2206 | -50.373 | 2026-09-16 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 237d0e54-bdbd-3683-842b-c8a94fd90f38 | -6.583 | -58.9658 | 2026-09-16 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 20873846-8639-3bf3-a5e2-98b248588eb5 | -10.9105 | -54.025 | 2026-09-16 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 27caa63d-761c-3b27-b5c1-d0cd0ddccc27 | -7.0428 | -59.2173 | 2026-09-16 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 31bccad1-ca0a-36ed-a3da-b595275a3146 | -13.3761 | -51.698 | 2026-09-16 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5477ec5c-1a69-36cb-b386-445c7e5ef194 | -6.1362 | -59.8871 | 2026-09-16 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c055131b-a438-3d48-8e8b-050d3f45af99 | -6.2916 | -55.2895 | 2026-09-16 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 5fa62053-5f95-3762-95c4-88916449d606 | -13.3754 | -51.7406 | 2026-09-16 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1f84a706-89eb-39f0-a414-ec1cdea282fc | -12.1453 | -44.2195 | 2026-09-16 14:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| dd66b389-b1ca-3490-8079-001cbd182b8b | 0.1931 | -51.5011 | 2026-09-16 14:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a51ce8bd-cb33-3e33-aa03-7db97c189253 | -9.3765 | -50.0925 | 2026-09-16 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| a17b1e62-ab72-3c52-bde3-d6e062cb0b4c | -8.7949 | -46.9069 | 2026-09-16 14:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 02bf8923-62ea-3b96-b4a8-75c91e618805 | -13.6337 | -45.9732 | 2026-09-16 14:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 4266fc05-77ab-3f12-a03b-daed5ef88435 | -10.6641 | -54.1491 | 2026-09-16 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 41b61f8d-8b39-3568-abd2-2a36c212f297 | -10.301 | -50.0016 | 2026-09-16 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 895e7a63-a420-3e3e-ae90-11c10bfce08e | -6.1178 | -59.8877 | 2026-09-16 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 335c1db1-f10d-388c-beef-e39fd6bde538 | -6.7648 | -59.4408 | 2026-09-16 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ee5c922d-227d-3eed-88b2-3636c237511d | -13.5127 | -51.5532 | 2026-09-16 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5d45a417-4250-311e-a48a-8e7f58b308bd | -10.6827 | -54.1679 | 2026-09-16 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f81460b1-357b-39b6-850c-4c1e108c61b9 | -6.7684 | -58.8035 | 2026-09-16 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c9f68ae7-b914-3f18-a973-37afc4f42646 | -9.3707 | -60.3032 | 2026-09-16 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 94d1cdbe-0d6e-3bdb-996c-ff3ce45a0aab | -15.6557 | -52.7366 | 2026-09-16 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| e4128e52-72c2-31f6-b2bb-ea80be518391 | -10.4772 | -50.9634 | 2026-09-16 14:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 51d988cf-3b74-306d-85b2-68b0d8ef1c6c | -6.0993 | -59.9076 | 2026-09-16 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6f8de681-a658-3976-94af-6dd318dbd21d | -9.0962 | -65.9384 | 2026-09-16 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 64d6ff07-2deb-320b-84eb-9fcb527cca89 | -9.0866 | -61.0287 | 2026-09-16 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d6bc3930-fd3b-328e-9671-1c3202c63319 | -7.3561 | -44.4956 | 2026-09-16 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 76f1f51e-84e2-31c6-81c7-de515c4939fb | -9.3569 | -50.1583 | 2026-09-16 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 33a0a842-3b9f-325a-83b2-7b5abf87e8be | -9.3577 | -50.0943 | 2026-09-16 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 93f36cd0-8ef1-3c54-9d07-30f174918d68 | -7.0613 | -59.2165 | 2026-09-16 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| de17be1b-9c32-3109-ac96-77175beaf415 | -11.3834 | -43.9378 | 2026-09-16 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| e2508fc3-1259-3fa9-9fcf-b191d2c200f6 | -8.5428 | -44.5132 | 2026-09-16 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 345.3 |
| 6e871700-0ae9-3583-98c4-bdf7dcc55c2e | -6.7683 | -58.8228 | 2026-09-16 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| fad61bb7-2579-315f-83eb-3d6d7ffbe526 | -9.8508 | -48.3615 | 2026-09-16 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a5eb03fe-8ea2-382d-9e26-13030efd5609 | -9.3892 | -60.3215 | 2026-09-16 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d9e0797d-c889-3be5-9f7c-ac9fd84b1ec2 | -8.6184 | -44.5049 | 2026-09-16 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 254.0 |
| 661b5a10-be96-30d8-b91f-7147d5cd2f97 | -6.5837 | -58.8498 | 2026-09-16 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 9c587fb2-745e-3b89-8462-8d380b9e4f7a | -10.9595 | -50.2529 | 2026-09-16 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| d926bca6-f2ef-3695-8130-ae12b88dceaf | -13.3391 | -51.6176 | 2026-09-16 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| bf40f48e-601e-3263-a232-31d27400877d | -11.6243 | -50.1998 | 2026-09-16 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 539da76a-8e5d-3fe0-b8df-5536e972a627 | -9.7608 | -60.4561 | 2026-09-16 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 51f51fab-7694-375c-9ea8-b8e439c9524e | -3.4462 | -57.9812 | 2026-09-16 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 2343c9cd-a2bc-3f2c-bb53-12c6ba0623cb | -11.2115 | -54.1003 | 2026-09-16 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 7b45dfe0-f3b3-32c8-8048-41ee3d079b5c | -13.3758 | -51.7193 | 2026-09-16 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 4134b691-bd2c-3f81-9019-43b2c0fd3b6d | -6.3197 | -59.9764 | 2026-09-16 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3c9c8ed3-b916-382c-bc6c-e3102447c54e | -2.1051 | -52.0575 | 2026-09-16 14:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| d1f19d8c-1d39-3ece-b09b-08198f5a5c8e | -3.7462 | -61.7552 | 2026-09-16 14:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 901175f3-4eae-3625-af55-fae15db23ac8 | -6.7832 | -59.4401 | 2026-09-16 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4e2246bb-e06b-3070-adbe-027298f37f3b | -8.8915 | -41.2524 | 2026-09-16 14:50:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 115.3 |
| 9524058b-f4f5-3387-bde0-324200e3d495 | -1.6206 | -55.5679 | 2026-09-16 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 3daf2948-4671-302e-8097-544958d8c440 | -13.395 | -51.7169 | 2026-09-16 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d7141616-2fb7-31af-ab3f-94598ef4094f | -6.6021 | -58.849 | 2026-09-16 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f508bd6f-ae1e-3922-abaa-81e012636b73 | -3.4645 | -58.0001 | 2026-09-16 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f0a253d7-94ab-3c33-86f4-8bda6309dd31 | -4.5021 | -55.4621 | 2026-09-16 14:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7a8cbeac-cde5-3465-9bee-7eb2fb6b20f3 | -6.5836 | -58.8691 | 2026-09-16 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1eab272c-a8e9-392f-8130-fca2d338b17f | -5.1255 | -55.955 | 2026-09-16 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| c97d6a71-1e62-3298-b0cd-35cec3452dfd | -9.3954 | -50.0908 | 2026-09-16 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| aee7c2ef-eabf-3e8f-9419-903f57eff7bc | -13.2993 | -51.7075 | 2026-09-16 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 5e1a0b20-db56-3b48-a29b-12d47f9c23a4 | -15.3804 | -52.9227 | 2026-09-16 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 86ebb278-996a-338f-8124-55a69ac3eb33 | -6.7839 | -62.9782 | 2026-09-16 14:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 90a3ed46-958d-3764-8786-a463a0eb05fa | -12.6821 | -54.7174 | 2026-09-16 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 24a7a6da-d8c2-3863-9194-e3504766095b | -11.5432 | -46.8745 | 2026-09-16 14:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 642b013d-8446-369d-a2a4-fb9600175fa6 | -11.1925 | -42.8305 | 2026-09-16 14:50:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 188.6 |
| f10ae9e0-7b9f-3586-9f92-fb0b97ccf0db | -10.8571 | -50.8183 | 2026-09-16 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 8796cc88-6185-3494-b347-a0a14977dfe1 | -5.144 | -55.9345 | 2026-09-16 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 416fc067-69ca-3dba-9212-65980bdc74ca | -11.2578 | -43.4621 | 2026-09-16 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 410.8 |
| e5d58678-1332-3354-bb9a-3c0a6ecf0829 | -6.8032 | -59.1693 | 2026-09-16 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 395.3 |
| 0af6d849-9923-3949-894c-ce139e967807 | -9.3893 | -60.3022 | 2026-09-16 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 648d4163-3d4d-363e-a614-f2414c9d52aa | -6.75 | -58.8043 | 2026-09-16 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| cc761d91-592f-3345-9613-746674e9ded2 | -11.2574 | -43.4858 | 2026-09-16 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 350.5 |
| 3c89ebab-5568-38c7-b8e7-29c47c4cc04d | -12.6826 | -54.6763 | 2026-09-16 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3e4849db-6644-30a1-b059-a248e4a592fd | -10.331 | -45.2883 | 2026-09-16 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 4cea27c6-718b-3779-b05e-e6b20b714ecc | -11.3642 | -43.9407 | 2026-09-16 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| fc834c82-f1f7-3379-9679-ce6d19537b6d | -11.2386 | -43.465 | 2026-09-16 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 310.8 |
| 31f3b1c4-fbbe-3c5f-9fcc-4768df0f68f6 | -9.376 | -50.1352 | 2026-09-16 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 62bafac0-fb55-3d3c-a0d7-3dc72e09b8e8 | -11.9734 | -49.7705 | 2026-09-16 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 0b984849-d39a-3b0e-bae7-acbbec6cdea8 | -8.8456 | -45.8939 | 2026-09-16 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 211.7 |
| 220f42b1-d83c-3d33-b0f8-8208ca49ef84 | -2.7149 | -57.608 | 2026-09-16 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |


[Clique aqui para ver as próximas entradas](README79.md)
