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
| f1f6e3d2-4233-3168-8c60-b1bd2fa26673 | -12.98366 | -62.71164 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71ba5dd4-2064-3f69-b961-0579957a51e9 | -12.98311 | -62.69257 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e7d5982-6d5d-3629-9f66-6dd3fb855311 | -12.98231 | -62.69715 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d56ccf60-8c18-3849-92ce-bc51dae4a275 | -12.98071 | -62.70635 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce45bfda-06c8-3d7c-871c-3b3fc9242778 | -12.97991 | -62.71096 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bf204f5-f96f-336d-945d-8b8c4c08cab4 | -12.97856 | -62.69648 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6f67283-4b37-3284-94cb-9c687309e9d3 | -12.97776 | -62.70108 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55d2ac0c-742d-3c4b-9538-656098c6d31e | -12.97696 | -62.70567 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d08a53e3-dd14-3fd3-9f01-6709b242d1c0 | -12.96418 | -62.66722 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 873ad641-0449-326b-a552-4b35e46a9680 | -12.96089 | -62.66492 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a022d302-ff6e-3fa7-93e1-a358b977cb1c | -12.96044 | -62.66655 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5114936-3de1-3133-83bf-86bfe420f086 | -12.95954 | -62.65055 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1aa6efc-8d5a-36b9-a112-fdb5ffc7ae33 | -12.95811 | -62.68033 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb20b8a5-4994-3881-8460-6401f652e0f2 | -12.95767 | -62.68325 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e6a44e5-e74f-3328-ae9c-26613e842d79 | -12.95733 | -62.68494 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de60bad3-5e13-319d-8872-28a5b6aacd1a | -12.95714 | -62.66426 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de64ae21-d286-34e0-942f-81a7e9a0ff3e | -12.95687 | -62.68784 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d91b2609-0b52-3f92-b758-f59afd131f5d | -12.95669 | -62.6659 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 138207e6-e4b8-3fc2-8655-872149064b57 | -12.95656 | -62.68953 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83c0368f-50b9-37e5-968e-d4c124429a11 | -12.95634 | -62.66884 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18251830-fa6b-38ca-9e8a-720b1b370ae2 | -12.95606 | -62.69244 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 118b64a5-be41-3121-bb71-8d9536bebf47 | -12.95591 | -62.67048 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94844b59-820a-3290-a09b-9f5115eb15d7 | -12.95578 | -62.69414 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 001c05f6-3665-30f9-9efe-2c2e5ac4b57b | -12.95553 | -62.67341 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64fecb15-6ee2-31f8-9eb2-8fe6cb517ad7 | -12.95514 | -62.67506 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32362dc3-af7a-37d0-bab0-33c5a9451626 | -12.95473 | -62.678 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2783dc1-dc55-3266-ac2f-d5284e7aa408 | -12.95436 | -62.67967 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4044d780-8676-325d-afb5-791a67b4f5cb | -12.95358 | -62.68427 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19352efc-dc4a-3ab3-a405-771177267399 | -12.95311 | -62.68718 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a720ff9e-27e8-3727-8030-063904e48472 | -12.9528 | -62.68887 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc0f7578-453c-32d9-97d7-882fe22d84a8 | -12.95202 | -62.69347 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b53fd729-befb-3da6-a124-ae70a16dc972 | -12.9515 | -62.69636 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8a4ac653-2ad3-39ee-820f-a90223341dd8 | -12.95125 | -62.69807 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7929b7af-11ab-3278-b467-ebf8fdaa7647 | -12.94775 | -62.6957 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 11d71e52-2d5a-34ab-add1-4b02ba8b8e58 | -12.94749 | -62.6974 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 93bdd14a-d854-3596-9b6a-3ce0828951aa | -12.94574 | -62.61681 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42eb5f67-5847-3658-92ca-c7d19deced7f | -12.94374 | -62.69672 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7e12a3ce-6d98-3fc1-bf92-af4939645ab4 | -12.94123 | -62.6207 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3804ee76-8661-395f-bb05-bdf8a2acf97f | -12.93999 | -62.69606 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c5cd3c7b-7cf9-3b94-aa35-951e9bf0c0a9 | -12.93623 | -62.69538 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6684fb23-b883-3df6-a403-949e5ed16bb7 | -12.93545 | -62.69996 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe1a3e5f-9cb2-352e-bc91-bd2024b5588d | -12.9317 | -62.6993 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| def375e1-abea-3791-9067-73317c7477e6 | -12.92795 | -62.69862 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33c845f4-9cb6-3425-b197-9c8a0f053f53 | -12.92419 | -62.69796 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbd952be-c924-3724-b2f5-583cbde35f5c | -12.92044 | -62.69729 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1818a05-4686-37a9-980a-ea83715b1999 | -12.91965 | -62.7019 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e2a1d52-6876-3bb3-b1fc-d169570ccf82 | -12.91668 | -62.69661 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54d7db34-9e2e-39ac-93b1-74dabe33da46 | -12.89971 | -62.66037 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8445e58-c05c-371c-a3b1-a8e23ef31642 | -12.85906 | -62.5331 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b085fde1-9e0a-3d7b-96a7-c8695551ecf7 | -12.85848 | -62.78643 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7031cc7d-0dc3-36b8-a7af-69655a644295 | -12.85752 | -62.54216 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13d046e5-3f7c-38e0-89c9-0114b982860d | -12.85687 | -62.52338 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a259112b-6e15-3fa9-bd7b-b7bfefea2e3e | -12.85676 | -62.5467 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a081a8df-7955-38c0-945d-ff144a882570 | -12.85599 | -62.55124 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49453b1d-4fb2-345c-81f6-c32867888537 | -12.8547 | -62.78575 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fa3ce67f-e15f-385e-916f-d4099c81f801 | -12.85389 | -62.79041 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| cb931157-afb7-316c-9f90-688386208b00 | -12.8538 | -62.5415 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c629a24a-03ec-3612-8707-394aa0c0e1f5 | -12.85315 | -62.52271 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7d6d2a87-3f3c-3ff9-a12b-cf0eb07bc33b | -12.85303 | -62.54603 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7e49bebf-1e84-371d-8610-4f718e0fcb1d | -12.85226 | -62.55056 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| de76432a-85b1-3ed8-aa81-81e4cba98bfd | -12.85161 | -62.53176 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 83e09973-da28-3ae8-8769-6e1d0ca48712 | -12.85149 | -62.55509 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 64f0858a-d028-32ec-bc22-de53780a5621 | -12.85093 | -62.78506 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e98be0b-af30-3be6-828c-f6532901e7f8 | -12.85012 | -62.78973 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3afb7167-9295-393e-b69b-c7a916ce57d2 | -12.85007 | -62.54082 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 08b65736-9aa9-3fb1-b009-6bb33811c4f6 | -12.84943 | -62.52204 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2212eaa8-6777-36a9-8386-452ca928557f | -12.8493 | -62.79439 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 876c3868-880a-3f1e-875c-5615839ce36a | -12.8493 | -62.54536 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f26fcf73-a4a6-389f-842f-5eddad02e50d | -12.84853 | -62.5499 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2713a6f0-c858-3f9e-ad07-6b385be478a7 | -12.84789 | -62.53109 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bbd1b4d8-54e0-34ed-a50a-c5aa10c7f3ef | -12.84776 | -62.55443 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 222232df-f9c3-3694-bd0e-404f0801d788 | -12.84634 | -62.78905 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 516d322a-89cd-3210-9c6c-64553b700c46 | -12.84571 | -62.52137 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 64ba65d9-c6c1-3e8f-83e4-96e73bc75fe7 | -12.84558 | -62.54469 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 726c2b48-5322-34b8-94c4-0f8cb81ab2ff | -12.84552 | -62.7937 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 074970ef-bc0d-37e1-ad22-879fb6cb46c0 | -12.84471 | -62.79838 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f2f730d3-2bff-3d3b-8c82-01270a9b8418 | -12.84417 | -62.53042 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d706c2d8-f736-361a-9588-40389df2a30d | -12.84389 | -62.80305 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3d7150d8-4f13-3ec3-a0eb-e47b35cf64ae | -12.84346 | -62.71671 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c8affcb-fd6d-3a50-96b7-7240bea54c36 | -12.84226 | -62.8124 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6d1c04e-eeee-31fe-a672-24d5586780b2 | -12.84198 | -62.5207 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d003d0d-3d10-30b3-9d7d-58ae52bad13b | -12.84185 | -62.54401 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6aec7ad8-02a1-3394-92bb-b14191af2eb4 | -12.84175 | -62.79303 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 644ceed7-dd86-3bb5-8a7a-db8a28117af5 | -12.84144 | -62.81708 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eff207a0-d730-3bac-8589-64d237ea79cd | -12.84121 | -62.52523 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f1c33d17-44c2-398b-8fcd-5ac7d9a166d4 | -12.84093 | -62.7977 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32c1c0f4-55da-3e4f-8233-97391884058e | -12.84044 | -62.52975 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 39f964e4-8355-371e-8d9f-e95294db16e5 | -12.84011 | -62.80237 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6656057a-414b-3ba5-b64e-c84d9eba0ca1 | -12.83967 | -62.53428 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b1ba1bd5-bb6c-3d32-baec-c997bc165cd6 | -12.83749 | -62.52456 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 750a4e7b-e3c0-3c3c-97e6-c69323193f0e | -12.83715 | -62.79702 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 758029fd-0aed-3b49-b426-42bfd5d72179 | -12.83672 | -62.52908 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 83bd7997-3bd4-3ec5-a3a0-deaf60d659d2 | -12.83633 | -62.80169 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c7c9a566-2c10-3154-a25a-b7d05019f7c4 | -12.83595 | -62.53361 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ae6bf831-6298-3cb4-8a96-52a55d3fd0a1 | -12.83454 | -62.51936 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a387b505-34b4-3176-b8e3-f84dc2c72c60 | -12.83377 | -62.52389 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f568e96f-ea15-399f-aa95-0296fbfa74f0 | -12.83344 | -62.79877 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a615fe-b776-3485-89e7-d301ea125a44 | -12.83255 | -62.80101 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4fd989d-594f-3c26-ac06-ade5e84f26a9 | -12.83005 | -62.52322 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 593c32ea-4ea1-379f-8025-b5cea1214724 | -12.82633 | -62.52256 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README158.md)
