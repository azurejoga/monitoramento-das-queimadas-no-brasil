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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 476994ea-eaef-3ac6-b098-5385a9dd040f | -16.30186 | -52.94336 | 2025-09-02 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4188b3f-7803-371f-b66d-09c12467bb3c | -17.2857 | -49.20662 | 2025-09-02 05:08:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29cc1441-8103-35ee-8c92-de7edc11e87c | -17.29171 | -49.20045 | 2025-09-02 05:08:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56d8baaf-6094-325c-b2ba-48503a16487a | -15.97378 | -48.24145 | 2025-09-02 05:08:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 039a034a-956d-3186-8b4e-45344bab23d9 | -17.70478 | -46.88751 | 2025-09-02 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bddb844e-6084-3ce4-a6a8-5742ba58a33f | -22.52906 | -46.80326 | 2025-09-02 05:08:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4a9698af-501c-3ac1-912d-843e2d65b177 | -16.59236 | -48.97504 | 2025-09-02 05:08:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30cc3326-8032-3163-9640-aaa4d29e41fd | -18.07218 | -45.96129 | 2025-09-02 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8147ce78-81bf-3677-ba28-20140d6b7ea1 | -17.8827 | -47.15813 | 2025-09-02 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92100da9-c91b-370a-a9ef-d0d0b7733c22 | -17.70427 | -46.89253 | 2025-09-02 05:08:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 319d5b4b-d2b5-3a8a-998a-43b1731c1fe3 | -20.69963 | -46.30793 | 2025-09-02 05:08:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81289207-592d-32d1-bc19-36b3724a7e67 | -17.89563 | -47.16763 | 2025-09-02 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 081c7061-d12b-3926-b30f-a43fb451a199 | -18.07274 | -45.95523 | 2025-09-02 05:08:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 917e225f-4494-3db3-a7ee-3bf3d70f9dbc | -18.54961 | -47.4649 | 2025-09-02 05:08:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb7b8705-7f0c-3c5e-86c1-6cfb7b8cba5d | -15.45375 | -59.0984 | 2025-09-02 05:08:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c01b481-5376-3816-8ac6-918b0f3757cd | -10.0623 | -48.0978 | 2025-09-02 05:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 1a4e29e6-9b5f-3389-96ce-2c66f5603a84 | -7.5476 | -61.3437 | 2025-09-02 05:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ab083aff-5212-3e19-9eec-def0e7e575af | -9.7294 | -48.9834 | 2025-09-02 05:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| c213f743-5d22-3c4a-8202-cb3bcc528573 | -22.95384 | -49.7397 | 2025-09-02 05:10:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7bc14918-5397-367b-8b19-b7dc3d237d8f | -23.20832 | -49.75836 | 2025-09-02 05:10:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e083dc27-a750-3473-ad7a-6cf596333283 | -23.50309 | -50.79758 | 2025-09-02 05:10:00 | NOAA-21 | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9cd80f6c-2ea7-32fe-9c42-f27bc52e67a7 | -22.95965 | -49.73644 | 2025-09-02 05:10:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 43b22632-61d9-3601-97d3-d5e14067f62e | -23.53617 | -51.59666 | 2025-09-02 05:10:00 | NOAA-21 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ef710c74-0ac2-3ca2-a99f-c04136254f7e | -22.95419 | -49.73585 | 2025-09-02 05:10:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f7c45f40-d517-333b-b313-fd2365145b10 | -23.54106 | -51.59719 | 2025-09-02 05:10:00 | NOAA-21 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0cc26868-a1fa-391d-b133-94f42941d5dc | -23.72294 | -51.66217 | 2025-09-02 05:10:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ac03d1dd-060f-35e0-bf80-b743bf984ade | -23.72783 | -51.66264 | 2025-09-02 05:10:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3e6653b1-5e50-375b-a2be-83d904c1379c | -23.93514 | -48.8462 | 2025-09-02 05:10:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48317963-d484-37bf-a581-bda65be5b6bc | -23.72843 | -51.65654 | 2025-09-02 05:10:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1a02bd6d-c620-3097-a697-c606eb7d5493 | -23.65525 | -47.41008 | 2025-09-02 05:10:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4a4d4022-6fd3-37c0-91cf-5d14611247cf | -23.31994 | -46.03684 | 2025-09-02 05:10:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 348fcd27-cc2b-35da-b3ed-2b0ea9e174a7 | -23.65184 | -47.41117 | 2025-09-02 05:10:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c2c19bd3-0bac-3481-a20b-2222b2948f00 | -32.21221 | -53.38365 | 2025-09-02 05:12:00 | NOAA-21 | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 924a23aa-0059-3ac0-8912-a74b78c4c1f8 | -7.5476 | -61.3437 | 2025-09-02 05:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6bbda8f6-e81d-3dd5-ad36-800192172e4b | -17.9016 | -47.1569 | 2025-09-02 05:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 9acbf512-a709-3e89-977d-6c3cbd12feab | -10.0623 | -48.0978 | 2025-09-02 05:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 24c3365a-d1b9-3229-94f1-9a29894ffb8e | -7.5477 | -61.3247 | 2025-09-02 05:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7b619a36-f4d2-3ee5-8f6a-f295d2163539 | 2.89579 | -60.26289 | 2025-09-02 05:29:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ee15589-437f-370f-908b-a141aec6974b | -3.78535 | -47.56792 | 2025-09-02 05:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82ab3667-d3d5-3b9d-b437-33444b4f6c3f | 1.0367 | -60.51545 | 2025-09-02 05:29:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 880902d2-1494-325e-91e8-789bbe4d3ebe | -4.47877 | -48.12007 | 2025-09-02 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c42847e9-7e61-3d12-b726-a4e4dcdefc3d | -4.30771 | -48.09787 | 2025-09-02 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4ac59bb-e077-3ae3-ae49-b6ccad2fad86 | -3.11861 | -59.92923 | 2025-09-02 05:29:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e62b0ac1-1899-311f-9da9-87a5f5d495c3 | -4.47972 | -48.11345 | 2025-09-02 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 254beb95-4cd0-332f-a681-74a228b991e5 | -4.30869 | -48.09115 | 2025-09-02 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 014aaccc-183e-3577-8c36-b4f132bd7a59 | -3.11522 | -59.92872 | 2025-09-02 05:29:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 741a8d61-a5fd-3f29-b6ce-6f8010436bba | -2.8822 | -59.2271 | 2025-09-02 05:29:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b75b500-0cea-3cb4-8044-454b1723f493 | -4.30452 | -48.09633 | 2025-09-02 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7743453c-c1a5-3de3-a246-4a0884a1536d | -4.31158 | -48.09733 | 2025-09-02 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e92fd9fc-6b0c-381f-a4b6-13de96efe337 | 0.9697 | -60.40933 | 2025-09-02 05:29:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7016d09f-2548-38cc-a6a0-e94b9a06a6bd | -11.0841 | -44.6575 | 2025-09-02 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1d205b66-c0c8-32f7-8236-f2ef34d6c8ae | -11.1033 | -44.6548 | 2025-09-02 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 270.8 |
| 2df2e719-65a8-37f3-9df6-baa90904a04c | -11.0845 | -44.6343 | 2025-09-02 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 846b962e-ad70-3151-a933-9a81c9eee1fa | -11.1224 | -44.6521 | 2025-09-02 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 788892d7-ffdd-30a4-9591-d5a2c4e76b15 | -11.1037 | -44.6315 | 2025-09-02 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 83f09afd-97ae-398a-8bf3-4ecbd6e6ebf0 | -7.5476 | -61.3437 | 2025-09-02 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 61cb9a71-9d88-3017-9cfb-45aa8e3d70cd | -10.0623 | -48.0978 | 2025-09-02 05:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ad52517c-b6c2-314a-8988-e61748de3166 | -7.53629 | -63.8542 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e667650-35b3-3cc4-bf1b-6cbde44e8eba | -9.09157 | -58.88155 | 2025-09-02 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a42f67c7-97d0-33f0-883d-a1c02055f145 | -11.83106 | -51.54338 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 716eaa34-c22e-3de6-a6b1-11fec391db27 | -11.67847 | -52.20027 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 064442b6-f707-3b05-a1eb-ec82c7bf9833 | -11.65439 | -52.18216 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1b2f3f3e-d883-32a7-856e-7dd8f60f1b00 | -11.93666 | -50.60938 | 2025-09-02 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 614b04d0-a92f-33bf-ad41-9e26326f3fda | -8.26962 | -61.45533 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0289ab29-b978-37b4-a667-9b6219c23d1c | -7.08487 | -63.18146 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae9083fc-1a1b-348b-95c9-6faceae353f0 | -6.80338 | -52.81559 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63a5518f-8405-3a67-a2c5-f61e63c96f65 | -6.82765 | -52.83961 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d193f9c-c852-33c8-8b91-661c13bd5b9f | -8.64721 | -63.26862 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0afb118a-b172-3887-8ed6-c9b955f32dc1 | -7.67783 | -61.08553 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 63677c33-8598-33c0-b0a8-ce72806af02d | -6.77081 | -52.81081 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbbf85a2-69e0-35a4-88a5-c0ab3b694e42 | -8.68907 | -62.40725 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b084c63-e1ef-3f74-b2fe-0a5a92eabdfa | -8.96987 | -65.97314 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25985198-a27f-3888-a43d-11a52b2c6716 | -11.67346 | -52.19053 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9a4b3817-a317-3bad-8e66-67f14c47eb46 | -11.67029 | -52.20268 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cc3c7eef-aa38-314d-b5e6-7aa2d62ed623 | -11.8379 | -51.53968 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 382c291c-e1ee-310a-9edf-8c2d9c7bf5c5 | -9.2851 | -61.01708 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3d3179b-5193-3888-aefd-4559e3d57e7f | -11.67794 | -52.20479 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 71dbd44b-fe08-3afd-9289-68a023eb4e9d | -7.67727 | -61.08912 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c03f420a-64eb-3169-b0c8-446f1458dde7 | -8.70237 | -62.40936 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02a24774-39e6-3e55-94ab-6a6edcd79df6 | -8.76049 | -62.42568 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 110da7d3-38b0-3c29-841f-d65d4d5c44c4 | -6.84104 | -52.83019 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23160851-2f13-3beb-936c-af4ea0e74ebf | -10.27542 | -54.26241 | 2025-09-02 05:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4727289b-317e-3a2a-b61c-0636e6e86521 | -8.76039 | -61.43567 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 092ef551-06ef-38d3-aa2a-fb2996372104 | -11.66981 | -52.22196 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2d251fbb-c385-32a6-822e-d246e5cd9df8 | -10.76156 | -59.84043 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2d95a26-21fc-30f6-8424-361667105ae2 | -6.79845 | -52.81129 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e73a502b-3021-39e8-a24d-0d564e247c5a | -7.57592 | -63.04654 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f730021-9ee3-3c22-9639-e98825f524b7 | -11.8426 | -51.46269 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9472507-3aa1-36b7-b8cc-50ee9df501b4 | -11.66974 | -52.20712 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7bf50f4f-2549-3e94-b91e-dfb58a9721e6 | -6.79348 | -52.80722 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48552517-3968-3002-b763-a13d84b5e539 | -6.56649 | -60.0584 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d144490-7376-3507-95a2-3edf45b1278f | -11.91912 | -50.61949 | 2025-09-02 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fb72e26-0bac-3155-aea2-f57addcbd333 | -7.67501 | -61.08139 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80a71446-9688-353d-bda4-131d11c78fec | -7.50469 | -63.48957 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e877d7d7-aed1-397c-9bf0-d262bd94d7d5 | -9.73477 | -48.98168 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 26bd02c9-6c80-31ab-926f-d07e9aa9820e | -11.66535 | -52.19294 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0e4352d8-06d6-3513-a500-fa0081208ac1 | -6.84151 | -52.82678 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec67af0f-cc31-3039-a025-ed64bbeefd76 | -6.85609 | -52.80124 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ead25d6-c506-3883-9e2c-5e6e6b0bce9a | -9.54894 | -65.95005 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf03873d-1cfd-371e-a1a6-02755985cf86 | -6.33758 | -58.18581 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README73.md)
