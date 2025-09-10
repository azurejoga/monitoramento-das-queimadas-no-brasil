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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c097c4a-5f5e-38a1-9b54-5e3f13ef9c66 | -19.6476 | -45.0374 | 2025-09-10 02:10:00 | GOES-19 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 40a7aebf-0d4d-3a81-abe7-411576616c5a | -8.0602 | -48.6856 | 2025-09-10 02:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 75d37c2c-2ab5-3e77-a4d1-0a9ed322e94f | -8.0414 | -48.6873 | 2025-09-10 02:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 371eaecc-32bb-305a-acf2-ae2d965a885d | -9.0132 | -46.0563 | 2025-09-10 02:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 4bd35037-d4e2-39eb-9756-888098a13eee | -11.4883 | -50.4083 | 2025-09-10 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 929b78ff-4491-3263-bec6-269055c30781 | -11.4657 | -43.6195 | 2025-09-10 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 39d1cf74-0446-3d09-af06-7b2ebd94c551 | -5.589 | -45.0505 | 2025-09-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 9e25fdc7-4f1e-3727-a6c1-323dc56b9c69 | -12.012 | -50.9891 | 2025-09-10 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 7f62a129-dd96-3bf6-9f08-9908abccfc2e | -5.5892 | -45.0278 | 2025-09-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 304f282f-ef3d-33c7-aa97-579ee36781e6 | -11.4465 | -43.6224 | 2025-09-10 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| d3ee44c3-83ea-37ec-b6a9-1ce851116151 | -11.4689 | -50.4319 | 2025-09-10 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| c179012e-6123-3d8a-a6af-b95720ee6442 | -5.5705 | -45.0291 | 2025-09-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 94462157-51a6-3e31-be99-2b74aa1730ad | -11.4883 | -50.4083 | 2025-09-10 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 00545734-a139-3125-b38b-0ff681750aaf | -14.7542 | -45.3156 | 2025-09-10 02:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 0b2eb836-a311-3ea2-80bd-bf7a84cff2fc | -20.0198 | -47.6225 | 2025-09-10 02:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 19a4b058-7317-37cb-b6c6-110ab3f5911d | -11.9929 | -50.9913 | 2025-09-10 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| b64aee8a-f73a-3852-8a1f-3554ea2e80a4 | -16.4148 | -49.8936 | 2025-09-10 02:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 85247b9e-6abd-37d1-971c-d908671140cb | -11.4657 | -43.6195 | 2025-09-10 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 645802ad-a9f9-3b5a-a8fa-c302aa2377cb | -8.0604 | -48.664 | 2025-09-10 02:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 7173e047-8f76-3e0c-b023-a69091ad54bc | -19.6476 | -45.0374 | 2025-09-10 02:20:00 | GOES-19 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| fe362222-8b00-360f-8753-78b827969a73 | -5.5892 | -45.0278 | 2025-09-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 166.0 |
| e3a0f5df-80e6-36bb-a849-a6d0d375d102 | -11.4652 | -43.6432 | 2025-09-10 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| c7ecb749-67d5-3284-8a18-15927b95c90f | -8.0602 | -48.6856 | 2025-09-10 02:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 109.6 |
| a79f470a-f569-3707-af3d-ea9863cb4f22 | -12.012 | -50.9891 | 2025-09-10 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 68bfe229-3e39-31c8-9b2d-09be3a08a704 | -11.4465 | -43.6224 | 2025-09-10 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 4b2210bb-b394-30cc-9ef2-76aeed73dad1 | -16.4143 | -49.9158 | 2025-09-10 02:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 41bde482-5568-32c8-a2f3-2fe7e478a943 | -5.535 | -42.65 | 2025-09-10 02:20:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 355af3ad-2f0c-3631-97c6-04f25eaa3090 | -16.3951 | -49.8969 | 2025-09-10 02:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ee78bb15-6add-3335-a8e9-7bb088d103fa | -8.0414 | -48.6873 | 2025-09-10 02:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 8a0ebdc2-3ac5-3190-acf7-49fa98d82e76 | -6.2595 | -43.4129 | 2025-09-10 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 30024f0c-95c4-300a-bd42-0533cd3e87f6 | -12.0117 | -51.0104 | 2025-09-10 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3ad3c148-a562-3d12-acec-4b65cb34890d | -5.5705 | -45.0291 | 2025-09-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 561d9ad0-96ab-3017-9856-ac0c308d31ba | -16.3946 | -49.9191 | 2025-09-10 02:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 79a4e845-5821-30aa-8037-c7f6e7ff5c15 | -14.7536 | -45.339 | 2025-09-10 02:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 545d1105-87c8-36f9-8d77-d66e64eb51b0 | -5.589 | -45.0505 | 2025-09-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| a52f87f1-b81d-3402-8a05-0fa3e61b6d61 | -11.488 | -50.4298 | 2025-09-10 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 4ad6aa4f-bb6d-3020-ba79-d27cd0f21323 | -9.0132 | -46.0563 | 2025-09-10 02:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ba56ac21-b54a-356a-a4e2-5397b1edf4cf | -5.5703 | -45.0518 | 2025-09-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7fa7ac7f-0745-3989-aaae-08ba941f0c9e | -5.6788 | -43.3425 | 2025-09-10 02:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| beacefc8-35ae-32ea-b47e-7612437423cb | -5.5705 | -45.0291 | 2025-09-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 65f6cd41-567f-3a67-90c5-27bee1637302 | -12.0117 | -51.0104 | 2025-09-10 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 06504d41-e5df-3fee-b18a-094537c364e2 | -5.66 | -43.344 | 2025-09-10 02:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 01a5b3dc-f4b9-3367-a60b-69ce4f56c36a | -8.0414 | -48.6873 | 2025-09-10 02:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6f3ce292-7b6d-3358-9777-430e19ab0ba0 | -5.5703 | -45.0518 | 2025-09-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b4251f5d-0837-3ee9-b677-5c63483c9767 | -11.4657 | -43.6195 | 2025-09-10 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| b78b08ed-602c-3cb8-8554-5130d8e0d733 | -19.6476 | -45.0374 | 2025-09-10 02:30:00 | GOES-19 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 412fb6cd-df7a-3b1c-ae1a-a8abb955537a | -5.535 | -42.65 | 2025-09-10 02:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 522c7178-eb51-379e-83de-e02cecdf8f4d | -5.589 | -45.0505 | 2025-09-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| edacb98d-ec16-3f63-b9e6-cd83708bb7bd | -5.5892 | -45.0278 | 2025-09-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 3a5451be-364a-307f-9c77-7d52cbc983c4 | -12.0304 | -51.0296 | 2025-09-10 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 28e387ff-4ab1-3de5-95d1-51de4dcdc53a | -20.0198 | -47.6225 | 2025-09-10 02:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 442234e6-edf6-3292-8220-07257ae9069a | -5.6788 | -43.3425 | 2025-09-10 02:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 41ab4227-627c-37c4-96d3-04815c642f92 | -19.9994 | -47.6271 | 2025-09-10 02:30:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0ae715d7-bc8b-328f-8462-b2af8fa6e9bf | -12.012 | -50.9891 | 2025-09-10 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 73897ad7-310a-3080-b513-1c30869d4867 | -6.2407 | -43.4144 | 2025-09-10 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 7d17a128-8e10-3625-bdcb-0d1c9ea71abe | -6.2595 | -43.4129 | 2025-09-10 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 7a702130-19f6-3caa-af3b-acf368506e63 | -8.0602 | -48.6856 | 2025-09-10 02:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 3e70522f-ca54-3dda-bed1-0e0ba2bcd362 | -11.4883 | -50.4083 | 2025-09-10 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ebfbc776-8599-3290-b075-9ef15555929a | -11.488 | -50.4298 | 2025-09-10 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 86d2f001-3f36-3e18-b969-03e82cad8ea6 | -11.4465 | -43.6224 | 2025-09-10 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1e3073f0-f998-3017-8533-c3dfea7f034e | -11.0733 | -65.1935 | 2025-09-10 02:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 264eafcc-129d-3c08-9e92-bfc9ee2cc2b4 | -5.5892 | -45.0278 | 2025-09-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ebda1dd1-ba50-3ca7-8a2f-2b4365f0bb17 | -11.0734 | -65.1746 | 2025-09-10 02:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| ac347dbc-36ca-305a-ba64-1560632ffef5 | -8.0414 | -48.6873 | 2025-09-10 02:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 5502ee9e-5489-3acd-a5de-2c9b0991924f | -5.589 | -45.0505 | 2025-09-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| bdb7a0fd-832a-32a5-880f-bb13dcf557b6 | -9.4388 | -46.7052 | 2025-09-10 02:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d96bf7ee-d358-32e9-b963-e6d4b2f8dc34 | -8.0602 | -48.6856 | 2025-09-10 02:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 97.2 |
| d5fb916a-5d94-3f2a-993e-e09d1f60d87f | -5.5703 | -45.0518 | 2025-09-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 724a01ac-8b04-381f-9971-dc652be89b25 | -11.4465 | -43.6224 | 2025-09-10 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 819be935-ee1d-32d1-a698-f0d17302ba54 | -6.2595 | -43.4129 | 2025-09-10 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| d23b70dc-09e0-39e1-8342-85f9d4cc2aaa | -8.0604 | -48.664 | 2025-09-10 02:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 1f66b66e-8fe2-362e-8e7f-0f0491d3a2b1 | -5.5705 | -45.0291 | 2025-09-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e25c5d61-905e-3485-bd18-96cee13369a1 | -11.4657 | -43.6195 | 2025-09-10 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d5d1cbd8-a4dd-3a4d-aecf-e692418ad7b2 | -6.2597 | -43.3895 | 2025-09-10 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| af2ddd42-b1f1-3a91-ba44-6738cbd04e58 | -11.488 | -50.4298 | 2025-09-10 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 4dcd4c05-a95b-3ce3-b09a-266712da716a | -20.0198 | -47.6225 | 2025-09-10 02:40:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 2267ebd5-0e59-332b-9ab1-a5e67b685bfc | -11.4657 | -43.6195 | 2025-09-10 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| a3ae58af-c4ea-3641-bf63-74f3d189919f | -5.5892 | -45.0278 | 2025-09-10 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 9d1ab48c-c222-34f2-8de6-6370f702d576 | -8.0604 | -48.664 | 2025-09-10 02:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 67.8 |
| acb50471-931c-3136-9c2a-b0e8c01d7f14 | -13.1176 | -54.9191 | 2025-09-10 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 0794cbc4-059e-345c-b3aa-70a567795361 | -5.5703 | -45.0518 | 2025-09-10 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ae3751ce-5994-32aa-bb69-d7f109dc995e | -5.589 | -45.0505 | 2025-09-10 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 18eb905e-5f54-3630-b811-e14bdb1c3cfb | -6.2595 | -43.4129 | 2025-09-10 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 422cdce4-07d6-3b84-9cd3-49bc7fe394a7 | -8.0414 | -48.6873 | 2025-09-10 02:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 88.8 |
| ac6bb077-5785-38a0-81a9-831f2c77f811 | -11.4465 | -43.6224 | 2025-09-10 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| ad21867b-a6cb-32bb-ba2f-5dcf24dae7aa | -8.0602 | -48.6856 | 2025-09-10 02:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 114.4 |
| aad36bbb-9123-3d9f-b620-e9651de205c3 | -20.0198 | -47.6225 | 2025-09-10 02:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ee5e781b-13af-3b0c-8f67-6104e6c0257e | -11.488 | -50.4298 | 2025-09-10 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 799eae53-3d7e-3ed5-86bb-bad09c49fa46 | -5.5705 | -45.0291 | 2025-09-10 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b5477c1e-82ec-3e3e-9a70-f89fd116ea48 | -5.535 | -42.65 | 2025-09-10 02:50:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 0bbbfd47-2a58-3014-862c-6561ebb9cb3f | -16.4577 | -50.6554 | 2025-09-10 02:50:00 | GOES-19 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c66f365f-7fd3-3dfb-92ef-3c173a988ebe | -5.589 | -45.0505 | 2025-09-10 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 54b26425-b83f-3f42-bf48-36d2ea20f450 | -5.5705 | -45.0291 | 2025-09-10 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ac306809-ccf6-38df-a672-289e502eb01e | -19.9994 | -47.6271 | 2025-09-10 03:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 77df69f6-dcbe-3482-86b0-6a95c2c574ef | -8.0602 | -48.6856 | 2025-09-10 03:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 228d3d02-4e01-308c-92a7-902370f4a33c | -11.4657 | -43.6195 | 2025-09-10 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e33ebf95-2866-31fb-bb53-5910aaaf6402 | -11.4465 | -43.6224 | 2025-09-10 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 34464780-5b12-3bb8-9337-67b7b5d6a650 | -11.0733 | -65.1935 | 2025-09-10 03:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 3dd8ec52-d772-397a-9014-80b7a9d67ee9 | -8.0414 | -48.6873 | 2025-09-10 03:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 7cef8405-0168-3633-9945-da991d8fba49 | -8.0416 | -48.6656 | 2025-09-10 03:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 88.1 |


[Clique aqui para ver as próximas entradas](README14.md)
