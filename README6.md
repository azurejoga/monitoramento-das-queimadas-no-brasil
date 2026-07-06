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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46cbbee4-d326-3224-abaf-9d4b34186b27 | -13.2408 | -54.32126 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3da551f2-d4c9-3fe9-a27a-2314a4a3e069 | -11.92619 | -43.37981 | 2026-07-06 05:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6c957740-2669-3987-87d3-cd841a04b5cc | -9.67422 | -54.34489 | 2026-07-06 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01c47c8a-8c7a-3ffc-a002-7e2b4b73de7b | -13.22446 | -54.31485 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 124527a0-6068-34e9-8764-47010be2343f | -18.93585 | -47.44715 | 2026-07-06 05:06:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2fba9cb-5aea-393e-ae92-ae6ce8e721af | -18.93451 | -47.4459 | 2026-07-06 05:06:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8ed27ba-6a3b-3670-8f49-93b961125fd0 | -18.93993 | -47.44669 | 2026-07-06 05:06:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d883dc54-9cb1-3c3d-91fe-f97303f716dd | -20.50034 | -45.24873 | 2026-07-06 05:06:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2bcafd04-b330-3d59-8813-eedf8d4e85bb | -20.50664 | -45.24979 | 2026-07-06 05:06:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bc657a66-6eba-3745-ba49-029865ab09e8 | -21.05749 | -47.25809 | 2026-07-06 05:06:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f9b0f3f-28da-366a-ba81-e4ec0751d83c | -18.93621 | -47.44355 | 2026-07-06 05:06:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52607151-31af-30f7-9358-0b8cf2ea941d | -21.06318 | -47.25829 | 2026-07-06 05:06:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62438bc2-99b4-37f3-8558-a90d653da046 | -10.92605 | -43.05408 | 2026-07-06 05:44:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 23d0886c-5365-3e09-824f-9326140de0f2 | -6.21518 | -57.77438 | 2026-07-06 05:48:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f341428-a057-3e67-9d97-85c186a481df | -10.39591 | -56.77616 | 2026-07-06 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 793f10a4-4bbd-35c4-8c8c-f86e9e54c64e | -9.25151 | -60.33137 | 2026-07-06 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d01e7477-0f66-3303-9bbd-8a4ac1591162 | -9.96647 | -64.96255 | 2026-07-06 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 518cd5c8-177a-3954-901e-1b62cbb14d76 | -13.29745 | -54.38622 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5910a82d-8352-370e-9931-fe4c99e55f60 | -9.5278 | -68.95478 | 2026-07-06 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd1f6b64-53dd-3fc0-977d-264a3f6e149c | -9.2121 | -67.39675 | 2026-07-06 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fb85d47-1a1b-3582-b02f-51a481b51d92 | -13.24634 | -54.31997 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2679efc-6f5a-346d-b60c-fe502387c8b4 | -13.29237 | -54.36411 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a7b4416-79f6-3119-8e71-70c156f459b8 | -13.30243 | -54.3695 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4599831e-8360-3739-ac5f-579f020d2597 | -13.28821 | -54.36744 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0a97dd42-a645-364d-8ace-d6e30b4f5580 | -13.28892 | -54.36042 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e6bef884-9e05-34fa-ac86-fbcd3ac73389 | -7.88184 | -72.4613 | 2026-07-06 05:50:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5304cbc-72b3-3812-83c3-201e07d4488b | -13.24976 | -54.31874 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 09f66c5d-24d0-3d84-91eb-4566dbb8fae0 | -10.39645 | -56.77179 | 2026-07-06 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c721c2f4-17c9-3ada-a413-ec8f09260e7c | -9.21264 | -67.39329 | 2026-07-06 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 300d7ebf-2ce7-379b-b04f-aec197d6b29f | -13.29604 | -54.36146 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e629f1df-633e-32ad-936c-f333cc5e415b | -13.29813 | -54.3792 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc6ea704-4916-3a9c-b324-f9925930e90f | -13.30172 | -54.37643 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ed664de1-dc55-3d03-970d-2d21d55bc79b | -9.2154 | -67.39728 | 2026-07-06 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad8d6f28-7d2d-31b7-b23d-36d37792b455 | -8.71752 | -54.54174 | 2026-07-06 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 793f1bbf-723c-3188-aa5f-48261c0acf53 | -13.24262 | -54.31772 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30c52f68-0699-3bda-bdc5-2e1b6903d4e0 | -8.33528 | -64.02879 | 2026-07-06 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc223df0-17b5-3020-a627-41396996d6a7 | -13.29881 | -54.37214 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 038e4a5a-bbcf-3e59-b5b3-4c518bfd5bf8 | -13.25347 | -54.32091 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14aa4d4f-541b-31ab-926e-4e489be0538f | -13.29306 | -54.35691 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f11c1c98-09fa-3fd2-b55f-04af4eabf30c | -9.21156 | -67.40022 | 2026-07-06 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3ec362f-317f-3f50-b351-de364e82a04d | -13.29949 | -54.36516 | 2026-07-06 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84aa9f29-5e10-3467-a095-d41b0263ab84 | -9.21594 | -67.39381 | 2026-07-06 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f03e7dd3-398c-35cb-b5d6-c57d7d9fff70 | -9.21545 | -67.39662 | 2026-07-06 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37f61c2d-1e57-37d1-b537-c3544433154e | -9.21028 | -67.40051 | 2026-07-06 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efa213e7-1cce-3414-9cd5-8caccb192d0b | -7.88514 | -72.46141 | 2026-07-06 06:25:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b66ee95-bb14-3a2f-8ec4-0915cb317147 | -9.21093 | -67.39597 | 2026-07-06 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f337119-043b-3d75-ac2c-7bfb916f7782 | -9.20829 | -67.39823 | 2026-07-06 06:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4efc74a8-962d-39be-b418-9ab246fbccbd | -9.2112 | -67.3943 | 2026-07-06 06:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70e64f70-cf82-3768-8f11-f11cedcc11ad | -7.88187 | -72.46132 | 2026-07-06 06:44:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65d27230-ecdf-3652-bce9-b0186ef158b6 | -9.21047 | -67.40038 | 2026-07-06 06:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c87b3e4e-3490-30f5-879a-1d4d9907fdb4 | -9.21506 | -67.39909 | 2026-07-06 06:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa97756e-bff7-3e2c-8d73-a810e1f5fc2a | -6.2126 | -57.77375 | 2026-07-06 07:22:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45f714e9-4188-3d88-879d-8fe466089181 | -13.28188 | -54.35123 | 2026-07-06 07:24:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 43fe8dc8-6b25-3ae2-a8e0-47ff5e42b27a | -13.2856 | -54.35709 | 2026-07-06 07:24:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| e251e2ad-bc04-3e3d-8024-3af030bfce7c | -13.29416 | -54.35299 | 2026-07-06 07:24:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| a98c5191-cdb1-3d06-8d02-01ae2beddab3 | -13.2969 | -54.3861 | 2026-07-06 09:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| deb1b1dd-064d-37e4-bfdf-18c0e1ad54df | -6.21136 | -46.8797 | 2026-07-06 11:45:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 71c0f15f-e06f-3c3f-b153-e3b3e505961d | -6.77417 | -39.19873 | 2026-07-06 11:45:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| a919eb1c-9295-3d49-817b-e84fb78ac762 | -4.63539 | -43.04729 | 2026-07-06 11:45:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b02ab9f9-8b7f-313a-97f1-668fc6afebaf | -6.8839 | -39.36042 | 2026-07-06 11:45:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 44e7176b-82e1-346f-98f2-0faabe3b4f28 | -6.93807 | -43.72148 | 2026-07-06 11:45:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0de78ec6-fb94-3ea8-b2db-07cc931ce4bd | -6.86956 | -44.67286 | 2026-07-06 11:45:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81d870d9-aed8-3589-a6e4-8494f14e0153 | -6.00732 | -45.08831 | 2026-07-06 11:45:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4a304454-3c2b-3328-863c-59705c989b1f | -7.00093 | -43.86473 | 2026-07-06 11:45:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4b26d4ea-91ec-363a-af84-38092c0bff5a | -6.77673 | -39.17865 | 2026-07-06 11:45:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| e8e6dafe-1eba-37a5-9499-bc64c063439a | -7.24102 | -47.10159 | 2026-07-06 11:47:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3b196572-cc84-3d8b-8cf7-8737da310628 | -11.92554 | -43.37525 | 2026-07-06 11:47:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 89dab731-b398-3b2b-bc3e-51e48e9be5df | -7.66771 | -44.23931 | 2026-07-06 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aea8ae07-8dc6-38a7-89ae-1236feda7f5c | -7.90095 | -48.25206 | 2026-07-06 11:47:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2b1b8fe0-2d94-397c-ae87-39eb10109421 | -11.46527 | -46.62145 | 2026-07-06 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fc254f3b-31cb-3803-a5eb-1dd50710fbda | -9.37344 | -48.8036 | 2026-07-06 11:47:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| decaeb34-d8ce-326d-9171-557f2b299382 | -14.27475 | -47.41525 | 2026-07-06 11:47:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 14ced58c-41d4-33ea-a622-97bb0614f1ee | -8.11458 | -47.12362 | 2026-07-06 11:47:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 96b53b5a-244a-3514-b554-9c334d9ad7e4 | -13.3093 | -54.36079 | 2026-07-06 11:47:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e7b43bb4-d5fa-31bf-bee1-7ddcea433d7b | -12.92134 | -51.86732 | 2026-07-06 11:47:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9be87924-e842-390d-a633-bf42b9704c20 | -7.24239 | -47.09231 | 2026-07-06 11:47:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 791596e9-2d67-3670-bf50-62b2ace5369f | -8.00976 | -44.16909 | 2026-07-06 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1a9ca9b6-0344-3d9e-a3c8-656ae782d8f8 | -7.64826 | -45.29303 | 2026-07-06 11:47:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c1b71857-f058-32a1-b156-50011172c6ff | -11.44232 | -46.63897 | 2026-07-06 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d18d4e1e-f898-398a-8fc1-70476df087a0 | -8.11591 | -47.11448 | 2026-07-06 11:47:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c22e69be-9bb7-3a6e-bd5a-a1eb771ffbe5 | -8.07537 | -46.69579 | 2026-07-06 11:47:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92e9f210-e06b-332c-b01b-4d2f0b54d102 | -11.46666 | -46.54897 | 2026-07-06 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1cd09e7c-7674-3df9-ae9d-c0c3d6af5964 | -7.6664 | -44.24876 | 2026-07-06 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ae607f69-d061-39df-bd97-6519ca80f25b | -11.44359 | -46.63007 | 2026-07-06 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 3c8e7157-f2f4-32b7-ab1c-e5724570c2ef | -7.647 | -45.3019 | 2026-07-06 11:47:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 44a428b1-e85f-3356-b380-e267e7e4437b | -17.54964 | -46.5462 | 2026-07-06 11:49:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eb01d5fa-4914-3b26-b693-83faf79c0199 | -12.5138 | -48.2581 | 2026-07-06 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 66fbc712-3833-3b99-b85e-d0ae0c45ff57 | -12.5138 | -48.2581 | 2026-07-06 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 7954da22-5e08-3203-a970-0df49c28025c | -13.2972 | -54.3655 | 2026-07-06 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 278cb689-7389-3db2-b9ba-2f7958ae3507 | -12.5138 | -48.2581 | 2026-07-06 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 39480bea-2641-3bbf-abae-20b9764e41f7 | -12.5138 | -48.2581 | 2026-07-06 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 1dd8b060-d8dc-3afb-b976-03a6c1a66f22 | -13.278 | -54.3675 | 2026-07-06 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ea2b9a95-4389-32fa-a183-58a2d9e55fae | -13.3163 | -54.3634 | 2026-07-06 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0cbf16ab-55f8-3dbb-897b-d5822e1a96f6 | -13.2972 | -54.3655 | 2026-07-06 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| ee8f1fa5-eaf1-37d1-81e3-fa9288bd9df4 | -13.2972 | -54.3655 | 2026-07-06 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| df4277ea-ab95-30bb-b190-f6fab6aa2ead | -12.5138 | -48.2581 | 2026-07-06 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| a0194580-f15d-3ba3-99b4-74e65d92defc | -10.8467 | -46.3582 | 2026-07-06 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f584dac3-4364-3231-abc0-bd6fb386f692 | -13.3163 | -54.3634 | 2026-07-06 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 82fa54df-5b46-35a1-9518-53cfd2d22e8b | -13.2969 | -54.3861 | 2026-07-06 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9ed6206e-1248-3172-97fa-1412a4169700 | -13.278 | -54.3675 | 2026-07-06 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |


[Clique aqui para ver as próximas entradas](README7.md)
