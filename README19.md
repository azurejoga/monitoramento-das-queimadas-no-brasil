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
| bf3f1f1b-6ed9-36d8-883b-d4489ebd8ed3 | -8.5025 | -43.285 | 2025-07-09 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 177.3 |
| 54b04e1b-c66d-3c21-b410-b3a4e5852bee | -6.1792 | -48.0494 | 2025-07-09 04:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 25c3468a-35cd-3441-be5c-87b65c5be70d | -8.5028 | -43.2614 | 2025-07-09 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 45ac322e-9200-3a17-a404-b54f5411f8bd | -8.5214 | -43.2828 | 2025-07-09 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 169.8 |
| 98e57034-7b7d-39f4-aa8c-00774b886f84 | -8.5217 | -43.2593 | 2025-07-09 04:40:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 339486cd-1751-33a0-8310-69ad2a395578 | -6.89308 | -47.39608 | 2025-07-09 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ccdc4a0-2a0e-39d7-afcc-89a9611cb2ba | -8.12538 | -46.42211 | 2025-07-09 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e817f3d9-f103-37fe-8d57-5e785bab6543 | -7.09234 | -49.16337 | 2025-07-09 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bae069b-12c4-359a-ba6e-a57f6f98255f | -7.57212 | -47.06129 | 2025-07-09 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7256f22-d532-396f-b503-7fa4a78f5542 | -5.62864 | -44.26445 | 2025-07-09 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b540d440-0560-3447-830d-2cdcddbd81de | -8.50442 | -43.28331 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 70ee6ca2-b356-304c-ad98-30d14ec294f7 | -7.23159 | -43.07207 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4e4c85b4-704f-3db0-b07c-74f13ed5c8ae | -8.51451 | -43.27855 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 38e3b476-d23a-35a2-9b96-5531d4aa5306 | -7.65916 | -44.36678 | 2025-07-09 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7334daf-2647-3b8a-80de-d32b075c492d | -6.89683 | -47.3966 | 2025-07-09 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e69547af-bdac-3b71-9164-64e50f50ee19 | -6.63731 | -43.19382 | 2025-07-09 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 079c8584-115a-340b-bbd1-d69372efc06d | -6.17007 | -48.0531 | 2025-07-09 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3871247f-a513-3581-8336-3ecf6eefae01 | -6.73247 | -44.33704 | 2025-07-09 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbbf6230-8600-3985-8528-8f1ad654dab8 | -5.58823 | -45.33511 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c257818-c848-3ef1-a7f0-59274bc06442 | -6.86382 | -42.78682 | 2025-07-09 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 93880555-ba73-3377-8e3e-6304bd11aa40 | -8.51074 | -43.27491 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 0929264c-8dae-3fd0-8dfd-d76692c1dc74 | -7.24083 | -43.07933 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2d567e01-d952-3ab1-ba6f-d97d1c8d3ded | -7.22657 | -43.07132 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f277f694-d65c-3097-b728-016550355f7a | -8.0347 | -47.0184 | 2025-07-09 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d0dcf74-52f4-3aa4-9ce0-1740a8bb1050 | -7.67509 | -44.35434 | 2025-07-09 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 571a816c-a0fe-36fc-b71c-73dbb42b7b6d | -6.89375 | -47.39157 | 2025-07-09 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daa2a948-a595-37bb-885d-f6ba56839dc6 | -8.23063 | -46.96539 | 2025-07-09 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5eb5bef1-6379-3bcd-b7b0-b12d514024be | -8.39281 | -42.9376 | 2025-07-09 04:44:00 | NOAA-20 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63a3a71d-85aa-35ff-8120-52209480ec5b | -7.80814 | -46.5708 | 2025-07-09 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a69fe29f-5491-3c8f-8300-a8498368c844 | -8.17484 | -46.51289 | 2025-07-09 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c3e3cef4-0097-38be-9417-b422bce93386 | -7.6744 | -44.35923 | 2025-07-09 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad8b9e4d-5c87-3769-8a4c-2d968ecf3097 | -6.74371 | -43.16324 | 2025-07-09 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 98a6a737-c1d0-321b-95d0-4c8890c661e1 | -7.08676 | -43.42266 | 2025-07-09 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9b150348-4748-3a7d-99fd-369e5b35d6fb | -6.72858 | -44.33164 | 2025-07-09 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a07b16b-8367-3ce1-a453-0e87252453bd | -8.17988 | -46.50642 | 2025-07-09 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fd38eb0-a2b9-39a6-a164-11fb97013b7d | -7.23621 | -43.0757 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7f511263-3233-3569-b48e-a0a322c53c64 | -7.23788 | -43.06394 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ebcc4bf8-5838-3159-8b63-69a391070f37 | -7.45198 | -49.71561 | 2025-07-09 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4de57ca0-9f46-3aa7-b859-c4b81441f6c5 | -6.54693 | -43.62647 | 2025-07-09 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb9320c1-20db-32c2-8cb8-6485dd9cacee | -6.57076 | -48.2466 | 2025-07-09 04:44:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4722455d-136b-3d8b-8554-a05f7e9202eb | -5.58783 | -52.08548 | 2025-07-09 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12fcee7e-9592-30b1-82a9-6e204bef789c | -5.62411 | -44.2638 | 2025-07-09 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02ae536d-c5e6-3662-8517-44682aa88f9a | -5.49957 | -45.49137 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92e5a2cd-7fe0-3e29-9c5e-1e02dde49387 | -8.51328 | -43.29358 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 219ed8c3-84da-343f-bc02-908f942cff64 | -8.50668 | -43.29883 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 96f2bd4a-d7dc-35eb-8155-152739dbd820 | -8.04251 | -47.01948 | 2025-07-09 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2757f1ac-bca4-3745-96f7-7c2e2de349cb | -8.50708 | -43.29587 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0c068f9e-b331-39c0-b8f6-9f1f08ff1721 | -7.24165 | -43.07352 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3f1d262b-54b7-3248-b372-eedaf8c565e6 | -6.54764 | -43.62165 | 2025-07-09 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0736b716-f37d-3ce2-8a1f-87365fa8ca30 | -8.50786 | -43.28993 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ef15df64-f433-3091-9933-0b5ff6f06856 | -5.50427 | -45.48837 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d05e6711-1030-3c53-a752-fefaa3552ea9 | -8.51496 | -43.2816 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ec52ce96-afd6-370b-8f3a-564b281e91cb | -7.23201 | -43.06915 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7e73b282-91e3-39ae-8218-26b7ee79d408 | -7.67371 | -44.36413 | 2025-07-09 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faceefb5-566c-3c64-aeb4-432cc35faef1 | -6.68189 | -43.19986 | 2025-07-09 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 18f0295e-71be-35a9-89c3-6c26c52730f2 | -5.50012 | -45.4877 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8918b6d4-c54e-3c40-978e-e6d9a0dc8ef6 | -8.22965 | -44.93398 | 2025-07-09 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2aebf30-df5f-3777-8c0d-16b38b5d9c94 | -6.17366 | -48.05361 | 2025-07-09 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4e9150ab-bb97-3620-b6c1-2a43412a8821 | -8.50823 | -43.2929 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a6b46e80-7fa2-31fc-87a9-fc1a7d7cbd47 | -5.58896 | -52.07841 | 2025-07-09 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1fd19e4-9589-3bb3-b6b7-90edec426cf1 | -5.02607 | -56.19432 | 2025-07-09 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bb7e54e-989d-3cfe-8df5-85854336a3d7 | -6.85786 | -42.79208 | 2025-07-09 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7517d014-1319-379b-8b24-23bb29b913a6 | -8.5099 | -43.28096 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| f275d087-5471-3dcd-931a-ba73d11075da | -8.23029 | -44.92944 | 2025-07-09 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87f7a659-d816-3823-9d42-90f6003bedea | -7.24668 | -43.07426 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 91bc52ec-0a09-30aa-aeb1-2e3154a48ecb | -8.51331 | -43.28763 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 9b052e0b-564a-33f2-97c9-cb6c65963963 | -7.23746 | -43.06691 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 37394629-6456-38da-840c-db058e641fd7 | -6.16711 | -48.0484 | 2025-07-09 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b0cc712e-64ae-342f-98fa-6842ceaeb125 | -8.22516 | -44.9333 | 2025-07-09 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ccce9e9-21d1-340e-8d35-5a4547a2d3f2 | -8.51412 | -43.28763 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b0d3927-cf74-372e-a08b-9db26af4e942 | -5.23 | -45.21453 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34a2fe60-c25c-3ff6-bcfd-c1b4e396c34b | -5.2306 | -45.2106 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4551059a-e05b-3aba-975b-ebf7e3df2147 | -7.66308 | -44.37246 | 2025-07-09 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffb2a217-cc0a-3f98-9412-fe1d7ffc05db | -5.23056 | -45.21423 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a30131c6-1738-3686-bb8b-e9781fa61dc6 | -5.58857 | -45.03613 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d02dcdca-683c-3b94-92b8-58bce3fcf187 | -8.51024 | -43.27182 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 2264e132-7032-3a9e-952d-b23ef11d29ef | -8.24381 | -46.95729 | 2025-07-09 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05a69441-f0b9-3eab-ab5a-e6a691dae4ae | -7.2358 | -43.07858 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 70e9c102-b64f-3887-9e24-b929ffda1d36 | -7.24249 | -43.06763 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 776878e5-809f-3d8d-896a-166ebb084d43 | -6.63769 | -56.27194 | 2025-07-09 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81ce3daa-2278-390c-a8cb-bd2318f32f83 | -8.15023 | -47.62751 | 2025-07-09 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64c90580-8645-3e51-9a85-1ff9e89c76a2 | -5.59287 | -45.03669 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81c012ed-49ba-3418-b38e-9d32a97484cd | -7.09176 | -49.16713 | 2025-07-09 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4fdec98-ab7c-38ed-a82e-048e9087c2c9 | -8.17938 | -46.50994 | 2025-07-09 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d717800d-b8b9-3740-aad7-caf635e49c29 | -5.58766 | -45.33898 | 2025-07-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 671eed32-b635-3c38-8ace-dbdb24c4cdcc | -5.96414 | -44.17825 | 2025-07-09 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb7118e7-a2f1-3542-a07f-3fc03eea9508 | -4.77909 | -45.34919 | 2025-07-09 04:44:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44960bd5-6f1c-30f7-ac5f-e93c8cbab521 | -8.27346 | -42.27576 | 2025-07-09 04:44:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 04b1ffc5-9e45-3356-a0dd-fbcd67758749 | -7.24207 | -43.07061 | 2025-07-09 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e13c17db-c5fe-345e-a119-4a3e0891c5ec | -8.504 | -43.28629 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 4db87ccd-effe-3560-b8e8-65e90de6f229 | -7.08832 | -49.1666 | 2025-07-09 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a5382617-49bd-3736-8154-acf54f35f90a | -8.51371 | -43.28462 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 129be8c7-e166-3354-a142-5e28701c6e53 | -8.5074 | -43.29882 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 76c573ad-8c05-348e-93b0-475e2248d645 | -6.85742 | -42.79515 | 2025-07-09 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1de358ab-a535-35c1-a9c1-2935da35d930 | -8.50747 | -43.2929 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ca270430-d41a-3fd6-acea-4805a50faccf | -6.56781 | -48.242 | 2025-07-09 04:44:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de64e3c6-efd9-3281-ad11-064e1876fb1e | -6.57138 | -48.24253 | 2025-07-09 04:44:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d579a991-3145-3324-8f7d-02c2f887919f | -6.8583 | -42.78903 | 2025-07-09 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6a1a99f8-06d3-3cb0-af03-f0af0ff31446 | -6.63679 | -56.272 | 2025-07-09 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9142e238-6ad0-30bf-9d03-6bc1896b13b7 | -8.50825 | -43.28695 | 2025-07-09 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |


[Clique aqui para ver as próximas entradas](README20.md)
