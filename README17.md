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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 519f71f5-854b-3eff-ad9e-4a219df23ce0 | -10.22418 | -36.3339 | 2026-09-27 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 43367ad3-8648-3262-9005-a1a03841db20 | -2.99771 | -50.474 | 2026-09-27 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32333723-fd20-3f7e-920b-42ebbf2a1f31 | -3.2675 | -50.14751 | 2026-09-27 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53827472-a272-3ac5-afb5-5d8db2b84fbf | -3.6989 | -51.37379 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 891ae8ab-7919-31ce-8d43-a7fb3d998698 | -9.34441 | -40.64061 | 2026-09-27 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4f31be4b-1789-3209-8d3b-fd5b2a8fc73e | -7.29042 | -43.30239 | 2026-09-27 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfeb2496-2d5b-3509-8084-9ae4ae2c55e4 | -8.36206 | -44.1678 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4271764b-6155-3a75-9135-a9c1e88f038e | -8.34587 | -44.13502 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60944fa5-df9a-34af-bf49-60034a774765 | -3.95526 | -48.12006 | 2026-09-27 04:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf8496ea-bad8-3a82-90ad-925dc5b93710 | -6.13614 | -53.06351 | 2026-09-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ea64db5-846d-371e-a2ad-ff0e463e9ce6 | -3.96407 | -50.71921 | 2026-09-27 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 73cb8544-e18a-38f5-a638-2ad9eb3764c4 | -8.34307 | -44.17517 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9e2370e-e9b5-3456-914e-eaa4d41c660d | -9.78401 | -44.82738 | 2026-09-27 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d3516cc-9f99-3816-984a-cd324c2e3390 | -5.20002 | -42.76872 | 2026-09-27 04:08:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbf75791-bb6d-3bae-805f-4a8c197670c7 | -7.38501 | -47.02081 | 2026-09-27 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0003f8a6-4eec-337b-97a6-7e6b97bbc809 | -6.83813 | -43.57395 | 2026-09-27 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57580884-512f-338e-b5d8-8ef5d33fdca5 | -5.75938 | -45.29504 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3f1e58e-93a4-3c00-9b29-4ceb59b8b2f5 | -6.9262 | -42.86899 | 2026-09-27 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f1018175-6dc8-362f-8d4f-b8c86f8c128b | -5.4981 | -45.51401 | 2026-09-27 04:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6285848d-e811-3134-b10c-1313c1942039 | -5.27567 | -40.59106 | 2026-09-27 04:08:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 51347010-ed24-3920-a09c-29833fa68b40 | -7.35112 | -42.0789 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 826290dc-d42a-3f23-98fe-e548f3365691 | -10.01836 | -50.15013 | 2026-09-27 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7797d559-afd4-3181-96e1-1efad2d71991 | -7.21042 | -39.35381 | 2026-09-27 04:08:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef719772-a4ce-3178-a2c3-d1f43785e53e | -6.93263 | -41.61259 | 2026-09-27 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a85dc23-f21e-3e3d-be6e-6adb807661d4 | -5.47788 | -48.58531 | 2026-09-27 04:08:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29dec268-6388-3de3-80f8-9b6044cb2fd5 | -6.13276 | -53.05544 | 2026-09-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64e49941-905c-3aa2-9269-ff82cfa4e2a5 | -3.97097 | -50.71553 | 2026-09-27 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e85ad9a1-f956-39aa-9533-576886efe91f | -3.86672 | -52.28504 | 2026-09-27 04:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47f08ce1-4ed8-3508-bb6c-5aaf81c97e52 | -7.28909 | -43.3106 | 2026-09-27 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9fe64a7e-4e6f-36e6-9112-8cedc23c74d2 | -5.73636 | -45.03107 | 2026-09-27 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a2ad621-2f61-3d7e-9595-0cf21bf9bd25 | -4.2848 | -48.56253 | 2026-09-27 04:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57037792-51cf-3c60-83d6-e0b6c7498b3c | -5.1945 | -46.20478 | 2026-09-27 04:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 878eb131-29bb-3394-aa8e-aa169b008562 | -3.01668 | -51.5366 | 2026-09-27 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c0454db-4801-3447-b2d5-b86204672a38 | -7.29148 | -43.30899 | 2026-09-27 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75205966-641a-3a5d-9499-2a9346452051 | -7.02273 | -46.44827 | 2026-09-27 04:08:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6732e497-a448-324f-9175-98f7e98a4381 | -6.16767 | -44.59452 | 2026-09-27 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df4a8076-b452-3f4a-bc0b-ecee991d0194 | -2.96644 | -49.56623 | 2026-09-27 04:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cc98a56-de35-3ccb-bb7f-e5025b11f37f | -11.13099 | -38.52615 | 2026-09-27 04:08:00 | NOAA-20 | CIPÓ | BAHIA | Brasil | 2907905 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c30d0ae9-9e44-3ea1-a1ab-9a0a0cece510 | -5.00688 | -44.67957 | 2026-09-27 04:08:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfbe73de-04ae-399c-8694-9253b5ecee2e | -7.98187 | -44.80977 | 2026-09-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c6642af-efe5-377d-8aca-0e4790de8b36 | -10.22289 | -49.98442 | 2026-09-27 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd10951d-d7cc-3a2b-8bf6-294c7f5fbe7d | -8.34512 | -44.15592 | 2026-09-27 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e69f4ec-0d12-36ef-bd0b-b2b4062eaaf7 | -7.36501 | -42.12271 | 2026-09-27 04:08:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a97878dc-204f-3d18-81d0-73c3d1f6d544 | -12.289 | -50.3143 | 2026-09-27 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ca965d94-325e-3c38-9285-7fba549ea9e1 | -11.9431 | -50.5058 | 2026-09-27 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 0c911faf-6f58-33c8-bb96-5417d8be558e | -12.2703 | -50.2951 | 2026-09-27 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| aa0b0a04-3975-3ab8-9a53-8a961e5b4022 | -11.8859 | -50.5125 | 2026-09-27 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| c5e18894-a47d-3dc5-9d8b-4208504b49ca | -12.0369 | -50.6019 | 2026-09-27 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 8abc88a0-fc1b-3615-bcce-7887cc5df92c | -12.2894 | -50.2927 | 2026-09-27 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 6e477e8b-5392-3b2e-b7e7-0ccfba4a14db | -11.8097 | -50.5214 | 2026-09-27 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3b8de398-6cf9-3489-bc4d-5e0ce4d42fd2 | -17.63109 | -44.84015 | 2026-09-27 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aefac8e4-abcb-3d1b-89b0-3028eeaef970 | -12.26714 | -50.31441 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e422d1ad-b09d-3a8c-8343-3e60fb5bab9f | -11.04548 | -51.32701 | 2026-09-27 04:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93be2816-4628-3147-a296-9c9ebbb88270 | -11.94115 | -50.51413 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3fe26f16-39e3-3815-9866-33e496a5cee2 | -14.10183 | -46.32218 | 2026-09-27 04:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc0a53f2-52f1-3b30-9833-aa2cf69a49e3 | -12.18644 | -47.38817 | 2026-09-27 04:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c267be9c-4688-3b21-ab8b-6130e626e214 | -12.28493 | -50.30503 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 68f98e80-7ad9-37d0-8bed-9d80225faf92 | -14.72922 | -45.57646 | 2026-09-27 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b83dce3-4999-3dd2-8623-57dcfa8d9685 | -11.60907 | -49.87043 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5b955b2-c449-34a9-a59b-b04043a1cb51 | -13.87644 | -49.0427 | 2026-09-27 04:10:00 | NOAA-20 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c5bc5a3-1320-36d5-b80f-9da0d7fa4529 | -14.79981 | -45.96197 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 51409cc5-fc4e-3933-a513-644f5ec2f5fa | -12.13784 | -50.33202 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d34c65a5-ec99-3071-b00b-8c3bdf3dc43a | -11.93717 | -50.50653 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1023c2a3-df03-3817-944a-9817a43ff7ae | -11.85818 | -50.55333 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c24c18d-2f92-33f1-966b-e8825f84016f | -11.95807 | -50.51079 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f022a1ac-95d0-38c4-9f31-4a5c0ad93ea2 | -11.60459 | -49.86645 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c8ca82f-7fd4-3214-a65c-8892111ee9d6 | -10.40336 | -53.81505 | 2026-09-27 04:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 02f81ec4-348d-3f84-8316-c8344a8145b6 | -12.2786 | -50.31023 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e77b7143-3506-3776-9764-a8016ad00b0a | -11.96817 | -50.54344 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8e2327e2-2b76-3f68-9710-5e7861cdd499 | -11.98472 | -50.56842 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8a4d4e5-f6e8-3517-8fb5-7de9b452593a | -15.45721 | -39.54922 | 2026-09-27 04:10:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 91976472-165c-3eb8-ae08-ec35c7ac1245 | -11.81664 | -50.51413 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5d0180e2-0a01-39f8-b377-1fba928dc276 | -13.09246 | -47.42784 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f438dab9-f207-3252-b355-f71150246020 | -15.33039 | -42.1331 | 2026-09-27 04:10:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f5dfde15-fd8f-3248-bf58-44d3488c2a09 | -12.66 | -47.29353 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2930d54d-0a87-368a-9b66-953ea6182455 | -11.80299 | -50.52842 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9949ba91-b6c1-30bb-a733-f34d4e3b59d7 | -13.85447 | -43.99368 | 2026-09-27 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04fe8808-c821-333e-bf68-d77ff633c148 | -11.93258 | -50.5022 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 919eb69e-bb9a-397e-8dd1-0eff1cf59da0 | -15.42511 | -47.91154 | 2026-09-27 04:10:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fb64450-b395-3904-93c8-1de0359514e0 | -12.28708 | -50.37719 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7585903b-0959-30a6-b49e-b4deac218e67 | -11.89157 | -50.51763 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a891db68-931d-3f1d-af72-65104bb2e4bf | -12.72666 | -41.80392 | 2026-09-27 04:10:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 90ea6c2c-7069-3423-8366-5b51b6cdb430 | -14.79027 | -45.95071 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00d78d69-9c56-3b0e-a0e7-6129cd52c553 | -11.77529 | -51.02549 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03327b05-a2e6-39bd-a143-ac06652aa1d9 | -14.21978 | -48.50858 | 2026-09-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30e111e8-5f90-37dc-87a6-e65d0bd67fdd | -12.02746 | -50.60102 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2972ae1f-074c-3594-aee4-e9d82aff9d0f | -18.03071 | -48.10328 | 2026-09-27 04:10:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 544e18a2-98b8-3352-a9d7-21f3f6005b52 | -18.37104 | -44.70062 | 2026-09-27 04:10:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6acb5e8b-9513-3a05-8ffc-54a3e7e1c581 | -13.30774 | -42.39863 | 2026-09-27 04:10:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0dc225e9-aafb-33d7-9894-61b4506e093b | -12.28793 | -50.28946 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 100bfaf5-f447-3239-ad4d-af01d5d1732a | -11.9712 | -50.58508 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7b954ad-f8ef-3173-80b9-5b62d953840a | -12.28161 | -50.29465 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 692e223a-5feb-3239-8dc7-0d4ce9699b68 | -11.76988 | -51.02438 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e0f186a-935d-3503-bb36-4ce6f891e2fa | -12.03397 | -50.5955 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5a81d147-38b5-3745-8df3-f3e7931fd9a3 | -12.29305 | -50.29049 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d007bebc-cfbf-35c2-9e3d-f089930c7128 | -12.30269 | -50.29568 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6fb399c1-e0bc-3e09-b1b7-a36ae6995842 | -12.13781 | -50.33894 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05879898-6b6a-30ad-a89e-166c49bd1ce5 | -11.87948 | -50.52692 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2af3615e-2ac6-3229-bcea-49183b65b38a | -11.88195 | -50.51378 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c6e4a19a-9538-3656-aeec-621d9cf4cca3 | -12.3015 | -50.30191 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README18.md)
