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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68bd1daa-3dcd-322e-85b0-25bd2f1f35c7 | -11.006 | -49.6461 | 2026-08-28 17:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| bf5197a2-a9b3-3a2d-9fdd-fb9eabf488bb | -9.2477 | -57.0697 | 2026-08-28 17:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 9361e460-975d-3826-8b80-3f65479c8969 | -8.3428 | -70.2781 | 2026-08-28 17:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 39.0 |
| e86508cc-6850-3eac-95ef-6d70cce7fd18 | -5.9995 | -57.8444 | 2026-08-28 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a11af102-91a2-37a3-b709-549ed7f56e14 | -1.2527 | -55.71849 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 43e3299e-5bc4-3429-b30e-f2d145fb48e9 | -2.88715 | -59.20108 | 2026-08-28 17:30:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 259dc544-0005-3252-ac99-de9d4bc32645 | -2.96064 | -60.97696 | 2026-08-28 17:30:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3a4bab6f-650e-3ef6-a680-34d9370083f6 | -4.32793 | -63.33688 | 2026-08-28 17:30:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a98c218b-fa39-3940-8fae-c52b74e0046a | 2.24097 | -50.76435 | 2026-08-28 17:30:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7585899d-3010-3f63-9414-5f0f8447465c | -3.09046 | -57.21029 | 2026-08-28 17:30:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5990e86-320b-3ecf-992d-1cf57f697dd2 | -3.24658 | -58.00806 | 2026-08-28 17:30:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5c6613bb-d259-3dfb-9e8c-fd6f5362fece | -3.41223 | -61.32837 | 2026-08-28 17:30:00 | NPP-375 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 577d90e5-5970-39ef-a9d0-12885d2a8799 | -1.24861 | -55.7152 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 10335cc9-ddd7-3e28-9e12-897cf523efd9 | -3.43929 | -59.08731 | 2026-08-28 17:30:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24e2f113-4594-3dd1-8c49-d6d88fcc8b28 | -3.3995 | -59.56543 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45824239-8099-3dbc-9645-edcd8db373b0 | -3.77444 | -62.00946 | 2026-08-28 17:30:00 | NPP-375 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e287863f-11df-3f5d-a472-bedaee2e50b7 | -3.40343 | -61.32059 | 2026-08-28 17:30:00 | NPP-375 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a0adc7cf-59b3-307e-af82-9dc51fdbe201 | -1.47544 | -46.56387 | 2026-08-28 17:30:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5c2f090d-8566-37c2-bc9f-9ac4cdb5091e | -1.10061 | -49.19496 | 2026-08-28 17:30:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 67543547-cb59-3144-9efc-2da7c5f4f20c | -0.90818 | -46.69029 | 2026-08-28 17:30:00 | NPP-375 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 96414dc9-b76b-344a-9cd3-a2367b6cefe1 | -3.48465 | -59.43149 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 03fca941-223e-3f9c-ab89-c1ad65397399 | -3.53462 | -59.02469 | 2026-08-28 17:30:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7a0f8e8b-1c33-3302-96e1-b54ba8c7884e | -3.71392 | -60.49031 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a2c83aef-50aa-3cc5-9f5b-5e437377702b | -1.8595 | -56.23853 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5063e279-9cf9-3350-99cb-7f9e62fdaaa1 | -1.81623 | -55.70415 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 044d116f-5e96-3724-b492-93732127570a | -3.40409 | -61.32502 | 2026-08-28 17:30:00 | NPP-375 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 413cfe74-dad7-35b8-83a9-9f10e93710e1 | -1.79292 | -47.9894 | 2026-08-28 17:30:00 | NPP-375 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff4783a6-592e-3cb0-a693-ff3c7bc07753 | -1.77764 | -48.70456 | 2026-08-28 17:30:00 | NPP-375 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5605dd81-1ca3-3dec-b974-ba554b7ec5a7 | -1.49081 | -55.67446 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b0a01d4f-3727-3337-b458-f2a7dfa249f9 | -1.52936 | -55.94997 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da3c2110-44e5-3927-9005-061343b5d676 | -3.77471 | -62.01224 | 2026-08-28 17:30:00 | NPP-375 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 02ea9a73-cb96-333f-82a4-e915a3fa92ce | 2.05277 | -55.90664 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b1ec7e5f-5f7c-3df8-99f5-8e56e92063c4 | -1.34726 | -55.46422 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 711197ed-6f71-3a88-8bba-ebf491f459ad | -2.9605 | -60.97551 | 2026-08-28 17:30:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a49d3c04-09e6-3d7e-a8a2-bdadc135e9a7 | -3.4872 | -59.43075 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c16987c6-95f6-34f0-a115-0e141c32173e | -2.4359 | -51.82708 | 2026-08-28 17:30:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7abfefb3-9f25-3f5d-99a7-7b60fcfbdf65 | -2.61151 | -56.59846 | 2026-08-28 17:30:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 813251e9-5ab7-368e-83ec-94cc0b8dc5c3 | -1.79684 | -54.9719 | 2026-08-28 17:30:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| de3eb155-b079-31ff-9798-afae4f847b89 | -0.51787 | -51.8122 | 2026-08-28 17:30:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b1e0da4-edc5-312b-8f9c-a10dad391fd0 | -3.04853 | -57.46564 | 2026-08-28 17:30:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 07878f22-bb46-3ee7-b7c9-8cf93dffaabd | -3.56069 | -60.90628 | 2026-08-28 17:30:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f3d35277-461a-3873-9b76-2cb5a8006fc2 | -2.87355 | -57.53548 | 2026-08-28 17:30:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 073e39c8-e200-3642-ae30-5ed1b98fae49 | -3.64462 | -60.55017 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 69371866-6129-3548-ad57-1713694b001c | -1.32615 | -56.12723 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32cd941c-bd88-3e8b-ab4c-10ac4cdf10ed | -1.23423 | -55.96797 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| b80b5eb6-6df9-3aed-9a02-6c3415dd7c51 | 2.24512 | -50.77081 | 2026-08-28 17:30:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| db916f1b-e5d9-3da7-9d95-cf9941e839eb | -1.91714 | -48.20647 | 2026-08-28 17:30:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f4eb653c-ba78-3e39-a321-0ab52a0600fa | -3.34654 | -58.20155 | 2026-08-28 17:30:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9cc6be5a-5a6f-3feb-a972-f8142757ed8a | -3.63866 | -60.55937 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| a3795280-ae43-33c7-ba53-db671ad71c2a | -3.7175 | -60.48975 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 801a34a0-a5b0-38ce-a144-78bf082d78d0 | -1.07051 | -46.6089 | 2026-08-28 17:30:00 | NPP-375 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1100486c-8320-344b-b218-14312011caeb | -2.27944 | -50.80555 | 2026-08-28 17:30:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bd2961fe-0d87-37b4-91e1-5180e9fb4e71 | -2.98589 | -57.918 | 2026-08-28 17:30:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f69a21e-92d6-355a-8aed-e31cd7013d78 | -3.38772 | -57.69489 | 2026-08-28 17:30:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 40325816-7fda-357e-bfdd-44454be111cd | -1.25093 | -55.70697 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7c8cd0e8-80c4-3b2f-afbf-f302eba08458 | -1.25211 | -55.71464 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8725f065-73d6-3f75-b9c9-8e7abbf91fbf | -1.77624 | -54.95825 | 2026-08-28 17:30:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b1148bd1-c57b-3824-9d65-8bbbbef6d4b4 | -3.19045 | -59.01222 | 2026-08-28 17:30:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab61748d-6b22-3f3d-b25e-31c431281a21 | -3.09259 | -57.22418 | 2026-08-28 17:30:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 26702b10-6110-33e5-b0bb-b7836408eeef | -3.48808 | -59.43098 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 52cb045a-091b-379f-a434-e5ff0ed5ca26 | -1.78177 | -54.97002 | 2026-08-28 17:30:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fea92cc2-a7ee-33a5-bc0e-9d52118ca1c9 | -3.2941 | -61.56933 | 2026-08-28 17:30:00 | NPP-375 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 388673de-c98a-3336-898e-5e7db83448a5 | 1.79039 | -55.81815 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4616943d-491d-3061-994a-c63d30106bde | -3.35675 | -59.57962 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 84bca9a6-6b4d-362c-b55c-d927cd8c4348 | -2.42684 | -56.37358 | 2026-08-28 17:30:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ff20bbb-b093-3835-9431-2d72b5c65de4 | -1.61359 | -50.01373 | 2026-08-28 17:30:00 | NPP-375 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a3fb9852-88e1-367f-b62a-de21f2a834f6 | -2.90604 | -58.30581 | 2026-08-28 17:30:00 | NPP-375 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1d6238ad-0f16-34df-b9e0-dcf6d32a8f51 | -1.96507 | -48.37193 | 2026-08-28 17:30:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39a88d74-d933-3913-a5a2-b2450dc60542 | -1.29859 | -50.02945 | 2026-08-28 17:30:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2d928482-6f25-32bf-9df7-df937ca4fdcc | -3.90552 | -60.94523 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 455add78-eb0d-3fcb-9446-e266a5541637 | 1.94818 | -55.7141 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 54400115-e7a9-3ab7-b182-67cce91bc051 | -3.09206 | -57.22071 | 2026-08-28 17:30:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbd4f132-0c82-3244-a15a-cdeddd035623 | -1.96567 | -48.37555 | 2026-08-28 17:30:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a40d4abb-e9c0-3ddc-be20-5732e640ea6c | 1.71713 | -56.03492 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3ab35570-367f-3bb5-8962-92d2342942c1 | -2.37726 | -57.25474 | 2026-08-28 17:30:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3927014-b584-30c8-80d4-43e1a3e6b98f | -2.75898 | -60.17498 | 2026-08-28 17:30:00 | NPP-375 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d577fdb6-6514-3291-8202-9ac9076b68e4 | -1.89896 | -47.04102 | 2026-08-28 17:30:00 | NPP-375 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eef0b547-a7e9-348a-a082-d73e07b96a24 | -1.46144 | -55.83218 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fa430766-8ba6-3851-ae63-f0bcb9ba5ab3 | -1.82031 | -55.70747 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aac253a0-60d6-38ff-be5c-52648a88d792 | -3.35618 | -59.57589 | 2026-08-28 17:30:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3d9080b3-00bf-3916-868a-10b9e654fcce | -3.10403 | -58.05157 | 2026-08-28 17:30:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9308833f-0099-3877-9e54-4ade708c1b7b | -1.65743 | -48.55209 | 2026-08-28 17:30:00 | NPP-375 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bba803f1-8976-3d31-a86a-65294d5da322 | -1.86292 | -56.23801 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec888145-5187-3863-a990-5e73f6aa2171 | -1.32681 | -55.96941 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| feb172ca-5955-34a0-b27f-5a746d068fd1 | -3.51358 | -61.59295 | 2026-08-28 17:30:00 | NPP-375 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 06806aca-e8be-35b8-a7d0-e0738e989df3 | -1.58123 | -47.73956 | 2026-08-28 17:30:00 | NPP-375 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| f3aaaea5-162a-3f52-832e-1050f0ff6db5 | -3.90487 | -60.94093 | 2026-08-28 17:30:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b1bafbd5-398c-30f8-99b8-1ccd6ca511dd | -2.89488 | -57.56761 | 2026-08-28 17:30:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 545f04bf-2069-3088-bcbe-ba5cf4385096 | -2.51804 | -60.03114 | 2026-08-28 17:30:00 | NPP-375 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2126a82-8444-3df7-856d-c07d94736c59 | 1.78914 | -55.82632 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f8887b2a-3377-37f9-8db3-9fefd0595f5f | -3.06336 | -58.00812 | 2026-08-28 17:30:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 199d9599-1397-3489-b8fd-5f014a15d19f | -1.37125 | -55.39159 | 2026-08-28 17:30:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f3765e81-be8a-3f9e-92a2-9c88e02284d9 | -1.99724 | -47.67417 | 2026-08-28 17:30:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dd1d0247-8723-3d1f-8116-20537f4970f9 | -1.28875 | -54.67311 | 2026-08-28 17:30:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4834421b-d9e3-3edd-b1e5-2402b148638d | -1.58189 | -47.74362 | 2026-08-28 17:30:00 | NPP-375 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e9551934-25b3-388d-ae51-a3a17d62e07a | -1.47857 | -46.56331 | 2026-08-28 17:30:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d756b110-2491-3d3e-8a40-910fb80a07e4 | -1.46202 | -55.83598 | 2026-08-28 17:30:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ac96079b-95b5-361a-bfa6-724ab2d41501 | -1.57542 | -47.74046 | 2026-08-28 17:30:00 | NPP-375 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 1f9735af-5f23-3942-b829-2ae8d65e04ab | -1.25443 | -55.70638 | 2026-08-28 17:30:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b87b428e-6492-3de2-93ce-a1eb23f27b47 | -1.99657 | -47.6701 | 2026-08-28 17:30:00 | NPP-375 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README133.md)
