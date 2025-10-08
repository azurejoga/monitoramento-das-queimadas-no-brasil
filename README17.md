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
| cfe5cde1-5717-3fb2-a745-56ce06de9ce2 | -4.08196 | -48.04397 | 2025-10-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25dcca6d-9000-3360-a5c0-8d4fd2a2a63e | -7.35828 | -43.86947 | 2025-10-08 03:47:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 978d2ae5-d441-3b2e-a5f2-791f318732c4 | -4.49668 | -46.36154 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 39fda314-9d2b-3b2c-be54-499ac1a2319e | -7.78938 | -42.62449 | 2025-10-08 03:47:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 02645a63-dfab-348b-9ea3-3542b0c1b415 | -6.9068 | -39.55101 | 2025-10-08 03:47:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cb672786-8a34-3fdc-a76c-8271a64c4f33 | -5.13719 | -44.96206 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5a35fd19-57e6-3074-86ca-1d803f5f2b49 | -6.42616 | -47.24574 | 2025-10-08 03:47:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d76fe7c-1a8f-3cde-adab-ad3fa3afee4b | -5.71094 | -45.6813 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f26034da-2088-3d8a-b558-3553a0af9013 | -7.4634 | -43.02838 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e52c7a23-ef3a-358b-8db9-0417b06ca878 | -4.50045 | -46.35963 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4e20c3f5-4d51-3cc2-8536-ab7d9cb0c33a | -4.2818 | -44.38244 | 2025-10-08 03:47:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b1e8494-6762-3a94-bf67-81a8bc370c7d | -7.02906 | -42.87837 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c8e1c3e4-c267-3617-8e5b-8176be42d373 | -3.58241 | -49.43587 | 2025-10-08 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a508e1da-7d82-3de9-9fca-214dfe914135 | -7.00839 | -42.87097 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 55ebde03-251f-36be-a646-ae10e1fc329b | -6.1418 | -42.67387 | 2025-10-08 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fd5ee60f-6895-343b-a971-6bca60024e3b | -7.03106 | -42.8664 | 2025-10-08 03:47:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| dc5c7b89-a277-3703-a80a-8351f0a6d928 | -5.71632 | -44.82629 | 2025-10-08 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c94066c0-6b0e-3886-8326-2a5fb4855d02 | -4.68669 | -45.83868 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2fbc166b-5091-3159-8ac5-f42c9c54c704 | -7.81891 | -44.17997 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 327fada2-f8cb-3942-be4b-2a5c97a5959d | -5.31879 | -45.25945 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85e1ca12-94ce-362b-8ca6-12bd5d1f5c58 | -7.00704 | -42.879 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 7c411607-003c-3579-8c86-25bd4d05f3f9 | -7.25545 | -44.11135 | 2025-10-08 03:47:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0675821a-6709-3173-b5da-0fb1644946ec | -4.50749 | -46.3525 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c649f447-9515-3ec3-bbdd-72bc8a6468df | -5.8637 | -44.30337 | 2025-10-08 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cc870411-5d67-33d9-bc1b-d398fabcc78b | -5.77093 | -45.74275 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb4fa26c-cb3a-3652-a0d6-8918872e7948 | -7.4428 | -43.14677 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ecc637ad-ee86-31b4-8abe-40304e597af1 | -4.84975 | -45.75713 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7c02639-356d-35ba-90cd-2bd48c479e57 | -7.01715 | -42.89712 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5d241c0a-6849-31c2-88da-a8c5b1f02fa8 | -7.02612 | -42.86971 | 2025-10-08 03:47:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 16ccea66-b8fe-3365-ade1-00fdf852cf65 | -6.14606 | -42.67463 | 2025-10-08 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1b1b1d6d-dc12-36db-9c80-e0140316aa81 | -4.68131 | -45.83753 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6e6ac821-5f35-3a33-abf9-a5d0e4b2fc0a | -7.01918 | -42.88503 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.5 |
| 7ccbf529-1ed1-3f7d-9dcb-258e342a57a6 | -7.8001 | -44.20591 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5a51f6ad-0742-3c39-893a-2b1014271aae | -4.50301 | -46.3583 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed14d627-d92b-34e9-9529-3d0f7ea111b9 | -7.65338 | -43.93892 | 2025-10-08 03:47:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3e4b395-0c99-3d05-b647-37031ce7df0d | -5.75406 | -44.60314 | 2025-10-08 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa33d6b9-68a9-3e70-a0f9-75583781da70 | -5.83511 | -44.97515 | 2025-10-08 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a85f42f-85c8-3006-b7a4-3216b6db9235 | -7.80032 | -44.20723 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a2797119-dc4b-3c62-af9c-0935ee6432ef | -7.81352 | -44.18366 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db1d0845-af8f-3eb7-a357-bfd1a66656b7 | -7.45842 | -43.0317 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| be553fc5-9776-3883-a9e1-36c2d7232645 | -4.87256 | -46.8284 | 2025-10-08 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4130557-7f62-39ec-bded-87f37e1d16de | -7.44328 | -43.13078 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 41496dfa-36f3-3f3f-bd0b-5e99cf32c5d6 | -7.02546 | -42.87371 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 4ff87c1c-87d5-3896-b32f-3047a9803da6 | -7.26 | -44.11253 | 2025-10-08 03:47:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b79a7f5-731c-3a3f-949f-5eea4906f5c8 | -7.03064 | -42.89515 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 147a4183-3be9-3c76-a3f7-2e247b7aac3b | -5.39413 | -45.20256 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2eb70317-78d5-37e7-8000-da51d83bb457 | -7.40963 | -45.17543 | 2025-10-08 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 69610aeb-f039-3aa8-a004-443d511c579d | -4.50366 | -46.35438 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 75fced7d-37f8-326a-bcf0-644299ccd99d | -5.16585 | -46.22599 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44251254-9691-31b3-a4fd-3dcabcd72fb0 | -7.35001 | -43.86338 | 2025-10-08 03:47:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f4f60ffa-a559-3f58-9048-17f9ce8fd9cb | -5.86932 | -44.29934 | 2025-10-08 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ae239b72-928b-3fbf-b1c1-0db4f222c7c8 | -7.43993 | -43.13781 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9cc0c17c-f2d4-305a-80a5-1fc44db86f05 | -5.82289 | -46.74306 | 2025-10-08 03:47:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da6ab21e-2b30-3f11-beba-0708559a183b | -5.60156 | -45.37692 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fab79969-ed2c-3e0f-bc32-c7ab53e34986 | -5.73482 | -45.26123 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49fb4f51-54ee-35b4-9b11-3c9b96818fbd | -4.68485 | -45.84962 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa828736-cd7f-3c50-8bc6-6efcb1e6f0b2 | -4.68673 | -45.85021 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9dbec5ea-408b-38ef-875c-1520aff63e83 | -7.01266 | -42.87165 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 49239571-2139-34ae-b4cd-44622d449ef4 | -4.50679 | -46.35651 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 261862b6-9e91-3078-83f9-8befa6fc99c2 | -8.85798 | -37.34603 | 2025-10-08 03:47:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7230322c-507a-3715-b905-146cea001c7e | -7.05374 | -37.69366 | 2025-10-08 03:47:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dae33f5e-7e25-37ed-8f9c-7eb25c07f268 | -4.49976 | -46.36356 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 14314f3d-875c-33cf-ba90-4accd0377739 | -5.83989 | -41.49952 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a65c393e-e04c-3940-8e39-a7737e212df3 | -7.16082 | -39.43761 | 2025-10-08 03:47:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 949cf9ae-445b-3867-855b-0e93bedd5f18 | -7.47926 | -43.06395 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| daa19dc0-abee-31dd-a5be-91dc57f47357 | -8.62168 | -45.1072 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ba6b043-f146-392c-8ae2-7858f030763e | -8.56671 | -46.2302 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e90bd93-7733-3bfc-ae9c-c1c1d3899c81 | -13.37076 | -47.55783 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f7646a9-7893-31fb-8f8c-2ca42986a92b | -9.18152 | -46.9181 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| ae386139-67a6-3313-9b71-ddb1ff0c0139 | -13.7305 | -45.71004 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63acd55d-a354-394c-8ebb-37cff961b26c | -11.72868 | -50.9552 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 355aeb7c-c323-3d20-80ca-318e5e5699bf | -13.28087 | -40.36202 | 2025-10-08 03:49:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 081a1be8-0f91-3e17-be49-e9fe0d4826cf | -9.08794 | -47.95954 | 2025-10-08 03:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5bfaae6-303a-370a-9278-32ee52f338bd | -11.71131 | -50.95055 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d2a1211c-feec-3dae-af4c-0a9ced2feaee | -9.19403 | -46.91073 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f4f3626-41c5-3a3a-9dcf-92602b33b1c6 | -13.35981 | -47.55846 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d3413d50-344c-39de-9b91-588c1ae0c9fa | -13.07357 | -48.01608 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb92451e-4b41-3228-a7c3-ea4ea684fca5 | -13.80155 | -45.80669 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64c8a59b-a69d-3410-9201-6d3b7b3e8a99 | -11.76892 | -45.13357 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0b97ed5-df2c-3ba7-ae34-332faa7fc6f4 | -13.28478 | -48.47736 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31af7f32-02ab-30ec-8450-b38b128d866d | -13.27313 | -48.04844 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 178d0c09-bf8f-39c0-b19d-470f813a6593 | -13.27203 | -48.04385 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d4fd379-05bc-3bd7-b8db-6e3da21ecabf | -13.07298 | -47.93499 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1e6d9a3-47b4-356c-9605-0dbafd0e0d82 | -3.10148 | -47.01086 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb820a3c-617e-3a25-af8a-1c2bc9fa2a57 | -13.2809 | -47.1532 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb6ffa99-b70f-369f-8c8a-f33024e1b58e | -11.793 | -45.05447 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dcfec6bd-62a6-37e8-a35e-7307692f9968 | -3.89108 | -41.53562 | 2025-10-08 03:49:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55fc95c3-a269-3f4a-beb8-5b5563b22b9a | -4.05029 | -39.05347 | 2025-10-08 03:49:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd0351da-ffe3-32b2-af72-abcd2255d15a | -9.75884 | -47.69073 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cd3ef56-ac20-36ae-ab76-bb541f962537 | -11.70501 | -46.35217 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cda5347-f6a2-348c-b651-1d2486554098 | -13.28772 | -48.48693 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d97b3944-df36-3da7-a170-a140df7d5179 | -8.68166 | -44.73222 | 2025-10-08 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 77ba85cc-a179-3171-a75a-3a43eaa3fb7e | -13.22491 | -47.18252 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1230c65c-8d78-38b2-9225-a4209fee60ff | -8.52778 | -46.23321 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fda3e40a-5b5c-3c60-b6a6-0531c5cdbf39 | -14.45411 | -48.79602 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d4c4c69-76b1-3657-90b0-30b387173ad8 | -12.94498 | -46.85552 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 58074be0-4df0-3c13-99b0-5700da5ab343 | -3.8999 | -44.90534 | 2025-10-08 03:49:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 32c63a7a-1727-3103-81ca-ee580db2da19 | -9.18216 | -46.91465 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 211a14cd-94a5-3385-9e84-bd4fd7087181 | -7.79833 | -46.01938 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2ab8c57-a44e-3f09-8c08-713ea9f48d76 | -8.48079 | -46.31536 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README18.md)
