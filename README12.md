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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ef468df-f3a7-3b88-b78a-4d23afdb44fc | -4.67548 | -46.30782 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b661f136-c295-3770-91fa-9eee6f9754ef | -3.59785 | -49.44095 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1c91f4a1-5edb-3a89-a767-18b76f2f1475 | -6.33055 | -41.70107 | 2025-11-07 04:53:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 13023713-e75d-303e-bafd-dce33fb3b2a2 | -3.29332 | -50.03843 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 446f9cd1-5bb4-33e1-b17b-d29bcd1e29ea | -3.85745 | -50.18414 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4859c44b-3eab-3586-8479-58bb330abbf2 | -5.08965 | -44.80486 | 2025-11-07 04:53:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f5555c8c-4957-35a4-9207-bb478cce444f | -2.0514 | -52.5603 | 2025-11-07 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0461aeb-d9b7-3720-95f6-ea020b914153 | -5.58028 | -46.30793 | 2025-11-07 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba4780cb-7825-36a0-9602-9cfb5975813e | -4.6311 | -46.54483 | 2025-11-07 04:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65f7efe9-0026-3803-b946-8e1ef2f11692 | -3.52444 | -47.54869 | 2025-11-07 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1146e88-b54c-38f4-8e58-de55cdf2b548 | -4.45403 | -46.43566 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 96946bc8-4177-3b1a-83d3-8e2a1baf7790 | -4.71076 | -46.43829 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 103f8d3f-42a6-3b55-a366-c5cedfd399f9 | -5.7647 | -40.79519 | 2025-11-07 04:53:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c7df8152-c09d-312e-9976-3f1bd7ac180e | -4.65086 | -46.87387 | 2025-11-07 04:53:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffa288ed-72bf-3bbf-a9f7-f0b866661bcf | -3.28988 | -50.03789 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65a8f7d4-a6c7-315a-80b5-a976a30a5903 | -3.06066 | -49.37491 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8302abbe-c51a-3705-ab0e-ecb219beaa85 | -4.29085 | -45.88541 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 44aed6cc-c9f1-3d90-9dbf-40e1ef54a84d | -4.60819 | -46.43602 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 168e7e73-b230-3d56-b621-9cfd8dd89c3c | -3.60077 | -49.44541 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5258cdd9-f6c8-37ac-9c80-5ec5dfa4ca3f | -2.7258 | -47.38942 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4e3e093-3e83-353f-bf4e-a299cae3fa93 | -3.04914 | -48.71522 | 2025-11-07 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44967e8b-db99-3476-8f9f-9edd6204b928 | -3.60862 | -43.51508 | 2025-11-07 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0099a60e-94ad-38d8-a9fd-2ed63998df53 | -5.55908 | -45.4535 | 2025-11-07 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2e84550-4aa2-31f5-8087-e2f1dac4ec19 | 2.56459 | -50.97642 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2177d525-63c7-33fa-b68c-16825b5f1340 | -4.9405 | -47.45901 | 2025-11-07 04:53:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47c6fbdc-c1a9-3a2c-987a-8f50a4bc79da | -5.3666 | -44.73182 | 2025-11-07 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2df687fc-292a-36c9-bb14-4ccba95fd218 | -3.59372 | -49.44432 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e33392aa-fef1-3a77-913d-a57f6bf8e8be | -4.31036 | -48.07699 | 2025-11-07 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c482d0-02de-3b3a-8742-bbd4a01be624 | -5.75223 | -40.79194 | 2025-11-07 04:53:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b4f9d5f-9eb6-3ce2-852a-b14a440d3553 | -5.64303 | -46.39654 | 2025-11-07 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13807b2d-e302-389f-bcfb-b03902104207 | -4.22808 | -49.3786 | 2025-11-07 04:53:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8212f976-3b96-3629-b334-d7f2e9538cb1 | -3.76824 | -44.00839 | 2025-11-07 04:53:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9e888938-c9d0-3c23-9501-3fc2ac4332d6 | -4.59216 | -45.99545 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e52ab615-54af-3893-bffd-93abe2874e42 | -5.27452 | -47.16437 | 2025-11-07 04:53:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7454d71-904d-3ef9-bb41-3f6c3a2608a8 | -5.69678 | -47.13496 | 2025-11-07 04:53:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8631e785-e3bc-3095-9084-e6ad4cf61039 | -4.71017 | -46.44227 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f539f536-7656-3007-8bcc-d3117ea0d2f9 | -4.40186 | -46.43555 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0530650d-2c56-30f0-9122-69157c15d318 | -3.25343 | -53.28082 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 199cc53e-bbbd-3f08-9398-e35c845bb5a3 | -5.10033 | -48.45472 | 2025-11-07 04:53:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eea8ccb4-9705-3310-9f2d-a0f124844e76 | -4.44862 | -46.44264 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1c27eb83-3987-3f3a-88c3-bbafaef41384 | -3.6734 | -50.48954 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faed8cdb-bff9-3338-b483-d3aad71a9804 | -3.34999 | -53.22639 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 78e1e425-2eaa-3db0-b48f-b0f8cfd0140f | -3.35335 | -53.22693 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2627da3b-dedf-3754-baaa-ff5967b28640 | -4.57493 | -46.40423 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab6574d6-afd7-3c3f-b95e-c4e89d825672 | -3.54102 | -49.43737 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae741815-b76c-31f1-b8e0-1e336204cc37 | -4.7156 | -46.43503 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74313e8a-bf7e-3afe-8fe4-a5215555d86a | 1.35308 | -50.7188 | 2025-11-07 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0223fa5-f3ef-3217-963b-62f4b77d131a | -4.71733 | -46.42327 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78eae358-e3b0-3138-b239-db12547186ae | -3.06019 | -49.37518 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7371d08-d89b-36f7-8fcb-07dce63123e4 | -5.36339 | -44.73578 | 2025-11-07 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2938b43-f954-3721-a7f9-30198d3c4579 | -3.45169 | -48.83524 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b8b84b5-3276-355d-8720-86e22cf35f99 | -4.11056 | -48.0223 | 2025-11-07 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 739a925e-fba8-3a18-8299-5372071209bf | -3.38053 | -44.17725 | 2025-11-07 04:53:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 43999dc9-4347-36ce-b3e9-331219dec42c | -4.64597 | -47.95014 | 2025-11-07 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8502ab14-d3bd-3896-9e7d-0191975f659d | -3.91441 | -44.40813 | 2025-11-07 04:53:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aee3f420-3f9f-30e7-a15d-65bb99f5819e | -2.72517 | -47.39633 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c3fe970-4284-3760-841a-8be4d2b3f9a6 | 2.5684 | -51.00058 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b45a0963-59ec-3d00-914f-78e9a8ae7f6c | -2.94467 | -49.35442 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| df8d3317-b445-3827-8ae7-a37eb5b207e4 | 1.3669 | -50.72017 | 2025-11-07 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50969ee2-9a72-3afa-829c-59d0addbaf78 | -4.112 | -48.01303 | 2025-11-07 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9d270835-9bcc-3d11-aa70-921a49c4b3be | -3.679 | -52.09475 | 2025-11-07 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f273059c-c42d-3574-9816-af28dfded9c9 | -3.59157 | -49.43712 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f3960eb-11b3-3fa4-9c29-643bbd5d596d | -5.27507 | -47.16068 | 2025-11-07 04:53:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1b68fb3-f85f-3d88-bd06-7312e6de68dd | -3.14032 | -49.20996 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 796868bf-a75a-3d05-be13-0ea5cf25e4e2 | -1.69128 | -52.12199 | 2025-11-07 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03f88c90-3c8f-3fdc-ba5b-6dab4acbafa9 | -5.27097 | -47.16009 | 2025-11-07 04:53:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 458a1987-f60a-3b08-9ce1-0b274af9c30b | -2.98419 | -52.82521 | 2025-11-07 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac34eae6-ca12-32a3-af9d-be26f7a5a723 | -3.77693 | -43.98582 | 2025-11-07 04:53:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1d23ecc-6ea5-3233-82ea-a7104a2cf4c1 | -5.46668 | -44.89196 | 2025-11-07 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8f4d831-3354-3636-a5a7-84fc45d548a3 | -5.68878 | -45.99789 | 2025-11-07 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0195b850-8a85-31dc-b024-6b3d03613688 | -4.40471 | -45.68656 | 2025-11-07 04:53:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51e39d0d-b486-3018-b5c1-508b469b48a3 | -2.67116 | -49.44471 | 2025-11-07 04:53:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca209879-db59-3f5b-9b9a-5c22953f311d | -3.43324 | -45.5977 | 2025-11-07 04:53:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf284faa-b2a4-3798-a36c-6c3788dbcf57 | -3.47679 | -49.9179 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2808867-19aa-3d40-840f-bb52e1c5e826 | -2.88187 | -52.61484 | 2025-11-07 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c36757e-954f-37aa-9fcd-d221df47e54c | -2.66767 | -49.44417 | 2025-11-07 04:53:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cc43812-3874-39ce-b8f9-c2a49ecd7db5 | 2.56513 | -50.97987 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58a6ef1a-2f0c-3197-80e6-14acc4bed7a9 | -2.72427 | -47.39909 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58b2c5e6-559e-3a01-a168-cfacd7cdb070 | 2.19337 | -50.85444 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bc46c6e-7d25-32af-a905-b416d72c52e7 | -3.59725 | -49.44487 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 67340816-f80a-32a5-8e68-718049e9c689 | -4.28898 | -45.89796 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 806ff96a-5694-3a5c-9e36-3b2dee280146 | -4.67608 | -46.30383 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 62d19e6e-4a94-3bc9-ac10-d41de823a9ce | -3.11994 | -50.14492 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cdf3146e-8b04-3f43-9ab2-0732bcc2908b | -4.11132 | -49.29195 | 2025-11-07 04:53:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e8bb263-6d2c-341e-8d01-c4a3cacd8f0f | -5.27862 | -47.165 | 2025-11-07 04:53:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eaf0e535-8104-388f-ba32-f81551644654 | -3.91927 | -44.40887 | 2025-11-07 04:53:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93f0f103-2610-3eeb-b83d-5277d4d7e50c | -5.09114 | -44.79462 | 2025-11-07 04:53:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 85915c6a-8a36-340a-b933-39eafc489ce8 | 2.56677 | -50.99022 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cf41e58-d5a3-3813-b6f3-0ac537665787 | -3.03528 | -50.30728 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbd53c86-c3a6-3b04-b1bd-1c5154b93a62 | -2.62823 | -50.07398 | 2025-11-07 04:53:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c932c01f-49a8-3079-9979-8c81f29c670b | -3.5252 | -47.54377 | 2025-11-07 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b782d27-2dd4-3fbd-a8fa-894ec387b97c | -3.17333 | -48.61131 | 2025-11-07 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6b2a64c6-5a88-3a9e-a9c8-d46a2ce4be9d | -6.33116 | -41.69673 | 2025-11-07 04:53:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2a7fe49-ba94-3a28-a934-e160e59a51d6 | -4.78528 | -48.64794 | 2025-11-07 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8eafac0b-8690-333d-8d46-a8aa4435320f | -3.42984 | -45.36028 | 2025-11-07 04:53:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bcd94df6-8ae1-31b3-8e55-14d25b270f4a | -5.7717 | -40.79134 | 2025-11-07 04:53:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7c9559d5-4d81-3b28-82e8-9ef7069d2c59 | -2.7259 | -47.39149 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff1cb715-cac9-34c9-b726-77545cb7d653 | -3.60817 | -43.51807 | 2025-11-07 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4f14e9e-58b1-3f97-ac6c-a3c43b98ff40 | -4.64209 | -47.94966 | 2025-11-07 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4af4432f-2a49-30f0-8237-951d9cee3ac2 | -3.53225 | -47.54985 | 2025-11-07 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README13.md)
