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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19ebccde-ced0-30c3-bcfd-6c3934d54143 | -5.8999 | -42.83859 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c3fc91a7-e759-34a2-8bd7-45ca5d184274 | -5.64868 | -43.60861 | 2025-10-14 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 123395a2-7a63-31e6-8cff-f7e76e33e2e0 | -7.92714 | -44.13387 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5325289-d344-3272-8295-5713fbee34d4 | -4.66513 | -43.13139 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea717675-e66d-3492-9998-a60671109140 | -9.16326 | -41.05589 | 2025-10-14 03:36:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 399871cc-a523-3f7b-85fd-2f9dd2abe919 | -5.62563 | -42.58021 | 2025-10-14 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 53ab5798-73ff-3053-ba9e-00a999c8be2c | -7.94263 | -44.11264 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f94e7375-a8ab-3bd8-9188-39133fcb4279 | -5.11065 | -43.2031 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 20668ef9-95d7-3460-ab41-2c7cd24d6e57 | -10.16423 | -36.39117 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 65ff5d61-c585-3577-8a7b-d9c5fa65f22b | -7.21308 | -35.77481 | 2025-10-14 03:36:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a2389db-e060-31b9-9cb8-fa73c89d7786 | -5.62504 | -42.58369 | 2025-10-14 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 89826d99-7158-3caa-93a7-1e07244ae860 | -6.76239 | -39.08197 | 2025-10-14 03:36:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 57efee9a-ba9c-3e85-aee9-9c3a41fecbe8 | -5.88446 | -42.87777 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d05134a7-9a70-3594-9e90-0f04860796cc | -4.83924 | -42.76874 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b4779b4e-7372-3448-a694-a9049226edc2 | -5.38485 | -43.2227 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66c8c869-7c23-3fd7-af77-54a9815f50be | -5.42138 | -40.98326 | 2025-10-14 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8b6aa229-fef3-3114-96f1-1158b551d0fa | -4.68502 | -43.1385 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 198eac73-0877-3d70-9621-14b9b4850242 | -7.16891 | -39.23391 | 2025-10-14 03:36:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6fc53d44-474b-3ff9-a4df-adeb3d1d601d | -7.94759 | -44.11756 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fbdf09e-1024-36cd-ab3e-1ef00a14916a | -7.16724 | -39.23414 | 2025-10-14 03:36:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 23d63fdb-8642-3504-98ce-968ba59a031d | -4.80633 | -45.33607 | 2025-10-14 03:36:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d43cb96-11c0-3ffe-9fd2-8a4bb8fdb348 | -7.23165 | -45.31928 | 2025-10-14 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b9dd896-47b0-3626-8d09-aa429c0b6f73 | -10.16485 | -36.38743 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9838621d-8711-38d8-9cdf-8bad1d46783f | -5.15254 | -39.50778 | 2025-10-14 03:36:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 03f6043c-cd3d-3734-8bdd-d44fc93b0218 | -4.83501 | -42.76767 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49aca1c1-7bc8-325d-bc81-9e6e10af4757 | -6.535 | -43.55885 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 101a41c5-c797-3397-80a0-2bf06ebeecf5 | -6.00254 | -42.8699 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a1a73809-fe44-3028-981a-65ed5767e15c | -4.66462 | -43.12325 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c4b63c4d-c0eb-315e-8d12-73ea1cbbba0c | -7.14864 | -41.70896 | 2025-10-14 03:36:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f46f92c0-91bd-35c4-a80a-b2dc1878e7c9 | -6.90488 | -45.66286 | 2025-10-14 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed8322b4-c134-33b5-b381-c0fedea4e18e | -5.39043 | -43.22359 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f70d2a85-706e-3957-bb68-413764818ee4 | -7.16301 | -42.19105 | 2025-10-14 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61e90efb-f9f5-3f8c-823c-07e5102a8977 | -4.66449 | -43.13522 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| be63b69a-d79b-3cef-9a81-3b104e182459 | -4.62811 | -45.77288 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac93f86b-fc78-3e04-8561-d0d84fd50cad | -7.94553 | -44.12914 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5e52f4d-1fba-33ed-bb5b-8776fdfeb7da | -5.12019 | -45.49556 | 2025-10-14 03:36:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9faf8620-3ae2-3830-8ef9-4444c8886b29 | -6.52717 | -38.7171 | 2025-10-14 03:36:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af539d3f-f81b-3750-aebb-ecc69a61b038 | -7.48968 | -42.15043 | 2025-10-14 03:36:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1fc65151-ba44-314d-a843-fd7031b865cc | -4.83923 | -42.77564 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0a0daed5-5761-3ebc-b13f-dcfda9d111b5 | -4.66396 | -43.12701 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| e83c3c6d-5baf-3df5-928b-125e33a42ed1 | -5.94084 | -43.73087 | 2025-10-14 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7ac35e6-f239-32ce-a67f-7e14f053ab21 | -4.7989 | -45.34074 | 2025-10-14 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 116425a4-f498-3e53-ade8-bbaae0d56fcb | -5.49709 | -43.07125 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3019bfb8-0eac-3a12-849d-c082496069c5 | -5.65094 | -43.6084 | 2025-10-14 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7349856d-9c26-302a-8fa5-e13922e07a9f | -4.67941 | -43.13758 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2eb31c8-e27f-3544-a8fa-bc9cb1a9bccf | -4.68568 | -43.13472 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1d8e6d4-5619-3a08-8057-67153b3e3e68 | -10.17447 | -36.39286 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 22004bff-6b96-39c8-8398-4ed949f21fd3 | -5.88855 | -42.90508 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 31fb2eee-3729-353b-a3a5-8c62eefc7a2c | -7.94691 | -44.1214 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1eaabebe-49b6-3c06-83a9-497051a4739d | -5.99121 | -42.87127 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a3e0340d-fcbe-365c-b0f2-3acaf25e2e86 | -5.15689 | -39.50848 | 2025-10-14 03:36:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2b969651-37ae-3e84-a38c-16052cb85ab3 | -5.90524 | -42.83976 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| aa66183e-6273-3c55-aea8-ceec8898f041 | -5.87711 | -42.87436 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 26ede499-1845-36cd-8ac5-9b2b8bb83643 | -7.75287 | -44.72877 | 2025-10-14 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f30bc40-6430-388d-957a-d14d457d11f3 | -7.7474 | -42.44214 | 2025-10-14 03:36:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a166d42a-76dc-399a-9a4c-a9622d3bee34 | -10.16826 | -36.38798 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1db73ebd-f433-32b4-8e17-e001bbc42de6 | -6.53652 | -43.55928 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7bfbbc95-1e08-3657-a924-849b10b9c474 | -6.30029 | -43.0013 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| eeab1ac6-47a4-3fac-9761-e4b14f946f0b | -10.16704 | -36.39546 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| d592709d-333e-342d-96f6-05bd02c15cd6 | -7.92509 | -44.12714 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 395b10ff-c1c7-3b05-945c-2a7add8ce2ba | -7.75719 | -44.7384 | 2025-10-14 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 412fd1bb-0c83-37ed-a167-756d7e702b8d | -4.62294 | -45.77605 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8197554f-9630-3ebd-b107-5b701f302b38 | -6.222 | -41.55984 | 2025-10-14 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 813a7b5f-0552-37a3-9675-bfe417437866 | -4.65953 | -43.13043 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 71ba7961-f73d-39dc-bc7e-93c814fbcfb7 | -6.98715 | -47.08928 | 2025-10-14 03:36:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3226f87-8358-30c3-8e89-4210e3f0f037 | -7.92217 | -44.12896 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5fce914e-453e-3c6a-8f8d-99728f02013b | -5.42322 | -41.34363 | 2025-10-14 03:36:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 527526bc-ef86-3e53-bba5-2de0e4a0af87 | -5.11132 | -43.19926 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| db166c1a-bc98-3387-8e98-1c08578b0ac7 | -8.39361 | -45.05867 | 2025-10-14 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4a3923e8-748a-320f-80c2-bca9a9883212 | -4.68007 | -43.13379 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 667fc06a-c9e0-331c-ab7a-6ac7515cb40d | -7.94989 | -44.11963 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19b7184a-2024-373d-8ebb-6cadbfbce836 | -5.48851 | -45.0012 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa96a957-32f3-3545-8255-c3b7fc192174 | -7.64298 | -42.56857 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7a19421f-dd32-3145-bf14-69ef8a9e5fb7 | -7.67881 | -40.40965 | 2025-10-14 03:36:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 20383b68-7696-330c-89ce-79e82bc627e7 | -5.38588 | -43.22325 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e5554b4-8608-36fe-b2f3-0c4ee37ff452 | -5.98812 | -42.87132 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 05305408-6c2e-3c56-b7c6-cd3c91215e56 | -7.92287 | -44.12508 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e384d34-d01b-3739-a0c3-b2cacb8be58f | -7.90018 | -44.99609 | 2025-10-14 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56ada8c8-c059-3560-84c1-f9db2e953fe3 | -6.75851 | -42.80409 | 2025-10-14 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5ca03275-0e55-38d7-80ca-5dc51a29a2a8 | -7.9356 | -44.11931 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48562e38-775d-3b8b-b5dc-a3eef2fa157b | -7.92654 | -44.11938 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a5b97e5-4a05-3fa9-ac96-8ca923bcac3f | -5.62139 | -42.68882 | 2025-10-14 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 898ab3ed-bee5-3abc-8e83-2a44d5a86d92 | -4.66194 | -43.13845 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f3d232d9-3022-318f-81ee-ee708db50d82 | -4.67315 | -43.14039 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c0d4a54b-cff5-33bd-9301-3a36ea866269 | -5.88494 | -42.9062 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 20b829ea-b8b1-3c02-9157-49514328bc3a | -6.44573 | -41.83965 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 88099ec4-bc52-351a-baf6-55e3b03274e2 | -9.49275 | -43.06353 | 2025-10-14 03:36:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c0371313-ee72-3a1c-a2fb-31f6aeebd359 | -5.88367 | -42.91334 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f1847ee-2810-3677-852a-fac9161f7572 | -5.25209 | -45.23629 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50ea113c-11e0-31b3-bc1b-976ae727f354 | -5.88385 | -42.88114 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 22638a24-8410-3ea1-a0ee-bf1bd59adefc | -4.66755 | -43.13941 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9849e550-ae28-3011-8432-64856e081971 | -7.60732 | -43.98264 | 2025-10-14 03:36:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee8f2b46-ac8c-3e6a-a54d-09657af5aa29 | -6.44623 | -41.83674 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fb7fcb2c-b4b8-3bce-a61f-c18ec229236f | -5.10443 | -43.20572 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 47c0cfd1-72a9-37cb-a57a-c6ab7ef3c777 | -6.15415 | -41.76671 | 2025-10-14 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 78945614-1e45-34a8-9a8f-ca8ea67db7ef | -7.93629 | -44.11545 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dc76da4-67b4-3291-99f6-1b516ad36c7a | -6.15367 | -41.76951 | 2025-10-14 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42b2ffce-7d7f-3906-9584-accf5ebf01ca | -5.4922 | -43.06678 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0c17bc9b-b9c6-381c-837e-be3d7325a228 | -6.24092 | -41.55561 | 2025-10-14 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d6ec42f1-e06c-3c08-8b29-f06a4db3dcec | -7.94126 | -44.12034 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
