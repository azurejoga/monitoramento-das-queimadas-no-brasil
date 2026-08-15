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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e396e59-fad3-3f63-992c-e9e8a339bf26 | -13.47632 | -51.80639 | 2026-08-15 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1b3ff01f-f0fc-3675-b1d5-7be6f2b9f0b6 | -14.05896 | -53.66557 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fd53ecf-4b1e-306d-a80a-60af90f8c8ac | -14.94535 | -46.63386 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1b7ba1c-b8a8-343d-b426-dbada9f37cb0 | -14.08444 | -53.62472 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d030281-e373-3890-9405-8cb9960802d8 | -14.43553 | -51.92818 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca6f4cda-b20e-3370-b91e-e75af7d43d58 | -13.22867 | -54.17846 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a66d627-38e7-3b36-b5c3-83d319061964 | -19.93725 | -42.13768 | 2026-08-15 04:17:00 | NOAA-20 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 81f023ca-5cc6-3d7d-9b3e-8e780a9e21fc | -14.92691 | -46.64011 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d039aacb-b157-3d80-9ac2-77c0d18077e2 | -14.91842 | -46.62534 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c42ad0f-bf65-3f4d-83a5-906ef953d5e6 | -14.98158 | -46.61502 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f21dee90-9597-3261-9228-2d3bc20ffe8c | -14.45636 | -45.67516 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7768e931-c7ca-3bcd-825e-9912146ead35 | -20.33717 | -46.73341 | 2026-08-15 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3eac0aa0-2276-3ef3-b740-78a64ae3b257 | -14.45099 | -45.69045 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baa4d10e-ddf5-355b-968a-c5908f936ac7 | -14.42745 | -51.91251 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6d558dc7-3159-39ad-878f-776ad4bbe959 | -16.87718 | -54.14729 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30cc354e-35b3-37dd-ae37-c4974d073f9f | -14.42946 | -51.85509 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce80e688-3ac2-3230-a312-e34bcdaacf51 | -14.4394 | -45.69634 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 858946c6-8fe1-3b58-9bdd-37e22a57e536 | -14.48677 | -52.08957 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 225e039a-a82b-3e92-8ce2-cd786f6c08a6 | -14.94614 | -46.62935 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b457ed9-07b1-3b64-aebd-293df0e6f7cb | -14.60428 | -46.73601 | 2026-08-15 04:17:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9303f3f9-90ae-3129-b13c-ef08886efe8d | -14.08935 | -54.52868 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64287462-7dc4-3a36-b14e-7320ca97da68 | -15.56953 | -46.42479 | 2026-08-15 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c4889d0-ba73-3fbb-aa01-273d43af9c61 | -14.13 | -53.67849 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9712e5ee-029c-37d9-9818-a3e14224bb2d | -14.07038 | -53.60206 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31d2d08f-256a-3923-a741-dc34264f0925 | -15.52625 | -52.99419 | 2026-08-15 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e3cd02c-51c9-3e92-a024-f651c070ea36 | -13.23541 | -54.17524 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78701838-f4a6-356d-b273-414b7c8bb2ca | -15.52359 | -53.00725 | 2026-08-15 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4fcf86a-c4d6-3f05-8f6e-c94e429ca16b | -13.24125 | -54.17638 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3092c20-b24b-3273-9c62-ad27a5042610 | -21.93295 | -44.49517 | 2026-08-15 04:17:00 | NOAA-20 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d6499091-3d80-3126-a968-17f8036e7e43 | -14.43325 | -51.93974 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52325dbc-2bd5-33c1-9370-1397fb4b906a | -14.43173 | -51.92136 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4ae1ca6-8d68-3fae-b227-694eaa9ca5dc | -16.10958 | -49.8609 | 2026-08-15 04:17:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 38a0f5d4-3db0-32b2-b883-744008ae3c7b | -14.46193 | -45.68407 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4636613-a0e0-3cc7-bd35-5a7a31e8b58b | -18.54725 | -48.20157 | 2026-08-15 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c075680-fe4c-3735-88a2-e7879eb64bd8 | -14.43019 | -51.92514 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ca953739-9f5b-3029-8704-f22705b29577 | -16.89094 | -54.13837 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cbd69c0b-a2ac-3b53-bf97-bb4e61cab1c5 | -14.46258 | -45.68022 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 013fed8f-b7aa-3d3a-94cf-83beb18899ed | -15.22091 | -52.72522 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90767f56-5027-3db4-95f8-03ae791a7168 | -19.04477 | -43.50847 | 2026-08-15 04:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5622aa60-ac30-3541-89a3-bf874a59fb03 | -20.28937 | -41.62286 | 2026-08-15 04:17:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cfaf6dfe-c5e6-3eeb-92cf-52a0ce7ecf9d | -14.30324 | -53.06385 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b6db1ad-83d4-3353-acc0-57ec5c6dd2b4 | -14.42301 | -51.91352 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 47408dce-53b8-3614-83bb-60a898abf140 | -21.93049 | -44.49598 | 2026-08-15 04:17:00 | NOAA-20 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3d64fcf8-0c87-38d8-9946-0ae11070dd80 | -15.5421 | -42.30225 | 2026-08-15 04:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 848f56d2-24cf-3c56-825a-1c54fd5fa933 | -13.22779 | -54.18275 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbf9c60a-1372-3278-91ec-ad3a77d6c660 | -14.75021 | -48.24733 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76713732-1d9c-3e6c-b083-0ceb19b62994 | -16.87803 | -54.14318 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5256af30-e94a-3acd-935d-7b7632ce089d | -16.98269 | -49.27249 | 2026-08-15 04:17:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4400ec7-2694-3b41-8316-451cd859b389 | -19.80197 | -47.84426 | 2026-08-15 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7600866b-a03b-31d6-9c1d-fbd06e335208 | -20.45872 | -42.01669 | 2026-08-15 04:17:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 05b7340b-cdd2-3b80-bb77-c0afadad057f | -14.46601 | -45.68082 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 319b82e2-fa97-3214-8da2-31e25ba137ac | -21.37511 | -46.7055 | 2026-08-15 04:17:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d1f82bad-fa5e-3124-a9a2-b7b60eef3731 | -15.99058 | -43.01332 | 2026-08-15 04:17:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1cff90ae-4a2b-3046-9e53-96c97d651910 | -15.12545 | -48.7019 | 2026-08-15 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b635e58-eb76-3dd4-9902-d2d20ad3ca74 | -13.26775 | -54.19553 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dfb2353-76a6-3fed-98e6-922346857ca9 | -19.68574 | -45.40234 | 2026-08-15 04:17:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| daf913d2-c229-3457-bda9-e3e90ac6354d | -14.43895 | -51.91083 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 71907f3e-6979-3e48-8136-50e8089f0529 | -20.28884 | -41.61992 | 2026-08-15 04:17:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 95462bbb-9dce-3ca8-827b-7ff3e74cf512 | -14.43781 | -51.9166 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| b6896daf-cf7f-3f6d-aa66-f368c8cd2634 | -14.71191 | -52.88496 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7162d0-da23-3213-bbd2-c06548d9a2f1 | -14.24363 | -45.41573 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c2d9376-7463-3758-b5db-3917a94d3fff | -14.45914 | -45.67961 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa12bb9d-3487-3d14-96c2-5c7de2cb3cc0 | -14.07715 | -53.60321 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fc7156b-dbb4-351b-83f9-b89f34579687 | -14.11643 | -53.65971 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9f8d496-6cb5-37aa-ab65-584bba55fb3b | -14.95744 | -46.62757 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e6f1ebaf-3541-3f0a-9d6a-3b106e0c09dd | -14.98586 | -46.6114 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93fc27dc-aed3-3e36-ac71-db7e0a96da33 | -14.91554 | -46.64233 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fb3f9c4-c93b-3454-a616-27d59c19e75c | -16.89281 | -54.15628 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1bf090b2-1983-3fa4-837f-354a4a853158 | -15.15423 | -50.05699 | 2026-08-15 04:17:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 389d6dff-cb39-3dca-a809-0323f0cb9ab0 | -15.65436 | -48.21519 | 2026-08-15 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42ef81ff-c345-30a5-94b8-f19af50eaab3 | -18.8914 | -47.25298 | 2026-08-15 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32afd0cd-d30c-3c3b-bd34-840ae036aa8d | -18.17133 | -43.98647 | 2026-08-15 04:17:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 423e8044-bd2d-3fa3-bda4-5cb5e8fa43d2 | -14.60024 | -46.75064 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ca75fd0-860a-3413-ba82-c0092cae4d55 | -13.81182 | -53.79011 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eefea7f1-916f-3032-88b9-75390c7f43e0 | -13.91243 | -53.95462 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3d6ff66-b1fc-3083-9c39-d71a8d073ef0 | -18.58352 | -47.14369 | 2026-08-15 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1604f403-a6e7-3bb6-a5ec-78cc61fa5330 | -14.22657 | -45.41273 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74ccf801-8b17-3372-8135-a32df1c9efb3 | -14.59996 | -46.73958 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0c32ae9-6aa3-3595-b6a4-093fee1d482c | -14.12923 | -53.68233 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c02bcb84-5d72-3040-8ddb-247fa5594b09 | -14.43239 | -51.91354 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e493e378-6c28-32bd-bd21-a39b06df2305 | -20.00234 | -43.97207 | 2026-08-15 04:17:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0552ff2c-5af8-3e94-aad7-cfa15c798503 | -14.42186 | -51.91932 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0b3de07f-59c3-39ae-bff4-734b22b52caa | -13.41816 | -57.04786 | 2026-08-15 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d0e5450-e3fb-3a2e-be15-b8c0813058b8 | -14.43438 | -51.85608 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bc2ddf9-118b-3727-ad6c-e7de4a143e84 | -16.66814 | -49.41502 | 2026-08-15 04:17:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ce8be94-5497-3370-a529-af0d646a85b8 | -16.89512 | -54.14301 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f8b1327a-285e-339e-bb8b-9f066cf26061 | -15.15604 | -50.0713 | 2026-08-15 04:17:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67b7326e-b3db-372f-9852-2acd50be1b04 | -14.42565 | -51.92612 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2018ed63-4c27-3199-bfbd-8841aa32f9b1 | -18.58002 | -47.14304 | 2026-08-15 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bb923aa-f8b6-30d0-8a0e-15fcaf89250f | -14.08307 | -53.62468 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be10b656-88ee-3d82-9728-3c5da4b000fa | -14.57437 | -46.77219 | 2026-08-15 04:17:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a558125-c1d1-36e4-a9d6-4262e840b42f | -19.84028 | -43.18802 | 2026-08-15 04:17:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 58ccb5ce-7c27-3e98-93c3-daa37b92b74a | -14.3025 | -53.06763 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fc141c0-a193-3cba-b024-77cc31b437ee | -15.65141 | -48.20946 | 2026-08-15 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb83f013-be53-3452-836c-8cc5c93ac35e | -14.44994 | -51.90714 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d20b0ae8-ecb7-30cf-81d4-cfa81cd121bb | -14.39593 | -48.94504 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a4307b3-e911-3b09-8c2b-6005724ba787 | -18.17466 | -43.987 | 2026-08-15 04:17:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de927757-2c9a-386e-bff5-147e78331807 | -21.52434 | -45.63475 | 2026-08-15 04:17:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 44894575-0af5-3f56-b7ed-37c3e55ba7b6 | -16.88265 | -54.14835 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8fd719c1-8038-301c-823e-bfbf1a1dc941 | -15.52744 | -53.01493 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |


[Clique aqui para ver as próximas entradas](README19.md)
