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

## Dados Diários - Página 251

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9144445-cabd-3e0c-beae-4c0e5850f05e | -8.4022 | -36.684 | 2026-10-09 15:22:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0de27d0b-4caf-35d9-8247-82f06113353c | -7.71956 | -37.65633 | 2026-10-09 15:22:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 54ee9a7b-2cfe-364b-9a46-3f9a04e4482d | -7.81881 | -38.8511 | 2026-10-09 15:22:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 54839703-97c7-34b8-9f1f-90b421f805cc | -13.24423 | -39.76382 | 2026-10-09 15:22:00 | NOAA-21 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 35.9 |
| 53c22a7f-494b-3603-89d9-a7c5d0f6b410 | -14.04771 | -40.45461 | 2026-10-09 15:22:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 16.8 |
| e626c872-1bf6-3032-85c0-afdcde781ec9 | -13.24187 | -39.76651 | 2026-10-09 15:22:00 | NOAA-21 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 40a5ce7d-78c1-399d-ae6e-e4bbb4e8a260 | -11.79596 | -40.92654 | 2026-10-09 15:22:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6a38979f-3710-3444-a43a-2a86966dd749 | -13.00131 | -39.73605 | 2026-10-09 15:22:00 | NOAA-21 | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| bb9c996e-a0e7-3de1-9c24-39d03b635a09 | -9.00233 | -41.16145 | 2026-10-09 15:22:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| cf82e9ee-72f6-3807-8b8f-b9ed096ed1ec | -7.83218 | -39.08689 | 2026-10-09 15:22:00 | NOAA-21 | PENAFORTE | CEARÁ | Brasil | 2310605 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 59470cee-d16a-3cf8-866f-492e7088f36e | -14.35905 | -40.29 | 2026-10-09 15:22:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 5ee1a2fc-76f8-3f90-97a8-74adc6c17e01 | -13.58343 | -40.01781 | 2026-10-09 15:22:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 2bdb9958-5960-3579-8c2d-8201aa668574 | -14.1263 | -40.68248 | 2026-10-09 15:22:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2faf814b-ff8a-3a9f-aa92-c4e81bc2b768 | -12.36649 | -38.88771 | 2026-10-09 15:22:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 98c48a32-22be-31e7-90e9-25f5660412e8 | -11.27991 | -41.13146 | 2026-10-09 15:22:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 5f1128ac-5035-3900-b7b8-b2b8d730a66f | -10.63615 | -40.03397 | 2026-10-09 15:22:00 | NOAA-21 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 34.1 |
| a22e5824-1b26-3103-a906-9d8295f76842 | -12.35003 | -39.55408 | 2026-10-09 15:22:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 92ce9c7a-3404-3c26-9a92-f369fb9848b2 | -9.25748 | -40.2647 | 2026-10-09 15:22:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dbda621f-52f1-31c7-ba97-51027fd1c065 | -14.47216 | -40.71411 | 2026-10-09 15:22:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| abbc24ae-41c7-371b-a690-24666135d3bb | -13.28588 | -40.32907 | 2026-10-09 15:22:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1c34a00b-a4bc-33eb-bef8-a70440fe3a03 | -8.24644 | -35.73768 | 2026-10-09 15:22:00 | NOAA-21 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| bd5075fb-cb4b-38fd-b406-f62a01bd85ec | -7.2573 | -35.32426 | 2026-10-09 15:22:00 | NOAA-21 | SÃO JOSÉ DOS RAMOS | PARAÍBA | Brasil | 2514453 | 25 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| f48a584b-bcad-3eaf-823a-a36b6674e5c5 | -13.56215 | -40.89132 | 2026-10-09 15:22:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 115.7 |
| c1e68b09-ed6d-3656-9dce-8deffc1ca022 | -14.04683 | -40.45478 | 2026-10-09 15:22:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 1c559b19-317a-39e3-b7e9-34ec9b23652a | -11.65048 | -38.89714 | 2026-10-09 15:22:00 | NOAA-21 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| cbbea411-5e42-319e-b223-7bc52775821a | -13.58762 | -40.01537 | 2026-10-09 15:22:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 17c94715-135f-3b33-8186-1743b2bda75a | -13.24127 | -39.76078 | 2026-10-09 15:22:00 | NOAA-21 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| c324f00d-6ee4-3a7f-b034-ddf8cfba60eb | -14.78196 | -40.74237 | 2026-10-09 15:22:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 3ecd530e-56b4-3613-a558-aa0db3248ca9 | -10.8683 | -39.43247 | 2026-10-09 15:22:00 | NOAA-21 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 0653135d-d540-3d56-858c-25ef02f71414 | -9.00287 | -41.16182 | 2026-10-09 15:22:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 57603222-70cb-397f-8b4e-6dc4c1589cd4 | -7.06306 | -34.88358 | 2026-10-09 15:22:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 2ff6aaf0-d95e-34e0-90b8-26397b38d24e | -7.54318 | -42.10547 | 2026-10-09 15:24:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 94b6b20a-0a8f-3a9c-98d7-731559a74c95 | -6.00329 | -40.94293 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 4b6b4174-ae70-3f3f-b882-df22f5269dd9 | -7.18935 | -42.00368 | 2026-10-09 15:24:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 0b0f1a1a-f0b1-35b2-b169-86deec0d6db9 | -5.99749 | -40.94914 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| fa43f6c7-4994-31fa-aea7-6f827a514f51 | -5.95945 | -40.91795 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| acd0811a-9c18-3ab6-aa23-a6b5782dd37b | -4.31237 | -41.23432 | 2026-10-09 15:24:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| e95f2b5a-ca37-3d15-8b05-c322743f51ae | -7.06969 | -40.95547 | 2026-10-09 15:24:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1bf90073-9b53-36b5-85e1-3ffa67749857 | -3.54146 | -40.37165 | 2026-10-09 15:24:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b6eed168-376f-34f3-b3b7-05e02be3c2b1 | -5.98926 | -41.38116 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| b516d650-90c1-3b8a-938c-5dd0d3232794 | -7.12399 | -41.81295 | 2026-10-09 15:24:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| f1247664-5378-30c2-adeb-680f1e739f52 | -5.70705 | -41.74561 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 75273431-dbb8-3be7-bb9c-71279aa42e80 | -6.00488 | -40.95429 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 29fa3013-25e2-39a7-b3fd-7bf03a77e1d3 | -5.98252 | -41.38188 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 124a39bd-ac98-3786-9b03-6b16339f509b | -6.05 | -35.2453 | 2026-10-09 15:24:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 150e16e0-76a5-3a47-83ad-c9f879f5c0a2 | -6.00299 | -40.94545 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 151.3 |
| bd7f0057-48f2-3c61-b846-673348dc1ece | -4.30592 | -38.10909 | 2026-10-09 15:24:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 400f287f-5bd1-3de7-81c8-33a1acdbecb3 | -5.95446 | -40.92678 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ff3f038e-5c3e-35af-85f7-6b09d2d865e2 | -5.94942 | -40.93859 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 215b914f-158b-3d48-aa7d-2e79f2a856eb | -3.45932 | -42.61683 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bfe869a8-4755-3b5c-b233-be61eca332bf | -7.54226 | -42.09848 | 2026-10-09 15:24:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 4facf8ef-5b11-302f-a7be-6d3cba0ec091 | -5.4929 | -40.54741 | 2026-10-09 15:24:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 3cb96c67-b147-3bd3-a7e8-5d5ff3df3811 | -6.80301 | -41.23936 | 2026-10-09 15:24:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 89233a6d-6e74-3872-9fde-b21fbcc80f4c | -4.03177 | -40.64868 | 2026-10-09 15:24:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 64ce2dad-984c-3b3f-9da0-8a71a26eaea4 | -4.238 | -40.55574 | 2026-10-09 15:24:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 87944ae4-ea52-3e57-ba49-9dd6ef540e83 | -5.41699 | -39.10718 | 2026-10-09 15:24:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 38a0ad47-8a15-3932-b549-906c24f801d6 | -6.80072 | -39.33775 | 2026-10-09 15:24:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ef3b6bba-a737-320c-82a9-a4de2288c79a | -5.18693 | -36.44737 | 2026-10-09 15:24:00 | NOAA-21 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 91009cad-51d5-36ea-a837-5df0485e258f | -5.3637 | -35.41964 | 2026-10-09 15:24:00 | NOAA-21 | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 77bd5d74-6890-3a76-9efe-62738904658f | -6.01415 | -40.97924 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 51e03f73-bed6-38ac-8b00-6f8c1e5a1f76 | -6.90137 | -38.55352 | 2026-10-09 15:24:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 917dbf7b-181d-3b5a-9377-bb2b3c237baa | -5.99567 | -40.98391 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| bc9706eb-1450-3e95-b4d5-43a985c53258 | -5.08196 | -36.93697 | 2026-10-09 15:24:00 | NOAA-21 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 766bca24-b8dc-316e-a2f9-e3abc1c0f494 | -7.05813 | -40.95251 | 2026-10-09 15:24:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3c30c7ad-b8f2-31cb-944e-6a92db0176b9 | -5.76094 | -42.09396 | 2026-10-09 15:24:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 58a76d14-dfa5-3fb0-938b-b471c7c16d42 | -5.95957 | -40.91559 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 85d9e1e9-cf2d-3871-ab55-69358f42c24b | -5.95879 | -40.91291 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 846c811a-6c31-374f-8b23-033d8d84528e | -7.19027 | -42.01103 | 2026-10-09 15:24:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 6a017483-85d9-30ec-bab9-30b33702e8f1 | -5.16937 | -37.32459 | 2026-10-09 15:24:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2638dac9-6802-31e5-b4e5-1ed3df1c06a8 | -6.00092 | -40.98013 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 9f2dc048-051d-33a7-bc8e-394cd2ae1ab0 | -6.00806 | -40.97699 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| df55e616-e497-3d57-b234-d6600b762812 | -7.13195 | -41.81943 | 2026-10-09 15:24:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 06e21da3-f91b-39dd-8ba9-bac96021faaf | -5.7549 | -41.63847 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f2982446-2f2d-3ca3-b5cd-300ee62ad1e3 | -6.37155 | -38.26132 | 2026-10-09 15:24:00 | NOAA-21 | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 61d023c5-90ac-3ae4-b3e0-24f5f254df2a | -3.90937 | -42.1143 | 2026-10-09 15:24:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 2574bbb2-40e0-3059-b266-d8793f377ea7 | -7.06242 | -40.95141 | 2026-10-09 15:24:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| ccbe9f02-2746-3ace-8163-eb111b46899a | -5.06666 | -36.97175 | 2026-10-09 15:24:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5dbe1f3d-7d04-342f-809d-cf43a8c1519c | -5.75687 | -41.63767 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| d066a7ff-6811-394f-9cfe-7cbd1bc28bec | -5.95593 | -40.93749 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 51502738-30fe-3a24-952b-bf5ad3766520 | -6.89683 | -41.47961 | 2026-10-09 15:24:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| eba9e56e-48cd-3b7e-af34-7ff0e9e62b6f | -4.53143 | -40.71919 | 2026-10-09 15:24:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 72b7c5e0-d513-3add-9352-9096c5317320 | -6.86272 | -41.75133 | 2026-10-09 15:24:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 0cb4fbdb-86cd-34a4-a65c-5df482509699 | -5.95518 | -40.93204 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 4cd0e7c4-f770-3159-b9bb-041c887ab0ac | -3.50379 | -42.57884 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f5c85fb3-254d-3425-9965-583b02a8aa9f | -6.00726 | -40.97128 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 52556ed9-c8e8-38e5-ae52-a434d3964b7d | -4.58172 | -40.6656 | 2026-10-09 15:24:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| cce159dc-1269-303a-b2df-fd02ce06a8dd | -6.01263 | -40.96782 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| ed13b52b-9724-3b33-934a-cde64939c1f9 | -7.12897 | -41.8064 | 2026-10-09 15:24:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| c5d913b1-e95e-3ce1-b721-59ebe64627f8 | -6.48656 | -41.83373 | 2026-10-09 15:24:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 0934f87c-d434-3164-a786-2e20b05428ab | -7.07128 | -40.94996 | 2026-10-09 15:24:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8595363b-d359-34dd-8ba3-bbaa438c0555 | -5.96011 | -40.92303 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| dadab61e-c33b-3a2a-ae79-3c735e38b65d | -5.95671 | -40.94316 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| e0dcced1-a18d-348d-8344-bb3fa642d033 | -6.73444 | -38.32359 | 2026-10-09 15:24:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 06207592-cbb6-3a6a-a00d-287208fabf08 | -6.0978 | -35.70229 | 2026-10-09 15:24:00 | NOAA-21 | SERRA CAIADA | RIO GRANDE DO NORTE | Brasil | 2410306 | 24 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 1b84194c-1ee4-3775-ae9f-93f8bd514962 | -6.8013 | -39.34203 | 2026-10-09 15:24:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 15680685-0fb5-3f91-ac80-7971fe93a9c1 | -5.23811 | -40.5886 | 2026-10-09 15:24:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| e45ed0de-9e16-32c2-9661-663e298633fb | -3.21678 | -42.96666 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 14671d72-529a-3039-a1fd-9846e827de96 | -6.4935 | -38.95377 | 2026-10-09 15:24:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2a0d9726-8780-35e4-a6f6-fc520622c853 | -6.41175 | -38.43354 | 2026-10-09 15:24:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 12.4 |
| f8721fbb-15af-3d62-a6a4-9018db9488a9 | -5.15355 | -39.50323 | 2026-10-09 15:24:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |


[Clique aqui para ver as próximas entradas](README252.md)
