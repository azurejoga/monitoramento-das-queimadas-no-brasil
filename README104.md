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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81387a1d-79f1-3191-beaa-82bd352014ac | -11.5563 | -49.90828 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb91bdd1-6669-39e9-90be-31742f7211b9 | -11.55284 | -49.90775 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 362283ce-f802-32b1-b5c9-00e2d5f96df7 | -11.55226 | -49.91161 | 2024-10-10 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 609e12d0-effe-3314-b674-25cf5214dfdc | -11.20616 | -49.93138 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12c941a0-f7ea-3619-87da-13e1a3ce1e9f | -11.1527 | -49.73098 | 2024-10-10 04:44:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42e85613-4e17-30b0-9072-64fcc7754228 | -11.11594 | -50.64151 | 2024-10-10 04:44:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 397e74d4-a540-376b-9837-d5ae0f77fa01 | -10.86705 | -49.76431 | 2024-10-10 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f657a0ce-8c1a-3f11-a1ce-f64d2e25e5d7 | -4.97344 | -50.66553 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fab2b3d9-154d-3d16-9140-744d3deafafd | -4.92105 | -50.56609 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67894985-1954-3b06-9bf2-06a814e6f990 | -4.87473 | -50.5377 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da897b7a-96c6-3d4a-9e31-714bff1ae170 | -4.87419 | -50.54114 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ada3ca77-e19f-305e-b816-7c2e00d2b039 | -4.87365 | -50.54458 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88c004dd-952a-3a6a-9917-e8da2bd325c4 | -4.87311 | -50.54802 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5a92096-4017-3d39-8c20-b4b6f695b64a | -4.87088 | -50.54062 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71c022d9-f3a0-32e9-a02e-7f18c1236fc8 | -4.87034 | -50.54407 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13c51d6c-a1db-33a3-ae06-329daf750321 | -4.8698 | -50.54751 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0b49020-83dd-3469-b084-c6bea5bb94cc | -4.84491 | -50.92104 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b238596-103b-3976-8381-e2b6a4a54668 | -4.84437 | -50.92449 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63698e21-7163-3777-b9a6-de1e729a840f | -4.8416 | -50.92052 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cac74e28-5119-37d7-b186-d9d520d487e4 | -4.84106 | -50.92397 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f1d894a-9cba-340d-886b-de4001f31edf | -4.8383 | -50.91999 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92f13a6e-8af0-3d64-82ad-9d7b729c920e | -4.83469 | -50.79243 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 229d8904-2a7e-3cb5-b690-f16dbf47662e | -4.83415 | -50.79588 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad2f34ae-fafa-37c7-b332-89c0dc00fce5 | -4.82838 | -50.91845 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9faa8d5e-ffe3-3641-8b93-905738a3187d | -4.82808 | -50.7914 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 58d9d8a6-6ca9-3fca-af50-ff0102355ec1 | -4.82754 | -50.79484 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d337ab57-8f9c-3768-9fb9-90c91c29f46f | -4.82478 | -50.79088 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e3134a6-ac8e-3fd3-9e27-f29380042ba8 | -4.82423 | -50.79432 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 456fb1b5-10cc-385b-8e30-53a771db9b75 | -4.82369 | -50.79777 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ebdaa35e-8ac5-38b4-9dcb-f7eade6f76fb | -4.81991 | -50.82183 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1cd1881-431a-3b43-b368-a5642ca4359c | -4.79567 | -50.75769 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 468f80d2-2b88-3c4a-a24d-843ec8ef99b2 | -4.7189 | -50.8797 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d81a6db-841e-3cb6-8fd2-aa924cbd5b10 | -4.71836 | -50.88315 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbdcec01-ac93-3d29-8ab5-ebea2cbba765 | -4.61038 | -50.31585 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c04688a-09c7-3e47-88f6-fdbc1f14f2c8 | -4.49906 | -50.54872 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fec2dc75-1625-3238-9a66-e8daf1d827bb | -4.49852 | -50.55216 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 517de8c6-9496-396e-98bb-1661823a6439 | -4.48176 | -50.46496 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 351dad15-206c-31f2-9017-8803bf222887 | -4.44993 | -50.49524 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fab48d8e-022b-30f3-bc16-6418ee7d1619 | -4.44939 | -50.49868 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53de1312-678a-3888-ab17-0baad5ad33a0 | -4.44608 | -50.49817 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a1a2bfe-03a2-3b22-a36f-3113026fbd80 | -4.43573 | -50.73624 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b7910c6-23a1-3456-a64d-93000a6aa097 | -5.0583 | -49.95012 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c8ad1f5-4cb9-3b8d-92d4-d412d8228458 | -4.95852 | -50.04503 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a924ba64-0953-3270-acc5-e2e6d777737d | -4.95174 | -49.76183 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc972c14-50c6-3710-94ec-cbf8d62d82d1 | -4.9512 | -49.76532 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e20fad2-18ec-3745-8caf-d56dddf8cc89 | -4.94896 | -49.7578 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a289f17-9e44-32d5-a8e1-5c7f5cae5656 | -4.94842 | -49.76131 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cd17df7-a5d4-320e-bedd-4585b9a83f12 | -4.94732 | -49.7683 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ce302c5-b92e-3b50-8ee0-37a00e803e9f | -4.94366 | -49.85716 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4945a35-6fb5-3a1a-826c-38d653977f85 | -4.94311 | -49.86065 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 871a3055-f5a2-3387-bbd4-fafe926bdc2f | -4.90825 | -49.86592 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7211d93-f073-3fcb-8ec9-90942795a626 | -4.90458 | -49.9331 | 2024-10-10 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb307044-557c-39dc-bc4c-5b0995e209c8 | -4.53077 | -49.54255 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9b6fc36-209a-3e84-b64d-2b20a83c066f | -4.46703 | -49.56153 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d29e901f-50d8-37f9-b484-072a9168c09b | -4.38052 | -49.78779 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29d39de7-90fd-36cb-a591-09f3bfcf094e | -4.37998 | -49.79127 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8aacca1d-156d-3e60-9cdb-c5dd22c8fa28 | -4.39668 | -50.74773 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24d3cf25-9962-39de-af71-caa4f6165104 | -4.39391 | -50.52547 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c3249be-4989-3cdb-a5f7-9be89b863d57 | -4.3906 | -50.52495 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae394bf5-0cc0-33ae-94ee-ef11d055e0b7 | -4.3482 | -50.51482 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1b83121-92dc-3a45-b38e-b553b05b98fd | -4.34766 | -50.51825 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cc78eaa-d4ad-37e9-a8e5-210ea4a842c5 | -4.26926 | -50.73502 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 394b4dff-84bd-32e0-b55d-539c1c40065c | -4.26595 | -50.7345 | 2024-10-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8afbacb-9d0c-37fa-a2ba-b3b1ab6b6afb | -6.55597 | -49.88372 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59f82f37-43be-3b48-ba8a-61e05085b713 | -6.54809 | -50.10992 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bfdf307-2484-338d-a30a-5c40b81ac4f6 | -6.34769 | -50.65229 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbaaebbd-b83d-3681-83c1-382fc7fda3ca | -6.32232 | -49.9888 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe7dfeae-313b-353a-985b-ec6642c33d1b | -6.32178 | -49.99227 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9617bb61-b7c7-305b-a63e-d0bb28d8a75c | -6.319 | -49.98825 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b68d533-fbe9-309b-b6f1-718c12a103e0 | -6.31567 | -49.98769 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a31736dc-725c-3fb8-bdab-7f36ea866353 | -6.31514 | -49.99114 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 85ae3cfa-3db2-3b87-974d-331fbe59336c | -6.31354 | -50.00147 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b896726-b81c-3ee5-a486-5326be7f5997 | -6.3129 | -49.98357 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 81ecfb9a-2be8-384f-9e91-6a05b9d66ed7 | -6.31235 | -49.98711 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b60e75cb-265d-3bf5-a9ec-ff674008a64b | -6.31181 | -49.99057 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 75a8b032-6c96-39b5-b514-8e36529ef321 | -6.31128 | -49.994 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5b89e5f6-30ce-31b8-b547-a9675febea00 | -6.31124 | -50.81998 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14663103-d15e-3960-92cf-e4ed82db4a6b | -6.31069 | -50.82343 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16cc77d2-c60a-3f59-844c-5d014d1d3604 | -6.31021 | -50.0009 | 2024-10-10 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b862c33a-c764-328b-9621-819dee03e805 | -6.30793 | -50.81946 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e18d2f9e-4520-345a-9c69-0a9744065e28 | -6.30739 | -50.82291 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45a11892-ed7f-340d-8f64-e695dfdbaade | -6.30685 | -50.82636 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42e13014-bf20-3e6d-ade5-5f37805d4569 | -6.30354 | -50.82585 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62d359e4-249f-34ca-b018-89b951165243 | -6.30024 | -50.82533 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b40a7d0-1218-3aec-9464-3d79defe84c6 | -6.29802 | -50.81791 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7028bd13-d884-3cc0-bcf9-571cbb9af3cf | -6.29471 | -50.81739 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e93ffba3-45ce-3951-b49d-09da33bc3ae7 | -6.29417 | -50.82084 | 2024-10-10 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f11ab32-ccce-32df-8ecc-189f523fefa8 | -6.20054 | -50.89799 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce098936-2e4a-3af5-8d34-3812fd6d9540 | -6.2 | -50.90144 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2c1179a-cbd0-387e-b22a-d1e6d5c7e432 | -6.19723 | -50.89747 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11902aeb-6d20-3779-9804-222528214cdb | -6.18017 | -50.89833 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2428972f-7c0c-317b-8f09-f9a1982699c8 | -6.17686 | -50.89782 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b2959c6-a011-3719-af81-f2afe7c8abbb | -6.16917 | -50.90368 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84a9148d-e124-3f8b-ba39-2619f59b7aa7 | -6.12854 | -50.9468 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ac1948a-56fb-30ca-8e5e-adbdfc141579 | -6.12843 | -51.14115 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b9d02f4-c4eb-39be-a5e1-5f3d7c970fa8 | -6.12788 | -51.14462 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f80623c3-0331-3268-bccf-125ba25f79c9 | -6.12523 | -50.94628 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f1388c2-966e-3dcd-98c6-12e6e28c4ba5 | -6.12512 | -51.14064 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba3a73bc-745c-3251-b820-d98a5be7d8e6 | -6.12469 | -50.94973 | 2024-10-10 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a011676e-6411-3e3e-8ac7-c8bab05fbee7 | -6.12458 | -51.1441 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README105.md)
