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

## Dados Diários - Página 213

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9abd0fb-65b6-364e-ac05-cd06afedf3df | -7.21413 | -44.29475 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2fa88628-28f4-3b89-bc98-52b850061815 | -5.80045 | -50.05775 | 2026-10-07 16:37:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 53a883da-cb05-3281-b937-fab4b0c09daf | -11.14428 | -46.10328 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a0dbdb60-e576-32b0-a040-3d51878995df | -6.93874 | -45.29096 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 430b6b03-5b16-3697-8307-64b5f17920d1 | -5.96962 | -40.95171 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 65a58cf3-8100-35b5-b7ab-7e74948718b8 | -3.94588 | -41.54823 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 51.9 |
| c4509e12-6687-37f6-b3ae-0d04ebb5c036 | -5.24742 | -50.90781 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6e1fc3e4-b350-3c1c-bc64-8b31e13eac5a | -3.89321 | -44.10857 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e1a0038d-dbad-356e-b490-dd9580898ed8 | -3.8803 | -44.13541 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fa150672-87f2-3d04-8a95-da486497718e | -8.98979 | -45.94257 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1c8b50bd-75d1-3376-82f8-961019205bbd | -3.77279 | -41.78326 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 44.6 |
| e86e6e5b-82f1-3fb5-bc74-aef53299524b | -6.47294 | -46.61572 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7047075f-68b6-3e41-a626-c7d85a243599 | -4.24112 | -49.98743 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 04ecb574-5749-3ef0-9f23-52898958c832 | -5.57211 | -51.08051 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb237757-4356-3252-b5a6-afd25115237d | -7.81863 | -44.57959 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7094ccff-7185-3f9c-91e1-e289f767faaf | -5.73903 | -41.7045 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 34ede911-c756-3b40-b0f7-51bbb7631850 | -6.14655 | -52.64548 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| cf2dca17-a578-3312-ad18-3d267f40385c | -5.42203 | -48.31341 | 2026-10-07 16:37:00 | NPP-375 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.1 |
| af9694c6-e2ac-39c3-b9d2-8c310dacbb19 | -11.15506 | -46.12741 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c6a42771-5791-3dd5-8633-4598cbf0161f | -14.90397 | -40.33156 | 2026-10-07 16:37:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 60f9d557-9ee5-3ce1-8f9c-1798c789f371 | -14.70752 | -41.27191 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7b4d6f5a-bf55-33f2-8e13-104ce07e5e28 | -4.84258 | -40.39673 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 26.9 |
| babe9213-5b2f-3f9f-9767-eea3726a75c5 | -4.81019 | -49.28065 | 2026-10-07 16:37:00 | NPP-375 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 53a19959-772a-3a98-8587-56279fb70e37 | -17.01933 | -45.90612 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 029da4a1-5f53-318b-8f0c-4b85d29b9fd9 | -3.19298 | -42.95971 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e6f1a2bd-5d0e-3530-8768-0379b008ca76 | -10.94851 | -45.38511 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 24f24db4-5ed1-3878-9fec-093a0f7bb466 | -4.51411 | -42.88084 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 89536ff7-f2e3-303c-8ba9-9ac26d1d30b5 | -11.00235 | -45.48528 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3ad3378f-9e6d-31d1-80a9-1fed621e16ca | -6.68452 | -44.96947 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acfa9708-0e9f-3350-b6c9-a757e1f88d5a | -14.8312 | -40.83599 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 21e65cfd-b345-3fd3-93f7-f3981a082c59 | -5.57667 | -51.07982 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0855dd99-a7e7-3f55-b086-a2ca69e64844 | -11.09662 | -47.62385 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5ff0b5df-51ad-386e-9ee5-128fb079bdee | -3.75795 | -40.83762 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| cf3720f6-7589-3823-b72f-c024c4d89cbf | -9.86224 | -46.31139 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a41a20b2-edce-37a6-b39d-0c711da4f57c | -8.64527 | -44.86297 | 2026-10-07 16:37:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3295b9f7-5b47-3117-8ad0-252b4724dc12 | -5.80242 | -52.36188 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| eb491983-6101-33ff-8c7f-9d25721dc1b1 | -6.67729 | -44.96694 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bd42abf9-dffb-3d5b-ac1e-724da12f88d3 | -6.49927 | -41.83186 | 2026-10-07 16:37:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| cdc1e6bd-8313-3444-8622-9115cfdc36ef | -9.64494 | -46.09544 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0397cdc4-76e1-30c0-9f60-9f6a2f46f4e9 | -16.10681 | -52.63821 | 2026-10-07 16:37:00 | NPP-375 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7c2d5aa-9e07-364b-86f0-ebac8ec8409c | -6.14696 | -52.6485 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 0e984b5a-ec49-3ab8-960b-3c1efc1c97ca | -8.06805 | -55.29132 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 10d836c3-ff08-33b8-bec1-a4dfa5957af0 | -3.85139 | -43.35833 | 2026-10-07 16:37:00 | NPP-375 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58faca4a-3246-3c22-b8e0-c2c4f634a0fe | -8.5637 | -51.23508 | 2026-10-07 16:37:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 79617a83-07ca-3983-8868-72f47ba58e2d | -11.15447 | -46.12324 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 27072e1a-b25f-3d78-b08f-84e094906a5c | -7.46948 | -42.83051 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 154.8 |
| 7f1270f6-1ae6-3d78-a615-a15d06776861 | -6.6836 | -44.94075 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f9a1a789-ee5f-36e5-a417-7ef31e88bdd8 | -3.90758 | -44.11349 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| b8a1d0ca-0f3f-3f35-8f0f-a52c87f384cc | -16.10248 | -40.79042 | 2026-10-07 16:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 565405c9-5f40-3c8c-a795-ee2574e8c0e1 | -11.38089 | -46.69638 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| faf7ba3d-2ecf-37ba-83e1-cb0db7d3bc96 | -8.02652 | -47.95838 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a0788bf-4daa-39ed-b361-954973ab3e0b | -11.05582 | -45.85288 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 47440b16-bc90-30a4-a0fb-a35a5a29f142 | -7.25906 | -35.0456 | 2026-10-07 16:37:00 | NPP-375 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2ff0425d-9741-3235-bbdc-97f168dc13fe | -5.81951 | -53.82982 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 11ce7f1c-18b3-3898-89ec-e92591746915 | -9.96747 | -43.57426 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 03eea150-65d1-3618-b6f7-91eb21367d6f | -9.61627 | -42.32977 | 2026-10-07 16:37:00 | NPP-375 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 39321738-1180-37c5-b09f-809ddb6c50ba | -10.52716 | -47.26573 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fbd42557-7914-323a-9baf-46724de37fe1 | -5.67822 | -53.49801 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d0368b47-4b03-3a62-aab1-b7594c032612 | -5.97588 | -41.35846 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 573fa986-c1fa-35dc-a795-e98243cf0563 | -3.56003 | -39.13235 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e7a2c48d-12ff-3534-a2c3-2d822ebf6592 | -9.17156 | -36.04104 | 2026-10-07 16:37:00 | NPP-375 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| b9a0fdde-f50a-3c01-a287-f8178e4d8d09 | -15.1043 | -44.08478 | 2026-10-07 16:37:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6bb2583e-5e54-3788-9ef4-e569d21dc9c2 | -6.57529 | -47.77185 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 532307a6-5b1d-3b83-8020-6ac52b582fe7 | -5.01042 | -50.94347 | 2026-10-07 16:37:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d8826571-7706-35da-b90d-71b57bacb266 | -15.60788 | -41.78065 | 2026-10-07 16:37:00 | NPP-375 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d2026cd9-4bf4-35d1-b48a-dd733c8f4152 | -8.98922 | -45.93865 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 93d73d4c-777d-3925-844e-3719c347c628 | -14.98911 | -41.66814 | 2026-10-07 16:37:00 | NPP-375 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ecb51ff2-4ec9-3c1e-adaf-57dac98dca72 | -6.17445 | -52.93114 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 946e87e9-e3fc-322f-b677-791074ef36ff | -6.58711 | -41.59297 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| bade301b-dcdb-3369-ad74-faa7373c07c1 | -6.14043 | -51.93203 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 3ec20b9a-1513-3879-b02d-ab38f9dd4899 | -7.9977 | -39.59134 | 2026-10-07 16:37:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 118.3 |
| e8986876-ed6e-3f5a-b455-ac51e617c4c7 | -9.63785 | -46.09653 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 0ec359a5-c26e-3b35-8a6f-f3dad2c8e7f1 | -7.21112 | -55.1201 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ff29b4b3-e28c-395f-9af6-85155e70069b | -5.7376 | -41.74078 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| bceca07e-2d48-3b03-8fd1-49c666d18854 | -7.06935 | -45.37085 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| beeed87d-ee0c-3158-be8f-88163a84fd70 | -4.70538 | -49.68579 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 545bef18-074e-34ce-8deb-38b3a82dbf13 | -10.19908 | -46.6937 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 24d2135e-e231-3fb8-8541-7a8c63d43a0d | -7.34579 | -45.28402 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ed974595-9b0a-34d7-b307-4d7bec5e9518 | -6.4682 | -55.47349 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 25db59ef-a0bd-3909-8f16-6a330cbe77b8 | -10.87853 | -47.6032 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 8100c160-7d06-3d7b-903e-5234a6b7390a | -16.41318 | -50.48921 | 2026-10-07 16:37:00 | NPP-375 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 00733fbc-6b5b-36e2-8324-e4fdc49ba490 | -17.01683 | -45.91647 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 07e4970b-9703-3719-bdda-6febdb6081ee | -6.40663 | -52.71764 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83c46e09-1159-37e4-9a05-5e8294377d36 | -4.08231 | -48.90519 | 2026-10-07 16:37:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bf3a0769-4087-311a-bd29-6a2360e51930 | -4.93628 | -40.55232 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 4f41f3b7-d490-320b-ab00-de42a0a01fb3 | -5.24292 | -50.9084 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c91e76c0-2ab5-3e84-916f-191c015bd4f8 | -6.98489 | -40.03556 | 2026-10-07 16:37:00 | NPP-375 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| fb7e3345-9190-3d94-8638-9a3db706a595 | -6.47703 | -46.6191 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| a4b60f9b-6f97-3ca1-9b26-640f9498397f | -6.64642 | -43.78445 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 813e5581-74c1-3b87-b20e-15ca26788872 | -6.66605 | -52.97451 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9b028532-8ae6-3ea5-ac86-4be2df86d1a9 | -7.26849 | -35.16051 | 2026-10-07 16:37:00 | NPP-375 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7e43a6d8-a4ac-3789-8280-f6e48d879f73 | -8.29572 | -45.4618 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8272c3ce-8dd6-38e6-8159-97b8ce239b86 | -10.97946 | -48.54147 | 2026-10-07 16:37:00 | NPP-375 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8c2a6e54-e3d5-37b7-9f07-f81f4b70cc0b | -6.52386 | -55.28276 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f2755760-081b-30af-8903-4d0db3b9c149 | -7.87633 | -44.22544 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5d57e701-8fdb-39d1-888c-84226f44b806 | -3.50255 | -41.95257 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 41d3fe00-8a48-363c-a2b8-9f5c4131da5d | -4.31357 | -43.00522 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 785d7b7f-d5ad-32ff-a4c4-a362b4ebbc30 | -7.00016 | -44.06526 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a6eb7b2c-8cf0-3cbc-91be-d73b7d3594c0 | -7.39771 | -46.2224 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a7566687-9fa8-3070-9486-b31a1fca7237 | -3.75368 | -41.70703 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |


[Clique aqui para ver as próximas entradas](README214.md)
