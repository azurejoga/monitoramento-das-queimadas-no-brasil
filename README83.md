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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95206c3f-5337-317f-b988-f79cc1593a02 | -13.20203 | -51.21215 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4d2a837d-e9bb-3443-825d-039f0ae95060 | -13.20119 | -51.21664 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31921b45-00cb-3f7a-85bf-e1cf7754cc56 | -13.20036 | -51.22113 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a8d0c48-e257-3c88-bd91-cd43156dce3e | -13.02032 | -51.21786 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9130d6e0-4e55-3650-b45a-ee9d4fa8f6d4 | -13.0195 | -51.22237 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 40611d84-6fb0-3e9b-9c26-e3da907d8cac | -13.01588 | -51.217 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 7e8562ea-c5ea-31a1-891d-e705f5a62d51 | -13.01505 | -51.22151 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 8cbb4b18-53ab-3bef-87e8-c1b4d7aff30e | -13.0106 | -51.22065 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 99025eea-e327-3064-8ee0-2b48c8d1782c | -12.99642 | -51.22256 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b702201e-36e7-38f3-bc50-f8b4012d416d | -12.99281 | -51.21719 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b270984d-8da2-3f33-9f1f-3ccdce17b2f6 | -12.99197 | -51.22171 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b3198308-8be4-30fb-a32e-38a1978a02dc | -12.98752 | -51.22084 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 424f16fc-1c75-3048-862b-89575def8557 | -12.97184 | -51.21595 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1969bc92-b92b-3e6c-9506-6f647c28de46 | -12.96973 | -51.21738 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 55a271b0-6389-3220-a5ff-a84f0d995c61 | -12.96888 | -51.22191 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd746e9a-52ac-33a9-8a43-b3568719ba51 | -12.96739 | -51.21509 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 46707e40-0b34-34e2-ab0d-90dbbb722d55 | -12.96657 | -51.21963 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 14370257-8e28-3b16-ad16-189ddf4d5bb7 | -12.96612 | -51.21201 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f79162f3-64f3-3081-9ad4-a05a7511cc63 | -12.96527 | -51.21654 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a6dabfaf-e148-3da4-b379-6e49d7d5aacb | -12.96293 | -51.21424 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| d9fcc139-2a20-32a0-b52b-ae673de35084 | -12.96212 | -51.21878 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 036982a8-003b-3a14-a7cc-fbb4956e6a38 | -12.96082 | -51.21569 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 257c8a69-cd4c-3f78-b008-217308976d8e | -12.95997 | -51.22021 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c031e471-f442-30eb-82b1-dece0e8a92dc | -12.95767 | -51.21791 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 49668435-e772-35c2-9a2e-a57b37b6103c | -12.95685 | -51.22243 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5b789e8b-db47-316b-9688-e350dbb86b93 | -12.95552 | -51.21935 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8f4de0fe-fb8e-3dc4-a1b4-10c52b8fc948 | -12.93424 | -51.19463 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9585f836-7cf4-3c8d-bc3c-5ece0f22977d | -12.93342 | -51.19915 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24e5286f-68ac-3587-996a-f12bd0543069 | -12.92979 | -51.19377 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 410736ca-a6cd-332c-9681-7c8a5c790eb7 | -12.92897 | -51.19829 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3c9d156a-5199-3fab-b370-3b140fef78c2 | -12.92815 | -51.2028 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 995864bd-40a9-3189-8371-431f09eb55a1 | -12.92534 | -51.19291 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 55077a2c-eb1c-34b4-a8f2-986420b7850d | -12.92452 | -51.19743 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a7b009b-c1ee-3b9a-9bf0-102dbbb07cfe | -12.9237 | -51.20195 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41e336b8-c823-3a87-a27f-48058781c6dc | -12.92287 | -51.20646 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99ec15d2-f960-3fe8-a497-1162cba856bf | -12.9209 | -51.19204 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 480b768a-2bc7-34a6-b900-c037f84ab460 | -12.92007 | -51.19656 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d2806931-dc46-3378-b86d-2baf0420c458 | -12.91925 | -51.20108 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5583d56c-7ade-3fc2-b7ed-5ad4842c5ecf | -12.91842 | -51.2056 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41077bb7-f3c6-332c-bdc1-307fa04767cc | -12.91759 | -51.21012 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62c215ea-2612-399a-bbce-137db14fc165 | -12.9148 | -51.20021 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| bc2605b8-968a-321d-8078-2e5788a822f7 | -12.91397 | -51.20473 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 433051f8-204e-3452-8b78-64a1fbfd2ddf | -12.91314 | -51.20926 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd96dc31-ba32-34d7-be0a-7a4c1a76f292 | -12.91231 | -51.21379 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1feb7186-2b2f-3e07-9ff2-32aad53c569e | -12.90869 | -51.20839 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b9ef44b7-1ecb-3ca6-ae78-e16500d41212 | -12.89283 | -51.21936 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e05fb3f0-2e67-3d96-bb53-5a1411005b10 | -13.01898 | -51.25038 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 016504b4-3b51-3db7-93f6-d0fee8df8a00 | -13.01867 | -51.2269 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 52a5c8b6-4538-35da-a145-07029583062a | -13.01815 | -51.25491 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 62e09452-796c-32cf-9849-ea6fed6aa1f4 | -13.01784 | -51.23141 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6e99aacb-0e82-360e-9c78-d367c29fe975 | -13.01732 | -51.25946 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39e085d9-4d61-3c47-ab6a-54a35e9a4613 | -13.01701 | -51.23594 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e118d1d4-d097-3e57-9fa3-eaad9f905363 | -13.01626 | -51.31593 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 3a052b20-d99b-33f1-95b1-485b16668925 | -13.01618 | -51.24046 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3c77f4de-a2f3-3ec8-81a9-faf9fa04fde5 | -13.01566 | -51.26855 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c44847e2-3e8e-37ba-a95f-3a964ca587f2 | -13.01483 | -51.2731 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0cc68ce0-bf94-380f-a082-bf5ed61d73ee | -13.01458 | -51.3251 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ea0f79e2-e0e5-3152-a0a1-e232691a1f49 | -13.01453 | -51.24952 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 4376a8bd-8c18-3e56-a0f1-6800af7bc7eb | -13.01422 | -51.22603 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 7d4d4fe2-684f-35b0-b2d1-60b045ca6c8c | -13.01369 | -51.25406 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 2701de6a-3f08-3be4-80f0-d63ece556f45 | -13.01339 | -51.23055 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d6ba3d40-bbfa-3fef-a901-41b5eed0c11a | -13.01286 | -51.25859 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6069ee9-a8a0-3170-a48c-091da5e1dfa9 | -13.01262 | -51.31049 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| cf04d2c8-93d9-3bf9-8120-67bcc46b2c1a | -13.01256 | -51.23507 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 21540a99-0ab5-3742-9652-61d1a871ae75 | -13.01203 | -51.26314 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0881217-21ab-32c4-9110-20da89ee2586 | -13.01173 | -51.23959 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c84193c-a6a7-379b-800c-025d01d68f5f | -13.0109 | -51.24411 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 54b41fba-5f60-36b3-8a4e-d6155981de95 | -13.01039 | -51.34808 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9874805e-92b2-3c44-986a-2fc855348634 | -13.01036 | -51.27224 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4038e172-125b-366b-9017-1f0376d18042 | -13.01011 | -51.32423 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f9fa9682-aeb8-3511-927e-2403a1620fa7 | -13.01007 | -51.24865 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 3a04e453-8dcd-3e81-adf3-373ebc63ebca | -13.00977 | -51.22516 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 9b57ce39-91c9-3671-bd10-1ba3985bcc74 | -13.00953 | -51.27679 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5dffe815-4774-397e-8029-88db7ef83cae | -13.00924 | -51.25319 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4daaa375-5285-3cad-a770-b428451e95fb | -13.00894 | -51.22969 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4faf58ce-2009-3edd-812b-bb4eb37af4ba | -13.0084 | -51.25772 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 72febde2-1718-3769-9dcd-e0f3aee0f42f | -13.00811 | -51.23421 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c6efea36-f995-340f-aaed-b85ac22417e4 | -13.00757 | -51.26227 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 97b6b1c4-88f4-3613-a323-942d6077f523 | -13.0073 | -51.31419 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 251efdc0-8c44-3942-8a6a-f9912f96bcc0 | -13.00728 | -51.23873 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9ded1bba-d678-34cd-a87f-94d142b88d32 | -13.00645 | -51.24325 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7af42097-3823-3bf2-8b88-2fc55a21de3a | -13.0059 | -51.3472 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab14d2fb-d023-3afc-9f85-20a480b902f8 | -13.00563 | -51.32335 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1f45547-094f-3a98-b578-38bfaea7b260 | -13.00561 | -51.24778 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 25860780-2aa8-3599-af58-43a2d8af40b4 | -13.00532 | -51.22429 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| de019f1c-9a86-34cd-85f3-3cd0fd4e6c21 | -13.00506 | -51.27592 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 808f416e-7395-32ff-bf99-5c5a6cbdccb6 | -13.00478 | -51.25233 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1104e28e-0fbe-31cc-a6fd-cad192b2ed95 | -13.00449 | -51.22882 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 85d2f9ea-14b9-33d4-a333-fd0fdba60860 | -13.00422 | -51.28048 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03f740e3-d205-3fc0-ab70-736683a10b8d | -13.00394 | -51.25686 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 06e8b358-6e18-348d-a32f-56cac4c9f6a7 | -13.00366 | -51.23335 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 4233d081-b4ae-393a-971e-cb53d9334d34 | -13.00311 | -51.2614 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 4cf8ad94-7056-3ba9-bf49-9f2fa61c0646 | -13.00282 | -51.23787 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 82f12955-9156-31ce-b2e8-c7655928fdbf | -13.00227 | -51.26595 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5686df2a-ebdb-3b6c-ad61-df9c2d69ddf6 | -13.00199 | -51.3179 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6b299517-7360-3c84-aab7-3631df85196a | -13.00199 | -51.24239 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f1dc84da-6bf1-315a-8d45-f1124c3e26d7 | -13.00144 | -51.2705 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9fd3ab03-250a-3a53-9cc3-4a61720b3bd3 | -13.00116 | -51.24692 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee4a594d-f926-337d-bfb6-ae00eb9020f1 | -13.00057 | -51.35093 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a4316e23-d836-3a26-9f72-2d0af797ca42 | -13.00032 | -51.25146 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README84.md)
