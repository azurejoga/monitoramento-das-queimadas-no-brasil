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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90eba761-26aa-331b-ba02-98892b808322 | -14.11094 | -45.51964 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| d8d18a2e-26dc-346d-b38a-959ad2273862 | -14.11015 | -45.52419 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 207093e0-1bbc-3262-80ef-82c132709ec9 | -14.10934 | -45.52877 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| b5979795-2174-3c00-a803-0f1653d11d91 | -14.10881 | -45.5099 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1499a7f2-42db-3b2a-ab49-98ae3870ea70 | -14.10853 | -45.53336 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02365e65-1d7b-33b7-a866-3b83a81308c1 | -14.10802 | -45.5144 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 675dc46d-57ef-3c35-a24f-500866108c12 | -14.10723 | -45.5189 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 63485fe5-71ef-3401-86d5-1b756822599b | -14.10643 | -45.52346 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 361b5570-7bbe-3455-a4b6-149528db7a66 | -14.10562 | -45.52807 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| c029982e-0f71-381e-90a5-83686e277e87 | -14.10511 | -45.50912 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fba8bd17-1f0f-38f4-8c71-b3c454aa3b15 | -14.10432 | -45.51363 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d1e8f3f-7496-3683-9f17-2988ceb788b8 | -14.10352 | -45.51817 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 375ed66f-3ecb-3ec6-95bd-322b2532bb4b | -14.10271 | -45.52276 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ccaab25-ef98-3ea3-95bb-fd86ea2b3783 | -14.10263 | -45.51517 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf6b20b4-b4a0-367e-8949-b2b1341e33d7 | -14.33187 | -42.34203 | 2024-10-07 04:02:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c73c4aa0-763e-34b6-af2d-b610afb575d9 | -13.92712 | -42.55783 | 2024-10-07 04:02:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ea1ad8f2-a5da-3439-bf25-e9fbf37b1fd0 | -13.82192 | -44.63228 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ffc9c9b-563a-368e-831a-d8b4c1c59a87 | -14.68491 | -45.13455 | 2024-10-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| de96693f-592d-3bf7-b1a6-0015ea3bf59b | -14.68418 | -45.13884 | 2024-10-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 00f0324d-1a6a-31a0-b64f-2690c31d44c1 | -18.62672 | -41.51117 | 2024-10-07 04:02:00 | NOAA-20 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3253d65e-8f1a-3e54-bb1a-bed19cf6c711 | -18.60714 | -41.50434 | 2024-10-07 04:02:00 | NOAA-20 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eac73430-7042-3c85-946a-3f6106bec8d3 | -18.60659 | -41.508 | 2024-10-07 04:02:00 | NOAA-20 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c1861364-f97d-358b-8cdf-ec7746fa6b4a | -20.19905 | -41.83097 | 2024-10-07 04:02:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d641270-cccf-30e1-a38a-3871dae73536 | -19.64957 | -41.48555 | 2024-10-07 04:02:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3439de63-a029-3254-9e51-72d352f3aad0 | -13.81762 | -44.63587 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a192156e-8e59-3af0-ba35-7305162da3d6 | -15.83614 | -42.21963 | 2024-10-07 04:02:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e379a07f-7ca6-3a49-a51a-9e1c7fbf6ed5 | -15.79236 | -42.28186 | 2024-10-07 04:02:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3dc9e0a3-e6cb-3b7c-a509-3bb7cf8e47f2 | -18.03853 | -42.07354 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4d4de2f6-82b2-3558-b1c5-a2cc6743ee43 | -18.03609 | -42.06974 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26437a7d-9142-3145-b864-6a0242db41ec | -18.03552 | -42.07337 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d8af45a7-a66d-3c14-8822-74188df61d0b | -18.03277 | -42.06919 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| acd694f1-5e9a-3b3e-8ac3-87074014de86 | -18.0322 | -42.07283 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 01a2b8da-dc14-3c34-bb9f-e46686759c13 | -18.02776 | -42.07954 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3d69efbc-c81d-3ca6-b9e8-bff210bbd198 | -18.025 | -42.07536 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3aab95db-9980-3fae-8896-67ae6de3e5c7 | -18.02444 | -42.07899 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 47e2954c-284f-3de7-bee0-6b16d5235e16 | -18.01329 | -42.12907 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 220e4f27-a78e-31ae-8405-8be5b7bb83bd | -18.01166 | -42.11766 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fadc14d9-7336-33f2-bb20-7584b5cbbf4d | -18.0111 | -42.12127 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 19c8d467-7cf8-35a6-bc74-45028b59448c | -18.01053 | -42.1249 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 71c7923a-3835-380c-a262-971eda8fbdd7 | -18.00997 | -42.12854 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 74688546-ab7d-3796-84d8-6d012589d1ad | -18.00834 | -42.11711 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a0f6d2ba-e342-3aca-b0df-da53843de862 | -18.00778 | -42.12073 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4154e41-8723-31c5-bc98-665141e6d8d2 | -18.00722 | -42.12437 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f9e060ca-be9e-3feb-89b8-18a0f16267e7 | -17.99785 | -42.29381 | 2024-10-07 04:02:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 853f73fc-514d-37b4-91a4-1a1f97abb882 | -17.99454 | -42.29325 | 2024-10-07 04:02:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d20a9b77-90f6-37cf-a489-cbfc0e2bb29f | -17.78088 | -42.80912 | 2024-10-07 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f50f1df4-78ab-322f-8f3c-8a1b6245b636 | -17.60994 | -42.55829 | 2024-10-07 04:02:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cac85d9b-2f10-3c2a-803e-097f1abbe7b5 | -17.38658 | -42.66082 | 2024-10-07 04:02:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cca3e0c-6e67-39ed-bef2-cb792751f78e | -17.3811 | -42.65247 | 2024-10-07 04:02:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d80a9dbe-2dff-30c3-a1ac-bf1e9043875f | -17.38053 | -42.65608 | 2024-10-07 04:02:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb4a08f3-c501-3c20-9bfe-cafba77f9551 | -17.37551 | -42.66632 | 2024-10-07 04:02:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f636fbc-acef-3b68-afde-d91f44a9b8c7 | -17.22911 | -42.60458 | 2024-10-07 04:02:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ffcb6754-ff83-39f5-83ad-48536378a14b | -17.84516 | -42.22704 | 2024-10-07 04:02:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bfeacb26-7cef-3f06-9969-d72b584aed96 | -17.84185 | -42.22648 | 2024-10-07 04:02:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d6b84ec4-0389-3349-bf1b-1c50d444be20 | -17.83854 | -42.22593 | 2024-10-07 04:02:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 99b63bf3-b4e4-387f-b81c-86b197759013 | -17.83798 | -42.22954 | 2024-10-07 04:02:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 394f7e13-a1f3-3ba6-b5d2-43ca1e71dfc2 | -17.83427 | -42.62183 | 2024-10-07 04:02:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4fdeed1c-df8e-347e-84df-283447c173d6 | -17.74208 | -42.21378 | 2024-10-07 04:02:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b589225-5d86-3515-9fb6-d152f4308948 | -17.74152 | -42.21738 | 2024-10-07 04:02:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d3ebd6a0-9e31-324a-bab2-cab2879c3b58 | -19.27811 | -42.85641 | 2024-10-07 04:02:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 002f04b4-1f4c-3dd2-a88a-74f6c0de3aaa | -19.2748 | -42.85584 | 2024-10-07 04:02:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa578603-2cb4-38a1-addf-8c1c7bcf5635 | -18.86406 | -42.89767 | 2024-10-07 04:02:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e3f55223-1646-3640-bebb-69672ca716f9 | -18.86348 | -42.90131 | 2024-10-07 04:02:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 0556d624-a1f5-33be-b411-fc93d0ae5db4 | -18.86291 | -42.90494 | 2024-10-07 04:02:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| f97b1e80-77e2-33cf-9482-88a14cba5dd5 | -18.86075 | -42.89709 | 2024-10-07 04:02:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bec1fc2b-45c7-3b03-83e5-84986bb3f3b4 | -18.86018 | -42.90073 | 2024-10-07 04:02:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 053b436f-ae39-3f2b-b682-ba01681703df | -18.8596 | -42.90436 | 2024-10-07 04:02:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 39cd1915-4889-3109-8199-9aebcb910e4a | -18.85687 | -42.90015 | 2024-10-07 04:02:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dd65187b-6b66-3604-9012-a9a0db1081b7 | -18.6998 | -43.05599 | 2024-10-07 04:02:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d0682178-62c7-39d2-9261-846e61f27c25 | -18.69649 | -43.05541 | 2024-10-07 04:02:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2e361aee-353e-301b-a299-032d8a46d636 | -18.628 | -42.05926 | 2024-10-07 04:02:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b6457d58-a299-30aa-8834-cbe660500181 | -18.47176 | -42.43261 | 2024-10-07 04:02:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67654838-c146-3c6a-a323-95bf871c90c3 | -18.46958 | -42.42477 | 2024-10-07 04:02:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 45754a08-827e-3f0f-ac19-4ad534dfcb53 | -18.46901 | -42.42841 | 2024-10-07 04:02:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f4154a2a-85be-319d-8f67-4b2fd51cfbaf | -18.46845 | -42.43203 | 2024-10-07 04:02:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6ed4f31e-df32-31df-b665-cdfc4a997932 | -18.46788 | -42.43566 | 2024-10-07 04:02:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6f3caea7-fd7c-3e6c-a1b7-699fcb2cc83b | -18.4674 | -42.41694 | 2024-10-07 04:02:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 575a2bac-8371-36ec-a1a1-804de381eee5 | -18.46684 | -42.42057 | 2024-10-07 04:02:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5f249b06-ffd9-37b1-a434-ebccee03dfd1 | -18.46627 | -42.4242 | 2024-10-07 04:02:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f857c55-2a50-330f-8424-c153ffae856f | -18.46409 | -42.41638 | 2024-10-07 04:02:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1583ba74-0bf2-3c0c-93eb-35aad6d7f9f3 | -18.24678 | -42.21972 | 2024-10-07 04:02:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8e8ee16c-21cf-3dce-a1fd-83ed1b21fcd0 | -18.24072 | -42.21499 | 2024-10-07 04:02:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 413f37bc-0e56-35fe-a996-f416ec19fde0 | -18.18585 | -42.99731 | 2024-10-07 04:02:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 50f51e29-9feb-33eb-9400-cc6ae66b2cb3 | -18.18527 | -43.00093 | 2024-10-07 04:02:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a2e4435b-1ed6-37b9-9e32-95de0e5fca56 | -18.1508 | -42.66129 | 2024-10-07 04:02:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b4a55568-e151-3c89-8aec-ab357f050770 | -19.43079 | -42.13549 | 2024-10-07 04:02:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 39308ff3-df40-3127-9272-909a727a9309 | -19.06637 | -42.18819 | 2024-10-07 04:02:00 | NOAA-20 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 81a9a1a7-d585-3043-b2c7-4f43e37a0080 | -19.30925 | -42.56992 | 2024-10-07 04:02:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6d69b64f-6ad0-32a2-af18-2733b35fd0b1 | -19.30868 | -42.5736 | 2024-10-07 04:02:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0fdd50f9-0b2c-35e8-8640-ea5bbac3f5b8 | -19.28825 | -42.57377 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| d5bf30f7-c92f-3a27-bc02-aa344be1b408 | -19.28768 | -42.57743 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5a2eff24-8826-33bb-b53b-c0931939cf8f | -19.28494 | -42.5732 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 2c0659b9-7c01-3d94-9d09-92a033d18716 | -19.28437 | -42.57685 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 23935dac-fae3-3711-8f6e-c5a1ccaee82b | -19.28106 | -42.57627 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2a322e7d-428a-388b-91b0-646185476772 | -19.20405 | -42.52663 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 65f12016-301b-3d48-9938-bdd9f63f1a18 | -19.20348 | -42.53028 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ad3a0eeb-171d-3ef7-9c84-22e3a92336a3 | -14.67842 | -45.12882 | 2024-10-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86fa2bdd-306d-374e-9508-057eea5e291d | -19.20074 | -42.52605 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ca0b8ac7-ab69-3bb0-ad16-623e9f1ed749 | -19.20017 | -42.5297 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 31c3f805-bc2d-36aa-a532-f34554f255fa | -19.19743 | -42.52549 | 2024-10-07 04:02:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README65.md)
