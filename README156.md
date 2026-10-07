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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e45b1ec-21c5-3f7b-a47b-7fd989cff3c6 | -11.62755 | -43.67282 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 08c5bdb0-7f9b-3589-b95c-629754be0a8c | -11.84756 | -43.55524 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f006bb1c-5c93-3ac5-af2f-36507c4d0106 | -10.23168 | -46.66452 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 68c4cb73-9305-3a5d-b1a7-24ae30fdff7a | -11.23204 | -44.86087 | 2026-10-07 16:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 3d1c37a1-518a-3a85-a6a5-0dc33c0e133a | -13.47516 | -42.47523 | 2026-10-07 16:01:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6974580f-d740-38da-b572-c6f5c599414d | -9.44149 | -44.60569 | 2026-10-07 16:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 38b228c9-7c6a-33cd-af5f-42f42705c1f5 | -9.35108 | -45.43505 | 2026-10-07 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6132cb44-0b99-3d94-80bb-15e85a4500e2 | -12.17989 | -44.76392 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 510.8 |
| edd69a6b-a3fd-3fa5-8fcd-f30098025da3 | -12.20556 | -44.65401 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| d2dfcd5a-1bbb-3ad0-a768-bdee9262cee1 | -8.46091 | -36.82555 | 2026-10-07 16:01:00 | NOAA-21 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 6945d088-0f77-33ea-9d6d-21016db032bd | -9.35042 | -45.43004 | 2026-10-07 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 2eb28f56-2a53-3f70-88fd-1385890dcbde | -11.22789 | -44.86713 | 2026-10-07 16:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 20567e0a-63f8-3fdd-9739-4d849b891da1 | -10.96986 | -45.39845 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a1d0b0da-54b4-383d-9d10-8afef5ad6914 | -13.97539 | -42.50487 | 2026-10-07 16:01:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a7d50aaf-4df4-3ca3-9a71-cba9cb74d3b7 | -11.14641 | -46.11647 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 23470e52-ee45-32db-9063-266ff31e35c2 | -8.59571 | -45.66848 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e29f3474-b0e6-3d26-89b6-ea62e79a54a9 | -11.38069 | -46.69542 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 197dd41a-73bd-30df-938b-c884542555da | -9.96587 | -43.56236 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| bd5e0d6e-9c8a-32cc-84f7-b038ff3e13b7 | -9.80108 | -48.92424 | 2026-10-07 16:01:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8fb848c1-e67a-30a7-8375-cbef8a8fdf4f | -9.78725 | -41.71102 | 2026-10-07 16:01:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8c0ac01f-6d67-32d7-823a-8945308c902b | -10.85482 | -50.69558 | 2026-10-07 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 51853807-8bc6-3828-9406-cb45c1cad296 | -11.07065 | -45.6358 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d6382fa6-acb3-3301-a92f-c822196efb03 | -8.78718 | -47.58512 | 2026-10-07 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ef2eed6d-c205-36c6-8923-43b9a725c1e0 | -13.50045 | -43.47957 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ea27369a-1176-35c7-b0d4-05c91b60b840 | -11.14066 | -46.1136 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e039fccf-ece2-31ba-8638-f1385a613fad | -11.86024 | -48.03721 | 2026-10-07 16:01:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e54c9d1c-cdb0-3fa5-8ea4-2bff6b83587b | -12.19672 | -48.41835 | 2026-10-07 16:01:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3f8151cc-a5c8-3ed7-be40-8a852b20f54d | -11.63061 | -43.62685 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b3c8d978-1f1a-3bbf-87ef-d7e02f1ee43a | -8.90091 | -47.59388 | 2026-10-07 16:01:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d567c6bf-924c-33a0-b8ec-6eb8d53a8f5e | -11.85081 | -43.54482 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d091ffb7-5aca-3259-a5ca-d135748a1a1f | -11.09487 | -47.62732 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f5cdcdc9-63d1-342d-af0a-0246301319da | -12.1883 | -44.75158 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9d6114b8-cdf1-3c31-bc71-4f260fd447f5 | -9.951 | -43.55131 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 224.1 |
| dd86866e-e30f-3689-9f18-81d713870752 | -13.02097 | -47.19302 | 2026-10-07 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1342732c-ae29-3ebe-9cf9-62fea83caaa0 | -11.15707 | -46.11551 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 552d8c60-8c70-33ab-a93b-37622f14b901 | -10.46072 | -46.83606 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 96ea541f-112f-3866-a648-fb78c9a87c26 | -11.73682 | -43.65172 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f7135cc0-3fa4-3f41-a282-5c25528fcacf | -12.22145 | -44.7184 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 033ca175-7f25-3330-a0c5-8661a6a1b8ef | -13.54988 | -44.78926 | 2026-10-07 16:01:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1de24110-5d00-3e2b-ae38-b937a0744cf2 | -11.38611 | -37.62543 | 2026-10-07 16:01:00 | NOAA-21 | UMBAÚBA | SERGIPE | Brasil | 2807600 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 3c84edd6-5e86-311f-a029-4c5ec1e587a6 | -9.16864 | -36.04316 | 2026-10-07 16:01:00 | NOAA-21 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 1275bab0-fe30-3b50-8711-d21a936810ce | -12.21963 | -44.68586 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ad257bf4-8fee-306a-8d77-75223a50cc21 | -11.22303 | -44.86793 | 2026-10-07 16:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3240835b-527b-3ee9-b3a1-fb6c5e3c706c | -11.0457 | -47.91072 | 2026-10-07 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69abc6f9-cbe9-3a43-8fae-a6ceda3118e9 | -8.6243 | -36.65118 | 2026-10-07 16:01:00 | NOAA-21 | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c63dcdd7-31d2-3bee-8688-37aa86f00811 | -9.95659 | -45.96759 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| bb4f6080-28e8-3cb2-8162-bf60a8864b01 | -10.5191 | -47.29011 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 65e81920-1b8c-3468-884e-6b9ba73db4e8 | -8.99432 | -45.94277 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| da0d96ee-6d1b-3df5-b305-75d4e19d59f0 | -12.6123 | -38.9122 | 2026-10-07 16:01:00 | NOAA-21 | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 56d26d82-ddf6-311c-b7a2-4c637e2d97e8 | -11.11619 | -45.70683 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 293a6bfc-bc77-3049-9673-10ec07d094f9 | -9.34612 | -45.43552 | 2026-10-07 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 2f10eeb2-7bda-34c6-b2bb-e764006d525b | -11.09891 | -47.6184 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 3a46ba44-0d2c-314b-a929-deb7c2ba5a5d | -12.17427 | -44.75896 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| a5e19731-a694-3f10-9746-e73f1dfb3a3f | -12.20627 | -44.65949 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 609bfb6e-54b9-34ac-b8f9-6b15a4b3b7df | -13.69099 | -49.10138 | 2026-10-07 16:01:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 09e473e0-2b13-3604-963e-5cfb275f08ac | -10.52662 | -47.28189 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8fc06c1a-d0aa-3574-86c2-de93fbd482ca | -13.11756 | -43.48296 | 2026-10-07 16:01:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e63cb729-65bd-3541-9c8a-4e323585faf7 | -11.09434 | -47.62312 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| c06a79d5-4525-3c1e-a28e-7dff6ed8dc63 | -8.64618 | -44.87547 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1a1a2339-8bce-3ca8-aade-c171a71ced07 | -8.97658 | -37.32878 | 2026-10-07 16:01:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 13.1 |
| eb9a7c6d-699b-3d0b-a3e1-9e5e450142ae | -11.14682 | -46.11976 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 8a1360a1-da0a-38db-8006-96126bce22d3 | -7.78118 | -35.37128 | 2026-10-07 16:01:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 7a69871f-e115-3b98-a7fc-df0cdda454d6 | -8.18205 | -36.69374 | 2026-10-07 16:01:00 | NOAA-21 | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a6497d7-887b-3a67-b2fc-3489c091c3e8 | -9.20669 | -46.70354 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1ef97d8e-ff9f-37c8-a150-e1a0f65a4331 | -9.58097 | -46.20995 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 34257763-d8d6-3fe4-877c-4dbd5c9db19b | -12.20321 | -47.12667 | 2026-10-07 16:01:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2c9c406-b0ea-3968-b6f7-4f9ca58b06e4 | -11.36291 | -42.27245 | 2026-10-07 16:01:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2e7926fd-55fa-3de1-9a49-a5b4ce792962 | -8.79572 | -47.21826 | 2026-10-07 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d6f0db03-18d1-3a7b-9f98-360c2b41addb | -11.84247 | -43.55115 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| fb62f468-ef9b-37a6-bb29-b15b6f0d3232 | -8.80091 | -47.21595 | 2026-10-07 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4a46026a-bca9-36f2-9529-4c5affb8132f | -9.97197 | -43.5745 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 721496ef-2a5f-360c-850a-67f2b9a91487 | -11.10652 | -47.5828 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 908f1e78-0a71-302b-9f06-c698036df8dc | -14.08272 | -43.76986 | 2026-10-07 16:01:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 11f23d1b-5695-34fb-a11f-b697b9f9352a | -14.58292 | -47.53259 | 2026-10-07 16:01:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e314296-aeb7-372d-9e28-0412c1e1a05a | -9.64627 | -46.09325 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 66bbd3e9-f76a-379f-983b-e31b0fdd9af9 | -11.1154 | -45.70059 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 4c561cd7-6293-3b70-9f0d-8468b27d5b61 | -12.20298 | -48.41776 | 2026-10-07 16:01:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| a54cdd48-92c4-35a5-8a68-8269a0204525 | -8.58294 | -44.86783 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| f1b47661-1e3a-3023-b62f-17b4b0c20fe2 | -10.34542 | -46.24674 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| eb2ba811-0ff7-36ec-bcf7-c3b26f3e5535 | -9.92175 | -44.80474 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 7ca3f2e7-7999-3e61-af8b-1ea4804b06bc | -10.13107 | -46.00062 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0c808429-64a4-3f8e-b900-1d388e1b3ac9 | -12.17357 | -44.75336 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| b1739906-d00e-30a9-9a5c-6da0d139917a | -10.87907 | -47.60438 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 61924543-38b2-3f29-9a0a-a9cba3e55382 | -11.71088 | -43.66434 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 6d5d0b4e-2895-3808-9a49-f75067b71f56 | -7.05625 | -36.25231 | 2026-10-07 16:01:00 | NOAA-21 | OLIVEDOS | PARAÍBA | Brasil | 2510501 | 25 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4414a0c2-3c75-3438-96fc-445a2717b7a6 | -12.16937 | -44.75959 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 9948732b-d8ed-3680-8be2-e704d264b15b | -11.14426 | -47.30103 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 409c749d-400c-38ac-8f0b-fdef31e2092b | -12.04581 | -43.38705 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c3ebeda5-05ab-3226-9cf6-036aa6918613 | -12.1841 | -44.75773 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 5ef51bb9-4967-3ed4-91e8-d61f1605866c | -11.11421 | -45.69123 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0d0948dd-c55d-3fe5-b047-18d7284f64e4 | -8.14255 | -36.06402 | 2026-10-07 16:01:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 85a5369a-4c14-35f7-b0cd-1a4fa30b01b8 | -11.04875 | -45.80966 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e77b8843-9772-31b1-ab1b-442fa4cce167 | -11.12029 | -45.94955 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1f739fb9-0b3b-3550-8ac0-12bc5fece7a1 | -9.92319 | -45.74914 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d4a2781f-dcdb-3799-bcbe-163fbfd8d4bf | -9.43796 | -45.82083 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ed079770-e1fa-3fd8-8d56-f4c51c4698cb | -9.61751 | -43.12583 | 2026-10-07 16:01:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 28d94342-b84d-351c-b137-9072ad92ec60 | -11.00095 | -45.48005 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b37bcc45-1bd3-30f3-a994-e6ddd8e30c51 | -11.10069 | -47.58355 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d642518e-927b-3d49-9366-fdf21b310096 | -11.71148 | -43.6689 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 11d2786c-0c9d-3be6-a494-b1288dc5ef8b | -11.38009 | -46.69226 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |


[Clique aqui para ver as próximas entradas](README157.md)
