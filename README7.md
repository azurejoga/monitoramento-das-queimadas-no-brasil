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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b72352d5-3dff-39e0-ad88-003d5014bdd9 | -5.48426 | -42.15648 | 2025-07-29 03:28:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cfceebd7-a8a6-3328-ab16-9e9d8a279eb4 | -3.8262 | -41.56142 | 2025-07-29 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9c114ecc-f14e-302d-aed9-039f4fecc4c9 | -14.3796 | -59.3333 | 2025-07-29 03:30:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 34c3f725-e9bc-3400-922c-e8bd8baef0dd | -14.3988 | -59.3316 | 2025-07-29 03:30:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| af8664f9-3bd3-37bd-aa36-a0a033e50cb9 | -11.4197 | -45.1412 | 2025-07-29 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| d0d7d943-06eb-36e3-8936-faa030ed20d0 | -11.4393 | -45.1154 | 2025-07-29 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 1c10ce10-63b8-3d7a-96b0-ee9f511a37a0 | -8.9475 | -46.7577 | 2025-07-29 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| ad4b262b-c531-3e85-bded-25cd8272fe18 | -11.4389 | -45.1385 | 2025-07-29 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| f9fb4301-c319-3cc1-a4d2-434a8dbdfb9b | -11.7508 | -48.1825 | 2025-07-29 03:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| bc327521-9dbb-32b5-9756-9383d06ec0ac | -11.4201 | -45.1181 | 2025-07-29 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d99b8557-efaa-3953-8d99-07b389a5c9ad | -11.27068 | -44.65083 | 2025-07-29 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c09053f-6ac2-358a-b3d6-45ceaf97cc6d | -8.94329 | -46.75092 | 2025-07-29 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7b51c892-721e-3558-b3d0-12d747e7b0df | -10.62586 | -45.22943 | 2025-07-29 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a52874b0-c2a6-373a-abbd-1c4885497c67 | -9.5157 | -40.35526 | 2025-07-29 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 79e20d1c-efd5-35c3-aa3b-7ad4ea1d7b9f | -9.65127 | -40.58717 | 2025-07-29 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bc429de3-e674-3c87-adf8-e517131dde23 | -7.55051 | -44.43896 | 2025-07-29 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 354fc008-a6fc-333f-b947-5ee9a49afa05 | -8.50901 | -43.31715 | 2025-07-29 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c38d17bd-6970-3511-990a-b79d2e4e815a | -8.50979 | -43.31293 | 2025-07-29 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 140d0e63-7146-38b3-beff-b895d62983e1 | -11.42265 | -45.12557 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| dec61256-1131-3111-820d-35761e465e1b | -7.54521 | -44.43198 | 2025-07-29 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27f3037e-2ebb-34cb-9305-8a8bf7c4ac36 | -12.57866 | -41.28838 | 2025-07-29 03:30:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b7c9c85-aa38-379f-ac97-3c670f3ce02a | -10.51853 | -42.55709 | 2025-07-29 03:30:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1cfc8d99-27fc-3b3a-9c17-ba32e9b1c2ff | -8.95731 | -46.75476 | 2025-07-29 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9a4976f-ab61-3818-a9e1-3fe4cd740db5 | -11.99716 | -46.95341 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c4fd27c-9a94-39b9-898e-6c22f78a0a61 | -11.30219 | -39.17699 | 2025-07-29 03:30:00 | NOAA-20 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5192812a-ad32-3512-bac8-fe70949f3168 | -7.09937 | -44.38272 | 2025-07-29 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7d413cc4-ea4b-372a-aa65-d594599cfe36 | -12.00255 | -46.9635 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6b74586-720e-3901-8f1a-461e4fae861c | -7.91861 | -44.08402 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbb0024b-7484-399f-9553-9692d56d8b76 | -11.42672 | -45.13741 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 888ec077-4f43-3172-a839-043929983259 | -8.28815 | -45.00699 | 2025-07-29 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5461386-51f5-31cf-b712-c90292702aa9 | -7.80041 | -46.57292 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c5c45b5-cddb-3b5a-ab77-f2f180f09994 | -11.42316 | -45.13513 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| f906dbfe-9516-34b1-8095-2dc367035ae0 | -9.35996 | -45.74243 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 777dc098-2085-3572-9864-192ab38250a1 | -11.99297 | -46.97491 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d3e884e-8db3-3c2a-8876-8df4fbfacbcb | -10.62793 | -45.23016 | 2025-07-29 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb1a8175-0a35-39fa-9bc2-8ab7494f2936 | -9.36401 | -45.73756 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4391bfcc-5ddf-33cf-a355-d51ffc193499 | -8.28918 | -45.00156 | 2025-07-29 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 382e88c3-1af8-3e2d-b20d-e9e7a31417ff | -12.00116 | -46.97002 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44d83529-f5dc-3498-94e8-f2019336b490 | -9.51194 | -40.37587 | 2025-07-29 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c0878c6d-0a45-3edb-9767-c22e038c4094 | -9.22767 | -43.15439 | 2025-07-29 03:30:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab7c443e-825b-3dd2-905c-ccd9092eabd9 | -11.27039 | -44.65539 | 2025-07-29 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 474d55d4-cf4f-386f-92c0-6446eb55391d | -11.42992 | -45.12161 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 76aca268-042d-3eaa-aa00-6968a628d40c | -12.57765 | -41.29367 | 2025-07-29 03:30:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f48eb709-8ed0-3cba-9e2a-9db01f34ef90 | -9.511 | -40.38107 | 2025-07-29 03:30:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bdc3b80-c039-343f-9657-f1e688abfbd0 | -7.92896 | -44.0881 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e422a07-8cc0-3d05-848f-efb9c63456cd | -11.42525 | -45.12439 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f463c14c-9a60-320c-b84d-685e8ce4f241 | -9.33235 | -37.98502 | 2025-07-29 03:30:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 42382c24-c8d0-3dc3-b43c-0f9bf7359736 | -10.51919 | -42.55366 | 2025-07-29 03:30:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5914e2fe-55b9-3601-a903-72e0e9d654d2 | -7.93607 | -44.08448 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1a219ea-59a3-304a-8fd5-9f2565234f22 | -9.86755 | -44.6946 | 2025-07-29 03:30:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64360d86-c221-3a51-96ff-42422bcea48f | -9.32892 | -37.9807 | 2025-07-29 03:30:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4701c310-e86f-3546-b884-cd241f2110a1 | -11.99714 | -46.95535 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 366f4f50-d244-35ca-813f-c8a54e63be9f | -8.95348 | -46.75295 | 2025-07-29 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b4a1634c-10cd-36b4-8358-b676251fde09 | -11.4289 | -45.12666 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 8b5fa726-d0aa-3403-b556-a45d3da96483 | -8.51486 | -43.31827 | 2025-07-29 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 22f70fb3-42e2-31d0-8ab0-821aca843328 | -10.62485 | -45.2346 | 2025-07-29 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e8e3f6c-4688-3fcc-a7af-dee76705b015 | -10.62689 | -45.23529 | 2025-07-29 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d6a1b3b-60c6-3dee-b4db-882e5a97afa5 | -7.93091 | -44.0868 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dd4751b-db5c-3893-ae1d-586b2d5d9eb9 | -8.94899 | -46.75954 | 2025-07-29 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 22fb1a35-9c04-38d1-b774-8eb78a5e2067 | -9.86922 | -44.69691 | 2025-07-29 03:30:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58f3966a-725d-30fe-b886-eaf919d5bc2c | -9.36453 | -45.71873 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90ab914b-ea5d-36da-9e7b-d2649bf8459a | -11.43407 | -45.13307 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10846f03-bcab-3ce7-bbe2-2dc057ed59b6 | -7.93428 | -44.09381 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 740035f3-05ba-38e8-8e8f-406efb328358 | -8.9394 | -46.74948 | 2025-07-29 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a0558fad-3027-37ad-a021-0dc9c7ba5309 | -9.40196 | -45.48874 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3200c088-d36d-3231-9dac-1a64417325ac | -7.79896 | -46.58028 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d63002f3-f2c7-3db3-a6bc-f72eb6a65e38 | -7.9352 | -44.08905 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c37e871c-5df8-3b53-890f-d27744bad05e | -8.95032 | -46.75275 | 2025-07-29 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b600fff6-0064-364d-b701-65627597b03c | -9.36339 | -45.72463 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 775d7929-04a8-33b4-8ee3-f9cb10c66790 | -8.94516 | -46.75758 | 2025-07-29 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| aaea978a-3609-3bb3-83d0-0fc473cad2dc | -7.93628 | -44.09245 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 463cbea8-bf4a-307a-8016-8ad7d806829e | -7.91772 | -44.08881 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 882909ee-f8b9-3768-9040-e0cb4d925c47 | -11.99978 | -46.9765 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d291522-95a3-339d-8bda-7b304258acab | -10.51985 | -42.55022 | 2025-07-29 03:30:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ebad4764-3434-3a26-b57c-fdebb67f51a3 | -11.99581 | -46.95995 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e6a704f-76d4-397a-a3ca-223341708000 | -11.99311 | -46.97305 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74ee66ee-ad2c-3fb0-902c-5591003433f6 | -9.40085 | -45.49453 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a34507ca-05c8-36bd-94e6-ba3a32dc6734 | -11.42783 | -45.13193 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 98058fb3-3867-3cf2-98fa-4ff53b917269 | -7.93005 | -44.09143 | 2025-07-29 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b130ee13-b6c5-3a68-a46e-e2ae5e2a80c5 | -9.87373 | -44.69599 | 2025-07-29 03:30:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 645d4acf-6f47-3869-bea1-0f967150668e | -7.54704 | -44.43281 | 2025-07-29 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cca7745d-f132-3418-bcbf-d6d284bbf044 | -9.22691 | -43.15835 | 2025-07-29 03:30:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 804d818a-3cd5-3aff-9458-aa6b236ef821 | -7.80615 | -46.58151 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c54cd04-c36c-3be5-9112-3e811e131a99 | -8.9521 | -46.75983 | 2025-07-29 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b6c11f97-0b36-338c-8c6d-533ba0a36d00 | -9.39873 | -45.4947 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| da88d0bd-ea54-30d9-a782-0933a1ad289f | -8.51388 | -43.31628 | 2025-07-29 03:30:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f0ff28cf-3546-31ba-8674-5b7e1a4deb76 | -9.8702 | -44.69179 | 2025-07-29 03:30:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a8fa423-71c6-3c23-afb6-ecf57584b092 | -9.36111 | -45.73643 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8685aedf-6e82-3a2a-a39f-d2e3a9590c08 | -9.39988 | -45.48896 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4867e3fc-4ef7-38b4-9f47-426434206dce | -8.94651 | -46.7509 | 2025-07-29 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 150174e5-c7fe-35cc-bc80-de300d97c493 | -9.33297 | -37.98143 | 2025-07-29 03:30:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07458f81-21eb-3cb7-8a1a-0d3877210e30 | -11.99992 | -46.97468 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7335e2a9-6279-3cd8-858d-0df60f6bcb22 | -11.27135 | -44.65065 | 2025-07-29 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 780071fd-f6df-3b61-8e1c-fb0e702b3050 | -11.42423 | -45.12963 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| bdb6eef0-4502-3fdc-af2c-0a41f3eeb144 | -11.24092 | -40.97712 | 2025-07-29 03:30:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2c6dcc18-47bf-3c2d-8d0e-ea1fd7fc185c | -12.00126 | -46.96816 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 28ac94de-23ac-3736-aef5-c1856fd4e8f2 | -11.42157 | -45.13089 | 2025-07-29 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 7d09c947-d172-3a2a-a1ed-a26cabc4ffd5 | -9.39221 | -45.49316 | 2025-07-29 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| faadf961-a7b8-3ee9-ba11-16180eae05bd | -11.99575 | -46.96188 | 2025-07-29 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7f3373d-0d7c-3007-b559-9a436782206e | -12.57822 | -41.29219 | 2025-07-29 03:30:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README8.md)
