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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 611a7bd6-c081-3e6f-a9ec-78dc19534ea6 | -16.33034 | -41.95067 | 2026-10-05 17:13:00 | NPP-375 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bb91410c-33d1-33a4-b5d8-35fd189d07f2 | -11.21772 | -47.1379 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3441402e-caa9-35fb-9b90-8cae92aeef0a | -11.45448 | -43.39251 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b7de62ad-5b5a-3ab4-ba79-91f183f3b825 | -15.58649 | -41.41045 | 2026-10-05 17:13:00 | NPP-375 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 63d0710b-2ac2-3501-9952-e33c4fab47a9 | -14.70712 | -58.66764 | 2026-10-05 17:13:00 | NPP-375 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3676757a-7ff6-34f6-b997-16b3bf184ba9 | -12.07261 | -41.39803 | 2026-10-05 17:13:00 | NPP-375 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9b5922e9-12fb-32d0-a356-f5c1be854a3c | -12.80554 | -43.3196 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d92d0ec-494e-3fa9-b519-6a82a135f28e | -12.05035 | -43.43651 | 2026-10-05 17:13:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e03d9131-ad5d-3537-8eb9-d9aafab96733 | -10.21279 | -46.68139 | 2026-10-05 17:13:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f1a49da3-57c6-3901-9ad0-21e468e7155b | -13.00203 | -44.56893 | 2026-10-05 17:13:00 | NPP-375 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 19d54d02-aa78-3f03-a97f-6ce6c8984041 | -11.63083 | -43.61462 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 63876819-94c4-3562-8b75-7c27e39e5b78 | -10.48339 | -47.24568 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5f3f8bdc-2058-317f-9095-99bb0d6f4373 | -11.34377 | -46.6616 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1a7a4b3d-4ca8-30fa-9717-75cb011e5d6d | -12.16421 | -60.74666 | 2026-10-05 17:13:00 | NPP-375 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b543809f-9720-394b-83df-6d8e268a2506 | -14.31477 | -46.49034 | 2026-10-05 17:13:00 | NPP-375 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8dc7a678-e23c-30bd-885b-b05139b45a55 | -11.80501 | -47.36139 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40283ce8-416a-3852-a40c-c38f6e5b085f | -11.78417 | -43.53858 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8d5a2205-071a-3761-bb39-4c77a86cd05f | -10.96939 | -45.43708 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e07ce935-c359-313c-9b7e-fe1468245eb0 | -13.05296 | -48.73391 | 2026-10-05 17:13:00 | NPP-375 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0dfdbff1-24ab-3436-b125-55ec5e7d6b7b | -13.90148 | -43.86553 | 2026-10-05 17:13:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| afe9b8bb-f125-3ba1-b73e-f5991f79b4a0 | -15.59187 | -40.31677 | 2026-10-05 17:13:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 02b11758-e411-3cc9-86df-b7cb25e181a9 | -10.94109 | -38.68248 | 2026-10-05 17:13:00 | NPP-375 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8280f92e-4012-3c17-ad07-9e907901e728 | -9.8426 | -47.0144 | 2026-10-05 17:13:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 304c4738-f4c7-35db-8ee7-5e6df46a0500 | -15.68906 | -39.78971 | 2026-10-05 17:13:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 77e23df5-d2ac-3e96-8174-b9704014c68a | -12.04642 | -43.44415 | 2026-10-05 17:13:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49f4aa25-88b6-313f-bf88-4d959e15e096 | -11.34734 | -46.65706 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 601b0ae2-4710-346b-8181-76e3075b6610 | -11.63497 | -43.63676 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b1196012-a3de-3e0f-aace-ef6dcea861d8 | -10.36489 | -45.02921 | 2026-10-05 17:13:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 5f9b8c36-8d86-323b-b43c-87652b90c151 | -11.21708 | -47.13416 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 74aa6a2e-bb55-3d9d-8aee-ee332937019a | -11.15564 | -43.49583 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 9305c733-df8d-3db6-8ff9-3075e199ba86 | -10.48687 | -47.24109 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 972e9d9e-47be-3d05-a14a-52e2810df24c | -16.30853 | -41.46208 | 2026-10-05 17:13:00 | NPP-375 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ce76b149-57dd-3859-8ba4-b1e8a602020f | -13.84749 | -42.37349 | 2026-10-05 17:13:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1ec15f8c-d6f0-39c2-b13c-da05c891e823 | -11.35496 | -46.67599 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| e666853c-9326-3b80-9408-49a5d1da3996 | -13.75552 | -42.31399 | 2026-10-05 17:13:00 | NPP-375 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 7a0c2daa-bba2-3fb3-b9d2-c8f74a26d252 | -13.92902 | -40.21597 | 2026-10-05 17:13:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 14f93f20-e530-353f-b4c1-285b13b63ac6 | -11.82658 | -47.3638 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b06d9deb-bdeb-3edc-8fff-b6611cae9afe | -12.57019 | -47.34829 | 2026-10-05 17:13:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c0a636e0-84aa-3322-b37e-606e1e11f068 | -11.39936 | -50.84401 | 2026-10-05 17:13:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 14fc77fc-724a-32e0-bec4-cd8955613d41 | -11.43799 | -47.68913 | 2026-10-05 17:13:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bb3391ac-b76f-3c94-bf59-7544ea7e79af | -10.48404 | -47.2495 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1ecfbc6-ef32-38ba-b358-c2b158f229b7 | -12.01365 | -62.52817 | 2026-10-05 17:13:00 | NPP-375 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fe204a1f-e400-3135-852c-3a8132929a89 | -11.96055 | -46.40204 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 50ff06a0-767a-3f73-96c7-2e1dd970fea1 | -9.81835 | -44.79305 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2740fec9-bf68-3cb8-9036-efe8b6ae946b | -11.22668 | -41.62658 | 2026-10-05 17:13:00 | NPP-375 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5a5ff5c1-56f4-3707-a395-90a8cbffd7b4 | -13.50225 | -40.84584 | 2026-10-05 17:13:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| cd318193-270c-3a55-91b5-830ba51da7f0 | -12.44301 | -42.33759 | 2026-10-05 17:13:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 99faefbf-5af0-356a-ab47-ada8df8b1118 | -12.8665 | -39.92887 | 2026-10-05 17:13:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8132f93c-cab8-33d7-b574-9cb08506e2e4 | -9.97086 | -45.60056 | 2026-10-05 17:13:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9c836790-cd52-39ac-ab57-dc91e0a92423 | -11.74741 | -43.4298 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80d8a490-8a1d-3a33-a5f0-c23b9e68b331 | -11.37266 | -47.62975 | 2026-10-05 17:13:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f10d81c4-5ec1-3bf9-b0b5-6ff5f92748d3 | -14.83213 | -41.72588 | 2026-10-05 17:13:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| ded1b3eb-b41f-3ada-b517-bbb785534a48 | -9.78491 | -45.90729 | 2026-10-05 17:13:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1ca4141a-48d5-3146-969a-f97fb108a3da | -11.82997 | -43.5546 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eab79ab5-f81e-33a0-834b-65023ab3ebc2 | -15.58716 | -42.86267 | 2026-10-05 17:13:00 | NPP-375 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 034b1653-901d-3d66-a85b-3ae0c94e29b6 | -9.78165 | -47.7973 | 2026-10-05 17:13:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 1aa6d999-bf4d-3f6a-995c-37df4f39fe9a | -12.11522 | -60.67217 | 2026-10-05 17:13:00 | NPP-375 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2308ef05-a2b9-3159-a3e8-8fcbab3ac4f6 | -11.80991 | -47.363 | 2026-10-05 17:13:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b0ea237-8a3d-3ad0-9534-d94286efefe9 | -15.97656 | -42.90458 | 2026-10-05 17:13:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0e8196cc-26e3-3fa3-9f2b-38175ed0daca | -13.50655 | -61.13606 | 2026-10-05 17:13:00 | NPP-375 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6ac565e1-93b5-3c81-ae7f-b166f9150501 | -12.08519 | -43.41735 | 2026-10-05 17:13:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b232fb66-3852-360b-afca-76f4ebf05056 | -11.34937 | -46.66882 | 2026-10-05 17:13:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 938f51a3-207e-34b6-b661-f64ab3039256 | -11.7789 | -43.54232 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 491a2a07-867d-3fe1-9594-f69b3c899747 | -11.26711 | -45.23874 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1837b45d-9a8f-3c40-aa59-275299b70129 | -12.03995 | -41.13825 | 2026-10-05 17:13:00 | NPP-375 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| f462e070-3ea5-3086-8a9a-059804305e1d | -10.49221 | -46.0493 | 2026-10-05 17:13:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 713b6373-e27c-36df-a6a3-108d5b4a08a9 | -9.9662 | -45.60136 | 2026-10-05 17:13:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8618987e-ac5e-3936-b88b-c909108d096b | -15.69407 | -39.78341 | 2026-10-05 17:13:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| c24a1b65-28fa-396c-be45-64f34871ebbc | -11.71435 | -43.42598 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 475cfc83-f71e-3a1e-82db-d2dc368ea009 | -9.84352 | -44.78656 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 6bd69b09-9a69-3e8c-be6e-e7282388c568 | -11.33819 | -51.29638 | 2026-10-05 17:13:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f1c04ef0-41ef-30b7-818a-bb1ee59a056b | -12.63059 | -40.70543 | 2026-10-05 17:13:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| dfdb7d80-82ca-3af3-80c0-05f9f4e0527a | -13.92791 | -40.21648 | 2026-10-05 17:13:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 0e38abf8-abde-3bba-aef6-78dbb0138f14 | -14.08763 | -40.49255 | 2026-10-05 17:13:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1f56c4de-a952-3e00-b049-1ac7f3aa49fa | -13.9351 | -40.2145 | 2026-10-05 17:13:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 39.3 |
| cd61dcb8-2434-396d-9472-0b43f24c3fce | -11.68279 | -43.65513 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ba8a4aec-9375-3fbe-90b4-6d58c531b752 | -10.33784 | -43.7335 | 2026-10-05 17:13:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fb8c426d-b3e4-3b8b-b3c1-40e85e2198f0 | -12.90457 | -40.07799 | 2026-10-05 17:13:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5bd223ee-9955-3cfe-b29c-9c31f68bbded | -15.71013 | -41.34764 | 2026-10-05 17:13:00 | NPP-375 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 00687254-44ed-3a05-9fa2-0f27eef146e6 | -11.632 | -43.62086 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 04e0528e-d388-3984-839a-68c7e0d39d50 | -12.81398 | -43.30238 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 54732212-fe7f-3cee-b7da-94bb2a6d86aa | -11.72352 | -43.50364 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| ae07494b-1b18-3cf3-9a9c-f60d03787b0c | -12.76485 | -62.05425 | 2026-10-05 17:13:00 | NPP-375 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4d111b3-89f2-34b2-9122-6c8b62e2246d | -9.87446 | -44.8446 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 45bcd0d1-51a7-35f1-bd0d-75ff3f7c465c | -12.63006 | -40.57857 | 2026-10-05 17:13:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 01475538-1650-3340-8176-96debdf04e56 | -11.62981 | -43.63762 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| abaa3a55-44ac-32cc-907d-5b1660968c10 | -9.7966 | -47.78758 | 2026-10-05 17:13:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f9628b20-e2e9-3712-aea3-8c6df96b3c5e | -12.8158 | -43.31177 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| af51f552-f840-325f-a440-650d1c2591ef | -12.81127 | -43.3159 | 2026-10-05 17:13:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 61a947d8-463c-32bb-936e-cfa59d98a2ee | -10.48274 | -47.24183 | 2026-10-05 17:13:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 19274c1c-bcf7-3959-8bd0-a79e18924df6 | -9.85961 | -44.79677 | 2026-10-05 17:13:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b4c7ce3f-a614-37c0-918a-3d01e1f4a2d9 | -12.33364 | -47.28264 | 2026-10-05 17:13:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4638a2b9-a4c4-39e7-88dd-515709367c69 | -11.26621 | -45.23377 | 2026-10-05 17:13:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c766698e-cab9-327a-9926-808ed1efd14f | -15.97676 | -42.90136 | 2026-10-05 17:13:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3b9b3c1b-2161-34d5-838f-7d301715cc61 | -12.92297 | -40.02077 | 2026-10-05 17:13:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 461bb4b5-3e6f-35f2-ba10-db9bbc37b9d6 | -10.45324 | -39.50578 | 2026-10-05 17:13:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 532d06fe-59c8-315e-99b8-6a4cf250ca2b | -11.75247 | -43.54399 | 2026-10-05 17:13:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4d54cd8b-eab1-302d-a024-46af813b9d66 | -14.5883 | -42.15733 | 2026-10-05 17:13:00 | NPP-375 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 02045dba-cc46-39a4-b3c0-874bb00ab281 | -10.24638 | -49.65196 | 2026-10-05 17:13:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9cf9b28-5621-3a4f-aa6a-d4938fcb4239 | -14.28111 | -41.49556 | 2026-10-05 17:13:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |


[Clique aqui para ver as próximas entradas](README107.md)
