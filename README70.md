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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 865e223d-0ed6-3c77-9e55-31ef1c3f1884 | -6.35892 | -42.89447 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b16f8996-a3c3-3451-ba8b-e0cd62a62bb3 | -11.67492 | -44.2803 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2547afc6-24ea-31d4-89e8-856f57a5fbe6 | -11.78716 | -47.56487 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07e760d1-469b-35cd-a4ee-578b43c8692d | -10.22732 | -43.02782 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad05b337-ec70-318e-872d-653593607eec | -8.56772 | -48.64376 | 2025-10-02 04:29:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3981a0fa-257d-3db7-baca-64d6a67e3896 | -9.92992 | -50.49244 | 2025-10-02 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b879f254-9ae6-323a-a6b6-ea230c9d9da1 | -6.82484 | -47.97714 | 2025-10-02 04:29:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd1aebfd-e8bb-329f-9d83-63952662d17a | -11.67547 | -45.31817 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 758a673f-2517-3695-ab78-e7ffd7ccf00d | -6.22404 | -45.33475 | 2025-10-02 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7ea929c9-fdbe-3056-a06e-627ef0d96b6a | -10.90498 | -44.30859 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a18f327-3a7b-3d3d-bfd3-0834915f1c27 | -11.80164 | -44.97681 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 012bf93a-55d3-3a04-a465-a367069b78de | -10.28876 | -45.18446 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d9ad26e-dd55-30c5-9ac9-07c65ab4b698 | -10.3498 | -48.21453 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d96e9f3-40ab-3ec4-8c88-bd216514e02d | -10.27027 | -50.33192 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e2691483-9958-3737-9578-83369fe86f83 | -9.93249 | -43.72272 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 353dc8a1-fd75-349c-90ff-5fdef571a093 | -10.26515 | -50.31808 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62719546-8ca8-3e90-90fa-72e27bdabf0b | -11.57934 | -47.66164 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5491643d-2f7f-3908-9c40-3f657adc3388 | -9.93103 | -43.75759 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 22e86f0c-1688-3843-9c40-874cf033f988 | -11.80343 | -44.96485 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 883c0bfb-5ce5-3c66-bc4b-6db4861ed3ca | -10.99597 | -46.59816 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b380eed4-7458-3714-a7b8-97e3a155cf67 | -11.67075 | -47.48843 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76f93701-ecb4-386e-ab24-588a6217df87 | -5.86055 | -47.63123 | 2025-10-02 04:29:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9566f9a6-1c4b-3553-adc7-56f3ee80329b | -11.81922 | -47.68589 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e94c71b-f5a1-30b6-a922-20a50eea6576 | -11.80104 | -44.98079 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c665439-ebb9-3ea9-9e90-30513180f136 | -7.51925 | -44.28381 | 2025-10-02 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e1bb59d-e303-3a07-9ada-45a30d309fb1 | -8.87711 | -46.5879 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd701027-6452-370b-903f-1d6557fa7140 | -6.32109 | -43.04596 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f32113f-c2e0-30d7-a799-89dae1e0b603 | -10.84721 | -45.38759 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce9996e7-b592-3c24-afa6-4710f472e618 | -9.42033 | -47.58309 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f59263e1-27ff-390a-8e23-12f9d6a20bd7 | -11.03545 | -47.83039 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5823ebd-a650-3ccd-99ba-acc5681b1ebd | -11.86582 | -45.0056 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cee73746-bc19-3b5a-ab89-a4760ed334a3 | -11.8153 | -45.00609 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfcaae28-d245-35c9-9d63-a931f46a6105 | -8.74682 | -48.87381 | 2025-10-02 04:29:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 906eed11-f79a-3e88-9634-1592d3e87771 | -10.70579 | -48.57907 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aec3c596-6f71-33e1-b7b8-db436c6b6b94 | -10.69302 | -48.723 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25ea4c94-e8a0-3062-921c-e61a6702f532 | -7.87334 | -45.27356 | 2025-10-02 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe95a16a-ca40-3b38-a4af-3453dec3ee22 | -11.18014 | -47.18909 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28f50752-e509-3e12-aecc-6d7ecfd8b285 | -8.66143 | -47.69664 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f50f327-40da-3c8e-9314-c9615fc46d75 | -8.86267 | -46.57867 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59568ea3-c190-3581-9c5c-39af0a2c656e | -10.81953 | -46.61759 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6a1a23b-e4c5-339e-9666-4d75477b3d12 | -8.55928 | -44.66442 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a834047-9aef-3c1d-a58b-a7fd477a8b3f | -11.7015 | -44.30174 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1ab0acc-3099-3518-81b1-b3b2a35d6dbb | -11.01031 | -49.57611 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb35fbf9-cc32-36b8-a2d9-a57f056600c3 | -6.36664 | -44.64234 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaf7bda0-ebd7-3b0d-a71a-5f3c483fae25 | -10.82173 | -46.6034 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3aceacf-4e31-3b31-a8de-d7738dd7342e | -5.90002 | -45.65092 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4a289e5-31dd-380b-8866-0459d1732bbf | -10.82232 | -46.62167 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 476c59bc-41ff-3b94-a774-892d7d12cdae | -10.85301 | -46.66658 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a0b91c7-55a2-3706-aa13-c989f7b315e2 | -9.00149 | -46.70428 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78be57a0-267a-362e-803c-d3eaaa29cea3 | -7.78786 | -48.45887 | 2025-10-02 04:29:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c10d8ff4-09cc-3356-8eca-fae0edc7cef0 | -8.89934 | -46.62009 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97715ad4-c6c3-38c6-876b-444be9591a92 | -6.71835 | -44.62384 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e11c933e-2aa3-3027-851b-c183d2134d21 | -10.99931 | -46.59869 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 917ad3fb-7d64-374d-9a1f-8888884a7d60 | -10.66613 | -48.52435 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c767fb1a-9c7a-380d-9fbb-02f499ce0eb7 | -8.82587 | -44.78854 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af59f349-f7d9-33e4-aa03-c8c5ebb85ca9 | -6.66652 | -42.79712 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2b9d841a-b521-3320-92ee-e167fcfd04d1 | -7.785 | -42.52012 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b57e41c7-9186-3ca5-b020-63d89f6ff963 | -6.96919 | -45.32278 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 239efd5b-5ffa-3136-acd2-312966f6fa39 | -11.44037 | -43.8937 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ea6f7dc-307d-345e-864f-a34f1fbbfc1f | -9.94653 | -43.72919 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f9c6e7a9-18aa-3793-85c3-a7126b5be98f | -6.78436 | -44.89627 | 2025-10-02 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c019ac1-d302-3c70-9744-b0886e22abb5 | -6.32903 | -43.04281 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64911f4b-64a8-3d7a-8c4f-ed5a20ec4d2e | -11.82882 | -44.98764 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 521667ed-be16-3a69-8941-44e1e8d8da63 | -8.57175 | -48.6406 | 2025-10-02 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25b70e06-9ebb-378d-9981-0db5bf21de9d | -10.82342 | -46.61457 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f12021ca-d138-3d06-8640-66d9475885e9 | -8.81899 | -46.68277 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a9eac4e-892c-39b4-a915-64a20b271b27 | -8.74603 | -47.33775 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4667469-e45b-31bd-9a3a-f04ea980c23f | -6.5514 | -43.92217 | 2025-10-02 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 86b4866e-ed88-3e85-922b-0cd5769b25cb | -11.03269 | -47.82628 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c4a922a-b2be-3997-8fa2-93066f55ec77 | -11.81271 | -45.02291 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 646f7582-d032-3b18-b41c-440b76072eb7 | -8.87934 | -46.59541 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d849316c-576c-3055-86c4-7ca22b169780 | -9.48826 | -45.5463 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 507f49ba-87cd-326e-9808-fd8709d537df | -10.20939 | -50.27142 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 995d0f47-1fc9-3458-8734-35d5d80cd382 | -11.80572 | -44.9976 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98f6af7a-f479-3ef8-8435-28b897896c24 | -11.08385 | -47.71135 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 162739ae-b8b1-34ab-b640-79f22ef9d71e | -10.24708 | -50.31498 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 058a7ab8-8437-35ec-a10d-c8b199bc73ee | -10.6617 | -48.59438 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d45cabc0-178d-3b43-9143-aa7503786e99 | -11.4656 | -45.12987 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f448ba6d-1b6e-3079-ac10-ae9475f694fb | -11.62053 | -45.0589 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f3887f4-892a-353b-8e0d-6b12e87ac394 | -9.95652 | -48.78433 | 2025-10-02 04:29:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 127f3285-c3d3-3369-ad4f-fa57747e4a7c | -11.59504 | -47.21585 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0840cd82-dad4-399f-9746-d37d6256e3e4 | -11.08143 | -47.81224 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fddd61df-d617-3263-bd06-3c511443fa9d | -11.28804 | -47.83167 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2ca3871-cc41-3a5f-ab3a-218a888449f0 | -10.26957 | -50.33612 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 051f16b9-6126-3fdc-b4e8-a10b6fde1586 | -7.30831 | -42.88278 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7beb4878-46cd-3b75-a4a8-558ba54b04f9 | -6.96244 | -45.32181 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 621b2ee3-fa7b-3b15-b40b-04e30ab39e38 | -6.72056 | -44.56367 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f05caf5-29a5-3a88-9352-8c6b45419fef | -6.96863 | -45.32634 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 059c9a2f-5b09-3406-af8a-80adeb1663ce | -10.79118 | -45.3485 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2336911-6575-3a6c-9fd9-9fe71a73dada | -12.22371 | -43.76546 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 740e5d6b-54b5-3129-baec-10ea0d2de406 | -9.95311 | -48.78375 | 2025-10-02 04:29:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0641c51-2ad2-37d7-a2d0-adb248689951 | -7.77148 | -42.53248 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c57943f4-1dd2-319e-8260-591cd79f4b9d | -10.81551 | -46.58819 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 015ada0d-15fb-37f9-8e17-cfeee13e1355 | -10.20648 | -50.26661 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dc4f2cd6-0279-3bb9-a864-248854f6115a | -7.06053 | -43.29709 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8594021a-d387-35f7-958d-ff9211d18c44 | -10.22326 | -50.32385 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 04751187-6ff7-3ae3-b424-112cfcd3a71e | -9.81158 | -48.25966 | 2025-10-02 04:29:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35f39161-487d-313d-a4e8-f8cec890b891 | -11.59251 | -45.05419 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 366cf48e-9cc4-3b35-b736-dac090f0578b | -11.49244 | -43.50502 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97b1478c-ed8e-34a4-ad2b-f5cb2df83a84 | -10.55215 | -43.6488 | 2025-10-02 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README71.md)
