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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dadcf987-b466-3ba5-8815-b48b097eafe9 | -5.78418 | -45.78295 | 2025-10-04 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6450b075-ad33-3eb0-bef4-f9d204defe38 | -7.74498 | -42.54863 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 981f2fe9-6296-3412-928d-e983c011326d | -7.35923 | -39.17204 | 2025-10-04 03:51:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e986bacc-c42d-38ed-a925-74616b4dbf32 | -7.7258 | -42.5608 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41a68a38-60cc-3677-8405-6fca332aa1cd | -7.33248 | -41.43831 | 2025-10-04 03:51:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f912a056-8e2e-3d78-990c-e160211dbaad | -8.13224 | -44.083 | 2025-10-04 03:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92eab94a-2af8-30ef-a789-2e63674c22a4 | -8.81677 | -44.81842 | 2025-10-04 03:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eece2d8b-6996-3e10-9801-9089a50580b5 | -10.33299 | -50.32612 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6f49efe0-14ae-380b-a09d-13ce7454f715 | -8.9015 | -46.05357 | 2025-10-04 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 263f824b-43d4-39fb-9185-02e6616c8235 | -6.46589 | -42.52274 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 111bd007-53f9-3213-9087-e115aae9d840 | -5.73705 | -42.92513 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 57c05eaa-973f-3b28-89ed-525d15bc31b3 | -4.95543 | -45.07706 | 2025-10-04 03:51:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3579907d-9948-32a4-b106-33377c6cd2a0 | -6.37161 | -43.88496 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ec0f4df-b013-3608-9ba4-19333b3bfdfc | -11.4358 | -43.49309 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb824132-177a-3784-be1e-9ff76080b1b9 | -5.02019 | -43.66344 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f2dfad5-ba24-3bc9-866f-4dc6964f85e6 | -7.4646 | -46.85018 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b6614b9-2fd4-366f-93d0-ba091426182a | -6.2031 | -44.33101 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46b65081-9bb3-3625-8ea8-7180e750d91d | -11.10348 | -47.71575 | 2025-10-04 03:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d08736a4-e126-390f-90c4-b43472788991 | -6.36525 | -43.89426 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9ecb4135-103f-3782-8944-be09d82ea6d7 | -7.46045 | -47.17925 | 2025-10-04 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a56b6af-b8e5-329c-98a4-abccc35a5940 | -5.88782 | -44.25896 | 2025-10-04 03:51:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5674ac9e-c00f-3d52-b234-1740f49a6ba1 | -5.38471 | -36.83243 | 2025-10-04 03:51:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bedcd263-00e8-3ffe-a425-5936854b79d5 | -6.672 | -42.37772 | 2025-10-04 03:51:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 71ee578a-41f3-365a-b3ca-9fceb80202d4 | -6.70529 | -42.78941 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e447c7b4-3efc-3ecb-a163-d115845d0e7b | -8.62766 | -43.9846 | 2025-10-04 03:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 747152ab-2164-3b5b-a0ff-e67009ab7f1a | -6.06486 | -42.52174 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 60d08afd-4e0b-30c0-b3c5-756236f1ff54 | -8.5844 | -44.80003 | 2025-10-04 03:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 44fc9598-956c-350a-aa14-52ec8d8bc7b0 | -9.95817 | -43.70306 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1059e837-510a-39e4-ba54-8f17990b3a00 | -6.05346 | -42.51136 | 2025-10-04 03:51:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 39d72000-554e-3c6b-89cb-287b1032002f | -12.08835 | -42.74148 | 2025-10-04 03:51:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe56bb46-607c-36ec-8074-a8ab5115a1e2 | -5.66111 | -42.71062 | 2025-10-04 03:51:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fec72a82-5392-3656-860d-0cf8a954b74b | -7.23816 | -42.98423 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 12d42de0-c9b4-3706-9bab-0137732f0682 | -6.61538 | -44.29338 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97fa8218-9a9f-3c04-9929-d1095577b2ca | -9.94656 | -43.74413 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b033b6e-f052-390c-bc40-fd9f7a8c639b | -7.73152 | -42.57729 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce547a6b-3fa4-3f01-a394-fa0c90745241 | -6.35205 | -43.45051 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4d1b9d8-5e47-3742-b918-7f8a55f71d06 | -11.16931 | -47.75561 | 2025-10-04 03:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 15498a18-046b-393a-b51e-43896f07ba1a | -8.61255 | -40.5025 | 2025-10-04 03:51:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d0ff2c3-d315-3c16-bf1b-9aa9db6db637 | -6.0747 | -42.51512 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 2367634c-afc7-3bae-b866-e1fb20efa963 | -7.7184 | -42.57892 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 38e91ff9-a382-30ce-8b3a-e30576ddfb0c | -7.71424 | -42.57821 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b30e688f-375b-35b0-af59-2d2bee4cdb59 | -7.3627 | -39.17259 | 2025-10-04 03:51:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e9f4c517-ed43-3a68-8a07-2935ddcd257f | -6.14247 | -37.59674 | 2025-10-04 03:51:00 | NPP-375D | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7969fd0-d512-3ab4-8c07-96e876b8b9f5 | -6.07449 | -42.51005 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 335ec889-756c-3808-aeb2-2e82cf207d3f | -11.49957 | -44.99994 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3708777a-c2bc-3ed3-8ab8-c1e46e9849d2 | -6.71373 | -42.15776 | 2025-10-04 03:51:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c0573d4d-c678-3e4c-a52c-6d16682b58f5 | -7.47017 | -46.85117 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f54406d5-5d8a-3970-b36b-b4cef374288c | -11.05749 | -47.78516 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b82b2b00-b06f-32d3-909b-54970b9ced64 | -7.89545 | -42.60144 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4d9f0dc0-ac3e-3c19-abd6-48fbe2ec170b | -6.36823 | -43.90499 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62d5ce0d-3d2c-3424-8aa6-f124b0b7d84b | -6.29421 | -42.48926 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4ad30f1b-9bc6-3678-b6ab-00ae29ffea1c | -11.48212 | -43.49786 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c186bd37-978d-350b-9011-97eb254f57dc | -6.18156 | -46.3147 | 2025-10-04 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66b1866d-b0da-3994-b472-9edadec62cb6 | -6.67342 | -42.83509 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 811a1eff-fcf6-3b3a-85a9-566682474bb6 | -7.2524 | -48.48207 | 2025-10-04 03:51:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 180bf06f-a7ed-3f9a-87be-34d3e59a028c | -7.72607 | -42.58413 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| be3e24f1-9c85-3518-9b3e-ddf61b71beb7 | -11.48765 | -44.98754 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 601e698d-8aaa-3769-8b83-f443eb290761 | -5.96841 | -45.89367 | 2025-10-04 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc9a4b7c-e0c3-3310-87f7-24f1f410dd1f | -11.13296 | -47.86179 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eeac5238-7e6d-3061-83db-16005bbea55a | -6.77013 | -43.60875 | 2025-10-04 03:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b153adb4-7a13-3a46-94ee-7a1254e03352 | -5.72367 | -42.68266 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f4f02cb6-66cb-3c71-a7b1-fc013a28bc1b | -5.31476 | -45.30049 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0c9d8b3-0208-3fd3-a6f6-78b49d6de26a | -6.88361 | -47.23869 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 97712845-9749-3dd4-8089-c4922dad79f6 | -5.69526 | -49.30724 | 2025-10-04 03:51:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7202989-20be-38e5-bfce-2501f0696de3 | -11.10277 | -47.71936 | 2025-10-04 03:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 205c570a-37f6-311f-afdb-3ec132f7b0a3 | -11.47735 | -45.02226 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bc83bf69-a81a-37fc-a4e0-f20109e6dd5d | -11.43165 | -43.49235 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a52c2434-bf17-3d54-8d15-dfdaff242a7e | -9.94099 | -43.57336 | 2025-10-04 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76b9daca-a69b-31bf-a8da-c971e39e35d1 | -7.54584 | -42.39949 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc230a51-63dc-3ae3-b370-4c15c717e67d | -5.44444 | -41.99426 | 2025-10-04 03:51:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae6d21fa-e4d8-3bfb-b9f1-d025d5f44ef0 | -7.77949 | -42.59732 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cf02eeb5-5698-33c1-b88b-a0d135cfcd6b | -7.48597 | -43.03247 | 2025-10-04 03:51:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 310edcf1-af57-3ac5-80b6-7cbc597c45c6 | -5.60595 | -43.22772 | 2025-10-04 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 605a1ab5-f9fc-37cd-8240-f790e1ff1228 | -8.91292 | -46.60458 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95904d06-09a5-33aa-8b62-90eddbf26113 | -6.20248 | -39.69939 | 2025-10-04 03:51:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 237b551f-6346-3448-a1f2-4ef3346c7f08 | -6.12922 | -45.93398 | 2025-10-04 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4873879f-945b-36b5-9085-6c436a1b712e | -11.0567 | -40.93814 | 2025-10-04 03:51:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c962be10-ff03-35e9-bbdc-4dcc3a9907c2 | -7.76772 | -46.22957 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c48eca2e-750f-3cd1-89d1-c2046363ec75 | -9.08411 | -48.02512 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2284edad-43e0-3eda-ad72-171472e63a5c | -11.47821 | -45.01739 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3556c5e-2574-3951-a237-0972ad68ad30 | -6.26892 | -43.10553 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91a37feb-96b0-375d-a811-6e87173523bb | -8.84727 | -46.83017 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ea7fb3a-43ef-3a5e-9b52-862eefed0d52 | -11.45975 | -45.14763 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88c82d04-4016-34dd-9e9f-a261f4b8f140 | -4.67572 | -45.68662 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8b61ad2-e530-3b1f-a879-f487f5a868aa | -11.14995 | -43.3957 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 939c5452-eea4-300c-9b74-fe6309d02d4f | -5.94513 | -43.29786 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 554327c1-cb01-388e-bb3c-0f659d7f89ce | -7.74358 | -42.60698 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 51bd2fc5-5bb7-39de-9f2f-b5c2b82a32f9 | -7.77127 | -46.2404 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2b416f4-d052-3fb7-8050-e99591e89748 | -6.6683 | -42.82436 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e56fce53-0181-3963-b167-a51ff6097510 | -10.33954 | -50.32751 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a74d6ce5-bfdd-3e23-9428-e42900ea2a9b | -8.84418 | -46.84709 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 592b16d6-331f-3352-ba18-7456d84e3d60 | -5.73264 | -42.92443 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 20b5f067-2908-3388-bacf-a3b3086109c8 | -6.653 | -42.79853 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 485b8d20-eaed-3479-81fa-b93d3cc300fa | -5.1994 | -45.06157 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6eacddf2-17ed-39df-b1ba-9b6d746434df | -5.38742 | -37.70936 | 2025-10-04 03:51:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e4d00383-8d23-3bad-80fa-771f7e707160 | -5.46334 | -43.15842 | 2025-10-04 03:51:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02744305-d98d-3d41-848f-ed09f6256fea | -11.08745 | -47.88783 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f22cc742-f81d-3391-ba19-cd35015d5d29 | -7.26597 | -45.48089 | 2025-10-04 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f087c441-5072-370d-a809-3ed1ff7e7be6 | -7.46392 | -46.854 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aaf22776-aeb5-3eaf-8ea3-d60eb37b500b | -6.2793 | -45.082 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README21.md)
