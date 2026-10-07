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

## Dados Diários - Página 199

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de27b030-3753-3b97-9e2d-191f646b6c17 | -7.89467 | -54.72137 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5469728f-c16c-3975-b111-5b65e543a98f | -4.57479 | -43.88223 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c60e564e-f636-3ed3-9a2b-d6279e79f2c1 | -6.20737 | -41.58727 | 2026-10-07 16:37:00 | NPP-375 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 8c53987d-078c-3169-a1f1-5c16382a6d62 | -6.64916 | -47.91025 | 2026-10-07 16:37:00 | NPP-375 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2e75c5da-243d-3f37-8619-9bc9c9a2f183 | -3.27733 | -42.74403 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 219e2b75-3345-3105-a231-0efc766825fb | -5.98581 | -40.93634 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 36b7ef2e-9e0c-3eab-8828-a996f4e9e8c9 | -4.6677 | -40.56379 | 2026-10-07 16:37:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4350a455-e4ae-3800-9cf2-35b0ad5d5d70 | -11.12308 | -45.95346 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 9a3763ec-9964-3f95-bdf2-ca5cbd75913b | -6.60339 | -41.58241 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 40369fa2-a89c-37cd-b005-402d3f3a882f | -7.3528 | -55.0097 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d40d26ca-26e3-336b-b0a9-da23ba967b72 | -7.6934 | -44.74006 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c38cfad2-3390-3887-9537-b945c4c13ed7 | -7.83287 | -44.18566 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d45dc006-e49c-3481-a281-d172eb6dcede | -7.8717 | -54.98545 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 4019a329-22ce-34f5-bd3e-a22a348461d7 | -3.5613 | -39.14003 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 40.7 |
| 77c1c6cb-aba6-35b7-9305-7da8de68a11f | -11.01702 | -47.97235 | 2026-10-07 16:37:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 76e346dc-a974-3f8e-a39b-5b15d5dd5af7 | -3.77154 | -44.35468 | 2026-10-07 16:37:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 24e47203-8d1e-36ec-8c7d-02b4b3b4a95c | -4.8198 | -40.02319 | 2026-10-07 16:37:00 | NPP-375 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ff5166dd-a22b-3f6a-b6e8-08f003e59877 | -14.67346 | -40.8096 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6ac29b70-b1b7-3b0e-95c5-8119bf20de92 | -5.95892 | -55.34072 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 2beb660e-3b62-3f37-9835-a1a15b3b21b7 | -4.79081 | -43.33368 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 7cd53e21-f4f9-3e86-90b3-1b1bace0759c | -10.68135 | -47.81694 | 2026-10-07 16:37:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8cfd2b16-1dba-3932-a6df-bbb68980e6ff | -5.73862 | -41.72459 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 12ba0921-47a8-31da-b128-4e0f3d5880b4 | -7.7829 | -35.37139 | 2026-10-07 16:37:00 | NPP-375 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9c49183a-17ad-3f6d-bb26-8044754a906c | -5.60551 | -45.58467 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7f0e385-bc9b-39b8-9b7a-f60e8c5e080a | -5.98074 | -41.36592 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4aaacfc9-b03e-3cbf-b1b6-824944dbf54b | -17.02367 | -45.92288 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d2d3adbf-8b40-3773-8580-68e445fec1fd | -15.72707 | -39.82692 | 2026-10-07 16:37:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 9fbb1cb9-51bd-3c79-863c-ec33858fcb58 | -6.98206 | -43.21974 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 076a4c3e-7990-329e-8671-ebfdbed51fc4 | -7.77181 | -48.23574 | 2026-10-07 16:37:00 | NPP-375 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 27d236cc-d8bf-3835-9252-45fb66401e9b | -4.07706 | -47.30054 | 2026-10-07 16:37:00 | NPP-375 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 817a2044-a62a-3feb-9313-f30fe34c3407 | -14.90268 | -40.82324 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 56af4e36-1430-3895-8cc2-d77457c7a43f | -3.22576 | -42.65204 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| da80321d-3b14-3757-8584-98c04c914fc3 | -7.53469 | -45.87782 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 62b62b4c-3cc6-38fb-aa6a-caab7676041c | -15.39267 | -41.69954 | 2026-10-07 16:37:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.1 |
| af5291eb-1eaf-3bdc-9cb7-0fdbad94a9c0 | -4.6309 | -48.85987 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a7660502-3479-34ae-8ed2-cee931a68168 | -11.14109 | -46.16195 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a5323be2-991a-34c3-b086-8a3770cca9de | -7.08763 | -35.23459 | 2026-10-07 16:37:00 | NPP-375 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cad917a9-1395-35fc-97d5-d8ef322aab01 | -5.60555 | -49.16352 | 2026-10-07 16:37:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d8cfc69-db07-348e-8223-40a8c5295374 | -9.39874 | -45.81135 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 14b31917-5784-37f1-994b-b70c20ddd59a | -15.96994 | -40.70408 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| bad8c71f-d6f5-3c39-ac86-cdeb90929bef | -6.04253 | -42.58748 | 2026-10-07 16:37:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 6d5f2aca-d7ea-3b35-bf51-1d687340d6a5 | -3.28517 | -42.26859 | 2026-10-07 16:37:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 49576ac4-96bf-3a61-9c19-d17e046ea3d9 | -7.18649 | -52.61462 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7644af5b-26b6-3d30-b4af-dcebafed39e1 | -6.44763 | -52.6712 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 830e9180-d987-3167-b864-aa0f1994756d | -7.19034 | -44.29483 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 714d6288-db36-37db-99a0-459c29f1307d | -6.94388 | -45.27924 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 63ac7ecd-0e08-3f25-8f61-b7214db7b6a8 | -3.86646 | -44.13396 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| dd99c0e3-6123-3dcc-9f98-899d2caf2e50 | -7.46287 | -43.20675 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 21a3bf39-9f25-3a43-a3f1-dd23cf79874b | -10.37793 | -46.25951 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 96b22c4d-af8e-386b-99a8-4eb092acd4fa | -15.96599 | -40.70096 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 60255a3b-5e2c-3e6a-8e68-a320baf7ec72 | -4.10419 | -42.49674 | 2026-10-07 16:37:00 | NPP-375 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a92d71df-28ad-307e-a32d-79bfed652de3 | -4.29732 | -50.78266 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3ae48c3c-cdb8-38f2-88d9-e087e2ef3654 | -7.86852 | -44.15165 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e6eafe88-5788-33de-a1f5-c5d66028275a | -7.47843 | -42.82181 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4de9bf2a-6281-3248-8ffb-a1582a238d39 | -3.2103 | -42.96053 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c32a7125-4b27-36ba-b003-12fce16aa3ff | -9.04044 | -46.87967 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 322b2d18-1d71-377c-9450-1db028c603c1 | -4.6347 | -48.85614 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| edf3680a-9d71-31e3-8d6d-cd182369ca57 | -5.98009 | -41.3619 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c26110cc-61de-392e-9fcd-adfb4dd8e95a | -6.98036 | -40.03157 | 2026-10-07 16:37:00 | NPP-375 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 0b8ffb68-1d04-38ea-a592-da32518f2985 | -4.23585 | -49.98059 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 17179d56-24ef-3ef5-a40a-b33896152cc9 | -5.28163 | -50.09782 | 2026-10-07 16:37:00 | NPP-375 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4df6611c-9f49-38ca-82cd-075ba83f41fb | -11.92202 | -50.63845 | 2026-10-07 16:37:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e4011f52-bd75-3fef-be1b-e31be4ca42a6 | -11.15026 | -46.11958 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f9a6f96a-1fd1-3699-8357-09c7f8e869df | -6.81871 | -38.53477 | 2026-10-07 16:37:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 6b4fe581-7436-3a6e-bc99-d49b03da3a25 | -3.75557 | -41.71114 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7a58db03-f27d-398b-902e-ad1d6a6ac932 | -7.47118 | -42.81933 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 2ad06298-8f53-3ce2-93cb-e328fce2eeb5 | -6.93782 | -45.26186 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 54a2257e-bd2b-300b-88af-326f33ed5f8d | -7.39931 | -38.84575 | 2026-10-07 16:37:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e8d551b6-e516-3af6-9ef3-5ee2f35c4262 | -3.74712 | -41.71222 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| aeafd759-fb3b-37a0-bc1a-e215ea13ea19 | -5.48774 | -42.83508 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 123.5 |
| 23b14299-2923-339d-8fd4-31636d3467f3 | -7.10158 | -45.24066 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ded8f723-b22f-317c-9891-f3f02766ea3e | -5.10529 | -42.93629 | 2026-10-07 16:37:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2c40965-b5bd-3465-a564-c7638ed59d37 | -6.46135 | -55.46961 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 41e6325c-e535-31d9-a5d1-8f90d7414135 | -7.2091 | -55.09839 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 755b7ba9-a169-3baf-b8ac-1bbe925d0b7e | -6.95565 | -44.41431 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eee9e279-9f96-3b8e-a1b0-1e7e0742d635 | -9.15009 | -45.83116 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2082895f-b1cb-3b6b-bd1e-d1ebf8e46f1b | -3.75119 | -44.61609 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1177209c-0b14-3bbb-8b53-a079973f02d8 | -17.19868 | -43.52486 | 2026-10-07 16:37:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6586d2e-bb1d-3260-8e34-30c2962c63de | -6.81603 | -52.86346 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1255abfa-a42c-393e-9664-a45508f83065 | -3.90044 | -38.49992 | 2026-10-07 16:37:00 | NPP-375 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f58fd51f-5d72-3c4c-8ada-bd305c2a3c30 | -8.59444 | -45.6699 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a2e53a43-11d8-3b67-bdda-74722fe95de9 | -6.5914 | -41.55221 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a3e08e06-ea99-3c98-af99-bb7008d33bc5 | -7.74985 | -54.95589 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 8d03bfb5-0a44-3f52-aff0-95de1d841bde | -15.65282 | -48.98413 | 2026-10-07 16:37:00 | NPP-375 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 051195bb-5db6-3ebf-9fcd-b19660a363aa | -3.6639 | -41.44027 | 2026-10-07 16:37:00 | NPP-375 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 933dda7c-1554-30b0-8fba-5b6678def9bb | -7.56281 | -47.78734 | 2026-10-07 16:37:00 | NPP-375 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 17140b56-4331-3321-822a-a64ae917ef23 | -4.11886 | -49.06797 | 2026-10-07 16:37:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 68716192-8a80-326c-b058-c96c7fa832de | -6.31888 | -43.48306 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d304a171-01aa-3481-85df-02642559c61d | -11.08674 | -45.64748 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a47b4d8d-4109-336e-ab5f-49d87eaeda02 | -9.86995 | -46.0593 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 2e623bc1-ad33-3bef-bd10-7e4c2ffc882d | -11.44673 | -47.65878 | 2026-10-07 16:37:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cde0f952-c411-302b-ac12-dfef5d3b93d0 | -6.47054 | -55.44382 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 49069f35-2f23-3025-8e39-8af8a7bc1364 | -4.76189 | -42.59295 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 83108f3f-33a6-38aa-a6f7-b355e7685af2 | -15.11773 | -39.92375 | 2026-10-07 16:37:00 | NPP-375 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 13fb317d-7506-3a59-b35b-983b0dc0261a | -6.24555 | -53.45834 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| fe097e4d-98ea-3822-8ebd-f87fd0aeb42f | -6.3248 | -55.33026 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5f4d4ac8-bb2e-3080-b10f-5f5bceb80b89 | -11.23181 | -46.25008 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 33bb9cee-2a3b-34f3-97af-326fe60f34b8 | -3.84075 | -42.6375 | 2026-10-07 16:37:00 | NPP-375 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 557fc45c-c934-3d0d-9f56-a43ddd6814d5 | -3.5103 | -41.95547 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 7ba2fe2d-3b76-36d0-887f-4bbbceac393c | -3.77433 | -44.35071 | 2026-10-07 16:37:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README200.md)
