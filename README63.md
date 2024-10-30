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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baa3c4b2-a157-33ed-b68d-85f9cc9101d4 | -2.89877 | -51.48061 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a9facde-3405-390b-895b-23e61a1e3300 | -2.89821 | -51.48419 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 576c6f38-4ea1-32ba-b978-919e6bb1dd33 | -2.88506 | -51.65521 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a7cc6b1-4ede-30fb-a525-e64d9136968b | -2.88449 | -51.65882 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01832cf0-29f9-3649-9123-f76acab424cf | -2.88167 | -51.65469 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8d15142-cf72-336a-9912-f64506ea5e15 | -2.8811 | -51.65829 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cac4cd78-b5c5-38e1-acbd-8f32afe2429c | -2.88095 | -51.31004 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79515b91-9553-36fe-be7a-2eeff61a8d3b | -2.87759 | -51.30951 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8134f68f-9465-38e0-a1bc-3d4b7b6ade8a | -2.87703 | -51.31306 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2defcbae-9762-3948-ad49-410a1fd268db | -2.87423 | -51.30899 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80d6c0c5-5e5d-3bde-8c3e-93075261d3c3 | -2.87367 | -51.31253 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 259dba06-e20a-36a9-b31d-83def10e4f9e | -2.84398 | -51.80497 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3e33800-19de-3d42-9e94-c0498d6cb935 | -2.84057 | -51.80443 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69c566f8-51b9-37ec-8036-1e8507c83fc9 | -2.83999 | -51.80808 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10723edf-6cdc-3186-9fc3-b69b9933287f | -2.83941 | -51.81173 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8003fc8e-26f7-345b-b441-9edb2cf010a4 | -2.83659 | -51.80754 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85b16185-32a5-32f9-9e5e-478b51a241a8 | -2.83601 | -51.81119 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| feaf6035-7825-3f25-8b2a-f7e2665d744d | -2.8326 | -51.81066 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f152adc0-a0d2-3ba5-9d4c-74652884b79c | -2.81328 | -51.95446 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2648f1c5-ed18-3a5e-8bb2-46f6f0d10306 | -2.80986 | -51.95392 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48c4eb0c-7460-3447-baa0-d5d44585fb2e | -2.80643 | -51.95339 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7723e3db-98f2-37e4-8b01-ba9bbc1b4a5a | -2.80585 | -51.95707 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bc6e9d4-f638-3022-af1a-e32296de8c91 | -2.80301 | -51.95285 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f806fda-be9c-3aae-953a-a05fafae9ca6 | -2.80242 | -51.95654 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b81e3b3-6b24-38d1-b56a-13153fb808e7 | -2.80193 | -51.80587 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b6129d9-96b1-3ed5-91ef-b7d865834039 | -2.79959 | -51.95231 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ceb9081f-fc12-3d02-b168-f61ff786dc04 | -2.79852 | -51.80535 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e612170c-4ba4-3bfc-af51-4066c269457a | -2.79511 | -51.80482 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70c0432e-5e13-3f47-902d-45c4d17e507a | -2.79383 | -51.46093 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efdf8875-45a9-3973-9182-2ab278a70b49 | -2.79327 | -51.46449 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd50691a-778b-3c0d-960f-51766d5da63f | -2.79046 | -51.46039 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3b3f8c1-7e02-3c76-b1aa-6fa656e606bc | -2.78989 | -51.46396 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1610546-9c00-3365-9396-ae6fc0eb6191 | -2.7853 | -51.95383 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a980282-32f6-3ab7-9964-a912c8e71f3b | -2.78471 | -51.95752 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09902644-bdf3-3cbb-bc51-c910198dfd16 | -2.78188 | -51.95329 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08017d47-3294-3191-98c2-4ae6c7857f86 | -2.77893 | -51.97175 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 199ba707-3c4e-345a-99b9-392e14b19a2e | -2.4202 | -50.50398 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4c9a3e0-4059-395b-93ba-d23503630163 | -2.41884 | -50.62093 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 279d2872-5795-36d4-aadd-404721bc60d9 | -2.34784 | -50.61696 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6879d23-ad1f-366f-8a19-8a632b6ad168 | -2.32852 | -51.24987 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4969b3b1-8b64-3a40-ab77-5081ddfed732 | -2.29029 | -50.66447 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e31ff85b-1c45-33fc-b3b0-0bc3695d3ec5 | -2.2875 | -50.66047 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df3e3e9f-2d66-3caa-9197-dd6b8c0d36cc | -2.28472 | -50.65648 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| add5c11a-3b89-3a52-9538-b49094b65cab | -2.28417 | -50.65995 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce81361e-4319-31b7-a933-2047011b8f7e | -2.25148 | -50.69405 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbc8a889-a7af-3a80-a6fd-5774c3f693bc | -2.24705 | -50.70049 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99527590-4b9d-3cd1-bc2b-9c4074c831ab | -2.23708 | -50.72033 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f19cf46a-72e7-3740-bf0f-f46876857657 | -2.2343 | -50.71633 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87a56d54-0402-395c-adec-c707bbf02a07 | -2.23277 | -50.81256 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a339c015-d37a-36ab-a466-0cacfb7ef6ea | -2.20118 | -50.96912 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aec55d0-3816-36bc-bdb2-a86a39975640 | -3.18583 | -51.25243 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0b6db26-251a-3f92-a08d-f2a57e996fa6 | -3.1848 | -51.35779 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9154983c-fb85-31e9-87b7-55106422efe2 | -3.18467 | -51.21616 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f47eb14-ac6f-3806-b17f-2ead786c7340 | -3.18424 | -51.36133 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53005ba9-b238-3fbd-a835-d1c8d337f1cc | -3.18411 | -51.21969 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 542a4af3-69c0-35af-87e7-08072f4753e6 | -3.18349 | -51.15829 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d10d3a9-d97b-3caa-9574-76680d1ebd5a | -3.18132 | -51.21563 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7686e2cb-6927-3896-911d-bf016d4368ab | -3.18076 | -51.21916 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a8ffa03-976f-3587-9f8d-f7b5c8740c4d | -3.17792 | -50.59396 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 03bd2414-9251-34c9-8fb0-18f3c5e745f1 | -3.17738 | -50.59742 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5ad3ce8a-89bf-38b8-ba40-3fbbd068b818 | -3.1746 | -50.59344 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ded552a-9266-3e39-9664-2412b4bfc13f | -3.17406 | -50.5969 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8504c114-fc4a-3991-a7dc-1a70ea657c68 | -3.17351 | -50.60036 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4b575969-b904-3ddd-96b2-b0750b373653 | -3.17128 | -50.59292 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 439dcdd7-c628-3943-bb34-1e9dd6520a2d | -3.17073 | -50.59638 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 69c49e70-df5d-35c1-a2cd-3d4ceb6ef808 | -3.17019 | -50.59984 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 996445e7-ce30-3096-bf09-42b13d0b5520 | -3.16795 | -50.5924 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 99e4f60f-1c29-39b4-aa5d-5220a85cbed9 | -3.16741 | -50.59586 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1002563f-baae-3161-a0c9-20838394da15 | -3.16686 | -50.59932 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc97d159-4b70-3035-9b01-cdc43d1b1a7d | -3.16463 | -50.59188 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4d30542-9907-3899-8505-30e865124bd9 | -3.16409 | -50.59534 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1a7cdfc-4b3d-3447-bb32-348b4439b2d4 | -3.16131 | -50.59137 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e66a3caa-7ca6-31c4-bb94-807d059de127 | -3.16076 | -50.59483 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af2069ac-ae3e-3d03-863a-3f6355910508 | -3.16027 | -50.61956 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72a99e6a-5723-3a57-a47a-1a98d4291595 | -3.15973 | -50.62302 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a2874633-3aa1-3151-9875-478ada922bd2 | -3.15918 | -50.62648 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a66f0f5a-0f6f-3853-810e-45acdc88ab00 | -3.15864 | -50.62994 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8fc1b263-b1ca-300a-988f-579a442bccd4 | -3.15798 | -50.59085 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58052be1-8772-33f7-8c91-d616084ed10e | -3.15744 | -50.59431 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76ce917d-200b-3155-9cbd-3bc0fa8db176 | -3.1564 | -50.6225 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3fc035d6-2df1-3750-9d01-7127964ca915 | -3.15586 | -50.62596 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3624e550-2772-37f0-a6a2-7e35f6c369d7 | -3.15531 | -50.62942 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6a7c1aa9-21ad-3d35-9680-453ce71621cf | -3.15466 | -50.59033 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e6e7822-736f-34fa-b908-12b6b3406562 | -3.15412 | -50.59378 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0074ae4e-e003-33e7-87c3-a4d56e7b3eaf | -3.15134 | -50.58981 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e24810f5-7f43-31bb-83c3-524d8c447528 | -3.15079 | -50.59327 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb9e529b-8cb9-397e-b2ce-d0d523e4e2ac | -3.11043 | -51.10007 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e809561-6647-3d92-9cec-b3c4968d7189 | -3.10987 | -51.10357 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad836e37-30a5-37f7-a247-9d46d76716a0 | -3.10931 | -51.10708 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d76813fe-3e98-3db7-859a-9cf6bdb151b2 | -3.10708 | -51.09955 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4d177772-dd5f-3728-ab66-566b89f297e0 | -3.10653 | -51.10305 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a43a5f2-2c25-3377-950a-1bd35a90e056 | -3.10597 | -51.10657 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65ef2972-fe45-39a1-ac4e-bf52778c21ad | -3.10522 | -51.09947 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a704f4aa-d81d-3a70-8a5b-1fa45d905532 | -3.10467 | -51.10298 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fe528c55-3e7c-39b0-b8b8-430b51b6303c | -3.10411 | -51.10649 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4167c97a-67fe-3012-a260-5cb8f3ad9141 | -3.45169 | -52.00351 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2223076f-c23b-3dcd-aea8-c227cfe77c36 | -3.44827 | -52.00298 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e3eb61f-1599-3c03-9010-08be25eb76a1 | -3.39447 | -52.05465 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc6e651a-b7ea-3ec3-9bb5-2779ddb12d75 | -3.40893 | -51.5053 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d17374e0-b85c-3995-9b28-e05f2daa4cd7 | -3.39762 | -50.80608 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README64.md)
