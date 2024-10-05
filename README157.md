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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a90d91ea-5127-3fdf-b365-f90db1f4b058 | -18.6785 | -57.2734 | 2024-10-05 11:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.2 |
| 34754e3b-719f-323e-9a7d-f004af9bc6a3 | -8.8714 | -48.3297 | 2024-10-05 11:55:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2dcc6d2e-4f90-3b48-ac6f-1fb9bb68fd07 | -11.7187 | -47.8107 | 2024-10-05 11:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a4a0dbfe-b6b6-3950-93ae-872874e5154a | -12.7819 | -50.5543 | 2024-10-05 11:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8a1d4292-24f0-32e3-8d73-101ddc1b5c69 | -13.1241 | -46.3748 | 2024-10-05 11:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 39485287-0444-32c4-a693-51ffadf0f912 | -16.9717 | -56.7646 | 2024-10-05 11:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 77500708-9963-3c44-a8a5-581759d8ec3a | -17.0299 | -56.7987 | 2024-10-05 11:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.7 |
| cb640318-cb6b-34b3-bafe-c3c35f5afcfa | -17.0316 | -56.6956 | 2024-10-05 11:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| b90dedc7-fca0-3ff3-82be-46b939332d34 | -17.1182 | -57.4039 | 2024-10-05 11:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 161.6 |
| 475c779b-3658-3304-9706-b65a5e4f55d8 | -17.1378 | -57.4016 | 2024-10-05 11:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 165.6 |
| 7acb5149-0aa8-372e-b0f6-21c11bded4b7 | -17.1375 | -57.4221 | 2024-10-05 11:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 174.8 |
| fc1f8bed-5b02-3916-a2cf-7bb3bc77bdf3 | -18.6785 | -57.2734 | 2024-10-05 11:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.1 |
| 35f7662c-8237-328e-9496-5edcecda71a2 | -18.6586 | -57.2759 | 2024-10-05 11:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.3 |
| 906ff93c-6635-34fb-9e7a-309b3fb27b02 | -18.49 | -52.91 | 2024-10-05 12:03:38 | MSG-03 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5940fc3b-dafc-331f-b0ff-d65e64bc7529 | -18.46 | -52.95 | 2024-10-05 12:03:38 | MSG-03 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 334fd26f-c36f-3aba-86ed-4a8f98e57384 | -18.49 | -52.97 | 2024-10-05 12:03:38 | MSG-03 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 526fa138-15b3-31a0-8c53-1b6dd294b209 | -8.5928 | -46.5039 | 2024-10-05 12:05:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 04c0209d-f51b-3792-b4d1-e2570d65d161 | -8.6116 | -46.502 | 2024-10-05 12:05:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| c7ac5731-b0d5-35e5-86ca-4a865e331e1f | -8.7584 | -49.9566 | 2024-10-05 12:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2ced485e-41dc-342a-a3ef-8186656c38cd | -8.7772 | -49.955 | 2024-10-05 12:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3816b3e8-6fbd-30d1-803a-a0bd89f7c213 | -8.8714 | -48.3297 | 2024-10-05 12:05:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 98306e8a-9271-394e-93e6-282bbd7305c4 | -9.8545 | -46.7257 | 2024-10-05 12:06:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 00855784-7361-38b0-8aa4-a4803d1c3f4d | -9.8356 | -46.7278 | 2024-10-05 12:06:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| b0a501b7-faf7-3bc6-94ac-0a7172e1a414 | -11.2427 | -46.5997 | 2024-10-05 12:06:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |
| d5b074ad-9e10-3e5d-83e9-4bbd3413dc5d | -11.3177 | -45.5228 | 2024-10-05 12:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 452120e6-3b0e-35c1-967b-f02913c9df8f | -11.3853 | -47.2088 | 2024-10-05 12:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 1f375a3a-ba63-399f-9c53-fa6a2b7e072d | -11.3665 | -47.1889 | 2024-10-05 12:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 61972b04-494d-35ee-89ed-d6b28bd24e61 | -11.3662 | -47.2113 | 2024-10-05 12:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 84a3d41f-c336-3454-9497-23ac299bcaf9 | -13.1056 | -46.3321 | 2024-10-05 12:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3b358cc3-4314-33f9-9048-440e8afcf690 | -14.0577 | -45.138 | 2024-10-05 12:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3f576259-48c6-32d8-b577-f1b8085fc1bc | -17.1085 | -56.7892 | 2024-10-05 12:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| b622352f-c59c-30c3-9b4d-9f4581bfe002 | -16.9714 | -56.7852 | 2024-10-05 12:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.2 |
| 602a51e3-ae01-3281-94e7-6320c8763cf0 | -17.0316 | -56.6956 | 2024-10-05 12:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 7997a1d6-987e-3906-a11d-f38e6acb88f6 | -16.9717 | -56.7646 | 2024-10-05 12:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.4 |
| 4907fe96-2eee-3bf9-9646-a8c34aef881e | -17.1378 | -57.4016 | 2024-10-05 12:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.9 |
| 21b299a9-de4f-3151-9e7b-897a783833d2 | -17.1182 | -57.4039 | 2024-10-05 12:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 157.1 |
| b2cb74b5-5efc-3334-93c3-3ed4fed908cf | -17.1574 | -57.3993 | 2024-10-05 12:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 8402bf91-5be1-3ea0-95df-8199b7960c97 | -18.6984 | -57.2708 | 2024-10-05 12:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| f7ed98d9-32c7-32ff-be00-7cc2dd3feb09 | -18.6785 | -57.2734 | 2024-10-05 12:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.7 |
| b319eca0-5398-3548-830b-26eee0dba153 | -18.6586 | -57.2759 | 2024-10-05 12:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| d4ab4639-dca0-37d6-b251-cbe060164d2d | -6.9514 | -59.0666 | 2024-10-05 12:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 26ee0346-1d80-31e2-ba9f-8a55f80c39ab | -8.5928 | -46.5039 | 2024-10-05 12:15:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| dda3d6db-b65f-3923-84f7-f0f2771d13b9 | -8.8525 | -48.3315 | 2024-10-05 12:15:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 83964325-d369-3f70-8c53-0b23ab948f89 | -8.8714 | -48.3297 | 2024-10-05 12:15:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f36c920a-8c8f-3896-8bae-4ca4bc86769d | -8.7772 | -49.955 | 2024-10-05 12:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 1ae077f9-0660-3c73-a9f5-f2aaff1ec850 | -8.8528 | -48.3097 | 2024-10-05 12:15:56 | GOES-16 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d8c538e9-5db0-3e23-94b0-5e65fed566be | -9.8356 | -46.7278 | 2024-10-05 12:16:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 035f8132-7592-3a6e-89c0-4aaa66cd1e02 | -9.8858 | -47.1901 | 2024-10-05 12:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| ba81623a-19b9-3149-a06c-b775705834ad | -9.8545 | -46.7257 | 2024-10-05 12:16:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a1b0019b-07a4-3060-9554-5820c9a53db8 | -10.4424 | -50.7336 | 2024-10-05 12:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 7ee3b742-b869-3beb-b552-86205f00ba7f | -10.7542 | -46.1894 | 2024-10-05 12:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| b1e6c66f-d522-335d-861f-dc3c1b72ceda | -10.7546 | -46.1667 | 2024-10-05 12:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 66707c9e-ac21-3c9d-a67c-e7733c9c8b9f | -11.2427 | -46.5997 | 2024-10-05 12:16:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 476.4 |
| 469c4054-735e-38b2-9226-097562f2f7e3 | -11.3368 | -45.5202 | 2024-10-05 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.4 |
| d4fc0941-cdfb-38d5-bd99-264d7d3c4b71 | -11.3177 | -45.5228 | 2024-10-05 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 39c8c8c3-e0e1-3067-8c82-18847cc94176 | -11.3662 | -47.2113 | 2024-10-05 12:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 2e85f430-d0c0-3542-abea-a2274a7edc69 | -11.3665 | -47.1889 | 2024-10-05 12:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| cdee14ef-76e7-3c5f-be46-9973af80b7a8 | -11.3853 | -47.2088 | 2024-10-05 12:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0d1b4127-669f-3181-8adb-39b24cefd9f5 | -12.7623 | -50.5782 | 2024-10-05 12:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1979b9a7-4161-35b4-a233-6d6363d79bf0 | -13.1056 | -46.3321 | 2024-10-05 12:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d6892778-9511-3181-b956-22d99adc3b98 | -14.0504 | -45.4877 | 2024-10-05 12:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| f217a232-252c-32ef-aa86-3e74a8b04f51 | -16.6797 | -55.4985 | 2024-10-05 12:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 6dcfe1e5-cdfe-340e-b463-5df86114ea0b | -16.6801 | -55.4777 | 2024-10-05 12:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 882e5d2e-bc0c-3ccc-9d00-2cbddf3c898e | -17.1085 | -56.7892 | 2024-10-05 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.8 |
| dc6ab92f-fd54-36ba-ba77-4d5a4f7cf564 | -16.9913 | -56.7622 | 2024-10-05 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 8cc08bc2-f4d0-3112-acf0-a80ed827b3a1 | -16.9717 | -56.7646 | 2024-10-05 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| 51354d1a-a9cf-303a-a0cf-d75d3a90c9a2 | -17.0316 | -56.6956 | 2024-10-05 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| e84b90e2-907b-3181-bf74-f4a22f9b4b39 | -16.9714 | -56.7852 | 2024-10-05 12:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.0 |
| d0543fb8-aa6e-38aa-8211-72f80ac85022 | -17.1185 | -57.3834 | 2024-10-05 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| dc656069-8f2e-354a-9fd1-40ffeab42f2b | -17.1378 | -57.4016 | 2024-10-05 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 186.3 |
| a04f8c16-24c5-306b-95f3-b5d84586e0b9 | -17.1574 | -57.3993 | 2024-10-05 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 0399d47b-c851-3ca7-89b5-62e63e61aa23 | -17.1182 | -57.4039 | 2024-10-05 12:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 180.1 |
| 36a4c7d4-fe3b-3de0-96ac-633297a966a8 | -18.6785 | -57.2734 | 2024-10-05 12:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.6 |
| cba55272-bdda-395e-8df5-07a0592168ba | -18.6984 | -57.2708 | 2024-10-05 12:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| b3338f0f-b56c-3cf6-8fc2-d6094bf0577c | -18.6586 | -57.2759 | 2024-10-05 12:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.8 |
| 2b995fb7-68ae-35fa-9010-f86a131e72be | -6.9699 | -59.0658 | 2024-10-05 12:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fe389eea-0eea-3662-bb9d-ff2b5270e898 | -6.9514 | -59.0666 | 2024-10-05 12:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| bc7b8c3e-f45e-3e11-9140-348e63e7bcad | -8.5928 | -46.5039 | 2024-10-05 12:25:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 6616561e-d29e-36a0-9e72-0b91ceeeeac2 | -8.8714 | -48.3297 | 2024-10-05 12:25:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8a880c8d-a0f2-376d-a41e-3bc6ea591ad7 | -8.7772 | -49.955 | 2024-10-05 12:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f836c017-d38c-3815-ae4d-b6d2a5db8028 | -9.8858 | -47.1901 | 2024-10-05 12:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 6bdfaf29-5bd8-3d6d-adc2-bbff9298b8f0 | -9.8545 | -46.7257 | 2024-10-05 12:26:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 157.5 |
| bb17e691-e2c0-3bae-a104-1dfaad47329a | -9.8356 | -46.7278 | 2024-10-05 12:26:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ab2df41f-2621-3ae9-bc05-a0b6b5d817bb | -10.1031 | -46.5623 | 2024-10-05 12:26:03 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| b5823562-8bb7-383f-bcb7-d8036b6c6347 | -10.4424 | -50.7336 | 2024-10-05 12:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 35b7dc35-e91d-3250-bb3e-3ea399803406 | -10.4427 | -50.7123 | 2024-10-05 12:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 15719e68-f516-3108-aa35-5bd46b43f4af | -10.7542 | -46.1894 | 2024-10-05 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 95ee6a8e-99f5-327b-aa05-b95d7e3d31a9 | -10.7736 | -46.1643 | 2024-10-05 12:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 95478651-407d-370d-9d2f-0f409b2a973a | -11.3368 | -45.5202 | 2024-10-05 12:26:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 84dc9746-969e-3a10-aa49-22773085a936 | -11.3662 | -47.2113 | 2024-10-05 12:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| e55ab36a-2ad0-3d9b-a3bf-cfc43be0bcb8 | -11.3177 | -45.5228 | 2024-10-05 12:26:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d8887ddf-710c-3ae7-980c-bca56bc6e3b1 | -11.3853 | -47.2088 | 2024-10-05 12:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 28883d40-076a-3974-b3d9-4483f25d1795 | -11.7187 | -47.8107 | 2024-10-05 12:26:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 3f2462d7-b4ec-3096-bf0a-91580376d6a8 | -12.7815 | -50.5758 | 2024-10-05 12:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| dc1f2530-3ca9-3c74-8ac6-dff0e6e156b2 | -14.0504 | -45.4877 | 2024-10-05 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 77473f31-7623-32f2-95a9-b8d43be055f6 | -15.1821 | -48.0754 | 2024-10-05 12:26:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d1037077-c578-313e-b699-aaa8a8e56787 | -15.1826 | -48.0528 | 2024-10-05 12:26:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b558fd40-d1d4-361a-ad1b-5f8d76f069fe | -17.1081 | -56.8098 | 2024-10-05 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| e9d8c724-078d-3af8-a561-8cd1b0fc782c | -16.9913 | -56.7622 | 2024-10-05 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| a0cdc3ee-4fad-3110-bcd6-e95fb30198a2 | -16.9717 | -56.7646 | 2024-10-05 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.7 |


[Clique aqui para ver as próximas entradas](README158.md)
