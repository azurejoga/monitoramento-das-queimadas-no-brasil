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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8846c9ae-e72e-3aa2-8103-2d203163b0ac | -4.11115 | -50.4446 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11e0792c-8a43-3590-b7a3-b73d9ce81560 | -2.61624 | -54.01466 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5471b6b-5bf1-370f-bf27-078f568266d1 | 0.62022 | -60.08783 | 2024-11-09 04:55:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dd43c609-811e-3e1e-872f-a1f455757259 | -3.24846 | -53.39769 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c88ad1-905d-3f2b-916b-97d165d697ed | -3.05001 | -50.37452 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 302c3fc2-48f6-3afb-8ccd-e478fade20aa | -2.10959 | -50.84646 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e138df6-a5dc-3755-948a-d206a8edc54e | -3.34531 | -50.36232 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e7095da7-d7e6-30ec-9f39-a240695a46a9 | -2.80363 | -51.48217 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60379963-d2e3-3f13-81c9-d94a13d6c69b | -2.23484 | -53.77332 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 6b7cc450-8c69-3326-8af5-e260fe484954 | -3.97908 | -46.16978 | 2024-11-09 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fcbc3338-4eaa-36fd-b775-adc5896e9999 | -4.13955 | -46.90274 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6efaa0a9-f46d-3a6c-a60d-ae1a1072083b | -2.54833 | -47.1251 | 2024-11-09 04:55:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d421759-5e1e-39ab-9883-4d06830b666f | -2.15099 | -49.13572 | 2024-11-09 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 265ade29-f58a-38b6-8b3c-e3511a46e368 | -3.10649 | -51.13027 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b71e24f-24c9-3a49-a38e-83116031cf2b | 0.69662 | -51.44056 | 2024-11-09 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93d7be69-9908-355e-80ba-fe02fd9a886d | -2.96086 | -48.0208 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d09f34f-2839-3235-a998-4058c68c280f | -3.23429 | -51.18806 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5ff5a6a-8fc8-32c9-88b5-277e17720bca | -2.32089 | -50.57272 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c755796-ac05-31dc-b415-bc5996f9fd5e | -2.23476 | -53.73065 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1788df3b-a66f-364c-a592-3fe53dbb4b7c | -2.86228 | -49.22372 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 856e4b61-f725-3783-a9ef-921aaab63ffd | -1.50855 | -54.52106 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 398c232f-3f7a-3984-a937-41686125dd28 | -2.11656 | -50.84754 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea923f8a-ff1c-3a29-86e1-44c948eb1f5a | -4.11375 | -48.50199 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95b73cfb-5477-36aa-a0ac-8f4780cf2692 | -4.19791 | -48.5505 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad2c95ff-d2eb-3567-8287-998c792a6b68 | -1.33984 | -51.42108 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76334908-4f1c-3f41-8ddc-47052c9776be | -2.81892 | -46.64483 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bce7d64-6d4f-30f2-b073-17d1096fb442 | -3.21352 | -54.05125 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 392df429-b7ff-37ed-8c89-9fc4e0ec1938 | -3.66849 | -49.95282 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1851226a-ce9f-34ae-8b62-3a5f7faca776 | -4.62643 | -46.54024 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17dbfd2a-b35a-391e-b453-a565bb2607ec | -3.21853 | -50.38621 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a191da2-22bb-358a-ac76-ea48f88f367b | -2.95094 | -46.75375 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 600f899b-6e91-3d08-bceb-155acceba9b1 | -3.02372 | -51.22978 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e951e2ab-6fbb-3208-b720-658fa43852c1 | -3.01241 | -53.43516 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 494c782e-69ea-3f81-8fad-0c0a0937e6ba | -2.68502 | -51.81794 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 734d9ce0-b72b-3001-8559-5e7087eb37c5 | -2.67092 | -51.81943 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beeaf4fb-686d-32e4-a80b-9f1b3bd75cf3 | -2.10686 | -51.09359 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c75adffb-117a-37b0-a3f9-551a0bd8b303 | -1.34041 | -51.41747 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0924e79-5ef0-3b62-a6ae-fecd2b61eab9 | -10.70007 | -45.04187 | 2024-11-09 04:57:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5265d56-5e21-3ab7-b389-8fb915df3041 | -8.85524 | -47.67068 | 2024-11-09 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69bee803-36b4-3c45-80c8-e4a30b44478d | -10.52746 | -49.35691 | 2024-11-09 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd65d189-e500-3941-ae46-212143702acc | -11.26223 | -49.9357 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd8ce809-c62f-30ea-9a0a-e1442073dc30 | -11.08211 | -43.33703 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 48e497c5-a5ce-3ebb-8311-d655e6547b85 | -6.62833 | -62.91804 | 2024-11-09 04:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a73efcb5-a1e8-33f2-904d-da7d6467bc37 | -11.63894 | -42.01202 | 2024-11-09 04:57:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3771af36-4ede-3f4b-84e7-c1ee58fa8992 | -10.53196 | -49.35636 | 2024-11-09 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 682d0782-1035-3b8a-8cd6-4ebd6e7874c7 | -11.08454 | -43.34063 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 10dab274-5be3-3b0f-804e-742d635a0a55 | -11.10416 | -43.33801 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 397e034c-b119-39fe-a2b6-75b90d44d401 | -10.72824 | -49.82697 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cbffbd1-2308-3e03-8179-af839b3bca43 | -11.87189 | -58.82168 | 2024-11-09 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14854938-889f-3ed2-850e-711597950384 | -11.08908 | -43.33269 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4c49a46c-acb2-3628-bfef-841ad4034180 | -11.08275 | -43.33183 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| e2c274bc-b7a8-3c72-9297-1af92bc14205 | -8.84868 | -47.68427 | 2024-11-09 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f74f36de-3470-36b9-baf9-1349c76b6fe8 | -11.09478 | -43.33873 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 975a703c-c92e-3fc1-a3a4-681dcd91d6d6 | -10.70054 | -45.03809 | 2024-11-09 04:57:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a270593c-29d5-30c3-b1d6-6f8a8d999aaf | -11.08513 | -43.33546 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0a22f39e-a79a-349f-bc94-31efcd47a616 | -11.26172 | -49.93938 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d9b3f4d-9e58-3196-82a7-e4baeb8aa6bd | -8.85329 | -47.68494 | 2024-11-09 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2dfc168-6fe0-3a2d-bf81-6f9e04ab1cd8 | -11.08781 | -43.34306 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3fc57685-cf79-3778-94b5-f7df3395e5a0 | -11.09147 | -43.33632 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a593c352-701a-3a88-ae8f-516ac4ada868 | -8.84932 | -47.67959 | 2024-11-09 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b66887b9-3347-38f5-80b0-56c3a257b24a | -11.59149 | -50.90015 | 2024-11-09 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adaf3348-cec5-3717-a562-a515a0807d1b | -6.62778 | -62.92119 | 2024-11-09 04:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddcc9b19-8cf4-3311-a636-7bbcb7e09069 | -11.581 | -49.7801 | 2024-11-09 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24889b5f-2d17-30b4-8f1c-1916516c1897 | -11.08573 | -43.33025 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0443ce3e-bfa9-365f-90ad-b038bc8c9dcf | -11.09087 | -43.34153 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1a78a8ac-af6d-3ec3-b7c1-e7e68a1edc30 | -8.84739 | -47.6937 | 2024-11-09 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85091248-0c7a-3cc5-acf4-0505734e2cbc | -10.73103 | -49.53262 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 29c9ade3-dba8-3c9f-9332-0027ffb21b6b | -11.5929 | -50.89802 | 2024-11-09 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cca3dc5-afe5-3f46-8e24-6f630e3c541e | -11.63901 | -42.01075 | 2024-11-09 04:57:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 592daa81-6a89-38aa-9ab6-042d47cde350 | -11.0782 | -43.33975 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| d587cd3a-821c-34e8-917e-d954a0e2b2ff | -11.08148 | -43.34217 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| ef1b486f-d082-3244-9f44-16c0cb9a4917 | -11.36447 | -49.79372 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20ab1729-fc69-3e11-9b9f-c3c7c24608e1 | -10.43071 | -49.24662 | 2024-11-09 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be0a9327-626e-342e-9038-424e182f8e33 | -8.85392 | -47.68027 | 2024-11-09 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17215033-59b3-3c0f-a341-f00c0fcba993 | -10.73155 | -49.52879 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a14e699-d8b8-35b8-a84a-dabe234ec76e | -10.0429 | -50.58475 | 2024-11-09 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fdb3e22-537f-3a0f-a956-91203b42d16d | -10.98643 | -51.46575 | 2024-11-09 04:57:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f808b0e-1c9c-3390-bd95-a6b35eed49af | -10.73234 | -49.82756 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1b850aa-a01d-3158-8f58-56a23ce1d529 | -7.29745 | -55.31451 | 2024-11-09 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ff9c5e3-f44e-34fe-8cf0-c21ddf3647f3 | -11.63823 | -42.01824 | 2024-11-09 04:57:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 957ac947-69b5-36d8-8127-3651dc3e641b | -11.09415 | -43.34392 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f082d7c9-3765-3ca5-9ed5-1432d78fba3c | -11.10113 | -43.33955 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c3698766-cf0f-37bb-95bd-7e0f6685c2b9 | -11.08085 | -43.34733 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 2244e102-356b-3aab-8f68-2e11f8de22c7 | -11.86885 | -58.82303 | 2024-11-09 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc27ce99-e3b5-38da-adfe-65282d7ee84b | -10.52775 | -49.35573 | 2024-11-09 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55dfde2f-6c22-3f80-9835-c443ebf9be87 | -6.62805 | -62.92212 | 2024-11-09 04:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec0db408-bb07-3441-a31f-1a423ab08c5e | -10.8999 | -44.70674 | 2024-11-09 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c9c97c9-504c-3e58-9825-8c09a19f17c3 | -10.89408 | -44.70615 | 2024-11-09 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbc4b5bc-126b-3cac-ae46-9022e8ee595e | -6.62861 | -62.91896 | 2024-11-09 04:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09357a65-7783-3ca9-a2a5-c0733bdaa027 | -11.08845 | -43.33789 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f4a64500-27bd-36e0-892a-e1d3591673a4 | -10.66854 | -49.42228 | 2024-11-09 04:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5e21a8a-798a-3b48-9427-10469a861380 | -11.87251 | -58.82374 | 2024-11-09 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 948cd389-8ea6-3634-9556-dd8a38d9e581 | -8.84804 | -47.68896 | 2024-11-09 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eccaab01-7640-3101-9746-9341f9d37c50 | -10.72414 | -49.82639 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 262978ce-f3e6-3bf6-8dcf-5b7321a88a40 | -11.08718 | -43.34823 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| d3bace1f-f616-3dcc-88bc-9c09a0a5a0d3 | -7.29688 | -55.31806 | 2024-11-09 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5bf753b-c43a-34db-b3ee-4572f28e4bbd | -11.55819 | -49.91539 | 2024-11-09 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e53897e-cab6-3f89-942e-f87fe5fdf695 | -12.11115 | -51.39999 | 2024-11-09 04:57:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7443e90b-b465-3839-91e8-2addfcbb95d0 | -10.7305 | -49.53644 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 26dd3d38-5e93-3221-ba47-682e7b1e9f65 | -11.36861 | -49.79431 | 2024-11-09 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README100.md)
