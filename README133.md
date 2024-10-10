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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35d59570-8035-3a3b-867c-ce3c7eff5b58 | -7.0419 | -59.40211 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c18d7792-6215-3653-b517-53a9f937c601 | -7.03991 | -59.3984 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 589d386c-4e96-3424-b039-a9ab214f4d46 | -7.03927 | -59.36673 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f7fdb300-74ba-3702-9370-ba7ff7ce25f8 | -7.03802 | -59.40153 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d9cda5a-79b1-3c7f-8431-5b1ad765f915 | -7.03539 | -59.36614 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0ee3f10-50aa-3353-9b2c-8aecff4a4fc8 | -7.03466 | -59.37102 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fd4076c0-f99b-3e71-9a41-9cd58882e573 | -7.0315 | -59.36557 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cad22951-c9a9-3bf4-867e-14236bf90283 | -7.03101 | -59.39544 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 484c37bb-31e1-3752-94f5-830ccee37794 | -7.03078 | -59.37044 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0de651a4-f44d-35ac-9d40-6bff9d391ebb | -7.02762 | -59.36498 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b8a7be5-7a77-334e-b3d3-564a6ea1e05e | -7.02713 | -59.39487 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6230ec0-070c-3e4c-a448-8c525c7451d3 | -7.02252 | -59.39918 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 396d3635-db15-361c-a280-df96bbea3126 | -7.01793 | -59.40344 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbd58b85-1e16-30e2-a681-42dedc59223c | -6.80553 | -59.34722 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a09232f-7f66-3664-bdb3-19cfba1057ea | -6.8048 | -59.35209 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1525075-1a62-3a9d-b44b-d3858a45e58a | -3.63024 | -60.21223 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0738ad3-2d68-3cff-bacb-116b8a8562fc | -3.52764 | -60.00665 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e611e9a-3633-3ddb-99bc-31794c5e491a | -3.52406 | -60.00611 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18795988-e380-31fc-b4e7-898b937f948e | -3.46294 | -60.61414 | 2024-10-10 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd214d87-e178-316d-94cd-2022c8356129 | -3.46234 | -60.618 | 2024-10-10 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffa14560-95a3-3349-b5ba-b675bbb799d2 | -3.45837 | -60.59764 | 2024-10-10 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3dcba8f-bdbc-3a33-885c-f269c6b2ddbb | -3.45241 | -60.63616 | 2024-10-10 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a33d28d8-bab4-395c-9eef-e3d6f84fa92b | -3.09341 | -61.0259 | 2024-10-10 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 551665b8-8c67-3fcf-a215-f09a40faa428 | -3.09294 | -60.98413 | 2024-10-10 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7537ddd-4cb1-3551-a5f5-56a8820bb46b | -3.08481 | -61.05854 | 2024-10-10 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f59b4f4-5809-32d0-bf66-2dbcf275a5b6 | -3.08139 | -61.05804 | 2024-10-10 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5681525e-ae6b-3d47-83e9-add594dc6190 | -2.22393 | -60.09495 | 2024-10-10 05:36:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87b10d1b-8a59-3641-891f-e96851b746f5 | -4.59974 | -61.11368 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c07a81a-5c34-3100-8abc-d5e94e49c7b5 | -4.59915 | -61.11745 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75dd51a7-8960-3046-bb75-1192baf716f5 | -4.69735 | -60.74645 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b74517dc-c721-3fc3-8936-d1810443b5dd | -3.887 | -60.59282 | 2024-10-10 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 185a1add-f334-37ba-bdfd-b514e34047ad | -3.77785 | -60.12645 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 571749a7-5f50-3801-9429-99e345dd5dbd | -3.67734 | -61.06394 | 2024-10-10 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af6a3265-b72d-3ecc-afff-fba8d7d5d00b | -4.71643 | -60.80923 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64d11113-3608-30e1-8561-a2c96e811247 | -4.13555 | -60.27178 | 2024-10-10 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8532090c-cbd2-384f-8cdb-1ddd5c8cb1d8 | -5.49742 | -60.45955 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd4a7cf9-fe94-331a-94c3-f8397d0c5523 | -5.41346 | -60.61039 | 2024-10-10 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8932fc6c-d9d8-3398-9123-2a1886e94bbe | -5.501 | -60.4601 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed8cb319-d9bf-335e-9531-a557470108b0 | -5.41701 | -60.61095 | 2024-10-10 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 451ad15c-4fea-3028-8072-1aae34987eb1 | -7.64505 | -61.20293 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e21a5c23-ad89-31ba-adc7-7202f95bec9c | -7.64482 | -61.20559 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8968581c-6a32-3bdd-855e-ddf55c06f910 | -7.64444 | -61.20694 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4332d89-d23f-3603-bf5e-d3af146e3ce4 | -7.64422 | -61.20959 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f6ef09f-0438-3864-bab3-1ad23e5723b1 | -7.64383 | -61.21094 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84642ed8-42d3-3335-a0b2-d0af23cfba00 | -7.64128 | -61.20504 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9890539c-e5ce-3e42-aad4-428cea0a9dd6 | -7.64091 | -61.2064 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07b23e9b-7202-3539-889e-ef47124be151 | -7.64069 | -61.20905 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b72fce6-1f46-3814-9ef7-2854a9a88507 | -7.6403 | -61.2104 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e880ad6-809a-3c2d-a716-5481ab1df9fc | -7.42492 | -61.53594 | 2024-10-10 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4a5647d-881b-3c8f-80a4-518bb53a0fe2 | -3.29547 | -61.60225 | 2024-10-10 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e55149fd-56fe-3106-8e5c-7b25cef6e219 | -3.29491 | -61.60583 | 2024-10-10 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56a38ddb-781a-3ddb-86dd-b73d4fc5be65 | -3.29377 | -61.59103 | 2024-10-10 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6744ed65-0548-3741-a0d7-c7187e7fb7fa | -3.29255 | -61.51019 | 2024-10-10 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1a3cc35-7925-3f51-9932-7ce697f878fc | -3.29042 | -61.59051 | 2024-10-10 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d70872f-ca0e-3417-99bb-98d50c9c1fd0 | -3.28918 | -61.50966 | 2024-10-10 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02d4ccca-fd99-39b6-b559-0f7771503686 | -3.0445 | -61.68363 | 2024-10-10 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e75a9137-620e-3cb0-8b5b-6a2f8de4383c | -2.99703 | -61.42104 | 2024-10-10 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45b1963a-e243-344b-8f8a-6c022a182c37 | -2.93717 | -61.76135 | 2024-10-10 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 066c41b0-a3d8-32a0-96d9-45be0de8dda0 | -4.51434 | -61.94276 | 2024-10-10 05:36:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 720702ce-2a73-36bb-ab91-78c36892d857 | -6.27133 | -62.47864 | 2024-10-10 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d386580-1864-38fc-83e3-e31373bdd7ec | -6.26799 | -62.47812 | 2024-10-10 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04cef0f1-0ce0-373d-8d3b-3328580909e7 | -6.24719 | -62.21915 | 2024-10-10 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3de60d75-99a2-3106-a20c-72f53816a888 | -4.39455 | -63.41027 | 2024-10-10 05:36:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c505d37f-5f35-3da9-950a-84424ed6741a | -4.39125 | -63.40976 | 2024-10-10 05:36:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0378bac-9601-3eb9-80a0-483a39e45830 | -8.23872 | -61.17879 | 2024-10-10 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00ac72ad-5221-385c-b1ce-bfd0d284ed0d | -9.96245 | -55.33345 | 2024-10-10 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4c9cd16-0729-310f-8785-b16ce7aebcd6 | -9.96201 | -55.33678 | 2024-10-10 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d19062a5-1b2e-3e68-83fc-3334cec8eda6 | -9.95226 | -55.32845 | 2024-10-10 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04695d62-5514-3b05-9f5a-b7d55698114e | -9.95164 | -58.12163 | 2024-10-10 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b89493e-f245-3bc3-b3fc-ccb8f4fbf965 | -9.98638 | -59.87278 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba554e5d-b059-3e4f-9495-52529443860d | -9.98174 | -59.87717 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c91edf4b-cdfb-3642-8d7f-67d07aa4014f | -9.9527 | -60.10518 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4f0e7fe-5f3e-3d3c-aeae-61494d9336d8 | -9.95258 | -59.80062 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b3612cd-8bd7-3f1b-b81a-891d540620c3 | -9.952 | -60.11004 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22b4b15d-0f96-32a2-828e-54080c8c7103 | -9.95019 | -60.14956 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e4dc140-8f95-3b79-b92b-70a5538c86d3 | -9.94884 | -60.10458 | 2024-10-10 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 116efe32-6f77-37bd-81f1-f85c44cfd1ce | -9.13689 | -51.49528 | 2024-10-10 05:38:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1b07e60-a565-3411-b4e7-ae64bfb0d7cb | -9.1362 | -51.50089 | 2024-10-10 05:38:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52620ea4-b4d3-3fbc-9f12-8afc66e634e4 | -10.67246 | -51.09435 | 2024-10-10 05:38:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bcd53670-cb48-39b5-b983-ea9820435ed9 | -10.41759 | -50.71017 | 2024-10-10 05:38:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3c283f7-770d-3627-ac39-a76e9aa3603f | -10.41676 | -50.7173 | 2024-10-10 05:38:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22950c43-2b52-3a97-b484-7f4c130fc3c2 | -11.29574 | -51.04437 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9288149c-c8e3-37f8-8a04-239d945b7b3a | -11.29496 | -51.0514 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8c14572f-0abd-3f10-bb71-eb7e6ed1cb9f | -9.3374 | -52.54931 | 2024-10-10 05:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6d731f00-f036-3042-ba8d-19ec47e7b681 | -10.82622 | -53.75248 | 2024-10-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b31d40e8-3e54-3d66-a01c-a1946b647767 | -10.82297 | -53.75372 | 2024-10-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac889eff-7dfb-36b2-bbd5-425d2238878d | -9.81911 | -54.53307 | 2024-10-10 05:38:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83c9a827-6226-3e01-b49a-9944a7a9a8a6 | -10.62019 | -54.23793 | 2024-10-10 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ab4f67c-8f1a-3203-b78c-5dd5d3158010 | -10.38516 | -54.1783 | 2024-10-10 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02f7df48-a647-39a7-a89d-a975f0c602ec | -10.37935 | -54.17772 | 2024-10-10 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6fe018d-c085-3559-8b22-3bdef3202520 | -10.37885 | -54.1818 | 2024-10-10 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 967e81d0-a620-326c-b7da-9baf6a65ed1f | -10.31263 | -53.70628 | 2024-10-10 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50ebb420-fd8d-3586-a6be-fc067677b363 | -10.31209 | -53.71076 | 2024-10-10 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ba38b5a-d4cd-3173-b96b-fc5962c7560a | -10.30666 | -53.7056 | 2024-10-10 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4431c7dd-7bf4-38f7-b5f4-8da6349a3f97 | -10.30613 | -53.71001 | 2024-10-10 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82479c1a-3f74-34fe-a81d-1fe8a4f9979c | -10.22203 | -54.30565 | 2024-10-10 05:38:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 851369d2-cf39-3086-97a6-0bb73ef18dd6 | -10.22062 | -54.30358 | 2024-10-10 05:38:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bc09078-6975-3a48-91eb-91acf0a442fd | -10.2163 | -54.30497 | 2024-10-10 05:38:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f9a5a83-de77-3e68-9ef8-1320d5fd56b6 | -10.21437 | -54.30692 | 2024-10-10 05:38:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71851077-6afb-3df9-9864-8e04c59ea7d0 | -11.6064 | -54.6889 | 2024-10-10 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README134.md)
