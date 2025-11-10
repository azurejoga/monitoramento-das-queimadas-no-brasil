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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c13c43c4-268e-36c0-a761-58ffe876be97 | -21.97036 | -49.81055 | 2025-11-10 04:23:00 | NOAA-20 | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 39a92f50-63e0-3b1d-9524-5df048315e0a | -14.70444 | -46.6035 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0af53260-b67d-3347-b40d-b18ebbe89d91 | -14.69458 | -46.60191 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77d5cdad-3df0-3656-b8d0-304cac5a16e4 | -12.39649 | -46.5888 | 2025-11-10 04:23:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70ccd2c8-c18b-3a04-85cc-2abf24bb0bd4 | -13.20607 | -44.56767 | 2025-11-10 04:23:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ffad9f1-c9da-3457-ae0d-b2d53ecc0756 | -14.49721 | -48.0133 | 2025-11-10 04:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 658153c8-580a-3fd6-9b9b-1101fcaa2001 | -17.2396 | -45.90286 | 2025-11-10 04:23:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d5af82f-4f4d-333c-90f0-309b53c56661 | -13.10868 | -56.50735 | 2025-11-10 04:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 934cd32d-f288-3b25-8519-e494c58d73d7 | -10.61148 | -52.17822 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a12ac6e7-0ae8-3bb1-9b49-a3fa741a469e | -14.49783 | -48.00955 | 2025-11-10 04:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d08d36b-7ba9-3a3e-98e4-a1deccb63bb0 | -17.24016 | -45.89916 | 2025-11-10 04:23:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d725fe-78c3-3b86-be27-72d1ef3be67d | -12.21045 | -49.49936 | 2025-11-10 04:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73ef1d20-a427-3367-a17d-122d033abed9 | -11.96777 | -48.72724 | 2025-11-10 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96e7e947-d3dc-33cd-a875-6703acafed32 | -13.06209 | -50.28711 | 2025-11-10 04:23:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88bc4103-aa58-32e9-90cc-d1611b68e17c | -11.07941 | -54.10578 | 2025-11-10 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06fbc0f3-5bd2-303b-9d77-f5270277ebfc | -23.37436 | -46.02732 | 2025-11-10 04:23:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bfef2ce0-fe79-3163-8e61-efddf708143a | -11.54798 | -48.54692 | 2025-11-10 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 68ad267a-f084-3bac-8fc8-0be51ccdd765 | -10.6156 | -52.18681 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c479c9cc-fba6-3358-a4a0-9afa281f616b | -13.55208 | -49.05805 | 2025-11-10 04:23:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ad3be50-fd6f-3eb4-960f-dcbc7b03bf76 | -16.51636 | -52.38148 | 2025-11-10 04:23:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16b785ad-46aa-3f06-9c9d-8b9d3cf54500 | -13.72987 | -51.46278 | 2025-11-10 04:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 670f1bc7-e5d1-387b-9c99-c5d28e5d502f | -16.5204 | -52.38233 | 2025-11-10 04:23:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77a6d35e-3073-3bb8-9fe1-3280151f3212 | -11.66277 | -48.46743 | 2025-11-10 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4f0b981-71d9-3a05-84a7-c451322239e2 | -13.20663 | -44.56396 | 2025-11-10 04:23:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b863b18-835c-3d99-9bea-72229e5303ac | -10.61273 | -52.17714 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a7faefb-6682-3a96-99b5-22387aa28d8c | -11.91661 | -44.18159 | 2025-11-10 04:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3655a510-f444-33a2-a84e-e1d32461d7e2 | -14.70058 | -46.60651 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f1cb84df-bfa6-3524-abc7-b7cf86fc365a | -10.61715 | -52.17794 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c0db07-d388-3d82-843f-56aa9e94012c | -13.94354 | -47.38695 | 2025-11-10 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6241c480-38bc-3fb7-a53f-f69c4c3f13cc | -17.12784 | -55.74343 | 2025-11-10 04:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 33eaef0e-2874-3fa5-a694-6266c0e11df6 | -14.70114 | -46.60296 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 637b48aa-560f-3907-a2e5-739030ef936d | -14.69188 | -46.57594 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ddb82a6-111b-3377-ae7e-ee2996db671b | -14.6902 | -46.5866 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01db932a-4d74-3af4-93be-7f90b5ad4070 | -14.7017 | -46.59941 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4ad36b0-874b-39e3-ae60-01f136ca4442 | -15.12448 | -49.52341 | 2025-11-10 04:23:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75d8381d-de5d-3cc4-a4cb-3c09f5a0e15d | -14.70831 | -46.60051 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f3d2a83-faa6-3215-aed4-b223dd5761a6 | -12.10922 | -43.65026 | 2025-11-10 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f571c597-f48f-358c-baab-04cdb1900208 | -14.70018 | -46.56639 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa37fbc0-f42d-37bd-acb5-e3506c012d52 | -14.6957 | -46.5948 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 953e0539-1d97-3f5d-b000-f20cef0742a7 | -14.69351 | -46.58715 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f3ca157-d0ee-3409-ae3a-05577b0a735e | -14.70226 | -46.59586 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00e689d4-f72b-371f-91bb-d6af0ac3a32d | -14.70388 | -46.60705 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db18ab80-5dba-3d4a-a648-9160e546b1d5 | -17.26336 | -48.04934 | 2025-11-10 04:23:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a62103c5-ba78-3035-b506-e314125939cf | -11.92001 | -44.18212 | 2025-11-10 04:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db249070-9dfe-3f9f-84f7-f962d3a55e85 | -13.96546 | -46.91407 | 2025-11-10 04:23:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a4ecddb-eaad-3617-90d6-edf4dc3d0981 | -10.6159 | -52.17902 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1c832ba-d3c8-3bc1-be4b-3321dc2df0c2 | -10.61509 | -52.18346 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8bbb6ab-23ba-39ae-9d66-e7b14146c97c | -12.10981 | -43.64637 | 2025-11-10 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8024304c-6599-3a46-8610-71ea4c740c6d | -13.96603 | -46.91051 | 2025-11-10 04:23:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7405478-c05e-3ec1-885c-dd191e2a69cc | -21.96764 | -49.80607 | 2025-11-10 04:23:00 | NOAA-20 | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 724f4fb4-8477-3179-8bd3-979458ef6702 | -11.07442 | -54.10488 | 2025-11-10 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ff1a862-a8bc-3eeb-b5b9-cb803d326ef8 | -21.967 | -49.80992 | 2025-11-10 04:23:00 | NOAA-20 | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 548179eb-264e-3d5c-8e63-44104f90dad8 | -11.96782 | -48.72641 | 2025-11-10 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c27b1161-fe81-3803-b408-a345e5ec6f9d | -11.91718 | -44.17787 | 2025-11-10 04:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91a403ae-2853-376f-b192-41552dbf9fc0 | -10.61638 | -52.18237 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de35dc69-bc18-38cb-91c2-911033231a0c | -14.69682 | -46.5877 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17c380c0-0604-30c5-95c2-f47a0255502d | -10.61195 | -52.18158 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d324b5f-2c96-3f68-9967-994e2b27f00f | -12.2224 | -51.44563 | 2025-11-10 04:23:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da798704-1783-3520-865e-5e0da2a52401 | -12.15858 | -49.16553 | 2025-11-10 04:23:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4014405a-8259-3376-9b55-09aa210d6a45 | -13.40577 | -48.54068 | 2025-11-10 04:23:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8fc24df-4a34-3f8c-9de0-26c0a2e18bc6 | -13.96215 | -46.91351 | 2025-11-10 04:23:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf05bcbf-5f72-3ffa-a725-baf12578b73f | -10.61067 | -52.18265 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4152dd6d-b198-3bed-ba5c-4645bc4a6f49 | -14.69133 | -46.57949 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fc85b6e-8512-3a03-b3f5-4b9add25abd1 | -14.69957 | -46.5918 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0326a86-b889-3af0-83e6-9f74c353d3ba | -13.00997 | -48.80713 | 2025-11-10 04:23:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a44c549-d930-36f6-892b-ba2b3e22be64 | -12.32069 | -51.31449 | 2025-11-10 04:23:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ebc62d2-e625-3312-9273-0bea0d505262 | -14.71236 | -46.59774 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e8882fa-8d97-31b4-9d5d-61fada165dc0 | -13.00646 | -48.80653 | 2025-11-10 04:23:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30b559b0-9795-3151-aa0e-b65bd409db00 | -14.69784 | -46.60241 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 930853a4-9b00-3484-b5bf-e946a98df4d2 | -11.80499 | -49.41228 | 2025-11-10 04:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e6561c7-64c5-3b4d-9c9d-3f132127aa85 | -14.49597 | -48.0208 | 2025-11-10 04:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e51168a6-25bf-3ecc-9921-63e262a2cec8 | -14.69463 | -46.58005 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 075d63b8-f738-302e-b741-9013e91aac0f | -14.70349 | -46.56694 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72fc84f7-7384-322f-bcff-82641661c7bd | -12.39705 | -46.58527 | 2025-11-10 04:23:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92432af9-88d2-3f5b-85d6-ae49ad830c6b | -14.6869 | -46.58605 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33e0173f-e6bd-3c32-a9f9-39e798de242a | -14.705 | -46.59996 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 762538f0-cdd1-3b70-aa2a-b1246ffc705c | -10.61118 | -52.186 | 2025-11-10 04:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc67120d-cada-3ed2-82c5-8d726b030965 | -18.51186 | -53.4892 | 2025-11-10 04:25:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89826b51-78aa-3d62-9b79-6bf2f2afe138 | -18.10857 | -54.51974 | 2025-11-10 04:25:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20cebc2f-2f9c-337d-85ca-021cd35e4152 | -18.47549 | -53.40592 | 2025-11-10 04:25:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 342fe690-bebc-3eab-82b1-2fbf4290568d | -18.47886 | -53.411 | 2025-11-10 04:25:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4131aba4-1e9f-315c-ad56-54ba20bdba70 | -18.21419 | -56.73096 | 2025-11-10 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 383e419f-fd71-3925-ad91-7eef36e3069e | -19.04957 | -48.48199 | 2025-11-10 04:25:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9362cdbe-abbb-3568-b592-52c7d1952c32 | -18.51109 | -53.49333 | 2025-11-10 04:25:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f8e7cb8-6f48-3ae1-85f2-7b91d2f9d91c | -18.21349 | -56.73426 | 2025-11-10 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7de184bd-bf24-3a4a-88a9-710de95d517f | -18.21381 | -56.73088 | 2025-11-10 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0555bcd9-f3b6-342d-8131-daf1d839bffe | -29.4008 | -50.86882 | 2025-11-10 04:25:00 | NOAA-20 | GRAMADO | RIO GRANDE DO SUL | Brasil | 4309100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9def7caf-0d17-38ae-88de-b66d05cfdcd5 | -19.0529 | -48.48258 | 2025-11-10 04:25:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21295828-be8e-3e9e-8689-633fdac08323 | -18.47965 | -53.40681 | 2025-11-10 04:25:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fadf842a-63cc-35bb-bc3a-d0a1284d27f5 | -18.50114 | -53.49991 | 2025-11-10 04:25:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a99e8fa-4239-31d1-bed7-e2ef1f15f7a4 | -24.9846 | -51.53996 | 2025-11-10 04:25:00 | NOAA-20 | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bfea0de8-fba1-3a5a-904a-2c4206422916 | -18.21313 | -56.73419 | 2025-11-10 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b7d9e6f0-cb2c-396a-b42b-58512b9ba4c3 | -19.36821 | -48.61379 | 2025-11-10 04:25:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a0c594b-0ea3-33b9-a236-0c67f667a168 | -19.37384 | -52.49724 | 2025-11-10 04:25:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e970d6d-0263-372c-92be-96922e8623c1 | -18.10702 | -54.52164 | 2025-11-10 04:25:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ebf6e77-6ed9-3c65-97ba-bf4c75c17a61 | -18.4747 | -53.41005 | 2025-11-10 04:25:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ff7b14f-70ca-3456-aaa3-e13d4d3b1d89 | -19.37481 | -52.49209 | 2025-11-10 04:25:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24cf2c1d-57e8-3a38-bf4b-4f0e911c456f | -19.374 | -52.49504 | 2025-11-10 04:25:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4cc0a9f-d4af-34fa-98a3-80dbf1abf9a2 | -19.97703 | -44.85413 | 2025-11-10 04:25:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87408331-82c7-316f-89c3-81301c0dc353 | -4.2128 | -50.6273 | 2025-11-10 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |


[Clique aqui para ver as próximas entradas](README15.md)
