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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b5b8079-4030-369f-8348-e1b29bf896f4 | -10.56958 | -49.78241 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4955531c-ccea-3945-bba6-036ca5176db0 | -10.87331 | -50.10567 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2825aea4-32ed-36e8-8690-c89c0b5b7519 | -9.87323 | -47.45845 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7be30893-caa6-36d6-b420-f94f69384206 | -13.2572 | -47.96366 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 799aad47-9b4f-376a-a424-6f6893b9df9a | -15.6181 | -43.67094 | 2025-10-28 04:44:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d297b426-a156-3867-81fa-e7dcb9c2665e | -10.84173 | -47.89354 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a91119fa-3d05-3da1-abea-ec05bbeeeaaa | -9.95699 | -47.08945 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 262b7452-7568-3506-91ed-fe664cc8304f | -13.67201 | -46.51553 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a57d21a5-d763-36d0-b2f5-d7eddf44c300 | -9.17377 | -44.57486 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b95f0d1-573f-3eda-b302-bdca677da17c | -14.08548 | -44.15342 | 2025-10-28 04:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7f16830-cff7-35e7-b9a7-a2f2c416b0ff | -13.01289 | -47.21698 | 2025-10-28 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5972531-a01c-3e41-a50c-78a7819c1afe | -10.68871 | -48.02463 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0b7a91c-f74c-3c7c-b95a-17b2f11ad502 | -12.98364 | -47.92707 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8715be67-7070-3c35-8216-0539774112d2 | -12.00074 | -49.85482 | 2025-10-28 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4384a2cf-8ad6-3f63-8457-39767f91d49a | -14.4408 | -49.43993 | 2025-10-28 04:44:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8ccf2b3-6f89-31dc-bcc6-3bee35248807 | -9.58515 | -49.67368 | 2025-10-28 04:44:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb3e09b0-9f0a-3110-a94d-79b014f803b1 | -14.73145 | -48.17687 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67d79400-e4b3-3f15-81d6-81400a227b83 | -13.91422 | -48.49519 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 142b0709-758b-3d69-9d57-476efca64872 | -14.30928 | -46.51482 | 2025-10-28 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63386e2f-5dec-32f3-b2af-c614006ca16b | -8.19161 | -48.17578 | 2025-10-28 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3da52144-dea1-36f7-8c36-3d80f16175ba | -13.31186 | -47.68587 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50049367-8ed3-32f2-bd8f-e96d793d3ce8 | -10.58237 | -49.76631 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8946501c-932f-3b1a-bdcc-94ef6d4e4ec8 | -12.53461 | -47.56483 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73a77dee-fb31-3cdc-bb4a-42abd9ec28a0 | -10.29298 | -47.18276 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15682371-3cf9-305f-8cdb-52d03773d191 | -9.89148 | -44.90247 | 2025-10-28 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2a9d0ad-d3ba-31bb-abca-f3113a0f203d | -13.3971 | -48.51142 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e835dd20-0c97-3296-ad98-ace0ff4f4273 | -11.70959 | -44.44614 | 2025-10-28 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dadf80ab-83c3-3cc9-b105-64d372bd3e87 | -12.59575 | -46.82814 | 2025-10-28 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84c620f7-b024-3f9c-87f0-920b5aa5460b | -13.3701 | -47.4102 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15d44caa-b345-36bb-b97a-7cc56468825d | -11.05008 | -49.90541 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bef5f46b-76fd-301a-bbdb-c5810a0d30b8 | -10.32043 | -47.14816 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed751fb2-e884-376b-a65e-b3991b3ee99d | -10.96717 | -50.26107 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aeff788-97df-349e-8a64-3b113ee14b20 | -13.21928 | -47.09256 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d20f033a-9714-33ac-80f9-fd3a69d1c593 | -10.39162 | -45.30554 | 2025-10-28 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79e6c174-0142-3cf9-b564-b70482f89592 | -13.37178 | -43.46049 | 2025-10-28 04:44:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1038eba-9943-3f80-8d64-de7eb112cc4b | -8.69851 | -50.80254 | 2025-10-28 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd6d30d6-b26d-3374-8ba3-84f3584c2042 | -13.0427 | -45.85174 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8933cbe3-8efb-3395-88c3-62da6bdb06c3 | -9.47151 | -46.90284 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be8ccd88-d066-3be0-96f9-90c110e46550 | -9.96 | -47.09425 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 750827d5-8181-36aa-8e44-4680632cee24 | -10.65181 | -44.11576 | 2025-10-28 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3434559-5d73-3415-a739-3d9df62e3fda | -13.50925 | -48.89548 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32e91aea-06aa-3447-99a1-fc6d0791de2d | -10.95443 | -50.27706 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fb886e8-a6c8-3c5d-a488-53fcbf31abff | -9.62569 | -47.72121 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8329fd88-ccb6-3bd3-bc4e-82e52f7255dd | -9.26536 | -45.56564 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95e7d1ad-0ff7-3783-bf3f-cdb70d1ec629 | -13.2255 | -47.103 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b2fafef-ed06-3f73-ac8e-043c4a2ccb52 | -12.22107 | -46.49063 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 155cca32-3ee0-335f-a411-483770b28809 | -15.15583 | -46.58892 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 96e6e5c4-f12e-323e-8c8a-39f75c85b5f9 | -10.91421 | -48.00873 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c516361b-4e8a-3183-acc3-118c496a3539 | -8.86534 | -45.40182 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b27c5a4-c033-3323-913a-a9b6db44d37c | -10.33083 | -47.22723 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b0b0ab6-d734-3513-803c-a1452664d632 | -13.94465 | -43.80013 | 2025-10-28 04:44:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12ca8c97-38eb-3de6-ab62-a22da93720a9 | -13.0432 | -45.84807 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb88f1b9-da43-37ca-b422-3f86bda4843e | -10.64372 | -48.01376 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75aa3e4c-002e-31e6-924b-1434942d33c3 | -10.29949 | -47.21385 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ff454c8-73f9-318f-b89e-16dfc548d3f7 | -13.24722 | -47.05932 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8963aa59-7fcb-33a4-83d7-b955ca363a9f | -13.5359 | -47.16551 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28fb2d44-c684-3e24-9e33-2250e22ef983 | -13.73836 | -48.41574 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 044c21c5-402e-3604-b841-23166725d83e | -9.37117 | -50.8105 | 2025-10-28 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb5f7ab3-84c5-3e59-a914-1183aa034f94 | -10.56236 | -49.78488 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c332b658-779c-3ba2-836b-9002f7ec9615 | -8.51298 | -47.19676 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f292f75e-7a7b-32ac-aa69-13859cb98c6c | -13.90651 | -48.47377 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6090318c-f975-3fb6-a439-33496bf825c9 | -14.53359 | -48.00053 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3013418-da1b-3a46-9531-4f60485c778d | -9.16543 | -46.37063 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 790acfd4-c866-3cf8-9e50-9901c50e51f0 | -10.86835 | -50.13729 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a737644c-0e68-3635-ad13-1198a9c47b41 | -14.42713 | -49.41898 | 2025-10-28 04:44:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 239aff33-c632-3c65-9c98-3c6d2bfa89bc | -13.63509 | -46.464 | 2025-10-28 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8005daa4-71f1-36a3-9086-6e989447c7f5 | -8.63955 | -44.77551 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf55835c-817f-36da-ba0a-e4a64c9f8ba8 | -12.61837 | -44.25427 | 2025-10-28 04:44:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3eb50b50-5b7b-3eb3-846c-69b7cad3a2ef | -8.6397 | -47.72189 | 2025-10-28 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06be8da0-e82d-3c69-90db-c7525ca6f1c6 | -13.88803 | -48.50068 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf790021-ce7c-36aa-afdd-d267e373ee13 | -10.87843 | -47.98328 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d96b3fa2-e0a2-38b3-914e-1bbe2cabbb7a | -14.0816 | -44.15491 | 2025-10-28 04:44:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f387e66f-b558-3456-ac3b-9249de994389 | -10.5857 | -49.76684 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d729398-452f-306a-abc5-4f751899a45d | -10.92441 | -47.81888 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0864231-f656-32c6-b468-f921d7e322e6 | -10.94607 | -50.27249 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cde69b42-2714-3e96-b415-cad43afc623f | -9.39122 | -47.70084 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b61abb8-2d2a-38ca-aa2b-50812b1c6895 | -14.72653 | -47.3596 | 2025-10-28 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58487dd4-cc26-35d8-8d71-047004765d31 | -9.14165 | -51.29787 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3090b228-9427-3c08-8379-feb8214a8f07 | -9.89585 | -50.04646 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b2d91f9-8afe-3d27-882b-51ea66247f62 | -9.33761 | -49.29096 | 2025-10-28 04:44:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95a0b378-e2dd-34b6-aa6d-91499d24f24d | -14.5707 | -48.00208 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4a78433-87fb-322f-9c0d-920d8a9e95f0 | -10.22276 | -49.90075 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d722e0c4-e117-3b90-9419-566a70ffdbf6 | -10.56068 | -49.77374 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 255385ab-f06e-3e86-b7bb-f59d4f17d810 | -13.54185 | -49.57644 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c3b3b3d-e1c1-3ffe-ae09-dee97e300512 | -14.53417 | -47.99638 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bbf8ee3-adcd-36c5-a3e5-10c6e0679658 | -12.18793 | -47.0217 | 2025-10-28 04:44:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4b14722-365b-34cb-8591-f82e420ad526 | -13.62413 | -47.02665 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 74917305-d1d6-3a93-96d2-b40b78356e9f | -10.95055 | -50.28004 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c78e63d2-88f7-34bb-bb62-4c88c35a15e8 | -12.5541 | -44.93328 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 492776d5-5063-33d7-988f-3cb84cdfd67f | -9.58182 | -49.67315 | 2025-10-28 04:44:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fefd0d57-f44d-3965-b781-f93045708eb6 | -13.787 | -44.3456 | 2025-10-28 04:44:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3db5eb63-d7c2-3139-8bb1-366310fbfc82 | -10.92501 | -50.27631 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40df7dc3-1d52-3fe7-94e2-da13ad2b29e3 | -11.02803 | -47.79995 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 825d6bbe-a39e-37f5-9016-adbc755e33ba | -10.56737 | -49.79656 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e86e13e0-150d-3c0f-b52f-38c5e11b43c0 | -15.16051 | -46.58426 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 318373ab-63d0-3593-b701-703532af1bb3 | -13.9166 | -48.47916 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2651ea0f-08a9-3692-acec-d149a2922625 | -11.16032 | -47.78087 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 243e6cb6-e843-3d0b-90bb-789cb1c9a263 | -14.81103 | -46.71144 | 2025-10-28 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f65611a6-5e16-37cc-8d29-8e3120cfe274 | -15.5801 | -43.20042 | 2025-10-28 04:44:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 4dc87078-5cac-3ca0-b226-882f0569b320 | -11.51119 | -44.00229 | 2025-10-28 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README60.md)
