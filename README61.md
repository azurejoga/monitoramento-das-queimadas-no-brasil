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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80a1841a-10a4-3785-a641-164c4f23d557 | -11.87311 | -44.7773 | 2026-10-07 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c80cf569-5885-3c1b-8fa6-9857a1542623 | -11.04681 | -47.91014 | 2026-10-07 04:21:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3eaddb15-b753-320d-b854-f78c70bfe7db | -9.91465 | -44.80715 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0d64924-accd-37ac-8c14-e03de5cf0f31 | -8.24913 | -47.98875 | 2026-10-07 04:21:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f0e6a17-3d12-3c32-a0df-4ee62e1a8c75 | -14.78605 | -42.26665 | 2026-10-07 04:21:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd38138c-5ca6-3cfa-be0f-32ed156d4e3c | -15.38132 | -41.74195 | 2026-10-07 04:21:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6ad835cc-404f-3cdb-bc26-98142de45527 | -9.89301 | -44.81445 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3a71e01-1d08-36e9-9439-c24d751114cc | -8.70515 | -45.22097 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89826ddc-c94c-322a-a5dc-603a2ef80b33 | -12.2044 | -44.65868 | 2026-10-07 04:21:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d0ff819-0f3c-3f5b-9001-1f5e4a6fd8a9 | -11.23699 | -44.86755 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15e516c8-c12b-3510-b9e4-0b35423b2d33 | -8.71205 | -45.19984 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9b5b4664-ec1f-3b16-8ad8-8d2f49a797b2 | -11.78898 | -43.538 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6add8e57-721b-3cef-97e6-400e73630749 | -12.26203 | -44.42289 | 2026-10-07 04:21:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd07a01d-1c31-37f3-a406-af380b25e40b | -13.02912 | -46.79774 | 2026-10-07 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21bddf9c-0dd8-362f-8761-b230cc54e89f | -13.57899 | -44.4262 | 2026-10-07 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1862dfe-9663-3037-b2db-d8556e99e9f7 | -11.08686 | -47.60535 | 2026-10-07 04:21:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba635cad-9092-3448-8b90-e3d6c3c98ad8 | -11.73082 | -43.65288 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 05afbde9-0d8e-3457-bce3-d14a338be694 | -11.11005 | -45.73183 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e546a856-22f6-3001-b080-527d94c4dbd9 | -8.70532 | -45.19872 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed9c7017-fe59-36ce-ad42-4a256b63609c | -11.73027 | -43.65644 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a8b520cd-98b6-334a-9461-8f4edce54a27 | -10.47038 | -46.8243 | 2026-10-07 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a31b1b3-46b4-30b3-9715-9dbfbdc82c2d | -13.39657 | -43.8731 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32465d13-7bc0-39f4-9ad2-4cdcd281f3ef | -10.9392 | -45.38991 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0b73eb4-bb02-3461-9a16-3353bc277104 | -11.6775 | -43.62255 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3f2a8a70-2fdb-3db3-9e8b-2bb65cb14e32 | -12.16673 | -44.25231 | 2026-10-07 04:21:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca22613b-9e93-36ae-af0e-48121545065f | -9.90524 | -44.802 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1b04638-acc5-3e10-8dc2-a3bef250953a | -16.12383 | -42.07747 | 2026-10-07 04:21:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7404f600-317b-3c73-9e90-61b346883a36 | -13.50328 | -44.3665 | 2026-10-07 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 95f190b6-8f0e-3d0e-9045-1c3d01c125db | -11.84458 | -43.5544 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f99ac398-0c22-3ad3-a0a2-22a4a91b6687 | -12.17891 | -44.73374 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af16293a-06a1-35ae-8336-80344caa953a | -11.78481 | -46.57584 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7c3eafe-4268-3f28-b728-d28913431b9e | -11.23587 | -44.87459 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d911a9e-293a-3030-b3eb-bccbd9cea481 | -9.80063 | -48.92079 | 2026-10-07 04:21:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93fbb470-7aae-315a-8eff-f0560bf3b71b | -11.79493 | -46.70724 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 71147ce0-f7c9-3c55-a5e3-2171510f4544 | -11.23643 | -44.87107 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f5a818c-81d6-3e8e-9612-bbe0449defc0 | -16.12775 | -43.74954 | 2026-10-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 334a659e-7ddc-3e6c-a396-5f4b48e2ca64 | -9.79975 | -48.92594 | 2026-10-07 04:21:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c050c6a8-74a8-3f95-9d4c-df7da4860e73 | -11.01023 | -45.45302 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a517435-8771-38d5-b3ef-18fdc3f93b63 | -11.32977 | -46.67385 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 125b95ad-e94b-3fc0-b09f-8172fe8a0357 | -11.32567 | -46.67716 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3800fec-d19f-34bb-a273-106a8d513ff4 | -11.23964 | -45.25219 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81cdfd49-d4be-31d0-8642-be34bea3966a | -8.71264 | -45.19623 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 82a7d5f1-21c0-3028-9631-46686673f141 | -12.66819 | -47.49632 | 2026-10-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f561f8f6-7174-3123-a645-1e52c56892c1 | -11.73298 | -43.50694 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77290ab6-44ef-3d59-8aae-d7c424118d8d | -9.82914 | -44.78929 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3d7d601-953b-3d71-bf15-381807903f1a | -11.00311 | -45.43331 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e9ae0d33-8d96-3cbb-a6ff-0615426cc4f2 | -11.00805 | -45.44522 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9c5b781-3c69-379e-a28f-3d0f5e33ce62 | -11.57823 | -48.44226 | 2026-10-07 04:21:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da2faf61-b9e1-3185-a2f0-58b45c159bb2 | -8.90872 | -49.96647 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08ec8721-69d5-3751-b5c3-7d67b155798a | -8.69841 | -45.21986 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93ae0df3-2717-3395-98fe-5cfc4c21d866 | -8.53118 | -55.37334 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32dd2315-11d2-3388-967d-d6bbc7520aee | -15.24054 | -43.27298 | 2026-10-07 04:21:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 6de0e026-2e55-3cfb-af7f-4281d837f7b7 | -13.63415 | -44.4207 | 2026-10-07 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69886d68-d0b4-333d-83b8-93932191f40d | -8.53549 | -55.38419 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a4e6443-3dcf-3d29-a5f1-9e24bf75de8c | -13.02817 | -43.11945 | 2026-10-07 04:21:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 28bcf201-afc4-388f-9a32-8e7b2b9a28a1 | -11.37815 | -46.68238 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 097b5d9f-0657-302b-b213-e7122046b9f4 | -11.77141 | -46.69937 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bb1a655-b73f-3200-a3d1-b84ab7fdbce0 | -11.06696 | -45.8597 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 904d4cf3-f170-3bf3-827e-0e53fb66ca77 | -11.74459 | -44.94353 | 2026-10-07 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35a29872-9094-37de-b30c-62a299ddb6b9 | -11.64431 | -43.66483 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bd7d5fe-7092-3ddc-87f0-b8072b3a680c | -11.72805 | -43.64879 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27cb4e21-ef62-381d-897a-95fdb893e9a8 | -14.89405 | -44.80899 | 2026-10-07 04:21:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05bfe8eb-8e76-3f32-9ef9-afe4d64ef4d5 | -13.33824 | -47.63227 | 2026-10-07 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63ffa71c-41bd-3d07-9fe4-192f4e7a5f75 | -11.00253 | -45.43692 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c0a2864-8151-3c37-9327-d1b75f8965ec | -11.74902 | -44.93705 | 2026-10-07 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c3f8b63-b617-3e6f-bd60-8f0259c472a0 | -8.60615 | -45.65255 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c4bbb05-e744-37ca-9bf9-2b8ccde6e857 | -11.75565 | -44.93813 | 2026-10-07 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60452853-b31b-3926-8907-e895e52eab0c | -11.78458 | -46.70549 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7db5f46e-6e06-3b9d-9019-706067dd9a21 | -11.22735 | -45.26477 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c291a11-2d6e-339f-8bcd-20598b14dbac | -11.2298 | -44.86999 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e2fc062-9a02-3345-896c-27863bdbcae3 | -13.02849 | -46.80148 | 2026-10-07 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2aab2662-3b26-33e9-917c-28d87c000c07 | -13.03049 | -48.57945 | 2026-10-07 04:21:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15890013-cd3a-3320-9283-24a8b7fda6aa | -11.10624 | -45.72404 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19179a89-fcd0-3039-9b2e-e97bd16f75cd | -11.11195 | -45.71004 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebace799-3a31-3585-9b0c-2c96227e0614 | -12.82042 | -44.67223 | 2026-10-07 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d528c447-9b45-34b8-b000-22b7e4f03c3b | -12.19492 | -44.71835 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5c42ed0-e631-3cb7-ba7f-5a374794ebcb | -8.70237 | -45.21679 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ab2afa1-b017-3e1a-8fe5-a6362ac3e145 | -11.36947 | -46.64871 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae245ea7-1a84-3614-8ea1-a5b7e6c06633 | -9.44104 | -45.82585 | 2026-10-07 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 095ea690-0c5f-3f06-956d-c3401b5f16f6 | -8.28839 | -50.27813 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b3d22d16-d079-37c4-9829-e8bd75ae229f | -11.7336 | -43.65697 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5e73d2a-6a2d-3fb7-8591-1829d894893e | -8.70928 | -45.19567 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 5f081130-8b03-3b72-82f8-114821deda44 | -11.22907 | -45.25412 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 048b6747-2eb2-3570-b4f8-a6c07cbe9e5a | -10.98812 | -45.41994 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01e3331f-c2f4-3631-ab1b-5bf88a43f7f5 | -11.38372 | -47.53957 | 2026-10-07 04:21:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 193b16cf-a417-3368-bfcd-e6c87312ea9a | -8.70296 | -45.21318 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b879f97f-e4a0-3048-ad40-a59a813a6096 | -12.18277 | -44.73077 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e196f7ba-1f02-3056-9b75-c37dd6e6aaf2 | -13.29905 | -44.00122 | 2026-10-07 04:21:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bbab237-5c29-3419-9276-7a4c97f91148 | -11.7479 | -44.94406 | 2026-10-07 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94735a03-e573-352f-b284-94f887526ebe | -14.89349 | -44.81256 | 2026-10-07 04:21:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d793ec3-26aa-3498-b558-3801abae1c3b | -11.67417 | -43.62201 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e70171c-ca5a-3bcb-b44a-05d26c2ff431 | -12.16186 | -49.39526 | 2026-10-07 04:21:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c982930-0a1a-3b6b-9f72-1e5f9e7ef731 | -9.8092 | -44.78606 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bbf56a5-2d01-3efe-a04c-6ba034132ac8 | -13.54584 | -49.154 | 2026-10-07 04:21:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8022fd90-e9cf-3698-8eb3-a055c3df2f82 | -11.79105 | -46.58078 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8faf5a4e-5e68-3dec-ae6a-fa091f1b0fff | -10.97591 | -45.41058 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f707ef1b-b0d7-3324-9ce1-4a2880a51a82 | -8.70869 | -45.19928 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| bf5458f9-1326-3439-a51b-bbf8cd640fcd | -11.692 | -43.68313 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 862c5c99-3cdb-3956-a559-6095ae9b5618 | -12.6682 | -47.49715 | 2026-10-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a870a957-45b6-384d-b45d-1ab4923ba0dd | -13.63692 | -44.42481 | 2026-10-07 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README62.md)
