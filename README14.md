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
| 049230e9-ec19-382e-bba2-06bbeb2aa358 | -12.27206 | -43.17271 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| f53827ce-cc07-3ee7-b19f-96e5447d1fb1 | -17.15479 | -39.50926 | 2026-08-22 03:45:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2f8e069f-821e-3a4f-af27-c341d28a8b3a | -11.4405 | -44.55548 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ac8cd79-7dd3-3e6a-9655-9086a0aefc68 | -17.96763 | -44.40528 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1145cb08-9dfd-3119-9009-38ea9d1879ae | -14.12382 | -48.06879 | 2026-08-22 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9301823d-c5ce-3f3f-9adb-934618468628 | -13.0888 | -43.33883 | 2026-08-22 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 51dea2e7-d980-3148-afd1-58f27bab0129 | -13.99949 | -42.47869 | 2026-08-22 03:45:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 5a4b6bc0-1037-34cd-bb06-297ec8fc4362 | -11.73584 | -45.58821 | 2026-08-22 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9417c93e-be3c-34ea-8ab5-ff2f2e155ef1 | -17.92527 | -44.41935 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58e7601c-568c-3027-8047-355c46c01f07 | -12.27903 | -43.16259 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3a21df72-1edb-3afe-aa72-f985af43610e | -15.81166 | -38.9145 | 2026-08-22 03:45:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c5274952-fa82-3b74-a671-523a087a211d | -12.26126 | -43.17638 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2d31a639-1503-3851-be6d-22bc2c5e7b29 | -15.18368 | -48.75082 | 2026-08-22 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 500acea1-f214-3769-88c0-d5612e813ac6 | -10.30521 | -48.22914 | 2026-08-22 03:45:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a013c1e-856f-39fd-9d7d-b130f19a430b | -12.71797 | -48.42154 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f032f284-4886-3901-b260-5f3ef663c7b6 | -12.24454 | -43.18456 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bb2f0128-bad8-3079-9cab-07a070216c96 | -18.66122 | -43.17349 | 2026-08-22 03:45:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c08728dc-241e-3568-b7a0-4636479fbfb9 | -13.52992 | -40.64902 | 2026-08-22 03:45:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b91cd20e-bb13-3a0a-9005-1f594e792ab9 | -11.45039 | -44.54065 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14218c59-bfc9-3c74-be18-4b1eece6dd89 | -17.56405 | -47.89008 | 2026-08-22 03:45:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbea0272-9e25-378c-b273-70dd547e9bfd | -12.27316 | -43.16689 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| cb4429fb-c825-398b-900d-f240fc27aafd | -12.25199 | -43.18555 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c22e5801-c73e-30a2-8ac5-b92f7adb2ed4 | -18.27481 | -43.31419 | 2026-08-22 03:45:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e1d5615-819e-3ab0-a6fd-2a4956601ab6 | -15.52057 | -45.86341 | 2026-08-22 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dee86a79-11b6-32f5-85cb-c0827e11cf85 | -18.33918 | -42.47233 | 2026-08-22 03:45:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f2faed4e-ad92-37f5-881b-11d90ce5f736 | -11.35023 | -46.35363 | 2026-08-22 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df5a76c2-d578-36fa-aafd-424280c2257a | -18.72837 | -42.22893 | 2026-08-22 03:45:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9c7720d9-9166-3ab9-8210-cbebf0890e4c | -17.95915 | -42.73131 | 2026-08-22 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2a8c3285-d510-3f37-9a71-40d79c4c1d92 | -12.27534 | -43.1554 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ee6ea37d-f65c-3421-862a-88daf61889dd | -11.59066 | -46.57982 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5dea497-e651-31c5-a21b-6377e811653b | -11.43917 | -44.56256 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd50f680-8651-3e58-b1dc-2866776c7c1d | -17.56505 | -47.88564 | 2026-08-22 03:45:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c8a0247-3979-3944-bc09-0e4bbf9d3f2a | -12.77649 | -48.38953 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e74198d3-03ad-3960-a9c8-e1b93dd73804 | -11.95311 | -45.4915 | 2026-08-22 03:45:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 96088373-a874-3e20-8b54-f7cf5c9e4a75 | -11.43475 | -44.56313 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fdc77e4-73d8-3b03-90f1-98b781330794 | -17.91798 | -44.40621 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01a36799-ddcc-385b-a32f-fe81d065ddf7 | -17.56223 | -47.88621 | 2026-08-22 03:45:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 772d6277-cb2e-3fe9-9225-311821839d10 | -18.34068 | -42.4643 | 2026-08-22 03:45:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 221b8845-a3e3-3575-b2c1-63809d0b40be | -12.44031 | -43.4021 | 2026-08-22 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a85560da-538c-3fba-a39e-bdb5abd6d42c | -17.9146 | -44.4231 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1e910e3-62d5-3847-85a6-3853e1019f91 | -14.94331 | -41.33029 | 2026-08-22 03:45:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ac6f1385-05ef-3f23-9570-eee198de8b4d | -11.44154 | -44.55718 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7abaec4-3cc4-3ce6-a540-e9f9b1a1c01a | -11.59534 | -46.55598 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 48a04989-39aa-389f-804c-b42b7375dc23 | -12.78315 | -48.391 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65025748-8fd6-3c98-b16a-de83eb5a2fed | -17.95999 | -42.72687 | 2026-08-22 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9e6ba7c3-e2b2-373b-8883-1714cba4466f | -12.75642 | -47.1104 | 2026-08-22 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 739133f4-db5a-3313-b471-12945b5fa7ec | -11.11546 | -46.19231 | 2026-08-22 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 975c119f-1caf-3263-ac0e-bc77358cf0cc | -17.92033 | -44.3945 | 2026-08-22 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e884621-82ff-3229-9315-4da7e2abefc7 | -15.97625 | -44.80863 | 2026-08-22 03:45:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e3909b4-7e52-32b1-a2ca-b3b83709bf56 | -16.42924 | -39.51646 | 2026-08-22 03:45:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e784e46f-d1d3-32ff-bf1a-9fb6600531df | -14.61852 | -42.53136 | 2026-08-22 03:45:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fbe51535-6b77-3232-b0e0-5465beb4dee4 | -16.42848 | -39.52081 | 2026-08-22 03:45:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ceb3451e-448c-374a-ab49-63b90ee68057 | -11.44383 | -44.5378 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a78ac1c0-c1fe-3ef7-b454-ff7c66f5cad2 | -14.1375 | -48.06737 | 2026-08-22 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd97e4bc-7bf1-3ce8-ac1b-94aa2ee3896e | -15.51586 | -45.85952 | 2026-08-22 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6902e286-3211-3a18-820e-cfedcced9fd2 | -14.12992 | -48.07157 | 2026-08-22 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 087caa76-0db0-3abe-8b12-4eb01a558a6f | -16.48575 | -47.94164 | 2026-08-22 03:45:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1b38141-b77f-3afa-99c0-5b6bd4142669 | -12.2801 | -43.15692 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 52572c5f-4e03-33ab-9b37-569d56f59a5d | -11.43613 | -44.55609 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c8c3400-527a-3376-a37a-60ea5d0efbe2 | -18.48469 | -43.86884 | 2026-08-22 03:45:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e4b12f4-d50c-3c0f-976f-ba17bae4cb4e | -13.08632 | -43.3362 | 2026-08-22 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2ae554ee-bcb9-367a-9d9c-45960ef25117 | -11.584 | -46.57913 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4598811a-2409-3a8c-816e-a255074a7255 | -10.29885 | -48.2252 | 2026-08-22 03:45:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a36c4cfe-58f8-3bde-8bb9-a0385f449cd1 | -12.24938 | -43.18567 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d8ef585a-1d6d-312f-bdf9-9705b28f9ddb | -18.6569 | -43.17253 | 2026-08-22 03:45:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b82ba917-019d-3b8c-9657-e6f94993bfba | -17.96423 | -42.72787 | 2026-08-22 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c7970472-15b4-39c4-9383-22014c238e2e | -16.48388 | -47.95053 | 2026-08-22 03:45:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9af9ffd1-e2f7-3dad-96bd-2c28ed188416 | -12.27426 | -43.16112 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e01be958-402c-334a-9730-4002032f3a0f | -16.71475 | -47.70754 | 2026-08-22 03:45:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74181f3b-82c4-37f7-af3c-b746d1cb9e24 | -11.84035 | -39.18401 | 2026-08-22 03:45:00 | NOAA-20 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7adeca86-6725-3479-84ad-ff069e8719b8 | -12.2476 | -43.12719 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ca0ddd2c-c9fb-34c4-ae3a-d5bb2c614d0a | -12.71132 | -48.41995 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2dfb434-9ed8-366e-8ee7-cbd72ace806b | -11.59718 | -46.54663 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 004b9499-2485-37c1-bf0b-0fad2293fb18 | -18.27565 | -43.30989 | 2026-08-22 03:45:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 152109f4-c6f1-36e2-8302-480d3396ef60 | -15.17849 | -48.74331 | 2026-08-22 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7131eaaf-f353-3cbc-8a91-88f18f2cc134 | -12.26721 | -43.17165 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 535d91d0-d5ae-3dc2-b34f-06390a0aab2e | -11.58459 | -46.57831 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ed46a33-70fb-39ce-a413-5038deadbbfc | -11.43544 | -44.55961 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9ccece2-c7c8-34bd-b720-895648a5b03c | -12.26609 | -43.17754 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| dacebfea-ed25-3638-a910-c7fb5d4f1287 | -10.30569 | -48.22973 | 2026-08-22 03:45:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7afc0960-7e1b-3790-b349-16c21a13dcf5 | -12.74024 | -48.46176 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a23640c-f88e-3640-b768-5df36526da55 | -11.62772 | -46.52039 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25a85127-30f3-32c1-aa16-67d31d813772 | -12.26235 | -43.12897 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 50f70204-b709-3825-9f89-e46832f5116d | -11.73011 | -45.58699 | 2026-08-22 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0539e374-d5dc-331a-806a-8aca56a3fa6b | -11.44449 | -44.53428 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 637f6190-8d88-3e38-a836-fe47e59d4d62 | -14.00047 | -42.47985 | 2026-08-22 03:45:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 52282d96-dc85-3aa5-a4b4-d986e43298f8 | -16.71588 | -47.70229 | 2026-08-22 03:45:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b28cee8-8c4d-347b-95bf-625883e4c76f | -11.58301 | -46.58399 | 2026-08-22 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8464b04e-6937-3e10-8d66-c7c663c69838 | -12.27094 | -43.17861 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| fb1723a0-38da-3b33-b99c-e272e828b4c3 | -15.44383 | -41.38437 | 2026-08-22 03:45:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5231ab88-8dd0-318b-ade9-2dc00c9bceaa | -17.96337 | -42.73243 | 2026-08-22 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a885a67d-d811-3e6a-b6a2-df492d456589 | -17.97134 | -44.36172 | 2026-08-22 03:45:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69c10616-ce8a-3b00-a8bd-bd611364b893 | -12.73903 | -48.46748 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff5f44b7-ed3a-3eb5-8d3c-95702bcb7c34 | -12.76975 | -48.38848 | 2026-08-22 03:45:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 72f989e1-83da-3058-a730-eb55ad0e7649 | -18.2671 | -43.69918 | 2026-08-22 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb680e49-6c3e-362f-84d7-cc3763ad0a87 | -12.82856 | -48.47419 | 2026-08-22 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a135bdf2-3f5e-3c60-afda-01402e6466fd | -11.44085 | -44.56071 | 2026-08-22 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2694d34-c9b2-3161-bf4c-35d8702525e2 | -12.24716 | -43.18436 | 2026-08-22 03:45:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2f59892a-9873-3c8a-8295-44b2cc6238f2 | -18.72451 | -40.89886 | 2026-08-22 03:45:00 | NOAA-20 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b4f9fd00-d6f2-3114-91e7-a47288161075 | -17.96086 | -44.36477 | 2026-08-22 03:45:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README15.md)
