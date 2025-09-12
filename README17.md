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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff1508d5-39b0-380f-8b95-1a4db6550fec | -15.67165 | -47.07217 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61a275ef-e71a-3c43-8619-4cf31f72d727 | -11.48973 | -43.63153 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 210411ea-30ad-364b-b3da-cc18c590ed42 | -10.87534 | -45.56389 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0637b429-821d-338b-a38d-41ec91485cbb | -13.25848 | -43.76715 | 2025-09-12 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93aeb77f-e3e6-3168-af80-35e02243003e | -15.67073 | -47.07648 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b4b7557-0598-3145-a5db-d04005a93e56 | -13.90859 | -48.23418 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bc55a961-74c5-3f63-87b0-e66d124a180e | -11.1527 | -45.31134 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c15104fb-fe70-369b-b645-431c729472fc | -10.56333 | -43.66001 | 2025-09-12 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a59e2aac-008a-3fee-b05d-eaf2434469b9 | -14.18807 | -46.20237 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f713a6ac-3397-3e5d-9891-4ee88d378c00 | -9.04002 | -47.09064 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 657a9aca-7237-307b-8be0-9f3e17f80c2a | -14.16718 | -46.18755 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e0f5b16-cc94-3e71-90f6-9b7cb9de4b0b | -14.45457 | -47.30835 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0312dc75-416f-3fd7-bb14-c573f2ca2e65 | -15.68404 | -47.01348 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0b18fcb-3e4b-34a0-8c96-2facd336c364 | -13.31597 | -40.56694 | 2025-09-12 03:38:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 37b5a44e-b315-3a51-a4bf-476b5c68a719 | -12.01942 | -43.78577 | 2025-09-12 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c68f98ea-5b5b-388a-aa5d-c5529355a599 | -11.42902 | -43.54553 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 94face6f-ed05-3761-b1c2-4c78e53f3338 | -9.06604 | -47.03819 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 11cddf93-31b6-3201-a5a9-593981ec3c93 | -11.42393 | -43.54461 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5eb4de0-0c22-3e93-9c1f-de6166d87aa6 | -8.52048 | -47.65359 | 2025-09-12 03:38:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8dd076a2-fd7c-3c4a-8cad-48aeead14744 | -12.00275 | -47.76975 | 2025-09-12 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 21157aeb-e9cd-3ec7-aca4-9c17ac12a7f0 | -10.55758 | -43.66194 | 2025-09-12 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b276fe3e-8d42-331f-96ca-5524f4b23b5b | -13.37348 | -41.91919 | 2025-09-12 03:38:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf50db69-38fa-3c2f-b4ac-b8565314bb58 | -12.11135 | -44.86579 | 2025-09-12 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45aee399-01fe-3c42-a7f7-5f885c4753bd | -12.11062 | -44.86956 | 2025-09-12 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c207cc8-6bbb-3d6c-9d9b-40255462f7f3 | -14.44095 | -48.42808 | 2025-09-12 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42b95fc2-9846-327e-acbd-43d221c59879 | -9.88115 | -46.46492 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5873c108-c7a5-30ac-86db-ac7b01333534 | -11.20086 | -37.23197 | 2025-09-12 03:38:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 31e9648a-2047-391e-965a-3633c6d3d8bb | -15.69314 | -47.02842 | 2025-09-12 03:38:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d7b08669-da1f-38c0-8e21-9288b235c11e | -11.98206 | -46.64814 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 992baacb-fb2e-3445-81fa-de5872a058e3 | -11.70685 | -46.53242 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7162f9c-f3d0-3618-902d-6e3dad8ae1e2 | -14.18001 | -46.21285 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1dfddbbf-ef91-3acf-b035-a002995ff0ea | -11.14927 | -45.23772 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7f2174d-a7e4-38b7-8931-d4fd0baf58b2 | -11.69144 | -46.51409 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d218e933-fb9a-362e-8958-dd679d45d9a6 | -11.46838 | -43.60463 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 483e06ab-13bd-3ffb-ab6b-0e4b4a49c66b | -9.04105 | -47.05093 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c2ba2eaa-1a44-3d67-b1d2-be6ae0adc6de | -11.48582 | -43.6242 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e0d0049-e791-3075-8416-00dace15c401 | -15.08385 | -48.01032 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b2de390-86f2-3c24-b0e2-0ed39801c144 | -13.9085 | -48.26645 | 2025-09-12 03:38:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2083dc67-2cdb-3e2c-89da-66c8ddb9bba1 | -15.0731 | -48.0131 | 2025-09-12 03:38:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88128318-4752-3240-a005-3fc6997cccd6 | -11.39628 | -43.52367 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de52965b-5bf6-34b9-95f8-1866c8933052 | -13.24736 | -43.77106 | 2025-09-12 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e23bb2e3-ba9e-375f-83a3-0b939d505505 | -11.14777 | -45.30616 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 077e2427-8bdc-3825-9ab4-371eabbb85ce | -11.37257 | -43.50999 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 351b9814-9abc-3e35-bdb0-87c95651003a | -14.416 | -47.3101 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e5774cb-e824-39a8-b88b-163b6fc2f9d5 | -9.04898 | -47.04538 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bcd07736-cb5e-37de-a1f1-2069ac8b37ae | -11.69376 | -46.53437 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2e2d4b54-8fe9-3e5b-a7b0-edd65bf339b1 | -9.35232 | -46.59044 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36e4640b-ae68-308c-8d8f-bfaed7152837 | -10.85009 | -48.16416 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81179382-a560-32e8-a23d-effe1163caa4 | -14.17592 | -46.17954 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c84780d-ac11-3f9c-a50e-8f873f967024 | -11.12464 | -45.12323 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ade23a1c-b11d-382d-9b68-d780827babde | -10.13219 | -47.92292 | 2025-09-12 03:38:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d137169f-0585-3aea-95ff-b7ed703bf33d | -10.70418 | -48.62658 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e6f12579-2fc1-3310-8e30-a478f5c4388b | -14.17425 | -46.18203 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a948280-3704-3921-8a7d-8f918db027cb | -10.74551 | -48.18356 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 73037c97-e19a-39aa-a173-76f01e4232c5 | -8.48093 | -47.27384 | 2025-09-12 03:38:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 539bf9b3-5c19-3ad6-9d14-d10211dfc3e6 | -9.11335 | -47.12462 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32da670e-3d98-3065-9655-80e8c8a2d78e | -13.32035 | -44.08907 | 2025-09-12 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6508bc43-fbe0-3d6f-8af8-8d36c0ad0818 | -10.83351 | -42.75851 | 2025-09-12 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a8e080e-3b8d-3b5a-9dd1-784c2237fd68 | -11.97604 | -46.64641 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c0b8230a-2d58-3a4e-9b64-d671b444a31e | -15.11437 | -48.09569 | 2025-09-12 03:38:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9afc145c-cf42-3086-a1c8-77e51e2688cc | -14.16567 | -46.19506 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 34f8033b-0c29-3c6f-99e2-2b4a43ab7d76 | -9.06964 | -47.11428 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f1dc275b-343c-310f-9072-126ed3b63eb5 | -9.01927 | -45.73921 | 2025-09-12 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1681568f-0fb7-318f-8202-24acb25c8b9c | -8.94501 | -46.09395 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80e2d14a-4a27-3679-9eaa-166c37a5c5de | -13.36398 | -41.92331 | 2025-09-12 03:38:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| efdbddff-8c34-3846-b805-e252849493eb | -14.28382 | -45.05176 | 2025-09-12 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 815d1dc3-3e18-39b5-9d35-87f2d9a20876 | -11.65907 | -46.64442 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3f3685bd-5d22-3493-bded-ff062faa7011 | -12.07933 | -47.59786 | 2025-09-12 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1cf0aa40-8676-3982-ae56-76daaaa4f596 | -11.41692 | -43.70797 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c844a52-74ac-3a1c-a4ac-e9c7ebabb89b | -14.17348 | -46.18586 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60267115-a5af-3595-8974-4858701f7a03 | -11.6918 | -46.54421 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fcbde10e-190e-32b6-adb8-28a35fcf8f2a | -11.66613 | -46.64111 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb535540-5ce5-3c99-a725-5b5ac44d93cd | -9.04812 | -47.06062 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9567b996-5831-3cb8-81a2-6b44cbe4f632 | -9.69279 | -47.55267 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4403f88c-fb2e-3f6f-b645-8fd730573023 | -9.03655 | -47.10812 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 34cfcb09-dbb3-3618-b800-07eb9aa11c58 | -9.68229 | -47.55587 | 2025-09-12 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a0acb49b-1615-3e72-bf0d-8207ad97937f | -12.00304 | -47.77436 | 2025-09-12 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be3c5170-69f6-3a59-989e-ff6d3e991bb4 | -11.68581 | -46.67092 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fba8d2cf-c238-3c68-a1d5-14dcce9e4e1c | -11.67508 | -46.59621 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c12c1dc6-55cc-3099-a572-77bf29f32d5f | -11.67622 | -46.62255 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4d9d7e3b-f9cb-370a-91bb-d166a3266ed2 | -9.06448 | -47.03608 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f633aa59-6536-310b-aabd-95d70086ac36 | -12.81116 | -44.75575 | 2025-09-12 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cc289c3-11d1-3679-86bc-d5ef5a8263f4 | -9.10791 | -47.11752 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d8d698a-a928-35a2-8d0c-e92be52093a3 | -10.84773 | -48.17025 | 2025-09-12 03:38:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3898f94-2b89-312b-8bcd-1edcc54570e6 | -11.67666 | -46.67869 | 2025-09-12 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3e64b69-f017-3098-90c8-cdc3c7f26bbf | -11.67129 | -46.64729 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6002573f-5370-3bd6-969d-5d6d23a2fca7 | -11.44362 | -43.56835 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dfc82c8-3468-37ec-88d3-93b9a26d58f6 | -14.13279 | -45.38411 | 2025-09-12 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce21b1af-6cde-3dc6-83f3-4dc6274ee442 | -9.06496 | -47.04387 | 2025-09-12 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c6aafb4d-82e7-3b8e-bc6e-9d000bed3960 | -10.08804 | -47.15953 | 2025-09-12 03:38:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1a3b674-f1f6-3e41-979b-5edd5f07b238 | -11.68411 | -46.58291 | 2025-09-12 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f8828c90-a4c8-3006-9d95-4b80ffefac91 | -10.35747 | -46.38814 | 2025-09-12 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62e3b20e-b9e9-3a22-8726-cab10e0da608 | -10.13786 | -46.311 | 2025-09-12 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c27a3544-ebfd-39f8-88a2-bf864264d8f8 | -12.00415 | -47.76892 | 2025-09-12 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 39d83565-b71b-3b57-8d3b-47a4d367af78 | -9.04203 | -47.1151 | 2025-09-12 03:38:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2c07c3a-254f-3111-ab59-31175f12d44c | -10.65047 | -48.65121 | 2025-09-12 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dac77cce-3b6f-3383-9c71-36c336d113d0 | -15.2188 | -41.80579 | 2025-09-12 03:38:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c37e38e-36d4-3b30-bb0c-8d0af9f8dc27 | -11.43586 | -43.56554 | 2025-09-12 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe7963da-1a82-3dcf-ae13-c1884b238882 | -11.12538 | -45.11948 | 2025-09-12 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2be0095d-ae9d-3e63-b5a0-01a7d59b5659 | -14.17511 | -46.18344 | 2025-09-12 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
