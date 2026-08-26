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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ae59e3b-3dc5-341d-88c2-b014d859b141 | -7.02322 | -59.24136 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdb0fb4a-90a4-37f1-9158-d9f336ed73ed | -7.54208 | -61.29869 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aadd42e5-0647-3b0c-b321-fb0a2ccea4a1 | -7.06752 | -59.21701 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a04e59a5-014c-39e5-ba57-ea5a05eb8044 | -6.69646 | -58.7197 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b9d1733-241d-397d-b6c3-ae8a44b1c770 | -6.69314 | -58.71918 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87a6bcf1-afd7-3088-8c7b-02de659786ed | -6.26232 | -55.42046 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5543713-39de-3e73-b8b7-dc439b1b4a64 | -7.21644 | -60.61346 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9780d0f8-cefb-3749-9b17-e7143f9eb48a | -7.00939 | -59.24272 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7e8998a-cb94-3bb8-9158-e45d5734507f | -6.97676 | -59.25532 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e08c1a2-df20-363e-ba63-999ae7d94038 | -6.1279 | -57.72245 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dd89653-839f-318c-9f17-7663495b1dfb | -6.29529 | -53.58045 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 691b82d3-1b98-399d-8ad5-618785a316ca | -3.12309 | -61.19193 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab37ef50-23ad-3104-99ae-727c16929f83 | -2.88969 | -48.80264 | 2026-08-26 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76fddc3e-7920-3ff3-b0d2-5e57b3916059 | -5.98426 | -55.71318 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bf3e212-bc3e-3f75-87ad-01b010de61ed | -7.51356 | -61.38673 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 78ebf4ae-0d24-385a-82f8-7430357d1667 | -6.60778 | -58.38034 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0c2f1be-59d9-32a6-bbf0-a851a8cfee76 | -6.25297 | -53.37468 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 238a1d44-73f5-3f04-b227-4ee222678452 | -3.49451 | -59.29071 | 2026-08-26 05:27:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72c2c63c-9970-3df9-91b5-bfc298c7df4d | -6.89932 | -59.59198 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bbf2734-fd4f-3eee-8b17-d44061308310 | -7.38752 | -55.15727 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a7c7111-7a26-33b3-b3cd-0ed3419300bf | -6.42312 | -54.93419 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe337fe8-8447-3575-84df-cf2e571a5816 | -6.11909 | -57.82346 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 121ffe33-4f5c-39e2-a80e-f0ea5a4833f7 | -6.72239 | -59.44983 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 125e3041-4133-307e-9574-69bac4daaa35 | -6.63511 | -58.50285 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cdbcbec-d305-3c38-9db9-92449726c533 | -3.20207 | -61.14538 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f8c13c4-73f1-3d4c-8c22-f68632a246f2 | -8.59946 | -54.85979 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0172a37b-69ee-3ad7-8f40-a800ca78e777 | -7.03262 | -59.22506 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67330bf6-8070-399c-813b-3e3fa7a032be | -6.81655 | -59.60402 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 523345c8-e479-3062-8065-78c222cdccc6 | -6.7966 | -59.60083 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3ec5294-446d-3e62-b3fd-91c9d790a0df | -6.16647 | -53.49253 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 666dbbb9-a7ed-3837-9fc6-088465e2a1d2 | -3.53926 | -48.18017 | 2026-08-26 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e71e522e-f2f6-3b9f-a081-60f6b4cc8f1f | -6.83684 | -59.9478 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b4d752d-f706-328f-8acf-5992c30acb8a | -6.89803 | -58.9193 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b3676dc-d999-3583-9c63-3b556954dc87 | -6.93743 | -62.88378 | 2026-08-26 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 799a4009-7574-3662-81f9-6d2466295f2c | -6.28001 | -53.36676 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02d005e6-832b-395e-afc5-f118ac4f02c3 | -6.2662 | -53.37266 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a3bdcc44-6bb1-33b5-998e-2250edeb67cb | -7.0631 | -59.22344 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b4a737d6-73e7-3383-a014-fc7cf1090146 | -6.79093 | -59.7429 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29aef84f-9dbd-3147-888e-95940e89546c | -8.62511 | -54.73717 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 706ae404-0fb8-342d-a260-61994d2a212a | -7.38114 | -59.98787 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 728655f3-952d-3a45-b46a-ca719e432a04 | -6.62238 | -58.50453 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22a78644-8574-370e-8750-a4b5ecba7c19 | -7.37879 | -55.19006 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88e1096f-5746-3eb6-8103-128dfcdd4236 | -8.15483 | -54.98589 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8849948a-4b14-321a-afec-ac7fc8c2a62f | -7.47373 | -61.38094 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d1e9e66-d439-3f30-a3b0-cf54785cd2a3 | -5.14752 | -56.27309 | 2026-08-26 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4334cfc5-dbd6-32b1-9e75-b668929f5089 | -6.13651 | -57.86632 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 425b3d54-c62a-3972-bafb-198f08f2c76c | -6.43809 | -54.96529 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2eec4125-5d51-3c37-ad47-fe829e294b76 | -6.12671 | -59.91744 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae0294e4-d52f-332a-b3da-0073d3787d95 | -7.0948 | -56.54251 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f079cad9-ddf7-3af2-a444-bb049efe850a | -6.26299 | -55.41598 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 011b3ace-7584-3891-bd35-772d23258155 | -6.65231 | -58.50197 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 424bf2ea-0013-3d38-a761-8a9f401f608f | -2.50495 | -48.1394 | 2026-08-26 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0871302-f7ac-3a64-9912-8b2890e6166f | -7.03539 | -59.22906 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe044c8c-d1a7-3dbd-842f-bfb5fc4c1d71 | -7.4353 | -59.77782 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8215c7e2-aced-3854-8f92-ce2df623238d | -6.99611 | -59.24061 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9229552f-3cdd-39e4-9ca7-0657ee591c12 | -7.51762 | -61.38351 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c8d55d14-d07b-32b4-8717-ef8085a153b1 | -8.2745 | -55.53913 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb9b4d1f-6fde-36ea-aadc-2e83daaf8a98 | -7.06587 | -59.22743 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4eb30c37-f1da-3753-a3f5-e94b1ebe4609 | -5.95485 | -53.58236 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 372caef5-b608-3897-be01-e009150cbfe4 | -7.02654 | -59.24189 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af7cf82e-46a2-3d92-aa09-cd82d065d85a | -7.02598 | -59.22401 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ead6b3d-0a2e-3920-bbc0-36a51330fa4e | -7.47684 | -61.37295 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0062d56f-fd99-3a06-bc82-3ae63ceaf3a7 | -6.78705 | -59.74585 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 749926c0-b526-3472-ab9f-3da3eaf890bf | -7.01105 | -59.23231 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 905ee747-1e31-3056-ba9a-f722d60b35f5 | -5.66082 | -46.95344 | 2026-08-26 05:27:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7958c662-18cc-3e55-9b3a-d3481afd999a | -8.14705 | -54.98454 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b9e0e46-7325-329e-bcbf-cbee11175de3 | -3.13867 | -61.18612 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dca96acf-9486-38f5-938c-a839a822d189 | -6.40525 | -60.05555 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b3ccae6-9403-3869-a2a2-df63a4b149ae | -8.02945 | -51.81669 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3720a7eb-9a4b-3a50-9018-c2b5c0f98e5e | -6.9392 | -59.08952 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 088657bd-10dd-3368-99ab-c9ea76d82e13 | -7.37983 | -55.15643 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6ee5c8e2-6dc0-385a-bd4a-4428d1934a85 | -7.02211 | -59.22696 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b68ab2b8-2be6-3297-939e-9378b9a42c12 | -3.77762 | -59.28191 | 2026-08-26 05:27:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e660c9a-fe97-3ece-928b-c90debb016d6 | -8.13442 | -47.50667 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd1e3c3d-06ce-3687-98ed-68893565404b | -7.07029 | -59.22102 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c7b2d263-85c7-3f78-a33b-62eb0cce4f4a | -8.5165 | -55.35503 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c016cca8-56e8-3b90-a004-80465071f12e | -8.13241 | -47.51127 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c666769d-9346-3acf-bbf4-15f2a19e4054 | -8.76691 | -49.97087 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7314709c-0820-34cc-a016-c25140b566c5 | -8.6356 | -54.74932 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70264d41-8b58-38f6-ae19-9edebf4a7741 | -6.80381 | -59.59841 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3b4f2ba-d037-3fbb-82b3-81dadfcf81d4 | -9.03693 | -50.79129 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f35a2af9-777a-325b-8fa9-5d605bce5858 | -7.51134 | -61.3786 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb3ca173-0e5f-3c87-aa62-16aa8af63790 | -7.27489 | -45.35881 | 2026-08-26 05:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 22861c23-da9d-3957-b844-ad10573c6107 | -6.32694 | -54.74 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fad4ac72-f6e9-3ce3-8b6d-db37e36e430f | -7.49849 | -55.34748 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94563964-55a5-3a47-95a5-98016482283c | -3.1338 | -61.19363 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e934598d-2500-3507-8b00-5d0eedf427b9 | -6.33855 | -54.74168 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea18770-b8f6-3655-a0ba-a18ff7392f2b | -7.01437 | -59.23283 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aafff2eb-bf76-373f-afa8-95a4ddf22026 | -7.26442 | -49.86445 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67ff043d-e38c-36fb-8cc2-4b0a1a3fd8c0 | -8.60344 | -54.86023 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aaed65a-86d5-3d5d-9b22-855458704432 | -8.56751 | -55.27433 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f33ea5d8-30ee-3138-85da-f94994fe6e70 | -5.93843 | -57.72649 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c96b35d9-2b59-3ce1-b867-4d4b02cac048 | -6.99945 | -59.26249 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d1ec859-8217-397c-90dd-046eb1c10a29 | -7.52108 | -61.38408 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 5ce65043-44ad-32bc-a0ed-178c731f8f72 | -3.32461 | -54.17953 | 2026-08-26 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f5a7446-6d06-347f-910e-d6306cef4ec8 | -7.39133 | -55.15797 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa4d69a4-e7e5-3db2-a234-1f4f8690c585 | -6.5067 | -55.22817 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d699d1aa-ccb9-3e4b-837a-8c6f72e30950 | -6.50628 | -53.26096 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 31dc6fc0-0250-3d82-95f9-2c121e23dc94 | -6.82322 | -59.41261 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8b63ed2-5331-3be1-aefb-45379379ffa4 | -6.99783 | -59.3156 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README53.md)
