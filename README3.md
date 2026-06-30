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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebf88202-24af-3aa6-816a-e8d241b1b1c1 | -17.712 | -46.7798 | 2026-06-30 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f6b90c0a-c25b-3df4-8926-01bee349d6ee | -13.2452 | -56.7965 | 2026-06-30 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 34b81b77-c657-356f-9b8d-86e4e70088a6 | -6.3135 | -43.6411 | 2026-06-30 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| aad7fbbb-ccb6-3e99-a364-18ecbd8c7cc2 | -13.2643 | -56.7947 | 2026-06-30 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 286271d0-eb59-3531-84ad-566becfa33ac | -12.4464 | -58.4825 | 2026-06-30 00:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c375781b-b067-3470-8975-6da325b4094b | -9.6037 | -56.9276 | 2026-06-30 00:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1ae668af-f582-3918-a49c-7aef259e508d | -7.4309 | -49.8729 | 2026-06-30 00:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8d767ac9-ca31-30ec-a522-a209d39d90fc | -12.8543 | -44.386 | 2026-06-30 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a054c97e-3cf7-39b0-b979-25b3e3885fae | -10.9401 | -43.0355 | 2026-06-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 8e0e1ca2-ab72-3e87-aeef-bdeee5c903b9 | -11.2277 | -54.3241 | 2026-06-30 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| d59ddfd2-3c75-3e34-9066-65f0f17d6f85 | -12.8552 | -44.3389 | 2026-06-30 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| fce4cbee-f568-34ae-85a0-3a8216b9a9ed | -13.2643 | -56.7947 | 2026-06-30 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| b159e0ce-4c20-3a36-93e2-b40aa3a1fa60 | -11.2279 | -54.3036 | 2026-06-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 6a7fbf08-0a8d-3680-94a3-e13316a85a8c | -13.2452 | -56.7965 | 2026-06-30 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f2808f84-cf10-37a8-a1af-5808b7e55379 | -12.8543 | -44.386 | 2026-06-30 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 8b1b671b-95cd-37b3-b42d-e523c842161a | -10.1388 | -52.4017 | 2026-06-30 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| cae7f87e-cb5c-3887-9bf9-d94b52e29c4f | -10.9401 | -43.0355 | 2026-06-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 0f696e4a-84b0-380b-ae60-7f0cfc4cf29c | -9.6037 | -56.9276 | 2026-06-30 00:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 9b7eb71a-4779-36d5-bbab-00913880d808 | -12.4464 | -58.4825 | 2026-06-30 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 27ce1610-fc96-33b9-ba19-f35ac704b1d5 | -17.712 | -46.7798 | 2026-06-30 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 19a5033a-981e-335f-ad04-65e05e93bebd | -11.2277 | -54.3241 | 2026-06-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| a1285874-ec2d-373a-a166-32f675afbc42 | -12.4462 | -58.5023 | 2026-06-30 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| d8be86a8-addd-35e4-a711-5bde5bb11064 | -7.4309 | -49.8729 | 2026-06-30 00:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| cf8b837e-62ad-3193-b1b0-657239624749 | -13.2452 | -56.7965 | 2026-06-30 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| cf47acee-f05c-3a9d-bfc4-bcaba9f4a297 | -13.2643 | -56.7947 | 2026-06-30 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ee969231-ed06-3cff-aaae-1230301b6c70 | -11.2277 | -54.3241 | 2026-06-30 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 40216af5-260b-38bf-a88d-437da26c3ad9 | -10.1388 | -52.4017 | 2026-06-30 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e898bce9-2927-3253-80b3-770ecb77aa4e | -12.8552 | -44.3389 | 2026-06-30 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e210bbb1-c017-3e2a-a2e2-1248af53f120 | -9.6037 | -56.9276 | 2026-06-30 00:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e0a104ff-faa4-3b1a-96ac-3dd4555c1a2b | -10.9401 | -43.0355 | 2026-06-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| ca328eab-99d2-3e24-93e5-799aa2f1e40d | -7.4309 | -49.8729 | 2026-06-30 00:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 562e352f-c8a4-3ab6-872b-c67302b03bfa | -11.2279 | -54.3036 | 2026-06-30 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 554c9f7b-04fe-3f4a-b1ce-de94421cef5e | -12.8543 | -44.386 | 2026-06-30 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 3a6357ed-22a0-3a1d-989a-74945393e2f6 | -17.712 | -46.7798 | 2026-06-30 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 6383600b-6d48-3723-994a-60d282c6c425 | -12.4464 | -58.4825 | 2026-06-30 00:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f6ba35b5-ccde-3ad4-9486-70edf1b3d588 | -12.8552 | -44.3389 | 2026-06-30 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| bb1fc85a-5f3c-3d8f-bbfc-d1a04ab53897 | -17.712 | -46.7798 | 2026-06-30 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1399a947-5700-3e46-a8d3-62b54d851303 | -12.4462 | -58.5023 | 2026-06-30 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 87b61790-89e2-31db-892d-db4495ea33c0 | -9.6037 | -56.9276 | 2026-06-30 01:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 794abd66-0939-3c9f-bfda-221de021738f | -10.9401 | -43.0355 | 2026-06-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 08286f55-6834-3efb-8949-fc4c3530c76c | -12.4464 | -58.4825 | 2026-06-30 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 95e7e1da-a38e-3d0a-9447-3fd29ced3f4c | -11.2279 | -54.3036 | 2026-06-30 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| be23697c-f453-30da-a1c1-bc4c574ba185 | -11.2277 | -54.3241 | 2026-06-30 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 695acdca-2048-3352-8d21-e3cc53e5bdd5 | -13.2643 | -56.7947 | 2026-06-30 01:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| cfcdee37-27f6-3e25-b375-344810a80ca6 | -12.8543 | -44.386 | 2026-06-30 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 6ce7f3f5-f51a-3b59-a9fa-56116d01e10b | -10.1388 | -52.4017 | 2026-06-30 01:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| e1cc1e9e-59e5-30a9-9756-9c336a08cf2d | -13.2452 | -56.7965 | 2026-06-30 01:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d1a26ce4-c8b7-3f24-a544-baf33596cf92 | -13.2643 | -56.7947 | 2026-06-30 01:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 58356885-712f-3de9-b05c-7949a6a64330 | -12.4464 | -58.4825 | 2026-06-30 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 4b994b76-5a06-34c1-abed-f7a8d5417095 | -9.6037 | -56.9276 | 2026-06-30 01:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 4c67bf24-2a91-358c-9c98-4bd84c893e21 | -13.2452 | -56.7965 | 2026-06-30 01:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c77911a0-d7ec-3370-b398-1f556c84488c | -17.712 | -46.7798 | 2026-06-30 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9aea2799-3953-34b9-809f-132b44ab3d6e | -11.2277 | -54.3241 | 2026-06-30 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7f236d4f-1756-3474-a1d2-9b8ba997cc67 | -11.2279 | -54.3036 | 2026-06-30 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d9a03c00-bfce-36cf-8830-7ec9759254d8 | -10.9401 | -43.0355 | 2026-06-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ef8f50da-7c55-3dc3-98aa-ab3bfceaac1e | -13.2452 | -56.7965 | 2026-06-30 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b549730e-f88d-3c78-8bdd-07b91a0435cb | -12.4464 | -58.4825 | 2026-06-30 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 231cbcb6-8b5b-3b28-b823-0338c242ce2f | -9.6037 | -56.9276 | 2026-06-30 01:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 320ffee0-9da3-3aa1-ae11-2ac005e89b20 | -11.2277 | -54.3241 | 2026-06-30 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ec7df37f-7f62-3bff-8fba-3e5f3f27b00c | -11.2279 | -54.3036 | 2026-06-30 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 2717bf8d-3068-32c5-b076-3c533cea1b4b | -17.712 | -46.7798 | 2026-06-30 01:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| ee51773e-c82f-379d-9b26-b82ee419334f | -10.9401 | -43.0355 | 2026-06-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9b1e825c-cfab-3eb7-a1c3-6a19d4b0f885 | -13.2643 | -56.7947 | 2026-06-30 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| c5f14a35-a295-3e46-8eaa-7bbe5ad189f7 | -13.2643 | -56.7947 | 2026-06-30 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 608b7719-9e67-3da5-b2d8-7068f2dec213 | -9.6037 | -56.9276 | 2026-06-30 01:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 569ff4cc-cd78-3831-8704-78ba60daaf88 | -17.712 | -46.7798 | 2026-06-30 01:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6c2d5f5c-be1c-3bb6-98ac-a6ab7cc81800 | -11.2277 | -54.3241 | 2026-06-30 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 80085a1a-69df-30db-94a8-a5c1b0d7f2ad | -10.9401 | -43.0355 | 2026-06-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| af25643c-8579-33a0-a867-6733bf453a56 | -13.2643 | -56.7947 | 2026-06-30 01:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 93ae0965-51c7-330e-85d7-6e582cfeb78f | -9.6037 | -56.9276 | 2026-06-30 01:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 01594761-d3c0-34c9-aa1d-0a670a3890e1 | -12.4464 | -58.4825 | 2026-06-30 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e11fd6a8-7596-3ea1-9db2-48c91050a951 | -17.712 | -46.7798 | 2026-06-30 01:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b7bb902d-1747-32fc-9c16-dae5b8f3d866 | -10.9401 | -43.0355 | 2026-06-30 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 0c836458-57bb-3801-8a6a-a84c41ab6fb5 | -17.712 | -46.7798 | 2026-06-30 01:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 705c3b82-437c-3ef1-a0b2-ca4a09e2549b | -10.9401 | -43.0355 | 2026-06-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 3050f04c-0df0-3142-83ec-30fe7bda88f3 | -12.4464 | -58.4825 | 2026-06-30 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 3a277705-8fd9-3754-816c-6ab3f6d6a22c | -13.2643 | -56.7947 | 2026-06-30 01:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c9345a34-4e70-396d-b847-059913374202 | -17.712 | -46.7798 | 2026-06-30 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| d3d7cdcc-6ffe-365f-9857-de0beb31abae | -13.2643 | -56.7947 | 2026-06-30 02:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 81182e14-c19b-386c-ac5e-af5eb21e5ba7 | -9.6037 | -56.9276 | 2026-06-30 02:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f9b87380-fa94-3ed3-9002-2d71b941b579 | -12.4464 | -58.4825 | 2026-06-30 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| e6383e29-031b-3bdb-a86d-e6ea81a871e9 | -9.6037 | -56.9276 | 2026-06-30 02:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e2328bf7-b6de-3f43-b0f4-71f14c7b5bf0 | -9.1933 | -45.3114 | 2026-06-30 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 382fc8bc-f68d-3b18-8a29-b5229c547021 | -10.9401 | -43.0355 | 2026-06-30 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c8ede7c9-b302-3c96-af2e-730b30ede3e8 | -13.2643 | -56.7947 | 2026-06-30 02:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 61030401-5784-324d-ab6b-0dab6d2d584a | -9.193 | -45.3342 | 2026-06-30 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f39a02c9-6821-3dcb-8e3e-a30abacd27fe | -13.2643 | -56.7947 | 2026-06-30 02:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 6bb5c1af-3f48-3263-995e-cc3bd7b968cb | -9.1933 | -45.3114 | 2026-06-30 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 845e6561-cbd7-3a48-a8fe-b7602ce36975 | -10.9401 | -43.0355 | 2026-06-30 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 885edb66-a002-30cf-85a4-e7b9094d5003 | -12.4464 | -58.4825 | 2026-06-30 02:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 4e9118d5-88db-34e7-b5c2-9145f57f4e25 | -9.6037 | -56.9276 | 2026-06-30 02:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f4b067a4-f2a0-3058-8e15-17aec96a8074 | -10.9401 | -43.0355 | 2026-06-30 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| f2272d97-6d7b-3923-8b25-f2698ebead84 | -9.1933 | -45.3114 | 2026-06-30 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 52de5e9e-3440-339f-9249-cf530ec90a9c | -9.193 | -45.3342 | 2026-06-30 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 89caa91b-1e3a-3718-80a9-9c0a42fcd63b | -13.2643 | -56.7947 | 2026-06-30 02:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b7ce82c3-6ef3-3865-89e0-ee7bfd9890ba | -12.4464 | -58.4825 | 2026-06-30 02:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 46966863-f671-38bf-855a-b6596fe471c3 | -13.2643 | -56.7947 | 2026-06-30 02:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 662c53ec-2c7e-34d6-98cf-6a454da6f304 | -10.9401 | -43.0355 | 2026-06-30 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| abcbc8b6-1031-3166-908b-0f7ab1999f65 | -7.4309 | -49.8729 | 2026-06-30 02:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| dbe5ddb2-ebcf-3b65-bb65-aaa688f51d8a | -7.4309 | -49.8729 | 2026-06-30 02:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |


[Clique aqui para ver as próximas entradas](README4.md)
