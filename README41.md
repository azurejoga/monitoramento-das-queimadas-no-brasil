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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b68529b-7999-3122-b7d1-9950ad48a4bc | -4.34891 | -45.75729 | 2024-12-02 04:25:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1660b7b6-4e38-31cd-a881-efa4e2821c88 | -4.65972 | -45.65043 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a033822-4c09-33fd-8dba-f2df8a992847 | -2.81156 | -53.0615 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 285e556d-c951-3461-a415-92c7872a8b0a | -3.19128 | -49.24611 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68edfbd9-aa4c-381d-ba92-bb6c977fb39f | -6.00193 | -45.41839 | 2024-12-02 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 462345e3-11c7-37fa-b6cd-16c60b7cda0a | -3.27721 | -48.78418 | 2024-12-02 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4f540e1-0c88-3dee-80d0-4c2115585813 | -5.12608 | -43.20973 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| ccf0ffdd-6279-3f3e-be81-b5c0bd44e390 | -4.00038 | -48.30322 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c617a6b9-f4ca-31b1-bc39-b6ae43a707b2 | -3.75208 | -54.5181 | 2024-12-02 04:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa679510-2564-32b1-b24a-6f78f520cce6 | -4.26747 | -50.85373 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13f73f9c-2558-37a8-a99f-1fe7b838df2b | -4.63538 | -45.45866 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 12301680-ffc9-387d-b2c8-bbb6c683f039 | -3.24953 | -53.92112 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0e4439b-cbbf-3d45-9980-137406f6c5c2 | -3.28531 | -50.55983 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d2bfd97-7d6f-33b7-b0f7-5b320726f99a | -2.55614 | -53.40302 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2febb1fb-401c-3b18-8616-6d5f8edf114d | -2.73821 | -51.75337 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bae7cdc8-86b4-3051-ae81-c3d9a2a1889f | -3.97844 | -46.75482 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69c38e74-43af-3159-b0ec-b21a8d452157 | -2.82455 | -54.19267 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f521ae01-cc86-3fa8-9fab-de75adec9628 | -3.93248 | -46.9148 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf5daadf-b93f-3f06-8257-499d34c6c4cc | -3.25443 | -50.6205 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb7285b0-b90d-3b0e-8e00-3ae6f622eaf1 | -4.07277 | -46.82008 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c21a1d2-2ca7-3bb2-a35d-df03b201affb | -8.50965 | -42.87687 | 2024-12-02 04:25:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c8cfcc1-5757-3870-941c-716c76c83db1 | -4.00127 | -46.65363 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4bee280-a2f3-316d-9be7-4e84e5e75fa7 | -4.30045 | -48.21218 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be69e4bf-8d4c-3820-aea1-d7068463c74b | -3.28153 | -53.35196 | 2024-12-02 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e0ce2d8-04fd-3dfd-b7f9-a2be59a8cb6d | -3.90301 | -51.05317 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 654e57fc-1c08-34e2-8b0a-068bb46f73f4 | -4.15118 | -48.24168 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde488dc-8ee7-324f-a31f-51bcba827dfe | -4.26341 | -50.85304 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dbcd61ce-43c5-3a24-88eb-7b286f3d31b3 | -4.8661 | -41.35836 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bc7d3c7a-0613-3057-9844-9341750696ee | -3.77707 | -52.03777 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d67478d5-6440-3a83-abc0-7eadb0a4de82 | -4.43884 | -45.35306 | 2024-12-02 04:25:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66b3afb2-2de4-3855-8e7e-b33eb7b60cc6 | -3.54764 | -51.45205 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f384fb36-42be-38c3-852d-21757bf898b1 | -4.07332 | -47.08683 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eff532b7-ecb5-3210-a8da-abbf3cc13dba | -6.08142 | -48.04803 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2af1a37-e66b-35f5-b687-1b80d5df1f14 | -2.79485 | -51.89967 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc109922-c888-3b58-90a8-2b440beb4c89 | -5.48233 | -44.07325 | 2024-12-02 04:25:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b7daff9-6b95-3bd7-90fe-8ce20887ff82 | -3.70067 | -47.12107 | 2024-12-02 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c1493f4-e763-3f2c-b3ce-0415d93b56d0 | -4.48793 | -46.05503 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 37e8b20d-dedb-31f5-8b10-c3921c19a49a | -2.71309 | -52.00502 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d783a56-d941-3833-bcc4-5a6640c81a5b | -3.29212 | -53.83762 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab3f005e-b9d1-3a5d-b2cb-1c02465d21d9 | -4.17206 | -48.20102 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fb5c3d3-9789-3968-92f1-75e66d408ca8 | -10.70292 | -44.97404 | 2024-12-02 04:25:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c42966e8-f9e5-3582-b6e2-2888f3c4df66 | -3.41537 | -54.63945 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 227c6c9a-1c62-3d67-8b81-759c9309ba29 | -3.31302 | -53.86833 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 369d5359-5b09-3361-b7cc-50e0f792308e | -4.27891 | -50.68158 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba02260b-a50a-37f6-9a8e-a7d436bd02bc | -3.50875 | -53.82786 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c50cec6-24c1-3f01-b16e-76aa66ba2a47 | -3.86258 | -50.89536 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86d52a73-d3db-3e0a-8d5c-42ae5cf8f444 | -4.75085 | -38.47069 | 2024-12-02 04:25:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b7ee8c20-55cd-345d-82eb-b2ad5527f7d8 | -3.06705 | -53.68331 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b695b861-2f19-30b4-9a4e-276896af93b7 | -10.6593 | -44.49374 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c45bd64e-053d-3a56-a62c-4ff8c0526b8e | -4.06937 | -47.08987 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d15acc6-afe0-38dc-8c95-132a4dd52d4f | -4.05206 | -46.82039 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cc79cb6-9388-31d3-aad4-34095b5b14bb | -4.92239 | -48.42706 | 2024-12-02 04:25:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 220f95bb-4139-30f3-a6c3-c4bb5376634d | -5.60783 | -43.47276 | 2024-12-02 04:25:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed77ec54-f305-3e8c-a7c0-df2311130063 | -3.28491 | -50.79263 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b251679-f574-37dd-9ac9-e1e1253f9089 | -4.3221 | -48.2117 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 852ba029-edd9-3d07-8e29-7a186bcac6ba | -9.19202 | -45.35076 | 2024-12-02 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ed2b8d1-600e-31aa-b660-794372cffd10 | -4.58737 | -50.60359 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 332cd9c6-7d72-3331-b86f-31dc3d198fb9 | -3.26634 | -53.62805 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8459128e-2a3a-37ab-8652-2e1523ae2e78 | -3.40128 | -50.22542 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cb98c68-26ac-3551-bd09-9efd14a33956 | -4.05257 | -50.95173 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c2b78d8-3b10-31b4-b568-3a52af5dd4b0 | -4.09393 | -46.12464 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef8ce8a4-0880-3aa0-8aa9-2d94b26a7289 | -4.06102 | -46.67711 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4735e278-f98a-3f05-8d31-40fc3110a413 | -6.24433 | -47.29297 | 2024-12-02 04:25:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af1a3dee-6ee4-3fa0-9fa7-693c3a5c789c | -3.74357 | -52.26324 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0b00743-c19f-3981-ae7c-c87f9f2198e8 | -3.86696 | -52.39333 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23006a35-3084-32d7-bae2-16576276b40c | -4.99633 | -41.31787 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a1f44325-900e-3739-a684-5646c1ea7e35 | -4.49536 | -45.70572 | 2024-12-02 04:25:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f00aa960-11ca-3a20-b836-3b2d3e6b5d11 | -3.95659 | -46.50272 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 150c356e-33b6-326e-9492-1dd43bb1e0c3 | -4.56661 | -45.46888 | 2024-12-02 04:25:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f4be626-0286-3a87-85d5-009fd0885eef | -2.88925 | -54.16082 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2700f985-04b0-368e-b6d8-fdaea1cb97db | -3.10353 | -49.45743 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 138083d9-62b5-3f58-8956-ba957b498f5b | -3.93528 | -46.9189 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e861c64-0b0b-3e7f-afa5-3759107758f1 | -3.68159 | -50.24475 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e3b00d8-b357-3858-b261-be1b88b39acf | -3.33735 | -51.52431 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c839180-748c-3ce5-b15b-b8e6cd182514 | -2.57793 | -53.67529 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96c43f01-f3c2-3e55-9818-c7360d9b8ffa | -2.70858 | -52.00428 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15d40cc8-1fd8-347d-af42-7d858988070e | -4.81758 | -44.35268 | 2024-12-02 04:25:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c063a03a-67f7-37dc-9248-4fcbeacb6cb0 | -2.75217 | -51.75122 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bba5374-26c0-3e7c-93e2-e6a60d788367 | -3.24624 | -50.77116 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20e1b506-e3db-3026-bb55-b3d1fa64644c | -4.26806 | -50.85013 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1aa32cf2-6826-317a-b1cb-ba8301f0beeb | -5.58381 | -45.14851 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 4d7242e5-a8c5-3334-a80a-86db284049ff | -3.30302 | -50.03771 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18b4b47a-ff3d-3d30-8c76-16702726128e | -6.37369 | -47.354 | 2024-12-02 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d721cca-789d-3978-b5e4-6093e1af4b93 | -5.17034 | -44.80291 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f5f4b2a3-386f-3ea6-908f-1f4cd29caa64 | -4.08739 | -46.20893 | 2024-12-02 04:25:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da916dbe-8abc-3da7-9e87-39dc89a848fb | -4.05598 | -46.81738 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 514eaa6b-7809-3f02-b8c0-3969521b2fe4 | -3.26541 | -53.63372 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3eacffa-1c3e-37fd-895e-69bb4ffc3927 | -6.4043 | -47.21685 | 2024-12-02 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 780c895c-5d7b-31b4-807f-6fcf69877620 | -4.30843 | -48.22943 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 842c20c6-74ee-3363-a674-0e788a9805f9 | -4.5779 | -43.35259 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e82aef71-002a-3d96-8d31-c673c6889e64 | -3.9354 | -46.7226 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd13f86c-3b84-36a6-b985-625f5358aaf7 | -3.43259 | -53.89087 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 26a89e91-d7f9-3dfc-9229-9c53f749aafc | -3.75622 | -52.32606 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a4a659-9519-36f9-9b1b-bcc1e872593c | -2.82402 | -54.19584 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74f22a47-a709-3d61-b600-82ad80b92678 | -3.86401 | -46.88953 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9ba741b-4830-31d5-92e8-128dd02bcb89 | -4.31447 | -48.21442 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a5c7801-d934-30b6-bd0b-fbc522e9f346 | -2.90228 | -51.37138 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fafc401-f111-3629-b16f-531f9a09e77f | -4.32998 | -45.92068 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d81399b9-2a10-3ad5-85b5-4fbf7614cd36 | -3.42753 | -53.88993 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 493bddde-f298-335b-a7cd-343cdf17a91d | -3.46639 | -50.26361 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README42.md)
