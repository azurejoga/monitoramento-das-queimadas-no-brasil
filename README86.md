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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f25e5dfc-b871-3cc3-a18b-b383fbdc118d | -12.90143 | -47.97116 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d16c4d6b-3053-319e-9217-9a2f0f2fcb06 | -11.80159 | -50.56988 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c32633db-b5c5-3d94-ba48-9e72de0cc9cd | -19.74812 | -46.08915 | 2025-09-12 04:27:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ab2a723-bdb2-30c5-bf15-08afd1397066 | -12.82529 | -47.95863 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80977b8e-76a8-3b3e-877c-6b9ffcb3786f | -15.11897 | -48.033 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7cda78c-a1c8-3b90-aa75-24d18c03d052 | -11.2174 | -54.99422 | 2025-09-12 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33517018-e5cc-3c07-a812-cb3386710b6b | -15.79435 | -52.23044 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6cbfef89-d112-34ce-ae78-2284f7e13c71 | -14.17332 | -46.18119 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75bca91e-855f-3664-85c9-a3022df881be | -20.20509 | -44.55463 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e9d0c0c7-04f1-3d40-a943-defe25deb20f | -15.55966 | -41.79076 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 196e786c-7bbd-33cb-85ea-9e3d174191f7 | -16.48651 | -51.99102 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8f4faae-991b-3887-88f6-1a0a049fafbb | -15.78824 | -52.24327 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8c954fb-c04b-3c29-9d81-2fdbd57d8973 | -14.61645 | -52.09204 | 2025-09-12 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 988700c5-585c-316d-a285-10b0cdc7db78 | -15.15955 | -52.40731 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b5286a7-5bed-33b3-853d-8c3fba3ef883 | -11.18951 | -55.09205 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66a3f8bb-d1fb-3fb0-a46f-2b98ad84ac49 | -16.80723 | -47.82558 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a9a5e6e7-011f-36ac-b1d0-825ae201078e | -12.89592 | -47.96302 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 083fa207-03a8-3f60-9a7a-a364c410f851 | -13.16939 | -50.08767 | 2025-09-12 04:27:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23849c4a-979e-3cde-9b4e-b3a2f62b139b | -17.21572 | -48.6901 | 2025-09-12 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb494772-47f0-34f3-96fa-a5f7b0870b3d | -13.94491 | -48.22282 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c33c24b-81e8-371e-ad16-77a1a7c176bb | -12.95779 | -46.7402 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6a45138-3b56-3f93-8fce-7165ad7f6bb8 | -17.33473 | -46.66953 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78f93e5d-974b-315a-93d9-53657c85f1ff | -13.30792 | -42.38356 | 2025-09-12 04:27:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c36f5b84-ef23-34da-9d00-f54ce80d2d62 | -14.16533 | -46.188 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8892dda7-7536-326b-a49d-3fbeb34139c7 | -15.68029 | -52.22799 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f48bc66f-ae95-3ef9-b118-4141862bd774 | -16.4918 | -51.98502 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5dc1f3b-2293-3c99-86f8-41954639ce48 | -12.82474 | -47.96212 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cdf0781e-839e-39eb-a078-b5adbab30f77 | -15.24223 | -53.83627 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a62f4c06-7735-3e53-a369-c920a6610598 | -15.09856 | -48.01135 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0931a8c8-771f-3d1b-96ba-2fbc9037c0e8 | -13.78025 | -46.28286 | 2025-09-12 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 45fc3928-845e-3159-9201-27f396537d70 | -15.15435 | -52.39266 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f077d274-15b2-309e-ac98-67aca02b0425 | -14.38874 | -52.95517 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 435a1602-654a-39af-bd50-ae238de33537 | -14.17447 | -46.19702 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd1eb2d7-fc42-3111-97c1-8747c44d53b9 | -12.9283 | -54.74892 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ea5cb7f4-e918-3154-b7dd-069e79030e0f | -18.65814 | -47.66766 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c6f398b-a3b0-3751-aa93-38834b30f4cc | -11.18866 | -55.0699 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57b86395-1246-31c6-be8d-ebb7a9bacf7c | -18.67162 | -47.66999 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd26f871-dc57-3a1c-9d3b-23ebcf41b3a2 | -17.3438 | -46.67367 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 17307972-ff56-3409-91d4-b242b564484d | -11.20197 | -55.07812 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 087ff54d-9bca-32b4-b8ea-8dde13374259 | -13.58721 | -47.69161 | 2025-09-12 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3454a27d-cfe2-39f5-897f-5e08f1a48d76 | -17.81751 | -46.73412 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c61a249-ecfb-336a-9d21-40addb50d128 | -15.69108 | -47.02332 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e96c949a-1d6e-34fb-afec-7bc35905c262 | -13.14668 | -47.14361 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6633130-201b-39cb-b658-386a30737ee3 | -16.42333 | -45.69558 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8d5f334-495e-3217-b8c0-02818f8429b1 | -17.20257 | -50.14699 | 2025-09-12 04:27:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d507371c-b249-35d9-b2be-53a8d35a0b38 | -15.51926 | -48.55307 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1642f839-852c-39cc-a3da-bacaea6c52f2 | -13.92118 | -47.96441 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 816fd6c3-fa0e-3f83-a4c1-d524d31a74bd | -13.36913 | -41.91773 | 2025-09-12 04:27:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5fea9542-735b-3ade-927a-91db4d4ce56d | -14.51087 | -53.90702 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5c1940c-0dac-391b-bcdd-ceb1fbdc9664 | -14.17276 | -46.20855 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2224dbb4-d041-3392-995e-3843eba03cb9 | -13.36034 | -41.92596 | 2025-09-12 04:27:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| d2a8c73e-6b5f-3753-9ccc-42fa16077c5d | -13.356 | -41.92595 | 2025-09-12 04:27:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 98ebabd3-6d2a-32e0-82f8-a092420d7b6f | -15.14931 | -52.46537 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c09d201e-6631-3ace-96bf-71f54e3d5c2a | -13.25148 | -43.76719 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fe3d2d7-efe3-3de6-8392-f14cbfbac182 | -14.12831 | -45.37658 | 2025-09-12 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba04f910-2b79-3352-a45d-d3df5c55f41e | -11.18291 | -55.07426 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bc05469-e259-3c37-95db-3b5e45f96685 | -11.22686 | -54.9962 | 2025-09-12 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d9510d1-467e-35c3-82a0-4fb5e5a9b211 | -13.27417 | -51.71937 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2e781beb-e491-3f09-8c2e-ee96120f3e71 | -17.35645 | -46.6837 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49846cec-e4b9-3d15-9929-09a5da7aad14 | -12.88105 | -47.94979 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8c793ae-af21-3818-8928-fb89e144003a | -14.17562 | -46.2128 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a3d85223-c6cd-3c05-b48c-23e730359e7b | -13.91499 | -48.26151 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3df6b6e3-5749-3a28-b6a4-22d35f2c91a3 | -15.79358 | -52.2348 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e766968-6401-3034-9772-24cb2092c80c | -16.06975 | -49.96986 | 2025-09-12 04:27:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e868cfc0-b812-3ab3-b3f5-fcb5da428014 | -17.8043 | -50.00404 | 2025-09-12 04:27:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf5d9426-a558-37b1-855e-5d49542907ea | -12.58688 | -45.68317 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38c73086-dde2-3de0-b4b6-83ca547bd1e5 | -15.11947 | -48.61107 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a884e09-7110-3a6e-8b8a-946653094bd4 | -12.92787 | -47.99653 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49d0423c-cf8e-30d1-8473-7c2dd6b4aa33 | -15.78988 | -52.23411 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a0b31ea-9316-3d46-aa89-0e3e7f33eee3 | -17.91454 | -45.90649 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fb15f64-f216-37b0-a51f-a6ec36289c52 | -11.19059 | -55.05945 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edc4668f-afa4-3e37-a410-04e70e5dec28 | -18.77245 | -48.54495 | 2025-09-12 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e46f17e-08dc-3647-8c38-cccbfe295aef | -11.92304 | -50.71483 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 689eb1f1-43eb-3530-8a6d-75f7b59ab4da | -13.9123 | -48.23558 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5179c480-f451-337a-94c2-712c331c4c18 | -14.43049 | -46.4012 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef8c1133-340f-353d-99b8-892bb43a2d93 | -13.91951 | -47.97504 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f01fde78-4126-3d2f-8b36-ebb9751215b4 | -18.87761 | -48.12043 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1299318-985c-3ae2-95b9-659c2886fc15 | -17.35187 | -46.69096 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 195d1c8a-ff20-3701-8b43-ea231e668834 | -17.35362 | -46.70315 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4309b48f-d45c-38d6-adec-f0d77ad9d9b6 | -14.37592 | -47.2892 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02bec4a7-d921-3b72-8ffd-1b66250d815e | -15.10765 | -52.45776 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a454a2a-7ac3-3e78-9ac0-30369b041693 | -15.11841 | -48.03656 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ad005ed-b26e-38eb-8497-814dc62ec170 | -14.16419 | -46.19566 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bed2c39c-073d-3517-bb77-175ff748b581 | -13.90568 | -48.23451 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 07744b6f-3291-3a9f-a250-70a9c0a49979 | -16.51375 | -55.17292 | 2025-09-12 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6759d113-e0b3-36ce-958b-9326f21a077d | -18.59703 | -47.18458 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 629c13f3-fa96-31f3-8714-c0ad615a471c | -15.52644 | -48.55061 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fbabf63-fed6-35ff-86f3-e65126ffe840 | -13.90899 | -48.23505 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 19b48c25-a271-383d-bdea-041303f5d313 | -14.3293 | -54.11702 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 250de007-c8e2-3ceb-8090-726b981c6076 | -19.19736 | -48.00881 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a2a21f8c-b897-3916-b211-30d93906fcf8 | -12.9526 | -54.74417 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0af4ba80-a491-3bef-8c5d-b7294d9793a6 | -18.54211 | -48.40952 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d1ef2f8-6a0b-3d51-94f9-e3a0b9364684 | -13.90393 | -48.2669 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 82590bf9-e6ee-3cb8-853e-04ee0c1b2a05 | -16.44424 | -49.03579 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9e360f3-f5bf-3b51-bfcc-ab57782e0498 | -13.91055 | -48.26801 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 52862c80-d5fa-3e0a-a202-c2abda65fbcc | -12.56618 | -49.14744 | 2025-09-12 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9afd1a2-ea8b-3f9e-96cc-8384e26c4ed8 | -13.50888 | -50.81109 | 2025-09-12 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b922c4c8-06dd-320a-8937-a4cdaefdb98a | -11.86672 | -58.81255 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40c41ea2-ebe9-3b84-bffb-ed84c6a43553 | -13.92224 | -48.23717 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2eda36d5-f435-39eb-980f-fe86cea5358f | -17.81694 | -46.73805 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README87.md)
