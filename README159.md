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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22541194-2cf6-3cf1-844b-5de3b57f9b6a | -9.2199 | -67.3852 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 0bfae551-2b1e-3d01-923a-963efc58d9a5 | -2.5353 | -65.8635 | 2026-10-05 18:10:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 61bca4bf-4434-302c-8ddc-caf766938cff | -9.393 | -65.8918 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 9796d045-eed8-3733-96e9-877fab141a88 | -9.1438 | -67.9428 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3a9c764f-55de-3116-b197-73ed46bb91ca | -4.786 | -42.5853 | 2026-10-05 18:10:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 549b7584-df84-3bcc-b653-345e51e59c65 | -9.0983 | -65.4717 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8b1cbefc-abdf-3035-be98-b7c369ad75b2 | -9.0982 | -65.4904 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 51bbebbf-8596-3044-a831-068be0cbbdad | -5.9606 | -41.3507 | 2026-10-05 18:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 823.0 |
| c3c7440e-6d60-38a5-8362-ce7f96a1f868 | -9.077 | -66.0881 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 6ca5b6de-e768-3222-ace9-94d552428f4d | -9.1174 | -65.359 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| b0508420-e1bc-30f0-930f-7297db679b70 | -5.9608 | -41.3266 | 2026-10-05 18:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 132.7 |
| 723ef5dc-64fc-3a4c-8f70-8fb74fadef3d | -9.1243 | -68.2391 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 3ffc6c05-6e24-3f63-8277-2d15dc7cdce6 | -8.5554 | -66.9945 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 8bae050e-9bd1-3505-8d7c-a4f4348c6b27 | -9.1253 | -67.9432 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 702fc0ef-17e5-35c2-b9e3-59a5905d708c | -9.1076 | -67.703 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 125.5 |
| d1086451-aaf0-380b-9aa4-5a5f2b0b32fe | -9.4751 | -64.3336 | 2026-10-05 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 1eab80ad-7f8e-3947-b762-d4866bcdeaf0 | -9.2367 | -67.8665 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f61f5fe1-fe9f-3092-b680-64d70550e542 | -7.997 | -42.9175 | 2026-10-05 18:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 139.2 |
| 1941ee3c-5d62-3e35-a42b-00d84d880c08 | -9.2366 | -67.885 | 2026-10-05 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 1b4f4cf4-3744-3b46-ab9c-3f95432ddda6 | -7.4889 | -42.8059 | 2026-10-05 18:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 8a0c2fe9-e305-302e-b4c5-7735f5c271c6 | -2.5353 | -65.8819 | 2026-10-05 18:10:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| aa020744-b3a3-3cac-87d8-7f5de2b751f6 | -9.0988 | -65.3596 | 2026-10-05 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 314a8e8d-cc97-3d2f-95fb-ff85777890ac | -2.79 | -57.66 | 2026-10-05 18:15:00 | MSG-03 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a4d6395-a30c-3261-8a4e-4a1b9c7efa10 | -3.11 | -53.75 | 2026-10-05 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 144a8b17-66ce-3d69-84ca-ac51bad8aa1b | -2.76 | -57.66 | 2026-10-05 18:15:00 | MSG-03 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30d43353-aa94-3c75-bea1-51f9c237ec3c | -4.8 | -42.12 | 2026-10-05 18:15:00 | MSG-03 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fa3ec91e-b1dc-3fcf-9dec-6d38dbfadd2a | -3.11 | -53.69 | 2026-10-05 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59f25313-e8f6-343a-9d6e-68eecd5ff033 | -13.80436 | -40.9581 | 2026-10-05 18:17:00 | AQUA_M-T | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 99a53e80-320e-3276-9dbf-ae21a668969e | -17.89486 | -39.42505 | 2026-10-05 18:17:00 | AQUA_M-T | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| a64d3308-5ce2-3076-8a1e-b3294a7f282d | -14.73435 | -41.77754 | 2026-10-05 18:17:00 | AQUA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 275.9 |
| e6ed2f2c-959c-36c3-87c0-e74c2a9e1ebf | -15.89452 | -40.73359 | 2026-10-05 18:17:00 | AQUA_M-T | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| aaca8cab-ef39-30b7-a843-94f8a04131c7 | -14.01791 | -41.01977 | 2026-10-05 18:17:00 | AQUA_M-T | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 35.1 |
| a212b77c-e4c9-39fe-ba79-063a49890da7 | -16.83218 | -42.23376 | 2026-10-05 18:17:00 | AQUA_M-T | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.9 |
| 91d8bb56-0c8b-3235-a44d-65967f64a79d | -16.07478 | -41.35073 | 2026-10-05 18:17:00 | AQUA_M-T | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| e8bce793-fa7a-351e-ae62-cfd12a34e173 | -12.86488 | -39.92552 | 2026-10-05 18:17:00 | AQUA_M-T | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 5f51cf15-7137-39dd-a95d-5ad1cc990483 | -13.37071 | -41.34423 | 2026-10-05 18:17:00 | AQUA_M-T | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 6d6f23e9-1dee-3242-a714-69bdb880c569 | -14.79838 | -41.55936 | 2026-10-05 18:17:00 | AQUA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 30.4 |
| b8f8079a-49a8-312c-a41d-50c2d2d9239a | -16.26066 | -41.92784 | 2026-10-05 18:17:00 | AQUA_M-T | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 92e1cdca-b645-3422-8fc7-d3327ba966dc | -13.01588 | -40.1403 | 2026-10-05 18:17:00 | AQUA_M-T | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 18.9 |
| d014424f-febd-3ae3-aa55-3a2a08a21271 | -15.48654 | -40.76451 | 2026-10-05 18:17:00 | AQUA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 769efb53-037f-324f-9d69-973d482eb084 | -15.79697 | -40.32371 | 2026-10-05 18:17:00 | AQUA_M-T | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| 4887a405-48cd-372c-8ef4-0665ab679682 | -16.16588 | -41.24635 | 2026-10-05 18:17:00 | AQUA_M-T | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.0 |
| b34a71e6-7990-3c5c-9ab4-3f394e4c8aa7 | -14.74153 | -41.76955 | 2026-10-05 18:17:00 | AQUA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 207.5 |
| 6cce7390-aeed-3b47-9908-d0c245dcc391 | -12.71055 | -43.11671 | 2026-10-05 18:17:00 | AQUA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 81db4ac8-62af-3fdd-a88d-764777cfec45 | -13.21279 | -40.23657 | 2026-10-05 18:17:00 | AQUA_M-T | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| e028e046-f833-39ac-b19d-93deb4581180 | -14.73219 | -41.76079 | 2026-10-05 18:17:00 | AQUA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 1e91ec35-1ff4-3274-979c-73498d04472c | -12.55386 | -39.59683 | 2026-10-05 18:17:00 | AQUA_M-T | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| dcef46da-fe8a-3b5c-9c8e-67623ed46c92 | -14.63609 | -40.57144 | 2026-10-05 18:17:00 | AQUA_M-T | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 2447d9ba-1ff0-3dfb-98b7-3b52667e06fb | -15.50512 | -41.27922 | 2026-10-05 18:17:00 | AQUA_M-T | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 9814d41b-e3ee-3c52-b7f4-80ced7918124 | -14.90054 | -40.326 | 2026-10-05 18:17:00 | AQUA_M-T | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 186cf7e8-9f9c-303d-8f30-d38d43e755a5 | -16.38146 | -39.48804 | 2026-10-05 18:17:00 | AQUA_M-T | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| aecdf3e0-4605-3335-9c6f-b9c54a5bdb4d | -13.00919 | -39.55648 | 2026-10-05 18:17:00 | AQUA_M-T | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 6c1f73a8-ab25-35f3-b261-bfedc8a23ef5 | -12.96328 | -40.66891 | 2026-10-05 18:17:00 | AQUA_M-T | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 6118c529-9b0c-3ca3-89d1-7bb62e79d761 | -13.31126 | -41.06094 | 2026-10-05 18:17:00 | AQUA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| c8436daa-f3a1-313e-a5f1-3a5dccc77619 | -15.50591 | -41.26774 | 2026-10-05 18:17:00 | AQUA_M-T | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 128.6 |
| e1f0ddb4-c2d9-3d1a-9e28-4bb22235039b | -15.59127 | -40.32133 | 2026-10-05 18:17:00 | AQUA_M-T | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| b57e51c4-0fba-30d0-864d-12d0b002972d | -14.7436 | -41.78661 | 2026-10-05 18:17:00 | AQUA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 00f12bdd-0e28-3b03-ae0e-4bf7eb9aa94a | -12.60879 | -38.06517 | 2026-10-05 18:17:00 | AQUA_M-T | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 69e88396-0a67-3a5d-9bc6-a203d2b953a7 | -12.71299 | -43.13679 | 2026-10-05 18:17:00 | AQUA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 44.6 |
| fc27e5ac-11d2-3187-a2ba-0ca3af52177c | -12.83561 | -44.45499 | 2026-10-05 18:17:00 | AQUA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 1ca77c54-4b04-3a03-91cb-225e1c4774b5 | -13.51515 | -40.84378 | 2026-10-05 18:17:00 | AQUA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 38ee453d-a5dc-309d-a461-f3e496b3f383 | -15.69559 | -39.78632 | 2026-10-05 18:17:00 | AQUA_M-T | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| e49847fc-f31e-3f93-9c16-a1da1995d1e2 | -15.51661 | -41.27779 | 2026-10-05 18:17:00 | AQUA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 54.8 |
| 9e382e86-6714-346f-ac7b-5d1f923bf069 | -13.51122 | -40.85085 | 2026-10-05 18:17:00 | AQUA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 44.8 |
| 00051deb-b389-301c-a9a1-a5edf7be8f63 | -16.32473 | -43.80138 | 2026-10-05 18:17:00 | AQUA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 87152c14-83f9-3bb4-afa3-98b6b428913f | -15.89583 | -40.72675 | 2026-10-05 18:17:00 | AQUA_M-T | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 160.2 |
| 38a9c502-c46a-34d0-9e2d-02ce9bccf314 | -15.51464 | -41.26178 | 2026-10-05 18:17:00 | AQUA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 109.5 |
| a6a503f8-5bab-3dc5-93b7-01093fb77103 | -15.15016 | -42.16573 | 2026-10-05 18:17:00 | AQUA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 76492476-7ca9-392b-9e93-fb9f961e76d3 | -12.09704 | -38.10176 | 2026-10-05 18:17:00 | AQUA_M-T | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| c777081a-8486-37ae-832e-e46d84cbd4db | -14.79459 | -41.55513 | 2026-10-05 18:17:00 | AQUA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| f6226492-e1e3-3c5c-846c-fa9aef683ab1 | -16.98005 | -45.49804 | 2026-10-05 18:17:00 | AQUA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ca4bec78-510a-3cbc-9e00-c80d0be22cfa | -12.60789 | -41.90988 | 2026-10-05 18:17:00 | AQUA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 6e34b6a6-71c9-3e64-8f3d-e3bc141e754f | -15.79525 | -40.3104 | 2026-10-05 18:17:00 | AQUA_M-T | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| e2d18008-398e-3bca-80b0-604e5fed17a4 | -13.80063 | -40.94983 | 2026-10-05 18:17:00 | AQUA_M-T | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 3eb1b803-24b8-3f95-ae65-d2efcd546fe6 | -15.50313 | -41.26294 | 2026-10-05 18:17:00 | AQUA_M-T | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 47672e1b-b178-374a-aba4-951b9b1e2db6 | -15.48469 | -40.75 | 2026-10-05 18:17:00 | AQUA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| bc3b380a-b56b-39c3-bd22-2911f60bbe5e | -14.65039 | -42.02345 | 2026-10-05 18:17:00 | AQUA_M-T | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 80d919e4-cbe2-3452-98ca-083f92a96d98 | -13.22302 | -40.23528 | 2026-10-05 18:17:00 | AQUA_M-T | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| ae0b9b1c-3600-3cd8-9e3d-877e5b73fbce | -12.72573 | -43.13512 | 2026-10-05 18:17:00 | AQUA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 28.8 |
| e4eb2e2d-f524-37ee-9b73-891e25861bf5 | -15.6972 | -39.7988 | 2026-10-05 18:17:00 | AQUA_M-T | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 5da7c18e-7831-3a68-a3cd-bce13e1b96be | -15.89397 | -40.71173 | 2026-10-05 18:17:00 | AQUA_M-T | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 139.8 |
| d4916636-673e-3a4a-ac37-680c2a7d2c51 | -15.89257 | -40.7187 | 2026-10-05 18:17:00 | AQUA_M-T | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.6 |
| 6e5735ec-2fe8-3035-9126-d24eac7c09b0 | -14.79655 | -41.57133 | 2026-10-05 18:17:00 | AQUA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 4aaa60ff-93e0-3523-bed2-42ef145981a5 | -16.16389 | -41.23011 | 2026-10-05 18:17:00 | AQUA_M-T | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 134.4 |
| 0376cbcb-cfbf-3112-b3a3-f41a2080293e | -12.75712 | -40.03795 | 2026-10-05 18:17:00 | AQUA_M-T | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 1aba1b5b-22aa-367c-86e3-e63eea58aa9c | -14.63838 | -42.02503 | 2026-10-05 18:17:00 | AQUA_M-T | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| ef9cf887-21fe-32bd-a570-fcab870ee596 | -12.72268 | -43.12191 | 2026-10-05 18:17:00 | AQUA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 46.9 |
| 5825e788-6e0f-3e14-b8fb-c08ebfff03c3 | -13.50938 | -40.83716 | 2026-10-05 18:17:00 | AQUA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 6c413915-b84f-304b-a8aa-875cf08e2a42 | -17.11023 | -41.74373 | 2026-10-05 18:17:00 | AQUA_M-T | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| ffc49c4b-a57c-39fe-86a4-a77ef240da03 | -15.27414 | -42.1939 | 2026-10-05 18:17:00 | AQUA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.4 |
| 2c669d68-2855-3903-a1da-b6d7a2248dbd | -17.89655 | -39.43808 | 2026-10-05 18:17:00 | AQUA_M-T | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 18700577-6abc-3671-b306-31f55529932f | -14.90239 | -40.33995 | 2026-10-05 18:17:00 | AQUA_M-T | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 13b7d9ce-61d4-31a6-9fd2-4b31ea567bce | -6.61694 | -37.89546 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 0fd5c3ea-31e0-3e90-90f5-759056cf6619 | -10.33885 | -39.49924 | 2026-10-05 18:19:00 | AQUA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| af32e2e6-dd4c-3ab0-b574-e4c6d840ae87 | -3.90026 | -38.39601 | 2026-10-05 18:19:00 | AQUA_M-T | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| bf88de1e-8aae-38f6-b107-804e0cd5e04e | -8.16022 | -35.72377 | 2026-10-05 18:19:00 | AQUA_M-T | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| f91611ea-4190-3e11-b250-c680f5c67034 | -4.51473 | -42.05957 | 2026-10-05 18:19:00 | AQUA_M-T | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 126.7 |
| c5ff8238-84a4-3f64-9067-62f08b11728e | -5.89407 | -43.45192 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f2fcbb19-318f-36c0-901c-cba19dea0cf5 | -5.73246 | -43.35696 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 94cbbfdf-f0b2-3c44-ab4e-f96d054dbaa5 | -3.17049 | -40.8567 | 2026-10-05 18:19:00 | AQUA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README160.md)
