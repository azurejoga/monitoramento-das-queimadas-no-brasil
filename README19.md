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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18c6b22e-6b68-3499-a34b-89c17b5c31ba | -7.15435 | -39.43746 | 2025-10-13 04:23:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af3d8bf5-3395-3d30-8992-486c2eb2ecbb | -7.3444 | -43.85775 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb5df697-ba55-32c6-8069-d136f60afa18 | -6.73752 | -42.08176 | 2025-10-13 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76fad157-8c20-3d18-905a-aeccfd455c14 | -8.45064 | -46.12135 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3347a518-161c-3ba9-8d61-6a174d02d7eb | -10.03753 | -43.81158 | 2025-10-13 04:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8e155947-2412-3a4c-a37b-3291f1b20bcb | -8.47687 | -46.1292 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f9328a1-b060-3dc6-8921-f63e4880305f | -10.79433 | -43.96732 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68f62bb3-afb6-35ab-950f-abbf1d25a574 | -6.46054 | -44.42183 | 2025-10-13 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f1c5ef3-cd22-3510-bfce-c874a4b3f6e7 | -7.5018 | -44.59629 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aef54930-d804-3afc-a755-918e4bd8ee96 | -7.48891 | -42.1586 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0420c663-0dbb-367e-a56b-de472b56661b | -7.75039 | -44.19366 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9751136-f0c2-32fb-9626-5faa417b3576 | -7.68912 | -42.38015 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 736dfd6b-42a9-3aed-9433-b402d8b530d1 | -6.774 | -42.83403 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3eded77d-9186-3e49-ac04-9f4d53bc7465 | -6.73686 | -42.2036 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d0fa50b8-5374-32ca-adf4-4828cb621e96 | -7.35395 | -44.09211 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54cb5d5d-4e06-30ce-b18b-3c1aa590637d | -9.26564 | -40.43519 | 2025-10-13 04:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af7b6082-b485-366d-a5a5-06c93998a648 | -8.22761 | -43.33789 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d866be3c-a8ba-3953-bab1-0aa97f826b24 | -9.56242 | -45.53615 | 2025-10-13 04:23:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cc9a972-b540-3638-aa3e-b3fab6118c86 | -7.49737 | -44.60276 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c99775c1-8211-307a-8c25-2a3de4e79eeb | -7.77348 | -44.04485 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48b88357-6949-33fe-b6c7-d7d27cde2cb2 | -8.47466 | -46.12157 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbee3e5a-79b3-3c18-8070-5ac4f3f5b1b4 | -8.46732 | -46.14594 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 137fe06b-4cd3-30b1-a470-ea63d1b618da | -8.46675 | -46.14953 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff1833a3-f9b8-3347-9fbd-87e53aed10d3 | -7.50125 | -44.59978 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0db6a3cb-242d-3784-a952-bed18b383f3b | -6.77343 | -42.83777 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e54e02c8-7f6b-365c-b57c-bfe234a4124d | -7.49909 | -44.63521 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db3e871c-764b-3230-a1b6-da1ced119b72 | -7.499 | -42.16426 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d07b23c-6434-3f6d-bb2f-2d2f1fb096ad | -10.79209 | -43.96404 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7da13380-885f-3bda-a9b7-d8157de83c9f | -8.16534 | -47.1481 | 2025-10-13 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99a6b07a-32a9-33bf-a9e1-c8904564068d | -7.35061 | -44.09159 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b71df7fd-ef5b-3b42-ba25-ccd29298e523 | -7.68416 | -42.38649 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 83c84e87-0b0c-3ed6-9cf6-2a7206484fef | -7.4902 | -44.62666 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 92102eb5-c561-3598-97b8-a9ab6624d39f | -7.91954 | -47.21803 | 2025-10-13 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa4a7b29-1ce9-3964-9937-54e5efbfa640 | -7.74985 | -44.1972 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf435978-63e1-3954-82b4-67ffbb3dc489 | -6.7635 | -44.64793 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74335c04-aa39-340c-97ed-21525aa3a020 | -8.1789 | -43.31559 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c0b5fc0f-3098-3e39-a042-e1f2e9c8f59f | -8.45677 | -46.126 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec36a54c-0e50-398a-8735-6f7d9b811543 | -7.51689 | -42.15751 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c2881e03-8207-3ee5-937b-1febeb3ace10 | -7.05284 | -44.27165 | 2025-10-13 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 754b864f-6a46-3b0f-b8f3-98d2c4771f26 | -8.47452 | -46.1654 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7a85b8c-3252-3bc5-b0c2-7d73e8bff7cf | -7.84185 | -44.52126 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51c3094c-c1db-3044-b738-2bbeb4409da7 | -8.22076 | -43.33681 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d12651b-f58d-3b55-a096-de633fb26f7f | -7.27103 | -44.15089 | 2025-10-13 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54cf81bf-4b9e-35ec-9b26-2490e30f213c | -7.69027 | -41.47335 | 2025-10-13 04:23:00 | NPP-375D | VERA MENDES | PIAUÍ | Brasil | 2211506 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| accf8f97-b7af-3837-9029-cdde28ca1f84 | -6.73768 | -42.15138 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ede38d1e-52fc-306d-9f3b-35469bb18376 | -7.50684 | -44.62929 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81e7363e-6669-344e-8bfa-c6a48b73235b | -7.92186 | -43.30747 | 2025-10-13 04:23:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bb0d9866-3eef-3f56-bdda-e54ace8300e4 | -8.22135 | -43.37883 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 47a82376-95f5-3b7d-85b2-970467e68df4 | -7.34891 | -44.08047 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8ca5560-e6ca-31d7-8847-97f1e3d795df | -8.45734 | -46.12243 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a424d73-5442-3e26-9ce1-956a5a5e17b0 | -6.74868 | -42.16796 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8025cd28-b723-36b8-ba6f-39523e3282fa | -6.73708 | -42.1553 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0017b104-08cb-3432-b493-ea574e4fcfcd | -7.48441 | -42.75265 | 2025-10-13 04:23:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 460ecd73-a675-3d4d-b8e0-7d3336252d62 | -10.78753 | -43.97094 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a03303e6-0f68-36c3-8630-dd96b5456f80 | -7.51578 | -44.65922 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3152a234-956a-37c0-8b9a-e6b6c92292c9 | -6.74632 | -42.15957 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fa672fb3-ac0b-32d4-9992-8d0e449b7d7e | -7.48324 | -42.76027 | 2025-10-13 04:23:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f3a2690-2d31-3129-958d-9a280d85e16b | -8.47573 | -46.13631 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a9b62e4-df7b-3597-8f0c-3cdbdf89d64f | -8.4818 | -46.16287 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d1c7417-561c-3e6e-83a8-6284b950b56a | -7.48907 | -44.61218 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fc24433-b2bc-3a12-aa78-c407a9ed3240 | -6.64988 | -41.38236 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cc27a242-0f42-3e97-a69b-5da19b1fd647 | -7.49298 | -44.63067 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b2214ec-246d-34b4-a6e8-47a57975932b | -8.23505 | -43.35806 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 890889bb-0929-382d-b1e4-7f76286919d3 | -6.82404 | -44.64659 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27733c91-2d7a-39ff-b0d1-026d156a20ed | -7.65706 | -42.56784 | 2025-10-13 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e4b79525-ea06-3b87-a045-277bb73daa82 | -7.84076 | -44.52824 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac3544a5-fcb9-31cf-8032-7ee900c1601c | -8.45456 | -46.11834 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0d7ad584-b88b-3fbb-be82-de5fbafd16a6 | -7.34832 | -43.85472 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 659c774b-b7c0-3a8a-af23-b29202ab25a4 | -6.27715 | -43.90588 | 2025-10-13 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17445365-f4af-3ff4-9b69-ea33100e2169 | -8.4629 | -46.13061 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba55141f-fe55-3296-9fc5-611f9d71fa42 | -8.46568 | -46.1347 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66c94ef9-c246-3316-a388-c9d5dddfd3e9 | -8.54345 | -44.59166 | 2025-10-13 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4306b86b-58f9-3bde-9ff1-7d52eb7b408f | -7.61996 | -43.04834 | 2025-10-13 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 531d6804-c7f1-309b-8af5-b3edfcd1cc9c | -7.62341 | -43.04886 | 2025-10-13 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ab022054-3eb0-39e0-88a3-52abba01d688 | -6.70062 | -45.97231 | 2025-10-13 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50f85692-9d72-3554-8b5a-15401156bf07 | -8.22705 | -43.34159 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 491bbb84-9140-3b0e-a2f3-54b59a006d51 | -8.32206 | -46.24634 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7edac65-824b-37a2-8480-5fc3c21d77df | -10.79894 | -43.98319 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6290c929-f632-37c4-8a0b-1e1e4053209e | -8.54066 | -44.58761 | 2025-10-13 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70c1f2a2-b36f-36ad-a086-44f46b648d6a | -7.6785 | -42.37849 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 81fa8f76-1bbe-37a8-8649-4bedbc607040 | -7.49741 | -44.62423 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0e96f89a-3ad3-3d02-a5b2-9bf6dbd5eec5 | -8.48237 | -46.15934 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77527e1c-d74b-3b2f-af31-3059b0011c9d | -6.42421 | -42.55024 | 2025-10-13 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dad7c26b-a267-3adf-a557-a4fe98a0182a | -7.15369 | -42.18556 | 2025-10-13 04:23:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 170c8618-00ba-33f1-9a30-9fa31f6177a7 | -10.03006 | -45.67953 | 2025-10-13 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3d7d48c-bd7f-30d2-b6c4-90d72d2ff00b | -6.82295 | -44.65355 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6578a996-5226-3033-8eb7-281ebd95a59c | -7.8424 | -44.51776 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0d09fcd-0032-3146-b9c4-a59eabfa2e73 | -10.80467 | -43.99167 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f7edda5-d7d8-3e50-9a53-02455ab88ace | -8.23047 | -43.34212 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 546a62ba-325d-3551-b968-2aafcff7bb04 | -8.40229 | -45.06425 | 2025-10-13 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1b6095f-d23b-310c-a0dd-f6e0e635e63d | -10.81033 | -43.97734 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b05a4455-726f-3810-af5f-099df65c11d0 | -7.26768 | -44.1504 | 2025-10-13 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bce40de9-496c-3d82-87b7-3d42a14c6db0 | -10.80921 | -43.98476 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e6b08b5-3be6-3900-9a09-f1f36d84b27b | -10.7881 | -43.96722 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b2709802-4728-33ef-b97d-f3ee697df559 | -10.79095 | -43.97146 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aeefec5e-9105-3aa6-be33-5baa956dfdfb | -8.46069 | -46.12297 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8379f2fc-0f65-30d8-8c8a-72b0655d2c85 | -6.76017 | -44.64741 | 2025-10-13 04:23:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4711a6d0-b3aa-3af7-b110-f4c627bb023d | -8.4495 | -46.12846 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f7b1edc6-e560-3912-9dfb-46199e5e2686 | -6.73979 | -42.20801 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 17aca3e6-5383-3bba-b360-d54efb4b9fd1 | -7.16019 | -42.19062 | 2025-10-13 04:23:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README20.md)
