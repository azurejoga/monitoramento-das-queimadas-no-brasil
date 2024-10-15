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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3557a588-22be-3efc-8a5f-7875b3cf3f03 | -4.11249 | -48.23643 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ad301b7-0524-3b8f-a636-fdc863751abb | -4.11198 | -48.23945 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1053769-3f92-3dfe-829d-f810ee321a1e | -4.11064 | -48.27924 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63ce8d59-5fa6-3157-96d4-e8dc23c0e51d | -4.1101 | -48.28247 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6567389d-f78f-333b-b438-5908dac5d35d | -4.05874 | -47.91331 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c237499-7fe6-34da-9751-fe22869e6408 | -3.93111 | -48.35314 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7fa4fec3-392f-3dc4-9280-e2aceb58273c | -3.93079 | -48.3523 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 423ced64-d037-38b2-982c-b7feaca746eb | -3.92583 | -48.35231 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e605618d-e558-3c02-8794-fd66f0d7b7be | -3.92551 | -48.3515 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d296aeb-3d4e-3783-aa2d-c5ca65317e0b | -3.92528 | -48.35566 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32757a4b-8df1-3fb9-9d60-003ba86f72bb | -3.92494 | -48.35484 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a556c5b6-e3f5-34ca-9364-9496ce9fe5d2 | -3.92473 | -48.35902 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a9c738bb-c16b-3b30-a932-ddab39402080 | -3.92436 | -48.35817 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 34a9d1f7-b32b-35cb-a54b-24acc63ec33e | -3.92218 | -48.34164 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9a62429-7bb2-3d12-bf09-1ca9e31c18b6 | -3.92194 | -48.34085 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0164f9eb-c818-388a-9709-ada38716adec | -3.91892 | -48.36142 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 302aa041-9306-3395-8ea0-716a3cb79929 | -3.91836 | -48.36477 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8974b2b-7b78-3edc-8ccd-457c6ff9cc5d | -3.91795 | -48.36392 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 377a2342-87ce-38ff-9d72-631d297dfea4 | -3.91748 | -48.33739 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38fa385d-8d49-3ede-b784-36a0354959c4 | -3.91726 | -48.33664 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbcfa43b-4ec1-332e-8b79-39b774f1e633 | -3.91693 | -48.34071 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78a9b9fe-cd93-3780-afd0-4d6b195f5929 | -3.91669 | -48.33991 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5cec48f-08f1-3aa5-bcc8-bf90b813ea27 | -3.91418 | -48.3573 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b99183eb-703e-30a2-a750-fce1263a63c9 | -3.91382 | -48.35649 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4872dc30-e146-3725-a7b4-35518e44a614 | -3.91364 | -48.36058 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf62d601-9b3e-3415-b9f6-df18d686808a | -3.91325 | -48.35977 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23f89673-e190-3c07-9b02-66217608187d | -3.91309 | -48.3639 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55956e2d-ce57-378e-8d23-4d52bcac7005 | -3.91268 | -48.36306 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36e5a3f0-98eb-34ce-89fe-b8328a82819c | -3.90838 | -48.35966 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76fcd4f2-b9d9-3081-8510-96d759fe0401 | -3.90783 | -48.36297 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3512a8d7-5e56-3ccc-8e3d-b553f6b036b0 | -3.90312 | -48.35873 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 546310bd-5276-3c6a-b39c-ed0323dadc9b | -3.90256 | -48.36206 | 2024-10-15 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 028cb3d9-da37-3b11-b612-3d754fdc60bf | -6.41813 | -49.59288 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4072a117-177f-39cc-97a0-d995210c0991 | -6.41761 | -49.59293 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48215f65-e5a0-303b-a0aa-4f12af6be2bd | -6.41751 | -49.59631 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d5e2654-f425-3e7f-a9a0-dc8c50b55270 | -6.41701 | -49.59636 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c41ed9b4-79b5-35b6-ac48-76deef903185 | -6.41684 | -49.60003 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33efaf5e-b988-36fb-af2f-e3957302ba94 | -6.41636 | -49.60014 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d07cae7-9e88-3ea3-8476-bbd5025ef0cb | -6.41614 | -49.6039 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24a92f17-9eec-3979-a517-13af7697dd5e | -6.41568 | -49.60408 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d21474d-8ccb-3f17-9494-a30e45522d10 | -6.4134 | -49.58777 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23180032-73c0-3651-b62a-a113af1c6c94 | -6.41284 | -49.58781 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d51ffe2c-d284-3ab1-85aa-66f6b452daaf | -6.4128 | -49.59107 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 043dab29-0805-3d74-985d-0c74bc77609a | -6.41226 | -49.59113 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2c5a00b-5914-3ec6-9f80-7ddb688a963a | -6.4074 | -49.58965 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f62263b5-0cbd-3a66-bb01-13b3025870af | -6.40685 | -49.58973 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d8bd1fcf-4a87-3e4a-80b1-6356c6830272 | -6.4067 | -49.59354 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da10b517-a2f4-337e-be2c-f6d07991c28a | -6.57845 | -48.23579 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 21.1 |
| f40f0794-1136-37e2-90cd-07708ad80071 | -6.57794 | -48.23869 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 21.1 |
| bf8805c7-3948-31dd-8fef-49f7754dfec9 | -6.57744 | -48.24159 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 184f5c92-2fe6-3f31-b095-dfdd8c98b4e1 | -6.57397 | -48.23199 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 931f525a-446e-34b7-bff8-26a36c736cac | -6.57346 | -48.23489 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7e50bcc0-0978-324f-93e2-5fec4cf4d70c | -6.57295 | -48.23779 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 6aaf8eae-a001-326e-a9fd-766125ea2fbc | -6.57244 | -48.24069 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 12.9 |
| aee3a16f-9fe6-31fc-8092-846d24c8e4ae | -6.57193 | -48.2436 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8a60a0af-1cd6-31c9-a6a1-1d16183da635 | -6.57142 | -48.24651 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ba9545d3-405c-3d5e-8a52-b7526ceb325c | -6.5709 | -48.24944 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e666c6e0-b18c-3e69-b9f9-3152021d6a33 | -6.56745 | -48.23981 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2c307619-e531-396e-befc-6fe2f7504b56 | -6.56693 | -48.24273 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 77a08c4c-3c97-3ea9-a0bb-79b9d2bf84a8 | -6.56642 | -48.24565 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e3b7525b-86a6-3665-99b9-79279bfd06a1 | -6.5659 | -48.24857 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 993e19ea-4e35-360d-ba5a-f4b7dd1f1837 | -6.56538 | -48.25151 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91ce4a53-ea3a-3708-a2d0-8c9a1e0d653a | -6.56487 | -48.25442 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 460d024f-f687-3529-b3be-f10f7f6040e7 | -6.56245 | -48.23893 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 82a1b0a6-5b27-32b7-ad51-c936bd5eded9 | -6.56194 | -48.24185 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e6543eea-1d9f-376d-af96-3fd7bfb976a6 | -6.56038 | -48.25063 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd06524d-ea1e-3a63-98c0-b87fb9c3e6c2 | -6.55747 | -48.23799 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371add16-63cd-3f80-a7cd-566170b26e4e | -6.55695 | -48.24092 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8e632d2-ac77-380c-b35d-9ddb2866f5ab | -6.55539 | -48.24973 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e01fa825-e3db-325f-94ad-825498ca13e0 | -6.55486 | -48.25268 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d92d93e0-87de-32f9-a0de-b4f790fc3b75 | -6.55195 | -48.24001 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7513b34-d664-3ca7-ba97-aad58c0ac6fd | -6.54987 | -48.25179 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87b152e6-f255-3707-9213-39e346a4edc9 | -6.54748 | -48.23618 | 2024-10-15 04:02:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 600dbf47-ea63-3727-bc64-2ea62a24ed74 | -5.22518 | -47.95563 | 2024-10-15 04:02:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1f8a676-44f0-39d0-aaea-009a06469d0f | -5.22467 | -47.95857 | 2024-10-15 04:02:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 745e0088-a68c-3087-85ff-77a81336778e | -5.22017 | -47.95471 | 2024-10-15 04:02:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31cba2dc-b64e-3b52-8e24-63a546d04f36 | -5.21967 | -47.95763 | 2024-10-15 04:02:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dedd3819-7be4-3f64-96a3-c690e793cd70 | -7.95701 | -49.06706 | 2024-10-15 04:02:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f51e8ccb-8111-3a45-9131-973e71980910 | -7.65441 | -49.36399 | 2024-10-15 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57803383-0f52-3f9d-b8b0-f78dec5024d0 | -7.65381 | -49.3673 | 2024-10-15 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80a0335e-1937-3b46-943a-5022efcc8e74 | -7.51812 | -49.48821 | 2024-10-15 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e3253680-16df-3603-8ad3-74e14596450f | -7.51751 | -49.49153 | 2024-10-15 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 70d132b3-29bf-3ae9-8801-c13d98221e9a | -7.30739 | -48.6068 | 2024-10-15 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2e508f6-aa20-375f-be6f-23bf4bf97fe3 | -6.66318 | -49.46386 | 2024-10-15 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| a70844d6-e991-38aa-ae0c-e991977ea255 | -6.66256 | -49.46731 | 2024-10-15 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| ee37d163-2821-3db7-a644-75b5c9e4e94d | -6.42348 | -49.59457 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9467f41e-7e80-3e60-a6e6-03f7a0b49914 | -6.42285 | -49.59807 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 814baf26-cf87-3614-81bd-fb5c73bba71a | -6.42222 | -49.60157 | 2024-10-15 04:02:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eaab660-94d2-3745-9d1f-a8605156e19f | -9.27417 | -49.23335 | 2024-10-15 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a5e89a3-b04a-3299-a699-c049cadbea5d | -9.18649 | -48.85942 | 2024-10-15 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e40efe09-8acd-3de2-83ba-ba870fc22279 | -9.18597 | -48.86227 | 2024-10-15 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 080f4eac-429a-3c6d-b426-816045021720 | -9.18151 | -48.85853 | 2024-10-15 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aafa69a2-c6d7-3c05-a3d5-1d0dbc6dae8c | -9.18099 | -48.86135 | 2024-10-15 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf525845-fe3e-3174-bb5b-458e906c18cf | -9.16127 | -49.82974 | 2024-10-15 04:02:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8098d09-c7fa-33e8-8797-f63b7141180f | -8.33776 | -49.66007 | 2024-10-15 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bf7b848-7195-3144-882d-14395be087a9 | -8.20598 | -49.33798 | 2024-10-15 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d22e56d3-216e-3879-bf88-f867d66cbd4d | -8.11679 | -49.35164 | 2024-10-15 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5feba30-ade5-3611-8e6b-be148cde8b56 | -8.11621 | -49.35482 | 2024-10-15 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc4b8392-c563-3941-998d-529cd8f712ab | -9.65632 | -48.97483 | 2024-10-15 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98a36859-ff3c-3c6d-ad5c-9a807b3464bd | -9.65579 | -48.97607 | 2024-10-15 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README31.md)
