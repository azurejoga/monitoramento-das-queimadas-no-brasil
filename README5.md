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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fa804be-bdd7-3627-a5de-437528f630b4 | -8.04023 | -39.69397 | 2025-11-10 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c6a98b0a-a85e-3add-8780-43185bab3729 | -5.10598 | -40.73197 | 2025-11-10 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 55750177-1c91-31e3-974d-671cc06958e3 | -2.97054 | -40.03065 | 2025-11-10 03:57:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d7d96a50-0d1e-3c0a-baeb-6cc58dca1712 | -2.44505 | -49.33673 | 2025-11-10 03:57:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 181f6e1a-506c-385f-869a-0a965372c42a | -3.27941 | -51.12255 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 049ae576-f8ca-30ae-abd0-20fa8835aad1 | -4.07337 | -44.13098 | 2025-11-10 03:57:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ecfe1e8-5ffe-3b9d-a837-883634a0676e | -4.64172 | -49.59452 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 401e089f-d579-3a3d-91eb-20ffad7e41d9 | -4.15104 | -38.48186 | 2025-11-10 03:57:00 | NPP-375D | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 33dbe154-c619-3ad0-af31-ee1cb5c82b07 | -4.20116 | -50.6325 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b555d518-b334-35f7-8c0f-d597d4e08728 | -2.60475 | -49.22434 | 2025-11-10 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| acaef8e4-bf1a-3977-aab5-ae0875a0bc69 | -2.97211 | -47.89956 | 2025-11-10 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cfc41be-7c71-363c-88f7-2a228f4cc9b3 | -4.91622 | -46.73349 | 2025-11-10 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a477fc6-4dd4-3263-b7cd-173bb47c5940 | -6.85866 | -40.15878 | 2025-11-10 03:57:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7e8c358f-e09e-3b97-a3db-3468c93ced62 | -3.31744 | -50.10418 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 439d235f-e09a-3778-b2bc-eb71bc13e546 | -3.69509 | -50.19365 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0b0ce97a-b64b-34ca-b6a9-933e14146d65 | -5.19176 | -46.15474 | 2025-11-10 03:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f300c487-bfb0-3ea6-aa78-a4a09bfea273 | -2.43953 | -49.33633 | 2025-11-10 03:57:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcabfe5a-e627-36fa-bc6a-68ce64058545 | -4.74839 | -49.50327 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58e429e4-b55b-3e37-952b-75e7af79d0c2 | -8.04563 | -39.69479 | 2025-11-10 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eebd674d-813c-39da-97f2-839fa37a6033 | -5.12906 | -44.72749 | 2025-11-10 03:57:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aaae0816-bcf0-351c-ad47-73864131c630 | -3.10154 | -50.3229 | 2025-11-10 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7171ef0e-4bc4-376e-b312-903636fdc9e8 | -2.96632 | -47.89854 | 2025-11-10 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ea2d8d0-7d7d-3aed-a5c9-6d4ee447d939 | -5.15083 | -50.87898 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78d7d4a2-c51b-3cb6-9461-3d7fe2102c28 | -4.67785 | -45.69166 | 2025-11-10 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f82113b-50ca-3f1d-ae52-a94aa7d2b08a | -4.91465 | -44.88663 | 2025-11-10 03:57:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6b9923a-8594-3ad5-95ae-e9423b62f5da | -4.11299 | -38.44673 | 2025-11-10 03:57:00 | NPP-375D | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aa04982f-8232-3318-910c-2e7c9a8dc75e | -3.45058 | -50.47747 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4958c4a6-b5f8-3ecf-a0ee-8ed009c96ad4 | -4.58363 | -46.66627 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 391a4efa-e2c3-3794-8587-99268d7dc6c0 | -3.69385 | -50.18848 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 94033ed6-fb2c-3da8-b55e-ac7ad1c122e4 | -4.11652 | -46.12469 | 2025-11-10 03:57:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b059c79-6bd4-3e20-977f-45c08b6d5a9b | -3.10253 | -50.19659 | 2025-11-10 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f07f97f1-3a5c-34e0-9377-e6816e868bae | -4.85664 | -45.78706 | 2025-11-10 03:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a6060f3-a25f-359e-8390-32c68142dd14 | -2.99033 | -40.3803 | 2025-11-10 03:57:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 86f8fd1a-6e27-332d-9b5e-38f669dc6fd4 | -3.40557 | -50.45732 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5868d613-47dc-3fa6-a6d1-1124c500dd0d | -3.70046 | -50.18958 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e81418ba-a675-36b0-a5dd-8b79bebac540 | -4.64882 | -46.34192 | 2025-11-10 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1dff4c9-85fb-3fb2-b72e-312f0f9cf7b1 | -4.10625 | -47.28686 | 2025-11-10 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7008a496-0a7e-3d09-8e2c-39c55f380f9d | -3.40452 | -50.44999 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ea0bb8f-5df6-3102-a168-1a58a0673851 | -7.8138 | -41.95642 | 2025-11-10 03:57:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5782f41e-8573-38ae-9f6e-e240793a0c74 | -5.76038 | -40.79194 | 2025-11-10 03:57:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9cc18f63-ae75-3b1e-b4d1-875588f7b47b | -6.86207 | -40.15932 | 2025-11-10 03:57:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b99e163-11c7-322d-9159-61cbd7864826 | -4.58254 | -46.67274 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5af9903-e965-33c6-96c1-76f6d6e95037 | -5.37768 | -44.72331 | 2025-11-10 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5670b7a4-7afa-3368-be64-873ce5a3aa5a | -4.53912 | -45.78308 | 2025-11-10 03:57:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dcc955c8-c362-37a4-8fdc-aae7231348cf | -2.92082 | -45.29155 | 2025-11-10 03:57:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0086b573-0683-3013-be7c-4a1d16f8e989 | -3.03778 | -49.49253 | 2025-11-10 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5b3fca9-8aab-37d7-bec8-00596ea0b9b0 | -4.53425 | -45.7821 | 2025-11-10 03:57:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fac58e00-65c3-3438-a29e-5401c256bacb | -3.76559 | -43.97871 | 2025-11-10 03:57:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 070a2fcb-0ef2-3b2c-b814-0bda2017a259 | -5.36891 | -44.72853 | 2025-11-10 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba9c1ae8-9e39-3817-a4b1-206867640036 | -4.58253 | -45.54172 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b89afb86-d083-383c-a5a0-fbbac432ccc3 | -7.90393 | -39.71961 | 2025-11-10 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d23b29f8-ba65-33e5-9d6a-b713f6f0f2db | -2.29364 | -47.87243 | 2025-11-10 03:57:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68983a7f-c55d-333b-a556-ee8c02c2d1e9 | -2.44502 | -49.34264 | 2025-11-10 03:57:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4229bcbf-cba2-3a16-b4b8-ab60700f2455 | -4.20007 | -50.63868 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 437a337c-9c58-33c4-b65e-69833f5a6a6c | -3.09486 | -50.32158 | 2025-11-10 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b996c8d-5930-3b80-be4b-7e93df924554 | -6.92447 | -44.13788 | 2025-11-10 03:57:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b871ba5-2798-3ac2-aade-c54186728376 | -7.56055 | -41.37196 | 2025-11-10 03:57:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee72ed18-d1e8-3147-ae2f-d0c045b3b654 | -4.68012 | -45.85384 | 2025-11-10 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 817a4977-1451-3a68-aebc-b534c9ba0e7b | -5.14891 | -50.87918 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d138dbe5-4c6f-3261-bc1a-8c90ce257458 | -8.08929 | -43.64878 | 2025-11-10 03:57:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 010ee3ce-4fae-3ab6-a207-0dea95def49f | -4.91049 | -44.88743 | 2025-11-10 03:57:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f6b01a3-f25b-3968-88f0-a5f7694129be | -8.04357 | -39.6945 | 2025-11-10 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 764a2b77-6118-3b13-8698-56473f653d31 | -5.22273 | -45.03274 | 2025-11-10 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f188ff91-be00-377e-a7fb-c7e5420692f3 | -7.88235 | -48.38974 | 2025-11-10 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19d9d769-07ea-37c8-8be8-a55df116fc7c | -4.20683 | -50.63968 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 45362d8a-6270-3fb5-84eb-034124db6b2f | -4.52428 | -40.35787 | 2025-11-10 03:57:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1df19e14-58d5-3646-8b43-5351beb1e5e3 | -4.11234 | -47.28413 | 2025-11-10 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49cae105-c094-35d3-a599-a1abd52eed97 | -5.37244 | -44.72711 | 2025-11-10 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef534aa4-309e-3ea8-8c10-20f5e92eca6e | -4.11602 | -46.1277 | 2025-11-10 03:57:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aea62120-698a-389f-9970-deba5f33502b | -4.61645 | -46.66172 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6fbebfe-e4b2-3509-88db-46369622caf5 | -4.91675 | -46.73048 | 2025-11-10 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 906b5b9e-2324-347a-9993-591ead866082 | -4.75032 | -49.5079 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f7ecd67-00ab-3c9b-8a00-5f9ab50858d3 | -4.57609 | -45.54167 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 13057445-13fa-340e-8d62-554c26578875 | -5.37869 | -44.7254 | 2025-11-10 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b411330-5280-3c47-98a8-c97b3aaf842e | -7.047 | -47.36607 | 2025-11-10 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52e6ca66-b10c-3e7e-b8f5-ec97f5d409a7 | -2.99413 | -48.05526 | 2025-11-10 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7ad650f-ea6a-3f95-977a-053d1ca3ab35 | -4.91501 | -46.73577 | 2025-11-10 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab6abc58-cfc3-398a-97a8-9a1c3d26d514 | -2.33896 | -47.03348 | 2025-11-10 03:57:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 375f39a5-897d-37d8-a0d1-58445084d6dc | -3.22407 | -48.78936 | 2025-11-10 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01119b3e-98f9-3cf7-a493-f9264c48482d | -4.61125 | -46.66092 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 945c4cf6-f607-3a72-9598-cdb2a46aa3f5 | -5.48602 | -44.38989 | 2025-11-10 03:57:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8855f248-cf84-3cb4-8eb1-1251606a1b4d | -5.92623 | -43.93151 | 2025-11-10 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f492a83c-21ff-39ea-960e-8bd0c1ed7bb5 | -5.3717 | -44.73159 | 2025-11-10 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7160bebf-fc7c-3d6c-a77a-8c8e9fd3ff1e | -4.25942 | -46.71019 | 2025-11-10 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c31eb2f3-7b6a-38b5-960e-e448f8a494ed | -4.75118 | -49.50299 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2697483-a628-3e3f-adc6-b64356ee8b46 | -3.8089 | -51.09645 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67c367c8-3ea7-38dc-a3c7-09f8635f9f99 | -3.31839 | -50.09865 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c1327cd-d8bb-34c2-8b62-a22b28a6c361 | -4.53778 | -45.78171 | 2025-11-10 03:57:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06cb13ac-5fa8-34c2-b123-72b40b15ab04 | -2.83213 | -48.65977 | 2025-11-10 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 270f1124-8e82-3e75-b103-813929e13a43 | -5.89019 | -43.9655 | 2025-11-10 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb907e3d-5cb6-3d60-af47-04896dc51a58 | -4.11782 | -47.28491 | 2025-11-10 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df330294-aa77-34a5-b933-a41c9b15589d | -1.31496 | -48.89728 | 2025-11-10 03:57:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3458198f-cf88-365c-97c4-6bcf3ed63c9b | -8.70887 | -41.13411 | 2025-11-10 03:57:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c5a3eda-1560-38f9-a3d6-653d6d610d50 | -3.3411 | -39.99575 | 2025-11-10 03:57:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c58f3c62-ea18-33d6-8598-570dadb5f5da | -5.18258 | -43.44503 | 2025-11-10 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc0e9397-f9a1-3598-8c01-569a0f510d87 | -4.58088 | -45.54258 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 46a00918-aea4-3b47-8e42-2e885335c602 | -6.54872 | -44.46612 | 2025-11-10 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23d4e168-a089-3d30-8222-d809f6f317ba | -3.14399 | -50.27596 | 2025-11-10 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5820b9ac-dd7e-312f-9a7a-6f3ce0e57850 | -6.72219 | -34.99599 | 2025-11-10 03:57:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 370346d5-f076-3d68-a004-04fa3e2581e3 | -4.5943 | -45.55092 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README6.md)
