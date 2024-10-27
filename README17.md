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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f67f7ede-d670-329d-b0a1-2aee5aef5833 | -2.6962 | -49.3139 | 2024-10-27 01:09:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8bddeb-5bfa-3390-bbda-7f2423347cd9 | -2.6988 | -49.324699 | 2024-10-27 01:09:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dca67503-a4cb-332d-a39e-1dc19de20003 | -2.9194 | -50.265202 | 2024-10-27 01:09:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 880573df-0315-3851-9448-d1e71ac85412 | -2.9216 | -50.274601 | 2024-10-27 01:09:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1dbc15b-3a36-393c-818d-25a26925b058 | -2.9238 | -50.284 | 2024-10-27 01:09:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 664dbc44-0867-3c03-bfe8-fef92a77dda3 | -3.0108 | -50.479401 | 2024-10-27 01:09:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb2f2919-eb47-3a1a-b002-1be87ba6c204 | -4.014 | -54.816299 | 2024-10-27 01:09:54 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02350ca7-94b5-35ae-a30c-4a725e1eb43d | -3.2483 | -51.541901 | 2024-10-27 01:09:54 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a76e4cb3-9185-344f-acae-470e4099dfb4 | -3.2502 | -51.5499 | 2024-10-27 01:09:54 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bafd9ae-c409-3111-96da-640489482617 | -3.2521 | -51.557899 | 2024-10-27 01:09:54 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 417c9c38-c5c2-3586-b2f3-092db2dba1f7 | -2.939 | -50.2607 | 2024-10-27 01:09:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f648f8-7200-3e70-8f22-cade35d8adc3 | -2.9412 | -50.2701 | 2024-10-27 01:09:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1572a9a4-6a1f-3510-82e3-2b7e76033547 | -2.7035 | -49.300701 | 2024-10-27 01:09:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a1e7ca6-b754-3541-aef3-902e34413563 | -2.6438 | -49.221901 | 2024-10-27 01:09:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1e01206-6a85-3acd-b2cb-cbcbfe5ff921 | -2.6464 | -49.232899 | 2024-10-27 01:09:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8740196-f038-3fe4-97ad-bae1707439bb | -2.649 | -49.2439 | 2024-10-27 01:09:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3260f43f-d7df-3f74-9fd5-1a4391072a74 | -2.634 | -49.224201 | 2024-10-27 01:09:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 981bea45-3db6-3231-b7e2-550e2df34bcb | -2.6366 | -49.235199 | 2024-10-27 01:09:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b364ac32-eb4c-3e64-bfec-3dce95db01c4 | -2.6392 | -49.246201 | 2024-10-27 01:09:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b704c25f-ce59-355f-9a61-f391018b2add | -3.0977 | -51.249298 | 2024-10-27 01:09:55 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b962f83-7960-355f-b91d-a58e506f48f0 | -3.0996 | -51.257599 | 2024-10-27 01:09:55 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db8e158e-b21e-3216-adfa-cb15d4d008bc | -3.5397 | -53.5131 | 2024-10-27 01:09:57 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d68feea-699d-3e72-8888-046e64ec782a | -2.4925 | -49.1036 | 2024-10-27 01:09:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7442714-af48-327d-9c4b-b4552bd42876 | -3.3192 | -52.647598 | 2024-10-27 01:09:57 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c8157b-ab80-3da2-b758-d393eae5cee8 | -3.3209 | -52.6548 | 2024-10-27 01:09:57 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9078f255-84d7-35a8-8420-e3f689af6c21 | -2.48 | -49.094501 | 2024-10-27 01:09:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bca28327-5827-3ede-917b-1aad224a381d | -2.4827 | -49.105801 | 2024-10-27 01:09:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6dda293-790a-32b0-bdb4-e3ecaf222901 | -3.6678 | -54.2052 | 2024-10-27 01:09:57 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8f5d4f3-f63c-3872-8b5f-d5f04a582cbd | -3.6694 | -54.212002 | 2024-10-27 01:09:57 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bccf65b-9d10-3564-8017-fb4e22f2873d | -3.671 | -54.2188 | 2024-10-27 01:09:57 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 894a304a-486b-326d-bcbd-efc7200c2f85 | -2.4703 | -49.096802 | 2024-10-27 01:09:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4064baa-5b69-3eec-a176-9112fd5e5ad6 | -2.473 | -49.108101 | 2024-10-27 01:09:57 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67426b3c-e595-390b-9c94-cd1cd4b2705a | -3.6173 | -54.030102 | 2024-10-27 01:09:57 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78d83a73-0621-3954-b386-74ab4c4a2b86 | -3.6768 | -54.2892 | 2024-10-27 01:09:57 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2a8de39-c2ed-3b34-a9ba-d88090ba1493 | -3.6075 | -54.032299 | 2024-10-27 01:09:57 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1061248-9fd1-353b-ba50-ea7d3b2728e3 | -3.6654 | -54.284599 | 2024-10-27 01:09:57 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2bdb6c6-6bf1-3b23-b9ed-0fb44f76891e | -3.667 | -54.291401 | 2024-10-27 01:09:57 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d47b74a7-f34c-3602-b31c-f7d50525f562 | -3.6685 | -54.298199 | 2024-10-27 01:09:57 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1679f0be-7451-3f7d-a374-cd7d37e3c71f | -1.7943 | -46.364498 | 2024-10-27 01:09:58 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b05b543f-9a56-37f1-855a-b75d5b274bec | -1.7986 | -46.382301 | 2024-10-27 01:09:58 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d66718ca-43de-30f2-b969-b755bf5e855d | -1.8028 | -46.400101 | 2024-10-27 01:09:58 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51ee5288-e053-3d0e-a414-27dc7e2787aa | -1.7889 | -46.384602 | 2024-10-27 01:09:58 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bac7cad-422f-3ad0-a073-18fac46acee7 | -1.7931 | -46.402401 | 2024-10-27 01:09:58 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8be82c1-46c0-317b-a4ca-d2dfbbccb14f | -3.7218 | -54.665901 | 2024-10-27 01:09:58 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbac5614-f201-3388-910d-b679865f64e3 | -3.5557 | -53.986401 | 2024-10-27 01:09:58 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 047d8117-3080-3540-88b4-f0101fd82d60 | -3.5573 | -53.993301 | 2024-10-27 01:09:58 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a21cd147-adde-3c50-af8f-ac71edecbfd4 | -2.8311 | -51.0341 | 2024-10-27 01:09:59 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a4e66ed-72e2-3c24-bf8f-4a6dbad10f3a | -3.6418 | -54.676701 | 2024-10-27 01:09:59 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 951b67ac-3edf-3ac5-aa5e-a0593afd23db | -2.1608 | -48.436798 | 2024-10-27 01:10:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20e55df1-5bf2-3974-bb71-b6418bc723f2 | -2.1638 | -48.449501 | 2024-10-27 01:10:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adbf0294-7a3f-38ce-be5c-be301a276c15 | -2.937 | -51.755299 | 2024-10-27 01:10:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da8fa77-fcfe-306d-9e21-cccfac70f0b6 | -2.9236 | -51.741699 | 2024-10-27 01:10:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50fadf8d-9a69-34be-888b-8ff331f2e992 | -2.9254 | -51.749599 | 2024-10-27 01:10:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54418aa1-6751-33d9-a0de-915a8a9eb59d | -2.9272 | -51.7575 | 2024-10-27 01:10:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44b58d79-3592-37a6-90c5-96fdbcd3a1b7 | -2.9291 | -51.7654 | 2024-10-27 01:10:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1201e7d8-5b9d-3233-8e25-fcc11e64e93c | -2.9138 | -51.7439 | 2024-10-27 01:10:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cbe63aa-3eae-311b-b281-b0625b7831b0 | -2.9156 | -51.751801 | 2024-10-27 01:10:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9395ca10-dff8-3eae-915a-14b74be3e845 | -3.5693 | -54.5853 | 2024-10-27 01:10:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbbb15ec-db9e-385f-a146-6f73b6f9fc54 | -3.585 | -54.6535 | 2024-10-27 01:10:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cf568d0-b285-3a4b-b46a-5124612523a7 | -3.5865 | -54.660301 | 2024-10-27 01:10:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6778f71-a49b-348d-b49f-f45cb93d9491 | -3.4591 | -54.194698 | 2024-10-27 01:10:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19a74e94-f148-31fc-b2e0-7578cb1eea77 | -3.4607 | -54.2015 | 2024-10-27 01:10:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c02b01c-53d0-342e-8100-76eb5b9cf92e | -3.5654 | -54.657902 | 2024-10-27 01:10:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb063f8f-dc12-313e-be3e-8a3e7077a5fb | -3.5669 | -54.6647 | 2024-10-27 01:10:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7953a82a-a1fb-3fc3-a917-fe7c34965c9f | -3.5685 | -54.671501 | 2024-10-27 01:10:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59589760-cd71-3b74-9b36-25edb7635235 | -2.7941 | -51.362099 | 2024-10-27 01:10:01 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb346d2-c812-3c76-b6f2-0b334ac6372b | -3.2369 | -53.273602 | 2024-10-27 01:10:01 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df6dc084-4cc4-37dd-a13e-5272b4a06794 | -3.5024 | -54.428398 | 2024-10-27 01:10:01 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2594acd3-d313-36da-a724-b3f5eb5cb3ef | -3.504 | -54.4352 | 2024-10-27 01:10:01 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5e31ae5-ee75-30b8-87c3-b1ac60a55fba | -3.2271 | -53.275799 | 2024-10-27 01:10:01 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e41a1852-103c-3d79-9149-5c09554e7981 | -3.4911 | -54.423801 | 2024-10-27 01:10:01 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35f7fa98-08ed-32bb-a936-686ad31dbb6a | -3.4926 | -54.430599 | 2024-10-27 01:10:01 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7591ffef-8465-34f1-9d6d-1e648c9007bd | -3.4942 | -54.437401 | 2024-10-27 01:10:01 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fd69856-26d4-30c0-9cd1-a92c71f8b662 | -3.4828 | -54.4328 | 2024-10-27 01:10:01 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0cf7919-732c-32e0-b21f-1f79ce91f886 | -3.4844 | -54.439602 | 2024-10-27 01:10:01 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57f99b87-f269-3c31-8fa7-9e54b5454cc6 | -2.816 | -51.589401 | 2024-10-27 01:10:01 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a1f4566-e43c-386c-a9be-322df09ce99a | -2.8179 | -51.597401 | 2024-10-27 01:10:01 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8787395a-bdc4-336b-b829-d9602cb3d523 | -2.4887 | -50.273602 | 2024-10-27 01:10:01 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c33651df-010d-3ef0-9b6f-994eb9319c0b | -2.8427 | -51.793301 | 2024-10-27 01:10:01 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 922b50bf-68fb-376e-9f2b-6b693773d35d | -2.8446 | -51.801201 | 2024-10-27 01:10:01 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9640ca8b-273b-3ba7-9bad-7fb24a80b89f | -2.8464 | -51.809101 | 2024-10-27 01:10:01 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb21df0-e140-3c98-8026-c76abe973294 | -2.4789 | -50.275799 | 2024-10-27 01:10:02 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2352839a-6635-309f-9c0e-5041b1ca282a | -2.4811 | -50.2854 | 2024-10-27 01:10:02 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c5d5c7f-0179-34f8-b662-8c89f9874536 | -2.8329 | -51.795502 | 2024-10-27 01:10:02 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 887dcba0-f6a5-39e9-aa40-6d14441ec5d6 | -2.8348 | -51.803398 | 2024-10-27 01:10:02 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7be6b3-231d-36b8-a7a4-e2f83eb73e5b | -2.8366 | -51.811298 | 2024-10-27 01:10:02 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15d1af53-c2da-309b-97e4-ac65be835481 | -3.4716 | -54.564201 | 2024-10-27 01:10:02 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 145359a5-db56-356a-9860-18d40185424e | -3.4732 | -54.570999 | 2024-10-27 01:10:02 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 308e4ac7-ccc0-3b99-80ec-87bbaf47cf96 | -3.4748 | -54.577801 | 2024-10-27 01:10:02 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 381385c1-a527-361b-9f5e-fc5d56c9f169 | -2.4691 | -50.278099 | 2024-10-27 01:10:02 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34682d94-6042-3371-a2e3-48c29178a3f6 | -2.4714 | -50.287601 | 2024-10-27 01:10:02 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14c3af1e-bb45-30d9-8f77-3eba1e5fe138 | -2.3021 | -49.696201 | 2024-10-27 01:10:02 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da746b2b-727f-390b-93a3-8ff3ba66d79b | -3.4308 | -54.566101 | 2024-10-27 01:10:02 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56b1d1fc-a595-3300-9431-3432061eb24f | -3.4324 | -54.572899 | 2024-10-27 01:10:02 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7d1acaa-5488-3d3e-8221-a2e82d541c2a | -2.4566 | -50.400799 | 2024-10-27 01:10:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13d9d1e2-4d1f-3b1f-aadd-fa852bcde7ae | -2.4588 | -50.410198 | 2024-10-27 01:10:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dc084a2-2143-3e32-b66a-2d622436b84c | -2.461 | -50.419601 | 2024-10-27 01:10:02 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d7fa8ab-a0de-33fb-814e-2ae6c06616a0 | -2.947 | -52.554699 | 2024-10-27 01:10:03 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3126aae4-58aa-3608-924e-83b828e504b4 | -2.9487 | -52.562 | 2024-10-27 01:10:03 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 660bf801-88f9-3d70-8220-540e8f3d1cb4 | -2.7891 | -51.9622 | 2024-10-27 01:10:03 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
