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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d19c109d-78c4-3a30-adfa-aec888ec6cf0 | -18.2537 | -56.6237 | 2024-10-18 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 272.7 |
| 3bfc5c3d-b401-3d8a-b10f-aac215abb95c | -18.254 | -56.6029 | 2024-10-18 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.3 |
| c4739014-eac3-3715-818c-a0d31d9b5009 | -18.2735 | -56.6211 | 2024-10-18 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.5 |
| d2c7db98-75af-3ca6-9031-ac0e1d368d46 | -18.2739 | -56.6003 | 2024-10-18 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 0d161690-47a4-33a6-b262-e4b8d34ae229 | -19.6005 | -57.0253 | 2024-10-18 01:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.9 |
| ce9e21a4-2434-307f-abfe-898baf7f3bcf | -19.6009 | -57.0044 | 2024-10-18 01:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 431.5 |
| cfd46657-81e1-3282-8397-448115c41f5f | -19.6013 | -56.9834 | 2024-10-18 01:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 217.0 |
| 3f6e8a95-da9b-3d65-a017-14bd291d5636 | -19.6206 | -57.0225 | 2024-10-18 01:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.0 |
| 5ed230c0-ec3a-395e-8490-1b1eb662963b | -19.621 | -57.0016 | 2024-10-18 01:46:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 177.4 |
| 14f384c6-9798-3a5e-9c08-1f290412f6f8 | -19.6213 | -56.9806 | 2024-10-18 01:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 7889f217-ab07-3549-8dfe-811a49b9c180 | -21.9662 | -49.7186 | 2024-10-18 01:47:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.3 |
| 311dd38f-1bf6-3a52-99f4-7ca326246785 | -23.3701 | -47.3747 | 2024-10-18 01:47:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.8 |
| b5d9b458-c3de-302a-bdff-11817c81c3e8 | -1.619 | -47.0919 | 2024-10-18 01:55:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e8005199-e775-3b00-87ae-5520b4e9e5f9 | -2.8795 | -51.6695 | 2024-10-18 01:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 354d600f-1905-3781-b7ab-7687aea2704e | -3.1382 | -51.497 | 2024-10-18 01:55:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b83f750a-f2a8-3dfc-bf3d-89d65b24e347 | -3.7009 | -45.9 | 2024-10-18 01:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| bdff047a-c445-3f81-b39b-6f6c50846686 | -4.4072 | -45.9773 | 2024-10-18 01:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 5387c73f-ab09-3d11-9224-7e9b2872176e | -4.4258 | -45.9763 | 2024-10-18 01:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 3cdecef7-ea01-32b0-849a-cf564e46ea45 | -4.58 | -48.0132 | 2024-10-18 01:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| df8da540-8a12-3d1d-b7b5-3fa8e0b670b9 | -6.6703 | -70.1174 | 2024-10-18 01:55:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 3cba6601-5ebd-3d1f-b3d0-b343b3d10e47 | -6.6886 | -70.1171 | 2024-10-18 01:55:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ca5dce50-8ce3-3ab0-9457-9e985e7bdb0f | -9.6073 | -36.0735 | 2024-10-18 01:55:59 | GOES-16 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| 01deb495-967d-3d65-8596-38a2ad5d27b0 | -12.5045 | -55.205 | 2024-10-18 01:56:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9d22c9a3-3072-3719-8935-778b80dabebe | -12.5048 | -55.1846 | 2024-10-18 01:56:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| dbe4fda4-9000-3e99-a6ab-87e92fc8b198 | -12.4964 | -63.2258 | 2024-10-18 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 282fe6ab-b1ec-35dc-8792-d6415ca05a5a | -12.4966 | -63.2066 | 2024-10-18 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 44b29f21-d72c-3f7c-aa8e-9b47c0d855cd | -12.4967 | -63.1874 | 2024-10-18 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e5c6cfb9-951f-3dc5-ac5d-b2335694ce50 | -12.5155 | -63.2055 | 2024-10-18 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 1c49f392-b707-3462-9c96-54bc7596749f | -17.2177 | -57.3102 | 2024-10-18 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 94185319-beef-3e99-b082-8fb95b060b4c | -17.2373 | -57.3079 | 2024-10-18 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.1 |
| f1e0a84a-013a-35b7-be1a-cb3c10b2ca5e | -17.7851 | -57.4679 | 2024-10-18 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| ba195b5a-d8b5-3526-a9ee-8fa12e16dede | -17.7855 | -57.4473 | 2024-10-18 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| f0a943d8-a6d4-364a-b8f2-31fe406349f5 | -17.8049 | -57.4655 | 2024-10-18 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 21bb2fdf-7130-316a-ab6e-30500525c17e | -17.8246 | -57.4631 | 2024-10-18 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 6704cf9a-d02f-3c77-900e-b7ac123ef0c0 | -18.0632 | -57.3514 | 2024-10-18 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| f2e02ce6-cad1-34d9-80b7-d64eccaa2b09 | -18.2533 | -56.6446 | 2024-10-18 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.2 |
| 5f19e25f-2338-3551-a0c7-15f20ccfd0a1 | -18.2537 | -56.6237 | 2024-10-18 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 349.6 |
| 0ac7e16c-b719-3141-915d-d643cf1be439 | -18.254 | -56.6029 | 2024-10-18 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.5 |
| 00e97253-a3ee-387b-8e36-a0d6d811c2b5 | -18.2735 | -56.6211 | 2024-10-18 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.5 |
| eefdf97f-90bf-3fb0-bce6-386d1e703b76 | -18.2739 | -56.6003 | 2024-10-18 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 59a4e978-2f94-3049-8d85-b8c498ce1f96 | -21.9662 | -49.7186 | 2024-10-18 01:57:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.3 |
| 3ccbf102-485d-3031-9a1d-a5883453f062 | -23.3701 | -47.3747 | 2024-10-18 01:57:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 2390a28c-a3f9-3bd0-b13e-0de5f6847661 | -1.619 | -47.0919 | 2024-10-18 02:05:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 727c281b-48ae-3f15-af1d-8bde350bee26 | -2.8795 | -51.6695 | 2024-10-18 02:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f3b1b7a0-e382-3e96-88fb-f3235e6b28da | -3.1382 | -51.497 | 2024-10-18 02:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| cf756ff5-726e-3465-a20c-a812dca293c4 | -3.7009 | -45.9 | 2024-10-18 02:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 94cf08a3-2d5e-3af0-b91e-d6b237fc7ccc | -3.908 | -42.402 | 2024-10-18 02:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| a9e0edf5-5d67-342b-852c-b807c48bade9 | -3.9267 | -42.401 | 2024-10-18 02:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 7516a8cd-43cc-3644-88f3-133e7593409c | -4.4072 | -45.9773 | 2024-10-18 02:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| d052ee24-d1df-3040-b2a9-a6955d22bc71 | -4.4258 | -45.9763 | 2024-10-18 02:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 04b3aa92-cdb3-30c4-89e6-0092669432f1 | -4.426 | -45.954 | 2024-10-18 02:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| b553e180-3be0-32d6-99e3-513584ece3c2 | -4.5614 | -48.0141 | 2024-10-18 02:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 585067f3-66bd-3661-90da-aee83e052ccf | -4.5799 | -48.0349 | 2024-10-18 02:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1c263d5c-f789-3e07-b9ff-01d202b1e460 | -4.58 | -48.0132 | 2024-10-18 02:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| da87e2d3-aa7d-3e69-8baf-7b1ceaf27ec7 | -6.6886 | -70.1171 | 2024-10-18 02:05:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 72bc9bce-1321-3e9a-a2a3-33a6423bd070 | -12.5048 | -55.1846 | 2024-10-18 02:06:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f068ad81-1588-3be7-a5f3-fadcce5170e0 | -12.4966 | -63.2066 | 2024-10-18 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 13fa4fe0-5ac0-37bc-a086-182f2078601a | -12.5149 | -63.2822 | 2024-10-18 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 99cf5d2d-5db3-341d-bcd8-4fdae8d75e8e | -12.515 | -63.263 | 2024-10-18 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 4f0fb29b-7987-3c89-86d5-20aa42180ecd | -12.5155 | -63.2055 | 2024-10-18 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 92e32936-972d-397c-bcac-b22a8c2aa19e | -12.5338 | -63.2812 | 2024-10-18 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e0ea6d65-fc7e-33b6-9c8c-e42aeb18a03c | -12.5339 | -63.262 | 2024-10-18 02:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9808807d-0613-3293-9400-c66ee928a4c6 | -17.2177 | -57.3102 | 2024-10-18 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 3d598037-2625-3dfb-8475-da5c7f8833e4 | -17.2373 | -57.3079 | 2024-10-18 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.3 |
| c5ea1e37-b1c1-36d5-b927-77a6d394b047 | -17.7851 | -57.4679 | 2024-10-18 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 38ab05fc-6359-398d-a440-76f6973ce7b9 | -17.7855 | -57.4473 | 2024-10-18 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 49dc7846-4264-3e68-a9b9-b572f80d4e52 | -17.8049 | -57.4655 | 2024-10-18 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| fe2057d7-1977-33f4-94c7-9373e12dd0c5 | -17.8246 | -57.4631 | 2024-10-18 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| b9417489-863b-3da8-b126-84bf06f5623d | -18.0632 | -57.3514 | 2024-10-18 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| c7e421fb-e672-39a9-8bac-236bff93b25d | -18.2533 | -56.6446 | 2024-10-18 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.4 |
| ba9de70c-f09e-3ce9-a263-7601eb1ff26b | -18.2537 | -56.6237 | 2024-10-18 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 312.2 |
| 7bc76501-7350-3aab-ba6d-a8c6c477e208 | -18.254 | -56.6029 | 2024-10-18 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.9 |
| c74ab280-d987-3280-8031-ca6ee5673a7b | -18.2735 | -56.6211 | 2024-10-18 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 0d894129-7fcd-315a-b3af-9dead180612e | -21.9662 | -49.7186 | 2024-10-18 02:07:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.0 |
| 34c8fd8f-0a89-306d-b30b-a7e6f0d9da32 | -1.619 | -47.0919 | 2024-10-18 02:15:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 671d63a6-79be-368e-a693-84c43e993101 | -3.1566 | -51.4965 | 2024-10-18 02:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 83a2913b-37ba-32d4-833a-22a1611b2e1d | -3.7009 | -45.9 | 2024-10-18 02:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 3b7bf1f0-871b-316f-8c68-e8a151d8c32d | -3.908 | -42.402 | 2024-10-18 02:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 72c6c509-e22f-3b4f-96ca-069d5fc92c1b | -3.9265 | -42.4246 | 2024-10-18 02:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 29f603a6-d2cb-3c8c-8969-26ab8c01db3f | -3.9267 | -42.401 | 2024-10-18 02:15:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 133.8 |
| ab39f3f4-18af-3061-a2c7-2d7703515bc5 | -4.4258 | -45.9763 | 2024-10-18 02:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 55f71cc9-82d6-3c49-abd3-c9c35ea9db65 | -4.426 | -45.954 | 2024-10-18 02:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| fdd6cbea-caff-3210-ad2d-ce583fd581c1 | -4.5614 | -48.0141 | 2024-10-18 02:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a91f2982-a346-3338-a971-d8405953d052 | -4.5799 | -48.0349 | 2024-10-18 02:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6b69b85a-8fb9-37d0-b928-6264ce262a89 | -4.58 | -48.0132 | 2024-10-18 02:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| d679fa12-7a30-33e9-8a1e-9dd1cab92203 | -6.6886 | -70.1171 | 2024-10-18 02:15:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8c0e4e9f-889b-33a0-98a4-bd78eb59bddf | -12.5048 | -55.1846 | 2024-10-18 02:16:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| f42613ee-14a3-3ad4-850e-2c95f3d745f7 | -12.4966 | -63.2066 | 2024-10-18 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| af779b11-2ca3-304b-9f8a-ee9470a846fa | -12.5155 | -63.2055 | 2024-10-18 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 16febc40-c736-349a-be10-b5fe978e665c | -17.2177 | -57.3102 | 2024-10-18 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 81ae0ad9-232e-399e-81a4-412286d56d5e | -17.2373 | -57.3079 | 2024-10-18 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.6 |
| d8748b10-5e9f-35c3-bf70-4d31578ad189 | -17.8407 | -40.0275 | 2024-10-18 02:16:44 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 198.9 |
| 10d47230-00d0-3d20-b888-6e0192ca757d | -17.8415 | -40.0014 | 2024-10-18 02:16:44 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 233.1 |
| 0c7f0248-3dde-3d40-bf8f-9d4ed48d3dac | -17.7855 | -57.4473 | 2024-10-18 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 1c7da5c1-3f21-3464-9bd8-a913d3ced862 | -17.8049 | -57.4655 | 2024-10-18 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| 99fa3e7a-4f35-37fe-ba45-855b2e7175ed | -17.8246 | -57.4631 | 2024-10-18 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 6687aa60-e9ae-3018-8dcb-1094927cf289 | -17.9234 | -57.451 | 2024-10-18 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| a5ddd9a2-71e4-37a7-bc64-89fa7c0aafe2 | -18.2533 | -56.6446 | 2024-10-18 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 186.1 |
| 88abc390-a44e-3391-954e-b9cea8941357 | -18.2537 | -56.6237 | 2024-10-18 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 327.6 |
| 4749b91e-729b-368a-87d6-4c7164868336 | -18.254 | -56.6029 | 2024-10-18 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |


[Clique aqui para ver as próximas entradas](README18.md)
