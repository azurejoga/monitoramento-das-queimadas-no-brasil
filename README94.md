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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6016fb46-7f10-3e15-bfc8-9f7185e2670b | -20.34887 | -48.86279 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56f3378d-11ab-37e7-bdb6-7b7184c028c2 | -20.34541 | -48.86213 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f4de47f7-9012-395f-b390-7505108357d6 | -20.3447 | -48.86621 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3bd96145-b341-3ed7-951a-96ebb12bb6f6 | -20.34359 | -48.86232 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bccc817b-c6f9-3d25-86ac-7f337808879b | -20.3429 | -48.86641 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69ff85e2-c652-3334-852b-cb12af4eb042 | -20.33943 | -48.86575 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd2f1b79-c801-335a-9bbf-8b4365a379d0 | -20.33527 | -48.82702 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d374b1d-2a21-3960-a567-2321c42bcec3 | -20.2714 | -49.51371 | 2024-10-09 04:17:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e75d31b4-aae1-3dd7-8312-9a29b48978a8 | -20.35938 | -48.7689 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47a5c7d5-2ab3-30df-ae99-a4ab49f3ad43 | -20.24988 | -48.88641 | 2024-10-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e17ff9c-218e-31e6-909c-08b7bf1a9f0c | -20.14696 | -48.82987 | 2024-10-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b96a9a04-3e45-3296-a67a-1751bd286d33 | -20.14491 | -48.82104 | 2024-10-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c25b5d78-769e-3af7-a7de-d40058db7a1a | -20.13853 | -48.87862 | 2024-10-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b366e6ea-e0b9-362e-92d6-9a829341b1e4 | -20.12778 | -48.84838 | 2024-10-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d29d3e47-21ad-3153-b0a5-3785c283593f | -20.12709 | -48.85242 | 2024-10-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d6bbef3-8ba7-3bed-82cc-7b000b648135 | -20.12608 | -48.84692 | 2024-10-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 922e609b-a136-3f21-9c30-d5f07904fff6 | -20.12538 | -48.85096 | 2024-10-09 04:17:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57dc484f-3511-32be-8582-9330848a0fa9 | -20.45349 | -48.83672 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b48f4bfa-8bd6-3b68-9d01-26f07c7a9331 | -20.45003 | -48.83603 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 851d2919-21bf-3e44-9a15-f42333e8db92 | -20.77769 | -48.56147 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77b16190-9d35-311e-8b41-32dce500c102 | -20.77569 | -48.57332 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82250277-6388-3490-8837-0022e4736581 | -20.76818 | -48.57597 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c3ad3ae-16af-367a-b1e8-8e0a05d290f9 | -20.76544 | -48.57132 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8d384a5-7bf8-3c3e-a568-bf2158c83671 | -20.76477 | -48.57528 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eaa5e0a4-d879-391a-953d-8e223fd2e396 | -20.7647 | -48.55492 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fb2d201-8c60-3931-85f3-d0efea2be290 | -20.75787 | -48.5536 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77d2a487-ffe4-3e2d-8185-e3994a22f4bb | -20.75575 | -48.52458 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73b238bb-1156-3bb7-8ccb-3be050dbf472 | -20.75513 | -48.54899 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60ed827a-1e75-3670-92bf-7c75217581bc | -20.7483 | -48.54765 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a79fac1a-f21e-3594-805e-16aee3705a44 | -20.74557 | -48.54301 | 2024-10-09 04:17:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f1c4c9d-517c-3c5d-9f66-a510ebdca65c | -20.3795 | -48.78904 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a133f136-bdf9-318a-8e1e-212ceb007168 | -20.3713 | -48.73323 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| deefc644-79f7-3649-ade2-30b888a0a177 | -20.36785 | -48.73257 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82ac88a2-e536-3592-ac6c-7b634536e0df | -20.36687 | -48.72452 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9b93608-6b84-35cf-835e-ddfacef44621 | -20.36619 | -48.72856 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf3eee4e-ee8c-3da1-a388-80c107c4bf27 | -20.36579 | -48.72385 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d75f740e-87f7-3db8-b630-9b85dbdfca19 | -20.36551 | -48.73258 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b81d35e-a452-329f-ae12-232f5541e694 | -20.3651 | -48.72789 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fac7e76-a7b7-3b0b-93d9-b24bd48f361d | -20.3644 | -48.73191 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b35c3a1-d843-343a-aa97-d914098b48f0 | -20.36342 | -48.72387 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02a717ef-391f-31cd-b7c6-4f6cc268358c | -20.36274 | -48.7279 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d543ea44-3962-3544-863e-84e58e4814a6 | -20.3407 | -48.73187 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 906605ef-8d6a-3a28-9ab1-fbe7739be094 | -20.3593 | -48.72723 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| be313b79-3d09-3263-bd33-5f606149462c | -20.35879 | -48.78495 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b95b8aa-c7fd-3ab2-b55d-2462cd6ef5e1 | -20.3587 | -48.77294 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 185122b0-c708-3bc7-9f3b-457323a948f0 | -20.35862 | -48.73124 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 798e2ffa-34ae-3507-9765-606aff2c7952 | -20.35812 | -48.76818 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96d779ea-7f7e-3f70-9940-a16492e574ac | -20.35802 | -48.77695 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 81b0621b-e18d-3a6c-8ffd-e0dd399b427d | -20.35743 | -48.77221 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7538c9-9dbf-345e-b4ed-9a72136ec16d | -20.35735 | -48.78098 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 151df0cf-498e-3e2d-aa7d-2b6b9c1b7663 | -20.35673 | -48.77623 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28eb0ae8-e4f0-35f4-8afd-972cc939b875 | -20.35666 | -48.78501 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 829234a9-3f89-3720-a9bf-e178f91bf146 | -20.35604 | -48.78024 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db563b52-6ffa-363b-8e4f-c7ce9e4c351b | -20.35585 | -48.72654 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c4af668e-1451-308c-8f34-65b9b71a6923 | -20.35534 | -48.78427 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6b52a5c-6179-3957-b44f-1f2206325a62 | -20.35517 | -48.73056 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b2e2f9e6-95c7-3a7e-836f-7774765fbf53 | -20.35377 | -48.7178 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b687a95b-cbee-3cb3-9d7d-e5048a3f4b3c | -20.35321 | -48.78433 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24684b5c-d6cd-3813-bdba-0a8086113a32 | -20.35309 | -48.72181 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34a4738a-19ff-3a9d-80f5-9e7604754fe6 | -20.35241 | -48.72585 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67daad2d-9fcf-30de-bdd9-f53aa4584587 | -20.35172 | -48.72988 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0914d362-1bd7-3cd1-97ce-1373643daab0 | -20.35033 | -48.71711 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 561ed648-58cd-386b-80e8-e8bf6007f94e | -20.34965 | -48.72111 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4896c6b5-866c-38cf-90e3-4b81177abd65 | -20.34896 | -48.72515 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7064dd2-a743-33aa-bc46-c997300c79eb | -20.34828 | -48.72919 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5a15ae2-4190-3e2d-8ece-1997d4b8a7c2 | -20.3476 | -48.7332 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 035f8fda-da6c-3782-b6c2-bc5ba2a0dc1a | -20.34621 | -48.72042 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21db7363-3c62-326e-9a8a-4bd919c745d1 | -20.34552 | -48.72446 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 3c6684d1-3771-34a0-9d81-8fa5ab3dd97c | -20.34484 | -48.7285 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 133.1 |
| af174a1b-16fd-3f7d-9393-0fa6ad554cda | -20.34415 | -48.73253 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 74d1918c-5f46-3f1a-8fd9-919789feb36c | -20.34347 | -48.73655 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 26037c4c-abef-386a-97cb-8fbfec79eeeb | -20.34276 | -48.71974 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 174cb67e-04c0-3766-ad3b-61147b8dab60 | -20.34208 | -48.72378 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 9f8bf7a8-85ea-3d71-b5a9-3c43d12fbc8f | -20.34139 | -48.72783 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 86a8be31-95bd-3690-890e-4433519e5b55 | -20.34002 | -48.7359 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 26.0 |
| a42a21bd-c111-3a85-a65e-128af8887fd9 | -20.33863 | -48.72311 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ce3199c9-8142-376d-8d67-3dc980306a84 | -20.33794 | -48.72717 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a4045fa2-9705-3f0a-b8ba-9631c788eea4 | -20.33725 | -48.73121 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24e45586-b079-3a83-9370-c22c78c81318 | -20.33657 | -48.73525 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60a11600-ca2b-3bcf-bb2e-2b7d95d62166 | -20.33518 | -48.72246 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 09473584-eefa-3ed9-93e4-0268c63de144 | -20.33449 | -48.72652 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8f9ac323-afa6-33b1-a1f4-3fe8fb4f8634 | -20.3338 | -48.73057 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c78a8337-ddf6-3ebc-938d-718b7ee29b89 | -20.33173 | -48.72182 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f10776d8-2849-3ec4-b260-c7bc87ade930 | -20.33104 | -48.72588 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| bb3a4326-c167-34d1-bfa9-8f0fbac30abf | -20.33035 | -48.72993 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2355320a-fa64-35b5-a21d-cf108adaa58c | -20.32827 | -48.72118 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9ea3e1ec-e4fd-3a75-b339-6779c8b56a96 | -20.32758 | -48.72524 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 53c6bb86-91f0-365f-913e-81eb017ff1dd | -20.32689 | -48.72929 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1b5405ff-4910-3db2-9870-5d57c7118725 | -20.32413 | -48.7246 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a44ae34a-76b9-38d8-9525-a39bdd82a69c | -20.30127 | -48.62937 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b3a08a9-edae-34f2-9cc6-a4f0eaa98a7f | -21.06511 | -48.56934 | 2024-10-09 04:17:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a26428f8-5c07-372a-8815-1e99279fe464 | -21.56121 | -48.50745 | 2024-10-09 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c72c29fb-df62-3ea8-a7c1-afc7ccacfc4e | -22.29399 | -50.00217 | 2024-10-09 04:17:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff11381c-6f71-3787-aaa2-a621f7ced53e | -22.28969 | -50.00568 | 2024-10-09 04:17:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5c7f6505-f259-3e6b-9f9e-4456d89483cb | -21.8303 | -49.15805 | 2024-10-09 04:17:00 | NOAA-21 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7f293e64-0f5a-38ae-94f1-9a655dfcba94 | -21.8296 | -49.16208 | 2024-10-09 04:17:00 | NOAA-21 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7630f347-33ec-3c80-9c2a-8587c102c92a | -21.82685 | -49.15738 | 2024-10-09 04:17:00 | NOAA-21 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 66ce2e3b-30ef-3ae5-b8cd-e0c9c9f5a9a1 | -21.82615 | -49.1614 | 2024-10-09 04:17:00 | NOAA-21 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8936f274-a3bf-3a94-a408-bb6b9a8362ce | -20.96325 | -49.347 | 2024-10-09 04:17:00 | NOAA-21 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4891196a-3837-380d-bbd5-694a887c312e | -22.5806 | -49.21935 | 2024-10-09 04:17:00 | NOAA-21 | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README95.md)
