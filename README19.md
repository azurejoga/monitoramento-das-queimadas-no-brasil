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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96b25ba0-d797-3706-9213-dfdfb23de71f | -13.01103 | -45.21701 | 2025-09-07 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd66725c-28d6-31c3-adb5-540e789d14d5 | -13.84655 | -46.25444 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36b082c6-9e6f-3096-9e3f-98f37e9d97f5 | -13.83801 | -46.27168 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03cadc1d-6a80-3575-a108-94c3f316867a | -13.00565 | -45.21577 | 2025-09-07 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7775b44b-ed02-38a1-aae4-86a021b451fa | -10.3357 | -46.4041 | 2025-09-07 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddd8d9b2-f889-3824-af78-2d48cc296284 | -15.67595 | -48.21272 | 2025-09-07 03:32:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e25ad9d-d2af-3b31-8419-6ccce3b3543a | -15.1755 | -47.97356 | 2025-09-07 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 097248e5-557b-39b3-bd38-3c2d6870fa4c | -15.72945 | -47.02778 | 2025-09-07 03:32:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0fe35f10-7155-37a6-b396-02c9ca10bac1 | -13.82993 | -46.2704 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b931f872-ae82-3ecc-8989-961401498645 | -13.67131 | -46.95548 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8db62ca2-d2ad-36f6-8a47-a8a2d9a23b2f | -16.26309 | -47.8499 | 2025-09-07 03:32:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbb8c7e8-a1d3-3e6e-bcc7-f4cdd3fd6f64 | -13.83479 | -46.27889 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aa263ff4-3934-356c-a2cc-b8e9db2c199d | -10.60724 | -44.33734 | 2025-09-07 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 38f6109b-7946-3fae-81d3-1a9dd0fa3959 | -11.31977 | -46.57043 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| e7aac2a6-5cd8-330c-8ec5-e0821175c457 | -13.01171 | -45.21703 | 2025-09-07 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c1f6876-6608-39e1-840c-6ab1efe2f488 | -13.84044 | -46.2519 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16ed755f-70da-3132-851a-5cd78c5734b7 | -13.83099 | -46.26537 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94bce448-17d8-3e14-ac32-322bfeef0ccd | -11.59402 | -47.17752 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 081d1b39-9b60-360d-ace2-da6ceb17531b | -16.08841 | -41.81502 | 2025-09-07 03:32:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3bd1b55a-40f1-3373-b467-e3a48c25ca08 | -16.28665 | -45.68581 | 2025-09-07 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76b9de12-bc21-3fab-95eb-d24e0fdc970d | -14.5606 | -43.72766 | 2025-09-07 03:32:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e29c55fe-67f0-32dd-b6be-791cd69a8cdb | -10.34551 | -46.46484 | 2025-09-07 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ee6954c-1244-38a2-9dc4-7c29d0f7b978 | -13.84902 | -46.25148 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 860b68db-7b9c-3338-aef3-41e2983b285b | -13.83697 | -46.2765 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 256a9b6a-b65b-34a2-adb9-a08752bb9eb6 | -15.94312 | -41.88815 | 2025-09-07 03:32:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54c95f16-4a4c-37ce-864b-f23a49f46745 | -15.36043 | -43.6684 | 2025-09-07 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.6 |
| befc67a1-cc21-30c2-b2d4-f094533b7df9 | -11.59651 | -47.15974 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 0448686f-2fe3-34ac-9b16-fd9bdb585198 | -17.31205 | -39.66788 | 2025-09-07 03:32:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f0504839-9fbb-3b72-8a65-6c3501e3f526 | -15.5288 | -42.62568 | 2025-09-07 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6e8d8056-4598-3151-ab9b-8c54aae002c1 | -13.79175 | -43.1664 | 2025-09-07 03:32:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 975f03fa-cb8e-341e-88fe-c2462a94a409 | -14.85548 | -46.69274 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1e94c12f-766f-30c7-825d-35dc71b30f65 | -13.84192 | -46.27655 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bf029d75-5871-33be-b182-73fd8c2dc09c | -11.59554 | -47.17019 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 83f2a93f-0b34-3ec6-859e-961a0ff832da | -13.82368 | -46.26854 | 2025-09-07 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e51672c2-fa85-3d87-a6d9-c4977649a9d3 | -16.4529 | -41.00862 | 2025-09-07 03:32:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2f59dc19-cdbe-3430-84f1-99d65c3285dd | -13.01073 | -45.22175 | 2025-09-07 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3233080-25c9-356b-a571-59db3f3f8d00 | -15.17386 | -47.98092 | 2025-09-07 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53aa43a2-4251-3af8-b182-08082155ec03 | -11.59836 | -47.15665 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e9b153ee-fe01-3500-a01d-9e42bfc301ba | -11.41027 | -43.64195 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e4a4a9c-4c11-34f2-8d99-ea8b5f0a4e57 | -13.7131 | -46.87709 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c51b98da-7c28-37f6-87a9-60115a491206 | -10.38148 | -44.96637 | 2025-09-07 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2ec34337-c493-3ada-8fbc-241107767b48 | -11.61091 | -47.16597 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| d09e61b1-bae5-3f6f-b9ee-7c9ced4fcf6b | -9.83292 | -46.55537 | 2025-09-07 03:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| bf161bfa-bda5-35ff-9305-0fa27d8fdb89 | -11.40441 | -43.61177 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29bfa2b8-32ba-3d3c-a2d9-33147787955d | -10.73629 | -44.35725 | 2025-09-07 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d598ea8-960e-3d20-a8b2-2feff79258f4 | -13.00663 | -45.21105 | 2025-09-07 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 083a1fe4-38dc-3970-aef7-455d38a336d3 | -14.8486 | -46.68936 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1a4e82d-bad7-39ac-a30d-306115e3d210 | -11.28627 | -41.99713 | 2025-09-07 03:32:00 | NOAA-21 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| efb63bab-940e-3971-a2a6-87966a96927f | -9.83361 | -46.55494 | 2025-09-07 03:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0c183e5c-78e0-3587-89ea-9db2b74394bd | -13.71651 | -46.90553 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65b5ab92-e634-348a-9b5e-cbbe02028ef4 | -11.3876 | -43.54825 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce36bf3c-afec-3bf3-b421-d09ee316b38f | -15.67746 | -48.20601 | 2025-09-07 03:32:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3a6a59b-955d-3e5c-884f-900ad9934c48 | -15.54301 | -42.65775 | 2025-09-07 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9a5ceb64-b4e7-3e98-adb0-29bd34a1319e | -10.43164 | -42.53435 | 2025-09-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e3677b93-b05b-3f64-b366-b8c8413ba3a1 | -12.61932 | -44.61107 | 2025-09-07 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9fa7d2c-48b4-3c1f-8746-02e399e16447 | -11.31484 | -46.5499 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7cdee5e-ff0e-3fab-981f-110a96a21354 | -11.31141 | -46.54322 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f48f07f3-eff5-328b-a130-53769ce24a86 | -11.61249 | -47.15833 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 5e6a61ad-6c94-34f5-b2b7-bb85904c422e | -11.32232 | -46.55822 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 99179d2b-ace8-388f-927f-87a19cf75e4c | -13.01008 | -45.22175 | 2025-09-07 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a68e84d2-3ce7-3d49-8296-33f37e9b4c0e | -15.10857 | -48.07941 | 2025-09-07 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4849bbae-5c16-3bd0-8367-f48e21ab4084 | -11.32154 | -46.55149 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fac545b2-a275-37f1-a936-4f748ae0d5c9 | -13.04569 | -47.12258 | 2025-09-07 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe20a589-a5d6-3167-a454-04c8c7c72b97 | -13.7277 | -46.90517 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abd9bf79-e5ae-3263-be83-896c3ec087eb | -10.60632 | -44.342 | 2025-09-07 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 7fdc9ed3-452c-3e75-b262-b4e04a4b355d | -11.61776 | -47.16209 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cceda9c8-19ea-3e3a-a828-6f42a202c595 | -13.82585 | -43.85958 | 2025-09-07 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc574e36-5627-3ec2-9ca8-cd96675a244e | -11.41103 | -43.63802 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3d82d6ec-19c3-3a76-90fc-cd9a666c2ca8 | -11.40616 | -43.63288 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65624485-33f0-33de-b056-188fe5a72811 | -11.39067 | -43.54724 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 73d42413-be72-337b-a00a-5efe3d7d9a0c | -11.61209 | -47.15469 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b67444af-391c-39c1-88c0-d4d2f6e4e416 | -11.31782 | -46.56985 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| c34bf289-68d5-310b-9377-5bb9c8fc32e5 | -11.31431 | -46.56289 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ffd8d84f-ba01-3788-a687-6d93538c94ee | -13.82594 | -43.85993 | 2025-09-07 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 421b5285-a17c-3bd3-bfdc-a327e1789a32 | -15.36112 | -43.66497 | 2025-09-07 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3ed5f1ac-b2cd-37e1-b1af-e7327247daae | -9.84183 | -46.54967 | 2025-09-07 03:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| baed2951-3f18-3f7b-bcb1-7f950a00c1b4 | -11.78011 | -47.56166 | 2025-09-07 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30f870e2-62f3-3c63-abaf-faf8b42f7421 | -11.58851 | -47.16912 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 240c1e4c-a977-36f4-9907-b5f521cf747f | -11.41006 | -43.61292 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7f31cb6-614e-3f2b-b01d-3f97d0e3391e | -14.85429 | -46.69817 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 90d30b78-b6db-34d3-b003-7a213114a21f | -9.84121 | -46.55001 | 2025-09-07 03:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 745952db-ff84-31a6-a643-cffc649f17ee | -11.58561 | -47.18307 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 831c1145-8855-366d-b807-83d467ae4818 | -11.59201 | -47.18068 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5eb72fee-4940-3d79-8db5-7ea5d3670aa0 | -13.82882 | -46.27568 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5eb18d57-fa86-3826-9289-a77bf2800cd7 | -14.84743 | -46.69484 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 308ad5cd-bde1-3e83-b00b-93a533698607 | -11.24261 | -46.44613 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c2c3b67-0f54-3d08-b25c-a0209400e23a | -16.33304 | -41.95089 | 2025-09-07 03:32:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bddd28ff-0994-3c36-8d7b-94fd42e7c61b | -13.55123 | -48.1107 | 2025-09-07 03:32:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f15fd478-4460-3fe9-88b8-1b9196be23cb | -11.31907 | -46.56364 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 30fb2f48-ee37-324a-b8c5-89f1038cb9e8 | -11.59357 | -47.17345 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| d3a45165-8b6a-322b-8d4d-f71870aada68 | -11.24375 | -46.44045 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb394dbd-73fd-3795-93ad-f1b07ebfdc59 | -14.27188 | -44.97553 | 2025-09-07 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0cd2bb2-35d8-3eff-a43b-cabf0b0950ef | -11.38836 | -43.54439 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7ee3b99-a876-3ad8-ad2f-2ccf5eb67606 | -13.70829 | -46.8792 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 58092bc9-62c6-360e-a5c1-171f93a57175 | -13.85393 | -46.25081 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62be4af7-54d8-36d2-ac00-de8e7c1205b7 | -13.85527 | -46.24441 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3e2dc07-7999-3df3-9c58-66e787c74b30 | -11.3156 | -46.55671 | 2025-09-07 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 89ff564d-9502-36f6-bf5a-56610789a25a | -13.7122 | -46.88121 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ae9c5d50-f263-3493-98ca-13f59038a4c3 | -13.84169 | -46.25469 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c83dacd-e3a9-39fc-8bf3-83fec05c616e | -13.66998 | -46.96173 | 2025-09-07 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README20.md)
