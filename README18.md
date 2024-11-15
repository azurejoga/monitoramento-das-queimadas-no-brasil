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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ff1d2d4-cedc-3516-a6be-de030ada6ee5 | -17.235 | -57.4516 | 2024-11-15 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| b417fb97-b689-36cb-9a28-8444384ee7b7 | -17.2543 | -57.4698 | 2024-11-15 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 21723ca1-6cd3-3b35-a1f4-70522a7ba274 | -17.2347 | -57.4721 | 2024-11-15 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 34bd99d6-3133-3bde-93e4-906bee894758 | -17.2547 | -57.4493 | 2024-11-15 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 106107f6-4c1b-30d9-ad4d-480e6572f908 | -17.5882 | -57.4711 | 2024-11-15 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| c2dd46fd-0f1e-3480-a98d-458cf45a2280 | -7.51211 | -34.85505 | 2024-11-15 04:40:00 | AQUA_M-M | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 8714c9b2-d3f1-342d-bbbb-9110e85fa267 | -7.51964 | -34.86523 | 2024-11-15 04:40:00 | AQUA_M-M | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 48267cd2-221f-3df1-a446-8cf228f18acf | -7.51079 | -34.86393 | 2024-11-15 04:40:00 | AQUA_M-M | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c38d26b9-7a3d-3097-b481-2ca20375976b | -7.52097 | -34.85635 | 2024-11-15 04:40:00 | AQUA_M-M | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 9b9100c2-3a42-306a-b49d-9e00122e9209 | -1.67431 | -47.98126 | 2024-11-15 04:42:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 639d307e-a107-3d8e-ab2f-dcb4aa8f7e93 | 0.00554 | -51.2244 | 2024-11-15 04:42:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f0b1828-c27e-3bb3-b18c-d4f9fe65cbbe | -1.90645 | -45.4551 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4982a579-7992-3cb2-a80c-67fdd52e3f0a | 1.05869 | -60.60412 | 2024-11-15 04:42:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18093a24-cfc9-3338-a83e-64ca4a2a4c09 | -1.45922 | -48.19581 | 2024-11-15 04:42:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf126f49-70e1-3486-ba1b-de59ca64d079 | 0.43719 | -50.92722 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8d8a38fb-df30-3b60-849a-30a0538cf11d | -0.94448 | -51.72876 | 2024-11-15 04:42:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b7beb6b-d164-3c0f-9bfc-e76fc15b1fc4 | 1.05944 | -60.60899 | 2024-11-15 04:42:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8342bd94-16e6-3834-8cbf-cd48b7b9370b | -0.98974 | -51.77813 | 2024-11-15 04:42:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2380780-393c-31b3-8b8b-205004907acf | 0.6066 | -50.84931 | 2024-11-15 04:42:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a7b7ffa-e7c4-3c90-8bdf-b4627cecac41 | -1.34449 | -46.55877 | 2024-11-15 04:42:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74950adb-407b-387f-8a7f-2b460fb7f2b6 | -1.93183 | -46.27689 | 2024-11-15 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abd8cb63-c2db-3bab-b130-6f2832975f73 | -1.90792 | -45.44743 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2aca93ed-544e-31ee-a439-e39679f00f8f | 0.44398 | -50.92616 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eb84e9c5-04a6-3594-86f2-453ed0670e10 | -1.90468 | -46.477 | 2024-11-15 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b57c5c19-a4f6-3f69-a20c-d9f2664b8809 | 1.55117 | -50.97103 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5296c3e1-d44e-3d80-9c46-5b4c69a25c4c | 1.07479 | -51.14101 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 022430f9-cfcd-3cfc-a9a5-b8b26bc97b3e | -1.91034 | -45.45572 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad4f0c47-5ead-3e5c-b2b6-fb39086c8348 | 0.12455 | -49.84734 | 2024-11-15 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa0abf32-1ed1-31c1-be16-af4854b97ba2 | -0.93638 | -51.73518 | 2024-11-15 04:42:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a13fbf51-c5cb-3302-9560-84058da1df0b | -0.29501 | -48.42726 | 2024-11-15 04:42:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 161c659c-40a8-3dd7-b0d0-86ebc290c4e3 | -1.91108 | -45.45292 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc57a52e-a347-398c-8ebc-91e94fe663fb | -1.14339 | -47.6925 | 2024-11-15 04:42:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae35d50b-b034-3509-b784-a27258465303 | -0.98628 | -51.77759 | 2024-11-15 04:42:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 402a204e-347d-3fe3-9049-231f3a6fdedd | -0.64032 | -51.73242 | 2024-11-15 04:42:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 0b5ea4da-9d75-3372-9435-00a62eeb4bc3 | 1.07765 | -51.13677 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25398f69-3a9f-3d11-9d58-b5ce4f775f41 | 1.0649 | -60.60313 | 2024-11-15 04:42:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e61b3b3b-788b-37e7-ad02-dd29c5c71611 | -1.90721 | -45.45023 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aa89554-fe73-3563-804e-b9e0d98e10a9 | 1.07422 | -51.1373 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e4d8529-4def-386a-9ef3-f66555068b05 | -1.92203 | -45.564 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de7532c3-0ca4-3966-8b12-c336cb8ae43c | 0.11791 | -49.84837 | 2024-11-15 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 497d4689-ab5e-3645-8901-03e5ff2eb574 | 1.07252 | -51.14894 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40e3ab31-78d2-3411-8997-11b58c10ef88 | -1.46261 | -48.19634 | 2024-11-15 04:42:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f22e0fb-412b-365e-9d5e-fa625865a03f | -1.12339 | -48.35435 | 2024-11-15 04:42:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6e7ddf6-f347-34e8-8f7f-5a8b8e642453 | -0.25496 | -48.50756 | 2024-11-15 04:42:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82231c07-f884-3482-a935-dc2529a45ee8 | -1.85688 | -46.28535 | 2024-11-15 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90e33c21-8ac1-35b9-9d3c-205f450c5c99 | -0.19087 | -49.04661 | 2024-11-15 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3469adc-952d-32d7-8f09-7747abbc3732 | 0.90807 | -50.14137 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f903d90d-c490-3089-8789-ca6c0f4a4d9d | 1.07194 | -51.14524 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 959167c6-46db-3507-879c-e0d566ed6682 | 0.38175 | -50.88405 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a810af7e-490d-323c-8828-2c9bfb937a65 | 1.05793 | -60.59925 | 2024-11-15 04:42:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2df8e170-5a8e-3ecd-97de-6dbebe9b42f4 | -1.92129 | -45.56884 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 148f5bb1-dfcd-3350-be82-bf8222514cf9 | -0.98915 | -51.78189 | 2024-11-15 04:42:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c20e9124-f330-38fe-958d-c5ee155c6f69 | 0.44341 | -50.92255 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09c679d5-d4c4-356e-9ba8-eb7f64e521c6 | -0.94103 | -51.72823 | 2024-11-15 04:42:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 598d6025-e3b8-3f48-8d10-592b0456b1b2 | 0.12068 | -49.84441 | 2024-11-15 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12b4c777-c577-386a-b391-fee15f3520f9 | 0.69614 | -51.44295 | 2024-11-15 04:42:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d2d2d9e-ac62-3bf2-9d11-15c8b13788d4 | -1.92812 | -46.27631 | 2024-11-15 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c689edc4-7ec1-3275-97a7-459818c63836 | 1.07537 | -51.14471 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd29eb18-3ff2-325f-b5c7-0efc6745aef3 | 0.4468 | -50.92202 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 570455a0-e20f-3cf1-895e-e6e22c52dae8 | 1.07595 | -51.14841 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe350d6a-8505-34d1-b722-59a21ad18239 | -1.2167 | -47.47223 | 2024-11-15 04:42:00 | NPP-375D | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0d264b6-1c91-3891-b0e1-1f3374d38625 | 1.19656 | -51.29467 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dff1c702-6f84-304d-a8c8-3fec37e9d539 | 1.01218 | -60.57761 | 2024-11-15 04:42:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffdeac2b-762c-3059-8a54-444a873b6ba8 | 1.06566 | -60.60801 | 2024-11-15 04:42:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b9016b7-64b4-3f70-9b43-d6a7690fcab0 | -1.71086 | -46.16116 | 2024-11-15 04:42:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2191930b-08bc-3a4f-af60-47988f65a163 | -0.80528 | -51.48715 | 2024-11-15 04:42:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cd8cc90-656a-37b7-a8f8-b0c56c3978fd | 1.0805 | -51.13252 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bbe261c-6689-3d5c-a32f-68ae613fdb62 | -0.02234 | -51.24754 | 2024-11-15 04:42:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 065e52e8-9847-3ff6-845c-cc0e2cba1ee9 | 0.12177 | -49.85131 | 2024-11-15 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89c49a4-8f23-3470-95c3-d7c3a661d388 | 1.05719 | -60.59443 | 2024-11-15 04:42:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afa679b2-e6d5-319b-a58d-7237844b2169 | 1.07136 | -51.14154 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e10db98e-fcb5-3b3c-bfec-aacd9c9ee142 | 0.02809 | -49.40727 | 2024-11-15 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bf1e7a7-e3cd-3f8f-8993-fff20dfe89b8 | -1.6997 | -45.81027 | 2024-11-15 04:42:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbea24cf-f2a2-3188-b9f7-a39a953e87fb | 1.55099 | -50.97095 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66bbffb4-de20-3201-a797-41ab7429a7ac | 0.85161 | -50.20787 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 35285f05-6901-3da8-9df1-59a59b6d1ac5 | 0.12123 | -49.84785 | 2024-11-15 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8eeab788-7941-35e6-a847-4f52bd3719ef | 0.60378 | -50.85345 | 2024-11-15 04:42:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd90f643-7258-3ed0-8ef1-8fed9f234b51 | -1.70713 | -46.16059 | 2024-11-15 04:42:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fc53217-1257-3026-a82c-070d62f3f691 | 0.44001 | -50.92307 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f006c718-78af-3638-8ecc-f09c9729bff6 | 0.38514 | -50.88352 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e97b96b-3dc0-3c4d-8655-40cd70b506b4 | -0.93817 | -51.72394 | 2024-11-15 04:42:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0f00d02-264c-351b-9553-77b5c02572ec | 0.84827 | -50.20839 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07dc5fef-e277-3400-acfe-d6c0251c5d46 | 0.83666 | -51.39856 | 2024-11-15 04:42:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85a9cb91-b87a-3d44-9f0e-d64e463817fe | -1.90645 | -45.45718 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d9f4bdd-89a1-38aa-8d4a-cac8c5f9791c | 0.90473 | -50.14189 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78d6daea-4d1c-31bf-8ca7-792b8c07c954 | 1.07707 | -51.13306 | 2024-11-15 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfc197d2-2944-345b-a640-f770faebea84 | 0.02478 | -49.40779 | 2024-11-15 04:42:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d07f08f-5c88-362c-92f6-304e11ea7965 | -1.67088 | -47.98075 | 2024-11-15 04:42:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1f2c8f3-2179-3190-b6ba-5171a571451e | -1.90719 | -45.4523 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10338b2e-ec4a-35cd-98ed-3d5f78f91135 | 0.84012 | -51.39802 | 2024-11-15 04:42:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a59e1d56-58c5-3294-9904-ef0f4b2ec8aa | 0.44737 | -50.92563 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b30ec9c3-0f07-3126-907a-4ab5cbff828b | -0.95654 | -47.88478 | 2024-11-15 04:42:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dfb08d8-d4a7-38f6-b2d7-8dc967cc94ff | 0.60717 | -50.85292 | 2024-11-15 04:42:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23b93dd1-e6c2-36ca-b238-e6906e0bc9c1 | -1.91111 | -45.45085 | 2024-11-15 04:42:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a1be438-a060-300d-93b2-02224a442d14 | -0.82846 | -48.61054 | 2024-11-15 04:42:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c88ce2a4-80e0-32af-9f55-e76463095fe2 | 0.44059 | -50.92669 | 2024-11-15 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 82831ff3-7982-3efe-bcc3-cbbd0f59c2df | 0.72224 | -51.47367 | 2024-11-15 04:42:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1000a0f3-7ef3-3841-88f1-03462b803cda | -1.70781 | -46.15614 | 2024-11-15 04:42:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afd40277-fe2f-3345-9b96-02fc068859e2 | -2.64363 | -46.18776 | 2024-11-15 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fb8ad70-c8d9-39ad-8b32-31665b804f88 | -2.16217 | -46.15891 | 2024-11-15 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
