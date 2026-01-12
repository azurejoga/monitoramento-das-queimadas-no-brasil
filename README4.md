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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51fcdff9-1e88-38e1-90dd-24ba8f91457d | -20.35552 | -40.95154 | 2026-01-12 04:23:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bbad4aaa-88d7-31ba-9826-10e604c23815 | -20.117 | -46.85844 | 2026-01-12 04:23:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9aa2da88-de94-3210-90ed-aae486387358 | -18.24964 | -42.62113 | 2026-01-12 04:23:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7e68fb31-d33c-3438-b171-31200427a929 | -17.32554 | -48.7907 | 2026-01-12 04:23:00 | NPP-375D | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42324673-48ca-39f1-9299-95ae424592c5 | -16.31269 | -45.10901 | 2026-01-12 04:23:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42a53686-d770-3482-9ee9-dc61bde08a81 | -16.05309 | -47.21711 | 2026-01-12 04:23:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57542866-dffb-3632-964a-4d730eb81748 | -23.39115 | -47.00874 | 2026-01-12 04:23:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b7752797-b916-32d5-82ae-98853498d362 | -21.01223 | -43.98533 | 2026-01-12 04:23:00 | NPP-375D | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 97f7536c-b760-33a1-9699-2cfb8f8c7bc3 | -15.51862 | -47.98802 | 2026-01-12 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5d1b7db-7bfa-3ddf-823c-39126fec1803 | -23.40608 | -46.42282 | 2026-01-12 04:23:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 663b8e74-a42a-3ea6-a779-e57775af0db9 | -20.1176 | -46.85477 | 2026-01-12 04:23:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c816a65-5f0d-3501-b161-d23bf293a9e5 | -13.04183 | -46.74632 | 2026-01-12 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e109b24-2aba-39dd-9729-3deccb529987 | -13.43175 | -43.85156 | 2026-01-12 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c04b8364-0f12-30fd-8dce-7a28848888f0 | -20.36016 | -40.94808 | 2026-01-12 04:23:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f6b7010d-9b4e-3ae1-ae03-b1fb0578b7a3 | -17.30264 | -42.67938 | 2026-01-12 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6229a7b3-fc1f-337f-989c-b465db6b8fb3 | -20.12093 | -46.85536 | 2026-01-12 04:23:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a05afc31-a223-3b90-a7f4-c62049c24f99 | -23.37482 | -46.0272 | 2026-01-12 04:23:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 513a6da9-3749-3181-9f1e-b7a440cd5b5c | -20.3643 | -40.9486 | 2026-01-12 04:23:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7a3ff251-9b45-3433-b911-c6cf4293c614 | -20.35606 | -40.94732 | 2026-01-12 04:23:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 416f0924-a653-3499-9e97-baa4de1e2a1d | -17.29905 | -42.67879 | 2026-01-12 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27ad0884-f164-33a3-82e7-dd96f2f1534e | -19.24045 | -48.67356 | 2026-01-12 04:23:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7399969d-9dcb-3509-b05b-91cd7ceb363a | -20.40722 | -42.35666 | 2026-01-12 04:23:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0225bc95-0f1e-379f-8791-6eb6db790c66 | -13.47872 | -44.01469 | 2026-01-12 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfc0422c-c38a-3192-8945-7401f1a1dc04 | -14.43541 | -46.24113 | 2026-01-12 04:23:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80a70615-991f-3612-adfa-a1b1e5443db7 | -21.01575 | -43.98592 | 2026-01-12 04:23:00 | NPP-375D | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 13290f60-4500-3d45-9ffe-469618ae1fc3 | -15.20651 | -47.84729 | 2026-01-12 04:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3afc9f0b-3117-3942-81ab-2c27dc92f271 | -20.11975 | -46.86272 | 2026-01-12 04:23:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b6b9e3c-c550-3356-9fd6-c8c9aab15755 | -17.29545 | -42.67818 | 2026-01-12 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51a58d13-db9c-3aa9-af64-9534ad54f9b6 | -17.32912 | -48.79137 | 2026-01-12 04:23:00 | NPP-375D | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 815b0fed-790b-32fc-98c8-ecb0ba741037 | -13.04527 | -46.74691 | 2026-01-12 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66abb56f-2265-3081-953f-ad37fe46e76b | -18.25025 | -42.61669 | 2026-01-12 04:23:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7717ded0-93c4-3ec7-abd0-3b504665d052 | -16.31326 | -45.1054 | 2026-01-12 04:23:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 198b9838-a4d5-3748-badc-3c1d84409e86 | -19.23976 | -48.67758 | 2026-01-12 04:23:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb8818dd-1347-3c5e-98dd-a21dff95be83 | -17.75506 | -43.42696 | 2026-01-12 04:23:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d35377c5-547e-352f-b8fb-cc56557a398e | -16.30993 | -45.10484 | 2026-01-12 04:23:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0107988-96a3-336c-8c6c-9c9270428df6 | -14.43439 | -46.24143 | 2026-01-12 04:23:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37579437-2449-3408-b162-92a01a0d1450 | -15.51794 | -47.99207 | 2026-01-12 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bcd76c3-b592-335d-a55f-541c2416d5ed | -22.56536 | -46.98522 | 2026-01-12 04:25:00 | NPP-375D | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b8dc2a4-46d1-3a91-976d-db88753467d3 | -20.40125 | -50.87302 | 2026-01-12 04:25:00 | NPP-375D | NOVA CANAÃ PAULISTA | SÃO PAULO | Brasil | 3532843 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a2a1b507-42d2-3e66-b975-d65d3ea907d5 | -22.67478 | -45.11115 | 2026-01-12 04:25:00 | NPP-375D | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99303ed2-f773-3b68-8c6c-46074437fa11 | -22.56869 | -46.98583 | 2026-01-12 04:25:00 | NPP-375D | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b6051af-63c4-30d2-ad1c-1b110e28f765 | -22.19597 | -43.01223 | 2026-01-12 04:25:00 | NPP-375D | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d6415498-d514-3836-a611-2ca5b6299b73 | -22.68225 | -45.10827 | 2026-01-12 04:25:00 | NPP-375D | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c434bfe9-1e9b-3385-bfac-b6db026e9471 | -23.01286 | -46.43757 | 2026-01-12 04:25:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f300d7dd-08fc-3b6b-b752-cf00c64f7e5c | -22.67881 | -45.10771 | 2026-01-12 04:25:00 | NPP-375D | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 647f07de-46eb-3fc9-8f1f-b6c992a94877 | -22.67822 | -45.11172 | 2026-01-12 04:25:00 | NPP-375D | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 03834a1d-ae18-3af1-8c79-04ca183ad9f4 | -0.08813 | -51.27977 | 2026-01-12 04:38:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4a4f3378-5896-3c7d-a1c7-034203f94196 | -3.59962 | -41.86816 | 2026-01-12 04:38:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 488eddf6-68c3-3ad2-b56a-3d6656081893 | -1.75511 | -53.41897 | 2026-01-12 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69fce0ad-2693-3cfe-8daa-11db0cefef3a | -2.57729 | -45.85167 | 2026-01-12 04:38:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47f37af3-f813-3f9e-8d58-564f61be1da6 | -1.85566 | -47.48323 | 2026-01-12 04:38:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 253843b3-b9e1-3fa2-90bc-54c5784ac617 | -2.57078 | -45.84653 | 2026-01-12 04:38:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18e1a385-5abd-3cb9-9ece-0fbdd028402a | -1.33179 | -45.83364 | 2026-01-12 04:38:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8a816556-3ef6-396a-b6de-94259336b2c4 | -0.09173 | -51.28032 | 2026-01-12 04:38:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 394aed77-45bf-3036-8b96-e1b8c6b9ed36 | -3.94537 | -38.39986 | 2026-01-12 04:38:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a515ef88-fff4-322c-85c3-f1fee26208b6 | -1.85232 | -47.48272 | 2026-01-12 04:38:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed1aa592-3374-379d-b1a2-c5050a441272 | -2.5135 | -47.57014 | 2026-01-12 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 979fd57a-7765-3911-b5fc-6fa4c15026dc | 0.65217 | -59.6534 | 2026-01-12 04:38:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a511049-4e09-36f0-973e-e8f7c8a12105 | -1.85288 | -47.4792 | 2026-01-12 04:38:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8beb1f22-cbf3-337b-aa81-0c1dfe3498b2 | -2.51685 | -47.57066 | 2026-01-12 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0de80503-d33c-353f-a218-872821f859fd | -3.94009 | -38.39474 | 2026-01-12 04:38:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 41ace3b7-6a00-3d2f-b2b4-9470f1761cb1 | -2.57791 | -45.84765 | 2026-01-12 04:38:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a486b34f-6e88-3238-8409-c9a5c2a037c8 | -3.53668 | -42.56022 | 2026-01-12 04:38:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 992e5237-5f92-3192-bef2-e70e494b4a3b | -3.93948 | -38.39891 | 2026-01-12 04:38:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0efe2d84-c827-38a5-bb70-c4618307cade | -0.08878 | -51.27565 | 2026-01-12 04:38:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 04a10beb-3a77-3a94-80aa-cacd1a6832de | -2.57435 | -45.8471 | 2026-01-12 04:38:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe539cd2-3c1a-32c6-97cc-53ff2477b144 | -2.26363 | -45.98569 | 2026-01-12 04:38:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e667751f-3415-3d72-8733-b7a064ed6aaa | -5.49642 | -42.15091 | 2026-01-12 04:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3c5a7e24-441c-3fc8-a1db-70f2fb12adfd | -10.37494 | -48.9161 | 2026-01-12 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dab4535-e321-38fc-b7b1-a0dcaf82f5f2 | -5.34129 | -43.364 | 2026-01-12 04:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad6e0fd0-ba35-325b-a19b-8103ecff05ae | -3.71954 | -43.32397 | 2026-01-12 04:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f005741-dff7-35ed-a278-757918e54bac | -10.38114 | -48.89824 | 2026-01-12 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec083e0e-741e-3fcf-9e13-d8c2f7f97fe8 | -4.70385 | -44.47642 | 2026-01-12 04:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41b955e1-da6b-3871-9249-eedabeeb615f | -3.72012 | -43.3201 | 2026-01-12 04:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa2fedff-fd5b-306b-b651-b4df3a2125b3 | -3.94321 | -40.70008 | 2026-01-12 04:40:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 75d4b5c6-cfe0-3fb5-804d-0565ac7ff410 | -4.7078 | -44.47706 | 2026-01-12 04:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8183cc4-cc9a-3136-b784-d466ddb4196d | -3.32128 | -45.9995 | 2026-01-12 04:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6711517a-12eb-3d43-8c26-ae3b434af8c0 | -5.49567 | -42.15588 | 2026-01-12 04:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b5ca5971-5d6f-3b72-b73f-e73ec9bdf786 | -5.49822 | -42.15314 | 2026-01-12 04:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 332cb153-88f8-362a-8272-07d0d511cf88 | -3.94828 | -40.70076 | 2026-01-12 04:40:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 34eda3b1-f4e7-3e26-9dc8-eb2b264d81cf | -5.49751 | -42.15813 | 2026-01-12 04:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5827432e-4dd6-3220-9f9f-abd0b5e90d57 | -4.21765 | -41.77295 | 2026-01-12 04:40:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| aea24997-dad8-3393-b9b8-35c5a4074f2d | -5.49353 | -42.15248 | 2026-01-12 04:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 43740cda-b3b9-37ba-8e46-1a15bcb54edf | -5.49492 | -42.16085 | 2026-01-12 04:40:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7526e676-ec3f-3dab-af92-51ac8ed8d8e1 | -3.79288 | -41.60453 | 2026-01-12 04:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c58f2deb-1dd3-356a-9887-e1cdd6ca6830 | -4.70456 | -44.47982 | 2026-01-12 04:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48ec4f6a-c377-3c7a-89df-4ef8d26b15fa | -10.38453 | -48.89875 | 2026-01-12 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4377ea07-dc31-3636-852f-d9fc04d25e9d | -12.31417 | -46.92289 | 2026-01-12 04:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87d293c2-c42c-3426-8bfb-8ca57b3984ac | -11.8869 | -44.71642 | 2026-01-12 04:42:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfc322b5-0443-3c9d-b1bb-fa3f3d73a7fd | -13.04456 | -46.74575 | 2026-01-12 04:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 10bb1133-6ec1-34f3-a6d7-c69b73e029bf | -12.31484 | -46.91825 | 2026-01-12 04:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0d676d7-478c-35ed-bb0e-abdbe202db29 | -12.5986 | -46.52813 | 2026-01-12 04:42:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ba5dddb-46c8-3a14-99f9-c2a7a98ddf1f | -12.3104 | -46.92233 | 2026-01-12 04:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ef27cd9-b051-35b2-aa79-d490a4275c61 | -17.30373 | -42.6781 | 2026-01-12 04:42:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 64b014d6-ee24-3e36-8c59-ae73d82b4b33 | -13.37951 | -53.5566 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc348735-046a-305a-bee3-dd2c7c52490c | -13.37408 | -53.56782 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79df285e-38d1-3008-92ef-b8692c7885a7 | -13.37603 | -53.556 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29469b84-f206-37a4-bfaf-c2673f633252 | -13.37885 | -53.56055 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07d0dc6e-a837-35f5-8031-d638142cca13 | -13.38167 | -53.56511 | 2026-01-12 04:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70c4b180-9e84-30bb-8725-d31e3aeda2f7 | -16.12641 | -49.88816 | 2026-01-12 04:42:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README5.md)
