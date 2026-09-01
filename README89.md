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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4710fa6-173a-3cba-bd47-47aac6c11ca2 | -8.77807 | -69.33976 | 2026-09-01 06:59:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18f703b9-d838-3742-9ec6-2acba3c08f63 | -14.4011 | -52.5014 | 2026-09-01 07:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7de61fb3-6483-3cda-82b0-c5f89bb1e889 | -15.7741 | -56.0842 | 2026-09-01 07:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| ffbb2585-f68d-3e36-a3e5-e59dfa4e1fc6 | -16.0352 | -54.3933 | 2026-09-01 07:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1f167b28-6aff-3475-bf26-deb80d20a7b7 | -7.5894 | -60.4827 | 2026-09-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c7e04c3a-75b1-37a0-bb5e-53a75374344d | -7.571 | -60.4643 | 2026-09-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| e7fb1bfd-d921-3ca7-9667-0e1a9745059d | -7.5895 | -60.4636 | 2026-09-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4933a073-1dfa-3e10-a896-bcb464406641 | -16.0547 | -54.3908 | 2026-09-01 07:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ca180dba-e23b-364e-8c21-14f28b1c094f | -7.5709 | -60.4835 | 2026-09-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 2215ee05-f97b-3fa6-b8af-cb788160a72b | -14.4011 | -52.5014 | 2026-09-01 07:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 30a01144-8297-3e4b-9774-ba847ed67a7d | -7.571 | -60.4643 | 2026-09-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| dd63ab12-34e3-3fe3-904f-1fcb756c5ebf | -15.4429 | -52.681 | 2026-09-01 07:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 65c005bd-0af9-3333-904a-39e1e5b252c4 | -14.4011 | -52.5014 | 2026-09-01 07:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d7565f1e-ff98-38be-80bd-3f88a41a2b3c | -4.95966 | -55.85628 | 2026-09-01 07:26:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e9f456f7-fc07-399b-bf0c-51944f5d2488 | -6.12851 | -55.63811 | 2026-09-01 07:26:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 928a1512-877b-3c8f-b978-1cee5ee27258 | -3.20166 | -61.13411 | 2026-09-01 07:26:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0d4a7e86-1715-3468-badc-d1454fc16d9d | -4.96258 | -55.83636 | 2026-09-01 07:26:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 52350529-a7c8-3193-aaa7-b929aa775ae7 | -4.97045 | -55.84762 | 2026-09-01 07:26:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a40c17d4-3702-3744-aa8d-7eb8315b5784 | -3.61948 | -60.55239 | 2026-09-01 07:26:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e7aafd35-f796-3159-bb91-13f82408edb7 | -5.2478 | -55.90665 | 2026-09-01 07:26:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 743caa6d-8195-3bff-8c33-09b5cafd843b | -1.47345 | -54.2313 | 2026-09-01 07:26:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 45b07077-cfe4-3c6d-a104-fd11e460b20c | -4.96112 | -55.84632 | 2026-09-01 07:26:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6aa38cfc-0009-3cfe-a940-0b0d5182e92d | -5.24928 | -55.89663 | 2026-09-01 07:26:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7aa29ec2-c2b9-36e3-b846-776c639540fa | -5.48092 | -57.14546 | 2026-09-01 07:26:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a00872e1-51eb-3251-9861-e20cf63db1ab | -3.61783 | -60.56307 | 2026-09-01 07:26:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5e7e55a8-ad65-396c-b8da-9094b6e4b614 | -5.49114 | -57.13776 | 2026-09-01 07:26:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1ad038af-d34c-3351-92bf-2e7a99740dc7 | -5.85299 | -57.55329 | 2026-09-01 07:26:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 807ca126-c18a-34c4-88c6-492a70eefbf7 | -3.11491 | -61.22459 | 2026-09-01 07:26:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a7b5cc39-fcab-3bf6-92dc-fa92d28a4db4 | -6.25041 | -55.4323 | 2026-09-01 07:29:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eb1530eb-0ea8-30a0-9617-1477bbd6b8ad | -16.04374 | -54.37225 | 2026-09-01 07:29:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ac991a30-4876-34f0-87dc-87cc3b5d2ea1 | -9.15063 | -59.53098 | 2026-09-01 07:29:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f37a29d4-f6b5-3eef-9c0e-17f96ab1a191 | -6.15336 | -57.7759 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df0c6909-c0e7-3d0f-8001-b5a31d557207 | -7.29855 | -60.56093 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 26752075-a2c6-3ee4-aa94-c5fd76377902 | -14.40333 | -52.49517 | 2026-09-01 07:29:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| f2e1b6e0-3bd8-36d5-9c20-852f9be1b2ef | -6.80564 | -59.5687 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| df6f58db-d5aa-35ec-a2a7-37e600e9c84c | -7.57191 | -60.47253 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| d5f49f30-7f64-3675-af52-aeb41293b8d9 | -6.59477 | -58.58665 | 2026-09-01 07:29:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3967232b-5013-3c8c-bf46-8061574faadc | -15.77283 | -56.07113 | 2026-09-01 07:29:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 398f5983-3a04-30d9-b87a-ff0905f44acd | -7.34309 | -60.57777 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 1796bee7-f18e-3cfd-bac1-abae8f963160 | -7.57955 | -60.48357 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fc2dfd9c-25ca-3195-835f-4797fe44f590 | -7.59023 | -60.47519 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| cdedbb8f-a6a9-36c4-912a-eb8737000cb0 | -7.56578 | -60.45201 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 86794ca8-5fc5-3486-8f6f-71469e0f7e3c | -6.11915 | -57.6838 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 21bb297a-51d7-36e7-a67a-6918a8c424cc | -5.87487 | -57.77969 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b6ce39f-2588-3f71-b224-5eab18bf7720 | -6.81331 | -59.08821 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e35bb5ba-b308-37f0-ba80-1c03c8eda9d0 | -8.26852 | -54.94017 | 2026-09-01 07:29:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| eff8e3db-1a3e-3217-9945-8b31b8abba99 | -15.86532 | -56.47555 | 2026-09-01 07:29:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 08f2a770-4529-36cf-9ff5-7ad4e8ec8591 | -15.76033 | -56.08357 | 2026-09-01 07:29:00 | AQUA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| e60a505b-614b-399b-a4a4-554e28520056 | -7.19917 | -60.6697 | 2026-09-01 07:29:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3922612e-1b1e-3350-9128-bf83872fad6b | -6.59344 | -58.59541 | 2026-09-01 07:29:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 71dca43e-07c4-33ab-9f48-a029391be10c | -6.15998 | -57.73174 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 67f40d44-c641-339a-93f2-9650dd400b29 | -8.2704 | -54.92704 | 2026-09-01 07:29:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 22c89ad2-8e4f-3979-9dfc-d437d5cbd5f0 | -7.57343 | -60.46284 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1b74376a-52b0-3f1e-a4fc-52b5c8bb0f9c | -8.11977 | -54.96402 | 2026-09-01 07:29:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 86c6897a-f865-399c-a674-52ee754e0e94 | -10.41366 | -64.45521 | 2026-09-01 07:29:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4013867b-c93a-3ab6-9fae-67a09b879dac | -6.61096 | -58.59801 | 2026-09-01 07:29:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e3b8a0b-1cb6-338c-a955-8fe9f01b2620 | -6.60353 | -58.58795 | 2026-09-01 07:29:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ae408d5-029f-323a-a7dc-a9851158e206 | -15.76698 | -56.07896 | 2026-09-01 07:29:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 3b5ae8dd-7565-38e8-991a-d7df09bc1fd9 | -7.18681 | -60.68795 | 2026-09-01 07:29:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8206afc6-abb5-3955-9eba-d6626404dfd0 | -6.95694 | -55.64836 | 2026-09-01 07:29:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 69460782-9ad7-3860-986e-7bb057e7c143 | -14.39443 | -52.51398 | 2026-09-01 07:29:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 235bbef9-edcb-3119-9259-da9dfb905c1b | -5.86609 | -57.77839 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eb7e8e70-ec6a-3219-a057-d63869d19c4d | -6.81196 | -59.09705 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a03dfc6f-71c8-3312-904c-024d968d4842 | -6.81923 | -58.87253 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a6681689-d2e6-3b53-b693-0c6575652ae9 | -7.73622 | -55.21976 | 2026-09-01 07:29:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| bbec6ea3-f2bb-319e-ad30-5320732155af | -14.39751 | -52.48899 | 2026-09-01 07:29:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4beeae03-b767-3a88-b901-7be20bc4d09f | -6.12049 | -57.67495 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f88690f5-0a78-3aa7-99fb-5870572dbd88 | -6.15866 | -57.74059 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e9a22cae-33ce-3bd6-99a5-4859e3440eb8 | -6.94883 | -55.63615 | 2026-09-01 07:29:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2e7947e5-b311-3a20-81d9-598f81839737 | -9.14581 | -60.94269 | 2026-09-01 07:29:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| b09abce9-a4f3-318c-9e03-625461b741eb | -9.14927 | -59.53986 | 2026-09-01 07:29:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef197b95-c115-3711-a22d-6c193fc79cda | -6.6022 | -58.59671 | 2026-09-01 07:29:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b12fb0d1-b156-3bb3-adf2-d834f1ce46f7 | -15.63615 | -56.3714 | 2026-09-01 07:29:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2f5eb57b-2dc3-3b66-a6b5-6f909f108ed9 | -7.33388 | -60.57635 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 38bee76a-e7d8-3162-b5da-006fa64c01dc | -6.95853 | -55.63749 | 2026-09-01 07:29:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 517f3065-6070-30b7-8d28-d8c70311954a | -5.94353 | -57.68171 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4574ac8b-3728-3507-b395-efdf2d755136 | -6.80451 | -59.08688 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 8a62e3ba-813b-35bd-93db-300c720e7bb2 | -15.76508 | -56.09312 | 2026-09-01 07:29:00 | AQUA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| bd49a4bf-fa7d-30b4-a28a-7a309cb59989 | -6.79363 | -59.39495 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d4bb194f-57a2-34ca-a064-1f57192c4174 | -7.62395 | -55.29299 | 2026-09-01 07:29:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ef210f3e-d9f5-3fd0-bde0-43655c646902 | -7.56428 | -60.46155 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 82d5bcf6-a176-3e47-9acb-d4001311f7b4 | -5.9422 | -57.69052 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a884cdb6-5d05-318a-a81f-f8847719a0bd | -7.03506 | -59.22134 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b554c4e1-6892-3272-a469-bf7784d1c112 | -7.3523 | -60.57922 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 95574aff-e9ab-32a9-b3c8-cf50dc26224e | -8.25824 | -54.9381 | 2026-09-01 07:29:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c66ac3b7-800e-3401-be6d-c780ad9b1208 | -15.76926 | -56.0992 | 2026-09-01 07:29:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 70c05772-5e04-34bb-a1ac-5ba19f9218ca | -5.95585 | -57.68019 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 750e9357-a3c5-3cba-9102-3dc9118fa5b4 | -7.18835 | -60.67813 | 2026-09-01 07:29:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f1dc7627-f550-3bf9-9f4b-ff936469fcb9 | -7.58106 | -60.47392 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 2f513096-265b-3758-9f86-d150c375b407 | -7.58256 | -60.46432 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7ac1a707-2cf7-3b77-b758-2d33f9814b07 | -6.17891 | -57.72549 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de30f158-6894-3112-b054-4691d66ad842 | -15.77104 | -56.08518 | 2026-09-01 07:29:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| f40d5b5b-2089-3abd-bfc9-cbb8d6c7fc3a | -16.0414 | -54.39127 | 2026-09-01 07:29:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 04e0688e-c16c-3048-b957-b90b61c16bca | -9.14733 | -60.93291 | 2026-09-01 07:29:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5021de5b-9fc1-3b5f-8c46-9a7e664f68df | -14.38938 | -52.4932 | 2026-09-01 07:29:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3b556dec-e0e7-3350-981d-94ea565c0242 | -6.80316 | -59.09573 | 2026-09-01 07:29:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| f09b8ca0-2998-3adf-9463-d90ccffff7a7 | -10.94926 | -61.65492 | 2026-09-01 07:29:00 | AQUA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ca399458-532f-313e-a78c-fe2c82277db3 | -15.75858 | -56.09741 | 2026-09-01 07:29:00 | AQUA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 583442ea-6497-3460-9e0e-201908d20783 | -6.17758 | -57.73433 | 2026-09-01 07:29:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 739a3c17-d8b9-3cf7-bf07-aad2eeae8296 | -9.38824 | -60.57085 | 2026-09-01 07:29:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README90.md)
