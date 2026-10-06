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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5fa5dbb-e7d7-3d1b-90d9-769c80e3c564 | -3.15674 | -50.43956 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f10806eb-1324-36e4-bf06-21a308f2e9a3 | -5.11951 | -43.99137 | 2026-10-06 04:19:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b4443a7-7e41-3731-93c1-8b88c5884da7 | -4.51143 | -43.69291 | 2026-10-06 04:19:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49c93932-2a57-3493-baf5-03aa45520ebd | -2.93092 | -54.12459 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a8357ef-27c9-3ecf-90fe-924a5b8c9ae8 | -5.97347 | -41.36457 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 150a5606-853e-3ac0-bb72-d0c90acfc14b | -8.52281 | -48.90873 | 2026-10-06 04:19:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd827765-c940-367d-a80a-efaac8567c82 | -5.84568 | -45.01675 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b35c5cc2-1a1a-3575-aa8d-6ac6c357fb95 | -11.45033 | -43.39557 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8be426b2-81ce-352d-9462-98c854620240 | -11.22519 | -44.85198 | 2026-10-06 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9915591-324f-3ff9-9994-a345b1e07a5f | -3.84172 | -50.32093 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f2b7d69-9f66-37b4-be8e-f532233aa3ae | -11.2831 | -45.51441 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 14888d99-da91-31e4-94f8-84d1be4af000 | -4.99829 | -42.42502 | 2026-10-06 04:19:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 93f608fc-040c-3f93-a392-09a29acbccab | -2.80839 | -54.13904 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24ef06d5-0c57-36be-870e-d009f6cbf00e | -7.46934 | -43.00282 | 2026-10-06 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a7b181c3-9f45-3c42-b6f1-15458cf75249 | -3.04789 | -54.22871 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c73e68be-2f7f-349c-a3ef-d86ef2e0f3a4 | -9.87112 | -44.81125 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a7c0c6c-9557-3a80-be38-e7d710f4ae94 | -6.35118 | -42.54455 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0c6d83e4-549c-3df5-8808-604204c1c072 | -3.08855 | -54.16107 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51ff225b-f6d9-3b52-b654-39e3ab0e7aa8 | -6.01094 | -47.39901 | 2026-10-06 04:19:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86be8f65-4bbc-35c2-906f-b1fe5d1b2887 | -3.33242 | -53.39416 | 2026-10-06 04:19:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d73fb113-d233-384a-a458-a4bcf8ab8c91 | -6.62468 | -37.88774 | 2026-10-06 04:19:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa0db7bc-c2ad-3380-8a3b-d3ee85a23941 | -4.45208 | -54.96213 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be24b6dd-67e5-385f-aa18-89470ab288e3 | -2.86299 | -54.14027 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fc5c39b-0c5d-3e50-a3ae-3d203b83dfbd | -5.81474 | -53.83605 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a9b8163-3eca-38be-a951-b7604e4e03eb | -6.36961 | -42.54353 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 188dbd73-6d4b-35d7-abb0-9e0f481f215d | -3.13059 | -53.71029 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06b4b79e-cf3b-368a-b13d-8e5c69b9db62 | -4.77221 | -50.81164 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23c4dadd-130c-3e2b-ab1b-f03218413fba | -3.05841 | -54.20988 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cf26550e-0ea9-3d18-822d-380140ecd205 | -7.45124 | -46.83363 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aae74d56-038c-3891-b781-3456389f9083 | -11.27664 | -45.50904 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| c791e2bb-3f7a-34fc-9300-a9bc015f90d5 | -3.09969 | -53.72306 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dda4a586-5b8a-3e68-bfc6-6185c4441b0c | -6.34779 | -45.81697 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b70cf727-0284-3037-982f-a82da285fbfc | -11.27945 | -45.49266 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b11e4e70-9e28-3514-824e-62bf6b03d48e | -7.48213 | -42.8094 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ab3be680-cce4-3e9d-b3a2-666327cfb394 | -5.98057 | -40.91035 | 2026-10-06 04:19:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b279d59a-3a56-3485-9f28-6db47ed25a87 | -5.6711 | -42.58284 | 2026-10-06 04:19:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc21c88f-6166-3296-8700-19fb540b8632 | -4.05282 | -54.05323 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbee7aa2-06cc-3ecf-9c80-746c9fe49a0b | -3.10902 | -53.71286 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6771007a-3ca9-3ab5-b264-a19d13e59325 | -3.14997 | -50.4457 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de2d1311-fe63-30e2-83a3-9f2e1b576fab | -11.26147 | -45.5037 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97a69d97-7e0f-39ca-a8ef-c3e5431fac3c | -6.31803 | -43.33832 | 2026-10-06 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 170f9431-1157-34f0-a16f-f6550db11974 | -2.87155 | -54.15105 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d1dd1f98-5c4f-32cb-b67c-6be6de3d7d9a | 2.46276 | -50.85248 | 2026-10-06 04:19:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 988d3239-fa59-300f-9803-75ad47b71f15 | -6.92452 | -43.68133 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6676d83c-225f-3d5c-b098-1b033b124ae3 | -3.05618 | -54.24377 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3819be6-3365-3bc3-b3be-554e4352d73d | -8.70193 | -45.20256 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 835108b0-34ec-3be9-88cd-afbd1d0c939f | -6.82026 | -38.53059 | 2026-10-06 04:19:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| be2c5670-03ba-3a46-a9d6-c7b49f03d835 | -3.07038 | -54.24571 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00934285-2e05-311e-a3c9-436a1ba9d0d5 | -5.67831 | -53.50018 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db0c7d68-775c-3135-b139-fa62c4e0575e | -10.5313 | -48.06073 | 2026-10-06 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83fe589b-e9cc-3135-82e2-fe3a53d804aa | -5.67738 | -53.50544 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e4437682-6c6c-3d9f-a134-a076e5c80698 | -11.28159 | -45.51571 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| a1bd444c-dd15-33f3-8ff8-92729a90d008 | -2.97867 | -54.12776 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3bf36581-f5ff-3153-a9d0-3df0e3d62245 | -2.86581 | -54.14224 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e3b2497-5ec0-3b8a-8bec-873070332350 | -2.94731 | -54.15523 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59d8f6a4-b949-3011-8e4f-665dc965f696 | -11.26726 | -45.51323 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c1fad7c4-729f-3ff8-b5fb-8384e540b7f8 | -9.08021 | -38.46846 | 2026-10-06 04:19:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f57aae3b-7d9c-311e-855d-ea34cdb178b3 | -2.94616 | -54.16186 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 34854607-155a-3c3f-b06e-65a7852cb636 | -5.8357 | -45.01307 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 87d7da27-3ba8-3089-9e5f-18b32819e390 | -9.26507 | -45.65298 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d573767-0e8a-34f4-91ac-504546c067ab | -5.8853 | -43.45894 | 2026-10-06 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973e369c-1ebf-3bb6-99a2-b9dce3f5aca2 | -11.27649 | -45.50206 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3792b9e9-1992-326b-be85-a1e09af92d51 | -11.27881 | -45.51792 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9ae3c57c-1e90-3baa-9db1-f58be6bda287 | -4.05969 | -54.05448 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d977bb21-cfcc-385f-a53c-5c17696b56b0 | -11.2774 | -45.52617 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 801ec36c-c776-33d7-9321-7e5395a53529 | -3.46973 | -50.09352 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 361193ca-d699-3059-a5c2-702e0cbfcd08 | -4.46447 | -54.96943 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c27c182a-140f-3634-bb3e-84f68eefb159 | -3.84786 | -50.31794 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ab256d7-6797-310e-a8b9-dfe2fc5e327d | -2.773 | -54.10827 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c32c356-48e6-3ff8-ab87-8c447dbdf748 | -3.46793 | -50.10388 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f64309a-e7e2-3c0f-895c-7f81deb5dcae | -2.89577 | -54.15981 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e4fa6f6-76c1-3839-b768-d03a5b293386 | -11.28169 | -45.52267 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de6dc93d-0865-387d-9f08-d1ea4a684ee3 | -7.89571 | -44.2017 | 2026-10-06 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01da8b0b-4ca6-39ae-a3c3-64ccc1274690 | -4.19591 | -44.26065 | 2026-10-06 04:19:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8ac5222-92f9-38be-a8f4-eba45ad307fc | -3.10028 | -53.76291 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 334d48f3-f9a3-351a-b5a3-ce4bc254d9c2 | -8.87135 | -45.3728 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35de6c63-c964-3808-8f33-2e063c053446 | -3.09559 | -54.16213 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c5a1299-37df-3fb3-beee-ae87a279e6f1 | -6.71781 | -45.97823 | 2026-10-06 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1715ba4-e0d1-348d-9ef3-2b05181cbbe2 | -11.29383 | -45.51634 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 457bff4b-9fa7-3402-bc39-15642f56eb74 | -5.31998 | -40.89479 | 2026-10-06 04:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae4f9070-df85-39dc-baee-d501b4364ab8 | -8.4564 | -39.55856 | 2026-10-06 04:19:00 | NPP-375D | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6351f57-a582-34c5-97da-fb394efa91ed | -3.0917 | -54.1666 | 2026-10-06 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 699897d8-e4cd-3238-95f0-a887d4cb7386 | -3.0001 | -54.1086 | 2026-10-06 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0a37cb3c-df20-3fd1-a8e4-01000c5fce76 | -2.8713 | -54.1518 | 2026-10-06 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 10ff3682-8d44-33c4-8605-9f7f83bb1b96 | -3.0933 | -53.7037 | 2026-10-06 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 30ae3cc3-92eb-3379-b931-66d9a7142ae0 | -3.0375 | -53.8865 | 2026-10-06 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 0edd7910-2a80-3847-96ab-d33c8ea2cc79 | -3.0915 | -54.2469 | 2026-10-06 04:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 281813f4-fcb4-37d3-ac7d-f5a90629a975 | -3.0 | -54.1287 | 2026-10-06 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4b4f9e63-8db5-3736-8216-db99da8ada60 | -5.8323 | -45.0105 | 2026-10-06 04:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 10233300-b1a7-3faa-b96a-1ba0531fbe30 | -3.6732 | -55.9425 | 2026-10-06 04:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 9c2b2651-581f-37de-83d7-e9755cbfbd77 | -3.1116 | -53.7436 | 2026-10-06 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c30d6bf0-1572-3cba-ab81-14cd6ef5a2ea | -3.0548 | -54.2076 | 2026-10-06 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c9fe3d2e-aa43-3535-86c3-2c9c67da927d | -3.6915 | -55.942 | 2026-10-06 04:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 82d6b62e-c961-30a0-ad52-773c2d3868d6 | -2.8714 | -54.1318 | 2026-10-06 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| eb805307-71f9-3267-90b5-3e3d6cee9bb0 | -5.8511 | -45.0091 | 2026-10-06 04:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 4d47d4df-574f-37a6-8d4d-48eea477f751 | -2.9449 | -54.13 | 2026-10-06 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e4d8529f-7051-3848-8aac-b321a104f8f5 | -3.0932 | -53.7239 | 2026-10-06 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 579be6c6-37cc-3120-a21a-1cbf41481c03 | -3.0732 | -54.2273 | 2026-10-06 04:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7a7e6e6e-a58e-3b01-a2ae-c9193f1a5f2c | -3.0192 | -53.887 | 2026-10-06 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| f042c4ca-2784-30d7-8474-3831bccc698a | -3.0731 | -54.2473 | 2026-10-06 04:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |


[Clique aqui para ver as próximas entradas](README34.md)
