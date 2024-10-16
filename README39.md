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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 712a83d9-5aa2-3d58-b1bb-25b48cee6e7a | -17.77929 | -42.81039 | 2024-10-16 04:10:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fc80018-41b5-36e8-a7f2-f37326270b40 | -17.74517 | -43.91178 | 2024-10-16 04:10:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dd8fe24-901b-37e5-bdea-75517491d547 | -17.74242 | -43.90759 | 2024-10-16 04:10:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1adbf27-5e89-3e29-aaa5-6af0407c4a86 | -17.74185 | -43.91121 | 2024-10-16 04:10:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2bf5398-460f-32b3-aebe-0951b5132c03 | -17.73852 | -43.91064 | 2024-10-16 04:10:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01689a5a-93aa-30ea-b5cd-c0fcfaa30e45 | -18.26854 | -43.78685 | 2024-10-16 04:10:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3f52c37-770d-3da8-b65c-5b784cbcf87b | -17.00949 | -49.78025 | 2024-10-16 04:10:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7cdecf5-8f30-331e-aa60-72fd996dd565 | -21.14891 | -53.62768 | 2024-10-16 04:10:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39a18589-a5d8-3a7a-9a46-5e6f3540a9a9 | -21.14759 | -53.63385 | 2024-10-16 04:10:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 52ba7da2-097e-3a70-b42c-e080a17a42aa | -20.99792 | -55.24033 | 2024-10-16 04:10:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8ab104e-a97c-371f-8194-3ac039ae9e09 | -20.99666 | -55.23845 | 2024-10-16 04:10:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47056d96-c8ee-3a5a-8e89-e2cd710b11c8 | -18.0881 | -41.43524 | 2024-10-16 04:10:00 | NPP-375D | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82b276c8-ef6f-34b8-8a0c-09a7032f023a | -18.08457 | -41.4347 | 2024-10-16 04:10:00 | NPP-375D | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 669ec689-e3b7-3adb-88de-dbf2b34b1acc | -22.3065 | -41.87996 | 2024-10-16 04:10:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 21cd029c-0d43-34b0-93d2-188052054ee3 | -20.85781 | -49.87128 | 2024-10-16 04:10:00 | NPP-375D | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4e514768-962a-3e45-95f9-17932bced90d | -19.31815 | -39.89143 | 2024-10-16 04:10:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c7d8455b-dd5c-3a64-9ff6-eb5452a8e12b | -20.71806 | -49.45265 | 2024-10-16 04:10:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9633da88-5099-31ac-b584-c1ecc5d79cf6 | -18.27209 | -51.74846 | 2024-10-16 04:10:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22e3d3ab-45cb-3322-bf09-8845e66ae821 | -17.55787 | -52.67002 | 2024-10-16 04:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a04e1690-4730-3f0f-81c5-45af4d178574 | -17.55285 | -52.66899 | 2024-10-16 04:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c817688f-c77e-3ea3-ad23-da4ec373d3aa | -19.3144 | -39.97822 | 2024-10-16 04:10:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7d7b17b-1b93-3717-85bc-4506682e9347 | -19.22227 | -40.14156 | 2024-10-16 04:10:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d23189bc-99e9-3f22-be11-86419257837b | -19.13767 | -40.40247 | 2024-10-16 04:10:00 | NPP-375D | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1573f481-a061-3329-9a82-6747615874e5 | -19.90938 | -41.29279 | 2024-10-16 04:10:00 | NPP-375D | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b4cb057e-33be-39d9-bacf-e2cd2f23caec | -19.90917 | -41.28952 | 2024-10-16 04:10:00 | NPP-375D | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d6fd7158-c707-3db0-b4d7-a47f4da621f1 | -19.90856 | -41.29388 | 2024-10-16 04:10:00 | NPP-375D | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 99791b72-e920-35ff-abb7-bbea8654a3c5 | -19.71679 | -40.35266 | 2024-10-16 04:10:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5cf214b9-03a6-3677-b55b-5aa90dd5e284 | -22.30597 | -41.88219 | 2024-10-16 04:10:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5e55e053-5626-31dd-b265-f2955fc9e40a | -21.27627 | -42.1072 | 2024-10-16 04:10:00 | NPP-375D | LAJE DO MURIAÉ | RIO DE JANEIRO | Brasil | 3302304 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3e40221e-03b9-3bef-b8d8-e293f0157c3a | -21.27274 | -42.10659 | 2024-10-16 04:10:00 | NPP-375D | LAJE DO MURIAÉ | RIO DE JANEIRO | Brasil | 3302304 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 155ee403-cb12-30f3-b9b1-5a3eba192d60 | -17.67808 | -42.74082 | 2024-10-16 04:10:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fa2cc18-d93c-3c4e-87c0-25263d8edda0 | -17.55603 | -42.3212 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18322a91-264b-3ebd-a0c7-bd4fba9f6482 | -17.30114 | -42.65026 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0d778040-7c97-38af-969e-e2c7b2ebb388 | -17.29776 | -42.6497 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 06330756-4640-3b5e-a76c-ce22bf586b89 | -17.29439 | -42.64915 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0b4436b1-2e5f-3a0d-b3f0-07692925c2e5 | -17.27698 | -42.65005 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9fd8aaaa-19ff-3f33-b3d1-db5d9b36f1eb | -17.27361 | -42.64948 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 59fc263c-0546-3837-b819-38bd59fccd9c | -17.27305 | -42.65324 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96a0a836-1f06-3dc5-ba6a-535a8114c0b0 | -17.25508 | -42.65788 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ceae368-6edd-3051-880d-e9ae3ed6c219 | -17.25171 | -42.65731 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cfad81ea-5c21-3c52-8f50-83dc1b2d35dd | -17.25115 | -42.66107 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8b4e2185-cd80-3451-a643-c7a2b8d126f2 | -17.24834 | -42.65675 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d83fefdb-3ad2-3cfa-8fe1-c81f767c701b | -17.24778 | -42.66051 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8e0059aa-d209-3741-868e-661b8a3c9433 | -17.24441 | -42.65995 | 2024-10-16 04:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 098012bc-90e1-33ea-8bad-71a418f2bd8e | -17.03253 | -42.74784 | 2024-10-16 04:10:00 | NPP-375D | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e4f47e2-c024-317c-89f2-fff0ea407d32 | -18.02947 | -42.4169 | 2024-10-16 04:10:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f6e51479-27d5-3a76-84cd-ce8857978f60 | -17.80711 | -42.20257 | 2024-10-16 04:10:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4a339d4f-b363-319b-9d76-790e0f10be9d | -17.78698 | -42.05323 | 2024-10-16 04:10:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7b396079-2e30-3f2b-9035-c53afa16f239 | -17.27335 | -41.95158 | 2024-10-16 04:10:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20664453-8209-306c-8fbf-1e4cf3402429 | -16.6695 | -42.0785 | 2024-10-16 04:10:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 963e5401-0289-3830-8272-4883426b7f9b | -19.37862 | -42.40634 | 2024-10-16 04:10:00 | NPP-375D | IPABA | MINAS GERAIS | Brasil | 3131158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1c2239e3-a435-3296-a5c9-3b198c90d36a | -19.15195 | -42.66988 | 2024-10-16 04:10:00 | NPP-375D | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c748641c-b47a-3d46-916f-5c80eaedee0b | -19.14854 | -42.66928 | 2024-10-16 04:10:00 | NPP-375D | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 68fc1f1a-e89c-3d6a-ae38-c6b11f508cde | -18.54591 | -42.6456 | 2024-10-16 04:10:00 | NPP-375D | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d351285a-4ec9-39a5-84e8-94b180624b11 | -18.32163 | -41.75972 | 2024-10-16 04:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2c3162b8-5928-3c53-a462-da230dfea08b | -18.31814 | -41.75917 | 2024-10-16 04:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f906b7d-0306-3822-9f15-6e1803b06c07 | -18.29485 | -41.74726 | 2024-10-16 04:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d9a94dde-e964-38dc-98fb-8cd6021d51d3 | -18.29251 | -41.73873 | 2024-10-16 04:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b54ddabc-3ee5-333b-8b7a-d0d040fb25a7 | -18.29193 | -41.74273 | 2024-10-16 04:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9a2ac65f-50d0-360c-860b-520924ec9389 | -18.28901 | -41.7382 | 2024-10-16 04:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a0f5bbb4-8015-3096-9fa4-5563e35149c1 | -18.28311 | -42.7944 | 2024-10-16 04:10:00 | NPP-375D | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 09b3a215-bbb8-3cca-a188-2314e2e7a352 | -18.28254 | -42.79816 | 2024-10-16 04:10:00 | NPP-375D | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1005d3b9-8e9c-3e11-85dd-11fdab721c0b | -18.27586 | -42.93886 | 2024-10-16 04:10:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a70aa45f-147a-360d-873c-5de810bf5ed2 | -18.23148 | -42.44051 | 2024-10-16 04:10:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5ec176e2-4114-3dd1-b320-b51ea466b0cc | -18.22025 | -42.11348 | 2024-10-16 04:10:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3feb46f7-2bf7-3a36-a6cb-95b36275c465 | -20.67955 | -42.33443 | 2024-10-16 04:10:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c01eeca4-3148-347e-8ea0-324db3f463e2 | -22.85542 | -43.50129 | 2024-10-16 04:10:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 25f55fa1-d989-34e1-9077-ba00a325215a | -22.74664 | -43.273 | 2024-10-16 04:10:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8052a241-0d3c-39c0-bdca-582c5c69b9a4 | -22.46469 | -44.0478 | 2024-10-16 04:10:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d0553501-0f97-39c0-ac42-cba138fdc748 | -20.65453 | -45.15543 | 2024-10-16 04:10:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5a2aae21-9265-344b-9632-26f39dcd2404 | -20.49329 | -44.03891 | 2024-10-16 04:10:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a274582b-9adb-3829-bfaf-1e4e119e2a1b | -21.4817 | -45.32759 | 2024-10-16 04:10:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9fe95267-af0e-3246-b757-ac38e93c62b3 | -21.39927 | -43.92531 | 2024-10-16 04:10:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6bfcfb48-77f3-3337-9c6f-69860fa13e9d | -21.31801 | -44.56713 | 2024-10-16 04:10:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fbb2671e-5fa4-3c81-a7ab-711c9770f468 | -21.19644 | -44.93869 | 2024-10-16 04:10:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d9b68a8-0dba-3e53-8c6d-fd4c0b3b4585 | -21.17846 | -43.98143 | 2024-10-16 04:10:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0ef9e565-df46-327e-b106-62511165ca85 | -22.31112 | -45.39547 | 2024-10-16 04:10:00 | NPP-375D | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a13d3b48-6821-3109-a204-a55bb9df5d9d | -22.93544 | -45.51105 | 2024-10-16 04:10:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 22f01df4-6c85-369b-98c1-3df4f19d6328 | -22.72894 | -45.51242 | 2024-10-16 04:10:00 | NPP-375D | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ff3b0f00-403b-3e24-8c6a-73cd5d0f4e3a | -16.27772 | -44.81238 | 2024-10-16 04:10:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca9476b3-7ce7-39d9-8b5e-521077d11fe7 | -16.27712 | -44.81605 | 2024-10-16 04:10:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 700f70b0-e13d-33c0-aa9b-2714e68de96b | -20.47948 | -45.29583 | 2024-10-16 04:10:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6228e896-2d8b-3d5b-a1f1-c80ce3eaebf4 | -21.67517 | -45.89801 | 2024-10-16 04:10:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1803c2c5-8b07-3da0-a8f8-8fd681f2d468 | -23.53554 | -46.00728 | 2024-10-16 04:10:00 | NPP-375D | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 10e940b5-d706-3057-aff3-ddf66e7ea6f7 | -23.40641 | -46.55647 | 2024-10-16 04:10:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fee78398-36ca-3205-9475-65cc3aea2323 | -23.33971 | -46.77077 | 2024-10-16 04:10:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2f4437c7-302e-328a-a3e9-02f403aff1dd | -23.33907 | -46.77463 | 2024-10-16 04:10:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 87e136c0-36cc-3bbd-ac56-cdc18c5ca78d | -22.70305 | -46.47693 | 2024-10-16 04:10:00 | NPP-375D | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bf61dd27-e1ae-3737-88b1-b203319246c1 | -22.61614 | -46.30678 | 2024-10-16 04:10:00 | NPP-375D | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b1b20ff5-717b-3432-bd83-c1057bda9843 | -22.61279 | -46.30614 | 2024-10-16 04:10:00 | NPP-375D | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef597e9f-df67-3419-b96b-4b6b8aef8128 | -22.61193 | -46.30275 | 2024-10-16 04:10:00 | NPP-375D | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 07fe0e23-fc93-36ed-a2c0-229e26c0114f | -22.61131 | -46.30658 | 2024-10-16 04:10:00 | NPP-375D | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fbae6d92-3a8f-3382-822f-493ef9149aaf | -18.26984 | -56.57404 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fbca77cf-72ef-3cac-8ac6-d4e3c1d5f46b | -18.26865 | -56.5793 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7ee89cdd-7797-3071-a7fb-6d6907daab0a | -20.85679 | -49.87675 | 2024-10-16 04:10:00 | NPP-375D | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| cc274d94-6387-3d49-9312-ba84bc9f16c4 | -20.85385 | -49.87043 | 2024-10-16 04:10:00 | NPP-375D | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d5fd9f27-a138-33be-8758-190c62b31cb6 | -18.26746 | -56.58455 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 65445d8b-f1b0-3cbf-a8ce-939386db65db | -20.85282 | -49.87592 | 2024-10-16 04:10:00 | NPP-375D | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2495b295-b360-3c06-88f3-a5c728f844f4 | -20.41836 | -50.74302 | 2024-10-16 04:10:00 | NPP-375D | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2cba8e25-d2bf-32c3-8141-9c538d2fc38b | -18.26628 | -56.58982 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |


[Clique aqui para ver as próximas entradas](README40.md)
