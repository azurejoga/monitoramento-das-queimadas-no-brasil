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
| 0ffaa91c-aa97-3983-94c5-83d68d81f1b4 | -11.1639 | -43.57231 | 2026-01-17 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2732bd4-55e0-366e-b5b2-baeccf7ae726 | -11.93646 | -44.61535 | 2026-01-17 03:57:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37012600-ca5b-3204-8929-65d21eeb38f1 | -11.79858 | -45.36747 | 2026-01-17 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf8c825a-797b-3150-86f9-45875f56515c | -11.53043 | -47.69101 | 2026-01-17 03:57:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7050bdff-94ef-3f45-a051-cc44ef45c207 | -14.75281 | -45.91033 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71fb6eb0-ec97-337d-b358-db65ffd6141e | -18.41775 | -42.70293 | 2026-01-17 03:57:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 15ef8acd-9e48-31f7-acf4-58d6fbc91f44 | -14.74803 | -45.91332 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ad9f93b-08ea-3915-bad4-23b6860d9543 | -12.20026 | -43.95252 | 2026-01-17 03:57:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9c06b82-81d1-3f08-8a17-d0aaf5e23dad | -11.83606 | -49.20413 | 2026-01-17 03:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8599aca5-81a7-3aad-bfdc-2c410ae5cba3 | -14.77322 | -45.93756 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b01e9a51-67cb-3b11-bec8-dd60f88e0987 | -11.81509 | -45.34693 | 2026-01-17 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af77ef37-9c74-3460-81a3-713001aafa74 | -17.27693 | -42.65221 | 2026-01-17 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f0a68b71-96d7-3574-841a-17c12e4ca04e | -14.76641 | -45.92847 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d991ff57-0993-3095-9e2c-caad1d50eca3 | -14.75212 | -45.9141 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 800f2fb9-d8ee-3584-9a33-8ccc267ea61c | -12.08821 | -43.76797 | 2026-01-17 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07e820af-b951-3181-ac08-daa0e8751a7b | -15.25816 | -42.9824 | 2026-01-17 03:57:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 703e999a-c80c-348e-a16c-19b24729740e | -18.68496 | -41.87104 | 2026-01-17 03:57:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 173b4ff5-02b3-38a8-97f6-237f224c6728 | -11.32362 | -44.49793 | 2026-01-17 03:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea0595db-ed34-39c2-a259-387b126e5bba | -14.74872 | -45.90956 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7bc9d0c-702d-3cf7-966f-d4169d26eb50 | -14.75143 | -45.91785 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ced301c2-b372-35b5-8bce-5191e719673f | -11.79927 | -45.36363 | 2026-01-17 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f834705-2bb3-377b-bfb9-8419e67fae3d | -14.76982 | -45.93302 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 589a6387-1272-30e5-a030-0a4c368293ad | -14.70696 | -48.90207 | 2026-01-17 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0aed2b4-b4fc-37a5-ac1f-e2c21e3d1379 | -12.22615 | -49.62883 | 2026-01-17 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26dc4fa6-38e4-3175-a774-27bde9a8efe4 | -12.19649 | -43.95184 | 2026-01-17 03:57:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efbadf2f-5ddc-3cbd-b6ed-756edc720a6b | -10.61021 | -44.65019 | 2026-01-17 03:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 12f63fb3-20da-396a-b451-59f2b16b8a7d | -14.7671 | -45.92468 | 2026-01-17 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 444159f1-0721-3110-8783-86ce57a40c60 | -12.35468 | -52.47942 | 2026-01-17 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92d96cf2-2984-30f1-b766-8c3bfba3bc6b | -11.8374 | -49.19725 | 2026-01-17 03:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b64ea020-4847-3d23-9a05-3f21d1b1bb38 | -13.62175 | -46.79219 | 2026-01-17 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4ba9313-4426-34e2-a2c9-1049174af34b | -11.84271 | -49.19845 | 2026-01-17 03:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0f9b5fc-5280-3a3c-889b-9671c1944f01 | -10.77977 | -44.42188 | 2026-01-17 03:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa0a5d84-c9bb-3e9f-8990-f338848c1cf0 | -14.77663 | -45.9421 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7c596dc-68c7-3244-9a0e-2213528915e3 | -12.91603 | -49.48687 | 2026-01-17 03:57:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 514121d0-d443-32f9-9489-3c70877ee960 | -12.09841 | -43.95708 | 2026-01-17 03:57:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c98452af-09ca-315d-9c0d-9fb7a1bf364b | -11.28701 | -48.73404 | 2026-01-17 03:57:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ffa1675-c6cd-30bd-9ec2-4560aed2e6b6 | -17.61168 | -46.66191 | 2026-01-17 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe355e2d-9774-32a5-82b9-6af132e9bee4 | -12.92138 | -49.48786 | 2026-01-17 03:57:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 352a3b94-a65d-37d8-922f-32c1a9684b44 | -11.05008 | -45.41041 | 2026-01-17 03:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4eff521e-d6f4-3af2-a104-5ebdef109903 | -12.34821 | -52.47807 | 2026-01-17 03:57:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4b227d7-49f3-3750-90e2-df0dd7041a62 | -14.78004 | -45.94666 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e74d9e33-0cbd-3896-80a5-ef64cffbbc11 | -17.27755 | -42.6485 | 2026-01-17 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0745a761-16e7-3473-a5f8-d5c269cdbea8 | -11.83013 | -46.59599 | 2026-01-17 03:57:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 864467c5-f752-3c31-b107-9fc8cba28f8c | -15.8943 | -43.45188 | 2026-01-17 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8b24d67b-7193-3f09-8248-7f8c939cbf7e | -20.72937 | -55.15898 | 2026-01-17 03:59:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d048a18e-c362-3c9a-9f18-3bb649d8197b | -21.62175 | -56.98492 | 2026-01-17 03:59:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| feba0fb0-2664-3fc1-b84c-8d2fad193443 | -20.72792 | -55.16502 | 2026-01-17 03:59:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5009f137-b33c-3f3d-b69a-7ed49ccddaa1 | -21.62868 | -56.98689 | 2026-01-17 03:59:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbbe9403-bb7f-32c5-95d5-1cf3f7b89f2d | -20.57439 | -42.92996 | 2026-01-17 03:59:00 | NOAA-21 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6176c66c-404d-3949-b012-2d066b8c354b | -25.72329 | -51.59639 | 2026-01-17 04:01:00 | NOAA-21 | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d50e9053-f8d3-3436-9cac-df07526bea41 | -13.6993 | -55.6773 | 2026-01-17 04:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6888e2ca-6a4a-322c-b2ce-bea38a2c51c4 | -2.92823 | -48.23869 | 2026-01-17 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e5a002c-f70d-3418-8deb-8464a00fb737 | -2.78724 | -42.34348 | 2026-01-17 04:23:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61ef1ebe-de1c-30ab-be80-13d332bec2e7 | -3.33665 | -49.02036 | 2026-01-17 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1bc08e1-e776-372d-a947-a7b8e1eb08ab | -1.94328 | -53.4656 | 2026-01-17 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 118a6c5f-861c-3aaa-83fb-50382c6a040e | -1.67233 | -45.7894 | 2026-01-17 04:23:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64479a93-0ac0-30e7-b27d-65072ca1cf17 | -2.92515 | -48.23334 | 2026-01-17 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b84e8dfd-27e9-3088-b697-37785b891e27 | -2.9009 | -40.43755 | 2026-01-17 04:23:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d85d9e84-6cad-3482-afc7-dba9cd1810cc | -3.41944 | -43.16681 | 2026-01-17 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a017fe28-39f3-3e8c-baeb-047050298ecf | -1.89191 | -45.55344 | 2026-01-17 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40fe4be8-ddf3-3bf4-abea-8712e8d93766 | -2.93362 | -48.2298 | 2026-01-17 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca95dff4-37ec-3233-bbe6-fecd2e40ea28 | -1.93773 | -53.46465 | 2026-01-17 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0b76111-9ef3-39e9-b019-9fb06427e4f5 | -3.42279 | -43.16733 | 2026-01-17 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ae5b2ce-4700-3503-b201-6624109badce | -1.94222 | -53.46533 | 2026-01-17 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 205c5107-82ae-3ae8-9028-c4fa0c78f119 | -0.97253 | -46.79528 | 2026-01-17 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae03e24c-5e28-393b-844f-bf8dd3da39ad | -3.41999 | -43.16329 | 2026-01-17 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 352ec15a-2442-3df1-8f38-b2e11ce9a6d8 | -3.47827 | -39.14766 | 2026-01-17 04:23:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b4bece66-e3cf-39f0-ae31-816857c9fa48 | -2.88092 | -40.09791 | 2026-01-17 04:23:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1e2e17ff-98a4-3ba2-95d9-170b1e9b5930 | -3.42334 | -43.16381 | 2026-01-17 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89864f04-0bb1-3de6-b338-e31d48d0f26d | -2.92438 | -48.23808 | 2026-01-17 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f76db740-2ffd-3398-b993-c21262a28389 | -2.929 | -48.23394 | 2026-01-17 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31d31357-f718-32d2-ae46-62b3accbff4a | -3.21891 | -48.79409 | 2026-01-17 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ab802c-6194-3ffd-a391-67d3cf69706b | -1.90862 | -45.2066 | 2026-01-17 04:23:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 333e1ec5-e65c-3326-9919-ee27a28dc0a6 | -2.79065 | -42.34401 | 2026-01-17 04:23:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81139245-2ae6-3ff4-89d9-1d3319a290cc | -0.97549 | -46.80004 | 2026-01-17 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5512de7-3cae-3818-80e8-4366abe8314b | -3.49374 | -47.16596 | 2026-01-17 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51e20b6a-57bc-3a6b-9862-af4b5a76a66f | -1.36686 | -46.63801 | 2026-01-17 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 357b628d-6d88-37f0-963e-efc21646595c | -3.49414 | -47.16872 | 2026-01-17 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c750b424-cd58-3992-b560-4dfd648152f8 | -1.67333 | -46.70322 | 2026-01-17 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b72024e-e014-31ad-8af8-22c8e3d741ff | -2.92977 | -48.22919 | 2026-01-17 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e05bea2c-e867-3854-ab92-b2c40d3f0c59 | -2.93054 | -48.22446 | 2026-01-17 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8c743ec-71a0-3ad5-aee7-beb7a2734cfb | -0.97185 | -46.79947 | 2026-01-17 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3eab611-9c67-300a-adb5-730f8748d836 | -11.16105 | -43.57463 | 2026-01-17 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9731e4f-39cc-30ee-be3e-944fb582eeae | -10.34455 | -44.82794 | 2026-01-17 04:25:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b06700d4-0736-32c0-9585-91c1878300af | -9.65549 | -46.23337 | 2026-01-17 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cbdc82b-8898-37b7-9997-49474c46f3b3 | -8.98244 | -48.0781 | 2026-01-17 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74160417-155b-3c07-bf74-e368f76f3d5a | -5.3767 | -43.1913 | 2026-01-17 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d48650e2-47b8-3832-87cd-a5beeab14e26 | -6.04688 | -44.1115 | 2026-01-17 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d18b6cf0-b256-30f3-803c-00864b2f5a4a | -9.76689 | -48.2724 | 2026-01-17 04:25:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bef5e93-4c66-38fc-8d6f-9e780fe22361 | -6.37803 | -43.81699 | 2026-01-17 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6114bf46-623a-3e28-a677-6fc034d1ffce | -10.56287 | -44.32236 | 2026-01-17 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01d33fed-9fbe-384a-a20f-bfbb46b0c520 | -8.10221 | -45.68327 | 2026-01-17 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 123db85e-97fb-304f-a3fe-d9e2f0ac3847 | -10.19815 | -44.89626 | 2026-01-17 04:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b706d0dd-34d8-3c84-998d-84a3c0288cbc | -10.3393 | -36.71186 | 2026-01-17 04:25:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a0b08b5-9222-32e9-928c-80188edcf6d1 | -6.96054 | -46.22197 | 2026-01-17 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1810185-044f-3bc5-b27a-09c7a57eb051 | -10.33888 | -36.71498 | 2026-01-17 04:25:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cca1832d-c605-3150-af43-d192281b1fe4 | -5.30859 | -45.16987 | 2026-01-17 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a390fed-dfaa-354d-a1d2-1424773b4e2f | -9.85402 | -44.71476 | 2026-01-17 04:25:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ec6b278-7e1a-35a5-8f6b-e96ff3e3a8a2 | -10.56004 | -44.31817 | 2026-01-17 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 90ba1712-97c1-3550-a7bc-0f5cdc815972 | -3.43079 | -49.23005 | 2026-01-17 04:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
