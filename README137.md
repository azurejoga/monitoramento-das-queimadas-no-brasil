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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcbe5a33-fcb3-398e-9996-38296248c72d | -17.34528 | -42.6786 | 2026-10-10 05:08:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c560be5f-9061-3212-b54f-9710ea94be95 | -16.12761 | -46.8879 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71254e37-6d64-3893-b2a0-699449a8508d | -17.46328 | -45.07426 | 2026-10-10 05:08:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5be85a66-7c99-3d0e-a89e-09e3ffe80587 | -17.45657 | -45.07845 | 2026-10-10 05:08:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d83ac98f-d737-3175-8477-2bd1f76a3915 | -15.65475 | -48.13995 | 2026-10-10 05:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09bab9ce-d499-3d2a-ae4e-c12e965e3f4d | -15.08749 | -46.94239 | 2026-10-10 05:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6c6ee19-b5cc-3caa-b8f9-89352064e34f | -18.915 | -47.92039 | 2026-10-10 05:08:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b391ac1-b7bf-3f1f-8514-da1804bef286 | -16.76295 | -47.06923 | 2026-10-10 05:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6281464-fcfd-3133-93c8-c00c22849619 | -17.46175 | -45.08957 | 2026-10-10 05:08:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be4cf1ee-916e-382f-8201-41741f4132be | -19.08132 | -48.14614 | 2026-10-10 05:08:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5110b319-c405-3493-ad0d-ec2a87934b41 | -16.58311 | -46.76545 | 2026-10-10 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57d65fed-410f-3e7b-b886-bafdab14aaea | -15.83765 | -47.45784 | 2026-10-10 05:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a0bf47e-03c3-30b7-9d65-854c9f8295b6 | 2.727 | -60.2586 | 2026-10-10 05:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e7956c03-b1db-3ada-9037-eee81e1316f5 | 2.727 | -60.2586 | 2026-10-10 05:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ffa45685-a859-33b2-bdb1-78ff514bfa5b | 4.28495 | -60.91367 | 2026-10-10 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a5b8b10-8f50-302d-bd49-246d52b6e843 | 1.73128 | -55.57232 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e7c1330-c7af-3def-80e9-3af2f635b984 | 4.26943 | -60.88867 | 2026-10-10 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9571ab76-0d5b-3e1b-9efa-5c734eac7cd4 | 1.67029 | -55.61588 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e932b86-902f-3a8e-8e03-4a30b6b7c649 | 3.04385 | -60.54395 | 2026-10-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc742317-1560-3572-aa86-70e8c9b92679 | 1.76969 | -55.52831 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6ed00a8-9baf-363e-852f-b4cbeed81849 | 1.67532 | -55.61156 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be72d7e9-ba24-33bb-a139-ccae49bbf19c | 1.21484 | -59.97518 | 2026-10-10 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1c2e421-3781-3bfd-b86d-ea58619803c5 | 1.21546 | -59.97904 | 2026-10-10 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 573b80bc-324c-3b6d-84e8-2c838cb359bc | 0.94566 | -55.75528 | 2026-10-10 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dbf91c7-fc0a-34c7-a017-cc3582b57532 | 3.03998 | -60.54457 | 2026-10-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14dca47f-f567-3b1b-9538-57343e983797 | 1.21896 | -59.9745 | 2026-10-10 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa3ea9ba-1c86-31c2-a14c-98d00ed4c0ec | 4.42491 | -60.89471 | 2026-10-10 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5df53f6d-53d7-35bd-85f8-172e135df514 | 3.0392 | -60.53972 | 2026-10-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fec8d9c-7e2c-31de-aa3a-4c5cd43ce21d | 4.27831 | -60.89632 | 2026-10-10 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e459e15-cb84-3b08-a414-9b2edc68feb9 | 0.78895 | -59.19861 | 2026-10-10 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fa92982-8858-3dc4-997e-8b462f118cdd | 0.78962 | -59.20284 | 2026-10-10 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4edfcd8-c8b4-378d-9692-c83c8171c8e6 | 1.98397 | -60.61325 | 2026-10-10 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c7179230-1cfe-3a34-b8fb-d68f15e80c1a | 1.68018 | -55.60684 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 088b9c91-c7f9-35a9-b03a-e80f6b1b2f35 | 3.04771 | -60.54332 | 2026-10-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1818fc1-f62c-3ca2-826d-7fa2479b3778 | 2.72969 | -60.2646 | 2026-10-10 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 4c476305-ed57-36ae-b1ee-16988389754a | 4.55615 | -60.71561 | 2026-10-10 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d1516a0-7317-3de9-b8c9-7109c6c57b78 | 4.55839 | -60.71358 | 2026-10-10 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a516418a-bae4-3f6b-b3a5-544492e17e98 | 1.77522 | -55.52734 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a59c3629-340c-336a-9ee0-c5e47d1b9710 | 1.72693 | -55.58056 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58519f91-5468-38f4-8e81-a867d04a57a9 | 1.68024 | -55.60701 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c72c392a-9d98-3171-905b-f2b674b2d35d | 1.67524 | -55.61141 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad8d5beb-7895-3d10-b35e-b0d64b56a12e | 2.72889 | -60.25951 | 2026-10-10 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 049758a1-732b-3ba8-ac75-068ca253f8a1 | 4.27388 | -60.89251 | 2026-10-10 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a92b6edc-cf14-3d05-9744-c8fd0fbe44f7 | 4.68656 | -60.5876 | 2026-10-10 05:46:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e578faf-d98c-3168-9d41-81ed1eda4592 | 0.94508 | -55.75151 | 2026-10-10 05:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 422496dd-120b-31a7-a2a0-a7da3267877f | 3.0369 | -60.55003 | 2026-10-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 27fd790d-6d19-3af0-ab86-56b45a3a1e9a | 2.72494 | -60.26014 | 2026-10-10 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 24e7b5b8-d896-30c3-815f-99c5172f1c17 | 1.67085 | -55.61948 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9fec6257-7e45-3b14-bec7-002c3a6dcefd | 1.68455 | -55.59874 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4e5098f-22c4-3fbb-bbee-353278464857 | 2.38986 | -60.25299 | 2026-10-10 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c338b685-221e-3037-b611-17739c60257e | 1.7301 | -55.56501 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18fb08ed-be83-3e99-9f5d-972e0fb3a274 | 1.76415 | -55.52922 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f346723-eb6f-3beb-95eb-5d350c55afc0 | 1.67099 | -55.61961 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fdf6595f-1a87-363f-b2f9-a7a49697f2cd | 2.01357 | -61.09497 | 2026-10-10 05:46:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3599c36-0a9f-31a5-8f3f-2b571de82cf6 | 3.03768 | -60.55486 | 2026-10-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d140e1b8-3ae8-3b14-9a14-b8093e1f8652 | 0.79966 | -59.4358 | 2026-10-10 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71c45bf5-6411-32a9-ac7f-6b5d7992b1e6 | 1.6704 | -55.61602 | 2026-10-10 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97f1d2c9-115d-3d0a-82b8-51e660f32996 | 3.04229 | -60.53426 | 2026-10-10 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db52c2d5-0729-33a3-8cb3-eded7158f90f | -5.22217 | -60.04854 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 55e5cb2d-1999-3c8c-935c-fa4d9067c7ec | -3.65188 | -59.17039 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da5349e6-58dc-37b7-939c-eb6daef4102c | -1.11249 | -54.15691 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78ce3906-0018-3693-a6d5-958913b282c4 | -2.85109 | -59.12313 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 177c39db-1a9f-313e-aaf2-ea0009c623b6 | -3.51931 | -59.94443 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23e52430-6cc7-31b0-8096-ba7f2c9438c8 | -4.34725 | -59.95433 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4168ec10-d893-357b-90dc-4abb81dd6a3a | -5.0712 | -60.2219 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef972c15-b979-3c45-aed9-7f65a731bbd7 | -3.59987 | -54.60147 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 689d8441-021f-368a-a368-317cd260c530 | -3.84488 | -55.7906 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c4768f2a-4ad5-3623-adca-c5c69cda8662 | -0.9876 | -52.44714 | 2026-10-10 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d3ccd1ed-246f-3958-b486-f0856991f687 | -1.8793 | -56.30965 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b809f7c8-06e8-31ec-922a-520c248bc188 | -3.60205 | -54.58572 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1937cfa5-5342-3d11-adf2-d188332b6f8a | -1.11091 | -54.16708 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 030a7c5e-6f7b-30ad-9b04-89f8dffc91b4 | -3.98596 | -59.35775 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2b8fbc3b-a231-312e-9820-818e1b60ada5 | -4.73498 | -55.66883 | 2026-10-10 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1199540b-24cf-3b16-b187-7024005aef56 | -3.32337 | -59.83863 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25f56273-db80-3062-ae10-5ac2dca60db2 | -6.09099 | -53.49885 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9d4c82d-ac3a-3f6c-a608-5bf637ba67fc | -5.21764 | -60.04788 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7cc187f5-b70c-3cb2-bb04-4245dc3eecaa | -1.51394 | -54.52065 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e4cf96c-5a0e-37d7-9a91-3ac0bfdce3c9 | -1.10684 | -54.17406 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cb4c0a4-4b34-3b7c-86ad-e082d979a666 | -3.103 | -53.93964 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 78f7d633-0128-33f6-b05e-e187e2d94820 | -2.61324 | -59.98291 | 2026-10-10 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 313a8287-ffc0-342e-aec1-e5b8aee6b5bc | 0.31595 | -60.44114 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b9b57ae-46d5-37bc-88c7-dbfb29d68a1c | -1.28248 | -55.74784 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4870e4ef-b677-3926-8bf3-08a6013beed3 | -2.05846 | -61.14101 | 2026-10-10 05:48:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 654a87f0-8681-3b9f-a880-d8006296cdd4 | -2.99535 | -53.89358 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2e49476f-b08b-396f-954c-0a7ce7c9dc25 | -2.54754 | -58.03256 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc0be18c-4002-3dca-acbb-5f15f0e89452 | -1.65092 | -55.2015 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 735355e5-24c3-3e97-bedc-f95da5b7becb | -3.89987 | -55.81578 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20cf483a-9f18-31f0-815d-9dc6bf8c94bf | -1.1076 | -54.16895 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1af5d63e-bac1-39d6-b086-b82cc464e0fd | -2.43692 | -55.9871 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8bcc6fc2-bd70-331c-86a2-d06533e218f0 | -5.3688 | -60.10028 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f9653df-7a4e-3064-b7ec-78360ee7d632 | -1.88678 | -54.67018 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| da6adfd2-7441-36b8-b39a-7306985997f9 | -3.026 | -57.78392 | 2026-10-10 05:48:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 657b44ef-18d7-30d4-9b19-09079c042398 | 0.14284 | -60.40185 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d75a19b-54fb-3537-87fe-bcf2bd52db42 | -3.30468 | -54.00637 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c717ef2c-daf3-30b4-a327-cf6433ad8b85 | -1.64432 | -54.40288 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ba175e66-0679-3372-851e-c17da4381b96 | -2.72833 | -57.47408 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 653abb46-db9c-3676-87a4-2af5547058a0 | -3.49801 | -54.61517 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8eb8670c-6ff9-3619-b00b-3426c43beaa9 | -6.4646 | -55.48692 | 2026-10-10 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a68f4543-fd56-3ff3-8aac-d018a843b544 | -2.39348 | -57.89481 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d04a4e8-1841-3806-8eac-7183b0218601 | -1.89019 | -54.69026 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README138.md)
