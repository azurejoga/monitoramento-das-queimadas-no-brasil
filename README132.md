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
| ed384c78-b25e-3549-a521-00536369829b | -11.33085 | -60.53013 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3ea6689-9fb1-3a72-a129-c908ea0f847a | -11.32749 | -60.52959 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a39c17a-f4a9-30f8-b1c3-66f0858f877a | -11.32694 | -60.53316 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70fe1320-837b-33eb-89fa-fa8dda2f0e0b | -11.31969 | -60.53567 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b0968d8-36ee-3e51-bca8-1abb79edb4b4 | -11.31914 | -60.53925 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87be4311-653c-345d-ab8a-7400c7d980e5 | -11.31578 | -60.53871 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd894cb6-5277-3952-b9d6-7e8dd3886c93 | -11.30432 | -60.43391 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73e9b585-5ef2-3262-bf1e-97e8d1e1beba | -11.30378 | -60.43748 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29874a4b-5138-33f5-be6d-8c46f0313c68 | -11.30323 | -60.44109 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d27e36c3-51c9-3592-85c9-87bf1f714fa5 | -11.30297 | -60.55508 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 297a8528-fa4c-3ddb-a97d-810fb3bedb5a | -11.30151 | -60.42978 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5562683-702a-3d64-9129-032a666ab0b8 | -11.30097 | -60.43336 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f295430c-4845-3625-8327-bdb46ea4882f | -11.30042 | -60.43694 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddec17b7-2c83-39b4-a911-6b35ec927be3 | -11.29987 | -60.44055 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fd3edee-2ff6-3b6d-bf35-8cf41a340117 | -11.29984 | -60.42982 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e56aba0-575f-3beb-8522-a02dd182047c | -11.29928 | -60.4334 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f59d6e4e-184e-38db-936e-d1724080f8e5 | -11.29873 | -60.43699 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0994fa7-dc42-3aeb-825f-0f84a8b1b79e | -11.28572 | -60.578 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48aadf1e-842c-3876-823b-262626ac1591 | -11.28532 | -60.47915 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d9c6a78-8d78-3409-9f33-69647d4df620 | -11.28477 | -60.48271 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6b5554b-5da0-39ca-aa5a-55a0d807075d | -11.28422 | -60.48628 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4a3b072-9c4e-30e3-8957-e0df544101d8 | -11.28416 | -60.44215 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 131c38d6-15cb-34ea-a7a4-b0f6c68dc768 | -11.28367 | -60.48986 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7eec80e-7782-3909-bb32-5689d54683fd | -11.28311 | -60.49345 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 327fb1f6-c018-3b82-b839-396099ed8b43 | -11.28255 | -60.49704 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c94e6db8-c1c0-3264-a753-ebf8c7f5978a | -11.28251 | -60.47507 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6e3737e-fcbd-350d-85da-479f7087a529 | -11.28196 | -60.47865 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65fcd9b1-0efb-30d1-b8ec-a9e8dacb2743 | -11.2814 | -60.48223 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ddf0ddf-906c-3bee-9783-2890e1b51787 | -11.28085 | -60.48581 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 138f36ce-fa8c-31e6-b323-455bc28a9121 | -11.2808 | -60.44162 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 61ba2f00-4856-3843-b660-717b5883a4dc | -11.2803 | -60.48939 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da0949b7-af95-3a95-80d2-c0f707454011 | -11.28024 | -60.44527 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc21f45e-a44f-32e5-a258-f37be56f1c23 | -11.27919 | -60.49656 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bf6031a-b366-35a3-a1e3-4501e7cb1604 | -11.27915 | -60.47456 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa4c337f-2bac-3e0e-b0ef-512072700517 | -11.27864 | -60.5001 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ddcb6843-25dd-39e8-87e3-50f2d1c9a9d7 | -11.2786 | -60.47813 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80963800-942a-3aec-97a2-f4cf7c4740c6 | -11.27809 | -60.50365 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f62a045b-ce1d-3ac6-84ef-bd5f42b377a3 | -11.27804 | -60.48172 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 36d3d307-c346-316c-a7aa-929b0481805b | -11.27749 | -60.48529 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 929bf410-870e-32c8-b718-471b0727f099 | -11.27745 | -60.44107 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20ebd88c-6ee0-322b-a2a0-cf770d1aed1f | -11.27689 | -60.44469 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb9b29fc-f707-3416-af73-7c0879707a96 | -11.27583 | -60.49603 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 337a8c1d-44b8-3fb4-be89-b44300781e14 | -11.27528 | -60.4996 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3871e945-72de-3c29-bbfe-9215117b431d | -11.27525 | -60.47756 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d344eb66-e4a1-3dc1-872b-ae3a253288ce | -11.27473 | -60.50315 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b96fa5f1-92fd-38cf-a20b-0dd9b7878030 | -11.2747 | -60.48115 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6cbd8a0f-b286-3ccd-a10b-e68703d28572 | -11.27418 | -60.50671 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2f569c10-9924-339a-89de-2a89cc0dc4d0 | -11.27414 | -60.48474 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f23c3a57-14d6-3e08-9834-b58f9d594ba5 | -11.2741 | -60.44049 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5864ae52-3ee5-3bec-b343-2e6a78819f74 | -11.27192 | -60.49908 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4fe24db-a081-3de8-a4d5-1145032a6200 | -11.27137 | -60.50265 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 711133ac-5d2a-38da-9076-16f6f6df5915 | -11.27082 | -60.50621 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f2f9814b-d289-3192-91df-ce6788dc2671 | -11.27079 | -60.48418 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7db452b7-e530-3a97-a529-3b5fe378d76e | -11.26801 | -60.50214 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb39677d-7525-34a2-aa3e-fdcf122047ac | -11.26746 | -60.50571 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08202021-7435-393c-8973-8efdc3823935 | -11.26744 | -60.48364 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f94db01-c65d-3d34-8a35-4479cd43104f | -11.26464 | -60.47947 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7628cc3-13ab-3ab7-8e8b-20dcd87c72db | -11.26356 | -60.50875 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5516a428-3d37-3d06-9d76-4511914530b1 | -11.26075 | -60.50469 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f737f16-0171-3106-8138-79feabbbe735 | -11.2602 | -60.50824 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a717dd30-b607-3c0b-a908-f41739ad79c1 | -11.29354 | -60.33666 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3196f8ae-824d-3e94-8d91-13ade03d2726 | -11.29298 | -60.34028 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 399304b4-fe66-3543-9d82-77f8ec1c6001 | -11.29018 | -60.33612 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64daff0a-345e-3e2c-80bd-0c222a7f9774 | -11.28962 | -60.33974 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0773efd7-e953-393f-88d6-03d4860a8c82 | -11.28289 | -60.33867 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d681b743-d9eb-3f0b-9c8e-2ee0d66617bd | -11.28008 | -60.33455 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95919a2f-f48a-390a-8744-3d60ab3d10d7 | -11.2796 | -60.38242 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 291c0d47-43cc-30f2-9d32-096c9e125f72 | -11.27905 | -60.386 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cc7adf3-7178-3b4d-bbd1-663c66127f23 | -11.27735 | -60.37471 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26a93fbe-82ba-38b8-a458-898443009c0d | -11.27679 | -60.37832 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3db62788-d5ea-382e-8253-e25d29bf436d | -11.27624 | -60.3819 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 650169c5-903b-3270-9dbc-4cbb25a8171b | -11.27569 | -60.3855 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12c1187a-145f-3fe6-9175-785ce3f7e51f | -11.27453 | -60.37061 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbc1485f-145d-3656-a434-77941c18b290 | -11.27398 | -60.37421 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3180e57-be31-33f3-bc23-8ff744460616 | -11.27342 | -60.37781 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c09a75cf-2be9-3dfb-b090-b49f962bbf70 | -11.27181 | -60.41069 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8058e0ed-65f8-31f2-ba12-2fd6c14fab15 | -11.27172 | -60.36651 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5d0768a-90c7-33b7-b85b-17adc5656392 | -11.27125 | -60.41427 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21112080-5300-3a78-90bc-fec1de799037 | -11.27116 | -60.37012 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 511f5911-b97e-31f5-aa9b-ea4c3a584a06 | -11.26835 | -60.366 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac849daa-15f4-34f7-8d93-d4951d285cad | -11.2679 | -60.41373 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 53ff02fd-8a32-3e97-b079-37a820e22132 | -11.2678 | -60.3696 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbdedbc5-562e-3540-b685-ca85dbdde964 | -11.26499 | -60.36546 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a28fdad-161b-32c6-b056-e92cf044678a | -11.26454 | -60.41317 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa2b31d0-f46f-3f43-8e89-4a2408be7003 | -11.26443 | -60.36908 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 519f4408-a5ba-3907-ac98-5f4636d75728 | -11.26162 | -60.36493 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 923d5c88-f372-3f4f-979a-d8a174fbc59f | -11.26118 | -60.41261 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 237bd69a-ca5e-36dc-9db8-e8fcfad370ee | -11.26107 | -60.36855 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6452555-85e7-391d-a6fa-4d0e39aa8722 | -11.25838 | -60.40848 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b9d298a-aaa6-38d5-989d-c42c01abbbb5 | -11.25783 | -60.41207 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b610a12-a4b1-31a8-bf53-43590c143cd3 | -11.25557 | -60.40435 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff1ff00d-da13-3060-98d6-1de0532f352e | -11.25221 | -60.40381 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8e85b7b-3812-34fe-bafe-10404f59593d | -11.2494 | -60.39967 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56333b76-4e94-38fd-be0e-2df566eba43d | -11.24788 | -60.22922 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61c66552-271c-3417-8b47-4c00e921d611 | -11.24659 | -60.39553 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a31db46b-62ac-3502-9ba8-8cd655e4a591 | -11.23987 | -60.39444 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8232d69-4667-3c28-8a5d-908c603b7fea | -11.23273 | -60.23799 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f011d876-bb1f-3ad0-abf7-f5c11558f1cf | -11.21559 | -60.23146 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d23b40f9-c8bf-34cb-9731-4d02bebae950 | -11.21503 | -60.2351 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 687741b6-16d6-3efc-8e56-83d3a36b6001 | -11.21222 | -60.23093 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README133.md)
