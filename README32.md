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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 938ad457-16ef-38b3-abcc-c286d995316b | -2.44969 | -53.70819 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bbe3d44-357a-325d-b3ee-bfe4c19324a5 | -3.09119 | -54.07774 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d178fee7-266a-3fb3-9744-3c65fbea0d9d | -2.96244 | -53.72692 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9258f5d1-b149-3105-8c08-c93b5b035bff | -3.10908 | -54.07792 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| beec7db3-2fc0-3ba5-9637-9f2bc8aa8d1f | -3.09935 | -53.74463 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92225fc0-e748-3d2d-8bbc-5d64991ccb9f | -3.08808 | -54.07249 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f66dc17e-0da7-3656-86ca-ddbdd9d2bbb1 | -3.52903 | -53.93822 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cffd63e3-c0d1-3401-bad1-c84ffc563de0 | -2.82559 | -53.07095 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d82d102f-d20a-3f8e-8e1f-0b6e22559740 | -3.46371 | -52.71699 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 419b2101-053c-3adf-8f34-63b212cf51ed | -4.38272 | -47.75483 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 10c8c447-3e76-3ddc-b7e8-8fd2f7b83fa4 | -3.12727 | -54.06154 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ce3c0da-9fc6-3853-9db3-bca243b4439d | -7.59502 | -46.63813 | 2024-12-10 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 479f4017-8e6b-3735-b140-66d1adbd3ab2 | -2.99498 | -53.0481 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47d4b181-9500-38b6-9b5a-db77aaf5bbfa | -3.53215 | -53.94374 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ce2b279-e1d0-349e-824e-ce6fbb7fa248 | -2.9139 | -52.95833 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f2cf837-08e0-31dd-89ae-6f9a808efcc7 | -3.08024 | -54.04723 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8a1573c-993d-3189-8d41-d09a21ed7d28 | -7.5992 | -46.63288 | 2024-12-10 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d64c989a-7858-36eb-b879-31861ceb3e0d | -3.0687 | -54.24572 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6389155b-5cfb-3b88-8f88-034dcbe0e899 | -2.81358 | -53.03973 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5993b79-dae5-3796-b740-ba022295cfc3 | -2.81344 | -53.04392 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d55d3e3-4adc-3956-a167-3ae50065a882 | -5.70865 | -46.54404 | 2024-12-10 05:16:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df3e3769-9b15-3209-813e-dc180c7c38a3 | -3.05662 | -54.24841 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a4672a2-bfe6-3355-b38b-05059dd48f98 | -3.67725 | -52.37789 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49a12895-1a26-3419-9b38-cb1232e1bf0b | -4.39284 | -47.76945 | 2024-12-10 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f847298a-a446-3025-b021-995ba31961cc | -3.08408 | -54.04782 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 685a40a0-6d0e-3c7f-8b5c-9a7dbf778b59 | -2.80984 | -53.06485 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac61c9d2-d476-3461-8783-b24d886e7c41 | -2.46024 | -53.63986 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f456263-bad2-3d84-858a-f0891960e21d | -5.92012 | -48.0516 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bea29553-5ca1-3624-9fc6-f390913a7d62 | -4.88986 | -48.05139 | 2024-12-10 05:16:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 386738c5-27cf-3391-b837-04619b929fc4 | -3.08537 | -54.07898 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6c3a94e-5bff-30ac-9cd9-082e5f1443fe | -1.60164 | -54.63886 | 2024-12-10 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3494d53f-4e25-30f2-bffc-5bfa92a8a7ea | -3.45885 | -52.83337 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 833e6b67-c0b1-3e41-9963-b6d8d450fd86 | -3.46511 | -54.67791 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91090f0f-a682-372c-be93-af369e96b1fc | -2.82243 | -48.085 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 467b5dde-e870-31ec-b821-2ba29d6eaed5 | -2.21978 | -53.7222 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b087657-2370-3d29-a229-441ae134311d | -2.57816 | -53.67996 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 162e9695-3cc1-387c-84fa-7fa7555ac332 | -2.78657 | -53.24189 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14a4229d-6311-3c65-a212-8e9896d83f39 | -5.71445 | -46.55061 | 2024-12-10 05:16:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b639aad1-6161-3cc6-a392-42dfec318741 | -2.83589 | -53.05785 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 19e3c77c-9877-3a0e-8a92-b28c4cf987a3 | -2.79611 | -53.23968 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5400045-9d59-31ee-a49c-76efa08316ea | -7.09096 | -59.55159 | 2024-12-10 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f381569-a3c1-3474-9755-95f73f78df4a | -2.03975 | -54.43644 | 2024-12-10 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dcbe91c-c0cf-33dc-94e4-366f2eb40724 | -3.04973 | -54.24282 | 2024-12-10 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f2f6d27-fb5f-3e94-b242-80b3042a8661 | -3.10491 | -53.25093 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9a244ff-fb00-3947-b7fb-0183cea2c63e | -3.08352 | -54.07657 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e26f22bd-e9f2-329b-8705-cc8c5c816e7f | -4.54546 | -48.01878 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 311a3506-40c9-3ab5-95a7-dd83a59dc581 | -2.91334 | -52.96189 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce2ab6e4-1558-37d4-9908-2a8bfe312e72 | -2.94025 | -52.50758 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3abadf42-a48b-321c-95a4-5ba86c4f618a | -3.16049 | -51.47985 | 2024-12-10 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8085a3fb-0b12-348b-bd5b-48d3ce954d09 | -3.10978 | -54.07327 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17d9ab3d-0d06-34ce-94e9-769a6c8b40d7 | -2.31193 | -54.00384 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 37944ae4-659b-3c18-bc50-038c405c69d0 | -2.81444 | -53.0619 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1eedb9b-7b44-343d-b690-63b21ad7996e | -3.10596 | -53.24385 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43bd6e61-2060-39df-afa2-6156a5bc3737 | -3.09732 | -53.24658 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 198c064e-494f-30ea-ae26-dae8667b9b85 | -3.27286 | -53.04459 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8be5a539-d4ef-3be7-a3ee-a85d16461e02 | -2.61979 | -48.0597 | 2024-12-10 05:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c63af51-6a5b-3cb1-bc0e-69c3b19fab60 | -3.60765 | -53.49363 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f67958e2-f27e-3a5e-a7ec-e42c1c66a47c | -2.98551 | -54.06464 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3094df26-b466-3afc-80fe-64654019aa98 | -2.814 | -53.04033 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bf2491e-88e6-3121-b453-c9387e52e59e | -3.60357 | -53.13167 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2de17337-ff5a-3905-9485-3e4a487fa181 | -2.99962 | -53.04515 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 664c6f69-02dd-3977-a70a-c5da5b839aa3 | -1.33325 | -52.22739 | 2024-12-10 05:16:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 696d38a5-99fa-3889-8693-7c1a2f4e2ce9 | -4.4683 | -48.11205 | 2024-12-10 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07ff5e98-7026-3280-841f-7dd86b575960 | -2.81359 | -53.06959 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6fee8ac-3e80-37d9-bae0-fe05a97d1884 | -3.34969 | -53.80613 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ad76f66-45b1-3e72-adf1-4277d4099648 | -3.57228 | -53.01926 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc8c7bec-9089-3384-a57f-411f7492294f | -2.82774 | -53.05661 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61eceac5-b6f4-31d0-b9f4-0ed4580c789d | -3.10071 | -54.08136 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4bd774a-784f-3539-8d7d-714663224f5c | -2.36544 | -53.87131 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 186c7525-b370-34ef-ae21-0c0e12556385 | -2.8212 | -53.04458 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c67c0f6d-6807-3c8a-84f7-62ca6bf33bbc | -3.09575 | -54.07367 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0ada73a-c262-3d17-a145-af93d0e12bc1 | -2.08174 | -53.40109 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 611ea775-e81d-33e9-a4f0-65d469e12c0f | -3.3011 | -51.63179 | 2024-12-10 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72e87bc8-8dea-30bd-b17d-360f96244085 | -2.32406 | -53.90075 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6a842b2-7769-3a51-8ba2-bed206a2bd6c | -2.81712 | -53.04396 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a031b280-f3e1-3d1c-b548-b058643ea989 | -2.35642 | -53.7943 | 2024-12-10 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91bc48b5-8a0c-3b48-91ce-1705b6d6d5f6 | -4.67602 | -49.50419 | 2024-12-10 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b38423b-d260-3dd2-905c-de6f2f4b55b5 | -3.77754 | -50.05387 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 301c55cb-03ab-362d-a4f3-29a9903379e6 | -6.65471 | -54.93443 | 2024-12-10 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e58248bb-c3a6-3bda-86bf-c3e4cf8d6f21 | -3.81783 | -50.95112 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e55c9d88-1b9d-3fd3-b5cb-355be15b5f96 | -2.79536 | -52.86243 | 2024-12-10 05:16:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 340a0b72-15fd-395c-98df-a8261bc52d25 | -2.81391 | -53.06548 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88fc3dcb-8571-3cb3-bad7-573209ba295f | -3.08881 | -54.06783 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41ce816c-99f7-3273-81e5-a1cf65ca330d | -3.12246 | -54.04143 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1245e47d-6b88-3ca3-a395-cc464a67e1fb | -2.88362 | -49.01455 | 2024-12-10 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9cf1b23-5039-3540-a4e3-a23de972c440 | -3.10837 | -54.08258 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fb23c65-60ee-3781-9c5e-51450b9d8999 | -7.59579 | -46.63241 | 2024-12-10 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92fb2c79-bd4f-35b5-b2ab-946c97f852a5 | -3.9084 | -53.44645 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d034ae9-c874-3f9c-92ed-1624b37e3a7e | -2.82152 | -53.07032 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b6b8369-9d17-30df-8365-5c5bb714c00a | -3.8737 | -50.36493 | 2024-12-10 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8954c45f-a953-350b-8ca4-b6cb40418e09 | -3.12318 | -54.03666 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bb6043c-f924-3187-be51-d43c467ab1a8 | -2.83535 | -53.06145 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 27040928-57b9-3e7a-ae72-7000305b5143 | -3.68178 | -54.31977 | 2024-12-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25f3277a-4fd8-366c-94a8-d6726b486eb6 | -3.09374 | -54.07549 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f431a85-ef4e-3f8f-b7d6-88c6dac2a470 | -2.83481 | -53.06503 | 2024-12-10 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e3e0d40-1d9b-35f0-b3b1-cfece81398bd | -5.91796 | -48.04924 | 2024-12-10 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 769ec6ad-3e89-376f-a17e-dbaf906bf4f8 | -3.92907 | -53.58577 | 2024-12-10 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84f7ed99-b93d-3bd1-97b8-2b1483dcd186 | -3.17876 | -55.0164 | 2024-12-10 05:16:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78a20a5a-c6b7-377f-991b-53e054a3a5ac | -3.09502 | -54.07832 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 290a612a-06a4-3f01-b55a-5c02b85fb178 | -3.08677 | -54.06963 | 2024-12-10 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README33.md)
