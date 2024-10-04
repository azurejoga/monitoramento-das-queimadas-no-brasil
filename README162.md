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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a588a986-8bc3-3307-875c-b3357779f70c | -15.89504 | -57.15495 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea42c577-624e-3a82-b5b1-6de1eec581a7 | -15.89446 | -57.15851 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9d13d9e-d0c2-383a-99cf-40622423c9f5 | -15.89229 | -57.15075 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd9d4edb-42e1-3a77-a2c1-e476c9bda141 | -15.89171 | -57.15434 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7884861b-107e-37e9-9b98-1afcb6a06c7e | -15.88564 | -57.14954 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea29659b-3019-3d0e-9782-d7aaad94f632 | -15.88507 | -57.1531 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d254b3ea-80da-398a-b4a4-54d9fa0cbd0a | -15.8829 | -57.14535 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc075619-9452-3414-9b1b-bb3c2a8c450f | -15.88232 | -57.14891 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7e12766-8a7e-3fc2-afcd-ed0a8ad39ca9 | -15.88073 | -57.13758 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b9f9233-ac70-3564-b205-70ca042e52ac | -15.88015 | -57.14116 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 534b4472-ccd7-3359-bc07-d8b2935e8942 | -15.87957 | -57.14473 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8eb2bcba-905c-3fef-aff3-e72dd4407062 | -15.879 | -57.14829 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0d3baf0-cf00-3663-9e81-6c10b1fc7dc9 | -15.87856 | -57.12978 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbfa825a-a6cd-3bf6-bba6-af4f480837c8 | -15.87843 | -57.15185 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2255bf28-5a96-3b3c-ad16-9e93c5349473 | -15.87799 | -57.13337 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 753da3d3-74fc-321c-8f58-6f22877d2175 | -15.87741 | -57.13698 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5028a9b-230e-3b9f-a776-df2ee53efd51 | -15.87683 | -57.14054 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88d5b3a3-eecc-3f15-bd36-bc684865e2a5 | -15.87452 | -57.15487 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 425a75f2-5286-3e18-81de-bc349b30eaa2 | -15.87293 | -57.1435 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ae4e540-ebf4-33bc-a9cd-519bd13ae301 | -16.4735 | -57.44427 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| e96d5399-ca12-353e-bc2e-2a8de9f076c7 | -16.47135 | -57.43638 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7c087fc4-8db4-318b-b9ce-c1fe4302b52e | -16.47016 | -57.44369 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 031ba8e9-fabb-361f-9b80-f8fd0e052baa | -16.46801 | -57.4358 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 564fdfb3-cab6-3ec8-b167-cf5f1afbda8d | -16.46742 | -57.43945 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5a8cb656-65d7-37f1-8888-8bb143ddea7a | -16.46349 | -57.44252 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6756331b-3beb-34d1-b8d4-947ffadeb998 | -16.44955 | -57.44384 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f82f3e97-d118-3ed5-9cb5-09fda86029c1 | -16.44896 | -57.44749 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| ed251ffa-80bf-3fe9-b2d4-77f22c0f6cc1 | -16.44562 | -57.44691 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c585b4d7-2bc3-3564-8363-7731e696300f | -16.44502 | -57.45056 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| bbfb3dec-7026-3fba-bf8a-9801bf725dc6 | -16.44443 | -57.4542 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 21256f7e-243e-3548-ace6-85b392d6b04f | -16.44384 | -57.45785 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 8037fb8b-fd4d-3148-bf03-6af4a8bc1b53 | -16.44109 | -57.45362 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| efdc678c-d81d-3725-8aca-215d2a334cc1 | -16.08612 | -57.53172 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 478ef573-f75d-3a3a-9473-11a6bfa6e1e1 | -16.08277 | -57.53112 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8d5ab4f4-f125-3ba3-81bd-90c031102ba5 | -16.08217 | -57.53491 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e04e75e1-cb46-33ab-a90b-f7f22c61ba08 | -16.07943 | -57.53054 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d78ac8c7-8e84-3a43-9f86-b9f741fc0e8d | -16.07668 | -57.52621 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 581e858b-8e59-37a1-9db2-b63abca3a443 | -15.93982 | -57.46551 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98c714fa-9e86-31a4-bed3-3e6634e8b961 | -15.93647 | -57.46493 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4a78750-8e43-3b02-b3d1-3f4afeedec2e | -15.93372 | -57.46069 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf2e4804-1082-3236-ac8d-ea907e746dd2 | -15.71019 | -57.43379 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f91d7e5-8893-350a-8896-3affecad8365 | -15.70744 | -57.42953 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5123d1fd-92d4-3e74-a050-2e46b3c37445 | -15.70684 | -57.43321 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5081077b-44cd-33ef-a149-289b117e7f7d | -15.7041 | -57.42894 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c413177-c221-39f6-8d7d-7dc9d09a3b6e | -15.7035 | -57.43263 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05988daf-c0f6-35e2-916c-a3c2afb74252 | -15.70257 | -57.41721 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be0bd33f-e627-3c6c-9c4e-36452de02f91 | -15.70196 | -57.42093 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71f607fd-ce68-3a1d-a121-6887ad93feb5 | -15.69588 | -57.41603 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01ac4f48-f21d-3b88-a63a-3c1024d69255 | -15.69466 | -57.42351 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96d207aa-bd99-39a9-ba92-e9530d9acccd | -15.69131 | -57.42295 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff9c4e99-8ebc-339b-a961-62ddade9bc29 | -15.69071 | -57.42663 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 097713fd-60cc-361f-a1d2-eaa7d916c9f9 | -15.68857 | -57.41866 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49cd0b37-127b-3e61-b089-183b5159e404 | -15.68771 | -57.44499 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d281a80-5d96-306c-b324-d2a5651fa3f2 | -15.68711 | -57.44865 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b529d3c-56e4-3b2b-919a-c92c58c89b63 | -15.68522 | -57.41808 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e104da08-2df7-359e-a907-f69339eeb91a | -15.68496 | -57.44074 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e1209b7-7798-3073-b712-5ff9e14a7fda | -15.68436 | -57.4444 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7aed9ebb-4047-34d3-88ed-19ac0af0af05 | -15.68376 | -57.44808 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbbf2fc0-c803-38e9-81d7-f6096ae48a90 | -15.67457 | -57.42007 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa6d3906-cb12-3b33-af19-2246d7366a27 | -15.65305 | -57.41299 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f257ca6-4958-3279-b6dd-929ec1085b17 | -15.57531 | -57.46746 | 2024-10-04 04:57:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89071d0e-1d29-3887-bb2d-aeb1d6aa7070 | -15.57471 | -57.47114 | 2024-10-04 04:57:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 212e692b-764f-36bf-b403-d6398be096d8 | -15.89721 | -57.16269 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aab559b5-42cf-309a-bd91-42d414bbb4d5 | -15.88839 | -57.15372 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecf55412-c103-3f1e-a709-499a43eb111c | -15.88781 | -57.1573 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26d5d1b2-2fce-32a3-987b-08d2d6bc806e | -15.88175 | -57.15247 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3828c60d-fb52-34ca-9c03-852079da2e80 | -15.87568 | -57.14769 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b75669a1-b39f-3f6c-9216-989bc661d224 | -15.8751 | -57.15127 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6404f9e0-592f-3633-b5ba-77a718d4e775 | -15.79425 | -57.3392 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98e9daa4-7e85-3961-a66f-6acc5ab9661b | -15.79367 | -57.34273 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd46317a-59df-312b-8881-d4afca1180dd | -15.79033 | -57.34216 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6fea64c-806d-32fe-84ba-f0991afcf57f | -15.78857 | -57.35306 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9eb4c6e3-ea6b-3ead-b596-d1d1d7339253 | -15.78757 | -57.33801 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80b0f308-1128-399f-b345-7ac100e12ba1 | -15.78738 | -57.3605 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 056a3c0c-1bac-3180-b63a-4505cf21b878 | -15.78404 | -57.35997 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff92c74c-541b-3ce5-aea5-8b604b50c733 | -15.78069 | -57.35944 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 563d78ed-f7c9-373e-90ae-d4f298a817c6 | -15.7746 | -57.35464 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47953e6e-79fa-3850-8886-8b3afe3055e1 | -15.70531 | -57.4215 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a655f44b-a6bb-367a-98fd-997dffeecc30 | -15.70135 | -57.42466 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff47176b-8c17-345a-94af-25e0b0979f8f | -15.70075 | -57.42837 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9eed977-1ce7-3eee-94e8-260ead7a3cca | -15.69983 | -57.41291 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf680565-e6c1-31e7-94bf-9a0a56650686 | -15.69707 | -57.40872 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1063738f-e404-399a-b4c5-e147f44f296a | -15.69527 | -57.41979 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 837ffcc7-a5ad-3b63-82b2-01297a1b485b | -15.69253 | -57.41547 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 579115fb-7c84-305f-949e-500ca17ca3e8 | -15.69192 | -57.41923 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6460e0de-82cb-357f-9930-73a895913a13 | -15.68705 | -57.40691 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90eb5c18-c766-3651-aac2-157ee4d75ef9 | -15.68187 | -57.4175 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a9cb926-2ad9-3f73-885b-52d86e159f8c | -15.67853 | -57.4169 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2b721d6-3c15-39c9-8f4e-ff2063dd29a7 | -15.67792 | -57.42064 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 238b3c08-422f-3b90-ba0a-9494e2b716ad | -15.67219 | -57.40091 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68c9c559-0964-3e66-a2f4-e95228216175 | -15.65545 | -57.39809 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df486403-09d9-31fb-9cee-fa091393e01f | -15.6527 | -57.39384 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b27a551e-57df-32c2-84c0-223c537fa392 | -15.6509 | -57.40503 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 822580f7-978f-3720-b943-bc8283e46055 | -15.64935 | -57.39331 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ad0b09e-77a5-32a5-8ac8-32fb275c70aa | -15.64875 | -57.39705 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed20a919-aa1a-3eb8-962c-21f3ce8cd36f | -15.64815 | -57.40076 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16782750-9aa5-3b19-af82-c2e9619387e2 | -15.64755 | -57.40447 | 2024-10-04 04:57:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a167be4e-2ef9-3a30-8581-a50e123a005a | -16.5718 | -57.25458 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b35798c0-aff2-3f1c-9c81-a271f174bf9c | -16.57135 | -57.42654 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d593bc12-1f09-3b6f-8dee-614212aa6eea | -16.56926 | -57.29145 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |


[Clique aqui para ver as próximas entradas](README163.md)
