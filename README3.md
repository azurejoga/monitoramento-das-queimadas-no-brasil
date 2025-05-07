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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d8e75ba-8b3a-3f62-82aa-b29fc88e40c6 | -11.19364 | -44.51324 | 2025-05-07 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 430bdd8b-92f3-307c-9a49-b553e0d6b0fc | -16.04755 | -43.81158 | 2025-05-07 03:38:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 364656eb-76d1-32bb-bc19-d2c29d2357c2 | -11.7767 | -48.70482 | 2025-05-07 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 966d29b5-9590-31ca-a611-166b33d0e6ad | -15.83127 | -46.57666 | 2025-05-07 03:38:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 889c650a-5ca9-3b32-b807-636bafba59b7 | -17.34693 | -43.85601 | 2025-05-07 03:38:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d38bb9d8-8fd6-3335-920e-bd98279b822f | -11.77524 | -48.71167 | 2025-05-07 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48c21dc8-628d-3c56-9e21-0d02b6e1576c | -11.19412 | -44.51146 | 2025-05-07 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b219055a-52d7-3665-82b1-a040644ec76e | -11.7832 | -47.35543 | 2025-05-07 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d06abfad-89f0-3ab0-b652-9bc25d7c87ad | -14.64828 | -45.91121 | 2025-05-07 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6febc801-062f-3824-9e3e-bf011f9db4c7 | -12.44207 | -38.1603 | 2025-05-07 03:38:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 17ec770d-26e8-3a0e-b9be-d3c83a4ab46a | -14.7262 | -42.87851 | 2025-05-07 03:38:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 26d9e22f-08ba-39bd-8adf-a247c63bf51d | -11.79915 | -44.27446 | 2025-05-07 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c317bcb8-d777-3498-9653-fb709cde7e29 | -18.00394 | -44.39246 | 2025-05-07 03:38:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc6c2bb4-5684-3056-b850-272e67b50d82 | -14.10289 | -44.13124 | 2025-05-07 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e26d57bc-dd13-3aff-8b53-085628b1d014 | -14.64747 | -45.91519 | 2025-05-07 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c97f294-dafe-3070-b9d7-8bdd21d01cd7 | -11.77773 | -48.70878 | 2025-05-07 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bd9d88b0-7a87-3b2c-b837-b88398cf80d7 | -12.444 | -38.16213 | 2025-05-07 03:38:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f2b0394-26db-3037-928b-393dedca4413 | -16.04485 | -43.79985 | 2025-05-07 03:38:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9496f982-a135-3299-92d7-0c3ea6441db1 | -11.19437 | -44.50954 | 2025-05-07 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d481e9d-9ccf-3fc7-aab1-53cf521f0837 | -11.41152 | -48.71251 | 2025-05-07 03:38:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2437db1b-3aff-366b-8f7b-795e9b8d2a10 | -16.04379 | -43.80523 | 2025-05-07 03:38:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d89d81f1-f9e2-3340-a8c4-0b815691308e | -17.86976 | -44.56841 | 2025-05-07 03:38:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76e7d7e5-d8b8-37eb-8be9-ecdbe06b17bc | -17.36552 | -42.51553 | 2025-05-07 03:38:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab744fae-e72e-325a-9a55-3dfe521ed517 | -11.77074 | -48.70732 | 2025-05-07 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4507b987-d387-311c-abd1-2b8bba54c699 | -14.1035 | -44.12814 | 2025-05-07 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a5a09e27-4f7e-39e6-b15c-9471fcb1ac8f | -15.79271 | -41.28024 | 2025-05-07 03:38:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f2b9746-6624-3b06-82a6-bc9044524555 | -11.79872 | -47.3777 | 2025-05-07 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9cde5d50-a00d-382a-8fac-f5ea35ddef7f | -16.04275 | -43.81055 | 2025-05-07 03:38:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5095ae50-9e94-3ab1-a460-0945beefed1f | -23.60596 | -49.00053 | 2025-05-07 03:40:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7057b919-77a1-30f6-bb1d-8563cf25c766 | -20.05802 | -49.37422 | 2025-05-07 03:40:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ee3c490d-888a-315e-aa83-12c59a1fbe0d | -23.61167 | -49.00193 | 2025-05-07 03:40:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3b342ec-14db-3623-8145-14503dc7a5d2 | -23.60772 | -49.01471 | 2025-05-07 03:40:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5fc31ed7-7cff-3f09-bb5c-4698c2e9553c | -22.39797 | -42.91379 | 2025-05-07 03:40:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 25200ba2-b1ed-3a1a-91fd-1ceaeb28ab25 | -23.60514 | -48.99976 | 2025-05-07 03:40:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f931e4f-3e71-3a46-ba6a-78349cd5958f | -23.60982 | -49.00562 | 2025-05-07 03:40:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3df58963-b684-3acb-8146-9bf775d56d36 | -20.05592 | -49.36965 | 2025-05-07 03:40:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7b7b8cdd-9f7e-3f36-bd50-0944676f8b2b | -22.81004 | -47.13365 | 2025-05-07 03:40:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dbecefea-1a38-3bcf-86d2-50494fd1f94b | -23.3371 | -46.77345 | 2025-05-07 03:40:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5c947670-0079-3b1b-b80e-ef262b35f90c | -21.38638 | -48.63849 | 2025-05-07 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c0d9782-7b42-30c9-995b-e63cadc66b8a | -20.05926 | -49.36879 | 2025-05-07 03:40:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dfe961c5-21cd-39c4-b9e2-685a78ef4f4e | -22.81078 | -47.13025 | 2025-05-07 03:40:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f2158595-f77e-307a-850e-0bc56fbeddd9 | -23.61085 | -49.00119 | 2025-05-07 03:40:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fa62ecb-a87a-3e2b-9bea-d705f99aec88 | -19.53178 | -43.9205 | 2025-05-07 03:40:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f09a1650-c10c-3079-9b84-cf91429ffdcf | -6.94035 | -42.7901 | 2025-05-07 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f88f738-ae27-3c9e-9b90-b698779a27e5 | -6.49817 | -44.72983 | 2025-05-07 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31d2ac36-a23b-3f15-9c8f-42e5b2525551 | -5.16164 | -45.10671 | 2025-05-07 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f7a3c2ef-ac4c-3782-a414-97ee8f7d278f | -10.69531 | -37.05037 | 2025-05-07 04:02:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 538303f1-0bb8-32d8-84ec-942192d8e52c | -6.69653 | -42.13438 | 2025-05-07 04:02:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 4002d26d-c747-37cb-94e6-57468c6a1a41 | -5.93116 | -40.63004 | 2025-05-07 04:02:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7c55bcf9-99c2-3316-a180-aa88b0164c21 | -8.07861 | -43.13038 | 2025-05-07 04:02:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a6080e5e-7fa3-30db-968b-50f43a230e19 | -6.55172 | -44.48633 | 2025-05-07 04:02:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da19013a-eb8c-39d9-b2af-cf82e31de3c4 | -6.94389 | -42.7907 | 2025-05-07 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95708026-b647-32a0-876f-5421cbd4890a | -6.71142 | -47.59138 | 2025-05-07 04:02:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60deba52-618d-3465-a549-3d0a1d0b8520 | -6.93195 | -42.79681 | 2025-05-07 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d8c33032-07f1-3b1d-ba05-2cf928536570 | -6.69999 | -42.13495 | 2025-05-07 04:02:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 089c823f-4ec2-3d5e-ae36-8bc60366d9fd | -5.64061 | -44.30642 | 2025-05-07 04:02:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fa1c305-56cc-3962-ac88-cf286d8efb06 | -6.55562 | -44.48701 | 2025-05-07 04:02:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c3f1cf8-b839-3e83-aacd-c589457c912c | -6.83544 | -42.79041 | 2025-05-07 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d7e9d939-0e8e-385b-888a-864b2594d225 | -9.61163 | -37.0406 | 2025-05-07 04:02:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 500a6a96-b194-3200-bfc1-9ce4ca7e7755 | -6.20709 | -42.17535 | 2025-05-07 04:02:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6fad0c8-2f9b-3732-8507-2ff8fe928040 | -8.07284 | -43.12112 | 2025-05-07 04:02:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c97523d5-33f8-37e2-891f-e2b6b2e3ae3f | -6.7006 | -42.13116 | 2025-05-07 04:02:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f73f6792-16f8-357d-a0ec-3da5615785eb | -9.61098 | -37.04505 | 2025-05-07 04:02:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bdf2b264-041c-3fa3-bab8-cbb39f6954ba | -5.56404 | -43.48442 | 2025-05-07 04:02:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7592d66a-5c30-326c-82e7-05fa657513eb | -6.93549 | -42.79743 | 2025-05-07 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5493bddf-85c6-3fb5-9d29-52f3d16e440d | -6.74578 | -44.52623 | 2025-05-07 04:02:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab9bd9c6-5b4d-3d8d-83ca-708251bcc3cc | -6.69307 | -42.13382 | 2025-05-07 04:02:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 964fd03d-bb98-33be-908c-58c84de45f16 | -6.92908 | -42.79732 | 2025-05-07 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da6b2d59-8e08-3924-acfb-ae4bf9bc3a28 | -6.93969 | -42.79407 | 2025-05-07 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 730f0426-bdb0-3c23-b653-2753fc9b3262 | -8.08217 | -43.13097 | 2025-05-07 04:02:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c6b4a0b8-b3fe-3685-ae15-648e21c354b9 | -5.46561 | -42.92276 | 2025-05-07 04:02:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d55feeed-a908-3897-8341-fbeccf131a40 | -5.46198 | -42.92218 | 2025-05-07 04:02:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 645f9959-d488-3291-91bb-fe6046a5bbbb | -4.82375 | -47.63132 | 2025-05-07 04:02:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2465c91a-7f42-3c42-a30d-2c65eecd488a | -8.07907 | -43.10566 | 2025-05-07 04:02:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0d69c974-aac8-30c1-a6d2-83f9747bb3fc | -8.06929 | -43.12053 | 2025-05-07 04:02:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 761dd355-1fd1-3f4c-b5a4-26068f3c38c8 | -6.55088 | -44.49125 | 2025-05-07 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93340823-4a80-3b42-97f9-b361f1caada7 | -9.06515 | -38.45683 | 2025-05-07 04:02:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 56bd980e-fcd8-31fd-aa33-77f7213ad743 | -9.21674 | -36.87254 | 2025-05-07 04:02:00 | NPP-375D | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 32fb6075-e835-3e83-ba0e-fa6028bbf968 | -4.89593 | -37.5277 | 2025-05-07 04:02:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53cb872b-051e-3528-8a24-b1bac18f44db | -1.55029 | -47.80782 | 2025-05-07 04:02:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 274c4a15-39ef-316e-afac-71e9ded3a152 | -5.84404 | -42.58881 | 2025-05-07 04:02:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 315b751d-c041-33fe-858a-a9a589927829 | -6.83478 | -42.79441 | 2025-05-07 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f9e1ce8f-50f8-3798-b894-cbdf02b17d58 | -5.16101 | -45.11045 | 2025-05-07 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5398efdf-e00b-3c1e-b4d3-c0dd3541f3cc | -5.79349 | -43.61536 | 2025-05-07 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5c3960f-560f-3ed0-976f-22d19a873058 | -6.49674 | -44.72721 | 2025-05-07 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2aea364-d192-3346-bb81-26f56218aa16 | -6.55478 | -44.49196 | 2025-05-07 04:02:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 264412cf-8416-36aa-934c-8881df7fdaf4 | -6.93615 | -42.79346 | 2025-05-07 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 57825a19-2a0f-358c-b785-a6c2a3829cb0 | -4.82334 | -47.62988 | 2025-05-07 04:02:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c44af33f-a4f0-3f20-9ec0-c874573572d8 | -6.49504 | -44.72421 | 2025-05-07 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3f80396-75a2-3abb-b1d0-0d3a81dcaeaa | -8.07928 | -43.12634 | 2025-05-07 04:02:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 54c6f616-9cf0-3a9a-827d-1caaf4553a64 | -1.55081 | -47.80456 | 2025-05-07 04:02:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d51c705-64d6-321c-9dca-af7fa7d93b13 | -8.23866 | -49.73909 | 2025-05-07 04:02:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b4337f0-8957-3a7c-891f-97b28df16948 | -5.79276 | -43.61981 | 2025-05-07 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdcb91f9-bc89-3555-9181-bf5dd30d799d | -8.23803 | -49.74248 | 2025-05-07 04:02:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe9e029a-51ae-31f8-8853-33f5a31aaa3a | -4.69361 | -43.25732 | 2025-05-07 04:02:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91f0128f-5b50-3620-8aac-32c305357885 | -5.8476 | -42.58942 | 2025-05-07 04:02:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f507a6f-1c40-38b3-bf91-4c421b64f891 | -11.79749 | -44.27635 | 2025-05-07 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1486ab14-473f-3fa0-b9b7-0d3e21ab8cb5 | -16.04692 | -43.8104 | 2025-05-07 04:04:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce8ba394-3df1-31dc-8f68-3c488b4c23ab | -13.49967 | -52.96156 | 2025-05-07 04:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a940aafc-318f-31db-8a04-398972eb9411 | -10.98094 | -44.4398 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README4.md)
