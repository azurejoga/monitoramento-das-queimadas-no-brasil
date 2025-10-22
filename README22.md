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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61f752e6-1987-3c23-aa84-6eafd25ffffb | -17.62284 | -46.60525 | 2025-10-22 12:40:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| ebaf5c87-5aee-3a84-8ee2-b2aee2f93c29 | -18.13968 | -52.9857 | 2025-10-22 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 14c4b529-5781-392d-bac3-268ad0cde647 | -17.96696 | -51.08382 | 2025-10-22 12:40:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 786c9b85-5e74-3584-8c5c-3cf34f201c37 | -17.61999 | -46.633 | 2025-10-22 12:40:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 31b535da-eac7-306b-8c37-36eba3f7dd98 | -16.46397 | -53.46803 | 2025-10-22 12:40:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0ebcf549-1bce-30f9-9bf7-4e1544ec7607 | -15.76484 | -51.95535 | 2025-10-22 12:40:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 95d624d5-dad1-36b7-be8d-64a1036568f8 | -17.62459 | -46.61105 | 2025-10-22 12:40:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 6fbb350d-eea6-34a1-857f-0f287595f504 | -16.86446 | -52.8919 | 2025-10-22 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ba7f7be4-0bdd-3332-86f5-024af4d76d55 | -18.1503 | -52.9768 | 2025-10-22 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 934345c2-26aa-3b12-8cf2-dfb2de60bbcd | -16.43051 | -51.77976 | 2025-10-22 12:40:00 | TERRA_M-T | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| be25fdf2-8e88-331d-9603-012a1eb22493 | -16.82403 | -47.63177 | 2025-10-22 12:40:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 25381b73-1e33-3c1b-bd53-08933bef2e71 | -16.86313 | -52.90179 | 2025-10-22 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f5858fa-38d7-3bae-9964-70d7f4a1aa75 | -17.34776 | -55.04408 | 2025-10-22 12:40:00 | TERRA_M-T | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ea6bdb88-4000-37f8-a95b-2139c161b8b2 | -17.22487 | -52.25631 | 2025-10-22 12:40:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 7355f807-3c18-3ee6-97c9-774eb84915b3 | -15.87386 | -53.20402 | 2025-10-22 12:40:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5b22318d-80fd-3c8a-9090-ebaddae63101 | -17.34909 | -55.03487 | 2025-10-22 12:40:00 | TERRA_M-T | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4de3f494-1b6b-367a-a958-e0b683766347 | -15.5916 | -56.6609 | 2025-10-22 12:40:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a9145038-095f-34c9-a88c-288004c38120 | -15.09736 | -52.82272 | 2025-10-22 12:40:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 83e68cc6-b8f6-3c6f-965e-1a85d497e6ca | -15.88286 | -53.20538 | 2025-10-22 12:40:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1c9affe0-0ba3-3412-8826-914d6cb9036c | -16.92201 | -52.67452 | 2025-10-22 12:40:00 | TERRA_M-T | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 65719355-2028-3a8e-8d53-0adcabf80f5a | -17.41443 | -55.08254 | 2025-10-22 12:40:00 | TERRA_M-T | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 25.6 |
| b9ac408d-4a83-3661-8913-b23a89daee44 | -22.38343 | -54.6068 | 2025-10-22 12:42:00 | TERRA_M-T | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| ff8407ea-c428-3a10-8092-0076873fc1c7 | -21.43374 | -54.1414 | 2025-10-22 12:42:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 19.8 |
| dd5b1d29-59c2-37b2-805e-c06cb1511c39 | -21.44284 | -54.14278 | 2025-10-22 12:42:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0347fc62-a28b-33f3-bf33-fafb099b47c4 | -25.77377 | -53.0001 | 2025-10-22 12:42:00 | TERRA_M-T | DOIS VIZINHOS | PARANÁ | Brasil | 4107207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 459e94e6-3ae3-3ecb-8212-ef007700fc43 | -21.2201 | -51.40708 | 2025-10-22 12:42:00 | TERRA_M-T | GUARAÇAÍ | SÃO PAULO | Brasil | 3517802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| c315667d-93e6-3bb1-a6ae-8752e56f67e3 | -23.46629 | -51.93994 | 2025-10-22 12:42:00 | TERRA_M-T | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 5f7e003a-38ea-3033-b9c5-07ef7000f956 | -22.3821 | -54.61674 | 2025-10-22 12:42:00 | TERRA_M-T | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 42649509-a669-32f4-8344-3d4fc39339f5 | -21.09191 | -49.78972 | 2025-10-22 12:42:00 | TERRA_M-T | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.5 |
| 9ba7d563-efc8-371e-a1b6-1e1e78ce4f8f | -25.73336 | -53.41962 | 2025-10-22 12:42:00 | TERRA_M-T | SANTA IZABEL DO OESTE | PARANÁ | Brasil | 4123808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 6644c681-7f79-367e-aff6-ae6a71f34bd8 | -25.90598 | -53.50668 | 2025-10-22 12:42:00 | TERRA_M-T | AMPÉRE | PARANÁ | Brasil | 4101002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 214bbae8-b5b3-34cf-9750-02c4ad7dee48 | -25.90449 | -53.51886 | 2025-10-22 12:42:00 | TERRA_M-T | AMPÉRE | PARANÁ | Brasil | 4101002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| dca48ea1-c1cd-3188-8fdd-1ea71c35487f | -19.06778 | -57.48106 | 2025-10-22 12:42:00 | TERRA_M-T | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| f8d0930b-75b0-373c-9bcb-841e2fbcfd1a | -24.5543 | -54.11671 | 2025-10-22 12:42:00 | TERRA_M-T | MARECHAL CÂNDIDO RONDON | PARANÁ | Brasil | 4114609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 31a497c0-6370-356c-b6ec-c8cc1700f9db | -20.74261 | -53.05436 | 2025-10-22 12:42:00 | TERRA_M-T | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eb196828-64b4-3c0a-94bc-8c20a68327bd | -25.21138 | -50.98691 | 2025-10-22 12:42:00 | TERRA_M-T | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 60cba515-f745-3dfd-b3a5-8daf057c7d03 | -25.16742 | -50.10377 | 2025-10-22 12:42:00 | TERRA_M-T | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 566881e2-1d92-3683-bf62-abe30c2e2768 | -20.67879 | -47.90611 | 2025-10-22 12:42:00 | TERRA_M-T | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c0f9dbe1-0c83-3ff7-9f1d-76438c6009c4 | -25.67909 | -52.66974 | 2025-10-22 12:42:00 | TERRA_M-T | SULINA | PARANÁ | Brasil | 4126652 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| d307aee5-2308-3c0b-aaf7-3d7a65e4f5a1 | -23.76056 | -51.53622 | 2025-10-22 12:42:00 | TERRA_M-T | NOVO ITACOLOMI | PARANÁ | Brasil | 4117297 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 42a37370-19ad-33de-81c9-146e0652e650 | -21.22472 | -51.41504 | 2025-10-22 12:42:00 | TERRA_M-T | GUARAÇAÍ | SÃO PAULO | Brasil | 3517802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| bdc2af62-6830-3154-840e-91bcf707ed0b | -20.69351 | -55.42853 | 2025-10-22 12:42:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2009d15a-b925-3f66-abf5-a6fcbe092d17 | -23.227 | -47.29331 | 2025-10-22 12:42:00 | TERRA_M-T | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| a118f4bd-6cd8-3488-84cf-84fe1f647242 | -25.27752 | -53.9781 | 2025-10-22 12:42:00 | TERRA_M-T | MATELÂNDIA | PARANÁ | Brasil | 4115606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| d2606e6a-c06d-3371-a982-303fff432d1d | -25.82189 | -53.10606 | 2025-10-22 12:42:00 | TERRA_M-T | DOIS VIZINHOS | PARANÁ | Brasil | 4107207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| e62c88b2-9715-3b6e-8fb6-4d78dffa59fa | -20.69485 | -55.41915 | 2025-10-22 12:42:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f57b4d84-3847-30bd-ab16-9eefb04cc203 | -21.10388 | -49.79106 | 2025-10-22 12:42:00 | TERRA_M-T | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 491beab0-daea-365f-a32f-bf5b12c226d5 | -23.76226 | -51.52145 | 2025-10-22 12:42:00 | TERRA_M-T | NOVO ITACOLOMI | PARANÁ | Brasil | 4117297 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| ff8969f9-6a6f-3570-9617-a3088e576043 | -21.89684 | -45.09289 | 2025-10-22 12:42:00 | TERRA_M-T | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| f9c58d87-17ac-317e-b4ca-8b2b4062b5c3 | -20.71945 | -55.18275 | 2025-10-22 12:42:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 04cdf2e1-1e41-3f99-9f79-daffd2df9eb8 | -25.98664 | -52.56292 | 2025-10-22 12:42:00 | TERRA_M-T | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 709ebdce-4ba0-3730-8cff-cce501256b74 | -20.42834 | -55.73846 | 2025-10-22 12:42:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cd498af6-e8fe-3a2c-b870-cb638aeb9f69 | -20.67174 | -47.91208 | 2025-10-22 12:42:00 | TERRA_M-T | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| fe004d57-40e0-3071-8574-4618606792f9 | -21.89399 | -45.08766 | 2025-10-22 12:42:00 | TERRA_M-T | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.4 |
| cbedd568-b313-3a31-a1f5-8af1177c3629 | -25.0247 | -53.87685 | 2025-10-22 12:42:00 | TERRA_M-T | VERA CRUZ DO OESTE | PARANÁ | Brasil | 4128559 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ed1cc631-7111-386e-bfe2-79a04e068929 | -23.83715 | -51.56765 | 2025-10-22 12:42:00 | TERRA_M-T | NOVO ITACOLOMI | PARANÁ | Brasil | 4117297 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| af1392f2-c0b7-38e9-820d-3f97e1bf2c15 | -27.77466 | -52.61826 | 2025-10-22 12:44:00 | TERRA_M-T | CAMPINAS DO SUL | RIO GRANDE DO SUL | Brasil | 4303806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| f59e7c71-6b50-3bca-8447-196722e85e17 | -29.22635 | -51.33489 | 2025-10-22 12:44:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 6c7b2ed9-653a-34b1-8770-48923f6ac10f | -27.55085 | -52.89935 | 2025-10-22 12:44:00 | TERRA_M-T | TRINDADE DO SUL | RIO GRANDE DO SUL | Brasil | 4321956 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 793c02cb-75b0-38af-b172-6625da267336 | -27.60808 | -52.23817 | 2025-10-22 12:44:00 | TERRA_M-T | ERECHIM | RIO GRANDE DO SUL | Brasil | 4307005 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c011ec42-261e-3aa5-ba17-3d3563913c2d | -29.66007 | -53.92754 | 2025-10-22 12:44:00 | TERRA_M-T | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 11.5 |
| eebad201-0f8e-329e-a019-29c90892f042 | -27.94592 | -52.91926 | 2025-10-22 12:44:00 | TERRA_M-T | SARANDI | RIO GRANDE DO SUL | Brasil | 4320107 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 5bf6cee5-b6db-3fc1-94f3-212a6b758bcb | -30.4964 | -51.60567 | 2025-10-22 12:44:00 | TERRA_M-T | SERTÃO SANTANA | RIO GRANDE DO SUL | Brasil | 4320552 | 43 | 33 | nan | nan | nan | Pampa | 10.7 |
| 8aef8cce-56d0-3efa-8eb3-46b0b0b9d039 | -30.50169 | -51.61274 | 2025-10-22 12:44:00 | TERRA_M-T | SERTÃO SANTANA | RIO GRANDE DO SUL | Brasil | 4320552 | 43 | 33 | nan | nan | nan | Pampa | 8.6 |
| 24e3e701-e073-347c-8cda-0dca5a3f1275 | -27.09437 | -52.15461 | 2025-10-22 12:44:00 | TERRA_M-T | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| d3eb3fdf-d628-39b7-9c23-2da906315843 | -29.22824 | -51.31533 | 2025-10-22 12:44:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| a4f29b18-b38c-39e8-9ffb-2045618f22df | -27.48818 | -52.92788 | 2025-10-22 12:44:00 | TERRA_M-T | TRINDADE DO SUL | RIO GRANDE DO SUL | Brasil | 4321956 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 9d91e3d2-1d1c-35f5-9ec2-0726d8d6631f | -17.6167 | -46.614 | 2025-10-22 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 136.4 |
| c74355fa-f4d9-3334-8fb8-d973be29200d | -17.335 | -55.0366 | 2025-10-22 12:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 812965c5-5f5e-3129-ba15-faccf3730acf | -17.6167 | -46.614 | 2025-10-22 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 00638bb7-1586-3fd0-b28b-f9aa1c8ecbb8 | -17.6167 | -46.614 | 2025-10-22 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 247.5 |
| 01fc8739-1bc0-30b9-b265-8cbbeb61dbdf | -17.6367 | -46.6098 | 2025-10-22 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 50ca2fe7-1ba2-3b65-99ff-ad272574e18f | -19.0526 | -57.4941 | 2025-10-22 13:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 03e5b259-4bcf-343b-b1ba-8659bf453a0b | -17.6167 | -46.614 | 2025-10-22 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 401.6 |
| f0adf019-0e6b-374a-a008-3570ab4387dc | -17.6367 | -46.6098 | 2025-10-22 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 60936cc4-54f1-376d-866f-9403065d1fa6 | -17.6367 | -46.6098 | 2025-10-22 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 6033b148-5886-3e35-bc73-aa9f9a42fae5 | -19.0526 | -57.4941 | 2025-10-22 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| dfdc7957-d379-34e8-948a-9603ee865b82 | -19.0726 | -57.4915 | 2025-10-22 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 7d7798b8-6d2a-30e0-8e38-1bbfda6b4e69 | -17.6167 | -46.614 | 2025-10-22 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 359.2 |
| dac09318-86e2-35a0-9ef5-932f7706b449 | -14.2245 | -51.5462 | 2025-10-22 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a7b39f49-37fd-357f-ad8c-c842bb1e679f | -17.6167 | -46.614 | 2025-10-22 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 606.6 |
| 4441b3fc-ea01-3524-af86-a5f473f22e26 | -17.335 | -55.0366 | 2025-10-22 13:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 45353728-3b9f-3522-8e42-2ac36a3fa779 | -17.6367 | -46.6098 | 2025-10-22 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 2bd61fa1-bdac-399b-8621-5439e8837bd0 | -19.0526 | -57.4941 | 2025-10-22 13:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 115.9 |
| 1d6f3ee5-380d-3fac-bda1-9f97590c690f | -19.0726 | -57.4915 | 2025-10-22 13:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 111.4 |
| 6b4162c0-12b8-32ad-bf6f-c102e4542cd2 | -19.0526 | -57.4941 | 2025-10-22 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 122.6 |
| 41837920-b4b5-33af-8db4-1133482a1548 | -22.3753 | -54.6198 | 2025-10-22 13:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 73.5 |
| 13b3aa9c-49c2-38b9-88ce-19b2f9aafdd4 | -19.0726 | -57.4915 | 2025-10-22 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 108.1 |
| 3c625469-5d6e-3e3c-84b8-69ee832b5ad9 | -17.335 | -55.0366 | 2025-10-22 13:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| 264ccfa8-7491-3cf6-ab36-6eeedd7d2e3c | -17.6367 | -46.6098 | 2025-10-22 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 5f783ff8-85ce-3655-8bdd-242225c231e6 | -14.2454 | -51.4579 | 2025-10-22 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 986c5886-06a7-3cb3-bc49-a5d544c3e84d | -17.6167 | -46.614 | 2025-10-22 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 373.2 |
| aa401650-4e89-34b0-98bc-6af425d9ee2e | -17.6167 | -46.614 | 2025-10-22 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 581.0 |
| 5d15b72f-9ffa-3af7-aa3e-a427d3bf7873 | -17.231 | -52.2472 | 2025-10-22 14:00:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1e6bd67e-612d-333b-8a8e-0276f43e0e96 | -19.0526 | -57.4941 | 2025-10-22 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 83.4 |
| b34d8bb8-6419-3ae6-8912-1dc2c5ff9e3f | -17.3547 | -55.0339 | 2025-10-22 14:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 186.1 |
| 762bc3ff-4d1f-3a83-8446-fd2c8b6e66f9 | -17.6367 | -46.6098 | 2025-10-22 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 294d8140-11a9-3b73-92b9-30e604e51cea | -19.0726 | -57.4915 | 2025-10-22 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 2d0d91ae-c499-3ec6-a3be-bd875cc45ca0 | -17.6367 | -46.6098 | 2025-10-22 14:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 13055079-a7a2-37b9-af23-255c2809b7af | -17.3547 | -55.0339 | 2025-10-22 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 129.2 |


[Clique aqui para ver as próximas entradas](README23.md)
