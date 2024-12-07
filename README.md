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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56e1b48d-017d-3b1b-a658-6002a21bfe03 | 2.745 | -60.3913 | 2024-12-07 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 32af08c7-0510-3f28-96df-ce73bd91f0fb | -15.2722 | -53.5698 | 2024-12-07 00:00:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 1ea3836f-15ee-36dd-af77-3eb721aecc33 | -12.2944 | -45.4958 | 2024-12-07 00:00:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 7dc25b25-7e07-3af2-9452-82ddbd3e85d4 | 2.5247 | -60.982 | 2024-12-07 00:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 187.4 |
| ba08ef56-5cee-31de-af9f-390c420b783f | 2.5065 | -60.9822 | 2024-12-07 00:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 245.8 |
| 548095bc-f975-3104-9884-15f0ac0036f0 | 2.5247 | -61.0009 | 2024-12-07 00:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 110.7 |
| a0aee2be-648b-3bc6-a5e3-8e07ddcf5154 | -8.9434 | -44.2373 | 2024-12-07 00:00:00 | GOES-16 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 260d593d-f872-3288-a2fb-c0e75f525075 | 2.5064 | -61.0012 | 2024-12-07 00:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 3eae31da-b38a-3a73-a71a-8f9f909c2bec | 2.7267 | -60.3916 | 2024-12-07 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 10704c95-bf84-344e-babc-c70c2bbec75e | -15.2528 | -53.5723 | 2024-12-07 00:00:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5c2fdf4e-4ad8-3b7a-915e-c25b1e74606b | 2.745 | -60.3913 | 2024-12-07 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 060acfda-536a-3ae6-84bd-9de603c0562d | -15.2528 | -53.5723 | 2024-12-07 00:10:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 75f90883-0980-381c-878f-9299f05e77fd | -12.2944 | -45.4958 | 2024-12-07 00:10:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 14588d70-abb9-36ec-b034-19a9fbfb530f | -9.7988 | -36.1213 | 2024-12-07 00:10:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| c02d1628-a574-3db1-bc81-e95c924ba0b3 | 2.5065 | -60.9822 | 2024-12-07 00:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 216.0 |
| 82990428-132b-3152-a15e-4de8eb00ac25 | 2.5064 | -61.0012 | 2024-12-07 00:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 6a671ec7-61ba-3ac4-8450-c065705133eb | 2.7267 | -60.3916 | 2024-12-07 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 68ef6e71-5e25-35bc-a574-ae04b0acb5ab | 2.5247 | -61.0009 | 2024-12-07 00:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 9a8ceed7-e1c2-3710-905d-5880b8728d75 | -9.7983 | -36.1484 | 2024-12-07 00:10:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| bc766983-fd93-3287-8174-d2aac9eab248 | 2.5247 | -60.982 | 2024-12-07 00:10:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 3b4d9709-a5c2-36b7-b020-efee07fb7abc | -10.4453 | -36.775002 | 2024-12-07 00:15:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 15efbe01-561f-3849-bd40-65d352e56c64 | -14.9006 | -40.367298 | 2024-12-07 00:15:00 | METOP-C | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1755e5ae-ba75-32b1-ae6e-76b00790ceb0 | -5.7685 | -46.542599 | 2024-12-07 00:15:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 538b2ba7-2491-33d3-acd3-fe526c4222bd | -12.2938 | -45.491402 | 2024-12-07 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c08802e-64d4-3f98-bf06-dcb2ef0c0676 | -9.1063 | -43.195599 | 2024-12-07 00:15:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 34d0a7e8-c976-3133-8883-1127bc88a23f | -12.296 | -45.502499 | 2024-12-07 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 634e9684-dec2-320f-8a9d-fd901e18f9d5 | -9.5258 | -35.920601 | 2024-12-07 00:15:00 | METOP-C | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e685c8b-02f0-3ac0-a4d6-b85f98d4fce0 | -9.802 | -36.121601 | 2024-12-07 00:15:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd2b7244-d49e-3a64-a0be-481122bf54d3 | -8.2762 | -48.024399 | 2024-12-07 00:15:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c844bde0-98db-3508-9ca2-63641ece4a19 | -6.8407 | -44.3834 | 2024-12-07 00:15:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acf18d0c-730c-31fa-b392-5a6382a81a0a | -9.8068 | -36.141399 | 2024-12-07 00:15:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 56e83adf-1c54-3757-bd77-fe735045be5a | -7.082 | -45.194901 | 2024-12-07 00:15:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 152f19d0-40eb-38e1-b026-523b2456e0fd | -20.068501 | -41.8591 | 2024-12-07 00:15:00 | METOP-C | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 901476d2-302f-3885-bfba-dd1e317692f2 | -4.6014 | -45.1745 | 2024-12-07 00:15:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f35c5a9-55f4-3e0d-97c0-b10c71fc9069 | -6.2055 | -46.0597 | 2024-12-07 00:15:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f529d989-b8f3-38aa-82c1-0eb43a4feeaa | -9.9759 | -36.328098 | 2024-12-07 00:15:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bdf4af38-a810-3f7b-ac5f-21d48d985027 | -9.797 | -36.143799 | 2024-12-07 00:15:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 111577fd-a327-39c7-b57d-ad50a3655cfb | -8.9351 | -44.238499 | 2024-12-07 00:15:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 559d12ae-29fa-3fd2-b80e-38080a50aa93 | -9.6191 | -36.049301 | 2024-12-07 00:15:00 | METOP-C | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf92cbf6-919b-358c-a835-2b8a9828b7da | -8.937 | -44.246899 | 2024-12-07 00:15:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 00f8551a-9c86-35c7-bc89-4c2f83e9b161 | -11.0558 | -45.382401 | 2024-12-07 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eddbf12b-1b84-31ba-a28e-84526a74b69a | -10.6632 | -44.498402 | 2024-12-07 00:15:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96dbef19-85ab-39cf-8a51-fb4e358843dd | -9.8044 | -36.1315 | 2024-12-07 00:15:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ed69634-837d-37b7-bed3-4bdc32c5fe01 | -8.9272 | -44.249001 | 2024-12-07 00:15:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c24aee8-548d-3fe0-86a0-8ef51ea68a2d | -11.0536 | -45.372002 | 2024-12-07 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56f9bd5f-ca90-380c-9964-6792aeabdf05 | -8.9388 | -44.255402 | 2024-12-07 00:15:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 41919bb4-8f3a-3caa-8a8c-001e1e7cf4d8 | -14.9022 | -40.374401 | 2024-12-07 00:15:00 | METOP-C | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83244192-dc06-3aba-a514-50ad436f3ffe | -18.118299 | -42.673901 | 2024-12-07 00:15:00 | METOP-C | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6fe67f7a-1056-3c9e-82b9-f1c352a33ab8 | -5.7707 | -46.552898 | 2024-12-07 00:15:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ff188b4-db29-3ae8-8ce5-18a875cefcff | -9.7922 | -36.124001 | 2024-12-07 00:15:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b681f6c6-9055-3ef8-9d2b-37cab4c8e76c | -4.4209 | -45.653198 | 2024-12-07 00:15:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f79fa1a-aee7-37e3-8b5b-3836091cf327 | -4.5995 | -45.166199 | 2024-12-07 00:15:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d12c9da2-febf-3533-8271-2a4947f55e15 | -10.4475 | -36.784 | 2024-12-07 00:15:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14e0615d-c081-35ba-97b6-72cdb96ed469 | -9.1046 | -43.188 | 2024-12-07 00:15:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 94132422-0a48-3dcb-8768-e76c26cb6fc0 | -10.5381 | -44.679798 | 2024-12-07 00:15:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99e3af66-e244-3481-93b3-804b86cd6f58 | -10.6612 | -44.4893 | 2024-12-07 00:15:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f6948157-11d2-325b-84f4-4f50e2753395 | -11.0634 | -45.3699 | 2024-12-07 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa30f8e1-a040-3e80-85df-b0ff45dbd44e | -10.3912 | -44.7113 | 2024-12-07 00:15:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 62bb3f28-947e-3a1c-b2de-41c54ab33c27 | -9.9783 | -36.3377 | 2024-12-07 00:15:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b3d6d17e-6188-3a42-afc1-402d63933a4c | -4.4229 | -45.6619 | 2024-12-07 00:15:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f98aa1e-e047-3f69-9922-34c121343e39 | -9.7946 | -36.1339 | 2024-12-07 00:15:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df51c5fd-7287-3e1e-a662-e22dd1c68579 | -8.9253 | -44.240601 | 2024-12-07 00:15:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c0a34810-229e-3d21-813c-b1829ed1eeab | -12.2886 | -45.515701 | 2024-12-07 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab7c919e-d0a0-3e41-bd60-e676a4e1f371 | -11.0656 | -45.380299 | 2024-12-07 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5561ea44-8443-3201-b529-e28a487edb0f | -7.0839 | -45.203899 | 2024-12-07 00:15:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b88c444-7b55-3440-bfba-92f120f50263 | -20.058701 | -41.861301 | 2024-12-07 00:15:00 | METOP-C | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fba56efc-aab3-31d6-b811-e945c8b4528d | -12.2863 | -45.504601 | 2024-12-07 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a72668bc-e60b-3967-a3a7-ea5ceb137233 | -12.284 | -45.4935 | 2024-12-07 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef5efd2e-6f0b-379a-83a5-9e0c1eaf3426 | -12.2817 | -45.482498 | 2024-12-07 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6359d492-60d9-3dd5-b719-a334c53900b5 | -6.454 | -45.744598 | 2024-12-07 00:15:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f05fb22-1664-32d7-a689-a87dddad7ee7 | 2.5247 | -61.0009 | 2024-12-07 00:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d071c31b-50f2-3c25-bec3-4fe75f49596c | 2.5247 | -60.982 | 2024-12-07 00:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 8283f94f-726f-376b-8c00-c4ffdb7cae6c | -15.2528 | -53.5723 | 2024-12-07 00:20:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 397e277d-e2b4-3a5e-a77f-1ac89c357e13 | 2.745 | -60.3913 | 2024-12-07 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 66ab98b1-76ab-3de9-839b-7ee138114c42 | 2.5064 | -61.0012 | 2024-12-07 00:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 97.5 |
| e698ba24-794b-3da2-8473-70058304f4ea | 2.5065 | -60.9822 | 2024-12-07 00:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 223.2 |
| 0b7a452e-5807-3a0a-a29b-d4577cd6f164 | -12.2944 | -45.4958 | 2024-12-07 00:20:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| c2fea724-bf5d-3758-a0de-7d3a04c32c4a | -15.2722 | -53.5698 | 2024-12-07 00:20:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| be4bb1b3-4a1f-3d86-99b4-33c60047f6f5 | -12.2944 | -45.4958 | 2024-12-07 00:30:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8ef2bbb2-5844-30a1-971f-f9b46f57e2d6 | 2.5064 | -61.0012 | 2024-12-07 00:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 5712aedc-3f2b-3e49-8c47-f028527f9783 | -8.9434 | -44.2373 | 2024-12-07 00:30:00 | GOES-16 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 29ae8bd9-98a2-3f6f-966c-b7ade95d1b61 | 2.745 | -60.3913 | 2024-12-07 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 7ff27c20-fef8-3c84-99e3-0cf09ddd768a | 2.5247 | -60.982 | 2024-12-07 00:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 522a6381-df32-3e3a-9b6a-4507748fb668 | -10.441 | -36.7855 | 2024-12-07 00:30:00 | GOES-16 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| e622a1cd-982b-3ce4-b7b8-7390e0a02b72 | -15.2722 | -53.5698 | 2024-12-07 00:30:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| e2083956-25ca-3473-a41d-695648bc10a3 | -12.2752 | -45.4987 | 2024-12-07 00:30:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| b283d944-1ef6-37f5-a53a-21b21d86d722 | 2.5065 | -60.9822 | 2024-12-07 00:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 207.2 |
| 5401f327-7806-379a-ac1a-cf74d29c4989 | -10.4603 | -36.782 | 2024-12-07 00:40:00 | GOES-16 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| 1613047c-4447-3b77-a53d-56464b250534 | 2.5064 | -61.0012 | 2024-12-07 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 20994cd1-b2df-3b30-bc0d-4c55f206910f | 2.5247 | -61.0009 | 2024-12-07 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 96899d07-af9f-37b3-a4ae-9876db0ec875 | 2.5065 | -60.9822 | 2024-12-07 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 149.6 |
| d5ddce6f-7a7a-3feb-a00f-fb5638996ee0 | -12.2944 | -45.4958 | 2024-12-07 00:40:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| d4d8cdb3-53cf-3a27-9db7-679e44626b07 | -15.2722 | -53.5698 | 2024-12-07 00:40:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ca19e5b8-0188-354d-b526-2b92b5d39ed2 | -10.441 | -36.7855 | 2024-12-07 00:40:00 | GOES-16 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 109.1 |
| e6c16f47-b330-353d-9b6a-fd0ebccef6fd | 2.5247 | -60.982 | 2024-12-07 00:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 536b1696-2762-322e-ad66-e8cc9904593b | 2.745 | -60.3913 | 2024-12-07 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f982c5f7-74b2-3e95-b48e-6830de6e3eee | -15.2528 | -53.5723 | 2024-12-07 00:40:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| eba29c47-4465-3dde-a071-9cbb7c6f13e6 | 2.5065 | -60.9822 | 2024-12-07 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 3d8135b8-d805-3932-8165-ae99a9f95256 | -15.2722 | -53.5698 | 2024-12-07 00:50:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 79a16832-9482-35fa-b293-43da5bef1732 | 2.745 | -60.3913 | 2024-12-07 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |


[Clique aqui para ver as próximas entradas](README2.md)
