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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdb6a712-b32b-3594-98f6-58489602582a | -14.19509 | -45.50896 | 2025-06-18 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2edad3f-940d-3c1b-b290-ac8b0e3ccd45 | -9.20689 | -49.67676 | 2025-06-18 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac66bd64-3260-332d-940d-d497a7c9c39a | -6.93658 | -47.25841 | 2025-06-18 03:49:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d584824-5f24-339a-8cad-23eb88bddefe | -11.55966 | -47.61439 | 2025-06-18 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b57a407f-c9b3-3209-ae3b-1df7214c8857 | -8.10976 | -45.54967 | 2025-06-18 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53582a88-8a95-3ba5-b225-3f33c6062edd | -12.00705 | -43.8505 | 2025-06-18 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84c8e472-7f56-32b1-8809-f5be381ca0e8 | -10.6542 | -49.36188 | 2025-06-18 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ff5c5a7-c7f8-3252-a5f1-edea3d81f222 | -9.26391 | -50.0439 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a83923ee-7f98-3eea-b482-4c74d4ae3bbe | -9.20051 | -49.67556 | 2025-06-18 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1365807e-fd8c-32f3-b1eb-c2f5e5f1fa55 | -14.19785 | -45.51904 | 2025-06-18 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8db01118-24c6-36b5-b3df-1e1849f43eef | -11.66333 | -44.61753 | 2025-06-18 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbe7c899-55a6-31bb-97b1-9a7f0f90fd12 | -11.33563 | -45.21186 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5f1c19b-b5bc-3096-b845-91b5428138c8 | -9.32563 | -47.83027 | 2025-06-18 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a5c2966-1b23-3e85-825e-9bcde50de773 | -12.2372 | -44.19963 | 2025-06-18 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a76e485f-3975-31fe-9ae0-11f2c9f953f9 | -9.96495 | -47.9405 | 2025-06-18 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46ed3cc6-1c33-33ae-95db-9f2a952950f9 | -10.65421 | -49.36213 | 2025-06-18 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9ecf5aa6-196a-36a6-811e-53e7fdf83744 | -9.25881 | -50.03837 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 45557fc3-02b5-3331-b3c5-6c404084e958 | -7.54636 | -45.64556 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4536c739-9687-3db0-9841-8c8a0aad1bcb | -9.8863 | -47.81448 | 2025-06-18 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c5e24d9-e980-364e-bcc5-26e4216864aa | -11.33909 | -45.21499 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08eba2f7-10fd-3834-bcb1-0cdb5f914c56 | -6.93726 | -47.25458 | 2025-06-18 03:49:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9f20478-33e2-3105-8bce-ad011788e53b | -8.72456 | -48.00108 | 2025-06-18 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a70e9aa9-22b4-3628-9f4b-22facc829df0 | -11.79567 | -43.78971 | 2025-06-18 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac7c1af4-679e-300c-8f86-ef3660a56274 | -9.80033 | -49.64067 | 2025-06-18 03:49:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d67a2c7-7766-3c80-b3ee-3bea93b9f39d | -11.33937 | -45.21759 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a693a0f-3dcb-3533-8e56-544f91e55cde | -11.33477 | -45.21664 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 130b8825-e8c7-3e8c-8d41-28f3fedf2b72 | -9.2585 | -50.03709 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e96d2b7-d57a-306d-83dc-125e74e2f237 | -9.82053 | -48.11074 | 2025-06-18 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f97575a-5b4b-3450-8969-51df51d68841 | -8.72805 | -49.02662 | 2025-06-18 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f1b56e5d-4fc5-34f3-9a8c-eabeaaf8c97a | -12.23224 | -44.20288 | 2025-06-18 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 990822d5-47f5-386e-b5e1-73c431195e11 | -11.57731 | -44.84209 | 2025-06-18 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7eb29cb9-1f7f-3873-9ae6-3d4e35b5cbd9 | -7.54021 | -45.65076 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 713a3e5e-6b43-360c-83ae-f3b93436a045 | -10.98499 | -45.11084 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 820c894a-26fc-3fe8-92c8-3c4c5fb90728 | -9.27181 | -50.04091 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c232527-ef4e-3e60-b05b-41cebf75770a | -9.26425 | -50.04524 | 2025-06-18 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46b28295-8f6b-3eef-8592-852fba45968f | -9.81936 | -48.11108 | 2025-06-18 03:49:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 102eff34-f568-3819-a1ed-c318b9ee4a01 | -14.20318 | -45.51527 | 2025-06-18 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41fd0327-6326-3c60-8ef0-6b64b1df87fa | -7.61326 | -45.55634 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70563eca-973c-3bd5-adc5-39ea7633860b | -8.45553 | -46.90369 | 2025-06-18 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2a7c044-a346-3dd4-9232-52dc0f8e5863 | -9.88395 | -47.81365 | 2025-06-18 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2f64ebd-e5a8-38c0-9dd9-5b42791a892d | -7.24307 | -44.7579 | 2025-06-18 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bd0276a-45d6-379e-b75d-2768d9f97f1c | -9.33056 | -47.83535 | 2025-06-18 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5aa83daf-a2dc-3d90-baf8-b1b2941c404b | -11.62365 | -46.77527 | 2025-06-18 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7e3c83b-66a5-30d7-b48c-d4d1ed0a2fbd | -8.72188 | -49.02544 | 2025-06-18 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 67312cb5-4009-372e-850f-02c3484fb432 | -11.57112 | -44.6737 | 2025-06-18 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c186d233-b1a5-38b9-bc3b-4c55d378807e | -8.96336 | -47.97442 | 2025-06-18 03:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4441839-6636-3db2-bed4-96a878cacaff | -14.2004 | -45.50522 | 2025-06-18 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a82febd7-63fb-3712-a352-a795d710259a | -10.98678 | -45.10097 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b40bcd2e-68a0-317b-8280-10d7cd8637da | -8.72534 | -47.99689 | 2025-06-18 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67d5a670-4cc2-3c36-884f-404615575e9e | -2.87378 | -40.0242 | 2025-06-18 03:49:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| db15321f-fa71-313a-b7a9-258023e5b968 | -9.88394 | -44.79598 | 2025-06-18 03:49:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96fec0f1-f729-3435-940c-609a6e2e0f55 | -8.11027 | -45.54678 | 2025-06-18 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7308f6bd-8f02-309d-8e75-dab46c2112ad | -14.20403 | -45.51066 | 2025-06-18 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bd711f3-76a8-31dd-ad58-08f8e5b4959f | -7.60818 | -45.55572 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71c45c1d-ba54-3446-a347-e916323e6b27 | -7.54476 | -45.65466 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e522a28-8c7b-33a6-b62c-f13b1b71f564 | -9.16111 | -49.64005 | 2025-06-18 03:49:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03be00b9-0379-3564-ad21-777028db7a09 | -10.98767 | -45.09605 | 2025-06-18 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ee1c26ab-b53e-356f-88cb-99fd6e9ca325 | -11.55813 | -47.61012 | 2025-06-18 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cd7620d-e67d-3628-a5cf-855f2cd01c50 | -2.87421 | -40.38247 | 2025-06-18 03:49:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7aaecbab-a3ac-38c2-9be1-5bc3237717ea | -8.7228 | -49.02066 | 2025-06-18 03:49:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 9832f402-eb53-3492-9d8b-46ef5615d4a4 | -7.54689 | -45.6425 | 2025-06-18 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 885dbfba-f884-307c-860b-404270169674 | -11.90987 | -44.17854 | 2025-06-18 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4afd3616-072c-3498-b793-16f0dc7f7e5d | -11.1379 | -53.9429 | 2025-06-18 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 200.4 |
| 38c5574f-4491-35ec-84f7-550fa5c583ec | -11.119 | -53.9446 | 2025-06-18 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 6929c088-d941-3091-b91e-b2ee0863116a | -11.1382 | -53.9223 | 2025-06-18 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| a242736f-e20b-355b-adc1-065fbb35d51a | -15.40633 | -47.82997 | 2025-06-18 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f48550eb-bedc-37c0-81c0-3ab92d933ad3 | -14.43845 | -48.90429 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 34297d2a-8a18-3858-88c0-8478ddaec8da | -19.47993 | -49.29123 | 2025-06-18 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4608ae1-3c6a-3d7b-b18c-375fd86b1599 | -22.67863 | -42.85493 | 2025-06-18 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 31182ffd-06b9-3703-ba16-023e42f376df | -19.47478 | -49.29002 | 2025-06-18 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5303aa4-9a49-3bbd-9e66-f346639e6397 | -22.67542 | -42.85543 | 2025-06-18 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0f3ef32f-a30c-3d18-8028-5bc11934f5d1 | -22.67884 | -42.85611 | 2025-06-18 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0949062a-8a7c-3b93-923b-593a9cac95be | -20.99821 | -47.39383 | 2025-06-18 03:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85f620d7-a0d1-3d53-8b3c-fe1712652b87 | -14.43137 | -48.91057 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6ad7ed42-c2b7-33b0-a061-b62b3a682190 | -16.78637 | -49.11732 | 2025-06-18 03:51:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91c1ee92-54c8-3ce4-bf7d-3b87532f9c71 | -18.99815 | -52.08888 | 2025-06-18 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fad06dc2-f2f5-3069-936a-e3b3b3a12684 | -20.80403 | -44.34694 | 2025-06-18 03:51:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ab041380-e090-3ee3-8c1a-7190af7ed566 | -20.7626 | -46.77048 | 2025-06-18 03:51:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e92c69ba-111f-31e3-b96c-beda41e7deba | -18.37851 | -44.50498 | 2025-06-18 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bce89c5c-5fc3-3e4c-b426-7f7023deb65a | -20.50459 | -45.59016 | 2025-06-18 03:51:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3e0b98f-e019-38ed-b9d2-900e8e51c209 | -19.90241 | -49.35241 | 2025-06-18 03:51:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 95aacbee-9657-312f-8c9f-bb2b634a9645 | -19.90442 | -49.35034 | 2025-06-18 03:51:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| aa89d669-d47c-3792-817f-3bdfb88c7317 | -20.50127 | -45.58561 | 2025-06-18 03:51:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6368b355-461e-34ae-9903-a66c814b2f08 | -14.43215 | -48.90679 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2bd10db5-d44a-3f1d-8f19-ada491108a31 | -17.69226 | -46.81202 | 2025-06-18 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2858132c-8bbe-3b95-bfb3-2ec773de290b | -15.62538 | -46.46581 | 2025-06-18 03:51:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c20fef7f-1931-3015-9519-94a60fca8263 | -21.66604 | -41.94967 | 2025-06-18 03:51:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8d5a192c-e3dd-3f13-aa48-7540f0224705 | -18.99717 | -52.08604 | 2025-06-18 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8a8628e-46b0-33a3-9571-98db4d3aabfc | -19.9031 | -49.34909 | 2025-06-18 03:51:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e5425b43-03f8-3047-ac0b-2339fb557fb1 | -20.42147 | -45.58388 | 2025-06-18 03:51:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7030262-5fd0-34f7-b939-c3d3a6d61c28 | -19.90371 | -49.35366 | 2025-06-18 03:51:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 5334678c-994a-37ef-8968-8d0e747d78f7 | -17.69198 | -46.81432 | 2025-06-18 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7caa4456-05f8-3df9-89e8-ccf2ed70e890 | -21.37263 | -48.96074 | 2025-06-18 03:51:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ceccbdbd-045f-34b2-9375-e4b2cd878e27 | -21.02378 | -42.83855 | 2025-06-18 03:51:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4b707b65-ac18-329f-b1c4-8e618dadc476 | -20.29198 | -41.74911 | 2025-06-18 03:51:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f28bdfa0-a626-399f-ba0d-a8289a208cb5 | -19.00334 | -52.08741 | 2025-06-18 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9ea5890a-6ac9-30e0-8958-cb594b0b45f2 | -21.6694 | -41.95031 | 2025-06-18 03:51:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2ea639d3-450a-3aa1-a66c-f8a2f74ccc26 | -21.66668 | -41.94583 | 2025-06-18 03:51:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 204cc014-57d4-3fdd-9c26-2b6ad5d980af | -21.67213 | -45.53755 | 2025-06-18 03:51:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f8ea1834-0dfa-394a-8fe0-ce86a3f78119 | -15.18725 | -44.20435 | 2025-06-18 03:51:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
