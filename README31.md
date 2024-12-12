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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 329bfa08-04f9-3587-99f1-4557d2024c32 | -11.11962 | -54.65778 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7f3d3ea-630f-3c6c-ac37-125fb4617362 | -14.75953 | -52.65516 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc89a739-aaf7-39b9-9b40-6a624bcae11f | -10.53644 | -62.10117 | 2024-12-12 05:03:00 | NOAA-20 | VALE DO PARAÍSO | RONDÔNIA | Brasil | 1101807 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d56f701c-89e6-3f4e-9203-9c2bb93fa485 | -15.0832 | -59.63887 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef199cf8-7daa-3130-b8c6-66945eebd97a | -12.56022 | -57.76458 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6219d85-b64d-3c78-b063-db3b8b977041 | -14.75162 | -52.65385 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7f482c37-51ea-339a-9021-e7de836e918e | -12.91703 | -55.0528 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4215c3f-8cb2-37ce-b135-f00d7c0258cf | -12.53874 | -57.72816 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 507277c1-33d4-3765-9a7f-5b851b3b5ca8 | -15.24383 | -59.91771 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d5e6c9e-5a2f-3a7e-a267-79f9abe4b0d6 | -13.69893 | -54.76205 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e72f18c-9a28-3bfb-a5ae-a8e88474adfa | -12.92046 | -55.05334 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ffa79bd-bb2c-3b4b-8def-21bf74d7c526 | -11.61045 | -54.53028 | 2024-12-12 05:03:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5208616c-55de-3bf0-a62e-812cc2ca0912 | -11.42402 | -55.92029 | 2024-12-12 05:03:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38654e77-247d-3532-a041-a0a3a2a2dc38 | -13.69833 | -54.76606 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ac16c396-df48-3c9c-8f2b-addf847d9748 | -11.42457 | -55.91673 | 2024-12-12 05:03:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f60ece4b-8aad-3059-b141-500b05ee55be | -14.74586 | -52.63693 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 319453f9-9359-3cdc-a0ab-536a03af921e | -15.09818 | -59.63363 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dd29d9f-5856-3716-ac21-5f128fc9adca | -15.02726 | -57.60685 | 2024-12-12 05:03:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84b32ffe-8b84-3ced-839a-6208958ad218 | -12.53598 | -57.72407 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c1a4173-d453-350c-b07c-e5597b8223f1 | -15.08878 | -59.6478 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dd40c11-1a07-3952-978e-6fb20653b4c8 | -12.99531 | -54.1479 | 2024-12-12 05:03:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 929c2758-f4e4-3274-aecf-41fb1e6c3c5f | -11.14902 | -54.22824 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1eda9cb-6546-37b6-98ea-8bd5b35227ca | -12.53541 | -57.7276 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22e05ab8-e676-3ab0-958b-66f46055d9cb | -15.02614 | -57.61398 | 2024-12-12 05:03:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba4980d2-43b8-33cf-8474-e2c048de1b8f | -15.08917 | -59.6241 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d9d7849-0a37-3155-b4e5-d0920676383e | -11.11618 | -54.65727 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57b4e48e-ca20-3b0c-bfe4-eebc5484e99e | -11.12077 | -54.65023 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5336f2f8-9479-35bd-af1b-41d2bd763376 | -15.09907 | -59.64961 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1033051-0e4e-3240-b470-6ad189103761 | -10.5539 | -58.00672 | 2024-12-12 05:03:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0846009-56c8-3228-a149-687d24eac686 | -14.75776 | -52.65645 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4c7b597-cf2f-339c-ac20-8e5b1193e114 | -12.56298 | -57.76869 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0706a989-1495-3ac9-ad36-10c8ae021662 | -12.92791 | -55.05056 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5535977e-e468-38e0-a32f-ab3fe8286f5b | -13.0655 | -52.04435 | 2024-12-12 05:03:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bac79de-737f-39a7-940b-f77567f4e2f0 | -15.08575 | -59.62349 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa2d0721-6758-3941-ab29-5d1e86c4d33e | -14.2854 | -57.46597 | 2024-12-12 05:03:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae87ca49-6f39-35b3-ad4e-dfd9fdd13343 | -13.06953 | -52.04496 | 2024-12-12 05:03:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb9a1a91-4047-383c-834e-827ef32b341a | -14.74692 | -52.65854 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7706c690-0a72-30a1-a406-1ac2e567c15a | -12.92447 | -55.05003 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96831dce-f41f-3df7-a54a-8b5329264e9b | -11.11217 | -54.66052 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79851b73-664e-3732-941b-8fc93346841a | -17.74542 | -56.32352 | 2024-12-12 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c8d0472c-b5e9-3f51-bbd3-1423b4d1e60b | -12.53817 | -57.73172 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 62dcfa9e-5477-3c25-8d1c-7d3efea786b8 | -11.2039 | -53.83532 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c6d7ca64-dda0-3be3-9e8d-f8c6fbb942a5 | -11.11274 | -54.65675 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2105c5b-19b6-384f-a194-8998ae3ca359 | -14.74984 | -52.63748 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e197654a-1eca-36ca-8c16-24071fedc4de | -13.69074 | -54.76899 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ffbd979a-ba3a-3b87-8984-167a9417d6e7 | -13.32176 | -52.41523 | 2024-12-12 05:03:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d6188d3-2c5a-3e73-8dcc-27b6255b0109 | -15.06629 | -59.65569 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9f82717-115d-36c1-9b93-c705df4e2572 | -11.20989 | -53.81948 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d517124b-2a09-32cd-be63-a8ddb797de34 | -14.75381 | -52.63803 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bd2daf5-28c7-318e-be2a-ff8aaab2283d | -11.88885 | -54.67756 | 2024-12-12 05:03:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4555b83c-3899-3c53-adb8-d934cc76c5e2 | -11.20572 | -53.82303 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 71e29fcb-7969-3164-bc79-470def661c79 | -14.74441 | -52.64745 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e2fb76ca-5cb8-34ba-be54-0ce57378cd74 | -11.78232 | -55.13334 | 2024-12-12 05:03:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bb052cf-cfcd-3f8e-8013-dfcfad7c4d0b | -14.75089 | -52.65908 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 013e61f2-970e-30a1-8753-22aef65c8aac | -15.97084 | -57.17006 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17a8dd83-0ad4-33ba-9c6e-fcaad4b47164 | -15.96529 | -57.16174 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edb745f2-0a6b-37eb-ae4c-742c58e49844 | -16.02555 | -58.46464 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 108fe94d-c898-3269-a1bb-fdfbe968615d | -11.42069 | -55.91976 | 2024-12-12 05:03:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dd7a358-2abe-3042-a48d-3c7a6386447e | -13.69193 | -54.76099 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e09a60d-c47b-3cb2-9750-34583cf2df0b | -12.55877 | -57.70959 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2792db52-b70e-3957-b765-ac703e4a98f0 | -15.06973 | -59.65628 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07290bb8-b8b6-3ab2-9aff-aeb4095246fa | -12.53655 | -57.72052 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bcc0833-cafd-34ec-a507-f3aed6e5d97d | -15.23972 | -59.92102 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83973925-9561-369f-b7ef-6441df9d2cfe | -15.09285 | -59.64455 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c82fd42a-76e7-3e9a-a5fb-de206ffff76d | -13.69483 | -54.76553 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f39ad642-8588-379f-ad70-ae09f1899faf | -14.28153 | -57.46898 | 2024-12-12 05:03:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d40e428d-844a-30b9-994a-9e24d86d7236 | -14.75705 | -52.6439 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ee2e8fe-a403-3f9a-b1af-2036dfaa64e0 | -11.64889 | -58.26868 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32c291e3-d1bd-3d97-8a84-f3e851098611 | -12.55678 | -58.35532 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b2e632e-0cb3-3360-b080-5da03b55d490 | -11.19861 | -53.8219 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e69382d-5492-3816-bed1-7bed62d7946e | -11.42846 | -55.9137 | 2024-12-12 05:03:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7154336-3d35-31e8-bf4e-74eabc123009 | -11.78289 | -55.12963 | 2024-12-12 05:03:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2ae48f3-9678-3406-9e7c-88e631121b2a | -12.99173 | -54.14734 | 2024-12-12 05:03:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5878331f-3c67-34c7-b39e-3134d75ab4a7 | -14.7491 | -52.64277 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e183449-e078-3e40-bb61-c41cc2de10b4 | -13.071 | -52.03427 | 2024-12-12 05:03:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6524ce49-09ea-3ea2-8107-6ecb01ce464f | -12.91359 | -55.05225 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73c0effc-901d-35ab-820a-44c105337ce6 | -14.75057 | -52.63215 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3550fa6-3d3f-3e1b-87ee-609901739f4d | -11.20451 | -53.83123 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f7da3c70-75a7-3204-acb4-56e55c4d1883 | -12.9239 | -55.05387 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e01757b-13d1-31ae-80bf-abd1443f2750 | -12.55342 | -58.35474 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f30b061c-6522-3700-aae8-8293712188f5 | -14.74296 | -52.65797 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 564b15f4-bcb2-38fa-b291-f9977b744839 | -13.65406 | -52.93683 | 2024-12-12 05:03:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43d8b1f4-3eee-3733-a62e-f38cd99e8f09 | -12.92103 | -55.04951 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba2b37d9-d48b-371b-ba2e-5cd02fa35c93 | -16.02222 | -58.46408 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3fde2597-39da-3986-a20d-19a8f8c8cc06 | -12.12048 | -64.16183 | 2024-12-12 05:03:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9476e216-8aaf-3f32-ae7a-a42c69de47e3 | -14.75631 | -52.64921 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f97892a0-aeea-3428-b961-57f100a7cc6a | -12.92334 | -55.05768 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ed8f95a-ebab-363b-8555-072d0a5a3fac | -12.9199 | -55.05716 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2be0e08-f747-3462-aa69-0a4ad81b5928 | -13.06196 | -52.0402 | 2024-12-12 05:03:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 070ddaea-9487-3fba-b4b9-b0a74137fd8d | -11.11447 | -54.6454 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 16376105-b7b5-3c0a-94d3-88241c7f21bd | -15.08536 | -59.64718 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01b1fab5-6a1f-33e2-aae8-64d867b6687a | -11.11561 | -54.66104 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74ddb50c-09ea-3d22-9c94-8d3431596936 | -12.5376 | -57.73526 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 69075c45-bcb9-32b1-aeef-a819d61f1a95 | -12.92504 | -55.0462 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21a1dc2d-aa5d-3566-90f1-de0f33887e17 | -15.09133 | -59.63239 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42bffe86-fb80-327b-b5bb-0ec0798a380c | -11.2033 | -53.83941 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c2b84fb6-0cfd-3283-baa7-18ca8fb28a47 | -11.06452 | -57.87114 | 2024-12-12 05:03:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5db0fc4e-b45d-3b3d-94aa-ad005288968f | -13.68843 | -54.76046 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc4d414f-c64a-3bf1-91f2-8d314be73e97 | -12.5562 | -58.35895 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75daa53a-2a8a-3726-bef7-c39ed2ea31df | -15.7977 | -58.52965 | 2024-12-12 05:03:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |


[Clique aqui para ver as próximas entradas](README32.md)
